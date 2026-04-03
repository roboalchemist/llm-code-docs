# ColorPickerButton

# ColorPickerButton

Inherits:Button<BaseButton<Control<CanvasItem<Node<Object
A button that brings up aColorPickerwhen pressed.

## Description

Encapsulates aColorPicker, making it accessible by pressing a button. Pressing the button will toggle theColorPicker's visibility.
See alsoBaseButtonwhich contains common properties and methods associated with this node.
Note:By default, the button may not be wide enough for the color preview swatch to be visible. Make sure to setControl.custom_minimum_sizeto a big enough value to give the button enough space.

## Tutorials

- 2D GD Paint Demo
2D GD Paint Demo
- GUI Drag And Drop Demo
GUI Drag And Drop Demo

## Properties

| Color | color | Color(0,0,0,1) |
|---|---|---|
| bool | edit_alpha | true |
| bool | edit_intensity | true |
| bool | toggle_mode | true(overridesBaseButton) |

Color
color
Color(0,0,0,1)
bool
edit_alpha
true
bool
edit_intensity
true
bool
toggle_mode
true(overridesBaseButton)

## Methods

| ColorPicker | get_picker() |
|---|---|
| PopupPanel | get_popup() |

ColorPicker
get_picker()
PopupPanel
get_popup()

## Theme Properties

| Texture2D | bg |

Texture2D

## Signals

color_changed(color:Color)🔗
Emitted when the color changes.
picker_created()🔗
Emitted when theColorPickeris created (the button is pressed for the first time).
popup_closed()🔗
Emitted when theColorPickeris closed.

## Property Descriptions

Colorcolor=Color(0,0,0,1)🔗

- voidset_pick_color(value:Color)
voidset_pick_color(value:Color)
- Colorget_pick_color()
Colorget_pick_color()
The currently selected color.
booledit_alpha=true🔗
- voidset_edit_alpha(value:bool)
voidset_edit_alpha(value:bool)
- boolis_editing_alpha()
boolis_editing_alpha()
Iftrue, the alpha channel in the displayedColorPickerwill be visible.
booledit_intensity=true🔗
- voidset_edit_intensity(value:bool)
voidset_edit_intensity(value:bool)
- boolis_editing_intensity()
boolis_editing_intensity()
Iftrue, the intensity slider in the displayedColorPickerwill be visible.

## Method Descriptions

ColorPickerget_picker()🔗
Returns theColorPickerthat this node toggles.
Warning:This is a required internal node, removing and freeing it may cause a crash. If you wish to hide it or any of its children, use theirCanvasItem.visibleproperty.
PopupPanelget_popup()🔗
Returns the control'sPopupPanelwhich allows you to connect to popup signals. This allows you to handle events when the ColorPicker is shown or hidden.
Warning:This is a required internal node, removing and freeing it may cause a crash. If you wish to hide it or any of its children, use theirWindow.visibleproperty.

## Theme Property Descriptions

Texture2Dbg🔗
The background of the color preview rect on the button.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
