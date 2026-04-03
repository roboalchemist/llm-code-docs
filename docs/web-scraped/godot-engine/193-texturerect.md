# TextureRect

# TextureRect

Inherits:Control<CanvasItem<Node<Object
A control that displays a texture.

## Description

A control that displays a texture, for example an icon inside a GUI. The texture's placement can be controlled with thestretch_modeproperty. It can scale, tile, or stay centered inside its bounding rectangle.

## Tutorials

- 3D Voxel Demo
3D Voxel Demo

## Properties

| ExpandMode | expand_mode | 0 |
|---|---|---|
| bool | flip_h | false |
| bool | flip_v | false |
| MouseFilter | mouse_filter | 1(overridesControl) |
| StretchMode | stretch_mode | 0 |
| Texture2D | texture |  |

ExpandMode
expand_mode
bool
flip_h
false
bool
flip_v
false
MouseFilter
mouse_filter
1(overridesControl)
StretchMode
stretch_mode
Texture2D
texture

## Enumerations

enumExpandMode:🔗
ExpandModeEXPAND_KEEP_SIZE=0
The minimum size will be equal to texture size, i.e.TextureRectcan't be smaller than the texture.
ExpandModeEXPAND_IGNORE_SIZE=1
The size of the texture won't be considered for minimum size calculation, so theTextureRectcan be shrunk down past the texture size.
ExpandModeEXPAND_FIT_WIDTH=2
The height of the texture will be ignored. Minimum width will be equal to the current height. Useful for horizontal layouts, e.g. insideHBoxContainer.
ExpandModeEXPAND_FIT_WIDTH_PROPORTIONAL=3
Same asEXPAND_FIT_WIDTH, but keeps texture's aspect ratio.
ExpandModeEXPAND_FIT_HEIGHT=4
The width of the texture will be ignored. Minimum height will be equal to the current width. Useful for vertical layouts, e.g. insideVBoxContainer.
ExpandModeEXPAND_FIT_HEIGHT_PROPORTIONAL=5
Same asEXPAND_FIT_HEIGHT, but keeps texture's aspect ratio.
enumStretchMode:🔗
StretchModeSTRETCH_SCALE=0
Scale to fit the node's bounding rectangle.
StretchModeSTRETCH_TILE=1
Tile inside the node's bounding rectangle.
StretchModeSTRETCH_KEEP=2
The texture keeps its original size and stays in the bounding rectangle's top-left corner.
StretchModeSTRETCH_KEEP_CENTERED=3
The texture keeps its original size and stays centered in the node's bounding rectangle.
StretchModeSTRETCH_KEEP_ASPECT=4
Scale the texture to fit the node's bounding rectangle, but maintain the texture's aspect ratio.
StretchModeSTRETCH_KEEP_ASPECT_CENTERED=5
Scale the texture to fit the node's bounding rectangle, center it and maintain its aspect ratio.
StretchModeSTRETCH_KEEP_ASPECT_COVERED=6
Scale the texture so that the shorter side fits the bounding rectangle. The other side clips to the node's limits.

## Property Descriptions

ExpandModeexpand_mode=0🔗

- voidset_expand_mode(value:ExpandMode)
voidset_expand_mode(value:ExpandMode)
- ExpandModeget_expand_mode()
ExpandModeget_expand_mode()
Experimental:UsingEXPAND_FIT_WIDTH,EXPAND_FIT_WIDTH_PROPORTIONAL,EXPAND_FIT_HEIGHT, orEXPAND_FIT_HEIGHT_PROPORTIONALmay result in unstable behavior in someContainercontrols. This behavior may be re-evaluated and changed in the future.
Defines how minimum size is determined based on the texture's size.
boolflip_h=false🔗
- voidset_flip_h(value:bool)
voidset_flip_h(value:bool)
- boolis_flipped_h()
boolis_flipped_h()
Iftrue, texture is flipped horizontally.
boolflip_v=false🔗
- voidset_flip_v(value:bool)
voidset_flip_v(value:bool)
- boolis_flipped_v()
boolis_flipped_v()
Iftrue, texture is flipped vertically.
StretchModestretch_mode=0🔗
- voidset_stretch_mode(value:StretchMode)
voidset_stretch_mode(value:StretchMode)
- StretchModeget_stretch_mode()
StretchModeget_stretch_mode()
Controls the texture's behavior when resizing the node's bounding rectangle.
Texture2Dtexture🔗
- voidset_texture(value:Texture2D)
voidset_texture(value:Texture2D)
- Texture2Dget_texture()
Texture2Dget_texture()
The node'sTexture2Dresource.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
