# Bug Report 001

## Bug ID: BUG_001

## Title: POST /tasks returns 200 instead of 201 on successful task creation

## Severity: Medium

## Priority: High

## Environment:
- API: Task Manager API
- Tool: Postman
- Server: localhost:5000

## Steps to Reproduce:
1. Start the Flask server (python app.py)
2. Open Postman
3. Send POST request to http://127.0.0.1:5000/tasks
4. Set body to {"title": "Buy groceries"}
5. Click Send

## Expected Result:
Status code 201 CREATED returned along with the created task in response body

## Actual Result:
Status code 200 OK returned instead of 201 CREATED

## Impact:
Frontend applications and other systems rely on status code 201 to confirm
a new resource was created. Returning 200 causes confusion and may break
client side logic that checks for 201 on creation.

## Status: Open