:github_url: hide



# ConeTwistJoint3D

**Inherits:** [Joint3D<class_Joint3D>] **<** [Node3D<class_Node3D>] **<** [Node<class_Node>] **<** [Object<class_Object>]

A physics joint that connects two 3D physics bodies in a way that simulates a ball-and-socket joint.


## Description

A physics joint that connects two 3D physics bodies in a way that simulates a ball-and-socket joint. The twist axis is initiated as the X axis of the **ConeTwistJoint3D**. Once the physics bodies swing, the twist axis is calculated as the middle of the X axes of the joint in the local space of the two physics bodies. Useful for limbs like shoulders and hips, lamps hanging off a ceiling, etc.


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------+---------------------------------------------------------------+---------------+
> | :ref:`float<class_float>` | :ref:`bias<class_ConeTwistJoint3D_property_bias>`             | ``0.3``       |
> +---------------------------+---------------------------------------------------------------+---------------+
> | :ref:`float<class_float>` | :ref:`relaxation<class_ConeTwistJoint3D_property_relaxation>` | ``1.0``       |
> +---------------------------+---------------------------------------------------------------+---------------+
> | :ref:`float<class_float>` | :ref:`softness<class_ConeTwistJoint3D_property_softness>`     | ``0.8``       |
> +---------------------------+---------------------------------------------------------------+---------------+
> | :ref:`float<class_float>` | :ref:`swing_span<class_ConeTwistJoint3D_property_swing_span>` | ``0.7853982`` |
> +---------------------------+---------------------------------------------------------------+---------------+
> | :ref:`float<class_float>` | :ref:`twist_span<class_ConeTwistJoint3D_property_twist_span>` | ``3.1415927`` |
> +---------------------------+---------------------------------------------------------------+---------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +---------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>` | :ref:`get_param<class_ConeTwistJoint3D_method_get_param>`\ (\ param\: :ref:`Param<enum_ConeTwistJoint3D_Param>`\ ) |const|                            |
> +---------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                    | :ref:`set_param<class_ConeTwistJoint3D_method_set_param>`\ (\ param\: :ref:`Param<enum_ConeTwistJoint3D_Param>`, value\: :ref:`float<class_float>`\ ) |
> +---------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Enumerations



enum **Param**: [🔗<enum_ConeTwistJoint3D_Param>]



[Param<enum_ConeTwistJoint3D_Param>] **PARAM_SWING_SPAN** = `0`

Swing is rotation from side to side, around the axis perpendicular to the twist axis.

The swing span defines, how much rotation will not get corrected along the swing axis.

Could be defined as looseness in the **ConeTwistJoint3D**.

If below 0.05, this behavior is locked.



[Param<enum_ConeTwistJoint3D_Param>] **PARAM_TWIST_SPAN** = `1`

Twist is the rotation around the twist axis, this value defined how far the joint can twist.

Twist is locked if below 0.05.



[Param<enum_ConeTwistJoint3D_Param>] **PARAM_BIAS** = `2`

The speed with which the swing or twist will take place.

The higher, the faster.



[Param<enum_ConeTwistJoint3D_Param>] **PARAM_SOFTNESS** = `3`

The ease with which the joint starts to twist. If it's too low, it takes more force to start twisting the joint.



[Param<enum_ConeTwistJoint3D_Param>] **PARAM_RELAXATION** = `4`

Defines, how fast the swing- and twist-speed-difference on both sides gets synced.



[Param<enum_ConeTwistJoint3D_Param>] **PARAM_MAX** = `5`

Represents the size of the [Param<enum_ConeTwistJoint3D_Param>] enum.


----


## Property Descriptions



[float<class_float>] **bias** = `0.3` [🔗<class_ConeTwistJoint3D_property_bias>]


- |void| **set_param**\ (\ param\: [Param<enum_ConeTwistJoint3D_Param>], value\: [float<class_float>]\ )
- [float<class_float>] **get_param**\ (\ param\: [Param<enum_ConeTwistJoint3D_Param>]\ ) |const|

The speed with which the swing or twist will take place.

The higher, the faster.


----



[float<class_float>] **relaxation** = `1.0` [🔗<class_ConeTwistJoint3D_property_relaxation>]


- |void| **set_param**\ (\ param\: [Param<enum_ConeTwistJoint3D_Param>], value\: [float<class_float>]\ )
- [float<class_float>] **get_param**\ (\ param\: [Param<enum_ConeTwistJoint3D_Param>]\ ) |const|

Defines, how fast the swing- and twist-speed-difference on both sides gets synced.


----



[float<class_float>] **softness** = `0.8` [🔗<class_ConeTwistJoint3D_property_softness>]


- |void| **set_param**\ (\ param\: [Param<enum_ConeTwistJoint3D_Param>], value\: [float<class_float>]\ )
- [float<class_float>] **get_param**\ (\ param\: [Param<enum_ConeTwistJoint3D_Param>]\ ) |const|

The ease with which the joint starts to twist. If it's too low, it takes more force to start twisting the joint.


----



[float<class_float>] **swing_span** = `0.7853982` [🔗<class_ConeTwistJoint3D_property_swing_span>]


- |void| **set_param**\ (\ param\: [Param<enum_ConeTwistJoint3D_Param>], value\: [float<class_float>]\ )
- [float<class_float>] **get_param**\ (\ param\: [Param<enum_ConeTwistJoint3D_Param>]\ ) |const|

Swing is rotation from side to side, around the axis perpendicular to the twist axis.

The swing span defines, how much rotation will not get corrected along the swing axis.

Could be defined as looseness in the **ConeTwistJoint3D**.

If below 0.05, this behavior is locked.


----



[float<class_float>] **twist_span** = `3.1415927` [🔗<class_ConeTwistJoint3D_property_twist_span>]


- |void| **set_param**\ (\ param\: [Param<enum_ConeTwistJoint3D_Param>], value\: [float<class_float>]\ )
- [float<class_float>] **get_param**\ (\ param\: [Param<enum_ConeTwistJoint3D_Param>]\ ) |const|

Twist is the rotation around the twist axis, this value defined how far the joint can twist.

Twist is locked if below 0.05.


----


## Method Descriptions



[float<class_float>] **get_param**\ (\ param\: [Param<enum_ConeTwistJoint3D_Param>]\ ) |const| [🔗<class_ConeTwistJoint3D_method_get_param>]

Returns the value of the specified parameter.


----



|void| **set_param**\ (\ param\: [Param<enum_ConeTwistJoint3D_Param>], value\: [float<class_float>]\ ) [🔗<class_ConeTwistJoint3D_method_set_param>]

Sets the value of the specified parameter.

