# ItemList in English

# ItemList

Inherits:Control<CanvasItem<Node<Object
A vertical list of selectable items with one or multiple columns.

## Description

This control provides a vertical list of selectable items that may be in a single or in multiple columns, with each item having options for text and an icon. Tooltips are supported and may be different for every item in the list.
Selectable items in the list may be selected or deselected and multiple selection may be enabled. Selection with right mouse button may also be enabled to allow use of popup context menus. Items may also be "activated" by double-clicking them or by pressingEnter.
Item text only supports single-line strings. Newline characters (e.g.\n) in the string won't produce a newline. Text wrapping is enabled inICON_MODE_TOPmode, but the column's width is adjusted to fully fit its content by default. You need to setfixed_column_widthgreater than zero to wrap the text.
Allset_*methods allow negative item indices, i.e.-1to access the last item,-2to select the second-to-last item, and so on.
Incremental search:LikePopupMenuandTree,ItemListsupports searching within the list while the control is focused. Press a key that matches the first letter of an item's name to select the first item starting with the given letter. After that point, there are two ways to perform incremental search: 1) Press the same key again before the timeout duration to select the next item starting with the same letter. 2) Press letter keys that match the rest of the word before the timeout duration to match to select the item in question directly. Both of these actions will be reset to the beginning of the list if the timeout duration has passed since the last keystroke was registered. You can adjust the timeout duration by changingProjectSettings.gui/timers/incremental_search_max_interval_msec.

## Properties

| bool | allow_reselect | false |
|---|---|---|
| bool | allow_rmb_select | false |
| bool | allow_search | true |
| bool | auto_height | false |
| bool | auto_width | false |
| bool | clip_contents | true(overridesControl) |
| int | fixed_column_width | 0 |
| Vector2i | fixed_icon_size | Vector2i(0,0) |
| FocusMode | focus_mode | 2(overridesControl) |
| IconMode | icon_mode | 1 |
| float | icon_scale | 1.0 |
| int | item_count | 0 |
| int | max_columns | 1 |
| int | max_text_lines | 1 |
| bool | same_column_width | false |
| ScrollHintMode | scroll_hint_mode | 0 |
| SelectMode | select_mode | 0 |
| OverrunBehavior | text_overrun_behavior | 3 |
| bool | tile_scroll_hint | false |
| bool | wraparound_items | true |

bool
allow_reselect
false
bool
allow_rmb_select
false
bool
allow_search
true
bool
auto_height
false
bool
auto_width
false
bool
clip_contents
true(overridesControl)
fixed_column_width
Vector2i
fixed_icon_size
Vector2i(0,0)
FocusMode
focus_mode
2(overridesControl)
IconMode
icon_mode
float
icon_scale
item_count
max_columns
max_text_lines
bool
same_column_width
false
ScrollHintMode
scroll_hint_mode
SelectMode
select_mode
OverrunBehavior
text_overrun_behavior
bool
tile_scroll_hint
false
bool
wraparound_items
true

## Methods

| int | add_icon_item(icon:Texture2D, selectable:bool= true) |
|---|---|
| int | add_item(text:String, icon:Texture2D= null, selectable:bool= true) |
| void | clear() |
| void | deselect(idx:int) |
| void | deselect_all() |
| void | ensure_current_is_visible() |
| void | force_update_list_size() |
| HScrollBar | get_h_scroll_bar() |
| int | get_item_at_position(position:Vector2, exact:bool= false)const |
| AutoTranslateMode | get_item_auto_translate_mode(idx:int)const |
| Color | get_item_custom_bg_color(idx:int)const |
| Color | get_item_custom_fg_color(idx:int)const |
| Texture2D | get_item_icon(idx:int)const |
| Color | get_item_icon_modulate(idx:int)const |
| Rect2 | get_item_icon_region(idx:int)const |
| String | get_item_language(idx:int)const |
| Variant | get_item_metadata(idx:int)const |
| Rect2 | get_item_rect(idx:int, expand:bool= true)const |
| String | get_item_text(idx:int)const |
| TextDirection | get_item_text_direction(idx:int)const |
| String | get_item_tooltip(idx:int)const |
| PackedInt32Array | get_selected_items() |
| VScrollBar | get_v_scroll_bar() |
| bool | is_anything_selected() |
| bool | is_item_disabled(idx:int)const |
| bool | is_item_icon_transposed(idx:int)const |
| bool | is_item_selectable(idx:int)const |
| bool | is_item_tooltip_enabled(idx:int)const |
| bool | is_selected(idx:int)const |
| void | move_item(from_idx:int, to_idx:int) |
| void | remove_item(idx:int) |
| void | select(idx:int, single:bool= true) |
| void | set_item_auto_translate_mode(idx:int, mode:AutoTranslateMode) |
| void | set_item_custom_bg_color(idx:int, custom_bg_color:Color) |
| void | set_item_custom_fg_color(idx:int, custom_fg_color:Color) |
| void | set_item_disabled(idx:int, disabled:bool) |
| void | set_item_icon(idx:int, icon:Texture2D) |
| void | set_item_icon_modulate(idx:int, modulate:Color) |
| void | set_item_icon_region(idx:int, rect:Rect2) |
| void | set_item_icon_transposed(idx:int, transposed:bool) |
| void | set_item_language(idx:int, language:String) |
| void | set_item_metadata(idx:int, metadata:Variant) |
| void | set_item_selectable(idx:int, selectable:bool) |
| void | set_item_text(idx:int, text:String) |
| void | set_item_text_direction(idx:int, direction:TextDirection) |
| void | set_item_tooltip(idx:int, tooltip:String) |
| void | set_item_tooltip_enabled(idx:int, enable:bool) |
| void | sort_items_by_text() |

add_icon_item(icon:Texture2D, selectable:bool= true)
add_item(text:String, icon:Texture2D= null, selectable:bool= true)
void
clear()
void
deselect(idx:int)
void
deselect_all()
void
ensure_current_is_visible()
void
force_update_list_size()
HScrollBar
get_h_scroll_bar()
get_item_at_position(position:Vector2, exact:bool= false)const
AutoTranslateMode
get_item_auto_translate_mode(idx:int)const
Color
get_item_custom_bg_color(idx:int)const
Color
get_item_custom_fg_color(idx:int)const
Texture2D
get_item_icon(idx:int)const
Color
get_item_icon_modulate(idx:int)const
Rect2
get_item_icon_region(idx:int)const
String
get_item_language(idx:int)const
Variant
get_item_metadata(idx:int)const
Rect2
get_item_rect(idx:int, expand:bool= true)const
String
get_item_text(idx:int)const
TextDirection
get_item_text_direction(idx:int)const
String
get_item_tooltip(idx:int)const
PackedInt32Array
get_selected_items()
VScrollBar
get_v_scroll_bar()
bool
is_anything_selected()
bool
is_item_disabled(idx:int)const
bool
is_item_icon_transposed(idx:int)const
bool
is_item_selectable(idx:int)const
bool
is_item_tooltip_enabled(idx:int)const
bool
is_selected(idx:int)const
void
move_item(from_idx:int, to_idx:int)
void
remove_item(idx:int)
void
select(idx:int, single:bool= true)
void
set_item_auto_translate_mode(idx:int, mode:AutoTranslateMode)
void
set_item_custom_bg_color(idx:int, custom_bg_color:Color)
void
set_item_custom_fg_color(idx:int, custom_fg_color:Color)
void
set_item_disabled(idx:int, disabled:bool)
void
set_item_icon(idx:int, icon:Texture2D)
void
set_item_icon_modulate(idx:int, modulate:Color)
void
set_item_icon_region(idx:int, rect:Rect2)
void
set_item_icon_transposed(idx:int, transposed:bool)
void
set_item_language(idx:int, language:String)
void
set_item_metadata(idx:int, metadata:Variant)
void
set_item_selectable(idx:int, selectable:bool)
void
set_item_text(idx:int, text:String)
void
set_item_text_direction(idx:int, direction:TextDirection)
void
set_item_tooltip(idx:int, tooltip:String)
void
set_item_tooltip_enabled(idx:int, enable:bool)
void
sort_items_by_text()

## Theme Properties

| Color | font_color | Color(0.65,0.65,0.65,1) |
|---|---|---|
| Color | font_hovered_color | Color(0.95,0.95,0.95,1) |
| Color | font_hovered_selected_color | Color(1,1,1,1) |
| Color | font_outline_color | Color(0,0,0,1) |
| Color | font_selected_color | Color(1,1,1,1) |
| Color | guide_color | Color(0.7,0.7,0.7,0.25) |
| Color | scroll_hint_color | Color(0,0,0,1) |
| int | h_separation | 4 |
| int | icon_margin | 4 |
| int | line_separation | 2 |
| int | outline_size | 0 |
| int | v_separation | 4 |
| Font | font |  |
| int | font_size |  |
| Texture2D | scroll_hint |  |
| StyleBox | cursor |  |
| StyleBox | cursor_unfocused |  |
| StyleBox | focus |  |
| StyleBox | hovered |  |
| StyleBox | hovered_selected |  |
| StyleBox | hovered_selected_focus |  |
| StyleBox | panel |  |
| StyleBox | selected |  |
| StyleBox | selected_focus |  |

Color
font_color
Color(0.65,0.65,0.65,1)
Color
font_hovered_color
Color(0.95,0.95,0.95,1)
Color
font_hovered_selected_color
Color(1,1,1,1)
Color
font_outline_color
Color(0,0,0,1)
Color
font_selected_color
Color(1,1,1,1)
Color
guide_color
Color(0.7,0.7,0.7,0.25)
Color
scroll_hint_color
Color(0,0,0,1)
h_separation
icon_margin
line_separation
outline_size
v_separation
Font
font
font_size
Texture2D
scroll_hint
StyleBox
cursor
StyleBox
cursor_unfocused
StyleBox
focus
StyleBox
hovered
StyleBox
hovered_selected
StyleBox
hovered_selected_focus
StyleBox
panel
StyleBox
selected
StyleBox
selected_focus

## Signals

empty_clicked(at_position:Vector2, mouse_button_index:int)🔗
Emitted when any mouse click is issued within the rect of the list but on empty space.
at_positionis the click position in this control's local coordinate system.
item_activated(index:int)🔗
Emitted when specified list item is activated via double-clicking or by pressingEnter.
item_clicked(index:int, at_position:Vector2, mouse_button_index:int)🔗
Emitted when specified list item has been clicked with any mouse button.
at_positionis the click position in this control's local coordinate system.
item_selected(index:int)🔗
Emitted when specified item has been selected. Only applicable in single selection mode.
allow_reselectmust be enabled to reselect an item.
multi_selected(index:int, selected:bool)🔗
Emitted when a multiple selection is altered on a list allowing multiple selection.

## Enumerations

enumIconMode:🔗
IconModeICON_MODE_TOP=0
Icon is drawn above the text.
IconModeICON_MODE_LEFT=1
Icon is drawn to the left of the text.
enumSelectMode:🔗
SelectModeSELECT_SINGLE=0
Only allow selecting a single item.
SelectModeSELECT_MULTI=1
Allows selecting multiple items by holdingCtrlorShift.
SelectModeSELECT_TOGGLE=2
Allows selecting multiple items by toggling them on and off.
enumScrollHintMode:🔗
ScrollHintModeSCROLL_HINT_MODE_DISABLED=0
Scroll hints will never be shown.
ScrollHintModeSCROLL_HINT_MODE_BOTH=1
Scroll hints will be shown at the top and bottom.
ScrollHintModeSCROLL_HINT_MODE_TOP=2
Only the top scroll hint will be shown.
ScrollHintModeSCROLL_HINT_MODE_BOTTOM=3
Only the bottom scroll hint will be shown.

## Property Descriptions

boolallow_reselect=false🔗

- voidset_allow_reselect(value:bool)
voidset_allow_reselect(value:bool)
- boolget_allow_reselect()
boolget_allow_reselect()
Iftrue, the currently selected item can be selected again.
boolallow_rmb_select=false🔗
- voidset_allow_rmb_select(value:bool)
voidset_allow_rmb_select(value:bool)
- boolget_allow_rmb_select()
boolget_allow_rmb_select()
Iftrue, right mouse button click can select items.
boolallow_search=true🔗
- voidset_allow_search(value:bool)
voidset_allow_search(value:bool)
- boolget_allow_search()
boolget_allow_search()
Iftrue, allows navigating theItemListwith letter keys through incremental search.
boolauto_height=false🔗
- voidset_auto_height(value:bool)
voidset_auto_height(value:bool)
- boolhas_auto_height()
boolhas_auto_height()
Iftrue, the control will automatically resize the height to fit its content.
boolauto_width=false🔗
- voidset_auto_width(value:bool)
voidset_auto_width(value:bool)
- boolhas_auto_width()
boolhas_auto_width()
Iftrue, the control will automatically resize the width to fit its content.
intfixed_column_width=0🔗
- voidset_fixed_column_width(value:int)
voidset_fixed_column_width(value:int)
- intget_fixed_column_width()
intget_fixed_column_width()
The width all columns will be adjusted to.
A value of zero disables the adjustment, each item will have a width equal to the width of its content and the columns will have an uneven width.
Vector2ifixed_icon_size=Vector2i(0,0)🔗
- voidset_fixed_icon_size(value:Vector2i)
voidset_fixed_icon_size(value:Vector2i)
- Vector2iget_fixed_icon_size()
Vector2iget_fixed_icon_size()
The size all icons will be adjusted to.
If either X or Y component is not greater than zero, icon size won't be affected.
IconModeicon_mode=1🔗
- voidset_icon_mode(value:IconMode)
voidset_icon_mode(value:IconMode)
- IconModeget_icon_mode()
IconModeget_icon_mode()
The icon position, whether above or to the left of the text. See theIconModeconstants.
floaticon_scale=1.0🔗
- voidset_icon_scale(value:float)
voidset_icon_scale(value:float)
- floatget_icon_scale()
floatget_icon_scale()
The scale of icon applied afterfixed_icon_sizeand transposing takes effect.
intitem_count=0🔗
- voidset_item_count(value:int)
voidset_item_count(value:int)
- intget_item_count()
intget_item_count()
The number of items currently in the list.
intmax_columns=1🔗
- voidset_max_columns(value:int)
voidset_max_columns(value:int)
- intget_max_columns()
intget_max_columns()
Maximum columns the list will have.
If greater than zero, the content will be split among the specified columns.
A value of zero means unlimited columns, i.e. all items will be put in the same row.
intmax_text_lines=1🔗
- voidset_max_text_lines(value:int)
voidset_max_text_lines(value:int)
- intget_max_text_lines()
intget_max_text_lines()
Maximum lines of text allowed in each item. Space will be reserved even when there is not enough lines of text to display.
Note:This property takes effect only whenicon_modeisICON_MODE_TOP. To make the text wrap,fixed_column_widthshould be greater than zero.
boolsame_column_width=false🔗
- voidset_same_column_width(value:bool)
voidset_same_column_width(value:bool)
- boolis_same_column_width()
boolis_same_column_width()
Whether all columns will have the same width.
Iftrue, the width is equal to the largest column width of all columns.
ScrollHintModescroll_hint_mode=0🔗
- voidset_scroll_hint_mode(value:ScrollHintMode)
voidset_scroll_hint_mode(value:ScrollHintMode)
- ScrollHintModeget_scroll_hint_mode()
ScrollHintModeget_scroll_hint_mode()
The way which scroll hints (indicators that show that the content can still be scrolled in a certain direction) will be shown.
SelectModeselect_mode=0🔗
- voidset_select_mode(value:SelectMode)
voidset_select_mode(value:SelectMode)
- SelectModeget_select_mode()
SelectModeget_select_mode()
Allows single or multiple item selection. See theSelectModeconstants.
OverrunBehaviortext_overrun_behavior=3🔗
- voidset_text_overrun_behavior(value:OverrunBehavior)
voidset_text_overrun_behavior(value:OverrunBehavior)
- OverrunBehaviorget_text_overrun_behavior()
OverrunBehaviorget_text_overrun_behavior()
The clipping behavior when the text exceeds an item's bounding rectangle.
booltile_scroll_hint=false🔗
- voidset_tile_scroll_hint(value:bool)
voidset_tile_scroll_hint(value:bool)
- boolis_scroll_hint_tiled()
boolis_scroll_hint_tiled()
Iftrue, the scroll hint texture will be tiled instead of stretched. Seescroll_hint_mode.
boolwraparound_items=true🔗
- voidset_wraparound_items(value:bool)
voidset_wraparound_items(value:bool)
- boolhas_wraparound_items()
boolhas_wraparound_items()
Iftrue, the control will automatically move items into a new row to fit its content. See alsoHFlowContainerfor this behavior.
Iffalse, the control will add a horizontal scrollbar to make all items visible.

## Method Descriptions

intadd_icon_item(icon:Texture2D, selectable:bool= true)🔗
Adds an item to the item list with no text, only an icon. Returns the index of an added item.
intadd_item(text:String, icon:Texture2D= null, selectable:bool= true)🔗
Adds an item to the item list with specified text. Returns the index of an added item.
Specify anicon, or usenullas theiconfor a list item with no icon.
Ifselectableistrue, the list item will be selectable.
voidclear()🔗
Removes all items from the list.
voiddeselect(idx:int)🔗
Ensures the item associated with the specified index is not selected.
voiddeselect_all()🔗
Ensures there are no items selected.
voidensure_current_is_visible()🔗
Ensure current selection is visible, adjusting the scroll position as necessary.
voidforce_update_list_size()🔗
Forces an update to the list size based on its items. This happens automatically whenever size of the items, or other relevant settings likeauto_height, change. The method can be used to trigger the update ahead of next drawing pass.
HScrollBarget_h_scroll_bar()🔗
Returns the horizontal scrollbar.
Warning:This is a required internal node, removing and freeing it may cause a crash. If you wish to hide it or any of its children, use theirCanvasItem.visibleproperty.
intget_item_at_position(position:Vector2, exact:bool= false)const🔗
Returns the item index at the givenposition.
When there is no item at that point, -1 will be returned ifexactistrue, and the closest item index will be returned otherwise.
Note:The returned value is unreliable if called right after modifying theItemList, before it redraws in the next frame.
AutoTranslateModeget_item_auto_translate_mode(idx:int)const🔗
Returns item's auto translate mode.
Colorget_item_custom_bg_color(idx:int)const🔗
Returns the custom background color of the item specified byidxindex.
Colorget_item_custom_fg_color(idx:int)const🔗
Returns the custom foreground color of the item specified byidxindex.
Texture2Dget_item_icon(idx:int)const🔗
Returns the icon associated with the specified index.
Colorget_item_icon_modulate(idx:int)const🔗
Returns aColormodulating item's icon at the specified index.
Rect2get_item_icon_region(idx:int)const🔗
Returns the region of item's icon used. The whole icon will be used if the region has no area.
Stringget_item_language(idx:int)const🔗
Returns item's text language code.
Variantget_item_metadata(idx:int)const🔗
Returns the metadata value of the specified index.
Rect2get_item_rect(idx:int, expand:bool= true)const🔗
Returns the position and size of the item with the specified index, in the coordinate system of theItemListnode. Ifexpandistruethe last column expands to fill the rest of the row.
Note:The returned value is unreliable if called right after modifying theItemList, before it redraws in the next frame.
Stringget_item_text(idx:int)const🔗
Returns the text associated with the specified index.
TextDirectionget_item_text_direction(idx:int)const🔗
Returns item's text base writing direction.
Stringget_item_tooltip(idx:int)const🔗
Returns the tooltip hint associated with the specified index.
PackedInt32Arrayget_selected_items()🔗
Returns an array with the indexes of the selected items.
VScrollBarget_v_scroll_bar()🔗
Returns the vertical scrollbar.
Warning:This is a required internal node, removing and freeing it may cause a crash. If you wish to hide it or any of its children, use theirCanvasItem.visibleproperty.
boolis_anything_selected()🔗
Returnstrueif one or more items are selected.
boolis_item_disabled(idx:int)const🔗
Returnstrueif the item at the specified index is disabled.
boolis_item_icon_transposed(idx:int)const🔗
Returnstrueif the item icon will be drawn transposed, i.e. the X and Y axes are swapped.
boolis_item_selectable(idx:int)const🔗
Returnstrueif the item at the specified index is selectable.
boolis_item_tooltip_enabled(idx:int)const🔗
Returnstrueif the tooltip is enabled for specified item index.
boolis_selected(idx:int)const🔗
Returnstrueif the item at the specified index is currently selected.
voidmove_item(from_idx:int, to_idx:int)🔗
Moves item from indexfrom_idxtoto_idx.
voidremove_item(idx:int)🔗
Removes the item specified byidxindex from the list.
voidselect(idx:int, single:bool= true)🔗
Select the item at the specified index.
Note:This method does not trigger the item selection signal.
voidset_item_auto_translate_mode(idx:int, mode:AutoTranslateMode)🔗
Sets the auto translate mode of the item associated with the specified index.
Items useNode.AUTO_TRANSLATE_MODE_INHERITby default, which uses the same auto translate mode as theItemListitself.
voidset_item_custom_bg_color(idx:int, custom_bg_color:Color)🔗
Sets the background color of the item specified byidxindex to the specifiedColor.
voidset_item_custom_fg_color(idx:int, custom_fg_color:Color)🔗
Sets the foreground color of the item specified byidxindex to the specifiedColor.
voidset_item_disabled(idx:int, disabled:bool)🔗
Disables (or enables) the item at the specified index.
Disabled items cannot be selected and do not trigger activation signals (when double-clicking or pressingEnter).
voidset_item_icon(idx:int, icon:Texture2D)🔗
Sets (or replaces) the icon'sTexture2Dassociated with the specified index.
voidset_item_icon_modulate(idx:int, modulate:Color)🔗
Sets a modulatingColorof the item associated with the specified index.
voidset_item_icon_region(idx:int, rect:Rect2)🔗
Sets the region of item's icon used. The whole icon will be used if the region has no area.
voidset_item_icon_transposed(idx:int, transposed:bool)🔗
Sets whether the item icon will be drawn transposed.
voidset_item_language(idx:int, language:String)🔗
Sets the language code of the text for the item at the given index tolanguage. This is used for line-breaking and text shaping algorithms. Iflanguageis empty, the current locale is used.
voidset_item_metadata(idx:int, metadata:Variant)🔗
Sets a value (of any type) to be stored with the item associated with the specified index.
voidset_item_selectable(idx:int, selectable:bool)🔗
Allows or disallows selection of the item associated with the specified index.
voidset_item_text(idx:int, text:String)🔗
Sets text of the item associated with the specified index.
voidset_item_text_direction(idx:int, direction:TextDirection)🔗
Sets item's text base writing direction.
voidset_item_tooltip(idx:int, tooltip:String)🔗
Sets the tooltip hint for the item associated with the specified index.
voidset_item_tooltip_enabled(idx:int, enable:bool)🔗
Sets whether the tooltip hint is enabled for specified item index.
voidsort_items_by_text()🔗
Sorts items in the list by their text.

## Theme Property Descriptions

Colorfont_color=Color(0.65,0.65,0.65,1)🔗
Default textColorof the item.
Colorfont_hovered_color=Color(0.95,0.95,0.95,1)🔗
TextColorused when the item is hovered and not selected yet.
Colorfont_hovered_selected_color=Color(1,1,1,1)🔗
TextColorused when the item is hovered and selected.
Colorfont_outline_color=Color(0,0,0,1)🔗
The tint of text outline of the item.
Colorfont_selected_color=Color(1,1,1,1)🔗
TextColorused when the item is selected, but not hovered.
Colorguide_color=Color(0.7,0.7,0.7,0.25)🔗
Colorof the guideline. The guideline is a line drawn between each row of items.
Colorscroll_hint_color=Color(0,0,0,1)🔗
Colorused to modulate thescroll_hinttexture.
inth_separation=4🔗
The horizontal spacing between items.
inticon_margin=4🔗
The spacing between item's icon and text.
intline_separation=2🔗
The vertical spacing between each line of text.
intoutline_size=0🔗
The size of the item text outline.
Note:If using a font withFontFile.multichannel_signed_distance_fieldenabled, itsFontFile.msdf_pixel_rangemust be set to at leasttwicethe value ofoutline_sizefor outline rendering to look correct. Otherwise, the outline may appear to be cut off earlier than intended.
intv_separation=4🔗
The vertical spacing between items.
Fontfont🔗
Fontof the item's text.
intfont_size🔗
Font size of the item's text.
Texture2Dscroll_hint🔗
The indicator that will be shown when the content can still be scrolled. Seescroll_hint_mode.
StyleBoxcursor🔗
StyleBoxused for the cursor, when theItemListis being focused.
StyleBoxcursor_unfocused🔗
StyleBoxused for the cursor, when theItemListis not being focused.
StyleBoxfocus🔗
The focused style for theItemList, drawn on top of everything.
StyleBoxhovered🔗
StyleBoxfor the hovered, but not selected items.
StyleBoxhovered_selected🔗
StyleBoxfor the hovered and selected items, used when theItemListis not being focused.
StyleBoxhovered_selected_focus🔗
StyleBoxfor the hovered and selected items, used when theItemListis being focused.
StyleBoxpanel🔗
The background style for theItemList.
StyleBoxselected🔗
StyleBoxfor the selected items, used when theItemListis not being focused.
StyleBoxselected_focus🔗
StyleBoxfor the selected items, used when theItemListis being focused.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
