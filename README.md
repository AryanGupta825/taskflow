# 🚀 TaskFlow — Team Task Manager

A full-stack team task management web application built with **Python Flask**, **MySQL**, and a beautiful dark-themed frontend using **Tailwind CSS**.

---

## ✨ Features

- 🔐 **JWT Authentication** — Secure signup & login
- 📁 **Project Management** — Create projects, invite team members with roles
- ✅ **Task Management** — Kanban board with To Do / In Progress / Done columns
- 📊 **Dashboard** — Live stats, tasks per user, overdue tracking
- 🛡 **Role-Based Access** — Admin (full control) vs Member (own tasks only)
- 📱 **Responsive UI** — Works on desktop and mobile

---

## 🛠 Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python 3.11, Flask 3.0 |
| Auth | Flask-JWT-Extended |
| Database | MySQL (via PyMySQL + SQLAlchemy) |
| Frontend | HTML5, Tailwind CSS, Vanilla JS |
| Deployment | Railway |

---

## 📁 Project Structure

```
taskflow/
├── app.py                  # Entry point
├── backend/
│   ├── __init__.py         # App factory
│   ├── models.py           # SQLAlchemy models
│   └── routes/
│       ├── auth.py         # Auth endpoints
│       ├── projects.py     # Project endpoints
│       ├── tasks.py        # Task endpoints
│       ├── dashboard.py    # Dashboard stats
│       └── frontend.py     # SPA serving
├── frontend/
│   ├── templates/
│   │   └── index.html      # SPA shell
│   └── static/
│       ├── css/main.css    # Design system
│       └── js/app.js       # SPA logic
├── requirements.txt
├── Procfile
├── railway.toml
└── .env.example
```


