# Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.serialization.html

Title: kombu.serialization — Kombu 5.6.2 documentation

URL Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.serialization.html

Markdown Content:
This document is for Kombu's development version, which can be significantly different from previous releases. Get the stable docs here: [5.3](https://kombu.readthedocs.io/en/latest/reference/kombu.serialization.html).

Serialization utilities.

*   [Overview](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.serialization.html#overview)

*   [Exceptions](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.serialization.html#exceptions)

*   [Serialization](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.serialization.html#serialization)

*   [Registry](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.serialization.html#registry)

[Overview](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.serialization.html#id4)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.serialization.html#overview "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Centralized support for encoding/decoding of data structures. Contains json, pickle, msgpack, and yaml serializers.

Optionally installs support for YAML if the [PyYAML](https://pyyaml.org/) package is installed.

Optionally installs support for [msgpack](https://msgpack.org/) if the [msgpack-python](https://pypi.org/project/msgpack-python/) package is installed.

[Exceptions](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.serialization.html#id5)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.serialization.html#exceptions "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

_exception_ kombu.serialization.SerializerNotInstalled[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/exceptions.html#SerializerNotInstalled)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.serialization.html#kombu.serialization.SerializerNotInstalled "Link to this definition")
Support for the requested serialization type is not installed.

[Serialization](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.serialization.html#id6)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.serialization.html#serialization "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

kombu.serialization.dumps(_data_, _serializer=None_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.serialization.html#kombu.serialization.dumps "Link to this definition")
Encode data.

Serialize a data structure into a string suitable for sending as an AMQP message body.

### Arguments:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.serialization.html#arguments "Link to this heading")

> data (List, Dict, str): The message data to send.
> 
> serializer (str): An optional string representing
> the serialization method you want the data marshalled into. (For example, json, raw, or pickle).
> 
> 
> If `None` (default), then json will be used, unless data is a [`str`](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)") or `unicode` object. In this latter case, no serialization occurs as it would be unnecessary.
> 
> 
> Note that if serializer is specified, then that serialization method will be used even if a [`str`](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)") or `unicode` object is passed in.

returns:
*   **Tuple[str, str, str]** (_A three-item tuple containing the_)

*   content type (e.g., application/json), content encoding, (e.g.,

*   utf-8) and a string containing the serialized data.

raises SerializerNotInstalled:
If the serialization method: requested is not available.

kombu.serialization.loads(_data_, _content\_type_, _content\_encoding_, _accept=None_, _force=False_, _\_trusted\_content=frozenset({'application/data','application/text'})_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.serialization.html#kombu.serialization.loads "Link to this definition")
Decode serialized data.

Deserialize a data stream as serialized using dumps based on content_type.

### Arguments:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.serialization.html#id1 "Link to this heading")

> data (bytes, buffer, str): The message data to deserialize.
> 
> content_type (str): The content-type of the data.
> (e.g., application/json).
> 
> content_encoding (str): The content-encoding of the data.
> (e.g., utf-8, binary, or us-ascii).
> 
> 
> accept (Set): List of content-types to accept.

raises ContentDisallowed:
If the content-type is not accepted.:

returns:
**Any**

rtype:
The unserialized data.

kombu.serialization.raw_encode(_data_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/serialization.html#raw_encode)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.serialization.html#kombu.serialization.raw_encode "Link to this definition")
Special case serializer.

[Registry](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.serialization.html#id7)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.serialization.html#registry "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

kombu.serialization.register(_name_, _encoder_, _decoder_, _content\_type_, _content\_encoding='utf-8'_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.serialization.html#kombu.serialization.register "Link to this definition")
Register a new encoder/decoder.

### Arguments:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.serialization.html#id2 "Link to this heading")

> name (str): A convenience name for the serialization method.
> 
> encoder (callable): A method that will be passed a python data
> structure and should return a string representing the serialized data. If `None`, then only a decoder will be registered. Encoding will not be possible.
> 
> decoder (Callable): A method that will be passed a string
> representing serialized data and should return a python data structure. If `None`, then only an encoder will be registered. Decoding will not be possible.
> 
> content_type (str): The mime-type describing the serialized
> structure.
> 
> content_encoding (str): The content encoding (character set) that
> the decoder method will be returning. Will usually be utf-8, us-ascii, or binary.

kombu.serialization.unregister(_name_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.serialization.html#kombu.serialization.unregister "Link to this definition")
Unregister registered encoder/decoder.

### Arguments:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.serialization.html#id3 "Link to this heading")

> name (str): Registered serialization method name.

raises SerializerNotInstalled:
If a serializer by that name: cannot be found.

kombu.serialization.registry _=<kombu.serialization.SerializerRegistry object>_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.serialization.html#kombu.serialization.registry "Link to this definition")
Global registry of serializers/deserializers.
