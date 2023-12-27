from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model): #defining schema of database through class
    
    sno = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(200),nullable = False)
    desc = db.Column(db.String(500),nullable = False)
    date_created = db.Column(db.DateTime,default = datetime.utcnow)
    
    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"
    
# Function to create database tables
def create_tables():
    with app.app_context():
        db.create_all()

@app.route('/')
def hello():
    return render_template('index.html')
    #return 'Hello, Flask!'

@app.route('/products')
def products():
    return 'Hello, this is products page!'

if __name__ == '__main__':
    # Call the function to create tables before running the application
    create_tables()
    app.run(debug=True)