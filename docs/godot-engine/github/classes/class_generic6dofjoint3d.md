:github_url: hide



# Generic6DOFJoint3D

**Inherits:** [Joint3D<class_Joint3D>] **<** [Node3D<class_Node3D>] **<** [Node<class_Node>] **<** [Object<class_Object>]

A physics joint that allows for complex movement and rotation between two 3D physics bodies.


## Description

The **Generic6DOFJoint3D** (6 Degrees Of Freedom) joint allows for implementing custom types of joints by locking the rotation and translation of certain axes.

The first 3 DOF represent the linear motion of the physics bodies and the last 3 DOF represent the angular motion of the physics bodies. Each axis can be either locked, or limited.


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------+-----------------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>` | :ref:`angular_limit_x/damping<class_Generic6DOFJoint3D_property_angular_limit_x/damping>`                       | ``1.0``   |
> +---------------------------+-----------------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>`   | :ref:`angular_limit_x/enabled<class_Generic6DOFJoint3D_property_angular_limit_x/enabled>`                       | ``true``  |
> +---------------------------+-----------------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>` | :ref:`angular_limit_x/erp<class_Generic6DOFJoint3D_property_angular_limit_x/erp>`                               | ``0.5``   |
> +---------------------------+-----------------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>` | :ref:`angular_limit_x/force_limit<class_Generic6DOFJoint3D_property_angular_limit_x/force_limit>`               | ``0.0``   |
> +---------------------------+-----------------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>` | :ref:`angular_limit_x/lower_angle<class_Generic6DOFJoint3D_property_angular_limit_x/lower_angle>`               | ``0.0``   |
> +---------------------------+-----------------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>` | :ref:`angular_limit_x/restitution<class_Generic6DOFJoint3D_property_angular_limit_x/restitution>`               | ``0.0``   |
> +---------------------------+-----------------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>` | :ref:`angular_limit_x/softness<class_Generic6DOFJoint3D_property_angular_limit_x/softness>`                     | ``0.5``   |
> +---------------------------+-----------------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>` | :ref:`angular_limit_x/upper_angle<class_Generic6DOFJoint3D_property_angular_limit_x/upper_angle>`               | ``0.0``   |
> +---------------------------+-----------------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>` | :ref:`angular_limit_y/damping<class_Generic6DOFJoint3D_property_angular_limit_y/damping>`                       | ``1.0``   |
> +---------------------------+-----------------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>`   | :ref:`angular_limit_y/enabled<class_Generic6DOFJoint3D_property_angular_limit_y/enabled>`                       | ``true``  |
> +---------------------------+-----------------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>` | :ref:`angular_limit_y/erp<class_Generic6DOFJoint3D_property_angular_limit_y/erp>`                               | ``0.5``   |
> +---------------------------+-----------------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>` | :ref:`angular_limit_y/force_limit<class_Generic6DOFJoint3D_property_angular_limit_y/force_limit>`               | ``0.0``   |
> +---------------------------+-----------------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>` | :ref:`angular_limit_y/lower_angle<class_Generic6DOFJoint3D_property_angular_limit_y/lower_angle>`               | ``0.0``   |
> +---------------------------+-----------------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>` | :ref:`angular_limit_y/restitution<class_Generic6DOFJoint3D_property_angular_limit_y/restitution>`               | ``0.0``   |
> +---------------------------+-----------------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>` | :ref:`angular_limit_y/softness<class_Generic6DOFJoint3D_property_angular_limit_y/softness>`                     | ``0.5``   |
> +---------------------------+-----------------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>` | :ref:`angular_limit_y/upper_angle<class_Generic6DOFJoint3D_property_angular_limit_y/upper_angle>`               | ``0.0``   |
> +---------------------------+-----------------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>` | :ref:`angular_limit_z/damping<class_Generic6DOFJoint3D_property_angular_limit_z/damping>`                       | ``1.0``   |
> +---------------------------+-----------------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>`   | :ref:`angular_limit_z/enabled<class_Generic6DOFJoint3D_property_angular_limit_z/enabled>`                       | ``true``  |
> +---------------------------+-----------------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>` | :ref:`angular_limit_z/erp<class_Generic6DOFJoint3D_property_angular_limit_z/erp>`                               | ``0.5``   |
> +---------------------------+-----------------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>` | :ref:`angular_limit_z/force_limit<class_Generic6DOFJoint3D_property_angular_limit_z/force_limit>`               | ``0.0``   |
> +---------------------------+-----------------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>` | :ref:`angular_limit_z/lower_angle<class_Generic6DOFJoint3D_property_angular_limit_z/lower_angle>`               | ``0.0``   |
> +---------------------------+-----------------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>` | :ref:`angular_limit_z/restitution<class_Generic6DOFJoint3D_property_angular_limit_z/restitution>`               | ``0.0``   |
> +---------------------------+-----------------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>` | :ref:`angular_limit_z/softness<class_Generic6DOFJoint3D_property_angular_limit_z/softness>`                     | ``0.5``   |
> +---------------------------+-----------------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>` | :ref:`angular_limit_z/upper_angle<class_Generic6DOFJoint3D_property_angular_limit_z/upper_angle>`               | ``0.0``   |
> +---------------------------+-----------------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>`   | :ref:`angular_motor_x/enabled<class_Generic6DOFJoint3D_property_angular_motor_x/enabled>`                       | ``false`` |
> +---------------------------+-----------------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>` | :ref:`angular_motor_x/force_limit<class_Generic6DOFJoint3D_property_angular_motor_x/force_limit>`               | ``300.0`` |
> +---------------------------+-----------------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>` | :ref:`angular_motor_x/target_velocity<class_Generic6DOFJoint3D_property_angular_motor_x/target_velocity>`       | ``0.0``   |
> +---------------------------+-----------------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>`   | :ref:`angular_motor_y/enabled<class_Generic6DOFJoint3D_property_angular_motor_y/enabled>`                       | ``false`` |
> +---------------------------+-----------------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>` | :ref:`angular_motor_y/force_limit<class_Generic6DOFJoint3D_property_angular_motor_y/force_limit>`               | ``300.0`` |
> +---------------------------+-----------------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>` | :ref:`angular_motor_y/target_velocity<class_Generic6DOFJoint3D_property_angular_motor_y/target_velocity>`       | ``0.0``   |
> +---------------------------+-----------------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>`   | :ref:`angular_motor_z/enabled<class_Generic6DOFJoint3D_property_angular_motor_z/enabled>`                       | ``false`` |
> +---------------------------+-----------------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>` | :ref:`angular_motor_z/force_limit<class_Generic6DOFJoint3D_property_angular_motor_z/force_limit>`               | ``300.0`` |
> +---------------------------+-----------------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>` | :ref:`angular_motor_z/target_velocity<class_Generic6DOFJoint3D_property_angular_motor_z/target_velocity>`       | ``0.0``   |
> +---------------------------+-----------------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>` | :ref:`angular_spring_x/damping<class_Generic6DOFJoint3D_property_angular_spring_x/damping>`                     | ``0.0``   |
> +---------------------------+-----------------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>`   | :ref:`angular_spring_x/enabled<class_Generic6DOFJoint3D_property_angular_spring_x/enabled>`                     | ``false`` |
> +---------------------------+-----------------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>` | :ref:`angular_spring_x/equilibrium_point<class_Generic6DOFJoint3D_property_angular_spring_x/equilibrium_point>` | ``0.0``   |
> +---------------------------+-----------------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>` | :ref:`angular_spring_x/stiffness<class_Generic6DOFJoint3D_property_angular_spring_x/stiffness>`                 | ``0.0``   |
> +---------------------------+-----------------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>` | :ref:`angular_spring_y/damping<class_Generic6DOFJoint3D_property_angular_spring_y/damping>`                     | ``0.0``   |
> +---------------------------+-----------------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>`   | :ref:`angular_spring_y/enabled<class_Generic6DOFJoint3D_property_angular_spring_y/enabled>`                     | ``false`` |
> +---------------------------+-----------------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>` | :ref:`angular_spring_y/equilibrium_point<class_Generic6DOFJoint3D_property_angular_spring_y/equilibrium_point>` | ``0.0``   |
> +---------------------------+-----------------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>` | :ref:`angular_spring_y/stiffness<class_Generic6DOFJoint3D_property_angular_spring_y/stiffness>`                 | ``0.0``   |
> +---------------------------+-----------------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>` | :ref:`angular_spring_z/damping<class_Generic6DOFJoint3D_property_angular_spring_z/damping>`                     | ``0.0``   |
> +---------------------------+-----------------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>`   | :ref:`angular_spring_z/enabled<class_Generic6DOFJoint3D_property_angular_spring_z/enabled>`                     | ``false`` |
> +---------------------------+-----------------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>` | :ref:`angular_spring_z/equilibrium_point<class_Generic6DOFJoint3D_property_angular_spring_z/equilibrium_point>` | ``0.0``   |
> +---------------------------+-----------------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>` | :ref:`angular_spring_z/stiffness<class_Generic6DOFJoint3D_property_angular_spring_z/stiffness>`                 | ``0.0``   |
> +---------------------------+-----------------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>` | :ref:`linear_limit_x/damping<class_Generic6DOFJoint3D_property_linear_limit_x/damping>`                         | ``1.0``   |
> +---------------------------+-----------------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>`   | :ref:`linear_limit_x/enabled<class_Generic6DOFJoint3D_property_linear_limit_x/enabled>`                         | ``true``  |
> +---------------------------+-----------------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>` | :ref:`linear_limit_x/lower_distance<class_Generic6DOFJoint3D_property_linear_limit_x/lower_distance>`           | ``0.0``   |
> +---------------------------+-----------------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>` | :ref:`linear_limit_x/restitution<class_Generic6DOFJoint3D_property_linear_limit_x/restitution>`                 | ``0.5``   |
> +---------------------------+-----------------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>` | :ref:`linear_limit_x/softness<class_Generic6DOFJoint3D_property_linear_limit_x/softness>`                       | ``0.7``   |
> +---------------------------+-----------------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>` | :ref:`linear_limit_x/upper_distance<class_Generic6DOFJoint3D_property_linear_limit_x/upper_distance>`           | ``0.0``   |
> +---------------------------+-----------------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>` | :ref:`linear_limit_y/damping<class_Generic6DOFJoint3D_property_linear_limit_y/damping>`                         | ``1.0``   |
> +---------------------------+-----------------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>`   | :ref:`linear_limit_y/enabled<class_Generic6DOFJoint3D_property_linear_limit_y/enabled>`                         | ``true``  |
> +---------------------------+-----------------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>` | :ref:`linear_limit_y/lower_distance<class_Generic6DOFJoint3D_property_linear_limit_y/lower_distance>`           | ``0.0``   |
> +---------------------------+-----------------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>` | :ref:`linear_limit_y/restitution<class_Generic6DOFJoint3D_property_linear_limit_y/restitution>`                 | ``0.5``   |
> +---------------------------+-----------------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>` | :ref:`linear_limit_y/softness<class_Generic6DOFJoint3D_property_linear_limit_y/softness>`                       | ``0.7``   |
> +---------------------------+-----------------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>` | :ref:`linear_limit_y/upper_distance<class_Generic6DOFJoint3D_property_linear_limit_y/upper_distance>`           | ``0.0``   |
> +---------------------------+-----------------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>` | :ref:`linear_limit_z/damping<class_Generic6DOFJoint3D_property_linear_limit_z/damping>`                         | ``1.0``   |
> +---------------------------+-----------------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>`   | :ref:`linear_limit_z/enabled<class_Generic6DOFJoint3D_property_linear_limit_z/enabled>`                         | ``true``  |
> +---------------------------+-----------------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>` | :ref:`linear_limit_z/lower_distance<class_Generic6DOFJoint3D_property_linear_limit_z/lower_distance>`           | ``0.0``   |
> +---------------------------+-----------------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>` | :ref:`linear_limit_z/restitution<class_Generic6DOFJoint3D_property_linear_limit_z/restitution>`                 | ``0.5``   |
> +---------------------------+-----------------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>` | :ref:`linear_limit_z/softness<class_Generic6DOFJoint3D_property_linear_limit_z/softness>`                       | ``0.7``   |
> +---------------------------+-----------------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>` | :ref:`linear_limit_z/upper_distance<class_Generic6DOFJoint3D_property_linear_limit_z/upper_distance>`           | ``0.0``   |
> +---------------------------+-----------------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>`   | :ref:`linear_motor_x/enabled<class_Generic6DOFJoint3D_property_linear_motor_x/enabled>`                         | ``false`` |
> +---------------------------+-----------------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>` | :ref:`linear_motor_x/force_limit<class_Generic6DOFJoint3D_property_linear_motor_x/force_limit>`                 | ``0.0``   |
> +---------------------------+-----------------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>` | :ref:`linear_motor_x/target_velocity<class_Generic6DOFJoint3D_property_linear_motor_x/target_velocity>`         | ``0.0``   |
> +---------------------------+-----------------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>`   | :ref:`linear_motor_y/enabled<class_Generic6DOFJoint3D_property_linear_motor_y/enabled>`                         | ``false`` |
> +---------------------------+-----------------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>` | :ref:`linear_motor_y/force_limit<class_Generic6DOFJoint3D_property_linear_motor_y/force_limit>`                 | ``0.0``   |
> +---------------------------+-----------------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>` | :ref:`linear_motor_y/target_velocity<class_Generic6DOFJoint3D_property_linear_motor_y/target_velocity>`         | ``0.0``   |
> +---------------------------+-----------------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>`   | :ref:`linear_motor_z/enabled<class_Generic6DOFJoint3D_property_linear_motor_z/enabled>`                         | ``false`` |
> +---------------------------+-----------------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>` | :ref:`linear_motor_z/force_limit<class_Generic6DOFJoint3D_property_linear_motor_z/force_limit>`                 | ``0.0``   |
> +---------------------------+-----------------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>` | :ref:`linear_motor_z/target_velocity<class_Generic6DOFJoint3D_property_linear_motor_z/target_velocity>`         | ``0.0``   |
> +---------------------------+-----------------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>` | :ref:`linear_spring_x/damping<class_Generic6DOFJoint3D_property_linear_spring_x/damping>`                       | ``0.01``  |
> +---------------------------+-----------------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>`   | :ref:`linear_spring_x/enabled<class_Generic6DOFJoint3D_property_linear_spring_x/enabled>`                       | ``false`` |
> +---------------------------+-----------------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>` | :ref:`linear_spring_x/equilibrium_point<class_Generic6DOFJoint3D_property_linear_spring_x/equilibrium_point>`   | ``0.0``   |
> +---------------------------+-----------------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>` | :ref:`linear_spring_x/stiffness<class_Generic6DOFJoint3D_property_linear_spring_x/stiffness>`                   | ``0.01``  |
> +---------------------------+-----------------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>` | :ref:`linear_spring_y/damping<class_Generic6DOFJoint3D_property_linear_spring_y/damping>`                       | ``0.01``  |
> +---------------------------+-----------------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>`   | :ref:`linear_spring_y/enabled<class_Generic6DOFJoint3D_property_linear_spring_y/enabled>`                       | ``false`` |
> +---------------------------+-----------------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>` | :ref:`linear_spring_y/equilibrium_point<class_Generic6DOFJoint3D_property_linear_spring_y/equilibrium_point>`   | ``0.0``   |
> +---------------------------+-----------------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>` | :ref:`linear_spring_y/stiffness<class_Generic6DOFJoint3D_property_linear_spring_y/stiffness>`                   | ``0.01``  |
> +---------------------------+-----------------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>` | :ref:`linear_spring_z/damping<class_Generic6DOFJoint3D_property_linear_spring_z/damping>`                       | ``0.01``  |
> +---------------------------+-----------------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>`   | :ref:`linear_spring_z/enabled<class_Generic6DOFJoint3D_property_linear_spring_z/enabled>`                       | ``false`` |
> +---------------------------+-----------------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>` | :ref:`linear_spring_z/equilibrium_point<class_Generic6DOFJoint3D_property_linear_spring_z/equilibrium_point>`   | ``0.0``   |
> +---------------------------+-----------------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>` | :ref:`linear_spring_z/stiffness<class_Generic6DOFJoint3D_property_linear_spring_z/stiffness>`                   | ``0.01``  |
> +---------------------------+-----------------------------------------------------------------------------------------------------------------+-----------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +---------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`   | :ref:`get_flag_x<class_Generic6DOFJoint3D_method_get_flag_x>`\ (\ flag\: :ref:`Flag<enum_Generic6DOFJoint3D_Flag>`\ ) |const|                                 |
> +---------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`   | :ref:`get_flag_y<class_Generic6DOFJoint3D_method_get_flag_y>`\ (\ flag\: :ref:`Flag<enum_Generic6DOFJoint3D_Flag>`\ ) |const|                                 |
> +---------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`   | :ref:`get_flag_z<class_Generic6DOFJoint3D_method_get_flag_z>`\ (\ flag\: :ref:`Flag<enum_Generic6DOFJoint3D_Flag>`\ ) |const|                                 |
> +---------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>` | :ref:`get_param_x<class_Generic6DOFJoint3D_method_get_param_x>`\ (\ param\: :ref:`Param<enum_Generic6DOFJoint3D_Param>`\ ) |const|                            |
> +---------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>` | :ref:`get_param_y<class_Generic6DOFJoint3D_method_get_param_y>`\ (\ param\: :ref:`Param<enum_Generic6DOFJoint3D_Param>`\ ) |const|                            |
> +---------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>` | :ref:`get_param_z<class_Generic6DOFJoint3D_method_get_param_z>`\ (\ param\: :ref:`Param<enum_Generic6DOFJoint3D_Param>`\ ) |const|                            |
> +---------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                    | :ref:`set_flag_x<class_Generic6DOFJoint3D_method_set_flag_x>`\ (\ flag\: :ref:`Flag<enum_Generic6DOFJoint3D_Flag>`, value\: :ref:`bool<class_bool>`\ )        |
> +---------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                    | :ref:`set_flag_y<class_Generic6DOFJoint3D_method_set_flag_y>`\ (\ flag\: :ref:`Flag<enum_Generic6DOFJoint3D_Flag>`, value\: :ref:`bool<class_bool>`\ )        |
> +---------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                    | :ref:`set_flag_z<class_Generic6DOFJoint3D_method_set_flag_z>`\ (\ flag\: :ref:`Flag<enum_Generic6DOFJoint3D_Flag>`, value\: :ref:`bool<class_bool>`\ )        |
> +---------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                    | :ref:`set_param_x<class_Generic6DOFJoint3D_method_set_param_x>`\ (\ param\: :ref:`Param<enum_Generic6DOFJoint3D_Param>`, value\: :ref:`float<class_float>`\ ) |
> +---------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                    | :ref:`set_param_y<class_Generic6DOFJoint3D_method_set_param_y>`\ (\ param\: :ref:`Param<enum_Generic6DOFJoint3D_Param>`, value\: :ref:`float<class_float>`\ ) |
> +---------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                    | :ref:`set_param_z<class_Generic6DOFJoint3D_method_set_param_z>`\ (\ param\: :ref:`Param<enum_Generic6DOFJoint3D_Param>`, value\: :ref:`float<class_float>`\ ) |
> +---------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Enumerations



enum **Param**: [🔗<enum_Generic6DOFJoint3D_Param>]



[Param<enum_Generic6DOFJoint3D_Param>] **PARAM_LINEAR_LOWER_LIMIT** = `0`

The minimum difference between the pivot points' axes.



[Param<enum_Generic6DOFJoint3D_Param>] **PARAM_LINEAR_UPPER_LIMIT** = `1`

The maximum difference between the pivot points' axes.



[Param<enum_Generic6DOFJoint3D_Param>] **PARAM_LINEAR_LIMIT_SOFTNESS** = `2`

A factor applied to the movement across the axes. The lower, the slower the movement.



[Param<enum_Generic6DOFJoint3D_Param>] **PARAM_LINEAR_RESTITUTION** = `3`

The amount of restitution on the axes' movement. The lower, the more momentum gets lost.



[Param<enum_Generic6DOFJoint3D_Param>] **PARAM_LINEAR_DAMPING** = `4`

The amount of damping that happens at the linear motion across the axes.



[Param<enum_Generic6DOFJoint3D_Param>] **PARAM_LINEAR_MOTOR_TARGET_VELOCITY** = `5`

The velocity the linear motor will try to reach.



[Param<enum_Generic6DOFJoint3D_Param>] **PARAM_LINEAR_MOTOR_FORCE_LIMIT** = `6`

The maximum force the linear motor will apply while trying to reach the velocity target.



[Param<enum_Generic6DOFJoint3D_Param>] **PARAM_LINEAR_SPRING_STIFFNESS** = `7`

> **CONTAINER**
>
	There is currently no description for this enum. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!





[Param<enum_Generic6DOFJoint3D_Param>] **PARAM_LINEAR_SPRING_DAMPING** = `8`

> **CONTAINER**
>
	There is currently no description for this enum. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!





[Param<enum_Generic6DOFJoint3D_Param>] **PARAM_LINEAR_SPRING_EQUILIBRIUM_POINT** = `9`

> **CONTAINER**
>
	There is currently no description for this enum. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!





[Param<enum_Generic6DOFJoint3D_Param>] **PARAM_ANGULAR_LOWER_LIMIT** = `10`

The minimum rotation in negative direction to break loose and rotate around the axes.



[Param<enum_Generic6DOFJoint3D_Param>] **PARAM_ANGULAR_UPPER_LIMIT** = `11`

The minimum rotation in positive direction to break loose and rotate around the axes.



[Param<enum_Generic6DOFJoint3D_Param>] **PARAM_ANGULAR_LIMIT_SOFTNESS** = `12`

The speed of all rotations across the axes.



[Param<enum_Generic6DOFJoint3D_Param>] **PARAM_ANGULAR_DAMPING** = `13`

The amount of rotational damping across the axes. The lower, the more damping occurs.



[Param<enum_Generic6DOFJoint3D_Param>] **PARAM_ANGULAR_RESTITUTION** = `14`

The amount of rotational restitution across the axes. The lower, the more restitution occurs.



[Param<enum_Generic6DOFJoint3D_Param>] **PARAM_ANGULAR_FORCE_LIMIT** = `15`

The maximum amount of force that can occur, when rotating around the axes.



[Param<enum_Generic6DOFJoint3D_Param>] **PARAM_ANGULAR_ERP** = `16`

When rotating across the axes, this error tolerance factor defines how much the correction gets slowed down. The lower, the slower.



[Param<enum_Generic6DOFJoint3D_Param>] **PARAM_ANGULAR_MOTOR_TARGET_VELOCITY** = `17`

Target speed for the motor at the axes.



[Param<enum_Generic6DOFJoint3D_Param>] **PARAM_ANGULAR_MOTOR_FORCE_LIMIT** = `18`

Maximum acceleration for the motor at the axes.



[Param<enum_Generic6DOFJoint3D_Param>] **PARAM_ANGULAR_SPRING_STIFFNESS** = `19`

> **CONTAINER**
>
	There is currently no description for this enum. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!





[Param<enum_Generic6DOFJoint3D_Param>] **PARAM_ANGULAR_SPRING_DAMPING** = `20`

> **CONTAINER**
>
	There is currently no description for this enum. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!





[Param<enum_Generic6DOFJoint3D_Param>] **PARAM_ANGULAR_SPRING_EQUILIBRIUM_POINT** = `21`

> **CONTAINER**
>
	There is currently no description for this enum. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!





[Param<enum_Generic6DOFJoint3D_Param>] **PARAM_MAX** = `22`

Represents the size of the [Param<enum_Generic6DOFJoint3D_Param>] enum.


----



enum **Flag**: [🔗<enum_Generic6DOFJoint3D_Flag>]



[Flag<enum_Generic6DOFJoint3D_Flag>] **FLAG_ENABLE_LINEAR_LIMIT** = `0`

If enabled, linear motion is possible within the given limits.



[Flag<enum_Generic6DOFJoint3D_Flag>] **FLAG_ENABLE_ANGULAR_LIMIT** = `1`

If enabled, rotational motion is possible within the given limits.



[Flag<enum_Generic6DOFJoint3D_Flag>] **FLAG_ENABLE_LINEAR_SPRING** = `3`

> **CONTAINER**
>
	There is currently no description for this enum. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!





[Flag<enum_Generic6DOFJoint3D_Flag>] **FLAG_ENABLE_ANGULAR_SPRING** = `2`

> **CONTAINER**
>
	There is currently no description for this enum. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!





[Flag<enum_Generic6DOFJoint3D_Flag>] **FLAG_ENABLE_MOTOR** = `4`

If enabled, there is a rotational motor across these axes.



[Flag<enum_Generic6DOFJoint3D_Flag>] **FLAG_ENABLE_LINEAR_MOTOR** = `5`

If enabled, there is a linear motor across these axes.



[Flag<enum_Generic6DOFJoint3D_Flag>] **FLAG_MAX** = `6`

Represents the size of the [Flag<enum_Generic6DOFJoint3D_Flag>] enum.


----


## Property Descriptions



[float<class_float>] **angular_limit_x/damping** = `1.0` [🔗<class_Generic6DOFJoint3D_property_angular_limit_x/damping>]


- |void| **set_param_x**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>], value\: [float<class_float>]\ )
- [float<class_float>] **get_param_x**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>]\ ) |const|

The amount of rotational damping across the X axis.

The lower, the longer an impulse from one side takes to travel to the other side.


----



[bool<class_bool>] **angular_limit_x/enabled** = `true` [🔗<class_Generic6DOFJoint3D_property_angular_limit_x/enabled>]


- |void| **set_flag_x**\ (\ flag\: [Flag<enum_Generic6DOFJoint3D_Flag>], value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_flag_x**\ (\ flag\: [Flag<enum_Generic6DOFJoint3D_Flag>]\ ) |const|

If `true`, rotation across the X axis is limited.


----



[float<class_float>] **angular_limit_x/erp** = `0.5` [🔗<class_Generic6DOFJoint3D_property_angular_limit_x/erp>]


- |void| **set_param_x**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>], value\: [float<class_float>]\ )
- [float<class_float>] **get_param_x**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>]\ ) |const|

When rotating across the X axis, this error tolerance factor defines how much the correction gets slowed down. The lower, the slower.


----



[float<class_float>] **angular_limit_x/force_limit** = `0.0` [🔗<class_Generic6DOFJoint3D_property_angular_limit_x/force_limit>]


- |void| **set_param_x**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>], value\: [float<class_float>]\ )
- [float<class_float>] **get_param_x**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>]\ ) |const|

The maximum amount of force that can occur, when rotating around the X axis.


----



[float<class_float>] **angular_limit_x/lower_angle** = `0.0` [🔗<class_Generic6DOFJoint3D_property_angular_limit_x/lower_angle>]


- |void| **set_param_x**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>], value\: [float<class_float>]\ )
- [float<class_float>] **get_param_x**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>]\ ) |const|

The minimum rotation in negative direction to break loose and rotate around the X axis.


----



[float<class_float>] **angular_limit_x/restitution** = `0.0` [🔗<class_Generic6DOFJoint3D_property_angular_limit_x/restitution>]


- |void| **set_param_x**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>], value\: [float<class_float>]\ )
- [float<class_float>] **get_param_x**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>]\ ) |const|

The amount of rotational restitution across the X axis. The lower, the more restitution occurs.


----



[float<class_float>] **angular_limit_x/softness** = `0.5` [🔗<class_Generic6DOFJoint3D_property_angular_limit_x/softness>]


- |void| **set_param_x**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>], value\: [float<class_float>]\ )
- [float<class_float>] **get_param_x**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>]\ ) |const|

The speed of all rotations across the X axis.


----



[float<class_float>] **angular_limit_x/upper_angle** = `0.0` [🔗<class_Generic6DOFJoint3D_property_angular_limit_x/upper_angle>]


- |void| **set_param_x**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>], value\: [float<class_float>]\ )
- [float<class_float>] **get_param_x**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>]\ ) |const|

The minimum rotation in positive direction to break loose and rotate around the X axis.


----



[float<class_float>] **angular_limit_y/damping** = `1.0` [🔗<class_Generic6DOFJoint3D_property_angular_limit_y/damping>]


- |void| **set_param_y**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>], value\: [float<class_float>]\ )
- [float<class_float>] **get_param_y**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>]\ ) |const|

The amount of rotational damping across the Y axis. The lower, the more damping occurs.


----



[bool<class_bool>] **angular_limit_y/enabled** = `true` [🔗<class_Generic6DOFJoint3D_property_angular_limit_y/enabled>]


- |void| **set_flag_y**\ (\ flag\: [Flag<enum_Generic6DOFJoint3D_Flag>], value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_flag_y**\ (\ flag\: [Flag<enum_Generic6DOFJoint3D_Flag>]\ ) |const|

If `true`, rotation across the Y axis is limited.


----



[float<class_float>] **angular_limit_y/erp** = `0.5` [🔗<class_Generic6DOFJoint3D_property_angular_limit_y/erp>]


- |void| **set_param_y**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>], value\: [float<class_float>]\ )
- [float<class_float>] **get_param_y**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>]\ ) |const|

When rotating across the Y axis, this error tolerance factor defines how much the correction gets slowed down. The lower, the slower.


----



[float<class_float>] **angular_limit_y/force_limit** = `0.0` [🔗<class_Generic6DOFJoint3D_property_angular_limit_y/force_limit>]


- |void| **set_param_y**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>], value\: [float<class_float>]\ )
- [float<class_float>] **get_param_y**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>]\ ) |const|

The maximum amount of force that can occur, when rotating around the Y axis.


----



[float<class_float>] **angular_limit_y/lower_angle** = `0.0` [🔗<class_Generic6DOFJoint3D_property_angular_limit_y/lower_angle>]


- |void| **set_param_y**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>], value\: [float<class_float>]\ )
- [float<class_float>] **get_param_y**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>]\ ) |const|

The minimum rotation in negative direction to break loose and rotate around the Y axis.


----



[float<class_float>] **angular_limit_y/restitution** = `0.0` [🔗<class_Generic6DOFJoint3D_property_angular_limit_y/restitution>]


- |void| **set_param_y**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>], value\: [float<class_float>]\ )
- [float<class_float>] **get_param_y**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>]\ ) |const|

The amount of rotational restitution across the Y axis. The lower, the more restitution occurs.


----



[float<class_float>] **angular_limit_y/softness** = `0.5` [🔗<class_Generic6DOFJoint3D_property_angular_limit_y/softness>]


- |void| **set_param_y**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>], value\: [float<class_float>]\ )
- [float<class_float>] **get_param_y**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>]\ ) |const|

The speed of all rotations across the Y axis.


----



[float<class_float>] **angular_limit_y/upper_angle** = `0.0` [🔗<class_Generic6DOFJoint3D_property_angular_limit_y/upper_angle>]


- |void| **set_param_y**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>], value\: [float<class_float>]\ )
- [float<class_float>] **get_param_y**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>]\ ) |const|

The minimum rotation in positive direction to break loose and rotate around the Y axis.


----



[float<class_float>] **angular_limit_z/damping** = `1.0` [🔗<class_Generic6DOFJoint3D_property_angular_limit_z/damping>]


- |void| **set_param_z**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>], value\: [float<class_float>]\ )
- [float<class_float>] **get_param_z**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>]\ ) |const|

The amount of rotational damping across the Z axis. The lower, the more damping occurs.


----



[bool<class_bool>] **angular_limit_z/enabled** = `true` [🔗<class_Generic6DOFJoint3D_property_angular_limit_z/enabled>]


- |void| **set_flag_z**\ (\ flag\: [Flag<enum_Generic6DOFJoint3D_Flag>], value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_flag_z**\ (\ flag\: [Flag<enum_Generic6DOFJoint3D_Flag>]\ ) |const|

If `true`, rotation across the Z axis is limited.


----



[float<class_float>] **angular_limit_z/erp** = `0.5` [🔗<class_Generic6DOFJoint3D_property_angular_limit_z/erp>]


- |void| **set_param_z**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>], value\: [float<class_float>]\ )
- [float<class_float>] **get_param_z**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>]\ ) |const|

When rotating across the Z axis, this error tolerance factor defines how much the correction gets slowed down. The lower, the slower.


----



[float<class_float>] **angular_limit_z/force_limit** = `0.0` [🔗<class_Generic6DOFJoint3D_property_angular_limit_z/force_limit>]


- |void| **set_param_z**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>], value\: [float<class_float>]\ )
- [float<class_float>] **get_param_z**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>]\ ) |const|

The maximum amount of force that can occur, when rotating around the Z axis.


----



[float<class_float>] **angular_limit_z/lower_angle** = `0.0` [🔗<class_Generic6DOFJoint3D_property_angular_limit_z/lower_angle>]


- |void| **set_param_z**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>], value\: [float<class_float>]\ )
- [float<class_float>] **get_param_z**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>]\ ) |const|

The minimum rotation in negative direction to break loose and rotate around the Z axis.


----



[float<class_float>] **angular_limit_z/restitution** = `0.0` [🔗<class_Generic6DOFJoint3D_property_angular_limit_z/restitution>]


- |void| **set_param_z**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>], value\: [float<class_float>]\ )
- [float<class_float>] **get_param_z**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>]\ ) |const|

The amount of rotational restitution across the Z axis. The lower, the more restitution occurs.


----



[float<class_float>] **angular_limit_z/softness** = `0.5` [🔗<class_Generic6DOFJoint3D_property_angular_limit_z/softness>]


- |void| **set_param_z**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>], value\: [float<class_float>]\ )
- [float<class_float>] **get_param_z**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>]\ ) |const|

The speed of all rotations across the Z axis.


----



[float<class_float>] **angular_limit_z/upper_angle** = `0.0` [🔗<class_Generic6DOFJoint3D_property_angular_limit_z/upper_angle>]


- |void| **set_param_z**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>], value\: [float<class_float>]\ )
- [float<class_float>] **get_param_z**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>]\ ) |const|

The minimum rotation in positive direction to break loose and rotate around the Z axis.


----



[bool<class_bool>] **angular_motor_x/enabled** = `false` [🔗<class_Generic6DOFJoint3D_property_angular_motor_x/enabled>]


- |void| **set_flag_x**\ (\ flag\: [Flag<enum_Generic6DOFJoint3D_Flag>], value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_flag_x**\ (\ flag\: [Flag<enum_Generic6DOFJoint3D_Flag>]\ ) |const|

If `true`, a rotating motor at the X axis is enabled.


----



[float<class_float>] **angular_motor_x/force_limit** = `300.0` [🔗<class_Generic6DOFJoint3D_property_angular_motor_x/force_limit>]


- |void| **set_param_x**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>], value\: [float<class_float>]\ )
- [float<class_float>] **get_param_x**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>]\ ) |const|

Maximum acceleration for the motor at the X axis.


----



[float<class_float>] **angular_motor_x/target_velocity** = `0.0` [🔗<class_Generic6DOFJoint3D_property_angular_motor_x/target_velocity>]


- |void| **set_param_x**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>], value\: [float<class_float>]\ )
- [float<class_float>] **get_param_x**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>]\ ) |const|

Target speed for the motor at the X axis.


----



[bool<class_bool>] **angular_motor_y/enabled** = `false` [🔗<class_Generic6DOFJoint3D_property_angular_motor_y/enabled>]


- |void| **set_flag_y**\ (\ flag\: [Flag<enum_Generic6DOFJoint3D_Flag>], value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_flag_y**\ (\ flag\: [Flag<enum_Generic6DOFJoint3D_Flag>]\ ) |const|

If `true`, a rotating motor at the Y axis is enabled.


----



[float<class_float>] **angular_motor_y/force_limit** = `300.0` [🔗<class_Generic6DOFJoint3D_property_angular_motor_y/force_limit>]


- |void| **set_param_y**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>], value\: [float<class_float>]\ )
- [float<class_float>] **get_param_y**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>]\ ) |const|

Maximum acceleration for the motor at the Y axis.


----



[float<class_float>] **angular_motor_y/target_velocity** = `0.0` [🔗<class_Generic6DOFJoint3D_property_angular_motor_y/target_velocity>]


- |void| **set_param_y**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>], value\: [float<class_float>]\ )
- [float<class_float>] **get_param_y**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>]\ ) |const|

Target speed for the motor at the Y axis.


----



[bool<class_bool>] **angular_motor_z/enabled** = `false` [🔗<class_Generic6DOFJoint3D_property_angular_motor_z/enabled>]


- |void| **set_flag_z**\ (\ flag\: [Flag<enum_Generic6DOFJoint3D_Flag>], value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_flag_z**\ (\ flag\: [Flag<enum_Generic6DOFJoint3D_Flag>]\ ) |const|

If `true`, a rotating motor at the Z axis is enabled.


----



[float<class_float>] **angular_motor_z/force_limit** = `300.0` [🔗<class_Generic6DOFJoint3D_property_angular_motor_z/force_limit>]


- |void| **set_param_z**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>], value\: [float<class_float>]\ )
- [float<class_float>] **get_param_z**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>]\ ) |const|

Maximum acceleration for the motor at the Z axis.


----



[float<class_float>] **angular_motor_z/target_velocity** = `0.0` [🔗<class_Generic6DOFJoint3D_property_angular_motor_z/target_velocity>]


- |void| **set_param_z**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>], value\: [float<class_float>]\ )
- [float<class_float>] **get_param_z**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>]\ ) |const|

Target speed for the motor at the Z axis.


----



[float<class_float>] **angular_spring_x/damping** = `0.0` [🔗<class_Generic6DOFJoint3D_property_angular_spring_x/damping>]


- |void| **set_param_x**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>], value\: [float<class_float>]\ )
- [float<class_float>] **get_param_x**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>]\ ) |const|

> **CONTAINER**
>
	There is currently no description for this property. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[bool<class_bool>] **angular_spring_x/enabled** = `false` [🔗<class_Generic6DOFJoint3D_property_angular_spring_x/enabled>]


- |void| **set_flag_x**\ (\ flag\: [Flag<enum_Generic6DOFJoint3D_Flag>], value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_flag_x**\ (\ flag\: [Flag<enum_Generic6DOFJoint3D_Flag>]\ ) |const|

> **CONTAINER**
>
	There is currently no description for this property. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[float<class_float>] **angular_spring_x/equilibrium_point** = `0.0` [🔗<class_Generic6DOFJoint3D_property_angular_spring_x/equilibrium_point>]


- |void| **set_param_x**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>], value\: [float<class_float>]\ )
- [float<class_float>] **get_param_x**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>]\ ) |const|

> **CONTAINER**
>
	There is currently no description for this property. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[float<class_float>] **angular_spring_x/stiffness** = `0.0` [🔗<class_Generic6DOFJoint3D_property_angular_spring_x/stiffness>]


- |void| **set_param_x**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>], value\: [float<class_float>]\ )
- [float<class_float>] **get_param_x**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>]\ ) |const|

> **CONTAINER**
>
	There is currently no description for this property. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[float<class_float>] **angular_spring_y/damping** = `0.0` [🔗<class_Generic6DOFJoint3D_property_angular_spring_y/damping>]


- |void| **set_param_y**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>], value\: [float<class_float>]\ )
- [float<class_float>] **get_param_y**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>]\ ) |const|

> **CONTAINER**
>
	There is currently no description for this property. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[bool<class_bool>] **angular_spring_y/enabled** = `false` [🔗<class_Generic6DOFJoint3D_property_angular_spring_y/enabled>]


- |void| **set_flag_y**\ (\ flag\: [Flag<enum_Generic6DOFJoint3D_Flag>], value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_flag_y**\ (\ flag\: [Flag<enum_Generic6DOFJoint3D_Flag>]\ ) |const|

> **CONTAINER**
>
	There is currently no description for this property. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[float<class_float>] **angular_spring_y/equilibrium_point** = `0.0` [🔗<class_Generic6DOFJoint3D_property_angular_spring_y/equilibrium_point>]


- |void| **set_param_y**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>], value\: [float<class_float>]\ )
- [float<class_float>] **get_param_y**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>]\ ) |const|

> **CONTAINER**
>
	There is currently no description for this property. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[float<class_float>] **angular_spring_y/stiffness** = `0.0` [🔗<class_Generic6DOFJoint3D_property_angular_spring_y/stiffness>]


- |void| **set_param_y**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>], value\: [float<class_float>]\ )
- [float<class_float>] **get_param_y**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>]\ ) |const|

> **CONTAINER**
>
	There is currently no description for this property. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[float<class_float>] **angular_spring_z/damping** = `0.0` [🔗<class_Generic6DOFJoint3D_property_angular_spring_z/damping>]


- |void| **set_param_z**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>], value\: [float<class_float>]\ )
- [float<class_float>] **get_param_z**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>]\ ) |const|

> **CONTAINER**
>
	There is currently no description for this property. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[bool<class_bool>] **angular_spring_z/enabled** = `false` [🔗<class_Generic6DOFJoint3D_property_angular_spring_z/enabled>]


- |void| **set_flag_z**\ (\ flag\: [Flag<enum_Generic6DOFJoint3D_Flag>], value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_flag_z**\ (\ flag\: [Flag<enum_Generic6DOFJoint3D_Flag>]\ ) |const|

> **CONTAINER**
>
	There is currently no description for this property. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[float<class_float>] **angular_spring_z/equilibrium_point** = `0.0` [🔗<class_Generic6DOFJoint3D_property_angular_spring_z/equilibrium_point>]


- |void| **set_param_z**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>], value\: [float<class_float>]\ )
- [float<class_float>] **get_param_z**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>]\ ) |const|

> **CONTAINER**
>
	There is currently no description for this property. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[float<class_float>] **angular_spring_z/stiffness** = `0.0` [🔗<class_Generic6DOFJoint3D_property_angular_spring_z/stiffness>]


- |void| **set_param_z**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>], value\: [float<class_float>]\ )
- [float<class_float>] **get_param_z**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>]\ ) |const|

> **CONTAINER**
>
	There is currently no description for this property. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[float<class_float>] **linear_limit_x/damping** = `1.0` [🔗<class_Generic6DOFJoint3D_property_linear_limit_x/damping>]


- |void| **set_param_x**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>], value\: [float<class_float>]\ )
- [float<class_float>] **get_param_x**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>]\ ) |const|

The amount of damping that happens at the X motion.


----



[bool<class_bool>] **linear_limit_x/enabled** = `true` [🔗<class_Generic6DOFJoint3D_property_linear_limit_x/enabled>]


- |void| **set_flag_x**\ (\ flag\: [Flag<enum_Generic6DOFJoint3D_Flag>], value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_flag_x**\ (\ flag\: [Flag<enum_Generic6DOFJoint3D_Flag>]\ ) |const|

If `true`, the linear motion across the X axis is limited.


----



[float<class_float>] **linear_limit_x/lower_distance** = `0.0` [🔗<class_Generic6DOFJoint3D_property_linear_limit_x/lower_distance>]


- |void| **set_param_x**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>], value\: [float<class_float>]\ )
- [float<class_float>] **get_param_x**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>]\ ) |const|

The minimum difference between the pivot points' X axis.


----



[float<class_float>] **linear_limit_x/restitution** = `0.5` [🔗<class_Generic6DOFJoint3D_property_linear_limit_x/restitution>]


- |void| **set_param_x**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>], value\: [float<class_float>]\ )
- [float<class_float>] **get_param_x**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>]\ ) |const|

The amount of restitution on the X axis movement. The lower, the more momentum gets lost.


----



[float<class_float>] **linear_limit_x/softness** = `0.7` [🔗<class_Generic6DOFJoint3D_property_linear_limit_x/softness>]


- |void| **set_param_x**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>], value\: [float<class_float>]\ )
- [float<class_float>] **get_param_x**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>]\ ) |const|

A factor applied to the movement across the X axis. The lower, the slower the movement.


----



[float<class_float>] **linear_limit_x/upper_distance** = `0.0` [🔗<class_Generic6DOFJoint3D_property_linear_limit_x/upper_distance>]


- |void| **set_param_x**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>], value\: [float<class_float>]\ )
- [float<class_float>] **get_param_x**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>]\ ) |const|

The maximum difference between the pivot points' X axis.


----



[float<class_float>] **linear_limit_y/damping** = `1.0` [🔗<class_Generic6DOFJoint3D_property_linear_limit_y/damping>]


- |void| **set_param_y**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>], value\: [float<class_float>]\ )
- [float<class_float>] **get_param_y**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>]\ ) |const|

The amount of damping that happens at the Y motion.


----



[bool<class_bool>] **linear_limit_y/enabled** = `true` [🔗<class_Generic6DOFJoint3D_property_linear_limit_y/enabled>]


- |void| **set_flag_y**\ (\ flag\: [Flag<enum_Generic6DOFJoint3D_Flag>], value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_flag_y**\ (\ flag\: [Flag<enum_Generic6DOFJoint3D_Flag>]\ ) |const|

If `true`, the linear motion across the Y axis is limited.


----



[float<class_float>] **linear_limit_y/lower_distance** = `0.0` [🔗<class_Generic6DOFJoint3D_property_linear_limit_y/lower_distance>]


- |void| **set_param_y**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>], value\: [float<class_float>]\ )
- [float<class_float>] **get_param_y**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>]\ ) |const|

The minimum difference between the pivot points' Y axis.


----



[float<class_float>] **linear_limit_y/restitution** = `0.5` [🔗<class_Generic6DOFJoint3D_property_linear_limit_y/restitution>]


- |void| **set_param_y**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>], value\: [float<class_float>]\ )
- [float<class_float>] **get_param_y**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>]\ ) |const|

The amount of restitution on the Y axis movement. The lower, the more momentum gets lost.


----



[float<class_float>] **linear_limit_y/softness** = `0.7` [🔗<class_Generic6DOFJoint3D_property_linear_limit_y/softness>]


- |void| **set_param_y**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>], value\: [float<class_float>]\ )
- [float<class_float>] **get_param_y**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>]\ ) |const|

A factor applied to the movement across the Y axis. The lower, the slower the movement.


----



[float<class_float>] **linear_limit_y/upper_distance** = `0.0` [🔗<class_Generic6DOFJoint3D_property_linear_limit_y/upper_distance>]


- |void| **set_param_y**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>], value\: [float<class_float>]\ )
- [float<class_float>] **get_param_y**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>]\ ) |const|

The maximum difference between the pivot points' Y axis.


----



[float<class_float>] **linear_limit_z/damping** = `1.0` [🔗<class_Generic6DOFJoint3D_property_linear_limit_z/damping>]


- |void| **set_param_z**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>], value\: [float<class_float>]\ )
- [float<class_float>] **get_param_z**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>]\ ) |const|

The amount of damping that happens at the Z motion.


----



[bool<class_bool>] **linear_limit_z/enabled** = `true` [🔗<class_Generic6DOFJoint3D_property_linear_limit_z/enabled>]


- |void| **set_flag_z**\ (\ flag\: [Flag<enum_Generic6DOFJoint3D_Flag>], value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_flag_z**\ (\ flag\: [Flag<enum_Generic6DOFJoint3D_Flag>]\ ) |const|

If `true`, the linear motion across the Z axis is limited.


----



[float<class_float>] **linear_limit_z/lower_distance** = `0.0` [🔗<class_Generic6DOFJoint3D_property_linear_limit_z/lower_distance>]


- |void| **set_param_z**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>], value\: [float<class_float>]\ )
- [float<class_float>] **get_param_z**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>]\ ) |const|

The minimum difference between the pivot points' Z axis.


----



[float<class_float>] **linear_limit_z/restitution** = `0.5` [🔗<class_Generic6DOFJoint3D_property_linear_limit_z/restitution>]


- |void| **set_param_z**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>], value\: [float<class_float>]\ )
- [float<class_float>] **get_param_z**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>]\ ) |const|

The amount of restitution on the Z axis movement. The lower, the more momentum gets lost.


----



[float<class_float>] **linear_limit_z/softness** = `0.7` [🔗<class_Generic6DOFJoint3D_property_linear_limit_z/softness>]


- |void| **set_param_z**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>], value\: [float<class_float>]\ )
- [float<class_float>] **get_param_z**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>]\ ) |const|

A factor applied to the movement across the Z axis. The lower, the slower the movement.


----



[float<class_float>] **linear_limit_z/upper_distance** = `0.0` [🔗<class_Generic6DOFJoint3D_property_linear_limit_z/upper_distance>]


- |void| **set_param_z**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>], value\: [float<class_float>]\ )
- [float<class_float>] **get_param_z**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>]\ ) |const|

The maximum difference between the pivot points' Z axis.


----



[bool<class_bool>] **linear_motor_x/enabled** = `false` [🔗<class_Generic6DOFJoint3D_property_linear_motor_x/enabled>]


- |void| **set_flag_x**\ (\ flag\: [Flag<enum_Generic6DOFJoint3D_Flag>], value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_flag_x**\ (\ flag\: [Flag<enum_Generic6DOFJoint3D_Flag>]\ ) |const|

If `true`, then there is a linear motor on the X axis. It will attempt to reach the target velocity while staying within the force limits.


----



[float<class_float>] **linear_motor_x/force_limit** = `0.0` [🔗<class_Generic6DOFJoint3D_property_linear_motor_x/force_limit>]


- |void| **set_param_x**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>], value\: [float<class_float>]\ )
- [float<class_float>] **get_param_x**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>]\ ) |const|

The maximum force the linear motor can apply on the X axis while trying to reach the target velocity.


----



[float<class_float>] **linear_motor_x/target_velocity** = `0.0` [🔗<class_Generic6DOFJoint3D_property_linear_motor_x/target_velocity>]


- |void| **set_param_x**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>], value\: [float<class_float>]\ )
- [float<class_float>] **get_param_x**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>]\ ) |const|

The speed that the linear motor will attempt to reach on the X axis.


----



[bool<class_bool>] **linear_motor_y/enabled** = `false` [🔗<class_Generic6DOFJoint3D_property_linear_motor_y/enabled>]


- |void| **set_flag_y**\ (\ flag\: [Flag<enum_Generic6DOFJoint3D_Flag>], value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_flag_y**\ (\ flag\: [Flag<enum_Generic6DOFJoint3D_Flag>]\ ) |const|

If `true`, then there is a linear motor on the Y axis. It will attempt to reach the target velocity while staying within the force limits.


----



[float<class_float>] **linear_motor_y/force_limit** = `0.0` [🔗<class_Generic6DOFJoint3D_property_linear_motor_y/force_limit>]


- |void| **set_param_y**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>], value\: [float<class_float>]\ )
- [float<class_float>] **get_param_y**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>]\ ) |const|

The maximum force the linear motor can apply on the Y axis while trying to reach the target velocity.


----



[float<class_float>] **linear_motor_y/target_velocity** = `0.0` [🔗<class_Generic6DOFJoint3D_property_linear_motor_y/target_velocity>]


- |void| **set_param_y**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>], value\: [float<class_float>]\ )
- [float<class_float>] **get_param_y**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>]\ ) |const|

The speed that the linear motor will attempt to reach on the Y axis.


----



[bool<class_bool>] **linear_motor_z/enabled** = `false` [🔗<class_Generic6DOFJoint3D_property_linear_motor_z/enabled>]


- |void| **set_flag_z**\ (\ flag\: [Flag<enum_Generic6DOFJoint3D_Flag>], value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_flag_z**\ (\ flag\: [Flag<enum_Generic6DOFJoint3D_Flag>]\ ) |const|

If `true`, then there is a linear motor on the Z axis. It will attempt to reach the target velocity while staying within the force limits.


----



[float<class_float>] **linear_motor_z/force_limit** = `0.0` [🔗<class_Generic6DOFJoint3D_property_linear_motor_z/force_limit>]


- |void| **set_param_z**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>], value\: [float<class_float>]\ )
- [float<class_float>] **get_param_z**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>]\ ) |const|

The maximum force the linear motor can apply on the Z axis while trying to reach the target velocity.


----



[float<class_float>] **linear_motor_z/target_velocity** = `0.0` [🔗<class_Generic6DOFJoint3D_property_linear_motor_z/target_velocity>]


- |void| **set_param_z**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>], value\: [float<class_float>]\ )
- [float<class_float>] **get_param_z**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>]\ ) |const|

The speed that the linear motor will attempt to reach on the Z axis.


----



[float<class_float>] **linear_spring_x/damping** = `0.01` [🔗<class_Generic6DOFJoint3D_property_linear_spring_x/damping>]


- |void| **set_param_x**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>], value\: [float<class_float>]\ )
- [float<class_float>] **get_param_x**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>]\ ) |const|

> **CONTAINER**
>
	There is currently no description for this property. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[bool<class_bool>] **linear_spring_x/enabled** = `false` [🔗<class_Generic6DOFJoint3D_property_linear_spring_x/enabled>]


- |void| **set_flag_x**\ (\ flag\: [Flag<enum_Generic6DOFJoint3D_Flag>], value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_flag_x**\ (\ flag\: [Flag<enum_Generic6DOFJoint3D_Flag>]\ ) |const|

> **CONTAINER**
>
	There is currently no description for this property. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[float<class_float>] **linear_spring_x/equilibrium_point** = `0.0` [🔗<class_Generic6DOFJoint3D_property_linear_spring_x/equilibrium_point>]


- |void| **set_param_x**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>], value\: [float<class_float>]\ )
- [float<class_float>] **get_param_x**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>]\ ) |const|

> **CONTAINER**
>
	There is currently no description for this property. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[float<class_float>] **linear_spring_x/stiffness** = `0.01` [🔗<class_Generic6DOFJoint3D_property_linear_spring_x/stiffness>]


- |void| **set_param_x**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>], value\: [float<class_float>]\ )
- [float<class_float>] **get_param_x**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>]\ ) |const|

> **CONTAINER**
>
	There is currently no description for this property. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[float<class_float>] **linear_spring_y/damping** = `0.01` [🔗<class_Generic6DOFJoint3D_property_linear_spring_y/damping>]


- |void| **set_param_y**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>], value\: [float<class_float>]\ )
- [float<class_float>] **get_param_y**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>]\ ) |const|

> **CONTAINER**
>
	There is currently no description for this property. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[bool<class_bool>] **linear_spring_y/enabled** = `false` [🔗<class_Generic6DOFJoint3D_property_linear_spring_y/enabled>]


- |void| **set_flag_y**\ (\ flag\: [Flag<enum_Generic6DOFJoint3D_Flag>], value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_flag_y**\ (\ flag\: [Flag<enum_Generic6DOFJoint3D_Flag>]\ ) |const|

> **CONTAINER**
>
	There is currently no description for this property. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[float<class_float>] **linear_spring_y/equilibrium_point** = `0.0` [🔗<class_Generic6DOFJoint3D_property_linear_spring_y/equilibrium_point>]


- |void| **set_param_y**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>], value\: [float<class_float>]\ )
- [float<class_float>] **get_param_y**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>]\ ) |const|

> **CONTAINER**
>
	There is currently no description for this property. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[float<class_float>] **linear_spring_y/stiffness** = `0.01` [🔗<class_Generic6DOFJoint3D_property_linear_spring_y/stiffness>]


- |void| **set_param_y**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>], value\: [float<class_float>]\ )
- [float<class_float>] **get_param_y**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>]\ ) |const|

> **CONTAINER**
>
	There is currently no description for this property. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[float<class_float>] **linear_spring_z/damping** = `0.01` [🔗<class_Generic6DOFJoint3D_property_linear_spring_z/damping>]


- |void| **set_param_z**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>], value\: [float<class_float>]\ )
- [float<class_float>] **get_param_z**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>]\ ) |const|

> **CONTAINER**
>
	There is currently no description for this property. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[bool<class_bool>] **linear_spring_z/enabled** = `false` [🔗<class_Generic6DOFJoint3D_property_linear_spring_z/enabled>]


- |void| **set_flag_z**\ (\ flag\: [Flag<enum_Generic6DOFJoint3D_Flag>], value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_flag_z**\ (\ flag\: [Flag<enum_Generic6DOFJoint3D_Flag>]\ ) |const|

> **CONTAINER**
>
	There is currently no description for this property. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[float<class_float>] **linear_spring_z/equilibrium_point** = `0.0` [🔗<class_Generic6DOFJoint3D_property_linear_spring_z/equilibrium_point>]


- |void| **set_param_z**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>], value\: [float<class_float>]\ )
- [float<class_float>] **get_param_z**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>]\ ) |const|

> **CONTAINER**
>
	There is currently no description for this property. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[float<class_float>] **linear_spring_z/stiffness** = `0.01` [🔗<class_Generic6DOFJoint3D_property_linear_spring_z/stiffness>]


- |void| **set_param_z**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>], value\: [float<class_float>]\ )
- [float<class_float>] **get_param_z**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>]\ ) |const|

> **CONTAINER**
>
	There is currently no description for this property. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----


## Method Descriptions



[bool<class_bool>] **get_flag_x**\ (\ flag\: [Flag<enum_Generic6DOFJoint3D_Flag>]\ ) |const| [🔗<class_Generic6DOFJoint3D_method_get_flag_x>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[bool<class_bool>] **get_flag_y**\ (\ flag\: [Flag<enum_Generic6DOFJoint3D_Flag>]\ ) |const| [🔗<class_Generic6DOFJoint3D_method_get_flag_y>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[bool<class_bool>] **get_flag_z**\ (\ flag\: [Flag<enum_Generic6DOFJoint3D_Flag>]\ ) |const| [🔗<class_Generic6DOFJoint3D_method_get_flag_z>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[float<class_float>] **get_param_x**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>]\ ) |const| [🔗<class_Generic6DOFJoint3D_method_get_param_x>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[float<class_float>] **get_param_y**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>]\ ) |const| [🔗<class_Generic6DOFJoint3D_method_get_param_y>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[float<class_float>] **get_param_z**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>]\ ) |const| [🔗<class_Generic6DOFJoint3D_method_get_param_z>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



|void| **set_flag_x**\ (\ flag\: [Flag<enum_Generic6DOFJoint3D_Flag>], value\: [bool<class_bool>]\ ) [🔗<class_Generic6DOFJoint3D_method_set_flag_x>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



|void| **set_flag_y**\ (\ flag\: [Flag<enum_Generic6DOFJoint3D_Flag>], value\: [bool<class_bool>]\ ) [🔗<class_Generic6DOFJoint3D_method_set_flag_y>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



|void| **set_flag_z**\ (\ flag\: [Flag<enum_Generic6DOFJoint3D_Flag>], value\: [bool<class_bool>]\ ) [🔗<class_Generic6DOFJoint3D_method_set_flag_z>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



|void| **set_param_x**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>], value\: [float<class_float>]\ ) [🔗<class_Generic6DOFJoint3D_method_set_param_x>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



|void| **set_param_y**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>], value\: [float<class_float>]\ ) [🔗<class_Generic6DOFJoint3D_method_set_param_y>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



|void| **set_param_z**\ (\ param\: [Param<enum_Generic6DOFJoint3D_Param>], value\: [float<class_float>]\ ) [🔗<class_Generic6DOFJoint3D_method_set_param_z>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!

