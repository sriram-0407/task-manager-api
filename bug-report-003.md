# Bug Report 003

## Bug ID: BUG_003

## Title: GET /tasks/{id} returns 201 instead of 200 on successful fetch

## Severity: Medium

## Priority: High

## Environment:
- API: Task Manager API
- Tool: Postman
- Server: localhost:5000

## Steps to Reproduce:
1. Start the Flask server (python app.py)
2. Create a task via POST /tasks with {"title": "Buy groceries"}
3. Note the id returned in response
4. Send GET request to http://127.0.0.1:5000/tasks/{id}
5. Click Send

## Expected Result:
Status code 200 OK returned with task data in response body

## Actual Result:
Status code 201 returned instead of 200 OK

## Impact:
GET requests should always return 200 OK when data is found successfully.
Returning 201 on a GET request is incorrect as 201 means resource was
created which is misleading and breaks REST API standards.

## Status: Open