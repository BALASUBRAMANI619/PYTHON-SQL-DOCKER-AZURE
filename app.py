from flask import Flask, render_template,redirect, url_for,request
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


@app.route("/create", methods=["GET", "POST"])
def create_user():
    if request.method == 'POST':
        name = request.form["name"]
        email = request.form["email"]

        # Create a new User object
        new_user = User(name=name, email=email)

        # Save to MySQL
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for("home"))
    return render_template('create.html',title="Add New User")


# ---------- EDIT TABLE ----------

@app.route("/edit/<int:user_id>", methods=["GET", "POST"])
def edit_user(user_id):
    user = User.query.get_or_404(user_id)

    if request.method == "POST":
        user.name = request.form["name"]
        user.email = request.form["email"]

        db.session.commit()
        return redirect(url_for("home"))

    return render_template("edit.html", title="Edit User", user=user)


# ---------- DELETE ROW ----------

@app.route("/delete/<int:user_id>", methods=["GET", "POST"])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/")
def home():
    title = "User list"
    users = User.query.all()   # Fetch all users from the database
    return render_template('home.html', title=title,users=users)


if __name__ == "__main__":
    app.run(debug=True)