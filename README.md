# Home Library

A full-stack web application for managing a personal home library. The application is being developed as a personal software project to practice full-stack development, database design, REST API development, and eventually Linux-based deployment.

## Project Status

**Current Phase:** Phase 1 — Core Application Development

The backend and database foundation are currently implemented. The React frontend has not yet been developed.

### Current Features

* FastAPI REST API
* PostgreSQL database
* SQLAlchemy ORM
* Book database model
* Pydantic request/response schemas
* CRUD operations for books
* Automatic API documentation through OpenAPI/Swagger
* Environment-based database configuration

### Planned Features

* React + TypeScript frontend
* Book search and filtering
* Book cover images
* ISBN-based book lookup
* Reading status tracking
* Book ratings
* Library statistics and dashboard
* User authentication
* Database migrations with Alembic
* Docker containerization
* Nginx reverse proxy
* HTTPS
* Deployment to a personal Linux homelab
* Automated testing
* CI/CD with GitHub Actions

---

## Technology Stack

### Backend

* **Python**
* **FastAPI**
* **Uvicorn**
* **SQLAlchemy**
* **Pydantic**
* **psycopg**

### Database

* **PostgreSQL**

### Frontend

Planned:

* **React**
* **TypeScript**
* **Tailwind CSS**

### Deployment

Planned:

* **Docker**
* **Docker Compose**
* **Nginx**
* **Ubuntu Server**

---

## Project Architecture

The application is being developed as a three-tier full-stack application.

```text
┌──────────────────────────┐
│        Frontend          │
│    React + TypeScript    │
└────────────┬─────────────┘
             │
             │ HTTP / REST
             ▼
┌──────────────────────────┐
│         Backend          │
│    Python + FastAPI      │
│        SQLAlchemy        │
└────────────┬─────────────┘
             │
             │ SQL
             ▼
┌──────────────────────────┐
│        Database          │
│       PostgreSQL         │
└──────────────────────────┘
```

The frontend will communicate with the FastAPI backend through REST endpoints. The backend uses SQLAlchemy to interact with PostgreSQL.

---

## Current Backend Structure

```text
backend/
├── .venv/
├── app/
│   ├── api/
│   │   ├── __init__.py
│   │   └── books.py
│   │
│   ├── database/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   └── connection.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   └── book.py
│   │
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── book.py
│   │
│   ├── __init__.py
│   └── main.py
│
└── requirements.txt
```

### Directory Responsibilities

**`app/api/`**

Contains FastAPI route definitions and API endpoints.

**`app/database/`**

Contains the SQLAlchemy database engine and declarative base configuration.

**`app/models/`**

Contains SQLAlchemy database models.

**`app/schemas/`**

Contains Pydantic schemas used for API validation and serialization.

**`app/main.py`**

Application entry point and FastAPI configuration.

---

## Database

The application currently uses PostgreSQL with a dedicated application database and database user.

```text
Database: home_library
Schema: public
Table: books
```

The application connects to PostgreSQL through SQLAlchemy using the PostgreSQL `psycopg` driver.

Database credentials are stored in a local `.env` file and are excluded from version control.

### Book Model

The current `books` table contains:

| Column             | Type    | Description                        |
| ------------------ | ------- | ---------------------------------- |
| `id`               | Integer | Unique book identifier             |
| `title`            | String  | Book title                         |
| `author`           | String  | Book author                        |
| `isbn`             | String  | International Standard Book Number |
| `publication_year` | Integer | Year the book was published        |
| `pages`            | Integer | Number of pages                    |
| `genre`            | String  | Book genre                         |
| `reading_status`   | String  | Current reading status             |
| `rating`           | Integer | Personal rating from 1–5           |
| `notes`            | Text    | Personal notes about the book      |

The initial database model is intentionally simple. The schema will evolve as additional application requirements are implemented.

---

## REST API

The current API provides CRUD operations for books.

| Method   | Endpoint          | Description              |
| -------- | ----------------- | ------------------------ |
| `GET`    | `/api/books/`     | Retrieve all books       |
| `GET`    | `/api/books/{id}` | Retrieve a specific book |
| `POST`   | `/api/books/`     | Create a new book        |
| `PUT`    | `/api/books/{id}` | Update an existing book  |
| `DELETE` | `/api/books/{id}` | Delete a book            |

FastAPI automatically generates interactive API documentation.

When running the development server, the documentation is available at:

```text
http://127.0.0.1:8000/docs
```

---

## Running the Backend

### Requirements

* Python 3.12+
* PostgreSQL
* Git

### Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/home-library.git
cd home-library
```

### Create the Virtual Environment

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure the Database

Create a `.env` file in the `backend` directory:

```text
DATABASE_URL=postgresql+psycopg://home_library_app:YOUR_PASSWORD@localhost:5432/home_library
```

Do not commit the `.env` file to Git.

### Start the Development Server

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Interactive API documentation:

```text
http://127.0.0.1:8000/docs
```

---

## Development Roadmap

### Phase 1 — Core Application

* [x] Initialize Git repository
* [x] Create GitHub repository
* [x] Set up Python virtual environment
* [x] Create FastAPI application
* [x] Install and configure PostgreSQL
* [x] Connect FastAPI to PostgreSQL
* [x] Configure SQLAlchemy
* [x] Create initial Book model
* [x] Create Pydantic schemas
* [x] Implement Book CRUD API
* [ ] Build React frontend
* [ ] Connect frontend to REST API

### Phase 2 — Library Features

* [ ] Search books
* [ ] Filter books
* [ ] Sort books
* [ ] Book cover images
* [ ] ISBN lookup
* [ ] Reading status
* [ ] Ratings
* [ ] Library statistics
* [ ] Improved database relationships

### Phase 3 — Application Improvements

* [ ] User authentication
* [ ] Authorization
* [ ] Input validation improvements
* [ ] Error handling
* [ ] Automated tests
* [ ] Alembic database migrations

### Phase 4 — Deployment

* [ ] Dockerize backend
* [ ] Dockerize frontend
* [ ] PostgreSQL container
* [ ] Docker Compose configuration
* [ ] Nginx reverse proxy
* [ ] HTTPS
* [ ] Deploy to Ubuntu homelab
* [ ] Configure backups

### Phase 5 — DevOps

* [ ] GitHub Actions
* [ ] Automated testing
* [ ] CI/CD pipeline
* [ ] Production configuration
* [ ] Monitoring/logging
* [ ] Deployment documentation

---

## Project Goals

This project is intended to provide practical experience with:

* Full-stack web application development
* REST API design
* Relational database design
* SQL and PostgreSQL
* Object-relational mapping
* API validation
* Frontend development
* Linux application deployment
* Containerization
* Reverse proxies and HTTPS
* Automated testing
* CI/CD
* Software development workflows

The project will be developed incrementally, with each phase building on the previous one.
