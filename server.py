from flask import Flask
app = Flask(__name__)
from flask import request, url_for
from werkzeug.contrib.atom import AtomFeed
from datetime import datetime


@app.route("/")
def hello():
    return "Hello World!"

class FeedItem:

    def __init__(self, title, body):
        self.title = title
        self.body = body

entries = []

@app.route('/atom')
def recent_feed():
    feed = AtomFeed(
        'Luk Posting',
         feed_url=request.url,
         url=request.url_root,
         author=request.url_root
     )
    for entry in entries:
        feed.add(
            entry.title,
            entry.body,
            content_type='html',
            url = 'http://google.pl',
            # url=urljoin(request.url_root, url_for("entries.detail", slug=entry.slug) ),
            updated=datetime.now(),
            published=datetime.now()
        )
    return feed.get_response()

@app.route("/add")
def add():
    title = 'title'+str(len(entries))
    body = 'body' + str(len(entries))
    entries.append(FeedItem(title, body))
    return 'Added, current entries size = '+str(len(entries))
