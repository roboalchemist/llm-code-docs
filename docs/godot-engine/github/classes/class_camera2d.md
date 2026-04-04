:github_url: hide



# Camera2D

**Inherits:** [Node2D<class_Node2D>] **<** [CanvasItem<class_CanvasItem>] **<** [Node<class_Node>] **<** [Object<class_Object>]

Camera node for 2D scenes.


## Description

Camera node for 2D scenes. It forces the screen (current layer) to scroll following this node. This makes it easier (and faster) to program scrollable scenes than manually changing the position of [CanvasItem<class_CanvasItem>]-based nodes.

Cameras register themselves in the nearest [Viewport<class_Viewport>] node (when ascending the tree). Only one camera can be active per viewport. If no viewport is available ascending the tree, the camera will register in the global viewport.

This node is intended to be a simple helper to get things going quickly, but more functionality may be desired to change how the camera works. To make your own custom camera node, inherit it from [Node2D<class_Node2D>] and change the transform of the canvas by setting [Viewport.canvas_transform<class_Viewport_property_canvas_transform>] in [Viewport<class_Viewport>] (you can obtain the current [Viewport<class_Viewport>] by using [Node.get_viewport()<class_Node_method_get_viewport>]).

Note that the **Camera2D** node's [Node2D.global_position<class_Node2D_property_global_position>] doesn't represent the actual position of the screen, which may differ due to applied smoothing or limits. You can use [get_screen_center_position()<class_Camera2D_method_get_screen_center_position>] to get the real position. Same for the node's [Node2D.global_rotation<class_Node2D_property_global_rotation>] which may be different due to applied rotation smoothing. You can use [get_screen_rotation()<class_Camera2D_method_get_screen_rotation>] to get the current rotation of the screen.


## Tutorials

- [2D Platformer Demo ](https://godotengine.org/asset-library/asset/2727)_

- [2D Isometric Demo ](https://godotengine.org/asset-library/asset/2718)_


## Properties

> **TABLE**
> :widths: auto
>
> +-----------------------------------------------------------------------+---------------------------------------------------------------------------------------+-------------------+
> | :ref:`AnchorMode<enum_Camera2D_AnchorMode>`                           | :ref:`anchor_mode<class_Camera2D_property_anchor_mode>`                               | ``1``             |
> +-----------------------------------------------------------------------+---------------------------------------------------------------------------------------+-------------------+
> | :ref:`Node<class_Node>`                                               | :ref:`custom_viewport<class_Camera2D_property_custom_viewport>`                       |                   |
> +-----------------------------------------------------------------------+---------------------------------------------------------------------------------------+-------------------+
> | :ref:`float<class_float>`                                             | :ref:`drag_bottom_margin<class_Camera2D_property_drag_bottom_margin>`                 | ``0.2``           |
> +-----------------------------------------------------------------------+---------------------------------------------------------------------------------------+-------------------+
> | :ref:`bool<class_bool>`                                               | :ref:`drag_horizontal_enabled<class_Camera2D_property_drag_horizontal_enabled>`       | ``false``         |
> +-----------------------------------------------------------------------+---------------------------------------------------------------------------------------+-------------------+
> | :ref:`float<class_float>`                                             | :ref:`drag_horizontal_offset<class_Camera2D_property_drag_horizontal_offset>`         | ``0.0``           |
> +-----------------------------------------------------------------------+---------------------------------------------------------------------------------------+-------------------+
> | :ref:`float<class_float>`                                             | :ref:`drag_left_margin<class_Camera2D_property_drag_left_margin>`                     | ``0.2``           |
> +-----------------------------------------------------------------------+---------------------------------------------------------------------------------------+-------------------+
> | :ref:`float<class_float>`                                             | :ref:`drag_right_margin<class_Camera2D_property_drag_right_margin>`                   | ``0.2``           |
> +-----------------------------------------------------------------------+---------------------------------------------------------------------------------------+-------------------+
> | :ref:`float<class_float>`                                             | :ref:`drag_top_margin<class_Camera2D_property_drag_top_margin>`                       | ``0.2``           |
> +-----------------------------------------------------------------------+---------------------------------------------------------------------------------------+-------------------+
> | :ref:`bool<class_bool>`                                               | :ref:`drag_vertical_enabled<class_Camera2D_property_drag_vertical_enabled>`           | ``false``         |
> +-----------------------------------------------------------------------+---------------------------------------------------------------------------------------+-------------------+
> | :ref:`float<class_float>`                                             | :ref:`drag_vertical_offset<class_Camera2D_property_drag_vertical_offset>`             | ``0.0``           |
> +-----------------------------------------------------------------------+---------------------------------------------------------------------------------------+-------------------+
> | :ref:`bool<class_bool>`                                               | :ref:`editor_draw_drag_margin<class_Camera2D_property_editor_draw_drag_margin>`       | ``false``         |
> +-----------------------------------------------------------------------+---------------------------------------------------------------------------------------+-------------------+
> | :ref:`bool<class_bool>`                                               | :ref:`editor_draw_limits<class_Camera2D_property_editor_draw_limits>`                 | ``false``         |
> +-----------------------------------------------------------------------+---------------------------------------------------------------------------------------+-------------------+
> | :ref:`bool<class_bool>`                                               | :ref:`editor_draw_screen<class_Camera2D_property_editor_draw_screen>`                 | ``true``          |
> +-----------------------------------------------------------------------+---------------------------------------------------------------------------------------+-------------------+
> | :ref:`bool<class_bool>`                                               | :ref:`enabled<class_Camera2D_property_enabled>`                                       | ``true``          |
> +-----------------------------------------------------------------------+---------------------------------------------------------------------------------------+-------------------+
> | :ref:`bool<class_bool>`                                               | :ref:`ignore_rotation<class_Camera2D_property_ignore_rotation>`                       | ``true``          |
> +-----------------------------------------------------------------------+---------------------------------------------------------------------------------------+-------------------+
> | :ref:`int<class_int>`                                                 | :ref:`limit_bottom<class_Camera2D_property_limit_bottom>`                             | ``10000000``      |
> +-----------------------------------------------------------------------+---------------------------------------------------------------------------------------+-------------------+
> | :ref:`bool<class_bool>`                                               | :ref:`limit_enabled<class_Camera2D_property_limit_enabled>`                           | ``true``          |
> +-----------------------------------------------------------------------+---------------------------------------------------------------------------------------+-------------------+
> | :ref:`int<class_int>`                                                 | :ref:`limit_left<class_Camera2D_property_limit_left>`                                 | ``-10000000``     |
> +-----------------------------------------------------------------------+---------------------------------------------------------------------------------------+-------------------+
> | :ref:`int<class_int>`                                                 | :ref:`limit_right<class_Camera2D_property_limit_right>`                               | ``10000000``      |
> +-----------------------------------------------------------------------+---------------------------------------------------------------------------------------+-------------------+
> | :ref:`bool<class_bool>`                                               | :ref:`limit_smoothed<class_Camera2D_property_limit_smoothed>`                         | ``false``         |
> +-----------------------------------------------------------------------+---------------------------------------------------------------------------------------+-------------------+
> | :ref:`int<class_int>`                                                 | :ref:`limit_top<class_Camera2D_property_limit_top>`                                   | ``-10000000``     |
> +-----------------------------------------------------------------------+---------------------------------------------------------------------------------------+-------------------+
> | :ref:`Vector2<class_Vector2>`                                         | :ref:`offset<class_Camera2D_property_offset>`                                         | ``Vector2(0, 0)`` |
> +-----------------------------------------------------------------------+---------------------------------------------------------------------------------------+-------------------+
> | :ref:`bool<class_bool>`                                               | :ref:`position_smoothing_enabled<class_Camera2D_property_position_smoothing_enabled>` | ``false``         |
> +-----------------------------------------------------------------------+---------------------------------------------------------------------------------------+-------------------+
> | :ref:`float<class_float>`                                             | :ref:`position_smoothing_speed<class_Camera2D_property_position_smoothing_speed>`     | ``5.0``           |
> +-----------------------------------------------------------------------+---------------------------------------------------------------------------------------+-------------------+
> | :ref:`Camera2DProcessCallback<enum_Camera2D_Camera2DProcessCallback>` | :ref:`process_callback<class_Camera2D_property_process_callback>`                     | ``1``             |
> +-----------------------------------------------------------------------+---------------------------------------------------------------------------------------+-------------------+
> | :ref:`bool<class_bool>`                                               | :ref:`rotation_smoothing_enabled<class_Camera2D_property_rotation_smoothing_enabled>` | ``false``         |
> +-----------------------------------------------------------------------+---------------------------------------------------------------------------------------+-------------------+
> | :ref:`float<class_float>`                                             | :ref:`rotation_smoothing_speed<class_Camera2D_property_rotation_smoothing_speed>`     | ``5.0``           |
> +-----------------------------------------------------------------------+---------------------------------------------------------------------------------------+-------------------+
> | :ref:`Vector2<class_Vector2>`                                         | :ref:`zoom<class_Camera2D_property_zoom>`                                             | ``Vector2(1, 1)`` |
> +-----------------------------------------------------------------------+---------------------------------------------------------------------------------------+-------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +-------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                        | :ref:`align<class_Camera2D_method_align>`\ (\ )                                                                                                            |
> +-------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                        | :ref:`force_update_scroll<class_Camera2D_method_force_update_scroll>`\ (\ )                                                                                |
> +-------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`     | :ref:`get_drag_margin<class_Camera2D_method_get_drag_margin>`\ (\ margin\: :ref:`Side<enum_@GlobalScope_Side>`\ ) |const|                                  |
> +-------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`         | :ref:`get_limit<class_Camera2D_method_get_limit>`\ (\ margin\: :ref:`Side<enum_@GlobalScope_Side>`\ ) |const|                                              |
> +-------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector2<class_Vector2>` | :ref:`get_screen_center_position<class_Camera2D_method_get_screen_center_position>`\ (\ ) |const|                                                          |
> +-------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`     | :ref:`get_screen_rotation<class_Camera2D_method_get_screen_rotation>`\ (\ ) |const|                                                                        |
> +-------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector2<class_Vector2>` | :ref:`get_target_position<class_Camera2D_method_get_target_position>`\ (\ ) |const|                                                                        |
> +-------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`       | :ref:`is_current<class_Camera2D_method_is_current>`\ (\ ) |const|                                                                                          |
> +-------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                        | :ref:`make_current<class_Camera2D_method_make_current>`\ (\ )                                                                                              |
> +-------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                        | :ref:`reset_smoothing<class_Camera2D_method_reset_smoothing>`\ (\ )                                                                                        |
> +-------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                        | :ref:`set_drag_margin<class_Camera2D_method_set_drag_margin>`\ (\ margin\: :ref:`Side<enum_@GlobalScope_Side>`, drag_margin\: :ref:`float<class_float>`\ ) |
> +-------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                        | :ref:`set_limit<class_Camera2D_method_set_limit>`\ (\ margin\: :ref:`Side<enum_@GlobalScope_Side>`, limit\: :ref:`int<class_int>`\ )                       |
> +-------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Enumerations



enum **AnchorMode**: [🔗<enum_Camera2D_AnchorMode>]



[AnchorMode<enum_Camera2D_AnchorMode>] **ANCHOR_MODE_FIXED_TOP_LEFT** = `0`

The camera's position is fixed so that the top-left corner is always at the origin.



[AnchorMode<enum_Camera2D_AnchorMode>] **ANCHOR_MODE_DRAG_CENTER** = `1`

The camera's position takes into account vertical/horizontal offsets and the screen size.


----



enum **Camera2DProcessCallback**: [🔗<enum_Camera2D_Camera2DProcessCallback>]



[Camera2DProcessCallback<enum_Camera2D_Camera2DProcessCallback>] **CAMERA2D_PROCESS_PHYSICS** = `0`

The camera updates during physics frames (see [Node.NOTIFICATION_INTERNAL_PHYSICS_PROCESS<class_Node_constant_NOTIFICATION_INTERNAL_PHYSICS_PROCESS>]).



[Camera2DProcessCallback<enum_Camera2D_Camera2DProcessCallback>] **CAMERA2D_PROCESS_IDLE** = `1`

The camera updates during process frames (see [Node.NOTIFICATION_INTERNAL_PROCESS<class_Node_constant_NOTIFICATION_INTERNAL_PROCESS>]).


----


## Property Descriptions



[AnchorMode<enum_Camera2D_AnchorMode>] **anchor_mode** = `1` [🔗<class_Camera2D_property_anchor_mode>]


- |void| **set_anchor_mode**\ (\ value\: [AnchorMode<enum_Camera2D_AnchorMode>]\ )
- [AnchorMode<enum_Camera2D_AnchorMode>] **get_anchor_mode**\ (\ )

The Camera2D's anchor point.


----



[Node<class_Node>] **custom_viewport** [🔗<class_Camera2D_property_custom_viewport>]


- |void| **set_custom_viewport**\ (\ value\: [Node<class_Node>]\ )
- [Node<class_Node>] **get_custom_viewport**\ (\ )

The custom [Viewport<class_Viewport>] node attached to the **Camera2D**. If `null` or not a [Viewport<class_Viewport>], uses the default viewport instead.


----



[float<class_float>] **drag_bottom_margin** = `0.2` [🔗<class_Camera2D_property_drag_bottom_margin>]


- |void| **set_drag_margin**\ (\ margin\: [Side<enum_@GlobalScope_Side>], drag_margin\: [float<class_float>]\ )
- [float<class_float>] **get_drag_margin**\ (\ margin\: [Side<enum_@GlobalScope_Side>]\ ) |const|

Bottom margin needed to drag the camera. A value of `1` makes the camera move only when reaching the bottom edge of the screen.


----



[bool<class_bool>] **drag_horizontal_enabled** = `false` [🔗<class_Camera2D_property_drag_horizontal_enabled>]


- |void| **set_drag_horizontal_enabled**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_drag_horizontal_enabled**\ (\ )

If `true`, the camera only moves when reaching the horizontal (left and right) drag margins. If `false`, the camera moves horizontally regardless of margins.


----



[float<class_float>] **drag_horizontal_offset** = `0.0` [🔗<class_Camera2D_property_drag_horizontal_offset>]


- |void| **set_drag_horizontal_offset**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_drag_horizontal_offset**\ (\ )

The relative horizontal drag offset of the camera between the right (`-1`) and left (`1`) drag margins.

\ **Note:** Used to set the initial horizontal drag offset; determine the current offset; or force the current offset. It's not automatically updated when [drag_horizontal_enabled<class_Camera2D_property_drag_horizontal_enabled>] is `true` or the drag margins are changed.


----



[float<class_float>] **drag_left_margin** = `0.2` [🔗<class_Camera2D_property_drag_left_margin>]


- |void| **set_drag_margin**\ (\ margin\: [Side<enum_@GlobalScope_Side>], drag_margin\: [float<class_float>]\ )
- [float<class_float>] **get_drag_margin**\ (\ margin\: [Side<enum_@GlobalScope_Side>]\ ) |const|

Left margin needed to drag the camera. A value of `1` makes the camera move only when reaching the left edge of the screen.


----



[float<class_float>] **drag_right_margin** = `0.2` [🔗<class_Camera2D_property_drag_right_margin>]


- |void| **set_drag_margin**\ (\ margin\: [Side<enum_@GlobalScope_Side>], drag_margin\: [float<class_float>]\ )
- [float<class_float>] **get_drag_margin**\ (\ margin\: [Side<enum_@GlobalScope_Side>]\ ) |const|

Right margin needed to drag the camera. A value of `1` makes the camera move only when reaching the right edge of the screen.


----



[float<class_float>] **drag_top_margin** = `0.2` [🔗<class_Camera2D_property_drag_top_margin>]


- |void| **set_drag_margin**\ (\ margin\: [Side<enum_@GlobalScope_Side>], drag_margin\: [float<class_float>]\ )
- [float<class_float>] **get_drag_margin**\ (\ margin\: [Side<enum_@GlobalScope_Side>]\ ) |const|

Top margin needed to drag the camera. A value of `1` makes the camera move only when reaching the top edge of the screen.


----



[bool<class_bool>] **drag_vertical_enabled** = `false` [🔗<class_Camera2D_property_drag_vertical_enabled>]


- |void| **set_drag_vertical_enabled**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_drag_vertical_enabled**\ (\ )

If `true`, the camera only moves when reaching the vertical (top and bottom) drag margins. If `false`, the camera moves vertically regardless of the drag margins.


----



[float<class_float>] **drag_vertical_offset** = `0.0` [🔗<class_Camera2D_property_drag_vertical_offset>]


- |void| **set_drag_vertical_offset**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_drag_vertical_offset**\ (\ )

The relative vertical drag offset of the camera between the bottom (`-1`) and top (`1`) drag margins.

\ **Note:** Used to set the initial vertical drag offset; determine the current offset; or force the current offset. It's not automatically updated when [drag_vertical_enabled<class_Camera2D_property_drag_vertical_enabled>] is `true` or the drag margins are changed.


----



[bool<class_bool>] **editor_draw_drag_margin** = `false` [🔗<class_Camera2D_property_editor_draw_drag_margin>]


- |void| **set_margin_drawing_enabled**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_margin_drawing_enabled**\ (\ )

If `true`, draws the camera's drag margin rectangle in the editor.


----



[bool<class_bool>] **editor_draw_limits** = `false` [🔗<class_Camera2D_property_editor_draw_limits>]


- |void| **set_limit_drawing_enabled**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_limit_drawing_enabled**\ (\ )

If `true`, draws the camera's limits rectangle in the editor.


----



[bool<class_bool>] **editor_draw_screen** = `true` [🔗<class_Camera2D_property_editor_draw_screen>]


- |void| **set_screen_drawing_enabled**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_screen_drawing_enabled**\ (\ )

If `true`, draws the camera's screen rectangle in the editor.


----



[bool<class_bool>] **enabled** = `true` [🔗<class_Camera2D_property_enabled>]


- |void| **set_enabled**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_enabled**\ (\ )

Controls whether the camera can be active or not. If `true`, the **Camera2D** will become the main camera when it enters the scene tree and there is no active camera currently (see [Viewport.get_camera_2d()<class_Viewport_method_get_camera_2d>]).

When the camera is currently active and [enabled<class_Camera2D_property_enabled>] is set to `false`, the next enabled **Camera2D** in the scene tree will become active.


----



[bool<class_bool>] **ignore_rotation** = `true` [🔗<class_Camera2D_property_ignore_rotation>]


- |void| **set_ignore_rotation**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_ignoring_rotation**\ (\ )

If `true`, the camera's rendered view is not affected by its [Node2D.rotation<class_Node2D_property_rotation>] and [Node2D.global_rotation<class_Node2D_property_global_rotation>].


----



[int<class_int>] **limit_bottom** = `10000000` [🔗<class_Camera2D_property_limit_bottom>]


- |void| **set_limit**\ (\ margin\: [Side<enum_@GlobalScope_Side>], limit\: [int<class_int>]\ )
- [int<class_int>] **get_limit**\ (\ margin\: [Side<enum_@GlobalScope_Side>]\ ) |const|

Bottom scroll limit in pixels. The camera stops moving when reaching this value, but [offset<class_Camera2D_property_offset>] can push the view past the limit.


----



[bool<class_bool>] **limit_enabled** = `true` [🔗<class_Camera2D_property_limit_enabled>]


- |void| **set_limit_enabled**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_limit_enabled**\ (\ )

If `true`, the limits will be enabled. Disabling this will allow the camera to focus anywhere, when the four `limit_*` properties will not work.


----



[int<class_int>] **limit_left** = `-10000000` [🔗<class_Camera2D_property_limit_left>]


- |void| **set_limit**\ (\ margin\: [Side<enum_@GlobalScope_Side>], limit\: [int<class_int>]\ )
- [int<class_int>] **get_limit**\ (\ margin\: [Side<enum_@GlobalScope_Side>]\ ) |const|

Left scroll limit in pixels. The camera stops moving when reaching this value, but [offset<class_Camera2D_property_offset>] can push the view past the limit.


----



[int<class_int>] **limit_right** = `10000000` [🔗<class_Camera2D_property_limit_right>]


- |void| **set_limit**\ (\ margin\: [Side<enum_@GlobalScope_Side>], limit\: [int<class_int>]\ )
- [int<class_int>] **get_limit**\ (\ margin\: [Side<enum_@GlobalScope_Side>]\ ) |const|

Right scroll limit in pixels. The camera stops moving when reaching this value, but [offset<class_Camera2D_property_offset>] can push the view past the limit.


----



[bool<class_bool>] **limit_smoothed** = `false` [🔗<class_Camera2D_property_limit_smoothed>]


- |void| **set_limit_smoothing_enabled**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_limit_smoothing_enabled**\ (\ )

If `true`, the camera smoothly stops when reaches its limits.

This property has no effect if [position_smoothing_enabled<class_Camera2D_property_position_smoothing_enabled>] is `false`.

\ **Note:** To immediately update the camera's position to be within limits without smoothing, even with this setting enabled, invoke [reset_smoothing()<class_Camera2D_method_reset_smoothing>].


----



[int<class_int>] **limit_top** = `-10000000` [🔗<class_Camera2D_property_limit_top>]


- |void| **set_limit**\ (\ margin\: [Side<enum_@GlobalScope_Side>], limit\: [int<class_int>]\ )
- [int<class_int>] **get_limit**\ (\ margin\: [Side<enum_@GlobalScope_Side>]\ ) |const|

Top scroll limit in pixels. The camera stops moving when reaching this value, but [offset<class_Camera2D_property_offset>] can push the view past the limit.


----



[Vector2<class_Vector2>] **offset** = `Vector2(0, 0)` [🔗<class_Camera2D_property_offset>]


- |void| **set_offset**\ (\ value\: [Vector2<class_Vector2>]\ )
- [Vector2<class_Vector2>] **get_offset**\ (\ )

The camera's relative offset. Useful for looking around or camera shake animations. The offsetted camera can go past the limits defined in [limit_top<class_Camera2D_property_limit_top>], [limit_bottom<class_Camera2D_property_limit_bottom>], [limit_left<class_Camera2D_property_limit_left>] and [limit_right<class_Camera2D_property_limit_right>].


----



[bool<class_bool>] **position_smoothing_enabled** = `false` [🔗<class_Camera2D_property_position_smoothing_enabled>]


- |void| **set_position_smoothing_enabled**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_position_smoothing_enabled**\ (\ )

If `true`, the camera's view smoothly moves towards its target position at [position_smoothing_speed<class_Camera2D_property_position_smoothing_speed>].


----



[float<class_float>] **position_smoothing_speed** = `5.0` [🔗<class_Camera2D_property_position_smoothing_speed>]


- |void| **set_position_smoothing_speed**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_position_smoothing_speed**\ (\ )

Speed in pixels per second of the camera's smoothing effect when [position_smoothing_enabled<class_Camera2D_property_position_smoothing_enabled>] is `true`.


----



[Camera2DProcessCallback<enum_Camera2D_Camera2DProcessCallback>] **process_callback** = `1` [🔗<class_Camera2D_property_process_callback>]


- |void| **set_process_callback**\ (\ value\: [Camera2DProcessCallback<enum_Camera2D_Camera2DProcessCallback>]\ )
- [Camera2DProcessCallback<enum_Camera2D_Camera2DProcessCallback>] **get_process_callback**\ (\ )

The camera's process callback.


----



[bool<class_bool>] **rotation_smoothing_enabled** = `false` [🔗<class_Camera2D_property_rotation_smoothing_enabled>]


- |void| **set_rotation_smoothing_enabled**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_rotation_smoothing_enabled**\ (\ )

If `true`, the camera's view smoothly rotates, via asymptotic smoothing, to align with its target rotation at [rotation_smoothing_speed<class_Camera2D_property_rotation_smoothing_speed>].

\ **Note:** This property has no effect if [ignore_rotation<class_Camera2D_property_ignore_rotation>] is `true`.


----



[float<class_float>] **rotation_smoothing_speed** = `5.0` [🔗<class_Camera2D_property_rotation_smoothing_speed>]


- |void| **set_rotation_smoothing_speed**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_rotation_smoothing_speed**\ (\ )

The angular, asymptotic speed of the camera's rotation smoothing effect when [rotation_smoothing_enabled<class_Camera2D_property_rotation_smoothing_enabled>] is `true`.


----



[Vector2<class_Vector2>] **zoom** = `Vector2(1, 1)` [🔗<class_Camera2D_property_zoom>]


- |void| **set_zoom**\ (\ value\: [Vector2<class_Vector2>]\ )
- [Vector2<class_Vector2>] **get_zoom**\ (\ )

The camera's zoom. Higher values are more zoomed in. For example, a zoom of `Vector2(2.0, 2.0)` will be twice as zoomed in on each axis (the view covers an area four times smaller). In contrast, a zoom of `Vector2(0.5, 0.5)` will be twice as zoomed out on each axis (the view covers an area four times larger). The X and Y components should generally always be set to the same value, unless you wish to stretch the camera view.

\ **Note:** [FontFile.oversampling<class_FontFile_property_oversampling>] does *not* take **Camera2D** zoom into account. This means that zooming in/out will cause bitmap fonts and rasterized (non-MSDF) dynamic fonts to appear blurry or pixelated unless the font is part of a [CanvasLayer<class_CanvasLayer>] that makes it ignore camera zoom. To ensure text remains crisp regardless of zoom, you can enable MSDF font rendering by enabling [ProjectSettings.gui/theme/default_font_multichannel_signed_distance_field<class_ProjectSettings_property_gui/theme/default_font_multichannel_signed_distance_field>] (applies to the default project font only), or enabling **Multichannel Signed Distance Field** in the import options of a DynamicFont for custom fonts. On system fonts, [SystemFont.multichannel_signed_distance_field<class_SystemFont_property_multichannel_signed_distance_field>] can be enabled in the inspector.


----


## Method Descriptions



|void| **align**\ (\ ) [🔗<class_Camera2D_method_align>]

Aligns the camera to the tracked node.

\ **Note:** Calling [force_update_scroll()<class_Camera2D_method_force_update_scroll>] after this method is not required.


----



|void| **force_update_scroll**\ (\ ) [🔗<class_Camera2D_method_force_update_scroll>]

Forces the camera to update scroll immediately.


----



[float<class_float>] **get_drag_margin**\ (\ margin\: [Side<enum_@GlobalScope_Side>]\ ) |const| [🔗<class_Camera2D_method_get_drag_margin>]

Returns the specified [Side<enum_@GlobalScope_Side>]'s margin. See also [drag_bottom_margin<class_Camera2D_property_drag_bottom_margin>], [drag_top_margin<class_Camera2D_property_drag_top_margin>], [drag_left_margin<class_Camera2D_property_drag_left_margin>], and [drag_right_margin<class_Camera2D_property_drag_right_margin>].


----



[int<class_int>] **get_limit**\ (\ margin\: [Side<enum_@GlobalScope_Side>]\ ) |const| [🔗<class_Camera2D_method_get_limit>]

Returns the camera limit for the specified [Side<enum_@GlobalScope_Side>]. See also [limit_bottom<class_Camera2D_property_limit_bottom>], [limit_top<class_Camera2D_property_limit_top>], [limit_left<class_Camera2D_property_limit_left>], and [limit_right<class_Camera2D_property_limit_right>].


----



[Vector2<class_Vector2>] **get_screen_center_position**\ (\ ) |const| [🔗<class_Camera2D_method_get_screen_center_position>]

Returns the center of the screen from this camera's point of view, in global coordinates.

\ **Note:** The exact targeted position of the camera may be different. See [get_target_position()<class_Camera2D_method_get_target_position>].


----



[float<class_float>] **get_screen_rotation**\ (\ ) |const| [🔗<class_Camera2D_method_get_screen_rotation>]

Returns the current screen rotation from this camera's point of view.

\ **Note:** The screen rotation can be different from [Node2D.global_rotation<class_Node2D_property_global_rotation>] if the camera is rotating smoothly due to [rotation_smoothing_enabled<class_Camera2D_property_rotation_smoothing_enabled>].


----



[Vector2<class_Vector2>] **get_target_position**\ (\ ) |const| [🔗<class_Camera2D_method_get_target_position>]

Returns this camera's target position, in global coordinates.

\ **Note:** The returned value is not the same as [Node2D.global_position<class_Node2D_property_global_position>], as it is affected by the drag properties. It is also not the same as the current position if [position_smoothing_enabled<class_Camera2D_property_position_smoothing_enabled>] is `true` (see [get_screen_center_position()<class_Camera2D_method_get_screen_center_position>]).


----



[bool<class_bool>] **is_current**\ (\ ) |const| [🔗<class_Camera2D_method_is_current>]

Returns `true` if this **Camera2D** is the active camera (see [Viewport.get_camera_2d()<class_Viewport_method_get_camera_2d>]).


----



|void| **make_current**\ (\ ) [🔗<class_Camera2D_method_make_current>]

Forces this **Camera2D** to become the current active one. [enabled<class_Camera2D_property_enabled>] must be `true`.


----



|void| **reset_smoothing**\ (\ ) [🔗<class_Camera2D_method_reset_smoothing>]

Sets the camera's position immediately to its current smoothing destination.

This method has no effect if [position_smoothing_enabled<class_Camera2D_property_position_smoothing_enabled>] is `false`.


----



|void| **set_drag_margin**\ (\ margin\: [Side<enum_@GlobalScope_Side>], drag_margin\: [float<class_float>]\ ) [🔗<class_Camera2D_method_set_drag_margin>]

Sets the specified [Side<enum_@GlobalScope_Side>]'s margin. See also [drag_bottom_margin<class_Camera2D_property_drag_bottom_margin>], [drag_top_margin<class_Camera2D_property_drag_top_margin>], [drag_left_margin<class_Camera2D_property_drag_left_margin>], and [drag_right_margin<class_Camera2D_property_drag_right_margin>].


----



|void| **set_limit**\ (\ margin\: [Side<enum_@GlobalScope_Side>], limit\: [int<class_int>]\ ) [🔗<class_Camera2D_method_set_limit>]

Sets the camera limit for the specified [Side<enum_@GlobalScope_Side>]. See also [limit_bottom<class_Camera2D_property_limit_bottom>], [limit_top<class_Camera2D_property_limit_top>], [limit_left<class_Camera2D_property_limit_left>], and [limit_right<class_Camera2D_property_limit_right>].

