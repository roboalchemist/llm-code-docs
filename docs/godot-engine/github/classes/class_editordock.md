:github_url: hide



# EditorDock

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [MarginContainer<class_MarginContainer>] **<** [Container<class_Container>] **<** [Control<class_Control>] **<** [CanvasItem<class_CanvasItem>] **<** [Node<class_Node>] **<** [Object<class_Object>]

**Inherited By:** [FileSystemDock<class_FileSystemDock>]

Dockable container for the editor.


## Description

EditorDock is a [Container<class_Container>] node that can be docked in one of the editor's dock slots. Docks are added by plugins to provide space for controls related to an [EditorPlugin<class_EditorPlugin>]. The editor comes with a few built-in docks, such as the Scene dock, FileSystem dock, etc.

You can add a dock by using [EditorPlugin.add_dock()<class_EditorPlugin_method_add_dock>]. The dock can be customized by changing its properties.

::

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


## Tutorials

- [../tutorials/plugins/editor/making_plugins](Making plugins .md)


## Properties

> **TABLE**
> :widths: auto
>
> +-------------------------------------------------------------+-----------------------------------------------------------------------+-----------------------+
> | |bitfield|\[:ref:`DockLayout<enum_EditorDock_DockLayout>`\] | :ref:`available_layouts<class_EditorDock_property_available_layouts>` | ``5``                 |
> +-------------------------------------------------------------+-----------------------------------------------------------------------+-----------------------+
> | :ref:`bool<class_bool>`                                     | :ref:`closable<class_EditorDock_property_closable>`                   | ``false``             |
> +-------------------------------------------------------------+-----------------------------------------------------------------------+-----------------------+
> | :ref:`DockSlot<enum_EditorDock_DockSlot>`                   | :ref:`default_slot<class_EditorDock_property_default_slot>`           | ``-1``                |
> +-------------------------------------------------------------+-----------------------------------------------------------------------+-----------------------+
> | :ref:`Texture2D<class_Texture2D>`                           | :ref:`dock_icon<class_EditorDock_property_dock_icon>`                 |                       |
> +-------------------------------------------------------------+-----------------------------------------------------------------------+-----------------------+
> | :ref:`Shortcut<class_Shortcut>`                             | :ref:`dock_shortcut<class_EditorDock_property_dock_shortcut>`         |                       |
> +-------------------------------------------------------------+-----------------------------------------------------------------------+-----------------------+
> | :ref:`bool<class_bool>`                                     | :ref:`force_show_icon<class_EditorDock_property_force_show_icon>`     | ``false``             |
> +-------------------------------------------------------------+-----------------------------------------------------------------------+-----------------------+
> | :ref:`bool<class_bool>`                                     | :ref:`global<class_EditorDock_property_global>`                       | ``true``              |
> +-------------------------------------------------------------+-----------------------------------------------------------------------+-----------------------+
> | :ref:`StringName<class_StringName>`                         | :ref:`icon_name<class_EditorDock_property_icon_name>`                 | ``&""``               |
> +-------------------------------------------------------------+-----------------------------------------------------------------------+-----------------------+
> | :ref:`String<class_String>`                                 | :ref:`layout_key<class_EditorDock_property_layout_key>`               | ``""``                |
> +-------------------------------------------------------------+-----------------------------------------------------------------------+-----------------------+
> | :ref:`String<class_String>`                                 | :ref:`title<class_EditorDock_property_title>`                         | ``""``                |
> +-------------------------------------------------------------+-----------------------------------------------------------------------+-----------------------+
> | :ref:`Color<class_Color>`                                   | :ref:`title_color<class_EditorDock_property_title_color>`             | ``Color(0, 0, 0, 0)`` |
> +-------------------------------------------------------------+-----------------------------------------------------------------------+-----------------------+
> | :ref:`bool<class_bool>`                                     | :ref:`transient<class_EditorDock_property_transient>`                 | ``false``             |
> +-------------------------------------------------------------+-----------------------------------------------------------------------+-----------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void| | :ref:`_load_layout_from_config<class_EditorDock_private_method__load_layout_from_config>`\ (\ config\: :ref:`ConfigFile<class_ConfigFile>`, section\: :ref:`String<class_String>`\ ) |virtual|     |
> +--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void| | :ref:`_save_layout_to_config<class_EditorDock_private_method__save_layout_to_config>`\ (\ config\: :ref:`ConfigFile<class_ConfigFile>`, section\: :ref:`String<class_String>`\ ) |virtual| |const| |
> +--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void| | :ref:`_update_layout<class_EditorDock_private_method__update_layout>`\ (\ layout\: :ref:`int<class_int>`\ ) |virtual|                                                                              |
> +--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void| | :ref:`close<class_EditorDock_method_close>`\ (\ )                                                                                                                                                  |
> +--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void| | :ref:`make_visible<class_EditorDock_method_make_visible>`\ (\ )                                                                                                                                    |
> +--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void| | :ref:`open<class_EditorDock_method_open>`\ (\ )                                                                                                                                                    |
> +--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Signals



**closed**\ (\ ) [🔗<class_EditorDock_signal_closed>]

Emitted when the dock is closed with the Close button in the context popup, before it's removed from its parent. See [closable<class_EditorDock_property_closable>].


----


## Enumerations



flags **DockLayout**: [🔗<enum_EditorDock_DockLayout>]



[DockLayout<enum_EditorDock_DockLayout>] **DOCK_LAYOUT_VERTICAL** = `1`

Allows placing the dock in the vertical dock slots on either side of the editor.



[DockLayout<enum_EditorDock_DockLayout>] **DOCK_LAYOUT_HORIZONTAL** = `2`

Allows placing the dock in the editor's bottom panel.



[DockLayout<enum_EditorDock_DockLayout>] **DOCK_LAYOUT_FLOATING** = `4`

Allows making the dock floating (opened as a separate window).



[DockLayout<enum_EditorDock_DockLayout>] **DOCK_LAYOUT_ALL** = `7`

Allows placing the dock in all available slots.


----



enum **DockSlot**: [🔗<enum_EditorDock_DockSlot>]



[DockSlot<enum_EditorDock_DockSlot>] **DOCK_SLOT_NONE** = `-1`

The dock is closed.



[DockSlot<enum_EditorDock_DockSlot>] **DOCK_SLOT_LEFT_UL** = `0`

Dock slot, left side, upper-left (empty in default layout).



[DockSlot<enum_EditorDock_DockSlot>] **DOCK_SLOT_LEFT_BL** = `1`

Dock slot, left side, bottom-left (empty in default layout).



[DockSlot<enum_EditorDock_DockSlot>] **DOCK_SLOT_LEFT_UR** = `2`

Dock slot, left side, upper-right (in default layout includes Scene and Import docks).



[DockSlot<enum_EditorDock_DockSlot>] **DOCK_SLOT_LEFT_BR** = `3`

Dock slot, left side, bottom-right (in default layout includes FileSystem and History docks).



[DockSlot<enum_EditorDock_DockSlot>] **DOCK_SLOT_RIGHT_UL** = `4`

Dock slot, right side, upper-left (in default layout includes Inspector, Signal, and Group docks).



[DockSlot<enum_EditorDock_DockSlot>] **DOCK_SLOT_RIGHT_BL** = `5`

Dock slot, right side, bottom-left (empty in default layout).



[DockSlot<enum_EditorDock_DockSlot>] **DOCK_SLOT_RIGHT_UR** = `6`

Dock slot, right side, upper-right (empty in default layout).



[DockSlot<enum_EditorDock_DockSlot>] **DOCK_SLOT_RIGHT_BR** = `7`

Dock slot, right side, bottom-right (empty in default layout).



[DockSlot<enum_EditorDock_DockSlot>] **DOCK_SLOT_BOTTOM** = `8`

Bottom panel.



[DockSlot<enum_EditorDock_DockSlot>] **DOCK_SLOT_MAX** = `9`

Represents the size of the [DockSlot<enum_EditorDock_DockSlot>] enum.


----


## Property Descriptions



|bitfield|\[[DockLayout<enum_EditorDock_DockLayout>]\] **available_layouts** = `5` [🔗<class_EditorDock_property_available_layouts>]


- |void| **set_available_layouts**\ (\ value\: |bitfield|\[[DockLayout<enum_EditorDock_DockLayout>]\]\ )
- |bitfield|\[[DockLayout<enum_EditorDock_DockLayout>]\] **get_available_layouts**\ (\ )

The available layouts for this dock, as a bitmask. By default, the dock allows vertical and floating layouts.


----



[bool<class_bool>] **closable** = `false` [🔗<class_EditorDock_property_closable>]


- |void| **set_closable**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_closable**\ (\ )

If `true`, the dock can be closed with the Close button in the context popup. Docks with [global<class_EditorDock_property_global>] enabled are always closable.


----



[DockSlot<enum_EditorDock_DockSlot>] **default_slot** = `-1` [🔗<class_EditorDock_property_default_slot>]


- |void| **set_default_slot**\ (\ value\: [DockSlot<enum_EditorDock_DockSlot>]\ )
- [DockSlot<enum_EditorDock_DockSlot>] **get_default_slot**\ (\ )

The default dock slot used when adding the dock with [EditorPlugin.add_dock()<class_EditorPlugin_method_add_dock>].

After the dock is added, it can be moved to a different slot and the editor will automatically remember its position between sessions. If you remove and re-add the dock, it will be reset to default.


----



[Texture2D<class_Texture2D>] **dock_icon** [🔗<class_EditorDock_property_dock_icon>]


- |void| **set_dock_icon**\ (\ value\: [Texture2D<class_Texture2D>]\ )
- [Texture2D<class_Texture2D>] **get_dock_icon**\ (\ )

The icon for the dock, as a texture. If specified, it will override [icon_name<class_EditorDock_property_icon_name>].


----



[Shortcut<class_Shortcut>] **dock_shortcut** [🔗<class_EditorDock_property_dock_shortcut>]


- |void| **set_dock_shortcut**\ (\ value\: [Shortcut<class_Shortcut>]\ )
- [Shortcut<class_Shortcut>] **get_dock_shortcut**\ (\ )

The shortcut used to open the dock.


----



[bool<class_bool>] **force_show_icon** = `false` [🔗<class_EditorDock_property_force_show_icon>]


- |void| **set_force_show_icon**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_force_show_icon**\ (\ )

If `true`, the dock will always display an icon, regardless of [EditorSettings.interface/editor/dock_tab_style<class_EditorSettings_property_interface/editor/dock_tab_style>] or [EditorSettings.interface/editor/bottom_dock_tab_style<class_EditorSettings_property_interface/editor/bottom_dock_tab_style>].


----



[bool<class_bool>] **global** = `true` [🔗<class_EditorDock_property_global>]


- |void| **set_global**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_global**\ (\ )

If `true`, the dock appears in the **Editor > Editor Docks** menu and can be closed. Non-global docks can still be closed using [close()<class_EditorDock_method_close>] or when [closable<class_EditorDock_property_closable>] is `true`.


----



[StringName<class_StringName>] **icon_name** = `&""` [🔗<class_EditorDock_property_icon_name>]


- |void| **set_icon_name**\ (\ value\: [StringName<class_StringName>]\ )
- [StringName<class_StringName>] **get_icon_name**\ (\ )

The icon for the dock, as a name from the `EditorIcons` theme type in the editor theme. You can find the list of available icons [here ](https://godot-editor-icons.github.io/)_.


----



[String<class_String>] **layout_key** = `""` [🔗<class_EditorDock_property_layout_key>]


- |void| **set_layout_key**\ (\ value\: [String<class_String>]\ )
- [String<class_String>] **get_layout_key**\ (\ )

The key representing this dock in the editor's layout file. If empty, the dock's displayed name will be used instead.


----



[String<class_String>] **title** = `""` [🔗<class_EditorDock_property_title>]


- |void| **set_title**\ (\ value\: [String<class_String>]\ )
- [String<class_String>] **get_title**\ (\ )

The title of the dock's tab. If empty, the dock's [Node.name<class_Node_property_name>] will be used. If the name is auto-generated (contains `@`), the first child's name will be used instead.


----



[Color<class_Color>] **title_color** = `Color(0, 0, 0, 0)` [🔗<class_EditorDock_property_title_color>]


- |void| **set_title_color**\ (\ value\: [Color<class_Color>]\ )
- [Color<class_Color>] **get_title_color**\ (\ )

The color of the dock tab's title. If its alpha is `0.0`, the default font color will be used.


----



[bool<class_bool>] **transient** = `false` [🔗<class_EditorDock_property_transient>]


- |void| **set_transient**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_transient**\ (\ )

If `true`, the dock is not automatically opened or closed when loading an editor layout, only moved. It also can't be opened using a shortcut. This is meant for docks that are opened and closed in specific cases, such as when selecting a [TileMap<class_TileMap>] or [AnimationTree<class_AnimationTree>] node.


----


## Method Descriptions



|void| **_load_layout_from_config**\ (\ config\: [ConfigFile<class_ConfigFile>], section\: [String<class_String>]\ ) |virtual| [🔗<class_EditorDock_private_method__load_layout_from_config>]

Implement this method to handle loading this dock's layout. It's equivalent to [EditorPlugin._set_window_layout()<class_EditorPlugin_private_method__set_window_layout>]. `section` is a unique section based on [layout_key<class_EditorDock_property_layout_key>].


----



|void| **_save_layout_to_config**\ (\ config\: [ConfigFile<class_ConfigFile>], section\: [String<class_String>]\ ) |virtual| |const| [🔗<class_EditorDock_private_method__save_layout_to_config>]

Implement this method to handle saving this dock's layout. It's equivalent to [EditorPlugin._get_window_layout()<class_EditorPlugin_private_method__get_window_layout>]. `section` is a unique section based on [layout_key<class_EditorDock_property_layout_key>].


----



|void| **_update_layout**\ (\ layout\: [int<class_int>]\ ) |virtual| [🔗<class_EditorDock_private_method__update_layout>]

Implement this method to handle the layout switching for this dock. `layout` is one of the [DockLayout<enum_EditorDock_DockLayout>] constants.

::

    func _update_layout(layout):
        box_container.vertical = (layout == DOCK_LAYOUT_VERTICAL)


----



|void| **close**\ (\ ) [🔗<class_EditorDock_method_close>]

Closes the dock, making its tab hidden.


----



|void| **make_visible**\ (\ ) [🔗<class_EditorDock_method_make_visible>]

Focuses the dock's tab (or window if it's floating). If the dock was closed, it will be opened. If it's a bottom dock, makes the bottom panel visible.


----



|void| **open**\ (\ ) [🔗<class_EditorDock_method_open>]

Opens the dock. It will appear in the last used dock slot. If the dock has no default slot, it will be opened floating.

\ **Note:** This does not focus the dock. If you want to open and focus the dock, use [make_visible()<class_EditorDock_method_make_visible>].

