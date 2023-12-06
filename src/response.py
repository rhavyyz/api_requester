import requests

from utils.format_json_string import fortmat_json_string 

class Response:
    def __init__(self, r : requests.Response) -> None:
        self.status_code = r.status_code
        self.body = r.json()

    def __str__(self) -> str:
        return self.status_code.__str__().strip() + "\n\nbody:\n\n" + fortmat_json_string(self.body.__str__()) 
        