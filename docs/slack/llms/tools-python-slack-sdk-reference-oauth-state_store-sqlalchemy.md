Source: https://docs.slack.dev/tools/python-slack-sdk/reference/oauth/state_store/sqlalchemy

# Module slack_sdk.oauth.state_store.sqlalchemy

## Classes

`class AsyncSQLAlchemyOAuthStateStore (expiration_seconds: int,   engine: sqlalchemy.ext.asyncio.engine.AsyncEngine,   logger: logging.Logger = <Logger slack_sdk.oauth.state_store.sqlalchemy (WARNING)>,   table_name: str = 'slack_oauth_states')`

Expand source code

```typescript
class AsyncSQLAlchemyOAuthStateStore(AsyncOAuthStateStore):
    default_table_name: str = "slack_oauth_states"

    expiration_seconds: int
    engine: AsyncEngine
    metadata: MetaData
    oauth_states: Table

    @classmethod
    def build_oauth_states_table(cls, metadata: MetaData, table_name: str) -> Table:
        return sqlalchemy.Table(
            table_name,
            metadata,
            metadata,
            Column("id", Integer, primary_key=True, autoincrement=True),
            Column("state", String(200), nullable=False),
            Column("expire_at", DateTime, nullable=False),
        )

    def __init__(
        self,
        expiration_seconds: int,
        engine: AsyncEngine,
        logger: Logger = logging.getLogger(__name__),
        table_name: str = default_table_name,
    ):
        self.expiration_seconds = expiration_seconds
        self._logger = logger
        self.engine = engine
        self.metadata = MetaData()
        self.oauth_states = self.build_oauth_states_table(self.metadata, table_name)

    async def create_tables(self):
        async with self.engine.begin() as conn:
            await conn.run_sync(self.metadata.create_all)

    @property
    def logger(self) -> Logger:
        if self._logger is None:
            self._logger = logging.getLogger(__name__)
        return self._logger

    async def async_issue(self, *args, **kwargs) -> str:
        state: str = str(uuid4())
        now = normalize_datetime_for_db(datetime.fromtimestamp(time.time() + self.expiration_seconds, tz=timezone.utc))
        async with self.engine.begin() as conn:
            await conn.execute(
                self.oauth_states.insert(),
                {"state": state, "expire_at": now},
            )
        return state

    async def async_consume(self, state: str) -> bool:
        try:
            now = normalize_datetime_for_db(datetime.now(tz=timezone.utc))
            async with self.engine.begin() as conn:
                c = self.oauth_states.c
                query = self.oauth_states.select().where(and_(c.state == state, c.expire_at > now))
                result = await conn.execute(query)
                for row in result.mappings():
                    self.logger.debug(f"consume's query result: {row}")
                    await conn.execute(self.oauth_states.delete().where(c.id == row["id"]))
                    return True
            return False
        except Exception as e:
            message = f"Failed to find any persistent data for state: {state} - {e}"
            self.logger.warning(message)
            return False
```

### Ancestors

* [AsyncOAuthStateStore](../async_state_store.html#slack_sdk.oauth.state_store.async_state_store.AsyncOAuthStateStore "slack_sdk.oauth.state_store.async_state_store.AsyncOAuthStateStore")

### Class variables

`var default_table_name : str`

The type of the None singleton.

`var engine : sqlalchemy.ext.asyncio.engine.AsyncEngine`

The type of the None singleton.

`var expiration_seconds : int`

The type of the None singleton.

`var metadata : sqlalchemy.sql.schema.MetaData`

The type of the None singleton.

`var oauth_states : sqlalchemy.sql.schema.Table`

The type of the None singleton.

### Static methods

`def build_oauth_states_table(metadata: sqlalchemy.sql.schema.MetaData, table_name: str) ‑> sqlalchemy.sql.schema.Table`

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
    try:
        now = normalize_datetime_for_db(datetime.now(tz=timezone.utc))
        async with self.engine.begin() as conn:
            c = self.oauth_states.c
            query = self.oauth_states.select().where(and_(c.state == state, c.expire_at > now))
            result = await conn.execute(query)
            for row in result.mappings():
                self.logger.debug(f"consume's query result: {row}")
                await conn.execute(self.oauth_states.delete().where(c.id == row["id"]))
                return True
        return False
    except Exception as e:
        message = f"Failed to find any persistent data for state: {state} - {e}"
        self.logger.warning(message)
        return False
```

`async def async_issue(self, *args, **kwargs) ‑> str`

Expand source code

```python
async def async_issue(self, *args, **kwargs) -> str:
    state: str = str(uuid4())
    now = normalize_datetime_for_db(datetime.fromtimestamp(time.time() + self.expiration_seconds, tz=timezone.utc))
    async with self.engine.begin() as conn:
        await conn.execute(
            self.oauth_states.insert(),
            {"state": state, "expire_at": now},
        )
    return state
```

`async def create_tables(self)`

Expand source code

```python
async def create_tables(self):
    async with self.engine.begin() as conn:
        await conn.run_sync(self.metadata.create_all)
```

`class SQLAlchemyOAuthStateStore (expiration_seconds: int,   engine: sqlalchemy.engine.base.Engine,   logger: logging.Logger = <Logger slack_sdk.oauth.state_store.sqlalchemy (WARNING)>,   table_name: str = 'slack_oauth_states')`

Expand source code

```typescript
class SQLAlchemyOAuthStateStore(OAuthStateStore):
    default_table_name: str = "slack_oauth_states"

    expiration_seconds: int
    engine: Engine
    metadata: MetaData
    oauth_states: Table

    @classmethod
    def build_oauth_states_table(cls, metadata: MetaData, table_name: str) -> Table:
        return sqlalchemy.Table(
            table_name,
            metadata,
            metadata,
            Column("id", Integer, primary_key=True, autoincrement=True),
            Column("state", String(200), nullable=False),
            Column("expire_at", DateTime, nullable=False),
        )

    def __init__(
        self,
        expiration_seconds: int,
        engine: Engine,
        logger: Logger = logging.getLogger(__name__),
        table_name: str = default_table_name,
    ):
        self.expiration_seconds = expiration_seconds
        self._logger = logger
        self.engine = engine
        self.metadata = MetaData()
        self.oauth_states = self.build_oauth_states_table(self.metadata, table_name)

    def create_tables(self):
        self.metadata.create_all(self.engine)

    @property
    def logger(self) -> Logger:
        if self._logger is None:
            self._logger = logging.getLogger(__name__)
        return self._logger

    def issue(self, *args, **kwargs) -> str:
        state: str = str(uuid4())
        now = normalize_datetime_for_db(datetime.fromtimestamp(time.time() + self.expiration_seconds, tz=timezone.utc))
        with self.engine.begin() as conn:
            conn.execute(
                self.oauth_states.insert(),
                {"state": state, "expire_at": now},
            )
        return state

    def consume(self, state: str) -> bool:
        try:
            now = normalize_datetime_for_db(datetime.now(tz=timezone.utc))
            with self.engine.begin() as conn:
                c = self.oauth_states.c
                query = self.oauth_states.select().where(and_(c.state == state, c.expire_at > now))
                result = conn.execute(query)
                for row in result.mappings():
                    self.logger.debug(f"consume's query result: {row}")
                    conn.execute(self.oauth_states.delete().where(c.id == row["id"]))
                    return True
            return False
        except Exception as e:
            message = f"Failed to find any persistent data for state: {state} - {e}"
            self.logger.warning(message)
            return False
```

### Ancestors (2)

* [OAuthStateStore](../state_store.html#slack_sdk.oauth.state_store.state_store.OAuthStateStore "slack_sdk.oauth.state_store.state_store.OAuthStateStore")

### Class variables (2)

`var default_table_name : str`

The type of the None singleton.

`var engine : sqlalchemy.engine.base.Engine`

The type of the None singleton.

`var expiration_seconds : int`

The type of the None singleton.

`var metadata : sqlalchemy.sql.schema.MetaData`

The type of the None singleton.

`var oauth_states : sqlalchemy.sql.schema.Table`

The type of the None singleton.

### Static methods (2)

`def build_oauth_states_table(metadata: sqlalchemy.sql.schema.MetaData, table_name: str) ‑> sqlalchemy.sql.schema.Table`

### Instance variables (2)

`prop logger : logging.Logger`

Expand source code

```python
@property
def logger(self) -> Logger:
    if self._logger is None:
        self._logger = logging.getLogger(__name__)
    return self._logger
```

### Methods (2)

`def consume(self, state: str) ‑> bool`

Expand source code

```python
def consume(self, state: str) -> bool:
    try:
        now = normalize_datetime_for_db(datetime.now(tz=timezone.utc))
        with self.engine.begin() as conn:
            c = self.oauth_states.c
            query = self.oauth_states.select().where(and_(c.state == state, c.expire_at > now))
            result = conn.execute(query)
            for row in result.mappings():
                self.logger.debug(f"consume's query result: {row}")
                conn.execute(self.oauth_states.delete().where(c.id == row["id"]))
                return True
        return False
    except Exception as e:
        message = f"Failed to find any persistent data for state: {state} - {e}"
        self.logger.warning(message)
        return False
```

`def create_tables(self)`

Expand source code

```python
def create_tables(self):
    self.metadata.create_all(self.engine)
```

`def issue(self, *args, **kwargs) ‑> str`

Expand source code

```python
def issue(self, *args, **kwargs) -> str:
    state: str = str(uuid4())
    now = normalize_datetime_for_db(datetime.fromtimestamp(time.time() + self.expiration_seconds, tz=timezone.utc))
    with self.engine.begin() as conn:
        conn.execute(
            self.oauth_states.insert(),
            {"state": state, "expire_at": now},
        )
    return state
```
