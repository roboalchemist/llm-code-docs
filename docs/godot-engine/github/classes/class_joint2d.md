:github_url: hide



# Joint2D

**Inherits:** [Node2D<class_Node2D>] **<** [CanvasItem<class_CanvasItem>] **<** [Node<class_Node>] **<** [Object<class_Object>]

**Inherited By:** [DampedSpringJoint2D<class_DampedSpringJoint2D>], [GrooveJoint2D<class_GrooveJoint2D>], [PinJoint2D<class_PinJoint2D>]

Abstract base class for all 2D physics joints.


## Description

Abstract base class for all joints in 2D physics. 2D joints bind together two physics bodies ([node_a<class_Joint2D_property_node_a>] and [node_b<class_Joint2D_property_node_b>]) and apply a constraint.


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------------+--------------------------------------------------------------------+------------------+
> | :ref:`float<class_float>`       | :ref:`bias<class_Joint2D_property_bias>`                           | ``0.0``          |
> +---------------------------------+--------------------------------------------------------------------+------------------+
> | :ref:`bool<class_bool>`         | :ref:`disable_collision<class_Joint2D_property_disable_collision>` | ``true``         |
> +---------------------------------+--------------------------------------------------------------------+------------------+
> | :ref:`NodePath<class_NodePath>` | :ref:`node_a<class_Joint2D_property_node_a>`                       | ``NodePath("")`` |
> +---------------------------------+--------------------------------------------------------------------+------------------+
> | :ref:`NodePath<class_NodePath>` | :ref:`node_b<class_Joint2D_property_node_b>`                       | ``NodePath("")`` |
> +---------------------------------+--------------------------------------------------------------------+------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +-----------------------+------------------------------------------------------------+
> | :ref:`RID<class_RID>` | :ref:`get_rid<class_Joint2D_method_get_rid>`\ (\ ) |const| |
> +-----------------------+------------------------------------------------------------+
>

----


## Property Descriptions



[float<class_float>] **bias** = `0.0` [🔗<class_Joint2D_property_bias>]


- |void| **set_bias**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_bias**\ (\ )

When [node_a<class_Joint2D_property_node_a>] and [node_b<class_Joint2D_property_node_b>] move in different directions the [bias<class_Joint2D_property_bias>] controls how fast the joint pulls them back to their original position. The lower the [bias<class_Joint2D_property_bias>] the more the two bodies can pull on the joint.

When set to `0`, the default value from [ProjectSettings.physics/2d/solver/default_constraint_bias<class_ProjectSettings_property_physics/2d/solver/default_constraint_bias>] is used.


----



[bool<class_bool>] **disable_collision** = `true` [🔗<class_Joint2D_property_disable_collision>]


- |void| **set_exclude_nodes_from_collision**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_exclude_nodes_from_collision**\ (\ )

If `true`, the two bodies bound together do not collide with each other.


----



[NodePath<class_NodePath>] **node_a** = `NodePath("")` [🔗<class_Joint2D_property_node_a>]


- |void| **set_node_a**\ (\ value\: [NodePath<class_NodePath>]\ )
- [NodePath<class_NodePath>] **get_node_a**\ (\ )

Path to the first body (A) attached to the joint. The node must inherit [PhysicsBody2D<class_PhysicsBody2D>].


----



[NodePath<class_NodePath>] **node_b** = `NodePath("")` [🔗<class_Joint2D_property_node_b>]


- |void| **set_node_b**\ (\ value\: [NodePath<class_NodePath>]\ )
- [NodePath<class_NodePath>] **get_node_b**\ (\ )

Path to the second body (B) attached to the joint. The node must inherit [PhysicsBody2D<class_PhysicsBody2D>].


----


## Method Descriptions



[RID<class_RID>] **get_rid**\ (\ ) |const| [🔗<class_Joint2D_method_get_rid>]

Returns the joint's internal [RID<class_RID>] from the [PhysicsServer2D<class_PhysicsServer2D>].

