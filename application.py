from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
import cv2
#from mtcnn.mtcnn import MTCNN
from matplotlib import pyplot as plt




application = Flask(__name__)

@application.route('/')
def hello_world():
    return render_template('before.html')


def draw_box(image_path, faces, number):
    #
    img1 = cv2.imread(image_path)


    for face in faces:
        x, y, w, h = face['box']
        cv2.rectangle(img1, (x, y), (x + w, y + h), (0, 0, 255), 2)


    if number==1:
        cv2.imwrite('static/a1.jpg', img1)
    else:
        cv2.imwrite('static/a2.jpg', img1)
    plt.clf()




@application.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        files = request.files.getlist("file")
        count = 0
        for file in files:
            if count==0:
                file.filename="static/f1.jpg"
            else:
                file.filename="static/s1.jpg"
            file.save(file.filename)
            count+=1
        # filename = secure_filename(file.filename)
        # file.save(os.path.join(application.config['UPLOAD_FOLDER'], filename))
        from mtcnn.mtcnn import MTCNN
        image_uno = plt.imread('static/f1.jpg')
        image_dos = plt.imread('static/s1.jpg')
        draw_box('static/f1.jpg', MTCNN.detect_faces(image_uno), 1)
        draw_box('static/s1.jpg', MTCNN.detect_faces(image_dos), 2)
        ##perform_predictions("static/f1.jpg","static/s1.jpg")
        # img3 = cv2.imread('static/first.jpg')
        # cv2.imwrite('trial/afterI.jpg', img3)
        # img2 = cv2.imread('trial/second.jpg')
        # cv2.imwrite('trial/afterI2.jpg', img2)
        return render_template('after.html')



