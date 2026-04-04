# DisplayServer in English

# DisplayServer

Inherits:Object
A server interface for low-level window management.

## Description

DisplayServerhandles everything related to window management. It is separated fromOSas a single operating system may support multiple display servers.
Headless mode:Starting the engine with the--headlesscommand line argumentdisables all rendering and window management functions. Most functions fromDisplayServerwill return dummy values in this case.

## Methods

| RID | accessibility_create_element(window_id:int, role:AccessibilityRole) |
|---|---|
| RID | accessibility_create_sub_element(parent_rid:RID, role:AccessibilityRole, insert_pos:int= -1) |
| RID | accessibility_create_sub_text_edit_elements(parent_rid:RID, shaped_text:RID, min_height:float, insert_pos:int= -1, is_last_line:bool= false) |
| Variant | accessibility_element_get_meta(id:RID)const |
| void | accessibility_element_set_meta(id:RID, meta:Variant) |
| void | accessibility_free_element(id:RID) |
| RID | accessibility_get_window_root(window_id:int)const |
| bool | accessibility_has_element(id:RID)const |
| int | accessibility_screen_reader_active()const |
| void | accessibility_set_window_focused(window_id:int, focused:bool) |
| void | accessibility_set_window_rect(window_id:int, rect_out:Rect2, rect_in:Rect2) |
| int | accessibility_should_increase_contrast()const |
| int | accessibility_should_reduce_animation()const |
| int | accessibility_should_reduce_transparency()const |
| void | accessibility_update_add_action(id:RID, action:AccessibilityAction, callable:Callable) |
| void | accessibility_update_add_child(id:RID, child_id:RID) |
| void | accessibility_update_add_custom_action(id:RID, action_id:int, action_description:String) |
| void | accessibility_update_add_related_controls(id:RID, related_id:RID) |
| void | accessibility_update_add_related_described_by(id:RID, related_id:RID) |
| void | accessibility_update_add_related_details(id:RID, related_id:RID) |
| void | accessibility_update_add_related_flow_to(id:RID, related_id:RID) |
| void | accessibility_update_add_related_labeled_by(id:RID, related_id:RID) |
| void | accessibility_update_add_related_radio_group(id:RID, related_id:RID) |
| void | accessibility_update_set_active_descendant(id:RID, other_id:RID) |
| void | accessibility_update_set_background_color(id:RID, color:Color) |
| void | accessibility_update_set_bounds(id:RID, p_rect:Rect2) |
| void | accessibility_update_set_checked(id:RID, checekd:bool) |
| void | accessibility_update_set_classname(id:RID, classname:String) |
| void | accessibility_update_set_color_value(id:RID, color:Color) |
| void | accessibility_update_set_description(id:RID, description:String) |
| void | accessibility_update_set_error_message(id:RID, other_id:RID) |
| void | accessibility_update_set_extra_info(id:RID, name:String) |
| void | accessibility_update_set_flag(id:RID, flag:AccessibilityFlags, value:bool) |
| void | accessibility_update_set_focus(id:RID) |
| void | accessibility_update_set_foreground_color(id:RID, color:Color) |
| void | accessibility_update_set_in_page_link_target(id:RID, other_id:RID) |
| void | accessibility_update_set_language(id:RID, language:String) |
| void | accessibility_update_set_list_item_count(id:RID, size:int) |
| void | accessibility_update_set_list_item_expanded(id:RID, expanded:bool) |
| void | accessibility_update_set_list_item_index(id:RID, index:int) |
| void | accessibility_update_set_list_item_level(id:RID, level:int) |
| void | accessibility_update_set_list_item_selected(id:RID, selected:bool) |
| void | accessibility_update_set_list_orientation(id:RID, vertical:bool) |
| void | accessibility_update_set_live(id:RID, live:AccessibilityLiveMode) |
| void | accessibility_update_set_member_of(id:RID, group_id:RID) |
| void | accessibility_update_set_name(id:RID, name:String) |
| void | accessibility_update_set_next_on_line(id:RID, other_id:RID) |
| void | accessibility_update_set_num_jump(id:RID, jump:float) |
| void | accessibility_update_set_num_range(id:RID, min:float, max:float) |
| void | accessibility_update_set_num_step(id:RID, step:float) |
| void | accessibility_update_set_num_value(id:RID, position:float) |
| void | accessibility_update_set_placeholder(id:RID, placeholder:String) |
| void | accessibility_update_set_popup_type(id:RID, popup:AccessibilityPopupType) |
| void | accessibility_update_set_previous_on_line(id:RID, other_id:RID) |
| void | accessibility_update_set_role(id:RID, role:AccessibilityRole) |
| void | accessibility_update_set_role_description(id:RID, description:String) |
| void | accessibility_update_set_scroll_x(id:RID, position:float) |
| void | accessibility_update_set_scroll_x_range(id:RID, min:float, max:float) |
| void | accessibility_update_set_scroll_y(id:RID, position:float) |
| void | accessibility_update_set_scroll_y_range(id:RID, min:float, max:float) |
| void | accessibility_update_set_shortcut(id:RID, shortcut:String) |
| void | accessibility_update_set_state_description(id:RID, description:String) |
| void | accessibility_update_set_table_cell_position(id:RID, row_index:int, column_index:int) |
| void | accessibility_update_set_table_cell_span(id:RID, row_span:int, column_span:int) |
| void | accessibility_update_set_table_column_count(id:RID, count:int) |
| void | accessibility_update_set_table_column_index(id:RID, index:int) |
| void | accessibility_update_set_table_row_count(id:RID, count:int) |
| void | accessibility_update_set_table_row_index(id:RID, index:int) |
| void | accessibility_update_set_text_align(id:RID, align:HorizontalAlignment) |
| void | accessibility_update_set_text_decorations(id:RID, underline:bool, strikethrough:bool, overline:bool) |
| void | accessibility_update_set_text_orientation(id:RID, vertical:bool) |
| void | accessibility_update_set_text_selection(id:RID, text_start_id:RID, start_char:int, text_end_id:RID, end_char:int) |
| void | accessibility_update_set_tooltip(id:RID, tooltip:String) |
| void | accessibility_update_set_transform(id:RID, transform:Transform2D) |
| void | accessibility_update_set_url(id:RID, url:String) |
| void | accessibility_update_set_value(id:RID, value:String) |
| void | beep()const |
| String | clipboard_get()const |
| Image | clipboard_get_image()const |
| String | clipboard_get_primary()const |
| bool | clipboard_has()const |
| bool | clipboard_has_image()const |
| void | clipboard_set(clipboard:String) |
| void | clipboard_set_primary(clipboard_primary:String) |
| bool | color_picker(callback:Callable) |
| int | create_status_indicator(icon:Texture2D, tooltip:String, callback:Callable) |
| CursorShape | cursor_get_shape()const |
| void | cursor_set_custom_image(cursor:Resource, shape:CursorShape= 0, hotspot:Vector2= Vector2(0, 0)) |
| void | cursor_set_shape(shape:CursorShape) |
| void | delete_status_indicator(id:int) |
| Error | dialog_input_text(title:String, description:String, existing_text:String, callback:Callable) |
| Error | dialog_show(title:String, description:String, buttons:PackedStringArray, callback:Callable) |
| void | enable_for_stealing_focus(process_id:int) |
| Error | file_dialog_show(title:String, current_directory:String, filename:String, show_hidden:bool, mode:FileDialogMode, filters:PackedStringArray, callback:Callable, parent_window_id:int= 0) |
| Error | file_dialog_with_options_show(title:String, current_directory:String, root:String, filename:String, show_hidden:bool, mode:FileDialogMode, filters:PackedStringArray, options:Array[Dictionary], callback:Callable, parent_window_id:int= 0) |
| void | force_process_and_drop_events() |
| Color | get_accent_color()const |
| Color | get_base_color()const |
| Array[Rect2] | get_display_cutouts()const |
| Rect2i | get_display_safe_area()const |
| int | get_keyboard_focus_screen()const |
| String | get_name()const |
| int | get_primary_screen()const |
| int | get_screen_count()const |
| int | get_screen_from_rect(rect:Rect2)const |
| bool | get_swap_cancel_ok() |
| int | get_window_at_screen_position(position:Vector2i)const |
| PackedInt32Array | get_window_list()const |
| int | global_menu_add_check_item(menu_root:String, label:String, callback:Callable= Callable(), key_callback:Callable= Callable(), tag:Variant= null, accelerator:Key= 0, index:int= -1) |
| int | global_menu_add_icon_check_item(menu_root:String, icon:Texture2D, label:String, callback:Callable= Callable(), key_callback:Callable= Callable(), tag:Variant= null, accelerator:Key= 0, index:int= -1) |
| int | global_menu_add_icon_item(menu_root:String, icon:Texture2D, label:String, callback:Callable= Callable(), key_callback:Callable= Callable(), tag:Variant= null, accelerator:Key= 0, index:int= -1) |
| int | global_menu_add_icon_radio_check_item(menu_root:String, icon:Texture2D, label:String, callback:Callable= Callable(), key_callback:Callable= Callable(), tag:Variant= null, accelerator:Key= 0, index:int= -1) |
| int | global_menu_add_item(menu_root:String, label:String, callback:Callable= Callable(), key_callback:Callable= Callable(), tag:Variant= null, accelerator:Key= 0, index:int= -1) |
| int | global_menu_add_multistate_item(menu_root:String, label:String, max_states:int, default_state:int, callback:Callable= Callable(), key_callback:Callable= Callable(), tag:Variant= null, accelerator:Key= 0, index:int= -1) |
| int | global_menu_add_radio_check_item(menu_root:String, label:String, callback:Callable= Callable(), key_callback:Callable= Callable(), tag:Variant= null, accelerator:Key= 0, index:int= -1) |
| int | global_menu_add_separator(menu_root:String, index:int= -1) |
| int | global_menu_add_submenu_item(menu_root:String, label:String, submenu:String, index:int= -1) |
| void | global_menu_clear(menu_root:String) |
| Key | global_menu_get_item_accelerator(menu_root:String, idx:int)const |
| Callable | global_menu_get_item_callback(menu_root:String, idx:int)const |
| int | global_menu_get_item_count(menu_root:String)const |
| Texture2D | global_menu_get_item_icon(menu_root:String, idx:int)const |
| int | global_menu_get_item_indentation_level(menu_root:String, idx:int)const |
| int | global_menu_get_item_index_from_tag(menu_root:String, tag:Variant)const |
| int | global_menu_get_item_index_from_text(menu_root:String, text:String)const |
| Callable | global_menu_get_item_key_callback(menu_root:String, idx:int)const |
| int | global_menu_get_item_max_states(menu_root:String, idx:int)const |
| int | global_menu_get_item_state(menu_root:String, idx:int)const |
| String | global_menu_get_item_submenu(menu_root:String, idx:int)const |
| Variant | global_menu_get_item_tag(menu_root:String, idx:int)const |
| String | global_menu_get_item_text(menu_root:String, idx:int)const |
| String | global_menu_get_item_tooltip(menu_root:String, idx:int)const |
| Dictionary | global_menu_get_system_menu_roots()const |
| bool | global_menu_is_item_checkable(menu_root:String, idx:int)const |
| bool | global_menu_is_item_checked(menu_root:String, idx:int)const |
| bool | global_menu_is_item_disabled(menu_root:String, idx:int)const |
| bool | global_menu_is_item_hidden(menu_root:String, idx:int)const |
| bool | global_menu_is_item_radio_checkable(menu_root:String, idx:int)const |
| void | global_menu_remove_item(menu_root:String, idx:int) |
| void | global_menu_set_item_accelerator(menu_root:String, idx:int, keycode:Key) |
| void | global_menu_set_item_callback(menu_root:String, idx:int, callback:Callable) |
| void | global_menu_set_item_checkable(menu_root:String, idx:int, checkable:bool) |
| void | global_menu_set_item_checked(menu_root:String, idx:int, checked:bool) |
| void | global_menu_set_item_disabled(menu_root:String, idx:int, disabled:bool) |
| void | global_menu_set_item_hidden(menu_root:String, idx:int, hidden:bool) |
| void | global_menu_set_item_hover_callbacks(menu_root:String, idx:int, callback:Callable) |
| void | global_menu_set_item_icon(menu_root:String, idx:int, icon:Texture2D) |
| void | global_menu_set_item_indentation_level(menu_root:String, idx:int, level:int) |
| void | global_menu_set_item_key_callback(menu_root:String, idx:int, key_callback:Callable) |
| void | global_menu_set_item_max_states(menu_root:String, idx:int, max_states:int) |
| void | global_menu_set_item_radio_checkable(menu_root:String, idx:int, checkable:bool) |
| void | global_menu_set_item_state(menu_root:String, idx:int, state:int) |
| void | global_menu_set_item_submenu(menu_root:String, idx:int, submenu:String) |
| void | global_menu_set_item_tag(menu_root:String, idx:int, tag:Variant) |
| void | global_menu_set_item_text(menu_root:String, idx:int, text:String) |
| void | global_menu_set_item_tooltip(menu_root:String, idx:int, tooltip:String) |
| void | global_menu_set_popup_callbacks(menu_root:String, open_callback:Callable, close_callback:Callable) |
| bool | has_additional_outputs()const |
| bool | has_feature(feature:Feature)const |
| bool | has_hardware_keyboard()const |
| void | help_set_search_callbacks(search_callback:Callable, action_callback:Callable) |
| Vector2i | ime_get_selection()const |
| String | ime_get_text()const |
| bool | is_dark_mode()const |
| bool | is_dark_mode_supported()const |
| bool | is_touchscreen_available()const |
| bool | is_window_transparency_available()const |
| int | keyboard_get_current_layout()const |
| Key | keyboard_get_keycode_from_physical(keycode:Key)const |
| Key | keyboard_get_label_from_physical(keycode:Key)const |
| int | keyboard_get_layout_count()const |
| String | keyboard_get_layout_language(index:int)const |
| String | keyboard_get_layout_name(index:int)const |
| void | keyboard_set_current_layout(index:int) |
| BitField[MouseButtonMask] | mouse_get_button_state()const |
| MouseMode | mouse_get_mode()const |
| Vector2i | mouse_get_position()const |
| void | mouse_set_mode(mouse_mode:MouseMode) |
| void | process_events() |
| void | register_additional_output(object:Object) |
| int | screen_get_dpi(screen:int= -1)const |
| Image | screen_get_image(screen:int= -1)const |
| Image | screen_get_image_rect(rect:Rect2i)const |
| float | screen_get_max_scale()const |
| ScreenOrientation | screen_get_orientation(screen:int= -1)const |
| Color | screen_get_pixel(position:Vector2i)const |
| Vector2i | screen_get_position(screen:int= -1)const |
| float | screen_get_refresh_rate(screen:int= -1)const |
| float | screen_get_scale(screen:int= -1)const |
| Vector2i | screen_get_size(screen:int= -1)const |
| Rect2i | screen_get_usable_rect(screen:int= -1)const |
| bool | screen_is_kept_on()const |
| void | screen_set_keep_on(enable:bool) |
| void | screen_set_orientation(orientation:ScreenOrientation, screen:int= -1) |
| void | set_hardware_keyboard_connection_change_callback(callable:Callable) |
| void | set_icon(image:Image) |
| void | set_native_icon(filename:String) |
| void | set_system_theme_change_callback(callable:Callable) |
| void | show_emoji_and_symbol_picker()const |
| Rect2 | status_indicator_get_rect(id:int)const |
| void | status_indicator_set_callback(id:int, callback:Callable) |
| void | status_indicator_set_icon(id:int, icon:Texture2D) |
| void | status_indicator_set_menu(id:int, menu_rid:RID) |
| void | status_indicator_set_tooltip(id:int, tooltip:String) |
| String | tablet_get_current_driver()const |
| int | tablet_get_driver_count()const |
| String | tablet_get_driver_name(idx:int)const |
| void | tablet_set_current_driver(name:String) |
| Array[Dictionary] | tts_get_voices()const |
| PackedStringArray | tts_get_voices_for_language(language:String)const |
| bool | tts_is_paused()const |
| bool | tts_is_speaking()const |
| void | tts_pause() |
| void | tts_resume() |
| void | tts_set_utterance_callback(event:TTSUtteranceEvent, callable:Callable) |
| void | tts_speak(text:String, voice:String, volume:int= 50, pitch:float= 1.0, rate:float= 1.0, utterance_id:int= 0, interrupt:bool= false) |
| void | tts_stop() |
| void | unregister_additional_output(object:Object) |
| int | virtual_keyboard_get_height()const |
| void | virtual_keyboard_hide() |
| void | virtual_keyboard_show(existing_text:String, position:Rect2= Rect2(0, 0, 0, 0), type:VirtualKeyboardType= 0, max_length:int= -1, cursor_start:int= -1, cursor_end:int= -1) |
| void | warp_mouse(position:Vector2i) |
| bool | window_can_draw(window_id:int= 0)const |
| int | window_get_active_popup()const |
| int | window_get_attached_instance_id(window_id:int= 0)const |
| int | window_get_current_screen(window_id:int= 0)const |
| bool | window_get_flag(flag:WindowFlags, window_id:int= 0)const |
| Vector2i | window_get_max_size(window_id:int= 0)const |
| Vector2i | window_get_min_size(window_id:int= 0)const |
| WindowMode | window_get_mode(window_id:int= 0)const |
| int | window_get_native_handle(handle_type:HandleType, window_id:int= 0)const |
| Rect2i | window_get_popup_safe_rect(window:int)const |
| Vector2i | window_get_position(window_id:int= 0)const |
| Vector2i | window_get_position_with_decorations(window_id:int= 0)const |
| Vector3i | window_get_safe_title_margins(window_id:int= 0)const |
| Vector2i | window_get_size(window_id:int= 0)const |
| Vector2i | window_get_size_with_decorations(window_id:int= 0)const |
| Vector2i | window_get_title_size(title:String, window_id:int= 0)const |
| VSyncMode | window_get_vsync_mode(window_id:int= 0)const |
| bool | window_is_focused(window_id:int= 0)const |
| bool | window_is_maximize_allowed(window_id:int= 0)const |
| bool | window_maximize_on_title_dbl_click()const |
| bool | window_minimize_on_title_dbl_click()const |
| void | window_move_to_foreground(window_id:int= 0) |
| void | window_request_attention(window_id:int= 0) |
| void | window_set_color(color:Color) |
| void | window_set_current_screen(screen:int, window_id:int= 0) |
| void | window_set_drop_files_callback(callback:Callable, window_id:int= 0) |
| void | window_set_exclusive(window_id:int, exclusive:bool) |
| void | window_set_flag(flag:WindowFlags, enabled:bool, window_id:int= 0) |
| void | window_set_ime_active(active:bool, window_id:int= 0) |
| void | window_set_ime_position(position:Vector2i, window_id:int= 0) |
| void | window_set_input_event_callback(callback:Callable, window_id:int= 0) |
| void | window_set_input_text_callback(callback:Callable, window_id:int= 0) |
| void | window_set_max_size(max_size:Vector2i, window_id:int= 0) |
| void | window_set_min_size(min_size:Vector2i, window_id:int= 0) |
| void | window_set_mode(mode:WindowMode, window_id:int= 0) |
| void | window_set_mouse_passthrough(region:PackedVector2Array, window_id:int= 0) |
| void | window_set_popup_safe_rect(window:int, rect:Rect2i) |
| void | window_set_position(position:Vector2i, window_id:int= 0) |
| void | window_set_rect_changed_callback(callback:Callable, window_id:int= 0) |
| void | window_set_size(size:Vector2i, window_id:int= 0) |
| void | window_set_title(title:String, window_id:int= 0) |
| void | window_set_transient(window_id:int, parent_window_id:int) |
| void | window_set_vsync_mode(vsync_mode:VSyncMode, window_id:int= 0) |
| void | window_set_window_buttons_offset(offset:Vector2i, window_id:int= 0) |
| void | window_set_window_event_callback(callback:Callable, window_id:int= 0) |
| void | window_start_drag(window_id:int= 0) |
| void | window_start_resize(edge:WindowResizeEdge, window_id:int= 0) |

accessibility_create_element(window_id:int, role:AccessibilityRole)
accessibility_create_sub_element(parent_rid:RID, role:AccessibilityRole, insert_pos:int= -1)
accessibility_create_sub_text_edit_elements(parent_rid:RID, shaped_text:RID, min_height:float, insert_pos:int= -1, is_last_line:bool= false)
Variant
accessibility_element_get_meta(id:RID)const
void
accessibility_element_set_meta(id:RID, meta:Variant)
void
accessibility_free_element(id:RID)
accessibility_get_window_root(window_id:int)const
bool
accessibility_has_element(id:RID)const
accessibility_screen_reader_active()const
void
accessibility_set_window_focused(window_id:int, focused:bool)
void
accessibility_set_window_rect(window_id:int, rect_out:Rect2, rect_in:Rect2)
accessibility_should_increase_contrast()const
accessibility_should_reduce_animation()const
accessibility_should_reduce_transparency()const
void
accessibility_update_add_action(id:RID, action:AccessibilityAction, callable:Callable)
void
accessibility_update_add_child(id:RID, child_id:RID)
void
accessibility_update_add_custom_action(id:RID, action_id:int, action_description:String)
void
accessibility_update_add_related_controls(id:RID, related_id:RID)
void
accessibility_update_add_related_described_by(id:RID, related_id:RID)
void
accessibility_update_add_related_details(id:RID, related_id:RID)
void
accessibility_update_add_related_flow_to(id:RID, related_id:RID)
void
accessibility_update_add_related_labeled_by(id:RID, related_id:RID)
void
accessibility_update_add_related_radio_group(id:RID, related_id:RID)
void
accessibility_update_set_active_descendant(id:RID, other_id:RID)
void
accessibility_update_set_background_color(id:RID, color:Color)
void
accessibility_update_set_bounds(id:RID, p_rect:Rect2)
void
accessibility_update_set_checked(id:RID, checekd:bool)
void
accessibility_update_set_classname(id:RID, classname:String)
void
accessibility_update_set_color_value(id:RID, color:Color)
void
accessibility_update_set_description(id:RID, description:String)
void
accessibility_update_set_error_message(id:RID, other_id:RID)
void
accessibility_update_set_extra_info(id:RID, name:String)
void
accessibility_update_set_flag(id:RID, flag:AccessibilityFlags, value:bool)
void
accessibility_update_set_focus(id:RID)
void
accessibility_update_set_foreground_color(id:RID, color:Color)
void
accessibility_update_set_in_page_link_target(id:RID, other_id:RID)
void
accessibility_update_set_language(id:RID, language:String)
void
accessibility_update_set_list_item_count(id:RID, size:int)
void
accessibility_update_set_list_item_expanded(id:RID, expanded:bool)
void
accessibility_update_set_list_item_index(id:RID, index:int)
void
accessibility_update_set_list_item_level(id:RID, level:int)
void
accessibility_update_set_list_item_selected(id:RID, selected:bool)
void
accessibility_update_set_list_orientation(id:RID, vertical:bool)
void
accessibility_update_set_live(id:RID, live:AccessibilityLiveMode)
void
accessibility_update_set_member_of(id:RID, group_id:RID)
void
accessibility_update_set_name(id:RID, name:String)
void
accessibility_update_set_next_on_line(id:RID, other_id:RID)
void
accessibility_update_set_num_jump(id:RID, jump:float)
void
accessibility_update_set_num_range(id:RID, min:float, max:float)
void
accessibility_update_set_num_step(id:RID, step:float)
void
accessibility_update_set_num_value(id:RID, position:float)
void
accessibility_update_set_placeholder(id:RID, placeholder:String)
void
accessibility_update_set_popup_type(id:RID, popup:AccessibilityPopupType)
void
accessibility_update_set_previous_on_line(id:RID, other_id:RID)
void
accessibility_update_set_role(id:RID, role:AccessibilityRole)
void
accessibility_update_set_role_description(id:RID, description:String)
void
accessibility_update_set_scroll_x(id:RID, position:float)
void
accessibility_update_set_scroll_x_range(id:RID, min:float, max:float)
void
accessibility_update_set_scroll_y(id:RID, position:float)
void
accessibility_update_set_scroll_y_range(id:RID, min:float, max:float)
void
accessibility_update_set_shortcut(id:RID, shortcut:String)
void
accessibility_update_set_state_description(id:RID, description:String)
void
accessibility_update_set_table_cell_position(id:RID, row_index:int, column_index:int)
void
accessibility_update_set_table_cell_span(id:RID, row_span:int, column_span:int)
void
accessibility_update_set_table_column_count(id:RID, count:int)
void
accessibility_update_set_table_column_index(id:RID, index:int)
void
accessibility_update_set_table_row_count(id:RID, count:int)
void
accessibility_update_set_table_row_index(id:RID, index:int)
void
accessibility_update_set_text_align(id:RID, align:HorizontalAlignment)
void
accessibility_update_set_text_decorations(id:RID, underline:bool, strikethrough:bool, overline:bool)
void
accessibility_update_set_text_orientation(id:RID, vertical:bool)
void
accessibility_update_set_text_selection(id:RID, text_start_id:RID, start_char:int, text_end_id:RID, end_char:int)
void
accessibility_update_set_tooltip(id:RID, tooltip:String)
void
accessibility_update_set_transform(id:RID, transform:Transform2D)
void
accessibility_update_set_url(id:RID, url:String)
void
accessibility_update_set_value(id:RID, value:String)
void
beep()const
String
clipboard_get()const
Image
clipboard_get_image()const
String
clipboard_get_primary()const
bool
clipboard_has()const
bool
clipboard_has_image()const
void
clipboard_set(clipboard:String)
void
clipboard_set_primary(clipboard_primary:String)
bool
color_picker(callback:Callable)
create_status_indicator(icon:Texture2D, tooltip:String, callback:Callable)
CursorShape
cursor_get_shape()const
void
cursor_set_custom_image(cursor:Resource, shape:CursorShape= 0, hotspot:Vector2= Vector2(0, 0))
void
cursor_set_shape(shape:CursorShape)
void
delete_status_indicator(id:int)
Error
dialog_input_text(title:String, description:String, existing_text:String, callback:Callable)
Error
dialog_show(title:String, description:String, buttons:PackedStringArray, callback:Callable)
void
enable_for_stealing_focus(process_id:int)
Error
file_dialog_show(title:String, current_directory:String, filename:String, show_hidden:bool, mode:FileDialogMode, filters:PackedStringArray, callback:Callable, parent_window_id:int= 0)
Error
file_dialog_with_options_show(title:String, current_directory:String, root:String, filename:String, show_hidden:bool, mode:FileDialogMode, filters:PackedStringArray, options:Array[Dictionary], callback:Callable, parent_window_id:int= 0)
void
force_process_and_drop_events()
Color
get_accent_color()const
Color
get_base_color()const
Array[Rect2]
get_display_cutouts()const
Rect2i
get_display_safe_area()const
get_keyboard_focus_screen()const
String
get_name()const
get_primary_screen()const
get_screen_count()const
get_screen_from_rect(rect:Rect2)const
bool
get_swap_cancel_ok()
get_window_at_screen_position(position:Vector2i)const
PackedInt32Array
get_window_list()const
global_menu_add_check_item(menu_root:String, label:String, callback:Callable= Callable(), key_callback:Callable= Callable(), tag:Variant= null, accelerator:Key= 0, index:int= -1)
global_menu_add_icon_check_item(menu_root:String, icon:Texture2D, label:String, callback:Callable= Callable(), key_callback:Callable= Callable(), tag:Variant= null, accelerator:Key= 0, index:int= -1)
global_menu_add_icon_item(menu_root:String, icon:Texture2D, label:String, callback:Callable= Callable(), key_callback:Callable= Callable(), tag:Variant= null, accelerator:Key= 0, index:int= -1)
global_menu_add_icon_radio_check_item(menu_root:String, icon:Texture2D, label:String, callback:Callable= Callable(), key_callback:Callable= Callable(), tag:Variant= null, accelerator:Key= 0, index:int= -1)
global_menu_add_item(menu_root:String, label:String, callback:Callable= Callable(), key_callback:Callable= Callable(), tag:Variant= null, accelerator:Key= 0, index:int= -1)
global_menu_add_multistate_item(menu_root:String, label:String, max_states:int, default_state:int, callback:Callable= Callable(), key_callback:Callable= Callable(), tag:Variant= null, accelerator:Key= 0, index:int= -1)
global_menu_add_radio_check_item(menu_root:String, label:String, callback:Callable= Callable(), key_callback:Callable= Callable(), tag:Variant= null, accelerator:Key= 0, index:int= -1)
global_menu_add_separator(menu_root:String, index:int= -1)
global_menu_add_submenu_item(menu_root:String, label:String, submenu:String, index:int= -1)
void
global_menu_clear(menu_root:String)
global_menu_get_item_accelerator(menu_root:String, idx:int)const
Callable
global_menu_get_item_callback(menu_root:String, idx:int)const
global_menu_get_item_count(menu_root:String)const
Texture2D
global_menu_get_item_icon(menu_root:String, idx:int)const
global_menu_get_item_indentation_level(menu_root:String, idx:int)const
global_menu_get_item_index_from_tag(menu_root:String, tag:Variant)const
global_menu_get_item_index_from_text(menu_root:String, text:String)const
Callable
global_menu_get_item_key_callback(menu_root:String, idx:int)const
global_menu_get_item_max_states(menu_root:String, idx:int)const
global_menu_get_item_state(menu_root:String, idx:int)const
String
global_menu_get_item_submenu(menu_root:String, idx:int)const
Variant
global_menu_get_item_tag(menu_root:String, idx:int)const
String
global_menu_get_item_text(menu_root:String, idx:int)const
String
global_menu_get_item_tooltip(menu_root:String, idx:int)const
Dictionary
global_menu_get_system_menu_roots()const
bool
global_menu_is_item_checkable(menu_root:String, idx:int)const
bool
global_menu_is_item_checked(menu_root:String, idx:int)const
bool
global_menu_is_item_disabled(menu_root:String, idx:int)const
bool
global_menu_is_item_hidden(menu_root:String, idx:int)const
bool
global_menu_is_item_radio_checkable(menu_root:String, idx:int)const
void
global_menu_remove_item(menu_root:String, idx:int)
void
global_menu_set_item_accelerator(menu_root:String, idx:int, keycode:Key)
void
global_menu_set_item_callback(menu_root:String, idx:int, callback:Callable)
void
global_menu_set_item_checkable(menu_root:String, idx:int, checkable:bool)
void
global_menu_set_item_checked(menu_root:String, idx:int, checked:bool)
void
global_menu_set_item_disabled(menu_root:String, idx:int, disabled:bool)
void
global_menu_set_item_hidden(menu_root:String, idx:int, hidden:bool)
void
global_menu_set_item_hover_callbacks(menu_root:String, idx:int, callback:Callable)
void
global_menu_set_item_icon(menu_root:String, idx:int, icon:Texture2D)
void
global_menu_set_item_indentation_level(menu_root:String, idx:int, level:int)
void
global_menu_set_item_key_callback(menu_root:String, idx:int, key_callback:Callable)
void
global_menu_set_item_max_states(menu_root:String, idx:int, max_states:int)
void
global_menu_set_item_radio_checkable(menu_root:String, idx:int, checkable:bool)
void
global_menu_set_item_state(menu_root:String, idx:int, state:int)
void
global_menu_set_item_submenu(menu_root:String, idx:int, submenu:String)
void
global_menu_set_item_tag(menu_root:String, idx:int, tag:Variant)
void
global_menu_set_item_text(menu_root:String, idx:int, text:String)
void
global_menu_set_item_tooltip(menu_root:String, idx:int, tooltip:String)
void
global_menu_set_popup_callbacks(menu_root:String, open_callback:Callable, close_callback:Callable)
bool
has_additional_outputs()const
bool
has_feature(feature:Feature)const
bool
has_hardware_keyboard()const
void
help_set_search_callbacks(search_callback:Callable, action_callback:Callable)
Vector2i
ime_get_selection()const
String
ime_get_text()const
bool
is_dark_mode()const
bool
is_dark_mode_supported()const
bool
is_touchscreen_available()const
bool
is_window_transparency_available()const
keyboard_get_current_layout()const
keyboard_get_keycode_from_physical(keycode:Key)const
keyboard_get_label_from_physical(keycode:Key)const
keyboard_get_layout_count()const
String
keyboard_get_layout_language(index:int)const
String
keyboard_get_layout_name(index:int)const
void
keyboard_set_current_layout(index:int)
BitField[MouseButtonMask]
mouse_get_button_state()const
MouseMode
mouse_get_mode()const
Vector2i
mouse_get_position()const
void
mouse_set_mode(mouse_mode:MouseMode)
void
process_events()
void
register_additional_output(object:Object)
screen_get_dpi(screen:int= -1)const
Image
screen_get_image(screen:int= -1)const
Image
screen_get_image_rect(rect:Rect2i)const
float
screen_get_max_scale()const
ScreenOrientation
screen_get_orientation(screen:int= -1)const
Color
screen_get_pixel(position:Vector2i)const
Vector2i
screen_get_position(screen:int= -1)const
float
screen_get_refresh_rate(screen:int= -1)const
float
screen_get_scale(screen:int= -1)const
Vector2i
screen_get_size(screen:int= -1)const
Rect2i
screen_get_usable_rect(screen:int= -1)const
bool
screen_is_kept_on()const
void
screen_set_keep_on(enable:bool)
void
screen_set_orientation(orientation:ScreenOrientation, screen:int= -1)
void
set_hardware_keyboard_connection_change_callback(callable:Callable)
void
set_icon(image:Image)
void
set_native_icon(filename:String)
void
set_system_theme_change_callback(callable:Callable)
void
show_emoji_and_symbol_picker()const
Rect2
status_indicator_get_rect(id:int)const
void
status_indicator_set_callback(id:int, callback:Callable)
void
status_indicator_set_icon(id:int, icon:Texture2D)
void
status_indicator_set_menu(id:int, menu_rid:RID)
void
status_indicator_set_tooltip(id:int, tooltip:String)
String
tablet_get_current_driver()const
tablet_get_driver_count()const
String
tablet_get_driver_name(idx:int)const
void
tablet_set_current_driver(name:String)
Array[Dictionary]
tts_get_voices()const
PackedStringArray
tts_get_voices_for_language(language:String)const
bool
tts_is_paused()const
bool
tts_is_speaking()const
void
tts_pause()
void
tts_resume()
void
tts_set_utterance_callback(event:TTSUtteranceEvent, callable:Callable)
void
tts_speak(text:String, voice:String, volume:int= 50, pitch:float= 1.0, rate:float= 1.0, utterance_id:int= 0, interrupt:bool= false)
void
tts_stop()
void
unregister_additional_output(object:Object)
virtual_keyboard_get_height()const
void
virtual_keyboard_hide()
void
virtual_keyboard_show(existing_text:String, position:Rect2= Rect2(0, 0, 0, 0), type:VirtualKeyboardType= 0, max_length:int= -1, cursor_start:int= -1, cursor_end:int= -1)
void
warp_mouse(position:Vector2i)
bool
window_can_draw(window_id:int= 0)const
window_get_active_popup()const
window_get_attached_instance_id(window_id:int= 0)const
window_get_current_screen(window_id:int= 0)const
bool
window_get_flag(flag:WindowFlags, window_id:int= 0)const
Vector2i
window_get_max_size(window_id:int= 0)const
Vector2i
window_get_min_size(window_id:int= 0)const
WindowMode
window_get_mode(window_id:int= 0)const
window_get_native_handle(handle_type:HandleType, window_id:int= 0)const
Rect2i
window_get_popup_safe_rect(window:int)const
Vector2i
window_get_position(window_id:int= 0)const
Vector2i
window_get_position_with_decorations(window_id:int= 0)const
Vector3i
window_get_safe_title_margins(window_id:int= 0)const
Vector2i
window_get_size(window_id:int= 0)const
Vector2i
window_get_size_with_decorations(window_id:int= 0)const
Vector2i
window_get_title_size(title:String, window_id:int= 0)const
VSyncMode
window_get_vsync_mode(window_id:int= 0)const
bool
window_is_focused(window_id:int= 0)const
bool
window_is_maximize_allowed(window_id:int= 0)const
bool
window_maximize_on_title_dbl_click()const
bool
window_minimize_on_title_dbl_click()const
void
window_move_to_foreground(window_id:int= 0)
void
window_request_attention(window_id:int= 0)
void
window_set_color(color:Color)
void
window_set_current_screen(screen:int, window_id:int= 0)
void
window_set_drop_files_callback(callback:Callable, window_id:int= 0)
void
window_set_exclusive(window_id:int, exclusive:bool)
void
window_set_flag(flag:WindowFlags, enabled:bool, window_id:int= 0)
void
window_set_ime_active(active:bool, window_id:int= 0)
void
window_set_ime_position(position:Vector2i, window_id:int= 0)
void
window_set_input_event_callback(callback:Callable, window_id:int= 0)
void
window_set_input_text_callback(callback:Callable, window_id:int= 0)
void
window_set_max_size(max_size:Vector2i, window_id:int= 0)
void
window_set_min_size(min_size:Vector2i, window_id:int= 0)
void
window_set_mode(mode:WindowMode, window_id:int= 0)
void
window_set_mouse_passthrough(region:PackedVector2Array, window_id:int= 0)
void
window_set_popup_safe_rect(window:int, rect:Rect2i)
void
window_set_position(position:Vector2i, window_id:int= 0)
void
window_set_rect_changed_callback(callback:Callable, window_id:int= 0)
void
window_set_size(size:Vector2i, window_id:int= 0)
void
window_set_title(title:String, window_id:int= 0)
void
window_set_transient(window_id:int, parent_window_id:int)
void
window_set_vsync_mode(vsync_mode:VSyncMode, window_id:int= 0)
void
window_set_window_buttons_offset(offset:Vector2i, window_id:int= 0)
void
window_set_window_event_callback(callback:Callable, window_id:int= 0)
void
window_start_drag(window_id:int= 0)
void
window_start_resize(edge:WindowResizeEdge, window_id:int= 0)

## Enumerations

enumFeature:🔗
FeatureFEATURE_GLOBAL_MENU=0
Deprecated:UseNativeMenuorPopupMenuinstead.
Display server supports global menu. This allows the application to display its menu items in the operating system's top bar.macOS
FeatureFEATURE_SUBWINDOWS=1
Display server supports multiple windows that can be moved outside of the main window.Windows, macOS, Linux (X11)
FeatureFEATURE_TOUCHSCREEN=2
Display server supports touchscreen input.Windows, Linux (X11), Android, iOS, Web
FeatureFEATURE_MOUSE=3
Display server supports mouse input.Windows, macOS, Linux (X11/Wayland), Android, Web
FeatureFEATURE_MOUSE_WARP=4
Display server supports warping mouse coordinates to keep the mouse cursor constrained within an area, but looping when one of the edges is reached.Windows, macOS, Linux (X11/Wayland)
FeatureFEATURE_CLIPBOARD=5
Display server supports setting and getting clipboard data. See alsoFEATURE_CLIPBOARD_PRIMARY.Windows, macOS, Linux (X11/Wayland), Android, iOS, Web
FeatureFEATURE_VIRTUAL_KEYBOARD=6
Display server supports popping up a virtual keyboard when requested to input text without a physical keyboard.Android, iOS, Web
FeatureFEATURE_CURSOR_SHAPE=7
Display server supports setting the mouse cursor shape to be different from the default.Windows, macOS, Linux (X11/Wayland), Android, Web
FeatureFEATURE_CUSTOM_CURSOR_SHAPE=8
Display server supports setting the mouse cursor shape to a custom image.Windows, macOS, Linux (X11/Wayland), Web
FeatureFEATURE_NATIVE_DIALOG=9
Display server supports spawning text dialogs using the operating system's native look-and-feel. Seedialog_show().Windows, macOS
FeatureFEATURE_IME=10
Display server supportsInput Method Editor, which is commonly used for inputting Chinese/Japanese/Korean text. This is handled by the operating system, rather than by Godot.Windows, macOS, Linux (X11)
FeatureFEATURE_WINDOW_TRANSPARENCY=11
Display server supports windows can use per-pixel transparency to make windows behind them partially or fully visible.Windows, macOS, Linux (X11/Wayland), Android
FeatureFEATURE_HIDPI=12
Display server supports querying the operating system's display scale factor. This allows automatically detecting the hiDPI displayreliably, instead of guessing based on the screen resolution and the display's reported DPI (which might be unreliable due to broken monitor EDID).Windows, Linux (Wayland), macOS
FeatureFEATURE_ICON=13
Display server supports changing the window icon (usually displayed in the top-left corner).Windows, macOS, Linux (X11/Wayland)
Note:Use on Wayland requires the compositor to implement thexdg_toplevel_icon_v1protocol, which not all compositors do. Seexdg_toplevel_icon_v1#compositor-supportfor more information on individual compositor support.
FeatureFEATURE_NATIVE_ICON=14
Display server supports changing the window icon (usually displayed in the top-left corner).Windows, macOS
FeatureFEATURE_ORIENTATION=15
Display server supports changing the screen orientation.Android, iOS
FeatureFEATURE_SWAP_BUFFERS=16
Display server supports V-Sync status can be changed from the default (which is forced to be enabled platforms not supporting this feature).Windows, macOS, Linux (X11/Wayland)
FeatureFEATURE_CLIPBOARD_PRIMARY=18
Display server supports Primary clipboard can be used. This is a different clipboard fromFEATURE_CLIPBOARD.Linux (X11/Wayland)
FeatureFEATURE_TEXT_TO_SPEECH=19
Display server supports text-to-speech. Seetts_*methods.Windows, macOS, Linux (X11/Wayland), Android, iOS, Web
FeatureFEATURE_EXTEND_TO_TITLE=20
Display server supports expanding window content to the title. SeeWINDOW_FLAG_EXTEND_TO_TITLE.macOS
FeatureFEATURE_SCREEN_CAPTURE=21
Display server supports reading screen pixels. Seescreen_get_pixel().
FeatureFEATURE_STATUS_INDICATOR=22
Display server supports application status indicators.
FeatureFEATURE_NATIVE_HELP=23
Display server supports native help system search callbacks. Seehelp_set_search_callbacks().
FeatureFEATURE_NATIVE_DIALOG_INPUT=24
Display server supports spawning text input dialogs using the operating system's native look-and-feel. Seedialog_input_text().Windows, macOS
FeatureFEATURE_NATIVE_DIALOG_FILE=25
Display server supports spawning dialogs for selecting files or directories using the operating system's native look-and-feel. Seefile_dialog_show().Windows, macOS, Linux (X11/Wayland), Android
FeatureFEATURE_NATIVE_DIALOG_FILE_EXTRA=26
The display server supports all features ofFEATURE_NATIVE_DIALOG_FILE, with the added functionality of Options and native dialog file access tores://anduser://paths. Seefile_dialog_show()andfile_dialog_with_options_show().Windows, macOS, Linux (X11/Wayland)
FeatureFEATURE_WINDOW_DRAG=27
The display server supports initiating window drag and resize operations on demand. Seewindow_start_drag()andwindow_start_resize().
FeatureFEATURE_SCREEN_EXCLUDE_FROM_CAPTURE=28
Display server supportsWINDOW_FLAG_EXCLUDE_FROM_CAPTUREwindow flag.Windows, macOS
FeatureFEATURE_WINDOW_EMBEDDING=29
Display server supports embedding a window from another process.Windows, Linux (X11), macOS
FeatureFEATURE_NATIVE_DIALOG_FILE_MIME=30
Native file selection dialog supports MIME types as filters.
FeatureFEATURE_EMOJI_AND_SYMBOL_PICKER=31
Display server supports system emoji and symbol picker.Windows, macOS
FeatureFEATURE_NATIVE_COLOR_PICKER=32
Display server supports native color picker.Linux (X11/Wayland)
FeatureFEATURE_SELF_FITTING_WINDOWS=33
Display server automatically fits popups according to the screen boundaries. Window nodes should not attempt to do that themselves.
FeatureFEATURE_ACCESSIBILITY_SCREEN_READER=34
Display server supports interaction with screen reader or Braille display.Linux (X11/Wayland), macOS, Windows
enumAccessibilityRole:🔗
AccessibilityRoleROLE_UNKNOWN=0
Unknown or custom role.
AccessibilityRoleROLE_DEFAULT_BUTTON=1
Default dialog button element.
AccessibilityRoleROLE_AUDIO=2
Audio player element.
AccessibilityRoleROLE_VIDEO=3
Video player element.
AccessibilityRoleROLE_STATIC_TEXT=4
Non-editable text label.
AccessibilityRoleROLE_CONTAINER=5
Container element. Elements with this role are used for internal structure and ignored by screen readers.
AccessibilityRoleROLE_PANEL=6
Panel container element.
AccessibilityRoleROLE_BUTTON=7
Button element.
AccessibilityRoleROLE_LINK=8
Link element.
AccessibilityRoleROLE_CHECK_BOX=9
Check box element.
AccessibilityRoleROLE_RADIO_BUTTON=10
Radio button element.
AccessibilityRoleROLE_CHECK_BUTTON=11
Check button element.
AccessibilityRoleROLE_SCROLL_BAR=12
Scroll bar element.
AccessibilityRoleROLE_SCROLL_VIEW=13
Scroll container element.
AccessibilityRoleROLE_SPLITTER=14
Container splitter handle element.
AccessibilityRoleROLE_SLIDER=15
Slider element.
AccessibilityRoleROLE_SPIN_BUTTON=16
Spin box element.
AccessibilityRoleROLE_PROGRESS_INDICATOR=17
Progress indicator element.
AccessibilityRoleROLE_TEXT_FIELD=18
Editable text field element.
AccessibilityRoleROLE_MULTILINE_TEXT_FIELD=19
Multiline editable text field element.
AccessibilityRoleROLE_COLOR_PICKER=20
Color picker element.
AccessibilityRoleROLE_TABLE=21
Table element.
AccessibilityRoleROLE_CELL=22
Table/tree cell element.
AccessibilityRoleROLE_ROW=23
Table/tree row element.
AccessibilityRoleROLE_ROW_GROUP=24
Table/tree row group element.
AccessibilityRoleROLE_ROW_HEADER=25
Table/tree row header element.
AccessibilityRoleROLE_COLUMN_HEADER=26
Table/tree column header element.
AccessibilityRoleROLE_TREE=27
Tree view element.
AccessibilityRoleROLE_TREE_ITEM=28
Tree view item element.
AccessibilityRoleROLE_LIST=29
List element.
AccessibilityRoleROLE_LIST_ITEM=30
List item element.
AccessibilityRoleROLE_LIST_BOX=31
List view element.
AccessibilityRoleROLE_LIST_BOX_OPTION=32
List view item element.
AccessibilityRoleROLE_TAB_BAR=33
Tab bar element.
AccessibilityRoleROLE_TAB=34
Tab bar item element.
AccessibilityRoleROLE_TAB_PANEL=35
Tab panel element.
AccessibilityRoleROLE_MENU_BAR=36
Menu bar element.
AccessibilityRoleROLE_MENU=37
Popup menu element.
AccessibilityRoleROLE_MENU_ITEM=38
Popup menu item element.
AccessibilityRoleROLE_MENU_ITEM_CHECK_BOX=39
Popup menu check button item element.
AccessibilityRoleROLE_MENU_ITEM_RADIO=40
Popup menu radio button item element.
AccessibilityRoleROLE_IMAGE=41
Image element.
AccessibilityRoleROLE_WINDOW=42
Window element.
AccessibilityRoleROLE_TITLE_BAR=43
Embedded window title bar element.
AccessibilityRoleROLE_DIALOG=44
Dialog window element.
AccessibilityRoleROLE_TOOLTIP=45
Tooltip element.
enumAccessibilityPopupType:🔗
AccessibilityPopupTypePOPUP_MENU=0
Popup menu.
AccessibilityPopupTypePOPUP_LIST=1
Popup list.
AccessibilityPopupTypePOPUP_TREE=2
Popup tree view.
AccessibilityPopupTypePOPUP_DIALOG=3
Popup dialog.
enumAccessibilityFlags:🔗
AccessibilityFlagsFLAG_HIDDEN=0
Element is hidden for accessibility tools.
AccessibilityFlagsFLAG_MULTISELECTABLE=1
Element supports multiple item selection.
AccessibilityFlagsFLAG_REQUIRED=2
Element require user input.
AccessibilityFlagsFLAG_VISITED=3
Element is a visited link.
AccessibilityFlagsFLAG_BUSY=4
Element content is not ready (e.g. loading).
AccessibilityFlagsFLAG_MODAL=5
Element is modal window.
AccessibilityFlagsFLAG_TOUCH_PASSTHROUGH=6
Element allows touches to be passed through when a screen reader is in touch exploration mode.
AccessibilityFlagsFLAG_READONLY=7
Element is text field with selectable but read-only text.
AccessibilityFlagsFLAG_DISABLED=8
Element is disabled.
AccessibilityFlagsFLAG_CLIPS_CHILDREN=9
Element clips children.
enumAccessibilityAction:🔗
AccessibilityActionACTION_CLICK=0
Single click action, callback argument is not set.
AccessibilityActionACTION_FOCUS=1
Focus action, callback argument is not set.
AccessibilityActionACTION_BLUR=2
Blur action, callback argument is not set.
AccessibilityActionACTION_COLLAPSE=3
Collapse action, callback argument is not set.
AccessibilityActionACTION_EXPAND=4
Expand action, callback argument is not set.
AccessibilityActionACTION_DECREMENT=5
Decrement action, callback argument is not set.
AccessibilityActionACTION_INCREMENT=6
Increment action, callback argument is not set.
AccessibilityActionACTION_HIDE_TOOLTIP=7
Hide tooltip action, callback argument is not set.
AccessibilityActionACTION_SHOW_TOOLTIP=8
Show tooltip action, callback argument is not set.
AccessibilityActionACTION_SET_TEXT_SELECTION=9
Set text selection action, callback argument is set toDictionarywith the following keys:

- "start_element"accessibility element of the selection start.
"start_element"accessibility element of the selection start.
- "start_char"character offset relative to the accessibility element of the selection start.
"start_char"character offset relative to the accessibility element of the selection start.
- "end_element"accessibility element of the selection end.
"end_element"accessibility element of the selection end.
- "end_char"character offset relative to the accessibility element of the selection end.
"end_char"character offset relative to the accessibility element of the selection end.
AccessibilityActionACTION_REPLACE_SELECTED_TEXT=10
Replace text action, callback argument is set toStringwith the replacement text.
AccessibilityActionACTION_SCROLL_BACKWARD=11
Scroll backward action, callback argument is not set.
AccessibilityActionACTION_SCROLL_DOWN=12
Scroll down action, callback argument is set toAccessibilityScrollUnit.
AccessibilityActionACTION_SCROLL_FORWARD=13
Scroll forward action, callback argument is not set.
AccessibilityActionACTION_SCROLL_LEFT=14
Scroll left action, callback argument is set toAccessibilityScrollUnit.
AccessibilityActionACTION_SCROLL_RIGHT=15
Scroll right action, callback argument is set toAccessibilityScrollUnit.
AccessibilityActionACTION_SCROLL_UP=16
Scroll up action, callback argument is set toAccessibilityScrollUnit.
AccessibilityActionACTION_SCROLL_INTO_VIEW=17
Scroll into view action, callback argument is set toAccessibilityScrollHint.
AccessibilityActionACTION_SCROLL_TO_POINT=18
Scroll to point action, callback argument is set toVector2with the relative point coordinates.
AccessibilityActionACTION_SET_SCROLL_OFFSET=19
Set scroll offset action, callback argument is set toVector2with the scroll offset.
AccessibilityActionACTION_SET_VALUE=20
Set value action, callback argument is set toStringor number with the new value.
AccessibilityActionACTION_SHOW_CONTEXT_MENU=21
Show context menu action, callback argument is not set.
AccessibilityActionACTION_CUSTOM=22
Custom action, callback argument is set to the integer action ID.
enumAccessibilityLiveMode:🔗
AccessibilityLiveModeLIVE_OFF=0
Indicates that updates to the live region should not be presented.
AccessibilityLiveModeLIVE_POLITE=1
Indicates that updates to the live region should be presented at the next opportunity (for example at the end of speaking the current sentence).
AccessibilityLiveModeLIVE_ASSERTIVE=2
Indicates that updates to the live region have the highest priority and should be presented immediately.
enumAccessibilityScrollUnit:🔗
AccessibilityScrollUnitSCROLL_UNIT_ITEM=0
The amount by which to scroll. A single item of a list, line of text.
AccessibilityScrollUnitSCROLL_UNIT_PAGE=1
The amount by which to scroll. A single page.
enumAccessibilityScrollHint:🔗
AccessibilityScrollHintSCROLL_HINT_TOP_LEFT=0
A preferred position for the node scrolled into view. Top-left edge of the scroll container.
AccessibilityScrollHintSCROLL_HINT_BOTTOM_RIGHT=1
A preferred position for the node scrolled into view. Bottom-right edge of the scroll container.
AccessibilityScrollHintSCROLL_HINT_TOP_EDGE=2
A preferred position for the node scrolled into view. Top edge of the scroll container.
AccessibilityScrollHintSCROLL_HINT_BOTTOM_EDGE=3
A preferred position for the node scrolled into view. Bottom edge of the scroll container.
AccessibilityScrollHintSCROLL_HINT_LEFT_EDGE=4
A preferred position for the node scrolled into view. Left edge of the scroll container.
AccessibilityScrollHintSCROLL_HINT_RIGHT_EDGE=5
A preferred position for the node scrolled into view. Right edge of the scroll container.
enumMouseMode:🔗
MouseModeMOUSE_MODE_VISIBLE=0
Makes the mouse cursor visible if it is hidden.
MouseModeMOUSE_MODE_HIDDEN=1
Makes the mouse cursor hidden if it is visible.
MouseModeMOUSE_MODE_CAPTURED=2
Captures the mouse. The mouse will be hidden and its position locked at the center of the window manager's window.
Note:If you want to process the mouse's movement in this mode, you need to useInputEventMouseMotion.relative.
MouseModeMOUSE_MODE_CONFINED=3
Confines the mouse cursor to the game window, and make it visible.
MouseModeMOUSE_MODE_CONFINED_HIDDEN=4
Confines the mouse cursor to the game window, and make it hidden.
MouseModeMOUSE_MODE_MAX=5
Max value of theMouseMode.
enumScreenOrientation:🔗
ScreenOrientationSCREEN_LANDSCAPE=0
Default landscape orientation.
ScreenOrientationSCREEN_PORTRAIT=1
Default portrait orientation.
ScreenOrientationSCREEN_REVERSE_LANDSCAPE=2
Reverse landscape orientation (upside down).
ScreenOrientationSCREEN_REVERSE_PORTRAIT=3
Reverse portrait orientation (upside down).
ScreenOrientationSCREEN_SENSOR_LANDSCAPE=4
Automatic landscape orientation (default or reverse depending on sensor).
ScreenOrientationSCREEN_SENSOR_PORTRAIT=5
Automatic portrait orientation (default or reverse depending on sensor).
ScreenOrientationSCREEN_SENSOR=6
Automatic landscape or portrait orientation (default or reverse depending on sensor).
enumVirtualKeyboardType:🔗
VirtualKeyboardTypeKEYBOARD_TYPE_DEFAULT=0
Default text virtual keyboard.
VirtualKeyboardTypeKEYBOARD_TYPE_MULTILINE=1
Multiline virtual keyboard.
VirtualKeyboardTypeKEYBOARD_TYPE_NUMBER=2
Virtual number keypad, useful for PIN entry.
VirtualKeyboardTypeKEYBOARD_TYPE_NUMBER_DECIMAL=3
Virtual number keypad, useful for entering fractional numbers.
VirtualKeyboardTypeKEYBOARD_TYPE_PHONE=4
Virtual phone number keypad.
VirtualKeyboardTypeKEYBOARD_TYPE_EMAIL_ADDRESS=5
Virtual keyboard with additional keys to assist with typing email addresses.
VirtualKeyboardTypeKEYBOARD_TYPE_PASSWORD=6
Virtual keyboard for entering a password. On most platforms, this should disable autocomplete and autocapitalization.
Note:This is not supported on Web. Instead, this behaves identically toKEYBOARD_TYPE_DEFAULT.
VirtualKeyboardTypeKEYBOARD_TYPE_URL=7
Virtual keyboard with additional keys to assist with typing URLs.
enumCursorShape:🔗
CursorShapeCURSOR_ARROW=0
Arrow cursor shape. This is the default when not pointing anything that overrides the mouse cursor, such as aLineEditorTextEdit.
CursorShapeCURSOR_IBEAM=1
I-beam cursor shape. This is used by default when hovering a control that accepts text input, such asLineEditorTextEdit.
CursorShapeCURSOR_POINTING_HAND=2
Pointing hand cursor shape. This is used by default when hovering aLinkButtonor a URL tag in aRichTextLabel.
CursorShapeCURSOR_CROSS=3
Crosshair cursor. This is intended to be displayed when the user needs precise aim over an element, such as a rectangle selection tool or a color picker.
CursorShapeCURSOR_WAIT=4
Wait cursor. On most cursor themes, this displays a spinning iconbesidesthe arrow. Intended to be used for non-blocking operations (when the user can do something else at the moment). See alsoCURSOR_BUSY.
CursorShapeCURSOR_BUSY=5
Wait cursor. On most cursor themes, thisreplacesthe arrow with a spinning icon. Intended to be used for blocking operations (when the user can't do anything else at the moment). See alsoCURSOR_WAIT.
CursorShapeCURSOR_DRAG=6
Dragging hand cursor. This is displayed during drag-and-drop operations. See alsoCURSOR_CAN_DROP.
CursorShapeCURSOR_CAN_DROP=7
"Can drop" cursor. This is displayed during drag-and-drop operations if hovering over aControlthat can accept the drag-and-drop event. On most cursor themes, this displays a dragging hand with an arrow symbol besides it. See alsoCURSOR_DRAG.
CursorShapeCURSOR_FORBIDDEN=8
Forbidden cursor. This is displayed during drag-and-drop operations if the hoveredControlcan't accept the drag-and-drop event.
CursorShapeCURSOR_VSIZE=9
Vertical resize cursor. Intended to be displayed when the hoveredControlcan be vertically resized using the mouse. See alsoCURSOR_VSPLIT.
CursorShapeCURSOR_HSIZE=10
Horizontal resize cursor. Intended to be displayed when the hoveredControlcan be horizontally resized using the mouse. See alsoCURSOR_HSPLIT.
CursorShapeCURSOR_BDIAGSIZE=11
Secondary diagonal resize cursor (top-right/bottom-left). Intended to be displayed when the hoveredControlcan be resized on both axes at once using the mouse.
CursorShapeCURSOR_FDIAGSIZE=12
Main diagonal resize cursor (top-left/bottom-right). Intended to be displayed when the hoveredControlcan be resized on both axes at once using the mouse.
CursorShapeCURSOR_MOVE=13
Move cursor. Intended to be displayed when the hoveredControlcan be moved using the mouse.
CursorShapeCURSOR_VSPLIT=14
Vertical split cursor. This is displayed when hovering aControlwith splits that can be vertically resized using the mouse, such asVSplitContainer. On some cursor themes, this cursor may have the same appearance asCURSOR_VSIZE.
CursorShapeCURSOR_HSPLIT=15
Horizontal split cursor. This is displayed when hovering aControlwith splits that can be horizontally resized using the mouse, such asHSplitContainer. On some cursor themes, this cursor may have the same appearance asCURSOR_HSIZE.
CursorShapeCURSOR_HELP=16
Help cursor. On most cursor themes, this displays a question mark icon instead of the mouse cursor. Intended to be used when the user has requested help on the next element that will be clicked.
CursorShapeCURSOR_MAX=17
Represents the size of theCursorShapeenum.
enumFileDialogMode:🔗
FileDialogModeFILE_DIALOG_MODE_OPEN_FILE=0
The native file dialog allows selecting one, and only one file.
FileDialogModeFILE_DIALOG_MODE_OPEN_FILES=1
The native file dialog allows selecting multiple files.
FileDialogModeFILE_DIALOG_MODE_OPEN_DIR=2
The native file dialog only allows selecting a directory, disallowing the selection of any file.
FileDialogModeFILE_DIALOG_MODE_OPEN_ANY=3
The native file dialog allows selecting one file or directory.
FileDialogModeFILE_DIALOG_MODE_SAVE_FILE=4
The native file dialog will warn when a file exists.
enumWindowMode:🔗
WindowModeWINDOW_MODE_WINDOWED=0
Windowed mode, i.e.Windowdoesn't occupy the whole screen (unless set to the size of the screen).
WindowModeWINDOW_MODE_MINIMIZED=1
Minimized window mode, i.e.Windowis not visible and available on window manager's window list. Normally happens when the minimize button is pressed.
WindowModeWINDOW_MODE_MAXIMIZED=2
Maximized window mode, i.e.Windowwill occupy whole screen area except task bar and still display its borders. Normally happens when the maximize button is pressed.
WindowModeWINDOW_MODE_FULLSCREEN=3
Full screen mode with full multi-window support.
Full screen window covers the entire display area of a screen and has no decorations. The display's video mode is not changed.
On Android:This enables immersive mode.
On macOS:A new desktop is used to display the running project.
Note:Regardless of the platform, enabling full screen will change the window size to match the monitor's size. Therefore, make sure your project supportsmultiple resolutionswhen enabling full screen mode.
WindowModeWINDOW_MODE_EXCLUSIVE_FULLSCREEN=4
A single window full screen mode. This mode has less overhead, but only one window can be open on a given screen at a time (opening a child window or application switching will trigger a full screen transition).
Full screen window covers the entire display area of a screen and has no border or decorations. The display's video mode is not changed.
Note:This mode might not work with screen recording software.
On Android:This enables immersive mode.
On Windows:Depending on video driver, full screen transition might cause screens to go black for a moment.
On macOS:A new desktop is used to display the running project. Exclusive full screen mode prevents Dock and Menu from showing up when the mouse pointer is hovering the edge of the screen.
On Linux (X11):Exclusive full screen mode bypasses compositor.
On Linux (Wayland):Equivalent toWINDOW_MODE_FULLSCREEN.
Note:Regardless of the platform, enabling full screen will change the window size to match the monitor's size. Therefore, make sure your project supportsmultiple resolutionswhen enabling full screen mode.
enumWindowFlags:🔗
WindowFlagsWINDOW_FLAG_RESIZE_DISABLED=0
The window can't be resized by dragging its resize grip. It's still possible to resize the window usingwindow_set_size(). This flag is ignored for full screen windows.
WindowFlagsWINDOW_FLAG_BORDERLESS=1
The window do not have native title bar and other decorations. This flag is ignored for full-screen windows.
WindowFlagsWINDOW_FLAG_ALWAYS_ON_TOP=2
The window is floating on top of all other windows. This flag is ignored for full-screen windows.
WindowFlagsWINDOW_FLAG_TRANSPARENT=3
The window background can be transparent.
Note:This flag has no effect ifis_window_transparency_available()returnsfalse.
Note:Transparency support is implemented on Linux (X11/Wayland), macOS, and Windows, but availability might vary depending on GPU driver, display manager, and compositor capabilities.
Note:Transparency support is implemented on Android, but can only be enabled viaProjectSettings.display/window/per_pixel_transparency/allowed. This flag has no effect on Android.
WindowFlagsWINDOW_FLAG_NO_FOCUS=4
The window can't be focused. No-focus window will ignore all input, except mouse clicks.
WindowFlagsWINDOW_FLAG_POPUP=5
Window is part of menu orOptionButtondropdown. This flag can't be changed when the window is visible. An active popup window will exclusively receive all input, without stealing focus from its parent. Popup windows are automatically closed when uses click outside it, or when an application is switched. Popup window must have transient parent set (seewindow_set_transient()).
WindowFlagsWINDOW_FLAG_EXTEND_TO_TITLE=6
Window content is expanded to the full size of the window. Unlike borderless window, the frame is left intact and can be used to resize the window, title bar is transparent, but have minimize/maximize/close buttons.
Usewindow_set_window_buttons_offset()to adjust minimize/maximize/close buttons offset.
Usewindow_get_safe_title_margins()to determine area under the title bar that is not covered by decorations.
Note:This flag is implemented only on macOS.
WindowFlagsWINDOW_FLAG_MOUSE_PASSTHROUGH=7
All mouse events are passed to the underlying window of the same application.
WindowFlagsWINDOW_FLAG_SHARP_CORNERS=8
Window style is overridden, forcing sharp corners.
Note:This flag is implemented only on Windows (11).
WindowFlagsWINDOW_FLAG_EXCLUDE_FROM_CAPTURE=9
Window is excluded from screenshots taken byscreen_get_image(),screen_get_image_rect(), andscreen_get_pixel().
Note:This flag is implemented on macOS and Windows (10, 20H1).
Note:Setting this flag will prevent standard screenshot methods from capturing a window image, but doesNOTguarantee that other apps won't be able to capture an image. It should not be used as a DRM or security measure.
WindowFlagsWINDOW_FLAG_POPUP_WM_HINT=10
Signals the window manager that this window is supposed to be an implementation-defined "popup" (usually a floating, borderless, untileable and immovable child window).
WindowFlagsWINDOW_FLAG_MINIMIZE_DISABLED=11
Window minimize button is disabled.
Note:This flag is implemented on macOS and Windows.
WindowFlagsWINDOW_FLAG_MAXIMIZE_DISABLED=12
Window maximize button is disabled.
Note:This flag is implemented on macOS and Windows.
WindowFlagsWINDOW_FLAG_MAX=13
Represents the size of theWindowFlagsenum.
enumWindowEvent:🔗
WindowEventWINDOW_EVENT_MOUSE_ENTER=0
Sent when the mouse pointer enters the window.
WindowEventWINDOW_EVENT_MOUSE_EXIT=1
Sent when the mouse pointer exits the window.
WindowEventWINDOW_EVENT_FOCUS_IN=2
Sent when the window grabs focus.
WindowEventWINDOW_EVENT_FOCUS_OUT=3
Sent when the window loses focus.
WindowEventWINDOW_EVENT_CLOSE_REQUEST=4
Sent when the user has attempted to close the window (e.g. close button is pressed).
WindowEventWINDOW_EVENT_GO_BACK_REQUEST=5
Sent when the device "Back" button is pressed.
Note:This event is implemented only on Android.
WindowEventWINDOW_EVENT_DPI_CHANGE=6
Sent when the window is moved to the display with different DPI, or display DPI is changed.
Note:This flag is implemented only on macOS and Linux (Wayland).
WindowEventWINDOW_EVENT_TITLEBAR_CHANGE=7
Sent when the window title bar decoration is changed (e.g.WINDOW_FLAG_EXTEND_TO_TITLEis set or window entered/exited full screen mode).
Note:This flag is implemented only on macOS.
WindowEventWINDOW_EVENT_FORCE_CLOSE=8
Sent when the window has been forcibly closed by the display server. The window will immediately hide and clean any internal rendering references.
Note:This flag is implemented only on Linux (Wayland).
enumWindowResizeEdge:🔗
WindowResizeEdgeWINDOW_EDGE_TOP_LEFT=0
Top-left edge of a window.
WindowResizeEdgeWINDOW_EDGE_TOP=1
Top edge of a window.
WindowResizeEdgeWINDOW_EDGE_TOP_RIGHT=2
Top-right edge of a window.
WindowResizeEdgeWINDOW_EDGE_LEFT=3
Left edge of a window.
WindowResizeEdgeWINDOW_EDGE_RIGHT=4
Right edge of a window.
WindowResizeEdgeWINDOW_EDGE_BOTTOM_LEFT=5
Bottom-left edge of a window.
WindowResizeEdgeWINDOW_EDGE_BOTTOM=6
Bottom edge of a window.
WindowResizeEdgeWINDOW_EDGE_BOTTOM_RIGHT=7
Bottom-right edge of a window.
WindowResizeEdgeWINDOW_EDGE_MAX=8
Represents the size of theWindowResizeEdgeenum.
enumVSyncMode:🔗
VSyncModeVSYNC_DISABLED=0
No vertical synchronization, which means the engine will display frames as fast as possible (tearing may be visible). Framerate is unlimited (regardless ofEngine.max_fps).
VSyncModeVSYNC_ENABLED=1
Default vertical synchronization mode, the image is displayed only on vertical blanking intervals (no tearing is visible). Framerate is limited by the monitor refresh rate (regardless ofEngine.max_fps).
VSyncModeVSYNC_ADAPTIVE=2
Behaves likeVSYNC_DISABLEDwhen the framerate drops below the screen's refresh rate to reduce stuttering (tearing may be visible). Otherwise, vertical synchronization is enabled to avoid tearing. Framerate is limited by the monitor refresh rate (regardless ofEngine.max_fps). Behaves likeVSYNC_ENABLEDwhen using the Compatibility rendering method.
VSyncModeVSYNC_MAILBOX=3
Displays the most recent image in the queue on vertical blanking intervals, while rendering to the other images (no tearing is visible). Framerate is unlimited (regardless ofEngine.max_fps).
Although not guaranteed, the images can be rendered as fast as possible, which may reduce input lag (also called "Fast" V-Sync mode).VSYNC_MAILBOXworks best when at least twice as many frames as the display refresh rate are rendered. Behaves likeVSYNC_ENABLEDwhen using the Compatibility rendering method.
enumHandleType:🔗
HandleTypeDISPLAY_HANDLE=0
Display handle:
- Linux (X11):X11::Display*for the display.
Linux (X11):X11::Display*for the display.
- Linux (Wayland):wl_displayfor the display.
Linux (Wayland):wl_displayfor the display.
- Android:EGLDisplayfor the display.
Android:EGLDisplayfor the display.
HandleTypeWINDOW_HANDLE=1
Window handle:
- Windows:HWNDfor the window.
Windows:HWNDfor the window.
- Linux (X11):X11::Window*for the window.
Linux (X11):X11::Window*for the window.
- Linux (Wayland):wl_surfacefor the window.
Linux (Wayland):wl_surfacefor the window.
- macOS:NSWindow*for the window.
macOS:NSWindow*for the window.
- iOS:UIViewController*for the view controller.
iOS:UIViewController*for the view controller.
- Android:jObjectfor the activity.
Android:jObjectfor the activity.
HandleTypeWINDOW_VIEW=2
Window view:
- Windows:HDCfor the window (only with the Compatibility renderer).
Windows:HDCfor the window (only with the Compatibility renderer).
- macOS:NSView*for the window main view.
macOS:NSView*for the window main view.
- iOS:UIView*for the window main view.
iOS:UIView*for the window main view.
HandleTypeOPENGL_CONTEXT=3
OpenGL context (only with the Compatibility renderer):
- Windows:HGLRCfor the window (native GL), orEGLContextfor the window (ANGLE).
Windows:HGLRCfor the window (native GL), orEGLContextfor the window (ANGLE).
- Linux (X11):GLXContext*for the window.
Linux (X11):GLXContext*for the window.
- Linux (Wayland):EGLContextfor the window.
Linux (Wayland):EGLContextfor the window.
- macOS:NSOpenGLContext*for the window (native GL), orEGLContextfor the window (ANGLE).
macOS:NSOpenGLContext*for the window (native GL), orEGLContextfor the window (ANGLE).
- Android:EGLContextfor the window.
Android:EGLContextfor the window.
HandleTypeEGL_DISPLAY=4
- Windows:EGLDisplayfor the window (ANGLE).
Windows:EGLDisplayfor the window (ANGLE).
- macOS:EGLDisplayfor the window (ANGLE).
macOS:EGLDisplayfor the window (ANGLE).
- Linux (Wayland):EGLDisplayfor the window.
Linux (Wayland):EGLDisplayfor the window.
HandleTypeEGL_CONFIG=5
- Windows:EGLConfigfor the window (ANGLE).
Windows:EGLConfigfor the window (ANGLE).
- macOS:EGLConfigfor the window (ANGLE).
macOS:EGLConfigfor the window (ANGLE).
- Linux (Wayland):EGLConfigfor the window.
Linux (Wayland):EGLConfigfor the window.
enumTTSUtteranceEvent:🔗
TTSUtteranceEventTTS_UTTERANCE_STARTED=0
Utterance has begun to be spoken.
TTSUtteranceEventTTS_UTTERANCE_ENDED=1
Utterance was successfully finished.
TTSUtteranceEventTTS_UTTERANCE_CANCELED=2
Utterance was canceled, or TTS service was unable to process it.
TTSUtteranceEventTTS_UTTERANCE_BOUNDARY=3
Utterance reached a word or sentence boundary.

## Constants

INVALID_SCREEN=-1🔗
The ID that refers to a screen that does not exist. This is returned by someDisplayServermethods if no screen matches the requested result.
SCREEN_WITH_MOUSE_FOCUS=-4🔗
Represents the screen containing the mouse pointer.
Note:On Android, iOS, Web, and Linux (Wayland), this constant always represents the screen at index0.
SCREEN_WITH_KEYBOARD_FOCUS=-3🔗
Represents the screen containing the window with the keyboard focus.
Note:On Android, iOS, Web, and Linux (Wayland), this constant always represents the screen at index0.
SCREEN_PRIMARY=-2🔗
Represents the primary screen.
Note:On Android, iOS, Web, and Linux (Wayland), this constant always represents the screen at index0.
SCREEN_OF_MAIN_WINDOW=-1🔗
Represents the screen where the main window is located. This is usually the default value in functions that allow specifying one of several screens.
Note:On Android, iOS, Web, and Linux (Wayland), this constant always represents the screen at index0.
MAIN_WINDOW_ID=0🔗
The ID of the main window spawned by the engine, which can be passed to methods expecting awindow_id.
INVALID_WINDOW_ID=-1🔗
The ID that refers to a nonexistent window. This is returned by someDisplayServermethods if no window matches the requested result.
INVALID_INDICATOR_ID=-1🔗
The ID that refers to a nonexistent application status indicator.

## Method Descriptions

RIDaccessibility_create_element(window_id:int, role:AccessibilityRole)🔗
Creates a new, empty accessibility element resource.
Note:An accessibility element is created and freed automatically for eachNode. In general, this function should not be called manually.
RIDaccessibility_create_sub_element(parent_rid:RID, role:AccessibilityRole, insert_pos:int= -1)🔗
Creates a new, empty accessibility sub-element resource. Sub-elements can be used to provide accessibility information for objects which are notNodes, such as list items, table cells, or menu items. Sub-elements are freed automatically when the parent element is freed, or can be freed early using theaccessibility_free_element()method.
RIDaccessibility_create_sub_text_edit_elements(parent_rid:RID, shaped_text:RID, min_height:float, insert_pos:int= -1, is_last_line:bool= false)🔗
Creates a new, empty accessibility sub-element from the shaped text buffer. Sub-elements are freed automatically when the parent element is freed, or can be freed early using theaccessibility_free_element()method.
Ifis_last_lineistrue, no trailing newline is appended to the text content. Set totruefor the last line in multi-line text fields and for single-line text fields.
Variantaccessibility_element_get_meta(id:RID)const🔗
Returns the metadata of the accessibility elementid.
voidaccessibility_element_set_meta(id:RID, meta:Variant)🔗
Sets the metadata of the accessibility elementidtometa.
voidaccessibility_free_element(id:RID)🔗
Frees the accessibility elementidcreated byaccessibility_create_element(),accessibility_create_sub_element(), oraccessibility_create_sub_text_edit_elements().
RIDaccessibility_get_window_root(window_id:int)const🔗
Returns the main accessibility element of the OS native window.
boolaccessibility_has_element(id:RID)const🔗
Returnstrueifidis a valid accessibility element.
intaccessibility_screen_reader_active()const🔗
Returns1if a screen reader, Braille display or other assistive app is active,0otherwise. Returns-1if status is unknown.
Note:This method is implemented on Linux, macOS, and Windows.
Note:Accessibility debugging tools, such as Accessibility Insights for Windows, Accessibility Inspector (macOS), or AT-SPI Browser (Linux/BSD), do not count as assistive apps and will not affect this value. To test your project with these tools, setProjectSettings.accessibility/general/accessibility_supportto1.
voidaccessibility_set_window_focused(window_id:int, focused:bool)🔗
Sets the window focused state for assistive apps.
Note:This method is implemented on Linux, macOS, and Windows.
Note:Advanced users only!Windowobjects call this method automatically.
voidaccessibility_set_window_rect(window_id:int, rect_out:Rect2, rect_in:Rect2)🔗
Sets window outer (with decorations) and inner (without decorations) bounds for assistive apps.
Note:This method is implemented on Linux, macOS, and Windows.
Note:Advanced users only!Windowobjects call this method automatically.
intaccessibility_should_increase_contrast()const🔗
Returns1if a high-contrast user interface theme should be used,0otherwise. Returns-1if status is unknown.
Note:This method is implemented on Linux (X11/Wayland, GNOME), macOS, and Windows.
intaccessibility_should_reduce_animation()const🔗
Returns1if flashing, blinking, and other moving content that can cause seizures in users with photosensitive epilepsy should be disabled,0otherwise. Returns-1if status is unknown.
Note:This method is implemented on macOS and Windows.
intaccessibility_should_reduce_transparency()const🔗
Returns1if background images, transparency, and other features that can reduce the contrast between the foreground and background should be disabled,0otherwise. Returns-1if status is unknown.
Note:This method is implemented on macOS and Windows.
voidaccessibility_update_add_action(id:RID, action:AccessibilityAction, callable:Callable)🔗
Adds a callback for the accessibility action (action which can be performed by using a special screen reader command or buttons on the Braille display), and marks this action as supported. The action callback receives oneVariantargument, which value depends on action type.
voidaccessibility_update_add_child(id:RID, child_id:RID)🔗
Adds a child accessibility element.
Note:Nodechildren and sub-elements are added to the child list automatically.
voidaccessibility_update_add_custom_action(id:RID, action_id:int, action_description:String)🔗
Adds support for a custom accessibility action.action_idis passed as an argument to the callback ofACTION_CUSTOMaction.
voidaccessibility_update_add_related_controls(id:RID, related_id:RID)🔗
Adds an element that is controlled by this element.
voidaccessibility_update_add_related_described_by(id:RID, related_id:RID)🔗
Adds an element that describes this element.
voidaccessibility_update_add_related_details(id:RID, related_id:RID)🔗
Adds an element that details this element.
voidaccessibility_update_add_related_flow_to(id:RID, related_id:RID)🔗
Adds an element that this element flow into.
voidaccessibility_update_add_related_labeled_by(id:RID, related_id:RID)🔗
Adds an element that labels this element.
voidaccessibility_update_add_related_radio_group(id:RID, related_id:RID)🔗
Adds an element that is part of the same radio group.
Note:This method should be called on each element of the group, using all other elements asrelated_id.
voidaccessibility_update_set_active_descendant(id:RID, other_id:RID)🔗
Adds an element that is an active descendant of this element.
voidaccessibility_update_set_background_color(id:RID, color:Color)🔗
Sets element background color.
voidaccessibility_update_set_bounds(id:RID, p_rect:Rect2)🔗
Sets element bounding box, relative to the node position.
voidaccessibility_update_set_checked(id:RID, checekd:bool)🔗
Sets element checked state.
voidaccessibility_update_set_classname(id:RID, classname:String)🔗
Sets element class name.
voidaccessibility_update_set_color_value(id:RID, color:Color)🔗
Sets element color value.
voidaccessibility_update_set_description(id:RID, description:String)🔗
Sets element accessibility description.
voidaccessibility_update_set_error_message(id:RID, other_id:RID)🔗
Sets an element which contains an error message for this element.
voidaccessibility_update_set_extra_info(id:RID, name:String)🔗
Sets element accessibility extra information added to the element name.
voidaccessibility_update_set_flag(id:RID, flag:AccessibilityFlags, value:bool)🔗
Sets element flag.
voidaccessibility_update_set_focus(id:RID)🔗
Sets currently focused element.
voidaccessibility_update_set_foreground_color(id:RID, color:Color)🔗
Sets element foreground color.
voidaccessibility_update_set_in_page_link_target(id:RID, other_id:RID)🔗
Sets target element for the link.
voidaccessibility_update_set_language(id:RID, language:String)🔗
Sets element text language.
voidaccessibility_update_set_list_item_count(id:RID, size:int)🔗
Sets number of items in the list.
voidaccessibility_update_set_list_item_expanded(id:RID, expanded:bool)🔗
Sets list/tree item expanded status.
voidaccessibility_update_set_list_item_index(id:RID, index:int)🔗
Sets the position of the element in the list.
voidaccessibility_update_set_list_item_level(id:RID, level:int)🔗
Sets the hierarchical level of the element in the list.
voidaccessibility_update_set_list_item_selected(id:RID, selected:bool)🔗
Sets list/tree item selected status.
voidaccessibility_update_set_list_orientation(id:RID, vertical:bool)🔗
Sets the orientation of the list elements.
voidaccessibility_update_set_live(id:RID, live:AccessibilityLiveMode)🔗
Sets the priority of the live region updates.
voidaccessibility_update_set_member_of(id:RID, group_id:RID)🔗
Sets the element to be a member of the group.
voidaccessibility_update_set_name(id:RID, name:String)🔗
Sets element accessibility name.
voidaccessibility_update_set_next_on_line(id:RID, other_id:RID)🔗
Sets next element on the line.
voidaccessibility_update_set_num_jump(id:RID, jump:float)🔗
Sets numeric value jump.
voidaccessibility_update_set_num_range(id:RID, min:float, max:float)🔗
Sets numeric value range.
voidaccessibility_update_set_num_step(id:RID, step:float)🔗
Sets numeric value step.
voidaccessibility_update_set_num_value(id:RID, position:float)🔗
Sets numeric value.
voidaccessibility_update_set_placeholder(id:RID, placeholder:String)🔗
Sets placeholder text.
voidaccessibility_update_set_popup_type(id:RID, popup:AccessibilityPopupType)🔗
Sets popup type for popup buttons.
voidaccessibility_update_set_previous_on_line(id:RID, other_id:RID)🔗
Sets previous element on the line.
voidaccessibility_update_set_role(id:RID, role:AccessibilityRole)🔗
Sets element accessibility role.
voidaccessibility_update_set_role_description(id:RID, description:String)🔗
Sets element accessibility role description text.
voidaccessibility_update_set_scroll_x(id:RID, position:float)🔗
Sets scroll bar x position.
voidaccessibility_update_set_scroll_x_range(id:RID, min:float, max:float)🔗
Sets scroll bar x range.
voidaccessibility_update_set_scroll_y(id:RID, position:float)🔗
Sets scroll bar y position.
voidaccessibility_update_set_scroll_y_range(id:RID, min:float, max:float)🔗
Sets scroll bar y range.
voidaccessibility_update_set_shortcut(id:RID, shortcut:String)🔗
Sets the list of keyboard shortcuts used by element.
voidaccessibility_update_set_state_description(id:RID, description:String)🔗
Sets human-readable description of the current checked state.
voidaccessibility_update_set_table_cell_position(id:RID, row_index:int, column_index:int)🔗
Sets cell position in the table.
voidaccessibility_update_set_table_cell_span(id:RID, row_span:int, column_span:int)🔗
Sets cell row/column span.
voidaccessibility_update_set_table_column_count(id:RID, count:int)🔗
Sets number of columns in the table.
voidaccessibility_update_set_table_column_index(id:RID, index:int)🔗
Sets position of the column.
voidaccessibility_update_set_table_row_count(id:RID, count:int)🔗
Sets number of rows in the table.
voidaccessibility_update_set_table_row_index(id:RID, index:int)🔗
Sets position of the row in the table.
voidaccessibility_update_set_text_align(id:RID, align:HorizontalAlignment)🔗
Sets element text alignment.
voidaccessibility_update_set_text_decorations(id:RID, underline:bool, strikethrough:bool, overline:bool)🔗
Sets text underline/overline/strikethrough.
voidaccessibility_update_set_text_orientation(id:RID, vertical:bool)🔗
Sets text orientation.
voidaccessibility_update_set_text_selection(id:RID, text_start_id:RID, start_char:int, text_end_id:RID, end_char:int)🔗
Sets text selection to the text field.text_start_idandtext_end_idshould be elements created byaccessibility_create_sub_text_edit_elements(). Character offsets are relative to the corresponding element.
voidaccessibility_update_set_tooltip(id:RID, tooltip:String)🔗
Sets tooltip text.
voidaccessibility_update_set_transform(id:RID, transform:Transform2D)🔗
Sets element 2D transform.
voidaccessibility_update_set_url(id:RID, url:String)🔗
Sets link URL.
voidaccessibility_update_set_value(id:RID, value:String)🔗
Sets element text value.
voidbeep()const🔗
Plays the beep sound from the operative system, if possible. Because it comes from the OS, the beep sound will be audible even if the application is muted. It may also be disabled for the entire OS by the user.
Note:This method is implemented on macOS, Linux (X11/Wayland), and Windows.
Stringclipboard_get()const🔗
Returns the user's clipboard as a string if possible.
Imageclipboard_get_image()const🔗
Returns the user's clipboard as an image if possible.
Note:This method uses the copied pixel data, e.g. from an image editing software or a web browser, not an image file copied from file explorer.
Stringclipboard_get_primary()const🔗
Returns the user'sprimaryclipboard as a string if possible. This is the clipboard that is set when the user selects text in any application, rather than when pressingCtrl+C. The clipboard data can then be pasted by clicking the middle mouse button in any application that supports the primary clipboard mechanism.
Note:This method is only implemented on Linux (X11/Wayland).
boolclipboard_has()const🔗
Returnstrueif there is a text content on the user's clipboard.
boolclipboard_has_image()const🔗
Returnstrueif there is an image content on the user's clipboard.
voidclipboard_set(clipboard:String)🔗
Sets the user's clipboard content to the given string.
voidclipboard_set_primary(clipboard_primary:String)🔗
Sets the user'sprimaryclipboard content to the given string. This is the clipboard that is set when the user selects text in any application, rather than when pressingCtrl+C. The clipboard data can then be pasted by clicking the middle mouse button in any application that supports the primary clipboard mechanism.
Note:This method is only implemented on Linux (X11/Wayland).
boolcolor_picker(callback:Callable)🔗
Displays OS native color picker.
Callbacks have the following arguments:status:bool,color:Color.
Note:This method is implemented if the display server has theFEATURE_NATIVE_COLOR_PICKERfeature.
Note:This method is only implemented on Linux (X11/Wayland).
intcreate_status_indicator(icon:Texture2D, tooltip:String, callback:Callable)🔗
Creates a new application status indicator with the specified icon, tooltip, and activation callback.
callbackshould take two arguments: the pressed mouse button (one of theMouseButtonconstants) and the click position in screen coordinates (aVector2i).
CursorShapecursor_get_shape()const🔗
Returns the default mouse cursor shape set bycursor_set_shape().
voidcursor_set_custom_image(cursor:Resource, shape:CursorShape= 0, hotspot:Vector2= Vector2(0, 0))🔗
Sets a custom mouse cursor image for the givenshape. This means the user's operating system and mouse cursor theme will no longer influence the mouse cursor's appearance.
cursorcan be either aTexture2Dor anImage, and it should not be larger than 256×256 to display correctly. Optionally,hotspotcan be set to offset the image's position relative to the click point. By default,hotspotis set to the top-left corner of the image. See alsocursor_set_shape().
Note:On Web, calling this method every frame can cause the cursor to flicker.
voidcursor_set_shape(shape:CursorShape)🔗
Sets the default mouse cursor shape. The cursor's appearance will vary depending on the user's operating system and mouse cursor theme. See alsocursor_get_shape()andcursor_set_custom_image().
voiddelete_status_indicator(id:int)🔗
Removes the application status indicator.
Errordialog_input_text(title:String, description:String, existing_text:String, callback:Callable)🔗
Shows a text input dialog which uses the operating system's native look-and-feel.callbackshould accept a singleStringparameter which contains the text field's contents.
Note:This method is implemented if the display server has theFEATURE_NATIVE_DIALOG_INPUTfeature. Supported platforms include macOS, Windows, and Android.
Errordialog_show(title:String, description:String, buttons:PackedStringArray, callback:Callable)🔗
Shows a text dialog which uses the operating system's native look-and-feel.callbackshould accept a singleintparameter which corresponds to the index of the pressed button.
Note:This method is implemented if the display server has theFEATURE_NATIVE_DIALOGfeature. Supported platforms include macOS, Windows, and Android.
voidenable_for_stealing_focus(process_id:int)🔗
Allows theprocess_idPID to steal focus from this window. In other words, this disables the operating system's focus stealing protection for the specified PID.
Note:This method is implemented only on Windows.
Errorfile_dialog_show(title:String, current_directory:String, filename:String, show_hidden:bool, mode:FileDialogMode, filters:PackedStringArray, callback:Callable, parent_window_id:int= 0)🔗
Displays OS native dialog for selecting files or directories in the file system.
Each filter string in thefiltersarray should be formatted like this:*.png,*.jpg,*.jpeg;ImageFiles;image/png,image/jpeg. The description text of the filter is optional and can be omitted. It is recommended to set both file extension and MIME type. See alsoFileDialog.filters.
Callbacks have the following arguments:status:bool,selected_paths:PackedStringArray,selected_filter_index:int.On Android,the third callback argument (selected_filter_index) is always0.
Note:This method is implemented if the display server has theFEATURE_NATIVE_DIALOG_FILEfeature. Supported platforms include Linux (X11/Wayland), Windows, macOS, and Android (API level 29+).
Note:current_directorymight be ignored.
Note:Embedded file dialogs and Windows file dialogs support only file extensions, while Android, Linux, and macOS file dialogs also support MIME types.
Note:On Android and Linux,show_hiddenis ignored.
Note:On Android and macOS, native file dialogs have no title.
Note:On macOS, sandboxed apps will save security-scoped bookmarks to retain access to the opened folders across multiple sessions. UseOS.get_granted_permissions()to get a list of saved bookmarks.
Note:On Android, this method uses the Android Storage Access Framework (SAF).
The file picker returns a URI instead of a filesystem path. This URI can be passed directly toFileAccessto perform read/write operations.
When usingFILE_DIALOG_MODE_OPEN_DIR, it returns a tree URI that grants full access to the selected directory. File operations inside this directory can be performed by passing a path on the formtreeUri#relative/path/to/filetoFileAccess.
To avoid opening the file picker again after each app restart, you can take persistable URI permission as follows:

```
val uri = "content://com.android..." # URI of the selected file or folder.
val persist = true # Set to false to release the persistable permission.
var android_runtime = Engine.get_singleton("AndroidRuntime")
android_runtime.updatePersistableUriPermission(uri, persist)
```

The persistable URI permission remains valid across app restarts as long as the directory is not moved, renamed, or deleted.
Errorfile_dialog_with_options_show(title:String, current_directory:String, root:String, filename:String, show_hidden:bool, mode:FileDialogMode, filters:PackedStringArray, options:Array[Dictionary], callback:Callable, parent_window_id:int= 0)🔗
Displays OS native dialog for selecting files or directories in the file system with additional user selectable options.
Each filter string in thefiltersarray should be formatted like this:*.png,*.jpg,*.jpeg;ImageFiles;image/png,image/jpeg. The description text of the filter is optional and can be omitted. It is recommended to set both file extension and MIME type. See alsoFileDialog.filters.
optionsis array ofDictionarys with the following keys:

- "name"- option's nameString.
"name"- option's nameString.
- "values"-PackedStringArrayof values. If empty, boolean option (check box) is used.
"values"-PackedStringArrayof values. If empty, boolean option (check box) is used.
- "default"- default selected option index (int) or default boolean value (bool).
"default"- default selected option index (int) or default boolean value (bool).
Callbacks have the following arguments:status:bool,selected_paths:PackedStringArray,selected_filter_index:int,selected_option:Dictionary.
Note:This method is implemented if the display server has theFEATURE_NATIVE_DIALOG_FILE_EXTRAfeature. Supported platforms include Linux (X11/Wayland), Windows, and macOS.
Note:current_directorymight be ignored.
Note:Embedded file dialogs and Windows file dialogs support only file extensions, while Android, Linux, and macOS file dialogs also support MIME types.
Note:On Linux (X11),show_hiddenis ignored.
Note:On macOS, native file dialogs have no title.
Note:On macOS, sandboxed apps will save security-scoped bookmarks to retain access to the opened folders across multiple sessions. UseOS.get_granted_permissions()to get a list of saved bookmarks.
voidforce_process_and_drop_events()🔗
Forces window manager processing while ignoring allInputEvents. See alsoprocess_events().
Note:This method is implemented on Windows and macOS.
Colorget_accent_color()const🔗
Returns OS theme accent color. ReturnsColor(0,0,0,0), if accent color is unknown.
Note:This method is implemented on macOS, Windows, Android, and Linux (X11/Wayland).
Colorget_base_color()const🔗
Returns the OS theme base color (default control background). ReturnsColor(0,0,0,0)if the base color is unknown.
Note:This method is implemented on macOS, Windows, and Android.
Array[Rect2]get_display_cutouts()const🔗
Returns anArrayofRect2, each of which is the bounding rectangle for a display cutout or notch. These are non-functional areas on edge-to-edge screens used by cameras and sensors. Returns an empty array if the device does not have cutouts. See alsoget_display_safe_area().
Note:Currently only implemented on Android. Other platforms will return an empty array even if they do have display cutouts or notches.
Rect2iget_display_safe_area()const🔗
Returns the unobscured area of the display where interactive controls should be rendered. See alsoget_display_cutouts().
Note:Currently only implemented on Android and iOS. On other platforms,screen_get_usable_rect(SCREEN_OF_MAIN_WINDOW)will be returned as a fallback. See alsoscreen_get_usable_rect().
intget_keyboard_focus_screen()const🔗
Returns the index of the screen containing the window with the keyboard focus, or the primary screen if there's no focused window.
Note:This method is implemented on Linux/X11, macOS, and Windows. On other platforms, this method always returns the primary screen.
Stringget_name()const🔗
Returns the name of theDisplayServercurrently in use. Most operating systems only have a singleDisplayServer, but Linux has access to more than oneDisplayServer(currently X11 and Wayland).
The names of built-in display servers areWindows,macOS,X11(Linux),Wayland(Linux),Android,iOS,web(HTML5), andheadless(when started with the--headlesscommand line argument).
intget_primary_screen()const🔗
Returns the index of the primary screen.
Note:This method is implemented on Linux/X11, macOS, and Windows. On other platforms, this method always returns0.
intget_screen_count()const🔗
Returns the number of displays available.
Note:This method is implemented on Linux (X11 and Wayland), macOS, and Windows. On other platforms, this method always returns1.
intget_screen_from_rect(rect:Rect2)const🔗
Returns the index of the screen that overlaps the most with the given rectangle. ReturnsINVALID_SCREENif the rectangle doesn't overlap with any screen or has no area.
boolget_swap_cancel_ok()🔗
Returnstrueif positions ofOKandCancelbuttons are swapped in dialogs. This is enabled by default on Windows to follow interface conventions, and be toggled by changingProjectSettings.gui/common/swap_cancel_ok.
Note:This doesn't affect native dialogs such as the ones spawned bydialog_show().
intget_window_at_screen_position(position:Vector2i)const🔗
Returns the ID of the window at the specified screenposition(in pixels). On multi-monitor setups, the screen position is relative to the virtual desktop area. On multi-monitor setups with different screen resolutions or orientations, the origin may be located outside any display like this:

```
* (0, 0)        +-------+
                |       |
+-------------+ |       |
|             | |       |
|             | |       |
+-------------+ +-------+
```

PackedInt32Arrayget_window_list()const🔗
Returns the list of Godot window IDs belonging to this process.
Note:Native dialogs are not included in this list.
intglobal_menu_add_check_item(menu_root:String, label:String, callback:Callable= Callable(), key_callback:Callable= Callable(), tag:Variant= null, accelerator:Key= 0, index:int= -1)🔗
Deprecated:UseNativeMenuorPopupMenuinstead.
Adds a new checkable item with textlabelto the global menu with IDmenu_root.
Returns index of the inserted item, it's not guaranteed to be the same asindexvalue.
Anacceleratorcan optionally be defined, which is a keyboard shortcut that can be pressed to trigger the menu button even if it's not currently open. Theacceleratoris generally a combination ofKeyModifierMasks andKeys using bitwise OR such asKEY_MASK_CTRL|KEY_A(Ctrl+A).
Note:Thecallbackandkey_callbackCallables need to accept exactly one Variant parameter, the parameter passed to the Callables will be the value passed totag.
Note:This method is implemented only on macOS.
Supported system menu IDs:

```
"_main" - Main menu (macOS).
"_dock" - Dock popup menu (macOS).
"_apple" - Apple menu (macOS, custom items added before "Services").
"_window" - Window menu (macOS, custom items added after "Bring All to Front").
"_help" - Help menu (macOS).
```

intglobal_menu_add_icon_check_item(menu_root:String, icon:Texture2D, label:String, callback:Callable= Callable(), key_callback:Callable= Callable(), tag:Variant= null, accelerator:Key= 0, index:int= -1)🔗
Deprecated:UseNativeMenuorPopupMenuinstead.
Adds a new checkable item with textlabeland iconiconto the global menu with IDmenu_root.
Returns index of the inserted item, it's not guaranteed to be the same asindexvalue.
Anacceleratorcan optionally be defined, which is a keyboard shortcut that can be pressed to trigger the menu button even if it's not currently open. Theacceleratoris generally a combination ofKeyModifierMasks andKeys using bitwise OR such asKEY_MASK_CTRL|KEY_A(Ctrl+A).
Note:Thecallbackandkey_callbackCallables need to accept exactly one Variant parameter, the parameter passed to the Callables will be the value passed totag.
Note:This method is implemented only on macOS.
Supported system menu IDs:

```
"_main" - Main menu (macOS).
"_dock" - Dock popup menu (macOS).
"_apple" - Apple menu (macOS, custom items added before "Services").
"_window" - Window menu (macOS, custom items added after "Bring All to Front").
"_help" - Help menu (macOS).
```

intglobal_menu_add_icon_item(menu_root:String, icon:Texture2D, label:String, callback:Callable= Callable(), key_callback:Callable= Callable(), tag:Variant= null, accelerator:Key= 0, index:int= -1)🔗
Deprecated:UseNativeMenuorPopupMenuinstead.
Adds a new item with textlabeland iconiconto the global menu with IDmenu_root.
Returns index of the inserted item, it's not guaranteed to be the same asindexvalue.
Anacceleratorcan optionally be defined, which is a keyboard shortcut that can be pressed to trigger the menu button even if it's not currently open. Theacceleratoris generally a combination ofKeyModifierMasks andKeys using bitwise OR such asKEY_MASK_CTRL|KEY_A(Ctrl+A).
Note:Thecallbackandkey_callbackCallables need to accept exactly one Variant parameter, the parameter passed to the Callables will be the value passed totag.
Note:This method is implemented only on macOS.
Supported system menu IDs:

```
"_main" - Main menu (macOS).
"_dock" - Dock popup menu (macOS).
"_apple" - Apple menu (macOS, custom items added before "Services").
"_window" - Window menu (macOS, custom items added after "Bring All to Front").
"_help" - Help menu (macOS).
```

intglobal_menu_add_icon_radio_check_item(menu_root:String, icon:Texture2D, label:String, callback:Callable= Callable(), key_callback:Callable= Callable(), tag:Variant= null, accelerator:Key= 0, index:int= -1)🔗
Deprecated:UseNativeMenuorPopupMenuinstead.
Adds a new radio-checkable item with textlabeland iconiconto the global menu with IDmenu_root.
Returns index of the inserted item, it's not guaranteed to be the same asindexvalue.
Anacceleratorcan optionally be defined, which is a keyboard shortcut that can be pressed to trigger the menu button even if it's not currently open. Theacceleratoris generally a combination ofKeyModifierMasks andKeys using bitwise OR such asKEY_MASK_CTRL|KEY_A(Ctrl+A).
Note:Radio-checkable items just display a checkmark, but don't have any built-in checking behavior and must be checked/unchecked manually. Seeglobal_menu_set_item_checked()for more info on how to control it.
Note:Thecallbackandkey_callbackCallables need to accept exactly one Variant parameter, the parameter passed to the Callables will be the value passed totag.
Note:This method is implemented only on macOS.
Supported system menu IDs:

```
"_main" - Main menu (macOS).
"_dock" - Dock popup menu (macOS).
"_apple" - Apple menu (macOS, custom items added before "Services").
"_window" - Window menu (macOS, custom items added after "Bring All to Front").
"_help" - Help menu (macOS).
```

intglobal_menu_add_item(menu_root:String, label:String, callback:Callable= Callable(), key_callback:Callable= Callable(), tag:Variant= null, accelerator:Key= 0, index:int= -1)🔗
Deprecated:UseNativeMenuorPopupMenuinstead.
Adds a new item with textlabelto the global menu with IDmenu_root.
Returns index of the inserted item, it's not guaranteed to be the same asindexvalue.
Anacceleratorcan optionally be defined, which is a keyboard shortcut that can be pressed to trigger the menu button even if it's not currently open. Theacceleratoris generally a combination ofKeyModifierMasks andKeys using bitwise OR such asKEY_MASK_CTRL|KEY_A(Ctrl+A).
Note:Thecallbackandkey_callbackCallables need to accept exactly one Variant parameter, the parameter passed to the Callables will be the value passed totag.
Note:This method is implemented only on macOS.
Supported system menu IDs:

```
"_main" - Main menu (macOS).
"_dock" - Dock popup menu (macOS).
"_apple" - Apple menu (macOS, custom items added before "Services").
"_window" - Window menu (macOS, custom items added after "Bring All to Front").
"_help" - Help menu (macOS).
```

intglobal_menu_add_multistate_item(menu_root:String, label:String, max_states:int, default_state:int, callback:Callable= Callable(), key_callback:Callable= Callable(), tag:Variant= null, accelerator:Key= 0, index:int= -1)🔗
Deprecated:UseNativeMenuorPopupMenuinstead.
Adds a new item with textlabelto the global menu with IDmenu_root.
Contrarily to normal binary items, multistate items can have more than two states, as defined bymax_states. Each press or activate of the item will increase the state by one. The default value is defined bydefault_state.
Returns index of the inserted item, it's not guaranteed to be the same asindexvalue.
Anacceleratorcan optionally be defined, which is a keyboard shortcut that can be pressed to trigger the menu button even if it's not currently open. Theacceleratoris generally a combination ofKeyModifierMasks andKeys using bitwise OR such asKEY_MASK_CTRL|KEY_A(Ctrl+A).
Note:By default, there's no indication of the current item state, it should be changed manually.
Note:Thecallbackandkey_callbackCallables need to accept exactly one Variant parameter, the parameter passed to the Callables will be the value passed totag.
Note:This method is implemented only on macOS.
Supported system menu IDs:

```
"_main" - Main menu (macOS).
"_dock" - Dock popup menu (macOS).
"_apple" - Apple menu (macOS, custom items added before "Services").
"_window" - Window menu (macOS, custom items added after "Bring All to Front").
"_help" - Help menu (macOS).
```

intglobal_menu_add_radio_check_item(menu_root:String, label:String, callback:Callable= Callable(), key_callback:Callable= Callable(), tag:Variant= null, accelerator:Key= 0, index:int= -1)🔗
Deprecated:UseNativeMenuorPopupMenuinstead.
Adds a new radio-checkable item with textlabelto the global menu with IDmenu_root.
Returns index of the inserted item, it's not guaranteed to be the same asindexvalue.
Anacceleratorcan optionally be defined, which is a keyboard shortcut that can be pressed to trigger the menu button even if it's not currently open. Theacceleratoris generally a combination ofKeyModifierMasks andKeys using bitwise OR such asKEY_MASK_CTRL|KEY_A(Ctrl+A).
Note:Radio-checkable items just display a checkmark, but don't have any built-in checking behavior and must be checked/unchecked manually. Seeglobal_menu_set_item_checked()for more info on how to control it.
Note:Thecallbackandkey_callbackCallables need to accept exactly one Variant parameter, the parameter passed to the Callables will be the value passed totag.
Note:This method is implemented only on macOS.
Supported system menu IDs:

```
"_main" - Main menu (macOS).
"_dock" - Dock popup menu (macOS).
"_apple" - Apple menu (macOS, custom items added before "Services").
"_window" - Window menu (macOS, custom items added after "Bring All to Front").
"_help" - Help menu (macOS).
```

intglobal_menu_add_separator(menu_root:String, index:int= -1)🔗
Deprecated:UseNativeMenuorPopupMenuinstead.
Adds a separator between items to the global menu with IDmenu_root. Separators also occupy an index.
Returns index of the inserted item, it's not guaranteed to be the same asindexvalue.
Note:This method is implemented only on macOS.
Supported system menu IDs:

```
"_main" - Main menu (macOS).
"_dock" - Dock popup menu (macOS).
"_apple" - Apple menu (macOS, custom items added before "Services").
"_window" - Window menu (macOS, custom items added after "Bring All to Front").
"_help" - Help menu (macOS).
```

intglobal_menu_add_submenu_item(menu_root:String, label:String, submenu:String, index:int= -1)🔗
Deprecated:UseNativeMenuorPopupMenuinstead.
Adds an item that will act as a submenu of the global menumenu_root. Thesubmenuargument is the ID of the global menu root that will be shown when the item is clicked.
Returns index of the inserted item, it's not guaranteed to be the same asindexvalue.
Note:This method is implemented only on macOS.
Supported system menu IDs:

```
"_main" - Main menu (macOS).
"_dock" - Dock popup menu (macOS).
"_apple" - Apple menu (macOS, custom items added before "Services").
"_window" - Window menu (macOS, custom items added after "Bring All to Front").
"_help" - Help menu (macOS).
```

voidglobal_menu_clear(menu_root:String)🔗
Deprecated:UseNativeMenuorPopupMenuinstead.
Removes all items from the global menu with IDmenu_root.
Note:This method is implemented only on macOS.
Supported system menu IDs:

```
"_main" - Main menu (macOS).
"_dock" - Dock popup menu (macOS).
"_apple" - Apple menu (macOS, custom items added before "Services").
"_window" - Window menu (macOS, custom items added after "Bring All to Front").
"_help" - Help menu (macOS).
```

Keyglobal_menu_get_item_accelerator(menu_root:String, idx:int)const🔗
Deprecated:UseNativeMenuorPopupMenuinstead.
Returns the accelerator of the item at indexidx. Accelerators are special combinations of keys that activate the item, no matter which control is focused.
Note:This method is implemented only on macOS.
Callableglobal_menu_get_item_callback(menu_root:String, idx:int)const🔗
Deprecated:UseNativeMenuorPopupMenuinstead.
Returns the callback of the item at indexidx.
Note:This method is implemented only on macOS.
intglobal_menu_get_item_count(menu_root:String)const🔗
Deprecated:UseNativeMenuorPopupMenuinstead.
Returns number of items in the global menu with IDmenu_root.
Note:This method is implemented only on macOS.
Texture2Dglobal_menu_get_item_icon(menu_root:String, idx:int)const🔗
Deprecated:UseNativeMenuorPopupMenuinstead.
Returns the icon of the item at indexidx.
Note:This method is implemented only on macOS.
intglobal_menu_get_item_indentation_level(menu_root:String, idx:int)const🔗
Deprecated:UseNativeMenuorPopupMenuinstead.
Returns the horizontal offset of the item at the givenidx.
Note:This method is implemented only on macOS.
intglobal_menu_get_item_index_from_tag(menu_root:String, tag:Variant)const🔗
Deprecated:UseNativeMenuorPopupMenuinstead.
Returns the index of the item with the specifiedtag. Indices are automatically assigned to each item by the engine, and cannot be set manually.
Note:This method is implemented only on macOS.
intglobal_menu_get_item_index_from_text(menu_root:String, text:String)const🔗
Deprecated:UseNativeMenuorPopupMenuinstead.
Returns the index of the item with the specifiedtext. Indices are automatically assigned to each item by the engine, and cannot be set manually.
Note:This method is implemented only on macOS.
Callableglobal_menu_get_item_key_callback(menu_root:String, idx:int)const🔗
Deprecated:UseNativeMenuorPopupMenuinstead.
Returns the callback of the item accelerator at indexidx.
Note:This method is implemented only on macOS.
intglobal_menu_get_item_max_states(menu_root:String, idx:int)const🔗
Deprecated:UseNativeMenuorPopupMenuinstead.
Returns number of states of a multistate item. Seeglobal_menu_add_multistate_item()for details.
Note:This method is implemented only on macOS.
intglobal_menu_get_item_state(menu_root:String, idx:int)const🔗
Deprecated:UseNativeMenuorPopupMenuinstead.
Returns the state of a multistate item. Seeglobal_menu_add_multistate_item()for details.
Note:This method is implemented only on macOS.
Stringglobal_menu_get_item_submenu(menu_root:String, idx:int)const🔗
Deprecated:UseNativeMenuorPopupMenuinstead.
Returns the submenu ID of the item at indexidx. Seeglobal_menu_add_submenu_item()for more info on how to add a submenu.
Note:This method is implemented only on macOS.
Variantglobal_menu_get_item_tag(menu_root:String, idx:int)const🔗
Deprecated:UseNativeMenuorPopupMenuinstead.
Returns the metadata of the specified item, which might be of any type. You can set it withglobal_menu_set_item_tag(), which provides a simple way of assigning context data to items.
Note:This method is implemented only on macOS.
Stringglobal_menu_get_item_text(menu_root:String, idx:int)const🔗
Deprecated:UseNativeMenuorPopupMenuinstead.
Returns the text of the item at indexidx.
Note:This method is implemented only on macOS.
Stringglobal_menu_get_item_tooltip(menu_root:String, idx:int)const🔗
Deprecated:UseNativeMenuorPopupMenuinstead.
Returns the tooltip associated with the specified indexidx.
Note:This method is implemented only on macOS.
Dictionaryglobal_menu_get_system_menu_roots()const🔗
Deprecated:UseNativeMenuorPopupMenuinstead.
Returns Dictionary of supported system menu IDs and names.
Note:This method is implemented only on macOS.
boolglobal_menu_is_item_checkable(menu_root:String, idx:int)const🔗
Deprecated:UseNativeMenuorPopupMenuinstead.
Returnstrueif the item at indexidxis checkable in some way, i.e. if it has a checkbox or radio button.
Note:This method is implemented only on macOS.
boolglobal_menu_is_item_checked(menu_root:String, idx:int)const🔗
Deprecated:UseNativeMenuorPopupMenuinstead.
Returnstrueif the item at indexidxis checked.
Note:This method is implemented only on macOS.
boolglobal_menu_is_item_disabled(menu_root:String, idx:int)const🔗
Deprecated:UseNativeMenuorPopupMenuinstead.
Returnstrueif the item at indexidxis disabled. When it is disabled it can't be selected, or its action invoked.
Seeglobal_menu_set_item_disabled()for more info on how to disable an item.
Note:This method is implemented only on macOS.
boolglobal_menu_is_item_hidden(menu_root:String, idx:int)const🔗
Deprecated:UseNativeMenuorPopupMenuinstead.
Returnstrueif the item at indexidxis hidden.
Seeglobal_menu_set_item_hidden()for more info on how to hide an item.
Note:This method is implemented only on macOS.
boolglobal_menu_is_item_radio_checkable(menu_root:String, idx:int)const🔗
Deprecated:UseNativeMenuorPopupMenuinstead.
Returnstrueif the item at indexidxhas radio button-style checkability.
Note:This is purely cosmetic; you must add the logic for checking/unchecking items in radio groups.
Note:This method is implemented only on macOS.
voidglobal_menu_remove_item(menu_root:String, idx:int)🔗
Deprecated:UseNativeMenuorPopupMenuinstead.
Removes the item at indexidxfrom the global menumenu_root.
Note:The indices of items after the removed item will be shifted by one.
Note:This method is implemented only on macOS.
voidglobal_menu_set_item_accelerator(menu_root:String, idx:int, keycode:Key)🔗
Deprecated:UseNativeMenuorPopupMenuinstead.
Sets the accelerator of the item at indexidx.keycodecan be a singleKey, or a combination ofKeyModifierMasks andKeys using bitwise OR such asKEY_MASK_CTRL|KEY_A(Ctrl+A).
Note:This method is implemented only on macOS.
voidglobal_menu_set_item_callback(menu_root:String, idx:int, callback:Callable)🔗
Deprecated:UseNativeMenuorPopupMenuinstead.
Sets the callback of the item at indexidx. Callback is emitted when an item is pressed.
Note:ThecallbackCallable needs to accept exactly one Variant parameter, the parameter passed to the Callable will be the value passed to thetagparameter when the menu item was created.
Note:This method is implemented only on macOS.
voidglobal_menu_set_item_checkable(menu_root:String, idx:int, checkable:bool)🔗
Deprecated:UseNativeMenuorPopupMenuinstead.
Sets whether the item at indexidxhas a checkbox. Iffalse, sets the type of the item to plain text.
Note:This method is implemented only on macOS.
voidglobal_menu_set_item_checked(menu_root:String, idx:int, checked:bool)🔗
Deprecated:UseNativeMenuorPopupMenuinstead.
Sets the checkstate status of the item at indexidx.
Note:This method is implemented only on macOS.
voidglobal_menu_set_item_disabled(menu_root:String, idx:int, disabled:bool)🔗
Deprecated:UseNativeMenuorPopupMenuinstead.
Enables/disables the item at indexidx. When it is disabled, it can't be selected and its action can't be invoked.
Note:This method is implemented only on macOS.
voidglobal_menu_set_item_hidden(menu_root:String, idx:int, hidden:bool)🔗
Deprecated:UseNativeMenuorPopupMenuinstead.
Hides/shows the item at indexidx. When it is hidden, an item does not appear in a menu and its action cannot be invoked.
Note:This method is implemented only on macOS.
voidglobal_menu_set_item_hover_callbacks(menu_root:String, idx:int, callback:Callable)🔗
Deprecated:UseNativeMenuorPopupMenuinstead.
Sets the callback of the item at indexidx. The callback is emitted when an item is hovered.
Note:ThecallbackCallable needs to accept exactly one Variant parameter, the parameter passed to the Callable will be the value passed to thetagparameter when the menu item was created.
Note:This method is implemented only on macOS.
voidglobal_menu_set_item_icon(menu_root:String, idx:int, icon:Texture2D)🔗
Deprecated:UseNativeMenuorPopupMenuinstead.
Replaces theTexture2Dicon of the specifiedidx.
Note:This method is implemented only on macOS.
Note:This method is not supported by macOS "_dock" menu items.
voidglobal_menu_set_item_indentation_level(menu_root:String, idx:int, level:int)🔗
Deprecated:UseNativeMenuorPopupMenuinstead.
Sets the horizontal offset of the item at the givenidx.
Note:This method is implemented only on macOS.
voidglobal_menu_set_item_key_callback(menu_root:String, idx:int, key_callback:Callable)🔗
Deprecated:UseNativeMenuorPopupMenuinstead.
Sets the callback of the item at indexidx. Callback is emitted when its accelerator is activated.
Note:Thekey_callbackCallable needs to accept exactly one Variant parameter, the parameter passed to the Callable will be the value passed to thetagparameter when the menu item was created.
Note:This method is implemented only on macOS.
voidglobal_menu_set_item_max_states(menu_root:String, idx:int, max_states:int)🔗
Deprecated:UseNativeMenuorPopupMenuinstead.
Sets number of state of a multistate item. Seeglobal_menu_add_multistate_item()for details.
Note:This method is implemented only on macOS.
voidglobal_menu_set_item_radio_checkable(menu_root:String, idx:int, checkable:bool)🔗
Deprecated:UseNativeMenuorPopupMenuinstead.
Sets the type of the item at the specified indexidxto radio button. Iffalse, sets the type of the item to plain text.
Note:This is purely cosmetic; you must add the logic for checking/unchecking items in radio groups.
Note:This method is implemented only on macOS.
voidglobal_menu_set_item_state(menu_root:String, idx:int, state:int)🔗
Deprecated:UseNativeMenuorPopupMenuinstead.
Sets the state of a multistate item. Seeglobal_menu_add_multistate_item()for details.
Note:This method is implemented only on macOS.
voidglobal_menu_set_item_submenu(menu_root:String, idx:int, submenu:String)🔗
Deprecated:UseNativeMenuorPopupMenuinstead.
Sets the submenu of the item at indexidx. The submenu is the ID of a global menu root that would be shown when the item is clicked.
Note:This method is implemented only on macOS.
voidglobal_menu_set_item_tag(menu_root:String, idx:int, tag:Variant)🔗
Deprecated:UseNativeMenuorPopupMenuinstead.
Sets the metadata of an item, which may be of any type. You can later get it withglobal_menu_get_item_tag(), which provides a simple way of assigning context data to items.
Note:This method is implemented only on macOS.
voidglobal_menu_set_item_text(menu_root:String, idx:int, text:String)🔗
Deprecated:UseNativeMenuorPopupMenuinstead.
Sets the text of the item at indexidx.
Note:This method is implemented only on macOS.
voidglobal_menu_set_item_tooltip(menu_root:String, idx:int, tooltip:String)🔗
Deprecated:UseNativeMenuorPopupMenuinstead.
Sets theStringtooltip of the item at the specified indexidx.
Note:This method is implemented only on macOS.
voidglobal_menu_set_popup_callbacks(menu_root:String, open_callback:Callable, close_callback:Callable)🔗
Deprecated:UseNativeMenuorPopupMenuinstead.
Registers callables to emit when the menu is respectively about to show or closed. Callback methods should have zero arguments.
boolhas_additional_outputs()const🔗
Returnstrueif any additional outputs have been registered viaregister_additional_output().
boolhas_feature(feature:Feature)const🔗
Returnstrueif the specifiedfeatureis supported by the currentDisplayServer,falseotherwise.
boolhas_hardware_keyboard()const🔗
Returnstrueif a hardware keyboard is connected.
Note:This method is implemented on Android and iOS. On other platforms, this method always returnstrue.
voidhelp_set_search_callbacks(search_callback:Callable, action_callback:Callable)🔗
Sets native help system search callbacks.
search_callbackhas the following arguments:Stringsearch_string,intresult_limitand return aDictionarywith "key, display name" pairs for the search results. Called when the user enters search terms in theHelpmenu.
action_callbackhas the following arguments:Stringkey. Called when the user selects a search result in theHelpmenu.
Note:This method is implemented only on macOS.
Vector2iime_get_selection()const🔗
Returns the text selection in theInput Method Editorcomposition string, with theVector2i'sxcomponent being the caret position andybeing the length of the selection.
Note:This method is implemented only on macOS.
Stringime_get_text()const🔗
Returns the composition string contained within theInput Method Editorwindow.
Note:This method is implemented only on macOS.
boolis_dark_mode()const🔗
Returnstrueif OS is using dark mode.
Note:This method is implemented on Android, iOS, macOS, Windows, and Linux (X11/Wayland).
boolis_dark_mode_supported()const🔗
Returnstrueif OS supports dark mode.
Note:This method is implemented on Android, iOS, macOS, Windows, and Linux (X11/Wayland).
boolis_touchscreen_available()const🔗
Returnstrueif touch events are available (Android or iOS), the capability is detected on the Web platform or ifProjectSettings.input_devices/pointing/emulate_touch_from_mouseistrue.
boolis_window_transparency_available()const🔗
Returnstrueif the window background can be made transparent. This method returnsfalseifProjectSettings.display/window/per_pixel_transparency/allowedis set tofalse, or if transparency is not supported by the renderer or OS compositor.
intkeyboard_get_current_layout()const🔗
Returns active keyboard layout index.
Note:This method is implemented on Linux (X11/Wayland), macOS, and Windows.
Keykeyboard_get_keycode_from_physical(keycode:Key)const🔗
Converts a physical (US QWERTY)keycodeto one in the active keyboard layout.
Note:This method is implemented on Linux (X11/Wayland), macOS and Windows.
Keykeyboard_get_label_from_physical(keycode:Key)const🔗
Converts a physical (US QWERTY)keycodeto localized label printed on the key in the active keyboard layout.
Note:This method is implemented on Linux (X11/Wayland), macOS and Windows.
intkeyboard_get_layout_count()const🔗
Returns the number of keyboard layouts.
Note:This method is implemented on Linux (X11/Wayland), macOS and Windows.
Stringkeyboard_get_layout_language(index:int)const🔗
Returns the ISO-639/BCP-47 language code of the keyboard layout at positionindex.
Note:This method is implemented on Linux (X11/Wayland), macOS and Windows.
Stringkeyboard_get_layout_name(index:int)const🔗
Returns the localized name of the keyboard layout at positionindex.
Note:This method is implemented on Linux (X11/Wayland), macOS and Windows.
voidkeyboard_set_current_layout(index:int)🔗
Sets the active keyboard layout.
Note:This method is implemented on Linux (X11/Wayland), macOS and Windows.
BitField[MouseButtonMask]mouse_get_button_state()const🔗
Returns the current state of mouse buttons (whether each button is pressed) as a bitmask. If multiple mouse buttons are pressed at the same time, the bits are added together. Equivalent toInput.get_mouse_button_mask().
MouseModemouse_get_mode()const🔗
Returns the current mouse mode. See alsomouse_set_mode().
Vector2imouse_get_position()const🔗
Returns the mouse cursor's current position in screen coordinates.
voidmouse_set_mode(mouse_mode:MouseMode)🔗
Sets the current mouse mode. See alsomouse_get_mode().
voidprocess_events()🔗
Perform window manager processing, including input flushing. See alsoforce_process_and_drop_events(),Input.flush_buffered_events()andInput.use_accumulated_input.
voidregister_additional_output(object:Object)🔗
Registers anObjectwhich represents an additional output that will be rendered too, beyond normal windows. TheObjectis only used as an identifier, which can be later passed tounregister_additional_output().
This can be used to prevent Godot from skipping rendering when no normal windows are visible.
intscreen_get_dpi(screen:int= -1)const🔗
Returns the dots per inch density of the specified screen. Returns platform specific default value ifscreenis invalid.
Note:One of the following constants can be used asscreen:SCREEN_OF_MAIN_WINDOW,SCREEN_PRIMARY,SCREEN_WITH_MOUSE_FOCUS, orSCREEN_WITH_KEYBOARD_FOCUS.
Note:On macOS, returned value is inaccurate if fractional display scaling mode is used.
Note:On Android devices, the actual screen densities are grouped into six generalized densities:

```
   ldpi - 120 dpi
   mdpi - 160 dpi
   hdpi - 240 dpi
  xhdpi - 320 dpi
 xxhdpi - 480 dpi
xxxhdpi - 640 dpi
```

Note:This method is implemented on Android, iOS, Linux (X11/Wayland), macOS, Web, and Windows. On other platforms, this method always returns72.
Imagescreen_get_image(screen:int= -1)const🔗
Returns a screenshot of thescreen. Returnsnullifscreenis invalid or theDisplayServerfails to capture screenshot.
Note:One of the following constants can be used asscreen:SCREEN_OF_MAIN_WINDOW,SCREEN_PRIMARY,SCREEN_WITH_MOUSE_FOCUS, orSCREEN_WITH_KEYBOARD_FOCUS.
Note:This method is implemented on Linux (X11, excluding XWayland), macOS, and Windows. On other platforms, this method always returnsnull.
Note:On macOS, this method requires the "Screen Recording" permission. If permission is not granted, this method returns a screenshot that will not include other application windows or OS elements not related to the application.
Imagescreen_get_image_rect(rect:Rect2i)const🔗
Returns a screenshot of the screen region defined byrect. Returnsnullifrectis outside screen bounds or theDisplayServerfails to capture screenshot.
Note:This method is implemented on macOS and Windows. On other platforms, this method always returnsnull.
Note:On macOS, this method requires the "Screen Recording" permission. If permission is not granted, this method returns a screenshot that will not include other application windows or OS elements not related to the application.
floatscreen_get_max_scale()const🔗
Returns the greatest scale factor of all screens.
Note:On macOS returned value is2.0if there is at least one hiDPI (Retina) screen in the system, and1.0in all other cases.
Note:This method is implemented only on macOS.
ScreenOrientationscreen_get_orientation(screen:int= -1)const🔗
Returns thescreen's current orientation. See alsoscreen_set_orientation(). ReturnsSCREEN_LANDSCAPEifscreenis invalid.
Note:One of the following constants can be used asscreen:SCREEN_OF_MAIN_WINDOW,SCREEN_PRIMARY,SCREEN_WITH_MOUSE_FOCUS, orSCREEN_WITH_KEYBOARD_FOCUS.
Note:This method is implemented on Android and iOS. On other platforms, this method always returnsSCREEN_LANDSCAPE.
Colorscreen_get_pixel(position:Vector2i)const🔗
Returns the color of the pixel at the given screenposition. On multi-monitor setups, the screen position is relative to the virtual desktop area.
Note:This method is implemented on Linux (X11, excluding XWayland), macOS, and Windows. On other platforms, this method always returnsColor(0,0,0,1).
Note:On macOS, this method requires the "Screen Recording" permission. If permission is not granted, this method returns a color from a screenshot that will not include other application windows or OS elements not related to the application.
Vector2iscreen_get_position(screen:int= -1)const🔗
Returns the screen's top-left corner position in pixels. ReturnsVector2i.ZEROifscreenis invalid. On multi-monitor setups, the screen position is relative to the virtual desktop area. On multi-monitor setups with different screen resolutions or orientations, the origin might be located outside any display like this:

```
* (0, 0)        +-------+
                |       |
+-------------+ |       |
|             | |       |
|             | |       |
+-------------+ +-------+
```

See alsoscreen_get_size().
Note:One of the following constants can be used asscreen:SCREEN_OF_MAIN_WINDOW,SCREEN_PRIMARY,SCREEN_WITH_MOUSE_FOCUS, orSCREEN_WITH_KEYBOARD_FOCUS.
floatscreen_get_refresh_rate(screen:int= -1)const🔗
Returns the current refresh rate of the specified screen. When V-Sync is enabled, this returns the maximum framerate the project can effectively reach. Returns-1.0ifscreenis invalid or theDisplayServerfails to find the refresh rate for the specified screen.
To fallback to a default refresh rate if the method fails, try:

```
var refresh_rate = DisplayServer.screen_get_refresh_rate()
if refresh_rate < 0:
    refresh_rate = 60.0
```

Note:One of the following constants can be used asscreen:SCREEN_OF_MAIN_WINDOW,SCREEN_PRIMARY,SCREEN_WITH_MOUSE_FOCUS, orSCREEN_WITH_KEYBOARD_FOCUS.
Note:This method is implemented on Android, iOS, macOS, Linux (X11 and Wayland), and Windows. On other platforms, this method always returns-1.0.
floatscreen_get_scale(screen:int= -1)const🔗
Returns the scale factor of the specified screen by index. Returns1.0ifscreenis invalid.
Note:One of the following constants can be used asscreen:SCREEN_OF_MAIN_WINDOW,SCREEN_PRIMARY,SCREEN_WITH_MOUSE_FOCUS, orSCREEN_WITH_KEYBOARD_FOCUS.
Note:On macOS, the returned value is2.0for hiDPI (Retina) screens, and1.0for all other cases.
Note:On Linux (Wayland), the returned value is accurate only whenscreenisSCREEN_OF_MAIN_WINDOW. Due to API limitations, passing a direct index will return a rounded-up integer, if the screen has a fractional scale (e.g.1.25would get rounded up to2.0).
Note:This method is implemented on Android, iOS, Web, macOS, and Linux (Wayland). On other platforms, this method always returns1.0.
Vector2iscreen_get_size(screen:int= -1)const🔗
Returns the screen's size in pixels. See alsoscreen_get_position()andscreen_get_usable_rect(). ReturnsVector2i.ZEROifscreenis invalid.
Note:One of the following constants can be used asscreen:SCREEN_OF_MAIN_WINDOW,SCREEN_PRIMARY,SCREEN_WITH_MOUSE_FOCUS, orSCREEN_WITH_KEYBOARD_FOCUS.
Rect2iscreen_get_usable_rect(screen:int= -1)const🔗
Returns the portion of the screen that is not obstructed by a status bar in pixels. See alsoscreen_get_size().
Note:One of the following constants can be used asscreen:SCREEN_OF_MAIN_WINDOW,SCREEN_PRIMARY,SCREEN_WITH_MOUSE_FOCUS, orSCREEN_WITH_KEYBOARD_FOCUS.
Note:This method is implemented on Linux/X11, macOS, and Windows. On other platforms, this method always returnsRect2i(screen_get_position(screen),screen_get_size(screen)).
boolscreen_is_kept_on()const🔗
Returnstrueif the screen should never be turned off by the operating system's power-saving measures. See alsoscreen_set_keep_on().
voidscreen_set_keep_on(enable:bool)🔗
Sets whether the screen should never be turned off by the operating system's power-saving measures. See alsoscreen_is_kept_on().
voidscreen_set_orientation(orientation:ScreenOrientation, screen:int= -1)🔗
Sets thescreen'sorientation. See alsoscreen_get_orientation().
Note:One of the following constants can be used asscreen:SCREEN_OF_MAIN_WINDOW,SCREEN_PRIMARY,SCREEN_WITH_MOUSE_FOCUS, orSCREEN_WITH_KEYBOARD_FOCUS.
Note:This method is implemented on Android and iOS.
Note:On iOS, this method has no effect ifProjectSettings.display/window/handheld/orientationis not set toSCREEN_SENSOR.
voidset_hardware_keyboard_connection_change_callback(callable:Callable)🔗
Sets the callback that should be called when a hardware keyboard is connected or disconnected.callableshould accept a singleboolargument indicating whether the keyboard has been connected (true) or disconnected (false).
Note:This method is only implemented on Android.
voidset_icon(image:Image)🔗
Sets the window icon (usually displayed in the top-left corner) with anImage. To use icons in the operating system's native format, useset_native_icon()instead.
Note:Requires support forFEATURE_ICON.
voidset_native_icon(filename:String)🔗
Sets the window icon (usually displayed in the top-left corner) in the operating system'snativeformat. The file atfilenamemust be in.icoformat on Windows or.icnson macOS. By using specially crafted.icoor.icnsicons,set_native_icon()allows specifying different icons depending on the size the icon is displayed at. This size is determined by the operating system and user preferences (including the display scale factor). To use icons in other formats, useset_icon()instead.
Note:Requires support forFEATURE_NATIVE_ICON.
voidset_system_theme_change_callback(callable:Callable)🔗
Sets the callback that should be called when the system's theme settings are changed.callableshould accept zero arguments.
Note:This method is implemented on Android, iOS, macOS, Windows, and Linux (X11/Wayland).
voidshow_emoji_and_symbol_picker()const🔗
Opens system emoji and symbol picker.
Note:This method is implemented on macOS and Windows.
Rect2status_indicator_get_rect(id:int)const🔗
Returns the rectangle for the given status indicatoridin screen coordinates. If the status indicator is not visible, returns an emptyRect2.
Note:This method is implemented on macOS and Windows.
voidstatus_indicator_set_callback(id:int, callback:Callable)🔗
Sets the application status indicator activation callback.callbackshould take two arguments:intmouse button index (one ofMouseButtonvalues) andVector2iclick position in screen coordinates.
Note:This method is implemented on macOS and Windows.
voidstatus_indicator_set_icon(id:int, icon:Texture2D)🔗
Sets the application status indicator icon.
Note:This method is implemented on macOS and Windows.
voidstatus_indicator_set_menu(id:int, menu_rid:RID)🔗
Sets the application status indicator native popup menu.
Note:On macOS, the menu is activated by any mouse button. Its activation callback isnottriggered.
Note:On Windows, the menu is activated by the right mouse button, selecting the status icon and pressingShift+F10, or the applications key. The menu's activation callback for the other mouse buttons is still triggered.
Note:Native popup is only supported ifNativeMenusupports theNativeMenu.FEATURE_POPUP_MENUfeature.
voidstatus_indicator_set_tooltip(id:int, tooltip:String)🔗
Sets the application status indicator tooltip.
Note:This method is implemented on macOS and Windows.
Stringtablet_get_current_driver()const🔗
Returns current active tablet driver name.
Note:This method is implemented only on Windows.
inttablet_get_driver_count()const🔗
Returns the total number of available tablet drivers.
Note:This method is implemented only on Windows.
Stringtablet_get_driver_name(idx:int)const🔗
Returns the tablet driver name for the given index.
Note:This method is implemented only on Windows.
voidtablet_set_current_driver(name:String)🔗
Set active tablet driver name.
Supported drivers:

- winink: Windows Ink API, default.
winink: Windows Ink API, default.
- wintab: Wacom Wintab API (compatible device driver required).
wintab: Wacom Wintab API (compatible device driver required).
- dummy: Dummy driver, tablet input is disabled.
dummy: Dummy driver, tablet input is disabled.
Note:This method is implemented only on Windows.
Array[Dictionary]tts_get_voices()const🔗
Returns anArrayof voice information dictionaries.
EachDictionarycontains twoStringentries:
- nameis voice name.
nameis voice name.
- idis voice identifier.
idis voice identifier.
- languageis language code inlang_Variantformat. Thelangpart is a 2 or 3-letter code based on the ISO-639 standard, in lowercase. TheVariantpart is an engine-dependent string describing country, region or/and dialect.
languageis language code inlang_Variantformat. Thelangpart is a 2 or 3-letter code based on the ISO-639 standard, in lowercase. TheVariantpart is an engine-dependent string describing country, region or/and dialect.
Note that Godot depends on system libraries for text-to-speech functionality. These libraries are installed by default on Windows and macOS, but not on all Linux distributions. If they are not present, this method will return an empty list. This applies to both Godot users on Linux, as well as end-users on Linux running Godot games that use text-to-speech.
Note:This method is implemented on Android, iOS, Web, Linux (X11/Wayland), macOS, and Windows.
PackedStringArraytts_get_voices_for_language(language:String)const🔗
Returns aPackedStringArrayof voice identifiers for thelanguage.
Note:This method is implemented on Android, iOS, Web, Linux (X11/Wayland), macOS, and Windows.
booltts_is_paused()const🔗
Returnstrueif the synthesizer is in a paused state.
Note:This method is implemented on Android, iOS, Web, Linux (X11/Wayland), macOS, and Windows.
booltts_is_speaking()const🔗
Returnstrueif the synthesizer is generating speech, or have utterance waiting in the queue.
Note:This method is implemented on Android, iOS, Web, Linux (X11/Wayland), macOS, and Windows.
voidtts_pause()🔗
Puts the synthesizer into a paused state.
Note:This method is implemented on Android, iOS, Web, Linux (X11/Wayland), macOS, and Windows.
voidtts_resume()🔗
Resumes the synthesizer if it was paused.
Note:This method is implemented on Android, iOS, Web, Linux (X11/Wayland), macOS, and Windows.
voidtts_set_utterance_callback(event:TTSUtteranceEvent, callable:Callable)🔗
Adds a callback, which is called when the utterance has started, finished, canceled or reached a text boundary.
- TTS_UTTERANCE_STARTED,TTS_UTTERANCE_ENDED, andTTS_UTTERANCE_CANCELEDcallable's method should take oneintparameter, the utterance ID.
TTS_UTTERANCE_STARTED,TTS_UTTERANCE_ENDED, andTTS_UTTERANCE_CANCELEDcallable's method should take oneintparameter, the utterance ID.
- TTS_UTTERANCE_BOUNDARYcallable's method should take twointparameters, the index of the character and the utterance ID.
TTS_UTTERANCE_BOUNDARYcallable's method should take twointparameters, the index of the character and the utterance ID.
Note:The granularity of the boundary callbacks is engine dependent.
Note:This method is implemented on Android, iOS, Web, Linux (X11/Wayland), macOS, and Windows.
voidtts_speak(text:String, voice:String, volume:int= 50, pitch:float= 1.0, rate:float= 1.0, utterance_id:int= 0, interrupt:bool= false)🔗
Adds an utterance to the queue. Ifinterruptistrue, the queue is cleared first.
- voiceidentifier is one of the"id"values returned bytts_get_voices()or one of the values returned bytts_get_voices_for_language().
voiceidentifier is one of the"id"values returned bytts_get_voices()or one of the values returned bytts_get_voices_for_language().
- volumeranges from0(lowest) to100(highest).
volumeranges from0(lowest) to100(highest).
- pitchranges from0.0(lowest) to2.0(highest),1.0is default pitch for the current voice.
pitchranges from0.0(lowest) to2.0(highest),1.0is default pitch for the current voice.
- rateranges from0.1(lowest) to10.0(highest),1.0is a normal speaking rate. Other values act as a percentage relative.
rateranges from0.1(lowest) to10.0(highest),1.0is a normal speaking rate. Other values act as a percentage relative.
- utterance_idis passed as a parameter to the callback functions.
utterance_idis passed as a parameter to the callback functions.
Note:On Windows and Linux (X11/Wayland), utterancetextcan use SSML markup. SSML support is engine and voice dependent. If the engine does not support SSML, you should strip out all XML markup before callingtts_speak().
Note:The granularity of pitch, rate, and volume is engine and voice dependent. Values may be truncated.
Note:This method is implemented on Android, iOS, Web, Linux (X11/Wayland), macOS, and Windows.
voidtts_stop()🔗
Stops synthesis in progress and removes all utterances from the queue.
Note:This method is implemented on Android, iOS, Web, Linux (X11/Wayland), macOS, and Windows.
voidunregister_additional_output(object:Object)🔗
Unregisters anObjectrepresenting an additional output, that was registered viaregister_additional_output().
intvirtual_keyboard_get_height()const🔗
Returns the on-screen keyboard's height in pixels. Returns0if there is no keyboard or if it is currently hidden.
Note:On Android 7 and 8, the keyboard height may return0the first time the keyboard is opened in non-immersive mode. This behavior does not occur in immersive mode.
voidvirtual_keyboard_hide()🔗
Hides the virtual keyboard if it is shown, does nothing otherwise.
voidvirtual_keyboard_show(existing_text:String, position:Rect2= Rect2(0, 0, 0, 0), type:VirtualKeyboardType= 0, max_length:int= -1, cursor_start:int= -1, cursor_end:int= -1)🔗
Shows the virtual keyboard if the platform has one.
existing_textparameter is useful for implementing your ownLineEditorTextEdit, as it tells the virtual keyboard what text has already been typed (the virtual keyboard uses it for auto-correct and predictions).
positionparameter is the screen spaceRect2of the edited text.
typeparameter allows configuring which type of virtual keyboard to show.
max_lengthlimits the number of characters that can be entered if different from-1.
cursor_startcan optionally define the current text cursor position ifcursor_endis not set.
cursor_startandcursor_endcan optionally define the current text selection.
Note:This method is implemented on Android, iOS and Web.
voidwarp_mouse(position:Vector2i)🔗
Sets the mouse cursor position to the givenpositionrelative to an origin at the upper left corner of the currently focused game Window Manager window.
Note:warp_mouse()is only supported on Windows, macOS, and Linux (X11/Wayland). It has no effect on Android, iOS, and Web.
boolwindow_can_draw(window_id:int= 0)const🔗
Returnstrueif anything can be drawn in the window specified bywindow_id,falseotherwise. Using the--disable-render-loopcommand line argument or a headless build will returnfalse.
intwindow_get_active_popup()const🔗
Returns ID of the active popup window, orINVALID_WINDOW_IDif there is none.
intwindow_get_attached_instance_id(window_id:int= 0)const🔗
Returns theObject.get_instance_id()of theWindowthewindow_idis attached to.
intwindow_get_current_screen(window_id:int= 0)const🔗
Returns the screen the window specified bywindow_idis currently positioned on. If the screen overlaps multiple displays, the screen where the window's center is located is returned. See alsowindow_set_current_screen(). ReturnsINVALID_SCREENifwindow_idis invalid.
Note:This method is implemented on Linux/X11, macOS, and Windows. On other platforms, this method always returns0.
boolwindow_get_flag(flag:WindowFlags, window_id:int= 0)const🔗
Returns the current value of the given window'sflag.
Vector2iwindow_get_max_size(window_id:int= 0)const🔗
Returns the window's maximum size (in pixels). See alsowindow_set_max_size().
Vector2iwindow_get_min_size(window_id:int= 0)const🔗
Returns the window's minimum size (in pixels). See alsowindow_set_min_size().
WindowModewindow_get_mode(window_id:int= 0)const🔗
Returns the mode of the given window.
intwindow_get_native_handle(handle_type:HandleType, window_id:int= 0)const🔗
Returns internal structure pointers for use in plugins.
Note:This method is implemented on Android, Linux (X11/Wayland), macOS, and Windows.
Rect2iwindow_get_popup_safe_rect(window:int)const🔗
Returns the bounding box of control, or menu item that was used to open the popup window, in the screen coordinate system.
Vector2iwindow_get_position(window_id:int= 0)const🔗
Returns the position of the client area of the given window on the screen.
Vector2iwindow_get_position_with_decorations(window_id:int= 0)const🔗
Returns the position of the given window on the screen including the borders drawn by the operating system. See alsowindow_get_position().
Vector3iwindow_get_safe_title_margins(window_id:int= 0)const🔗
Returns left margins (x), right margins (y) and height (z) of the title that are safe to use (contains no buttons or other elements) whenWINDOW_FLAG_EXTEND_TO_TITLEflag is set.
Vector2iwindow_get_size(window_id:int= 0)const🔗
Returns the size of the window specified bywindow_id(in pixels), excluding the borders drawn by the operating system. This is also called the "client area". See alsowindow_get_size_with_decorations(),window_set_size()andwindow_get_position().
Vector2iwindow_get_size_with_decorations(window_id:int= 0)const🔗
Returns the size of the window specified bywindow_id(in pixels), including the borders drawn by the operating system. See alsowindow_get_size().
Vector2iwindow_get_title_size(title:String, window_id:int= 0)const🔗
Returns the estimated window title bar size (including text and window buttons) for the window specified bywindow_id(in pixels). This method does not change the window title.
Note:This method is implemented on macOS and Windows.
VSyncModewindow_get_vsync_mode(window_id:int= 0)const🔗
Returns the V-Sync mode of the given window.
boolwindow_is_focused(window_id:int= 0)const🔗
Returnstrueif the window specified bywindow_idis focused.
boolwindow_is_maximize_allowed(window_id:int= 0)const🔗
Returnstrueif the given window can be maximized (the maximize button is enabled).
boolwindow_maximize_on_title_dbl_click()const🔗
Returnstrueif double-clicking on a window's title should maximize it.
Note:This method is implemented only on macOS.
boolwindow_minimize_on_title_dbl_click()const🔗
Returnstrueif double-clicking on a window's title should minimize it.
Note:This method is implemented only on macOS.
voidwindow_move_to_foreground(window_id:int= 0)🔗
Moves the window specified bywindow_idto the foreground, so that it is visible over other windows.
voidwindow_request_attention(window_id:int= 0)🔗
Makes the window specified bywindow_idrequest attention, which is materialized by the window title and taskbar entry blinking until the window is focused. This usually has no visible effect if the window is currently focused. The exact behavior varies depending on the operating system.
voidwindow_set_color(color:Color)🔗
Sets the background color of the root window.
Note:This method is implemented only on Android.
voidwindow_set_current_screen(screen:int, window_id:int= 0)🔗
Moves the window specified bywindow_idto the specifiedscreen. See alsowindow_get_current_screen().
Note:One of the following constants can be used asscreen:SCREEN_OF_MAIN_WINDOW,SCREEN_PRIMARY,SCREEN_WITH_MOUSE_FOCUS, orSCREEN_WITH_KEYBOARD_FOCUS.
Note:This method is implemented on Linux/X11, macOS, and Windows.
voidwindow_set_drop_files_callback(callback:Callable, window_id:int= 0)🔗
Sets thecallbackthat should be called when files are dropped from the operating system's file manager to the window specified bywindow_id.callbackshould take onePackedStringArrayargument, which is the list of dropped files.
Warning:Advanced users only! Adding such a callback to aWindownode will override its default implementation, which can introduce bugs.
Note:This method is implemented on Windows, macOS, Linux (X11/Wayland), and Web.
voidwindow_set_exclusive(window_id:int, exclusive:bool)🔗
If set totrue, this window will always stay on top of its parent window, parent window will ignore input while this window is opened.
Note:On macOS, exclusive windows are confined to the same space (virtual desktop or screen) as the parent window.
Note:This method is implemented on macOS and Windows.
voidwindow_set_flag(flag:WindowFlags, enabled:bool, window_id:int= 0)🔗
Enables or disables the given window's givenflag.
voidwindow_set_ime_active(active:bool, window_id:int= 0)🔗
Sets whetherInput Method Editorshould be enabled for the window specified bywindow_id. See alsowindow_set_ime_position().
voidwindow_set_ime_position(position:Vector2i, window_id:int= 0)🔗
Sets the position of theInput Method Editorpopup for the specifiedwindow_id. Only effective ifwindow_set_ime_active()was set totruefor the specifiedwindow_id.
voidwindow_set_input_event_callback(callback:Callable, window_id:int= 0)🔗
Sets thecallbackthat should be called when anyInputEventis sent to the window specified bywindow_id.
Warning:Advanced users only! Adding such a callback to aWindownode will override its default implementation, which can introduce bugs.
voidwindow_set_input_text_callback(callback:Callable, window_id:int= 0)🔗
Sets thecallbackthat should be called when text is entered using the virtual keyboard to the window specified bywindow_id.
Warning:Advanced users only! Adding such a callback to aWindownode will override its default implementation, which can introduce bugs.
voidwindow_set_max_size(max_size:Vector2i, window_id:int= 0)🔗
Sets the maximum size of the window specified bywindow_idin pixels. Normally, the user will not be able to drag the window to make it larger than the specified size. See alsowindow_get_max_size().
Note:It's recommended to change this value usingWindow.max_sizeinstead.
Note:Using third-party tools, it is possible for users to disable window geometry restrictions and therefore bypass this limit.
voidwindow_set_min_size(min_size:Vector2i, window_id:int= 0)🔗
Sets the minimum size for the given window tomin_sizein pixels. Normally, the user will not be able to drag the window to make it smaller than the specified size. See alsowindow_get_min_size().
Note:It's recommended to change this value usingWindow.min_sizeinstead.
Note:By default, the main window has a minimum size ofVector2i(64,64). This prevents issues that can arise when the window is resized to a near-zero size.
Note:Using third-party tools, it is possible for users to disable window geometry restrictions and therefore bypass this limit.
voidwindow_set_mode(mode:WindowMode, window_id:int= 0)🔗
Sets window mode for the given window tomode.
Note:On Android, setting it toWINDOW_MODE_FULLSCREENorWINDOW_MODE_EXCLUSIVE_FULLSCREENwill enable immersive mode.
Note:Setting the window to full screen forcibly sets the borderless flag totrue, so make sure to set it back tofalsewhen not wanted.
voidwindow_set_mouse_passthrough(region:PackedVector2Array, window_id:int= 0)🔗
Sets a polygonal region of the window which accepts mouse events. Mouse events outside the region will be passed through.
Passing an empty array will disable passthrough support (all mouse events will be intercepted by the window, which is the default behavior).

```
# Set region, using Path2D node.
DisplayServer.window_set_mouse_passthrough($Path2D.curve.get_baked_points())

# Set region, using Polygon2D node.
DisplayServer.window_set_mouse_passthrough($Polygon2D.polygon)

# Reset region to default.
DisplayServer.window_set_mouse_passthrough([])
```

```
// Set region, using Path2D node.
DisplayServer.WindowSetMousePassthrough(GetNode<Path2D>("Path2D").Curve.GetBakedPoints());

// Set region, using Polygon2D node.
DisplayServer.WindowSetMousePassthrough(GetNode<Polygon2D>("Polygon2D").Polygon);

// Reset region to default.
DisplayServer.WindowSetMousePassthrough([]);
```

Note:On Windows, the portion of a window that lies outside the region is not drawn, while on Linux (X11) and macOS it is.
Note:This method is implemented on Linux (X11), macOS and Windows.
voidwindow_set_popup_safe_rect(window:int, rect:Rect2i)🔗
Sets the bounding box of control, or menu item that was used to open the popup window, in the screen coordinate system. Clicking this area will not auto-close this popup.
voidwindow_set_position(position:Vector2i, window_id:int= 0)🔗
Sets the position of the given window toposition. On multi-monitor setups, the screen position is relative to the virtual desktop area. On multi-monitor setups with different screen resolutions or orientations, the origin may be located outside any display like this:

```
* (0, 0)        +-------+
                |       |
+-------------+ |       |
|             | |       |
|             | |       |
+-------------+ +-------+
```

See alsowindow_get_position()andwindow_set_size().
Note:It's recommended to change this value usingWindow.positioninstead.
Note:On Linux (Wayland): this method is a no-op.
voidwindow_set_rect_changed_callback(callback:Callable, window_id:int= 0)🔗
Sets thecallbackthat will be called when the window specified bywindow_idis moved or resized.
Warning:Advanced users only! Adding such a callback to aWindownode will override its default implementation, which can introduce bugs.
voidwindow_set_size(size:Vector2i, window_id:int= 0)🔗
Sets the size of the given window tosize(in pixels). See alsowindow_get_size()andwindow_get_position().
Note:It's recommended to change this value usingWindow.sizeinstead.
voidwindow_set_title(title:String, window_id:int= 0)🔗
Sets the title of the given window totitle.
Note:It's recommended to change this value usingWindow.titleinstead.
Note:Avoid changing the window title every frame, as this can cause performance issues on certain window managers. Try to change the window title only a few times per second at most.
voidwindow_set_transient(window_id:int, parent_window_id:int)🔗
Sets window transient parent. Transient window will be destroyed with its transient parent and will return focus to their parent when closed. The transient window is displayed on top of a non-exclusive full-screen parent window. Transient windows can't enter full-screen mode.
Note:It's recommended to change this value usingWindow.transientinstead.
Note:The behavior might be different depending on the platform.
voidwindow_set_vsync_mode(vsync_mode:VSyncMode, window_id:int= 0)🔗
Sets the V-Sync mode of the given window. See alsoProjectSettings.display/window/vsync/vsync_mode.
Depending on the platform and used renderer, the engine will fall back toVSYNC_ENABLEDif the desired mode is not supported.
Note:V-Sync modes other thanVSYNC_ENABLEDare only supported in the Forward+ and Mobile rendering methods, not Compatibility.
voidwindow_set_window_buttons_offset(offset:Vector2i, window_id:int= 0)🔗
WhenWINDOW_FLAG_EXTEND_TO_TITLEflag is set, set offset to the center of the first titlebar button.
Note:This flag is implemented only on macOS.
voidwindow_set_window_event_callback(callback:Callable, window_id:int= 0)🔗
Sets thecallbackthat will be called when an event occurs in the window specified bywindow_id.
Warning:Advanced users only! Adding such a callback to aWindownode will override its default implementation, which can introduce bugs.
voidwindow_start_drag(window_id:int= 0)🔗
Starts an interactive drag operation on the window with the givenwindow_id, using the current mouse position. Call this method when handling a mouse button being pressed to simulate a pressed event on the window's title bar. Using this method allows the window to participate in space switching, tiling, and other system features.
Note:This method is implemented on Linux (X11/Wayland), macOS, and Windows.
voidwindow_start_resize(edge:WindowResizeEdge, window_id:int= 0)🔗
Starts an interactive resize operation on the window with the givenwindow_id, using the current mouse position. Call this method when handling a mouse button being pressed to simulate a pressed event on the window's edge.
Note:This method is implemented on Linux (X11/Wayland), macOS, and Windows.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
