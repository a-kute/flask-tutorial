from flask import Flask, render_template, request
from matplotlib import pyplot as plt




application = Flask(__name__)

@application.route('/')
def hello_world():
    return render_template('before.html')
# def draw_box(image_path, faces):
#     image = plt.imread(image_path)
#     plt.imshow(image)
#     ax = plt.gca()
#     for face in faces:
#         x,y,w,h = face['box']
#         face_border = Rectangle((x,y),w,h,fill=False,color='red')
#         ax.add_patch(face_border)
#
#     plt.axis('off')
#     plt.savefig('static/a1.jpg')
#     plt.show()
#


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
        from mtcnn.mtcnn import MTCNN


        # filename = secure_filename(file.filename)
        # file.save(os.path.join(application.config['UPLOAD_FOLDER'], filename))


        image_uno = plt.imread('static/f1.jpg')
        image_dos = plt.imread('static/s1.jpg')
        #draw_box('static/f1.jpg', MTCNN.detect_faces(image_uno))
        #draw_box('static/s1.jpg', MTCNN.detect_faces(image_dos))


        ##perform_predictions("static/f1.jpg","static/s1.jpg")
        # img3 = cv2.imread('static/first.jpg')
        # cv2.imwrite('trial/afterI.jpg', img3)
        # img2 = cv2.imread('trial/second.jpg')
        # cv2.imwrite('trial/afterI2.jpg', img2)
        return render_template('after.html')



