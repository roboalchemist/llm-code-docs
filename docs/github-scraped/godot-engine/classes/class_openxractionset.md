:github_url: hide



# OpenXRActionSet

**Inherits:** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Collection of [OpenXRAction<class_OpenXRAction>] resources that make up an action set.


## Description

Action sets in OpenXR define a collection of actions that can be activated in unison. This allows games to easily change between different states that require different inputs or need to reinterpret inputs. For instance we could have an action set that is active when a menu is open, an action set that is active when the player is freely walking around and an action set that is active when the player is controlling a vehicle.

Action sets can contain the same action with the same name, if such action sets are active at the same time the action set with the highest priority defines which binding is active.


## Properties

> **TABLE**
> :widths: auto
>
> +-----------------------------+----------------------------------------------------------------------+--------+
> | :ref:`Array<class_Array>`   | :ref:`actions<class_OpenXRActionSet_property_actions>`               | ``[]`` |
> +-----------------------------+----------------------------------------------------------------------+--------+
> | :ref:`String<class_String>` | :ref:`localized_name<class_OpenXRActionSet_property_localized_name>` | ``""`` |
> +-----------------------------+----------------------------------------------------------------------+--------+
> | :ref:`int<class_int>`       | :ref:`priority<class_OpenXRActionSet_property_priority>`             | ``0``  |
> +-----------------------------+----------------------------------------------------------------------+--------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +-----------------------+--------------------------------------------------------------------------------------------------------------------------+
> | |void|                | :ref:`add_action<class_OpenXRActionSet_method_add_action>`\ (\ action\: :ref:`OpenXRAction<class_OpenXRAction>`\ )       |
> +-----------------------+--------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>` | :ref:`get_action_count<class_OpenXRActionSet_method_get_action_count>`\ (\ ) |const|                                     |
> +-----------------------+--------------------------------------------------------------------------------------------------------------------------+
> | |void|                | :ref:`remove_action<class_OpenXRActionSet_method_remove_action>`\ (\ action\: :ref:`OpenXRAction<class_OpenXRAction>`\ ) |
> +-----------------------+--------------------------------------------------------------------------------------------------------------------------+
>

----


## Property Descriptions



[Array<class_Array>] **actions** = `[]` [🔗<class_OpenXRActionSet_property_actions>]


- |void| **set_actions**\ (\ value\: [Array<class_Array>]\ )
- [Array<class_Array>] **get_actions**\ (\ )

Collection of actions for this action set.


----



[String<class_String>] **localized_name** = `""` [🔗<class_OpenXRActionSet_property_localized_name>]


- |void| **set_localized_name**\ (\ value\: [String<class_String>]\ )
- [String<class_String>] **get_localized_name**\ (\ )

The localized name of this action set.


----



[int<class_int>] **priority** = `0` [🔗<class_OpenXRActionSet_property_priority>]


- |void| **set_priority**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_priority**\ (\ )

The priority for this action set.


----


## Method Descriptions



|void| **add_action**\ (\ action\: [OpenXRAction<class_OpenXRAction>]\ ) [🔗<class_OpenXRActionSet_method_add_action>]

Add an action to this action set.


----



[int<class_int>] **get_action_count**\ (\ ) |const| [🔗<class_OpenXRActionSet_method_get_action_count>]

Retrieve the number of actions in our action set.


----



|void| **remove_action**\ (\ action\: [OpenXRAction<class_OpenXRAction>]\ ) [🔗<class_OpenXRActionSet_method_remove_action>]

Remove an action from this action set.

