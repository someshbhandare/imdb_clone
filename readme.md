# Movie List API

This Django-based REST API allows users to view a list of movies with support for pagination, filtering, and sorting. It is designed to be extensible and efficient, providing the necessary functionality for a CRM system to manage movie data.

---

## Features

1. **Pagination**: View movies in pages, with the ability to customize the page size.
2. **Filtering**: Filter movies by:
   - **Year of release** (based on the `release_date` field).
   - **Language** (based on the `original_language` field).
3. **Sorting**: Sort movies by:
   - **Release date**.
   - **Ratings** (average rating).

---

## Requirements

- Python 3.8+
- Django 4.x
- Django REST Framework (DRF)
- PostgreSQL

---

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/someshbhandare/myspace.git
   ```
   
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

4. **Start the development server:**
   ```bash
   python manage.py runserver
    ```

