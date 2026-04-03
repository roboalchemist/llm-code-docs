# TouchScreenButton in English

# TouchScreenButton
Inherits:Node2D<CanvasItem<Node<Object
Button for touch screen devices for gameplay use.

## Description
TouchScreenButton allows you to create on-screen buttons for touch devices. It's intended for gameplay use, such as a unit you have to touch to move. UnlikeButton, TouchScreenButton supports multitouch out of the box. Several TouchScreenButtons can be pressed at the same time with touch input.
This node inherits fromNode2D. Unlike withControlnodes, you cannot set anchors on it. If you want to create menus or user interfaces, you may want to useButtonnodes instead. To make button nodes react to touch events, you can enableProjectSettings.input_devices/pointing/emulate_mouse_from_touchin the Project Settings.
You can configure TouchScreenButton to be visible only on touch devices, helping you develop your game both for desktop and mobile devices.

## Properties

| String | action | "" |
|---|---|---|
| BitMap | bitmask |  |
| bool | passby_press | false |
| Shape2D | shape |  |
| bool | shape_centered | true |
| bool | shape_visible | true |
| Texture2D | texture_normal |  |
| Texture2D | texture_pressed |  |
| VisibilityMode | visibility_mode | 0 |

String
action
BitMap
bitmask
bool
passby_press
false
Shape2D
shape
bool
shape_centered
true
bool
shape_visible
true
Texture2D
texture_normal
Texture2D
texture_pressed
VisibilityMode
visibility_mode

## Methods

| bool | is_pressed()const |

bool
is_pressed()const

## Signals
pressed()🔗
Emitted when the button is pressed (down).
released()🔗
Emitted when the button is released (up).

## Enumerations
enumVisibilityMode:🔗
VisibilityModeVISIBILITY_ALWAYS=0
Always visible.
VisibilityModeVISIBILITY_TOUCHSCREEN_ONLY=1
Visible on touch screens only.

## Property Descriptions
Stringaction=""🔗
- voidset_action(value:String)
voidset_action(value:String)
- Stringget_action()
Stringget_action()
The button's action. Actions can be handled withInputEventAction.
BitMapbitmask🔗
- voidset_bitmask(value:BitMap)
voidset_bitmask(value:BitMap)
- BitMapget_bitmask()
BitMapget_bitmask()
The button's bitmask.
boolpassby_press=false🔗
- voidset_passby_press(value:bool)
voidset_passby_press(value:bool)
- boolis_passby_press_enabled()
boolis_passby_press_enabled()
Iftrue, thepressedandreleasedsignals are emitted whenever a pressed finger goes in and out of the button, even if the pressure started outside the active area of the button.
Note:This is a "pass-by" (not "bypass") press mode.
Shape2Dshape🔗
- voidset_shape(value:Shape2D)
voidset_shape(value:Shape2D)
- Shape2Dget_shape()
Shape2Dget_shape()
The button's shape.
boolshape_centered=true🔗
- voidset_shape_centered(value:bool)
voidset_shape_centered(value:bool)
- boolis_shape_centered()
boolis_shape_centered()
Iftrue, the button's shape is centered in the provided texture. If no texture is used, this property has no effect.
boolshape_visible=true🔗
- voidset_shape_visible(value:bool)
voidset_shape_visible(value:bool)
- boolis_shape_visible()
boolis_shape_visible()
Iftrue, the button's shape is visible in the editor.
Texture2Dtexture_normal🔗
- voidset_texture_normal(value:Texture2D)
voidset_texture_normal(value:Texture2D)
- Texture2Dget_texture_normal()
Texture2Dget_texture_normal()
The button's texture for the normal state.
Texture2Dtexture_pressed🔗
- voidset_texture_pressed(value:Texture2D)
voidset_texture_pressed(value:Texture2D)
- Texture2Dget_texture_pressed()
Texture2Dget_texture_pressed()
The button's texture for the pressed state.
VisibilityModevisibility_mode=0🔗
- voidset_visibility_mode(value:VisibilityMode)
voidset_visibility_mode(value:VisibilityMode)
- VisibilityModeget_visibility_mode()
VisibilityModeget_visibility_mode()
The button's visibility mode.

## Method Descriptions
boolis_pressed()const🔗
Returnstrueif this button is currently pressed.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.