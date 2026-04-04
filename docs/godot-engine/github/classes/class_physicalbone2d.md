:github_url: hide

> **META**
	:keywords: ragdoll



# PhysicalBone2D

**Inherits:** [RigidBody2D<class_RigidBody2D>] **<** [PhysicsBody2D<class_PhysicsBody2D>] **<** [CollisionObject2D<class_CollisionObject2D>] **<** [Node2D<class_Node2D>] **<** [CanvasItem<class_CanvasItem>] **<** [Node<class_Node>] **<** [Object<class_Object>]

A [RigidBody2D<class_RigidBody2D>]-derived node used to make [Bone2D<class_Bone2D>]\ s in a [Skeleton2D<class_Skeleton2D>] react to physics.


## Description

The **PhysicalBone2D** node is a [RigidBody2D<class_RigidBody2D>]-based node that can be used to make [Bone2D<class_Bone2D>]\ s in a [Skeleton2D<class_Skeleton2D>] react to physics.

\ **Note:** To make the [Bone2D<class_Bone2D>]\ s visually follow the **PhysicalBone2D** node, use a [SkeletonModification2DPhysicalBones<class_SkeletonModification2DPhysicalBones>] modification on the [Skeleton2D<class_Skeleton2D>] parent.

\ **Note:** The **PhysicalBone2D** node does not automatically create a [Joint2D<class_Joint2D>] node to keep **PhysicalBone2D** nodes together. They must be created manually. For most cases, you want to use a [PinJoint2D<class_PinJoint2D>] node. The **PhysicalBone2D** node will automatically configure the [Joint2D<class_Joint2D>] node once it's been added as a child node.


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------------+-----------------------------------------------------------------------------------------------+------------------+
> | :ref:`bool<class_bool>`         | :ref:`auto_configure_joint<class_PhysicalBone2D_property_auto_configure_joint>`               | ``true``         |
> +---------------------------------+-----------------------------------------------------------------------------------------------+------------------+
> | :ref:`int<class_int>`           | :ref:`bone2d_index<class_PhysicalBone2D_property_bone2d_index>`                               | ``-1``           |
> +---------------------------------+-----------------------------------------------------------------------------------------------+------------------+
> | :ref:`NodePath<class_NodePath>` | :ref:`bone2d_nodepath<class_PhysicalBone2D_property_bone2d_nodepath>`                         | ``NodePath("")`` |
> +---------------------------------+-----------------------------------------------------------------------------------------------+------------------+
> | :ref:`bool<class_bool>`         | :ref:`follow_bone_when_simulating<class_PhysicalBone2D_property_follow_bone_when_simulating>` | ``false``        |
> +---------------------------------+-----------------------------------------------------------------------------------------------+------------------+
> | :ref:`bool<class_bool>`         | :ref:`simulate_physics<class_PhysicalBone2D_property_simulate_physics>`                       | ``false``        |
> +---------------------------------+-----------------------------------------------------------------------------------------------+------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +-------------------------------+-----------------------------------------------------------------------------------------------+
> | :ref:`Joint2D<class_Joint2D>` | :ref:`get_joint<class_PhysicalBone2D_method_get_joint>`\ (\ ) |const|                         |
> +-------------------------------+-----------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`       | :ref:`is_simulating_physics<class_PhysicalBone2D_method_is_simulating_physics>`\ (\ ) |const| |
> +-------------------------------+-----------------------------------------------------------------------------------------------+
>

----


## Property Descriptions



[bool<class_bool>] **auto_configure_joint** = `true` [🔗<class_PhysicalBone2D_property_auto_configure_joint>]


- |void| **set_auto_configure_joint**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_auto_configure_joint**\ (\ )

If `true`, the **PhysicalBone2D** will automatically configure the first [Joint2D<class_Joint2D>] child node. The automatic configuration is limited to setting up the node properties and positioning the [Joint2D<class_Joint2D>].


----



[int<class_int>] **bone2d_index** = `-1` [🔗<class_PhysicalBone2D_property_bone2d_index>]


- |void| **set_bone2d_index**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_bone2d_index**\ (\ )

The index of the [Bone2D<class_Bone2D>] that this **PhysicalBone2D** should simulate.


----



[NodePath<class_NodePath>] **bone2d_nodepath** = `NodePath("")` [🔗<class_PhysicalBone2D_property_bone2d_nodepath>]


- |void| **set_bone2d_nodepath**\ (\ value\: [NodePath<class_NodePath>]\ )
- [NodePath<class_NodePath>] **get_bone2d_nodepath**\ (\ )

The [NodePath<class_NodePath>] to the [Bone2D<class_Bone2D>] that this **PhysicalBone2D** should simulate.


----



[bool<class_bool>] **follow_bone_when_simulating** = `false` [🔗<class_PhysicalBone2D_property_follow_bone_when_simulating>]


- |void| **set_follow_bone_when_simulating**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_follow_bone_when_simulating**\ (\ )

If `true`, the **PhysicalBone2D** will keep the transform of the bone it is bound to when simulating physics.


----



[bool<class_bool>] **simulate_physics** = `false` [🔗<class_PhysicalBone2D_property_simulate_physics>]


- |void| **set_simulate_physics**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_simulate_physics**\ (\ )

If `true`, the **PhysicalBone2D** will start simulating using physics. If `false`, the **PhysicalBone2D** will follow the transform of the [Bone2D<class_Bone2D>] node.

\ **Note:** To have the [Bone2D<class_Bone2D>]\ s visually follow the **PhysicalBone2D**, use a [SkeletonModification2DPhysicalBones<class_SkeletonModification2DPhysicalBones>] modification on the [Skeleton2D<class_Skeleton2D>] node with the [Bone2D<class_Bone2D>] nodes.


----


## Method Descriptions



[Joint2D<class_Joint2D>] **get_joint**\ (\ ) |const| [🔗<class_PhysicalBone2D_method_get_joint>]

Returns the first [Joint2D<class_Joint2D>] child node, if one exists. This is mainly a helper function to make it easier to get the [Joint2D<class_Joint2D>] that the **PhysicalBone2D** is autoconfiguring.


----



[bool<class_bool>] **is_simulating_physics**\ (\ ) |const| [🔗<class_PhysicalBone2D_method_is_simulating_physics>]

Returns a boolean that indicates whether the **PhysicalBone2D** is running and simulating using the Godot 2D physics engine. When `true`, the PhysicalBone2D node is using physics.

