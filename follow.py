# Twitter v1.1 API examples here: https://repl.it/@aneagoie/TweetTweet
import tweepy
from other import  keys
import time

def authenticate_user():
    client = tweepy.Client(
        bearer_token = keys.bearer_token,
        consumer_key = keys.api_key,
        consumer_secret = keys.api_secret,
        access_token = keys.access_token,
        access_token_secret = keys.access_token_secret
    )
    return client


def verify_account(client):
    while True:
        try:
            handle = input("Which user's follower would you like to follow? ")
            if handle == '':
                continue

            user_data = client.get_user(username=handle)
            user_id = user_data[0]['id']
            return user_id

        except TypeError as err:
            print('Not a valid user')


def follow_users_following(client, id):
    following = [follower[0] for follower in tweepy.Paginator(client.get_users_following, id)]

    for follower in following[0]:
        try:
            client.follow_user(follower['id'])
            print(f"You are now following {follower}")
        except tweepy.Forbidden as err:
            print(err.response)
    time.sleep(20)

if __name__ == '__main__':
    client = authenticate_user()
    user_id = verify_account(client)
    follow_users_following(client, user_id)
    print('All done.')