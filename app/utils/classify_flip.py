import torch
import torch.nn as nn
from torchvision import models, transforms
from PIL import Image
from pathlib import Path

# ---- Settings ----
MODEL_PATH = Path("models/flip_classifier.pt")
CLASS_NAMES = ["flip", "notflip"]
IMG_SIZE = 224
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")


# ---- Image preprocessing ----
transform = transforms.Compose([
    transforms.Resize((IMG_SIZE, IMG_SIZE)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
])


# ---- Load model once ----
def load_model():
    model = models.efficientnet_b0(weights=None)

    num_features = model.classifier[1].in_features
    model.classifier[1] = nn.Linear(num_features, 2)

    checkpoint = torch.load(MODEL_PATH, map_location=DEVICE)

    # Case 1: saved using torch.save(model.state_dict())
    if isinstance(checkpoint, dict):
        if "model_state_dict" in checkpoint:
            model.load_state_dict(checkpoint["model_state_dict"])
        else:
            model.load_state_dict(checkpoint)

    # Case 2: saved using torch.save(model)
    else:
        model = checkpoint

    model.to(DEVICE)
    model.eval()
    return model


model = load_model()


# ---- Prediction function used by app.py ----
def predict_flip(image: Image.Image):
    if image.mode != "RGB":
        image = image.convert("RGB")

    input_tensor = transform(image).unsqueeze(0).to(DEVICE)

    with torch.no_grad():
        outputs = model(input_tensor)
        probabilities = torch.softmax(outputs, dim=1)
        confidence, predicted_idx = torch.max(probabilities, dim=1)

    label = CLASS_NAMES[predicted_idx.item()]
    confidence = confidence.item()

    return label, confidence