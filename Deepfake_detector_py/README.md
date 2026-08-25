# Deepfake Detection System

A deep learning-based web application that analyzes videos and predicts whether the uploaded video is **REAL** or **FAKE** using a Convolutional Neural Network (CNN).

The system extracts frames from an uploaded video, preprocesses them, classifies the frames using a trained CNN model, and combines the frame-level predictions to produce the final video-level result.

## Features

* 🎥 Upload videos through a web interface
* 🖼️ Extract and analyze video frames using OpenCV
* 🧠 CNN-based deepfake classification
* 🔍 Frame-level prediction
* 📊 Aggregated prediction for the complete video
* 🌐 Flask-based web interface
* 🐍 Python-based deep learning pipeline

## How It Works

```text
User uploads video
        ↓
    Flask Server
        ↓
   Video Processing
        ↓
   Frame Extraction
        ↓
      Preprocessing
        ↓
      CNN Model
        ↓
 Frame-level Predictions
        ↓
 Prediction Aggregation
        ↓
   REAL / FAKE Result
```

### Workflow

1. The user uploads a video through the Flask web interface.
2. The application reads the video using OpenCV.
3. Selected frames are extracted from the video.
4. Each frame is preprocessed into the format expected by the CNN.
5. The trained CNN model predicts whether each frame is real or fake.
6. Frame-level predictions are aggregated.
7. The application displays the final **REAL** or **FAKE** prediction.

## Tech Stack

| Technology         | Purpose                               |
| ------------------ | ------------------------------------- |
| Python             | Core programming language             |
| TensorFlow / Keras | CNN model development and inference   |
| OpenCV             | Video processing and frame extraction |
| NumPy              | Numerical and array operations        |
| Flask              | Backend and web application           |
| HTML               | Frontend interface                    |

## Project Structure

```text
Deepfake-Detector/
│
├── Deepfake_detector_py/
│   ├── templates/
│   │   └── index.html
│   │
│   ├── utils/
│   │   ├── predict.py
│   │   └── preprocess.py
│   │
│   ├── app.py
│   ├── train.py
│   ├── requirements.txt
│   └── README.md
│
└── README.md
```

### File Description

**`app.py`**
Flask application responsible for handling the web interface, receiving uploaded videos, running prediction, and returning the result.

**`train.py`**
Contains the model-training pipeline used to train the CNN for real/fake classification.

**`utils/preprocess.py`**
Handles preprocessing of video frames before they are passed to the model.

**`utils/predict.py`**
Contains prediction logic used to classify frames and generate the final result.

**`templates/index.html`**
Frontend interface through which users can upload videos and view predictions.

**`requirements.txt`**
Contains the Python dependencies required to run the project.

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/dhruuvpradhan/deepfake-detector.git
cd deepfake-detector
```

### 2. Create a Virtual Environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Linux / macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r Deepfake_detector_py/requirements.txt
```

## Running the Application

Navigate to the project directory:

```bash
cd Deepfake_detector_py
```

Start the Flask application:

```bash
python app.py
```

The terminal will provide the local address where the application is running. Open that address in your browser and upload a video for analysis.

## Model Training

If you need to train the CNN model, run:

```bash
python train.py
```

Make sure the required training data and model configuration expected by `train.py` are available before starting training.

## Prediction

The prediction pipeline works at the frame level:

```text
Video
  ↓
Frame Extraction
  ↓
Frame Preprocessing
  ↓
CNN Prediction
  ↓
REAL / FAKE Scores
  ↓
Aggregated Video Prediction
```

This approach allows the system to use information from multiple frames instead of relying on a single frame.

## Limitations

Deepfake detection is a challenging computer-vision problem. The prediction quality depends heavily on:

* Training data quality and diversity
* Video resolution and compression
* Face visibility and pose
* Type of manipulation used to generate the deepfake
* Number and quality of extracted frames
* CNN model performance

Therefore, the output should be treated as a **model prediction**, not as definitive proof that a video is authentic or manipulated.

## Future Improvements

* Improve the CNN architecture and model accuracy
* Add face detection and face-region extraction
* Use transfer learning with models such as ResNet or EfficientNet
* Add temporal analysis across consecutive frames
* Display prediction confidence
* Support larger video formats and file sizes
* Add model evaluation metrics such as precision, recall, F1-score, and ROC-AUC
* Deploy the application using a cloud platform
* Add an API endpoint for programmatic video analysis

## Use Cases

Potential applications include:

* Social media content verification
* Digital media analysis
* Research and education
* Misinformation detection
* Video authenticity screening

## Disclaimer

This project is intended for **educational and research purposes**. Deepfake detection models can produce false positives and false negatives, so predictions should not be considered conclusive evidence of video authenticity.

## License

Add an appropriate open-source license before publishing this project for external use.
