:github_url: hide



# InputMap

**Inherits:** [Object<class_Object>]

A singleton that manages all [InputEventAction<class_InputEventAction>]\ s.


## Description

Manages all [InputEventAction<class_InputEventAction>] which can be created/modified from the project settings menu **Project > Project Settings > Input Map** or in code with [add_action()<class_InputMap_method_add_action>] and [action_add_event()<class_InputMap_method_action_add_event>]. See [Node._input()<class_Node_private_method__input>].


## Tutorials

- [Using InputEvent: InputMap ](../tutorials/inputs/inputevent.html#inputmap)_


## Methods

> **TABLE**
> :widths: auto
>
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                           | :ref:`action_add_event<class_InputMap_method_action_add_event>`\ (\ action\: :ref:`StringName<class_StringName>`, event\: :ref:`InputEvent<class_InputEvent>`\ )                                                      |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                           | :ref:`action_erase_event<class_InputMap_method_action_erase_event>`\ (\ action\: :ref:`StringName<class_StringName>`, event\: :ref:`InputEvent<class_InputEvent>`\ )                                                  |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                           | :ref:`action_erase_events<class_InputMap_method_action_erase_events>`\ (\ action\: :ref:`StringName<class_StringName>`\ )                                                                                             |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`                                        | :ref:`action_get_deadzone<class_InputMap_method_action_get_deadzone>`\ (\ action\: :ref:`StringName<class_StringName>`\ )                                                                                             |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`\[:ref:`InputEvent<class_InputEvent>`\] | :ref:`action_get_events<class_InputMap_method_action_get_events>`\ (\ action\: :ref:`StringName<class_StringName>`\ )                                                                                                 |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                          | :ref:`action_has_event<class_InputMap_method_action_has_event>`\ (\ action\: :ref:`StringName<class_StringName>`, event\: :ref:`InputEvent<class_InputEvent>`\ )                                                      |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                           | :ref:`action_set_deadzone<class_InputMap_method_action_set_deadzone>`\ (\ action\: :ref:`StringName<class_StringName>`, deadzone\: :ref:`float<class_float>`\ )                                                       |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                           | :ref:`add_action<class_InputMap_method_add_action>`\ (\ action\: :ref:`StringName<class_StringName>`, deadzone\: :ref:`float<class_float>` = 0.2\ )                                                                   |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                           | :ref:`erase_action<class_InputMap_method_erase_action>`\ (\ action\: :ref:`StringName<class_StringName>`\ )                                                                                                           |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                          | :ref:`event_is_action<class_InputMap_method_event_is_action>`\ (\ event\: :ref:`InputEvent<class_InputEvent>`, action\: :ref:`StringName<class_StringName>`, exact_match\: :ref:`bool<class_bool>` = false\ ) |const| |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`                                      | :ref:`get_action_description<class_InputMap_method_get_action_description>`\ (\ action\: :ref:`StringName<class_StringName>`\ ) |const|                                                                               |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`\[:ref:`StringName<class_StringName>`\] | :ref:`get_actions<class_InputMap_method_get_actions>`\ (\ )                                                                                                                                                           |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                          | :ref:`has_action<class_InputMap_method_has_action>`\ (\ action\: :ref:`StringName<class_StringName>`\ ) |const|                                                                                                       |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                           | :ref:`load_from_project_settings<class_InputMap_method_load_from_project_settings>`\ (\ )                                                                                                                             |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Method Descriptions



|void| **action_add_event**\ (\ action\: [StringName<class_StringName>], event\: [InputEvent<class_InputEvent>]\ ) [🔗<class_InputMap_method_action_add_event>]

Adds an [InputEvent<class_InputEvent>] to an action. This [InputEvent<class_InputEvent>] will trigger the action.


----



|void| **action_erase_event**\ (\ action\: [StringName<class_StringName>], event\: [InputEvent<class_InputEvent>]\ ) [🔗<class_InputMap_method_action_erase_event>]

Removes an [InputEvent<class_InputEvent>] from an action.


----



|void| **action_erase_events**\ (\ action\: [StringName<class_StringName>]\ ) [🔗<class_InputMap_method_action_erase_events>]

Removes all events from an action.


----



[float<class_float>] **action_get_deadzone**\ (\ action\: [StringName<class_StringName>]\ ) [🔗<class_InputMap_method_action_get_deadzone>]

Returns a deadzone value for the action.


----



[Array<class_Array>]\[[InputEvent<class_InputEvent>]\] **action_get_events**\ (\ action\: [StringName<class_StringName>]\ ) [🔗<class_InputMap_method_action_get_events>]

Returns an array of [InputEvent<class_InputEvent>]\ s associated with a given action.

\ **Note:** When used in the editor (e.g. a tool script or [EditorPlugin<class_EditorPlugin>]), this method will return events for the editor action. If you want to access your project's input binds from the editor, read the `input/*` settings from [ProjectSettings<class_ProjectSettings>].


----



[bool<class_bool>] **action_has_event**\ (\ action\: [StringName<class_StringName>], event\: [InputEvent<class_InputEvent>]\ ) [🔗<class_InputMap_method_action_has_event>]

Returns `true` if the action has the given [InputEvent<class_InputEvent>] associated with it.


----



|void| **action_set_deadzone**\ (\ action\: [StringName<class_StringName>], deadzone\: [float<class_float>]\ ) [🔗<class_InputMap_method_action_set_deadzone>]

Sets a deadzone value for the action.


----



|void| **add_action**\ (\ action\: [StringName<class_StringName>], deadzone\: [float<class_float>] = 0.2\ ) [🔗<class_InputMap_method_add_action>]

Adds an empty action to the **InputMap** with a configurable `deadzone`.

An [InputEvent<class_InputEvent>] can then be added to this action with [action_add_event()<class_InputMap_method_action_add_event>].


----



|void| **erase_action**\ (\ action\: [StringName<class_StringName>]\ ) [🔗<class_InputMap_method_erase_action>]

Removes an action from the **InputMap**.


----



[bool<class_bool>] **event_is_action**\ (\ event\: [InputEvent<class_InputEvent>], action\: [StringName<class_StringName>], exact_match\: [bool<class_bool>] = false\ ) |const| [🔗<class_InputMap_method_event_is_action>]

Returns `true` if the given event is part of an existing action. This method ignores keyboard modifiers if the given [InputEvent<class_InputEvent>] is not pressed (for proper release detection). See [action_has_event()<class_InputMap_method_action_has_event>] if you don't want this behavior.

If `exact_match` is `false`, it ignores additional input modifiers for [InputEventKey<class_InputEventKey>] and [InputEventMouseButton<class_InputEventMouseButton>] events, and the direction for [InputEventJoypadMotion<class_InputEventJoypadMotion>] events.


----



[String<class_String>] **get_action_description**\ (\ action\: [StringName<class_StringName>]\ ) |const| [🔗<class_InputMap_method_get_action_description>]

Returns the human-readable description of the given action.


----



[Array<class_Array>]\[[StringName<class_StringName>]\] **get_actions**\ (\ ) [🔗<class_InputMap_method_get_actions>]

Returns an array of all actions in the **InputMap**.


----



[bool<class_bool>] **has_action**\ (\ action\: [StringName<class_StringName>]\ ) |const| [🔗<class_InputMap_method_has_action>]

Returns `true` if the **InputMap** has a registered action with the given name.


----



|void| **load_from_project_settings**\ (\ ) [🔗<class_InputMap_method_load_from_project_settings>]

Clears all [InputEventAction<class_InputEventAction>] in the **InputMap** and load it anew from [ProjectSettings<class_ProjectSettings>].

