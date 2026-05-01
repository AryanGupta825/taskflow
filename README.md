================================================================================
  TASKFLOW — TEAM TASK MANAGER
================================================================================

  A full-stack team task management web application built with Python Flask,
  MySQL, and a dark-themed frontend using Tailwind CSS. It allows teams to
  create projects, assign tasks, track progress, and manage members with
  role-based access control — similar to Trello or Asana.

  Live URL : http://taskflow-kco6.onrender.com
  GitHub   : https://github.com/AryanGupta825/taskflow

================================================================================
  ABOUT THE PROJECT
================================================================================

  TaskFlow solves the problem of team task coordination. Instead of managing
  tasks over chat messages or spreadsheets, teams can create a shared project
  workspace where an Admin controls the tasks and Members update their progress.

  Key highlights:

  - Secure JWT-based login and signup system
  - Project creation where the creator becomes Admin automatically
  - Admin can invite members by email, assign tasks, set priorities and
    due dates, and monitor the full team's workload
  - Members can only see tasks assigned to them and update their status
  - Kanban board (To Do / In Progress / Done) for visual task tracking
  - Live dashboard showing completion rate, overdue tasks, and team workload
  - All role permissions enforced at the API level, not just the UI
  - Fully deployed on Render with MySQL as the production database

================================================================================
  CODE STRUCTURE
================================================================================

  taskflow/
  ├── app.py                        Entry point — creates and runs the Flask app
  │
  ├── backend/
  │   ├── __init__.py               App factory (create_app function),
  │   │                             registers blueprints and extensions
  │   │
  │   ├── models.py                 SQLAlchemy database models:
  │   │                               User          — stores name, email, hashed password
  │   │                               Project       — name, description, color, admin reference
  │   │                               ProjectMember — links users to projects with a role
  │   │                               Task          — title, status, priority, due date,
  │   │                                              assigned user, parent project
  │   │
  │   └── routes/
  │       ├── auth.py               POST /api/auth/signup
  │       │                         POST /api/auth/login
  │       │                         GET  /api/auth/me
  │       │
  │       ├── projects.py           GET    /api/projects
  │       │                         POST   /api/projects
  │       │                         GET    /api/projects/<id>
  │       │                         PUT    /api/projects/<id>
  │       │                         DELETE /api/projects/<id>
  │       │                         POST   /api/projects/<id>/members
  │       │                         DELETE /api/projects/<id>/members/<user_id>
  │       │
  │       ├── tasks.py              GET    /api/tasks?project=<id>
  │       │                         POST   /api/tasks
  │       │                         PUT    /api/tasks/<id>
  │       │                         DELETE /api/tasks/<id>
  │       │
  │       ├── dashboard.py          GET /api/dashboard?project=<id>
  │       │                         Returns total tasks, status breakdown,
  │       │                         overdue list, and per-member workload
  │       │
  │       └── frontend.py           Catch-all route that serves index.html
  │                                 for every non-API URL (SPA support)
  │
  ├── frontend/
  │   ├── templates/
  │   │   └── index.html            Single HTML shell — all views are rendered
  │   │                             dynamically by JavaScript into <div id="app">
  │   │
  │   └── static/
  │       ├── css/
  │       │   └── main.css          Dark theme design system — CSS variables,
  │       │                         custom scrollbar, component base styles
  │       │
  │       └── js/
  │           └── app.js            Full SPA logic:
  │                                   - Client-side router
  │                                   - Auth state (token stored in localStorage)
  │                                   - All fetch() API calls with JWT headers
  │                                   - Page render functions for each view
  │                                   - Event handlers for forms and buttons
  │
  ├── requirements.txt              Python dependencies
  ├── Procfile                      Gunicorn start command for Render
  ├── railway.toml                  Build and deploy configuration
  └── .env.example                  Template for environment variables

================================================================================
  SKILLS DEMONSTRATED
================================================================================

  BACKEND DEVELOPMENT
  -------------------
  - Built a RESTful API using Python Flask with Blueprint-based route separation
  - Designed a relational MySQL database with 4 tables and proper foreign keys
  - Used SQLAlchemy ORM for all database operations — no raw SQL with user input
  - Implemented JWT authentication using Flask-JWT-Extended
  - Hashed all passwords with bcrypt before storing in the database
  - Validated all request inputs before processing to prevent bad data
  - Applied role-based access control at the route level (not just the UI)
  - Configured CORS to restrict API access to the frontend origin only

  FRONTEND DEVELOPMENT
  --------------------
  - Built a Single Page Application using only HTML, CSS, and Vanilla JavaScript
  - Implemented client-side routing so pages change without full reloads
  - Managed global auth state using localStorage and injected tokens into
    every fetch() request automatically
  - Dynamically rendered all UI (Kanban board, dashboard charts, member lists)
    by building HTML strings in JavaScript and injecting into the DOM
  - Styled the entire UI with Tailwind CSS utility classes and a custom
    dark theme defined through CSS variables

  DATABASE DESIGN
  ---------------
  - Designed normalized schema with Users, Projects, ProjectMembers, and Tasks
  - Used a junction table (ProjectMembers) to handle many-to-many relationships
    between users and projects, with an additional role column
  - Applied ON DELETE CASCADE so deleting a project removes all its tasks
    and member records automatically

  DEPLOYMENT
  ----------
  - Deployed the full application on Render using GitHub integration
  - Configured Gunicorn as the production WSGI server
  - Managed all secrets through Render environment variables
  - Connected the MySQL database to the Flask app via DATABASE_URL
  - Wrote a health check endpoint for uptime monitoring

================================================================================
