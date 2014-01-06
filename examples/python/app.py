from flask import Flask, redirect, url_for, session, request, jsonify
from flask_oauthlib.client import OAuth


app = Flask(__name__)
app.debug = True
app.secret_key = 'changeme'
oauth = OAuth(app)

consumer_key = 'WI?dIp8B2E=cKBR9Wqc!.M9Cejsz62up7=IkmcD2'     # Client ID
consumer_secret = '4?nQyyty91-SZ;udseamL4Q8TZq0qIgjhdPCqC!.hXaPV0PR?6=U7jWTMkys;RB8PVxXZrmc.gGaSk=@s2MfNImAbL=cnlXnEoE4Dy0CwQxhOMOUoM_8wWvTzhm_OW=f'  # Client Secret
access_token_url = 'https://localhost:8085/o/token/'  
authorize_url = 'https://localhost:8085/o/authorize/'

goonauth = oauth.remote_app(
    'goonauth',
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    request_token_params={'scope': 'write'},
    base_url='https://localhost:8085/api/',
    request_token_url=None,
    access_token_method='POST',
    access_token_url=access_token_url,
    authorize_url=authorize_url
)


@app.route('/')
def index():
    if 'goonauth_token' in session:
        return 'authd'

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
    
    session['goonauth_token'] = (resp['access_token'], '')


@goonauth.tokengetter
def get_goonauth_oauth_token():
    return session.get('goonauth_token')


if __name__ == '__main__':
    app.run(ssl_context='adhoc')
