import requests

from utils.format_json_string import fortmat_json_string

class Request:
    method : any
    method_name : str
    url : str
    body : dict

    ___methods = {
        "GET":requests.get,
        "POST":requests.post,
        "DELETE":requests.delete,
        "PUT":requests.put,
    }

    def __init__(self, r : dict) -> None:
        self.method_name = r["method"]
        self.url = r["url"]
        self.method = self.___methods[self.method_name]
        self.body = r.get("body", {})

    def make(self):
        return self.method(url=self.url, json=self.body, headers={'Content-Type': 'application/json'})
    
    def __str__(self) -> str:
        return self.method_name + " : " + self.url + "\n\nbody:\n\n" + fortmat_json_string(self.body.__str__()) 