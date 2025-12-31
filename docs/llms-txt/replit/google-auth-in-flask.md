# Source: https://docs.replit.com/additional-resources/google-auth-in-flask.md

# Google Authentication in Python and Flask

> Learn how to implement Google OAuth authentication in a Flask app on Replit, including user login and Google Sheets API integration.

Allowing your users to log in to your website using their Google account has these benefits:

1. You don't have to implement your own authentication scheme.
2. You can get users' name and contact information easily.
3. You can use the same credentials to access users' Google resources like Sheets and Drive.

This guide that will walk you through how to do that with Python and Flask on Replit.

First, we'll walk through how to setup basic OAuth authentication, then cover how to use the resulting credentials to access users' Google resources.

## Introduction to OAuth

Google authentication is based on the OAuth standard. The way OAuth works is as follows:

1. Somewhere on your website, you direct a user to a login page.
2. When they go to the login page, you don't implement the login form on your website, but instead redirect to Google's login service to login the user.
3. When Google's login service successfully logs in the user, it redirects back to your website at a predefined URL of your choosing, say `https://YOUR_DOMAIN/oauth2callback`, while sending some information pertinent to the user and the login session.
4. You use the user's login information to further obtain an access token, which is like a pass you can use to access the user's resources, like their profile information, their spreadsheets, documents and more.

## OAuth: Show me the code

If you are like me, the first thing you want is working code. The code below is what you need. However, you'll need to set up some things in your Google Cloud Console in order to get everything working. That will be covered in the next section. Create a new Replit App using the [Flask template](https://replit.com/@replit/Flask?v=1) and put the following in `main.py`. The comments in the code explains what the individual parts do:

```python  theme={null}
from flask import Flask, redirect, session, url_for, request
import google_auth_oauthlib.flow
import json
import os
import requests

app = Flask('app')
# `FLASK_SECRET_KEY` is used by sessions. You should create a random string
# and store it as secret.
app.secret_key = os.environ.get('FLASK_SECRET_KEY') or os.urandom(24)

# `GOOGLE_APIS_OAUTH_SECRET` contains the contents of a JSON file to be downloaded
# from the Google Cloud Credentials panel. See next section.
oauth_config = json.loads(os.environ['GOOGLE_OAUTH_SECRETS'])

# This sets up a configuration for the OAuth flow
oauth_flow = google_auth_oauthlib.flow.Flow.from_client_config(
    oauth_config,
    # scopes define what APIs you want to access on behave of the user once authenticated
    scopes=[
        "https://www.googleapis.com/auth/userinfo.email",
        "openid",
        "https://www.googleapis.com/auth/userinfo.profile",
    ]
)

# This is entrypoint of the login page. It will redirect to the Google login service located at the
# `authorization_url`. The `redirect_uri` is actually the URI which the Google login service will use to
# redirect back to this app.
@app.route('/signin')
def signin():
    # We rewrite the URL from http to https because inside the Replit App http is used,
    # but externally it's accessed via https, and the redirect_uri has to match that
    oauth_flow.redirect_uri = url_for('oauth2callback', _external=True).replace('http://', 'https://')
    authorization_url, state = oauth_flow.authorization_url()
    session['state'] = state
    return redirect(authorization_url)

# This is the endpoint that Google login service redirects back to. It must be added to the "Authorized redirect URIs"
# in the API credentials panel within Google Cloud. It will call a Google endpoint to request
# an access token and store it in the user session. After this, the access token can be used to access
# APIs on behalf of the user.
@app.route('/oauth2callback')
def oauth2callback():
    if not session['state'] == request.args['state']:
        return 'Invalid state parameter', 400
    oauth_flow.fetch_token(authorization_response=request.url.replace('http:', 'https:'))
    session['access_token'] = oauth_flow.credentials.token
    return redirect("/")

# This is the home page of the app. It directs the user to log in if they are not already.
# It shows the user info's information if they already are.
@app.route('/')
def welcome():
    if "access_token" in session:
        user_info = get_user_info(session["access_token"])
        if user_info:
            return f"""
                Hello {user_info["given_name"]}!<br>
                Your email address is {user_info["email"]}<br>
                <a href="/logout">Log out</a>
            """
    return """
        <h1>Hello!</h1>
        <a href="/signin">Sign In via Google</a><br>
    """

# Call the userinfo API to get the user's information with a valid access token.
# This is the first example of using the access token to access an API on the user's behalf.
def get_user_info(access_token):
    response = requests.get("https://www.googleapis.com/oauth2/v3/userinfo", headers={
       "Authorization": f"Bearer {access_token}"
   })
    if response.status_code == 200:
        user_info = response.json()
        return user_info
    else:
        print(f"Failed to fetch user info: {response.status_code} {response.text}")
        return None

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

```

## Set up your OAuth App / Client

To get the above code working, you'll need to do these things in Google Cloud.

1. Create a Google Cloud project (if you don't already have one).
2. Configure the OAuth consent screen.
3. Create an OAuth client ID for your app.

### Create a Google Cloud project

If you already have a Google Cloud project you want to use for this exercise, you can skip this step.

1. Go to the [Google Cloud Console](https://console.cloud.google.com/)
2. Click on the project selector dropbox next to the Google Cloud logo:

<Frame>
  <img src="https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/google-project-dropdown.png?fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=a30f634d9a23d770a6d2f4011d0d9dae" alt="Google Project Dropdown" data-og-width="734" width="734" data-og-height="94" height="94" data-path="images/google-auth-in-flask/google-project-dropdown.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/google-project-dropdown.png?w=280&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=141a1f032ba086019245ae3ca65fce24 280w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/google-project-dropdown.png?w=560&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=90ea5c0792a79667f802117242709e42 560w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/google-project-dropdown.png?w=840&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=3fb734cd615778dfc430fccadb31bc1d 840w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/google-project-dropdown.png?w=1100&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=f7d003515be1029d97a911b5bcbfc648 1100w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/google-project-dropdown.png?w=1650&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=21ce29392761513299e8eeabc5e5785b 1650w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/google-project-dropdown.png?w=2500&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=9c0d4b3ed5d102f882881672906752de 2500w" />
</Frame>

3. Select an existing project or Click "New Project" and create an new project.

<Frame>
  <img src="https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/select-project.png?fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=e74b58a12409487b6185d0c26768467c" alt="Select Project" data-og-width="1092" width="1092" data-og-height="868" height="868" data-path="images/google-auth-in-flask/select-project.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/select-project.png?w=280&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=ea9e7ccf9f4aa48e94b6035ae8d50537 280w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/select-project.png?w=560&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=f86cce6eb731127ea752174d1962d5c2 560w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/select-project.png?w=840&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=06215e79a407d12e4fc4fb37759cd2ab 840w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/select-project.png?w=1100&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=7b827ca4d88793a750488cb47b06bf41 1100w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/select-project.png?w=1650&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=edcf0cf5fabc7292446fa091dae68f5e 1650w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/select-project.png?w=2500&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=9988ec2dd85055671b3f1ee78adab6d3 2500w" />
</Frame>

4. If creating a new project, enter a project name, and click "Create".

<Frame>
  <img src="https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/new-project.png?fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=4435873966a96504d766496022464e75" alt="New Project" data-og-width="1110" width="1110" data-og-height="868" height="868" data-path="images/google-auth-in-flask/new-project.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/new-project.png?w=280&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=9c6c714a3498b817eb37a6cba4625312 280w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/new-project.png?w=560&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=37eb8e9915f8f24668ddc08dfdccb40f 560w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/new-project.png?w=840&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=775e0c84b752cec41cf1d4c166970f0a 840w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/new-project.png?w=1100&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=c3b0a59ea68dab3d33fdad0858859853 1100w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/new-project.png?w=1650&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=3401b57fa3f74bd7572f5d592ba81805 1650w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/new-project.png?w=2500&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=e1f5646d3de6dbe66029ef803e8da52c 2500w" />
</Frame>

If you see your new project show up in a popup, click "Select project" to make that the *active project*.

### Configure the OAuth consent screen

Now that you have a project, you can configure the OAuth consent screen for it:

1. Go to the [OAuth Consent Screen](https://console.cloud.google.com/apis/credentials/consent)

<Frame>
  <img src="https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/oauth-consent-screen.png?fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=49c9930fd4dcec9194a31221fb0dcdfa" alt="OAuth Consent Screen" data-og-width="1196" width="1196" data-og-height="675" height="675" data-path="images/google-auth-in-flask/oauth-consent-screen.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/oauth-consent-screen.png?w=280&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=ca6a8ce4087d3da0847e12b77d66b323 280w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/oauth-consent-screen.png?w=560&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=bbeab4b70dce9fa3cadf6c3c80e6aaab 560w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/oauth-consent-screen.png?w=840&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=7165a337bc679b0eb14d97f6cd3a56de 840w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/oauth-consent-screen.png?w=1100&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=52a29b8e1156085225593e86c5199ea5 1100w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/oauth-consent-screen.png?w=1650&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=8fd0b51c7547424ffde9319db7ee37da 1650w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/oauth-consent-screen.png?w=2500&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=f0ad1808d977028219ae2d8c2c0073dd 2500w" />
</Frame>

2. Make sure the project in the project drop down is the one you want.
3. Select "External" to allow any user to log in to your app with a Google account. "Internal" will allow only people from your organization.
4. Click "Create".
5. Enter an app name and the email of the person supporting this app (you?)

<Frame>
  <img src="https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/oauth-consent-step-2.png?fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=613070383292b3a679e1f9653036f660" alt="OAuth Consent Screen" data-og-width="1196" width="1196" data-og-height="675" height="675" data-path="images/google-auth-in-flask/oauth-consent-step-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/oauth-consent-step-2.png?w=280&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=53a59078b8d0f831530ab44766c63b83 280w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/oauth-consent-step-2.png?w=560&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=565e56853434c9123ac09f6ce777570e 560w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/oauth-consent-step-2.png?w=840&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=eef34eda90e3e6132c38d70f2d12b09f 840w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/oauth-consent-step-2.png?w=1100&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=63b19416b2b1baa9750711746a88414f 1100w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/oauth-consent-step-2.png?w=1650&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=12025e4c9fd24b826339fee7ba2d1333 1650w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/oauth-consent-step-2.png?w=2500&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=35230cd5e862820986ea9fbfc1d5639e 2500w" />
</Frame>

6. Enter an email address under "Developer contact information".

<Frame>
  <img src="https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/oauth-consent-step-2-b.png?fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=82001a9c28a09f1ba232f2c6b80b3118" alt="Developer contact information" data-og-width="533" width="533" data-og-height="207" height="207" data-path="images/google-auth-in-flask/oauth-consent-step-2-b.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/oauth-consent-step-2-b.png?w=280&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=986d6522b3e862325838cd85de91ad98 280w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/oauth-consent-step-2-b.png?w=560&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=e3fcc67a205ae288cd9fd2f637ade5e2 560w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/oauth-consent-step-2-b.png?w=840&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=ddba135fab9723f7ec77b2c054c7f9f5 840w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/oauth-consent-step-2-b.png?w=1100&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=29d2aa5ba9e1dac2b7634af6ac3544c7 1100w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/oauth-consent-step-2-b.png?w=1650&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=bef601c12bafa329335509f536ebbd74 1650w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/oauth-consent-step-2-b.png?w=2500&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=f7d5a7b428bbec1dd57ac379fc88186a 2500w" />
</Frame>

7. Click "Save and continue".
8. In the Scopes screen, you can add the APIs you want your app to have access to. You already have access to the APIs for getting basic user information.

<Frame>
  <img src="https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/oauth-scopes.png?fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=616e631af44331268912e1b054ed2d4d" alt="OAuth Scopes" data-og-width="1093" width="1093" data-og-height="647" height="647" data-path="images/google-auth-in-flask/oauth-scopes.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/oauth-scopes.png?w=280&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=8242a26f18ab3dcc55b60ba94f841860 280w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/oauth-scopes.png?w=560&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=215b33b37ebba4787eabe739f96a4c44 560w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/oauth-scopes.png?w=840&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=dc0bd5112b210b1e133752317d388803 840w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/oauth-scopes.png?w=1100&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=3cf860c8e4d7150357e7964cd83124e3 1100w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/oauth-scopes.png?w=1650&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=b56331cfe48d4afdc43e65ec76c49024 1650w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/oauth-scopes.png?w=2500&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=ca3ca674659d8f76c9a6a3e6f21f373f 2500w" />
</Frame>

For now, leave this as is and click "Save and continue".
9\. In Test Users, you need to add the email of the users you want to be able to test the app during its testing phase.

<Frame>
  <img src="https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/test-users.png?fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=2d3d6dd451cf47b3c5d49a6fe1362b2d" alt="Test Users" data-og-width="1050" width="1050" data-og-height="641" height="641" data-path="images/google-auth-in-flask/test-users.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/test-users.png?w=280&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=a2f177acc8e3a2bf806ab47ee209a6b9 280w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/test-users.png?w=560&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=a3d36ab7d53a98636169fc573ec0af4c 560w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/test-users.png?w=840&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=067289a63ce872e52ead31319e082844 840w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/test-users.png?w=1100&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=9e635f22753b4c21facfadefb7d43ebd 1100w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/test-users.png?w=1650&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=dc690bb163f9d951e46c54885adb6294 1650w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/test-users.png?w=2500&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=20ccf2d589a02673c4531fea7a32fe2a 2500w" />
</Frame>

Click "Add users"
10\. Add one or more email Google email addresses, and click "Add".

<Frame>
  <img src="https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/test-users-add.png?fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=d2b34047e7e9d45c5933f1abe3e29dcd" alt="Test Users" data-og-width="1050" width="1050" data-og-height="641" height="641" data-path="images/google-auth-in-flask/test-users-add.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/test-users-add.png?w=280&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=3789d50d5bad2d04781ed13825e225a8 280w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/test-users-add.png?w=560&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=421b7ef4ef582fb8ad68d5dc8d5ba112 560w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/test-users-add.png?w=840&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=cfbd8dac34f914ca14fa65e84f420cb6 840w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/test-users-add.png?w=1100&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=0587d027bfa9ad57f683d700f3be0924 1100w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/test-users-add.png?w=1650&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=758c18aba8d278204d9c2a4d4536440d 1650w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/test-users-add.png?w=2500&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=024d64661032930e790249810920086a 2500w" />
</Frame>

Then click "Save and continue".
11\. Review the summary screen. You can always go back and edit any of the steps.

<Frame>
  <img src="https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/summary.png?fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=37a3ea92af93f314a105d4eb35b4cd14" alt="Test Users" data-og-width="735" width="735" data-og-height="328" height="328" data-path="images/google-auth-in-flask/summary.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/summary.png?w=280&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=974587fb87caf19f9eb000633b9a8155 280w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/summary.png?w=560&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=546958b7ddcecab44ff9476252f9d442 560w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/summary.png?w=840&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=67ee80bfe02ffeb1b721ca3416b774d5 840w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/summary.png?w=1100&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=a2bfd0dade9848444245d6b5b96bf938 1100w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/summary.png?w=1650&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=f92e3fa8bb682790d8e25497619d3772 1650w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/summary.png?w=2500&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=01d0ab53ea2519e955537d7fbdcdaa11 2500w" />
</Frame>

### Create an OAuth client ID for your app

This is the last part. To get OAuth working, you need to create an OAuth client ID for the app.

1. Go to [Credentials](https://console.cloud.google.com/apis/credentials).

<Frame>
  <img src="https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/credentials.png?fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=456919dc3158da1e521882c6dbebec9d" alt="Test Users" data-og-width="1050" width="1050" data-og-height="605" height="605" data-path="images/google-auth-in-flask/credentials.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/credentials.png?w=280&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=b3a24bd68aae1836af63a70865dd1f57 280w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/credentials.png?w=560&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=500345833eac8e25f2a61ad558db6ab0 560w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/credentials.png?w=840&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=b9e752efe943d02f995cb5c4fafcae47 840w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/credentials.png?w=1100&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=525a312dfdff71e53ac76d2e31af0325 1100w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/credentials.png?w=1650&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=bace4f3c0fe355601ea9b37da7443d47 1650w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/credentials.png?w=2500&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=cb648ea7d78f7087151506f18514d734 2500w" />
</Frame>

2. Click "Create credentials"

<Frame>
  <img src="https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/create-credentials.png?fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=1d7d149734afd522a6b54787771b8614" alt="Test Users" data-og-width="1050" width="1050" data-og-height="605" height="605" data-path="images/google-auth-in-flask/create-credentials.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/create-credentials.png?w=280&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=7f26b13a7ee45a320e026b3ab2d12b55 280w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/create-credentials.png?w=560&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=c2c2a8c5e0ec9ddbcf97fb4104d4840c 560w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/create-credentials.png?w=840&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=0d502380429c8511fc828d1248bee991 840w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/create-credentials.png?w=1100&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=100ce49f5edd922a835c3d7eaa5c394c 1100w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/create-credentials.png?w=1650&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=792735da6488055fac4787d0c8c21c1d 1650w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/create-credentials.png?w=2500&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=4ccb819564f2731e1746e47e109ec25d 2500w" />
</Frame>

select "OAuth client ID".
3\.  Select "Web application" for Application type. Enter a name for this client ID.

<Frame>
  <img src="https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/create-credentials-web.png?fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=27d176683f267e10e559e91969936ec9" alt="Test Users" data-og-width="1050" width="1050" data-og-height="605" height="605" data-path="images/google-auth-in-flask/create-credentials-web.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/create-credentials-web.png?w=280&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=10eaadca05020ce6667cbe16105721a4 280w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/create-credentials-web.png?w=560&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=86ee0a7729ef88e027c510a1588133ae 560w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/create-credentials-web.png?w=840&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=5e31a6c19ffa2921c2515e5f48e9f38c 840w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/create-credentials-web.png?w=1100&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=ab82bcbab7f7923786ff85651b02ae6c 1100w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/create-credentials-web.png?w=1650&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=cd4be2e2c782619faddb32a05790899d 1650w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/create-credentials-web.png?w=2500&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=b7ad85318c548ea060a5d695a779bf13 2500w" />
</Frame>

4. Now, go to your Flask Replit App. Open the shell, and enter: `echo https://$REPLIT_DEV_DOMAIN/oauth2callback`. The result will look something like: `https://81309e9b-c4df-48e0-a2c2-0a8d3c0e3162-00-35ppsa0tcuv6v.infra-staging.replit.dev/oauth2callback`. Copy this text and enter it as one of the "Authorized redirect URIs" in the bottom of the form

<Frame>
  <img src="https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/authorized-redirect-uris.png?fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=0cbf4b9efec37c1d0d63241d1453eead" alt="Test Users" data-og-width="800" width="800" data-og-height="271" height="271" data-path="images/google-auth-in-flask/authorized-redirect-uris.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/authorized-redirect-uris.png?w=280&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=a7bc4c137f04d78a0d387464622d9675 280w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/authorized-redirect-uris.png?w=560&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=3eb2174cb168c64ad2c0195c2301cc37 560w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/authorized-redirect-uris.png?w=840&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=5635a8ad1c75dce2b1ecf1b742b022b8 840w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/authorized-redirect-uris.png?w=1100&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=e4d6e0e666a0c0809105cc693d02d0cf 1100w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/authorized-redirect-uris.png?w=1650&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=219d894478b594dd2dc7519be0b6bf3b 1650w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/authorized-redirect-uris.png?w=2500&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=e149c86f22d6273c25903f3398b041ac 2500w" />
</Frame>

Later when you publish your app, you'll want to come back here to add another entry `https://YOUR_APP_DOMAIN/oauth2callback`

5. Click "Create"
6. Click "Download JSON":

<Frame>
  <img src="https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/secrets_json.png?fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=b51a15e9157b0949d7fc6a1e69930acf" alt="Test Users" data-og-width="573" width="573" data-og-height="607" height="607" data-path="images/google-auth-in-flask/secrets_json.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/secrets_json.png?w=280&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=a258dadce0e255fd66375513a9f78b81 280w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/secrets_json.png?w=560&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=7b49820d2bbf6c3b6925462cbe1e728f 560w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/secrets_json.png?w=840&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=114e32f264a925694c1ca0a246f3679d 840w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/secrets_json.png?w=1100&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=7d1617754f2ce79dc5be0904be7b868c 1100w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/secrets_json.png?w=1650&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=09fdcc8ad7dce7e6271e82c9fe8cf032 1650w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/secrets_json.png?w=2500&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=99b3c81557cfd33824ff706509b42849 2500w" />
</Frame>

7. Go to your Replit App again, open the Secrets pane. Create a secret named `GOOGLE_OAUTH_SECRETS`, and paste of the contents of the downloaded file
   as the secret value.

<Frame>
  <img src="https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/add-secret.png?fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=bd181325e743c64e07eb0f84e7d9ee05" alt="Test Users" data-og-width="1060" width="1060" data-og-height="677" height="677" data-path="images/google-auth-in-flask/add-secret.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/add-secret.png?w=280&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=a8af7b52faea45416848fc1f4b715ad1 280w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/add-secret.png?w=560&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=c3b3d0ffd22830f93b8a669ae38e65cd 560w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/add-secret.png?w=840&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=62d2b11ef135d995cb0af23ba3f56a3c 840w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/add-secret.png?w=1100&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=233790e0f432aea6dbef4630a3073505 1100w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/add-secret.png?w=1650&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=6d2a6901b92f154fee5c6a74f0313077 1650w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/google-auth-in-flask/add-secret.png?w=2500&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=2692650a5589a255641eea4a5fe7150f 2500w" />
</Frame>

Phew! That was tedious. Congratulations if you made it through! Now you can run the Flask app and log in using a test user Google account. To make your app available to any Google user, you'll need to go back to the [consent page](https://console.cloud.google.com/apis/credentials/consent) and click "Publish App". A verification process may be required if your app requires additional Google APIs like Sheets and Drive.

Next, we'll cover how to integrate with a Google API like Sheets. Follow along if you want to go further.

## Google Sheets API Setup

In order to add a Google API integration like Google Sheets, first you need to enable the API for the app. You can [browser the available APIs](https://console.cloud.google.com/apis/library). As an example, we'll use Google Sheets.

1. Go to the [Google Sheets API listing page](https://console.cloud.google.com/apis/library/sheets.googleapis.com).
2. Click "Enable".

Done! That's all the Google Cloud setup you had to do for this part.

## Google Sheets Integration: Show me the code

First, in the oauth flow section of the original code, we leave everything the same, except add `"https://www.googleapis.com/auth/spreadsheets.readonly"` to the list of scopes:

```python  theme={null}
# This sets up a configuration for the OAuth flow
oauth_flow = google_auth_oauthlib.flow.Flow.from_client_config(
    oauth_config,
    # scopes define what APIs you want to access on behave of the user once authenticated
    scopes=[
        "https://www.googleapis.com/auth/userinfo.email",
        "openid",
        "https://www.googleapis.com/auth/userinfo.profile",
        "https://www.googleapis.com/auth/spreadsheets.readonly"
    ]
)
```

Now, the way you access a Google API with the `googleapiclient.discovery` library is to first create a `Credentials` object using the access token, and then use the `build` function to create a callable API object. For the sheets API it looks like:

```python  theme={null}
credentials = google.oauth2.credentials.Credentials(token=session['access_token'])
service = build("sheets", "v4", credentials=credentials)
sheets_api = service.spreadsheets()
```

As to how to actually use the Sheets API, I've created a couple of helper functions:

```python  theme={null}
# fetch all sheets within a Google spreadsheet
def get_sheets(sheets_api, spreadsheet_id) -> list[str]:
    result = sheets_api.get(spreadsheetId=spreadsheet_id).execute()
    return [sheet["properties"]["title"] for sheet in result["sheets"]]

# fetch the data for a given sheet within a Google spreadsheet
def get_sheet_data(sheets_api, spreadsheet_id, sheet_title) -> list[list[str]]:
    result = (
        sheets_api.values()
        .get(spreadsheetId=spreadsheet_id, range=sheet_title)
        .execute()
    )
    return result["values"]
```

With the above help, we can create a POST handler endpoint that imports a Google spreadsheet like so:

```python  theme={null}
@app.route("/import_spreadsheet", methods = ['POST'])
def import_spreadsheet():
    if 'access_token' not in session:
        return redirect('/signin')
    spreadsheet_id = request.form["spreadsheet_id"]
    credentials = google.oauth2.credentials.Credentials(token=session['access_token'])
    service = build("sheets", "v4", credentials=credentials)
    sheets_api = service.spreadsheets()
    try:
        sheets = get_sheets(sheets_api, spreadsheet_id)
        data_by_sheets = {}
        for sheet in sheets:
            data = get_sheet_data(sheets_api, spreadsheet_id, sheet)
            data_by_sheets[sheet] = data
    except googleapiclient.errors.HttpError as e:
        return f"upload failure"
    dirpath = os.path.join("static", "uploads", spreadsheet_id)
    filepath = os.path.join(dirpath, "data.json")
    os.makedirs(dirpath, exist_ok=True)
    with open(filepath, "w") as file:
        json.dump(data_by_sheets, file)
    return "upload success!"
```

Here is the full working code:

```python  theme={null}
from flask import Flask, redirect, session, url_for, request
import google_auth_oauthlib.flow
import json
import os
import requests
from googleapiclient.discovery import build
import googleapiclient.errors
import google.oauth2.credentials

app = Flask('app')
# `FLASK_SECRET_KEY` is used by sessions. You should create a random string
# and store it as secret.
app.secret_key = os.environ.get('FLASK_SECRET_KEY') or os.urandom(24)

# `GOOGLE_APIS_OAUTH_SECRET` contains the contents of a JSON file to be downloaded
# from the Google Cloud Credentials panel. See next section.
oauth_config = json.loads(os.environ['GOOGLE_OAUTH_SECRETS'])

# This sets up a configuration for the OAuth flow
oauth_flow = google_auth_oauthlib.flow.Flow.from_client_config(
    oauth_config,
    # scopes define what APIs you want to access on behave of the user once authenticated
    scopes=[
        "https://www.googleapis.com/auth/userinfo.email",
        "openid",
        "https://www.googleapis.com/auth/userinfo.profile",
        "https://www.googleapis.com/auth/spreadsheets.readonly"
    ]
)

# This is entrypoint of the login page. It will redirect to the Google login service located at the
# `authorization_url`. The `redirect_uri` is actually the URI which the Google login service will use to
# redirect back to this app.
@app.route('/signin')
def signin():
    # We rewrite the URL from http to https because inside the Replit App http is used,
    # but externally it's accessed via https, and the redirect_uri has to match that
    oauth_flow.redirect_uri = url_for('oauth2callback', _external=True).replace('http://', 'https://')
    authorization_url, state = oauth_flow.authorization_url()
    session['state'] = state
    return redirect(authorization_url)

# This is the endpoint that Google login service redirects back to. It must be added to the "Authorized redirect URIs"
# in the API credentials panel within Google Cloud. It will call a Google endpoint to request
# an access token and store it in the user session. After this, the access token can be used to access
# APIs on behalf of the user.
@app.route('/oauth2callback')
def oauth2callback():
    if not session['state'] == request.args['state']:
        return 'Invalid state parameter', 400
    oauth_flow.fetch_token(authorization_response=request.url.replace('http:', 'https:'))
    session['access_token'] = oauth_flow.credentials.token
    return redirect("/")

# Call the userinfo API to get the user's information with a valid access token.
# This is the first example of using the access token to access an API on the user's behalf.
def get_user_info(access_token):
    response = requests.get("https://www.googleapis.com/oauth2/v3/userinfo", headers={
       "Authorization": f"Bearer {access_token}"
   })
    if response.status_code == 200:
        user_info = response.json()
        return user_info
    else:
        print(f"Failed to fetch user info: {response.status_code} {response.text}")
        return None

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

# fetch all sheets within a Google spreadsheet
def get_sheets(sheets_api, spreadsheet_id) -> list[str]:
    result = sheets_api.get(spreadsheetId=spreadsheet_id).execute()
    return [sheet["properties"]["title"] for sheet in result["sheets"]]

# fetch the data for a given sheet within a Google spreadsheet
def get_sheet_data(sheets_api, spreadsheet_id, sheet_title) -> list[list[str]]:
    result = (
        sheets_api.values()
        .get(spreadsheetId=spreadsheet_id, range=sheet_title)
        .execute()
    )
    return result["values"]

# Render a form to allow importing a spreadsheet
@app.route("/import_spreadsheet_form")
def import_spreadsheet_form():
    return """
    <h3>Import Spreadsheet</h3>
    <form action="/import_spreadsheet" method="POST">
        <label>Spreadsheet ID</label>
        <input type="text" name="spreadsheet_id">

        <button type="submit">Import</button>
    </form>
    """

@app.route("/import_spreadsheet", methods = ['POST'])
def import_spreadsheet():
    if 'access_token' not in session:
        return redirect('/signin')
    spreadsheet_id = request.form["spreadsheet_id"]
    credentials = google.oauth2.credentials.Credentials(token=session['access_token'])
    service = build("sheets", "v4", credentials=credentials)
    sheets_api = service.spreadsheets()
    try:
        sheets = get_sheets(sheets_api, spreadsheet_id)
        data_by_sheets = {}
        for sheet in sheets:
            data = get_sheet_data(sheets_api, spreadsheet_id, sheet)
            data_by_sheets[sheet] = data
    except googleapiclient.errors.HttpError as e:
        return f"upload failure"
    dirpath = os.path.join("static", "uploads", spreadsheet_id)
    filepath = os.path.join(dirpath, "data.json")
    os.makedirs(dirpath, exist_ok=True)
    with open(filepath, "w") as file:
        json.dump(data_by_sheets, file)
    return "upload success! Really!"

@app.route('/')
def welcome():
    if "access_token" in session:
        user_info = get_user_info(session["access_token"])
        if user_info:
            return f"""
            Hello {user_info["given_name"]}!<br>
            Your email address is {user_info["email"]}<br>
            <a href="/signin">Sign In to Google</a><br>
            <a href="/import_spreadsheet_form">Import a Sheet</a>
            """
    return """
    <h1>Welcome to Google Sheet Importer</h1>
    <a href="/signin">Sign In to Google</a><br>
    <a href="/import_spreadsheet_form">Import a Sheet</a>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

Remember, if you publish the app. Make sure to:

1. Added the production `/oauth2callback` URI for to the "Authorized redirect URIs".
2. Go to the [consent page](https://console.cloud.google.com/apis/credentials/consent) and "Publish App".

Hope you had a good experience, and hope you Enjoy your further advantures.
