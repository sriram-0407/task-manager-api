# Bug Report 002

## Bug ID: BUG_002

## Title: DELETE /tasks/{id} returns 200 instead of 204 on successful deletion

## Severity: Medium

## Priority: High

## Environment:
- API: Task Manager API
- Tool: Postman
- Server: localhost:5000

## Steps to Reproduce:
1. Start the Flask server (python app.py)
2. Create a task via POST /tasks with {"title": "Test delete task"}
3. Note the id returned in response
4. Send DELETE request to http://127.0.0.1:5000/tasks/{id}
5. Click Send

## Expected Result:
Status code 204 No Content returned with empty response body

## Actual Result:
Status code 200 OK returned with response body
{"message": "Task deleted"}

## Impact:
DELETE requests should return 204 No Content as per REST API standards.
Returning 200 with a body on deletion breaks REST conventions and may
confuse client applications expecting empty response on deletion.

## Status: Open