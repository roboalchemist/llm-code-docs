# Source: https://docs.streamlit.io/develop/api-reference/user/st.logout

# st.logout

Logout the current user.

This command removes the user's information from `st.user`, deletes their identity cookie, and redirects them back to your app's home page. This creates a new session.

If the user has multiple sessions open in the same browser, `st.user` will not be cleared in any other session. `st.user` only reads from the identity cookie at the start of a session. After a session is running, you must call `st.login()` or `st.logout()` within that session to update `st.user`.

## Note

This does not log the user out of their underlying account from the identity provider.

## Example

### .streamlit/secrets.toml

```toml
[auth]
redirect_uri = "http://localhost:8501/oauth2callback"
cookie_secret = "xxx"
client_id = "xxx"
client_secret = "xxx"
server_metadata_url = "https://accounts.google.com/.well-known/openid-configuration"  # fmt: skip
```

### Your app code

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

## Related Links

- [Previous: st.login](/develop/api-reference/user/st.login)
- [Next: st.user](/develop/api-reference/user/st.user)