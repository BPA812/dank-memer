import requests
#Created by BPA812 on Github (2024)
api_url = "https://meme-api.com/gimme"
timesv = int(input('How many memes do you want to generate?'))
memelist = []
for i in range(timesv):
  response = requests.get(api_url)
  resp = response.json()
  while resp['url'] in memelist:
    response = requests.get(api_url)
    resp = response.json()
  while resp['nsfw'] is True:
    response = requests.get(api_url)
    resp = response.json()
  listv = resp['preview']
  memelist.append(resp['url'])
  print('Meme ' + str(i + 1) + ':')
  print('\n')
  print('Meme Title: ' + resp['title'])
  print('Reddit Preview: ' + listv[-1])
  print('Image URL: ' + resp['url'])
  print('Subreddit: r/' + resp['subreddit'])
  print('\n')
