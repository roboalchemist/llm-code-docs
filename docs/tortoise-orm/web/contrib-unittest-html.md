# Source: https://tortoise.github.io/contrib/unittest.html

Title: Testing Support - Tortoise ORM v1.1.6 Documentation

URL Source: https://tortoise.github.io/contrib/unittest.html

Markdown Content:
Tortoise ORM provides testing utilities designed for pytest with true test isolation. Each test gets its own database context, ensuring tests don’t interfere with each other.

*   [Quick Start](https://tortoise.github.io/contrib/unittest.html#quick-start)

*   [`tortoise_test_context` Reference](https://tortoise.github.io/contrib/unittest.html#tortoise-test-context-reference)

*   [Testing with Multiple Databases](https://tortoise.github.io/contrib/unittest.html#testing-with-multiple-databases)

*   [Event Loop Isolation](https://tortoise.github.io/contrib/unittest.html#event-loop-isolation)

*   [Unit Testing Without a Database](https://tortoise.github.io/contrib/unittest.html#unit-testing-without-a-database)

*   [Testing Database Capabilities](https://tortoise.github.io/contrib/unittest.html#testing-database-capabilities)

*   [Environment Variables](https://tortoise.github.io/contrib/unittest.html#environment-variables)

*   [Utility Functions](https://tortoise.github.io/contrib/unittest.html#utility-functions)

    *   [truncate_all_models](https://tortoise.github.io/contrib/unittest.html#truncate-all-models)

*   [Migration from Legacy Test Classes](https://tortoise.github.io/contrib/unittest.html#migration-from-legacy-test-classes)

*   [Reference](https://tortoise.github.io/contrib/unittest.html#module-tortoise.contrib.test)

[Quick Start](https://tortoise.github.io/contrib/unittest.html#id2)[¶](https://tortoise.github.io/contrib/unittest.html#quick-start "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------

1.   Create a `conftest.py` file in your tests directory:

```
import os
import pytest_asyncio
from tortoise.contrib.test import tortoise_test_context

@pytest_asyncio.fixture
async def db():
    """Provide isolated database context for each test."""
    db_url = os.getenv("TORTOISE_TEST_DB", "sqlite://:memory:")
    async with tortoise_test_context(["myapp.models"], db_url=db_url) as ctx:
        yield ctx
```

1.   Write your tests as async functions:

```
import pytest
from myapp.models import User

@pytest.mark.asyncio
async def test_create_user(db):
    user = await User.create(name="Test User", email="test@example.com")
    assert user.id is not None
    assert user.name == "Test User"

@pytest.mark.asyncio
async def test_filter_users(db):
    await User.create(name="Alice")
    await User.create(name="Bob")

    users = await User.filter(name="Alice")
    assert len(users) == 1
    assert users[0].name == "Alice"
```

1.   Run your tests:

```
pytest tests/ -v
```

[`tortoise_test_context` Reference](https://tortoise.github.io/contrib/unittest.html#id3)[¶](https://tortoise.github.io/contrib/unittest.html#tortoise-test-context-reference "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The `tortoise_test_context` function creates an isolated ORM context for testing:

```
from tortoise.contrib.test import tortoise_test_context

async with tortoise_test_context(
    modules=["myapp.models"],           # Required: List of model modules
    db_url="sqlite://:memory:",         # Optional: Database URL (default: sqlite://:memory:)
    app_label="models",                 # Optional: App label (default: "models")
    connection_label="default",         # Optional: Connection alias (default: "default")
) as ctx:
    # Your test code here
    pass
```

**Parameters:**

*   `modules` (list): List of module paths containing your models. Required.

*   `db_url` (str): Database connection URL. Defaults to `sqlite://:memory:`.

*   `app_label` (str): Label for the app in the ORM registry. Defaults to `"models"`.

*   `connection_label` (str): Alias for the database connection. Defaults to `"default"`.

The context manager:

1.   Creates a fresh `TortoiseContext`

2.   Initializes the ORM with the given configuration

3.   Generates database schemas

4.   Yields the context for your test

5.   Closes all connections on exit

[Testing with Multiple Databases](https://tortoise.github.io/contrib/unittest.html#id4)[¶](https://tortoise.github.io/contrib/unittest.html#testing-with-multiple-databases "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

For tests that require multiple database connections:

```
import pytest_asyncio
from tortoise.context import TortoiseContext

@pytest_asyncio.fixture
async def multi_db():
    """Fixture for testing with multiple databases."""
    async with TortoiseContext() as ctx:
        await ctx.init(config={
            "connections": {
                "primary": "sqlite://:memory:",
                "secondary": "sqlite://:memory:",
            },
            "apps": {
                "models": {
                    "models": ["myapp.models"],
                    "default_connection": "primary",
                },
                "archive": {
                    "models": ["myapp.archive_models"],
                    "default_connection": "secondary",
                }
            }
        })
        await ctx.generate_schemas()
        yield ctx
```

[Event Loop Isolation](https://tortoise.github.io/contrib/unittest.html#id5)[¶](https://tortoise.github.io/contrib/unittest.html#event-loop-isolation "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Some backends (asyncpg, aiomysql) bind connection pools to the event loop that created them. `tortoise_test_context()` handles this transparently – if the event loop changes between tests, connections are automatically recreated.

This means you **don’t** need `loop_scope="session"` or any special pytest-asyncio configuration. The simplest setup works:

```
# pyproject.toml -- no loop_scope overrides needed
[tool.pytest.ini_options]
asyncio_mode = "auto"
```

If you use `TortoiseContext` directly (without `tortoise_test_context`), you may see a `TortoiseLoopSwitchWarning` when the loop changes. Suppress it with:

```
import warnings
from tortoise.warnings import TortoiseLoopSwitchWarning
warnings.filterwarnings("ignore", category=TortoiseLoopSwitchWarning)
```

[Unit Testing Without a Database](https://tortoise.github.io/contrib/unittest.html#id6)[¶](https://tortoise.github.io/contrib/unittest.html#unit-testing-without-a-database "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

For testing pure business logic that reads model attributes and iterates relations without making queries, use `Model.construct()` to create model instances in memory:

```
from myapp.models import User, Organization, Membership

def test_user_has_active_membership():
    org = Organization.construct(id=1, name="Corp")
    membership = Membership.construct(
        organization=org,
        role="admin",
        is_active=True,
    )
    user = User.construct(
        id=1,
        email="test@example.com",
        memberships=[membership],
    )

    # Pure business logic -- no database needed
    active = [m for m in user.memberships if m.is_active]
    assert len(active) == 1
    assert active[0].role == "admin"
```

`construct()` creates “detached” instances that behave like ORM-loaded objects:

*   Reverse FK fields (e.g., `user.memberships`) accept lists and wrap them in `ReverseRelation`, so `len()`, `in`, iteration, and `bool()` all work.

*   M2M fields work the same way, wrapped in `ManyToManyRelation`.

*   FK fields populate the source field automatically (e.g., `event.tournament_id` is set from `tournament.pk`).

*   No validation is performed – null checks, type checks, and `_saved_in_db` guards are all skipped.

Note

`construct()` requires Tortoise to be initialized (via `tortoise_test_context` or `Tortoise.init()`) for relation fields to work, because relation metadata is resolved during initialization. For simple data-only fields, it works without initialization.

See [`tortoise.models.Model.construct()`](https://tortoise.github.io/models.html#tortoise.models.Model.construct "tortoise.models.Model.construct (Python method) — Create a model instance without validation, DB checks, or FK restrictions.") for the full API reference.

[Testing Database Capabilities](https://tortoise.github.io/contrib/unittest.html#id7)[¶](https://tortoise.github.io/contrib/unittest.html#testing-database-capabilities "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Use `requireCapability` to skip tests based on database capabilities:

```
from tortoise.contrib.test import requireCapability

@pytest.mark.asyncio
@requireCapability(dialect="postgres")
async def test_postgres_specific_feature(db):
    """This test only runs on PostgreSQL."""
    # Test postgres-specific functionality
    pass

@pytest.mark.asyncio
@requireCapability(dialect="sqlite")
async def test_sqlite_specific_feature(db):
    """This test only runs on SQLite."""
    pass
```

[Environment Variables](https://tortoise.github.io/contrib/unittest.html#id8)[¶](https://tortoise.github.io/contrib/unittest.html#environment-variables "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Configure your test database via environment variables:

```
# SQLite (default)
export TORTOISE_TEST_DB="sqlite://:memory:"

# PostgreSQL
export TORTOISE_TEST_DB="postgres://user:pass@localhost:5432/testdb"

# MySQL
export TORTOISE_TEST_DB="mysql://user:pass@localhost:3306/testdb"
```

Using `{}` in the URL creates randomized database names (useful for parallel testing):

```
export TORTOISE_TEST_DB="sqlite:///tmp/test-{}.sqlite"
export TORTOISE_TEST_DB="postgres://user:pass@localhost:5432/test_{}"
```

[Utility Functions](https://tortoise.github.io/contrib/unittest.html#id9)[¶](https://tortoise.github.io/contrib/unittest.html#utility-functions "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [truncate_all_models](https://tortoise.github.io/contrib/unittest.html#id10)[¶](https://tortoise.github.io/contrib/unittest.html#truncate-all-models "Link to this heading")

Truncate all model tables in the current context. The function handles foreign key constraints automatically:

*   **PostgreSQL**: Uses a single `TRUNCATE ... CASCADE` statement (fast, single round-trip).

*   **Other databases**: Deletes in topological order — child tables are emptied before the parent tables they reference, avoiding FK constraint violations.

```
from tortoise.contrib.test import truncate_all_models

@pytest.mark.asyncio
async def test_with_truncation(db):
    # Create some data
    await User.create(name="Test")

    # Truncate all tables (FK-safe)
    await truncate_all_models()

    # Tables are now empty
    count = await User.all().count()
    assert count == 0
```

[Migration from Legacy Test Classes](https://tortoise.github.io/contrib/unittest.html#id11)[¶](https://tortoise.github.io/contrib/unittest.html#migration-from-legacy-test-classes "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

If you’re upgrading from the legacy `test.TestCase` classes, see the [Migration Guide: Tortoise 1.0](https://tortoise.github.io/migration_guide.html#migration-guide) for detailed migration instructions.

**Quick reference:**

Migration Mapping[¶](https://tortoise.github.io/contrib/unittest.html#id1 "Link to this table")| Legacy (Removed) | Modern Replacement |
| --- | --- |
| `test.TestCase` | pytest + `db` fixture |
| `test.IsolatedTestCase` | pytest + `db` fixture (isolation is default) |
| `test.TruncationTestCase` | pytest + `db` fixture + `truncate_all_models()` |
| `test.SimpleTestCase` | pytest + `db` fixture |
| `initializer()` | `tortoise_test_context()` |
| `finalizer()` | (automatic with context manager) |
| `self.assertEqual(a, b)` | `assert a == b` |
| `self.assertIn(a, b)` | `assert a in b` |
| `self.assertRaises(Exc)` | `pytest.raises(Exc)` |

[Reference](https://tortoise.github.io/contrib/unittest.html#id12)[¶](https://tortoise.github.io/contrib/unittest.html#module-tortoise.contrib.test "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Modern testing utilities for Tortoise ORM.

Use tortoise_test_context() with pytest fixtures:

> @pytest_asyncio.fixture async def db():
> 
> 
> > async with tortoise_test_context([“myapp.models”]) as ctx:
> > yield ctx
> 
> 
> @pytest.mark.asyncio async def test_example(db):
> 
> 
> > user = await User.create(name=”Test”) assert user.id is not None

For capability-based test skipping:

> @requireCapability(dialect=”sqlite”) @pytest.mark.asyncio async def test_sqlite_only(db):
> 
> 
> > # This test only runs on SQLite …

tortoise.contrib.test.requireCapability(_[connection\_name](https://tortoise.github.io/contrib/unittest.html#tortoise.contrib.test.requireCapability.connection\_name "tortoise.contrib.test.requireCapability.connection\_name (Python parameter) — name of the connection to retrieve capabilities from.")=`'models'`_, _**[conditions](https://tortoise.github.io/contrib/unittest.html#tortoise.contrib.test.requireCapability.conditions "tortoise.contrib.test.requireCapability.conditions (Python parameter) — capability tests which must all pass for the test to run.")_)[[source]](https://tortoise.github.io/_modules/tortoise/contrib/test.html#requireCapability)[¶](https://tortoise.github.io/contrib/unittest.html#tortoise.contrib.test.requireCapability "Link to this definition")
Skip a test if the required capabilities are not matched.

Note

The database must be initialized _before_ the decorated test runs.

Usage:

```
@requireCapability(dialect='sqlite')
@pytest.mark.asyncio
async def test_run_sqlite_only(db):
    ...
```

Or to conditionally skip a class:

```
@requireCapability(dialect='sqlite')
class TestSqlite:
    @pytest.mark.asyncio
    async def test_something(self, db):
        ...
```

Parameters:[¶](https://tortoise.github.io/contrib/unittest.html#tortoise.contrib.test.requireCapability-parameters "Permalink to this headline")connection_name=`'models'`[¶](https://tortoise.github.io/contrib/unittest.html#tortoise.contrib.test.requireCapability.connection_name "Permalink to this definition")
name of the connection to retrieve capabilities from.

**conditions[¶](https://tortoise.github.io/contrib/unittest.html#tortoise.contrib.test.requireCapability.conditions "Permalink to this definition")
capability tests which must all pass for the test to run.

Return type:[¶](https://tortoise.github.io/contrib/unittest.html#tortoise.contrib.test.requireCapability-return-type "Permalink to this headline")
`Callable`

tortoise.contrib.test.tortoise_test_context(_[modules](https://tortoise.github.io/contrib/unittest.html#tortoise.contrib.test.tortoise\_test\_context "tortoise.contrib.test.tortoise\_test\_context.modules (Python parameter)")_, _[db\_url](https://tortoise.github.io/contrib/unittest.html#tortoise.contrib.test.tortoise\_test\_context "tortoise.contrib.test.tortoise\_test\_context.db\_url (Python parameter)")=`'sqlite://:memory:'`_, _[app\_label](https://tortoise.github.io/contrib/unittest.html#tortoise.contrib.test.tortoise\_test\_context "tortoise.contrib.test.tortoise\_test\_context.app\_label (Python parameter)")=`'models'`_, _*_, _[connection\_label](https://tortoise.github.io/contrib/unittest.html#tortoise.contrib.test.tortoise\_test\_context "tortoise.contrib.test.tortoise\_test\_context.connection\_label (Python parameter)")=`None`_, _[use\_tz](https://tortoise.github.io/contrib/unittest.html#tortoise.contrib.test.tortoise\_test\_context "tortoise.contrib.test.tortoise\_test\_context.use\_tz (Python parameter)")=`True`_, _[timezone](https://tortoise.github.io/contrib/unittest.html#tortoise.contrib.test.tortoise\_test\_context "tortoise.contrib.test.tortoise\_test\_context.timezone (Python parameter)")=`'UTC'`_, _[routers](https://tortoise.github.io/contrib/unittest.html#tortoise.contrib.test.tortoise\_test\_context "tortoise.contrib.test.tortoise\_test\_context.routers (Python parameter)")=`None`_)[[source]](https://tortoise.github.io/_modules/tortoise/context.html#tortoise_test_context)[¶](https://tortoise.github.io/contrib/unittest.html#tortoise.contrib.test.tortoise_test_context "Link to this definition")
Async context manager for isolated test database setup.

This is the recommended way to set up Tortoise ORM for testing with pytest. Each call creates a completely isolated context with its own: - ConnectionHandler (no global state pollution) - Apps registry - Database (created fresh, cleaned up on exit) - Timezone and router configuration

Example with pytest-asyncio:
@pytest_asyncio.fixture async def db():

> async with tortoise_test_context([“myapp.models”]) as ctx:
> yield ctx

@pytest.mark.asyncio async def test_create_user(db):

> user = await User.create(name=”Alice”) assert user.id is not None

Features: - Creates isolated TortoiseContext (no global state pollution) - Creates fresh database and generates schemas - Cleans up connections on exit - xdist-safe (each worker gets own context)

Args:
modules: List of module paths to discover models from. db_url: Database URL, defaults to in-memory SQLite. app_label: The app label for the models, defaults to “models”. connection_label: The connection alias name. If None, defaults to “default”. use_tz: If True, datetime fields will be timezone-aware. timezone: Timezone to use, defaults to “UTC”. routers: List of database router paths or classes.

Yields:
An initialized TortoiseContext ready for use.

Return type:[¶](https://tortoise.github.io/contrib/unittest.html#tortoise.contrib.test.tortoise_test_context-return-type "Permalink to this headline")
`AsyncIterator`

_async_ tortoise.contrib.test.truncate_all_models()[[source]](https://tortoise.github.io/_modules/tortoise/contrib/test.html#truncate_all_models)[¶](https://tortoise.github.io/contrib/unittest.html#tortoise.contrib.test.truncate_all_models "Link to this definition")
Truncate all models in the current context.

This is a utility function for test cleanup that deletes all rows from all registered model tables.

On PostgreSQL, uses `TRUNCATE ... CASCADE` for a single fast statement. On other databases, deletes in topological (FK dependency) order so that child rows are removed before parent rows they reference.

Raises:
ValueError: If Tortoise.apps is not loaded.

Return type:[¶](https://tortoise.github.io/contrib/unittest.html#tortoise.contrib.test.truncate_all_models-return-type "Permalink to this headline")
`None`
