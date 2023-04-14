from eat_it.app import app

UNIMPLEMENTED = 200


def test_app_user_create_endpoint() -> None:
    payload = {"first_name": "Jan", "last_name": "Kowalski"}
    client = app.test_client()
    response = client.post(path='/users', json=payload)
    assert response.status_code == UNIMPLEMENTED


def test_app_user_update_endpoint() -> None:
    payload = {"first_name": "Jan", "last_name": "Kowalski"}
    client = app.test_client()
    response = client.put(path='/users/1', json=payload)
    assert response.status_code == UNIMPLEMENTED


def test_app_user_get_endpoint() -> None:
    payload = {"first_name": "Jan", "last_name": "Kowalski"}
    client = app.test_client()
    response = client.get(path='/users/1', json=payload)
    assert response.status_code == UNIMPLEMENTED


def test_app_user_delete_endpoint() -> None:
    payload = {"first_name": "Jan", "last_name": "Kowalski"}
    client = app.test_client()
    response = client.delete(path='/users/1', json=payload)
    assert response.status_code == UNIMPLEMENTED


def test_app_user_get_endpoint() -> None:
    payload = {"first_name": "Jan", "last_name": "Kowalski"}
    client = app.test_client()
    response = client.get(path='/users/1', json=payload)
    assert response.status_code == UNIMPLEMENTED


def test_app_user_delete_endpoint() -> None:
    payload = {"first_name": "Jan", "last_name": "Kowalski"}
    client = app.test_client()
    response = client.delete(path='/users/1', json=payload)
    assert response.status_code == UNIMPLEMENTED


def test_app_user_patch_endpoint() -> None:
    payload = {"first_name": "Jan", "last_name": "Kowalski"}
    client = app.test_client()
    response = client.patch(path='/users/1', json=payload)
    assert response.status_code == UNIMPLEMENTED


def test_app_users_get_endpoint() -> None:
    payload = {"first_name": "Jan", "last_name": "Kowalski"}
    client = app.test_client()
    response = client.get(path='/users/1', json=payload)
    assert response.status_code == UNIMPLEMENTED
