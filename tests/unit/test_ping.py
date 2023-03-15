from eat_it.app import users, user, create_user, delete_user, update_user
from eat_it.app import app


def test_create_user_returns_user():
    payload = {"first_name": "Magda", "last_name": "Saturska"}
    with app.test_request_context(method="POST", path="/users", json=payload):
        result = create_user()
    assert result.json == payload


def test_update_user_returns_user():
    payload = {"first_name": "Tosia", "last_name": "Saturska"}
    with app.test_request_context(method="PUT", path="/users/1", json=payload):
        result = update_user()
    assert result.json == payload


def test_user_returns_200_response_patch():
    result = user(1)
    assert result.status_code == 200


def test_delete_user_returns_204_response_delete():
    result = delete_user(1)
    assert result.status_code == 204


