# RenderingServer

# RenderingServer

Inherits:Object
Server for anything visible.

## Description

The rendering server is the API backend for everything visible. The whole scene system mounts on it to display. The rendering server is completely opaque: the internals are entirely implementation-specific and cannot be accessed.
The rendering server can be used to bypass the scene/Nodesystem entirely. This can improve performance in cases where the scene system is the bottleneck, but won't improve performance otherwise (for instance, if the GPU is already fully utilized).
Resources are created using the**createfunctions. These functions returnRIDs which are not references to the objects themselves, but opaquepointerstowards these objects.
All objects are drawn to a viewport. You can use theViewportattached to theSceneTreeor you can create one yourself withviewport_create(). When using a custom scenario or canvas, the scenario or canvas needs to be attached to the viewport usingviewport_set_scenario()orviewport_attach_canvas().
Scenarios:In 3D, all visual objects must be associated with a scenario. The scenario is a visual representation of the world. If accessing the rendering server from a running game, the scenario can be accessed from the scene tree from anyNode3Dnode withNode3D.get_world_3d(). Otherwise, a scenario can be created withscenario_create().
Similarly, in 2D, a canvas is needed to draw all canvas items.
3D:In 3D, all visible objects are comprised of a resource and an instance. A resource can be a mesh, a particle system, a light, or any other 3D object. In order to be visible resources must be attached to an instance usinginstance_set_base(). The instance must also be attached to the scenario usinginstance_set_scenario()in order to be visible. RenderingServer methods that don't have a prefix are usually 3D-specific (but not always).
2D:In 2D, all visible objects are some form of canvas item. In order to be visible, a canvas item needs to be the child of a canvas attached to a viewport, or it needs to be the child of another canvas item that is eventually attached to the canvas. 2D-specific RenderingServer methods generally start withcanvas**.
Headless mode:Starting the engine with the--headlesscommand line argumentdisables all rendering and window management functions. Most functions fromRenderingServerwill return dummy values in this case.

## Tutorials

- Optimization using Servers
Optimization using Servers

## Properties

| bool | render_loop_enabled |

bool
render_loop_enabled

## Methods

| Array[Image] | bake_render_uv2(base:RID, material_overrides:Array[RID], image_size:Vector2i) |
|---|---|
| void | call_on_render_thread(callable:Callable) |
| RID | camera_attributes_create() |
| void | camera_attributes_set_auto_exposure(camera_attributes:RID, enable:bool, min_sensitivity:float, max_sensitivity:float, speed:float, scale:float) |
| void | camera_attributes_set_dof_blur(camera_attributes:RID, far_enable:bool, far_distance:float, far_transition:float, near_enable:bool, near_distance:float, near_transition:float, amount:float) |
| void | camera_attributes_set_dof_blur_bokeh_shape(shape:DOFBokehShape) |
| void | camera_attributes_set_dof_blur_quality(quality:DOFBlurQuality, use_jitter:bool) |
| void | camera_attributes_set_exposure(camera_attributes:RID, multiplier:float, normalization:float) |
| RID | camera_create() |
| void | camera_set_camera_attributes(camera:RID, effects:RID) |
| void | camera_set_compositor(camera:RID, compositor:RID) |
| void | camera_set_cull_mask(camera:RID, layers:int) |
| void | camera_set_environment(camera:RID, env:RID) |
| void | camera_set_frustum(camera:RID, size:float, offset:Vector2, z_near:float, z_far:float) |
| void | camera_set_orthogonal(camera:RID, size:float, z_near:float, z_far:float) |
| void | camera_set_perspective(camera:RID, fovy_degrees:float, z_near:float, z_far:float) |
| void | camera_set_transform(camera:RID, transform:Transform3D) |
| void | camera_set_use_vertical_aspect(camera:RID, enable:bool) |
| RID | canvas_create() |
| void | canvas_item_add_animation_slice(item:RID, animation_length:float, slice_begin:float, slice_end:float, offset:float= 0.0) |
| void | canvas_item_add_circle(item:RID, pos:Vector2, radius:float, color:Color, antialiased:bool= false) |
| void | canvas_item_add_clip_ignore(item:RID, ignore:bool) |
| void | canvas_item_add_ellipse(item:RID, pos:Vector2, major:float, minor:float, color:Color, antialiased:bool= false) |
| void | canvas_item_add_lcd_texture_rect_region(item:RID, rect:Rect2, texture:RID, src_rect:Rect2, modulate:Color) |
| void | canvas_item_add_line(item:RID, from:Vector2, to:Vector2, color:Color, width:float= -1.0, antialiased:bool= false) |
| void | canvas_item_add_mesh(item:RID, mesh:RID, transform:Transform2D= Transform2D(1, 0, 0, 1, 0, 0), modulate:Color= Color(1, 1, 1, 1), texture:RID= RID()) |
| void | canvas_item_add_msdf_texture_rect_region(item:RID, rect:Rect2, texture:RID, src_rect:Rect2, modulate:Color= Color(1, 1, 1, 1), outline_size:int= 0, px_range:float= 1.0, scale:float= 1.0) |
| void | canvas_item_add_multiline(item:RID, points:PackedVector2Array, colors:PackedColorArray, width:float= -1.0, antialiased:bool= false) |
| void | canvas_item_add_multimesh(item:RID, mesh:RID, texture:RID= RID()) |
| void | canvas_item_add_nine_patch(item:RID, rect:Rect2, source:Rect2, texture:RID, topleft:Vector2, bottomright:Vector2, x_axis_mode:NinePatchAxisMode= 0, y_axis_mode:NinePatchAxisMode= 0, draw_center:bool= true, modulate:Color= Color(1, 1, 1, 1)) |
| void | canvas_item_add_particles(item:RID, particles:RID, texture:RID) |
| void | canvas_item_add_polygon(item:RID, points:PackedVector2Array, colors:PackedColorArray, uvs:PackedVector2Array= PackedVector2Array(), texture:RID= RID()) |
| void | canvas_item_add_polyline(item:RID, points:PackedVector2Array, colors:PackedColorArray, width:float= -1.0, antialiased:bool= false) |
| void | canvas_item_add_primitive(item:RID, points:PackedVector2Array, colors:PackedColorArray, uvs:PackedVector2Array, texture:RID) |
| void | canvas_item_add_rect(item:RID, rect:Rect2, color:Color, antialiased:bool= false) |
| void | canvas_item_add_set_transform(item:RID, transform:Transform2D) |
| void | canvas_item_add_texture_rect(item:RID, rect:Rect2, texture:RID, tile:bool= false, modulate:Color= Color(1, 1, 1, 1), transpose:bool= false) |
| void | canvas_item_add_texture_rect_region(item:RID, rect:Rect2, texture:RID, src_rect:Rect2, modulate:Color= Color(1, 1, 1, 1), transpose:bool= false, clip_uv:bool= true) |
| void | canvas_item_add_triangle_array(item:RID, indices:PackedInt32Array, points:PackedVector2Array, colors:PackedColorArray, uvs:PackedVector2Array= PackedVector2Array(), bones:PackedInt32Array= PackedInt32Array(), weights:PackedFloat32Array= PackedFloat32Array(), texture:RID= RID(), count:int= -1) |
| void | canvas_item_attach_skeleton(item:RID, skeleton:RID) |
| void | canvas_item_clear(item:RID) |
| RID | canvas_item_create() |
| Variant | canvas_item_get_instance_shader_parameter(instance:RID, parameter:StringName)const |
| Variant | canvas_item_get_instance_shader_parameter_default_value(instance:RID, parameter:StringName)const |
| Array[Dictionary] | canvas_item_get_instance_shader_parameter_list(instance:RID)const |
| void | canvas_item_reset_physics_interpolation(item:RID) |
| void | canvas_item_set_canvas_group_mode(item:RID, mode:CanvasGroupMode, clear_margin:float= 5.0, fit_empty:bool= false, fit_margin:float= 0.0, blur_mipmaps:bool= false) |
| void | canvas_item_set_clip(item:RID, clip:bool) |
| void | canvas_item_set_copy_to_backbuffer(item:RID, enabled:bool, rect:Rect2) |
| void | canvas_item_set_custom_rect(item:RID, use_custom_rect:bool, rect:Rect2= Rect2(0, 0, 0, 0)) |
| void | canvas_item_set_default_texture_filter(item:RID, filter:CanvasItemTextureFilter) |
| void | canvas_item_set_default_texture_repeat(item:RID, repeat:CanvasItemTextureRepeat) |
| void | canvas_item_set_distance_field_mode(item:RID, enabled:bool) |
| void | canvas_item_set_draw_behind_parent(item:RID, enabled:bool) |
| void | canvas_item_set_draw_index(item:RID, index:int) |
| void | canvas_item_set_instance_shader_parameter(instance:RID, parameter:StringName, value:Variant) |
| void | canvas_item_set_interpolated(item:RID, interpolated:bool) |
| void | canvas_item_set_light_mask(item:RID, mask:int) |
| void | canvas_item_set_material(item:RID, material:RID) |
| void | canvas_item_set_modulate(item:RID, color:Color) |
| void | canvas_item_set_parent(item:RID, parent:RID) |
| void | canvas_item_set_self_modulate(item:RID, color:Color) |
| void | canvas_item_set_sort_children_by_y(item:RID, enabled:bool) |
| void | canvas_item_set_transform(item:RID, transform:Transform2D) |
| void | canvas_item_set_use_parent_material(item:RID, enabled:bool) |
| void | canvas_item_set_visibility_layer(item:RID, visibility_layer:int) |
| void | canvas_item_set_visibility_notifier(item:RID, enable:bool, area:Rect2, enter_callable:Callable, exit_callable:Callable) |
| void | canvas_item_set_visible(item:RID, visible:bool) |
| void | canvas_item_set_z_as_relative_to_parent(item:RID, enabled:bool) |
| void | canvas_item_set_z_index(item:RID, z_index:int) |
| void | canvas_item_transform_physics_interpolation(item:RID, transform:Transform2D) |
| void | canvas_light_attach_to_canvas(light:RID, canvas:RID) |
| RID | canvas_light_create() |
| void | canvas_light_occluder_attach_to_canvas(occluder:RID, canvas:RID) |
| RID | canvas_light_occluder_create() |
| void | canvas_light_occluder_reset_physics_interpolation(occluder:RID) |
| void | canvas_light_occluder_set_as_sdf_collision(occluder:RID, enable:bool) |
| void | canvas_light_occluder_set_enabled(occluder:RID, enabled:bool) |
| void | canvas_light_occluder_set_interpolated(occluder:RID, interpolated:bool) |
| void | canvas_light_occluder_set_light_mask(occluder:RID, mask:int) |
| void | canvas_light_occluder_set_polygon(occluder:RID, polygon:RID) |
| void | canvas_light_occluder_set_transform(occluder:RID, transform:Transform2D) |
| void | canvas_light_occluder_transform_physics_interpolation(occluder:RID, transform:Transform2D) |
| void | canvas_light_reset_physics_interpolation(light:RID) |
| void | canvas_light_set_blend_mode(light:RID, mode:CanvasLightBlendMode) |
| void | canvas_light_set_color(light:RID, color:Color) |
| void | canvas_light_set_enabled(light:RID, enabled:bool) |
| void | canvas_light_set_energy(light:RID, energy:float) |
| void | canvas_light_set_height(light:RID, height:float) |
| void | canvas_light_set_interpolated(light:RID, interpolated:bool) |
| void | canvas_light_set_item_cull_mask(light:RID, mask:int) |
| void | canvas_light_set_item_shadow_cull_mask(light:RID, mask:int) |
| void | canvas_light_set_layer_range(light:RID, min_layer:int, max_layer:int) |
| void | canvas_light_set_mode(light:RID, mode:CanvasLightMode) |
| void | canvas_light_set_shadow_color(light:RID, color:Color) |
| void | canvas_light_set_shadow_enabled(light:RID, enabled:bool) |
| void | canvas_light_set_shadow_filter(light:RID, filter:CanvasLightShadowFilter) |
| void | canvas_light_set_shadow_smooth(light:RID, smooth:float) |
| void | canvas_light_set_texture(light:RID, texture:RID) |
| void | canvas_light_set_texture_offset(light:RID, offset:Vector2) |
| void | canvas_light_set_texture_scale(light:RID, scale:float) |
| void | canvas_light_set_transform(light:RID, transform:Transform2D) |
| void | canvas_light_set_z_range(light:RID, min_z:int, max_z:int) |
| void | canvas_light_transform_physics_interpolation(light:RID, transform:Transform2D) |
| RID | canvas_occluder_polygon_create() |
| void | canvas_occluder_polygon_set_cull_mode(occluder_polygon:RID, mode:CanvasOccluderPolygonCullMode) |
| void | canvas_occluder_polygon_set_shape(occluder_polygon:RID, shape:PackedVector2Array, closed:bool) |
| void | canvas_set_disable_scale(disable:bool) |
| void | canvas_set_item_mirroring(canvas:RID, item:RID, mirroring:Vector2) |
| void | canvas_set_item_repeat(item:RID, repeat_size:Vector2, repeat_times:int) |
| void | canvas_set_modulate(canvas:RID, color:Color) |
| void | canvas_set_shadow_texture_size(size:int) |
| RID | canvas_texture_create() |
| void | canvas_texture_set_channel(canvas_texture:RID, channel:CanvasTextureChannel, texture:RID) |
| void | canvas_texture_set_shading_parameters(canvas_texture:RID, base_color:Color, shininess:float) |
| void | canvas_texture_set_texture_filter(canvas_texture:RID, filter:CanvasItemTextureFilter) |
| void | canvas_texture_set_texture_repeat(canvas_texture:RID, repeat:CanvasItemTextureRepeat) |
| RID | compositor_create() |
| RID | compositor_effect_create() |
| void | compositor_effect_set_callback(effect:RID, callback_type:CompositorEffectCallbackType, callback:Callable) |
| void | compositor_effect_set_enabled(effect:RID, enabled:bool) |
| void | compositor_effect_set_flag(effect:RID, flag:CompositorEffectFlags, set:bool) |
| void | compositor_set_compositor_effects(compositor:RID, effects:Array[RID]) |
| RenderingDevice | create_local_rendering_device()const |
| Rect2 | debug_canvas_item_get_rect(item:RID) |
| RID | decal_create() |
| void | decal_set_albedo_mix(decal:RID, albedo_mix:float) |
| void | decal_set_cull_mask(decal:RID, mask:int) |
| void | decal_set_distance_fade(decal:RID, enabled:bool, begin:float, length:float) |
| void | decal_set_emission_energy(decal:RID, energy:float) |
| void | decal_set_fade(decal:RID, above:float, below:float) |
| void | decal_set_modulate(decal:RID, color:Color) |
| void | decal_set_normal_fade(decal:RID, fade:float) |
| void | decal_set_size(decal:RID, size:Vector3) |
| void | decal_set_texture(decal:RID, type:DecalTexture, texture:RID) |
| void | decals_set_filter(filter:DecalFilter) |
| RID | directional_light_create() |
| void | directional_shadow_atlas_set_size(size:int, is_16bits:bool) |
| void | directional_soft_shadow_filter_set_quality(quality:ShadowQuality) |
| Image | environment_bake_panorama(environment:RID, bake_irradiance:bool, size:Vector2i) |
| RID | environment_create() |
| void | environment_glow_set_use_bicubic_upscale(enable:bool) |
| void | environment_set_adjustment(env:RID, enable:bool, brightness:float, contrast:float, saturation:float, use_1d_color_correction:bool, color_correction:RID) |
| void | environment_set_ambient_light(env:RID, color:Color, ambient:EnvironmentAmbientSource= 0, energy:float= 1.0, sky_contribution:float= 0.0, reflection_source:EnvironmentReflectionSource= 0) |
| void | environment_set_background(env:RID, bg:EnvironmentBG) |
| void | environment_set_bg_color(env:RID, color:Color) |
| void | environment_set_bg_energy(env:RID, multiplier:float, exposure_value:float) |
| void | environment_set_camera_id(env:RID, id:int) |
| void | environment_set_canvas_max_layer(env:RID, max_layer:int) |
| void | environment_set_fog(env:RID, enable:bool, light_color:Color, light_energy:float, sun_scatter:float, density:float, height:float, height_density:float, aerial_perspective:float, sky_affect:float, fog_mode:EnvironmentFogMode= 0) |
| void | environment_set_fog_depth(env:RID, curve:float, begin:float, end:float) |
| void | environment_set_glow(env:RID, enable:bool, levels:PackedFloat32Array, intensity:float, strength:float, mix:float, bloom_threshold:float, blend_mode:EnvironmentGlowBlendMode, hdr_bleed_threshold:float, hdr_bleed_scale:float, hdr_luminance_cap:float, glow_map_strength:float, glow_map:RID) |
| void | environment_set_sdfgi(env:RID, enable:bool, cascades:int, min_cell_size:float, y_scale:EnvironmentSDFGIYScale, use_occlusion:bool, bounce_feedback:float, read_sky:bool, energy:float, normal_bias:float, probe_bias:float) |
| void | environment_set_sdfgi_frames_to_converge(frames:EnvironmentSDFGIFramesToConverge) |
| void | environment_set_sdfgi_frames_to_update_light(frames:EnvironmentSDFGIFramesToUpdateLight) |
| void | environment_set_sdfgi_ray_count(ray_count:EnvironmentSDFGIRayCount) |
| void | environment_set_sky(env:RID, sky:RID) |
| void | environment_set_sky_custom_fov(env:RID, scale:float) |
| void | environment_set_sky_orientation(env:RID, orientation:Basis) |
| void | environment_set_ssao(env:RID, enable:bool, radius:float, intensity:float, power:float, detail:float, horizon:float, sharpness:float, light_affect:float, ao_channel_affect:float) |
| void | environment_set_ssao_quality(quality:EnvironmentSSAOQuality, half_size:bool, adaptive_target:float, blur_passes:int, fadeout_from:float, fadeout_to:float) |
| void | environment_set_ssil_quality(quality:EnvironmentSSILQuality, half_size:bool, adaptive_target:float, blur_passes:int, fadeout_from:float, fadeout_to:float) |
| void | environment_set_ssr(env:RID, enable:bool, max_steps:int, fade_in:float, fade_out:float, depth_tolerance:float) |
| void | environment_set_ssr_half_size(half_size:bool) |
| void | environment_set_ssr_roughness_quality(quality:EnvironmentSSRRoughnessQuality) |
| void | environment_set_tonemap(env:RID, tone_mapper:EnvironmentToneMapper, exposure:float, white:float) |
| void | environment_set_tonemap_agx_contrast(env:RID, agx_contrast:float) |
| void | environment_set_volumetric_fog(env:RID, enable:bool, density:float, albedo:Color, emission:Color, emission_energy:float, anisotropy:float, length:float, p_detail_spread:float, gi_inject:float, temporal_reprojection:bool, temporal_reprojection_amount:float, ambient_inject:float, sky_affect:float) |
| void | environment_set_volumetric_fog_filter_active(active:bool) |
| void | environment_set_volumetric_fog_volume_size(size:int, depth:int) |
| RID | fog_volume_create() |
| void | fog_volume_set_material(fog_volume:RID, material:RID) |
| void | fog_volume_set_shape(fog_volume:RID, shape:FogVolumeShape) |
| void | fog_volume_set_size(fog_volume:RID, size:Vector3) |
| void | force_draw(swap_buffers:bool= true, frame_step:float= 0.0) |
| void | force_sync() |
| void | free_rid(rid:RID) |
| String | get_current_rendering_driver_name()const |
| String | get_current_rendering_method()const |
| Color | get_default_clear_color() |
| float | get_frame_setup_time_cpu()const |
| RenderingDevice | get_rendering_device()const |
| int | get_rendering_info(info:RenderingInfo) |
| Array[Dictionary] | get_shader_parameter_list(shader:RID)const |
| RID | get_test_cube() |
| RID | get_test_texture() |
| String | get_video_adapter_api_version()const |
| String | get_video_adapter_name()const |
| DeviceType | get_video_adapter_type()const |
| String | get_video_adapter_vendor()const |
| RID | get_white_texture() |
| void | gi_set_use_half_resolution(half_resolution:bool) |
| void | global_shader_parameter_add(name:StringName, type:GlobalShaderParameterType, default_value:Variant) |
| Variant | global_shader_parameter_get(name:StringName)const |
| Array[StringName] | global_shader_parameter_get_list()const |
| GlobalShaderParameterType | global_shader_parameter_get_type(name:StringName)const |
| void | global_shader_parameter_remove(name:StringName) |
| void | global_shader_parameter_set(name:StringName, value:Variant) |
| void | global_shader_parameter_set_override(name:StringName, value:Variant) |
| bool | has_changed()const |
| bool | has_feature(feature:Features)const |
| bool | has_os_feature(feature:String)const |
| void | instance_attach_object_instance_id(instance:RID, id:int) |
| void | instance_attach_skeleton(instance:RID, skeleton:RID) |
| RID | instance_create() |
| RID | instance_create2(base:RID, scenario:RID) |
| Variant | instance_geometry_get_shader_parameter(instance:RID, parameter:StringName)const |
| Variant | instance_geometry_get_shader_parameter_default_value(instance:RID, parameter:StringName)const |
| Array[Dictionary] | instance_geometry_get_shader_parameter_list(instance:RID)const |
| void | instance_geometry_set_cast_shadows_setting(instance:RID, shadow_casting_setting:ShadowCastingSetting) |
| void | instance_geometry_set_flag(instance:RID, flag:InstanceFlags, enabled:bool) |
| void | instance_geometry_set_lightmap(instance:RID, lightmap:RID, lightmap_uv_scale:Rect2, lightmap_slice:int) |
| void | instance_geometry_set_lod_bias(instance:RID, lod_bias:float) |
| void | instance_geometry_set_material_overlay(instance:RID, material:RID) |
| void | instance_geometry_set_material_override(instance:RID, material:RID) |
| void | instance_geometry_set_shader_parameter(instance:RID, parameter:StringName, value:Variant) |
| void | instance_geometry_set_transparency(instance:RID, transparency:float) |
| void | instance_geometry_set_visibility_range(instance:RID, min:float, max:float, min_margin:float, max_margin:float, fade_mode:VisibilityRangeFadeMode) |
| void | instance_set_base(instance:RID, base:RID) |
| void | instance_set_blend_shape_weight(instance:RID, shape:int, weight:float) |
| void | instance_set_custom_aabb(instance:RID, aabb:AABB) |
| void | instance_set_extra_visibility_margin(instance:RID, margin:float) |
| void | instance_set_ignore_culling(instance:RID, enabled:bool) |
| void | instance_set_layer_mask(instance:RID, mask:int) |
| void | instance_set_pivot_data(instance:RID, sorting_offset:float, use_aabb_center:bool) |
| void | instance_set_scenario(instance:RID, scenario:RID) |
| void | instance_set_surface_override_material(instance:RID, surface:int, material:RID) |
| void | instance_set_transform(instance:RID, transform:Transform3D) |
| void | instance_set_visibility_parent(instance:RID, parent:RID) |
| void | instance_set_visible(instance:RID, visible:bool) |
| void | instance_teleport(instance:RID) |
| PackedInt64Array | instances_cull_aabb(aabb:AABB, scenario:RID= RID())const |
| PackedInt64Array | instances_cull_convex(convex:Array[Plane], scenario:RID= RID())const |
| PackedInt64Array | instances_cull_ray(from:Vector3, to:Vector3, scenario:RID= RID())const |
| bool | is_on_render_thread() |
| void | light_directional_set_blend_splits(light:RID, enable:bool) |
| void | light_directional_set_shadow_mode(light:RID, mode:LightDirectionalShadowMode) |
| void | light_directional_set_sky_mode(light:RID, mode:LightDirectionalSkyMode) |
| void | light_omni_set_shadow_mode(light:RID, mode:LightOmniShadowMode) |
| void | light_projectors_set_filter(filter:LightProjectorFilter) |
| void | light_set_bake_mode(light:RID, bake_mode:LightBakeMode) |
| void | light_set_color(light:RID, color:Color) |
| void | light_set_cull_mask(light:RID, mask:int) |
| void | light_set_distance_fade(decal:RID, enabled:bool, begin:float, shadow:float, length:float) |
| void | light_set_max_sdfgi_cascade(light:RID, cascade:int) |
| void | light_set_negative(light:RID, enable:bool) |
| void | light_set_param(light:RID, param:LightParam, value:float) |
| void | light_set_projector(light:RID, texture:RID) |
| void | light_set_reverse_cull_face_mode(light:RID, enabled:bool) |
| void | light_set_shadow(light:RID, enabled:bool) |
| void | light_set_shadow_caster_mask(light:RID, mask:int) |
| RID | lightmap_create() |
| PackedInt32Array | lightmap_get_probe_capture_bsp_tree(lightmap:RID)const |
| PackedVector3Array | lightmap_get_probe_capture_points(lightmap:RID)const |
| PackedColorArray | lightmap_get_probe_capture_sh(lightmap:RID)const |
| PackedInt32Array | lightmap_get_probe_capture_tetrahedra(lightmap:RID)const |
| void | lightmap_set_baked_exposure_normalization(lightmap:RID, baked_exposure:float) |
| void | lightmap_set_probe_bounds(lightmap:RID, bounds:AABB) |
| void | lightmap_set_probe_capture_data(lightmap:RID, points:PackedVector3Array, point_sh:PackedColorArray, tetrahedra:PackedInt32Array, bsp_tree:PackedInt32Array) |
| void | lightmap_set_probe_capture_update_speed(speed:float) |
| void | lightmap_set_probe_interior(lightmap:RID, interior:bool) |
| void | lightmap_set_textures(lightmap:RID, light:RID, uses_sh:bool) |
| void | lightmaps_set_bicubic_filter(enable:bool) |
| RID | make_sphere_mesh(latitudes:int, longitudes:int, radius:float) |
| RID | material_create() |
| Variant | material_get_param(material:RID, parameter:StringName)const |
| void | material_set_next_pass(material:RID, next_material:RID) |
| void | material_set_param(material:RID, parameter:StringName, value:Variant) |
| void | material_set_render_priority(material:RID, priority:int) |
| void | material_set_shader(shader_material:RID, shader:RID) |
| void | material_set_use_debanding(enable:bool) |
| void | mesh_add_surface(mesh:RID, surface:Dictionary) |
| void | mesh_add_surface_from_arrays(mesh:RID, primitive:PrimitiveType, arrays:Array, blend_shapes:Array= [], lods:Dictionary= {}, compress_format:BitField[ArrayFormat] = 0) |
| void | mesh_clear(mesh:RID) |
| RID | mesh_create() |
| RID | mesh_create_from_surfaces(surfaces:Array[Dictionary], blend_shape_count:int= 0) |
| int | mesh_get_blend_shape_count(mesh:RID)const |
| BlendShapeMode | mesh_get_blend_shape_mode(mesh:RID)const |
| AABB | mesh_get_custom_aabb(mesh:RID)const |
| Dictionary | mesh_get_surface(mesh:RID, surface:int) |
| int | mesh_get_surface_count(mesh:RID)const |
| void | mesh_set_blend_shape_mode(mesh:RID, mode:BlendShapeMode) |
| void | mesh_set_custom_aabb(mesh:RID, aabb:AABB) |
| void | mesh_set_shadow_mesh(mesh:RID, shadow_mesh:RID) |
| Array | mesh_surface_get_arrays(mesh:RID, surface:int)const |
| Array[Array] | mesh_surface_get_blend_shape_arrays(mesh:RID, surface:int)const |
| int | mesh_surface_get_format_attribute_stride(format:BitField[ArrayFormat], vertex_count:int)const |
| int | mesh_surface_get_format_index_stride(format:BitField[ArrayFormat], vertex_count:int)const |
| int | mesh_surface_get_format_normal_tangent_stride(format:BitField[ArrayFormat], vertex_count:int)const |
| int | mesh_surface_get_format_offset(format:BitField[ArrayFormat], vertex_count:int, array_index:int)const |
| int | mesh_surface_get_format_skin_stride(format:BitField[ArrayFormat], vertex_count:int)const |
| int | mesh_surface_get_format_vertex_stride(format:BitField[ArrayFormat], vertex_count:int)const |
| RID | mesh_surface_get_material(mesh:RID, surface:int)const |
| void | mesh_surface_remove(mesh:RID, surface:int) |
| void | mesh_surface_set_material(mesh:RID, surface:int, material:RID) |
| void | mesh_surface_update_attribute_region(mesh:RID, surface:int, offset:int, data:PackedByteArray) |
| void | mesh_surface_update_index_region(mesh:RID, surface:int, offset:int, data:PackedByteArray) |
| void | mesh_surface_update_skin_region(mesh:RID, surface:int, offset:int, data:PackedByteArray) |
| void | mesh_surface_update_vertex_region(mesh:RID, surface:int, offset:int, data:PackedByteArray) |
| void | multimesh_allocate_data(multimesh:RID, instances:int, transform_format:MultimeshTransformFormat, color_format:bool= false, custom_data_format:bool= false, use_indirect:bool= false) |
| RID | multimesh_create() |
| AABB | multimesh_get_aabb(multimesh:RID)const |
| PackedFloat32Array | multimesh_get_buffer(multimesh:RID)const |
| RID | multimesh_get_buffer_rd_rid(multimesh:RID)const |
| RID | multimesh_get_command_buffer_rd_rid(multimesh:RID)const |
| AABB | multimesh_get_custom_aabb(multimesh:RID)const |
| int | multimesh_get_instance_count(multimesh:RID)const |
| RID | multimesh_get_mesh(multimesh:RID)const |
| int | multimesh_get_visible_instances(multimesh:RID)const |
| Color | multimesh_instance_get_color(multimesh:RID, index:int)const |
| Color | multimesh_instance_get_custom_data(multimesh:RID, index:int)const |
| Transform3D | multimesh_instance_get_transform(multimesh:RID, index:int)const |
| Transform2D | multimesh_instance_get_transform_2d(multimesh:RID, index:int)const |
| void | multimesh_instance_reset_physics_interpolation(multimesh:RID, index:int) |
| void | multimesh_instance_set_color(multimesh:RID, index:int, color:Color) |
| void | multimesh_instance_set_custom_data(multimesh:RID, index:int, custom_data:Color) |
| void | multimesh_instance_set_transform(multimesh:RID, index:int, transform:Transform3D) |
| void | multimesh_instance_set_transform_2d(multimesh:RID, index:int, transform:Transform2D) |
| void | multimesh_instances_reset_physics_interpolation(multimesh:RID) |
| void | multimesh_set_buffer(multimesh:RID, buffer:PackedFloat32Array) |
| void | multimesh_set_buffer_interpolated(multimesh:RID, buffer:PackedFloat32Array, buffer_previous:PackedFloat32Array) |
| void | multimesh_set_custom_aabb(multimesh:RID, aabb:AABB) |
| void | multimesh_set_mesh(multimesh:RID, mesh:RID) |
| void | multimesh_set_physics_interpolated(multimesh:RID, interpolated:bool) |
| void | multimesh_set_physics_interpolation_quality(multimesh:RID, quality:MultimeshPhysicsInterpolationQuality) |
| void | multimesh_set_visible_instances(multimesh:RID, visible:int) |
| RID | occluder_create() |
| void | occluder_set_mesh(occluder:RID, vertices:PackedVector3Array, indices:PackedInt32Array) |
| RID | omni_light_create() |
| RID | particles_collision_create() |
| void | particles_collision_height_field_update(particles_collision:RID) |
| void | particles_collision_set_attractor_attenuation(particles_collision:RID, curve:float) |
| void | particles_collision_set_attractor_directionality(particles_collision:RID, amount:float) |
| void | particles_collision_set_attractor_strength(particles_collision:RID, strength:float) |
| void | particles_collision_set_box_extents(particles_collision:RID, extents:Vector3) |
| void | particles_collision_set_collision_type(particles_collision:RID, type:ParticlesCollisionType) |
| void | particles_collision_set_cull_mask(particles_collision:RID, mask:int) |
| void | particles_collision_set_field_texture(particles_collision:RID, texture:RID) |
| void | particles_collision_set_height_field_mask(particles_collision:RID, mask:int) |
| void | particles_collision_set_height_field_resolution(particles_collision:RID, resolution:ParticlesCollisionHeightfieldResolution) |
| void | particles_collision_set_sphere_radius(particles_collision:RID, radius:float) |
| RID | particles_create() |
| void | particles_emit(particles:RID, transform:Transform3D, velocity:Vector3, color:Color, custom:Color, emit_flags:int) |
| AABB | particles_get_current_aabb(particles:RID) |
| bool | particles_get_emitting(particles:RID) |
| bool | particles_is_inactive(particles:RID) |
| void | particles_request_process(particles:RID) |
| void | particles_request_process_time(particles:RID, time:float) |
| void | particles_restart(particles:RID) |
| void | particles_set_amount(particles:RID, amount:int) |
| void | particles_set_amount_ratio(particles:RID, ratio:float) |
| void | particles_set_collision_base_size(particles:RID, size:float) |
| void | particles_set_custom_aabb(particles:RID, aabb:AABB) |
| void | particles_set_draw_order(particles:RID, order:ParticlesDrawOrder) |
| void | particles_set_draw_pass_mesh(particles:RID, pass:int, mesh:RID) |
| void | particles_set_draw_passes(particles:RID, count:int) |
| void | particles_set_emission_transform(particles:RID, transform:Transform3D) |
| void | particles_set_emitter_velocity(particles:RID, velocity:Vector3) |
| void | particles_set_emitting(particles:RID, emitting:bool) |
| void | particles_set_explosiveness_ratio(particles:RID, ratio:float) |
| void | particles_set_fixed_fps(particles:RID, fps:int) |
| void | particles_set_fractional_delta(particles:RID, enable:bool) |
| void | particles_set_interp_to_end(particles:RID, factor:float) |
| void | particles_set_interpolate(particles:RID, enable:bool) |
| void | particles_set_lifetime(particles:RID, lifetime:float) |
| void | particles_set_mode(particles:RID, mode:ParticlesMode) |
| void | particles_set_one_shot(particles:RID, one_shot:bool) |
| void | particles_set_pre_process_time(particles:RID, time:float) |
| void | particles_set_process_material(particles:RID, material:RID) |
| void | particles_set_randomness_ratio(particles:RID, ratio:float) |
| void | particles_set_speed_scale(particles:RID, scale:float) |
| void | particles_set_subemitter(particles:RID, subemitter_particles:RID) |
| void | particles_set_trail_bind_poses(particles:RID, bind_poses:Array[Transform3D]) |
| void | particles_set_trails(particles:RID, enable:bool, length_sec:float) |
| void | particles_set_transform_align(particles:RID, align:ParticlesTransformAlign) |
| void | particles_set_use_local_coordinates(particles:RID, enable:bool) |
| void | positional_soft_shadow_filter_set_quality(quality:ShadowQuality) |
| RID | reflection_probe_create() |
| void | reflection_probe_set_ambient_color(probe:RID, color:Color) |
| void | reflection_probe_set_ambient_energy(probe:RID, energy:float) |
| void | reflection_probe_set_ambient_mode(probe:RID, mode:ReflectionProbeAmbientMode) |
| void | reflection_probe_set_as_interior(probe:RID, enable:bool) |
| void | reflection_probe_set_blend_distance(probe:RID, blend_distance:float) |
| void | reflection_probe_set_cull_mask(probe:RID, layers:int) |
| void | reflection_probe_set_enable_box_projection(probe:RID, enable:bool) |
| void | reflection_probe_set_enable_shadows(probe:RID, enable:bool) |
| void | reflection_probe_set_intensity(probe:RID, intensity:float) |
| void | reflection_probe_set_max_distance(probe:RID, distance:float) |
| void | reflection_probe_set_mesh_lod_threshold(probe:RID, pixels:float) |
| void | reflection_probe_set_origin_offset(probe:RID, offset:Vector3) |
| void | reflection_probe_set_reflection_mask(probe:RID, layers:int) |
| void | reflection_probe_set_resolution(probe:RID, resolution:int) |
| void | reflection_probe_set_size(probe:RID, size:Vector3) |
| void | reflection_probe_set_update_mode(probe:RID, mode:ReflectionProbeUpdateMode) |
| void | request_frame_drawn_callback(callable:Callable) |
| RID | scenario_create() |
| void | scenario_set_camera_attributes(scenario:RID, effects:RID) |
| void | scenario_set_compositor(scenario:RID, compositor:RID) |
| void | scenario_set_environment(scenario:RID, environment:RID) |
| void | scenario_set_fallback_environment(scenario:RID, environment:RID) |
| void | screen_space_roughness_limiter_set_active(enable:bool, amount:float, limit:float) |
| void | set_boot_image(image:Image, color:Color, scale:bool, use_filter:bool= true) |
| void | set_boot_image_with_stretch(image:Image, color:Color, stretch_mode:SplashStretchMode, use_filter:bool= true) |
| void | set_debug_generate_wireframes(generate:bool) |
| void | set_default_clear_color(color:Color) |
| RID | shader_create() |
| String | shader_get_code(shader:RID)const |
| RID | shader_get_default_texture_parameter(shader:RID, name:StringName, index:int= 0)const |
| Variant | shader_get_parameter_default(shader:RID, name:StringName)const |
| void | shader_set_code(shader:RID, code:String) |
| void | shader_set_default_texture_parameter(shader:RID, name:StringName, texture:RID, index:int= 0) |
| void | shader_set_path_hint(shader:RID, path:String) |
| void | skeleton_allocate_data(skeleton:RID, bones:int, is_2d_skeleton:bool= false) |
| Transform3D | skeleton_bone_get_transform(skeleton:RID, bone:int)const |
| Transform2D | skeleton_bone_get_transform_2d(skeleton:RID, bone:int)const |
| void | skeleton_bone_set_transform(skeleton:RID, bone:int, transform:Transform3D) |
| void | skeleton_bone_set_transform_2d(skeleton:RID, bone:int, transform:Transform2D) |
| RID | skeleton_create() |
| int | skeleton_get_bone_count(skeleton:RID)const |
| void | skeleton_set_base_transform_2d(skeleton:RID, base_transform:Transform2D) |
| Image | sky_bake_panorama(sky:RID, energy:float, bake_irradiance:bool, size:Vector2i) |
| RID | sky_create() |
| void | sky_set_material(sky:RID, material:RID) |
| void | sky_set_mode(sky:RID, mode:SkyMode) |
| void | sky_set_radiance_size(sky:RID, radiance_size:int) |
| RID | spot_light_create() |
| void | sub_surface_scattering_set_quality(quality:SubSurfaceScatteringQuality) |
| void | sub_surface_scattering_set_scale(scale:float, depth_scale:float) |
| RID | texture_2d_create(image:Image) |
| Image | texture_2d_get(texture:RID)const |
| Image | texture_2d_layer_get(texture:RID, layer:int)const |
| RID | texture_2d_layered_create(layers:Array[Image], layered_type:TextureLayeredType) |
| RID | texture_2d_layered_placeholder_create(layered_type:TextureLayeredType) |
| RID | texture_2d_placeholder_create() |
| void | texture_2d_update(texture:RID, image:Image, layer:int) |
| RID | texture_3d_create(format:Format, width:int, height:int, depth:int, mipmaps:bool, data:Array[Image]) |
| Array[Image] | texture_3d_get(texture:RID)const |
| RID | texture_3d_placeholder_create() |
| void | texture_3d_update(texture:RID, data:Array[Image]) |
| RID | texture_create_from_native_handle(type:TextureType, format:Format, native_handle:int, width:int, height:int, depth:int, layers:int= 1, layered_type:TextureLayeredType= 0) |
| Format | texture_get_format(texture:RID)const |
| int | texture_get_native_handle(texture:RID, srgb:bool= false)const |
| String | texture_get_path(texture:RID)const |
| RID | texture_get_rd_texture(texture:RID, srgb:bool= false)const |
| RID | texture_proxy_create(base:RID) |
| void | texture_proxy_update(texture:RID, proxy_to:RID) |
| RID | texture_rd_create(rd_texture:RID, layer_type:TextureLayeredType= 0) |
| void | texture_replace(texture:RID, by_texture:RID) |
| void | texture_set_force_redraw_if_visible(texture:RID, enable:bool) |
| void | texture_set_path(texture:RID, path:String) |
| void | texture_set_size_override(texture:RID, width:int, height:int) |
| void | viewport_attach_camera(viewport:RID, camera:RID) |
| void | viewport_attach_canvas(viewport:RID, canvas:RID) |
| void | viewport_attach_to_screen(viewport:RID, rect:Rect2= Rect2(0, 0, 0, 0), screen:int= 0) |
| RID | viewport_create() |
| float | viewport_get_measured_render_time_cpu(viewport:RID)const |
| float | viewport_get_measured_render_time_gpu(viewport:RID)const |
| int | viewport_get_render_info(viewport:RID, type:ViewportRenderInfoType, info:ViewportRenderInfo) |
| RID | viewport_get_render_target(viewport:RID)const |
| RID | viewport_get_texture(viewport:RID)const |
| ViewportUpdateMode | viewport_get_update_mode(viewport:RID)const |
| void | viewport_remove_canvas(viewport:RID, canvas:RID) |
| void | viewport_set_active(viewport:RID, active:bool) |
| void | viewport_set_anisotropic_filtering_level(viewport:RID, anisotropic_filtering_level:ViewportAnisotropicFiltering) |
| void | viewport_set_canvas_cull_mask(viewport:RID, canvas_cull_mask:int) |
| void | viewport_set_canvas_stacking(viewport:RID, canvas:RID, layer:int, sublayer:int) |
| void | viewport_set_canvas_transform(viewport:RID, canvas:RID, offset:Transform2D) |
| void | viewport_set_clear_mode(viewport:RID, clear_mode:ViewportClearMode) |
| void | viewport_set_debug_draw(viewport:RID, draw:ViewportDebugDraw) |
| void | viewport_set_default_canvas_item_texture_filter(viewport:RID, filter:CanvasItemTextureFilter) |
| void | viewport_set_default_canvas_item_texture_repeat(viewport:RID, repeat:CanvasItemTextureRepeat) |
| void | viewport_set_disable_2d(viewport:RID, disable:bool) |
| void | viewport_set_disable_3d(viewport:RID, disable:bool) |
| void | viewport_set_environment_mode(viewport:RID, mode:ViewportEnvironmentMode) |
| void | viewport_set_fsr_sharpness(viewport:RID, sharpness:float) |
| void | viewport_set_global_canvas_transform(viewport:RID, transform:Transform2D) |
| void | viewport_set_measure_render_time(viewport:RID, enable:bool) |
| void | viewport_set_msaa_2d(viewport:RID, msaa:ViewportMSAA) |
| void | viewport_set_msaa_3d(viewport:RID, msaa:ViewportMSAA) |
| void | viewport_set_occlusion_culling_build_quality(quality:ViewportOcclusionCullingBuildQuality) |
| void | viewport_set_occlusion_rays_per_thread(rays_per_thread:int) |
| void | viewport_set_parent_viewport(viewport:RID, parent_viewport:RID) |
| void | viewport_set_positional_shadow_atlas_quadrant_subdivision(viewport:RID, quadrant:int, subdivision:int) |
| void | viewport_set_positional_shadow_atlas_size(viewport:RID, size:int, use_16_bits:bool= false) |
| void | viewport_set_render_direct_to_screen(viewport:RID, enabled:bool) |
| void | viewport_set_scaling_3d_mode(viewport:RID, scaling_3d_mode:ViewportScaling3DMode) |
| void | viewport_set_scaling_3d_scale(viewport:RID, scale:float) |
| void | viewport_set_scenario(viewport:RID, scenario:RID) |
| void | viewport_set_screen_space_aa(viewport:RID, mode:ViewportScreenSpaceAA) |
| void | viewport_set_sdf_oversize_and_scale(viewport:RID, oversize:ViewportSDFOversize, scale:ViewportSDFScale) |
| void | viewport_set_size(viewport:RID, width:int, height:int) |
| void | viewport_set_snap_2d_transforms_to_pixel(viewport:RID, enabled:bool) |
| void | viewport_set_snap_2d_vertices_to_pixel(viewport:RID, enabled:bool) |
| void | viewport_set_texture_mipmap_bias(viewport:RID, mipmap_bias:float) |
| void | viewport_set_transparent_background(viewport:RID, enabled:bool) |
| void | viewport_set_update_mode(viewport:RID, update_mode:ViewportUpdateMode) |
| void | viewport_set_use_debanding(viewport:RID, enable:bool) |
| void | viewport_set_use_hdr_2d(viewport:RID, enabled:bool) |
| void | viewport_set_use_occlusion_culling(viewport:RID, enable:bool) |
| void | viewport_set_use_taa(viewport:RID, enable:bool) |
| void | viewport_set_use_xr(viewport:RID, use_xr:bool) |
| void | viewport_set_vrs_mode(viewport:RID, mode:ViewportVRSMode) |
| void | viewport_set_vrs_texture(viewport:RID, texture:RID) |
| void | viewport_set_vrs_update_mode(viewport:RID, mode:ViewportVRSUpdateMode) |
| RID | visibility_notifier_create() |
| void | visibility_notifier_set_aabb(notifier:RID, aabb:AABB) |
| void | visibility_notifier_set_callbacks(notifier:RID, enter_callable:Callable, exit_callable:Callable) |
| void | voxel_gi_allocate_data(voxel_gi:RID, to_cell_xform:Transform3D, aabb:AABB, octree_size:Vector3i, octree_cells:PackedByteArray, data_cells:PackedByteArray, distance_field:PackedByteArray, level_counts:PackedInt32Array) |
| RID | voxel_gi_create() |
| PackedByteArray | voxel_gi_get_data_cells(voxel_gi:RID)const |
| PackedByteArray | voxel_gi_get_distance_field(voxel_gi:RID)const |
| PackedInt32Array | voxel_gi_get_level_counts(voxel_gi:RID)const |
| PackedByteArray | voxel_gi_get_octree_cells(voxel_gi:RID)const |
| Vector3i | voxel_gi_get_octree_size(voxel_gi:RID)const |
| Transform3D | voxel_gi_get_to_cell_xform(voxel_gi:RID)const |
| void | voxel_gi_set_baked_exposure_normalization(voxel_gi:RID, baked_exposure:float) |
| void | voxel_gi_set_bias(voxel_gi:RID, bias:float) |
| void | voxel_gi_set_dynamic_range(voxel_gi:RID, range:float) |
| void | voxel_gi_set_energy(voxel_gi:RID, energy:float) |
| void | voxel_gi_set_interior(voxel_gi:RID, enable:bool) |
| void | voxel_gi_set_normal_bias(voxel_gi:RID, bias:float) |
| void | voxel_gi_set_propagation(voxel_gi:RID, amount:float) |
| void | voxel_gi_set_quality(quality:VoxelGIQuality) |
| void | voxel_gi_set_use_two_bounces(voxel_gi:RID, enable:bool) |

Array[Image]
bake_render_uv2(base:RID, material_overrides:Array[RID], image_size:Vector2i)
void
call_on_render_thread(callable:Callable)
camera_attributes_create()
void
camera_attributes_set_auto_exposure(camera_attributes:RID, enable:bool, min_sensitivity:float, max_sensitivity:float, speed:float, scale:float)
void
camera_attributes_set_dof_blur(camera_attributes:RID, far_enable:bool, far_distance:float, far_transition:float, near_enable:bool, near_distance:float, near_transition:float, amount:float)
void
camera_attributes_set_dof_blur_bokeh_shape(shape:DOFBokehShape)
void
camera_attributes_set_dof_blur_quality(quality:DOFBlurQuality, use_jitter:bool)
void
camera_attributes_set_exposure(camera_attributes:RID, multiplier:float, normalization:float)
camera_create()
void
camera_set_camera_attributes(camera:RID, effects:RID)
void
camera_set_compositor(camera:RID, compositor:RID)
void
camera_set_cull_mask(camera:RID, layers:int)
void
camera_set_environment(camera:RID, env:RID)
void
camera_set_frustum(camera:RID, size:float, offset:Vector2, z_near:float, z_far:float)
void
camera_set_orthogonal(camera:RID, size:float, z_near:float, z_far:float)
void
camera_set_perspective(camera:RID, fovy_degrees:float, z_near:float, z_far:float)
void
camera_set_transform(camera:RID, transform:Transform3D)
void
camera_set_use_vertical_aspect(camera:RID, enable:bool)
canvas_create()
void
canvas_item_add_animation_slice(item:RID, animation_length:float, slice_begin:float, slice_end:float, offset:float= 0.0)
void
canvas_item_add_circle(item:RID, pos:Vector2, radius:float, color:Color, antialiased:bool= false)
void
canvas_item_add_clip_ignore(item:RID, ignore:bool)
void
canvas_item_add_ellipse(item:RID, pos:Vector2, major:float, minor:float, color:Color, antialiased:bool= false)
void
canvas_item_add_lcd_texture_rect_region(item:RID, rect:Rect2, texture:RID, src_rect:Rect2, modulate:Color)
void
canvas_item_add_line(item:RID, from:Vector2, to:Vector2, color:Color, width:float= -1.0, antialiased:bool= false)
void
canvas_item_add_mesh(item:RID, mesh:RID, transform:Transform2D= Transform2D(1, 0, 0, 1, 0, 0), modulate:Color= Color(1, 1, 1, 1), texture:RID= RID())
void
canvas_item_add_msdf_texture_rect_region(item:RID, rect:Rect2, texture:RID, src_rect:Rect2, modulate:Color= Color(1, 1, 1, 1), outline_size:int= 0, px_range:float= 1.0, scale:float= 1.0)
void
canvas_item_add_multiline(item:RID, points:PackedVector2Array, colors:PackedColorArray, width:float= -1.0, antialiased:bool= false)
void
canvas_item_add_multimesh(item:RID, mesh:RID, texture:RID= RID())
void
canvas_item_add_nine_patch(item:RID, rect:Rect2, source:Rect2, texture:RID, topleft:Vector2, bottomright:Vector2, x_axis_mode:NinePatchAxisMode= 0, y_axis_mode:NinePatchAxisMode= 0, draw_center:bool= true, modulate:Color= Color(1, 1, 1, 1))
void
canvas_item_add_particles(item:RID, particles:RID, texture:RID)
void
canvas_item_add_polygon(item:RID, points:PackedVector2Array, colors:PackedColorArray, uvs:PackedVector2Array= PackedVector2Array(), texture:RID= RID())
void
canvas_item_add_polyline(item:RID, points:PackedVector2Array, colors:PackedColorArray, width:float= -1.0, antialiased:bool= false)
void
canvas_item_add_primitive(item:RID, points:PackedVector2Array, colors:PackedColorArray, uvs:PackedVector2Array, texture:RID)
void
canvas_item_add_rect(item:RID, rect:Rect2, color:Color, antialiased:bool= false)
void
canvas_item_add_set_transform(item:RID, transform:Transform2D)
void
canvas_item_add_texture_rect(item:RID, rect:Rect2, texture:RID, tile:bool= false, modulate:Color= Color(1, 1, 1, 1), transpose:bool= false)
void
canvas_item_add_texture_rect_region(item:RID, rect:Rect2, texture:RID, src_rect:Rect2, modulate:Color= Color(1, 1, 1, 1), transpose:bool= false, clip_uv:bool= true)
void
canvas_item_add_triangle_array(item:RID, indices:PackedInt32Array, points:PackedVector2Array, colors:PackedColorArray, uvs:PackedVector2Array= PackedVector2Array(), bones:PackedInt32Array= PackedInt32Array(), weights:PackedFloat32Array= PackedFloat32Array(), texture:RID= RID(), count:int= -1)
void
canvas_item_attach_skeleton(item:RID, skeleton:RID)
void
canvas_item_clear(item:RID)
canvas_item_create()
Variant
canvas_item_get_instance_shader_parameter(instance:RID, parameter:StringName)const
Variant
canvas_item_get_instance_shader_parameter_default_value(instance:RID, parameter:StringName)const
Array[Dictionary]
canvas_item_get_instance_shader_parameter_list(instance:RID)const
void
canvas_item_reset_physics_interpolation(item:RID)
void
canvas_item_set_canvas_group_mode(item:RID, mode:CanvasGroupMode, clear_margin:float= 5.0, fit_empty:bool= false, fit_margin:float= 0.0, blur_mipmaps:bool= false)
void
canvas_item_set_clip(item:RID, clip:bool)
void
canvas_item_set_copy_to_backbuffer(item:RID, enabled:bool, rect:Rect2)
void
canvas_item_set_custom_rect(item:RID, use_custom_rect:bool, rect:Rect2= Rect2(0, 0, 0, 0))
void
canvas_item_set_default_texture_filter(item:RID, filter:CanvasItemTextureFilter)
void
canvas_item_set_default_texture_repeat(item:RID, repeat:CanvasItemTextureRepeat)
void
canvas_item_set_distance_field_mode(item:RID, enabled:bool)
void
canvas_item_set_draw_behind_parent(item:RID, enabled:bool)
void
canvas_item_set_draw_index(item:RID, index:int)
void
canvas_item_set_instance_shader_parameter(instance:RID, parameter:StringName, value:Variant)
void
canvas_item_set_interpolated(item:RID, interpolated:bool)
void
canvas_item_set_light_mask(item:RID, mask:int)
void
canvas_item_set_material(item:RID, material:RID)
void
canvas_item_set_modulate(item:RID, color:Color)
void
canvas_item_set_parent(item:RID, parent:RID)
void
canvas_item_set_self_modulate(item:RID, color:Color)
void
canvas_item_set_sort_children_by_y(item:RID, enabled:bool)
void
canvas_item_set_transform(item:RID, transform:Transform2D)
void
canvas_item_set_use_parent_material(item:RID, enabled:bool)
void
canvas_item_set_visibility_layer(item:RID, visibility_layer:int)
void
canvas_item_set_visibility_notifier(item:RID, enable:bool, area:Rect2, enter_callable:Callable, exit_callable:Callable)
void
canvas_item_set_visible(item:RID, visible:bool)
void
canvas_item_set_z_as_relative_to_parent(item:RID, enabled:bool)
void
canvas_item_set_z_index(item:RID, z_index:int)
void
canvas_item_transform_physics_interpolation(item:RID, transform:Transform2D)
void
canvas_light_attach_to_canvas(light:RID, canvas:RID)
canvas_light_create()
void
canvas_light_occluder_attach_to_canvas(occluder:RID, canvas:RID)
canvas_light_occluder_create()
void
canvas_light_occluder_reset_physics_interpolation(occluder:RID)
void
canvas_light_occluder_set_as_sdf_collision(occluder:RID, enable:bool)
void
canvas_light_occluder_set_enabled(occluder:RID, enabled:bool)
void
canvas_light_occluder_set_interpolated(occluder:RID, interpolated:bool)
void
canvas_light_occluder_set_light_mask(occluder:RID, mask:int)
void
canvas_light_occluder_set_polygon(occluder:RID, polygon:RID)
void
canvas_light_occluder_set_transform(occluder:RID, transform:Transform2D)
void
canvas_light_occluder_transform_physics_interpolation(occluder:RID, transform:Transform2D)
void
canvas_light_reset_physics_interpolation(light:RID)
void
canvas_light_set_blend_mode(light:RID, mode:CanvasLightBlendMode)
void
canvas_light_set_color(light:RID, color:Color)
void
canvas_light_set_enabled(light:RID, enabled:bool)
void
canvas_light_set_energy(light:RID, energy:float)
void
canvas_light_set_height(light:RID, height:float)
void
canvas_light_set_interpolated(light:RID, interpolated:bool)
void
canvas_light_set_item_cull_mask(light:RID, mask:int)
void
canvas_light_set_item_shadow_cull_mask(light:RID, mask:int)
void
canvas_light_set_layer_range(light:RID, min_layer:int, max_layer:int)
void
canvas_light_set_mode(light:RID, mode:CanvasLightMode)
void
canvas_light_set_shadow_color(light:RID, color:Color)
void
canvas_light_set_shadow_enabled(light:RID, enabled:bool)
void
canvas_light_set_shadow_filter(light:RID, filter:CanvasLightShadowFilter)
void
canvas_light_set_shadow_smooth(light:RID, smooth:float)
void
canvas_light_set_texture(light:RID, texture:RID)
void
canvas_light_set_texture_offset(light:RID, offset:Vector2)
void
canvas_light_set_texture_scale(light:RID, scale:float)
void
canvas_light_set_transform(light:RID, transform:Transform2D)
void
canvas_light_set_z_range(light:RID, min_z:int, max_z:int)
void
canvas_light_transform_physics_interpolation(light:RID, transform:Transform2D)
canvas_occluder_polygon_create()
void
canvas_occluder_polygon_set_cull_mode(occluder_polygon:RID, mode:CanvasOccluderPolygonCullMode)
void
canvas_occluder_polygon_set_shape(occluder_polygon:RID, shape:PackedVector2Array, closed:bool)
void
canvas_set_disable_scale(disable:bool)
void
canvas_set_item_mirroring(canvas:RID, item:RID, mirroring:Vector2)
void
canvas_set_item_repeat(item:RID, repeat_size:Vector2, repeat_times:int)
void
canvas_set_modulate(canvas:RID, color:Color)
void
canvas_set_shadow_texture_size(size:int)
canvas_texture_create()
void
canvas_texture_set_channel(canvas_texture:RID, channel:CanvasTextureChannel, texture:RID)
void
canvas_texture_set_shading_parameters(canvas_texture:RID, base_color:Color, shininess:float)
void
canvas_texture_set_texture_filter(canvas_texture:RID, filter:CanvasItemTextureFilter)
void
canvas_texture_set_texture_repeat(canvas_texture:RID, repeat:CanvasItemTextureRepeat)
compositor_create()
compositor_effect_create()
void
compositor_effect_set_callback(effect:RID, callback_type:CompositorEffectCallbackType, callback:Callable)
void
compositor_effect_set_enabled(effect:RID, enabled:bool)
void
compositor_effect_set_flag(effect:RID, flag:CompositorEffectFlags, set:bool)
void
compositor_set_compositor_effects(compositor:RID, effects:Array[RID])
RenderingDevice
create_local_rendering_device()const
Rect2
debug_canvas_item_get_rect(item:RID)
decal_create()
void
decal_set_albedo_mix(decal:RID, albedo_mix:float)
void
decal_set_cull_mask(decal:RID, mask:int)
void
decal_set_distance_fade(decal:RID, enabled:bool, begin:float, length:float)
void
decal_set_emission_energy(decal:RID, energy:float)
void
decal_set_fade(decal:RID, above:float, below:float)
void
decal_set_modulate(decal:RID, color:Color)
void
decal_set_normal_fade(decal:RID, fade:float)
void
decal_set_size(decal:RID, size:Vector3)
void
decal_set_texture(decal:RID, type:DecalTexture, texture:RID)
void
decals_set_filter(filter:DecalFilter)
directional_light_create()
void
directional_shadow_atlas_set_size(size:int, is_16bits:bool)
void
directional_soft_shadow_filter_set_quality(quality:ShadowQuality)
Image
environment_bake_panorama(environment:RID, bake_irradiance:bool, size:Vector2i)
environment_create()
void
environment_glow_set_use_bicubic_upscale(enable:bool)
void
environment_set_adjustment(env:RID, enable:bool, brightness:float, contrast:float, saturation:float, use_1d_color_correction:bool, color_correction:RID)
void
environment_set_ambient_light(env:RID, color:Color, ambient:EnvironmentAmbientSource= 0, energy:float= 1.0, sky_contribution:float= 0.0, reflection_source:EnvironmentReflectionSource= 0)
void
environment_set_background(env:RID, bg:EnvironmentBG)
void
environment_set_bg_color(env:RID, color:Color)
void
environment_set_bg_energy(env:RID, multiplier:float, exposure_value:float)
void
environment_set_camera_id(env:RID, id:int)
void
environment_set_canvas_max_layer(env:RID, max_layer:int)
void
environment_set_fog(env:RID, enable:bool, light_color:Color, light_energy:float, sun_scatter:float, density:float, height:float, height_density:float, aerial_perspective:float, sky_affect:float, fog_mode:EnvironmentFogMode= 0)
void
environment_set_fog_depth(env:RID, curve:float, begin:float, end:float)
void
environment_set_glow(env:RID, enable:bool, levels:PackedFloat32Array, intensity:float, strength:float, mix:float, bloom_threshold:float, blend_mode:EnvironmentGlowBlendMode, hdr_bleed_threshold:float, hdr_bleed_scale:float, hdr_luminance_cap:float, glow_map_strength:float, glow_map:RID)
void
environment_set_sdfgi(env:RID, enable:bool, cascades:int, min_cell_size:float, y_scale:EnvironmentSDFGIYScale, use_occlusion:bool, bounce_feedback:float, read_sky:bool, energy:float, normal_bias:float, probe_bias:float)
void
environment_set_sdfgi_frames_to_converge(frames:EnvironmentSDFGIFramesToConverge)
void
environment_set_sdfgi_frames_to_update_light(frames:EnvironmentSDFGIFramesToUpdateLight)
void
environment_set_sdfgi_ray_count(ray_count:EnvironmentSDFGIRayCount)
void
environment_set_sky(env:RID, sky:RID)
void
environment_set_sky_custom_fov(env:RID, scale:float)
void
environment_set_sky_orientation(env:RID, orientation:Basis)
void
environment_set_ssao(env:RID, enable:bool, radius:float, intensity:float, power:float, detail:float, horizon:float, sharpness:float, light_affect:float, ao_channel_affect:float)
void
environment_set_ssao_quality(quality:EnvironmentSSAOQuality, half_size:bool, adaptive_target:float, blur_passes:int, fadeout_from:float, fadeout_to:float)
void
environment_set_ssil_quality(quality:EnvironmentSSILQuality, half_size:bool, adaptive_target:float, blur_passes:int, fadeout_from:float, fadeout_to:float)
void
environment_set_ssr(env:RID, enable:bool, max_steps:int, fade_in:float, fade_out:float, depth_tolerance:float)
void
environment_set_ssr_half_size(half_size:bool)
void
environment_set_ssr_roughness_quality(quality:EnvironmentSSRRoughnessQuality)
void
environment_set_tonemap(env:RID, tone_mapper:EnvironmentToneMapper, exposure:float, white:float)
void
environment_set_tonemap_agx_contrast(env:RID, agx_contrast:float)
void
environment_set_volumetric_fog(env:RID, enable:bool, density:float, albedo:Color, emission:Color, emission_energy:float, anisotropy:float, length:float, p_detail_spread:float, gi_inject:float, temporal_reprojection:bool, temporal_reprojection_amount:float, ambient_inject:float, sky_affect:float)
void
environment_set_volumetric_fog_filter_active(active:bool)
void
environment_set_volumetric_fog_volume_size(size:int, depth:int)
fog_volume_create()
void
fog_volume_set_material(fog_volume:RID, material:RID)
void
fog_volume_set_shape(fog_volume:RID, shape:FogVolumeShape)
void
fog_volume_set_size(fog_volume:RID, size:Vector3)
void
force_draw(swap_buffers:bool= true, frame_step:float= 0.0)
void
force_sync()
void
free_rid(rid:RID)
String
get_current_rendering_driver_name()const
String
get_current_rendering_method()const
Color
get_default_clear_color()
float
get_frame_setup_time_cpu()const
RenderingDevice
get_rendering_device()const
get_rendering_info(info:RenderingInfo)
Array[Dictionary]
get_shader_parameter_list(shader:RID)const
get_test_cube()
get_test_texture()
String
get_video_adapter_api_version()const
String
get_video_adapter_name()const
DeviceType
get_video_adapter_type()const
String
get_video_adapter_vendor()const
get_white_texture()
void
gi_set_use_half_resolution(half_resolution:bool)
void
global_shader_parameter_add(name:StringName, type:GlobalShaderParameterType, default_value:Variant)
Variant
global_shader_parameter_get(name:StringName)const
Array[StringName]
global_shader_parameter_get_list()const
GlobalShaderParameterType
global_shader_parameter_get_type(name:StringName)const
void
global_shader_parameter_remove(name:StringName)
void
global_shader_parameter_set(name:StringName, value:Variant)
void
global_shader_parameter_set_override(name:StringName, value:Variant)
bool
has_changed()const
bool
has_feature(feature:Features)const
bool
has_os_feature(feature:String)const
void
instance_attach_object_instance_id(instance:RID, id:int)
void
instance_attach_skeleton(instance:RID, skeleton:RID)
instance_create()
instance_create2(base:RID, scenario:RID)
Variant
instance_geometry_get_shader_parameter(instance:RID, parameter:StringName)const
Variant
instance_geometry_get_shader_parameter_default_value(instance:RID, parameter:StringName)const
Array[Dictionary]
instance_geometry_get_shader_parameter_list(instance:RID)const
void
instance_geometry_set_cast_shadows_setting(instance:RID, shadow_casting_setting:ShadowCastingSetting)
void
instance_geometry_set_flag(instance:RID, flag:InstanceFlags, enabled:bool)
void
instance_geometry_set_lightmap(instance:RID, lightmap:RID, lightmap_uv_scale:Rect2, lightmap_slice:int)
void
instance_geometry_set_lod_bias(instance:RID, lod_bias:float)
void
instance_geometry_set_material_overlay(instance:RID, material:RID)
void
instance_geometry_set_material_override(instance:RID, material:RID)
void
instance_geometry_set_shader_parameter(instance:RID, parameter:StringName, value:Variant)
void
instance_geometry_set_transparency(instance:RID, transparency:float)
void
instance_geometry_set_visibility_range(instance:RID, min:float, max:float, min_margin:float, max_margin:float, fade_mode:VisibilityRangeFadeMode)
void
instance_set_base(instance:RID, base:RID)
void
instance_set_blend_shape_weight(instance:RID, shape:int, weight:float)
void
instance_set_custom_aabb(instance:RID, aabb:AABB)
void
instance_set_extra_visibility_margin(instance:RID, margin:float)
void
instance_set_ignore_culling(instance:RID, enabled:bool)
void
instance_set_layer_mask(instance:RID, mask:int)
void
instance_set_pivot_data(instance:RID, sorting_offset:float, use_aabb_center:bool)
void
instance_set_scenario(instance:RID, scenario:RID)
void
instance_set_surface_override_material(instance:RID, surface:int, material:RID)
void
instance_set_transform(instance:RID, transform:Transform3D)
void
instance_set_visibility_parent(instance:RID, parent:RID)
void
instance_set_visible(instance:RID, visible:bool)
void
instance_teleport(instance:RID)
PackedInt64Array
instances_cull_aabb(aabb:AABB, scenario:RID= RID())const
PackedInt64Array
instances_cull_convex(convex:Array[Plane], scenario:RID= RID())const
PackedInt64Array
instances_cull_ray(from:Vector3, to:Vector3, scenario:RID= RID())const
bool
is_on_render_thread()
void
light_directional_set_blend_splits(light:RID, enable:bool)
void
light_directional_set_shadow_mode(light:RID, mode:LightDirectionalShadowMode)
void
light_directional_set_sky_mode(light:RID, mode:LightDirectionalSkyMode)
void
light_omni_set_shadow_mode(light:RID, mode:LightOmniShadowMode)
void
light_projectors_set_filter(filter:LightProjectorFilter)
void
light_set_bake_mode(light:RID, bake_mode:LightBakeMode)
void
light_set_color(light:RID, color:Color)
void
light_set_cull_mask(light:RID, mask:int)
void
light_set_distance_fade(decal:RID, enabled:bool, begin:float, shadow:float, length:float)
void
light_set_max_sdfgi_cascade(light:RID, cascade:int)
void
light_set_negative(light:RID, enable:bool)
void
light_set_param(light:RID, param:LightParam, value:float)
void
light_set_projector(light:RID, texture:RID)
void
light_set_reverse_cull_face_mode(light:RID, enabled:bool)
void
light_set_shadow(light:RID, enabled:bool)
void
light_set_shadow_caster_mask(light:RID, mask:int)
lightmap_create()
PackedInt32Array
lightmap_get_probe_capture_bsp_tree(lightmap:RID)const
PackedVector3Array
lightmap_get_probe_capture_points(lightmap:RID)const
PackedColorArray
lightmap_get_probe_capture_sh(lightmap:RID)const
PackedInt32Array
lightmap_get_probe_capture_tetrahedra(lightmap:RID)const
void
lightmap_set_baked_exposure_normalization(lightmap:RID, baked_exposure:float)
void
lightmap_set_probe_bounds(lightmap:RID, bounds:AABB)
void
lightmap_set_probe_capture_data(lightmap:RID, points:PackedVector3Array, point_sh:PackedColorArray, tetrahedra:PackedInt32Array, bsp_tree:PackedInt32Array)
void
lightmap_set_probe_capture_update_speed(speed:float)
void
lightmap_set_probe_interior(lightmap:RID, interior:bool)
void
lightmap_set_textures(lightmap:RID, light:RID, uses_sh:bool)
void
lightmaps_set_bicubic_filter(enable:bool)
make_sphere_mesh(latitudes:int, longitudes:int, radius:float)
material_create()
Variant
material_get_param(material:RID, parameter:StringName)const
void
material_set_next_pass(material:RID, next_material:RID)
void
material_set_param(material:RID, parameter:StringName, value:Variant)
void
material_set_render_priority(material:RID, priority:int)
void
material_set_shader(shader_material:RID, shader:RID)
void
material_set_use_debanding(enable:bool)
void
mesh_add_surface(mesh:RID, surface:Dictionary)
void
mesh_add_surface_from_arrays(mesh:RID, primitive:PrimitiveType, arrays:Array, blend_shapes:Array= [], lods:Dictionary= {}, compress_format:BitField[ArrayFormat] = 0)
void
mesh_clear(mesh:RID)
mesh_create()
mesh_create_from_surfaces(surfaces:Array[Dictionary], blend_shape_count:int= 0)
mesh_get_blend_shape_count(mesh:RID)const
BlendShapeMode
mesh_get_blend_shape_mode(mesh:RID)const
AABB
mesh_get_custom_aabb(mesh:RID)const
Dictionary
mesh_get_surface(mesh:RID, surface:int)
mesh_get_surface_count(mesh:RID)const
void
mesh_set_blend_shape_mode(mesh:RID, mode:BlendShapeMode)
void
mesh_set_custom_aabb(mesh:RID, aabb:AABB)
void
mesh_set_shadow_mesh(mesh:RID, shadow_mesh:RID)
Array
mesh_surface_get_arrays(mesh:RID, surface:int)const
Array[Array]
mesh_surface_get_blend_shape_arrays(mesh:RID, surface:int)const
mesh_surface_get_format_attribute_stride(format:BitField[ArrayFormat], vertex_count:int)const
mesh_surface_get_format_index_stride(format:BitField[ArrayFormat], vertex_count:int)const
mesh_surface_get_format_normal_tangent_stride(format:BitField[ArrayFormat], vertex_count:int)const
mesh_surface_get_format_offset(format:BitField[ArrayFormat], vertex_count:int, array_index:int)const
mesh_surface_get_format_skin_stride(format:BitField[ArrayFormat], vertex_count:int)const
mesh_surface_get_format_vertex_stride(format:BitField[ArrayFormat], vertex_count:int)const
mesh_surface_get_material(mesh:RID, surface:int)const
void
mesh_surface_remove(mesh:RID, surface:int)
void
mesh_surface_set_material(mesh:RID, surface:int, material:RID)
void
mesh_surface_update_attribute_region(mesh:RID, surface:int, offset:int, data:PackedByteArray)
void
mesh_surface_update_index_region(mesh:RID, surface:int, offset:int, data:PackedByteArray)
void
mesh_surface_update_skin_region(mesh:RID, surface:int, offset:int, data:PackedByteArray)
void
mesh_surface_update_vertex_region(mesh:RID, surface:int, offset:int, data:PackedByteArray)
void
multimesh_allocate_data(multimesh:RID, instances:int, transform_format:MultimeshTransformFormat, color_format:bool= false, custom_data_format:bool= false, use_indirect:bool= false)
multimesh_create()
AABB
multimesh_get_aabb(multimesh:RID)const
PackedFloat32Array
multimesh_get_buffer(multimesh:RID)const
multimesh_get_buffer_rd_rid(multimesh:RID)const
multimesh_get_command_buffer_rd_rid(multimesh:RID)const
AABB
multimesh_get_custom_aabb(multimesh:RID)const
multimesh_get_instance_count(multimesh:RID)const
multimesh_get_mesh(multimesh:RID)const
multimesh_get_visible_instances(multimesh:RID)const
Color
multimesh_instance_get_color(multimesh:RID, index:int)const
Color
multimesh_instance_get_custom_data(multimesh:RID, index:int)const
Transform3D
multimesh_instance_get_transform(multimesh:RID, index:int)const
Transform2D
multimesh_instance_get_transform_2d(multimesh:RID, index:int)const
void
multimesh_instance_reset_physics_interpolation(multimesh:RID, index:int)
void
multimesh_instance_set_color(multimesh:RID, index:int, color:Color)
void
multimesh_instance_set_custom_data(multimesh:RID, index:int, custom_data:Color)
void
multimesh_instance_set_transform(multimesh:RID, index:int, transform:Transform3D)
void
multimesh_instance_set_transform_2d(multimesh:RID, index:int, transform:Transform2D)
void
multimesh_instances_reset_physics_interpolation(multimesh:RID)
void
multimesh_set_buffer(multimesh:RID, buffer:PackedFloat32Array)
void
multimesh_set_buffer_interpolated(multimesh:RID, buffer:PackedFloat32Array, buffer_previous:PackedFloat32Array)
void
multimesh_set_custom_aabb(multimesh:RID, aabb:AABB)
void
multimesh_set_mesh(multimesh:RID, mesh:RID)
void
multimesh_set_physics_interpolated(multimesh:RID, interpolated:bool)
void
multimesh_set_physics_interpolation_quality(multimesh:RID, quality:MultimeshPhysicsInterpolationQuality)
void
multimesh_set_visible_instances(multimesh:RID, visible:int)
occluder_create()
void
occluder_set_mesh(occluder:RID, vertices:PackedVector3Array, indices:PackedInt32Array)
omni_light_create()
particles_collision_create()
void
particles_collision_height_field_update(particles_collision:RID)
void
particles_collision_set_attractor_attenuation(particles_collision:RID, curve:float)
void
particles_collision_set_attractor_directionality(particles_collision:RID, amount:float)
void
particles_collision_set_attractor_strength(particles_collision:RID, strength:float)
void
particles_collision_set_box_extents(particles_collision:RID, extents:Vector3)
void
particles_collision_set_collision_type(particles_collision:RID, type:ParticlesCollisionType)
void
particles_collision_set_cull_mask(particles_collision:RID, mask:int)
void
particles_collision_set_field_texture(particles_collision:RID, texture:RID)
void
particles_collision_set_height_field_mask(particles_collision:RID, mask:int)
void
particles_collision_set_height_field_resolution(particles_collision:RID, resolution:ParticlesCollisionHeightfieldResolution)
void
particles_collision_set_sphere_radius(particles_collision:RID, radius:float)
particles_create()
void
particles_emit(particles:RID, transform:Transform3D, velocity:Vector3, color:Color, custom:Color, emit_flags:int)
AABB
particles_get_current_aabb(particles:RID)
bool
particles_get_emitting(particles:RID)
bool
particles_is_inactive(particles:RID)
void
particles_request_process(particles:RID)
void
particles_request_process_time(particles:RID, time:float)
void
particles_restart(particles:RID)
void
particles_set_amount(particles:RID, amount:int)
void
particles_set_amount_ratio(particles:RID, ratio:float)
void
particles_set_collision_base_size(particles:RID, size:float)
void
particles_set_custom_aabb(particles:RID, aabb:AABB)
void
particles_set_draw_order(particles:RID, order:ParticlesDrawOrder)
void
particles_set_draw_pass_mesh(particles:RID, pass:int, mesh:RID)
void
particles_set_draw_passes(particles:RID, count:int)
void
particles_set_emission_transform(particles:RID, transform:Transform3D)
void
particles_set_emitter_velocity(particles:RID, velocity:Vector3)
void
particles_set_emitting(particles:RID, emitting:bool)
void
particles_set_explosiveness_ratio(particles:RID, ratio:float)
void
particles_set_fixed_fps(particles:RID, fps:int)
void
particles_set_fractional_delta(particles:RID, enable:bool)
void
particles_set_interp_to_end(particles:RID, factor:float)
void
particles_set_interpolate(particles:RID, enable:bool)
void
particles_set_lifetime(particles:RID, lifetime:float)
void
particles_set_mode(particles:RID, mode:ParticlesMode)
void
particles_set_one_shot(particles:RID, one_shot:bool)
void
particles_set_pre_process_time(particles:RID, time:float)
void
particles_set_process_material(particles:RID, material:RID)
void
particles_set_randomness_ratio(particles:RID, ratio:float)
void
particles_set_speed_scale(particles:RID, scale:float)
void
particles_set_subemitter(particles:RID, subemitter_particles:RID)
void
particles_set_trail_bind_poses(particles:RID, bind_poses:Array[Transform3D])
void
particles_set_trails(particles:RID, enable:bool, length_sec:float)
void
particles_set_transform_align(particles:RID, align:ParticlesTransformAlign)
void
particles_set_use_local_coordinates(particles:RID, enable:bool)
void
positional_soft_shadow_filter_set_quality(quality:ShadowQuality)
reflection_probe_create()
void
reflection_probe_set_ambient_color(probe:RID, color:Color)
void
reflection_probe_set_ambient_energy(probe:RID, energy:float)
void
reflection_probe_set_ambient_mode(probe:RID, mode:ReflectionProbeAmbientMode)
void
reflection_probe_set_as_interior(probe:RID, enable:bool)
void
reflection_probe_set_blend_distance(probe:RID, blend_distance:float)
void
reflection_probe_set_cull_mask(probe:RID, layers:int)
void
reflection_probe_set_enable_box_projection(probe:RID, enable:bool)
void
reflection_probe_set_enable_shadows(probe:RID, enable:bool)
void
reflection_probe_set_intensity(probe:RID, intensity:float)
void
reflection_probe_set_max_distance(probe:RID, distance:float)
void
reflection_probe_set_mesh_lod_threshold(probe:RID, pixels:float)
void
reflection_probe_set_origin_offset(probe:RID, offset:Vector3)
void
reflection_probe_set_reflection_mask(probe:RID, layers:int)
void
reflection_probe_set_resolution(probe:RID, resolution:int)
void
reflection_probe_set_size(probe:RID, size:Vector3)
void
reflection_probe_set_update_mode(probe:RID, mode:ReflectionProbeUpdateMode)
void
request_frame_drawn_callback(callable:Callable)
scenario_create()
void
scenario_set_camera_attributes(scenario:RID, effects:RID)
void
scenario_set_compositor(scenario:RID, compositor:RID)
void
scenario_set_environment(scenario:RID, environment:RID)
void
scenario_set_fallback_environment(scenario:RID, environment:RID)
void
screen_space_roughness_limiter_set_active(enable:bool, amount:float, limit:float)
void
set_boot_image(image:Image, color:Color, scale:bool, use_filter:bool= true)
void
set_boot_image_with_stretch(image:Image, color:Color, stretch_mode:SplashStretchMode, use_filter:bool= true)
void
set_debug_generate_wireframes(generate:bool)
void
set_default_clear_color(color:Color)
shader_create()
String
shader_get_code(shader:RID)const
shader_get_default_texture_parameter(shader:RID, name:StringName, index:int= 0)const
Variant
shader_get_parameter_default(shader:RID, name:StringName)const
void
shader_set_code(shader:RID, code:String)
void
shader_set_default_texture_parameter(shader:RID, name:StringName, texture:RID, index:int= 0)
void
shader_set_path_hint(shader:RID, path:String)
void
skeleton_allocate_data(skeleton:RID, bones:int, is_2d_skeleton:bool= false)
Transform3D
skeleton_bone_get_transform(skeleton:RID, bone:int)const
Transform2D
skeleton_bone_get_transform_2d(skeleton:RID, bone:int)const
void
skeleton_bone_set_transform(skeleton:RID, bone:int, transform:Transform3D)
void
skeleton_bone_set_transform_2d(skeleton:RID, bone:int, transform:Transform2D)
skeleton_create()
skeleton_get_bone_count(skeleton:RID)const
void
skeleton_set_base_transform_2d(skeleton:RID, base_transform:Transform2D)
Image
sky_bake_panorama(sky:RID, energy:float, bake_irradiance:bool, size:Vector2i)
sky_create()
void
sky_set_material(sky:RID, material:RID)
void
sky_set_mode(sky:RID, mode:SkyMode)
void
sky_set_radiance_size(sky:RID, radiance_size:int)
spot_light_create()
void
sub_surface_scattering_set_quality(quality:SubSurfaceScatteringQuality)
void
sub_surface_scattering_set_scale(scale:float, depth_scale:float)
texture_2d_create(image:Image)
Image
texture_2d_get(texture:RID)const
Image
texture_2d_layer_get(texture:RID, layer:int)const
texture_2d_layered_create(layers:Array[Image], layered_type:TextureLayeredType)
texture_2d_layered_placeholder_create(layered_type:TextureLayeredType)
texture_2d_placeholder_create()
void
texture_2d_update(texture:RID, image:Image, layer:int)
texture_3d_create(format:Format, width:int, height:int, depth:int, mipmaps:bool, data:Array[Image])
Array[Image]
texture_3d_get(texture:RID)const
texture_3d_placeholder_create()
void
texture_3d_update(texture:RID, data:Array[Image])
texture_create_from_native_handle(type:TextureType, format:Format, native_handle:int, width:int, height:int, depth:int, layers:int= 1, layered_type:TextureLayeredType= 0)
Format
texture_get_format(texture:RID)const
texture_get_native_handle(texture:RID, srgb:bool= false)const
String
texture_get_path(texture:RID)const
texture_get_rd_texture(texture:RID, srgb:bool= false)const
texture_proxy_create(base:RID)
void
texture_proxy_update(texture:RID, proxy_to:RID)
texture_rd_create(rd_texture:RID, layer_type:TextureLayeredType= 0)
void
texture_replace(texture:RID, by_texture:RID)
void
texture_set_force_redraw_if_visible(texture:RID, enable:bool)
void
texture_set_path(texture:RID, path:String)
void
texture_set_size_override(texture:RID, width:int, height:int)
void
viewport_attach_camera(viewport:RID, camera:RID)
void
viewport_attach_canvas(viewport:RID, canvas:RID)
void
viewport_attach_to_screen(viewport:RID, rect:Rect2= Rect2(0, 0, 0, 0), screen:int= 0)
viewport_create()
float
viewport_get_measured_render_time_cpu(viewport:RID)const
float
viewport_get_measured_render_time_gpu(viewport:RID)const
viewport_get_render_info(viewport:RID, type:ViewportRenderInfoType, info:ViewportRenderInfo)
viewport_get_render_target(viewport:RID)const
viewport_get_texture(viewport:RID)const
ViewportUpdateMode
viewport_get_update_mode(viewport:RID)const
void
viewport_remove_canvas(viewport:RID, canvas:RID)
void
viewport_set_active(viewport:RID, active:bool)
void
viewport_set_anisotropic_filtering_level(viewport:RID, anisotropic_filtering_level:ViewportAnisotropicFiltering)
void
viewport_set_canvas_cull_mask(viewport:RID, canvas_cull_mask:int)
void
viewport_set_canvas_stacking(viewport:RID, canvas:RID, layer:int, sublayer:int)
void
viewport_set_canvas_transform(viewport:RID, canvas:RID, offset:Transform2D)
void
viewport_set_clear_mode(viewport:RID, clear_mode:ViewportClearMode)
void
viewport_set_debug_draw(viewport:RID, draw:ViewportDebugDraw)
void
viewport_set_default_canvas_item_texture_filter(viewport:RID, filter:CanvasItemTextureFilter)
void
viewport_set_default_canvas_item_texture_repeat(viewport:RID, repeat:CanvasItemTextureRepeat)
void
viewport_set_disable_2d(viewport:RID, disable:bool)
void
viewport_set_disable_3d(viewport:RID, disable:bool)
void
viewport_set_environment_mode(viewport:RID, mode:ViewportEnvironmentMode)
void
viewport_set_fsr_sharpness(viewport:RID, sharpness:float)
void
viewport_set_global_canvas_transform(viewport:RID, transform:Transform2D)
void
viewport_set_measure_render_time(viewport:RID, enable:bool)
void
viewport_set_msaa_2d(viewport:RID, msaa:ViewportMSAA)
void
viewport_set_msaa_3d(viewport:RID, msaa:ViewportMSAA)
void
viewport_set_occlusion_culling_build_quality(quality:ViewportOcclusionCullingBuildQuality)
void
viewport_set_occlusion_rays_per_thread(rays_per_thread:int)
void
viewport_set_parent_viewport(viewport:RID, parent_viewport:RID)
void
viewport_set_positional_shadow_atlas_quadrant_subdivision(viewport:RID, quadrant:int, subdivision:int)
void
viewport_set_positional_shadow_atlas_size(viewport:RID, size:int, use_16_bits:bool= false)
void
viewport_set_render_direct_to_screen(viewport:RID, enabled:bool)
void
viewport_set_scaling_3d_mode(viewport:RID, scaling_3d_mode:ViewportScaling3DMode)
void
viewport_set_scaling_3d_scale(viewport:RID, scale:float)
void
viewport_set_scenario(viewport:RID, scenario:RID)
void
viewport_set_screen_space_aa(viewport:RID, mode:ViewportScreenSpaceAA)
void
viewport_set_sdf_oversize_and_scale(viewport:RID, oversize:ViewportSDFOversize, scale:ViewportSDFScale)
void
viewport_set_size(viewport:RID, width:int, height:int)
void
viewport_set_snap_2d_transforms_to_pixel(viewport:RID, enabled:bool)
void
viewport_set_snap_2d_vertices_to_pixel(viewport:RID, enabled:bool)
void
viewport_set_texture_mipmap_bias(viewport:RID, mipmap_bias:float)
void
viewport_set_transparent_background(viewport:RID, enabled:bool)
void
viewport_set_update_mode(viewport:RID, update_mode:ViewportUpdateMode)
void
viewport_set_use_debanding(viewport:RID, enable:bool)
void
viewport_set_use_hdr_2d(viewport:RID, enabled:bool)
void
viewport_set_use_occlusion_culling(viewport:RID, enable:bool)
void
viewport_set_use_taa(viewport:RID, enable:bool)
void
viewport_set_use_xr(viewport:RID, use_xr:bool)
void
viewport_set_vrs_mode(viewport:RID, mode:ViewportVRSMode)
void
viewport_set_vrs_texture(viewport:RID, texture:RID)
void
viewport_set_vrs_update_mode(viewport:RID, mode:ViewportVRSUpdateMode)
visibility_notifier_create()
void
visibility_notifier_set_aabb(notifier:RID, aabb:AABB)
void
visibility_notifier_set_callbacks(notifier:RID, enter_callable:Callable, exit_callable:Callable)
void
voxel_gi_allocate_data(voxel_gi:RID, to_cell_xform:Transform3D, aabb:AABB, octree_size:Vector3i, octree_cells:PackedByteArray, data_cells:PackedByteArray, distance_field:PackedByteArray, level_counts:PackedInt32Array)
voxel_gi_create()
PackedByteArray
voxel_gi_get_data_cells(voxel_gi:RID)const
PackedByteArray
voxel_gi_get_distance_field(voxel_gi:RID)const
PackedInt32Array
voxel_gi_get_level_counts(voxel_gi:RID)const
PackedByteArray
voxel_gi_get_octree_cells(voxel_gi:RID)const
Vector3i
voxel_gi_get_octree_size(voxel_gi:RID)const
Transform3D
voxel_gi_get_to_cell_xform(voxel_gi:RID)const
void
voxel_gi_set_baked_exposure_normalization(voxel_gi:RID, baked_exposure:float)
void
voxel_gi_set_bias(voxel_gi:RID, bias:float)
void
voxel_gi_set_dynamic_range(voxel_gi:RID, range:float)
void
voxel_gi_set_energy(voxel_gi:RID, energy:float)
void
voxel_gi_set_interior(voxel_gi:RID, enable:bool)
void
voxel_gi_set_normal_bias(voxel_gi:RID, bias:float)
void
voxel_gi_set_propagation(voxel_gi:RID, amount:float)
void
voxel_gi_set_quality(quality:VoxelGIQuality)
void
voxel_gi_set_use_two_bounces(voxel_gi:RID, enable:bool)

## Signals

frame_post_draw()🔗
Emitted at the end of the frame, after the RenderingServer has finished updating all the Viewports.
frame_pre_draw()🔗
Emitted at the beginning of the frame, before the RenderingServer updates all the Viewports.

## Enumerations

enumTextureType:🔗
TextureTypeTEXTURE_TYPE_2D=0
2D texture.
TextureTypeTEXTURE_TYPE_LAYERED=1
Layered texture.
TextureTypeTEXTURE_TYPE_3D=2
3D texture.
enumTextureLayeredType:🔗
TextureLayeredTypeTEXTURE_LAYERED_2D_ARRAY=0
Array of 2-dimensional textures (seeTexture2DArray).
TextureLayeredTypeTEXTURE_LAYERED_CUBEMAP=1
Cubemap texture (seeCubemap).
TextureLayeredTypeTEXTURE_LAYERED_CUBEMAP_ARRAY=2
Array of cubemap textures (seeCubemapArray).
enumCubeMapLayer:🔗
CubeMapLayerCUBEMAP_LAYER_LEFT=0
Left face of aCubemap.
CubeMapLayerCUBEMAP_LAYER_RIGHT=1
Right face of aCubemap.
CubeMapLayerCUBEMAP_LAYER_BOTTOM=2
Bottom face of aCubemap.
CubeMapLayerCUBEMAP_LAYER_TOP=3
Top face of aCubemap.
CubeMapLayerCUBEMAP_LAYER_FRONT=4
Front face of aCubemap.
CubeMapLayerCUBEMAP_LAYER_BACK=5
Back face of aCubemap.
enumShaderMode:🔗
ShaderModeSHADER_SPATIAL=0
Shader is a 3D shader.
ShaderModeSHADER_CANVAS_ITEM=1
Shader is a 2D shader.
ShaderModeSHADER_PARTICLES=2
Shader is a particle shader (can be used in both 2D and 3D).
ShaderModeSHADER_SKY=3
Shader is a 3D sky shader.
ShaderModeSHADER_FOG=4
Shader is a 3D fog shader.
ShaderModeSHADER_MAX=5
Represents the size of theShaderModeenum.
enumArrayType:🔗
ArrayTypeARRAY_VERTEX=0
Array is a vertex position array.
ArrayTypeARRAY_NORMAL=1
Array is a normal array.
ArrayTypeARRAY_TANGENT=2
Array is a tangent array.
ArrayTypeARRAY_COLOR=3
Array is a vertex color array.
ArrayTypeARRAY_TEX_UV=4
Array is a UV coordinates array.
ArrayTypeARRAY_TEX_UV2=5
Array is a UV coordinates array for the second set of UV coordinates.
ArrayTypeARRAY_CUSTOM0=6
Array is a custom data array for the first set of custom data.
ArrayTypeARRAY_CUSTOM1=7
Array is a custom data array for the second set of custom data.
ArrayTypeARRAY_CUSTOM2=8
Array is a custom data array for the third set of custom data.
ArrayTypeARRAY_CUSTOM3=9
Array is a custom data array for the fourth set of custom data.
ArrayTypeARRAY_BONES=10
Array contains bone information.
ArrayTypeARRAY_WEIGHTS=11
Array is weight information.
ArrayTypeARRAY_INDEX=12
Array is an index array.
ArrayTypeARRAY_MAX=13
Represents the size of theArrayTypeenum.
enumArrayCustomFormat:🔗
ArrayCustomFormatARRAY_CUSTOM_RGBA8_UNORM=0
Custom data array contains 8-bit-per-channel red/green/blue/alpha color data. Values are normalized, unsigned floating-point in the[0.0,1.0]range.
ArrayCustomFormatARRAY_CUSTOM_RGBA8_SNORM=1
Custom data array contains 8-bit-per-channel red/green/blue/alpha color data. Values are normalized, signed floating-point in the[-1.0,1.0]range.
ArrayCustomFormatARRAY_CUSTOM_RG_HALF=2
Custom data array contains 16-bit-per-channel red/green color data. Values are floating-point in half precision.
ArrayCustomFormatARRAY_CUSTOM_RGBA_HALF=3
Custom data array contains 16-bit-per-channel red/green/blue/alpha color data. Values are floating-point in half precision.
ArrayCustomFormatARRAY_CUSTOM_R_FLOAT=4
Custom data array contains 32-bit-per-channel red color data. Values are floating-point in single precision.
ArrayCustomFormatARRAY_CUSTOM_RG_FLOAT=5
Custom data array contains 32-bit-per-channel red/green color data. Values are floating-point in single precision.
ArrayCustomFormatARRAY_CUSTOM_RGB_FLOAT=6
Custom data array contains 32-bit-per-channel red/green/blue color data. Values are floating-point in single precision.
ArrayCustomFormatARRAY_CUSTOM_RGBA_FLOAT=7
Custom data array contains 32-bit-per-channel red/green/blue/alpha color data. Values are floating-point in single precision.
ArrayCustomFormatARRAY_CUSTOM_MAX=8
Represents the size of theArrayCustomFormatenum.
flagsArrayFormat:🔗
ArrayFormatARRAY_FORMAT_VERTEX=1
Flag used to mark a vertex position array.
ArrayFormatARRAY_FORMAT_NORMAL=2
Flag used to mark a normal array.
ArrayFormatARRAY_FORMAT_TANGENT=4
Flag used to mark a tangent array.
ArrayFormatARRAY_FORMAT_COLOR=8
Flag used to mark a vertex color array.
ArrayFormatARRAY_FORMAT_TEX_UV=16
Flag used to mark a UV coordinates array.
ArrayFormatARRAY_FORMAT_TEX_UV2=32
Flag used to mark a UV coordinates array for the second UV coordinates.
ArrayFormatARRAY_FORMAT_CUSTOM0=64
Flag used to mark an array of custom per-vertex data for the first set of custom data.
ArrayFormatARRAY_FORMAT_CUSTOM1=128
Flag used to mark an array of custom per-vertex data for the second set of custom data.
ArrayFormatARRAY_FORMAT_CUSTOM2=256
Flag used to mark an array of custom per-vertex data for the third set of custom data.
ArrayFormatARRAY_FORMAT_CUSTOM3=512
Flag used to mark an array of custom per-vertex data for the fourth set of custom data.
ArrayFormatARRAY_FORMAT_BONES=1024
Flag used to mark a bone information array.
ArrayFormatARRAY_FORMAT_WEIGHTS=2048
Flag used to mark a weights array.
ArrayFormatARRAY_FORMAT_INDEX=4096
Flag used to mark an index array.
ArrayFormatARRAY_FORMAT_BLEND_SHAPE_MASK=7
Mask of mesh channels permitted in blend shapes.
ArrayFormatARRAY_FORMAT_CUSTOM_BASE=13
Shift of first custom channel.
ArrayFormatARRAY_FORMAT_CUSTOM_BITS=3
Number of format bits per custom channel. SeeArrayCustomFormat.
ArrayFormatARRAY_FORMAT_CUSTOM0_SHIFT=13
Amount to shiftArrayCustomFormatfor custom channel index 0.
ArrayFormatARRAY_FORMAT_CUSTOM1_SHIFT=16
Amount to shiftArrayCustomFormatfor custom channel index 1.
ArrayFormatARRAY_FORMAT_CUSTOM2_SHIFT=19
Amount to shiftArrayCustomFormatfor custom channel index 2.
ArrayFormatARRAY_FORMAT_CUSTOM3_SHIFT=22
Amount to shiftArrayCustomFormatfor custom channel index 3.
ArrayFormatARRAY_FORMAT_CUSTOM_MASK=7
Mask of custom format bits per custom channel. Must be shifted by one of the SHIFT constants. SeeArrayCustomFormat.
ArrayFormatARRAY_COMPRESS_FLAGS_BASE=25
Shift of first compress flag. Compress flags should be passed toArrayMesh.add_surface_from_arrays()andSurfaceTool.commit().
ArrayFormatARRAY_FLAG_USE_2D_VERTICES=33554432
Flag used to mark that the array contains 2D vertices.
ArrayFormatARRAY_FLAG_USE_DYNAMIC_UPDATE=67108864
Flag used to mark that the mesh data will useGL_DYNAMIC_DRAWon GLES. Unused on Vulkan.
ArrayFormatARRAY_FLAG_USE_8_BONE_WEIGHTS=134217728
Flag used to mark that the array uses 8 bone weights instead of 4.
ArrayFormatARRAY_FLAG_USES_EMPTY_VERTEX_ARRAY=268435456
Flag used to mark that the mesh does not have a vertex array and instead will infer vertex positions in the shader using indices and other information.
ArrayFormatARRAY_FLAG_COMPRESS_ATTRIBUTES=536870912
Flag used to mark that a mesh is using compressed attributes (vertices, normals, tangents, UVs). When this form of compression is enabled, vertex positions will be packed into an RGBA16UNORM attribute and scaled in the vertex shader. The normal and tangent will be packed into an RG16UNORM representing an axis, and a 16-bit float stored in the A-channel of the vertex. UVs will use 16-bit normalized floats instead of full 32-bit signed floats. When using this compression mode you must use either vertices, normals, and tangents or only vertices. You cannot use normals without tangents. Importers will automatically enable this compression if they can.
ArrayFormatARRAY_FLAG_FORMAT_VERSION_BASE=35
Flag used to mark the start of the bits used to store the mesh version.
ArrayFormatARRAY_FLAG_FORMAT_VERSION_SHIFT=35
Flag used to shift a mesh format int to bring the version into the lowest digits.
ArrayFormatARRAY_FLAG_FORMAT_VERSION_1=0
Flag used to record the format used by prior mesh versions before the introduction of a version.
ArrayFormatARRAY_FLAG_FORMAT_VERSION_2=34359738368
Flag used to record the second iteration of the mesh version flag. The primary difference between this andARRAY_FLAG_FORMAT_VERSION_1is that this version supportsARRAY_FLAG_COMPRESS_ATTRIBUTESand in this version vertex positions are de-interleaved from normals and tangents.
ArrayFormatARRAY_FLAG_FORMAT_CURRENT_VERSION=34359738368
Flag used to record the current version that the engine expects. Currently this is the same asARRAY_FLAG_FORMAT_VERSION_2.
ArrayFormatARRAY_FLAG_FORMAT_VERSION_MASK=255
Flag used to isolate the bits used for mesh version after usingARRAY_FLAG_FORMAT_VERSION_SHIFTto shift them into place.
enumPrimitiveType:🔗
PrimitiveTypePRIMITIVE_POINTS=0
Primitive to draw consists of points.
PrimitiveTypePRIMITIVE_LINES=1
Primitive to draw consists of lines.
PrimitiveTypePRIMITIVE_LINE_STRIP=2
Primitive to draw consists of a line strip from start to end.
PrimitiveTypePRIMITIVE_TRIANGLES=3
Primitive to draw consists of triangles.
PrimitiveTypePRIMITIVE_TRIANGLE_STRIP=4
Primitive to draw consists of a triangle strip (the last 3 vertices are always combined to make a triangle).
PrimitiveTypePRIMITIVE_MAX=5
Represents the size of thePrimitiveTypeenum.
enumBlendShapeMode:🔗
BlendShapeModeBLEND_SHAPE_MODE_NORMALIZED=0
Blend shapes are normalized.
BlendShapeModeBLEND_SHAPE_MODE_RELATIVE=1
Blend shapes are relative to base weight.
enumMultimeshTransformFormat:🔗
MultimeshTransformFormatMULTIMESH_TRANSFORM_2D=0
UseTransform2Dto store MultiMesh transform.
MultimeshTransformFormatMULTIMESH_TRANSFORM_3D=1
UseTransform3Dto store MultiMesh transform.
enumMultimeshPhysicsInterpolationQuality:🔗
MultimeshPhysicsInterpolationQualityMULTIMESH_INTERP_QUALITY_FAST=0
MultiMesh physics interpolation favors speed over quality.
MultimeshPhysicsInterpolationQualityMULTIMESH_INTERP_QUALITY_HIGH=1
MultiMesh physics interpolation favors quality over speed.
enumLightProjectorFilter:🔗
LightProjectorFilterLIGHT_PROJECTOR_FILTER_NEAREST=0
Nearest-neighbor filter for light projectors (use for pixel art light projectors). No mipmaps are used for rendering, which means light projectors at a distance will look sharp but grainy. This has roughly the same performance cost as using mipmaps.
LightProjectorFilterLIGHT_PROJECTOR_FILTER_LINEAR=1
Linear filter for light projectors (use for non-pixel art light projectors). No mipmaps are used for rendering, which means light projectors at a distance will look smooth but blurry. This has roughly the same performance cost as using mipmaps.
LightProjectorFilterLIGHT_PROJECTOR_FILTER_NEAREST_MIPMAPS=2
Nearest-neighbor filter for light projectors (use for pixel art light projectors). Isotropic mipmaps are used for rendering, which means light projectors at a distance will look smooth but blurry. This has roughly the same performance cost as not using mipmaps.
LightProjectorFilterLIGHT_PROJECTOR_FILTER_LINEAR_MIPMAPS=3
Linear filter for light projectors (use for non-pixel art light projectors). Isotropic mipmaps are used for rendering, which means light projectors at a distance will look smooth but blurry. This has roughly the same performance cost as not using mipmaps.
LightProjectorFilterLIGHT_PROJECTOR_FILTER_NEAREST_MIPMAPS_ANISOTROPIC=4
Nearest-neighbor filter for light projectors (use for pixel art light projectors). Anisotropic mipmaps are used for rendering, which means light projectors at a distance will look smooth and sharp when viewed from oblique angles. This looks better compared to isotropic mipmaps, but is slower. The level of anisotropic filtering is defined byProjectSettings.rendering/textures/default_filters/anisotropic_filtering_level.
LightProjectorFilterLIGHT_PROJECTOR_FILTER_LINEAR_MIPMAPS_ANISOTROPIC=5
Linear filter for light projectors (use for non-pixel art light projectors). Anisotropic mipmaps are used for rendering, which means light projectors at a distance will look smooth and sharp when viewed from oblique angles. This looks better compared to isotropic mipmaps, but is slower. The level of anisotropic filtering is defined byProjectSettings.rendering/textures/default_filters/anisotropic_filtering_level.
enumLightType:🔗
LightTypeLIGHT_DIRECTIONAL=0
Directional (sun/moon) light (seeDirectionalLight3D).
LightTypeLIGHT_OMNI=1
Omni light (seeOmniLight3D).
LightTypeLIGHT_SPOT=2
Spot light (seeSpotLight3D).
enumLightParam:🔗
LightParamLIGHT_PARAM_ENERGY=0
The light's energy multiplier.
LightParamLIGHT_PARAM_INDIRECT_ENERGY=1
The light's indirect energy multiplier (final indirect energy isLIGHT_PARAM_ENERGY*LIGHT_PARAM_INDIRECT_ENERGY).
LightParamLIGHT_PARAM_VOLUMETRIC_FOG_ENERGY=2
The light's volumetric fog energy multiplier (final volumetric fog energy isLIGHT_PARAM_ENERGY*LIGHT_PARAM_VOLUMETRIC_FOG_ENERGY).
LightParamLIGHT_PARAM_SPECULAR=3
The light's influence on specularity.
LightParamLIGHT_PARAM_RANGE=4
The light's range.
LightParamLIGHT_PARAM_SIZE=5
The size of the light when using spot light or omni light. The angular size of the light when using directional light.
LightParamLIGHT_PARAM_ATTENUATION=6
The light's attenuation.
LightParamLIGHT_PARAM_SPOT_ANGLE=7
The spotlight's angle.
LightParamLIGHT_PARAM_SPOT_ATTENUATION=8
The spotlight's attenuation.
LightParamLIGHT_PARAM_SHADOW_MAX_DISTANCE=9
The maximum distance for shadow splits. Increasing this value will make directional shadows visible from further away, at the cost of lower overall shadow detail and performance (since more objects need to be included in the directional shadow rendering).
LightParamLIGHT_PARAM_SHADOW_SPLIT_1_OFFSET=10
Proportion of shadow atlas occupied by the first split.
LightParamLIGHT_PARAM_SHADOW_SPLIT_2_OFFSET=11
Proportion of shadow atlas occupied by the second split.
LightParamLIGHT_PARAM_SHADOW_SPLIT_3_OFFSET=12
Proportion of shadow atlas occupied by the third split. The fourth split occupies the rest.
LightParamLIGHT_PARAM_SHADOW_FADE_START=13
Proportion of shadow max distance where the shadow will start to fade out.
LightParamLIGHT_PARAM_SHADOW_NORMAL_BIAS=14
Normal bias used to offset shadow lookup by object normal. Can be used to fix self-shadowing artifacts.
LightParamLIGHT_PARAM_SHADOW_BIAS=15
Bias for the shadow lookup to fix self-shadowing artifacts.
LightParamLIGHT_PARAM_SHADOW_PANCAKE_SIZE=16
Sets the size of the directional shadow pancake. The pancake offsets the start of the shadow's camera frustum to provide a higher effective depth resolution for the shadow. However, a high pancake size can cause artifacts in the shadows of large objects that are close to the edge of the frustum. Reducing the pancake size can help. Setting the size to0turns off the pancaking effect.
LightParamLIGHT_PARAM_SHADOW_OPACITY=17
The light's shadow opacity. Values lower than1.0make the light appear through shadows. This can be used to fake global illumination at a low performance cost.
LightParamLIGHT_PARAM_SHADOW_BLUR=18
Blurs the edges of the shadow. Can be used to hide pixel artifacts in low resolution shadow maps. A high value can make shadows appear grainy and can cause other unwanted artifacts. Try to keep as near default as possible.
LightParamLIGHT_PARAM_TRANSMITTANCE_BIAS=19
There is currently no description for this enum. Please help us bycontributing one!
LightParamLIGHT_PARAM_INTENSITY=20
Constant representing the intensity of the light, measured in Lumens when dealing with aSpotLight3DorOmniLight3D, or measured in Lux with aDirectionalLight3D. Only used whenProjectSettings.rendering/lights_and_shadows/use_physical_light_unitsistrue.
LightParamLIGHT_PARAM_MAX=21
Represents the size of theLightParamenum.
enumLightBakeMode:🔗
LightBakeModeLIGHT_BAKE_DISABLED=0
Light is ignored when baking. This is the fastest mode, but the light will be taken into account when baking global illumination. This mode should generally be used for dynamic lights that change quickly, as the effect of global illumination is less noticeable on those lights.
LightBakeModeLIGHT_BAKE_STATIC=1
Light is taken into account in static baking (VoxelGI,LightmapGI, SDFGI (Environment.sdfgi_enabled)). The light can be moved around or modified, but its global illumination will not update in real-time. This is suitable for subtle changes (such as flickering torches), but generally not large changes such as toggling a light on and off.
LightBakeModeLIGHT_BAKE_DYNAMIC=2
Light is taken into account in dynamic baking (VoxelGIand SDFGI (Environment.sdfgi_enabled) only). The light can be moved around or modified with global illumination updating in real-time. The light's global illumination appearance will be slightly different compared toLIGHT_BAKE_STATIC. This has a greater performance cost compared toLIGHT_BAKE_STATIC. When using SDFGI, the update speed of dynamic lights is affected byProjectSettings.rendering/global_illumination/sdfgi/frames_to_update_lights.
enumLightOmniShadowMode:🔗
LightOmniShadowModeLIGHT_OMNI_SHADOW_DUAL_PARABOLOID=0
Use a dual paraboloid shadow map for omni lights.
LightOmniShadowModeLIGHT_OMNI_SHADOW_CUBE=1
Use a cubemap shadow map for omni lights. Slower but better quality than dual paraboloid.
enumLightDirectionalShadowMode:🔗
LightDirectionalShadowModeLIGHT_DIRECTIONAL_SHADOW_ORTHOGONAL=0
Use orthogonal shadow projection for directional light.
LightDirectionalShadowModeLIGHT_DIRECTIONAL_SHADOW_PARALLEL_2_SPLITS=1
Use 2 splits for shadow projection when using directional light.
LightDirectionalShadowModeLIGHT_DIRECTIONAL_SHADOW_PARALLEL_4_SPLITS=2
Use 4 splits for shadow projection when using directional light.
enumLightDirectionalSkyMode:🔗
LightDirectionalSkyModeLIGHT_DIRECTIONAL_SKY_MODE_LIGHT_AND_SKY=0
Use DirectionalLight3D in both sky rendering and scene lighting.
LightDirectionalSkyModeLIGHT_DIRECTIONAL_SKY_MODE_LIGHT_ONLY=1
Only use DirectionalLight3D in scene lighting.
LightDirectionalSkyModeLIGHT_DIRECTIONAL_SKY_MODE_SKY_ONLY=2
Only use DirectionalLight3D in sky rendering.
enumShadowQuality:🔗
ShadowQualitySHADOW_QUALITY_HARD=0
Lowest shadow filtering quality (fastest). Soft shadows are not available with this quality setting, which means theLight3D.shadow_blurproperty is ignored ifLight3D.light_sizeandLight3D.light_angular_distanceis0.0.
Note:The variable shadow blur performed byLight3D.light_sizeandLight3D.light_angular_distanceis still effective when using hard shadow filtering. In this case,Light3D.shadow_bluristaken into account. However, the results will not be blurred, instead the blur amount is treated as a maximum radius for the penumbra.
ShadowQualitySHADOW_QUALITY_SOFT_VERY_LOW=1
Very low shadow filtering quality (faster). When using this quality setting,Light3D.shadow_bluris automatically multiplied by 0.75× to avoid introducing too much noise. This division only applies to lights whoseLight3D.light_sizeorLight3D.light_angular_distanceis0.0).
ShadowQualitySHADOW_QUALITY_SOFT_LOW=2
Low shadow filtering quality (fast).
ShadowQualitySHADOW_QUALITY_SOFT_MEDIUM=3
Medium low shadow filtering quality (average).
ShadowQualitySHADOW_QUALITY_SOFT_HIGH=4
High low shadow filtering quality (slow). When using this quality setting,Light3D.shadow_bluris automatically multiplied by 1.5× to better make use of the high sample count. This increased blur also improves the stability of dynamic object shadows. This multiplier only applies to lights whoseLight3D.light_sizeorLight3D.light_angular_distanceis0.0).
ShadowQualitySHADOW_QUALITY_SOFT_ULTRA=5
Highest low shadow filtering quality (slowest). When using this quality setting,Light3D.shadow_bluris automatically multiplied by 2× to better make use of the high sample count. This increased blur also improves the stability of dynamic object shadows. This multiplier only applies to lights whoseLight3D.light_sizeorLight3D.light_angular_distanceis0.0).
ShadowQualitySHADOW_QUALITY_MAX=6
Represents the size of theShadowQualityenum.
enumReflectionProbeUpdateMode:🔗
ReflectionProbeUpdateModeREFLECTION_PROBE_UPDATE_ONCE=0
Reflection probe will update reflections once and then stop.
ReflectionProbeUpdateModeREFLECTION_PROBE_UPDATE_ALWAYS=1
Reflection probe will update each frame. This mode is necessary to capture moving objects.
enumReflectionProbeAmbientMode:🔗
ReflectionProbeAmbientModeREFLECTION_PROBE_AMBIENT_DISABLED=0
Do not apply any ambient lighting inside the reflection probe's box defined by its size.
ReflectionProbeAmbientModeREFLECTION_PROBE_AMBIENT_ENVIRONMENT=1
Apply automatically-sourced environment lighting inside the reflection probe's box defined by its size.
ReflectionProbeAmbientModeREFLECTION_PROBE_AMBIENT_COLOR=2
Apply custom ambient lighting inside the reflection probe's box defined by its size. Seereflection_probe_set_ambient_color()andreflection_probe_set_ambient_energy().
enumDecalTexture:🔗
DecalTextureDECAL_TEXTURE_ALBEDO=0
Albedo texture slot in a decal (Decal.texture_albedo).
DecalTextureDECAL_TEXTURE_NORMAL=1
Normal map texture slot in a decal (Decal.texture_normal).
DecalTextureDECAL_TEXTURE_ORM=2
Occlusion/Roughness/Metallic texture slot in a decal (Decal.texture_orm).
DecalTextureDECAL_TEXTURE_EMISSION=3
Emission texture slot in a decal (Decal.texture_emission).
DecalTextureDECAL_TEXTURE_MAX=4
Represents the size of theDecalTextureenum.
enumDecalFilter:🔗
DecalFilterDECAL_FILTER_NEAREST=0
Nearest-neighbor filter for decals (use for pixel art decals). No mipmaps are used for rendering, which means decals at a distance will look sharp but grainy. This has roughly the same performance cost as using mipmaps.
DecalFilterDECAL_FILTER_LINEAR=1
Linear filter for decals (use for non-pixel art decals). No mipmaps are used for rendering, which means decals at a distance will look smooth but blurry. This has roughly the same performance cost as using mipmaps.
DecalFilterDECAL_FILTER_NEAREST_MIPMAPS=2
Nearest-neighbor filter for decals (use for pixel art decals). Isotropic mipmaps are used for rendering, which means decals at a distance will look smooth but blurry. This has roughly the same performance cost as not using mipmaps.
DecalFilterDECAL_FILTER_LINEAR_MIPMAPS=3
Linear filter for decals (use for non-pixel art decals). Isotropic mipmaps are used for rendering, which means decals at a distance will look smooth but blurry. This has roughly the same performance cost as not using mipmaps.
DecalFilterDECAL_FILTER_NEAREST_MIPMAPS_ANISOTROPIC=4
Nearest-neighbor filter for decals (use for pixel art decals). Anisotropic mipmaps are used for rendering, which means decals at a distance will look smooth and sharp when viewed from oblique angles. This looks better compared to isotropic mipmaps, but is slower. The level of anisotropic filtering is defined byProjectSettings.rendering/textures/default_filters/anisotropic_filtering_level.
DecalFilterDECAL_FILTER_LINEAR_MIPMAPS_ANISOTROPIC=5
Linear filter for decals (use for non-pixel art decals). Anisotropic mipmaps are used for rendering, which means decals at a distance will look smooth and sharp when viewed from oblique angles. This looks better compared to isotropic mipmaps, but is slower. The level of anisotropic filtering is defined byProjectSettings.rendering/textures/default_filters/anisotropic_filtering_level.
enumVoxelGIQuality:🔗
VoxelGIQualityVOXEL_GI_QUALITY_LOW=0
LowVoxelGIrendering quality using 4 cones.
VoxelGIQualityVOXEL_GI_QUALITY_HIGH=1
HighVoxelGIrendering quality using 6 cones.
enumParticlesMode:🔗
ParticlesModePARTICLES_MODE_2D=0
2D particles.
ParticlesModePARTICLES_MODE_3D=1
3D particles.
enumParticlesTransformAlign:🔗
ParticlesTransformAlignPARTICLES_TRANSFORM_ALIGN_DISABLED=0
There is currently no description for this enum. Please help us bycontributing one!
ParticlesTransformAlignPARTICLES_TRANSFORM_ALIGN_Z_BILLBOARD=1
There is currently no description for this enum. Please help us bycontributing one!
ParticlesTransformAlignPARTICLES_TRANSFORM_ALIGN_Y_TO_VELOCITY=2
There is currently no description for this enum. Please help us bycontributing one!
ParticlesTransformAlignPARTICLES_TRANSFORM_ALIGN_Z_BILLBOARD_Y_TO_VELOCITY=3
There is currently no description for this enum. Please help us bycontributing one!
enumParticlesDrawOrder:🔗
ParticlesDrawOrderPARTICLES_DRAW_ORDER_INDEX=0
Draw particles in the order that they appear in the particles array.
ParticlesDrawOrderPARTICLES_DRAW_ORDER_LIFETIME=1
Sort particles based on their lifetime. In other words, the particle with the highest lifetime is drawn at the front.
ParticlesDrawOrderPARTICLES_DRAW_ORDER_REVERSE_LIFETIME=2
Sort particles based on the inverse of their lifetime. In other words, the particle with the lowest lifetime is drawn at the front.
ParticlesDrawOrderPARTICLES_DRAW_ORDER_VIEW_DEPTH=3
Sort particles based on their distance to the camera.
enumParticlesCollisionType:🔗
ParticlesCollisionTypePARTICLES_COLLISION_TYPE_SPHERE_ATTRACT=0
There is currently no description for this enum. Please help us bycontributing one!
ParticlesCollisionTypePARTICLES_COLLISION_TYPE_BOX_ATTRACT=1
There is currently no description for this enum. Please help us bycontributing one!
ParticlesCollisionTypePARTICLES_COLLISION_TYPE_VECTOR_FIELD_ATTRACT=2
There is currently no description for this enum. Please help us bycontributing one!
ParticlesCollisionTypePARTICLES_COLLISION_TYPE_SPHERE_COLLIDE=3
There is currently no description for this enum. Please help us bycontributing one!
ParticlesCollisionTypePARTICLES_COLLISION_TYPE_BOX_COLLIDE=4
There is currently no description for this enum. Please help us bycontributing one!
ParticlesCollisionTypePARTICLES_COLLISION_TYPE_SDF_COLLIDE=5
There is currently no description for this enum. Please help us bycontributing one!
ParticlesCollisionTypePARTICLES_COLLISION_TYPE_HEIGHTFIELD_COLLIDE=6
There is currently no description for this enum. Please help us bycontributing one!
enumParticlesCollisionHeightfieldResolution:🔗
ParticlesCollisionHeightfieldResolutionPARTICLES_COLLISION_HEIGHTFIELD_RESOLUTION_256=0
There is currently no description for this enum. Please help us bycontributing one!
ParticlesCollisionHeightfieldResolutionPARTICLES_COLLISION_HEIGHTFIELD_RESOLUTION_512=1
There is currently no description for this enum. Please help us bycontributing one!
ParticlesCollisionHeightfieldResolutionPARTICLES_COLLISION_HEIGHTFIELD_RESOLUTION_1024=2
There is currently no description for this enum. Please help us bycontributing one!
ParticlesCollisionHeightfieldResolutionPARTICLES_COLLISION_HEIGHTFIELD_RESOLUTION_2048=3
There is currently no description for this enum. Please help us bycontributing one!
ParticlesCollisionHeightfieldResolutionPARTICLES_COLLISION_HEIGHTFIELD_RESOLUTION_4096=4
There is currently no description for this enum. Please help us bycontributing one!
ParticlesCollisionHeightfieldResolutionPARTICLES_COLLISION_HEIGHTFIELD_RESOLUTION_8192=5
There is currently no description for this enum. Please help us bycontributing one!
ParticlesCollisionHeightfieldResolutionPARTICLES_COLLISION_HEIGHTFIELD_RESOLUTION_MAX=6
Represents the size of theParticlesCollisionHeightfieldResolutionenum.
enumFogVolumeShape:🔗
FogVolumeShapeFOG_VOLUME_SHAPE_ELLIPSOID=0
FogVolumewill be shaped like an ellipsoid (stretched sphere).
FogVolumeShapeFOG_VOLUME_SHAPE_CONE=1
FogVolumewill be shaped like a cone pointing upwards (in local coordinates). The cone's angle is set automatically to fill the size. The cone will be adjusted to fit within the size. Rotate theFogVolumenode to reorient the cone. Non-uniform scaling via size is not supported (scale theFogVolumenode instead).
FogVolumeShapeFOG_VOLUME_SHAPE_CYLINDER=2
FogVolumewill be shaped like an upright cylinder (in local coordinates). Rotate theFogVolumenode to reorient the cylinder. The cylinder will be adjusted to fit within the size. Non-uniform scaling via size is not supported (scale theFogVolumenode instead).
FogVolumeShapeFOG_VOLUME_SHAPE_BOX=3
FogVolumewill be shaped like a box.
FogVolumeShapeFOG_VOLUME_SHAPE_WORLD=4
FogVolumewill have no shape, will cover the whole world and will not be culled.
FogVolumeShapeFOG_VOLUME_SHAPE_MAX=5
Represents the size of theFogVolumeShapeenum.
enumViewportScaling3DMode:🔗
ViewportScaling3DModeVIEWPORT_SCALING_3D_MODE_BILINEAR=0
Use bilinear scaling for the viewport's 3D buffer. The amount of scaling can be set usingViewport.scaling_3d_scale. Values less than1.0will result in undersampling while values greater than1.0will result in supersampling. A value of1.0disables scaling.
ViewportScaling3DModeVIEWPORT_SCALING_3D_MODE_FSR=1
Use AMD FidelityFX Super Resolution 1.0 upscaling for the viewport's 3D buffer. The amount of scaling can be set usingViewport.scaling_3d_scale. Values less than1.0will result in the viewport being upscaled using FSR. Values greater than1.0are not supported and bilinear downsampling will be used instead. A value of1.0disables scaling.
ViewportScaling3DModeVIEWPORT_SCALING_3D_MODE_FSR2=2
Use AMD FidelityFX Super Resolution 2.2 upscaling for the viewport's 3D buffer. The amount of scaling can be set usingViewport.scaling_3d_scale. Values less than1.0will result in the viewport being upscaled using FSR2. Values greater than1.0are not supported and bilinear downsampling will be used instead. A value of1.0will use FSR2 at native resolution as a TAA solution.
ViewportScaling3DModeVIEWPORT_SCALING_3D_MODE_METALFX_SPATIAL=3
Use MetalFX spatial upscaling for the viewport's 3D buffer. The amount of scaling can be set usingViewport.scaling_3d_scale. Values less than1.0will result in the viewport being upscaled using MetalFX. Values greater than1.0are not supported and bilinear downsampling will be used instead. A value of1.0disables scaling.
Note:Only supported when the Metal rendering driver is in use, which limits this scaling mode to macOS and iOS.
ViewportScaling3DModeVIEWPORT_SCALING_3D_MODE_METALFX_TEMPORAL=4
Use MetalFX temporal upscaling for the viewport's 3D buffer. The amount of scaling can be set usingViewport.scaling_3d_scale. Values less than1.0will result in the viewport being upscaled using MetalFX. Values greater than1.0are not supported and bilinear downsampling will be used instead. A value of1.0will use MetalFX at native resolution as a TAA solution.
Note:Only supported when the Metal rendering driver is in use, which limits this scaling mode to macOS and iOS.
ViewportScaling3DModeVIEWPORT_SCALING_3D_MODE_MAX=5
Represents the size of theViewportScaling3DModeenum.
enumViewportUpdateMode:🔗
ViewportUpdateModeVIEWPORT_UPDATE_DISABLED=0
Do not update the viewport's render target.
ViewportUpdateModeVIEWPORT_UPDATE_ONCE=1
Update the viewport's render target once, then switch toVIEWPORT_UPDATE_DISABLED.
ViewportUpdateModeVIEWPORT_UPDATE_WHEN_VISIBLE=2
Update the viewport's render target only when it is visible. This is the default value.
ViewportUpdateModeVIEWPORT_UPDATE_WHEN_PARENT_VISIBLE=3
Update the viewport's render target only when its parent is visible.
ViewportUpdateModeVIEWPORT_UPDATE_ALWAYS=4
Always update the viewport's render target.
enumViewportClearMode:🔗
ViewportClearModeVIEWPORT_CLEAR_ALWAYS=0
Always clear the viewport's render target before drawing.
ViewportClearModeVIEWPORT_CLEAR_NEVER=1
Never clear the viewport's render target.
ViewportClearModeVIEWPORT_CLEAR_ONLY_NEXT_FRAME=2
Clear the viewport's render target on the next frame, then switch toVIEWPORT_CLEAR_NEVER.
enumViewportEnvironmentMode:🔗
ViewportEnvironmentModeVIEWPORT_ENVIRONMENT_DISABLED=0
Disable rendering of 3D environment over 2D canvas.
ViewportEnvironmentModeVIEWPORT_ENVIRONMENT_ENABLED=1
Enable rendering of 3D environment over 2D canvas.
ViewportEnvironmentModeVIEWPORT_ENVIRONMENT_INHERIT=2
Inherit enable/disable value from parent. If the topmost parent is also set toVIEWPORT_ENVIRONMENT_INHERIT, then this has the same behavior asVIEWPORT_ENVIRONMENT_ENABLED.
ViewportEnvironmentModeVIEWPORT_ENVIRONMENT_MAX=3
Represents the size of theViewportEnvironmentModeenum.
enumViewportSDFOversize:🔗
ViewportSDFOversizeVIEWPORT_SDF_OVERSIZE_100_PERCENT=0
Do not oversize the 2D signed distance field. Occluders may disappear when touching the viewport's edges, andGPUParticles3Dcollision may stop working earlier than intended. This has the lowest GPU requirements.
ViewportSDFOversizeVIEWPORT_SDF_OVERSIZE_120_PERCENT=1
2D signed distance field covers 20% of the viewport's size outside the viewport on each side (top, right, bottom, left).
ViewportSDFOversizeVIEWPORT_SDF_OVERSIZE_150_PERCENT=2
2D signed distance field covers 50% of the viewport's size outside the viewport on each side (top, right, bottom, left).
ViewportSDFOversizeVIEWPORT_SDF_OVERSIZE_200_PERCENT=3
2D signed distance field covers 100% of the viewport's size outside the viewport on each side (top, right, bottom, left). This has the highest GPU requirements.
ViewportSDFOversizeVIEWPORT_SDF_OVERSIZE_MAX=4
Represents the size of theViewportSDFOversizeenum.
enumViewportSDFScale:🔗
ViewportSDFScaleVIEWPORT_SDF_SCALE_100_PERCENT=0
Full resolution 2D signed distance field scale. This has the highest GPU requirements.
ViewportSDFScaleVIEWPORT_SDF_SCALE_50_PERCENT=1
Half resolution 2D signed distance field scale on each axis (25% of the viewport pixel count).
ViewportSDFScaleVIEWPORT_SDF_SCALE_25_PERCENT=2
Quarter resolution 2D signed distance field scale on each axis (6.25% of the viewport pixel count). This has the lowest GPU requirements.
ViewportSDFScaleVIEWPORT_SDF_SCALE_MAX=3
Represents the size of theViewportSDFScaleenum.
enumViewportMSAA:🔗
ViewportMSAAVIEWPORT_MSAA_DISABLED=0
Multisample antialiasing for 3D is disabled. This is the default value, and also the fastest setting.
ViewportMSAAVIEWPORT_MSAA_2X=1
Multisample antialiasing uses 2 samples per pixel for 3D. This has a moderate impact on performance.
ViewportMSAAVIEWPORT_MSAA_4X=2
Multisample antialiasing uses 4 samples per pixel for 3D. This has a high impact on performance.
ViewportMSAAVIEWPORT_MSAA_8X=3
Multisample antialiasing uses 8 samples per pixel for 3D. This has a very high impact on performance. Likely unsupported on low-end and older hardware.
ViewportMSAAVIEWPORT_MSAA_MAX=4
Represents the size of theViewportMSAAenum.
enumViewportAnisotropicFiltering:🔗
ViewportAnisotropicFilteringVIEWPORT_ANISOTROPY_DISABLED=0
Anisotropic filtering is disabled.
ViewportAnisotropicFilteringVIEWPORT_ANISOTROPY_2X=1
Use 2× anisotropic filtering.
ViewportAnisotropicFilteringVIEWPORT_ANISOTROPY_4X=2
Use 4× anisotropic filtering. This is the default value.
ViewportAnisotropicFilteringVIEWPORT_ANISOTROPY_8X=3
Use 8× anisotropic filtering.
ViewportAnisotropicFilteringVIEWPORT_ANISOTROPY_16X=4
Use 16× anisotropic filtering.
ViewportAnisotropicFilteringVIEWPORT_ANISOTROPY_MAX=5
Represents the size of theViewportAnisotropicFilteringenum.
enumViewportScreenSpaceAA:🔗
ViewportScreenSpaceAAVIEWPORT_SCREEN_SPACE_AA_DISABLED=0
Do not perform any antialiasing in the full screen post-process.
ViewportScreenSpaceAAVIEWPORT_SCREEN_SPACE_AA_FXAA=1
Use fast approximate antialiasing. FXAA is a popular screen-space antialiasing method, which is fast but will make the image look blurry, especially at lower resolutions. It can still work relatively well at large resolutions such as 1440p and 4K.
ViewportScreenSpaceAAVIEWPORT_SCREEN_SPACE_AA_SMAA=2
Use subpixel morphological antialiasing. SMAA may produce clearer results than FXAA, but at a slightly higher performance cost.
ViewportScreenSpaceAAVIEWPORT_SCREEN_SPACE_AA_MAX=3
Represents the size of theViewportScreenSpaceAAenum.
enumViewportOcclusionCullingBuildQuality:🔗
ViewportOcclusionCullingBuildQualityVIEWPORT_OCCLUSION_BUILD_QUALITY_LOW=0
Low occlusion culling BVH build quality (as defined by Embree). Results in the lowest CPU usage, but least effective culling.
ViewportOcclusionCullingBuildQualityVIEWPORT_OCCLUSION_BUILD_QUALITY_MEDIUM=1
Medium occlusion culling BVH build quality (as defined by Embree).
ViewportOcclusionCullingBuildQualityVIEWPORT_OCCLUSION_BUILD_QUALITY_HIGH=2
High occlusion culling BVH build quality (as defined by Embree). Results in the highest CPU usage, but most effective culling.
enumViewportRenderInfo:🔗
ViewportRenderInfoVIEWPORT_RENDER_INFO_OBJECTS_IN_FRAME=0
Number of objects drawn in a single frame.
ViewportRenderInfoVIEWPORT_RENDER_INFO_PRIMITIVES_IN_FRAME=1
Number of points, lines, or triangles drawn in a single frame.
ViewportRenderInfoVIEWPORT_RENDER_INFO_DRAW_CALLS_IN_FRAME=2
Number of draw calls during this frame.
ViewportRenderInfoVIEWPORT_RENDER_INFO_MAX=3
Represents the size of theViewportRenderInfoenum.
enumViewportRenderInfoType:🔗
ViewportRenderInfoTypeVIEWPORT_RENDER_INFO_TYPE_VISIBLE=0
Visible render pass (excluding shadows).
ViewportRenderInfoTypeVIEWPORT_RENDER_INFO_TYPE_SHADOW=1
Shadow render pass. Objects will be rendered several times depending on the number of amounts of lights with shadows and the number of directional shadow splits.
ViewportRenderInfoTypeVIEWPORT_RENDER_INFO_TYPE_CANVAS=2
Canvas item rendering. This includes all 2D rendering.
ViewportRenderInfoTypeVIEWPORT_RENDER_INFO_TYPE_MAX=3
Represents the size of theViewportRenderInfoTypeenum.
enumViewportDebugDraw:🔗
ViewportDebugDrawVIEWPORT_DEBUG_DRAW_DISABLED=0
Debug draw is disabled. Default setting.
ViewportDebugDrawVIEWPORT_DEBUG_DRAW_UNSHADED=1
Objects are displayed without light information.
ViewportDebugDrawVIEWPORT_DEBUG_DRAW_LIGHTING=2
Objects are displayed with only light information.
Note:When using this debug draw mode, custom shaders are ignored since all materials in the scene temporarily use a debug material. This means the result from custom shader functions (such as vertex displacement) won't be visible anymore when using this debug draw mode.
ViewportDebugDrawVIEWPORT_DEBUG_DRAW_OVERDRAW=3
Objects are displayed semi-transparent with additive blending so you can see where they are drawing over top of one another. A higher overdraw (represented by brighter colors) means you are wasting performance on drawing pixels that are being hidden behind others.
Note:When using this debug draw mode, custom shaders are ignored since all materials in the scene temporarily use a debug material. This means the result from custom shader functions (such as vertex displacement) won't be visible anymore when using this debug draw mode.
ViewportDebugDrawVIEWPORT_DEBUG_DRAW_WIREFRAME=4
Debug draw draws objects in wireframe.
Note:set_debug_generate_wireframes()must be called before loading any meshes for wireframes to be visible when using the Compatibility renderer.
ViewportDebugDrawVIEWPORT_DEBUG_DRAW_NORMAL_BUFFER=5
Normal buffer is drawn instead of regular scene so you can see the per-pixel normals that will be used by post-processing effects.
ViewportDebugDrawVIEWPORT_DEBUG_DRAW_VOXEL_GI_ALBEDO=6
Objects are displayed with only the albedo value fromVoxelGIs. Requires at least one visibleVoxelGInode that has been baked to have a visible effect.
Note:Only supported when using the Forward+ rendering method.
ViewportDebugDrawVIEWPORT_DEBUG_DRAW_VOXEL_GI_LIGHTING=7
Objects are displayed with only the lighting value fromVoxelGIs. Requires at least one visibleVoxelGInode that has been baked to have a visible effect.
Note:Only supported when using the Forward+ rendering method.
ViewportDebugDrawVIEWPORT_DEBUG_DRAW_VOXEL_GI_EMISSION=8
Objects are displayed with only the emission color fromVoxelGIs. Requires at least one visibleVoxelGInode that has been baked to have a visible effect.
Note:Only supported when using the Forward+ rendering method.
ViewportDebugDrawVIEWPORT_DEBUG_DRAW_SHADOW_ATLAS=9
Draws the shadow atlas that stores shadows fromOmniLight3Ds andSpotLight3Ds in the upper left quadrant of theViewport.
ViewportDebugDrawVIEWPORT_DEBUG_DRAW_DIRECTIONAL_SHADOW_ATLAS=10
Draws the shadow atlas that stores shadows fromDirectionalLight3Ds in the upper left quadrant of theViewport.
The slice of the camera frustum related to the shadow map cascade is superimposed to visualize coverage. The color of each slice matches the colors used forVIEWPORT_DEBUG_DRAW_PSSM_SPLITS. When shadow cascades are blended the overlap is taken into account when drawing the frustum slices.
The last cascade shows all frustum slices to illustrate the coverage of all slices.
ViewportDebugDrawVIEWPORT_DEBUG_DRAW_SCENE_LUMINANCE=11
Draws the estimated scene luminance. This is a 1×1 texture that is generated when autoexposure is enabled to control the scene's exposure.
Note:Only supported when using the Forward+ or Mobile rendering methods.
ViewportDebugDrawVIEWPORT_DEBUG_DRAW_SSAO=12
Draws the screen space ambient occlusion texture instead of the scene so that you can clearly see how it is affecting objects. In order for this display mode to work, you must haveEnvironment.ssao_enabledset in yourWorldEnvironment.
Note:Only supported when using the Forward+ rendering method.
ViewportDebugDrawVIEWPORT_DEBUG_DRAW_SSIL=13
Draws the screen space indirect lighting texture instead of the scene so that you can clearly see how it is affecting objects. In order for this display mode to work, you must haveEnvironment.ssil_enabledset in yourWorldEnvironment.
Note:Only supported when using the Forward+ rendering method.
ViewportDebugDrawVIEWPORT_DEBUG_DRAW_PSSM_SPLITS=14
Colors each PSSM split for theDirectionalLight3Ds in the scene a different color so you can see where the splits are. In order (from closest to furthest from the camera), they are colored red, green, blue, and yellow.
Note:When using this debug draw mode, custom shaders are ignored since all materials in the scene temporarily use a debug material. This means the result from custom shader functions (such as vertex displacement) won't be visible anymore when using this debug draw mode.
Note:Only supported when using the Forward+ or Mobile rendering methods.
ViewportDebugDrawVIEWPORT_DEBUG_DRAW_DECAL_ATLAS=15
Draws the decal atlas that stores decal textures fromDecals.
Note:Only supported when using the Forward+ or Mobile rendering methods.
ViewportDebugDrawVIEWPORT_DEBUG_DRAW_SDFGI=16
Draws SDFGI cascade data. This is the data structure that is used to bounce lighting against and create reflections.
Note:Only supported when using the Forward+ rendering method.
ViewportDebugDrawVIEWPORT_DEBUG_DRAW_SDFGI_PROBES=17
Draws SDFGI probe data. This is the data structure that is used to give indirect lighting dynamic objects moving within the scene.
When in the editor, left-clicking a probe will display additional bright dots that show its occlusion information. A white dot means the light is not occluded at all at the dot's position, while a red dot means the light is fully occluded. Intermediate values are possible.
Note:Only supported when using the Forward+ rendering method.
ViewportDebugDrawVIEWPORT_DEBUG_DRAW_GI_BUFFER=18
Draws the global illumination buffer fromVoxelGIor SDFGI. RequiresVoxelGI(at least one visible baked VoxelGI node) or SDFGI (Environment.sdfgi_enabled) to be enabled to have a visible effect.
Note:Only supported when using the Forward+ rendering method.
ViewportDebugDrawVIEWPORT_DEBUG_DRAW_DISABLE_LOD=19
Disable mesh LOD. All meshes are drawn with full detail, which can be used to compare performance.
ViewportDebugDrawVIEWPORT_DEBUG_DRAW_CLUSTER_OMNI_LIGHTS=20
Draws theOmniLight3Dcluster. Clustering determines where lights are positioned in screen-space, which allows the engine to only process these portions of the screen for lighting.
Note:Only supported when using the Forward+ rendering method.
ViewportDebugDrawVIEWPORT_DEBUG_DRAW_CLUSTER_SPOT_LIGHTS=21
Draws theSpotLight3Dcluster. Clustering determines where lights are positioned in screen-space, which allows the engine to only process these portions of the screen for lighting.
Note:Only supported when using the Forward+ rendering method.
ViewportDebugDrawVIEWPORT_DEBUG_DRAW_CLUSTER_DECALS=22
Draws theDecalcluster. Clustering determines where decals are positioned in screen-space, which allows the engine to only process these portions of the screen for decals.
Note:Only supported when using the Forward+ rendering method.
ViewportDebugDrawVIEWPORT_DEBUG_DRAW_CLUSTER_REFLECTION_PROBES=23
Draws theReflectionProbecluster. Clustering determines where reflection probes are positioned in screen-space, which allows the engine to only process these portions of the screen for reflection probes.
Note:Only supported when using the Forward+ rendering method.
ViewportDebugDrawVIEWPORT_DEBUG_DRAW_OCCLUDERS=24
Draws the occlusion culling buffer. This low-resolution occlusion culling buffer is rasterized on the CPU and is used to check whether instances are occluded by other objects.
Note:Only supported when using the Forward+ or Mobile rendering methods.
ViewportDebugDrawVIEWPORT_DEBUG_DRAW_MOTION_VECTORS=25
Draws the motion vectors buffer. This is used by temporal antialiasing to correct for motion that occurs during gameplay.
Note:Only supported when using the Forward+ rendering method.
ViewportDebugDrawVIEWPORT_DEBUG_DRAW_INTERNAL_BUFFER=26
Internal buffer is drawn instead of regular scene so you can see the per-pixel output that will be used by post-processing effects.
Note:Only supported when using the Forward+ or Mobile rendering methods.
enumViewportVRSMode:🔗
ViewportVRSModeVIEWPORT_VRS_DISABLED=0
Variable rate shading is disabled.
ViewportVRSModeVIEWPORT_VRS_TEXTURE=1
Variable rate shading uses a texture. Note, for stereoscopic use a texture atlas with a texture for each view.
ViewportVRSModeVIEWPORT_VRS_XR=2
Variable rate shading texture is supplied by the primaryXRInterface. Note that this may override the update mode.
ViewportVRSModeVIEWPORT_VRS_MAX=3
Represents the size of theViewportVRSModeenum.
enumViewportVRSUpdateMode:🔗
ViewportVRSUpdateModeVIEWPORT_VRS_UPDATE_DISABLED=0
The input texture for variable rate shading will not be processed.
ViewportVRSUpdateModeVIEWPORT_VRS_UPDATE_ONCE=1
The input texture for variable rate shading will be processed once.
ViewportVRSUpdateModeVIEWPORT_VRS_UPDATE_ALWAYS=2
The input texture for variable rate shading will be processed each frame.
ViewportVRSUpdateModeVIEWPORT_VRS_UPDATE_MAX=3
Represents the size of theViewportVRSUpdateModeenum.
enumSkyMode:🔗
SkyModeSKY_MODE_AUTOMATIC=0
Automatically selects the appropriate process mode based on your sky shader. If your shader usesTIMEorPOSITION, this will useSKY_MODE_REALTIME. If your shader uses any of theLIGHT_*variables or any custom uniforms, this usesSKY_MODE_INCREMENTAL. Otherwise, this defaults toSKY_MODE_QUALITY.
SkyModeSKY_MODE_QUALITY=1
Uses high quality importance sampling to process the radiance map. In general, this results in much higher quality thanSKY_MODE_REALTIMEbut takes much longer to generate. This should not be used if you plan on changing the sky at runtime. If you are finding that the reflection is not blurry enough and is showing sparkles or fireflies, try increasingProjectSettings.rendering/reflections/sky_reflections/ggx_samples.
SkyModeSKY_MODE_INCREMENTAL=2
Uses the same high quality importance sampling to process the radiance map asSKY_MODE_QUALITY, but updates over several frames. The number of frames is determined byProjectSettings.rendering/reflections/sky_reflections/roughness_layers. Use this when you need highest quality radiance maps, but have a sky that updates slowly.
SkyModeSKY_MODE_REALTIME=3
Uses the fast filtering algorithm to process the radiance map. In general this results in lower quality, but substantially faster run times. If you need better quality, but still need to update the sky every frame, consider turning onProjectSettings.rendering/reflections/sky_reflections/fast_filter_high_quality.
Note:The fast filtering algorithm is limited to 256×256 cubemaps, sosky_set_radiance_size()must be set to256. Otherwise, a warning is printed and the overridden radiance size is ignored.
enumCompositorEffectFlags:🔗
CompositorEffectFlagsCOMPOSITOR_EFFECT_FLAG_ACCESS_RESOLVED_COLOR=1
The rendering effect requires the color buffer to be resolved if MSAA is enabled.
CompositorEffectFlagsCOMPOSITOR_EFFECT_FLAG_ACCESS_RESOLVED_DEPTH=2
The rendering effect requires the depth buffer to be resolved if MSAA is enabled.
CompositorEffectFlagsCOMPOSITOR_EFFECT_FLAG_NEEDS_MOTION_VECTORS=4
The rendering effect requires motion vectors to be produced.
CompositorEffectFlagsCOMPOSITOR_EFFECT_FLAG_NEEDS_ROUGHNESS=8
The rendering effect requires normals and roughness g-buffer to be produced (Forward+ only).
CompositorEffectFlagsCOMPOSITOR_EFFECT_FLAG_NEEDS_SEPARATE_SPECULAR=16
The rendering effect requires specular data to be separated out (Forward+ only).
enumCompositorEffectCallbackType:🔗
CompositorEffectCallbackTypeCOMPOSITOR_EFFECT_CALLBACK_TYPE_PRE_OPAQUE=0
The callback is called before our opaque rendering pass, but after depth prepass (if applicable).
CompositorEffectCallbackTypeCOMPOSITOR_EFFECT_CALLBACK_TYPE_POST_OPAQUE=1
The callback is called after our opaque rendering pass, but before our sky is rendered.
CompositorEffectCallbackTypeCOMPOSITOR_EFFECT_CALLBACK_TYPE_POST_SKY=2
The callback is called after our sky is rendered, but before our back buffers are created (and if enabled, before subsurface scattering and/or screen space reflections).
CompositorEffectCallbackTypeCOMPOSITOR_EFFECT_CALLBACK_TYPE_PRE_TRANSPARENT=3
The callback is called before our transparent rendering pass, but after our sky is rendered and we've created our back buffers.
CompositorEffectCallbackTypeCOMPOSITOR_EFFECT_CALLBACK_TYPE_POST_TRANSPARENT=4
The callback is called after our transparent rendering pass, but before any built-in post-processing effects and output to our render target.
CompositorEffectCallbackTypeCOMPOSITOR_EFFECT_CALLBACK_TYPE_ANY=-1
There is currently no description for this enum. Please help us bycontributing one!
enumEnvironmentBG:🔗
EnvironmentBGENV_BG_CLEAR_COLOR=0
Use the clear color as background.
EnvironmentBGENV_BG_COLOR=1
Use a specified color as the background.
EnvironmentBGENV_BG_SKY=2
Use a sky resource for the background.
EnvironmentBGENV_BG_CANVAS=3
Use a specified canvas layer as the background. This can be useful for instantiating a 2D scene in a 3D world.
EnvironmentBGENV_BG_KEEP=4
Do not clear the background, use whatever was rendered last frame as the background.
EnvironmentBGENV_BG_CAMERA_FEED=5
Displays a camera feed in the background.
EnvironmentBGENV_BG_MAX=6
Represents the size of theEnvironmentBGenum.
enumEnvironmentAmbientSource:🔗
EnvironmentAmbientSourceENV_AMBIENT_SOURCE_BG=0
Gather ambient light from whichever source is specified as the background.
EnvironmentAmbientSourceENV_AMBIENT_SOURCE_DISABLED=1
Disable ambient light.
EnvironmentAmbientSourceENV_AMBIENT_SOURCE_COLOR=2
Specify a specificColorfor ambient light.
EnvironmentAmbientSourceENV_AMBIENT_SOURCE_SKY=3
Gather ambient light from theSkyregardless of what the background is.
enumEnvironmentReflectionSource:🔗
EnvironmentReflectionSourceENV_REFLECTION_SOURCE_BG=0
Use the background for reflections.
EnvironmentReflectionSourceENV_REFLECTION_SOURCE_DISABLED=1
Disable reflections.
EnvironmentReflectionSourceENV_REFLECTION_SOURCE_SKY=2
Use theSkyfor reflections regardless of what the background is.
enumEnvironmentGlowBlendMode:🔗
EnvironmentGlowBlendModeENV_GLOW_BLEND_MODE_ADDITIVE=0
Additive glow blending mode. Mostly used for particles, glows (bloom), lens flare, bright sources.
EnvironmentGlowBlendModeENV_GLOW_BLEND_MODE_SCREEN=1
Screen glow blending mode. Increases brightness, used frequently with bloom.
EnvironmentGlowBlendModeENV_GLOW_BLEND_MODE_SOFTLIGHT=2
Soft light glow blending mode. Modifies contrast, exposes shadows and highlights (vivid bloom).
EnvironmentGlowBlendModeENV_GLOW_BLEND_MODE_REPLACE=3
Replace glow blending mode. Replaces all pixels' color by the glow value. This can be used to simulate a full-screen blur effect by tweaking the glow parameters to match the original image's brightness.
EnvironmentGlowBlendModeENV_GLOW_BLEND_MODE_MIX=4
Mixes the glow with the underlying color to avoid increasing brightness as much while still maintaining a glow effect.
enumEnvironmentFogMode:🔗
EnvironmentFogModeENV_FOG_MODE_EXPONENTIAL=0
Use a physically-based fog model defined primarily by fog density.
EnvironmentFogModeENV_FOG_MODE_DEPTH=1
Use a simple fog model defined by start and end positions and a custom curve. While not physically accurate, this model can be useful when you need more artistic control.
enumEnvironmentToneMapper:🔗
EnvironmentToneMapperENV_TONE_MAPPER_LINEAR=0
Does not modify color data, resulting in a linear tonemapping curve which unnaturally clips bright values, causing bright lighting to look blown out. The simplest and fastest tonemapper.
EnvironmentToneMapperENV_TONE_MAPPER_REINHARD=1
A simple tonemapping curve that rolls off bright values to prevent clipping. This results in an image that can appear dull and low contrast. Slower thanENV_TONE_MAPPER_LINEAR.
Note:WhenEnvironment.tonemap_whiteis left at the default value of1.0,ENV_TONE_MAPPER_REINHARDproduces an identical image toENV_TONE_MAPPER_LINEAR.
EnvironmentToneMapperENV_TONE_MAPPER_FILMIC=2
Uses a film-like tonemapping curve to prevent clipping of bright values and provide better contrast thanENV_TONE_MAPPER_REINHARD. Slightly slower thanENV_TONE_MAPPER_REINHARD.
EnvironmentToneMapperENV_TONE_MAPPER_ACES=3
Uses a high-contrast film-like tonemapping curve and desaturates bright values for a more realistic appearance. Slightly slower thanENV_TONE_MAPPER_FILMIC.
Note:This tonemapping operator is called "ACES Fitted" in Godot 3.x.
EnvironmentToneMapperENV_TONE_MAPPER_AGX=4
Uses an adjustable film-like tonemapping curve and desaturates bright values for a more realistic appearance. Better than other tonemappers at maintaining the hue of colors as they become brighter. The slowest tonemapping option.
enumEnvironmentSSRRoughnessQuality:🔗
EnvironmentSSRRoughnessQualityENV_SSR_ROUGHNESS_QUALITY_DISABLED=0
Lowest quality of roughness filter for screen-space reflections. Rough materials will not have blurrier screen-space reflections compared to smooth (non-rough) materials. This is the fastest option.
EnvironmentSSRRoughnessQualityENV_SSR_ROUGHNESS_QUALITY_LOW=1
Low quality of roughness filter for screen-space reflections.
EnvironmentSSRRoughnessQualityENV_SSR_ROUGHNESS_QUALITY_MEDIUM=2
Medium quality of roughness filter for screen-space reflections.
EnvironmentSSRRoughnessQualityENV_SSR_ROUGHNESS_QUALITY_HIGH=3
High quality of roughness filter for screen-space reflections. This is the slowest option.
enumEnvironmentSSAOQuality:🔗
EnvironmentSSAOQualityENV_SSAO_QUALITY_VERY_LOW=0
Lowest quality of screen-space ambient occlusion.
EnvironmentSSAOQualityENV_SSAO_QUALITY_LOW=1
Low quality screen-space ambient occlusion.
EnvironmentSSAOQualityENV_SSAO_QUALITY_MEDIUM=2
Medium quality screen-space ambient occlusion.
EnvironmentSSAOQualityENV_SSAO_QUALITY_HIGH=3
High quality screen-space ambient occlusion.
EnvironmentSSAOQualityENV_SSAO_QUALITY_ULTRA=4
Highest quality screen-space ambient occlusion. Uses the adaptive target setting which can be dynamically adjusted to smoothly balance performance and visual quality.
enumEnvironmentSSILQuality:🔗
EnvironmentSSILQualityENV_SSIL_QUALITY_VERY_LOW=0
Lowest quality of screen-space indirect lighting.
EnvironmentSSILQualityENV_SSIL_QUALITY_LOW=1
Low quality screen-space indirect lighting.
EnvironmentSSILQualityENV_SSIL_QUALITY_MEDIUM=2
High quality screen-space indirect lighting.
EnvironmentSSILQualityENV_SSIL_QUALITY_HIGH=3
High quality screen-space indirect lighting.
EnvironmentSSILQualityENV_SSIL_QUALITY_ULTRA=4
Highest quality screen-space indirect lighting. Uses the adaptive target setting which can be dynamically adjusted to smoothly balance performance and visual quality.
enumEnvironmentSDFGIYScale:🔗
EnvironmentSDFGIYScaleENV_SDFGI_Y_SCALE_50_PERCENT=0
Use 50% scale for SDFGI on the Y (vertical) axis. SDFGI cells will be twice as short as they are wide. This allows providing increased GI detail and reduced light leaking with thin floors and ceilings. This is usually the best choice for scenes that don't feature much verticality.
EnvironmentSDFGIYScaleENV_SDFGI_Y_SCALE_75_PERCENT=1
Use 75% scale for SDFGI on the Y (vertical) axis. This is a balance between the 50% and 100% SDFGI Y scales.
EnvironmentSDFGIYScaleENV_SDFGI_Y_SCALE_100_PERCENT=2
Use 100% scale for SDFGI on the Y (vertical) axis. SDFGI cells will be as tall as they are wide. This is usually the best choice for highly vertical scenes. The downside is that light leaking may become more noticeable with thin floors and ceilings.
enumEnvironmentSDFGIRayCount:🔗
EnvironmentSDFGIRayCountENV_SDFGI_RAY_COUNT_4=0
Throw 4 rays per frame when converging SDFGI. This has the lowest GPU requirements, but creates the most noisy result.
EnvironmentSDFGIRayCountENV_SDFGI_RAY_COUNT_8=1
Throw 8 rays per frame when converging SDFGI.
EnvironmentSDFGIRayCountENV_SDFGI_RAY_COUNT_16=2
Throw 16 rays per frame when converging SDFGI.
EnvironmentSDFGIRayCountENV_SDFGI_RAY_COUNT_32=3
Throw 32 rays per frame when converging SDFGI.
EnvironmentSDFGIRayCountENV_SDFGI_RAY_COUNT_64=4
Throw 64 rays per frame when converging SDFGI.
EnvironmentSDFGIRayCountENV_SDFGI_RAY_COUNT_96=5
Throw 96 rays per frame when converging SDFGI. This has high GPU requirements.
EnvironmentSDFGIRayCountENV_SDFGI_RAY_COUNT_128=6
Throw 128 rays per frame when converging SDFGI. This has very high GPU requirements, but creates the least noisy result.
EnvironmentSDFGIRayCountENV_SDFGI_RAY_COUNT_MAX=7
Represents the size of theEnvironmentSDFGIRayCountenum.
enumEnvironmentSDFGIFramesToConverge:🔗
EnvironmentSDFGIFramesToConvergeENV_SDFGI_CONVERGE_IN_5_FRAMES=0
Converge SDFGI over 5 frames. This is the most responsive, but creates the most noisy result with a given ray count.
EnvironmentSDFGIFramesToConvergeENV_SDFGI_CONVERGE_IN_10_FRAMES=1
Configure SDFGI to fully converge over 10 frames.
EnvironmentSDFGIFramesToConvergeENV_SDFGI_CONVERGE_IN_15_FRAMES=2
Configure SDFGI to fully converge over 15 frames.
EnvironmentSDFGIFramesToConvergeENV_SDFGI_CONVERGE_IN_20_FRAMES=3
Configure SDFGI to fully converge over 20 frames.
EnvironmentSDFGIFramesToConvergeENV_SDFGI_CONVERGE_IN_25_FRAMES=4
Configure SDFGI to fully converge over 25 frames.
EnvironmentSDFGIFramesToConvergeENV_SDFGI_CONVERGE_IN_30_FRAMES=5
Configure SDFGI to fully converge over 30 frames. This is the least responsive, but creates the least noisy result with a given ray count.
EnvironmentSDFGIFramesToConvergeENV_SDFGI_CONVERGE_MAX=6
Represents the size of theEnvironmentSDFGIFramesToConvergeenum.
enumEnvironmentSDFGIFramesToUpdateLight:🔗
EnvironmentSDFGIFramesToUpdateLightENV_SDFGI_UPDATE_LIGHT_IN_1_FRAME=0
Update indirect light from dynamic lights in SDFGI over 1 frame. This is the most responsive, but has the highest GPU requirements.
EnvironmentSDFGIFramesToUpdateLightENV_SDFGI_UPDATE_LIGHT_IN_2_FRAMES=1
Update indirect light from dynamic lights in SDFGI over 2 frames.
EnvironmentSDFGIFramesToUpdateLightENV_SDFGI_UPDATE_LIGHT_IN_4_FRAMES=2
Update indirect light from dynamic lights in SDFGI over 4 frames.
EnvironmentSDFGIFramesToUpdateLightENV_SDFGI_UPDATE_LIGHT_IN_8_FRAMES=3
Update indirect light from dynamic lights in SDFGI over 8 frames.
EnvironmentSDFGIFramesToUpdateLightENV_SDFGI_UPDATE_LIGHT_IN_16_FRAMES=4
Update indirect light from dynamic lights in SDFGI over 16 frames. This is the least responsive, but has the lowest GPU requirements.
EnvironmentSDFGIFramesToUpdateLightENV_SDFGI_UPDATE_LIGHT_MAX=5
Represents the size of theEnvironmentSDFGIFramesToUpdateLightenum.
enumSubSurfaceScatteringQuality:🔗
SubSurfaceScatteringQualitySUB_SURFACE_SCATTERING_QUALITY_DISABLED=0
Disables subsurface scattering entirely, even on materials that haveBaseMaterial3D.subsurf_scatter_enabledset totrue. This has the lowest GPU requirements.
SubSurfaceScatteringQualitySUB_SURFACE_SCATTERING_QUALITY_LOW=1
Low subsurface scattering quality.
SubSurfaceScatteringQualitySUB_SURFACE_SCATTERING_QUALITY_MEDIUM=2
Medium subsurface scattering quality.
SubSurfaceScatteringQualitySUB_SURFACE_SCATTERING_QUALITY_HIGH=3
High subsurface scattering quality. This has the highest GPU requirements.
enumDOFBokehShape:🔗
DOFBokehShapeDOF_BOKEH_BOX=0
Calculate the DOF blur using a box filter. The fastest option, but results in obvious lines in blur pattern.
DOFBokehShapeDOF_BOKEH_HEXAGON=1
Calculates DOF blur using a hexagon shaped filter.
DOFBokehShapeDOF_BOKEH_CIRCLE=2
Calculates DOF blur using a circle shaped filter. Best quality and most realistic, but slowest. Use only for areas where a lot of performance can be dedicated to post-processing (e.g. cutscenes).
enumDOFBlurQuality:🔗
DOFBlurQualityDOF_BLUR_QUALITY_VERY_LOW=0
Lowest quality DOF blur. This is the fastest setting, but you may be able to see filtering artifacts.
DOFBlurQualityDOF_BLUR_QUALITY_LOW=1
Low quality DOF blur.
DOFBlurQualityDOF_BLUR_QUALITY_MEDIUM=2
Medium quality DOF blur.
DOFBlurQualityDOF_BLUR_QUALITY_HIGH=3
Highest quality DOF blur. Results in the smoothest looking blur by taking the most samples, but is also significantly slower.
enumInstanceType:🔗
InstanceTypeINSTANCE_NONE=0
The instance does not have a type.
InstanceTypeINSTANCE_MESH=1
The instance is a mesh.
InstanceTypeINSTANCE_MULTIMESH=2
The instance is a multimesh.
InstanceTypeINSTANCE_PARTICLES=3
The instance is a particle emitter.
InstanceTypeINSTANCE_PARTICLES_COLLISION=4
The instance is a GPUParticles collision shape.
InstanceTypeINSTANCE_LIGHT=5
The instance is a light.
InstanceTypeINSTANCE_REFLECTION_PROBE=6
The instance is a reflection probe.
InstanceTypeINSTANCE_DECAL=7
The instance is a decal.
InstanceTypeINSTANCE_VOXEL_GI=8
The instance is a VoxelGI.
InstanceTypeINSTANCE_LIGHTMAP=9
The instance is a lightmap.
InstanceTypeINSTANCE_OCCLUDER=10
The instance is an occlusion culling occluder.
InstanceTypeINSTANCE_VISIBLITY_NOTIFIER=11
The instance is a visible on-screen notifier.
InstanceTypeINSTANCE_FOG_VOLUME=12
The instance is a fog volume.
InstanceTypeINSTANCE_MAX=13
Represents the size of theInstanceTypeenum.
InstanceTypeINSTANCE_GEOMETRY_MASK=14
A combination of the flags of geometry instances (mesh, multimesh, immediate and particles).
enumInstanceFlags:🔗
InstanceFlagsINSTANCE_FLAG_USE_BAKED_LIGHT=0
Allows the instance to be used in baked lighting.
InstanceFlagsINSTANCE_FLAG_USE_DYNAMIC_GI=1
Allows the instance to be used with dynamic global illumination.
InstanceFlagsINSTANCE_FLAG_DRAW_NEXT_FRAME_IF_VISIBLE=2
When set, manually requests to draw geometry on next frame.
InstanceFlagsINSTANCE_FLAG_IGNORE_OCCLUSION_CULLING=3
Always draw, even if the instance would be culled by occlusion culling. Does not affect view frustum culling.
InstanceFlagsINSTANCE_FLAG_MAX=4
Represents the size of theInstanceFlagsenum.
enumShadowCastingSetting:🔗
ShadowCastingSettingSHADOW_CASTING_SETTING_OFF=0
Disable shadows from this instance.
ShadowCastingSettingSHADOW_CASTING_SETTING_ON=1
Cast shadows from this instance.
ShadowCastingSettingSHADOW_CASTING_SETTING_DOUBLE_SIDED=2
Disable backface culling when rendering the shadow of the object. This is slightly slower but may result in more correct shadows.
ShadowCastingSettingSHADOW_CASTING_SETTING_SHADOWS_ONLY=3
Only render the shadows from the object. The object itself will not be drawn.
enumVisibilityRangeFadeMode:🔗
VisibilityRangeFadeModeVISIBILITY_RANGE_FADE_DISABLED=0
Disable visibility range fading for the given instance.
VisibilityRangeFadeModeVISIBILITY_RANGE_FADE_SELF=1
Fade-out the given instance when it approaches its visibility range limits.
VisibilityRangeFadeModeVISIBILITY_RANGE_FADE_DEPENDENCIES=2
Fade-in the given instance's dependencies when reaching its visibility range limits.
enumBakeChannels:🔗
BakeChannelsBAKE_CHANNEL_ALBEDO_ALPHA=0
Index ofImagein array ofImages returned bybake_render_uv2(). Image usesImage.FORMAT_RGBA8and contains albedo color in the.rgbchannels and alpha in the.achannel.
BakeChannelsBAKE_CHANNEL_NORMAL=1
Index ofImagein array ofImages returned bybake_render_uv2(). Image usesImage.FORMAT_RGBA8and contains the per-pixel normal of the object in the.rgbchannels and nothing in the.achannel. The per-pixel normal is encoded asnormal*0.5+0.5.
BakeChannelsBAKE_CHANNEL_ORM=2
Index ofImagein array ofImages returned bybake_render_uv2(). Image usesImage.FORMAT_RGBA8and contains ambient occlusion (from material and decals only) in the.rchannel, roughness in the.gchannel, metallic in the.bchannel and sub surface scattering amount in the.achannel.
BakeChannelsBAKE_CHANNEL_EMISSION=3
Index ofImagein array ofImages returned bybake_render_uv2(). Image usesImage.FORMAT_RGBAHand contains emission color in the.rgbchannels and nothing in the.achannel.
enumCanvasTextureChannel:🔗
CanvasTextureChannelCANVAS_TEXTURE_CHANNEL_DIFFUSE=0
Diffuse canvas texture (CanvasTexture.diffuse_texture).
CanvasTextureChannelCANVAS_TEXTURE_CHANNEL_NORMAL=1
Normal map canvas texture (CanvasTexture.normal_texture).
CanvasTextureChannelCANVAS_TEXTURE_CHANNEL_SPECULAR=2
Specular map canvas texture (CanvasTexture.specular_texture).
enumNinePatchAxisMode:🔗
NinePatchAxisModeNINE_PATCH_STRETCH=0
The nine patch gets stretched where needed.
NinePatchAxisModeNINE_PATCH_TILE=1
The nine patch gets filled with tiles where needed.
NinePatchAxisModeNINE_PATCH_TILE_FIT=2
The nine patch gets filled with tiles where needed and stretches them a bit if needed.
enumCanvasItemTextureFilter:🔗
CanvasItemTextureFilterCANVAS_ITEM_TEXTURE_FILTER_DEFAULT=0
Uses the default filter mode for thisViewport.
CanvasItemTextureFilterCANVAS_ITEM_TEXTURE_FILTER_NEAREST=1
The texture filter reads from the nearest pixel only. This makes the texture look pixelated from up close, and grainy from a distance (due to mipmaps not being sampled).
CanvasItemTextureFilterCANVAS_ITEM_TEXTURE_FILTER_LINEAR=2
The texture filter blends between the nearest 4 pixels. This makes the texture look smooth from up close, and grainy from a distance (due to mipmaps not being sampled).
CanvasItemTextureFilterCANVAS_ITEM_TEXTURE_FILTER_NEAREST_WITH_MIPMAPS=3
The texture filter reads from the nearest pixel and blends between the nearest 2 mipmaps (or uses the nearest mipmap ifProjectSettings.rendering/textures/default_filters/use_nearest_mipmap_filteristrue). This makes the texture look pixelated from up close, and smooth from a distance.
Use this for non-pixel art textures that may be viewed at a low scale (e.g. due toCamera2Dzoom or sprite scaling), as mipmaps are important to smooth out pixels that are smaller than on-screen pixels.
CanvasItemTextureFilterCANVAS_ITEM_TEXTURE_FILTER_LINEAR_WITH_MIPMAPS=4
The texture filter blends between the nearest 4 pixels and between the nearest 2 mipmaps (or uses the nearest mipmap ifProjectSettings.rendering/textures/default_filters/use_nearest_mipmap_filteristrue). This makes the texture look smooth from up close, and smooth from a distance.
Use this for non-pixel art textures that may be viewed at a low scale (e.g. due toCamera2Dzoom or sprite scaling), as mipmaps are important to smooth out pixels that are smaller than on-screen pixels.
CanvasItemTextureFilterCANVAS_ITEM_TEXTURE_FILTER_NEAREST_WITH_MIPMAPS_ANISOTROPIC=5
The texture filter reads from the nearest pixel and blends between 2 mipmaps (or uses the nearest mipmap ifProjectSettings.rendering/textures/default_filters/use_nearest_mipmap_filteristrue) based on the angle between the surface and the camera view. This makes the texture look pixelated from up close, and smooth from a distance. Anisotropic filtering improves texture quality on surfaces that are almost in line with the camera, but is slightly slower. The anisotropic filtering level can be changed by adjustingProjectSettings.rendering/textures/default_filters/anisotropic_filtering_level.
Note:This texture filter is rarely useful in 2D projects.CANVAS_ITEM_TEXTURE_FILTER_NEAREST_WITH_MIPMAPSis usually more appropriate in this case.
CanvasItemTextureFilterCANVAS_ITEM_TEXTURE_FILTER_LINEAR_WITH_MIPMAPS_ANISOTROPIC=6
The texture filter blends between the nearest 4 pixels and blends between 2 mipmaps (or uses the nearest mipmap ifProjectSettings.rendering/textures/default_filters/use_nearest_mipmap_filteristrue) based on the angle between the surface and the camera view. This makes the texture look smooth from up close, and smooth from a distance. Anisotropic filtering improves texture quality on surfaces that are almost in line with the camera, but is slightly slower. The anisotropic filtering level can be changed by adjustingProjectSettings.rendering/textures/default_filters/anisotropic_filtering_level.
Note:This texture filter is rarely useful in 2D projects.CANVAS_ITEM_TEXTURE_FILTER_LINEAR_WITH_MIPMAPSis usually more appropriate in this case.
CanvasItemTextureFilterCANVAS_ITEM_TEXTURE_FILTER_MAX=7
Max value forCanvasItemTextureFilterenum.
enumCanvasItemTextureRepeat:🔗
CanvasItemTextureRepeatCANVAS_ITEM_TEXTURE_REPEAT_DEFAULT=0
Uses the default repeat mode for thisViewport.
CanvasItemTextureRepeatCANVAS_ITEM_TEXTURE_REPEAT_DISABLED=1
Disables textures repeating. Instead, when reading UVs outside the 0-1 range, the value will be clamped to the edge of the texture, resulting in a stretched out look at the borders of the texture.
CanvasItemTextureRepeatCANVAS_ITEM_TEXTURE_REPEAT_ENABLED=2
Enables the texture to repeat when UV coordinates are outside the 0-1 range. If using one of the linear filtering modes, this can result in artifacts at the edges of a texture when the sampler filters across the edges of the texture.
CanvasItemTextureRepeatCANVAS_ITEM_TEXTURE_REPEAT_MIRROR=3
Flip the texture when repeating so that the edge lines up instead of abruptly changing.
CanvasItemTextureRepeatCANVAS_ITEM_TEXTURE_REPEAT_MAX=4
Max value forCanvasItemTextureRepeatenum.
enumCanvasGroupMode:🔗
CanvasGroupModeCANVAS_GROUP_MODE_DISABLED=0
Child draws over parent and is not clipped.
CanvasGroupModeCANVAS_GROUP_MODE_CLIP_ONLY=1
Parent is used for the purposes of clipping only. Child is clipped to the parent's visible area, parent is not drawn.
CanvasGroupModeCANVAS_GROUP_MODE_CLIP_AND_DRAW=2
Parent is used for clipping child, but parent is also drawn underneath child as normal before clipping child to its visible area.
CanvasGroupModeCANVAS_GROUP_MODE_TRANSPARENT=3
There is currently no description for this enum. Please help us bycontributing one!
enumCanvasLightMode:🔗
CanvasLightModeCANVAS_LIGHT_MODE_POINT=0
2D point light (seePointLight2D).
CanvasLightModeCANVAS_LIGHT_MODE_DIRECTIONAL=1
2D directional (sun/moon) light (seeDirectionalLight2D).
enumCanvasLightBlendMode:🔗
CanvasLightBlendModeCANVAS_LIGHT_BLEND_MODE_ADD=0
Adds light color additive to the canvas.
CanvasLightBlendModeCANVAS_LIGHT_BLEND_MODE_SUB=1
Adds light color subtractive to the canvas.
CanvasLightBlendModeCANVAS_LIGHT_BLEND_MODE_MIX=2
The light adds color depending on transparency.
enumCanvasLightShadowFilter:🔗
CanvasLightShadowFilterCANVAS_LIGHT_FILTER_NONE=0
Do not apply a filter to canvas light shadows.
CanvasLightShadowFilterCANVAS_LIGHT_FILTER_PCF5=1
Use PCF5 filtering to filter canvas light shadows.
CanvasLightShadowFilterCANVAS_LIGHT_FILTER_PCF13=2
Use PCF13 filtering to filter canvas light shadows.
CanvasLightShadowFilterCANVAS_LIGHT_FILTER_MAX=3
Max value of theCanvasLightShadowFilterenum.
enumCanvasOccluderPolygonCullMode:🔗
CanvasOccluderPolygonCullModeCANVAS_OCCLUDER_POLYGON_CULL_DISABLED=0
Culling of the canvas occluder is disabled.
CanvasOccluderPolygonCullModeCANVAS_OCCLUDER_POLYGON_CULL_CLOCKWISE=1
Culling of the canvas occluder is clockwise.
CanvasOccluderPolygonCullModeCANVAS_OCCLUDER_POLYGON_CULL_COUNTER_CLOCKWISE=2
Culling of the canvas occluder is counterclockwise.
enumGlobalShaderParameterType:🔗
GlobalShaderParameterTypeGLOBAL_VAR_TYPE_BOOL=0
Boolean global shader parameter (globaluniformbool...).
GlobalShaderParameterTypeGLOBAL_VAR_TYPE_BVEC2=1
2-dimensional boolean vector global shader parameter (globaluniformbvec2...).
GlobalShaderParameterTypeGLOBAL_VAR_TYPE_BVEC3=2
3-dimensional boolean vector global shader parameter (globaluniformbvec3...).
GlobalShaderParameterTypeGLOBAL_VAR_TYPE_BVEC4=3
4-dimensional boolean vector global shader parameter (globaluniformbvec4...).
GlobalShaderParameterTypeGLOBAL_VAR_TYPE_INT=4
Integer global shader parameter (globaluniformint...).
GlobalShaderParameterTypeGLOBAL_VAR_TYPE_IVEC2=5
2-dimensional integer vector global shader parameter (globaluniformivec2...).
GlobalShaderParameterTypeGLOBAL_VAR_TYPE_IVEC3=6
3-dimensional integer vector global shader parameter (globaluniformivec3...).
GlobalShaderParameterTypeGLOBAL_VAR_TYPE_IVEC4=7
4-dimensional integer vector global shader parameter (globaluniformivec4...).
GlobalShaderParameterTypeGLOBAL_VAR_TYPE_RECT2I=8
2-dimensional integer rectangle global shader parameter (globaluniformivec4...). Equivalent toGLOBAL_VAR_TYPE_IVEC4in shader code, but exposed as aRect2iin the editor UI.
GlobalShaderParameterTypeGLOBAL_VAR_TYPE_UINT=9
Unsigned integer global shader parameter (globaluniformuint...).
GlobalShaderParameterTypeGLOBAL_VAR_TYPE_UVEC2=10
2-dimensional unsigned integer vector global shader parameter (globaluniformuvec2...).
GlobalShaderParameterTypeGLOBAL_VAR_TYPE_UVEC3=11
3-dimensional unsigned integer vector global shader parameter (globaluniformuvec3...).
GlobalShaderParameterTypeGLOBAL_VAR_TYPE_UVEC4=12
4-dimensional unsigned integer vector global shader parameter (globaluniformuvec4...).
GlobalShaderParameterTypeGLOBAL_VAR_TYPE_FLOAT=13
Single-precision floating-point global shader parameter (globaluniformfloat...).
GlobalShaderParameterTypeGLOBAL_VAR_TYPE_VEC2=14
2-dimensional floating-point vector global shader parameter (globaluniformvec2...).
GlobalShaderParameterTypeGLOBAL_VAR_TYPE_VEC3=15
3-dimensional floating-point vector global shader parameter (globaluniformvec3...).
GlobalShaderParameterTypeGLOBAL_VAR_TYPE_VEC4=16
4-dimensional floating-point vector global shader parameter (globaluniformvec4...).
GlobalShaderParameterTypeGLOBAL_VAR_TYPE_COLOR=17
Color global shader parameter (globaluniformvec4...). Equivalent toGLOBAL_VAR_TYPE_VEC4in shader code, but exposed as aColorin the editor UI.
GlobalShaderParameterTypeGLOBAL_VAR_TYPE_RECT2=18
2-dimensional floating-point rectangle global shader parameter (globaluniformvec4...). Equivalent toGLOBAL_VAR_TYPE_VEC4in shader code, but exposed as aRect2in the editor UI.
GlobalShaderParameterTypeGLOBAL_VAR_TYPE_MAT2=19
2×2 matrix global shader parameter (globaluniformmat2...). Exposed as aPackedInt32Arrayin the editor UI.
GlobalShaderParameterTypeGLOBAL_VAR_TYPE_MAT3=20
3×3 matrix global shader parameter (globaluniformmat3...). Exposed as aBasisin the editor UI.
GlobalShaderParameterTypeGLOBAL_VAR_TYPE_MAT4=21
4×4 matrix global shader parameter (globaluniformmat4...). Exposed as aProjectionin the editor UI.
GlobalShaderParameterTypeGLOBAL_VAR_TYPE_TRANSFORM_2D=22
2-dimensional transform global shader parameter (globaluniformmat2x3...). Exposed as aTransform2Din the editor UI.
GlobalShaderParameterTypeGLOBAL_VAR_TYPE_TRANSFORM=23
3-dimensional transform global shader parameter (globaluniformmat3x4...). Exposed as aTransform3Din the editor UI.
GlobalShaderParameterTypeGLOBAL_VAR_TYPE_SAMPLER2D=24
2D sampler global shader parameter (globaluniformsampler2D...). Exposed as aTexture2Din the editor UI.
GlobalShaderParameterTypeGLOBAL_VAR_TYPE_SAMPLER2DARRAY=25
2D sampler array global shader parameter (globaluniformsampler2DArray...). Exposed as aTexture2DArrayin the editor UI.
GlobalShaderParameterTypeGLOBAL_VAR_TYPE_SAMPLER3D=26
3D sampler global shader parameter (globaluniformsampler3D...). Exposed as aTexture3Din the editor UI.
GlobalShaderParameterTypeGLOBAL_VAR_TYPE_SAMPLERCUBE=27
Cubemap sampler global shader parameter (globaluniformsamplerCube...). Exposed as aCubemapin the editor UI.
GlobalShaderParameterTypeGLOBAL_VAR_TYPE_SAMPLEREXT=28
External sampler global shader parameter (globaluniformsamplerExternalOES...). Exposed as anExternalTexturein the editor UI.
GlobalShaderParameterTypeGLOBAL_VAR_TYPE_MAX=29
Represents the size of theGlobalShaderParameterTypeenum.
enumRenderingInfo:🔗
RenderingInfoRENDERING_INFO_TOTAL_OBJECTS_IN_FRAME=0
Number of objects rendered in the current 3D scene. This varies depending on camera position and rotation.
RenderingInfoRENDERING_INFO_TOTAL_PRIMITIVES_IN_FRAME=1
Number of points, lines, or triangles rendered in the current 3D scene. This varies depending on camera position and rotation.
RenderingInfoRENDERING_INFO_TOTAL_DRAW_CALLS_IN_FRAME=2
Number of draw calls performed to render in the current 3D scene. This varies depending on camera position and rotation.
RenderingInfoRENDERING_INFO_TEXTURE_MEM_USED=3
Texture memory used (in bytes).
RenderingInfoRENDERING_INFO_BUFFER_MEM_USED=4
Buffer memory used (in bytes). This includes vertex data, uniform buffers, and many miscellaneous buffer types used internally.
RenderingInfoRENDERING_INFO_VIDEO_MEM_USED=5
Video memory used (in bytes). When using the Forward+ or Mobile renderers, this is always greater than the sum ofRENDERING_INFO_TEXTURE_MEM_USEDandRENDERING_INFO_BUFFER_MEM_USED, since there is miscellaneous data not accounted for by those two metrics. When using the Compatibility renderer, this is equal to the sum ofRENDERING_INFO_TEXTURE_MEM_USEDandRENDERING_INFO_BUFFER_MEM_USED.
RenderingInfoRENDERING_INFO_PIPELINE_COMPILATIONS_CANVAS=6
Number of pipeline compilations that were triggered by the 2D canvas renderer.
RenderingInfoRENDERING_INFO_PIPELINE_COMPILATIONS_MESH=7
Number of pipeline compilations that were triggered by loading meshes. These compilations will show up as longer loading times the first time a user runs the game and the pipeline is required.
RenderingInfoRENDERING_INFO_PIPELINE_COMPILATIONS_SURFACE=8
Number of pipeline compilations that were triggered by building the surface cache before rendering the scene. These compilations will show up as a stutter when loading a scene the first time a user runs the game and the pipeline is required.
RenderingInfoRENDERING_INFO_PIPELINE_COMPILATIONS_DRAW=9
Number of pipeline compilations that were triggered while drawing the scene. These compilations will show up as stutters during gameplay the first time a user runs the game and the pipeline is required.
RenderingInfoRENDERING_INFO_PIPELINE_COMPILATIONS_SPECIALIZATION=10
Number of pipeline compilations that were triggered to optimize the current scene. These compilations are done in the background and should not cause any stutters whatsoever.
enumPipelineSource:🔗
PipelineSourcePIPELINE_SOURCE_CANVAS=0
Pipeline compilation that was triggered by the 2D canvas renderer.
PipelineSourcePIPELINE_SOURCE_MESH=1
Pipeline compilation that was triggered by loading a mesh.
PipelineSourcePIPELINE_SOURCE_SURFACE=2
Pipeline compilation that was triggered by building the surface cache before rendering the scene.
PipelineSourcePIPELINE_SOURCE_DRAW=3
Pipeline compilation that was triggered while drawing the scene.
PipelineSourcePIPELINE_SOURCE_SPECIALIZATION=4
Pipeline compilation that was triggered to optimize the current scene.
PipelineSourcePIPELINE_SOURCE_MAX=5
Represents the size of thePipelineSourceenum.
enumSplashStretchMode:🔗
SplashStretchModeSPLASH_STRETCH_MODE_DISABLED=0
No stretching is applied.
SplashStretchModeSPLASH_STRETCH_MODE_KEEP=1
Stretches image to fullscreen while preserving aspect ratio.
SplashStretchModeSPLASH_STRETCH_MODE_KEEP_WIDTH=2
Stretches the height of the image based on the width of the screen.
SplashStretchModeSPLASH_STRETCH_MODE_KEEP_HEIGHT=3
Stretches the width of the image based on the height of the screen.
SplashStretchModeSPLASH_STRETCH_MODE_COVER=4
Stretches the image to cover the entire screen while preserving aspect ratio.
SplashStretchModeSPLASH_STRETCH_MODE_IGNORE=5
Stretches the image to cover the entire screen but doesn't preserve aspect ratio.
enumFeatures:🔗
FeaturesFEATURE_SHADERS=0
Deprecated:This constant has not been used since Godot 3.0.
FeaturesFEATURE_MULTITHREADED=1
Deprecated:This constant has not been used since Godot 3.0.

## Constants

NO_INDEX_ARRAY=-1🔗
Marks an error that shows that the index array is empty.
ARRAY_WEIGHTS_SIZE=4🔗
Number of weights/bones per vertex.
CANVAS_ITEM_Z_MIN=-4096🔗
The minimum Z-layer for canvas items.
CANVAS_ITEM_Z_MAX=4096🔗
The maximum Z-layer for canvas items.
CANVAS_LAYER_MIN=-2147483648🔗
The minimum canvas layer.
CANVAS_LAYER_MAX=2147483647🔗
The maximum canvas layer.
MAX_GLOW_LEVELS=7🔗
The maximum number of glow levels that can be used with the glow post-processing effect.
MAX_CURSORS=8🔗
Deprecated:This constant is not used by the engine.
MAX_2D_DIRECTIONAL_LIGHTS=8🔗
The maximum number of directional lights that can be rendered at a given time in 2D.
MAX_MESH_SURFACES=256🔗
The maximum number of surfaces a mesh can have.
MATERIAL_RENDER_PRIORITY_MIN=-128🔗
The minimum renderpriority of all materials.
MATERIAL_RENDER_PRIORITY_MAX=127🔗
The maximum renderpriority of all materials.
ARRAY_CUSTOM_COUNT=4🔗
The number of custom data arrays available (ARRAY_CUSTOM0,ARRAY_CUSTOM1,ARRAY_CUSTOM2,ARRAY_CUSTOM3).
PARTICLES_EMIT_FLAG_POSITION=1🔗
There is currently no description for this constant. Please help us bycontributing one!
PARTICLES_EMIT_FLAG_ROTATION_SCALE=2🔗
There is currently no description for this constant. Please help us bycontributing one!
PARTICLES_EMIT_FLAG_VELOCITY=4🔗
There is currently no description for this constant. Please help us bycontributing one!
PARTICLES_EMIT_FLAG_COLOR=8🔗
There is currently no description for this constant. Please help us bycontributing one!
PARTICLES_EMIT_FLAG_CUSTOM=16🔗
There is currently no description for this constant. Please help us bycontributing one!

## Property Descriptions

boolrender_loop_enabled🔗

- voidset_render_loop_enabled(value:bool)
voidset_render_loop_enabled(value:bool)
- boolis_render_loop_enabled()
boolis_render_loop_enabled()
Iffalse, disables rendering completely, but the engine logic is still being processed. You can callforce_draw()to draw a frame even with rendering disabled.

## Method Descriptions

Array[Image]bake_render_uv2(base:RID, material_overrides:Array[RID], image_size:Vector2i)🔗
Bakes the material data of the Mesh passed in thebaseparameter with optionalmaterial_overridesto a set ofImages of sizeimage_size. Returns an array ofImages containing material properties as specified inBakeChannels.
voidcall_on_render_thread(callable:Callable)🔗
As the RenderingServer actual logic may run on a separate thread, accessing its internals from the main (or any other) thread will result in errors. To make it easier to run code that can safely access the rendering internals (such asRenderingDeviceand similar RD classes), push a callable via this function so it will be executed on the render thread.
RIDcamera_attributes_create()🔗
Creates a camera attributes object and adds it to the RenderingServer. It can be accessed with the RID that is returned. This RID will be used in allcamera_attributes_RenderingServer functions.
Once finished with your RID, you will want to free the RID using the RenderingServer'sfree_rid()method.
Note:The equivalent resource isCameraAttributes.
voidcamera_attributes_set_auto_exposure(camera_attributes:RID, enable:bool, min_sensitivity:float, max_sensitivity:float, speed:float, scale:float)🔗
Sets the parameters to use with the auto-exposure effect. These parameters take on the same meaning as their counterparts inCameraAttributesandCameraAttributesPractical.
voidcamera_attributes_set_dof_blur(camera_attributes:RID, far_enable:bool, far_distance:float, far_transition:float, near_enable:bool, near_distance:float, near_transition:float, amount:float)🔗
Sets the parameters to use with the DOF blur effect. These parameters take on the same meaning as their counterparts inCameraAttributesPractical.
voidcamera_attributes_set_dof_blur_bokeh_shape(shape:DOFBokehShape)🔗
Sets the shape of the DOF bokeh pattern toshape. Different shapes may be used to achieve artistic effect, or to meet performance targets.
voidcamera_attributes_set_dof_blur_quality(quality:DOFBlurQuality, use_jitter:bool)🔗
Sets the quality level of the DOF blur effect toquality.use_jittercan be used to jitter samples taken during the blur pass to hide artifacts at the cost of looking more fuzzy.
voidcamera_attributes_set_exposure(camera_attributes:RID, multiplier:float, normalization:float)🔗
Sets the exposure values that will be used by the renderers. The normalization amount is used to bake a given Exposure Value (EV) into rendering calculations to reduce the dynamic range of the scene.
The normalization factor can be calculated from exposure value (EV100) as follows:

```
func get_exposure_normalization(ev100: float):
    return 1.0 / (pow(2.0, ev100) * 1.2)
```

The exposure value can be calculated from aperture (in f-stops), shutter speed (in seconds), and sensitivity (in ISO) as follows:

```
func get_exposure(aperture: float, shutter_speed: float, sensitivity: float):
    return log((aperture * aperture) / shutter_speed * (100.0 / sensitivity)) / log(2)
```

RIDcamera_create()🔗
Creates a 3D camera and adds it to the RenderingServer. It can be accessed with the RID that is returned. This RID will be used in allcamera_*RenderingServer functions.
Once finished with your RID, you will want to free the RID using the RenderingServer'sfree_rid()method.
Note:The equivalent node isCamera3D.
voidcamera_set_camera_attributes(camera:RID, effects:RID)🔗
Sets the camera_attributes created withcamera_attributes_create()to the given camera.
voidcamera_set_compositor(camera:RID, compositor:RID)🔗
Sets the compositor used by this camera. Equivalent toCamera3D.compositor.
voidcamera_set_cull_mask(camera:RID, layers:int)🔗
Sets the cull mask associated with this camera. The cull mask describes which 3D layers are rendered by this camera. Equivalent toCamera3D.cull_mask.
voidcamera_set_environment(camera:RID, env:RID)🔗
Sets the environment used by this camera. Equivalent toCamera3D.environment.
voidcamera_set_frustum(camera:RID, size:float, offset:Vector2, z_near:float, z_far:float)🔗
Sets camera to use frustum projection. This mode allows adjusting theoffsetargument to create "tilted frustum" effects.
voidcamera_set_orthogonal(camera:RID, size:float, z_near:float, z_far:float)🔗
Sets camera to use orthogonal projection, also known as orthographic projection. Objects remain the same size on the screen no matter how far away they are.
voidcamera_set_perspective(camera:RID, fovy_degrees:float, z_near:float, z_far:float)🔗
Sets camera to use perspective projection. Objects on the screen becomes smaller when they are far away.
voidcamera_set_transform(camera:RID, transform:Transform3D)🔗
SetsTransform3Dof camera.
voidcamera_set_use_vertical_aspect(camera:RID, enable:bool)🔗
Iftrue, preserves the horizontal aspect ratio which is equivalent toCamera3D.KEEP_WIDTH. Iffalse, preserves the vertical aspect ratio which is equivalent toCamera3D.KEEP_HEIGHT.
RIDcanvas_create()🔗
Creates a canvas and returns the assignedRID. It can be accessed with the RID that is returned. This RID will be used in allcanvas_*RenderingServer functions.
Once finished with your RID, you will want to free the RID using the RenderingServer'sfree_rid()method.
Canvas has noResourceorNodeequivalent.
voidcanvas_item_add_animation_slice(item:RID, animation_length:float, slice_begin:float, slice_end:float, offset:float= 0.0)🔗
Subsequent drawing commands will be ignored unless they fall within the specified animation slice. This is a faster way to implement animations that loop on background rather than redrawing constantly.
voidcanvas_item_add_circle(item:RID, pos:Vector2, radius:float, color:Color, antialiased:bool= false)🔗
Draws a circle on theCanvasItempointed to by theitemRID. See alsoCanvasItem.draw_circle().
voidcanvas_item_add_clip_ignore(item:RID, ignore:bool)🔗
Ifignoreistrue, ignore clipping on items drawn with this canvas item until this is called again withignoreset tofalse.
voidcanvas_item_add_ellipse(item:RID, pos:Vector2, major:float, minor:float, color:Color, antialiased:bool= false)🔗
Draws an ellipse with semi-major axismajorand semi-minor axisminoron theCanvasItempointed to by theitemRID. See alsoCanvasItem.draw_ellipse().
voidcanvas_item_add_lcd_texture_rect_region(item:RID, rect:Rect2, texture:RID, src_rect:Rect2, modulate:Color)🔗
See alsoCanvasItem.draw_lcd_texture_rect_region().
voidcanvas_item_add_line(item:RID, from:Vector2, to:Vector2, color:Color, width:float= -1.0, antialiased:bool= false)🔗
Draws a line on theCanvasItempointed to by theitemRID. See alsoCanvasItem.draw_line().
voidcanvas_item_add_mesh(item:RID, mesh:RID, transform:Transform2D= Transform2D(1, 0, 0, 1, 0, 0), modulate:Color= Color(1, 1, 1, 1), texture:RID= RID())🔗
Draws a mesh created withmesh_create()with giventransform,modulatecolor, andtexture. This is used internally byMeshInstance2D.
voidcanvas_item_add_msdf_texture_rect_region(item:RID, rect:Rect2, texture:RID, src_rect:Rect2, modulate:Color= Color(1, 1, 1, 1), outline_size:int= 0, px_range:float= 1.0, scale:float= 1.0)🔗
See alsoCanvasItem.draw_msdf_texture_rect_region().
voidcanvas_item_add_multiline(item:RID, points:PackedVector2Array, colors:PackedColorArray, width:float= -1.0, antialiased:bool= false)🔗
Draws a 2D multiline on theCanvasItempointed to by theitemRID. See alsoCanvasItem.draw_multiline()andCanvasItem.draw_multiline_colors().
voidcanvas_item_add_multimesh(item:RID, mesh:RID, texture:RID= RID())🔗
Draws a 2DMultiMeshon theCanvasItempointed to by theitemRID. See alsoCanvasItem.draw_multimesh().
voidcanvas_item_add_nine_patch(item:RID, rect:Rect2, source:Rect2, texture:RID, topleft:Vector2, bottomright:Vector2, x_axis_mode:NinePatchAxisMode= 0, y_axis_mode:NinePatchAxisMode= 0, draw_center:bool= true, modulate:Color= Color(1, 1, 1, 1))🔗
Draws a nine-patch rectangle on theCanvasItempointed to by theitemRID.
voidcanvas_item_add_particles(item:RID, particles:RID, texture:RID)🔗
Draws particles on theCanvasItempointed to by theitemRID.
voidcanvas_item_add_polygon(item:RID, points:PackedVector2Array, colors:PackedColorArray, uvs:PackedVector2Array= PackedVector2Array(), texture:RID= RID())🔗
Draws a 2D polygon on theCanvasItempointed to by theitemRID. If you need more flexibility (such as being able to use bones), usecanvas_item_add_triangle_array()instead. See alsoCanvasItem.draw_polygon().
Note:If you frequently redraw the same polygon with a large number of vertices, consider pre-calculating the triangulation withGeometry2D.triangulate_polygon()and usingCanvasItem.draw_mesh(),CanvasItem.draw_multimesh(), orcanvas_item_add_triangle_array().
voidcanvas_item_add_polyline(item:RID, points:PackedVector2Array, colors:PackedColorArray, width:float= -1.0, antialiased:bool= false)🔗
Draws a 2D polyline on theCanvasItempointed to by theitemRID. See alsoCanvasItem.draw_polyline()andCanvasItem.draw_polyline_colors().
voidcanvas_item_add_primitive(item:RID, points:PackedVector2Array, colors:PackedColorArray, uvs:PackedVector2Array, texture:RID)🔗
Draws a 2D primitive on theCanvasItempointed to by theitemRID. See alsoCanvasItem.draw_primitive().
voidcanvas_item_add_rect(item:RID, rect:Rect2, color:Color, antialiased:bool= false)🔗
Draws a rectangle on theCanvasItempointed to by theitemRID. See alsoCanvasItem.draw_rect().
voidcanvas_item_add_set_transform(item:RID, transform:Transform2D)🔗
Sets aTransform2Dthat will be used to transform subsequent canvas item commands.
voidcanvas_item_add_texture_rect(item:RID, rect:Rect2, texture:RID, tile:bool= false, modulate:Color= Color(1, 1, 1, 1), transpose:bool= false)🔗
Draws a 2D textured rectangle on theCanvasItempointed to by theitemRID. See alsoCanvasItem.draw_texture_rect()andTexture2D.draw_rect().
voidcanvas_item_add_texture_rect_region(item:RID, rect:Rect2, texture:RID, src_rect:Rect2, modulate:Color= Color(1, 1, 1, 1), transpose:bool= false, clip_uv:bool= true)🔗
Draws the specified region of a 2D textured rectangle on theCanvasItempointed to by theitemRID. See alsoCanvasItem.draw_texture_rect_region()andTexture2D.draw_rect_region().
voidcanvas_item_add_triangle_array(item:RID, indices:PackedInt32Array, points:PackedVector2Array, colors:PackedColorArray, uvs:PackedVector2Array= PackedVector2Array(), bones:PackedInt32Array= PackedInt32Array(), weights:PackedFloat32Array= PackedFloat32Array(), texture:RID= RID(), count:int= -1)🔗
Draws a triangle array on theCanvasItempointed to by theitemRID. This is internally used byLine2DandStyleBoxFlatfor rendering.canvas_item_add_triangle_array()is highly flexible, but more complex to use thancanvas_item_add_polygon().
Note:Ifcountis set to a non-negative value, only the firstcount*3indices (corresponding tocounttriangles) will be drawn. Otherwise, all indices are drawn.
voidcanvas_item_attach_skeleton(item:RID, skeleton:RID)🔗
Attaches a skeleton to theCanvasItem. Removes the previous skeleton.
voidcanvas_item_clear(item:RID)🔗
Clears theCanvasItemand removes all commands in it.
RIDcanvas_item_create()🔗
Creates a new CanvasItem instance and returns itsRID. It can be accessed with the RID that is returned. This RID will be used in allcanvas_item_*RenderingServer functions.
Once finished with your RID, you will want to free the RID using the RenderingServer'sfree_rid()method.
Note:The equivalent node isCanvasItem.
Variantcanvas_item_get_instance_shader_parameter(instance:RID, parameter:StringName)const🔗
Returns the value of the per-instance shader uniform from the specified canvas item instance. Equivalent toCanvasItem.get_instance_shader_parameter().
Variantcanvas_item_get_instance_shader_parameter_default_value(instance:RID, parameter:StringName)const🔗
Returns the default value of the per-instance shader uniform from the specified canvas item instance. Equivalent toCanvasItem.get_instance_shader_parameter().
Array[Dictionary]canvas_item_get_instance_shader_parameter_list(instance:RID)const🔗
Returns a dictionary of per-instance shader uniform names of the per-instance shader uniform from the specified canvas item instance.
The returned dictionary is in PropertyInfo format, with the keysname,class_name,type,hint,hint_string, andusage.
voidcanvas_item_reset_physics_interpolation(item:RID)🔗
Prevents physics interpolation for the current physics tick.
This is useful when moving a canvas item to a new location, to give an instantaneous change rather than interpolation from the previous location.
voidcanvas_item_set_canvas_group_mode(item:RID, mode:CanvasGroupMode, clear_margin:float= 5.0, fit_empty:bool= false, fit_margin:float= 0.0, blur_mipmaps:bool= false)🔗
Sets the canvas group mode used during 2D rendering for the canvas item specified by theitemRID. For faster but more limited clipping, usecanvas_item_set_clip()instead.
Note:The equivalent node functionality is found inCanvasGroupandCanvasItem.clip_children.
voidcanvas_item_set_clip(item:RID, clip:bool)🔗
Ifclipistrue, makes the canvas item specified by theitemRID not draw anything outside of its rect's coordinates. This clipping is fast, but works only with axis-aligned rectangles. This means that rotation is ignored by the clipping rectangle. For more advanced clipping shapes, usecanvas_item_set_canvas_group_mode()instead.
Note:The equivalent node functionality is found inLabel.clip_text,RichTextLabel(always enabled) and more.
voidcanvas_item_set_copy_to_backbuffer(item:RID, enabled:bool, rect:Rect2)🔗
Sets theCanvasItemto copy a rect to the backbuffer.
voidcanvas_item_set_custom_rect(item:RID, use_custom_rect:bool, rect:Rect2= Rect2(0, 0, 0, 0))🔗
Ifuse_custom_rectistrue, sets the custom visibility rectangle (used for culling) torectfor the canvas item specified byitem. Setting a custom visibility rect can reduce CPU load when drawing lots of 2D instances. Ifuse_custom_rectisfalse, automatically computes a visibility rectangle based on the canvas item's draw commands.
voidcanvas_item_set_default_texture_filter(item:RID, filter:CanvasItemTextureFilter)🔗
Sets the default texture filter mode for the canvas item specified by theitemRID. Equivalent toCanvasItem.texture_filter.
voidcanvas_item_set_default_texture_repeat(item:RID, repeat:CanvasItemTextureRepeat)🔗
Sets the default texture repeat mode for the canvas item specified by theitemRID. Equivalent toCanvasItem.texture_repeat.
voidcanvas_item_set_distance_field_mode(item:RID, enabled:bool)🔗
Ifenabledistrue, enables multichannel signed distance field rendering mode for the canvas item specified by theitemRID. This is meant to be used for font rendering, or with specially generated images usingmsdfgen.
voidcanvas_item_set_draw_behind_parent(item:RID, enabled:bool)🔗
Ifenabledistrue, draws the canvas item specified by theitemRID behind its parent. Equivalent toCanvasItem.show_behind_parent.
voidcanvas_item_set_draw_index(item:RID, index:int)🔗
Sets the index for theCanvasItem.
voidcanvas_item_set_instance_shader_parameter(instance:RID, parameter:StringName, value:Variant)🔗
Sets the per-instance shader uniform on the specified canvas item instance. Equivalent toCanvasItem.set_instance_shader_parameter().
voidcanvas_item_set_interpolated(item:RID, interpolated:bool)🔗
Ifinterpolatedistrue, turns on physics interpolation for the canvas item.
voidcanvas_item_set_light_mask(item:RID, mask:int)🔗
Sets the lightmaskfor the canvas item specified by theitemRID. Equivalent toCanvasItem.light_mask.
voidcanvas_item_set_material(item:RID, material:RID)🔗
Sets a newmaterialto the canvas item specified by theitemRID. Equivalent toCanvasItem.material.
voidcanvas_item_set_modulate(item:RID, color:Color)🔗
Multiplies the color of the canvas item specified by theitemRID, while affecting its children. See alsocanvas_item_set_self_modulate(). Equivalent toCanvasItem.modulate.
voidcanvas_item_set_parent(item:RID, parent:RID)🔗
Sets a parentCanvasItemto theCanvasItem. The item will inherit transform, modulation and visibility from its parent, likeCanvasItemnodes in the scene tree.
voidcanvas_item_set_self_modulate(item:RID, color:Color)🔗
Multiplies the color of the canvas item specified by theitemRID, without affecting its children. See alsocanvas_item_set_modulate(). Equivalent toCanvasItem.self_modulate.
voidcanvas_item_set_sort_children_by_y(item:RID, enabled:bool)🔗
Ifenabledistrue, child nodes with the lowest Y position are drawn before those with a higher Y position. Y-sorting only affects children that inherit from the canvas item specified by theitemRID, not the canvas item itself. Equivalent toCanvasItem.y_sort_enabled.
voidcanvas_item_set_transform(item:RID, transform:Transform2D)🔗
Sets thetransformof the canvas item specified by theitemRID. This affects where and how the item will be drawn. Child canvas items' transforms are multiplied by their parent's transform. Equivalent toNode2D.transform.
voidcanvas_item_set_use_parent_material(item:RID, enabled:bool)🔗
Sets if theCanvasItemuses its parent's material.
voidcanvas_item_set_visibility_layer(item:RID, visibility_layer:int)🔗
Sets the rendering visibility layer associated with thisCanvasItem. OnlyViewportnodes with a matching rendering mask will render thisCanvasItem.
voidcanvas_item_set_visibility_notifier(item:RID, enable:bool, area:Rect2, enter_callable:Callable, exit_callable:Callable)🔗
Sets the givenCanvasItemas visibility notifier.areadefines the area of detecting visibility.enter_callableis called when theCanvasItementers the screen,exit_callableis called when theCanvasItemexits the screen. Ifenableisfalse, the item will no longer function as notifier.
This method can be used to manually mimicVisibleOnScreenNotifier2D.
voidcanvas_item_set_visible(item:RID, visible:bool)🔗
Sets the visibility of theCanvasItem.
voidcanvas_item_set_z_as_relative_to_parent(item:RID, enabled:bool)🔗
If this is enabled, the Z index of the parent will be added to the children's Z index.
voidcanvas_item_set_z_index(item:RID, z_index:int)🔗
Sets theCanvasItem's Z index, i.e. its draw order (lower indexes are drawn first).
voidcanvas_item_transform_physics_interpolation(item:RID, transform:Transform2D)🔗
Transforms both the current and previous stored transform for a canvas item.
This allows transforming a canvas item without creating a "glitch" in the interpolation, which is particularly useful for large worlds utilizing a shifting origin.
voidcanvas_light_attach_to_canvas(light:RID, canvas:RID)🔗
Attaches the canvas light to the canvas. Removes it from its previous canvas.
RIDcanvas_light_create()🔗
Creates a canvas light and adds it to the RenderingServer. It can be accessed with the RID that is returned. This RID will be used in allcanvas_light_*RenderingServer functions.
Once finished with your RID, you will want to free the RID using the RenderingServer'sfree_rid()method.
Note:The equivalent node isLight2D.
voidcanvas_light_occluder_attach_to_canvas(occluder:RID, canvas:RID)🔗
Attaches a light occluder to the canvas. Removes it from its previous canvas.
RIDcanvas_light_occluder_create()🔗
Creates a light occluder and adds it to the RenderingServer. It can be accessed with the RID that is returned. This RID will be used in allcanvas_light_occluder_*RenderingServer functions.
Once finished with your RID, you will want to free the RID using the RenderingServer'sfree_rid()method.
Note:The equivalent node isLightOccluder2D.
voidcanvas_light_occluder_reset_physics_interpolation(occluder:RID)🔗
Prevents physics interpolation for the current physics tick.
This is useful when moving an occluder to a new location, to give an instantaneous change rather than interpolation from the previous location.
voidcanvas_light_occluder_set_as_sdf_collision(occluder:RID, enable:bool)🔗
There is currently no description for this method. Please help us bycontributing one!
voidcanvas_light_occluder_set_enabled(occluder:RID, enabled:bool)🔗
Enables or disables light occluder.
voidcanvas_light_occluder_set_interpolated(occluder:RID, interpolated:bool)🔗
Ifinterpolatedistrue, turns on physics interpolation for the light occluder.
voidcanvas_light_occluder_set_light_mask(occluder:RID, mask:int)🔗
The light mask. SeeLightOccluder2Dfor more information on light masks.
voidcanvas_light_occluder_set_polygon(occluder:RID, polygon:RID)🔗
Sets a light occluder's polygon.
voidcanvas_light_occluder_set_transform(occluder:RID, transform:Transform2D)🔗
Sets a light occluder'sTransform2D.
voidcanvas_light_occluder_transform_physics_interpolation(occluder:RID, transform:Transform2D)🔗
Transforms both the current and previous stored transform for a light occluder.
This allows transforming an occluder without creating a "glitch" in the interpolation, which is particularly useful for large worlds utilizing a shifting origin.
voidcanvas_light_reset_physics_interpolation(light:RID)🔗
Prevents physics interpolation for the current physics tick.
This is useful when moving a canvas item to a new location, to give an instantaneous change rather than interpolation from the previous location.
voidcanvas_light_set_blend_mode(light:RID, mode:CanvasLightBlendMode)🔗
Sets the blend mode for the given canvas light tomode. Equivalent toLight2D.blend_mode.
voidcanvas_light_set_color(light:RID, color:Color)🔗
Sets the color for a light.
voidcanvas_light_set_enabled(light:RID, enabled:bool)🔗
Enables or disables a canvas light.
voidcanvas_light_set_energy(light:RID, energy:float)🔗
Sets a canvas light's energy.
voidcanvas_light_set_height(light:RID, height:float)🔗
Sets a canvas light's height.
voidcanvas_light_set_interpolated(light:RID, interpolated:bool)🔗
Ifinterpolatedistrue, turns on physics interpolation for the canvas light.
voidcanvas_light_set_item_cull_mask(light:RID, mask:int)🔗
The light mask. SeeLightOccluder2Dfor more information on light masks.
voidcanvas_light_set_item_shadow_cull_mask(light:RID, mask:int)🔗
The binary mask used to determine which layers this canvas light's shadows affects. SeeLightOccluder2Dfor more information on light masks.
voidcanvas_light_set_layer_range(light:RID, min_layer:int, max_layer:int)🔗
The layer range that gets rendered with this light.
voidcanvas_light_set_mode(light:RID, mode:CanvasLightMode)🔗
Sets the mode of the canvas light.
voidcanvas_light_set_shadow_color(light:RID, color:Color)🔗
Sets the color of the canvas light's shadow.
voidcanvas_light_set_shadow_enabled(light:RID, enabled:bool)🔗
Enables or disables the canvas light's shadow.
voidcanvas_light_set_shadow_filter(light:RID, filter:CanvasLightShadowFilter)🔗
Sets the canvas light's shadow's filter.
voidcanvas_light_set_shadow_smooth(light:RID, smooth:float)🔗
Smoothens the shadow. The lower, the smoother.
voidcanvas_light_set_texture(light:RID, texture:RID)🔗
Sets the texture to be used by aPointLight2D. Equivalent toPointLight2D.texture.
voidcanvas_light_set_texture_offset(light:RID, offset:Vector2)🔗
Sets the offset of aPointLight2D's texture. Equivalent toPointLight2D.offset.
voidcanvas_light_set_texture_scale(light:RID, scale:float)🔗
Sets the scale factor of aPointLight2D's texture. Equivalent toPointLight2D.texture_scale.
voidcanvas_light_set_transform(light:RID, transform:Transform2D)🔗
Sets the canvas light'sTransform2D.
voidcanvas_light_set_z_range(light:RID, min_z:int, max_z:int)🔗
Sets the Z range of objects that will be affected by this light. Equivalent toLight2D.range_z_minandLight2D.range_z_max.
voidcanvas_light_transform_physics_interpolation(light:RID, transform:Transform2D)🔗
Transforms both the current and previous stored transform for a canvas light.
This allows transforming a light without creating a "glitch" in the interpolation, which is particularly useful for large worlds utilizing a shifting origin.
RIDcanvas_occluder_polygon_create()🔗
Creates a new light occluder polygon and adds it to the RenderingServer. It can be accessed with the RID that is returned. This RID will be used in allcanvas_occluder_polygon_*RenderingServer functions.
Once finished with your RID, you will want to free the RID using the RenderingServer'sfree_rid()method.
Note:The equivalent resource isOccluderPolygon2D.
voidcanvas_occluder_polygon_set_cull_mode(occluder_polygon:RID, mode:CanvasOccluderPolygonCullMode)🔗
Sets an occluder polygon's cull mode.
voidcanvas_occluder_polygon_set_shape(occluder_polygon:RID, shape:PackedVector2Array, closed:bool)🔗
Sets the shape of the occluder polygon.
voidcanvas_set_disable_scale(disable:bool)🔗
There is currently no description for this method. Please help us bycontributing one!
voidcanvas_set_item_mirroring(canvas:RID, item:RID, mirroring:Vector2)🔗
A copy of the canvas item will be drawn with a local offset of themirroring.
Note:This is equivalent to callingcanvas_set_item_repeat()likecanvas_set_item_repeat(item,mirroring,1), with an additional check ensuringcanvasis a parent ofitem.
voidcanvas_set_item_repeat(item:RID, repeat_size:Vector2, repeat_times:int)🔗
A copy of the canvas item will be drawn with a local offset of therepeat_sizeby the number of times of therepeat_times. As therepeat_timesincreases, the copies will spread away from the origin texture.
voidcanvas_set_modulate(canvas:RID, color:Color)🔗
Modulates all colors in the given canvas.
voidcanvas_set_shadow_texture_size(size:int)🔗
Sets theProjectSettings.rendering/2d/shadow_atlas/sizeto use forLight2Dshadow rendering (in pixels). The value is rounded up to the nearest power of 2.
RIDcanvas_texture_create()🔗
Creates a canvas texture and adds it to the RenderingServer. It can be accessed with the RID that is returned. This RID will be used in allcanvas_texture_*RenderingServer functions.
Once finished with your RID, you will want to free the RID using the RenderingServer'sfree_rid()method. See alsotexture_2d_create().
Note:The equivalent resource isCanvasTextureand is only meant to be used in 2D rendering, not 3D.
voidcanvas_texture_set_channel(canvas_texture:RID, channel:CanvasTextureChannel, texture:RID)🔗
Sets thechannel'stexturefor the canvas texture specified by thecanvas_textureRID. Equivalent toCanvasTexture.diffuse_texture,CanvasTexture.normal_textureandCanvasTexture.specular_texture.
voidcanvas_texture_set_shading_parameters(canvas_texture:RID, base_color:Color, shininess:float)🔗
Sets thebase_colorandshininessto use for the canvas texture specified by thecanvas_textureRID. Equivalent toCanvasTexture.specular_colorandCanvasTexture.specular_shininess.
voidcanvas_texture_set_texture_filter(canvas_texture:RID, filter:CanvasItemTextureFilter)🔗
Sets the texturefiltermode to use for the canvas texture specified by thecanvas_textureRID.
voidcanvas_texture_set_texture_repeat(canvas_texture:RID, repeat:CanvasItemTextureRepeat)🔗
Sets the texturerepeatmode to use for the canvas texture specified by thecanvas_textureRID.
RIDcompositor_create()🔗
Creates a new compositor and adds it to the RenderingServer. It can be accessed with the RID that is returned.
Once finished with your RID, you will want to free the RID using the RenderingServer'sfree_rid()method.
RIDcompositor_effect_create()🔗
Creates a new rendering effect and adds it to the RenderingServer. It can be accessed with the RID that is returned.
Once finished with your RID, you will want to free the RID using the RenderingServer'sfree_rid()method.
voidcompositor_effect_set_callback(effect:RID, callback_type:CompositorEffectCallbackType, callback:Callable)🔗
Sets the callback type (callback_type) and callback method(callback) for this rendering effect.
voidcompositor_effect_set_enabled(effect:RID, enabled:bool)🔗
Enables/disables this rendering effect.
voidcompositor_effect_set_flag(effect:RID, flag:CompositorEffectFlags, set:bool)🔗
Sets the flag (flag) for this rendering effect totrueorfalse(set).
voidcompositor_set_compositor_effects(compositor:RID, effects:Array[RID])🔗
Sets the compositor effects for the specified compositor RID.effectsshould be an array containing RIDs created withcompositor_effect_create().
RenderingDevicecreate_local_rendering_device()const🔗
Creates a RenderingDevice that can be used to do draw and compute operations on a separate thread. Cannot draw to the screen nor share data with the global RenderingDevice.
Note:When using the OpenGL rendering driver or when running in headless mode, this function always returnsnull.
Rect2debug_canvas_item_get_rect(item:RID)🔗
Returns the bounding rectangle for a canvas item in local space, as calculated by the renderer. This bound is used internally for culling.
Warning:This function is intended for debugging in the editor, and will pass through and return a zeroRect2in exported projects.
RIDdecal_create()🔗
Creates a decal and adds it to the RenderingServer. It can be accessed with the RID that is returned. This RID will be used in alldecal_*RenderingServer functions.
Once finished with your RID, you will want to free the RID using the RenderingServer'sfree_rid()method.
To place in a scene, attach this decal to an instance usinginstance_set_base()using the returned RID.
Note:The equivalent node isDecal.
voiddecal_set_albedo_mix(decal:RID, albedo_mix:float)🔗
Sets thealbedo_mixin the decal specified by thedecalRID. Equivalent toDecal.albedo_mix.
voiddecal_set_cull_mask(decal:RID, mask:int)🔗
Sets the cullmaskin the decal specified by thedecalRID. Equivalent toDecal.cull_mask.
voiddecal_set_distance_fade(decal:RID, enabled:bool, begin:float, length:float)🔗
Sets the distance fade parameters in the decal specified by thedecalRID. Equivalent toDecal.distance_fade_enabled,Decal.distance_fade_beginandDecal.distance_fade_length.
voiddecal_set_emission_energy(decal:RID, energy:float)🔗
Sets the emissionenergyin the decal specified by thedecalRID. Equivalent toDecal.emission_energy.
voiddecal_set_fade(decal:RID, above:float, below:float)🔗
Sets the upper fade (above) and lower fade (below) in the decal specified by thedecalRID. Equivalent toDecal.upper_fadeandDecal.lower_fade.
voiddecal_set_modulate(decal:RID, color:Color)🔗
Sets the color multiplier in the decal specified by thedecalRID tocolor. Equivalent toDecal.modulate.
voiddecal_set_normal_fade(decal:RID, fade:float)🔗
Sets the normalfadein the decal specified by thedecalRID. Equivalent toDecal.normal_fade.
voiddecal_set_size(decal:RID, size:Vector3)🔗
Sets thesizeof the decal specified by thedecalRID. Equivalent toDecal.size.
voiddecal_set_texture(decal:RID, type:DecalTexture, texture:RID)🔗
Sets thetexturein the given texturetypeslot for the specified decal. Equivalent toDecal.set_texture().
voiddecals_set_filter(filter:DecalFilter)🔗
Sets the texturefiltermode to use when rendering decals. This parameter is global and cannot be set on a per-decal basis.
RIDdirectional_light_create()🔗
Creates a directional light and adds it to the RenderingServer. It can be accessed with the RID that is returned. This RID can be used in mostlight_*RenderingServer functions.
Once finished with your RID, you will want to free the RID using the RenderingServer'sfree_rid()method.
To place in a scene, attach this directional light to an instance usinginstance_set_base()using the returned RID.
Note:The equivalent node isDirectionalLight3D.
voiddirectional_shadow_atlas_set_size(size:int, is_16bits:bool)🔗
Sets thesizeof the directional light shadows in 3D. See alsoProjectSettings.rendering/lights_and_shadows/directional_shadow/size. This parameter is global and cannot be set on a per-viewport basis.
voiddirectional_soft_shadow_filter_set_quality(quality:ShadowQuality)🔗
Sets the filterqualityfor directional light shadows in 3D. See alsoProjectSettings.rendering/lights_and_shadows/directional_shadow/soft_shadow_filter_quality. This parameter is global and cannot be set on a per-viewport basis.
Imageenvironment_bake_panorama(environment:RID, bake_irradiance:bool, size:Vector2i)🔗
Generates and returns anImagecontaining the radiance map for the specifiedenvironmentRID's sky. This supports built-in sky material and custom sky shaders. Ifbake_irradianceistrue, the irradiance map is saved instead of the radiance map. The radiance map is used to render reflected light, while the irradiance map is used to render ambient light. See alsosky_bake_panorama().
Note:The image is saved using linear encoding without any tonemapping performed, which means it will look too dark if viewed directly in an image editor.
Note:sizeshould be a 2:1 aspect ratio for the generated panorama to have square pixels. For radiance maps, there is no point in using a height greater thanSky.radiance_size, as it won't increase detail. Irradiance maps only contain low-frequency data, so there is usually no point in going past a size of 128×64 pixels when saving an irradiance map.
RIDenvironment_create()🔗
Creates an environment and adds it to the RenderingServer. It can be accessed with the RID that is returned. This RID will be used in allenvironment_*RenderingServer functions.
Once finished with your RID, you will want to free the RID using the RenderingServer'sfree_rid()method.
Note:The equivalent resource isEnvironment.
voidenvironment_glow_set_use_bicubic_upscale(enable:bool)🔗
Ifenableistrue, enables bicubic upscaling for glow which improves quality at the cost of performance. Equivalent toProjectSettings.rendering/environment/glow/upscale_mode.
Note:This setting is only effective when using the Forward+ or Mobile rendering methods, as Compatibility uses a different glow implementation.
voidenvironment_set_adjustment(env:RID, enable:bool, brightness:float, contrast:float, saturation:float, use_1d_color_correction:bool, color_correction:RID)🔗
Sets the values to be used with the "adjustments" post-process effect. SeeEnvironmentfor more details.
voidenvironment_set_ambient_light(env:RID, color:Color, ambient:EnvironmentAmbientSource= 0, energy:float= 1.0, sky_contribution:float= 0.0, reflection_source:EnvironmentReflectionSource= 0)🔗
Sets the values to be used for ambient light rendering. SeeEnvironmentfor more details.
voidenvironment_set_background(env:RID, bg:EnvironmentBG)🔗
Sets the environment's background mode. Equivalent toEnvironment.background_mode.
voidenvironment_set_bg_color(env:RID, color:Color)🔗
Color displayed for clear areas of the scene. Only effective if using theENV_BG_COLORbackground mode.
voidenvironment_set_bg_energy(env:RID, multiplier:float, exposure_value:float)🔗
Sets the intensity of the background color.
voidenvironment_set_camera_id(env:RID, id:int)🔗
Sets the camera ID to be used as environment background.
voidenvironment_set_canvas_max_layer(env:RID, max_layer:int)🔗
Sets the maximum layer to use if using Canvas background mode.
voidenvironment_set_fog(env:RID, enable:bool, light_color:Color, light_energy:float, sun_scatter:float, density:float, height:float, height_density:float, aerial_perspective:float, sky_affect:float, fog_mode:EnvironmentFogMode= 0)🔗
Configures fog for the specified environment RID. Seefog_*properties inEnvironmentfor more information.
voidenvironment_set_fog_depth(env:RID, curve:float, begin:float, end:float)🔗
Configures fog depth for the specified environment RID. Only has an effect when the fog mode of the environment isENV_FOG_MODE_DEPTH. Seefog_depth_*properties inEnvironmentfor more information.
voidenvironment_set_glow(env:RID, enable:bool, levels:PackedFloat32Array, intensity:float, strength:float, mix:float, bloom_threshold:float, blend_mode:EnvironmentGlowBlendMode, hdr_bleed_threshold:float, hdr_bleed_scale:float, hdr_luminance_cap:float, glow_map_strength:float, glow_map:RID)🔗
Configures glow for the specified environment RID. Seeglow_*properties inEnvironmentfor more information.
voidenvironment_set_sdfgi(env:RID, enable:bool, cascades:int, min_cell_size:float, y_scale:EnvironmentSDFGIYScale, use_occlusion:bool, bounce_feedback:float, read_sky:bool, energy:float, normal_bias:float, probe_bias:float)🔗
Configures signed distance field global illumination for the specified environment RID. Seesdfgi_*properties inEnvironmentfor more information.
voidenvironment_set_sdfgi_frames_to_converge(frames:EnvironmentSDFGIFramesToConverge)🔗
Sets the number of frames to use for converging signed distance field global illumination. Equivalent toProjectSettings.rendering/global_illumination/sdfgi/frames_to_converge.
voidenvironment_set_sdfgi_frames_to_update_light(frames:EnvironmentSDFGIFramesToUpdateLight)🔗
Sets the update speed for dynamic lights' indirect lighting when computing signed distance field global illumination. Equivalent toProjectSettings.rendering/global_illumination/sdfgi/frames_to_update_lights.
voidenvironment_set_sdfgi_ray_count(ray_count:EnvironmentSDFGIRayCount)🔗
Sets the number of rays to throw per frame when computing signed distance field global illumination. Equivalent toProjectSettings.rendering/global_illumination/sdfgi/probe_ray_count.
voidenvironment_set_sky(env:RID, sky:RID)🔗
Sets theSkyto be used as the environment's background when usingBGModesky. Equivalent toEnvironment.sky.
voidenvironment_set_sky_custom_fov(env:RID, scale:float)🔗
Sets a custom field of view for the backgroundSky. Equivalent toEnvironment.sky_custom_fov.
voidenvironment_set_sky_orientation(env:RID, orientation:Basis)🔗
Sets the rotation of the backgroundSkyexpressed as aBasis. Equivalent toEnvironment.sky_rotation, where the rotation vector is used to construct theBasis.
voidenvironment_set_ssao(env:RID, enable:bool, radius:float, intensity:float, power:float, detail:float, horizon:float, sharpness:float, light_affect:float, ao_channel_affect:float)🔗
Sets the variables to be used with the screen-space ambient occlusion (SSAO) post-process effect. SeeEnvironmentfor more details.
voidenvironment_set_ssao_quality(quality:EnvironmentSSAOQuality, half_size:bool, adaptive_target:float, blur_passes:int, fadeout_from:float, fadeout_to:float)🔗
Sets the quality level of the screen-space ambient occlusion (SSAO) post-process effect. SeeEnvironmentfor more details.
voidenvironment_set_ssil_quality(quality:EnvironmentSSILQuality, half_size:bool, adaptive_target:float, blur_passes:int, fadeout_from:float, fadeout_to:float)🔗
Sets the quality level of the screen-space indirect lighting (SSIL) post-process effect. SeeEnvironmentfor more details.
voidenvironment_set_ssr(env:RID, enable:bool, max_steps:int, fade_in:float, fade_out:float, depth_tolerance:float)🔗
Sets the variables to be used with the screen-space reflections (SSR) post-process effect. SeeEnvironmentfor more details.
voidenvironment_set_ssr_half_size(half_size:bool)🔗
Sets whether screen-space reflections will be rendered at full or half size. Half size is faster, but may look pixelated or cause flickering.
voidenvironment_set_ssr_roughness_quality(quality:EnvironmentSSRRoughnessQuality)🔗
Deprecated:This option no longer does anything.
voidenvironment_set_tonemap(env:RID, tone_mapper:EnvironmentToneMapper, exposure:float, white:float)🔗
Sets the variables to be used with the "tonemap" post-process effect. SeeEnvironmentfor more details.
voidenvironment_set_tonemap_agx_contrast(env:RID, agx_contrast:float)🔗
SeeEnvironment.tonemap_agx_contrastfor more details.
voidenvironment_set_volumetric_fog(env:RID, enable:bool, density:float, albedo:Color, emission:Color, emission_energy:float, anisotropy:float, length:float, p_detail_spread:float, gi_inject:float, temporal_reprojection:bool, temporal_reprojection_amount:float, ambient_inject:float, sky_affect:float)🔗
Sets the variables to be used with the volumetric fog post-process effect. SeeEnvironmentfor more details.
voidenvironment_set_volumetric_fog_filter_active(active:bool)🔗
Enables filtering of the volumetric fog scattering buffer. This results in much smoother volumes with very few under-sampling artifacts.
voidenvironment_set_volumetric_fog_volume_size(size:int, depth:int)🔗
Sets the resolution of the volumetric fog's froxel buffer.sizeis modified by the screen's aspect ratio and then used to set the width and height of the buffer. Whiledepthis directly used to set the depth of the buffer.
RIDfog_volume_create()🔗
Creates a new fog volume and adds it to the RenderingServer. It can be accessed with the RID that is returned. This RID will be used in allfog_volume_*RenderingServer functions.
Once finished with your RID, you will want to free the RID using the RenderingServer'sfree_rid()method.
Note:The equivalent node isFogVolume.
voidfog_volume_set_material(fog_volume:RID, material:RID)🔗
Sets theMaterialof the fog volume. Can be either aFogMaterialor a customShaderMaterial.
voidfog_volume_set_shape(fog_volume:RID, shape:FogVolumeShape)🔗
Sets the shape of the fog volume to eitherFOG_VOLUME_SHAPE_ELLIPSOID,FOG_VOLUME_SHAPE_CONE,FOG_VOLUME_SHAPE_CYLINDER,FOG_VOLUME_SHAPE_BOXorFOG_VOLUME_SHAPE_WORLD.
voidfog_volume_set_size(fog_volume:RID, size:Vector3)🔗
Sets the size of the fog volume when shape isFOG_VOLUME_SHAPE_ELLIPSOID,FOG_VOLUME_SHAPE_CONE,FOG_VOLUME_SHAPE_CYLINDERorFOG_VOLUME_SHAPE_BOX.
voidforce_draw(swap_buffers:bool= true, frame_step:float= 0.0)🔗
Forces redrawing of all viewports at once. Must be called from the main thread.
voidforce_sync()🔗
Forces a synchronization between the CPU and GPU, which may be required in certain cases. Only call this when needed, as CPU-GPU synchronization has a performance cost.
voidfree_rid(rid:RID)🔗
Tries to free an object in the RenderingServer. To avoid memory leaks, this should be called after using an object as memory management does not occur automatically when using RenderingServer directly.
Stringget_current_rendering_driver_name()const🔗
Returns the name of the current rendering driver. This can bevulkan,d3d12,metal,opengl3,opengl3_es, oropengl3_angle. See alsoget_current_rendering_method().
WhenProjectSettings.rendering/renderer/rendering_methodisforward_plusormobile, the rendering driver is determined byProjectSettings.rendering/rendering_device/driver.
WhenProjectSettings.rendering/renderer/rendering_methodisgl_compatibility, the rendering driver is determined byProjectSettings.rendering/gl_compatibility/driver.
The rendering driver is also determined by the--rendering-drivercommand line argument that overrides this project setting, or an automatic fallback that is applied depending on the hardware.
Stringget_current_rendering_method()const🔗
Returns the name of the current rendering method. This can beforward_plus,mobile, orgl_compatibility. See alsoget_current_rendering_driver_name().
The rendering method is determined byProjectSettings.rendering/renderer/rendering_method, the--rendering-methodcommand line argument that overrides this project setting, or an automatic fallback that is applied depending on the hardware.
Colorget_default_clear_color()🔗
Returns the default clear color which is used when a specific clear color has not been selected. See alsoset_default_clear_color().
floatget_frame_setup_time_cpu()const🔗
Returns the time taken to setup rendering on the CPU in milliseconds. This value is shared across all viewports and doesnotrequireviewport_set_measure_render_time()to be enabled on a viewport to be queried. See alsoviewport_get_measured_render_time_cpu().
RenderingDeviceget_rendering_device()const🔗
Returns the global RenderingDevice.
Note:When using the OpenGL rendering driver or when running in headless mode, this function always returnsnull.
intget_rendering_info(info:RenderingInfo)🔗
Returns a statistic about the rendering engine which can be used for performance profiling. See alsoviewport_get_render_info(), which returns information specific to a viewport.
Note:Only 3D rendering is currently taken into account by some of these values, such as the number of draw calls.
Note:Rendering information is not available until at least 2 frames have been rendered by the engine. If rendering information is not available,get_rendering_info()returns0. To print rendering information in_ready()successfully, use the following:

```
func _ready():
    for _i in 2:
        await get_tree().process_frame

    print(RenderingServer.get_rendering_info(RENDERING_INFO_TOTAL_DRAW_CALLS_IN_FRAME))
```

Array[Dictionary]get_shader_parameter_list(shader:RID)const🔗
Returns the parameters of a shader.
RIDget_test_cube()🔗
Returns the RID of the test cube. This mesh will be created and returned on the first call toget_test_cube(), then it will be cached for subsequent calls. See alsomake_sphere_mesh().
RIDget_test_texture()🔗
Returns the RID of a 256×256 texture with a testing pattern on it (inImage.FORMAT_RGB8format). This texture will be created and returned on the first call toget_test_texture(), then it will be cached for subsequent calls. See alsoget_white_texture().
Example:Get the test texture and apply it to aSprite2Dnode:

```
var texture_rid = RenderingServer.get_test_texture()
var texture = ImageTexture.create_from_image(RenderingServer.texture_2d_get(texture_rid))
$Sprite2D.texture = texture
```

Stringget_video_adapter_api_version()const🔗
Returns the version of the graphics video adaptercurrently in use(e.g. "1.2.189" for Vulkan, "3.3.0 NVIDIA 510.60.02" for OpenGL). This version may be different from the actual latest version supported by the hardware, as Godot may not always request the latest version. See alsoOS.get_video_adapter_driver_info().
Note:When running a headless or server binary, this function returns an empty string.
Stringget_video_adapter_name()const🔗
Returns the name of the video adapter (e.g. "GeForce GTX 1080/PCIe/SSE2").
Note:When running a headless or server binary, this function returns an empty string.
Note:On the web platform, some browsers such as Firefox may report a different, fixed GPU name such as "GeForce GTX 980" (regardless of the user's actual GPU model). This is done to make fingerprinting more difficult.
DeviceTypeget_video_adapter_type()const🔗
Returns the type of the video adapter. Since dedicated graphics cards from a given generation willusuallybe significantly faster than integrated graphics made in the same generation, the device type can be used as a basis for automatic graphics settings adjustment. However, this is not always true, so make sure to provide users with a way to manually override graphics settings.
Note:When using the OpenGL rendering driver or when running in headless mode, this function always returnsRenderingDevice.DEVICE_TYPE_OTHER.
Stringget_video_adapter_vendor()const🔗
Returns the vendor of the video adapter (e.g. "NVIDIA Corporation").
Note:When running a headless or server binary, this function returns an empty string.
RIDget_white_texture()🔗
Returns the ID of a 4×4 white texture (inImage.FORMAT_RGB8format). This texture will be created and returned on the first call toget_white_texture(), then it will be cached for subsequent calls. See alsoget_test_texture().
Example:Get the white texture and apply it to aSprite2Dnode:

```
var texture_rid = RenderingServer.get_white_texture()
var texture = ImageTexture.create_from_image(RenderingServer.texture_2d_get(texture_rid))
$Sprite2D.texture = texture
```

voidgi_set_use_half_resolution(half_resolution:bool)🔗
Ifhalf_resolutionistrue, rendersVoxelGIand SDFGI (Environment.sdfgi_enabled) buffers at halved resolution on each axis (e.g. 960×540 when the viewport size is 1920×1080). This improves performance significantly when VoxelGI or SDFGI is enabled, at the cost of artifacts that may be visible on polygon edges. The loss in quality becomes less noticeable as the viewport resolution increases.LightmapGIrendering is not affected by this setting. Equivalent toProjectSettings.rendering/global_illumination/gi/use_half_resolution.
voidglobal_shader_parameter_add(name:StringName, type:GlobalShaderParameterType, default_value:Variant)🔗
Creates a new global shader uniform.
Note:Global shader parameter names are case-sensitive.
Variantglobal_shader_parameter_get(name:StringName)const🔗
Returns the value of the global shader uniform specified byname.
Note:global_shader_parameter_get()has a large performance penalty as the rendering thread needs to synchronize with the calling thread, which is slow. Do not use this method during gameplay to avoid stuttering. If you need to read values in a script after setting them, consider creating an autoload where you store the values you need to query at the same time you're setting them as global parameters.
Array[StringName]global_shader_parameter_get_list()const🔗
Returns the list of global shader uniform names.
Note:global_shader_parameter_get()has a large performance penalty as the rendering thread needs to synchronize with the calling thread, which is slow. Do not use this method during gameplay to avoid stuttering. If you need to read values in a script after setting them, consider creating an autoload where you store the values you need to query at the same time you're setting them as global parameters.
GlobalShaderParameterTypeglobal_shader_parameter_get_type(name:StringName)const🔗
Returns the type associated to the global shader uniform specified byname.
Note:global_shader_parameter_get()has a large performance penalty as the rendering thread needs to synchronize with the calling thread, which is slow. Do not use this method during gameplay to avoid stuttering. If you need to read values in a script after setting them, consider creating an autoload where you store the values you need to query at the same time you're setting them as global parameters.
voidglobal_shader_parameter_remove(name:StringName)🔗
Removes the global shader uniform specified byname.
voidglobal_shader_parameter_set(name:StringName, value:Variant)🔗
Sets the global shader uniformnametovalue.
voidglobal_shader_parameter_set_override(name:StringName, value:Variant)🔗
Overrides the global shader uniformnamewithvalue. Equivalent to theShaderGlobalsOverridenode.
boolhas_changed()const🔗
Returnstrueif changes have been made to the RenderingServer's data.force_draw()is usually called if this happens.
boolhas_feature(feature:Features)const🔗
Deprecated:This method has not been used since Godot 3.0.
This method does nothing and always returnsfalse.
boolhas_os_feature(feature:String)const🔗
Returnstrueif the OS supports a certainfeature. Features might bes3tc,etc, andetc2.
voidinstance_attach_object_instance_id(instance:RID, id:int)🔗
Attaches a unique Object ID to instance. Object ID must be attached to instance for proper culling withinstances_cull_aabb(),instances_cull_convex(), andinstances_cull_ray().
voidinstance_attach_skeleton(instance:RID, skeleton:RID)🔗
Attaches a skeleton to an instance. Removes the previous skeleton from the instance.
RIDinstance_create()🔗
Creates a visual instance and adds it to the RenderingServer. It can be accessed with the RID that is returned. This RID will be used in allinstance_*RenderingServer functions.
Once finished with your RID, you will want to free the RID using the RenderingServer'sfree_rid()method.
An instance is a way of placing a 3D object in the scenario. Objects like particles, meshes, reflection probes and decals need to be associated with an instance to be visible in the scenario usinginstance_set_base().
Note:The equivalent node isVisualInstance3D.
RIDinstance_create2(base:RID, scenario:RID)🔗
Creates a visual instance, adds it to the RenderingServer, and sets both base and scenario. It can be accessed with the RID that is returned. This RID will be used in allinstance_*RenderingServer functions.
Once finished with your RID, you will want to free the RID using the RenderingServer'sfree_rid()method. This is a shorthand for usinginstance_create()and setting the base and scenario manually.
Variantinstance_geometry_get_shader_parameter(instance:RID, parameter:StringName)const🔗
Returns the value of the per-instance shader uniform from the specified 3D geometry instance. Equivalent toGeometryInstance3D.get_instance_shader_parameter().
Note:Per-instance shader parameter names are case-sensitive.
Variantinstance_geometry_get_shader_parameter_default_value(instance:RID, parameter:StringName)const🔗
Returns the default value of the per-instance shader uniform from the specified 3D geometry instance. Equivalent toGeometryInstance3D.get_instance_shader_parameter().
Array[Dictionary]instance_geometry_get_shader_parameter_list(instance:RID)const🔗
Returns a dictionary of per-instance shader uniform names of the per-instance shader uniform from the specified 3D geometry instance. The returned dictionary is in PropertyInfo format, with the keysname,class_name,type,hint,hint_stringandusage. Equivalent toGeometryInstance3D.get_instance_shader_parameter().
voidinstance_geometry_set_cast_shadows_setting(instance:RID, shadow_casting_setting:ShadowCastingSetting)🔗
Sets the shadow casting setting. Equivalent toGeometryInstance3D.cast_shadow.
voidinstance_geometry_set_flag(instance:RID, flag:InstanceFlags, enabled:bool)🔗
Sets theflagfor a giveninstancetoenabled.
voidinstance_geometry_set_lightmap(instance:RID, lightmap:RID, lightmap_uv_scale:Rect2, lightmap_slice:int)🔗
Sets the lightmap GI instance to use for the specified 3D geometry instance. The lightmap UV scale for the specified instance (equivalent toGeometryInstance3D.gi_lightmap_scale) and lightmap atlas slice must also be specified.
voidinstance_geometry_set_lod_bias(instance:RID, lod_bias:float)🔗
Sets the level of detail bias to use when rendering the specified 3D geometry instance. Higher values result in higher detail from further away. Equivalent toGeometryInstance3D.lod_bias.
voidinstance_geometry_set_material_overlay(instance:RID, material:RID)🔗
Sets a material that will be rendered for all surfaces on top of active materials for the mesh associated with this instance. Equivalent toGeometryInstance3D.material_overlay.
voidinstance_geometry_set_material_override(instance:RID, material:RID)🔗
Sets a material that will override the material for all surfaces on the mesh associated with this instance. Equivalent toGeometryInstance3D.material_override.
voidinstance_geometry_set_shader_parameter(instance:RID, parameter:StringName, value:Variant)🔗
Sets the per-instance shader uniform on the specified 3D geometry instance. Equivalent toGeometryInstance3D.set_instance_shader_parameter().
voidinstance_geometry_set_transparency(instance:RID, transparency:float)🔗
Sets the transparency for the given geometry instance. Equivalent toGeometryInstance3D.transparency.
A transparency of0.0is fully opaque, while1.0is fully transparent. Values greater than0.0(exclusive) will force the geometry's materials to go through the transparent pipeline, which is slower to render and can exhibit rendering issues due to incorrect transparency sorting. However, unlike using a transparent material, settingtransparencyto a value greater than0.0(exclusive) willnotdisable shadow rendering.
In spatial shaders,1.0-transparencyis set as the default value of theALPHAbuilt-in.
Note:transparencyis clamped between0.0and1.0, so this property cannot be used to make transparent materials more opaque than they originally are.
voidinstance_geometry_set_visibility_range(instance:RID, min:float, max:float, min_margin:float, max_margin:float, fade_mode:VisibilityRangeFadeMode)🔗
Sets the visibility range values for the given geometry instance. Equivalent toGeometryInstance3D.visibility_range_beginand related properties.
voidinstance_set_base(instance:RID, base:RID)🔗
Sets the base of the instance. A base can be any of the 3D objects that are created in the RenderingServer that can be displayed. For example, any of the light types, mesh, multimesh, particle system, reflection probe, decal, lightmap, voxel GI and visibility notifiers are all types that can be set as the base of an instance in order to be displayed in the scenario.
voidinstance_set_blend_shape_weight(instance:RID, shape:int, weight:float)🔗
Sets the weight for a given blend shape associated with this instance.
voidinstance_set_custom_aabb(instance:RID, aabb:AABB)🔗
Sets a custom AABB to use when culling objects from the view frustum. Equivalent to settingGeometryInstance3D.custom_aabb.
voidinstance_set_extra_visibility_margin(instance:RID, margin:float)🔗
Sets a margin to increase the size of the AABB when culling objects from the view frustum. This allows you to avoid culling objects that fall outside the view frustum. Equivalent toGeometryInstance3D.extra_cull_margin.
voidinstance_set_ignore_culling(instance:RID, enabled:bool)🔗
Iftrue, ignores both frustum and occlusion culling on the specified 3D geometry instance. This is not the same asGeometryInstance3D.ignore_occlusion_culling, which only ignores occlusion culling and leaves frustum culling intact.
voidinstance_set_layer_mask(instance:RID, mask:int)🔗
Sets the render layers that this instance will be drawn to. Equivalent toVisualInstance3D.layers.
voidinstance_set_pivot_data(instance:RID, sorting_offset:float, use_aabb_center:bool)🔗
Sets the sorting offset and switches between using the bounding box or instance origin for depth sorting.
voidinstance_set_scenario(instance:RID, scenario:RID)🔗
Sets the scenario that the instance is in. The scenario is the 3D world that the objects will be displayed in.
voidinstance_set_surface_override_material(instance:RID, surface:int, material:RID)🔗
Sets the override material of a specific surface. Equivalent toMeshInstance3D.set_surface_override_material().
voidinstance_set_transform(instance:RID, transform:Transform3D)🔗
Sets the world space transform of the instance. Equivalent toNode3D.global_transform.
voidinstance_set_visibility_parent(instance:RID, parent:RID)🔗
Sets the visibility parent for the given instance. Equivalent toNode3D.visibility_parent.
voidinstance_set_visible(instance:RID, visible:bool)🔗
Sets whether an instance is drawn or not. Equivalent toNode3D.visible.
voidinstance_teleport(instance:RID)🔗
Resets motion vectors and other interpolated values. Use thisafterteleporting a mesh from one position to another to avoid ghosting artifacts.
PackedInt64Arrayinstances_cull_aabb(aabb:AABB, scenario:RID= RID())const🔗
Returns an array of object IDs intersecting with the provided AABB. Only 3D nodes that inherit fromVisualInstance3Dare considered, such asMeshInstance3DorDirectionalLight3D. Use@GlobalScope.instance_from_id()to obtain the actual nodes. A scenario RID must be provided, which is available in theWorld3Dyou want to query. This forces an update for all resources queued to update.
Warning:This function is primarily intended for editor usage. For in-game use cases, prefer physics collision.
PackedInt64Arrayinstances_cull_convex(convex:Array[Plane], scenario:RID= RID())const🔗
Returns an array of object IDs intersecting with the provided convex shape. Only 3D nodes that inherit fromVisualInstance3Dare considered, such asMeshInstance3DorDirectionalLight3D. Use@GlobalScope.instance_from_id()to obtain the actual nodes. A scenario RID must be provided, which is available in theWorld3Dyou want to query. This forces an update for all resources queued to update.
Warning:This function is primarily intended for editor usage. For in-game use cases, prefer physics collision.
PackedInt64Arrayinstances_cull_ray(from:Vector3, to:Vector3, scenario:RID= RID())const🔗
Returns an array of object IDs intersecting with the provided 3D ray. Only 3D nodes that inherit fromVisualInstance3Dare considered, such asMeshInstance3DorDirectionalLight3D. Use@GlobalScope.instance_from_id()to obtain the actual nodes. A scenario RID must be provided, which is available in theWorld3Dyou want to query. This forces an update for all resources queued to update.
Warning:This function is primarily intended for editor usage. For in-game use cases, prefer physics collision.
boolis_on_render_thread()🔗
Returnstrueif our code is currently executing on the rendering thread.
voidlight_directional_set_blend_splits(light:RID, enable:bool)🔗
Iftrue, this directional light will blend between shadow map splits resulting in a smoother transition between them. Equivalent toDirectionalLight3D.directional_shadow_blend_splits.
voidlight_directional_set_shadow_mode(light:RID, mode:LightDirectionalShadowMode)🔗
Sets the shadow mode for this directional light. Equivalent toDirectionalLight3D.directional_shadow_mode.
voidlight_directional_set_sky_mode(light:RID, mode:LightDirectionalSkyMode)🔗
Iftrue, this light will not be used for anything except sky shaders. Use this for lights that impact your sky shader that you may want to hide from affecting the rest of the scene. For example, you may want to enable this when the sun in your sky shader falls below the horizon.
voidlight_omni_set_shadow_mode(light:RID, mode:LightOmniShadowMode)🔗
Sets whether to use a dual paraboloid or a cubemap for the shadow map. Dual paraboloid is faster but may suffer from artifacts. Equivalent toOmniLight3D.omni_shadow_mode.
voidlight_projectors_set_filter(filter:LightProjectorFilter)🔗
Sets the texture filter mode to use when rendering light projectors. This parameter is global and cannot be set on a per-light basis.
voidlight_set_bake_mode(light:RID, bake_mode:LightBakeMode)🔗
Sets the bake mode to use for the specified 3D light. Equivalent toLight3D.light_bake_mode.
voidlight_set_color(light:RID, color:Color)🔗
Sets the color of the light. Equivalent toLight3D.light_color.
voidlight_set_cull_mask(light:RID, mask:int)🔗
Sets the cull mask for this 3D light. Lights only affect objects in the selected layers. Equivalent toLight3D.light_cull_mask.
voidlight_set_distance_fade(decal:RID, enabled:bool, begin:float, shadow:float, length:float)🔗
Sets the distance fade for this 3D light. This acts as a form of level of detail (LOD) and can be used to improve performance. Equivalent toLight3D.distance_fade_enabled,Light3D.distance_fade_begin,Light3D.distance_fade_shadow, andLight3D.distance_fade_length.
voidlight_set_max_sdfgi_cascade(light:RID, cascade:int)🔗
Sets the maximum SDFGI cascade in which the 3D light's indirect lighting is rendered. Higher values allow the light to be rendered in SDFGI further away from the camera.
voidlight_set_negative(light:RID, enable:bool)🔗
Iftrue, the 3D light will subtract light instead of adding light. Equivalent toLight3D.light_negative.
voidlight_set_param(light:RID, param:LightParam, value:float)🔗
Sets the specified 3D light parameter. Equivalent toLight3D.set_param().
voidlight_set_projector(light:RID, texture:RID)🔗
Sets the projector texture to use for the specified 3D light. Equivalent toLight3D.light_projector.
voidlight_set_reverse_cull_face_mode(light:RID, enabled:bool)🔗
Iftrue, reverses the backface culling of the mesh. This can be useful when you have a flat mesh that has a light behind it. If you need to cast a shadow on both sides of the mesh, set the mesh to use double-sided shadows withinstance_geometry_set_cast_shadows_setting(). Equivalent toLight3D.shadow_reverse_cull_face.
voidlight_set_shadow(light:RID, enabled:bool)🔗
Iftrue, light will cast shadows. Equivalent toLight3D.shadow_enabled.
voidlight_set_shadow_caster_mask(light:RID, mask:int)🔗
Sets the shadow caster mask for this 3D light. Shadows will only be cast using objects in the selected layers. Equivalent toLight3D.shadow_caster_mask.
RIDlightmap_create()🔗
Creates a new lightmap global illumination instance and adds it to the RenderingServer. It can be accessed with the RID that is returned. This RID will be used in alllightmap_*RenderingServer functions.
Once finished with your RID, you will want to free the RID using the RenderingServer'sfree_rid()method.
Note:The equivalent node isLightmapGI.
PackedInt32Arraylightmap_get_probe_capture_bsp_tree(lightmap:RID)const🔗
There is currently no description for this method. Please help us bycontributing one!
PackedVector3Arraylightmap_get_probe_capture_points(lightmap:RID)const🔗
There is currently no description for this method. Please help us bycontributing one!
PackedColorArraylightmap_get_probe_capture_sh(lightmap:RID)const🔗
There is currently no description for this method. Please help us bycontributing one!
PackedInt32Arraylightmap_get_probe_capture_tetrahedra(lightmap:RID)const🔗
There is currently no description for this method. Please help us bycontributing one!
voidlightmap_set_baked_exposure_normalization(lightmap:RID, baked_exposure:float)🔗
Used to inform the renderer what exposure normalization value was used while baking the lightmap. This value will be used and modulated at run time to ensure that the lightmap maintains a consistent level of exposure even if the scene-wide exposure normalization is changed at run time. For more information seecamera_attributes_set_exposure().
voidlightmap_set_probe_bounds(lightmap:RID, bounds:AABB)🔗
There is currently no description for this method. Please help us bycontributing one!
voidlightmap_set_probe_capture_data(lightmap:RID, points:PackedVector3Array, point_sh:PackedColorArray, tetrahedra:PackedInt32Array, bsp_tree:PackedInt32Array)🔗
There is currently no description for this method. Please help us bycontributing one!
voidlightmap_set_probe_capture_update_speed(speed:float)🔗
There is currently no description for this method. Please help us bycontributing one!
voidlightmap_set_probe_interior(lightmap:RID, interior:bool)🔗
There is currently no description for this method. Please help us bycontributing one!
voidlightmap_set_textures(lightmap:RID, light:RID, uses_sh:bool)🔗
Set the textures on the givenlightmapGI instance to the texture array pointed to by thelightRID. If the lightmap texture was baked withLightmapGI.directionalset totrue, thenuses_shmust also betrue.
voidlightmaps_set_bicubic_filter(enable:bool)🔗
Toggles whether a bicubic filter should be used when lightmaps are sampled. This smoothens their appearance at a performance cost.
RIDmake_sphere_mesh(latitudes:int, longitudes:int, radius:float)🔗
Returns a mesh of a sphere with the given number of horizontal subdivisions, vertical subdivisions and radius. See alsoget_test_cube().
RIDmaterial_create()🔗
Creates an empty material and adds it to the RenderingServer. It can be accessed with the RID that is returned. This RID will be used in allmaterial_*RenderingServer functions.
Once finished with your RID, you will want to free the RID using the RenderingServer'sfree_rid()method.
Note:The equivalent resource isMaterial.
Variantmaterial_get_param(material:RID, parameter:StringName)const🔗
Returns the value of a certain material's parameter.
voidmaterial_set_next_pass(material:RID, next_material:RID)🔗
Sets an object's next material.
voidmaterial_set_param(material:RID, parameter:StringName, value:Variant)🔗
Sets a material's parameter.
voidmaterial_set_render_priority(material:RID, priority:int)🔗
Sets a material's render priority.
voidmaterial_set_shader(shader_material:RID, shader:RID)🔗
Sets a shader material's shader.
voidmaterial_set_use_debanding(enable:bool)🔗
When using the Mobile renderer,material_set_use_debanding()can be used to enable or disable the debanding feature of 3D materials (BaseMaterial3DandShaderMaterial).
material_set_use_debanding()has no effect when using the Compatibility or Forward+ renderer. In Forward+,Viewportdebanding can be used instead.
See alsoProjectSettings.rendering/anti_aliasing/quality/use_debandingandviewport_set_use_debanding().
voidmesh_add_surface(mesh:RID, surface:Dictionary)🔗
There is currently no description for this method. Please help us bycontributing one!
voidmesh_add_surface_from_arrays(mesh:RID, primitive:PrimitiveType, arrays:Array, blend_shapes:Array= [], lods:Dictionary= {}, compress_format:BitField[ArrayFormat] = 0)🔗
There is currently no description for this method. Please help us bycontributing one!
voidmesh_clear(mesh:RID)🔗
Removes all surfaces from a mesh.
RIDmesh_create()🔗
Creates a new mesh and adds it to the RenderingServer. It can be accessed with the RID that is returned. This RID will be used in allmesh_*RenderingServer functions.
Once finished with your RID, you will want to free the RID using the RenderingServer'sfree_rid()method.
To place in a scene, attach this mesh to an instance usinginstance_set_base()using the returned RID.
Note:The equivalent resource isMesh.
RIDmesh_create_from_surfaces(surfaces:Array[Dictionary], blend_shape_count:int= 0)🔗
There is currently no description for this method. Please help us bycontributing one!
intmesh_get_blend_shape_count(mesh:RID)const🔗
Returns a mesh's blend shape count.
BlendShapeModemesh_get_blend_shape_mode(mesh:RID)const🔗
Returns a mesh's blend shape mode.
AABBmesh_get_custom_aabb(mesh:RID)const🔗
Returns a mesh's custom aabb.
Dictionarymesh_get_surface(mesh:RID, surface:int)🔗
There is currently no description for this method. Please help us bycontributing one!
intmesh_get_surface_count(mesh:RID)const🔗
Returns a mesh's number of surfaces.
voidmesh_set_blend_shape_mode(mesh:RID, mode:BlendShapeMode)🔗
Sets a mesh's blend shape mode.
voidmesh_set_custom_aabb(mesh:RID, aabb:AABB)🔗
Sets a mesh's custom aabb.
voidmesh_set_shadow_mesh(mesh:RID, shadow_mesh:RID)🔗
There is currently no description for this method. Please help us bycontributing one!
Arraymesh_surface_get_arrays(mesh:RID, surface:int)const🔗
Returns a mesh's surface's buffer arrays.
Array[Array]mesh_surface_get_blend_shape_arrays(mesh:RID, surface:int)const🔗
Returns a mesh's surface's arrays for blend shapes.
intmesh_surface_get_format_attribute_stride(format:BitField[ArrayFormat], vertex_count:int)const🔗
Returns the stride of the attribute buffer for a mesh with givenformat.
intmesh_surface_get_format_index_stride(format:BitField[ArrayFormat], vertex_count:int)const🔗
Returns the stride of the index buffer for a mesh with the givenformat.
intmesh_surface_get_format_normal_tangent_stride(format:BitField[ArrayFormat], vertex_count:int)const🔗
Returns the stride of the combined normals and tangents for a mesh with givenformat. Note importantly that, while normals and tangents are in the vertex buffer with vertices, they are only interleaved with each other and so have a different stride than vertex positions.
intmesh_surface_get_format_offset(format:BitField[ArrayFormat], vertex_count:int, array_index:int)const🔗
Returns the offset of a given attribute byarray_indexin the start of its respective buffer.
intmesh_surface_get_format_skin_stride(format:BitField[ArrayFormat], vertex_count:int)const🔗
Returns the stride of the skin buffer for a mesh with givenformat.
intmesh_surface_get_format_vertex_stride(format:BitField[ArrayFormat], vertex_count:int)const🔗
Returns the stride of the vertex positions for a mesh with givenformat. Note importantly that vertex positions are stored consecutively and are not interleaved with the other attributes in the vertex buffer (normals and tangents).
RIDmesh_surface_get_material(mesh:RID, surface:int)const🔗
Returns a mesh's surface's material.
voidmesh_surface_remove(mesh:RID, surface:int)🔗
Removes the surface at the given index from the Mesh, shifting surfaces with higher index down by one.
voidmesh_surface_set_material(mesh:RID, surface:int, material:RID)🔗
Sets a mesh's surface's material.
voidmesh_surface_update_attribute_region(mesh:RID, surface:int, offset:int, data:PackedByteArray)🔗
There is currently no description for this method. Please help us bycontributing one!
voidmesh_surface_update_index_region(mesh:RID, surface:int, offset:int, data:PackedByteArray)🔗
Updates the index buffer of the mesh surface with the givendata. The expected data are 16 or 32-bit unsigned integers, which can be determined withmesh_surface_get_format_index_stride().
voidmesh_surface_update_skin_region(mesh:RID, surface:int, offset:int, data:PackedByteArray)🔗
There is currently no description for this method. Please help us bycontributing one!
voidmesh_surface_update_vertex_region(mesh:RID, surface:int, offset:int, data:PackedByteArray)🔗
There is currently no description for this method. Please help us bycontributing one!
voidmultimesh_allocate_data(multimesh:RID, instances:int, transform_format:MultimeshTransformFormat, color_format:bool= false, custom_data_format:bool= false, use_indirect:bool= false)🔗
There is currently no description for this method. Please help us bycontributing one!
RIDmultimesh_create()🔗
Creates a new multimesh on the RenderingServer and returns anRIDhandle. This RID will be used in allmultimesh_*RenderingServer functions.
Once finished with your RID, you will want to free the RID using the RenderingServer'sfree_rid()method.
To place in a scene, attach this multimesh to an instance usinginstance_set_base()using the returned RID.
Note:The equivalent resource isMultiMesh.
AABBmultimesh_get_aabb(multimesh:RID)const🔗
Calculates and returns the axis-aligned bounding box that encloses all instances within the multimesh.
PackedFloat32Arraymultimesh_get_buffer(multimesh:RID)const🔗
Returns the MultiMesh data (such as instance transforms, colors, etc.). Seemultimesh_set_buffer()for details on the returned data.
Note:If the buffer is in the engine's internal cache, it will have to be fetched from GPU memory and possibly decompressed. This meansmultimesh_get_buffer()is potentially a slow operation and should be avoided whenever possible.
RIDmultimesh_get_buffer_rd_rid(multimesh:RID)const🔗
Returns theRenderingDeviceRIDhandle of theMultiMesh, which can be used as any other buffer on the Rendering Device.
RIDmultimesh_get_command_buffer_rd_rid(multimesh:RID)const🔗
Returns theRenderingDeviceRIDhandle of theMultiMeshcommand buffer. ThisRIDis only valid ifuse_indirectis set totruewhen allocating data throughmultimesh_allocate_data(). It can be used to directly modify the instance count via buffer.
The data structure is dependent on both how many surfaces the mesh contains and whether it is indexed or not, the buffer has 5 integers in it, with the last unused if the mesh is not indexed.
Each of the values in the buffer correspond to these options:

```
Indexed:
  0 - indexCount;
  1 - instanceCount;
  2 - firstIndex;
  3 - vertexOffset;
  4 - firstInstance;
Non Indexed:
  0 - vertexCount;
  1 - instanceCount;
  2 - firstVertex;
  3 - firstInstance;
  4 - unused;
```

AABBmultimesh_get_custom_aabb(multimesh:RID)const🔗
Returns the custom AABB defined for this MultiMesh resource.
intmultimesh_get_instance_count(multimesh:RID)const🔗
Returns the number of instances allocated for this multimesh.
RIDmultimesh_get_mesh(multimesh:RID)const🔗
Returns the RID of the mesh that will be used in drawing this multimesh.
intmultimesh_get_visible_instances(multimesh:RID)const🔗
Returns the number of visible instances for this multimesh.
Colormultimesh_instance_get_color(multimesh:RID, index:int)const🔗
Returns the color by which the specified instance will be modulated.
Colormultimesh_instance_get_custom_data(multimesh:RID, index:int)const🔗
Returns the custom data associated with the specified instance.
Transform3Dmultimesh_instance_get_transform(multimesh:RID, index:int)const🔗
Returns theTransform3Dof the specified instance.
Transform2Dmultimesh_instance_get_transform_2d(multimesh:RID, index:int)const🔗
Returns theTransform2Dof the specified instance. For use when the multimesh is set to use 2D transforms.
voidmultimesh_instance_reset_physics_interpolation(multimesh:RID, index:int)🔗
Prevents physics interpolation for the specified instance during the current physics tick.
This is useful when moving an instance to a new location, to give an instantaneous change rather than interpolation from the previous location.
voidmultimesh_instance_set_color(multimesh:RID, index:int, color:Color)🔗
Sets the color by which this instance will be modulated. Equivalent toMultiMesh.set_instance_color().
voidmultimesh_instance_set_custom_data(multimesh:RID, index:int, custom_data:Color)🔗
Sets the custom data for this instance. Custom data is passed as aColor, but is interpreted as avec4in the shader. Equivalent toMultiMesh.set_instance_custom_data().
voidmultimesh_instance_set_transform(multimesh:RID, index:int, transform:Transform3D)🔗
Sets theTransform3Dfor this instance. Equivalent toMultiMesh.set_instance_transform().
voidmultimesh_instance_set_transform_2d(multimesh:RID, index:int, transform:Transform2D)🔗
Sets theTransform2Dfor this instance. For use when multimesh is used in 2D. Equivalent toMultiMesh.set_instance_transform_2d().
voidmultimesh_instances_reset_physics_interpolation(multimesh:RID)🔗
Prevents physics interpolation for all instances during the current physics tick.
This is useful when moving all instances to new locations, to give instantaneous changes rather than interpolation from the previous locations.
voidmultimesh_set_buffer(multimesh:RID, buffer:PackedFloat32Array)🔗
Set the entire data to use for drawing themultimeshat once tobuffer(such as instance transforms and colors).buffer's size must match the number of instances multiplied by the per-instance data size (which depends on the enabled MultiMesh fields). Otherwise, an error message is printed and nothing is rendered. See alsomultimesh_get_buffer().
The per-instance data size and expected data order is:

```
2D:
  - Position: 8 floats (8 floats for Transform2D)
  - Position + Vertex color: 12 floats (8 floats for Transform2D, 4 floats for Color)
  - Position + Custom data: 12 floats (8 floats for Transform2D, 4 floats of custom data)
  - Position + Vertex color + Custom data: 16 floats (8 floats for Transform2D, 4 floats for Color, 4 floats of custom data)
3D:
  - Position: 12 floats (12 floats for Transform3D)
  - Position + Vertex color: 16 floats (12 floats for Transform3D, 4 floats for Color)
  - Position + Custom data: 16 floats (12 floats for Transform3D, 4 floats of custom data)
  - Position + Vertex color + Custom data: 20 floats (12 floats for Transform3D, 4 floats for Color, 4 floats of custom data)
```

Instance transforms are in row-major order. Specifically:

- ForTransform2Dthe float-order is:(x.x,y.x,padding_float,origin.x,x.y,y.y,padding_float,origin.y).
ForTransform2Dthe float-order is:(x.x,y.x,padding_float,origin.x,x.y,y.y,padding_float,origin.y).
- ForTransform3Dthe float-order is:(basis.x.x,basis.y.x,basis.z.x,origin.x,basis.x.y,basis.y.y,basis.z.y,origin.y,basis.x.z,basis.y.z,basis.z.z,origin.z).
ForTransform3Dthe float-order is:(basis.x.x,basis.y.x,basis.z.x,origin.x,basis.x.y,basis.y.y,basis.z.y,origin.y,basis.x.z,basis.y.z,basis.z.z,origin.z).
voidmultimesh_set_buffer_interpolated(multimesh:RID, buffer:PackedFloat32Array, buffer_previous:PackedFloat32Array)🔗
Alternative version ofmultimesh_set_buffer()for use with physics interpolation.
Takes both an array of current data and an array of data for the previous physics tick.
voidmultimesh_set_custom_aabb(multimesh:RID, aabb:AABB)🔗
Sets the custom AABB for this MultiMesh resource.
voidmultimesh_set_mesh(multimesh:RID, mesh:RID)🔗
Sets the mesh to be drawn by the multimesh. Equivalent toMultiMesh.mesh.
voidmultimesh_set_physics_interpolated(multimesh:RID, interpolated:bool)🔗
Turns on and off physics interpolation for this MultiMesh resource.
voidmultimesh_set_physics_interpolation_quality(multimesh:RID, quality:MultimeshPhysicsInterpolationQuality)🔗
Sets the physics interpolation quality for theMultiMesh.
A value ofMULTIMESH_INTERP_QUALITY_FASTgives fast but low quality interpolation, a value ofMULTIMESH_INTERP_QUALITY_HIGHgives slower but higher quality interpolation.
voidmultimesh_set_visible_instances(multimesh:RID, visible:int)🔗
Sets the number of instances visible at a given time. If -1, all instances that have been allocated are drawn. Equivalent toMultiMesh.visible_instance_count.
RIDoccluder_create()🔗
Creates an occluder instance and adds it to the RenderingServer. It can be accessed with the RID that is returned. This RID will be used in alloccluder_*RenderingServer functions.
Once finished with your RID, you will want to free the RID using the RenderingServer'sfree_rid()method.
Note:The equivalent resource isOccluder3D(not to be confused with theOccluderInstance3Dnode).
voidoccluder_set_mesh(occluder:RID, vertices:PackedVector3Array, indices:PackedInt32Array)🔗
Sets the mesh data for the given occluder RID, which controls the shape of the occlusion culling that will be performed.
RIDomni_light_create()🔗
Creates a new omni light and adds it to the RenderingServer. It can be accessed with the RID that is returned. This RID can be used in mostlight_*RenderingServer functions.
Once finished with your RID, you will want to free the RID using the RenderingServer'sfree_rid()method.
To place in a scene, attach this omni light to an instance usinginstance_set_base()using the returned RID.
Note:The equivalent node isOmniLight3D.
RIDparticles_collision_create()🔗
Creates a new 3D GPU particle collision or attractor and adds it to the RenderingServer. It can be accessed with the RID that is returned. This RID can be used in mostparticles_collision_*RenderingServer functions.
Note:The equivalent nodes areGPUParticlesCollision3DandGPUParticlesAttractor3D.
voidparticles_collision_height_field_update(particles_collision:RID)🔗
Requests an update for the 3D GPU particle collision heightfield. This may be automatically called by the 3D GPU particle collision heightfield depending on itsGPUParticlesCollisionHeightField3D.update_mode.
voidparticles_collision_set_attractor_attenuation(particles_collision:RID, curve:float)🔗
Sets the attenuationcurvefor the 3D GPU particles attractor specified by theparticles_collisionRID. Only used for attractors, not colliders. Equivalent toGPUParticlesAttractor3D.attenuation.
voidparticles_collision_set_attractor_directionality(particles_collision:RID, amount:float)🔗
Sets the directionalityamountfor the 3D GPU particles attractor specified by theparticles_collisionRID. Only used for attractors, not colliders. Equivalent toGPUParticlesAttractor3D.directionality.
voidparticles_collision_set_attractor_strength(particles_collision:RID, strength:float)🔗
Sets thestrengthfor the 3D GPU particles attractor specified by theparticles_collisionRID. Only used for attractors, not colliders. Equivalent toGPUParticlesAttractor3D.strength.
voidparticles_collision_set_box_extents(particles_collision:RID, extents:Vector3)🔗
Sets theextentsfor the 3D GPU particles collision by theparticles_collisionRID. Equivalent toGPUParticlesCollisionBox3D.size,GPUParticlesCollisionSDF3D.size,GPUParticlesCollisionHeightField3D.size,GPUParticlesAttractorBox3D.sizeorGPUParticlesAttractorVectorField3D.sizedepending on theparticles_collisiontype.
voidparticles_collision_set_collision_type(particles_collision:RID, type:ParticlesCollisionType)🔗
Sets the collision or attractor shapetypefor the 3D GPU particles collision or attractor specified by theparticles_collisionRID.
voidparticles_collision_set_cull_mask(particles_collision:RID, mask:int)🔗
Sets the cullmaskfor the 3D GPU particles collision or attractor specified by theparticles_collisionRID. Equivalent toGPUParticlesCollision3D.cull_maskorGPUParticlesAttractor3D.cull_maskdepending on theparticles_collisiontype.
voidparticles_collision_set_field_texture(particles_collision:RID, texture:RID)🔗
Sets the signed distance fieldtexturefor the 3D GPU particles collision specified by theparticles_collisionRID. Equivalent toGPUParticlesCollisionSDF3D.textureorGPUParticlesAttractorVectorField3D.texturedepending on theparticles_collisiontype.
voidparticles_collision_set_height_field_mask(particles_collision:RID, mask:int)🔗
Sets the heightfieldmaskfor the 3D GPU particles heightfield collision specified by theparticles_collisionRID. Equivalent toGPUParticlesCollisionHeightField3D.heightfield_mask.
voidparticles_collision_set_height_field_resolution(particles_collision:RID, resolution:ParticlesCollisionHeightfieldResolution)🔗
Sets the heightmapresolutionfor the 3D GPU particles heightfield collision specified by theparticles_collisionRID. Equivalent toGPUParticlesCollisionHeightField3D.resolution.
voidparticles_collision_set_sphere_radius(particles_collision:RID, radius:float)🔗
Sets theradiusfor the 3D GPU particles sphere collision or attractor specified by theparticles_collisionRID. Equivalent toGPUParticlesCollisionSphere3D.radiusorGPUParticlesAttractorSphere3D.radiusdepending on theparticles_collisiontype.
RIDparticles_create()🔗
Creates a GPU-based particle system and adds it to the RenderingServer. It can be accessed with the RID that is returned. This RID will be used in allparticles_*RenderingServer functions.
Once finished with your RID, you will want to free the RID using the RenderingServer'sfree_rid()method.
To place in a scene, attach these particles to an instance usinginstance_set_base()using the returned RID.
Note:The equivalent nodes areGPUParticles2DandGPUParticles3D.
Note:Allparticles_*methods only apply to GPU-based particles, not CPU-based particles.CPUParticles2DandCPUParticles3Ddo not have equivalent RenderingServer functions available, as these useMultiMeshInstance2DandMultiMeshInstance3Dunder the hood (seemultimesh_*methods).
voidparticles_emit(particles:RID, transform:Transform3D, velocity:Vector3, color:Color, custom:Color, emit_flags:int)🔗
Manually emits particles from theparticlesinstance.
AABBparticles_get_current_aabb(particles:RID)🔗
Calculates and returns the axis-aligned bounding box that contains all the particles. Equivalent toGPUParticles3D.capture_aabb().
boolparticles_get_emitting(particles:RID)🔗
Returnstrueif particles are currently set to emitting.
boolparticles_is_inactive(particles:RID)🔗
Returnstrueif particles are not emitting and particles are set to inactive.
voidparticles_request_process(particles:RID)🔗
Add particle system to list of particle systems that need to be updated. Update will take place on the next frame, or on the next call toinstances_cull_aabb(),instances_cull_convex(), orinstances_cull_ray().
voidparticles_request_process_time(particles:RID, time:float)🔗
Requests particles to process for extra process time during a single frame.
voidparticles_restart(particles:RID)🔗
Reset the particles on the next update. Equivalent toGPUParticles3D.restart().
voidparticles_set_amount(particles:RID, amount:int)🔗
Sets the number of particles to be drawn and allocates the memory for them. Equivalent toGPUParticles3D.amount.
voidparticles_set_amount_ratio(particles:RID, ratio:float)🔗
Sets the amount ratio for particles to be emitted. Equivalent toGPUParticles3D.amount_ratio.
voidparticles_set_collision_base_size(particles:RID, size:float)🔗
There is currently no description for this method. Please help us bycontributing one!
voidparticles_set_custom_aabb(particles:RID, aabb:AABB)🔗
Sets a custom axis-aligned bounding box for the particle system. Equivalent toGPUParticles3D.visibility_aabb.
voidparticles_set_draw_order(particles:RID, order:ParticlesDrawOrder)🔗
Sets the draw order of the particles. Equivalent toGPUParticles3D.draw_order.
voidparticles_set_draw_pass_mesh(particles:RID, pass:int, mesh:RID)🔗
Sets the mesh to be used for the specified draw pass. Equivalent toGPUParticles3D.draw_pass_1,GPUParticles3D.draw_pass_2,GPUParticles3D.draw_pass_3, andGPUParticles3D.draw_pass_4.
voidparticles_set_draw_passes(particles:RID, count:int)🔗
Sets the number of draw passes to use. Equivalent toGPUParticles3D.draw_passes.
voidparticles_set_emission_transform(particles:RID, transform:Transform3D)🔗
Sets theTransform3Dthat will be used by the particles when they first emit.
voidparticles_set_emitter_velocity(particles:RID, velocity:Vector3)🔗
Sets the velocity of a particle node, that will be used byParticleProcessMaterial.inherit_velocity_ratio.
voidparticles_set_emitting(particles:RID, emitting:bool)🔗
Iftrue, particles will emit over time. Setting tofalsedoes not reset the particles, but only stops their emission. Equivalent toGPUParticles3D.emitting.
voidparticles_set_explosiveness_ratio(particles:RID, ratio:float)🔗
Sets the explosiveness ratio. Equivalent toGPUParticles3D.explosiveness.
voidparticles_set_fixed_fps(particles:RID, fps:int)🔗
Sets the frame rate that the particle system rendering will be fixed to. Equivalent toGPUParticles3D.fixed_fps.
voidparticles_set_fractional_delta(particles:RID, enable:bool)🔗
Iftrue, uses fractional delta which smooths the movement of the particles. Equivalent toGPUParticles3D.fract_delta.
voidparticles_set_interp_to_end(particles:RID, factor:float)🔗
Sets the value that informs aParticleProcessMaterialto rush all particles towards the end of their lifetime.
voidparticles_set_interpolate(particles:RID, enable:bool)🔗
There is currently no description for this method. Please help us bycontributing one!
voidparticles_set_lifetime(particles:RID, lifetime:float)🔗
Sets the lifetime of each particle in the system. Equivalent toGPUParticles3D.lifetime.
voidparticles_set_mode(particles:RID, mode:ParticlesMode)🔗
Sets whether the GPU particles specified by theparticlesRID should be rendered in 2D or 3D according tomode.
voidparticles_set_one_shot(particles:RID, one_shot:bool)🔗
Iftrue, particles will emit once and then stop. Equivalent toGPUParticles3D.one_shot.
voidparticles_set_pre_process_time(particles:RID, time:float)🔗
Sets the preprocess time for the particles' animation. This lets you delay starting an animation until after the particles have begun emitting. Equivalent toGPUParticles3D.preprocess.
voidparticles_set_process_material(particles:RID, material:RID)🔗
Sets the material for processing the particles.
Note:This is not the material used to draw the materials. Equivalent toGPUParticles3D.process_material.
voidparticles_set_randomness_ratio(particles:RID, ratio:float)🔗
Sets the emission randomness ratio. This randomizes the emission of particles within their phase. Equivalent toGPUParticles3D.randomness.
voidparticles_set_speed_scale(particles:RID, scale:float)🔗
Sets the speed scale of the particle system. Equivalent toGPUParticles3D.speed_scale.
voidparticles_set_subemitter(particles:RID, subemitter_particles:RID)🔗
There is currently no description for this method. Please help us bycontributing one!
voidparticles_set_trail_bind_poses(particles:RID, bind_poses:Array[Transform3D])🔗
There is currently no description for this method. Please help us bycontributing one!
voidparticles_set_trails(particles:RID, enable:bool, length_sec:float)🔗
Ifenableistrue, enables trails for theparticleswith the specifiedlength_secin seconds. Equivalent toGPUParticles3D.trail_enabledandGPUParticles3D.trail_lifetime.
voidparticles_set_transform_align(particles:RID, align:ParticlesTransformAlign)🔗
There is currently no description for this method. Please help us bycontributing one!
voidparticles_set_use_local_coordinates(particles:RID, enable:bool)🔗
Iftrue, particles use local coordinates. Iffalsethey use global coordinates. Equivalent toGPUParticles3D.local_coords.
voidpositional_soft_shadow_filter_set_quality(quality:ShadowQuality)🔗
Sets the filter quality for omni and spot light shadows in 3D. See alsoProjectSettings.rendering/lights_and_shadows/positional_shadow/soft_shadow_filter_quality. This parameter is global and cannot be set on a per-viewport basis.
RIDreflection_probe_create()🔗
Creates a reflection probe and adds it to the RenderingServer. It can be accessed with the RID that is returned. This RID will be used in allreflection_probe_*RenderingServer functions.
Once finished with your RID, you will want to free the RID using the RenderingServer'sfree_rid()method.
To place in a scene, attach this reflection probe to an instance usinginstance_set_base()using the returned RID.
Note:The equivalent node isReflectionProbe.
voidreflection_probe_set_ambient_color(probe:RID, color:Color)🔗
Sets the reflection probe's custom ambient light color. Equivalent toReflectionProbe.ambient_color.
voidreflection_probe_set_ambient_energy(probe:RID, energy:float)🔗
Sets the reflection probe's custom ambient light energy. Equivalent toReflectionProbe.ambient_color_energy.
voidreflection_probe_set_ambient_mode(probe:RID, mode:ReflectionProbeAmbientMode)🔗
Sets the reflection probe's ambient light mode. Equivalent toReflectionProbe.ambient_mode.
voidreflection_probe_set_as_interior(probe:RID, enable:bool)🔗
Iftrue, reflections will ignore sky contribution. Equivalent toReflectionProbe.interior.
voidreflection_probe_set_blend_distance(probe:RID, blend_distance:float)🔗
Sets the distance in meters over which a probe blends into the scene.
voidreflection_probe_set_cull_mask(probe:RID, layers:int)🔗
Sets the render cull mask for this reflection probe. Only instances with a matching layer will be reflected by this probe. Equivalent toReflectionProbe.cull_mask.
voidreflection_probe_set_enable_box_projection(probe:RID, enable:bool)🔗
Iftrue, uses box projection. This can make reflections look more correct in certain situations. Equivalent toReflectionProbe.box_projection.
voidreflection_probe_set_enable_shadows(probe:RID, enable:bool)🔗
Iftrue, computes shadows in the reflection probe. This makes the reflection much slower to compute. Equivalent toReflectionProbe.enable_shadows.
voidreflection_probe_set_intensity(probe:RID, intensity:float)🔗
Sets the intensity of the reflection probe. Intensity modulates the strength of the reflection. Equivalent toReflectionProbe.intensity.
voidreflection_probe_set_max_distance(probe:RID, distance:float)🔗
Sets the max distance away from the probe an object can be before it is culled. Equivalent toReflectionProbe.max_distance.
voidreflection_probe_set_mesh_lod_threshold(probe:RID, pixels:float)🔗
Sets the mesh level of detail to use in the reflection probe rendering. Higher values will use less detailed versions of meshes that have LOD variations generated, which can improve performance. Equivalent toReflectionProbe.mesh_lod_threshold.
voidreflection_probe_set_origin_offset(probe:RID, offset:Vector3)🔗
Sets the origin offset to be used when this reflection probe is in box project mode. Equivalent toReflectionProbe.origin_offset.
voidreflection_probe_set_reflection_mask(probe:RID, layers:int)🔗
Sets the render reflection mask for this reflection probe. Only instances with a matching layer will have reflections applied from this probe. Equivalent toReflectionProbe.reflection_mask.
voidreflection_probe_set_resolution(probe:RID, resolution:int)🔗
Deprecated:This method has not done anything since Godot 3.
Deprecated. This method does nothing.
voidreflection_probe_set_size(probe:RID, size:Vector3)🔗
Sets the size of the area that the reflection probe will capture. Equivalent toReflectionProbe.size.
voidreflection_probe_set_update_mode(probe:RID, mode:ReflectionProbeUpdateMode)🔗
Sets how often the reflection probe updates. Can either be once or every frame.
voidrequest_frame_drawn_callback(callable:Callable)🔗
Schedules a callback to the given callable after a frame has been drawn.
RIDscenario_create()🔗
Creates a scenario and adds it to the RenderingServer. It can be accessed with the RID that is returned. This RID will be used in allscenario_*RenderingServer functions.
Once finished with your RID, you will want to free the RID using the RenderingServer'sfree_rid()method.
The scenario is the 3D world that all the visual instances exist in.
voidscenario_set_camera_attributes(scenario:RID, effects:RID)🔗
Sets the camera attributes (effects) that will be used with this scenario. See alsoCameraAttributes.
voidscenario_set_compositor(scenario:RID, compositor:RID)🔗
Sets the compositor (compositor) that will be used with this scenario. See alsoCompositor.
voidscenario_set_environment(scenario:RID, environment:RID)🔗
Sets the environment that will be used with this scenario. See alsoEnvironment.
voidscenario_set_fallback_environment(scenario:RID, environment:RID)🔗
Sets the fallback environment to be used by this scenario. The fallback environment is used if no environment is set. Internally, this is used by the editor to provide a default environment.
voidscreen_space_roughness_limiter_set_active(enable:bool, amount:float, limit:float)🔗
Sets the screen-space roughness limiter parameters, such as whether it should be enabled and its thresholds. Equivalent toProjectSettings.rendering/anti_aliasing/screen_space_roughness_limiter/enabled,ProjectSettings.rendering/anti_aliasing/screen_space_roughness_limiter/amountandProjectSettings.rendering/anti_aliasing/screen_space_roughness_limiter/limit.
voidset_boot_image(image:Image, color:Color, scale:bool, use_filter:bool= true)🔗
Deprecated:Useset_boot_image_with_stretch()instead.
Sets a boot image. Thecolordefines the background color. The value ofscaleindicates if the image will be scaled to fit the screen size. Ifuse_filteristrue, the image will be scaled with linear interpolation. Ifuse_filterisfalse, the image will be scaled with nearest-neighbor interpolation.
voidset_boot_image_with_stretch(image:Image, color:Color, stretch_mode:SplashStretchMode, use_filter:bool= true)🔗
Sets a boot image. Thecolordefines the background color. The value ofstretch_modeindicates how the image will be stretched (seeSplashStretchModefor possible values). Ifuse_filteristrue, the image will be scaled with linear interpolation. Ifuse_filterisfalse, the image will be scaled with nearest-neighbor interpolation.
voidset_debug_generate_wireframes(generate:bool)🔗
Ifgenerateistrue, generates debug wireframes for all meshes that are loaded when using the Compatibility renderer. By default, the engine does not generate debug wireframes at runtime, since they slow down loading of assets and take up VRAM.
Note:You must call this method before loading any meshes when using the Compatibility renderer, otherwise wireframes will not be used.
voidset_default_clear_color(color:Color)🔗
Sets the default clear color which is used when a specific clear color has not been selected. See alsoget_default_clear_color().
RIDshader_create()🔗
Creates an empty shader and adds it to the RenderingServer. It can be accessed with the RID that is returned. This RID will be used in allshader_*RenderingServer functions.
Once finished with your RID, you will want to free the RID using the RenderingServer'sfree_rid()method.
Note:The equivalent resource isShader.
Stringshader_get_code(shader:RID)const🔗
Returns a shader's source code as a string.
RIDshader_get_default_texture_parameter(shader:RID, name:StringName, index:int= 0)const🔗
Returns a default texture from a shader searched by name.
Note:If the sampler array is used useindexto access the specified texture.
Variantshader_get_parameter_default(shader:RID, name:StringName)const🔗
Returns the default value for the specified shader uniform. This is usually the value written in the shader source code.
voidshader_set_code(shader:RID, code:String)🔗
Sets the shader's source code (which triggers recompilation after being changed).
voidshader_set_default_texture_parameter(shader:RID, name:StringName, texture:RID, index:int= 0)🔗
Sets a shader's default texture. Overwrites the texture given by name.
Note:If the sampler array is used useindexto access the specified texture.
voidshader_set_path_hint(shader:RID, path:String)🔗
Sets the path hint for the specified shader. This should generally match theShaderresource'sResource.resource_path.
voidskeleton_allocate_data(skeleton:RID, bones:int, is_2d_skeleton:bool= false)🔗
There is currently no description for this method. Please help us bycontributing one!
Transform3Dskeleton_bone_get_transform(skeleton:RID, bone:int)const🔗
Returns theTransform3Dset for a specific bone of this skeleton.
Transform2Dskeleton_bone_get_transform_2d(skeleton:RID, bone:int)const🔗
Returns theTransform2Dset for a specific bone of this skeleton.
voidskeleton_bone_set_transform(skeleton:RID, bone:int, transform:Transform3D)🔗
Sets theTransform3Dfor a specific bone of this skeleton.
voidskeleton_bone_set_transform_2d(skeleton:RID, bone:int, transform:Transform2D)🔗
Sets theTransform2Dfor a specific bone of this skeleton.
RIDskeleton_create()🔗
Creates a skeleton and adds it to the RenderingServer. It can be accessed with the RID that is returned. This RID will be used in allskeleton_*RenderingServer functions.
Once finished with your RID, you will want to free the RID using the RenderingServer'sfree_rid()method.
intskeleton_get_bone_count(skeleton:RID)const🔗
Returns the number of bones allocated for this skeleton.
voidskeleton_set_base_transform_2d(skeleton:RID, base_transform:Transform2D)🔗
There is currently no description for this method. Please help us bycontributing one!
Imagesky_bake_panorama(sky:RID, energy:float, bake_irradiance:bool, size:Vector2i)🔗
Generates and returns anImagecontaining the radiance map for the specifiedskyRID. This supports built-in sky material and custom sky shaders. Ifbake_irradianceistrue, the irradiance map is saved instead of the radiance map. The radiance map is used to render reflected light, while the irradiance map is used to render ambient light. See alsoenvironment_bake_panorama().
Note:The image is saved using linear encoding without any tonemapping performed, which means it will look too dark if viewed directly in an image editor.energyvalues above1.0can be used to brighten the resulting image.
Note:sizeshould be a 2:1 aspect ratio for the generated panorama to have square pixels. For radiance maps, there is no point in using a height greater thanSky.radiance_size, as it won't increase detail. Irradiance maps only contain low-frequency data, so there is usually no point in going past a size of 128×64 pixels when saving an irradiance map.
RIDsky_create()🔗
Creates an empty sky and adds it to the RenderingServer. It can be accessed with the RID that is returned. This RID will be used in allsky_*RenderingServer functions.
Once finished with your RID, you will want to free the RID using the RenderingServer'sfree_rid()method.
voidsky_set_material(sky:RID, material:RID)🔗
Sets the material that the sky uses to render the background, ambient and reflection maps.
voidsky_set_mode(sky:RID, mode:SkyMode)🔗
Sets the processmodeof the sky specified by theskyRID. Equivalent toSky.process_mode.
voidsky_set_radiance_size(sky:RID, radiance_size:int)🔗
Sets theradiance_sizeof the sky specified by theskyRID (in pixels). Equivalent toSky.radiance_size.
RIDspot_light_create()🔗
Creates a spot light and adds it to the RenderingServer. It can be accessed with the RID that is returned. This RID can be used in mostlight_*RenderingServer functions.
Once finished with your RID, you will want to free the RID using the RenderingServer'sfree_rid()method.
To place in a scene, attach this spot light to an instance usinginstance_set_base()using the returned RID.
voidsub_surface_scattering_set_quality(quality:SubSurfaceScatteringQuality)🔗
SetsProjectSettings.rendering/environment/subsurface_scattering/subsurface_scattering_qualityto use when rendering materials that have subsurface scattering enabled.
voidsub_surface_scattering_set_scale(scale:float, depth_scale:float)🔗
Sets theProjectSettings.rendering/environment/subsurface_scattering/subsurface_scattering_scaleandProjectSettings.rendering/environment/subsurface_scattering/subsurface_scattering_depth_scaleto use when rendering materials that have subsurface scattering enabled.
RIDtexture_2d_create(image:Image)🔗
Creates a 2-dimensional texture and adds it to the RenderingServer. It can be accessed with the RID that is returned. This RID will be used in alltexture_2d_*RenderingServer functions.
Once finished with your RID, you will want to free the RID using the RenderingServer'sfree_rid()method.
Note:The equivalent resource isTexture2D.
Note:Not to be confused withRenderingDevice.texture_create(), which creates the graphics API's own texture type as opposed to the Godot-specificTexture2Dresource.
Imagetexture_2d_get(texture:RID)const🔗
Returns anImageinstance from the giventextureRID.
Example:Get the test texture fromget_test_texture()and apply it to aSprite2Dnode:

```
var texture_rid = RenderingServer.get_test_texture()
var texture = ImageTexture.create_from_image(RenderingServer.texture_2d_get(texture_rid))
$Sprite2D.texture = texture
```

Imagetexture_2d_layer_get(texture:RID, layer:int)const🔗
Returns anImageinstance from the giventextureRIDandlayer.
RIDtexture_2d_layered_create(layers:Array[Image], layered_type:TextureLayeredType)🔗
Creates a 2-dimensional layered texture and adds it to the RenderingServer. It can be accessed with the RID that is returned. This RID will be used in alltexture_2d_layered_*RenderingServer functions.
Once finished with your RID, you will want to free the RID using the RenderingServer'sfree_rid()method.
Note:The equivalent resource isTextureLayered.
RIDtexture_2d_layered_placeholder_create(layered_type:TextureLayeredType)🔗
Creates a placeholder for a 2-dimensional layered texture and adds it to the RenderingServer. It can be accessed with the RID that is returned. This RID will be used in alltexture_2d_layered_*RenderingServer functions, although it does nothing when used. See alsotexture_2d_placeholder_create().
Note:The equivalent resource isPlaceholderTextureLayered.
RIDtexture_2d_placeholder_create()🔗
Creates a placeholder for a 2-dimensional layered texture and adds it to the RenderingServer. It can be accessed with the RID that is returned. This RID will be used in alltexture_2d_layered_*RenderingServer functions, although it does nothing when used. See alsotexture_2d_layered_placeholder_create().
Once finished with your RID, you will want to free the RID using the RenderingServer'sfree_rid()method.
Note:The equivalent resource isPlaceholderTexture2D.
voidtexture_2d_update(texture:RID, image:Image, layer:int)🔗
Updates the texture specified by thetextureRIDwith the data inimage. Alayermust also be specified, which should be0when updating a single-layer texture (Texture2D).
Note:Theimagemust have the same width, height and format as the currenttexturedata. Otherwise, an error will be printed and the original texture won't be modified. If you need to use different width, height or format, usetexture_replace()instead.
RIDtexture_3d_create(format:Format, width:int, height:int, depth:int, mipmaps:bool, data:Array[Image])🔗
Note:The equivalent resource isTexture3D.
Array[Image]texture_3d_get(texture:RID)const🔗
Returns 3D texture data as an array ofImages for the specified textureRID.
RIDtexture_3d_placeholder_create()🔗
Creates a placeholder for a 3-dimensional texture and adds it to the RenderingServer. It can be accessed with the RID that is returned. This RID will be used in alltexture_3d_*RenderingServer functions, although it does nothing when used.
Once finished with your RID, you will want to free the RID using the RenderingServer'sfree_rid()method.
Note:The equivalent resource isPlaceholderTexture3D.
voidtexture_3d_update(texture:RID, data:Array[Image])🔗
Updates the texture specified by thetextureRID's data with the data indata. All the texture's layers must be replaced at once.
Note:Thetexturemust have the same width, height, depth and format as the current texture data. Otherwise, an error will be printed and the original texture won't be modified. If you need to use different width, height, depth or format, usetexture_replace()instead.
RIDtexture_create_from_native_handle(type:TextureType, format:Format, native_handle:int, width:int, height:int, depth:int, layers:int= 1, layered_type:TextureLayeredType= 0)🔗
Creates a texture based on a native handle that was created outside of Godot's renderer.
Note:If using only the rendering device renderer, it's recommend to useRenderingDevice.texture_create_from_extension()together withtexture_rd_create(), rather than this method. This way, the texture's format and usage can be controlled more effectively.
Formattexture_get_format(texture:RID)const🔗
Returns the format for the texture.
inttexture_get_native_handle(texture:RID, srgb:bool= false)const🔗
Returns the internal graphics handle for this texture object. For use when communicating with third-party APIs mostly with GDExtension.
srgbshould betruewhen the texture uses nonlinear sRGB encoding andfalsewhen the texture uses linear encoding.
Note:This function returns auint64_twhich internally maps to aGLuint(OpenGL) orVkImage(Vulkan).
Stringtexture_get_path(texture:RID)const🔗
There is currently no description for this method. Please help us bycontributing one!
RIDtexture_get_rd_texture(texture:RID, srgb:bool= false)const🔗
Returns a textureRIDthat can be used withRenderingDevice.
srgbshould betruewhen the texture uses nonlinear sRGB encoding andfalsewhen the texture uses linear encoding.
RIDtexture_proxy_create(base:RID)🔗
Deprecated:ProxyTexture was removed in Godot 4.
This method does nothing and always returns an invalidRID.
voidtexture_proxy_update(texture:RID, proxy_to:RID)🔗
Deprecated:ProxyTexture was removed in Godot 4.
This method does nothing.
RIDtexture_rd_create(rd_texture:RID, layer_type:TextureLayeredType= 0)🔗
Creates a new texture object based on a texture created directly on theRenderingDevice. If the texture contains layers,layer_typeis used to define the layer type.
Once finished with your RID, you will want to free the RID using the RenderingServer'sfree_rid()method.
Note:The RenderingServer'sfree_rid()won't free the underlyingrd_texture, you will want to free therd_textureusingRenderingDevice.free_rid().
voidtexture_replace(texture:RID, by_texture:RID)🔗
Replacestexture's texture data by the texture specified by theby_textureRID, without changingtexture's RID.
voidtexture_set_force_redraw_if_visible(texture:RID, enable:bool)🔗
There is currently no description for this method. Please help us bycontributing one!
voidtexture_set_path(texture:RID, path:String)🔗
There is currently no description for this method. Please help us bycontributing one!
voidtexture_set_size_override(texture:RID, width:int, height:int)🔗
There is currently no description for this method. Please help us bycontributing one!
voidviewport_attach_camera(viewport:RID, camera:RID)🔗
Sets a viewport's camera.
voidviewport_attach_canvas(viewport:RID, canvas:RID)🔗
Sets a viewport's canvas.
voidviewport_attach_to_screen(viewport:RID, rect:Rect2= Rect2(0, 0, 0, 0), screen:int= 0)🔗
Copies the viewport to a region of the screen specified byrect. Ifviewport_set_render_direct_to_screen()istrue, then the viewport does not use a framebuffer and the contents of the viewport are rendered directly to screen. However, note that the root viewport is drawn last, therefore it will draw over the screen. Accordingly, you must set the root viewport to an area that does not cover the area that you have attached this viewport to.
For example, you can set the root viewport to not render at all with the following code:

```
func _ready():
    RenderingServer.viewport_attach_to_screen(get_viewport().get_viewport_rid(), Rect2())
    RenderingServer.viewport_attach_to_screen($Viewport.get_viewport_rid(), Rect2(0, 0, 600, 600))
```

Using this can result in significant optimization, especially on lower-end devices. However, it comes at the cost of having to manage your viewports manually. For further optimization, seeviewport_set_render_direct_to_screen().
RIDviewport_create()🔗
Creates an empty viewport and adds it to the RenderingServer. It can be accessed with the RID that is returned. This RID will be used in allviewport_*RenderingServer functions.
Once finished with your RID, you will want to free the RID using the RenderingServer'sfree_rid()method.
Note:The equivalent node isViewport.
floatviewport_get_measured_render_time_cpu(viewport:RID)const🔗
Returns the CPU time taken to render the last frame in milliseconds. Thisonlyincludes time spent in rendering-related operations; scripts'_processfunctions and other engine subsystems are not included in this readout. To get a complete readout of CPU time spent to render the scene, sum the render times of all viewports that are drawn every frame plusget_frame_setup_time_cpu(). UnlikeEngine.get_frames_per_second(), this method will accurately reflect CPU utilization even if framerate is capped via V-Sync orEngine.max_fps. See alsoviewport_get_measured_render_time_gpu().
Note:Requires measurements to be enabled on the specifiedviewportusingviewport_set_measure_render_time(). Otherwise, this method returns0.0.
floatviewport_get_measured_render_time_gpu(viewport:RID)const🔗
Returns the GPU time taken to render the last frame in milliseconds. To get a complete readout of GPU time spent to render the scene, sum the render times of all viewports that are drawn every frame. UnlikeEngine.get_frames_per_second(), this method accurately reflects GPU utilization even if framerate is capped via V-Sync orEngine.max_fps. See alsoviewport_get_measured_render_time_cpu().
Note:Requires measurements to be enabled on the specifiedviewportusingviewport_set_measure_render_time(). Otherwise, this method returns0.0.
Note:When GPU utilization is low enough during a certain period of time, GPUs will decrease their power state (which in turn decreases core and memory clock speeds). This can cause the reported GPU time to increase if GPU utilization is kept low enough by a framerate cap (compared to what it would be at the GPU's highest power state). Keep this in mind when benchmarking usingviewport_get_measured_render_time_gpu(). This behavior can be overridden in the graphics driver settings at the cost of higher power usage.
intviewport_get_render_info(viewport:RID, type:ViewportRenderInfoType, info:ViewportRenderInfo)🔗
Returns a statistic about the rendering engine which can be used for performance profiling. This is separated into render passtypes, each of them having the sameinfos you can query (different passes will return different values).
See alsoget_rendering_info(), which returns global information across all viewports.
Note:Viewport rendering information is not available until at least 2 frames have been rendered by the engine. If rendering information is not available,viewport_get_render_info()returns0. To print rendering information in_ready()successfully, use the following:

```
func _ready():
    for _i in 2:
        await get_tree().process_frame

    print(
            RenderingServer.viewport_get_render_info(get_viewport().get_viewport_rid(),
            RenderingServer.VIEWPORT_RENDER_INFO_TYPE_VISIBLE,
            RenderingServer.VIEWPORT_RENDER_INFO_DRAW_CALLS_IN_FRAME)
    )
```

RIDviewport_get_render_target(viewport:RID)const🔗
Returns the render target for the viewport.
RIDviewport_get_texture(viewport:RID)const🔗
Returns the viewport's last rendered frame.
ViewportUpdateModeviewport_get_update_mode(viewport:RID)const🔗
Returns the viewport's update mode.
Warning:Calling this from any thread other than the rendering thread will be detrimental to performance.
voidviewport_remove_canvas(viewport:RID, canvas:RID)🔗
Detaches a viewport from a canvas.
voidviewport_set_active(viewport:RID, active:bool)🔗
Iftrue, sets the viewport active, else sets it inactive.
voidviewport_set_anisotropic_filtering_level(viewport:RID, anisotropic_filtering_level:ViewportAnisotropicFiltering)🔗
Sets the maximum number of samples to take when using anisotropic filtering on textures (as a power of two). A higher sample count will result in sharper textures at oblique angles, but is more expensive to compute. A value of0forcibly disables anisotropic filtering, even on materials where it is enabled.
The anisotropic filtering level also affects decals and light projectors if they are configured to use anisotropic filtering. SeeProjectSettings.rendering/textures/decals/filterandProjectSettings.rendering/textures/light_projectors/filter.
Note:In 3D, for this setting to have an effect, setBaseMaterial3D.texture_filtertoBaseMaterial3D.TEXTURE_FILTER_LINEAR_WITH_MIPMAPS_ANISOTROPICorBaseMaterial3D.TEXTURE_FILTER_NEAREST_WITH_MIPMAPS_ANISOTROPICon materials.
Note:In 2D, for this setting to have an effect, setCanvasItem.texture_filtertoCanvasItem.TEXTURE_FILTER_LINEAR_WITH_MIPMAPS_ANISOTROPICorCanvasItem.TEXTURE_FILTER_NEAREST_WITH_MIPMAPS_ANISOTROPICon theCanvasItemnode displaying the texture (or inCanvasTexture). However, anisotropic filtering is rarely useful in 2D, so only enable it for textures in 2D if it makes a meaningful visual difference.
voidviewport_set_canvas_cull_mask(viewport:RID, canvas_cull_mask:int)🔗
Sets the rendering mask associated with thisViewport. OnlyCanvasItemnodes with a matching rendering visibility layer will be rendered by thisViewport.
voidviewport_set_canvas_stacking(viewport:RID, canvas:RID, layer:int, sublayer:int)🔗
Sets the stacking order for a viewport's canvas.
layeris the actual canvas layer, whilesublayerspecifies the stacking order of the canvas among those in the same layer.
Note:layershould be betweenCANVAS_LAYER_MINandCANVAS_LAYER_MAX(inclusive). Any other value will wrap around.
voidviewport_set_canvas_transform(viewport:RID, canvas:RID, offset:Transform2D)🔗
Sets the transformation of a viewport's canvas.
voidviewport_set_clear_mode(viewport:RID, clear_mode:ViewportClearMode)🔗
Sets the clear mode of a viewport.
voidviewport_set_debug_draw(viewport:RID, draw:ViewportDebugDraw)🔗
Sets the debug draw mode of a viewport.
voidviewport_set_default_canvas_item_texture_filter(viewport:RID, filter:CanvasItemTextureFilter)🔗
Sets the default texture filtering mode for the specifiedviewportRID.
voidviewport_set_default_canvas_item_texture_repeat(viewport:RID, repeat:CanvasItemTextureRepeat)🔗
Sets the default texture repeat mode for the specifiedviewportRID.
voidviewport_set_disable_2d(viewport:RID, disable:bool)🔗
Iftrue, the viewport's canvas (i.e. 2D and GUI elements) is not rendered.
voidviewport_set_disable_3d(viewport:RID, disable:bool)🔗
Iftrue, the viewport's 3D elements are not rendered.
voidviewport_set_environment_mode(viewport:RID, mode:ViewportEnvironmentMode)🔗
Sets the viewport's environment mode which allows enabling or disabling rendering of 3D environment over 2D canvas. When disabled, 2D will not be affected by the environment. When enabled, 2D will be affected by the environment if the environment background mode isENV_BG_CANVAS. The default behavior is to inherit the setting from the viewport's parent. If the topmost parent is also set toVIEWPORT_ENVIRONMENT_INHERIT, then the behavior will be the same as if it was set toVIEWPORT_ENVIRONMENT_ENABLED.
voidviewport_set_fsr_sharpness(viewport:RID, sharpness:float)🔗
Determines how sharp the upscaled image will be when using the FSR upscaling mode. Sharpness halves with every whole number. Values go from 0.0 (sharpest) to 2.0. Values above 2.0 won't make a visible difference.
voidviewport_set_global_canvas_transform(viewport:RID, transform:Transform2D)🔗
Sets the viewport's global transformation matrix.
voidviewport_set_measure_render_time(viewport:RID, enable:bool)🔗
Sets the measurement for the givenviewportRID (obtained usingViewport.get_viewport_rid()). Once enabled,viewport_get_measured_render_time_cpu()andviewport_get_measured_render_time_gpu()will return values greater than0.0when queried with the givenviewport.
voidviewport_set_msaa_2d(viewport:RID, msaa:ViewportMSAA)🔗
Sets the multisample antialiasing mode for 2D/Canvas on the specifiedviewportRID. Equivalent toProjectSettings.rendering/anti_aliasing/quality/msaa_2dorViewport.msaa_2d.
voidviewport_set_msaa_3d(viewport:RID, msaa:ViewportMSAA)🔗
Sets the multisample antialiasing mode for 3D on the specifiedviewportRID. Equivalent toProjectSettings.rendering/anti_aliasing/quality/msaa_3dorViewport.msaa_3d.
voidviewport_set_occlusion_culling_build_quality(quality:ViewportOcclusionCullingBuildQuality)🔗
Sets theProjectSettings.rendering/occlusion_culling/bvh_build_qualityto use for occlusion culling. This parameter is global and cannot be set on a per-viewport basis.
voidviewport_set_occlusion_rays_per_thread(rays_per_thread:int)🔗
Sets theProjectSettings.rendering/occlusion_culling/occlusion_rays_per_threadto use for occlusion culling. This parameter is global and cannot be set on a per-viewport basis.
voidviewport_set_parent_viewport(viewport:RID, parent_viewport:RID)🔗
Sets the viewport's parent to the viewport specified by theparent_viewportRID.
voidviewport_set_positional_shadow_atlas_quadrant_subdivision(viewport:RID, quadrant:int, subdivision:int)🔗
Sets the number of subdivisions to use in the specified shadow atlasquadrantfor omni and spot shadows. See alsoViewport.set_positional_shadow_atlas_quadrant_subdiv().
voidviewport_set_positional_shadow_atlas_size(viewport:RID, size:int, use_16_bits:bool= false)🔗
Sets thesizeof the shadow atlas's images (used for omni and spot lights) on the viewport specified by theviewportRID. The value is rounded up to the nearest power of 2. Ifuse_16_bitsistrue, use 16 bits for the omni/spot shadow depth map. Enabling this results in shadows having less precision and may result in shadow acne, but can lead to performance improvements on some devices.
Note:If this is set to0, no positional shadows will be visible at all. This can improve performance significantly on low-end systems by reducing both the CPU and GPU load (as fewer draw calls are needed to draw the scene without shadows).
voidviewport_set_render_direct_to_screen(viewport:RID, enabled:bool)🔗
Iftrue, render the contents of the viewport directly to screen. This allows a low-level optimization where you can skip drawing a viewport to the root viewport. While this optimization can result in a significant increase in speed (especially on older devices), it comes at a cost of usability. When this is enabled, you cannot read from the viewport or from the screen_texture. You also lose the benefit of certain window settings, such as the various stretch modes. Another consequence to be aware of is that in 2D the rendering happens in window coordinates, so if you have a viewport that is double the size of the window, and you set this, then only the portion that fits within the window will be drawn, no automatic scaling is possible, even if your game scene is significantly larger than the window size.
voidviewport_set_scaling_3d_mode(viewport:RID, scaling_3d_mode:ViewportScaling3DMode)🔗
Sets the 3D resolution scaling mode. Bilinear scaling renders at different resolution to either undersample or supersample the viewport. FidelityFX Super Resolution 1.0, abbreviated to FSR, is an upscaling technology that produces high quality images at fast framerates by using a spatially aware upscaling algorithm. FSR is slightly more expensive than bilinear, but it produces significantly higher image quality. FSR should be used where possible.
voidviewport_set_scaling_3d_scale(viewport:RID, scale:float)🔗
Scales the 3D render buffer based on the viewport size uses an image filter specified inViewportScaling3DModeto scale the output image to the full viewport size. Values lower than1.0can be used to speed up 3D rendering at the cost of quality (undersampling). Values greater than1.0are only valid for bilinear mode and can be used to improve 3D rendering quality at a high performance cost (supersampling). See alsoViewportMSAAfor multi-sample antialiasing, which is significantly cheaper but only smoothens the edges of polygons.
When using FSR upscaling, AMD recommends exposing the following values as preset options to users "Ultra Quality: 0.77", "Quality: 0.67", "Balanced: 0.59", "Performance: 0.5" instead of exposing the entire scale.
voidviewport_set_scenario(viewport:RID, scenario:RID)🔗
Sets a viewport's scenario. The scenario contains information about environment information, reflection atlas, etc.
voidviewport_set_screen_space_aa(viewport:RID, mode:ViewportScreenSpaceAA)🔗
Sets the viewport's screen-space antialiasing mode. Equivalent toProjectSettings.rendering/anti_aliasing/quality/screen_space_aaorViewport.screen_space_aa.
voidviewport_set_sdf_oversize_and_scale(viewport:RID, oversize:ViewportSDFOversize, scale:ViewportSDFScale)🔗
Sets the viewport's 2D signed distance fieldProjectSettings.rendering/2d/sdf/oversizeandProjectSettings.rendering/2d/sdf/scale. This is used when sampling the signed distance field inCanvasItemshaders as well asGPUParticles2Dcollision. This isnotused by SDFGI in 3D rendering.
voidviewport_set_size(viewport:RID, width:int, height:int)🔗
Sets the viewport's width and height in pixels.
voidviewport_set_snap_2d_transforms_to_pixel(viewport:RID, enabled:bool)🔗
Iftrue, canvas item transforms (i.e. origin position) are snapped to the nearest pixel when rendering. This can lead to a crisper appearance at the cost of less smooth movement, especially whenCamera2Dsmoothing is enabled. Equivalent toProjectSettings.rendering/2d/snap/snap_2d_transforms_to_pixel.
voidviewport_set_snap_2d_vertices_to_pixel(viewport:RID, enabled:bool)🔗
Iftrue, canvas item vertices (i.e. polygon points) are snapped to the nearest pixel when rendering. This can lead to a crisper appearance at the cost of less smooth movement, especially whenCamera2Dsmoothing is enabled. Equivalent toProjectSettings.rendering/2d/snap/snap_2d_vertices_to_pixel.
voidviewport_set_texture_mipmap_bias(viewport:RID, mipmap_bias:float)🔗
Affects the final texture sharpness by reading from a lower or higher mipmap (also called "texture LOD bias"). Negative values make mipmapped textures sharper but grainier when viewed at a distance, while positive values make mipmapped textures blurrier (even when up close). To get sharper textures at a distance without introducing too much graininess, set this between-0.75and0.0. Enabling temporal antialiasing (ProjectSettings.rendering/anti_aliasing/quality/use_taa) can help reduce the graininess visible when using negative mipmap bias.
Note:When the 3D scaling mode is set to FSR 1.0, this value is used to adjust the automatic mipmap bias which is calculated internally based on the scale factor. The formula for this is-log2(1.0/scale)+mipmap_bias.
voidviewport_set_transparent_background(viewport:RID, enabled:bool)🔗
Iftrue, the viewport renders its background as transparent.
voidviewport_set_update_mode(viewport:RID, update_mode:ViewportUpdateMode)🔗
Sets when the viewport should be updated.
voidviewport_set_use_debanding(viewport:RID, enable:bool)🔗
Equivalent toViewport.use_debanding. See alsoProjectSettings.rendering/anti_aliasing/quality/use_debanding.
voidviewport_set_use_hdr_2d(viewport:RID, enabled:bool)🔗
Iftrue, 2D rendering will use a high dynamic range (HDR)RGBA16format framebuffer. Additionally, 2D rendering will be performed on linear values and will be converted using the appropriate transfer function immediately before blitting to the screen (if the Viewport is attached to the screen).
Practically speaking, this means that the end result of the Viewport will not be clamped to the0-1range and can be used in 3D rendering without color encoding adjustments. This allows 2D rendering to take advantage of effects requiring high dynamic range (e.g. 2D glow) as well as substantially improves the appearance of effects requiring highly detailed gradients. This setting has the same effect asViewport.use_hdr_2d.
voidviewport_set_use_occlusion_culling(viewport:RID, enable:bool)🔗
Iftrue, enables occlusion culling on the specified viewport. Equivalent toProjectSettings.rendering/occlusion_culling/use_occlusion_culling.
voidviewport_set_use_taa(viewport:RID, enable:bool)🔗
Iftrue, use temporal antialiasing. Equivalent toProjectSettings.rendering/anti_aliasing/quality/use_taaorViewport.use_taa.
voidviewport_set_use_xr(viewport:RID, use_xr:bool)🔗
Iftrue, the viewport uses augmented or virtual reality technologies. SeeXRInterface.
voidviewport_set_vrs_mode(viewport:RID, mode:ViewportVRSMode)🔗
Sets the Variable Rate Shading (VRS) mode for the viewport. If the GPU does not support VRS, this property is ignored. Equivalent toProjectSettings.rendering/vrs/mode.
voidviewport_set_vrs_texture(viewport:RID, texture:RID)🔗
The texture to use when the VRS mode is set toVIEWPORT_VRS_TEXTURE. Equivalent toProjectSettings.rendering/vrs/texture.
voidviewport_set_vrs_update_mode(viewport:RID, mode:ViewportVRSUpdateMode)🔗
Sets the update mode for Variable Rate Shading (VRS) for the viewport. VRS requires the input texture to be converted to the format usable by the VRS method supported by the hardware. The update mode defines how often this happens. If the GPU does not support VRS, or VRS is not enabled, this property is ignored.
If set toVIEWPORT_VRS_UPDATE_ONCE, the input texture is copied once and the mode is changed toVIEWPORT_VRS_UPDATE_DISABLED.
RIDvisibility_notifier_create()🔗
Creates a new 3D visibility notifier object and adds it to the RenderingServer. It can be accessed with the RID that is returned. This RID will be used in allvisibility_notifier_*RenderingServer functions.
Once finished with your RID, you will want to free the RID using the RenderingServer'sfree_rid()method.
To place in a scene, attach this notifier to an instance usinginstance_set_base()using the returned RID.
Note:The equivalent node isVisibleOnScreenNotifier3D.
voidvisibility_notifier_set_aabb(notifier:RID, aabb:AABB)🔗
There is currently no description for this method. Please help us bycontributing one!
voidvisibility_notifier_set_callbacks(notifier:RID, enter_callable:Callable, exit_callable:Callable)🔗
There is currently no description for this method. Please help us bycontributing one!
voidvoxel_gi_allocate_data(voxel_gi:RID, to_cell_xform:Transform3D, aabb:AABB, octree_size:Vector3i, octree_cells:PackedByteArray, data_cells:PackedByteArray, distance_field:PackedByteArray, level_counts:PackedInt32Array)🔗
There is currently no description for this method. Please help us bycontributing one!
RIDvoxel_gi_create()🔗
Creates a new voxel-based global illumination object and adds it to the RenderingServer. It can be accessed with the RID that is returned. This RID will be used in allvoxel_gi_*RenderingServer functions.
Once finished with your RID, you will want to free the RID using the RenderingServer'sfree_rid()method.
Note:The equivalent node isVoxelGI.
PackedByteArrayvoxel_gi_get_data_cells(voxel_gi:RID)const🔗
There is currently no description for this method. Please help us bycontributing one!
PackedByteArrayvoxel_gi_get_distance_field(voxel_gi:RID)const🔗
There is currently no description for this method. Please help us bycontributing one!
PackedInt32Arrayvoxel_gi_get_level_counts(voxel_gi:RID)const🔗
There is currently no description for this method. Please help us bycontributing one!
PackedByteArrayvoxel_gi_get_octree_cells(voxel_gi:RID)const🔗
There is currently no description for this method. Please help us bycontributing one!
Vector3ivoxel_gi_get_octree_size(voxel_gi:RID)const🔗
There is currently no description for this method. Please help us bycontributing one!
Transform3Dvoxel_gi_get_to_cell_xform(voxel_gi:RID)const🔗
There is currently no description for this method. Please help us bycontributing one!
voidvoxel_gi_set_baked_exposure_normalization(voxel_gi:RID, baked_exposure:float)🔗
Used to inform the renderer what exposure normalization value was used while baking the voxel gi. This value will be used and modulated at run time to ensure that the voxel gi maintains a consistent level of exposure even if the scene-wide exposure normalization is changed at run time. For more information seecamera_attributes_set_exposure().
voidvoxel_gi_set_bias(voxel_gi:RID, bias:float)🔗
Sets theVoxelGIData.biasvalue to use on the specifiedvoxel_gi'sRID.
voidvoxel_gi_set_dynamic_range(voxel_gi:RID, range:float)🔗
Sets theVoxelGIData.dynamic_rangevalue to use on the specifiedvoxel_gi'sRID.
voidvoxel_gi_set_energy(voxel_gi:RID, energy:float)🔗
Sets theVoxelGIData.energyvalue to use on the specifiedvoxel_gi'sRID.
voidvoxel_gi_set_interior(voxel_gi:RID, enable:bool)🔗
Sets theVoxelGIData.interiorvalue to use on the specifiedvoxel_gi'sRID.
voidvoxel_gi_set_normal_bias(voxel_gi:RID, bias:float)🔗
Sets theVoxelGIData.normal_biasvalue to use on the specifiedvoxel_gi'sRID.
voidvoxel_gi_set_propagation(voxel_gi:RID, amount:float)🔗
Sets theVoxelGIData.propagationvalue to use on the specifiedvoxel_gi'sRID.
voidvoxel_gi_set_quality(quality:VoxelGIQuality)🔗
Sets theProjectSettings.rendering/global_illumination/voxel_gi/qualityvalue to use when rendering. This parameter is global and cannot be set on a per-VoxelGI basis.
voidvoxel_gi_set_use_two_bounces(voxel_gi:RID, enable:bool)🔗
Sets theVoxelGIData.use_two_bouncesvalue to use on the specifiedvoxel_gi'sRID.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
