:github_url: hide



# RDAttachmentFormat

**Inherits:** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Attachment format (used by [RenderingDevice<class_RenderingDevice>]).


## Description

This object is used by [RenderingDevice<class_RenderingDevice>].


## Properties

> **TABLE**
> :widths: auto
>
> +------------------------------------------------------------+-------------------------------------------------------------------+--------+
> | :ref:`DataFormat<enum_RenderingDevice_DataFormat>`         | :ref:`format<class_RDAttachmentFormat_property_format>`           | ``36`` |
> +------------------------------------------------------------+-------------------------------------------------------------------+--------+
> | :ref:`TextureSamples<enum_RenderingDevice_TextureSamples>` | :ref:`samples<class_RDAttachmentFormat_property_samples>`         | ``0``  |
> +------------------------------------------------------------+-------------------------------------------------------------------+--------+
> | :ref:`int<class_int>`                                      | :ref:`usage_flags<class_RDAttachmentFormat_property_usage_flags>` | ``0``  |
> +------------------------------------------------------------+-------------------------------------------------------------------+--------+
>

----


## Property Descriptions



[DataFormat<enum_RenderingDevice_DataFormat>] **format** = `36` [🔗<class_RDAttachmentFormat_property_format>]


- |void| **set_format**\ (\ value\: [DataFormat<enum_RenderingDevice_DataFormat>]\ )
- [DataFormat<enum_RenderingDevice_DataFormat>] **get_format**\ (\ )

The attachment's data format.


----



[TextureSamples<enum_RenderingDevice_TextureSamples>] **samples** = `0` [🔗<class_RDAttachmentFormat_property_samples>]


- |void| **set_samples**\ (\ value\: [TextureSamples<enum_RenderingDevice_TextureSamples>]\ )
- [TextureSamples<enum_RenderingDevice_TextureSamples>] **get_samples**\ (\ )

The number of samples used when sampling the attachment.


----



[int<class_int>] **usage_flags** = `0` [🔗<class_RDAttachmentFormat_property_usage_flags>]


- |void| **set_usage_flags**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_usage_flags**\ (\ )

The attachment's usage flags, which determine what can be done with it.

