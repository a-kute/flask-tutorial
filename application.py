from flask import Flask, render_template, request

application = Flask(__name__)

@application.route('/')
def hello_world():
    return render_template('before.html')



@application.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    # if request.method == 'POST':
    #     files = request.files.getlist("file")
    #     count = 0
    #     for file in files:
    #         if count==0:
    #             file.filename="static/f1.jpg"
    #         else:
    #             file.filename="static/s1.jpg"
    #         file.save(file.filename)
    #         count+=1
        # filename = secure_filename(f.filename)
        # f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        #perform_predictions("static/f1.jpg","static/s1.jpg")
        # img3 = cv2.imread('static/first.jpg')
        # cv2.imwrite('trial/afterI.jpg', img3)
        # img2 = cv2.imread('trial/second.jpg')
        # cv2.imwrite('trial/afterI2.jpg', img2)
        return render_template('after.html')



