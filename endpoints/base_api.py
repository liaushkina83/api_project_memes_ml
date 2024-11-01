from abc import abstractmethod

import allure
from requests import Response
import requests
from data import constans

class BaseApi:
    response: Response

    def __init__(self):
        self.token = None

    @allure.step('Make authorization')
    def make_authorize(self):
        payload = {
            "name": "Margarita",
        }
        headers = {"Content-Type": 'application/json'}
        response = requests.post(
            f"{constans.BASE_URL}/{constans.AUTORIZ}",
            json=payload,
            headers=headers
        )
        assert response.status_code == 200
        data = response.json()
        self.token = data["token"]

    @allure.title('Check is token alive')
    def check_if_token_alive(self):
        headers = {"Content-Type": 'application/json'}
        response = requests.get(
            f"{constans.BASE_URL}/{constans.AUTORIZ}/{self.token}",
            headers=headers
        )
        return response.status_code == 200

    @allure.step('Do authorization')
    def do_authorize(self):
        if self.token is not None:
            is_alive_token = self.check_if_token_alive()
            if is_alive_token == True:
                return

        self.make_authorize()


    @allure.step('Check response status code')
    def check_response_code_is_(self, code):
        assert self.response.status_code == code, "Response does not match with expected"

    @allure.step('Check response field')
    def check_response_field_is_(self, field, value):
        assert self.response.json()[field] == value

    @property
    def response_json(self):
        return self.response.json()

    @property
    @abstractmethod
    def data(self):
        pass
