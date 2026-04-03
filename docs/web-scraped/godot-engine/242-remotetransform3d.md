# RemoteTransform3D

# RemoteTransform3D
Inherits:Node3D<Node<Object
RemoteTransform3D pushes its ownTransform3Dto anotherNode3Dderived Node in the scene.

## Description
RemoteTransform3D pushes its ownTransform3Dto anotherNode3Dderived Node (called the remote node) in the scene.
It can be set to update another Node's position, rotation and/or scale. It can use either global or local coordinates.

## Properties

| NodePath | remote_path | NodePath("") |
|---|---|---|
| bool | update_position | true |
| bool | update_rotation | true |
| bool | update_scale | true |
| bool | use_global_coordinates | true |

NodePath
remote_path
NodePath("")
bool
update_position
true
bool
update_rotation
true
bool
update_scale
true
bool
use_global_coordinates
true

## Methods

| void | force_update_cache() |

void
force_update_cache()

## Property Descriptions
NodePathremote_path=NodePath("")🔗
- voidset_remote_node(value:NodePath)
voidset_remote_node(value:NodePath)
- NodePathget_remote_node()
NodePathget_remote_node()
TheNodePathto the remote node, relative to the RemoteTransform3D's position in the scene.
boolupdate_position=true🔗
- voidset_update_position(value:bool)
voidset_update_position(value:bool)
- boolget_update_position()
boolget_update_position()
Iftrue, the remote node's position is updated.
boolupdate_rotation=true🔗
- voidset_update_rotation(value:bool)
voidset_update_rotation(value:bool)
- boolget_update_rotation()
boolget_update_rotation()
Iftrue, the remote node's rotation is updated.
boolupdate_scale=true🔗
- voidset_update_scale(value:bool)
voidset_update_scale(value:bool)
- boolget_update_scale()
boolget_update_scale()
Iftrue, the remote node's scale is updated.
booluse_global_coordinates=true🔗
- voidset_use_global_coordinates(value:bool)
voidset_use_global_coordinates(value:bool)
- boolget_use_global_coordinates()
boolget_use_global_coordinates()
Iftrue, global coordinates are used. Iffalse, local coordinates are used.

## Method Descriptions
voidforce_update_cache()🔗
RemoteTransform3Dcaches the remote node. It may not notice if the remote node disappears;force_update_cache()forces it to update the cache again.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.