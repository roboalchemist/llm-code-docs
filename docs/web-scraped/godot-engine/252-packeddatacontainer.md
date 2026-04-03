# PackedDataContainer

# PackedDataContainer
Deprecated:Use@GlobalScope.var_to_bytes()orFileAccess.store_var()instead. To enable data compression, usePackedByteArray.compress()orFileAccess.open_compressed().
Inherits:Resource<RefCounted<Object
Efficiently packs and serializesArrayorDictionary.

## Description
PackedDataContainercan be used to efficiently store data from untyped containers. The data is packed into raw bytes and can be saved to file. OnlyArrayandDictionarycan be stored this way.
You can retrieve the data by iterating on the container, which will work as if iterating on the packed data itself. If the packed container is aDictionary, the data can be retrieved by key names (String/StringNameonly).
```
var data = { "key": "value", "another_key": 123, "lock": Vector2() }
var packed = PackedDataContainer.new()
packed.pack(data)
ResourceSaver.save(packed, "packed_data.res")
```
```
var container = load("packed_data.res")
for key in container:
    prints(key, container[key])
```
Prints:
```
key value
lock (0, 0)
another_key 123
```
Nested containers will be packed recursively. While iterating, they will be returned asPackedDataContainerRef.

## Methods

| Error | pack(value:Variant) |
|---|---|
| int | size()const |

Error
pack(value:Variant)
size()const

## Method Descriptions
Errorpack(value:Variant)🔗
Packs the given container into a binary representation. Thevaluemust be eitherArrayorDictionary, any other type will result in invalid data error.
Note:Subsequent calls to this method will overwrite the existing data.
intsize()const🔗
Returns the size of the packed container (seeArray.size()andDictionary.size()).

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.