from flask import Flask, render_template
import requests


app = Flask(__name__)

url_blog = "https://api.npoint.io/a829f08f6029a464d006"
response = requests.get(url=url_blog)
all_posts = response.json()


@app.route("/")
def get_all_posts():
   return render_template("index.html", posts=all_posts)


@app.route("/post/<int:num>")
def get_post(num):
   return render_template("post.html", posts=all_posts[num-1])


@app.route("/about")
def get_about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
