
# Flask CRUD Web Application (MySQL + SQLAlchemy)

A simple and clean **CRUD (Create, Read, Update, Delete)** web application built using **Flask**, **MySQL**, **SQLAlchemy**, and **Bootstrap**.  
This project is perfect for beginners learning Flask or anyone who wants a minimal, well-structured CRUD example.

---

## 🚀 Features

- Create new users  
- View all users  
- Edit user details  
- Delete users  
- MySQL database integration  
- Bootstrap UI with navbar & styled tables  
- Form validation (empty fields, duplicate emails)  
- Flash messages for success/error feedback  
- Custom 404 error page  

---

## 🛠️ Tech Stack

- **Python 3**
- **Flask**
- **Flask-SQLAlchemy**
- **MySQL**
- **PyMySQL**
- **Bootstrap 5**

---

## 📂 Project Structure

flask_crud_app/
│
├── app.py
├── requirements.txt
├── templates/
│ ├── base.html
│ ├── home.html
│ ├── create.html
│ ├── edit.html 

📘 How It Works
🟦 Create User

Fill the form → data saved into MySQL → redirect to home page.

🟩 Read Users

Home page lists all users from database in a styled table.

🟧 Update User

Click Edit → update form → changes saved via SQLAlchemy.

🟥 Delete User

Click Delete → user removed permanently from MySQL.