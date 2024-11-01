import requests

from endpoints.base_api import BaseApi
from data import constans
from models.meme_oblect import MemeObject

class DeleteMeme(BaseApi):
    def delete_meme(self, meme_id):
        headers = {"Authorization": self.token}
        self.response = requests.delete(
            f'{constans.BASE_URL}/{constans.MEME_POSTFIX}/{meme_id}', headers=headers
        )

    @property
    def data(self):
        return MemeObject(**self.response_json)
