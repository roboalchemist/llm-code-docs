:github_url: hide



# FileDialog

**Inherits:** [ConfirmationDialog<class_ConfirmationDialog>] **<** [AcceptDialog<class_AcceptDialog>] **<** [Window<class_Window>] **<** [Viewport<class_Viewport>] **<** [Node<class_Node>] **<** [Object<class_Object>]

**Inherited By:** [EditorFileDialog<class_EditorFileDialog>]

A dialog for selecting files or directories in the filesystem.


## Description

**FileDialog** is a preset dialog used to choose files and directories in the filesystem. It supports filter masks. **FileDialog** automatically sets its window title according to the [file_mode<class_FileDialog_property_file_mode>]. If you want to use a custom title, disable this by setting [mode_overrides_title<class_FileDialog_property_mode_overrides_title>] to `false`.

\ **Note:** **FileDialog** is invisible by default. To make it visible, call one of the `popup_*` methods from [Window<class_Window>] on the node, such as [Window.popup_centered_clamped()<class_Window_method_popup_centered_clamped>].


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------------------------------+-------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+
> | :ref:`Access<enum_FileDialog_Access>`             | :ref:`access<class_FileDialog_property_access>`                                           | ``0``                                                                                    |
> +---------------------------------------------------+-------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`                       | :ref:`current_dir<class_FileDialog_property_current_dir>`                                 |                                                                                          |
> +---------------------------------------------------+-------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`                       | :ref:`current_file<class_FileDialog_property_current_file>`                               |                                                                                          |
> +---------------------------------------------------+-------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`                       | :ref:`current_path<class_FileDialog_property_current_path>`                               |                                                                                          |
> +---------------------------------------------------+-------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                           | :ref:`deleting_enabled<class_FileDialog_property_deleting_enabled>`                       | ``true``                                                                                 |
> +---------------------------------------------------+-------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                           | dialog_hide_on_ok                                                                         | ``false`` (overrides :ref:`AcceptDialog<class_AcceptDialog_property_dialog_hide_on_ok>`) |
> +---------------------------------------------------+-------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+
> | :ref:`DisplayMode<enum_FileDialog_DisplayMode>`   | :ref:`display_mode<class_FileDialog_property_display_mode>`                               | ``0``                                                                                    |
> +---------------------------------------------------+-------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                           | :ref:`favorites_enabled<class_FileDialog_property_favorites_enabled>`                     | ``true``                                                                                 |
> +---------------------------------------------------+-------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                           | :ref:`file_filter_toggle_enabled<class_FileDialog_property_file_filter_toggle_enabled>`   | ``true``                                                                                 |
> +---------------------------------------------------+-------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+
> | :ref:`FileMode<enum_FileDialog_FileMode>`         | :ref:`file_mode<class_FileDialog_property_file_mode>`                                     | ``4``                                                                                    |
> +---------------------------------------------------+-------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                           | :ref:`file_sort_options_enabled<class_FileDialog_property_file_sort_options_enabled>`     | ``true``                                                                                 |
> +---------------------------------------------------+-------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`                       | :ref:`filename_filter<class_FileDialog_property_filename_filter>`                         | ``""``                                                                                   |
> +---------------------------------------------------+-------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+
> | :ref:`PackedStringArray<class_PackedStringArray>` | :ref:`filters<class_FileDialog_property_filters>`                                         | ``PackedStringArray()``                                                                  |
> +---------------------------------------------------+-------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                           | :ref:`folder_creation_enabled<class_FileDialog_property_folder_creation_enabled>`         | ``true``                                                                                 |
> +---------------------------------------------------+-------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                           | :ref:`hidden_files_toggle_enabled<class_FileDialog_property_hidden_files_toggle_enabled>` | ``true``                                                                                 |
> +---------------------------------------------------+-------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                           | :ref:`layout_toggle_enabled<class_FileDialog_property_layout_toggle_enabled>`             | ``true``                                                                                 |
> +---------------------------------------------------+-------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                           | :ref:`mode_overrides_title<class_FileDialog_property_mode_overrides_title>`               | ``true``                                                                                 |
> +---------------------------------------------------+-------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                             | :ref:`option_count<class_FileDialog_property_option_count>`                               | ``0``                                                                                    |
> +---------------------------------------------------+-------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                           | :ref:`overwrite_warning_enabled<class_FileDialog_property_overwrite_warning_enabled>`     | ``true``                                                                                 |
> +---------------------------------------------------+-------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                           | :ref:`recent_list_enabled<class_FileDialog_property_recent_list_enabled>`                 | ``true``                                                                                 |
> +---------------------------------------------------+-------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`                       | :ref:`root_subfolder<class_FileDialog_property_root_subfolder>`                           | ``""``                                                                                   |
> +---------------------------------------------------+-------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                           | :ref:`show_hidden_files<class_FileDialog_property_show_hidden_files>`                     | ``false``                                                                                |
> +---------------------------------------------------+-------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+
> | :ref:`Vector2i<class_Vector2i>`                   | size                                                                                      | ``Vector2i(640, 360)`` (overrides :ref:`Window<class_Window_property_size>`)             |
> +---------------------------------------------------+-------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`                       | title                                                                                     | ``"Save a File"`` (overrides :ref:`Window<class_Window_property_title>`)                 |
> +---------------------------------------------------+-------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                           | :ref:`use_native_dialog<class_FileDialog_property_use_native_dialog>`                     | ``false``                                                                                |
> +---------------------------------------------------+-------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +---------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                            | :ref:`add_filter<class_FileDialog_method_add_filter>`\ (\ filter\: :ref:`String<class_String>`, description\: :ref:`String<class_String>` = "", mime_type\: :ref:`String<class_String>` = ""\ )          |
> +---------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                            | :ref:`add_option<class_FileDialog_method_add_option>`\ (\ name\: :ref:`String<class_String>`, values\: :ref:`PackedStringArray<class_PackedStringArray>`, default_value_index\: :ref:`int<class_int>`\ ) |
> +---------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                            | :ref:`clear_filename_filter<class_FileDialog_method_clear_filename_filter>`\ (\ )                                                                                                                        |
> +---------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                            | :ref:`clear_filters<class_FileDialog_method_clear_filters>`\ (\ )                                                                                                                                        |
> +---------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                            | :ref:`deselect_all<class_FileDialog_method_deselect_all>`\ (\ )                                                                                                                                          |
> +---------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedStringArray<class_PackedStringArray>` | :ref:`get_favorite_list<class_FileDialog_method_get_favorite_list>`\ (\ ) |static|                                                                                                                       |
> +---------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`LineEdit<class_LineEdit>`                   | :ref:`get_line_edit<class_FileDialog_method_get_line_edit>`\ (\ )                                                                                                                                        |
> +---------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                             | :ref:`get_option_default<class_FileDialog_method_get_option_default>`\ (\ option\: :ref:`int<class_int>`\ ) |const|                                                                                      |
> +---------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`                       | :ref:`get_option_name<class_FileDialog_method_get_option_name>`\ (\ option\: :ref:`int<class_int>`\ ) |const|                                                                                            |
> +---------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedStringArray<class_PackedStringArray>` | :ref:`get_option_values<class_FileDialog_method_get_option_values>`\ (\ option\: :ref:`int<class_int>`\ ) |const|                                                                                        |
> +---------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedStringArray<class_PackedStringArray>` | :ref:`get_recent_list<class_FileDialog_method_get_recent_list>`\ (\ ) |static|                                                                                                                           |
> +---------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Dictionary<class_Dictionary>`               | :ref:`get_selected_options<class_FileDialog_method_get_selected_options>`\ (\ ) |const|                                                                                                                  |
> +---------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`VBoxContainer<class_VBoxContainer>`         | :ref:`get_vbox<class_FileDialog_method_get_vbox>`\ (\ )                                                                                                                                                  |
> +---------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                            | :ref:`invalidate<class_FileDialog_method_invalidate>`\ (\ )                                                                                                                                              |
> +---------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                           | :ref:`is_customization_flag_enabled<class_FileDialog_method_is_customization_flag_enabled>`\ (\ flag\: :ref:`Customization<enum_FileDialog_Customization>`\ ) |const|                                    |
> +---------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                            | :ref:`popup_file_dialog<class_FileDialog_method_popup_file_dialog>`\ (\ )                                                                                                                                |
> +---------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                            | :ref:`set_customization_flag_enabled<class_FileDialog_method_set_customization_flag_enabled>`\ (\ flag\: :ref:`Customization<enum_FileDialog_Customization>`, enabled\: :ref:`bool<class_bool>`\ )       |
> +---------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                            | :ref:`set_favorite_list<class_FileDialog_method_set_favorite_list>`\ (\ favorites\: :ref:`PackedStringArray<class_PackedStringArray>`\ ) |static|                                                        |
> +---------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                            | :ref:`set_get_icon_callback<class_FileDialog_method_set_get_icon_callback>`\ (\ callback\: :ref:`Callable<class_Callable>`\ ) |static|                                                                   |
> +---------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                            | :ref:`set_get_thumbnail_callback<class_FileDialog_method_set_get_thumbnail_callback>`\ (\ callback\: :ref:`Callable<class_Callable>`\ ) |static|                                                         |
> +---------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                            | :ref:`set_option_default<class_FileDialog_method_set_option_default>`\ (\ option\: :ref:`int<class_int>`, default_value_index\: :ref:`int<class_int>`\ )                                                 |
> +---------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                            | :ref:`set_option_name<class_FileDialog_method_set_option_name>`\ (\ option\: :ref:`int<class_int>`, name\: :ref:`String<class_String>`\ )                                                                |
> +---------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                            | :ref:`set_option_values<class_FileDialog_method_set_option_values>`\ (\ option\: :ref:`int<class_int>`, values\: :ref:`PackedStringArray<class_PackedStringArray>`\ )                                    |
> +---------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                            | :ref:`set_recent_list<class_FileDialog_method_set_recent_list>`\ (\ recents\: :ref:`PackedStringArray<class_PackedStringArray>`\ ) |static|                                                              |
> +---------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

## Theme Properties

> **TABLE**
> :widths: auto
>
> +-----------------------------------+-----------------------------------------------------------------------------------+--------------------------+
> | :ref:`Color<class_Color>`         | :ref:`file_disabled_color<class_FileDialog_theme_color_file_disabled_color>`      | ``Color(1, 1, 1, 0.25)`` |
> +-----------------------------------+-----------------------------------------------------------------------------------+--------------------------+
> | :ref:`Color<class_Color>`         | :ref:`file_icon_color<class_FileDialog_theme_color_file_icon_color>`              | ``Color(1, 1, 1, 1)``    |
> +-----------------------------------+-----------------------------------------------------------------------------------+--------------------------+
> | :ref:`Color<class_Color>`         | :ref:`folder_icon_color<class_FileDialog_theme_color_folder_icon_color>`          | ``Color(1, 1, 1, 1)``    |
> +-----------------------------------+-----------------------------------------------------------------------------------+--------------------------+
> | :ref:`int<class_int>`             | :ref:`thumbnail_size<class_FileDialog_theme_constant_thumbnail_size>`             | ``64``                   |
> +-----------------------------------+-----------------------------------------------------------------------------------+--------------------------+
> | :ref:`Texture2D<class_Texture2D>` | :ref:`back_folder<class_FileDialog_theme_icon_back_folder>`                       |                          |
> +-----------------------------------+-----------------------------------------------------------------------------------+--------------------------+
> | :ref:`Texture2D<class_Texture2D>` | :ref:`create_folder<class_FileDialog_theme_icon_create_folder>`                   |                          |
> +-----------------------------------+-----------------------------------------------------------------------------------+--------------------------+
> | :ref:`Texture2D<class_Texture2D>` | :ref:`favorite<class_FileDialog_theme_icon_favorite>`                             |                          |
> +-----------------------------------+-----------------------------------------------------------------------------------+--------------------------+
> | :ref:`Texture2D<class_Texture2D>` | :ref:`favorite_down<class_FileDialog_theme_icon_favorite_down>`                   |                          |
> +-----------------------------------+-----------------------------------------------------------------------------------+--------------------------+
> | :ref:`Texture2D<class_Texture2D>` | :ref:`favorite_up<class_FileDialog_theme_icon_favorite_up>`                       |                          |
> +-----------------------------------+-----------------------------------------------------------------------------------+--------------------------+
> | :ref:`Texture2D<class_Texture2D>` | :ref:`file<class_FileDialog_theme_icon_file>`                                     |                          |
> +-----------------------------------+-----------------------------------------------------------------------------------+--------------------------+
> | :ref:`Texture2D<class_Texture2D>` | :ref:`file_thumbnail<class_FileDialog_theme_icon_file_thumbnail>`                 |                          |
> +-----------------------------------+-----------------------------------------------------------------------------------+--------------------------+
> | :ref:`Texture2D<class_Texture2D>` | :ref:`folder<class_FileDialog_theme_icon_folder>`                                 |                          |
> +-----------------------------------+-----------------------------------------------------------------------------------+--------------------------+
> | :ref:`Texture2D<class_Texture2D>` | :ref:`folder_thumbnail<class_FileDialog_theme_icon_folder_thumbnail>`             |                          |
> +-----------------------------------+-----------------------------------------------------------------------------------+--------------------------+
> | :ref:`Texture2D<class_Texture2D>` | :ref:`forward_folder<class_FileDialog_theme_icon_forward_folder>`                 |                          |
> +-----------------------------------+-----------------------------------------------------------------------------------+--------------------------+
> | :ref:`Texture2D<class_Texture2D>` | :ref:`list_mode<class_FileDialog_theme_icon_list_mode>`                           |                          |
> +-----------------------------------+-----------------------------------------------------------------------------------+--------------------------+
> | :ref:`Texture2D<class_Texture2D>` | :ref:`parent_folder<class_FileDialog_theme_icon_parent_folder>`                   |                          |
> +-----------------------------------+-----------------------------------------------------------------------------------+--------------------------+
> | :ref:`Texture2D<class_Texture2D>` | :ref:`reload<class_FileDialog_theme_icon_reload>`                                 |                          |
> +-----------------------------------+-----------------------------------------------------------------------------------+--------------------------+
> | :ref:`Texture2D<class_Texture2D>` | :ref:`sort<class_FileDialog_theme_icon_sort>`                                     |                          |
> +-----------------------------------+-----------------------------------------------------------------------------------+--------------------------+
> | :ref:`Texture2D<class_Texture2D>` | :ref:`thumbnail_mode<class_FileDialog_theme_icon_thumbnail_mode>`                 |                          |
> +-----------------------------------+-----------------------------------------------------------------------------------+--------------------------+
> | :ref:`Texture2D<class_Texture2D>` | :ref:`toggle_filename_filter<class_FileDialog_theme_icon_toggle_filename_filter>` |                          |
> +-----------------------------------+-----------------------------------------------------------------------------------+--------------------------+
> | :ref:`Texture2D<class_Texture2D>` | :ref:`toggle_hidden<class_FileDialog_theme_icon_toggle_hidden>`                   |                          |
> +-----------------------------------+-----------------------------------------------------------------------------------+--------------------------+
>

----


## Signals



**dir_selected**\ (\ dir\: [String<class_String>]\ ) [🔗<class_FileDialog_signal_dir_selected>]

Emitted when the user selects a directory.


----



**file_selected**\ (\ path\: [String<class_String>]\ ) [🔗<class_FileDialog_signal_file_selected>]

Emitted when the user selects a file by double-clicking it or pressing the **OK** button.


----



**filename_filter_changed**\ (\ filter\: [String<class_String>]\ ) [🔗<class_FileDialog_signal_filename_filter_changed>]

Emitted when the filter for file names changes.


----



**files_selected**\ (\ paths\: [PackedStringArray<class_PackedStringArray>]\ ) [🔗<class_FileDialog_signal_files_selected>]

Emitted when the user selects multiple files.


----


## Enumerations



enum **FileMode**: [🔗<enum_FileDialog_FileMode>]



[FileMode<enum_FileDialog_FileMode>] **FILE_MODE_OPEN_FILE** = `0`

The dialog allows selecting one, and only one file.



[FileMode<enum_FileDialog_FileMode>] **FILE_MODE_OPEN_FILES** = `1`

The dialog allows selecting multiple files.



[FileMode<enum_FileDialog_FileMode>] **FILE_MODE_OPEN_DIR** = `2`

The dialog only allows selecting a directory, disallowing the selection of any file.



[FileMode<enum_FileDialog_FileMode>] **FILE_MODE_OPEN_ANY** = `3`

The dialog allows selecting one file or directory.



[FileMode<enum_FileDialog_FileMode>] **FILE_MODE_SAVE_FILE** = `4`

The dialog will warn when a file exists.


----



enum **Access**: [🔗<enum_FileDialog_Access>]



[Access<enum_FileDialog_Access>] **ACCESS_RESOURCES** = `0`

The dialog only allows accessing files under the [Resource<class_Resource>] path (`res://`).



[Access<enum_FileDialog_Access>] **ACCESS_USERDATA** = `1`

The dialog only allows accessing files under user data path (`user://`).



[Access<enum_FileDialog_Access>] **ACCESS_FILESYSTEM** = `2`

The dialog allows accessing files on the whole file system.


----



enum **DisplayMode**: [🔗<enum_FileDialog_DisplayMode>]



[DisplayMode<enum_FileDialog_DisplayMode>] **DISPLAY_THUMBNAILS** = `0`

The dialog displays files as a grid of thumbnails. Use [thumbnail_size<class_FileDialog_theme_constant_thumbnail_size>] to adjust their size.



[DisplayMode<enum_FileDialog_DisplayMode>] **DISPLAY_LIST** = `1`

The dialog displays files as a list of filenames.


----



enum **Customization**: [🔗<enum_FileDialog_Customization>]



[Customization<enum_FileDialog_Customization>] **CUSTOMIZATION_HIDDEN_FILES** = `0`

Toggles visibility of the favorite button, and the favorite list on the left side of the dialog.

Equivalent to [hidden_files_toggle_enabled<class_FileDialog_property_hidden_files_toggle_enabled>].



[Customization<enum_FileDialog_Customization>] **CUSTOMIZATION_CREATE_FOLDER** = `1`

If enabled, shows the button for creating new directories (when using [FILE_MODE_OPEN_DIR<class_FileDialog_constant_FILE_MODE_OPEN_DIR>], [FILE_MODE_OPEN_ANY<class_FileDialog_constant_FILE_MODE_OPEN_ANY>], or [FILE_MODE_SAVE_FILE<class_FileDialog_constant_FILE_MODE_SAVE_FILE>]).

Equivalent to [folder_creation_enabled<class_FileDialog_property_folder_creation_enabled>].



[Customization<enum_FileDialog_Customization>] **CUSTOMIZATION_FILE_FILTER** = `2`

If enabled, shows the toggle file filter button.

Equivalent to [file_filter_toggle_enabled<class_FileDialog_property_file_filter_toggle_enabled>].



[Customization<enum_FileDialog_Customization>] **CUSTOMIZATION_FILE_SORT** = `3`

If enabled, shows the file sorting options button.

Equivalent to [file_sort_options_enabled<class_FileDialog_property_file_sort_options_enabled>].



[Customization<enum_FileDialog_Customization>] **CUSTOMIZATION_FAVORITES** = `4`

If enabled, shows the toggle favorite button and favorite list on the left side of the dialog.

Equivalent to [favorites_enabled<class_FileDialog_property_favorites_enabled>].



[Customization<enum_FileDialog_Customization>] **CUSTOMIZATION_RECENT** = `5`

If enabled, shows the recent directories list on the left side of the dialog.

Equivalent to [recent_list_enabled<class_FileDialog_property_recent_list_enabled>].



[Customization<enum_FileDialog_Customization>] **CUSTOMIZATION_LAYOUT** = `6`

If enabled, shows the layout switch buttons (list/thumbnails).

Equivalent to [layout_toggle_enabled<class_FileDialog_property_layout_toggle_enabled>].



[Customization<enum_FileDialog_Customization>] **CUSTOMIZATION_OVERWRITE_WARNING** = `7`

If enabled, the **FileDialog** will warn the user before overwriting files in save mode.

Equivalent to [overwrite_warning_enabled<class_FileDialog_property_overwrite_warning_enabled>].



[Customization<enum_FileDialog_Customization>] **CUSTOMIZATION_DELETE** = `8`

If enabled, the context menu will show the "Delete" option, which allows moving files and folders to trash.

Equivalent to [deleting_enabled<class_FileDialog_property_deleting_enabled>].


----


## Property Descriptions



[Access<enum_FileDialog_Access>] **access** = `0` [🔗<class_FileDialog_property_access>]


- |void| **set_access**\ (\ value\: [Access<enum_FileDialog_Access>]\ )
- [Access<enum_FileDialog_Access>] **get_access**\ (\ )

The file system access scope.

\ **Warning:** In Web builds, FileDialog cannot access the host file system. In sandboxed Linux and macOS environments, [use_native_dialog<class_FileDialog_property_use_native_dialog>] is automatically used to allow limited access to host file system.


----



[String<class_String>] **current_dir** [🔗<class_FileDialog_property_current_dir>]


- |void| **set_current_dir**\ (\ value\: [String<class_String>]\ )
- [String<class_String>] **get_current_dir**\ (\ )

The current working directory of the file dialog.

\ **Note:** For native file dialogs, this property is only treated as a hint and may not be respected by specific OS implementations.


----



[String<class_String>] **current_file** [🔗<class_FileDialog_property_current_file>]


- |void| **set_current_file**\ (\ value\: [String<class_String>]\ )
- [String<class_String>] **get_current_file**\ (\ )

The currently selected file of the file dialog.


----



[String<class_String>] **current_path** [🔗<class_FileDialog_property_current_path>]


- |void| **set_current_path**\ (\ value\: [String<class_String>]\ )
- [String<class_String>] **get_current_path**\ (\ )

The currently selected file path of the file dialog.


----



[bool<class_bool>] **deleting_enabled** = `true` [🔗<class_FileDialog_property_deleting_enabled>]


- |void| **set_customization_flag_enabled**\ (\ flag\: [Customization<enum_FileDialog_Customization>], enabled\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_customization_flag_enabled**\ (\ flag\: [Customization<enum_FileDialog_Customization>]\ ) |const|

If `true`, the context menu will show the "Delete" option, which allows moving files and folders to trash.


----



[DisplayMode<enum_FileDialog_DisplayMode>] **display_mode** = `0` [🔗<class_FileDialog_property_display_mode>]


- |void| **set_display_mode**\ (\ value\: [DisplayMode<enum_FileDialog_DisplayMode>]\ )
- [DisplayMode<enum_FileDialog_DisplayMode>] **get_display_mode**\ (\ )

Display mode of the dialog's file list.


----



[bool<class_bool>] **favorites_enabled** = `true` [🔗<class_FileDialog_property_favorites_enabled>]


- |void| **set_customization_flag_enabled**\ (\ flag\: [Customization<enum_FileDialog_Customization>], enabled\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_customization_flag_enabled**\ (\ flag\: [Customization<enum_FileDialog_Customization>]\ ) |const|

If `true`, shows the toggle favorite button and favorite list on the left side of the dialog.


----



[bool<class_bool>] **file_filter_toggle_enabled** = `true` [🔗<class_FileDialog_property_file_filter_toggle_enabled>]


- |void| **set_customization_flag_enabled**\ (\ flag\: [Customization<enum_FileDialog_Customization>], enabled\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_customization_flag_enabled**\ (\ flag\: [Customization<enum_FileDialog_Customization>]\ ) |const|

If `true`, shows the toggle file filter button.


----



[FileMode<enum_FileDialog_FileMode>] **file_mode** = `4` [🔗<class_FileDialog_property_file_mode>]


- |void| **set_file_mode**\ (\ value\: [FileMode<enum_FileDialog_FileMode>]\ )
- [FileMode<enum_FileDialog_FileMode>] **get_file_mode**\ (\ )

The dialog's open or save mode, which affects the selection behavior.


----



[bool<class_bool>] **file_sort_options_enabled** = `true` [🔗<class_FileDialog_property_file_sort_options_enabled>]


- |void| **set_customization_flag_enabled**\ (\ flag\: [Customization<enum_FileDialog_Customization>], enabled\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_customization_flag_enabled**\ (\ flag\: [Customization<enum_FileDialog_Customization>]\ ) |const|

If `true`, shows the file sorting options button.


----



[String<class_String>] **filename_filter** = `""` [🔗<class_FileDialog_property_filename_filter>]


- |void| **set_filename_filter**\ (\ value\: [String<class_String>]\ )
- [String<class_String>] **get_filename_filter**\ (\ )

The filter for file names (case-insensitive). When set to a non-empty string, only files that contains the substring will be shown. [filename_filter<class_FileDialog_property_filename_filter>] can be edited by the user with the filter button at the top of the file dialog.

See also [filters<class_FileDialog_property_filters>], which should be used to restrict the file types that can be selected instead of [filename_filter<class_FileDialog_property_filename_filter>] which is meant to be set by the user.


----



[PackedStringArray<class_PackedStringArray>] **filters** = `PackedStringArray()` [🔗<class_FileDialog_property_filters>]


- |void| **set_filters**\ (\ value\: [PackedStringArray<class_PackedStringArray>]\ )
- [PackedStringArray<class_PackedStringArray>] **get_filters**\ (\ )

The available file type filters. Each filter string in the array should be formatted like this: `*.png,*.jpg,*.jpeg;Image Files;image/png,image/jpeg`. The description text of the filter is optional and can be omitted. Both file extensions and MIME type should be always set.

\ **Note:** Embedded file dialogs and Windows file dialogs support only file extensions, while Android, Linux, and macOS file dialogs also support MIME types.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedStringArray<class_PackedStringArray>] for more details.


----



[bool<class_bool>] **folder_creation_enabled** = `true` [🔗<class_FileDialog_property_folder_creation_enabled>]


- |void| **set_customization_flag_enabled**\ (\ flag\: [Customization<enum_FileDialog_Customization>], enabled\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_customization_flag_enabled**\ (\ flag\: [Customization<enum_FileDialog_Customization>]\ ) |const|

If `true`, shows the button for creating new directories (when using [FILE_MODE_OPEN_DIR<class_FileDialog_constant_FILE_MODE_OPEN_DIR>], [FILE_MODE_OPEN_ANY<class_FileDialog_constant_FILE_MODE_OPEN_ANY>], or [FILE_MODE_SAVE_FILE<class_FileDialog_constant_FILE_MODE_SAVE_FILE>]), and the context menu will have the "New Folder..." option.


----



[bool<class_bool>] **hidden_files_toggle_enabled** = `true` [🔗<class_FileDialog_property_hidden_files_toggle_enabled>]


- |void| **set_customization_flag_enabled**\ (\ flag\: [Customization<enum_FileDialog_Customization>], enabled\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_customization_flag_enabled**\ (\ flag\: [Customization<enum_FileDialog_Customization>]\ ) |const|

If `true`, shows the toggle hidden files button.


----



[bool<class_bool>] **layout_toggle_enabled** = `true` [🔗<class_FileDialog_property_layout_toggle_enabled>]


- |void| **set_customization_flag_enabled**\ (\ flag\: [Customization<enum_FileDialog_Customization>], enabled\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_customization_flag_enabled**\ (\ flag\: [Customization<enum_FileDialog_Customization>]\ ) |const|

If `true`, shows the layout switch buttons (list/thumbnails).


----



[bool<class_bool>] **mode_overrides_title** = `true` [🔗<class_FileDialog_property_mode_overrides_title>]


- |void| **set_mode_overrides_title**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_mode_overriding_title**\ (\ )

If `true`, changing the [file_mode<class_FileDialog_property_file_mode>] property will set the window title accordingly (e.g. setting [file_mode<class_FileDialog_property_file_mode>] to [FILE_MODE_OPEN_FILE<class_FileDialog_constant_FILE_MODE_OPEN_FILE>] will change the window title to "Open a File").


----



[int<class_int>] **option_count** = `0` [🔗<class_FileDialog_property_option_count>]


- |void| **set_option_count**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_option_count**\ (\ )

The number of additional [OptionButton<class_OptionButton>]\ s and [CheckBox<class_CheckBox>]\ es in the dialog.


----



[bool<class_bool>] **overwrite_warning_enabled** = `true` [🔗<class_FileDialog_property_overwrite_warning_enabled>]


- |void| **set_customization_flag_enabled**\ (\ flag\: [Customization<enum_FileDialog_Customization>], enabled\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_customization_flag_enabled**\ (\ flag\: [Customization<enum_FileDialog_Customization>]\ ) |const|

If `true`, the **FileDialog** will warn the user before overwriting files in save mode.


----



[bool<class_bool>] **recent_list_enabled** = `true` [🔗<class_FileDialog_property_recent_list_enabled>]


- |void| **set_customization_flag_enabled**\ (\ flag\: [Customization<enum_FileDialog_Customization>], enabled\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_customization_flag_enabled**\ (\ flag\: [Customization<enum_FileDialog_Customization>]\ ) |const|

If `true`, shows the recent directories list on the left side of the dialog.


----



[String<class_String>] **root_subfolder** = `""` [🔗<class_FileDialog_property_root_subfolder>]


- |void| **set_root_subfolder**\ (\ value\: [String<class_String>]\ )
- [String<class_String>] **get_root_subfolder**\ (\ )

If non-empty, the given sub-folder will be "root" of this **FileDialog**, i.e. user won't be able to go to its parent directory.

\ **Note:** This property is ignored by native file dialogs.


----



[bool<class_bool>] **show_hidden_files** = `false` [🔗<class_FileDialog_property_show_hidden_files>]


- |void| **set_show_hidden_files**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_showing_hidden_files**\ (\ )

If `true`, the dialog will show hidden files.

\ **Note:** This property is ignored by native file dialogs on Android and Linux.


----



[bool<class_bool>] **use_native_dialog** = `false` [🔗<class_FileDialog_property_use_native_dialog>]


- |void| **set_use_native_dialog**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_use_native_dialog**\ (\ )

If `true`, and if supported by the current [DisplayServer<class_DisplayServer>], OS native dialog will be used instead of custom one.

\ **Note:** On Android, it is only supported for Android 10+ devices and when using [ACCESS_FILESYSTEM<class_FileDialog_constant_ACCESS_FILESYSTEM>]. For access mode [ACCESS_RESOURCES<class_FileDialog_constant_ACCESS_RESOURCES>] and [ACCESS_USERDATA<class_FileDialog_constant_ACCESS_USERDATA>], the system will fall back to custom FileDialog.

\ **Note:** On Linux and macOS, sandboxed apps always use native dialogs to access the host file system.

\ **Note:** On macOS, sandboxed apps will save security-scoped bookmarks to retain access to the opened folders across multiple sessions. Use [OS.get_granted_permissions()<class_OS_method_get_granted_permissions>] to get a list of saved bookmarks.

\ **Note:** Native dialogs are isolated from the base process, file dialog properties can't be modified once the dialog is shown.

\ **Note:** This property is ignored in [EditorFileDialog<class_EditorFileDialog>].


----


## Method Descriptions



|void| **add_filter**\ (\ filter\: [String<class_String>], description\: [String<class_String>] = "", mime_type\: [String<class_String>] = ""\ ) [🔗<class_FileDialog_method_add_filter>]

Adds a comma-separated file extension `filter` and comma-separated MIME type `mime_type` option to the **FileDialog** with an optional `description`, which restricts what files can be picked.

A `filter` should be of the form `"filename.extension"`, where filename and extension can be `*` to match any string. Filters starting with `.` (i.e. empty filenames) are not allowed.

For example, a `filter` of `"*.png, *.jpg"`, a `mime_type` of `image/png, image/jpeg`, and a `description` of `"Images"` results in filter text "Images (\*.png, \*.jpg)".

\ **Note:** Embedded file dialogs and Windows file dialogs support only file extensions, while Android, Linux, and macOS file dialogs also support MIME types.


----



|void| **add_option**\ (\ name\: [String<class_String>], values\: [PackedStringArray<class_PackedStringArray>], default_value_index\: [int<class_int>]\ ) [🔗<class_FileDialog_method_add_option>]

Adds an additional [OptionButton<class_OptionButton>] to the file dialog. If `values` is empty, a [CheckBox<class_CheckBox>] is added instead.

\ `default_value_index` should be an index of the value in the `values`. If `values` is empty it should be either `1` (checked), or `0` (unchecked).


----



|void| **clear_filename_filter**\ (\ ) [🔗<class_FileDialog_method_clear_filename_filter>]

Clear the filter for file names.


----



|void| **clear_filters**\ (\ ) [🔗<class_FileDialog_method_clear_filters>]

Clear all the added filters in the dialog.


----



|void| **deselect_all**\ (\ ) [🔗<class_FileDialog_method_deselect_all>]

Clear all currently selected items in the dialog.


----



[PackedStringArray<class_PackedStringArray>] **get_favorite_list**\ (\ ) |static| [🔗<class_FileDialog_method_get_favorite_list>]

Returns the list of favorite directories, which is shared by all **FileDialog** nodes. Useful to store the list of favorites between project sessions. This method can be called only from the main thread.


----



[LineEdit<class_LineEdit>] **get_line_edit**\ (\ ) [🔗<class_FileDialog_method_get_line_edit>]

Returns the LineEdit for the selected file.

\ **Warning:** This is a required internal node, removing and freeing it may cause a crash. If you wish to hide it or any of its children, use their [CanvasItem.visible<class_CanvasItem_property_visible>] property.


----



[int<class_int>] **get_option_default**\ (\ option\: [int<class_int>]\ ) |const| [🔗<class_FileDialog_method_get_option_default>]

Returns the default value index of the [OptionButton<class_OptionButton>] or [CheckBox<class_CheckBox>] with index `option`.


----



[String<class_String>] **get_option_name**\ (\ option\: [int<class_int>]\ ) |const| [🔗<class_FileDialog_method_get_option_name>]

Returns the name of the [OptionButton<class_OptionButton>] or [CheckBox<class_CheckBox>] with index `option`.


----



[PackedStringArray<class_PackedStringArray>] **get_option_values**\ (\ option\: [int<class_int>]\ ) |const| [🔗<class_FileDialog_method_get_option_values>]

Returns an array of values of the [OptionButton<class_OptionButton>] with index `option`.


----



[PackedStringArray<class_PackedStringArray>] **get_recent_list**\ (\ ) |static| [🔗<class_FileDialog_method_get_recent_list>]

Returns the list of recent directories, which is shared by all **FileDialog** nodes. Useful to store the list of recents between project sessions. This method can be called only from the main thread.


----



[Dictionary<class_Dictionary>] **get_selected_options**\ (\ ) |const| [🔗<class_FileDialog_method_get_selected_options>]

Returns a [Dictionary<class_Dictionary>] with the selected values of the additional [OptionButton<class_OptionButton>]\ s and/or [CheckBox<class_CheckBox>]\ es. [Dictionary<class_Dictionary>] keys are names and values are selected value indices.


----



[VBoxContainer<class_VBoxContainer>] **get_vbox**\ (\ ) [🔗<class_FileDialog_method_get_vbox>]

Returns the vertical box container of the dialog, custom controls can be added to it.

\ **Warning:** This is a required internal node, removing and freeing it may cause a crash. If you wish to hide it or any of its children, use their [CanvasItem.visible<class_CanvasItem_property_visible>] property.

\ **Note:** Changes to this node are ignored by native file dialogs, use [add_option()<class_FileDialog_method_add_option>] to add custom elements to the dialog instead.


----



|void| **invalidate**\ (\ ) [🔗<class_FileDialog_method_invalidate>]

Invalidates and updates this dialog's content list.

\ **Note:** This method does nothing on native file dialogs.


----



[bool<class_bool>] **is_customization_flag_enabled**\ (\ flag\: [Customization<enum_FileDialog_Customization>]\ ) |const| [🔗<class_FileDialog_method_is_customization_flag_enabled>]

Returns `true` if the provided `flag` is enabled.


----



|void| **popup_file_dialog**\ (\ ) [🔗<class_FileDialog_method_popup_file_dialog>]

Shows the **FileDialog** using the default size and position for file dialogs, and selects the file name if there is a current file.


----



|void| **set_customization_flag_enabled**\ (\ flag\: [Customization<enum_FileDialog_Customization>], enabled\: [bool<class_bool>]\ ) [🔗<class_FileDialog_method_set_customization_flag_enabled>]

Sets the specified customization `flag`, allowing to customize the features available in this **FileDialog**.


----



|void| **set_favorite_list**\ (\ favorites\: [PackedStringArray<class_PackedStringArray>]\ ) |static| [🔗<class_FileDialog_method_set_favorite_list>]

Sets the list of favorite directories, which is shared by all **FileDialog** nodes. Useful to restore the list of favorites saved with [get_favorite_list()<class_FileDialog_method_get_favorite_list>]. This method can be called only from the main thread.

\ **Note:** **FileDialog** will update its internal [ItemList<class_ItemList>] of favorites when its visibility changes. Be sure to call this method earlier if you want your changes to have effect.


----



|void| **set_get_icon_callback**\ (\ callback\: [Callable<class_Callable>]\ ) |static| [🔗<class_FileDialog_method_set_get_icon_callback>]

Sets the callback used by the **FileDialog** nodes to get a file icon, when [DISPLAY_LIST<class_FileDialog_constant_DISPLAY_LIST>] mode is used. The callback should take a single [String<class_String>] argument (file path), and return a [Texture2D<class_Texture2D>]. If an invalid texture is returned, the [file<class_FileDialog_theme_icon_file>] icon will be used instead.


----



|void| **set_get_thumbnail_callback**\ (\ callback\: [Callable<class_Callable>]\ ) |static| [🔗<class_FileDialog_method_set_get_thumbnail_callback>]

Sets the callback used by the **FileDialog** nodes to get a file icon, when [DISPLAY_THUMBNAILS<class_FileDialog_constant_DISPLAY_THUMBNAILS>] mode is used. The callback should take a single [String<class_String>] argument (file path), and return a [Texture2D<class_Texture2D>]. If an invalid texture is returned, the [file_thumbnail<class_FileDialog_theme_icon_file_thumbnail>] icon will be used instead.

Thumbnails are usually more complex and may take a while to load. To avoid stalling the application, you can use [ImageTexture<class_ImageTexture>] to asynchronously create the thumbnail.

::

    func _ready():
        FileDialog.set_get_thumbnail_callback(thumbnail_method)

    func thumbnail_method(path):
        var image_texture = ImageTexture.new()
        make_thumbnail_async(path, image_texture)
        return image_texture

    func make_thumbnail_async(path, image_texture):
        var thumbnail_texture = await generate_thumbnail(path) # Some method that generates a thumbnail.
        image_texture.set_image(thumbnail_texture.get_image())


----



|void| **set_option_default**\ (\ option\: [int<class_int>], default_value_index\: [int<class_int>]\ ) [🔗<class_FileDialog_method_set_option_default>]

Sets the default value index of the [OptionButton<class_OptionButton>] or [CheckBox<class_CheckBox>] with index `option`.


----



|void| **set_option_name**\ (\ option\: [int<class_int>], name\: [String<class_String>]\ ) [🔗<class_FileDialog_method_set_option_name>]

Sets the name of the [OptionButton<class_OptionButton>] or [CheckBox<class_CheckBox>] with index `option`.


----



|void| **set_option_values**\ (\ option\: [int<class_int>], values\: [PackedStringArray<class_PackedStringArray>]\ ) [🔗<class_FileDialog_method_set_option_values>]

Sets the option values of the [OptionButton<class_OptionButton>] with index `option`.


----



|void| **set_recent_list**\ (\ recents\: [PackedStringArray<class_PackedStringArray>]\ ) |static| [🔗<class_FileDialog_method_set_recent_list>]

Sets the list of recent directories, which is shared by all **FileDialog** nodes. Useful to restore the list of recents saved with [set_recent_list()<class_FileDialog_method_set_recent_list>]. This method can be called only from the main thread.

\ **Note:** **FileDialog** will update its internal [ItemList<class_ItemList>] of recent directories when its visibility changes. Be sure to call this method earlier if you want your changes to have effect.


----


## Theme Property Descriptions



[Color<class_Color>] **file_disabled_color** = `Color(1, 1, 1, 0.25)` [🔗<class_FileDialog_theme_color_file_disabled_color>]

The color tint for disabled files (when the **FileDialog** is used in open folder mode).


----



[Color<class_Color>] **file_icon_color** = `Color(1, 1, 1, 1)` [🔗<class_FileDialog_theme_color_file_icon_color>]

The color modulation applied to the file icon.


----



[Color<class_Color>] **folder_icon_color** = `Color(1, 1, 1, 1)` [🔗<class_FileDialog_theme_color_folder_icon_color>]

The color modulation applied to the folder icon.


----



[int<class_int>] **thumbnail_size** = `64` [🔗<class_FileDialog_theme_constant_thumbnail_size>]

The size of thumbnail icons when [DISPLAY_THUMBNAILS<class_FileDialog_constant_DISPLAY_THUMBNAILS>] is enabled.


----



[Texture2D<class_Texture2D>] **back_folder** [🔗<class_FileDialog_theme_icon_back_folder>]

Custom icon for the back arrow.


----



[Texture2D<class_Texture2D>] **create_folder** [🔗<class_FileDialog_theme_icon_create_folder>]

Custom icon for the create folder button.


----



[Texture2D<class_Texture2D>] **favorite** [🔗<class_FileDialog_theme_icon_favorite>]

Custom icon for favorite folder button.


----



[Texture2D<class_Texture2D>] **favorite_down** [🔗<class_FileDialog_theme_icon_favorite_down>]

Custom icon for button to move down a favorite entry.


----



[Texture2D<class_Texture2D>] **favorite_up** [🔗<class_FileDialog_theme_icon_favorite_up>]

Custom icon for button to move up a favorite entry.


----



[Texture2D<class_Texture2D>] **file** [🔗<class_FileDialog_theme_icon_file>]

Custom icon for files.


----



[Texture2D<class_Texture2D>] **file_thumbnail** [🔗<class_FileDialog_theme_icon_file_thumbnail>]

Icon for files when in thumbnail mode.


----



[Texture2D<class_Texture2D>] **folder** [🔗<class_FileDialog_theme_icon_folder>]

Custom icon for folders.


----



[Texture2D<class_Texture2D>] **folder_thumbnail** [🔗<class_FileDialog_theme_icon_folder_thumbnail>]

Icon for folders when in thumbnail mode.


----



[Texture2D<class_Texture2D>] **forward_folder** [🔗<class_FileDialog_theme_icon_forward_folder>]

Custom icon for the forward arrow.


----



[Texture2D<class_Texture2D>] **list_mode** [🔗<class_FileDialog_theme_icon_list_mode>]

Icon for the button that enables list mode.


----



[Texture2D<class_Texture2D>] **parent_folder** [🔗<class_FileDialog_theme_icon_parent_folder>]

Custom icon for the parent folder arrow.


----



[Texture2D<class_Texture2D>] **reload** [🔗<class_FileDialog_theme_icon_reload>]

Custom icon for the reload button.


----



[Texture2D<class_Texture2D>] **sort** [🔗<class_FileDialog_theme_icon_sort>]

Custom icon for the sorting options menu.


----



[Texture2D<class_Texture2D>] **thumbnail_mode** [🔗<class_FileDialog_theme_icon_thumbnail_mode>]

Icon for the button that enables thumbnail mode.


----



[Texture2D<class_Texture2D>] **toggle_filename_filter** [🔗<class_FileDialog_theme_icon_toggle_filename_filter>]

Custom icon for the toggle button for the filter for file names.


----



[Texture2D<class_Texture2D>] **toggle_hidden** [🔗<class_FileDialog_theme_icon_toggle_hidden>]

Custom icon for the toggle hidden button.

