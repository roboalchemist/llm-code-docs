:github_url: hide



# TextureButton

**Inherits:** [BaseButton<class_BaseButton>] **<** [Control<class_Control>] **<** [CanvasItem<class_CanvasItem>] **<** [Node<class_Node>] **<** [Object<class_Object>]

Texture-based button. Supports Pressed, Hover, Disabled and Focused states.


## Description

**TextureButton** has the same functionality as [Button<class_Button>], except it uses sprites instead of Godot's [Theme<class_Theme>] resource. It is faster to create, but it doesn't support localization like more complex [Control<class_Control>]\ s.

See also [BaseButton<class_BaseButton>] which contains common properties and methods associated with this node.

\ **Note:** Setting a texture for the "normal" state ([texture_normal<class_TextureButton_property_texture_normal>]) is recommended. If [texture_normal<class_TextureButton_property_texture_normal>] is not set, the **TextureButton** will still receive input events and be clickable, but the user will not be able to see it unless they activate another one of its states with a texture assigned (e.g., hover over it to show [texture_hover<class_TextureButton_property_texture_hover>]).


## Tutorials

- [3D Voxel Demo ](https://godotengine.org/asset-library/asset/2755)_


## Properties

> **TABLE**
> :widths: auto
>
> +----------------------------------------------------+------------------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>`                            | :ref:`flip_h<class_TextureButton_property_flip_h>`                           | ``false`` |
> +----------------------------------------------------+------------------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>`                            | :ref:`flip_v<class_TextureButton_property_flip_v>`                           | ``false`` |
> +----------------------------------------------------+------------------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>`                            | :ref:`ignore_texture_size<class_TextureButton_property_ignore_texture_size>` | ``false`` |
> +----------------------------------------------------+------------------------------------------------------------------------------+-----------+
> | :ref:`StretchMode<enum_TextureButton_StretchMode>` | :ref:`stretch_mode<class_TextureButton_property_stretch_mode>`               | ``2``     |
> +----------------------------------------------------+------------------------------------------------------------------------------+-----------+
> | :ref:`BitMap<class_BitMap>`                        | :ref:`texture_click_mask<class_TextureButton_property_texture_click_mask>`   |           |
> +----------------------------------------------------+------------------------------------------------------------------------------+-----------+
> | :ref:`Texture2D<class_Texture2D>`                  | :ref:`texture_disabled<class_TextureButton_property_texture_disabled>`       |           |
> +----------------------------------------------------+------------------------------------------------------------------------------+-----------+
> | :ref:`Texture2D<class_Texture2D>`                  | :ref:`texture_focused<class_TextureButton_property_texture_focused>`         |           |
> +----------------------------------------------------+------------------------------------------------------------------------------+-----------+
> | :ref:`Texture2D<class_Texture2D>`                  | :ref:`texture_hover<class_TextureButton_property_texture_hover>`             |           |
> +----------------------------------------------------+------------------------------------------------------------------------------+-----------+
> | :ref:`Texture2D<class_Texture2D>`                  | :ref:`texture_normal<class_TextureButton_property_texture_normal>`           |           |
> +----------------------------------------------------+------------------------------------------------------------------------------+-----------+
> | :ref:`Texture2D<class_Texture2D>`                  | :ref:`texture_pressed<class_TextureButton_property_texture_pressed>`         |           |
> +----------------------------------------------------+------------------------------------------------------------------------------+-----------+
>

----


## Enumerations



enum **StretchMode**: [🔗<enum_TextureButton_StretchMode>]



[StretchMode<enum_TextureButton_StretchMode>] **STRETCH_SCALE** = `0`

Scale to fit the node's bounding rectangle.



[StretchMode<enum_TextureButton_StretchMode>] **STRETCH_TILE** = `1`

Tile inside the node's bounding rectangle.



[StretchMode<enum_TextureButton_StretchMode>] **STRETCH_KEEP** = `2`

The texture keeps its original size and stays in the bounding rectangle's top-left corner.



[StretchMode<enum_TextureButton_StretchMode>] **STRETCH_KEEP_CENTERED** = `3`

The texture keeps its original size and stays centered in the node's bounding rectangle.



[StretchMode<enum_TextureButton_StretchMode>] **STRETCH_KEEP_ASPECT** = `4`

Scale the texture to fit the node's bounding rectangle, but maintain the texture's aspect ratio.



[StretchMode<enum_TextureButton_StretchMode>] **STRETCH_KEEP_ASPECT_CENTERED** = `5`

Scale the texture to fit the node's bounding rectangle, center it, and maintain its aspect ratio.



[StretchMode<enum_TextureButton_StretchMode>] **STRETCH_KEEP_ASPECT_COVERED** = `6`

Scale the texture so that the shorter side fits the bounding rectangle. The other side clips to the node's limits.


----


## Property Descriptions



[bool<class_bool>] **flip_h** = `false` [🔗<class_TextureButton_property_flip_h>]


- |void| **set_flip_h**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_flipped_h**\ (\ )

If `true`, texture is flipped horizontally.


----



[bool<class_bool>] **flip_v** = `false` [🔗<class_TextureButton_property_flip_v>]


- |void| **set_flip_v**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_flipped_v**\ (\ )

If `true`, texture is flipped vertically.


----



[bool<class_bool>] **ignore_texture_size** = `false` [🔗<class_TextureButton_property_ignore_texture_size>]


- |void| **set_ignore_texture_size**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_ignore_texture_size**\ (\ )

If `true`, the size of the texture won't be considered for minimum size calculation, so the **TextureButton** can be shrunk down past the texture size.


----



[StretchMode<enum_TextureButton_StretchMode>] **stretch_mode** = `2` [🔗<class_TextureButton_property_stretch_mode>]


- |void| **set_stretch_mode**\ (\ value\: [StretchMode<enum_TextureButton_StretchMode>]\ )
- [StretchMode<enum_TextureButton_StretchMode>] **get_stretch_mode**\ (\ )

Controls the texture's behavior when you resize the node's bounding rectangle. See the [StretchMode<enum_TextureButton_StretchMode>] constants for available options.


----



[BitMap<class_BitMap>] **texture_click_mask** [🔗<class_TextureButton_property_texture_click_mask>]


- |void| **set_click_mask**\ (\ value\: [BitMap<class_BitMap>]\ )
- [BitMap<class_BitMap>] **get_click_mask**\ (\ )

Pure black and white [BitMap<class_BitMap>] image to use for click detection. On the mask, white pixels represent the button's clickable area. Use it to create buttons with curved shapes.


----



[Texture2D<class_Texture2D>] **texture_disabled** [🔗<class_TextureButton_property_texture_disabled>]


- |void| **set_texture_disabled**\ (\ value\: [Texture2D<class_Texture2D>]\ )
- [Texture2D<class_Texture2D>] **get_texture_disabled**\ (\ )

Texture to display when the node is disabled. See [BaseButton.disabled<class_BaseButton_property_disabled>]. If not assigned, the **TextureButton** displays [texture_normal<class_TextureButton_property_texture_normal>] instead.


----



[Texture2D<class_Texture2D>] **texture_focused** [🔗<class_TextureButton_property_texture_focused>]


- |void| **set_texture_focused**\ (\ value\: [Texture2D<class_Texture2D>]\ )
- [Texture2D<class_Texture2D>] **get_texture_focused**\ (\ )

Texture to *overlay on the base texture* when the node has mouse or keyboard focus. Because [texture_focused<class_TextureButton_property_texture_focused>] is displayed on top of the base texture, a partially transparent texture should be used to ensure the base texture remains visible. A texture that represents an outline or an underline works well for this purpose. To disable the focus visual effect, assign a fully transparent texture of any size. Note that disabling the focus visual effect will harm keyboard/controller navigation usability, so this is not recommended for accessibility reasons.


----



[Texture2D<class_Texture2D>] **texture_hover** [🔗<class_TextureButton_property_texture_hover>]


- |void| **set_texture_hover**\ (\ value\: [Texture2D<class_Texture2D>]\ )
- [Texture2D<class_Texture2D>] **get_texture_hover**\ (\ )

Texture to display when the mouse hovers over the node. If not assigned, the **TextureButton** displays [texture_normal<class_TextureButton_property_texture_normal>] instead when hovered over.


----



[Texture2D<class_Texture2D>] **texture_normal** [🔗<class_TextureButton_property_texture_normal>]


- |void| **set_texture_normal**\ (\ value\: [Texture2D<class_Texture2D>]\ )
- [Texture2D<class_Texture2D>] **get_texture_normal**\ (\ )

Texture to display by default, when the node is **not** in the disabled, hover or pressed state. This texture is still displayed in the focused state, with [texture_focused<class_TextureButton_property_texture_focused>] drawn on top.


----



[Texture2D<class_Texture2D>] **texture_pressed** [🔗<class_TextureButton_property_texture_pressed>]


- |void| **set_texture_pressed**\ (\ value\: [Texture2D<class_Texture2D>]\ )
- [Texture2D<class_Texture2D>] **get_texture_pressed**\ (\ )

Texture to display on mouse down over the node, if the node has keyboard focus and the player presses the Enter key or if the player presses the [BaseButton.shortcut<class_BaseButton_property_shortcut>] key. If not assigned, the **TextureButton** displays [texture_hover<class_TextureButton_property_texture_hover>] instead when pressed.

