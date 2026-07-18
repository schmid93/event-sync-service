# Event Sync Service

A full-stack take-home assessment built with **Python (FastAPI)** and **React + TypeScript**.

## Overview

This application ingests meeting data from two independent sources (a CRM and a calendar), reconciles records that refer to the same real world meeting, detects data conflicts, and exposes the unified result through a REST API and a simple web interface.

---

## Tech Stack

### Backend

- Python 3.12
- FastAPI
- Pydantic
- Uvicorn

### Frontend

- React
- TypeScript
- Vite

---

## Project Structure

```text
event-sync-service/
│
├── backend/                 # FastAPI REST API
│   ├── app/
│   └── requirements.txt
│
├── frontend/                # React + TypeScript application
│   └── src/
│
├── docs/                    # Architecture decisions and documentation
│
└── README.md
```

The project is cleanly separated into two independent applications to improve maintainability and keep frontend and backend concerns isolated.

---

## Current Progress

The initial project setup has been completed:

- ✅ Python virtual environment configured
- ✅ FastAPI backend initialized
- ✅ Health check endpoint (`/health`)
- ✅ React + Vite frontend scaffolded
- ✅ Project structure defined
- ✅ Git repository initialized

The backend currently exposes a simple health endpoint to verify that the API is running correctly.

---

# Running the Project

## Backend

```bash
cd backend

python -m venv .venv
```

### Windows

```bash
.venv\Scripts\activate
```

### macOS / Linux

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the API:

```bash
uvicorn app.main:app --reload
```

The backend will be available at:

- API: http://localhost:8000
- Swagger UI: http://localhost:8000/docs

---

## Frontend

```bash
cd frontend

npm install
npm run dev
```

The frontend will be available at:

- http://localhost:5173

---

## Notes

This project is being developed step by step. As new functionality is added, architectural decisions, assumptions, and trade-offs will be documented to explain the reasoning behind the implementation.
