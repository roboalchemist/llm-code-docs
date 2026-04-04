# Source: https://tortoise.github.io/migration_guide.html

Title: Migration Guide: Tortoise 1.0 - Tortoise ORM v1.1.6 Documentation

URL Source: https://tortoise.github.io/migration_guide.html

Markdown Content:
This guide covers the breaking changes and migration steps for upgrading to Tortoise ORM 1.0+ which introduces a isolated-context architecture for improved test isolation and cleaner state management.

*   [Overview](https://tortoise.github.io/migration_guide.html#overview)

*   [Quick Reference](https://tortoise.github.io/migration_guide.html#quick-reference)

*   [What Stays the Same](https://tortoise.github.io/migration_guide.html#what-stays-the-same)

*   [Connection Access Changes](https://tortoise.github.io/migration_guide.html#connection-access-changes)

    *   [Old Pattern (Deprecated)](https://tortoise.github.io/migration_guide.html#old-pattern-deprecated)

    *   [New Pattern](https://tortoise.github.io/migration_guide.html#new-pattern)

*   [Test Migration](https://tortoise.github.io/migration_guide.html#test-migration)

    *   [Old Test Pattern](https://tortoise.github.io/migration_guide.html#old-test-pattern)

    *   [New Test Pattern](https://tortoise.github.io/migration_guide.html#new-test-pattern)

    *   [Migration Checklist](https://tortoise.github.io/migration_guide.html#migration-checklist)

*   [Multiple `asyncio.run()` Calls (Uncommon Pattern)](https://tortoise.github.io/migration_guide.html#multiple-asyncio-run-calls-uncommon-pattern)

    *   [Old Pattern (No Longer Works)](https://tortoise.github.io/migration_guide.html#old-pattern-no-longer-works)

    *   [New Patterns](https://tortoise.github.io/migration_guide.html#new-patterns)

*   [Using `TortoiseContext` Directly](https://tortoise.github.io/migration_guide.html#using-tortoisecontext-directly)

*   [Framework Integration Changes](https://tortoise.github.io/migration_guide.html#framework-integration-changes)

    *   [Multiple FastAPI Apps (Global Fallback)](https://tortoise.github.io/migration_guide.html#multiple-fastapi-apps-global-fallback)

    *   [Custom Integration Migration](https://tortoise.github.io/migration_guide.html#custom-integration-migration)

*   [Removed APIs](https://tortoise.github.io/migration_guide.html#removed-apis)

*   [Deprecated APIs](https://tortoise.github.io/migration_guide.html#deprecated-apis)

*   [Still Available](https://tortoise.github.io/migration_guide.html#still-available)

*   [Troubleshooting](https://tortoise.github.io/migration_guide.html#troubleshooting)

    *   [“No TortoiseContext is currently active”](https://tortoise.github.io/migration_guide.html#no-tortoisecontext-is-currently-active)

    *   [“Global context fallback is already enabled”](https://tortoise.github.io/migration_guide.html#global-context-fallback-is-already-enabled)

    *   [“ConfigurationError: Connections not initialized”](https://tortoise.github.io/migration_guide.html#configurationerror-connections-not-initialized)

    *   [Test isolation issues](https://tortoise.github.io/migration_guide.html#test-isolation-issues)

*   [Getting Help](https://tortoise.github.io/migration_guide.html#getting-help)

[Overview](https://tortoise.github.io/migration_guide.html#id2)[¶](https://tortoise.github.io/migration_guide.html#overview "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------

Tortoise ORM 1.0 introduces a **isolated-context architecture** that:

*   Removes global state (`_default_context`, metaclass)

*   Uses `TortoiseContext` as the single source of truth

*   Provides test isolation with `tortoise_test_context()`

*   Simplifies connection management

Most application code continues to work unchanged. The main changes affect:

1.   Direct access to the `connections` singleton

2.   Test infrastructure (`test.TestCase`, `initializer`, etc.)

3.   Multiple `asyncio.run()` call patterns

[Quick Reference](https://tortoise.github.io/migration_guide.html#id3)[¶](https://tortoise.github.io/migration_guide.html#quick-reference "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------

API Changes[¶](https://tortoise.github.io/migration_guide.html#id1 "Link to this table")| Old Pattern | New Pattern |
| --- | --- |
| `from tortoise import connections` (deprecated) | `from tortoise.connection import get_connection, get_connections` |
| `connections.get("default")` (still works) | `Tortoise.get_connection("default")` or `get_connection("default")` |
| `connections.close_all()` (still works) | `Tortoise.close_connections()` |
| `test.TestCase` (removed) | pytest + `db` fixture |
| `initializer()` / `finalizer()` (removed) | `tortoise_test_context()` |

[What Stays the Same](https://tortoise.github.io/migration_guide.html#id4)[¶](https://tortoise.github.io/migration_guide.html#what-stays-the-same "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The following APIs continue to work unchanged:

```
# Initialization (unchanged)
await Tortoise.init(config=...)
await Tortoise.init(db_url="...", modules={...})
await Tortoise.generate_schemas()

# Accessing apps (unchanged)
Tortoise.apps
Tortoise._inited

# Model operations (unchanged)
await User.create(name="test")
await User.filter(name="test").first()

# Framework integrations (unchanged for users)
# FastAPI, Starlette, Sanic, etc.
```

[Connection Access Changes](https://tortoise.github.io/migration_guide.html#id5)[¶](https://tortoise.github.io/migration_guide.html#connection-access-changes "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [Old Pattern (Deprecated)](https://tortoise.github.io/migration_guide.html#id6)[¶](https://tortoise.github.io/migration_guide.html#old-pattern-deprecated "Link to this heading")

```
from tortoise import connections

conn = connections.get("default")
await connections.close_all()
```

### [New Pattern](https://tortoise.github.io/migration_guide.html#id7)[¶](https://tortoise.github.io/migration_guide.html#new-pattern "Link to this heading")

```
from tortoise import Tortoise
# Or: from tortoise.connection import get_connection, get_connections

# Get a single connection
conn = Tortoise.get_connection("default")

# Get the connection handler
handler = get_connections()
all_conns = handler.all()

# Close all connections
await Tortoise.close_connections()
```

[Test Migration](https://tortoise.github.io/migration_guide.html#id8)[¶](https://tortoise.github.io/migration_guide.html#test-migration "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------------------

The legacy test base classes (`TestCase`, `IsolatedTestCase`, etc.) and helper functions (`initializer`, `finalizer`) have been replaced with a pytest-based approach using `tortoise_test_context()`.

### [Old Test Pattern](https://tortoise.github.io/migration_guide.html#id9)[¶](https://tortoise.github.io/migration_guide.html#old-test-pattern "Link to this heading")

```
from tortoise.contrib import test

class TestUser(test.TestCase):
    async def test_create(self):
        user = await User.create(name="Test")
        self.assertEqual(user.name, "Test")

    async def test_filter(self):
        await User.create(name="Test")
        users = await User.filter(name="Test")
        self.assertEqual(len(users), 1)
```

With `conftest.py`:

```
from tortoise.contrib.test import initializer, finalizer

@pytest.fixture(scope="session", autouse=True)
def initialize_tests(request):
    initializer(["myapp.models"])
    request.addfinalizer(finalizer)
```

### [New Test Pattern](https://tortoise.github.io/migration_guide.html#id10)[¶](https://tortoise.github.io/migration_guide.html#new-test-pattern "Link to this heading")

```
import pytest
from tests.testmodels import User

@pytest.mark.asyncio
async def test_create(db):
    user = await User.create(name="Test")
    assert user.name == "Test"

@pytest.mark.asyncio
async def test_filter(db):
    await User.create(name="Test")
    users = await User.filter(name="Test")
    assert len(users) == 1
```

With `conftest.py`:

```
import pytest_asyncio
from tortoise.contrib.test import tortoise_test_context

@pytest_asyncio.fixture
async def db():
    async with tortoise_test_context(["myapp.models"]) as ctx:
        yield ctx
```

### [Migration Checklist](https://tortoise.github.io/migration_guide.html#id11)[¶](https://tortoise.github.io/migration_guide.html#migration-checklist "Link to this heading")

For each test file:

1.   Replace `from tortoise.contrib import test` with `import pytest`

2.   Remove class wrapper (`class TestXxx(test.TestCase):`)

3.   Add `@pytest.mark.asyncio` decorator to each async test

4.   Add `db` fixture parameter to each test function

5.   Replace assertion methods: - `self.assertEqual(a, b)` → `assert a == b` - `self.assertIn(a, b)` → `assert a in b` - `self.assertRaises(Exc)` → `pytest.raises(Exc)` - `self.assertTrue(x)` → `assert x` - `self.assertFalse(x)` → `assert not x`

[Multiple `asyncio.run()` Calls (Uncommon Pattern)](https://tortoise.github.io/migration_guide.html#id12)[¶](https://tortoise.github.io/migration_guide.html#multiple-asyncio-run-calls-uncommon-pattern "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Note

This section only applies if you use multiple **separate**`asyncio.run()` calls in sequence. The typical pattern of a single `asyncio.run(main())` that contains all ORM operations continues to work unchanged.

If you use multiple separate `asyncio.run()` calls (sometimes seen in scripts or REPL sessions), the ContextVar that tracks ORM state is lost between runs due to Python’s ContextVar scoping rules. This pattern now requires explicit context management.

As a fallback _enable_global_fallback on Tortoise.init(…) can be used to set created context as global fallback.

### [Old Pattern (No Longer Works)](https://tortoise.github.io/migration_guide.html#id13)[¶](https://tortoise.github.io/migration_guide.html#old-pattern-no-longer-works "Link to this heading")

```
import asyncio
from tortoise import Tortoise

# Context is lost after asyncio.run() completes
asyncio.run(Tortoise.init(db_url="sqlite://:memory:", modules={"models": ["__main__"]}))
asyncio.run(User.create(name="test"))  # FAILS: No context
```

### [New Patterns](https://tortoise.github.io/migration_guide.html#id14)[¶](https://tortoise.github.io/migration_guide.html#new-patterns "Link to this heading")

**Option 1: Single asyncio.run (Recommended)**

```
import asyncio
from tortoise import Tortoise

async def main():
    await Tortoise.init(db_url="sqlite://:memory:", modules={"models": ["__main__"]})
    await Tortoise.generate_schemas()
    user = await User.create(name="test")
    print(f"Created user: {user.id}")
    await Tortoise.close_connections()

asyncio.run(main())
```

**Option 2: Capture and Reuse Context**

```
import asyncio
from tortoise import Tortoise

# Tortoise.init() returns the context
ctx = asyncio.run(Tortoise.init(db_url="sqlite://:memory:", modules={"models": ["__main__"]}))

# Re-enter context for subsequent runs
with ctx:
    asyncio.run(Tortoise.generate_schemas())
    asyncio.run(User.create(name="test"))
```

**Option 3: Explicit Context Manager**

```
import asyncio
from tortoise.context import TortoiseContext

with TortoiseContext() as ctx:
    asyncio.run(ctx.init(db_url="sqlite://:memory:", modules={"models": ["__main__"]}))
    asyncio.run(ctx.generate_schemas())
    asyncio.run(User.create(name="test"))
```

[Using `TortoiseContext` Directly](https://tortoise.github.io/migration_guide.html#id15)[¶](https://tortoise.github.io/migration_guide.html#using-tortoisecontext-directly "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

For advanced use cases (testing, multi-tenant applications), you can use `TortoiseContext` directly:

```
from tortoise.context import TortoiseContext

async def run_isolated():
    async with TortoiseContext() as ctx:
        await ctx.init(
            db_url="sqlite://:memory:",
            modules={"models": ["myapp.models"]}
        )
        await ctx.generate_schemas()

        # All ORM operations use this context
        user = await User.create(name="test")

        # Context auto-closes on exit
```

Benefits of `TortoiseContext`:

*   **Test isolation**: Each context has independent connections and state

*   **Multi-tenancy**: Different contexts can connect to different databases

*   **No global state**: Clear ownership of ORM state

*   **Automatic cleanup**: Connections close when context exits

[Framework Integration Changes](https://tortoise.github.io/migration_guide.html#id16)[¶](https://tortoise.github.io/migration_guide.html#framework-integration-changes "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

If you use the built-in framework integrations (FastAPI, Starlette, etc.), no changes are required. The integrations have been updated internally to use `Tortoise.close_connections()` instead of `connections.close_all()`.

### [Multiple FastAPI Apps (Global Fallback)](https://tortoise.github.io/migration_guide.html#id17)[¶](https://tortoise.github.io/migration_guide.html#multiple-fastapi-apps-global-fallback "Link to this heading")

When using `RegisterTortoise` with FastAPI, a global fallback context is enabled by default. This allows Tortoise ORM to work correctly with `asgi-lifespan` (used in tests) where the lifespan runs in a separate background task from the requests.

If you run **multiple FastAPI apps** in the same process (e.g., in tests), you may encounter:

```
ConfigurationError: Global context fallback is already enabled by another Tortoise.init() call.
```

**Solution:** Disable global fallback for secondary apps and use explicit context access:

```
# main_app.py - Primary app (uses global fallback)
from tortoise.contrib.fastapi import RegisterTortoise

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with RegisterTortoise(
        app,
        db_url="sqlite://:memory:",
        modules={"models": ["myapp.models"]},
    ):
        yield

app = FastAPI(lifespan=lifespan)
```

```
# secondary_app.py - Secondary app (explicit context)
from tortoise.contrib.fastapi import RegisterTortoise

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with RegisterTortoise(
        app,
        db_url="sqlite://:memory:",
        modules={"models": ["myapp.models"]},
        _enable_global_fallback=False,  # Disable global fallback
    ):
        yield

app_secondary = FastAPI(lifespan=lifespan)
```

In tests, access the secondary app’s context explicitly via `app.state`:

```
@pytest.fixture
async def client_secondary():
    async with LifespanManager(app_secondary) as manager:
        # Get context from app.state and enter it
        ctx = app_secondary.state._tortoise_context
        with ctx:  # Make context current via contextvar
            async with AsyncClient(app=app_secondary) as c:
                yield c
```

The `_enable_global_fallback` parameter:

*   `True` (default): Sets context as global fallback for cross-task access

*   `False`: Context only accessible via `app.state._tortoise_context`

This is also available in `Tortoise.init()` (default `False`) and `TortoiseContext.init()` (default `False`).

### [Custom Integration Migration](https://tortoise.github.io/migration_guide.html#id18)[¶](https://tortoise.github.io/migration_guide.html#custom-integration-migration "Link to this heading")

If you’ve written custom framework integrations:

```
# Old
from tortoise import connections

async def shutdown():
    await connections.close_all()

# New
from tortoise import Tortoise

async def shutdown():
    await Tortoise.close_connections()
```

[Removed APIs](https://tortoise.github.io/migration_guide.html#id19)[¶](https://tortoise.github.io/migration_guide.html#removed-apis "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------------------

The following APIs have been removed:

*   `test.TestCase`, `test.IsolatedTestCase`, `test.TruncationTestCase`

*   `test.SimpleTestCase`

*   `test.initializer()`, `test.finalizer()`

*   `test.env_initializer()`

*   `test.getDBConfig()`

[Deprecated APIs](https://tortoise.github.io/migration_guide.html#id20)[¶](https://tortoise.github.io/migration_guide.html#deprecated-apis "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------------------------

The following APIs still work but are deprecated:

*   `from tortoise import connections` - use `get_connection()` / `get_connections()` instead

[Still Available](https://tortoise.github.io/migration_guide.html#id21)[¶](https://tortoise.github.io/migration_guide.html#still-available "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------------------------

The following APIs are still available and work as before:

*   `init_memory_sqlite()` decorator - for simple scripts

*   `MEMORY_SQLITE` constant - `"sqlite://:memory:"`

*   `requireCapability()` - for capability-based test skipping

*   `truncate_all_models()` - for test cleanup

[Troubleshooting](https://tortoise.github.io/migration_guide.html#id22)[¶](https://tortoise.github.io/migration_guide.html#troubleshooting "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [“No TortoiseContext is currently active”](https://tortoise.github.io/migration_guide.html#id23)[¶](https://tortoise.github.io/migration_guide.html#no-tortoisecontext-is-currently-active "Link to this heading")

This error occurs when trying to access ORM features without an active context.

**Solutions:**

1.   Ensure `Tortoise.init()` was called before accessing models

2.   If using multiple `asyncio.run()` calls, use context manager pattern

3.   In tests, ensure the `db` fixture is being used

### [“Global context fallback is already enabled”](https://tortoise.github.io/migration_guide.html#id24)[¶](https://tortoise.github.io/migration_guide.html#global-context-fallback-is-already-enabled "Link to this heading")

This error occurs when multiple `Tortoise.init()` or `RegisterTortoise` calls try to enable global fallback simultaneously.

**Solutions:**

1.   For multiple FastAPI apps, set `_enable_global_fallback=False` on secondary apps

2.   Access secondary app’s context explicitly via `app.state._tortoise_context`

3.   See “Multiple FastAPI Apps (Global Fallback)” section above

### [“ConfigurationError: Connections not initialized”](https://tortoise.github.io/migration_guide.html#id25)[¶](https://tortoise.github.io/migration_guide.html#configurationerror-connections-not-initialized "Link to this heading")

This error occurs when trying to access connections before initialization.

**Solution:** Ensure `Tortoise.init()` or `ctx.init()` has been called and awaited.

### [Test isolation issues](https://tortoise.github.io/migration_guide.html#id26)[¶](https://tortoise.github.io/migration_guide.html#test-isolation-issues "Link to this heading")

If tests are interfering with each other:

1.   Ensure using function-scoped `db` fixture (not session-scoped)

2.   Use `tortoise_test_context()` which provides explicit isolation

3.   Remove any `@pytest.fixture(scope="session")` that calls `initializer()`

[Getting Help](https://tortoise.github.io/migration_guide.html#id27)[¶](https://tortoise.github.io/migration_guide.html#getting-help "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------------------

If you encounter issues during migration:

1.   Check the [GitHub Issues](https://github.com/tortoise/tortoise-orm/issues)

2.   Review the [examples directory](https://github.com/tortoise/tortoise-orm/tree/develop/examples)

3.   Ask in the [GitHub Discussions](https://github.com/tortoise/tortoise-orm/discussions)
