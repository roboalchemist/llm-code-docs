:github_url: hide



# JavaClass

**Inherits:** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Represents a class from the Java Native Interface.


## Description

Represents a class from the Java Native Interface. It is returned from [JavaClassWrapper.wrap()<class_JavaClassWrapper_method_wrap>].

\ **Note:** This class only works on Android. On any other platform, this class does nothing.

\ **Note:** This class is not to be confused with [JavaScriptObject<class_JavaScriptObject>].


## Methods

> **TABLE**
> :widths: auto
>
> +------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`                                      | :ref:`get_java_class_name<class_JavaClass_method_get_java_class_name>`\ (\ ) |const|                                       |
> +------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`\[:ref:`Dictionary<class_Dictionary>`\] | :ref:`get_java_method_list<class_JavaClass_method_get_java_method_list>`\ (\ ) |const|                                     |
> +------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
> | :ref:`JavaClass<class_JavaClass>`                                | :ref:`get_java_parent_class<class_JavaClass_method_get_java_parent_class>`\ (\ ) |const|                                   |
> +------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                          | :ref:`has_java_method<class_JavaClass_method_has_java_method>`\ (\ method\: :ref:`StringName<class_StringName>`\ ) |const| |
> +------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
>

----


## Method Descriptions



[String<class_String>] **get_java_class_name**\ (\ ) |const| [🔗<class_JavaClass_method_get_java_class_name>]

Returns the Java class name.


----



[Array<class_Array>]\[[Dictionary<class_Dictionary>]\] **get_java_method_list**\ (\ ) |const| [🔗<class_JavaClass_method_get_java_method_list>]

Returns the object's Java methods and their signatures as an [Array<class_Array>] of dictionaries, in the same format as [Object.get_method_list()<class_Object_method_get_method_list>].


----



[JavaClass<class_JavaClass>] **get_java_parent_class**\ (\ ) |const| [🔗<class_JavaClass_method_get_java_parent_class>]

Returns a **JavaClass** representing the Java parent class of this class.


----



[bool<class_bool>] **has_java_method**\ (\ method\: [StringName<class_StringName>]\ ) |const| [🔗<class_JavaClass_method_has_java_method>]

Returns `true` if the given `method` name exists in the object's Java methods.

