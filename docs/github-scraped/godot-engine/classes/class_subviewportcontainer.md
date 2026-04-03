:github_url: hide



# SubViewportContainer

**Inherits:** [Container<class_Container>] **<** [Control<class_Control>] **<** [CanvasItem<class_CanvasItem>] **<** [Node<class_Node>] **<** [Object<class_Object>]

A container used for displaying the contents of a [SubViewport<class_SubViewport>].


## Description

A container that displays the contents of underlying [SubViewport<class_SubViewport>] child nodes. It uses the combined size of the [SubViewport<class_SubViewport>]\ s as minimum size, unless [stretch<class_SubViewportContainer_property_stretch>] is enabled.

\ **Note:** Changing a **SubViewportContainer**'s [Control.scale<class_Control_property_scale>] will cause its contents to appear distorted. To change its visual size without causing distortion, adjust the node's margins instead (if it's not already in a container).

\ **Note:** The **SubViewportContainer** forwards mouse-enter and mouse-exit notifications to its sub-viewports.


## Properties

> **TABLE**
> :widths: auto
>
> +------------------------------------------+---------------------------------------------------------------------------+---------------------------------------------------------------------+
> | :ref:`FocusMode<enum_Control_FocusMode>` | focus_mode                                                                | ``1`` (overrides :ref:`Control<class_Control_property_focus_mode>`) |
> +------------------------------------------+---------------------------------------------------------------------------+---------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                  | :ref:`mouse_target<class_SubViewportContainer_property_mouse_target>`     | ``false``                                                           |
> +------------------------------------------+---------------------------------------------------------------------------+---------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                  | :ref:`stretch<class_SubViewportContainer_property_stretch>`               | ``false``                                                           |
> +------------------------------------------+---------------------------------------------------------------------------+---------------------------------------------------------------------+
> | :ref:`int<class_int>`                    | :ref:`stretch_shrink<class_SubViewportContainer_property_stretch_shrink>` | ``1``                                                               |
> +------------------------------------------+---------------------------------------------------------------------------+---------------------------------------------------------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +-------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>` | :ref:`_propagate_input_event<class_SubViewportContainer_private_method__propagate_input_event>`\ (\ event\: :ref:`InputEvent<class_InputEvent>`\ ) |virtual| |const| |
> +-------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Property Descriptions



[bool<class_bool>] **mouse_target** = `false` [🔗<class_SubViewportContainer_property_mouse_target>]


- |void| **set_mouse_target**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_mouse_target_enabled**\ (\ )

Configure, if either the **SubViewportContainer** or alternatively the [Control<class_Control>] nodes of its [SubViewport<class_SubViewport>] children should be available as targets of mouse-related functionalities, like identifying the drop target in drag-and-drop operations or cursor shape of hovered [Control<class_Control>] node.

If `false`, the [Control<class_Control>] nodes inside its [SubViewport<class_SubViewport>] children are considered as targets.

If `true`, the **SubViewportContainer** itself will be considered as a target.


----



[bool<class_bool>] **stretch** = `false` [🔗<class_SubViewportContainer_property_stretch>]


- |void| **set_stretch**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_stretch_enabled**\ (\ )

If `true`, the sub-viewport will be automatically resized to the control's size.

\ **Note:** If `true`, this will prohibit changing [SubViewport.size<class_SubViewport_property_size>] of its children manually.


----



[int<class_int>] **stretch_shrink** = `1` [🔗<class_SubViewportContainer_property_stretch_shrink>]


- |void| **set_stretch_shrink**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_stretch_shrink**\ (\ )

Divides the sub-viewport's effective resolution by this value while preserving its scale. This can be used to speed up rendering.

For example, a 1280×720 sub-viewport with [stretch_shrink<class_SubViewportContainer_property_stretch_shrink>] set to `2` will be rendered at 640×360 while occupying the same size in the container.

\ **Note:** [stretch<class_SubViewportContainer_property_stretch>] must be `true` for this property to work.


----


## Method Descriptions



[bool<class_bool>] **_propagate_input_event**\ (\ event\: [InputEvent<class_InputEvent>]\ ) |virtual| |const| [🔗<class_SubViewportContainer_private_method__propagate_input_event>]

**Experimental:** This method may be changed or removed in future versions.

Virtual method to be implemented by the user. If it returns `true`, the `event` is propagated to [SubViewport<class_SubViewport>] children. Propagation doesn't happen if it returns `false`. If the function is not implemented, all events are propagated to SubViewports.

