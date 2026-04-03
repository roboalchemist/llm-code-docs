:github_url: hide



# AnimatedSprite2D

**Inherits:** [Node2D<class_Node2D>] **<** [CanvasItem<class_CanvasItem>] **<** [Node<class_Node>] **<** [Object<class_Object>]

Sprite node that contains multiple textures as frames to play for animation.


## Description

**AnimatedSprite2D** is similar to the [Sprite2D<class_Sprite2D>] node, except it carries multiple textures as animation frames. Animations are created using a [SpriteFrames<class_SpriteFrames>] resource, which allows you to import image files (or a folder containing said files) to provide the animation frames for the sprite. The [SpriteFrames<class_SpriteFrames>] resource can be configured in the editor via the SpriteFrames bottom panel.


## Tutorials

- [../tutorials/2d/2d_sprite_animation](2D Sprite animation .md)

- [2D Dodge The Creeps Demo ](https://godotengine.org/asset-library/asset/2712)_


## Properties

> **TABLE**
> :widths: auto
>
> +-----------------------------------------+-----------------------------------------------------------------------+-------------------+
> | :ref:`StringName<class_StringName>`     | :ref:`animation<class_AnimatedSprite2D_property_animation>`           | ``&"default"``    |
> +-----------------------------------------+-----------------------------------------------------------------------+-------------------+
> | :ref:`String<class_String>`             | :ref:`autoplay<class_AnimatedSprite2D_property_autoplay>`             | ``""``            |
> +-----------------------------------------+-----------------------------------------------------------------------+-------------------+
> | :ref:`bool<class_bool>`                 | :ref:`centered<class_AnimatedSprite2D_property_centered>`             | ``true``          |
> +-----------------------------------------+-----------------------------------------------------------------------+-------------------+
> | :ref:`bool<class_bool>`                 | :ref:`flip_h<class_AnimatedSprite2D_property_flip_h>`                 | ``false``         |
> +-----------------------------------------+-----------------------------------------------------------------------+-------------------+
> | :ref:`bool<class_bool>`                 | :ref:`flip_v<class_AnimatedSprite2D_property_flip_v>`                 | ``false``         |
> +-----------------------------------------+-----------------------------------------------------------------------+-------------------+
> | :ref:`int<class_int>`                   | :ref:`frame<class_AnimatedSprite2D_property_frame>`                   | ``0``             |
> +-----------------------------------------+-----------------------------------------------------------------------+-------------------+
> | :ref:`float<class_float>`               | :ref:`frame_progress<class_AnimatedSprite2D_property_frame_progress>` | ``0.0``           |
> +-----------------------------------------+-----------------------------------------------------------------------+-------------------+
> | :ref:`Vector2<class_Vector2>`           | :ref:`offset<class_AnimatedSprite2D_property_offset>`                 | ``Vector2(0, 0)`` |
> +-----------------------------------------+-----------------------------------------------------------------------+-------------------+
> | :ref:`float<class_float>`               | :ref:`speed_scale<class_AnimatedSprite2D_property_speed_scale>`       | ``1.0``           |
> +-----------------------------------------+-----------------------------------------------------------------------+-------------------+
> | :ref:`SpriteFrames<class_SpriteFrames>` | :ref:`sprite_frames<class_AnimatedSprite2D_property_sprite_frames>`   |                   |
> +-----------------------------------------+-----------------------------------------------------------------------+-------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +---------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>` | :ref:`get_playing_speed<class_AnimatedSprite2D_method_get_playing_speed>`\ (\ ) |const|                                                                                                             |
> +---------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`   | :ref:`is_playing<class_AnimatedSprite2D_method_is_playing>`\ (\ ) |const|                                                                                                                           |
> +---------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                    | :ref:`pause<class_AnimatedSprite2D_method_pause>`\ (\ )                                                                                                                                             |
> +---------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                    | :ref:`play<class_AnimatedSprite2D_method_play>`\ (\ name\: :ref:`StringName<class_StringName>` = &"", custom_speed\: :ref:`float<class_float>` = 1.0, from_end\: :ref:`bool<class_bool>` = false\ ) |
> +---------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                    | :ref:`play_backwards<class_AnimatedSprite2D_method_play_backwards>`\ (\ name\: :ref:`StringName<class_StringName>` = &""\ )                                                                         |
> +---------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                    | :ref:`set_frame_and_progress<class_AnimatedSprite2D_method_set_frame_and_progress>`\ (\ frame\: :ref:`int<class_int>`, progress\: :ref:`float<class_float>`\ )                                      |
> +---------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                    | :ref:`stop<class_AnimatedSprite2D_method_stop>`\ (\ )                                                                                                                                               |
> +---------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Signals



**animation_changed**\ (\ ) [🔗<class_AnimatedSprite2D_signal_animation_changed>]

Emitted when [animation<class_AnimatedSprite2D_property_animation>] changes.


----



**animation_finished**\ (\ ) [🔗<class_AnimatedSprite2D_signal_animation_finished>]

Emitted when the animation reaches the end, or the start if it is played in reverse. When the animation finishes, it pauses the playback.

\ **Note:** This signal is not emitted if an animation is looping.


----



**animation_looped**\ (\ ) [🔗<class_AnimatedSprite2D_signal_animation_looped>]

Emitted when the animation loops.


----



**frame_changed**\ (\ ) [🔗<class_AnimatedSprite2D_signal_frame_changed>]

Emitted when [frame<class_AnimatedSprite2D_property_frame>] changes.


----



**sprite_frames_changed**\ (\ ) [🔗<class_AnimatedSprite2D_signal_sprite_frames_changed>]

Emitted when [sprite_frames<class_AnimatedSprite2D_property_sprite_frames>] changes.


----


## Property Descriptions



[StringName<class_StringName>] **animation** = `&"default"` [🔗<class_AnimatedSprite2D_property_animation>]


- |void| **set_animation**\ (\ value\: [StringName<class_StringName>]\ )
- [StringName<class_StringName>] **get_animation**\ (\ )

The current animation from the [sprite_frames<class_AnimatedSprite2D_property_sprite_frames>] resource. If this value is changed, the [frame<class_AnimatedSprite2D_property_frame>] counter and the [frame_progress<class_AnimatedSprite2D_property_frame_progress>] are reset.


----



[String<class_String>] **autoplay** = `""` [🔗<class_AnimatedSprite2D_property_autoplay>]


- |void| **set_autoplay**\ (\ value\: [String<class_String>]\ )
- [String<class_String>] **get_autoplay**\ (\ )

The key of the animation to play when the scene loads.


----



[bool<class_bool>] **centered** = `true` [🔗<class_AnimatedSprite2D_property_centered>]


- |void| **set_centered**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_centered**\ (\ )

If `true`, texture will be centered.

\ **Note:** For games with a pixel art aesthetic, textures may appear deformed when centered. This is caused by their position being between pixels. To prevent this, set this property to `false`, or consider enabling [ProjectSettings.rendering/2d/snap/snap_2d_vertices_to_pixel<class_ProjectSettings_property_rendering/2d/snap/snap_2d_vertices_to_pixel>] and [ProjectSettings.rendering/2d/snap/snap_2d_transforms_to_pixel<class_ProjectSettings_property_rendering/2d/snap/snap_2d_transforms_to_pixel>].


----



[bool<class_bool>] **flip_h** = `false` [🔗<class_AnimatedSprite2D_property_flip_h>]


- |void| **set_flip_h**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_flipped_h**\ (\ )

If `true`, texture is flipped horizontally.


----



[bool<class_bool>] **flip_v** = `false` [🔗<class_AnimatedSprite2D_property_flip_v>]


- |void| **set_flip_v**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_flipped_v**\ (\ )

If `true`, texture is flipped vertically.


----



[int<class_int>] **frame** = `0` [🔗<class_AnimatedSprite2D_property_frame>]


- |void| **set_frame**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_frame**\ (\ )

The displayed animation frame's index. Setting this property also resets [frame_progress<class_AnimatedSprite2D_property_frame_progress>]. If this is not desired, use [set_frame_and_progress()<class_AnimatedSprite2D_method_set_frame_and_progress>].


----



[float<class_float>] **frame_progress** = `0.0` [🔗<class_AnimatedSprite2D_property_frame_progress>]


- |void| **set_frame_progress**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_frame_progress**\ (\ )

The progress value between `0.0` and `1.0` until the current frame transitions to the next frame. If the animation is playing backwards, the value transitions from `1.0` to `0.0`.


----



[Vector2<class_Vector2>] **offset** = `Vector2(0, 0)` [🔗<class_AnimatedSprite2D_property_offset>]


- |void| **set_offset**\ (\ value\: [Vector2<class_Vector2>]\ )
- [Vector2<class_Vector2>] **get_offset**\ (\ )

The texture's drawing offset.


----



[float<class_float>] **speed_scale** = `1.0` [🔗<class_AnimatedSprite2D_property_speed_scale>]


- |void| **set_speed_scale**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_speed_scale**\ (\ )

The speed scaling ratio. For example, if this value is `1`, then the animation plays at normal speed. If it's `0.5`, then it plays at half speed. If it's `2`, then it plays at double speed.

If set to a negative value, the animation is played in reverse. If set to `0`, the animation will not advance.


----



[SpriteFrames<class_SpriteFrames>] **sprite_frames** [🔗<class_AnimatedSprite2D_property_sprite_frames>]


- |void| **set_sprite_frames**\ (\ value\: [SpriteFrames<class_SpriteFrames>]\ )
- [SpriteFrames<class_SpriteFrames>] **get_sprite_frames**\ (\ )

The [SpriteFrames<class_SpriteFrames>] resource containing the animation(s). Allows you the option to load, edit, clear, make unique and save the states of the [SpriteFrames<class_SpriteFrames>] resource.


----


## Method Descriptions



[float<class_float>] **get_playing_speed**\ (\ ) |const| [🔗<class_AnimatedSprite2D_method_get_playing_speed>]

Returns the actual playing speed of current animation or `0` if not playing. This speed is the [speed_scale<class_AnimatedSprite2D_property_speed_scale>] property multiplied by `custom_speed` argument specified when calling the [play()<class_AnimatedSprite2D_method_play>] method.

Returns a negative value if the current animation is playing backwards.


----



[bool<class_bool>] **is_playing**\ (\ ) |const| [🔗<class_AnimatedSprite2D_method_is_playing>]

Returns `true` if an animation is currently playing (even if [speed_scale<class_AnimatedSprite2D_property_speed_scale>] and/or `custom_speed` are `0`).


----



|void| **pause**\ (\ ) [🔗<class_AnimatedSprite2D_method_pause>]

Pauses the currently playing animation. The [frame<class_AnimatedSprite2D_property_frame>] and [frame_progress<class_AnimatedSprite2D_property_frame_progress>] will be kept and calling [play()<class_AnimatedSprite2D_method_play>] or [play_backwards()<class_AnimatedSprite2D_method_play_backwards>] without arguments will resume the animation from the current playback position.

See also [stop()<class_AnimatedSprite2D_method_stop>].


----



|void| **play**\ (\ name\: [StringName<class_StringName>] = &"", custom_speed\: [float<class_float>] = 1.0, from_end\: [bool<class_bool>] = false\ ) [🔗<class_AnimatedSprite2D_method_play>]

Plays the animation with key `name`. If `custom_speed` is negative and `from_end` is `true`, the animation will play backwards (which is equivalent to calling [play_backwards()<class_AnimatedSprite2D_method_play_backwards>]).

If this method is called with that same animation `name`, or with no `name` parameter, the assigned animation will resume playing if it was paused.


----



|void| **play_backwards**\ (\ name\: [StringName<class_StringName>] = &""\ ) [🔗<class_AnimatedSprite2D_method_play_backwards>]

Plays the animation with key `name` in reverse.

This method is a shorthand for [play()<class_AnimatedSprite2D_method_play>] with `custom_speed = -1.0` and `from_end = true`, so see its description for more information.


----



|void| **set_frame_and_progress**\ (\ frame\: [int<class_int>], progress\: [float<class_float>]\ ) [🔗<class_AnimatedSprite2D_method_set_frame_and_progress>]

Sets [frame<class_AnimatedSprite2D_property_frame>] and [frame_progress<class_AnimatedSprite2D_property_frame_progress>] to the given values. Unlike setting [frame<class_AnimatedSprite2D_property_frame>], this method does not reset the [frame_progress<class_AnimatedSprite2D_property_frame_progress>] to `0.0` implicitly.

\ **Example:** Change the animation while keeping the same [frame<class_AnimatedSprite2D_property_frame>] and [frame_progress<class_AnimatedSprite2D_property_frame_progress>]:


> **TABS**
>

    var current_frame = animated_sprite.get_frame()
    var current_progress = animated_sprite.get_frame_progress()
    animated_sprite.play("walk_another_skin")
    animated_sprite.set_frame_and_progress(current_frame, current_progress)




----



|void| **stop**\ (\ ) [🔗<class_AnimatedSprite2D_method_stop>]

Stops the currently playing animation. The animation position is reset to `0` and the `custom_speed` is reset to `1.0`. See also [pause()<class_AnimatedSprite2D_method_pause>].

