from urllib.request import urlopen


# GET
http_response = urlopen('https://movie.naver.com/movie/sdb/rank/rmovie.nhn')
body = http_response.read()
html = body.decode("cp949")
print(html)