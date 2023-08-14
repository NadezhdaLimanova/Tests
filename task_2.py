import requests
import unittest
from unittest import TestCase
import pytest


"""Тест через unittest"""

class TestYandex(TestCase):

    def test_create_folder(self):
        self.path = 'test'  # название папки
        self.token = ' '  # вписать токен
        self.headers = {'Authorization': f'OAuth {self.token}'}
        self.url_create = 'https://cloud-api.yandex.net/v1/disk/resources'
        res = requests.put(f'{self.url_create}?path={self.path}', headers=self.headers)
        result = res.status_code
        expected_result = 201
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()

"""Тесты через pytest"""

@ pytest.mark.parametrize('expected',
                          [
                              (409)
                              ]
                          )
def test_create_folder(expected):
        path = 'test'  # название папки
        token = ' '  # вписать токен
        headers = {'Authorization': f'OAuth {token}'}
        url_create = 'https://cloud-api.yandex.net/v1/disk/resources'
        res = requests.put(f'{url_create}?path={path}', headers=headers)
        result = res.status_code
        assert result == expected


@ pytest.mark.xfail
def test_create_folder_fail():
        path = 'test'  # название папки
        token = ' '  # вписать токен
        headers = {'Authorization': f'OAuth {token}'}
        url_create = 'https://cloud-api.yandex.net/v1/disk/resources'
        res = requests.put(f'{url_create}?path={path}', headers=headers)
        expected = 201
        result = res.status_code
        assert result == expected