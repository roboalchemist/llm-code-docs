# Sprite2D in English

# Sprite2D

Inherits:Node2D<CanvasItem<Node<Object
General-purpose sprite node.

## Description

A node that displays a 2D texture. The texture displayed can be a region from a larger atlas texture, or a frame from a sprite sheet animation.

## Tutorials

- Instancing Demo
Instancing Demo

## Properties

| bool | centered | true |
|---|---|---|
| bool | flip_h | false |
| bool | flip_v | false |
| int | frame | 0 |
| Vector2i | frame_coords | Vector2i(0,0) |
| int | hframes | 1 |
| Vector2 | offset | Vector2(0,0) |
| bool | region_enabled | false |
| bool | region_filter_clip_enabled | false |
| Rect2 | region_rect | Rect2(0,0,0,0) |
| Texture2D | texture |  |
| int | vframes | 1 |

bool
centered
true
bool
flip_h
false
bool
flip_v
false
frame
Vector2i
frame_coords
Vector2i(0,0)
hframes
Vector2
offset
Vector2(0,0)
bool
region_enabled
false
bool
region_filter_clip_enabled
false
Rect2
region_rect
Rect2(0,0,0,0)
Texture2D
texture
vframes

## Methods

| Rect2 | get_rect()const |
|---|---|
| bool | is_pixel_opaque(pos:Vector2)const |

Rect2
get_rect()const
bool
is_pixel_opaque(pos:Vector2)const

## Signals

frame_changed()🔗
Emitted when theframechanges.
texture_changed()🔗
Emitted when thetexturechanges.

## Property Descriptions

boolcentered=true🔗

- voidset_centered(value:bool)
voidset_centered(value:bool)
- boolis_centered()
boolis_centered()
Iftrue, texture is centered.
Note:For games with a pixel art aesthetic, textures may appear deformed when centered. This is caused by their position being between pixels. To prevent this, set this property tofalse, or consider enablingProjectSettings.rendering/2d/snap/snap_2d_vertices_to_pixelandProjectSettings.rendering/2d/snap/snap_2d_transforms_to_pixel.
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
Vector2offset=Vector2(0,0)🔗
- voidset_offset(value:Vector2)
voidset_offset(value:Vector2)
- Vector2get_offset()
Vector2get_offset()
The texture's drawing offset.
Note:When you increaseoffset.y in Sprite2D, the sprite moves downward on screen (i.e., +Y is down).
boolregion_enabled=false🔗
- voidset_region_enabled(value:bool)
voidset_region_enabled(value:bool)
- boolis_region_enabled()
boolis_region_enabled()
Iftrue, texture is cut from a larger atlas texture. Seeregion_rect.
Note:When using a customShaderon aSprite2D, theUVshader built-in will refer to the entire texture space. Use theREGION_RECTbuilt-in to get the currently visible region defined inregion_rectinstead. SeeCanvasItem shadersfor details.
boolregion_filter_clip_enabled=false🔗
- voidset_region_filter_clip_enabled(value:bool)
voidset_region_filter_clip_enabled(value:bool)
- boolis_region_filter_clip_enabled()
boolis_region_filter_clip_enabled()
Iftrue, the area outside of theregion_rectis clipped to avoid bleeding of the surrounding texture pixels.region_enabledmust betrue.
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
Texture2Dobject to draw.
intvframes=1🔗
- voidset_vframes(value:int)
voidset_vframes(value:int)
- intget_vframes()
intget_vframes()
The number of rows in the sprite sheet. When this property is changed,frameis adjusted so that the same visual frame is maintained (same row and column). If that's impossible,frameis reset to0.

## Method Descriptions

Rect2get_rect()const🔗
Returns aRect2representing the Sprite2D's boundary in local coordinates.
Example:Detect if the Sprite2D was clicked:

```
func _input(event):
    if event is InputEventMouseButton and event.pressed and event.button_index == MOUSE_BUTTON_LEFT:
        if get_rect().has_point(to_local(event.position)):
            print("A click!")
```

```
public override void _Input(InputEvent @event)
{
    if (@event is InputEventMouseButton inputEventMouse)
    {
        if (inputEventMouse.Pressed && inputEventMouse.ButtonIndex == MouseButton.Left)
        {
            if (GetRect().HasPoint(ToLocal(inputEventMouse.Position)))
            {
                GD.Print("A click!");
            }
        }
    }
}
```

boolis_pixel_opaque(pos:Vector2)const🔗
Returnstrueif the pixel at the given position is opaque,falseotherwise. Also returnsfalseif the given position is out of bounds or this sprite'stextureisnull.posis in local coordinates.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
