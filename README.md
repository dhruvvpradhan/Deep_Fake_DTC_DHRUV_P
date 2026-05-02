# Deep_Fake_DTC_DHRUV_P
This project is a Deep Learning-based Deepfake Detection System that analyzes videos and determines whether they are REAL or FAKE. It works by extracting frames from a video and using a Convolutional Neural Network (CNN) to classify each frame, followed by an aggregated prediction.
🔍 Overview

This project is a Deep Learning-based Deepfake Detection System that analyzes videos and determines whether they are REAL or FAKE. It works by extracting frames from a video and using a Convolutional Neural Network (CNN) to classify each frame, followed by an aggregated prediction.

⚙️ How It Works (Step-by-Step)
🎥 Input Video Upload
User uploads a video through a web interface
🧹 Frame Extraction
Video is split into multiple frames using OpenCV
🧠 Model Prediction
Each frame is passed through a trained CNN model
📊 Final Decision
Predictions are averaged → output is:
✅ REAL
❌ FAKE
🛠 Tech Stack
Programming: Python
Libraries: TensorFlow, Keras, OpenCV, NumPy
Frontend: HTML
Backend: Flask
🚀 Features
Video-based deepfake detection
Frame-by-frame analysis
Lightweight CNN model
Simple web interface for testing
📊 Output
Binary classification: REAL / FAKE
Based on average probability across frames
🎯 Use Cases
Social media content verification
Fake news detection
Digital forensics
Cybersecurity applications
🔮 Future Enhancements
Use ResNet / EfficientNet for higher accuracy
Integrate face detection (MTCNN)
Add LSTM for temporal learning (video patterns)
Deploy using Streamlit / Cloud (Render, AWS)
