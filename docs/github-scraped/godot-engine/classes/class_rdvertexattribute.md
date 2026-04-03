:github_url: hide



# RDVertexAttribute

**Inherits:** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Vertex attribute (used by [RenderingDevice<class_RenderingDevice>]).


## Description

This object is used by [RenderingDevice<class_RenderingDevice>].


## Properties

> **TABLE**
> :widths: auto
>
> +--------------------------------------------------------------+--------------------------------------------------------------+----------------+
> | :ref:`int<class_int>`                                        | :ref:`binding<class_RDVertexAttribute_property_binding>`     | ``4294967295`` |
> +--------------------------------------------------------------+--------------------------------------------------------------+----------------+
> | :ref:`DataFormat<enum_RenderingDevice_DataFormat>`           | :ref:`format<class_RDVertexAttribute_property_format>`       | ``232``        |
> +--------------------------------------------------------------+--------------------------------------------------------------+----------------+
> | :ref:`VertexFrequency<enum_RenderingDevice_VertexFrequency>` | :ref:`frequency<class_RDVertexAttribute_property_frequency>` | ``0``          |
> +--------------------------------------------------------------+--------------------------------------------------------------+----------------+
> | :ref:`int<class_int>`                                        | :ref:`location<class_RDVertexAttribute_property_location>`   | ``0``          |
> +--------------------------------------------------------------+--------------------------------------------------------------+----------------+
> | :ref:`int<class_int>`                                        | :ref:`offset<class_RDVertexAttribute_property_offset>`       | ``0``          |
> +--------------------------------------------------------------+--------------------------------------------------------------+----------------+
> | :ref:`int<class_int>`                                        | :ref:`stride<class_RDVertexAttribute_property_stride>`       | ``0``          |
> +--------------------------------------------------------------+--------------------------------------------------------------+----------------+
>

----


## Property Descriptions



[int<class_int>] **binding** = `4294967295` [🔗<class_RDVertexAttribute_property_binding>]


- |void| **set_binding**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_binding**\ (\ )

The index of the buffer in the vertex buffer array to bind this vertex attribute. When set to `-1`, it defaults to the index of the attribute.

\ **Note:** You cannot mix binding explicitly assigned attributes with implicitly assigned ones (i.e. `-1`). Either all attributes must have their binding set to `-1`, or all must have explicit bindings.


----



[DataFormat<enum_RenderingDevice_DataFormat>] **format** = `232` [🔗<class_RDVertexAttribute_property_format>]


- |void| **set_format**\ (\ value\: [DataFormat<enum_RenderingDevice_DataFormat>]\ )
- [DataFormat<enum_RenderingDevice_DataFormat>] **get_format**\ (\ )

The way that this attribute's data is interpreted when sent to a shader.


----



[VertexFrequency<enum_RenderingDevice_VertexFrequency>] **frequency** = `0` [🔗<class_RDVertexAttribute_property_frequency>]


- |void| **set_frequency**\ (\ value\: [VertexFrequency<enum_RenderingDevice_VertexFrequency>]\ )
- [VertexFrequency<enum_RenderingDevice_VertexFrequency>] **get_frequency**\ (\ )

The rate at which this attribute is pulled from its vertex buffer.


----



[int<class_int>] **location** = `0` [🔗<class_RDVertexAttribute_property_location>]


- |void| **set_location**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_location**\ (\ )

The location in the shader that this attribute is bound to.


----



[int<class_int>] **offset** = `0` [🔗<class_RDVertexAttribute_property_offset>]


- |void| **set_offset**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_offset**\ (\ )

The number of bytes between the start of the vertex buffer and the first instance of this attribute.


----



[int<class_int>] **stride** = `0` [🔗<class_RDVertexAttribute_property_stride>]


- |void| **set_stride**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_stride**\ (\ )

The number of bytes between the starts of consecutive instances of this attribute.

