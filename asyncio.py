from aiohttp import ClientSession
import json
import asyncio 


async def make_request(url):
  client = ClientSession()
  response = await client.get(url)
  print("Запрос отправлен")
  print(url)
  print()
  json_data = await response.json()
  await client.close()
  print("Запрос получен")
  print(url)
  print(json_data['name'])
  print()
  return json_data['name']


async def main():
  cor_1 = make_request('http://swapi.dev/api/people/1')
  cor_2 = make_request('http://swapi.dev/api/people/2')
  cor_3 = make_request('http://swapi.dev/api/people/3')
  cor_4 = make_request('http://swapi.dev/api/people/4')
  reponse = await asyncio.gather(cor_1,cor_2,cor_3,cor_4)
  print(reponse)


asyncio.run(main())