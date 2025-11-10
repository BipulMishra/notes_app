# 📝 Personal Notes Manager App

A **full-stack mini application** built with **FastAPI**, **Streamlit**, and **SQLite** — designed to help you create, view, and delete personal notes easily.

---

## 🚀 Tech Stack

| Layer | Technology |
|--------|-------------|
| **Frontend (UI)** | [Streamlit](https://streamlit.io/) |
| **Backend (API)** | [FastAPI](https://fastapi.tiangolo.com/) |
| **Database** | SQLite (via SQLAlchemy ORM) |
| **Server** | Uvicorn (ASGI server) |
| **Dependency Manager** | [uv](https://docs.astral.sh/uv/) |

---

## 🧠 Overview

This project demonstrates how a Python-based full-stack app works using FastAPI (backend) and Streamlit (frontend).  

**Architecture:**
```

User → Streamlit UI → FastAPI API → SQLite Database

```

- 🧾 Add, view, and delete notes.
- 💾 Data is persisted in a local SQLite database (`notes.db`).
- 🔗 API and frontend run independently and communicate via REST API calls.

---

## 🗂️ Project Structure

```

notes_app/
│
├── backend/
│   ├── main.py            # FastAPI app entry point
│   ├── crud.py            # Database operations (CRUD)
│   ├── database.py        # SQLAlchemy setup
│   ├── models.py          # Database models (tables)
│
├── frontend/
│   ├── app.py             # Streamlit frontend UI
│
├── requirements.txt       # All project dependencies
└── README.md              # Project documentation

````

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

```bash
git clone https://github.com/<your-username>/notes_app.git
cd notes_app
````

### 2️⃣ Create and activate virtual environment

```bash
uv venv
```

* **Windows:**

  ```bash
  .venv\Scripts\activate
  ```
* **macOS/Linux:**

  ```bash
  source .venv/bin/activate
  ```

### 3️⃣ Install dependencies

```bash
uv pip install -r requirements.txt
```

---

## 🖥️ Running the App

### ▶️ Start Backend (FastAPI)

```bash
uvicorn backend.main:app --reload
```

Server will start at 👉 **[http://127.0.0.1:8000](http://127.0.0.1:8000)**

* API Docs: **[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)**
* OpenAPI Spec: **[http://127.0.0.1:8000/openapi.json](http://127.0.0.1:8000/openapi.json)**

---

### ▶️ Start Frontend (Streamlit)

Open a new terminal tab (keep backend running):

```bash
streamlit run frontend/app.py
```

Frontend runs at 👉 **[http://localhost:8501](http://localhost:8501)**

---

## 💾 Database Details

* Database file: `notes_app/backend/notes.db`
* ORM: SQLAlchemy
* Model: `Note(id, title, content, created_at)`

---

## 🧩 API Endpoints

| Method     | Endpoint                 | Description         |
| ---------- | ------------------------ | ------------------- |
| **GET**    | `/notes`                 | Fetch all notes     |
| **POST**   | `/notes?title=&content=` | Add a new note      |
| **DELETE** | `/notes/{note_id}`       | Delete a note by ID |

---

## 💡 Features

* ✏️ Add personal notes
* 📄 View all notes
* 🗑️ Delete notes
* ⚡ Real-time updates between frontend and backend
* 📚 Lightweight and beginner-friendly

---

## 🔍 Example Workflow

1. Run the backend (`uvicorn backend.main:app --reload`)
2. Run the frontend (`streamlit run frontend/app.py`)
3. Add a note in the Streamlit interface
4. View all notes live
5. Delete notes directly from the UI

---

## 🧠 What You’ll Learn

* How FastAPI handles API requests and database sessions
* How Streamlit interacts with REST APIs
* How SQLAlchemy ORM connects Python objects with SQLite tables
* How to structure small full-stack Python apps

---

## 🧰 Future Improvements

* ✨ Add “Edit Note” functionality
* 🔍 Add search/filter feature
* 🔐 Add user authentication
* 🌍 Deploy backend (Render) + frontend (Streamlit Cloud)

---

## 👨‍💻 Author

**Bipul Mishra**
💼 Data & Software Enthusiast
📚 Learning FastAPI • Streamlit • Data Engineering

---

## 🪪 License

This project is open-source and free to use for learning purposes.


