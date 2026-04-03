# OpenXRIPBinding in English

# OpenXRIPBinding
Inherits:Resource<RefCounted<Object
Defines a binding between anOpenXRActionand an XR input or output.

## Description
This binding resource binds anOpenXRActionto an input or output. As most controllers have left hand and right versions that are handled by the same interaction profile we can specify multiple bindings. For instance an action "Fire" could be bound to both "/user/hand/left/input/trigger" and "/user/hand/right/input/trigger". This would require two binding entries.

## Properties

| OpenXRAction | action |  |
|---|---|---|
| Array | binding_modifiers | [] |
| String | binding_path | "" |
| PackedStringArray | paths |  |

OpenXRAction
action
Array
binding_modifiers
String
binding_path
PackedStringArray
paths

## Methods

| void | add_path(path:String) |
|---|---|
| OpenXRActionBindingModifier | get_binding_modifier(index:int)const |
| int | get_binding_modifier_count()const |
| int | get_path_count()const |
| bool | has_path(path:String)const |
| void | remove_path(path:String) |

void
add_path(path:String)
OpenXRActionBindingModifier
get_binding_modifier(index:int)const
get_binding_modifier_count()const
get_path_count()const
bool
has_path(path:String)const
void
remove_path(path:String)

## Property Descriptions
OpenXRActionaction🔗
- voidset_action(value:OpenXRAction)
voidset_action(value:OpenXRAction)
- OpenXRActionget_action()
OpenXRActionget_action()
OpenXRActionthat is bound tobinding_path.
Arraybinding_modifiers=[]🔗
- voidset_binding_modifiers(value:Array)
voidset_binding_modifiers(value:Array)
- Arrayget_binding_modifiers()
Arrayget_binding_modifiers()
Binding modifiers for this binding.
Stringbinding_path=""🔗
- voidset_binding_path(value:String)
voidset_binding_path(value:String)
- Stringget_binding_path()
Stringget_binding_path()
Binding path that defines the input or output bound toaction.
Note:Binding paths are suggestions, an XR runtime may choose to bind the action to a different input or output emulating this input or output.
PackedStringArraypaths🔗
- voidset_paths(value:PackedStringArray)
voidset_paths(value:PackedStringArray)
- PackedStringArrayget_paths()
PackedStringArrayget_paths()
Deprecated:Usebinding_pathinstead.
Paths that define the inputs or outputs bound on the device.
Note:The returned array iscopiedand any changes to it will not update the original property value. SeePackedStringArrayfor more details.

## Method Descriptions
voidadd_path(path:String)🔗
Deprecated:Binding is for a single path.
Add an input/output path to this binding.
OpenXRActionBindingModifierget_binding_modifier(index:int)const🔗
Get theOpenXRBindingModifierat this index.
intget_binding_modifier_count()const🔗
Get the number of binding modifiers for this binding.
intget_path_count()const🔗
Deprecated:Binding is for a single path.
Get the number of input/output paths in this binding.
boolhas_path(path:String)const🔗
Deprecated:Binding is for a single path.
Returnstrueif this input/output path is part of this binding.
voidremove_path(path:String)🔗
Deprecated:Binding is for a single path.
Removes this input/output path from this binding.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.