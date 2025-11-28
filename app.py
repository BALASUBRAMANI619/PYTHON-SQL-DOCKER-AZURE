from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

app = Flask(__name__)

# ---------- MySQL Database Configuration ----------
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:new_password@localhost/flask_crud"
#app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:your_password@localhost/flask_crud"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
with app.app_context():
    try:
        result = db.session.execute(text("SELECT 1")).scalar()
        print("Connection successful:", result)
    except Exception as e:
        print("Connection failed:", e)

# ---------- Database Model ----------
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<User {self.name}>"

# ---------- Create Tables ----------
with app.app_context():
    db.create_all()

# ---------- Routes ----------

@app.route("/")
def home():
    title = "Home Page"
    return render_template('home.html', title=title)

if __name__ == "__main__":
    app.run(debug=True)