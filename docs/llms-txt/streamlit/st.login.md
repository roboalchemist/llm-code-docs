# st.login

Initiate the login flow for the given provider.

This command redirects the user to an OpenID Connect (OIDC) provider. After the user authenticates their identity, they are redirected back to the home page of your app. Streamlit stores a cookie with the user's identity information in the user's browser. You can access the identity information through [st.user](https://docs.streamlit.io/develop/api-reference/user/st.user). Call [st.logout()](https://docs.streamlit.io/develop/api-reference/user/st.logout) to remove the cookie and start a new session.

You can use any OIDC provider, including Google, Microsoft, Okta, and more. You must configure the provider through secrets management. Although OIDC is an extension of OAuth 2.0, you can't use generic OAuth providers. Streamlit parses the user's identity token and surfaces its attributes in [st.user](https://docs.streamlit.io/develop/api-reference/user/st.user). If the provider returns an access token, that token is ignored. Therefore, this command will not allow your app to act on behalf of a user in a secure system.

For all providers, there are two shared settings, `redirect_uri` and `cookie_secret`, which you must specify in an `[auth]` dictionary in `secrets.toml`. Other settings must be defined as described in the `provider` parameter.

- `redirect_uri` is your app's absolute URL with the pathname `oauth2callback`. For local development using the default port, this is `http://localhost:8501/oauth2callback`.
- `cookie_secret` should be a strong, randomly generated secret.

In addition to the shared settings, the following settings are required:

- `client_id`
- `client_secret`
- `server_metadata_url`

For a complete list of OIDC parameters, see [OpenID Connect Core](https://openid.net/specs/openid-connect-core-1_0.html#AuthRequest) and your provider's documentation. By default, Streamlit sets `scope="openid profile email"` and `prompt="select_account"`. You can change these and other OIDC parameters by passing a dictionary of settings to `client_kwargs`. `state` and `nonce`, which are used for security, are handled automatically and don't need to be specified. For more information, see Example 4.

## Examples

### Example 1: Use an unnamed default identity provider

If you do not specify a name for your provider, specify all settings within the `[auth]` dictionary of your `secrets.toml` file. The following example configures Google as the default provider. For information about using OIDC with Google, see [Google Identity](https://developers.google.com/identity/openid-connect/openid-connect).

```toml
[auth]
redirect_uri = "http://localhost:8501/oauth2callback"
cookie_secret = "xxx"
client_id = "xxx"
client_secret = "xxx"
server_metadata_url = "https://accounts.google.com/.well-known/openid-configuration"  # fmt: skip
```

Your app code:

```python
import streamlit as st

if not st.user.is_logged_in:
    if st.button("Log in"):
        st.login()
else:
    if st.button("Log out"):
        st.logout()
    st.write(f"Hello, {st.user.name}!")
```

### Example 2: Use a named identity provider

If you specify a name for your provider, save the shared settings in the `[auth]` dictionary of your `secrets.toml` file, and save the other settings in an `[auth.{provider}]` dictionary, where `{provider}` is the name of your provider. The following example configures Microsoft as the provider. The example uses `provider="microsoft"`, but you can use any name. This name is internal to Streamlit and is used to match the login command to its configuration. For information about using OIDC with Microsoft, see [Microsoft Entra ID](https://learn.microsoft.com/en-us/power-pages/security/authentication/openid-settings). To configure your `{tenant}` value in `server_metadata_url`, see [Microsoft identity platform](https://learn.microsoft.com/en-us/entra/identity-platform/v2-protocols-oidc#find-your-apps-openid-configuration-document-uri).

```toml
[auth]
redirect_uri = "http://localhost:8501/oauth2callback"
cookie_secret = "xxx"

[auth.microsoft]
client_id = "xxx"
client_secret = "xxx"
server_metadata_url = "https://login.microsoftonline.com/{tenant}/v2.0/.well-known/openid-configuration"
```

Your app code:

```python
import streamlit as st

if not st.user.is_logged_in:
    st.login("microsoft")
else:
    st.write(f"Hello, {st.user.name}!")
```

### Example 3: Use multiple, named providers

If you want to give your users a choice of authentication methods, configure multiple providers and give them each a unique name. The following example lets users choose between Okta and Microsoft to log in. Always check with your identity provider to understand the structure of their identity tokens because the returned fields may differ. Remember to set `{tenant}` and `{subdomain}` in `server_metadata_url` for Microsoft and Okta, respectively.

```toml
[auth]
redirect_uri = "http://localhost:8501/oauth2callback"
cookie_secret = "xxx"

[auth.microsoft]
client_id = "xxx"
client_secret = "xxx"
server_metadata_url = "https://login.microsoftonline.com/{tenant}/v2.0/.well-known/openid-configuration"

[auth.okta]
client_id = "xxx"
client_secret = "xxx"
server_metadata_url = "https://{subdomain}.okta.com/.well-known/openid-configuration"  # fmt: skip
```

Your app code:

```python
import streamlit as st

if not st.user.is_logged_in:
    st.header("Log in:")
    if st.button("Microsoft"):
        st.login("microsoft")
    if st.button("Okta"):
        st.login("okta")
else:
    if st.button("Log out"):
        st.logout()
    st.write(f"Hello, {st.user.name}!")
```

### Example 4: Change the default connection settings

`prompt="select_account"` may be treated differently by some providers when a user is already logged into their account. If a user is logged into their Google or Microsoft account from a previous session, the provider will prompt them to select the account they want to use, even if it's the only one. However, if the user is logged into their Okta or Auth0 account from a previous session, the account will automatically be selected. `st.logout()` does not clear a user's related cookies. To force users to log in every time, use `prompt="login"` as described in Auth0's [Customize Signup and Login Prompts](https://auth0.com/docs/customize/login-pages/universal-login/customize-signup-and-login-prompts).

```toml
[auth]
redirect_uri = "http://localhost:8501/oauth2callback"
cookie_secret = "xxx"

[auth.auth0]
client_id = "xxx"
client_secret = "xxx"
server_metadata_url = "https://{account}.{region}.auth0.com/.well-known/openid-configuration"  # fmt: skip
client_kwargs = { "prompt" = "login" }
```

Your app code:

```python
import streamlit as st

if st.button("Log in"):
    st.login("auth0")
if st.user.is_logged_in:
    if st.button("Log out"):
        st.logout()
    st.write(f"Hello, {st.user.name}!")
```