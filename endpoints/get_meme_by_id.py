import requests

from data import constans
from endpoints.base_api import BaseApi
from models.meme_oblect import MemeObject


class GetMemeById(BaseApi):
    def get_meme_by_id(self, meme_id):
        headers = {"Authorization": self.token}
        self.response = requests.get(f'{constans.BASE_URL}/{constans.MEME_POSTFIX}/{meme_id}', headers=headers)

    @property
    def data(self):
        return MemeObject(**self.response_json)

    def check_meme_id_is_(self, meme_id):
        assert self.data.id == meme_id
