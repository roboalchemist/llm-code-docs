# Source: https://docs.streamlit.io/develop/api-reference/user/st.user

# st.user

A read-only, dict-like object for accessing information about the current user.

`st.user` is dependent on the host platform running your Streamlit app. If your host platform has not configured the object, `st.user` will behave as it does in a locally running app.

When authentication is configured in `secrets.toml`, Streamlit will parse the OpenID Connect (OIDC) identity token and copy the attributes to `st.user`. Check your provider's documentation for their available attributes (known as claims).

When authentication is not configured, `st.user` has no attributes.

You can access values via key or attribute notation. For example, use `st.user["email"]` or `st.user.email` to access the `email` attribute.

## Methods

- **to_dict()**
  - **Returns**: `Dict[str,str]`
  - **Description**: Get user info as a dictionary.
  - **Args**: None
  - **Returns**: A dictionary of the current user's information.

## Examples

### Example 1: Google's identity token

If you configure a basic Google OIDC connection as shown in Example 1 of `st.login()`, the following data is available in `st.user`. Streamlit adds the `is_logged_in` attribute. Additional attributes may be available depending on the configuration of the user's Google account. For more information about Google's identity tokens, see [Obtain user information from the ID token](https://developers.google.com/identity/openid-connect/openid-connect#obtainuserinfo) in Google's docs.

Your app code:

```python
import streamlit as st

if st.user.is_logged_in:
    st.write(st.user)
```

Displayed data when a user is logged in:

```json
{
    "is_logged_in": true,
    "iss": "https://accounts.google.com",
    "azp": "{client_id}.apps.googleusercontent.com",
    "aud": "{client_id}.apps.googleusercontent.com",
    "sub": "{unique_user_id}",
    "email": "{user}@gmail.com",
    "email_verified": true,
    "at_hash": "{access_token_hash}",
    "nonce": "{nonce_string}",
    "name": "{full_name}",
    "picture": "https://lh3.googleusercontent.com/a/{content_path}",
    "given_name": "{given_name}",
    "family_name": "{family_name}",
    "iat": {issued_time},
    "exp": {expiration_time}
}
```

### Example 2: Microsoft's identity token

If you configure a basic Microsoft OIDC connection as shown in Example 2 of `st.login()`, the following data is available in `st.user`. For more information about Microsoft's identity tokens, see [ID token claims reference](https://learn.microsoft.com/en-us/entra/identity-platform/id-token-claims-reference) in Microsoft's docs.

Your app code:

```python
import streamlit as st

if st.user.is_logged_in:
    st.write(st.user)
```

Displayed data when a user is logged in:

```json
{
    "is_logged_in": true,
    "ver": "2.0",
    "iss": "https://login.microsoftonline.com/{tenant_id}/v2.0",
    "sub": "{application_user_id}",
    "aud": "{application_id}",
    "exp": {expiration_time},
    "iat": {issued_time},
    "nbf": {start_time},
    "name": "{full_name}",
    "preferred_username": "{username}",
    "oid": "{user_GUID}",
    "email": "{email}",
    "tid": "{tenant_id}",
    "nonce": "{nonce_string}",
    "aio": "{opaque_string}"
}
```