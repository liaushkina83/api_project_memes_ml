import requests
import allure
from data import constans
from endpoints.base_api import BaseApi
from models.meme_oblect import MemeObject


class GetMemeList(BaseApi):
    @allure.step('Get all memes')
    def get_memes_list(self):
        headers = {"Authorization": self.token}
        self.response = requests.get(f'{constans.BASE_URL}/{constans.MEME_POSTFIX}', headers=headers)

    @property
    def data(self):
        return MemeObject(**self.response_json)

