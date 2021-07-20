import praw

class RedditPrawCLS:
  def __init__(self, cred):
      self.reddit = praw.Reddit(client_id=cred['client_id'],
                                client_secret=cred['client_secret'],
                                user_agent=cred['user_agent'])
      self.subreddit = "roastme"