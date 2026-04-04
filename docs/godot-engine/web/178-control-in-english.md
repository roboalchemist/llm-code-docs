# Control in English

# Control

Inherits:CanvasItem<Node<Object
Inherited By:BaseButton,ColorRect,Container,GraphEdit,ItemList,Label,LineEdit,MenuBar,NinePatchRect,Panel,Range,ReferenceRect,RichTextLabel,Separator,TabBar,TextEdit,TextureRect,Tree,VideoStreamPlayer
Base class for all GUI controls. Adapts its position and size based on its parent control.

## Description

Base class for all UI-related nodes.Controlfeatures a bounding rectangle that defines its extents, an anchor position relative to its parent control or the current viewport, and offsets relative to the anchor. The offsets update automatically when the node, any of its parents, or the screen size change.
For more information on Godot's UI system, anchors, offsets, and containers, see the related tutorials in the manual. To build flexible UIs, you'll need a mix of UI elements that inherit fromControlandContainernodes.
Note:Since bothNode2DandControlinherit fromCanvasItem, they share several concepts from the class such as theCanvasItem.z_indexandCanvasItem.visibleproperties.
User Interface nodes and input
Godot propagates input events via viewports. EachViewportis responsible for propagatingInputEvents to their child nodes. As theSceneTree.rootis aWindow, this already happens automatically for all UI elements in your game.
Input events are propagated through theSceneTreefrom the root node to all child nodes by callingNode._input(). For UI elements specifically, it makes more sense to override the virtual method_gui_input(), which filters out unrelated input events, such as by checking z-order,mouse_filter, focus, or if the event was inside of the control's bounding box.
Callaccept_event()so no other node receives the event. Once you accept an input, it becomes handled soNode._unhandled_input()will not process it.
Only oneControlnode can be in focus. Only the node in focus will receive events. To get the focus, callgrab_focus().Controlnodes lose focus when another node grabs it, or if you hide the node in focus. Focus will not be represented visually if gained via mouse/touch input, only appearing with keyboard/gamepad input (for accessibility), or viagrab_focus().
Setmouse_filtertoMOUSE_FILTER_IGNOREto tell aControlnode to ignore mouse or touch events. You'll need it if you place an icon on top of a button.
Themeresources change the control's appearance. Thethemeof aControlnode affects all of its direct and indirect children (as long as a chain of controls is uninterrupted). To override some of the theme items, call one of theadd_theme_*_overridemethods, likeadd_theme_font_override(). You can also override theme items in the Inspector.
Note:Theme items arenotObjectproperties. This means you can't access their values usingObject.get()andObject.set(). Instead, use theget_theme_*andadd_theme_*_overridemethods provided by this class.

## Tutorials

- GUI documentation index
GUI documentation index
- Custom drawing in 2D
Custom drawing in 2D
- Control node gallery
Control node gallery
- Multiple resolutions
Multiple resolutions
- All GUI Demos
All GUI Demos

## Properties

| Array[NodePath] | accessibility_controls_nodes | [] |
|---|---|---|
| Array[NodePath] | accessibility_described_by_nodes | [] |
| String | accessibility_description | "" |
| Array[NodePath] | accessibility_flow_to_nodes | [] |
| Array[NodePath] | accessibility_labeled_by_nodes | [] |
| AccessibilityLiveMode | accessibility_live | 0 |
| String | accessibility_name | "" |
| float | anchor_bottom | 0.0 |
| float | anchor_left | 0.0 |
| float | anchor_right | 0.0 |
| float | anchor_top | 0.0 |
| bool | auto_translate |  |
| bool | clip_contents | false |
| Vector2 | custom_minimum_size | Vector2(0,0) |
| FocusBehaviorRecursive | focus_behavior_recursive | 0 |
| FocusMode | focus_mode | 0 |
| NodePath | focus_neighbor_bottom | NodePath("") |
| NodePath | focus_neighbor_left | NodePath("") |
| NodePath | focus_neighbor_right | NodePath("") |
| NodePath | focus_neighbor_top | NodePath("") |
| NodePath | focus_next | NodePath("") |
| NodePath | focus_previous | NodePath("") |
| Vector2 | global_position |  |
| GrowDirection | grow_horizontal | 1 |
| GrowDirection | grow_vertical | 1 |
| LayoutDirection | layout_direction | 0 |
| bool | localize_numeral_system | true |
| MouseBehaviorRecursive | mouse_behavior_recursive | 0 |
| CursorShape | mouse_default_cursor_shape | 0 |
| MouseFilter | mouse_filter | 0 |
| bool | mouse_force_pass_scroll_events | true |
| float | offset_bottom | 0.0 |
| float | offset_left | 0.0 |
| float | offset_right | 0.0 |
| float | offset_top | 0.0 |
| PhysicsInterpolationMode | physics_interpolation_mode | 2(overridesNode) |
| Vector2 | pivot_offset | Vector2(0,0) |
| Vector2 | pivot_offset_ratio | Vector2(0,0) |
| Vector2 | position | Vector2(0,0) |
| float | rotation | 0.0 |
| float | rotation_degrees |  |
| Vector2 | scale | Vector2(1,1) |
| Node | shortcut_context |  |
| Vector2 | size | Vector2(0,0) |
| BitField[SizeFlags] | size_flags_horizontal | 1 |
| float | size_flags_stretch_ratio | 1.0 |
| BitField[SizeFlags] | size_flags_vertical | 1 |
| Theme | theme |  |
| StringName | theme_type_variation | &"" |
| AutoTranslateMode | tooltip_auto_translate_mode | 0 |
| String | tooltip_text | "" |

Array[NodePath]
accessibility_controls_nodes
Array[NodePath]
accessibility_described_by_nodes
String
accessibility_description
Array[NodePath]
accessibility_flow_to_nodes
Array[NodePath]
accessibility_labeled_by_nodes
AccessibilityLiveMode
accessibility_live
String
accessibility_name
float
anchor_bottom
float
anchor_left
float
anchor_right
float
anchor_top
bool
auto_translate
bool
clip_contents
false
Vector2
custom_minimum_size
Vector2(0,0)
FocusBehaviorRecursive
focus_behavior_recursive
FocusMode
focus_mode
NodePath
focus_neighbor_bottom
NodePath("")
NodePath
focus_neighbor_left
NodePath("")
NodePath
focus_neighbor_right
NodePath("")
NodePath
focus_neighbor_top
NodePath("")
NodePath
focus_next
NodePath("")
NodePath
focus_previous
NodePath("")
Vector2
global_position
GrowDirection
grow_horizontal
GrowDirection
grow_vertical
LayoutDirection
layout_direction
bool
localize_numeral_system
true
MouseBehaviorRecursive
mouse_behavior_recursive
CursorShape
mouse_default_cursor_shape
MouseFilter
mouse_filter
bool
mouse_force_pass_scroll_events
true
float
offset_bottom
float
offset_left
float
offset_right
float
offset_top
PhysicsInterpolationMode
physics_interpolation_mode
2(overridesNode)
Vector2
pivot_offset
Vector2(0,0)
Vector2
pivot_offset_ratio
Vector2(0,0)
Vector2
position
Vector2(0,0)
float
rotation
float
rotation_degrees
Vector2
scale
Vector2(1,1)
Node
shortcut_context
Vector2
size
Vector2(0,0)
BitField[SizeFlags]
size_flags_horizontal
float
size_flags_stretch_ratio
BitField[SizeFlags]
size_flags_vertical
Theme
theme
StringName
theme_type_variation
AutoTranslateMode
tooltip_auto_translate_mode
String
tooltip_text

## Methods

| String | _accessibility_get_contextual_info()virtualconst |
|---|---|
| bool | _can_drop_data(at_position:Vector2, data:Variant)virtualconst |
| void | _drop_data(at_position:Vector2, data:Variant)virtual |
| String | _get_accessibility_container_name(node:Node)virtualconst |
| Variant | _get_drag_data(at_position:Vector2)virtual |
| Vector2 | _get_minimum_size()virtualconst |
| String | _get_tooltip(at_position:Vector2)virtualconst |
| void | _gui_input(event:InputEvent)virtual |
| bool | _has_point(point:Vector2)virtualconst |
| Object | _make_custom_tooltip(for_text:String)virtualconst |
| Array[Vector3i] | _structured_text_parser(args:Array, text:String)virtualconst |
| void | accept_event() |
| void | accessibility_drag() |
| void | accessibility_drop() |
| void | add_theme_color_override(name:StringName, color:Color) |
| void | add_theme_constant_override(name:StringName, constant:int) |
| void | add_theme_font_override(name:StringName, font:Font) |
| void | add_theme_font_size_override(name:StringName, font_size:int) |
| void | add_theme_icon_override(name:StringName, texture:Texture2D) |
| void | add_theme_stylebox_override(name:StringName, stylebox:StyleBox) |
| void | begin_bulk_theme_override() |
| void | end_bulk_theme_override() |
| Control | find_next_valid_focus()const |
| Control | find_prev_valid_focus()const |
| Control | find_valid_focus_neighbor(side:Side)const |
| void | force_drag(data:Variant, preview:Control) |
| float | get_anchor(side:Side)const |
| Vector2 | get_begin()const |
| Vector2 | get_combined_minimum_size()const |
| Vector2 | get_combined_pivot_offset()const |
| CursorShape | get_cursor_shape(position:Vector2= Vector2(0, 0))const |
| Vector2 | get_end()const |
| FocusMode | get_focus_mode_with_override()const |
| NodePath | get_focus_neighbor(side:Side)const |
| Rect2 | get_global_rect()const |
| Vector2 | get_minimum_size()const |
| MouseFilter | get_mouse_filter_with_override()const |
| float | get_offset(offset:Side)const |
| Vector2 | get_parent_area_size()const |
| Control | get_parent_control()const |
| Rect2 | get_rect()const |
| Vector2 | get_screen_position()const |
| Color | get_theme_color(name:StringName, theme_type:StringName= &"")const |
| int | get_theme_constant(name:StringName, theme_type:StringName= &"")const |
| float | get_theme_default_base_scale()const |
| Font | get_theme_default_font()const |
| int | get_theme_default_font_size()const |
| Font | get_theme_font(name:StringName, theme_type:StringName= &"")const |
| int | get_theme_font_size(name:StringName, theme_type:StringName= &"")const |
| Texture2D | get_theme_icon(name:StringName, theme_type:StringName= &"")const |
| StyleBox | get_theme_stylebox(name:StringName, theme_type:StringName= &"")const |
| String | get_tooltip(at_position:Vector2= Vector2(0, 0))const |
| void | grab_click_focus() |
| void | grab_focus(hide_focus:bool= false) |
| bool | has_focus(ignore_hidden_focus:bool= false)const |
| bool | has_theme_color(name:StringName, theme_type:StringName= &"")const |
| bool | has_theme_color_override(name:StringName)const |
| bool | has_theme_constant(name:StringName, theme_type:StringName= &"")const |
| bool | has_theme_constant_override(name:StringName)const |
| bool | has_theme_font(name:StringName, theme_type:StringName= &"")const |
| bool | has_theme_font_override(name:StringName)const |
| bool | has_theme_font_size(name:StringName, theme_type:StringName= &"")const |
| bool | has_theme_font_size_override(name:StringName)const |
| bool | has_theme_icon(name:StringName, theme_type:StringName= &"")const |
| bool | has_theme_icon_override(name:StringName)const |
| bool | has_theme_stylebox(name:StringName, theme_type:StringName= &"")const |
| bool | has_theme_stylebox_override(name:StringName)const |
| bool | is_drag_successful()const |
| bool | is_layout_rtl()const |
| void | release_focus() |
| void | remove_theme_color_override(name:StringName) |
| void | remove_theme_constant_override(name:StringName) |
| void | remove_theme_font_override(name:StringName) |
| void | remove_theme_font_size_override(name:StringName) |
| void | remove_theme_icon_override(name:StringName) |
| void | remove_theme_stylebox_override(name:StringName) |
| void | reset_size() |
| void | set_anchor(side:Side, anchor:float, keep_offset:bool= false, push_opposite_anchor:bool= true) |
| void | set_anchor_and_offset(side:Side, anchor:float, offset:float, push_opposite_anchor:bool= false) |
| void | set_anchors_and_offsets_preset(preset:LayoutPreset, resize_mode:LayoutPresetMode= 0, margin:int= 0) |
| void | set_anchors_preset(preset:LayoutPreset, keep_offsets:bool= false) |
| void | set_begin(position:Vector2) |
| void | set_drag_forwarding(drag_func:Callable, can_drop_func:Callable, drop_func:Callable) |
| void | set_drag_preview(control:Control) |
| void | set_end(position:Vector2) |
| void | set_focus_neighbor(side:Side, neighbor:NodePath) |
| void | set_global_position(position:Vector2, keep_offsets:bool= false) |
| void | set_offset(side:Side, offset:float) |
| void | set_offsets_preset(preset:LayoutPreset, resize_mode:LayoutPresetMode= 0, margin:int= 0) |
| void | set_position(position:Vector2, keep_offsets:bool= false) |
| void | set_size(size:Vector2, keep_offsets:bool= false) |
| void | update_minimum_size() |
| void | warp_mouse(position:Vector2) |

String
_accessibility_get_contextual_info()virtualconst
bool
_can_drop_data(at_position:Vector2, data:Variant)virtualconst
void
_drop_data(at_position:Vector2, data:Variant)virtual
String
_get_accessibility_container_name(node:Node)virtualconst
Variant
_get_drag_data(at_position:Vector2)virtual
Vector2
_get_minimum_size()virtualconst
String
_get_tooltip(at_position:Vector2)virtualconst
void
_gui_input(event:InputEvent)virtual
bool
_has_point(point:Vector2)virtualconst
Object
_make_custom_tooltip(for_text:String)virtualconst
Array[Vector3i]
_structured_text_parser(args:Array, text:String)virtualconst
void
accept_event()
void
accessibility_drag()
void
accessibility_drop()
void
add_theme_color_override(name:StringName, color:Color)
void
add_theme_constant_override(name:StringName, constant:int)
void
add_theme_font_override(name:StringName, font:Font)
void
add_theme_font_size_override(name:StringName, font_size:int)
void
add_theme_icon_override(name:StringName, texture:Texture2D)
void
add_theme_stylebox_override(name:StringName, stylebox:StyleBox)
void
begin_bulk_theme_override()
void
end_bulk_theme_override()
Control
find_next_valid_focus()const
Control
find_prev_valid_focus()const
Control
find_valid_focus_neighbor(side:Side)const
void
force_drag(data:Variant, preview:Control)
float
get_anchor(side:Side)const
Vector2
get_begin()const
Vector2
get_combined_minimum_size()const
Vector2
get_combined_pivot_offset()const
CursorShape
get_cursor_shape(position:Vector2= Vector2(0, 0))const
Vector2
get_end()const
FocusMode
get_focus_mode_with_override()const
NodePath
get_focus_neighbor(side:Side)const
Rect2
get_global_rect()const
Vector2
get_minimum_size()const
MouseFilter
get_mouse_filter_with_override()const
float
get_offset(offset:Side)const
Vector2
get_parent_area_size()const
Control
get_parent_control()const
Rect2
get_rect()const
Vector2
get_screen_position()const
Color
get_theme_color(name:StringName, theme_type:StringName= &"")const
get_theme_constant(name:StringName, theme_type:StringName= &"")const
float
get_theme_default_base_scale()const
Font
get_theme_default_font()const
get_theme_default_font_size()const
Font
get_theme_font(name:StringName, theme_type:StringName= &"")const
get_theme_font_size(name:StringName, theme_type:StringName= &"")const
Texture2D
get_theme_icon(name:StringName, theme_type:StringName= &"")const
StyleBox
get_theme_stylebox(name:StringName, theme_type:StringName= &"")const
String
get_tooltip(at_position:Vector2= Vector2(0, 0))const
void
grab_click_focus()
void
grab_focus(hide_focus:bool= false)
bool
has_focus(ignore_hidden_focus:bool= false)const
bool
has_theme_color(name:StringName, theme_type:StringName= &"")const
bool
has_theme_color_override(name:StringName)const
bool
has_theme_constant(name:StringName, theme_type:StringName= &"")const
bool
has_theme_constant_override(name:StringName)const
bool
has_theme_font(name:StringName, theme_type:StringName= &"")const
bool
has_theme_font_override(name:StringName)const
bool
has_theme_font_size(name:StringName, theme_type:StringName= &"")const
bool
has_theme_font_size_override(name:StringName)const
bool
has_theme_icon(name:StringName, theme_type:StringName= &"")const
bool
has_theme_icon_override(name:StringName)const
bool
has_theme_stylebox(name:StringName, theme_type:StringName= &"")const
bool
has_theme_stylebox_override(name:StringName)const
bool
is_drag_successful()const
bool
is_layout_rtl()const
void
release_focus()
void
remove_theme_color_override(name:StringName)
void
remove_theme_constant_override(name:StringName)
void
remove_theme_font_override(name:StringName)
void
remove_theme_font_size_override(name:StringName)
void
remove_theme_icon_override(name:StringName)
void
remove_theme_stylebox_override(name:StringName)
void
reset_size()
void
set_anchor(side:Side, anchor:float, keep_offset:bool= false, push_opposite_anchor:bool= true)
void
set_anchor_and_offset(side:Side, anchor:float, offset:float, push_opposite_anchor:bool= false)
void
set_anchors_and_offsets_preset(preset:LayoutPreset, resize_mode:LayoutPresetMode= 0, margin:int= 0)
void
set_anchors_preset(preset:LayoutPreset, keep_offsets:bool= false)
void
set_begin(position:Vector2)
void
set_drag_forwarding(drag_func:Callable, can_drop_func:Callable, drop_func:Callable)
void
set_drag_preview(control:Control)
void
set_end(position:Vector2)
void
set_focus_neighbor(side:Side, neighbor:NodePath)
void
set_global_position(position:Vector2, keep_offsets:bool= false)
void
set_offset(side:Side, offset:float)
void
set_offsets_preset(preset:LayoutPreset, resize_mode:LayoutPresetMode= 0, margin:int= 0)
void
set_position(position:Vector2, keep_offsets:bool= false)
void
set_size(size:Vector2, keep_offsets:bool= false)
void
update_minimum_size()
void
warp_mouse(position:Vector2)

## Signals

focus_entered()🔗
Emitted when the node gains focus.
focus_exited()🔗
Emitted when the node loses focus.
gui_input(event:InputEvent)🔗
Emitted when the node receives anInputEvent.
minimum_size_changed()🔗
Emitted when the node's minimum size changes.
mouse_entered()🔗
Emitted when the mouse cursor enters the control's (or any child control's) visible area, that is not occluded behind other Controls or Windows, provided itsmouse_filterlets the event reach it and regardless if it's currently focused or not.
Note:CanvasItem.z_indexdoesn't affect, which Control receives the signal.
mouse_exited()🔗
Emitted when the mouse cursor leaves the control's (and all child control's) visible area, that is not occluded behind other Controls or Windows, provided itsmouse_filterlets the event reach it and regardless if it's currently focused or not.
Note:CanvasItem.z_indexdoesn't affect, which Control receives the signal.
Note:If you want to check whether the mouse truly left the area, ignoring any top nodes, you can use code like this:

```
func _on_mouse_exited():
    if not Rect2(Vector2(), size).has_point(get_local_mouse_position()):
        # Not hovering over area.
```

resized()🔗
Emitted when the control changes size.
size_flags_changed()🔗
Emitted when one of the size flags changes. Seesize_flags_horizontalandsize_flags_vertical.
theme_changed()🔗
Emitted when theNOTIFICATION_THEME_CHANGEDnotification is sent.

## Enumerations

enumFocusMode:🔗
FocusModeFOCUS_NONE=0
The node cannot grab focus. Use withfocus_mode.
FocusModeFOCUS_CLICK=1
The node can only grab focus on mouse clicks. Use withfocus_mode.
FocusModeFOCUS_ALL=2
The node can grab focus on mouse click, using the arrows and the Tab keys on the keyboard, or using the D-pad buttons on a gamepad. Use withfocus_mode.
FocusModeFOCUS_ACCESSIBILITY=3
The node can grab focus only when screen reader is active. Use withfocus_mode.
enumFocusBehaviorRecursive:🔗
FocusBehaviorRecursiveFOCUS_BEHAVIOR_INHERITED=0
Inherits thefocus_behavior_recursivefrom the parent control. If there is no parent control, this is the same asFOCUS_BEHAVIOR_ENABLED.
FocusBehaviorRecursiveFOCUS_BEHAVIOR_DISABLED=1
Prevents the control from getting focused.get_focus_mode_with_override()will returnFOCUS_NONE.
FocusBehaviorRecursiveFOCUS_BEHAVIOR_ENABLED=2
Allows the control to be focused, depending on thefocus_mode. This can be used to ignore the parent'sfocus_behavior_recursive.get_focus_mode_with_override()will return thefocus_mode.
enumMouseBehaviorRecursive:🔗
MouseBehaviorRecursiveMOUSE_BEHAVIOR_INHERITED=0
Inherits themouse_behavior_recursivefrom the parent control. If there is no parent control, this is the same asMOUSE_BEHAVIOR_ENABLED.
MouseBehaviorRecursiveMOUSE_BEHAVIOR_DISABLED=1
Prevents the control from receiving mouse input.get_mouse_filter_with_override()will returnMOUSE_FILTER_IGNORE.
MouseBehaviorRecursiveMOUSE_BEHAVIOR_ENABLED=2
Allows the control to receive mouse input, depending on themouse_filter. This can be used to ignore the parent'smouse_behavior_recursive.get_mouse_filter_with_override()will return themouse_filter.
enumCursorShape:🔗
CursorShapeCURSOR_ARROW=0
Show the system's arrow mouse cursor when the user hovers the node. Use withmouse_default_cursor_shape.
CursorShapeCURSOR_IBEAM=1
Show the system's I-beam mouse cursor when the user hovers the node. The I-beam pointer has a shape similar to "I". It tells the user they can highlight or insert text.
CursorShapeCURSOR_POINTING_HAND=2
Show the system's pointing hand mouse cursor when the user hovers the node.
CursorShapeCURSOR_CROSS=3
Show the system's cross mouse cursor when the user hovers the node.
CursorShapeCURSOR_WAIT=4
Show the system's wait mouse cursor when the user hovers the node. Often an hourglass.
CursorShapeCURSOR_BUSY=5
Show the system's busy mouse cursor when the user hovers the node. Often an arrow with a small hourglass.
CursorShapeCURSOR_DRAG=6
Show the system's drag mouse cursor, often a closed fist or a cross symbol, when the user hovers the node. It tells the user they're currently dragging an item, like a node in the Scene dock.
CursorShapeCURSOR_CAN_DROP=7
Show the system's drop mouse cursor when the user hovers the node. It can be an open hand. It tells the user they can drop an item they're currently grabbing, like a node in the Scene dock.
CursorShapeCURSOR_FORBIDDEN=8
Show the system's forbidden mouse cursor when the user hovers the node. Often a crossed circle.
CursorShapeCURSOR_VSIZE=9
Show the system's vertical resize mouse cursor when the user hovers the node. A double-headed vertical arrow. It tells the user they can resize the window or the panel vertically.
CursorShapeCURSOR_HSIZE=10
Show the system's horizontal resize mouse cursor when the user hovers the node. A double-headed horizontal arrow. It tells the user they can resize the window or the panel horizontally.
CursorShapeCURSOR_BDIAGSIZE=11
Show the system's window resize mouse cursor when the user hovers the node. The cursor is a double-headed arrow that goes from the bottom left to the top right. It tells the user they can resize the window or the panel both horizontally and vertically.
CursorShapeCURSOR_FDIAGSIZE=12
Show the system's window resize mouse cursor when the user hovers the node. The cursor is a double-headed arrow that goes from the top left to the bottom right, the opposite ofCURSOR_BDIAGSIZE. It tells the user they can resize the window or the panel both horizontally and vertically.
CursorShapeCURSOR_MOVE=13
Show the system's move mouse cursor when the user hovers the node. It shows 2 double-headed arrows at a 90 degree angle. It tells the user they can move a UI element freely.
CursorShapeCURSOR_VSPLIT=14
Show the system's vertical split mouse cursor when the user hovers the node. On Windows, it's the same asCURSOR_VSIZE.
CursorShapeCURSOR_HSPLIT=15
Show the system's horizontal split mouse cursor when the user hovers the node. On Windows, it's the same asCURSOR_HSIZE.
CursorShapeCURSOR_HELP=16
Show the system's help mouse cursor when the user hovers the node, a question mark.
enumLayoutPreset:🔗
LayoutPresetPRESET_TOP_LEFT=0
Snap all 4 anchors to the top-left of the parent control's bounds. Use withset_anchors_preset().
LayoutPresetPRESET_TOP_RIGHT=1
Snap all 4 anchors to the top-right of the parent control's bounds. Use withset_anchors_preset().
LayoutPresetPRESET_BOTTOM_LEFT=2
Snap all 4 anchors to the bottom-left of the parent control's bounds. Use withset_anchors_preset().
LayoutPresetPRESET_BOTTOM_RIGHT=3
Snap all 4 anchors to the bottom-right of the parent control's bounds. Use withset_anchors_preset().
LayoutPresetPRESET_CENTER_LEFT=4
Snap all 4 anchors to the center of the left edge of the parent control's bounds. Use withset_anchors_preset().
LayoutPresetPRESET_CENTER_TOP=5
Snap all 4 anchors to the center of the top edge of the parent control's bounds. Use withset_anchors_preset().
LayoutPresetPRESET_CENTER_RIGHT=6
Snap all 4 anchors to the center of the right edge of the parent control's bounds. Use withset_anchors_preset().
LayoutPresetPRESET_CENTER_BOTTOM=7
Snap all 4 anchors to the center of the bottom edge of the parent control's bounds. Use withset_anchors_preset().
LayoutPresetPRESET_CENTER=8
Snap all 4 anchors to the center of the parent control's bounds. Use withset_anchors_preset().
LayoutPresetPRESET_LEFT_WIDE=9
Snap all 4 anchors to the left edge of the parent control. The left offset becomes relative to the left edge and the top offset relative to the top left corner of the node's parent. Use withset_anchors_preset().
LayoutPresetPRESET_TOP_WIDE=10
Snap all 4 anchors to the top edge of the parent control. The left offset becomes relative to the top left corner, the top offset relative to the top edge, and the right offset relative to the top right corner of the node's parent. Use withset_anchors_preset().
LayoutPresetPRESET_RIGHT_WIDE=11
Snap all 4 anchors to the right edge of the parent control. The right offset becomes relative to the right edge and the top offset relative to the top right corner of the node's parent. Use withset_anchors_preset().
LayoutPresetPRESET_BOTTOM_WIDE=12
Snap all 4 anchors to the bottom edge of the parent control. The left offset becomes relative to the bottom left corner, the bottom offset relative to the bottom edge, and the right offset relative to the bottom right corner of the node's parent. Use withset_anchors_preset().
LayoutPresetPRESET_VCENTER_WIDE=13
Snap all 4 anchors to a vertical line that cuts the parent control in half. Use withset_anchors_preset().
LayoutPresetPRESET_HCENTER_WIDE=14
Snap all 4 anchors to a horizontal line that cuts the parent control in half. Use withset_anchors_preset().
LayoutPresetPRESET_FULL_RECT=15
Snap all 4 anchors to the respective corners of the parent control. Set all 4 offsets to 0 after you applied this preset and theControlwill fit its parent control. Use withset_anchors_preset().
enumLayoutPresetMode:🔗
LayoutPresetModePRESET_MODE_MINSIZE=0
The control will be resized to its minimum size.
LayoutPresetModePRESET_MODE_KEEP_WIDTH=1
The control's width will not change.
LayoutPresetModePRESET_MODE_KEEP_HEIGHT=2
The control's height will not change.
LayoutPresetModePRESET_MODE_KEEP_SIZE=3
The control's size will not change.
flagsSizeFlags:🔗
SizeFlagsSIZE_SHRINK_BEGIN=0
Tells the parentContainerto align the node with its start, either the top or the left edge. It is mutually exclusive withSIZE_FILLand other shrink size flags, but can be used withSIZE_EXPANDin some containers. Use withsize_flags_horizontalandsize_flags_vertical.
Note:Setting this flag is equal to not having any size flags.
SizeFlagsSIZE_FILL=1
Tells the parentContainerto expand the bounds of this node to fill all the available space without pushing any other node. It is mutually exclusive with shrink size flags. Use withsize_flags_horizontalandsize_flags_vertical.
SizeFlagsSIZE_EXPAND=2
Tells the parentContainerto let this node take all the available space on the axis you flag. If multiple neighboring nodes are set to expand, they'll share the space based on their stretch ratio. Seesize_flags_stretch_ratio. Use withsize_flags_horizontalandsize_flags_vertical.
SizeFlagsSIZE_EXPAND_FILL=3
Sets the node's size flags to both fill and expand. SeeSIZE_FILLandSIZE_EXPANDfor more information.
SizeFlagsSIZE_SHRINK_CENTER=4
Tells the parentContainerto center the node in the available space. It is mutually exclusive withSIZE_FILLand other shrink size flags, but can be used withSIZE_EXPANDin some containers. Use withsize_flags_horizontalandsize_flags_vertical.
SizeFlagsSIZE_SHRINK_END=8
Tells the parentContainerto align the node with its end, either the bottom or the right edge. It is mutually exclusive withSIZE_FILLand other shrink size flags, but can be used withSIZE_EXPANDin some containers. Use withsize_flags_horizontalandsize_flags_vertical.
enumMouseFilter:🔗
MouseFilterMOUSE_FILTER_STOP=0
The control will receive mouse movement input events and mouse button input events if clicked on through_gui_input(). The control will also receive themouse_enteredandmouse_exitedsignals. These events are automatically marked as handled, and they will not propagate further to other controls. This also results in blocking signals in other controls.
MouseFilterMOUSE_FILTER_PASS=1
The control will receive mouse movement input events and mouse button input events if clicked on through_gui_input(). The control will also receive themouse_enteredandmouse_exitedsignals.
If this control does not handle the event, the event will propagate up to its parent control if it has one. The event is bubbled up the node hierarchy until it reaches a non-CanvasItem, a control withMOUSE_FILTER_STOP, or aCanvasItemwithCanvasItem.top_levelenabled. This will allow signals to fire in all controls it reaches. If no control handled it, the event will be passed toNode._shortcut_input()for further processing.
MouseFilterMOUSE_FILTER_IGNORE=2
The control will not receive any mouse movement input events nor mouse button input events through_gui_input(). The control will also not receive themouse_enterednormouse_exitedsignals. This will not block other controls from receiving these events or firing the signals. Ignored events will not be handled automatically. If a child hasMOUSE_FILTER_PASSand an event was passed to this control, the event will further propagate up to the control's parent.
Note:If the control has receivedmouse_enteredbut notmouse_exited, changing themouse_filtertoMOUSE_FILTER_IGNOREwill causemouse_exitedto be emitted.
enumGrowDirection:🔗
GrowDirectionGROW_DIRECTION_BEGIN=0
The control will grow to the left or top to make up if its minimum size is changed to be greater than its current size on the respective axis.
GrowDirectionGROW_DIRECTION_END=1
The control will grow to the right or bottom to make up if its minimum size is changed to be greater than its current size on the respective axis.
GrowDirectionGROW_DIRECTION_BOTH=2
The control will grow in both directions equally to make up if its minimum size is changed to be greater than its current size.
enumAnchor:🔗
AnchorANCHOR_BEGIN=0
Snaps one of the 4 anchor's sides to the origin of the node'sRect, in the top left. Use it with one of theanchor_*member variables, likeanchor_left. To change all 4 anchors at once, useset_anchors_preset().
AnchorANCHOR_END=1
Snaps one of the 4 anchor's sides to the end of the node'sRect, in the bottom right. Use it with one of theanchor_*member variables, likeanchor_left. To change all 4 anchors at once, useset_anchors_preset().
enumLayoutDirection:🔗
LayoutDirectionLAYOUT_DIRECTION_INHERITED=0
Automatic layout direction, determined from the parent control layout direction.
LayoutDirectionLAYOUT_DIRECTION_APPLICATION_LOCALE=1
Automatic layout direction, determined from the current locale. Right-to-left layout direction is automatically used for languages that require it such as Arabic and Hebrew, but only if a valid translation file is loaded for the given language (unless said language is configured as a fallback inProjectSettings.internationalization/locale/fallback). For all other languages (or if no valid translation file is found by Godot), left-to-right layout direction is used. If usingTextServerFallback(ProjectSettings.internationalization/rendering/text_driver), left-to-right layout direction is always used regardless of the language. Right-to-left layout direction can also be forced usingProjectSettings.internationalization/rendering/force_right_to_left_layout_direction.
LayoutDirectionLAYOUT_DIRECTION_LTR=2
Left-to-right layout direction.
LayoutDirectionLAYOUT_DIRECTION_RTL=3
Right-to-left layout direction.
LayoutDirectionLAYOUT_DIRECTION_SYSTEM_LOCALE=4
Automatic layout direction, determined from the system locale. Right-to-left layout direction is automatically used for languages that require it such as Arabic and Hebrew, but only if a valid translation file is loaded for the given language. For all other languages (or if no valid translation file is found by Godot), left-to-right layout direction is used. If usingTextServerFallback(ProjectSettings.internationalization/rendering/text_driver), left-to-right layout direction is always used regardless of the language.
LayoutDirectionLAYOUT_DIRECTION_MAX=5
Represents the size of theLayoutDirectionenum.
LayoutDirectionLAYOUT_DIRECTION_LOCALE=1
Deprecated:UseLAYOUT_DIRECTION_APPLICATION_LOCALEinstead.
enumTextDirection:🔗
TextDirectionTEXT_DIRECTION_INHERITED=3
Text writing direction is the same as layout direction.
TextDirectionTEXT_DIRECTION_AUTO=0
Automatic text writing direction, determined from the current locale and text content.
TextDirectionTEXT_DIRECTION_LTR=1
Left-to-right text writing direction.
TextDirectionTEXT_DIRECTION_RTL=2
Right-to-left text writing direction.

## Constants

NOTIFICATION_RESIZED=40🔗
Sent when the node changes size. Usesizeto get the new size.
NOTIFICATION_MOUSE_ENTER=41🔗
Sent when the mouse cursor enters the control's (or any child control's) visible area, that is not occluded behind other Controls or Windows, provided itsmouse_filterlets the event reach it and regardless if it's currently focused or not.
Note:CanvasItem.z_indexdoesn't affect which Control receives the notification.
See alsoNOTIFICATION_MOUSE_ENTER_SELF.
NOTIFICATION_MOUSE_EXIT=42🔗
Sent when the mouse cursor leaves the control's (and all child control's) visible area, that is not occluded behind other Controls or Windows, provided itsmouse_filterlets the event reach it and regardless if it's currently focused or not.
Note:CanvasItem.z_indexdoesn't affect which Control receives the notification.
See alsoNOTIFICATION_MOUSE_EXIT_SELF.
NOTIFICATION_MOUSE_ENTER_SELF=60🔗
Experimental:The reason this notification is sent may change in the future.
Sent when the mouse cursor enters the control's visible area, that is not occluded behind other Controls or Windows, provided itsmouse_filterlets the event reach it and regardless if it's currently focused or not.
Note:CanvasItem.z_indexdoesn't affect which Control receives the notification.
See alsoNOTIFICATION_MOUSE_ENTER.
NOTIFICATION_MOUSE_EXIT_SELF=61🔗
Experimental:The reason this notification is sent may change in the future.
Sent when the mouse cursor leaves the control's visible area, that is not occluded behind other Controls or Windows, provided itsmouse_filterlets the event reach it and regardless if it's currently focused or not.
Note:CanvasItem.z_indexdoesn't affect which Control receives the notification.
See alsoNOTIFICATION_MOUSE_EXIT.
NOTIFICATION_FOCUS_ENTER=43🔗
Sent when the node grabs focus.
NOTIFICATION_FOCUS_EXIT=44🔗
Sent when the node loses focus.
This notification is sent in reversed order.
NOTIFICATION_THEME_CHANGED=45🔗
Sent when the node needs to refresh its theme items. This happens in one of the following cases:

- Thethemeproperty is changed on this node or any of its ancestors.
Thethemeproperty is changed on this node or any of its ancestors.
- Thetheme_type_variationproperty is changed on this node.
Thetheme_type_variationproperty is changed on this node.
- One of the node's theme property overrides is changed.
One of the node's theme property overrides is changed.
- The node enters the scene tree.
The node enters the scene tree.
Note:As an optimization, this notification won't be sent from changes that occur while this node is outside of the scene tree. Instead, all of the theme item updates can be applied at once when the node enters the scene tree.
Note:This notification is received alongsideNode.NOTIFICATION_ENTER_TREE, so if you are instantiating a scene, the child nodes will not be initialized yet. You can use it to setup theming for this node, child nodes created from script, or if you want to access child nodes added in the editor, make sure the node is ready usingNode.is_node_ready().

```
func _notification(what):
    if what == NOTIFICATION_THEME_CHANGED:
        if not is_node_ready():
            await ready # Wait until ready signal.
        $Label.add_theme_color_override("font_color", Color.YELLOW)
```

NOTIFICATION_SCROLL_BEGIN=47🔗
Sent when this node is inside aScrollContainerwhich has begun being scrolled when dragging the scrollable areawith a touch event. This notification isnotsent when scrolling by dragging the scrollbar, scrolling with the mouse wheel or scrolling with keyboard/gamepad events.
Note:This signal is only emitted on Android or iOS, or on desktop/web platforms whenProjectSettings.input_devices/pointing/emulate_touch_from_mouseis enabled.
NOTIFICATION_SCROLL_END=48🔗
Sent when this node is inside aScrollContainerwhich has stopped being scrolled when dragging the scrollable areawith a touch event. This notification isnotsent when scrolling by dragging the scrollbar, scrolling with the mouse wheel or scrolling with keyboard/gamepad events.
Note:This signal is only emitted on Android or iOS, or on desktop/web platforms whenProjectSettings.input_devices/pointing/emulate_touch_from_mouseis enabled.
NOTIFICATION_LAYOUT_DIRECTION_CHANGED=49🔗
Sent when the control layout direction is changed from LTR or RTL or vice versa. This notification is propagated to child Control nodes as result of a change tolayout_direction.

## Property Descriptions

Array[NodePath]accessibility_controls_nodes=[]🔗

- voidset_accessibility_controls_nodes(value:Array[NodePath])
voidset_accessibility_controls_nodes(value:Array[NodePath])
- Array[NodePath]get_accessibility_controls_nodes()
Array[NodePath]get_accessibility_controls_nodes()
The paths to the nodes which are controlled by this node.
Array[NodePath]accessibility_described_by_nodes=[]🔗
- voidset_accessibility_described_by_nodes(value:Array[NodePath])
voidset_accessibility_described_by_nodes(value:Array[NodePath])
- Array[NodePath]get_accessibility_described_by_nodes()
Array[NodePath]get_accessibility_described_by_nodes()
The paths to the nodes which are describing this node.
Stringaccessibility_description=""🔗
- voidset_accessibility_description(value:String)
voidset_accessibility_description(value:String)
- Stringget_accessibility_description()
Stringget_accessibility_description()
The human-readable node description that is reported to assistive apps.
Array[NodePath]accessibility_flow_to_nodes=[]🔗
- voidset_accessibility_flow_to_nodes(value:Array[NodePath])
voidset_accessibility_flow_to_nodes(value:Array[NodePath])
- Array[NodePath]get_accessibility_flow_to_nodes()
Array[NodePath]get_accessibility_flow_to_nodes()
The paths to the nodes which this node flows into.
Array[NodePath]accessibility_labeled_by_nodes=[]🔗
- voidset_accessibility_labeled_by_nodes(value:Array[NodePath])
voidset_accessibility_labeled_by_nodes(value:Array[NodePath])
- Array[NodePath]get_accessibility_labeled_by_nodes()
Array[NodePath]get_accessibility_labeled_by_nodes()
The paths to the nodes which label this node.
AccessibilityLiveModeaccessibility_live=0🔗
- voidset_accessibility_live(value:AccessibilityLiveMode)
voidset_accessibility_live(value:AccessibilityLiveMode)
- AccessibilityLiveModeget_accessibility_live()
AccessibilityLiveModeget_accessibility_live()
The mode with which a live region updates. A live region is aNodethat is updated as a result of an external event when the user's focus may be elsewhere.
Stringaccessibility_name=""🔗
- voidset_accessibility_name(value:String)
voidset_accessibility_name(value:String)
- Stringget_accessibility_name()
Stringget_accessibility_name()
The human-readable node name that is reported to assistive apps.
floatanchor_bottom=0.0🔗
- floatget_anchor(side:Side)const
floatget_anchor(side:Side)const
Anchors the bottom edge of the node to the origin, the center, or the end of its parent control. It changes how the bottom offset updates when the node moves or changes size. You can use one of theAnchorconstants for convenience.
floatanchor_left=0.0🔗
- floatget_anchor(side:Side)const
floatget_anchor(side:Side)const
Anchors the left edge of the node to the origin, the center or the end of its parent control. It changes how the left offset updates when the node moves or changes size. You can use one of theAnchorconstants for convenience.
floatanchor_right=0.0🔗
- floatget_anchor(side:Side)const
floatget_anchor(side:Side)const
Anchors the right edge of the node to the origin, the center or the end of its parent control. It changes how the right offset updates when the node moves or changes size. You can use one of theAnchorconstants for convenience.
floatanchor_top=0.0🔗
- floatget_anchor(side:Side)const
floatget_anchor(side:Side)const
Anchors the top edge of the node to the origin, the center or the end of its parent control. It changes how the top offset updates when the node moves or changes size. You can use one of theAnchorconstants for convenience.
boolauto_translate🔗
- voidset_auto_translate(value:bool)
voidset_auto_translate(value:bool)
- boolis_auto_translating()
boolis_auto_translating()
Deprecated:UseNode.auto_translate_modeandNode.can_auto_translate()instead.
Toggles if any text should automatically change to its translated version depending on the current locale.
boolclip_contents=false🔗
- voidset_clip_contents(value:bool)
voidset_clip_contents(value:bool)
- boolis_clipping_contents()
boolis_clipping_contents()
Enables whether rendering ofCanvasItembased children should be clipped to this control's rectangle. Iftrue, parts of a child which would be visibly outside of this control's rectangle will not be rendered and won't receive input.
Vector2custom_minimum_size=Vector2(0,0)🔗
- voidset_custom_minimum_size(value:Vector2)
voidset_custom_minimum_size(value:Vector2)
- Vector2get_custom_minimum_size()
Vector2get_custom_minimum_size()
The minimum size of the node's bounding rectangle. If you set it to a value greater than(0,0), the node's bounding rectangle will always have at least this size. Note thatControlnodes have their internal minimum size returned byget_minimum_size(). It depends on the control's contents, like text, textures, or style boxes. The actual minimum size is the maximum value of this property and the internal minimum size (seeget_combined_minimum_size()).
FocusBehaviorRecursivefocus_behavior_recursive=0🔗
- voidset_focus_behavior_recursive(value:FocusBehaviorRecursive)
voidset_focus_behavior_recursive(value:FocusBehaviorRecursive)
- FocusBehaviorRecursiveget_focus_behavior_recursive()
FocusBehaviorRecursiveget_focus_behavior_recursive()
Determines which controls can be focused together withfocus_mode. Seeget_focus_mode_with_override(). Since the default behavior isFOCUS_BEHAVIOR_INHERITED, this can be used to prevent all children controls from getting focused.
FocusModefocus_mode=0🔗
- voidset_focus_mode(value:FocusMode)
voidset_focus_mode(value:FocusMode)
- FocusModeget_focus_mode()
FocusModeget_focus_mode()
Determines which controls can be focused. Only one control can be focused at a time, and the focused control will receive keyboard, gamepad, and mouse events in_gui_input(). Useget_focus_mode_with_override()to determine if a control can grab focus, sincefocus_behavior_recursivealso affects it. See alsograb_focus().
NodePathfocus_neighbor_bottom=NodePath("")🔗
- voidset_focus_neighbor(side:Side, neighbor:NodePath)
voidset_focus_neighbor(side:Side, neighbor:NodePath)
- NodePathget_focus_neighbor(side:Side)const
NodePathget_focus_neighbor(side:Side)const
Tells Godot which node it should give focus to if the user presses the down arrow on the keyboard or down on a gamepad by default. You can change the key by editing theProjectSettings.input/ui_downinput action. The node must be aControl. If this property is not set, Godot will give focus to the closestControlto the bottom of this one.
NodePathfocus_neighbor_left=NodePath("")🔗
- voidset_focus_neighbor(side:Side, neighbor:NodePath)
voidset_focus_neighbor(side:Side, neighbor:NodePath)
- NodePathget_focus_neighbor(side:Side)const
NodePathget_focus_neighbor(side:Side)const
Tells Godot which node it should give focus to if the user presses the left arrow on the keyboard or left on a gamepad by default. You can change the key by editing theProjectSettings.input/ui_leftinput action. The node must be aControl. If this property is not set, Godot will give focus to the closestControlto the left of this one.
NodePathfocus_neighbor_right=NodePath("")🔗
- voidset_focus_neighbor(side:Side, neighbor:NodePath)
voidset_focus_neighbor(side:Side, neighbor:NodePath)
- NodePathget_focus_neighbor(side:Side)const
NodePathget_focus_neighbor(side:Side)const
Tells Godot which node it should give focus to if the user presses the right arrow on the keyboard or right on a gamepad by default. You can change the key by editing theProjectSettings.input/ui_rightinput action. The node must be aControl. If this property is not set, Godot will give focus to the closestControlto the right of this one.
NodePathfocus_neighbor_top=NodePath("")🔗
- voidset_focus_neighbor(side:Side, neighbor:NodePath)
voidset_focus_neighbor(side:Side, neighbor:NodePath)
- NodePathget_focus_neighbor(side:Side)const
NodePathget_focus_neighbor(side:Side)const
Tells Godot which node it should give focus to if the user presses the top arrow on the keyboard or top on a gamepad by default. You can change the key by editing theProjectSettings.input/ui_upinput action. The node must be aControl. If this property is not set, Godot will give focus to the closestControlto the top of this one.
NodePathfocus_next=NodePath("")🔗
- voidset_focus_next(value:NodePath)
voidset_focus_next(value:NodePath)
- NodePathget_focus_next()
NodePathget_focus_next()
Tells Godot which node it should give focus to if the user pressesTabon a keyboard by default. You can change the key by editing theProjectSettings.input/ui_focus_nextinput action.
If this property is not set, Godot will select a "best guess" based on surrounding nodes in the scene tree.
NodePathfocus_previous=NodePath("")🔗
- voidset_focus_previous(value:NodePath)
voidset_focus_previous(value:NodePath)
- NodePathget_focus_previous()
NodePathget_focus_previous()
Tells Godot which node it should give focus to if the user pressesShift+Tabon a keyboard by default. You can change the key by editing theProjectSettings.input/ui_focus_previnput action.
If this property is not set, Godot will select a "best guess" based on surrounding nodes in the scene tree.
Vector2global_position🔗
- Vector2get_global_position()
Vector2get_global_position()
The node's global position, relative to the world (usually to theCanvasLayer).
GrowDirectiongrow_horizontal=1🔗
- voidset_h_grow_direction(value:GrowDirection)
voidset_h_grow_direction(value:GrowDirection)
- GrowDirectionget_h_grow_direction()
GrowDirectionget_h_grow_direction()
Controls the direction on the horizontal axis in which the control should grow if its horizontal minimum size is changed to be greater than its current size, as the control always has to be at least the minimum size.
GrowDirectiongrow_vertical=1🔗
- voidset_v_grow_direction(value:GrowDirection)
voidset_v_grow_direction(value:GrowDirection)
- GrowDirectionget_v_grow_direction()
GrowDirectionget_v_grow_direction()
Controls the direction on the vertical axis in which the control should grow if its vertical minimum size is changed to be greater than its current size, as the control always has to be at least the minimum size.
LayoutDirectionlayout_direction=0🔗
- voidset_layout_direction(value:LayoutDirection)
voidset_layout_direction(value:LayoutDirection)
- LayoutDirectionget_layout_direction()
LayoutDirectionget_layout_direction()
Controls layout direction and text writing direction. Right-to-left layouts are necessary for certain languages (e.g. Arabic and Hebrew). See alsois_layout_rtl().
boollocalize_numeral_system=true🔗
- voidset_localize_numeral_system(value:bool)
voidset_localize_numeral_system(value:bool)
- boolis_localizing_numeral_system()
boolis_localizing_numeral_system()
Iftrue, automatically converts code line numbers, list indices,SpinBoxandProgressBarvalues from the Western Arabic (0..9) to the numeral systems used in current locale.
Note:Numbers within the text are not automatically converted, it can be done manually, usingTextServer.format_number().
MouseBehaviorRecursivemouse_behavior_recursive=0🔗
- voidset_mouse_behavior_recursive(value:MouseBehaviorRecursive)
voidset_mouse_behavior_recursive(value:MouseBehaviorRecursive)
- MouseBehaviorRecursiveget_mouse_behavior_recursive()
MouseBehaviorRecursiveget_mouse_behavior_recursive()
Determines which controls can receive mouse input together withmouse_filter. Seeget_mouse_filter_with_override(). Since the default behavior isMOUSE_BEHAVIOR_INHERITED, this can be used to prevent all children controls from receiving mouse input.
CursorShapemouse_default_cursor_shape=0🔗
- voidset_default_cursor_shape(value:CursorShape)
voidset_default_cursor_shape(value:CursorShape)
- CursorShapeget_default_cursor_shape()
CursorShapeget_default_cursor_shape()
The default cursor shape for this control. Useful for Godot plugins and applications or games that use the system's mouse cursors.
Note:On Linux, shapes may vary depending on the cursor theme of the system.
MouseFiltermouse_filter=0🔗
- voidset_mouse_filter(value:MouseFilter)
voidset_mouse_filter(value:MouseFilter)
- MouseFilterget_mouse_filter()
MouseFilterget_mouse_filter()
Determines which controls will be able to receive mouse button input events through_gui_input()and themouse_entered, andmouse_exitedsignals. Also determines how these events should be propagated. See the constants to learn what each does. Useget_mouse_filter_with_override()to determine if a control can receive mouse input, sincemouse_behavior_recursivealso affects it.
boolmouse_force_pass_scroll_events=true🔗
- voidset_force_pass_scroll_events(value:bool)
voidset_force_pass_scroll_events(value:bool)
- boolis_force_pass_scroll_events()
boolis_force_pass_scroll_events()
When enabled, scroll wheel events processed by_gui_input()will be passed to the parent control even ifmouse_filteris set toMOUSE_FILTER_STOP.
You should disable it on the root of your UI if you do not want scroll events to go to theNode._unhandled_input()processing.
Note:Because this property defaults totrue, this allows nested scrollable containers to work out of the box.
floatoffset_bottom=0.0🔗
- voidset_offset(side:Side, offset:float)
voidset_offset(side:Side, offset:float)
- floatget_offset(offset:Side)const
floatget_offset(offset:Side)const
Distance between the node's bottom edge and its parent control, based onanchor_bottom.
Offsets are often controlled by one or multiple parentContainernodes, so you should not modify them manually if your node is a direct child of aContainer. Offsets update automatically when you move or resize the node.
floatoffset_left=0.0🔗
- voidset_offset(side:Side, offset:float)
voidset_offset(side:Side, offset:float)
- floatget_offset(offset:Side)const
floatget_offset(offset:Side)const
Distance between the node's left edge and its parent control, based onanchor_left.
Offsets are often controlled by one or multiple parentContainernodes, so you should not modify them manually if your node is a direct child of aContainer. Offsets update automatically when you move or resize the node.
floatoffset_right=0.0🔗
- voidset_offset(side:Side, offset:float)
voidset_offset(side:Side, offset:float)
- floatget_offset(offset:Side)const
floatget_offset(offset:Side)const
Distance between the node's right edge and its parent control, based onanchor_right.
Offsets are often controlled by one or multiple parentContainernodes, so you should not modify them manually if your node is a direct child of aContainer. Offsets update automatically when you move or resize the node.
floatoffset_top=0.0🔗
- voidset_offset(side:Side, offset:float)
voidset_offset(side:Side, offset:float)
- floatget_offset(offset:Side)const
floatget_offset(offset:Side)const
Distance between the node's top edge and its parent control, based onanchor_top.
Offsets are often controlled by one or multiple parentContainernodes, so you should not modify them manually if your node is a direct child of aContainer. Offsets update automatically when you move or resize the node.
Vector2pivot_offset=Vector2(0,0)🔗
- voidset_pivot_offset(value:Vector2)
voidset_pivot_offset(value:Vector2)
- Vector2get_pivot_offset()
Vector2get_pivot_offset()
By default, the node's pivot is its top-left corner. When you change itsrotationorscale, it will rotate or scale around this pivot.
The actual offset is the combined value of this property andpivot_offset_ratio.
Vector2pivot_offset_ratio=Vector2(0,0)🔗
- voidset_pivot_offset_ratio(value:Vector2)
voidset_pivot_offset_ratio(value:Vector2)
- Vector2get_pivot_offset_ratio()
Vector2get_pivot_offset_ratio()
Same aspivot_offset, but expressed as uniform vector, whereVector2(0,0)is the top-left corner of this control, andVector2(1,1)is its bottom-right corner. Set this property toVector2(0.5,0.5)to pivot around this control's center.
The actual offset is the combined value of this property andpivot_offset.
Vector2position=Vector2(0,0)🔗
- Vector2get_position()
Vector2get_position()
The node's position, relative to its containing node. It corresponds to the rectangle's top-left corner. The property is not affected bypivot_offset.
floatrotation=0.0🔗
- voidset_rotation(value:float)
voidset_rotation(value:float)
- floatget_rotation()
floatget_rotation()
The node's rotation around its pivot, in radians. Seepivot_offsetto change the pivot's position.
Note:This property is edited in the inspector in degrees. If you want to use degrees in a script, userotation_degrees.
floatrotation_degrees🔗
- voidset_rotation_degrees(value:float)
voidset_rotation_degrees(value:float)
- floatget_rotation_degrees()
floatget_rotation_degrees()
Helper property to accessrotationin degrees instead of radians.
Vector2scale=Vector2(1,1)🔗
- voidset_scale(value:Vector2)
voidset_scale(value:Vector2)
- Vector2get_scale()
Vector2get_scale()
The node's scale, relative to itssize. Change this property to scale the node around itspivot_offset. The Control's tooltip will also scale according to this value.
Note:This property is mainly intended to be used for animation purposes. To support multiple resolutions in your project, use an appropriate viewport stretch mode as described in thedocumentationinstead of scaling Controls individually.
Note:FontFile.oversamplingdoesnottakeControlscaleinto account. This means that scaling up/down will cause bitmap fonts and rasterized (non-MSDF) dynamic fonts to appear blurry or pixelated. To ensure text remains crisp regardless of scale, you can enable MSDF font rendering by enablingProjectSettings.gui/theme/default_font_multichannel_signed_distance_field(applies to the default project font only), or enablingMultichannel Signed Distance Fieldin the import options of a DynamicFont for custom fonts. On system fonts,SystemFont.multichannel_signed_distance_fieldcan be enabled in the inspector.
Note:If the Control node is a child of aContainernode, the scale will be reset toVector2(1,1)when the scene is instantiated. To set the Control's scale when it's instantiated, wait for one frame usingawaitget_tree().process_framethen set itsscaleproperty.
Nodeshortcut_context🔗
- voidset_shortcut_context(value:Node)
voidset_shortcut_context(value:Node)
- Nodeget_shortcut_context()
Nodeget_shortcut_context()
TheNodewhich must be a parent of the focusedControlfor the shortcut to be activated. Ifnull, the shortcut can be activated when any control is focused (a global shortcut). This allows shortcuts to be accepted only when the user has a certain area of the GUI focused.
Vector2size=Vector2(0,0)🔗
- Vector2get_size()
Vector2get_size()
The size of the node's bounding rectangle, in the node's coordinate system.Containernodes update this property automatically.
BitField[SizeFlags]size_flags_horizontal=1🔗
- voidset_h_size_flags(value:BitField[SizeFlags])
voidset_h_size_flags(value:BitField[SizeFlags])
- BitField[SizeFlags]get_h_size_flags()
BitField[SizeFlags]get_h_size_flags()
Tells the parentContainernodes how they should resize and place the node on the X axis. Use a combination of theSizeFlagsconstants to change the flags. See the constants to learn what each does.
floatsize_flags_stretch_ratio=1.0🔗
- voidset_stretch_ratio(value:float)
voidset_stretch_ratio(value:float)
- floatget_stretch_ratio()
floatget_stretch_ratio()
If the node and at least one of its neighbors uses theSIZE_EXPANDsize flag, the parentContainerwill let it take more or less space depending on this property. If this node has a stretch ratio of 2 and its neighbor a ratio of 1, this node will take two thirds of the available space.
BitField[SizeFlags]size_flags_vertical=1🔗
- voidset_v_size_flags(value:BitField[SizeFlags])
voidset_v_size_flags(value:BitField[SizeFlags])
- BitField[SizeFlags]get_v_size_flags()
BitField[SizeFlags]get_v_size_flags()
Tells the parentContainernodes how they should resize and place the node on the Y axis. Use a combination of theSizeFlagsconstants to change the flags. See the constants to learn what each does.
Themetheme🔗
- voidset_theme(value:Theme)
voidset_theme(value:Theme)
- Themeget_theme()
Themeget_theme()
TheThemeresource this node and all itsControlandWindowchildren use. If a child node has its ownThemeresource set, theme items are merged with child's definitions having higher priority.
Note:Windowstyles will have no effect unless the window is embedded.
StringNametheme_type_variation=&""🔗
- voidset_theme_type_variation(value:StringName)
voidset_theme_type_variation(value:StringName)
- StringNameget_theme_type_variation()
StringNameget_theme_type_variation()
The name of a theme type variation used by thisControlto look up its own theme items. When empty, the class name of the node is used (e.g.Buttonfor theButtoncontrol), as well as the class names of all parent classes (in order of inheritance).
When set, this property gives the highest priority to the type of the specified name. This type can in turn extend another type, forming a dependency chain. SeeTheme.set_type_variation(). If the theme item cannot be found using this type or its base types, lookup falls back on the class names.
Note:To look upControl's own items use variousget_theme_*methods without specifyingtheme_type.
Note:Theme items are looked for in the tree order, from branch to root, where eachControlnode is checked for itsthemeproperty. The earliest match against any type/class name is returned. The project-level Theme and the default Theme are checked last.
AutoTranslateModetooltip_auto_translate_mode=0🔗
- voidset_tooltip_auto_translate_mode(value:AutoTranslateMode)
voidset_tooltip_auto_translate_mode(value:AutoTranslateMode)
- AutoTranslateModeget_tooltip_auto_translate_mode()
AutoTranslateModeget_tooltip_auto_translate_mode()
Defines if tooltip text should automatically change to its translated version depending on the current locale. Uses the same auto translate mode as this control when set toNode.AUTO_TRANSLATE_MODE_INHERIT.
Note:Tooltips customized using_make_custom_tooltip()do not use this auto translate mode automatically.
Stringtooltip_text=""🔗
- voidset_tooltip_text(value:String)
voidset_tooltip_text(value:String)
- Stringget_tooltip_text()
Stringget_tooltip_text()
The default tooltip text. The tooltip appears when the user's mouse cursor stays idle over this control for a few moments, provided that themouse_filterproperty is notMOUSE_FILTER_IGNORE. The time required for the tooltip to appear can be changed with theProjectSettings.gui/timers/tooltip_delay_secsetting.
This string is the default return value ofget_tooltip(). Override_get_tooltip()to generate tooltip text dynamically. Override_make_custom_tooltip()to customize the tooltip interface and behavior.
The tooltip popup will use either a default implementation, or a custom one that you can provide by overriding_make_custom_tooltip(). The default tooltip includes aPopupPanelandLabelwhose theme properties can be customized usingThememethods with the"TooltipPanel"and"TooltipLabel"respectively. For example:

```
var style_box = StyleBoxFlat.new()
style_box.set_bg_color(Color(1, 1, 0))
style_box.set_border_width_all(2)
# We assume here that the `theme` property has been assigned a custom Theme beforehand.
theme.set_stylebox("panel", "TooltipPanel", style_box)
theme.set_color("font_color", "TooltipLabel", Color(0, 1, 1))
```

```
var styleBox = new StyleBoxFlat();
styleBox.SetBgColor(new Color(1, 1, 0));
styleBox.SetBorderWidthAll(2);
// We assume here that the `Theme` property has been assigned a custom Theme beforehand.
Theme.SetStyleBox("panel", "TooltipPanel", styleBox);
Theme.SetColor("font_color", "TooltipLabel", new Color(0, 1, 1));
```

## Method Descriptions

String_accessibility_get_contextual_info()virtualconst🔗
Return the description of the keyboard shortcuts and other contextual help for this control.
bool_can_drop_data(at_position:Vector2, data:Variant)virtualconst🔗
Godot calls this method to test ifdatafrom a control's_get_drag_data()can be dropped atat_position.at_positionis local to this control.
This method should only be used to test the data. Process the data in_drop_data().
Note:If the drag was initiated by a keyboard shortcut oraccessibility_drag(),at_positionis set toVector2.INF, and the currently selected item/text position should be used as the drop position.

```
func _can_drop_data(position, data):
    # Check position if it is relevant to you
    # Otherwise, just check data
    return typeof(data) == TYPE_DICTIONARY and data.has("expected")
```

```
public override bool _CanDropData(Vector2 atPosition, Variant data)
{
    // Check position if it is relevant to you
    // Otherwise, just check data
    return data.VariantType == Variant.Type.Dictionary && data.AsGodotDictionary().ContainsKey("expected");
}
```

void_drop_data(at_position:Vector2, data:Variant)virtual🔗
Godot calls this method to pass you thedatafrom a control's_get_drag_data()result. Godot first calls_can_drop_data()to test ifdatais allowed to drop atat_positionwhereat_positionis local to this control.
Note:If the drag was initiated by a keyboard shortcut oraccessibility_drag(),at_positionis set toVector2.INF, and the currently selected item/text position should be used as the drop position.

```
func _can_drop_data(position, data):
    return typeof(data) == TYPE_DICTIONARY and data.has("color")

func _drop_data(position, data):
    var color = data["color"]
```

```
public override bool _CanDropData(Vector2 atPosition, Variant data)
{
    return data.VariantType == Variant.Type.Dictionary && data.AsGodotDictionary().ContainsKey("color");
}

public override void _DropData(Vector2 atPosition, Variant data)
{
    Color color = data.AsGodotDictionary()["color"].AsColor();
}
```

String_get_accessibility_container_name(node:Node)virtualconst🔗
Override this method to return a human-readable description of the position of the childnodein the custom container, added to theaccessibility_name.
Variant_get_drag_data(at_position:Vector2)virtual🔗
Godot calls this method to get data that can be dragged and dropped onto controls that expect drop data. Returnsnullif there is no data to drag. Controls that want to receive drop data should implement_can_drop_data()and_drop_data().at_positionis local to this control. Drag may be forced withforce_drag().
A preview that will follow the mouse that should represent the data can be set withset_drag_preview(). A good time to set the preview is in this method.
Note:If the drag was initiated by a keyboard shortcut oraccessibility_drag(),at_positionis set toVector2.INF, and the currently selected item/text position should be used as the drag position.

```
func _get_drag_data(position):
    var mydata = make_data() # This is your custom method generating the drag data.
    set_drag_preview(make_preview(mydata)) # This is your custom method generating the preview of the drag data.
    return mydata
```

```
public override Variant _GetDragData(Vector2 atPosition)
{
    var myData = MakeData(); // This is your custom method generating the drag data.
    SetDragPreview(MakePreview(myData)); // This is your custom method generating the preview of the drag data.
    return myData;
}
```

Vector2_get_minimum_size()virtualconst🔗
Virtual method to be implemented by the user. Returns the minimum size for this control. Alternative tocustom_minimum_sizefor controlling minimum size via code. The actual minimum size will be the max value of these two (in each axis separately).
If not overridden, defaults toVector2.ZERO.
Note:This method will not be called when the script is attached to aControlnode that already overrides its minimum size (e.g.Label,Button,PanelContaineretc.). It can only be used with most basic GUI nodes, likeControl,Container,Paneletc.
String_get_tooltip(at_position:Vector2)virtualconst🔗
Virtual method to be implemented by the user. Returns the tooltip text for the positionat_positionin control's local coordinates, which will typically appear when the cursor is resting over this control. Seeget_tooltip().
Note:If this method returns an emptyStringand_make_custom_tooltip()is not overridden, no tooltip is displayed.
void_gui_input(event:InputEvent)virtual🔗
Virtual method to be implemented by the user. Override this method to handle and accept inputs on UI elements. See alsoaccept_event().
Example:Click on the control to print a message:

```
func _gui_input(event):
    if event is InputEventMouseButton:
        if event.button_index == MOUSE_BUTTON_LEFT and event.pressed:
            print("I've been clicked D:")
```

```
public override void _GuiInput(InputEvent @event)
{
    if (@event is InputEventMouseButton mb)
    {
        if (mb.ButtonIndex == MouseButton.Left && mb.Pressed)
        {
            GD.Print("I've been clicked D:");
        }
    }
}
```

If theeventinheritsInputEventMouse, this method willnotbe called when:

- the control'smouse_filteris set toMOUSE_FILTER_IGNORE;
the control'smouse_filteris set toMOUSE_FILTER_IGNORE;
- the control is obstructed by another control on top, that doesn't havemouse_filterset toMOUSE_FILTER_IGNORE;
the control is obstructed by another control on top, that doesn't havemouse_filterset toMOUSE_FILTER_IGNORE;
- the control's parent hasmouse_filterset toMOUSE_FILTER_STOPor has accepted the event;
the control's parent hasmouse_filterset toMOUSE_FILTER_STOPor has accepted the event;
- the control's parent hasclip_contentsenabled and theevent's position is outside the parent's rectangle;
the control's parent hasclip_contentsenabled and theevent's position is outside the parent's rectangle;
- theevent's position is outside the control (see_has_point()).
theevent's position is outside the control (see_has_point()).
Note:Theevent's position is relative to this control's origin.
bool_has_point(point:Vector2)virtualconst🔗
Virtual method to be implemented by the user. Returns whether the givenpointis inside this control.
If not overridden, default behavior is checking if the point is within control's Rect.
Note:If you want to check if a point is inside the control, you can useRect2(Vector2.ZERO,size).has_point(point).
Object_make_custom_tooltip(for_text:String)virtualconst🔗
Virtual method to be implemented by the user. Returns aControlnode that should be used as a tooltip instead of the default one.for_textis the return value ofget_tooltip().
The returned node must be of typeControlor Control-derived. It can have child nodes of any type. It is freed when the tooltip disappears, so make sure you always provide a new instance (if you want to use a pre-existing node from your scene tree, you can duplicate it and pass the duplicated instance). Whennullor a non-Control node is returned, the default tooltip will be used instead.
The returned node will be added as child to aPopupPanel, so you should only provide the contents of that panel. ThatPopupPanelcan be themed usingTheme.set_stylebox()for the type"TooltipPanel"(seetooltip_textfor an example).
Note:The tooltip is shrunk to minimal size. If you want to ensure it's fully visible, you might want to set itscustom_minimum_sizeto some non-zero value.
Note:The node (and any relevant children) should have theirCanvasItem.visibleset totruewhen returned, otherwise, the viewport that instantiates it will not be able to calculate its minimum size reliably.
Note:If overridden, this method is called even ifget_tooltip()returns an empty string. When this happens with the default tooltip, it is not displayed. To copy this behavior, returnnullin this method whenfor_textis empty.
Example:Use a constructed node as a tooltip:

```
func _make_custom_tooltip(for_text):
    var label = Label.new()
    label.text = for_text
    return label
```

```
public override Control _MakeCustomTooltip(string forText)
{
    var label = new Label();
    label.Text = forText;
    return label;
}
```

Example:Use a scene instance as a tooltip:

```
func _make_custom_tooltip(for_text):
    var tooltip = preload("res://some_tooltip_scene.tscn").instantiate()
    tooltip.get_node("Label").text = for_text
    return tooltip
```

```
public override Control _MakeCustomTooltip(string forText)
{
    Node tooltip = ResourceLoader.Load<PackedScene>("res://some_tooltip_scene.tscn").Instantiate();
    tooltip.GetNode<Label>("Label").Text = forText;
    return tooltip;
}
```

Array[Vector3i]_structured_text_parser(args:Array, text:String)virtualconst🔗
User defined BiDi algorithm override function.
Returns anArrayofVector3itext ranges and text base directions, in the left-to-right order. Ranges should cover full sourcetextwithout overlaps. BiDi algorithm will be used on each range separately.
voidaccept_event()🔗
Marks an input event as handled. Once you accept an input event, it stops propagating, even to nodes listening toNode._unhandled_input()orNode._unhandled_key_input().
Note:This does not affect the methods inInput, only the way events are propagated.
voidaccessibility_drag()🔗
Starts drag-and-drop operation without using a mouse.
voidaccessibility_drop()🔗
Ends drag-and-drop operation without using a mouse.
voidadd_theme_color_override(name:StringName, color:Color)🔗
Creates a local override for a themeColorwith the specifiedname. Local overrides always take precedence when fetching theme items for the control. An override can be removed withremove_theme_color_override().
See alsoget_theme_color().
Example:Override aLabel's color and reset it later:

```
# Given the child Label node "MyLabel", override its font color with a custom value.
$MyLabel.add_theme_color_override("font_color", Color(1, 0.5, 0))
# Reset the font color of the child label.
$MyLabel.remove_theme_color_override("font_color")
# Alternatively it can be overridden with the default value from the Label type.
$MyLabel.add_theme_color_override("font_color", get_theme_color("font_color", "Label"))
```

```
// Given the child Label node "MyLabel", override its font color with a custom value.
GetNode<Label>("MyLabel").AddThemeColorOverride("font_color", new Color(1, 0.5f, 0));
// Reset the font color of the child label.
GetNode<Label>("MyLabel").RemoveThemeColorOverride("font_color");
// Alternatively it can be overridden with the default value from the Label type.
GetNode<Label>("MyLabel").AddThemeColorOverride("font_color", GetThemeColor("font_color", "Label"));
```

voidadd_theme_constant_override(name:StringName, constant:int)🔗
Creates a local override for a theme constant with the specifiedname. Local overrides always take precedence when fetching theme items for the control. An override can be removed withremove_theme_constant_override().
See alsoget_theme_constant().
voidadd_theme_font_override(name:StringName, font:Font)🔗
Creates a local override for a themeFontwith the specifiedname. Local overrides always take precedence when fetching theme items for the control. An override can be removed withremove_theme_font_override().
See alsoget_theme_font().
voidadd_theme_font_size_override(name:StringName, font_size:int)🔗
Creates a local override for a theme font size with the specifiedname. Local overrides always take precedence when fetching theme items for the control. An override can be removed withremove_theme_font_size_override().
See alsoget_theme_font_size().
voidadd_theme_icon_override(name:StringName, texture:Texture2D)🔗
Creates a local override for a theme icon with the specifiedname. Local overrides always take precedence when fetching theme items for the control. An override can be removed withremove_theme_icon_override().
See alsoget_theme_icon().
voidadd_theme_stylebox_override(name:StringName, stylebox:StyleBox)🔗
Creates a local override for a themeStyleBoxwith the specifiedname. Local overrides always take precedence when fetching theme items for the control. An override can be removed withremove_theme_stylebox_override().
See alsoget_theme_stylebox().
Example:Modify a property in aStyleBoxby duplicating it:

```
# The snippet below assumes the child node "MyButton" has a StyleBoxFlat assigned.
# Resources are shared across instances, so we need to duplicate it
# to avoid modifying the appearance of all other buttons.
var new_stylebox_normal = $MyButton.get_theme_stylebox("normal").duplicate()
new_stylebox_normal.border_width_top = 3
new_stylebox_normal.border_color = Color(0, 1, 0.5)
$MyButton.add_theme_stylebox_override("normal", new_stylebox_normal)
# Remove the stylebox override.
$MyButton.remove_theme_stylebox_override("normal")
```

```
// The snippet below assumes the child node "MyButton" has a StyleBoxFlat assigned.
// Resources are shared across instances, so we need to duplicate it
// to avoid modifying the appearance of all other buttons.
StyleBoxFlat newStyleboxNormal = GetNode<Button>("MyButton").GetThemeStylebox("normal").Duplicate() as StyleBoxFlat;
newStyleboxNormal.BorderWidthTop = 3;
newStyleboxNormal.BorderColor = new Color(0, 1, 0.5f);
GetNode<Button>("MyButton").AddThemeStyleboxOverride("normal", newStyleboxNormal);
// Remove the stylebox override.
GetNode<Button>("MyButton").RemoveThemeStyleboxOverride("normal");
```

voidbegin_bulk_theme_override()🔗
Prevents*_theme_*_overridemethods from emittingNOTIFICATION_THEME_CHANGEDuntilend_bulk_theme_override()is called.
voidend_bulk_theme_override()🔗
Ends a bulk theme override update. Seebegin_bulk_theme_override().
Controlfind_next_valid_focus()const🔗
Finds the next (below in the tree)Controlthat can receive the focus.
Controlfind_prev_valid_focus()const🔗
Finds the previous (above in the tree)Controlthat can receive the focus.
Controlfind_valid_focus_neighbor(side:Side)const🔗
Finds the nextControlthat can receive the focus on the specifiedSide.
Note:This is different fromget_focus_neighbor(), which returns the path of a specified focus neighbor.
voidforce_drag(data:Variant, preview:Control)🔗
Forces drag and bypasses_get_drag_data()andset_drag_preview()by passingdataandpreview. Drag will start even if the mouse is neither over nor pressed on this control.
The methods_can_drop_data()and_drop_data()must be implemented on controls that want to receive drop data.
floatget_anchor(side:Side)const🔗
Returns the anchor for the specifiedSide. A getter method foranchor_bottom,anchor_left,anchor_rightandanchor_top.
Vector2get_begin()const🔗
Returnsoffset_leftandoffset_top. See alsoposition.
Vector2get_combined_minimum_size()const🔗
Returns combined minimum size fromcustom_minimum_sizeandget_minimum_size().
Vector2get_combined_pivot_offset()const🔗
Returns the combined value ofpivot_offsetandpivot_offset_ratio, in pixels. The ratio is multiplied by the control's size.
CursorShapeget_cursor_shape(position:Vector2= Vector2(0, 0))const🔗
Returns the mouse cursor shape for this control when hovered overpositionin local coordinates. For most controls, this is the same asmouse_default_cursor_shape, but some built-in controls implement more complex logic.
Vector2get_end()const🔗
Returnsoffset_rightandoffset_bottom.
FocusModeget_focus_mode_with_override()const🔗
Returns thefocus_mode, but takes thefocus_behavior_recursiveinto account. Iffocus_behavior_recursiveis set toFOCUS_BEHAVIOR_DISABLED, or it is set toFOCUS_BEHAVIOR_INHERITEDand its ancestor is set toFOCUS_BEHAVIOR_DISABLED, then this returnsFOCUS_NONE.
NodePathget_focus_neighbor(side:Side)const🔗
Returns the focus neighbor for the specifiedSide. A getter method forfocus_neighbor_bottom,focus_neighbor_left,focus_neighbor_rightandfocus_neighbor_top.
Note:To find the nextControlon the specificSide, even if a neighbor is not assigned, usefind_valid_focus_neighbor().
Rect2get_global_rect()const🔗
Returns the position and size of the control relative to the containing canvas. Seeglobal_positionandsize.
Note:If the node itself or any parentCanvasItembetween the node and the canvas have a non default rotation or skew, the resulting size is likely not meaningful.
Note:SettingViewport.gui_snap_controls_to_pixelstotruecan lead to rounding inaccuracies between the displayed control and the returnedRect2.
Vector2get_minimum_size()const🔗
Returns the minimum size for this control. Seecustom_minimum_size.
MouseFilterget_mouse_filter_with_override()const🔗
Returns themouse_filter, but takes themouse_behavior_recursiveinto account. Ifmouse_behavior_recursiveis set toMOUSE_BEHAVIOR_DISABLED, or it is set toMOUSE_BEHAVIOR_INHERITEDand its ancestor is set toMOUSE_BEHAVIOR_DISABLED, then this returnsMOUSE_FILTER_IGNORE.
floatget_offset(offset:Side)const🔗
Returns the offset for the specifiedSide. A getter method foroffset_bottom,offset_left,offset_rightandoffset_top.
Vector2get_parent_area_size()const🔗
Returns the width/height occupied in the parent control.
Controlget_parent_control()const🔗
Returns the parent control node.
Rect2get_rect()const🔗
Returns the position and size of the control in the coordinate system of the containing node. Seeposition,scaleandsize.
Note:Ifrotationis not the default rotation, the resulting size is not meaningful.
Note:SettingViewport.gui_snap_controls_to_pixelstotruecan lead to rounding inaccuracies between the displayed control and the returnedRect2.
Vector2get_screen_position()const🔗
Returns the position of thisControlin global screen coordinates (i.e. taking window position into account). Mostly useful for editor plugins.
Equivalent toget_screen_transform().origin(seeCanvasItem.get_screen_transform()).
Example:Show a popup at the mouse position:

```
popup_menu.position = get_screen_position() + get_screen_transform().basis_xform(get_local_mouse_position())

# The above code is equivalent to:
popup_menu.position = get_screen_transform() * get_local_mouse_position()

popup_menu.reset_size()
popup_menu.popup()
```

Colorget_theme_color(name:StringName, theme_type:StringName= &"")const🔗
Returns aColorfrom the first matchingThemein the tree if thatThemehas a color item with the specifiednameandtheme_type. Iftheme_typeis omitted the class name of the current control is used as the type, ortheme_type_variationif it is defined. If the type is a class name its parent classes are also checked, in order of inheritance. If the type is a variation its base types are checked, in order of dependency, then the control's class name and its parent classes are checked.
For the current control its local overrides are considered first (seeadd_theme_color_override()), then its assignedtheme. After the current control, each parent control and its assignedthemeare considered; controls without athemeassigned are skipped. If no matchingThemeis found in the tree, the custom projectTheme(seeProjectSettings.gui/theme/custom) and the defaultThemeare used (seeThemeDB).

```
func _ready():
    # Get the font color defined for the current Control's class, if it exists.
    modulate = get_theme_color("font_color")
    # Get the font color defined for the Button class.
    modulate = get_theme_color("font_color", "Button")
```

```
public override void _Ready()
{
    // Get the font color defined for the current Control's class, if it exists.
    Modulate = GetThemeColor("font_color");
    // Get the font color defined for the Button class.
    Modulate = GetThemeColor("font_color", "Button");
}
```

intget_theme_constant(name:StringName, theme_type:StringName= &"")const🔗
Returns a constant from the first matchingThemein the tree if thatThemehas a constant item with the specifiednameandtheme_type.
Seeget_theme_color()for details.
floatget_theme_default_base_scale()const🔗
Returns the default base scale value from the first matchingThemein the tree if thatThemehas a validTheme.default_base_scalevalue.
Seeget_theme_color()for details.
Fontget_theme_default_font()const🔗
Returns the default font from the first matchingThemein the tree if thatThemehas a validTheme.default_fontvalue.
Seeget_theme_color()for details.
intget_theme_default_font_size()const🔗
Returns the default font size value from the first matchingThemein the tree if thatThemehas a validTheme.default_font_sizevalue.
Seeget_theme_color()for details.
Fontget_theme_font(name:StringName, theme_type:StringName= &"")const🔗
Returns aFontfrom the first matchingThemein the tree if thatThemehas a font item with the specifiednameandtheme_type.
Seeget_theme_color()for details.
intget_theme_font_size(name:StringName, theme_type:StringName= &"")const🔗
Returns a font size from the first matchingThemein the tree if thatThemehas a font size item with the specifiednameandtheme_type.
Seeget_theme_color()for details.
Texture2Dget_theme_icon(name:StringName, theme_type:StringName= &"")const🔗
Returns an icon from the first matchingThemein the tree if thatThemehas an icon item with the specifiednameandtheme_type.
Seeget_theme_color()for details.
StyleBoxget_theme_stylebox(name:StringName, theme_type:StringName= &"")const🔗
Returns aStyleBoxfrom the first matchingThemein the tree if thatThemehas a stylebox item with the specifiednameandtheme_type.
Seeget_theme_color()for details.
Stringget_tooltip(at_position:Vector2= Vector2(0, 0))const🔗
Returns the tooltip text for the positionat_positionin control's local coordinates, which will typically appear when the cursor is resting over this control. By default, it returnstooltip_text.
This method can be overridden to customize its behavior. See_get_tooltip().
Note:If this method returns an emptyStringand_make_custom_tooltip()is not overridden, no tooltip is displayed.
voidgrab_click_focus()🔗
Creates anInputEventMouseButtonthat attempts to click the control. If the event is received, the control gains focus.

```
func _process(delta):
    grab_click_focus() # When clicking another Control node, this node will be clicked instead.
```

```
public override void _Process(double delta)
{
    GrabClickFocus(); // When clicking another Control node, this node will be clicked instead.
}
```

voidgrab_focus(hide_focus:bool= false)🔗
Steal the focus from another control and become the focused control (seefocus_mode).
Ifhide_focusistrue, the control will not visually show its focused state. Has no effect forLineEditandTextEditwhenProjectSettings.gui/common/show_focus_state_on_pointer_eventis set toControlSupportsKeyboardInput, or for any control when it is set toAlways.
Note:Using this method together withCallable.call_deferred()makes it more reliable, especially when called insideNode._ready().
boolhas_focus(ignore_hidden_focus:bool= false)const🔗
Returnstrueif this is the current focused control. Seefocus_mode.
Ifignore_hidden_focusistrue, controls that have their focus hidden will always returnfalse. Hidden focus happens automatically when controls gain focus via mouse input, or manually usinggrab_focus()withhide_focusset totrue.
boolhas_theme_color(name:StringName, theme_type:StringName= &"")const🔗
Returnstrueif there is a matchingThemein the tree that has a color item with the specifiednameandtheme_type.
Seeget_theme_color()for details.
boolhas_theme_color_override(name:StringName)const🔗
Returnstrueif there is a local override for a themeColorwith the specifiednamein thisControlnode.
Seeadd_theme_color_override().
boolhas_theme_constant(name:StringName, theme_type:StringName= &"")const🔗
Returnstrueif there is a matchingThemein the tree that has a constant item with the specifiednameandtheme_type.
Seeget_theme_color()for details.
boolhas_theme_constant_override(name:StringName)const🔗
Returnstrueif there is a local override for a theme constant with the specifiednamein thisControlnode.
Seeadd_theme_constant_override().
boolhas_theme_font(name:StringName, theme_type:StringName= &"")const🔗
Returnstrueif there is a matchingThemein the tree that has a font item with the specifiednameandtheme_type.
Seeget_theme_color()for details.
boolhas_theme_font_override(name:StringName)const🔗
Returnstrueif there is a local override for a themeFontwith the specifiednamein thisControlnode.
Seeadd_theme_font_override().
boolhas_theme_font_size(name:StringName, theme_type:StringName= &"")const🔗
Returnstrueif there is a matchingThemein the tree that has a font size item with the specifiednameandtheme_type.
Seeget_theme_color()for details.
boolhas_theme_font_size_override(name:StringName)const🔗
Returnstrueif there is a local override for a theme font size with the specifiednamein thisControlnode.
Seeadd_theme_font_size_override().
boolhas_theme_icon(name:StringName, theme_type:StringName= &"")const🔗
Returnstrueif there is a matchingThemein the tree that has an icon item with the specifiednameandtheme_type.
Seeget_theme_color()for details.
boolhas_theme_icon_override(name:StringName)const🔗
Returnstrueif there is a local override for a theme icon with the specifiednamein thisControlnode.
Seeadd_theme_icon_override().
boolhas_theme_stylebox(name:StringName, theme_type:StringName= &"")const🔗
Returnstrueif there is a matchingThemein the tree that has a stylebox item with the specifiednameandtheme_type.
Seeget_theme_color()for details.
boolhas_theme_stylebox_override(name:StringName)const🔗
Returnstrueif there is a local override for a themeStyleBoxwith the specifiednamein thisControlnode.
Seeadd_theme_stylebox_override().
boolis_drag_successful()const🔗
Returnstrueif a drag operation is successful. Alternative toViewport.gui_is_drag_successful().
Best used withNode.NOTIFICATION_DRAG_END.
boolis_layout_rtl()const🔗
Returnstrueif the layout is right-to-left. See alsolayout_direction.
voidrelease_focus()🔗
Give up the focus. No other control will be able to receive input.
voidremove_theme_color_override(name:StringName)🔗
Removes a local override for a themeColorwith the specifiednamepreviously added byadd_theme_color_override()or via the Inspector dock.
voidremove_theme_constant_override(name:StringName)🔗
Removes a local override for a theme constant with the specifiednamepreviously added byadd_theme_constant_override()or via the Inspector dock.
voidremove_theme_font_override(name:StringName)🔗
Removes a local override for a themeFontwith the specifiednamepreviously added byadd_theme_font_override()or via the Inspector dock.
voidremove_theme_font_size_override(name:StringName)🔗
Removes a local override for a theme font size with the specifiednamepreviously added byadd_theme_font_size_override()or via the Inspector dock.
voidremove_theme_icon_override(name:StringName)🔗
Removes a local override for a theme icon with the specifiednamepreviously added byadd_theme_icon_override()or via the Inspector dock.
voidremove_theme_stylebox_override(name:StringName)🔗
Removes a local override for a themeStyleBoxwith the specifiednamepreviously added byadd_theme_stylebox_override()or via the Inspector dock.
voidreset_size()🔗
Resets the size toget_combined_minimum_size(). This is equivalent to callingset_size(Vector2())(or any size below the minimum).
voidset_anchor(side:Side, anchor:float, keep_offset:bool= false, push_opposite_anchor:bool= true)🔗
Sets the anchor for the specifiedSidetoanchor. A setter method foranchor_bottom,anchor_left,anchor_rightandanchor_top.
Ifkeep_offsetistrue, offsets aren't updated after this operation.
Ifpush_opposite_anchoristrueand the opposite anchor overlaps this anchor, the opposite one will have its value overridden. For example, when setting left anchor to 1 and the right anchor has value of 0.5, the right anchor will also get value of 1. Ifpush_opposite_anchorwasfalse, the left anchor would get value 0.5.
voidset_anchor_and_offset(side:Side, anchor:float, offset:float, push_opposite_anchor:bool= false)🔗
Works the same asset_anchor(), but instead ofkeep_offsetargument and automatic update of offset, it allows to set the offset yourself (seeset_offset()).
voidset_anchors_and_offsets_preset(preset:LayoutPreset, resize_mode:LayoutPresetMode= 0, margin:int= 0)🔗
Sets both anchor preset and offset preset. Seeset_anchors_preset()andset_offsets_preset().
voidset_anchors_preset(preset:LayoutPreset, keep_offsets:bool= false)🔗
Sets the anchors to apresetfromLayoutPresetenum. This is the code equivalent to using the Layout menu in the 2D editor.
Ifkeep_offsetsistrue, control's position will also be updated.
voidset_begin(position:Vector2)🔗
Setsoffset_leftandoffset_topat the same time. Equivalent of changingposition.
voidset_drag_forwarding(drag_func:Callable, can_drop_func:Callable, drop_func:Callable)🔗
Sets the given callables to be used instead of the control's own drag-and-drop virtual methods. If a callable is empty, its respective virtual method is used as normal.
The arguments for each callable should be exactly the same as their respective virtual methods, which would be:

- drag_funccorresponds to_get_drag_data()and requires aVector2;
drag_funccorresponds to_get_drag_data()and requires aVector2;
- can_drop_funccorresponds to_can_drop_data()and requires both aVector2and aVariant;
can_drop_funccorresponds to_can_drop_data()and requires both aVector2and aVariant;
- drop_funccorresponds to_drop_data()and requires both aVector2and aVariant.
drop_funccorresponds to_drop_data()and requires both aVector2and aVariant.
voidset_drag_preview(control:Control)🔗
Shows the given control at the mouse pointer. A good time to call this method is in_get_drag_data(). The control must not be in the scene tree. You should not free the control, and you should not keep a reference to the control beyond the duration of the drag. It will be deleted automatically after the drag has ended.

```
@export var color = Color(1, 0, 0, 1)

func _get_drag_data(position):
    # Use a control that is not in the tree
    var cpb = ColorPickerButton.new()
    cpb.color = color
    cpb.size = Vector2(50, 50)
    set_drag_preview(cpb)
    return color
```

```
[Export]
private Color _color = new Color(1, 0, 0, 1);

public override Variant _GetDragData(Vector2 atPosition)
{
    // Use a control that is not in the tree
    var cpb = new ColorPickerButton();
    cpb.Color = _color;
    cpb.Size = new Vector2(50, 50);
    SetDragPreview(cpb);
    return _color;
}
```

voidset_end(position:Vector2)🔗
Setsoffset_rightandoffset_bottomat the same time.
voidset_focus_neighbor(side:Side, neighbor:NodePath)🔗
Sets the focus neighbor for the specifiedSideto theControlatneighbornode path. A setter method forfocus_neighbor_bottom,focus_neighbor_left,focus_neighbor_rightandfocus_neighbor_top.
voidset_global_position(position:Vector2, keep_offsets:bool= false)🔗
Sets theglobal_positionto givenposition.
Ifkeep_offsetsistrue, control's anchors will be updated instead of offsets.
voidset_offset(side:Side, offset:float)🔗
Sets the offset for the specifiedSidetooffset. A setter method foroffset_bottom,offset_left,offset_rightandoffset_top.
voidset_offsets_preset(preset:LayoutPreset, resize_mode:LayoutPresetMode= 0, margin:int= 0)🔗
Sets the offsets to apresetfromLayoutPresetenum. This is the code equivalent to using the Layout menu in the 2D editor.
Use parameterresize_modewith constants fromLayoutPresetModeto better determine the resulting size of theControl. Constant size will be ignored if used with presets that change size, e.g.PRESET_LEFT_WIDE.
Use parametermarginto determine the gap between theControland the edges.
voidset_position(position:Vector2, keep_offsets:bool= false)🔗
Sets thepositionto givenposition.
Ifkeep_offsetsistrue, control's anchors will be updated instead of offsets.
voidset_size(size:Vector2, keep_offsets:bool= false)🔗
Sets the size (seesize).
Ifkeep_offsetsistrue, control's anchors will be updated instead of offsets.
voidupdate_minimum_size()🔗
Invalidates the size cache in this node and in parent nodes up to top level. Intended to be used withget_minimum_size()when the return value is changed. Settingcustom_minimum_sizedirectly calls this method automatically.
voidwarp_mouse(position:Vector2)🔗
Moves the mouse cursor toposition, relative topositionof thisControl.
Note:warp_mouse()is only supported on Windows, macOS and Linux. It has no effect on Android, iOS and Web.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
