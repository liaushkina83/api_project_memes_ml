import requests
import allure

from endpoints.base_api import BaseApi
from data import constans
from models.meme_oblect import MemeObject


class UpdateMeme(BaseApi):
    @allure.step('Send PUT request with updates')
    def update_meme(self, payload, meme_id):
        headers = {"Authorization": self.token}
        self.response = requests.put(
            f'{constans.BASE_URL}/{constans.MEME_POSTFIX}/{meme_id}',
            json=payload,
            headers=headers
        )

    @property
    def data(self):
        return MemeObject(**self.response_json)

