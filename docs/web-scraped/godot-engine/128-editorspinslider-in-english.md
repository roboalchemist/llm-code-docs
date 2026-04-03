# EditorSpinSlider in English

# EditorSpinSlider

Inherits:Range<Control<CanvasItem<Node<Object
Godot editor's control for editing numeric values.

## Description

ThisControlnode is used in the editor's Inspector dock to allow editing of numeric values. Can be used withEditorInspectorPluginto recreate the same behavior.
If theRange.stepvalue is1, theEditorSpinSliderwill display up/down arrows, similar toSpinBox. If theRange.stepvalue is not1, a slider will be displayed instead.

## Properties

| ControlState | control_state | 0 |
|---|---|---|
| bool | editing_integer | false |
| bool | flat | false |
| FocusMode | focus_mode | 2(overridesControl) |
| bool | hide_slider | false |
| String | label | "" |
| bool | read_only | false |
| BitField[SizeFlags] | size_flags_vertical | 1(overridesControl) |
| float | step | 1.0(overridesRange) |
| String | suffix | "" |

ControlState
control_state
bool
editing_integer
false
bool
flat
false
FocusMode
focus_mode
2(overridesControl)
bool
hide_slider
false
String
label
bool
read_only
false
BitField[SizeFlags]
size_flags_vertical
1(overridesControl)
float
step
1.0(overridesRange)
String
suffix

## Theme Properties

| Texture2D | updown |
|---|---|
| Texture2D | updown_disabled |

Texture2D
updown
Texture2D
updown_disabled

## Signals

grabbed()🔗
Emitted when the spinner/slider is grabbed.
ungrabbed()🔗
Emitted when the spinner/slider is ungrabbed.
updown_pressed()🔗
Emitted when the updown button is pressed.
value_focus_entered()🔗
Emitted when the value form gains focus.
value_focus_exited()🔗
Emitted when the value form loses focus.

## Enumerations

enumControlState:🔗
ControlStateCONTROL_STATE_DEFAULT=0
The type of control used will depend on the value ofediting_integer. Up-down arrows iftrue, a slider iffalse.
ControlStateCONTROL_STATE_PREFER_SLIDER=1
A slider will always be used, even ifediting_integeris enabled.
ControlStateCONTROL_STATE_HIDE=2
Neither the up-down arrows nor the slider will be shown.

## Property Descriptions

ControlStatecontrol_state=0🔗

- voidset_control_state(value:ControlState)
voidset_control_state(value:ControlState)
- ControlStateget_control_state()
ControlStateget_control_state()
The state in which the control used to manipulate the value will be.
boolediting_integer=false🔗
- voidset_editing_integer(value:bool)
voidset_editing_integer(value:bool)
- boolis_editing_integer()
boolis_editing_integer()
Iftrue, theEditorSpinSlideris considered to be editing an integer value. Iffalse, theEditorSpinSlideris considered to be editing a floating-point value. This is used to determine whether a slider should be drawn by default. The slider is only drawn for floats; integers use up-down arrows similar toSpinBoxinstead, unlesscontrol_stateis set toCONTROL_STATE_PREFER_SLIDER. It will also useEditorSettings.interface/inspector/integer_drag_speedinstead ofEditorSettings.interface/inspector/float_drag_speedif the slider is available.
boolflat=false🔗
- voidset_flat(value:bool)
voidset_flat(value:bool)
- boolis_flat()
boolis_flat()
Iftrue, the slider will not draw background.
boolhide_slider=false🔗
- voidset_hide_slider(value:bool)
voidset_hide_slider(value:bool)
- boolis_hiding_slider()
boolis_hiding_slider()
Deprecated:Usecontrol_stateinstead.
Iftrue, the slider and up/down arrows are hidden.
Stringlabel=""🔗
- voidset_label(value:String)
voidset_label(value:String)
- Stringget_label()
Stringget_label()
The text that displays to the left of the value.
boolread_only=false🔗
- voidset_read_only(value:bool)
voidset_read_only(value:bool)
- boolis_read_only()
boolis_read_only()
Iftrue, the slider can't be interacted with.
Stringsuffix=""🔗
- voidset_suffix(value:String)
voidset_suffix(value:String)
- Stringget_suffix()
Stringget_suffix()
The suffix to display after the value (in a faded color). This should generally be a plural word. You may have to use an abbreviation if the suffix is too long to be displayed.

## Theme Property Descriptions

Texture2Dupdown🔗
Single texture representing both the up and down buttons.
Texture2Dupdown_disabled🔗
Single texture representing both the up and down buttons, when the control is readonly or disabled.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
