:github_url: hide



# TouchScreenButton

**Inherits:** [Node2D<class_Node2D>] **<** [CanvasItem<class_CanvasItem>] **<** [Node<class_Node>] **<** [Object<class_Object>]

Button for touch screen devices for gameplay use.


## Description

TouchScreenButton allows you to create on-screen buttons for touch devices. It's intended for gameplay use, such as a unit you have to touch to move. Unlike [Button<class_Button>], TouchScreenButton supports multitouch out of the box. Several TouchScreenButtons can be pressed at the same time with touch input.

This node inherits from [Node2D<class_Node2D>]. Unlike with [Control<class_Control>] nodes, you cannot set anchors on it. If you want to create menus or user interfaces, you may want to use [Button<class_Button>] nodes instead. To make button nodes react to touch events, you can enable [ProjectSettings.input_devices/pointing/emulate_mouse_from_touch<class_ProjectSettings_property_input_devices/pointing/emulate_mouse_from_touch>] in the Project Settings.

You can configure TouchScreenButton to be visible only on touch devices, helping you develop your game both for desktop and mobile devices.


## Properties

> **TABLE**
> :widths: auto
>
> +--------------------------------------------------------------+--------------------------------------------------------------------------+-----------+
> | :ref:`String<class_String>`                                  | :ref:`action<class_TouchScreenButton_property_action>`                   | ``""``    |
> +--------------------------------------------------------------+--------------------------------------------------------------------------+-----------+
> | :ref:`BitMap<class_BitMap>`                                  | :ref:`bitmask<class_TouchScreenButton_property_bitmask>`                 |           |
> +--------------------------------------------------------------+--------------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>`                                      | :ref:`passby_press<class_TouchScreenButton_property_passby_press>`       | ``false`` |
> +--------------------------------------------------------------+--------------------------------------------------------------------------+-----------+
> | :ref:`Shape2D<class_Shape2D>`                                | :ref:`shape<class_TouchScreenButton_property_shape>`                     |           |
> +--------------------------------------------------------------+--------------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>`                                      | :ref:`shape_centered<class_TouchScreenButton_property_shape_centered>`   | ``true``  |
> +--------------------------------------------------------------+--------------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>`                                      | :ref:`shape_visible<class_TouchScreenButton_property_shape_visible>`     | ``true``  |
> +--------------------------------------------------------------+--------------------------------------------------------------------------+-----------+
> | :ref:`Texture2D<class_Texture2D>`                            | :ref:`texture_normal<class_TouchScreenButton_property_texture_normal>`   |           |
> +--------------------------------------------------------------+--------------------------------------------------------------------------+-----------+
> | :ref:`Texture2D<class_Texture2D>`                            | :ref:`texture_pressed<class_TouchScreenButton_property_texture_pressed>` |           |
> +--------------------------------------------------------------+--------------------------------------------------------------------------+-----------+
> | :ref:`VisibilityMode<enum_TouchScreenButton_VisibilityMode>` | :ref:`visibility_mode<class_TouchScreenButton_property_visibility_mode>` | ``0``     |
> +--------------------------------------------------------------+--------------------------------------------------------------------------+-----------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +-------------------------+----------------------------------------------------------------------------+
> | :ref:`bool<class_bool>` | :ref:`is_pressed<class_TouchScreenButton_method_is_pressed>`\ (\ ) |const| |
> +-------------------------+----------------------------------------------------------------------------+
>

----


## Signals



**pressed**\ (\ ) [🔗<class_TouchScreenButton_signal_pressed>]

Emitted when the button is pressed (down).


----



**released**\ (\ ) [🔗<class_TouchScreenButton_signal_released>]

Emitted when the button is released (up).


----


## Enumerations



enum **VisibilityMode**: [🔗<enum_TouchScreenButton_VisibilityMode>]



[VisibilityMode<enum_TouchScreenButton_VisibilityMode>] **VISIBILITY_ALWAYS** = `0`

Always visible.



[VisibilityMode<enum_TouchScreenButton_VisibilityMode>] **VISIBILITY_TOUCHSCREEN_ONLY** = `1`

Visible on touch screens only.


----


## Property Descriptions



[String<class_String>] **action** = `""` [🔗<class_TouchScreenButton_property_action>]


- |void| **set_action**\ (\ value\: [String<class_String>]\ )
- [String<class_String>] **get_action**\ (\ )

The button's action. Actions can be handled with [InputEventAction<class_InputEventAction>].


----



[BitMap<class_BitMap>] **bitmask** [🔗<class_TouchScreenButton_property_bitmask>]


- |void| **set_bitmask**\ (\ value\: [BitMap<class_BitMap>]\ )
- [BitMap<class_BitMap>] **get_bitmask**\ (\ )

The button's bitmask.


----



[bool<class_bool>] **passby_press** = `false` [🔗<class_TouchScreenButton_property_passby_press>]


- |void| **set_passby_press**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_passby_press_enabled**\ (\ )

If `true`, the [pressed<class_TouchScreenButton_signal_pressed>] and [released<class_TouchScreenButton_signal_released>] signals are emitted whenever a pressed finger goes in and out of the button, even if the pressure started outside the active area of the button.

\ **Note:** This is a "pass-by" (not "bypass") press mode.


----



[Shape2D<class_Shape2D>] **shape** [🔗<class_TouchScreenButton_property_shape>]


- |void| **set_shape**\ (\ value\: [Shape2D<class_Shape2D>]\ )
- [Shape2D<class_Shape2D>] **get_shape**\ (\ )

The button's shape.


----



[bool<class_bool>] **shape_centered** = `true` [🔗<class_TouchScreenButton_property_shape_centered>]


- |void| **set_shape_centered**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_shape_centered**\ (\ )

If `true`, the button's shape is centered in the provided texture. If no texture is used, this property has no effect.


----



[bool<class_bool>] **shape_visible** = `true` [🔗<class_TouchScreenButton_property_shape_visible>]


- |void| **set_shape_visible**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_shape_visible**\ (\ )

If `true`, the button's shape is visible in the editor.


----



[Texture2D<class_Texture2D>] **texture_normal** [🔗<class_TouchScreenButton_property_texture_normal>]


- |void| **set_texture_normal**\ (\ value\: [Texture2D<class_Texture2D>]\ )
- [Texture2D<class_Texture2D>] **get_texture_normal**\ (\ )

The button's texture for the normal state.


----



[Texture2D<class_Texture2D>] **texture_pressed** [🔗<class_TouchScreenButton_property_texture_pressed>]


- |void| **set_texture_pressed**\ (\ value\: [Texture2D<class_Texture2D>]\ )
- [Texture2D<class_Texture2D>] **get_texture_pressed**\ (\ )

The button's texture for the pressed state.


----



[VisibilityMode<enum_TouchScreenButton_VisibilityMode>] **visibility_mode** = `0` [🔗<class_TouchScreenButton_property_visibility_mode>]


- |void| **set_visibility_mode**\ (\ value\: [VisibilityMode<enum_TouchScreenButton_VisibilityMode>]\ )
- [VisibilityMode<enum_TouchScreenButton_VisibilityMode>] **get_visibility_mode**\ (\ )

The button's visibility mode.


----


## Method Descriptions



[bool<class_bool>] **is_pressed**\ (\ ) |const| [🔗<class_TouchScreenButton_method_is_pressed>]

Returns `true` if this button is currently pressed.

