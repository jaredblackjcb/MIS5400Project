# Twitter API:
# https://github.com/bear/python-twitter

import twitter

CONSUMER_KEY = 'O0yCU2nVnQrXPMJEOM2P182iE'
CONSUMER_SECRET = 'wC72lN3SnvPxh4N643yu6QnxCoQmg0GVcbLkAKYuAf64xOM24w'
ACCESS_TOKEN = '1089923587681673216-1apbN0HdirrYhiPpnjmwx2zsSS2nqQ'
ACCESS_TOKEN_SECRET = '7OY5RD8gJ0KXnnRMhTI74kCJds9NM3FKe5BQE62E2HUi3 '

api = twitter.Api(
                consumer_key=CONSUMER_KEY
              , consumer_secret=CONSUMER_SECRET
              , access_token_key=ACCESS_TOKEN
              , access_token_secret=ACCESS_TOKEN_SECRET
              )

users = api.GetFriends()

print([u.screen_name for u in users])