:github_url: hide



# JavaObject

**Inherits:** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Represents an object from the Java Native Interface.


## Description

Represents an object from the Java Native Interface. It can be returned from Java methods called on [JavaClass<class_JavaClass>] or other **JavaObject**\ s. See [JavaClassWrapper<class_JavaClassWrapper>] for an example.

\ **Note:** This class only works on Android. On any other platform, this class does nothing.

\ **Note:** This class is not to be confused with [JavaScriptObject<class_JavaScriptObject>].


## Methods

> **TABLE**
> :widths: auto
>
> +-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
> | :ref:`JavaClass<class_JavaClass>` | :ref:`get_java_class<class_JavaObject_method_get_java_class>`\ (\ ) |const|                                                 |
> +-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`           | :ref:`has_java_method<class_JavaObject_method_has_java_method>`\ (\ method\: :ref:`StringName<class_StringName>`\ ) |const| |
> +-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
>

----


## Method Descriptions



[JavaClass<class_JavaClass>] **get_java_class**\ (\ ) |const| [🔗<class_JavaObject_method_get_java_class>]

Returns the [JavaClass<class_JavaClass>] that this object is an instance of.


----



[bool<class_bool>] **has_java_method**\ (\ method\: [StringName<class_StringName>]\ ) |const| [🔗<class_JavaObject_method_has_java_method>]

Returns `true` if the given `method` name exists in the object's Java methods.

