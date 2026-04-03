# Generic6DOFJoint3D in English

# Generic6DOFJoint3D
Inherits:Joint3D<Node3D<Node<Object
A physics joint that allows for complex movement and rotation between two 3D physics bodies.

## Description
TheGeneric6DOFJoint3D(6 Degrees Of Freedom) joint allows for implementing custom types of joints by locking the rotation and translation of certain axes.
The first 3 DOF represent the linear motion of the physics bodies and the last 3 DOF represent the angular motion of the physics bodies. Each axis can be either locked, or limited.

## Properties

| float | angular_limit_x/damping | 1.0 |
|---|---|---|
| bool | angular_limit_x/enabled | true |
| float | angular_limit_x/erp | 0.5 |
| float | angular_limit_x/force_limit | 0.0 |
| float | angular_limit_x/lower_angle | 0.0 |
| float | angular_limit_x/restitution | 0.0 |
| float | angular_limit_x/softness | 0.5 |
| float | angular_limit_x/upper_angle | 0.0 |
| float | angular_limit_y/damping | 1.0 |
| bool | angular_limit_y/enabled | true |
| float | angular_limit_y/erp | 0.5 |
| float | angular_limit_y/force_limit | 0.0 |
| float | angular_limit_y/lower_angle | 0.0 |
| float | angular_limit_y/restitution | 0.0 |
| float | angular_limit_y/softness | 0.5 |
| float | angular_limit_y/upper_angle | 0.0 |
| float | angular_limit_z/damping | 1.0 |
| bool | angular_limit_z/enabled | true |
| float | angular_limit_z/erp | 0.5 |
| float | angular_limit_z/force_limit | 0.0 |
| float | angular_limit_z/lower_angle | 0.0 |
| float | angular_limit_z/restitution | 0.0 |
| float | angular_limit_z/softness | 0.5 |
| float | angular_limit_z/upper_angle | 0.0 |
| bool | angular_motor_x/enabled | false |
| float | angular_motor_x/force_limit | 300.0 |
| float | angular_motor_x/target_velocity | 0.0 |
| bool | angular_motor_y/enabled | false |
| float | angular_motor_y/force_limit | 300.0 |
| float | angular_motor_y/target_velocity | 0.0 |
| bool | angular_motor_z/enabled | false |
| float | angular_motor_z/force_limit | 300.0 |
| float | angular_motor_z/target_velocity | 0.0 |
| float | angular_spring_x/damping | 0.0 |
| bool | angular_spring_x/enabled | false |
| float | angular_spring_x/equilibrium_point | 0.0 |
| float | angular_spring_x/stiffness | 0.0 |
| float | angular_spring_y/damping | 0.0 |
| bool | angular_spring_y/enabled | false |
| float | angular_spring_y/equilibrium_point | 0.0 |
| float | angular_spring_y/stiffness | 0.0 |
| float | angular_spring_z/damping | 0.0 |
| bool | angular_spring_z/enabled | false |
| float | angular_spring_z/equilibrium_point | 0.0 |
| float | angular_spring_z/stiffness | 0.0 |
| float | linear_limit_x/damping | 1.0 |
| bool | linear_limit_x/enabled | true |
| float | linear_limit_x/lower_distance | 0.0 |
| float | linear_limit_x/restitution | 0.5 |
| float | linear_limit_x/softness | 0.7 |
| float | linear_limit_x/upper_distance | 0.0 |
| float | linear_limit_y/damping | 1.0 |
| bool | linear_limit_y/enabled | true |
| float | linear_limit_y/lower_distance | 0.0 |
| float | linear_limit_y/restitution | 0.5 |
| float | linear_limit_y/softness | 0.7 |
| float | linear_limit_y/upper_distance | 0.0 |
| float | linear_limit_z/damping | 1.0 |
| bool | linear_limit_z/enabled | true |
| float | linear_limit_z/lower_distance | 0.0 |
| float | linear_limit_z/restitution | 0.5 |
| float | linear_limit_z/softness | 0.7 |
| float | linear_limit_z/upper_distance | 0.0 |
| bool | linear_motor_x/enabled | false |
| float | linear_motor_x/force_limit | 0.0 |
| float | linear_motor_x/target_velocity | 0.0 |
| bool | linear_motor_y/enabled | false |
| float | linear_motor_y/force_limit | 0.0 |
| float | linear_motor_y/target_velocity | 0.0 |
| bool | linear_motor_z/enabled | false |
| float | linear_motor_z/force_limit | 0.0 |
| float | linear_motor_z/target_velocity | 0.0 |
| float | linear_spring_x/damping | 0.01 |
| bool | linear_spring_x/enabled | false |
| float | linear_spring_x/equilibrium_point | 0.0 |
| float | linear_spring_x/stiffness | 0.01 |
| float | linear_spring_y/damping | 0.01 |
| bool | linear_spring_y/enabled | false |
| float | linear_spring_y/equilibrium_point | 0.0 |
| float | linear_spring_y/stiffness | 0.01 |
| float | linear_spring_z/damping | 0.01 |
| bool | linear_spring_z/enabled | false |
| float | linear_spring_z/equilibrium_point | 0.0 |
| float | linear_spring_z/stiffness | 0.01 |

float
angular_limit_x/damping
bool
angular_limit_x/enabled
true
float
angular_limit_x/erp
float
angular_limit_x/force_limit
float
angular_limit_x/lower_angle
float
angular_limit_x/restitution
float
angular_limit_x/softness
float
angular_limit_x/upper_angle
float
angular_limit_y/damping
bool
angular_limit_y/enabled
true
float
angular_limit_y/erp
float
angular_limit_y/force_limit
float
angular_limit_y/lower_angle
float
angular_limit_y/restitution
float
angular_limit_y/softness
float
angular_limit_y/upper_angle
float
angular_limit_z/damping
bool
angular_limit_z/enabled
true
float
angular_limit_z/erp
float
angular_limit_z/force_limit
float
angular_limit_z/lower_angle
float
angular_limit_z/restitution
float
angular_limit_z/softness
float
angular_limit_z/upper_angle
bool
angular_motor_x/enabled
false
float
angular_motor_x/force_limit
300.0
float
angular_motor_x/target_velocity
bool
angular_motor_y/enabled
false
float
angular_motor_y/force_limit
300.0
float
angular_motor_y/target_velocity
bool
angular_motor_z/enabled
false
float
angular_motor_z/force_limit
300.0
float
angular_motor_z/target_velocity
float
angular_spring_x/damping
bool
angular_spring_x/enabled
false
float
angular_spring_x/equilibrium_point
float
angular_spring_x/stiffness
float
angular_spring_y/damping
bool
angular_spring_y/enabled
false
float
angular_spring_y/equilibrium_point
float
angular_spring_y/stiffness
float
angular_spring_z/damping
bool
angular_spring_z/enabled
false
float
angular_spring_z/equilibrium_point
float
angular_spring_z/stiffness
float
linear_limit_x/damping
bool
linear_limit_x/enabled
true
float
linear_limit_x/lower_distance
float
linear_limit_x/restitution
float
linear_limit_x/softness
float
linear_limit_x/upper_distance
float
linear_limit_y/damping
bool
linear_limit_y/enabled
true
float
linear_limit_y/lower_distance
float
linear_limit_y/restitution
float
linear_limit_y/softness
float
linear_limit_y/upper_distance
float
linear_limit_z/damping
bool
linear_limit_z/enabled
true
float
linear_limit_z/lower_distance
float
linear_limit_z/restitution
float
linear_limit_z/softness
float
linear_limit_z/upper_distance
bool
linear_motor_x/enabled
false
float
linear_motor_x/force_limit
float
linear_motor_x/target_velocity
bool
linear_motor_y/enabled
false
float
linear_motor_y/force_limit
float
linear_motor_y/target_velocity
bool
linear_motor_z/enabled
false
float
linear_motor_z/force_limit
float
linear_motor_z/target_velocity
float
linear_spring_x/damping
0.01
bool
linear_spring_x/enabled
false
float
linear_spring_x/equilibrium_point
float
linear_spring_x/stiffness
0.01
float
linear_spring_y/damping
0.01
bool
linear_spring_y/enabled
false
float
linear_spring_y/equilibrium_point
float
linear_spring_y/stiffness
0.01
float
linear_spring_z/damping
0.01
bool
linear_spring_z/enabled
false
float
linear_spring_z/equilibrium_point
float
linear_spring_z/stiffness
0.01

## Methods

| bool | get_flag_x(flag:Flag)const |
|---|---|
| bool | get_flag_y(flag:Flag)const |
| bool | get_flag_z(flag:Flag)const |
| float | get_param_x(param:Param)const |
| float | get_param_y(param:Param)const |
| float | get_param_z(param:Param)const |
| void | set_flag_x(flag:Flag, value:bool) |
| void | set_flag_y(flag:Flag, value:bool) |
| void | set_flag_z(flag:Flag, value:bool) |
| void | set_param_x(param:Param, value:float) |
| void | set_param_y(param:Param, value:float) |
| void | set_param_z(param:Param, value:float) |

bool
get_flag_x(flag:Flag)const
bool
get_flag_y(flag:Flag)const
bool
get_flag_z(flag:Flag)const
float
get_param_x(param:Param)const
float
get_param_y(param:Param)const
float
get_param_z(param:Param)const
void
set_flag_x(flag:Flag, value:bool)
void
set_flag_y(flag:Flag, value:bool)
void
set_flag_z(flag:Flag, value:bool)
void
set_param_x(param:Param, value:float)
void
set_param_y(param:Param, value:float)
void
set_param_z(param:Param, value:float)

## Enumerations
enumParam:🔗
ParamPARAM_LINEAR_LOWER_LIMIT=0
The minimum difference between the pivot points' axes.
ParamPARAM_LINEAR_UPPER_LIMIT=1
The maximum difference between the pivot points' axes.
ParamPARAM_LINEAR_LIMIT_SOFTNESS=2
A factor applied to the movement across the axes. The lower, the slower the movement.
ParamPARAM_LINEAR_RESTITUTION=3
The amount of restitution on the axes' movement. The lower, the more momentum gets lost.
ParamPARAM_LINEAR_DAMPING=4
The amount of damping that happens at the linear motion across the axes.
ParamPARAM_LINEAR_MOTOR_TARGET_VELOCITY=5
The velocity the linear motor will try to reach.
ParamPARAM_LINEAR_MOTOR_FORCE_LIMIT=6
The maximum force the linear motor will apply while trying to reach the velocity target.
ParamPARAM_LINEAR_SPRING_STIFFNESS=7
There is currently no description for this enum. Please help us bycontributing one!
ParamPARAM_LINEAR_SPRING_DAMPING=8
There is currently no description for this enum. Please help us bycontributing one!
ParamPARAM_LINEAR_SPRING_EQUILIBRIUM_POINT=9
There is currently no description for this enum. Please help us bycontributing one!
ParamPARAM_ANGULAR_LOWER_LIMIT=10
The minimum rotation in negative direction to break loose and rotate around the axes.
ParamPARAM_ANGULAR_UPPER_LIMIT=11
The minimum rotation in positive direction to break loose and rotate around the axes.
ParamPARAM_ANGULAR_LIMIT_SOFTNESS=12
The speed of all rotations across the axes.
ParamPARAM_ANGULAR_DAMPING=13
The amount of rotational damping across the axes. The lower, the more damping occurs.
ParamPARAM_ANGULAR_RESTITUTION=14
The amount of rotational restitution across the axes. The lower, the more restitution occurs.
ParamPARAM_ANGULAR_FORCE_LIMIT=15
The maximum amount of force that can occur, when rotating around the axes.
ParamPARAM_ANGULAR_ERP=16
When rotating across the axes, this error tolerance factor defines how much the correction gets slowed down. The lower, the slower.
ParamPARAM_ANGULAR_MOTOR_TARGET_VELOCITY=17
Target speed for the motor at the axes.
ParamPARAM_ANGULAR_MOTOR_FORCE_LIMIT=18
Maximum acceleration for the motor at the axes.
ParamPARAM_ANGULAR_SPRING_STIFFNESS=19
There is currently no description for this enum. Please help us bycontributing one!
ParamPARAM_ANGULAR_SPRING_DAMPING=20
There is currently no description for this enum. Please help us bycontributing one!
ParamPARAM_ANGULAR_SPRING_EQUILIBRIUM_POINT=21
There is currently no description for this enum. Please help us bycontributing one!
ParamPARAM_MAX=22
Represents the size of theParamenum.
enumFlag:🔗
FlagFLAG_ENABLE_LINEAR_LIMIT=0
If enabled, linear motion is possible within the given limits.
FlagFLAG_ENABLE_ANGULAR_LIMIT=1
If enabled, rotational motion is possible within the given limits.
FlagFLAG_ENABLE_LINEAR_SPRING=3
There is currently no description for this enum. Please help us bycontributing one!
FlagFLAG_ENABLE_ANGULAR_SPRING=2
There is currently no description for this enum. Please help us bycontributing one!
FlagFLAG_ENABLE_MOTOR=4
If enabled, there is a rotational motor across these axes.
FlagFLAG_ENABLE_LINEAR_MOTOR=5
If enabled, there is a linear motor across these axes.
FlagFLAG_MAX=6
Represents the size of theFlagenum.

## Property Descriptions
floatangular_limit_x/damping=1.0🔗
- voidset_param_x(param:Param, value:float)
voidset_param_x(param:Param, value:float)
- floatget_param_x(param:Param)const
floatget_param_x(param:Param)const
The amount of rotational damping across the X axis.
The lower, the longer an impulse from one side takes to travel to the other side.
boolangular_limit_x/enabled=true🔗
- voidset_flag_x(flag:Flag, value:bool)
voidset_flag_x(flag:Flag, value:bool)
- boolget_flag_x(flag:Flag)const
boolget_flag_x(flag:Flag)const
Iftrue, rotation across the X axis is limited.
floatangular_limit_x/erp=0.5🔗
- voidset_param_x(param:Param, value:float)
voidset_param_x(param:Param, value:float)
- floatget_param_x(param:Param)const
floatget_param_x(param:Param)const
When rotating across the X axis, this error tolerance factor defines how much the correction gets slowed down. The lower, the slower.
floatangular_limit_x/force_limit=0.0🔗
- voidset_param_x(param:Param, value:float)
voidset_param_x(param:Param, value:float)
- floatget_param_x(param:Param)const
floatget_param_x(param:Param)const
The maximum amount of force that can occur, when rotating around the X axis.
floatangular_limit_x/lower_angle=0.0🔗
- voidset_param_x(param:Param, value:float)
voidset_param_x(param:Param, value:float)
- floatget_param_x(param:Param)const
floatget_param_x(param:Param)const
The minimum rotation in negative direction to break loose and rotate around the X axis.
floatangular_limit_x/restitution=0.0🔗
- voidset_param_x(param:Param, value:float)
voidset_param_x(param:Param, value:float)
- floatget_param_x(param:Param)const
floatget_param_x(param:Param)const
The amount of rotational restitution across the X axis. The lower, the more restitution occurs.
floatangular_limit_x/softness=0.5🔗
- voidset_param_x(param:Param, value:float)
voidset_param_x(param:Param, value:float)
- floatget_param_x(param:Param)const
floatget_param_x(param:Param)const
The speed of all rotations across the X axis.
floatangular_limit_x/upper_angle=0.0🔗
- voidset_param_x(param:Param, value:float)
voidset_param_x(param:Param, value:float)
- floatget_param_x(param:Param)const
floatget_param_x(param:Param)const
The minimum rotation in positive direction to break loose and rotate around the X axis.
floatangular_limit_y/damping=1.0🔗
- voidset_param_y(param:Param, value:float)
voidset_param_y(param:Param, value:float)
- floatget_param_y(param:Param)const
floatget_param_y(param:Param)const
The amount of rotational damping across the Y axis. The lower, the more damping occurs.
boolangular_limit_y/enabled=true🔗
- voidset_flag_y(flag:Flag, value:bool)
voidset_flag_y(flag:Flag, value:bool)
- boolget_flag_y(flag:Flag)const
boolget_flag_y(flag:Flag)const
Iftrue, rotation across the Y axis is limited.
floatangular_limit_y/erp=0.5🔗
- voidset_param_y(param:Param, value:float)
voidset_param_y(param:Param, value:float)
- floatget_param_y(param:Param)const
floatget_param_y(param:Param)const
When rotating across the Y axis, this error tolerance factor defines how much the correction gets slowed down. The lower, the slower.
floatangular_limit_y/force_limit=0.0🔗
- voidset_param_y(param:Param, value:float)
voidset_param_y(param:Param, value:float)
- floatget_param_y(param:Param)const
floatget_param_y(param:Param)const
The maximum amount of force that can occur, when rotating around the Y axis.
floatangular_limit_y/lower_angle=0.0🔗
- voidset_param_y(param:Param, value:float)
voidset_param_y(param:Param, value:float)
- floatget_param_y(param:Param)const
floatget_param_y(param:Param)const
The minimum rotation in negative direction to break loose and rotate around the Y axis.
floatangular_limit_y/restitution=0.0🔗
- voidset_param_y(param:Param, value:float)
voidset_param_y(param:Param, value:float)
- floatget_param_y(param:Param)const
floatget_param_y(param:Param)const
The amount of rotational restitution across the Y axis. The lower, the more restitution occurs.
floatangular_limit_y/softness=0.5🔗
- voidset_param_y(param:Param, value:float)
voidset_param_y(param:Param, value:float)
- floatget_param_y(param:Param)const
floatget_param_y(param:Param)const
The speed of all rotations across the Y axis.
floatangular_limit_y/upper_angle=0.0🔗
- voidset_param_y(param:Param, value:float)
voidset_param_y(param:Param, value:float)
- floatget_param_y(param:Param)const
floatget_param_y(param:Param)const
The minimum rotation in positive direction to break loose and rotate around the Y axis.
floatangular_limit_z/damping=1.0🔗
- voidset_param_z(param:Param, value:float)
voidset_param_z(param:Param, value:float)
- floatget_param_z(param:Param)const
floatget_param_z(param:Param)const
The amount of rotational damping across the Z axis. The lower, the more damping occurs.
boolangular_limit_z/enabled=true🔗
- voidset_flag_z(flag:Flag, value:bool)
voidset_flag_z(flag:Flag, value:bool)
- boolget_flag_z(flag:Flag)const
boolget_flag_z(flag:Flag)const
Iftrue, rotation across the Z axis is limited.
floatangular_limit_z/erp=0.5🔗
- voidset_param_z(param:Param, value:float)
voidset_param_z(param:Param, value:float)
- floatget_param_z(param:Param)const
floatget_param_z(param:Param)const
When rotating across the Z axis, this error tolerance factor defines how much the correction gets slowed down. The lower, the slower.
floatangular_limit_z/force_limit=0.0🔗
- voidset_param_z(param:Param, value:float)
voidset_param_z(param:Param, value:float)
- floatget_param_z(param:Param)const
floatget_param_z(param:Param)const
The maximum amount of force that can occur, when rotating around the Z axis.
floatangular_limit_z/lower_angle=0.0🔗
- voidset_param_z(param:Param, value:float)
voidset_param_z(param:Param, value:float)
- floatget_param_z(param:Param)const
floatget_param_z(param:Param)const
The minimum rotation in negative direction to break loose and rotate around the Z axis.
floatangular_limit_z/restitution=0.0🔗
- voidset_param_z(param:Param, value:float)
voidset_param_z(param:Param, value:float)
- floatget_param_z(param:Param)const
floatget_param_z(param:Param)const
The amount of rotational restitution across the Z axis. The lower, the more restitution occurs.
floatangular_limit_z/softness=0.5🔗
- voidset_param_z(param:Param, value:float)
voidset_param_z(param:Param, value:float)
- floatget_param_z(param:Param)const
floatget_param_z(param:Param)const
The speed of all rotations across the Z axis.
floatangular_limit_z/upper_angle=0.0🔗
- voidset_param_z(param:Param, value:float)
voidset_param_z(param:Param, value:float)
- floatget_param_z(param:Param)const
floatget_param_z(param:Param)const
The minimum rotation in positive direction to break loose and rotate around the Z axis.
boolangular_motor_x/enabled=false🔗
- voidset_flag_x(flag:Flag, value:bool)
voidset_flag_x(flag:Flag, value:bool)
- boolget_flag_x(flag:Flag)const
boolget_flag_x(flag:Flag)const
Iftrue, a rotating motor at the X axis is enabled.
floatangular_motor_x/force_limit=300.0🔗
- voidset_param_x(param:Param, value:float)
voidset_param_x(param:Param, value:float)
- floatget_param_x(param:Param)const
floatget_param_x(param:Param)const
Maximum acceleration for the motor at the X axis.
floatangular_motor_x/target_velocity=0.0🔗
- voidset_param_x(param:Param, value:float)
voidset_param_x(param:Param, value:float)
- floatget_param_x(param:Param)const
floatget_param_x(param:Param)const
Target speed for the motor at the X axis.
boolangular_motor_y/enabled=false🔗
- voidset_flag_y(flag:Flag, value:bool)
voidset_flag_y(flag:Flag, value:bool)
- boolget_flag_y(flag:Flag)const
boolget_flag_y(flag:Flag)const
Iftrue, a rotating motor at the Y axis is enabled.
floatangular_motor_y/force_limit=300.0🔗
- voidset_param_y(param:Param, value:float)
voidset_param_y(param:Param, value:float)
- floatget_param_y(param:Param)const
floatget_param_y(param:Param)const
Maximum acceleration for the motor at the Y axis.
floatangular_motor_y/target_velocity=0.0🔗
- voidset_param_y(param:Param, value:float)
voidset_param_y(param:Param, value:float)
- floatget_param_y(param:Param)const
floatget_param_y(param:Param)const
Target speed for the motor at the Y axis.
boolangular_motor_z/enabled=false🔗
- voidset_flag_z(flag:Flag, value:bool)
voidset_flag_z(flag:Flag, value:bool)
- boolget_flag_z(flag:Flag)const
boolget_flag_z(flag:Flag)const
Iftrue, a rotating motor at the Z axis is enabled.
floatangular_motor_z/force_limit=300.0🔗
- voidset_param_z(param:Param, value:float)
voidset_param_z(param:Param, value:float)
- floatget_param_z(param:Param)const
floatget_param_z(param:Param)const
Maximum acceleration for the motor at the Z axis.
floatangular_motor_z/target_velocity=0.0🔗
- voidset_param_z(param:Param, value:float)
voidset_param_z(param:Param, value:float)
- floatget_param_z(param:Param)const
floatget_param_z(param:Param)const
Target speed for the motor at the Z axis.
floatangular_spring_x/damping=0.0🔗
- voidset_param_x(param:Param, value:float)
voidset_param_x(param:Param, value:float)
- floatget_param_x(param:Param)const
floatget_param_x(param:Param)const
There is currently no description for this property. Please help us bycontributing one!
boolangular_spring_x/enabled=false🔗
- voidset_flag_x(flag:Flag, value:bool)
voidset_flag_x(flag:Flag, value:bool)
- boolget_flag_x(flag:Flag)const
boolget_flag_x(flag:Flag)const
There is currently no description for this property. Please help us bycontributing one!
floatangular_spring_x/equilibrium_point=0.0🔗
- voidset_param_x(param:Param, value:float)
voidset_param_x(param:Param, value:float)
- floatget_param_x(param:Param)const
floatget_param_x(param:Param)const
There is currently no description for this property. Please help us bycontributing one!
floatangular_spring_x/stiffness=0.0🔗
- voidset_param_x(param:Param, value:float)
voidset_param_x(param:Param, value:float)
- floatget_param_x(param:Param)const
floatget_param_x(param:Param)const
There is currently no description for this property. Please help us bycontributing one!
floatangular_spring_y/damping=0.0🔗
- voidset_param_y(param:Param, value:float)
voidset_param_y(param:Param, value:float)
- floatget_param_y(param:Param)const
floatget_param_y(param:Param)const
There is currently no description for this property. Please help us bycontributing one!
boolangular_spring_y/enabled=false🔗
- voidset_flag_y(flag:Flag, value:bool)
voidset_flag_y(flag:Flag, value:bool)
- boolget_flag_y(flag:Flag)const
boolget_flag_y(flag:Flag)const
There is currently no description for this property. Please help us bycontributing one!
floatangular_spring_y/equilibrium_point=0.0🔗
- voidset_param_y(param:Param, value:float)
voidset_param_y(param:Param, value:float)
- floatget_param_y(param:Param)const
floatget_param_y(param:Param)const
There is currently no description for this property. Please help us bycontributing one!
floatangular_spring_y/stiffness=0.0🔗
- voidset_param_y(param:Param, value:float)
voidset_param_y(param:Param, value:float)
- floatget_param_y(param:Param)const
floatget_param_y(param:Param)const
There is currently no description for this property. Please help us bycontributing one!
floatangular_spring_z/damping=0.0🔗
- voidset_param_z(param:Param, value:float)
voidset_param_z(param:Param, value:float)
- floatget_param_z(param:Param)const
floatget_param_z(param:Param)const
There is currently no description for this property. Please help us bycontributing one!
boolangular_spring_z/enabled=false🔗
- voidset_flag_z(flag:Flag, value:bool)
voidset_flag_z(flag:Flag, value:bool)
- boolget_flag_z(flag:Flag)const
boolget_flag_z(flag:Flag)const
There is currently no description for this property. Please help us bycontributing one!
floatangular_spring_z/equilibrium_point=0.0🔗
- voidset_param_z(param:Param, value:float)
voidset_param_z(param:Param, value:float)
- floatget_param_z(param:Param)const
floatget_param_z(param:Param)const
There is currently no description for this property. Please help us bycontributing one!
floatangular_spring_z/stiffness=0.0🔗
- voidset_param_z(param:Param, value:float)
voidset_param_z(param:Param, value:float)
- floatget_param_z(param:Param)const
floatget_param_z(param:Param)const
There is currently no description for this property. Please help us bycontributing one!
floatlinear_limit_x/damping=1.0🔗
- voidset_param_x(param:Param, value:float)
voidset_param_x(param:Param, value:float)
- floatget_param_x(param:Param)const
floatget_param_x(param:Param)const
The amount of damping that happens at the X motion.
boollinear_limit_x/enabled=true🔗
- voidset_flag_x(flag:Flag, value:bool)
voidset_flag_x(flag:Flag, value:bool)
- boolget_flag_x(flag:Flag)const
boolget_flag_x(flag:Flag)const
Iftrue, the linear motion across the X axis is limited.
floatlinear_limit_x/lower_distance=0.0🔗
- voidset_param_x(param:Param, value:float)
voidset_param_x(param:Param, value:float)
- floatget_param_x(param:Param)const
floatget_param_x(param:Param)const
The minimum difference between the pivot points' X axis.
floatlinear_limit_x/restitution=0.5🔗
- voidset_param_x(param:Param, value:float)
voidset_param_x(param:Param, value:float)
- floatget_param_x(param:Param)const
floatget_param_x(param:Param)const
The amount of restitution on the X axis movement. The lower, the more momentum gets lost.
floatlinear_limit_x/softness=0.7🔗
- voidset_param_x(param:Param, value:float)
voidset_param_x(param:Param, value:float)
- floatget_param_x(param:Param)const
floatget_param_x(param:Param)const
A factor applied to the movement across the X axis. The lower, the slower the movement.
floatlinear_limit_x/upper_distance=0.0🔗
- voidset_param_x(param:Param, value:float)
voidset_param_x(param:Param, value:float)
- floatget_param_x(param:Param)const
floatget_param_x(param:Param)const
The maximum difference between the pivot points' X axis.
floatlinear_limit_y/damping=1.0🔗
- voidset_param_y(param:Param, value:float)
voidset_param_y(param:Param, value:float)
- floatget_param_y(param:Param)const
floatget_param_y(param:Param)const
The amount of damping that happens at the Y motion.
boollinear_limit_y/enabled=true🔗
- voidset_flag_y(flag:Flag, value:bool)
voidset_flag_y(flag:Flag, value:bool)
- boolget_flag_y(flag:Flag)const
boolget_flag_y(flag:Flag)const
Iftrue, the linear motion across the Y axis is limited.
floatlinear_limit_y/lower_distance=0.0🔗
- voidset_param_y(param:Param, value:float)
voidset_param_y(param:Param, value:float)
- floatget_param_y(param:Param)const
floatget_param_y(param:Param)const
The minimum difference between the pivot points' Y axis.
floatlinear_limit_y/restitution=0.5🔗
- voidset_param_y(param:Param, value:float)
voidset_param_y(param:Param, value:float)
- floatget_param_y(param:Param)const
floatget_param_y(param:Param)const
The amount of restitution on the Y axis movement. The lower, the more momentum gets lost.
floatlinear_limit_y/softness=0.7🔗
- voidset_param_y(param:Param, value:float)
voidset_param_y(param:Param, value:float)
- floatget_param_y(param:Param)const
floatget_param_y(param:Param)const
A factor applied to the movement across the Y axis. The lower, the slower the movement.
floatlinear_limit_y/upper_distance=0.0🔗
- voidset_param_y(param:Param, value:float)
voidset_param_y(param:Param, value:float)
- floatget_param_y(param:Param)const
floatget_param_y(param:Param)const
The maximum difference between the pivot points' Y axis.
floatlinear_limit_z/damping=1.0🔗
- voidset_param_z(param:Param, value:float)
voidset_param_z(param:Param, value:float)
- floatget_param_z(param:Param)const
floatget_param_z(param:Param)const
The amount of damping that happens at the Z motion.
boollinear_limit_z/enabled=true🔗
- voidset_flag_z(flag:Flag, value:bool)
voidset_flag_z(flag:Flag, value:bool)
- boolget_flag_z(flag:Flag)const
boolget_flag_z(flag:Flag)const
Iftrue, the linear motion across the Z axis is limited.
floatlinear_limit_z/lower_distance=0.0🔗
- voidset_param_z(param:Param, value:float)
voidset_param_z(param:Param, value:float)
- floatget_param_z(param:Param)const
floatget_param_z(param:Param)const
The minimum difference between the pivot points' Z axis.
floatlinear_limit_z/restitution=0.5🔗
- voidset_param_z(param:Param, value:float)
voidset_param_z(param:Param, value:float)
- floatget_param_z(param:Param)const
floatget_param_z(param:Param)const
The amount of restitution on the Z axis movement. The lower, the more momentum gets lost.
floatlinear_limit_z/softness=0.7🔗
- voidset_param_z(param:Param, value:float)
voidset_param_z(param:Param, value:float)
- floatget_param_z(param:Param)const
floatget_param_z(param:Param)const
A factor applied to the movement across the Z axis. The lower, the slower the movement.
floatlinear_limit_z/upper_distance=0.0🔗
- voidset_param_z(param:Param, value:float)
voidset_param_z(param:Param, value:float)
- floatget_param_z(param:Param)const
floatget_param_z(param:Param)const
The maximum difference between the pivot points' Z axis.
boollinear_motor_x/enabled=false🔗
- voidset_flag_x(flag:Flag, value:bool)
voidset_flag_x(flag:Flag, value:bool)
- boolget_flag_x(flag:Flag)const
boolget_flag_x(flag:Flag)const
Iftrue, then there is a linear motor on the X axis. It will attempt to reach the target velocity while staying within the force limits.
floatlinear_motor_x/force_limit=0.0🔗
- voidset_param_x(param:Param, value:float)
voidset_param_x(param:Param, value:float)
- floatget_param_x(param:Param)const
floatget_param_x(param:Param)const
The maximum force the linear motor can apply on the X axis while trying to reach the target velocity.
floatlinear_motor_x/target_velocity=0.0🔗
- voidset_param_x(param:Param, value:float)
voidset_param_x(param:Param, value:float)
- floatget_param_x(param:Param)const
floatget_param_x(param:Param)const
The speed that the linear motor will attempt to reach on the X axis.
boollinear_motor_y/enabled=false🔗
- voidset_flag_y(flag:Flag, value:bool)
voidset_flag_y(flag:Flag, value:bool)
- boolget_flag_y(flag:Flag)const
boolget_flag_y(flag:Flag)const
Iftrue, then there is a linear motor on the Y axis. It will attempt to reach the target velocity while staying within the force limits.
floatlinear_motor_y/force_limit=0.0🔗
- voidset_param_y(param:Param, value:float)
voidset_param_y(param:Param, value:float)
- floatget_param_y(param:Param)const
floatget_param_y(param:Param)const
The maximum force the linear motor can apply on the Y axis while trying to reach the target velocity.
floatlinear_motor_y/target_velocity=0.0🔗
- voidset_param_y(param:Param, value:float)
voidset_param_y(param:Param, value:float)
- floatget_param_y(param:Param)const
floatget_param_y(param:Param)const
The speed that the linear motor will attempt to reach on the Y axis.
boollinear_motor_z/enabled=false🔗
- voidset_flag_z(flag:Flag, value:bool)
voidset_flag_z(flag:Flag, value:bool)
- boolget_flag_z(flag:Flag)const
boolget_flag_z(flag:Flag)const
Iftrue, then there is a linear motor on the Z axis. It will attempt to reach the target velocity while staying within the force limits.
floatlinear_motor_z/force_limit=0.0🔗
- voidset_param_z(param:Param, value:float)
voidset_param_z(param:Param, value:float)
- floatget_param_z(param:Param)const
floatget_param_z(param:Param)const
The maximum force the linear motor can apply on the Z axis while trying to reach the target velocity.
floatlinear_motor_z/target_velocity=0.0🔗
- voidset_param_z(param:Param, value:float)
voidset_param_z(param:Param, value:float)
- floatget_param_z(param:Param)const
floatget_param_z(param:Param)const
The speed that the linear motor will attempt to reach on the Z axis.
floatlinear_spring_x/damping=0.01🔗
- voidset_param_x(param:Param, value:float)
voidset_param_x(param:Param, value:float)
- floatget_param_x(param:Param)const
floatget_param_x(param:Param)const
There is currently no description for this property. Please help us bycontributing one!
boollinear_spring_x/enabled=false🔗
- voidset_flag_x(flag:Flag, value:bool)
voidset_flag_x(flag:Flag, value:bool)
- boolget_flag_x(flag:Flag)const
boolget_flag_x(flag:Flag)const
There is currently no description for this property. Please help us bycontributing one!
floatlinear_spring_x/equilibrium_point=0.0🔗
- voidset_param_x(param:Param, value:float)
voidset_param_x(param:Param, value:float)
- floatget_param_x(param:Param)const
floatget_param_x(param:Param)const
There is currently no description for this property. Please help us bycontributing one!
floatlinear_spring_x/stiffness=0.01🔗
- voidset_param_x(param:Param, value:float)
voidset_param_x(param:Param, value:float)
- floatget_param_x(param:Param)const
floatget_param_x(param:Param)const
There is currently no description for this property. Please help us bycontributing one!
floatlinear_spring_y/damping=0.01🔗
- voidset_param_y(param:Param, value:float)
voidset_param_y(param:Param, value:float)
- floatget_param_y(param:Param)const
floatget_param_y(param:Param)const
There is currently no description for this property. Please help us bycontributing one!
boollinear_spring_y/enabled=false🔗
- voidset_flag_y(flag:Flag, value:bool)
voidset_flag_y(flag:Flag, value:bool)
- boolget_flag_y(flag:Flag)const
boolget_flag_y(flag:Flag)const
There is currently no description for this property. Please help us bycontributing one!
floatlinear_spring_y/equilibrium_point=0.0🔗
- voidset_param_y(param:Param, value:float)
voidset_param_y(param:Param, value:float)
- floatget_param_y(param:Param)const
floatget_param_y(param:Param)const
There is currently no description for this property. Please help us bycontributing one!
floatlinear_spring_y/stiffness=0.01🔗
- voidset_param_y(param:Param, value:float)
voidset_param_y(param:Param, value:float)
- floatget_param_y(param:Param)const
floatget_param_y(param:Param)const
There is currently no description for this property. Please help us bycontributing one!
floatlinear_spring_z/damping=0.01🔗
- voidset_param_z(param:Param, value:float)
voidset_param_z(param:Param, value:float)
- floatget_param_z(param:Param)const
floatget_param_z(param:Param)const
There is currently no description for this property. Please help us bycontributing one!
boollinear_spring_z/enabled=false🔗
- voidset_flag_z(flag:Flag, value:bool)
voidset_flag_z(flag:Flag, value:bool)
- boolget_flag_z(flag:Flag)const
boolget_flag_z(flag:Flag)const
There is currently no description for this property. Please help us bycontributing one!
floatlinear_spring_z/equilibrium_point=0.0🔗
- voidset_param_z(param:Param, value:float)
voidset_param_z(param:Param, value:float)
- floatget_param_z(param:Param)const
floatget_param_z(param:Param)const
There is currently no description for this property. Please help us bycontributing one!
floatlinear_spring_z/stiffness=0.01🔗
- voidset_param_z(param:Param, value:float)
voidset_param_z(param:Param, value:float)
- floatget_param_z(param:Param)const
floatget_param_z(param:Param)const
There is currently no description for this property. Please help us bycontributing one!

## Method Descriptions
boolget_flag_x(flag:Flag)const🔗
There is currently no description for this method. Please help us bycontributing one!
boolget_flag_y(flag:Flag)const🔗
There is currently no description for this method. Please help us bycontributing one!
boolget_flag_z(flag:Flag)const🔗
There is currently no description for this method. Please help us bycontributing one!
floatget_param_x(param:Param)const🔗
There is currently no description for this method. Please help us bycontributing one!
floatget_param_y(param:Param)const🔗
There is currently no description for this method. Please help us bycontributing one!
floatget_param_z(param:Param)const🔗
There is currently no description for this method. Please help us bycontributing one!
voidset_flag_x(flag:Flag, value:bool)🔗
There is currently no description for this method. Please help us bycontributing one!
voidset_flag_y(flag:Flag, value:bool)🔗
There is currently no description for this method. Please help us bycontributing one!
voidset_flag_z(flag:Flag, value:bool)🔗
There is currently no description for this method. Please help us bycontributing one!
voidset_param_x(param:Param, value:float)🔗
There is currently no description for this method. Please help us bycontributing one!
voidset_param_y(param:Param, value:float)🔗
There is currently no description for this method. Please help us bycontributing one!
voidset_param_z(param:Param, value:float)🔗
There is currently no description for this method. Please help us bycontributing one!

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.