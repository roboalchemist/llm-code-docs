:github_url: hide



# MethodTweener

**Inherits:** [Tweener<class_Tweener>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Interpolates an abstract value and supplies it to a method called over time.


## Description

**MethodTweener** is similar to a combination of [CallbackTweener<class_CallbackTweener>] and [PropertyTweener<class_PropertyTweener>]. It calls a method providing an interpolated value as a parameter. See [Tween.tween_method()<class_Tween_method_tween_method>] for more usage information.

The tweener will finish automatically if the callback's target object is freed.

\ **Note:** [Tween.tween_method()<class_Tween_method_tween_method>] is the only correct way to create **MethodTweener**. Any **MethodTweener** created manually will not function correctly.


## Methods

> **TABLE**
> :widths: auto
>
> +-------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
> | :ref:`MethodTweener<class_MethodTweener>` | :ref:`set_delay<class_MethodTweener_method_set_delay>`\ (\ delay\: :ref:`float<class_float>`\ )                        |
> +-------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
> | :ref:`MethodTweener<class_MethodTweener>` | :ref:`set_ease<class_MethodTweener_method_set_ease>`\ (\ ease\: :ref:`EaseType<enum_Tween_EaseType>`\ )                |
> +-------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
> | :ref:`MethodTweener<class_MethodTweener>` | :ref:`set_trans<class_MethodTweener_method_set_trans>`\ (\ trans\: :ref:`TransitionType<enum_Tween_TransitionType>`\ ) |
> +-------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
>

----


## Method Descriptions



[MethodTweener<class_MethodTweener>] **set_delay**\ (\ delay\: [float<class_float>]\ ) [🔗<class_MethodTweener_method_set_delay>]

Sets the time in seconds after which the **MethodTweener** will start interpolating. By default there's no delay.


----



[MethodTweener<class_MethodTweener>] **set_ease**\ (\ ease\: [EaseType<enum_Tween_EaseType>]\ ) [🔗<class_MethodTweener_method_set_ease>]

Sets the type of used easing from [EaseType<enum_Tween_EaseType>]. If not set, the default easing is used from the [Tween<class_Tween>] that contains this Tweener.


----



[MethodTweener<class_MethodTweener>] **set_trans**\ (\ trans\: [TransitionType<enum_Tween_TransitionType>]\ ) [🔗<class_MethodTweener_method_set_trans>]

Sets the type of used transition from [TransitionType<enum_Tween_TransitionType>]. If not set, the default transition is used from the [Tween<class_Tween>] that contains this Tweener.

