"""Program to scrape the posts, comments and analyze them for keywords
"""


# Modules used in program
from nltk.corpus import stopwords 	
import nltk
from dotenv import load_dotenv
import praw
import os
import json


load_dotenv()

reddit = praw.Reddit(client_id=os.getenv('ID'), 
 					client_secret=os.getenv('SECRET'),
					user_agent=os.getenv('USER_AGENT'),
					username=os.getenv('NAME'),
					password=os.getenv('PASSWORD'))


stop_words = set(stopwords.words('english'))


# Function to scrape the post and comments and save them into the file
def fetch_subreddit_post_comments(topic, number_of_posts = 3, num_of_comments = 5):
	item = topic+ '.json'
	if os.path.isfile(item): 
		return parse_(item)
	else:	
		final_list = []		
		submission_post = []
		sub_reddit = reddit.subreddit(topic)
		for submission in sub_reddit.hot(limit = number_of_posts):
			word_dict = {}
			submission_post = submission.title
			word_dict['post'] = submission_post		
			comment_body = []
			for comment in submission.comments[:num_of_comments]:	
				if hasattr(comment, "body"):
					comment_body.append(comment.body)
			word_dict['comments'] = comment_body
			final_list.append(word_dict)

		with open(topic+".json", "w+") as f:
			json.dump(final_list, f, indent = 2)
		return final_list		


# Function to scrape the respective file (if present else scrape from reddit)
# and analyze the comments
def analyze_subreddit_post_comments(topic, number_of_posts= 3, num_of_comments= 5, limit_for_keywords_phrase = 20): # analyze comments
	item = topic+'.json'
	data = []
	if not os.path.isfile(item): 
		data =fetch_subreddit_post_comments(topic, number_of_posts, num_of_comments)
	else:
		data= parse_(item)		
	ws =[] # empty words list
	for post in data:
		for comment_ in post['comments']:
			for word in comment_.split():
				if word not in stop_words:
					ws.append(word)	
	x =  count_keywords(ws, limit_for_keywords_phrase)
	return x

	
# Count the number of times a phrase was repeated
def count_keywords(final_words_list, limit_for_keywords_phrase):
	ngrams = list(nltk.ngrams(final_words_list, n=2))
	ngrams_count = {i : ngrams.count(i) for i in ngrams}

	return sort_keywords_count(ngrams_count, limit_for_keywords_phrase)


# Sort the keywords phrase in descending order
def sort_keywords_count(keyword_count, limit_for_keywords_phrase):		
	keywords_dict = {}					
	final_list = []
	sort_orders = sorted(keyword_count.items(), key=lambda x: x[1], reverse=True)

	for i in sort_orders[:limit_for_keywords_phrase]:
		keywords_dict['words'] = i[0]
		keywords_dict['count'] = i[1]
		final_list.append(keywords_dict)
		keywords_dict = {}
	return final_list	


# Parse the file for subreddit
def parse_(top):
	with open(top, 'r') as f:
		data = json.load(f)
	return data