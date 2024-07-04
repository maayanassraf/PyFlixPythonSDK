import unittest
from unittest.mock import patch, Mock
from src.client import Client


class TestClient(unittest.TestCase):

    def setUp(self):
        self.api_key = 'test_api_key'
        self.client = Client(self.api_key)

    @patch('src.client.requests.get')
    def test_search_movies(self, mock_get):
        mock_response = Mock()
        expected_result = {'results': [{'title': 'Test Movie'}]}
        mock_response.json.return_value = expected_result
        mock_get.return_value = mock_response

        result = self.client.search_movies('test')

        self.assertEqual(result, expected_result)
        mock_get.assert_called_once_with(
            'https://api.netflix.com/movies/search',
            headers={
                'Authorization': f'Bearer {self.api_key}',
                'Content-Type': 'application/json'
            },
            params={'query': 'test'}
        )

    @patch('src.client.requests.get')
    def test_get_movie_details(self, mock_get):
        mock_response = Mock()
        expected_result = {'id': '12345', 'title': 'Test Movie'}
        mock_response.json.return_value = expected_result
        mock_get.return_value = mock_response

        result = self.client.get_movie_details('12345')

        self.assertEqual(result, expected_result)
        mock_get.assert_called_once_with(
            'https://api.netflix.com/movies/12345',
            headers={'Authorization': f'Bearer {self.api_key}'}
        )


if __name__ == '__main__':
    unittest.main()
