import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing.image import img_to_array
import json

# Load the class_indices dictionary from the file
with open(r'D:\Me\work\Chatbot\chatbot\models\class_indices.json', 'r') as f:
    class_indices = json.load(f)

# Define your function to classify the image
def classify_image(image):
    health_status_output = ''
    # Load the TFLite model
    interpreter = tf.lite.Interpreter(model_path=r"D:\Me\work\Chatbot\chatbot\models\cropAgent.tflite")
    interpreter.allocate_tensors()

    # Preprocess the image
    image_array = img_to_array(image.resize((224, 224)))  # Resize the image to match the input size of the model
    image_array = np.expand_dims(image_array, axis=0)
    image_array /= 255.0

    # Get the input and output tensors
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    # Set the input tensor
    interpreter.set_tensor(input_details[0]['index'], image_array)

    # Run the inference
    interpreter.invoke()

    # Get the output tensor
    predictions = interpreter.get_tensor(output_details[0]['index'])
    predicted_class_index = np.argmax(predictions[0])
    class_labels = list(class_indices.keys())
    plant_name, plant_type = class_labels[predicted_class_index].split("__")
    predicted_probability = predictions[0][predicted_class_index]

    health_status_output = 'healthy' if plant_type == 'healthy' else plant_type

    return plant_name, plant_type.strip('_'), health_status_output.strip('_')
