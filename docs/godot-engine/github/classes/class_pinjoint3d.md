:github_url: hide



# PinJoint3D

**Inherits:** [Joint3D<class_Joint3D>] **<** [Node3D<class_Node3D>] **<** [Node<class_Node>] **<** [Object<class_Object>]

A physics joint that attaches two 3D physics bodies at a single point, allowing them to freely rotate.


## Description

A physics joint that attaches two 3D physics bodies at a single point, allowing them to freely rotate. For example, a [RigidBody3D<class_RigidBody3D>] can be attached to a [StaticBody3D<class_StaticBody3D>] to create a pendulum or a seesaw.


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------+-----------------------------------------------------------------------------+---------+
> | :ref:`float<class_float>` | :ref:`params/bias<class_PinJoint3D_property_params/bias>`                   | ``0.3`` |
> +---------------------------+-----------------------------------------------------------------------------+---------+
> | :ref:`float<class_float>` | :ref:`params/damping<class_PinJoint3D_property_params/damping>`             | ``1.0`` |
> +---------------------------+-----------------------------------------------------------------------------+---------+
> | :ref:`float<class_float>` | :ref:`params/impulse_clamp<class_PinJoint3D_property_params/impulse_clamp>` | ``0.0`` |
> +---------------------------+-----------------------------------------------------------------------------+---------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +---------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>` | :ref:`get_param<class_PinJoint3D_method_get_param>`\ (\ param\: :ref:`Param<enum_PinJoint3D_Param>`\ ) |const|                            |
> +---------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                    | :ref:`set_param<class_PinJoint3D_method_set_param>`\ (\ param\: :ref:`Param<enum_PinJoint3D_Param>`, value\: :ref:`float<class_float>`\ ) |
> +---------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Enumerations



enum **Param**: [🔗<enum_PinJoint3D_Param>]



[Param<enum_PinJoint3D_Param>] **PARAM_BIAS** = `0`

The force with which the pinned objects stay in positional relation to each other. The higher, the stronger.



[Param<enum_PinJoint3D_Param>] **PARAM_DAMPING** = `1`

The force with which the pinned objects stay in velocity relation to each other. The higher, the stronger.



[Param<enum_PinJoint3D_Param>] **PARAM_IMPULSE_CLAMP** = `2`

If above 0, this value is the maximum value for an impulse that this Joint3D produces.


----


## Property Descriptions



[float<class_float>] **params/bias** = `0.3` [🔗<class_PinJoint3D_property_params/bias>]


- |void| **set_param**\ (\ param\: [Param<enum_PinJoint3D_Param>], value\: [float<class_float>]\ )
- [float<class_float>] **get_param**\ (\ param\: [Param<enum_PinJoint3D_Param>]\ ) |const|

The force with which the pinned objects stay in positional relation to each other. The higher, the stronger.


----



[float<class_float>] **params/damping** = `1.0` [🔗<class_PinJoint3D_property_params/damping>]


- |void| **set_param**\ (\ param\: [Param<enum_PinJoint3D_Param>], value\: [float<class_float>]\ )
- [float<class_float>] **get_param**\ (\ param\: [Param<enum_PinJoint3D_Param>]\ ) |const|

The force with which the pinned objects stay in velocity relation to each other. The higher, the stronger.


----



[float<class_float>] **params/impulse_clamp** = `0.0` [🔗<class_PinJoint3D_property_params/impulse_clamp>]


- |void| **set_param**\ (\ param\: [Param<enum_PinJoint3D_Param>], value\: [float<class_float>]\ )
- [float<class_float>] **get_param**\ (\ param\: [Param<enum_PinJoint3D_Param>]\ ) |const|

If above 0, this value is the maximum value for an impulse that this Joint3D produces.


----


## Method Descriptions



[float<class_float>] **get_param**\ (\ param\: [Param<enum_PinJoint3D_Param>]\ ) |const| [🔗<class_PinJoint3D_method_get_param>]

Returns the value of the specified parameter.


----



|void| **set_param**\ (\ param\: [Param<enum_PinJoint3D_Param>], value\: [float<class_float>]\ ) [🔗<class_PinJoint3D_method_set_param>]

Sets the value of the specified parameter.

