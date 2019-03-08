import os
import textwrap
from flask import Flask, abort, render_template, request, make_response
from jinja2 import TemplateNotFound
from imgurpython import ImgurClient
import config

app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'development key')

client_id = config.client_id
client_secret = config.client_secret

client = ImgurClient(client_id, client_secret)

items = client.get_album_images('nkOo18T')
pics = []
for item in items:
    pics.append([item.link,item.description])

# Jinja2 configuration
app.jinja_env.add_extension('jinja2.ext.do')
app.jinja_env.filters['dedent'] = lambda s: textwrap.dedent(s.lstrip('\n'))

@app.route('/')
def index():
    return render_template('index.html',pics=pics, )
