import json
import pytest
from eat_it.controllers import AddUserController, AddUserRequest


@pytest.fixture
def payload() -> dict:
    return {"first_name": "Magda", "last_name": "Saturska"}


@pytest.fixture
def client() -> None:
    with pytest.raises(NotImplementedError):
        yield


def test_get_user(client) -> None:
    with pytest.raises(NotImplementedError):
        response = client.get("/users")
        assert response.status_code == 501


def test_add_user(client, payload) -> None:
    with pytest.raises(NotImplementedError):
        response = client.post("/users", data=json.dumps(payload))
        assert response.status_code == 201
        assert response.json == payload


def test_patch_user(client, payload) -> None:
    with pytest.raises(NotImplementedError):
        response = client.patch("/users/1", data=json.dumps(payload))
        assert response.status_code == 200
        assert response.json == payload


def test_delete_user(client) -> None:
    with pytest.raises(NotImplementedError):
        response = client.delete("/users/1")
        assert response.status_code == 204


def test_put_user(client, payload) -> None:
    with pytest.raises(NotImplementedError):
        response = client.put("/users", data=json.dumps(payload))
        assert response.status_code == 200
        assert response.json == payload
