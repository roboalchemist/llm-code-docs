:github_url: hide



# Range

**Inherits:** [Control<class_Control>] **<** [CanvasItem<class_CanvasItem>] **<** [Node<class_Node>] **<** [Object<class_Object>]

**Inherited By:** [EditorSpinSlider<class_EditorSpinSlider>], [ProgressBar<class_ProgressBar>], [ScrollBar<class_ScrollBar>], [Slider<class_Slider>], [SpinBox<class_SpinBox>], [TextureProgressBar<class_TextureProgressBar>]

Abstract base class for controls that represent a number within a range.


## Description

Range is an abstract base class for controls that represent a number within a range, using a configured [step<class_Range_property_step>] and [page<class_Range_property_page>] size. See e.g. [ScrollBar<class_ScrollBar>] and [Slider<class_Slider>] for examples of higher-level nodes using Range.


## Properties

> **TABLE**
> :widths: auto
>
> +--------------------------------------------------------+----------------------------------------------------------+------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                | :ref:`allow_greater<class_Range_property_allow_greater>` | ``false``                                                                    |
> +--------------------------------------------------------+----------------------------------------------------------+------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                | :ref:`allow_lesser<class_Range_property_allow_lesser>`   | ``false``                                                                    |
> +--------------------------------------------------------+----------------------------------------------------------+------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                | :ref:`exp_edit<class_Range_property_exp_edit>`           | ``false``                                                                    |
> +--------------------------------------------------------+----------------------------------------------------------+------------------------------------------------------------------------------+
> | :ref:`float<class_float>`                              | :ref:`max_value<class_Range_property_max_value>`         | ``100.0``                                                                    |
> +--------------------------------------------------------+----------------------------------------------------------+------------------------------------------------------------------------------+
> | :ref:`float<class_float>`                              | :ref:`min_value<class_Range_property_min_value>`         | ``0.0``                                                                      |
> +--------------------------------------------------------+----------------------------------------------------------+------------------------------------------------------------------------------+
> | :ref:`float<class_float>`                              | :ref:`page<class_Range_property_page>`                   | ``0.0``                                                                      |
> +--------------------------------------------------------+----------------------------------------------------------+------------------------------------------------------------------------------+
> | :ref:`float<class_float>`                              | :ref:`ratio<class_Range_property_ratio>`                 |                                                                              |
> +--------------------------------------------------------+----------------------------------------------------------+------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                | :ref:`rounded<class_Range_property_rounded>`             | ``false``                                                                    |
> +--------------------------------------------------------+----------------------------------------------------------+------------------------------------------------------------------------------+
> | |bitfield|\[:ref:`SizeFlags<enum_Control_SizeFlags>`\] | size_flags_vertical                                      | ``0`` (overrides :ref:`Control<class_Control_property_size_flags_vertical>`) |
> +--------------------------------------------------------+----------------------------------------------------------+------------------------------------------------------------------------------+
> | :ref:`float<class_float>`                              | :ref:`step<class_Range_property_step>`                   | ``0.01``                                                                     |
> +--------------------------------------------------------+----------------------------------------------------------+------------------------------------------------------------------------------+
> | :ref:`float<class_float>`                              | :ref:`value<class_Range_property_value>`                 | ``0.0``                                                                      |
> +--------------------------------------------------------+----------------------------------------------------------+------------------------------------------------------------------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +--------+-------------------------------------------------------------------------------------------------------------------------+
> | |void| | :ref:`_value_changed<class_Range_private_method__value_changed>`\ (\ new_value\: :ref:`float<class_float>`\ ) |virtual| |
> +--------+-------------------------------------------------------------------------------------------------------------------------+
> | |void| | :ref:`set_value_no_signal<class_Range_method_set_value_no_signal>`\ (\ value\: :ref:`float<class_float>`\ )             |
> +--------+-------------------------------------------------------------------------------------------------------------------------+
> | |void| | :ref:`share<class_Range_method_share>`\ (\ with\: :ref:`Node<class_Node>`\ )                                            |
> +--------+-------------------------------------------------------------------------------------------------------------------------+
> | |void| | :ref:`unshare<class_Range_method_unshare>`\ (\ )                                                                        |
> +--------+-------------------------------------------------------------------------------------------------------------------------+
>

----


## Signals



**changed**\ (\ ) [🔗<class_Range_signal_changed>]

Emitted when [min_value<class_Range_property_min_value>], [max_value<class_Range_property_max_value>], [page<class_Range_property_page>], or [step<class_Range_property_step>] change.


----



**value_changed**\ (\ value\: [float<class_float>]\ ) [🔗<class_Range_signal_value_changed>]

Emitted when [value<class_Range_property_value>] changes. When used on a [Slider<class_Slider>], this is called continuously while dragging (potentially every frame). If you are performing an expensive operation in a function connected to [value_changed<class_Range_signal_value_changed>], consider using a *debouncing* [Timer<class_Timer>] to call the function less often.

\ **Note:** Unlike signals such as [LineEdit.text_changed<class_LineEdit_signal_text_changed>], [value_changed<class_Range_signal_value_changed>] is also emitted when `value` is set directly via code.


----


## Property Descriptions



[bool<class_bool>] **allow_greater** = `false` [🔗<class_Range_property_allow_greater>]


- |void| **set_allow_greater**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_greater_allowed**\ (\ )

If `true`, [value<class_Range_property_value>] may be greater than [max_value<class_Range_property_max_value>].


----



[bool<class_bool>] **allow_lesser** = `false` [🔗<class_Range_property_allow_lesser>]


- |void| **set_allow_lesser**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_lesser_allowed**\ (\ )

If `true`, [value<class_Range_property_value>] may be less than [min_value<class_Range_property_min_value>].


----



[bool<class_bool>] **exp_edit** = `false` [🔗<class_Range_property_exp_edit>]


- |void| **set_exp_ratio**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_ratio_exp**\ (\ )

If `true`, and [min_value<class_Range_property_min_value>] is greater or equal to `0`, [value<class_Range_property_value>] will be represented exponentially rather than linearly.


----



[float<class_float>] **max_value** = `100.0` [🔗<class_Range_property_max_value>]


- |void| **set_max**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_max**\ (\ )

Maximum value. Range is clamped if [value<class_Range_property_value>] is greater than [max_value<class_Range_property_max_value>].


----



[float<class_float>] **min_value** = `0.0` [🔗<class_Range_property_min_value>]


- |void| **set_min**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_min**\ (\ )

Minimum value. Range is clamped if [value<class_Range_property_value>] is less than [min_value<class_Range_property_min_value>].


----



[float<class_float>] **page** = `0.0` [🔗<class_Range_property_page>]


- |void| **set_page**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_page**\ (\ )

Page size. Used mainly for [ScrollBar<class_ScrollBar>]. A [ScrollBar<class_ScrollBar>]'s grabber length is the [ScrollBar<class_ScrollBar>]'s size multiplied by [page<class_Range_property_page>] over the difference between [min_value<class_Range_property_min_value>] and [max_value<class_Range_property_max_value>].


----



[float<class_float>] **ratio** [🔗<class_Range_property_ratio>]


- |void| **set_as_ratio**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_as_ratio**\ (\ )

The value mapped between 0 and 1.


----



[bool<class_bool>] **rounded** = `false` [🔗<class_Range_property_rounded>]


- |void| **set_use_rounded_values**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_using_rounded_values**\ (\ )

If `true`, [value<class_Range_property_value>] will always be rounded to the nearest integer.


----



[float<class_float>] **step** = `0.01` [🔗<class_Range_property_step>]


- |void| **set_step**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_step**\ (\ )

If greater than `0.0`, [value<class_Range_property_value>] will always be rounded to a multiple of this property's value above [min_value<class_Range_property_min_value>]. For example, if [min_value<class_Range_property_min_value>] is `0.1` and step is `0.2`, then [value<class_Range_property_value>] is limited to `0.1`, `0.3`, `0.5`, and so on. If [rounded<class_Range_property_rounded>] is also `true`, [value<class_Range_property_value>] will first be rounded to a multiple of this property's value, then rounded to the nearest integer.


----



[float<class_float>] **value** = `0.0` [🔗<class_Range_property_value>]


- |void| **set_value**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_value**\ (\ )

Range's current value. Changing this property (even via code) will trigger [value_changed<class_Range_signal_value_changed>] signal. Use [set_value_no_signal()<class_Range_method_set_value_no_signal>] if you want to avoid it.


----


## Method Descriptions



|void| **_value_changed**\ (\ new_value\: [float<class_float>]\ ) |virtual| [🔗<class_Range_private_method__value_changed>]

Called when the **Range**'s value is changed (following the same conditions as [value_changed<class_Range_signal_value_changed>]).


----



|void| **set_value_no_signal**\ (\ value\: [float<class_float>]\ ) [🔗<class_Range_method_set_value_no_signal>]

Sets the **Range**'s current value to the specified `value`, without emitting the [value_changed<class_Range_signal_value_changed>] signal.


----



|void| **share**\ (\ with\: [Node<class_Node>]\ ) [🔗<class_Range_method_share>]

Binds two **Range**\ s together along with any ranges previously grouped with either of them. When any of range's member variables change, it will share the new value with all other ranges in its group.


----



|void| **unshare**\ (\ ) [🔗<class_Range_method_unshare>]

Stops the **Range** from sharing its member variables with any other.

