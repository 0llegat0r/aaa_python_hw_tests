from what_is_year_now import what_is_year_now
import unittest
from unittest.mock import patch, MagicMock
import urllib
import json
import io


class TestWIYN(unittest.TestCase):
    def setUp(self):
        self.urllib = MagicMock(urllib)

    @patch('what_is_year_now.urllib')
    @patch('what_is_year_now.json')
    def test_YYYY_MM_DD(self, mock_json, mock_urllib):
        json_str = '{"currentDateTime": "2020-12-01"}'
        ctx_manager = mock_urllib.request.urlopen.return_value.__enter__
        ctx_manager.return_value = json_str
        mock_json.load.return_value = json.loads(json_str)
        self.assertEqual(what_is_year_now(), 2020)

    @patch('what_is_year_now.urllib')
    def test_DD_MM_YYYY(self, mock_urllib):
        s = '{"currentDateTime": "01.12.2020"}'
        resp = io.StringIO(s)  # HTTPResponse()
        mock_urllib.request.urlopen.return_value.__enter__.return_value = resp
        self.assertEqual(what_is_year_now(), 2020)

    @patch('what_is_year_now.urllib')
    def test_invalid_format(self, mock_urllib):
        s = '{"currentDateTime": "12-01-2020"}'
        resp = io.StringIO(s)
        mock_urllib.request.urlopen.return_value.__enter__.return_value = resp
        with self.assertRaises(ValueError):
            what_is_year_now()


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
