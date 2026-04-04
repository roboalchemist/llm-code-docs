:github_url: hide



# MissingResource

**Inherits:** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

An internal editor class intended for keeping the data of unrecognized resources.


## Description

This is an internal editor class intended for keeping data of resources of unknown type (most likely this type was supplied by an extension that is no longer loaded). It can't be manually instantiated or placed in a scene.

\ **Warning:** Ignore missing resources unless you know what you are doing. Existing properties on a missing resource can be freely modified in code, regardless of the type they are intended to be.


## Properties

> **TABLE**
> :widths: auto
>
> +-----------------------------+----------------------------------------------------------------------------------+
> | :ref:`String<class_String>` | :ref:`original_class<class_MissingResource_property_original_class>`             |
> +-----------------------------+----------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`     | :ref:`recording_properties<class_MissingResource_property_recording_properties>` |
> +-----------------------------+----------------------------------------------------------------------------------+
>

----


## Property Descriptions



[String<class_String>] **original_class** [🔗<class_MissingResource_property_original_class>]


- |void| **set_original_class**\ (\ value\: [String<class_String>]\ )
- [String<class_String>] **get_original_class**\ (\ )

The name of the class this resource was supposed to be (see [Object.get_class()<class_Object_method_get_class>]).


----



[bool<class_bool>] **recording_properties** [🔗<class_MissingResource_property_recording_properties>]


- |void| **set_recording_properties**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_recording_properties**\ (\ )

If set to `true`, allows new properties to be added on top of the existing ones with [Object.set()<class_Object_method_set>].

