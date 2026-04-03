# Window in English

# Window
Inherits:Viewport<Node<Object
Inherited By:AcceptDialog,Popup
Base class for all windows, dialogs, and popups.

## Description
A node that creates a window. The window can either be a native system window or embedded inside anotherWindow(seeViewport.gui_embed_subwindows).
At runtime,Windows will not close automatically when requested. You need to handle it manually using theclose_requestedsignal (this applies both to pressing the close button and clicking outside of a popup).

## Properties

| String | accessibility_description | "" |
|---|---|---|
| String | accessibility_name | "" |
| bool | always_on_top | false |
| bool | auto_translate |  |
| bool | borderless | false |
| ContentScaleAspect | content_scale_aspect | 0 |
| float | content_scale_factor | 1.0 |
| ContentScaleMode | content_scale_mode | 0 |
| Vector2i | content_scale_size | Vector2i(0,0) |
| ContentScaleStretch | content_scale_stretch | 0 |
| int | current_screen |  |
| bool | exclude_from_capture | false |
| bool | exclusive | false |
| bool | extend_to_title | false |
| bool | force_native | false |
| WindowInitialPosition | initial_position | 0 |
| bool | keep_title_visible | false |
| Vector2i | max_size | Vector2i(0,0) |
| bool | maximize_disabled | false |
| Vector2i | min_size | Vector2i(0,0) |
| bool | minimize_disabled | false |
| Mode | mode | 0 |
| bool | mouse_passthrough | false |
| PackedVector2Array | mouse_passthrough_polygon | PackedVector2Array() |
| Rect2i | nonclient_area | Rect2i(0,0,0,0) |
| bool | popup_window | false |
| bool | popup_wm_hint | false |
| Vector2i | position | Vector2i(0,0) |
| bool | sharp_corners | false |
| Vector2i | size | Vector2i(100,100) |
| Theme | theme |  |
| StringName | theme_type_variation | &"" |
| String | title | "" |
| bool | transient | false |
| bool | transient_to_focused | false |
| bool | transparent | false |
| bool | unfocusable | false |
| bool | unresizable | false |
| bool | visible | true |
| bool | wrap_controls | false |

String
accessibility_description
String
accessibility_name
bool
always_on_top
false
bool
auto_translate
bool
borderless
false
ContentScaleAspect
content_scale_aspect
float
content_scale_factor
ContentScaleMode
content_scale_mode
Vector2i
content_scale_size
Vector2i(0,0)
ContentScaleStretch
content_scale_stretch
current_screen
bool
exclude_from_capture
false
bool
exclusive
false
bool
extend_to_title
false
bool
force_native
false
WindowInitialPosition
initial_position
bool
keep_title_visible
false
Vector2i
max_size
Vector2i(0,0)
bool
maximize_disabled
false
Vector2i
min_size
Vector2i(0,0)
bool
minimize_disabled
false
Mode
mode
bool
mouse_passthrough
false
PackedVector2Array
mouse_passthrough_polygon
PackedVector2Array()
Rect2i
nonclient_area
Rect2i(0,0,0,0)
bool
popup_window
false
bool
popup_wm_hint
false
Vector2i
position
Vector2i(0,0)
bool
sharp_corners
false
Vector2i
size
Vector2i(100,100)
Theme
theme
StringName
theme_type_variation
String
title
bool
transient
false
bool
transient_to_focused
false
bool
transparent
false
bool
unfocusable
false
bool
unresizable
false
bool
visible
true
bool
wrap_controls
false

## Methods

| Vector2 | _get_contents_minimum_size()virtualconst |
|---|---|
| void | add_theme_color_override(name:StringName, color:Color) |
| void | add_theme_constant_override(name:StringName, constant:int) |
| void | add_theme_font_override(name:StringName, font:Font) |
| void | add_theme_font_size_override(name:StringName, font_size:int) |
| void | add_theme_icon_override(name:StringName, texture:Texture2D) |
| void | add_theme_stylebox_override(name:StringName, stylebox:StyleBox) |
| void | begin_bulk_theme_override() |
| bool | can_draw()const |
| void | child_controls_changed() |
| void | end_bulk_theme_override() |
| Vector2 | get_contents_minimum_size()const |
| bool | get_flag(flag:Flags)const |
| Window | get_focused_window()static |
| LayoutDirection | get_layout_direction()const |
| Vector2i | get_position_with_decorations()const |
| Vector2i | get_size_with_decorations()const |
| Color | get_theme_color(name:StringName, theme_type:StringName= &"")const |
| int | get_theme_constant(name:StringName, theme_type:StringName= &"")const |
| float | get_theme_default_base_scale()const |
| Font | get_theme_default_font()const |
| int | get_theme_default_font_size()const |
| Font | get_theme_font(name:StringName, theme_type:StringName= &"")const |
| int | get_theme_font_size(name:StringName, theme_type:StringName= &"")const |
| Texture2D | get_theme_icon(name:StringName, theme_type:StringName= &"")const |
| StyleBox | get_theme_stylebox(name:StringName, theme_type:StringName= &"")const |
| int | get_window_id()const |
| void | grab_focus() |
| bool | has_focus()const |
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
| void | hide() |
| bool | is_embedded()const |
| bool | is_layout_rtl()const |
| bool | is_maximize_allowed()const |
| bool | is_using_font_oversampling()const |
| void | move_to_center() |
| void | move_to_foreground() |
| void | popup(rect:Rect2i= Rect2i(0, 0, 0, 0)) |
| void | popup_centered(minsize:Vector2i= Vector2i(0, 0)) |
| void | popup_centered_clamped(minsize:Vector2i= Vector2i(0, 0), fallback_ratio:float= 0.75) |
| void | popup_centered_ratio(ratio:float= 0.8) |
| void | popup_exclusive(from_node:Node, rect:Rect2i= Rect2i(0, 0, 0, 0)) |
| void | popup_exclusive_centered(from_node:Node, minsize:Vector2i= Vector2i(0, 0)) |
| void | popup_exclusive_centered_clamped(from_node:Node, minsize:Vector2i= Vector2i(0, 0), fallback_ratio:float= 0.75) |
| void | popup_exclusive_centered_ratio(from_node:Node, ratio:float= 0.8) |
| void | popup_exclusive_on_parent(from_node:Node, parent_rect:Rect2i) |
| void | popup_on_parent(parent_rect:Rect2i) |
| void | remove_theme_color_override(name:StringName) |
| void | remove_theme_constant_override(name:StringName) |
| void | remove_theme_font_override(name:StringName) |
| void | remove_theme_font_size_override(name:StringName) |
| void | remove_theme_icon_override(name:StringName) |
| void | remove_theme_stylebox_override(name:StringName) |
| void | request_attention() |
| void | reset_size() |
| void | set_flag(flag:Flags, enabled:bool) |
| void | set_ime_active(active:bool) |
| void | set_ime_position(position:Vector2i) |
| void | set_layout_direction(direction:LayoutDirection) |
| void | set_unparent_when_invisible(unparent:bool) |
| void | set_use_font_oversampling(enable:bool) |
| void | show() |
| void | start_drag() |
| void | start_resize(edge:WindowResizeEdge) |

Vector2
_get_contents_minimum_size()virtualconst
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
bool
can_draw()const
void
child_controls_changed()
void
end_bulk_theme_override()
Vector2
get_contents_minimum_size()const
bool
get_flag(flag:Flags)const
Window
get_focused_window()static
LayoutDirection
get_layout_direction()const
Vector2i
get_position_with_decorations()const
Vector2i
get_size_with_decorations()const
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
get_window_id()const
void
grab_focus()
bool
has_focus()const
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
void
hide()
bool
is_embedded()const
bool
is_layout_rtl()const
bool
is_maximize_allowed()const
bool
is_using_font_oversampling()const
void
move_to_center()
void
move_to_foreground()
void
popup(rect:Rect2i= Rect2i(0, 0, 0, 0))
void
popup_centered(minsize:Vector2i= Vector2i(0, 0))
void
popup_centered_clamped(minsize:Vector2i= Vector2i(0, 0), fallback_ratio:float= 0.75)
void
popup_centered_ratio(ratio:float= 0.8)
void
popup_exclusive(from_node:Node, rect:Rect2i= Rect2i(0, 0, 0, 0))
void
popup_exclusive_centered(from_node:Node, minsize:Vector2i= Vector2i(0, 0))
void
popup_exclusive_centered_clamped(from_node:Node, minsize:Vector2i= Vector2i(0, 0), fallback_ratio:float= 0.75)
void
popup_exclusive_centered_ratio(from_node:Node, ratio:float= 0.8)
void
popup_exclusive_on_parent(from_node:Node, parent_rect:Rect2i)
void
popup_on_parent(parent_rect:Rect2i)
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
request_attention()
void
reset_size()
void
set_flag(flag:Flags, enabled:bool)
void
set_ime_active(active:bool)
void
set_ime_position(position:Vector2i)
void
set_layout_direction(direction:LayoutDirection)
void
set_unparent_when_invisible(unparent:bool)
void
set_use_font_oversampling(enable:bool)
void
show()
void
start_drag()
void
start_resize(edge:WindowResizeEdge)

## Theme Properties

| Color | title_color | Color(0.875,0.875,0.875,1) |
|---|---|---|
| Color | title_outline_modulate | Color(0,0,0,1) |
| int | close_h_offset | 18 |
| int | close_v_offset | 24 |
| int | resize_margin | 4 |
| int | title_height | 36 |
| int | title_outline_size | 0 |
| Font | title_font |  |
| int | title_font_size |  |
| Texture2D | close |  |
| Texture2D | close_pressed |  |
| StyleBox | embedded_border |  |
| StyleBox | embedded_unfocused_border |  |

Color
title_color
Color(0.875,0.875,0.875,1)
Color
title_outline_modulate
Color(0,0,0,1)
close_h_offset
close_v_offset
resize_margin
title_height
title_outline_size
Font
title_font
title_font_size
Texture2D
close
Texture2D
close_pressed
StyleBox
embedded_border
StyleBox
embedded_unfocused_border

## Signals
about_to_popup()🔗
Emitted right afterpopup()call, before theWindowappears or does anything.
close_requested()🔗
Emitted when theWindow's close button is pressed or whenpopup_windowis enabled and user clicks outside the window.
This signal can be used to handle window closing, e.g. by connecting it tohide().
dpi_changed()🔗
Emitted when theWindow's DPI changes as a result of OS-level changes (e.g. moving the window from a Retina display to a lower resolution one).
Note:Only implemented on macOS and Linux (Wayland).
files_dropped(files:PackedStringArray)🔗
Emitted when files are dragged from the OS file manager and dropped in the game window. The argument is a list of file paths.
```
func _ready():
    get_window().files_dropped.connect(on_files_dropped)

func on_files_dropped(files):
    print(files)
```
Note:This signal only works with native windows, i.e. the main window andWindow-derived nodes whenViewport.gui_embed_subwindowsis disabled in the main viewport.
focus_entered()🔗
Emitted when theWindowgains focus.
focus_exited()🔗
Emitted when theWindowloses its focus.
go_back_requested()🔗
Emitted when a go back request is sent (e.g. pressing the "Back" button on Android), right afterNode.NOTIFICATION_WM_GO_BACK_REQUEST.
mouse_entered()🔗
Emitted when the mouse cursor enters theWindow's visible area, that is not occluded behind otherControls or windows, provided itsViewport.gui_disable_inputisfalseand regardless if it's currently focused or not.
mouse_exited()🔗
Emitted when the mouse cursor leaves theWindow's visible area, that is not occluded behind otherControls or windows, provided itsViewport.gui_disable_inputisfalseand regardless if it's currently focused or not.
nonclient_window_input(event:InputEvent)🔗
Emitted when the mouse event is received by the custom decoration area defined bynonclient_area, and normal input to the window is blocked (such as when it has an exclusive child opened).event's position is in the embedder's coordinate system.
theme_changed()🔗
Emitted when theNOTIFICATION_THEME_CHANGEDnotification is sent.
title_changed()🔗
Emitted when window title bar text is changed.
titlebar_changed()🔗
Emitted when window title bar decorations are changed, e.g. macOS window enter/exit full screen mode, or extend-to-title flag is changed.
visibility_changed()🔗
Emitted whenWindowis made visible or disappears.
window_input(event:InputEvent)🔗
Emitted when theWindowis currently focused and receives any input, passing the received event as an argument. The event's position, if present, is in the embedder's coordinate system.

## Enumerations
enumMode:🔗
ModeMODE_WINDOWED=0
Windowed mode, i.e.Windowdoesn't occupy the whole screen (unless set to the size of the screen).
ModeMODE_MINIMIZED=1
Minimized window mode, i.e.Windowis not visible and available on window manager's window list. Normally happens when the minimize button is pressed.
ModeMODE_MAXIMIZED=2
Maximized window mode, i.e.Windowwill occupy whole screen area except task bar and still display its borders. Normally happens when the maximize button is pressed.
ModeMODE_FULLSCREEN=3
Full screen mode with full multi-window support.
Full screen window covers the entire display area of a screen and has no decorations. The display's video mode is not changed.
On Android:This enables immersive mode.
On macOS:A new desktop is used to display the running project.
Note:Regardless of the platform, enabling full screen will change the window size to match the monitor's size. Therefore, make sure your project supportsmultiple resolutionswhen enabling full screen mode.
ModeMODE_EXCLUSIVE_FULLSCREEN=4
A single window full screen mode. This mode has less overhead, but only one window can be open on a given screen at a time (opening a child window or application switching will trigger a full screen transition).
Full screen window covers the entire display area of a screen and has no border or decorations. The display's video mode is not changed.
Note:This mode might not work with screen recording software.
On Android:This enables immersive mode.
On Windows:Depending on video driver, full screen transition might cause screens to go black for a moment.
On macOS:A new desktop is used to display the running project. Exclusive full screen mode prevents Dock and Menu from showing up when the mouse pointer is hovering the edge of the screen.
On Linux (X11):Exclusive full screen mode bypasses compositor.
On Linux (Wayland):Equivalent toMODE_FULLSCREEN.
Note:Regardless of the platform, enabling full screen will change the window size to match the monitor's size. Therefore, make sure your project supportsmultiple resolutionswhen enabling full screen mode.
enumFlags:🔗
FlagsFLAG_RESIZE_DISABLED=0
The window can't be resized by dragging its resize grip. It's still possible to resize the window usingsize. This flag is ignored for full screen windows. Set withunresizable.
FlagsFLAG_BORDERLESS=1
The window do not have native title bar and other decorations. This flag is ignored for full-screen windows. Set withborderless.
FlagsFLAG_ALWAYS_ON_TOP=2
The window is floating on top of all other windows. This flag is ignored for full-screen windows. Set withalways_on_top.
FlagsFLAG_TRANSPARENT=3
The window background can be transparent. Set withtransparent.
Note:This flag has no effect if eitherProjectSettings.display/window/per_pixel_transparency/allowed, or the window'sViewport.transparent_bgis set tofalse.
FlagsFLAG_NO_FOCUS=4
The window can't be focused. No-focus window will ignore all input, except mouse clicks. Set withunfocusable.
FlagsFLAG_POPUP=5
Window is part of menu orOptionButtondropdown. This flag can't be changed when the window is visible. An active popup window will exclusively receive all input, without stealing focus from its parent. Popup windows are automatically closed when uses click outside it, or when an application is switched. Popup window must have transient parent set (seetransient).
Note:This flag has no effect in embedded windows (unless said window is aPopup).
FlagsFLAG_EXTEND_TO_TITLE=6
Window content is expanded to the full size of the window. Unlike borderless window, the frame is left intact and can be used to resize the window, title bar is transparent, but have minimize/maximize/close buttons. Set withextend_to_title.
Note:This flag is implemented only on macOS.
Note:This flag has no effect in embedded windows.
FlagsFLAG_MOUSE_PASSTHROUGH=7
All mouse events are passed to the underlying window of the same application.
Note:This flag has no effect in embedded windows.
FlagsFLAG_SHARP_CORNERS=8
Window style is overridden, forcing sharp corners.
Note:This flag has no effect in embedded windows.
Note:This flag is implemented only on Windows (11).
FlagsFLAG_EXCLUDE_FROM_CAPTURE=9
Windows is excluded from screenshots taken byDisplayServer.screen_get_image(),DisplayServer.screen_get_image_rect(), andDisplayServer.screen_get_pixel().
Note:This flag has no effect in embedded windows.
Note:This flag is implemented on macOS and Windows (10, 20H1).
Note:Setting this flag will prevent standard screenshot methods from capturing a window image, but doesNOTguarantee that other apps won't be able to capture an image. It should not be used as a DRM or security measure.
FlagsFLAG_POPUP_WM_HINT=10
Signals the window manager that this window is supposed to be an implementation-defined "popup" (usually a floating, borderless, untileable and immovable child window).
FlagsFLAG_MINIMIZE_DISABLED=11
Window minimize button is disabled.
Note:This flag is implemented on macOS and Windows.
FlagsFLAG_MAXIMIZE_DISABLED=12
Window maximize button is disabled.
Note:This flag is implemented on macOS and Windows.
FlagsFLAG_MAX=13
Max value of theFlags.
enumContentScaleMode:🔗
ContentScaleModeCONTENT_SCALE_MODE_DISABLED=0
The content will not be scaled to match theWindow's size (content_scale_sizeis ignored).
ContentScaleModeCONTENT_SCALE_MODE_CANVAS_ITEMS=1
The content will be rendered at the target size. This is more performance-expensive thanCONTENT_SCALE_MODE_VIEWPORT, but provides better results.
ContentScaleModeCONTENT_SCALE_MODE_VIEWPORT=2
The content will be rendered at the base size and then scaled to the target size. More performant thanCONTENT_SCALE_MODE_CANVAS_ITEMS, but results in pixelated image.
enumContentScaleAspect:🔗
ContentScaleAspectCONTENT_SCALE_ASPECT_IGNORE=0
The aspect will be ignored. Scaling will simply stretch the content to fit the target size.
ContentScaleAspectCONTENT_SCALE_ASPECT_KEEP=1
The content's aspect will be preserved. If the target size has different aspect from the base one, the image will be centered and black bars will appear on left and right sides.
ContentScaleAspectCONTENT_SCALE_ASPECT_KEEP_WIDTH=2
The content can be expanded vertically. Scaling horizontally will result in keeping the width ratio and then black bars on left and right sides.
ContentScaleAspectCONTENT_SCALE_ASPECT_KEEP_HEIGHT=3
The content can be expanded horizontally. Scaling vertically will result in keeping the height ratio and then black bars on top and bottom sides.
ContentScaleAspectCONTENT_SCALE_ASPECT_EXPAND=4
The content's aspect will be preserved. If the target size has different aspect from the base one, the content will stay in the top-left corner and add an extra visible area in the stretched space.
enumContentScaleStretch:🔗
ContentScaleStretchCONTENT_SCALE_STRETCH_FRACTIONAL=0
The content will be stretched according to a fractional factor. This fills all the space available in the window, but allows "pixel wobble" to occur due to uneven pixel scaling.
ContentScaleStretchCONTENT_SCALE_STRETCH_INTEGER=1
The content will be stretched only according to an integer factor, preserving sharp pixels. This may leave a black background visible on the window's edges depending on the window size.
enumLayoutDirection:🔗
LayoutDirectionLAYOUT_DIRECTION_INHERITED=0
Automatic layout direction, determined from the parent window layout direction.
LayoutDirectionLAYOUT_DIRECTION_APPLICATION_LOCALE=1
Automatic layout direction, determined from the current locale.
LayoutDirectionLAYOUT_DIRECTION_LTR=2
Left-to-right layout direction.
LayoutDirectionLAYOUT_DIRECTION_RTL=3
Right-to-left layout direction.
LayoutDirectionLAYOUT_DIRECTION_SYSTEM_LOCALE=4
Automatic layout direction, determined from the system locale.
LayoutDirectionLAYOUT_DIRECTION_MAX=5
Represents the size of theLayoutDirectionenum.
LayoutDirectionLAYOUT_DIRECTION_LOCALE=1
Deprecated:UseLAYOUT_DIRECTION_APPLICATION_LOCALEinstead.
enumWindowInitialPosition:🔗
WindowInitialPositionWINDOW_INITIAL_POSITION_ABSOLUTE=0
Initial window position is determined byposition.
WindowInitialPositionWINDOW_INITIAL_POSITION_CENTER_PRIMARY_SCREEN=1
Initial window position is the center of the primary screen.
WindowInitialPositionWINDOW_INITIAL_POSITION_CENTER_MAIN_WINDOW_SCREEN=2
Initial window position is the center of the main window screen.
WindowInitialPositionWINDOW_INITIAL_POSITION_CENTER_OTHER_SCREEN=3
Initial window position is the center ofcurrent_screenscreen.
WindowInitialPositionWINDOW_INITIAL_POSITION_CENTER_SCREEN_WITH_MOUSE_FOCUS=4
Initial window position is the center of the screen containing the mouse pointer.
WindowInitialPositionWINDOW_INITIAL_POSITION_CENTER_SCREEN_WITH_KEYBOARD_FOCUS=5
Initial window position is the center of the screen containing the window with the keyboard focus.

## Constants
NOTIFICATION_VISIBILITY_CHANGED=30🔗
Emitted whenWindow's visibility changes, right beforevisibility_changed.
NOTIFICATION_THEME_CHANGED=32🔗
Sent when the node needs to refresh its theme items. This happens in one of the following cases:
- Thethemeproperty is changed on this node or any of its ancestors.
Thethemeproperty is changed on this node or any of its ancestors.
- Thetheme_type_variationproperty is changed on this node.
Thetheme_type_variationproperty is changed on this node.
- The node enters the scene tree.
The node enters the scene tree.
Note:As an optimization, this notification won't be sent from changes that occur while this node is outside of the scene tree. Instead, all of the theme item updates can be applied at once when the node enters the scene tree.

## Property Descriptions
Stringaccessibility_description=""🔗
- voidset_accessibility_description(value:String)
voidset_accessibility_description(value:String)
- Stringget_accessibility_description()
Stringget_accessibility_description()
The human-readable node description that is reported to assistive apps.
Stringaccessibility_name=""🔗
- voidset_accessibility_name(value:String)
voidset_accessibility_name(value:String)
- Stringget_accessibility_name()
Stringget_accessibility_name()
The human-readable node name that is reported to assistive apps.
boolalways_on_top=false🔗
- voidset_flag(flag:Flags, enabled:bool)
voidset_flag(flag:Flags, enabled:bool)
- boolget_flag(flag:Flags)const
boolget_flag(flag:Flags)const
Iftrue, the window will be on top of all other windows. Does not work iftransientis enabled.
boolauto_translate🔗
- voidset_auto_translate(value:bool)
voidset_auto_translate(value:bool)
- boolis_auto_translating()
boolis_auto_translating()
Deprecated:UseNode.auto_translate_modeandNode.can_auto_translate()instead.
Toggles if any text should automatically change to its translated version depending on the current locale.
boolborderless=false🔗
- voidset_flag(flag:Flags, enabled:bool)
voidset_flag(flag:Flags, enabled:bool)
- boolget_flag(flag:Flags)const
boolget_flag(flag:Flags)const
Iftrue, the window will have no borders.
ContentScaleAspectcontent_scale_aspect=0🔗
- voidset_content_scale_aspect(value:ContentScaleAspect)
voidset_content_scale_aspect(value:ContentScaleAspect)
- ContentScaleAspectget_content_scale_aspect()
ContentScaleAspectget_content_scale_aspect()
Specifies how the content's aspect behaves when theWindowis resized. The base aspect is determined bycontent_scale_size.
floatcontent_scale_factor=1.0🔗
- voidset_content_scale_factor(value:float)
voidset_content_scale_factor(value:float)
- floatget_content_scale_factor()
floatget_content_scale_factor()
Specifies the base scale ofWindow's content when itssizeis equal tocontent_scale_size. See alsoViewport.get_stretch_transform().
ContentScaleModecontent_scale_mode=0🔗
- voidset_content_scale_mode(value:ContentScaleMode)
voidset_content_scale_mode(value:ContentScaleMode)
- ContentScaleModeget_content_scale_mode()
ContentScaleModeget_content_scale_mode()
Specifies how the content is scaled when theWindowis resized.
Vector2icontent_scale_size=Vector2i(0,0)🔗
- voidset_content_scale_size(value:Vector2i)
voidset_content_scale_size(value:Vector2i)
- Vector2iget_content_scale_size()
Vector2iget_content_scale_size()
The content's base size in "virtual" pixels. Not to be confused withsize, which sets the actual window's physical size in pixels. If set to a value greater than0andcontent_scale_modeis set to a value other thanCONTENT_SCALE_MODE_DISABLED, theWindow's content will be scaled when the window is resized to a different size. Higher values will make the content appearsmaller, as it will be able to fit more of the project in view. On the rootWindow, this is set to matchProjectSettings.display/window/size/viewport_widthandProjectSettings.display/window/size/viewport_heightby default.
For example, when usingCONTENT_SCALE_MODE_CANVAS_ITEMSandcontent_scale_sizeset toVector2i(1280,720), using a window size of2560×1440will make 2D elements appear at double their original size, as the content is scaled by a factor of2.0(2560.0/1280.0=2.0,1440.0/720.0=2.0).
Seethe Base size section of the Multiple resolutions documentationfor details.
ContentScaleStretchcontent_scale_stretch=0🔗
- voidset_content_scale_stretch(value:ContentScaleStretch)
voidset_content_scale_stretch(value:ContentScaleStretch)
- ContentScaleStretchget_content_scale_stretch()
ContentScaleStretchget_content_scale_stretch()
The policy to use to determine the final scale factor for 2D elements. This affects howcontent_scale_factoris applied, in addition to the automatic scale factor determined bycontent_scale_size.
intcurrent_screen🔗
- voidset_current_screen(value:int)
voidset_current_screen(value:int)
- intget_current_screen()
intget_current_screen()
The screen the window is currently on.
boolexclude_from_capture=false🔗
- voidset_flag(flag:Flags, enabled:bool)
voidset_flag(flag:Flags, enabled:bool)
- boolget_flag(flag:Flags)const
boolget_flag(flag:Flags)const
Iftrue, theWindowis excluded from screenshots taken byDisplayServer.screen_get_image(),DisplayServer.screen_get_image_rect(), andDisplayServer.screen_get_pixel().
Note:This property is implemented on macOS and Windows.
Note:Enabling this setting will prevent standard screenshot methods from capturing a window image, but doesNOTguarantee that other apps won't be able to capture an image. It should not be used as a DRM or security measure.
boolexclusive=false🔗
- voidset_exclusive(value:bool)
voidset_exclusive(value:bool)
- boolis_exclusive()
boolis_exclusive()
Iftrue, theWindowwill be in exclusive mode. Exclusive windows are always on top of their parent and will block all input going to the parentWindow.
Needstransientenabled to work.
boolextend_to_title=false🔗
- voidset_flag(flag:Flags, enabled:bool)
voidset_flag(flag:Flags, enabled:bool)
- boolget_flag(flag:Flags)const
boolget_flag(flag:Flags)const
Iftrue, theWindowcontents is expanded to the full size of the window, window title bar is transparent.
Note:This property is implemented only on macOS.
Note:This property only works with native windows.
boolforce_native=false🔗
- voidset_force_native(value:bool)
voidset_force_native(value:bool)
- boolget_force_native()
boolget_force_native()
Iftrue, native window will be used regardless of parent viewport and project settings.
WindowInitialPositioninitial_position=0🔗
- voidset_initial_position(value:WindowInitialPosition)
voidset_initial_position(value:WindowInitialPosition)
- WindowInitialPositionget_initial_position()
WindowInitialPositionget_initial_position()
Specifies the initial type of position for theWindow.
boolkeep_title_visible=false🔗
- voidset_keep_title_visible(value:bool)
voidset_keep_title_visible(value:bool)
- boolget_keep_title_visible()
boolget_keep_title_visible()
Iftrue, theWindowwidth is expanded to keep the title bar text fully visible.
Vector2imax_size=Vector2i(0,0)🔗
- voidset_max_size(value:Vector2i)
voidset_max_size(value:Vector2i)
- Vector2iget_max_size()
Vector2iget_max_size()
If non-zero, theWindowcan't be resized to be bigger than this size.
Note:This property will be ignored if the value is lower thanmin_size.
boolmaximize_disabled=false🔗
- voidset_flag(flag:Flags, enabled:bool)
voidset_flag(flag:Flags, enabled:bool)
- boolget_flag(flag:Flags)const
boolget_flag(flag:Flags)const
Iftrue, theWindow's maximize button is disabled.
Note:If both minimize and maximize buttons are disabled, buttons are fully hidden, and only close button is visible.
Note:This property is implemented only on macOS and Windows.
Vector2imin_size=Vector2i(0,0)🔗
- voidset_min_size(value:Vector2i)
voidset_min_size(value:Vector2i)
- Vector2iget_min_size()
Vector2iget_min_size()
If non-zero, theWindowcan't be resized to be smaller than this size.
Note:This property will be ignored in favor ofget_contents_minimum_size()ifwrap_controlsis enabled and if its size is bigger.
boolminimize_disabled=false🔗
- voidset_flag(flag:Flags, enabled:bool)
voidset_flag(flag:Flags, enabled:bool)
- boolget_flag(flag:Flags)const
boolget_flag(flag:Flags)const
Iftrue, theWindow's minimize button is disabled.
Note:If both minimize and maximize buttons are disabled, buttons are fully hidden, and only close button is visible.
Note:This property is implemented only on macOS and Windows.
Modemode=0🔗
- voidset_mode(value:Mode)
voidset_mode(value:Mode)
- Modeget_mode()
Modeget_mode()
Set's the window's current mode.
Note:Fullscreen mode is not exclusive full screen on Windows and Linux.
Note:This method only works with native windows, i.e. the main window andWindow-derived nodes whenViewport.gui_embed_subwindowsis disabled in the main viewport.
boolmouse_passthrough=false🔗
- voidset_flag(flag:Flags, enabled:bool)
voidset_flag(flag:Flags, enabled:bool)
- boolget_flag(flag:Flags)const
boolget_flag(flag:Flags)const
Iftrue, all mouse events will be passed to the underlying window of the same application. See alsomouse_passthrough_polygon.
Note:This property is implemented on Linux (X11), macOS and Windows.
Note:This property only works with native windows.
PackedVector2Arraymouse_passthrough_polygon=PackedVector2Array()🔗
- voidset_mouse_passthrough_polygon(value:PackedVector2Array)
voidset_mouse_passthrough_polygon(value:PackedVector2Array)
- PackedVector2Arrayget_mouse_passthrough_polygon()
PackedVector2Arrayget_mouse_passthrough_polygon()
Sets a polygonal region of the window which accepts mouse events. Mouse events outside the region will be passed through.
Passing an empty array will disable passthrough support (all mouse events will be intercepted by the window, which is the default behavior).
```
# Set region, using Path2D node.
$Window.mouse_passthrough_polygon = $Path2D.curve.get_baked_points()

# Set region, using Polygon2D node.
$Window.mouse_passthrough_polygon = $Polygon2D.polygon

# Reset region to default.
$Window.mouse_passthrough_polygon = []
```
```
// Set region, using Path2D node.
GetNode<Window>("Window").MousePassthroughPolygon = GetNode<Path2D>("Path2D").Curve.GetBakedPoints();

// Set region, using Polygon2D node.
GetNode<Window>("Window").MousePassthroughPolygon = GetNode<Polygon2D>("Polygon2D").Polygon;

// Reset region to default.
GetNode<Window>("Window").MousePassthroughPolygon = [];
```
Note:This property is ignored ifmouse_passthroughis set totrue.
Note:On Windows, the portion of a window that lies outside the region is not drawn, while on Linux (X11) and macOS it is.
Note:This property is implemented on Linux (X11), macOS and Windows.
Note:The returned array iscopiedand any changes to it will not update the original property value. SeePackedVector2Arrayfor more details.
Rect2inonclient_area=Rect2i(0,0,0,0)🔗
- voidset_nonclient_area(value:Rect2i)
voidset_nonclient_area(value:Rect2i)
- Rect2iget_nonclient_area()
Rect2iget_nonclient_area()
If set, defines the window's custom decoration area which will receive mouse input, even if normal input to the window is blocked (such as when it has an exclusive child opened). See alsononclient_window_input.
boolpopup_window=false🔗
- voidset_flag(flag:Flags, enabled:bool)
voidset_flag(flag:Flags, enabled:bool)
- boolget_flag(flag:Flags)const
boolget_flag(flag:Flags)const
Iftrue, theWindowwill be considered a popup. Popups are sub-windows that don't show as separate windows in system's window manager's window list and will send close request when anything is clicked outside of them (unlessexclusiveis enabled).
boolpopup_wm_hint=false🔗
- voidset_flag(flag:Flags, enabled:bool)
voidset_flag(flag:Flags, enabled:bool)
- boolget_flag(flag:Flags)const
boolget_flag(flag:Flags)const
Iftrue, theWindowwill signal to the window manager that it is supposed to be an implementation-defined "popup" (usually a floating, borderless, untileable and immovable child window).
Vector2iposition=Vector2i(0,0)🔗
- voidset_position(value:Vector2i)
voidset_position(value:Vector2i)
- Vector2iget_position()
Vector2iget_position()
The window's position in pixels.
IfProjectSettings.display/window/subwindows/embed_subwindowsisfalse, the position is in absolute screen coordinates. This typically applies to editor plugins. If the setting istrue, the window's position is in the coordinates of its parentViewport.
Note:This property only works ifinitial_positionis set toWINDOW_INITIAL_POSITION_ABSOLUTE.
boolsharp_corners=false🔗
- voidset_flag(flag:Flags, enabled:bool)
voidset_flag(flag:Flags, enabled:bool)
- boolget_flag(flag:Flags)const
boolget_flag(flag:Flags)const
Iftrue, theWindowwill override the OS window style to display sharp corners.
Note:This property is implemented only on Windows (11).
Note:This property only works with native windows.
Vector2isize=Vector2i(100,100)🔗
- voidset_size(value:Vector2i)
voidset_size(value:Vector2i)
- Vector2iget_size()
Vector2iget_size()
The window's size in pixels. See alsocontent_scale_size, which doesn't set the window's physical size but affects how scaling works relative to the currentcontent_scale_mode.
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
The name of a theme type variation used by thisWindowto look up its own theme items. SeeControl.theme_type_variationfor more details.
Stringtitle=""🔗
- voidset_title(value:String)
voidset_title(value:String)
- Stringget_title()
Stringget_title()
The window's title. If theWindowis native, title styles set inThemewill have no effect.
booltransient=false🔗
- voidset_transient(value:bool)
voidset_transient(value:bool)
- boolis_transient()
boolis_transient()
Iftrue, theWindowis transient, i.e. it's considered a child of anotherWindow. The transient window will be destroyed with its transient parent and will return focus to their parent when closed. The transient window is displayed on top of a non-exclusive full-screen parent window. Transient windows can't enter full-screen mode.
Note that behavior might be different depending on the platform.
booltransient_to_focused=false🔗
- voidset_transient_to_focused(value:bool)
voidset_transient_to_focused(value:bool)
- boolis_transient_to_focused()
boolis_transient_to_focused()
Iftrue, and theWindowistransient, this window will (at the time of becoming visible) become transient to the currently focused window instead of the immediate parent window in the hierarchy. Note that the transient parent is assigned at the time this window becomes visible, so changing it afterwards has no effect until re-shown.
booltransparent=false🔗
- voidset_flag(flag:Flags, enabled:bool)
voidset_flag(flag:Flags, enabled:bool)
- boolget_flag(flag:Flags)const
boolget_flag(flag:Flags)const
Iftrue, theWindow's background can be transparent. This is best used with embedded windows.
Note:Transparency support is implemented on Linux, macOS and Windows, but availability might vary depending on GPU driver, display manager, and compositor capabilities.
Note:This property has no effect ifProjectSettings.display/window/per_pixel_transparency/allowedis set tofalse.
boolunfocusable=false🔗
- voidset_flag(flag:Flags, enabled:bool)
voidset_flag(flag:Flags, enabled:bool)
- boolget_flag(flag:Flags)const
boolget_flag(flag:Flags)const
Iftrue, theWindowcan't be focused nor interacted with. It can still be visible.
boolunresizable=false🔗
- voidset_flag(flag:Flags, enabled:bool)
voidset_flag(flag:Flags, enabled:bool)
- boolget_flag(flag:Flags)const
boolget_flag(flag:Flags)const
Iftrue, the window can't be resized.
boolvisible=true🔗
- voidset_visible(value:bool)
voidset_visible(value:bool)
- boolis_visible()
boolis_visible()
Iftrue, the window is visible.
boolwrap_controls=false🔗
- voidset_wrap_controls(value:bool)
voidset_wrap_controls(value:bool)
- boolis_wrapping_controls()
boolis_wrapping_controls()
Iftrue, the window's size will automatically update when a child node is added or removed, ignoringmin_sizeif the new size is bigger.
Iffalse, you need to callchild_controls_changed()manually.

## Method Descriptions
Vector2_get_contents_minimum_size()virtualconst🔗
Virtual method to be implemented by the user. Overrides the value returned byget_contents_minimum_size().
voidadd_theme_color_override(name:StringName, color:Color)🔗
Creates a local override for a themeColorwith the specifiedname. Local overrides always take precedence when fetching theme items for the control. An override can be removed withremove_theme_color_override().
See alsoget_theme_color()andControl.add_theme_color_override()for more details.
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
See alsoget_theme_stylebox()andControl.add_theme_stylebox_override()for more details.
voidbegin_bulk_theme_override()🔗
Prevents*_theme_*_overridemethods from emittingNOTIFICATION_THEME_CHANGEDuntilend_bulk_theme_override()is called.
boolcan_draw()const🔗
Returns whether the window is being drawn to the screen.
voidchild_controls_changed()🔗
Requests an update of theWindowsize to fit underlyingControlnodes.
voidend_bulk_theme_override()🔗
Ends a bulk theme override update. Seebegin_bulk_theme_override().
Vector2get_contents_minimum_size()const🔗
Returns the combined minimum size from the childControlnodes of the window. Usechild_controls_changed()to update it when child nodes have changed.
The value returned by this method can be overridden with_get_contents_minimum_size().
boolget_flag(flag:Flags)const🔗
Returnstrueif theflagis set.
Windowget_focused_window()static🔗
Returns the focused window.
LayoutDirectionget_layout_direction()const🔗
Returns layout direction and text writing direction.
Vector2iget_position_with_decorations()const🔗
Returns the window's position including its border.
Note:Ifvisibleisfalse, this method returns the same value asposition.
Vector2iget_size_with_decorations()const🔗
Returns the window's size including its border.
Note:Ifvisibleisfalse, this method returns the same value assize.
Colorget_theme_color(name:StringName, theme_type:StringName= &"")const🔗
Returns aColorfrom the first matchingThemein the tree if thatThemehas a color item with the specifiednameandtheme_type.
SeeControl.get_theme_color()for more details.
intget_theme_constant(name:StringName, theme_type:StringName= &"")const🔗
Returns a constant from the first matchingThemein the tree if thatThemehas a constant item with the specifiednameandtheme_type.
SeeControl.get_theme_color()for more details.
floatget_theme_default_base_scale()const🔗
Returns the default base scale value from the first matchingThemein the tree if thatThemehas a validTheme.default_base_scalevalue.
SeeControl.get_theme_color()for details.
Fontget_theme_default_font()const🔗
Returns the default font from the first matchingThemein the tree if thatThemehas a validTheme.default_fontvalue.
SeeControl.get_theme_color()for details.
intget_theme_default_font_size()const🔗
Returns the default font size value from the first matchingThemein the tree if thatThemehas a validTheme.default_font_sizevalue.
SeeControl.get_theme_color()for details.
Fontget_theme_font(name:StringName, theme_type:StringName= &"")const🔗
Returns aFontfrom the first matchingThemein the tree if thatThemehas a font item with the specifiednameandtheme_type.
SeeControl.get_theme_color()for details.
intget_theme_font_size(name:StringName, theme_type:StringName= &"")const🔗
Returns a font size from the first matchingThemein the tree if thatThemehas a font size item with the specifiednameandtheme_type.
SeeControl.get_theme_color()for details.
Texture2Dget_theme_icon(name:StringName, theme_type:StringName= &"")const🔗
Returns an icon from the first matchingThemein the tree if thatThemehas an icon item with the specifiednameandtheme_type.
SeeControl.get_theme_color()for details.
StyleBoxget_theme_stylebox(name:StringName, theme_type:StringName= &"")const🔗
Returns aStyleBoxfrom the first matchingThemein the tree if thatThemehas a stylebox item with the specifiednameandtheme_type.
SeeControl.get_theme_color()for details.
intget_window_id()const🔗
Returns the ID of the window.
voidgrab_focus()🔗
Causes the window to grab focus, allowing it to receive user input.
boolhas_focus()const🔗
Returnstrueif the window is focused.
boolhas_theme_color(name:StringName, theme_type:StringName= &"")const🔗
Returnstrueif there is a matchingThemein the tree that has a color item with the specifiednameandtheme_type.
SeeControl.get_theme_color()for details.
boolhas_theme_color_override(name:StringName)const🔗
Returnstrueif there is a local override for a themeColorwith the specifiednamein thisControlnode.
Seeadd_theme_color_override().
boolhas_theme_constant(name:StringName, theme_type:StringName= &"")const🔗
Returnstrueif there is a matchingThemein the tree that has a constant item with the specifiednameandtheme_type.
SeeControl.get_theme_color()for details.
boolhas_theme_constant_override(name:StringName)const🔗
Returnstrueif there is a local override for a theme constant with the specifiednamein thisControlnode.
Seeadd_theme_constant_override().
boolhas_theme_font(name:StringName, theme_type:StringName= &"")const🔗
Returnstrueif there is a matchingThemein the tree that has a font item with the specifiednameandtheme_type.
SeeControl.get_theme_color()for details.
boolhas_theme_font_override(name:StringName)const🔗
Returnstrueif there is a local override for a themeFontwith the specifiednamein thisControlnode.
Seeadd_theme_font_override().
boolhas_theme_font_size(name:StringName, theme_type:StringName= &"")const🔗
Returnstrueif there is a matchingThemein the tree that has a font size item with the specifiednameandtheme_type.
SeeControl.get_theme_color()for details.
boolhas_theme_font_size_override(name:StringName)const🔗
Returnstrueif there is a local override for a theme font size with the specifiednamein thisControlnode.
Seeadd_theme_font_size_override().
boolhas_theme_icon(name:StringName, theme_type:StringName= &"")const🔗
Returnstrueif there is a matchingThemein the tree that has an icon item with the specifiednameandtheme_type.
SeeControl.get_theme_color()for details.
boolhas_theme_icon_override(name:StringName)const🔗
Returnstrueif there is a local override for a theme icon with the specifiednamein thisControlnode.
Seeadd_theme_icon_override().
boolhas_theme_stylebox(name:StringName, theme_type:StringName= &"")const🔗
Returnstrueif there is a matchingThemein the tree that has a stylebox item with the specifiednameandtheme_type.
SeeControl.get_theme_color()for details.
boolhas_theme_stylebox_override(name:StringName)const🔗
Returnstrueif there is a local override for a themeStyleBoxwith the specifiednamein thisControlnode.
Seeadd_theme_stylebox_override().
voidhide()🔗
Hides the window. This is not the same as minimized state. Hidden window can't be interacted with and needs to be made visible withshow().
boolis_embedded()const🔗
Returnstrueif the window is currently embedded in another window.
boolis_layout_rtl()const🔗
Returnstrueif the layout is right-to-left.
boolis_maximize_allowed()const🔗
Returnstrueif the window can be maximized (the maximize button is enabled).
boolis_using_font_oversampling()const🔗
Returnstrueif font oversampling is enabled. Seeset_use_font_oversampling().
voidmove_to_center()🔗
Centers the window in the current screen. If the window is embedded, it is centered in the embedderViewportinstead.
voidmove_to_foreground()🔗
Deprecated:Usegrab_focus()instead.
Causes the window to grab focus, allowing it to receive user input.
voidpopup(rect:Rect2i= Rect2i(0, 0, 0, 0))🔗
Shows theWindowand makes it transient (seetransient). Ifrectis provided, it will be set as theWindow's size. Fails if called on the main window.
IfProjectSettings.display/window/subwindows/embed_subwindowsistrue(single-window mode),rect's coordinates are global and relative to the main window's top-left corner (excluding window decorations). Ifrect's position coordinates are negative, the window will be located outside the main window and may not be visible as a result.
IfProjectSettings.display/window/subwindows/embed_subwindowsisfalse(multi-window mode),rect's coordinates are global and relative to the top-left corner of the leftmost screen. Ifrect's position coordinates are negative, the window will be placed at the top-left corner of the screen.
Note:rectmust be in global coordinates if specified.
voidpopup_centered(minsize:Vector2i= Vector2i(0, 0))🔗
Popups theWindowat the center of the current screen, with optionally given minimum size. If theWindowis embedded, it will be centered in the parentViewportinstead.
Note:Calling it with the default value ofminsizeis equivalent to calling it withsize.
voidpopup_centered_clamped(minsize:Vector2i= Vector2i(0, 0), fallback_ratio:float= 0.75)🔗
Popups theWindowcentered inside its parentWindow.fallback_ratiodetermines the maximum size of theWindow, in relation to its parent.
Note:Calling it with the default value ofminsizeis equivalent to calling it withsize.
voidpopup_centered_ratio(ratio:float= 0.8)🔗
IfWindowis embedded, popups theWindowcentered inside its embedder and sets its size as aratioof embedder's size.
IfWindowis a native window, popups theWindowcentered inside the screen of its parentWindowand sets its size as aratioof the screen size.
voidpopup_exclusive(from_node:Node, rect:Rect2i= Rect2i(0, 0, 0, 0))🔗
Attempts to parent this dialog to the last exclusive window relative tofrom_node, and then callspopup()on it. The dialog must have no current parent, otherwise the method fails.
See alsoset_unparent_when_invisible()andNode.get_last_exclusive_window().
voidpopup_exclusive_centered(from_node:Node, minsize:Vector2i= Vector2i(0, 0))🔗
Attempts to parent this dialog to the last exclusive window relative tofrom_node, and then callspopup_centered()on it. The dialog must have no current parent, otherwise the method fails.
See alsoset_unparent_when_invisible()andNode.get_last_exclusive_window().
voidpopup_exclusive_centered_clamped(from_node:Node, minsize:Vector2i= Vector2i(0, 0), fallback_ratio:float= 0.75)🔗
Attempts to parent this dialog to the last exclusive window relative tofrom_node, and then callspopup_centered_clamped()on it. The dialog must have no current parent, otherwise the method fails.
See alsoset_unparent_when_invisible()andNode.get_last_exclusive_window().
voidpopup_exclusive_centered_ratio(from_node:Node, ratio:float= 0.8)🔗
Attempts to parent this dialog to the last exclusive window relative tofrom_node, and then callspopup_centered_ratio()on it. The dialog must have no current parent, otherwise the method fails.
See alsoset_unparent_when_invisible()andNode.get_last_exclusive_window().
voidpopup_exclusive_on_parent(from_node:Node, parent_rect:Rect2i)🔗
Attempts to parent this dialog to the last exclusive window relative tofrom_node, and then callspopup_on_parent()on it. The dialog must have no current parent, otherwise the method fails.
See alsoset_unparent_when_invisible()andNode.get_last_exclusive_window().
voidpopup_on_parent(parent_rect:Rect2i)🔗
Popups theWindowwith a position shifted by parentWindow's position. If theWindowis embedded, has the same effect aspopup().
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
voidrequest_attention()🔗
Tells the OS that theWindowneeds an attention. This makes the window stand out in some way depending on the system, e.g. it might blink on the task bar.
voidreset_size()🔗
Resets the size to the minimum size, which is the max ofmin_sizeand (ifwrap_controlsis enabled)get_contents_minimum_size(). This is equivalent to callingset_size(Vector2i())(or any size below the minimum).
voidset_flag(flag:Flags, enabled:bool)🔗
Sets a specified window flag.
voidset_ime_active(active:bool)🔗
Ifactiveistrue, enables system's native IME (Input Method Editor).
voidset_ime_position(position:Vector2i)🔗
Moves IME to the given position.
voidset_layout_direction(direction:LayoutDirection)🔗
Sets layout direction and text writing direction. Right-to-left layouts are necessary for certain languages (e.g. Arabic and Hebrew).
voidset_unparent_when_invisible(unparent:bool)🔗
Ifunparentistrue, the window is automatically unparented when going invisible.
Note:Make sure to keep a reference to the node, otherwise it will be orphaned. You also need to manually callNode.queue_free()to free the window if it's not parented.
voidset_use_font_oversampling(enable:bool)🔗
Enables font oversampling. This makes fonts look better when they are scaled up.
voidshow()🔗
Makes theWindowappear. This enables interactions with theWindowand doesn't change any of its property other than visibility (unlike e.g.popup()).
voidstart_drag()🔗
Starts an interactive drag operation on the window, using the current mouse position. Call this method when handling a mouse button being pressed to simulate a pressed event on the window's title bar. Using this method allows the window to participate in space switching, tiling, and other system features.
voidstart_resize(edge:WindowResizeEdge)🔗
Starts an interactive resize operation on the window, using the current mouse position. Call this method when handling a mouse button being pressed to simulate a pressed event on the window's edge.

## Theme Property Descriptions
Colortitle_color=Color(0.875,0.875,0.875,1)🔗
The color of the title's text.
Colortitle_outline_modulate=Color(0,0,0,1)🔗
The color of the title's text outline.
intclose_h_offset=18🔗
Horizontal position offset of the close button, relative to the end of the title bar, towards the beginning of the title bar.
intclose_v_offset=24🔗
Vertical position offset of the close button, relative to the bottom of the title bar, towards the top of the title bar.
intresize_margin=4🔗
Defines the outside margin at which the window border can be grabbed with mouse and resized.
inttitle_height=36🔗
Height of the title bar.
inttitle_outline_size=0🔗
The size of the title outline.
Fonttitle_font🔗
The font used to draw the title.
inttitle_font_size🔗
The size of the title font.
Texture2Dclose🔗
The icon for the close button.
Texture2Dclose_pressed🔗
The icon for the close button when it's being pressed.
StyleBoxembedded_border🔗
The background style used when theWindowis embedded. Note that this is drawn only under the window's content, excluding the title. For proper borders and title bar style, you can useexpand_margin_*properties ofStyleBoxFlat.
Note:The content background will not be visible unlesstransparentis enabled.
StyleBoxembedded_unfocused_border🔗
The background style used when theWindowis embedded and unfocused.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.