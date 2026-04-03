:github_url: hide



# SpriteFrames

**Inherits:** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Sprite frame library for AnimatedSprite2D and AnimatedSprite3D.


## Description

Sprite frame library for an [AnimatedSprite2D<class_AnimatedSprite2D>] or [AnimatedSprite3D<class_AnimatedSprite3D>] node. Contains frames and animation data for playback.


## Methods

> **TABLE**
> :widths: auto
>
> +---------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                            | :ref:`add_animation<class_SpriteFrames_method_add_animation>`\ (\ anim\: :ref:`StringName<class_StringName>`\ )                                                                                                                            |
> +---------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                            | :ref:`add_frame<class_SpriteFrames_method_add_frame>`\ (\ anim\: :ref:`StringName<class_StringName>`, texture\: :ref:`Texture2D<class_Texture2D>`, duration\: :ref:`float<class_float>` = 1.0, at_position\: :ref:`int<class_int>` = -1\ ) |
> +---------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                            | :ref:`clear<class_SpriteFrames_method_clear>`\ (\ anim\: :ref:`StringName<class_StringName>`\ )                                                                                                                                            |
> +---------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                            | :ref:`clear_all<class_SpriteFrames_method_clear_all>`\ (\ )                                                                                                                                                                                |
> +---------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                            | :ref:`duplicate_animation<class_SpriteFrames_method_duplicate_animation>`\ (\ anim_from\: :ref:`StringName<class_StringName>`, anim_to\: :ref:`StringName<class_StringName>`\ )                                                            |
> +---------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                           | :ref:`get_animation_loop<class_SpriteFrames_method_get_animation_loop>`\ (\ anim\: :ref:`StringName<class_StringName>`\ ) |const|                                                                                                          |
> +---------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedStringArray<class_PackedStringArray>` | :ref:`get_animation_names<class_SpriteFrames_method_get_animation_names>`\ (\ ) |const|                                                                                                                                                    |
> +---------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`                         | :ref:`get_animation_speed<class_SpriteFrames_method_get_animation_speed>`\ (\ anim\: :ref:`StringName<class_StringName>`\ ) |const|                                                                                                        |
> +---------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                             | :ref:`get_frame_count<class_SpriteFrames_method_get_frame_count>`\ (\ anim\: :ref:`StringName<class_StringName>`\ ) |const|                                                                                                                |
> +---------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`                         | :ref:`get_frame_duration<class_SpriteFrames_method_get_frame_duration>`\ (\ anim\: :ref:`StringName<class_StringName>`, idx\: :ref:`int<class_int>`\ ) |const|                                                                             |
> +---------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Texture2D<class_Texture2D>`                 | :ref:`get_frame_texture<class_SpriteFrames_method_get_frame_texture>`\ (\ anim\: :ref:`StringName<class_StringName>`, idx\: :ref:`int<class_int>`\ ) |const|                                                                               |
> +---------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                           | :ref:`has_animation<class_SpriteFrames_method_has_animation>`\ (\ anim\: :ref:`StringName<class_StringName>`\ ) |const|                                                                                                                    |
> +---------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                            | :ref:`remove_animation<class_SpriteFrames_method_remove_animation>`\ (\ anim\: :ref:`StringName<class_StringName>`\ )                                                                                                                      |
> +---------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                            | :ref:`remove_frame<class_SpriteFrames_method_remove_frame>`\ (\ anim\: :ref:`StringName<class_StringName>`, idx\: :ref:`int<class_int>`\ )                                                                                                 |
> +---------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                            | :ref:`rename_animation<class_SpriteFrames_method_rename_animation>`\ (\ anim\: :ref:`StringName<class_StringName>`, newname\: :ref:`StringName<class_StringName>`\ )                                                                       |
> +---------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                            | :ref:`set_animation_loop<class_SpriteFrames_method_set_animation_loop>`\ (\ anim\: :ref:`StringName<class_StringName>`, loop\: :ref:`bool<class_bool>`\ )                                                                                  |
> +---------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                            | :ref:`set_animation_speed<class_SpriteFrames_method_set_animation_speed>`\ (\ anim\: :ref:`StringName<class_StringName>`, fps\: :ref:`float<class_float>`\ )                                                                               |
> +---------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                            | :ref:`set_frame<class_SpriteFrames_method_set_frame>`\ (\ anim\: :ref:`StringName<class_StringName>`, idx\: :ref:`int<class_int>`, texture\: :ref:`Texture2D<class_Texture2D>`, duration\: :ref:`float<class_float>` = 1.0\ )              |
> +---------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Method Descriptions



|void| **add_animation**\ (\ anim\: [StringName<class_StringName>]\ ) [🔗<class_SpriteFrames_method_add_animation>]

Adds a new `anim` animation to the library.


----



|void| **add_frame**\ (\ anim\: [StringName<class_StringName>], texture\: [Texture2D<class_Texture2D>], duration\: [float<class_float>] = 1.0, at_position\: [int<class_int>] = -1\ ) [🔗<class_SpriteFrames_method_add_frame>]

Adds a frame to the `anim` animation. If `at_position` is `-1`, the frame will be added to the end of the animation. `duration` specifies the relative duration, see [get_frame_duration()<class_SpriteFrames_method_get_frame_duration>] for details.


----



|void| **clear**\ (\ anim\: [StringName<class_StringName>]\ ) [🔗<class_SpriteFrames_method_clear>]

Removes all frames from the `anim` animation.


----



|void| **clear_all**\ (\ ) [🔗<class_SpriteFrames_method_clear_all>]

Removes all animations. An empty `default` animation will be created.


----



|void| **duplicate_animation**\ (\ anim_from\: [StringName<class_StringName>], anim_to\: [StringName<class_StringName>]\ ) [🔗<class_SpriteFrames_method_duplicate_animation>]

Duplicates the animation `anim_from` to a new animation named `anim_to`. Fails if `anim_to` already exists, or if `anim_from` does not exist.


----



[bool<class_bool>] **get_animation_loop**\ (\ anim\: [StringName<class_StringName>]\ ) |const| [🔗<class_SpriteFrames_method_get_animation_loop>]

Returns `true` if the given animation is configured to loop when it finishes playing. Otherwise, returns `false`.


----



[PackedStringArray<class_PackedStringArray>] **get_animation_names**\ (\ ) |const| [🔗<class_SpriteFrames_method_get_animation_names>]

Returns an array containing the names associated to each animation. Values are placed in alphabetical order.


----



[float<class_float>] **get_animation_speed**\ (\ anim\: [StringName<class_StringName>]\ ) |const| [🔗<class_SpriteFrames_method_get_animation_speed>]

Returns the speed in frames per second for the `anim` animation.


----



[int<class_int>] **get_frame_count**\ (\ anim\: [StringName<class_StringName>]\ ) |const| [🔗<class_SpriteFrames_method_get_frame_count>]

Returns the number of frames for the `anim` animation.


----



[float<class_float>] **get_frame_duration**\ (\ anim\: [StringName<class_StringName>], idx\: [int<class_int>]\ ) |const| [🔗<class_SpriteFrames_method_get_frame_duration>]

Returns a relative duration of the frame `idx` in the `anim` animation (defaults to `1.0`). For example, a frame with a duration of `2.0` is displayed twice as long as a frame with a duration of `1.0`. You can calculate the absolute duration (in seconds) of a frame using the following formula:

::

    absolute_duration = relative_duration / (animation_fps * abs(playing_speed))

In this example, `playing_speed` refers to either [AnimatedSprite2D.get_playing_speed()<class_AnimatedSprite2D_method_get_playing_speed>] or [AnimatedSprite3D.get_playing_speed()<class_AnimatedSprite3D_method_get_playing_speed>].


----



[Texture2D<class_Texture2D>] **get_frame_texture**\ (\ anim\: [StringName<class_StringName>], idx\: [int<class_int>]\ ) |const| [🔗<class_SpriteFrames_method_get_frame_texture>]

Returns the texture of the frame `idx` in the `anim` animation.


----



[bool<class_bool>] **has_animation**\ (\ anim\: [StringName<class_StringName>]\ ) |const| [🔗<class_SpriteFrames_method_has_animation>]

Returns `true` if the `anim` animation exists.


----



|void| **remove_animation**\ (\ anim\: [StringName<class_StringName>]\ ) [🔗<class_SpriteFrames_method_remove_animation>]

Removes the `anim` animation.


----



|void| **remove_frame**\ (\ anim\: [StringName<class_StringName>], idx\: [int<class_int>]\ ) [🔗<class_SpriteFrames_method_remove_frame>]

Removes the `anim` animation's frame `idx`.


----



|void| **rename_animation**\ (\ anim\: [StringName<class_StringName>], newname\: [StringName<class_StringName>]\ ) [🔗<class_SpriteFrames_method_rename_animation>]

Changes the `anim` animation's name to `newname`.


----



|void| **set_animation_loop**\ (\ anim\: [StringName<class_StringName>], loop\: [bool<class_bool>]\ ) [🔗<class_SpriteFrames_method_set_animation_loop>]

If `loop` is `true`, the `anim` animation will loop when it reaches the end, or the start if it is played in reverse.


----



|void| **set_animation_speed**\ (\ anim\: [StringName<class_StringName>], fps\: [float<class_float>]\ ) [🔗<class_SpriteFrames_method_set_animation_speed>]

Sets the speed for the `anim` animation in frames per second.


----



|void| **set_frame**\ (\ anim\: [StringName<class_StringName>], idx\: [int<class_int>], texture\: [Texture2D<class_Texture2D>], duration\: [float<class_float>] = 1.0\ ) [🔗<class_SpriteFrames_method_set_frame>]

Sets the `texture` and the `duration` of the frame `idx` in the `anim` animation. `duration` specifies the relative duration, see [get_frame_duration()<class_SpriteFrames_method_get_frame_duration>] for details.

