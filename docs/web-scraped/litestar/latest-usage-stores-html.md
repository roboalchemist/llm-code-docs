# Source: https://docs.litestar.dev/latest/usage/stores.html

Title: Stores — Litestar Framework

URL Source: https://docs.litestar.dev/latest/usage/stores.html

Markdown Content:
When developing applications, oftentimes a simply storage mechanism is needed, for example when [caching response data](https://docs.litestar.dev/latest/usage/caching.html) or storing data for [server-side sessions](https://docs.litestar.dev/latest/usage/middleware/builtin-middleware.html#server-side-sessions). In cases like these a traditional database is often not needed, and a simple key/value store suffices.

Litestar provides several low level key value stores, offering an asynchronous interface to store data in a thread- and process-safe manner. These stores are centrally managed via a [`registry`](https://docs.litestar.dev/latest/reference/stores/registry.html#litestar.stores.registry.StoreRegistry "litestar.stores.registry.StoreRegistry"), allowing easy access throughout the whole application and third party integration (for example plugins).

Built-in stores[#](https://docs.litestar.dev/latest/usage/stores.html#built-in-stores "Link to this heading")
-------------------------------------------------------------------------------------------------------------

[`MemoryStore`](https://docs.litestar.dev/latest/reference/stores/memory.html#litestar.stores.memory.MemoryStore "litestar.stores.memory.MemoryStore")
A simple in-memory store, using a dictionary to hold data. This store offers no persistence and is not thread or multiprocess safe, but it is suitable for basic applications such as caching and has generally the lowest overhead. This is the default store used by Litestar internally. If you plan to enable [multiple web workers](https://docs.litestar.dev/latest/reference/cli.html) and you need inter-process communication across multiple worker processes, you should use one of the other non-memory stores instead.

[`FileStore`](https://docs.litestar.dev/latest/reference/stores/file.html#litestar.stores.file.FileStore "litestar.stores.file.FileStore")
A store that saves data as files on disk. Persistence is built in, and data is easy to extract and back up. It is slower compared to in-memory solutions, and primarily suitable for situations when larger amounts of data need to be stored, is particularly long-lived, or persistence has a very high importance. Offers [namespacing](https://docs.litestar.dev/latest/usage/stores.html#namespacing).

[`RedisStore`](https://docs.litestar.dev/latest/reference/stores/redis.html#litestar.stores.redis.RedisStore "litestar.stores.redis.RedisStore")
A store backend by [redis](https://redis.io/). It offers all the guarantees and features of Redis, making it suitable for almost all applications. Offers [namespacing](https://docs.litestar.dev/latest/usage/stores.html#namespacing).

[`ValkeyStore`](https://docs.litestar.dev/latest/reference/stores/valkey.html#litestar.stores.valkey.ValkeyStore "litestar.stores.valkey.ValkeyStore")
A store backed by [valkey](https://valkey.io/), a fork of Redis created as the result of Redis’ license changes. Similarly to the RedisStore, it is suitable for almost all applications and supports [namespacing](https://docs.litestar.dev/latest/usage/stores.html#namespacing). At the time of writing, `Valkey` is equivalent to `redis.asyncio.Redis`, and all notes pertaining to Redis also apply to Valkey.

Why not memcached?

Memcached is not a supported backend, and will likely also not be added in the future. The reason for this is simply that it’s hard to support memcached properly, since it’s missing a lot of basic functionality like checking a key’s expiry time, or something like Redis’ [SCAN](https://redis.io/commands/scan/) command, which allows to implement pattern-based deletion of keys.

Interacting with a store[#](https://docs.litestar.dev/latest/usage/stores.html#interacting-with-a-store "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------

The most fundamental operations of a store are:

*   [`get`](https://docs.litestar.dev/latest/reference/stores/base.html#litestar.stores.base.Store.get "litestar.stores.base.Store.get"): To retrieve a stored value

*   [`set`](https://docs.litestar.dev/latest/reference/stores/base.html#litestar.stores.base.Store.set "litestar.stores.base.Store.set"): To set a value in the store

*   [`delete`](https://docs.litestar.dev/latest/reference/stores/base.html#litestar.stores.base.Store.delete "litestar.stores.base.Store.delete"): To delete a stored value

### Getting and setting values[#](https://docs.litestar.dev/latest/usage/stores.html#getting-and-setting-values "Link to this heading")

from litestar.stores.memory import MemoryStore

store = MemoryStore()

async def main() -> None:
    value = await store.get("key")
    print(value)  # this will print 'None', as no store with this key has been defined yet

    await store.set("key", b"value")
    value = await store.get("key")
    print(value)

### Setting an expiry time[#](https://docs.litestar.dev/latest/usage/stores.html#setting-an-expiry-time "Link to this heading")

The [`set`](https://docs.litestar.dev/latest/reference/stores/base.html#litestar.stores.base.Store.set "litestar.stores.base.Store.set") method has an optional parameter `expires_in`, allowing to specify a time after which a stored value should expire.

from asyncio import sleep

from litestar.stores.memory import MemoryStore

store = MemoryStore()

async def main() -> None:
    await store.set("foo", b"bar", expires_in=1)
    value = await store.get("foo")
    print(value)

    await sleep(1)
    value = await store.get("foo")  # this will return 'None', since the key has expired
    print(value)

Note

It is up to the individual store to decide how to handle expired values, and implementations may differ. The [`redis based store`](https://docs.litestar.dev/latest/reference/stores/redis.html#litestar.stores.redis.RedisStore "litestar.stores.redis.RedisStore") for example uses Redis’ native expiry mechanism to handle this, while the [`FileStore`](https://docs.litestar.dev/latest/reference/stores/file.html#litestar.stores.file.FileStore "litestar.stores.file.FileStore") only deletes expired values when they’re trying to be accessed, or explicitly deleted via the [`delete_expired`](https://docs.litestar.dev/latest/reference/stores/file.html#litestar.stores.file.FileStore.delete_expired "litestar.stores.file.FileStore.delete_expired") method.

It is also possible to extend the expiry time on each access, which is useful for applications such as server side sessions or LRU caches:

from asyncio import sleep

from litestar.stores.memory import MemoryStore

store = MemoryStore()

async def main() -> None:
    await store.set("foo", b"bar", expires_in=1)
    await sleep(0.5)

    await store.get("foo", renew_for=1)  # this will reset the time to live to one second

    await sleep(1)
    # it has now been 1.5 seconds since the key was set with a life time of one second,
    # so it should have expired however, since it was renewed for one second, it is still available
    value = await store.get("foo")
    print(value)

#### Deleting expired values[#](https://docs.litestar.dev/latest/usage/stores.html#deleting-expired-values "Link to this heading")

When using a [`MemoryStore`](https://docs.litestar.dev/latest/reference/stores/memory.html#litestar.stores.memory.MemoryStore "litestar.stores.memory.MemoryStore") or [`FileStore`](https://docs.litestar.dev/latest/reference/stores/file.html#litestar.stores.file.FileStore "litestar.stores.file.FileStore"), expired data won’t be deleted automatically. Instead, it will only happen when the data is being accessed, or if this process is invoked explicitly via [`MemoryStore.delete_expired`](https://docs.litestar.dev/latest/reference/stores/memory.html#litestar.stores.memory.MemoryStore.delete_expired "litestar.stores.memory.MemoryStore.delete_expired") or [`FileStore.delete_expired`](https://docs.litestar.dev/latest/reference/stores/file.html#litestar.stores.file.FileStore.delete_expired "litestar.stores.file.FileStore.delete_expired") respectively.

It’s a good practice to call `delete_expired` periodically, to ensure the size of the stored values does not grow indefinitely.

In this example, an [after_response](https://docs.litestar.dev/latest/usage/lifecycle-hooks.html#after-response) handler is used to delete expired items at most every 30 second:

from datetime import datetime, timedelta

from litestar import Litestar, Request
from litestar.stores.memory import MemoryStore

memory_store = MemoryStore()

async def after_response(request: Request) -> None:
    now = datetime.utcnow()
    last_cleared = request.app.state.get("store_last_cleared", now)
    if datetime.utcnow() - last_cleared > timedelta(seconds=30):
        await memory_store.delete_expired()
    app.state["store_last_cleared"] = now

app = Litestar(after_response=after_response)

When using the [`FileStore`](https://docs.litestar.dev/latest/reference/stores/file.html#litestar.stores.file.FileStore "litestar.stores.file.FileStore"), expired items may also be deleted on startup:

from pathlib import Path

from litestar import Litestar
from litestar.stores.file import FileStore

file_store = FileStore(Path("data"))

async def on_startup() -> None:
    await file_store.delete_expired()

app = Litestar(on_startup=[on_startup])

Note

For the [`MemoryStore`](https://docs.litestar.dev/latest/reference/stores/memory.html#litestar.stores.memory.MemoryStore "litestar.stores.memory.MemoryStore"), this is not needed as the data is simply stored in a dictionary. This means that every time a new instance of this store is created, it will start out empty.

### What can be stored[#](https://docs.litestar.dev/latest/usage/stores.html#what-can-be-stored "Link to this heading")

Stores generally operate on [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)"); They accept bytes to store, and will return bytes. For convenience, the [`set`](https://docs.litestar.dev/latest/reference/stores/base.html#litestar.stores.base.Store.set "litestar.stores.base.Store.set") method also allows to pass in strings, which will be UTF-8 encoded before being stored. This means that [`get`](https://docs.litestar.dev/latest/reference/stores/base.html#litestar.stores.base.Store.get "litestar.stores.base.Store.get") will return bytes even when a string has been passed to [`set`](https://docs.litestar.dev/latest/reference/stores/base.html#litestar.stores.base.Store.set "litestar.stores.base.Store.set").

The reason for this limitation is simple: Different backends used to store the data offer vastly different encoding, storage, and (de)serialization capacities. Since stores are designed to be interchangeable, this means settling for a common denominator, a type that all backends will support. [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)") meet these requirements and make it possible to store a very wide variety of data.

Technical details

[`MemoryStore`](https://docs.litestar.dev/latest/reference/stores/memory.html#litestar.stores.memory.MemoryStore "litestar.stores.memory.MemoryStore") differs from this, because it does not do any encoding before storing the value. This means that it’s technically possible to store arbitrary objects in this store, and get the same object back. However, this is not reflected in the store’s typing, as the underlying [`Store`](https://docs.litestar.dev/latest/reference/stores/base.html#litestar.stores.base.Store "litestar.stores.base.Store") interface does not guarantee this behaviour, and it is not guaranteed that [`MemoryStore`](https://docs.litestar.dev/latest/reference/stores/memory.html#litestar.stores.memory.MemoryStore "litestar.stores.memory.MemoryStore") will always behave in this case.

### Namespacing[#](https://docs.litestar.dev/latest/usage/stores.html#namespacing "Link to this heading")

When stores are being used for more than one purpose, some extra bookkeeping is required to safely perform bulk operations such as [`delete_all`](https://docs.litestar.dev/latest/reference/stores/base.html#litestar.stores.base.Store.delete_all "litestar.stores.base.Store.delete_all"). If for example a [`RedisStore`](https://docs.litestar.dev/latest/reference/stores/redis.html#litestar.stores.redis.RedisStore "litestar.stores.redis.RedisStore") was used, simply issuing a [FLUSHALL](https://redis.io/commands/flushall/) command might have unforeseen consequences.

To help with this, some stores offer namespacing capabilities, allowing to build a simple hierarchy of stores. These come with the additional [`with_namespace`](https://docs.litestar.dev/latest/reference/stores/base.html#litestar.stores.base.NamespacedStore.with_namespace "litestar.stores.base.NamespacedStore.with_namespace") method, which returns a new [`NamespacedStore`](https://docs.litestar.dev/latest/reference/stores/base.html#litestar.stores.base.NamespacedStore "litestar.stores.base.NamespacedStore") instance. Once a namespaced store is created, operations on it will only affect itself and its child namespaces.

When using the [`RedisStore`](https://docs.litestar.dev/latest/reference/stores/redis.html#litestar.stores.redis.RedisStore "litestar.stores.redis.RedisStore"), this allows to reuse the same underlying `Redis` instance and connection, while ensuring isolation.

Note

[`RedisStore`](https://docs.litestar.dev/latest/reference/stores/redis.html#litestar.stores.redis.RedisStore "litestar.stores.redis.RedisStore") uses the `LITESTAR` namespace by default; all keys created by this store, will use the `LITESTAR` prefix when storing data in redis. [`RedisStore.delete_all`](https://docs.litestar.dev/latest/reference/stores/redis.html#litestar.stores.redis.RedisStore.delete_all "litestar.stores.redis.RedisStore.delete_all") is implemented in such a way that it will only delete keys matching the current namespace, making it safe and side-effect free.

This can be turned off by explicitly passing `namespace=None` to the store when creating a new instance.

from litestar import Litestar
from litestar.stores.redis import RedisStore

root_store = RedisStore.with_client()
cache_store = root_store.with_namespace("cache")
session_store = root_store.with_namespace("sessions")

async def before_shutdown() -> None:
    await cache_store.delete_all()

app = Litestar(before_shutdown=[before_shutdown])

Even though all three stores defined here use the same Redis instance, calling `delete_all` on the `cache_store` will not affect data within the `session_store`.

Defining stores hierarchically like this still allows to easily clear everything, by simply calling [`delete_all`](https://docs.litestar.dev/latest/reference/stores/base.html#litestar.stores.base.Store.delete_all "litestar.stores.base.Store.delete_all") on the root store.

Managing stores with the registry[#](https://docs.litestar.dev/latest/usage/stores.html#managing-stores-with-the-registry "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------

The [`StoreRegistry`](https://docs.litestar.dev/latest/reference/stores/registry.html#litestar.stores.registry.StoreRegistry "litestar.stores.registry.StoreRegistry") is a central place through which stores can be configured and managed, and can help to easily access stores set up and used by other parts of the application, Litestar internals or third party integrations. It is available throughout the whole application context via the [`Litestar.stores`](https://docs.litestar.dev/latest/reference/app.html#litestar.app.Litestar "litestar.app.Litestar") attribute.

It operates on a few basic principles:

*   An initial mapping of stores can be provided to the registry

*   Registered stores can be requested with [`get`](https://docs.litestar.dev/latest/reference/stores/registry.html#litestar.stores.registry.StoreRegistry.get "litestar.stores.registry.StoreRegistry.get")

*   If a store has been requested that has not been registered yet, a store of that name will be created and registered using the [the default factory](https://docs.litestar.dev/latest/usage/stores.html#the-default-factory)

from litestar import Litestar
from litestar.stores.memory import MemoryStore

app = Litestar([], stores={"memory": MemoryStore()})

memory_store = app.stores.get("memory")
# this is the previously defined store

some_other_store = app.stores.get("something_else")
# this will be a newly created instance

assert app.stores.get("something_else") is some_other_store
# but subsequent requests will return the same instance

This pattern offers isolation of stores, and an easy way to configure stores used by middlewares and other Litestar features or third party integrations.

In the following example, the store set up by the [`RateLimitMiddleware`](https://docs.litestar.dev/latest/reference/middleware/rate_limit.html#litestar.middleware.rate_limit.RateLimitMiddleware "litestar.middleware.rate_limit.RateLimitMiddleware") is accessed via the registry:

from litestar import Litestar
from litestar.middleware.rate_limit import RateLimitConfig

app = Litestar(middleware=[RateLimitConfig(("second", 1)).middleware])
rate_limit_store = app.stores.get("rate_limit")

This works because [`RateLimitMiddleware`](https://docs.litestar.dev/latest/reference/middleware/rate_limit.html#litestar.middleware.rate_limit.RateLimitMiddleware "litestar.middleware.rate_limit.RateLimitMiddleware") will request its store internally via `app.stores.get` as well.

### The default factory[#](https://docs.litestar.dev/latest/usage/stores.html#the-default-factory "Link to this heading")

The pattern above is made possible by using the registry’s default factory; A callable that gets invoked every time a store is requested that hasn’t been registered yet. It’s similar to the `default` argument to [`dict.get()`](https://docs.python.org/3/library/stdtypes.html#dict.get "(in Python v3.14)").

By default, the default factory is a function that returns a new [`MemoryStore`](https://docs.litestar.dev/latest/reference/stores/memory.html#litestar.stores.memory.MemoryStore "litestar.stores.memory.MemoryStore") instance. This behaviour can be changed by supplying a custom `default_factory` method to the registry.

To make use of this, a registry instance can be passed directly to the application:

from litestar import Litestar
from litestar.stores.memory import MemoryStore
from litestar.stores.registry import StoreRegistry

memory_store = MemoryStore()

def default_factory(name: str) -> MemoryStore:
    return memory_store

app = Litestar([], stores=StoreRegistry(default_factory=default_factory))

The registry will now return the same [`MemoryStore`](https://docs.litestar.dev/latest/reference/stores/memory.html#litestar.stores.memory.MemoryStore "litestar.stores.memory.MemoryStore") every time an undefined store is being requested.

### Using the registry to configure integrations[#](https://docs.litestar.dev/latest/usage/stores.html#using-the-registry-to-configure-integrations "Link to this heading")

This mechanism also allows to control the stores used by various integrations, such as middlewares:

from pathlib import Path

from litestar import Litestar
from litestar.middleware.session.server_side import ServerSideSessionConfig
from litestar.stores.file import FileStore
from litestar.stores.redis import RedisStore

app = Litestar(
    stores={
        "sessions": RedisStore.with_client(),
        "response_cache": FileStore(Path("response-cache")),
    },
    middleware=[ServerSideSessionConfig().middleware],
)

In this example, the registry is being set up with stores using the `sessions` and `response_cache` keys. These are not magic constants, but instead configuration values that can be changed. Those names just happen to be their default values. Adjusting those default values allows to easily reuse stores, without the need for a more complex setup:

from pathlib import Path

from litestar import Litestar
from litestar.config.response_cache import ResponseCacheConfig
from litestar.middleware.rate_limit import RateLimitConfig
from litestar.middleware.session.server_side import ServerSideSessionConfig
from litestar.stores.file import FileStore
from litestar.stores.redis import RedisStore

app = Litestar(
    stores={"redis": RedisStore.with_client(), "file": FileStore(Path("data"))},
    response_cache_config=ResponseCacheConfig(store="redis"),
    middleware=[
        ServerSideSessionConfig(store="file").middleware,
        RateLimitConfig(rate_limit=("second", 10), store="redis").middleware,
    ],
)

Now the rate limit middleware and response caching will use the `redis` store, while sessions will be store in the `file` store.

### Setting up the default factory with namespacing[#](https://docs.litestar.dev/latest/usage/stores.html#setting-up-the-default-factory-with-namespacing "Link to this heading")

The default factory can be used in conjunction with [namespacing](https://docs.litestar.dev/latest/usage/stores.html#namespacing) to create isolated, hierarchically organized stores, with minimal boilerplate:

from litestar import Litestar, get
from litestar.middleware.rate_limit import RateLimitConfig
from litestar.middleware.session.server_side import ServerSideSessionConfig
from litestar.stores.redis import RedisStore
from litestar.stores.registry import StoreRegistry

root_store = RedisStore.with_client()

@get(cache=True, sync_to_thread=False)
def cached_handler() -> str:
    # this will use app.stores.get("response_cache")
    return "Hello, world!"

app = Litestar(
    [cached_handler],
    stores=StoreRegistry(default_factory=root_store.with_namespace),
    middleware=[
        RateLimitConfig(("second", 1)).middleware,
        ServerSideSessionConfig().middleware,
    ],
)

Without any extra configuration, every call to `app.stores.get` with a unique name will return a namespace for this name only, while re-using the underlying Redis instance.

### Store lifetime[#](https://docs.litestar.dev/latest/usage/stores.html#store-lifetime "Link to this heading")

Stores may not be automatically closed when the application is shut down. This is the case in particular for the RedisStore if you are not using the class method [`RedisStore.with_client`](https://docs.litestar.dev/latest/reference/stores/redis.html#litestar.stores.redis.RedisStore.with_client "litestar.stores.redis.RedisStore.with_client") and passing in your own Redis instance. In this case you’re responsible to close the Redis instance yourself.
