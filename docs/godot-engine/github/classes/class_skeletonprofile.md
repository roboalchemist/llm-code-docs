:github_url: hide



# SkeletonProfile

**Inherits:** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

**Inherited By:** [SkeletonProfileHumanoid<class_SkeletonProfileHumanoid>]

Base class for a profile of a virtual skeleton used as a target for retargeting.


## Description

This resource is used in [EditorScenePostImport<class_EditorScenePostImport>]. Some parameters are referring to bones in [Skeleton3D<class_Skeleton3D>], [Skin<class_Skin>], [Animation<class_Animation>], and some other nodes are rewritten based on the parameters of **SkeletonProfile**.

\ **Note:** These parameters need to be set only when creating a custom profile. In [SkeletonProfileHumanoid<class_SkeletonProfileHumanoid>], they are defined internally as read-only values.


## Tutorials

- [../tutorials/assets_pipeline/retargeting_3d_skeletons](Retargeting 3D Skeletons .md)


## Properties

> **TABLE**
> :widths: auto
>
> +-------------------------------------+------------------------------------------------------------------------+---------+
> | :ref:`int<class_int>`               | :ref:`bone_size<class_SkeletonProfile_property_bone_size>`             | ``0``   |
> +-------------------------------------+------------------------------------------------------------------------+---------+
> | :ref:`int<class_int>`               | :ref:`group_size<class_SkeletonProfile_property_group_size>`           | ``0``   |
> +-------------------------------------+------------------------------------------------------------------------+---------+
> | :ref:`StringName<class_StringName>` | :ref:`root_bone<class_SkeletonProfile_property_root_bone>`             | ``&""`` |
> +-------------------------------------+------------------------------------------------------------------------+---------+
> | :ref:`StringName<class_StringName>` | :ref:`scale_base_bone<class_SkeletonProfile_property_scale_base_bone>` | ``&""`` |
> +-------------------------------------+------------------------------------------------------------------------+---------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +----------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                    | :ref:`find_bone<class_SkeletonProfile_method_find_bone>`\ (\ bone_name\: :ref:`StringName<class_StringName>`\ ) |const|                                                                       |
> +----------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`StringName<class_StringName>`                      | :ref:`get_bone_name<class_SkeletonProfile_method_get_bone_name>`\ (\ bone_idx\: :ref:`int<class_int>`\ ) |const|                                                                              |
> +----------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`StringName<class_StringName>`                      | :ref:`get_bone_parent<class_SkeletonProfile_method_get_bone_parent>`\ (\ bone_idx\: :ref:`int<class_int>`\ ) |const|                                                                          |
> +----------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`StringName<class_StringName>`                      | :ref:`get_bone_tail<class_SkeletonProfile_method_get_bone_tail>`\ (\ bone_idx\: :ref:`int<class_int>`\ ) |const|                                                                              |
> +----------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`StringName<class_StringName>`                      | :ref:`get_group<class_SkeletonProfile_method_get_group>`\ (\ bone_idx\: :ref:`int<class_int>`\ ) |const|                                                                                      |
> +----------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`StringName<class_StringName>`                      | :ref:`get_group_name<class_SkeletonProfile_method_get_group_name>`\ (\ group_idx\: :ref:`int<class_int>`\ ) |const|                                                                           |
> +----------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector2<class_Vector2>`                            | :ref:`get_handle_offset<class_SkeletonProfile_method_get_handle_offset>`\ (\ bone_idx\: :ref:`int<class_int>`\ ) |const|                                                                      |
> +----------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Transform3D<class_Transform3D>`                    | :ref:`get_reference_pose<class_SkeletonProfile_method_get_reference_pose>`\ (\ bone_idx\: :ref:`int<class_int>`\ ) |const|                                                                    |
> +----------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`TailDirection<enum_SkeletonProfile_TailDirection>` | :ref:`get_tail_direction<class_SkeletonProfile_method_get_tail_direction>`\ (\ bone_idx\: :ref:`int<class_int>`\ ) |const|                                                                    |
> +----------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Texture2D<class_Texture2D>`                        | :ref:`get_texture<class_SkeletonProfile_method_get_texture>`\ (\ group_idx\: :ref:`int<class_int>`\ ) |const|                                                                                 |
> +----------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                  | :ref:`is_required<class_SkeletonProfile_method_is_required>`\ (\ bone_idx\: :ref:`int<class_int>`\ ) |const|                                                                                  |
> +----------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                   | :ref:`set_bone_name<class_SkeletonProfile_method_set_bone_name>`\ (\ bone_idx\: :ref:`int<class_int>`, bone_name\: :ref:`StringName<class_StringName>`\ )                                     |
> +----------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                   | :ref:`set_bone_parent<class_SkeletonProfile_method_set_bone_parent>`\ (\ bone_idx\: :ref:`int<class_int>`, bone_parent\: :ref:`StringName<class_StringName>`\ )                               |
> +----------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                   | :ref:`set_bone_tail<class_SkeletonProfile_method_set_bone_tail>`\ (\ bone_idx\: :ref:`int<class_int>`, bone_tail\: :ref:`StringName<class_StringName>`\ )                                     |
> +----------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                   | :ref:`set_group<class_SkeletonProfile_method_set_group>`\ (\ bone_idx\: :ref:`int<class_int>`, group\: :ref:`StringName<class_StringName>`\ )                                                 |
> +----------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                   | :ref:`set_group_name<class_SkeletonProfile_method_set_group_name>`\ (\ group_idx\: :ref:`int<class_int>`, group_name\: :ref:`StringName<class_StringName>`\ )                                 |
> +----------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                   | :ref:`set_handle_offset<class_SkeletonProfile_method_set_handle_offset>`\ (\ bone_idx\: :ref:`int<class_int>`, handle_offset\: :ref:`Vector2<class_Vector2>`\ )                               |
> +----------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                   | :ref:`set_reference_pose<class_SkeletonProfile_method_set_reference_pose>`\ (\ bone_idx\: :ref:`int<class_int>`, bone_name\: :ref:`Transform3D<class_Transform3D>`\ )                         |
> +----------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                   | :ref:`set_required<class_SkeletonProfile_method_set_required>`\ (\ bone_idx\: :ref:`int<class_int>`, required\: :ref:`bool<class_bool>`\ )                                                    |
> +----------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                   | :ref:`set_tail_direction<class_SkeletonProfile_method_set_tail_direction>`\ (\ bone_idx\: :ref:`int<class_int>`, tail_direction\: :ref:`TailDirection<enum_SkeletonProfile_TailDirection>`\ ) |
> +----------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                   | :ref:`set_texture<class_SkeletonProfile_method_set_texture>`\ (\ group_idx\: :ref:`int<class_int>`, texture\: :ref:`Texture2D<class_Texture2D>`\ )                                            |
> +----------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Signals



**profile_updated**\ (\ ) [🔗<class_SkeletonProfile_signal_profile_updated>]

This signal is emitted when change the value in profile. This is used to update key name in the [BoneMap<class_BoneMap>] and to redraw the [BoneMap<class_BoneMap>] editor.

\ **Note:** This signal is not connected directly to editor to simplify the reference, instead it is passed on to editor through the [BoneMap<class_BoneMap>].


----


## Enumerations



enum **TailDirection**: [🔗<enum_SkeletonProfile_TailDirection>]



[TailDirection<enum_SkeletonProfile_TailDirection>] **TAIL_DIRECTION_AVERAGE_CHILDREN** = `0`

Direction to the average coordinates of bone children.



[TailDirection<enum_SkeletonProfile_TailDirection>] **TAIL_DIRECTION_SPECIFIC_CHILD** = `1`

Direction to the coordinates of specified bone child.



[TailDirection<enum_SkeletonProfile_TailDirection>] **TAIL_DIRECTION_END** = `2`

Direction is not calculated.


----


## Property Descriptions



[int<class_int>] **bone_size** = `0` [🔗<class_SkeletonProfile_property_bone_size>]


- |void| **set_bone_size**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_bone_size**\ (\ )

The amount of bones in retargeting section's [BoneMap<class_BoneMap>] editor. For example, [SkeletonProfileHumanoid<class_SkeletonProfileHumanoid>] has 56 bones.

The size of elements in [BoneMap<class_BoneMap>] updates when changing this property in it's assigned **SkeletonProfile**.


----



[int<class_int>] **group_size** = `0` [🔗<class_SkeletonProfile_property_group_size>]


- |void| **set_group_size**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_group_size**\ (\ )

The amount of groups of bones in retargeting section's [BoneMap<class_BoneMap>] editor. For example, [SkeletonProfileHumanoid<class_SkeletonProfileHumanoid>] has 4 groups.

This property exists to separate the bone list into several sections in the editor.


----



[StringName<class_StringName>] **root_bone** = `&""` [🔗<class_SkeletonProfile_property_root_bone>]


- |void| **set_root_bone**\ (\ value\: [StringName<class_StringName>]\ )
- [StringName<class_StringName>] **get_root_bone**\ (\ )

A bone name that will be used as the root bone in [AnimationTree<class_AnimationTree>]. This should be the bone of the parent of hips that exists at the world origin.


----



[StringName<class_StringName>] **scale_base_bone** = `&""` [🔗<class_SkeletonProfile_property_scale_base_bone>]


- |void| **set_scale_base_bone**\ (\ value\: [StringName<class_StringName>]\ )
- [StringName<class_StringName>] **get_scale_base_bone**\ (\ )

A bone name which will use model's height as the coefficient for normalization. For example, [SkeletonProfileHumanoid<class_SkeletonProfileHumanoid>] defines it as `Hips`.


----


## Method Descriptions



[int<class_int>] **find_bone**\ (\ bone_name\: [StringName<class_StringName>]\ ) |const| [🔗<class_SkeletonProfile_method_find_bone>]

Returns the bone index that matches `bone_name` as its name.


----



[StringName<class_StringName>] **get_bone_name**\ (\ bone_idx\: [int<class_int>]\ ) |const| [🔗<class_SkeletonProfile_method_get_bone_name>]

Returns the name of the bone at `bone_idx` that will be the key name in the [BoneMap<class_BoneMap>].

In the retargeting process, the returned bone name is the bone name of the target skeleton.


----



[StringName<class_StringName>] **get_bone_parent**\ (\ bone_idx\: [int<class_int>]\ ) |const| [🔗<class_SkeletonProfile_method_get_bone_parent>]

Returns the name of the bone which is the parent to the bone at `bone_idx`. The result is empty if the bone has no parent.


----



[StringName<class_StringName>] **get_bone_tail**\ (\ bone_idx\: [int<class_int>]\ ) |const| [🔗<class_SkeletonProfile_method_get_bone_tail>]

Returns the name of the bone which is the tail of the bone at `bone_idx`.


----



[StringName<class_StringName>] **get_group**\ (\ bone_idx\: [int<class_int>]\ ) |const| [🔗<class_SkeletonProfile_method_get_group>]

Returns the group of the bone at `bone_idx`.


----



[StringName<class_StringName>] **get_group_name**\ (\ group_idx\: [int<class_int>]\ ) |const| [🔗<class_SkeletonProfile_method_get_group_name>]

Returns the name of the group at `group_idx` that will be the drawing group in the [BoneMap<class_BoneMap>] editor.


----



[Vector2<class_Vector2>] **get_handle_offset**\ (\ bone_idx\: [int<class_int>]\ ) |const| [🔗<class_SkeletonProfile_method_get_handle_offset>]

Returns the offset of the bone at `bone_idx` that will be the button position in the [BoneMap<class_BoneMap>] editor.

This is the offset with origin at the top left corner of the square.


----



[Transform3D<class_Transform3D>] **get_reference_pose**\ (\ bone_idx\: [int<class_int>]\ ) |const| [🔗<class_SkeletonProfile_method_get_reference_pose>]

Returns the reference pose transform for bone `bone_idx`.


----



[TailDirection<enum_SkeletonProfile_TailDirection>] **get_tail_direction**\ (\ bone_idx\: [int<class_int>]\ ) |const| [🔗<class_SkeletonProfile_method_get_tail_direction>]

Returns the tail direction of the bone at `bone_idx`.


----



[Texture2D<class_Texture2D>] **get_texture**\ (\ group_idx\: [int<class_int>]\ ) |const| [🔗<class_SkeletonProfile_method_get_texture>]

Returns the texture of the group at `group_idx` that will be the drawing group background image in the [BoneMap<class_BoneMap>] editor.


----



[bool<class_bool>] **is_required**\ (\ bone_idx\: [int<class_int>]\ ) |const| [🔗<class_SkeletonProfile_method_is_required>]

Returns whether the bone at `bone_idx` is required for retargeting.

This value is used by the bone map editor. If this method returns `true`, and no bone is assigned, the handle color will be red on the bone map editor.


----



|void| **set_bone_name**\ (\ bone_idx\: [int<class_int>], bone_name\: [StringName<class_StringName>]\ ) [🔗<class_SkeletonProfile_method_set_bone_name>]

Sets the name of the bone at `bone_idx` that will be the key name in the [BoneMap<class_BoneMap>].

In the retargeting process, the setting bone name is the bone name of the target skeleton.


----



|void| **set_bone_parent**\ (\ bone_idx\: [int<class_int>], bone_parent\: [StringName<class_StringName>]\ ) [🔗<class_SkeletonProfile_method_set_bone_parent>]

Sets the bone with name `bone_parent` as the parent of the bone at `bone_idx`. If an empty string is passed, then the bone has no parent.


----



|void| **set_bone_tail**\ (\ bone_idx\: [int<class_int>], bone_tail\: [StringName<class_StringName>]\ ) [🔗<class_SkeletonProfile_method_set_bone_tail>]

Sets the bone with name `bone_tail` as the tail of the bone at `bone_idx`.


----



|void| **set_group**\ (\ bone_idx\: [int<class_int>], group\: [StringName<class_StringName>]\ ) [🔗<class_SkeletonProfile_method_set_group>]

Sets the group of the bone at `bone_idx`.


----



|void| **set_group_name**\ (\ group_idx\: [int<class_int>], group_name\: [StringName<class_StringName>]\ ) [🔗<class_SkeletonProfile_method_set_group_name>]

Sets the name of the group at `group_idx` that will be the drawing group in the [BoneMap<class_BoneMap>] editor.


----



|void| **set_handle_offset**\ (\ bone_idx\: [int<class_int>], handle_offset\: [Vector2<class_Vector2>]\ ) [🔗<class_SkeletonProfile_method_set_handle_offset>]

Sets the offset of the bone at `bone_idx` that will be the button position in the [BoneMap<class_BoneMap>] editor.

This is the offset with origin at the top left corner of the square.


----



|void| **set_reference_pose**\ (\ bone_idx\: [int<class_int>], bone_name\: [Transform3D<class_Transform3D>]\ ) [🔗<class_SkeletonProfile_method_set_reference_pose>]

Sets the reference pose transform for bone `bone_idx`.


----



|void| **set_required**\ (\ bone_idx\: [int<class_int>], required\: [bool<class_bool>]\ ) [🔗<class_SkeletonProfile_method_set_required>]

Sets the required status for bone `bone_idx` to `required`.


----



|void| **set_tail_direction**\ (\ bone_idx\: [int<class_int>], tail_direction\: [TailDirection<enum_SkeletonProfile_TailDirection>]\ ) [🔗<class_SkeletonProfile_method_set_tail_direction>]

Sets the tail direction of the bone at `bone_idx`.

\ **Note:** This only specifies the method of calculation. The actual coordinates required should be stored in an external skeleton, so the calculation itself needs to be done externally.


----



|void| **set_texture**\ (\ group_idx\: [int<class_int>], texture\: [Texture2D<class_Texture2D>]\ ) [🔗<class_SkeletonProfile_method_set_texture>]

Sets the texture of the group at `group_idx` that will be the drawing group background image in the [BoneMap<class_BoneMap>] editor.

