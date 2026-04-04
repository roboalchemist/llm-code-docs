:github_url: hide



# SubViewport

**Inherits:** [Viewport<class_Viewport>] **<** [Node<class_Node>] **<** [Object<class_Object>]

An interface to a game world that doesn't create a window or draw to the screen directly.


## Description

**SubViewport** Isolates a rectangular region of a scene to be displayed independently. This can be used, for example, to display UI in 3D space.

\ **Note:** **SubViewport** is a [Viewport<class_Viewport>] that isn't a [Window<class_Window>], i.e. it doesn't draw anything by itself. To display anything, **SubViewport** must have a non-zero size and be either put inside a [SubViewportContainer<class_SubViewportContainer>] or assigned to a [ViewportTexture<class_ViewportTexture>].

\ **Note:** [InputEvent<class_InputEvent>]\ s are not passed to a standalone **SubViewport** by default. To ensure [InputEvent<class_InputEvent>] propagation, a **SubViewport** can be placed inside of a [SubViewportContainer<class_SubViewportContainer>].


## Tutorials

- [../tutorials/rendering/viewports](Using Viewports .md)

- [../tutorials/2d/2d_transforms](Viewport and canvas transforms .md)

- [GUI in 3D Viewport Demo ](https://godotengine.org/asset-library/asset/2807)_

- [3D in 2D Viewport Demo ](https://godotengine.org/asset-library/asset/2804)_

- [2D in 3D Viewport Demo ](https://godotengine.org/asset-library/asset/2803)_

- [Screen Capture Demo ](https://godotengine.org/asset-library/asset/2808)_

- [Dynamic Split Screen Demo ](https://godotengine.org/asset-library/asset/2806)_

- [3D Resolution Scaling Demo ](https://godotengine.org/asset-library/asset/2805)_


## Properties

> **TABLE**
> :widths: auto
>
> +------------------------------------------------+----------------------------------------------------------------------------------------+------------------------+
> | :ref:`ClearMode<enum_SubViewport_ClearMode>`   | :ref:`render_target_clear_mode<class_SubViewport_property_render_target_clear_mode>`   | ``0``                  |
> +------------------------------------------------+----------------------------------------------------------------------------------------+------------------------+
> | :ref:`UpdateMode<enum_SubViewport_UpdateMode>` | :ref:`render_target_update_mode<class_SubViewport_property_render_target_update_mode>` | ``2``                  |
> +------------------------------------------------+----------------------------------------------------------------------------------------+------------------------+
> | :ref:`Vector2i<class_Vector2i>`                | :ref:`size<class_SubViewport_property_size>`                                           | ``Vector2i(512, 512)`` |
> +------------------------------------------------+----------------------------------------------------------------------------------------+------------------------+
> | :ref:`Vector2i<class_Vector2i>`                | :ref:`size_2d_override<class_SubViewport_property_size_2d_override>`                   | ``Vector2i(0, 0)``     |
> +------------------------------------------------+----------------------------------------------------------------------------------------+------------------------+
> | :ref:`bool<class_bool>`                        | :ref:`size_2d_override_stretch<class_SubViewport_property_size_2d_override_stretch>`   | ``false``              |
> +------------------------------------------------+----------------------------------------------------------------------------------------+------------------------+
>

----


## Enumerations



enum **ClearMode**: [🔗<enum_SubViewport_ClearMode>]



[ClearMode<enum_SubViewport_ClearMode>] **CLEAR_MODE_ALWAYS** = `0`

Always clear the render target before drawing.



[ClearMode<enum_SubViewport_ClearMode>] **CLEAR_MODE_NEVER** = `1`

Never clear the render target.



[ClearMode<enum_SubViewport_ClearMode>] **CLEAR_MODE_ONCE** = `2`

Clear the render target on the next frame, then switch to [CLEAR_MODE_NEVER<class_SubViewport_constant_CLEAR_MODE_NEVER>].


----



enum **UpdateMode**: [🔗<enum_SubViewport_UpdateMode>]



[UpdateMode<enum_SubViewport_UpdateMode>] **UPDATE_DISABLED** = `0`

Do not update the render target.



[UpdateMode<enum_SubViewport_UpdateMode>] **UPDATE_ONCE** = `1`

Update the render target once, then switch to [UPDATE_DISABLED<class_SubViewport_constant_UPDATE_DISABLED>].



[UpdateMode<enum_SubViewport_UpdateMode>] **UPDATE_WHEN_VISIBLE** = `2`

Update the render target only when it is visible. This is the default value.



[UpdateMode<enum_SubViewport_UpdateMode>] **UPDATE_WHEN_PARENT_VISIBLE** = `3`

Update the render target only when its parent is visible.



[UpdateMode<enum_SubViewport_UpdateMode>] **UPDATE_ALWAYS** = `4`

Always update the render target.


----


## Property Descriptions



[ClearMode<enum_SubViewport_ClearMode>] **render_target_clear_mode** = `0` [🔗<class_SubViewport_property_render_target_clear_mode>]


- |void| **set_clear_mode**\ (\ value\: [ClearMode<enum_SubViewport_ClearMode>]\ )
- [ClearMode<enum_SubViewport_ClearMode>] **get_clear_mode**\ (\ )

The clear mode when the sub-viewport is used as a render target.

\ **Note:** This property is intended for 2D usage.


----



[UpdateMode<enum_SubViewport_UpdateMode>] **render_target_update_mode** = `2` [🔗<class_SubViewport_property_render_target_update_mode>]


- |void| **set_update_mode**\ (\ value\: [UpdateMode<enum_SubViewport_UpdateMode>]\ )
- [UpdateMode<enum_SubViewport_UpdateMode>] **get_update_mode**\ (\ )

The update mode when the sub-viewport is used as a render target.


----



[Vector2i<class_Vector2i>] **size** = `Vector2i(512, 512)` [🔗<class_SubViewport_property_size>]


- |void| **set_size**\ (\ value\: [Vector2i<class_Vector2i>]\ )
- [Vector2i<class_Vector2i>] **get_size**\ (\ )

The width and height of the sub-viewport. Must be set to a value greater than or equal to 2 pixels on both dimensions. Otherwise, nothing will be displayed.

\ **Note:** If the parent node is a [SubViewportContainer<class_SubViewportContainer>] and its [SubViewportContainer.stretch<class_SubViewportContainer_property_stretch>] is `true`, the viewport size cannot be changed manually.


----



[Vector2i<class_Vector2i>] **size_2d_override** = `Vector2i(0, 0)` [🔗<class_SubViewport_property_size_2d_override>]


- |void| **set_size_2d_override**\ (\ value\: [Vector2i<class_Vector2i>]\ )
- [Vector2i<class_Vector2i>] **get_size_2d_override**\ (\ )

The 2D size override of the sub-viewport. If either the width or height is `0`, the override is disabled.


----



[bool<class_bool>] **size_2d_override_stretch** = `false` [🔗<class_SubViewport_property_size_2d_override_stretch>]


- |void| **set_size_2d_override_stretch**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_size_2d_override_stretch_enabled**\ (\ )

If `true`, the 2D size override affects stretch as well.

