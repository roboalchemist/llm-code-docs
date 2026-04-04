:github_url: hide



# SubtweenTweener

**Inherits:** [Tweener<class_Tweener>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Runs a [Tween<class_Tween>] nested within another [Tween<class_Tween>].


## Description

**SubtweenTweener** is used to execute a [Tween<class_Tween>] as one step in a sequence defined by another [Tween<class_Tween>]. See [Tween.tween_subtween()<class_Tween_method_tween_subtween>] for more usage information.

\ **Note:** [Tween.tween_subtween()<class_Tween_method_tween_subtween>] is the only correct way to create **SubtweenTweener**. Any **SubtweenTweener** created manually will not function correctly.


## Methods

> **TABLE**
> :widths: auto
>
> +-----------------------------------------------+---------------------------------------------------------------------------------------------------+
> | :ref:`SubtweenTweener<class_SubtweenTweener>` | :ref:`set_delay<class_SubtweenTweener_method_set_delay>`\ (\ delay\: :ref:`float<class_float>`\ ) |
> +-----------------------------------------------+---------------------------------------------------------------------------------------------------+
>

----


## Method Descriptions



[SubtweenTweener<class_SubtweenTweener>] **set_delay**\ (\ delay\: [float<class_float>]\ ) [🔗<class_SubtweenTweener_method_set_delay>]

Sets the time in seconds after which the **SubtweenTweener** will start running the subtween. By default there's no delay.

