# 📚 book_manager — Django REST API (Docker + PostgreSQL)

## 🏁 Project Setup & Installation

## 🧰 Tech Stack

- Django 5, DRF
- PostgreSQL
- Docker, docker-compose
- JWT (SimpleJWT)
- Tests: DRF APITestCase

### 1. Clone the Repository

```bash
git clone https://github.com/Praveenkumar9392/Simple-Book-Management-System.git
cd book_manager
```

### 2. Environment Variables

Copy the example environment file and edit as needed:

```bash
cp .env.example .env
```
Edit `.env` to set your database credentials and secret key.

---

## 🖥️ Local Development (without Docker)

> Requires Python 3.12+ and PostgreSQL running locally.

```bash
python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt

# Set environment variables or ensure they are in your .env file

python manage.py migrate
python manage.py runserver
```

App will be available at: http://localhost:8000/

---

## 🐳 Dockerized Setup

> Requires Docker & docker-compose installed.

### Build and Run with Docker

```bash
docker build -t book_manager_app .
docker run -p 8000:8000 book_manager_app
```

App will be available at: http://localhost:8000/

---

### Using Docker Compose (Recommended)

```bash
docker compose up --build

```
- To stop: `docker compose down`

### Run Django Management Commands

```bash
docker compose exec web python manage.py migrate
docker compose exec web python manage.py createsuperuser
docker compose exec web python manage.py shell
```

### Run Tests

```bash
docker compose run --rm web python manage.py test
```

---
## 🛣️ API Endpoints


Base path: `/api/`
- `POST /auth/token/` — obtain JWT (with username/password)
- `POST   /books/` — create
- `GET    /books/` — list 
- `GET    /books/<id>/` — retrieve
- `PUT    /books/<id>/` — update
- `DELETE /books/<id>/` — delete


## 🔎 Filtering, Search, Ordering

- Filtering: `/books/?author=martin&is_available=true`
- Search: `/books/?search=clean`
- Ordering: `/books/?ordering=-published_date`


## 📌 Notes

- If you need to insert a user or test data, use the Django shell:

  ```bash
    docker exec -it <container_name_or_id> /bin/sh
  ```
  
  Then, in the shell:
  ```python
  from django.contrib.auth.models import User
  User.objects.create_user(username='testuser', password='testpass')
  ```
