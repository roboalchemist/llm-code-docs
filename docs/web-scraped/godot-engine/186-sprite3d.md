# Sprite3D

# Sprite3D

Inherits:SpriteBase3D<GeometryInstance3D<VisualInstance3D<Node3D<Node<Object
2D sprite node in a 3D world.

## Description

A node that displays a 2D texture in a 3D environment. The texture displayed can be a region from a larger atlas texture, or a frame from a sprite sheet animation. See alsoSpriteBase3Dwhere properties such as the billboard mode are defined.

## Properties

| int | frame | 0 |
|---|---|---|
| Vector2i | frame_coords | Vector2i(0,0) |
| int | hframes | 1 |
| bool | region_enabled | false |
| Rect2 | region_rect | Rect2(0,0,0,0) |
| Texture2D | texture |  |
| int | vframes | 1 |

frame
Vector2i
frame_coords
Vector2i(0,0)
hframes
bool
region_enabled
false
Rect2
region_rect
Rect2(0,0,0,0)
Texture2D
texture
vframes

## Signals

frame_changed()🔗
Emitted when theframechanges.
texture_changed()🔗
Emitted when thetexturechanges.

## Property Descriptions

intframe=0🔗

- voidset_frame(value:int)
voidset_frame(value:int)
- intget_frame()
intget_frame()
Current frame to display from sprite sheet.hframesorvframesmust be greater than 1. This property is automatically adjusted whenhframesorvframesare changed to keep pointing to the same visual frame (same column and row). If that's impossible, this value is reset to0.
Vector2iframe_coords=Vector2i(0,0)🔗
- voidset_frame_coords(value:Vector2i)
voidset_frame_coords(value:Vector2i)
- Vector2iget_frame_coords()
Vector2iget_frame_coords()
Coordinates of the frame to display from sprite sheet. This is as an alias for theframeproperty.hframesorvframesmust be greater than 1.
inthframes=1🔗
- voidset_hframes(value:int)
voidset_hframes(value:int)
- intget_hframes()
intget_hframes()
The number of columns in the sprite sheet. When this property is changed,frameis adjusted so that the same visual frame is maintained (same row and column). If that's impossible,frameis reset to0.
boolregion_enabled=false🔗
- voidset_region_enabled(value:bool)
voidset_region_enabled(value:bool)
- boolis_region_enabled()
boolis_region_enabled()
Iftrue, the sprite will useregion_rectand display only the specified part of its texture.
Rect2region_rect=Rect2(0,0,0,0)🔗
- voidset_region_rect(value:Rect2)
voidset_region_rect(value:Rect2)
- Rect2get_region_rect()
Rect2get_region_rect()
The region of the atlas texture to display.region_enabledmust betrue.
Texture2Dtexture🔗
- voidset_texture(value:Texture2D)
voidset_texture(value:Texture2D)
- Texture2Dget_texture()
Texture2Dget_texture()
Texture2Dobject to draw. IfGeometryInstance3D.material_overrideis used, this will be overridden. The size information is still used.
intvframes=1🔗
- voidset_vframes(value:int)
voidset_vframes(value:int)
- intget_vframes()
intget_vframes()
The number of rows in the sprite sheet. When this property is changed,frameis adjusted so that the same visual frame is maintained (same row and column). If that's impossible,frameis reset to0.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
