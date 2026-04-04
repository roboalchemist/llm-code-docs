:github_url: hide



# PropertyTweener

**Inherits:** [Tweener<class_Tweener>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Interpolates an [Object<class_Object>]'s property over time.


## Description

**PropertyTweener** is used to interpolate a property in an object. See [Tween.tween_property()<class_Tween_method_tween_property>] for more usage information.

The tweener will finish automatically if the target object is freed.

\ **Note:** [Tween.tween_property()<class_Tween_method_tween_property>] is the only correct way to create **PropertyTweener**. Any **PropertyTweener** created manually will not function correctly.


## Methods

> **TABLE**
> :widths: auto
>
> +-----------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PropertyTweener<class_PropertyTweener>` | :ref:`as_relative<class_PropertyTweener_method_as_relative>`\ (\ )                                                                                |
> +-----------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PropertyTweener<class_PropertyTweener>` | :ref:`from<class_PropertyTweener_method_from>`\ (\ value\: :ref:`Variant<class_Variant>`\ )                                                       |
> +-----------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PropertyTweener<class_PropertyTweener>` | :ref:`from_current<class_PropertyTweener_method_from_current>`\ (\ )                                                                              |
> +-----------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PropertyTweener<class_PropertyTweener>` | :ref:`set_custom_interpolator<class_PropertyTweener_method_set_custom_interpolator>`\ (\ interpolator_method\: :ref:`Callable<class_Callable>`\ ) |
> +-----------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PropertyTweener<class_PropertyTweener>` | :ref:`set_delay<class_PropertyTweener_method_set_delay>`\ (\ delay\: :ref:`float<class_float>`\ )                                                 |
> +-----------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PropertyTweener<class_PropertyTweener>` | :ref:`set_ease<class_PropertyTweener_method_set_ease>`\ (\ ease\: :ref:`EaseType<enum_Tween_EaseType>`\ )                                         |
> +-----------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PropertyTweener<class_PropertyTweener>` | :ref:`set_trans<class_PropertyTweener_method_set_trans>`\ (\ trans\: :ref:`TransitionType<enum_Tween_TransitionType>`\ )                          |
> +-----------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Method Descriptions



[PropertyTweener<class_PropertyTweener>] **as_relative**\ (\ ) [🔗<class_PropertyTweener_method_as_relative>]

When called, the final value will be used as a relative value instead.

\ **Example:** Move the node by `100` pixels to the right.


> **TABS**
>

    var tween = get_tree().create_tween()
    tween.tween_property(self, "position", Vector2.RIGHT * 100, 1).as_relative()


    Tween tween = GetTree().CreateTween();
    tween.TweenProperty(this, "position", Vector2.Right * 100.0f, 1.0f).AsRelative();




----



[PropertyTweener<class_PropertyTweener>] **from**\ (\ value\: [Variant<class_Variant>]\ ) [🔗<class_PropertyTweener_method_from>]

Sets a custom initial value to the **PropertyTweener**.

\ **Example:** Move the node from position `(100, 100)` to `(200, 100)`.


> **TABS**
>

    var tween = get_tree().create_tween()
    tween.tween_property(self, "position", Vector2(200, 100), 1).from(Vector2(100, 100))


    Tween tween = GetTree().CreateTween();
    tween.TweenProperty(this, "position", new Vector2(200.0f, 100.0f), 1.0f).From(new Vector2(100.0f, 100.0f));




----



[PropertyTweener<class_PropertyTweener>] **from_current**\ (\ ) [🔗<class_PropertyTweener_method_from_current>]

Makes the **PropertyTweener** use the current property value (i.e. at the time of creating this **PropertyTweener**) as a starting point. This is equivalent of using [from()<class_PropertyTweener_method_from>] with the current value. These two calls will do the same:


> **TABS**
>

    tween.tween_property(self, "position", Vector2(200, 100), 1).from(position)
    tween.tween_property(self, "position", Vector2(200, 100), 1).from_current()


    tween.TweenProperty(this, "position", new Vector2(200.0f, 100.0f), 1.0f).From(Position);
    tween.TweenProperty(this, "position", new Vector2(200.0f, 100.0f), 1.0f).FromCurrent();




----



[PropertyTweener<class_PropertyTweener>] **set_custom_interpolator**\ (\ interpolator_method\: [Callable<class_Callable>]\ ) [🔗<class_PropertyTweener_method_set_custom_interpolator>]

Allows interpolating the value with a custom easing function. The provided `interpolator_method` will be called with a value ranging from `0.0` to `1.0` and is expected to return a value within the same range (values outside the range can be used for overshoot). The return value of the method is then used for interpolation between initial and final value. Note that the parameter passed to the method is still subject to the tweener's own easing.


> **TABS**
>

    @export var curve: Curve

    func _ready():
        var tween = create_tween()
        # Interpolate the value using a custom curve.
        tween.tween_property(self, "position:x", 300, 1).as_relative().set_custom_interpolator(tween_curve)

    func tween_curve(v):
        return curve.sample_baked(v)


    [Export]
    public Curve Curve { get; set; }

    public override void _Ready()
    {
        Tween tween = CreateTween();
        // Interpolate the value using a custom curve.
        Callable tweenCurveCallable = Callable.From<float, float>(TweenCurve);
        tween.TweenProperty(this, "position:x", 300.0f, 1.0f).AsRelative().SetCustomInterpolator(tweenCurveCallable);
    }

    private float TweenCurve(float value)
    {
        return Curve.SampleBaked(value);
    }




----



[PropertyTweener<class_PropertyTweener>] **set_delay**\ (\ delay\: [float<class_float>]\ ) [🔗<class_PropertyTweener_method_set_delay>]

Sets the time in seconds after which the **PropertyTweener** will start interpolating. By default there's no delay.


----



[PropertyTweener<class_PropertyTweener>] **set_ease**\ (\ ease\: [EaseType<enum_Tween_EaseType>]\ ) [🔗<class_PropertyTweener_method_set_ease>]

Sets the type of used easing from [EaseType<enum_Tween_EaseType>]. If not set, the default easing is used from the [Tween<class_Tween>] that contains this Tweener.


----



[PropertyTweener<class_PropertyTweener>] **set_trans**\ (\ trans\: [TransitionType<enum_Tween_TransitionType>]\ ) [🔗<class_PropertyTweener_method_set_trans>]

Sets the type of used transition from [TransitionType<enum_Tween_TransitionType>]. If not set, the default transition is used from the [Tween<class_Tween>] that contains this Tweener.

