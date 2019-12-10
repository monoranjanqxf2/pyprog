import requests,json
url="https://openweathermap.org/find?q="
location="bangalore"
url2="https://openweathermap.org/find?q="+location+"&?appid=e314f45649acb17fe6f6f3640e7b30cf"
response=requests.get(url2)
x=response
print(x)

