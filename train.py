import os
import cv2
import numpy as np
from joblib import dump
from sklearn.preprocessing import LabelEncoder

# bucket = 'vigilenteye-faces-video'
# people_list = os.listdir(path)
# faces = []
# labels = []
# label = 0    

def model_training_controller ():
    print('Generando Codificador...')
    label_encoder = LabelEncoder()
    labels = []
    faces = []
    input_dir = '/opt/ml/input/data/train/'

    for user_name in os.listdir(input_dir):
        print('user_name: ' + user_name)
        user_dir = os.path.join(input_dir, user_name)
        for img_file in os.listdir(user_dir):
            local_file_path = os.path.join(user_dir, img_file)
            print('img_file: ' + img_file)

            img = cv2.imread(local_file_path, 0)
            labels.append(user_name)
            faces.append(img)
    
    encoded_labels = label_encoder.fit_transform(labels)

    print('Creando el modelo...')
    model = cv2.face.LBPHFaceRecognizer_create()
    print('Entrenando al modelo...')
    model.train(np.array(faces), np.array(encoded_labels))
    print('Exportando el modelo...')

    model_path = '/opt/ml/model/modeloLBPHFace.xml'
    label_encoder_path = '/opt/ml/model/label_encoder.pkl'

    model.write(model_path)
    dump(label_encoder, label_encoder_path)

    return 'ok'

model_training_controller()