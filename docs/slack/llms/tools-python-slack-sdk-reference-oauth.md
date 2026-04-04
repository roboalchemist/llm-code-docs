Source: https://docs.slack.dev/tools/python-slack-sdk/reference/oauth

# Module slack_sdk.oauth

Modules for implementing the Slack OAuth flow

[https://docs.slack.dev/tools/python-slack-sdk/oauth](https://docs.slack.dev/tools/python-slack-sdk/oauth)

## Sub-modules

`[slack_sdk.oauth.authorize_url_generator](authorize_url_generator/index.html "slack_sdk.oauth.authorize_url_generator")`

`[slack_sdk.oauth.installation_store](installation_store/index.html "slack_sdk.oauth.installation_store")`

`[slack_sdk.oauth.redirect_uri_page_renderer](redirect_uri_page_renderer/index.html "slack_sdk.oauth.redirect_uri_page_renderer")`

`[slack_sdk.oauth.sqlalchemy_utils](sqlalchemy_utils/index.html "slack_sdk.oauth.sqlalchemy_utils")`

`[slack_sdk.oauth.state_store](state_store/index.html "slack_sdk.oauth.state_store")`

OAuth state parameter data store …

`[slack_sdk.oauth.state_utils](state_utils/index.html "slack_sdk.oauth.state_utils")`

`[slack_sdk.oauth.token_rotation](token_rotation/index.html "slack_sdk.oauth.token_rotation")`

## Classes

`class AuthorizeUrlGenerator (*,   client_id: str,   redirect_uri: str | None = None,   scopes: Sequence[str] | None = None,   user_scopes: Sequence[str] | None = None,   authorization_url: str = 'https://slack.com/oauth/v2/authorize')`

Expand source code

```typescript
class AuthorizeUrlGenerator:
    def __init__(
        self,
        *,
        client_id: str,
        redirect_uri: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        user_scopes: Optional[Sequence[str]] = None,
        authorization_url: str = "https://slack.com/oauth/v2/authorize",
    ):
        self.client_id = client_id
        self.redirect_uri = redirect_uri
        self.scopes = scopes
        self.user_scopes = user_scopes
        self.authorization_url = authorization_url

    def generate(self, state: str, team: Optional[str] = None) -> str:
        scopes = ",".join(self.scopes) if self.scopes else ""
        user_scopes = ",".join(self.user_scopes) if self.user_scopes else ""
        url = (
            f"{self.authorization_url}?"
            f"state={state}&"
            f"client_id={self.client_id}&"
            f"scope={scopes}&"
            f"user_scope={user_scopes}"
        )
        if self.redirect_uri is not None:
            url += f"&redirect_uri={self.redirect_uri}"
        if team is not None:
            url += f"&team={team}"
        return url
```

### Methods

`def generate(self, state: str, team: str | None = None) ‑> str`

Expand source code

```python
def generate(self, state: str, team: Optional[str] = None) -> str:
    scopes = ",".join(self.scopes) if self.scopes else ""
    user_scopes = ",".join(self.user_scopes) if self.user_scopes else ""
    url = (
        f"{self.authorization_url}?"
        f"state={state}&"
        f"client_id={self.client_id}&"
        f"scope={scopes}&"
        f"user_scope={user_scopes}"
    )
    if self.redirect_uri is not None:
        url += f"&redirect_uri={self.redirect_uri}"
    if team is not None:
        url += f"&team={team}"
    return url
```

`class InstallationStore`

Expand source code

```typescript
class InstallationStore:
    """The installation store interface.

    The minimum required methods are:

    * save(installation)
    * find_installation(enterprise_id, team_id, user_id, is_enterprise_install)

    If you would like to properly handle app uninstallations and token revocations,
    the following methods should be implemented.

    * delete_installation(enterprise_id, team_id, user_id)
    * delete_all(enterprise_id, team_id)

    If your app needs only bot scope installations, the simpler way to implement would be:

    * save(installation)
    * find_bot(enterprise_id, team_id, is_enterprise_install)
    * delete_bot(enterprise_id, team_id)
    * delete_all(enterprise_id, team_id)
    """

    @property
    def logger(self) -> Logger:
        raise NotImplementedError()

    def save(self, installation: Installation):
        """Saves an installation data"""
        raise NotImplementedError()

    def save_bot(self, bot: Bot):
        """Saves a bot installation data"""
        raise NotImplementedError()

    def find_bot(
        self,
        *,
        enterprise_id: Optional[str],
        team_id: Optional[str],
        is_enterprise_install: Optional[bool] = False,
    ) -> Optional[Bot]:
        """Finds a bot scope installation per workspace / org"""
        raise NotImplementedError()

    def find_installation(
        self,
        *,
        enterprise_id: Optional[str],
        team_id: Optional[str],
        user_id: Optional[str] = None,
        is_enterprise_install: Optional[bool] = False,
    ) -> Optional[Installation]:
        """Finds a relevant installation for the given IDs.
        If the user_id is absent, this method may return the latest installation in the workspace / org.
        """
        raise NotImplementedError()

    def delete_bot(
        self,
        *,
        enterprise_id: Optional[str],
        team_id: Optional[str],
    ) -> None:
        """Deletes a bot scope installation per workspace / org"""
        raise NotImplementedError()

    def delete_installation(
        self,
        *,
        enterprise_id: Optional[str],
        team_id: Optional[str],
        user_id: Optional[str] = None,
    ) -> None:
        """Deletes an installation that matches the given IDs"""
        raise NotImplementedError()

    def delete_all(
        self,
        *,
        enterprise_id: Optional[str],
        team_id: Optional[str],
    ):
        """Deletes all installation data for the given workspace / org"""
        self.delete_bot(enterprise_id=enterprise_id, team_id=team_id)
        self.delete_installation(enterprise_id=enterprise_id, team_id=team_id)
```

The installation store interface.

The minimum required methods are:

* save(installation)
* find\_installation(enterprise\_id, team\_id, user\_id, is\_enterprise\_install)

If you would like to properly handle app uninstallations and token revocations, the following methods should be implemented.

* delete\_installation(enterprise\_id, team\_id, user\_id)
* delete\_all(enterprise\_id, team\_id)

If your app needs only bot scope installations, the simpler way to implement would be:

* save(installation)
* find\_bot(enterprise\_id, team\_id, is\_enterprise\_install)
* delete\_bot(enterprise\_id, team\_id)
* delete\_all(enterprise\_id, team\_id)

### Subclasses

* [AmazonS3InstallationStore](installation_store/amazon_s3/index.html#slack_sdk.oauth.installation_store.amazon_s3.AmazonS3InstallationStore "slack_sdk.oauth.installation_store.amazon_s3.AmazonS3InstallationStore")
* [CacheableInstallationStore](installation_store/cacheable_installation_store.html#slack_sdk.oauth.installation_store.cacheable_installation_store.CacheableInstallationStore "slack_sdk.oauth.installation_store.cacheable_installation_store.CacheableInstallationStore")
* [FileInstallationStore](installation_store/file/index.html#slack_sdk.oauth.installation_store.file.FileInstallationStore "slack_sdk.oauth.installation_store.file.FileInstallationStore")
* [SQLAlchemyInstallationStore](installation_store/sqlalchemy/index.html#slack_sdk.oauth.installation_store.sqlalchemy.SQLAlchemyInstallationStore "slack_sdk.oauth.installation_store.sqlalchemy.SQLAlchemyInstallationStore")
* [SQLite3InstallationStore](installation_store/sqlite3/index.html#slack_sdk.oauth.installation_store.sqlite3.SQLite3InstallationStore "slack_sdk.oauth.installation_store.sqlite3.SQLite3InstallationStore")

### Instance variables

`prop logger : logging.Logger`

Expand source code

```python
@property
def logger(self) -> Logger:
    raise NotImplementedError()
```

### Methods (2)

`def delete_all(self, *, enterprise_id: str | None, team_id: str | None)`

Expand source code

```python
def delete_all(
    self,
    *,
    enterprise_id: Optional[str],
    team_id: Optional[str],
):
    """Deletes all installation data for the given workspace / org"""
    self.delete_bot(enterprise_id=enterprise_id, team_id=team_id)
    self.delete_installation(enterprise_id=enterprise_id, team_id=team_id)
```

Deletes all installation data for the given workspace / org

`def delete_bot(self, *, enterprise_id: str | None, team_id: str | None) ‑> None`

Expand source code

```python
def delete_bot(
    self,
    *,
    enterprise_id: Optional[str],
    team_id: Optional[str],
) -> None:
    """Deletes a bot scope installation per workspace / org"""
    raise NotImplementedError()
```

Deletes a bot scope installation per workspace / org

`def delete_installation(self, *, enterprise_id: str | None, team_id: str | None, user_id: str | None = None) ‑> None`

Expand source code

```python
def delete_installation(
    self,
    *,
    enterprise_id: Optional[str],
    team_id: Optional[str],
    user_id: Optional[str] = None,
) -> None:
    """Deletes an installation that matches the given IDs"""
    raise NotImplementedError()
```

Deletes an installation that matches the given IDs

`def find_bot(self,   *,   enterprise_id: str | None,   team_id: str | None,   is_enterprise_install: bool | None = False) ‑> [Bot](installation_store/models/bot.html#slack_sdk.oauth.installation_store.models.bot.Bot "slack_sdk.oauth.installation_store.models.bot.Bot") | None`

Expand source code

```python
def find_bot(
    self,
    *,
    enterprise_id: Optional[str],
    team_id: Optional[str],
    is_enterprise_install: Optional[bool] = False,
) -> Optional[Bot]:
    """Finds a bot scope installation per workspace / org"""
    raise NotImplementedError()
```

Finds a bot scope installation per workspace / org

`def find_installation(self,   *,   enterprise_id: str | None,   team_id: str | None,   user_id: str | None = None,   is_enterprise_install: bool | None = False) ‑> [Installation](installation_store/models/installation.html#slack_sdk.oauth.installation_store.models.installation.Installation "slack_sdk.oauth.installation_store.models.installation.Installation") | None`

Expand source code

```python
def find_installation(
    self,
    *,
    enterprise_id: Optional[str],
    team_id: Optional[str],
    user_id: Optional[str] = None,
    is_enterprise_install: Optional[bool] = False,
) -> Optional[Installation]:
    """Finds a relevant installation for the given IDs.
    If the user_id is absent, this method may return the latest installation in the workspace / org.
    """
    raise NotImplementedError()
```

Finds a relevant installation for the given IDs. If the user\_id is absent, this method may return the latest installation in the workspace / org.

`def save(self,   installation: [Installation](installation_store/models/installation.html#slack_sdk.oauth.installation_store.models.installation.Installation "slack_sdk.oauth.installation_store.models.installation.Installation"))`

Expand source code

```python
def save(self, installation: Installation):
    """Saves an installation data"""
    raise NotImplementedError()
```

Saves an installation data

`def save_bot(self,   bot: [Bot](installation_store/models/bot.html#slack_sdk.oauth.installation_store.models.bot.Bot "slack_sdk.oauth.installation_store.models.bot.Bot"))`

Expand source code

```python
def save_bot(self, bot: Bot):
    """Saves a bot installation data"""
    raise NotImplementedError()
```

Saves a bot installation data

`class OAuthStateStore`

Expand source code

```typescript
class OAuthStateStore:
    @property
    def logger(self) -> Logger:
        raise NotImplementedError()

    def issue(self, *args, **kwargs) -> str:
        raise NotImplementedError()

    def consume(self, state: str) -> bool:
        raise NotImplementedError()
```

### Subclasses (2)

* [AmazonS3OAuthStateStore](state_store/amazon_s3/index.html#slack_sdk.oauth.state_store.amazon_s3.AmazonS3OAuthStateStore "slack_sdk.oauth.state_store.amazon_s3.AmazonS3OAuthStateStore")
* [FileOAuthStateStore](state_store/file/index.html#slack_sdk.oauth.state_store.file.FileOAuthStateStore "slack_sdk.oauth.state_store.file.FileOAuthStateStore")
* [SQLAlchemyOAuthStateStore](state_store/sqlalchemy/index.html#slack_sdk.oauth.state_store.sqlalchemy.SQLAlchemyOAuthStateStore "slack_sdk.oauth.state_store.sqlalchemy.SQLAlchemyOAuthStateStore")
* [SQLite3OAuthStateStore](state_store/sqlite3/index.html#slack_sdk.oauth.state_store.sqlite3.SQLite3OAuthStateStore "slack_sdk.oauth.state_store.sqlite3.SQLite3OAuthStateStore")

### Instance variables (2)

`prop logger : logging.Logger`

Expand source code

```python
@property
def logger(self) -> Logger:
    raise NotImplementedError()
```

### Methods (3)

`def consume(self, state: str) ‑> bool`

Expand source code

```python
def consume(self, state: str) -> bool:
    raise NotImplementedError()
```

`def issue(self, *args, **kwargs) ‑> str`

Expand source code

```python
def issue(self, *args, **kwargs) -> str:
    raise NotImplementedError()
```

`class OAuthStateUtils (*, cookie_name: str = 'slack-app-oauth-state', expiration_seconds: int = 600)`

Expand source code

```typescript
class OAuthStateUtils:
    cookie_name: str
    expiration_seconds: int

    default_cookie_name: str = "slack-app-oauth-state"
    default_expiration_seconds: int = 60 * 10  # 10 minutes

    def __init__(
        self,
        *,
        cookie_name: str = default_cookie_name,
        expiration_seconds: int = default_expiration_seconds,
    ):
        self.cookie_name = cookie_name
        self.expiration_seconds = expiration_seconds

    def build_set_cookie_for_new_state(self, state: str) -> str:
        return f"{self.cookie_name}={state}; " "Secure; " "HttpOnly; " "Path=/; " f"Max-Age={self.expiration_seconds}"

    def build_set_cookie_for_deletion(self) -> str:
        return f"{self.cookie_name}=deleted; " "Secure; " "HttpOnly; " "Path=/; " "Expires=Thu, 01 Jan 1970 00:00:00 GMT"

    def is_valid_browser(
        self,
        state: Optional[str],
        request_headers: Dict[str, Union[str, Sequence[str]]],
    ) -> bool:
        if state is None or request_headers is None or request_headers.get("cookie", None) is None:
            return False
        cookies = request_headers["cookie"]
        if isinstance(cookies, str):
            cookies = [cookies]
        for cookie in cookies:
            values = cookie.split(";")
            for value in values:
                # handle quoted cookie values (e.g. due to base64 encoding)
                if value.strip().replace('"', "").replace("'", "") == f"{self.cookie_name}={state}":
                    return True
        return False
```

### Class variables

`var cookie_name : str`

The type of the None singleton.

`var default_cookie_name : str`

The type of the None singleton.

`var default_expiration_seconds : int`

The type of the None singleton.

`var expiration_seconds : int`

The type of the None singleton.

### Methods (4)

`def build_set_cookie_for_deletion(self) ‑> str`

Expand source code

```python
def build_set_cookie_for_deletion(self) -> str:
    return f"{self.cookie_name}=deleted; " "Secure; " "HttpOnly; " "Path=/; " "Expires=Thu, 01 Jan 1970 00:00:00 GMT"
```

`def build_set_cookie_for_new_state(self, state: str) ‑> str`

Expand source code

```python
def build_set_cookie_for_new_state(self, state: str) -> str:
    return f"{self.cookie_name}={state}; " "Secure; " "HttpOnly; " "Path=/; " f"Max-Age={self.expiration_seconds}"
```

`def is_valid_browser(self, state: str | None, request_headers: Dict[str, str | Sequence[str]]) ‑> bool`

Expand source code

```python
def is_valid_browser(
    self,
    state: Optional[str],
    request_headers: Dict[str, Union[str, Sequence[str]]],
) -> bool:
    if state is None or request_headers is None or request_headers.get("cookie", None) is None:
        return False
    cookies = request_headers["cookie"]
    if isinstance(cookies, str):
        cookies = [cookies]
    for cookie in cookies:
        values = cookie.split(";")
        for value in values:
            # handle quoted cookie values (e.g. due to base64 encoding)
            if value.strip().replace('"', "").replace("'", "") == f"{self.cookie_name}={state}":
                return True
    return False
```

`class OpenIDConnectAuthorizeUrlGenerator (*,   client_id: str,   redirect_uri: str,   scopes: Sequence[str] | None = None,   authorization_url: str = 'https://slack.com/openid/connect/authorize')`

Expand source code

```typescript
class OpenIDConnectAuthorizeUrlGenerator:
    """Refer to https://openid.net/specs/openid-connect-core-1_0.html"""

    def __init__(
        self,
        *,
        client_id: str,
        redirect_uri: str,
        scopes: Optional[Sequence[str]] = None,
        authorization_url: str = "https://slack.com/openid/connect/authorize",
    ):
        self.client_id = client_id
        self.redirect_uri = redirect_uri
        self.scopes = scopes
        self.authorization_url = authorization_url

    def generate(self, state: str, nonce: Optional[str] = None, team: Optional[str] = None) -> str:
        scopes = ",".join(self.scopes) if self.scopes else ""
        url = (
            f"{self.authorization_url}?"
            "response_type=code&"
            f"state={state}&"
            f"client_id={self.client_id}&"
            f"scope={scopes}&"
            f"redirect_uri={self.redirect_uri}"
        )
        if team is not None:
            url += f"&team={team}"
        if nonce is not None:
            url += f"&nonce={nonce}"
        return url
```

Refer to [https://openid.net/specs/openid-connect-core-1\_0.html](https://openid.net/specs/openid-connect-core-1_0.html)

### Methods (5)

`def generate(self, state: str, nonce: str | None = None, team: str | None = None) ‑> str`

Expand source code

```python
def generate(self, state: str, nonce: Optional[str] = None, team: Optional[str] = None) -> str:
    scopes = ",".join(self.scopes) if self.scopes else ""
    url = (
        f"{self.authorization_url}?"
        "response_type=code&"
        f"state={state}&"
        f"client_id={self.client_id}&"
        f"scope={scopes}&"
        f"redirect_uri={self.redirect_uri}"
    )
    if team is not None:
        url += f"&team={team}"
    if nonce is not None:
        url += f"&nonce={nonce}"
    return url
```

`class RedirectUriPageRenderer (*,   install_path: str,   redirect_uri_path: str,   success_url: str | None = None,   failure_url: str | None = None)`

Expand source code

```typescript
class RedirectUriPageRenderer:
    def __init__(
        self,
        *,
        install_path: str,
        redirect_uri_path: str,
        success_url: Optional[str] = None,
        failure_url: Optional[str] = None,
    ):
        self.install_path = install_path
        self.redirect_uri_path = redirect_uri_path
        self.success_url = success_url
        self.failure_url = failure_url

    def render_success_page(
        self,
        app_id: str,
        team_id: Optional[str],
        is_enterprise_install: Optional[bool] = None,
        enterprise_url: Optional[str] = None,
    ) -> str:
        url = self.success_url
        if url is None:
            if is_enterprise_install is True and enterprise_url is not None and app_id is not None:
                url = f"{enterprise_url}manage/organization/apps/profile/{app_id}/workspaces/add"
            elif team_id is None or app_id is None:
                url = "slack://open"
            else:
                url = f"slack://app?team={team_id}&id={app_id}"
        browser_url = f"https://app.slack.com/client/{team_id}"

        return f"""
<html>
<head>
<meta http-equiv="refresh" content="0; URL={html.escape(url)}">
<style>
body {{
  padding: 10px 15px;
  font-family: verdana;
  text-align: center;
}}
</style>
</head>
<body>
<h2>Thank you!</h2>
<p>Redirecting to the Slack App... click <a href="{html.escape(url)}">here</a>. If you use the browser version of Slack, click <a href="{html.escape(browser_url)}" target="_blank">this link</a> instead.</p>
</body>
</html>
"""  # noqa: E501

    def render_failure_page(self, reason: str) -> str:
        return f"""
<html>
<head>
<style>
body {{
  padding: 10px 15px;
  font-family: verdana;
  text-align: center;
}}
</style>
</head>
<body>
<h2>Oops, Something Went Wrong!</h2>
<p>Please try again from <a href="{html.escape(self.install_path)}">here</a> or contact the app owner (reason: {html.escape(reason)})</p>
</body>
</html>
"""  # noqa: E501
```

### Methods (6)

`def render_failure_page(self, reason: str) ‑> str`

Expand source code

```python
    def render_failure_page(self, reason: str) -> str:
        return f"""
<html>
<head>
<style>
body {{
  padding: 10px 15px;
  font-family: verdana;
  text-align: center;
}}
</style>
</head>
<body>
<h2>Oops, Something Went Wrong!</h2>
<p>Please try again from <a href="{html.escape(self.install_path)}">here</a> or contact the app owner (reason: {html.escape(reason)})</p>
</body>
</html>
"""  # noqa: E501
```

`def render_success_page(self,   app_id: str,   team_id: str | None,   is_enterprise_install: bool | None = None,   enterprise_url: str | None = None) ‑> str`

Expand source code

```python
    def render_success_page(
        self,
        app_id: str,
        team_id: Optional[str],
        is_enterprise_install: Optional[bool] = None,
        enterprise_url: Optional[str] = None,
    ) -> str:
        url = self.success_url
        if url is None:
            if is_enterprise_install is True and enterprise_url is not None and app_id is not None:
                url = f"{enterprise_url}manage/organization/apps/profile/{app_id}/workspaces/add"
            elif team_id is None or app_id is None:
                url = "slack://open"
            else:
                url = f"slack://app?team={team_id}&id={app_id}"
        browser_url = f"https://app.slack.com/client/{team_id}"

        return f"""
<html>
<head>
<meta http-equiv="refresh" content="0; URL={html.escape(url)}">
<style>
body {{
  padding: 10px 15px;
  font-family: verdana;
  text-align: center;
}}
</style>
</head>
<body>
<h2>Thank you!</h2>
<p>Redirecting to the Slack App... click <a href="{html.escape(url)}">here</a>. If you use the browser version of Slack, click <a href="{html.escape(browser_url)}" target="_blank">this link</a> instead.</p>
</body>
</html>
"""  # noqa: E501
```
