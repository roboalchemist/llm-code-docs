# Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.json.html

Title: kombu.utils.json — Kombu 5.6.2 documentation

URL Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.json.html

Markdown Content:
This document is for Kombu's development version, which can be significantly different from previous releases. Get the stable docs here: [5.3](https://kombu.readthedocs.io/en/latest/reference/kombu.utils.json.html).

JSON Utilities - `kombu.utils.json`[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.json.html#json-utilities-kombu-utils-json "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

JSON Serialization Utilities.

_class_ kombu.utils.json.JSONEncoder(_*_, _skipkeys=False_, _ensure\_ascii=True_, _check\_circular=True_, _allow\_nan=True_, _sort\_keys=False_, _indent=None_, _separators=None_, _default=None_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/utils/json.html#JSONEncoder)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.json.html#kombu.utils.json.JSONEncoder "Link to this definition")
Kombu custom json encoder.

default(_o_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/utils/json.html#JSONEncoder.default)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.json.html#kombu.utils.json.JSONEncoder.default "Link to this definition")
Implement this method in a subclass such that it returns a serializable object for `o`, or calls the base implementation (to raise a `TypeError`).

For example, to support arbitrary iterators, you could implement default like this:

def default(self, o):
    try:
        iterable = iter(o)
    except TypeError:
        pass
    else:
        return list(iterable)
    # Let the base class default method raise the TypeError
    return JSONEncoder.default(self, o)

kombu.utils.json.dumps(_s_, _\_dumps=<function dumps>_, _cls=<class'kombu.utils.json.JSONEncoder'>_, _default\_kwargs=None_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/utils/json.html#dumps)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.json.html#kombu.utils.json.dumps "Link to this definition")
Serialize object to json string.

kombu.utils.json.loads(_s_, _\_loads=<function loads>_, _decode\_bytes=True_, _object\_hook=<function object\_hook>_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/utils/json.html#loads)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.json.html#kombu.utils.json.loads "Link to this definition")
Deserialize json from string.

kombu.utils.json.object_hook(_o:[dict](https://docs.python.org/dev/library/stdtypes.html#dict "(in Python v3.15)")_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/utils/json.html#object_hook)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.json.html#kombu.utils.json.object_hook "Link to this definition")
Hook function to perform custom deserialization.

kombu.utils.json.register_type(_t:type[T],marker:str|None,encoder:Callable[[T],EncodedT],decoder:Callable[[EncodedT],T]=<function<lambda>>_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/utils/json.html#register_type)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.json.html#kombu.utils.json.register_type "Link to this definition")
Add support for serializing/deserializing native python type.

If marker is None, the encoding is a pure transformation and the result is not placed in an envelope, so decoder is unnecessary. Decoding must instead be handled outside this library.
