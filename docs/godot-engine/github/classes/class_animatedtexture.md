:github_url: hide



# AnimatedTexture

**Deprecated:** This class does not work properly in current versions and may be removed in the future. There is currently no equivalent workaround.

**Inherits:** [Texture2D<class_Texture2D>] **<** [Texture<class_Texture>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Proxy texture for simple frame-based animations.


## Description

**AnimatedTexture** is a resource format for frame-based animations, where multiple textures can be chained automatically with a predefined delay for each frame. Unlike [AnimationPlayer<class_AnimationPlayer>] or [AnimatedSprite2D<class_AnimatedSprite2D>], it isn't a [Node<class_Node>], but has the advantage of being usable anywhere a [Texture2D<class_Texture2D>] resource can be used, e.g. in a [TileSet<class_TileSet>].

The playback of the animation is controlled by the [speed_scale<class_AnimatedTexture_property_speed_scale>] property, as well as each frame's duration (see [set_frame_duration()<class_AnimatedTexture_method_set_frame_duration>]). The animation loops, i.e. it will restart at frame 0 automatically after playing the last frame.

\ **AnimatedTexture** currently requires all frame textures to have the same size, otherwise the bigger ones will be cropped to match the smallest one.

\ **Note:** AnimatedTexture doesn't support using [AtlasTexture<class_AtlasTexture>]\ s. Each frame needs to be a separate [Texture2D<class_Texture2D>].

\ **Warning:** The current implementation is not efficient for the modern renderers.


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------+--------------------------------------------------------------------+----------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`     | :ref:`current_frame<class_AnimatedTexture_property_current_frame>` |                                                                                        |
> +---------------------------+--------------------------------------------------------------------+----------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`     | :ref:`frames<class_AnimatedTexture_property_frames>`               | ``1``                                                                                  |
> +---------------------------+--------------------------------------------------------------------+----------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`   | :ref:`one_shot<class_AnimatedTexture_property_one_shot>`           | ``false``                                                                              |
> +---------------------------+--------------------------------------------------------------------+----------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`   | :ref:`pause<class_AnimatedTexture_property_pause>`                 | ``false``                                                                              |
> +---------------------------+--------------------------------------------------------------------+----------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`   | resource_local_to_scene                                            | ``false`` (overrides :ref:`Resource<class_Resource_property_resource_local_to_scene>`) |
> +---------------------------+--------------------------------------------------------------------+----------------------------------------------------------------------------------------+
> | :ref:`float<class_float>` | :ref:`speed_scale<class_AnimatedTexture_property_speed_scale>`     | ``1.0``                                                                                |
> +---------------------------+--------------------------------------------------------------------+----------------------------------------------------------------------------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`         | :ref:`get_frame_duration<class_AnimatedTexture_method_get_frame_duration>`\ (\ frame\: :ref:`int<class_int>`\ ) |const|                                    |
> +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Texture2D<class_Texture2D>` | :ref:`get_frame_texture<class_AnimatedTexture_method_get_frame_texture>`\ (\ frame\: :ref:`int<class_int>`\ ) |const|                                      |
> +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                            | :ref:`set_frame_duration<class_AnimatedTexture_method_set_frame_duration>`\ (\ frame\: :ref:`int<class_int>`, duration\: :ref:`float<class_float>`\ )      |
> +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                            | :ref:`set_frame_texture<class_AnimatedTexture_method_set_frame_texture>`\ (\ frame\: :ref:`int<class_int>`, texture\: :ref:`Texture2D<class_Texture2D>`\ ) |
> +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Constants



**MAX_FRAMES** = `256` [🔗<class_AnimatedTexture_constant_MAX_FRAMES>]

The maximum number of frames supported by **AnimatedTexture**. If you need more frames in your animation, use [AnimationPlayer<class_AnimationPlayer>] or [AnimatedSprite2D<class_AnimatedSprite2D>].


----


## Property Descriptions



[int<class_int>] **current_frame** [🔗<class_AnimatedTexture_property_current_frame>]


- |void| **set_current_frame**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_current_frame**\ (\ )

Sets the currently visible frame of the texture. Setting this frame while playing resets the current frame time, so the newly selected frame plays for its whole configured frame duration.


----



[int<class_int>] **frames** = `1` [🔗<class_AnimatedTexture_property_frames>]


- |void| **set_frames**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_frames**\ (\ )

Number of frames to use in the animation. While you can create the frames independently with [set_frame_texture()<class_AnimatedTexture_method_set_frame_texture>], you need to set this value for the animation to take new frames into account. The maximum number of frames is [MAX_FRAMES<class_AnimatedTexture_constant_MAX_FRAMES>].


----



[bool<class_bool>] **one_shot** = `false` [🔗<class_AnimatedTexture_property_one_shot>]


- |void| **set_one_shot**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_one_shot**\ (\ )

If `true`, the animation will only play once and will not loop back to the first frame after reaching the end. Note that reaching the end will not set [pause<class_AnimatedTexture_property_pause>] to `true`.


----



[bool<class_bool>] **pause** = `false` [🔗<class_AnimatedTexture_property_pause>]


- |void| **set_pause**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_pause**\ (\ )

If `true`, the animation will pause where it currently is (i.e. at [current_frame<class_AnimatedTexture_property_current_frame>]). The animation will continue from where it was paused when changing this property to `false`.


----



[float<class_float>] **speed_scale** = `1.0` [🔗<class_AnimatedTexture_property_speed_scale>]


- |void| **set_speed_scale**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_speed_scale**\ (\ )

The animation speed is multiplied by this value. If set to a negative value, the animation is played in reverse.


----


## Method Descriptions



[float<class_float>] **get_frame_duration**\ (\ frame\: [int<class_int>]\ ) |const| [🔗<class_AnimatedTexture_method_get_frame_duration>]

Returns the given `frame`'s duration, in seconds.


----



[Texture2D<class_Texture2D>] **get_frame_texture**\ (\ frame\: [int<class_int>]\ ) |const| [🔗<class_AnimatedTexture_method_get_frame_texture>]

Returns the given frame's [Texture2D<class_Texture2D>].


----



|void| **set_frame_duration**\ (\ frame\: [int<class_int>], duration\: [float<class_float>]\ ) [🔗<class_AnimatedTexture_method_set_frame_duration>]

Sets the duration of any given `frame`. The final duration is affected by the [speed_scale<class_AnimatedTexture_property_speed_scale>]. If set to `0`, the frame is skipped during playback.


----



|void| **set_frame_texture**\ (\ frame\: [int<class_int>], texture\: [Texture2D<class_Texture2D>]\ ) [🔗<class_AnimatedTexture_method_set_frame_texture>]

Assigns a [Texture2D<class_Texture2D>] to the given frame. Frame IDs start at 0, so the first frame has ID 0, and the last frame of the animation has ID [frames<class_AnimatedTexture_property_frames>] - 1.

You can define any number of textures up to [MAX_FRAMES<class_AnimatedTexture_constant_MAX_FRAMES>], but keep in mind that only frames from 0 to [frames<class_AnimatedTexture_property_frames>] - 1 will be part of the animation.

