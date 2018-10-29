import slackweb
from github_webhook import Webhook
from flask import Flask
import keys

URL = keys.url
app = Flask(__name__)  # Standard Flask app
webhook = Webhook(app) # Defines '/postreceive' endpoint
slack = slackweb.Slack(URL)
slack.notify(text="This is a test.")

@app.route("/")        # Standard Flask endpoint
def hello_world():
    return "Hello, World!"

@webhook.hook()        # Defines a handler for the 'push' event
def on_push(data):
    print("Got push with: {0}".format(data))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
