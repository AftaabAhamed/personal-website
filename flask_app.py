from flask import Flask 
from flask import render_template , current_app


# creates a Flask application 
app = Flask(__name__,static_folder="static") 


@app.route("/") 
def hello(): 
	return render_template('index.html') 

# run the application 
if __name__ == "__main__": 
	app.run(debug=True)
