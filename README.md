# CV Reader: End-to-End Accessible Document Reading System

End-to-end document accessibility system that detects page flips, extracts text using OCR, and converts content into speech.

## Live Demo

🚀 Web App: https://bal141-page-reader.hf.space

🤗 Hugging Face Space: https://huggingface.co/spaces/bal141/Page-Reader

## Overview

CV Reader is an end-to-end computer vision and speech synthesis system that converts document images into spoken audio.

The project combines:

* Deep Learning based page-flip detection
* Optical Character Recognition (OCR)
* Text preprocessing and cleanup
* Text-to-Speech (TTS) generation
* Interactive Gradio web application

The goal is to enable accessible document reading for visually impaired users and to explore real-world deployment of computer vision models.

---

## Problem Statement

OCR systems perform poorly when a document is in motion. Running OCR on a page that is actively being turned often produces unusable text.

This project introduces a preprocessing stage that first determines whether a page is currently being flipped before attempting text extraction.

The pipeline ensures that OCR and speech generation are only performed on stable document pages.

---

## Dataset

The project uses the page-flipping dataset.

The dataset consists of document images labeled as:

* Flip
* Not Flip

The objective is to classify a single image and determine whether a page is currently being turned.

---

## Project Pipeline

```text
Document Image
       │
       ▼
Page Flip Detection
(EfficientNet-B0)
       │
       ├── Flip
       │      └── Reject Processing
       │
       └── Not Flip
               │
               ▼
      OCR Text Extraction
               │
               ▼
       Text Cleaning
               │
               ▼
       Text-to-Speech
               │
               ▼
         Audio Output
```

---

## Model Development

Several architectures were explored and evaluated.

### Custom CNN

A baseline convolutional neural network was developed to establish initial performance benchmarks.

### ResNet50

Transfer learning was performed using ResNet50 to evaluate the effectiveness of deep residual networks for page-flip detection.

### MobileNetV2

A lightweight architecture optimized for mobile and edge deployment.

### EfficientNet-B0

EfficientNet-B0 achieved the best overall performance and was selected as the production model.

### DeepinderNet141 (Custom CNN)

A custom convolutional neural network designed and trained from scratch for page-flip detection.

---

## Final Model Performance

### EfficientNet-B0

Test Results:

| Metric    | Score  |
| --------- | ------ |
| Accuracy  | 99.66% |
| Precision | 99.67% |
| Recall    | 99.35% |
| F1 Score  | 99.51% |

Confusion Matrix:

```text
[[290,   0]
 [  2, 305]]
```

The model demonstrated near-perfect classification performance while maintaining a lightweight deployment footprint.

---

## OCR Pipeline

The OCR stage processes stable document pages using:

* Tesseract OCR
* OpenCV preprocessing
* Image normalization
* Noise reduction
* Text cleanup

OCR output is post-processed to remove:

* OCR artifacts
* Excess whitespace
* Invalid symbols
* Formatting inconsistencies

---

## Text-to-Speech Experiments

Multiple speech synthesis approaches were explored.

### Sesame CSM

Evaluated high-quality neural speech generation using:

* sesame/csm-1b

---

## Interactive Web Application

A Gradio interface was developed to demonstrate the complete pipeline.

Users can:

1. Upload a document image
2. Detect page state
3. Extract text
4. Generate audio narration
5. Download the generated speech output

---

## Technology Stack

### Machine Learning

* PyTorch
* TensorFlow
* TorchVision

### Computer Vision

* OpenCV
* Pillow

### OCR

* Tesseract OCR
* EasyOCR

### Speech Synthesis

* gTTS
* Sesame CSM

### Deployment

* Gradio
* Hugging Face Spaces

---

## Repository Structure

```text
CV-Reader/
│
├── app/
│   ├── app.py
│   ├── requirements.txt
│   ├── packages.txt
│   ├── models/
│   └── utils/
│
├── notebooks/
│   ├── CV-Reader.ipynb
│   └── texttospeech.ipynb
│
├── README.md
└── LICENSE
```

---

## Running Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Launch the application:

```bash
python app.py
```

The Gradio interface will be available in your browser.

---

## Future Improvements

* Multi-page document processing
* PDF generation
* OCR correction using Large Language Models
* Multilingual OCR support
* Neural speech generation using VibeVoice
* Mobile deployment
* Real-time document scanning

---

## Key Takeaways

This project demonstrates the development of a complete machine learning pipeline from dataset exploration and model training to OCR integration, speech synthesis and deployment.

The work highlights practical applications of deep learning, computer vision, OCR and generative AI in accessibility-focused software systems.

## License

MIT License
