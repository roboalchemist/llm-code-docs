# OpenXRInteractionProfile in English

# OpenXRInteractionProfile
Inherits:Resource<RefCounted<Object
Suggested bindings object for OpenXR.

## Description
This object stores suggested bindings for an interaction profile. Interaction profiles define the metadata for a tracked XR device such as an XR controller.
For more information see theinteraction profiles info in the OpenXR specification.

## Properties

| Array | binding_modifiers | [] |
|---|---|---|
| Array | bindings | [] |
| String | interaction_profile_path | "" |

Array
binding_modifiers
Array
bindings
String
interaction_profile_path

## Methods

| OpenXRIPBinding | get_binding(index:int)const |
|---|---|
| int | get_binding_count()const |
| OpenXRIPBindingModifier | get_binding_modifier(index:int)const |
| int | get_binding_modifier_count()const |

OpenXRIPBinding
get_binding(index:int)const
get_binding_count()const
OpenXRIPBindingModifier
get_binding_modifier(index:int)const
get_binding_modifier_count()const

## Property Descriptions
Arraybinding_modifiers=[]🔗
- voidset_binding_modifiers(value:Array)
voidset_binding_modifiers(value:Array)
- Arrayget_binding_modifiers()
Arrayget_binding_modifiers()
Binding modifiers for this interaction profile.
Arraybindings=[]🔗
- voidset_bindings(value:Array)
voidset_bindings(value:Array)
- Arrayget_bindings()
Arrayget_bindings()
Action bindings for this interaction profile.
Stringinteraction_profile_path=""🔗
- voidset_interaction_profile_path(value:String)
voidset_interaction_profile_path(value:String)
- Stringget_interaction_profile_path()
Stringget_interaction_profile_path()
The interaction profile path identifying the XR device.

## Method Descriptions
OpenXRIPBindingget_binding(index:int)const🔗
Retrieve the binding at this index.
intget_binding_count()const🔗
Get the number of bindings in this interaction profile.
OpenXRIPBindingModifierget_binding_modifier(index:int)const🔗
Get theOpenXRBindingModifierat this index.
intget_binding_modifier_count()const🔗
Get the number of binding modifiers in this interaction profile.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.