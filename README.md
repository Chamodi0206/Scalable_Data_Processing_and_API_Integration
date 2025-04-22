# 🌐 FastAPI-Based Scalable Data Ingestion & Integration System

Welcome! 👋 This repository is about building a scalable and modular backend system that can fetch, process, and expose data via APIs. It demonstrates real-world API integration using **FastAPI**, **SQLAlchemy**, **asynchronous programming**, and clean architecture principles.

---

## 🧠 Project Overview

The goal of this system is to:

- Connect with **external APIs** (REST & GraphQL).
- Fetch structured user and country data.
- Store it safely in a local SQL database.
- Expose the data through a **RESTful API** built with FastAPI.
- Ensure **performance, reliability, and modularity** for production-ready extensibility.

This isn’t just about writing code — it’s about designing for scale, clarity, and robustness.

---

## ⚙️ Core Architecture

The project is built around a **modular backend service** using:

### 🔧 Key Technologies

| Component         | Purpose                                            |
|------------------|----------------------------------------------------|
| `FastAPI`         | High-performance web framework for API endpoints. |
| `SQLAlchemy`      | ORM layer to interact with the SQLite database.   |
| `httpx`           | For making async requests to external APIs.       |
| `Pydantic`        | Request/response data validation and typing.      |
| `logging`         | Custom timestamped logger for transparency.       |

---

## 📂 Modules Breakdown

### 1. **Data Fetching Modules**
- `fetch_users.py`: Pulls user data from a public REST API.
- `fetch_countries.py`: Queries a GraphQL API to gather country details.
- Both modules are wrapped in error handling and logging for resilience.

### 2. **Database Management**
- `models.py`: Defines the schema using SQLAlchemy.
- `crud.py`: Manages all DB operations with safe insertions (no duplicates).

### 3. **API Layer**
- `main.py`: Ties everything together, exposing clean `/users` and `/countries` endpoints.
- Built with clarity, documentation, and extensibility in mind.

---

## 🔄 Real-Time & Parallel Processing Options

To support scalability and performance under high data load, we’ve planned for several concurrency strategies:

| Approach          | Use Case                          |
|------------------|-----------------------------------|
| **AsyncIO**       | Fast, non-blocking I/O operations. |
| **ThreadPoolExecutor** | Ideal for blocking I/O + parallelism. |
| **Celery + Redis**| Production-ready task queue for retries, scheduling, etc. |

The system is built in a way that these strategies can be plugged in with minimal refactoring.

---

## 🛡️ Error Handling & Logging

Nothing is left to chance — every fetch call is wrapped in robust error-handling blocks, with structured logs to trace what happened and when.

### Sample:
```python
try:
    # fetch logic here
except Exception as e:
    logger.error(f"[User Fetch Error] {e}")
```

This keeps your operations auditable, even when something goes wrong.

---

## 🔐 Data Validation & Security

- All incoming data is validated using **Pydantic schemas**.
- The system avoids redundant inserts by checking for existing records.
- Only safe, structured, and validated data makes it into the DB.

---

## 🌍 Why This Matters

This project simulates what a real-world, scalable backend service would look like in a data-heavy application. It’s not only about *getting data* — it’s about doing so **responsibly**, **cleanly**, and in a way that **future developers will thank you for**.

---

## 🚀 Getting Started

```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
uvicorn app.main:app --reload
```

Visit the API docs at 👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 💬 Final Notes

This work reflects my approach to building maintainable systems that scale. If you’d like to test, extend, or integrate this further, feel free to explore the code and reach out. Thanks for reviewing my work!

— *Chamodi Senarathne*
