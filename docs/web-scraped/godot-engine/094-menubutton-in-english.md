# MenuButton in English

# MenuButton
Inherits:Button<BaseButton<Control<CanvasItem<Node<Object
A button that brings up aPopupMenuwhen clicked.

## Description
A button that brings up aPopupMenuwhen clicked. To create new items inside thisPopupMenu, useget_popup().add_item("MyItemName"). You can also create them directly from Godot editor's inspector.
See alsoBaseButtonwhich contains common properties and methods associated with this node.

## Properties

| ActionMode | action_mode | 0(overridesBaseButton) |
|---|---|---|
| bool | flat | true(overridesButton) |
| FocusMode | focus_mode | 3(overridesControl) |
| int | item_count | 0 |
| bool | switch_on_hover | false |
| bool | toggle_mode | true(overridesBaseButton) |

ActionMode
action_mode
0(overridesBaseButton)
bool
flat
true(overridesButton)
FocusMode
focus_mode
3(overridesControl)
item_count
bool
switch_on_hover
false
bool
toggle_mode
true(overridesBaseButton)

## Methods

| PopupMenu | get_popup()const |
|---|---|
| void | set_disable_shortcuts(disabled:bool) |
| void | show_popup() |

PopupMenu
get_popup()const
void
set_disable_shortcuts(disabled:bool)
void
show_popup()

## Signals
about_to_popup()🔗
Emitted when thePopupMenuof this MenuButton is about to show.

## Property Descriptions
intitem_count=0🔗
- voidset_item_count(value:int)
voidset_item_count(value:int)
- intget_item_count()
intget_item_count()
The number of items currently in the list.
boolswitch_on_hover=false🔗
- voidset_switch_on_hover(value:bool)
voidset_switch_on_hover(value:bool)
- boolis_switch_on_hover()
boolis_switch_on_hover()
Iftrue, when the cursor hovers above anotherMenuButtonwithin the same parent which also hasswitch_on_hoverenabled, it will close the currentMenuButtonand open the other one.

## Method Descriptions
PopupMenuget_popup()const🔗
Returns thePopupMenucontained in this button.
Warning:This is a required internal node, removing and freeing it may cause a crash. If you wish to hide it or any of its children, use theirWindow.visibleproperty.
voidset_disable_shortcuts(disabled:bool)🔗
Iftrue, shortcuts are disabled and cannot be used to trigger the button.
voidshow_popup()🔗
Adjusts popup position and sizing for theMenuButton, then shows thePopupMenu. Prefer this over usingget_popup().popup().

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.