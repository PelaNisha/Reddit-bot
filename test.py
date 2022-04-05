from RedditBot import *
subreddit_title = input("Enter the topic")
scraped_data = analyze_subreddit_post_comments(subreddit_title)
print(scraped_data)