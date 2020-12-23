import os

from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def home():
    data = {'message': ['Hello from imageuploadapi server']}
    returnData = jsonify(data)
    print("returnData: {}".format(returnData))
    return returnData


@app.route('/api/v1/imageupload', methods=['POST'])
def image_upload_request():
    print("* /api/v1/image called")

    data = {'message': ['not a POST request']}

    if request.method == 'POST':  # this block is only entered when the form is submitted

        try:
            filename_on_server = ""

            # get data from request

            print("!!! get form-data")
            form_data = request.form
            print("form-data: {}".format(form_data))

            print("!!! get file-data")
            file_data = request.files
            print("file-data: {}".format(file_data))

            # show form data
            print("!!! form-data")
            for key, value in form_data.items():
                print("{} : {}".format(key, value))

            # show image data
            print("!!! file-data")
            for key, value in file_data.items():
                # reference to value: https://werkzeug.palletsprojects.com/en/1.0.x/datastructures/
                # type(value) in debug console shows datatype
                print("{} : {}".format(key, value))

                # use form-data name to save the image in temp
                pfn_image = os.path.join('..','data_temp',"{}.{}".format(value.name,'png'))
                print("  save image as: {}".format(pfn_image))

                value.save(pfn_image)
                value.close()

            data = {'message': 'processing ok'}

        except Exception as e:
            print("exception: ".format(e))
            data = {'message': ['processing failed'],
                    'exception:':e}

    returnData = jsonify(data)

    print("returnData: {}".format(returnData))

    return returnData


if __name__ == '__main__':
    print("running from main")
    # run app in debug mode on port 5000
    app.run(debug=True, use_reloader=True, host='0.0.0.0',
            port=int(os.environ.get('PORT', 5000)))
