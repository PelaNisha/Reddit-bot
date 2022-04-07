# What is a RedditBot?
A Reddit bot is a program that can monitor posts, comments, and other users' actions and autonomously respond to them.

#  Steps to use this repository
1. First of all create a reddit account for your bot.
2. Create an application.
3. You can create an application on [this webpage](https://ssl.reddit.com/prefs/apps/) by typing the name of your bot, selecting the option ‘script,’ providing some description, writing any random link in the box ‘redirect url,’ and clicking the button ‘create app.’ Then you will get ‘personal use script’ and ‘secret’. You will use them while writing a script for your Reddit bot.
4. Now you have the bot ID, SECRET_KEY, PASSWORD, USERAGENT and USERNAME, you can use them for your own bot.
5. Clone this repository into your computer after that.
6. Open the python file into your code editor.
7. Create a new file ".env" and fill the information like ID, SECRET_KEY, etc like in the .env.example file like:
```
ID=your_id
SECRET=your_secret_key
PASSWORD=the_password
USER_AGENT=app_name
NAME=reddit_username
```
8. Now you are all set to use the program.

# How to use the file
- Create any python file in the same directory.
- Import the RedditBot file like:- 
```
from RedditBot import fetch_subreddit_post_comments, analyze_subreddit_post_comments
```
- Use the functions from the RedditBot file, example is given below
```
from RedditBot import fetch_subreddit_post_comments, analyze_subreddit_post_comments
subreddit_title = input("Enter the topic")
posts_and_comments = fetch_subreddit_post_comments(subreddit_title)
print(posts_and_comments)
```
- You can also scrape urls or keywords exclusively by
```
print(posts_and_comments['urls'])
print(posts_and_comments['keywords'])
```

# Features
- You can fetch the posts and comments from  a subreddit and save it to a file.
```
posts_and_comments = fetch_subreddit_post_comments(subreddit_title)
```
- You can analyze the posts and comments from a subreddit to generate the most common phrases or keywords and also url list in the comments.
```
analyzed_posts_and_comments = analyze_subreddit_post_comments(subreddit_title)
```
- You can give the name of the subreddit, the number of posts, comments per post in the argument of fetch_subreddit_post_comments function and also limits for keyphrase to extract in the analyze_subreddit_post_comments function.

### for fetching of comments and post of certain number of posts:
```
fetch_subreddit_post_comments(topic, number_of_posts, num_of_comments)
```
### for analyzing comments of certain number of posts with limited keyphrase as output:
```
analyze_subreddit_post_comments(topic, number_of_posts, num_of_comments, limit_for_keywords_phrase)
```

# Dependencies
- a Code Editor preferably VScode
- python installed and running

## Also import the following modules by using pip or pip3 install... from the terminal	
- nltk
- dotenv 
- praw

example:
        `pip install nltk` (for python version<3)
        `pip3 install nltk` (for other python versions)