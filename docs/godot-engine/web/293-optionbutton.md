# OptionButton

# OptionButton
Inherits:Button<BaseButton<Control<CanvasItem<Node<Object
A button that brings up a dropdown with selectable options when pressed.

## Description
OptionButtonis a type of button that brings up a dropdown with selectable items when pressed. The item selected becomes the "current" item and is displayed as the button text.
See alsoBaseButtonwhich contains common properties and methods associated with this node.
Note:The IDs used for items are limited to signed 32-bit integers, not the full 64 bits ofint. These have a range of-2^31to2^31-1, that is,-2147483648to2147483647.
Note:TheButton.textandButton.iconproperties are set automatically based on the selected item. They shouldn't be changed manually.

## Properties

| ActionMode | action_mode | 0(overridesBaseButton) |
|---|---|---|
| HorizontalAlignment | alignment | 0(overridesButton) |
| bool | allow_reselect | false |
| bool | fit_to_longest_item | true |
| int | item_count | 0 |
| int | selected | -1 |
| bool | toggle_mode | true(overridesBaseButton) |

ActionMode
action_mode
0(overridesBaseButton)
HorizontalAlignment
alignment
0(overridesButton)
bool
allow_reselect
false
bool
fit_to_longest_item
true
item_count
selected
bool
toggle_mode
true(overridesBaseButton)

## Methods

| void | add_icon_item(texture:Texture2D, label:String, id:int= -1) |
|---|---|
| void | add_item(label:String, id:int= -1) |
| void | add_separator(text:String= "") |
| void | clear() |
| AutoTranslateMode | get_item_auto_translate_mode(idx:int)const |
| Texture2D | get_item_icon(idx:int)const |
| int | get_item_id(idx:int)const |
| int | get_item_index(id:int)const |
| Variant | get_item_metadata(idx:int)const |
| String | get_item_text(idx:int)const |
| String | get_item_tooltip(idx:int)const |
| PopupMenu | get_popup()const |
| int | get_selectable_item(from_last:bool= false)const |
| int | get_selected_id()const |
| Variant | get_selected_metadata()const |
| bool | has_selectable_items()const |
| bool | is_item_disabled(idx:int)const |
| bool | is_item_separator(idx:int)const |
| void | remove_item(idx:int) |
| void | select(idx:int) |
| void | set_disable_shortcuts(disabled:bool) |
| void | set_item_auto_translate_mode(idx:int, mode:AutoTranslateMode) |
| void | set_item_disabled(idx:int, disabled:bool) |
| void | set_item_icon(idx:int, texture:Texture2D) |
| void | set_item_id(idx:int, id:int) |
| void | set_item_metadata(idx:int, metadata:Variant) |
| void | set_item_text(idx:int, text:String) |
| void | set_item_tooltip(idx:int, tooltip:String) |
| void | show_popup() |

void
add_icon_item(texture:Texture2D, label:String, id:int= -1)
void
add_item(label:String, id:int= -1)
void
add_separator(text:String= "")
void
clear()
AutoTranslateMode
get_item_auto_translate_mode(idx:int)const
Texture2D
get_item_icon(idx:int)const
get_item_id(idx:int)const
get_item_index(id:int)const
Variant
get_item_metadata(idx:int)const
String
get_item_text(idx:int)const
String
get_item_tooltip(idx:int)const
PopupMenu
get_popup()const
get_selectable_item(from_last:bool= false)const
get_selected_id()const
Variant
get_selected_metadata()const
bool
has_selectable_items()const
bool
is_item_disabled(idx:int)const
bool
is_item_separator(idx:int)const
void
remove_item(idx:int)
void
select(idx:int)
void
set_disable_shortcuts(disabled:bool)
void
set_item_auto_translate_mode(idx:int, mode:AutoTranslateMode)
void
set_item_disabled(idx:int, disabled:bool)
void
set_item_icon(idx:int, texture:Texture2D)
void
set_item_id(idx:int, id:int)
void
set_item_metadata(idx:int, metadata:Variant)
void
set_item_text(idx:int, text:String)
void
set_item_tooltip(idx:int, tooltip:String)
void
show_popup()

## Theme Properties

| int | arrow_margin | 4 |
|---|---|---|
| int | modulate_arrow | 0 |
| Texture2D | arrow |  |

arrow_margin
modulate_arrow
Texture2D
arrow

## Signals
item_focused(index:int)🔗
Emitted when the user navigates to an item using theProjectSettings.input/ui_uporProjectSettings.input/ui_downinput actions. The index of the item selected is passed as argument.
item_selected(index:int)🔗
Emitted when the current item has been changed by the user. The index of the item selected is passed as argument.
allow_reselectmust be enabled to reselect an item.

## Property Descriptions
boolallow_reselect=false🔗
- voidset_allow_reselect(value:bool)
voidset_allow_reselect(value:bool)
- boolget_allow_reselect()
boolget_allow_reselect()
Iftrue, the currently selected item can be selected again.
boolfit_to_longest_item=true🔗
- voidset_fit_to_longest_item(value:bool)
voidset_fit_to_longest_item(value:bool)
- boolis_fit_to_longest_item()
boolis_fit_to_longest_item()
Iftrue, minimum size will be determined by the longest item's text, instead of the currently selected one's.
Note:For performance reasons, the minimum size doesn't update immediately when adding, removing or modifying items.
intitem_count=0🔗
- voidset_item_count(value:int)
voidset_item_count(value:int)
- intget_item_count()
intget_item_count()
The number of items to select from.
intselected=-1🔗
- intget_selected()
intget_selected()
The index of the currently selected item, or-1if no item is selected.

## Method Descriptions
voidadd_icon_item(texture:Texture2D, label:String, id:int= -1)🔗
Adds an item, with atextureicon, textlabeland (optionally)id. If noidis passed, the item index will be used as the item's ID. New items are appended at the end.
Note:The item will be selected if there are no other items.
voidadd_item(label:String, id:int= -1)🔗
Adds an item, with textlabeland (optionally)id. If noidis passed, the item index will be used as the item's ID. New items are appended at the end.
Note:The item will be selected if there are no other items.
voidadd_separator(text:String= "")🔗
Adds a separator to the list of items. Separators help to group items, and can optionally be given atextheader. A separator also gets an index assigned, and is appended at the end of the item list.
voidclear()🔗
Clears all the items in theOptionButton.
AutoTranslateModeget_item_auto_translate_mode(idx:int)const🔗
Returns the auto translate mode of the item at indexidx.
Texture2Dget_item_icon(idx:int)const🔗
Returns the icon of the item at indexidx.
intget_item_id(idx:int)const🔗
Returns the ID of the item at indexidx.
intget_item_index(id:int)const🔗
Returns the index of the item with the givenid.
Variantget_item_metadata(idx:int)const🔗
Retrieves the metadata of an item. Metadata may be any type and can be used to store extra information about an item, such as an external string ID.
Stringget_item_text(idx:int)const🔗
Returns the text of the item at indexidx.
Stringget_item_tooltip(idx:int)const🔗
Returns the tooltip of the item at indexidx.
PopupMenuget_popup()const🔗
Returns thePopupMenucontained in this button.
Warning:This is a required internal node, removing and freeing it may cause a crash. If you wish to hide it or any of its children, use theirWindow.visibleproperty.
intget_selectable_item(from_last:bool= false)const🔗
Returns the index of the first item which is not disabled, or marked as a separator. Iffrom_lastistrue, the items will be searched in reverse order.
Returns-1if no item is found.
intget_selected_id()const🔗
Returns the ID of the selected item, or-1if no item is selected.
Variantget_selected_metadata()const🔗
Gets the metadata of the selected item. Metadata for items can be set usingset_item_metadata().
boolhas_selectable_items()const🔗
Returnstrueif this button contains at least one item which is not disabled, or marked as a separator.
boolis_item_disabled(idx:int)const🔗
Returnstrueif the item at indexidxis disabled.
boolis_item_separator(idx:int)const🔗
Returnstrueif the item at indexidxis marked as a separator.
voidremove_item(idx:int)🔗
Removes the item at indexidx.
voidselect(idx:int)🔗
Selects an item by index and makes it the current item. This will work even if the item is disabled.
Passing-1as the index deselects any currently selected item.
voidset_disable_shortcuts(disabled:bool)🔗
Iftrue, shortcuts are disabled and cannot be used to trigger the button.
voidset_item_auto_translate_mode(idx:int, mode:AutoTranslateMode)🔗
Sets the auto translate mode of the item at indexidx.
Items useNode.AUTO_TRANSLATE_MODE_INHERITby default, which uses the same auto translate mode as theOptionButtonitself.
voidset_item_disabled(idx:int, disabled:bool)🔗
Sets whether the item at indexidxis disabled.
Disabled items are drawn differently in the dropdown and are not selectable by the user. If the current selected item is set as disabled, it will remain selected.
voidset_item_icon(idx:int, texture:Texture2D)🔗
Sets the icon of the item at indexidx.
voidset_item_id(idx:int, id:int)🔗
Sets the ID of the item at indexidx.
voidset_item_metadata(idx:int, metadata:Variant)🔗
Sets the metadata of an item. Metadata may be of any type and can be used to store extra information about an item, such as an external string ID.
voidset_item_text(idx:int, text:String)🔗
Sets the text of the item at indexidx.
voidset_item_tooltip(idx:int, tooltip:String)🔗
Sets the tooltip of the item at indexidx.
voidshow_popup()🔗
Adjusts popup position and sizing for theOptionButton, then shows thePopupMenu. Prefer this over usingget_popup().popup().

## Theme Property Descriptions
intarrow_margin=4🔗
The horizontal space between the arrow icon and the right edge of the button.
intmodulate_arrow=0🔗
If different than0, the arrow icon will be modulated to the font color.
Texture2Darrow🔗
The arrow icon to be drawn on the right end of the button.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.