:github_url: hide

> **META**
	:keywords: spatial



# Node3D

**Inherits:** [Node<class_Node>] **<** [Object<class_Object>]

**Inherited By:** [AudioListener3D<class_AudioListener3D>], [AudioStreamPlayer3D<class_AudioStreamPlayer3D>], [BoneAttachment3D<class_BoneAttachment3D>], [Camera3D<class_Camera3D>], [CollisionObject3D<class_CollisionObject3D>], [CollisionPolygon3D<class_CollisionPolygon3D>], [CollisionShape3D<class_CollisionShape3D>], [GridMap<class_GridMap>], [ImporterMeshInstance3D<class_ImporterMeshInstance3D>], [Joint3D<class_Joint3D>], [LightmapProbe<class_LightmapProbe>], [Marker3D<class_Marker3D>], [NavigationLink3D<class_NavigationLink3D>], [NavigationObstacle3D<class_NavigationObstacle3D>], [NavigationRegion3D<class_NavigationRegion3D>], [OpenXRCompositionLayer<class_OpenXRCompositionLayer>], [OpenXRHand<class_OpenXRHand>], [OpenXRRenderModel<class_OpenXRRenderModel>], [OpenXRRenderModelManager<class_OpenXRRenderModelManager>], [Path3D<class_Path3D>], [PathFollow3D<class_PathFollow3D>], [RayCast3D<class_RayCast3D>], [RemoteTransform3D<class_RemoteTransform3D>], [ShapeCast3D<class_ShapeCast3D>], [Skeleton3D<class_Skeleton3D>], [SkeletonModifier3D<class_SkeletonModifier3D>], [SpringArm3D<class_SpringArm3D>], [SpringBoneCollision3D<class_SpringBoneCollision3D>], [VehicleWheel3D<class_VehicleWheel3D>], [VisualInstance3D<class_VisualInstance3D>], [XRFaceModifier3D<class_XRFaceModifier3D>], [XRNode3D<class_XRNode3D>], [XROrigin3D<class_XROrigin3D>]

Base object in 3D space, inherited by all 3D nodes.


## Description

The **Node3D** node is the base representation of a node in 3D space. All other 3D nodes inherit from this class.

Affine operations (translation, rotation, scale) are calculated in the coordinate system relative to the parent, unless the **Node3D**'s [top_level<class_Node3D_property_top_level>] is `true`. In this coordinate system, affine operations correspond to direct affine operations on the **Node3D**'s [transform<class_Node3D_property_transform>]. The term *parent space* refers to this coordinate system. The coordinate system that is attached to the **Node3D** itself is referred to as object-local coordinate system, or *local space*.

\ **Note:** Unless otherwise specified, all methods that need angle parameters must receive angles in *radians*. To convert degrees to radians, use [@GlobalScope.deg_to_rad()<class_@GlobalScope_method_deg_to_rad>].

\ **Note:** In Godot 3 and older, **Node3D** was named *Spatial*.


## Tutorials

- [../tutorials/3d/introduction_to_3d](Introduction to 3D .md)

- [All 3D Demos ](https://github.com/godotengine/godot-demo-projects/tree/master/3d)_


## Properties

> **TABLE**
> :widths: auto
>
> +-------------------------------------------------------+-------------------------------------------------------------------------------+-----------------------------------------------------+
> | :ref:`Basis<class_Basis>`                             | :ref:`basis<class_Node3D_property_basis>`                                     |                                                     |
> +-------------------------------------------------------+-------------------------------------------------------------------------------+-----------------------------------------------------+
> | :ref:`Basis<class_Basis>`                             | :ref:`global_basis<class_Node3D_property_global_basis>`                       |                                                     |
> +-------------------------------------------------------+-------------------------------------------------------------------------------+-----------------------------------------------------+
> | :ref:`Vector3<class_Vector3>`                         | :ref:`global_position<class_Node3D_property_global_position>`                 |                                                     |
> +-------------------------------------------------------+-------------------------------------------------------------------------------+-----------------------------------------------------+
> | :ref:`Vector3<class_Vector3>`                         | :ref:`global_rotation<class_Node3D_property_global_rotation>`                 |                                                     |
> +-------------------------------------------------------+-------------------------------------------------------------------------------+-----------------------------------------------------+
> | :ref:`Vector3<class_Vector3>`                         | :ref:`global_rotation_degrees<class_Node3D_property_global_rotation_degrees>` |                                                     |
> +-------------------------------------------------------+-------------------------------------------------------------------------------+-----------------------------------------------------+
> | :ref:`Transform3D<class_Transform3D>`                 | :ref:`global_transform<class_Node3D_property_global_transform>`               |                                                     |
> +-------------------------------------------------------+-------------------------------------------------------------------------------+-----------------------------------------------------+
> | :ref:`Vector3<class_Vector3>`                         | :ref:`position<class_Node3D_property_position>`                               | ``Vector3(0, 0, 0)``                                |
> +-------------------------------------------------------+-------------------------------------------------------------------------------+-----------------------------------------------------+
> | :ref:`Quaternion<class_Quaternion>`                   | :ref:`quaternion<class_Node3D_property_quaternion>`                           |                                                     |
> +-------------------------------------------------------+-------------------------------------------------------------------------------+-----------------------------------------------------+
> | :ref:`Vector3<class_Vector3>`                         | :ref:`rotation<class_Node3D_property_rotation>`                               | ``Vector3(0, 0, 0)``                                |
> +-------------------------------------------------------+-------------------------------------------------------------------------------+-----------------------------------------------------+
> | :ref:`Vector3<class_Vector3>`                         | :ref:`rotation_degrees<class_Node3D_property_rotation_degrees>`               |                                                     |
> +-------------------------------------------------------+-------------------------------------------------------------------------------+-----------------------------------------------------+
> | :ref:`RotationEditMode<enum_Node3D_RotationEditMode>` | :ref:`rotation_edit_mode<class_Node3D_property_rotation_edit_mode>`           | ``0``                                               |
> +-------------------------------------------------------+-------------------------------------------------------------------------------+-----------------------------------------------------+
> | :ref:`EulerOrder<enum_@GlobalScope_EulerOrder>`       | :ref:`rotation_order<class_Node3D_property_rotation_order>`                   | ``2``                                               |
> +-------------------------------------------------------+-------------------------------------------------------------------------------+-----------------------------------------------------+
> | :ref:`Vector3<class_Vector3>`                         | :ref:`scale<class_Node3D_property_scale>`                                     | ``Vector3(1, 1, 1)``                                |
> +-------------------------------------------------------+-------------------------------------------------------------------------------+-----------------------------------------------------+
> | :ref:`bool<class_bool>`                               | :ref:`top_level<class_Node3D_property_top_level>`                             | ``false``                                           |
> +-------------------------------------------------------+-------------------------------------------------------------------------------+-----------------------------------------------------+
> | :ref:`Transform3D<class_Transform3D>`                 | :ref:`transform<class_Node3D_property_transform>`                             | ``Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0)`` |
> +-------------------------------------------------------+-------------------------------------------------------------------------------+-----------------------------------------------------+
> | :ref:`NodePath<class_NodePath>`                       | :ref:`visibility_parent<class_Node3D_property_visibility_parent>`             | ``NodePath("")``                                    |
> +-------------------------------------------------------+-------------------------------------------------------------------------------+-----------------------------------------------------+
> | :ref:`bool<class_bool>`                               | :ref:`visible<class_Node3D_property_visible>`                                 | ``true``                                            |
> +-------------------------------------------------------+-------------------------------------------------------------------------------+-----------------------------------------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +--------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                             | :ref:`add_gizmo<class_Node3D_method_add_gizmo>`\ (\ gizmo\: :ref:`Node3DGizmo<class_Node3DGizmo>`\ )                                                                                                                                                                      |
> +--------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                             | :ref:`clear_gizmos<class_Node3D_method_clear_gizmos>`\ (\ )                                                                                                                                                                                                               |
> +--------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                             | :ref:`clear_subgizmo_selection<class_Node3D_method_clear_subgizmo_selection>`\ (\ )                                                                                                                                                                                       |
> +--------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                             | :ref:`force_update_transform<class_Node3D_method_force_update_transform>`\ (\ )                                                                                                                                                                                           |
> +--------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`\[:ref:`Node3DGizmo<class_Node3DGizmo>`\] | :ref:`get_gizmos<class_Node3D_method_get_gizmos>`\ (\ ) |const|                                                                                                                                                                                                           |
> +--------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Transform3D<class_Transform3D>`                              | :ref:`get_global_transform_interpolated<class_Node3D_method_get_global_transform_interpolated>`\ (\ )                                                                                                                                                                     |
> +--------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Node3D<class_Node3D>`                                        | :ref:`get_parent_node_3d<class_Node3D_method_get_parent_node_3d>`\ (\ ) |const|                                                                                                                                                                                           |
> +--------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`World3D<class_World3D>`                                      | :ref:`get_world_3d<class_Node3D_method_get_world_3d>`\ (\ ) |const|                                                                                                                                                                                                       |
> +--------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                             | :ref:`global_rotate<class_Node3D_method_global_rotate>`\ (\ axis\: :ref:`Vector3<class_Vector3>`, angle\: :ref:`float<class_float>`\ )                                                                                                                                    |
> +--------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                             | :ref:`global_scale<class_Node3D_method_global_scale>`\ (\ scale\: :ref:`Vector3<class_Vector3>`\ )                                                                                                                                                                        |
> +--------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                             | :ref:`global_translate<class_Node3D_method_global_translate>`\ (\ offset\: :ref:`Vector3<class_Vector3>`\ )                                                                                                                                                               |
> +--------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                             | :ref:`hide<class_Node3D_method_hide>`\ (\ )                                                                                                                                                                                                                               |
> +--------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                            | :ref:`is_local_transform_notification_enabled<class_Node3D_method_is_local_transform_notification_enabled>`\ (\ ) |const|                                                                                                                                                 |
> +--------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                            | :ref:`is_scale_disabled<class_Node3D_method_is_scale_disabled>`\ (\ ) |const|                                                                                                                                                                                             |
> +--------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                            | :ref:`is_transform_notification_enabled<class_Node3D_method_is_transform_notification_enabled>`\ (\ ) |const|                                                                                                                                                             |
> +--------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                            | :ref:`is_visible_in_tree<class_Node3D_method_is_visible_in_tree>`\ (\ ) |const|                                                                                                                                                                                           |
> +--------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                             | :ref:`look_at<class_Node3D_method_look_at>`\ (\ target\: :ref:`Vector3<class_Vector3>`, up\: :ref:`Vector3<class_Vector3>` = Vector3(0, 1, 0), use_model_front\: :ref:`bool<class_bool>` = false\ )                                                                       |
> +--------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                             | :ref:`look_at_from_position<class_Node3D_method_look_at_from_position>`\ (\ position\: :ref:`Vector3<class_Vector3>`, target\: :ref:`Vector3<class_Vector3>`, up\: :ref:`Vector3<class_Vector3>` = Vector3(0, 1, 0), use_model_front\: :ref:`bool<class_bool>` = false\ ) |
> +--------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                             | :ref:`orthonormalize<class_Node3D_method_orthonormalize>`\ (\ )                                                                                                                                                                                                           |
> +--------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                             | :ref:`rotate<class_Node3D_method_rotate>`\ (\ axis\: :ref:`Vector3<class_Vector3>`, angle\: :ref:`float<class_float>`\ )                                                                                                                                                  |
> +--------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                             | :ref:`rotate_object_local<class_Node3D_method_rotate_object_local>`\ (\ axis\: :ref:`Vector3<class_Vector3>`, angle\: :ref:`float<class_float>`\ )                                                                                                                        |
> +--------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                             | :ref:`rotate_x<class_Node3D_method_rotate_x>`\ (\ angle\: :ref:`float<class_float>`\ )                                                                                                                                                                                    |
> +--------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                             | :ref:`rotate_y<class_Node3D_method_rotate_y>`\ (\ angle\: :ref:`float<class_float>`\ )                                                                                                                                                                                    |
> +--------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                             | :ref:`rotate_z<class_Node3D_method_rotate_z>`\ (\ angle\: :ref:`float<class_float>`\ )                                                                                                                                                                                    |
> +--------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                             | :ref:`scale_object_local<class_Node3D_method_scale_object_local>`\ (\ scale\: :ref:`Vector3<class_Vector3>`\ )                                                                                                                                                            |
> +--------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                             | :ref:`set_disable_scale<class_Node3D_method_set_disable_scale>`\ (\ disable\: :ref:`bool<class_bool>`\ )                                                                                                                                                                  |
> +--------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                             | :ref:`set_identity<class_Node3D_method_set_identity>`\ (\ )                                                                                                                                                                                                               |
> +--------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                             | :ref:`set_ignore_transform_notification<class_Node3D_method_set_ignore_transform_notification>`\ (\ enabled\: :ref:`bool<class_bool>`\ )                                                                                                                                  |
> +--------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                             | :ref:`set_notify_local_transform<class_Node3D_method_set_notify_local_transform>`\ (\ enable\: :ref:`bool<class_bool>`\ )                                                                                                                                                 |
> +--------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                             | :ref:`set_notify_transform<class_Node3D_method_set_notify_transform>`\ (\ enable\: :ref:`bool<class_bool>`\ )                                                                                                                                                             |
> +--------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                             | :ref:`set_subgizmo_selection<class_Node3D_method_set_subgizmo_selection>`\ (\ gizmo\: :ref:`Node3DGizmo<class_Node3DGizmo>`, id\: :ref:`int<class_int>`, transform\: :ref:`Transform3D<class_Transform3D>`\ )                                                             |
> +--------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                             | :ref:`show<class_Node3D_method_show>`\ (\ )                                                                                                                                                                                                                               |
> +--------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector3<class_Vector3>`                                      | :ref:`to_global<class_Node3D_method_to_global>`\ (\ local_point\: :ref:`Vector3<class_Vector3>`\ ) |const|                                                                                                                                                                |
> +--------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector3<class_Vector3>`                                      | :ref:`to_local<class_Node3D_method_to_local>`\ (\ global_point\: :ref:`Vector3<class_Vector3>`\ ) |const|                                                                                                                                                                 |
> +--------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                             | :ref:`translate<class_Node3D_method_translate>`\ (\ offset\: :ref:`Vector3<class_Vector3>`\ )                                                                                                                                                                             |
> +--------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                             | :ref:`translate_object_local<class_Node3D_method_translate_object_local>`\ (\ offset\: :ref:`Vector3<class_Vector3>`\ )                                                                                                                                                   |
> +--------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                             | :ref:`update_gizmos<class_Node3D_method_update_gizmos>`\ (\ )                                                                                                                                                                                                             |
> +--------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Signals



**visibility_changed**\ (\ ) [🔗<class_Node3D_signal_visibility_changed>]

Emitted when this node's visibility changes (see [visible<class_Node3D_property_visible>] and [is_visible_in_tree()<class_Node3D_method_is_visible_in_tree>]).

This signal is emitted *after* the related [NOTIFICATION_VISIBILITY_CHANGED<class_Node3D_constant_NOTIFICATION_VISIBILITY_CHANGED>] notification.


----


## Enumerations



enum **RotationEditMode**: [🔗<enum_Node3D_RotationEditMode>]



[RotationEditMode<enum_Node3D_RotationEditMode>] **ROTATION_EDIT_MODE_EULER** = `0`

The rotation is edited using a [Vector3<class_Vector3>] in [Euler angles ](https://en.wikipedia.org/wiki/Euler_angles)_.



[RotationEditMode<enum_Node3D_RotationEditMode>] **ROTATION_EDIT_MODE_QUATERNION** = `1`

The rotation is edited using a [Quaternion<class_Quaternion>].



[RotationEditMode<enum_Node3D_RotationEditMode>] **ROTATION_EDIT_MODE_BASIS** = `2`

The rotation is edited using a [Basis<class_Basis>]. In this mode, the raw [basis<class_Node3D_property_basis>]'s axes can be freely modified, but the [scale<class_Node3D_property_scale>] property is not available.


----


## Constants



**NOTIFICATION_TRANSFORM_CHANGED** = `2000` [🔗<class_Node3D_constant_NOTIFICATION_TRANSFORM_CHANGED>]

Notification received when this node's [global_transform<class_Node3D_property_global_transform>] changes, if [is_transform_notification_enabled()<class_Node3D_method_is_transform_notification_enabled>] is `true`. See also [set_notify_transform()<class_Node3D_method_set_notify_transform>].

\ **Note:** Most 3D nodes such as [VisualInstance3D<class_VisualInstance3D>] or [CollisionObject3D<class_CollisionObject3D>] automatically enable this to function correctly.

\ **Note:** In the editor, nodes will propagate this notification to their children if a gizmo is attached (see [add_gizmo()<class_Node3D_method_add_gizmo>]).



**NOTIFICATION_ENTER_WORLD** = `41` [🔗<class_Node3D_constant_NOTIFICATION_ENTER_WORLD>]

Notification received when this node is registered to a new [World3D<class_World3D>] (see [get_world_3d()<class_Node3D_method_get_world_3d>]).



**NOTIFICATION_EXIT_WORLD** = `42` [🔗<class_Node3D_constant_NOTIFICATION_EXIT_WORLD>]

Notification received when this node is unregistered from the current [World3D<class_World3D>] (see [get_world_3d()<class_Node3D_method_get_world_3d>]).

This notification is sent in reversed order.



**NOTIFICATION_VISIBILITY_CHANGED** = `43` [🔗<class_Node3D_constant_NOTIFICATION_VISIBILITY_CHANGED>]

Notification received when this node's visibility changes (see [visible<class_Node3D_property_visible>] and [is_visible_in_tree()<class_Node3D_method_is_visible_in_tree>]).

This notification is received *before* the related [visibility_changed<class_Node3D_signal_visibility_changed>] signal.



**NOTIFICATION_LOCAL_TRANSFORM_CHANGED** = `44` [🔗<class_Node3D_constant_NOTIFICATION_LOCAL_TRANSFORM_CHANGED>]

Notification received when this node's [transform<class_Node3D_property_transform>] changes, if [is_local_transform_notification_enabled()<class_Node3D_method_is_local_transform_notification_enabled>] is `true`. This is not received when a parent **Node3D**'s [transform<class_Node3D_property_transform>] changes. See also [set_notify_local_transform()<class_Node3D_method_set_notify_local_transform>].

\ **Note:** Some 3D nodes such as [CSGShape3D<class_CSGShape3D>] or [CollisionShape3D<class_CollisionShape3D>] automatically enable this to function correctly.


----


## Property Descriptions



[Basis<class_Basis>] **basis** [🔗<class_Node3D_property_basis>]


- |void| **set_basis**\ (\ value\: [Basis<class_Basis>]\ )
- [Basis<class_Basis>] **get_basis**\ (\ )

Basis of the [transform<class_Node3D_property_transform>] property. Represents the rotation, scale, and shear of this node in parent space (relative to the parent node).


----



[Basis<class_Basis>] **global_basis** [🔗<class_Node3D_property_global_basis>]


- |void| **set_global_basis**\ (\ value\: [Basis<class_Basis>]\ )
- [Basis<class_Basis>] **get_global_basis**\ (\ )

Basis of the [global_transform<class_Node3D_property_global_transform>] property. Represents the rotation, scale, and shear of this node in global space (relative to the world).

\ **Note:** If the node is not inside the tree, getting this property fails and returns [Basis.IDENTITY<class_Basis_constant_IDENTITY>].


----



[Vector3<class_Vector3>] **global_position** [🔗<class_Node3D_property_global_position>]


- |void| **set_global_position**\ (\ value\: [Vector3<class_Vector3>]\ )
- [Vector3<class_Vector3>] **get_global_position**\ (\ )

Global position (translation) of this node in global space (relative to the world). This is equivalent to the [global_transform<class_Node3D_property_global_transform>]'s [Transform3D.origin<class_Transform3D_property_origin>].

\ **Note:** If the node is not inside the tree, getting this property fails and returns [Vector3.ZERO<class_Vector3_constant_ZERO>].


----



[Vector3<class_Vector3>] **global_rotation** [🔗<class_Node3D_property_global_rotation>]


- |void| **set_global_rotation**\ (\ value\: [Vector3<class_Vector3>]\ )
- [Vector3<class_Vector3>] **get_global_rotation**\ (\ )

Global rotation of this node as [Euler angles ](https://en.wikipedia.org/wiki/Euler_angles)_, in radians and in global space (relative to the world). This value is obtained from [global_basis<class_Node3D_property_global_basis>]'s rotation.

- The [Vector3.x<class_Vector3_property_x>] is the angle around the global X axis (pitch);

- The [Vector3.y<class_Vector3_property_y>] is the angle around the global Y axis (yaw);

- The [Vector3.z<class_Vector3_property_z>] is the angle around the global Z axis (roll).

\ **Note:** Unlike [rotation<class_Node3D_property_rotation>], this property always follows the YXZ convention ([@GlobalScope.EULER_ORDER_YXZ<class_@GlobalScope_constant_EULER_ORDER_YXZ>]).

\ **Note:** If the node is not inside the tree, getting this property fails and returns [Vector3.ZERO<class_Vector3_constant_ZERO>].


----



[Vector3<class_Vector3>] **global_rotation_degrees** [🔗<class_Node3D_property_global_rotation_degrees>]


- |void| **set_global_rotation_degrees**\ (\ value\: [Vector3<class_Vector3>]\ )
- [Vector3<class_Vector3>] **get_global_rotation_degrees**\ (\ )

The [global_rotation<class_Node3D_property_global_rotation>] of this node, in degrees instead of radians.

\ **Note:** If the node is not inside the tree, getting this property fails and returns [Vector3.ZERO<class_Vector3_constant_ZERO>].


----



[Transform3D<class_Transform3D>] **global_transform** [🔗<class_Node3D_property_global_transform>]


- |void| **set_global_transform**\ (\ value\: [Transform3D<class_Transform3D>]\ )
- [Transform3D<class_Transform3D>] **get_global_transform**\ (\ )

The transformation of this node, in global space (relative to the world). Contains and represents this node's [global_position<class_Node3D_property_global_position>], [global_rotation<class_Node3D_property_global_rotation>], and global scale.

\ **Note:** If the node is not inside the tree, getting this property fails and returns [Transform3D.IDENTITY<class_Transform3D_constant_IDENTITY>].


----



[Vector3<class_Vector3>] **position** = `Vector3(0, 0, 0)` [🔗<class_Node3D_property_position>]


- |void| **set_position**\ (\ value\: [Vector3<class_Vector3>]\ )
- [Vector3<class_Vector3>] **get_position**\ (\ )

Position (translation) of this node in parent space (relative to the parent node). This is equivalent to the [transform<class_Node3D_property_transform>]'s [Transform3D.origin<class_Transform3D_property_origin>].


----



[Quaternion<class_Quaternion>] **quaternion** [🔗<class_Node3D_property_quaternion>]


- |void| **set_quaternion**\ (\ value\: [Quaternion<class_Quaternion>]\ )
- [Quaternion<class_Quaternion>] **get_quaternion**\ (\ )

Rotation of this node represented as a [Quaternion<class_Quaternion>] in parent space (relative to the parent node). This value is obtained from [basis<class_Node3D_property_basis>]'s rotation.

\ **Note:** Quaternions are much more suitable for 3D math but are less intuitive. Setting this property can be useful for interpolation (see [Quaternion.slerp()<class_Quaternion_method_slerp>]).


----



[Vector3<class_Vector3>] **rotation** = `Vector3(0, 0, 0)` [🔗<class_Node3D_property_rotation>]


- |void| **set_rotation**\ (\ value\: [Vector3<class_Vector3>]\ )
- [Vector3<class_Vector3>] **get_rotation**\ (\ )

Rotation of this node as [Euler angles ](https://en.wikipedia.org/wiki/Euler_angles)_, in radians and in parent space (relative to the parent node). This value is obtained from [basis<class_Node3D_property_basis>]'s rotation.

- The [Vector3.x<class_Vector3_property_x>] is the angle around the local X axis (pitch);

- The [Vector3.y<class_Vector3_property_y>] is the angle around the local Y axis (yaw);

- The [Vector3.z<class_Vector3_property_z>] is the angle around the local Z axis (roll).

The order of each consecutive rotation can be changed with [rotation_order<class_Node3D_property_rotation_order>] (see [EulerOrder<enum_@GlobalScope_EulerOrder>] constants). By default, the YXZ convention is used ([@GlobalScope.EULER_ORDER_YXZ<class_@GlobalScope_constant_EULER_ORDER_YXZ>]).

\ **Note:** This property is edited in degrees in the inspector. If you want to use degrees in a script, use [rotation_degrees<class_Node3D_property_rotation_degrees>].


----



[Vector3<class_Vector3>] **rotation_degrees** [🔗<class_Node3D_property_rotation_degrees>]


- |void| **set_rotation_degrees**\ (\ value\: [Vector3<class_Vector3>]\ )
- [Vector3<class_Vector3>] **get_rotation_degrees**\ (\ )

The [rotation<class_Node3D_property_rotation>] of this node, in degrees instead of radians.

\ **Note:** This is **not** the property available in the Inspector dock.


----



[RotationEditMode<enum_Node3D_RotationEditMode>] **rotation_edit_mode** = `0` [🔗<class_Node3D_property_rotation_edit_mode>]


- |void| **set_rotation_edit_mode**\ (\ value\: [RotationEditMode<enum_Node3D_RotationEditMode>]\ )
- [RotationEditMode<enum_Node3D_RotationEditMode>] **get_rotation_edit_mode**\ (\ )

How this node's rotation and scale are displayed in the Inspector dock.


----



[EulerOrder<enum_@GlobalScope_EulerOrder>] **rotation_order** = `2` [🔗<class_Node3D_property_rotation_order>]


- |void| **set_rotation_order**\ (\ value\: [EulerOrder<enum_@GlobalScope_EulerOrder>]\ )
- [EulerOrder<enum_@GlobalScope_EulerOrder>] **get_rotation_order**\ (\ )

The axis rotation order of the [rotation<class_Node3D_property_rotation>] property. The final orientation is calculated by rotating around the local X, Y, and Z axis in this order.


----



[Vector3<class_Vector3>] **scale** = `Vector3(1, 1, 1)` [🔗<class_Node3D_property_scale>]


- |void| **set_scale**\ (\ value\: [Vector3<class_Vector3>]\ )
- [Vector3<class_Vector3>] **get_scale**\ (\ )

Scale of this node in local space (relative to this node). This value is obtained from [basis<class_Node3D_property_basis>]'s scale.

\ **Note:** The behavior of some 3D node types is not affected by this property. These include [Light3D<class_Light3D>], [Camera3D<class_Camera3D>], [AudioStreamPlayer3D<class_AudioStreamPlayer3D>], and more.

\ **Warning:** The scale's components must either be all positive or all negative, and **not** exactly `0.0`. Otherwise, it won't be possible to obtain the scale from the [basis<class_Node3D_property_basis>]. This may cause the intended scale to be lost when reloaded from disk, and potentially other unstable behavior.


----



[bool<class_bool>] **top_level** = `false` [🔗<class_Node3D_property_top_level>]


- |void| **set_as_top_level**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_set_as_top_level**\ (\ )

If `true`, the node does not inherit its transformations from its parent. As such, node transformations will only be in global space, which also means that [global_transform<class_Node3D_property_global_transform>] and [transform<class_Node3D_property_transform>] will be identical.


----



[Transform3D<class_Transform3D>] **transform** = `Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0)` [🔗<class_Node3D_property_transform>]


- |void| **set_transform**\ (\ value\: [Transform3D<class_Transform3D>]\ )
- [Transform3D<class_Transform3D>] **get_transform**\ (\ )

The local transformation of this node, in parent space (relative to the parent node). Contains and represents this node's [position<class_Node3D_property_position>], [rotation<class_Node3D_property_rotation>], and [scale<class_Node3D_property_scale>].


----



[NodePath<class_NodePath>] **visibility_parent** = `NodePath("")` [🔗<class_Node3D_property_visibility_parent>]


- |void| **set_visibility_parent**\ (\ value\: [NodePath<class_NodePath>]\ )
- [NodePath<class_NodePath>] **get_visibility_parent**\ (\ )

Path to the visibility range parent for this node and its descendants. The visibility parent must be a [GeometryInstance3D<class_GeometryInstance3D>].

Any visual instance will only be visible if the visibility parent (and all of its visibility ancestors) is hidden by being closer to the camera than its own [GeometryInstance3D.visibility_range_begin<class_GeometryInstance3D_property_visibility_range_begin>]. Nodes hidden via the [visible<class_Node3D_property_visible>] property are essentially removed from the visibility dependency tree, so dependent instances will not take the hidden node or its descendants into account.


----



[bool<class_bool>] **visible** = `true` [🔗<class_Node3D_property_visible>]


- |void| **set_visible**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_visible**\ (\ )

If `true`, this node can be visible. The node is only rendered when all of its ancestors are visible, as well. That means [is_visible_in_tree()<class_Node3D_method_is_visible_in_tree>] must return `true`.


----


## Method Descriptions



|void| **add_gizmo**\ (\ gizmo\: [Node3DGizmo<class_Node3DGizmo>]\ ) [🔗<class_Node3D_method_add_gizmo>]

Attaches the given `gizmo` to this node. Only works in the editor.

\ **Note:** `gizmo` should be an [EditorNode3DGizmo<class_EditorNode3DGizmo>]. The argument type is [Node3DGizmo<class_Node3DGizmo>] to avoid depending on editor classes in **Node3D**.


----



|void| **clear_gizmos**\ (\ ) [🔗<class_Node3D_method_clear_gizmos>]

Clears all [EditorNode3DGizmo<class_EditorNode3DGizmo>] objects attached to this node. Only works in the editor.


----



|void| **clear_subgizmo_selection**\ (\ ) [🔗<class_Node3D_method_clear_subgizmo_selection>]

Deselects all subgizmos for this node. Useful to call when the selected subgizmo may no longer exist after a property change. Only works in the editor.


----



|void| **force_update_transform**\ (\ ) [🔗<class_Node3D_method_force_update_transform>]

Forces the node's [global_transform<class_Node3D_property_global_transform>] to update, by sending [NOTIFICATION_TRANSFORM_CHANGED<class_Node3D_constant_NOTIFICATION_TRANSFORM_CHANGED>]. Fails if the node is not inside the tree.

\ **Note:** For performance reasons, transform changes are usually accumulated and applied *once* at the end of the frame. The update propagates through **Node3D** children, as well. Therefore, use this method only when you need an up-to-date transform (such as during physics operations).


----



[Array<class_Array>]\[[Node3DGizmo<class_Node3DGizmo>]\] **get_gizmos**\ (\ ) |const| [🔗<class_Node3D_method_get_gizmos>]

Returns all the [EditorNode3DGizmo<class_EditorNode3DGizmo>] objects attached to this node. Only works in the editor.


----



[Transform3D<class_Transform3D>] **get_global_transform_interpolated**\ (\ ) [🔗<class_Node3D_method_get_global_transform_interpolated>]

When using physics interpolation, there will be circumstances in which you want to know the interpolated (displayed) transform of a node rather than the standard transform (which may only be accurate to the most recent physics tick).

This is particularly important for frame-based operations that take place in [Node._process()<class_Node_private_method__process>], rather than [Node._physics_process()<class_Node_private_method__physics_process>]. Examples include [Camera3D<class_Camera3D>]\ s focusing on a node, or finding where to fire lasers from on a frame rather than physics tick.

\ **Note:** This function creates an interpolation pump on the **Node3D** the first time it is called, which can respond to physics interpolation resets. If you get problems with "streaking" when initially following a **Node3D**, be sure to call [get_global_transform_interpolated()<class_Node3D_method_get_global_transform_interpolated>] at least once *before* resetting the **Node3D** physics interpolation.


----



[Node3D<class_Node3D>] **get_parent_node_3d**\ (\ ) |const| [🔗<class_Node3D_method_get_parent_node_3d>]

Returns the parent **Node3D** that directly affects this node's [global_transform<class_Node3D_property_global_transform>]. Returns `null` if no parent exists, the parent is not a **Node3D**, or [top_level<class_Node3D_property_top_level>] is `true`.

\ **Note:** This method is not always equivalent to [Node.get_parent()<class_Node_method_get_parent>], which does not take [top_level<class_Node3D_property_top_level>] into account.


----



[World3D<class_World3D>] **get_world_3d**\ (\ ) |const| [🔗<class_Node3D_method_get_world_3d>]

Returns the [World3D<class_World3D>] this node is registered to.

Usually, this is the same as the world used by this node's viewport (see [Node.get_viewport()<class_Node_method_get_viewport>] and [Viewport.find_world_3d()<class_Viewport_method_find_world_3d>]).


----



|void| **global_rotate**\ (\ axis\: [Vector3<class_Vector3>], angle\: [float<class_float>]\ ) [🔗<class_Node3D_method_global_rotate>]

Rotates this node's [global_basis<class_Node3D_property_global_basis>] around the global `axis` by the given `angle`, in radians. This operation is calculated in global space (relative to the world) and preserves the [global_position<class_Node3D_property_global_position>].


----



|void| **global_scale**\ (\ scale\: [Vector3<class_Vector3>]\ ) [🔗<class_Node3D_method_global_scale>]

Scales this node's [global_basis<class_Node3D_property_global_basis>] by the given `scale` factor. This operation is calculated in global space (relative to the world) and preserves the [global_position<class_Node3D_property_global_position>].

\ **Note:** This method is not to be confused with the [scale<class_Node3D_property_scale>] property.


----



|void| **global_translate**\ (\ offset\: [Vector3<class_Vector3>]\ ) [🔗<class_Node3D_method_global_translate>]

Adds the given translation `offset` to the node's [global_position<class_Node3D_property_global_position>] in global space (relative to the world).


----



|void| **hide**\ (\ ) [🔗<class_Node3D_method_hide>]

Prevents this node from being rendered. Equivalent to setting [visible<class_Node3D_property_visible>] to `false`. This is the opposite of [show()<class_Node3D_method_show>].


----



[bool<class_bool>] **is_local_transform_notification_enabled**\ (\ ) |const| [🔗<class_Node3D_method_is_local_transform_notification_enabled>]

Returns `true` if the node receives [NOTIFICATION_LOCAL_TRANSFORM_CHANGED<class_Node3D_constant_NOTIFICATION_LOCAL_TRANSFORM_CHANGED>] whenever [transform<class_Node3D_property_transform>] changes. This is enabled with [set_notify_local_transform()<class_Node3D_method_set_notify_local_transform>].


----



[bool<class_bool>] **is_scale_disabled**\ (\ ) |const| [🔗<class_Node3D_method_is_scale_disabled>]

Returns `true` if this node's [global_transform<class_Node3D_property_global_transform>] is automatically orthonormalized. This results in this node not appearing distorted, as if its global scale were set to [Vector3.ONE<class_Vector3_constant_ONE>] (or its negative counterpart). See also [set_disable_scale()<class_Node3D_method_set_disable_scale>] and [orthonormalize()<class_Node3D_method_orthonormalize>].

\ **Note:** [transform<class_Node3D_property_transform>] is not affected by this setting.


----



[bool<class_bool>] **is_transform_notification_enabled**\ (\ ) |const| [🔗<class_Node3D_method_is_transform_notification_enabled>]

Returns `true` if the node receives [NOTIFICATION_TRANSFORM_CHANGED<class_Node3D_constant_NOTIFICATION_TRANSFORM_CHANGED>] whenever [global_transform<class_Node3D_property_global_transform>] changes. This is enabled with [set_notify_transform()<class_Node3D_method_set_notify_transform>].


----



[bool<class_bool>] **is_visible_in_tree**\ (\ ) |const| [🔗<class_Node3D_method_is_visible_in_tree>]

Returns `true` if this node is inside the scene tree and the [visible<class_Node3D_property_visible>] property is `true` for this node and all of its **Node3D** ancestors *in sequence*. An ancestor of any other type (such as [Node<class_Node>] or [Node2D<class_Node2D>]) breaks the sequence. See also [Node.get_parent()<class_Node_method_get_parent>].

\ **Note:** This method cannot take [VisualInstance3D.layers<class_VisualInstance3D_property_layers>] into account, so even if this method returns `true`, the node may not be rendered.


----



|void| **look_at**\ (\ target\: [Vector3<class_Vector3>], up\: [Vector3<class_Vector3>] = Vector3(0, 1, 0), use_model_front\: [bool<class_bool>] = false\ ) [🔗<class_Node3D_method_look_at>]

Rotates the node so that the local forward axis (-Z, [Vector3.FORWARD<class_Vector3_constant_FORWARD>]) points toward the `target` position. This operation is calculated in global space (relative to the world).

The local up axis (+Y) points as close to the `up` vector as possible while staying perpendicular to the local forward axis. The resulting transform is orthogonal, and the scale is preserved. Non-uniform scaling may not work correctly.

The `target` position cannot be the same as the node's position, the `up` vector cannot be [Vector3.ZERO<class_Vector3_constant_ZERO>]. Furthermore, the direction from the node's position to the `target` position cannot be parallel to the `up` vector, to avoid an unintended rotation around the local Z axis.

If `use_model_front` is `true`, the +Z axis (asset front) is treated as forward (implies +X is left) and points toward the `target` position. By default, the -Z axis (camera forward) is treated as forward (implies +X is right).

\ **Note:** This method fails if the node is not in the scene tree. If necessary, use [look_at_from_position()<class_Node3D_method_look_at_from_position>] instead.


----



|void| **look_at_from_position**\ (\ position\: [Vector3<class_Vector3>], target\: [Vector3<class_Vector3>], up\: [Vector3<class_Vector3>] = Vector3(0, 1, 0), use_model_front\: [bool<class_bool>] = false\ ) [🔗<class_Node3D_method_look_at_from_position>]

Moves the node to the specified `position`, then rotates the node to point toward the `target` position, similar to [look_at()<class_Node3D_method_look_at>]. This operation is calculated in global space (relative to the world).


----



|void| **orthonormalize**\ (\ ) [🔗<class_Node3D_method_orthonormalize>]

Orthonormalizes this node's [basis<class_Node3D_property_basis>]. This method sets this node's [scale<class_Node3D_property_scale>] to [Vector3.ONE<class_Vector3_constant_ONE>] (or its negative counterpart), but preserves the [position<class_Node3D_property_position>] and [rotation<class_Node3D_property_rotation>]. See also [Transform3D.orthonormalized()<class_Transform3D_method_orthonormalized>].


----



|void| **rotate**\ (\ axis\: [Vector3<class_Vector3>], angle\: [float<class_float>]\ ) [🔗<class_Node3D_method_rotate>]

Rotates this node's [basis<class_Node3D_property_basis>] around the `axis` by the given `angle`, in radians. This operation is calculated in parent space (relative to the parent) and preserves the [position<class_Node3D_property_position>].


----



|void| **rotate_object_local**\ (\ axis\: [Vector3<class_Vector3>], angle\: [float<class_float>]\ ) [🔗<class_Node3D_method_rotate_object_local>]

Rotates this node's [basis<class_Node3D_property_basis>] around the `axis` by the given `angle`, in radians. This operation is calculated in local space (relative to this node) and preserves the [position<class_Node3D_property_position>].


----



|void| **rotate_x**\ (\ angle\: [float<class_float>]\ ) [🔗<class_Node3D_method_rotate_x>]

Rotates this node's [basis<class_Node3D_property_basis>] around the X axis by the given `angle`, in radians. This operation is calculated in parent space (relative to the parent) and preserves the [position<class_Node3D_property_position>].


----



|void| **rotate_y**\ (\ angle\: [float<class_float>]\ ) [🔗<class_Node3D_method_rotate_y>]

Rotates this node's [basis<class_Node3D_property_basis>] around the Y axis by the given `angle`, in radians. This operation is calculated in parent space (relative to the parent) and preserves the [position<class_Node3D_property_position>].


----



|void| **rotate_z**\ (\ angle\: [float<class_float>]\ ) [🔗<class_Node3D_method_rotate_z>]

Rotates this node's [basis<class_Node3D_property_basis>] around the Z axis by the given `angle`, in radians. This operation is calculated in parent space (relative to the parent) and preserves the [position<class_Node3D_property_position>].


----



|void| **scale_object_local**\ (\ scale\: [Vector3<class_Vector3>]\ ) [🔗<class_Node3D_method_scale_object_local>]

Scales this node's [basis<class_Node3D_property_basis>] by the given `scale` factor. This operation is calculated in local space (relative to this node) and preserves the [position<class_Node3D_property_position>].


----



|void| **set_disable_scale**\ (\ disable\: [bool<class_bool>]\ ) [🔗<class_Node3D_method_set_disable_scale>]

If `true`, this node's [global_transform<class_Node3D_property_global_transform>] is automatically orthonormalized. This results in this node not appearing distorted, as if its global scale were set to [Vector3.ONE<class_Vector3_constant_ONE>] (or its negative counterpart). See also [is_scale_disabled()<class_Node3D_method_is_scale_disabled>] and [orthonormalize()<class_Node3D_method_orthonormalize>].

\ **Note:** [transform<class_Node3D_property_transform>] is not affected by this setting.


----



|void| **set_identity**\ (\ ) [🔗<class_Node3D_method_set_identity>]

Sets this node's [transform<class_Node3D_property_transform>] to [Transform3D.IDENTITY<class_Transform3D_constant_IDENTITY>], which resets all transformations in parent space ([position<class_Node3D_property_position>], [rotation<class_Node3D_property_rotation>], and [scale<class_Node3D_property_scale>]).


----



|void| **set_ignore_transform_notification**\ (\ enabled\: [bool<class_bool>]\ ) [🔗<class_Node3D_method_set_ignore_transform_notification>]

If `true`, the node will not receive [NOTIFICATION_TRANSFORM_CHANGED<class_Node3D_constant_NOTIFICATION_TRANSFORM_CHANGED>] or [NOTIFICATION_LOCAL_TRANSFORM_CHANGED<class_Node3D_constant_NOTIFICATION_LOCAL_TRANSFORM_CHANGED>].

It may useful to call this method when handling these notifications to prevent infinite recursion.


----



|void| **set_notify_local_transform**\ (\ enable\: [bool<class_bool>]\ ) [🔗<class_Node3D_method_set_notify_local_transform>]

If `true`, the node will receive [NOTIFICATION_LOCAL_TRANSFORM_CHANGED<class_Node3D_constant_NOTIFICATION_LOCAL_TRANSFORM_CHANGED>] whenever [transform<class_Node3D_property_transform>] changes.

\ **Note:** Some 3D nodes such as [CSGShape3D<class_CSGShape3D>] or [CollisionShape3D<class_CollisionShape3D>] automatically enable this to function correctly.


----



|void| **set_notify_transform**\ (\ enable\: [bool<class_bool>]\ ) [🔗<class_Node3D_method_set_notify_transform>]

If `true`, the node will receive [NOTIFICATION_TRANSFORM_CHANGED<class_Node3D_constant_NOTIFICATION_TRANSFORM_CHANGED>] whenever [global_transform<class_Node3D_property_global_transform>] changes.

\ **Note:** Most 3D nodes such as [VisualInstance3D<class_VisualInstance3D>] or [CollisionObject3D<class_CollisionObject3D>] automatically enable this to function correctly.

\ **Note:** In the editor, nodes will propagate this notification to their children if a gizmo is attached (see [add_gizmo()<class_Node3D_method_add_gizmo>]).


----



|void| **set_subgizmo_selection**\ (\ gizmo\: [Node3DGizmo<class_Node3DGizmo>], id\: [int<class_int>], transform\: [Transform3D<class_Transform3D>]\ ) [🔗<class_Node3D_method_set_subgizmo_selection>]

Selects the `gizmo`'s subgizmo with the given `id` and sets its transform. Only works in the editor.

\ **Note:** The gizmo object would typically be an instance of [EditorNode3DGizmo<class_EditorNode3DGizmo>], but the argument type is kept generic to avoid creating a dependency on editor classes in **Node3D**.


----



|void| **show**\ (\ ) [🔗<class_Node3D_method_show>]

Allows this node to be rendered. Equivalent to setting [visible<class_Node3D_property_visible>] to `true`. This is the opposite of [hide()<class_Node3D_method_hide>].


----



[Vector3<class_Vector3>] **to_global**\ (\ local_point\: [Vector3<class_Vector3>]\ ) |const| [🔗<class_Node3D_method_to_global>]

Returns the `local_point` converted from this node's local space to global space. This is the opposite of [to_local()<class_Node3D_method_to_local>].


----



[Vector3<class_Vector3>] **to_local**\ (\ global_point\: [Vector3<class_Vector3>]\ ) |const| [🔗<class_Node3D_method_to_local>]

Returns the `global_point` converted from global space to this node's local space. This is the opposite of [to_global()<class_Node3D_method_to_global>].


----



|void| **translate**\ (\ offset\: [Vector3<class_Vector3>]\ ) [🔗<class_Node3D_method_translate>]

Adds the given translation `offset` to the node's position, in local space (relative to this node).

\ **Note:** Prefer using [translate_object_local()<class_Node3D_method_translate_object_local>], instead, as this method may be changed in a future release.

\ **Note:** Despite the naming convention, this operation is **not** calculated in parent space for compatibility reasons. To translate in parent space, add `offset` to the [position<class_Node3D_property_position>] (`node_3d.position += offset`).


----



|void| **translate_object_local**\ (\ offset\: [Vector3<class_Vector3>]\ ) [🔗<class_Node3D_method_translate_object_local>]

Adds the given translation `offset` to the node's position, in local space (relative to this node).


----



|void| **update_gizmos**\ (\ ) [🔗<class_Node3D_method_update_gizmos>]

Updates all the [EditorNode3DGizmo<class_EditorNode3DGizmo>] objects attached to this node. Only works in the editor.

