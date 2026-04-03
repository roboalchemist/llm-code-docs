:github_url: hide

> **META**
	:keywords: tray



# StatusIndicator

**Inherits:** [Node<class_Node>] **<** [Object<class_Object>]

Application status indicator (aka notification area icon).

\ **Note:** Status indicator is implemented on macOS and Windows.


## Properties

> **TABLE**
> :widths: auto
>
> +-----------------------------------+--------------------------------------------------------+------------------+
> | :ref:`Texture2D<class_Texture2D>` | :ref:`icon<class_StatusIndicator_property_icon>`       |                  |
> +-----------------------------------+--------------------------------------------------------+------------------+
> | :ref:`NodePath<class_NodePath>`   | :ref:`menu<class_StatusIndicator_property_menu>`       | ``NodePath("")`` |
> +-----------------------------------+--------------------------------------------------------+------------------+
> | :ref:`String<class_String>`       | :ref:`tooltip<class_StatusIndicator_property_tooltip>` | ``""``           |
> +-----------------------------------+--------------------------------------------------------+------------------+
> | :ref:`bool<class_bool>`           | :ref:`visible<class_StatusIndicator_property_visible>` | ``true``         |
> +-----------------------------------+--------------------------------------------------------+------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +---------------------------+----------------------------------------------------------------------+
> | :ref:`Rect2<class_Rect2>` | :ref:`get_rect<class_StatusIndicator_method_get_rect>`\ (\ ) |const| |
> +---------------------------+----------------------------------------------------------------------+
>

----


## Signals



**pressed**\ (\ mouse_button\: [int<class_int>], mouse_position\: [Vector2i<class_Vector2i>]\ ) [🔗<class_StatusIndicator_signal_pressed>]

Emitted when the status indicator is pressed.


----


## Property Descriptions



[Texture2D<class_Texture2D>] **icon** [🔗<class_StatusIndicator_property_icon>]


- |void| **set_icon**\ (\ value\: [Texture2D<class_Texture2D>]\ )
- [Texture2D<class_Texture2D>] **get_icon**\ (\ )

Status indicator icon.


----



[NodePath<class_NodePath>] **menu** = `NodePath("")` [🔗<class_StatusIndicator_property_menu>]


- |void| **set_menu**\ (\ value\: [NodePath<class_NodePath>]\ )
- [NodePath<class_NodePath>] **get_menu**\ (\ )

Status indicator native popup menu. If this is set, the [pressed<class_StatusIndicator_signal_pressed>] signal is not emitted.

\ **Note:** Native popup is only supported if [NativeMenu<class_NativeMenu>] supports [NativeMenu.FEATURE_POPUP_MENU<class_NativeMenu_constant_FEATURE_POPUP_MENU>] feature.


----



[String<class_String>] **tooltip** = `""` [🔗<class_StatusIndicator_property_tooltip>]


- |void| **set_tooltip**\ (\ value\: [String<class_String>]\ )
- [String<class_String>] **get_tooltip**\ (\ )

Status indicator tooltip.


----



[bool<class_bool>] **visible** = `true` [🔗<class_StatusIndicator_property_visible>]


- |void| **set_visible**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_visible**\ (\ )

If `true`, the status indicator is visible.


----


## Method Descriptions



[Rect2<class_Rect2>] **get_rect**\ (\ ) |const| [🔗<class_StatusIndicator_method_get_rect>]

Returns the status indicator rectangle in screen coordinates. If this status indicator is not visible, returns an empty [Rect2<class_Rect2>].

