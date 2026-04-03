# ButtonGroup in English

# ButtonGroup
Inherits:Resource<RefCounted<Object
A group of buttons that doesn't allow more than one button to be pressed at a time.

## Description
A group ofBaseButton-derived buttons. The buttons in aButtonGroupare treated like radio buttons: No more than one button can be pressed at a time. Some types of buttons (such asCheckBox) may have a special appearance in this state.
Every member of aButtonGroupshould haveBaseButton.toggle_modeset totrue.

## Properties

| bool | allow_unpress | false |
|---|---|---|
| bool | resource_local_to_scene | true(overridesResource) |

bool
allow_unpress
false
bool
resource_local_to_scene
true(overridesResource)

## Methods

| Array[BaseButton] | get_buttons() |
|---|---|
| BaseButton | get_pressed_button() |

Array[BaseButton]
get_buttons()
BaseButton
get_pressed_button()

## Signals
pressed(button:BaseButton)🔗
Emitted when one of the buttons of the group is pressed.

## Property Descriptions
boolallow_unpress=false🔗
- voidset_allow_unpress(value:bool)
voidset_allow_unpress(value:bool)
- boolis_allow_unpress()
boolis_allow_unpress()
Iftrue, it is possible to unpress all buttons in thisButtonGroup.

## Method Descriptions
Array[BaseButton]get_buttons()🔗
Returns anArrayofButtons who have this as theirButtonGroup(seeBaseButton.button_group).
BaseButtonget_pressed_button()🔗
Returns the current pressed button.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.