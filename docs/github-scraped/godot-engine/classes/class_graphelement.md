:github_url: hide



# GraphElement

**Inherits:** [Container<class_Container>] **<** [Control<class_Control>] **<** [CanvasItem<class_CanvasItem>] **<** [Node<class_Node>] **<** [Object<class_Object>]

**Inherited By:** [GraphFrame<class_GraphFrame>], [GraphNode<class_GraphNode>]

A container that represents a basic element that can be placed inside a [GraphEdit<class_GraphEdit>] control.


## Description

**GraphElement** allows to create custom elements for a [GraphEdit<class_GraphEdit>] graph. By default such elements can be selected, resized, and repositioned, but they cannot be connected. For a graph element that allows for connections see [GraphNode<class_GraphNode>].


## Properties

> **TABLE**
> :widths: auto
>
> +-------------------------------+---------------------------------------------------------------------+-------------------+
> | :ref:`bool<class_bool>`       | :ref:`draggable<class_GraphElement_property_draggable>`             | ``true``          |
> +-------------------------------+---------------------------------------------------------------------+-------------------+
> | :ref:`Vector2<class_Vector2>` | :ref:`position_offset<class_GraphElement_property_position_offset>` | ``Vector2(0, 0)`` |
> +-------------------------------+---------------------------------------------------------------------+-------------------+
> | :ref:`bool<class_bool>`       | :ref:`resizable<class_GraphElement_property_resizable>`             | ``false``         |
> +-------------------------------+---------------------------------------------------------------------+-------------------+
> | :ref:`bool<class_bool>`       | :ref:`scaling_menus<class_GraphElement_property_scaling_menus>`     | ``false``         |
> +-------------------------------+---------------------------------------------------------------------+-------------------+
> | :ref:`bool<class_bool>`       | :ref:`selectable<class_GraphElement_property_selectable>`           | ``true``          |
> +-------------------------------+---------------------------------------------------------------------+-------------------+
> | :ref:`bool<class_bool>`       | :ref:`selected<class_GraphElement_property_selected>`               | ``false``         |
> +-------------------------------+---------------------------------------------------------------------+-------------------+
>

## Theme Properties

> **TABLE**
> :widths: auto
>
> +-----------------------------------+-------------------------------------------------------+
> | :ref:`Texture2D<class_Texture2D>` | :ref:`resizer<class_GraphElement_theme_icon_resizer>` |
> +-----------------------------------+-------------------------------------------------------+
>

----


## Signals



**delete_request**\ (\ ) [🔗<class_GraphElement_signal_delete_request>]

Emitted when removing the GraphElement is requested.


----



**dragged**\ (\ from\: [Vector2<class_Vector2>], to\: [Vector2<class_Vector2>]\ ) [🔗<class_GraphElement_signal_dragged>]

Emitted when the GraphElement is dragged.


----



**node_deselected**\ (\ ) [🔗<class_GraphElement_signal_node_deselected>]

Emitted when the GraphElement is deselected.


----



**node_selected**\ (\ ) [🔗<class_GraphElement_signal_node_selected>]

Emitted when the GraphElement is selected.


----



**position_offset_changed**\ (\ ) [🔗<class_GraphElement_signal_position_offset_changed>]

Emitted when the GraphElement is moved.


----



**raise_request**\ (\ ) [🔗<class_GraphElement_signal_raise_request>]

Emitted when displaying the GraphElement over other ones is requested. Happens on focusing (clicking into) the GraphElement.


----



**resize_end**\ (\ new_size\: [Vector2<class_Vector2>]\ ) [🔗<class_GraphElement_signal_resize_end>]

Emitted when releasing the mouse button after dragging the resizer handle (see [resizable<class_GraphElement_property_resizable>]).


----



**resize_request**\ (\ new_size\: [Vector2<class_Vector2>]\ ) [🔗<class_GraphElement_signal_resize_request>]

Emitted when resizing the GraphElement is requested. Happens on dragging the resizer handle (see [resizable<class_GraphElement_property_resizable>]).


----


## Property Descriptions



[bool<class_bool>] **draggable** = `true` [🔗<class_GraphElement_property_draggable>]


- |void| **set_draggable**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_draggable**\ (\ )

If `true`, the user can drag the GraphElement.


----



[Vector2<class_Vector2>] **position_offset** = `Vector2(0, 0)` [🔗<class_GraphElement_property_position_offset>]


- |void| **set_position_offset**\ (\ value\: [Vector2<class_Vector2>]\ )
- [Vector2<class_Vector2>] **get_position_offset**\ (\ )

The offset of the GraphElement, relative to the scroll offset of the [GraphEdit<class_GraphEdit>].


----



[bool<class_bool>] **resizable** = `false` [🔗<class_GraphElement_property_resizable>]


- |void| **set_resizable**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_resizable**\ (\ )

If `true`, the user can resize the GraphElement.

\ **Note:** Dragging the handle will only emit the [resize_request<class_GraphElement_signal_resize_request>] and [resize_end<class_GraphElement_signal_resize_end>] signals, the GraphElement needs to be resized manually.


----



[bool<class_bool>] **scaling_menus** = `false` [🔗<class_GraphElement_property_scaling_menus>]


- |void| **set_scaling_menus**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_scaling_menus**\ (\ )

If `true`, [PopupMenu<class_PopupMenu>]\ s that are descendants of the GraphElement are scaled with the [GraphEdit<class_GraphEdit>] zoom.


----



[bool<class_bool>] **selectable** = `true` [🔗<class_GraphElement_property_selectable>]


- |void| **set_selectable**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_selectable**\ (\ )

If `true`, the user can select the GraphElement.


----



[bool<class_bool>] **selected** = `false` [🔗<class_GraphElement_property_selected>]


- |void| **set_selected**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_selected**\ (\ )

If `true`, the GraphElement is selected.


----


## Theme Property Descriptions



[Texture2D<class_Texture2D>] **resizer** [🔗<class_GraphElement_theme_icon_resizer>]

The icon used for the resizer, visible when [resizable<class_GraphElement_property_resizable>] is enabled.

