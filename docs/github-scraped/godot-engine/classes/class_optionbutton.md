:github_url: hide

> **META**
	:keywords: select, dropdown



# OptionButton

**Inherits:** [Button<class_Button>] **<** [BaseButton<class_BaseButton>] **<** [Control<class_Control>] **<** [CanvasItem<class_CanvasItem>] **<** [Node<class_Node>] **<** [Object<class_Object>]

A button that brings up a dropdown with selectable options when pressed.


## Description

**OptionButton** is a type of button that brings up a dropdown with selectable items when pressed. The item selected becomes the "current" item and is displayed as the button text.

See also [BaseButton<class_BaseButton>] which contains common properties and methods associated with this node.

\ **Note:** The IDs used for items are limited to signed 32-bit integers, not the full 64 bits of [int<class_int>]. These have a range of `-2^31` to `2^31 - 1`, that is, `-2147483648` to `2147483647`.

\ **Note:** The [Button.text<class_Button_property_text>] and [Button.icon<class_Button_property_icon>] properties are set automatically based on the selected item. They shouldn't be changed manually.


## Properties

> **TABLE**
> :widths: auto
>
> +-------------------------------------------------------------------+-----------------------------------------------------------------------------+-------------------------------------------------------------------------------+
> | :ref:`ActionMode<enum_BaseButton_ActionMode>`                     | action_mode                                                                 | ``0`` (overrides :ref:`BaseButton<class_BaseButton_property_action_mode>`)    |
> +-------------------------------------------------------------------+-----------------------------------------------------------------------------+-------------------------------------------------------------------------------+
> | :ref:`HorizontalAlignment<enum_@GlobalScope_HorizontalAlignment>` | alignment                                                                   | ``0`` (overrides :ref:`Button<class_Button_property_alignment>`)              |
> +-------------------------------------------------------------------+-----------------------------------------------------------------------------+-------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                           | :ref:`allow_reselect<class_OptionButton_property_allow_reselect>`           | ``false``                                                                     |
> +-------------------------------------------------------------------+-----------------------------------------------------------------------------+-------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                           | :ref:`fit_to_longest_item<class_OptionButton_property_fit_to_longest_item>` | ``true``                                                                      |
> +-------------------------------------------------------------------+-----------------------------------------------------------------------------+-------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                             | :ref:`item_count<class_OptionButton_property_item_count>`                   | ``0``                                                                         |
> +-------------------------------------------------------------------+-----------------------------------------------------------------------------+-------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                             | :ref:`selected<class_OptionButton_property_selected>`                       | ``-1``                                                                        |
> +-------------------------------------------------------------------+-----------------------------------------------------------------------------+-------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                           | toggle_mode                                                                 | ``true`` (overrides :ref:`BaseButton<class_BaseButton_property_toggle_mode>`) |
> +-------------------------------------------------------------------+-----------------------------------------------------------------------------+-------------------------------------------------------------------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +-------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                | :ref:`add_icon_item<class_OptionButton_method_add_icon_item>`\ (\ texture\: :ref:`Texture2D<class_Texture2D>`, label\: :ref:`String<class_String>`, id\: :ref:`int<class_int>` = -1\ )       |
> +-------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                | :ref:`add_item<class_OptionButton_method_add_item>`\ (\ label\: :ref:`String<class_String>`, id\: :ref:`int<class_int>` = -1\ )                                                              |
> +-------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                | :ref:`add_separator<class_OptionButton_method_add_separator>`\ (\ text\: :ref:`String<class_String>` = ""\ )                                                                                 |
> +-------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                | :ref:`clear<class_OptionButton_method_clear>`\ (\ )                                                                                                                                          |
> +-------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`AutoTranslateMode<enum_Node_AutoTranslateMode>` | :ref:`get_item_auto_translate_mode<class_OptionButton_method_get_item_auto_translate_mode>`\ (\ idx\: :ref:`int<class_int>`\ ) |const|                                                       |
> +-------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Texture2D<class_Texture2D>`                     | :ref:`get_item_icon<class_OptionButton_method_get_item_icon>`\ (\ idx\: :ref:`int<class_int>`\ ) |const|                                                                                     |
> +-------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                 | :ref:`get_item_id<class_OptionButton_method_get_item_id>`\ (\ idx\: :ref:`int<class_int>`\ ) |const|                                                                                         |
> +-------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                 | :ref:`get_item_index<class_OptionButton_method_get_item_index>`\ (\ id\: :ref:`int<class_int>`\ ) |const|                                                                                    |
> +-------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Variant<class_Variant>`                         | :ref:`get_item_metadata<class_OptionButton_method_get_item_metadata>`\ (\ idx\: :ref:`int<class_int>`\ ) |const|                                                                             |
> +-------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`                           | :ref:`get_item_text<class_OptionButton_method_get_item_text>`\ (\ idx\: :ref:`int<class_int>`\ ) |const|                                                                                     |
> +-------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`                           | :ref:`get_item_tooltip<class_OptionButton_method_get_item_tooltip>`\ (\ idx\: :ref:`int<class_int>`\ ) |const|                                                                               |
> +-------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PopupMenu<class_PopupMenu>`                     | :ref:`get_popup<class_OptionButton_method_get_popup>`\ (\ ) |const|                                                                                                                          |
> +-------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                 | :ref:`get_selectable_item<class_OptionButton_method_get_selectable_item>`\ (\ from_last\: :ref:`bool<class_bool>` = false\ ) |const|                                                         |
> +-------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                 | :ref:`get_selected_id<class_OptionButton_method_get_selected_id>`\ (\ ) |const|                                                                                                              |
> +-------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Variant<class_Variant>`                         | :ref:`get_selected_metadata<class_OptionButton_method_get_selected_metadata>`\ (\ ) |const|                                                                                                  |
> +-------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                               | :ref:`has_selectable_items<class_OptionButton_method_has_selectable_items>`\ (\ ) |const|                                                                                                    |
> +-------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                               | :ref:`is_item_disabled<class_OptionButton_method_is_item_disabled>`\ (\ idx\: :ref:`int<class_int>`\ ) |const|                                                                               |
> +-------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                               | :ref:`is_item_separator<class_OptionButton_method_is_item_separator>`\ (\ idx\: :ref:`int<class_int>`\ ) |const|                                                                             |
> +-------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                | :ref:`remove_item<class_OptionButton_method_remove_item>`\ (\ idx\: :ref:`int<class_int>`\ )                                                                                                 |
> +-------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                | :ref:`select<class_OptionButton_method_select>`\ (\ idx\: :ref:`int<class_int>`\ )                                                                                                           |
> +-------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                | :ref:`set_disable_shortcuts<class_OptionButton_method_set_disable_shortcuts>`\ (\ disabled\: :ref:`bool<class_bool>`\ )                                                                      |
> +-------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                | :ref:`set_item_auto_translate_mode<class_OptionButton_method_set_item_auto_translate_mode>`\ (\ idx\: :ref:`int<class_int>`, mode\: :ref:`AutoTranslateMode<enum_Node_AutoTranslateMode>`\ ) |
> +-------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                | :ref:`set_item_disabled<class_OptionButton_method_set_item_disabled>`\ (\ idx\: :ref:`int<class_int>`, disabled\: :ref:`bool<class_bool>`\ )                                                 |
> +-------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                | :ref:`set_item_icon<class_OptionButton_method_set_item_icon>`\ (\ idx\: :ref:`int<class_int>`, texture\: :ref:`Texture2D<class_Texture2D>`\ )                                                |
> +-------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                | :ref:`set_item_id<class_OptionButton_method_set_item_id>`\ (\ idx\: :ref:`int<class_int>`, id\: :ref:`int<class_int>`\ )                                                                     |
> +-------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                | :ref:`set_item_metadata<class_OptionButton_method_set_item_metadata>`\ (\ idx\: :ref:`int<class_int>`, metadata\: :ref:`Variant<class_Variant>`\ )                                           |
> +-------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                | :ref:`set_item_text<class_OptionButton_method_set_item_text>`\ (\ idx\: :ref:`int<class_int>`, text\: :ref:`String<class_String>`\ )                                                         |
> +-------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                | :ref:`set_item_tooltip<class_OptionButton_method_set_item_tooltip>`\ (\ idx\: :ref:`int<class_int>`, tooltip\: :ref:`String<class_String>`\ )                                                |
> +-------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                | :ref:`show_popup<class_OptionButton_method_show_popup>`\ (\ )                                                                                                                                |
> +-------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

## Theme Properties

> **TABLE**
> :widths: auto
>
> +-----------------------------------+-------------------------------------------------------------------------+-------+
> | :ref:`int<class_int>`             | :ref:`arrow_margin<class_OptionButton_theme_constant_arrow_margin>`     | ``4`` |
> +-----------------------------------+-------------------------------------------------------------------------+-------+
> | :ref:`int<class_int>`             | :ref:`modulate_arrow<class_OptionButton_theme_constant_modulate_arrow>` | ``0`` |
> +-----------------------------------+-------------------------------------------------------------------------+-------+
> | :ref:`Texture2D<class_Texture2D>` | :ref:`arrow<class_OptionButton_theme_icon_arrow>`                       |       |
> +-----------------------------------+-------------------------------------------------------------------------+-------+
>

----


## Signals



**item_focused**\ (\ index\: [int<class_int>]\ ) [🔗<class_OptionButton_signal_item_focused>]

Emitted when the user navigates to an item using the [ProjectSettings.input/ui_up<class_ProjectSettings_property_input/ui_up>] or [ProjectSettings.input/ui_down<class_ProjectSettings_property_input/ui_down>] input actions. The index of the item selected is passed as argument.


----



**item_selected**\ (\ index\: [int<class_int>]\ ) [🔗<class_OptionButton_signal_item_selected>]

Emitted when the current item has been changed by the user. The index of the item selected is passed as argument.

\ [allow_reselect<class_OptionButton_property_allow_reselect>] must be enabled to reselect an item.


----


## Property Descriptions



[bool<class_bool>] **allow_reselect** = `false` [🔗<class_OptionButton_property_allow_reselect>]


- |void| **set_allow_reselect**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_allow_reselect**\ (\ )

If `true`, the currently selected item can be selected again.


----



[bool<class_bool>] **fit_to_longest_item** = `true` [🔗<class_OptionButton_property_fit_to_longest_item>]


- |void| **set_fit_to_longest_item**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_fit_to_longest_item**\ (\ )

If `true`, minimum size will be determined by the longest item's text, instead of the currently selected one's.

\ **Note:** For performance reasons, the minimum size doesn't update immediately when adding, removing or modifying items.


----



[int<class_int>] **item_count** = `0` [🔗<class_OptionButton_property_item_count>]


- |void| **set_item_count**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_item_count**\ (\ )

The number of items to select from.


----



[int<class_int>] **selected** = `-1` [🔗<class_OptionButton_property_selected>]


- [int<class_int>] **get_selected**\ (\ )

The index of the currently selected item, or `-1` if no item is selected.


----


## Method Descriptions



|void| **add_icon_item**\ (\ texture\: [Texture2D<class_Texture2D>], label\: [String<class_String>], id\: [int<class_int>] = -1\ ) [🔗<class_OptionButton_method_add_icon_item>]

Adds an item, with a `texture` icon, text `label` and (optionally) `id`. If no `id` is passed, the item index will be used as the item's ID. New items are appended at the end.

\ **Note:** The item will be selected if there are no other items.


----



|void| **add_item**\ (\ label\: [String<class_String>], id\: [int<class_int>] = -1\ ) [🔗<class_OptionButton_method_add_item>]

Adds an item, with text `label` and (optionally) `id`. If no `id` is passed, the item index will be used as the item's ID. New items are appended at the end.

\ **Note:** The item will be selected if there are no other items.


----



|void| **add_separator**\ (\ text\: [String<class_String>] = ""\ ) [🔗<class_OptionButton_method_add_separator>]

Adds a separator to the list of items. Separators help to group items, and can optionally be given a `text` header. A separator also gets an index assigned, and is appended at the end of the item list.


----



|void| **clear**\ (\ ) [🔗<class_OptionButton_method_clear>]

Clears all the items in the **OptionButton**.


----



[AutoTranslateMode<enum_Node_AutoTranslateMode>] **get_item_auto_translate_mode**\ (\ idx\: [int<class_int>]\ ) |const| [🔗<class_OptionButton_method_get_item_auto_translate_mode>]

Returns the auto translate mode of the item at index `idx`.


----



[Texture2D<class_Texture2D>] **get_item_icon**\ (\ idx\: [int<class_int>]\ ) |const| [🔗<class_OptionButton_method_get_item_icon>]

Returns the icon of the item at index `idx`.


----



[int<class_int>] **get_item_id**\ (\ idx\: [int<class_int>]\ ) |const| [🔗<class_OptionButton_method_get_item_id>]

Returns the ID of the item at index `idx`.


----



[int<class_int>] **get_item_index**\ (\ id\: [int<class_int>]\ ) |const| [🔗<class_OptionButton_method_get_item_index>]

Returns the index of the item with the given `id`.


----



[Variant<class_Variant>] **get_item_metadata**\ (\ idx\: [int<class_int>]\ ) |const| [🔗<class_OptionButton_method_get_item_metadata>]

Retrieves the metadata of an item. Metadata may be any type and can be used to store extra information about an item, such as an external string ID.


----



[String<class_String>] **get_item_text**\ (\ idx\: [int<class_int>]\ ) |const| [🔗<class_OptionButton_method_get_item_text>]

Returns the text of the item at index `idx`.


----



[String<class_String>] **get_item_tooltip**\ (\ idx\: [int<class_int>]\ ) |const| [🔗<class_OptionButton_method_get_item_tooltip>]

Returns the tooltip of the item at index `idx`.


----



[PopupMenu<class_PopupMenu>] **get_popup**\ (\ ) |const| [🔗<class_OptionButton_method_get_popup>]

Returns the [PopupMenu<class_PopupMenu>] contained in this button.

\ **Warning:** This is a required internal node, removing and freeing it may cause a crash. If you wish to hide it or any of its children, use their [Window.visible<class_Window_property_visible>] property.


----



[int<class_int>] **get_selectable_item**\ (\ from_last\: [bool<class_bool>] = false\ ) |const| [🔗<class_OptionButton_method_get_selectable_item>]

Returns the index of the first item which is not disabled, or marked as a separator. If `from_last` is `true`, the items will be searched in reverse order.

Returns `-1` if no item is found.


----



[int<class_int>] **get_selected_id**\ (\ ) |const| [🔗<class_OptionButton_method_get_selected_id>]

Returns the ID of the selected item, or `-1` if no item is selected.


----



[Variant<class_Variant>] **get_selected_metadata**\ (\ ) |const| [🔗<class_OptionButton_method_get_selected_metadata>]

Gets the metadata of the selected item. Metadata for items can be set using [set_item_metadata()<class_OptionButton_method_set_item_metadata>].


----



[bool<class_bool>] **has_selectable_items**\ (\ ) |const| [🔗<class_OptionButton_method_has_selectable_items>]

Returns `true` if this button contains at least one item which is not disabled, or marked as a separator.


----



[bool<class_bool>] **is_item_disabled**\ (\ idx\: [int<class_int>]\ ) |const| [🔗<class_OptionButton_method_is_item_disabled>]

Returns `true` if the item at index `idx` is disabled.


----



[bool<class_bool>] **is_item_separator**\ (\ idx\: [int<class_int>]\ ) |const| [🔗<class_OptionButton_method_is_item_separator>]

Returns `true` if the item at index `idx` is marked as a separator.


----



|void| **remove_item**\ (\ idx\: [int<class_int>]\ ) [🔗<class_OptionButton_method_remove_item>]

Removes the item at index `idx`.


----



|void| **select**\ (\ idx\: [int<class_int>]\ ) [🔗<class_OptionButton_method_select>]

Selects an item by index and makes it the current item. This will work even if the item is disabled.

Passing `-1` as the index deselects any currently selected item.


----



|void| **set_disable_shortcuts**\ (\ disabled\: [bool<class_bool>]\ ) [🔗<class_OptionButton_method_set_disable_shortcuts>]

If `true`, shortcuts are disabled and cannot be used to trigger the button.


----



|void| **set_item_auto_translate_mode**\ (\ idx\: [int<class_int>], mode\: [AutoTranslateMode<enum_Node_AutoTranslateMode>]\ ) [🔗<class_OptionButton_method_set_item_auto_translate_mode>]

Sets the auto translate mode of the item at index `idx`.

Items use [Node.AUTO_TRANSLATE_MODE_INHERIT<class_Node_constant_AUTO_TRANSLATE_MODE_INHERIT>] by default, which uses the same auto translate mode as the **OptionButton** itself.


----



|void| **set_item_disabled**\ (\ idx\: [int<class_int>], disabled\: [bool<class_bool>]\ ) [🔗<class_OptionButton_method_set_item_disabled>]

Sets whether the item at index `idx` is disabled.

Disabled items are drawn differently in the dropdown and are not selectable by the user. If the current selected item is set as disabled, it will remain selected.


----



|void| **set_item_icon**\ (\ idx\: [int<class_int>], texture\: [Texture2D<class_Texture2D>]\ ) [🔗<class_OptionButton_method_set_item_icon>]

Sets the icon of the item at index `idx`.


----



|void| **set_item_id**\ (\ idx\: [int<class_int>], id\: [int<class_int>]\ ) [🔗<class_OptionButton_method_set_item_id>]

Sets the ID of the item at index `idx`.


----



|void| **set_item_metadata**\ (\ idx\: [int<class_int>], metadata\: [Variant<class_Variant>]\ ) [🔗<class_OptionButton_method_set_item_metadata>]

Sets the metadata of an item. Metadata may be of any type and can be used to store extra information about an item, such as an external string ID.


----



|void| **set_item_text**\ (\ idx\: [int<class_int>], text\: [String<class_String>]\ ) [🔗<class_OptionButton_method_set_item_text>]

Sets the text of the item at index `idx`.


----



|void| **set_item_tooltip**\ (\ idx\: [int<class_int>], tooltip\: [String<class_String>]\ ) [🔗<class_OptionButton_method_set_item_tooltip>]

Sets the tooltip of the item at index `idx`.


----



|void| **show_popup**\ (\ ) [🔗<class_OptionButton_method_show_popup>]

Adjusts popup position and sizing for the **OptionButton**, then shows the [PopupMenu<class_PopupMenu>]. Prefer this over using `get_popup().popup()`.


----


## Theme Property Descriptions



[int<class_int>] **arrow_margin** = `4` [🔗<class_OptionButton_theme_constant_arrow_margin>]

The horizontal space between the arrow icon and the right edge of the button.


----



[int<class_int>] **modulate_arrow** = `0` [🔗<class_OptionButton_theme_constant_modulate_arrow>]

If different than `0`, the arrow icon will be modulated to the font color.


----



[Texture2D<class_Texture2D>] **arrow** [🔗<class_OptionButton_theme_icon_arrow>]

The arrow icon to be drawn on the right end of the button.

