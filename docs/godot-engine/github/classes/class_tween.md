:github_url: hide



# Tween

**Inherits:** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Lightweight object used for general-purpose animation via script, using [Tweener<class_Tweener>]\ s.


## Description

Tweens are mostly useful for animations requiring a numerical property to be interpolated over a range of values. The name *tween* comes from *in-betweening*, an animation technique where you specify *keyframes* and the computer interpolates the frames that appear between them. Animating something with a **Tween** is called tweening.

\ **Tween** is more suited than [AnimationPlayer<class_AnimationPlayer>] for animations where you don't know the final values in advance. For example, interpolating a dynamically-chosen camera zoom value is best done with a **Tween**; it would be difficult to do the same thing with an [AnimationPlayer<class_AnimationPlayer>] node. Tweens are also more light-weight than [AnimationPlayer<class_AnimationPlayer>], so they are very much suited for simple animations or general tasks that don't require visual tweaking provided by the editor. They can be used in a "fire-and-forget" manner for some logic that normally would be done by code. You can e.g. make something shoot periodically by using a looped [CallbackTweener<class_CallbackTweener>] with a delay.

A **Tween** can be created by using either [SceneTree.create_tween()<class_SceneTree_method_create_tween>] or [Node.create_tween()<class_Node_method_create_tween>]. **Tween**\ s created manually (i.e. by using `Tween.new()`) are invalid and can't be used for tweening values.

A tween animation is created by adding [Tweener<class_Tweener>]\ s to the **Tween** object, using [tween_property()<class_Tween_method_tween_property>], [tween_interval()<class_Tween_method_tween_interval>], [tween_callback()<class_Tween_method_tween_callback>] or [tween_method()<class_Tween_method_tween_method>]:


> **TABS**
>

    var tween = get_tree().create_tween()
    tween.tween_property($Sprite, "modulate", Color.RED, 1.0)
    tween.tween_property($Sprite, "scale", Vector2(), 1.0)
    tween.tween_callback($Sprite.queue_free)


    Tween tween = GetTree().CreateTween();
    tween.TweenProperty(GetNode("Sprite"), "modulate", Colors.Red, 1.0f);
    tween.TweenProperty(GetNode("Sprite"), "scale", Vector2.Zero, 1.0f);
    tween.TweenCallback(Callable.From(GetNode("Sprite").QueueFree));



This sequence will make the `$Sprite` node turn red, then shrink, before finally calling [Node.queue_free()<class_Node_method_queue_free>] to free the sprite. [Tweener<class_Tweener>]\ s are executed one after another by default. This behavior can be changed using [parallel()<class_Tween_method_parallel>] and [set_parallel()<class_Tween_method_set_parallel>].

When a [Tweener<class_Tweener>] is created with one of the `tween_*` methods, a chained method call can be used to tweak the properties of this [Tweener<class_Tweener>]. For example, if you want to set a different transition type in the above example, you can use [set_trans()<class_Tween_method_set_trans>]:


> **TABS**
>

    var tween = get_tree().create_tween()
    tween.tween_property($Sprite, "modulate", Color.RED, 1.0).set_trans(Tween.TRANS_SINE)
    tween.tween_property($Sprite, "scale", Vector2(), 1.0).set_trans(Tween.TRANS_BOUNCE)
    tween.tween_callback($Sprite.queue_free)


    Tween tween = GetTree().CreateTween();
    tween.TweenProperty(GetNode("Sprite"), "modulate", Colors.Red, 1.0f).SetTrans(Tween.TransitionType.Sine);
    tween.TweenProperty(GetNode("Sprite"), "scale", Vector2.Zero, 1.0f).SetTrans(Tween.TransitionType.Bounce);
    tween.TweenCallback(Callable.From(GetNode("Sprite").QueueFree));



Most of the **Tween** methods can be chained this way too. In the following example the **Tween** is bound to the running script's node and a default transition is set for its [Tweener<class_Tweener>]\ s:


> **TABS**
>

    var tween = get_tree().create_tween().bind_node(self).set_trans(Tween.TRANS_ELASTIC)
    tween.tween_property($Sprite, "modulate", Color.RED, 1.0)
    tween.tween_property($Sprite, "scale", Vector2(), 1.0)
    tween.tween_callback($Sprite.queue_free)


    var tween = GetTree().CreateTween().BindNode(this).SetTrans(Tween.TransitionType.Elastic);
    tween.TweenProperty(GetNode("Sprite"), "modulate", Colors.Red, 1.0f);
    tween.TweenProperty(GetNode("Sprite"), "scale", Vector2.Zero, 1.0f);
    tween.TweenCallback(Callable.From(GetNode("Sprite").QueueFree));



Another interesting use for **Tween**\ s is animating arbitrary sets of objects:


> **TABS**
>

    var tween = create_tween()
    for sprite in get_children():
        tween.tween_property(sprite, "position", Vector2(0, 0), 1.0)


    Tween tween = CreateTween();
    foreach (Node sprite in GetChildren())
        tween.TweenProperty(sprite, "position", Vector2.Zero, 1.0f);



In the example above, all children of a node are moved one after another to position `(0, 0)`.

You should avoid using more than one **Tween** per object's property. If two or more tweens animate one property at the same time, the last one created will take priority and assign the final value. If you want to interrupt and restart an animation, consider assigning the **Tween** to a variable:


> **TABS**
>

    var tween
    func animate():
        if tween:
            tween.kill() # Abort the previous animation.
        tween = create_tween()


    private Tween _tween;

    public void Animate()
    {
        if (_tween != null)
            _tween.Kill(); // Abort the previous animation
        _tween = CreateTween();
    }



Some [Tweener<class_Tweener>]\ s use transitions and eases. The first accepts a [TransitionType<enum_Tween_TransitionType>] constant, and refers to the way the timing of the animation is handled (see [easings.net ](https://easings.net/)_ for some examples). The second accepts an [EaseType<enum_Tween_EaseType>] constant, and controls where the `trans_type` is applied to the interpolation (in the beginning, the end, or both). If you don't know which transition and easing to pick, you can try different [TransitionType<enum_Tween_TransitionType>] constants with [EASE_IN_OUT<class_Tween_constant_EASE_IN_OUT>], and use the one that looks best.

\ [Tween easing and transition types cheatsheet ](https://raw.githubusercontent.com/godotengine/godot-docs/master/img/tween_cheatsheet.webp)_\ 

\ **Note:** Tweens are not designed to be reused and trying to do so results in an undefined behavior. Create a new Tween for each animation and every time you replay an animation from start. Keep in mind that Tweens start immediately, so only create a Tween when you want to start animating.

\ **Note:** The tween is processed after all of the nodes in the current frame, i.e. node's [Node._process()<class_Node_private_method__process>] method would be called before the tween (or [Node._physics_process()<class_Node_private_method__physics_process>] depending on the value passed to [set_process_mode()<class_Tween_method_set_process_mode>]).


## Methods

> **TABLE**
> :widths: auto
>
> +-----------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Tween<class_Tween>`                     | :ref:`bind_node<class_Tween_method_bind_node>`\ (\ node\: :ref:`Node<class_Node>`\ )                                                                                                                                                                                                                                                                                       |
> +-----------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Tween<class_Tween>`                     | :ref:`chain<class_Tween_method_chain>`\ (\ )                                                                                                                                                                                                                                                                                                                               |
> +-----------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                       | :ref:`custom_step<class_Tween_method_custom_step>`\ (\ delta\: :ref:`float<class_float>`\ )                                                                                                                                                                                                                                                                                |
> +-----------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                         | :ref:`get_loops_left<class_Tween_method_get_loops_left>`\ (\ ) |const|                                                                                                                                                                                                                                                                                                     |
> +-----------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`                     | :ref:`get_total_elapsed_time<class_Tween_method_get_total_elapsed_time>`\ (\ ) |const|                                                                                                                                                                                                                                                                                     |
> +-----------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Variant<class_Variant>`                 | :ref:`interpolate_value<class_Tween_method_interpolate_value>`\ (\ initial_value\: :ref:`Variant<class_Variant>`, delta_value\: :ref:`Variant<class_Variant>`, elapsed_time\: :ref:`float<class_float>`, duration\: :ref:`float<class_float>`, trans_type\: :ref:`TransitionType<enum_Tween_TransitionType>`, ease_type\: :ref:`EaseType<enum_Tween_EaseType>`\ ) |static| |
> +-----------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                       | :ref:`is_running<class_Tween_method_is_running>`\ (\ )                                                                                                                                                                                                                                                                                                                     |
> +-----------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                       | :ref:`is_valid<class_Tween_method_is_valid>`\ (\ )                                                                                                                                                                                                                                                                                                                         |
> +-----------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                        | :ref:`kill<class_Tween_method_kill>`\ (\ )                                                                                                                                                                                                                                                                                                                                 |
> +-----------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Tween<class_Tween>`                     | :ref:`parallel<class_Tween_method_parallel>`\ (\ )                                                                                                                                                                                                                                                                                                                         |
> +-----------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                        | :ref:`pause<class_Tween_method_pause>`\ (\ )                                                                                                                                                                                                                                                                                                                               |
> +-----------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                        | :ref:`play<class_Tween_method_play>`\ (\ )                                                                                                                                                                                                                                                                                                                                 |
> +-----------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Tween<class_Tween>`                     | :ref:`set_ease<class_Tween_method_set_ease>`\ (\ ease\: :ref:`EaseType<enum_Tween_EaseType>`\ )                                                                                                                                                                                                                                                                            |
> +-----------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Tween<class_Tween>`                     | :ref:`set_ignore_time_scale<class_Tween_method_set_ignore_time_scale>`\ (\ ignore\: :ref:`bool<class_bool>` = true\ )                                                                                                                                                                                                                                                      |
> +-----------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Tween<class_Tween>`                     | :ref:`set_loops<class_Tween_method_set_loops>`\ (\ loops\: :ref:`int<class_int>` = 0\ )                                                                                                                                                                                                                                                                                    |
> +-----------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Tween<class_Tween>`                     | :ref:`set_parallel<class_Tween_method_set_parallel>`\ (\ parallel\: :ref:`bool<class_bool>` = true\ )                                                                                                                                                                                                                                                                      |
> +-----------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Tween<class_Tween>`                     | :ref:`set_pause_mode<class_Tween_method_set_pause_mode>`\ (\ mode\: :ref:`TweenPauseMode<enum_Tween_TweenPauseMode>`\ )                                                                                                                                                                                                                                                    |
> +-----------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Tween<class_Tween>`                     | :ref:`set_process_mode<class_Tween_method_set_process_mode>`\ (\ mode\: :ref:`TweenProcessMode<enum_Tween_TweenProcessMode>`\ )                                                                                                                                                                                                                                            |
> +-----------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Tween<class_Tween>`                     | :ref:`set_speed_scale<class_Tween_method_set_speed_scale>`\ (\ speed\: :ref:`float<class_float>`\ )                                                                                                                                                                                                                                                                        |
> +-----------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Tween<class_Tween>`                     | :ref:`set_trans<class_Tween_method_set_trans>`\ (\ trans\: :ref:`TransitionType<enum_Tween_TransitionType>`\ )                                                                                                                                                                                                                                                             |
> +-----------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                        | :ref:`stop<class_Tween_method_stop>`\ (\ )                                                                                                                                                                                                                                                                                                                                 |
> +-----------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`CallbackTweener<class_CallbackTweener>` | :ref:`tween_callback<class_Tween_method_tween_callback>`\ (\ callback\: :ref:`Callable<class_Callable>`\ )                                                                                                                                                                                                                                                                 |
> +-----------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`IntervalTweener<class_IntervalTweener>` | :ref:`tween_interval<class_Tween_method_tween_interval>`\ (\ time\: :ref:`float<class_float>`\ )                                                                                                                                                                                                                                                                           |
> +-----------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`MethodTweener<class_MethodTweener>`     | :ref:`tween_method<class_Tween_method_tween_method>`\ (\ method\: :ref:`Callable<class_Callable>`, from\: :ref:`Variant<class_Variant>`, to\: :ref:`Variant<class_Variant>`, duration\: :ref:`float<class_float>`\ )                                                                                                                                                       |
> +-----------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PropertyTweener<class_PropertyTweener>` | :ref:`tween_property<class_Tween_method_tween_property>`\ (\ object\: :ref:`Object<class_Object>`, property\: :ref:`NodePath<class_NodePath>`, final_val\: :ref:`Variant<class_Variant>`, duration\: :ref:`float<class_float>`\ )                                                                                                                                          |
> +-----------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`SubtweenTweener<class_SubtweenTweener>` | :ref:`tween_subtween<class_Tween_method_tween_subtween>`\ (\ subtween\: :ref:`Tween<class_Tween>`\ )                                                                                                                                                                                                                                                                       |
> +-----------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Signals



**finished**\ (\ ) [🔗<class_Tween_signal_finished>]

Emitted when the **Tween** has finished all tweening. Never emitted when the **Tween** is set to infinite looping (see [set_loops()<class_Tween_method_set_loops>]).


----



**loop_finished**\ (\ loop_count\: [int<class_int>]\ ) [🔗<class_Tween_signal_loop_finished>]

Emitted when a full loop is complete (see [set_loops()<class_Tween_method_set_loops>]), providing the loop index. This signal is not emitted after the final loop, use [finished<class_Tween_signal_finished>] instead for this case.


----



**step_finished**\ (\ idx\: [int<class_int>]\ ) [🔗<class_Tween_signal_step_finished>]

Emitted when one step of the **Tween** is complete, providing the step index. One step is either a single [Tweener<class_Tweener>] or a group of [Tweener<class_Tweener>]\ s running in parallel.


----


## Enumerations



enum **TweenProcessMode**: [🔗<enum_Tween_TweenProcessMode>]



[TweenProcessMode<enum_Tween_TweenProcessMode>] **TWEEN_PROCESS_PHYSICS** = `0`

The **Tween** updates after each physics frame (see [Node._physics_process()<class_Node_private_method__physics_process>]).



[TweenProcessMode<enum_Tween_TweenProcessMode>] **TWEEN_PROCESS_IDLE** = `1`

The **Tween** updates after each process frame (see [Node._process()<class_Node_private_method__process>]).


----



enum **TweenPauseMode**: [🔗<enum_Tween_TweenPauseMode>]



[TweenPauseMode<enum_Tween_TweenPauseMode>] **TWEEN_PAUSE_BOUND** = `0`

If the **Tween** has a bound node, it will process when that node can process (see [Node.process_mode<class_Node_property_process_mode>]). Otherwise it's the same as [TWEEN_PAUSE_STOP<class_Tween_constant_TWEEN_PAUSE_STOP>].



[TweenPauseMode<enum_Tween_TweenPauseMode>] **TWEEN_PAUSE_STOP** = `1`

If [SceneTree<class_SceneTree>] is paused, the **Tween** will also pause.



[TweenPauseMode<enum_Tween_TweenPauseMode>] **TWEEN_PAUSE_PROCESS** = `2`

The **Tween** will process regardless of whether [SceneTree<class_SceneTree>] is paused.


----



enum **TransitionType**: [🔗<enum_Tween_TransitionType>]



[TransitionType<enum_Tween_TransitionType>] **TRANS_LINEAR** = `0`

The animation is interpolated linearly.



[TransitionType<enum_Tween_TransitionType>] **TRANS_SINE** = `1`

The animation is interpolated using a sine function.



[TransitionType<enum_Tween_TransitionType>] **TRANS_QUINT** = `2`

The animation is interpolated with a quintic (to the power of 5) function.



[TransitionType<enum_Tween_TransitionType>] **TRANS_QUART** = `3`

The animation is interpolated with a quartic (to the power of 4) function.



[TransitionType<enum_Tween_TransitionType>] **TRANS_QUAD** = `4`

The animation is interpolated with a quadratic (to the power of 2) function.



[TransitionType<enum_Tween_TransitionType>] **TRANS_EXPO** = `5`

The animation is interpolated with an exponential (to the power of x) function.



[TransitionType<enum_Tween_TransitionType>] **TRANS_ELASTIC** = `6`

The animation is interpolated with elasticity, wiggling around the edges.



[TransitionType<enum_Tween_TransitionType>] **TRANS_CUBIC** = `7`

The animation is interpolated with a cubic (to the power of 3) function.



[TransitionType<enum_Tween_TransitionType>] **TRANS_CIRC** = `8`

The animation is interpolated with a function using square roots.



[TransitionType<enum_Tween_TransitionType>] **TRANS_BOUNCE** = `9`

The animation is interpolated by bouncing at the end.



[TransitionType<enum_Tween_TransitionType>] **TRANS_BACK** = `10`

The animation is interpolated backing out at ends.



[TransitionType<enum_Tween_TransitionType>] **TRANS_SPRING** = `11`

The animation is interpolated like a spring towards the end.


----



enum **EaseType**: [🔗<enum_Tween_EaseType>]



[EaseType<enum_Tween_EaseType>] **EASE_IN** = `0`

The interpolation starts slowly and speeds up towards the end.



[EaseType<enum_Tween_EaseType>] **EASE_OUT** = `1`

The interpolation starts quickly and slows down towards the end.



[EaseType<enum_Tween_EaseType>] **EASE_IN_OUT** = `2`

A combination of [EASE_IN<class_Tween_constant_EASE_IN>] and [EASE_OUT<class_Tween_constant_EASE_OUT>]. The interpolation is slowest at both ends.



[EaseType<enum_Tween_EaseType>] **EASE_OUT_IN** = `3`

A combination of [EASE_IN<class_Tween_constant_EASE_IN>] and [EASE_OUT<class_Tween_constant_EASE_OUT>]. The interpolation is fastest at both ends.


----


## Method Descriptions



[Tween<class_Tween>] **bind_node**\ (\ node\: [Node<class_Node>]\ ) [🔗<class_Tween_method_bind_node>]

Binds this **Tween** with the given `node`. **Tween**\ s are processed directly by the [SceneTree<class_SceneTree>], so they run independently of the animated nodes. When you bind a [Node<class_Node>] with the **Tween**, the **Tween** will halt the animation when the object is not inside tree and the **Tween** will be automatically killed when the bound object is freed. Also [TWEEN_PAUSE_BOUND<class_Tween_constant_TWEEN_PAUSE_BOUND>] will make the pausing behavior dependent on the bound node.

For a shorter way to create and bind a **Tween**, you can use [Node.create_tween()<class_Node_method_create_tween>].


----



[Tween<class_Tween>] **chain**\ (\ ) [🔗<class_Tween_method_chain>]

Used to chain two [Tweener<class_Tweener>]\ s after [set_parallel()<class_Tween_method_set_parallel>] is called with `true`.


> **TABS**
>

    var tween = create_tween().set_parallel(true)
    tween.tween_property(...)
    tween.tween_property(...) # Will run parallelly with above.
    tween.chain().tween_property(...) # Will run after two above are finished.


    Tween tween = CreateTween().SetParallel(true);
    tween.TweenProperty(...);
    tween.TweenProperty(...); // Will run parallelly with above.
    tween.Chain().TweenProperty(...); // Will run after two above are finished.




----



[bool<class_bool>] **custom_step**\ (\ delta\: [float<class_float>]\ ) [🔗<class_Tween_method_custom_step>]

Processes the **Tween** by the given `delta` value, in seconds. This is mostly useful for manual control when the **Tween** is paused. It can also be used to end the **Tween** animation immediately, by setting `delta` longer than the whole duration of the **Tween** animation.

Returns `true` if the **Tween** still has [Tweener<class_Tweener>]\ s that haven't finished.


----



[int<class_int>] **get_loops_left**\ (\ ) |const| [🔗<class_Tween_method_get_loops_left>]

Returns the number of remaining loops for this **Tween** (see [set_loops()<class_Tween_method_set_loops>]). A return value of `-1` indicates an infinitely looping **Tween**, and a return value of `0` indicates that the **Tween** has already finished.


----



[float<class_float>] **get_total_elapsed_time**\ (\ ) |const| [🔗<class_Tween_method_get_total_elapsed_time>]

Returns the total time in seconds the **Tween** has been animating (i.e. the time since it started, not counting pauses etc.). The time is affected by [set_speed_scale()<class_Tween_method_set_speed_scale>], and [stop()<class_Tween_method_stop>] will reset it to `0`.

\ **Note:** As it results from accumulating frame deltas, the time returned after the **Tween** has finished animating will be slightly greater than the actual **Tween** duration.


----



[Variant<class_Variant>] **interpolate_value**\ (\ initial_value\: [Variant<class_Variant>], delta_value\: [Variant<class_Variant>], elapsed_time\: [float<class_float>], duration\: [float<class_float>], trans_type\: [TransitionType<enum_Tween_TransitionType>], ease_type\: [EaseType<enum_Tween_EaseType>]\ ) |static| [🔗<class_Tween_method_interpolate_value>]

This method can be used for manual interpolation of a value, when you don't want **Tween** to do animating for you. It's similar to [@GlobalScope.lerp()<class_@GlobalScope_method_lerp>], but with support for custom transition and easing.

\ `initial_value` is the starting value of the interpolation.

\ `delta_value` is the change of the value in the interpolation, i.e. it's equal to `final_value - initial_value`.

\ `elapsed_time` is the time in seconds that passed after the interpolation started and it's used to control the position of the interpolation. E.g. when it's equal to half of the `duration`, the interpolated value will be halfway between initial and final values. This value can also be greater than `duration` or lower than 0, which will extrapolate the value.

\ `duration` is the total time of the interpolation.

\ **Note:** If `duration` is equal to `0`, the method will always return the final value, regardless of `elapsed_time` provided.


----



[bool<class_bool>] **is_running**\ (\ ) [🔗<class_Tween_method_is_running>]

Returns whether the **Tween** is currently running, i.e. it wasn't paused and it's not finished.


----



[bool<class_bool>] **is_valid**\ (\ ) [🔗<class_Tween_method_is_valid>]

Returns whether the **Tween** is valid. A valid **Tween** is a **Tween** contained by the scene tree (i.e. the array from [SceneTree.get_processed_tweens()<class_SceneTree_method_get_processed_tweens>] will contain this **Tween**). A **Tween** might become invalid when it has finished tweening, is killed, or when created with `Tween.new()`. Invalid **Tween**\ s can't have [Tweener<class_Tweener>]\ s appended.


----



|void| **kill**\ (\ ) [🔗<class_Tween_method_kill>]

Aborts all tweening operations and invalidates the **Tween**.


----



[Tween<class_Tween>] **parallel**\ (\ ) [🔗<class_Tween_method_parallel>]

Makes the next [Tweener<class_Tweener>] run parallelly to the previous one.


> **TABS**
>

    var tween = create_tween()
    tween.tween_property(...)
    tween.parallel().tween_property(...)
    tween.parallel().tween_property(...)


    Tween tween = CreateTween();
    tween.TweenProperty(...);
    tween.Parallel().TweenProperty(...);
    tween.Parallel().TweenProperty(...);



All [Tweener<class_Tweener>]\ s in the example will run at the same time.

You can make the **Tween** parallel by default by using [set_parallel()<class_Tween_method_set_parallel>].


----



|void| **pause**\ (\ ) [🔗<class_Tween_method_pause>]

Pauses the tweening. The animation can be resumed by using [play()<class_Tween_method_play>].

\ **Note:** If a Tween is paused and not bound to any node, it will exist indefinitely until manually started or invalidated. If you lose a reference to such Tween, you can retrieve it using [SceneTree.get_processed_tweens()<class_SceneTree_method_get_processed_tweens>].


----



|void| **play**\ (\ ) [🔗<class_Tween_method_play>]

Resumes a paused or stopped **Tween**.


----



[Tween<class_Tween>] **set_ease**\ (\ ease\: [EaseType<enum_Tween_EaseType>]\ ) [🔗<class_Tween_method_set_ease>]

Sets the default ease type for [PropertyTweener<class_PropertyTweener>]\ s and [MethodTweener<class_MethodTweener>]\ s appended after this method.

Before this method is called, the default ease type is [EASE_IN_OUT<class_Tween_constant_EASE_IN_OUT>].

::

    var tween = create_tween()
    tween.tween_property(self, "position", Vector2(300, 0), 0.5) # Uses EASE_IN_OUT.
    tween.set_ease(Tween.EASE_IN)
    tween.tween_property(self, "rotation_degrees", 45.0, 0.5) # Uses EASE_IN.


----



[Tween<class_Tween>] **set_ignore_time_scale**\ (\ ignore\: [bool<class_bool>] = true\ ) [🔗<class_Tween_method_set_ignore_time_scale>]

If `ignore` is `true`, the tween will ignore [Engine.time_scale<class_Engine_property_time_scale>] and update with the real, elapsed time. This affects all [Tweener<class_Tweener>]\ s and their delays. Default value is `false`.


----



[Tween<class_Tween>] **set_loops**\ (\ loops\: [int<class_int>] = 0\ ) [🔗<class_Tween_method_set_loops>]

Sets the number of times the tweening sequence will be repeated, i.e. `set_loops(2)` will run the animation twice.

Calling this method without arguments will make the **Tween** run infinitely, until either it is killed with [kill()<class_Tween_method_kill>], the **Tween**'s bound node is freed, or all the animated objects have been freed (which makes further animation impossible).

\ **Warning:** Make sure to always add some duration/delay when using infinite loops. To prevent the game freezing, 0-duration looped animations (e.g. a single [CallbackTweener<class_CallbackTweener>] with no delay) are stopped after a small number of loops, which may produce unexpected results. If a **Tween**'s lifetime depends on some node, always use [bind_node()<class_Tween_method_bind_node>].


----



[Tween<class_Tween>] **set_parallel**\ (\ parallel\: [bool<class_bool>] = true\ ) [🔗<class_Tween_method_set_parallel>]

If `parallel` is `true`, the [Tweener<class_Tweener>]\ s appended after this method will by default run simultaneously, as opposed to sequentially.

\ **Note:** Just like with [parallel()<class_Tween_method_parallel>], the tweener added right before this method will also be part of the parallel step.

::

    tween.tween_property(self, "position", Vector2(300, 0), 0.5)
    tween.set_parallel()
    tween.tween_property(self, "modulate", Color.GREEN, 0.5) # Runs together with the position tweener.


----



[Tween<class_Tween>] **set_pause_mode**\ (\ mode\: [TweenPauseMode<enum_Tween_TweenPauseMode>]\ ) [🔗<class_Tween_method_set_pause_mode>]

Determines the behavior of the **Tween** when the [SceneTree<class_SceneTree>] is paused.

Default value is [TWEEN_PAUSE_BOUND<class_Tween_constant_TWEEN_PAUSE_BOUND>].


----



[Tween<class_Tween>] **set_process_mode**\ (\ mode\: [TweenProcessMode<enum_Tween_TweenProcessMode>]\ ) [🔗<class_Tween_method_set_process_mode>]

Determines whether the **Tween** should run after process frames (see [Node._process()<class_Node_private_method__process>]) or physics frames (see [Node._physics_process()<class_Node_private_method__physics_process>]).

Default value is [TWEEN_PROCESS_IDLE<class_Tween_constant_TWEEN_PROCESS_IDLE>].


----



[Tween<class_Tween>] **set_speed_scale**\ (\ speed\: [float<class_float>]\ ) [🔗<class_Tween_method_set_speed_scale>]

Scales the speed of tweening. This affects all [Tweener<class_Tweener>]\ s and their delays.


----



[Tween<class_Tween>] **set_trans**\ (\ trans\: [TransitionType<enum_Tween_TransitionType>]\ ) [🔗<class_Tween_method_set_trans>]

Sets the default transition type for [PropertyTweener<class_PropertyTweener>]\ s and [MethodTweener<class_MethodTweener>]\ s appended after this method.

Before this method is called, the default transition type is [TRANS_LINEAR<class_Tween_constant_TRANS_LINEAR>].

::

    var tween = create_tween()
    tween.tween_property(self, "position", Vector2(300, 0), 0.5) # Uses TRANS_LINEAR.
    tween.set_trans(Tween.TRANS_SINE)
    tween.tween_property(self, "rotation_degrees", 45.0, 0.5) # Uses TRANS_SINE.


----



|void| **stop**\ (\ ) [🔗<class_Tween_method_stop>]

Stops the tweening and resets the **Tween** to its initial state. This will not remove any appended [Tweener<class_Tweener>]\ s.

\ **Note:** This does *not* reset targets of [PropertyTweener<class_PropertyTweener>]\ s to their values when the **Tween** first started.

::

    var tween = create_tween()

    # Will move from 0 to 500 over 1 second.
    position.x = 0.0
    tween.tween_property(self, "position:x", 500, 1.0)

    # Will be at (about) 250 when the timer finishes.
    await get_tree().create_timer(0.5).timeout

    # Will now move from (about) 250 to 500 over 1 second,
    # thus at half the speed as before.
    tween.stop()
    tween.play()

\ **Note:** If a Tween is stopped and not bound to any node, it will exist indefinitely until manually started or invalidated. If you lose a reference to such Tween, you can retrieve it using [SceneTree.get_processed_tweens()<class_SceneTree_method_get_processed_tweens>].


----



[CallbackTweener<class_CallbackTweener>] **tween_callback**\ (\ callback\: [Callable<class_Callable>]\ ) [🔗<class_Tween_method_tween_callback>]

Creates and appends a [CallbackTweener<class_CallbackTweener>]. This method can be used to call an arbitrary method in any object. Use [Callable.bind()<class_Callable_method_bind>] to bind additional arguments for the call.

\ **Example:** Object that keeps shooting every 1 second:


> **TABS**
>

    var tween = get_tree().create_tween().set_loops()
    tween.tween_callback(shoot).set_delay(1.0)


    Tween tween = GetTree().CreateTween().SetLoops();
    tween.TweenCallback(Callable.From(Shoot)).SetDelay(1.0f);



\ **Example:** Turning a sprite red and then blue, with 2 second delay:


> **TABS**
>

    var tween = get_tree().create_tween()
    tween.tween_callback($Sprite.set_modulate.bind(Color.RED)).set_delay(2)
    tween.tween_callback($Sprite.set_modulate.bind(Color.BLUE)).set_delay(2)


    Tween tween = GetTree().CreateTween();
    Sprite2D sprite = GetNode<Sprite2D>("Sprite");
    tween.TweenCallback(Callable.From(() => sprite.Modulate = Colors.Red)).SetDelay(2.0f);
    tween.TweenCallback(Callable.From(() => sprite.Modulate = Colors.Blue)).SetDelay(2.0f);




----



[IntervalTweener<class_IntervalTweener>] **tween_interval**\ (\ time\: [float<class_float>]\ ) [🔗<class_Tween_method_tween_interval>]

Creates and appends an [IntervalTweener<class_IntervalTweener>]. This method can be used to create delays in the tween animation, as an alternative to using the delay in other [Tweener<class_Tweener>]\ s, or when there's no animation (in which case the **Tween** acts as a timer). `time` is the length of the interval, in seconds.

\ **Example:** Creating an interval in code execution:


> **TABS**
>

    # ... some code
    await create_tween().tween_interval(2).finished
    # ... more code


    // ... some code
    await ToSignal(CreateTween().TweenInterval(2.0f), Tween.SignalName.Finished);
    // ... more code



\ **Example:** Creating an object that moves back and forth and jumps every few seconds:


> **TABS**
>

    var tween = create_tween().set_loops()
    tween.tween_property($Sprite, "position:x", 200.0, 1.0).as_relative()
    tween.tween_callback(jump)
    tween.tween_interval(2)
    tween.tween_property($Sprite, "position:x", -200.0, 1.0).as_relative()
    tween.tween_callback(jump)
    tween.tween_interval(2)


    Tween tween = CreateTween().SetLoops();
    tween.TweenProperty(GetNode("Sprite"), "position:x", 200.0f, 1.0f).AsRelative();
    tween.TweenCallback(Callable.From(Jump));
    tween.TweenInterval(2.0f);
    tween.TweenProperty(GetNode("Sprite"), "position:x", -200.0f, 1.0f).AsRelative();
    tween.TweenCallback(Callable.From(Jump));
    tween.TweenInterval(2.0f);




----



[MethodTweener<class_MethodTweener>] **tween_method**\ (\ method\: [Callable<class_Callable>], from\: [Variant<class_Variant>], to\: [Variant<class_Variant>], duration\: [float<class_float>]\ ) [🔗<class_Tween_method_tween_method>]

Creates and appends a [MethodTweener<class_MethodTweener>]. This method is similar to a combination of [tween_callback()<class_Tween_method_tween_callback>] and [tween_property()<class_Tween_method_tween_property>]. It calls a method over time with a tweened value provided as an argument. The value is tweened between `from` and `to` over the time specified by `duration`, in seconds. Use [Callable.bind()<class_Callable_method_bind>] to bind additional arguments for the call. You can use [MethodTweener.set_ease()<class_MethodTweener_method_set_ease>] and [MethodTweener.set_trans()<class_MethodTweener_method_set_trans>] to tweak the easing and transition of the value or [MethodTweener.set_delay()<class_MethodTweener_method_set_delay>] to delay the tweening.

\ **Example:** Making a 3D object look from one point to another point:


> **TABS**
>

    var tween = create_tween()
    tween.tween_method(look_at.bind(Vector3.UP), Vector3(-1, 0, -1), Vector3(1, 0, -1), 1.0) # The look_at() method takes up vector as second argument.


    Tween tween = CreateTween();
    tween.TweenMethod(Callable.From((Vector3 target) => LookAt(target, Vector3.Up)), new Vector3(-1.0f, 0.0f, -1.0f), new Vector3(1.0f, 0.0f, -1.0f), 1.0f); // Use lambdas to bind additional arguments for the call.



\ **Example:** Setting the text of a [Label<class_Label>], using an intermediate method and after a delay:


> **TABS**
>

    func _ready():
        var tween = create_tween()
        tween.tween_method(set_label_text, 0, 10, 1.0).set_delay(1.0)

    func set_label_text(value: int):
        $Label.text = "Counting " + str(value)


    public override void _Ready()
    {
        base._Ready();

        Tween tween = CreateTween();
        tween.TweenMethod(Callable.From<int>(SetLabelText), 0.0f, 10.0f, 1.0f).SetDelay(1.0f);
    }

    private void SetLabelText(int value)
    {
        GetNode<Label>("Label").Text = $"Counting {value}";
    }




----



[PropertyTweener<class_PropertyTweener>] **tween_property**\ (\ object\: [Object<class_Object>], property\: [NodePath<class_NodePath>], final_val\: [Variant<class_Variant>], duration\: [float<class_float>]\ ) [🔗<class_Tween_method_tween_property>]

Creates and appends a [PropertyTweener<class_PropertyTweener>]. This method tweens a `property` of an `object` between an initial value and `final_val` in a span of time equal to `duration`, in seconds. The initial value by default is the property's value at the time the tweening of the [PropertyTweener<class_PropertyTweener>] starts.


> **TABS**
>

    var tween = create_tween()
    tween.tween_property($Sprite, "position", Vector2(100, 200), 1.0)
    tween.tween_property($Sprite, "position", Vector2(200, 300), 1.0)


    Tween tween = CreateTween();
    tween.TweenProperty(GetNode("Sprite"), "position", new Vector2(100.0f, 200.0f), 1.0f);
    tween.TweenProperty(GetNode("Sprite"), "position", new Vector2(200.0f, 300.0f), 1.0f);



will move the sprite to position (100, 200) and then to (200, 300). If you use [PropertyTweener.from()<class_PropertyTweener_method_from>] or [PropertyTweener.from_current()<class_PropertyTweener_method_from_current>], the starting position will be overwritten by the given value instead. See other methods in [PropertyTweener<class_PropertyTweener>] to see how the tweening can be tweaked further.

\ **Note:** You can find the correct property name by hovering over the property in the Inspector. You can also provide the components of a property directly by using `"property:component"` (eg. `position:x`), where it would only apply to that particular component.

\ **Example:** Moving an object twice from the same position, with different transition types:


> **TABS**
>

    var tween = create_tween()
    tween.tween_property($Sprite, "position", Vector2.RIGHT * 300, 1.0).as_relative().set_trans(Tween.TRANS_SINE)
    tween.tween_property($Sprite, "position", Vector2.RIGHT * 300, 1.0).as_relative().from_current().set_trans(Tween.TRANS_EXPO)


    Tween tween = CreateTween();
    tween.TweenProperty(GetNode("Sprite"), "position", Vector2.Right * 300.0f, 1.0f).AsRelative().SetTrans(Tween.TransitionType.Sine);
    tween.TweenProperty(GetNode("Sprite"), "position", Vector2.Right * 300.0f, 1.0f).AsRelative().FromCurrent().SetTrans(Tween.TransitionType.Expo);




----



[SubtweenTweener<class_SubtweenTweener>] **tween_subtween**\ (\ subtween\: [Tween<class_Tween>]\ ) [🔗<class_Tween_method_tween_subtween>]

Creates and appends a [SubtweenTweener<class_SubtweenTweener>]. This method can be used to nest `subtween` within this **Tween**, allowing for the creation of more complex and composable sequences.

::

    # Subtween will rotate the object.
    var subtween = create_tween()
    subtween.tween_property(self, "rotation_degrees", 45.0, 1.0)
    subtween.tween_property(self, "rotation_degrees", 0.0, 1.0)

    # Parent tween will execute the subtween as one of its steps.
    var tween = create_tween()
    tween.tween_property(self, "position:x", 500, 3.0)
    tween.tween_subtween(subtween)
    tween.tween_property(self, "position:x", 300, 2.0)

\ **Note:** The methods [pause()<class_Tween_method_pause>], [stop()<class_Tween_method_stop>], and [set_loops()<class_Tween_method_set_loops>] can cause the parent **Tween** to get stuck on the subtween step; see the documentation for those methods for more information.

\ **Note:** The pause and process modes set by [set_pause_mode()<class_Tween_method_set_pause_mode>] and [set_process_mode()<class_Tween_method_set_process_mode>] on `subtween` will be overridden by the parent **Tween**'s settings.

