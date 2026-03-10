

A deep learning application that detects brain tumors in MRI scans using MobileNetV2 and Streamlit.

## Overview

This project uses a pre-trained MobileNetV2 model fine-tuned on brain MRI images to classify whether a scan contains a tumor or not. It provides an interactive web interface for uploading and analyzing MRI images.

## Features

- 🧠 Brain tumor detection from MRI images
- 🎯 Uses pre-trained MobileNetV2 model
- 💻 Interactive Streamlit web interface
- 📊 Real-time prediction with confidence scores
- 🖼️ Support for JPG, JPEG, PNG formats

## Model Details

- **Architecture**: MobileNetV2 (transfer learning)
- **Framework**: TensorFlow/Keras
- **Input Size**: 224x224 RGB images
- **Output**: Binary classification (Tumor/No Tumor)

## Prediction Logic

| Score Range | Prediction |
|------------|-----------|
| < 0.4 | 🧠 Tumor Detected |
| 0.4 - 0.45 | ⚠️ Uncertain (needs medical review) |
| > 0.45 | ✅ No Tumor |

## Installation

### Prerequisites
- Python 3.9+
- pip

### Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/brain-tumor-detection.git
cd brain-tumor-detection


2. Install Dependencies:
pip install -r requirements.txt\

3. Run thee Streamlit app:
streamlit run app.py


.
├── app.py                              # Main Streamlit application
├── test.py                             # Testing script
├── brain_tumor_mobilenet_fixed.keras   # Pre-trained model
├── brain_tumor_dataset/                # Sample MRI images
├── requirements.txt                    # Python dependencies
├── README.md                          # This file
└── .gitignore                         # Git ignore file

Model Training
The model was trained on a brain tumor MRI dataset with:

Training samples: ~200 images
Classes: Tumor (Yes/No)
Data augmentation: Applied during training
Transfer learning: MobileNetV2 base weights
Dependencies
streamlit: Web framework for data apps
tensorflow: Deep learning framework
pillow: Image processing
numpy: Numerical computing
Deployment
Local Streamlit Deployment
⚠️ Important Note
This model is developed for educational and demonstration purposes only. It should NOT be used for actual medical diagnosis without proper validation and medical professional review. Always consult healthcare providers for medical decisions.

Future Improvements
 Add model accuracy metrics dashboard
 Implement confidence interval analysis
 Support for batch prediction (multiple images)
 Add image preprocessing visualization
 Create comparison with radiologist annotations
 Deploy on cloud platform (Streamlit Cloud)
Dataset
The model was trained on publicly available brain MRI datasets:

Brain Tumor Segmentation Dataset
Medical imaging datasets from research institutions
Technologies Used
Deep Learning: TensorFlow, Keras
Pre-trained Model: MobileNetV2
Web Framework: Streamlit
Image Processing: PIL (Pillow)
Numerical Computing: NumPy
License
This project is available under the MIT License.

Author
Created as part of an ML internship portfolio project.

References
TensorFlow Documentation
Streamlit Documentation
MobileNetV2 Paper
Brain Tumor Dataset
Contact & Support
For questions or issues, create an issue on the GitHub repository.
EOF

STEP 6: Initialize Git & Create First Commit
STEP 7: Connect to GitHub & Push
Replace your-username and brain-tumor-detection with your actual GitHub username and repo name:

Complete Command Sequence
Checklist
 Create GitHub repository
 Clone repo locally (if starting fresh)
 Create requirements.txt
 Create README.md
 Create .gitignore
 Run git init
 Add all files (git add .)
 Create first commit (git commit -m "...")
 Add remote (git remote add origin ...)
 Push to GitHub (git push -u origin main)
Would you like me to execute these commands automatically for you? I can create all the files and push to GitHub if you provide your GitHub URL.