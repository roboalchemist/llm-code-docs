# CanvasItem

# CanvasItem
Inherits:Node<Object
Inherited By:Control,Node2D
Abstract base class for everything in 2D space.

## Description
Abstract base class for everything in 2D space. Canvas items are laid out in a tree; children inherit and extend their parent's transform.CanvasItemis extended byControlfor GUI-related nodes, and byNode2Dfor 2D game objects.
AnyCanvasItemcan draw. For this,queue_redraw()is called by the engine, thenNOTIFICATION_DRAWwill be received on idle time to request a redraw. Because of this, canvas items don't need to be redrawn on every frame, improving the performance significantly. Several functions for drawing on theCanvasItemare provided (seedraw_*functions). However, they can only be used inside_draw(), its correspondingObject._notification()or methods connected to thedrawsignal.
Canvas items are drawn in tree order on their canvas layer. By default, children are on top of their parents, so a rootCanvasItemwill be drawn behind everything. This behavior can be changed on a per-item basis.
ACanvasItemcan be hidden, which will also hide its children. By adjusting various other properties of aCanvasItem, you can also modulate its color (viamodulateorself_modulate), change its Z-index, blend mode, and more.
Note that properties like transform, modulation, and visibility are only propagated todirectCanvasItemchild nodes. If there is a non-CanvasItemnode in between, likeNodeorAnimationPlayer, theCanvasItemnodes below will have an independent position andmodulatechain. See alsotop_level.

## Tutorials
- Viewport and canvas transforms
Viewport and canvas transforms
- Custom drawing in 2D
Custom drawing in 2D
- Audio Spectrum Visualizer Demo
Audio Spectrum Visualizer Demo

## Properties

| ClipChildrenMode | clip_children | 0 |
|---|---|---|
| int | light_mask | 1 |
| Material | material |  |
| Color | modulate | Color(1,1,1,1) |
| Color | self_modulate | Color(1,1,1,1) |
| bool | show_behind_parent | false |
| TextureFilter | texture_filter | 0 |
| TextureRepeat | texture_repeat | 0 |
| bool | top_level | false |
| bool | use_parent_material | false |
| int | visibility_layer | 1 |
| bool | visible | true |
| bool | y_sort_enabled | false |
| bool | z_as_relative | true |
| int | z_index | 0 |

ClipChildrenMode
clip_children
light_mask
Material
material
Color
modulate
Color(1,1,1,1)
Color
self_modulate
Color(1,1,1,1)
bool
show_behind_parent
false
TextureFilter
texture_filter
TextureRepeat
texture_repeat
bool
top_level
false
bool
use_parent_material
false
visibility_layer
bool
visible
true
bool
y_sort_enabled
false
bool
z_as_relative
true
z_index

## Methods

| void | _draw()virtual |
|---|---|
| void | draw_animation_slice(animation_length:float, slice_begin:float, slice_end:float, offset:float= 0.0) |
| void | draw_arc(center:Vector2, radius:float, start_angle:float, end_angle:float, point_count:int, color:Color, width:float= -1.0, antialiased:bool= false) |
| void | draw_char(font:Font, pos:Vector2, char:String, font_size:int= 16, modulate:Color= Color(1, 1, 1, 1), oversampling:float= 0.0)const |
| void | draw_char_outline(font:Font, pos:Vector2, char:String, font_size:int= 16, size:int= -1, modulate:Color= Color(1, 1, 1, 1), oversampling:float= 0.0)const |
| void | draw_circle(position:Vector2, radius:float, color:Color, filled:bool= true, width:float= -1.0, antialiased:bool= false) |
| void | draw_colored_polygon(points:PackedVector2Array, color:Color, uvs:PackedVector2Array= PackedVector2Array(), texture:Texture2D= null) |
| void | draw_dashed_line(from:Vector2, to:Vector2, color:Color, width:float= -1.0, dash:float= 2.0, aligned:bool= true, antialiased:bool= false) |
| void | draw_ellipse(position:Vector2, major:float, minor:float, color:Color, filled:bool= true, width:float= -1.0, antialiased:bool= false) |
| void | draw_ellipse_arc(center:Vector2, major:float, minor:float, start_angle:float, end_angle:float, point_count:int, color:Color, width:float= -1.0, antialiased:bool= false) |
| void | draw_end_animation() |
| void | draw_lcd_texture_rect_region(texture:Texture2D, rect:Rect2, src_rect:Rect2, modulate:Color= Color(1, 1, 1, 1)) |
| void | draw_line(from:Vector2, to:Vector2, color:Color, width:float= -1.0, antialiased:bool= false) |
| void | draw_mesh(mesh:Mesh, texture:Texture2D, transform:Transform2D= Transform2D(1, 0, 0, 1, 0, 0), modulate:Color= Color(1, 1, 1, 1)) |
| void | draw_msdf_texture_rect_region(texture:Texture2D, rect:Rect2, src_rect:Rect2, modulate:Color= Color(1, 1, 1, 1), outline:float= 0.0, pixel_range:float= 4.0, scale:float= 1.0) |
| void | draw_multiline(points:PackedVector2Array, color:Color, width:float= -1.0, antialiased:bool= false) |
| void | draw_multiline_colors(points:PackedVector2Array, colors:PackedColorArray, width:float= -1.0, antialiased:bool= false) |
| void | draw_multiline_string(font:Font, pos:Vector2, text:String, alignment:HorizontalAlignment= 0, width:float= -1, font_size:int= 16, max_lines:int= -1, modulate:Color= Color(1, 1, 1, 1), brk_flags:BitField[LineBreakFlag] = 3, justification_flags:BitField[JustificationFlag] = 3, direction:Direction= 0, orientation:Orientation= 0, oversampling:float= 0.0)const |
| void | draw_multiline_string_outline(font:Font, pos:Vector2, text:String, alignment:HorizontalAlignment= 0, width:float= -1, font_size:int= 16, max_lines:int= -1, size:int= 1, modulate:Color= Color(1, 1, 1, 1), brk_flags:BitField[LineBreakFlag] = 3, justification_flags:BitField[JustificationFlag] = 3, direction:Direction= 0, orientation:Orientation= 0, oversampling:float= 0.0)const |
| void | draw_multimesh(multimesh:MultiMesh, texture:Texture2D) |
| void | draw_polygon(points:PackedVector2Array, colors:PackedColorArray, uvs:PackedVector2Array= PackedVector2Array(), texture:Texture2D= null) |
| void | draw_polyline(points:PackedVector2Array, color:Color, width:float= -1.0, antialiased:bool= false) |
| void | draw_polyline_colors(points:PackedVector2Array, colors:PackedColorArray, width:float= -1.0, antialiased:bool= false) |
| void | draw_primitive(points:PackedVector2Array, colors:PackedColorArray, uvs:PackedVector2Array, texture:Texture2D= null) |
| void | draw_rect(rect:Rect2, color:Color, filled:bool= true, width:float= -1.0, antialiased:bool= false) |
| void | draw_set_transform(position:Vector2, rotation:float= 0.0, scale:Vector2= Vector2(1, 1)) |
| void | draw_set_transform_matrix(xform:Transform2D) |
| void | draw_string(font:Font, pos:Vector2, text:String, alignment:HorizontalAlignment= 0, width:float= -1, font_size:int= 16, modulate:Color= Color(1, 1, 1, 1), justification_flags:BitField[JustificationFlag] = 3, direction:Direction= 0, orientation:Orientation= 0, oversampling:float= 0.0)const |
| void | draw_string_outline(font:Font, pos:Vector2, text:String, alignment:HorizontalAlignment= 0, width:float= -1, font_size:int= 16, size:int= 1, modulate:Color= Color(1, 1, 1, 1), justification_flags:BitField[JustificationFlag] = 3, direction:Direction= 0, orientation:Orientation= 0, oversampling:float= 0.0)const |
| void | draw_style_box(style_box:StyleBox, rect:Rect2) |
| void | draw_texture(texture:Texture2D, position:Vector2, modulate:Color= Color(1, 1, 1, 1)) |
| void | draw_texture_rect(texture:Texture2D, rect:Rect2, tile:bool, modulate:Color= Color(1, 1, 1, 1), transpose:bool= false) |
| void | draw_texture_rect_region(texture:Texture2D, rect:Rect2, src_rect:Rect2, modulate:Color= Color(1, 1, 1, 1), transpose:bool= false, clip_uv:bool= true) |
| void | force_update_transform() |
| RID | get_canvas()const |
| RID | get_canvas_item()const |
| CanvasLayer | get_canvas_layer_node()const |
| Transform2D | get_canvas_transform()const |
| Vector2 | get_global_mouse_position()const |
| Transform2D | get_global_transform()const |
| Transform2D | get_global_transform_with_canvas()const |
| Variant | get_instance_shader_parameter(name:StringName)const |
| Vector2 | get_local_mouse_position()const |
| Transform2D | get_screen_transform()const |
| Transform2D | get_transform()const |
| Rect2 | get_viewport_rect()const |
| Transform2D | get_viewport_transform()const |
| bool | get_visibility_layer_bit(layer:int)const |
| World2D | get_world_2d()const |
| void | hide() |
| bool | is_local_transform_notification_enabled()const |
| bool | is_transform_notification_enabled()const |
| bool | is_visible_in_tree()const |
| Vector2 | make_canvas_position_local(viewport_point:Vector2)const |
| InputEvent | make_input_local(event:InputEvent)const |
| void | move_to_front() |
| void | queue_redraw() |
| void | set_instance_shader_parameter(name:StringName, value:Variant) |
| void | set_notify_local_transform(enable:bool) |
| void | set_notify_transform(enable:bool) |
| void | set_visibility_layer_bit(layer:int, enabled:bool) |
| void | show() |

void
_draw()virtual
void
draw_animation_slice(animation_length:float, slice_begin:float, slice_end:float, offset:float= 0.0)
void
draw_arc(center:Vector2, radius:float, start_angle:float, end_angle:float, point_count:int, color:Color, width:float= -1.0, antialiased:bool= false)
void
draw_char(font:Font, pos:Vector2, char:String, font_size:int= 16, modulate:Color= Color(1, 1, 1, 1), oversampling:float= 0.0)const
void
draw_char_outline(font:Font, pos:Vector2, char:String, font_size:int= 16, size:int= -1, modulate:Color= Color(1, 1, 1, 1), oversampling:float= 0.0)const
void
draw_circle(position:Vector2, radius:float, color:Color, filled:bool= true, width:float= -1.0, antialiased:bool= false)
void
draw_colored_polygon(points:PackedVector2Array, color:Color, uvs:PackedVector2Array= PackedVector2Array(), texture:Texture2D= null)
void
draw_dashed_line(from:Vector2, to:Vector2, color:Color, width:float= -1.0, dash:float= 2.0, aligned:bool= true, antialiased:bool= false)
void
draw_ellipse(position:Vector2, major:float, minor:float, color:Color, filled:bool= true, width:float= -1.0, antialiased:bool= false)
void
draw_ellipse_arc(center:Vector2, major:float, minor:float, start_angle:float, end_angle:float, point_count:int, color:Color, width:float= -1.0, antialiased:bool= false)
void
draw_end_animation()
void
draw_lcd_texture_rect_region(texture:Texture2D, rect:Rect2, src_rect:Rect2, modulate:Color= Color(1, 1, 1, 1))
void
draw_line(from:Vector2, to:Vector2, color:Color, width:float= -1.0, antialiased:bool= false)
void
draw_mesh(mesh:Mesh, texture:Texture2D, transform:Transform2D= Transform2D(1, 0, 0, 1, 0, 0), modulate:Color= Color(1, 1, 1, 1))
void
draw_msdf_texture_rect_region(texture:Texture2D, rect:Rect2, src_rect:Rect2, modulate:Color= Color(1, 1, 1, 1), outline:float= 0.0, pixel_range:float= 4.0, scale:float= 1.0)
void
draw_multiline(points:PackedVector2Array, color:Color, width:float= -1.0, antialiased:bool= false)
void
draw_multiline_colors(points:PackedVector2Array, colors:PackedColorArray, width:float= -1.0, antialiased:bool= false)
void
draw_multiline_string(font:Font, pos:Vector2, text:String, alignment:HorizontalAlignment= 0, width:float= -1, font_size:int= 16, max_lines:int= -1, modulate:Color= Color(1, 1, 1, 1), brk_flags:BitField[LineBreakFlag] = 3, justification_flags:BitField[JustificationFlag] = 3, direction:Direction= 0, orientation:Orientation= 0, oversampling:float= 0.0)const
void
draw_multiline_string_outline(font:Font, pos:Vector2, text:String, alignment:HorizontalAlignment= 0, width:float= -1, font_size:int= 16, max_lines:int= -1, size:int= 1, modulate:Color= Color(1, 1, 1, 1), brk_flags:BitField[LineBreakFlag] = 3, justification_flags:BitField[JustificationFlag] = 3, direction:Direction= 0, orientation:Orientation= 0, oversampling:float= 0.0)const
void
draw_multimesh(multimesh:MultiMesh, texture:Texture2D)
void
draw_polygon(points:PackedVector2Array, colors:PackedColorArray, uvs:PackedVector2Array= PackedVector2Array(), texture:Texture2D= null)
void
draw_polyline(points:PackedVector2Array, color:Color, width:float= -1.0, antialiased:bool= false)
void
draw_polyline_colors(points:PackedVector2Array, colors:PackedColorArray, width:float= -1.0, antialiased:bool= false)
void
draw_primitive(points:PackedVector2Array, colors:PackedColorArray, uvs:PackedVector2Array, texture:Texture2D= null)
void
draw_rect(rect:Rect2, color:Color, filled:bool= true, width:float= -1.0, antialiased:bool= false)
void
draw_set_transform(position:Vector2, rotation:float= 0.0, scale:Vector2= Vector2(1, 1))
void
draw_set_transform_matrix(xform:Transform2D)
void
draw_string(font:Font, pos:Vector2, text:String, alignment:HorizontalAlignment= 0, width:float= -1, font_size:int= 16, modulate:Color= Color(1, 1, 1, 1), justification_flags:BitField[JustificationFlag] = 3, direction:Direction= 0, orientation:Orientation= 0, oversampling:float= 0.0)const
void
draw_string_outline(font:Font, pos:Vector2, text:String, alignment:HorizontalAlignment= 0, width:float= -1, font_size:int= 16, size:int= 1, modulate:Color= Color(1, 1, 1, 1), justification_flags:BitField[JustificationFlag] = 3, direction:Direction= 0, orientation:Orientation= 0, oversampling:float= 0.0)const
void
draw_style_box(style_box:StyleBox, rect:Rect2)
void
draw_texture(texture:Texture2D, position:Vector2, modulate:Color= Color(1, 1, 1, 1))
void
draw_texture_rect(texture:Texture2D, rect:Rect2, tile:bool, modulate:Color= Color(1, 1, 1, 1), transpose:bool= false)
void
draw_texture_rect_region(texture:Texture2D, rect:Rect2, src_rect:Rect2, modulate:Color= Color(1, 1, 1, 1), transpose:bool= false, clip_uv:bool= true)
void
force_update_transform()
get_canvas()const
get_canvas_item()const
CanvasLayer
get_canvas_layer_node()const
Transform2D
get_canvas_transform()const
Vector2
get_global_mouse_position()const
Transform2D
get_global_transform()const
Transform2D
get_global_transform_with_canvas()const
Variant
get_instance_shader_parameter(name:StringName)const
Vector2
get_local_mouse_position()const
Transform2D
get_screen_transform()const
Transform2D
get_transform()const
Rect2
get_viewport_rect()const
Transform2D
get_viewport_transform()const
bool
get_visibility_layer_bit(layer:int)const
World2D
get_world_2d()const
void
hide()
bool
is_local_transform_notification_enabled()const
bool
is_transform_notification_enabled()const
bool
is_visible_in_tree()const
Vector2
make_canvas_position_local(viewport_point:Vector2)const
InputEvent
make_input_local(event:InputEvent)const
void
move_to_front()
void
queue_redraw()
void
set_instance_shader_parameter(name:StringName, value:Variant)
void
set_notify_local_transform(enable:bool)
void
set_notify_transform(enable:bool)
void
set_visibility_layer_bit(layer:int, enabled:bool)
void
show()

## Signals
draw()🔗
Emitted when theCanvasItemmust redraw,afterthe relatedNOTIFICATION_DRAWnotification, andbefore_draw()is called.
Note:Deferred connections do not allow drawing through thedraw_*methods.
hidden()🔗
Emitted when this node becomes hidden, i.e. it's no longer visible in the tree (seeis_visible_in_tree()).
item_rect_changed()🔗
Emitted when theCanvasItem's boundaries (position or size) change, or when an action took place that may have affected these boundaries (e.g. changingSprite2D.texture).
visibility_changed()🔗
Emitted when theCanvasItem's visibility changes, either because its ownvisibleproperty changed or because its visibility in the tree changed (seeis_visible_in_tree()).
This signal is emittedafterthe relatedNOTIFICATION_VISIBILITY_CHANGEDnotification.

## Enumerations
enumTextureFilter:🔗
TextureFilterTEXTURE_FILTER_PARENT_NODE=0
TheCanvasItemwill inherit the filter from its parent.
TextureFilterTEXTURE_FILTER_NEAREST=1
The texture filter reads from the nearest pixel only. This makes the texture look pixelated from up close, and grainy from a distance (due to mipmaps not being sampled).
TextureFilterTEXTURE_FILTER_LINEAR=2
The texture filter blends between the nearest 4 pixels. This makes the texture look smooth from up close, and grainy from a distance (due to mipmaps not being sampled).
TextureFilterTEXTURE_FILTER_NEAREST_WITH_MIPMAPS=3
The texture filter reads from the nearest pixel and blends between the nearest 2 mipmaps (or uses the nearest mipmap ifProjectSettings.rendering/textures/default_filters/use_nearest_mipmap_filteristrue). This makes the texture look pixelated from up close, and smooth from a distance.
Use this for non-pixel art textures that may be viewed at a low scale (e.g. due toCamera2Dzoom or sprite scaling), as mipmaps are important to smooth out pixels that are smaller than on-screen pixels.
TextureFilterTEXTURE_FILTER_LINEAR_WITH_MIPMAPS=4
The texture filter blends between the nearest 4 pixels and between the nearest 2 mipmaps (or uses the nearest mipmap ifProjectSettings.rendering/textures/default_filters/use_nearest_mipmap_filteristrue). This makes the texture look smooth from up close, and smooth from a distance.
Use this for non-pixel art textures that may be viewed at a low scale (e.g. due toCamera2Dzoom or sprite scaling), as mipmaps are important to smooth out pixels that are smaller than on-screen pixels.
TextureFilterTEXTURE_FILTER_NEAREST_WITH_MIPMAPS_ANISOTROPIC=5
The texture filter reads from the nearest pixel and blends between 2 mipmaps (or uses the nearest mipmap ifProjectSettings.rendering/textures/default_filters/use_nearest_mipmap_filteristrue) based on the angle between the surface and the camera view. This makes the texture look pixelated from up close, and smooth from a distance. Anisotropic filtering improves texture quality on surfaces that are almost in line with the camera, but is slightly slower. The anisotropic filtering level can be changed by adjustingProjectSettings.rendering/textures/default_filters/anisotropic_filtering_level.
Note:This texture filter is rarely useful in 2D projects.TEXTURE_FILTER_NEAREST_WITH_MIPMAPSis usually more appropriate in this case.
TextureFilterTEXTURE_FILTER_LINEAR_WITH_MIPMAPS_ANISOTROPIC=6
The texture filter blends between the nearest 4 pixels and blends between 2 mipmaps (or uses the nearest mipmap ifProjectSettings.rendering/textures/default_filters/use_nearest_mipmap_filteristrue) based on the angle between the surface and the camera view. This makes the texture look smooth from up close, and smooth from a distance. Anisotropic filtering improves texture quality on surfaces that are almost in line with the camera, but is slightly slower. The anisotropic filtering level can be changed by adjustingProjectSettings.rendering/textures/default_filters/anisotropic_filtering_level.
Note:This texture filter is rarely useful in 2D projects.TEXTURE_FILTER_LINEAR_WITH_MIPMAPSis usually more appropriate in this case.
TextureFilterTEXTURE_FILTER_MAX=7
Represents the size of theTextureFilterenum.
enumTextureRepeat:🔗
TextureRepeatTEXTURE_REPEAT_PARENT_NODE=0
TheCanvasItemwill inherit the filter from its parent.
TextureRepeatTEXTURE_REPEAT_DISABLED=1
The texture does not repeat. Sampling the texture outside its extents will result in "stretching" of the edge pixels. You can avoid this by ensuring a 1-pixel fully transparent border on each side of the texture.
TextureRepeatTEXTURE_REPEAT_ENABLED=2
The texture repeats when exceeding the texture's size.
TextureRepeatTEXTURE_REPEAT_MIRROR=3
The texture repeats when the exceeding the texture's size in a "2×2 tiled mode". Repeated textures at even positions are mirrored.
TextureRepeatTEXTURE_REPEAT_MAX=4
Represents the size of theTextureRepeatenum.
enumClipChildrenMode:🔗
ClipChildrenModeCLIP_CHILDREN_DISABLED=0
Children are drawn over this node and are not clipped.
ClipChildrenModeCLIP_CHILDREN_ONLY=1
This node is used as a mask and isnotdrawn. The mask is based on this node's alpha channel: Opaque pixels are kept, transparent pixels are discarded, and semi-transparent pixels are blended in according to their opacity. Children are clipped to this node's drawn area.
ClipChildrenModeCLIP_CHILDREN_AND_DRAW=2
This node is used as a mask and is also drawn. The mask is based on this node's alpha channel: Opaque pixels are kept, transparent pixels are discarded, and semi-transparent pixels are blended in according to their opacity. Children are clipped to the parent's drawn area.
ClipChildrenModeCLIP_CHILDREN_MAX=3
Represents the size of theClipChildrenModeenum.

## Constants
NOTIFICATION_TRANSFORM_CHANGED=2000🔗
Notification received when this node's global transform changes, ifis_transform_notification_enabled()istrue. See alsoset_notify_transform()andget_transform().
Note:Many canvas items such asCamera2DorCollisionObject2Dautomatically enable this in order to function correctly.
NOTIFICATION_LOCAL_TRANSFORM_CHANGED=35🔗
Notification received when this node's transform changes, ifis_local_transform_notification_enabled()istrue. This is not received when a parentNode2D's transform changes. See alsoset_notify_local_transform().
Note:Many canvas items such asCamera2DorCollisionShape2Dautomatically enable this in order to function correctly.
NOTIFICATION_DRAW=30🔗
TheCanvasItemis requested to draw (see_draw()).
NOTIFICATION_VISIBILITY_CHANGED=31🔗
Notification received when this node's visibility changes (seevisibleandis_visible_in_tree()).
This notification is receivedbeforethe relatedvisibility_changedsignal.
NOTIFICATION_ENTER_CANVAS=32🔗
TheCanvasItemhas entered the canvas.
NOTIFICATION_EXIT_CANVAS=33🔗
TheCanvasItemhas exited the canvas.
This notification is sent in reversed order.
NOTIFICATION_WORLD_2D_CHANGED=36🔗
Notification received when thisCanvasItemis registered to a newWorld2D(seeget_world_2d()).

## Property Descriptions
ClipChildrenModeclip_children=0🔗
- voidset_clip_children_mode(value:ClipChildrenMode)
voidset_clip_children_mode(value:ClipChildrenMode)
- ClipChildrenModeget_clip_children_mode()
ClipChildrenModeget_clip_children_mode()
The mode in which this node clips its children, acting as a mask.
Note:Clipping nodes cannot be nested or placed within aCanvasGroup. If an ancestor of this node clips its children or is aCanvasGroup, then this node's clip mode should be set toCLIP_CHILDREN_DISABLEDto avoid unexpected behavior.
intlight_mask=1🔗
- voidset_light_mask(value:int)
voidset_light_mask(value:int)
- intget_light_mask()
intget_light_mask()
The rendering layers in which thisCanvasItemresponds toLight2Dnodes.
Materialmaterial🔗
- voidset_material(value:Material)
voidset_material(value:Material)
- Materialget_material()
Materialget_material()
The material applied to thisCanvasItem.
Colormodulate=Color(1,1,1,1)🔗
- voidset_modulate(value:Color)
voidset_modulate(value:Color)
- Colorget_modulate()
Colorget_modulate()
The color applied to thisCanvasItem. This property does affect childCanvasItems, unlikeself_modulatewhich only affects the node itself.
Colorself_modulate=Color(1,1,1,1)🔗
- voidset_self_modulate(value:Color)
voidset_self_modulate(value:Color)
- Colorget_self_modulate()
Colorget_self_modulate()
The color applied to thisCanvasItem. This property doesnotaffect childCanvasItems, unlikemodulatewhich affects both the node itself and its children.
Note:Internal children are also not affected by this property (see theinclude_internalparameter inNode.add_child()). For built-in nodes this includes sliders inColorPicker, and the tab bar inTabContainer.
boolshow_behind_parent=false🔗
- voidset_draw_behind_parent(value:bool)
voidset_draw_behind_parent(value:bool)
- boolis_draw_behind_parent_enabled()
boolis_draw_behind_parent_enabled()
Iftrue, this node draws behind its parent.
TextureFiltertexture_filter=0🔗
- voidset_texture_filter(value:TextureFilter)
voidset_texture_filter(value:TextureFilter)
- TextureFilterget_texture_filter()
TextureFilterget_texture_filter()
The filtering mode used to render thisCanvasItem's texture(s).
TextureRepeattexture_repeat=0🔗
- voidset_texture_repeat(value:TextureRepeat)
voidset_texture_repeat(value:TextureRepeat)
- TextureRepeatget_texture_repeat()
TextureRepeatget_texture_repeat()
The repeating mode used to render thisCanvasItem's texture(s). It affects what happens when the texture is sampled outside its extents, for example by setting aSprite2D.region_rectthat is larger than the texture or assigningPolygon2DUV points outside the texture.
Note:TextureRectis not affected bytexture_repeat, as it uses its own texture repeating implementation.
booltop_level=false🔗
- voidset_as_top_level(value:bool)
voidset_as_top_level(value:bool)
- boolis_set_as_top_level()
boolis_set_as_top_level()
Iftrue, thisCanvasItemwillnotinherit its transform from parentCanvasItems. Its draw order will also be changed to make it draw on top of otherCanvasItems that do not havetop_levelset totrue. TheCanvasItemwill effectively act as if it was placed as a child of a bareNode.
booluse_parent_material=false🔗
- voidset_use_parent_material(value:bool)
voidset_use_parent_material(value:bool)
- boolget_use_parent_material()
boolget_use_parent_material()
Iftrue, the parentCanvasItem'smaterialis used as this node's material.
intvisibility_layer=1🔗
- voidset_visibility_layer(value:int)
voidset_visibility_layer(value:int)
- intget_visibility_layer()
intget_visibility_layer()
The rendering layer in which thisCanvasItemis rendered byViewportnodes. AViewportwill render aCanvasItemif it and all its parents share a layer with theViewport's canvas cull mask.
Note:ACanvasItemdoes not inherit its parents' visibility layers. This means that if a parentCanvasItemdoes not have all the same layers as its child, the child may not be visible even if both the parent and child havevisibleset totrue. For example, if a parent has layer 1 and a child has layer 2, the child will not be visible in aViewportwith the canvas cull mask set to layer 1 or 2 (seeViewport.canvas_cull_mask). To ensure that both the parent and child are visible, the parent must have both layers 1 and 2, or the child must havetop_levelset totrue.
boolvisible=true🔗
- voidset_visible(value:bool)
voidset_visible(value:bool)
- boolis_visible()
boolis_visible()
Iftrue, thisCanvasItemmay be drawn. Whether thisCanvasItemis actually drawn depends on the visibility of all of itsCanvasItemancestors. In other words: thisCanvasItemwill be drawn whenis_visible_in_tree()returnstrueand allCanvasItemancestors share at least onevisibility_layerwith thisCanvasItem.
Note:For controls that inheritPopup, the correct way to make them visible is to call one of the multiplepopup*()functions instead.
booly_sort_enabled=false🔗
- voidset_y_sort_enabled(value:bool)
voidset_y_sort_enabled(value:bool)
- boolis_y_sort_enabled()
boolis_y_sort_enabled()
Iftrue, this and childCanvasItemnodes with a higher Y position are rendered in front of nodes with a lower Y position. Iffalse, this and childCanvasItemnodes are rendered normally in scene tree order.
With Y-sorting enabled on a parent node ('A') but disabled on a child node ('B'), the child node ('B') is sorted but its children ('C1', 'C2', etc.) render together on the same Y position as the child node ('B'). This allows you to organize the render order of a scene without changing the scene tree.
Nodes sort relative to each other only if they are on the samez_index.
boolz_as_relative=true🔗
- voidset_z_as_relative(value:bool)
voidset_z_as_relative(value:bool)
- boolis_z_relative()
boolis_z_relative()
Iftrue, this node's final Z index is relative to its parent's Z index.
For example, ifz_indexis2and its parent's final Z index is3, then this node's final Z index will be5(2+3).
intz_index=0🔗
- voidset_z_index(value:int)
voidset_z_index(value:int)
- intget_z_index()
intget_z_index()
The order in which this node is drawn. A node with a higher Z index will display in front of others. Must be betweenRenderingServer.CANVAS_ITEM_Z_MINandRenderingServer.CANVAS_ITEM_Z_MAX(inclusive).
Note:The Z index doesnotaffect the order in whichCanvasItemnodes are processed or the way input events are handled. This is especially important to keep in mind forControlnodes.

## Method Descriptions
void_draw()virtual🔗
Called whenCanvasItemhas been requested to redraw (afterqueue_redraw()is called, either manually or by the engine).
Corresponds to theNOTIFICATION_DRAWnotification inObject._notification().
voiddraw_animation_slice(animation_length:float, slice_begin:float, slice_end:float, offset:float= 0.0)🔗
Subsequent drawing commands will be ignored unless they fall within the specified animation slice. This is a faster way to implement animations that loop on background rather than redrawing constantly.
voiddraw_arc(center:Vector2, radius:float, start_angle:float, end_angle:float, point_count:int, color:Color, width:float= -1.0, antialiased:bool= false)🔗
Draws an unfilled arc between the given angles with a uniformcolorandwidthand optional antialiasing (supported only for positivewidth). The larger the value ofpoint_count, the smoother the curve.centeris defined in local space. For elliptical arcs, seedraw_ellipse_arc(). See alsodraw_circle().
Ifwidthis negative, it will be ignored and the arc will be drawn usingRenderingServer.PRIMITIVE_LINE_STRIP. This means that when the CanvasItem is scaled, the arc will remain thin. If this behavior is not desired, then pass a positivewidthlike1.0.
The arc is drawn fromstart_angletowards the value ofend_angleso in clockwise direction ifstart_angle<end_angleand counter-clockwise otherwise. Passing the same angles but in reversed order will produce the same arc. If absolute difference ofstart_angleandend_angleis greater than@GDScript.TAUradians, then a full circle arc is drawn (i.e. arc will not overlap itself).
voiddraw_char(font:Font, pos:Vector2, char:String, font_size:int= 16, modulate:Color= Color(1, 1, 1, 1), oversampling:float= 0.0)const🔗
Draws a string first character using a custom font. Ifoversamplingis greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.posis defined in local space.
voiddraw_char_outline(font:Font, pos:Vector2, char:String, font_size:int= 16, size:int= -1, modulate:Color= Color(1, 1, 1, 1), oversampling:float= 0.0)const🔗
Draws a string first character outline using a custom font. Ifoversamplingis greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.posis defined in local space.
voiddraw_circle(position:Vector2, radius:float, color:Color, filled:bool= true, width:float= -1.0, antialiased:bool= false)🔗
Draws a circle, withpositiondefined in local space. See alsodraw_ellipse(),draw_arc(),draw_polyline(), anddraw_polygon().
Iffilledistrue, the circle will be filled with thecolorspecified. Iffilledisfalse, the circle will be drawn as a stroke with thecolorandwidthspecified.
Ifwidthis negative, then two-point primitives will be drawn instead of a four-point ones. This means that when the CanvasItem is scaled, the lines will remain thin. If this behavior is not desired, then pass a positivewidthlike1.0.
Ifantialiasedistrue, half transparent "feathers" will be attached to the boundary, making outlines smooth.
Note:widthis only effective iffilledisfalse.
voiddraw_colored_polygon(points:PackedVector2Array, color:Color, uvs:PackedVector2Array= PackedVector2Array(), texture:Texture2D= null)🔗
Draws a colored polygon of any number of points, convex or concave. The points in thepointsarray are defined in local space. Unlikedraw_polygon(), a single color must be specified for the whole polygon.
Note:If you frequently redraw the same polygon with a large number of vertices, consider pre-calculating the triangulation withGeometry2D.triangulate_polygon()and usingdraw_mesh(),draw_multimesh(), orRenderingServer.canvas_item_add_triangle_array().
Note:Styleboxes, textures, and meshes stored only inside local variables shouldnotbe used with this method in GDScript, because the drawing operation doesn't begin immediately once this method is called. In GDScript, when the function with the local variables ends, the local variables get destroyed before the rendering takes place.
voiddraw_dashed_line(from:Vector2, to:Vector2, color:Color, width:float= -1.0, dash:float= 2.0, aligned:bool= true, antialiased:bool= false)🔗
Draws a dashed line from a 2D point to another, with a given color and width. Thefromandtopositions are defined in local space. See alsodraw_line(),draw_multiline(), anddraw_polyline().
Ifwidthis negative, then a two-point primitives will be drawn instead of a four-point ones. This means that when the CanvasItem is scaled, the line parts will remain thin. If this behavior is not desired, then pass a positivewidthlike1.0.
dashis the length of each dash in pixels, with the gap between each dash being the same length. Ifalignedistrue, the length of the first and last dashes may be shortened or lengthened to allow the line to begin and end at the precise points defined byfromandto. Both ends are always symmetrical whenalignedistrue. Ifalignedisfalse, all dashes will have the same length, but the line may appear incomplete at the end due to the dash length not dividing evenly into the line length. Only full dashes are drawn whenalignedisfalse.
Ifantialiasedistrue, half transparent "feathers" will be attached to the boundary, making outlines smooth.
Note:antialiasedis only effective ifwidthis greater than0.0.
voiddraw_ellipse(position:Vector2, major:float, minor:float, color:Color, filled:bool= true, width:float= -1.0, antialiased:bool= false)🔗
Draws an ellipse with semi-major axismajorand semi-minor axisminor. See alsodraw_circle(),draw_ellipse_arc(),draw_polyline(), anddraw_polygon().
Iffilledistrue, the ellipse will be filled with thecolorspecified. Iffilledisfalse, the ellipse will be drawn as a stroke with thecolorandwidthspecified.
Ifwidthis negative, then two-point primitives will be drawn instead of four-point ones. This means that when the CanvasItem is scaled, the lines will remain thin. If this behavior is not desired, then pass a positivewidthlike1.0.
Ifantialiasedistrue, half transparent "feathers" will be attached to the boundary, making outlines smooth.
Note:widthis only effective iffilledisfalse.
voiddraw_ellipse_arc(center:Vector2, major:float, minor:float, start_angle:float, end_angle:float, point_count:int, color:Color, width:float= -1.0, antialiased:bool= false)🔗
Draws an unfilled elliptical arc between the given angles with a uniformcolorandwidthand optional antialiasing (supported only for positivewidth). The larger the value ofpoint_count, the smoother the curve. For circular arcs, seedraw_arc(). See alsodraw_ellipse().
Ifwidthis negative, it will be ignored and the arc will be drawn usingRenderingServer.PRIMITIVE_LINE_STRIP. This means that when the CanvasItem is scaled, the arc will remain thin. If this behavior is not desired, then pass a positivewidthlike1.0.
The arc is drawn fromstart_angletowards the value ofend_angleso in clockwise direction ifstart_angle<end_angleand counter-clockwise otherwise. Passing the same angles but in reversed order will produce the same arc. If absolute difference ofstart_angleandend_angleis greater than@GDScript.TAUradians, then a full ellipse is drawn (i.e. arc will not overlap itself).
voiddraw_end_animation()🔗
After submitting all animations slices viadraw_animation_slice(), this function can be used to revert drawing to its default state (all subsequent drawing commands will be visible). If you don't care about this particular use case, usage of this function after submitting the slices is not required.
voiddraw_lcd_texture_rect_region(texture:Texture2D, rect:Rect2, src_rect:Rect2, modulate:Color= Color(1, 1, 1, 1))🔗
Draws a textured rectangle region of the font texture with LCD subpixel anti-aliasing at a given position, optionally modulated by a color. Therectis defined in local space.
Texture is drawn using the following blend operation, blend mode of theCanvasItemMaterialis ignored:
```
dst.r = texture.r * modulate.r * modulate.a + dst.r * (1.0 - texture.r * modulate.a);
dst.g = texture.g * modulate.g * modulate.a + dst.g * (1.0 - texture.g * modulate.a);
dst.b = texture.b * modulate.b * modulate.a + dst.b * (1.0 - texture.b * modulate.a);
dst.a = modulate.a + dst.a * (1.0 - modulate.a);
```
Note:Styleboxes, textures, and meshes stored only inside local variables shouldnotbe used with this method in GDScript, because the drawing operation doesn't begin immediately once this method is called. In GDScript, when the function with the local variables ends, the local variables get destroyed before the rendering takes place.
voiddraw_line(from:Vector2, to:Vector2, color:Color, width:float= -1.0, antialiased:bool= false)🔗
Draws a line from a 2D point to another, with a given color and width. It can be optionally antialiased. Thefromandtopositions are defined in local space. See alsodraw_dashed_line(),draw_multiline(), anddraw_polyline().
Ifwidthis negative, then a two-point primitive will be drawn instead of a four-point one. This means that when the CanvasItem is scaled, the line will remain thin. If this behavior is not desired, then pass a positivewidthlike1.0.
voiddraw_mesh(mesh:Mesh, texture:Texture2D, transform:Transform2D= Transform2D(1, 0, 0, 1, 0, 0), modulate:Color= Color(1, 1, 1, 1))🔗
Draws aMeshin 2D, using the provided texture. SeeMeshInstance2Dfor related documentation. Thetransformis defined in local space.
Note:Styleboxes, textures, and meshes stored only inside local variables shouldnotbe used with this method in GDScript, because the drawing operation doesn't begin immediately once this method is called. In GDScript, when the function with the local variables ends, the local variables get destroyed before the rendering takes place.
voiddraw_msdf_texture_rect_region(texture:Texture2D, rect:Rect2, src_rect:Rect2, modulate:Color= Color(1, 1, 1, 1), outline:float= 0.0, pixel_range:float= 4.0, scale:float= 1.0)🔗
Draws a textured rectangle region of the multichannel signed distance field texture at a given position, optionally modulated by a color. Therectis defined in local space. SeeFontFile.multichannel_signed_distance_fieldfor more information and caveats about MSDF font rendering.
Ifoutlineis positive, each alpha channel value of pixel in region is set to maximum value of true distance in theoutlineradius.
Value of thepixel_rangeshould the same that was used during distance field texture generation.
Note:Styleboxes, textures, and meshes stored only inside local variables shouldnotbe used with this method in GDScript, because the drawing operation doesn't begin immediately once this method is called. In GDScript, when the function with the local variables ends, the local variables get destroyed before the rendering takes place.
voiddraw_multiline(points:PackedVector2Array, color:Color, width:float= -1.0, antialiased:bool= false)🔗
Draws multiple disconnected lines with a uniformwidthandcolor. Each line is defined by two consecutive points frompointsarray in local space, i.e. i-th segment consists ofpoints[2*i],points[2*i+1]endpoints. When drawing large amounts of lines, this is faster than using individualdraw_line()calls. To draw interconnected lines, usedraw_polyline()instead.
Ifwidthis negative, then two-point primitives will be drawn instead of a four-point ones. This means that when the CanvasItem is scaled, the lines will remain thin. If this behavior is not desired, then pass a positivewidthlike1.0.
Note:antialiasedis only effective ifwidthis greater than0.0.
voiddraw_multiline_colors(points:PackedVector2Array, colors:PackedColorArray, width:float= -1.0, antialiased:bool= false)🔗
Draws multiple disconnected lines with a uniformwidthand segment-by-segment coloring. Each segment is defined by two consecutive points frompointsarray in local space and a corresponding color fromcolorsarray, i.e. i-th segment consists ofpoints[2*i],points[2*i+1]endpoints and hascolors[i]color. When drawing large amounts of lines, this is faster than using individualdraw_line()calls. To draw interconnected lines, usedraw_polyline_colors()instead.
Ifwidthis negative, then two-point primitives will be drawn instead of a four-point ones. This means that when the CanvasItem is scaled, the lines will remain thin. If this behavior is not desired, then pass a positivewidthlike1.0.
Note:antialiasedis only effective ifwidthis greater than0.0.
voiddraw_multiline_string(font:Font, pos:Vector2, text:String, alignment:HorizontalAlignment= 0, width:float= -1, font_size:int= 16, max_lines:int= -1, modulate:Color= Color(1, 1, 1, 1), brk_flags:BitField[LineBreakFlag] = 3, justification_flags:BitField[JustificationFlag] = 3, direction:Direction= 0, orientation:Orientation= 0, oversampling:float= 0.0)const🔗
Breakstextinto lines and draws it using the specifiedfontat theposin local space (top-left corner). The text will have its color multiplied bymodulate. Ifwidthis greater than or equal to 0, the text will be clipped if it exceeds the specified width. Ifoversamplingis greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.
voiddraw_multiline_string_outline(font:Font, pos:Vector2, text:String, alignment:HorizontalAlignment= 0, width:float= -1, font_size:int= 16, max_lines:int= -1, size:int= 1, modulate:Color= Color(1, 1, 1, 1), brk_flags:BitField[LineBreakFlag] = 3, justification_flags:BitField[JustificationFlag] = 3, direction:Direction= 0, orientation:Orientation= 0, oversampling:float= 0.0)const🔗
Breakstextto the lines and draws text outline using the specifiedfontat theposin local space (top-left corner). The text will have its color multiplied bymodulate. Ifwidthis greater than or equal to 0, the text will be clipped if it exceeds the specified width. Ifoversamplingis greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.
voiddraw_multimesh(multimesh:MultiMesh, texture:Texture2D)🔗
Draws aMultiMeshin 2D with the provided texture. SeeMultiMeshInstance2Dfor related documentation.
Note:Styleboxes, textures, and meshes stored only inside local variables shouldnotbe used with this method in GDScript, because the drawing operation doesn't begin immediately once this method is called. In GDScript, when the function with the local variables ends, the local variables get destroyed before the rendering takes place.
voiddraw_polygon(points:PackedVector2Array, colors:PackedColorArray, uvs:PackedVector2Array= PackedVector2Array(), texture:Texture2D= null)🔗
Draws a solid polygon of any number of points, convex or concave. Unlikedraw_colored_polygon(), each point's color can be changed individually. Thepointsarray is defined in local space. See alsodraw_polyline()anddraw_polyline_colors(). If you need more flexibility (such as being able to use bones), useRenderingServer.canvas_item_add_triangle_array()instead.
Note:If you frequently redraw the same polygon with a large number of vertices, consider pre-calculating the triangulation withGeometry2D.triangulate_polygon()and usingdraw_mesh(),draw_multimesh(), orRenderingServer.canvas_item_add_triangle_array().
Note:Styleboxes, textures, and meshes stored only inside local variables shouldnotbe used with this method in GDScript, because the drawing operation doesn't begin immediately once this method is called. In GDScript, when the function with the local variables ends, the local variables get destroyed before the rendering takes place.
voiddraw_polyline(points:PackedVector2Array, color:Color, width:float= -1.0, antialiased:bool= false)🔗
Draws interconnected line segments with a uniformcolorandwidthand optional antialiasing (supported only for positivewidth). Thepointsarray is defined in local space. When drawing large amounts of lines, this is faster than using individualdraw_line()calls. To draw disconnected lines, usedraw_multiline()instead. See alsodraw_polygon().
Ifwidthis negative, it will be ignored and the polyline will be drawn usingRenderingServer.PRIMITIVE_LINE_STRIP. This means that when the CanvasItem is scaled, the polyline will remain thin. If this behavior is not desired, then pass a positivewidthlike1.0.
voiddraw_polyline_colors(points:PackedVector2Array, colors:PackedColorArray, width:float= -1.0, antialiased:bool= false)🔗
Draws interconnected line segments with a uniformwidth, point-by-point coloring, and optional antialiasing (supported only for positivewidth). Colors assigned to line points match by index betweenpointsandcolors, i.e. each line segment is filled with a gradient between the colors of the endpoints. Thepointsarray is defined in local space. When drawing large amounts of lines, this is faster than using individualdraw_line()calls. To draw disconnected lines, usedraw_multiline_colors()instead. See alsodraw_polygon().
Ifwidthis negative, it will be ignored and the polyline will be drawn usingRenderingServer.PRIMITIVE_LINE_STRIP. This means that when the CanvasItem is scaled, the polyline will remain thin. If this behavior is not desired, then pass a positivewidthlike1.0.
voiddraw_primitive(points:PackedVector2Array, colors:PackedColorArray, uvs:PackedVector2Array, texture:Texture2D= null)🔗
Draws a custom primitive. 1 point for a point, 2 points for a line, 3 points for a triangle, and 4 points for a quad. If 0 points or more than 4 points are specified, nothing will be drawn and an error message will be printed. Thepointsarray is defined in local space. See alsodraw_line(),draw_polyline(),draw_polygon(), anddraw_rect().
Note:Styleboxes, textures, and meshes stored only inside local variables shouldnotbe used with this method in GDScript, because the drawing operation doesn't begin immediately once this method is called. In GDScript, when the function with the local variables ends, the local variables get destroyed before the rendering takes place.
voiddraw_rect(rect:Rect2, color:Color, filled:bool= true, width:float= -1.0, antialiased:bool= false)🔗
Draws a rectangle. Iffilledistrue, the rectangle will be filled with thecolorspecified. Iffilledisfalse, the rectangle will be drawn as a stroke with thecolorandwidthspecified. Therectis specified in local space. See alsodraw_texture_rect().
Ifwidthis negative, then two-point primitives will be drawn instead of a four-point ones. This means that when the CanvasItem is scaled, the lines will remain thin. If this behavior is not desired, then pass a positivewidthlike1.0.
Ifantialiasedistrue, half transparent "feathers" will be attached to the boundary, making outlines smooth.
Note:widthis only effective iffilledisfalse.
Note:Unfilled rectangles drawn with a negativewidthmay not display perfectly. For example, corners may be missing or brighter due to overlapping lines (for a translucentcolor).
voiddraw_set_transform(position:Vector2, rotation:float= 0.0, scale:Vector2= Vector2(1, 1))🔗
Sets a custom local transform for drawing via components. Anything drawn afterwards will be transformed by this.
Note:FontFile.oversamplingdoesnottakescaleinto account. This means that scaling up/down will cause bitmap fonts and rasterized (non-MSDF) dynamic fonts to appear blurry or pixelated. To ensure text remains crisp regardless of scale, you can enable MSDF font rendering by enablingProjectSettings.gui/theme/default_font_multichannel_signed_distance_field(applies to the default project font only), or enablingMultichannel Signed Distance Fieldin the import options of a DynamicFont for custom fonts. On system fonts,SystemFont.multichannel_signed_distance_fieldcan be enabled in the inspector.
voiddraw_set_transform_matrix(xform:Transform2D)🔗
Sets a custom local transform for drawing via matrix. Anything drawn afterwards will be transformed by this.
voiddraw_string(font:Font, pos:Vector2, text:String, alignment:HorizontalAlignment= 0, width:float= -1, font_size:int= 16, modulate:Color= Color(1, 1, 1, 1), justification_flags:BitField[JustificationFlag] = 3, direction:Direction= 0, orientation:Orientation= 0, oversampling:float= 0.0)const🔗
Drawstextusing the specifiedfontat theposin local space (bottom-left corner using the baseline of the font). The text will have its color multiplied bymodulate. Ifwidthis greater than or equal to 0, the text will be clipped if it exceeds the specified width. Ifoversamplingis greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.
Example:Draw "Hello world", using the project's default font:
```
draw_string(ThemeDB.fallback_font, Vector2(64, 64), "Hello world", HORIZONTAL_ALIGNMENT_LEFT, -1, ThemeDB.fallback_font_size)
```
```
DrawString(ThemeDB.FallbackFont, new Vector2(64, 64), "Hello world", HorizontalAlignment.Left, -1, ThemeDB.FallbackFontSize);
```
See alsoFont.draw_string().
voiddraw_string_outline(font:Font, pos:Vector2, text:String, alignment:HorizontalAlignment= 0, width:float= -1, font_size:int= 16, size:int= 1, modulate:Color= Color(1, 1, 1, 1), justification_flags:BitField[JustificationFlag] = 3, direction:Direction= 0, orientation:Orientation= 0, oversampling:float= 0.0)const🔗
Drawstextoutline using the specifiedfontat theposin local space (bottom-left corner using the baseline of the font). The text will have its color multiplied bymodulate. Ifwidthis greater than or equal to 0, the text will be clipped if it exceeds the specified width. Ifoversamplingis greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.
voiddraw_style_box(style_box:StyleBox, rect:Rect2)🔗
Draws a styled rectangle. Therectis defined in local space.
Note:Styleboxes, textures, and meshes stored only inside local variables shouldnotbe used with this method in GDScript, because the drawing operation doesn't begin immediately once this method is called. In GDScript, when the function with the local variables ends, the local variables get destroyed before the rendering takes place.
voiddraw_texture(texture:Texture2D, position:Vector2, modulate:Color= Color(1, 1, 1, 1))🔗
Draws a texture at a given position. Thepositionis defined in local space.
Note:Styleboxes, textures, and meshes stored only inside local variables shouldnotbe used with this method in GDScript, because the drawing operation doesn't begin immediately once this method is called. In GDScript, when the function with the local variables ends, the local variables get destroyed before the rendering takes place.
voiddraw_texture_rect(texture:Texture2D, rect:Rect2, tile:bool, modulate:Color= Color(1, 1, 1, 1), transpose:bool= false)🔗
Draws a textured rectangle at a given position, optionally modulated by a color. Therectis defined in local space. Iftransposeistrue, the texture will have its X and Y coordinates swapped. See alsodraw_rect()anddraw_texture_rect_region().
Note:Styleboxes, textures, and meshes stored only inside local variables shouldnotbe used with this method in GDScript, because the drawing operation doesn't begin immediately once this method is called. In GDScript, when the function with the local variables ends, the local variables get destroyed before the rendering takes place.
voiddraw_texture_rect_region(texture:Texture2D, rect:Rect2, src_rect:Rect2, modulate:Color= Color(1, 1, 1, 1), transpose:bool= false, clip_uv:bool= true)🔗
Draws a textured rectangle from a texture's region (specified bysrc_rect) at a given position in local space, optionally modulated by a color. Iftransposeistrue, the texture will have its X and Y coordinates swapped. See alsodraw_texture_rect().
Note:Styleboxes, textures, and meshes stored only inside local variables shouldnotbe used with this method in GDScript, because the drawing operation doesn't begin immediately once this method is called. In GDScript, when the function with the local variables ends, the local variables get destroyed before the rendering takes place.
voidforce_update_transform()🔗
Forces the node's transform to update. Fails if the node is not inside the tree. See alsoget_transform().
Note:For performance reasons, transform changes are usually accumulated and appliedonceat the end of the frame. The update propagates throughCanvasItemchildren, as well. Therefore, use this method only when you need an up-to-date transform (such as during physics operations).
RIDget_canvas()const🔗
Returns theRIDof theWorld2Dcanvas where this node is registered to, used by theRenderingServer.
RIDget_canvas_item()const🔗
Returns the internal canvas itemRIDused by theRenderingServerfor this node.
CanvasLayerget_canvas_layer_node()const🔗
Returns theCanvasLayerthat contains this node, ornullif the node is not in anyCanvasLayer.
Transform2Dget_canvas_transform()const🔗
Returns the transform of this node, converted from its registered canvas's coordinate system to its viewport's coordinate system. See alsoNode.get_viewport().
Vector2get_global_mouse_position()const🔗
Returns mouse cursor's global position relative to theCanvasLayerthat contains this node.
Note:For screen-space coordinates (e.g. when using a non-embeddedPopup), you can useDisplayServer.mouse_get_position().
Transform2Dget_global_transform()const🔗
Returns the global transform matrix of this item, i.e. the combined transform up to the topmostCanvasItemnode. The topmost item is aCanvasItemthat either has no parent, has non-CanvasItemparent or it hastop_levelenabled.
Transform2Dget_global_transform_with_canvas()const🔗
Returns the transform from the local coordinate system of thisCanvasItemto theViewports coordinate system.
Variantget_instance_shader_parameter(name:StringName)const🔗
Get the value of a shader parameter as set on this instance.
Vector2get_local_mouse_position()const🔗
Returns the mouse's position in thisCanvasItemusing the local coordinate system of thisCanvasItem.
Transform2Dget_screen_transform()const🔗
Returns the transform of thisCanvasItemin global screen coordinates (i.e. taking window position into account). Mostly useful for editor plugins.
Equivalent toget_global_transform_with_canvas()if the window is embedded (seeViewport.gui_embed_subwindows).
Transform2Dget_transform()const🔗
Returns the transform matrix of thisCanvasItem.
Rect2get_viewport_rect()const🔗
Returns this node's viewport boundaries as aRect2. See alsoNode.get_viewport().
Transform2Dget_viewport_transform()const🔗
Returns the transform of this node, converted from its registered canvas's coordinate system to its viewport embedder's coordinate system. See alsoViewport.get_final_transform()andNode.get_viewport().
boolget_visibility_layer_bit(layer:int)const🔗
Returnstrueif the layer at the given index is set invisibility_layer.
World2Dget_world_2d()const🔗
Returns theWorld2Dthis node is registered to.
Usually, this is the same as this node's viewport (seeNode.get_viewport()andViewport.find_world_2d()).
voidhide()🔗
Hide theCanvasItemif it's currently visible. This is equivalent to settingvisibletofalse.
boolis_local_transform_notification_enabled()const🔗
Returnstrueif the node receivesNOTIFICATION_LOCAL_TRANSFORM_CHANGEDwhenever its local transform changes. This is enabled withset_notify_local_transform().
boolis_transform_notification_enabled()const🔗
Returnstrueif the node receivesNOTIFICATION_TRANSFORM_CHANGEDwhenever its global transform changes. This is enabled withset_notify_transform().
boolis_visible_in_tree()const🔗
Returnstrueif the node is present in theSceneTree, itsvisibleproperty istrueand all its ancestors are also visible. If any ancestor is hidden, this node will not be visible in the scene tree, and is therefore not drawn (see_draw()).
Visibility is checked only in parent nodes that inherit fromCanvasItem,CanvasLayer, andWindow. If the parent is of any other type (such asNode,AnimationPlayer, orNode3D), it is assumed to be visible.
Note:This method does not takevisibility_layerinto account, so even if this method returnstrue, the node might end up not being rendered.
Vector2make_canvas_position_local(viewport_point:Vector2)const🔗
Transformsviewport_pointfrom the viewport's coordinates to this node's local coordinates.
For the opposite operation, useget_global_transform_with_canvas().
```
var viewport_point = get_global_transform_with_canvas() * local_point
```
InputEventmake_input_local(event:InputEvent)const🔗
Returns a copy of the giveneventwith its coordinates converted from global space to thisCanvasItem's local space. If not possible, returns the sameInputEventunchanged.
voidmove_to_front()🔗
Moves this node below its siblings, usually causing the node to draw on top of its siblings. Does nothing if this node does not have a parent. See alsoNode.move_child().
voidqueue_redraw()🔗
Queues theCanvasItemto redraw. During idle time, ifCanvasItemis visible,NOTIFICATION_DRAWis sent and_draw()is called. This only occursonceper frame, even if this method has been called multiple times.
voidset_instance_shader_parameter(name:StringName, value:Variant)🔗
Set the value of a shader uniform for this instance only (per-instance uniform). See alsoShaderMaterial.set_shader_parameter()to assign a uniform on all instances using the sameShaderMaterial.
Note:For a shader uniform to be assignable on a per-instance basis, itmustbe defined withinstanceuniform...rather thanuniform...in the shader code.
Note:nameis case-sensitive and must match the name of the uniform in the code exactly (not the capitalized name in the inspector).
voidset_notify_local_transform(enable:bool)🔗
Iftrue, the node will receiveNOTIFICATION_LOCAL_TRANSFORM_CHANGEDwhenever its local transform changes.
Note:Many canvas items such asBone2DorCollisionShape2Dautomatically enable this in order to function correctly.
voidset_notify_transform(enable:bool)🔗
Iftrue, the node will receiveNOTIFICATION_TRANSFORM_CHANGEDwhenever its global transform changes.
Note:Many canvas items such asCamera2DorLight2Dautomatically enable this in order to function correctly.
voidset_visibility_layer_bit(layer:int, enabled:bool)🔗
Set/clear individual bits on the rendering visibility layer. This simplifies editing thisCanvasItem's visibility layer.
voidshow()🔗
Show theCanvasItemif it's currently hidden. This is equivalent to settingvisibletotrue.
Note:For controls that inheritPopup, the correct way to make them visible is to call one of the multiplepopup*()functions instead.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.