:github_url: hide



# HingeJoint3D

**Inherits:** [Joint3D<class_Joint3D>] **<** [Node3D<class_Node3D>] **<** [Node<class_Node>] **<** [Object<class_Object>]

A physics joint that restricts the rotation of a 3D physics body around an axis relative to another physics body.


## Description

A physics joint that restricts the rotation of a 3D physics body around an axis relative to another physics body. For example, Body A can be a [StaticBody3D<class_StaticBody3D>] representing a door hinge that a [RigidBody3D<class_RigidBody3D>] rotates around.


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------+---------------------------------------------------------------------------------------+----------------+
> | :ref:`float<class_float>` | :ref:`angular_limit/bias<class_HingeJoint3D_property_angular_limit/bias>`             | ``0.3``        |
> +---------------------------+---------------------------------------------------------------------------------------+----------------+
> | :ref:`bool<class_bool>`   | :ref:`angular_limit/enable<class_HingeJoint3D_property_angular_limit/enable>`         | ``false``      |
> +---------------------------+---------------------------------------------------------------------------------------+----------------+
> | :ref:`float<class_float>` | :ref:`angular_limit/lower<class_HingeJoint3D_property_angular_limit/lower>`           | ``-1.5707964`` |
> +---------------------------+---------------------------------------------------------------------------------------+----------------+
> | :ref:`float<class_float>` | :ref:`angular_limit/relaxation<class_HingeJoint3D_property_angular_limit/relaxation>` | ``1.0``        |
> +---------------------------+---------------------------------------------------------------------------------------+----------------+
> | :ref:`float<class_float>` | :ref:`angular_limit/softness<class_HingeJoint3D_property_angular_limit/softness>`     | ``0.9``        |
> +---------------------------+---------------------------------------------------------------------------------------+----------------+
> | :ref:`float<class_float>` | :ref:`angular_limit/upper<class_HingeJoint3D_property_angular_limit/upper>`           | ``1.5707964``  |
> +---------------------------+---------------------------------------------------------------------------------------+----------------+
> | :ref:`bool<class_bool>`   | :ref:`motor/enable<class_HingeJoint3D_property_motor/enable>`                         | ``false``      |
> +---------------------------+---------------------------------------------------------------------------------------+----------------+
> | :ref:`float<class_float>` | :ref:`motor/max_impulse<class_HingeJoint3D_property_motor/max_impulse>`               | ``1.0``        |
> +---------------------------+---------------------------------------------------------------------------------------+----------------+
> | :ref:`float<class_float>` | :ref:`motor/target_velocity<class_HingeJoint3D_property_motor/target_velocity>`       | ``1.0``        |
> +---------------------------+---------------------------------------------------------------------------------------+----------------+
> | :ref:`float<class_float>` | :ref:`params/bias<class_HingeJoint3D_property_params/bias>`                           | ``0.3``        |
> +---------------------------+---------------------------------------------------------------------------------------+----------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +---------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`   | :ref:`get_flag<class_HingeJoint3D_method_get_flag>`\ (\ flag\: :ref:`Flag<enum_HingeJoint3D_Flag>`\ ) |const|                                 |
> +---------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>` | :ref:`get_param<class_HingeJoint3D_method_get_param>`\ (\ param\: :ref:`Param<enum_HingeJoint3D_Param>`\ ) |const|                            |
> +---------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                    | :ref:`set_flag<class_HingeJoint3D_method_set_flag>`\ (\ flag\: :ref:`Flag<enum_HingeJoint3D_Flag>`, enabled\: :ref:`bool<class_bool>`\ )      |
> +---------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                    | :ref:`set_param<class_HingeJoint3D_method_set_param>`\ (\ param\: :ref:`Param<enum_HingeJoint3D_Param>`, value\: :ref:`float<class_float>`\ ) |
> +---------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Enumerations



enum **Param**: [🔗<enum_HingeJoint3D_Param>]



[Param<enum_HingeJoint3D_Param>] **PARAM_BIAS** = `0`

The speed with which the two bodies get pulled together when they move in different directions.



[Param<enum_HingeJoint3D_Param>] **PARAM_LIMIT_UPPER** = `1`

The maximum rotation. Only active if [angular_limit/enable<class_HingeJoint3D_property_angular_limit/enable>] is `true`.



[Param<enum_HingeJoint3D_Param>] **PARAM_LIMIT_LOWER** = `2`

The minimum rotation. Only active if [angular_limit/enable<class_HingeJoint3D_property_angular_limit/enable>] is `true`.



[Param<enum_HingeJoint3D_Param>] **PARAM_LIMIT_BIAS** = `3`

The speed with which the rotation across the axis perpendicular to the hinge gets corrected.



[Param<enum_HingeJoint3D_Param>] **PARAM_LIMIT_SOFTNESS** = `4`

**Deprecated:** This property is never used by the engine and is kept for compatibility purpose.





[Param<enum_HingeJoint3D_Param>] **PARAM_LIMIT_RELAXATION** = `5`

The lower this value, the more the rotation gets slowed down.



[Param<enum_HingeJoint3D_Param>] **PARAM_MOTOR_TARGET_VELOCITY** = `6`

Target speed for the motor.



[Param<enum_HingeJoint3D_Param>] **PARAM_MOTOR_MAX_IMPULSE** = `7`

Maximum acceleration for the motor.



[Param<enum_HingeJoint3D_Param>] **PARAM_MAX** = `8`

Represents the size of the [Param<enum_HingeJoint3D_Param>] enum.


----



enum **Flag**: [🔗<enum_HingeJoint3D_Flag>]



[Flag<enum_HingeJoint3D_Flag>] **FLAG_USE_LIMIT** = `0`

If `true`, the hinges maximum and minimum rotation, defined by [angular_limit/lower<class_HingeJoint3D_property_angular_limit/lower>] and [angular_limit/upper<class_HingeJoint3D_property_angular_limit/upper>] has effects.



[Flag<enum_HingeJoint3D_Flag>] **FLAG_ENABLE_MOTOR** = `1`

When activated, a motor turns the hinge.



[Flag<enum_HingeJoint3D_Flag>] **FLAG_MAX** = `2`

Represents the size of the [Flag<enum_HingeJoint3D_Flag>] enum.


----


## Property Descriptions



[float<class_float>] **angular_limit/bias** = `0.3` [🔗<class_HingeJoint3D_property_angular_limit/bias>]


- |void| **set_param**\ (\ param\: [Param<enum_HingeJoint3D_Param>], value\: [float<class_float>]\ )
- [float<class_float>] **get_param**\ (\ param\: [Param<enum_HingeJoint3D_Param>]\ ) |const|

The speed with which the rotation across the axis perpendicular to the hinge gets corrected.


----



[bool<class_bool>] **angular_limit/enable** = `false` [🔗<class_HingeJoint3D_property_angular_limit/enable>]


- |void| **set_flag**\ (\ flag\: [Flag<enum_HingeJoint3D_Flag>], enabled\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_flag**\ (\ flag\: [Flag<enum_HingeJoint3D_Flag>]\ ) |const|

If `true`, the hinges maximum and minimum rotation, defined by [angular_limit/lower<class_HingeJoint3D_property_angular_limit/lower>] and [angular_limit/upper<class_HingeJoint3D_property_angular_limit/upper>] has effects.


----



[float<class_float>] **angular_limit/lower** = `-1.5707964` [🔗<class_HingeJoint3D_property_angular_limit/lower>]


- |void| **set_param**\ (\ param\: [Param<enum_HingeJoint3D_Param>], value\: [float<class_float>]\ )
- [float<class_float>] **get_param**\ (\ param\: [Param<enum_HingeJoint3D_Param>]\ ) |const|

The minimum rotation. Only active if [angular_limit/enable<class_HingeJoint3D_property_angular_limit/enable>] is `true`.


----



[float<class_float>] **angular_limit/relaxation** = `1.0` [🔗<class_HingeJoint3D_property_angular_limit/relaxation>]


- |void| **set_param**\ (\ param\: [Param<enum_HingeJoint3D_Param>], value\: [float<class_float>]\ )
- [float<class_float>] **get_param**\ (\ param\: [Param<enum_HingeJoint3D_Param>]\ ) |const|

The lower this value, the more the rotation gets slowed down.


----



[float<class_float>] **angular_limit/softness** = `0.9` [🔗<class_HingeJoint3D_property_angular_limit/softness>]


- |void| **set_param**\ (\ param\: [Param<enum_HingeJoint3D_Param>], value\: [float<class_float>]\ )
- [float<class_float>] **get_param**\ (\ param\: [Param<enum_HingeJoint3D_Param>]\ ) |const|

**Deprecated:** This property is never set by the engine and is kept for compatibility purposes.


----



[float<class_float>] **angular_limit/upper** = `1.5707964` [🔗<class_HingeJoint3D_property_angular_limit/upper>]


- |void| **set_param**\ (\ param\: [Param<enum_HingeJoint3D_Param>], value\: [float<class_float>]\ )
- [float<class_float>] **get_param**\ (\ param\: [Param<enum_HingeJoint3D_Param>]\ ) |const|

The maximum rotation. Only active if [angular_limit/enable<class_HingeJoint3D_property_angular_limit/enable>] is `true`.


----



[bool<class_bool>] **motor/enable** = `false` [🔗<class_HingeJoint3D_property_motor/enable>]


- |void| **set_flag**\ (\ flag\: [Flag<enum_HingeJoint3D_Flag>], enabled\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_flag**\ (\ flag\: [Flag<enum_HingeJoint3D_Flag>]\ ) |const|

When activated, a motor turns the hinge.


----



[float<class_float>] **motor/max_impulse** = `1.0` [🔗<class_HingeJoint3D_property_motor/max_impulse>]


- |void| **set_param**\ (\ param\: [Param<enum_HingeJoint3D_Param>], value\: [float<class_float>]\ )
- [float<class_float>] **get_param**\ (\ param\: [Param<enum_HingeJoint3D_Param>]\ ) |const|

Maximum acceleration for the motor.


----



[float<class_float>] **motor/target_velocity** = `1.0` [🔗<class_HingeJoint3D_property_motor/target_velocity>]


- |void| **set_param**\ (\ param\: [Param<enum_HingeJoint3D_Param>], value\: [float<class_float>]\ )
- [float<class_float>] **get_param**\ (\ param\: [Param<enum_HingeJoint3D_Param>]\ ) |const|

Target speed for the motor.


----



[float<class_float>] **params/bias** = `0.3` [🔗<class_HingeJoint3D_property_params/bias>]


- |void| **set_param**\ (\ param\: [Param<enum_HingeJoint3D_Param>], value\: [float<class_float>]\ )
- [float<class_float>] **get_param**\ (\ param\: [Param<enum_HingeJoint3D_Param>]\ ) |const|

The speed with which the two bodies get pulled together when they move in different directions.


----


## Method Descriptions



[bool<class_bool>] **get_flag**\ (\ flag\: [Flag<enum_HingeJoint3D_Flag>]\ ) |const| [🔗<class_HingeJoint3D_method_get_flag>]

Returns the value of the specified flag.


----



[float<class_float>] **get_param**\ (\ param\: [Param<enum_HingeJoint3D_Param>]\ ) |const| [🔗<class_HingeJoint3D_method_get_param>]

Returns the value of the specified parameter.


----



|void| **set_flag**\ (\ flag\: [Flag<enum_HingeJoint3D_Flag>], enabled\: [bool<class_bool>]\ ) [🔗<class_HingeJoint3D_method_set_flag>]

If `true`, enables the specified flag.


----



|void| **set_param**\ (\ param\: [Param<enum_HingeJoint3D_Param>], value\: [float<class_float>]\ ) [🔗<class_HingeJoint3D_method_set_param>]

Sets the value of the specified parameter.

