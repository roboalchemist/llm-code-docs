:github_url: hide



# EncodedObjectAsID

**Inherits:** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Holds a reference to an [Object<class_Object>]'s instance ID.


## Description

Utility class which holds a reference to the internal identifier of an [Object<class_Object>] instance, as given by [Object.get_instance_id()<class_Object_method_get_instance_id>]. This ID can then be used to retrieve the object instance with [@GlobalScope.instance_from_id()<class_@GlobalScope_method_instance_from_id>].

This class is used internally by the editor inspector and script debugger, but can also be used in plugins to pass and display objects as their IDs.


## Properties

> **TABLE**
> :widths: auto
>
> +-----------------------+--------------------------------------------------------------+-------+
> | :ref:`int<class_int>` | :ref:`object_id<class_EncodedObjectAsID_property_object_id>` | ``0`` |
> +-----------------------+--------------------------------------------------------------+-------+
>

----


## Property Descriptions



[int<class_int>] **object_id** = `0` [🔗<class_EncodedObjectAsID_property_object_id>]


- |void| **set_object_id**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_object_id**\ (\ )

The [Object<class_Object>] identifier stored in this **EncodedObjectAsID** instance. The object instance can be retrieved with [@GlobalScope.instance_from_id()<class_@GlobalScope_method_instance_from_id>].

