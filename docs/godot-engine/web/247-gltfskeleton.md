# GLTFSkeleton

# GLTFSkeleton
Inherits:Resource<RefCounted<Object
There is currently no description for this class. Please help us bycontributing one!

## Tutorials
- Runtime file loading and saving
Runtime file loading and saving

## Properties

| PackedInt32Array | joints | PackedInt32Array() |
|---|---|---|
| PackedInt32Array | roots | PackedInt32Array() |

PackedInt32Array
joints
PackedInt32Array()
PackedInt32Array
roots
PackedInt32Array()

## Methods

| BoneAttachment3D | get_bone_attachment(idx:int) |
|---|---|
| int | get_bone_attachment_count() |
| Dictionary | get_godot_bone_node() |
| Skeleton3D | get_godot_skeleton() |
| Array[String] | get_unique_names() |
| void | set_godot_bone_node(godot_bone_node:Dictionary) |
| void | set_unique_names(unique_names:Array[String]) |

BoneAttachment3D
get_bone_attachment(idx:int)
get_bone_attachment_count()
Dictionary
get_godot_bone_node()
Skeleton3D
get_godot_skeleton()
Array[String]
get_unique_names()
void
set_godot_bone_node(godot_bone_node:Dictionary)
void
set_unique_names(unique_names:Array[String])

## Property Descriptions
PackedInt32Arrayjoints=PackedInt32Array()🔗
- voidset_joints(value:PackedInt32Array)
voidset_joints(value:PackedInt32Array)
- PackedInt32Arrayget_joints()
PackedInt32Arrayget_joints()
There is currently no description for this property. Please help us bycontributing one!
Note:The returned array iscopiedand any changes to it will not update the original property value. SeePackedInt32Arrayfor more details.
PackedInt32Arrayroots=PackedInt32Array()🔗
- voidset_roots(value:PackedInt32Array)
voidset_roots(value:PackedInt32Array)
- PackedInt32Arrayget_roots()
PackedInt32Arrayget_roots()
There is currently no description for this property. Please help us bycontributing one!
Note:The returned array iscopiedand any changes to it will not update the original property value. SeePackedInt32Arrayfor more details.

## Method Descriptions
BoneAttachment3Dget_bone_attachment(idx:int)🔗
There is currently no description for this method. Please help us bycontributing one!
intget_bone_attachment_count()🔗
There is currently no description for this method. Please help us bycontributing one!
Dictionaryget_godot_bone_node()🔗
Returns aDictionarythat maps skeleton bone indices to the indices of glTF nodes. This property is unused during import, and only set during export. In a glTF file, a bone is a node, so Godot converts skeleton bones to glTF nodes.
Skeleton3Dget_godot_skeleton()🔗
There is currently no description for this method. Please help us bycontributing one!
Array[String]get_unique_names()🔗
There is currently no description for this method. Please help us bycontributing one!
voidset_godot_bone_node(godot_bone_node:Dictionary)🔗
Sets aDictionarythat maps skeleton bone indices to the indices of glTF nodes. This property is unused during import, and only set during export. In a glTF file, a bone is a node, so Godot converts skeleton bones to glTF nodes.
voidset_unique_names(unique_names:Array[String])🔗
There is currently no description for this method. Please help us bycontributing one!

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.