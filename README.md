# JWT Authentication API

This is a simple backend project built using FastAPI and MongoDB.

It provides user authentication using JWT (JSON Web Tokens) and includes a protected API route.

---

## 🔹 What this project does

- Allows users to sign up
- Allows users to log in
- Generates JWT token after login
- Protects an API using JWT authentication
- Returns user details for authenticated users

---

## 🔹 Tech Stack

- Python
- FastAPI
- MongoDB
- PyMongo
- JWT (python-jose)
- Passlib (bcrypt)
- Uvicorn

---

## 🔹 API Endpoints

### Signup
```
POST /auth/signup
```

Parameters:
- email
- password

---

### Login
```
POST /auth/login
```

Response:
- JWT token

---

### Protected Route
```
GET /auth/me
```

Header:
```
Authorization: Bearer <JWT_TOKEN>
```

Returns logged-in user details.

---

## 🔹 How to Run the Project

1. Install dependencies:
```
pip install -r requirements.txt
```

2. Create `.env` file:
```
JWT_SECRET=your_secret_key
MONGODB_URI=your_mongodb_uri
```

3. Start the server:
```
PYTHONPATH=. python -m uvicorn app.main:app --reload
```

4. Open API docs:
```
http://127.0.0.1:8000/docs
```

---

## 🔹 Status

Project is complete and working.