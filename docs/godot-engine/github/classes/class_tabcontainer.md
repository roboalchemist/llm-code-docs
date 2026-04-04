:github_url: hide



# TabContainer

**Inherits:** [Container<class_Container>] **<** [Control<class_Control>] **<** [CanvasItem<class_CanvasItem>] **<** [Node<class_Node>] **<** [Object<class_Object>]

A container that creates a tab for each child control, displaying only the active tab's control.


## Description

Arranges child controls into a tabbed view, creating a tab for each one. The active tab's corresponding control is made visible, while all other child controls are hidden. Ignores non-control children.

\ **Note:** The drawing of the clickable tabs is handled by this node; [TabBar<class_TabBar>] is not needed.


## Tutorials

- [../tutorials/ui/gui_containers](Using Containers .md)


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------------------------------+-----------------------------------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>`                           | :ref:`all_tabs_in_front<class_TabContainer_property_all_tabs_in_front>`                       | ``false`` |
> +---------------------------------------------------+-----------------------------------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>`                           | :ref:`clip_tabs<class_TabContainer_property_clip_tabs>`                                       | ``true``  |
> +---------------------------------------------------+-----------------------------------------------------------------------------------------------+-----------+
> | :ref:`int<class_int>`                             | :ref:`current_tab<class_TabContainer_property_current_tab>`                                   | ``-1``    |
> +---------------------------------------------------+-----------------------------------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>`                           | :ref:`deselect_enabled<class_TabContainer_property_deselect_enabled>`                         | ``false`` |
> +---------------------------------------------------+-----------------------------------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>`                           | :ref:`drag_to_rearrange_enabled<class_TabContainer_property_drag_to_rearrange_enabled>`       | ``false`` |
> +---------------------------------------------------+-----------------------------------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>`                           | :ref:`switch_on_drag_hover<class_TabContainer_property_switch_on_drag_hover>`                 | ``true``  |
> +---------------------------------------------------+-----------------------------------------------------------------------------------------------+-----------+
> | :ref:`AlignmentMode<enum_TabBar_AlignmentMode>`   | :ref:`tab_alignment<class_TabContainer_property_tab_alignment>`                               | ``0``     |
> +---------------------------------------------------+-----------------------------------------------------------------------------------------------+-----------+
> | :ref:`FocusMode<enum_Control_FocusMode>`          | :ref:`tab_focus_mode<class_TabContainer_property_tab_focus_mode>`                             | ``2``     |
> +---------------------------------------------------+-----------------------------------------------------------------------------------------------+-----------+
> | :ref:`TabPosition<enum_TabContainer_TabPosition>` | :ref:`tabs_position<class_TabContainer_property_tabs_position>`                               | ``0``     |
> +---------------------------------------------------+-----------------------------------------------------------------------------------------------+-----------+
> | :ref:`int<class_int>`                             | :ref:`tabs_rearrange_group<class_TabContainer_property_tabs_rearrange_group>`                 | ``-1``    |
> +---------------------------------------------------+-----------------------------------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>`                           | :ref:`tabs_visible<class_TabContainer_property_tabs_visible>`                                 | ``true``  |
> +---------------------------------------------------+-----------------------------------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>`                           | :ref:`use_hidden_tabs_for_min_size<class_TabContainer_property_use_hidden_tabs_for_min_size>` | ``false`` |
> +---------------------------------------------------+-----------------------------------------------------------------------------------------------+-----------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Control<class_Control>`     | :ref:`get_current_tab_control<class_TabContainer_method_get_current_tab_control>`\ (\ ) |const|                                                            |
> +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Popup<class_Popup>`         | :ref:`get_popup<class_TabContainer_method_get_popup>`\ (\ ) |const|                                                                                        |
> +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`             | :ref:`get_previous_tab<class_TabContainer_method_get_previous_tab>`\ (\ ) |const|                                                                          |
> +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`TabBar<class_TabBar>`       | :ref:`get_tab_bar<class_TabContainer_method_get_tab_bar>`\ (\ ) |const|                                                                                    |
> +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Texture2D<class_Texture2D>` | :ref:`get_tab_button_icon<class_TabContainer_method_get_tab_button_icon>`\ (\ tab_idx\: :ref:`int<class_int>`\ ) |const|                                   |
> +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Control<class_Control>`     | :ref:`get_tab_control<class_TabContainer_method_get_tab_control>`\ (\ tab_idx\: :ref:`int<class_int>`\ ) |const|                                           |
> +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`             | :ref:`get_tab_count<class_TabContainer_method_get_tab_count>`\ (\ ) |const|                                                                                |
> +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Texture2D<class_Texture2D>` | :ref:`get_tab_icon<class_TabContainer_method_get_tab_icon>`\ (\ tab_idx\: :ref:`int<class_int>`\ ) |const|                                                 |
> +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`             | :ref:`get_tab_icon_max_width<class_TabContainer_method_get_tab_icon_max_width>`\ (\ tab_idx\: :ref:`int<class_int>`\ ) |const|                             |
> +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`             | :ref:`get_tab_idx_at_point<class_TabContainer_method_get_tab_idx_at_point>`\ (\ point\: :ref:`Vector2<class_Vector2>`\ ) |const|                           |
> +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`             | :ref:`get_tab_idx_from_control<class_TabContainer_method_get_tab_idx_from_control>`\ (\ control\: :ref:`Control<class_Control>`\ ) |const|                 |
> +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Variant<class_Variant>`     | :ref:`get_tab_metadata<class_TabContainer_method_get_tab_metadata>`\ (\ tab_idx\: :ref:`int<class_int>`\ ) |const|                                         |
> +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`       | :ref:`get_tab_title<class_TabContainer_method_get_tab_title>`\ (\ tab_idx\: :ref:`int<class_int>`\ ) |const|                                               |
> +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`       | :ref:`get_tab_tooltip<class_TabContainer_method_get_tab_tooltip>`\ (\ tab_idx\: :ref:`int<class_int>`\ ) |const|                                           |
> +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`           | :ref:`is_tab_disabled<class_TabContainer_method_is_tab_disabled>`\ (\ tab_idx\: :ref:`int<class_int>`\ ) |const|                                           |
> +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`           | :ref:`is_tab_hidden<class_TabContainer_method_is_tab_hidden>`\ (\ tab_idx\: :ref:`int<class_int>`\ ) |const|                                               |
> +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`           | :ref:`select_next_available<class_TabContainer_method_select_next_available>`\ (\ )                                                                        |
> +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`           | :ref:`select_previous_available<class_TabContainer_method_select_previous_available>`\ (\ )                                                                |
> +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                            | :ref:`set_popup<class_TabContainer_method_set_popup>`\ (\ popup\: :ref:`Node<class_Node>`\ )                                                               |
> +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                            | :ref:`set_tab_button_icon<class_TabContainer_method_set_tab_button_icon>`\ (\ tab_idx\: :ref:`int<class_int>`, icon\: :ref:`Texture2D<class_Texture2D>`\ ) |
> +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                            | :ref:`set_tab_disabled<class_TabContainer_method_set_tab_disabled>`\ (\ tab_idx\: :ref:`int<class_int>`, disabled\: :ref:`bool<class_bool>`\ )             |
> +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                            | :ref:`set_tab_hidden<class_TabContainer_method_set_tab_hidden>`\ (\ tab_idx\: :ref:`int<class_int>`, hidden\: :ref:`bool<class_bool>`\ )                   |
> +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                            | :ref:`set_tab_icon<class_TabContainer_method_set_tab_icon>`\ (\ tab_idx\: :ref:`int<class_int>`, icon\: :ref:`Texture2D<class_Texture2D>`\ )               |
> +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                            | :ref:`set_tab_icon_max_width<class_TabContainer_method_set_tab_icon_max_width>`\ (\ tab_idx\: :ref:`int<class_int>`, width\: :ref:`int<class_int>`\ )      |
> +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                            | :ref:`set_tab_metadata<class_TabContainer_method_set_tab_metadata>`\ (\ tab_idx\: :ref:`int<class_int>`, metadata\: :ref:`Variant<class_Variant>`\ )       |
> +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                            | :ref:`set_tab_title<class_TabContainer_method_set_tab_title>`\ (\ tab_idx\: :ref:`int<class_int>`, title\: :ref:`String<class_String>`\ )                  |
> +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                            | :ref:`set_tab_tooltip<class_TabContainer_method_set_tab_tooltip>`\ (\ tab_idx\: :ref:`int<class_int>`, tooltip\: :ref:`String<class_String>`\ )            |
> +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

## Theme Properties

> **TABLE**
> :widths: auto
>
> +-----------------------------------+------------------------------------------------------------------------------------+-------------------------------------+
> | :ref:`Color<class_Color>`         | :ref:`drop_mark_color<class_TabContainer_theme_color_drop_mark_color>`             | ``Color(1, 1, 1, 1)``               |
> +-----------------------------------+------------------------------------------------------------------------------------+-------------------------------------+
> | :ref:`Color<class_Color>`         | :ref:`font_disabled_color<class_TabContainer_theme_color_font_disabled_color>`     | ``Color(0.875, 0.875, 0.875, 0.5)`` |
> +-----------------------------------+------------------------------------------------------------------------------------+-------------------------------------+
> | :ref:`Color<class_Color>`         | :ref:`font_hovered_color<class_TabContainer_theme_color_font_hovered_color>`       | ``Color(0.95, 0.95, 0.95, 1)``      |
> +-----------------------------------+------------------------------------------------------------------------------------+-------------------------------------+
> | :ref:`Color<class_Color>`         | :ref:`font_outline_color<class_TabContainer_theme_color_font_outline_color>`       | ``Color(0, 0, 0, 1)``               |
> +-----------------------------------+------------------------------------------------------------------------------------+-------------------------------------+
> | :ref:`Color<class_Color>`         | :ref:`font_selected_color<class_TabContainer_theme_color_font_selected_color>`     | ``Color(0.95, 0.95, 0.95, 1)``      |
> +-----------------------------------+------------------------------------------------------------------------------------+-------------------------------------+
> | :ref:`Color<class_Color>`         | :ref:`font_unselected_color<class_TabContainer_theme_color_font_unselected_color>` | ``Color(0.7, 0.7, 0.7, 1)``         |
> +-----------------------------------+------------------------------------------------------------------------------------+-------------------------------------+
> | :ref:`Color<class_Color>`         | :ref:`icon_disabled_color<class_TabContainer_theme_color_icon_disabled_color>`     | ``Color(1, 1, 1, 1)``               |
> +-----------------------------------+------------------------------------------------------------------------------------+-------------------------------------+
> | :ref:`Color<class_Color>`         | :ref:`icon_hovered_color<class_TabContainer_theme_color_icon_hovered_color>`       | ``Color(1, 1, 1, 1)``               |
> +-----------------------------------+------------------------------------------------------------------------------------+-------------------------------------+
> | :ref:`Color<class_Color>`         | :ref:`icon_selected_color<class_TabContainer_theme_color_icon_selected_color>`     | ``Color(1, 1, 1, 1)``               |
> +-----------------------------------+------------------------------------------------------------------------------------+-------------------------------------+
> | :ref:`Color<class_Color>`         | :ref:`icon_unselected_color<class_TabContainer_theme_color_icon_unselected_color>` | ``Color(1, 1, 1, 1)``               |
> +-----------------------------------+------------------------------------------------------------------------------------+-------------------------------------+
> | :ref:`int<class_int>`             | :ref:`icon_max_width<class_TabContainer_theme_constant_icon_max_width>`            | ``0``                               |
> +-----------------------------------+------------------------------------------------------------------------------------+-------------------------------------+
> | :ref:`int<class_int>`             | :ref:`icon_separation<class_TabContainer_theme_constant_icon_separation>`          | ``4``                               |
> +-----------------------------------+------------------------------------------------------------------------------------+-------------------------------------+
> | :ref:`int<class_int>`             | :ref:`outline_size<class_TabContainer_theme_constant_outline_size>`                | ``0``                               |
> +-----------------------------------+------------------------------------------------------------------------------------+-------------------------------------+
> | :ref:`int<class_int>`             | :ref:`side_margin<class_TabContainer_theme_constant_side_margin>`                  | ``8``                               |
> +-----------------------------------+------------------------------------------------------------------------------------+-------------------------------------+
> | :ref:`int<class_int>`             | :ref:`tab_separation<class_TabContainer_theme_constant_tab_separation>`            | ``0``                               |
> +-----------------------------------+------------------------------------------------------------------------------------+-------------------------------------+
> | :ref:`Font<class_Font>`           | :ref:`font<class_TabContainer_theme_font_font>`                                    |                                     |
> +-----------------------------------+------------------------------------------------------------------------------------+-------------------------------------+
> | :ref:`int<class_int>`             | :ref:`font_size<class_TabContainer_theme_font_size_font_size>`                     |                                     |
> +-----------------------------------+------------------------------------------------------------------------------------+-------------------------------------+
> | :ref:`Texture2D<class_Texture2D>` | :ref:`decrement<class_TabContainer_theme_icon_decrement>`                          |                                     |
> +-----------------------------------+------------------------------------------------------------------------------------+-------------------------------------+
> | :ref:`Texture2D<class_Texture2D>` | :ref:`decrement_highlight<class_TabContainer_theme_icon_decrement_highlight>`      |                                     |
> +-----------------------------------+------------------------------------------------------------------------------------+-------------------------------------+
> | :ref:`Texture2D<class_Texture2D>` | :ref:`drop_mark<class_TabContainer_theme_icon_drop_mark>`                          |                                     |
> +-----------------------------------+------------------------------------------------------------------------------------+-------------------------------------+
> | :ref:`Texture2D<class_Texture2D>` | :ref:`increment<class_TabContainer_theme_icon_increment>`                          |                                     |
> +-----------------------------------+------------------------------------------------------------------------------------+-------------------------------------+
> | :ref:`Texture2D<class_Texture2D>` | :ref:`increment_highlight<class_TabContainer_theme_icon_increment_highlight>`      |                                     |
> +-----------------------------------+------------------------------------------------------------------------------------+-------------------------------------+
> | :ref:`Texture2D<class_Texture2D>` | :ref:`menu<class_TabContainer_theme_icon_menu>`                                    |                                     |
> +-----------------------------------+------------------------------------------------------------------------------------+-------------------------------------+
> | :ref:`Texture2D<class_Texture2D>` | :ref:`menu_highlight<class_TabContainer_theme_icon_menu_highlight>`                |                                     |
> +-----------------------------------+------------------------------------------------------------------------------------+-------------------------------------+
> | :ref:`StyleBox<class_StyleBox>`   | :ref:`panel<class_TabContainer_theme_style_panel>`                                 |                                     |
> +-----------------------------------+------------------------------------------------------------------------------------+-------------------------------------+
> | :ref:`StyleBox<class_StyleBox>`   | :ref:`tab_disabled<class_TabContainer_theme_style_tab_disabled>`                   |                                     |
> +-----------------------------------+------------------------------------------------------------------------------------+-------------------------------------+
> | :ref:`StyleBox<class_StyleBox>`   | :ref:`tab_focus<class_TabContainer_theme_style_tab_focus>`                         |                                     |
> +-----------------------------------+------------------------------------------------------------------------------------+-------------------------------------+
> | :ref:`StyleBox<class_StyleBox>`   | :ref:`tab_hovered<class_TabContainer_theme_style_tab_hovered>`                     |                                     |
> +-----------------------------------+------------------------------------------------------------------------------------+-------------------------------------+
> | :ref:`StyleBox<class_StyleBox>`   | :ref:`tab_selected<class_TabContainer_theme_style_tab_selected>`                   |                                     |
> +-----------------------------------+------------------------------------------------------------------------------------+-------------------------------------+
> | :ref:`StyleBox<class_StyleBox>`   | :ref:`tab_unselected<class_TabContainer_theme_style_tab_unselected>`               |                                     |
> +-----------------------------------+------------------------------------------------------------------------------------+-------------------------------------+
> | :ref:`StyleBox<class_StyleBox>`   | :ref:`tabbar_background<class_TabContainer_theme_style_tabbar_background>`         |                                     |
> +-----------------------------------+------------------------------------------------------------------------------------+-------------------------------------+
>

----


## Signals



**active_tab_rearranged**\ (\ idx_to\: [int<class_int>]\ ) [🔗<class_TabContainer_signal_active_tab_rearranged>]

Emitted when the active tab is rearranged via mouse drag. See [drag_to_rearrange_enabled<class_TabContainer_property_drag_to_rearrange_enabled>].


----



**pre_popup_pressed**\ (\ ) [🔗<class_TabContainer_signal_pre_popup_pressed>]

Emitted when the **TabContainer**'s [Popup<class_Popup>] button is clicked. See [set_popup()<class_TabContainer_method_set_popup>] for details.


----



**tab_button_pressed**\ (\ tab\: [int<class_int>]\ ) [🔗<class_TabContainer_signal_tab_button_pressed>]

Emitted when the user clicks on the button icon on this tab.


----



**tab_changed**\ (\ tab\: [int<class_int>]\ ) [🔗<class_TabContainer_signal_tab_changed>]

Emitted when switching to another tab.


----



**tab_clicked**\ (\ tab\: [int<class_int>]\ ) [🔗<class_TabContainer_signal_tab_clicked>]

Emitted when a tab is clicked, even if it is the current tab.


----



**tab_hovered**\ (\ tab\: [int<class_int>]\ ) [🔗<class_TabContainer_signal_tab_hovered>]

Emitted when a tab is hovered by the mouse.


----



**tab_selected**\ (\ tab\: [int<class_int>]\ ) [🔗<class_TabContainer_signal_tab_selected>]

Emitted when a tab is selected via click, directional input, or script, even if it is the current tab.


----


## Enumerations



enum **TabPosition**: [🔗<enum_TabContainer_TabPosition>]



[TabPosition<enum_TabContainer_TabPosition>] **POSITION_TOP** = `0`

Places the tab bar at the top.



[TabPosition<enum_TabContainer_TabPosition>] **POSITION_BOTTOM** = `1`

Places the tab bar at the bottom. The tab bar's [StyleBox<class_StyleBox>] will be flipped vertically.



[TabPosition<enum_TabContainer_TabPosition>] **POSITION_MAX** = `2`

Represents the size of the [TabPosition<enum_TabContainer_TabPosition>] enum.


----


## Property Descriptions



[bool<class_bool>] **all_tabs_in_front** = `false` [🔗<class_TabContainer_property_all_tabs_in_front>]


- |void| **set_all_tabs_in_front**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_all_tabs_in_front**\ (\ )

If `true`, all tabs are drawn in front of the panel. If `false`, inactive tabs are drawn behind the panel.


----



[bool<class_bool>] **clip_tabs** = `true` [🔗<class_TabContainer_property_clip_tabs>]


- |void| **set_clip_tabs**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_clip_tabs**\ (\ )

If `true`, tabs overflowing this node's width will be hidden, displaying two navigation buttons instead. Otherwise, this node's minimum size is updated so that all tabs are visible.


----



[int<class_int>] **current_tab** = `-1` [🔗<class_TabContainer_property_current_tab>]


- |void| **set_current_tab**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_current_tab**\ (\ )

The current tab index. When set, this index's [Control<class_Control>] node's `visible` property is set to `true` and all others are set to `false`.

A value of `-1` means that no tab is selected.


----



[bool<class_bool>] **deselect_enabled** = `false` [🔗<class_TabContainer_property_deselect_enabled>]


- |void| **set_deselect_enabled**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_deselect_enabled**\ (\ )

If `true`, all tabs can be deselected so that no tab is selected. Click on the [current_tab<class_TabContainer_property_current_tab>] to deselect it.

Only the tab header will be shown if no tabs are selected.


----



[bool<class_bool>] **drag_to_rearrange_enabled** = `false` [🔗<class_TabContainer_property_drag_to_rearrange_enabled>]


- |void| **set_drag_to_rearrange_enabled**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_drag_to_rearrange_enabled**\ (\ )

If `true`, tabs can be rearranged with mouse drag.


----



[bool<class_bool>] **switch_on_drag_hover** = `true` [🔗<class_TabContainer_property_switch_on_drag_hover>]


- |void| **set_switch_on_drag_hover**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_switch_on_drag_hover**\ (\ )

If `true`, hovering over a tab while dragging something will switch to that tab. Does not have effect when hovering another tab to rearrange.


----



[AlignmentMode<enum_TabBar_AlignmentMode>] **tab_alignment** = `0` [🔗<class_TabContainer_property_tab_alignment>]


- |void| **set_tab_alignment**\ (\ value\: [AlignmentMode<enum_TabBar_AlignmentMode>]\ )
- [AlignmentMode<enum_TabBar_AlignmentMode>] **get_tab_alignment**\ (\ )

The position at which tabs will be placed.


----



[FocusMode<enum_Control_FocusMode>] **tab_focus_mode** = `2` [🔗<class_TabContainer_property_tab_focus_mode>]


- |void| **set_tab_focus_mode**\ (\ value\: [FocusMode<enum_Control_FocusMode>]\ )
- [FocusMode<enum_Control_FocusMode>] **get_tab_focus_mode**\ (\ )

The focus access mode for the internal [TabBar<class_TabBar>] node.


----



[TabPosition<enum_TabContainer_TabPosition>] **tabs_position** = `0` [🔗<class_TabContainer_property_tabs_position>]


- |void| **set_tabs_position**\ (\ value\: [TabPosition<enum_TabContainer_TabPosition>]\ )
- [TabPosition<enum_TabContainer_TabPosition>] **get_tabs_position**\ (\ )

The horizontal alignment of the tabs.


----



[int<class_int>] **tabs_rearrange_group** = `-1` [🔗<class_TabContainer_property_tabs_rearrange_group>]


- |void| **set_tabs_rearrange_group**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_tabs_rearrange_group**\ (\ )

**TabContainer**\ s with the same rearrange group ID will allow dragging the tabs between them. Enable drag with [drag_to_rearrange_enabled<class_TabContainer_property_drag_to_rearrange_enabled>].

Setting this to `-1` will disable rearranging between **TabContainer**\ s.


----



[bool<class_bool>] **tabs_visible** = `true` [🔗<class_TabContainer_property_tabs_visible>]


- |void| **set_tabs_visible**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **are_tabs_visible**\ (\ )

If `true`, tabs are visible. If `false`, tabs' content and titles are hidden.


----



[bool<class_bool>] **use_hidden_tabs_for_min_size** = `false` [🔗<class_TabContainer_property_use_hidden_tabs_for_min_size>]


- |void| **set_use_hidden_tabs_for_min_size**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_use_hidden_tabs_for_min_size**\ (\ )

If `true`, child [Control<class_Control>] nodes that are hidden have their minimum size take into account in the total, instead of only the currently visible one.


----


## Method Descriptions



[Control<class_Control>] **get_current_tab_control**\ (\ ) |const| [🔗<class_TabContainer_method_get_current_tab_control>]

Returns the child [Control<class_Control>] node located at the active tab index.


----



[Popup<class_Popup>] **get_popup**\ (\ ) |const| [🔗<class_TabContainer_method_get_popup>]

Returns the [Popup<class_Popup>] node instance if one has been set already with [set_popup()<class_TabContainer_method_set_popup>].

\ **Warning:** This is a required internal node, removing and freeing it may cause a crash. If you wish to hide it or any of its children, use their [Window.visible<class_Window_property_visible>] property.


----



[int<class_int>] **get_previous_tab**\ (\ ) |const| [🔗<class_TabContainer_method_get_previous_tab>]

Returns the previously active tab index.


----



[TabBar<class_TabBar>] **get_tab_bar**\ (\ ) |const| [🔗<class_TabContainer_method_get_tab_bar>]

Returns the [TabBar<class_TabBar>] contained in this container.

\ **Warning:** This is a required internal node, removing and freeing it or editing its tabs may cause a crash. If you wish to edit the tabs, use the methods provided in **TabContainer**.


----



[Texture2D<class_Texture2D>] **get_tab_button_icon**\ (\ tab_idx\: [int<class_int>]\ ) |const| [🔗<class_TabContainer_method_get_tab_button_icon>]

Returns the button icon from the tab at index `tab_idx`.


----



[Control<class_Control>] **get_tab_control**\ (\ tab_idx\: [int<class_int>]\ ) |const| [🔗<class_TabContainer_method_get_tab_control>]

Returns the [Control<class_Control>] node from the tab at index `tab_idx`.


----



[int<class_int>] **get_tab_count**\ (\ ) |const| [🔗<class_TabContainer_method_get_tab_count>]

Returns the number of tabs.


----



[Texture2D<class_Texture2D>] **get_tab_icon**\ (\ tab_idx\: [int<class_int>]\ ) |const| [🔗<class_TabContainer_method_get_tab_icon>]

Returns the [Texture2D<class_Texture2D>] for the tab at index `tab_idx` or `null` if the tab has no [Texture2D<class_Texture2D>].


----



[int<class_int>] **get_tab_icon_max_width**\ (\ tab_idx\: [int<class_int>]\ ) |const| [🔗<class_TabContainer_method_get_tab_icon_max_width>]

Returns the maximum allowed width of the icon for the tab at index `tab_idx`.


----



[int<class_int>] **get_tab_idx_at_point**\ (\ point\: [Vector2<class_Vector2>]\ ) |const| [🔗<class_TabContainer_method_get_tab_idx_at_point>]

Returns the index of the tab at local coordinates `point`. Returns `-1` if the point is outside the control boundaries or if there's no tab at the queried position.


----



[int<class_int>] **get_tab_idx_from_control**\ (\ control\: [Control<class_Control>]\ ) |const| [🔗<class_TabContainer_method_get_tab_idx_from_control>]

Returns the index of the tab tied to the given `control`. The control must be a child of the **TabContainer**.


----



[Variant<class_Variant>] **get_tab_metadata**\ (\ tab_idx\: [int<class_int>]\ ) |const| [🔗<class_TabContainer_method_get_tab_metadata>]

Returns the metadata value set to the tab at index `tab_idx` using [set_tab_metadata()<class_TabContainer_method_set_tab_metadata>]. If no metadata was previously set, returns `null` by default.


----



[String<class_String>] **get_tab_title**\ (\ tab_idx\: [int<class_int>]\ ) |const| [🔗<class_TabContainer_method_get_tab_title>]

Returns the title of the tab at index `tab_idx`. Tab titles default to the name of the indexed child node, but this can be overridden with [set_tab_title()<class_TabContainer_method_set_tab_title>].


----



[String<class_String>] **get_tab_tooltip**\ (\ tab_idx\: [int<class_int>]\ ) |const| [🔗<class_TabContainer_method_get_tab_tooltip>]

Returns the tooltip text of the tab at index `tab_idx`.


----



[bool<class_bool>] **is_tab_disabled**\ (\ tab_idx\: [int<class_int>]\ ) |const| [🔗<class_TabContainer_method_is_tab_disabled>]

Returns `true` if the tab at index `tab_idx` is disabled.


----



[bool<class_bool>] **is_tab_hidden**\ (\ tab_idx\: [int<class_int>]\ ) |const| [🔗<class_TabContainer_method_is_tab_hidden>]

Returns `true` if the tab at index `tab_idx` is hidden.


----



[bool<class_bool>] **select_next_available**\ (\ ) [🔗<class_TabContainer_method_select_next_available>]

Selects the first available tab with greater index than the currently selected. Returns `true` if tab selection changed.


----



[bool<class_bool>] **select_previous_available**\ (\ ) [🔗<class_TabContainer_method_select_previous_available>]

Selects the first available tab with lower index than the currently selected. Returns `true` if tab selection changed.


----



|void| **set_popup**\ (\ popup\: [Node<class_Node>]\ ) [🔗<class_TabContainer_method_set_popup>]

If set on a [Popup<class_Popup>] node instance, a popup menu icon appears in the top-right corner of the **TabContainer** (setting it to `null` will make it go away). Clicking it will expand the [Popup<class_Popup>] node.


----



|void| **set_tab_button_icon**\ (\ tab_idx\: [int<class_int>], icon\: [Texture2D<class_Texture2D>]\ ) [🔗<class_TabContainer_method_set_tab_button_icon>]

Sets the button icon from the tab at index `tab_idx`.


----



|void| **set_tab_disabled**\ (\ tab_idx\: [int<class_int>], disabled\: [bool<class_bool>]\ ) [🔗<class_TabContainer_method_set_tab_disabled>]

If `disabled` is `true`, disables the tab at index `tab_idx`, making it non-interactable.


----



|void| **set_tab_hidden**\ (\ tab_idx\: [int<class_int>], hidden\: [bool<class_bool>]\ ) [🔗<class_TabContainer_method_set_tab_hidden>]

If `hidden` is `true`, hides the tab at index `tab_idx`, making it disappear from the tab area.


----



|void| **set_tab_icon**\ (\ tab_idx\: [int<class_int>], icon\: [Texture2D<class_Texture2D>]\ ) [🔗<class_TabContainer_method_set_tab_icon>]

Sets an icon for the tab at index `tab_idx`.


----



|void| **set_tab_icon_max_width**\ (\ tab_idx\: [int<class_int>], width\: [int<class_int>]\ ) [🔗<class_TabContainer_method_set_tab_icon_max_width>]

Sets the maximum allowed width of the icon for the tab at index `tab_idx`. This limit is applied on top of the default size of the icon and on top of [icon_max_width<class_TabContainer_theme_constant_icon_max_width>]. The height is adjusted according to the icon's ratio.


----



|void| **set_tab_metadata**\ (\ tab_idx\: [int<class_int>], metadata\: [Variant<class_Variant>]\ ) [🔗<class_TabContainer_method_set_tab_metadata>]

Sets the metadata value for the tab at index `tab_idx`, which can be retrieved later using [get_tab_metadata()<class_TabContainer_method_get_tab_metadata>].


----



|void| **set_tab_title**\ (\ tab_idx\: [int<class_int>], title\: [String<class_String>]\ ) [🔗<class_TabContainer_method_set_tab_title>]

Sets a custom title for the tab at index `tab_idx` (tab titles default to the name of the indexed child node). Set it back to the child's name to make the tab default to it again.


----



|void| **set_tab_tooltip**\ (\ tab_idx\: [int<class_int>], tooltip\: [String<class_String>]\ ) [🔗<class_TabContainer_method_set_tab_tooltip>]

Sets a custom tooltip text for tab at index `tab_idx`.

\ **Note:** By default, if the `tooltip` is empty and the tab text is truncated (not all characters fit into the tab), the title will be displayed as a tooltip. To hide the tooltip, assign `" "` as the `tooltip` text.


----


## Theme Property Descriptions



[Color<class_Color>] **drop_mark_color** = `Color(1, 1, 1, 1)` [🔗<class_TabContainer_theme_color_drop_mark_color>]

Modulation color for the [drop_mark<class_TabContainer_theme_icon_drop_mark>] icon.


----



[Color<class_Color>] **font_disabled_color** = `Color(0.875, 0.875, 0.875, 0.5)` [🔗<class_TabContainer_theme_color_font_disabled_color>]

Font color of disabled tabs.


----



[Color<class_Color>] **font_hovered_color** = `Color(0.95, 0.95, 0.95, 1)` [🔗<class_TabContainer_theme_color_font_hovered_color>]

Font color of the currently hovered tab. Does not apply to the selected tab.


----



[Color<class_Color>] **font_outline_color** = `Color(0, 0, 0, 1)` [🔗<class_TabContainer_theme_color_font_outline_color>]

The tint of text outline of the tab name.


----



[Color<class_Color>] **font_selected_color** = `Color(0.95, 0.95, 0.95, 1)` [🔗<class_TabContainer_theme_color_font_selected_color>]

Font color of the currently selected tab.


----



[Color<class_Color>] **font_unselected_color** = `Color(0.7, 0.7, 0.7, 1)` [🔗<class_TabContainer_theme_color_font_unselected_color>]

Font color of the other, unselected tabs.


----



[Color<class_Color>] **icon_disabled_color** = `Color(1, 1, 1, 1)` [🔗<class_TabContainer_theme_color_icon_disabled_color>]

Icon color of disabled tabs.


----



[Color<class_Color>] **icon_hovered_color** = `Color(1, 1, 1, 1)` [🔗<class_TabContainer_theme_color_icon_hovered_color>]

Icon color of the currently hovered tab. Does not apply to the selected tab.


----



[Color<class_Color>] **icon_selected_color** = `Color(1, 1, 1, 1)` [🔗<class_TabContainer_theme_color_icon_selected_color>]

Icon color of the currently selected tab.


----



[Color<class_Color>] **icon_unselected_color** = `Color(1, 1, 1, 1)` [🔗<class_TabContainer_theme_color_icon_unselected_color>]

Icon color of the other, unselected tabs.


----



[int<class_int>] **icon_max_width** = `0` [🔗<class_TabContainer_theme_constant_icon_max_width>]

The maximum allowed width of the tab's icon. This limit is applied on top of the default size of the icon, but before the value set with [TabBar.set_tab_icon_max_width()<class_TabBar_method_set_tab_icon_max_width>]. The height is adjusted according to the icon's ratio.


----



[int<class_int>] **icon_separation** = `4` [🔗<class_TabContainer_theme_constant_icon_separation>]

Space between tab's name and its icon.


----



[int<class_int>] **outline_size** = `0` [🔗<class_TabContainer_theme_constant_outline_size>]

The size of the tab text outline.

\ **Note:** If using a font with [FontFile.multichannel_signed_distance_field<class_FontFile_property_multichannel_signed_distance_field>] enabled, its [FontFile.msdf_pixel_range<class_FontFile_property_msdf_pixel_range>] must be set to at least *twice* the value of [outline_size<class_TabContainer_theme_constant_outline_size>] for outline rendering to look correct. Otherwise, the outline may appear to be cut off earlier than intended.


----



[int<class_int>] **side_margin** = `8` [🔗<class_TabContainer_theme_constant_side_margin>]

The space at the left or right edges of the tab bar, accordingly with the current [tab_alignment<class_TabContainer_property_tab_alignment>].

The margin is ignored with [TabBar.ALIGNMENT_RIGHT<class_TabBar_constant_ALIGNMENT_RIGHT>] if the tabs are clipped (see [clip_tabs<class_TabContainer_property_clip_tabs>]) or a popup has been set (see [set_popup()<class_TabContainer_method_set_popup>]). The margin is always ignored with [TabBar.ALIGNMENT_CENTER<class_TabBar_constant_ALIGNMENT_CENTER>].


----



[int<class_int>] **tab_separation** = `0` [🔗<class_TabContainer_theme_constant_tab_separation>]

The space between tabs in the tab bar.


----



[Font<class_Font>] **font** [🔗<class_TabContainer_theme_font_font>]

The font used to draw tab names.


----



[int<class_int>] **font_size** [🔗<class_TabContainer_theme_font_size_font_size>]

Font size of the tab names.


----



[Texture2D<class_Texture2D>] **decrement** [🔗<class_TabContainer_theme_icon_decrement>]

Icon for the left arrow button that appears when there are too many tabs to fit in the container width. When the button is disabled (i.e. the first tab is visible), it appears semi-transparent.


----



[Texture2D<class_Texture2D>] **decrement_highlight** [🔗<class_TabContainer_theme_icon_decrement_highlight>]

Icon for the left arrow button that appears when there are too many tabs to fit in the container width. Used when the button is being hovered with the cursor.


----



[Texture2D<class_Texture2D>] **drop_mark** [🔗<class_TabContainer_theme_icon_drop_mark>]

Icon shown to indicate where a dragged tab is gonna be dropped (see [drag_to_rearrange_enabled<class_TabContainer_property_drag_to_rearrange_enabled>]).


----



[Texture2D<class_Texture2D>] **increment** [🔗<class_TabContainer_theme_icon_increment>]

Icon for the right arrow button that appears when there are too many tabs to fit in the container width. When the button is disabled (i.e. the last tab is visible) it appears semi-transparent.


----



[Texture2D<class_Texture2D>] **increment_highlight** [🔗<class_TabContainer_theme_icon_increment_highlight>]

Icon for the right arrow button that appears when there are too many tabs to fit in the container width. Used when the button is being hovered with the cursor.


----



[Texture2D<class_Texture2D>] **menu** [🔗<class_TabContainer_theme_icon_menu>]

The icon for the menu button (see [set_popup()<class_TabContainer_method_set_popup>]).


----



[Texture2D<class_Texture2D>] **menu_highlight** [🔗<class_TabContainer_theme_icon_menu_highlight>]

The icon for the menu button (see [set_popup()<class_TabContainer_method_set_popup>]) when it's being hovered with the cursor.


----



[StyleBox<class_StyleBox>] **panel** [🔗<class_TabContainer_theme_style_panel>]

The style for the background fill.


----



[StyleBox<class_StyleBox>] **tab_disabled** [🔗<class_TabContainer_theme_style_tab_disabled>]

The style of disabled tabs.


----



[StyleBox<class_StyleBox>] **tab_focus** [🔗<class_TabContainer_theme_style_tab_focus>]

[StyleBox<class_StyleBox>] used when the [TabBar<class_TabBar>] is focused. The [tab_focus<class_TabContainer_theme_style_tab_focus>] [StyleBox<class_StyleBox>] is displayed *over* the base [StyleBox<class_StyleBox>] of the selected tab, so a partially transparent [StyleBox<class_StyleBox>] should be used to ensure the base [StyleBox<class_StyleBox>] remains visible. A [StyleBox<class_StyleBox>] that represents an outline or an underline works well for this purpose. To disable the focus visual effect, assign a [StyleBoxEmpty<class_StyleBoxEmpty>] resource. Note that disabling the focus visual effect will harm keyboard/controller navigation usability, so this is not recommended for accessibility reasons.


----



[StyleBox<class_StyleBox>] **tab_hovered** [🔗<class_TabContainer_theme_style_tab_hovered>]

The style of the currently hovered tab.

\ **Note:** This style will be drawn with the same width as [tab_unselected<class_TabContainer_theme_style_tab_unselected>] at minimum.


----



[StyleBox<class_StyleBox>] **tab_selected** [🔗<class_TabContainer_theme_style_tab_selected>]

The style of the currently selected tab.


----



[StyleBox<class_StyleBox>] **tab_unselected** [🔗<class_TabContainer_theme_style_tab_unselected>]

The style of the other, unselected tabs.


----



[StyleBox<class_StyleBox>] **tabbar_background** [🔗<class_TabContainer_theme_style_tabbar_background>]

The style for the background fill of the [TabBar<class_TabBar>] area.

