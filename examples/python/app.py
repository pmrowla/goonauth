from flask import Flask, redirect, url_for, session, request, jsonify
from flask_oauthlib.client import OAuth

import requests


app = Flask(__name__)
app.debug = True
app.secret_key = 'changeme1'
oauth = OAuth(app)

consumer_key = 'Vmc8aEJ=cYR5r6rf11--xiEA.!DJlLK997XY.uk7'     # Client ID
consumer_secret = 'mDfa3qAo1Hcvv8Y1s1Fn;r08YvZYMDPKhxbgRGv:h1d0SOiSOIPTE3ZBZZcjc=TvkVIFxEJ1:WKawBVi6jtC_WLBXp-rOciJ!_b?L5B7hVq7y1hsFNL9oi-hr?kRzrDg'
access_token_url = 'https://goonauth.cattes.us/o/token/'  
authorize_url = 'https://goonauth.cattes.us/o/authorize/'

goonauth = oauth.remote_app(
    'goonauth',
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    request_token_params={'scope': 'read'},
    base_url='https://goonauth.cattes.us/api/',
    request_token_url=None,
    access_token_method='POST',
    access_token_url=access_token_url,
    authorize_url=authorize_url
)


@app.route('/')
def index():
    if 'goonauth_token' in session:
        headers = {
            'Authorization': 'Bearer ' + session.get('goonauth_token')
        }
        profile = requests.get('https://goonauth.cattes.us/api/user/', headers=headers).text
        return profile

    return redirect(url_for('login'))


@app.route('/login')
def login():
    return goonauth.authorize(callback=url_for('authorized', _external=True))


@app.route('/login/authorized/')
@goonauth.authorized_handler
def authorized(resp):
    if resp is None:
        return 'Access denied: reason=%s error=%s' % (
            request.args['error_reason'],
            request.args['error_description']
        )
    
    session['goonauth_token'] = resp['access_token']
    return redirect('/')


@goonauth.tokengetter
def get_goonauth_oauth_token():
    return session.get('goonauth_token')


if __name__ == '__main__':
    #app.run(ssl_context='adhoc')
    app.run()
