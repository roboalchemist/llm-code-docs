:github_url: hide



# AnimationNodeOneShot

**Inherits:** [AnimationNodeSync<class_AnimationNodeSync>] **<** [AnimationNode<class_AnimationNode>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Plays an animation once in an [AnimationNodeBlendTree<class_AnimationNodeBlendTree>].


## Description

A resource to add to an [AnimationNodeBlendTree<class_AnimationNodeBlendTree>]. This animation node will execute a sub-animation and return once it finishes. Blend times for fading in and out can be customized, as well as filters.

After setting the request and changing the animation playback, the one-shot node automatically clears the request on the next process frame by setting its `request` value to [ONE_SHOT_REQUEST_NONE<class_AnimationNodeOneShot_constant_ONE_SHOT_REQUEST_NONE>].


> **TABS**
>

    # Play child animation connected to "shot" port.
    animation_tree.set("parameters/OneShot/request", AnimationNodeOneShot.ONE_SHOT_REQUEST_FIRE)
    # Alternative syntax (same result as above).
    animation_tree["parameters/OneShot/request"] = AnimationNodeOneShot.ONE_SHOT_REQUEST_FIRE

    # Abort child animation connected to "shot" port.
    animation_tree.set("parameters/OneShot/request", AnimationNodeOneShot.ONE_SHOT_REQUEST_ABORT)
    # Alternative syntax (same result as above).
    animation_tree["parameters/OneShot/request"] = AnimationNodeOneShot.ONE_SHOT_REQUEST_ABORT

    # Abort child animation with fading out connected to "shot" port.
    animation_tree.set("parameters/OneShot/request", AnimationNodeOneShot.ONE_SHOT_REQUEST_FADE_OUT)
    # Alternative syntax (same result as above).
    animation_tree["parameters/OneShot/request"] = AnimationNodeOneShot.ONE_SHOT_REQUEST_FADE_OUT

    # Get current state (read-only).
    animation_tree.get("parameters/OneShot/active")
    # Alternative syntax (same result as above).
    animation_tree["parameters/OneShot/active"]

    # Get current internal state (read-only).
    animation_tree.get("parameters/OneShot/internal_active")
    # Alternative syntax (same result as above).
    animation_tree["parameters/OneShot/internal_active"]


    // Play child animation connected to "shot" port.
    animationTree.Set("parameters/OneShot/request", (int)AnimationNodeOneShot.OneShotRequest.Fire);

    // Abort child animation connected to "shot" port.
    animationTree.Set("parameters/OneShot/request", (int)AnimationNodeOneShot.OneShotRequest.Abort);

    // Abort child animation with fading out connected to "shot" port.
    animationTree.Set("parameters/OneShot/request", (int)AnimationNodeOneShot.OneShotRequest.FadeOut);

    // Get current state (read-only).
    animationTree.Get("parameters/OneShot/active");

    // Get current internal state (read-only).
    animationTree.Get("parameters/OneShot/internal_active");




## Tutorials

- [../tutorials/animation/animation_tree](Using AnimationTree .md)

- [Third Person Shooter (TPS) Demo ](https://godotengine.org/asset-library/asset/2710)_


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------------------------------+-----------------------------------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>`                           | :ref:`abort_on_reset<class_AnimationNodeOneShot_property_abort_on_reset>`                     | ``false`` |
> +---------------------------------------------------+-----------------------------------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>`                           | :ref:`autorestart<class_AnimationNodeOneShot_property_autorestart>`                           | ``false`` |
> +---------------------------------------------------+-----------------------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>`                         | :ref:`autorestart_delay<class_AnimationNodeOneShot_property_autorestart_delay>`               | ``1.0``   |
> +---------------------------------------------------+-----------------------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>`                         | :ref:`autorestart_random_delay<class_AnimationNodeOneShot_property_autorestart_random_delay>` | ``0.0``   |
> +---------------------------------------------------+-----------------------------------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>`                           | :ref:`break_loop_at_end<class_AnimationNodeOneShot_property_break_loop_at_end>`               | ``false`` |
> +---------------------------------------------------+-----------------------------------------------------------------------------------------------+-----------+
> | :ref:`Curve<class_Curve>`                         | :ref:`fadein_curve<class_AnimationNodeOneShot_property_fadein_curve>`                         |           |
> +---------------------------------------------------+-----------------------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>`                         | :ref:`fadein_time<class_AnimationNodeOneShot_property_fadein_time>`                           | ``0.0``   |
> +---------------------------------------------------+-----------------------------------------------------------------------------------------------+-----------+
> | :ref:`Curve<class_Curve>`                         | :ref:`fadeout_curve<class_AnimationNodeOneShot_property_fadeout_curve>`                       |           |
> +---------------------------------------------------+-----------------------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>`                         | :ref:`fadeout_time<class_AnimationNodeOneShot_property_fadeout_time>`                         | ``0.0``   |
> +---------------------------------------------------+-----------------------------------------------------------------------------------------------+-----------+
> | :ref:`MixMode<enum_AnimationNodeOneShot_MixMode>` | :ref:`mix_mode<class_AnimationNodeOneShot_property_mix_mode>`                                 | ``0``     |
> +---------------------------------------------------+-----------------------------------------------------------------------------------------------+-----------+
>

----


## Enumerations



enum **OneShotRequest**: [🔗<enum_AnimationNodeOneShot_OneShotRequest>]



[OneShotRequest<enum_AnimationNodeOneShot_OneShotRequest>] **ONE_SHOT_REQUEST_NONE** = `0`

The default state of the request. Nothing is done.



[OneShotRequest<enum_AnimationNodeOneShot_OneShotRequest>] **ONE_SHOT_REQUEST_FIRE** = `1`

The request to play the animation connected to "shot" port.



[OneShotRequest<enum_AnimationNodeOneShot_OneShotRequest>] **ONE_SHOT_REQUEST_ABORT** = `2`

The request to stop the animation connected to "shot" port.



[OneShotRequest<enum_AnimationNodeOneShot_OneShotRequest>] **ONE_SHOT_REQUEST_FADE_OUT** = `3`

The request to fade out the animation connected to "shot" port.


----



enum **MixMode**: [🔗<enum_AnimationNodeOneShot_MixMode>]



[MixMode<enum_AnimationNodeOneShot_MixMode>] **MIX_MODE_BLEND** = `0`

Blends two animations. See also [AnimationNodeBlend2<class_AnimationNodeBlend2>].



[MixMode<enum_AnimationNodeOneShot_MixMode>] **MIX_MODE_ADD** = `1`

Blends two animations additively. See also [AnimationNodeAdd2<class_AnimationNodeAdd2>].


----


## Property Descriptions



[bool<class_bool>] **abort_on_reset** = `false` [🔗<class_AnimationNodeOneShot_property_abort_on_reset>]


- |void| **set_abort_on_reset**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_aborted_on_reset**\ (\ )

If `true`, the sub-animation will abort if resumed with a reset after a prior interruption.


----



[bool<class_bool>] **autorestart** = `false` [🔗<class_AnimationNodeOneShot_property_autorestart>]


- |void| **set_autorestart**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **has_autorestart**\ (\ )

If `true`, the sub-animation will restart automatically after finishing.

In other words, to start auto restarting, the animation must be played once with the [ONE_SHOT_REQUEST_FIRE<class_AnimationNodeOneShot_constant_ONE_SHOT_REQUEST_FIRE>] request. The [ONE_SHOT_REQUEST_ABORT<class_AnimationNodeOneShot_constant_ONE_SHOT_REQUEST_ABORT>] request stops the auto restarting, but it does not disable the [autorestart<class_AnimationNodeOneShot_property_autorestart>] itself. So, the [ONE_SHOT_REQUEST_FIRE<class_AnimationNodeOneShot_constant_ONE_SHOT_REQUEST_FIRE>] request will start auto restarting again.


----



[float<class_float>] **autorestart_delay** = `1.0` [🔗<class_AnimationNodeOneShot_property_autorestart_delay>]


- |void| **set_autorestart_delay**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_autorestart_delay**\ (\ )

The delay after which the automatic restart is triggered, in seconds.


----



[float<class_float>] **autorestart_random_delay** = `0.0` [🔗<class_AnimationNodeOneShot_property_autorestart_random_delay>]


- |void| **set_autorestart_random_delay**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_autorestart_random_delay**\ (\ )

If [autorestart<class_AnimationNodeOneShot_property_autorestart>] is `true`, a random additional delay (in seconds) between 0 and this value will be added to [autorestart_delay<class_AnimationNodeOneShot_property_autorestart_delay>].


----



[bool<class_bool>] **break_loop_at_end** = `false` [🔗<class_AnimationNodeOneShot_property_break_loop_at_end>]


- |void| **set_break_loop_at_end**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_loop_broken_at_end**\ (\ )

If `true`, breaks the loop at the end of the loop cycle for transition, even if the animation is looping.


----



[Curve<class_Curve>] **fadein_curve** [🔗<class_AnimationNodeOneShot_property_fadein_curve>]


- |void| **set_fadein_curve**\ (\ value\: [Curve<class_Curve>]\ )
- [Curve<class_Curve>] **get_fadein_curve**\ (\ )

Determines how cross-fading between animations is eased. If empty, the transition will be linear. Should be a unit [Curve<class_Curve>].


----



[float<class_float>] **fadein_time** = `0.0` [🔗<class_AnimationNodeOneShot_property_fadein_time>]


- |void| **set_fadein_time**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_fadein_time**\ (\ )

The fade-in duration. For example, setting this to `1.0` for a 5 second length animation will produce a cross-fade that starts at 0 second and ends at 1 second during the animation.

\ **Note:** **AnimationNodeOneShot** transitions the current state after the fading has finished.


----



[Curve<class_Curve>] **fadeout_curve** [🔗<class_AnimationNodeOneShot_property_fadeout_curve>]


- |void| **set_fadeout_curve**\ (\ value\: [Curve<class_Curve>]\ )
- [Curve<class_Curve>] **get_fadeout_curve**\ (\ )

Determines how cross-fading between animations is eased. If empty, the transition will be linear. Should be a unit [Curve<class_Curve>].


----



[float<class_float>] **fadeout_time** = `0.0` [🔗<class_AnimationNodeOneShot_property_fadeout_time>]


- |void| **set_fadeout_time**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_fadeout_time**\ (\ )

The fade-out duration. For example, setting this to `1.0` for a 5 second length animation will produce a cross-fade that starts at 4 second and ends at 5 second during the animation.

\ **Note:** **AnimationNodeOneShot** transitions the current state after the fading has finished.


----



[MixMode<enum_AnimationNodeOneShot_MixMode>] **mix_mode** = `0` [🔗<class_AnimationNodeOneShot_property_mix_mode>]


- |void| **set_mix_mode**\ (\ value\: [MixMode<enum_AnimationNodeOneShot_MixMode>]\ )
- [MixMode<enum_AnimationNodeOneShot_MixMode>] **get_mix_mode**\ (\ )

The blend type.

