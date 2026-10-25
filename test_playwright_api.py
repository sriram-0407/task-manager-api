"""
Test Case: TC_PW_001 - Verify GET /tasks returns a valid list using Playwright
Preconditions: Flask server running locally on http://127.0.0.1:5000
Test Steps:
    1. Send a GET request to /tasks using Playwright's request client
    2. Check the response status code and structure
Expected Result: Status 200, response is a list (even if empty)
"""

import pytest


def test_get_all_tasks(playwright):
    request_context = playwright.request.new_context(base_url="http://127.0.0.1:5000")

    response = request_context.get("/tasks")

    print("Status code:", response.status)
    print("Response body:", response.json())

    assert response.status == 200, f"Expected 200, got {response.status}"
    assert isinstance(response.json(), list), "Expected response to be a list"

    print("TC_PW_001 PASSED: GET /tasks returned a valid list using Playwright")

    request_context.dispose()