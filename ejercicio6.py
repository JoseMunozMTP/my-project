import unittest


class TestSuma(unittest.TestCase):

    def test_request_post(self):
        import requests

        URL = 'https://mtp.alejmans.dev/maas/proxy/test/suma'

        A = 1
        B = 2

        data = {
            "a": A,
            "b": B
        }

        response = requests.post(URL, json=data)

        print('Resultado POST:', response.json()["result"])

        self.assertEqual(response.json()["result"], 3)

    def test_request_get(self):
        import requests

        URL = 'https://mtp.alejmans.dev/maas/proxy/test/suma'

        A = 1
        B = 2

        data = {
            "a": A,
            "b": B
        }

        response = requests.get(URL, params=data)

        print('Resultado GET:', response.text)

        self.assertEqual(float(response.text), 3)


if __name__ == '__main__':
    unittest.main()
