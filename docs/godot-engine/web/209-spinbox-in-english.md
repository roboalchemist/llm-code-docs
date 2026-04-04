# SpinBox in English

# SpinBox

Inherits:Range<Control<CanvasItem<Node<Object
An input field for numbers.

## Description

SpinBoxis a numerical input text field. It allows entering integers and floating-point numbers. TheSpinBoxalso has up and down buttons that can be clicked increase or decrease the value. The value can also be changed by dragging the mouse up or down over theSpinBox's arrows.
Additionally, mathematical expressions can be entered. These are evaluated when the user pressesEnterwhile editing theSpinBox's text field. This uses theExpressionclass to parse and evaluate the expression. The result of the expression is then set as the value of theSpinBox. Some examples of valid expressions are5+2*3,pow(2,4), andPI+sin(0.5). Expressions are case-sensitive.
Example:Create aSpinBox, disable its context menu and set its text alignment to right.

```
var spin_box = SpinBox.new()
add_child(spin_box)
var line_edit = spin_box.get_line_edit()
line_edit.context_menu_enabled = false
spin_box.horizontal_alignment = LineEdit.HORIZONTAL_ALIGNMENT_RIGHT
```

```
var spinBox = new SpinBox();
AddChild(spinBox);
var lineEdit = spinBox.GetLineEdit();
lineEdit.ContextMenuEnabled = false;
spinBox.AlignHorizontal = LineEdit.HorizontalAlignEnum.Right;
```

SeeRangeclass for more options over theSpinBox.
Note:With theSpinBox's context menu disabled, you can right-click the bottom half of the spinbox to set the value to its minimum, while right-clicking the top half sets the value to its maximum.
Note:SpinBoxrelies on an underlyingLineEditnode. To theme aSpinBox's background, add theme items forLineEditand customize them. TheLineEdithas theSpinBoxInnerLineEdittheme variation, so that you can give it a distinct appearance from regularLineEdits.
Note:If you want to implement drag and drop for the underlyingLineEdit, you can useControl.set_drag_forwarding()on the node returned byget_line_edit().

## Properties

| HorizontalAlignment | alignment | 0 |
|---|---|---|
| bool | custom_arrow_round | false |
| float | custom_arrow_step | 0.0 |
| bool | editable | true |
| String | prefix | "" |
| bool | select_all_on_focus | false |
| BitField[SizeFlags] | size_flags_vertical | 1(overridesControl) |
| float | step | 1.0(overridesRange) |
| String | suffix | "" |
| bool | update_on_text_changed | false |

HorizontalAlignment
alignment
bool
custom_arrow_round
false
float
custom_arrow_step
bool
editable
true
String
prefix
bool
select_all_on_focus
false
BitField[SizeFlags]
size_flags_vertical
1(overridesControl)
float
step
1.0(overridesRange)
String
suffix
bool
update_on_text_changed
false

## Methods

| void | apply() |
|---|---|
| LineEdit | get_line_edit() |

void
apply()
LineEdit
get_line_edit()

## Theme Properties

| Color | down_disabled_icon_modulate | Color(0.875,0.875,0.875,0.5) |
|---|---|---|
| Color | down_hover_icon_modulate | Color(0.95,0.95,0.95,1) |
| Color | down_icon_modulate | Color(0.875,0.875,0.875,1) |
| Color | down_pressed_icon_modulate | Color(0.95,0.95,0.95,1) |
| Color | up_disabled_icon_modulate | Color(0.875,0.875,0.875,0.5) |
| Color | up_hover_icon_modulate | Color(0.95,0.95,0.95,1) |
| Color | up_icon_modulate | Color(0.875,0.875,0.875,1) |
| Color | up_pressed_icon_modulate | Color(0.95,0.95,0.95,1) |
| int | buttons_vertical_separation | 0 |
| int | buttons_width | 16 |
| int | field_and_buttons_separation | 2 |
| int | set_min_buttons_width_from_icons | 1 |
| Texture2D | down |  |
| Texture2D | down_disabled |  |
| Texture2D | down_hover |  |
| Texture2D | down_pressed |  |
| Texture2D | up |  |
| Texture2D | up_disabled |  |
| Texture2D | up_hover |  |
| Texture2D | up_pressed |  |
| Texture2D | updown |  |
| StyleBox | down_background |  |
| StyleBox | down_background_disabled |  |
| StyleBox | down_background_hovered |  |
| StyleBox | down_background_pressed |  |
| StyleBox | field_and_buttons_separator |  |
| StyleBox | up_background |  |
| StyleBox | up_background_disabled |  |
| StyleBox | up_background_hovered |  |
| StyleBox | up_background_pressed |  |
| StyleBox | up_down_buttons_separator |  |

Color
down_disabled_icon_modulate
Color(0.875,0.875,0.875,0.5)
Color
down_hover_icon_modulate
Color(0.95,0.95,0.95,1)
Color
down_icon_modulate
Color(0.875,0.875,0.875,1)
Color
down_pressed_icon_modulate
Color(0.95,0.95,0.95,1)
Color
up_disabled_icon_modulate
Color(0.875,0.875,0.875,0.5)
Color
up_hover_icon_modulate
Color(0.95,0.95,0.95,1)
Color
up_icon_modulate
Color(0.875,0.875,0.875,1)
Color
up_pressed_icon_modulate
Color(0.95,0.95,0.95,1)
buttons_vertical_separation
buttons_width
field_and_buttons_separation
set_min_buttons_width_from_icons
Texture2D
down
Texture2D
down_disabled
Texture2D
down_hover
Texture2D
down_pressed
Texture2D
Texture2D
up_disabled
Texture2D
up_hover
Texture2D
up_pressed
Texture2D
updown
StyleBox
down_background
StyleBox
down_background_disabled
StyleBox
down_background_hovered
StyleBox
down_background_pressed
StyleBox
field_and_buttons_separator
StyleBox
up_background
StyleBox
up_background_disabled
StyleBox
up_background_hovered
StyleBox
up_background_pressed
StyleBox
up_down_buttons_separator

## Property Descriptions

HorizontalAlignmentalignment=0🔗

- voidset_horizontal_alignment(value:HorizontalAlignment)
voidset_horizontal_alignment(value:HorizontalAlignment)
- HorizontalAlignmentget_horizontal_alignment()
HorizontalAlignmentget_horizontal_alignment()
Changes the alignment of the underlyingLineEdit.
boolcustom_arrow_round=false🔗
- voidset_custom_arrow_round(value:bool)
voidset_custom_arrow_round(value:bool)
- boolis_custom_arrow_rounding()
boolis_custom_arrow_rounding()
Iftrue, the value will be rounded to a multiple ofcustom_arrow_stepwhen interacting with the arrow buttons. Otherwise, increments the value bycustom_arrow_stepand then rounds it according toRange.step.
floatcustom_arrow_step=0.0🔗
- voidset_custom_arrow_step(value:float)
voidset_custom_arrow_step(value:float)
- floatget_custom_arrow_step()
floatget_custom_arrow_step()
If not0, sets the step when interacting with the arrow buttons of theSpinBox.
Note:Range.valuewill still be rounded to a multiple ofRange.step.
booleditable=true🔗
- voidset_editable(value:bool)
voidset_editable(value:bool)
- boolis_editable()
boolis_editable()
Iftrue, theSpinBoxwill be editable. Otherwise, it will be read only.
Stringprefix=""🔗
- voidset_prefix(value:String)
voidset_prefix(value:String)
- Stringget_prefix()
Stringget_prefix()
Adds the specified prefix string before the numerical value of theSpinBox.
boolselect_all_on_focus=false🔗
- voidset_select_all_on_focus(value:bool)
voidset_select_all_on_focus(value:bool)
- boolis_select_all_on_focus()
boolis_select_all_on_focus()
Iftrue, theSpinBoxwill select the whole text when theLineEditgains focus. Clicking the up and down arrows won't trigger this behavior.
Stringsuffix=""🔗
- voidset_suffix(value:String)
voidset_suffix(value:String)
- Stringget_suffix()
Stringget_suffix()
Adds the specified suffix string after the numerical value of theSpinBox.
boolupdate_on_text_changed=false🔗
- voidset_update_on_text_changed(value:bool)
voidset_update_on_text_changed(value:bool)
- boolget_update_on_text_changed()
boolget_update_on_text_changed()
Sets the value of theRangefor thisSpinBoxwhen theLineEdittext ischangedinstead ofsubmitted. SeeLineEdit.text_changedandLineEdit.text_submitted.
Note:If set totrue, this will interfere with entering mathematical expressions in theSpinBox. TheSpinBoxwill try to evaluate the expression as you type, which means symbols like a trailing+are removed immediately by the expression being evaluated.

## Method Descriptions

voidapply()🔗
Applies the current value of thisSpinBox. This is equivalent to pressingEnterwhile editing theLineEditused by theSpinBox. This will causeLineEdit.text_submittedto be emitted and its currently contained expression to be evaluated.
LineEditget_line_edit()🔗
Returns theLineEditinstance from thisSpinBox. You can use it to access properties and methods ofLineEdit.
Warning:This is a required internal node, removing and freeing it may cause a crash. If you wish to hide it or any of its children, use theirCanvasItem.visibleproperty.

## Theme Property Descriptions

Colordown_disabled_icon_modulate=Color(0.875,0.875,0.875,0.5)🔗
Down button icon modulation color, when the button is disabled.
Colordown_hover_icon_modulate=Color(0.95,0.95,0.95,1)🔗
Down button icon modulation color, when the button is hovered.
Colordown_icon_modulate=Color(0.875,0.875,0.875,1)🔗
Down button icon modulation color.
Colordown_pressed_icon_modulate=Color(0.95,0.95,0.95,1)🔗
Down button icon modulation color, when the button is being pressed.
Colorup_disabled_icon_modulate=Color(0.875,0.875,0.875,0.5)🔗
Up button icon modulation color, when the button is disabled.
Colorup_hover_icon_modulate=Color(0.95,0.95,0.95,1)🔗
Up button icon modulation color, when the button is hovered.
Colorup_icon_modulate=Color(0.875,0.875,0.875,1)🔗
Up button icon modulation color.
Colorup_pressed_icon_modulate=Color(0.95,0.95,0.95,1)🔗
Up button icon modulation color, when the button is being pressed.
intbuttons_vertical_separation=0🔗
Vertical separation between the up and down buttons.
intbuttons_width=16🔗
Width of the up and down buttons. If smaller than any icon set on the buttons, the respective icon may overlap neighboring elements. If smaller than0, the width is automatically adjusted from the icon size.
intfield_and_buttons_separation=2🔗
Width of the horizontal separation between the text input field (LineEdit) and the buttons.
intset_min_buttons_width_from_icons=1🔗
If not0, the minimum button width corresponds to the widest of all icons set on those buttons, even ifbuttons_widthis smaller.
Texture2Ddown🔗
Down button icon, displayed in the middle of the down (value-decreasing) button.
Texture2Ddown_disabled🔗
Down button icon when the button is disabled.
Texture2Ddown_hover🔗
Down button icon when the button is hovered.
Texture2Ddown_pressed🔗
Down button icon when the button is being pressed.
Texture2Dup🔗
Up button icon, displayed in the middle of the up (value-increasing) button.
Texture2Dup_disabled🔗
Up button icon when the button is disabled.
Texture2Dup_hover🔗
Up button icon when the button is hovered.
Texture2Dup_pressed🔗
Up button icon when the button is being pressed.
Texture2Dupdown🔗
Single texture representing both the up and down buttons icons. It is displayed in the middle of the buttons and does not change upon interaction. If a valid icon is assigned, it will replaceupanddown.
StyleBoxdown_background🔗
Background style of the down button.
StyleBoxdown_background_disabled🔗
Background style of the down button when disabled.
StyleBoxdown_background_hovered🔗
Background style of the down button when hovered.
StyleBoxdown_background_pressed🔗
Background style of the down button when being pressed.
StyleBoxfield_and_buttons_separator🔗
StyleBoxdrawn in the space occupied by the separation between the input field and the buttons.
StyleBoxup_background🔗
Background style of the up button.
StyleBoxup_background_disabled🔗
Background style of the up button when disabled.
StyleBoxup_background_hovered🔗
Background style of the up button when hovered.
StyleBoxup_background_pressed🔗
Background style of the up button when being pressed.
StyleBoxup_down_buttons_separator🔗
StyleBoxdrawn in the space occupied by the separation between the up and down buttons.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
