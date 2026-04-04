Source: https://docs.slack.dev/tools/python-slack-sdk/reference/oauth/token_rotation

# Module slack_sdk.oauth.token_rotation

## Sub-modules

`[slack_sdk.oauth.token_rotation.async_rotator](async_rotator.html "slack_sdk.oauth.token_rotation.async_rotator")`

`[slack_sdk.oauth.token_rotation.rotator](rotator.html "slack_sdk.oauth.token_rotation.rotator")`

## Classes

`class TokenRotator (*,   client_id: str,   client_secret: str,   client: [WebClient](../../web/client.html#slack_sdk.web.client.WebClient "slack_sdk.web.client.WebClient") | None = None)`

Expand source code

```typescript
class TokenRotator:
    client: WebClient
    client_id: str
    client_secret: str

    def __init__(self, *, client_id: str, client_secret: str, client: Optional[WebClient] = None):
        self.client = client if client is not None else WebClient(token=None)
        self.client_id = client_id
        self.client_secret = client_secret

    def perform_token_rotation(
        self,
        *,
        installation: Installation,
        minutes_before_expiration: int = 120,  # 2 hours by default
    ) -> Optional[Installation]:
        """Performs token rotation if the underlying tokens (bot / user) are expired / expiring.

        Args:
            installation: the current installation data
            minutes_before_expiration: the minutes before the token expiration

        Returns:
            None if no rotation is necessary for now.
        """

        # TODO: make the following two calls in parallel for better performance

        # bot
        rotated_bot: Optional[Bot] = self.perform_bot_token_rotation(
            bot=installation.to_bot(),
            minutes_before_expiration=minutes_before_expiration,
        )

        # user
        rotated_installation: Optional[Installation] = self.perform_user_token_rotation(
            installation=installation,
            minutes_before_expiration=minutes_before_expiration,
        )

        if rotated_bot is not None:
            if rotated_installation is None:
                rotated_installation = Installation(**installation.to_dict_for_copying())
            rotated_installation.bot_token = rotated_bot.bot_token
            rotated_installation.bot_refresh_token = rotated_bot.bot_refresh_token
            rotated_installation.bot_token_expires_at = rotated_bot.bot_token_expires_at

        return rotated_installation

    def perform_bot_token_rotation(
        self,
        *,
        bot: Bot,
        minutes_before_expiration: int = 120,  # 2 hours by default
    ) -> Optional[Bot]:
        """Performs bot token rotation if the underlying bot token is expired / expiring.

        Args:
            bot: the current bot installation data
            minutes_before_expiration: the minutes before the token expiration

        Returns:
            None if no rotation is necessary for now.
        """
        if bot.bot_token_expires_at is None:
            return None
        if bot.bot_token_expires_at > time() + minutes_before_expiration * 60:
            return None

        try:
            refresh_response = self.client.oauth_v2_access(
                client_id=self.client_id,
                client_secret=self.client_secret,
                grant_type="refresh_token",
                refresh_token=bot.bot_refresh_token,
            )
            if refresh_response.get("token_type") != "bot":
                return None

            refreshed_bot = Bot(**bot.to_dict_for_copying())
            refreshed_bot.bot_token = refresh_response["access_token"]
            refreshed_bot.bot_refresh_token = refresh_response.get("refresh_token")
            refreshed_bot.bot_token_expires_at = int(time()) + int(refresh_response["expires_in"])
            return refreshed_bot

        except SlackApiError as e:
            raise SlackTokenRotationError(e)

    def perform_user_token_rotation(
        self,
        *,
        installation: Installation,
        minutes_before_expiration: int = 120,  # 2 hours by default
    ) -> Optional[Installation]:
        """Performs user token rotation if the underlying user token is expired / expiring.

        Args:
            installation: the current installation data
            minutes_before_expiration: the minutes before the token expiration

        Returns:
            None if no rotation is necessary for now.
        """
        if installation.user_token_expires_at is None:
            return None
        if installation.user_token_expires_at > time() + minutes_before_expiration * 60:
            return None

        try:
            refresh_response = self.client.oauth_v2_access(
                client_id=self.client_id,
                client_secret=self.client_secret,
                grant_type="refresh_token",
                refresh_token=installation.user_refresh_token,
            )

            if refresh_response.get("token_type") != "user":
                return None

            refreshed_installation = Installation(**installation.to_dict_for_copying())
            refreshed_installation.user_token = refresh_response.get("access_token")
            refreshed_installation.user_refresh_token = refresh_response.get("refresh_token")
            refreshed_installation.user_token_expires_at = int(time()) + int(refresh_response["expires_in"])
            return refreshed_installation

        except SlackApiError as e:
            raise SlackTokenRotationError(e)
```

### Class variables

`var client : [WebClient](../../web/client.html#slack_sdk.web.client.WebClient "slack_sdk.web.client.WebClient")`

The type of the None singleton.

`var client_id : str`

The type of the None singleton.

`var client_secret : str`

The type of the None singleton.

### Methods

`def perform_bot_token_rotation(self,   *,   bot: [Bot](../installation_store/models/bot.html#slack_sdk.oauth.installation_store.models.bot.Bot "slack_sdk.oauth.installation_store.models.bot.Bot"),   minutes_before_expiration: int = 120) ‑> [Bot](../installation_store/models/bot.html#slack_sdk.oauth.installation_store.models.bot.Bot "slack_sdk.oauth.installation_store.models.bot.Bot") | None`

Expand source code

```python
def perform_bot_token_rotation(
    self,
    *,
    bot: Bot,
    minutes_before_expiration: int = 120,  # 2 hours by default
) -> Optional[Bot]:
    """Performs bot token rotation if the underlying bot token is expired / expiring.

    Args:
        bot: the current bot installation data
        minutes_before_expiration: the minutes before the token expiration

    Returns:
        None if no rotation is necessary for now.
    """
    if bot.bot_token_expires_at is None:
        return None
    if bot.bot_token_expires_at > time() + minutes_before_expiration * 60:
        return None

    try:
        refresh_response = self.client.oauth_v2_access(
            client_id=self.client_id,
            client_secret=self.client_secret,
            grant_type="refresh_token",
            refresh_token=bot.bot_refresh_token,
        )
        if refresh_response.get("token_type") != "bot":
            return None

        refreshed_bot = Bot(**bot.to_dict_for_copying())
        refreshed_bot.bot_token = refresh_response["access_token"]
        refreshed_bot.bot_refresh_token = refresh_response.get("refresh_token")
        refreshed_bot.bot_token_expires_at = int(time()) + int(refresh_response["expires_in"])
        return refreshed_bot

    except SlackApiError as e:
        raise SlackTokenRotationError(e)
```

Performs bot token rotation if the underlying bot token is expired / expiring.

## Args

**`bot`**

the current bot installation data

**`minutes_before_expiration`**

the minutes before the token expiration

## Returns

None if no rotation is necessary for now.

`def perform_token_rotation(self,   *,   installation: [Installation](../installation_store/models/installation.html#slack_sdk.oauth.installation_store.models.installation.Installation "slack_sdk.oauth.installation_store.models.installation.Installation"),   minutes_before_expiration: int = 120) ‑> [Installation](../installation_store/models/installation.html#slack_sdk.oauth.installation_store.models.installation.Installation "slack_sdk.oauth.installation_store.models.installation.Installation") | None`

Expand source code

```python
def perform_token_rotation(
    self,
    *,
    installation: Installation,
    minutes_before_expiration: int = 120,  # 2 hours by default
) -> Optional[Installation]:
    """Performs token rotation if the underlying tokens (bot / user) are expired / expiring.

    Args:
        installation: the current installation data
        minutes_before_expiration: the minutes before the token expiration

    Returns:
        None if no rotation is necessary for now.
    """

    # TODO: make the following two calls in parallel for better performance

    # bot
    rotated_bot: Optional[Bot] = self.perform_bot_token_rotation(
        bot=installation.to_bot(),
        minutes_before_expiration=minutes_before_expiration,
    )

    # user
    rotated_installation: Optional[Installation] = self.perform_user_token_rotation(
        installation=installation,
        minutes_before_expiration=minutes_before_expiration,
    )

    if rotated_bot is not None:
        if rotated_installation is None:
            rotated_installation = Installation(**installation.to_dict_for_copying())
        rotated_installation.bot_token = rotated_bot.bot_token
        rotated_installation.bot_refresh_token = rotated_bot.bot_refresh_token
        rotated_installation.bot_token_expires_at = rotated_bot.bot_token_expires_at

    return rotated_installation
```

Performs token rotation if the underlying tokens (bot / user) are expired / expiring.

## Args (2)

**`installation`**

the current installation data

**`minutes_before_expiration`**

the minutes before the token expiration

## Returns (2)

None if no rotation is necessary for now.

`def perform_user_token_rotation(self,   *,   installation: [Installation](../installation_store/models/installation.html#slack_sdk.oauth.installation_store.models.installation.Installation "slack_sdk.oauth.installation_store.models.installation.Installation"),   minutes_before_expiration: int = 120) ‑> [Installation](../installation_store/models/installation.html#slack_sdk.oauth.installation_store.models.installation.Installation "slack_sdk.oauth.installation_store.models.installation.Installation") | None`

Expand source code

```python
def perform_user_token_rotation(
    self,
    *,
    installation: Installation,
    minutes_before_expiration: int = 120,  # 2 hours by default
) -> Optional[Installation]:
    """Performs user token rotation if the underlying user token is expired / expiring.

    Args:
        installation: the current installation data
        minutes_before_expiration: the minutes before the token expiration

    Returns:
        None if no rotation is necessary for now.
    """
    if installation.user_token_expires_at is None:
        return None
    if installation.user_token_expires_at > time() + minutes_before_expiration * 60:
        return None

    try:
        refresh_response = self.client.oauth_v2_access(
            client_id=self.client_id,
            client_secret=self.client_secret,
            grant_type="refresh_token",
            refresh_token=installation.user_refresh_token,
        )

        if refresh_response.get("token_type") != "user":
            return None

        refreshed_installation = Installation(**installation.to_dict_for_copying())
        refreshed_installation.user_token = refresh_response.get("access_token")
        refreshed_installation.user_refresh_token = refresh_response.get("refresh_token")
        refreshed_installation.user_token_expires_at = int(time()) + int(refresh_response["expires_in"])
        return refreshed_installation

    except SlackApiError as e:
        raise SlackTokenRotationError(e)
```

Performs user token rotation if the underlying user token is expired / expiring.

## Args (3)

**`installation`**

the current installation data

**`minutes_before_expiration`**

the minutes before the token expiration

## Returns (3)

None if no rotation is necessary for now.
