from flask import *
import os
from werkzeug.utils import secure_filename


UPLOAD_FOLDER = 'C:/Python/CCProject/uploads'
#ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'This is your secret key to utilize session in Flask'

@app.route('/') 
def main(): 
	return render_template("index.html") 


@app.route('/upload', methods=['POST']) 
def upload(): 
	if request.method == 'POST': 

		# Get the list of files from webpage 
		f = request.files.getlist('file')
		
		#data_file =secure_filename('file')
		
		#session['uploaded_data_file_path']=(os.path.join(app.config['UPLOAD_FOLDER'], data_file))

		# Iterate for each file in the files List, and Save them 
		for file in f:
			file.save(os.path.join(app.config['UPLOAD_FOLDER'],file.filename))
	return "<h1>File Uploaded Successfully.!</h1>"


if __name__ == '__main__': 
	app.run(debug=True) 
