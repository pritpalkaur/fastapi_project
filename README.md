# 🛒 Products API (FastAPI + SQL Server + JWT)

A secure and scalable FastAPI backend for managing products in SQL Server. Includes JWT authentication, Swagger documentation, error logging, and clean architecture.

---

## 🚀 Features

- ✅ FastAPI with auto-generated Swagger UI (`/docs`)
- 🔐 JWT-based authentication (`/token`)
- 🧾 Pydantic models for request/response validation
- 🗃️ SQL Server integration via `pyodbc`
- 🧠 Error logging to `error.log`
- 📁 Clean structure: `main.py`, `models.py`, `auth.py`, `db.py`

---

## 🛠️ Setup

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/fastapi_project.git
cd fastapi_project

###**how to run**
python -m venv venv
.\venv\Scripts\activate
-----------------------------------------------------
pip install -r requirements.txt
 pip install fastapi uvicorn python-jose[cryptography] python-multipart pyodbc
--------------------------------------------------
Run locally
uvicorn main:app --reload
 
