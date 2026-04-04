Source: https://docs.slack.dev/tools/python-slack-sdk/reference/oauth/state_store

# Module slack_sdk.oauth.state_store

OAuth state parameter data store

Refer to [https://docs.slack.dev/tools/python-slack-sdk/oauth](https://docs.slack.dev/tools/python-slack-sdk/oauth) for details.

## Sub-modules

`[slack_sdk.oauth.state_store.amazon_s3](amazon_s3/index.html "slack_sdk.oauth.state_store.amazon_s3")`

`[slack_sdk.oauth.state_store.async_state_store](async_state_store.html "slack_sdk.oauth.state_store.async_state_store")`

`[slack_sdk.oauth.state_store.file](file/index.html "slack_sdk.oauth.state_store.file")`

`[slack_sdk.oauth.state_store.sqlalchemy](sqlalchemy/index.html "slack_sdk.oauth.state_store.sqlalchemy")`

`[slack_sdk.oauth.state_store.sqlite3](sqlite3/index.html "slack_sdk.oauth.state_store.sqlite3")`

`[slack_sdk.oauth.state_store.state_store](state_store.html "slack_sdk.oauth.state_store.state_store")`

## Classes

`class FileOAuthStateStore (*,   expiration_seconds: int,   base_dir: str = '$HOME/.bolt-app-oauth-state',   client_id: str | None = None,   logger: logging.Logger = <Logger slack_sdk.oauth.state_store.file (WARNING)>)`

Expand source code

```typescript
class FileOAuthStateStore(OAuthStateStore, AsyncOAuthStateStore):
    def __init__(
        self,
        *,
        expiration_seconds: int,
        base_dir: str = str(Path.home()) + "/.bolt-app-oauth-state",
        client_id: Optional[str] = None,
        logger: Logger = logging.getLogger(__name__),
    ):
        self.expiration_seconds = expiration_seconds

        self.base_dir = base_dir
        self.client_id = client_id
        if self.client_id is not None:
            self.base_dir = f"{self.base_dir}/{self.client_id}"
        self._logger = logger

    @property
    def logger(self) -> Logger:
        if self._logger is None:
            self._logger = logging.getLogger(__name__)
        return self._logger

    async def async_issue(self, *args, **kwargs) -> str:
        return self.issue(*args, **kwargs)

    async def async_consume(self, state: str) -> bool:
        return self.consume(state)

    def issue(self, *args, **kwargs) -> str:
        state = str(uuid4())
        self._mkdir(self.base_dir)
        filepath = f"{self.base_dir}/{state}"
        with open(filepath, "w") as f:
            content = str(time.time())
            f.write(content)
        return state

    def consume(self, state: str) -> bool:
        filepath = f"{self.base_dir}/{state}"
        try:
            with open(filepath) as f:
                created = float(f.read())
                expiration = created + self.expiration_seconds
                still_valid: bool = time.time() < expiration

            os.remove(filepath)  # consume the file by deleting it
            return still_valid

        except FileNotFoundError as e:
            message = f"Failed to find any persistent data for state: {state} - {e}"
            self.logger.warning(message)
            return False

    @staticmethod
    def _mkdir(path: Union[str, Path]):
        if isinstance(path, str):
            path = Path(path)
        path.mkdir(parents=True, exist_ok=True)
```

### Ancestors

* [OAuthStateStore](state_store.html#slack_sdk.oauth.state_store.state_store.OAuthStateStore "slack_sdk.oauth.state_store.state_store.OAuthStateStore")
* [AsyncOAuthStateStore](async_state_store.html#slack_sdk.oauth.state_store.async_state_store.AsyncOAuthStateStore "slack_sdk.oauth.state_store.async_state_store.AsyncOAuthStateStore")

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

### Methods

`async def async_consume(self, state: str) ‑> bool`

Expand source code

```python
async def async_consume(self, state: str) -> bool:
    return self.consume(state)
```

`async def async_issue(self, *args, **kwargs) ‑> str`

Expand source code

```python
async def async_issue(self, *args, **kwargs) -> str:
    return self.issue(*args, **kwargs)
```

`def consume(self, state: str) ‑> bool`

Expand source code

```python
def consume(self, state: str) -> bool:
    filepath = f"{self.base_dir}/{state}"
    try:
        with open(filepath) as f:
            created = float(f.read())
            expiration = created + self.expiration_seconds
            still_valid: bool = time.time() < expiration

        os.remove(filepath)  # consume the file by deleting it
        return still_valid

    except FileNotFoundError as e:
        message = f"Failed to find any persistent data for state: {state} - {e}"
        self.logger.warning(message)
        return False
```

`def issue(self, *args, **kwargs) ‑> str`

Expand source code

```python
def issue(self, *args, **kwargs) -> str:
    state = str(uuid4())
    self._mkdir(self.base_dir)
    filepath = f"{self.base_dir}/{state}"
    with open(filepath, "w") as f:
        content = str(time.time())
        f.write(content)
    return state
```

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

### Subclasses

* [AmazonS3OAuthStateStore](amazon_s3/index.html#slack_sdk.oauth.state_store.amazon_s3.AmazonS3OAuthStateStore "slack_sdk.oauth.state_store.amazon_s3.AmazonS3OAuthStateStore")
* [FileOAuthStateStore](file/index.html#slack_sdk.oauth.state_store.file.FileOAuthStateStore "slack_sdk.oauth.state_store.file.FileOAuthStateStore")
* [SQLAlchemyOAuthStateStore](sqlalchemy/index.html#slack_sdk.oauth.state_store.sqlalchemy.SQLAlchemyOAuthStateStore "slack_sdk.oauth.state_store.sqlalchemy.SQLAlchemyOAuthStateStore")
* [SQLite3OAuthStateStore](sqlite3/index.html#slack_sdk.oauth.state_store.sqlite3.SQLite3OAuthStateStore "slack_sdk.oauth.state_store.sqlite3.SQLite3OAuthStateStore")

### Instance variables (2)

`prop logger : logging.Logger`

Expand source code

```python
@property
def logger(self) -> Logger:
    raise NotImplementedError()
```

### Methods (2)

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
