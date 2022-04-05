# What is a RedditBot?
A Reddit bot is a program that can monitor posts, comments, and other users' actions and autonomously respond to them.

#  Steps to use this repository
1. First of all create a reddit account for your bot.
2. Create an application.
3. You can create an application on this webpage- https://ssl.reddit.com/prefs/apps/ by typing the name of your bot, selecting the option ‘script,’ providing some description, writing any random link in the box ‘redirect url,’ and clicking the button ‘create app.’ Then you will get ‘personal use script’ and ‘secret’. You will use them while writing a script for your Reddit bot.
4. Now you have the bot ID, SECRET_KEY, PASSWORD, USERAGENT and USERNAME, you can use them for your own bot.
5. Clone this repository into your computer after that.
6. Open the python file into your code editor.
7. Create a new file ".env" and fill the information like ID, SECRET_KEY, etc like in the .env.example file(make sure there is no space inbetween).
8. Now you are all set to use the program.

# How to use the file
- Create any python file in the same directory.
- import the RedditBot.py file like:- import RedditBot.
- Now you can use the functions from the RedditBot.py file.

# Features
- You can fetch the posts and comments from  a subreddit and save it to a file.
- You can analyze the posts and comments from a subreddit to generate the most common phrases or keywords.
- You can give the name of the subreddit, the number of posts, comments per post in the argument of fetch_subreddit_post_comments function and also limits for keyphrase to extract in the analyze_subreddit_post_comments function.

# Dependencies
- a CodeEditor like preferably VScode
- python installed and running