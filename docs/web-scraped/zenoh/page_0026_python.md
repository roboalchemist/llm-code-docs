# Python · Zenoh - pub/sub, geo distributed storage, query

Source: https://zenoh.io/docs/migration_1.0/python

# Source: https://zenoh.io/docs/migration_1.0/python

# Python

## Highlights
The library has been fully rewritten to use only Rust. It should make no difference for users, except for a significant performance improvement.
The API has also been reworked to feel more pythonic, using notably context managers.

## Context managers and background callbacks
Youshouldclose the zenoh session after use and the recommended way is through context manager:
```
import zenoh
with zenoh.open(zenoh.Config()) as session:
    # `session.close()` will be called at the end of the block
```

Session-managed objects like subscribers or queryables can also be managed using context managers:
```
with session.declare_subscriber("my/keyexpr") as subscriber:
    # `subscriber.undeclare()` will be called at the end of the block`
```

In previous version, it was necessary to keep a variable in the scope for a subscriber/queryable declared with a callback. This constraint has been lifted, and it’s now possible to declare a “background” entity; this entity will keep living in background, having its callback executed until the session is closed.
```
import zenoh
with zenoh.open(zenoh.Config()) as session:
    # no need to declare a variable
    session.declare_subscriber("my/keyepxr", lambda s: print(s), background=True)
    sleep(10) # subscriber stays in background and its callback can be called
    # `session.close()` will be called at the end of the block,
    # and it will undeclare the subscriber
```

## Drop-callback has to be wrapped inhandlers.Callback
In the previous 0.11.0 version, it was possible to pass a drop-callback with the main callback in a tuple for operations likeSession.declare_subscriber. However, it was also possible to pass a tuple with a “receiver” (renamed “handler” in 1.0.0) as second member, and that could confuse users.
The API has been changed and now requires the drop-callback to be wrapped inhandlers.Callback.
- Zenoh 0.11.x
```
def on_sample(sample: zenoh.Sample): ...
def on_done(): ...
session.declare_subscriber((on_sample, on_done))
```

- Zenoh 1.0.0
```
def on_sample(sample: zenoh.Sample): ...
def on_done(): ...
session.declare_subscriber(zenoh.handlers.Callback(on_sample, on_done))
```

NOTE: ⚠️ Passing drop-callback in a tuple will no longer work as expected, as the drop callback will never be executed. To ease migration and avoid surprises, a warning will be displayed in this case.

## Value is gone, long live ZBytes
Valuehas been split intoZBytesandEncoding.putand other operations now require aZBytespayload, and builders accept an optionalEncodingparameter.
ZBytesis a raw bytes container. It can be created directly from raw bytes/strings usingZBytesconstructor. Then bytes can be retrieved usingZBytes.to_bytesorZBytes.to_string. Sample payload is now aZBytesinstead ofbytes.
- Zenoh 0.11.x
```
sample = subscriber.recv()
my_string = sample.payload.decode("utf-8")
```

- Zenoh 1.0.0
```
sample = subscriber.recv()
my_string = sample.payload.to_string()
```

You can look at a full set of examples inexamples/z_bytes.py.

## Serialization
Zenoh does provide serialization for convenience as an extension inzenoh.extmodule. Serialization is implemented for a bunch of standard types likeint,float,list,dict,tuple, etc. and is used through functionsz_serialize/z_deserialize.
```
input = b"raw bytes"
payload = ZBytes(input)
output = payload.to_bytes()
```

zenoh.extserialization doesn’t pretend to cover all use cases, as it is just one available choice among other serialization formats like JSON, Protobuf, CBOR, etc. In the end, Zenoh will just send and receive payload raw bytes independently of the serialization used.
NOTE: ⚠️ Serialization ofbytesis not the same as passingbytestoZBytesconstructor.

## Encoding
Encodinghas been reworked.
Zenoh does not impose any encoding requirement on the user, nor does it operate on it.
It can be thought of as optional metadata, carried over by Zenoh in such a way that the end user’s application may perform different operations based on encoding.
NOTE: ⚠️ The encoding is no longer automatically inferred from the payload type.
```
session.put(json.dumps({"key", "value"}), encoding=Encoding.APPLICATION_JSON)
```

Users can also define their own encoding scheme that does not need to be based on the pre-defined variants.
```
encoding = Encoding("pointcloud/LAS")
```

Because encoding is now optional forput,Publishercan be declared with a default encoding, which will be used in everyPublisher.put.
```
publisher = session.declare_publisher("my/keyepxr", encoding=Encoding.APPLICATION_JSON)
// default encoding from publisher `application/json`
publisher.put(json.dumps({"key", "value"}))
```

## Handlers
The library now directly exposes Rust-backed handlers inzenoh.handlers. When no handler is provided,zenoh.handlers.DefaultHandleris used.
```
import zenoh.handlers
subscriber = session.declare_subscriber("my/keyexpr", zenoh.handlers.DefaultHandler())
# equivalent to `session.declare_subscriber("my/keyexpr")`# builtin handlers provides `try_recv`/`recv` methods and can be iterated sample_or_none = subscriber.handler.try_recv()
sample = subscriber.handler.recv()
for sample in subscriber.handler:
    ...
# builtin handlers methods can be accessed directly through subscriber/queryable object sample_or_none = subscriber.try_recv()
sample = subscriber.recv()
for sample in subscriber:
    ...
```

Callbacks can also be used as handler:
```
def handle_sample(sample: zenoh.Sample):
    ...
session.declare_subscriber("my/keyexpr", handle_sample)
# A drop callback can be passed using `zenoh.handlers.Callback`def stop():
    ...
session.declare_subscriber("my/keyexpr", zenoh.handlers.Callback(handle_sample, stop))
```

Note that for each callback handler, zenoh will in fact use a builtin handler and spawn a thread iterating the handler and calling the callback. This is needed to avoid GIL-related issues in low-level parts of zenoh, and as a result, leads to a significant performance improvement.