import requests

from utils.format_json_string import fortmat_json_string 

class Response:
    def __init__(self, r : requests.Response) -> None:
        self.status_code = r.status_code

        print("="*60,self.status_code, len(r.text), "\n\n\n\n\n")

        if len(r.text) > 0 and self.status_code < 500:
            self.body = r.json()
        elif self.status_code >= 500:
            self.body = r.text
        else:
            self.body = dict()

    def __str__(self) -> str:
        return self.status_code.__str__().strip() + "\n\nbody:\n\n" + fortmat_json_string(self.body.__str__()) 
        