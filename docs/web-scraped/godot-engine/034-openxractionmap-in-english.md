# OpenXRActionMap in English

# OpenXRActionMap

Inherits:Resource<RefCounted<Object
Collection ofOpenXRActionSetandOpenXRInteractionProfileresources for the OpenXR module.

## Description

OpenXR uses an action system similar to Godots Input map system to bind inputs and outputs on various types of XR controllers to named actions. OpenXR specifies more detail on these inputs and outputs than Godot supports.
Another important distinction is that OpenXR offers no control over these bindings. The bindings we register are suggestions, it is up to the XR runtime to offer users the ability to change these bindings. This allows the XR runtime to fill in the gaps if new hardware becomes available.
The action map therefore needs to be loaded at startup and can't be changed afterwards. This resource is a container for the entire action map.

## Properties

| Array | action_sets | [] |
|---|---|---|
| Array | interaction_profiles | [] |

Array
action_sets
Array
interaction_profiles

## Methods

| void | add_action_set(action_set:OpenXRActionSet) |
|---|---|
| void | add_interaction_profile(interaction_profile:OpenXRInteractionProfile) |
| void | create_default_action_sets() |
| OpenXRActionSet | find_action_set(name:String)const |
| OpenXRInteractionProfile | find_interaction_profile(name:String)const |
| OpenXRActionSet | get_action_set(idx:int)const |
| int | get_action_set_count()const |
| OpenXRInteractionProfile | get_interaction_profile(idx:int)const |
| int | get_interaction_profile_count()const |
| void | remove_action_set(action_set:OpenXRActionSet) |
| void | remove_interaction_profile(interaction_profile:OpenXRInteractionProfile) |

void
add_action_set(action_set:OpenXRActionSet)
void
add_interaction_profile(interaction_profile:OpenXRInteractionProfile)
void
create_default_action_sets()
OpenXRActionSet
find_action_set(name:String)const
OpenXRInteractionProfile
find_interaction_profile(name:String)const
OpenXRActionSet
get_action_set(idx:int)const
get_action_set_count()const
OpenXRInteractionProfile
get_interaction_profile(idx:int)const
get_interaction_profile_count()const
void
remove_action_set(action_set:OpenXRActionSet)
void
remove_interaction_profile(interaction_profile:OpenXRInteractionProfile)

## Property Descriptions

Arrayaction_sets=[]🔗

- voidset_action_sets(value:Array)
voidset_action_sets(value:Array)
- Arrayget_action_sets()
Arrayget_action_sets()
Collection ofOpenXRActionSets that are part of this action map.
Arrayinteraction_profiles=[]🔗
- voidset_interaction_profiles(value:Array)
voidset_interaction_profiles(value:Array)
- Arrayget_interaction_profiles()
Arrayget_interaction_profiles()
Collection ofOpenXRInteractionProfiles that are part of this action map.

## Method Descriptions

voidadd_action_set(action_set:OpenXRActionSet)🔗
Add an action set.
voidadd_interaction_profile(interaction_profile:OpenXRInteractionProfile)🔗
Add an interaction profile.
voidcreate_default_action_sets()🔗
Setup this action set with our default actions.
OpenXRActionSetfind_action_set(name:String)const🔗
Retrieve an action set by name.
OpenXRInteractionProfilefind_interaction_profile(name:String)const🔗
Find an interaction profile by its name (path).
OpenXRActionSetget_action_set(idx:int)const🔗
Retrieve the action set at this index.
intget_action_set_count()const🔗
Retrieve the number of actions sets in our action map.
OpenXRInteractionProfileget_interaction_profile(idx:int)const🔗
Get the interaction profile at this index.
intget_interaction_profile_count()const🔗
Retrieve the number of interaction profiles in our action map.
voidremove_action_set(action_set:OpenXRActionSet)🔗
Remove an action set.
voidremove_interaction_profile(interaction_profile:OpenXRInteractionProfile)🔗
Remove an interaction profile.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
