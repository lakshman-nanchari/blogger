🚀 Overview

This is a Django Blogger Application that provides API endpoints for:

User Registration & Authentication

CRUD Operations for Blog Posts

Swagger API Documentation using drf-yasg

📌 Features

✅ User Registration (Signup)
✅ User Authentication
✅ Create, Read, Update, and Delete Blog Posts
✅ Swagger API Documentation (drf-yasg)
✅ Token Authentication (Optional)

🛠️ Installation

1️⃣ Clone the Repository

git clone https://github.com/your-username/django-blogger.git
cd django-blogger

2️⃣ Create and Activate a Virtual Environment

python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

3️⃣ Install Dependencies

pip install -r requirements.txt

4️⃣ Apply Migrations

python manage.py makemigrations
python manage.py migrate

5️⃣ Create a Superuser

python manage.py createsuperuser

6️⃣ Run the Development Server

python manage.py runserver

Now, visit:

Swagger UI: http://127.0.0.1:8000/swagger/

ReDoc UI: http://127.0.0.1:8000/redoc/

🔧 API Endpoints

Authentication

Method

Endpoint

Description

POST

/api/register/

Register a new user

Blog APIs

Method

Endpoint

Description

GET

/api/blogs/

List all blogs

POST

/api/blogs/

Create a new blog (Auth required)

GET

/api/blogs/<id>/

Retrieve a blog

PUT

/api/blogs/<id>/

Update a blog (Author only)

DELETE

/api/blogs/<id>/

Delete a blog (Author only)

📝 Swagger API Documentation

The API documentation is available at:

Swagger UI: http://127.0.0.1:8000/swagger/

ReDoc UI: http://127.0.0.1:8000/redoc/

📂 Project Structure

blogger/
│── blogger/          # Main Django Project
│── blog/             # Blog Application
│── venv/             # Virtual Environment
│── manage.py         # Django Management Script
│── requirements.txt  # Dependencies
│── README.md         # Project Documentation

🔒 Authentication

This project requires authentication for creating, updating, and deleting blog posts.

You can use Django’s session authentication or implement Token-based authentication.

📜 License

This project is open-source. Feel free to modify and use it.

👨‍💻 Author

Your Name - GitHub

🛠️ Future Improvements

✅ Add JWT Authentication

✅ Implement Comments & Likes

✅ Deploy to a Live Server

Feel free to contribute! 🚀
