import praw
import re
import config as cfg

word_list = ["I\"m".lower(),"I'm".lower(),"Im".lower()] #Keep adding possiblities here

reddit = praw.Reddit(client_id = cfg.client_id, client_secret = cfg.client_secret, password = cfg.password, user_agent = cfg.user_agent, username = cfg.username)

subreddit = reddit.subreddit("funny")

for post in subreddit.hot(limit = 10): #Loop through the top 10 'Hot' Posts for a given subcategory
    post.comments.replace_more(limit = 0) #Flatteing comments
    for comment in post.comments.list():
        for word in word_list:
            for comment_word in comment.body.split():
                if word == comment_word:
                    try:
                        comment_body = comment.body
                        comment_body = comment_body.replace("\n","")
                        comment_body = comment_body + "."
                        dad_joke = re.search(f"({word}).*?[,.!?]" , comment_body)[0]
                        dad_joke = dad_joke.replace(word,"").strip()[:-1]
                        dad_joke = "Hi " + dad_joke + ", I'm DadBot!"
                        print(post.title)
                        print(dad_joke)
                        comment.reply(dad_joke)
                        break
                    except Exception as e :
                        print ("Exception occured {}".format(e))
                