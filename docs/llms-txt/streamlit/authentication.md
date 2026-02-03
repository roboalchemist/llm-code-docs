# Source: https://docs.streamlit.io/develop/tutorials/authentication

# Source: https://docs.streamlit.io/develop/concepts/connections/authentication

# User authentication and information

Personalizing your app for your users is a great way to make your app more engaging.

User authentication and personalization unlocks a plethora of use cases for developers, including controls for admins, a personalized stock ticker, or a chatbot app with a saved history between sessions.

Before reading this guide, you should have a basic understanding of [secrets management](/develop/concepts/connections/secrets-management).

## OpenID Connect

Streamlit supports user authentication with OpenID Connect (OIDC), which is an authentication protocol built on top of OAuth 2.0. OIDC supports authentication, but not authorization: that is, OIDC connections tell you who a user is (authentication), but don't give you the authority to impersonate them (authorization). If you need to connect with a generic OAuth 2.0 provider or have your app to act on behalf of a user, consider using or creating a custom component.

Some popular OIDC providers are:

- [Google Identity](https://developers.google.com/identity/openid-connect/openid-connect)
- [Microsoft Entra ID](https://learn.microsoft.com/en-us/power-pages/security/authentication/openid-settings)
- [Okta](https://help.okta.com/en-us/content/topics/apps/apps_app_integration_wizard_oidc.htm)
- [Auth0](https://auth0.com/docs/get-started/auth0-overview/create-applications/regular-web-apps)

### Configure your OIDC connection in Streamlit

After you've configured your identity-provider client, you'll need to configure your Streamlit app, too. `st.login()` uses your app's `secrets.toml` file to configure your connection, similar to how `st.connection()` works.

Whether you have one OIDC provider or many, you'll need to declare a unique name for each. If you want to use Google Identity and Microsoft Entra ID as two providers for the same app, your configuration for local development will look like the following TOML file:

```toml
[auth]
redirect_uri = "http://localhost:8501/oauth2callback"
cookie_secret = "xxx"
client_id = "xxx"
client_secret = "xxx"
server_metadata_url = "https://{account}.{region}.auth0.com/.well-known/openid-configuration"
```

Microsoft's server metadata URL varies slightly depending on how your client is scoped. Replace `{tenant}` with the appropriate value described in Microsoft's documentation for [OpenID configuration](https://learn.microsoft.com/en-us/entra/identity-platform/v2-protocols-oidc#find-your-apps-openid-configuration-document-uri).

Your app code:

```python
import streamlit as st

if not st.user.is_logged_in:
    if st.button("Log in with Google"):
        st.login("google")
    st.stop()

if st.button("Log out"):
    st.logout()
st.markdown(f"Welcome! {st.user.name}")
```

Using callbacks, this would look like:

```python
import streamlit as st

if not st.user.is_logged_in:
    st.button("Log in with Google", on_click=st.login)
    st.stop()
st.button("Log out", on_click=st.logout)
st.markdown(f"Welcome! {st.user.name}")
```

## Passing keywords to your identity provider

To customize the behavior of your identity provider, you may need to declare additional keywords. For a complete list of OIDC parameters, see [OpenID Connect Core](https://openid.net/specs/openid-connect-core-1_0.html#AuthRequest) and your provider's documentation. By default, Streamlit sets `scope="openid profile email"` and `prompt="select_account"`. You can change these and other OIDC parameters by passing a dictionary of settings to `client_kwargs`. `state` and `nonce`, which are used for security, are handled automatically and don't need to be specified.

For example, if you are using Auth0 and need to force users to log in every time, use `prompt="login"` as described in Auth0's [Customize Signup and Login Prompts](https://auth0.com/docs/customize/login-pages/universal-login/customize-signup-and-login-prompts). Your configuration will look like this:

```toml
[auth]
redirect_uri = "http://localhost:8501/oauth2callback"
cookie_secret = "xxx"
[auth.auth0]
client_id = "xxx"
client_secret = "xxx"
server_metadata_url = "https://{account}.{region}.auth0.com/.well-known/openid-configuration"
client_kwargs = { "prompt" = "login" }
```

Hosted Code environments such as GitHub Codespaces have additional security controls in place preventing the login redirect to be handled properly.