from flask import Flask, request
import tensorflow as tf
import numpy as np
import wget
import os


url = 'https://drive.google.com/uc?export=download&id=1ZlMqtm1mJ7BVEhobORtYxR1MucHjqhMh'
filename = 'efficientnetb5-Brain Tumor-94.87.h5'

if not os.path.exists(filename):
    wget.download(url, filename)

model = tf.keras.models.load_model('efficientnetb5-Brain Tumor-94.87.h5')
app = Flask(__name__)
classes = ['Astrocitoma',
            'Carcinoma',
            'Ependimoma',
            'Ganglioglioma',
            'Germinoma',
            'Glioblastoma',
            'Granuloma',
            'Meduloblastoma',
            'Meningioma',
            'Neurocitoma',
            'Oligodendroglioma',
            'Papiloma',
            'Schwannoma',
            'Tuberculoma',
            '_NORMAL']

@app.route('/', methods=['GET'])
def get_author():
    author = {
        "name": "Nathaniel Handan",
        "email": "handanfoun@gmail.com"
    }
    return author

@app.route('/predict', methods=['POST'])
def predict():
    try:
        image = request.files['file'].read()
        
        image = tf.image.decode_image(image, channels=3)
        image = tf.image.convert_image_dtype(image, tf.float32)
        image = tf.image.resize(image, [224, 224]) 

        predictions = model.predict(np.expand_dims(image, axis=0))
        predicted_class = classes[np.argmax(predictions) ]

        return f'Predicted Class: {predicted_class}'
    except KeyError:
        return {"error": "File not found."}
    except Exception as e:
        return {"error": str(e)}

if __name__ == '__main__':
    app.run(debug=True, port=5000) 