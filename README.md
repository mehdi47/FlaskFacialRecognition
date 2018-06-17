# FlaskFacialRecognition (!!!Project In Work , Not Completed!!!)

This is a FLASK web based application using facial recognition .
The application , returns informations about user cv after facial recognition process is successful and gives opportunity of validating or not the user information.

### Prerequisites
* Python 3.x
* OpenCV 3.x
* Numpy
* MatPlotLib
* Flask
* Wamp or Xampp (depeding on your OS)
* MySQL and PyMYSQL
* wtForms
* passlib.hash
* flask_mysqldb
* Anaconda

### Installing

* in your anaconda prompt , input : activate the_name_of_your_conda_environnement
* pip install opencv-contrib-python
* pip install matplotlib
* pip install pymysql
* pip install flask
* pip install WTForms
* pip install passlib
* pip install Flask-MySQLdb
* Download wamp or xampp , and anaconda from their websites and follow instructions to install

## Running the tests

* run the dataSetGenerator.py and enter a unique id and name to create face samples with your face
* run trainer.py to train the model
* run detector.py to start facial recognition
* run app.py and go to localhost:5000 to access the flask app
* in app.py , input the route defined in each functions to access views
