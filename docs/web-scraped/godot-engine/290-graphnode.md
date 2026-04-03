# GraphNode

# GraphNode
Inherits:GraphElement<Container<Control<CanvasItem<Node<Object
A container with connection ports, representing a node in aGraphEdit.

## Description
GraphNodeallows to create nodes for aGraphEditgraph with customizable content based on its child controls.GraphNodeis derived fromContainerand it is responsible for placing its children on screen. This works similar toVBoxContainer. Children, in turn, provideGraphNodewith so-called slots, each of which can have a connection port on either side.
EachGraphNodeslot is defined by its index and can provide the node with up to two ports: one on the left, and one on the right. By convention the left port is also referred to as theinput portand the right port is referred to as theoutput port. Each port can be enabled and configured individually, using different type and color. The type is an arbitrary value that you can define using your own considerations. The parentGraphEditwill receive this information on each connect and disconnect request.
Slots can be configured in the Inspector dock once you add at least one childControl. The properties are grouped by each slot's index in the "Slot" section.
Note:While GraphNode is set up using slots and slot indices, connections are made between the ports which are enabled. Because of thatGraphEdituses the port's index and not the slot's index. You can useget_input_port_slot()andget_output_port_slot()to get the slot index from the port index.

## Properties

| FocusMode | focus_mode | 3(overridesControl) |
|---|---|---|
| bool | ignore_invalid_connection_type | false |
| MouseFilter | mouse_filter | 0(overridesControl) |
| FocusMode | slots_focus_mode | 3 |
| String | title | "" |

FocusMode
focus_mode
3(overridesControl)
bool
ignore_invalid_connection_type
false
MouseFilter
mouse_filter
0(overridesControl)
FocusMode
slots_focus_mode
String
title

## Methods

| void | _draw_port(slot_index:int, position:Vector2i, left:bool, color:Color)virtual |
|---|---|
| void | clear_all_slots() |
| void | clear_slot(slot_index:int) |
| Color | get_input_port_color(port_idx:int) |
| int | get_input_port_count() |
| Vector2 | get_input_port_position(port_idx:int) |
| int | get_input_port_slot(port_idx:int) |
| int | get_input_port_type(port_idx:int) |
| Color | get_output_port_color(port_idx:int) |
| int | get_output_port_count() |
| Vector2 | get_output_port_position(port_idx:int) |
| int | get_output_port_slot(port_idx:int) |
| int | get_output_port_type(port_idx:int) |
| Color | get_slot_color_left(slot_index:int)const |
| Color | get_slot_color_right(slot_index:int)const |
| Texture2D | get_slot_custom_icon_left(slot_index:int)const |
| Texture2D | get_slot_custom_icon_right(slot_index:int)const |
| Variant | get_slot_metadata_left(slot_index:int)const |
| Variant | get_slot_metadata_right(slot_index:int)const |
| int | get_slot_type_left(slot_index:int)const |
| int | get_slot_type_right(slot_index:int)const |
| HBoxContainer | get_titlebar_hbox() |
| bool | is_slot_draw_stylebox(slot_index:int)const |
| bool | is_slot_enabled_left(slot_index:int)const |
| bool | is_slot_enabled_right(slot_index:int)const |
| void | set_slot(slot_index:int, enable_left_port:bool, type_left:int, color_left:Color, enable_right_port:bool, type_right:int, color_right:Color, custom_icon_left:Texture2D= null, custom_icon_right:Texture2D= null, draw_stylebox:bool= true) |
| void | set_slot_color_left(slot_index:int, color:Color) |
| void | set_slot_color_right(slot_index:int, color:Color) |
| void | set_slot_custom_icon_left(slot_index:int, custom_icon:Texture2D) |
| void | set_slot_custom_icon_right(slot_index:int, custom_icon:Texture2D) |
| void | set_slot_draw_stylebox(slot_index:int, enable:bool) |
| void | set_slot_enabled_left(slot_index:int, enable:bool) |
| void | set_slot_enabled_right(slot_index:int, enable:bool) |
| void | set_slot_metadata_left(slot_index:int, value:Variant) |
| void | set_slot_metadata_right(slot_index:int, value:Variant) |
| void | set_slot_type_left(slot_index:int, type:int) |
| void | set_slot_type_right(slot_index:int, type:int) |

void
_draw_port(slot_index:int, position:Vector2i, left:bool, color:Color)virtual
void
clear_all_slots()
void
clear_slot(slot_index:int)
Color
get_input_port_color(port_idx:int)
get_input_port_count()
Vector2
get_input_port_position(port_idx:int)
get_input_port_slot(port_idx:int)
get_input_port_type(port_idx:int)
Color
get_output_port_color(port_idx:int)
get_output_port_count()
Vector2
get_output_port_position(port_idx:int)
get_output_port_slot(port_idx:int)
get_output_port_type(port_idx:int)
Color
get_slot_color_left(slot_index:int)const
Color
get_slot_color_right(slot_index:int)const
Texture2D
get_slot_custom_icon_left(slot_index:int)const
Texture2D
get_slot_custom_icon_right(slot_index:int)const
Variant
get_slot_metadata_left(slot_index:int)const
Variant
get_slot_metadata_right(slot_index:int)const
get_slot_type_left(slot_index:int)const
get_slot_type_right(slot_index:int)const
HBoxContainer
get_titlebar_hbox()
bool
is_slot_draw_stylebox(slot_index:int)const
bool
is_slot_enabled_left(slot_index:int)const
bool
is_slot_enabled_right(slot_index:int)const
void
set_slot(slot_index:int, enable_left_port:bool, type_left:int, color_left:Color, enable_right_port:bool, type_right:int, color_right:Color, custom_icon_left:Texture2D= null, custom_icon_right:Texture2D= null, draw_stylebox:bool= true)
void
set_slot_color_left(slot_index:int, color:Color)
void
set_slot_color_right(slot_index:int, color:Color)
void
set_slot_custom_icon_left(slot_index:int, custom_icon:Texture2D)
void
set_slot_custom_icon_right(slot_index:int, custom_icon:Texture2D)
void
set_slot_draw_stylebox(slot_index:int, enable:bool)
void
set_slot_enabled_left(slot_index:int, enable:bool)
void
set_slot_enabled_right(slot_index:int, enable:bool)
void
set_slot_metadata_left(slot_index:int, value:Variant)
void
set_slot_metadata_right(slot_index:int, value:Variant)
void
set_slot_type_left(slot_index:int, type:int)
void
set_slot_type_right(slot_index:int, type:int)

## Theme Properties

| Color | resizer_color | Color(0.875,0.875,0.875,1) |
|---|---|---|
| int | port_h_offset | 0 |
| int | separation | 2 |
| Texture2D | port |  |
| StyleBox | panel |  |
| StyleBox | panel_focus |  |
| StyleBox | panel_selected |  |
| StyleBox | slot |  |
| StyleBox | slot_selected |  |
| StyleBox | titlebar |  |
| StyleBox | titlebar_selected |  |

Color
resizer_color
Color(0.875,0.875,0.875,1)
port_h_offset
separation
Texture2D
port
StyleBox
panel
StyleBox
panel_focus
StyleBox
panel_selected
StyleBox
slot
StyleBox
slot_selected
StyleBox
titlebar
StyleBox
titlebar_selected

## Signals
slot_sizes_changed()🔗
Emitted when any slot's size might have changed.
slot_updated(slot_index:int)🔗
Emitted when any GraphNode's slot is updated.

## Property Descriptions
boolignore_invalid_connection_type=false🔗
- voidset_ignore_invalid_connection_type(value:bool)
voidset_ignore_invalid_connection_type(value:bool)
- boolis_ignoring_valid_connection_type()
boolis_ignoring_valid_connection_type()
Iftrue, you can connect ports with different types, even if the connection was not explicitly allowed in the parentGraphEdit.
FocusModeslots_focus_mode=3🔗
- voidset_slots_focus_mode(value:FocusMode)
voidset_slots_focus_mode(value:FocusMode)
- FocusModeget_slots_focus_mode()
FocusModeget_slots_focus_mode()
Determines how connection slots can be focused.
- If set toControl.FOCUS_CLICK, connections can only be made with the mouse.
If set toControl.FOCUS_CLICK, connections can only be made with the mouse.
- If set toControl.FOCUS_ALL, slots can also be focused using theProjectSettings.input/ui_upandProjectSettings.input/ui_downand connected usingProjectSettings.input/ui_leftandProjectSettings.input/ui_rightinput actions.
If set toControl.FOCUS_ALL, slots can also be focused using theProjectSettings.input/ui_upandProjectSettings.input/ui_downand connected usingProjectSettings.input/ui_leftandProjectSettings.input/ui_rightinput actions.
- If set toControl.FOCUS_ACCESSIBILITY, slot input actions are only enabled when the screen reader is active.
If set toControl.FOCUS_ACCESSIBILITY, slot input actions are only enabled when the screen reader is active.
Stringtitle=""🔗
- voidset_title(value:String)
voidset_title(value:String)
- Stringget_title()
Stringget_title()
The text displayed in the GraphNode's title bar.

## Method Descriptions
void_draw_port(slot_index:int, position:Vector2i, left:bool, color:Color)virtual🔗
There is currently no description for this method. Please help us bycontributing one!
voidclear_all_slots()🔗
Disables all slots of the GraphNode. This will remove all input/output ports from the GraphNode.
voidclear_slot(slot_index:int)🔗
Disables the slot with the givenslot_index. This will remove the corresponding input and output port from the GraphNode.
Colorget_input_port_color(port_idx:int)🔗
Returns theColorof the input port with the givenport_idx.
intget_input_port_count()🔗
Returns the number of slots with an enabled input port.
Vector2get_input_port_position(port_idx:int)🔗
Returns the position of the input port with the givenport_idx.
intget_input_port_slot(port_idx:int)🔗
Returns the corresponding slot index of the input port with the givenport_idx.
intget_input_port_type(port_idx:int)🔗
Returns the type of the input port with the givenport_idx.
Colorget_output_port_color(port_idx:int)🔗
Returns theColorof the output port with the givenport_idx.
intget_output_port_count()🔗
Returns the number of slots with an enabled output port.
Vector2get_output_port_position(port_idx:int)🔗
Returns the position of the output port with the givenport_idx.
intget_output_port_slot(port_idx:int)🔗
Returns the corresponding slot index of the output port with the givenport_idx.
intget_output_port_type(port_idx:int)🔗
Returns the type of the output port with the givenport_idx.
Colorget_slot_color_left(slot_index:int)const🔗
Returns the left (input)Colorof the slot with the givenslot_index.
Colorget_slot_color_right(slot_index:int)const🔗
Returns the right (output)Colorof the slot with the givenslot_index.
Texture2Dget_slot_custom_icon_left(slot_index:int)const🔗
Returns the left (input) customTexture2Dof the slot with the givenslot_index.
Texture2Dget_slot_custom_icon_right(slot_index:int)const🔗
Returns the right (output) customTexture2Dof the slot with the givenslot_index.
Variantget_slot_metadata_left(slot_index:int)const🔗
Returns the left (input) metadata of the slot with the givenslot_index.
Variantget_slot_metadata_right(slot_index:int)const🔗
Returns the right (output) metadata of the slot with the givenslot_index.
intget_slot_type_left(slot_index:int)const🔗
Returns the left (input) type of the slot with the givenslot_index.
intget_slot_type_right(slot_index:int)const🔗
Returns the right (output) type of the slot with the givenslot_index.
HBoxContainerget_titlebar_hbox()🔗
Returns theHBoxContainerused for the title bar, only containing aLabelfor displaying the title by default. This can be used to add custom controls to the title bar such as option or close buttons.
boolis_slot_draw_stylebox(slot_index:int)const🔗
Returnstrueif the backgroundStyleBoxof the slot with the givenslot_indexis drawn.
boolis_slot_enabled_left(slot_index:int)const🔗
Returnstrueif left (input) side of the slot with the givenslot_indexis enabled.
boolis_slot_enabled_right(slot_index:int)const🔗
Returnstrueif right (output) side of the slot with the givenslot_indexis enabled.
voidset_slot(slot_index:int, enable_left_port:bool, type_left:int, color_left:Color, enable_right_port:bool, type_right:int, color_right:Color, custom_icon_left:Texture2D= null, custom_icon_right:Texture2D= null, draw_stylebox:bool= true)🔗
Sets properties of the slot with the givenslot_index.
Ifenable_left_port/enable_right_portistrue, a port will appear and the slot will be able to be connected from this side.
Withtype_left/type_rightan arbitrary type can be assigned to each port. Two ports can be connected if they share the same type, or if the connection between their types is allowed in the parentGraphEdit(seeGraphEdit.add_valid_connection_type()). Keep in mind that theGraphEdithas the final say in accepting the connection. Type compatibility simply allows theGraphEdit.connection_requestsignal to be emitted.
Ports can be further customized usingcolor_left/color_rightandcustom_icon_left/custom_icon_right. The color parameter adds a tint to the icon. The custom icon can be used to override the default port dot.
Additionally,draw_styleboxcan be used to enable or disable drawing of the background stylebox for each slot. Seeslot.
Individual properties can also be set using one of theset_slot_*methods.
Note:This method only sets properties of the slot. To create the slot itself, add aControl-derived child to the GraphNode.
voidset_slot_color_left(slot_index:int, color:Color)🔗
Sets theColorof the left (input) side of the slot with the givenslot_indextocolor.
voidset_slot_color_right(slot_index:int, color:Color)🔗
Sets theColorof the right (output) side of the slot with the givenslot_indextocolor.
voidset_slot_custom_icon_left(slot_index:int, custom_icon:Texture2D)🔗
Sets the customTexture2Dof the left (input) side of the slot with the givenslot_indextocustom_icon.
voidset_slot_custom_icon_right(slot_index:int, custom_icon:Texture2D)🔗
Sets the customTexture2Dof the right (output) side of the slot with the givenslot_indextocustom_icon.
voidset_slot_draw_stylebox(slot_index:int, enable:bool)🔗
Toggles the backgroundStyleBoxof the slot with the givenslot_index.
voidset_slot_enabled_left(slot_index:int, enable:bool)🔗
Toggles the left (input) side of the slot with the givenslot_index. Ifenableistrue, a port will appear on the left side and the slot will be able to be connected from this side.
voidset_slot_enabled_right(slot_index:int, enable:bool)🔗
Toggles the right (output) side of the slot with the givenslot_index. Ifenableistrue, a port will appear on the right side and the slot will be able to be connected from this side.
voidset_slot_metadata_left(slot_index:int, value:Variant)🔗
Sets the custom metadata for the left (input) side of the slot with the givenslot_indextovalue.
voidset_slot_metadata_right(slot_index:int, value:Variant)🔗
Sets the custom metadata for the right (output) side of the slot with the givenslot_indextovalue.
voidset_slot_type_left(slot_index:int, type:int)🔗
Sets the left (input) type of the slot with the givenslot_indextotype. If the value is negative, all connections will be disallowed to be created via user inputs.
voidset_slot_type_right(slot_index:int, type:int)🔗
Sets the right (output) type of the slot with the givenslot_indextotype. If the value is negative, all connections will be disallowed to be created via user inputs.

## Theme Property Descriptions
Colorresizer_color=Color(0.875,0.875,0.875,1)🔗
The color modulation applied to the resizer icon.
intport_h_offset=0🔗
Horizontal offset for the ports.
intseparation=2🔗
The vertical distance between ports.
Texture2Dport🔗
The icon used for representing ports.
StyleBoxpanel🔗
The default background for the slot area of theGraphNode.
StyleBoxpanel_focus🔗
StyleBoxused when theGraphNodeis focused (when used with assistive apps).
StyleBoxpanel_selected🔗
TheStyleBoxused for the slot area when selected.
StyleBoxslot🔗
TheStyleBoxused for each slot of theGraphNode.
StyleBoxslot_selected🔗
StyleBoxused when the slot is focused (when used with assistive apps).
StyleBoxtitlebar🔗
TheStyleBoxused for the title bar of theGraphNode.
StyleBoxtitlebar_selected🔗
TheStyleBoxused for the title bar of theGraphNodewhen it is selected.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.