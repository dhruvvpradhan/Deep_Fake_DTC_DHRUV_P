import numpy as np
from tensorflow.keras.models import load_model
from utils.preprocess import extract_frames

model = load_model("models/model.h5")

def predict_video(video_path):
    frames = extract_frames(video_path)
    preds = model.predict(frames)
    avg = np.mean(preds)

    if avg > 0.5:
        return "FAKE"
    else:
        return "REAL"
