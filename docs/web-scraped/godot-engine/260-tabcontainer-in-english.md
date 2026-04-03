# TabContainer in English

# TabContainer

Inherits:Container<Control<CanvasItem<Node<Object
A container that creates a tab for each child control, displaying only the active tab's control.

## Description

Arranges child controls into a tabbed view, creating a tab for each one. The active tab's corresponding control is made visible, while all other child controls are hidden. Ignores non-control children.
Note:The drawing of the clickable tabs is handled by this node;TabBaris not needed.

## Tutorials

- Using Containers
Using Containers

## Properties

| bool | all_tabs_in_front | false |
|---|---|---|
| bool | clip_tabs | true |
| int | current_tab | -1 |
| bool | deselect_enabled | false |
| bool | drag_to_rearrange_enabled | false |
| bool | switch_on_drag_hover | true |
| AlignmentMode | tab_alignment | 0 |
| FocusMode | tab_focus_mode | 2 |
| TabPosition | tabs_position | 0 |
| int | tabs_rearrange_group | -1 |
| bool | tabs_visible | true |
| bool | use_hidden_tabs_for_min_size | false |

bool
all_tabs_in_front
false
bool
clip_tabs
true
current_tab
bool
deselect_enabled
false
bool
drag_to_rearrange_enabled
false
bool
switch_on_drag_hover
true
AlignmentMode
tab_alignment
FocusMode
tab_focus_mode
TabPosition
tabs_position
tabs_rearrange_group
bool
tabs_visible
true
bool
use_hidden_tabs_for_min_size
false

## Methods

| Control | get_current_tab_control()const |
|---|---|
| Popup | get_popup()const |
| int | get_previous_tab()const |
| TabBar | get_tab_bar()const |
| Texture2D | get_tab_button_icon(tab_idx:int)const |
| Control | get_tab_control(tab_idx:int)const |
| int | get_tab_count()const |
| Texture2D | get_tab_icon(tab_idx:int)const |
| int | get_tab_icon_max_width(tab_idx:int)const |
| int | get_tab_idx_at_point(point:Vector2)const |
| int | get_tab_idx_from_control(control:Control)const |
| Variant | get_tab_metadata(tab_idx:int)const |
| String | get_tab_title(tab_idx:int)const |
| String | get_tab_tooltip(tab_idx:int)const |
| bool | is_tab_disabled(tab_idx:int)const |
| bool | is_tab_hidden(tab_idx:int)const |
| bool | select_next_available() |
| bool | select_previous_available() |
| void | set_popup(popup:Node) |
| void | set_tab_button_icon(tab_idx:int, icon:Texture2D) |
| void | set_tab_disabled(tab_idx:int, disabled:bool) |
| void | set_tab_hidden(tab_idx:int, hidden:bool) |
| void | set_tab_icon(tab_idx:int, icon:Texture2D) |
| void | set_tab_icon_max_width(tab_idx:int, width:int) |
| void | set_tab_metadata(tab_idx:int, metadata:Variant) |
| void | set_tab_title(tab_idx:int, title:String) |
| void | set_tab_tooltip(tab_idx:int, tooltip:String) |

Control
get_current_tab_control()const
Popup
get_popup()const
get_previous_tab()const
TabBar
get_tab_bar()const
Texture2D
get_tab_button_icon(tab_idx:int)const
Control
get_tab_control(tab_idx:int)const
get_tab_count()const
Texture2D
get_tab_icon(tab_idx:int)const
get_tab_icon_max_width(tab_idx:int)const
get_tab_idx_at_point(point:Vector2)const
get_tab_idx_from_control(control:Control)const
Variant
get_tab_metadata(tab_idx:int)const
String
get_tab_title(tab_idx:int)const
String
get_tab_tooltip(tab_idx:int)const
bool
is_tab_disabled(tab_idx:int)const
bool
is_tab_hidden(tab_idx:int)const
bool
select_next_available()
bool
select_previous_available()
void
set_popup(popup:Node)
void
set_tab_button_icon(tab_idx:int, icon:Texture2D)
void
set_tab_disabled(tab_idx:int, disabled:bool)
void
set_tab_hidden(tab_idx:int, hidden:bool)
void
set_tab_icon(tab_idx:int, icon:Texture2D)
void
set_tab_icon_max_width(tab_idx:int, width:int)
void
set_tab_metadata(tab_idx:int, metadata:Variant)
void
set_tab_title(tab_idx:int, title:String)
void
set_tab_tooltip(tab_idx:int, tooltip:String)

## Theme Properties

| Color | drop_mark_color | Color(1,1,1,1) |
|---|---|---|
| Color | font_disabled_color | Color(0.875,0.875,0.875,0.5) |
| Color | font_hovered_color | Color(0.95,0.95,0.95,1) |
| Color | font_outline_color | Color(0,0,0,1) |
| Color | font_selected_color | Color(0.95,0.95,0.95,1) |
| Color | font_unselected_color | Color(0.7,0.7,0.7,1) |
| Color | icon_disabled_color | Color(1,1,1,1) |
| Color | icon_hovered_color | Color(1,1,1,1) |
| Color | icon_selected_color | Color(1,1,1,1) |
| Color | icon_unselected_color | Color(1,1,1,1) |
| int | icon_max_width | 0 |
| int | icon_separation | 4 |
| int | outline_size | 0 |
| int | side_margin | 8 |
| int | tab_separation | 0 |
| Font | font |  |
| int | font_size |  |
| Texture2D | decrement |  |
| Texture2D | decrement_highlight |  |
| Texture2D | drop_mark |  |
| Texture2D | increment |  |
| Texture2D | increment_highlight |  |
| Texture2D | menu |  |
| Texture2D | menu_highlight |  |
| StyleBox | panel |  |
| StyleBox | tab_disabled |  |
| StyleBox | tab_focus |  |
| StyleBox | tab_hovered |  |
| StyleBox | tab_selected |  |
| StyleBox | tab_unselected |  |
| StyleBox | tabbar_background |  |

Color
drop_mark_color
Color(1,1,1,1)
Color
font_disabled_color
Color(0.875,0.875,0.875,0.5)
Color
font_hovered_color
Color(0.95,0.95,0.95,1)
Color
font_outline_color
Color(0,0,0,1)
Color
font_selected_color
Color(0.95,0.95,0.95,1)
Color
font_unselected_color
Color(0.7,0.7,0.7,1)
Color
icon_disabled_color
Color(1,1,1,1)
Color
icon_hovered_color
Color(1,1,1,1)
Color
icon_selected_color
Color(1,1,1,1)
Color
icon_unselected_color
Color(1,1,1,1)
icon_max_width
icon_separation
outline_size
side_margin
tab_separation
Font
font
font_size
Texture2D
decrement
Texture2D
decrement_highlight
Texture2D
drop_mark
Texture2D
increment
Texture2D
increment_highlight
Texture2D
menu
Texture2D
menu_highlight
StyleBox
panel
StyleBox
tab_disabled
StyleBox
tab_focus
StyleBox
tab_hovered
StyleBox
tab_selected
StyleBox
tab_unselected
StyleBox
tabbar_background

## Signals

active_tab_rearranged(idx_to:int)🔗
Emitted when the active tab is rearranged via mouse drag. Seedrag_to_rearrange_enabled.
pre_popup_pressed()🔗
Emitted when theTabContainer'sPopupbutton is clicked. Seeset_popup()for details.
tab_button_pressed(tab:int)🔗
Emitted when the user clicks on the button icon on this tab.
tab_changed(tab:int)🔗
Emitted when switching to another tab.
tab_clicked(tab:int)🔗
Emitted when a tab is clicked, even if it is the current tab.
tab_hovered(tab:int)🔗
Emitted when a tab is hovered by the mouse.
tab_selected(tab:int)🔗
Emitted when a tab is selected via click, directional input, or script, even if it is the current tab.

## Enumerations

enumTabPosition:🔗
TabPositionPOSITION_TOP=0
Places the tab bar at the top.
TabPositionPOSITION_BOTTOM=1
Places the tab bar at the bottom. The tab bar'sStyleBoxwill be flipped vertically.
TabPositionPOSITION_MAX=2
Represents the size of theTabPositionenum.

## Property Descriptions

boolall_tabs_in_front=false🔗

- voidset_all_tabs_in_front(value:bool)
voidset_all_tabs_in_front(value:bool)
- boolis_all_tabs_in_front()
boolis_all_tabs_in_front()
Iftrue, all tabs are drawn in front of the panel. Iffalse, inactive tabs are drawn behind the panel.
boolclip_tabs=true🔗
- voidset_clip_tabs(value:bool)
voidset_clip_tabs(value:bool)
- boolget_clip_tabs()
boolget_clip_tabs()
Iftrue, tabs overflowing this node's width will be hidden, displaying two navigation buttons instead. Otherwise, this node's minimum size is updated so that all tabs are visible.
intcurrent_tab=-1🔗
- voidset_current_tab(value:int)
voidset_current_tab(value:int)
- intget_current_tab()
intget_current_tab()
The current tab index. When set, this index'sControlnode'svisibleproperty is set totrueand all others are set tofalse.
A value of-1means that no tab is selected.
booldeselect_enabled=false🔗
- voidset_deselect_enabled(value:bool)
voidset_deselect_enabled(value:bool)
- boolget_deselect_enabled()
boolget_deselect_enabled()
Iftrue, all tabs can be deselected so that no tab is selected. Click on thecurrent_tabto deselect it.
Only the tab header will be shown if no tabs are selected.
booldrag_to_rearrange_enabled=false🔗
- voidset_drag_to_rearrange_enabled(value:bool)
voidset_drag_to_rearrange_enabled(value:bool)
- boolget_drag_to_rearrange_enabled()
boolget_drag_to_rearrange_enabled()
Iftrue, tabs can be rearranged with mouse drag.
boolswitch_on_drag_hover=true🔗
- voidset_switch_on_drag_hover(value:bool)
voidset_switch_on_drag_hover(value:bool)
- boolget_switch_on_drag_hover()
boolget_switch_on_drag_hover()
Iftrue, hovering over a tab while dragging something will switch to that tab. Does not have effect when hovering another tab to rearrange.
AlignmentModetab_alignment=0🔗
- voidset_tab_alignment(value:AlignmentMode)
voidset_tab_alignment(value:AlignmentMode)
- AlignmentModeget_tab_alignment()
AlignmentModeget_tab_alignment()
The position at which tabs will be placed.
FocusModetab_focus_mode=2🔗
- voidset_tab_focus_mode(value:FocusMode)
voidset_tab_focus_mode(value:FocusMode)
- FocusModeget_tab_focus_mode()
FocusModeget_tab_focus_mode()
The focus access mode for the internalTabBarnode.
TabPositiontabs_position=0🔗
- voidset_tabs_position(value:TabPosition)
voidset_tabs_position(value:TabPosition)
- TabPositionget_tabs_position()
TabPositionget_tabs_position()
The horizontal alignment of the tabs.
inttabs_rearrange_group=-1🔗
- voidset_tabs_rearrange_group(value:int)
voidset_tabs_rearrange_group(value:int)
- intget_tabs_rearrange_group()
intget_tabs_rearrange_group()
TabContainers with the same rearrange group ID will allow dragging the tabs between them. Enable drag withdrag_to_rearrange_enabled.
Setting this to-1will disable rearranging betweenTabContainers.
booltabs_visible=true🔗
- voidset_tabs_visible(value:bool)
voidset_tabs_visible(value:bool)
- boolare_tabs_visible()
boolare_tabs_visible()
Iftrue, tabs are visible. Iffalse, tabs' content and titles are hidden.
booluse_hidden_tabs_for_min_size=false🔗
- voidset_use_hidden_tabs_for_min_size(value:bool)
voidset_use_hidden_tabs_for_min_size(value:bool)
- boolget_use_hidden_tabs_for_min_size()
boolget_use_hidden_tabs_for_min_size()
Iftrue, childControlnodes that are hidden have their minimum size take into account in the total, instead of only the currently visible one.

## Method Descriptions

Controlget_current_tab_control()const🔗
Returns the childControlnode located at the active tab index.
Popupget_popup()const🔗
Returns thePopupnode instance if one has been set already withset_popup().
Warning:This is a required internal node, removing and freeing it may cause a crash. If you wish to hide it or any of its children, use theirWindow.visibleproperty.
intget_previous_tab()const🔗
Returns the previously active tab index.
TabBarget_tab_bar()const🔗
Returns theTabBarcontained in this container.
Warning:This is a required internal node, removing and freeing it or editing its tabs may cause a crash. If you wish to edit the tabs, use the methods provided inTabContainer.
Texture2Dget_tab_button_icon(tab_idx:int)const🔗
Returns the button icon from the tab at indextab_idx.
Controlget_tab_control(tab_idx:int)const🔗
Returns theControlnode from the tab at indextab_idx.
intget_tab_count()const🔗
Returns the number of tabs.
Texture2Dget_tab_icon(tab_idx:int)const🔗
Returns theTexture2Dfor the tab at indextab_idxornullif the tab has noTexture2D.
intget_tab_icon_max_width(tab_idx:int)const🔗
Returns the maximum allowed width of the icon for the tab at indextab_idx.
intget_tab_idx_at_point(point:Vector2)const🔗
Returns the index of the tab at local coordinatespoint. Returns-1if the point is outside the control boundaries or if there's no tab at the queried position.
intget_tab_idx_from_control(control:Control)const🔗
Returns the index of the tab tied to the givencontrol. The control must be a child of theTabContainer.
Variantget_tab_metadata(tab_idx:int)const🔗
Returns the metadata value set to the tab at indextab_idxusingset_tab_metadata(). If no metadata was previously set, returnsnullby default.
Stringget_tab_title(tab_idx:int)const🔗
Returns the title of the tab at indextab_idx. Tab titles default to the name of the indexed child node, but this can be overridden withset_tab_title().
Stringget_tab_tooltip(tab_idx:int)const🔗
Returns the tooltip text of the tab at indextab_idx.
boolis_tab_disabled(tab_idx:int)const🔗
Returnstrueif the tab at indextab_idxis disabled.
boolis_tab_hidden(tab_idx:int)const🔗
Returnstrueif the tab at indextab_idxis hidden.
boolselect_next_available()🔗
Selects the first available tab with greater index than the currently selected. Returnstrueif tab selection changed.
boolselect_previous_available()🔗
Selects the first available tab with lower index than the currently selected. Returnstrueif tab selection changed.
voidset_popup(popup:Node)🔗
If set on aPopupnode instance, a popup menu icon appears in the top-right corner of theTabContainer(setting it tonullwill make it go away). Clicking it will expand thePopupnode.
voidset_tab_button_icon(tab_idx:int, icon:Texture2D)🔗
Sets the button icon from the tab at indextab_idx.
voidset_tab_disabled(tab_idx:int, disabled:bool)🔗
Ifdisabledistrue, disables the tab at indextab_idx, making it non-interactable.
voidset_tab_hidden(tab_idx:int, hidden:bool)🔗
Ifhiddenistrue, hides the tab at indextab_idx, making it disappear from the tab area.
voidset_tab_icon(tab_idx:int, icon:Texture2D)🔗
Sets an icon for the tab at indextab_idx.
voidset_tab_icon_max_width(tab_idx:int, width:int)🔗
Sets the maximum allowed width of the icon for the tab at indextab_idx. This limit is applied on top of the default size of the icon and on top oficon_max_width. The height is adjusted according to the icon's ratio.
voidset_tab_metadata(tab_idx:int, metadata:Variant)🔗
Sets the metadata value for the tab at indextab_idx, which can be retrieved later usingget_tab_metadata().
voidset_tab_title(tab_idx:int, title:String)🔗
Sets a custom title for the tab at indextab_idx(tab titles default to the name of the indexed child node). Set it back to the child's name to make the tab default to it again.
voidset_tab_tooltip(tab_idx:int, tooltip:String)🔗
Sets a custom tooltip text for tab at indextab_idx.
Note:By default, if thetooltipis empty and the tab text is truncated (not all characters fit into the tab), the title will be displayed as a tooltip. To hide the tooltip, assign""as thetooltiptext.

## Theme Property Descriptions

Colordrop_mark_color=Color(1,1,1,1)🔗
Modulation color for thedrop_markicon.
Colorfont_disabled_color=Color(0.875,0.875,0.875,0.5)🔗
Font color of disabled tabs.
Colorfont_hovered_color=Color(0.95,0.95,0.95,1)🔗
Font color of the currently hovered tab. Does not apply to the selected tab.
Colorfont_outline_color=Color(0,0,0,1)🔗
The tint of text outline of the tab name.
Colorfont_selected_color=Color(0.95,0.95,0.95,1)🔗
Font color of the currently selected tab.
Colorfont_unselected_color=Color(0.7,0.7,0.7,1)🔗
Font color of the other, unselected tabs.
Coloricon_disabled_color=Color(1,1,1,1)🔗
Icon color of disabled tabs.
Coloricon_hovered_color=Color(1,1,1,1)🔗
Icon color of the currently hovered tab. Does not apply to the selected tab.
Coloricon_selected_color=Color(1,1,1,1)🔗
Icon color of the currently selected tab.
Coloricon_unselected_color=Color(1,1,1,1)🔗
Icon color of the other, unselected tabs.
inticon_max_width=0🔗
The maximum allowed width of the tab's icon. This limit is applied on top of the default size of the icon, but before the value set withTabBar.set_tab_icon_max_width(). The height is adjusted according to the icon's ratio.
inticon_separation=4🔗
Space between tab's name and its icon.
intoutline_size=0🔗
The size of the tab text outline.
Note:If using a font withFontFile.multichannel_signed_distance_fieldenabled, itsFontFile.msdf_pixel_rangemust be set to at leasttwicethe value ofoutline_sizefor outline rendering to look correct. Otherwise, the outline may appear to be cut off earlier than intended.
intside_margin=8🔗
The space at the left or right edges of the tab bar, accordingly with the currenttab_alignment.
The margin is ignored withTabBar.ALIGNMENT_RIGHTif the tabs are clipped (seeclip_tabs) or a popup has been set (seeset_popup()). The margin is always ignored withTabBar.ALIGNMENT_CENTER.
inttab_separation=0🔗
The space between tabs in the tab bar.
Fontfont🔗
The font used to draw tab names.
intfont_size🔗
Font size of the tab names.
Texture2Ddecrement🔗
Icon for the left arrow button that appears when there are too many tabs to fit in the container width. When the button is disabled (i.e. the first tab is visible), it appears semi-transparent.
Texture2Ddecrement_highlight🔗
Icon for the left arrow button that appears when there are too many tabs to fit in the container width. Used when the button is being hovered with the cursor.
Texture2Ddrop_mark🔗
Icon shown to indicate where a dragged tab is gonna be dropped (seedrag_to_rearrange_enabled).
Texture2Dincrement🔗
Icon for the right arrow button that appears when there are too many tabs to fit in the container width. When the button is disabled (i.e. the last tab is visible) it appears semi-transparent.
Texture2Dincrement_highlight🔗
Icon for the right arrow button that appears when there are too many tabs to fit in the container width. Used when the button is being hovered with the cursor.
Texture2Dmenu🔗
The icon for the menu button (seeset_popup()).
Texture2Dmenu_highlight🔗
The icon for the menu button (seeset_popup()) when it's being hovered with the cursor.
StyleBoxpanel🔗
The style for the background fill.
StyleBoxtab_disabled🔗
The style of disabled tabs.
StyleBoxtab_focus🔗
StyleBoxused when theTabBaris focused. Thetab_focusStyleBoxis displayedoverthe baseStyleBoxof the selected tab, so a partially transparentStyleBoxshould be used to ensure the baseStyleBoxremains visible. AStyleBoxthat represents an outline or an underline works well for this purpose. To disable the focus visual effect, assign aStyleBoxEmptyresource. Note that disabling the focus visual effect will harm keyboard/controller navigation usability, so this is not recommended for accessibility reasons.
StyleBoxtab_hovered🔗
The style of the currently hovered tab.
Note:This style will be drawn with the same width astab_unselectedat minimum.
StyleBoxtab_selected🔗
The style of the currently selected tab.
StyleBoxtab_unselected🔗
The style of the other, unselected tabs.
StyleBoxtabbar_background🔗
The style for the background fill of theTabBararea.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
