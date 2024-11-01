import requests

from endpoints.base_api import BaseApi
from data import constans
from models.meme_oblect import MemeObject


class CreateMeme(BaseApi):
    def create_meme(self, payload):
        headers = {"Authorization": self.token}
        self.response = requests.post(
            f'{constans.BASE_URL}/{constans.MEME_POSTFIX}',
            json=payload,
            headers=headers
        )

    @property
    def data(self):
        return MemeObject(**self.response_json)
