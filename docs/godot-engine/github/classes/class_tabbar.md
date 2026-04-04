:github_url: hide



# TabBar

**Inherits:** [Control<class_Control>] **<** [CanvasItem<class_CanvasItem>] **<** [Node<class_Node>] **<** [Object<class_Object>]

A control that provides a horizontal bar with tabs.


## Description

A control that provides a horizontal bar with tabs. Similar to [TabContainer<class_TabContainer>] but is only in charge of drawing tabs, not interacting with children.


## Properties

> **TABLE**
> :widths: auto
>
> +-----------------------------------------------------------------------+-----------------------------------------------------------------------------------+---------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                               | :ref:`clip_tabs<class_TabBar_property_clip_tabs>`                                 | ``true``                                                            |
> +-----------------------------------------------------------------------+-----------------------------------------------------------------------------------+---------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                               | :ref:`close_with_middle_mouse<class_TabBar_property_close_with_middle_mouse>`     | ``true``                                                            |
> +-----------------------------------------------------------------------+-----------------------------------------------------------------------------------+---------------------------------------------------------------------+
> | :ref:`int<class_int>`                                                 | :ref:`current_tab<class_TabBar_property_current_tab>`                             | ``-1``                                                              |
> +-----------------------------------------------------------------------+-----------------------------------------------------------------------------------+---------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                               | :ref:`deselect_enabled<class_TabBar_property_deselect_enabled>`                   | ``false``                                                           |
> +-----------------------------------------------------------------------+-----------------------------------------------------------------------------------+---------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                               | :ref:`drag_to_rearrange_enabled<class_TabBar_property_drag_to_rearrange_enabled>` | ``false``                                                           |
> +-----------------------------------------------------------------------+-----------------------------------------------------------------------------------+---------------------------------------------------------------------+
> | :ref:`FocusMode<enum_Control_FocusMode>`                              | focus_mode                                                                        | ``2`` (overrides :ref:`Control<class_Control_property_focus_mode>`) |
> +-----------------------------------------------------------------------+-----------------------------------------------------------------------------------+---------------------------------------------------------------------+
> | :ref:`int<class_int>`                                                 | :ref:`max_tab_width<class_TabBar_property_max_tab_width>`                         | ``0``                                                               |
> +-----------------------------------------------------------------------+-----------------------------------------------------------------------------------+---------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                               | :ref:`scroll_to_selected<class_TabBar_property_scroll_to_selected>`               | ``true``                                                            |
> +-----------------------------------------------------------------------+-----------------------------------------------------------------------------------+---------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                               | :ref:`scrolling_enabled<class_TabBar_property_scrolling_enabled>`                 | ``true``                                                            |
> +-----------------------------------------------------------------------+-----------------------------------------------------------------------------------+---------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                               | :ref:`select_with_rmb<class_TabBar_property_select_with_rmb>`                     | ``false``                                                           |
> +-----------------------------------------------------------------------+-----------------------------------------------------------------------------------+---------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                               | :ref:`switch_on_drag_hover<class_TabBar_property_switch_on_drag_hover>`           | ``true``                                                            |
> +-----------------------------------------------------------------------+-----------------------------------------------------------------------------------+---------------------------------------------------------------------+
> | :ref:`AlignmentMode<enum_TabBar_AlignmentMode>`                       | :ref:`tab_alignment<class_TabBar_property_tab_alignment>`                         | ``0``                                                               |
> +-----------------------------------------------------------------------+-----------------------------------------------------------------------------------+---------------------------------------------------------------------+
> | :ref:`CloseButtonDisplayPolicy<enum_TabBar_CloseButtonDisplayPolicy>` | :ref:`tab_close_display_policy<class_TabBar_property_tab_close_display_policy>`   | ``0``                                                               |
> +-----------------------------------------------------------------------+-----------------------------------------------------------------------------------+---------------------------------------------------------------------+
> | :ref:`int<class_int>`                                                 | :ref:`tab_count<class_TabBar_property_tab_count>`                                 | ``0``                                                               |
> +-----------------------------------------------------------------------+-----------------------------------------------------------------------------------+---------------------------------------------------------------------+
> | :ref:`int<class_int>`                                                 | :ref:`tabs_rearrange_group<class_TabBar_property_tabs_rearrange_group>`           | ``-1``                                                              |
> +-----------------------------------------------------------------------+-----------------------------------------------------------------------------------+---------------------------------------------------------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +--------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                           | :ref:`add_tab<class_TabBar_method_add_tab>`\ (\ title\: :ref:`String<class_String>` = "", icon\: :ref:`Texture2D<class_Texture2D>` = null\ )                                   |
> +--------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                           | :ref:`clear_tabs<class_TabBar_method_clear_tabs>`\ (\ )                                                                                                                        |
> +--------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                           | :ref:`ensure_tab_visible<class_TabBar_method_ensure_tab_visible>`\ (\ idx\: :ref:`int<class_int>`\ )                                                                           |
> +--------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                          | :ref:`get_offset_buttons_visible<class_TabBar_method_get_offset_buttons_visible>`\ (\ ) |const|                                                                                |
> +--------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                            | :ref:`get_previous_tab<class_TabBar_method_get_previous_tab>`\ (\ ) |const|                                                                                                    |
> +--------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Texture2D<class_Texture2D>`                | :ref:`get_tab_button_icon<class_TabBar_method_get_tab_button_icon>`\ (\ tab_idx\: :ref:`int<class_int>`\ ) |const|                                                             |
> +--------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Texture2D<class_Texture2D>`                | :ref:`get_tab_icon<class_TabBar_method_get_tab_icon>`\ (\ tab_idx\: :ref:`int<class_int>`\ ) |const|                                                                           |
> +--------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                            | :ref:`get_tab_icon_max_width<class_TabBar_method_get_tab_icon_max_width>`\ (\ tab_idx\: :ref:`int<class_int>`\ ) |const|                                                       |
> +--------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                            | :ref:`get_tab_idx_at_point<class_TabBar_method_get_tab_idx_at_point>`\ (\ point\: :ref:`Vector2<class_Vector2>`\ ) |const|                                                     |
> +--------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`                      | :ref:`get_tab_language<class_TabBar_method_get_tab_language>`\ (\ tab_idx\: :ref:`int<class_int>`\ ) |const|                                                                   |
> +--------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Variant<class_Variant>`                    | :ref:`get_tab_metadata<class_TabBar_method_get_tab_metadata>`\ (\ tab_idx\: :ref:`int<class_int>`\ ) |const|                                                                   |
> +--------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                            | :ref:`get_tab_offset<class_TabBar_method_get_tab_offset>`\ (\ ) |const|                                                                                                        |
> +--------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Rect2<class_Rect2>`                        | :ref:`get_tab_rect<class_TabBar_method_get_tab_rect>`\ (\ tab_idx\: :ref:`int<class_int>`\ ) |const|                                                                           |
> +--------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`TextDirection<enum_Control_TextDirection>` | :ref:`get_tab_text_direction<class_TabBar_method_get_tab_text_direction>`\ (\ tab_idx\: :ref:`int<class_int>`\ ) |const|                                                       |
> +--------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`                      | :ref:`get_tab_title<class_TabBar_method_get_tab_title>`\ (\ tab_idx\: :ref:`int<class_int>`\ ) |const|                                                                         |
> +--------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`                      | :ref:`get_tab_tooltip<class_TabBar_method_get_tab_tooltip>`\ (\ tab_idx\: :ref:`int<class_int>`\ ) |const|                                                                     |
> +--------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                          | :ref:`is_tab_disabled<class_TabBar_method_is_tab_disabled>`\ (\ tab_idx\: :ref:`int<class_int>`\ ) |const|                                                                     |
> +--------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                          | :ref:`is_tab_hidden<class_TabBar_method_is_tab_hidden>`\ (\ tab_idx\: :ref:`int<class_int>`\ ) |const|                                                                         |
> +--------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                           | :ref:`move_tab<class_TabBar_method_move_tab>`\ (\ from\: :ref:`int<class_int>`, to\: :ref:`int<class_int>`\ )                                                                  |
> +--------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                           | :ref:`remove_tab<class_TabBar_method_remove_tab>`\ (\ tab_idx\: :ref:`int<class_int>`\ )                                                                                       |
> +--------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                          | :ref:`select_next_available<class_TabBar_method_select_next_available>`\ (\ )                                                                                                  |
> +--------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                          | :ref:`select_previous_available<class_TabBar_method_select_previous_available>`\ (\ )                                                                                          |
> +--------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                           | :ref:`set_tab_button_icon<class_TabBar_method_set_tab_button_icon>`\ (\ tab_idx\: :ref:`int<class_int>`, icon\: :ref:`Texture2D<class_Texture2D>`\ )                           |
> +--------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                           | :ref:`set_tab_disabled<class_TabBar_method_set_tab_disabled>`\ (\ tab_idx\: :ref:`int<class_int>`, disabled\: :ref:`bool<class_bool>`\ )                                       |
> +--------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                           | :ref:`set_tab_hidden<class_TabBar_method_set_tab_hidden>`\ (\ tab_idx\: :ref:`int<class_int>`, hidden\: :ref:`bool<class_bool>`\ )                                             |
> +--------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                           | :ref:`set_tab_icon<class_TabBar_method_set_tab_icon>`\ (\ tab_idx\: :ref:`int<class_int>`, icon\: :ref:`Texture2D<class_Texture2D>`\ )                                         |
> +--------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                           | :ref:`set_tab_icon_max_width<class_TabBar_method_set_tab_icon_max_width>`\ (\ tab_idx\: :ref:`int<class_int>`, width\: :ref:`int<class_int>`\ )                                |
> +--------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                           | :ref:`set_tab_language<class_TabBar_method_set_tab_language>`\ (\ tab_idx\: :ref:`int<class_int>`, language\: :ref:`String<class_String>`\ )                                   |
> +--------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                           | :ref:`set_tab_metadata<class_TabBar_method_set_tab_metadata>`\ (\ tab_idx\: :ref:`int<class_int>`, metadata\: :ref:`Variant<class_Variant>`\ )                                 |
> +--------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                           | :ref:`set_tab_text_direction<class_TabBar_method_set_tab_text_direction>`\ (\ tab_idx\: :ref:`int<class_int>`, direction\: :ref:`TextDirection<enum_Control_TextDirection>`\ ) |
> +--------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                           | :ref:`set_tab_title<class_TabBar_method_set_tab_title>`\ (\ tab_idx\: :ref:`int<class_int>`, title\: :ref:`String<class_String>`\ )                                            |
> +--------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                           | :ref:`set_tab_tooltip<class_TabBar_method_set_tab_tooltip>`\ (\ tab_idx\: :ref:`int<class_int>`, tooltip\: :ref:`String<class_String>`\ )                                      |
> +--------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

## Theme Properties

> **TABLE**
> :widths: auto
>
> +-----------------------------------+-----------------------------------------------------------------------------------+-------------------------------------+
> | :ref:`Color<class_Color>`         | :ref:`drop_mark_color<class_TabBar_theme_color_drop_mark_color>`                  | ``Color(1, 1, 1, 1)``               |
> +-----------------------------------+-----------------------------------------------------------------------------------+-------------------------------------+
> | :ref:`Color<class_Color>`         | :ref:`font_disabled_color<class_TabBar_theme_color_font_disabled_color>`          | ``Color(0.875, 0.875, 0.875, 0.5)`` |
> +-----------------------------------+-----------------------------------------------------------------------------------+-------------------------------------+
> | :ref:`Color<class_Color>`         | :ref:`font_hovered_color<class_TabBar_theme_color_font_hovered_color>`            | ``Color(0.95, 0.95, 0.95, 1)``      |
> +-----------------------------------+-----------------------------------------------------------------------------------+-------------------------------------+
> | :ref:`Color<class_Color>`         | :ref:`font_outline_color<class_TabBar_theme_color_font_outline_color>`            | ``Color(0, 0, 0, 1)``               |
> +-----------------------------------+-----------------------------------------------------------------------------------+-------------------------------------+
> | :ref:`Color<class_Color>`         | :ref:`font_selected_color<class_TabBar_theme_color_font_selected_color>`          | ``Color(0.95, 0.95, 0.95, 1)``      |
> +-----------------------------------+-----------------------------------------------------------------------------------+-------------------------------------+
> | :ref:`Color<class_Color>`         | :ref:`font_unselected_color<class_TabBar_theme_color_font_unselected_color>`      | ``Color(0.7, 0.7, 0.7, 1)``         |
> +-----------------------------------+-----------------------------------------------------------------------------------+-------------------------------------+
> | :ref:`Color<class_Color>`         | :ref:`icon_disabled_color<class_TabBar_theme_color_icon_disabled_color>`          | ``Color(1, 1, 1, 1)``               |
> +-----------------------------------+-----------------------------------------------------------------------------------+-------------------------------------+
> | :ref:`Color<class_Color>`         | :ref:`icon_hovered_color<class_TabBar_theme_color_icon_hovered_color>`            | ``Color(1, 1, 1, 1)``               |
> +-----------------------------------+-----------------------------------------------------------------------------------+-------------------------------------+
> | :ref:`Color<class_Color>`         | :ref:`icon_selected_color<class_TabBar_theme_color_icon_selected_color>`          | ``Color(1, 1, 1, 1)``               |
> +-----------------------------------+-----------------------------------------------------------------------------------+-------------------------------------+
> | :ref:`Color<class_Color>`         | :ref:`icon_unselected_color<class_TabBar_theme_color_icon_unselected_color>`      | ``Color(1, 1, 1, 1)``               |
> +-----------------------------------+-----------------------------------------------------------------------------------+-------------------------------------+
> | :ref:`int<class_int>`             | :ref:`h_separation<class_TabBar_theme_constant_h_separation>`                     | ``4``                               |
> +-----------------------------------+-----------------------------------------------------------------------------------+-------------------------------------+
> | :ref:`int<class_int>`             | :ref:`hover_switch_wait_msec<class_TabBar_theme_constant_hover_switch_wait_msec>` | ``500``                             |
> +-----------------------------------+-----------------------------------------------------------------------------------+-------------------------------------+
> | :ref:`int<class_int>`             | :ref:`icon_max_width<class_TabBar_theme_constant_icon_max_width>`                 | ``0``                               |
> +-----------------------------------+-----------------------------------------------------------------------------------+-------------------------------------+
> | :ref:`int<class_int>`             | :ref:`outline_size<class_TabBar_theme_constant_outline_size>`                     | ``0``                               |
> +-----------------------------------+-----------------------------------------------------------------------------------+-------------------------------------+
> | :ref:`int<class_int>`             | :ref:`tab_separation<class_TabBar_theme_constant_tab_separation>`                 | ``0``                               |
> +-----------------------------------+-----------------------------------------------------------------------------------+-------------------------------------+
> | :ref:`Font<class_Font>`           | :ref:`font<class_TabBar_theme_font_font>`                                         |                                     |
> +-----------------------------------+-----------------------------------------------------------------------------------+-------------------------------------+
> | :ref:`int<class_int>`             | :ref:`font_size<class_TabBar_theme_font_size_font_size>`                          |                                     |
> +-----------------------------------+-----------------------------------------------------------------------------------+-------------------------------------+
> | :ref:`Texture2D<class_Texture2D>` | :ref:`close<class_TabBar_theme_icon_close>`                                       |                                     |
> +-----------------------------------+-----------------------------------------------------------------------------------+-------------------------------------+
> | :ref:`Texture2D<class_Texture2D>` | :ref:`decrement<class_TabBar_theme_icon_decrement>`                               |                                     |
> +-----------------------------------+-----------------------------------------------------------------------------------+-------------------------------------+
> | :ref:`Texture2D<class_Texture2D>` | :ref:`decrement_highlight<class_TabBar_theme_icon_decrement_highlight>`           |                                     |
> +-----------------------------------+-----------------------------------------------------------------------------------+-------------------------------------+
> | :ref:`Texture2D<class_Texture2D>` | :ref:`drop_mark<class_TabBar_theme_icon_drop_mark>`                               |                                     |
> +-----------------------------------+-----------------------------------------------------------------------------------+-------------------------------------+
> | :ref:`Texture2D<class_Texture2D>` | :ref:`increment<class_TabBar_theme_icon_increment>`                               |                                     |
> +-----------------------------------+-----------------------------------------------------------------------------------+-------------------------------------+
> | :ref:`Texture2D<class_Texture2D>` | :ref:`increment_highlight<class_TabBar_theme_icon_increment_highlight>`           |                                     |
> +-----------------------------------+-----------------------------------------------------------------------------------+-------------------------------------+
> | :ref:`StyleBox<class_StyleBox>`   | :ref:`button_highlight<class_TabBar_theme_style_button_highlight>`                |                                     |
> +-----------------------------------+-----------------------------------------------------------------------------------+-------------------------------------+
> | :ref:`StyleBox<class_StyleBox>`   | :ref:`button_pressed<class_TabBar_theme_style_button_pressed>`                    |                                     |
> +-----------------------------------+-----------------------------------------------------------------------------------+-------------------------------------+
> | :ref:`StyleBox<class_StyleBox>`   | :ref:`tab_disabled<class_TabBar_theme_style_tab_disabled>`                        |                                     |
> +-----------------------------------+-----------------------------------------------------------------------------------+-------------------------------------+
> | :ref:`StyleBox<class_StyleBox>`   | :ref:`tab_focus<class_TabBar_theme_style_tab_focus>`                              |                                     |
> +-----------------------------------+-----------------------------------------------------------------------------------+-------------------------------------+
> | :ref:`StyleBox<class_StyleBox>`   | :ref:`tab_hovered<class_TabBar_theme_style_tab_hovered>`                          |                                     |
> +-----------------------------------+-----------------------------------------------------------------------------------+-------------------------------------+
> | :ref:`StyleBox<class_StyleBox>`   | :ref:`tab_selected<class_TabBar_theme_style_tab_selected>`                        |                                     |
> +-----------------------------------+-----------------------------------------------------------------------------------+-------------------------------------+
> | :ref:`StyleBox<class_StyleBox>`   | :ref:`tab_unselected<class_TabBar_theme_style_tab_unselected>`                    |                                     |
> +-----------------------------------+-----------------------------------------------------------------------------------+-------------------------------------+
>

----


## Signals



**active_tab_rearranged**\ (\ idx_to\: [int<class_int>]\ ) [🔗<class_TabBar_signal_active_tab_rearranged>]

Emitted when the active tab is rearranged via mouse drag. See [drag_to_rearrange_enabled<class_TabBar_property_drag_to_rearrange_enabled>].


----



**tab_button_pressed**\ (\ tab\: [int<class_int>]\ ) [🔗<class_TabBar_signal_tab_button_pressed>]

Emitted when a tab's right button is pressed. See [set_tab_button_icon()<class_TabBar_method_set_tab_button_icon>].


----



**tab_changed**\ (\ tab\: [int<class_int>]\ ) [🔗<class_TabBar_signal_tab_changed>]

Emitted when switching to another tab.


----



**tab_clicked**\ (\ tab\: [int<class_int>]\ ) [🔗<class_TabBar_signal_tab_clicked>]

Emitted when a tab is clicked, even if it is the current tab.


----



**tab_close_pressed**\ (\ tab\: [int<class_int>]\ ) [🔗<class_TabBar_signal_tab_close_pressed>]

Emitted when a tab's close button is pressed or, if [close_with_middle_mouse<class_TabBar_property_close_with_middle_mouse>] is `true`, when middle-clicking on a tab.

\ **Note:** Tabs are not removed automatically; this behavior needs to be coded manually. For example:


> **TABS**
>

    $TabBar.tab_close_pressed.connect($TabBar.remove_tab)


    GetNode<TabBar>("TabBar").TabClosePressed += GetNode<TabBar>("TabBar").RemoveTab;




----



**tab_hovered**\ (\ tab\: [int<class_int>]\ ) [🔗<class_TabBar_signal_tab_hovered>]

Emitted when a tab is hovered by the mouse.


----



**tab_rmb_clicked**\ (\ tab\: [int<class_int>]\ ) [🔗<class_TabBar_signal_tab_rmb_clicked>]

Emitted when a tab is right-clicked.


----



**tab_selected**\ (\ tab\: [int<class_int>]\ ) [🔗<class_TabBar_signal_tab_selected>]

Emitted when a tab is selected via click, directional input, or script, even if it is the current tab.


----


## Enumerations



enum **AlignmentMode**: [🔗<enum_TabBar_AlignmentMode>]



[AlignmentMode<enum_TabBar_AlignmentMode>] **ALIGNMENT_LEFT** = `0`

Aligns tabs to the left.



[AlignmentMode<enum_TabBar_AlignmentMode>] **ALIGNMENT_CENTER** = `1`

Aligns tabs in the middle.



[AlignmentMode<enum_TabBar_AlignmentMode>] **ALIGNMENT_RIGHT** = `2`

Aligns tabs to the right.



[AlignmentMode<enum_TabBar_AlignmentMode>] **ALIGNMENT_MAX** = `3`

Represents the size of the [AlignmentMode<enum_TabBar_AlignmentMode>] enum.


----



enum **CloseButtonDisplayPolicy**: [🔗<enum_TabBar_CloseButtonDisplayPolicy>]



[CloseButtonDisplayPolicy<enum_TabBar_CloseButtonDisplayPolicy>] **CLOSE_BUTTON_SHOW_NEVER** = `0`

Never show the close buttons.



[CloseButtonDisplayPolicy<enum_TabBar_CloseButtonDisplayPolicy>] **CLOSE_BUTTON_SHOW_ACTIVE_ONLY** = `1`

Only show the close button on the currently active tab.



[CloseButtonDisplayPolicy<enum_TabBar_CloseButtonDisplayPolicy>] **CLOSE_BUTTON_SHOW_ALWAYS** = `2`

Show the close button on all tabs.



[CloseButtonDisplayPolicy<enum_TabBar_CloseButtonDisplayPolicy>] **CLOSE_BUTTON_MAX** = `3`

Represents the size of the [CloseButtonDisplayPolicy<enum_TabBar_CloseButtonDisplayPolicy>] enum.


----


## Property Descriptions



[bool<class_bool>] **clip_tabs** = `true` [🔗<class_TabBar_property_clip_tabs>]


- |void| **set_clip_tabs**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_clip_tabs**\ (\ )

If `true`, tabs overflowing this node's width will be hidden, displaying two navigation buttons instead. Otherwise, this node's minimum size is updated so that all tabs are visible.


----



[bool<class_bool>] **close_with_middle_mouse** = `true` [🔗<class_TabBar_property_close_with_middle_mouse>]


- |void| **set_close_with_middle_mouse**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_close_with_middle_mouse**\ (\ )

If `true`, middle-clicking on a tab will emit the [tab_close_pressed<class_TabBar_signal_tab_close_pressed>] signal.


----



[int<class_int>] **current_tab** = `-1` [🔗<class_TabBar_property_current_tab>]


- |void| **set_current_tab**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_current_tab**\ (\ )

The index of the current selected tab. A value of `-1` means that no tab is selected and can only be set when [deselect_enabled<class_TabBar_property_deselect_enabled>] is `true` or if all tabs are hidden or disabled.


----



[bool<class_bool>] **deselect_enabled** = `false` [🔗<class_TabBar_property_deselect_enabled>]


- |void| **set_deselect_enabled**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_deselect_enabled**\ (\ )

If `true`, all tabs can be deselected so that no tab is selected. Click on the current tab to deselect it.


----



[bool<class_bool>] **drag_to_rearrange_enabled** = `false` [🔗<class_TabBar_property_drag_to_rearrange_enabled>]


- |void| **set_drag_to_rearrange_enabled**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_drag_to_rearrange_enabled**\ (\ )

If `true`, tabs can be rearranged with mouse drag.


----



[int<class_int>] **max_tab_width** = `0` [🔗<class_TabBar_property_max_tab_width>]


- |void| **set_max_tab_width**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_max_tab_width**\ (\ )

Sets the maximum width which all tabs should be limited to. Unlimited if set to `0`.


----



[bool<class_bool>] **scroll_to_selected** = `true` [🔗<class_TabBar_property_scroll_to_selected>]


- |void| **set_scroll_to_selected**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_scroll_to_selected**\ (\ )

If `true`, the tab offset will be changed to keep the currently selected tab visible.


----



[bool<class_bool>] **scrolling_enabled** = `true` [🔗<class_TabBar_property_scrolling_enabled>]


- |void| **set_scrolling_enabled**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_scrolling_enabled**\ (\ )

if `true`, the mouse's scroll wheel can be used to navigate the scroll view.


----



[bool<class_bool>] **select_with_rmb** = `false` [🔗<class_TabBar_property_select_with_rmb>]


- |void| **set_select_with_rmb**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_select_with_rmb**\ (\ )

If `true`, enables selecting a tab with the right mouse button.


----



[bool<class_bool>] **switch_on_drag_hover** = `true` [🔗<class_TabBar_property_switch_on_drag_hover>]


- |void| **set_switch_on_drag_hover**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_switch_on_drag_hover**\ (\ )

If `true`, hovering over a tab while dragging something will switch to that tab. Does not have effect when hovering another tab to rearrange. The delay for when this happens is dictated by [hover_switch_wait_msec<class_TabBar_theme_constant_hover_switch_wait_msec>].


----



[AlignmentMode<enum_TabBar_AlignmentMode>] **tab_alignment** = `0` [🔗<class_TabBar_property_tab_alignment>]


- |void| **set_tab_alignment**\ (\ value\: [AlignmentMode<enum_TabBar_AlignmentMode>]\ )
- [AlignmentMode<enum_TabBar_AlignmentMode>] **get_tab_alignment**\ (\ )

The horizontal alignment of the tabs.


----



[CloseButtonDisplayPolicy<enum_TabBar_CloseButtonDisplayPolicy>] **tab_close_display_policy** = `0` [🔗<class_TabBar_property_tab_close_display_policy>]


- |void| **set_tab_close_display_policy**\ (\ value\: [CloseButtonDisplayPolicy<enum_TabBar_CloseButtonDisplayPolicy>]\ )
- [CloseButtonDisplayPolicy<enum_TabBar_CloseButtonDisplayPolicy>] **get_tab_close_display_policy**\ (\ )

When the close button will appear on the tabs.


----



[int<class_int>] **tab_count** = `0` [🔗<class_TabBar_property_tab_count>]


- |void| **set_tab_count**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_tab_count**\ (\ )

The number of tabs currently in the bar.


----



[int<class_int>] **tabs_rearrange_group** = `-1` [🔗<class_TabBar_property_tabs_rearrange_group>]


- |void| **set_tabs_rearrange_group**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_tabs_rearrange_group**\ (\ )

**TabBar**\ s with the same rearrange group ID will allow dragging the tabs between them. Enable drag with [drag_to_rearrange_enabled<class_TabBar_property_drag_to_rearrange_enabled>].

Setting this to `-1` will disable rearranging between **TabBar**\ s.


----


## Method Descriptions



|void| **add_tab**\ (\ title\: [String<class_String>] = "", icon\: [Texture2D<class_Texture2D>] = null\ ) [🔗<class_TabBar_method_add_tab>]

Adds a new tab.


----



|void| **clear_tabs**\ (\ ) [🔗<class_TabBar_method_clear_tabs>]

Clears all tabs.


----



|void| **ensure_tab_visible**\ (\ idx\: [int<class_int>]\ ) [🔗<class_TabBar_method_ensure_tab_visible>]

Moves the scroll view to make the tab visible.


----



[bool<class_bool>] **get_offset_buttons_visible**\ (\ ) |const| [🔗<class_TabBar_method_get_offset_buttons_visible>]

Returns `true` if the offset buttons (the ones that appear when there's not enough space for all tabs) are visible.


----



[int<class_int>] **get_previous_tab**\ (\ ) |const| [🔗<class_TabBar_method_get_previous_tab>]

Returns the previously active tab index.


----



[Texture2D<class_Texture2D>] **get_tab_button_icon**\ (\ tab_idx\: [int<class_int>]\ ) |const| [🔗<class_TabBar_method_get_tab_button_icon>]

Returns the icon for the right button of the tab at index `tab_idx` or `null` if the right button has no icon.


----



[Texture2D<class_Texture2D>] **get_tab_icon**\ (\ tab_idx\: [int<class_int>]\ ) |const| [🔗<class_TabBar_method_get_tab_icon>]

Returns the icon for the tab at index `tab_idx` or `null` if the tab has no icon.


----



[int<class_int>] **get_tab_icon_max_width**\ (\ tab_idx\: [int<class_int>]\ ) |const| [🔗<class_TabBar_method_get_tab_icon_max_width>]

Returns the maximum allowed width of the icon for the tab at index `tab_idx`.


----



[int<class_int>] **get_tab_idx_at_point**\ (\ point\: [Vector2<class_Vector2>]\ ) |const| [🔗<class_TabBar_method_get_tab_idx_at_point>]

Returns the index of the tab at local coordinates `point`. Returns `-1` if the point is outside the control boundaries or if there's no tab at the queried position.


----



[String<class_String>] **get_tab_language**\ (\ tab_idx\: [int<class_int>]\ ) |const| [🔗<class_TabBar_method_get_tab_language>]

Returns tab title language code.


----



[Variant<class_Variant>] **get_tab_metadata**\ (\ tab_idx\: [int<class_int>]\ ) |const| [🔗<class_TabBar_method_get_tab_metadata>]

Returns the metadata value set to the tab at index `tab_idx` using [set_tab_metadata()<class_TabBar_method_set_tab_metadata>]. If no metadata was previously set, returns `null` by default.


----



[int<class_int>] **get_tab_offset**\ (\ ) |const| [🔗<class_TabBar_method_get_tab_offset>]

Returns the number of hidden tabs offsetted to the left.


----



[Rect2<class_Rect2>] **get_tab_rect**\ (\ tab_idx\: [int<class_int>]\ ) |const| [🔗<class_TabBar_method_get_tab_rect>]

Returns tab [Rect2<class_Rect2>] with local position and size.


----



[TextDirection<enum_Control_TextDirection>] **get_tab_text_direction**\ (\ tab_idx\: [int<class_int>]\ ) |const| [🔗<class_TabBar_method_get_tab_text_direction>]

Returns tab title text base writing direction.


----



[String<class_String>] **get_tab_title**\ (\ tab_idx\: [int<class_int>]\ ) |const| [🔗<class_TabBar_method_get_tab_title>]

Returns the title of the tab at index `tab_idx`.


----



[String<class_String>] **get_tab_tooltip**\ (\ tab_idx\: [int<class_int>]\ ) |const| [🔗<class_TabBar_method_get_tab_tooltip>]

Returns the tooltip text of the tab at index `tab_idx`.


----



[bool<class_bool>] **is_tab_disabled**\ (\ tab_idx\: [int<class_int>]\ ) |const| [🔗<class_TabBar_method_is_tab_disabled>]

Returns `true` if the tab at index `tab_idx` is disabled.


----



[bool<class_bool>] **is_tab_hidden**\ (\ tab_idx\: [int<class_int>]\ ) |const| [🔗<class_TabBar_method_is_tab_hidden>]

Returns `true` if the tab at index `tab_idx` is hidden.


----



|void| **move_tab**\ (\ from\: [int<class_int>], to\: [int<class_int>]\ ) [🔗<class_TabBar_method_move_tab>]

Moves a tab from `from` to `to`.


----



|void| **remove_tab**\ (\ tab_idx\: [int<class_int>]\ ) [🔗<class_TabBar_method_remove_tab>]

Removes the tab at index `tab_idx`.


----



[bool<class_bool>] **select_next_available**\ (\ ) [🔗<class_TabBar_method_select_next_available>]

Selects the first available tab with greater index than the currently selected. Returns `true` if tab selection changed.


----



[bool<class_bool>] **select_previous_available**\ (\ ) [🔗<class_TabBar_method_select_previous_available>]

Selects the first available tab with lower index than the currently selected. Returns `true` if tab selection changed.


----



|void| **set_tab_button_icon**\ (\ tab_idx\: [int<class_int>], icon\: [Texture2D<class_Texture2D>]\ ) [🔗<class_TabBar_method_set_tab_button_icon>]

Sets an `icon` for the button of the tab at index `tab_idx` (located to the right, before the close button), making it visible and clickable (See [tab_button_pressed<class_TabBar_signal_tab_button_pressed>]). Giving it a `null` value will hide the button.


----



|void| **set_tab_disabled**\ (\ tab_idx\: [int<class_int>], disabled\: [bool<class_bool>]\ ) [🔗<class_TabBar_method_set_tab_disabled>]

If `disabled` is `true`, disables the tab at index `tab_idx`, making it non-interactable.


----



|void| **set_tab_hidden**\ (\ tab_idx\: [int<class_int>], hidden\: [bool<class_bool>]\ ) [🔗<class_TabBar_method_set_tab_hidden>]

If `hidden` is `true`, hides the tab at index `tab_idx`, making it disappear from the tab area.


----



|void| **set_tab_icon**\ (\ tab_idx\: [int<class_int>], icon\: [Texture2D<class_Texture2D>]\ ) [🔗<class_TabBar_method_set_tab_icon>]

Sets an `icon` for the tab at index `tab_idx`.


----



|void| **set_tab_icon_max_width**\ (\ tab_idx\: [int<class_int>], width\: [int<class_int>]\ ) [🔗<class_TabBar_method_set_tab_icon_max_width>]

Sets the maximum allowed width of the icon for the tab at index `tab_idx`. This limit is applied on top of the default size of the icon and on top of [icon_max_width<class_TabBar_theme_constant_icon_max_width>]. The height is adjusted according to the icon's ratio.


----



|void| **set_tab_language**\ (\ tab_idx\: [int<class_int>], language\: [String<class_String>]\ ) [🔗<class_TabBar_method_set_tab_language>]

Sets the language code of the title for the tab at index `tab_idx` to `language`. This is used for line-breaking and text shaping algorithms. If `language` is empty, the current locale is used.


----



|void| **set_tab_metadata**\ (\ tab_idx\: [int<class_int>], metadata\: [Variant<class_Variant>]\ ) [🔗<class_TabBar_method_set_tab_metadata>]

Sets the metadata value for the tab at index `tab_idx`, which can be retrieved later using [get_tab_metadata()<class_TabBar_method_get_tab_metadata>].


----



|void| **set_tab_text_direction**\ (\ tab_idx\: [int<class_int>], direction\: [TextDirection<enum_Control_TextDirection>]\ ) [🔗<class_TabBar_method_set_tab_text_direction>]

Sets tab title base writing direction.


----



|void| **set_tab_title**\ (\ tab_idx\: [int<class_int>], title\: [String<class_String>]\ ) [🔗<class_TabBar_method_set_tab_title>]

Sets a `title` for the tab at index `tab_idx`.


----



|void| **set_tab_tooltip**\ (\ tab_idx\: [int<class_int>], tooltip\: [String<class_String>]\ ) [🔗<class_TabBar_method_set_tab_tooltip>]

Sets a `tooltip` for tab at index `tab_idx`.

\ **Note:** By default, if the `tooltip` is empty and the tab text is truncated (not all characters fit into the tab), the title will be displayed as a tooltip. To hide the tooltip, assign `" "` as the `tooltip` text.


----


## Theme Property Descriptions



[Color<class_Color>] **drop_mark_color** = `Color(1, 1, 1, 1)` [🔗<class_TabBar_theme_color_drop_mark_color>]

Modulation color for the [drop_mark<class_TabBar_theme_icon_drop_mark>] icon.


----



[Color<class_Color>] **font_disabled_color** = `Color(0.875, 0.875, 0.875, 0.5)` [🔗<class_TabBar_theme_color_font_disabled_color>]

Font color of disabled tabs.


----



[Color<class_Color>] **font_hovered_color** = `Color(0.95, 0.95, 0.95, 1)` [🔗<class_TabBar_theme_color_font_hovered_color>]

Font color of the currently hovered tab. Does not apply to the selected tab.


----



[Color<class_Color>] **font_outline_color** = `Color(0, 0, 0, 1)` [🔗<class_TabBar_theme_color_font_outline_color>]

The tint of text outline of the tab name.


----



[Color<class_Color>] **font_selected_color** = `Color(0.95, 0.95, 0.95, 1)` [🔗<class_TabBar_theme_color_font_selected_color>]

Font color of the currently selected tab.


----



[Color<class_Color>] **font_unselected_color** = `Color(0.7, 0.7, 0.7, 1)` [🔗<class_TabBar_theme_color_font_unselected_color>]

Font color of the other, unselected tabs.


----



[Color<class_Color>] **icon_disabled_color** = `Color(1, 1, 1, 1)` [🔗<class_TabBar_theme_color_icon_disabled_color>]

Icon color of disabled tabs.


----



[Color<class_Color>] **icon_hovered_color** = `Color(1, 1, 1, 1)` [🔗<class_TabBar_theme_color_icon_hovered_color>]

Icon color of the currently hovered tab. Does not apply to the selected tab.


----



[Color<class_Color>] **icon_selected_color** = `Color(1, 1, 1, 1)` [🔗<class_TabBar_theme_color_icon_selected_color>]

Icon color of the currently selected tab.


----



[Color<class_Color>] **icon_unselected_color** = `Color(1, 1, 1, 1)` [🔗<class_TabBar_theme_color_icon_unselected_color>]

Icon color of the other, unselected tabs.


----



[int<class_int>] **h_separation** = `4` [🔗<class_TabBar_theme_constant_h_separation>]

The horizontal separation between the elements inside tabs.


----



[int<class_int>] **hover_switch_wait_msec** = `500` [🔗<class_TabBar_theme_constant_hover_switch_wait_msec>]

During a drag-and-drop, this is how many milliseconds to wait before switching the tab.


----



[int<class_int>] **icon_max_width** = `0` [🔗<class_TabBar_theme_constant_icon_max_width>]

The maximum allowed width of the tab's icon. This limit is applied on top of the default size of the icon, but before the value set with [set_tab_icon_max_width()<class_TabBar_method_set_tab_icon_max_width>]. The height is adjusted according to the icon's ratio.


----



[int<class_int>] **outline_size** = `0` [🔗<class_TabBar_theme_constant_outline_size>]

The size of the tab text outline.

\ **Note:** If using a font with [FontFile.multichannel_signed_distance_field<class_FontFile_property_multichannel_signed_distance_field>] enabled, its [FontFile.msdf_pixel_range<class_FontFile_property_msdf_pixel_range>] must be set to at least *twice* the value of [outline_size<class_TabBar_theme_constant_outline_size>] for outline rendering to look correct. Otherwise, the outline may appear to be cut off earlier than intended.


----



[int<class_int>] **tab_separation** = `0` [🔗<class_TabBar_theme_constant_tab_separation>]

The space between tabs in the tab bar.


----



[Font<class_Font>] **font** [🔗<class_TabBar_theme_font_font>]

The font used to draw tab names.


----



[int<class_int>] **font_size** [🔗<class_TabBar_theme_font_size_font_size>]

Font size of the tab names.


----



[Texture2D<class_Texture2D>] **close** [🔗<class_TabBar_theme_icon_close>]

The icon for the close button (see [tab_close_display_policy<class_TabBar_property_tab_close_display_policy>]).


----



[Texture2D<class_Texture2D>] **decrement** [🔗<class_TabBar_theme_icon_decrement>]

Icon for the left arrow button that appears when there are too many tabs to fit in the container width. When the button is disabled (i.e. the first tab is visible), it appears semi-transparent.


----



[Texture2D<class_Texture2D>] **decrement_highlight** [🔗<class_TabBar_theme_icon_decrement_highlight>]

Icon for the left arrow button that appears when there are too many tabs to fit in the container width. Used when the button is being hovered with the cursor.


----



[Texture2D<class_Texture2D>] **drop_mark** [🔗<class_TabBar_theme_icon_drop_mark>]

Icon shown to indicate where a dragged tab is gonna be dropped (see [drag_to_rearrange_enabled<class_TabBar_property_drag_to_rearrange_enabled>]).


----



[Texture2D<class_Texture2D>] **increment** [🔗<class_TabBar_theme_icon_increment>]

Icon for the right arrow button that appears when there are too many tabs to fit in the container width. When the button is disabled (i.e. the last tab is visible) it appears semi-transparent.


----



[Texture2D<class_Texture2D>] **increment_highlight** [🔗<class_TabBar_theme_icon_increment_highlight>]

Icon for the right arrow button that appears when there are too many tabs to fit in the container width. Used when the button is being hovered with the cursor.


----



[StyleBox<class_StyleBox>] **button_highlight** [🔗<class_TabBar_theme_style_button_highlight>]

Background of the tab and close buttons when they're being hovered with the cursor.


----



[StyleBox<class_StyleBox>] **button_pressed** [🔗<class_TabBar_theme_style_button_pressed>]

Background of the tab and close buttons when it's being pressed.


----



[StyleBox<class_StyleBox>] **tab_disabled** [🔗<class_TabBar_theme_style_tab_disabled>]

The style of disabled tabs.


----



[StyleBox<class_StyleBox>] **tab_focus** [🔗<class_TabBar_theme_style_tab_focus>]

[StyleBox<class_StyleBox>] used when the **TabBar** is focused. The [tab_focus<class_TabBar_theme_style_tab_focus>] [StyleBox<class_StyleBox>] is displayed *over* the base [StyleBox<class_StyleBox>] of the selected tab, so a partially transparent [StyleBox<class_StyleBox>] should be used to ensure the base [StyleBox<class_StyleBox>] remains visible. A [StyleBox<class_StyleBox>] that represents an outline or an underline works well for this purpose. To disable the focus visual effect, assign a [StyleBoxEmpty<class_StyleBoxEmpty>] resource. Note that disabling the focus visual effect will harm keyboard/controller navigation usability, so this is not recommended for accessibility reasons.


----



[StyleBox<class_StyleBox>] **tab_hovered** [🔗<class_TabBar_theme_style_tab_hovered>]

The style of the currently hovered tab. Does not apply to the selected tab.

\ **Note:** This style will be drawn with the same width as [tab_unselected<class_TabBar_theme_style_tab_unselected>] at minimum.


----



[StyleBox<class_StyleBox>] **tab_selected** [🔗<class_TabBar_theme_style_tab_selected>]

The style of the currently selected tab.


----



[StyleBox<class_StyleBox>] **tab_unselected** [🔗<class_TabBar_theme_style_tab_unselected>]

The style of the other, unselected tabs.

