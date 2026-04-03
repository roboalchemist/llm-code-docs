:github_url: hide



# Popup

**Inherits:** [Window<class_Window>] **<** [Viewport<class_Viewport>] **<** [Node<class_Node>] **<** [Object<class_Object>]

**Inherited By:** [PopupMenu<class_PopupMenu>], [PopupPanel<class_PopupPanel>]

Base class for contextual windows and panels with fixed position.


## Description

**Popup** is a base class for contextual windows and panels with fixed position. It's a modal by default (see [Window.popup_window<class_Window_property_popup_window>]) and provides methods for implementing custom popup behavior.

\ **Note:** **Popup** is invisible by default. To make it visible, call one of the `popup_*` methods from [Window<class_Window>] on the node, such as [Window.popup_centered_clamped()<class_Window_method_popup_centered_clamped>].


## Properties

> **TABLE**
> :widths: auto
>
> +-------------------------+-------------------+-----------------------------------------------------------------------------+
> | :ref:`bool<class_bool>` | borderless        | ``true`` (overrides :ref:`Window<class_Window_property_borderless>`)        |
> +-------------------------+-------------------+-----------------------------------------------------------------------------+
> | :ref:`bool<class_bool>` | maximize_disabled | ``true`` (overrides :ref:`Window<class_Window_property_maximize_disabled>`) |
> +-------------------------+-------------------+-----------------------------------------------------------------------------+
> | :ref:`bool<class_bool>` | minimize_disabled | ``true`` (overrides :ref:`Window<class_Window_property_minimize_disabled>`) |
> +-------------------------+-------------------+-----------------------------------------------------------------------------+
> | :ref:`bool<class_bool>` | popup_window      | ``true`` (overrides :ref:`Window<class_Window_property_popup_window>`)      |
> +-------------------------+-------------------+-----------------------------------------------------------------------------+
> | :ref:`bool<class_bool>` | popup_wm_hint     | ``true`` (overrides :ref:`Window<class_Window_property_popup_wm_hint>`)     |
> +-------------------------+-------------------+-----------------------------------------------------------------------------+
> | :ref:`bool<class_bool>` | transient         | ``true`` (overrides :ref:`Window<class_Window_property_transient>`)         |
> +-------------------------+-------------------+-----------------------------------------------------------------------------+
> | :ref:`bool<class_bool>` | unresizable       | ``true`` (overrides :ref:`Window<class_Window_property_unresizable>`)       |
> +-------------------------+-------------------+-----------------------------------------------------------------------------+
> | :ref:`bool<class_bool>` | visible           | ``false`` (overrides :ref:`Window<class_Window_property_visible>`)          |
> +-------------------------+-------------------+-----------------------------------------------------------------------------+
> | :ref:`bool<class_bool>` | wrap_controls     | ``true`` (overrides :ref:`Window<class_Window_property_wrap_controls>`)     |
> +-------------------------+-------------------+-----------------------------------------------------------------------------+
>

----


## Signals



**popup_hide**\ (\ ) [🔗<class_Popup_signal_popup_hide>]

Emitted when the popup is hidden.

