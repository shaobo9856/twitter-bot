import tweepy
from other import keys

client = tweepy.Client(bearer_token=keys.bearer_token)

query = "corona -is:retweet"

response = client.search_recent_tweets(query=query,max_results=100)

#print(response)


list = client.get_list(id=1599672026452852739)

print(list.includes)



