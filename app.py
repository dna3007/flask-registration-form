from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:123456@localhost/student"
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    phone = db.Column(db.String(20))
    email = db.Column(db.String(100))
    password = db.Column(db.String(100))
    gender = db.Column(db.String(10))
    date_of_birth = db.Column(db.Date)
    hobbies = db.Column(db.String(200))
    qualification = db.Column(db.String(100))
    address = db.Column(db.String(200))


with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']
        password = request.form['password']
        gender = request.form['gender']
        dob = request.form['dob']
        hobbies = request.form.getlist('hobby')
        hobbies = ", ".join(hobbies)
        qualification = request.form['qualification']
        address = request.form['address']

        user = User(
            name=name, 
            phone=phone, 
            email=email, 
            password=password, 
            gender=gender, 
            date_of_birth=dob,
            hobbies=hobbies, 
            qualification=qualification, 
            address=address
            )
        db.session.add(user)
        db.session.commit()


    users = User.query.all()
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, port=8000)
