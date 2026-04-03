# ProjectSettings in English

# ProjectSettings

Inherits:Object
Stores globally-accessible variables.

## Description

Stores variables that can be accessed from everywhere. Useget_setting(),set_setting()orhas_setting()to access them. Variables stored inproject.godotare also loaded intoProjectSettings, making this object very useful for reading custom game configuration options.
When naming a Project Settings property, use the full path to the setting including the category. For example,"application/config/name"for the project name. Category and property names can be viewed in the Project Settings dialog.
Feature tags:Project settings can be overridden for specific platforms and configurations (debug, release, ...) usingfeature tags.
Overriding:Any project setting can be overridden by creating a file namedoverride.cfgin the project's root directory. This can also be used in exported projects by placing this file in the same directory as the project binary. Overriding will still take the base project settings'feature tagsin account. Therefore, make sure toalsooverride the setting with the desired feature tags if you want them to override base project settings on all platforms and configurations.

## Tutorials

- Project Settings
Project Settings
- 3D Physics Tests Demo
3D Physics Tests Demo
- 3D Platformer Demo
3D Platformer Demo
- Operating System Testing Demo
Operating System Testing Demo

## Properties

| int | accessibility/general/accessibility_support | 0 |
|---|---|---|
| int | accessibility/general/updates_per_second | 60 |
| bool | animation/compatibility/default_parent_skeleton_in_mesh_instance_3d | false |
| bool | animation/warnings/check_angle_interpolation_type_conflicting | true |
| bool | animation/warnings/check_invalid_track_paths | true |
| Color | application/boot_splash/bg_color | Color(0.14,0.14,0.14,1) |
| String | application/boot_splash/image | "" |
| int | application/boot_splash/minimum_display_time | 0 |
| bool | application/boot_splash/show_image | true |
| int | application/boot_splash/stretch_mode | 1 |
| bool | application/boot_splash/use_filter | true |
| bool | application/config/auto_accept_quit | true |
| String | application/config/custom_user_dir_name | "" |
| String | application/config/description | "" |
| bool | application/config/disable_project_settings_override | false |
| String | application/config/icon | "" |
| String | application/config/macos_native_icon | "" |
| String | application/config/name | "" |
| Dictionary | application/config/name_localized | {} |
| String | application/config/project_settings_override | "" |
| bool | application/config/quit_on_go_back | true |
| bool | application/config/use_custom_user_dir | false |
| bool | application/config/use_hidden_project_data_directory | true |
| String | application/config/version | "" |
| String | application/config/windows_native_icon | "" |
| bool | application/run/delta_smoothing | true |
| bool | application/run/disable_stderr | false |
| bool | application/run/disable_stdout | false |
| bool | application/run/enable_alt_space_menu | false |
| bool | application/run/flush_stdout_on_print | false |
| bool | application/run/flush_stdout_on_print.debug | true |
| int | application/run/frame_delay_msec | 0 |
| bool | application/run/load_shell_environment | false |
| bool | application/run/low_processor_mode | false |
| int | application/run/low_processor_mode_sleep_usec | 6900 |
| String | application/run/main_loop_type | "SceneTree" |
| String | application/run/main_scene | "" |
| int | application/run/max_fps | 0 |
| bool | application/run/print_header | true |
| float | audio/buses/channel_disable_threshold_db | -60.0 |
| float | audio/buses/channel_disable_time | 2.0 |
| String | audio/buses/default_bus_layout | "res://default_bus_layout.tres" |
| String | audio/driver/driver |  |
| bool | audio/driver/enable_input | false |
| int | audio/driver/mix_rate | 44100 |
| int | audio/driver/mix_rate.web | 0 |
| int | audio/driver/output_latency | 15 |
| int | audio/driver/output_latency.web | 50 |
| float | audio/general/2d_panning_strength | 0.5 |
| float | audio/general/3d_panning_strength | 0.5 |
| int | audio/general/default_playback_type | 0 |
| int | audio/general/default_playback_type.web | 1 |
| bool | audio/general/ios/mix_with_others | false |
| int | audio/general/ios/session_category | 0 |
| bool | audio/general/text_to_speech | false |
| int | audio/video/video_delay_compensation_ms | 0 |
| bool | collada/use_ambient | false |
| int | compression/formats/gzip/compression_level | -1 |
| int | compression/formats/zlib/compression_level | -1 |
| int | compression/formats/zstd/compression_level | 3 |
| bool | compression/formats/zstd/long_distance_matching | false |
| int | compression/formats/zstd/window_log_size | 27 |
| Color | debug/canvas_items/debug_redraw_color | Color(1,0.2,0.2,0.5) |
| float | debug/canvas_items/debug_redraw_time | 1.0 |
| bool | debug/file_logging/enable_file_logging | false |
| bool | debug/file_logging/enable_file_logging.pc | true |
| String | debug/file_logging/log_path | "user://logs/godot.log" |
| int | debug/file_logging/max_log_files | 5 |
| int | debug/gdscript/warnings/assert_always_false | 1 |
| int | debug/gdscript/warnings/assert_always_true | 1 |
| int | debug/gdscript/warnings/confusable_capture_reassignment | 1 |
| int | debug/gdscript/warnings/confusable_identifier | 1 |
| int | debug/gdscript/warnings/confusable_local_declaration | 1 |
| int | debug/gdscript/warnings/confusable_local_usage | 1 |
| int | debug/gdscript/warnings/deprecated_keyword | 1 |
| Dictionary | debug/gdscript/warnings/directory_rules | {"res://addons":0} |
| int | debug/gdscript/warnings/empty_file | 1 |
| bool | debug/gdscript/warnings/enable | true |
| int | debug/gdscript/warnings/enum_variable_without_default | 1 |
| int | debug/gdscript/warnings/get_node_default_without_onready | 2 |
| int | debug/gdscript/warnings/incompatible_ternary | 1 |
| int | debug/gdscript/warnings/inference_on_variant | 2 |
| int | debug/gdscript/warnings/inferred_declaration | 0 |
| int | debug/gdscript/warnings/int_as_enum_without_cast | 1 |
| int | debug/gdscript/warnings/int_as_enum_without_match | 1 |
| int | debug/gdscript/warnings/integer_division | 1 |
| int | debug/gdscript/warnings/missing_await | 0 |
| int | debug/gdscript/warnings/missing_tool | 1 |
| int | debug/gdscript/warnings/narrowing_conversion | 1 |
| int | debug/gdscript/warnings/native_method_override | 2 |
| int | debug/gdscript/warnings/onready_with_export | 2 |
| int | debug/gdscript/warnings/redundant_await | 1 |
| int | debug/gdscript/warnings/redundant_static_unload | 1 |
| bool | debug/gdscript/warnings/renamed_in_godot_4_hint | true |
| int | debug/gdscript/warnings/return_value_discarded | 0 |
| int | debug/gdscript/warnings/shadowed_global_identifier | 1 |
| int | debug/gdscript/warnings/shadowed_variable | 1 |
| int | debug/gdscript/warnings/shadowed_variable_base_class | 1 |
| int | debug/gdscript/warnings/standalone_expression | 1 |
| int | debug/gdscript/warnings/standalone_ternary | 1 |
| int | debug/gdscript/warnings/static_called_on_instance | 1 |
| int | debug/gdscript/warnings/unassigned_variable | 1 |
| int | debug/gdscript/warnings/unassigned_variable_op_assign | 1 |
| int | debug/gdscript/warnings/unreachable_code | 1 |
| int | debug/gdscript/warnings/unreachable_pattern | 1 |
| int | debug/gdscript/warnings/unsafe_call_argument | 0 |
| int | debug/gdscript/warnings/unsafe_cast | 0 |
| int | debug/gdscript/warnings/unsafe_method_access | 0 |
| int | debug/gdscript/warnings/unsafe_property_access | 0 |
| int | debug/gdscript/warnings/unsafe_void_return | 1 |
| int | debug/gdscript/warnings/untyped_declaration | 0 |
| int | debug/gdscript/warnings/unused_local_constant | 1 |
| int | debug/gdscript/warnings/unused_parameter | 1 |
| int | debug/gdscript/warnings/unused_private_class_variable | 1 |
| int | debug/gdscript/warnings/unused_signal | 1 |
| int | debug/gdscript/warnings/unused_variable | 1 |
| String | debug/settings/crash_handler/message | "Pleaseincludethiswhenreportingthebugtotheprojectdeveloper." |
| String | debug/settings/crash_handler/message.editor | "Pleaseincludethiswhenreportingthebugon:https://github.com/godotengine/godot/issues" |
| bool | debug/settings/gdscript/always_track_call_stacks | false |
| bool | debug/settings/gdscript/always_track_local_variables | false |
| int | debug/settings/gdscript/max_call_stack | 1024 |
| bool | debug/settings/physics_interpolation/enable_warnings | true |
| int | debug/settings/profiler/max_functions | 16384 |
| int | debug/settings/profiler/max_timestamp_query_elements | 256 |
| bool | debug/settings/stdout/print_fps | false |
| bool | debug/settings/stdout/print_gpu_profile | false |
| bool | debug/settings/stdout/verbose_stdout | false |
| bool | debug/shader_language/warnings/device_limit_exceeded | true |
| bool | debug/shader_language/warnings/enable | true |
| bool | debug/shader_language/warnings/float_comparison | true |
| bool | debug/shader_language/warnings/formatting_error | true |
| bool | debug/shader_language/warnings/magic_position_write | true |
| bool | debug/shader_language/warnings/treat_warnings_as_errors | false |
| bool | debug/shader_language/warnings/unused_constant | true |
| bool | debug/shader_language/warnings/unused_function | true |
| bool | debug/shader_language/warnings/unused_local_variable | true |
| bool | debug/shader_language/warnings/unused_struct | true |
| bool | debug/shader_language/warnings/unused_uniform | true |
| bool | debug/shader_language/warnings/unused_varying | true |
| Color | debug/shapes/avoidance/2d/agents_radius_color | Color(1,1,0,0.25) |
| bool | debug/shapes/avoidance/2d/enable_agents_radius | true |
| bool | debug/shapes/avoidance/2d/enable_obstacles_radius | true |
| bool | debug/shapes/avoidance/2d/enable_obstacles_static | true |
| Color | debug/shapes/avoidance/2d/obstacles_radius_color | Color(1,0.5,0,0.25) |
| Color | debug/shapes/avoidance/2d/obstacles_static_edge_pushin_color | Color(1,0,0,1) |
| Color | debug/shapes/avoidance/2d/obstacles_static_edge_pushout_color | Color(1,1,0,1) |
| Color | debug/shapes/avoidance/2d/obstacles_static_face_pushin_color | Color(1,0,0,0) |
| Color | debug/shapes/avoidance/2d/obstacles_static_face_pushout_color | Color(1,1,0,0.5) |
| Color | debug/shapes/avoidance/3d/agents_radius_color | Color(1,1,0,0.25) |
| bool | debug/shapes/avoidance/3d/enable_agents_radius | true |
| bool | debug/shapes/avoidance/3d/enable_obstacles_radius | true |
| bool | debug/shapes/avoidance/3d/enable_obstacles_static | true |
| Color | debug/shapes/avoidance/3d/obstacles_radius_color | Color(1,0.5,0,0.25) |
| Color | debug/shapes/avoidance/3d/obstacles_static_edge_pushin_color | Color(1,0,0,1) |
| Color | debug/shapes/avoidance/3d/obstacles_static_edge_pushout_color | Color(1,1,0,1) |
| Color | debug/shapes/avoidance/3d/obstacles_static_face_pushin_color | Color(1,0,0,0) |
| Color | debug/shapes/avoidance/3d/obstacles_static_face_pushout_color | Color(1,1,0,0.5) |
| Color | debug/shapes/collision/contact_color | Color(1,0.2,0.1,0.8) |
| bool | debug/shapes/collision/draw_2d_outlines | true |
| int | debug/shapes/collision/max_contacts_displayed | 10000 |
| Color | debug/shapes/collision/shape_color | Color(0,0.6,0.7,0.42) |
| Color | debug/shapes/navigation/2d/agent_path_color | Color(1,0,0,1) |
| float | debug/shapes/navigation/2d/agent_path_point_size | 4.0 |
| Color | debug/shapes/navigation/2d/edge_connection_color | Color(1,0,1,1) |
| bool | debug/shapes/navigation/2d/enable_agent_paths | true |
| bool | debug/shapes/navigation/2d/enable_edge_connections | true |
| bool | debug/shapes/navigation/2d/enable_edge_lines | true |
| bool | debug/shapes/navigation/2d/enable_geometry_face_random_color | true |
| bool | debug/shapes/navigation/2d/enable_link_connections | true |
| Color | debug/shapes/navigation/2d/geometry_edge_color | Color(0.5,1,1,1) |
| Color | debug/shapes/navigation/2d/geometry_edge_disabled_color | Color(0.5,0.5,0.5,1) |
| Color | debug/shapes/navigation/2d/geometry_face_color | Color(0.5,1,1,0.4) |
| Color | debug/shapes/navigation/2d/geometry_face_disabled_color | Color(0.5,0.5,0.5,0.4) |
| Color | debug/shapes/navigation/2d/link_connection_color | Color(1,0.5,1,1) |
| Color | debug/shapes/navigation/2d/link_connection_disabled_color | Color(0.5,0.5,0.5,1) |
| Color | debug/shapes/navigation/3d/agent_path_color | Color(1,0,0,1) |
| float | debug/shapes/navigation/3d/agent_path_point_size | 4.0 |
| Color | debug/shapes/navigation/3d/edge_connection_color | Color(1,0,1,1) |
| bool | debug/shapes/navigation/3d/enable_agent_paths | true |
| bool | debug/shapes/navigation/3d/enable_agent_paths_xray | true |
| bool | debug/shapes/navigation/3d/enable_edge_connections | true |
| bool | debug/shapes/navigation/3d/enable_edge_connections_xray | true |
| bool | debug/shapes/navigation/3d/enable_edge_lines | true |
| bool | debug/shapes/navigation/3d/enable_edge_lines_xray | true |
| bool | debug/shapes/navigation/3d/enable_geometry_face_random_color | true |
| bool | debug/shapes/navigation/3d/enable_link_connections | true |
| bool | debug/shapes/navigation/3d/enable_link_connections_xray | true |
| Color | debug/shapes/navigation/3d/geometry_edge_color | Color(0.5,1,1,1) |
| Color | debug/shapes/navigation/3d/geometry_edge_disabled_color | Color(0.5,0.5,0.5,1) |
| Color | debug/shapes/navigation/3d/geometry_face_color | Color(0.5,1,1,0.4) |
| Color | debug/shapes/navigation/3d/geometry_face_disabled_color | Color(0.5,0.5,0.5,0.4) |
| Color | debug/shapes/navigation/3d/link_connection_color | Color(1,0.5,1,1) |
| Color | debug/shapes/navigation/3d/link_connection_disabled_color | Color(0.5,0.5,0.5,1) |
| Color | debug/shapes/paths/geometry_color | Color(0.1,1,0.7,0.4) |
| float | debug/shapes/paths/geometry_width | 2.0 |
| String | display/display_server/driver |  |
| String | display/display_server/driver.android |  |
| String | display/display_server/driver.ios |  |
| String | display/display_server/driver.linuxbsd |  |
| String | display/display_server/driver.macos |  |
| String | display/display_server/driver.visionos |  |
| String | display/display_server/driver.windows |  |
| String | display/mouse_cursor/custom_image | "" |
| Vector2 | display/mouse_cursor/custom_image_hotspot | Vector2(0,0) |
| Vector2 | display/mouse_cursor/tooltip_position_offset | Vector2(10,10) |
| bool | display/window/dpi/allow_hidpi | true |
| bool | display/window/energy_saving/keep_screen_on | true |
| bool | display/window/frame_pacing/android/enable_frame_pacing | true |
| int | display/window/frame_pacing/android/swappy_mode | 2 |
| int | display/window/handheld/orientation | 0 |
| bool | display/window/ios/allow_high_refresh_rate | true |
| bool | display/window/ios/hide_home_indicator | true |
| bool | display/window/ios/hide_status_bar | true |
| bool | display/window/ios/suppress_ui_gesture | true |
| bool | display/window/per_pixel_transparency/allowed | false |
| bool | display/window/size/always_on_top | false |
| bool | display/window/size/borderless | false |
| bool | display/window/size/extend_to_title | false |
| Vector2i | display/window/size/initial_position | Vector2i(0,0) |
| int | display/window/size/initial_position_type | 1 |
| int | display/window/size/initial_screen | 0 |
| bool | display/window/size/maximize_disabled | false |
| bool | display/window/size/minimize_disabled | false |
| int | display/window/size/mode | 0 |
| bool | display/window/size/no_focus | false |
| bool | display/window/size/resizable | true |
| bool | display/window/size/sharp_corners | false |
| bool | display/window/size/transparent | false |
| int | display/window/size/viewport_height | 648 |
| int | display/window/size/viewport_width | 1152 |
| int | display/window/size/window_height_override | 0 |
| int | display/window/size/window_width_override | 0 |
| String | display/window/stretch/aspect | "keep" |
| String | display/window/stretch/mode | "disabled" |
| float | display/window/stretch/scale | 1.0 |
| String | display/window/stretch/scale_mode | "fractional" |
| bool | display/window/subwindows/embed_subwindows | true |
| int | display/window/vsync/vsync_mode | 1 |
| String | dotnet/project/assembly_name | "" |
| int | dotnet/project/assembly_reload_attempts | 3 |
| String | dotnet/project/solution_directory | "" |
| bool | editor/export/convert_text_resources_to_binary | true |
| int | editor/import/atlas_max_width | 2048 |
| bool | editor/import/reimport_missing_imported_files | true |
| bool | editor/import/use_multiple_threads | true |
| int | editor/movie_writer/audio_bit_depth | 16 |
| bool | editor/movie_writer/disable_vsync | false |
| int | editor/movie_writer/fps | 60 |
| int | editor/movie_writer/mix_rate | 48000 |
| String | editor/movie_writer/movie_file | "" |
| float | editor/movie_writer/ogv/audio_quality | 0.5 |
| int | editor/movie_writer/ogv/encoding_speed | 4 |
| int | editor/movie_writer/ogv/keyframe_interval | 64 |
| int | editor/movie_writer/speaker_mode | 0 |
| float | editor/movie_writer/video_quality | 0.75 |
| String | editor/naming/default_signal_callback_name | "_on_{node_name}_{signal_name}" |
| String | editor/naming/default_signal_callback_to_self_name | "_on_{signal_name}" |
| int | editor/naming/node_name_casing | 0 |
| int | editor/naming/node_name_num_separator | 0 |
| int | editor/naming/scene_name_casing | 2 |
| int | editor/naming/script_name_casing | 0 |
| String | editor/run/main_run_args | "" |
| PackedStringArray | editor/script/search_in_file_extensions |  |
| String | editor/script/templates_search_path | "res://script_templates" |
| bool | editor/version_control/autoload_on_startup | false |
| String | editor/version_control/plugin_name | "" |
| bool | filesystem/import/blender/enabled | true |
| bool | filesystem/import/blender/enabled.android | false |
| bool | filesystem/import/blender/enabled.web | false |
| bool | filesystem/import/fbx2gltf/enabled | true |
| bool | filesystem/import/fbx2gltf/enabled.android | false |
| bool | filesystem/import/fbx2gltf/enabled.web | false |
| int | gui/common/default_scroll_deadzone | 0 |
| int | gui/common/drag_threshold | 10 |
| int | gui/common/show_focus_state_on_pointer_event | 1 |
| bool | gui/common/snap_controls_to_pixels | true |
| int | gui/common/swap_cancel_ok | 0 |
| int | gui/common/text_edit_undo_stack_max_size | 1024 |
| bool | gui/fonts/dynamic_fonts/use_oversampling | true |
| String | gui/theme/custom | "" |
| String | gui/theme/custom_font | "" |
| int | gui/theme/default_font_antialiasing | 1 |
| bool | gui/theme/default_font_generate_mipmaps | false |
| int | gui/theme/default_font_hinting | 1 |
| bool | gui/theme/default_font_multichannel_signed_distance_field | false |
| int | gui/theme/default_font_subpixel_positioning | 1 |
| float | gui/theme/default_theme_scale | 1.0 |
| int | gui/theme/lcd_subpixel_layout | 1 |
| float | gui/timers/button_shortcut_feedback_highlight_time | 0.2 |
| int | gui/timers/incremental_search_max_interval_msec | 2000 |
| float | gui/timers/text_edit_idle_detect_sec | 3 |
| float | gui/timers/tooltip_delay_sec | 0.5 |
| float | gui/timers/tooltip_delay_sec.editor_hint | 0.5 |
| Dictionary | input/ui_accept |  |
| Dictionary | input/ui_accessibility_drag_and_drop |  |
| Dictionary | input/ui_cancel |  |
| Dictionary | input/ui_close_dialog |  |
| Dictionary | input/ui_close_dialog.macos |  |
| Dictionary | input/ui_colorpicker_delete_preset |  |
| Dictionary | input/ui_copy |  |
| Dictionary | input/ui_cut |  |
| Dictionary | input/ui_down |  |
| Dictionary | input/ui_end |  |
| Dictionary | input/ui_filedialog_delete |  |
| Dictionary | input/ui_filedialog_find |  |
| Dictionary | input/ui_filedialog_focus_path |  |
| Dictionary | input/ui_filedialog_focus_path.macos |  |
| Dictionary | input/ui_filedialog_refresh |  |
| Dictionary | input/ui_filedialog_show_hidden |  |
| Dictionary | input/ui_filedialog_up_one_level |  |
| Dictionary | input/ui_focus_mode |  |
| Dictionary | input/ui_focus_next |  |
| Dictionary | input/ui_focus_prev |  |
| Dictionary | input/ui_graph_delete |  |
| Dictionary | input/ui_graph_duplicate |  |
| Dictionary | input/ui_graph_follow_left |  |
| Dictionary | input/ui_graph_follow_left.macos |  |
| Dictionary | input/ui_graph_follow_right |  |
| Dictionary | input/ui_graph_follow_right.macos |  |
| Dictionary | input/ui_home |  |
| Dictionary | input/ui_left |  |
| Dictionary | input/ui_menu |  |
| Dictionary | input/ui_page_down |  |
| Dictionary | input/ui_page_up |  |
| Dictionary | input/ui_paste |  |
| Dictionary | input/ui_redo |  |
| Dictionary | input/ui_right |  |
| Dictionary | input/ui_select |  |
| Dictionary | input/ui_swap_input_direction |  |
| Dictionary | input/ui_text_add_selection_for_next_occurrence |  |
| Dictionary | input/ui_text_backspace |  |
| Dictionary | input/ui_text_backspace_all_to_left |  |
| Dictionary | input/ui_text_backspace_all_to_left.macos |  |
| Dictionary | input/ui_text_backspace_word |  |
| Dictionary | input/ui_text_backspace_word.macos |  |
| Dictionary | input/ui_text_caret_add_above |  |
| Dictionary | input/ui_text_caret_add_above.macos |  |
| Dictionary | input/ui_text_caret_add_below |  |
| Dictionary | input/ui_text_caret_add_below.macos |  |
| Dictionary | input/ui_text_caret_document_end |  |
| Dictionary | input/ui_text_caret_document_end.macos |  |
| Dictionary | input/ui_text_caret_document_start |  |
| Dictionary | input/ui_text_caret_document_start.macos |  |
| Dictionary | input/ui_text_caret_down |  |
| Dictionary | input/ui_text_caret_left |  |
| Dictionary | input/ui_text_caret_line_end |  |
| Dictionary | input/ui_text_caret_line_end.macos |  |
| Dictionary | input/ui_text_caret_line_start |  |
| Dictionary | input/ui_text_caret_line_start.macos |  |
| Dictionary | input/ui_text_caret_page_down |  |
| Dictionary | input/ui_text_caret_page_up |  |
| Dictionary | input/ui_text_caret_right |  |
| Dictionary | input/ui_text_caret_up |  |
| Dictionary | input/ui_text_caret_word_left |  |
| Dictionary | input/ui_text_caret_word_left.macos |  |
| Dictionary | input/ui_text_caret_word_right |  |
| Dictionary | input/ui_text_caret_word_right.macos |  |
| Dictionary | input/ui_text_clear_carets_and_selection |  |
| Dictionary | input/ui_text_completion_accept |  |
| Dictionary | input/ui_text_completion_query |  |
| Dictionary | input/ui_text_completion_replace |  |
| Dictionary | input/ui_text_dedent |  |
| Dictionary | input/ui_text_delete |  |
| Dictionary | input/ui_text_delete_all_to_right |  |
| Dictionary | input/ui_text_delete_all_to_right.macos |  |
| Dictionary | input/ui_text_delete_word |  |
| Dictionary | input/ui_text_delete_word.macos |  |
| Dictionary | input/ui_text_indent |  |
| Dictionary | input/ui_text_newline |  |
| Dictionary | input/ui_text_newline_above |  |
| Dictionary | input/ui_text_newline_blank |  |
| Dictionary | input/ui_text_scroll_down |  |
| Dictionary | input/ui_text_scroll_down.macos |  |
| Dictionary | input/ui_text_scroll_up |  |
| Dictionary | input/ui_text_scroll_up.macos |  |
| Dictionary | input/ui_text_select_all |  |
| Dictionary | input/ui_text_select_word_under_caret |  |
| Dictionary | input/ui_text_select_word_under_caret.macos |  |
| Dictionary | input/ui_text_skip_selection_for_next_occurrence |  |
| Dictionary | input/ui_text_submit |  |
| Dictionary | input/ui_text_toggle_insert_mode |  |
| Dictionary | input/ui_undo |  |
| Dictionary | input/ui_unicode_start |  |
| Dictionary | input/ui_up |  |
| bool | input_devices/buffering/agile_event_flushing | false |
| bool | input_devices/compatibility/legacy_just_pressed_behavior | false |
| String | input_devices/pen_tablet/driver |  |
| String | input_devices/pen_tablet/driver.windows |  |
| bool | input_devices/pointing/android/disable_scroll_deadzone | false |
| bool | input_devices/pointing/android/enable_long_press_as_right_click | false |
| bool | input_devices/pointing/android/enable_pan_and_scale_gestures | false |
| bool | input_devices/pointing/android/override_volume_buttons | false |
| int | input_devices/pointing/android/rotary_input_scroll_axis | 1 |
| bool | input_devices/pointing/emulate_mouse_from_touch | true |
| bool | input_devices/pointing/emulate_touch_from_mouse | false |
| bool | input_devices/sensors/enable_accelerometer | false |
| bool | input_devices/sensors/enable_gravity | false |
| bool | input_devices/sensors/enable_gyroscope | false |
| bool | input_devices/sensors/enable_magnetometer | false |
| String | internationalization/locale/fallback | "en" |
| bool | internationalization/locale/include_text_server_data | false |
| int | internationalization/locale/line_breaking_strictness | 0 |
| String | internationalization/locale/test | "" |
| bool | internationalization/pseudolocalization/double_vowels | false |
| float | internationalization/pseudolocalization/expansion_ratio | 0.0 |
| bool | internationalization/pseudolocalization/fake_bidi | false |
| bool | internationalization/pseudolocalization/override | false |
| String | internationalization/pseudolocalization/prefix | "[" |
| bool | internationalization/pseudolocalization/replace_with_accents | true |
| bool | internationalization/pseudolocalization/skip_placeholders | true |
| String | internationalization/pseudolocalization/suffix | "]" |
| bool | internationalization/pseudolocalization/use_pseudolocalization | false |
| bool | internationalization/rendering/force_right_to_left_layout_direction | false |
| bool | internationalization/rendering/root_node_auto_translate | true |
| int | internationalization/rendering/root_node_layout_direction | 0 |
| String | internationalization/rendering/text_driver | "" |
| String | layer_names/2d_navigation/layer_1 | "" |
| String | layer_names/2d_navigation/layer_2 | "" |
| String | layer_names/2d_navigation/layer_3 | "" |
| String | layer_names/2d_navigation/layer_4 | "" |
| String | layer_names/2d_navigation/layer_5 | "" |
| String | layer_names/2d_navigation/layer_6 | "" |
| String | layer_names/2d_navigation/layer_7 | "" |
| String | layer_names/2d_navigation/layer_8 | "" |
| String | layer_names/2d_navigation/layer_9 | "" |
| String | layer_names/2d_navigation/layer_10 | "" |
| String | layer_names/2d_navigation/layer_11 | "" |
| String | layer_names/2d_navigation/layer_12 | "" |
| String | layer_names/2d_navigation/layer_13 | "" |
| String | layer_names/2d_navigation/layer_14 | "" |
| String | layer_names/2d_navigation/layer_15 | "" |
| String | layer_names/2d_navigation/layer_16 | "" |
| String | layer_names/2d_navigation/layer_17 | "" |
| String | layer_names/2d_navigation/layer_18 | "" |
| String | layer_names/2d_navigation/layer_19 | "" |
| String | layer_names/2d_navigation/layer_20 | "" |
| String | layer_names/2d_navigation/layer_21 | "" |
| String | layer_names/2d_navigation/layer_22 | "" |
| String | layer_names/2d_navigation/layer_23 | "" |
| String | layer_names/2d_navigation/layer_24 | "" |
| String | layer_names/2d_navigation/layer_25 | "" |
| String | layer_names/2d_navigation/layer_26 | "" |
| String | layer_names/2d_navigation/layer_27 | "" |
| String | layer_names/2d_navigation/layer_28 | "" |
| String | layer_names/2d_navigation/layer_29 | "" |
| String | layer_names/2d_navigation/layer_30 | "" |
| String | layer_names/2d_navigation/layer_31 | "" |
| String | layer_names/2d_navigation/layer_32 | "" |
| String | layer_names/2d_physics/layer_1 | "" |
| String | layer_names/2d_physics/layer_2 | "" |
| String | layer_names/2d_physics/layer_3 | "" |
| String | layer_names/2d_physics/layer_4 | "" |
| String | layer_names/2d_physics/layer_5 | "" |
| String | layer_names/2d_physics/layer_6 | "" |
| String | layer_names/2d_physics/layer_7 | "" |
| String | layer_names/2d_physics/layer_8 | "" |
| String | layer_names/2d_physics/layer_9 | "" |
| String | layer_names/2d_physics/layer_10 | "" |
| String | layer_names/2d_physics/layer_11 | "" |
| String | layer_names/2d_physics/layer_12 | "" |
| String | layer_names/2d_physics/layer_13 | "" |
| String | layer_names/2d_physics/layer_14 | "" |
| String | layer_names/2d_physics/layer_15 | "" |
| String | layer_names/2d_physics/layer_16 | "" |
| String | layer_names/2d_physics/layer_17 | "" |
| String | layer_names/2d_physics/layer_18 | "" |
| String | layer_names/2d_physics/layer_19 | "" |
| String | layer_names/2d_physics/layer_20 | "" |
| String | layer_names/2d_physics/layer_21 | "" |
| String | layer_names/2d_physics/layer_22 | "" |
| String | layer_names/2d_physics/layer_23 | "" |
| String | layer_names/2d_physics/layer_24 | "" |
| String | layer_names/2d_physics/layer_25 | "" |
| String | layer_names/2d_physics/layer_26 | "" |
| String | layer_names/2d_physics/layer_27 | "" |
| String | layer_names/2d_physics/layer_28 | "" |
| String | layer_names/2d_physics/layer_29 | "" |
| String | layer_names/2d_physics/layer_30 | "" |
| String | layer_names/2d_physics/layer_31 | "" |
| String | layer_names/2d_physics/layer_32 | "" |
| String | layer_names/2d_render/layer_1 | "" |
| String | layer_names/2d_render/layer_2 | "" |
| String | layer_names/2d_render/layer_3 | "" |
| String | layer_names/2d_render/layer_4 | "" |
| String | layer_names/2d_render/layer_5 | "" |
| String | layer_names/2d_render/layer_6 | "" |
| String | layer_names/2d_render/layer_7 | "" |
| String | layer_names/2d_render/layer_8 | "" |
| String | layer_names/2d_render/layer_9 | "" |
| String | layer_names/2d_render/layer_10 | "" |
| String | layer_names/2d_render/layer_11 | "" |
| String | layer_names/2d_render/layer_12 | "" |
| String | layer_names/2d_render/layer_13 | "" |
| String | layer_names/2d_render/layer_14 | "" |
| String | layer_names/2d_render/layer_15 | "" |
| String | layer_names/2d_render/layer_16 | "" |
| String | layer_names/2d_render/layer_17 | "" |
| String | layer_names/2d_render/layer_18 | "" |
| String | layer_names/2d_render/layer_19 | "" |
| String | layer_names/2d_render/layer_20 | "" |
| String | layer_names/3d_navigation/layer_1 | "" |
| String | layer_names/3d_navigation/layer_2 | "" |
| String | layer_names/3d_navigation/layer_3 | "" |
| String | layer_names/3d_navigation/layer_4 | "" |
| String | layer_names/3d_navigation/layer_5 | "" |
| String | layer_names/3d_navigation/layer_6 | "" |
| String | layer_names/3d_navigation/layer_7 | "" |
| String | layer_names/3d_navigation/layer_8 | "" |
| String | layer_names/3d_navigation/layer_9 | "" |
| String | layer_names/3d_navigation/layer_10 | "" |
| String | layer_names/3d_navigation/layer_11 | "" |
| String | layer_names/3d_navigation/layer_12 | "" |
| String | layer_names/3d_navigation/layer_13 | "" |
| String | layer_names/3d_navigation/layer_14 | "" |
| String | layer_names/3d_navigation/layer_15 | "" |
| String | layer_names/3d_navigation/layer_16 | "" |
| String | layer_names/3d_navigation/layer_17 | "" |
| String | layer_names/3d_navigation/layer_18 | "" |
| String | layer_names/3d_navigation/layer_19 | "" |
| String | layer_names/3d_navigation/layer_20 | "" |
| String | layer_names/3d_navigation/layer_21 | "" |
| String | layer_names/3d_navigation/layer_22 | "" |
| String | layer_names/3d_navigation/layer_23 | "" |
| String | layer_names/3d_navigation/layer_24 | "" |
| String | layer_names/3d_navigation/layer_25 | "" |
| String | layer_names/3d_navigation/layer_26 | "" |
| String | layer_names/3d_navigation/layer_27 | "" |
| String | layer_names/3d_navigation/layer_28 | "" |
| String | layer_names/3d_navigation/layer_29 | "" |
| String | layer_names/3d_navigation/layer_30 | "" |
| String | layer_names/3d_navigation/layer_31 | "" |
| String | layer_names/3d_navigation/layer_32 | "" |
| String | layer_names/3d_physics/layer_1 | "" |
| String | layer_names/3d_physics/layer_2 | "" |
| String | layer_names/3d_physics/layer_3 | "" |
| String | layer_names/3d_physics/layer_4 | "" |
| String | layer_names/3d_physics/layer_5 | "" |
| String | layer_names/3d_physics/layer_6 | "" |
| String | layer_names/3d_physics/layer_7 | "" |
| String | layer_names/3d_physics/layer_8 | "" |
| String | layer_names/3d_physics/layer_9 | "" |
| String | layer_names/3d_physics/layer_10 | "" |
| String | layer_names/3d_physics/layer_11 | "" |
| String | layer_names/3d_physics/layer_12 | "" |
| String | layer_names/3d_physics/layer_13 | "" |
| String | layer_names/3d_physics/layer_14 | "" |
| String | layer_names/3d_physics/layer_15 | "" |
| String | layer_names/3d_physics/layer_16 | "" |
| String | layer_names/3d_physics/layer_17 | "" |
| String | layer_names/3d_physics/layer_18 | "" |
| String | layer_names/3d_physics/layer_19 | "" |
| String | layer_names/3d_physics/layer_20 | "" |
| String | layer_names/3d_physics/layer_21 | "" |
| String | layer_names/3d_physics/layer_22 | "" |
| String | layer_names/3d_physics/layer_23 | "" |
| String | layer_names/3d_physics/layer_24 | "" |
| String | layer_names/3d_physics/layer_25 | "" |
| String | layer_names/3d_physics/layer_26 | "" |
| String | layer_names/3d_physics/layer_27 | "" |
| String | layer_names/3d_physics/layer_28 | "" |
| String | layer_names/3d_physics/layer_29 | "" |
| String | layer_names/3d_physics/layer_30 | "" |
| String | layer_names/3d_physics/layer_31 | "" |
| String | layer_names/3d_physics/layer_32 | "" |
| String | layer_names/3d_render/layer_1 | "" |
| String | layer_names/3d_render/layer_2 | "" |
| String | layer_names/3d_render/layer_3 | "" |
| String | layer_names/3d_render/layer_4 | "" |
| String | layer_names/3d_render/layer_5 | "" |
| String | layer_names/3d_render/layer_6 | "" |
| String | layer_names/3d_render/layer_7 | "" |
| String | layer_names/3d_render/layer_8 | "" |
| String | layer_names/3d_render/layer_9 | "" |
| String | layer_names/3d_render/layer_10 | "" |
| String | layer_names/3d_render/layer_11 | "" |
| String | layer_names/3d_render/layer_12 | "" |
| String | layer_names/3d_render/layer_13 | "" |
| String | layer_names/3d_render/layer_14 | "" |
| String | layer_names/3d_render/layer_15 | "" |
| String | layer_names/3d_render/layer_16 | "" |
| String | layer_names/3d_render/layer_17 | "" |
| String | layer_names/3d_render/layer_18 | "" |
| String | layer_names/3d_render/layer_19 | "" |
| String | layer_names/3d_render/layer_20 | "" |
| String | layer_names/avoidance/layer_1 | "" |
| String | layer_names/avoidance/layer_2 | "" |
| String | layer_names/avoidance/layer_3 | "" |
| String | layer_names/avoidance/layer_4 | "" |
| String | layer_names/avoidance/layer_5 | "" |
| String | layer_names/avoidance/layer_6 | "" |
| String | layer_names/avoidance/layer_7 | "" |
| String | layer_names/avoidance/layer_8 | "" |
| String | layer_names/avoidance/layer_9 | "" |
| String | layer_names/avoidance/layer_10 | "" |
| String | layer_names/avoidance/layer_11 | "" |
| String | layer_names/avoidance/layer_12 | "" |
| String | layer_names/avoidance/layer_13 | "" |
| String | layer_names/avoidance/layer_14 | "" |
| String | layer_names/avoidance/layer_15 | "" |
| String | layer_names/avoidance/layer_16 | "" |
| String | layer_names/avoidance/layer_17 | "" |
| String | layer_names/avoidance/layer_18 | "" |
| String | layer_names/avoidance/layer_19 | "" |
| String | layer_names/avoidance/layer_20 | "" |
| String | layer_names/avoidance/layer_21 | "" |
| String | layer_names/avoidance/layer_22 | "" |
| String | layer_names/avoidance/layer_23 | "" |
| String | layer_names/avoidance/layer_24 | "" |
| String | layer_names/avoidance/layer_25 | "" |
| String | layer_names/avoidance/layer_26 | "" |
| String | layer_names/avoidance/layer_27 | "" |
| String | layer_names/avoidance/layer_28 | "" |
| String | layer_names/avoidance/layer_29 | "" |
| String | layer_names/avoidance/layer_30 | "" |
| String | layer_names/avoidance/layer_31 | "" |
| String | layer_names/avoidance/layer_32 | "" |
| int | memory/limits/message_queue/max_size_mb | 32 |
| float | navigation/2d/default_cell_size | 1.0 |
| float | navigation/2d/default_edge_connection_margin | 1.0 |
| float | navigation/2d/default_link_connection_radius | 4.0 |
| float | navigation/2d/merge_rasterizer_cell_scale | 1.0 |
| String | navigation/2d/navigation_engine | "DEFAULT" |
| bool | navigation/2d/use_edge_connections | true |
| bool | navigation/2d/warnings/navmesh_cell_size_mismatch | true |
| bool | navigation/2d/warnings/navmesh_edge_merge_errors | true |
| float | navigation/3d/default_cell_height | 0.25 |
| float | navigation/3d/default_cell_size | 0.25 |
| float | navigation/3d/default_edge_connection_margin | 0.25 |
| float | navigation/3d/default_link_connection_radius | 1.0 |
| Vector3 | navigation/3d/default_up | Vector3(0,1,0) |
| float | navigation/3d/merge_rasterizer_cell_scale | 1.0 |
| String | navigation/3d/navigation_engine | "DEFAULT" |
| bool | navigation/3d/use_edge_connections | true |
| bool | navigation/3d/warnings/navmesh_cell_size_mismatch | true |
| bool | navigation/3d/warnings/navmesh_edge_merge_errors | true |
| bool | navigation/avoidance/thread_model/avoidance_use_high_priority_threads | true |
| bool | navigation/avoidance/thread_model/avoidance_use_multiple_threads | true |
| bool | navigation/baking/thread_model/baking_use_high_priority_threads | true |
| bool | navigation/baking/thread_model/baking_use_multiple_threads | true |
| bool | navigation/baking/use_crash_prevention_checks | true |
| int | navigation/pathfinding/max_threads | 4 |
| bool | navigation/world/map_use_async_iterations | true |
| bool | navigation/world/region_use_async_iterations | true |
| int | network/limits/debugger/max_chars_per_second | 32768 |
| int | network/limits/debugger/max_errors_per_second | 400 |
| int | network/limits/debugger/max_queued_messages | 2048 |
| int | network/limits/debugger/max_warnings_per_second | 400 |
| int | network/limits/packet_peer_stream/max_buffer_po2 | 16 |
| int | network/limits/tcp/connect_timeout_seconds | 30 |
| int | network/limits/unix/connect_timeout_seconds | 30 |
| int | network/limits/webrtc/max_channel_in_buffer_kb | 64 |
| String | network/tls/certificate_bundle_override | "" |
| bool | network/tls/enable_tls_v1.3 | true |
| float | physics/2d/default_angular_damp | 1.0 |
| float | physics/2d/default_gravity | 980.0 |
| Vector2 | physics/2d/default_gravity_vector | Vector2(0,1) |
| float | physics/2d/default_linear_damp | 0.1 |
| String | physics/2d/physics_engine | "DEFAULT" |
| bool | physics/2d/run_on_separate_thread | false |
| float | physics/2d/sleep_threshold_angular | 0.13962634 |
| float | physics/2d/sleep_threshold_linear | 2.0 |
| float | physics/2d/solver/contact_max_allowed_penetration | 0.3 |
| float | physics/2d/solver/contact_max_separation | 1.5 |
| float | physics/2d/solver/contact_recycle_radius | 1.0 |
| float | physics/2d/solver/default_constraint_bias | 0.2 |
| float | physics/2d/solver/default_contact_bias | 0.8 |
| int | physics/2d/solver/solver_iterations | 16 |
| float | physics/2d/time_before_sleep | 0.5 |
| float | physics/3d/default_angular_damp | 0.1 |
| float | physics/3d/default_gravity | 9.8 |
| Vector3 | physics/3d/default_gravity_vector | Vector3(0,-1,0) |
| float | physics/3d/default_linear_damp | 0.1 |
| String | physics/3d/physics_engine | "DEFAULT" |
| String | physics/3d/physics_interpolation/scene_traversal | "DEFAULT" |
| bool | physics/3d/run_on_separate_thread | false |
| float | physics/3d/sleep_threshold_angular | 0.13962634 |
| float | physics/3d/sleep_threshold_linear | 0.1 |
| float | physics/3d/solver/contact_max_allowed_penetration | 0.01 |
| float | physics/3d/solver/contact_max_separation | 0.05 |
| float | physics/3d/solver/contact_recycle_radius | 0.01 |
| float | physics/3d/solver/default_contact_bias | 0.8 |
| int | physics/3d/solver/solver_iterations | 16 |
| float | physics/3d/time_before_sleep | 0.5 |
| bool | physics/common/enable_object_picking | true |
| int | physics/common/max_physics_steps_per_frame | 8 |
| bool | physics/common/physics_interpolation | false |
| float | physics/common/physics_jitter_fix | 0.5 |
| int | physics/common/physics_ticks_per_second | 60 |
| float | physics/jolt_physics_3d/collisions/active_edge_threshold | 0.87266463 |
| float | physics/jolt_physics_3d/collisions/collision_margin_fraction | 0.08 |
| int | physics/jolt_physics_3d/joints/world_node | 0 |
| float | physics/jolt_physics_3d/limits/max_angular_velocity | 47.12389 |
| int | physics/jolt_physics_3d/limits/max_bodies | 10240 |
| int | physics/jolt_physics_3d/limits/max_body_pairs | 65536 |
| int | physics/jolt_physics_3d/limits/max_contact_constraints | 20480 |
| float | physics/jolt_physics_3d/limits/max_linear_velocity | 500.0 |
| int | physics/jolt_physics_3d/limits/temporary_memory_buffer_size | 32 |
| float | physics/jolt_physics_3d/limits/world_boundary_shape_size | 2000.0 |
| float | physics/jolt_physics_3d/motion_queries/recovery_amount | 0.4 |
| int | physics/jolt_physics_3d/motion_queries/recovery_iterations | 4 |
| bool | physics/jolt_physics_3d/motion_queries/use_enhanced_internal_edge_removal | true |
| bool | physics/jolt_physics_3d/queries/enable_ray_cast_face_index | false |
| bool | physics/jolt_physics_3d/queries/use_enhanced_internal_edge_removal | false |
| bool | physics/jolt_physics_3d/simulation/allow_sleep | true |
| float | physics/jolt_physics_3d/simulation/baumgarte_stabilization_factor | 0.2 |
| float | physics/jolt_physics_3d/simulation/body_pair_contact_cache_angle_threshold | 0.034906585 |
| float | physics/jolt_physics_3d/simulation/body_pair_contact_cache_distance_threshold | 0.001 |
| bool | physics/jolt_physics_3d/simulation/body_pair_contact_cache_enabled | true |
| float | physics/jolt_physics_3d/simulation/bounce_velocity_threshold | 1.0 |
| float | physics/jolt_physics_3d/simulation/continuous_cd_max_penetration | 0.25 |
| float | physics/jolt_physics_3d/simulation/continuous_cd_movement_threshold | 0.75 |
| bool | physics/jolt_physics_3d/simulation/generate_all_kinematic_contacts | false |
| float | physics/jolt_physics_3d/simulation/penetration_slop | 0.02 |
| int | physics/jolt_physics_3d/simulation/position_steps | 2 |
| float | physics/jolt_physics_3d/simulation/sleep_time_threshold | 0.5 |
| float | physics/jolt_physics_3d/simulation/sleep_velocity_threshold | 0.03 |
| float | physics/jolt_physics_3d/simulation/soft_body_point_radius | 0.01 |
| float | physics/jolt_physics_3d/simulation/speculative_contact_distance | 0.02 |
| bool | physics/jolt_physics_3d/simulation/use_enhanced_internal_edge_removal | true |
| int | physics/jolt_physics_3d/simulation/velocity_steps | 10 |
| int | rendering/2d/batching/item_buffer_size | 16384 |
| int | rendering/2d/batching/uniform_set_cache_size | 4096 |
| int | rendering/2d/sdf/oversize | 1 |
| int | rendering/2d/sdf/scale | 1 |
| int | rendering/2d/shadow_atlas/size | 2048 |
| bool | rendering/2d/snap/snap_2d_transforms_to_pixel | false |
| bool | rendering/2d/snap/snap_2d_vertices_to_pixel | false |
| int | rendering/anti_aliasing/quality/msaa_2d | 0 |
| int | rendering/anti_aliasing/quality/msaa_3d | 0 |
| int | rendering/anti_aliasing/quality/screen_space_aa | 0 |
| float | rendering/anti_aliasing/quality/smaa_edge_detection_threshold | 0.05 |
| bool | rendering/anti_aliasing/quality/use_debanding | false |
| bool | rendering/anti_aliasing/quality/use_taa | false |
| float | rendering/anti_aliasing/screen_space_roughness_limiter/amount | 0.25 |
| bool | rendering/anti_aliasing/screen_space_roughness_limiter/enabled | true |
| float | rendering/anti_aliasing/screen_space_roughness_limiter/limit | 0.18 |
| int | rendering/camera/depth_of_field/depth_of_field_bokeh_quality | 1 |
| int | rendering/camera/depth_of_field/depth_of_field_bokeh_shape | 1 |
| bool | rendering/camera/depth_of_field/depth_of_field_use_jitter | false |
| String | rendering/driver/depth_prepass/disable_for_vendors | "PowerVR,Mali,Adreno,Apple" |
| bool | rendering/driver/depth_prepass/enable | true |
| int | rendering/driver/threads/thread_model | 1 |
| Color | rendering/environment/defaults/default_clear_color | Color(0.3,0.3,0.3,1) |
| String | rendering/environment/defaults/default_environment | "" |
| int | rendering/environment/glow/upscale_mode | 1 |
| int | rendering/environment/glow/upscale_mode.mobile | 0 |
| bool | rendering/environment/screen_space_reflection/half_size | true |
| float | rendering/environment/ssao/adaptive_target | 0.5 |
| int | rendering/environment/ssao/blur_passes | 2 |
| float | rendering/environment/ssao/fadeout_from | 50.0 |
| float | rendering/environment/ssao/fadeout_to | 300.0 |
| bool | rendering/environment/ssao/half_size | true |
| int | rendering/environment/ssao/quality | 2 |
| float | rendering/environment/ssil/adaptive_target | 0.5 |
| int | rendering/environment/ssil/blur_passes | 4 |
| float | rendering/environment/ssil/fadeout_from | 50.0 |
| float | rendering/environment/ssil/fadeout_to | 300.0 |
| bool | rendering/environment/ssil/half_size | true |
| int | rendering/environment/ssil/quality | 2 |
| float | rendering/environment/subsurface_scattering/subsurface_scattering_depth_scale | 0.01 |
| int | rendering/environment/subsurface_scattering/subsurface_scattering_quality | 1 |
| float | rendering/environment/subsurface_scattering/subsurface_scattering_scale | 0.05 |
| int | rendering/environment/volumetric_fog/use_filter | 1 |
| int | rendering/environment/volumetric_fog/volume_depth | 64 |
| int | rendering/environment/volumetric_fog/volume_size | 64 |
| String | rendering/gl_compatibility/driver | "opengl3" |
| String | rendering/gl_compatibility/driver.android | "opengl3" |
| String | rendering/gl_compatibility/driver.ios | "opengl3" |
| String | rendering/gl_compatibility/driver.linuxbsd | "opengl3" |
| String | rendering/gl_compatibility/driver.macos | "opengl3" |
| String | rendering/gl_compatibility/driver.web | "opengl3" |
| String | rendering/gl_compatibility/driver.windows | "opengl3" |
| bool | rendering/gl_compatibility/fallback_to_angle | true |
| bool | rendering/gl_compatibility/fallback_to_gles | true |
| bool | rendering/gl_compatibility/fallback_to_native | true |
| Array | rendering/gl_compatibility/force_angle_on_devices |  |
| int | rendering/gl_compatibility/item_buffer_size | 16384 |
| bool | rendering/gl_compatibility/nvidia_disable_threaded_optimization | true |
| bool | rendering/global_illumination/gi/use_half_resolution | false |
| int | rendering/global_illumination/sdfgi/frames_to_converge | 5 |
| int | rendering/global_illumination/sdfgi/frames_to_update_lights | 2 |
| int | rendering/global_illumination/sdfgi/probe_ray_count | 1 |
| int | rendering/global_illumination/voxel_gi/quality | 0 |
| int | rendering/lightmapping/bake_performance/max_rays_per_pass | 4 |
| int | rendering/lightmapping/bake_performance/max_rays_per_probe_pass | 64 |
| int | rendering/lightmapping/bake_performance/max_transparency_rays | 8 |
| int | rendering/lightmapping/bake_performance/region_size | 512 |
| int | rendering/lightmapping/bake_quality/high_quality_probe_ray_count | 512 |
| int | rendering/lightmapping/bake_quality/high_quality_ray_count | 512 |
| int | rendering/lightmapping/bake_quality/low_quality_probe_ray_count | 64 |
| int | rendering/lightmapping/bake_quality/low_quality_ray_count | 32 |
| int | rendering/lightmapping/bake_quality/medium_quality_probe_ray_count | 256 |
| int | rendering/lightmapping/bake_quality/medium_quality_ray_count | 128 |
| int | rendering/lightmapping/bake_quality/ultra_quality_probe_ray_count | 2048 |
| int | rendering/lightmapping/bake_quality/ultra_quality_ray_count | 2048 |
| int | rendering/lightmapping/denoising/denoiser | 0 |
| bool | rendering/lightmapping/lightmap_gi/use_bicubic_filter | true |
| float | rendering/lightmapping/primitive_meshes/texel_size | 0.2 |
| float | rendering/lightmapping/probe_capture/update_speed | 15 |
| bool | rendering/lights_and_shadows/directional_shadow/16_bits | true |
| int | rendering/lights_and_shadows/directional_shadow/size | 4096 |
| int | rendering/lights_and_shadows/directional_shadow/size.mobile | 2048 |
| int | rendering/lights_and_shadows/directional_shadow/soft_shadow_filter_quality | 2 |
| int | rendering/lights_and_shadows/directional_shadow/soft_shadow_filter_quality.mobile | 0 |
| bool | rendering/lights_and_shadows/positional_shadow/atlas_16_bits | true |
| int | rendering/lights_and_shadows/positional_shadow/atlas_quadrant_0_subdiv | 2 |
| int | rendering/lights_and_shadows/positional_shadow/atlas_quadrant_1_subdiv | 2 |
| int | rendering/lights_and_shadows/positional_shadow/atlas_quadrant_2_subdiv | 3 |
| int | rendering/lights_and_shadows/positional_shadow/atlas_quadrant_3_subdiv | 4 |
| int | rendering/lights_and_shadows/positional_shadow/atlas_size | 4096 |
| int | rendering/lights_and_shadows/positional_shadow/atlas_size.mobile | 2048 |
| int | rendering/lights_and_shadows/positional_shadow/soft_shadow_filter_quality | 2 |
| int | rendering/lights_and_shadows/positional_shadow/soft_shadow_filter_quality.mobile | 0 |
| bool | rendering/lights_and_shadows/tighter_shadow_caster_culling | true |
| bool | rendering/lights_and_shadows/use_physical_light_units | false |
| float | rendering/limits/cluster_builder/max_clustered_elements | 512 |
| int | rendering/limits/global_shader_variables/buffer_size | 65536 |
| int | rendering/limits/opengl/max_lights_per_object | 8 |
| int | rendering/limits/opengl/max_renderable_elements | 65536 |
| int | rendering/limits/opengl/max_renderable_lights | 32 |
| int | rendering/limits/spatial_indexer/threaded_cull_minimum_instances | 1000 |
| int | rendering/limits/spatial_indexer/update_iterations_per_frame | 10 |
| float | rendering/limits/time/time_rollover_secs | 3600 |
| float | rendering/mesh_lod/lod_change/threshold_pixels | 1.0 |
| int | rendering/occlusion_culling/bvh_build_quality | 2 |
| bool | rendering/occlusion_culling/jitter_projection | true |
| int | rendering/occlusion_culling/occlusion_rays_per_thread | 512 |
| bool | rendering/occlusion_culling/use_occlusion_culling | false |
| int | rendering/reflections/reflection_atlas/reflection_count | 64 |
| int | rendering/reflections/reflection_atlas/reflection_size | 256 |
| int | rendering/reflections/reflection_atlas/reflection_size.mobile | 128 |
| bool | rendering/reflections/sky_reflections/fast_filter_high_quality | false |
| int | rendering/reflections/sky_reflections/ggx_samples | 32 |
| int | rendering/reflections/sky_reflections/ggx_samples.mobile | 16 |
| int | rendering/reflections/sky_reflections/roughness_layers | 7 |
| bool | rendering/reflections/sky_reflections/texture_array_reflections | true |
| bool | rendering/reflections/sky_reflections/texture_array_reflections.mobile | false |
| bool | rendering/reflections/specular_occlusion/enabled | true |
| String | rendering/renderer/rendering_method | "forward_plus" |
| String | rendering/renderer/rendering_method.mobile | "mobile" |
| String | rendering/renderer/rendering_method.web | "gl_compatibility" |
| int | rendering/rendering_device/d3d12/agility_sdk_version | 618 |
| int | rendering/rendering_device/d3d12/max_resource_descriptors | 65536 |
| int | rendering/rendering_device/d3d12/max_sampler_descriptors | 1024 |
| String | rendering/rendering_device/driver | "vulkan" |
| String | rendering/rendering_device/driver.android | "vulkan" |
| String | rendering/rendering_device/driver.ios | "metal" |
| String | rendering/rendering_device/driver.linuxbsd | "vulkan" |
| String | rendering/rendering_device/driver.macos | "metal" |
| String | rendering/rendering_device/driver.visionos | "metal" |
| String | rendering/rendering_device/driver.windows | "vulkan" |
| bool | rendering/rendering_device/fallback_to_d3d12 | true |
| bool | rendering/rendering_device/fallback_to_opengl3 | true |
| bool | rendering/rendering_device/fallback_to_vulkan | true |
| bool | rendering/rendering_device/pipeline_cache/enable | true |
| float | rendering/rendering_device/pipeline_cache/save_chunk_size_mb | 3.0 |
| int | rendering/rendering_device/staging_buffer/block_size_kb | 256 |
| int | rendering/rendering_device/staging_buffer/max_size_mb | 128 |
| int | rendering/rendering_device/staging_buffer/texture_download_region_size_px | 64 |
| int | rendering/rendering_device/staging_buffer/texture_upload_region_size_px | 64 |
| int | rendering/rendering_device/vsync/frame_queue_size | 2 |
| int | rendering/rendering_device/vsync/swapchain_image_count | 3 |
| int | rendering/rendering_device/vulkan/max_descriptors_per_pool | 64 |
| float | rendering/scaling_3d/fsr_sharpness | 0.2 |
| int | rendering/scaling_3d/mode | 0 |
| int | rendering/scaling_3d/mode.ios |  |
| int | rendering/scaling_3d/mode.macos |  |
| float | rendering/scaling_3d/scale | 1.0 |
| bool | rendering/shader_compiler/shader_cache/compress | true |
| bool | rendering/shader_compiler/shader_cache/enabled | true |
| bool | rendering/shader_compiler/shader_cache/strip_debug | false |
| bool | rendering/shader_compiler/shader_cache/strip_debug.release | true |
| bool | rendering/shader_compiler/shader_cache/use_zstd_compression | true |
| bool | rendering/shading/overrides/force_lambert_over_burley | false |
| bool | rendering/shading/overrides/force_lambert_over_burley.mobile | true |
| bool | rendering/shading/overrides/force_vertex_shading | false |
| int | rendering/textures/basis_universal/rdo_dict_size | 1024 |
| bool | rendering/textures/basis_universal/zstd_supercompression | true |
| int | rendering/textures/basis_universal/zstd_supercompression_level | 6 |
| int | rendering/textures/canvas_textures/default_texture_filter | 1 |
| int | rendering/textures/canvas_textures/default_texture_repeat | 0 |
| int | rendering/textures/decals/filter | 3 |
| int | rendering/textures/default_filters/anisotropic_filtering_level | 2 |
| float | rendering/textures/default_filters/texture_mipmap_bias | 0.0 |
| bool | rendering/textures/default_filters/use_nearest_mipmap_filter | false |
| int | rendering/textures/light_projectors/filter | 3 |
| bool | rendering/textures/lossless_compression/force_png | false |
| bool | rendering/textures/vram_compression/cache_gpu_compressor | true |
| bool | rendering/textures/vram_compression/compress_with_gpu | true |
| bool | rendering/textures/vram_compression/import_etc2_astc | false |
| bool | rendering/textures/vram_compression/import_s3tc_bptc | false |
| int | rendering/textures/webp_compression/compression_method | 2 |
| float | rendering/textures/webp_compression/lossless_compression_factor | 25 |
| bool | rendering/viewport/hdr_2d | false |
| bool | rendering/viewport/transparent_background | false |
| int | rendering/vrs/mode | 0 |
| String | rendering/vrs/texture | "" |
| float | threading/worker_pool/low_priority_thread_ratio | 0.3 |
| int | threading/worker_pool/max_threads | -1 |
| bool | xr/openxr/binding_modifiers/analog_threshold | false |
| bool | xr/openxr/binding_modifiers/dpad_binding | false |
| String | xr/openxr/default_action_map | "res://openxr_action_map.tres" |
| bool | xr/openxr/enabled | false |
| int | xr/openxr/environment_blend_mode | "0" |
| int | xr/openxr/extensions/debug_message_types | "15" |
| int | xr/openxr/extensions/debug_utils | "0" |
| bool | xr/openxr/extensions/eye_gaze_interaction | false |
| bool | xr/openxr/extensions/frame_synthesis | false |
| bool | xr/openxr/extensions/hand_interaction_profile | false |
| bool | xr/openxr/extensions/hand_tracking | false |
| bool | xr/openxr/extensions/hand_tracking_controller_data_source | false |
| bool | xr/openxr/extensions/hand_tracking_unobstructed_data_source | false |
| bool | xr/openxr/extensions/render_model | false |
| int | xr/openxr/extensions/spatial_entity/april_tag_dict | "3" |
| int | xr/openxr/extensions/spatial_entity/aruco_dict | "15" |
| bool | xr/openxr/extensions/spatial_entity/enable_builtin_anchor_detection | false |
| bool | xr/openxr/extensions/spatial_entity/enable_builtin_marker_tracking | false |
| bool | xr/openxr/extensions/spatial_entity/enable_builtin_plane_detection | false |
| bool | xr/openxr/extensions/spatial_entity/enable_marker_tracking | false |
| bool | xr/openxr/extensions/spatial_entity/enable_persistent_anchors | false |
| bool | xr/openxr/extensions/spatial_entity/enable_plane_tracking | false |
| bool | xr/openxr/extensions/spatial_entity/enable_spatial_anchors | false |
| bool | xr/openxr/extensions/spatial_entity/enabled | false |
| int | xr/openxr/form_factor | "0" |
| bool | xr/openxr/foveation_dynamic | false |
| int | xr/openxr/foveation_level | "0" |
| int | xr/openxr/reference_space | "1" |
| bool | xr/openxr/startup_alert | true |
| bool | xr/openxr/submit_depth_buffer | false |
| String | xr/openxr/target_api_version | "" |
| int | xr/openxr/view_configuration | "1" |
| bool | xr/shaders/enabled | false |

accessibility/general/accessibility_support
accessibility/general/updates_per_second
bool
animation/compatibility/default_parent_skeleton_in_mesh_instance_3d
false
bool
animation/warnings/check_angle_interpolation_type_conflicting
true
bool
animation/warnings/check_invalid_track_paths
true
Color
application/boot_splash/bg_color
Color(0.14,0.14,0.14,1)
String
application/boot_splash/image
application/boot_splash/minimum_display_time
bool
application/boot_splash/show_image
true
application/boot_splash/stretch_mode
bool
application/boot_splash/use_filter
true
bool
application/config/auto_accept_quit
true
String
application/config/custom_user_dir_name
String
application/config/description
bool
application/config/disable_project_settings_override
false
String
application/config/icon
String
application/config/macos_native_icon
String
application/config/name
Dictionary
application/config/name_localized
String
application/config/project_settings_override
bool
application/config/quit_on_go_back
true
bool
application/config/use_custom_user_dir
false
bool
application/config/use_hidden_project_data_directory
true
String
application/config/version
String
application/config/windows_native_icon
bool
application/run/delta_smoothing
true
bool
application/run/disable_stderr
false
bool
application/run/disable_stdout
false
bool
application/run/enable_alt_space_menu
false
bool
application/run/flush_stdout_on_print
false
bool
application/run/flush_stdout_on_print.debug
true
application/run/frame_delay_msec
bool
application/run/load_shell_environment
false
bool
application/run/low_processor_mode
false
application/run/low_processor_mode_sleep_usec
6900
String
application/run/main_loop_type
"SceneTree"
String
application/run/main_scene
application/run/max_fps
bool
application/run/print_header
true
float
audio/buses/channel_disable_threshold_db
-60.0
float
audio/buses/channel_disable_time
String
audio/buses/default_bus_layout
"res://default_bus_layout.tres"
String
audio/driver/driver
bool
audio/driver/enable_input
false
audio/driver/mix_rate
44100
audio/driver/mix_rate.web
audio/driver/output_latency
audio/driver/output_latency.web
float
audio/general/2d_panning_strength
float
audio/general/3d_panning_strength
audio/general/default_playback_type
audio/general/default_playback_type.web
bool
audio/general/ios/mix_with_others
false
audio/general/ios/session_category
bool
audio/general/text_to_speech
false
audio/video/video_delay_compensation_ms
bool
collada/use_ambient
false
compression/formats/gzip/compression_level
compression/formats/zlib/compression_level
compression/formats/zstd/compression_level
bool
compression/formats/zstd/long_distance_matching
false
compression/formats/zstd/window_log_size
Color
debug/canvas_items/debug_redraw_color
Color(1,0.2,0.2,0.5)
float
debug/canvas_items/debug_redraw_time
bool
debug/file_logging/enable_file_logging
false
bool
debug/file_logging/enable_file_logging.pc
true
String
debug/file_logging/log_path
"user://logs/godot.log"
debug/file_logging/max_log_files
debug/gdscript/warnings/assert_always_false
debug/gdscript/warnings/assert_always_true
debug/gdscript/warnings/confusable_capture_reassignment
debug/gdscript/warnings/confusable_identifier
debug/gdscript/warnings/confusable_local_declaration
debug/gdscript/warnings/confusable_local_usage
debug/gdscript/warnings/deprecated_keyword
Dictionary
debug/gdscript/warnings/directory_rules
{"res://addons":0}
debug/gdscript/warnings/empty_file
bool
debug/gdscript/warnings/enable
true
debug/gdscript/warnings/enum_variable_without_default
debug/gdscript/warnings/get_node_default_without_onready
debug/gdscript/warnings/incompatible_ternary
debug/gdscript/warnings/inference_on_variant
debug/gdscript/warnings/inferred_declaration
debug/gdscript/warnings/int_as_enum_without_cast
debug/gdscript/warnings/int_as_enum_without_match
debug/gdscript/warnings/integer_division
debug/gdscript/warnings/missing_await
debug/gdscript/warnings/missing_tool
debug/gdscript/warnings/narrowing_conversion
debug/gdscript/warnings/native_method_override
debug/gdscript/warnings/onready_with_export
debug/gdscript/warnings/redundant_await
debug/gdscript/warnings/redundant_static_unload
bool
debug/gdscript/warnings/renamed_in_godot_4_hint
true
debug/gdscript/warnings/return_value_discarded
debug/gdscript/warnings/shadowed_global_identifier
debug/gdscript/warnings/shadowed_variable
debug/gdscript/warnings/shadowed_variable_base_class
debug/gdscript/warnings/standalone_expression
debug/gdscript/warnings/standalone_ternary
debug/gdscript/warnings/static_called_on_instance
debug/gdscript/warnings/unassigned_variable
debug/gdscript/warnings/unassigned_variable_op_assign
debug/gdscript/warnings/unreachable_code
debug/gdscript/warnings/unreachable_pattern
debug/gdscript/warnings/unsafe_call_argument
debug/gdscript/warnings/unsafe_cast
debug/gdscript/warnings/unsafe_method_access
debug/gdscript/warnings/unsafe_property_access
debug/gdscript/warnings/unsafe_void_return
debug/gdscript/warnings/untyped_declaration
debug/gdscript/warnings/unused_local_constant
debug/gdscript/warnings/unused_parameter
debug/gdscript/warnings/unused_private_class_variable
debug/gdscript/warnings/unused_signal
debug/gdscript/warnings/unused_variable
String
debug/settings/crash_handler/message
"Pleaseincludethiswhenreportingthebugtotheprojectdeveloper."
String
debug/settings/crash_handler/message.editor
"Pleaseincludethiswhenreportingthebugon:https://github.com/godotengine/godot/issues"
bool
debug/settings/gdscript/always_track_call_stacks
false
bool
debug/settings/gdscript/always_track_local_variables
false
debug/settings/gdscript/max_call_stack
1024
bool
debug/settings/physics_interpolation/enable_warnings
true
debug/settings/profiler/max_functions
16384
debug/settings/profiler/max_timestamp_query_elements
bool
debug/settings/stdout/print_fps
false
bool
debug/settings/stdout/print_gpu_profile
false
bool
debug/settings/stdout/verbose_stdout
false
bool
debug/shader_language/warnings/device_limit_exceeded
true
bool
debug/shader_language/warnings/enable
true
bool
debug/shader_language/warnings/float_comparison
true
bool
debug/shader_language/warnings/formatting_error
true
bool
debug/shader_language/warnings/magic_position_write
true
bool
debug/shader_language/warnings/treat_warnings_as_errors
false
bool
debug/shader_language/warnings/unused_constant
true
bool
debug/shader_language/warnings/unused_function
true
bool
debug/shader_language/warnings/unused_local_variable
true
bool
debug/shader_language/warnings/unused_struct
true
bool
debug/shader_language/warnings/unused_uniform
true
bool
debug/shader_language/warnings/unused_varying
true
Color
debug/shapes/avoidance/2d/agents_radius_color
Color(1,1,0,0.25)
bool
debug/shapes/avoidance/2d/enable_agents_radius
true
bool
debug/shapes/avoidance/2d/enable_obstacles_radius
true
bool
debug/shapes/avoidance/2d/enable_obstacles_static
true
Color
debug/shapes/avoidance/2d/obstacles_radius_color
Color(1,0.5,0,0.25)
Color
debug/shapes/avoidance/2d/obstacles_static_edge_pushin_color
Color(1,0,0,1)
Color
debug/shapes/avoidance/2d/obstacles_static_edge_pushout_color
Color(1,1,0,1)
Color
debug/shapes/avoidance/2d/obstacles_static_face_pushin_color
Color(1,0,0,0)
Color
debug/shapes/avoidance/2d/obstacles_static_face_pushout_color
Color(1,1,0,0.5)
Color
debug/shapes/avoidance/3d/agents_radius_color
Color(1,1,0,0.25)
bool
debug/shapes/avoidance/3d/enable_agents_radius
true
bool
debug/shapes/avoidance/3d/enable_obstacles_radius
true
bool
debug/shapes/avoidance/3d/enable_obstacles_static
true
Color
debug/shapes/avoidance/3d/obstacles_radius_color
Color(1,0.5,0,0.25)
Color
debug/shapes/avoidance/3d/obstacles_static_edge_pushin_color
Color(1,0,0,1)
Color
debug/shapes/avoidance/3d/obstacles_static_edge_pushout_color
Color(1,1,0,1)
Color
debug/shapes/avoidance/3d/obstacles_static_face_pushin_color
Color(1,0,0,0)
Color
debug/shapes/avoidance/3d/obstacles_static_face_pushout_color
Color(1,1,0,0.5)
Color
debug/shapes/collision/contact_color
Color(1,0.2,0.1,0.8)
bool
debug/shapes/collision/draw_2d_outlines
true
debug/shapes/collision/max_contacts_displayed
10000
Color
debug/shapes/collision/shape_color
Color(0,0.6,0.7,0.42)
Color
debug/shapes/navigation/2d/agent_path_color
Color(1,0,0,1)
float
debug/shapes/navigation/2d/agent_path_point_size
Color
debug/shapes/navigation/2d/edge_connection_color
Color(1,0,1,1)
bool
debug/shapes/navigation/2d/enable_agent_paths
true
bool
debug/shapes/navigation/2d/enable_edge_connections
true
bool
debug/shapes/navigation/2d/enable_edge_lines
true
bool
debug/shapes/navigation/2d/enable_geometry_face_random_color
true
bool
debug/shapes/navigation/2d/enable_link_connections
true
Color
debug/shapes/navigation/2d/geometry_edge_color
Color(0.5,1,1,1)
Color
debug/shapes/navigation/2d/geometry_edge_disabled_color
Color(0.5,0.5,0.5,1)
Color
debug/shapes/navigation/2d/geometry_face_color
Color(0.5,1,1,0.4)
Color
debug/shapes/navigation/2d/geometry_face_disabled_color
Color(0.5,0.5,0.5,0.4)
Color
debug/shapes/navigation/2d/link_connection_color
Color(1,0.5,1,1)
Color
debug/shapes/navigation/2d/link_connection_disabled_color
Color(0.5,0.5,0.5,1)
Color
debug/shapes/navigation/3d/agent_path_color
Color(1,0,0,1)
float
debug/shapes/navigation/3d/agent_path_point_size
Color
debug/shapes/navigation/3d/edge_connection_color
Color(1,0,1,1)
bool
debug/shapes/navigation/3d/enable_agent_paths
true
bool
debug/shapes/navigation/3d/enable_agent_paths_xray
true
bool
debug/shapes/navigation/3d/enable_edge_connections
true
bool
debug/shapes/navigation/3d/enable_edge_connections_xray
true
bool
debug/shapes/navigation/3d/enable_edge_lines
true
bool
debug/shapes/navigation/3d/enable_edge_lines_xray
true
bool
debug/shapes/navigation/3d/enable_geometry_face_random_color
true
bool
debug/shapes/navigation/3d/enable_link_connections
true
bool
debug/shapes/navigation/3d/enable_link_connections_xray
true
Color
debug/shapes/navigation/3d/geometry_edge_color
Color(0.5,1,1,1)
Color
debug/shapes/navigation/3d/geometry_edge_disabled_color
Color(0.5,0.5,0.5,1)
Color
debug/shapes/navigation/3d/geometry_face_color
Color(0.5,1,1,0.4)
Color
debug/shapes/navigation/3d/geometry_face_disabled_color
Color(0.5,0.5,0.5,0.4)
Color
debug/shapes/navigation/3d/link_connection_color
Color(1,0.5,1,1)
Color
debug/shapes/navigation/3d/link_connection_disabled_color
Color(0.5,0.5,0.5,1)
Color
debug/shapes/paths/geometry_color
Color(0.1,1,0.7,0.4)
float
debug/shapes/paths/geometry_width
String
display/display_server/driver
String
display/display_server/driver.android
String
display/display_server/driver.ios
String
display/display_server/driver.linuxbsd
String
display/display_server/driver.macos
String
display/display_server/driver.visionos
String
display/display_server/driver.windows
String
display/mouse_cursor/custom_image
Vector2
display/mouse_cursor/custom_image_hotspot
Vector2(0,0)
Vector2
display/mouse_cursor/tooltip_position_offset
Vector2(10,10)
bool
display/window/dpi/allow_hidpi
true
bool
display/window/energy_saving/keep_screen_on
true
bool
display/window/frame_pacing/android/enable_frame_pacing
true
display/window/frame_pacing/android/swappy_mode
display/window/handheld/orientation
bool
display/window/ios/allow_high_refresh_rate
true
bool
display/window/ios/hide_home_indicator
true
bool
display/window/ios/hide_status_bar
true
bool
display/window/ios/suppress_ui_gesture
true
bool
display/window/per_pixel_transparency/allowed
false
bool
display/window/size/always_on_top
false
bool
display/window/size/borderless
false
bool
display/window/size/extend_to_title
false
Vector2i
display/window/size/initial_position
Vector2i(0,0)
display/window/size/initial_position_type
display/window/size/initial_screen
bool
display/window/size/maximize_disabled
false
bool
display/window/size/minimize_disabled
false
display/window/size/mode
bool
display/window/size/no_focus
false
bool
display/window/size/resizable
true
bool
display/window/size/sharp_corners
false
bool
display/window/size/transparent
false
display/window/size/viewport_height
display/window/size/viewport_width
1152
display/window/size/window_height_override
display/window/size/window_width_override
String
display/window/stretch/aspect
"keep"
String
display/window/stretch/mode
"disabled"
float
display/window/stretch/scale
String
display/window/stretch/scale_mode
"fractional"
bool
display/window/subwindows/embed_subwindows
true
display/window/vsync/vsync_mode
String
dotnet/project/assembly_name
dotnet/project/assembly_reload_attempts
String
dotnet/project/solution_directory
bool
editor/export/convert_text_resources_to_binary
true
editor/import/atlas_max_width
2048
bool
editor/import/reimport_missing_imported_files
true
bool
editor/import/use_multiple_threads
true
editor/movie_writer/audio_bit_depth
bool
editor/movie_writer/disable_vsync
false
editor/movie_writer/fps
editor/movie_writer/mix_rate
48000
String
editor/movie_writer/movie_file
float
editor/movie_writer/ogv/audio_quality
editor/movie_writer/ogv/encoding_speed
editor/movie_writer/ogv/keyframe_interval
editor/movie_writer/speaker_mode
float
editor/movie_writer/video_quality
0.75
String
editor/naming/default_signal_callback_name
"_on_{node_name}_{signal_name}"
String
editor/naming/default_signal_callback_to_self_name
"_on_{signal_name}"
editor/naming/node_name_casing
editor/naming/node_name_num_separator
editor/naming/scene_name_casing
editor/naming/script_name_casing
String
editor/run/main_run_args
PackedStringArray
editor/script/search_in_file_extensions
String
editor/script/templates_search_path
"res://script_templates"
bool
editor/version_control/autoload_on_startup
false
String
editor/version_control/plugin_name
bool
filesystem/import/blender/enabled
true
bool
filesystem/import/blender/enabled.android
false
bool
filesystem/import/blender/enabled.web
false
bool
filesystem/import/fbx2gltf/enabled
true
bool
filesystem/import/fbx2gltf/enabled.android
false
bool
filesystem/import/fbx2gltf/enabled.web
false
gui/common/default_scroll_deadzone
gui/common/drag_threshold
gui/common/show_focus_state_on_pointer_event
bool
gui/common/snap_controls_to_pixels
true
gui/common/swap_cancel_ok
gui/common/text_edit_undo_stack_max_size
1024
bool
gui/fonts/dynamic_fonts/use_oversampling
true
String
gui/theme/custom
String
gui/theme/custom_font
gui/theme/default_font_antialiasing
bool
gui/theme/default_font_generate_mipmaps
false
gui/theme/default_font_hinting
bool
gui/theme/default_font_multichannel_signed_distance_field
false
gui/theme/default_font_subpixel_positioning
float
gui/theme/default_theme_scale
gui/theme/lcd_subpixel_layout
float
gui/timers/button_shortcut_feedback_highlight_time
gui/timers/incremental_search_max_interval_msec
2000
float
gui/timers/text_edit_idle_detect_sec
float
gui/timers/tooltip_delay_sec
float
gui/timers/tooltip_delay_sec.editor_hint
Dictionary
input/ui_accept
Dictionary
input/ui_accessibility_drag_and_drop
Dictionary
input/ui_cancel
Dictionary
input/ui_close_dialog
Dictionary
input/ui_close_dialog.macos
Dictionary
input/ui_colorpicker_delete_preset
Dictionary
input/ui_copy
Dictionary
input/ui_cut
Dictionary
input/ui_down
Dictionary
input/ui_end
Dictionary
input/ui_filedialog_delete
Dictionary
input/ui_filedialog_find
Dictionary
input/ui_filedialog_focus_path
Dictionary
input/ui_filedialog_focus_path.macos
Dictionary
input/ui_filedialog_refresh
Dictionary
input/ui_filedialog_show_hidden
Dictionary
input/ui_filedialog_up_one_level
Dictionary
input/ui_focus_mode
Dictionary
input/ui_focus_next
Dictionary
input/ui_focus_prev
Dictionary
input/ui_graph_delete
Dictionary
input/ui_graph_duplicate
Dictionary
input/ui_graph_follow_left
Dictionary
input/ui_graph_follow_left.macos
Dictionary
input/ui_graph_follow_right
Dictionary
input/ui_graph_follow_right.macos
Dictionary
input/ui_home
Dictionary
input/ui_left
Dictionary
input/ui_menu
Dictionary
input/ui_page_down
Dictionary
input/ui_page_up
Dictionary
input/ui_paste
Dictionary
input/ui_redo
Dictionary
input/ui_right
Dictionary
input/ui_select
Dictionary
input/ui_swap_input_direction
Dictionary
input/ui_text_add_selection_for_next_occurrence
Dictionary
input/ui_text_backspace
Dictionary
input/ui_text_backspace_all_to_left
Dictionary
input/ui_text_backspace_all_to_left.macos
Dictionary
input/ui_text_backspace_word
Dictionary
input/ui_text_backspace_word.macos
Dictionary
input/ui_text_caret_add_above
Dictionary
input/ui_text_caret_add_above.macos
Dictionary
input/ui_text_caret_add_below
Dictionary
input/ui_text_caret_add_below.macos
Dictionary
input/ui_text_caret_document_end
Dictionary
input/ui_text_caret_document_end.macos
Dictionary
input/ui_text_caret_document_start
Dictionary
input/ui_text_caret_document_start.macos
Dictionary
input/ui_text_caret_down
Dictionary
input/ui_text_caret_left
Dictionary
input/ui_text_caret_line_end
Dictionary
input/ui_text_caret_line_end.macos
Dictionary
input/ui_text_caret_line_start
Dictionary
input/ui_text_caret_line_start.macos
Dictionary
input/ui_text_caret_page_down
Dictionary
input/ui_text_caret_page_up
Dictionary
input/ui_text_caret_right
Dictionary
input/ui_text_caret_up
Dictionary
input/ui_text_caret_word_left
Dictionary
input/ui_text_caret_word_left.macos
Dictionary
input/ui_text_caret_word_right
Dictionary
input/ui_text_caret_word_right.macos
Dictionary
input/ui_text_clear_carets_and_selection
Dictionary
input/ui_text_completion_accept
Dictionary
input/ui_text_completion_query
Dictionary
input/ui_text_completion_replace
Dictionary
input/ui_text_dedent
Dictionary
input/ui_text_delete
Dictionary
input/ui_text_delete_all_to_right
Dictionary
input/ui_text_delete_all_to_right.macos
Dictionary
input/ui_text_delete_word
Dictionary
input/ui_text_delete_word.macos
Dictionary
input/ui_text_indent
Dictionary
input/ui_text_newline
Dictionary
input/ui_text_newline_above
Dictionary
input/ui_text_newline_blank
Dictionary
input/ui_text_scroll_down
Dictionary
input/ui_text_scroll_down.macos
Dictionary
input/ui_text_scroll_up
Dictionary
input/ui_text_scroll_up.macos
Dictionary
input/ui_text_select_all
Dictionary
input/ui_text_select_word_under_caret
Dictionary
input/ui_text_select_word_under_caret.macos
Dictionary
input/ui_text_skip_selection_for_next_occurrence
Dictionary
input/ui_text_submit
Dictionary
input/ui_text_toggle_insert_mode
Dictionary
input/ui_undo
Dictionary
input/ui_unicode_start
Dictionary
input/ui_up
bool
input_devices/buffering/agile_event_flushing
false
bool
input_devices/compatibility/legacy_just_pressed_behavior
false
String
input_devices/pen_tablet/driver
String
input_devices/pen_tablet/driver.windows
bool
input_devices/pointing/android/disable_scroll_deadzone
false
bool
input_devices/pointing/android/enable_long_press_as_right_click
false
bool
input_devices/pointing/android/enable_pan_and_scale_gestures
false
bool
input_devices/pointing/android/override_volume_buttons
false
input_devices/pointing/android/rotary_input_scroll_axis
bool
input_devices/pointing/emulate_mouse_from_touch
true
bool
input_devices/pointing/emulate_touch_from_mouse
false
bool
input_devices/sensors/enable_accelerometer
false
bool
input_devices/sensors/enable_gravity
false
bool
input_devices/sensors/enable_gyroscope
false
bool
input_devices/sensors/enable_magnetometer
false
String
internationalization/locale/fallback
"en"
bool
internationalization/locale/include_text_server_data
false
internationalization/locale/line_breaking_strictness
String
internationalization/locale/test
bool
internationalization/pseudolocalization/double_vowels
false
float
internationalization/pseudolocalization/expansion_ratio
bool
internationalization/pseudolocalization/fake_bidi
false
bool
internationalization/pseudolocalization/override
false
String
internationalization/pseudolocalization/prefix
bool
internationalization/pseudolocalization/replace_with_accents
true
bool
internationalization/pseudolocalization/skip_placeholders
true
String
internationalization/pseudolocalization/suffix
bool
internationalization/pseudolocalization/use_pseudolocalization
false
bool
internationalization/rendering/force_right_to_left_layout_direction
false
bool
internationalization/rendering/root_node_auto_translate
true
internationalization/rendering/root_node_layout_direction
String
internationalization/rendering/text_driver
String
layer_names/2d_navigation/layer_1
String
layer_names/2d_navigation/layer_2
String
layer_names/2d_navigation/layer_3
String
layer_names/2d_navigation/layer_4
String
layer_names/2d_navigation/layer_5
String
layer_names/2d_navigation/layer_6
String
layer_names/2d_navigation/layer_7
String
layer_names/2d_navigation/layer_8
String
layer_names/2d_navigation/layer_9
String
layer_names/2d_navigation/layer_10
String
layer_names/2d_navigation/layer_11
String
layer_names/2d_navigation/layer_12
String
layer_names/2d_navigation/layer_13
String
layer_names/2d_navigation/layer_14
String
layer_names/2d_navigation/layer_15
String
layer_names/2d_navigation/layer_16
String
layer_names/2d_navigation/layer_17
String
layer_names/2d_navigation/layer_18
String
layer_names/2d_navigation/layer_19
String
layer_names/2d_navigation/layer_20
String
layer_names/2d_navigation/layer_21
String
layer_names/2d_navigation/layer_22
String
layer_names/2d_navigation/layer_23
String
layer_names/2d_navigation/layer_24
String
layer_names/2d_navigation/layer_25
String
layer_names/2d_navigation/layer_26
String
layer_names/2d_navigation/layer_27
String
layer_names/2d_navigation/layer_28
String
layer_names/2d_navigation/layer_29
String
layer_names/2d_navigation/layer_30
String
layer_names/2d_navigation/layer_31
String
layer_names/2d_navigation/layer_32
String
layer_names/2d_physics/layer_1
String
layer_names/2d_physics/layer_2
String
layer_names/2d_physics/layer_3
String
layer_names/2d_physics/layer_4
String
layer_names/2d_physics/layer_5
String
layer_names/2d_physics/layer_6
String
layer_names/2d_physics/layer_7
String
layer_names/2d_physics/layer_8
String
layer_names/2d_physics/layer_9
String
layer_names/2d_physics/layer_10
String
layer_names/2d_physics/layer_11
String
layer_names/2d_physics/layer_12
String
layer_names/2d_physics/layer_13
String
layer_names/2d_physics/layer_14
String
layer_names/2d_physics/layer_15
String
layer_names/2d_physics/layer_16
String
layer_names/2d_physics/layer_17
String
layer_names/2d_physics/layer_18
String
layer_names/2d_physics/layer_19
String
layer_names/2d_physics/layer_20
String
layer_names/2d_physics/layer_21
String
layer_names/2d_physics/layer_22
String
layer_names/2d_physics/layer_23
String
layer_names/2d_physics/layer_24
String
layer_names/2d_physics/layer_25
String
layer_names/2d_physics/layer_26
String
layer_names/2d_physics/layer_27
String
layer_names/2d_physics/layer_28
String
layer_names/2d_physics/layer_29
String
layer_names/2d_physics/layer_30
String
layer_names/2d_physics/layer_31
String
layer_names/2d_physics/layer_32
String
layer_names/2d_render/layer_1
String
layer_names/2d_render/layer_2
String
layer_names/2d_render/layer_3
String
layer_names/2d_render/layer_4
String
layer_names/2d_render/layer_5
String
layer_names/2d_render/layer_6
String
layer_names/2d_render/layer_7
String
layer_names/2d_render/layer_8
String
layer_names/2d_render/layer_9
String
layer_names/2d_render/layer_10
String
layer_names/2d_render/layer_11
String
layer_names/2d_render/layer_12
String
layer_names/2d_render/layer_13
String
layer_names/2d_render/layer_14
String
layer_names/2d_render/layer_15
String
layer_names/2d_render/layer_16
String
layer_names/2d_render/layer_17
String
layer_names/2d_render/layer_18
String
layer_names/2d_render/layer_19
String
layer_names/2d_render/layer_20
String
layer_names/3d_navigation/layer_1
String
layer_names/3d_navigation/layer_2
String
layer_names/3d_navigation/layer_3
String
layer_names/3d_navigation/layer_4
String
layer_names/3d_navigation/layer_5
String
layer_names/3d_navigation/layer_6
String
layer_names/3d_navigation/layer_7
String
layer_names/3d_navigation/layer_8
String
layer_names/3d_navigation/layer_9
String
layer_names/3d_navigation/layer_10
String
layer_names/3d_navigation/layer_11
String
layer_names/3d_navigation/layer_12
String
layer_names/3d_navigation/layer_13
String
layer_names/3d_navigation/layer_14
String
layer_names/3d_navigation/layer_15
String
layer_names/3d_navigation/layer_16
String
layer_names/3d_navigation/layer_17
String
layer_names/3d_navigation/layer_18
String
layer_names/3d_navigation/layer_19
String
layer_names/3d_navigation/layer_20
String
layer_names/3d_navigation/layer_21
String
layer_names/3d_navigation/layer_22
String
layer_names/3d_navigation/layer_23
String
layer_names/3d_navigation/layer_24
String
layer_names/3d_navigation/layer_25
String
layer_names/3d_navigation/layer_26
String
layer_names/3d_navigation/layer_27
String
layer_names/3d_navigation/layer_28
String
layer_names/3d_navigation/layer_29
String
layer_names/3d_navigation/layer_30
String
layer_names/3d_navigation/layer_31
String
layer_names/3d_navigation/layer_32
String
layer_names/3d_physics/layer_1
String
layer_names/3d_physics/layer_2
String
layer_names/3d_physics/layer_3
String
layer_names/3d_physics/layer_4
String
layer_names/3d_physics/layer_5
String
layer_names/3d_physics/layer_6
String
layer_names/3d_physics/layer_7
String
layer_names/3d_physics/layer_8
String
layer_names/3d_physics/layer_9
String
layer_names/3d_physics/layer_10
String
layer_names/3d_physics/layer_11
String
layer_names/3d_physics/layer_12
String
layer_names/3d_physics/layer_13
String
layer_names/3d_physics/layer_14
String
layer_names/3d_physics/layer_15
String
layer_names/3d_physics/layer_16
String
layer_names/3d_physics/layer_17
String
layer_names/3d_physics/layer_18
String
layer_names/3d_physics/layer_19
String
layer_names/3d_physics/layer_20
String
layer_names/3d_physics/layer_21
String
layer_names/3d_physics/layer_22
String
layer_names/3d_physics/layer_23
String
layer_names/3d_physics/layer_24
String
layer_names/3d_physics/layer_25
String
layer_names/3d_physics/layer_26
String
layer_names/3d_physics/layer_27
String
layer_names/3d_physics/layer_28
String
layer_names/3d_physics/layer_29
String
layer_names/3d_physics/layer_30
String
layer_names/3d_physics/layer_31
String
layer_names/3d_physics/layer_32
String
layer_names/3d_render/layer_1
String
layer_names/3d_render/layer_2
String
layer_names/3d_render/layer_3
String
layer_names/3d_render/layer_4
String
layer_names/3d_render/layer_5
String
layer_names/3d_render/layer_6
String
layer_names/3d_render/layer_7
String
layer_names/3d_render/layer_8
String
layer_names/3d_render/layer_9
String
layer_names/3d_render/layer_10
String
layer_names/3d_render/layer_11
String
layer_names/3d_render/layer_12
String
layer_names/3d_render/layer_13
String
layer_names/3d_render/layer_14
String
layer_names/3d_render/layer_15
String
layer_names/3d_render/layer_16
String
layer_names/3d_render/layer_17
String
layer_names/3d_render/layer_18
String
layer_names/3d_render/layer_19
String
layer_names/3d_render/layer_20
String
layer_names/avoidance/layer_1
String
layer_names/avoidance/layer_2
String
layer_names/avoidance/layer_3
String
layer_names/avoidance/layer_4
String
layer_names/avoidance/layer_5
String
layer_names/avoidance/layer_6
String
layer_names/avoidance/layer_7
String
layer_names/avoidance/layer_8
String
layer_names/avoidance/layer_9
String
layer_names/avoidance/layer_10
String
layer_names/avoidance/layer_11
String
layer_names/avoidance/layer_12
String
layer_names/avoidance/layer_13
String
layer_names/avoidance/layer_14
String
layer_names/avoidance/layer_15
String
layer_names/avoidance/layer_16
String
layer_names/avoidance/layer_17
String
layer_names/avoidance/layer_18
String
layer_names/avoidance/layer_19
String
layer_names/avoidance/layer_20
String
layer_names/avoidance/layer_21
String
layer_names/avoidance/layer_22
String
layer_names/avoidance/layer_23
String
layer_names/avoidance/layer_24
String
layer_names/avoidance/layer_25
String
layer_names/avoidance/layer_26
String
layer_names/avoidance/layer_27
String
layer_names/avoidance/layer_28
String
layer_names/avoidance/layer_29
String
layer_names/avoidance/layer_30
String
layer_names/avoidance/layer_31
String
layer_names/avoidance/layer_32
memory/limits/message_queue/max_size_mb
float
navigation/2d/default_cell_size
float
navigation/2d/default_edge_connection_margin
float
navigation/2d/default_link_connection_radius
float
navigation/2d/merge_rasterizer_cell_scale
String
navigation/2d/navigation_engine
"DEFAULT"
bool
navigation/2d/use_edge_connections
true
bool
navigation/2d/warnings/navmesh_cell_size_mismatch
true
bool
navigation/2d/warnings/navmesh_edge_merge_errors
true
float
navigation/3d/default_cell_height
0.25
float
navigation/3d/default_cell_size
0.25
float
navigation/3d/default_edge_connection_margin
0.25
float
navigation/3d/default_link_connection_radius
Vector3
navigation/3d/default_up
Vector3(0,1,0)
float
navigation/3d/merge_rasterizer_cell_scale
String
navigation/3d/navigation_engine
"DEFAULT"
bool
navigation/3d/use_edge_connections
true
bool
navigation/3d/warnings/navmesh_cell_size_mismatch
true
bool
navigation/3d/warnings/navmesh_edge_merge_errors
true
bool
navigation/avoidance/thread_model/avoidance_use_high_priority_threads
true
bool
navigation/avoidance/thread_model/avoidance_use_multiple_threads
true
bool
navigation/baking/thread_model/baking_use_high_priority_threads
true
bool
navigation/baking/thread_model/baking_use_multiple_threads
true
bool
navigation/baking/use_crash_prevention_checks
true
navigation/pathfinding/max_threads
bool
navigation/world/map_use_async_iterations
true
bool
navigation/world/region_use_async_iterations
true
network/limits/debugger/max_chars_per_second
32768
network/limits/debugger/max_errors_per_second
network/limits/debugger/max_queued_messages
2048
network/limits/debugger/max_warnings_per_second
network/limits/packet_peer_stream/max_buffer_po2
network/limits/tcp/connect_timeout_seconds
network/limits/unix/connect_timeout_seconds
network/limits/webrtc/max_channel_in_buffer_kb
String
network/tls/certificate_bundle_override
bool
network/tls/enable_tls_v1.3
true
float
physics/2d/default_angular_damp
float
physics/2d/default_gravity
980.0
Vector2
physics/2d/default_gravity_vector
Vector2(0,1)
float
physics/2d/default_linear_damp
String
physics/2d/physics_engine
"DEFAULT"
bool
physics/2d/run_on_separate_thread
false
float
physics/2d/sleep_threshold_angular
0.13962634
float
physics/2d/sleep_threshold_linear
float
physics/2d/solver/contact_max_allowed_penetration
float
physics/2d/solver/contact_max_separation
float
physics/2d/solver/contact_recycle_radius
float
physics/2d/solver/default_constraint_bias
float
physics/2d/solver/default_contact_bias
physics/2d/solver/solver_iterations
float
physics/2d/time_before_sleep
float
physics/3d/default_angular_damp
float
physics/3d/default_gravity
Vector3
physics/3d/default_gravity_vector
Vector3(0,-1,0)
float
physics/3d/default_linear_damp
String
physics/3d/physics_engine
"DEFAULT"
String
physics/3d/physics_interpolation/scene_traversal
"DEFAULT"
bool
physics/3d/run_on_separate_thread
false
float
physics/3d/sleep_threshold_angular
0.13962634
float
physics/3d/sleep_threshold_linear
float
physics/3d/solver/contact_max_allowed_penetration
0.01
float
physics/3d/solver/contact_max_separation
0.05
float
physics/3d/solver/contact_recycle_radius
0.01
float
physics/3d/solver/default_contact_bias
physics/3d/solver/solver_iterations
float
physics/3d/time_before_sleep
bool
physics/common/enable_object_picking
true
physics/common/max_physics_steps_per_frame
bool
physics/common/physics_interpolation
false
float
physics/common/physics_jitter_fix
physics/common/physics_ticks_per_second
float
physics/jolt_physics_3d/collisions/active_edge_threshold
0.87266463
float
physics/jolt_physics_3d/collisions/collision_margin_fraction
0.08
physics/jolt_physics_3d/joints/world_node
float
physics/jolt_physics_3d/limits/max_angular_velocity
47.12389
physics/jolt_physics_3d/limits/max_bodies
10240
physics/jolt_physics_3d/limits/max_body_pairs
65536
physics/jolt_physics_3d/limits/max_contact_constraints
20480
float
physics/jolt_physics_3d/limits/max_linear_velocity
500.0
physics/jolt_physics_3d/limits/temporary_memory_buffer_size
float
physics/jolt_physics_3d/limits/world_boundary_shape_size
2000.0
float
physics/jolt_physics_3d/motion_queries/recovery_amount
physics/jolt_physics_3d/motion_queries/recovery_iterations
bool
physics/jolt_physics_3d/motion_queries/use_enhanced_internal_edge_removal
true
bool
physics/jolt_physics_3d/queries/enable_ray_cast_face_index
false
bool
physics/jolt_physics_3d/queries/use_enhanced_internal_edge_removal
false
bool
physics/jolt_physics_3d/simulation/allow_sleep
true
float
physics/jolt_physics_3d/simulation/baumgarte_stabilization_factor
float
physics/jolt_physics_3d/simulation/body_pair_contact_cache_angle_threshold
0.034906585
float
physics/jolt_physics_3d/simulation/body_pair_contact_cache_distance_threshold
0.001
bool
physics/jolt_physics_3d/simulation/body_pair_contact_cache_enabled
true
float
physics/jolt_physics_3d/simulation/bounce_velocity_threshold
float
physics/jolt_physics_3d/simulation/continuous_cd_max_penetration
0.25
float
physics/jolt_physics_3d/simulation/continuous_cd_movement_threshold
0.75
bool
physics/jolt_physics_3d/simulation/generate_all_kinematic_contacts
false
float
physics/jolt_physics_3d/simulation/penetration_slop
0.02
physics/jolt_physics_3d/simulation/position_steps
float
physics/jolt_physics_3d/simulation/sleep_time_threshold
float
physics/jolt_physics_3d/simulation/sleep_velocity_threshold
0.03
float
physics/jolt_physics_3d/simulation/soft_body_point_radius
0.01
float
physics/jolt_physics_3d/simulation/speculative_contact_distance
0.02
bool
physics/jolt_physics_3d/simulation/use_enhanced_internal_edge_removal
true
physics/jolt_physics_3d/simulation/velocity_steps
rendering/2d/batching/item_buffer_size
16384
rendering/2d/batching/uniform_set_cache_size
4096
rendering/2d/sdf/oversize
rendering/2d/sdf/scale
rendering/2d/shadow_atlas/size
2048
bool
rendering/2d/snap/snap_2d_transforms_to_pixel
false
bool
rendering/2d/snap/snap_2d_vertices_to_pixel
false
rendering/anti_aliasing/quality/msaa_2d
rendering/anti_aliasing/quality/msaa_3d
rendering/anti_aliasing/quality/screen_space_aa
float
rendering/anti_aliasing/quality/smaa_edge_detection_threshold
0.05
bool
rendering/anti_aliasing/quality/use_debanding
false
bool
rendering/anti_aliasing/quality/use_taa
false
float
rendering/anti_aliasing/screen_space_roughness_limiter/amount
0.25
bool
rendering/anti_aliasing/screen_space_roughness_limiter/enabled
true
float
rendering/anti_aliasing/screen_space_roughness_limiter/limit
0.18
rendering/camera/depth_of_field/depth_of_field_bokeh_quality
rendering/camera/depth_of_field/depth_of_field_bokeh_shape
bool
rendering/camera/depth_of_field/depth_of_field_use_jitter
false
String
rendering/driver/depth_prepass/disable_for_vendors
"PowerVR,Mali,Adreno,Apple"
bool
rendering/driver/depth_prepass/enable
true
rendering/driver/threads/thread_model
Color
rendering/environment/defaults/default_clear_color
Color(0.3,0.3,0.3,1)
String
rendering/environment/defaults/default_environment
rendering/environment/glow/upscale_mode
rendering/environment/glow/upscale_mode.mobile
bool
rendering/environment/screen_space_reflection/half_size
true
float
rendering/environment/ssao/adaptive_target
rendering/environment/ssao/blur_passes
float
rendering/environment/ssao/fadeout_from
50.0
float
rendering/environment/ssao/fadeout_to
300.0
bool
rendering/environment/ssao/half_size
true
rendering/environment/ssao/quality
float
rendering/environment/ssil/adaptive_target
rendering/environment/ssil/blur_passes
float
rendering/environment/ssil/fadeout_from
50.0
float
rendering/environment/ssil/fadeout_to
300.0
bool
rendering/environment/ssil/half_size
true
rendering/environment/ssil/quality
float
rendering/environment/subsurface_scattering/subsurface_scattering_depth_scale
0.01
rendering/environment/subsurface_scattering/subsurface_scattering_quality
float
rendering/environment/subsurface_scattering/subsurface_scattering_scale
0.05
rendering/environment/volumetric_fog/use_filter
rendering/environment/volumetric_fog/volume_depth
rendering/environment/volumetric_fog/volume_size
String
rendering/gl_compatibility/driver
"opengl3"
String
rendering/gl_compatibility/driver.android
"opengl3"
String
rendering/gl_compatibility/driver.ios
"opengl3"
String
rendering/gl_compatibility/driver.linuxbsd
"opengl3"
String
rendering/gl_compatibility/driver.macos
"opengl3"
String
rendering/gl_compatibility/driver.web
"opengl3"
String
rendering/gl_compatibility/driver.windows
"opengl3"
bool
rendering/gl_compatibility/fallback_to_angle
true
bool
rendering/gl_compatibility/fallback_to_gles
true
bool
rendering/gl_compatibility/fallback_to_native
true
Array
rendering/gl_compatibility/force_angle_on_devices
rendering/gl_compatibility/item_buffer_size
16384
bool
rendering/gl_compatibility/nvidia_disable_threaded_optimization
true
bool
rendering/global_illumination/gi/use_half_resolution
false
rendering/global_illumination/sdfgi/frames_to_converge
rendering/global_illumination/sdfgi/frames_to_update_lights
rendering/global_illumination/sdfgi/probe_ray_count
rendering/global_illumination/voxel_gi/quality
rendering/lightmapping/bake_performance/max_rays_per_pass
rendering/lightmapping/bake_performance/max_rays_per_probe_pass
rendering/lightmapping/bake_performance/max_transparency_rays
rendering/lightmapping/bake_performance/region_size
rendering/lightmapping/bake_quality/high_quality_probe_ray_count
rendering/lightmapping/bake_quality/high_quality_ray_count
rendering/lightmapping/bake_quality/low_quality_probe_ray_count
rendering/lightmapping/bake_quality/low_quality_ray_count
rendering/lightmapping/bake_quality/medium_quality_probe_ray_count
rendering/lightmapping/bake_quality/medium_quality_ray_count
rendering/lightmapping/bake_quality/ultra_quality_probe_ray_count
2048
rendering/lightmapping/bake_quality/ultra_quality_ray_count
2048
rendering/lightmapping/denoising/denoiser
bool
rendering/lightmapping/lightmap_gi/use_bicubic_filter
true
float
rendering/lightmapping/primitive_meshes/texel_size
float
rendering/lightmapping/probe_capture/update_speed
bool
rendering/lights_and_shadows/directional_shadow/16_bits
true
rendering/lights_and_shadows/directional_shadow/size
4096
rendering/lights_and_shadows/directional_shadow/size.mobile
2048
rendering/lights_and_shadows/directional_shadow/soft_shadow_filter_quality
rendering/lights_and_shadows/directional_shadow/soft_shadow_filter_quality.mobile
bool
rendering/lights_and_shadows/positional_shadow/atlas_16_bits
true
rendering/lights_and_shadows/positional_shadow/atlas_quadrant_0_subdiv
rendering/lights_and_shadows/positional_shadow/atlas_quadrant_1_subdiv
rendering/lights_and_shadows/positional_shadow/atlas_quadrant_2_subdiv
rendering/lights_and_shadows/positional_shadow/atlas_quadrant_3_subdiv
rendering/lights_and_shadows/positional_shadow/atlas_size
4096
rendering/lights_and_shadows/positional_shadow/atlas_size.mobile
2048
rendering/lights_and_shadows/positional_shadow/soft_shadow_filter_quality
rendering/lights_and_shadows/positional_shadow/soft_shadow_filter_quality.mobile
bool
rendering/lights_and_shadows/tighter_shadow_caster_culling
true
bool
rendering/lights_and_shadows/use_physical_light_units
false
float
rendering/limits/cluster_builder/max_clustered_elements
rendering/limits/global_shader_variables/buffer_size
65536
rendering/limits/opengl/max_lights_per_object
rendering/limits/opengl/max_renderable_elements
65536
rendering/limits/opengl/max_renderable_lights
rendering/limits/spatial_indexer/threaded_cull_minimum_instances
1000
rendering/limits/spatial_indexer/update_iterations_per_frame
float
rendering/limits/time/time_rollover_secs
3600
float
rendering/mesh_lod/lod_change/threshold_pixels
rendering/occlusion_culling/bvh_build_quality
bool
rendering/occlusion_culling/jitter_projection
true
rendering/occlusion_culling/occlusion_rays_per_thread
bool
rendering/occlusion_culling/use_occlusion_culling
false
rendering/reflections/reflection_atlas/reflection_count
rendering/reflections/reflection_atlas/reflection_size
rendering/reflections/reflection_atlas/reflection_size.mobile
bool
rendering/reflections/sky_reflections/fast_filter_high_quality
false
rendering/reflections/sky_reflections/ggx_samples
rendering/reflections/sky_reflections/ggx_samples.mobile
rendering/reflections/sky_reflections/roughness_layers
bool
rendering/reflections/sky_reflections/texture_array_reflections
true
bool
rendering/reflections/sky_reflections/texture_array_reflections.mobile
false
bool
rendering/reflections/specular_occlusion/enabled
true
String
rendering/renderer/rendering_method
"forward_plus"
String
rendering/renderer/rendering_method.mobile
"mobile"
String
rendering/renderer/rendering_method.web
"gl_compatibility"
rendering/rendering_device/d3d12/agility_sdk_version
rendering/rendering_device/d3d12/max_resource_descriptors
65536
rendering/rendering_device/d3d12/max_sampler_descriptors
1024
String
rendering/rendering_device/driver
"vulkan"
String
rendering/rendering_device/driver.android
"vulkan"
String
rendering/rendering_device/driver.ios
"metal"
String
rendering/rendering_device/driver.linuxbsd
"vulkan"
String
rendering/rendering_device/driver.macos
"metal"
String
rendering/rendering_device/driver.visionos
"metal"
String
rendering/rendering_device/driver.windows
"vulkan"
bool
rendering/rendering_device/fallback_to_d3d12
true
bool
rendering/rendering_device/fallback_to_opengl3
true
bool
rendering/rendering_device/fallback_to_vulkan
true
bool
rendering/rendering_device/pipeline_cache/enable
true
float
rendering/rendering_device/pipeline_cache/save_chunk_size_mb
rendering/rendering_device/staging_buffer/block_size_kb
rendering/rendering_device/staging_buffer/max_size_mb
rendering/rendering_device/staging_buffer/texture_download_region_size_px
rendering/rendering_device/staging_buffer/texture_upload_region_size_px
rendering/rendering_device/vsync/frame_queue_size
rendering/rendering_device/vsync/swapchain_image_count
rendering/rendering_device/vulkan/max_descriptors_per_pool
float
rendering/scaling_3d/fsr_sharpness
rendering/scaling_3d/mode
rendering/scaling_3d/mode.ios
rendering/scaling_3d/mode.macos
float
rendering/scaling_3d/scale
bool
rendering/shader_compiler/shader_cache/compress
true
bool
rendering/shader_compiler/shader_cache/enabled
true
bool
rendering/shader_compiler/shader_cache/strip_debug
false
bool
rendering/shader_compiler/shader_cache/strip_debug.release
true
bool
rendering/shader_compiler/shader_cache/use_zstd_compression
true
bool
rendering/shading/overrides/force_lambert_over_burley
false
bool
rendering/shading/overrides/force_lambert_over_burley.mobile
true
bool
rendering/shading/overrides/force_vertex_shading
false
rendering/textures/basis_universal/rdo_dict_size
1024
bool
rendering/textures/basis_universal/zstd_supercompression
true
rendering/textures/basis_universal/zstd_supercompression_level
rendering/textures/canvas_textures/default_texture_filter
rendering/textures/canvas_textures/default_texture_repeat
rendering/textures/decals/filter
rendering/textures/default_filters/anisotropic_filtering_level
float
rendering/textures/default_filters/texture_mipmap_bias
bool
rendering/textures/default_filters/use_nearest_mipmap_filter
false
rendering/textures/light_projectors/filter
bool
rendering/textures/lossless_compression/force_png
false
bool
rendering/textures/vram_compression/cache_gpu_compressor
true
bool
rendering/textures/vram_compression/compress_with_gpu
true
bool
rendering/textures/vram_compression/import_etc2_astc
false
bool
rendering/textures/vram_compression/import_s3tc_bptc
false
rendering/textures/webp_compression/compression_method
float
rendering/textures/webp_compression/lossless_compression_factor
bool
rendering/viewport/hdr_2d
false
bool
rendering/viewport/transparent_background
false
rendering/vrs/mode
String
rendering/vrs/texture
float
threading/worker_pool/low_priority_thread_ratio
threading/worker_pool/max_threads
bool
xr/openxr/binding_modifiers/analog_threshold
false
bool
xr/openxr/binding_modifiers/dpad_binding
false
String
xr/openxr/default_action_map
"res://openxr_action_map.tres"
bool
xr/openxr/enabled
false
xr/openxr/environment_blend_mode
xr/openxr/extensions/debug_message_types
"15"
xr/openxr/extensions/debug_utils
bool
xr/openxr/extensions/eye_gaze_interaction
false
bool
xr/openxr/extensions/frame_synthesis
false
bool
xr/openxr/extensions/hand_interaction_profile
false
bool
xr/openxr/extensions/hand_tracking
false
bool
xr/openxr/extensions/hand_tracking_controller_data_source
false
bool
xr/openxr/extensions/hand_tracking_unobstructed_data_source
false
bool
xr/openxr/extensions/render_model
false
xr/openxr/extensions/spatial_entity/april_tag_dict
xr/openxr/extensions/spatial_entity/aruco_dict
"15"
bool
xr/openxr/extensions/spatial_entity/enable_builtin_anchor_detection
false
bool
xr/openxr/extensions/spatial_entity/enable_builtin_marker_tracking
false
bool
xr/openxr/extensions/spatial_entity/enable_builtin_plane_detection
false
bool
xr/openxr/extensions/spatial_entity/enable_marker_tracking
false
bool
xr/openxr/extensions/spatial_entity/enable_persistent_anchors
false
bool
xr/openxr/extensions/spatial_entity/enable_plane_tracking
false
bool
xr/openxr/extensions/spatial_entity/enable_spatial_anchors
false
bool
xr/openxr/extensions/spatial_entity/enabled
false
xr/openxr/form_factor
bool
xr/openxr/foveation_dynamic
false
xr/openxr/foveation_level
xr/openxr/reference_space
bool
xr/openxr/startup_alert
true
bool
xr/openxr/submit_depth_buffer
false
String
xr/openxr/target_api_version
xr/openxr/view_configuration
bool
xr/shaders/enabled
false

## Methods

| void | add_property_info(hint:Dictionary) |
|---|---|
| bool | check_changed_settings_in_group(setting_prefix:String)const |
| void | clear(name:String) |
| PackedStringArray | get_changed_settings()const |
| Array[Dictionary] | get_global_class_list() |
| int | get_order(name:String)const |
| Variant | get_setting(name:String, default_value:Variant= null)const |
| Variant | get_setting_with_override(name:StringName)const |
| Variant | get_setting_with_override_and_custom_features(name:StringName, features:PackedStringArray)const |
| String | globalize_path(path:String)const |
| bool | has_setting(name:String)const |
| bool | load_resource_pack(pack:String, replace_files:bool= true, offset:int= 0) |
| String | localize_path(path:String)const |
| Error | save() |
| Error | save_custom(file:String) |
| void | set_as_basic(name:String, basic:bool) |
| void | set_as_internal(name:String, internal:bool) |
| void | set_initial_value(name:String, value:Variant) |
| void | set_order(name:String, position:int) |
| void | set_restart_if_changed(name:String, restart:bool) |
| void | set_setting(name:String, value:Variant) |

void
add_property_info(hint:Dictionary)
bool
check_changed_settings_in_group(setting_prefix:String)const
void
clear(name:String)
PackedStringArray
get_changed_settings()const
Array[Dictionary]
get_global_class_list()
get_order(name:String)const
Variant
get_setting(name:String, default_value:Variant= null)const
Variant
get_setting_with_override(name:StringName)const
Variant
get_setting_with_override_and_custom_features(name:StringName, features:PackedStringArray)const
String
globalize_path(path:String)const
bool
has_setting(name:String)const
bool
load_resource_pack(pack:String, replace_files:bool= true, offset:int= 0)
String
localize_path(path:String)const
Error
save()
Error
save_custom(file:String)
void
set_as_basic(name:String, basic:bool)
void
set_as_internal(name:String, internal:bool)
void
set_initial_value(name:String, value:Variant)
void
set_order(name:String, position:int)
void
set_restart_if_changed(name:String, restart:bool)
void
set_setting(name:String, value:Variant)

## Signals

settings_changed()🔗
Emitted when any setting is changed, up to once per process frame.

## Property Descriptions

intaccessibility/general/accessibility_support=0🔗
Accessibility support mode:

- Auto(0): Accessibility support is enabled, but updates to the accessibility information are processed only if an assistive app (such as a screen reader or a Braille display) is active (default).
Auto(0): Accessibility support is enabled, but updates to the accessibility information are processed only if an assistive app (such as a screen reader or a Braille display) is active (default).
- Always Active(1): Accessibility support is enabled, and updates to the accessibility information are always processed, regardless of the status of assistive apps.
Always Active(1): Accessibility support is enabled, and updates to the accessibility information are always processed, regardless of the status of assistive apps.
- Disabled(2): Accessibility support is fully disabled.
Disabled(2): Accessibility support is fully disabled.
Note:Accessibility debugging tools, such as Accessibility Insights for Windows, Accessibility Inspector (macOS), or AT-SPI Browser (Linux/BSD), do not count as assistive apps. To test your project with these tools, useAlways Active.
intaccessibility/general/updates_per_second=60🔗
The number of accessibility information updates per second.
boolanimation/compatibility/default_parent_skeleton_in_mesh_instance_3d=false🔗
Iftrue,MeshInstance3D.skeletonwill point to the parent node (..) by default, which was the behavior before Godot 4.6. It's recommended to keep this setting disabled unless the old behavior is needed for compatibility.
Note:If you disable this option in an existing project, it's strongly recommended to use theProject>Tools>UpgradeProjectFiles...option to ensure existing scenes do not break.
boolanimation/warnings/check_angle_interpolation_type_conflicting=true🔗
Iftrue,AnimationMixerprints the warning of interpolation being forced to choose the shortest rotation path due to multiple angle interpolation types being mixed in theAnimationMixercache.
boolanimation/warnings/check_invalid_track_paths=true🔗
Iftrue,AnimationMixerprints the warning of no matching object of the track path in the scene.
Colorapplication/boot_splash/bg_color=Color(0.14,0.14,0.14,1)🔗
Background color for the boot splash.
Stringapplication/boot_splash/image=""🔗
Path to an image used as the boot splash. If left empty, the default Godot Engine splash will be displayed instead.
Note:Only effective ifapplication/boot_splash/show_imageistrue.
Note:The only supported format is PNG. Using another image format will result in an error.
Note:The image will also show when opening the project in the editor. If you want to display the default splash image in the editor, add an empty override foreditor_hintfeature.
intapplication/boot_splash/minimum_display_time=0🔗
Minimum boot splash display time (in milliseconds). It is not recommended to set too high values for this setting.
boolapplication/boot_splash/show_image=true🔗
Iftrue, displays the image specified inapplication/boot_splash/imagewhen the engine starts. Iffalse, only displays the plain color specified inapplication/boot_splash/bg_color.
intapplication/boot_splash/stretch_mode=1🔗
Specifies how the splash image will be stretched. For the original size without stretching, set to disabled. SeeSplashStretchModeconstants for more information.
boolapplication/boot_splash/use_filter=true🔗
Iftrue, applies linear filtering when scaling the image (recommended for high-resolution artwork). Iffalse, uses nearest-neighbor interpolation (recommended for pixel art).
boolapplication/config/auto_accept_quit=true🔗
Iftrue, the application automatically accepts quitting requests.
Stringapplication/config/custom_user_dir_name=""🔗
This user directory is used for storing persistent data (user://filesystem). If a custom directory name is defined, this name will be appended to the system-specific user data directory (same parent folder as the Godot configuration folder documented inOS.get_user_data_dir()).
Theapplication/config/use_custom_user_dirsetting must be enabled for this to take effect.
Note:Ifapplication/config/custom_user_dir_namecontains trailing periods, they will be stripped as folder names ending with a period are not allowed on Windows.
Stringapplication/config/description=""🔗
The project's description, displayed as a tooltip in the Project Manager when hovering the project.
boolapplication/config/disable_project_settings_override=false🔗
Iftrue, disables loading of project settings overrides (file defined inapplication/config/project_settings_overrideandres://override.cfg) and related CLI arguments.
Stringapplication/config/icon=""🔗
Icon used for the project, set when project loads. Exporters will also use this icon as a fallback if necessary.
Stringapplication/config/macos_native_icon=""🔗
Icon set in.icnsformat used on macOS to set the game's icon. This is done automatically on start by callingDisplayServer.set_native_icon().
Stringapplication/config/name=""🔗
The project's name. It is used both by the Project Manager and by exporters. The project name can be translated by translating its value in localization files. The window title will be set to match the project name automatically on startup.
Note:Changing this value will also change the user data folder's path ifapplication/config/use_custom_user_dirisfalse. After renaming the project, you will no longer be able to access existing data inuser://unless you rename the old folder to match the new project name. SeeData pathsin the documentation for more information.
Dictionaryapplication/config/name_localized={}🔗
Translations of the project's name. This setting is used by OS tools to translate application name on Android, iOS and macOS.
Note:When left empty, the application name is translated using the project translations.
Stringapplication/config/project_settings_override=""🔗
Specifies a file to override project settings. For example:user://custom_settings.cfg. See "Overriding" in theProjectSettingsclass description at the top for more information.
Note:Regardless of this setting's value,res://override.cfgwill still be read to override the project settings.
boolapplication/config/quit_on_go_back=true🔗
Iftrue, the application quits automatically when navigating back (e.g. using the system "Back" button on Android).
boolapplication/config/use_custom_user_dir=false🔗
Iftrue, the project will save user data to its own user directory. Ifapplication/config/custom_user_dir_nameis empty,<OSuserdatadirectory>/<projectname>directory will be used. Iffalse, the project will save user data to<OSuserdatadirectory>/Godot/app_userdata/<projectname>.
See alsoFile paths in Godot projects. This setting is only effective on desktop platforms.
boolapplication/config/use_hidden_project_data_directory=true🔗
Iftrue, the project will use a hidden directory (.godot) for storing project-specific data (metadata, shader cache, etc.).
Iffalse, a non-hidden directory (godot) will be used instead.
Note:Restart the application after changing this setting.
Note:Changing this value can help on platforms or with third-party tools where hidden directory patterns are disallowed. Only modify this setting if you know that your environment requires it, as changing the default can impact compatibility with some external tools or plugins which expect the default.godotfolder.
Stringapplication/config/version=""🔗
The project's human-readable version identifier. This is used by exporters if the version identifier isn't overridden there. Ifapplication/config/versionis an empty string and the version identifier isn't overridden in an exporter, the exporter will use1.0.0as a version identifier.
Stringapplication/config/windows_native_icon=""🔗
Icon set in.icoformat used on Windows to set the game's icon. This is done automatically on start by callingDisplayServer.set_native_icon().
boolapplication/run/delta_smoothing=true🔗
Time samples for frame deltas are subject to random variation introduced by the platform, even when frames are displayed at regular intervals thanks to V-Sync. This can lead to jitter. Delta smoothing can often give a better result by filtering the input deltas to correct for minor fluctuations from the refresh rate.
Note:Delta smoothing is only attempted whendisplay/window/vsync/vsync_modeis set toenabled, as it does not work well without V-Sync.
It may take several seconds at a stable frame rate before the smoothing is initially activated. It will only be active on machines where performance is adequate to render frames at the refresh rate.
boolapplication/run/disable_stderr=false🔗
Iftrue, disables printing to standard error. Iftrue, this also hides error and warning messages printed by@GlobalScope.push_error()and@GlobalScope.push_warning(). See alsoapplication/run/disable_stdout.
Changes to this setting will only be applied upon restarting the application. To control this at runtime, useEngine.print_error_messages.
boolapplication/run/disable_stdout=false🔗
Iftrue, disables printing to standard output. This is equivalent to starting the editor or project with the--quietcommand line argument. See alsoapplication/run/disable_stderr.
Changes to this setting will only be applied upon restarting the application. To control this at runtime, useEngine.print_to_stdout.
boolapplication/run/enable_alt_space_menu=false🔗
Iftrue, allows theAlt+Spacekeys to display the window menu. This menu allows the user to perform various window management operations such as moving, resizing, or minimizing the window.
Note:When the menu is displayed, project execution will pause until the menu isfullyclosed due to Windows behavior. Consider this when enabling this setting in a networked multiplayer game. The menu is only considered fully closed when an option is selected, when the user clicks outside, or whenEscapeis pressed after bringing up the window menuandanother key is pressed afterwards.
Note:This setting is implemented only on Windows.
boolapplication/run/flush_stdout_on_print=false🔗
Iftrue, flushes the standard output stream every time a line is printed. This affects both terminal logging and file logging.
When running a project, this setting must be enabled if you want logs to be collected by service managers such as systemd/journalctl. This setting is disabled by default on release builds, since flushing on every printed line will negatively affect performance if lots of lines are printed in a rapid succession. Also, if this setting is enabled, logged files will still be written successfully if the application crashes or is otherwise killed by the user (without being closed "normally").
Note:Regardless of this setting, the standard error stream (stderr) is always flushed when a line is printed to it.
Changes to this setting will only be applied upon restarting the application.
boolapplication/run/flush_stdout_on_print.debug=true🔗
Debug build override forapplication/run/flush_stdout_on_print, as performance is less important during debugging.
Changes to this setting will only be applied upon restarting the application.
intapplication/run/frame_delay_msec=0🔗
Forces aconstantdelay between frames in the main loop (in milliseconds). In most situations,application/run/max_fpsshould be preferred as an FPS limiter as it's more precise.
This setting can be overridden using the--frame-delay<ms;>command line argument.
boolapplication/run/load_shell_environment=false🔗
Iftrue, loads the default shell and copies environment variables set by the shell startup scripts to the app environment.
Note:This setting is implemented on macOS for non-sandboxed applications only.
boolapplication/run/low_processor_mode=false🔗
Iftrue, enables low-processor usage mode. When enabled, the engine takes longer to redraw, but only redraws the screen if necessary. This may lower power consumption, and is intended for editors or mobile applications. For most games, because the screen needs to be redrawn every frame, it is recommended to keep this setting disabled.
intapplication/run/low_processor_mode_sleep_usec=6900🔗
Amount of sleeping between frames when the low-processor usage mode is enabled (in microseconds). Higher values will result in lower CPU usage.
Stringapplication/run/main_loop_type="SceneTree"🔗
The name of the type implementing the engine's main loop.
Stringapplication/run/main_scene=""🔗
Path to the main scene file that will be loaded when the project runs.
intapplication/run/max_fps=0🔗
Maximum number of frames per second allowed. A value of0means "no limit". The actual number of frames per second may still be below this value if the CPU or GPU cannot keep up with the project logic and rendering.
Limiting the FPS can be useful to reduce system power consumption, which reduces heat and noise emissions (and improves battery life on mobile devices).
Ifdisplay/window/vsync/vsync_modeis set toEnabledorAdaptive, it takes precedence and the forced FPS number cannot exceed the monitor's refresh rate. See alsoDisplayServer.screen_get_refresh_rate().
Ifdisplay/window/vsync/vsync_modeisEnabled, on monitors with variable refresh rate enabled (G-Sync/FreeSync), using an FPS limit slightly lower than the monitor's refresh rate willreduce input lag while avoiding tearing. At higher refresh rates, the difference between the FPS limit and the monitor refresh rate should be increased to ensure frames to account for timing inaccuracies. The optimal formula for the FPS limit value in this scenario isr-(r*r)/3600.0, whereris the monitor's refresh rate.
Ifdisplay/window/vsync/vsync_modeisDisabled, limiting the FPS to a high value that can be consistently reached on the system can reduce input lag compared to an uncapped framerate. Since this works by ensuring the GPU load is lower than 100%, this latency reduction is only effective in GPU-bottlenecked scenarios, not CPU-bottlenecked scenarios.
See alsophysics/common/physics_ticks_per_second.
This setting can be overridden using the--max-fps<fps>command line argument (including with a value of0for unlimited framerate).
Note:This property is only read when the project starts. To change the rendering FPS cap at runtime, setEngine.max_fpsinstead.
boolapplication/run/print_header=true🔗
Iftrue, the engine header is printed in the console on startup. This header describes the current version of the engine, as well as the renderer being used. This behavior can also be disabled on the command line with the--no-headeroption.
floataudio/buses/channel_disable_threshold_db=-60.0🔗
Audio buses will disable automatically when sound goes below a given dB threshold for a given time. This saves CPU as effects assigned to that bus will no longer do any processing.
floataudio/buses/channel_disable_time=2.0🔗
Audio buses will disable automatically when sound goes below a given dB threshold for a given time. This saves CPU as effects assigned to that bus will no longer do any processing.
Stringaudio/buses/default_bus_layout="res://default_bus_layout.tres"🔗
DefaultAudioBusLayoutresource file to use in the project, unless overridden by the scene.
Stringaudio/driver/driver🔗
Specifies the audio driver to use. This setting is platform-dependent as each platform supports different audio drivers. If left empty, the default audio driver will be used.
TheDummyaudio driver disables all audio playback and recording, which is useful for non-game applications as it reduces CPU usage. It also prevents the engine from appearing as an application playing audio in the OS' audio mixer.
To query the value that is being used at run-time (which may be overridden by command-line arguments or headless mode), useAudioServer.get_driver_name().
Note:The driver in use can be overridden at runtime via the--audio-drivercommand line argument.
boolaudio/driver/enable_input=false🔗
Iftrue, microphone input will be allowed. This requires appropriate permissions to be set when exporting to Android or iOS.
Note:If the operating system blocks access to audio input devices (due to the user's privacy settings), audio capture will only return silence. On Windows, make sure that apps are allowed to access the microphone in the OS' privacy settings.
intaudio/driver/mix_rate=44100🔗
Target mixing rate used for audio (in Hz). In general, it's better to not touch this and leave it to the host operating system.
Note:On iOS and macOS, mixing rate is determined by audio driver, this value is ignored.
Note:Input and output mixing rates might be different. UseAudioServer.get_mix_rate()andAudioServer.get_input_mix_rate()to get actual values.
intaudio/driver/mix_rate.web=0🔗
Safer override foraudio/driver/mix_ratein the Web platform. Here0means "let the browser choose" (since some browsers do not like forcing the mix rate).
intaudio/driver/output_latency=15🔗
Specifies the preferred output latency in milliseconds for audio. Lower values will result in lower audio latency at the cost of increased CPU usage. Low values may result in audible crackling on slower hardware.
Audio output latency may be constrained by the host operating system and audio hardware drivers. If the host can not provide the specified audio output latency then Godot will attempt to use the nearest latency allowed by the host. As such you should always useAudioServer.get_output_latency()to determine the actual audio output latency.
Audio output latency can be overridden using the--audio-output-latency<ms>command line argument.
Note:This setting is ignored on Android.
intaudio/driver/output_latency.web=50🔗
Safer override foraudio/driver/output_latencyin the Web platform, to avoid audio issues especially on mobile devices.
floataudio/general/2d_panning_strength=0.5🔗
The base strength of the panning effect for allAudioStreamPlayer2Dnodes. The panning strength can be further scaled on each Node usingAudioStreamPlayer2D.panning_strength. A value of0.0disables stereo panning entirely, leaving only volume attenuation in place. A value of1.0completely mutes one of the channels if the sound is located exactly to the left (or right) of the listener.
The default value of0.5is tuned for headphones. When using speakers, you may find lower values to sound better as speakers have a lower stereo separation compared to headphones.
floataudio/general/3d_panning_strength=0.5🔗
The base strength of the panning effect for allAudioStreamPlayer3Dnodes. The panning strength can be further scaled on each Node usingAudioStreamPlayer3D.panning_strength. A value of0.0disables stereo panning entirely, leaving only volume attenuation in place. A value of1.0completely mutes one of the channels if the sound is located exactly to the left (or right) of the listener.
The default value of0.5is tuned for headphones which means that the opposite side channel goes no lower than 50% of the volume of the nearside channel. You may find that you can set this value higher for speakers to have the same effect since both ears can hear from each speaker.
intaudio/general/default_playback_type=0🔗
Experimental:This property may be changed or removed in future versions.
Specifies the default playback type of the platform.
The default value is set toStream, as most platforms have no issues mixing streams.
intaudio/general/default_playback_type.web=1🔗
Experimental:This property may be changed or removed in future versions.
Specifies the default playback type of the Web platform.
The default value is set toSampleas the Web platform is not suited to mix audio streams outside of the Web Audio API, especially when exporting a single-threaded game.Sampleallows for lower latency on the web platform at the cost of flexibility (AudioEffects are not supported).
Warning:ForcingStreamon the Web platform may cause high audio latency and crackling, especially when exporting a multi-threaded game.
boolaudio/general/ios/mix_with_others=false🔗
Sets themixWithOthersoption for the AVAudioSession on iOS. This will override the mix behavior, if the category is set toPlayandRecord,Playback, orMultiRoute.
Ambientalways has this set per default.
intaudio/general/ios/session_category=0🔗
Sets theAVAudioSessionCategoryon iOS. Use thePlaybackcategory to get sound output, even if the phone is in silent mode.
boolaudio/general/text_to_speech=false🔗
Iftrue, text-to-speech support is enabled on startup, otherwise it is enabled the first time any TTS method is used. See alsoDisplayServer.tts_get_voices()andDisplayServer.tts_speak().
Note:Enabling TTS can cause additional idle CPU usage and interfere with the sleep mode, so consider disabling it if TTS is not used.
intaudio/video/video_delay_compensation_ms=0🔗
Setting to hardcode audio delay when playing video. Best to leave this unchanged unless you know what you are doing.
boolcollada/use_ambient=false🔗
Iftrue, ambient lights will be imported from COLLADA models asDirectionalLight3D. Iffalse, ambient lights will be ignored.
intcompression/formats/gzip/compression_level=-1🔗
The default compression level for gzip. Affects compressed scenes and resources. Higher levels result in smaller files at the cost of compression speed. Decompression speed is mostly unaffected by the compression level.-1uses the default gzip compression level, which is identical to6but could change in the future due to underlying zlib updates.
intcompression/formats/zlib/compression_level=-1🔗
The default compression level for Zlib. Affects compressed scenes and resources. Higher levels result in smaller files at the cost of compression speed. Decompression speed is mostly unaffected by the compression level.-1uses the default gzip compression level, which is identical to6but could change in the future due to underlying zlib updates.
intcompression/formats/zstd/compression_level=3🔗
The default compression level for Zstandard. Affects compressed scenes and resources. Higher levels result in smaller files at the cost of compression speed. Decompression speed is mostly unaffected by the compression level.
boolcompression/formats/zstd/long_distance_matching=false🔗
Enableslong-distance matchingin Zstandard.
intcompression/formats/zstd/window_log_size=27🔗
Largest size limit (in power of 2) allowed when compressing using long-distance matching with Zstandard. Higher values can result in better compression, but will require more memory when compressing and decompressing.
Colordebug/canvas_items/debug_redraw_color=Color(1,0.2,0.2,0.5)🔗
If canvas item redraw debugging is active, this color will be flashed on canvas items when they redraw.
floatdebug/canvas_items/debug_redraw_time=1.0🔗
If canvas item redraw debugging is active, this will be the time the flash will last each time they redraw.
booldebug/file_logging/enable_file_logging=false🔗
Iftrue, logs all output and error messages to files. See alsodebug/file_logging/log_path,debug/file_logging/max_log_files, andapplication/run/flush_stdout_on_print.
booldebug/file_logging/enable_file_logging.pc=true🔗
Desktop override fordebug/file_logging/enable_file_logging, as log files are not readily accessible on mobile/Web platforms.
Stringdebug/file_logging/log_path="user://logs/godot.log"🔗
Path at which to store log files for the project. Using a path underuser://is recommended.
This can be specified manually on the command line using the--log-file<file>command line argument. If this command line argument is specified, log rotation is automatically disabled (seedebug/file_logging/max_log_files).
intdebug/file_logging/max_log_files=5🔗
Specifies the maximum number of log files allowed (used for rotation). Set to1to disable log file rotation.
If the--log-file<file>command line argumentis used, log rotation is always disabled.
intdebug/gdscript/warnings/assert_always_false=1🔗
When set toWarnorError, produces a warning or an error respectively when anassertcall always evaluates tofalse.
intdebug/gdscript/warnings/assert_always_true=1🔗
When set toWarnorError, produces a warning or an error respectively when anassertcall always evaluates totrue.
intdebug/gdscript/warnings/confusable_capture_reassignment=1🔗
When set toWarnorError, produces a warning or an error respectively when a local variable captured by a lambda is reassigned, since this does not modify the outer local variable.
intdebug/gdscript/warnings/confusable_identifier=1🔗
When set toWarnorError, produces a warning or an error respectively when an identifier contains characters that can be confused with something else, like when mixing different alphabets.
intdebug/gdscript/warnings/confusable_local_declaration=1🔗
When set toWarnorError, produces a warning or an error respectively when an identifier declared in the nested block has the same name as an identifier declared below in the parent block.
intdebug/gdscript/warnings/confusable_local_usage=1🔗
When set toWarnorError, produces a warning or an error respectively when an identifier that will be shadowed below in the block is used.
intdebug/gdscript/warnings/deprecated_keyword=1🔗
When set toWarnorError, produces a warning or an error respectively when deprecated keywords are used.
Note:There are currently no deprecated keywords, so this warning is never produced.
Dictionarydebug/gdscript/warnings/directory_rules={"res://addons":0}🔗
The rules for including or excluding scripts when generating warnings, as a dictionary. Each rule is an entry consisting of a directory path (key) and a decision (value). When trying to generate a warning, the GDScript parser chooses the most specific rule, i.e. the most nested directory containing the script. If the decision isExclude, warnings are not generated for this script. If the decision isIncludeor the script doesn't satisfy any of the rules, the warning configuration specified in the Project Settings is applied.
It is recommended to include your own addons/libraries, either project-specific or actively being developed at the moment. Third-party or project-agnostic addons/libraries should be excluded, as they may be incompatible with the project's warning configuration.
Note:It is not recommended to remove or change the rule for"res://addons"as the project's warning configuration may break third-party addons. Instead, consider including individual addons, if necessary.
Note:The editor does not check whether the specified paths are existing directories. It also does not automatically update these paths when directories are moved.
intdebug/gdscript/warnings/empty_file=1🔗
When set toWarnorError, produces a warning or an error respectively when an empty file is parsed.
booldebug/gdscript/warnings/enable=true🔗
Iftrue, enables specific GDScript warnings (seedebug/gdscript/warnings/*settings). Iffalse, disables all GDScript warnings.
intdebug/gdscript/warnings/enum_variable_without_default=1🔗
When set toWarnorError, produces a warning or an error respectively when a variable has an enum type but no explicit default value, but only if the enum does not contain0as a valid value.
intdebug/gdscript/warnings/get_node_default_without_onready=2🔗
When set toWarnorError, produces a warning or an error respectively whenNode.get_node()(or the shorthand$) is used as default value of a class variable without the@onreadyannotation.
intdebug/gdscript/warnings/incompatible_ternary=1🔗
When set toWarnorError, produces a warning or an error respectively when a ternary operator may emit values with incompatible types.
intdebug/gdscript/warnings/inference_on_variant=2🔗
When set toWarnorError, produces a warning or an error respectively when a static inferred type uses aVariantas initial value, which makes the static type to also be Variant.
intdebug/gdscript/warnings/inferred_declaration=0🔗
When set toWarnorError, produces a warning or an error respectively when a variable, constant, or parameter has an implicitly inferred static type. In GDScript, type inference is performed by declaring a variable with:=instead of=and leaving out the type specifier. For example,varx:=1willinfertheinttype, whilevarx:int=1explicitly declares the variable asint.
Note:This warning is recommendedin additiontodebug/gdscript/warnings/untyped_declarationif you want to always specify the type explicitly. HavingINFERRED_DECLARATIONwarning level higher thanUNTYPED_DECLARATIONwarning level makes little sense and is not recommended.
intdebug/gdscript/warnings/int_as_enum_without_cast=1🔗
When set toWarnorError, produces a warning or an error respectively when trying to use an integer as an enum without an explicit cast.
intdebug/gdscript/warnings/int_as_enum_without_match=1🔗
When set toWarnorError, produces a warning or an error respectively when trying to use an integer as an enum when there is no matching enum member for that numeric value.
intdebug/gdscript/warnings/integer_division=1🔗
When set toWarnorError, produces a warning or an error respectively when dividing an integer by another integer (the decimal part will be discarded).
intdebug/gdscript/warnings/missing_await=0🔗
When set toWarnorError, produces a warning or an error respectively when calling a coroutine withoutawait.
intdebug/gdscript/warnings/missing_tool=1🔗
When set toWarnorError, produces a warning or an error respectively when the base class script has the@toolannotation, but the current class script does not have it.
intdebug/gdscript/warnings/narrowing_conversion=1🔗
When set toWarnorError, produces a warning or an error respectively when passing a floating-point value to a function that expects an integer (it will be converted and lose precision).
intdebug/gdscript/warnings/native_method_override=2🔗
When set toWarnorError, produces a warning or an error respectively when a method in the script overrides a native method, because it may not behave as expected.
intdebug/gdscript/warnings/onready_with_export=2🔗
When set toWarnorError, produces a warning or an error respectively when the@onreadyannotation is used together with the@exportannotation, since it may not behave as expected.
intdebug/gdscript/warnings/redundant_await=1🔗
When set toWarnorError, produces a warning or an error respectively when a function that is not a coroutine is called with await.
intdebug/gdscript/warnings/redundant_static_unload=1🔗
When set toWarnorError, produces a warning or an error respectively when the@static_unloadannotation is used in a script without any static variables.
booldebug/gdscript/warnings/renamed_in_godot_4_hint=true🔗
When enabled, using a property, enum, or function that was renamed since Godot 3 will produce a hint if an error occurs.
intdebug/gdscript/warnings/return_value_discarded=0🔗
When set toWarnorError, produces a warning or an error respectively when calling a function without using its return value (by assigning it to a variable or using it as a function argument). These return values are sometimes used to indicate possible errors using theErrorenum.
intdebug/gdscript/warnings/shadowed_global_identifier=1🔗
When set toWarnorError, produces a warning or an error respectively when defining a local or member variable, signal, or enum that would have the same name as a built-in function or global class name, thus shadowing it.
intdebug/gdscript/warnings/shadowed_variable=1🔗
When set toWarnorError, produces a warning or an error respectively when a local variable or local constant shadows a member declared in the current class.
intdebug/gdscript/warnings/shadowed_variable_base_class=1🔗
When set toWarnorError, produces a warning or an error respectively when a local variable or local constant shadows a member declared in a base class.
intdebug/gdscript/warnings/standalone_expression=1🔗
When set toWarnorError, produces a warning or an error respectively when calling an expression that may have no effect on the surrounding code, such as writing2+2as a statement.
intdebug/gdscript/warnings/standalone_ternary=1🔗
When set toWarnorError, produces a warning or an error respectively when calling a ternary expression that may have no effect on the surrounding code, such as writing42ifactiveelse0as a statement.
intdebug/gdscript/warnings/static_called_on_instance=1🔗
When set toWarnorError, produces a warning or an error respectively when calling a static method from an instance of a class instead of from the class directly.
intdebug/gdscript/warnings/unassigned_variable=1🔗
When set toWarnorError, produces a warning or an error respectively when using a variable that wasn't previously assigned.
intdebug/gdscript/warnings/unassigned_variable_op_assign=1🔗
When set toWarnorError, produces a warning or an error respectively when assigning a variable using an assignment operator like+=if the variable wasn't previously assigned.
intdebug/gdscript/warnings/unreachable_code=1🔗
When set toWarnorError, produces a warning or an error respectively when unreachable code is detected (such as after areturnstatement that will always be executed).
intdebug/gdscript/warnings/unreachable_pattern=1🔗
When set toWarnorError, produces a warning or an error respectively when an unreachablematchpattern is detected.
intdebug/gdscript/warnings/unsafe_call_argument=0🔗
When set toWarnorError, produces a warning or an error respectively when using an expression whose type may not be compatible with the function parameter expected.
intdebug/gdscript/warnings/unsafe_cast=0🔗
When set toWarnorError, produces a warning or an error respectively when aVariantvalue is cast to a non-Variant.
intdebug/gdscript/warnings/unsafe_method_access=0🔗
When set toWarnorError, produces a warning or an error respectively when calling a method whose presence is not guaranteed at compile-time in the class.
intdebug/gdscript/warnings/unsafe_property_access=0🔗
When set toWarnorError, produces a warning or an error respectively when accessing a property whose presence is not guaranteed at compile-time in the class.
intdebug/gdscript/warnings/unsafe_void_return=1🔗
When set toWarnorError, produces a warning or an error respectively when returning a call from avoidfunction when such call cannot be guaranteed to be alsovoid.
intdebug/gdscript/warnings/untyped_declaration=0🔗
When set toWarnorError, produces a warning or an error respectively when a variable or parameter has no static type, or if a function has no static return type.
Note:This warning is recommended together withEditorSettings.text_editor/completion/add_type_hintsto help achieve type safety.
intdebug/gdscript/warnings/unused_local_constant=1🔗
When set toWarnorError, produces a warning or an error respectively when a local constant is never used.
intdebug/gdscript/warnings/unused_parameter=1🔗
When set toWarnorError, produces a warning or an error respectively when a function parameter is never used.
intdebug/gdscript/warnings/unused_private_class_variable=1🔗
When set toWarnorError, produces a warning or an error respectively when a private member variable is never used.
intdebug/gdscript/warnings/unused_signal=1🔗
When set toWarnorError, produces a warning or an error respectively when a signal is declared but never explicitly used in the class.
intdebug/gdscript/warnings/unused_variable=1🔗
When set toWarnorError, produces a warning or an error respectively when a local variable is unused.
Stringdebug/settings/crash_handler/message="Pleaseincludethiswhenreportingthebugtotheprojectdeveloper."🔗
Message to be displayed before the backtrace when the engine crashes. By default, this message is only used in exported projects due to the editor-only override applied to this setting.
Stringdebug/settings/crash_handler/message.editor="Pleaseincludethiswhenreportingthebugon:https://github.com/godotengine/godot/issues"🔗
Editor-only override fordebug/settings/crash_handler/message. Does not affect exported projects in debug or release mode.
booldebug/settings/gdscript/always_track_call_stacks=false🔗
Whether GDScript call stacks will be tracked in release builds, thus allowingEngine.capture_script_backtraces()to function.
Note:This setting has no effect on editor builds or debug builds, where GDScript call stacks are tracked regardless.
booldebug/settings/gdscript/always_track_local_variables=false🔗
Whether GDScript local variables will be tracked in all builds, including export builds, thus allowingEngine.capture_script_backtraces()to capture them when enabling itsinclude_variablesparameter.
Enabling this comes at the cost of roughly 50 bytes of memory per local variable, for every compiled class in the entire project, so can be several MiB in larger projects.
Note:This setting has no effect when running the game from the editor, where GDScript local variables are tracked regardless.
intdebug/settings/gdscript/max_call_stack=1024🔗
Maximum call stack allowed for debugging GDScript.
booldebug/settings/physics_interpolation/enable_warnings=true🔗
Iftrue, enables warnings which can help pinpoint where nodes are being incorrectly updated, which will result in incorrect interpolation and visual glitches.
When a node is being interpolated, it is essential that the transform is set duringNode._physics_process()(during a physics tick) rather thanNode._process()(during a frame).
intdebug/settings/profiler/max_functions=16384🔗
Maximum number of functions per frame allowed when profiling.
intdebug/settings/profiler/max_timestamp_query_elements=256🔗
Maximum number of timestamp query elements allowed per frame for visual profiling.
booldebug/settings/stdout/print_fps=false🔗
Print frames per second to standard output every second.
booldebug/settings/stdout/print_gpu_profile=false🔗
Print GPU profile information to standard output every second. This includes how long each frame takes the GPU to render on average, broken down into different steps of the render pipeline, such as CanvasItems, shadows, glow, etc.
booldebug/settings/stdout/verbose_stdout=false🔗
Print more information to standard output when running. It displays information such as memory leaks, which scenes and resources are being loaded, etc. This can also be enabled using the--verboseor-vcommand line argument, even on an exported project. See alsoOS.is_stdout_verbose()and@GlobalScope.print_verbose().
booldebug/shader_language/warnings/device_limit_exceeded=true🔗
When set totrue, produces a warning when the shader exceeds certain device limits. Currently, the only device limit checked is the limit on uniform buffer size. More device limits will be added in the future.
booldebug/shader_language/warnings/enable=true🔗
Iftrue, enables specific shader warnings (seedebug/shader_language/warnings/*settings). Iffalse, disables all shader warnings.
booldebug/shader_language/warnings/float_comparison=true🔗
When set totrue, produces a warning when two floating-point numbers are compared directly with the==operator or the!=operator.
booldebug/shader_language/warnings/formatting_error=true🔗
When set totrue, produces a warning upon encountering certain formatting errors. Currently this only checks for empty statements. More formatting errors may be added over time.
booldebug/shader_language/warnings/magic_position_write=true🔗
When set totrue, produces a warning when the shader containsPOSITION=vec4(vertex,as this was very common code written in Godot 4.2 and earlier that was paired with a QuadMesh to produce a full screen post processes pass. With the switch to reversed z in 4.3, this trick no longer works, as it implicitly relied on theVERTEX.zbeing 0.
booldebug/shader_language/warnings/treat_warnings_as_errors=false🔗
When set totrue, warnings are treated as errors.
booldebug/shader_language/warnings/unused_constant=true🔗
When set totrue, produces a warning when a constant is never used.
booldebug/shader_language/warnings/unused_function=true🔗
When set totrue, produces a warning when a function is never used.
booldebug/shader_language/warnings/unused_local_variable=true🔗
When set totrue, produces a warning when a local variable is never used.
booldebug/shader_language/warnings/unused_struct=true🔗
When set totrue, produces a warning when a struct is never used.
booldebug/shader_language/warnings/unused_uniform=true🔗
When set totrue, produces a warning when a uniform is never used.
booldebug/shader_language/warnings/unused_varying=true🔗
When set totrue, produces a warning when a varying is never used.
Colordebug/shapes/avoidance/2d/agents_radius_color=Color(1,1,0,0.25)🔗
Color of the avoidance agents radius, visible when "Visible Avoidance" is enabled in the Debug menu.
booldebug/shapes/avoidance/2d/enable_agents_radius=true🔗
If enabled, displays avoidance agents radius when "Visible Avoidance" is enabled in the Debug menu.
booldebug/shapes/avoidance/2d/enable_obstacles_radius=true🔗
If enabled, displays avoidance obstacles radius when "Visible Avoidance" is enabled in the Debug menu.
booldebug/shapes/avoidance/2d/enable_obstacles_static=true🔗
If enabled, displays static avoidance obstacles when "Visible Avoidance" is enabled in the Debug menu.
Colordebug/shapes/avoidance/2d/obstacles_radius_color=Color(1,0.5,0,0.25)🔗
Color of the avoidance obstacles radius, visible when "Visible Avoidance" is enabled in the Debug menu.
Colordebug/shapes/avoidance/2d/obstacles_static_edge_pushin_color=Color(1,0,0,1)🔗
Color of the static avoidance obstacles edges when their vertices are winded in order to push agents in, visible when "Visible Avoidance" is enabled in the Debug menu.
Colordebug/shapes/avoidance/2d/obstacles_static_edge_pushout_color=Color(1,1,0,1)🔗
Color of the static avoidance obstacles edges when their vertices are winded in order to push agents out, visible when "Visible Avoidance" is enabled in the Debug menu.
Colordebug/shapes/avoidance/2d/obstacles_static_face_pushin_color=Color(1,0,0,0)🔗
Color of the static avoidance obstacles faces when their vertices are winded in order to push agents in, visible when "Visible Avoidance" is enabled in the Debug menu.
Colordebug/shapes/avoidance/2d/obstacles_static_face_pushout_color=Color(1,1,0,0.5)🔗
Color of the static avoidance obstacles faces when their vertices are winded in order to push agents out, visible when "Visible Avoidance" is enabled in the Debug menu.
Colordebug/shapes/avoidance/3d/agents_radius_color=Color(1,1,0,0.25)🔗
Color of the avoidance agents radius, visible when "Visible Avoidance" is enabled in the Debug menu.
booldebug/shapes/avoidance/3d/enable_agents_radius=true🔗
If enabled, displays avoidance agents radius when "Visible Avoidance" is enabled in the Debug menu.
booldebug/shapes/avoidance/3d/enable_obstacles_radius=true🔗
If enabled, displays avoidance obstacles radius when "Visible Avoidance" is enabled in the Debug menu.
booldebug/shapes/avoidance/3d/enable_obstacles_static=true🔗
If enabled, displays static avoidance obstacles when "Visible Avoidance" is enabled in the Debug menu.
Colordebug/shapes/avoidance/3d/obstacles_radius_color=Color(1,0.5,0,0.25)🔗
Color of the avoidance obstacles radius, visible when "Visible Avoidance" is enabled in the Debug menu.
Colordebug/shapes/avoidance/3d/obstacles_static_edge_pushin_color=Color(1,0,0,1)🔗
Color of the static avoidance obstacles edges when their vertices are winded in order to push agents in, visible when "Visible Avoidance" is enabled in the Debug menu.
Colordebug/shapes/avoidance/3d/obstacles_static_edge_pushout_color=Color(1,1,0,1)🔗
Color of the static avoidance obstacles edges when their vertices are winded in order to push agents out, visible when "Visible Avoidance" is enabled in the Debug menu.
Colordebug/shapes/avoidance/3d/obstacles_static_face_pushin_color=Color(1,0,0,0)🔗
Color of the static avoidance obstacles faces when their vertices are winded in order to push agents in, visible when "Visible Avoidance" is enabled in the Debug menu.
Colordebug/shapes/avoidance/3d/obstacles_static_face_pushout_color=Color(1,1,0,0.5)🔗
Color of the static avoidance obstacles faces when their vertices are winded in order to push agents out, visible when "Visible Avoidance" is enabled in the Debug menu.
Colordebug/shapes/collision/contact_color=Color(1,0.2,0.1,0.8)🔗
Color of the contact points between collision shapes, visible when "Visible Collision Shapes" is enabled in the Debug menu.
booldebug/shapes/collision/draw_2d_outlines=true🔗
Sets whether 2D physics will display collision outlines in game when "Visible Collision Shapes" is enabled in the Debug menu.
intdebug/shapes/collision/max_contacts_displayed=10000🔗
Maximum number of contact points between collision shapes to display when "Visible Collision Shapes" is enabled in the Debug menu.
Colordebug/shapes/collision/shape_color=Color(0,0.6,0.7,0.42)🔗
Color of the collision shapes, visible when "Visible Collision Shapes" is enabled in the Debug menu.
Colordebug/shapes/navigation/2d/agent_path_color=Color(1,0,0,1)🔗
Color to display enabled navigation agent paths when an agent has debug enabled.
floatdebug/shapes/navigation/2d/agent_path_point_size=4.0🔗
Rasterized size (pixel) used to render navigation agent path points when an agent has debug enabled.
Colordebug/shapes/navigation/2d/edge_connection_color=Color(1,0,1,1)🔗
Color to display edge connections between navigation regions, visible when "Visible Navigation" is enabled in the Debug menu.
booldebug/shapes/navigation/2d/enable_agent_paths=true🔗
If enabled, displays navigation agent paths when an agent has debug enabled.
booldebug/shapes/navigation/2d/enable_edge_connections=true🔗
If enabled, displays edge connections between navigation regions when "Visible Navigation" is enabled in the Debug menu.
booldebug/shapes/navigation/2d/enable_edge_lines=true🔗
If enabled, displays navigation mesh polygon edges when "Visible Navigation" is enabled in the Debug menu.
booldebug/shapes/navigation/2d/enable_geometry_face_random_color=true🔗
If enabled, colorizes each navigation mesh polygon face with a random color when "Visible Navigation" is enabled in the Debug menu.
booldebug/shapes/navigation/2d/enable_link_connections=true🔗
If enabled, displays navigation link connections when "Visible Navigation" is enabled in the Debug menu.
Colordebug/shapes/navigation/2d/geometry_edge_color=Color(0.5,1,1,1)🔗
Color to display enabled navigation mesh polygon edges, visible when "Visible Navigation" is enabled in the Debug menu.
Colordebug/shapes/navigation/2d/geometry_edge_disabled_color=Color(0.5,0.5,0.5,1)🔗
Color to display disabled navigation mesh polygon edges, visible when "Visible Navigation" is enabled in the Debug menu.
Colordebug/shapes/navigation/2d/geometry_face_color=Color(0.5,1,1,0.4)🔗
Color to display enabled navigation mesh polygon faces, visible when "Visible Navigation" is enabled in the Debug menu.
Colordebug/shapes/navigation/2d/geometry_face_disabled_color=Color(0.5,0.5,0.5,0.4)🔗
Color to display disabled navigation mesh polygon faces, visible when "Visible Navigation" is enabled in the Debug menu.
Colordebug/shapes/navigation/2d/link_connection_color=Color(1,0.5,1,1)🔗
Color to use to display navigation link connections, visible when "Visible Navigation" is enabled in the Debug menu.
Colordebug/shapes/navigation/2d/link_connection_disabled_color=Color(0.5,0.5,0.5,1)🔗
Color to use to display disabled navigation link connections, visible when "Visible Navigation" is enabled in the Debug menu.
Colordebug/shapes/navigation/3d/agent_path_color=Color(1,0,0,1)🔗
Color to display enabled navigation agent paths when an agent has debug enabled.
floatdebug/shapes/navigation/3d/agent_path_point_size=4.0🔗
Rasterized size (pixel) used to render navigation agent path points when an agent has debug enabled.
Colordebug/shapes/navigation/3d/edge_connection_color=Color(1,0,1,1)🔗
Color to display edge connections between navigation regions, visible when "Visible Navigation" is enabled in the Debug menu.
booldebug/shapes/navigation/3d/enable_agent_paths=true🔗
If enabled, displays navigation agent paths when an agent has debug enabled.
booldebug/shapes/navigation/3d/enable_agent_paths_xray=true🔗
If enabled, displays navigation agent paths through geometry when an agent has debug enabled.
booldebug/shapes/navigation/3d/enable_edge_connections=true🔗
If enabled, displays edge connections between navigation regions when "Visible Navigation" is enabled in the Debug menu.
booldebug/shapes/navigation/3d/enable_edge_connections_xray=true🔗
If enabled, displays edge connections between navigation regions through geometry when "Visible Navigation" is enabled in the Debug menu.
booldebug/shapes/navigation/3d/enable_edge_lines=true🔗
If enabled, displays navigation mesh polygon edges when "Visible Navigation" is enabled in the Debug menu.
booldebug/shapes/navigation/3d/enable_edge_lines_xray=true🔗
If enabled, displays navigation mesh polygon edges through geometry when "Visible Navigation" is enabled in the Debug menu.
booldebug/shapes/navigation/3d/enable_geometry_face_random_color=true🔗
If enabled, colorizes each navigation mesh polygon face with a random color when "Visible Navigation" is enabled in the Debug menu.
booldebug/shapes/navigation/3d/enable_link_connections=true🔗
If enabled, displays navigation link connections when "Visible Navigation" is enabled in the Debug menu.
booldebug/shapes/navigation/3d/enable_link_connections_xray=true🔗
If enabled, displays navigation link connections through geometry when "Visible Navigation" is enabled in the Debug menu.
Colordebug/shapes/navigation/3d/geometry_edge_color=Color(0.5,1,1,1)🔗
Color to display enabled navigation mesh polygon edges, visible when "Visible Navigation" is enabled in the Debug menu.
Colordebug/shapes/navigation/3d/geometry_edge_disabled_color=Color(0.5,0.5,0.5,1)🔗
Color to display disabled navigation mesh polygon edges, visible when "Visible Navigation" is enabled in the Debug menu.
Colordebug/shapes/navigation/3d/geometry_face_color=Color(0.5,1,1,0.4)🔗
Color to display enabled navigation mesh polygon faces, visible when "Visible Navigation" is enabled in the Debug menu.
Colordebug/shapes/navigation/3d/geometry_face_disabled_color=Color(0.5,0.5,0.5,0.4)🔗
Color to display disabled navigation mesh polygon faces, visible when "Visible Navigation" is enabled in the Debug menu.
Colordebug/shapes/navigation/3d/link_connection_color=Color(1,0.5,1,1)🔗
Color to use to display navigation link connections, visible when "Visible Navigation" is enabled in the Debug menu.
Colordebug/shapes/navigation/3d/link_connection_disabled_color=Color(0.5,0.5,0.5,1)🔗
Color to use to display disabled navigation link connections, visible when "Visible Navigation" is enabled in the Debug menu.
Colordebug/shapes/paths/geometry_color=Color(0.1,1,0.7,0.4)🔗
Color of the curve path geometry, visible when "Visible Paths" is enabled in the Debug menu.
floatdebug/shapes/paths/geometry_width=2.0🔗
Line width of the curve path geometry, visible when "Visible Paths" is enabled in the Debug menu.
Stringdisplay/display_server/driver🔗
Sets the driver to be used by the display server. This property can not be edited directly, instead, set the driver using the platform-specific overrides.
Stringdisplay/display_server/driver.android🔗
Android override fordisplay/display_server/driver.
Stringdisplay/display_server/driver.ios🔗
iOS override fordisplay/display_server/driver.
Stringdisplay/display_server/driver.linuxbsd🔗
LinuxBSD override fordisplay/display_server/driver.
Stringdisplay/display_server/driver.macos🔗
MacOS override fordisplay/display_server/driver.
Stringdisplay/display_server/driver.visionos🔗
visionOS override fordisplay/display_server/driver.
Stringdisplay/display_server/driver.windows🔗
Windows override fordisplay/display_server/driver.
Stringdisplay/mouse_cursor/custom_image=""🔗
Custom image for the mouse cursor (limited to 256×256).
Vector2display/mouse_cursor/custom_image_hotspot=Vector2(0,0)🔗
Hotspot for the custom mouse cursor image.
Vector2display/mouse_cursor/tooltip_position_offset=Vector2(10,10)🔗
Position offset for tooltips, relative to the mouse cursor's hotspot.
booldisplay/window/dpi/allow_hidpi=true🔗
Iftrue, allows HiDPI display on Windows, macOS, Android, iOS and Web. Iffalse, the platform's low-DPI fallback will be used on HiDPI displays, which causes the window to be displayed in a blurry or pixelated manner (and can cause various window management bugs). Therefore, it is recommended to make your project scale tomultiple resolutionsinstead of disabling this setting.
Note:This setting has no effect on Linux as DPI-awareness fallbacks are not supported there.
booldisplay/window/energy_saving/keep_screen_on=true🔗
Iftrue, keeps the screen on (even in case of inactivity), so the screensaver does not take over. Works on desktop and mobile platforms.
booldisplay/window/frame_pacing/android/enable_frame_pacing=true🔗
Enable Swappy for stable frame pacing on Android. Highly recommended.
Note:This option will be forced off when using OpenXR.
intdisplay/window/frame_pacing/android/swappy_mode=2🔗
Swappy mode to use. The options are:
- pipeline_forced_on: Try to honorEngine.max_fps. Pipelining is always on. This is the same behavior as a desktop PC.
pipeline_forced_on: Try to honorEngine.max_fps. Pipelining is always on. This is the same behavior as a desktop PC.
- auto_fps_pipeline_forced_on: Calculate the max FPS automatically. The actual max FPS will be between0andEngine.max_fps. While this sounds convenient, beware that Swappy will often downgrade the max FPS until it finds a value that can be maintained. That means, if your game runs between 40fps and 60fps on a 60hz screen, after some time Swappy will downgrade the max FPS so that the game renders at a perfect 30fps.
auto_fps_pipeline_forced_on: Calculate the max FPS automatically. The actual max FPS will be between0andEngine.max_fps. While this sounds convenient, beware that Swappy will often downgrade the max FPS until it finds a value that can be maintained. That means, if your game runs between 40fps and 60fps on a 60hz screen, after some time Swappy will downgrade the max FPS so that the game renders at a perfect 30fps.
- auto_fps_auto_pipeline: Same asauto_fps_pipeline_forced_on, but if Swappy detects that rendering is very fast (for example it takes less than 8ms to render on a 60hz screen), Swappy will disable pipelining to minimize input latency. This is the default.
auto_fps_auto_pipeline: Same asauto_fps_pipeline_forced_on, but if Swappy detects that rendering is very fast (for example it takes less than 8ms to render on a 60hz screen), Swappy will disable pipelining to minimize input latency. This is the default.
Note:IfEngine.max_fpsis0, the actual max FPS will be considered to be the screen's refresh rate (often 60hz, 90hz, or 120hz, depending on device model and OS settings).
intdisplay/window/handheld/orientation=0🔗
The default screen orientation to use on mobile devices. SeeScreenOrientationfor possible values.
Note:When set to a portrait orientation, this project setting does not flip the project resolution's width and height automatically. Instead, you have to setdisplay/window/size/viewport_widthanddisplay/window/size/viewport_heightaccordingly.
booldisplay/window/ios/allow_high_refresh_rate=true🔗
Iftrue, iOS devices that support high refresh rate/"ProMotion" will be allowed to render at up to 120 frames per second.
booldisplay/window/ios/hide_home_indicator=true🔗
Iftrue, the home indicator is hidden automatically. This only affects iOS devices without a physical home button.
booldisplay/window/ios/hide_status_bar=true🔗
Iftrue, the status bar is hidden while the app is running.
booldisplay/window/ios/suppress_ui_gesture=true🔗
Iftrue, it will require two swipes to access iOS UI that uses gestures.
Note:This setting has no effect on the home indicator ifhide_home_indicatoristrue.
booldisplay/window/per_pixel_transparency/allowed=false🔗
Iftrue, allows per-pixel transparency for the window background. This affects performance, so leave it onfalseunless you need it. See alsodisplay/window/size/transparentandrendering/viewport/transparent_background.
booldisplay/window/size/always_on_top=false🔗
Forces the main window to be always on top.
Note:This setting is ignored on iOS, Android, and Web.
booldisplay/window/size/borderless=false🔗
Forces the main window to be borderless.
Note:This setting is ignored on iOS, Android, and Web.
booldisplay/window/size/extend_to_title=false🔗
Main window content is expanded to the full size of the window. Unlike a borderless window, the frame is left intact and can be used to resize the window, and the title bar is transparent, but has minimize/maximize/close buttons.
Note:This setting is implemented only on macOS.
Vector2idisplay/window/size/initial_position=Vector2i(0,0)🔗
Main window initial position (in virtual desktop coordinates), this setting is used only ifdisplay/window/size/initial_position_typeis set to "Absolute" (0).
Note:This setting only affects the exported project, or when the project is run from the command line. In the editor, the value ofEditorSettings.run/window_placement/rect_custom_positionis used instead.
intdisplay/window/size/initial_position_type=1🔗
Main window initial position.
0- "Absolute",display/window/size/initial_positionis used to set window position.
1- "Primary Screen Center".
3- "Other Screen Center",display/window/size/initial_screenis used to set the screen.
4- "Center of Screen With Mouse Pointer".
5- "Center of Screen With Keyboard Focus".
Note:This setting only affects the exported project, or when the project is run from the command line. In the editor, the value ofEditorSettings.run/window_placement/rectis used instead.
intdisplay/window/size/initial_screen=0🔗
Main window initial screen, this setting is used only ifdisplay/window/size/initial_position_typeis set to "Other Screen Center" (2).
Note:This setting only affects the exported project, or when the project is run from the command line. In the editor, the value ofEditorSettings.run/window_placement/screenis used instead.
booldisplay/window/size/maximize_disabled=false🔗
Iftrue, the main window's maximize button is disabled.
booldisplay/window/size/minimize_disabled=false🔗
Iftrue, the main window's minimize button is disabled.
intdisplay/window/size/mode=0🔗
Main window mode. SeeWindowModefor possible values and how each mode behaves.
Note:Game embedding is available only in the "Windowed" mode.
booldisplay/window/size/no_focus=false🔗
Main window can't be focused. No-focus window will ignore all input, except mouse clicks.
booldisplay/window/size/resizable=true🔗
Iftrue, allows the window to be resizable by default.
Note:This property is only read when the project starts. To change whether the window is resizable at runtime, setWindow.unresizableinstead on the root Window, which can be retrieved usingget_viewport().get_window().Window.unresizabletakes the opposite value of this setting.
Note:Certain window managers can be configured to ignore the non-resizable status of a window. Do not rely on this setting as a guarantee that the window willneverbe resizable.
Note:This setting is ignored on iOS.
booldisplay/window/size/sharp_corners=false🔗
Iftrue, the main window uses sharp corners by default.
Note:This property is implemented only on Windows (11).
booldisplay/window/size/transparent=false🔗
Iftrue, enables a window manager hint that the main window backgroundcanbe transparent. This does not make the background actually transparent. For the background to be transparent, the root viewport must also be made transparent by enablingrendering/viewport/transparent_background.
Note:To use a transparent splash screen, setapplication/boot_splash/bg_colortoColor(0,0,0,0).
Note:This setting has no effect ifdisplay/window/per_pixel_transparency/allowedis set tofalse.
Note:This setting has no effect on Android as transparency is controlled only viadisplay/window/per_pixel_transparency/allowed.
intdisplay/window/size/viewport_height=648🔗
Sets the game's main viewport height. On desktop platforms, this is also the initial window height, represented by an indigo-colored rectangle in the 2D editor. Stretch mode settings also use this as a reference when using thecanvas_itemsorviewportstretch modes. See alsodisplay/window/size/viewport_width,display/window/size/window_width_overrideanddisplay/window/size/window_height_override.
intdisplay/window/size/viewport_width=1152🔗
Sets the game's main viewport width. On desktop platforms, this is also the initial window width, represented by an indigo-colored rectangle in the 2D editor. Stretch mode settings also use this as a reference when using thecanvas_itemsorviewportstretch modes. See alsodisplay/window/size/viewport_height,display/window/size/window_width_overrideanddisplay/window/size/window_height_override.
intdisplay/window/size/window_height_override=0🔗
On desktop platforms, overrides the game's initial window height. See alsodisplay/window/size/window_width_override,display/window/size/viewport_widthanddisplay/window/size/viewport_height.
Note:By default, or when set to0, the initial window height is thedisplay/window/size/viewport_height. This setting is ignored on iOS, Android, and Web.
intdisplay/window/size/window_width_override=0🔗
On desktop platforms, overrides the game's initial window width. See alsodisplay/window/size/window_height_override,display/window/size/viewport_widthanddisplay/window/size/viewport_height.
Note:By default, or when set to0, the initial window width is thedisplay/window/size/viewport_width. This setting is ignored on iOS, Android, and Web.
Stringdisplay/window/stretch/aspect="keep"🔗
Defines how the aspect ratio of the base size is preserved when stretching to fit the resolution of the window or screen.
"ignore": Ignore the aspect ratio when stretching the screen. This means that the original resolution will be stretched to exactly fill the screen, even if it's wider or narrower. This may result in non-uniform stretching: things looking wider or taller than designed.
"keep": Keep aspect ratio when stretching the screen. This means that the viewport retains its original size regardless of the screen resolution, and black bars will be added to the top/bottom of the screen ("letterboxing") or the sides ("pillarboxing").
"keep_width": Keep aspect ratio when stretching the screen. If the screen is wider than the base size, black bars are added at the left and right (pillarboxing). But if the screen is taller than the base resolution, the viewport will be grown in the vertical direction (and more content will be visible at the bottom). You can also think of this as "Expand Vertically".
"keep_height": Keep aspect ratio when stretching the screen. If the screen is taller than the base size, black bars are added at the top and bottom (letterboxing). But if the screen is wider than the base resolution, the viewport will be grown in the horizontal direction (and more content will be visible to the right). You can also think of this as "Expand Horizontally".
"expand": Keep aspect ratio when stretching the screen, but keep neither the base width nor height. Depending on the screen aspect ratio, the viewport will either be larger in the horizontal direction (if the screen is wider than the base size) or in the vertical direction (if the screen is taller than the original size).
Stringdisplay/window/stretch/mode="disabled"🔗
Defines how the base size is stretched to fit the resolution of the window or screen.
"disabled": No stretching happens. One unit in the scene corresponds to one pixel on the screen. In this mode,display/window/stretch/aspecthas no effect. Recommended for non-game applications.
"canvas_items": The base size specified in width and height in the project settings is stretched to cover the whole screen (takingdisplay/window/stretch/aspectinto account). This means that everything is rendered directly at the target resolution. 3D is unaffected, while in 2D, there is no longer a 1:1 correspondence between sprite pixels and screen pixels, which may result in scaling artifacts. Recommended for most games that don't use a pixel art aesthetic, although it is possible to use this stretch mode for pixel art games too (especially in 3D).
"viewport": The size of the rootViewportis set precisely to the base size specified in the Project Settings' Display section. The scene is rendered to this viewport first. Finally, this viewport is scaled to fit the screen (takingdisplay/window/stretch/aspectinto account). Recommended for games that use a pixel art aesthetic.
floatdisplay/window/stretch/scale=1.0🔗
The scale factor multiplier to use for 2D elements. This multiplies the final scale factor determined bydisplay/window/stretch/mode. If using theDisabledstretch mode, this scale factor is applied as-is. This can be adjusted to make the UI easier to read on certain displays.
Stringdisplay/window/stretch/scale_mode="fractional"🔗
The policy to use to determine the final scale factor for 2D elements. This affects howdisplay/window/stretch/scaleis applied, in addition to the automatic scale factor determined bydisplay/window/stretch/mode.
"fractional": The scale factor will not be modified.
"integer": The scale factor will be floored to an integer value, which means that the screen size will always be an integer multiple of the base viewport size. This provides a crisp pixel art appearance.
Note:When using integer scaling with a stretch mode, resizing the window to be smaller than the base viewport size will clip the contents. Consider preventing that by settingWindow.min_sizeto the same value as the base viewport size defined indisplay/window/size/viewport_widthanddisplay/window/size/viewport_height.
booldisplay/window/subwindows/embed_subwindows=true🔗
Iftrue, subwindows are embedded in the main window (this is also called single-window mode). Single-window mode can be faster as it does not need to create a separate window for every popup and tooltip, which can be a slow operation depending on the operating system and rendering method in use.
Iffalse, subwindows are created as separate windows (this is also called multi-window mode). This allows them to be moved outside the main window and use native operating system window decorations.
This is equivalent toEditorSettings.interface/editor/single_window_modein the editor.
intdisplay/window/vsync/vsync_mode=1🔗
Sets the V-Sync mode for the main game window. The editor's own V-Sync mode can be set usingEditorSettings.interface/editor/vsync_mode.
SeeVSyncModefor possible values and how they affect the behavior of your application.
Depending on the platform and rendering method, the engine will fall back toEnabledif the desired mode is not supported.
V-Sync can be disabled on the command line using the--disable-vsynccommand line argument.
Note:TheAdaptiveandMailboxV-Sync modes are only supported in the Forward+ and Mobile rendering methods, not Compatibility.
Note:This property is only read when the project starts. To change the V-Sync mode at runtime, callDisplayServer.window_set_vsync_mode()instead.
Stringdotnet/project/assembly_name=""🔗
Name of the .NET assembly. This name is used as the name of the.csprojand.slnfiles. By default, it's set to the name of the project (application/config/name) allowing to change it in the future without affecting the .NET assembly.
intdotnet/project/assembly_reload_attempts=3🔗
Number of times to attempt assembly reloading after rebuilding .NET assemblies. Effectively also the timeout in seconds to wait for unloading of script assemblies to finish.
Stringdotnet/project/solution_directory=""🔗
Directory that contains the.slnfile. By default, the.slnfiles is in the root of the project directory, next to theproject.godotand.csprojfiles.
Changing this value allows setting up a multi-project scenario where there are multiple.csproj. Keep in mind that the Godot project is considered one of the C# projects in the workspace and it's root directory should contain theproject.godotand.csprojnext to each other.
booleditor/export/convert_text_resources_to_binary=true🔗
Iftrue, text resource (tres) and text scene (tscn) files are converted to their corresponding binary format on export. This decreases file sizes and speeds up loading slightly.
Note:Because a resource's file extension may change in an exported project, it is heavily recommended to use@GDScript.load()orResourceLoaderinstead ofFileAccessto load resources dynamically.
Note:The project settings file (project.godot) will always be converted to binary on export, regardless of this setting.
inteditor/import/atlas_max_width=2048🔗
The maximum width to use when importing textures as an atlas. The value will be rounded to the nearest power of two when used. Use this to prevent imported textures from growing too large in the other direction.
booleditor/import/reimport_missing_imported_files=true🔗
There is currently no description for this property. Please help us bycontributing one!
booleditor/import/use_multiple_threads=true🔗
Iftrueimporting of resources is run on multiple threads.
inteditor/movie_writer/audio_bit_depth=16🔗
Number of bits per audio sample written to the.avifile. Only 16 and 32-bit are supported.
booleditor/movie_writer/disable_vsync=false🔗
Iftrue, requests V-Sync to be disabled when writing a movie (similar to settingdisplay/window/vsync/vsync_modetoDisabled). This can speed up video writing if the hardware is fast enough to render, encode and save the video at a framerate higher than the monitor's refresh rate.
Note:editor/movie_writer/disable_vsynchas no effect if the operating system or graphics driver forces V-Sync with no way for applications to disable it.
inteditor/movie_writer/fps=60🔗
The number of frames per second to record in the video when writing a movie. Simulation speed will adjust to always match the specified framerate, which means the engine will appear to run slower at highereditor/movie_writer/fpsvalues. Certain FPS values will require you to adjusteditor/movie_writer/mix_rateto prevent audio from desynchronizing over time.
This can be specified manually on the command line using the--fixed-fps<fps>command line argument.
inteditor/movie_writer/mix_rate=48000🔗
The audio mix rate to use in the recorded audio when writing a movie (in Hz). This can be different fromaudio/driver/mix_rate, but this value must be divisible byeditor/movie_writer/fpsto prevent audio from desynchronizing over time.
Stringeditor/movie_writer/movie_file=""🔗
The output path for the movie. The file extension determines theMovieWriterthat will be used.
Godot has 3 built-inMovieWriters:
- OGV container with Theora for video and Vorbis for audio (.ogvfile extension). Lossy compression, medium file sizes, fast encoding. The lossy compression quality can be adjusted by changingeditor/movie_writer/video_qualityandeditor/movie_writer/ogv/audio_quality. The resulting file can be viewed in Godot withVideoStreamPlayerand most video players, but not web browsers as they don't support Theora.
OGV container with Theora for video and Vorbis for audio (.ogvfile extension). Lossy compression, medium file sizes, fast encoding. The lossy compression quality can be adjusted by changingeditor/movie_writer/video_qualityandeditor/movie_writer/ogv/audio_quality. The resulting file can be viewed in Godot withVideoStreamPlayerand most video players, but not web browsers as they don't support Theora.
- AVI container with MJPEG for video and uncompressed audio (.avifile extension). Lossy compression, medium file sizes, fast encoding. The lossy compression quality can be adjusted by changingeditor/movie_writer/video_quality. The resulting file can be viewed in most video players, but it must be converted to another format for viewing on the web or by Godot withVideoStreamPlayer. MJPEG does not support transparency. AVI output is currently limited to a file of 4 GB in size at most.
AVI container with MJPEG for video and uncompressed audio (.avifile extension). Lossy compression, medium file sizes, fast encoding. The lossy compression quality can be adjusted by changingeditor/movie_writer/video_quality. The resulting file can be viewed in most video players, but it must be converted to another format for viewing on the web or by Godot withVideoStreamPlayer. MJPEG does not support transparency. AVI output is currently limited to a file of 4 GB in size at most.
- PNG image sequence for video and WAV for audio (.pngfile extension). Lossless compression, large file sizes, slow encoding. Designed to be encoded to a video file with another tool such asFFmpegafter recording. Transparency is currently not supported, even if the root viewport is set to be transparent.
PNG image sequence for video and WAV for audio (.pngfile extension). Lossless compression, large file sizes, slow encoding. Designed to be encoded to a video file with another tool such asFFmpegafter recording. Transparency is currently not supported, even if the root viewport is set to be transparent.
If you need to encode to a different format or pipe a stream through third-party software, you can extend thisMovieWriterclass to create your own movie writers.
When using PNG output, the frame number will be appended at the end of the file name. It starts from 0 and is padded with 8 digits to ensure correct sorting and easier processing. For example, if the output path is/tmp/hello.png, the first two frames will be/tmp/hello00000000.pngand/tmp/hello00000001.png. The audio will be saved at/tmp/hello.wav.
floateditor/movie_writer/ogv/audio_quality=0.5🔗
The audio encoding quality to use when writing Vorbis audio to a file, between-0.1and1.0(inclusive). Higherqualityvalues result in better-sounding output at the cost of larger file sizes. Even at quality1.0, compression remains lossy.
Note:This does not affect video quality, which is controlled byeditor/movie_writer/video_qualityinstead.
inteditor/movie_writer/ogv/encoding_speed=4🔗
The tradeoff between encoding speed and compression efficiency. Speed1is the slowest but provides the best compression. Speed4is the fastest but provides the worst compression. Video quality is generally not affected significantly by this setting.
inteditor/movie_writer/ogv/keyframe_interval=64🔗
Forces keyframes at the specified interval (in frame count). Higher values can improve compression up to a certain level at the expense of higher latency when seeking.
inteditor/movie_writer/speaker_mode=0🔗
The speaker mode to use in the recorded audio when writing a movie. SeeSpeakerModefor possible values.
floateditor/movie_writer/video_quality=0.75🔗
The video encoding quality to use when writing a Theora or AVI (MJPEG) video to a file, between0.0and1.0(inclusive). Higherqualityvalues result in better-looking output at the cost of larger file sizes. Recommendedqualityvalues are between0.75and0.9. Even at quality1.0, compression remains lossy.
Stringeditor/naming/default_signal_callback_name="_on_{node_name}_{signal_name}"🔗
The format of the default signal callback name (in the Signal Connection Dialog). The following substitutions are available:{NodeName},{nodeName},{node_name},{SignalName},{signalName}, and{signal_name}.
Stringeditor/naming/default_signal_callback_to_self_name="_on_{signal_name}"🔗
The format of the default signal callback name when a signal connects to the same node that emits it (in the Signal Connection Dialog). The following substitutions are available:{NodeName},{nodeName},{node_name},{SignalName},{signalName}, and{signal_name}.
inteditor/naming/node_name_casing=0🔗
When creating node names automatically, set the type of casing to use in this project. This is mostly an editor setting.
inteditor/naming/node_name_num_separator=0🔗
What to use to separate node name from number. This is mostly an editor setting.
inteditor/naming/scene_name_casing=2🔗
When generating scene file names from scene root node, set the type of casing to use in this project. This is mostly an editor setting.
inteditor/naming/script_name_casing=0🔗
When generating script file names from the selected node, set the type of casing to use in this project. This is mostly an editor setting.
Stringeditor/run/main_run_args=""🔗
The command-line arguments to append to Godot's own command line when running the project. This doesn't affect the editor itself.
It is possible to make another executable run Godot by using the%command%placeholder. The placeholder will be replaced with Godot's own command line. Program-specific arguments should be placedbeforethe placeholder, whereas Godot-specific arguments should be placedafterthe placeholder.
For example, this can be used to force the project to run on the dedicated GPU in an NVIDIA Optimus system on Linux:

```
prime-run %command%
```

PackedStringArrayeditor/script/search_in_file_extensions🔗
Text-based file extensions to include in the script editor's "Find in Files" feature. You can add e.g.tscnif you wish to also parse your scene files, especially if you use built-in scripts which are serialized in the scene files.
Note:The returned array iscopiedand any changes to it will not update the original property value. SeePackedStringArrayfor more details.
Stringeditor/script/templates_search_path="res://script_templates"🔗
Search path for project-specific script templates. Godot will search for script templates both in the editor-specific path and in this project-specific path.
booleditor/version_control/autoload_on_startup=false🔗
There is currently no description for this property. Please help us bycontributing one!
Stringeditor/version_control/plugin_name=""🔗
There is currently no description for this property. Please help us bycontributing one!
boolfilesystem/import/blender/enabled=true🔗
Iftrue, Blender 3D scene files with the.blendextension will be imported by converting them to glTF 2.0.
This requires configuring a path to a Blender executable in theEditorSettings.filesystem/import/blender/blender_pathsetting. Blender 3.0 or later is required.
boolfilesystem/import/blender/enabled.android=false🔗
Override forfilesystem/import/blender/enabledon Android where Blender can't easily be accessed from Godot.
boolfilesystem/import/blender/enabled.web=false🔗
Override forfilesystem/import/blender/enabledon the Web where Blender can't easily be accessed from Godot.
boolfilesystem/import/fbx2gltf/enabled=true🔗
Iftrue, Autodesk FBX 3D scene files with the.fbxextension will be imported by converting them to glTF 2.0.
This requires configuring a path to an FBX2glTF executable in the editor settings atEditorSettings.filesystem/import/fbx/fbx2gltf_path.
boolfilesystem/import/fbx2gltf/enabled.android=false🔗
Override forfilesystem/import/fbx2gltf/enabledon Android where FBX2glTF can't easily be accessed from Godot.
boolfilesystem/import/fbx2gltf/enabled.web=false🔗
Override forfilesystem/import/fbx2gltf/enabledon the Web where FBX2glTF can't easily be accessed from Godot.
intgui/common/default_scroll_deadzone=0🔗
Default value forScrollContainer.scroll_deadzone, which will be used for allScrollContainers unless overridden.
intgui/common/drag_threshold=10🔗
The minimum distance the mouse cursor must move while pressed before a drag operation begins in the default viewport. For custom viewports seeViewport.gui_drag_threshold.
intgui/common/show_focus_state_on_pointer_event=1🔗
Determines whether aControlshould visually indicate focus when said focus is gained using a mouse or touch input.

- Never(0) show the focused state for mouse/touch input.
Never(0) show the focused state for mouse/touch input.
- Control Supports Keyboard Input(1) shows the focused state even when gained via mouse/touch input (similar to how browsers handle focus).
Control Supports Keyboard Input(1) shows the focused state even when gained via mouse/touch input (similar to how browsers handle focus).
- Always(2) show the focused state, even if said focus was gained via mouse/touch input.
Always(2) show the focused state, even if said focus was gained via mouse/touch input.
boolgui/common/snap_controls_to_pixels=true🔗
Iftrue, snapsControlnode vertices to the nearest pixel to ensure they remain crisp even when the camera moves or zooms.
intgui/common/swap_cancel_ok=0🔗
How to position the Cancel and OK buttons in the project'sAcceptDialogwindows. Different platforms have different conventions for this, which can be overridden through this setting.
- Autofollows the platform convention: OK first on Windows, KDE, and LXQt; Cancel first on macOS and other Linux desktop environments.
Autofollows the platform convention: OK first on Windows, KDE, and LXQt; Cancel first on macOS and other Linux desktop environments.
- Cancel Firstforces the Cancel/OK ordering.
Cancel Firstforces the Cancel/OK ordering.
- OK Firstforces the OK/Cancel ordering.
OK Firstforces the OK/Cancel ordering.
To check if these buttons are swapped at runtime, useDisplayServer.get_swap_cancel_ok().
Note:This doesn't affect native dialogs such as the ones spawned byDisplayServer.dialog_show().
intgui/common/text_edit_undo_stack_max_size=1024🔗
Maximum undo/redo history size forTextEditfields.
boolgui/fonts/dynamic_fonts/use_oversampling=true🔗
If set totrueanddisplay/window/stretch/modeis set to"canvas_items", font andDPITextureoversampling is enabled in the main window. UseViewport.oversamplingto control oversampling in other viewports and windows.
Stringgui/theme/custom=""🔗
Path to a customThemeresource file to use for the project (.themeor generic.tres/.resextension).
Stringgui/theme/custom_font=""🔗
Path to a customFontresource to use as default for all GUI elements of the project.
intgui/theme/default_font_antialiasing=1🔗
Font anti-aliasing mode for the default project font. SeeFontFile.antialiasing.
Note:This setting does not affect customFonts used within the project. Use theImportdock for that instead (seeResourceImporterDynamicFont.antialiasing).
boolgui/theme/default_font_generate_mipmaps=false🔗
If set totrue, the default font will have mipmaps generated. This prevents text from looking grainy when aControlis scaled down, or when aLabel3Dis viewed from a long distance (ifLabel3D.texture_filteris set to a mode that displays mipmaps).
Enablinggui/theme/default_font_generate_mipmapsincreases font generation time and memory usage. Only enable this setting if you actually need it.
Note:This setting does not affect customFonts used within the project. Use theImportdock for that instead (seeResourceImporterDynamicFont.generate_mipmaps).
intgui/theme/default_font_hinting=1🔗
Font hinting mode for the default project font. SeeFontFile.hinting.
Note:This setting does not affect customFonts used within the project. Use theImportdock for that instead (seeResourceImporterDynamicFont.hinting).
boolgui/theme/default_font_multichannel_signed_distance_field=false🔗
If set totrue, the default font will use multichannel signed distance field (MSDF) for crisp rendering at any size. Since this approach does not rely on rasterizing the font every time its size changes, this allows for resizing the font in real-time without any performance penalty. Text will also not look grainy forControls that are scaled down (or forLabel3Ds viewed from a long distance).
MSDF font rendering can be combined withgui/theme/default_font_generate_mipmapsto further improve font rendering quality when scaled down.
Note:This setting does not affect customFonts used within the project. Use theImportdock for that instead (seeResourceImporterDynamicFont.multichannel_signed_distance_field).
intgui/theme/default_font_subpixel_positioning=1🔗
Font glyph subpixel positioning mode for the default project font. SeeFontFile.subpixel_positioning.
Note:This setting does not affect customFonts used within the project. Use theImportdock for that instead (seeResourceImporterDynamicFont.subpixel_positioning).
floatgui/theme/default_theme_scale=1.0🔗
The default scale factor forControls, when not overridden by aTheme.
Note:This property is only read when the project starts. To change the default theme scale at runtime, setThemeDB.fallback_base_scaleinstead. However, to adjust the scale of all 2D elements at runtime, it's preferable to useWindow.content_scale_factoron the rootWindownode instead (as this also affects overriddenThemes). SeeMultiple resolutionsin the documentation for details.
intgui/theme/lcd_subpixel_layout=1🔗
LCD subpixel layout used for font anti-aliasing. SeeFontLCDSubpixelLayout.
floatgui/timers/button_shortcut_feedback_highlight_time=0.2🔗
WhenBaseButton.shortcut_feedbackis enabled, this is the time theBaseButtonwill remain highlighted after a shortcut.
intgui/timers/incremental_search_max_interval_msec=2000🔗
Timer setting for incremental search inTree,ItemList, etc. controls (in milliseconds).
floatgui/timers/text_edit_idle_detect_sec=3🔗
Timer for detecting idle inTextEdit(in seconds).
floatgui/timers/tooltip_delay_sec=0.5🔗
Default delay for tooltips (in seconds).
floatgui/timers/tooltip_delay_sec.editor_hint=0.5🔗
Delay for tooltips in the editor.
Dictionaryinput/ui_accept🔗
DefaultInputEventActionto confirm a focused button, menu or list item, or validate input.
Note:Defaultui_*actions cannot be removed as they are necessary for the internal logic of severalControls. The events assigned to the action can however be modified.
Dictionaryinput/ui_accessibility_drag_and_drop🔗
DefaultInputEventActionto start or end a drag-and-drop operation without using mouse.
Note:Defaultui_*actions cannot be removed as they are necessary for the internal logic of severalControls. The events assigned to the action can however be modified.
Dictionaryinput/ui_cancel🔗
DefaultInputEventActionto discard a modal or pending input.
Note:Defaultui_*actions cannot be removed as they are necessary for the internal logic of severalControls. The events assigned to the action can however be modified.
Dictionaryinput/ui_close_dialog🔗
DefaultInputEventActionto close a dialog window.
Note:Defaultui_*actions cannot be removed as they are necessary for the internal logic of severalControls. The events assigned to the action can however be modified.
Dictionaryinput/ui_close_dialog.macos🔗
macOS specific override for the shortcut to close a dialog window.
Dictionaryinput/ui_colorpicker_delete_preset🔗
DefaultInputEventActionto delete a color preset in aColorPicker.
Note:Defaultui_*actions cannot be removed as they are necessary for the internal logic of severalControls. The events assigned to the action can however be modified.
Dictionaryinput/ui_copy🔗
DefaultInputEventActionto copy a selection to the clipboard.
Note:Defaultui_*actions cannot be removed as they are necessary for the internal logic of severalControls. The events assigned to the action can however be modified.
Dictionaryinput/ui_cut🔗
DefaultInputEventActionto cut a selection to the clipboard.
Note:Defaultui_*actions cannot be removed as they are necessary for the internal logic of severalControls. The events assigned to the action can however be modified.
Dictionaryinput/ui_down🔗
DefaultInputEventActionto move down in the UI.
Note:Defaultui_*actions cannot be removed as they are necessary for the internal logic of severalControls. The events assigned to the action can however be modified.
Dictionaryinput/ui_end🔗
DefaultInputEventActionto go to the end position of aControl(e.g. last item in anItemListor aTree), matching the behavior of@GlobalScope.KEY_ENDon typical desktop UI systems.
Note:Defaultui_*actions cannot be removed as they are necessary for the internal logic of severalControls. The events assigned to the action can however be modified.
Dictionaryinput/ui_filedialog_delete🔗
DefaultInputEventActionto delete the selected file in aFileDialog.
Note:Defaultui_*actions cannot be removed as they are necessary for the internal logic of severalControls. The events assigned to the action can however be modified.
Dictionaryinput/ui_filedialog_find🔗
DefaultInputEventActionto open file filter in aFileDialog.
Note:Defaultui_*actions cannot be removed as they are necessary for the internal logic of severalControls. The events assigned to the action can however be modified.
Dictionaryinput/ui_filedialog_focus_path🔗
DefaultInputEventActionto focus path edit field in aFileDialog.
Note:Defaultui_*actions cannot be removed as they are necessary for the internal logic of severalControls. The events assigned to the action can however be modified.
Dictionaryinput/ui_filedialog_focus_path.macos🔗
macOS specific override for the shortcut to focus path edit field inFileDialog.
Dictionaryinput/ui_filedialog_refresh🔗
DefaultInputEventActionto refresh the contents of the current directory of aFileDialog.
Note:Defaultui_*actions cannot be removed as they are necessary for the internal logic of severalControls. The events assigned to the action can however be modified.
Dictionaryinput/ui_filedialog_show_hidden🔗
DefaultInputEventActionto toggle showing hidden files and directories in aFileDialog.
Note:Defaultui_*actions cannot be removed as they are necessary for the internal logic of severalControls. The events assigned to the action can however be modified.
Dictionaryinput/ui_filedialog_up_one_level🔗
DefaultInputEventActionto go up one directory in aFileDialog.
Note:Defaultui_*actions cannot be removed as they are necessary for the internal logic of severalControls. The events assigned to the action can however be modified.
Dictionaryinput/ui_focus_mode🔗
DefaultInputEventActionto switchTextEditinput/ui_text_indentbetween moving keyboard focus to the nextControlin the scene and inputting aTabcharacter.
Note:Defaultui_*actions cannot be removed as they are necessary for the internal logic of severalControls. The events assigned to the action can however be modified.
Dictionaryinput/ui_focus_next🔗
DefaultInputEventActionto focus the nextControlin the scene. The focus behavior can be configured viaControl.focus_next.
Note:Defaultui_*actions cannot be removed as they are necessary for the internal logic of severalControls. The events assigned to the action can however be modified.
Dictionaryinput/ui_focus_prev🔗
DefaultInputEventActionto focus the previousControlin the scene. The focus behavior can be configured viaControl.focus_previous.
Note:Defaultui_*actions cannot be removed as they are necessary for the internal logic of severalControls. The events assigned to the action can however be modified.
Dictionaryinput/ui_graph_delete🔗
DefaultInputEventActionto delete aGraphNodein aGraphEdit.
Note:Defaultui_*actions cannot be removed as they are necessary for the internal logic of severalControls. The events assigned to the action can however be modified.
Dictionaryinput/ui_graph_duplicate🔗
DefaultInputEventActionto duplicate aGraphNodein aGraphEdit.
Note:Defaultui_*actions cannot be removed as they are necessary for the internal logic of severalControls. The events assigned to the action can however be modified.
Dictionaryinput/ui_graph_follow_left🔗
DefaultInputEventActionto follow aGraphNodeinput port connection.
Note:Defaultui_*actions cannot be removed as they are necessary for the internal logic of severalControls. The events assigned to the action can however be modified.
Dictionaryinput/ui_graph_follow_left.macos🔗
macOS specific override for the shortcut to follow aGraphNodeinput port connection.
Dictionaryinput/ui_graph_follow_right🔗
DefaultInputEventActionto follow aGraphNodeoutput port connection.
Note:Defaultui_*actions cannot be removed as they are necessary for the internal logic of severalControls. The events assigned to the action can however be modified.
Dictionaryinput/ui_graph_follow_right.macos🔗
macOS specific override for the shortcut to follow aGraphNodeoutput port connection.
Dictionaryinput/ui_home🔗
DefaultInputEventActionto go to the start position of aControl(e.g. first item in anItemListor aTree), matching the behavior of@GlobalScope.KEY_HOMEon typical desktop UI systems.
Note:Defaultui_*actions cannot be removed as they are necessary for the internal logic of severalControls. The events assigned to the action can however be modified.
Dictionaryinput/ui_left🔗
DefaultInputEventActionto move left in the UI.
Note:Defaultui_*actions cannot be removed as they are necessary for the internal logic of severalControls. The events assigned to the action can however be modified.
Dictionaryinput/ui_menu🔗
DefaultInputEventActionto open a context menu in a text field.
Note:Defaultui_*actions cannot be removed as they are necessary for the internal logic of severalControls. The events assigned to the action can however be modified.
Dictionaryinput/ui_page_down🔗
DefaultInputEventActionto go down a page in aControl(e.g. in anItemListor aTree), matching the behavior of@GlobalScope.KEY_PAGEDOWNon typical desktop UI systems.
Note:Defaultui_*actions cannot be removed as they are necessary for the internal logic of severalControls. The events assigned to the action can however be modified.
Dictionaryinput/ui_page_up🔗
DefaultInputEventActionto go up a page in aControl(e.g. in anItemListor aTree), matching the behavior of@GlobalScope.KEY_PAGEUPon typical desktop UI systems.
Note:Defaultui_*actions cannot be removed as they are necessary for the internal logic of severalControls. The events assigned to the action can however be modified.
Dictionaryinput/ui_paste🔗
DefaultInputEventActionto paste from the clipboard.
Note:Defaultui_*actions cannot be removed as they are necessary for the internal logic of severalControls. The events assigned to the action can however be modified.
Dictionaryinput/ui_redo🔗
DefaultInputEventActionto redo an undone action.
Note:Defaultui_*actions cannot be removed as they are necessary for the internal logic of severalControls. The events assigned to the action can however be modified.
Dictionaryinput/ui_right🔗
DefaultInputEventActionto move right in the UI.
Note:Defaultui_*actions cannot be removed as they are necessary for the internal logic of severalControls. The events assigned to the action can however be modified.
Dictionaryinput/ui_select🔗
DefaultInputEventActionto select an item in aControl(e.g. in anItemListor aTree).
Note:Defaultui_*actions cannot be removed as they are necessary for the internal logic of severalControls. The events assigned to the action can however be modified.
Dictionaryinput/ui_swap_input_direction🔗
DefaultInputEventActionto swap input direction, i.e. change between left-to-right to right-to-left modes. Affects text-editing controls (LineEdit,TextEdit).
Dictionaryinput/ui_text_add_selection_for_next_occurrence🔗
If a selection is currently active with the last caret in text fields, searches for the next occurrence of the selection, adds a caret and selects the next occurrence.
If no selection is currently active with the last caret in text fields, selects the word currently under the caret.
The action can be performed sequentially for all occurrences of the selection of the last caret and for all existing carets.
The viewport is adjusted to the latest newly added caret.
Note:Defaultui_*actions cannot be removed as they are necessary for the internal logic of severalControls. The events assigned to the action can however be modified.
Dictionaryinput/ui_text_backspace🔗
DefaultInputEventActionto delete the character before the text cursor.
Note:Defaultui_*actions cannot be removed as they are necessary for the internal logic of severalControls. The events assigned to the action can however be modified.
Dictionaryinput/ui_text_backspace_all_to_left🔗
DefaultInputEventActionto deletealltext before the text cursor.
Note:Defaultui_*actions cannot be removed as they are necessary for the internal logic of severalControls. The events assigned to the action can however be modified.
Dictionaryinput/ui_text_backspace_all_to_left.macos🔗
macOS specific override for the shortcut to delete all text before the text cursor.
Dictionaryinput/ui_text_backspace_word🔗
DefaultInputEventActionto delete all characters before the cursor up until a whitespace or punctuation character.
Note:Defaultui_*actions cannot be removed as they are necessary for the internal logic of severalControls. The events assigned to the action can however be modified.
Dictionaryinput/ui_text_backspace_word.macos🔗
macOS specific override for the shortcut to delete a word.
Dictionaryinput/ui_text_caret_add_above🔗
DefaultInputEventActionto add an additional caret above every caret of a text.
Dictionaryinput/ui_text_caret_add_above.macos🔗
macOS specific override for the shortcut to add a caret above every caret.
Dictionaryinput/ui_text_caret_add_below🔗
DefaultInputEventActionto add an additional caret below every caret of a text.
Dictionaryinput/ui_text_caret_add_below.macos🔗
macOS specific override for the shortcut to add a caret below every caret.
Dictionaryinput/ui_text_caret_document_end🔗
DefaultInputEventActionto move the text cursor to the end of the text.
Note:Defaultui_*actions cannot be removed as they are necessary for the internal logic of severalControls. The events assigned to the action can however be modified.
Dictionaryinput/ui_text_caret_document_end.macos🔗
macOS specific override for the shortcut to move the text cursor to the end of the text.
Dictionaryinput/ui_text_caret_document_start🔗
DefaultInputEventActionto move the text cursor to the start of the text.
Note:Defaultui_*actions cannot be removed as they are necessary for the internal logic of severalControls. The events assigned to the action can however be modified.
Dictionaryinput/ui_text_caret_document_start.macos🔗
macOS specific override for the shortcut to move the text cursor to the start of the text.
Dictionaryinput/ui_text_caret_down🔗
DefaultInputEventActionto move the text cursor down.
Note:Defaultui_*actions cannot be removed as they are necessary for the internal logic of severalControls. The events assigned to the action can however be modified.
Dictionaryinput/ui_text_caret_left🔗
DefaultInputEventActionto move the text cursor left.
Note:Defaultui_*actions cannot be removed as they are necessary for the internal logic of severalControls. The events assigned to the action can however be modified.
Dictionaryinput/ui_text_caret_line_end🔗
DefaultInputEventActionto move the text cursor to the end of the line.
Note:Defaultui_*actions cannot be removed as they are necessary for the internal logic of severalControls. The events assigned to the action can however be modified.
Dictionaryinput/ui_text_caret_line_end.macos🔗
macOS specific override for the shortcut to move the text cursor to the end of the line.
Dictionaryinput/ui_text_caret_line_start🔗
DefaultInputEventActionto move the text cursor to the start of the line.
Note:Defaultui_*actions cannot be removed as they are necessary for the internal logic of severalControls. The events assigned to the action can however be modified.
Dictionaryinput/ui_text_caret_line_start.macos🔗
macOS specific override for the shortcut to move the text cursor to the start of the line.
Dictionaryinput/ui_text_caret_page_down🔗
DefaultInputEventActionto move the text cursor down one page.
Note:Defaultui_*actions cannot be removed as they are necessary for the internal logic of severalControls. The events assigned to the action can however be modified.
Dictionaryinput/ui_text_caret_page_up🔗
DefaultInputEventActionto move the text cursor up one page.
Note:Defaultui_*actions cannot be removed as they are necessary for the internal logic of severalControls. The events assigned to the action can however be modified.
Dictionaryinput/ui_text_caret_right🔗
DefaultInputEventActionto move the text cursor right.
Note:Defaultui_*actions cannot be removed as they are necessary for the internal logic of severalControls. The events assigned to the action can however be modified.
Dictionaryinput/ui_text_caret_up🔗
DefaultInputEventActionto move the text cursor up.
Note:Defaultui_*actions cannot be removed as they are necessary for the internal logic of severalControls. The events assigned to the action can however be modified.
Dictionaryinput/ui_text_caret_word_left🔗
DefaultInputEventActionto move the text cursor left to the next whitespace or punctuation.
Note:Defaultui_*actions cannot be removed as they are necessary for the internal logic of severalControls. The events assigned to the action can however be modified.
Dictionaryinput/ui_text_caret_word_left.macos🔗
macOS specific override for the shortcut to move the text cursor back one word.
Dictionaryinput/ui_text_caret_word_right🔗
DefaultInputEventActionto move the text cursor right to the next whitespace or punctuation.
Note:Defaultui_*actions cannot be removed as they are necessary for the internal logic of severalControls. The events assigned to the action can however be modified.
Dictionaryinput/ui_text_caret_word_right.macos🔗
macOS specific override for the shortcut to move the text cursor forward one word.
Dictionaryinput/ui_text_clear_carets_and_selection🔗
If there's only one caret active and with a selection, clears the selection.
In case there's more than one caret active, removes the secondary carets and clears their selections.
Note:Defaultui_*actions cannot be removed as they are necessary for the internal logic of severalControls. The events assigned to the action can however be modified.
Dictionaryinput/ui_text_completion_accept🔗
DefaultInputEventActionto accept an autocompletion hint.
Note:Defaultui_*actions cannot be removed as they are necessary for the internal logic of severalControls. The events assigned to the action can however be modified.
Dictionaryinput/ui_text_completion_query🔗
DefaultInputEventActionto request autocompletion.
Note:Defaultui_*actions cannot be removed as they are necessary for the internal logic of severalControls. The events assigned to the action can however be modified.
Dictionaryinput/ui_text_completion_replace🔗
DefaultInputEventActionto accept an autocompletion hint, replacing existing text.
Note:Defaultui_*actions cannot be removed as they are necessary for the internal logic of severalControls. The events assigned to the action can however be modified.
Dictionaryinput/ui_text_dedent🔗
DefaultInputEventActionto unindent text.
Note:Defaultui_*actions cannot be removed as they are necessary for the internal logic of severalControls. The events assigned to the action can however be modified.
Dictionaryinput/ui_text_delete🔗
DefaultInputEventActionto delete the character after the text cursor.
Note:Defaultui_*actions cannot be removed as they are necessary for the internal logic of severalControls. The events assigned to the action can however be modified.
Dictionaryinput/ui_text_delete_all_to_right🔗
DefaultInputEventActionto deletealltext after the text cursor.
Note:Defaultui_*actions cannot be removed as they are necessary for the internal logic of severalControls. The events assigned to the action can however be modified.
Dictionaryinput/ui_text_delete_all_to_right.macos🔗
macOS specific override for the shortcut to delete all text after the text cursor.
Dictionaryinput/ui_text_delete_word🔗
DefaultInputEventActionto delete all characters after the cursor up until a whitespace or punctuation character.
Note:Defaultui_*actions cannot be removed as they are necessary for the internal logic of severalControls. The events assigned to the action can however be modified.
Dictionaryinput/ui_text_delete_word.macos🔗
macOS specific override for the shortcut to delete a word after the text cursor.
Dictionaryinput/ui_text_indent🔗
DefaultInputEventActionto indent the current line.
Note:Defaultui_*actions cannot be removed as they are necessary for the internal logic of severalControls. The events assigned to the action can however be modified.
Dictionaryinput/ui_text_newline🔗
DefaultInputEventActionto insert a new line at the position of the text cursor.
Note:Defaultui_*actions cannot be removed as they are necessary for the internal logic of severalControls. The events assigned to the action can however be modified.
Dictionaryinput/ui_text_newline_above🔗
DefaultInputEventActionto insert a new line before the current one.
Note:Defaultui_*actions cannot be removed as they are necessary for the internal logic of severalControls. The events assigned to the action can however be modified.
Dictionaryinput/ui_text_newline_blank🔗
DefaultInputEventActionto insert a new line after the current one.
Note:Defaultui_*actions cannot be removed as they are necessary for the internal logic of severalControls. The events assigned to the action can however be modified.
Dictionaryinput/ui_text_scroll_down🔗
DefaultInputEventActionto scroll down one line of text.
Note:Defaultui_*actions cannot be removed as they are necessary for the internal logic of severalControls. The events assigned to the action can however be modified.
Dictionaryinput/ui_text_scroll_down.macos🔗
macOS specific override for the shortcut to scroll down one line.
Dictionaryinput/ui_text_scroll_up🔗
DefaultInputEventActionto scroll up one line of text.
Note:Defaultui_*actions cannot be removed as they are necessary for the internal logic of severalControls. The events assigned to the action can however be modified.
Dictionaryinput/ui_text_scroll_up.macos🔗
macOS specific override for the shortcut to scroll up one line.
Dictionaryinput/ui_text_select_all🔗
DefaultInputEventActionto select all text.
Note:Defaultui_*actions cannot be removed as they are necessary for the internal logic of severalControls. The events assigned to the action can however be modified.
Dictionaryinput/ui_text_select_word_under_caret🔗
If no selection is currently active, selects the word currently under the caret in text fields. If a selection is currently active, deselects the current selection.
Note:Defaultui_*actions cannot be removed as they are necessary for the internal logic of severalControls. The events assigned to the action can however be modified.
Dictionaryinput/ui_text_select_word_under_caret.macos🔗
macOS specific override for the shortcut to select the word currently under the caret.
Dictionaryinput/ui_text_skip_selection_for_next_occurrence🔗
If no selection is currently active with the last caret in text fields, searches for the next occurrence of the word currently under the caret and moves the caret to the next occurrence. The action can be performed sequentially for other occurrences of the word under the last caret.
If a selection is currently active with the last caret in text fields, searches for the next occurrence of the selection, adds a caret, selects the next occurrence then deselects the previous selection and its associated caret. The action can be performed sequentially for other occurrences of the selection of the last caret.
The viewport is adjusted to the latest newly added caret.
Note:Defaultui_*actions cannot be removed as they are necessary for the internal logic of severalControls. The events assigned to the action can however be modified.
Dictionaryinput/ui_text_submit🔗
DefaultInputEventActionto submit a text field.
Note:Defaultui_*actions cannot be removed as they are necessary for the internal logic of severalControls. The events assigned to the action can however be modified.
Dictionaryinput/ui_text_toggle_insert_mode🔗
DefaultInputEventActionto toggleinsert modein a text field. While in insert mode, inserting new text overrides the character after the cursor, unless the next character is a new line.
Note:Defaultui_*actions cannot be removed as they are necessary for the internal logic of severalControls. The events assigned to the action can however be modified.
Dictionaryinput/ui_undo🔗
DefaultInputEventActionto undo the most recent action.
Note:Defaultui_*actions cannot be removed as they are necessary for the internal logic of severalControls. The events assigned to the action can however be modified.
Dictionaryinput/ui_unicode_start🔗
DefaultInputEventActionto start Unicode character hexadecimal code input in a text field.
Note:Defaultui_*actions cannot be removed as they are necessary for the internal logic of severalControls. The events assigned to the action can however be modified.
Dictionaryinput/ui_up🔗
DefaultInputEventActionto move up in the UI.
Note:Defaultui_*actions cannot be removed as they are necessary for the internal logic of severalControls. The events assigned to the action can however be modified.
boolinput_devices/buffering/agile_event_flushing=false🔗
Iftrue, key/touch/joystick events will be flushed just before every idle and physics frame.
Iffalse, such events will be flushed only once per process frame, between iterations of the engine.
Enabling this can greatly improve the responsiveness to input, specially in devices that need to run multiple physics frames per visible (process) frame, because they can't run at the target frame rate.
Note:Currently implemented only on Android.
boolinput_devices/compatibility/legacy_just_pressed_behavior=false🔗
Iftrue,Input.is_action_just_pressed()andInput.is_action_just_released()will only returntrueif the action is still in the respective state, i.e. an action that is pressedandreleased on the same frame will be missed.
Iffalse, no input will be lost.
Note:You should in nearly all cases prefer thefalsesetting. The legacy behavior is to enable supporting old projects that rely on the old logic, without changes to script.
Stringinput_devices/pen_tablet/driver🔗
Specifies the tablet driver to use. If left empty, the default driver will be used.
Note:The driver in use can be overridden at runtime via the--tablet-drivercommand line argument.
Note:UseDisplayServer.tablet_set_current_driver()to switch tablet driver in runtime.
Stringinput_devices/pen_tablet/driver.windows🔗
Override forinput_devices/pen_tablet/driveron Windows. Supported values are:
- auto(default), useswintabif Windows Ink is disabled in the Wacom Tablet Properties or system settings,wininkotherwise.
auto(default), useswintabif Windows Ink is disabled in the Wacom Tablet Properties or system settings,wininkotherwise.
- winink, uses Windows native "Windows Ink" driver.
winink, uses Windows native "Windows Ink" driver.
- wintab, uses Wacom "WinTab" driver.
wintab, uses Wacom "WinTab" driver.
- dummy, tablet input is disabled.
dummy, tablet input is disabled.
boolinput_devices/pointing/android/disable_scroll_deadzone=false🔗
Iftrue, disables the scroll deadzone on Android, allowing even very small scroll movements to be registered. This may increase scroll sensitivity but can also lead to unintended scrolling from slight finger movements.
boolinput_devices/pointing/android/enable_long_press_as_right_click=false🔗
Iftrue, long press events on an Android touchscreen are transformed into right click events.
boolinput_devices/pointing/android/enable_pan_and_scale_gestures=false🔗
Iftrue, multi-touch pan and scale gestures are enabled on Android devices.
boolinput_devices/pointing/android/override_volume_buttons=false🔗
Iftrue, system volume changes are disabled when the buttons are used within the app.
intinput_devices/pointing/android/rotary_input_scroll_axis=1🔗
On Wear OS devices, defines which axis of the mouse wheel rotary input is mapped to. This rotary input is usually performed by rotating the physical or virtual (touch-based) bezel on a smartwatch.
boolinput_devices/pointing/emulate_mouse_from_touch=true🔗
Iftrue, sends mouse input events when tapping or swiping on the touchscreen.
boolinput_devices/pointing/emulate_touch_from_mouse=false🔗
Iftrue, sends touch input events when clicking or dragging the mouse.
boolinput_devices/sensors/enable_accelerometer=false🔗
Iftrue, the accelerometer sensor is enabled andInput.get_accelerometer()returns valid data.
boolinput_devices/sensors/enable_gravity=false🔗
Iftrue, the gravity sensor is enabled andInput.get_gravity()returns valid data.
boolinput_devices/sensors/enable_gyroscope=false🔗
Iftrue, the gyroscope sensor is enabled andInput.get_gyroscope()returns valid data.
boolinput_devices/sensors/enable_magnetometer=false🔗
Iftrue, the magnetometer sensor is enabled andInput.get_magnetometer()returns valid data.
Stringinternationalization/locale/fallback="en"🔗
The locale to fall back to if a translation isn't available in a given language. If left empty,en(English) will be used.
Note:Not to be confused withTextServerFallback.
boolinternationalization/locale/include_text_server_data=false🔗
Iftrue, text server break iteration rule sets, dictionaries and other optional data are included in the exported project.
Note:"ICU / HarfBuzz / Graphite" text server data includes dictionaries for Burmese, Chinese, Japanese, Khmer, Lao and Thai as well as Unicode Standard Annex #29 and Unicode Standard Annex #14 word and line breaking rules. Data is about 4 MB large.
Note:TextServerFallbackdoes not use additional data.
intinternationalization/locale/line_breaking_strictness=0🔗
Default strictness of line-breaking rules. Can be overridden by adding@lb={auto,loose,normal,strict}to the language code.
- Auto(0) - strictness is based on the length of the line.
Auto(0) - strictness is based on the length of the line.
- Loose(1) - the least restrictive set of line-breaking rules. Typically used for short lines.
Loose(1) - the least restrictive set of line-breaking rules. Typically used for short lines.
- Normal(2) - the most common set of line-breaking rules.
Normal(2) - the most common set of line-breaking rules.
- Strict(3) - the most stringent set of line-breaking rules.
Strict(3) - the most stringent set of line-breaking rules.
SeeLine Breaking Strictness: the line-break propertyfor more info.
Stringinternationalization/locale/test=""🔗
If non-empty, this locale will be used instead of the automatically detected system locale.
Note:This setting also applies to the exported project. To only affect testing within the editor, override this setting with aneditorfeature tagfor localization testing purposes.
boolinternationalization/pseudolocalization/double_vowels=false🔗
Double vowels in strings during pseudolocalization to simulate the lengthening of text due to localization.
floatinternationalization/pseudolocalization/expansion_ratio=0.0🔗
The expansion ratio to use during pseudolocalization. A value of0.3is sufficient for most practical purposes, and will increase the length of each string by 30%.
boolinternationalization/pseudolocalization/fake_bidi=false🔗
Iftrue, emulate bidirectional (right-to-left) text when pseudolocalization is enabled. This can be used to spot issues with RTL layout and UI mirroring that will crop up if the project is localized to RTL languages such as Arabic or Hebrew. See alsointernationalization/rendering/force_right_to_left_layout_direction.
boolinternationalization/pseudolocalization/override=false🔗
Replace all characters in the string with*. Useful for finding non-localizable strings.
Stringinternationalization/pseudolocalization/prefix="["🔗
Prefix that will be prepended to the pseudolocalized string.
boolinternationalization/pseudolocalization/replace_with_accents=true🔗
Replace all characters with their accented variants during pseudolocalization.
boolinternationalization/pseudolocalization/skip_placeholders=true🔗
Skip placeholders for string formatting like%sor%fduring pseudolocalization. Useful to identify strings which need additional control characters to display correctly.
Stringinternationalization/pseudolocalization/suffix="]"🔗
Suffix that will be appended to the pseudolocalized string.
boolinternationalization/pseudolocalization/use_pseudolocalization=false🔗
Iftrue, enables pseudolocalization for the project. This can be used to spot untranslatable strings or layout issues that may occur once the project is localized to languages that have longer strings than the source language.
Note:This property is only read when the project starts. To toggle pseudolocalization at run-time, useTranslationServer.pseudolocalization_enabledinstead.
boolinternationalization/rendering/force_right_to_left_layout_direction=false🔗
Force layout direction and text writing direction to RTL for all controls, even if the current locale is intended to use a left-to-right layout and text writing direction. This should be enabled for testing purposes only. See alsointernationalization/pseudolocalization/fake_bidi.
boolinternationalization/rendering/root_node_auto_translate=true🔗
Iftrue, root node will useNode.AUTO_TRANSLATE_MODE_ALWAYS, otherwiseNode.AUTO_TRANSLATE_MODE_DISABLEDwill be used.
Note:This property is only read when the project starts. To change the auto translate mode at runtime, setNode.auto_translate_modeofSceneTree.rootinstead.
intinternationalization/rendering/root_node_layout_direction=0🔗
Root node default layout direction.
Stringinternationalization/rendering/text_driver=""🔗
Specifies theTextServerto use. If left empty, the default will be used.
"ICU / HarfBuzz / Graphite" (TextServerAdvanced) is the most advanced text driver, supporting right-to-left typesetting and complex scripts (for languages like Arabic, Hebrew, etc.). The "Fallback" text driver (TextServerFallback) does not support right-to-left typesetting and complex scripts.
Note:The driver in use can be overridden at runtime via the--text-drivercommand line argument.
Note:There is an additionalDummytext driver available, which disables all text rendering and font-related functionality. This driver is not listed in the project settings, but it can be enabled when running the editor or project using the--text-driverDummycommand line argument.
Stringlayer_names/2d_navigation/layer_1=""🔗
Optional name for the 2D navigation layer 1. If left empty, the layer will display as "Layer 1".
Stringlayer_names/2d_navigation/layer_2=""🔗
Optional name for the 2D navigation layer 2. If left empty, the layer will display as "Layer 2".
Stringlayer_names/2d_navigation/layer_3=""🔗
Optional name for the 2D navigation layer 3. If left empty, the layer will display as "Layer 3".
Stringlayer_names/2d_navigation/layer_4=""🔗
Optional name for the 2D navigation layer 4. If left empty, the layer will display as "Layer 4".
Stringlayer_names/2d_navigation/layer_5=""🔗
Optional name for the 2D navigation layer 5. If left empty, the layer will display as "Layer 5".
Stringlayer_names/2d_navigation/layer_6=""🔗
Optional name for the 2D navigation layer 6. If left empty, the layer will display as "Layer 6".
Stringlayer_names/2d_navigation/layer_7=""🔗
Optional name for the 2D navigation layer 7. If left empty, the layer will display as "Layer 7".
Stringlayer_names/2d_navigation/layer_8=""🔗
Optional name for the 2D navigation layer 8. If left empty, the layer will display as "Layer 8".
Stringlayer_names/2d_navigation/layer_9=""🔗
Optional name for the 2D navigation layer 9. If left empty, the layer will display as "Layer 9".
Stringlayer_names/2d_navigation/layer_10=""🔗
Optional name for the 2D navigation layer 10. If left empty, the layer will display as "Layer 10".
Stringlayer_names/2d_navigation/layer_11=""🔗
Optional name for the 2D navigation layer 11. If left empty, the layer will display as "Layer 11".
Stringlayer_names/2d_navigation/layer_12=""🔗
Optional name for the 2D navigation layer 12. If left empty, the layer will display as "Layer 12".
Stringlayer_names/2d_navigation/layer_13=""🔗
Optional name for the 2D navigation layer 13. If left empty, the layer will display as "Layer 13".
Stringlayer_names/2d_navigation/layer_14=""🔗
Optional name for the 2D navigation layer 14. If left empty, the layer will display as "Layer 14".
Stringlayer_names/2d_navigation/layer_15=""🔗
Optional name for the 2D navigation layer 15. If left empty, the layer will display as "Layer 15".
Stringlayer_names/2d_navigation/layer_16=""🔗
Optional name for the 2D navigation layer 16. If left empty, the layer will display as "Layer 16".
Stringlayer_names/2d_navigation/layer_17=""🔗
Optional name for the 2D navigation layer 17. If left empty, the layer will display as "Layer 17".
Stringlayer_names/2d_navigation/layer_18=""🔗
Optional name for the 2D navigation layer 18. If left empty, the layer will display as "Layer 18".
Stringlayer_names/2d_navigation/layer_19=""🔗
Optional name for the 2D navigation layer 19. If left empty, the layer will display as "Layer 19".
Stringlayer_names/2d_navigation/layer_20=""🔗
Optional name for the 2D navigation layer 20. If left empty, the layer will display as "Layer 20".
Stringlayer_names/2d_navigation/layer_21=""🔗
Optional name for the 2D navigation layer 21. If left empty, the layer will display as "Layer 21".
Stringlayer_names/2d_navigation/layer_22=""🔗
Optional name for the 2D navigation layer 22. If left empty, the layer will display as "Layer 22".
Stringlayer_names/2d_navigation/layer_23=""🔗
Optional name for the 2D navigation layer 23. If left empty, the layer will display as "Layer 23".
Stringlayer_names/2d_navigation/layer_24=""🔗
Optional name for the 2D navigation layer 24. If left empty, the layer will display as "Layer 24".
Stringlayer_names/2d_navigation/layer_25=""🔗
Optional name for the 2D navigation layer 25. If left empty, the layer will display as "Layer 25".
Stringlayer_names/2d_navigation/layer_26=""🔗
Optional name for the 2D navigation layer 26. If left empty, the layer will display as "Layer 26".
Stringlayer_names/2d_navigation/layer_27=""🔗
Optional name for the 2D navigation layer 27. If left empty, the layer will display as "Layer 27".
Stringlayer_names/2d_navigation/layer_28=""🔗
Optional name for the 2D navigation layer 28. If left empty, the layer will display as "Layer 28".
Stringlayer_names/2d_navigation/layer_29=""🔗
Optional name for the 2D navigation layer 29. If left empty, the layer will display as "Layer 29".
Stringlayer_names/2d_navigation/layer_30=""🔗
Optional name for the 2D navigation layer 30. If left empty, the layer will display as "Layer 30".
Stringlayer_names/2d_navigation/layer_31=""🔗
Optional name for the 2D navigation layer 31. If left empty, the layer will display as "Layer 31".
Stringlayer_names/2d_navigation/layer_32=""🔗
Optional name for the 2D navigation layer 32. If left empty, the layer will display as "Layer 32".
Stringlayer_names/2d_physics/layer_1=""🔗
Optional name for the 2D physics layer 1. If left empty, the layer will display as "Layer 1".
Stringlayer_names/2d_physics/layer_2=""🔗
Optional name for the 2D physics layer 2. If left empty, the layer will display as "Layer 2".
Stringlayer_names/2d_physics/layer_3=""🔗
Optional name for the 2D physics layer 3. If left empty, the layer will display as "Layer 3".
Stringlayer_names/2d_physics/layer_4=""🔗
Optional name for the 2D physics layer 4. If left empty, the layer will display as "Layer 4".
Stringlayer_names/2d_physics/layer_5=""🔗
Optional name for the 2D physics layer 5. If left empty, the layer will display as "Layer 5".
Stringlayer_names/2d_physics/layer_6=""🔗
Optional name for the 2D physics layer 6. If left empty, the layer will display as "Layer 6".
Stringlayer_names/2d_physics/layer_7=""🔗
Optional name for the 2D physics layer 7. If left empty, the layer will display as "Layer 7".
Stringlayer_names/2d_physics/layer_8=""🔗
Optional name for the 2D physics layer 8. If left empty, the layer will display as "Layer 8".
Stringlayer_names/2d_physics/layer_9=""🔗
Optional name for the 2D physics layer 9. If left empty, the layer will display as "Layer 9".
Stringlayer_names/2d_physics/layer_10=""🔗
Optional name for the 2D physics layer 10. If left empty, the layer will display as "Layer 10".
Stringlayer_names/2d_physics/layer_11=""🔗
Optional name for the 2D physics layer 11. If left empty, the layer will display as "Layer 11".
Stringlayer_names/2d_physics/layer_12=""🔗
Optional name for the 2D physics layer 12. If left empty, the layer will display as "Layer 12".
Stringlayer_names/2d_physics/layer_13=""🔗
Optional name for the 2D physics layer 13. If left empty, the layer will display as "Layer 13".
Stringlayer_names/2d_physics/layer_14=""🔗
Optional name for the 2D physics layer 14. If left empty, the layer will display as "Layer 14".
Stringlayer_names/2d_physics/layer_15=""🔗
Optional name for the 2D physics layer 15. If left empty, the layer will display as "Layer 15".
Stringlayer_names/2d_physics/layer_16=""🔗
Optional name for the 2D physics layer 16. If left empty, the layer will display as "Layer 16".
Stringlayer_names/2d_physics/layer_17=""🔗
Optional name for the 2D physics layer 17. If left empty, the layer will display as "Layer 17".
Stringlayer_names/2d_physics/layer_18=""🔗
Optional name for the 2D physics layer 18. If left empty, the layer will display as "Layer 18".
Stringlayer_names/2d_physics/layer_19=""🔗
Optional name for the 2D physics layer 19. If left empty, the layer will display as "Layer 19".
Stringlayer_names/2d_physics/layer_20=""🔗
Optional name for the 2D physics layer 20. If left empty, the layer will display as "Layer 20".
Stringlayer_names/2d_physics/layer_21=""🔗
Optional name for the 2D physics layer 21. If left empty, the layer will display as "Layer 21".
Stringlayer_names/2d_physics/layer_22=""🔗
Optional name for the 2D physics layer 22. If left empty, the layer will display as "Layer 22".
Stringlayer_names/2d_physics/layer_23=""🔗
Optional name for the 2D physics layer 23. If left empty, the layer will display as "Layer 23".
Stringlayer_names/2d_physics/layer_24=""🔗
Optional name for the 2D physics layer 24. If left empty, the layer will display as "Layer 24".
Stringlayer_names/2d_physics/layer_25=""🔗
Optional name for the 2D physics layer 25. If left empty, the layer will display as "Layer 25".
Stringlayer_names/2d_physics/layer_26=""🔗
Optional name for the 2D physics layer 26. If left empty, the layer will display as "Layer 26".
Stringlayer_names/2d_physics/layer_27=""🔗
Optional name for the 2D physics layer 27. If left empty, the layer will display as "Layer 27".
Stringlayer_names/2d_physics/layer_28=""🔗
Optional name for the 2D physics layer 28. If left empty, the layer will display as "Layer 28".
Stringlayer_names/2d_physics/layer_29=""🔗
Optional name for the 2D physics layer 29. If left empty, the layer will display as "Layer 29".
Stringlayer_names/2d_physics/layer_30=""🔗
Optional name for the 2D physics layer 30. If left empty, the layer will display as "Layer 30".
Stringlayer_names/2d_physics/layer_31=""🔗
Optional name for the 2D physics layer 31. If left empty, the layer will display as "Layer 31".
Stringlayer_names/2d_physics/layer_32=""🔗
Optional name for the 2D physics layer 32. If left empty, the layer will display as "Layer 32".
Stringlayer_names/2d_render/layer_1=""🔗
Optional name for the 2D render layer 1. If left empty, the layer will display as "Layer 1".
Stringlayer_names/2d_render/layer_2=""🔗
Optional name for the 2D render layer 2. If left empty, the layer will display as "Layer 2".
Stringlayer_names/2d_render/layer_3=""🔗
Optional name for the 2D render layer 3. If left empty, the layer will display as "Layer 3".
Stringlayer_names/2d_render/layer_4=""🔗
Optional name for the 2D render layer 4. If left empty, the layer will display as "Layer 4".
Stringlayer_names/2d_render/layer_5=""🔗
Optional name for the 2D render layer 5. If left empty, the layer will display as "Layer 5".
Stringlayer_names/2d_render/layer_6=""🔗
Optional name for the 2D render layer 6. If left empty, the layer will display as "Layer 6".
Stringlayer_names/2d_render/layer_7=""🔗
Optional name for the 2D render layer 7. If left empty, the layer will display as "Layer 7".
Stringlayer_names/2d_render/layer_8=""🔗
Optional name for the 2D render layer 8. If left empty, the layer will display as "Layer 8".
Stringlayer_names/2d_render/layer_9=""🔗
Optional name for the 2D render layer 9. If left empty, the layer will display as "Layer 9".
Stringlayer_names/2d_render/layer_10=""🔗
Optional name for the 2D render layer 10. If left empty, the layer will display as "Layer 10".
Stringlayer_names/2d_render/layer_11=""🔗
Optional name for the 2D render layer 11. If left empty, the layer will display as "Layer 11".
Stringlayer_names/2d_render/layer_12=""🔗
Optional name for the 2D render layer 12. If left empty, the layer will display as "Layer 12".
Stringlayer_names/2d_render/layer_13=""🔗
Optional name for the 2D render layer 13. If left empty, the layer will display as "Layer 13".
Stringlayer_names/2d_render/layer_14=""🔗
Optional name for the 2D render layer 14. If left empty, the layer will display as "Layer 14".
Stringlayer_names/2d_render/layer_15=""🔗
Optional name for the 2D render layer 15. If left empty, the layer will display as "Layer 15".
Stringlayer_names/2d_render/layer_16=""🔗
Optional name for the 2D render layer 16. If left empty, the layer will display as "Layer 16".
Stringlayer_names/2d_render/layer_17=""🔗
Optional name for the 2D render layer 17. If left empty, the layer will display as "Layer 17".
Stringlayer_names/2d_render/layer_18=""🔗
Optional name for the 2D render layer 18. If left empty, the layer will display as "Layer 18".
Stringlayer_names/2d_render/layer_19=""🔗
Optional name for the 2D render layer 19. If left empty, the layer will display as "Layer 19".
Stringlayer_names/2d_render/layer_20=""🔗
Optional name for the 2D render layer 20. If left empty, the layer will display as "Layer 20".
Stringlayer_names/3d_navigation/layer_1=""🔗
Optional name for the 3D navigation layer 1. If left empty, the layer will display as "Layer 1".
Stringlayer_names/3d_navigation/layer_2=""🔗
Optional name for the 3D navigation layer 2. If left empty, the layer will display as "Layer 2".
Stringlayer_names/3d_navigation/layer_3=""🔗
Optional name for the 3D navigation layer 3. If left empty, the layer will display as "Layer 3".
Stringlayer_names/3d_navigation/layer_4=""🔗
Optional name for the 3D navigation layer 4. If left empty, the layer will display as "Layer 4".
Stringlayer_names/3d_navigation/layer_5=""🔗
Optional name for the 3D navigation layer 5. If left empty, the layer will display as "Layer 5".
Stringlayer_names/3d_navigation/layer_6=""🔗
Optional name for the 3D navigation layer 6. If left empty, the layer will display as "Layer 6".
Stringlayer_names/3d_navigation/layer_7=""🔗
Optional name for the 3D navigation layer 7. If left empty, the layer will display as "Layer 7".
Stringlayer_names/3d_navigation/layer_8=""🔗
Optional name for the 3D navigation layer 8. If left empty, the layer will display as "Layer 8".
Stringlayer_names/3d_navigation/layer_9=""🔗
Optional name for the 3D navigation layer 9. If left empty, the layer will display as "Layer 9".
Stringlayer_names/3d_navigation/layer_10=""🔗
Optional name for the 3D navigation layer 10. If left empty, the layer will display as "Layer 10".
Stringlayer_names/3d_navigation/layer_11=""🔗
Optional name for the 3D navigation layer 11. If left empty, the layer will display as "Layer 11".
Stringlayer_names/3d_navigation/layer_12=""🔗
Optional name for the 3D navigation layer 12. If left empty, the layer will display as "Layer 12".
Stringlayer_names/3d_navigation/layer_13=""🔗
Optional name for the 3D navigation layer 13. If left empty, the layer will display as "Layer 13".
Stringlayer_names/3d_navigation/layer_14=""🔗
Optional name for the 3D navigation layer 14. If left empty, the layer will display as "Layer 14".
Stringlayer_names/3d_navigation/layer_15=""🔗
Optional name for the 3D navigation layer 15. If left empty, the layer will display as "Layer 15".
Stringlayer_names/3d_navigation/layer_16=""🔗
Optional name for the 3D navigation layer 16. If left empty, the layer will display as "Layer 16".
Stringlayer_names/3d_navigation/layer_17=""🔗
Optional name for the 3D navigation layer 17. If left empty, the layer will display as "Layer 17".
Stringlayer_names/3d_navigation/layer_18=""🔗
Optional name for the 3D navigation layer 18. If left empty, the layer will display as "Layer 18".
Stringlayer_names/3d_navigation/layer_19=""🔗
Optional name for the 3D navigation layer 19. If left empty, the layer will display as "Layer 19".
Stringlayer_names/3d_navigation/layer_20=""🔗
Optional name for the 3D navigation layer 20. If left empty, the layer will display as "Layer 20".
Stringlayer_names/3d_navigation/layer_21=""🔗
Optional name for the 3D navigation layer 21. If left empty, the layer will display as "Layer 21".
Stringlayer_names/3d_navigation/layer_22=""🔗
Optional name for the 3D navigation layer 22. If left empty, the layer will display as "Layer 22".
Stringlayer_names/3d_navigation/layer_23=""🔗
Optional name for the 3D navigation layer 23. If left empty, the layer will display as "Layer 23".
Stringlayer_names/3d_navigation/layer_24=""🔗
Optional name for the 3D navigation layer 24. If left empty, the layer will display as "Layer 24".
Stringlayer_names/3d_navigation/layer_25=""🔗
Optional name for the 3D navigation layer 25. If left empty, the layer will display as "Layer 25".
Stringlayer_names/3d_navigation/layer_26=""🔗
Optional name for the 3D navigation layer 26. If left empty, the layer will display as "Layer 26".
Stringlayer_names/3d_navigation/layer_27=""🔗
Optional name for the 3D navigation layer 27. If left empty, the layer will display as "Layer 27".
Stringlayer_names/3d_navigation/layer_28=""🔗
Optional name for the 3D navigation layer 28. If left empty, the layer will display as "Layer 28".
Stringlayer_names/3d_navigation/layer_29=""🔗
Optional name for the 3D navigation layer 29. If left empty, the layer will display as "Layer 29".
Stringlayer_names/3d_navigation/layer_30=""🔗
Optional name for the 3D navigation layer 30. If left empty, the layer will display as "Layer 30".
Stringlayer_names/3d_navigation/layer_31=""🔗
Optional name for the 3D navigation layer 31. If left empty, the layer will display as "Layer 31".
Stringlayer_names/3d_navigation/layer_32=""🔗
Optional name for the 3D navigation layer 32. If left empty, the layer will display as "Layer 32".
Stringlayer_names/3d_physics/layer_1=""🔗
Optional name for the 3D physics layer 1. If left empty, the layer will display as "Layer 1".
Stringlayer_names/3d_physics/layer_2=""🔗
Optional name for the 3D physics layer 2. If left empty, the layer will display as "Layer 2".
Stringlayer_names/3d_physics/layer_3=""🔗
Optional name for the 3D physics layer 3. If left empty, the layer will display as "Layer 3".
Stringlayer_names/3d_physics/layer_4=""🔗
Optional name for the 3D physics layer 4. If left empty, the layer will display as "Layer 4".
Stringlayer_names/3d_physics/layer_5=""🔗
Optional name for the 3D physics layer 5. If left empty, the layer will display as "Layer 5".
Stringlayer_names/3d_physics/layer_6=""🔗
Optional name for the 3D physics layer 6. If left empty, the layer will display as "Layer 6".
Stringlayer_names/3d_physics/layer_7=""🔗
Optional name for the 3D physics layer 7. If left empty, the layer will display as "Layer 7".
Stringlayer_names/3d_physics/layer_8=""🔗
Optional name for the 3D physics layer 8. If left empty, the layer will display as "Layer 8".
Stringlayer_names/3d_physics/layer_9=""🔗
Optional name for the 3D physics layer 9. If left empty, the layer will display as "Layer 9".
Stringlayer_names/3d_physics/layer_10=""🔗
Optional name for the 3D physics layer 10. If left empty, the layer will display as "Layer 10".
Stringlayer_names/3d_physics/layer_11=""🔗
Optional name for the 3D physics layer 11. If left empty, the layer will display as "Layer 11".
Stringlayer_names/3d_physics/layer_12=""🔗
Optional name for the 3D physics layer 12. If left empty, the layer will display as "Layer 12".
Stringlayer_names/3d_physics/layer_13=""🔗
Optional name for the 3D physics layer 13. If left empty, the layer will display as "Layer 13".
Stringlayer_names/3d_physics/layer_14=""🔗
Optional name for the 3D physics layer 14. If left empty, the layer will display as "Layer 14".
Stringlayer_names/3d_physics/layer_15=""🔗
Optional name for the 3D physics layer 15. If left empty, the layer will display as "Layer 15".
Stringlayer_names/3d_physics/layer_16=""🔗
Optional name for the 3D physics layer 16. If left empty, the layer will display as "Layer 16".
Stringlayer_names/3d_physics/layer_17=""🔗
Optional name for the 3D physics layer 17. If left empty, the layer will display as "Layer 17".
Stringlayer_names/3d_physics/layer_18=""🔗
Optional name for the 3D physics layer 18. If left empty, the layer will display as "Layer 18".
Stringlayer_names/3d_physics/layer_19=""🔗
Optional name for the 3D physics layer 19. If left empty, the layer will display as "Layer 19".
Stringlayer_names/3d_physics/layer_20=""🔗
Optional name for the 3D physics layer 20. If left empty, the layer will display as "Layer 20".
Stringlayer_names/3d_physics/layer_21=""🔗
Optional name for the 3D physics layer 21. If left empty, the layer will display as "Layer 21".
Stringlayer_names/3d_physics/layer_22=""🔗
Optional name for the 3D physics layer 22. If left empty, the layer will display as "Layer 22".
Stringlayer_names/3d_physics/layer_23=""🔗
Optional name for the 3D physics layer 23. If left empty, the layer will display as "Layer 23".
Stringlayer_names/3d_physics/layer_24=""🔗
Optional name for the 3D physics layer 24. If left empty, the layer will display as "Layer 24".
Stringlayer_names/3d_physics/layer_25=""🔗
Optional name for the 3D physics layer 25. If left empty, the layer will display as "Layer 25".
Stringlayer_names/3d_physics/layer_26=""🔗
Optional name for the 3D physics layer 26. If left empty, the layer will display as "Layer 26".
Stringlayer_names/3d_physics/layer_27=""🔗
Optional name for the 3D physics layer 27. If left empty, the layer will display as "Layer 27".
Stringlayer_names/3d_physics/layer_28=""🔗
Optional name for the 3D physics layer 28. If left empty, the layer will display as "Layer 28".
Stringlayer_names/3d_physics/layer_29=""🔗
Optional name for the 3D physics layer 29. If left empty, the layer will display as "Layer 29".
Stringlayer_names/3d_physics/layer_30=""🔗
Optional name for the 3D physics layer 30. If left empty, the layer will display as "Layer 30".
Stringlayer_names/3d_physics/layer_31=""🔗
Optional name for the 3D physics layer 31. If left empty, the layer will display as "Layer 31".
Stringlayer_names/3d_physics/layer_32=""🔗
Optional name for the 3D physics layer 32. If left empty, the layer will display as "Layer 32".
Stringlayer_names/3d_render/layer_1=""🔗
Optional name for the 3D render layer 1. If left empty, the layer will display as "Layer 1".
Stringlayer_names/3d_render/layer_2=""🔗
Optional name for the 3D render layer 2. If left empty, the layer will display as "Layer 2".
Stringlayer_names/3d_render/layer_3=""🔗
Optional name for the 3D render layer 3. If left empty, the layer will display as "Layer 3".
Stringlayer_names/3d_render/layer_4=""🔗
Optional name for the 3D render layer 4. If left empty, the layer will display as "Layer 4".
Stringlayer_names/3d_render/layer_5=""🔗
Optional name for the 3D render layer 5. If left empty, the layer will display as "Layer 5".
Stringlayer_names/3d_render/layer_6=""🔗
Optional name for the 3D render layer 6. If left empty, the layer will display as "Layer 6".
Stringlayer_names/3d_render/layer_7=""🔗
Optional name for the 3D render layer 7. If left empty, the layer will display as "Layer 7".
Stringlayer_names/3d_render/layer_8=""🔗
Optional name for the 3D render layer 8. If left empty, the layer will display as "Layer 8".
Stringlayer_names/3d_render/layer_9=""🔗
Optional name for the 3D render layer 9. If left empty, the layer will display as "Layer 9".
Stringlayer_names/3d_render/layer_10=""🔗
Optional name for the 3D render layer 10. If left empty, the layer will display as "Layer 10".
Stringlayer_names/3d_render/layer_11=""🔗
Optional name for the 3D render layer 11. If left empty, the layer will display as "Layer 11".
Stringlayer_names/3d_render/layer_12=""🔗
Optional name for the 3D render layer 12. If left empty, the layer will display as "Layer 12".
Stringlayer_names/3d_render/layer_13=""🔗
Optional name for the 3D render layer 13. If left empty, the layer will display as "Layer 13".
Stringlayer_names/3d_render/layer_14=""🔗
Optional name for the 3D render layer 14. If left empty, the layer will display as "Layer 14".
Stringlayer_names/3d_render/layer_15=""🔗
Optional name for the 3D render layer 15. If left empty, the layer will display as "Layer 15".
Stringlayer_names/3d_render/layer_16=""🔗
Optional name for the 3D render layer 16. If left empty, the layer will display as "Layer 16".
Stringlayer_names/3d_render/layer_17=""🔗
Optional name for the 3D render layer 17. If left empty, the layer will display as "Layer 17".
Stringlayer_names/3d_render/layer_18=""🔗
Optional name for the 3D render layer 18. If left empty, the layer will display as "Layer 18".
Stringlayer_names/3d_render/layer_19=""🔗
Optional name for the 3D render layer 19. If left empty, the layer will display as "Layer 19".
Stringlayer_names/3d_render/layer_20=""🔗
Optional name for the 3D render layer 20. If left empty, the layer will display as "Layer 20".
Stringlayer_names/avoidance/layer_1=""🔗
Optional name for the navigation avoidance layer 1. If left empty, the layer will display as "Layer 1".
Stringlayer_names/avoidance/layer_2=""🔗
Optional name for the navigation avoidance layer 2. If left empty, the layer will display as "Layer 2".
Stringlayer_names/avoidance/layer_3=""🔗
Optional name for the navigation avoidance layer 3. If left empty, the layer will display as "Layer 3".
Stringlayer_names/avoidance/layer_4=""🔗
Optional name for the navigation avoidance layer 4. If left empty, the layer will display as "Layer 4".
Stringlayer_names/avoidance/layer_5=""🔗
Optional name for the navigation avoidance layer 5. If left empty, the layer will display as "Layer 5".
Stringlayer_names/avoidance/layer_6=""🔗
Optional name for the navigation avoidance layer 6. If left empty, the layer will display as "Layer 6".
Stringlayer_names/avoidance/layer_7=""🔗
Optional name for the navigation avoidance layer 7. If left empty, the layer will display as "Layer 7".
Stringlayer_names/avoidance/layer_8=""🔗
Optional name for the navigation avoidance layer 8. If left empty, the layer will display as "Layer 8".
Stringlayer_names/avoidance/layer_9=""🔗
Optional name for the navigation avoidance layer 9. If left empty, the layer will display as "Layer 9".
Stringlayer_names/avoidance/layer_10=""🔗
Optional name for the navigation avoidance layer 10. If left empty, the layer will display as "Layer 10".
Stringlayer_names/avoidance/layer_11=""🔗
Optional name for the navigation avoidance layer 11. If left empty, the layer will display as "Layer 11".
Stringlayer_names/avoidance/layer_12=""🔗
Optional name for the navigation avoidance layer 12. If left empty, the layer will display as "Layer 12".
Stringlayer_names/avoidance/layer_13=""🔗
Optional name for the navigation avoidance layer 13. If left empty, the layer will display as "Layer 13".
Stringlayer_names/avoidance/layer_14=""🔗
Optional name for the navigation avoidance layer 14. If left empty, the layer will display as "Layer 14".
Stringlayer_names/avoidance/layer_15=""🔗
Optional name for the navigation avoidance layer 15. If left empty, the layer will display as "Layer 15".
Stringlayer_names/avoidance/layer_16=""🔗
Optional name for the navigation avoidance layer 16. If left empty, the layer will display as "Layer 16".
Stringlayer_names/avoidance/layer_17=""🔗
Optional name for the navigation avoidance layer 17. If left empty, the layer will display as "Layer 17".
Stringlayer_names/avoidance/layer_18=""🔗
Optional name for the navigation avoidance layer 18. If left empty, the layer will display as "Layer 18".
Stringlayer_names/avoidance/layer_19=""🔗
Optional name for the navigation avoidance layer 19. If left empty, the layer will display as "Layer 19".
Stringlayer_names/avoidance/layer_20=""🔗
Optional name for the navigation avoidance layer 20. If left empty, the layer will display as "Layer 20".
Stringlayer_names/avoidance/layer_21=""🔗
Optional name for the navigation avoidance layer 21. If left empty, the layer will display as "Layer 21".
Stringlayer_names/avoidance/layer_22=""🔗
Optional name for the navigation avoidance layer 22. If left empty, the layer will display as "Layer 22".
Stringlayer_names/avoidance/layer_23=""🔗
Optional name for the navigation avoidance layer 23. If left empty, the layer will display as "Layer 23".
Stringlayer_names/avoidance/layer_24=""🔗
Optional name for the navigation avoidance layer 24. If left empty, the layer will display as "Layer 24".
Stringlayer_names/avoidance/layer_25=""🔗
Optional name for the navigation avoidance layer 25. If left empty, the layer will display as "Layer 25".
Stringlayer_names/avoidance/layer_26=""🔗
Optional name for the navigation avoidance layer 26. If left empty, the layer will display as "Layer 26".
Stringlayer_names/avoidance/layer_27=""🔗
Optional name for the navigation avoidance layer 27. If left empty, the layer will display as "Layer 27".
Stringlayer_names/avoidance/layer_28=""🔗
Optional name for the navigation avoidance layer 28. If left empty, the layer will display as "Layer 28".
Stringlayer_names/avoidance/layer_29=""🔗
Optional name for the navigation avoidance layer 29. If left empty, the layer will display as "Layer 29".
Stringlayer_names/avoidance/layer_30=""🔗
Optional name for the navigation avoidance layer 30. If left empty, the layer will display as "Layer 30".
Stringlayer_names/avoidance/layer_31=""🔗
Optional name for the navigation avoidance layer 31. If left empty, the layer will display as "Layer 31".
Stringlayer_names/avoidance/layer_32=""🔗
Optional name for the navigation avoidance layer 32. If left empty, the layer will display as "Layer 32".
intmemory/limits/message_queue/max_size_mb=32🔗
Godot uses a message queue to defer some function calls. If you run out of space on it (you will see an error), you can increase the size here.
floatnavigation/2d/default_cell_size=1.0🔗
Default cell size for 2D navigation maps. SeeNavigationServer2D.map_set_cell_size().
floatnavigation/2d/default_edge_connection_margin=1.0🔗
Default edge connection margin for 2D navigation maps. SeeNavigationServer2D.map_set_edge_connection_margin().
floatnavigation/2d/default_link_connection_radius=4.0🔗
Default link connection radius for 2D navigation maps. SeeNavigationServer2D.map_set_link_connection_radius().
floatnavigation/2d/merge_rasterizer_cell_scale=1.0🔗
Default merge rasterizer cell scale for 2D navigation maps. SeeNavigationServer2D.map_set_merge_rasterizer_cell_scale().
Stringnavigation/2d/navigation_engine="DEFAULT"🔗
Sets which navigation engine to use for 2D navigation.
DEFAULTis equivalent toGodotNavigation2D, but may change in future releases. Select an explicit implementation if you want to ensure that your project stays on the same engine.
GodotNavigation2Dis Godot's internal 2D navigation engine.
Dummyis a 2D navigation server that does nothing and returns only dummy values, effectively disabling all 2D navigation functionality.
Third-party modules can add other navigation engines to select with this setting.
boolnavigation/2d/use_edge_connections=true🔗
If enabled 2D navigation regions will use edge connections to connect with other navigation regions within proximity of the navigation map edge connection margin. This setting only affects World2D default navigation maps.
boolnavigation/2d/warnings/navmesh_cell_size_mismatch=true🔗
Iftrue, the navigation system will print warnings when a navigation mesh with a small cell size is used on a navigation map with a larger size as this commonly causes rasterization errors.
boolnavigation/2d/warnings/navmesh_edge_merge_errors=true🔗
Iftrue, the navigation system will print warnings about navigation mesh edge merge errors occurring in navigation regions or maps.
floatnavigation/3d/default_cell_height=0.25🔗
Default cell height for 3D navigation maps. SeeNavigationServer3D.map_set_cell_height().
floatnavigation/3d/default_cell_size=0.25🔗
Default cell size for 3D navigation maps. SeeNavigationServer3D.map_set_cell_size().
floatnavigation/3d/default_edge_connection_margin=0.25🔗
Default edge connection margin for 3D navigation maps. SeeNavigationServer3D.map_set_edge_connection_margin().
floatnavigation/3d/default_link_connection_radius=1.0🔗
Default link connection radius for 3D navigation maps. SeeNavigationServer3D.map_set_link_connection_radius().
Vector3navigation/3d/default_up=Vector3(0,1,0)🔗
Default up orientation for 3D navigation maps. SeeNavigationServer3D.map_set_up().
floatnavigation/3d/merge_rasterizer_cell_scale=1.0🔗
Default merge rasterizer cell scale for 3D navigation maps. SeeNavigationServer3D.map_set_merge_rasterizer_cell_scale().
Stringnavigation/3d/navigation_engine="DEFAULT"🔗
Sets which navigation engine to use for 3D navigation.
DEFAULTis equivalent toGodotNavigation3D, but may change in future releases. Select an explicit implementation if you want to ensure that your project stays on the same engine.
GodotNavigation3Dis Godot's internal 3D navigation engine.
Dummyis a 3D navigation server that does nothing and returns only dummy values, effectively disabling all 3D navigation functionality.
Third-party modules can add other navigation engines to select with this setting.
boolnavigation/3d/use_edge_connections=true🔗
If enabled 3D navigation regions will use edge connections to connect with other navigation regions within proximity of the navigation map edge connection margin. This setting only affects World3D default navigation maps.
boolnavigation/3d/warnings/navmesh_cell_size_mismatch=true🔗
Iftrue, the navigation system will print warnings when a navigation mesh with a small cell size (or in 3D height) is used on a navigation map with a larger size as this commonly causes rasterization errors.
boolnavigation/3d/warnings/navmesh_edge_merge_errors=true🔗
Iftrue, the navigation system will print warnings about navigation mesh edge merge errors occurring in navigation regions or maps.
boolnavigation/avoidance/thread_model/avoidance_use_high_priority_threads=true🔗
If enabled and avoidance calculations use multiple threads the threads run with high priority.
boolnavigation/avoidance/thread_model/avoidance_use_multiple_threads=true🔗
If enabled the avoidance calculations use multiple threads.
boolnavigation/baking/thread_model/baking_use_high_priority_threads=true🔗
If enabled and async navmesh baking uses multiple threads the threads run with high priority.
boolnavigation/baking/thread_model/baking_use_multiple_threads=true🔗
If enabled the async navmesh baking uses multiple threads.
boolnavigation/baking/use_crash_prevention_checks=true🔗
If enabled, and baking would potentially lead to an engine crash, the baking will be interrupted and an error message with explanation will be raised.
intnavigation/pathfinding/max_threads=4🔗
Maximum number of threads that can run pathfinding queries simultaneously on the same pathfinding graph, for example the same navigation map. Additional threads increase memory consumption and synchronization time due to the need for extra data copies prepared for each thread. A value of-1means unlimited and the maximum available OS processor count is used. Defaults to1when the OS does not support threads.
boolnavigation/world/map_use_async_iterations=true🔗
If enabled, navigation map synchronization uses an async process that runs on a background thread. This avoids stalling the main thread but adds an additional delay to any navigation map change.
boolnavigation/world/region_use_async_iterations=true🔗
If enabled, navigation region synchronization uses an async process that runs on a background thread. This avoids stalling the main thread but adds an additional delay to any navigation region change.
intnetwork/limits/debugger/max_chars_per_second=32768🔗
Maximum number of characters allowed to send as output from the debugger. Over this value, content is dropped. This helps not to stall the debugger connection.
intnetwork/limits/debugger/max_errors_per_second=400🔗
Maximum number of errors allowed to be sent from the debugger. Over this value, content is dropped. This helps not to stall the debugger connection.
intnetwork/limits/debugger/max_queued_messages=2048🔗
Maximum number of messages in the debugger queue. Over this value, content is dropped. This helps to limit the debugger memory usage.
intnetwork/limits/debugger/max_warnings_per_second=400🔗
Maximum number of warnings allowed to be sent from the debugger. Over this value, content is dropped. This helps not to stall the debugger connection.
intnetwork/limits/packet_peer_stream/max_buffer_po2=16🔗
Default size of packet peer stream for deserializing Godot data (in bytes, specified as a power of two). The default value16is equal to 65,536 bytes. Over this size, data is dropped.
intnetwork/limits/tcp/connect_timeout_seconds=30🔗
Timeout (in seconds) for connection attempts using TCP.
intnetwork/limits/unix/connect_timeout_seconds=30🔗
Timeout (in seconds) for connection attempts using UNIX domain socket.
intnetwork/limits/webrtc/max_channel_in_buffer_kb=64🔗
Maximum size (in kiB) for theWebRTCDataChannelinput buffer.
Stringnetwork/tls/certificate_bundle_override=""🔗
The CA certificates bundle to use for TLS connections. If this is set to a non-empty value, this willoverrideGodot's defaultMozilla certificate bundle. If left empty, the default certificate bundle will be used.
If in doubt, leave this setting empty.
boolnetwork/tls/enable_tls_v1.3=true🔗
Iftrue, enable TLSv1.3 negotiation.
Note:Only supported when using Mbed TLS 3.0 or later (Linux distribution packages may be compiled against older system Mbed TLS packages), otherwise the maximum supported TLS version is always TLSv1.2.
floatphysics/2d/default_angular_damp=1.0🔗
The default rotational motion damping in 2D. Damping is used to gradually slow down physical objects over time. RigidBodies will fall back to this value when combining their own damping values and no area damping value is present.
Suggested values are in the range0to30. At value0objects will keep moving with the same velocity. Greater values will stop the object faster. A value equal to or greater than the physics tick rate (physics/common/physics_ticks_per_second) will bring the object to a stop in one iteration.
Note:Godot damping calculations are velocity-dependent, meaning bodies moving faster will take a longer time to come to rest. They do not simulate inertia, friction, or air resistance. Therefore heavier or larger bodies will lose speed at the same proportional rate as lighter or smaller bodies.
During each physics tick, Godot will multiply the linear velocity of RigidBodies by1.0-combined_damp/physics_ticks_per_second. By default, bodies combine damp factors:combined_dampis the sum of the damp value of the body and this value or the area's value the body is in. SeeDampMode.
Warning:Godot's damping calculations are simulation tick rate dependent. Changingphysics/common/physics_ticks_per_secondmay significantly change the outcomes and feel of your simulation. This is true for the entire range of damping values greater than 0. To get back to a similar feel, you also need to change your damp values. This needed change is not proportional and differs from case to case.
floatphysics/2d/default_gravity=980.0🔗
The default gravity strength in 2D (in pixels per second squared).
Note:This property is only read when the project starts. To change the default gravity at runtime, use the following code sample:

```
# Set the default gravity strength to 980.
PhysicsServer2D.area_set_param(get_viewport().find_world_2d().space, PhysicsServer2D.AREA_PARAM_GRAVITY, 980)
```

```
// Set the default gravity strength to 980.
PhysicsServer2D.AreaSetParam(GetViewport().FindWorld2D().Space, PhysicsServer2D.AreaParameter.Gravity, 980);
```

Vector2physics/2d/default_gravity_vector=Vector2(0,1)🔗
The default gravity direction in 2D.
Note:This property is only read when the project starts. To change the default gravity vector at runtime, use the following code sample:

```
# Set the default gravity direction to `Vector2(0, 1)`.
PhysicsServer2D.area_set_param(get_viewport().find_world_2d().space, PhysicsServer2D.AREA_PARAM_GRAVITY_VECTOR, Vector2.DOWN)
```

```
// Set the default gravity direction to `Vector2(0, 1)`.
PhysicsServer2D.AreaSetParam(GetViewport().FindWorld2D().Space, PhysicsServer2D.AreaParameter.GravityVector, Vector2.Down)
```

floatphysics/2d/default_linear_damp=0.1🔗
The default linear motion damping in 2D. Damping is used to gradually slow down physical objects over time. RigidBodies will fall back to this value when combining their own damping values and no area damping value is present.
Suggested values are in the range0to30. At value0objects will keep moving with the same velocity. Greater values will stop the object faster. A value equal to or greater than the physics tick rate (physics/common/physics_ticks_per_second) will bring the object to a stop in one iteration.
Note:Godot damping calculations are velocity-dependent, meaning bodies moving faster will take a longer time to come to rest. They do not simulate inertia, friction, or air resistance. Therefore heavier or larger bodies will lose speed at the same proportional rate as lighter or smaller bodies.
During each physics tick, Godot will multiply the linear velocity of RigidBodies by1.0-combined_damp/physics_ticks_per_second, wherecombined_dampis the sum of the linear damp of the body and this value, or the area's value the body is in, assuming the body defaults to combine damp values. SeeDampMode.
Warning:Godot's damping calculations are simulation tick rate dependent. Changingphysics/common/physics_ticks_per_secondmay significantly change the outcomes and feel of your simulation. This is true for the entire range of damping values greater than 0. To get back to a similar feel, you also need to change your damp values. This needed change is not proportional and differs from case to case.
Stringphysics/2d/physics_engine="DEFAULT"🔗
Sets which physics engine to use for 2D physics.
DEFAULTis currently equivalent toGodotPhysics2D, but may change in future releases. Select an explicit implementation if you want to ensure that your project stays on the same engine.
GodotPhysics2Dis Godot's internal 2D physics engine.
Dummyis a 2D physics server that does nothing and returns only dummy values, effectively disabling all 2D physics functionality.
Third-party extensions and modules can add other physics engines to select with this setting.
boolphysics/2d/run_on_separate_thread=false🔗
Iftrue, the 2D physics server runs on a separate thread, making better use of multi-core CPUs. Iffalse, the 2D physics server runs on the main thread. Running the physics server on a separate thread can increase performance, but restricts API access to only physics process.
floatphysics/2d/sleep_threshold_angular=0.13962634🔗
Threshold angular velocity under which a 2D physics body will be considered inactive. SeePhysicsServer2D.SPACE_PARAM_BODY_ANGULAR_VELOCITY_SLEEP_THRESHOLD.
floatphysics/2d/sleep_threshold_linear=2.0🔗
Threshold linear velocity under which a 2D physics body will be considered inactive. SeePhysicsServer2D.SPACE_PARAM_BODY_LINEAR_VELOCITY_SLEEP_THRESHOLD.
floatphysics/2d/solver/contact_max_allowed_penetration=0.3🔗
Maximum distance a shape can penetrate another shape before it is considered a collision. SeePhysicsServer2D.SPACE_PARAM_CONTACT_MAX_ALLOWED_PENETRATION.
floatphysics/2d/solver/contact_max_separation=1.5🔗
Maximum distance a shape can be from another before they are considered separated and the contact is discarded. SeePhysicsServer2D.SPACE_PARAM_CONTACT_MAX_SEPARATION.
floatphysics/2d/solver/contact_recycle_radius=1.0🔗
Maximum distance a pair of bodies has to move before their collision status has to be recalculated. SeePhysicsServer2D.SPACE_PARAM_CONTACT_RECYCLE_RADIUS.
floatphysics/2d/solver/default_constraint_bias=0.2🔗
Default solver bias for all physics constraints. Defines how much bodies react to enforce constraints. SeePhysicsServer2D.SPACE_PARAM_CONSTRAINT_DEFAULT_BIAS.
Individual constraints can have a specific bias value (seeJoint2D.bias).
floatphysics/2d/solver/default_contact_bias=0.8🔗
Default solver bias for all physics contacts. Defines how much bodies react to enforce contact separation. SeePhysicsServer2D.SPACE_PARAM_CONTACT_DEFAULT_BIAS.
Individual shapes can have a specific bias value (seeShape2D.custom_solver_bias).
intphysics/2d/solver/solver_iterations=16🔗
Number of solver iterations for all contacts and constraints. The greater the number of iterations, the more accurate the collisions will be. However, a greater number of iterations requires more CPU power, which can decrease performance. SeePhysicsServer2D.SPACE_PARAM_SOLVER_ITERATIONS.
floatphysics/2d/time_before_sleep=0.5🔗
Time (in seconds) of inactivity before which a 2D physics body will put to sleep. SeePhysicsServer2D.SPACE_PARAM_BODY_TIME_TO_SLEEP.
floatphysics/3d/default_angular_damp=0.1🔗
The default rotational motion damping in 3D. Damping is used to gradually slow down physical objects over time. RigidBodies will fall back to this value when combining their own damping values and no area damping value is present.
Suggested values are in the range0to30. At value0objects will keep moving with the same velocity. Greater values will stop the object faster. A value equal to or greater than the physics tick rate (physics/common/physics_ticks_per_second) will bring the object to a stop in one iteration.
Note:Godot damping calculations are velocity-dependent, meaning bodies moving faster will take a longer time to come to rest. They do not simulate inertia, friction, or air resistance. Therefore heavier or larger bodies will lose speed at the same proportional rate as lighter or smaller bodies.
During each physics tick, Godot will multiply the angular velocity of RigidBodies by1.0-combined_damp/physics_ticks_per_second. By default, bodies combine damp factors:combined_dampis the sum of the damp value of the body and this value or the area's value the body is in. SeeDampMode.
Warning:Godot's damping calculations are simulation tick rate dependent. Changingphysics/common/physics_ticks_per_secondmay significantly change the outcomes and feel of your simulation. This is true for the entire range of damping values greater than 0. To get back to a similar feel, you also need to change your damp values. This needed change is not proportional and differs from case to case.
floatphysics/3d/default_gravity=9.8🔗
The default gravity strength in 3D (in meters per second squared).
Note:This property is only read when the project starts. To change the default gravity at runtime, use the following code sample:

```
# Set the default gravity strength to 9.8.
PhysicsServer3D.area_set_param(get_viewport().find_world_3d().space, PhysicsServer3D.AREA_PARAM_GRAVITY, 9.8)
```

```
// Set the default gravity strength to 9.8.
PhysicsServer3D.AreaSetParam(GetViewport().FindWorld3D().Space, PhysicsServer3D.AreaParameter.Gravity, 9.8);
```

Vector3physics/3d/default_gravity_vector=Vector3(0,-1,0)🔗
The default gravity direction in 3D.
Note:This property is only read when the project starts. To change the default gravity vector at runtime, use the following code sample:

```
# Set the default gravity direction to `Vector3(0, -1, 0)`.
PhysicsServer3D.area_set_param(get_viewport().find_world_3d().space, PhysicsServer3D.AREA_PARAM_GRAVITY_VECTOR, Vector3.DOWN)
```

```
// Set the default gravity direction to `Vector3(0, -1, 0)`.
PhysicsServer3D.AreaSetParam(GetViewport().FindWorld3D().Space, PhysicsServer3D.AreaParameter.GravityVector, Vector3.Down)
```

floatphysics/3d/default_linear_damp=0.1🔗
The default linear motion damping in 3D. Damping is used to gradually slow down physical objects over time. RigidBodies will fall back to this value when combining their own damping values and no area damping value is present.
Suggested values are in the range0to30. At value0objects will keep moving with the same velocity. Greater values will stop the object faster. A value equal to or greater than the physics tick rate (physics/common/physics_ticks_per_second) will bring the object to a stop in one iteration.
Note:Godot damping calculations are velocity-dependent, meaning bodies moving faster will take a longer time to come to rest. They do not simulate inertia, friction, or air resistance. Therefore heavier or larger bodies will lose speed at the same proportional rate as lighter or smaller bodies.
During each physics tick, Godot will multiply the linear velocity of RigidBodies by1.0-combined_damp/physics_ticks_per_second. By default, bodies combine damp factors:combined_dampis the sum of the damp value of the body and this value or the area's value the body is in. SeeDampMode.
Warning:Godot's damping calculations are simulation tick rate dependent. Changingphysics/common/physics_ticks_per_secondmay significantly change the outcomes and feel of your simulation. This is true for the entire range of damping values greater than 0. To get back to a similar feel, you also need to change your damp values. This needed change is not proportional and differs from case to case.
Stringphysics/3d/physics_engine="DEFAULT"🔗
Sets which physics engine to use for 3D physics.
DEFAULTis currently equivalent toGodotPhysics3D, but may change in future releases. Select an explicit implementation if you want to ensure that your project stays on the same engine.
GodotPhysics3Dis Godot's internal 3D physics engine.
Jolt Physicsis an alternative physics engine that is generally faster and more reliable thanGodotPhysics3D. Jolt Physics is the default for projects created starting in Godot 4.6.
Dummyis a 3D physics server that does nothing and returns only dummy values, effectively disabling all 3D physics functionality.
Third-party extensions and modules can add other physics engines to select with this setting.
Stringphysics/3d/physics_interpolation/scene_traversal="DEFAULT"🔗
The approach used for 3D scene traversal when physics interpolation is enabled.

- DEFAULT: The default optimized method.
DEFAULT: The default optimized method.
- Legacy: The previous reference method used for scene tree traversal, which is slower.
Legacy: The previous reference method used for scene tree traversal, which is slower.
- Debug: Swaps betweenDEFAULTandLegacymethods on alternating frames, and provides logging information (which in turn makes it slower). Intended for debugging only; you should use theDEFAULTmethod in most cases.
Debug: Swaps betweenDEFAULTandLegacymethods on alternating frames, and provides logging information (which in turn makes it slower). Intended for debugging only; you should use theDEFAULTmethod in most cases.
boolphysics/3d/run_on_separate_thread=false🔗
Iftrue, the 3D physics server runs on a separate thread, making better use of multi-core CPUs. Iffalse, the 3D physics server runs on the main thread. Running the physics server on a separate thread can increase performance, but restricts API access to only physics process.
Note:Whenphysics/3d/physics_engineis set toJoltPhysics, enabling this setting will prevent the 3D physics server from being able to provide any context when reporting errors and warnings, and will instead always refer to nodes as<unknown>.
floatphysics/3d/sleep_threshold_angular=0.13962634🔗
Threshold angular velocity under which a 3D physics body will be considered inactive. SeePhysicsServer3D.SPACE_PARAM_BODY_ANGULAR_VELOCITY_SLEEP_THRESHOLD.
floatphysics/3d/sleep_threshold_linear=0.1🔗
Threshold linear velocity under which a 3D physics body will be considered inactive. SeePhysicsServer3D.SPACE_PARAM_BODY_LINEAR_VELOCITY_SLEEP_THRESHOLD.
floatphysics/3d/solver/contact_max_allowed_penetration=0.01🔗
Maximum distance a shape can penetrate another shape before it is considered a collision. SeePhysicsServer3D.SPACE_PARAM_CONTACT_MAX_ALLOWED_PENETRATION.
floatphysics/3d/solver/contact_max_separation=0.05🔗
Maximum distance a shape can be from another before they are considered separated and the contact is discarded. SeePhysicsServer3D.SPACE_PARAM_CONTACT_MAX_SEPARATION.
floatphysics/3d/solver/contact_recycle_radius=0.01🔗
Maximum distance a pair of bodies has to move before their collision status has to be recalculated. SeePhysicsServer3D.SPACE_PARAM_CONTACT_RECYCLE_RADIUS.
floatphysics/3d/solver/default_contact_bias=0.8🔗
Default solver bias for all physics contacts. Defines how much bodies react to enforce contact separation. SeePhysicsServer3D.SPACE_PARAM_CONTACT_DEFAULT_BIAS.
Individual shapes can have a specific bias value (seeShape3D.custom_solver_bias).
intphysics/3d/solver/solver_iterations=16🔗
Number of solver iterations for all contacts and constraints. The greater the number of iterations, the more accurate the collisions will be. However, a greater number of iterations requires more CPU power, which can decrease performance. SeePhysicsServer3D.SPACE_PARAM_SOLVER_ITERATIONS.
floatphysics/3d/time_before_sleep=0.5🔗
Time (in seconds) of inactivity before which a 3D physics body will put to sleep. SeePhysicsServer3D.SPACE_PARAM_BODY_TIME_TO_SLEEP.
boolphysics/common/enable_object_picking=true🔗
EnablesViewport.physics_object_pickingon the root viewport.
intphysics/common/max_physics_steps_per_frame=8🔗
Controls the maximum number of physics steps that can be simulated each rendered frame. The default value is tuned to avoid situations where the framerate suddenly drops to a very low value beyond a certain amount of physics simulation. This occurs because the physics engine can't keep up with the expected simulation rate. In this case, the framerate will start dropping, but the engine is only allowed to simulate a certain number of physics steps per rendered frame. This snowballs into a situation where framerate keeps dropping until it reaches a very low framerate (typically 1-2 FPS) and is called thephysics spiral of death.
However, the game will appear to slow down if the rendering FPS is less than1/max_physics_steps_per_frameofphysics/common/physics_ticks_per_second. This occurs even ifdeltais consistently used in physics calculations. To avoid this, increasephysics/common/max_physics_steps_per_frameif you have increasedphysics/common/physics_ticks_per_secondsignificantly above its default value.
Note:This property is only read when the project starts. To change the maximum number of simulated physics steps per frame at runtime, setEngine.max_physics_steps_per_frameinstead.
boolphysics/common/physics_interpolation=false🔗
Iftrue, the renderer will interpolate the transforms of objects (both physics and non-physics) between the last two transforms, so that smooth motion is seen even when physics ticks do not coincide with rendered frames. See alsoNode.reset_physics_interpolation().
Note:Although this is a global setting, finer control of individual branches of theSceneTreeis possible usingNode.physics_interpolation_mode.
Note:This property is only read when the project starts. To toggle physics interpolation at runtime, setSceneTree.physics_interpolationinstead.
Note:Propertyphysics/common/physics_jitter_fixis automatically disabled ifphysics/common/physics_interpolationis set totrue, as the two methods are incompatible.
floatphysics/common/physics_jitter_fix=0.5🔗
Controls how much physics ticks are synchronized with real time. For 0 or less, the ticks are synchronized. Such values are recommended for network games, where clock synchronization matters. Higher values cause higher deviation of in-game clock and real clock, but allows smoothing out framerate jitters. The default value of 0.5 should be good enough for most; values above 2 could cause the game to react to dropped frames with a noticeable delay and are not recommended.
Note:Jitter fix is automatically disabled at runtime whenphysics/common/physics_interpolationis enabled.
Note:When using a custom physics interpolation solution, the physics jitter fix should be disabled by settingphysics/common/physics_jitter_fixto0.0.
Note:This property is only read when the project starts. To change the physics jitter fix at runtime, setEngine.physics_jitter_fixinstead.
intphysics/common/physics_ticks_per_second=60🔗
The number of fixed iterations per second. This controls how often physics simulation and theNode._physics_process()method are run.
CPU usage scales approximately with the physics tick rate. However, at very low tick rates (usually below 30), physics behavior can break down. Input can also become less responsive at low tick rates as there can be a gap between input being registered, and the response on the next physics tick. High tick rates give more accurate physics simulation, particularly for fast moving objects. For example, racing games may benefit from increasing the tick rate above the default 60.
See alsoapplication/run/max_fps.
Note:This property is only read when the project starts. To change the physics FPS at runtime, setEngine.physics_ticks_per_secondinstead.
Note:Onlyphysics/common/max_physics_steps_per_framephysics ticks may be simulated per rendered frame at most. If more physics ticks have to be simulated per rendered frame to keep up with rendering, the project will appear to slow down (even ifdeltais used consistently in physics calculations). Therefore, it is recommended to also increasephysics/common/max_physics_steps_per_frameif increasingphysics/common/physics_ticks_per_secondsignificantly above its default value.
Note:Consider enablingphysics interpolationif you changephysics/common/physics_ticks_per_secondto a value that is not a multiple of60. Using physics interpolation will avoid jittering when the monitor refresh rate and physics update rate don't exactly match.
floatphysics/jolt_physics_3d/collisions/active_edge_threshold=0.87266463🔗
The maximum angle, in radians, between two adjacent triangles in aConcavePolygonShape3DorHeightMapShape3Dfor which the edge between those triangles is considered inactive.
Collisions against an inactive edge will have its normal overridden to instead be the surface normal of the triangle. This can help alleviate ghost collisions.
Note:Setting this too high can result in objects not depenetrating properly.
Note:This applies to all shape queries, as well as physics bodies within the simulation.
Note:This does not apply when enabling Jolt's enhanced internal edge removal, which supersedes this.
floatphysics/jolt_physics_3d/collisions/collision_margin_fraction=0.08🔗
The amount of collision margin to use for certain convex collision shapes, such asBoxShape3D,CylinderShape3DandConvexPolygonShape3D, as a fraction of the shape's shortest axis, withShape3D.marginas the upper bound. This is mainly used to speed up collision detection with convex shapes.
Note:Collision margins in Jolt do not add any extra size to the shape. Instead the shape is first shrunk by the margin and then expanded by the same amount, resulting in a shape with rounded corners.
Note:Setting this value too close to0.0may also negatively affect the accuracy of the collision detection with convex shapes.
intphysics/jolt_physics_3d/joints/world_node=0🔗
Which of the two nodes bound by a joint should represent the world when one of the two is omitted, as eitherJoint3D.node_aorJoint3D.node_b. This can be thought of as having the omitted node be aStaticBody3Dat the joint's position. Joint limits are more easily expressed whenJoint3D.node_arepresents the world.
Note:In Godot Physics, onlyJoint3D.node_bcan represent the world.
floatphysics/jolt_physics_3d/limits/max_angular_velocity=47.12389🔗
The maximum angular velocity that aRigidBody3Dcan reach, in radians per second.
This is mainly used as a fail-safe, to prevent the simulation from exploding, as fast-moving objects colliding with complex physics structures can otherwise cause them to go out of control. Fast-moving objects can also cause a lot of stress on the collision detection system, which can slow down the simulation considerably.
intphysics/jolt_physics_3d/limits/max_bodies=10240🔗
The maximum number ofPhysicsBody3Dto support at the same time, awake or sleeping. When this limit is exceeded, an error is reported and anything past that point is undefined behavior.
Note:This limit also applies within the editor.
intphysics/jolt_physics_3d/limits/max_body_pairs=65536🔗
The maximum number of body pairs to allow processing of. When this limit is exceeded, a warning is reported and collisions will randomly be ignored while bodies pass through each other.
intphysics/jolt_physics_3d/limits/max_contact_constraints=20480🔗
The maximum number of contact constraints to allow processing of. When this limit is exceeded, a warning is reported and collisions will randomly be ignored while bodies pass through each other.
floatphysics/jolt_physics_3d/limits/max_linear_velocity=500.0🔗
The maximum linear velocity that aRigidBody3Dcan reach, in meters per second.
This is mainly used as a fail-safe, to prevent the simulation from exploding, as fast-moving objects colliding with complex physics structures can otherwise cause them to go out of control. Fast-moving objects can also cause a lot of stress on the collision detection system, which can slow down the simulation considerably.
intphysics/jolt_physics_3d/limits/temporary_memory_buffer_size=32🔗
The amount of memory to pre-allocate for the stack allocator used within Jolt, in MiB. This allocator is used within the physics step to store things that are only needed during it, like which bodies are in contact, how they form islands and the data needed to solve the contacts.
floatphysics/jolt_physics_3d/limits/world_boundary_shape_size=2000.0🔗
The size ofWorldBoundaryShape3Dboundaries, for all three dimensions. The plane is effectively centered within a box of this size, and anything outside of the box will not collide with it. This is necessary asWorldBoundaryShape3Dis not unbounded when using Jolt, in order to prevent precision issues.
Note:Setting this value too high can make collision detection less accurate.
Note:Collisions against the effective edges of aWorldBoundaryShape3Dwill be inconsistent.
floatphysics/jolt_physics_3d/motion_queries/recovery_amount=0.4🔗
Fraction of the total penetration to depenetrate per iteration during motion queries.
Note:This affects methodsCharacterBody3D.move_and_slide(),PhysicsBody3D.move_and_collide(),PhysicsBody3D.test_move()andPhysicsServer3D.body_test_motion().
intphysics/jolt_physics_3d/motion_queries/recovery_iterations=4🔗
The number of iterations to run when depenetrating during motion queries.
Note:This affects methodsCharacterBody3D.move_and_slide(),PhysicsBody3D.move_and_collide(),PhysicsBody3D.test_move()andPhysicsServer3D.body_test_motion().
boolphysics/jolt_physics_3d/motion_queries/use_enhanced_internal_edge_removal=true🔗
Iftrue, enables Jolt's enhanced internal edge removal during motion queries. This can help alleviate ghost collisions, but only with edges within a single body, meaning edges between separate bodies can still cause ghost collisions.
Note:This affects methodsCharacterBody3D.move_and_slide(),PhysicsBody3D.move_and_collide(),PhysicsBody3D.test_move()andPhysicsServer3D.body_test_motion().
boolphysics/jolt_physics_3d/queries/enable_ray_cast_face_index=false🔗
Iftrue, populates theface_indexfield in the results ofPhysicsDirectSpaceState3D.intersect_ray(), also accessed throughRayCast3D.get_collision_face_index(). Iffalse, theface_indexfield will be left at its default value of-1.
Note:Enabling this setting will increase Jolt's memory usage forConcavePolygonShape3Dby around 25%.
boolphysics/jolt_physics_3d/queries/use_enhanced_internal_edge_removal=false🔗
Iftrue, enables Jolt's enhanced internal edge removal during shape queries. This can help alleviate ghost collisions when using shape queries for things like character movement, but only with edges within a single body, meaning edges between separate bodies can still cause ghost collisions.
Note:This affects methodsPhysicsDirectSpaceState3D.cast_motion(),PhysicsDirectSpaceState3D.collide_shape(),PhysicsDirectSpaceState3D.get_rest_info()andPhysicsDirectSpaceState3D.intersect_shape().
Note:Enabling this setting can cause certain shapes to be culled from the results entirely, but you will get at least one intersection per body.
boolphysics/jolt_physics_3d/simulation/allow_sleep=true🔗
Iftrue,RigidBody3Dnodes are allowed to go to sleep if their velocity is below the threshold defined inphysics/jolt_physics_3d/simulation/sleep_velocity_thresholdfor the duration set inphysics/jolt_physics_3d/simulation/sleep_time_threshold. This can improve physics simulation performance when there are non-movingRigidBody3Dnodes, at the cost of some nodes possibly failing to wake up in certain scenarios. Consider disabling this temporarily to troubleshootRigidBody3Dnodes not moving when they should.
floatphysics/jolt_physics_3d/simulation/baumgarte_stabilization_factor=0.2🔗
How much of the position error of aRigidBody3Dto fix during a physics step, where0.0is none and1.0is the full amount. This affects things like how quickly bodies depenetrate.
Note:Setting this value too high can makeRigidBody3Dnodes unstable.
floatphysics/jolt_physics_3d/simulation/body_pair_contact_cache_angle_threshold=0.034906585🔗
The maximum relative angle by which a body pair can move and still reuse the collision results from the previous physics step, in radians.
floatphysics/jolt_physics_3d/simulation/body_pair_contact_cache_distance_threshold=0.001🔗
The maximum relative distance by which a body pair can move and still reuse the collision results from the previous physics step, in meters.
boolphysics/jolt_physics_3d/simulation/body_pair_contact_cache_enabled=true🔗
Iftrue, enables the body pair contact cache, which removes the need for potentially expensive collision detection when the relative orientation between two bodies hasn't changed much.
floatphysics/jolt_physics_3d/simulation/bounce_velocity_threshold=1.0🔗
The minimum velocity needed before a collision can be bouncy, in meters per second.
floatphysics/jolt_physics_3d/simulation/continuous_cd_max_penetration=0.25🔗
Fraction of a body's inner radius that may penetrate another body while using continuous collision detection.
floatphysics/jolt_physics_3d/simulation/continuous_cd_movement_threshold=0.75🔗
Fraction of a body's inner radius that the body must move per step to make use of continuous collision detection.
boolphysics/jolt_physics_3d/simulation/generate_all_kinematic_contacts=false🔗
Iftrue, aRigidBody3Dfrozen withRigidBody3D.FREEZE_MODE_KINEMATICis able to collide with other kinematic and static bodies, and therefore generate contacts for them.
Note:This setting can come at a heavy CPU and memory cost if you allow many/large frozen kinematic bodies with a non-zeroRigidBody3D.max_contacts_reportedto overlap with complex static geometry, such asConcavePolygonShape3DorHeightMapShape3D.
floatphysics/jolt_physics_3d/simulation/penetration_slop=0.02🔗
How much bodies are allowed to penetrate each other, in meters.
intphysics/jolt_physics_3d/simulation/position_steps=2🔗
Number of solver position iterations. The greater the number of iterations, the more accurate the simulation will be, at the cost of CPU performance.
floatphysics/jolt_physics_3d/simulation/sleep_time_threshold=0.5🔗
Time in seconds aRigidBody3Dwill spend below the sleep velocity threshold before going to sleep.
floatphysics/jolt_physics_3d/simulation/sleep_velocity_threshold=0.03🔗
The linear velocity of specific points on the bounding box of aRigidBody3D, below which it can be put to sleep, in meters per second. These points help capture both the linear and angular motion of aRigidBody3D.
floatphysics/jolt_physics_3d/simulation/soft_body_point_radius=0.01🔗
How big the points of aSoftBody3Dare, in meters. A higher value can prevent behavior such as cloth laying perfectly flush against other surfaces and causing Z-fighting.
floatphysics/jolt_physics_3d/simulation/speculative_contact_distance=0.02🔗
Radius around physics bodies, inside which speculative contact points will be detected, in meters. This is mainly used to prevent tunneling/penetration forRigidBody3Dnodes during simulation.
Note:Setting this too high may result in ghost collisions, as speculative contacts are based on the closest points during the collision detection step which may not be the actual closest points by the time the two bodies hit.
boolphysics/jolt_physics_3d/simulation/use_enhanced_internal_edge_removal=true🔗
Iftrue, enables Jolt's enhanced internal edge removal forRigidBody3D. This can help alleviate ghost collisions when, for example, aRigidBody3Dcollides with the edges of two perfectly joinedBoxShape3D. The removal only applies to edges internal to a single body, meaning edges between separate bodies can still cause ghost collisions.
intphysics/jolt_physics_3d/simulation/velocity_steps=10🔗
Number of solver velocity iterations. The greater the number of iterations, the more accurate the simulation will be, at the cost of CPU performance.
Note:This needs to be at least2in order for friction to work, as friction is applied using the non-penetration impulse from the previous iteration.
intrendering/2d/batching/item_buffer_size=16384🔗
Maximum number of canvas item commands that can be batched into a single draw call.
intrendering/2d/batching/uniform_set_cache_size=4096🔗
Maximum number of uniform sets that will be cached by the 2D renderer when batching draw calls.
Note:Increasing this value can improve performance if the project renders many unique sprite textures every frame.
intrendering/2d/sdf/oversize=1🔗
Controls how much of the original viewport size should be covered by the 2D signed distance field. This SDF can be sampled inCanvasItemshaders and is used forGPUParticles2Dcollision. Higher values allow portions of occluders located outside the viewport to still be taken into account in the generated signed distance field, at the cost of performance. If you notice particles falling throughLightOccluder2Ds as the occluders leave the viewport, increase this setting.
The percentage specified is added on each axis and on both sides. For example, with the default setting of 120%, the signed distance field will cover 20% of the viewport's size outside the viewport on each side (top, right, bottom, left).
Note:This property is only read when the project starts. To change the 2D SDF oversizing percentage at runtime, useRenderingServer.viewport_set_sdf_oversize_and_scale()instead.
intrendering/2d/sdf/scale=1🔗
The resolution scale to use for the 2D signed distance field. Higher values lead to a more precise and more stable signed distance field as the camera moves, at the cost of performance. The default value (50%) renders at half the resolution of the viewport size on each axis, which means the SDF is generated with 25% of the viewport's pixel count.
Note:This property is only read when the project starts. To change the 2D SDF resolution scale at runtime, useRenderingServer.viewport_set_sdf_oversize_and_scale()instead.
intrendering/2d/shadow_atlas/size=2048🔗
The size of the 2D shadow atlas in pixels. Higher values result in more preciseLight2Dshadows, at the cost of performance and video memory usage. The specified value is rounded up to the nearest power of 2.
Note:This property is only read when the project starts. To change the 2D shadow atlas size at runtime, useRenderingServer.canvas_set_shadow_texture_size()instead.
boolrendering/2d/snap/snap_2d_transforms_to_pixel=false🔗
Iftrue,CanvasItemnodes will internally snap to full pixels. Useful for low-resolution pixel art games. Their position can still be sub-pixel, but the decimals will not have effect as the position is rounded. This can lead to a crisper appearance at the cost of less smooth movement, especially whenCamera2Dsmoothing is enabled.
Note:This property is only read when the project starts. To toggle 2D transform snapping at runtime, useRenderingServer.viewport_set_snap_2d_transforms_to_pixel()on the rootViewportinstead.
Note:Controlnodes are snapped to the nearest pixel by default. This is controlled bygui/common/snap_controls_to_pixels.
Note:It is not recommended to use this setting together withrendering/2d/snap/snap_2d_vertices_to_pixel, as movement may appear even less smooth. Prefer only enabling this setting instead.
boolrendering/2d/snap/snap_2d_vertices_to_pixel=false🔗
Iftrue, vertices ofCanvasItemnodes will snap to full pixels. Useful for low-resolution pixel art games. Only affects the final vertex positions, not the transforms. This can lead to a crisper appearance at the cost of less smooth movement, especially whenCamera2Dsmoothing is enabled.
Note:This property is only read when the project starts. To toggle 2D vertex snapping at runtime, useRenderingServer.viewport_set_snap_2d_vertices_to_pixel()on the rootViewportinstead.
Note:Controlnodes are snapped to the nearest pixel by default. This is controlled bygui/common/snap_controls_to_pixels.
Note:It is not recommended to use this setting together withrendering/2d/snap/snap_2d_transforms_to_pixel, as movement may appear even less smooth. Prefer only enabling that setting instead.
intrendering/anti_aliasing/quality/msaa_2d=0🔗
Sets the number of multisample antialiasing (MSAA) samples to use for 2D/Canvas rendering (as a power of two). MSAA is used to reduce aliasing around the edges of polygons. A higher MSAA value results in smoother edges but can be significantly slower on some hardware, especially integrated graphics due to their limited memory bandwidth. This has no effect on shader-induced aliasing or texture aliasing.
Note:MSAA is only supported in the Forward+ and Mobile rendering methods, not Compatibility.
Note:This property is only read when the project starts. To set the number of 2D MSAA samples at runtime, setViewport.msaa_2dor useRenderingServer.viewport_set_msaa_2d().
intrendering/anti_aliasing/quality/msaa_3d=0🔗
Sets the number of multisample antialiasing (MSAA) samples to use for 3D rendering (as a power of two). MSAA is used to reduce aliasing around the edges of polygons. A higher MSAA value results in smoother edges but can be significantly slower on some hardware, especially integrated graphics due to their limited memory bandwidth. See alsorendering/scaling_3d/modefor supersampling, which provides higher quality but is much more expensive. This has no effect on shader-induced aliasing or texture aliasing.
Note:This property is only read when the project starts. To set the number of 3D MSAA samples at runtime, setViewport.msaa_3dor useRenderingServer.viewport_set_msaa_3d().
intrendering/anti_aliasing/quality/screen_space_aa=0🔗
Sets the screen-space antialiasing mode for the default screenViewport. Screen-space antialiasing works by selectively blurring edges in a post-process shader. It differs from MSAA which takes multiple coverage samples while rendering objects. Screen-space AA methods are typically faster than MSAA and will smooth out specular aliasing, but tend to make scenes appear blurry. The blurriness is partially counteracted by automatically using a negative mipmap LOD bias (seerendering/textures/default_filters/texture_mipmap_bias).
Another way to combat specular aliasing is to enablerendering/anti_aliasing/screen_space_roughness_limiter/enabled.
Note:Screen-space antialiasing is only supported in the Forward+ and Mobile rendering methods, not Compatibility.
Note:This property is only read when the project starts. To set the screen-space antialiasing mode at runtime, setViewport.screen_space_aaon the rootViewportinstead, or useRenderingServer.viewport_set_screen_space_aa().
floatrendering/anti_aliasing/quality/smaa_edge_detection_threshold=0.05🔗
Sets the sensitivity to edges when using SMAA for antialiasing. Lower values will catch more edges, at a potentially higher performance cost.
Note:This property is only read when the project starts. There is currently no way to change this setting at run-time.
boolrendering/anti_aliasing/quality/use_debanding=false🔗
Iftrue, uses a fast dithering filter just before transforming floating point color values to integer color values to make banding significantly less visible. Debanding is applied at different steps of the rendering process depending on the rendering method andrendering/viewport/hdr_2dsetting.
In some cases, debanding may introduce a slightly noticeable dithering pattern. It's recommended to enable debanding only when actually needed since the dithering pattern will make lossless-compressed screenshots larger.
Note:This property is only read when the project starts and configuresRenderingServer.material_set_use_debanding()andViewport.use_debandingof the rootViewport. Whenrendering/viewport/hdr_2dis disabled, you should additionally set theViewport.use_debandingof other viewports in your project. To set debanding at run-time, the property that should be set depends on the renderer: Forward+ only usesViewport.use_debandingand Mobile uses bothRenderingServer.material_set_use_debanding()andViewport.use_debanding.
boolrendering/anti_aliasing/quality/use_taa=false🔗
Enables temporal antialiasing for the default screenViewport. TAA works by jittering the camera and accumulating the images of the last rendered frames, motion vector rendering is used to account for camera and object motion. Enabling TAA can make the image blurrier, which is partially counteracted by automatically using a negative mipmap LOD bias (seerendering/textures/default_filters/texture_mipmap_bias).
Note:The implementation is not complete yet. Some visual instances such as particles and skinned meshes may show ghosting artifacts in motion.
Note:TAA is only supported in the Forward+ rendering method, not Mobile or Compatibility.
Note:This property is only read when the project starts. To set TAA at runtime, setViewport.use_taaon the rootViewportinstead, or useRenderingServer.viewport_set_use_taa().
floatrendering/anti_aliasing/screen_space_roughness_limiter/amount=0.25🔗
Note:This property is only read when the project starts. To control the screen-space roughness limiter at runtime, callRenderingServer.screen_space_roughness_limiter_set_active()instead.
boolrendering/anti_aliasing/screen_space_roughness_limiter/enabled=true🔗
Iftrue, enables a spatial filter to limit roughness in areas with high-frequency detail. This can help reduce specular aliasing to an extent, though not as much as enablingrendering/anti_aliasing/quality/use_taa. This filter has a small performance cost, so consider disabling it if it doesn't benefit your scene noticeably.
Note:The screen-space roughness limiter is only supported in the Forward+ and Mobile rendering methods, not Compatibility.
Note:This property is only read when the project starts. To control the screen-space roughness limiter at runtime, callRenderingServer.screen_space_roughness_limiter_set_active()instead.
floatrendering/anti_aliasing/screen_space_roughness_limiter/limit=0.18🔗
Note:This property is only read when the project starts. To control the screen-space roughness limiter at runtime, callRenderingServer.screen_space_roughness_limiter_set_active()instead.
intrendering/camera/depth_of_field/depth_of_field_bokeh_quality=1🔗
Sets the quality of the depth of field effect. Higher quality takes more samples, which is slower but looks smoother.
intrendering/camera/depth_of_field/depth_of_field_bokeh_shape=1🔗
Sets the depth of field shape. Can be Box, Hexagon, or Circle. Box is the fastest. Circle is the most realistic, but also the most expensive to compute.
boolrendering/camera/depth_of_field/depth_of_field_use_jitter=false🔗
Iftrue, jitters DOF samples to make effect slightly blurrier and hide lines created from low sample rates. This can result in a slightly grainy appearance when used with a low number of samples.
Stringrendering/driver/depth_prepass/disable_for_vendors="PowerVR,Mali,Adreno,Apple"🔗
Disablesrendering/driver/depth_prepass/enableconditionally for certain vendors. By default, disables the depth prepass for mobile devices as mobile devices do not benefit from the depth prepass due to their unique architecture.
boolrendering/driver/depth_prepass/enable=true🔗
Iftrue, performs a previous depth pass before rendering 3D materials. This increases performance significantly in scenes with high overdraw, when complex materials and lighting are used. However, in scenes with few occluded surfaces, the depth prepass may reduce performance. If your game is viewed from a fixed angle that makes it easy to avoid overdraw (such as top-down or side-scrolling perspective), consider disabling the depth prepass to improve performance. This setting can be changed at run-time to optimize performance depending on the scene currently being viewed.
Note:Depth prepass is only supported when using the Forward+ or Compatibility rendering method. When using the Mobile rendering method, there is no depth prepass performed.
intrendering/driver/threads/thread_model=1🔗
Experimental:This setting has several known bugs which can lead to crashing, especially when using particles or resizing the window. Not recommended for use in production at this stage.
The thread model to use for rendering. Rendering on a thread may improve performance, but synchronizing to the main thread can cause a bit more jitter.
Colorrendering/environment/defaults/default_clear_color=Color(0.3,0.3,0.3,1)🔗
Default background clear color. Overridable perViewportusing itsEnvironment. SeeEnvironment.background_modeandEnvironment.background_colorin particular. To change this default color programmatically, useRenderingServer.set_default_clear_color().
Stringrendering/environment/defaults/default_environment=""🔗
Environmentthat will be used as a fallback environment in case a scene does not specify its own environment. The default environment is loaded in at scene load time regardless of whether you have set an environment or not. If you do not rely on the fallback environment, you do not need to set this property.
intrendering/environment/glow/upscale_mode=1🔗
Sets how the glow effect is upscaled before being copied onto the screen. Linear is faster, but looks blocky. Bicubic is slower but looks smooth.
Note:rendering/environment/glow/upscale_modeis only effective when using the Forward+ or Mobile rendering methods, as Compatibility uses a different glow implementation.
intrendering/environment/glow/upscale_mode.mobile=0🔗
Lower-end override forrendering/environment/glow/upscale_modeon mobile devices, due to performance concerns or driver support.
boolrendering/environment/screen_space_reflection/half_size=true🔗
Iftrue, screen-space reflections will be rendered at half size and then upscaled before being added to the scene. This is faster but may look pixelated or cause flickering. Iffalse, screen-space reflections will be rendered at full size.
floatrendering/environment/ssao/adaptive_target=0.5🔗
Quality target to use whenrendering/environment/ssao/qualityis set toUltra. A value of0.0provides a quality and speed similar toMediumwhile a value of1.0provides much higher quality than any of the other settings at the cost of performance.
intrendering/environment/ssao/blur_passes=2🔗
Number of blur passes to use when computing screen-space ambient occlusion. A higher number will result in a smoother look, but will be slower to compute and will have less high-frequency detail.
floatrendering/environment/ssao/fadeout_from=50.0🔗
Distance at which the screen-space ambient occlusion effect starts to fade out. Use this hide ambient occlusion from far away.
floatrendering/environment/ssao/fadeout_to=300.0🔗
Distance at which the screen-space ambient occlusion is fully faded out. Use this hide ambient occlusion from far away.
boolrendering/environment/ssao/half_size=true🔗
Iftrue, screen-space ambient occlusion will be rendered at half size and then upscaled before being added to the scene. This is significantly faster but may miss small details. Iffalse, screen-space ambient occlusion will be rendered at full size.
intrendering/environment/ssao/quality=2🔗
Sets the quality of the screen-space ambient occlusion effect. Higher values take more samples and so will result in better quality, at the cost of performance. Setting toUltrawill use therendering/environment/ssao/adaptive_targetsetting.
floatrendering/environment/ssil/adaptive_target=0.5🔗
Quality target to use whenrendering/environment/ssil/qualityis set toUltra. A value of0.0provides a quality and speed similar toMediumwhile a value of1.0provides much higher quality than any of the other settings at the cost of performance. When using the adaptive target, the performance cost scales with the complexity of the scene.
intrendering/environment/ssil/blur_passes=4🔗
Number of blur passes to use when computing screen-space indirect lighting. A higher number will result in a smoother look, but will be slower to compute and will have less high-frequency detail.
floatrendering/environment/ssil/fadeout_from=50.0🔗
Distance at which the screen-space indirect lighting effect starts to fade out. Use this to hide screen-space indirect lighting from far away.
floatrendering/environment/ssil/fadeout_to=300.0🔗
Distance at which the screen-space indirect lighting is fully faded out. Use this to hide screen-space indirect lighting from far away.
boolrendering/environment/ssil/half_size=true🔗
Iftrue, screen-space indirect lighting will be rendered at half size and then upscaled before being added to the scene. This is significantly faster but may miss small details and may result in some objects appearing to glow at their edges.
intrendering/environment/ssil/quality=2🔗
Sets the quality of the screen-space indirect lighting effect. Higher values take more samples and so will result in better quality, at the cost of performance. Setting toUltrawill use therendering/environment/ssil/adaptive_targetsetting.
floatrendering/environment/subsurface_scattering/subsurface_scattering_depth_scale=0.01🔗
Scales the depth over which the subsurface scattering effect is applied. A high value may allow light to scatter into a part of the mesh or another mesh that is close in screen space but far in depth. See alsorendering/environment/subsurface_scattering/subsurface_scattering_scale.
Note:This property is only read when the project starts. To set the subsurface scattering depth scale at runtime, callRenderingServer.sub_surface_scattering_set_scale()instead.
intrendering/environment/subsurface_scattering/subsurface_scattering_quality=1🔗
Sets the quality of the subsurface scattering effect. Higher values are slower but look nicer. This affects the rendering of materials that haveBaseMaterial3D.subsurf_scatter_enabledset totrue, along withShaderMaterials that setSSS_STRENGTH.
Note:This property is only read when the project starts. To set the subsurface scattering quality at runtime, callRenderingServer.sub_surface_scattering_set_quality()instead.
floatrendering/environment/subsurface_scattering/subsurface_scattering_scale=0.05🔗
Scales the distance over which samples are taken for subsurface scattering effect. Changing this does not impact performance, but higher values will result in significant artifacts as the samples will become obviously spread out. A lower value results in a smaller spread of scattered light. See alsorendering/environment/subsurface_scattering/subsurface_scattering_depth_scale.
Note:This property is only read when the project starts. To set the subsurface scattering scale at runtime, callRenderingServer.sub_surface_scattering_set_scale()instead.
intrendering/environment/volumetric_fog/use_filter=1🔗
Enables filtering of the volumetric fog effect prior to integration. This substantially blurs the fog which reduces fine details but also smooths out harsh edges and aliasing artifacts. Disable when more detail is required.
intrendering/environment/volumetric_fog/volume_depth=64🔗
Number of slices to use along the depth of the froxel buffer for volumetric fog. A lower number will be more efficient but may result in artifacts appearing during camera movement. See alsoEnvironment.volumetric_fog_length.
intrendering/environment/volumetric_fog/volume_size=64🔗
Base size used to determine size of froxel buffer in the camera X-axis and Y-axis. The final size is scaled by the aspect ratio of the screen, so actual values may differ from what is set. Set a larger size for more detailed fog, set a smaller size for better performance.
Stringrendering/gl_compatibility/driver="opengl3"🔗
Sets the driver to be used by the renderer when using the Compatibility renderer. Editing this property has no effect in the default configuration, as first-party platforms each have platform-specific overrides. Use those overrides to configure the driver for each platform.
This can be overridden using the--rendering-driver<driver>command line argument.
Supported values are:
- opengl3, OpenGL 3.3 on desktop platforms, OpenGL ES 3.0 on mobile platforms, WebGL 2.0 on web.
opengl3, OpenGL 3.3 on desktop platforms, OpenGL ES 3.0 on mobile platforms, WebGL 2.0 on web.
- opengl3_angle, OpenGL ES 3.0 using the ANGLE compatibility layer, supported on macOS (over native OpenGL) and Windows (over Direct3D 11).
opengl3_angle, OpenGL ES 3.0 using the ANGLE compatibility layer, supported on macOS (over native OpenGL) and Windows (over Direct3D 11).
- opengl3_es, OpenGL ES 3.0 on Linux/BSD.
opengl3_es, OpenGL ES 3.0 on Linux/BSD.
Note:The availability of these options depends on whether the engine was compiled with support for them (determined by SCons optionsopengl3andangle_libs).
Note:The actual rendering driver may be automatically changed by the engine as a result of a fallback, or a user-specified command line argument. To get the actual rendering driver that is used at runtime, useRenderingServer.get_current_rendering_driver_name()instead of reading this project setting's value.
Stringrendering/gl_compatibility/driver.android="opengl3"🔗
Android override forrendering/gl_compatibility/driver.
Only one option is supported:
- opengl3, OpenGL ES 3.0 from native drivers.
opengl3, OpenGL ES 3.0 from native drivers.
Stringrendering/gl_compatibility/driver.ios="opengl3"🔗
iOS override forrendering/gl_compatibility/driver.
Only one option is supported:
- opengl3, OpenGL ES 3.0 from native drivers.
opengl3, OpenGL ES 3.0 from native drivers.
Stringrendering/gl_compatibility/driver.linuxbsd="opengl3"🔗
LinuxBSD override forrendering/gl_compatibility/driver.
Two options are supported:
- opengl3(default), OpenGL 3.3 from native drivers.
opengl3(default), OpenGL 3.3 from native drivers.
- opengl3_es, OpenGL ES 3.0 from native drivers. Ifrendering/gl_compatibility/fallback_to_glesis enabled, this is used as a fallback if OpenGL 3.3 is not supported.
opengl3_es, OpenGL ES 3.0 from native drivers. Ifrendering/gl_compatibility/fallback_to_glesis enabled, this is used as a fallback if OpenGL 3.3 is not supported.
Stringrendering/gl_compatibility/driver.macos="opengl3"🔗
macOS override forrendering/gl_compatibility/driver.
Two options are supported:
- opengl3(default), OpenGL 3.3 from native drivers. Ifrendering/gl_compatibility/fallback_to_nativeis enabled, this is used as a fallback if ANGLE is configured as the preferred driver but not supported.
opengl3(default), OpenGL 3.3 from native drivers. Ifrendering/gl_compatibility/fallback_to_nativeis enabled, this is used as a fallback if ANGLE is configured as the preferred driver but not supported.
- opengl3_angle, OpenGL ES 3.0 using the ANGLE compatibility layer over native OpenGL drivers. Ifrendering/gl_compatibility/fallback_to_angleis enabled, this is used as a fallback if OpenGL 3.3 is not supported.
opengl3_angle, OpenGL ES 3.0 using the ANGLE compatibility layer over native OpenGL drivers. Ifrendering/gl_compatibility/fallback_to_angleis enabled, this is used as a fallback if OpenGL 3.3 is not supported.
Stringrendering/gl_compatibility/driver.web="opengl3"🔗
Web override forrendering/gl_compatibility/driver.
Only one option is supported:
- opengl3, WebGL 2.0. The underlying native API depends on the target OS, browser, and browser configuration.
opengl3, WebGL 2.0. The underlying native API depends on the target OS, browser, and browser configuration.
Stringrendering/gl_compatibility/driver.windows="opengl3"🔗
Windows override forrendering/gl_compatibility/driver.
Two options are supported:
- opengl3(default), OpenGL 3.3 from native drivers. Ifrendering/gl_compatibility/fallback_to_nativeis enabled, this is used as a fallback if ANGLE is configured as the preferred driver but not supported.
opengl3(default), OpenGL 3.3 from native drivers. Ifrendering/gl_compatibility/fallback_to_nativeis enabled, this is used as a fallback if ANGLE is configured as the preferred driver but not supported.
- opengl3_angle, OpenGL ES 3.0 using the ANGLE compatibility layer over native Direct3D 11 drivers. Ifrendering/gl_compatibility/fallback_to_angleis enabled, this is used as a fallback if OpenGL 3.3 is not supported. By default, ANGLE is used as the default driver for some devices listed inrendering/gl_compatibility/force_angle_on_devices.
opengl3_angle, OpenGL ES 3.0 using the ANGLE compatibility layer over native Direct3D 11 drivers. Ifrendering/gl_compatibility/fallback_to_angleis enabled, this is used as a fallback if OpenGL 3.3 is not supported. By default, ANGLE is used as the default driver for some devices listed inrendering/gl_compatibility/force_angle_on_devices.
boolrendering/gl_compatibility/fallback_to_angle=true🔗
Iftrue, the Compatibility renderer will fall back to ANGLE if native OpenGL is not supported or the device is listed inrendering/gl_compatibility/force_angle_on_devices.
Note:This setting is implemented only on Windows.
boolrendering/gl_compatibility/fallback_to_gles=true🔗
Iftrue, the Compatibility renderer will fall back to OpenGLES if desktop OpenGL is not supported.
Note:This setting is implemented only on Linux/X11.
boolrendering/gl_compatibility/fallback_to_native=true🔗
Iftrue, the Compatibility renderer will fall back to native OpenGL if ANGLE is not supported, or ANGLE dynamic libraries aren't found.
Note:This setting is implemented on macOS and Windows.
Arrayrendering/gl_compatibility/force_angle_on_devices🔗
AnArrayof devices which should always use the ANGLE renderer.
Each entry is aDictionarywith the following keys:vendorandname.namecan be set to*to add all devices with the specifiedvendor.
Note:This setting is implemented only on Windows.
intrendering/gl_compatibility/item_buffer_size=16384🔗
Maximum number of canvas items commands that can be drawn in a single viewport update. If more render commands are issued they will be ignored. Decreasing this limit may improve performance on bandwidth limited devices. Increase this limit if you find that not all objects are being drawn in a frame.
boolrendering/gl_compatibility/nvidia_disable_threaded_optimization=true🔗
Iftrue, disables the threaded optimization feature from the NVIDIA drivers, which are known to cause stuttering in most OpenGL applications.
Note:This setting only works on Windows, as threaded optimization is disabled by default on other platforms.
boolrendering/global_illumination/gi/use_half_resolution=false🔗
Iftrue, rendersVoxelGIand SDFGI (Environment.sdfgi_enabled) buffers at halved resolution (e.g. 960×540 when the viewport size is 1920×1080). This improves performance significantly when VoxelGI or SDFGI is enabled, at the cost of artifacts that may be visible on polygon edges. The loss in quality becomes less noticeable as the viewport resolution increases.LightmapGIrendering is not affected by this setting.
Note:This property is only read when the project starts. To set half-resolution GI at run-time, callRenderingServer.gi_set_use_half_resolution()instead.
intrendering/global_illumination/sdfgi/frames_to_converge=5🔗
The number of frames to use for converging signed distance field global illumination. Higher values lead to a less noisy result, at the cost of taking a longer time to fully converge. This means the scene's global illumination will be too dark for a longer period of time, especially when the camera moves fast. The actual convergence speed depends on rendered framerate. For example, with the default setting of 30 frames, rendering at 60 FPS will make SDFGI fully converge after 0.5 seconds. See alsorendering/global_illumination/sdfgi/frames_to_update_lightsandrendering/global_illumination/sdfgi/probe_ray_count.
Note:This property is only read when the project starts. To control SDFGI convergence speed at runtime, callRenderingServer.environment_set_sdfgi_frames_to_converge()instead.
intrendering/global_illumination/sdfgi/frames_to_update_lights=2🔗
The number of frames over which dynamic lights should be updated in signed distance field global illumination. Higher values take more time to update indirect lighting coming from dynamic lights, but result in better performance when many dynamic lights are present. See alsorendering/global_illumination/sdfgi/frames_to_convergeandrendering/global_illumination/sdfgi/probe_ray_count.
Note:This only affectsLight3Dnodes whoseLight3D.light_bake_modeisLight3D.BAKE_DYNAMIC(which is the default). Consider making non-moving lights use theLight3D.BAKE_STATICbake mode to improve performance.
Note:This property is only read when the project starts. To control SDFGI light update speed at runtime, callRenderingServer.environment_set_sdfgi_frames_to_update_light()instead.
intrendering/global_illumination/sdfgi/probe_ray_count=1🔗
The number of rays to throw per frame when computing signed distance field global illumination. Higher values lead to a less noisy result, at the cost of performance. See alsorendering/global_illumination/sdfgi/frames_to_convergeandrendering/global_illumination/sdfgi/frames_to_update_lights.
Note:This property is only read when the project starts. To control SDFGI quality at runtime, callRenderingServer.environment_set_sdfgi_ray_count()instead.
intrendering/global_illumination/voxel_gi/quality=0🔗
The VoxelGI quality to use. High quality leads to more precise lighting and better reflections, but is slower to render. This setting does not affect the baked data and doesn't require baking theVoxelGIagain to apply.
Note:This property is only read when the project starts. To control VoxelGI quality at runtime, callRenderingServer.voxel_gi_set_quality()instead.
intrendering/lightmapping/bake_performance/max_rays_per_pass=4🔗
The maximum number of rays that can be thrown per pass when baking lightmaps withLightmapGI. Depending on the scene, adjusting this value may result in higher GPU utilization when baking lightmaps, leading to faster bake times.
Note:Using a value that is too high for your system can cause crashes due to the GPU being unresponsive for long periods of time, and the graphics driver being reset by the OS.
intrendering/lightmapping/bake_performance/max_rays_per_probe_pass=64🔗
The maximum number of rays that can be thrown per pass when baking dynamic object lighting inLightmapProbes withLightmapGI. Depending on the scene, adjusting this value may result in higher GPU utilization when baking lightmaps, leading to faster bake times.
Note:Using a value that is too high for your system can cause crashes due to the GPU being unresponsive for long periods of time, and the graphics driver being reset by the OS.
intrendering/lightmapping/bake_performance/max_transparency_rays=8🔗
The maximum number of retry rays that can be thrown per pass when hitting a transparent surface when baking lightmaps withLightmapGI. Depending on the scene, reducing this value may lead to faster bake times.
Note:Using a value that is too high for your system can cause crashes due to the GPU being unresponsive for long periods of time, and the graphics driver being reset by the OS.
intrendering/lightmapping/bake_performance/region_size=512🔗
The region size to use when baking lightmaps withLightmapGI. The specified value is rounded up to the nearest power of 2.
Note:Using a value that is too high for your system can cause crashes due to the GPU being unresponsive for long periods of time, and the graphics driver being reset by the OS.
intrendering/lightmapping/bake_quality/high_quality_probe_ray_count=512🔗
The number of rays to use for baking dynamic object lighting inLightmapProbes whenLightmapGI.qualityisLightmapGI.BAKE_QUALITY_HIGH.
intrendering/lightmapping/bake_quality/high_quality_ray_count=512🔗
The number of rays to use for baking lightmaps withLightmapGIwhenLightmapGI.qualityisLightmapGI.BAKE_QUALITY_HIGH.
intrendering/lightmapping/bake_quality/low_quality_probe_ray_count=64🔗
The number of rays to use for baking dynamic object lighting inLightmapProbes whenLightmapGI.qualityisLightmapGI.BAKE_QUALITY_LOW.
intrendering/lightmapping/bake_quality/low_quality_ray_count=32🔗
The number of rays to use for baking lightmaps withLightmapGIwhenLightmapGI.qualityisLightmapGI.BAKE_QUALITY_LOW.
intrendering/lightmapping/bake_quality/medium_quality_probe_ray_count=256🔗
The number of rays to use for baking dynamic object lighting inLightmapProbes whenLightmapGI.qualityisLightmapGI.BAKE_QUALITY_MEDIUM.
intrendering/lightmapping/bake_quality/medium_quality_ray_count=128🔗
The number of rays to use for baking lightmaps withLightmapGIwhenLightmapGI.qualityisLightmapGI.BAKE_QUALITY_MEDIUM.
intrendering/lightmapping/bake_quality/ultra_quality_probe_ray_count=2048🔗
The number of rays to use for baking dynamic object lighting inLightmapProbes whenLightmapGI.qualityisLightmapGI.BAKE_QUALITY_ULTRA.
intrendering/lightmapping/bake_quality/ultra_quality_ray_count=2048🔗
The number of rays to use for baking lightmaps withLightmapGIwhenLightmapGI.qualityisLightmapGI.BAKE_QUALITY_ULTRA.
intrendering/lightmapping/denoising/denoiser=0🔗
Denoiser tool used for denoising lightmaps.
UsingOpenImageDenoise(OIDN) requires configuring a path to an OIDN executable in the editor settings atEditorSettings.filesystem/tools/oidn/oidn_denoise_path. OIDN can be downloaded fromOpenImageDenoise's downloads page.
OIDN will use GPU acceleration when available. Unlike JNLM which uses compute shaders for acceleration, OIDN uses vendor-specific acceleration methods. For GPU acceleration to be available, the following libraries must be installed on the system depending on your GPU:
- NVIDIA GPUs: CUDA libraries
NVIDIA GPUs: CUDA libraries
- AMD GPUs: HIP libraries
AMD GPUs: HIP libraries
- Intel GPUs: SYCL libraries
Intel GPUs: SYCL libraries
If no GPU acceleration is configured on the system, multi-threaded CPU-based denoising will be performed instead. This CPU-based denoising is significantly slower than the JNLM denoiser in most cases.
boolrendering/lightmapping/lightmap_gi/use_bicubic_filter=true🔗
Iftrue, applies a bicubic filter during lightmap sampling. This makes lightmaps look much smoother, at a moderate performance cost.
Note:The bicubic filter exaggerates the 'bleeding' effect that occurs when a lightmap's resolution is low enough.
floatrendering/lightmapping/primitive_meshes/texel_size=0.2🔗
The texel_size that is used to calculate theMesh.lightmap_size_hintonPrimitiveMeshresources ifPrimitiveMesh.add_uv2is enabled.
floatrendering/lightmapping/probe_capture/update_speed=15🔗
The framerate-independent update speed when representing dynamic object lighting fromLightmapProbes. Higher values make dynamic object lighting update faster. Higher values can prevent fast-moving objects from having "outdated" indirect lighting displayed on them, at the cost of possible flickering when an object moves from a bright area to a shaded area.
boolrendering/lights_and_shadows/directional_shadow/16_bits=true🔗
Use 16 bits for the directional shadow depth map. Enabling this results in shadows having less precision and may result in shadow acne, but can lead to performance improvements on some devices.
intrendering/lights_and_shadows/directional_shadow/size=4096🔗
The directional shadow's size in pixels. Higher values will result in sharper shadows, at the cost of performance. The value is rounded up to the nearest power of 2.
intrendering/lights_and_shadows/directional_shadow/size.mobile=2048🔗
Lower-end override forrendering/lights_and_shadows/directional_shadow/sizeon mobile devices, due to performance concerns or driver support.
intrendering/lights_and_shadows/directional_shadow/soft_shadow_filter_quality=2🔗
Quality setting for shadows cast byDirectionalLight3Ds. Higher quality settings use more samples when reading from shadow maps and are thus slower. Low quality settings may result in shadows looking grainy.
Note:The Soft Very Low setting will automatically multiplyconstantshadow blur by 0.75x to reduce the amount of noise visible. This automatic blur change only affects the constant blur factor defined inLight3D.shadow_blur, not the variable blur performed byDirectionalLight3Ds'Light3D.light_angular_distance.
Note:The Soft High and Soft Ultra settings will automatically multiplyconstantshadow blur by 1.5× and 2× respectively to make better use of the increased sample count. This increased blur also improves stability of dynamic object shadows.
intrendering/lights_and_shadows/directional_shadow/soft_shadow_filter_quality.mobile=0🔗
Lower-end override forrendering/lights_and_shadows/directional_shadow/soft_shadow_filter_qualityon mobile devices, due to performance concerns or driver support.
boolrendering/lights_and_shadows/positional_shadow/atlas_16_bits=true🔗
Use 16 bits for the omni/spot shadow depth map. Enabling this results in shadows having less precision and may result in shadow acne, but can lead to performance improvements on some devices.
intrendering/lights_and_shadows/positional_shadow/atlas_quadrant_0_subdiv=2🔗
The subdivision amount of the first quadrant on the shadow atlas. See thedocumentationfor more information.
intrendering/lights_and_shadows/positional_shadow/atlas_quadrant_1_subdiv=2🔗
The subdivision amount of the second quadrant on the shadow atlas. See thedocumentationfor more information.
intrendering/lights_and_shadows/positional_shadow/atlas_quadrant_2_subdiv=3🔗
The subdivision amount of the third quadrant on the shadow atlas. See thedocumentationfor more information.
intrendering/lights_and_shadows/positional_shadow/atlas_quadrant_3_subdiv=4🔗
The subdivision amount of the fourth quadrant on the shadow atlas. See thedocumentationfor more information.
intrendering/lights_and_shadows/positional_shadow/atlas_size=4096🔗
The size of the shadow atlas used forOmniLight3DandSpotLight3Dnodes. See thedocumentationfor more information.
intrendering/lights_and_shadows/positional_shadow/atlas_size.mobile=2048🔗
Lower-end override forrendering/lights_and_shadows/positional_shadow/atlas_sizeon mobile devices, due to performance concerns or driver support.
intrendering/lights_and_shadows/positional_shadow/soft_shadow_filter_quality=2🔗
Quality setting for shadows cast byOmniLight3Ds andSpotLight3Ds. Higher quality settings use more samples when reading from shadow maps and are thus slower. Low quality settings may result in shadows looking grainy.
Note:The Soft Very Low setting will automatically multiplyconstantshadow blur by 0.75x to reduce the amount of noise visible. This automatic blur change only affects the constant blur factor defined inLight3D.shadow_blur, not the variable blur performed byDirectionalLight3Ds'Light3D.light_angular_distance.
Note:The Soft High and Soft Ultra settings will automatically multiply shadow blur by 1.5× and 2× respectively to make better use of the increased sample count. This increased blur also improves stability of dynamic object shadows.
intrendering/lights_and_shadows/positional_shadow/soft_shadow_filter_quality.mobile=0🔗
Lower-end override forrendering/lights_and_shadows/positional_shadow/soft_shadow_filter_qualityon mobile devices, due to performance concerns or driver support.
boolrendering/lights_and_shadows/tighter_shadow_caster_culling=true🔗
Iftrue, items that cannot cast shadows into the view frustum will not be rendered into shadow maps.
This can increase performance.
boolrendering/lights_and_shadows/use_physical_light_units=false🔗
Enables the use of physically based units for light sources. Physically based units tend to be much larger than the arbitrary units used by Godot, but they can be used to match lighting within Godot to real-world lighting. Due to the large dynamic range of lighting conditions present in nature, Godot bakes exposure into the various lighting quantities before rendering. Most light sources bake exposure automatically at run time based on the activeCameraAttributesresource, butLightmapGIandVoxelGIrequire aCameraAttributesresource to be set at bake time to reduce the dynamic range. At run time, Godot will automatically reconcile the baked exposure with the active exposure to ensure lighting remains consistent.
floatrendering/limits/cluster_builder/max_clustered_elements=512🔗
The maximum number of clustered elements (OmniLight3D+SpotLight3D+Decal+ReflectionProbe) that can be rendered at once in the camera view. If there are more clustered elements present in the camera view, some of them will not be rendered (leading to pop-in during camera movement). Enabling distance fade on lights and decals (Light3D.distance_fade_enabled,Decal.distance_fade_enabled) can help avoid reaching this limit.
Decreasing this value may improve GPU performance on certain setups, even if the maximum number of clustered elements is never reached in the project.
Note:This setting is only effective when using the Forward+ rendering method, not Mobile and Compatibility.
intrendering/limits/global_shader_variables/buffer_size=65536🔗
The maximum number of uniforms that can be used by the global shader uniform buffer. Each item takes up one slot. In other words, a single uniform float and a uniform vec4 will take the same amount of space in the buffer.
Note:When using the Compatibility renderer, most mobile devices (and all web exports) will be limited to a maximum size of 1024 due to hardware constraints.
intrendering/limits/opengl/max_lights_per_object=8🔗
Max number of omnilights and spotlights renderable per object. At the default value of 8, this means that each surface can be affected by up to 8 omnilights and 8 spotlights. This is further limited by hardware support andrendering/limits/opengl/max_renderable_lights. Setting this low will slightly reduce memory usage, may decrease shader compile times, and may result in faster rendering on low-end, mobile, or web devices.
Note:This setting is only effective when using the Compatibility rendering method, not Forward+ and Mobile.
intrendering/limits/opengl/max_renderable_elements=65536🔗
Max number of elements renderable in a frame. If more elements than this are visible per frame, they will not be drawn. Keep in mind elements refer to mesh surfaces and not meshes themselves. Setting this low will slightly reduce memory usage and may decrease shader compile times, particularly on web. For most uses, the default value is suitable, but consider lowering as much as possible on web export.
Note:This setting is only effective when using the Compatibility rendering method, not Forward+ and Mobile.
intrendering/limits/opengl/max_renderable_lights=32🔗
Max number of positional lights renderable in a frame. If more lights than this number are used, they will be ignored. Setting this low will slightly reduce memory usage and may decrease shader compile times, particularly on web. For most uses, the default value is suitable, but consider lowering as much as possible on web export.
Note:This setting is only effective when using the Compatibility rendering method, not Forward+ and Mobile.
intrendering/limits/spatial_indexer/threaded_cull_minimum_instances=1000🔗
The minimum number of instances that must be present in a scene to enable culling computations on multiple threads. If a scene has fewer instances than this number, culling is done on a single thread.
intrendering/limits/spatial_indexer/update_iterations_per_frame=10🔗
There is currently no description for this property. Please help us bycontributing one!
floatrendering/limits/time/time_rollover_secs=3600🔗
Maximum time (in seconds) before theTIMEshader built-in variable rolls over. TheTIMEvariable increments bydeltaeach frame, and when it exceeds this value, it rolls over to0.0. Since large floating-point values are less precise than small floating-point values, this should be set as low as possible to maximize the precision of theTIMEbuilt-in variable in shaders. This is especially important on mobile platforms where precision in shaders is significantly reduced. However, if this is set too low, shader animations may appear to restart from the beginning while the project is running.
On desktop platforms, values below4096are recommended, ideally below2048. On mobile platforms, values below64are recommended, ideally below32.
floatrendering/mesh_lod/lod_change/threshold_pixels=1.0🔗
The automatic LOD bias to use for meshes rendered within theReflectionProbe. Higher values will use less detailed versions of meshes that have LOD variations generated. If set to0.0, automatic LOD is disabled. Increaserendering/mesh_lod/lod_change/threshold_pixelsto improve performance at the cost of geometry detail.
Note:rendering/mesh_lod/lod_change/threshold_pixelsdoes not affectGeometryInstance3Dvisibility ranges (also known as "manual" LOD or hierarchical LOD).
Note:This property is only read when the project starts. To adjust the automatic LOD threshold at runtime, setViewport.mesh_lod_thresholdon the rootViewport.
intrendering/occlusion_culling/bvh_build_quality=2🔗
TheBounding Volume Hierarchyquality to use when rendering the occlusion culling buffer. Higher values will result in more accurate occlusion culling, at the cost of higher CPU usage. See alsorendering/occlusion_culling/occlusion_rays_per_thread.
Note:This property is only read when the project starts. To adjust the BVH build quality at runtime, useRenderingServer.viewport_set_occlusion_culling_build_quality().
boolrendering/occlusion_culling/jitter_projection=true🔗
Iftrue, the projection used for rendering the occlusion buffer will be jittered. This can help prevent objects being incorrectly culled when visible through small gaps.
intrendering/occlusion_culling/occlusion_rays_per_thread=512🔗
The number of occlusion rays traced per CPU thread. Higher values will result in more accurate occlusion culling, at the cost of higher CPU usage. The occlusion culling buffer's pixel count is roughly equal toocclusion_rays_per_thread*number_of_logical_cpu_cores, so it will depend on the system's CPU. Therefore, CPUs with fewer cores will use a lower resolution to attempt keeping performance costs even across devices. See alsorendering/occlusion_culling/bvh_build_quality.
Note:This property is only read when the project starts. To adjust the number of occlusion rays traced per thread at runtime, useRenderingServer.viewport_set_occlusion_rays_per_thread().
boolrendering/occlusion_culling/use_occlusion_culling=false🔗
Iftrue,OccluderInstance3Dnodes will be usable for occlusion culling in 3D in the root viewport. In custom viewports,Viewport.use_occlusion_cullingmust be set totrueinstead.
Note:Enabling occlusion culling has a cost on the CPU. Only enable occlusion culling if you actually plan to use it. Large open scenes with few or no objects blocking the view will generally not benefit much from occlusion culling. Large open scenes generally benefit more from mesh LOD and visibility ranges (GeometryInstance3D.visibility_range_beginandGeometryInstance3D.visibility_range_end) compared to occlusion culling.
Note:Due to memory constraints, occlusion culling is not supported by default in Web export templates. It can be enabled by compiling custom Web export templates withmodule_raycast_enabled=yes.
intrendering/reflections/reflection_atlas/reflection_count=64🔗
Number of cubemaps to store in the reflection atlas. The number ofReflectionProbes in a scene will be limited by this amount. A higher number requires more VRAM.
intrendering/reflections/reflection_atlas/reflection_size=256🔗
Size of cubemap faces forReflectionProbes. A higher number requires more VRAM and may make reflection probe updating slower.
intrendering/reflections/reflection_atlas/reflection_size.mobile=128🔗
Lower-end override forrendering/reflections/reflection_atlas/reflection_sizeon mobile devices, due to performance concerns or driver support.
boolrendering/reflections/sky_reflections/fast_filter_high_quality=false🔗
Use a higher quality variant of the fast filtering algorithm. Significantly slower than using default quality, but results in smoother reflections. Should only be used when the scene is especially detailed.
intrendering/reflections/sky_reflections/ggx_samples=32🔗
Sets the number of samples to take when using importance sampling forSkys andReflectionProbes. A higher value will result in smoother, higher quality reflections, but increases time to calculate radiance maps. In general, fewer samples are needed for simpler, low dynamic range environments while more samples are needed for HDR environments and environments with a high level of detail.
intrendering/reflections/sky_reflections/ggx_samples.mobile=16🔗
Lower-end override forrendering/reflections/sky_reflections/ggx_sampleson mobile devices, due to performance concerns or driver support.
intrendering/reflections/sky_reflections/roughness_layers=7🔗
Limits the number of layers to use in radiance maps when using importance sampling. A lower number will be slightly faster and take up less VRAM.
boolrendering/reflections/sky_reflections/texture_array_reflections=true🔗
Iftrue, uses texture arrays instead of mipmaps for reflection probes and panorama backgrounds (sky). This reduces jitter noise and upscaling artifacts on reflections, but is significantly slower to compute and usesrendering/reflections/sky_reflections/roughness_layerstimes more memory.
Note:Texture array reflections are always disabled on macOS on Intel GPUs due to driver bugs.
boolrendering/reflections/sky_reflections/texture_array_reflections.mobile=false🔗
Lower-end override forrendering/reflections/sky_reflections/texture_array_reflectionson mobile devices, due to performance concerns or driver support.
boolrendering/reflections/specular_occlusion/enabled=true🔗
Iftrue, reduces reflections based on ambient light.
Stringrendering/renderer/rendering_method="forward_plus"🔗
Sets the renderer that will be used by the project. Options are:
forward_plus(Forward+): High-end renderer designed for desktop devices. Has a higher base overhead, but scales well with complex scenes. Not suitable for older devices or mobile.
mobile(Mobile): Modern renderer designed for mobile devices. Has a lower base overhead than Forward+, but does not scale as well to large scenes with many elements.
gl_compatibility(Compatibility): Low-end renderer designed for older devices. Based on the limitations of the OpenGL 3.3 / OpenGL ES 3.0 / WebGL 2 APIs. Lighting calculations are performed on nonlinear sRGB-encoded color data, which produces inaccurate results that may look acceptable for some games.
This can be overridden using the--rendering-method<method>command line argument.
Note:The actual rendering method may be automatically changed by the engine as a result of a fallback, or a user-specified command line argument. To get the actual rendering method that is used at runtime, useRenderingServer.get_current_rendering_method()instead of reading this project setting's value.
Stringrendering/renderer/rendering_method.mobile="mobile"🔗
Override forrendering/renderer/rendering_methodon mobile devices.
Stringrendering/renderer/rendering_method.web="gl_compatibility"🔗
Override forrendering/renderer/rendering_methodon web.
intrendering/rendering_device/d3d12/agility_sdk_version=618🔗
Version code of theDirect3D 12 Agility SDKto use (D3D12SDKVersion). This must match theminorversion that is installed next to the editor binary and in the export templates directory for the current editor version. For example, if you have1.618.5installed, you need to input618here.
intrendering/rendering_device/d3d12/max_resource_descriptors=65536🔗
The number of entries in the resource descriptor heap the Direct3D 12 rendering driver uses for most rendering operations.
Depending on the complexity of scenes, this value may be lowered or may need to be raised.
intrendering/rendering_device/d3d12/max_sampler_descriptors=1024🔗
The number of entries in the sampler descriptor heap the Direct3D 12 rendering driver uses for most rendering operations.
Depending on the complexity of scenes, this value may be lowered or may need to be raised.
Stringrendering/rendering_device/driver="vulkan"🔗
Sets the driver to be used by the renderer when using a RenderingDevice-based renderer like the Forward+ or Mobile renderers. Editing this property has no effect in the default configuration, as first-party platforms each have platform-specific overrides. Use those overrides to configure the driver for each platform.
This can be overridden using the--rendering-driver<driver>command line argument.
Supported values are:
- metal, Metal (supported on Apple Silicon Macs and iOS).
metal, Metal (supported on Apple Silicon Macs and iOS).
- vulkan, Vulkan (supported on all desktop and mobile platforms).
vulkan, Vulkan (supported on all desktop and mobile platforms).
- d3d12, Direct3D 12 (supported on Windows).
d3d12, Direct3D 12 (supported on Windows).
Note:The availability of these options depends on whether the engine was compiled with support for them (determined by SCons optionsvulkan,metal, andd3d12).
Note:If a given platform has no registered drivers, it can fall back to the Compatibility renderer (OpenGL 3) ifrendering/rendering_device/fallback_to_opengl3is enabled. This fallback happens automatically for the Web platform regardless of that property.
Note:The actual rendering driver may be automatically changed by the engine as a result of a fallback, or a user-specified command line argument. To get the actual rendering driver that is used at runtime, useRenderingServer.get_current_rendering_driver_name()instead of reading this project setting's value.
Stringrendering/rendering_device/driver.android="vulkan"🔗
Android override forrendering/rendering_device/driver.
Only one option is supported:
- vulkan, Vulkan from native drivers.
vulkan, Vulkan from native drivers.
Note:If Vulkan was disabled at compile time, there is no alternative RenderingDevice driver.
Stringrendering/rendering_device/driver.ios="metal"🔗
iOS override forrendering/rendering_device/driver.
Two options are supported:
- metal(default), Metal from native drivers.
metal(default), Metal from native drivers.
- vulkan, Vulkan over Metal via MoltenVK.
vulkan, Vulkan over Metal via MoltenVK.
Stringrendering/rendering_device/driver.linuxbsd="vulkan"🔗
LinuxBSD override forrendering/rendering_device/driver.
Only one option is supported:
- vulkan, Vulkan from native drivers.
vulkan, Vulkan from native drivers.
Note:If Vulkan was disabled at compile time, there is no alternative RenderingDevice driver.
Stringrendering/rendering_device/driver.macos="metal"🔗
macOS override forrendering/rendering_device/driver.
Two options are supported:
- metal(default), Metal from native drivers, only supported on Apple Silicon Macs. On Intel Macs, it will automatically fall back tovulkanas Metal support is not implemented.
metal(default), Metal from native drivers, only supported on Apple Silicon Macs. On Intel Macs, it will automatically fall back tovulkanas Metal support is not implemented.
- vulkan, Vulkan over Metal via MoltenVK, supported on both Apple Silicon and Intel Macs.
vulkan, Vulkan over Metal via MoltenVK, supported on both Apple Silicon and Intel Macs.
Stringrendering/rendering_device/driver.visionos="metal"🔗
visionOS override forrendering/rendering_device/driver.
Only one option is supported:
- metal(default), Metal from native drivers.
metal(default), Metal from native drivers.
Stringrendering/rendering_device/driver.windows="vulkan"🔗
Windows override forrendering/rendering_device/driver.
Two options are supported:
- vulkan(default), Vulkan from native drivers. Ifrendering/rendering_device/fallback_to_vulkanis enabled, this is used as a fallback if Direct3D 12 is not supported.
vulkan(default), Vulkan from native drivers. Ifrendering/rendering_device/fallback_to_vulkanis enabled, this is used as a fallback if Direct3D 12 is not supported.
- d3d12, Direct3D 12 from native drivers. Ifrendering/rendering_device/fallback_to_d3d12is enabled, this is used as a fallback if Vulkan is not supported.
d3d12, Direct3D 12 from native drivers. Ifrendering/rendering_device/fallback_to_d3d12is enabled, this is used as a fallback if Vulkan is not supported.
Note:Starting with Godot 4.6, new projects are configured by default to used3d12on Windows. Projects created before Godot 4.6 keepvulkanfor compatibility reasons, but it is recommended to switch them manually tod3d12.
boolrendering/rendering_device/fallback_to_d3d12=true🔗
Iftrue, the Forward+ renderer will fall back to Direct3D 12 if Vulkan is not supported. The fallback is always attempted regardless of this setting if Vulkan driver support was disabled at compile time.
Note:This setting is implemented only on Windows.
boolrendering/rendering_device/fallback_to_opengl3=true🔗
Iftrue, the Forward+ renderer will fall back to OpenGL 3 if Direct3D 12, Metal, and Vulkan are not supported.
Note:This setting is implemented on Windows, Android, macOS, iOS, and Linux/X11.
boolrendering/rendering_device/fallback_to_vulkan=true🔗
Iftrue, the Forward+ renderer will fall back to Vulkan if Direct3D 12 (on Windows) or Metal (on macOS x86_64) are not supported. The fallback is always attempted regardless of this setting if Direct3D 12 (Windows) or Metal (macOS) driver support was disabled at compile time.
Note:This setting is implemented on Windows and macOS.
boolrendering/rendering_device/pipeline_cache/enable=true🔗
Enable the pipeline cache that is saved to disk if the graphics API supports it.
Note:This property is unable to control the pipeline caching the GPU driver itself does. Only turn this off along with deleting the contents of the driver's cache if you wish to simulate the experience a user will get when starting the game for the first time.
floatrendering/rendering_device/pipeline_cache/save_chunk_size_mb=3.0🔗
Determines at which interval pipeline cache is saved to disk. The lower the value, the more often it is saved.
intrendering/rendering_device/staging_buffer/block_size_kb=256🔗
The size of a block allocated in the staging buffers. Staging buffers are the intermediate resources the engine uses to upload or download data to the GPU. This setting determines the max amount of data that can be transferred in a copy operation. Increasing this will result in faster data transfers at the cost of extra memory.
Note:This property is only read when the project starts. There is currently no way to change this value at run-time.
intrendering/rendering_device/staging_buffer/max_size_mb=128🔗
The maximum amount of memory allowed to be used by staging buffers. If the amount of data being uploaded or downloaded exceeds this amount, the GPU will stall and wait for previous frames to finish.
Note:This property is only read when the project starts. There is currently no way to change this value at run-time.
intrendering/rendering_device/staging_buffer/texture_download_region_size_px=64🔗
The region size in pixels used to download texture data from the GPU when using methods likeRenderingDevice.texture_get_data_async().
Note:This property's upper limit is controlled byrendering/rendering_device/staging_buffer/block_size_kband whether it's possible to allocate a single block of texture data with this region size in the format that is requested.
Note:This property is only read when the project starts. There is currently no way to change this value at run-time.
intrendering/rendering_device/staging_buffer/texture_upload_region_size_px=64🔗
The region size in pixels used to upload texture data from the GPU when using methods likeRenderingDevice.texture_update().
Note:This property's upper limit is controlled byrendering/rendering_device/staging_buffer/block_size_kband whether it's possible to allocate a single block of texture data with this region size in the format that is requested.
Note:This property is only read when the project starts. There is currently no way to change this value at run-time.
intrendering/rendering_device/vsync/frame_queue_size=2🔗
The number of frames to track on the CPU side before stalling to wait for the GPU.
Try theV-Sync Simulator, an interactive interface that simulates presentation to better understand how it is affected by different variables under various conditions.
Note:This property is only read when the project starts. There is currently no way to change this value at run-time.
intrendering/rendering_device/vsync/swapchain_image_count=3🔗
The number of images the swapchain will consist of (back buffers + front buffer).
2corresponds to double-buffering and3to triple-buffering.
Double-buffering may give you the lowest lag/latency but if V-Sync is on and the system can't render at 60 fps, the framerate will go down in multiples of it (e.g. 30 fps, 15, 7.5, etc.). Triple buffering gives you higher framerate (specially if the system can't reach a constant 60 fps) at the cost of up to 1 frame of latency, withDisplayServer.VSYNC_ENABLED(FIFO).
Use double-buffering withDisplayServer.VSYNC_ENABLED. Triple-buffering is a must if you plan on usingDisplayServer.VSYNC_MAILBOXmode.
Try theV-Sync Simulator, an interactive interface that simulates presentation to better understand how it is affected by different variables under various conditions.
Note:Changes to this setting will only be applied on startup or when the swapchain is recreated (e.g. when setting the V-Sync mode).
Note:Some platforms may restrict the actual value.
intrendering/rendering_device/vulkan/max_descriptors_per_pool=64🔗
The number of descriptors per pool. Godot's Vulkan backend uses linear pools for descriptors that will be created and destroyed within a single frame. Instead of destroying every single descriptor every frame, they all can be destroyed at once by resetting the pool they belong to.
A larger number is more efficient up to a limit, after that it will only waste RAM (maximum efficiency is achieved when there is no more than 1 pool per frame). A small number could end up with one pool per descriptor, which negatively impacts performance.
Note:Changing this property requires a restart to take effect.
floatrendering/scaling_3d/fsr_sharpness=0.2🔗
Determines how sharp the upscaled image will be when using the FSR upscaling mode. Sharpness halves with every whole number. Values go from 0.0 (sharpest) to 2.0. Values above 2.0 won't make a visible difference.
intrendering/scaling_3d/mode=0🔗
Sets the scaling 3D mode. Bilinear scaling renders at different resolution to either undersample or supersample the viewport. FidelityFX Super Resolution 1.0, abbreviated to FSR, is an upscaling technology that produces high quality images at fast framerates by using a spatially-aware upscaling algorithm. FSR is slightly more expensive than bilinear, but it produces significantly higher image quality. On particularly low-end GPUs, the added cost of FSR may not be worth it (compared to using bilinear scaling with a slightly higher resolution scale to match performance).
Note:FSR is only effective when using the Forward+ rendering method, not Mobile or Compatibility. If using an incompatible rendering method, FSR will fall back to bilinear scaling.
intrendering/scaling_3d/mode.ios🔗
iOS override forrendering/scaling_3d/mode. This allows selecting the MetalFX spatial and MetalFX temporal scaling modes, which are exclusive to platforms where the Metal rendering driver is used.
intrendering/scaling_3d/mode.macos🔗
macOS override forrendering/scaling_3d/mode. This allows selecting the MetalFX spatial and MetalFX temporal scaling modes, which are exclusive to platforms where the Metal rendering driver is used.
floatrendering/scaling_3d/scale=1.0🔗
Scales the 3D render buffer based on the viewport size uses an image filter specified inrendering/scaling_3d/modeto scale the output image to the full viewport size. Values lower than1.0can be used to speed up 3D rendering at the cost of quality (undersampling). Values greater than1.0are only valid for bilinear mode and can be used to improve 3D rendering quality at a high performance cost (supersampling). See alsorendering/anti_aliasing/quality/msaa_3dfor multi-sample antialiasing, which is significantly cheaper but only smooths the edges of polygons.
boolrendering/shader_compiler/shader_cache/compress=true🔗
There is currently no description for this property. Please help us bycontributing one!
boolrendering/shader_compiler/shader_cache/enabled=true🔗
Enable the shader cache, which stores compiled shaders to disk to prevent stuttering from shader compilation the next time the shader is needed.
boolrendering/shader_compiler/shader_cache/strip_debug=false🔗
There is currently no description for this property. Please help us bycontributing one!
boolrendering/shader_compiler/shader_cache/strip_debug.release=true🔗
There is currently no description for this property. Please help us bycontributing one!
boolrendering/shader_compiler/shader_cache/use_zstd_compression=true🔗
There is currently no description for this property. Please help us bycontributing one!
boolrendering/shading/overrides/force_lambert_over_burley=false🔗
Iftrue, uses faster but lower-quality Lambert material lighting model instead of Burley.
boolrendering/shading/overrides/force_lambert_over_burley.mobile=true🔗
Lower-end override forrendering/shading/overrides/force_lambert_over_burleyon mobile devices, due to performance concerns or driver support.
boolrendering/shading/overrides/force_vertex_shading=false🔗
Iftrue, forces vertex shading for all rendering. This can increase performance a lot, but also reduces quality immensely. Can be used to optimize performance on low-end mobile devices.
intrendering/textures/basis_universal/rdo_dict_size=1024🔗
The dictionary size for Rate-Distortion Optimization (RDO) when importing textures as Basis Universal and when RDO is enabled, ranging from64to65536. Higher values reduce the file sizes further, but make encoding times significantly longer.
boolrendering/textures/basis_universal/zstd_supercompression=true🔗
Iftrue, enables Zstandard supercompression to reduce file size when importing textures as Basis Universal.
Note:Basis Universal textures need to be compressed to gain the benefit of smaller file sizes, otherwise they are as large as VRAM-compressed textures.
intrendering/textures/basis_universal/zstd_supercompression_level=6🔗
Specify the compression level for Basis Universal Zstandard supercompression, ranging from1to22.
intrendering/textures/canvas_textures/default_texture_filter=1🔗
The default texture filtering mode to use forCanvasItems built-in texture. In shaders, this texture is accessed asTEXTURE.
Note:For pixel art aesthetics, see alsorendering/2d/snap/snap_2d_vertices_to_pixelandrendering/2d/snap/snap_2d_transforms_to_pixel.
intrendering/textures/canvas_textures/default_texture_repeat=0🔗
The default texture repeating mode to use forCanvasItems built-in texture. In shaders, this texture is accessed asTEXTURE.
intrendering/textures/decals/filter=3🔗
The filtering quality to use forDecalnodes. When using one of the anisotropic filtering modes, the anisotropic filtering level is controlled byrendering/textures/default_filters/anisotropic_filtering_level.
intrendering/textures/default_filters/anisotropic_filtering_level=2🔗
Sets the maximum number of samples to take when using anisotropic filtering on textures (as a power of two). A higher sample count will result in sharper textures at oblique angles, but is more expensive to compute. A value of0forcibly disables anisotropic filtering, even on materials where it is enabled.
The anisotropic filtering level also affects decals and light projectors if they are configured to use anisotropic filtering. Seerendering/textures/decals/filterandrendering/textures/light_projectors/filter.
Note:In 3D, for this setting to have an effect, setBaseMaterial3D.texture_filtertoBaseMaterial3D.TEXTURE_FILTER_LINEAR_WITH_MIPMAPS_ANISOTROPICorBaseMaterial3D.TEXTURE_FILTER_NEAREST_WITH_MIPMAPS_ANISOTROPICon materials.
Note:In 2D, for this setting to have an effect, setCanvasItem.texture_filtertoCanvasItem.TEXTURE_FILTER_LINEAR_WITH_MIPMAPS_ANISOTROPICorCanvasItem.TEXTURE_FILTER_NEAREST_WITH_MIPMAPS_ANISOTROPICon theCanvasItemnode displaying the texture (or inCanvasTexture). However, anisotropic filtering is rarely useful in 2D, so only enable it for textures in 2D if it makes a meaningful visual difference.
Note:This property is only read when the project starts. To change the anisotropic filtering level at runtime, setViewport.anisotropic_filtering_levelon the rootViewportinstead.
floatrendering/textures/default_filters/texture_mipmap_bias=0.0🔗
Affects the final texture sharpness by reading from a lower or higher mipmap (also called "texture LOD bias"). Negative values make mipmapped textures sharper but grainier when viewed at a distance, while positive values make mipmapped textures blurrier (even when up close).
Enabling temporal antialiasing (rendering/anti_aliasing/quality/use_taa) will automatically apply a-0.5offset to this value, while enabling FXAA (rendering/anti_aliasing/quality/screen_space_aa) will automatically apply a-0.25offset to this value. If both TAA and FXAA are enabled at the same time, an offset of-0.75is applied to this value.
Note:Ifrendering/scaling_3d/scaleis lower than1.0(exclusive),rendering/textures/default_filters/texture_mipmap_biasis used to adjust the automatic mipmap bias which is calculated internally based on the scale factor. The formula for this islog2(scaling_3d_scale)+mipmap_bias.
boolrendering/textures/default_filters/use_nearest_mipmap_filter=false🔗
Iftrue, uses nearest-neighbor mipmap filtering when using mipmaps (also called "bilinear filtering"), which will result in visible seams appearing between mipmap stages. This may increase performance in mobile as less memory bandwidth is used. Iffalse, linear mipmap filtering (also called "trilinear filtering") is used.
Note:This property is only read when the project starts. There is currently no way to change this setting at run-time.
intrendering/textures/light_projectors/filter=3🔗
The filtering quality to use forOmniLight3DandSpotLight3Dprojectors. When using one of the anisotropic filtering modes, the anisotropic filtering level is controlled byrendering/textures/default_filters/anisotropic_filtering_level.
boolrendering/textures/lossless_compression/force_png=false🔗
Iftrue, the texture importer will import lossless textures using the PNG format. Otherwise, it will default to using WebP.
boolrendering/textures/vram_compression/cache_gpu_compressor=true🔗
Iftrue, the GPU texture compressor will cache the local RenderingDevice and its resources (shaders and pipelines), making subsequent imports faster at the cost of increased memory usage.
boolrendering/textures/vram_compression/compress_with_gpu=true🔗
Iftrue, the texture importer will utilize the GPU for compressing textures, improving the import time of large images.
Note:This only functions on a device which supports either Vulkan, Direct3D 12, or Metal as a rendering driver.
Note:Currently this only affects certain compressed formats (BC1, BC3, BC4, BC5, and BC6), all of which are exclusive to desktop platforms and consoles.
boolrendering/textures/vram_compression/import_etc2_astc=false🔗
Iftrue, the texture importer will import VRAM-compressed textures using the Ericsson Texture Compression 2 algorithm for lower quality textures and normal maps and Adaptable Scalable Texture Compression algorithm for high quality textures (in 4×4 block size).
Note:This setting is an override. The texture importer will always import the format the host platform needs, even if this is set tofalse.
Note:Changing this setting doesnotimpact textures that were already imported before. To make this setting apply to textures that were already imported, exit the editor, remove the.godot/imported/folder located inside the project folder then restart the editor (seeapplication/config/use_hidden_project_data_directory).
boolrendering/textures/vram_compression/import_s3tc_bptc=false🔗
Iftrue, the texture importer will import VRAM-compressed textures using the S3 Texture Compression algorithm (DXT1-5) for lower quality textures and the BPTC algorithm (BC6H and BC7) for high quality textures. This algorithm is only supported on PC desktop platforms and consoles.
Note:This setting is an override. The texture importer will always import the format the host platform needs, even if this is set tofalse.
Note:Changing this setting doesnotimpact textures that were already imported before. To make this setting apply to textures that were already imported, exit the editor, remove the.godot/imported/folder located inside the project folder then restart the editor (seeapplication/config/use_hidden_project_data_directory).
intrendering/textures/webp_compression/compression_method=2🔗
The default compression method for WebP. Affects both lossy and lossless WebP. A higher value results in smaller files at the cost of compression speed. Decompression speed is mostly unaffected by the compression method. Supported values are 0 to 6. Note that compression methods above 4 are very slow and offer very little savings.
floatrendering/textures/webp_compression/lossless_compression_factor=25🔗
The default compression factor for lossless WebP. Decompression speed is mostly unaffected by the compression factor. Supported values are 0 to 100.
boolrendering/viewport/hdr_2d=false🔗
Iftrue, enablesViewport.use_hdr_2don the root Viewport. 2D rendering will use a high dynamic range (HDR)RGBA16format framebuffer. Additionally, 2D rendering will be performed on linear values and will be converted using the appropriate transfer function immediately before blitting to the screen.
Practically speaking, this means that the end result of the Viewport will not be clamped to the0-1range and can be used in 3D rendering without color encoding adjustments. This allows 2D rendering to take advantage of effects requiring high dynamic range (e.g. 2D glow) as well as substantially improves the appearance of effects requiring highly detailed gradients.
Note:This property is only read when the project starts. To toggle HDR 2D at runtime, setViewport.use_hdr_2don the rootViewport.
boolrendering/viewport/transparent_background=false🔗
Iftrue, enablesViewport.transparent_bgon the root viewport. This allows per-pixel transparency to be effective after also enablingdisplay/window/size/transparentanddisplay/window/per_pixel_transparency/allowed.
intrendering/vrs/mode=0🔗
Set the default Variable Rate Shading (VRS) mode for the main viewport. SeeViewport.vrs_modeto change this at runtime, andVRSModefor possible values.
Stringrendering/vrs/texture=""🔗
Ifrendering/vrs/modeis set toTexture, this is the path to default texture loaded as the VRS image.
The texturemustuse a lossless compression format so that colors can be matched precisely. The following VRS densities are mapped to various colors, with brighter colors representing a lower level of shading precision:

```
- 1×1 = rgb(0, 0, 0)     - #000000
- 1×2 = rgb(0, 85, 0)    - #005500
- 2×1 = rgb(85, 0, 0)    - #550000
- 2×2 = rgb(85, 85, 0)   - #555500
- 2×4 = rgb(85, 170, 0)  - #55aa00
- 4×2 = rgb(170, 85, 0)  - #aa5500
- 4×4 = rgb(170, 170, 0) - #aaaa00
- 4×8 = rgb(170, 255, 0) - #aaff00 - Not supported on most hardware
- 8×4 = rgb(255, 170, 0) - #ffaa00 - Not supported on most hardware
- 8×8 = rgb(255, 255, 0) - #ffff00 - Not supported on most hardware
```

floatthreading/worker_pool/low_priority_thread_ratio=0.3🔗
The ratio ofWorkerThreadPool's threads that will be reserved for low-priority tasks. For example, if 10 threads are available and this value is set to0.3, 3 of the worker threads will be reserved for low-priority tasks. The actual value won't exceed the number of CPU cores minus one, and if possible, at least one worker thread will be dedicated to low-priority tasks.
intthreading/worker_pool/max_threads=-1🔗
Maximum number of threads to be used byWorkerThreadPool. On Web, a value of-1means1. On other platforms, it means alllogicalCPU cores available (seeOS.get_processor_count()).
boolxr/openxr/binding_modifiers/analog_threshold=false🔗
Iftrue, enables the analog threshold binding modifier if supported by the XR runtime.
boolxr/openxr/binding_modifiers/dpad_binding=false🔗
Iftrue, enables the D-pad binding modifier if supported by the XR runtime.
Stringxr/openxr/default_action_map="res://openxr_action_map.tres"🔗
Action map configuration to load by default.
boolxr/openxr/enabled=false🔗
Iftrue, Godot will setup and initialize OpenXR on startup.
intxr/openxr/environment_blend_mode="0"🔗
Specify how OpenXR should blend in the environment. This is specific to certain AR and passthrough devices where camera images are blended in by the XR compositor.
intxr/openxr/extensions/debug_message_types="15"🔗
Specifies the message types for which we request debug messages. Requiresxr/openxr/extensions/debug_utilsto be set and the extension to be supported by the XR runtime.
intxr/openxr/extensions/debug_utils="0"🔗
Enables debug utilities on XR runtimes that supports the debug utils extension. Sets the maximum severity being reported (0 = disabled, 1 = error, 2 = warning, 3 = info, 4 = verbose).
boolxr/openxr/extensions/eye_gaze_interaction=false🔗
Specify whether to enable eye tracking for this project. Depending on the platform, additional export configuration may be needed.
boolxr/openxr/extensions/frame_synthesis=false🔗
Iftruethe frame synthesis extension will be activated if supported by the platform.
Note:This feature should not be enabled in conjunction with Application Space Warp, if supported this replaces ASW.
boolxr/openxr/extensions/hand_interaction_profile=false🔗
Iftruethe hand interaction profile extension will be activated if supported by the platform.
boolxr/openxr/extensions/hand_tracking=false🔗
Iftrue, the hand tracking extension is enabled if available.
Note:By default hand tracking will only work for data sources chosen by the XR runtime. For SteamVR this is the controller inferred data source, for most other runtimes this is the unobstructed data source. There is no way to query this. If a runtime supports the OpenXR data source extension you can use thexr/openxr/extensions/hand_tracking_controller_data_sourceand/orxr/openxr/extensions/hand_tracking_unobstructed_data_sourceto indicate you wish to enable these data sources. If neither is selected the data source extension is not enabled and the XR runtimes default behavior persists.
boolxr/openxr/extensions/hand_tracking_controller_data_source=false🔗
Iftrue, support for the controller inferred data source is requested. If supported, you will receive hand tracking data even if the user has a controller in hand, with finger positions automatically inferred from controller input and/or sensors.
Note:This requires the OpenXR data source extension and controller inferred handtracking to be supported by the XR runtime. If not supported this setting will be ignored.xr/openxr/extensions/hand_trackingmust be enabled for this setting to be used.
boolxr/openxr/extensions/hand_tracking_unobstructed_data_source=false🔗
Iftrue, support for the unobstructed data source is requested. If supported, you will receive hand tracking data based on the actual finger positions of the user often determined by optical tracking.
Note:This requires the OpenXR data source extension and unobstructed handtracking to be supported by the XR runtime. If not supported this setting will be ignored.xr/openxr/extensions/hand_trackingmust be enabled for this setting to be used.
boolxr/openxr/extensions/render_model=false🔗
Iftruewe enable the render model extension if available.
Note:This relates to the core OpenXR render model extension and has no relation to any vendor render model extensions.
intxr/openxr/extensions/spatial_entity/april_tag_dict="3"🔗
The April Tag marker types the built-in marker tracking is set to recognize (if April Tag marker tracking is available and enabled).
intxr/openxr/extensions/spatial_entity/aruco_dict="15"🔗
The ArUco marker types the built-in marker tracking is set to recognize (if ArUco marker tracking is available and enabled).
boolxr/openxr/extensions/spatial_entity/enable_builtin_anchor_detection=false🔗
Iftrue, we enable the built-in logic for handling anchors. Godot will query (persistent) anchors and manageOpenXRAnchorTrackerinstances for you. If disabled you'll need to create your own spatial and persistence context and perform your own discovery queries.
Note:This functionality requires that spatial anchors are supported and enabled.
boolxr/openxr/extensions/spatial_entity/enable_builtin_marker_tracking=false🔗
Iftrue, we enable the built-in logic for handling marker tracking. Godot will query markers and manageOpenXRMarkerTrackerinstances for you. If disabled you'll need to create your own spatial context and perform your own discovery queries.
Note:This functionality requires that marker tracking is supported and enabled.
boolxr/openxr/extensions/spatial_entity/enable_builtin_plane_detection=false🔗
Iftrue, we enable the built-in logic for handling plane detection. Godot will query detected planes (walls, floors, ceilings, etc.) and manageOpenXRPlaneTrackerinstances for you. If disabled you'll need to create your own spatial context and perform your own discovery queries.
Note:This functionality requires that plane tracking is supported and enabled.
boolxr/openxr/extensions/spatial_entity/enable_marker_tracking=false🔗
Iftrue, support for the marker tracking extension is requested. If supported, you will be able to query information about markers detected by the XR runtime, e.g. QR codes, aruca markers and april tags.
Note:This requires that the OpenXR spatial entities and marker tracking extensions are supported by the XR runtime. If not supported this setting will be ignored.xr/openxr/extensions/spatial_entity/enabledmust be enabled for this setting to be used.
boolxr/openxr/extensions/spatial_entity/enable_persistent_anchors=false🔗
Iftrue, support for the persistent anchors extension is requested. If supported, you will be able to store spatial anchors and they will be restored on application startup.
Note:This requires that the OpenXR spatial entities, spatial anchors, and spatial persistence extensions are supported by the XR runtime. If not supported this setting will be ignored.xr/openxr/extensions/spatial_entity/enabledandxr/openxr/extensions/spatial_entity/enable_spatial_anchorsmust be enabled for this setting to be used.
boolxr/openxr/extensions/spatial_entity/enable_plane_tracking=false🔗
Iftrue, support for the plane tracking extension is requested. If supported, you will be able to query information about planes detected by the XR runtime, e.g. walls, floors, etc.
Note:This requires that the OpenXR spatial entities and plane tracking extensions are supported by the XR runtime. If not supported this setting will be ignored.xr/openxr/extensions/spatial_entity/enabledmust be enabled for this setting to be used.
boolxr/openxr/extensions/spatial_entity/enable_spatial_anchors=false🔗
Iftrue, support for the spatial anchors extension is requested. If supported, you will be able to register anchor locations in the real world that the XR runtime will adjust as needed and/or potentially share with other headsets.
Note:This requires that the OpenXR spatial entities and spatial anchors extensions are supported by the XR runtime. If not supported this setting will be ignored.xr/openxr/extensions/spatial_entity/enabledmust be enabled for this setting to be used.
boolxr/openxr/extensions/spatial_entity/enabled=false🔗
Iftrue, support for the spatial entity extension is requested. If supported, you will be able to access spatial information about the real environment around you. What information is available is dependent on additional extensions.
Note:This requires that the OpenXR spatial entities extension is supported by the XR runtime. If not supported this setting will be ignored.
intxr/openxr/form_factor="0"🔗
Specify whether OpenXR should be configured for an HMD or a hand held device.
boolxr/openxr/foveation_dynamic=false🔗
Iftrueand foveation is supported, will automatically adjust foveation level based on framerate up to the level set onxr/openxr/foveation_level.
intxr/openxr/foveation_level="0"🔗
Applied foveation level if supported.
Note:On platforms other than Android, ifrendering/anti_aliasing/quality/msaa_3dis enabled, this feature will be disabled.
intxr/openxr/reference_space="1"🔗
Specify the default reference space.
boolxr/openxr/startup_alert=true🔗
Iftrue, Godot will display an alert modal when OpenXR initialization fails on startup.
boolxr/openxr/submit_depth_buffer=false🔗
Iftrue, OpenXR will manage the depth buffer and use the depth buffer for advanced reprojection provided this is supported by the XR runtime. Note that some rendering features in Godot can't be used with this feature.
Stringxr/openxr/target_api_version=""🔗
Optionally sets a specific API version of OpenXR to initialize inmajor.minor.patchnotation. Some XR runtimes gate old behavior behind version checks. This is non-standard OpenXR behavior.
intxr/openxr/view_configuration="1"🔗
Specify the view configuration with which to configure OpenXR setting up either Mono or Stereo rendering.
boolxr/shaders/enabled=false🔗
Iftrue, Godot will compile shaders required for XR.

## Method Descriptions

voidadd_property_info(hint:Dictionary)🔗
Adds a custom property info to a property. The dictionary must contain:

- "name":String(the property's name)
"name":String(the property's name)
- "type":int(seeVariant.Type)
"type":int(seeVariant.Type)
- optionally"hint":int(seePropertyHint) and"hint_string":String
optionally"hint":int(seePropertyHint) and"hint_string":String

```
ProjectSettings.set("category/property_name", 0)

var property_info = {
    "name": "category/property_name",
    "type": TYPE_INT,
    "hint": PROPERTY_HINT_ENUM,
    "hint_string": "one,two,three"
}

ProjectSettings.add_property_info(property_info)
```

```
ProjectSettings.Singleton.Set("category/property_name", 0);

var propertyInfo = new Godot.Collections.Dictionary
{
    { "name", "category/propertyName" },
    { "type", (int)Variant.Type.Int },
    { "hint", (int)PropertyHint.Enum },
    { "hint_string", "one,two,three" },
};

ProjectSettings.AddPropertyInfo(propertyInfo);
```

Note:Setting"usage"for the property is not supported. Useset_as_basic(),set_restart_if_changed(), andset_as_internal()to modify usage flags.
boolcheck_changed_settings_in_group(setting_prefix:String)const🔗
Checks if any settings with the prefixsetting_prefixexist in the set of changed settings. See alsoget_changed_settings().
voidclear(name:String)🔗
Clears the whole configuration (not recommended, may break things).
PackedStringArrayget_changed_settings()const🔗
Gets an array of the settings which have been changed since the last save. Note that internallychanged_settingsis cleared after a successful save, so generally the most appropriate place to use this method is when processingsettings_changed.
Array[Dictionary]get_global_class_list()🔗
Returns anArrayof registered global classes. Each global class is represented as aDictionarythat contains the following entries:

- baseis a name of the base class;
baseis a name of the base class;
- classis a name of the registered global class;
classis a name of the registered global class;
- iconis a path to a custom icon of the global class, if it has any;
iconis a path to a custom icon of the global class, if it has any;
- languageis a name of a programming language in which the global class is written;
languageis a name of a programming language in which the global class is written;
- pathis a path to a file containing the global class.
pathis a path to a file containing the global class.
Note:Both the script and the icon paths are local to the project filesystem, i.e. they start withres://.
intget_order(name:String)const🔗
Returns the order of a configuration value (influences when saved to the config file).
Variantget_setting(name:String, default_value:Variant= null)const🔗
Returns the value of the setting identified byname. If the setting doesn't exist anddefault_valueis specified, the value ofdefault_valueis returned. Otherwise,nullis returned.

```
print(ProjectSettings.get_setting("application/config/name"))
print(ProjectSettings.get_setting("application/config/custom_description", "No description specified."))
```

```
GD.Print(ProjectSettings.GetSetting("application/config/name"));
GD.Print(ProjectSettings.GetSetting("application/config/custom_description", "No description specified."));
```

Note:This method doesn't take potential feature overrides into account automatically. Useget_setting_with_override()to handle seamlessly.
See alsohas_setting()to check whether a setting exists.
Variantget_setting_with_override(name:StringName)const🔗
Similar toget_setting(), but applies feature tag overrides if any exists and is valid.
Example:If the setting override"application/config/name.windows"exists, and the following code is executed on aWindowsoperating system, the overridden setting is printed instead:

```
print(ProjectSettings.get_setting_with_override("application/config/name"))
```

```
GD.Print(ProjectSettings.GetSettingWithOverride("application/config/name"));
```

Variantget_setting_with_override_and_custom_features(name:StringName, features:PackedStringArray)const🔗
Similar toget_setting_with_override(), but applies feature tag overrides instead of current OS features.
Stringglobalize_path(path:String)const🔗
Returns the absolute, native OS path corresponding to the localizedpath(starting withres://oruser://). The returned path will vary depending on the operating system and user preferences. SeeFile paths in Godot projectsto see what those paths convert to. See alsolocalize_path().
Note:globalize_path()withres://will not work in an exported project. Instead, prepend the executable's base directory to the path when running from an exported project:

```
var path = ""
if OS.has_feature("editor"):
    # Running from an editor binary.
    # `path` will contain the absolute path to `hello.txt` located in the project root.
    path = ProjectSettings.globalize_path("res://hello.txt")
else:
    # Running from an exported project.
    # `path` will contain the absolute path to `hello.txt` next to the executable.
    # This is *not* identical to using `ProjectSettings.globalize_path()` with a `res://` path,
    # but is close enough in spirit.
    path = OS.get_executable_path().get_base_dir().path_join("hello.txt")
```

boolhas_setting(name:String)const🔗
Returnstrueif a configuration value is present.
Note:In order to be be detected, custom settings have to be either defined withset_setting(), or exist in theproject.godotfile. This is especially relevant when usingset_initial_value().
boolload_resource_pack(pack:String, replace_files:bool= true, offset:int= 0)🔗
Loads the contents of the .pck or .zip file specified bypackinto the resource filesystem (res://). Returnstrueon success.
Note:If a file frompackshares the same path as a file already in the resource filesystem, any attempts to load that file will use the file frompackunlessreplace_filesis set tofalse.
Note:The optionaloffsetparameter can be used to specify the offset in bytes to the start of the resource pack. This is only supported for .pck files.
Note:DirAccesswill not show changes made to the contents ofres://after calling this function.
Stringlocalize_path(path:String)const🔗
Returns the localized path (starting withres://) corresponding to the absolute, native OSpath. See alsoglobalize_path().
Errorsave()🔗
Saves the configuration to theproject.godotfile.
Note:This method is intended to be used by editor plugins, as modifiedProjectSettingscan't be loaded back in the running app. If you want to change project settings in exported projects, usesave_custom()to saveoverride.cfgfile.
Errorsave_custom(file:String)🔗
Saves the configuration to a custom file. The file extension must be.godot(to save in text-basedConfigFileformat) or.binary(to save in binary format). You can also saveoverride.cfgfile, which is also text, but can be used in exported projects unlike other formats.
voidset_as_basic(name:String, basic:bool)🔗
Defines if the specified setting is considered basic or advanced. Basic settings will always be shown in the project settings. Advanced settings will only be shown if the user enables the "Advanced Settings" option.
voidset_as_internal(name:String, internal:bool)🔗
Defines if the specified setting is considered internal. An internal setting won't show up in the Project Settings dialog. This is mostly useful for addons that need to store their own internal settings without exposing them directly to the user.
voidset_initial_value(name:String, value:Variant)🔗
Sets the specified setting's initial value. This is the value the setting reverts to. The setting should already exist before calling this method. Note that project settings equal to their default value are not saved, so your code needs to account for that.

```
extends EditorPlugin

const SETTING_NAME = "addons/my_setting"
const SETTING_DEFAULT = 10.0

func _enter_tree():
    if not ProjectSettings.has_setting(SETTING_NAME):
        ProjectSettings.set_setting(SETTING_NAME, SETTING_DEFAULT)

    ProjectSettings.set_initial_value(SETTING_NAME, SETTING_DEFAULT)
```

If you have a project setting defined by anEditorPlugin, but want to use it in a running project, you will need a similar code at runtime.
voidset_order(name:String, position:int)🔗
Sets the order of a configuration value (influences when saved to the config file).
voidset_restart_if_changed(name:String, restart:bool)🔗
Sets whether a setting requires restarting the editor to properly take effect.
Note:This is just a hint to display to the user that the editor must be restarted for changes to take effect. Enablingset_restart_if_changed()doesnotdelay the setting being set when changed.
voidset_setting(name:String, value:Variant)🔗
Sets the value of a setting.

```
ProjectSettings.set_setting("application/config/name", "Example")
```

```
ProjectSettings.SetSetting("application/config/name", "Example");
```

This can also be used to erase custom project settings. To do this change the setting value tonull.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
