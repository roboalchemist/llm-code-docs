# PhysicalBone2D in English

# PhysicalBone2D
Inherits:RigidBody2D<PhysicsBody2D<CollisionObject2D<Node2D<CanvasItem<Node<Object
ARigidBody2D-derived node used to makeBone2Ds in aSkeleton2Dreact to physics.

## Description
ThePhysicalBone2Dnode is aRigidBody2D-based node that can be used to makeBone2Ds in aSkeleton2Dreact to physics.
Note:To make theBone2Ds visually follow thePhysicalBone2Dnode, use aSkeletonModification2DPhysicalBonesmodification on theSkeleton2Dparent.
Note:ThePhysicalBone2Dnode does not automatically create aJoint2Dnode to keepPhysicalBone2Dnodes together. They must be created manually. For most cases, you want to use aPinJoint2Dnode. ThePhysicalBone2Dnode will automatically configure theJoint2Dnode once it's been added as a child node.

## Properties

| bool | auto_configure_joint | true |
|---|---|---|
| int | bone2d_index | -1 |
| NodePath | bone2d_nodepath | NodePath("") |
| bool | follow_bone_when_simulating | false |
| bool | simulate_physics | false |

bool
auto_configure_joint
true
bone2d_index
NodePath
bone2d_nodepath
NodePath("")
bool
follow_bone_when_simulating
false
bool
simulate_physics
false

## Methods

| Joint2D | get_joint()const |
|---|---|
| bool | is_simulating_physics()const |

Joint2D
get_joint()const
bool
is_simulating_physics()const

## Property Descriptions
boolauto_configure_joint=true🔗
- voidset_auto_configure_joint(value:bool)
voidset_auto_configure_joint(value:bool)
- boolget_auto_configure_joint()
boolget_auto_configure_joint()
Iftrue, thePhysicalBone2Dwill automatically configure the firstJoint2Dchild node. The automatic configuration is limited to setting up the node properties and positioning theJoint2D.
intbone2d_index=-1🔗
- voidset_bone2d_index(value:int)
voidset_bone2d_index(value:int)
- intget_bone2d_index()
intget_bone2d_index()
The index of theBone2Dthat thisPhysicalBone2Dshould simulate.
NodePathbone2d_nodepath=NodePath("")🔗
- voidset_bone2d_nodepath(value:NodePath)
voidset_bone2d_nodepath(value:NodePath)
- NodePathget_bone2d_nodepath()
NodePathget_bone2d_nodepath()
TheNodePathto theBone2Dthat thisPhysicalBone2Dshould simulate.
boolfollow_bone_when_simulating=false🔗
- voidset_follow_bone_when_simulating(value:bool)
voidset_follow_bone_when_simulating(value:bool)
- boolget_follow_bone_when_simulating()
boolget_follow_bone_when_simulating()
Iftrue, thePhysicalBone2Dwill keep the transform of the bone it is bound to when simulating physics.
boolsimulate_physics=false🔗
- voidset_simulate_physics(value:bool)
voidset_simulate_physics(value:bool)
- boolget_simulate_physics()
boolget_simulate_physics()
Iftrue, thePhysicalBone2Dwill start simulating using physics. Iffalse, thePhysicalBone2Dwill follow the transform of theBone2Dnode.
Note:To have theBone2Ds visually follow thePhysicalBone2D, use aSkeletonModification2DPhysicalBonesmodification on theSkeleton2Dnode with theBone2Dnodes.

## Method Descriptions
Joint2Dget_joint()const🔗
Returns the firstJoint2Dchild node, if one exists. This is mainly a helper function to make it easier to get theJoint2Dthat thePhysicalBone2Dis autoconfiguring.
boolis_simulating_physics()const🔗
Returns a boolean that indicates whether thePhysicalBone2Dis running and simulating using the Godot 2D physics engine. Whentrue, the PhysicalBone2D node is using physics.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.