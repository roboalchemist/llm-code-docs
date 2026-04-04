# Zenoh Migration Guides

# https://zenoh.io/docs/migration_1.0/python/

Source: https://zenoh.io/docs/migration_1.0/python/

![](../../../img/zenoh-dragon-bg-150x163.png)
`handlers.Callback`

# Python

## Highlights

The library has been fully rewritten to use only Rust. It should make no difference for users, except for a significant performance improvement.

The API has also been reworked to feel more pythonic, using notably context managers.

## Context managers and background callbacks

You *should* close the zenoh session after use and the recommended way is through context manager:

`import zenoh
with zenoh.open(zenoh.Config()) as session:
 # `session.close()` will be called at the end of the block`

Session-managed objects like subscribers or queryables can also be managed using context managers:

`with session.declare_subscriber("my/keyexpr") as subscriber:
 # `subscriber.undeclare()` will be called at the end of the block``

In previous version, it was necessary to keep a variable in the scope for a subscriber/queryable declared with a callback. This constraint has been lifted, and it’s now possible to declare a “background” entity; this entity will keep living in background, having its callback executed until the session is closed.

`import zenoh
with zenoh.open(zenoh.Config()) as session:
 # no need to declare a variable
 session.declare_subscriber("my/keyepxr", lambda s: print(s), background=True)
 sleep(10) # subscriber stays in background and its callback can be called
 # `session.close()` will be called at the end of the block,
 # and it will undeclare the subscriber`

## Drop-callback has to be wrapped in `handlers.Callback`

`handlers.Callback`

In the previous 0.11.0 version, it was possible to pass a drop-callback with the main callback in a tuple for operations like `Session.declare_subscriber`. However, it was also possible to pass a tuple with a “receiver” (renamed “handler” in 1.0.0) as second member, and that could confuse users.
The API has been changed and now requires the drop-callback to be wrapped in `handlers.Callback`.

`Session.declare_subscriber`
`handlers.Callback`
`def on_sample(sample: zenoh.Sample): ...
def on_done(): ...
session.declare_subscriber((on_sample, on_done))`
`def on_sample(sample: zenoh.Sample): ...
def on_done(): ...
session.declare_subscriber(zenoh.handlers.Callback(on_sample, on_done))`

NOTE: ⚠️ Passing drop-callback in a tuple will no longer work as expected, as the drop callback will never be executed. To ease migration and avoid surprises, a warning will be displayed in this case.

## Value is gone, long live ZBytes

`Value` has been split into `ZBytes` and `Encoding`. `put` and other operations now require a `ZBytes` payload, and builders accept an optional `Encoding` parameter.

`Value`
`ZBytes`
`Encoding`
`put`
`ZBytes`
`Encoding`

`ZBytes` is a raw bytes container. It can be created directly from raw bytes/strings using `ZBytes` constructor. Then bytes can be retrieved using `ZBytes.to_bytes` or `ZBytes.to_string`. Sample payload is now a `ZBytes` instead of `bytes`.

`ZBytes`
`ZBytes`
`ZBytes.to_bytes`
`ZBytes.to_string`
`ZBytes`
`bytes`
`sample = subscriber.recv()
my_string = sample.payload.decode("utf-8")`
`sample = subscriber.recv()
my_string = sample.payload.to_string()`

You can look at a full set of examples in [`examples/z_bytes.py`](https://github.com/eclipse-zenoh/zenoh-python/blob/1.0.0-beta.4/examples/z_bytes.py).

`examples/z_bytes.py`

## Serialization

Zenoh does provide serialization for convenience as an extension in `zenoh.ext` module. Serialization is implemented for a bunch of standard types like `int`, `float`, `list`, `dict`, `tuple`, etc. and is used through functions `z_serialize`/`z_deserialize`.

`zenoh.ext`
`int`
`float`
`list`
`dict`
`tuple`
`z_serialize`
`z_deserialize`
`input = b"raw bytes"
payload = ZBytes(input)
output = payload.to_bytes()`

`zenoh.ext` serialization doesn’t pretend to cover all use cases, as it is just one available choice among other serialization formats like JSON, Protobuf, CBOR, etc. In the end, Zenoh will just send and receive payload raw bytes independently of the serialization used.

`zenoh.ext`

NOTE: ⚠️ Serialization of `bytes` is not the same as passing `bytes` to `ZBytes` constructor.

`bytes`
`bytes`
`ZBytes`

## Encoding

`Encoding` has been reworked.
Zenoh does not impose any encoding requirement on the user, nor does it operate on it.
It can be thought of as optional metadata, carried over by Zenoh in such a way that the end user’s application may perform different operations based on encoding.

`Encoding`

NOTE: ⚠️ The encoding is no longer automatically inferred from the payload type.

`session.put(json.dumps({"key", "value"}), encoding=Encoding.APPLICATION_JSON)`

Users can also define their own encoding scheme that does not need to be based on the pre-defined variants.

`encoding = Encoding("pointcloud/LAS")`

Because encoding is now optional for `put`, `Publisher` can be declared with a default encoding, which will be used in every `Publisher.put`.

`put`
`Publisher`
`Publisher.put`
`publisher = session.declare_publisher("my/keyepxr", encoding=Encoding.APPLICATION_JSON)
// default encoding from publisher `application/json`
publisher.put(json.dumps({"key", "value"}))`

## Handlers

The library now directly exposes Rust-backed handlers in `zenoh.handlers`. When no handler is provided, `zenoh.handlers.DefaultHandler` is used.

`zenoh.handlers`
`zenoh.handlers.DefaultHandler`
`import zenoh.handlers
subscriber = session.declare_subscriber("my/keyexpr", zenoh.handlers.DefaultHandler())
# equivalent to `session.declare_subscriber("my/keyexpr")`# builtin handlers provides `try_recv`/`recv` methods and can be iterated sample_or_none = subscriber.handler.try_recv()
sample = subscriber.handler.recv()
for sample in subscriber.handler:
 ...
# builtin handlers methods can be accessed directly through subscriber/queryable object sample_or_none = subscriber.try_recv()
sample = subscriber.recv()
for sample in subscriber:
 ...`

Callbacks can also be used as handler:

`def handle_sample(sample: zenoh.Sample):
 ...
session.declare_subscriber("my/keyexpr", handle_sample)
# A drop callback can be passed using `zenoh.handlers.Callback`def stop():
 ...
session.declare_subscriber("my/keyexpr", zenoh.handlers.Callback(handle_sample, stop))`

Note that for each callback handler, zenoh will in fact use a builtin handler and spawn a thread iterating the handler and calling the callback. This is needed to avoid GIL-related issues in low-level parts of zenoh, and as a result, leads to a significant performance improvement.

##### Eclipse Incubation

![](../../../img/eclipse-incubation.png)

![](../../../img/eclipse-incubation.png)

Eclipse zenoh ™ is an incubating project under the Eclipse Foundation.

##### More Information

[Legal](https://www.eclipse.org/legal)

[Privacy policy](https://www.eclipse.org/legal/privacy.php)

[Terms of use](https://www.eclipse.org/legal/termsofuse.php)

[Copyright](https://www.eclipse.org/legal/copyright.php)

[Report a security issue](https://www.eclipse.org/security/)

[Eclipse Public License 2.0](https://www.eclipse.org/legal/epl-2.0/)

[Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0)

[Eclipse Foundation](https://www.eclipse.org/)

##### Sponsored by:

[![](../../../img/eclipse-foundation.svg)](https://www.eclipse.org)

![](../../../img/eclipse-foundation.svg)

[![](../../../img/zettascale-dark.svg)](https://zettascale.tech)

![](../../../img/zettascale-dark.svg)

##### Follow us

[GitHub](https://github.com/eclipse-zenoh/zenoh)

[Discord](https://discord.gg/vSDSpqnbkm)

[Youtube](https://www.youtube.com/channel/UCslbiyiqgOAPMjCrPWIfQ5Q)

[About](../../../docs/overview/what-is-zenoh)

![](../../../img/zenoh-dragon-150x163.png)

![](../../../img/zenoh-dragon-150x163.png)

Eclipse zenoh ™ is free, open source and always will be.

Copyright © 2022 Eclipse Foundation

Built with [HUGO](https://gohugo.io/)

---

