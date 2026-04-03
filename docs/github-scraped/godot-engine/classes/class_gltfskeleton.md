:github_url: hide



# GLTFSkeleton

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
> +-------------------------------------------------+---------------------------------------------------+------------------------+
> | :ref:`PackedInt32Array<class_PackedInt32Array>` | :ref:`joints<class_GLTFSkeleton_property_joints>` | ``PackedInt32Array()`` |
> +-------------------------------------------------+---------------------------------------------------+------------------------+
> | :ref:`PackedInt32Array<class_PackedInt32Array>` | :ref:`roots<class_GLTFSkeleton_property_roots>`   | ``PackedInt32Array()`` |
> +-------------------------------------------------+---------------------------------------------------+------------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +----------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`BoneAttachment3D<class_BoneAttachment3D>`          | :ref:`get_bone_attachment<class_GLTFSkeleton_method_get_bone_attachment>`\ (\ idx\: :ref:`int<class_int>`\ )                                       |
> +----------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                    | :ref:`get_bone_attachment_count<class_GLTFSkeleton_method_get_bone_attachment_count>`\ (\ )                                                        |
> +----------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Dictionary<class_Dictionary>`                      | :ref:`get_godot_bone_node<class_GLTFSkeleton_method_get_godot_bone_node>`\ (\ )                                                                    |
> +----------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Skeleton3D<class_Skeleton3D>`                      | :ref:`get_godot_skeleton<class_GLTFSkeleton_method_get_godot_skeleton>`\ (\ )                                                                      |
> +----------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`\[:ref:`String<class_String>`\] | :ref:`get_unique_names<class_GLTFSkeleton_method_get_unique_names>`\ (\ )                                                                          |
> +----------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                   | :ref:`set_godot_bone_node<class_GLTFSkeleton_method_set_godot_bone_node>`\ (\ godot_bone_node\: :ref:`Dictionary<class_Dictionary>`\ )             |
> +----------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                   | :ref:`set_unique_names<class_GLTFSkeleton_method_set_unique_names>`\ (\ unique_names\: :ref:`Array<class_Array>`\[:ref:`String<class_String>`\]\ ) |
> +----------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Property Descriptions



[PackedInt32Array<class_PackedInt32Array>] **joints** = `PackedInt32Array()` [🔗<class_GLTFSkeleton_property_joints>]


- |void| **set_joints**\ (\ value\: [PackedInt32Array<class_PackedInt32Array>]\ )
- [PackedInt32Array<class_PackedInt32Array>] **get_joints**\ (\ )

> **CONTAINER**
>
	There is currently no description for this property. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedInt32Array<class_PackedInt32Array>] for more details.


----



[PackedInt32Array<class_PackedInt32Array>] **roots** = `PackedInt32Array()` [🔗<class_GLTFSkeleton_property_roots>]


- |void| **set_roots**\ (\ value\: [PackedInt32Array<class_PackedInt32Array>]\ )
- [PackedInt32Array<class_PackedInt32Array>] **get_roots**\ (\ )

> **CONTAINER**
>
	There is currently no description for this property. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedInt32Array<class_PackedInt32Array>] for more details.


----


## Method Descriptions



[BoneAttachment3D<class_BoneAttachment3D>] **get_bone_attachment**\ (\ idx\: [int<class_int>]\ ) [🔗<class_GLTFSkeleton_method_get_bone_attachment>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[int<class_int>] **get_bone_attachment_count**\ (\ ) [🔗<class_GLTFSkeleton_method_get_bone_attachment_count>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[Dictionary<class_Dictionary>] **get_godot_bone_node**\ (\ ) [🔗<class_GLTFSkeleton_method_get_godot_bone_node>]

Returns a [Dictionary<class_Dictionary>] that maps skeleton bone indices to the indices of glTF nodes. This property is unused during import, and only set during export. In a glTF file, a bone is a node, so Godot converts skeleton bones to glTF nodes.


----



[Skeleton3D<class_Skeleton3D>] **get_godot_skeleton**\ (\ ) [🔗<class_GLTFSkeleton_method_get_godot_skeleton>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[Array<class_Array>]\[[String<class_String>]\] **get_unique_names**\ (\ ) [🔗<class_GLTFSkeleton_method_get_unique_names>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



|void| **set_godot_bone_node**\ (\ godot_bone_node\: [Dictionary<class_Dictionary>]\ ) [🔗<class_GLTFSkeleton_method_set_godot_bone_node>]

Sets a [Dictionary<class_Dictionary>] that maps skeleton bone indices to the indices of glTF nodes. This property is unused during import, and only set during export. In a glTF file, a bone is a node, so Godot converts skeleton bones to glTF nodes.


----



|void| **set_unique_names**\ (\ unique_names\: [Array<class_Array>]\[[String<class_String>]\]\ ) [🔗<class_GLTFSkeleton_method_set_unique_names>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!

