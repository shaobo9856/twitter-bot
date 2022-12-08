import tweepy
from other import keys
import openpyxl
import time

def api():
    #auth = tweepy.OAuth2BearerHandler(keys.client_id,keys.client_secret)  # tweepy.OAuth2AppHandler(keys.client_id,keys.client_secret)
    auth = tweepy.OAuthHandler(keys.api_key, keys.api_secret)
    auth.set_access_token(keys.access_token, keys.access_token_secret)
    return tweepy.API(auth)


def tweet(api: tweepy.API, message: str, image_path = None):
    if image_path :
        api.update_status_with_media(message, image_path)
    else:
        api.update_status(message)
    print("tweeted successfully!")


if __name__ == '__main__':
    api = api()
    data = openpyxl.load_workbook(r'drafts.xlsx')
    sheet1 = data.worksheets[0]

    while True:
        try:
            for index, row in enumerate(sheet1.rows):
                if index == 0:
                    continue
                if row[0].value == "no":
                    content = row[1].value
                    print(content)
                    tweet(api, content)
                    row[0].value = "yes"
                    data.save(filename=r'drafts.xlsx')
                    break
        except:
            print("error")

        time.sleep(14400)
