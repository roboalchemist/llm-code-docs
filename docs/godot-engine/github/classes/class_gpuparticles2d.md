:github_url: hide



# GPUParticles2D

**Inherits:** [Node2D<class_Node2D>] **<** [CanvasItem<class_CanvasItem>] **<** [Node<class_Node>] **<** [Object<class_Object>]

A 2D particle emitter.


## Description

2D particle node used to create a variety of particle systems and effects. **GPUParticles2D** features an emitter that generates some number of particles at a given rate.

Use the [process_material<class_GPUParticles2D_property_process_material>] property to add a [ParticleProcessMaterial<class_ParticleProcessMaterial>] to configure particle appearance and behavior. Alternatively, you can add a [ShaderMaterial<class_ShaderMaterial>] which will be applied to all particles.

2D particles can optionally collide with [LightOccluder2D<class_LightOccluder2D>], but they don't collide with [PhysicsBody2D<class_PhysicsBody2D>] nodes.


## Tutorials

- [../tutorials/2d/particle_systems_2d](Particle systems (2D) .md)

- [2D Particles Demo ](https://godotengine.org/asset-library/asset/2724)_

- [2D Dodge The Creeps Demo (uses GPUParticles2D for the trail behind the player) ](https://godotengine.org/asset-library/asset/2712)_


## Properties

> **TABLE**
> :widths: auto
>
> +-------------------------------------------------+---------------------------------------------------------------------------------------------+---------------------------------+
> | :ref:`int<class_int>`                           | :ref:`amount<class_GPUParticles2D_property_amount>`                                         | ``8``                           |
> +-------------------------------------------------+---------------------------------------------------------------------------------------------+---------------------------------+
> | :ref:`float<class_float>`                       | :ref:`amount_ratio<class_GPUParticles2D_property_amount_ratio>`                             | ``1.0``                         |
> +-------------------------------------------------+---------------------------------------------------------------------------------------------+---------------------------------+
> | :ref:`float<class_float>`                       | :ref:`collision_base_size<class_GPUParticles2D_property_collision_base_size>`               | ``1.0``                         |
> +-------------------------------------------------+---------------------------------------------------------------------------------------------+---------------------------------+
> | :ref:`DrawOrder<enum_GPUParticles2D_DrawOrder>` | :ref:`draw_order<class_GPUParticles2D_property_draw_order>`                                 | ``1``                           |
> +-------------------------------------------------+---------------------------------------------------------------------------------------------+---------------------------------+
> | :ref:`bool<class_bool>`                         | :ref:`emitting<class_GPUParticles2D_property_emitting>`                                     | ``true``                        |
> +-------------------------------------------------+---------------------------------------------------------------------------------------------+---------------------------------+
> | :ref:`float<class_float>`                       | :ref:`explosiveness<class_GPUParticles2D_property_explosiveness>`                           | ``0.0``                         |
> +-------------------------------------------------+---------------------------------------------------------------------------------------------+---------------------------------+
> | :ref:`int<class_int>`                           | :ref:`fixed_fps<class_GPUParticles2D_property_fixed_fps>`                                   | ``30``                          |
> +-------------------------------------------------+---------------------------------------------------------------------------------------------+---------------------------------+
> | :ref:`bool<class_bool>`                         | :ref:`fract_delta<class_GPUParticles2D_property_fract_delta>`                               | ``true``                        |
> +-------------------------------------------------+---------------------------------------------------------------------------------------------+---------------------------------+
> | :ref:`float<class_float>`                       | :ref:`interp_to_end<class_GPUParticles2D_property_interp_to_end>`                           | ``0.0``                         |
> +-------------------------------------------------+---------------------------------------------------------------------------------------------+---------------------------------+
> | :ref:`bool<class_bool>`                         | :ref:`interpolate<class_GPUParticles2D_property_interpolate>`                               | ``true``                        |
> +-------------------------------------------------+---------------------------------------------------------------------------------------------+---------------------------------+
> | :ref:`float<class_float>`                       | :ref:`lifetime<class_GPUParticles2D_property_lifetime>`                                     | ``1.0``                         |
> +-------------------------------------------------+---------------------------------------------------------------------------------------------+---------------------------------+
> | :ref:`bool<class_bool>`                         | :ref:`local_coords<class_GPUParticles2D_property_local_coords>`                             | ``false``                       |
> +-------------------------------------------------+---------------------------------------------------------------------------------------------+---------------------------------+
> | :ref:`bool<class_bool>`                         | :ref:`one_shot<class_GPUParticles2D_property_one_shot>`                                     | ``false``                       |
> +-------------------------------------------------+---------------------------------------------------------------------------------------------+---------------------------------+
> | :ref:`float<class_float>`                       | :ref:`preprocess<class_GPUParticles2D_property_preprocess>`                                 | ``0.0``                         |
> +-------------------------------------------------+---------------------------------------------------------------------------------------------+---------------------------------+
> | :ref:`Material<class_Material>`                 | :ref:`process_material<class_GPUParticles2D_property_process_material>`                     |                                 |
> +-------------------------------------------------+---------------------------------------------------------------------------------------------+---------------------------------+
> | :ref:`float<class_float>`                       | :ref:`randomness<class_GPUParticles2D_property_randomness>`                                 | ``0.0``                         |
> +-------------------------------------------------+---------------------------------------------------------------------------------------------+---------------------------------+
> | :ref:`int<class_int>`                           | :ref:`seed<class_GPUParticles2D_property_seed>`                                             | ``0``                           |
> +-------------------------------------------------+---------------------------------------------------------------------------------------------+---------------------------------+
> | :ref:`float<class_float>`                       | :ref:`speed_scale<class_GPUParticles2D_property_speed_scale>`                               | ``1.0``                         |
> +-------------------------------------------------+---------------------------------------------------------------------------------------------+---------------------------------+
> | :ref:`NodePath<class_NodePath>`                 | :ref:`sub_emitter<class_GPUParticles2D_property_sub_emitter>`                               | ``NodePath("")``                |
> +-------------------------------------------------+---------------------------------------------------------------------------------------------+---------------------------------+
> | :ref:`Texture2D<class_Texture2D>`               | :ref:`texture<class_GPUParticles2D_property_texture>`                                       |                                 |
> +-------------------------------------------------+---------------------------------------------------------------------------------------------+---------------------------------+
> | :ref:`bool<class_bool>`                         | :ref:`trail_enabled<class_GPUParticles2D_property_trail_enabled>`                           | ``false``                       |
> +-------------------------------------------------+---------------------------------------------------------------------------------------------+---------------------------------+
> | :ref:`float<class_float>`                       | :ref:`trail_lifetime<class_GPUParticles2D_property_trail_lifetime>`                         | ``0.3``                         |
> +-------------------------------------------------+---------------------------------------------------------------------------------------------+---------------------------------+
> | :ref:`int<class_int>`                           | :ref:`trail_section_subdivisions<class_GPUParticles2D_property_trail_section_subdivisions>` | ``4``                           |
> +-------------------------------------------------+---------------------------------------------------------------------------------------------+---------------------------------+
> | :ref:`int<class_int>`                           | :ref:`trail_sections<class_GPUParticles2D_property_trail_sections>`                         | ``8``                           |
> +-------------------------------------------------+---------------------------------------------------------------------------------------------+---------------------------------+
> | :ref:`bool<class_bool>`                         | :ref:`use_fixed_seed<class_GPUParticles2D_property_use_fixed_seed>`                         | ``false``                       |
> +-------------------------------------------------+---------------------------------------------------------------------------------------------+---------------------------------+
> | :ref:`Rect2<class_Rect2>`                       | :ref:`visibility_rect<class_GPUParticles2D_property_visibility_rect>`                       | ``Rect2(-100, -100, 200, 200)`` |
> +-------------------------------------------------+---------------------------------------------------------------------------------------------+---------------------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Rect2<class_Rect2>` | :ref:`capture_rect<class_GPUParticles2D_method_capture_rect>`\ (\ ) |const|                                                                                                                                                                                          |
> +---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                    | :ref:`convert_from_particles<class_GPUParticles2D_method_convert_from_particles>`\ (\ particles\: :ref:`Node<class_Node>`\ )                                                                                                                                         |
> +---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                    | :ref:`emit_particle<class_GPUParticles2D_method_emit_particle>`\ (\ xform\: :ref:`Transform2D<class_Transform2D>`, velocity\: :ref:`Vector2<class_Vector2>`, color\: :ref:`Color<class_Color>`, custom\: :ref:`Color<class_Color>`, flags\: :ref:`int<class_int>`\ ) |
> +---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                    | :ref:`request_particles_process<class_GPUParticles2D_method_request_particles_process>`\ (\ process_time\: :ref:`float<class_float>`\ )                                                                                                                              |
> +---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                    | :ref:`restart<class_GPUParticles2D_method_restart>`\ (\ keep_seed\: :ref:`bool<class_bool>` = false\ )                                                                                                                                                               |
> +---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Signals



**finished**\ (\ ) [🔗<class_GPUParticles2D_signal_finished>]

Emitted when all active particles have finished processing. To immediately restart the emission cycle, call [restart()<class_GPUParticles2D_method_restart>].

This signal is never emitted when [one_shot<class_GPUParticles2D_property_one_shot>] is disabled, as particles will be emitted and processed continuously.

\ **Note:** For [one_shot<class_GPUParticles2D_property_one_shot>] emitters, due to the particles being computed on the GPU, there may be a short period after receiving the signal during which setting [emitting<class_GPUParticles2D_property_emitting>] to `true` will not restart the emission cycle. This delay is avoided by instead calling [restart()<class_GPUParticles2D_method_restart>].


----


## Enumerations



enum **DrawOrder**: [🔗<enum_GPUParticles2D_DrawOrder>]



[DrawOrder<enum_GPUParticles2D_DrawOrder>] **DRAW_ORDER_INDEX** = `0`

Particles are drawn in the order emitted.



[DrawOrder<enum_GPUParticles2D_DrawOrder>] **DRAW_ORDER_LIFETIME** = `1`

Particles are drawn in order of remaining lifetime. In other words, the particle with the highest lifetime is drawn at the front.



[DrawOrder<enum_GPUParticles2D_DrawOrder>] **DRAW_ORDER_REVERSE_LIFETIME** = `2`

Particles are drawn in reverse order of remaining lifetime. In other words, the particle with the lowest lifetime is drawn at the front.


----



enum **EmitFlags**: [🔗<enum_GPUParticles2D_EmitFlags>]



[EmitFlags<enum_GPUParticles2D_EmitFlags>] **EMIT_FLAG_POSITION** = `1`

Particle starts at the specified position.



[EmitFlags<enum_GPUParticles2D_EmitFlags>] **EMIT_FLAG_ROTATION_SCALE** = `2`

Particle starts with specified rotation and scale.



[EmitFlags<enum_GPUParticles2D_EmitFlags>] **EMIT_FLAG_VELOCITY** = `4`

Particle starts with the specified velocity vector, which defines the emission direction and speed.



[EmitFlags<enum_GPUParticles2D_EmitFlags>] **EMIT_FLAG_COLOR** = `8`

Particle starts with specified color.



[EmitFlags<enum_GPUParticles2D_EmitFlags>] **EMIT_FLAG_CUSTOM** = `16`

Particle starts with specified `CUSTOM` data.


----


## Property Descriptions



[int<class_int>] **amount** = `8` [🔗<class_GPUParticles2D_property_amount>]


- |void| **set_amount**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_amount**\ (\ )

The number of particles to emit in one emission cycle. The effective emission rate is `(amount * amount_ratio) / lifetime` particles per second. Higher values will increase GPU requirements, even if not all particles are visible at a given time or if [amount_ratio<class_GPUParticles2D_property_amount_ratio>] is decreased.

\ **Note:** Changing this value will cause the particle system to restart. To avoid this, change [amount_ratio<class_GPUParticles2D_property_amount_ratio>] instead.


----



[float<class_float>] **amount_ratio** = `1.0` [🔗<class_GPUParticles2D_property_amount_ratio>]


- |void| **set_amount_ratio**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_amount_ratio**\ (\ )

The ratio of particles that should actually be emitted. If set to a value lower than `1.0`, this will set the amount of emitted particles throughout the lifetime to `amount * amount_ratio`. Unlike changing [amount<class_GPUParticles2D_property_amount>], changing [amount_ratio<class_GPUParticles2D_property_amount_ratio>] while emitting does not affect already-emitted particles and doesn't cause the particle system to restart. [amount_ratio<class_GPUParticles2D_property_amount_ratio>] can be used to create effects that make the number of emitted particles vary over time.

\ **Note:** Reducing the [amount_ratio<class_GPUParticles2D_property_amount_ratio>] has no performance benefit, since resources need to be allocated and processed for the total [amount<class_GPUParticles2D_property_amount>] of particles regardless of the [amount_ratio<class_GPUParticles2D_property_amount_ratio>]. If you don't intend to change the number of particles emitted while the particles are emitting, make sure [amount_ratio<class_GPUParticles2D_property_amount_ratio>] is set to `1` and change [amount<class_GPUParticles2D_property_amount>] to your liking instead.


----



[float<class_float>] **collision_base_size** = `1.0` [🔗<class_GPUParticles2D_property_collision_base_size>]


- |void| **set_collision_base_size**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_collision_base_size**\ (\ )

Multiplier for particle's collision radius. `1.0` corresponds to the size of the sprite. If particles appear to sink into the ground when colliding, increase this value. If particles appear to float when colliding, decrease this value. Only effective if [ParticleProcessMaterial.collision_mode<class_ParticleProcessMaterial_property_collision_mode>] is [ParticleProcessMaterial.COLLISION_RIGID<class_ParticleProcessMaterial_constant_COLLISION_RIGID>] or [ParticleProcessMaterial.COLLISION_HIDE_ON_CONTACT<class_ParticleProcessMaterial_constant_COLLISION_HIDE_ON_CONTACT>].

\ **Note:** Particles always have a spherical collision shape.


----



[DrawOrder<enum_GPUParticles2D_DrawOrder>] **draw_order** = `1` [🔗<class_GPUParticles2D_property_draw_order>]


- |void| **set_draw_order**\ (\ value\: [DrawOrder<enum_GPUParticles2D_DrawOrder>]\ )
- [DrawOrder<enum_GPUParticles2D_DrawOrder>] **get_draw_order**\ (\ )

Particle draw order.


----



[bool<class_bool>] **emitting** = `true` [🔗<class_GPUParticles2D_property_emitting>]


- |void| **set_emitting**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_emitting**\ (\ )

If `true`, particles are being emitted. [emitting<class_GPUParticles2D_property_emitting>] can be used to start and stop particles from emitting. However, if [one_shot<class_GPUParticles2D_property_one_shot>] is `true` setting [emitting<class_GPUParticles2D_property_emitting>] to `true` will not restart the emission cycle unless all active particles have finished processing. Use the [finished<class_GPUParticles2D_signal_finished>] signal to be notified once all active particles finish processing.

\ **Note:** For [one_shot<class_GPUParticles2D_property_one_shot>] emitters, due to the particles being computed on the GPU, there may be a short period after receiving the [finished<class_GPUParticles2D_signal_finished>] signal during which setting this to `true` will not restart the emission cycle.

\ **Tip:** If your [one_shot<class_GPUParticles2D_property_one_shot>] emitter needs to immediately restart emitting particles once [finished<class_GPUParticles2D_signal_finished>] signal is received, consider calling [restart()<class_GPUParticles2D_method_restart>] instead of setting [emitting<class_GPUParticles2D_property_emitting>].


----



[float<class_float>] **explosiveness** = `0.0` [🔗<class_GPUParticles2D_property_explosiveness>]


- |void| **set_explosiveness_ratio**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_explosiveness_ratio**\ (\ )

How rapidly particles in an emission cycle are emitted. If greater than `0`, there will be a gap in emissions before the next cycle begins.


----



[int<class_int>] **fixed_fps** = `30` [🔗<class_GPUParticles2D_property_fixed_fps>]


- |void| **set_fixed_fps**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_fixed_fps**\ (\ )

The particle system's frame rate is fixed to a value. For example, changing the value to 2 will make the particles render at 2 frames per second. Note this does not slow down the simulation of the particle system itself.


----



[bool<class_bool>] **fract_delta** = `true` [🔗<class_GPUParticles2D_property_fract_delta>]


- |void| **set_fractional_delta**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_fractional_delta**\ (\ )

If `true`, results in fractional delta calculation which has a smoother particles display effect.


----



[float<class_float>] **interp_to_end** = `0.0` [🔗<class_GPUParticles2D_property_interp_to_end>]


- |void| **set_interp_to_end**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_interp_to_end**\ (\ )

Causes all the particles in this node to interpolate towards the end of their lifetime.

\ **Note:** This only works when used with a [ParticleProcessMaterial<class_ParticleProcessMaterial>]. It needs to be manually implemented for custom process shaders.


----



[bool<class_bool>] **interpolate** = `true` [🔗<class_GPUParticles2D_property_interpolate>]


- |void| **set_interpolate**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_interpolate**\ (\ )

Enables particle interpolation, which makes the particle movement smoother when their [fixed_fps<class_GPUParticles2D_property_fixed_fps>] is lower than the screen refresh rate.


----



[float<class_float>] **lifetime** = `1.0` [🔗<class_GPUParticles2D_property_lifetime>]


- |void| **set_lifetime**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_lifetime**\ (\ )

The amount of time each particle will exist (in seconds). The effective emission rate is `(amount * amount_ratio) / lifetime` particles per second.


----



[bool<class_bool>] **local_coords** = `false` [🔗<class_GPUParticles2D_property_local_coords>]


- |void| **set_use_local_coordinates**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_use_local_coordinates**\ (\ )

If `true`, particles use the parent node's coordinate space (known as local coordinates). This will cause particles to move and rotate along the **GPUParticles2D** node (and its parents) when it is moved or rotated. If `false`, particles use global coordinates; they will not move or rotate along the **GPUParticles2D** node (and its parents) when it is moved or rotated.


----



[bool<class_bool>] **one_shot** = `false` [🔗<class_GPUParticles2D_property_one_shot>]


- |void| **set_one_shot**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_one_shot**\ (\ )

If `true`, only one emission cycle occurs. If set `true` during a cycle, emission will stop at the cycle's end.


----



[float<class_float>] **preprocess** = `0.0` [🔗<class_GPUParticles2D_property_preprocess>]


- |void| **set_pre_process_time**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_pre_process_time**\ (\ )

Particle system starts as if it had already run for this many seconds.

\ **Note:** This can be very expensive if set to a high number as it requires running the particle shader a number of times equal to the [fixed_fps<class_GPUParticles2D_property_fixed_fps>] (or 30, if [fixed_fps<class_GPUParticles2D_property_fixed_fps>] is 0) for every second. In extreme cases it can even lead to a GPU crash due to the volume of work done in a single frame.


----



[Material<class_Material>] **process_material** [🔗<class_GPUParticles2D_property_process_material>]


- |void| **set_process_material**\ (\ value\: [Material<class_Material>]\ )
- [Material<class_Material>] **get_process_material**\ (\ )

[Material<class_Material>] for processing particles. Can be a [ParticleProcessMaterial<class_ParticleProcessMaterial>] or a [ShaderMaterial<class_ShaderMaterial>].


----



[float<class_float>] **randomness** = `0.0` [🔗<class_GPUParticles2D_property_randomness>]


- |void| **set_randomness_ratio**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_randomness_ratio**\ (\ )

Emission lifetime randomness ratio.


----



[int<class_int>] **seed** = `0` [🔗<class_GPUParticles2D_property_seed>]


- |void| **set_seed**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_seed**\ (\ )

Sets the random seed used by the particle system. Only effective if [use_fixed_seed<class_GPUParticles2D_property_use_fixed_seed>] is `true`.


----



[float<class_float>] **speed_scale** = `1.0` [🔗<class_GPUParticles2D_property_speed_scale>]


- |void| **set_speed_scale**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_speed_scale**\ (\ )

Particle system's running speed scaling ratio. A value of `0` can be used to pause the particles.


----



[NodePath<class_NodePath>] **sub_emitter** = `NodePath("")` [🔗<class_GPUParticles2D_property_sub_emitter>]


- |void| **set_sub_emitter**\ (\ value\: [NodePath<class_NodePath>]\ )
- [NodePath<class_NodePath>] **get_sub_emitter**\ (\ )

Path to another **GPUParticles2D** node that will be used as a subemitter (see [ParticleProcessMaterial.sub_emitter_mode<class_ParticleProcessMaterial_property_sub_emitter_mode>]). Subemitters can be used to achieve effects such as fireworks, sparks on collision, bubbles popping into water drops, and more.

\ **Note:** When [sub_emitter<class_GPUParticles2D_property_sub_emitter>] is set, the target **GPUParticles2D** node will no longer emit particles on its own.


----



[Texture2D<class_Texture2D>] **texture** [🔗<class_GPUParticles2D_property_texture>]


- |void| **set_texture**\ (\ value\: [Texture2D<class_Texture2D>]\ )
- [Texture2D<class_Texture2D>] **get_texture**\ (\ )

Particle texture. If `null`, particles will be squares with a size of 1×1 pixels.

\ **Note:** To use a flipbook texture, assign a new [CanvasItemMaterial<class_CanvasItemMaterial>] to the **GPUParticles2D**'s [CanvasItem.material<class_CanvasItem_property_material>] property, then enable [CanvasItemMaterial.particles_animation<class_CanvasItemMaterial_property_particles_animation>] and set [CanvasItemMaterial.particles_anim_h_frames<class_CanvasItemMaterial_property_particles_anim_h_frames>], [CanvasItemMaterial.particles_anim_v_frames<class_CanvasItemMaterial_property_particles_anim_v_frames>], and [CanvasItemMaterial.particles_anim_loop<class_CanvasItemMaterial_property_particles_anim_loop>] to match the flipbook texture.


----



[bool<class_bool>] **trail_enabled** = `false` [🔗<class_GPUParticles2D_property_trail_enabled>]


- |void| **set_trail_enabled**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_trail_enabled**\ (\ )

If `true`, enables particle trails using a mesh skinning system.

\ **Note:** Unlike [GPUParticles3D<class_GPUParticles3D>], the number of trail sections and subdivisions is set with the [trail_sections<class_GPUParticles2D_property_trail_sections>] and [trail_section_subdivisions<class_GPUParticles2D_property_trail_section_subdivisions>] properties.


----



[float<class_float>] **trail_lifetime** = `0.3` [🔗<class_GPUParticles2D_property_trail_lifetime>]


- |void| **set_trail_lifetime**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_trail_lifetime**\ (\ )

The amount of time the particle's trail should represent (in seconds). Only effective if [trail_enabled<class_GPUParticles2D_property_trail_enabled>] is `true`.


----



[int<class_int>] **trail_section_subdivisions** = `4` [🔗<class_GPUParticles2D_property_trail_section_subdivisions>]


- |void| **set_trail_section_subdivisions**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_trail_section_subdivisions**\ (\ )

The number of subdivisions to use for the particle trail rendering. Higher values can result in smoother trail curves, at the cost of performance due to increased mesh complexity. See also [trail_sections<class_GPUParticles2D_property_trail_sections>]. Only effective if [trail_enabled<class_GPUParticles2D_property_trail_enabled>] is `true`.


----



[int<class_int>] **trail_sections** = `8` [🔗<class_GPUParticles2D_property_trail_sections>]


- |void| **set_trail_sections**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_trail_sections**\ (\ )

The number of sections to use for the particle trail rendering. Higher values can result in smoother trail curves, at the cost of performance due to increased mesh complexity. See also [trail_section_subdivisions<class_GPUParticles2D_property_trail_section_subdivisions>]. Only effective if [trail_enabled<class_GPUParticles2D_property_trail_enabled>] is `true`.


----



[bool<class_bool>] **use_fixed_seed** = `false` [🔗<class_GPUParticles2D_property_use_fixed_seed>]


- |void| **set_use_fixed_seed**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_use_fixed_seed**\ (\ )

If `true`, particles will use the same seed for every simulation using the seed defined in [seed<class_GPUParticles2D_property_seed>]. This is useful for situations where the visual outcome should be consistent across replays, for example when using Movie Maker mode.


----



[Rect2<class_Rect2>] **visibility_rect** = `Rect2(-100, -100, 200, 200)` [🔗<class_GPUParticles2D_property_visibility_rect>]


- |void| **set_visibility_rect**\ (\ value\: [Rect2<class_Rect2>]\ )
- [Rect2<class_Rect2>] **get_visibility_rect**\ (\ )

The [Rect2<class_Rect2>] that determines the node's region which needs to be visible on screen for the particle system to be active.

Grow the rect if particles suddenly appear/disappear when the node enters/exits the screen. The [Rect2<class_Rect2>] can be grown via code or with the **Particles → Generate Visibility Rect** editor tool.


----


## Method Descriptions



[Rect2<class_Rect2>] **capture_rect**\ (\ ) |const| [🔗<class_GPUParticles2D_method_capture_rect>]

Returns a rectangle containing the positions of all existing particles.

\ **Note:** When using threaded rendering this method synchronizes the rendering thread. Calling it often may have a negative impact on performance.


----



|void| **convert_from_particles**\ (\ particles\: [Node<class_Node>]\ ) [🔗<class_GPUParticles2D_method_convert_from_particles>]

Sets this node's properties to match a given [CPUParticles2D<class_CPUParticles2D>] node.


----



|void| **emit_particle**\ (\ xform\: [Transform2D<class_Transform2D>], velocity\: [Vector2<class_Vector2>], color\: [Color<class_Color>], custom\: [Color<class_Color>], flags\: [int<class_int>]\ ) [🔗<class_GPUParticles2D_method_emit_particle>]

Emits a single particle. Whether `xform`, `velocity`, `color` and `custom` are applied depends on the value of `flags`. See [EmitFlags<enum_GPUParticles2D_EmitFlags>].

The default ParticleProcessMaterial will overwrite `color` and use the contents of `custom` as `(rotation, age, animation, lifetime)`.

\ **Note:** [emit_particle()<class_GPUParticles2D_method_emit_particle>] is only supported on the Forward+ and Mobile rendering methods, not Compatibility.


----



|void| **request_particles_process**\ (\ process_time\: [float<class_float>]\ ) [🔗<class_GPUParticles2D_method_request_particles_process>]

Requests the particles to process for extra process time during a single frame.

Useful for particle playback, if used in combination with [use_fixed_seed<class_GPUParticles2D_property_use_fixed_seed>] or by calling [restart()<class_GPUParticles2D_method_restart>] with parameter `keep_seed` set to `true`.


----



|void| **restart**\ (\ keep_seed\: [bool<class_bool>] = false\ ) [🔗<class_GPUParticles2D_method_restart>]

Restarts the particle emission cycle, clearing existing particles. To avoid particles vanishing from the viewport, wait for the [finished<class_GPUParticles2D_signal_finished>] signal before calling.

\ **Note:** The [finished<class_GPUParticles2D_signal_finished>] signal is only emitted by [one_shot<class_GPUParticles2D_property_one_shot>] emitters.

If `keep_seed` is `true`, the current random seed will be preserved. Useful for seeking and playback.

