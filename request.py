from urllib.parse import urlencode
from urllib.request import urlopen, Request

# GET
httpresponse = urlopen('http://www.example.com?a=10&b=20')
body = httpresponse.read()
# print(body)

# POST
data = {
    'email': 'feel',
    'password': '1234',
    'name': '박필'
}
data = urlencode(data).encode('utf-8')

request = Request('http://www.example.com', data)
request.add_header('Content-Type', 'text/html')

httpresponse = urlopen(request)
