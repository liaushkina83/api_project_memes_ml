import pytest
import requests

from endpoints.get_meme_list import GetMemeList
from endpoints.get_meme_by_id import GetMemeById
from endpoints.create_meme import CreateMeme
from endpoints.delete_meme import DeleteMeme
from endpoints.update_meme import UpdateMeme
from data import payload

@pytest.fixture()
def get_meme_list_endpoint():
    return GetMemeList()

@pytest.fixture()
def get_one_meme_endpoint():
    return GetMemeById()

@pytest.fixture()
def create_meme_endpoint():
    return CreateMeme()

@pytest.fixture()
def update_meme_endpoint():
    return UpdateMeme()

@pytest.fixture()
def delete_meme_endpoint():
    return DeleteMeme()

@pytest.fixture()
def mem_id(create_meme_endpoint, delete_meme_endpoint):
    create_meme_endpoint.do_authorize()
    create_meme_endpoint.create_meme(payload.DEFAULT_PAYLOAD_NEW_MEME)
    assert create_meme_endpoint.response.status_code == 200, "cannot create meme"
    this_id = create_meme_endpoint.response_json['id']
    yield this_id
    delete_meme_endpoint.delete_meme(this_id)


@pytest.fixture(scope="session")
def create_authorize():
    payload = {
        "name": "Margarita",
        }
    headers = {"Content-Type": 'application/json'}
    response = requests.post(
        "http://167.172.172.115:52355/authorize",
        json=payload,
        headers=headers
    )
    data = response.json()
    my_token = data["token"]
    print(f"Received token: {my_token}")
    return my_token


@pytest.fixture(scope="function")
def create_meme(create_authorize):
    headers = {"Authorization": create_authorize}
    payload = {
        "text": "Иван Иванов",
        "url": "ddd",
        "tags": ["blue", "red"],
        "info": {}
        }
    response = requests.post(
        f"http://167.172.172.115:52355/meme",
        headers=headers,
        json=payload
    )
    assert response.status_code == 200, f"Failed to added new meme: {response.status_code}"

    mem_id = response.json()["id"]
    yield mem_id

    requests.delete(
        f"http://167.172.172.115:52355/meme/{mem_id}",
        headers=headers
    )
