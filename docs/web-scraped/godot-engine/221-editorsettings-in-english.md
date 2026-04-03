# EditorSettings in English

# EditorSettings
Inherits:Resource<RefCounted<Object
Object that holds the project-independent editor settings.

## Description
Object that holds the project-independent editor settings. These settings are generally visible in theEditor > Editor Settingsmenu.
Property names use slash delimiters to distinguish sections. Setting values can be of anyVarianttype. It's recommended to usesnake_casefor editor settings to be consistent with the Godot editor itself.
Editor settings are saved automatically when changed.
Accessing the settings can be done using the following methods, such as:
```
var settings = EditorInterface.get_editor_settings()
# `settings.set("some/property", 10)` also works as this class overrides `_set()` internally.
settings.set_setting("some/property", 10)
# `settings.get("some/property")` also works as this class overrides `_get()` internally.
settings.get_setting("some/property")
var list_of_settings = settings.get_property_list()
```
```
EditorSettings settings = EditorInterface.Singleton.GetEditorSettings();
// `settings.set("some/property", value)` also works as this class overrides `_set()` internally.
settings.SetSetting("some/property", Value);
// `settings.get("some/property", value)` also works as this class overrides `_get()` internally.
settings.GetSetting("some/property");
Godot.Collections.Array<Godot.Collections.Dictionary> listOfSettings = settings.GetPropertyList();
```
Note:This class shouldn't be instantiated directly. Instead, access the singleton usingEditorInterface.get_editor_settings().

## Properties

| bool | asset_library/use_threads |
|---|---|
| bool | debugger/auto_switch_to_remote_scene_tree |
| bool | debugger/auto_switch_to_stack_trace |
| int | debugger/max_node_selection |
| bool | debugger/profile_native_calls |
| int | debugger/profiler_frame_history_size |
| int | debugger/profiler_frame_max_functions |
| int | debugger/profiler_target_fps |
| float | debugger/remote_inspect_refresh_interval |
| float | debugger/remote_scene_tree_refresh_interval |
| bool | docks/filesystem/always_show_folders |
| String | docks/filesystem/other_file_extensions |
| String | docks/filesystem/textfile_extensions |
| int | docks/filesystem/thumbnail_size |
| float | docks/property_editor/auto_refresh_interval |
| float | docks/property_editor/subresource_hue_tint |
| bool | docks/scene_tree/accessibility_warnings |
| bool | docks/scene_tree/ask_before_deleting_related_animation_tracks |
| bool | docks/scene_tree/ask_before_revoking_unique_name |
| bool | docks/scene_tree/auto_expand_to_selected |
| bool | docks/scene_tree/center_node_on_reparent |
| bool | docks/scene_tree/hide_filtered_out_parents |
| bool | docks/scene_tree/start_create_dialog_fully_expanded |
| float | editors/2d/auto_resample_delay |
| Color | editors/2d/bone_color1 |
| Color | editors/2d/bone_color2 |
| Color | editors/2d/bone_ik_color |
| Color | editors/2d/bone_outline_color |
| float | editors/2d/bone_outline_size |
| Color | editors/2d/bone_selected_color |
| float | editors/2d/bone_width |
| Color | editors/2d/grid_color |
| Color | editors/2d/guides_color |
| float | editors/2d/ruler_width |
| Color | editors/2d/smart_snapping_line_color |
| bool | editors/2d/use_integer_zoom_by_default |
| Color | editors/2d/viewport_border_color |
| float | editors/2d/zoom_speed_factor |
| Color | editors/3d/active_selection_box_color |
| float | editors/3d/default_fov |
| float | editors/3d/default_z_far |
| float | editors/3d/default_z_near |
| int | editors/3d/freelook/freelook_activation_modifier |
| float | editors/3d/freelook/freelook_base_speed |
| float | editors/3d/freelook/freelook_inertia |
| int | editors/3d/freelook/freelook_navigation_scheme |
| float | editors/3d/freelook/freelook_sensitivity |
| bool | editors/3d/freelook/freelook_speed_zoom_link |
| float | editors/3d/grid_division_level_bias |
| int | editors/3d/grid_division_level_max |
| int | editors/3d/grid_division_level_min |
| int | editors/3d/grid_size |
| bool | editors/3d/grid_xy_plane |
| bool | editors/3d/grid_xz_plane |
| bool | editors/3d/grid_yz_plane |
| float | editors/3d/manipulator_gizmo_opacity |
| int | editors/3d/manipulator_gizmo_size |
| bool | editors/3d/navigation/emulate_3_button_mouse |
| bool | editors/3d/navigation/emulate_numpad |
| bool | editors/3d/navigation/invert_x_axis |
| bool | editors/3d/navigation/invert_y_axis |
| int | editors/3d/navigation/navigation_scheme |
| int | editors/3d/navigation/orbit_mouse_button |
| int | editors/3d/navigation/pan_mouse_button |
| bool | editors/3d/navigation/show_viewport_navigation_gizmo |
| bool | editors/3d/navigation/show_viewport_rotation_gizmo |
| bool | editors/3d/navigation/warped_mouse_panning |
| int | editors/3d/navigation/zoom_mouse_button |
| int | editors/3d/navigation/zoom_style |
| float | editors/3d/navigation_feel/angle_snap_threshold |
| float | editors/3d/navigation_feel/orbit_inertia |
| float | editors/3d/navigation_feel/orbit_sensitivity |
| float | editors/3d/navigation_feel/translation_inertia |
| float | editors/3d/navigation_feel/translation_sensitivity |
| float | editors/3d/navigation_feel/zoom_inertia |
| Color | editors/3d/primary_grid_color |
| int | editors/3d/primary_grid_steps |
| Color | editors/3d/secondary_grid_color |
| Color | editors/3d/selection_box_color |
| int | editors/3d/show_gizmo_during_rotation |
| Color | editors/3d_gizmos/gizmo_colors/aabb |
| Color | editors/3d_gizmos/gizmo_colors/camera |
| Color | editors/3d_gizmos/gizmo_colors/csg |
| Color | editors/3d_gizmos/gizmo_colors/decal |
| Color | editors/3d_gizmos/gizmo_colors/fog_volume |
| Color | editors/3d_gizmos/gizmo_colors/gridmap_grid |
| Color | editors/3d_gizmos/gizmo_colors/ik_chain |
| Color | editors/3d_gizmos/gizmo_colors/instantiated |
| Color | editors/3d_gizmos/gizmo_colors/joint |
| Color | editors/3d_gizmos/gizmo_colors/joint_body_a |
| Color | editors/3d_gizmos/gizmo_colors/joint_body_b |
| Color | editors/3d_gizmos/gizmo_colors/lightmap_lines |
| Color | editors/3d_gizmos/gizmo_colors/lightprobe_lines |
| Color | editors/3d_gizmos/gizmo_colors/occluder |
| Color | editors/3d_gizmos/gizmo_colors/particle_attractor |
| Color | editors/3d_gizmos/gizmo_colors/particle_collision |
| Color | editors/3d_gizmos/gizmo_colors/particles |
| Color | editors/3d_gizmos/gizmo_colors/path_tilt |
| Color | editors/3d_gizmos/gizmo_colors/reflection_probe |
| Color | editors/3d_gizmos/gizmo_colors/selected_bone |
| Color | editors/3d_gizmos/gizmo_colors/skeleton |
| Color | editors/3d_gizmos/gizmo_colors/spring_bone_collision |
| Color | editors/3d_gizmos/gizmo_colors/spring_bone_inside_collision |
| Color | editors/3d_gizmos/gizmo_colors/spring_bone_joint |
| Color | editors/3d_gizmos/gizmo_colors/stream_player_3d |
| Color | editors/3d_gizmos/gizmo_colors/visibility_notifier |
| Color | editors/3d_gizmos/gizmo_colors/voxel_gi |
| float | editors/3d_gizmos/gizmo_settings/bone_axis_length |
| int | editors/3d_gizmos/gizmo_settings/bone_shape |
| float | editors/3d_gizmos/gizmo_settings/lightmap_gi_probe_size |
| float | editors/3d_gizmos/gizmo_settings/path3d_tilt_disk_size |
| bool | editors/animation/autorename_animation_tracks |
| bool | editors/animation/confirm_insert_track |
| float | editors/animation/default_animation_step |
| bool | editors/animation/default_create_bezier_tracks |
| bool | editors/animation/default_create_reset_tracks |
| bool | editors/animation/default_fps_compatibility |
| int | editors/animation/default_fps_mode |
| bool | editors/animation/insert_at_current_time |
| Color | editors/animation/onion_layers_future_color |
| Color | editors/animation/onion_layers_past_color |
| Color | editors/bone_mapper/handle_colors/error |
| Color | editors/bone_mapper/handle_colors/missing |
| Color | editors/bone_mapper/handle_colors/set |
| Color | editors/bone_mapper/handle_colors/unset |
| float | editors/grid_map/pick_distance |
| int | editors/grid_map/preview_size |
| int | editors/panning/2d_editor_pan_speed |
| int | editors/panning/2d_editor_panning_scheme |
| int | editors/panning/animation_editors_panning_scheme |
| bool | editors/panning/simple_panning |
| int | editors/panning/sub_editors_panning_scheme |
| bool | editors/panning/warped_mouse_panning |
| int | editors/panning/zoom_style |
| float | editors/polygon_editor/auto_bake_delay |
| int | editors/polygon_editor/point_grab_radius |
| bool | editors/polygon_editor/show_previous_outline |
| bool | editors/shader_editor/behavior/files/restore_shaders_on_load |
| bool | editors/tiles_editor/display_grid |
| Color | editors/tiles_editor/grid_color |
| bool | editors/tiles_editor/highlight_selected_layer |
| Color | editors/visual_editors/category_colors/color_color |
| Color | editors/visual_editors/category_colors/conditional_color |
| Color | editors/visual_editors/category_colors/input_color |
| Color | editors/visual_editors/category_colors/output_color |
| Color | editors/visual_editors/category_colors/particle_color |
| Color | editors/visual_editors/category_colors/scalar_color |
| Color | editors/visual_editors/category_colors/special_color |
| Color | editors/visual_editors/category_colors/textures_color |
| Color | editors/visual_editors/category_colors/transform_color |
| Color | editors/visual_editors/category_colors/utility_color |
| Color | editors/visual_editors/category_colors/vector_color |
| String | editors/visual_editors/color_theme |
| Color | editors/visual_editors/connection_colors/boolean_color |
| Color | editors/visual_editors/connection_colors/sampler_color |
| Color | editors/visual_editors/connection_colors/scalar_color |
| Color | editors/visual_editors/connection_colors/transform_color |
| Color | editors/visual_editors/connection_colors/vector2_color |
| Color | editors/visual_editors/connection_colors/vector3_color |
| Color | editors/visual_editors/connection_colors/vector4_color |
| int | editors/visual_editors/grid_pattern |
| float | editors/visual_editors/lines_curvature |
| float | editors/visual_editors/minimap_opacity |
| int | editors/visual_editors/visual_shader/port_preview_size |
| String | export/ssh/scp |
| String | export/ssh/ssh |
| String | filesystem/directories/autoscan_project_path |
| String | filesystem/directories/default_project_path |
| String | filesystem/external_programs/3d_model_editor |
| String | filesystem/external_programs/audio_editor |
| String | filesystem/external_programs/raster_image_editor |
| String | filesystem/external_programs/terminal_emulator |
| String | filesystem/external_programs/terminal_emulator_flags |
| String | filesystem/external_programs/vector_image_editor |
| int | filesystem/file_dialog/display_mode |
| bool | filesystem/file_dialog/show_hidden_files |
| int | filesystem/file_dialog/thumbnail_size |
| String | filesystem/file_server/password |
| int | filesystem/file_server/port |
| String | filesystem/import/blender/blender_path |
| int | filesystem/import/blender/rpc_port |
| float | filesystem/import/blender/rpc_server_uptime |
| String | filesystem/import/fbx/fbx2gltf_path |
| bool | filesystem/on_save/compress_binary_resources |
| bool | filesystem/on_save/safe_save_on_backup_then_rename |
| bool | filesystem/on_save/warn_on_saving_large_text_resources |
| int | filesystem/quick_open_dialog/default_display_mode |
| bool | filesystem/quick_open_dialog/enable_fuzzy_matching |
| bool | filesystem/quick_open_dialog/include_addons |
| bool | filesystem/quick_open_dialog/instant_preview |
| int | filesystem/quick_open_dialog/max_fuzzy_misses |
| int | filesystem/quick_open_dialog/max_results |
| bool | filesystem/quick_open_dialog/show_search_highlight |
| String | filesystem/tools/oidn/oidn_denoise_path |
| bool | input/buffering/agile_event_flushing |
| bool | input/buffering/use_accumulated_input |
| int | interface/accessibility/accessibility_support |
| int | interface/editor/accept_dialog_cancel_ok_buttons |
| bool | interface/editor/automatically_open_screenshots |
| int | interface/editor/bottom_dock_tab_style |
| String | interface/editor/code_font |
| int | interface/editor/code_font_contextual_ligatures |
| String | interface/editor/code_font_custom_opentype_features |
| String | interface/editor/code_font_custom_variations |
| int | interface/editor/code_font_size |
| bool | interface/editor/collapse_main_menu |
| float | interface/editor/custom_display_scale |
| int | interface/editor/display_scale |
| int | interface/editor/dock_tab_style |
| float | interface/editor/dragging_hover_wait_seconds |
| String | interface/editor/editor_language |
| int | interface/editor/editor_screen |
| bool | interface/editor/expand_to_title |
| bool | interface/editor/font_allow_msdf |
| int | interface/editor/font_antialiasing |
| bool | interface/editor/font_disable_embedded_bitmaps |
| int | interface/editor/font_hinting |
| int | interface/editor/font_subpixel_positioning |
| bool | interface/editor/import_resources_when_unfocused |
| bool | interface/editor/keep_screen_on |
| bool | interface/editor/localize_settings |
| int | interface/editor/low_processor_mode_sleep_usec |
| String | interface/editor/main_font |
| String | interface/editor/main_font_bold |
| String | interface/editor/main_font_custom_opentype_features |
| int | interface/editor/main_font_size |
| bool | interface/editor/mouse_extra_buttons_navigate_history |
| int | interface/editor/project_manager_screen |
| bool | interface/editor/save_each_scene_on_quit |
| bool | interface/editor/save_on_focus_loss |
| bool | interface/editor/separate_distraction_mode |
| int | interface/editor/show_internal_errors_in_toast_notifications |
| int | interface/editor/show_update_spinner |
| bool | interface/editor/single_window_mode |
| int | interface/editor/tablet_driver |
| int | interface/editor/ui_layout_direction |
| int | interface/editor/unfocused_low_processor_mode_sleep_usec |
| bool | interface/editor/update_continuously |
| bool | interface/editor/use_embedded_menu |
| bool | interface/editor/use_native_file_dialogs |
| int | interface/editor/vsync_mode |
| bool | interface/editors/derive_script_globals_by_name |
| bool | interface/editors/show_scene_tree_root_selection |
| bool | interface/inspector/auto_unfold_foreign_scenes |
| bool | interface/inspector/color_picker_show_intensity |
| int | interface/inspector/default_color_picker_mode |
| int | interface/inspector/default_color_picker_shape |
| float | interface/inspector/default_float_step |
| int | interface/inspector/default_property_name_style |
| bool | interface/inspector/delimitate_all_container_and_resources |
| bool | interface/inspector/disable_folding |
| float | interface/inspector/float_drag_speed |
| bool | interface/inspector/horizontal_vector2_editing |
| bool | interface/inspector/horizontal_vector_types_editing |
| float | interface/inspector/integer_drag_speed |
| int | interface/inspector/max_array_dictionary_items_per_page |
| int | interface/inspector/nested_color_mode |
| bool | interface/inspector/open_resources_in_current_inspector |
| PackedStringArray | interface/inspector/resources_to_open_in_new_inspector |
| bool | interface/inspector/show_low_level_opentype_features |
| bool | interface/multi_window/enable |
| bool | interface/multi_window/maximize_window |
| bool | interface/multi_window/restore_windows_on_load |
| bool | interface/scene_tabs/auto_select_current_scene_file |
| int | interface/scene_tabs/display_close_button |
| int | interface/scene_tabs/maximum_width |
| bool | interface/scene_tabs/restore_scenes_on_load |
| bool | interface/scene_tabs/show_script_button |
| bool | interface/scene_tabs/show_thumbnail_on_hover |
| Color | interface/theme/accent_color |
| int | interface/theme/additional_spacing |
| Color | interface/theme/base_color |
| int | interface/theme/base_spacing |
| int | interface/theme/border_size |
| String | interface/theme/color_preset |
| float | interface/theme/contrast |
| int | interface/theme/corner_radius |
| String | interface/theme/custom_theme |
| bool | interface/theme/draw_extra_borders |
| int | interface/theme/draw_relationship_lines |
| bool | interface/theme/follow_system_theme |
| int | interface/theme/icon_and_font_color |
| float | interface/theme/icon_saturation |
| float | interface/theme/relationship_line_opacity |
| String | interface/theme/spacing_preset |
| String | interface/theme/style |
| bool | interface/theme/use_system_accent_color |
| bool | interface/touchscreen/enable_long_press_as_right_click |
| bool | interface/touchscreen/enable_pan_and_scale_gestures |
| bool | interface/touchscreen/enable_touch_optimizations |
| float | interface/touchscreen/scale_gizmo_handles |
| int | interface/touchscreen/touch_actions_panel |
| int | network/connection/check_for_updates |
| int | network/connection/network_mode |
| String | network/debug/remote_host |
| int | network/debug/remote_port |
| String | network/http_proxy/host |
| int | network/http_proxy/port |
| String | network/tls/editor_tls_certificates |
| bool | network/tls/enable_tls_v1.3 |
| String | project_manager/default_renderer |
| int | project_manager/directory_naming_convention |
| int | project_manager/sorting_order |
| bool | run/auto_save/save_before_running |
| int | run/bottom_panel/action_on_play |
| int | run/bottom_panel/action_on_stop |
| bool | run/output/always_clear_output_on_play |
| int | run/output/font_size |
| int | run/output/max_lines |
| bool | run/platforms/linuxbsd/prefer_wayland |
| int | run/window_placement/android_window |
| int | run/window_placement/game_embed_mode |
| int | run/window_placement/rect |
| Vector2 | run/window_placement/rect_custom_position |
| int | run/window_placement/screen |
| bool | text_editor/appearance/caret/caret_blink |
| float | text_editor/appearance/caret/caret_blink_interval |
| bool | text_editor/appearance/caret/highlight_all_occurrences |
| bool | text_editor/appearance/caret/highlight_current_line |
| int | text_editor/appearance/caret/type |
| bool | text_editor/appearance/enable_inline_color_picker |
| int | text_editor/appearance/guidelines/line_length_guideline_hard_column |
| int | text_editor/appearance/guidelines/line_length_guideline_soft_column |
| bool | text_editor/appearance/guidelines/show_line_length_guidelines |
| bool | text_editor/appearance/gutters/highlight_type_safe_lines |
| bool | text_editor/appearance/gutters/line_numbers_zero_padded |
| bool | text_editor/appearance/gutters/show_info_gutter |
| bool | text_editor/appearance/gutters/show_line_numbers |
| int | text_editor/appearance/lines/autowrap_mode |
| bool | text_editor/appearance/lines/code_folding |
| int | text_editor/appearance/lines/word_wrap |
| int | text_editor/appearance/minimap/minimap_width |
| bool | text_editor/appearance/minimap/show_minimap |
| bool | text_editor/appearance/whitespace/draw_spaces |
| bool | text_editor/appearance/whitespace/draw_tabs |
| int | text_editor/appearance/whitespace/line_spacing |
| bool | text_editor/behavior/documentation/enable_tooltips |
| bool | text_editor/behavior/files/auto_reload_and_parse_scripts_on_save |
| bool | text_editor/behavior/files/auto_reload_scripts_on_external_change |
| int | text_editor/behavior/files/autosave_interval_secs |
| bool | text_editor/behavior/files/convert_indent_on_save |
| bool | text_editor/behavior/files/drop_preload_resources_as_uid |
| bool | text_editor/behavior/files/open_dominant_script_on_scene_change |
| bool | text_editor/behavior/files/restore_scripts_on_load |
| bool | text_editor/behavior/files/trim_final_newlines_on_save |
| bool | text_editor/behavior/files/trim_trailing_whitespace_on_save |
| bool | text_editor/behavior/general/empty_selection_clipboard |
| bool | text_editor/behavior/indent/auto_indent |
| bool | text_editor/behavior/indent/indent_wrapped_lines |
| int | text_editor/behavior/indent/size |
| int | text_editor/behavior/indent/type |
| String | text_editor/behavior/navigation/custom_word_separators |
| bool | text_editor/behavior/navigation/drag_and_drop_selection |
| bool | text_editor/behavior/navigation/move_caret_on_right_click |
| bool | text_editor/behavior/navigation/open_script_when_connecting_signal_to_existing_method |
| bool | text_editor/behavior/navigation/scroll_past_end_of_file |
| bool | text_editor/behavior/navigation/smooth_scrolling |
| bool | text_editor/behavior/navigation/stay_in_script_editor_on_node_selected |
| bool | text_editor/behavior/navigation/use_custom_word_separators |
| bool | text_editor/behavior/navigation/use_default_word_separators |
| int | text_editor/behavior/navigation/v_scroll_speed |
| bool | text_editor/completion/add_node_path_literals |
| bool | text_editor/completion/add_string_name_literals |
| bool | text_editor/completion/add_type_hints |
| bool | text_editor/completion/auto_brace_complete |
| float | text_editor/completion/code_complete_delay |
| bool | text_editor/completion/code_complete_enabled |
| bool | text_editor/completion/colorize_suggestions |
| bool | text_editor/completion/complete_file_paths |
| float | text_editor/completion/idle_parse_delay |
| float | text_editor/completion/idle_parse_delay_with_errors_found |
| bool | text_editor/completion/put_callhint_tooltip_below_current_line |
| bool | text_editor/completion/use_single_quotes |
| String | text_editor/external/exec_flags |
| String | text_editor/external/exec_path |
| bool | text_editor/external/use_external_editor |
| int | text_editor/help/class_reference_examples |
| int | text_editor/help/help_font_size |
| int | text_editor/help/help_source_font_size |
| int | text_editor/help/help_title_font_size |
| bool | text_editor/help/show_help_index |
| bool | text_editor/help/sort_functions_alphabetically |
| bool | text_editor/script_list/group_help_pages |
| bool | text_editor/script_list/highlight_scene_scripts |
| int | text_editor/script_list/list_script_names_as |
| bool | text_editor/script_list/script_temperature_enabled |
| int | text_editor/script_list/script_temperature_history_size |
| bool | text_editor/script_list/show_members_overview |
| bool | text_editor/script_list/sort_members_outline_alphabetically |
| int | text_editor/script_list/sort_scripts_by |
| String | text_editor/theme/color_theme |
| Color | text_editor/theme/highlighting/background_color |
| Color | text_editor/theme/highlighting/base_type_color |
| Color | text_editor/theme/highlighting/bookmark_color |
| Color | text_editor/theme/highlighting/brace_mismatch_color |
| Color | text_editor/theme/highlighting/breakpoint_color |
| Color | text_editor/theme/highlighting/caret_background_color |
| Color | text_editor/theme/highlighting/caret_color |
| Color | text_editor/theme/highlighting/code_folding_color |
| Color | text_editor/theme/highlighting/comment_color |
| Color | text_editor/theme/highlighting/comment_markers/critical_color |
| String | text_editor/theme/highlighting/comment_markers/critical_list |
| Color | text_editor/theme/highlighting/comment_markers/notice_color |
| String | text_editor/theme/highlighting/comment_markers/notice_list |
| Color | text_editor/theme/highlighting/comment_markers/warning_color |
| String | text_editor/theme/highlighting/comment_markers/warning_list |
| Color | text_editor/theme/highlighting/completion_background_color |
| Color | text_editor/theme/highlighting/completion_existing_color |
| Color | text_editor/theme/highlighting/completion_font_color |
| Color | text_editor/theme/highlighting/completion_scroll_color |
| Color | text_editor/theme/highlighting/completion_scroll_hovered_color |
| Color | text_editor/theme/highlighting/completion_selected_color |
| Color | text_editor/theme/highlighting/control_flow_keyword_color |
| Color | text_editor/theme/highlighting/current_line_color |
| Color | text_editor/theme/highlighting/doc_comment_color |
| Color | text_editor/theme/highlighting/engine_type_color |
| Color | text_editor/theme/highlighting/executing_line_color |
| Color | text_editor/theme/highlighting/folded_code_region_color |
| Color | text_editor/theme/highlighting/function_color |
| Color | text_editor/theme/highlighting/gdscript/annotation_color |
| Color | text_editor/theme/highlighting/gdscript/function_definition_color |
| Color | text_editor/theme/highlighting/gdscript/global_function_color |
| Color | text_editor/theme/highlighting/gdscript/node_path_color |
| Color | text_editor/theme/highlighting/gdscript/node_reference_color |
| Color | text_editor/theme/highlighting/gdscript/string_name_color |
| Color | text_editor/theme/highlighting/keyword_color |
| Color | text_editor/theme/highlighting/line_length_guideline_color |
| Color | text_editor/theme/highlighting/line_number_color |
| Color | text_editor/theme/highlighting/mark_color |
| Color | text_editor/theme/highlighting/member_variable_color |
| Color | text_editor/theme/highlighting/number_color |
| Color | text_editor/theme/highlighting/safe_line_number_color |
| Color | text_editor/theme/highlighting/search_result_border_color |
| Color | text_editor/theme/highlighting/search_result_color |
| Color | text_editor/theme/highlighting/selection_color |
| Color | text_editor/theme/highlighting/string_color |
| Color | text_editor/theme/highlighting/string_placeholder_color |
| Color | text_editor/theme/highlighting/symbol_color |
| Color | text_editor/theme/highlighting/text_color |
| Color | text_editor/theme/highlighting/text_selected_color |
| Color | text_editor/theme/highlighting/user_type_color |
| Color | text_editor/theme/highlighting/warning_color |
| Color | text_editor/theme/highlighting/word_highlighted_color |
| String | version_control/ssh_private_key_path |
| String | version_control/ssh_public_key_path |
| String | version_control/username |

bool
asset_library/use_threads
bool
debugger/auto_switch_to_remote_scene_tree
bool
debugger/auto_switch_to_stack_trace
debugger/max_node_selection
bool
debugger/profile_native_calls
debugger/profiler_frame_history_size
debugger/profiler_frame_max_functions
debugger/profiler_target_fps
float
debugger/remote_inspect_refresh_interval
float
debugger/remote_scene_tree_refresh_interval
bool
docks/filesystem/always_show_folders
String
docks/filesystem/other_file_extensions
String
docks/filesystem/textfile_extensions
docks/filesystem/thumbnail_size
float
docks/property_editor/auto_refresh_interval
float
docks/property_editor/subresource_hue_tint
bool
docks/scene_tree/accessibility_warnings
bool
docks/scene_tree/ask_before_deleting_related_animation_tracks
bool
docks/scene_tree/ask_before_revoking_unique_name
bool
docks/scene_tree/auto_expand_to_selected
bool
docks/scene_tree/center_node_on_reparent
bool
docks/scene_tree/hide_filtered_out_parents
bool
docks/scene_tree/start_create_dialog_fully_expanded
float
editors/2d/auto_resample_delay
Color
editors/2d/bone_color1
Color
editors/2d/bone_color2
Color
editors/2d/bone_ik_color
Color
editors/2d/bone_outline_color
float
editors/2d/bone_outline_size
Color
editors/2d/bone_selected_color
float
editors/2d/bone_width
Color
editors/2d/grid_color
Color
editors/2d/guides_color
float
editors/2d/ruler_width
Color
editors/2d/smart_snapping_line_color
bool
editors/2d/use_integer_zoom_by_default
Color
editors/2d/viewport_border_color
float
editors/2d/zoom_speed_factor
Color
editors/3d/active_selection_box_color
float
editors/3d/default_fov
float
editors/3d/default_z_far
float
editors/3d/default_z_near
editors/3d/freelook/freelook_activation_modifier
float
editors/3d/freelook/freelook_base_speed
float
editors/3d/freelook/freelook_inertia
editors/3d/freelook/freelook_navigation_scheme
float
editors/3d/freelook/freelook_sensitivity
bool
editors/3d/freelook/freelook_speed_zoom_link
float
editors/3d/grid_division_level_bias
editors/3d/grid_division_level_max
editors/3d/grid_division_level_min
editors/3d/grid_size
bool
editors/3d/grid_xy_plane
bool
editors/3d/grid_xz_plane
bool
editors/3d/grid_yz_plane
float
editors/3d/manipulator_gizmo_opacity
editors/3d/manipulator_gizmo_size
bool
editors/3d/navigation/emulate_3_button_mouse
bool
editors/3d/navigation/emulate_numpad
bool
editors/3d/navigation/invert_x_axis
bool
editors/3d/navigation/invert_y_axis
editors/3d/navigation/navigation_scheme
editors/3d/navigation/orbit_mouse_button
editors/3d/navigation/pan_mouse_button
bool
editors/3d/navigation/show_viewport_navigation_gizmo
bool
editors/3d/navigation/show_viewport_rotation_gizmo
bool
editors/3d/navigation/warped_mouse_panning
editors/3d/navigation/zoom_mouse_button
editors/3d/navigation/zoom_style
float
editors/3d/navigation_feel/angle_snap_threshold
float
editors/3d/navigation_feel/orbit_inertia
float
editors/3d/navigation_feel/orbit_sensitivity
float
editors/3d/navigation_feel/translation_inertia
float
editors/3d/navigation_feel/translation_sensitivity
float
editors/3d/navigation_feel/zoom_inertia
Color
editors/3d/primary_grid_color
editors/3d/primary_grid_steps
Color
editors/3d/secondary_grid_color
Color
editors/3d/selection_box_color
editors/3d/show_gizmo_during_rotation
Color
editors/3d_gizmos/gizmo_colors/aabb
Color
editors/3d_gizmos/gizmo_colors/camera
Color
editors/3d_gizmos/gizmo_colors/csg
Color
editors/3d_gizmos/gizmo_colors/decal
Color
editors/3d_gizmos/gizmo_colors/fog_volume
Color
editors/3d_gizmos/gizmo_colors/gridmap_grid
Color
editors/3d_gizmos/gizmo_colors/ik_chain
Color
editors/3d_gizmos/gizmo_colors/instantiated
Color
editors/3d_gizmos/gizmo_colors/joint
Color
editors/3d_gizmos/gizmo_colors/joint_body_a
Color
editors/3d_gizmos/gizmo_colors/joint_body_b
Color
editors/3d_gizmos/gizmo_colors/lightmap_lines
Color
editors/3d_gizmos/gizmo_colors/lightprobe_lines
Color
editors/3d_gizmos/gizmo_colors/occluder
Color
editors/3d_gizmos/gizmo_colors/particle_attractor
Color
editors/3d_gizmos/gizmo_colors/particle_collision
Color
editors/3d_gizmos/gizmo_colors/particles
Color
editors/3d_gizmos/gizmo_colors/path_tilt
Color
editors/3d_gizmos/gizmo_colors/reflection_probe
Color
editors/3d_gizmos/gizmo_colors/selected_bone
Color
editors/3d_gizmos/gizmo_colors/skeleton
Color
editors/3d_gizmos/gizmo_colors/spring_bone_collision
Color
editors/3d_gizmos/gizmo_colors/spring_bone_inside_collision
Color
editors/3d_gizmos/gizmo_colors/spring_bone_joint
Color
editors/3d_gizmos/gizmo_colors/stream_player_3d
Color
editors/3d_gizmos/gizmo_colors/visibility_notifier
Color
editors/3d_gizmos/gizmo_colors/voxel_gi
float
editors/3d_gizmos/gizmo_settings/bone_axis_length
editors/3d_gizmos/gizmo_settings/bone_shape
float
editors/3d_gizmos/gizmo_settings/lightmap_gi_probe_size
float
editors/3d_gizmos/gizmo_settings/path3d_tilt_disk_size
bool
editors/animation/autorename_animation_tracks
bool
editors/animation/confirm_insert_track
float
editors/animation/default_animation_step
bool
editors/animation/default_create_bezier_tracks
bool
editors/animation/default_create_reset_tracks
bool
editors/animation/default_fps_compatibility
editors/animation/default_fps_mode
bool
editors/animation/insert_at_current_time
Color
editors/animation/onion_layers_future_color
Color
editors/animation/onion_layers_past_color
Color
editors/bone_mapper/handle_colors/error
Color
editors/bone_mapper/handle_colors/missing
Color
editors/bone_mapper/handle_colors/set
Color
editors/bone_mapper/handle_colors/unset
float
editors/grid_map/pick_distance
editors/grid_map/preview_size
editors/panning/2d_editor_pan_speed
editors/panning/2d_editor_panning_scheme
editors/panning/animation_editors_panning_scheme
bool
editors/panning/simple_panning
editors/panning/sub_editors_panning_scheme
bool
editors/panning/warped_mouse_panning
editors/panning/zoom_style
float
editors/polygon_editor/auto_bake_delay
editors/polygon_editor/point_grab_radius
bool
editors/polygon_editor/show_previous_outline
bool
editors/shader_editor/behavior/files/restore_shaders_on_load
bool
editors/tiles_editor/display_grid
Color
editors/tiles_editor/grid_color
bool
editors/tiles_editor/highlight_selected_layer
Color
editors/visual_editors/category_colors/color_color
Color
editors/visual_editors/category_colors/conditional_color
Color
editors/visual_editors/category_colors/input_color
Color
editors/visual_editors/category_colors/output_color
Color
editors/visual_editors/category_colors/particle_color
Color
editors/visual_editors/category_colors/scalar_color
Color
editors/visual_editors/category_colors/special_color
Color
editors/visual_editors/category_colors/textures_color
Color
editors/visual_editors/category_colors/transform_color
Color
editors/visual_editors/category_colors/utility_color
Color
editors/visual_editors/category_colors/vector_color
String
editors/visual_editors/color_theme
Color
editors/visual_editors/connection_colors/boolean_color
Color
editors/visual_editors/connection_colors/sampler_color
Color
editors/visual_editors/connection_colors/scalar_color
Color
editors/visual_editors/connection_colors/transform_color
Color
editors/visual_editors/connection_colors/vector2_color
Color
editors/visual_editors/connection_colors/vector3_color
Color
editors/visual_editors/connection_colors/vector4_color
editors/visual_editors/grid_pattern
float
editors/visual_editors/lines_curvature
float
editors/visual_editors/minimap_opacity
editors/visual_editors/visual_shader/port_preview_size
String
export/ssh/scp
String
export/ssh/ssh
String
filesystem/directories/autoscan_project_path
String
filesystem/directories/default_project_path
String
filesystem/external_programs/3d_model_editor
String
filesystem/external_programs/audio_editor
String
filesystem/external_programs/raster_image_editor
String
filesystem/external_programs/terminal_emulator
String
filesystem/external_programs/terminal_emulator_flags
String
filesystem/external_programs/vector_image_editor
filesystem/file_dialog/display_mode
bool
filesystem/file_dialog/show_hidden_files
filesystem/file_dialog/thumbnail_size
String
filesystem/file_server/password
filesystem/file_server/port
String
filesystem/import/blender/blender_path
filesystem/import/blender/rpc_port
float
filesystem/import/blender/rpc_server_uptime
String
filesystem/import/fbx/fbx2gltf_path
bool
filesystem/on_save/compress_binary_resources
bool
filesystem/on_save/safe_save_on_backup_then_rename
bool
filesystem/on_save/warn_on_saving_large_text_resources
filesystem/quick_open_dialog/default_display_mode
bool
filesystem/quick_open_dialog/enable_fuzzy_matching
bool
filesystem/quick_open_dialog/include_addons
bool
filesystem/quick_open_dialog/instant_preview
filesystem/quick_open_dialog/max_fuzzy_misses
filesystem/quick_open_dialog/max_results
bool
filesystem/quick_open_dialog/show_search_highlight
String
filesystem/tools/oidn/oidn_denoise_path
bool
input/buffering/agile_event_flushing
bool
input/buffering/use_accumulated_input
interface/accessibility/accessibility_support
interface/editor/accept_dialog_cancel_ok_buttons
bool
interface/editor/automatically_open_screenshots
interface/editor/bottom_dock_tab_style
String
interface/editor/code_font
interface/editor/code_font_contextual_ligatures
String
interface/editor/code_font_custom_opentype_features
String
interface/editor/code_font_custom_variations
interface/editor/code_font_size
bool
interface/editor/collapse_main_menu
float
interface/editor/custom_display_scale
interface/editor/display_scale
interface/editor/dock_tab_style
float
interface/editor/dragging_hover_wait_seconds
String
interface/editor/editor_language
interface/editor/editor_screen
bool
interface/editor/expand_to_title
bool
interface/editor/font_allow_msdf
interface/editor/font_antialiasing
bool
interface/editor/font_disable_embedded_bitmaps
interface/editor/font_hinting
interface/editor/font_subpixel_positioning
bool
interface/editor/import_resources_when_unfocused
bool
interface/editor/keep_screen_on
bool
interface/editor/localize_settings
interface/editor/low_processor_mode_sleep_usec
String
interface/editor/main_font
String
interface/editor/main_font_bold
String
interface/editor/main_font_custom_opentype_features
interface/editor/main_font_size
bool
interface/editor/mouse_extra_buttons_navigate_history
interface/editor/project_manager_screen
bool
interface/editor/save_each_scene_on_quit
bool
interface/editor/save_on_focus_loss
bool
interface/editor/separate_distraction_mode
interface/editor/show_internal_errors_in_toast_notifications
interface/editor/show_update_spinner
bool
interface/editor/single_window_mode
interface/editor/tablet_driver
interface/editor/ui_layout_direction
interface/editor/unfocused_low_processor_mode_sleep_usec
bool
interface/editor/update_continuously
bool
interface/editor/use_embedded_menu
bool
interface/editor/use_native_file_dialogs
interface/editor/vsync_mode
bool
interface/editors/derive_script_globals_by_name
bool
interface/editors/show_scene_tree_root_selection
bool
interface/inspector/auto_unfold_foreign_scenes
bool
interface/inspector/color_picker_show_intensity
interface/inspector/default_color_picker_mode
interface/inspector/default_color_picker_shape
float
interface/inspector/default_float_step
interface/inspector/default_property_name_style
bool
interface/inspector/delimitate_all_container_and_resources
bool
interface/inspector/disable_folding
float
interface/inspector/float_drag_speed
bool
interface/inspector/horizontal_vector2_editing
bool
interface/inspector/horizontal_vector_types_editing
float
interface/inspector/integer_drag_speed
interface/inspector/max_array_dictionary_items_per_page
interface/inspector/nested_color_mode
bool
interface/inspector/open_resources_in_current_inspector
PackedStringArray
interface/inspector/resources_to_open_in_new_inspector
bool
interface/inspector/show_low_level_opentype_features
bool
interface/multi_window/enable
bool
interface/multi_window/maximize_window
bool
interface/multi_window/restore_windows_on_load
bool
interface/scene_tabs/auto_select_current_scene_file
interface/scene_tabs/display_close_button
interface/scene_tabs/maximum_width
bool
interface/scene_tabs/restore_scenes_on_load
bool
interface/scene_tabs/show_script_button
bool
interface/scene_tabs/show_thumbnail_on_hover
Color
interface/theme/accent_color
interface/theme/additional_spacing
Color
interface/theme/base_color
interface/theme/base_spacing
interface/theme/border_size
String
interface/theme/color_preset
float
interface/theme/contrast
interface/theme/corner_radius
String
interface/theme/custom_theme
bool
interface/theme/draw_extra_borders
interface/theme/draw_relationship_lines
bool
interface/theme/follow_system_theme
interface/theme/icon_and_font_color
float
interface/theme/icon_saturation
float
interface/theme/relationship_line_opacity
String
interface/theme/spacing_preset
String
interface/theme/style
bool
interface/theme/use_system_accent_color
bool
interface/touchscreen/enable_long_press_as_right_click
bool
interface/touchscreen/enable_pan_and_scale_gestures
bool
interface/touchscreen/enable_touch_optimizations
float
interface/touchscreen/scale_gizmo_handles
interface/touchscreen/touch_actions_panel
network/connection/check_for_updates
network/connection/network_mode
String
network/debug/remote_host
network/debug/remote_port
String
network/http_proxy/host
network/http_proxy/port
String
network/tls/editor_tls_certificates
bool
network/tls/enable_tls_v1.3
String
project_manager/default_renderer
project_manager/directory_naming_convention
project_manager/sorting_order
bool
run/auto_save/save_before_running
run/bottom_panel/action_on_play
run/bottom_panel/action_on_stop
bool
run/output/always_clear_output_on_play
run/output/font_size
run/output/max_lines
bool
run/platforms/linuxbsd/prefer_wayland
run/window_placement/android_window
run/window_placement/game_embed_mode
run/window_placement/rect
Vector2
run/window_placement/rect_custom_position
run/window_placement/screen
bool
text_editor/appearance/caret/caret_blink
float
text_editor/appearance/caret/caret_blink_interval
bool
text_editor/appearance/caret/highlight_all_occurrences
bool
text_editor/appearance/caret/highlight_current_line
text_editor/appearance/caret/type
bool
text_editor/appearance/enable_inline_color_picker
text_editor/appearance/guidelines/line_length_guideline_hard_column
text_editor/appearance/guidelines/line_length_guideline_soft_column
bool
text_editor/appearance/guidelines/show_line_length_guidelines
bool
text_editor/appearance/gutters/highlight_type_safe_lines
bool
text_editor/appearance/gutters/line_numbers_zero_padded
bool
text_editor/appearance/gutters/show_info_gutter
bool
text_editor/appearance/gutters/show_line_numbers
text_editor/appearance/lines/autowrap_mode
bool
text_editor/appearance/lines/code_folding
text_editor/appearance/lines/word_wrap
text_editor/appearance/minimap/minimap_width
bool
text_editor/appearance/minimap/show_minimap
bool
text_editor/appearance/whitespace/draw_spaces
bool
text_editor/appearance/whitespace/draw_tabs
text_editor/appearance/whitespace/line_spacing
bool
text_editor/behavior/documentation/enable_tooltips
bool
text_editor/behavior/files/auto_reload_and_parse_scripts_on_save
bool
text_editor/behavior/files/auto_reload_scripts_on_external_change
text_editor/behavior/files/autosave_interval_secs
bool
text_editor/behavior/files/convert_indent_on_save
bool
text_editor/behavior/files/drop_preload_resources_as_uid
bool
text_editor/behavior/files/open_dominant_script_on_scene_change
bool
text_editor/behavior/files/restore_scripts_on_load
bool
text_editor/behavior/files/trim_final_newlines_on_save
bool
text_editor/behavior/files/trim_trailing_whitespace_on_save
bool
text_editor/behavior/general/empty_selection_clipboard
bool
text_editor/behavior/indent/auto_indent
bool
text_editor/behavior/indent/indent_wrapped_lines
text_editor/behavior/indent/size
text_editor/behavior/indent/type
String
text_editor/behavior/navigation/custom_word_separators
bool
text_editor/behavior/navigation/drag_and_drop_selection
bool
text_editor/behavior/navigation/move_caret_on_right_click
bool
text_editor/behavior/navigation/open_script_when_connecting_signal_to_existing_method
bool
text_editor/behavior/navigation/scroll_past_end_of_file
bool
text_editor/behavior/navigation/smooth_scrolling
bool
text_editor/behavior/navigation/stay_in_script_editor_on_node_selected
bool
text_editor/behavior/navigation/use_custom_word_separators
bool
text_editor/behavior/navigation/use_default_word_separators
text_editor/behavior/navigation/v_scroll_speed
bool
text_editor/completion/add_node_path_literals
bool
text_editor/completion/add_string_name_literals
bool
text_editor/completion/add_type_hints
bool
text_editor/completion/auto_brace_complete
float
text_editor/completion/code_complete_delay
bool
text_editor/completion/code_complete_enabled
bool
text_editor/completion/colorize_suggestions
bool
text_editor/completion/complete_file_paths
float
text_editor/completion/idle_parse_delay
float
text_editor/completion/idle_parse_delay_with_errors_found
bool
text_editor/completion/put_callhint_tooltip_below_current_line
bool
text_editor/completion/use_single_quotes
String
text_editor/external/exec_flags
String
text_editor/external/exec_path
bool
text_editor/external/use_external_editor
text_editor/help/class_reference_examples
text_editor/help/help_font_size
text_editor/help/help_source_font_size
text_editor/help/help_title_font_size
bool
text_editor/help/show_help_index
bool
text_editor/help/sort_functions_alphabetically
bool
text_editor/script_list/group_help_pages
bool
text_editor/script_list/highlight_scene_scripts
text_editor/script_list/list_script_names_as
bool
text_editor/script_list/script_temperature_enabled
text_editor/script_list/script_temperature_history_size
bool
text_editor/script_list/show_members_overview
bool
text_editor/script_list/sort_members_outline_alphabetically
text_editor/script_list/sort_scripts_by
String
text_editor/theme/color_theme
Color
text_editor/theme/highlighting/background_color
Color
text_editor/theme/highlighting/base_type_color
Color
text_editor/theme/highlighting/bookmark_color
Color
text_editor/theme/highlighting/brace_mismatch_color
Color
text_editor/theme/highlighting/breakpoint_color
Color
text_editor/theme/highlighting/caret_background_color
Color
text_editor/theme/highlighting/caret_color
Color
text_editor/theme/highlighting/code_folding_color
Color
text_editor/theme/highlighting/comment_color
Color
text_editor/theme/highlighting/comment_markers/critical_color
String
text_editor/theme/highlighting/comment_markers/critical_list
Color
text_editor/theme/highlighting/comment_markers/notice_color
String
text_editor/theme/highlighting/comment_markers/notice_list
Color
text_editor/theme/highlighting/comment_markers/warning_color
String
text_editor/theme/highlighting/comment_markers/warning_list
Color
text_editor/theme/highlighting/completion_background_color
Color
text_editor/theme/highlighting/completion_existing_color
Color
text_editor/theme/highlighting/completion_font_color
Color
text_editor/theme/highlighting/completion_scroll_color
Color
text_editor/theme/highlighting/completion_scroll_hovered_color
Color
text_editor/theme/highlighting/completion_selected_color
Color
text_editor/theme/highlighting/control_flow_keyword_color
Color
text_editor/theme/highlighting/current_line_color
Color
text_editor/theme/highlighting/doc_comment_color
Color
text_editor/theme/highlighting/engine_type_color
Color
text_editor/theme/highlighting/executing_line_color
Color
text_editor/theme/highlighting/folded_code_region_color
Color
text_editor/theme/highlighting/function_color
Color
text_editor/theme/highlighting/gdscript/annotation_color
Color
text_editor/theme/highlighting/gdscript/function_definition_color
Color
text_editor/theme/highlighting/gdscript/global_function_color
Color
text_editor/theme/highlighting/gdscript/node_path_color
Color
text_editor/theme/highlighting/gdscript/node_reference_color
Color
text_editor/theme/highlighting/gdscript/string_name_color
Color
text_editor/theme/highlighting/keyword_color
Color
text_editor/theme/highlighting/line_length_guideline_color
Color
text_editor/theme/highlighting/line_number_color
Color
text_editor/theme/highlighting/mark_color
Color
text_editor/theme/highlighting/member_variable_color
Color
text_editor/theme/highlighting/number_color
Color
text_editor/theme/highlighting/safe_line_number_color
Color
text_editor/theme/highlighting/search_result_border_color
Color
text_editor/theme/highlighting/search_result_color
Color
text_editor/theme/highlighting/selection_color
Color
text_editor/theme/highlighting/string_color
Color
text_editor/theme/highlighting/string_placeholder_color
Color
text_editor/theme/highlighting/symbol_color
Color
text_editor/theme/highlighting/text_color
Color
text_editor/theme/highlighting/text_selected_color
Color
text_editor/theme/highlighting/user_type_color
Color
text_editor/theme/highlighting/warning_color
Color
text_editor/theme/highlighting/word_highlighted_color
String
version_control/ssh_private_key_path
String
version_control/ssh_public_key_path
String
version_control/username

## Methods

| void | add_property_info(info:Dictionary) |
|---|---|
| void | add_shortcut(path:String, shortcut:Shortcut) |
| bool | check_changed_settings_in_group(setting_prefix:String)const |
| void | erase(property:String) |
| PackedStringArray | get_changed_settings()const |
| PackedStringArray | get_favorites()const |
| Variant | get_project_metadata(section:String, key:String, default:Variant= null)const |
| PackedStringArray | get_recent_dirs()const |
| Variant | get_setting(name:String)const |
| Shortcut | get_shortcut(path:String)const |
| PackedStringArray | get_shortcut_list() |
| bool | has_setting(name:String)const |
| bool | has_shortcut(path:String)const |
| bool | is_shortcut(path:String, event:InputEvent)const |
| void | mark_setting_changed(setting:String) |
| void | remove_shortcut(path:String) |
| void | set_builtin_action_override(name:String, actions_list:Array[InputEvent]) |
| void | set_favorites(dirs:PackedStringArray) |
| void | set_initial_value(name:StringName, value:Variant, update_current:bool) |
| void | set_project_metadata(section:String, key:String, data:Variant) |
| void | set_recent_dirs(dirs:PackedStringArray) |
| void | set_setting(name:String, value:Variant) |

void
add_property_info(info:Dictionary)
void
add_shortcut(path:String, shortcut:Shortcut)
bool
check_changed_settings_in_group(setting_prefix:String)const
void
erase(property:String)
PackedStringArray
get_changed_settings()const
PackedStringArray
get_favorites()const
Variant
get_project_metadata(section:String, key:String, default:Variant= null)const
PackedStringArray
get_recent_dirs()const
Variant
get_setting(name:String)const
Shortcut
get_shortcut(path:String)const
PackedStringArray
get_shortcut_list()
bool
has_setting(name:String)const
bool
has_shortcut(path:String)const
bool
is_shortcut(path:String, event:InputEvent)const
void
mark_setting_changed(setting:String)
void
remove_shortcut(path:String)
void
set_builtin_action_override(name:String, actions_list:Array[InputEvent])
void
set_favorites(dirs:PackedStringArray)
void
set_initial_value(name:StringName, value:Variant, update_current:bool)
void
set_project_metadata(section:String, key:String, data:Variant)
void
set_recent_dirs(dirs:PackedStringArray)
void
set_setting(name:String, value:Variant)

## Signals
settings_changed()🔗
Emitted after any editor setting has changed.

## Constants
NOTIFICATION_EDITOR_SETTINGS_CHANGED=10000🔗
Emitted after any editor setting has changed. It's used by various editor plugins to update their visuals on theme changes or logic on configuration changes.

## Property Descriptions
boolasset_library/use_threads🔗
Iftrue, the Asset Library uses multiple threads for its HTTP requests. This prevents the Asset Library from blocking the main thread for every loaded asset.
booldebugger/auto_switch_to_remote_scene_tree🔗
Iftrue, automatically switches to theRemotescene tree when running the project from the editor. Iffalse, stays on theLocalscene tree when running the project from the editor.
Warning:Enabling this setting can cause stuttering when running a project with a large amount of nodes (typically a few thousands of nodes or more), even if the editor window isn't focused. This is due to the remote scene tree being updated every second regardless of whether the editor is focused.
booldebugger/auto_switch_to_stack_trace🔗
Iftrue, automatically switches to theStack Tracepanel when the debugger hits a breakpoint or steps.
intdebugger/max_node_selection🔗
The limit of how many remote nodes can be selected at once.
Warning:Increasing this value is not recommended, as selecting too many can make the editing and inspection of remote properties unreliable.
booldebugger/profile_native_calls🔗
Iftrue, enables collection of profiling data from non-GDScript Godot functions, such as engine class methods. Enabling this slows execution while profiling further.
intdebugger/profiler_frame_history_size🔗
The size of the profiler's frame history. The default value (3600) allows seeing up to 60 seconds of profiling if the project renders at a constant 60 FPS. Higher values allow viewing longer periods of profiling in the graphs, especially when the project is running at high framerates.
intdebugger/profiler_frame_max_functions🔗
The maximum number of script functions that can be displayed per frame in the profiler. If there are more script functions called in a given profiler frame, these functions will be discarded from the profiling results entirely.
Note:This setting is only read when the profiler is first started, so changing it during profiling will have no effect.
intdebugger/profiler_target_fps🔗
The target frame rate shown in the visual profiler graph, in frames per second.
floatdebugger/remote_inspect_refresh_interval🔗
The refresh interval for the remote inspector's properties (in seconds). Lower values are more reactive, but may cause stuttering while the project is running from the editor and theRemotescene tree is selected in the Scene tree dock.
floatdebugger/remote_scene_tree_refresh_interval🔗
The refresh interval for the remote scene tree (in seconds). Lower values are more reactive, but may cause stuttering while the project is running from the editor and theRemotescene tree is selected in the Scene tree dock.
booldocks/filesystem/always_show_folders🔗
Iftrue, displays folders in the FileSystem dock's bottom pane when split mode is enabled. Iffalse, only files will be displayed in the bottom pane. Split mode can be toggled by pressing the icon next to theres://folder path.
Note:This setting has no effect when split mode is disabled (which is the default).
Stringdocks/filesystem/other_file_extensions🔗
A comma separated list of unsupported file extensions to show in the FileSystem dock, e.g."ico,icns".
Stringdocks/filesystem/textfile_extensions🔗
A comma separated list of file extensions to consider as editable text files in the FileSystem dock (by double-clicking on the files), e.g."txt,md,cfg,ini,log,json,yml,yaml,toml,xml".
intdocks/filesystem/thumbnail_size🔗
The thumbnail size to use in the FileSystem dock (in pixels). See alsofilesystem/file_dialog/thumbnail_size.
floatdocks/property_editor/auto_refresh_interval🔗
The refresh interval to use for the Inspector dock's properties. The effect of this setting is mainly noticeable when adjusting gizmos in the 2D/3D editor and looking at the inspector at the same time. Lower values make the inspector refresh more often, but take up more CPU time.
floatdocks/property_editor/subresource_hue_tint🔗
The tint intensity to use for the subresources background in the Inspector dock. The tint is used to distinguish between different subresources in the inspector. Higher values result in a more noticeable background color difference.
booldocks/scene_tree/accessibility_warnings🔗
Iftrue, accessibility related warnings are displayed alongside other configuration warnings.
booldocks/scene_tree/ask_before_deleting_related_animation_tracks🔗
Iftrue, when a node is deleted with animation tracks referencing it, a confirmation dialog appears before the tracks are deleted. The dialog will appear even when using the "Delete (No Confirm)" shortcut.
booldocks/scene_tree/ask_before_revoking_unique_name🔗
Iftrue, displays a confirmation dialog after left-clicking the "percent" icon next to a node name in the Scene tree dock. When clicked, this icon revokes the node's scene-unique name, which can impact the behavior of scripts that rely on this scene-unique name due to identifiers not being found anymore.
booldocks/scene_tree/auto_expand_to_selected🔗
Iftrue, the scene tree dock will automatically unfold nodes when a node that has folded parents is selected.
booldocks/scene_tree/center_node_on_reparent🔗
Iftrue, new node created when reparenting node(s) will be positioned at the average position of the selected node(s).
booldocks/scene_tree/hide_filtered_out_parents🔗
Iftrue, the scene tree dock will only show nodes that match the filter, without showing parents that don't. This settings can also be changed in the Scene dock's top menu.
booldocks/scene_tree/start_create_dialog_fully_expanded🔗
Iftrue, the Create dialog (Create New Node/Create New Resource) will start with all its sections expanded. Otherwise, sections will be collapsed until the user starts searching (which will automatically expand sections as needed).
floateditors/2d/auto_resample_delay🔗
Delay time for automatic resampling in the 2D editor (in seconds).
Coloreditors/2d/bone_color1🔗
The "start" stop of the color gradient to use for bones in the 2D skeleton editor.
Coloreditors/2d/bone_color2🔗
The "end" stop of the color gradient to use for bones in the 2D skeleton editor.
Coloreditors/2d/bone_ik_color🔗
The color to use for inverse kinematics-enabled bones in the 2D skeleton editor.
Coloreditors/2d/bone_outline_color🔗
The outline color to use for non-selected bones in the 2D skeleton editor. See alsoeditors/2d/bone_selected_color.
floateditors/2d/bone_outline_size🔗
The outline size in the 2D skeleton editor (in pixels). See alsoeditors/2d/bone_width.
Note:Changes to this value only apply after modifying aBone2Dnode in any way, or closing and reopening the scene.
Coloreditors/2d/bone_selected_color🔗
The color to use for selected bones in the 2D skeleton editor. See alsoeditors/2d/bone_outline_color.
floateditors/2d/bone_width🔗
The bone width in the 2D skeleton editor (in pixels). See alsoeditors/2d/bone_outline_size.
Note:Changes to this value only apply after modifying aBone2Dnode in any way, or closing and reopening the scene.
Coloreditors/2d/grid_color🔗
The grid color to use in the 2D editor.
Coloreditors/2d/guides_color🔗
The guides color to use in the 2D editor. Guides can be created by dragging the mouse cursor from the rulers.
floateditors/2d/ruler_width🔗
The thickness of the coordinate ruler in the 2D editor. Increasing this will also increase the size of the ruler font, improving readability when using a lower editor scale. The editor may force a minimum size to keep the ruler numbers legible.
Coloreditors/2d/smart_snapping_line_color🔗
The color to use when drawing smart snapping lines in the 2D editor. The smart snapping lines will automatically display when moving 2D nodes if smart snapping is enabled in the Snapping Options menu at the top of the 2D editor viewport.
booleditors/2d/use_integer_zoom_by_default🔗
Iftrue, the 2D editor will snap to integer zoom values when not holding theAltkey. Iffalse, this behavior is swapped.
Coloreditors/2d/viewport_border_color🔗
The color of the viewport border in the 2D editor. This border represents the viewport's size at the base resolution defined in the Project Settings. Objects placed outside this border will not be visible unless aCamera2Dnode is used, or unless the window is resized and the stretch mode is set todisabled.
floateditors/2d/zoom_speed_factor🔗
The factor to use when zooming in or out in the 2D editor. For example,1.1will zoom in by 10% with every step. If set to2.0, zooming will only cycle through powers of two.
Coloreditors/3d/active_selection_box_color🔗
The color to use for the active selection box that surrounds selected nodes in the 3D editor viewport. The color's alpha channel influences the selection box's opacity.
Note:The term "active" indicates that this object is the primary selection used as the basis for certain operations. This is the last selectedNode3D, which can be reordered withShift+Leftmousebutton.
floateditors/3d/default_fov🔗
The default camera vertical field of view to use in the 3D editor (in degrees). The camera field of view can be adjusted on a per-scene basis using theViewmenu at the top of the 3D editor. If a scene had its camera field of view adjusted using theViewmenu, this setting is ignored in the scene in question. This setting is also ignored while aCamera3Dnode is being previewed in the editor.
Note:The editor camera always uses theKeep Heightaspect mode.
floateditors/3d/default_z_far🔗
The default camera far clip distance to use in the 3D editor (in degrees). Higher values make it possible to view objects placed further away from the camera, at the cost of lower precision in the depth buffer (which can result in visible Z-fighting in the distance). The camera far clip distance can be adjusted on a per-scene basis using theViewmenu at the top of the 3D editor. If a scene had its camera far clip distance adjusted using theViewmenu, this setting is ignored in the scene in question. This setting is also ignored while aCamera3Dnode is being previewed in the editor.
floateditors/3d/default_z_near🔗
The default camera near clip distance to use in the 3D editor (in degrees). Lower values make it possible to view objects placed closer to the camera, at the cost of lower precision in the depth buffer (which can result in visible Z-fighting in the distance). The camera near clip distance can be adjusted on a per-scene basis using theViewmenu at the top of the 3D editor. If a scene had its camera near clip distance adjusted using theViewmenu, this setting is ignored in the scene in question. This setting is also ignored while aCamera3Dnode is being previewed in the editor.
inteditors/3d/freelook/freelook_activation_modifier🔗
The modifier key to use to enable freelook in the 3D editor (on top of pressing the right mouse button).
Note:Regardless of this setting, the freelook toggle keyboard shortcut (Shift+Fby default) is always available.
Note:On certain window managers on Linux, theAltkey will be intercepted by the window manager when clicking a mouse button at the same time. This means Godot will not see the modifier key as being pressed.
floateditors/3d/freelook/freelook_base_speed🔗
The base 3D freelook speed in units per second. This can be adjusted by using the mouse wheel while in freelook mode, or by holding down the "fast" or "slow" modifier keys (ShiftandAltby default, respectively).
floateditors/3d/freelook/freelook_inertia🔗
The inertia of the 3D freelook camera. Higher values make the camera start and stop slower, which looks smoother but adds latency.
inteditors/3d/freelook/freelook_navigation_scheme🔗
The navigation scheme to use when freelook is enabled in the 3D editor. Some of the navigation schemes below may be more convenient when designing specific levels in the 3D editor.
- Default:The "Freelook Forward", "Freelook Backward", "Freelook Up" and "Freelook Down" keys will move relative to the camera, taking its pitch angle into account for the movement.
Default:The "Freelook Forward", "Freelook Backward", "Freelook Up" and "Freelook Down" keys will move relative to the camera, taking its pitch angle into account for the movement.
- Partially Axis-Locked:The "Freelook Forward" and "Freelook Backward" keys will move relative to the camera, taking its pitch angle into account for the movement. The "Freelook Up" and "Freelook Down" keys will move in an "absolute" manner,nottaking the camera's pitch angle into account for the movement.
Partially Axis-Locked:The "Freelook Forward" and "Freelook Backward" keys will move relative to the camera, taking its pitch angle into account for the movement. The "Freelook Up" and "Freelook Down" keys will move in an "absolute" manner,nottaking the camera's pitch angle into account for the movement.
- Fully Axis-Locked:The "Freelook Forward", "Freelook Backward", "Freelook Up" and "Freelook Down" keys will move in an "absolute" manner,nottaking the camera's pitch angle into account for the movement.
Fully Axis-Locked:The "Freelook Forward", "Freelook Backward", "Freelook Up" and "Freelook Down" keys will move in an "absolute" manner,nottaking the camera's pitch angle into account for the movement.
See alsoeditors/3d/navigation/navigation_scheme.
floateditors/3d/freelook/freelook_sensitivity🔗
The mouse sensitivity to use while freelook mode is active in the 3D editor. See alsoeditors/3d/navigation_feel/orbit_sensitivity.
booleditors/3d/freelook/freelook_speed_zoom_link🔗
Iftrue, freelook speed is linked to the zoom value used in the camera orbit mode in the 3D editor.
floateditors/3d/grid_division_level_bias🔗
The grid division bias to use in the 3D editor. Negative values will cause small grid divisions to appear earlier, whereas positive values will cause small grid divisions to appear later.
inteditors/3d/grid_division_level_max🔗
The largest grid division to use in the 3D editor. Together witheditors/3d/primary_grid_steps, this determines how large the grid divisions can be. The grid divisions will not be able to get larger thanprimary_grid_steps^grid_division_level_maxunits. By default, wheneditors/3d/primary_grid_stepsis8, this means grid divisions cannot get larger than64units each (so primary grid lines are512units apart), no matter how far away the camera is from the grid.
inteditors/3d/grid_division_level_min🔗
The smallest grid division to use in the 3D editor. Together witheditors/3d/primary_grid_steps, this determines how small the grid divisions can be. The grid divisions will not be able to get smaller thanprimary_grid_steps^grid_division_level_minunits. By default, this means grid divisions cannot get smaller than 1 unit each, no matter how close the camera is from the grid.
inteditors/3d/grid_size🔗
The grid size in units. Higher values prevent the grid from appearing "cut off" at certain angles, but make the grid more demanding to render. Depending on the camera's position, the grid may not be fully visible since a shader is used to fade it progressively.
booleditors/3d/grid_xy_plane🔗
Iftrue, renders the grid on the XY plane in perspective view. This can be useful for 3D side-scrolling games.
booleditors/3d/grid_xz_plane🔗
Iftrue, renders the grid on the XZ plane in perspective view.
booleditors/3d/grid_yz_plane🔗
Iftrue, renders the grid on the YZ plane in perspective view. This can be useful for 3D side-scrolling games.
floateditors/3d/manipulator_gizmo_opacity🔗
Opacity of the default gizmo for moving, rotating, and scaling 3D nodes.
inteditors/3d/manipulator_gizmo_size🔗
Size of the default gizmo for moving, rotating, and scaling 3D nodes.
booleditors/3d/navigation/emulate_3_button_mouse🔗
Iftrue, enables 3-button mouse emulation mode. This is useful on laptops when using a trackpad.
When 3-button mouse emulation mode is enabled, the pan, zoom and orbit modifiers can always be used in the 3D editor viewport, even when not holding down any mouse button.
booleditors/3d/navigation/emulate_numpad🔗
Iftrue, allows using the top row0-9keys to function as their equivalent numpad keys for 3D editor navigation. This should be enabled on keyboards that have no numeric keypad available.
booleditors/3d/navigation/invert_x_axis🔗
Iftrue, invert the horizontal mouse axis when panning or orbiting in the 3D editor. This setting doesnotapply to freelook mode.
booleditors/3d/navigation/invert_y_axis🔗
Iftrue, invert the vertical mouse axis when panning, orbiting, or using freelook mode in the 3D editor.
inteditors/3d/navigation/navigation_scheme🔗
The navigation scheme preset to use in the 3D editor. Changing this setting will affect the mouse button and modifier keys used to navigate the 3D editor viewport.
All schemes can useMousewheelto zoom.
- Godot:Middlemousebuttonto orbit.Shift+Middlemousebuttonto pan.Ctrl+Middlemousebuttonto zoom.
Godot:Middlemousebuttonto orbit.Shift+Middlemousebuttonto pan.Ctrl+Middlemousebuttonto zoom.
- Maya:Alt+Leftmousebuttonto orbit.Middlemousebuttonto pan,Shift+Middlemousebuttonto pan 10 times faster.Alt+Rightmousebuttonto zoom.
Maya:Alt+Leftmousebuttonto orbit.Middlemousebuttonto pan,Shift+Middlemousebuttonto pan 10 times faster.Alt+Rightmousebuttonto zoom.
- Modo:Alt+Leftmousebuttonto orbit.Alt+Shift+Leftmousebuttonto pan.Ctrl+Alt+Leftmousebuttonto zoom.
Modo:Alt+Leftmousebuttonto orbit.Alt+Shift+Leftmousebuttonto pan.Ctrl+Alt+Leftmousebuttonto zoom.
- Tablet/Trackpad:Altto orbit.Shiftto pan.Ctrlto zoom. Enables 3-button mouse emulation mode.
Tablet/Trackpad:Altto orbit.Shiftto pan.Ctrlto zoom. Enables 3-button mouse emulation mode.
See alsoeditors/3d/navigation/orbit_mouse_button,editors/3d/navigation/pan_mouse_button,editors/3d/navigation/zoom_mouse_button,editors/3d/freelook/freelook_navigation_scheme, andeditors/3d/navigation/emulate_3_button_mouse.
Note:On certain window managers on Linux, theAltkey will be intercepted by the window manager when clicking a mouse button at the same time. This means Godot will not see the modifier key as being pressed.
inteditors/3d/navigation/orbit_mouse_button🔗
The mouse button that needs to be held down to orbit in the 3D editor viewport.
inteditors/3d/navigation/pan_mouse_button🔗
The mouse button that needs to be held down to pan in the 3D editor viewport.
booleditors/3d/navigation/show_viewport_navigation_gizmo🔗
Iftrue, shows gizmos for moving and rotating the camera in the bottom corners of the 3D editor's viewport. Useful for devices that use touch screen.
booleditors/3d/navigation/show_viewport_rotation_gizmo🔗
Iftrue, shows a small orientation gizmo in the top-right corner of the 3D editor's viewports.
booleditors/3d/navigation/warped_mouse_panning🔗
Iftrue, warps the mouse around the 3D viewport while panning in the 3D editor. This makes it possible to pan over a large area without having to exit panning and adjust the mouse cursor.
inteditors/3d/navigation/zoom_mouse_button🔗
The mouse button that needs to be held down to zoom in the 3D editor viewport.
inteditors/3d/navigation/zoom_style🔗
The mouse cursor movement direction to use when zooming by moving the mouse. This does not affect zooming with the mouse wheel.
floateditors/3d/navigation_feel/angle_snap_threshold🔗
The angle threshold for snapping camera rotation to 45-degree angles while orbiting withAltheld.
floateditors/3d/navigation_feel/orbit_inertia🔗
The inertia to use when orbiting in the 3D editor. Higher values make the camera start and stop slower, which looks smoother but adds latency.
floateditors/3d/navigation_feel/orbit_sensitivity🔗
The mouse sensitivity to use when orbiting in the 3D editor. See alsoeditors/3d/freelook/freelook_sensitivity.
floateditors/3d/navigation_feel/translation_inertia🔗
The inertia to use when panning in the 3D editor. Higher values make the camera start and stop slower, which looks smoother but adds latency.
floateditors/3d/navigation_feel/translation_sensitivity🔗
The mouse sensitivity to use when panning in the 3D editor.
floateditors/3d/navigation_feel/zoom_inertia🔗
The inertia to use when zooming in the 3D editor. Higher values make the camera start and stop slower, which looks smoother but adds latency.
Coloreditors/3d/primary_grid_color🔗
The color to use for the primary 3D grid. The color's alpha channel affects the grid's opacity.
inteditors/3d/primary_grid_steps🔗
If set above 0, where a primary grid line should be drawn. By default, primary lines are configured to be more visible than secondary lines. This helps with measurements in the 3D editor. See alsoeditors/3d/primary_grid_colorandeditors/3d/secondary_grid_color.
Coloreditors/3d/secondary_grid_color🔗
The color to use for the secondary 3D grid. This is generally a less visible color thaneditors/3d/primary_grid_color. The color's alpha channel affects the grid's opacity.
Coloreditors/3d/selection_box_color🔗
The color to use for the selection box that surrounds selected nodes in the 3D editor viewport. The color's alpha channel influences the selection box's opacity.
inteditors/3d/show_gizmo_during_rotation🔗
If checked, the transform gizmo remains visible during rotation in that transform mode.
Coloreditors/3d_gizmos/gizmo_colors/aabb🔗
The color to use for the AABB gizmo that displays theGeometryInstance3D's customAABB.
Coloreditors/3d_gizmos/gizmo_colors/camera🔗
The 3D editor gizmo color forCamera3Ds.
Coloreditors/3d_gizmos/gizmo_colors/csg🔗
The 3D editor gizmo color for CSG nodes (such asCSGShape3DorCSGBox3D).
Coloreditors/3d_gizmos/gizmo_colors/decal🔗
The 3D editor gizmo color forDecalnodes.
Coloreditors/3d_gizmos/gizmo_colors/fog_volume🔗
The 3D editor gizmo color forFogVolumenodes.
Coloreditors/3d_gizmos/gizmo_colors/gridmap_grid🔗
The 3D editor gizmo color for theGridMapgrid.
Coloreditors/3d_gizmos/gizmo_colors/ik_chain🔗
The 3D editor gizmo color for theIKModifier3Dguides.
Coloreditors/3d_gizmos/gizmo_colors/instantiated🔗
The color override to use for 3D editor gizmos if theNode3Din question is part of an instantiated scene file (from the perspective of the current scene).
Coloreditors/3d_gizmos/gizmo_colors/joint🔗
The 3D editor gizmo color forJoint3Ds andPhysicalBone3Ds.
Coloreditors/3d_gizmos/gizmo_colors/joint_body_a🔗
Color for representingJoint3D.node_afor someJoint3Dtypes.
Coloreditors/3d_gizmos/gizmo_colors/joint_body_b🔗
Color for representingJoint3D.node_bfor someJoint3Dtypes.
Coloreditors/3d_gizmos/gizmo_colors/lightmap_lines🔗
Color of lines displayed in bakedLightmapGInode's grid.
Coloreditors/3d_gizmos/gizmo_colors/lightprobe_lines🔗
The 3D editor gizmo color used forLightmapProbenodes.
Coloreditors/3d_gizmos/gizmo_colors/occluder🔗
The 3D editor gizmo color used forOccluderInstance3Dnodes.
Coloreditors/3d_gizmos/gizmo_colors/particle_attractor🔗
The 3D editor gizmo color used forGPUParticlesAttractor3Dnodes.
Coloreditors/3d_gizmos/gizmo_colors/particle_collision🔗
The 3D editor gizmo color used forGPUParticlesCollision3Dnodes.
Coloreditors/3d_gizmos/gizmo_colors/particles🔗
The 3D editor gizmo color used forCPUParticles3DandGPUParticles3Dnodes.
Coloreditors/3d_gizmos/gizmo_colors/path_tilt🔗
The 3D editor gizmo color used forPath3Dtilt circles, which indicate the direction theCurve3Dis tilted towards.
Coloreditors/3d_gizmos/gizmo_colors/reflection_probe🔗
The 3D editor gizmo color used forReflectionProbenodes.
Coloreditors/3d_gizmos/gizmo_colors/selected_bone🔗
The 3D editor gizmo color used for the currently selectedSkeleton3Dbone.
Coloreditors/3d_gizmos/gizmo_colors/skeleton🔗
The 3D editor gizmo color used forSkeleton3Dnodes.
Coloreditors/3d_gizmos/gizmo_colors/spring_bone_collision🔗
The 3D editor gizmo color used forSpringBoneCollision3Dnodes.
Coloreditors/3d_gizmos/gizmo_colors/spring_bone_inside_collision🔗
The 3D editor gizmo color used forSpringBoneCollision3Dnodes with inside mode.
Coloreditors/3d_gizmos/gizmo_colors/spring_bone_joint🔗
The 3D editor gizmo color used forSpringBoneSimulator3Dnodes.
Coloreditors/3d_gizmos/gizmo_colors/stream_player_3d🔗
The 3D editor gizmo color used forAudioStreamPlayer3D's emission angle.
Coloreditors/3d_gizmos/gizmo_colors/visibility_notifier🔗
The 3D editor gizmo color used forVisibleOnScreenNotifier3DandVisibleOnScreenEnabler3Dnodes.
Coloreditors/3d_gizmos/gizmo_colors/voxel_gi🔗
The 3D editor gizmo color used forVoxelGInodes.
floateditors/3d_gizmos/gizmo_settings/bone_axis_length🔗
The length ofSkeleton3Dbone gizmos in the 3D editor.
inteditors/3d_gizmos/gizmo_settings/bone_shape🔗
The shape ofSkeleton3Dbone gizmos in the 3D editor.Wireis a thin line, whileOctahedronis a set of lines that represent a thicker hollow line pointing in a specific direction (similar to most 3D animation software).
floateditors/3d_gizmos/gizmo_settings/lightmap_gi_probe_size🔗
Size of probe gizmos displayed when editingLightmapGIandLightmapProbenodes. Setting this to0.0will hide the probe spheres ofLightmapGIand wireframes ofLightmapProbenodes, but will keep the wireframes linking probes fromLightmapGIand billboard icons fromLightmapProbeintact.
floateditors/3d_gizmos/gizmo_settings/path3d_tilt_disk_size🔗
Size of the disk gizmo displayed when editingPath3D's tilt handles.
booleditors/animation/autorename_animation_tracks🔗
Iftrue, automatically updates animation tracks' target paths when renaming or reparenting nodes in the Scene tree dock.
booleditors/animation/confirm_insert_track🔗
Iftrue, display a confirmation dialog when adding a new track to an animation by pressing the "key" icon next to a property. Holding Shift will bypass the dialog.
Iffalse, the behavior is reversed, i.e. the dialog only appears when Shift is held.
floateditors/animation/default_animation_step🔗
Default step used when creating a newAnimationin the Animation bottom panel. Only affects the first animation created in theAnimationPlayer. By default, other newly created animations will use the step from the previous ones.
This value is always expressed in seconds. If you want e.g.10FPS to be the default, you need to set the default step to0.1.
booleditors/animation/default_create_bezier_tracks🔗
Iftrue, create a Bezier track instead of a standard track when pressing the "key" icon next to a property. Bezier tracks provide more control over animation curves, but are more difficult to adjust quickly.
booleditors/animation/default_create_reset_tracks🔗
Iftrue, create aRESETtrack when creating a new animation track. This track can be used to restore the animation to a "default" state.
booleditors/animation/default_fps_compatibility🔗
Controls whetherAnimationPlayerwill apply snapping to nearest integer FPS when snapping is in Seconds mode. The option is remembered locally for a scene and this option only determines the default value when scene doesn't have local state yet.
inteditors/animation/default_fps_mode🔗
Default step mode forAnimationPlayer(seconds or FPS). The option is remembered locally for a scene and this option only determines the default value when scene doesn't have local state yet.
booleditors/animation/insert_at_current_time🔗
Iftrue, animation keys and markers are inserted at the current time in the animation.
Iffalse, they are inserted at the mouse cursor's position.
Coloreditors/animation/onion_layers_future_color🔗
The modulate color to use for "future" frames displayed in the animation editor's onion skinning feature.
Coloreditors/animation/onion_layers_past_color🔗
The modulate color to use for "past" frames displayed in the animation editor's onion skinning feature.
Coloreditors/bone_mapper/handle_colors/error🔗
There is currently no description for this property. Please help us bycontributing one!
Coloreditors/bone_mapper/handle_colors/missing🔗
There is currently no description for this property. Please help us bycontributing one!
Coloreditors/bone_mapper/handle_colors/set🔗
There is currently no description for this property. Please help us bycontributing one!
Coloreditors/bone_mapper/handle_colors/unset🔗
There is currently no description for this property. Please help us bycontributing one!
floateditors/grid_map/pick_distance🔗
The maximum distance at which tiles can be placed on a GridMap, relative to the camera position (in 3D units).
inteditors/grid_map/preview_size🔗
Texture size of mesh previews generated for GridMap's MeshLibrary.
inteditors/panning/2d_editor_pan_speed🔗
The panning speed when using the mouse wheel or touchscreen events in the 2D editor. This setting does not apply to panning by holding down the middle or right mouse buttons.
inteditors/panning/2d_editor_panning_scheme🔗
Controls whether the mouse wheel scroll zooms or pans in the 2D editor. See alsoeditors/panning/sub_editors_panning_schemeandeditors/panning/animation_editors_panning_scheme.
inteditors/panning/animation_editors_panning_scheme🔗
Controls whether the mouse wheel scroll zooms or pans in the animation track and Bezier editors. See alsoeditors/panning/2d_editor_panning_schemeandeditors/panning/sub_editors_panning_scheme(which controls the animation blend tree editor's pan behavior).
booleditors/panning/simple_panning🔗
Iftrue, allows panning by holding downSpacein the 2D editor viewport (in addition to panning with the middle or right mouse buttons). Iffalse, the left mouse button must be held down while holding downSpaceto pan in the 2D editor viewport.
inteditors/panning/sub_editors_panning_scheme🔗
Controls whether the mouse wheel scroll zooms or pans in subeditors. The list of affected subeditors is: animation blend tree editor,Polygon2Deditor, tileset editor, texture region editor and visual shader editor. See alsoeditors/panning/2d_editor_panning_schemeandeditors/panning/animation_editors_panning_scheme.
booleditors/panning/warped_mouse_panning🔗
Iftrue, warps the mouse around the 2D viewport while panning in the 2D editor. This makes it possible to pan over a large area without having to exit panning and adjust the mouse cursor.
inteditors/panning/zoom_style🔗
The mouse cursor movement direction to use when drag-zooming in any editor (except 3D scene editor) by moving the mouse. This does not affect zooming with the mouse wheel.
floateditors/polygon_editor/auto_bake_delay🔗
The delay in seconds until more complex and performance costly polygon editors commit their outlines, e.g. the 2D navigation polygon editor rebakes the navigation mesh polygons. A negative value stops the auto bake.
inteditors/polygon_editor/point_grab_radius🔗
The radius in which points can be selected in thePolygon2DandCollisionPolygon2Deditors (in pixels). Higher values make it easier to select points quickly, but can make it more difficult to select the expected point when several points are located close to each other.
booleditors/polygon_editor/show_previous_outline🔗
Iftrue, displays the polygon's previous shape in the 2D polygon editors with an opaque gray outline. This outline is displayed while dragging a point until the left mouse button is released.
booleditors/shader_editor/behavior/files/restore_shaders_on_load🔗
Iftrue, reopens shader files that were open in the shader editor when the project was last closed.
booleditors/tiles_editor/display_grid🔗
Iftrue, displays a grid while the TileMap editor is active. See alsoeditors/tiles_editor/grid_color.
Coloreditors/tiles_editor/grid_color🔗
The color to use for the TileMap editor's grid.
Note:Only effective ifeditors/tiles_editor/display_gridistrue.
booleditors/tiles_editor/highlight_selected_layer🔗
Highlight the currently selected TileMapLayer by dimming the other ones in the scene.
Coloreditors/visual_editors/category_colors/color_color🔗
The color of a graph node's header when it belongs to the "Color" category.
Coloreditors/visual_editors/category_colors/conditional_color🔗
The color of a graph node's header when it belongs to the "Conditional" category.
Coloreditors/visual_editors/category_colors/input_color🔗
The color of a graph node's header when it belongs to the "Input" category.
Coloreditors/visual_editors/category_colors/output_color🔗
The color of a graph node's header when it belongs to the "Output" category.
Coloreditors/visual_editors/category_colors/particle_color🔗
The color of a graph node's header when it belongs to the "Particle" category.
Coloreditors/visual_editors/category_colors/scalar_color🔗
The color of a graph node's header when it belongs to the "Scalar" category.
Coloreditors/visual_editors/category_colors/special_color🔗
The color of a graph node's header when it belongs to the "Special" category.
Coloreditors/visual_editors/category_colors/textures_color🔗
The color of a graph node's header when it belongs to the "Textures" category.
Coloreditors/visual_editors/category_colors/transform_color🔗
The color of a graph node's header when it belongs to the "Transform" category.
Coloreditors/visual_editors/category_colors/utility_color🔗
The color of a graph node's header when it belongs to the "Utility" category.
Coloreditors/visual_editors/category_colors/vector_color🔗
The color of a graph node's header when it belongs to the "Vector" category.
Stringeditors/visual_editors/color_theme🔗
The color theme to use in the visual shader editor.
Coloreditors/visual_editors/connection_colors/boolean_color🔗
The color of a port/connection of boolean type.
Coloreditors/visual_editors/connection_colors/sampler_color🔗
The color of a port/connection of sampler type.
Coloreditors/visual_editors/connection_colors/scalar_color🔗
The color of a port/connection of scalar type (float, int, unsigned int).
Coloreditors/visual_editors/connection_colors/transform_color🔗
The color of a port/connection of transform type.
Coloreditors/visual_editors/connection_colors/vector2_color🔗
The color of a port/connection of Vector2 type.
Coloreditors/visual_editors/connection_colors/vector3_color🔗
The color of a port/connection of Vector3 type.
Coloreditors/visual_editors/connection_colors/vector4_color🔗
The color of a port/connection of Vector4 type.
inteditors/visual_editors/grid_pattern🔗
The pattern used for the background grid.
floateditors/visual_editors/lines_curvature🔗
The curvature to use for connection lines in the visual shader editor. Higher values will make connection lines appear more curved, with values above0.5resulting in more "angular" turns in the middle of connection lines.
floateditors/visual_editors/minimap_opacity🔗
The opacity of the minimap displayed in the bottom-right corner of the visual shader editor.
inteditors/visual_editors/visual_shader/port_preview_size🔗
The size to use for port previews in the visual shader uniforms (toggled by clicking the "eye" icon next to an output). The value is defined in pixels at 100% zoom, and will scale with zoom automatically.
Stringexport/ssh/scp🔗
Path to the SCP (secure copy) executable (used for remote deploy to desktop platforms). If left empty, the editor will attempt to runscpfromPATH.
Note:SCP is not the same as SFTP. Specifying the SFTP executable here will not work.
Stringexport/ssh/ssh🔗
Path to the SSH executable (used for remote deploy to desktop platforms). If left empty, the editor will attempt to runsshfromPATH.
Stringfilesystem/directories/autoscan_project_path🔗
The folder where projects should be scanned for (recursively), in a way similar to the project manager'sScanbutton. This can be set to the same value asfilesystem/directories/default_project_pathfor convenience.
Note:Setting this path to a folder with very large amounts of files/folders can slow down the project manager startup significantly. To keep the project manager quick to start up, it is recommended to set this value to a folder as "specific" as possible.
Stringfilesystem/directories/default_project_path🔗
The folder where new projects should be created by default when clicking the project manager'sNew Projectbutton. This can be set to the same value asfilesystem/directories/autoscan_project_pathfor convenience.
Stringfilesystem/external_programs/3d_model_editor🔗
The program that opens 3D model scene files when clicking "Open in External Program" option in Filesystem Dock. If not specified, the file will be opened in the system's default program.
Stringfilesystem/external_programs/audio_editor🔗
The program that opens audio files when clicking "Open in External Program" option in Filesystem Dock. If not specified, the file will be opened in the system's default program.
Stringfilesystem/external_programs/raster_image_editor🔗
The program that opens raster image files when clicking "Open in External Program" option in Filesystem Dock. If not specified, the file will be opened in the system's default program.
Stringfilesystem/external_programs/terminal_emulator🔗
The terminal emulator program to use when usingOpen in Terminalcontext menu action in the FileSystem dock. You can enter an absolute path to a program binary, or a path to a program that is present in thePATHenvironment variable.
If left empty, Godot will use the default terminal emulator for the system:
- Windows:PowerShell
Windows:PowerShell
- macOS:Terminal.app
macOS:Terminal.app
- Linux:The first terminal found on the system in this order: gnome-terminal, konsole, xfce4-terminal, lxterminal, kitty, alacritty, urxvt, xterm.
Linux:The first terminal found on the system in this order: gnome-terminal, konsole, xfce4-terminal, lxterminal, kitty, alacritty, urxvt, xterm.
To use Command Prompt (cmd) instead of PowerShell on Windows, entercmdin this field and the correct flags will automatically be used.
On macOS, make sure to point to the actual program binary located within thePrograms/MacOSfolder of the .app bundle, rather than the .app bundle directory.
If specifying a custom terminal emulator, you may need to overridefilesystem/external_programs/terminal_emulator_flagsso it opens in the correct folder.
Stringfilesystem/external_programs/terminal_emulator_flags🔗
The command-line arguments to pass to the terminal emulator that is run when usingOpen in Terminalcontext menu action in the FileSystem dock. See alsofilesystem/external_programs/terminal_emulator.
If left empty, the default flags are{directory}, which is replaced by the absolute path to the directory that is being opened in the terminal.
Note:If the terminal emulator is set to PowerShell, cmd, or Konsole, Godot will automatically prepend arguments to this list, as these terminals require nonstandard arguments to open in the correct folder.
Stringfilesystem/external_programs/vector_image_editor🔗
The program that opens vector image files when clicking "Open in External Program" option in Filesystem Dock. If not specified, the file will be opened in the system's default program.
intfilesystem/file_dialog/display_mode🔗
The display mode to use in the editor's file dialogs.
- Thumbnailstakes more space, but displays dynamic resource thumbnails, making resources easier to preview without having to open them.
Thumbnailstakes more space, but displays dynamic resource thumbnails, making resources easier to preview without having to open them.
- Listis more compact but doesn't display dynamic resource thumbnails. Instead, it displays static icons based on the file extension.
Listis more compact but doesn't display dynamic resource thumbnails. Instead, it displays static icons based on the file extension.
boolfilesystem/file_dialog/show_hidden_files🔗
Iftrue, display hidden files in the editor's file dialogs. Files that have names starting with.are considered hidden (e.g..hidden_file).
intfilesystem/file_dialog/thumbnail_size🔗
The thumbnail size to use in the editor's file dialogs (in pixels). See alsodocks/filesystem/thumbnail_size.
Stringfilesystem/file_server/password🔗
Password used for file server when exporting project with remote file system.
intfilesystem/file_server/port🔗
Port used for file server when exporting project with remote file system.
Stringfilesystem/import/blender/blender_path🔗
The path to the Blender executable used for converting the Blender 3D scene files.blendto glTF 2.0 format during import. Blender 3.0 or later is required.
To enable this feature for your specific project, useProjectSettings.filesystem/import/blender/enabled.
If this setting is empty, Blender's default paths will be detected and used automatically if present in this order:
Windows:
```
- C:\Program Files\Blender Foundation\blender.exe
- C:\Program Files (x86)\Blender Foundation\blender.exe
```
macOS:
```
- /opt/homebrew/bin/blender
- /opt/local/bin/blender
- /usr/local/bin/blender
- /usr/local/opt/blender
- /Applications/Blender.app/Contents/MacOS/Blender
```
Linux/*BSD:
```
- /usr/bin/blender
- /usr/local/bin/blender
- /opt/blender/bin/blender
```
intfilesystem/import/blender/rpc_port🔗
The port number used for Remote Procedure Call (RPC) communication with Godot's created process of the blender executable.
Setting this to 0 effectively disables communication with Godot and the blender process, making performance slower.
floatfilesystem/import/blender/rpc_server_uptime🔗
The maximum idle uptime (in seconds) of the Blender process.
This prevents Godot from having to create a new process for each import within the given seconds.
Stringfilesystem/import/fbx/fbx2gltf_path🔗
The path to the FBX2glTF executable used for converting Autodesk FBX 3D scene files.fbxto glTF 2.0 format during import.
To enable this feature for your specific project, useProjectSettings.filesystem/import/fbx2gltf/enabled.
boolfilesystem/on_save/compress_binary_resources🔗
Iftrue, uses lossless compression for binary resources.
boolfilesystem/on_save/safe_save_on_backup_then_rename🔗
Iftrue, when saving a file, the editor will rename the old file to a different name, save a new file, then only remove the old file once the new file has been saved. This makes loss of data less likely to happen if the editor or operating system exits unexpectedly while saving (e.g. due to a crash or power outage).
Note:On Windows, this feature can interact negatively with certain antivirus programs. In this case, you may have to set this tofalseto prevent file locking issues.
boolfilesystem/on_save/warn_on_saving_large_text_resources🔗
Iftrue, displays a warning toast message when saving a text-based scene or resource that is larger than 500 KiB on disk. This is typically caused by binary subresources being embedded as text, which results in slow and inefficient conversion to text. This in turn impacts scene saving and loading times.
This should usually be resolved by moving the embedded binary subresource to its own binary resource file (.resextension instead of.tres). This is the preferred approach. Alternatively, the entire scene can be saved with the binary.scnformat as opposed to.tscn, but this will make it less friendly to version control systems.
intfilesystem/quick_open_dialog/default_display_mode🔗
If set toAdaptive, the dialog opens in list view or grid view depending on the requested type. If set toLastUsed, the display mode will always open the way you last used it.
boolfilesystem/quick_open_dialog/enable_fuzzy_matching🔗
Iftrue, together with exact matches of a filename, the dialog includes approximate matches.
This is useful for finding the correct files even when there are typos in the search query; for example, searching "nprmal" will find "normal". Additionally, it allows you to write shorter search queries; for example, searching "nml" will also find "normal".
See alsofilesystem/quick_open_dialog/max_fuzzy_misses.
boolfilesystem/quick_open_dialog/include_addons🔗
Iftrue, results will include files located in theaddonsfolder.
boolfilesystem/quick_open_dialog/instant_preview🔗
Iftrue, highlighting a resource will preview it quickly without confirming the selection or closing the dialog.
intfilesystem/quick_open_dialog/max_fuzzy_misses🔗
The number of missed query characters allowed in a match when fuzzy matching is enabled. For example, with the default value of2,"normal"would match"narmal"and"norma"but not"nor".
intfilesystem/quick_open_dialog/max_results🔗
Maximum number of matches to show in dialog.
boolfilesystem/quick_open_dialog/show_search_highlight🔗
Iftrue, results will be highlighted with their search matches.
Stringfilesystem/tools/oidn/oidn_denoise_path🔗
The path to the directory containing the Open Image Denoise (OIDN) executable, used optionally for denoising lightmaps. It can be downloaded fromopenimagedenoise.org.
To enable this feature for your specific project, useProjectSettings.rendering/lightmapping/denoising/denoiser.
boolinput/buffering/agile_event_flushing🔗
Iftrue, input events will be flushed just before every idle and physics frame.
Iffalse, these events will be flushed only once per process frame, between iterations of the engine.
Enabling this setting can greatly improve input responsiveness, especially in devices that struggle to run at the project's intended frame rate.
boolinput/buffering/use_accumulated_input🔗
Iftrue, similar input events sent by the operating system are accumulated. When input accumulation is enabled, all input events generated during a frame will be merged and emitted when the frame is done rendering. Therefore, this limits the number of input method calls per second to the rendering FPS.
Input accumulation can be disabled to get slightly more precise/reactive input at the cost of increased CPU usage.
Note:Input accumulation isenabledby default.
intinterface/accessibility/accessibility_support🔗
Editor accessibility support mode:
- Auto(0): Accessibility support is enabled, but updates to the accessibility information are processed only if an assistive app (such as a screen reader or a Braille display) is active (default).
Auto(0): Accessibility support is enabled, but updates to the accessibility information are processed only if an assistive app (such as a screen reader or a Braille display) is active (default).
- Always Active(1): Accessibility support is enabled, and updates to the accessibility information are always processed, regardless of the status of assistive apps.
Always Active(1): Accessibility support is enabled, and updates to the accessibility information are always processed, regardless of the status of assistive apps.
- Disabled(2): Accessibility support is fully disabled.
Disabled(2): Accessibility support is fully disabled.
Note:Accessibility debugging tools, such as Accessibility Insights for Windows, Accessibility Inspector (macOS), or AT-SPI Browser (Linux/BSD), do not count as assistive apps. To test the editor with these tools, useAlways Active.
intinterface/editor/accept_dialog_cancel_ok_buttons🔗
How to position the Cancel and OK buttons in the editor'sAcceptDialogwindows. Different platforms have different conventions for this, which can be overridden through this setting to avoid accidental clicks when using Godot on multiple platforms.
- Autofollows the platform convention: OK first on Windows, KDE, and LXQt; Cancel first on macOS and other Linux desktop environments.
Autofollows the platform convention: OK first on Windows, KDE, and LXQt; Cancel first on macOS and other Linux desktop environments.
- Cancel Firstforces the Cancel/OK ordering.
Cancel Firstforces the Cancel/OK ordering.
- OK Firstforces the OK/Cancel ordering.
OK Firstforces the OK/Cancel ordering.
To check if these buttons are swapped at runtime, useDisplayServer.get_swap_cancel_ok().
boolinterface/editor/automatically_open_screenshots🔗
Iftrue, automatically opens screenshots with the default program associated to.pngfiles after a screenshot is taken using theEditor > Take Screenshotaction.
intinterface/editor/bottom_dock_tab_style🔗
Tab style of editor docks located at the bottom.
Stringinterface/editor/code_font🔗
The font to use for the script editor. Must be a resource of aFonttype such as a.ttfor.otffont file.
intinterface/editor/code_font_contextual_ligatures🔗
The font ligatures to enable for the currently configured code font. Not all fonts include support for ligatures.
Note:The default editor code font (JetBrains Mono) has contextual ligatures in its font file.
Stringinterface/editor/code_font_custom_opentype_features🔗
List of custom OpenType features to use, if supported by the currently configured code font. Not all fonts include support for custom OpenType features. The string should follow the OpenType specification.
Note:The default editor code font (JetBrains Mono) has custom OpenType features in its font file, but there is no documented list yet.
Stringinterface/editor/code_font_custom_variations🔗
List of alternative characters to use, if supported by the currently configured code font. Not all fonts include support for custom variations. The string should follow the OpenType specification.
Note:The default editor code font (JetBrains Mono) has alternate characters in its font file, but there is no documented list yet.
intinterface/editor/code_font_size🔗
The size of the font in the script editor. This setting does not impact the font size of the Output panel (seerun/output/font_size).
boolinterface/editor/collapse_main_menu🔗
Iftrue, the main menu collapses into aMenuButton.
Note:This setting is only applicable on macOS wheninterface/editor/use_embedded_menuistrue.
Note:Defaults totrueon the Android editor.
floatinterface/editor/custom_display_scale🔗
The custom editor scale factor to use. This can be used for displays with very high DPI where a scale factor of 200% is not sufficient.
Note:Only effective ifinterface/editor/display_scaleis set toCustom.
intinterface/editor/display_scale🔗
The display scale factor to use for the editor interface. Higher values are more suited to hiDPI/Retina displays.
If set toAuto, the editor scale is automatically determined based on the screen resolution and reported display DPI. This heuristic is not always ideal, which means you can get better results by setting the editor scale manually.
If set toCustom, the scaling value ininterface/editor/custom_display_scalewill be used.
intinterface/editor/dock_tab_style🔗
Tab style of editor docks, except bottom docks.
floatinterface/editor/dragging_hover_wait_seconds🔗
During a drag-and-drop, this is how long to wait over a UI element before it triggers a reaction (e.g. a section unfolds to show nested items).
Stringinterface/editor/editor_language🔗
The language to use for the editor interface. If set toAuto, the language is automatically determined based on the system locale. See alsoEditorInterface.get_editor_language().
Translations are provided by the community. If you spot a mistake,contribute to editor translations on Weblate!
intinterface/editor/editor_screen🔗
The preferred monitor to display the editor. IfAuto, the editor will remember the last screen it was displayed on across multiple sessions.
boolinterface/editor/expand_to_title🔗
Expanding main editor window content to the title, if supported byDisplayServer. SeeDisplayServer.WINDOW_FLAG_EXTEND_TO_TITLE.
Specific to the macOS platform.
boolinterface/editor/font_allow_msdf🔗
If set totrue, MSDF font rendering will be used for the visual shader graph editor. You may need to set this tofalsewhen using a custom main font, as some fonts will look broken due to the use of self-intersecting outlines in their font data. Downloading the font from the font maker's official website as opposed to a service like Google Fonts can help resolve this issue.
intinterface/editor/font_antialiasing🔗
FreeType's font anti-aliasing mode used to render the editor fonts. Most fonts are not designed to look good with anti-aliasing disabled, so it's recommended to leave this enabled unless you're using a pixel art font.
boolinterface/editor/font_disable_embedded_bitmaps🔗
If set totrue, embedded font bitmap loading is disabled (bitmap-only and color fonts ignore this property).
intinterface/editor/font_hinting🔗
The font hinting mode to use for the editor fonts. FreeType supports the following font hinting modes:
- None:Don't use font hinting when rasterizing the font. This results in a smooth font, but it can look blurry.
None:Don't use font hinting when rasterizing the font. This results in a smooth font, but it can look blurry.
- Light:Use hinting on the X axis only. This is a compromise between font sharpness and smoothness.
Light:Use hinting on the X axis only. This is a compromise between font sharpness and smoothness.
- Normal:Use hinting on both X and Y axes. This results in a sharp font, but it doesn't look very smooth.
Normal:Use hinting on both X and Y axes. This results in a sharp font, but it doesn't look very smooth.
If set toAuto, the font hinting mode will be set to match the current operating system in use. This means theLighthinting mode will be used on Windows and Linux, and theNonehinting mode will be used on macOS.
intinterface/editor/font_subpixel_positioning🔗
The subpixel positioning mode to use when rendering editor font glyphs. This affects both the main and code fonts.Disabledis the fastest to render and uses the least memory.Autoonly uses subpixel positioning for small font sizes (where the benefit is the most noticeable).One Half of a PixelandOne Quarter of a Pixelforce the same subpixel positioning mode for all editor fonts, regardless of their size (withOne Quarter of a Pixelbeing the highest-quality option).
boolinterface/editor/import_resources_when_unfocused🔗
Iftrue, (re)imports resources even if the editor window is unfocused or minimized. Iffalse, resources are only (re)imported when the editor window is focused. This can be set totrueto speed up iteration by starting the import process earlier when saving files in the project folder. This also allows getting visual feedback on changes without having to click the editor window, which is useful with multi-monitor setups. The downside of setting this totrueis that it increases idle CPU usage and may steal CPU time from other applications when importing resources.
boolinterface/editor/keep_screen_on🔗
Iftrue, keeps the screen on (even in case of inactivity), so the screensaver does not take over. Works on desktop and mobile platforms.
boolinterface/editor/localize_settings🔗
Iftrue, setting names in the editor are localized when possible.
Note:This setting affects mostEditorInspectors in the editor UI, primarily Project Settings and Editor Settings. To control names displayed in the Inspector dock, useinterface/inspector/default_property_name_styleinstead.
intinterface/editor/low_processor_mode_sleep_usec🔗
The amount of sleeping between frames in the editor (in microseconds). Higher values will result in lower CPU/GPU usage, which can improve battery life on laptops. However, higher values will result in a less responsive editor. The default value is set to allow for maximum smoothness on monitors up to 144 Hz. See alsointerface/editor/unfocused_low_processor_mode_sleep_usec.
Note:This setting is ignored ifinterface/editor/update_continuouslyistrue, as enabling that setting disables low-processor mode.
Stringinterface/editor/main_font🔗
The font to use for the editor interface. Must be a resource of aFonttype such as a.ttfor.otffont file.
Note:If the provided font is variable, a weight of 400 (normal) will be used.
Stringinterface/editor/main_font_bold🔗
The font to use for bold text in the editor interface. Must be a resource of aFonttype such as a.ttfor.otffont file.
Note:If the provided font is variable, a weight of 700 (bold) will be used.
Stringinterface/editor/main_font_custom_opentype_features🔗
List of custom OpenType features to use, if supported by the currently configured main font. Check what OpenType features are supported by your font first.
The string should follow the OpenType specification, e.g.ss01,tnum,calt=false. Microsoft's documentation contains a list ofall registered features.
Note:The default editor main font (Inter) has custom OpenType features in its font file, withss04andtnumenabled andcaltdisabled by default. Supported features can be found at its website.
intinterface/editor/main_font_size🔗
The size of the font in the editor interface.
boolinterface/editor/mouse_extra_buttons_navigate_history🔗
Iftrue, the mouse's additional side buttons will be usable to navigate in the script editor's file history. Set this tofalseif you're using the side buttons for other purposes (such as a push-to-talk button in a VoIP program).
intinterface/editor/project_manager_screen🔗
The preferred monitor to display the project manager.
boolinterface/editor/save_each_scene_on_quit🔗
Iffalse, the editor will save all scenes when confirming theSaveaction when quitting the editor or quitting to the project list. Iftrue, the editor will ask to save each scene individually.
boolinterface/editor/save_on_focus_loss🔗
Iftrue, scenes and scripts are saved when the editor loses focus. Depending on the work flow, this behavior can be less intrusive thantext_editor/behavior/files/autosave_interval_secsor remembering to save manually.
boolinterface/editor/separate_distraction_mode🔗
Iftrue, the editor's Script tab will have a separate distraction mode setting from the 2D/3D/Game/AssetLib tabs. Iffalse, the distraction-free mode toggle is shared between all tabs.
intinterface/editor/show_internal_errors_in_toast_notifications🔗
If enabled, displays internal engine errors in toast notifications (toggleable by clicking the "bell" icon at the bottom of the editor). No matter the value of this setting, non-internal engine errors will always be visible in toast notifications.
The defaultAutovalue will only enable this if the editor was compiled with thedev_build=yesSCons option (the default isdev_build=no).
intinterface/editor/show_update_spinner🔗
If enabled, displays an icon in the top-right corner of the editor that spins when the editor redraws a frame. This can be used to diagnose situations where the engine is constantly redrawing, which should be avoided as this increases CPU and GPU utilization for no good reason. To further troubleshoot these situations, start the editor with the--debug-canvas-item-redrawcommand line argument.
Consider enabling this if you are developing editor plugins to ensure they only make the editor redraw when required.
The defaultAutovalue will only enable this if the editor was compiled with thedev_build=yesSCons option (the default isdev_build=no).
Note:Ifinterface/editor/update_continuouslyistrue, the spinner icon displays in red.
Note:If the editor was started with the--debug-canvas-item-redrawcommand line argument, the update spinner willneverdisplay regardless of this setting's value. This is to avoid confusion with what would cause redrawing in real world scenarios.
boolinterface/editor/single_window_mode🔗
Iftrue, embed modal windows such as docks inside the main editor window. When single-window mode is enabled, tooltips will also be embedded inside the main editor window, which means they can't be displayed outside of the editor window. Single-window mode can be faster as it does not need to create a separate window for every popup and tooltip, which can be a slow operation depending on the operating system and rendering method in use.
This is equivalent toProjectSettings.display/window/subwindows/embed_subwindowsin the running project, except the setting's value is inverted.
Note:To query whether the editor can use multiple windows in an editor plugin, useEditorInterface.is_multi_window_enabled()instead of querying the value of this editor setting.
Note:Iftrue, game embedding is disabled.
intinterface/editor/tablet_driver🔗
Overrides the tablet driver used by the editor.
intinterface/editor/ui_layout_direction🔗
Editor UI default layout direction.
intinterface/editor/unfocused_low_processor_mode_sleep_usec🔗
When the editor window is unfocused, the amount of sleeping between frames when the low-processor usage mode is enabled (in microseconds). Higher values will result in lower CPU/GPU usage, which can improve battery life on laptops (in addition to improving the running project's performance if the editor has to redraw continuously). However, higher values will result in a less responsive editor. The default value is set to limit the editor to 10 FPS when the editor window is unfocused. See alsointerface/editor/low_processor_mode_sleep_usec.
Note:This setting is ignored ifinterface/editor/update_continuouslyistrue, as enabling that setting disables low-processor mode.
boolinterface/editor/update_continuously🔗
Iftrue, redraws the editor every frame even if nothing has changed on screen. When this setting is enabled, the update spinner displays in red (seeinterface/editor/show_update_spinner).
Warning:This greatly increases CPU and GPU utilization, leading to increased power usage. This should only be enabled for troubleshooting purposes.
boolinterface/editor/use_embedded_menu🔗
Iftrue, editor main menu is using embeddedMenuBarinstead of system global menu.
Specific to the macOS platform.
boolinterface/editor/use_native_file_dialogs🔗
Iftrue, editor UI uses OS native file/directory selection dialogs.
intinterface/editor/vsync_mode🔗
Sets the V-Sync mode for the editor. Does not affect the project when run from the editor (this is controlled byProjectSettings.display/window/vsync/vsync_mode).
Depending on the platform and used renderer, the engine will fall back toEnabledif the desired mode is not supported.
Note:V-Sync modes other thanEnabledare only supported in the Forward+ and Mobile rendering methods, not Compatibility.
boolinterface/editors/derive_script_globals_by_name🔗
Iftrue, when extending a script, the global class name of the script is inserted in the script creation dialog, if it exists. Iffalse, the script's file path is always inserted.
boolinterface/editors/show_scene_tree_root_selection🔗
Iftrue, the Scene dock will display buttons to quickly add a root node to a newly created scene.
boolinterface/inspector/auto_unfold_foreign_scenes🔗
Iftrue, automatically unfolds Inspector property groups containing modified values when opening a scene for the first time. Only affects scenes without saved folding preferences and only unfolds groups with properties that have been changed from their default values.
Note:This setting only works in specific scenarios: when opening a scene brought in from another project, or when opening a new scene that already has modified properties (e.g., from version control). Duplicated scenes are not considered foreign, so this setting will not affect them.
boolinterface/inspector/color_picker_show_intensity🔗
Iftrue, show the intensity slider in theColorPickers opened in the editor.
intinterface/inspector/default_color_picker_mode🔗
The default color picker mode to use when openingColorPickers in the editor. This mode can be temporarily adjusted on the color picker itself.
intinterface/inspector/default_color_picker_shape🔗
The default color picker shape to use when openingColorPickers in the editor. This shape can be temporarily adjusted on the color picker itself.
floatinterface/inspector/default_float_step🔗
The floating-point precision to use for properties that don't define an explicit precision step. Lower values allow entering more precise values.
intinterface/inspector/default_property_name_style🔗
The default property name style to display in the Inspector dock. This style can be temporarily adjusted in the Inspector dock's menu.
- Raw:Displays properties insnake_case.
Raw:Displays properties insnake_case.
- Capitalized:Displays properties capitalized.
Capitalized:Displays properties capitalized.
- Localized:Displays the localized string for the current editor language if a translation is available for the given property. If no translation is available, falls back toCapitalized.
Localized:Displays the localized string for the current editor language if a translation is available for the given property. If no translation is available, falls back toCapitalized.
Note:To display translated setting names in Project Settings and Editor Settings, useinterface/editor/localize_settingsinstead.
boolinterface/inspector/delimitate_all_container_and_resources🔗
Iftrue, add a margin around Array, Dictionary, and Resource Editors that are not already colored.
Note:Ifinterface/inspector/nested_color_modeis set toContainers & Resourcesthis parameter will have no effect since those editors will already be colored.
boolinterface/inspector/disable_folding🔗
Iftrue, forces all property groups to be expanded in the Inspector dock and prevents collapsing them.
floatinterface/inspector/float_drag_speed🔗
Base speed for increasing/decreasing float values by dragging them in the inspector.
boolinterface/inspector/horizontal_vector2_editing🔗
Iftrue,Vector2andVector2iproperties are shown on a single line in the inspector instead of two lines. This is overall more compact, but it can be harder to view and edit large values without expanding the inspector horizontally.
boolinterface/inspector/horizontal_vector_types_editing🔗
Iftrue,Vector3,Vector3i,Vector4,Vector4i,Rect2,Rect2i,Plane, andQuaternionproperties are shown on a single line in the inspector instead of multiple lines. This is overall more compact, but it can be harder to view and edit large values without expanding the inspector horizontally.
floatinterface/inspector/integer_drag_speed🔗
Base speed for increasing/decreasing integer values by dragging them in the inspector.
intinterface/inspector/max_array_dictionary_items_per_page🔗
The number ofArrayorDictionaryitems to display on each "page" in the inspector. Higher values allow viewing more values per page, but take more time to load. This increased load time is noticeable when selecting nodes that have array or dictionary properties in the editor.
intinterface/inspector/nested_color_mode🔗
Control which property editors are colored when they are opened.
- Containers & Resources:Color all Array, Dictionary, and Resource Editors.
Containers & Resources:Color all Array, Dictionary, and Resource Editors.
- Resources:Color all Resource Editors.
Resources:Color all Resource Editors.
- External Resources:Color Resource Editors that edits an external resource.
External Resources:Color Resource Editors that edits an external resource.
boolinterface/inspector/open_resources_in_current_inspector🔗
Iftrue, subresources can be edited in the current inspector view. If the resource type is defined ininterface/inspector/resources_to_open_in_new_inspectoror if this setting isfalse, attempting to edit a subresource always opens a new inspector view.
PackedStringArrayinterface/inspector/resources_to_open_in_new_inspector🔗
List of resources that should always be opened in a new inspector view, even ifinterface/inspector/open_resources_in_current_inspectoristrue.
Note:The returned array iscopiedand any changes to it will not update the original property value. SeePackedStringArrayfor more details.
boolinterface/inspector/show_low_level_opentype_features🔗
Iftrue, display OpenType features marked ashiddenby the font file in theFonteditor.
boolinterface/multi_window/enable🔗
Iftrue, multiple window support in editor is enabled. The following panels can become dedicated windows (i.e. made floating): Docks, Script editor, Shader editor, and Game Workspace.
Note:Wheninterface/editor/single_window_modeistrue, the multi window support is always disabled.
Note:To query whether the editor can use multiple windows in an editor plugin, useEditorInterface.is_multi_window_enabled()instead of querying the value of this editor setting.
boolinterface/multi_window/maximize_window🔗
Iftrue, when panels are made floating they will be maximized.
Iffalse, when panels are made floating their position and size will match the ones when they are attached (excluding window border) to the editor window.
boolinterface/multi_window/restore_windows_on_load🔗
Iftrue, the floating panel position, size, and screen will be saved on editor exit. On next launch the panels that were floating will be made floating in the saved positions, sizes and screens, if possible.
boolinterface/scene_tabs/auto_select_current_scene_file🔗
Iftrue, the FileSystem dock will automatically navigate to the currently selected scene tab.
intinterface/scene_tabs/display_close_button🔗
Controls when the Close (X) button is displayed on scene tabs at the top of the editor.
intinterface/scene_tabs/maximum_width🔗
The maximum width of each scene tab at the top editor (in pixels).
boolinterface/scene_tabs/restore_scenes_on_load🔗
Iftrue, when a project is loaded, restores scenes that were opened on the last editor session.
Note:With many opened scenes, the editor may take longer to become usable. If starting the editor quickly is necessary, consider setting this tofalse.
boolinterface/scene_tabs/show_script_button🔗
Iftrue, show a button next to each scene tab that opens the scene's "dominant" script when clicked. The "dominant" script is the one that is at the highest level in the scene's hierarchy.
boolinterface/scene_tabs/show_thumbnail_on_hover🔗
Iftrue, display an automatically-generated thumbnail when hovering scene tabs with the mouse. Scene thumbnails are generated when saving the scene.
Colorinterface/theme/accent_color🔗
The color to use for "highlighted" user interface elements in the editor (pressed and hovered items).
intinterface/theme/additional_spacing🔗
The extra spacing to add to various GUI elements in the editor (in pixels). Increasing this value is useful to improve usability on touch screens, at the cost of reducing the amount of usable screen real estate.
See alsointerface/theme/spacing_preset.
Colorinterface/theme/base_color🔗
The base color to use for user interface elements in the editor. Secondary colors (such as darker/lighter variants) are derived from this color.
intinterface/theme/base_spacing🔗
The base spacing used by various GUI elements in the editor (in pixels). See alsointerface/theme/spacing_preset.
intinterface/theme/border_size🔗
The border size to use for interface elements (in pixels).
Stringinterface/theme/color_preset🔗
The editor color preset to use.
floatinterface/theme/contrast🔗
The contrast factor to use when deriving the editor theme's base color (seeinterface/theme/base_color). When using a positive values, the derived colors will bedarkerthan the base color. This contrast factor can be set to a negative value, which will make the derived colorsbrighterthan the base color. Negative contrast rates often look better for light themes.
intinterface/theme/corner_radius🔗
The corner radius to use for interface elements (in pixels).0is square.
Stringinterface/theme/custom_theme🔗
The custom theme resource to use for the editor. Must be a Godot theme resource in.tresor.resformat.
boolinterface/theme/draw_extra_borders🔗
Iftrue, draws additional borders around interactive UI elements in the editor. This is automatically enabled when using theBlack (OLED)theme preset, as this theme preset uses a fully black background.
intinterface/theme/draw_relationship_lines🔗
What relationship lines to draw in the editor'sTree-based GUIs (such as the Scene tree dock).
- Nonewill make it so that no relationship lines are drawn.
Nonewill make it so that no relationship lines are drawn.
- Selected Onlywill only draw them for selected items.
Selected Onlywill only draw them for selected items.
- Allwill always draw them for all items.
Allwill always draw them for all items.
boolinterface/theme/follow_system_theme🔗
Iftrue, the editor theme preset will attempt to automatically match the system theme.
intinterface/theme/icon_and_font_color🔗
The icon and font color scheme to use in the editor.
- Autodetermines the color scheme to use automatically based oninterface/theme/base_color.
Autodetermines the color scheme to use automatically based oninterface/theme/base_color.
- Darkmakes fonts and icons dark (suitable for light themes). Icon colors are automatically converted by the editor following the set of rules defined inthis file.
Darkmakes fonts and icons dark (suitable for light themes). Icon colors are automatically converted by the editor following the set of rules defined inthis file.
- Lightmakes fonts and icons light (suitable for dark themes).
Lightmakes fonts and icons light (suitable for dark themes).
floatinterface/theme/icon_saturation🔗
The saturation to use for editor icons. Higher values result in more vibrant colors.
Note:The default editor icon saturation was increased by 30% in Godot 4.0 and later. To get Godot 3.x's icon saturation back, setinterface/theme/icon_saturationto0.77.
floatinterface/theme/relationship_line_opacity🔗
The opacity to use when drawing relationship lines in the editor'sTree-based GUIs (such as the Scene tree dock).
Stringinterface/theme/spacing_preset🔗
The editor theme spacing preset to use. See alsointerface/theme/base_spacingandinterface/theme/additional_spacing.
Stringinterface/theme/style🔗
The editor theme style to use.
boolinterface/theme/use_system_accent_color🔗
Iftrue, set accent color based on system settings.
Note:This setting is only effective on Windows, MacOS, and Android.
boolinterface/touchscreen/enable_long_press_as_right_click🔗
Iftrue, long press on touchscreen is treated as right click.
Note:Defaults totrueon touchscreen devices.
boolinterface/touchscreen/enable_pan_and_scale_gestures🔗
Iftrue, enable two finger pan and scale gestures on touchscreen devices.
Note:Defaults totrueon touchscreen devices.
boolinterface/touchscreen/enable_touch_optimizations🔗
Iftrue, increases the scrollbar touch area, enables a larger dragger for split containers, and increases PopupMenu vertical separation to improve usability on touchscreen devices.
Note:Defaults totrueon touchscreen devices.
floatinterface/touchscreen/scale_gizmo_handles🔗
Specify the multiplier to apply to the scale for the editor gizmo handles to improve usability on touchscreen devices.
Note:Defaults to1on non-touchscreen devices.
intinterface/touchscreen/touch_actions_panel🔗
A touch-friendly panel that provides easy access to common actions such as save, delete, undo, and redo without requiring a keyboard.
Note:Only available in the Android and XR editor.
intnetwork/connection/check_for_updates🔗
Specifies how the engine should check for updates.
- Disable Update Checkswill block the engine from checking updates (see alsonetwork/connection/network_mode).
Disable Update Checkswill block the engine from checking updates (see alsonetwork/connection/network_mode).
- Check Newest Preview(default for preview versions) will check for the newest available development snapshot.
Check Newest Preview(default for preview versions) will check for the newest available development snapshot.
- Check Newest Stable(default for stable versions) will check for the newest available stable version.
Check Newest Stable(default for stable versions) will check for the newest available stable version.
- Check Newest Patchwill check for the latest available stable version, but only within the same minor version. E.g. if your version is4.3.stable, you will be notified about4.3.1.stable, but not4.4.stable.
Check Newest Patchwill check for the latest available stable version, but only within the same minor version. E.g. if your version is4.3.stable, you will be notified about4.3.1.stable, but not4.4.stable.
All update modes will ignore builds with different major versions (e.g. Godot 4 -> Godot 5).
intnetwork/connection/network_mode🔗
Determines whether online features, such as the Asset Library or update checks, are enabled in the editor. If this is a privacy concern, disabling these online features prevents the editor from making HTTP requests to the Godot website or third-party platforms hosting assets from the Asset Library.
Editor plugins and tool scripts are recommended to follow this setting. However, Godot can't prevent them from violating this rule.
Stringnetwork/debug/remote_host🔗
The address to listen to when starting the remote debugger. This can be set to this device's local IP address to allow external clients to connect to the remote debugger (instead of restricting the remote debugger to connections fromlocalhost).
intnetwork/debug/remote_port🔗
The port to listen to when starting the remote debugger. Godot will try to use port numbers above the configured number if the configured number is already taken by another application.
Stringnetwork/http_proxy/host🔗
The host to use to contact the HTTP and HTTPS proxy in the editor (for the asset library and export template downloads). See alsonetwork/http_proxy/port.
Note:Godot currently doesn't automatically use system proxy settings, so you have to enter them manually here if needed.
intnetwork/http_proxy/port🔗
The port number to use to contact the HTTP and HTTPS proxy in the editor (for the asset library and export template downloads). See alsonetwork/http_proxy/host.
Note:Godot currently doesn't automatically use system proxy settings, so you have to enter them manually here if needed.
Stringnetwork/tls/editor_tls_certificates🔗
The TLS certificate bundle to use for HTTP requests made within the editor (e.g. from the AssetLib tab). If left empty, theincluded Mozilla certificate bundlewill be used.
boolnetwork/tls/enable_tls_v1.3🔗
Iftrue, enable TLSv1.3 negotiation.
Note:Only supported when using Mbed TLS 3.0 or later (Linux distribution packages may be compiled against older system Mbed TLS packages), otherwise the maximum supported TLS version is always TLSv1.2.
Stringproject_manager/default_renderer🔗
The renderer type that will be checked off by default when creating a new project. Accepted strings are "forward_plus", "mobile" or "gl_compatibility".
intproject_manager/directory_naming_convention🔗
Directory naming convention for the project manager. Options are "No Convention" (project name is directory name), "kebab-case" (default), "snake_case", "camelCase", "PascalCase", or "Title Case".
intproject_manager/sorting_order🔗
The sorting order to use in the project manager. When changing the sorting order in the project manager, this setting is set permanently in the editor settings.
boolrun/auto_save/save_before_running🔗
Iftrue, saves all scenes and scripts automatically before running the project. Setting this tofalseprevents the editor from saving if there are no changes which can speed up the project startup slightly, but it makes it possible to run a project that has unsaved changes. (Unsaved changes will not be visible in the running project.)
intrun/bottom_panel/action_on_play🔗
The action to execute on the bottom panel when running the project.
Note:This option won't do anything if the bottom panel switching is locked using the pin button in the corner of the bottom panel.
intrun/bottom_panel/action_on_stop🔗
The action to execute on the bottom panel when stopping the project.
Note:This option won't do anything if the bottom panel switching is locked using the pin button in the corner of the bottom panel.
boolrun/output/always_clear_output_on_play🔗
Iftrue, the editor will clear the Output panel when running the project.
intrun/output/font_size🔗
The size of the font in theOutputpanel at the bottom of the editor. This setting does not impact the font size of the script editor (seeinterface/editor/code_font_size).
intrun/output/max_lines🔗
Maximum number of lines to show at any one time in the Output panel.
boolrun/platforms/linuxbsd/prefer_wayland🔗
Iftrue, on Linux/BSD, the editor will check for Wayland first instead of X11 (if available).
intrun/window_placement/android_window🔗
Specifies how the Play window is launched relative to the Android editor.
- Auto (based on screen size)(default) will automatically choose how to launch the Play window based on the device and screen metrics. Defaults toSame as Editoron phones andSide-by-side with Editoron tablets.
Auto (based on screen size)(default) will automatically choose how to launch the Play window based on the device and screen metrics. Defaults toSame as Editoron phones andSide-by-side with Editoron tablets.
- Same as Editorwill launch the Play window in the same window as the Editor.
Same as Editorwill launch the Play window in the same window as the Editor.
- Side-by-side with Editorwill launch the Play window side-by-side with the Editor window.
Side-by-side with Editorwill launch the Play window side-by-side with the Editor window.
Note:Only available in the Android editor.
intrun/window_placement/game_embed_mode🔗
Overrides game embedding setting for all newly opened projects. If enabled, game embedding settings are not saved.
intrun/window_placement/rect🔗
The window mode to use to display the project when starting the project from the editor.
Note:Game embedding is not available for"Force Maximized"or"Force Fullscreen".
Vector2run/window_placement/rect_custom_position🔗
The custom position to use when starting the project from the editor (in pixels from the top-left corner). Only effective ifrun/window_placement/rectis set toCustom Position.
intrun/window_placement/screen🔗
The monitor to display the project on when starting the project from the editor.
booltext_editor/appearance/caret/caret_blink🔗
Iftrue, makes the caret blink according totext_editor/appearance/caret/caret_blink_interval. Disabling this setting can improve battery life on laptops if you spend long amounts of time in the script editor, since it will reduce the frequency at which the editor needs to be redrawn.
floattext_editor/appearance/caret/caret_blink_interval🔗
The interval at which the caret will blink (in seconds). See alsotext_editor/appearance/caret/caret_blink.
booltext_editor/appearance/caret/highlight_all_occurrences🔗
Iftrue, highlights all occurrences of the currently selected text in the script editor. See alsotext_editor/theme/highlighting/word_highlighted_color.
booltext_editor/appearance/caret/highlight_current_line🔗
Iftrue, colors the background of the line the caret is currently on withtext_editor/theme/highlighting/current_line_color.
inttext_editor/appearance/caret/type🔗
The shape of the caret to use in the script editor.Linedisplays a vertical line to the left of the current character, whereasBlockdisplays an outline over the current character.
booltext_editor/appearance/enable_inline_color_picker🔗
Iftrue, displays a colored button before anyColorconstructor in the script editor. Clicking on them allows the color to be modified through a color picker.
inttext_editor/appearance/guidelines/line_length_guideline_hard_column🔗
The column at which to display a subtle line as a line length guideline for scripts. This should generally be greater thantext_editor/appearance/guidelines/line_length_guideline_soft_column.
inttext_editor/appearance/guidelines/line_length_guideline_soft_column🔗
The column at which to display averysubtle line as a line length guideline for scripts. This should generally be lower thantext_editor/appearance/guidelines/line_length_guideline_hard_column.
booltext_editor/appearance/guidelines/show_line_length_guidelines🔗
Iftrue, displays line length guidelines to help you keep line lengths in check. See alsotext_editor/appearance/guidelines/line_length_guideline_soft_columnandtext_editor/appearance/guidelines/line_length_guideline_hard_column.
booltext_editor/appearance/gutters/highlight_type_safe_lines🔗
Iftrue, highlights type-safe lines by displaying their line number color withtext_editor/theme/highlighting/safe_line_number_colorinstead oftext_editor/theme/highlighting/line_number_color. Type-safe lines are lines of code where the type of all variables is known at compile-time. These type-safe lines may run faster thanks to typed instructions.
booltext_editor/appearance/gutters/line_numbers_zero_padded🔗
Iftrue, displays line numbers with zero padding (e.g.007instead of7).
booltext_editor/appearance/gutters/show_info_gutter🔗
Iftrue, displays a gutter at the left containing icons for methods with signal connections and for overridden methods.
booltext_editor/appearance/gutters/show_line_numbers🔗
Iftrue, displays line numbers in a gutter at the left.
inttext_editor/appearance/lines/autowrap_mode🔗
Iftext_editor/appearance/lines/word_wrapis set to1, sets text wrapping mode. To see how each mode behaves, seeAutowrapMode.
booltext_editor/appearance/lines/code_folding🔗
Iftrue, displays the folding arrows next to indented code sections and allows code folding. Iffalse, hides the folding arrows next to indented code sections and disallows code folding.
inttext_editor/appearance/lines/word_wrap🔗
Iftrue, wraps long lines over multiple lines to avoid horizontal scrolling. This is a display-only feature; it does not actually insert line breaks in your scripts.
inttext_editor/appearance/minimap/minimap_width🔗
The width of the minimap in the script editor (in pixels).
booltext_editor/appearance/minimap/show_minimap🔗
Iftrue, draws an overview of the script near the scroll bar. The minimap can be left-clicked to scroll directly to a location in an "absolute" manner.
booltext_editor/appearance/whitespace/draw_spaces🔗
Iftrue, draws space characters as centered points.
booltext_editor/appearance/whitespace/draw_tabs🔗
Iftrue, draws tab characters as chevrons.
inttext_editor/appearance/whitespace/line_spacing🔗
The space to add between lines (in pixels). Greater line spacing can help improve readability at the cost of displaying fewer lines on screen.
booltext_editor/behavior/documentation/enable_tooltips🔗
Iftrue, documentation tooltips will appear when hovering over a symbol.
booltext_editor/behavior/files/auto_reload_and_parse_scripts_on_save🔗
Iftrue, tool scripts will be automatically soft-reloaded after they are saved.
booltext_editor/behavior/files/auto_reload_scripts_on_external_change🔗
Iftrue, automatically reloads scripts and text-based shaders in the editor when they have been modified and saved by external editors or tools and the editor regains focus. External changes can be discarded by using the Undo function after they've been loaded in the editor.
Iffalse, a file conflict dialog will always be displayed when the editor regains focus. This dialog allows you to choose whether to keep local changes or discard them.
Note:Even when this setting istrue, a file conflict dialog is still displayed in certain situations. For instance, it will display when the script editor has unsaved changes that the external editor did not account for.
inttext_editor/behavior/files/autosave_interval_secs🔗
If set to a value greater than0, automatically saves the current script following the specified interval (in seconds). This can be used to prevent data loss if the editor crashes.
booltext_editor/behavior/files/convert_indent_on_save🔗
Iftrue, converts indentation to match the script editor's indentation settings when saving a script. See alsotext_editor/behavior/indent/type.
booltext_editor/behavior/files/drop_preload_resources_as_uid🔗
Iftrue, when dropping aResourcefile to script editor whileCtrlis held, the resource will be preloaded with a UID. Iffalse, the resource will be preloaded with a path.
When you holdCtrl+Shift, the behavior is reversed.
booltext_editor/behavior/files/open_dominant_script_on_scene_change🔗
Iftrue, opening a scene automatically opens the script attached to the root node, or the topmost node if the root has no script.
booltext_editor/behavior/files/restore_scripts_on_load🔗
Iftrue, reopens scripts that were opened in the last session when the editor is reopened on a given project.
booltext_editor/behavior/files/trim_final_newlines_on_save🔗
Iftrue, trims all empty newlines after the final newline when saving a script. Final newlines refer to the empty newlines found at the end of files. Since these serve no practical purpose, they can and should be removed to make version control diffs less noisy.
booltext_editor/behavior/files/trim_trailing_whitespace_on_save🔗
Iftrue, trims trailing whitespace when saving a script. Trailing whitespace refers to tab and space characters placed at the end of lines. Since these serve no practical purpose, they can and should be removed to make version control diffs less noisy.
booltext_editor/behavior/general/empty_selection_clipboard🔗
Iftrue, copying or cutting without a selection is performed on all lines with a caret. Otherwise, copy and cut require a selection.
booltext_editor/behavior/indent/auto_indent🔗
Iftrue, automatically indents code when pressing theEnterkey based on blocks above the new line.
booltext_editor/behavior/indent/indent_wrapped_lines🔗
Iftrue, all wrapped lines are indented to the same amount as the unwrapped line.
inttext_editor/behavior/indent/size🔗
When using tab indentation, determines the length of each tab. When using space indentation, determines how many spaces are inserted when pressingTaband when automatic indentation is performed.
inttext_editor/behavior/indent/type🔗
The indentation style to use (tabs or spaces).
Note:TheGDScript style guiderecommends using tabs for indentation. It is advised to change this setting only if you need to work on a project that currently uses spaces for indentation.
Stringtext_editor/behavior/navigation/custom_word_separators🔗
The characters to consider as word delimiters iftext_editor/behavior/navigation/use_custom_word_separatorsistrue. This is in addition to default characters iftext_editor/behavior/navigation/use_default_word_separatorsistrue. The characters should be defined without separation, for example_♥=.
booltext_editor/behavior/navigation/drag_and_drop_selection🔗
Iftrue, allows drag-and-dropping text in the script editor to move text. Disable this if you find yourself accidentally drag-and-dropping text in the script editor.
booltext_editor/behavior/navigation/move_caret_on_right_click🔗
Iftrue, the caret will be moved when right-clicking somewhere in the script editor (like when left-clicking or middle-clicking). Iffalse, the caret will only be moved when left-clicking or middle-clicking somewhere.
booltext_editor/behavior/navigation/open_script_when_connecting_signal_to_existing_method🔗
Iftrue, opens the script editor when connecting a signal to an existing script method from the Signals dock.
booltext_editor/behavior/navigation/scroll_past_end_of_file🔗
Iftrue, allows scrolling past the end of the file.
booltext_editor/behavior/navigation/smooth_scrolling🔗
Iftrue, enables a smooth scrolling animation when using the mouse wheel to scroll. Seetext_editor/behavior/navigation/v_scroll_speedfor the speed of this animation.
Note:text_editor/behavior/navigation/smooth_scrollingcurrently behaves poorly in projects whereProjectSettings.physics/common/physics_ticks_per_secondhas been increased significantly from its default value (60). In this case, it is recommended to disable this setting.
booltext_editor/behavior/navigation/stay_in_script_editor_on_node_selected🔗
Iftrue, prevents automatically switching between the Script and 2D/3D screens when selecting a node in the Scene tree dock.
booltext_editor/behavior/navigation/use_custom_word_separators🔗
Iftrue, uses the characters intext_editor/behavior/navigation/custom_word_separatorsas word separators for word navigation and operations. This is in addition to the default characters iftext_editor/behavior/navigation/use_default_word_separatorsis also enabled. Word navigation and operations include double-clicking on a word or holdingCtrl(Cmdon macOS) while pressingleft,right,backspace, ordelete.
booltext_editor/behavior/navigation/use_default_word_separators🔗
Iftrue, uses the characters in`!"#$%&'()*+,-./:;<=>?@[\]^`{|}~, the Unicode General Punctuation table, and the Unicode CJK Punctuation table as word separators for word navigation and operations. Iffalse, a subset of these characters are used and does not include the characters<>$~^=+|. This is in addition to custom characters iftext_editor/behavior/navigation/use_custom_word_separatorsis also enabled. These characters are used to determine where a word stops. Word navigation and operations include double-clicking on a word or holdingCtrl(Cmdon macOS) while pressingleft,right,backspace, ordelete.
inttext_editor/behavior/navigation/v_scroll_speed🔗
The speed of scrolling in lines per second whentext_editor/behavior/navigation/smooth_scrollingistrue. Higher values make the script scroll by faster when using the mouse wheel.
Note:You can hold downAltwhile using the mouse wheel to temporarily scroll 5 times faster.
booltext_editor/completion/add_node_path_literals🔗
Iftrue, usesNodePathinstead ofStringwhen appropriate for code autocompletion or for drag and dropping object properties into the script editor.
booltext_editor/completion/add_string_name_literals🔗
Iftrue, usesStringNameinstead ofStringwhen appropriate for code autocompletion.
booltext_editor/completion/add_type_hints🔗
Iftrue, automatically addsGDScript static typing(such as->voidand:int) in many situations where it's possible to, including when:
- Accepting a suggestion from code autocompletion;
Accepting a suggestion from code autocompletion;
- Creating a new script from a template;
Creating a new script from a template;
- Connecting signals from the Signals dock;
Connecting signals from the Signals dock;
- Creating variables prefixed with@GDScript.@onready, by dropping nodes from the Scene dock into the script editor while holdingCtrl.
Creating variables prefixed with@GDScript.@onready, by dropping nodes from the Scene dock into the script editor while holdingCtrl.
booltext_editor/completion/auto_brace_complete🔗
Iftrue, automatically inserts the matching closing brace when the opening brace is inserted by typing or autocompletion. Also automatically removes the closing brace when pressingBackspaceon the opening brace. This includes brackets ((),[],{}), string quotation marks ('',""), and comments (/**/) if the language supports it.
floattext_editor/completion/code_complete_delay🔗
The delay in seconds after which autocompletion suggestions should be displayed when the user stops typing.
booltext_editor/completion/code_complete_enabled🔗
Iftrue, code completion will be triggered automatically aftertext_editor/completion/code_complete_delay. Even iffalse, code completion can be triggered manually with theui_text_completion_queryaction (by defaultCtrl+SpaceorCmd+Spaceon macOS).
booltext_editor/completion/colorize_suggestions🔗
Iftrueenables the coloring for some items in the autocompletion suggestions, like vector components.
booltext_editor/completion/complete_file_paths🔗
Iftrue, provides autocompletion suggestions for file paths in methods such asload()andpreload().
floattext_editor/completion/idle_parse_delay🔗
The delay in seconds after which the script editor should check for errors when the user stops typing.
floattext_editor/completion/idle_parse_delay_with_errors_found🔗
The delay used instead oftext_editor/completion/idle_parse_delay, when the parser has found errors. A lower value should feel more responsive while fixing code, but may cause notable stuttering and increase CPU usage.
booltext_editor/completion/put_callhint_tooltip_below_current_line🔗
Iftrue, the code completion tooltip will appear below the current line unless there is no space on screen below the current line. Iffalse, the code completion tooltip will appear above the current line.
booltext_editor/completion/use_single_quotes🔗
Iftrue, performs string autocompletion with single quotes. Iffalse, performs string autocompletion with double quotes (which matches theGDScript style guide).
Stringtext_editor/external/exec_flags🔗
The command-line arguments to pass to the external text editor that is run whentext_editor/external/use_external_editoristrue. See alsotext_editor/external/exec_path.
Stringtext_editor/external/exec_path🔗
The path to the text editor executable used to edit text files iftext_editor/external/use_external_editoristrue.
booltext_editor/external/use_external_editor🔗
Iftrue, uses an external editor instead of the built-in Script Editor. See alsotext_editor/external/exec_pathandtext_editor/external/exec_flags.
inttext_editor/help/class_reference_examples🔗
Controls which multi-line code blocks should be displayed in the editor help. This setting does not affect single-line code literals in the editor help.
inttext_editor/help/help_font_size🔗
The font size to use for the editor help (built-in class reference).
inttext_editor/help/help_source_font_size🔗
The font size to use for code samples in the editor help (built-in class reference).
inttext_editor/help/help_title_font_size🔗
The font size to use for headings in the editor help (built-in class reference).
booltext_editor/help/show_help_index🔗
Iftrue, displays a table of contents at the left of the editor help (at the location where the members overview would appear when editing a script).
booltext_editor/help/sort_functions_alphabetically🔗
Iftrue, the script's method list in the Script Editor is sorted alphabetically.
booltext_editor/script_list/group_help_pages🔗
Iftrue, class reference pages are grouped together at the bottom of the Script Editor's script list.
booltext_editor/script_list/highlight_scene_scripts🔗
Iftrue, the scripts that are used by the current scene are highlighted in the Script Editor's script list.
inttext_editor/script_list/list_script_names_as🔗
Specifies how script paths should be displayed in Script Editor's script list. If using the "Name" option and some scripts share the same file name, more parts of their paths are revealed to avoid conflicts.
booltext_editor/script_list/script_temperature_enabled🔗
Iftrue, the names of recently opened scripts in the Script Editor are highlighted with the accent color, with its intensity based on how recently they were opened.
inttext_editor/script_list/script_temperature_history_size🔗
How many script names can be highlighted at most, iftext_editor/script_list/script_temperature_enabledistrue. Scripts older than this value use the default font color.
booltext_editor/script_list/show_members_overview🔗
Iftrue, displays an overview of the current script's member functions at the left of the script editor. See alsotext_editor/script_list/sort_members_outline_alphabetically.
booltext_editor/script_list/sort_members_outline_alphabetically🔗
Iftrue, sorts the members outline (located at the left of the script editor) using alphabetical order. Iffalse, sorts the members outline depending on the order in which members are found in the script.
Note:Only effective iftext_editor/script_list/show_members_overviewistrue.
inttext_editor/script_list/sort_scripts_by🔗
Specifies sorting used for Script Editor's open script list.
Stringtext_editor/theme/color_theme🔗
The syntax theme to use in the script editor.
You can save your own syntax theme from your current settings by usingFile > Theme > Save As...at the top of the script editor. The syntax theme will then be available locally in the list of color themes.
You can find additional syntax themes to install in thegodot-syntax-themesrepository.
Colortext_editor/theme/highlighting/background_color🔗
The script editor's background color. If set to a translucent color, the editor theme's base color will be visible behind.
Colortext_editor/theme/highlighting/base_type_color🔗
The script editor's base type color (used for types likeVector2,Vector3,Color, ...).
Colortext_editor/theme/highlighting/bookmark_color🔗
The script editor's bookmark icon color (displayed in the gutter).
Colortext_editor/theme/highlighting/brace_mismatch_color🔗
The script editor's brace mismatch color. Used when the caret is currently on a mismatched brace, parenthesis or bracket character.
Colortext_editor/theme/highlighting/breakpoint_color🔗
The script editor's breakpoint icon color (displayed in the gutter).
Colortext_editor/theme/highlighting/caret_background_color🔗
The script editor's caret background color.
Note:This setting has no effect as it's currently unused.
Colortext_editor/theme/highlighting/caret_color🔗
The script editor's caret color.
Colortext_editor/theme/highlighting/code_folding_color🔗
The script editor's color for the code folding icon (displayed in the gutter).
Colortext_editor/theme/highlighting/comment_color🔗
The script editor's comment color.
Note:In GDScript, unlike Python, multiline strings are not considered to be comments, and will use the string highlighting color instead.
Colortext_editor/theme/highlighting/comment_markers/critical_color🔗
The script editor's critical comment marker text color. These markers are determined bytext_editor/theme/highlighting/comment_markers/critical_list.
Stringtext_editor/theme/highlighting/comment_markers/critical_list🔗
A comma-separated list of case-sensitive words to highlight in comments. The text will be highlighted in the script editor with thetext_editor/theme/highlighting/comment_markers/critical_colorcolor. These must not include spaces or symbols or they will not be highlighted.
Note:This is only implemented in the GDScript syntax highlighter.
Colortext_editor/theme/highlighting/comment_markers/notice_color🔗
The script editor's notice comment marker text color. These markers are determined bytext_editor/theme/highlighting/comment_markers/notice_list.
Stringtext_editor/theme/highlighting/comment_markers/notice_list🔗
A comma-separated list of case-sensitive words to highlight in comments. The text will be highlighted in the script editor with thetext_editor/theme/highlighting/comment_markers/notice_colorcolor. These must not include spaces or symbols or they will not be highlighted.
Note:This is only implemented in the GDScript syntax highlighter.
Colortext_editor/theme/highlighting/comment_markers/warning_color🔗
The script editor's warning comment marker text color. These markers are determined bytext_editor/theme/highlighting/comment_markers/warning_list.
Stringtext_editor/theme/highlighting/comment_markers/warning_list🔗
A comma-separated list of case-sensitive words to highlight in comments. The text will be highlighted in the script editor with thetext_editor/theme/highlighting/comment_markers/warning_colorcolor. These must not include spaces or symbols or they will not be highlighted.
Note:This is only implemented in the GDScript syntax highlighter.
Colortext_editor/theme/highlighting/completion_background_color🔗
The script editor's autocompletion box background color.
Colortext_editor/theme/highlighting/completion_existing_color🔗
The script editor's autocompletion box background color to highlight existing characters in the completion results. This should be a translucent color so thattext_editor/theme/highlighting/completion_selected_colorcan be seen behind.
Colortext_editor/theme/highlighting/completion_font_color🔗
The script editor's autocompletion box text color.
Colortext_editor/theme/highlighting/completion_scroll_color🔗
The script editor's autocompletion box scroll bar color.
Colortext_editor/theme/highlighting/completion_scroll_hovered_color🔗
The script editor's autocompletion box scroll bar color when hovered or pressed with the mouse.
Colortext_editor/theme/highlighting/completion_selected_color🔗
The script editor's autocompletion box background color for the currently selected line.
Colortext_editor/theme/highlighting/control_flow_keyword_color🔗
The script editor's control flow keyword color (used for keywords likeif,for,return, ...).
Colortext_editor/theme/highlighting/current_line_color🔗
The script editor's background color for the line the caret is currently on. This should be set to a translucent color so that it can display on top of other line color modifiers such astext_editor/theme/highlighting/mark_color.
Colortext_editor/theme/highlighting/doc_comment_color🔗
The script editor's documentation comment color. In GDScript, this is used for comments starting with##. In C#, this is used for comments starting with///or/**.
Colortext_editor/theme/highlighting/engine_type_color🔗
The script editor's engine type color (Object,Mesh,Node, ...).
Colortext_editor/theme/highlighting/executing_line_color🔗
The script editor's color for the debugger's executing line icon (displayed in the gutter).
Colortext_editor/theme/highlighting/folded_code_region_color🔗
The script editor's background line highlighting color for folded code region.
Colortext_editor/theme/highlighting/function_color🔗
The script editor's function call color.
Note:When using the GDScript syntax highlighter, this is only used when calling some functions since function definitions and global functions have their own colorstext_editor/theme/highlighting/gdscript/function_definition_colorandtext_editor/theme/highlighting/gdscript/global_function_color.
Colortext_editor/theme/highlighting/gdscript/annotation_color🔗
The GDScript syntax highlighter text color for annotations (e.g.@export).
Colortext_editor/theme/highlighting/gdscript/function_definition_color🔗
The GDScript syntax highlighter text color for function definitions (e.g. the_readyinfunc_ready():).
Colortext_editor/theme/highlighting/gdscript/global_function_color🔗
The GDScript syntax highlighter text color for global functions, such as the ones in@GlobalScope(e.g.preload()).
Colortext_editor/theme/highlighting/gdscript/node_path_color🔗
The GDScript syntax highlighter text color forNodePathliterals (e.g.^"position:x").
Colortext_editor/theme/highlighting/gdscript/node_reference_color🔗
The GDScript syntax highlighter text color for node reference literals (e.g.$"Sprite"and%"Sprite"]).
Colortext_editor/theme/highlighting/gdscript/string_name_color🔗
The GDScript syntax highlighter text color forStringNameliterals (e.g.&"example").
Colortext_editor/theme/highlighting/keyword_color🔗
The script editor's non-control flow keyword color (used for keywords likevar,func,extends, ...).
Colortext_editor/theme/highlighting/line_length_guideline_color🔗
The script editor's color for the line length guideline. The "hard" line length guideline will be drawn with this color, whereas the "soft" line length guideline will be drawn with half of its opacity.
Colortext_editor/theme/highlighting/line_number_color🔗
The script editor's color for line numbers. See alsotext_editor/theme/highlighting/safe_line_number_color.
Colortext_editor/theme/highlighting/mark_color🔗
The script editor's background color for lines with errors. This should be set to a translucent color so that it can display on top of other line color modifiers such astext_editor/theme/highlighting/current_line_color.
Colortext_editor/theme/highlighting/member_variable_color🔗
The script editor's color for member variables on objects (e.g.self.some_property).
Note:This color is not used for local variable declaration and access.
Colortext_editor/theme/highlighting/number_color🔗
The script editor's color for numbers (integer and floating-point).
Colortext_editor/theme/highlighting/safe_line_number_color🔗
The script editor's color for type-safe line numbers. See alsotext_editor/theme/highlighting/line_number_color.
Note:Only displayed iftext_editor/appearance/gutters/highlight_type_safe_linesistrue.
Colortext_editor/theme/highlighting/search_result_border_color🔗
The script editor's color for the border of search results. This border helps bring further attention to the search result. Set this color's opacity to 0 to disable the border.
Colortext_editor/theme/highlighting/search_result_color🔗
The script editor's background color for search results.
Colortext_editor/theme/highlighting/selection_color🔗
The script editor's background color for the currently selected text.
Colortext_editor/theme/highlighting/string_color🔗
The script editor's color for strings (single-line and multi-line).
Colortext_editor/theme/highlighting/string_placeholder_color🔗
The script editor's color for string placeholders, such as%sand{_}. Refer to theGDScript format strings documentationfor more details.
Note:Only the default{_}placeholder patterns are highlighted for theString.format()method. Custom patterns still appear as plain strings.
Colortext_editor/theme/highlighting/symbol_color🔗
The script editor's color for operators (()[]{}+-*/, ...).
Colortext_editor/theme/highlighting/text_color🔗
The script editor's color for text not highlighted by any syntax highlighting rule.
Colortext_editor/theme/highlighting/text_selected_color🔗
The script editor's background color for text. This should be set to a translucent color so that it can display on top of other line color modifiers such astext_editor/theme/highlighting/current_line_color.
Colortext_editor/theme/highlighting/user_type_color🔗
The script editor's color for user-defined types (usingclass_name).
Colortext_editor/theme/highlighting/warning_color🔗
The script editor's background color for lines with warnings. This should be set to a translucent color so that it can display on top of other line color modifiers such astext_editor/theme/highlighting/current_line_color.
Colortext_editor/theme/highlighting/word_highlighted_color🔗
The script editor's color for words highlighted by selecting them. Only visible iftext_editor/appearance/caret/highlight_all_occurrencesistrue.
Stringversion_control/ssh_private_key_path🔗
Path to private SSH key file for the editor's Version Control integration credentials.
Stringversion_control/ssh_public_key_path🔗
Path to public SSH key file for the editor's Version Control integration credentials.
Stringversion_control/username🔗
Default username for editor's Version Control integration.

## Method Descriptions
voidadd_property_info(info:Dictionary)🔗
Adds a custom property info to a property. The dictionary must contain:
- name:String(the name of the property)
name:String(the name of the property)
- type:int(seeVariant.Type)
type:int(seeVariant.Type)
- optionallyhint:int(seePropertyHint) andhint_string:String
optionallyhint:int(seePropertyHint) andhint_string:String
```
var settings = EditorInterface.get_editor_settings()
settings.set("category/property_name", 0)

var property_info = {
    "name": "category/property_name",
    "type": TYPE_INT,
    "hint": PROPERTY_HINT_ENUM,
    "hint_string": "one,two,three"
}

settings.add_property_info(property_info)
```
```
var settings = GetEditorInterface().GetEditorSettings();
settings.Set("category/property_name", 0);

var propertyInfo = new Godot.Collections.Dictionary
{
    { "name", "category/propertyName" },
    { "type", Variant.Type.Int },
    { "hint", PropertyHint.Enum },
    { "hint_string", "one,two,three" },
};

settings.AddPropertyInfo(propertyInfo);
```
voidadd_shortcut(path:String, shortcut:Shortcut)🔗
Adds ashortcutwhose path is specified bypath.
Thepathdetermines how the shortcut is organized and displayed in the editor's shortcut settings. The path format affects the display as follows:
- "name"(no slash): Creates a category namednamewith the shortcut displayed asname.
"name"(no slash): Creates a category namednamewith the shortcut displayed asname.
- "category/name"(single slash): Displays asnamein thecategorysection.
"category/name"(single slash): Displays asnamein thecategorysection.
- "category/name/extra"(multiple slashes): Extra path components are ignored, so this behaves the same as"category/name".
"category/name/extra"(multiple slashes): Extra path components are ignored, so this behaves the same as"category/name".
Note:Shortcuts are only saved to the editor settings if they differ from their original/default state. This means empty shortcuts that were originally empty will not persist between editor sessions and must be re-added. If a shortcut with the samepathalready exists, this method will update it with the newshortcutinstead of creating a duplicate.
```
# Add a custom shortcut for a plugin action.
var my_shortcut = Shortcut.new()
var input_event = InputEventKey.new()
input_event.keycode = KEY_F5
input_event.ctrl_pressed = true
my_shortcut.events.append(input_event)

# This will appear under the "My Plugin" category as "Reload Data".
EditorInterface.get_editor_settings().add_shortcut("my_plugin/reload_data", my_shortcut)

# This will appear under the "Test Action" category as "Test Action".
EditorInterface.get_editor_settings().add_shortcut("test_action", my_shortcut)
```
boolcheck_changed_settings_in_group(setting_prefix:String)const🔗
Checks if any settings with the prefixsetting_prefixexist in the set of changed settings. See alsoget_changed_settings().
voiderase(property:String)🔗
Erases the setting whose name is specified byproperty.
PackedStringArrayget_changed_settings()const🔗
Gets an array of the settings which have been changed since the last save. Note that internallychanged_settingsis cleared after a successful save, so generally the most appropriate place to use this method is when processingNOTIFICATION_EDITOR_SETTINGS_CHANGED.
PackedStringArrayget_favorites()const🔗
Returns the list of favorite files and directories for this project.
Variantget_project_metadata(section:String, key:String, default:Variant= null)const🔗
Returns project-specific metadata for thesectionandkeyspecified. If the metadata doesn't exist,defaultwill be returned instead. See alsoset_project_metadata().
PackedStringArrayget_recent_dirs()const🔗
Returns the list of recently visited folders in the file dialog for this project.
Variantget_setting(name:String)const🔗
Returns the value of the setting specified byname. This is equivalent to usingObject.get()on the EditorSettings instance.
Shortcutget_shortcut(path:String)const🔗
Returns the shortcut specified bypath. Tries to find a built-in action if no shortcut with the provided path is found in the shortcut list. If found, adds it to the list and returns it, otherwise returnsnull.
PackedStringArrayget_shortcut_list()🔗
Returns the list of stored shortcut paths.
boolhas_setting(name:String)const🔗
Returnstrueif the setting specified bynameexists,falseotherwise.
boolhas_shortcut(path:String)const🔗
Returnstrueif the shortcut specified bypathexists,falseotherwise.
boolis_shortcut(path:String, event:InputEvent)const🔗
Returnstrueif the shortcut specified bypathmatches the event specified byevent,falseotherwise.
voidmark_setting_changed(setting:String)🔗
Marks the passed editor setting as being changed, seeget_changed_settings(). Only settings which exist (seehas_setting()) will be accepted.
voidremove_shortcut(path:String)🔗
Removes the shortcut specified bypath.
voidset_builtin_action_override(name:String, actions_list:Array[InputEvent])🔗
Overrides the built-in editor actionnamewith the input actions defined inactions_list.
voidset_favorites(dirs:PackedStringArray)🔗
Sets the list of favorite files and directories for this project.
voidset_initial_value(name:StringName, value:Variant, update_current:bool)🔗
Sets the initial value of the setting specified bynametovalue. This is used to provide a value for the Revert button in the Editor Settings. Ifupdate_currentistrue, the setting is reset tovalueas well.
voidset_project_metadata(section:String, key:String, data:Variant)🔗
Sets project-specific metadata with thesection,keyanddataspecified. This metadata is stored outside the project folder and therefore won't be checked into version control. See alsoget_project_metadata().
voidset_recent_dirs(dirs:PackedStringArray)🔗
Sets the list of recently visited folders in the file dialog for this project.
voidset_setting(name:String, value:Variant)🔗
Sets thevalueof the setting specified byname. This is equivalent to usingObject.set()on the EditorSettings instance.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.