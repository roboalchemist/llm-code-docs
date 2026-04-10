# Source: https://dev.writer.com/framework/authentication.md

# Authentication

The Writer Framework authentication module allows you to restrict access to your application. Framework will be able to authenticate a user through an identity provider such as Google, Microsoft, Facebook, Github, Auth0, etc.

<Warning>
  Authentication is done before accessing the application. It is not possible to
  trigger authentication for certain pages exclusively.
</Warning>

<Warning>
  Static assets from Writer Framework exposed through `/static` and `/extensions` endpoints are not protected behind Authentication.
</Warning>

## Use Basic Auth

Basic Auth is a simple authentication method that uses a username and password. Authentication configuration is done in the [server\_setup.py module](/framework/custom-server).

<Warning>
  Password authentication and Basic Auth are not sufficiently secure for critical applications. If HTTPS encryption fails, a user could potentially intercept passwords in plaintext. Additionally, these methods are vulnerable to brute force attacks that attempt to crack passwords. To enhance security, it is advisable to implement authentication through trusted identity providers such as Google, Microsoft, Facebook, GitHub, or Auth0.
</Warning>

```python server_setup.py theme={null}
import os
import writer.serve
import writer.auth

auth = writer.auth.BasicAuth(
    login=os.getenv('LOGIN'),
    password=os.getenv('PASSWORD'),
)

writer.serve.register_auth(auth)
```

### Brute force protection

A simple brute force protection is implemented by default. If a user fails to log in, the IP of this user is blocked.
Writer framework will ban the IP from either the `X-Forwarded-For` header or the `X-Real-IP` header or the client IP address.

When a user fails to log in, they wait 1 second before they can try again. This time can be modified by
modifying the value of `delay_after_failure`.

<img src="https://mintcdn.com/writer/eBiCs3I5_-mSTcT-/framework/images/429.png?fit=max&auto=format&n=eBiCs3I5_-mSTcT-&q=85&s=2a0e055b6df575a4c9f4ba392111461a" alt="429" data-og-width="848" width="848" data-og-height="634" height="634" data-path="framework/images/429.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/eBiCs3I5_-mSTcT-/framework/images/429.png?w=280&fit=max&auto=format&n=eBiCs3I5_-mSTcT-&q=85&s=a94da887bbb03a647b076b399582409f 280w, https://mintcdn.com/writer/eBiCs3I5_-mSTcT-/framework/images/429.png?w=560&fit=max&auto=format&n=eBiCs3I5_-mSTcT-&q=85&s=3a8896dcc47ee735ba6ea1440b9843f5 560w, https://mintcdn.com/writer/eBiCs3I5_-mSTcT-/framework/images/429.png?w=840&fit=max&auto=format&n=eBiCs3I5_-mSTcT-&q=85&s=0f5e1f381ea2b0df1c4666b1de8cb453 840w, https://mintcdn.com/writer/eBiCs3I5_-mSTcT-/framework/images/429.png?w=1100&fit=max&auto=format&n=eBiCs3I5_-mSTcT-&q=85&s=3da1ed2f7ce600a478c8ab7ee7ad8ad6 1100w, https://mintcdn.com/writer/eBiCs3I5_-mSTcT-/framework/images/429.png?w=1650&fit=max&auto=format&n=eBiCs3I5_-mSTcT-&q=85&s=904b4bca2dccf4b9aecc2f5150bba521 1650w, https://mintcdn.com/writer/eBiCs3I5_-mSTcT-/framework/images/429.png?w=2500&fit=max&auto=format&n=eBiCs3I5_-mSTcT-&q=85&s=410b36ef8a1b4af7de1d4f4aa95c4e32 2500w" />

## Use OIDC provider

Authentication configuration is done in the `server_setup.py` [module](/framework/custom-server). The configuration depends on your identity provider.
Here is an example configuration for Google.

<img src="https://mintcdn.com/writer/eBiCs3I5_-mSTcT-/framework/images/auth.png?fit=max&auto=format&n=eBiCs3I5_-mSTcT-&q=85&s=4686c4fa72431516b12cd6ca16b035b1" alt="Authentication OIDC Principle" data-og-width="3006" width="3006" data-og-height="831" height="831" data-path="framework/images/auth.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/eBiCs3I5_-mSTcT-/framework/images/auth.png?w=280&fit=max&auto=format&n=eBiCs3I5_-mSTcT-&q=85&s=676a69e812216a7576c27068acc72088 280w, https://mintcdn.com/writer/eBiCs3I5_-mSTcT-/framework/images/auth.png?w=560&fit=max&auto=format&n=eBiCs3I5_-mSTcT-&q=85&s=71f4ca197e56f10f2ff1cb17a4b1c5a2 560w, https://mintcdn.com/writer/eBiCs3I5_-mSTcT-/framework/images/auth.png?w=840&fit=max&auto=format&n=eBiCs3I5_-mSTcT-&q=85&s=fa485ce81406b77a65f06e93b14e922a 840w, https://mintcdn.com/writer/eBiCs3I5_-mSTcT-/framework/images/auth.png?w=1100&fit=max&auto=format&n=eBiCs3I5_-mSTcT-&q=85&s=81aa8809ba7b365bcca880e437c93cf6 1100w, https://mintcdn.com/writer/eBiCs3I5_-mSTcT-/framework/images/auth.png?w=1650&fit=max&auto=format&n=eBiCs3I5_-mSTcT-&q=85&s=424c2166a8dc4b7a614480d4b798b3f8 1650w, https://mintcdn.com/writer/eBiCs3I5_-mSTcT-/framework/images/auth.png?w=2500&fit=max&auto=format&n=eBiCs3I5_-mSTcT-&q=85&s=e871fee2f8a4f588ca23b278646dfdbd 2500w" />

```python server_setup.py theme={null}
import os
import writer.serve
import writer.auth

oidc = writer.auth.Oidc(
    client_id="1xxxxxxxxx-qxxxxxxxxxxxxxxx.apps.googleusercontent.com",
    client_secret="GOxxxx-xxxxxxxxxxxxxxxxxxxxx",
    host_url=os.getenv('HOST_URL', "http://localhost:5000"),
    url_authorize="https://accounts.google.com/o/oauth2/auth",
    url_oauthtoken="https://oauth2.googleapis.com/token",
    url_userinfo='https://www.googleapis.com/oauth2/v1/userinfo?alt=json'
)

writer.serve.register_auth(oidc)
```

### Use pre-configured OIDC

The Writer Framework provides pre-configured OIDC providers. You can use them directly in your application.

| Provider | Function             | Description                                                                             |
| -------- | -------------------- | --------------------------------------------------------------------------------------- |
| Google   | `writer.auth.Google` | Allow your users to login with their Google Account                                     |
| Github   | `writer.auth.Github` | Allow your users to login with their Github Account                                     |
| Auth0    | `writer.auth.Auth0`  | Allow your users to login with different providers or with login password through Auth0 |

#### Google

You have to register your application into [Google Cloud Console](https://console.cloud.google.com/).

```python server_setup.py theme={null}
import os
import writer.serve
import writer.auth

oidc = writer.auth.Google(
	client_id="1xxxxxxxxx-qxxxxxxxxxxxxxxx.apps.googleusercontent.com",
	client_secret="GOxxxx-xxxxxxxxxxxxxxxxxxxxx",
	host_url=os.getenv('HOST_URL', "http://localhost:5000")
)

writer.serve.register_auth(oidc)
```

#### Github

You have to register your application into [Github](https://docs.github.com/en/apps/creating-github-apps/registering-a-github-app/registering-a-github-app#registering-a-github-app)

```python server_setup.py theme={null}
import os
import writer.serve
import writer.auth

oidc = writer.auth.Github(
	client_id="xxxxxxx",
	client_secret="xxxxxxxxxxxxx",
	host_url=os.getenv('HOST_URL', "http://localhost:5000")
)

writer.serve.register_auth(oidc)
```

#### Auth0

You have to register your application into [Auth0](https://auth0.com/).

```python server_setup.py theme={null}
import os
import writer.serve
import writer.auth

oidc = writer.auth.Auth0(
	client_id="xxxxxxx",
	client_secret="xxxxxxxxxxxxx",
	domain="xxx-xxxxx.eu.auth0.com",
	host_url=os.getenv('HOST_URL', "http://localhost:5000")
)

writer.serve.register_auth(oidc)
```

### Authentication workflow

<img src="https://mintcdn.com/writer/eBiCs3I5_-mSTcT-/framework/images/authentication_oidc.png?fit=max&auto=format&n=eBiCs3I5_-mSTcT-&q=85&s=44a0e689e6a53f0c45339a1e300e64f6" data-og-width="1743" width="1743" data-og-height="1920" height="1920" data-path="framework/images/authentication_oidc.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/eBiCs3I5_-mSTcT-/framework/images/authentication_oidc.png?w=280&fit=max&auto=format&n=eBiCs3I5_-mSTcT-&q=85&s=f8b390f434e832ab2de95439db6779c4 280w, https://mintcdn.com/writer/eBiCs3I5_-mSTcT-/framework/images/authentication_oidc.png?w=560&fit=max&auto=format&n=eBiCs3I5_-mSTcT-&q=85&s=661fc1c8cde6685e409833ae31fae220 560w, https://mintcdn.com/writer/eBiCs3I5_-mSTcT-/framework/images/authentication_oidc.png?w=840&fit=max&auto=format&n=eBiCs3I5_-mSTcT-&q=85&s=6b2ca8720ccd337f48aea87adc244d94 840w, https://mintcdn.com/writer/eBiCs3I5_-mSTcT-/framework/images/authentication_oidc.png?w=1100&fit=max&auto=format&n=eBiCs3I5_-mSTcT-&q=85&s=7e2091c03f07762b840059a7dfcda93c 1100w, https://mintcdn.com/writer/eBiCs3I5_-mSTcT-/framework/images/authentication_oidc.png?w=1650&fit=max&auto=format&n=eBiCs3I5_-mSTcT-&q=85&s=f121c3c7507b2dec7cce9a5a6bc71936 1650w, https://mintcdn.com/writer/eBiCs3I5_-mSTcT-/framework/images/authentication_oidc.png?w=2500&fit=max&auto=format&n=eBiCs3I5_-mSTcT-&q=85&s=d081225cee272555aae4cc4a91434c09 2500w" />

### App static assets

Static assets in your application are inaccessible. You can use the `app_static_public` parameter to allow their usage.
When `app_static_public` is set to `True`, the static assets in your application are accessible without authentication.

```python  theme={null}
oidc = writer.auth.Auth0(
	client_id="xxxxxxx",
	client_secret="xxxxxxxxxxxxx",
	domain="xxx-xxxxx.eu.auth0.com",
	host_url=os.getenv('HOST_URL', "http://localhost:5000"),
	app_static_public=True
)
```

## User information in event handler

When the `user_info` route is configured, user information will be accessible
in the event handler through the `session` argument.

```python  theme={null}
def on_page_load(state, session):
    email = session['userinfo'].get('email', None)
    state['email'] = email
```

## Unauthorize access

It is possible to reject a user who, for example, does not have the correct email address.

<Tip>
  You can also use userinfo inside app. You can restrict access to certain pages
  inside the application by using the `session` object. See [User information in
  event handler](#user-information-in-event-handler)
</Tip>

```python  theme={null}
from fastapi import Request

import writer.serve
import writer.auth

oidc = ...

def callback(request: Request, session_id: str, userinfo: dict):
    if userinfo['email'] not in ['nom.prenom123@example.com']:
        raise writer.auth.Unauthorized(more_info="You can contact the administrator at <a href='https://support.example.com'>support.example.com</a>")

writer.serve.register_auth(oidc, callback=callback)
```

The default authentication error page look like this:

<img src="https://mintcdn.com/writer/eBiCs3I5_-mSTcT-/framework/images/auth_unauthorized_default.png?fit=max&auto=format&n=eBiCs3I5_-mSTcT-&q=85&s=121f690212138f13acaa32b387c2e3ee" data-og-width="2649" width="2649" data-og-height="1383" height="1383" data-path="framework/images/auth_unauthorized_default.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/eBiCs3I5_-mSTcT-/framework/images/auth_unauthorized_default.png?w=280&fit=max&auto=format&n=eBiCs3I5_-mSTcT-&q=85&s=b2a608bc6fba8be77b39c03b87e468b7 280w, https://mintcdn.com/writer/eBiCs3I5_-mSTcT-/framework/images/auth_unauthorized_default.png?w=560&fit=max&auto=format&n=eBiCs3I5_-mSTcT-&q=85&s=a8597b336659bdf15f930fb56b66b2b0 560w, https://mintcdn.com/writer/eBiCs3I5_-mSTcT-/framework/images/auth_unauthorized_default.png?w=840&fit=max&auto=format&n=eBiCs3I5_-mSTcT-&q=85&s=455c1199ef94c89c371f761d53ddb35e 840w, https://mintcdn.com/writer/eBiCs3I5_-mSTcT-/framework/images/auth_unauthorized_default.png?w=1100&fit=max&auto=format&n=eBiCs3I5_-mSTcT-&q=85&s=0a9e202a52308aac6de28ad90f4b30d3 1100w, https://mintcdn.com/writer/eBiCs3I5_-mSTcT-/framework/images/auth_unauthorized_default.png?w=1650&fit=max&auto=format&n=eBiCs3I5_-mSTcT-&q=85&s=d53b1aacd21a9a394c9632c0eea77727 1650w, https://mintcdn.com/writer/eBiCs3I5_-mSTcT-/framework/images/auth_unauthorized_default.png?w=2500&fit=max&auto=format&n=eBiCs3I5_-mSTcT-&q=85&s=bb3dac7bd9c98872bb438f77e30142ee 2500w" />

| Parameter    | Description            |
| ------------ | ---------------------- |
| status\_code | HTTP status code       |
| message      | Error message          |
| more\_info   | Additional information |

## Modify user info

User info can be modified in the callback.

```python  theme={null}
from fastapi import Request

import writer.serve
import writer.auth

oidc = ...

def callback(request: Request, session_id: str, userinfo: dict):
	userinfo['group'] = []
	if userinfo['email'] in ['fabien@example.com']:
		userinfo['group'].append('admin')
		userinfo['group'].append('user')
	else:
		userinfo['group'].append('user')

writer.serve.register_auth(oidc, callback=callback)
```

## Custom unauthorized page

You can customize the access denial page using your own template.

```python  theme={null}
import os

from fastapi import Request, Response
from fastapi.templating import Jinja2Templates

import writer.serve
import writer.auth

oidc = ...

def unauthorized(request: Request, exc: writer.auth.Unauthorized) -> Response:
    templates = Jinja2Templates(directory=os.path.join(os.path.dirname(__file__), "templates"))
    return templates.TemplateResponse(request=request, name="unauthorized.html", status_code=exc.status_code, context={
        "status_code": exc.status_code,
        "message": exc.message,
        "more_info": exc.more_info
    })

writer.serve.register_auth(oidc, unauthorized_action=unauthorized)
```

## Enable in edit mode

Authentication is disabled in edit mode. To activate it, you must trigger the loading of the server\_setup module in edition mode.

```bash  theme={null}
writer edit --enable-server-setup
```
