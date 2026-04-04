:github_url: hide



# SplitContainer

**Inherits:** [Container<class_Container>] **<** [Control<class_Control>] **<** [CanvasItem<class_CanvasItem>] **<** [Node<class_Node>] **<** [Object<class_Object>]

**Inherited By:** [HSplitContainer<class_HSplitContainer>], [VSplitContainer<class_VSplitContainer>]

A container that arranges child controls horizontally or vertically and provides grabbers for adjusting the split ratios between them.


## Description

A container that arranges child controls horizontally or vertically and creates grabbers between them. The grabbers can be dragged around to change the size relations between the child controls.


## Tutorials

- [../tutorials/ui/gui_containers](Using Containers .md)


## Properties

> **TABLE**
> :widths: auto
>
> +-----------------------------------------------------------------+---------------------------------------------------------------------------------------------------+-------------------------+
> | :ref:`bool<class_bool>`                                         | :ref:`collapsed<class_SplitContainer_property_collapsed>`                                         | ``false``               |
> +-----------------------------------------------------------------+---------------------------------------------------------------------------------------------------+-------------------------+
> | :ref:`bool<class_bool>`                                         | :ref:`drag_area_highlight_in_editor<class_SplitContainer_property_drag_area_highlight_in_editor>` | ``false``               |
> +-----------------------------------------------------------------+---------------------------------------------------------------------------------------------------+-------------------------+
> | :ref:`int<class_int>`                                           | :ref:`drag_area_margin_begin<class_SplitContainer_property_drag_area_margin_begin>`               | ``0``                   |
> +-----------------------------------------------------------------+---------------------------------------------------------------------------------------------------+-------------------------+
> | :ref:`int<class_int>`                                           | :ref:`drag_area_margin_end<class_SplitContainer_property_drag_area_margin_end>`                   | ``0``                   |
> +-----------------------------------------------------------------+---------------------------------------------------------------------------------------------------+-------------------------+
> | :ref:`int<class_int>`                                           | :ref:`drag_area_offset<class_SplitContainer_property_drag_area_offset>`                           | ``0``                   |
> +-----------------------------------------------------------------+---------------------------------------------------------------------------------------------------+-------------------------+
> | :ref:`DraggerVisibility<enum_SplitContainer_DraggerVisibility>` | :ref:`dragger_visibility<class_SplitContainer_property_dragger_visibility>`                       | ``0``                   |
> +-----------------------------------------------------------------+---------------------------------------------------------------------------------------------------+-------------------------+
> | :ref:`bool<class_bool>`                                         | :ref:`dragging_enabled<class_SplitContainer_property_dragging_enabled>`                           | ``true``                |
> +-----------------------------------------------------------------+---------------------------------------------------------------------------------------------------+-------------------------+
> | :ref:`int<class_int>`                                           | :ref:`split_offset<class_SplitContainer_property_split_offset>`                                   | ``0``                   |
> +-----------------------------------------------------------------+---------------------------------------------------------------------------------------------------+-------------------------+
> | :ref:`PackedInt32Array<class_PackedInt32Array>`                 | :ref:`split_offsets<class_SplitContainer_property_split_offsets>`                                 | ``PackedInt32Array(0)`` |
> +-----------------------------------------------------------------+---------------------------------------------------------------------------------------------------+-------------------------+
> | :ref:`bool<class_bool>`                                         | :ref:`touch_dragger_enabled<class_SplitContainer_property_touch_dragger_enabled>`                 | ``false``               |
> +-----------------------------------------------------------------+---------------------------------------------------------------------------------------------------+-------------------------+
> | :ref:`bool<class_bool>`                                         | :ref:`vertical<class_SplitContainer_property_vertical>`                                           | ``false``               |
> +-----------------------------------------------------------------+---------------------------------------------------------------------------------------------------+-------------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                     | :ref:`clamp_split_offset<class_SplitContainer_method_clamp_split_offset>`\ (\ priority_index\: :ref:`int<class_int>` = 0\ ) |
> +------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Control<class_Control>`                              | :ref:`get_drag_area_control<class_SplitContainer_method_get_drag_area_control>`\ (\ )                                       |
> +------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`\[:ref:`Control<class_Control>`\] | :ref:`get_drag_area_controls<class_SplitContainer_method_get_drag_area_controls>`\ (\ )                                     |
> +------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
>

## Theme Properties

> **TABLE**
> :widths: auto
>
> +-----------------------------------+--------------------------------------------------------------------------------------------------+-------------------------+
> | :ref:`Color<class_Color>`         | :ref:`touch_dragger_color<class_SplitContainer_theme_color_touch_dragger_color>`                 | ``Color(1, 1, 1, 0.3)`` |
> +-----------------------------------+--------------------------------------------------------------------------------------------------+-------------------------+
> | :ref:`Color<class_Color>`         | :ref:`touch_dragger_hover_color<class_SplitContainer_theme_color_touch_dragger_hover_color>`     | ``Color(1, 1, 1, 0.6)`` |
> +-----------------------------------+--------------------------------------------------------------------------------------------------+-------------------------+
> | :ref:`Color<class_Color>`         | :ref:`touch_dragger_pressed_color<class_SplitContainer_theme_color_touch_dragger_pressed_color>` | ``Color(1, 1, 1, 1)``   |
> +-----------------------------------+--------------------------------------------------------------------------------------------------+-------------------------+
> | :ref:`int<class_int>`             | :ref:`autohide<class_SplitContainer_theme_constant_autohide>`                                    | ``1``                   |
> +-----------------------------------+--------------------------------------------------------------------------------------------------+-------------------------+
> | :ref:`int<class_int>`             | :ref:`minimum_grab_thickness<class_SplitContainer_theme_constant_minimum_grab_thickness>`        | ``6``                   |
> +-----------------------------------+--------------------------------------------------------------------------------------------------+-------------------------+
> | :ref:`int<class_int>`             | :ref:`separation<class_SplitContainer_theme_constant_separation>`                                | ``12``                  |
> +-----------------------------------+--------------------------------------------------------------------------------------------------+-------------------------+
> | :ref:`Texture2D<class_Texture2D>` | :ref:`grabber<class_SplitContainer_theme_icon_grabber>`                                          |                         |
> +-----------------------------------+--------------------------------------------------------------------------------------------------+-------------------------+
> | :ref:`Texture2D<class_Texture2D>` | :ref:`h_grabber<class_SplitContainer_theme_icon_h_grabber>`                                      |                         |
> +-----------------------------------+--------------------------------------------------------------------------------------------------+-------------------------+
> | :ref:`Texture2D<class_Texture2D>` | :ref:`h_touch_dragger<class_SplitContainer_theme_icon_h_touch_dragger>`                          |                         |
> +-----------------------------------+--------------------------------------------------------------------------------------------------+-------------------------+
> | :ref:`Texture2D<class_Texture2D>` | :ref:`touch_dragger<class_SplitContainer_theme_icon_touch_dragger>`                              |                         |
> +-----------------------------------+--------------------------------------------------------------------------------------------------+-------------------------+
> | :ref:`Texture2D<class_Texture2D>` | :ref:`v_grabber<class_SplitContainer_theme_icon_v_grabber>`                                      |                         |
> +-----------------------------------+--------------------------------------------------------------------------------------------------+-------------------------+
> | :ref:`Texture2D<class_Texture2D>` | :ref:`v_touch_dragger<class_SplitContainer_theme_icon_v_touch_dragger>`                          |                         |
> +-----------------------------------+--------------------------------------------------------------------------------------------------+-------------------------+
> | :ref:`StyleBox<class_StyleBox>`   | :ref:`split_bar_background<class_SplitContainer_theme_style_split_bar_background>`               |                         |
> +-----------------------------------+--------------------------------------------------------------------------------------------------+-------------------------+
>

----


## Signals



**drag_ended**\ (\ ) [🔗<class_SplitContainer_signal_drag_ended>]

Emitted when the user ends dragging.


----



**drag_started**\ (\ ) [🔗<class_SplitContainer_signal_drag_started>]

Emitted when the user starts dragging.


----



**dragged**\ (\ offset\: [int<class_int>]\ ) [🔗<class_SplitContainer_signal_dragged>]

Emitted when any dragger is dragged by user.


----


## Enumerations



enum **DraggerVisibility**: [🔗<enum_SplitContainer_DraggerVisibility>]



[DraggerVisibility<enum_SplitContainer_DraggerVisibility>] **DRAGGER_VISIBLE** = `0`

The split dragger icon is always visible when [autohide<class_SplitContainer_theme_constant_autohide>] is `false`, otherwise visible only when the cursor hovers it.

The size of the grabber icon determines the minimum [separation<class_SplitContainer_theme_constant_separation>].

The dragger icon is automatically hidden if the length of the grabber icon is longer than the split bar.



[DraggerVisibility<enum_SplitContainer_DraggerVisibility>] **DRAGGER_HIDDEN** = `1`

The split dragger icon is never visible regardless of the value of [autohide<class_SplitContainer_theme_constant_autohide>].

The size of the grabber icon determines the minimum [separation<class_SplitContainer_theme_constant_separation>].



[DraggerVisibility<enum_SplitContainer_DraggerVisibility>] **DRAGGER_HIDDEN_COLLAPSED** = `2`

The split dragger icon is not visible, and the split bar is collapsed to zero thickness.


----


## Property Descriptions



[bool<class_bool>] **collapsed** = `false` [🔗<class_SplitContainer_property_collapsed>]


- |void| **set_collapsed**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_collapsed**\ (\ )

If `true`, the draggers will be disabled and the children will be sized as if all [split_offsets<class_SplitContainer_property_split_offsets>] were `0`.


----



[bool<class_bool>] **drag_area_highlight_in_editor** = `false` [🔗<class_SplitContainer_property_drag_area_highlight_in_editor>]


- |void| **set_drag_area_highlight_in_editor**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_drag_area_highlight_in_editor_enabled**\ (\ )

Highlights the drag area [Rect2<class_Rect2>] so you can see where it is during development. The drag area is gold if [dragging_enabled<class_SplitContainer_property_dragging_enabled>] is `true`, and red if `false`.


----



[int<class_int>] **drag_area_margin_begin** = `0` [🔗<class_SplitContainer_property_drag_area_margin_begin>]


- |void| **set_drag_area_margin_begin**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_drag_area_margin_begin**\ (\ )

Reduces the size of the drag area and split bar [split_bar_background<class_SplitContainer_theme_style_split_bar_background>] at the beginning of the container.


----



[int<class_int>] **drag_area_margin_end** = `0` [🔗<class_SplitContainer_property_drag_area_margin_end>]


- |void| **set_drag_area_margin_end**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_drag_area_margin_end**\ (\ )

Reduces the size of the drag area and split bar [split_bar_background<class_SplitContainer_theme_style_split_bar_background>] at the end of the container.


----



[int<class_int>] **drag_area_offset** = `0` [🔗<class_SplitContainer_property_drag_area_offset>]


- |void| **set_drag_area_offset**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_drag_area_offset**\ (\ )

Shifts the drag area in the axis of the container to prevent the drag area from overlapping the [ScrollBar<class_ScrollBar>] or other selectable [Control<class_Control>] of a child node.


----



[DraggerVisibility<enum_SplitContainer_DraggerVisibility>] **dragger_visibility** = `0` [🔗<class_SplitContainer_property_dragger_visibility>]


- |void| **set_dragger_visibility**\ (\ value\: [DraggerVisibility<enum_SplitContainer_DraggerVisibility>]\ )
- [DraggerVisibility<enum_SplitContainer_DraggerVisibility>] **get_dragger_visibility**\ (\ )

Determines the dragger's visibility. This property does not determine whether dragging is enabled or not. Use [dragging_enabled<class_SplitContainer_property_dragging_enabled>] for that.


----



[bool<class_bool>] **dragging_enabled** = `true` [🔗<class_SplitContainer_property_dragging_enabled>]


- |void| **set_dragging_enabled**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_dragging_enabled**\ (\ )

Enables or disables split dragging.


----



[int<class_int>] **split_offset** = `0` [🔗<class_SplitContainer_property_split_offset>]


- |void| **set_split_offset**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_split_offset**\ (\ )

**Deprecated:** Use [split_offsets<class_SplitContainer_property_split_offsets>] instead. The first element of the array is the split offset between the first two children.

The first element of [split_offsets<class_SplitContainer_property_split_offsets>].


----



[PackedInt32Array<class_PackedInt32Array>] **split_offsets** = `PackedInt32Array(0)` [🔗<class_SplitContainer_property_split_offsets>]


- |void| **set_split_offsets**\ (\ value\: [PackedInt32Array<class_PackedInt32Array>]\ )
- [PackedInt32Array<class_PackedInt32Array>] **get_split_offsets**\ (\ )

Offsets for each dragger in pixels. Each one is the offset of the split between the [Control<class_Control>] nodes before and after the dragger, with `0` being the default position. The default position is based on the [Control<class_Control>] nodes expand flags and minimum sizes. See [Control.size_flags_horizontal<class_Control_property_size_flags_horizontal>], [Control.size_flags_vertical<class_Control_property_size_flags_vertical>], and [Control.size_flags_stretch_ratio<class_Control_property_size_flags_stretch_ratio>].

If none of the [Control<class_Control>] nodes before the dragger are expanded, the default position will be at the start of the **SplitContainer**. If none of the [Control<class_Control>] nodes after the dragger are expanded, the default position will be at the end of the **SplitContainer**. If the dragger is in between expanded [Control<class_Control>] nodes, the default position will be in the middle, based on the [Control.size_flags_stretch_ratio<class_Control_property_size_flags_stretch_ratio>]\ s and minimum sizes.

\ **Note:** If the split offsets cause [Control<class_Control>] nodes to overlap, the first split will take priority when resolving the positions.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedInt32Array<class_PackedInt32Array>] for more details.


----



[bool<class_bool>] **touch_dragger_enabled** = `false` [🔗<class_SplitContainer_property_touch_dragger_enabled>]


- |void| **set_touch_dragger_enabled**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_touch_dragger_enabled**\ (\ )

If `true`, a touch-friendly drag handle will be enabled for better usability on smaller screens. Unlike the standard grabber, this drag handle overlaps the **SplitContainer**'s children and does not affect their minimum separation. The standard grabber will no longer be drawn when this option is enabled.


----



[bool<class_bool>] **vertical** = `false` [🔗<class_SplitContainer_property_vertical>]


- |void| **set_vertical**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_vertical**\ (\ )

If `true`, the **SplitContainer** will arrange its children vertically, rather than horizontally.

Can't be changed when using [HSplitContainer<class_HSplitContainer>] and [VSplitContainer<class_VSplitContainer>].


----


## Method Descriptions



|void| **clamp_split_offset**\ (\ priority_index\: [int<class_int>] = 0\ ) [🔗<class_SplitContainer_method_clamp_split_offset>]

Clamps the [split_offsets<class_SplitContainer_property_split_offsets>] values to ensure they are within valid ranges and do not overlap with each other. When overlaps occur, this method prioritizes one split offset (at index `priority_index`) by clamping any overlapping split offsets to it.


----



[Control<class_Control>] **get_drag_area_control**\ (\ ) [🔗<class_SplitContainer_method_get_drag_area_control>]

**Deprecated:** Use the first element of [get_drag_area_controls()<class_SplitContainer_method_get_drag_area_controls>] instead.

Returns the drag area [Control<class_Control>]. For example, you can move a pre-configured button into the drag area [Control<class_Control>] so that it rides along with the split bar. Try setting the [Button<class_Button>] anchors to `center` prior to the `reparent()` call.

::

    $BarnacleButton.reparent($SplitContainer.get_drag_area_control())

\ **Note:** The drag area [Control<class_Control>] is drawn over the **SplitContainer**'s children, so [CanvasItem<class_CanvasItem>] draw objects called from the [Control<class_Control>] and children added to the [Control<class_Control>] will also appear over the **SplitContainer**'s children. Try setting [Control.mouse_filter<class_Control_property_mouse_filter>] of custom children to [Control.MOUSE_FILTER_IGNORE<class_Control_constant_MOUSE_FILTER_IGNORE>] to prevent blocking the mouse from dragging if desired.

\ **Warning:** This is a required internal node, removing and freeing it may cause a crash.


----



[Array<class_Array>]\[[Control<class_Control>]\] **get_drag_area_controls**\ (\ ) [🔗<class_SplitContainer_method_get_drag_area_controls>]

Returns an [Array<class_Array>] of the drag area [Control<class_Control>]\ s. These are the interactable [Control<class_Control>] nodes between each child. For example, this can be used to add a pre-configured button to a drag area [Control<class_Control>] so that it rides along with the split bar. Try setting the [Button<class_Button>] anchors to `center` prior to the [Node.reparent()<class_Node_method_reparent>] call.

::

    $BarnacleButton.reparent($SplitContainer.get_drag_area_controls()[0])

\ **Note:** The drag area [Control<class_Control>]\ s are drawn over the **SplitContainer**'s children, so [CanvasItem<class_CanvasItem>] draw objects called from a drag area and children added to it will also appear over the **SplitContainer**'s children. Try setting [Control.mouse_filter<class_Control_property_mouse_filter>] of custom children to [Control.MOUSE_FILTER_IGNORE<class_Control_constant_MOUSE_FILTER_IGNORE>] to prevent blocking the mouse from dragging if desired.

\ **Warning:** These are required internal nodes, removing or freeing them may cause a crash.


----


## Theme Property Descriptions



[Color<class_Color>] **touch_dragger_color** = `Color(1, 1, 1, 0.3)` [🔗<class_SplitContainer_theme_color_touch_dragger_color>]

The color of the touch dragger.


----



[Color<class_Color>] **touch_dragger_hover_color** = `Color(1, 1, 1, 0.6)` [🔗<class_SplitContainer_theme_color_touch_dragger_hover_color>]

The color of the touch dragger when hovered.


----



[Color<class_Color>] **touch_dragger_pressed_color** = `Color(1, 1, 1, 1)` [🔗<class_SplitContainer_theme_color_touch_dragger_pressed_color>]

The color of the touch dragger when pressed.


----



[int<class_int>] **autohide** = `1` [🔗<class_SplitContainer_theme_constant_autohide>]

Boolean value. If `1` (`true`), the grabbers will hide automatically when they aren't under the cursor. If `0` (`false`), the grabbers are always visible. The [dragger_visibility<class_SplitContainer_property_dragger_visibility>] must be [DRAGGER_VISIBLE<class_SplitContainer_constant_DRAGGER_VISIBLE>].


----



[int<class_int>] **minimum_grab_thickness** = `6` [🔗<class_SplitContainer_theme_constant_minimum_grab_thickness>]

The minimum thickness of the area users can click on to grab a split bar. This ensures that the split bar can still be dragged if [separation<class_SplitContainer_theme_constant_separation>] or [h_grabber<class_SplitContainer_theme_icon_h_grabber>] / [v_grabber<class_SplitContainer_theme_icon_v_grabber>]'s size is too narrow to easily select.


----



[int<class_int>] **separation** = `12` [🔗<class_SplitContainer_theme_constant_separation>]

The split bar thickness, i.e., the gap between each child of the container. This is overridden by the size of the grabber icon if [dragger_visibility<class_SplitContainer_property_dragger_visibility>] is set to [DRAGGER_VISIBLE<class_SplitContainer_constant_DRAGGER_VISIBLE>], or [DRAGGER_HIDDEN<class_SplitContainer_constant_DRAGGER_HIDDEN>], and [separation<class_SplitContainer_theme_constant_separation>] is smaller than the size of the grabber icon in the same axis.

\ **Note:** To obtain [separation<class_SplitContainer_theme_constant_separation>] values less than the size of the grabber icon, for example a `1 px` hairline, set [h_grabber<class_SplitContainer_theme_icon_h_grabber>] or [v_grabber<class_SplitContainer_theme_icon_v_grabber>] to a new [ImageTexture<class_ImageTexture>], which effectively sets the grabber icon size to `0 px`.


----



[Texture2D<class_Texture2D>] **grabber** [🔗<class_SplitContainer_theme_icon_grabber>]

The icon used for the grabbers drawn in the separations. This is only used in [HSplitContainer<class_HSplitContainer>] and [VSplitContainer<class_VSplitContainer>]. For **SplitContainer**, see [h_grabber<class_SplitContainer_theme_icon_h_grabber>] and [v_grabber<class_SplitContainer_theme_icon_v_grabber>] instead.


----



[Texture2D<class_Texture2D>] **h_grabber** [🔗<class_SplitContainer_theme_icon_h_grabber>]

The icon used for the grabbers drawn in the separations when [vertical<class_SplitContainer_property_vertical>] is `false`.


----



[Texture2D<class_Texture2D>] **h_touch_dragger** [🔗<class_SplitContainer_theme_icon_h_touch_dragger>]

The icon used for the drag handle when [touch_dragger_enabled<class_SplitContainer_property_touch_dragger_enabled>] is `true` and [vertical<class_SplitContainer_property_vertical>] is `false`.


----



[Texture2D<class_Texture2D>] **touch_dragger** [🔗<class_SplitContainer_theme_icon_touch_dragger>]

The icon used for the drag handle when [touch_dragger_enabled<class_SplitContainer_property_touch_dragger_enabled>] is `true`. This is only used in [HSplitContainer<class_HSplitContainer>] and [VSplitContainer<class_VSplitContainer>]. For **SplitContainer**, see [h_touch_dragger<class_SplitContainer_theme_icon_h_touch_dragger>] and [v_touch_dragger<class_SplitContainer_theme_icon_v_touch_dragger>] instead.


----



[Texture2D<class_Texture2D>] **v_grabber** [🔗<class_SplitContainer_theme_icon_v_grabber>]

The icon used for the grabbers drawn in the separations when [vertical<class_SplitContainer_property_vertical>] is `true`.


----



[Texture2D<class_Texture2D>] **v_touch_dragger** [🔗<class_SplitContainer_theme_icon_v_touch_dragger>]

The icon used for the drag handle when [touch_dragger_enabled<class_SplitContainer_property_touch_dragger_enabled>] is `true` and [vertical<class_SplitContainer_property_vertical>] is `true`.


----



[StyleBox<class_StyleBox>] **split_bar_background** [🔗<class_SplitContainer_theme_style_split_bar_background>]

Determines the background of the split bar if its thickness is greater than zero.

