:github_url: hide



# PackedDataContainer

**Deprecated:** Use [@GlobalScope.var_to_bytes()<class_@GlobalScope_method_var_to_bytes>] or [FileAccess.store_var()<class_FileAccess_method_store_var>] instead. To enable data compression, use [PackedByteArray.compress()<class_PackedByteArray_method_compress>] or [FileAccess.open_compressed()<class_FileAccess_method_open_compressed>].

**Inherits:** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Efficiently packs and serializes [Array<class_Array>] or [Dictionary<class_Dictionary>].


## Description

**PackedDataContainer** can be used to efficiently store data from untyped containers. The data is packed into raw bytes and can be saved to file. Only [Array<class_Array>] and [Dictionary<class_Dictionary>] can be stored this way.

You can retrieve the data by iterating on the container, which will work as if iterating on the packed data itself. If the packed container is a [Dictionary<class_Dictionary>], the data can be retrieved by key names ([String<class_String>]/[StringName<class_StringName>] only).

::

    var data = { "key": "value", "another_key": 123, "lock": Vector2() }
    var packed = PackedDataContainer.new()
    packed.pack(data)
    ResourceSaver.save(packed, "packed_data.res")

::

    var container = load("packed_data.res")
    for key in container:
        prints(key, container[key])

Prints:

> **CODE**
>
> key value
> lock (0, 0)
> another_key 123
>
Nested containers will be packed recursively. While iterating, they will be returned as [PackedDataContainerRef<class_PackedDataContainerRef>].


## Methods

> **TABLE**
> :widths: auto
>
> +---------------------------------------+-------------------------------------------------------------------------------------------------+
> | :ref:`Error<enum_@GlobalScope_Error>` | :ref:`pack<class_PackedDataContainer_method_pack>`\ (\ value\: :ref:`Variant<class_Variant>`\ ) |
> +---------------------------------------+-------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                 | :ref:`size<class_PackedDataContainer_method_size>`\ (\ ) |const|                                |
> +---------------------------------------+-------------------------------------------------------------------------------------------------+
>

----


## Method Descriptions



[Error<enum_@GlobalScope_Error>] **pack**\ (\ value\: [Variant<class_Variant>]\ ) [🔗<class_PackedDataContainer_method_pack>]

Packs the given container into a binary representation. The `value` must be either [Array<class_Array>] or [Dictionary<class_Dictionary>], any other type will result in invalid data error.

\ **Note:** Subsequent calls to this method will overwrite the existing data.


----



[int<class_int>] **size**\ (\ ) |const| [🔗<class_PackedDataContainer_method_size>]

Returns the size of the packed container (see [Array.size()<class_Array_method_size>] and [Dictionary.size()<class_Dictionary_method_size>]).

