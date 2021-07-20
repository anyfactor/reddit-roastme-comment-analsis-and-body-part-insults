from reddit_data import RedditPrawCLS
from json import load

def get_cred_fn():
  with open("SECRET", mode='r', encoding='utf-8') as file:
    cred = load(file)
  print(cred)

def main():
  cred = get_cred_fn()
  reddit_praw = RedditPrawCLS(cred)

if __name__ == "__main__":
  main()
