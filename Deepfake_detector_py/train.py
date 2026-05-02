import os
import numpy as np
from tensorflow.keras import layers, models
from utils.preprocess import preprocess_image

data = []
labels = []

for label, folder in enumerate(["real", "fake"]):
    path = os.path.join("dataset", folder)

    for file in os.listdir(path):
        img = preprocess_image(os.path.join(path, file))
        data.append(img)
        labels.append(label)

data = np.array(data)
labels = np.array(labels)

model = models.Sequential([
    layers.Conv2D(32, (3,3), activation='relu', input_shape=(128,128,3)),
    layers.MaxPooling2D(2,2),
    layers.Conv2D(64, (3,3), activation='relu'),
    layers.MaxPooling2D(2,2),
    layers.Conv2D(128, (3,3), activation='relu'),
    layers.MaxPooling2D(2,2),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

model.fit(data, labels, epochs=5, batch_size=32)

model.save("models/model.h5")
