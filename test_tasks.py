import requests

BASE_URL = "http://127.0.0.1:5000"

# ===== FUNCTIONAL TESTS =====

def test_create_task_valid_title():
    response = requests.post(f"{BASE_URL}/tasks", json={"title": "Buy groceries"})
    assert response.status_code == 201
    assert response.json()["title"] == "Buy groceries"
    assert response.json()["completed"] == False

def test_create_task_with_description():
    response = requests.post(f"{BASE_URL}/tasks", json={"title": "Buy groceries", "description": "milk, eggs"})
    assert response.status_code == 201
    assert response.json()["description"] == "milk, eggs"

def test_create_task_completed_true():
    response = requests.post(f"{BASE_URL}/tasks", json={"title": "Buy groceries", "completed": True})
    assert response.status_code == 201
    assert response.json()["completed"] == True

def test_get_all_tasks():
    response = requests.get(f"{BASE_URL}/tasks")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_single_task():
    create = requests.post(f"{BASE_URL}/tasks", json={"title": "Test task"})
    task_id = create.json()["id"]
    response = requests.get(f"{BASE_URL}/tasks/{task_id}")
    assert response.status_code == 200
    assert response.json()["id"] == task_id

def test_update_task_title():
    create = requests.post(f"{BASE_URL}/tasks", json={"title": "Old title"})
    task_id = create.json()["id"]
    response = requests.put(f"{BASE_URL}/tasks/{task_id}", json={"title": "New title"})
    assert response.status_code == 200
    assert response.json()["title"] == "New title"

def test_delete_task():
    create = requests.post(f"{BASE_URL}/tasks", json={"title": "Delete me"})
    task_id = create.json()["id"]
    response = requests.delete(f"{BASE_URL}/tasks/{task_id}")
    assert response.status_code == 204

def test_get_deleted_task():
    create = requests.post(f"{BASE_URL}/tasks", json={"title": "Delete me"})
    task_id = create.json()["id"]
    requests.delete(f"{BASE_URL}/tasks/{task_id}")
    response = requests.get(f"{BASE_URL}/tasks/{task_id}")
    assert response.status_code == 404

# ===== NEGATIVE TESTS =====

def test_create_task_empty_title():
    response = requests.post(f"{BASE_URL}/tasks", json={"title": ""})
    assert response.status_code == 400

def test_create_task_no_title_field():
    response = requests.post(f"{BASE_URL}/tasks", json={})
    assert response.status_code == 400

def test_create_task_no_body():
    response = requests.post(f"{BASE_URL}/tasks")
    assert response.status_code == 400

def test_create_task_title_as_number():
    response = requests.post(f"{BASE_URL}/tasks", json={"title": 12345})
    assert response.status_code == 400

def test_create_task_completed_as_string():
    response = requests.post(f"{BASE_URL}/tasks", json={"title": "Buy groceries", "completed": "yes"})
    assert response.status_code == 400

def test_get_nonexistent_task():
    response = requests.get(f"{BASE_URL}/tasks/999")
    assert response.status_code == 404

def test_update_nonexistent_task():
    response = requests.put(f"{BASE_URL}/tasks/999", json={"title": "Test"})
    assert response.status_code == 404

def test_delete_nonexistent_task():
    response = requests.delete(f"{BASE_URL}/tasks/999")
    assert response.status_code == 404

# ===== BOUNDARY TESTS =====

def test_create_task_title_100_chars():
    title = "a" * 100
    response = requests.post(f"{BASE_URL}/tasks", json={"title": title})
    assert response.status_code == 201

def test_create_task_title_101_chars():
    title = "a" * 101
    response = requests.post(f"{BASE_URL}/tasks", json={"title": title})
    assert response.status_code == 400