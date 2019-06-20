from http.client import HTTPConnection

conn = HTTPConnection('www.example.com')

# 성공
# GET / HTTP/1.1
# 200 OK
# conn.request('GET', '/')
# res = conn.getresponse()
# print(res.status, res.reason)

# if res.reason == 200:
#     body = res.read()
#     print(body)


# 실패
# GET /hello.html / HTTP/1.1
# 404 Not Found
conn.request('GET', '/hello.html')
res = conn.getresponse()
print(res.status, res.reason)
