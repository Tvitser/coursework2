import json
from pprint import pprint

def open_json(file_name):
    with open(file_name, encoding="utf-8") as file:
        return json.load(file)


def count_comments(filename):
    posts = open_json("data/data.json")
    coms = open_json(filename)
    comments_count={}
    for comment in coms:
        post_id=comment["post_id"]
        if post_id in comments_count:
            comments_count[post_id]+=1
        else:
            comments_count[post_id]=1
    for index, post in enumerate(posts):
        pk=post["pk"]
        if pk in comments_count:
            posts[index]["comments_count"]=comments_count[pk]
        else:
            posts[index]["comments_count"]=0
    return posts

    return number_coms

def get_comments_by_pk(pk):
    comments=open_json("data/comments.json")
    post_comments=[]
    for comment in comments:
        if comment["post_id"]==int(pk):
            post_comments.append(comment)
    return post_comments

def replace_hashtags_with_links(content):
    words=content.split(" ")
    for index, word in enumerate(words):
        if word.startswith("#"):
            tag=word[1:]
            words[index]=f"<a href='/tags/{tag}'>{word}</a>"
    return " ".join(words)

def search_post_by_username(username):
    posts=count_comments("data/comments.json")
    user_posts=[]
    for post in posts:
        if username in post["poster_name"]:
            user_posts.append(post)
    return user_posts

def search_post_by_key(key):
    posts = count_comments("data/comments.json")
    key_posts=[]
    for post in posts:
        if key in post["content"]:
            key_posts.append(post)
    return key_posts
