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

---

## ⚙️ Local Setup

### Prerequisites
- Python 3.11+
- MySQL 8.0+

### 1. Clone & Install

```bash
git clone https://github.com/yourusername/taskflow.git
cd taskflow
pip install -r backend/requirements.txt
```

### 2. Database Setup

```sql
CREATE DATABASE taskflow CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

### 3. Environment Variables

```bash
cp .env.example .env
# Edit .env with your credentials
```

### 4. Run

```bash
python app.py
# Visit http://localhost:5000
```

---

## 🌐 Railway Deployment

### 1. Push to GitHub

```bash
git init && git add . && git commit -m "Initial commit"
git remote add origin https://github.com/yourusername/taskflow.git
git push -u origin main
```

### 2. Deploy on Railway

1. Go to [railway.app](https://railway.app) and sign in
2. Click **New Project → Deploy from GitHub repo**
3. Select your repository
4. Add a **MySQL** database service
5. Set environment variables:
   ```
   DATABASE_URL=<auto-provided by Railway MySQL>
   SECRET_KEY=your-secret-key-here
   JWT_SECRET_KEY=your-jwt-secret-here
   ```
6. Deploy! Railway auto-detects the Procfile

### 3. Environment Variables on Railway

| Variable | Value |
|----------|-------|
| `DATABASE_URL` | Copy from MySQL service (format: `mysql+pymysql://...`) |
| `SECRET_KEY` | Any random string |
| `JWT_SECRET_KEY` | Any random string |

---

## 📡 API Endpoints

### Auth
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/auth/signup` | Register user |
| POST | `/api/auth/login` | Login |
| GET | `/api/auth/me` | Current user |

### Projects
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/projects` | List my projects |
| POST | `/api/projects` | Create project |
| GET | `/api/projects/:id` | Get project |
| PUT | `/api/projects/:id` | Update project (Admin) |
| DELETE | `/api/projects/:id` | Delete project (Admin) |
| GET | `/api/projects/:id/members` | List members |
| POST | `/api/projects/:id/members` | Add member (Admin) |
| DELETE | `/api/projects/:id/members/:uid` | Remove member (Admin) |
| GET | `/api/projects/:id/tasks` | Project tasks |

### Tasks
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/tasks` | All my tasks |
| POST | `/api/tasks` | Create task |
| GET | `/api/tasks/:id` | Get task |
| PUT | `/api/tasks/:id` | Update task |
| DELETE | `/api/tasks/:id` | Delete task (Admin) |

### Dashboard
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/dashboard` | Stats & analytics |

---

## 🎭 Role Permissions

| Action | Admin | Member |
|--------|-------|--------|
| Create tasks | ✅ | ❌ |
| Assign tasks | ✅ | ❌ |
| Update any task | ✅ | ❌ |
| Update own task status | ✅ | ✅ |
| Delete tasks | ✅ | ❌ |
| Add/remove members | ✅ | ❌ |
| View project tasks | ✅ | ✅ |

---

## 👤 Author

Built as a full-stack coding assignment demonstrating Flask REST APIs, MySQL with SQLAlchemy ORM, JWT authentication, role-based access control, and modern SPA frontend design.
