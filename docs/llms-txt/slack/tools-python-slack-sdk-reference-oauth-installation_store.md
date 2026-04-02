Source: https://docs.slack.dev/tools/python-slack-sdk/reference/oauth/installation_store

# Module slack_sdk.oauth.installation_store

## Sub-modules

`[slack_sdk.oauth.installation_store.amazon_s3](amazon_s3/index.html "slack_sdk.oauth.installation_store.amazon_s3")`

`[slack_sdk.oauth.installation_store.async_cacheable_installation_store](async_cacheable_installation_store.html "slack_sdk.oauth.installation_store.async_cacheable_installation_store")`

`[slack_sdk.oauth.installation_store.async_installation_store](async_installation_store.html "slack_sdk.oauth.installation_store.async_installation_store")`

`[slack_sdk.oauth.installation_store.cacheable_installation_store](cacheable_installation_store.html "slack_sdk.oauth.installation_store.cacheable_installation_store")`

`[slack_sdk.oauth.installation_store.file](file/index.html "slack_sdk.oauth.installation_store.file")`

`[slack_sdk.oauth.installation_store.installation_store](installation_store.html "slack_sdk.oauth.installation_store.installation_store")`

Slack installation data store …

`[slack_sdk.oauth.installation_store.internals](internals.html "slack_sdk.oauth.installation_store.internals")`

`[slack_sdk.oauth.installation_store.models](models/index.html "slack_sdk.oauth.installation_store.models")`

`[slack_sdk.oauth.installation_store.sqlalchemy](sqlalchemy/index.html "slack_sdk.oauth.installation_store.sqlalchemy")`

`[slack_sdk.oauth.installation_store.sqlite3](sqlite3/index.html "slack_sdk.oauth.installation_store.sqlite3")`

## Classes

`class Bot (*,   app_id: str | None = None,   enterprise_id: str | None = None,   enterprise_name: str | None = None,   team_id: str | None = None,   team_name: str | None = None,   bot_token: str,   bot_id: str,   bot_user_id: str,   bot_scopes: str | Sequence[str] = '',   bot_refresh_token: str | None = None,   bot_token_expires_in: int | None = None,   bot_token_expires_at: int | datetime.datetime | str | None = None,   is_enterprise_install: bool | None = False,   installed_at: float | datetime.datetime | str,   custom_values: Dict[str, Any] | None = None)`

Expand source code

```typescript
class Bot:
    app_id: Optional[str]
    enterprise_id: Optional[str]
    enterprise_name: Optional[str]
    team_id: Optional[str]
    team_name: Optional[str]
    bot_token: str
    bot_id: str
    bot_user_id: str
    bot_scopes: Sequence[str]
    # only when token rotation is enabled
    bot_refresh_token: Optional[str]
    # only when token rotation is enabled
    bot_token_expires_at: Optional[int]
    is_enterprise_install: bool
    installed_at: float

    custom_values: Dict[str, Any]

    def __init__(
        self,
        *,
        app_id: Optional[str] = None,
        # org / workspace
        enterprise_id: Optional[str] = None,
        enterprise_name: Optional[str] = None,
        team_id: Optional[str] = None,
        team_name: Optional[str] = None,
        # bot
        bot_token: str,
        bot_id: str,
        bot_user_id: str,
        bot_scopes: Union[str, Sequence[str]] = "",
        # only when token rotation is enabled
        bot_refresh_token: Optional[str] = None,
        # only when token rotation is enabled
        bot_token_expires_in: Optional[int] = None,
        # only for duplicating this object
        # only when token rotation is enabled
        bot_token_expires_at: Optional[Union[int, datetime, str]] = None,
        is_enterprise_install: Optional[bool] = False,
        # timestamps
        # The expected value type is float but the internals handle other types too
        # for str values, we support only ISO datetime format.
        installed_at: Union[float, datetime, str],
        # custom values
        custom_values: Optional[Dict[str, Any]] = None,
    ):
        self.app_id = app_id
        self.enterprise_id = enterprise_id
        self.enterprise_name = enterprise_name
        self.team_id = team_id
        self.team_name = team_name

        self.bot_token = bot_token
        self.bot_id = bot_id
        self.bot_user_id = bot_user_id
        if isinstance(bot_scopes, str):
            self.bot_scopes = bot_scopes.split(",") if len(bot_scopes) > 0 else []
        else:
            self.bot_scopes = bot_scopes
        self.bot_refresh_token = bot_refresh_token

        if bot_token_expires_at is not None:
            self.bot_token_expires_at = _timestamp_to_type(bot_token_expires_at, int)
        elif bot_token_expires_in is not None:
            self.bot_token_expires_at = int(time()) + bot_token_expires_in
        else:
            self.bot_token_expires_at = None

        self.is_enterprise_install = is_enterprise_install or False

        self.installed_at = _timestamp_to_type(installed_at, float)

        self.custom_values = custom_values if custom_values is not None else {}

    def set_custom_value(self, name: str, value: Any):
        self.custom_values[name] = value

    def get_custom_value(self, name: str) -> Optional[Any]:
        return self.custom_values.get(name)

    def _to_standard_value_dict(self) -> Dict[str, Any]:
        return {
            "app_id": self.app_id,
            "enterprise_id": self.enterprise_id,
            "enterprise_name": self.enterprise_name,
            "team_id": self.team_id,
            "team_name": self.team_name,
            "bot_token": self.bot_token,
            "bot_id": self.bot_id,
            "bot_user_id": self.bot_user_id,
            "bot_scopes": ",".join(self.bot_scopes) if self.bot_scopes else None,
            "bot_refresh_token": self.bot_refresh_token,
            "bot_token_expires_at": (
                datetime.fromtimestamp(self.bot_token_expires_at, tz=timezone.utc)
                if self.bot_token_expires_at is not None
                else None
            ),
            "is_enterprise_install": self.is_enterprise_install,
            "installed_at": datetime.fromtimestamp(self.installed_at, tz=timezone.utc),
        }

    def to_dict_for_copying(self) -> Dict[str, Any]:
        return {"custom_values": self.custom_values, **self._to_standard_value_dict()}

    def to_dict(self) -> Dict[str, Any]:
        # prioritize standard_values over custom_values
        # when the same keys exist in both
        return {**self.custom_values, **self._to_standard_value_dict()}
```

### Class variables

`var app_id : str | None`

The type of the None singleton.

`var bot_id : str`

The type of the None singleton.

`var bot_refresh_token : str | None`

The type of the None singleton.

`var bot_scopes : Sequence[str]`

The type of the None singleton.

`var bot_token : str`

The type of the None singleton.

`var bot_token_expires_at : int | None`

The type of the None singleton.

`var bot_user_id : str`

The type of the None singleton.

`var custom_values : Dict[str, Any]`

The type of the None singleton.

`var enterprise_id : str | None`

The type of the None singleton.

`var enterprise_name : str | None`

The type of the None singleton.

`var installed_at : float`

The type of the None singleton.

`var is_enterprise_install : bool`

The type of the None singleton.

`var team_id : str | None`

The type of the None singleton.

`var team_name : str | None`

The type of the None singleton.

### Methods

`def get_custom_value(self, name: str) ‑> Any | None`

Expand source code

```python
def get_custom_value(self, name: str) -> Optional[Any]:
    return self.custom_values.get(name)
```

`def set_custom_value(self, name: str, value: Any)`

Expand source code

```python
def set_custom_value(self, name: str, value: Any):
    self.custom_values[name] = value
```

`def to_dict(self) ‑> Dict[str, Any]`

Expand source code

```python
def to_dict(self) -> Dict[str, Any]:
    # prioritize standard_values over custom_values
    # when the same keys exist in both
    return {**self.custom_values, **self._to_standard_value_dict()}
```

`def to_dict_for_copying(self) ‑> Dict[str, Any]`

Expand source code

```python
def to_dict_for_copying(self) -> Dict[str, Any]:
    return {"custom_values": self.custom_values, **self._to_standard_value_dict()}
```

`class FileInstallationStore (*,   base_dir: str = '$HOME/.bolt-app-installation',   historical_data_enabled: bool = True,   client_id: str | None = None,   logger: logging.Logger = <Logger slack_sdk.oauth.installation_store.file (WARNING)>)`

Expand source code

```typescript
class FileInstallationStore(InstallationStore, AsyncInstallationStore):
    def __init__(
        self,
        *,
        base_dir: str = str(Path.home()) + "/.bolt-app-installation",
        historical_data_enabled: bool = True,
        client_id: Optional[str] = None,
        logger: Logger = logging.getLogger(__name__),
    ):
        self.base_dir = base_dir
        self.historical_data_enabled = historical_data_enabled
        self.client_id = client_id
        if self.client_id is not None:
            self.base_dir = f"{self.base_dir}/{self.client_id}"
        self._logger = logger

    @property
    def logger(self) -> Logger:
        if self._logger is None:
            self._logger = logging.getLogger(__name__)
        return self._logger

    async def async_save(self, installation: Installation):
        return self.save(installation)

    async def async_save_bot(self, bot: Bot):
        return self.save_bot(bot)

    def save(self, installation: Installation):
        none = "none"
        e_id = installation.enterprise_id or none
        t_id = installation.team_id or none
        team_installation_dir = f"{self.base_dir}/{e_id}-{t_id}"
        self._mkdir(team_installation_dir)

        self.save_bot(installation.to_bot())

        if self.historical_data_enabled:
            history_version: str = str(installation.installed_at)

            # per workspace
            entity: str = json.dumps(installation.__dict__)
            with open(f"{team_installation_dir}/installer-latest", "w") as f:
                f.write(entity)
            with open(f"{team_installation_dir}/installer-{history_version}", "w") as f:
                f.write(entity)

            # per workspace per user
            u_id = installation.user_id or none
            entity = json.dumps(installation.__dict__)
            with open(f"{team_installation_dir}/installer-{u_id}-latest", "w") as f:
                f.write(entity)
            with open(f"{team_installation_dir}/installer-{u_id}-{history_version}", "w") as f:
                f.write(entity)

        else:
            u_id = installation.user_id or none
            installer_filepath = f"{team_installation_dir}/installer-{u_id}-latest"
            with open(installer_filepath, "w") as f:
                entity = json.dumps(installation.__dict__)
                f.write(entity)

    def save_bot(self, bot: Bot):
        if bot.bot_token is None:
            self.logger.debug("Skipped saving a new row because of the absense of bot token in it")
            return

        none = "none"
        e_id = bot.enterprise_id or none
        t_id = bot.team_id or none
        team_installation_dir = f"{self.base_dir}/{e_id}-{t_id}"
        self._mkdir(team_installation_dir)

        if self.historical_data_enabled:
            history_version: str = str(bot.installed_at)

            entity: str = json.dumps(bot.__dict__)
            with open(f"{team_installation_dir}/bot-latest", "w") as f:
                f.write(entity)
            with open(f"{team_installation_dir}/bot-{history_version}", "w") as f:
                f.write(entity)
        else:
            with open(f"{team_installation_dir}/bot-latest", "w") as f:
                entity = json.dumps(bot.__dict__)
                f.write(entity)

    async def async_find_bot(
        self,
        *,
        enterprise_id: Optional[str],
        team_id: Optional[str],
        is_enterprise_install: Optional[bool] = False,
    ) -> Optional[Bot]:
        return self.find_bot(
            enterprise_id=enterprise_id,
            team_id=team_id,
            is_enterprise_install=is_enterprise_install,
        )

    def find_bot(
        self,
        *,
        enterprise_id: Optional[str],
        team_id: Optional[str],
        is_enterprise_install: Optional[bool] = False,
    ) -> Optional[Bot]:
        none = "none"
        e_id = enterprise_id or none
        t_id = team_id or none
        if is_enterprise_install:
            t_id = none
        bot_filepath = f"{self.base_dir}/{e_id}-{t_id}/bot-latest"
        try:
            with open(bot_filepath) as f:
                data = json.loads(f.read())
                return Bot(**data)
        except FileNotFoundError as e:
            message = f"Installation data missing for enterprise: {e_id}, team: {t_id}: {e}"
            self.logger.debug(message)
            return None

    async def async_find_installation(
        self,
        *,
        enterprise_id: Optional[str],
        team_id: Optional[str],
        user_id: Optional[str] = None,
        is_enterprise_install: Optional[bool] = False,
    ) -> Optional[Installation]:
        return self.find_installation(
            enterprise_id=enterprise_id,
            team_id=team_id,
            user_id=user_id,
            is_enterprise_install=is_enterprise_install,
        )

    def find_installation(
        self,
        *,
        enterprise_id: Optional[str],
        team_id: Optional[str],
        user_id: Optional[str] = None,
        is_enterprise_install: Optional[bool] = False,
    ) -> Optional[Installation]:
        none = "none"
        e_id = enterprise_id or none
        t_id = team_id or none
        if is_enterprise_install:
            t_id = none
        installation_filepath = f"{self.base_dir}/{e_id}-{t_id}/installer-latest"
        if user_id is not None:
            installation_filepath = f"{self.base_dir}/{e_id}-{t_id}/installer-{user_id}-latest"

        try:
            installation: Optional[Installation] = None
            with open(installation_filepath) as f:
                data = json.loads(f.read())
                installation = Installation(**data)

            has_user_installation = user_id is not None and installation is not None
            no_bot_token_installation = installation is not None and installation.bot_token is None
            should_find_bot_installation = has_user_installation or no_bot_token_installation
            if should_find_bot_installation:
                # Retrieve the latest bot token, just in case
                # See also: https://github.com/slackapi/bolt-python/issues/664
                latest_bot_installation = self.find_bot(
                    enterprise_id=enterprise_id,
                    team_id=team_id,
                    is_enterprise_install=is_enterprise_install,
                )
                if latest_bot_installation is not None and installation.bot_token != latest_bot_installation.bot_token:
                    # NOTE: this logic is based on the assumption that every single installation has bot scopes
                    # If you need to installation patterns without bot scopes in the same S3 bucket,
                    # please fork this code and implement your own logic.
                    installation.bot_id = latest_bot_installation.bot_id
                    installation.bot_user_id = latest_bot_installation.bot_user_id
                    installation.bot_token = latest_bot_installation.bot_token
                    installation.bot_scopes = latest_bot_installation.bot_scopes
                    installation.bot_refresh_token = latest_bot_installation.bot_refresh_token
                    installation.bot_token_expires_at = latest_bot_installation.bot_token_expires_at

            return installation

        except FileNotFoundError as e:
            message = f"Installation data missing for enterprise: {e_id}, team: {t_id}: {e}"
            self.logger.debug(message)
            return None

    async def async_delete_bot(self, *, enterprise_id: Optional[str], team_id: Optional[str]) -> None:
        return self.delete_bot(enterprise_id=enterprise_id, team_id=team_id)

    def delete_bot(self, *, enterprise_id: Optional[str], team_id: Optional[str]) -> None:
        none = "none"
        e_id = enterprise_id or none
        t_id = team_id or none
        filepath_glob = f"{self.base_dir}/{e_id}-{t_id}/bot-*"
        self._delete_by_glob(e_id, t_id, filepath_glob)

    async def async_delete_installation(
        self,
        *,
        enterprise_id: Optional[str],
        team_id: Optional[str],
        user_id: Optional[str] = None,
    ) -> None:
        return self.delete_installation(enterprise_id=enterprise_id, team_id=team_id, user_id=user_id)

    def delete_installation(
        self,
        *,
        enterprise_id: Optional[str],
        team_id: Optional[str],
        user_id: Optional[str] = None,
    ) -> None:
        none = "none"
        e_id = enterprise_id or none
        t_id = team_id or none
        if user_id is not None:
            filepath_glob = f"{self.base_dir}/{e_id}-{t_id}/installer-{user_id}-*"
        else:
            filepath_glob = f"{self.base_dir}/{e_id}-{t_id}/installer-*"
        self._delete_by_glob(e_id, t_id, filepath_glob)

    def _delete_by_glob(self, e_id: str, t_id: str, filepath_glob: str):
        for filepath in glob.glob(filepath_glob):
            try:
                os.remove(filepath)
            except FileNotFoundError as e:
                message = f"Failed to delete installation data for enterprise: {e_id}, team: {t_id}: {e}"
                self.logger.warning(message)

    @staticmethod
    def _mkdir(path: Union[str, Path]):
        if isinstance(path, str):
            path = Path(path)
        path.mkdir(parents=True, exist_ok=True)
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

### Ancestors

* [InstallationStore](installation_store.html#slack_sdk.oauth.installation_store.installation_store.InstallationStore "slack_sdk.oauth.installation_store.installation_store.InstallationStore")
* [AsyncInstallationStore](async_installation_store.html#slack_sdk.oauth.installation_store.async_installation_store.AsyncInstallationStore "slack_sdk.oauth.installation_store.async_installation_store.AsyncInstallationStore")

### Instance variables

`prop logger : logging.Logger`

Expand source code

```python
@property
def logger(self) -> Logger:
    if self._logger is None:
        self._logger = logging.getLogger(__name__)
    return self._logger
```

### Inherited members

* `**[InstallationStore](installation_store.html#slack_sdk.oauth.installation_store.installation_store.InstallationStore "slack_sdk.oauth.installation_store.installation_store.InstallationStore")**`:
  * `[save](installation_store.html#slack_sdk.oauth.installation_store.installation_store.InstallationStore.save "slack_sdk.oauth.installation_store.installation_store.InstallationStore.save")`
  * `[save_bot](installation_store.html#slack_sdk.oauth.installation_store.installation_store.InstallationStore.save_bot "slack_sdk.oauth.installation_store.installation_store.InstallationStore.save_bot")`
* `**[InstallationStore](installation_store.html#slack_sdk.oauth.installation_store.installation_store.InstallationStore "slack_sdk.oauth.installation_store.installation_store.InstallationStore")**`:
  * `[find_bot](installation_store.html#slack_sdk.oauth.installation_store.installation_store.InstallationStore.find_bot "slack_sdk.oauth.installation_store.installation_store.InstallationStore.find_bot")`
* `**[InstallationStore](installation_store.html#slack_sdk.oauth.installation_store.installation_store.InstallationStore "slack_sdk.oauth.installation_store.installation_store.InstallationStore")**`:
  * `[find_installation](installation_store.html#slack_sdk.oauth.installation_store.installation_store.InstallationStore.find_installation "slack_sdk.oauth.installation_store.installation_store.InstallationStore.find_installation")`
* `**[InstallationStore](installation_store.html#slack_sdk.oauth.installation_store.installation_store.InstallationStore "slack_sdk.oauth.installation_store.installation_store.InstallationStore")**`:
  * `[delete_bot](installation_store.html#slack_sdk.oauth.installation_store.installation_store.InstallationStore.delete_bot "slack_sdk.oauth.installation_store.installation_store.InstallationStore.delete_bot")`
* `**[InstallationStore](installation_store.html#slack_sdk.oauth.installation_store.installation_store.InstallationStore "slack_sdk.oauth.installation_store.installation_store.InstallationStore")**`:
  * `[delete_all](installation_store.html#slack_sdk.oauth.installation_store.installation_store.InstallationStore.delete_all "slack_sdk.oauth.installation_store.installation_store.InstallationStore.delete_all")`
  * `[delete_installation](installation_store.html#slack_sdk.oauth.installation_store.installation_store.InstallationStore.delete_installation "slack_sdk.oauth.installation_store.installation_store.InstallationStore.delete_installation")`
* `**[AsyncInstallationStore](async_installation_store.html#slack_sdk.oauth.installation_store.async_installation_store.AsyncInstallationStore "slack_sdk.oauth.installation_store.async_installation_store.AsyncInstallationStore")**`:
  * `[async_save](async_installation_store.html#slack_sdk.oauth.installation_store.async_installation_store.AsyncInstallationStore.async_save "slack_sdk.oauth.installation_store.async_installation_store.AsyncInstallationStore.async_save")`
  * `[async_save_bot](async_installation_store.html#slack_sdk.oauth.installation_store.async_installation_store.AsyncInstallationStore.async_save_bot "slack_sdk.oauth.installation_store.async_installation_store.AsyncInstallationStore.async_save_bot")`
* `**[AsyncInstallationStore](async_installation_store.html#slack_sdk.oauth.installation_store.async_installation_store.AsyncInstallationStore "slack_sdk.oauth.installation_store.async_installation_store.AsyncInstallationStore")**`:
  * `[async_find_bot](async_installation_store.html#slack_sdk.oauth.installation_store.async_installation_store.AsyncInstallationStore.async_find_bot "slack_sdk.oauth.installation_store.async_installation_store.AsyncInstallationStore.async_find_bot")`
* `**[AsyncInstallationStore](async_installation_store.html#slack_sdk.oauth.installation_store.async_installation_store.AsyncInstallationStore "slack_sdk.oauth.installation_store.async_installation_store.AsyncInstallationStore")**`:
  * `[async_find_installation](async_installation_store.html#slack_sdk.oauth.installation_store.async_installation_store.AsyncInstallationStore.async_find_installation "slack_sdk.oauth.installation_store.async_installation_store.AsyncInstallationStore.async_find_installation")`
* `**[AsyncInstallationStore](async_installation_store.html#slack_sdk.oauth.installation_store.async_installation_store.AsyncInstallationStore "slack_sdk.oauth.installation_store.async_installation_store.AsyncInstallationStore")**`:
  * `[async_delete_bot](async_installation_store.html#slack_sdk.oauth.installation_store.async_installation_store.AsyncInstallationStore.async_delete_bot "slack_sdk.oauth.installation_store.async_installation_store.AsyncInstallationStore.async_delete_bot")`
* `**[AsyncInstallationStore](async_installation_store.html#slack_sdk.oauth.installation_store.async_installation_store.AsyncInstallationStore "slack_sdk.oauth.installation_store.async_installation_store.AsyncInstallationStore")**`:
  * `[async_delete_installation](async_installation_store.html#slack_sdk.oauth.installation_store.async_installation_store.AsyncInstallationStore.async_delete_installation "slack_sdk.oauth.installation_store.async_installation_store.AsyncInstallationStore.async_delete_installation")`
* `**[AsyncInstallationStore](async_installation_store.html#slack_sdk.oauth.installation_store.async_installation_store.AsyncInstallationStore "slack_sdk.oauth.installation_store.async_installation_store.AsyncInstallationStore")**`:
  * `[async_delete_all](async_installation_store.html#slack_sdk.oauth.installation_store.async_installation_store.AsyncInstallationStore.async_delete_all "slack_sdk.oauth.installation_store.async_installation_store.AsyncInstallationStore.async_delete_all")`

`class Installation (*,   app_id: str | None = None,   enterprise_id: str | None = None,   enterprise_name: str | None = None,   enterprise_url: str | None = None,   team_id: str | None = None,   team_name: str | None = None,   bot_token: str | None = None,   bot_id: str | None = None,   bot_user_id: str | None = None,   bot_scopes: str | Sequence[str] = '',   bot_refresh_token: str | None = None,   bot_token_expires_in: int | None = None,   bot_token_expires_at: int | datetime.datetime | str | None = None,   user_id: str,   user_token: str | None = None,   user_scopes: str | Sequence[str] = '',   user_refresh_token: str | None = None,   user_token_expires_in: int | None = None,   user_token_expires_at: int | datetime.datetime | str | None = None,   incoming_webhook_url: str | None = None,   incoming_webhook_channel: str | None = None,   incoming_webhook_channel_id: str | None = None,   incoming_webhook_configuration_url: str | None = None,   is_enterprise_install: bool | None = False,   token_type: str | None = None,   installed_at: float | datetime.datetime | str | None = None,   custom_values: Dict[str, Any] | None = None)`

Expand source code

```typescript
class Installation:
    app_id: Optional[str]
    enterprise_id: Optional[str]
    enterprise_name: Optional[str]
    enterprise_url: Optional[str]
    team_id: Optional[str]
    team_name: Optional[str]
    bot_token: Optional[str]
    bot_id: Optional[str]
    bot_user_id: Optional[str]
    bot_scopes: Optional[Sequence[str]]
    bot_refresh_token: Optional[str]  # only when token rotation is enabled
    # only when token rotation is enabled
    # Unix time (seconds): only when token rotation is enabled
    bot_token_expires_at: Optional[int]
    user_id: str
    user_token: Optional[str]
    user_scopes: Optional[Sequence[str]]
    user_refresh_token: Optional[str]  # only when token rotation is enabled
    # Unix time (seconds): only when token rotation is enabled
    user_token_expires_at: Optional[int]
    incoming_webhook_url: Optional[str]
    incoming_webhook_channel: Optional[str]
    incoming_webhook_channel_id: Optional[str]
    incoming_webhook_configuration_url: Optional[str]
    is_enterprise_install: bool
    token_type: Optional[str]
    installed_at: float

    custom_values: Dict[str, Any]

    def __init__(
        self,
        *,
        app_id: Optional[str] = None,
        # org / workspace
        enterprise_id: Optional[str] = None,
        enterprise_name: Optional[str] = None,
        enterprise_url: Optional[str] = None,
        team_id: Optional[str] = None,
        team_name: Optional[str] = None,
        # bot
        bot_token: Optional[str] = None,
        bot_id: Optional[str] = None,
        bot_user_id: Optional[str] = None,
        bot_scopes: Union[str, Sequence[str]] = "",
        bot_refresh_token: Optional[str] = None,  # only when token rotation is enabled
        # only when token rotation is enabled
        bot_token_expires_in: Optional[int] = None,
        # only for duplicating this object
        # only when token rotation is enabled
        bot_token_expires_at: Optional[Union[int, datetime, str]] = None,
        # installer
        user_id: str,
        user_token: Optional[str] = None,
        user_scopes: Union[str, Sequence[str]] = "",
        user_refresh_token: Optional[str] = None,  # only when token rotation is enabled
        # only when token rotation is enabled
        user_token_expires_in: Optional[int] = None,
        # only for duplicating this object
        # only when token rotation is enabled
        user_token_expires_at: Optional[Union[int, datetime, str]] = None,
        # incoming webhook
        incoming_webhook_url: Optional[str] = None,
        incoming_webhook_channel: Optional[str] = None,
        incoming_webhook_channel_id: Optional[str] = None,
        incoming_webhook_configuration_url: Optional[str] = None,
        # org app
        is_enterprise_install: Optional[bool] = False,
        token_type: Optional[str] = None,
        # timestamps
        # The expected value type is float but the internals handle other types too
        # for str values, we supports only ISO datetime format.
        installed_at: Optional[Union[float, datetime, str]] = None,
        # custom values
        custom_values: Optional[Dict[str, Any]] = None,
    ):
        self.app_id = app_id
        self.enterprise_id = enterprise_id
        self.enterprise_name = enterprise_name
        self.enterprise_url = enterprise_url
        self.team_id = team_id
        self.team_name = team_name
        self.bot_token = bot_token
        self.bot_id = bot_id
        self.bot_user_id = bot_user_id
        if isinstance(bot_scopes, str):
            self.bot_scopes = bot_scopes.split(",") if len(bot_scopes) > 0 else []
        else:
            self.bot_scopes = bot_scopes
        self.bot_refresh_token = bot_refresh_token

        if bot_token_expires_at is not None:
            self.bot_token_expires_at = _timestamp_to_type(bot_token_expires_at, int)
        elif bot_token_expires_in is not None:
            self.bot_token_expires_at = int(time()) + bot_token_expires_in
        else:
            self.bot_token_expires_at = None

        self.user_id = user_id
        self.user_token = user_token
        if isinstance(user_scopes, str):
            self.user_scopes = user_scopes.split(",") if len(user_scopes) > 0 else []
        else:
            self.user_scopes = user_scopes
        self.user_refresh_token = user_refresh_token

        if user_token_expires_at is not None:
            self.user_token_expires_at = _timestamp_to_type(user_token_expires_at, int)
        elif user_token_expires_in is not None:
            self.user_token_expires_at = int(time()) + user_token_expires_in
        else:
            self.user_token_expires_at = None

        self.incoming_webhook_url = incoming_webhook_url
        self.incoming_webhook_channel = incoming_webhook_channel
        self.incoming_webhook_channel_id = incoming_webhook_channel_id
        self.incoming_webhook_configuration_url = incoming_webhook_configuration_url

        self.is_enterprise_install = is_enterprise_install or False
        self.token_type = token_type

        if installed_at is None:
            self.installed_at = datetime.now().timestamp()
        else:
            self.installed_at = _timestamp_to_type(installed_at, float)

        self.custom_values = custom_values if custom_values is not None else {}

    def to_bot(self) -> Bot:
        return Bot(
            app_id=self.app_id,
            enterprise_id=self.enterprise_id,
            enterprise_name=self.enterprise_name,
            team_id=self.team_id,
            team_name=self.team_name,
            bot_token=self.bot_token,  # type: ignore[arg-type]
            bot_id=self.bot_id,  # type: ignore[arg-type]
            bot_user_id=self.bot_user_id,  # type: ignore[arg-type]
            bot_scopes=self.bot_scopes,  # type: ignore[arg-type]
            bot_refresh_token=self.bot_refresh_token,
            bot_token_expires_at=self.bot_token_expires_at,
            is_enterprise_install=self.is_enterprise_install,
            installed_at=self.installed_at,
            custom_values=self.custom_values,
        )

    def set_custom_value(self, name: str, value: Any):
        self.custom_values[name] = value

    def get_custom_value(self, name: str) -> Optional[Any]:
        return self.custom_values.get(name)

    def _to_standard_value_dict(self) -> Dict[str, Any]:
        return {
            "app_id": self.app_id,
            "enterprise_id": self.enterprise_id,
            "enterprise_name": self.enterprise_name,
            "enterprise_url": self.enterprise_url,
            "team_id": self.team_id,
            "team_name": self.team_name,
            "bot_token": self.bot_token,
            "bot_id": self.bot_id,
            "bot_user_id": self.bot_user_id,
            "bot_scopes": ",".join(self.bot_scopes) if self.bot_scopes else None,
            "bot_refresh_token": self.bot_refresh_token,
            "bot_token_expires_at": (
                datetime.fromtimestamp(self.bot_token_expires_at, tz=timezone.utc)
                if self.bot_token_expires_at is not None
                else None
            ),
            "user_id": self.user_id,
            "user_token": self.user_token,
            "user_scopes": ",".join(self.user_scopes) if self.user_scopes else None,
            "user_refresh_token": self.user_refresh_token,
            "user_token_expires_at": (
                datetime.fromtimestamp(self.user_token_expires_at, tz=timezone.utc)
                if self.user_token_expires_at is not None
                else None
            ),
            "incoming_webhook_url": self.incoming_webhook_url,
            "incoming_webhook_channel": self.incoming_webhook_channel,
            "incoming_webhook_channel_id": self.incoming_webhook_channel_id,
            "incoming_webhook_configuration_url": self.incoming_webhook_configuration_url,
            "is_enterprise_install": self.is_enterprise_install,
            "token_type": self.token_type,
            "installed_at": datetime.fromtimestamp(self.installed_at, tz=timezone.utc),
        }

    def to_dict_for_copying(self) -> Dict[str, Any]:
        return {"custom_values": self.custom_values, **self._to_standard_value_dict()}

    def to_dict(self) -> Dict[str, Any]:
        # prioritize standard_values over custom_values
        # when the same keys exist in both
        return {**self.custom_values, **self._to_standard_value_dict()}
```

### Class variables (2)

`var app_id : str | None`

The type of the None singleton.

`var bot_id : str | None`

The type of the None singleton.

`var bot_refresh_token : str | None`

The type of the None singleton.

`var bot_scopes : Sequence[str] | None`

The type of the None singleton.

`var bot_token : str | None`

The type of the None singleton.

`var bot_token_expires_at : int | None`

The type of the None singleton.

`var bot_user_id : str | None`

The type of the None singleton.

`var custom_values : Dict[str, Any]`

The type of the None singleton.

`var enterprise_id : str | None`

The type of the None singleton.

`var enterprise_name : str | None`

The type of the None singleton.

`var enterprise_url : str | None`

The type of the None singleton.

`var incoming_webhook_channel : str | None`

The type of the None singleton.

`var incoming_webhook_channel_id : str | None`

The type of the None singleton.

`var incoming_webhook_configuration_url : str | None`

The type of the None singleton.

`var incoming_webhook_url : str | None`

The type of the None singleton.

`var installed_at : float`

The type of the None singleton.

`var is_enterprise_install : bool`

The type of the None singleton.

`var team_id : str | None`

The type of the None singleton.

`var team_name : str | None`

The type of the None singleton.

`var token_type : str | None`

The type of the None singleton.

`var user_id : str`

The type of the None singleton.

`var user_refresh_token : str | None`

The type of the None singleton.

`var user_scopes : Sequence[str] | None`

The type of the None singleton.

`var user_token : str | None`

The type of the None singleton.

`var user_token_expires_at : int | None`

The type of the None singleton.

### Methods (2)

`def get_custom_value(self, name: str) ‑> Any | None`

Expand source code

```python
def get_custom_value(self, name: str) -> Optional[Any]:
    return self.custom_values.get(name)
```

`def set_custom_value(self, name: str, value: Any)`

Expand source code

```python
def set_custom_value(self, name: str, value: Any):
    self.custom_values[name] = value
```

`def to_bot(self) ‑> [Bot](models/bot.html#slack_sdk.oauth.installation_store.models.bot.Bot "slack_sdk.oauth.installation_store.models.bot.Bot")`

Expand source code

```python
def to_bot(self) -> Bot:
    return Bot(
        app_id=self.app_id,
        enterprise_id=self.enterprise_id,
        enterprise_name=self.enterprise_name,
        team_id=self.team_id,
        team_name=self.team_name,
        bot_token=self.bot_token,  # type: ignore[arg-type]
        bot_id=self.bot_id,  # type: ignore[arg-type]
        bot_user_id=self.bot_user_id,  # type: ignore[arg-type]
        bot_scopes=self.bot_scopes,  # type: ignore[arg-type]
        bot_refresh_token=self.bot_refresh_token,
        bot_token_expires_at=self.bot_token_expires_at,
        is_enterprise_install=self.is_enterprise_install,
        installed_at=self.installed_at,
        custom_values=self.custom_values,
    )
```

`def to_dict(self) ‑> Dict[str, Any]`

Expand source code

```python
def to_dict(self) -> Dict[str, Any]:
    # prioritize standard_values over custom_values
    # when the same keys exist in both
    return {**self.custom_values, **self._to_standard_value_dict()}
```

`def to_dict_for_copying(self) ‑> Dict[str, Any]`

Expand source code

```python
def to_dict_for_copying(self) -> Dict[str, Any]:
    return {"custom_values": self.custom_values, **self._to_standard_value_dict()}
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

* [AmazonS3InstallationStore](amazon_s3/index.html#slack_sdk.oauth.installation_store.amazon_s3.AmazonS3InstallationStore "slack_sdk.oauth.installation_store.amazon_s3.AmazonS3InstallationStore")
* [CacheableInstallationStore](cacheable_installation_store.html#slack_sdk.oauth.installation_store.cacheable_installation_store.CacheableInstallationStore "slack_sdk.oauth.installation_store.cacheable_installation_store.CacheableInstallationStore")
* [FileInstallationStore](file/index.html#slack_sdk.oauth.installation_store.file.FileInstallationStore "slack_sdk.oauth.installation_store.file.FileInstallationStore")
* [SQLAlchemyInstallationStore](sqlalchemy/index.html#slack_sdk.oauth.installation_store.sqlalchemy.SQLAlchemyInstallationStore "slack_sdk.oauth.installation_store.sqlalchemy.SQLAlchemyInstallationStore")
* [SQLite3InstallationStore](sqlite3/index.html#slack_sdk.oauth.installation_store.sqlite3.SQLite3InstallationStore "slack_sdk.oauth.installation_store.sqlite3.SQLite3InstallationStore")

### Instance variables (2)

`prop logger : logging.Logger`

Expand source code

```python
@property
def logger(self) -> Logger:
    raise NotImplementedError()
```

### Methods (3)

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

`def find_bot(self,   *,   enterprise_id: str | None,   team_id: str | None,   is_enterprise_install: bool | None = False) ‑> [Bot](models/bot.html#slack_sdk.oauth.installation_store.models.bot.Bot "slack_sdk.oauth.installation_store.models.bot.Bot") | None`

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

`def find_installation(self,   *,   enterprise_id: str | None,   team_id: str | None,   user_id: str | None = None,   is_enterprise_install: bool | None = False) ‑> [Installation](models/installation.html#slack_sdk.oauth.installation_store.models.installation.Installation "slack_sdk.oauth.installation_store.models.installation.Installation") | None`

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

`def save(self,   installation: [Installation](models/installation.html#slack_sdk.oauth.installation_store.models.installation.Installation "slack_sdk.oauth.installation_store.models.installation.Installation"))`

Expand source code

```python
def save(self, installation: Installation):
    """Saves an installation data"""
    raise NotImplementedError()
```

Saves an installation data

`def save_bot(self,   bot: [Bot](models/bot.html#slack_sdk.oauth.installation_store.models.bot.Bot "slack_sdk.oauth.installation_store.models.bot.Bot"))`

Expand source code

```python
def save_bot(self, bot: Bot):
    """Saves a bot installation data"""
    raise NotImplementedError()
```

Saves a bot installation data
