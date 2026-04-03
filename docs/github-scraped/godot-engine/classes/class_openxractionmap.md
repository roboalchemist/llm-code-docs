:github_url: hide



# OpenXRActionMap

**Inherits:** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Collection of [OpenXRActionSet<class_OpenXRActionSet>] and [OpenXRInteractionProfile<class_OpenXRInteractionProfile>] resources for the OpenXR module.


## Description

OpenXR uses an action system similar to Godots Input map system to bind inputs and outputs on various types of XR controllers to named actions. OpenXR specifies more detail on these inputs and outputs than Godot supports.

Another important distinction is that OpenXR offers no control over these bindings. The bindings we register are suggestions, it is up to the XR runtime to offer users the ability to change these bindings. This allows the XR runtime to fill in the gaps if new hardware becomes available.

The action map therefore needs to be loaded at startup and can't be changed afterwards. This resource is a container for the entire action map.


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------+----------------------------------------------------------------------------------+--------+
> | :ref:`Array<class_Array>` | :ref:`action_sets<class_OpenXRActionMap_property_action_sets>`                   | ``[]`` |
> +---------------------------+----------------------------------------------------------------------------------+--------+
> | :ref:`Array<class_Array>` | :ref:`interaction_profiles<class_OpenXRActionMap_property_interaction_profiles>` | ``[]`` |
> +---------------------------+----------------------------------------------------------------------------------+--------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +-----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                          | :ref:`add_action_set<class_OpenXRActionMap_method_add_action_set>`\ (\ action_set\: :ref:`OpenXRActionSet<class_OpenXRActionSet>`\ )                                                    |
> +-----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                          | :ref:`add_interaction_profile<class_OpenXRActionMap_method_add_interaction_profile>`\ (\ interaction_profile\: :ref:`OpenXRInteractionProfile<class_OpenXRInteractionProfile>`\ )       |
> +-----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                          | :ref:`create_default_action_sets<class_OpenXRActionMap_method_create_default_action_sets>`\ (\ )                                                                                        |
> +-----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`OpenXRActionSet<class_OpenXRActionSet>`                   | :ref:`find_action_set<class_OpenXRActionMap_method_find_action_set>`\ (\ name\: :ref:`String<class_String>`\ ) |const|                                                                  |
> +-----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`OpenXRInteractionProfile<class_OpenXRInteractionProfile>` | :ref:`find_interaction_profile<class_OpenXRActionMap_method_find_interaction_profile>`\ (\ name\: :ref:`String<class_String>`\ ) |const|                                                |
> +-----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`OpenXRActionSet<class_OpenXRActionSet>`                   | :ref:`get_action_set<class_OpenXRActionMap_method_get_action_set>`\ (\ idx\: :ref:`int<class_int>`\ ) |const|                                                                           |
> +-----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                           | :ref:`get_action_set_count<class_OpenXRActionMap_method_get_action_set_count>`\ (\ ) |const|                                                                                            |
> +-----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`OpenXRInteractionProfile<class_OpenXRInteractionProfile>` | :ref:`get_interaction_profile<class_OpenXRActionMap_method_get_interaction_profile>`\ (\ idx\: :ref:`int<class_int>`\ ) |const|                                                         |
> +-----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                           | :ref:`get_interaction_profile_count<class_OpenXRActionMap_method_get_interaction_profile_count>`\ (\ ) |const|                                                                          |
> +-----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                          | :ref:`remove_action_set<class_OpenXRActionMap_method_remove_action_set>`\ (\ action_set\: :ref:`OpenXRActionSet<class_OpenXRActionSet>`\ )                                              |
> +-----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                          | :ref:`remove_interaction_profile<class_OpenXRActionMap_method_remove_interaction_profile>`\ (\ interaction_profile\: :ref:`OpenXRInteractionProfile<class_OpenXRInteractionProfile>`\ ) |
> +-----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Property Descriptions



[Array<class_Array>] **action_sets** = `[]` [🔗<class_OpenXRActionMap_property_action_sets>]


- |void| **set_action_sets**\ (\ value\: [Array<class_Array>]\ )
- [Array<class_Array>] **get_action_sets**\ (\ )

Collection of [OpenXRActionSet<class_OpenXRActionSet>]\ s that are part of this action map.


----



[Array<class_Array>] **interaction_profiles** = `[]` [🔗<class_OpenXRActionMap_property_interaction_profiles>]


- |void| **set_interaction_profiles**\ (\ value\: [Array<class_Array>]\ )
- [Array<class_Array>] **get_interaction_profiles**\ (\ )

Collection of [OpenXRInteractionProfile<class_OpenXRInteractionProfile>]\ s that are part of this action map.


----


## Method Descriptions



|void| **add_action_set**\ (\ action_set\: [OpenXRActionSet<class_OpenXRActionSet>]\ ) [🔗<class_OpenXRActionMap_method_add_action_set>]

Add an action set.


----



|void| **add_interaction_profile**\ (\ interaction_profile\: [OpenXRInteractionProfile<class_OpenXRInteractionProfile>]\ ) [🔗<class_OpenXRActionMap_method_add_interaction_profile>]

Add an interaction profile.


----



|void| **create_default_action_sets**\ (\ ) [🔗<class_OpenXRActionMap_method_create_default_action_sets>]

Setup this action set with our default actions.


----



[OpenXRActionSet<class_OpenXRActionSet>] **find_action_set**\ (\ name\: [String<class_String>]\ ) |const| [🔗<class_OpenXRActionMap_method_find_action_set>]

Retrieve an action set by name.


----



[OpenXRInteractionProfile<class_OpenXRInteractionProfile>] **find_interaction_profile**\ (\ name\: [String<class_String>]\ ) |const| [🔗<class_OpenXRActionMap_method_find_interaction_profile>]

Find an interaction profile by its name (path).


----



[OpenXRActionSet<class_OpenXRActionSet>] **get_action_set**\ (\ idx\: [int<class_int>]\ ) |const| [🔗<class_OpenXRActionMap_method_get_action_set>]

Retrieve the action set at this index.


----



[int<class_int>] **get_action_set_count**\ (\ ) |const| [🔗<class_OpenXRActionMap_method_get_action_set_count>]

Retrieve the number of actions sets in our action map.


----



[OpenXRInteractionProfile<class_OpenXRInteractionProfile>] **get_interaction_profile**\ (\ idx\: [int<class_int>]\ ) |const| [🔗<class_OpenXRActionMap_method_get_interaction_profile>]

Get the interaction profile at this index.


----



[int<class_int>] **get_interaction_profile_count**\ (\ ) |const| [🔗<class_OpenXRActionMap_method_get_interaction_profile_count>]

Retrieve the number of interaction profiles in our action map.


----



|void| **remove_action_set**\ (\ action_set\: [OpenXRActionSet<class_OpenXRActionSet>]\ ) [🔗<class_OpenXRActionMap_method_remove_action_set>]

Remove an action set.


----



|void| **remove_interaction_profile**\ (\ interaction_profile\: [OpenXRInteractionProfile<class_OpenXRInteractionProfile>]\ ) [🔗<class_OpenXRActionMap_method_remove_interaction_profile>]

Remove an interaction profile.

