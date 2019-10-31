import base64
import requests

print("Enter twitter handle:")
text = input()

#secret key and key 
client_key = "LX6RcfNwWXBNKkykJrx4Ja34Z"
client_secret = "6XkrAzUgLmGjQ40fuI06g60usOFAbYVzgonzdds1XUUiYfjjrI"
#token generated
key_secret = '{}:{}'.format(client_key,client_secret).encode('ascii')
base64_encoded_key = base64.b64encode(key_secret)
base64_encoded_key = base64_encoded_key.decode('ascii')

base_url = 'https://api.twitter.com/'
auth_url = '{}oauth2/token'.format(base_url)

auth_headers = {
'Authorization': 'Basic {}'.format(base64_encoded_key),
'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
}

auth_data = {
'grant_type': 'client_credentials'
}

auth_resp = requests.post(auth_url, headers=auth_headers, data=auth_data)
access_token = auth_resp.json()['access_token']

#tweet fetch
search_headers = {
'Authorization': 'Bearer {}'.format(access_token)    
}

search_params = {
'screen_name':text,
'q': text,
'result_type': 'recent',
'count': 10
}

search_url = '{}1.1/statuses/user_timeline.json'.format(base_url)

search_resp = requests.get(search_url, headers=search_headers, params=search_params)

tweet_data = search_resp.json()


tweets = []
if search_resp.status_code == 200:
 tweets = []
 for x in tweet_data:
    tweets.append(x['text'])
 if tweets == []:
    tweets.append('Nothing to display') 
elif search_resp.status_code == 404:
 tweets = []
 tweets.append('No results!! Check whether the user handle entered is valid.')
else:
 tweets.append('Nothing to display')
      
print(tweets)
