:github_url: hide



# BaseButton

**Inherits:** [Control<class_Control>] **<** [CanvasItem<class_CanvasItem>] **<** [Node<class_Node>] **<** [Object<class_Object>]

**Inherited By:** [Button<class_Button>], [LinkButton<class_LinkButton>], [TextureButton<class_TextureButton>]

Abstract base class for GUI buttons.


## Description

**BaseButton** is an abstract base class for GUI buttons. It doesn't display anything by itself.


## Properties

> **TABLE**
> :widths: auto
>
> +-------------------------------------------------------------------------+-----------------------------------------------------------------------------+---------------------------------------------------------------------+
> | :ref:`ActionMode<enum_BaseButton_ActionMode>`                           | :ref:`action_mode<class_BaseButton_property_action_mode>`                   | ``1``                                                               |
> +-------------------------------------------------------------------------+-----------------------------------------------------------------------------+---------------------------------------------------------------------+
> | :ref:`ButtonGroup<class_ButtonGroup>`                                   | :ref:`button_group<class_BaseButton_property_button_group>`                 |                                                                     |
> +-------------------------------------------------------------------------+-----------------------------------------------------------------------------+---------------------------------------------------------------------+
> | |bitfield|\[:ref:`MouseButtonMask<enum_@GlobalScope_MouseButtonMask>`\] | :ref:`button_mask<class_BaseButton_property_button_mask>`                   | ``1``                                                               |
> +-------------------------------------------------------------------------+-----------------------------------------------------------------------------+---------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                                 | :ref:`button_pressed<class_BaseButton_property_button_pressed>`             | ``false``                                                           |
> +-------------------------------------------------------------------------+-----------------------------------------------------------------------------+---------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                                 | :ref:`disabled<class_BaseButton_property_disabled>`                         | ``false``                                                           |
> +-------------------------------------------------------------------------+-----------------------------------------------------------------------------+---------------------------------------------------------------------+
> | :ref:`FocusMode<enum_Control_FocusMode>`                                | focus_mode                                                                  | ``2`` (overrides :ref:`Control<class_Control_property_focus_mode>`) |
> +-------------------------------------------------------------------------+-----------------------------------------------------------------------------+---------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                                 | :ref:`keep_pressed_outside<class_BaseButton_property_keep_pressed_outside>` | ``false``                                                           |
> +-------------------------------------------------------------------------+-----------------------------------------------------------------------------+---------------------------------------------------------------------+
> | :ref:`Shortcut<class_Shortcut>`                                         | :ref:`shortcut<class_BaseButton_property_shortcut>`                         |                                                                     |
> +-------------------------------------------------------------------------+-----------------------------------------------------------------------------+---------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                                 | :ref:`shortcut_feedback<class_BaseButton_property_shortcut_feedback>`       | ``true``                                                            |
> +-------------------------------------------------------------------------+-----------------------------------------------------------------------------+---------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                                 | :ref:`shortcut_in_tooltip<class_BaseButton_property_shortcut_in_tooltip>`   | ``true``                                                            |
> +-------------------------------------------------------------------------+-----------------------------------------------------------------------------+---------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                                 | :ref:`toggle_mode<class_BaseButton_property_toggle_mode>`                   | ``false``                                                           |
> +-------------------------------------------------------------------------+-----------------------------------------------------------------------------+---------------------------------------------------------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +-------------------------------------------+----------------------------------------------------------------------------------------------------------------------+
> | |void|                                    | :ref:`_pressed<class_BaseButton_private_method__pressed>`\ (\ ) |virtual|                                            |
> +-------------------------------------------+----------------------------------------------------------------------------------------------------------------------+
> | |void|                                    | :ref:`_toggled<class_BaseButton_private_method__toggled>`\ (\ toggled_on\: :ref:`bool<class_bool>`\ ) |virtual|      |
> +-------------------------------------------+----------------------------------------------------------------------------------------------------------------------+
> | :ref:`DrawMode<enum_BaseButton_DrawMode>` | :ref:`get_draw_mode<class_BaseButton_method_get_draw_mode>`\ (\ ) |const|                                            |
> +-------------------------------------------+----------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                   | :ref:`is_hovered<class_BaseButton_method_is_hovered>`\ (\ ) |const|                                                  |
> +-------------------------------------------+----------------------------------------------------------------------------------------------------------------------+
> | |void|                                    | :ref:`set_pressed_no_signal<class_BaseButton_method_set_pressed_no_signal>`\ (\ pressed\: :ref:`bool<class_bool>`\ ) |
> +-------------------------------------------+----------------------------------------------------------------------------------------------------------------------+
>

----


## Signals



**button_down**\ (\ ) [🔗<class_BaseButton_signal_button_down>]

Emitted when the button starts being held down.


----



**button_up**\ (\ ) [🔗<class_BaseButton_signal_button_up>]

Emitted when the button stops being held down.


----



**pressed**\ (\ ) [🔗<class_BaseButton_signal_pressed>]

Emitted when the button is toggled or pressed. This is on [button_down<class_BaseButton_signal_button_down>] if [action_mode<class_BaseButton_property_action_mode>] is [ACTION_MODE_BUTTON_PRESS<class_BaseButton_constant_ACTION_MODE_BUTTON_PRESS>] and on [button_up<class_BaseButton_signal_button_up>] otherwise.

If you need to know the button's pressed state (and [toggle_mode<class_BaseButton_property_toggle_mode>] is active), use [toggled<class_BaseButton_signal_toggled>] instead.


----



**toggled**\ (\ toggled_on\: [bool<class_bool>]\ ) [🔗<class_BaseButton_signal_toggled>]

Emitted when the button was just toggled between pressed and normal states (only if [toggle_mode<class_BaseButton_property_toggle_mode>] is active). The new state is contained in the `toggled_on` argument.


----


## Enumerations



enum **DrawMode**: [🔗<enum_BaseButton_DrawMode>]



[DrawMode<enum_BaseButton_DrawMode>] **DRAW_NORMAL** = `0`

The normal state (i.e. not pressed, not hovered, not toggled and enabled) of buttons.



[DrawMode<enum_BaseButton_DrawMode>] **DRAW_PRESSED** = `1`

The state of buttons are pressed.



[DrawMode<enum_BaseButton_DrawMode>] **DRAW_HOVER** = `2`

The state of buttons are hovered.



[DrawMode<enum_BaseButton_DrawMode>] **DRAW_DISABLED** = `3`

The state of buttons are disabled.



[DrawMode<enum_BaseButton_DrawMode>] **DRAW_HOVER_PRESSED** = `4`

The state of buttons are both hovered and pressed.


----



enum **ActionMode**: [🔗<enum_BaseButton_ActionMode>]



[ActionMode<enum_BaseButton_ActionMode>] **ACTION_MODE_BUTTON_PRESS** = `0`

Require just a press to consider the button clicked.



[ActionMode<enum_BaseButton_ActionMode>] **ACTION_MODE_BUTTON_RELEASE** = `1`

Require a press and a subsequent release before considering the button clicked.


----


## Property Descriptions



[ActionMode<enum_BaseButton_ActionMode>] **action_mode** = `1` [🔗<class_BaseButton_property_action_mode>]


- |void| **set_action_mode**\ (\ value\: [ActionMode<enum_BaseButton_ActionMode>]\ )
- [ActionMode<enum_BaseButton_ActionMode>] **get_action_mode**\ (\ )

Determines when the button is considered clicked.


----



[ButtonGroup<class_ButtonGroup>] **button_group** [🔗<class_BaseButton_property_button_group>]


- |void| **set_button_group**\ (\ value\: [ButtonGroup<class_ButtonGroup>]\ )
- [ButtonGroup<class_ButtonGroup>] **get_button_group**\ (\ )

The [ButtonGroup<class_ButtonGroup>] associated with the button. Not to be confused with node groups.

\ **Note:** The button will be configured as a radio button if a [ButtonGroup<class_ButtonGroup>] is assigned to it.


----



|bitfield|\[[MouseButtonMask<enum_@GlobalScope_MouseButtonMask>]\] **button_mask** = `1` [🔗<class_BaseButton_property_button_mask>]


- |void| **set_button_mask**\ (\ value\: |bitfield|\[[MouseButtonMask<enum_@GlobalScope_MouseButtonMask>]\]\ )
- |bitfield|\[[MouseButtonMask<enum_@GlobalScope_MouseButtonMask>]\] **get_button_mask**\ (\ )

Binary mask to choose which mouse buttons this button will respond to.

To allow both left-click and right-click, use `MOUSE_BUTTON_MASK_LEFT | MOUSE_BUTTON_MASK_RIGHT`.


----



[bool<class_bool>] **button_pressed** = `false` [🔗<class_BaseButton_property_button_pressed>]


- |void| **set_pressed**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_pressed**\ (\ )

If `true`, the button's state is pressed. Means the button is pressed down or toggled (if [toggle_mode<class_BaseButton_property_toggle_mode>] is active). Only works if [toggle_mode<class_BaseButton_property_toggle_mode>] is `true`.

\ **Note:** Changing the value of [button_pressed<class_BaseButton_property_button_pressed>] will result in [toggled<class_BaseButton_signal_toggled>] to be emitted. If you want to change the pressed state without emitting that signal, use [set_pressed_no_signal()<class_BaseButton_method_set_pressed_no_signal>].


----



[bool<class_bool>] **disabled** = `false` [🔗<class_BaseButton_property_disabled>]


- |void| **set_disabled**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_disabled**\ (\ )

If `true`, the button is in disabled state and can't be clicked or toggled.

\ **Note:** If the button is disabled while held down, [button_up<class_BaseButton_signal_button_up>] will be emitted.


----



[bool<class_bool>] **keep_pressed_outside** = `false` [🔗<class_BaseButton_property_keep_pressed_outside>]


- |void| **set_keep_pressed_outside**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_keep_pressed_outside**\ (\ )

If `true`, the button stays pressed when moving the cursor outside the button while pressing it.

\ **Note:** This property only affects the button's visual appearance. Signals will be emitted at the same moment regardless of this property's value.


----



[Shortcut<class_Shortcut>] **shortcut** [🔗<class_BaseButton_property_shortcut>]


- |void| **set_shortcut**\ (\ value\: [Shortcut<class_Shortcut>]\ )
- [Shortcut<class_Shortcut>] **get_shortcut**\ (\ )

[Shortcut<class_Shortcut>] associated to the button.


----



[bool<class_bool>] **shortcut_feedback** = `true` [🔗<class_BaseButton_property_shortcut_feedback>]


- |void| **set_shortcut_feedback**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_shortcut_feedback**\ (\ )

If `true`, the button will highlight for a short amount of time when its shortcut is activated. If `false` and [toggle_mode<class_BaseButton_property_toggle_mode>] is `false`, the shortcut will activate without any visual feedback.


----



[bool<class_bool>] **shortcut_in_tooltip** = `true` [🔗<class_BaseButton_property_shortcut_in_tooltip>]


- |void| **set_shortcut_in_tooltip**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_shortcut_in_tooltip_enabled**\ (\ )

If `true`, the button will add information about its shortcut in the tooltip.

\ **Note:** This property does nothing when the tooltip control is customized using [Control._make_custom_tooltip()<class_Control_private_method__make_custom_tooltip>].


----



[bool<class_bool>] **toggle_mode** = `false` [🔗<class_BaseButton_property_toggle_mode>]


- |void| **set_toggle_mode**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_toggle_mode**\ (\ )

If `true`, the button is in toggle mode. Makes the button flip state between pressed and unpressed each time its area is clicked.


----


## Method Descriptions



|void| **_pressed**\ (\ ) |virtual| [🔗<class_BaseButton_private_method__pressed>]

Called when the button is pressed. If you need to know the button's pressed state (and [toggle_mode<class_BaseButton_property_toggle_mode>] is active), use [_toggled()<class_BaseButton_private_method__toggled>] instead.


----



|void| **_toggled**\ (\ toggled_on\: [bool<class_bool>]\ ) |virtual| [🔗<class_BaseButton_private_method__toggled>]

Called when the button is toggled (only if [toggle_mode<class_BaseButton_property_toggle_mode>] is active).


----



[DrawMode<enum_BaseButton_DrawMode>] **get_draw_mode**\ (\ ) |const| [🔗<class_BaseButton_method_get_draw_mode>]

Returns the visual state used to draw the button. This is useful mainly when implementing your own draw code by either overriding _draw() or connecting to "draw" signal. The visual state of the button is defined by the [DrawMode<enum_BaseButton_DrawMode>] enum.


----



[bool<class_bool>] **is_hovered**\ (\ ) |const| [🔗<class_BaseButton_method_is_hovered>]

Returns `true` if the mouse has entered the button and has not left it yet.


----



|void| **set_pressed_no_signal**\ (\ pressed\: [bool<class_bool>]\ ) [🔗<class_BaseButton_method_set_pressed_no_signal>]

Changes the [button_pressed<class_BaseButton_property_button_pressed>] state of the button, without emitting [toggled<class_BaseButton_signal_toggled>]. Use when you just want to change the state of the button without sending the pressed event (e.g. when initializing scene). Only works if [toggle_mode<class_BaseButton_property_toggle_mode>] is `true`.

\ **Note:** This method doesn't unpress other buttons in [button_group<class_BaseButton_property_button_group>].

