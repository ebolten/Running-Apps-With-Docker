from flask import Flask
import subprocess
from flask_json import FlaskJSON, JsonError, json_response, as_json
from flask_cors import CORS, cross_origin

# build docker file: docker build --tag=TAG/IMG-TITLE -f Dockerfile_FILENAME .
# run docker file: docker run TAG/IMG-TITLE

# build the fortran app --> docker build --tag=me/fortran-img -f Dockerfile_fortran .
# run the fortran app --> docker run me/fortran-img

# build the python app --> docker build --tag=me/python-img -f Dockerfile_python .
# run the python app --> docker run me/python-img

print('running app.py')

def html_page():
    return (
        "<html>" +
            "<div style='text-align:center;margin:50px' >" +
                "<h1> Hello World! </h1>" +
                "<p> I am running a Docker file :) </p>" +
            "</div>" +
        "</html>"
    )

# creating a demo flask app
# this app is run with Docker
app = Flask(__name__)
json = FlaskJSON(app)

@app.route('/html')
@cross_origin()
def hello():
    subprocess.call(['./runDocker.sh'])
    return html_page()

#run the Flask app
if __name__ == '__main__':
    app.run()