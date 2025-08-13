# utils/classifier.py
import cv2
import numpy as np

def load_model(class_file='classification_classes_ILSVRC2012.txt',
               model_file='models/DenseNet_121.caffemodel',
               config_file='models/DenseNet_121.prototxt'):
    """Loads the DNN model and class labels."""
    with open(class_file, 'r') as f:
        image_net_names = f.read().split('\n')
    class_names = [name.split(',')[0] for name in image_net_names if name.strip()]

    model = cv2.dnn.readNet(model=model_file, config=config_file, framework='Caffe')
    return model, class_names

def classify(model, image, class_names):
    """Runs classification and returns formatted result."""
    if image.shape[2] == 4:
        image = cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)

    blob = cv2.dnn.blobFromImage(
        image=image, scalefactor=0.017, size=(224, 224), mean=(104, 117, 123))
    model.setInput(blob)
    outputs = model.forward()

    final_outputs = outputs[0].reshape(1000, 1)
    label_id = np.argmax(final_outputs)
    probs = np.exp(final_outputs) / np.sum(np.exp(final_outputs))
    final_prob = np.max(probs) * 100.
    out_name = class_names[label_id]
    return f"{out_name}, {final_prob:.2f}%"
