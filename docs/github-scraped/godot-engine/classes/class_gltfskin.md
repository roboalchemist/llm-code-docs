:github_url: hide



# GLTFSkin

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
> +-------------------------------------------------+-----------------------------------------------------------------+------------------------+
> | :ref:`Skin<class_Skin>`                         | :ref:`godot_skin<class_GLTFSkin_property_godot_skin>`           |                        |
> +-------------------------------------------------+-----------------------------------------------------------------+------------------------+
> | :ref:`PackedInt32Array<class_PackedInt32Array>` | :ref:`joints<class_GLTFSkin_property_joints>`                   | ``PackedInt32Array()`` |
> +-------------------------------------------------+-----------------------------------------------------------------+------------------------+
> | :ref:`PackedInt32Array<class_PackedInt32Array>` | :ref:`joints_original<class_GLTFSkin_property_joints_original>` | ``PackedInt32Array()`` |
> +-------------------------------------------------+-----------------------------------------------------------------+------------------------+
> | :ref:`PackedInt32Array<class_PackedInt32Array>` | :ref:`non_joints<class_GLTFSkin_property_non_joints>`           | ``PackedInt32Array()`` |
> +-------------------------------------------------+-----------------------------------------------------------------+------------------------+
> | :ref:`PackedInt32Array<class_PackedInt32Array>` | :ref:`roots<class_GLTFSkin_property_roots>`                     | ``PackedInt32Array()`` |
> +-------------------------------------------------+-----------------------------------------------------------------+------------------------+
> | :ref:`int<class_int>`                           | :ref:`skeleton<class_GLTFSkin_property_skeleton>`               | ``-1``                 |
> +-------------------------------------------------+-----------------------------------------------------------------+------------------------+
> | :ref:`int<class_int>`                           | :ref:`skin_root<class_GLTFSkin_property_skin_root>`             | ``-1``                 |
> +-------------------------------------------------+-----------------------------------------------------------------+------------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +--------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`\[:ref:`Transform3D<class_Transform3D>`\] | :ref:`get_inverse_binds<class_GLTFSkin_method_get_inverse_binds>`\ (\ )                                                                                     |
> +--------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Dictionary<class_Dictionary>`                                | :ref:`get_joint_i_to_bone_i<class_GLTFSkin_method_get_joint_i_to_bone_i>`\ (\ )                                                                             |
> +--------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Dictionary<class_Dictionary>`                                | :ref:`get_joint_i_to_name<class_GLTFSkin_method_get_joint_i_to_name>`\ (\ )                                                                                 |
> +--------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                             | :ref:`set_inverse_binds<class_GLTFSkin_method_set_inverse_binds>`\ (\ inverse_binds\: :ref:`Array<class_Array>`\[:ref:`Transform3D<class_Transform3D>`\]\ ) |
> +--------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                             | :ref:`set_joint_i_to_bone_i<class_GLTFSkin_method_set_joint_i_to_bone_i>`\ (\ joint_i_to_bone_i\: :ref:`Dictionary<class_Dictionary>`\ )                    |
> +--------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                             | :ref:`set_joint_i_to_name<class_GLTFSkin_method_set_joint_i_to_name>`\ (\ joint_i_to_name\: :ref:`Dictionary<class_Dictionary>`\ )                          |
> +--------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Property Descriptions



[Skin<class_Skin>] **godot_skin** [🔗<class_GLTFSkin_property_godot_skin>]


- |void| **set_godot_skin**\ (\ value\: [Skin<class_Skin>]\ )
- [Skin<class_Skin>] **get_godot_skin**\ (\ )

> **CONTAINER**
>
	There is currently no description for this property. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[PackedInt32Array<class_PackedInt32Array>] **joints** = `PackedInt32Array()` [🔗<class_GLTFSkin_property_joints>]


- |void| **set_joints**\ (\ value\: [PackedInt32Array<class_PackedInt32Array>]\ )
- [PackedInt32Array<class_PackedInt32Array>] **get_joints**\ (\ )

> **CONTAINER**
>
	There is currently no description for this property. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedInt32Array<class_PackedInt32Array>] for more details.


----



[PackedInt32Array<class_PackedInt32Array>] **joints_original** = `PackedInt32Array()` [🔗<class_GLTFSkin_property_joints_original>]


- |void| **set_joints_original**\ (\ value\: [PackedInt32Array<class_PackedInt32Array>]\ )
- [PackedInt32Array<class_PackedInt32Array>] **get_joints_original**\ (\ )

> **CONTAINER**
>
	There is currently no description for this property. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedInt32Array<class_PackedInt32Array>] for more details.


----



[PackedInt32Array<class_PackedInt32Array>] **non_joints** = `PackedInt32Array()` [🔗<class_GLTFSkin_property_non_joints>]


- |void| **set_non_joints**\ (\ value\: [PackedInt32Array<class_PackedInt32Array>]\ )
- [PackedInt32Array<class_PackedInt32Array>] **get_non_joints**\ (\ )

> **CONTAINER**
>
	There is currently no description for this property. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedInt32Array<class_PackedInt32Array>] for more details.


----



[PackedInt32Array<class_PackedInt32Array>] **roots** = `PackedInt32Array()` [🔗<class_GLTFSkin_property_roots>]


- |void| **set_roots**\ (\ value\: [PackedInt32Array<class_PackedInt32Array>]\ )
- [PackedInt32Array<class_PackedInt32Array>] **get_roots**\ (\ )

> **CONTAINER**
>
	There is currently no description for this property. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedInt32Array<class_PackedInt32Array>] for more details.


----



[int<class_int>] **skeleton** = `-1` [🔗<class_GLTFSkin_property_skeleton>]


- |void| **set_skeleton**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_skeleton**\ (\ )

> **CONTAINER**
>
	There is currently no description for this property. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[int<class_int>] **skin_root** = `-1` [🔗<class_GLTFSkin_property_skin_root>]


- |void| **set_skin_root**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_skin_root**\ (\ )

> **CONTAINER**
>
	There is currently no description for this property. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----


## Method Descriptions



[Array<class_Array>]\[[Transform3D<class_Transform3D>]\] **get_inverse_binds**\ (\ ) [🔗<class_GLTFSkin_method_get_inverse_binds>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[Dictionary<class_Dictionary>] **get_joint_i_to_bone_i**\ (\ ) [🔗<class_GLTFSkin_method_get_joint_i_to_bone_i>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[Dictionary<class_Dictionary>] **get_joint_i_to_name**\ (\ ) [🔗<class_GLTFSkin_method_get_joint_i_to_name>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



|void| **set_inverse_binds**\ (\ inverse_binds\: [Array<class_Array>]\[[Transform3D<class_Transform3D>]\]\ ) [🔗<class_GLTFSkin_method_set_inverse_binds>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



|void| **set_joint_i_to_bone_i**\ (\ joint_i_to_bone_i\: [Dictionary<class_Dictionary>]\ ) [🔗<class_GLTFSkin_method_set_joint_i_to_bone_i>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



|void| **set_joint_i_to_name**\ (\ joint_i_to_name\: [Dictionary<class_Dictionary>]\ ) [🔗<class_GLTFSkin_method_set_joint_i_to_name>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!

