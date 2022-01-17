from flask import Flask, render_template, request
from functions import open_json, count_comments, get_comments_by_pk, replace_hashtags_with_links, search_post_by_username, search_post_by_key
app=Flask("__name__")

@app.route("/")
def main_page():
    posts=count_comments("data/comments.json")
    return render_template("index.html", posts=posts, number_coms=count_comments("data/comments.json"))
@app.route("/post/<pk>")
def post_page(pk):
    post=open_json("data/data.json")
    comments_count = len(get_comments_by_pk(pk))
    post_comments=get_comments_by_pk(pk)
    post[int(pk)-1]["content"]=replace_hashtags_with_links(post[int(pk)-1]["content"])
    return render_template("post.html", post=post[int(pk)-1], post_comments=post_comments, comments_count=comments_count)

@app.route("/user/<username>")
def user_page(username):
    user_posts=search_post_by_username(username)
    return render_template("user-feed.html", user_posts=user_posts)

@app.route("/search")
def search_page():
    key=request.args.get("s")
    posts=search_post_by_key(key)
    posts_len=len(posts)
    return render_template("search.html", posts=posts, posts_len=posts_len)

if __name__=="__main__":
    app.run()