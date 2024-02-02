import requests
from constants.global_constants import BACKEND_URL

class Test_Api:
    def setup_method(self):
        self.response = requests.get(BACKEND_URL)

    def test_statusCode(self):
        assert self.response.status_code == 200

    def test_contentType(self):
        content_type = self.response.headers.get("Content-Type")
        assert content_type == "application/json"

    def test_response_content_format(self):
        json_data = self.response.json()
        assert "data" in json_data
        for flight in json_data["data"]:
            assert "id" in flight and isinstance(flight["id"], int)
            assert "from" in flight and isinstance(flight["from"], str)
            assert "to" in flight and isinstance(flight["to"], str)
            assert "date" in flight and isinstance(flight["date"], str)

        
