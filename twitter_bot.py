#this is a twitter bot demo  
import twitter

def hello_twitter_bot(friend):
	api = twitter.Api(consumer_key="",
	                  consumer_secret="",
	                  access_token_key="",
	                  access_token_secret="")

	status = api.PostUpdate('@' + friend + ' Hello, Nice to Meet You!')
	print(status.text)