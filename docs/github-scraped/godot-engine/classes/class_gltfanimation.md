:github_url: hide



# GLTFAnimation

**Inherits:** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

> **CONTAINER**
>
	There is currently no description for this class. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


## Tutorials

- [../tutorials/io/runtime_file_loading_and_saving](Runtime file loading and saving .md)


## Properties

> **TABLE**
> :widths: auto
>
> +-----------------------------+------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>`     | :ref:`loop<class_GLTFAnimation_property_loop>`                   | ``false`` |
> +-----------------------------+------------------------------------------------------------------+-----------+
> | :ref:`String<class_String>` | :ref:`original_name<class_GLTFAnimation_property_original_name>` | ``""``    |
> +-----------------------------+------------------------------------------------------------------+-----------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Variant<class_Variant>` | :ref:`get_additional_data<class_GLTFAnimation_method_get_additional_data>`\ (\ extension_name\: :ref:`StringName<class_StringName>`\ )                                                  |
> +-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                        | :ref:`set_additional_data<class_GLTFAnimation_method_set_additional_data>`\ (\ extension_name\: :ref:`StringName<class_StringName>`, additional_data\: :ref:`Variant<class_Variant>`\ ) |
> +-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Property Descriptions



[bool<class_bool>] **loop** = `false` [🔗<class_GLTFAnimation_property_loop>]


- |void| **set_loop**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_loop**\ (\ )

> **CONTAINER**
>
	There is currently no description for this property. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[String<class_String>] **original_name** = `""` [🔗<class_GLTFAnimation_property_original_name>]


- |void| **set_original_name**\ (\ value\: [String<class_String>]\ )
- [String<class_String>] **get_original_name**\ (\ )

The original name of the animation.


----


## Method Descriptions



[Variant<class_Variant>] **get_additional_data**\ (\ extension_name\: [StringName<class_StringName>]\ ) [🔗<class_GLTFAnimation_method_get_additional_data>]

Gets additional arbitrary data in this **GLTFAnimation** instance. This can be used to keep per-node state data in [GLTFDocumentExtension<class_GLTFDocumentExtension>] classes, which is important because they are stateless.

The argument should be the [GLTFDocumentExtension<class_GLTFDocumentExtension>] name (does not have to match the extension name in the glTF file), and the return value can be anything you set. If nothing was set, the return value is `null`.


----



|void| **set_additional_data**\ (\ extension_name\: [StringName<class_StringName>], additional_data\: [Variant<class_Variant>]\ ) [🔗<class_GLTFAnimation_method_set_additional_data>]

Sets additional arbitrary data in this **GLTFAnimation** instance. This can be used to keep per-node state data in [GLTFDocumentExtension<class_GLTFDocumentExtension>] classes, which is important because they are stateless.

The first argument should be the [GLTFDocumentExtension<class_GLTFDocumentExtension>] name (does not have to match the extension name in the glTF file), and the second argument can be anything you want.

