:github_url: hide



# BackBufferCopy

**Inherits:** [Node2D<class_Node2D>] **<** [CanvasItem<class_CanvasItem>] **<** [Node<class_Node>] **<** [Object<class_Object>]

A node that copies a region of the screen to a buffer for access in shader code.


## Description

Node for back-buffering the currently-displayed screen. The region defined in the **BackBufferCopy** node is buffered with the content of the screen it covers, or the entire screen according to the [copy_mode<class_BackBufferCopy_property_copy_mode>]. It can be accessed in shader scripts using the screen texture (i.e. a uniform sampler with `hint_screen_texture`).

\ **Note:** Since this node inherits from [Node2D<class_Node2D>] (and not [Control<class_Control>]), anchors and margins won't apply to child [Control<class_Control>]-derived nodes. This can be problematic when resizing the window. To avoid this, add [Control<class_Control>]-derived nodes as *siblings* to the **BackBufferCopy** node instead of adding them as children.


## Tutorials

- [../tutorials/shaders/screen-reading_shaders](Screen-reading shaders .md)


## Properties

> **TABLE**
> :widths: auto
>
> +-----------------------------------------------+-----------------------------------------------------------+---------------------------------+
> | :ref:`CopyMode<enum_BackBufferCopy_CopyMode>` | :ref:`copy_mode<class_BackBufferCopy_property_copy_mode>` | ``1``                           |
> +-----------------------------------------------+-----------------------------------------------------------+---------------------------------+
> | :ref:`Rect2<class_Rect2>`                     | :ref:`rect<class_BackBufferCopy_property_rect>`           | ``Rect2(-100, -100, 200, 200)`` |
> +-----------------------------------------------+-----------------------------------------------------------+---------------------------------+
>

----


## Enumerations



enum **CopyMode**: [🔗<enum_BackBufferCopy_CopyMode>]



[CopyMode<enum_BackBufferCopy_CopyMode>] **COPY_MODE_DISABLED** = `0`

Disables the buffering mode. This means the **BackBufferCopy** node will directly use the portion of screen it covers.



[CopyMode<enum_BackBufferCopy_CopyMode>] **COPY_MODE_RECT** = `1`

**BackBufferCopy** buffers a rectangular region.



[CopyMode<enum_BackBufferCopy_CopyMode>] **COPY_MODE_VIEWPORT** = `2`

**BackBufferCopy** buffers the entire screen.


----


## Property Descriptions



[CopyMode<enum_BackBufferCopy_CopyMode>] **copy_mode** = `1` [🔗<class_BackBufferCopy_property_copy_mode>]


- |void| **set_copy_mode**\ (\ value\: [CopyMode<enum_BackBufferCopy_CopyMode>]\ )
- [CopyMode<enum_BackBufferCopy_CopyMode>] **get_copy_mode**\ (\ )

Buffer mode.


----



[Rect2<class_Rect2>] **rect** = `Rect2(-100, -100, 200, 200)` [🔗<class_BackBufferCopy_property_rect>]


- |void| **set_rect**\ (\ value\: [Rect2<class_Rect2>]\ )
- [Rect2<class_Rect2>] **get_rect**\ (\ )

The area covered by the **BackBufferCopy**. Only used if [copy_mode<class_BackBufferCopy_property_copy_mode>] is [COPY_MODE_RECT<class_BackBufferCopy_constant_COPY_MODE_RECT>].

