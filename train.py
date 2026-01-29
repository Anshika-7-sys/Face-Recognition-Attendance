import cv2
import os
import numpy as np

recognizer = cv2.face.LBPHFaceRecognizer_create()
faces = []
labels = []
label_map = {}
label_id = 0

for person in os.listdir("dataset"):
    label_map[label_id] = person
    person_path = os.path.join("dataset", person)

    for img in os.listdir(person_path):
        img_path = os.path.join(person_path, img)
        face = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
        faces.append(face)
        labels.append(label_id)

    label_id += 1

recognizer.train(faces, np.array(labels))
recognizer.save("model.yml")

np.save("labels.npy", label_map)

print("Training completed")
