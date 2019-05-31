import praw
import random
import time
from imgurpython import ImgurClient

def sleep_show(seconds):
	for i in reversed(range(seconds)):
		if i < 60:
			print("\rSleeping for %ds     " % i, end='', flush=True)
		elif i % 60 == 0:
			print("\rSleeping for %dm     " % (i / 60), end='', flush=True)
		else:
			print("\rSleeping for %dm %ds  " % (i / 60, i % 60), end='', flush=True)
		time.sleep(1)

words = [
	'mods', 'gay', '420', 'ah',
	'skrr', 'gang gang', 'flex',
	'xd', 'yass', 'Rise up!',
	'HhhMmMmmMmMm', 'dogs',
	'war', 'eDgY', 'sExY',
	'Reddit', 'normie', 'vaccines'
]

reddit_id = 'ECcClErdeUPmDA'
reddit_secret = 'XlOGp9tg5fZRy3lVooTuEVWi45A'

imgur_id = '89799fddb880372'
imgur_secret = 'b552691c08a926d2f1223538d7d0c793e8f41f8d'

reddit = praw.Reddit(client_id=reddit_id, client_secret=reddit_secret, password='johannes88', user_agent='testusr', username='Zedyx')
imgur = ImgurClient(imgur_id, imgur_secret)


while True:
	try:
		file = 'images_2019-05-19/dankmemes/' + str(random.randint(0, 1000)) + '.jpg'
		
		link = imgur.upload_from_path(file)
		print('Uploaded image', file, 'to', link['link'])
		
		submission = reddit.subreddit('dankmemes').submit(random.choice(words) + ' ' + random.choice(words) + ' ' + random.choice(words), url=link['link'])
		print('Submitted to reddit: https://www.reddit.com/' + str(submission))
		
		print('Sleeping 15m...')
		sleep_show(900)
	except:
		print("Exception! Sleeping 15m...")
		sleep_show(900)
		pass