# Task Manager API — QA Testing Project

A REST API built with Python Flask, created as a QA testing practice project.
The main focus is on manual testing, bug reporting, and test automation.

## Project Overview
This project demonstrates end-to-end QA testing skills including:
- Manual API testing using Postman
- Test case design and documentation
- Bug identification and reporting
- Automated testing using Pytest

## Tech Stack
- Python, Flask (API)
- Postman (Manual Testing)
- Pytest + Requests (Automation)

## API Endpoints
| Method | Endpoint | Description |
|---|---|---|
| POST | /tasks | Create a new task |
| GET | /tasks | Get all tasks |
| GET | /tasks/{id} | Get single task |
| PUT | /tasks/{id} | Update a task |
| DELETE | /tasks/{id} | Delete a task |

## Testing Summary
| Type | Count |
|---|---|
| Manual Test Cases | 25 |
| Automated Test Cases | 18 |
| Bug Reports | 3 |

## How to Run the API
1. Install Flask: `pip install flask`
2. Run server: `python app.py`
3. API runs on: `http://127.0.0.1:5000`

## How to Run Automated Tests
1. Install dependencies: `pip install pytest requests`
2. Make sure Flask server is running
3. Run: `python -m pytest test_tasks.py -v`

## Test Cases
All 25 manual test cases are documented in Google Sheets covering:
- Functional testing
- Negative testing
- Boundary value testing
- Edge case testing
- Full flow testing

## Bug Reports
Three bugs were identified and documented:
- BUG_001: POST /tasks returns 200 instead of 201
- BUG_002: DELETE /tasks/{id} returns 200 instead of 204
- BUG_003: GET /tasks/{id} returns 201 instead of 200

## Postman Collection
Import `Task manager API tests.postman_collection.json` into Postman
to run all saved API requests directly.
