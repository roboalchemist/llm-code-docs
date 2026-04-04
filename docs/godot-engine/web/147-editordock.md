# EditorDock

# EditorDock

Experimental:This class may be changed or removed in future versions.
Inherits:MarginContainer<Container<Control<CanvasItem<Node<Object
Inherited By:FileSystemDock
Dockable container for the editor.

## Description

EditorDock is aContainernode that can be docked in one of the editor's dock slots. Docks are added by plugins to provide space for controls related to anEditorPlugin. The editor comes with a few built-in docks, such as the Scene dock, FileSystem dock, etc.
You can add a dock by usingEditorPlugin.add_dock(). The dock can be customized by changing its properties.

```
@tool
extends EditorPlugin

# Dock reference.
var dock

# Plugin initialization.
func _enter_tree():
    dock = EditorDock.new()
    dock.title = "My Dock"
    dock.dock_icon = preload("./dock_icon.png")
    dock.default_slot = EditorDock.DOCK_SLOT_RIGHT_UL
    var dock_content = preload("./dock_content.tscn").instantiate()
    dock.add_child(dock_content)
    add_dock(dock)

# Plugin clean-up.
func _exit_tree():
    remove_dock(dock)
    dock.queue_free()
    dock = null
```

## Tutorials

- Making plugins
Making plugins

## Properties

| BitField[DockLayout] | available_layouts | 5 |
|---|---|---|
| bool | closable | false |
| DockSlot | default_slot | -1 |
| Texture2D | dock_icon |  |
| Shortcut | dock_shortcut |  |
| bool | force_show_icon | false |
| bool | global | true |
| StringName | icon_name | &"" |
| String | layout_key | "" |
| String | title | "" |
| Color | title_color | Color(0,0,0,0) |
| bool | transient | false |

BitField[DockLayout]
available_layouts
bool
closable
false
DockSlot
default_slot
Texture2D
dock_icon
Shortcut
dock_shortcut
bool
force_show_icon
false
bool
global
true
StringName
icon_name
String
layout_key
String
title
Color
title_color
Color(0,0,0,0)
bool
transient
false

## Methods

| void | _load_layout_from_config(config:ConfigFile, section:String)virtual |
|---|---|
| void | _save_layout_to_config(config:ConfigFile, section:String)virtualconst |
| void | _update_layout(layout:int)virtual |
| void | close() |
| void | make_visible() |
| void | open() |

void
_load_layout_from_config(config:ConfigFile, section:String)virtual
void
_save_layout_to_config(config:ConfigFile, section:String)virtualconst
void
_update_layout(layout:int)virtual
void
close()
void
make_visible()
void
open()

## Signals

closed()🔗
Emitted when the dock is closed with the Close button in the context popup, before it's removed from its parent. Seeclosable.

## Enumerations

flagsDockLayout:🔗
DockLayoutDOCK_LAYOUT_VERTICAL=1
Allows placing the dock in the vertical dock slots on either side of the editor.
DockLayoutDOCK_LAYOUT_HORIZONTAL=2
Allows placing the dock in the editor's bottom panel.
DockLayoutDOCK_LAYOUT_FLOATING=4
Allows making the dock floating (opened as a separate window).
DockLayoutDOCK_LAYOUT_ALL=7
Allows placing the dock in all available slots.
enumDockSlot:🔗
DockSlotDOCK_SLOT_NONE=-1
The dock is closed.
DockSlotDOCK_SLOT_LEFT_UL=0
Dock slot, left side, upper-left (empty in default layout).
DockSlotDOCK_SLOT_LEFT_BL=1
Dock slot, left side, bottom-left (empty in default layout).
DockSlotDOCK_SLOT_LEFT_UR=2
Dock slot, left side, upper-right (in default layout includes Scene and Import docks).
DockSlotDOCK_SLOT_LEFT_BR=3
Dock slot, left side, bottom-right (in default layout includes FileSystem and History docks).
DockSlotDOCK_SLOT_RIGHT_UL=4
Dock slot, right side, upper-left (in default layout includes Inspector, Signal, and Group docks).
DockSlotDOCK_SLOT_RIGHT_BL=5
Dock slot, right side, bottom-left (empty in default layout).
DockSlotDOCK_SLOT_RIGHT_UR=6
Dock slot, right side, upper-right (empty in default layout).
DockSlotDOCK_SLOT_RIGHT_BR=7
Dock slot, right side, bottom-right (empty in default layout).
DockSlotDOCK_SLOT_BOTTOM=8
Bottom panel.
DockSlotDOCK_SLOT_MAX=9
Represents the size of theDockSlotenum.

## Property Descriptions

BitField[DockLayout]available_layouts=5🔗

- voidset_available_layouts(value:BitField[DockLayout])
voidset_available_layouts(value:BitField[DockLayout])
- BitField[DockLayout]get_available_layouts()
BitField[DockLayout]get_available_layouts()
The available layouts for this dock, as a bitmask. By default, the dock allows vertical and floating layouts.
boolclosable=false🔗
- voidset_closable(value:bool)
voidset_closable(value:bool)
- boolis_closable()
boolis_closable()
Iftrue, the dock can be closed with the Close button in the context popup. Docks withglobalenabled are always closable.
DockSlotdefault_slot=-1🔗
- voidset_default_slot(value:DockSlot)
voidset_default_slot(value:DockSlot)
- DockSlotget_default_slot()
DockSlotget_default_slot()
The default dock slot used when adding the dock withEditorPlugin.add_dock().
After the dock is added, it can be moved to a different slot and the editor will automatically remember its position between sessions. If you remove and re-add the dock, it will be reset to default.
Texture2Ddock_icon🔗
- voidset_dock_icon(value:Texture2D)
voidset_dock_icon(value:Texture2D)
- Texture2Dget_dock_icon()
Texture2Dget_dock_icon()
The icon for the dock, as a texture. If specified, it will overrideicon_name.
Shortcutdock_shortcut🔗
- voidset_dock_shortcut(value:Shortcut)
voidset_dock_shortcut(value:Shortcut)
- Shortcutget_dock_shortcut()
Shortcutget_dock_shortcut()
The shortcut used to open the dock.
boolforce_show_icon=false🔗
- voidset_force_show_icon(value:bool)
voidset_force_show_icon(value:bool)
- boolget_force_show_icon()
boolget_force_show_icon()
Iftrue, the dock will always display an icon, regardless ofEditorSettings.interface/editor/dock_tab_styleorEditorSettings.interface/editor/bottom_dock_tab_style.
boolglobal=true🔗
- voidset_global(value:bool)
voidset_global(value:bool)
- boolis_global()
boolis_global()
Iftrue, the dock appears in theEditor > Editor Docksmenu and can be closed. Non-global docks can still be closed usingclose()or whenclosableistrue.
StringNameicon_name=&""🔗
- voidset_icon_name(value:StringName)
voidset_icon_name(value:StringName)
- StringNameget_icon_name()
StringNameget_icon_name()
The icon for the dock, as a name from theEditorIconstheme type in the editor theme. You can find the list of available iconshere.
Stringlayout_key=""🔗
- voidset_layout_key(value:String)
voidset_layout_key(value:String)
- Stringget_layout_key()
Stringget_layout_key()
The key representing this dock in the editor's layout file. If empty, the dock's displayed name will be used instead.
Stringtitle=""🔗
- voidset_title(value:String)
voidset_title(value:String)
- Stringget_title()
Stringget_title()
The title of the dock's tab. If empty, the dock'sNode.namewill be used. If the name is auto-generated (contains@), the first child's name will be used instead.
Colortitle_color=Color(0,0,0,0)🔗
- voidset_title_color(value:Color)
voidset_title_color(value:Color)
- Colorget_title_color()
Colorget_title_color()
The color of the dock tab's title. If its alpha is0.0, the default font color will be used.
booltransient=false🔗
- voidset_transient(value:bool)
voidset_transient(value:bool)
- boolis_transient()
boolis_transient()
Iftrue, the dock is not automatically opened or closed when loading an editor layout, only moved. It also can't be opened using a shortcut. This is meant for docks that are opened and closed in specific cases, such as when selecting aTileMaporAnimationTreenode.

## Method Descriptions

void_load_layout_from_config(config:ConfigFile, section:String)virtual🔗
Implement this method to handle loading this dock's layout. It's equivalent toEditorPlugin._set_window_layout().sectionis a unique section based onlayout_key.
void_save_layout_to_config(config:ConfigFile, section:String)virtualconst🔗
Implement this method to handle saving this dock's layout. It's equivalent toEditorPlugin._get_window_layout().sectionis a unique section based onlayout_key.
void_update_layout(layout:int)virtual🔗
Implement this method to handle the layout switching for this dock.layoutis one of theDockLayoutconstants.

```
func _update_layout(layout):
    box_container.vertical = (layout == DOCK_LAYOUT_VERTICAL)
```

voidclose()🔗
Closes the dock, making its tab hidden.
voidmake_visible()🔗
Focuses the dock's tab (or window if it's floating). If the dock was closed, it will be opened. If it's a bottom dock, makes the bottom panel visible.
voidopen()🔗
Opens the dock. It will appear in the last used dock slot. If the dock has no default slot, it will be opened floating.
Note:This does not focus the dock. If you want to open and focus the dock, usemake_visible().

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
