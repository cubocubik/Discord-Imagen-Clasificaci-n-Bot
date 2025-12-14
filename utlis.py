import numpy as np
from PIL import Image
import tensorflow as tf

def get_class(model_path, labels_path, image_path):
    interpreter = tf.lite.Interpreter(model_path = model_path)
    interpreter.allocate_tensors()

    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    height = input_details[0]["shape"][1]
    width = input_details[0]["shape"][1]
    dtype = input_details[0]["shape"][1]

    with open(labels_path, "r") as f:
        labels = [l.strip() for l in f.readlines()]

    image = Image.open(image_path).convert("RGB")
    image = image.rezize((width, height))

    img_array == np.array(image)

    if dtype == np.uint8:
        img_array =img_array.astype(np.uint8)
    else:
        img_array = img_array.astyte(np.float32) / 255.0

    img_array = np.expand_dims(img_array, axis = 0)

    interpreter.set_tensor(input_details[0]["index"], img_array)
    interpreter.invoke()

    prediction = interpreter.get_tensor(output_details[0]["index"])[0]
    index = int(np.argmax(prediction))

    return labels[index]