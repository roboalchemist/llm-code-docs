# Tree in English

# Tree
Inherits:Control<CanvasItem<Node<Object
A control used to show a set of internalTreeItems in a hierarchical structure.

## Description
A control used to show a set of internalTreeItems in a hierarchical structure. The tree items can be selected, expanded and collapsed. The tree can have multiple columns with custom controls likeLineEdits, buttons and popups. It can be useful for structured displays and interactions.
Trees are built via code, usingTreeItemobjects to create the structure. They have a single root, but multiple roots can be simulated withhide_root:
```
func _ready():
    var tree = Tree.new()
    var root = tree.create_item()
    tree.hide_root = true
    var child1 = tree.create_item(root)
    var child2 = tree.create_item(root)
    var subchild1 = tree.create_item(child1)
    subchild1.set_text(0, "Subchild1")
```
```
public override void _Ready()
{
    var tree = new Tree();
    TreeItem root = tree.CreateItem();
    tree.HideRoot = true;
    TreeItem child1 = tree.CreateItem(root);
    TreeItem child2 = tree.CreateItem(root);
    TreeItem subchild1 = tree.CreateItem(child1);
    subchild1.SetText(0, "Subchild1");
}
```
To iterate over all theTreeItemobjects in aTreeobject, useTreeItem.get_next()andTreeItem.get_first_child()after getting the root throughget_root(). You can useObject.free()on aTreeItemto remove it from theTree.
Incremental search:LikeItemListandPopupMenu,Treesupports searching within the list while the control is focused. Press a key that matches the first letter of an item's name to select the first item starting with the given letter. After that point, there are two ways to perform incremental search: 1) Press the same key again before the timeout duration to select the next item starting with the same letter. 2) Press letter keys that match the rest of the word before the timeout duration to match to select the item in question directly. Both of these actions will be reset to the beginning of the list if the timeout duration has passed since the last keystroke was registered. You can adjust the timeout duration by changingProjectSettings.gui/timers/incremental_search_max_interval_msec.

## Properties

| bool | allow_reselect | false |
|---|---|---|
| bool | allow_rmb_select | false |
| bool | allow_search | true |
| bool | auto_tooltip | true |
| bool | clip_contents | true(overridesControl) |
| bool | column_titles_visible | false |
| int | columns | 1 |
| int | drop_mode_flags | 0 |
| bool | enable_drag_unfolding | true |
| bool | enable_recursive_folding | true |
| FocusMode | focus_mode | 2(overridesControl) |
| bool | hide_folding | false |
| bool | hide_root | false |
| ScrollHintMode | scroll_hint_mode | 0 |
| bool | scroll_horizontal_enabled | true |
| bool | scroll_vertical_enabled | true |
| SelectMode | select_mode | 0 |
| bool | tile_scroll_hint | false |

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
auto_tooltip
true
bool
clip_contents
true(overridesControl)
bool
column_titles_visible
false
columns
drop_mode_flags
bool
enable_drag_unfolding
true
bool
enable_recursive_folding
true
FocusMode
focus_mode
2(overridesControl)
bool
hide_folding
false
bool
hide_root
false
ScrollHintMode
scroll_hint_mode
bool
scroll_horizontal_enabled
true
bool
scroll_vertical_enabled
true
SelectMode
select_mode
bool
tile_scroll_hint
false

## Methods

| void | clear() |
|---|---|
| TreeItem | create_item(parent:TreeItem= null, index:int= -1) |
| void | deselect_all() |
| bool | edit_selected(force_edit:bool= false) |
| void | ensure_cursor_is_visible() |
| int | get_button_id_at_position(position:Vector2)const |
| int | get_column_at_position(position:Vector2)const |
| int | get_column_expand_ratio(column:int)const |
| String | get_column_title(column:int)const |
| HorizontalAlignment | get_column_title_alignment(column:int)const |
| TextDirection | get_column_title_direction(column:int)const |
| String | get_column_title_language(column:int)const |
| String | get_column_title_tooltip_text(column:int)const |
| int | get_column_width(column:int)const |
| Rect2 | get_custom_popup_rect()const |
| int | get_drop_section_at_position(position:Vector2)const |
| TreeItem | get_edited()const |
| int | get_edited_column()const |
| Rect2 | get_item_area_rect(item:TreeItem, column:int= -1, button_index:int= -1)const |
| TreeItem | get_item_at_position(position:Vector2)const |
| TreeItem | get_next_selected(from:TreeItem) |
| int | get_pressed_button()const |
| TreeItem | get_root()const |
| Vector2 | get_scroll()const |
| TreeItem | get_selected()const |
| int | get_selected_column()const |
| bool | is_column_clipping_content(column:int)const |
| bool | is_column_expanding(column:int)const |
| void | scroll_to_item(item:TreeItem, center_on_item:bool= false) |
| void | set_column_clip_content(column:int, enable:bool) |
| void | set_column_custom_minimum_width(column:int, min_width:int) |
| void | set_column_expand(column:int, expand:bool) |
| void | set_column_expand_ratio(column:int, ratio:int) |
| void | set_column_title(column:int, title:String) |
| void | set_column_title_alignment(column:int, title_alignment:HorizontalAlignment) |
| void | set_column_title_direction(column:int, direction:TextDirection) |
| void | set_column_title_language(column:int, language:String) |
| void | set_column_title_tooltip_text(column:int, tooltip_text:String) |
| void | set_selected(item:TreeItem, column:int) |

void
clear()
TreeItem
create_item(parent:TreeItem= null, index:int= -1)
void
deselect_all()
bool
edit_selected(force_edit:bool= false)
void
ensure_cursor_is_visible()
get_button_id_at_position(position:Vector2)const
get_column_at_position(position:Vector2)const
get_column_expand_ratio(column:int)const
String
get_column_title(column:int)const
HorizontalAlignment
get_column_title_alignment(column:int)const
TextDirection
get_column_title_direction(column:int)const
String
get_column_title_language(column:int)const
String
get_column_title_tooltip_text(column:int)const
get_column_width(column:int)const
Rect2
get_custom_popup_rect()const
get_drop_section_at_position(position:Vector2)const
TreeItem
get_edited()const
get_edited_column()const
Rect2
get_item_area_rect(item:TreeItem, column:int= -1, button_index:int= -1)const
TreeItem
get_item_at_position(position:Vector2)const
TreeItem
get_next_selected(from:TreeItem)
get_pressed_button()const
TreeItem
get_root()const
Vector2
get_scroll()const
TreeItem
get_selected()const
get_selected_column()const
bool
is_column_clipping_content(column:int)const
bool
is_column_expanding(column:int)const
void
scroll_to_item(item:TreeItem, center_on_item:bool= false)
void
set_column_clip_content(column:int, enable:bool)
void
set_column_custom_minimum_width(column:int, min_width:int)
void
set_column_expand(column:int, expand:bool)
void
set_column_expand_ratio(column:int, ratio:int)
void
set_column_title(column:int, title:String)
void
set_column_title_alignment(column:int, title_alignment:HorizontalAlignment)
void
set_column_title_direction(column:int, direction:TextDirection)
void
set_column_title_language(column:int, language:String)
void
set_column_title_tooltip_text(column:int, tooltip_text:String)
void
set_selected(item:TreeItem, column:int)

## Theme Properties

| Color | children_hl_line_color | Color(0.27,0.27,0.27,1) |
|---|---|---|
| Color | custom_button_font_highlight | Color(0.95,0.95,0.95,1) |
| Color | drop_position_color | Color(1,1,1,1) |
| Color | font_color | Color(0.7,0.7,0.7,1) |
| Color | font_disabled_color | Color(0.875,0.875,0.875,0.5) |
| Color | font_hovered_color | Color(0.95,0.95,0.95,1) |
| Color | font_hovered_dimmed_color | Color(0.875,0.875,0.875,1) |
| Color | font_hovered_selected_color | Color(1,1,1,1) |
| Color | font_outline_color | Color(0,0,0,1) |
| Color | font_selected_color | Color(1,1,1,1) |
| Color | guide_color | Color(0.7,0.7,0.7,0.25) |
| Color | parent_hl_line_color | Color(0.27,0.27,0.27,1) |
| Color | relationship_line_color | Color(0.27,0.27,0.27,1) |
| Color | scroll_hint_color | Color(0,0,0,1) |
| Color | title_button_color | Color(0.875,0.875,0.875,1) |
| int | button_margin | 4 |
| int | check_h_separation | 4 |
| int | children_hl_line_width | 1 |
| int | dragging_unfold_wait_msec | 500 |
| int | draw_guides | 1 |
| int | draw_relationship_lines | 0 |
| int | h_separation | 4 |
| int | icon_h_separation | 4 |
| int | icon_max_width | 0 |
| int | inner_item_margin_bottom | 0 |
| int | inner_item_margin_left | 0 |
| int | inner_item_margin_right | 0 |
| int | inner_item_margin_top | 0 |
| int | item_margin | 16 |
| int | outline_size | 0 |
| int | parent_hl_line_margin | 0 |
| int | parent_hl_line_width | 1 |
| int | relationship_line_width | 1 |
| int | scroll_border | 4 |
| int | scroll_speed | 12 |
| int | scrollbar_h_separation | 4 |
| int | scrollbar_margin_bottom | -1 |
| int | scrollbar_margin_left | -1 |
| int | scrollbar_margin_right | -1 |
| int | scrollbar_margin_top | -1 |
| int | scrollbar_v_separation | 4 |
| int | v_separation | 4 |
| Font | font |  |
| Font | title_button_font |  |
| int | font_size |  |
| int | title_button_font_size |  |
| Texture2D | arrow |  |
| Texture2D | arrow_collapsed |  |
| Texture2D | arrow_collapsed_mirrored |  |
| Texture2D | checked |  |
| Texture2D | checked_disabled |  |
| Texture2D | indeterminate |  |
| Texture2D | indeterminate_disabled |  |
| Texture2D | scroll_hint |  |
| Texture2D | select_arrow |  |
| Texture2D | unchecked |  |
| Texture2D | unchecked_disabled |  |
| Texture2D | updown |  |
| StyleBox | button_hover |  |
| StyleBox | button_pressed |  |
| StyleBox | cursor |  |
| StyleBox | cursor_unfocused |  |
| StyleBox | custom_button |  |
| StyleBox | custom_button_hover |  |
| StyleBox | custom_button_pressed |  |
| StyleBox | focus |  |
| StyleBox | hovered |  |
| StyleBox | hovered_dimmed |  |
| StyleBox | hovered_selected |  |
| StyleBox | hovered_selected_focus |  |
| StyleBox | panel |  |
| StyleBox | selected |  |
| StyleBox | selected_focus |  |
| StyleBox | title_button_hover |  |
| StyleBox | title_button_normal |  |
| StyleBox | title_button_pressed |  |

Color
children_hl_line_color
Color(0.27,0.27,0.27,1)
Color
custom_button_font_highlight
Color(0.95,0.95,0.95,1)
Color
drop_position_color
Color(1,1,1,1)
Color
font_color
Color(0.7,0.7,0.7,1)
Color
font_disabled_color
Color(0.875,0.875,0.875,0.5)
Color
font_hovered_color
Color(0.95,0.95,0.95,1)
Color
font_hovered_dimmed_color
Color(0.875,0.875,0.875,1)
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
parent_hl_line_color
Color(0.27,0.27,0.27,1)
Color
relationship_line_color
Color(0.27,0.27,0.27,1)
Color
scroll_hint_color
Color(0,0,0,1)
Color
title_button_color
Color(0.875,0.875,0.875,1)
button_margin
check_h_separation
children_hl_line_width
dragging_unfold_wait_msec
draw_guides
draw_relationship_lines
h_separation
icon_h_separation
icon_max_width
inner_item_margin_bottom
inner_item_margin_left
inner_item_margin_right
inner_item_margin_top
item_margin
outline_size
parent_hl_line_margin
parent_hl_line_width
relationship_line_width
scroll_border
scroll_speed
scrollbar_h_separation
scrollbar_margin_bottom
scrollbar_margin_left
scrollbar_margin_right
scrollbar_margin_top
scrollbar_v_separation
v_separation
Font
font
Font
title_button_font
font_size
title_button_font_size
Texture2D
arrow
Texture2D
arrow_collapsed
Texture2D
arrow_collapsed_mirrored
Texture2D
checked
Texture2D
checked_disabled
Texture2D
indeterminate
Texture2D
indeterminate_disabled
Texture2D
scroll_hint
Texture2D
select_arrow
Texture2D
unchecked
Texture2D
unchecked_disabled
Texture2D
updown
StyleBox
button_hover
StyleBox
button_pressed
StyleBox
cursor
StyleBox
cursor_unfocused
StyleBox
custom_button
StyleBox
custom_button_hover
StyleBox
custom_button_pressed
StyleBox
focus
StyleBox
hovered
StyleBox
hovered_dimmed
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
StyleBox
title_button_hover
StyleBox
title_button_normal
StyleBox
title_button_pressed

## Signals
button_clicked(item:TreeItem, column:int, id:int, mouse_button_index:int)🔗
Emitted when a button on the tree was pressed (seeTreeItem.add_button()).
cell_selected()🔗
Emitted when a cell is selected.
check_propagated_to_item(item:TreeItem, column:int)🔗
Emitted whenTreeItem.propagate_check()is called. Connect to this signal to process the items that are affected whenTreeItem.propagate_check()is invoked. The order that the items affected will be processed is as follows: the item that invoked the method, children of that item, and finally parents of that item.
column_title_clicked(column:int, mouse_button_index:int)🔗
Emitted when a column's title is clicked with either@GlobalScope.MOUSE_BUTTON_LEFTor@GlobalScope.MOUSE_BUTTON_RIGHT.
custom_item_clicked(mouse_button_index:int)🔗
Emitted when an item withTreeItem.CELL_MODE_CUSTOMis clicked with a mouse button.
custom_popup_edited(arrow_clicked:bool)🔗
Emitted when a cell with theTreeItem.CELL_MODE_CUSTOMis clicked to be edited.
empty_clicked(click_position:Vector2, mouse_button_index:int)🔗
Emitted when a mouse button is clicked in the empty space of the tree.
item_activated()🔗
Emitted when an item is double-clicked, or selected with aui_acceptinput event (e.g. usingEnterorSpaceon the keyboard).
item_collapsed(item:TreeItem)🔗
Emitted when an item is expanded or collapsed by clicking on the folding arrow or through code.
Note:Despite its name, this signal is also emitted when an item is expanded.
item_edited()🔗
Emitted when an item is edited.
item_icon_double_clicked()🔗
Emitted when an item's icon is double-clicked. For a signal that emits when any part of the item is double-clicked, seeitem_activated.
item_mouse_selected(mouse_position:Vector2, mouse_button_index:int)🔗
Emitted when an item is selected with a mouse button.
item_selected()🔗
Emitted when an item is selected.
multi_selected(item:TreeItem, column:int, selected:bool)🔗
Emitted instead ofitem_selectedifselect_modeis set toSELECT_MULTI.
nothing_selected()🔗
Emitted when a left mouse button click does not select any item.

## Enumerations
enumSelectMode:🔗
SelectModeSELECT_SINGLE=0
Allows selection of a single cell at a time. From the perspective of items, only a single item is allowed to be selected. And there is only one column selected in the selected item.
The focus cursor is always hidden in this mode, but it is positioned at the current selection, making the currently selected item the currently focused item.
SelectModeSELECT_ROW=1
Allows selection of a single row at a time. From the perspective of items, only a single items is allowed to be selected. And all the columns are selected in the selected item.
The focus cursor is always hidden in this mode, but it is positioned at the first column of the current selection, making the currently selected item the currently focused item.
SelectModeSELECT_MULTI=2
Allows selection of multiple cells at the same time. From the perspective of items, multiple items are allowed to be selected. And there can be multiple columns selected in each selected item.
The focus cursor is visible in this mode, the item or column under the cursor is not necessarily selected.
enumDropModeFlags:🔗
DropModeFlagsDROP_MODE_DISABLED=0
Disables all drop sections, but still allows to detect the "on item" drop section byget_drop_section_at_position().
Note:This is the default flag, it has no effect when combined with other flags.
DropModeFlagsDROP_MODE_ON_ITEM=1
Enables the "on item" drop section. This drop section covers the entire item.
When combined withDROP_MODE_INBETWEEN, this drop section halves the height and stays centered vertically.
DropModeFlagsDROP_MODE_INBETWEEN=2
Enables "above item" and "below item" drop sections. The "above item" drop section covers the top half of the item, and the "below item" drop section covers the bottom half.
When combined withDROP_MODE_ON_ITEM, these drop sections halves the height and stays on top / bottom accordingly.
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
Iftrue, the currently selected cell may be selected again.
boolallow_rmb_select=false🔗
- voidset_allow_rmb_select(value:bool)
voidset_allow_rmb_select(value:bool)
- boolget_allow_rmb_select()
boolget_allow_rmb_select()
Iftrue, a right mouse button click can select items.
boolallow_search=true🔗
- voidset_allow_search(value:bool)
voidset_allow_search(value:bool)
- boolget_allow_search()
boolget_allow_search()
Iftrue, allows navigating theTreewith letter keys through incremental search.
boolauto_tooltip=true🔗
- voidset_auto_tooltip(value:bool)
voidset_auto_tooltip(value:bool)
- boolis_auto_tooltip_enabled()
boolis_auto_tooltip_enabled()
Iftrue, tree items with no tooltip assigned display their text as their tooltip. See alsoTreeItem.get_tooltip_text()andTreeItem.get_button_tooltip_text().
boolcolumn_titles_visible=false🔗
- voidset_column_titles_visible(value:bool)
voidset_column_titles_visible(value:bool)
- boolare_column_titles_visible()
boolare_column_titles_visible()
Iftrue, column titles are visible.
intcolumns=1🔗
- voidset_columns(value:int)
voidset_columns(value:int)
- intget_columns()
intget_columns()
The number of columns.
intdrop_mode_flags=0🔗
- voidset_drop_mode_flags(value:int)
voidset_drop_mode_flags(value:int)
- intget_drop_mode_flags()
intget_drop_mode_flags()
The drop mode as an OR combination of flags. SeeDropModeFlagsconstants. Once dropping is done, reverts toDROP_MODE_DISABLED. Setting this duringControl._can_drop_data()is recommended.
This controls the drop sections, i.e. the decision and drawing of possible drop locations based on the mouse position.
boolenable_drag_unfolding=true🔗
- voidset_enable_drag_unfolding(value:bool)
voidset_enable_drag_unfolding(value:bool)
- boolis_drag_unfolding_enabled()
boolis_drag_unfolding_enabled()
Iftrue, tree items will unfold when hovered over during a drag-and-drop. The delay for when this happens is dictated bydragging_unfold_wait_msec.
boolenable_recursive_folding=true🔗
- voidset_enable_recursive_folding(value:bool)
voidset_enable_recursive_folding(value:bool)
- boolis_recursive_folding_enabled()
boolis_recursive_folding_enabled()
Iftrue, recursive folding is enabled for thisTree. Holding downShiftwhile clicking the fold arrow or usingui_right/ui_leftshortcuts collapses or uncollapses theTreeItemand all its descendants.
boolhide_folding=false🔗
- voidset_hide_folding(value:bool)
voidset_hide_folding(value:bool)
- boolis_folding_hidden()
boolis_folding_hidden()
Iftrue, the folding arrow is hidden.
boolhide_root=false🔗
- voidset_hide_root(value:bool)
voidset_hide_root(value:bool)
- boolis_root_hidden()
boolis_root_hidden()
Iftrue, the tree's root is hidden.
ScrollHintModescroll_hint_mode=0🔗
- voidset_scroll_hint_mode(value:ScrollHintMode)
voidset_scroll_hint_mode(value:ScrollHintMode)
- ScrollHintModeget_scroll_hint_mode()
ScrollHintModeget_scroll_hint_mode()
The way which scroll hints (indicators that show that the content can still be scrolled in a certain direction) will be shown.
boolscroll_horizontal_enabled=true🔗
- voidset_h_scroll_enabled(value:bool)
voidset_h_scroll_enabled(value:bool)
- boolis_h_scroll_enabled()
boolis_h_scroll_enabled()
Iftrue, enables horizontal scrolling.
boolscroll_vertical_enabled=true🔗
- voidset_v_scroll_enabled(value:bool)
voidset_v_scroll_enabled(value:bool)
- boolis_v_scroll_enabled()
boolis_v_scroll_enabled()
Iftrue, enables vertical scrolling.
SelectModeselect_mode=0🔗
- voidset_select_mode(value:SelectMode)
voidset_select_mode(value:SelectMode)
- SelectModeget_select_mode()
SelectModeget_select_mode()
Allows single or multiple selection. See theSelectModeconstants.
booltile_scroll_hint=false🔗
- voidset_tile_scroll_hint(value:bool)
voidset_tile_scroll_hint(value:bool)
- boolis_scroll_hint_tiled()
boolis_scroll_hint_tiled()
Iftrue, the scroll hint texture will be tiled instead of stretched. Seescroll_hint_mode.

## Method Descriptions
voidclear()🔗
Clears the tree. This removes all items.
TreeItemcreate_item(parent:TreeItem= null, index:int= -1)🔗
Creates an item in the tree and adds it as a child ofparent, which can be either a validTreeItemornull.
Ifparentisnull, the root item will be the parent, or the new item will be the root itself if the tree is empty.
The new item will be theindex-th child of parent, or it will be the last child if there are not enough siblings.
voiddeselect_all()🔗
Deselects all tree items (rows and columns). InSELECT_MULTImode also removes selection cursor.
booledit_selected(force_edit:bool= false)🔗
Edits the selected tree item as if it was clicked.
Either the item must be set editable withTreeItem.set_editable()orforce_editmust betrue.
Returnstrueif the item could be edited. Fails if no item is selected.
voidensure_cursor_is_visible()🔗
Makes the currently focused cell visible.
This will scroll the tree if necessary. InSELECT_ROWmode, this will not do horizontal scrolling, as all the cells in the selected row is focused logically.
Note:Despite the name of this method, the focus cursor itself is only visible inSELECT_MULTImode.
intget_button_id_at_position(position:Vector2)const🔗
Returns the button ID atposition, or -1 if no button is there.
intget_column_at_position(position:Vector2)const🔗
Returns the column index atposition, or -1 if no item is there.
intget_column_expand_ratio(column:int)const🔗
Returns the expand ratio assigned to the column.
Stringget_column_title(column:int)const🔗
Returns the column's title.
HorizontalAlignmentget_column_title_alignment(column:int)const🔗
Returns the column title alignment.
TextDirectionget_column_title_direction(column:int)const🔗
Returns column title base writing direction.
Stringget_column_title_language(column:int)const🔗
Returns column title language code.
Stringget_column_title_tooltip_text(column:int)const🔗
Returns the column title's tooltip text.
intget_column_width(column:int)const🔗
Returns the column's width in pixels.
Rect2get_custom_popup_rect()const🔗
Returns the rectangle for custom popups. Helper to create custom cell controls that display a popup. SeeTreeItem.set_cell_mode().
intget_drop_section_at_position(position:Vector2)const🔗
Returns the drop section atposition, or -100 if no item is there.
Values -1, 0, or 1 will be returned for the "above item", "on item", and "below item" drop sections, respectively. SeeDropModeFlagsfor a description of each drop section.
To get the item which the returned drop section is relative to, useget_item_at_position().
TreeItemget_edited()const🔗
Returns the currently edited item. Can be used withitem_editedto get the item that was modified.
```
func _ready():
    $Tree.item_edited.connect(on_Tree_item_edited)

func on_Tree_item_edited():
    print($Tree.get_edited()) # This item just got edited (e.g. checked).
```
```
public override void _Ready()
{
    GetNode<Tree>("Tree").ItemEdited += OnTreeItemEdited;
}

public void OnTreeItemEdited()
{
    GD.Print(GetNode<Tree>("Tree").GetEdited()); // This item just got edited (e.g. checked).
}
```
intget_edited_column()const🔗
Returns the column for the currently edited item.
Rect2get_item_area_rect(item:TreeItem, column:int= -1, button_index:int= -1)const🔗
Returns the rectangle area for the specifiedTreeItem. Ifcolumnis specified, only get the position and size of that column, otherwise get the rectangle containing all columns. If a button index is specified, the rectangle of that button will be returned.
TreeItemget_item_at_position(position:Vector2)const🔗
Returns the tree item at the specified position (relative to the tree origin position).
TreeItemget_next_selected(from:TreeItem)🔗
Returns the next selectedTreeItemafter the given one, ornullif the end is reached.
Iffromisnull, this returns the first selected item.
intget_pressed_button()const🔗
Returns the last pressed button's index.
TreeItemget_root()const🔗
Returns the tree's root item, ornullif the tree is empty.
Vector2get_scroll()const🔗
Returns the current scrolling position.
TreeItemget_selected()const🔗
Returns the currently focused item, ornullif no item is focused.
InSELECT_ROWandSELECT_SINGLEmodes, the focused item is same as the selected item. InSELECT_MULTImode, the focused item is the item under the focus cursor, not necessarily selected.
To get the currently selected item(s), useget_next_selected().
intget_selected_column()const🔗
Returns the currently focused column, or -1 if no column is focused.
InSELECT_SINGLEmode, the focused column is the selected column. InSELECT_ROWmode, the focused column is always 0 if any item is selected. InSELECT_MULTImode, the focused column is the column under the focus cursor, and there are not necessarily any column selected.
To tell whether a column of an item is selected, useTreeItem.is_selected().
boolis_column_clipping_content(column:int)const🔗
Returnstrueif the column has enabled clipping (seeset_column_clip_content()).
boolis_column_expanding(column:int)const🔗
Returnstrueif the column has enabled expanding (seeset_column_expand()).
voidscroll_to_item(item:TreeItem, center_on_item:bool= false)🔗
Causes theTreeto jump to the specifiedTreeItem.
voidset_column_clip_content(column:int, enable:bool)🔗
Allows to enable clipping for column's content, making the content size ignored.
voidset_column_custom_minimum_width(column:int, min_width:int)🔗
Overrides the calculated minimum width of a column. It can be set to0to restore the default behavior. Columns that have the "Expand" flag will use their "min_width" in a similar fashion toControl.size_flags_stretch_ratio.
voidset_column_expand(column:int, expand:bool)🔗
Iftrue, the column will have the "Expand" flag ofControl. Columns that have the "Expand" flag will use their expand ratio in a similar fashion toControl.size_flags_stretch_ratio(seeset_column_expand_ratio()).
voidset_column_expand_ratio(column:int, ratio:int)🔗
Sets the relative expand ratio for a column. Seeset_column_expand().
voidset_column_title(column:int, title:String)🔗
Sets the title of a column.
voidset_column_title_alignment(column:int, title_alignment:HorizontalAlignment)🔗
Sets the column title alignment. Note that@GlobalScope.HORIZONTAL_ALIGNMENT_FILLis not supported for column titles.
voidset_column_title_direction(column:int, direction:TextDirection)🔗
Sets column title base writing direction.
voidset_column_title_language(column:int, language:String)🔗
Sets the language code of the givencolumn's title tolanguage. This is used for line-breaking and text shaping algorithms. Iflanguageis empty, the current locale is used.
voidset_column_title_tooltip_text(column:int, tooltip_text:String)🔗
Sets the column title's tooltip text.
voidset_selected(item:TreeItem, column:int)🔗
Selects the specifiedTreeItemand column.

## Theme Property Descriptions
Colorchildren_hl_line_color=Color(0.27,0.27,0.27,1)🔗
TheColorof the relationship lines between the selectedTreeItemand its children.
Colorcustom_button_font_highlight=Color(0.95,0.95,0.95,1)🔗
TextColorfor aTreeItem.CELL_MODE_CUSTOMmode cell when it's hovered.
Colordrop_position_color=Color(1,1,1,1)🔗
Colorused to draw possible drop locations. SeeDropModeFlagsconstants for further description of drop locations.
Colorfont_color=Color(0.7,0.7,0.7,1)🔗
Default textColorof the item.
Colorfont_disabled_color=Color(0.875,0.875,0.875,0.5)🔗
TextColorfor aTreeItem.CELL_MODE_CHECKmode cell when it's non-editable (seeTreeItem.set_editable()).
Colorfont_hovered_color=Color(0.95,0.95,0.95,1)🔗
TextColorused when the item is hovered and not selected yet.
Colorfont_hovered_dimmed_color=Color(0.875,0.875,0.875,1)🔗
TextColorused when the item is hovered, while a button of the same item is hovered as the same time.
Colorfont_hovered_selected_color=Color(1,1,1,1)🔗
TextColorused when the item is hovered and selected.
Colorfont_outline_color=Color(0,0,0,1)🔗
The tint of text outline of the item.
Colorfont_selected_color=Color(1,1,1,1)🔗
TextColorused when the item is selected.
Colorguide_color=Color(0.7,0.7,0.7,0.25)🔗
Colorof the guideline.
Colorparent_hl_line_color=Color(0.27,0.27,0.27,1)🔗
TheColorof the relationship lines between the selectedTreeItemand its parents.
Colorrelationship_line_color=Color(0.27,0.27,0.27,1)🔗
The defaultColorof the relationship lines.
Colorscroll_hint_color=Color(0,0,0,1)🔗
Colorused to modulate thescroll_hinttexture.
Colortitle_button_color=Color(0.875,0.875,0.875,1)🔗
Default textColorof the title button.
intbutton_margin=4🔗
The horizontal space between each button in a cell.
intcheck_h_separation=4🔗
The horizontal space between the checkbox and the text in aTreeItem.CELL_MODE_CHECKmode cell.
intchildren_hl_line_width=1🔗
The width of the relationship lines between the selectedTreeItemand its children.
intdragging_unfold_wait_msec=500🔗
During a drag-and-drop, this is how many milliseconds to wait over a section before the section unfolds.
intdraw_guides=1🔗
Draws the guidelines if not zero, this acts as a boolean. The guideline is a horizontal line drawn at the bottom of each item.
intdraw_relationship_lines=0🔗
Draws the relationship lines if not zero, this acts as a boolean. Relationship lines are drawn at the start of child items to show hierarchy.
inth_separation=4🔗
The horizontal space between item cells. This is also used as the margin at the start of an item when folding is disabled.
inticon_h_separation=4🔗
The horizontal space between the icon and the text in item's cells.
inticon_max_width=0🔗
The maximum allowed width of the icon in item's cells. This limit is applied on top of the default size of the icon, but before the value set withTreeItem.set_icon_max_width(). The height is adjusted according to the icon's ratio.
intinner_item_margin_bottom=0🔗
The inner bottom margin of a cell.
intinner_item_margin_left=0🔗
The inner left margin of a cell.
intinner_item_margin_right=0🔗
The inner right margin of a cell.
intinner_item_margin_top=0🔗
The inner top margin of a cell.
intitem_margin=16🔗
The horizontal margin at the start of an item. This is used when folding is enabled for the item.
intoutline_size=0🔗
The size of the text outline.
Note:If using a font withFontFile.multichannel_signed_distance_fieldenabled, itsFontFile.msdf_pixel_rangemust be set to at leasttwicethe value ofoutline_sizefor outline rendering to look correct. Otherwise, the outline may appear to be cut off earlier than intended.
intparent_hl_line_margin=0🔗
The space between the parent relationship lines for the selectedTreeItemand the relationship lines to its siblings that are not selected.
intparent_hl_line_width=1🔗
The width of the relationship lines between the selectedTreeItemand its parents.
intrelationship_line_width=1🔗
The default width of the relationship lines.
intscroll_border=4🔗
The maximum distance between the mouse cursor and the control's border to trigger border scrolling when dragging.
intscroll_speed=12🔗
The speed of border scrolling.
intscrollbar_h_separation=4🔗
The horizontal separation of tree content and scrollbar.
intscrollbar_margin_bottom=-1🔗
The bottom margin of the scrollbars. When negative, usespanelbottom margin.
intscrollbar_margin_left=-1🔗
The left margin of the horizontal scrollbar. When negative, usespanelleft margin.
intscrollbar_margin_right=-1🔗
The right margin of the scrollbars. When negative, usespanelright margin.
intscrollbar_margin_top=-1🔗
The top margin of the vertical scrollbar. When negative, usespaneltop margin.
intscrollbar_v_separation=4🔗
The vertical separation of tree content and scrollbar.
intv_separation=4🔗
The vertical padding inside each item, i.e. the distance between the item's content and top/bottom border.
Fontfont🔗
Fontof the item's text.
Fonttitle_button_font🔗
Fontof the title button's text.
intfont_size🔗
Font size of the item's text.
inttitle_button_font_size🔗
Font size of the title button's text.
Texture2Darrow🔗
The arrow icon used when a foldable item is not collapsed.
Texture2Darrow_collapsed🔗
The arrow icon used when a foldable item is collapsed (for left-to-right layouts).
Texture2Darrow_collapsed_mirrored🔗
The arrow icon used when a foldable item is collapsed (for right-to-left layouts).
Texture2Dchecked🔗
The check icon to display when theTreeItem.CELL_MODE_CHECKmode cell is checked and editable (seeTreeItem.set_editable()).
Texture2Dchecked_disabled🔗
The check icon to display when theTreeItem.CELL_MODE_CHECKmode cell is checked and non-editable (seeTreeItem.set_editable()).
Texture2Dindeterminate🔗
The check icon to display when theTreeItem.CELL_MODE_CHECKmode cell is indeterminate and editable (seeTreeItem.set_editable()).
Texture2Dindeterminate_disabled🔗
The check icon to display when theTreeItem.CELL_MODE_CHECKmode cell is indeterminate and non-editable (seeTreeItem.set_editable()).
Texture2Dscroll_hint🔗
The indicator that will be shown when the content can still be scrolled. Seescroll_hint_mode.
Texture2Dselect_arrow🔗
The arrow icon to display for theTreeItem.CELL_MODE_RANGEmode cell.
Texture2Dunchecked🔗
The check icon to display when theTreeItem.CELL_MODE_CHECKmode cell is unchecked and editable (seeTreeItem.set_editable()).
Texture2Dunchecked_disabled🔗
The check icon to display when theTreeItem.CELL_MODE_CHECKmode cell is unchecked and non-editable (seeTreeItem.set_editable()).
Texture2Dupdown🔗
The updown arrow icon to display for theTreeItem.CELL_MODE_RANGEmode cell.
StyleBoxbutton_hover🔗
StyleBoxused when a button in the tree is hovered.
StyleBoxbutton_pressed🔗
StyleBoxused when a button in the tree is pressed.
StyleBoxcursor🔗
StyleBoxused for the cursor, when theTreeis being focused.
StyleBoxcursor_unfocused🔗
StyleBoxused for the cursor, when theTreeis not being focused.
StyleBoxcustom_button🔗
DefaultStyleBoxfor aTreeItem.CELL_MODE_CUSTOMmode cell when button is enabled withTreeItem.set_custom_as_button().
StyleBoxcustom_button_hover🔗
StyleBoxfor aTreeItem.CELL_MODE_CUSTOMmode button cell when it's hovered.
StyleBoxcustom_button_pressed🔗
StyleBoxfor aTreeItem.CELL_MODE_CUSTOMmode button cell when it's pressed.
StyleBoxfocus🔗
The focused style for theTree, drawn on top of everything.
StyleBoxhovered🔗
StyleBoxfor the item being hovered, but not selected.
StyleBoxhovered_dimmed🔗
StyleBoxfor the item being hovered, while a button of the same item is hovered as the same time.
StyleBoxhovered_selected🔗
StyleBoxfor the hovered and selected items, used when theTreeis not being focused.
StyleBoxhovered_selected_focus🔗
StyleBoxfor the hovered and selected items, used when theTreeis being focused.
StyleBoxpanel🔗
The background style for theTree.
StyleBoxselected🔗
StyleBoxfor the selected items, used when theTreeis not being focused.
StyleBoxselected_focus🔗
StyleBoxfor the selected items, used when theTreeis being focused.
StyleBoxtitle_button_hover🔗
StyleBoxused when the title button is being hovered.
StyleBoxtitle_button_normal🔗
DefaultStyleBoxfor the title button.
StyleBoxtitle_button_pressed🔗
StyleBoxused when the title button is being pressed.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.