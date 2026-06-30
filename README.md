# FastAPI Task Manager
<img width="1440" height="779" alt="Screenshot 2026-06-23 at 08 56 55" src="https://github.com/user-attachments/assets/6265807e-a157-41b1-a563-22368d9ae988" />


## Overview

FastAPI Task Manager adalah mini project yang dibuat untuk mempelajari backend development menggunakan FastAPI dari nol.

Project ini tidak hanya berfokus pada cara menggunakan FastAPI, tetapi juga bertujuan memahami bagaimana konsep-konsep yang sebelumnya digunakan di Express.js dan Node.js diterapkan dalam ekosistem Python.

Learning Path:

```
Express.js
↓
FastAPI
↓
AI Backend
↓
RAG (Retrieval-Augmented Generation)
↓
Agentic AI
```

---

## Learning Objectives

Melalui project ini, saya ingin memahami:

* Struktur dasar aplikasi FastAPI
* Routing dan HTTP methods
* Request dan Response handling
* Pydantic schema validation
* CRUD API development
* Database integration menggunakan SQLAlchemy
* Authentication menggunakan JWT
* Database migration menggunakan Alembic
* Dockerization
* Backend architecture yang scalable

---

## Tech Stack

### Frontend
- Svelte
- JavaScript (ES6+)
- HTML5
- CSS3

### Backend
- FastAPI
- Uvicorn
- Pydantic

### API
- REST API
- JSON

### Development Tools
- Python Virtual Environment (.venv)
- pip
- npm

### Planned
- SQLAlchemy
- PostgreSQL
- Alembic
- JWT Authentication
- Docker

## Background

Project ini dibuat dengan pendekatan perbandingan antara Express.js dan FastAPI.

Contoh:

### Express.js

```javascript
const express = require("express");
const app = express();
```

### FastAPI

```python
from fastapi import FastAPI

app = FastAPI()
```

Tujuannya adalah memahami konsep yang sama dalam dua ekosistem yang berbeda.

---

## Project Structure (Planned)

```text
fastapi_task_manager/
│
├── app/
│   ├── routers/
│   ├── models/
│   ├── schemas/
│   ├── services/
│   ├── database/
│   └── core/
│
├── tests/
│
├── .venv/
├── requirements.txt
└── main.py
```

---

## Current Progress

### Completed

* Understanding REST API fundamentals
* Understanding Path Parameters
* Understanding Query Parameters
* Creating Python Virtual Environment
* Installing FastAPI
* Installing Uvicorn
* Understanding FastAPI vs Uvicorn
* Understanding project setup

### In Progress

* Creating first FastAPI application
* Understanding decorators in Python
* Understanding FastAPI routing

### Next Topics

1. FastAPI Routing
2. Request Body
3. Pydantic
4. CRUD Operations
5. SQLAlchemy ORM
6. PostgreSQL Integration
7. JWT Authentication
8. Alembic Migration
9. Docker
10. Clean Architecture

---

## Environment Setup

Create virtual environment:

```bash
python3 -m venv .venv
```

Activate virtual environment:

Mac/Linux:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install fastapi uvicorn
```

---

## Run Development Server

```bash
uvicorn main:app --reload
```

Example output:

```text
INFO:     Uvicorn running on http://127.0.0.1:8000
```

---

## Learning Notes

### FastAPI vs Uvicorn

FastAPI:

```text
Framework
```

Uvicorn:

```text
ASGI Web Server
```

Analogy:

```text
FastAPI + Uvicorn
≈
Express.js Runtime Environment
```

---

## Future Features

* Task CRUD
* User Authentication
* User Authorization
* Task Categories
* Task Status Tracking
* Pagination
* Search and Filtering
* Docker Deployment
* Unit Testing
* CI/CD Pipeline

---

## Status

🚧 Learning Project — Active Development

This repository is intended for learning FastAPI fundamentals before applying the same concepts to larger production projects.
