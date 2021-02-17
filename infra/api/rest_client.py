import json
from http import HTTPStatus

import requests
from requests.auth import HTTPBasicAuth

from main_config import config

basic_auth = HTTPBasicAuth(config['basic_auth']['username'], config['basic_auth']['password'])
content_type_json = {'Content-type': 'application/json'}


class RestClient:

    def __init__(self, base_url):
        self.base_url = base_url

    #######
    # GET #
    #######
    def get(self, path, expected_response_status_code: int = HTTPStatus.OK):
        url = self.base_url + path
        self._report(f"GET: {url}")
        response = requests.get(url, auth=basic_auth)
        self._report(self.__response_to_str(response))
        self.__assert_response_status_code("GET", url, response, expected_response_status_code)
        return response

    ########
    # POST #
    ########
    def post(self, path, payload, expected_response_status_code: int = HTTPStatus.OK):
        url = self.base_url + path
        request_body = self.__payload_to_json_str(payload)
        self._report("POST: " + url + "\n" + request_body)
        response = requests.post(url, data=request_body, auth=basic_auth, headers=content_type_json)
        self._report(self.__response_to_str(response))
        self.__assert_response_status_code("POST", url, response, expected_response_status_code)
        return response

    #######
    # PUT #
    #######
    def put(self, path, payload, expected_response_status_code: int = HTTPStatus.OK):
        url = self.base_url + path
        request_body = self.__payload_to_json_str(payload)
        self._report("PUT: " + url + "\n" + request_body)
        response = requests.put(url, data=request_body, auth=basic_auth, headers=content_type_json)
        self._report(self.__response_to_str(response))
        self.__assert_response_status_code("PUT", url, response, expected_response_status_code)
        return response

    ##########
    # DELETE #
    ##########
    def delete(self, path, expected_response_status_code: int = HTTPStatus.OK):
        url = self.base_url + path
        self._report(f"DELETE: {url}")
        response = requests.delete(url, auth=basic_auth, headers=content_type_json)
        self._report(self.__response_to_str(response))
        self.__assert_response_status_code("DELETE", url, response, expected_response_status_code)
        return response

    #########
    # PATCH #
    #########
    def patch(self, path, payload, expected_response_status_code: int = HTTPStatus.OK):
        url = self.base_url + path
        request_body = self.__payload_to_json_str(payload)
        self._report("PATCH: " + url + "\n" + request_body)
        response = requests.patch(url, data=request_body, auth=basic_auth, headers=content_type_json)
        self._report(self.__response_to_str(response))
        self.__assert_response_status_code("PATCH", url, response, expected_response_status_code)
        return response

    @staticmethod
    def _report(message):
        print(message+"\n")
        pass

    @staticmethod
    def __response_to_str(response):

        response_body_str = response.text
        if len(response_body_str) > 400:
            response_body_str = response_body_str[0:400] + " ..."

        return f"RESPONSE: {RestClient.__get_response_status_code_and_description(response)}\n{response_body_str}"

    @staticmethod
    def __get_response_status_code_and_description(response):
        return f"{str(response.status_code)} ({requests.status_codes._codes[response.status_code][0].upper()})"

    @staticmethod
    def __assert_response_status_code(request_type, request_url, response, expected_response_status_code: int):
        if expected_response_status_code != -1 and response.status_code != expected_response_status_code:
            assert False, f"{request_type}: {request_url}\nBad Response: {RestClient.__response_to_str(response)}"

    @staticmethod
    def __payload_to_json_str(payload):
        if type(payload) is dict:
            json_str = json.dumps(payload)
            return json_str
        elif type(payload) is str:
            return payload