import json
from src.request import Request
from src.response import Response

global data

with open("requests.json") as f:
    data = json.load(f)

data = [Request(req) for req in data]

with open("results.txt", "w+") as f:
    for i, req in enumerate(data):
        res = Response(req.make())

        f.writelines([
            "\n"+ "=" * 25 + "New Request" + "="* 25,
            "\n" + req.__str__(),
            "\n" + "-" * 60,
            "\n" + res.__str__()
        ])