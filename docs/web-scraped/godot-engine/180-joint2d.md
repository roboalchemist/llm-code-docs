# Joint2D

# Joint2D
Inherits:Node2D<CanvasItem<Node<Object
Inherited By:DampedSpringJoint2D,GrooveJoint2D,PinJoint2D
Abstract base class for all 2D physics joints.

## Description
Abstract base class for all joints in 2D physics. 2D joints bind together two physics bodies (node_aandnode_b) and apply a constraint.

## Properties

| float | bias | 0.0 |
|---|---|---|
| bool | disable_collision | true |
| NodePath | node_a | NodePath("") |
| NodePath | node_b | NodePath("") |

float
bias
bool
disable_collision
true
NodePath
node_a
NodePath("")
NodePath
node_b
NodePath("")

## Methods

| RID | get_rid()const |

get_rid()const

## Property Descriptions
floatbias=0.0🔗
- voidset_bias(value:float)
voidset_bias(value:float)
- floatget_bias()
floatget_bias()
Whennode_aandnode_bmove in different directions thebiascontrols how fast the joint pulls them back to their original position. The lower thebiasthe more the two bodies can pull on the joint.
When set to0, the default value fromProjectSettings.physics/2d/solver/default_constraint_biasis used.
booldisable_collision=true🔗
- voidset_exclude_nodes_from_collision(value:bool)
voidset_exclude_nodes_from_collision(value:bool)
- boolget_exclude_nodes_from_collision()
boolget_exclude_nodes_from_collision()
Iftrue, the two bodies bound together do not collide with each other.
NodePathnode_a=NodePath("")🔗
- voidset_node_a(value:NodePath)
voidset_node_a(value:NodePath)
- NodePathget_node_a()
NodePathget_node_a()
Path to the first body (A) attached to the joint. The node must inheritPhysicsBody2D.
NodePathnode_b=NodePath("")🔗
- voidset_node_b(value:NodePath)
voidset_node_b(value:NodePath)
- NodePathget_node_b()
NodePathget_node_b()
Path to the second body (B) attached to the joint. The node must inheritPhysicsBody2D.

## Method Descriptions
RIDget_rid()const🔗
Returns the joint's internalRIDfrom thePhysicsServer2D.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.