# SliderJoint3D in English

# SliderJoint3D
Inherits:Joint3D<Node3D<Node<Object
A physics joint that restricts the movement of a 3D physics body along an axis relative to another physics body.

## Description
A physics joint that restricts the movement of a 3D physics body along an axis relative to another physics body. For example, Body A could be aStaticBody3Drepresenting a piston base, while Body B could be aRigidBody3Drepresenting the piston head, moving up and down.

## Properties

| float | angular_limit/damping | 0.0 |
|---|---|---|
| float | angular_limit/lower_angle | 0.0 |
| float | angular_limit/restitution | 0.7 |
| float | angular_limit/softness | 1.0 |
| float | angular_limit/upper_angle | 0.0 |
| float | angular_motion/damping | 1.0 |
| float | angular_motion/restitution | 0.7 |
| float | angular_motion/softness | 1.0 |
| float | angular_ortho/damping | 1.0 |
| float | angular_ortho/restitution | 0.7 |
| float | angular_ortho/softness | 1.0 |
| float | linear_limit/damping | 1.0 |
| float | linear_limit/lower_distance | -1.0 |
| float | linear_limit/restitution | 0.7 |
| float | linear_limit/softness | 1.0 |
| float | linear_limit/upper_distance | 1.0 |
| float | linear_motion/damping | 0.0 |
| float | linear_motion/restitution | 0.7 |
| float | linear_motion/softness | 1.0 |
| float | linear_ortho/damping | 1.0 |
| float | linear_ortho/restitution | 0.7 |
| float | linear_ortho/softness | 1.0 |

float
angular_limit/damping
float
angular_limit/lower_angle
float
angular_limit/restitution
float
angular_limit/softness
float
angular_limit/upper_angle
float
angular_motion/damping
float
angular_motion/restitution
float
angular_motion/softness
float
angular_ortho/damping
float
angular_ortho/restitution
float
angular_ortho/softness
float
linear_limit/damping
float
linear_limit/lower_distance
-1.0
float
linear_limit/restitution
float
linear_limit/softness
float
linear_limit/upper_distance
float
linear_motion/damping
float
linear_motion/restitution
float
linear_motion/softness
float
linear_ortho/damping
float
linear_ortho/restitution
float
linear_ortho/softness

## Methods

| float | get_param(param:Param)const |
|---|---|
| void | set_param(param:Param, value:float) |

float
get_param(param:Param)const
void
set_param(param:Param, value:float)

## Enumerations
enumParam:🔗
ParamPARAM_LINEAR_LIMIT_UPPER=0
Constant for accessinglinear_limit/upper_distance. The maximum difference between the pivot points on their X axis before damping happens.
ParamPARAM_LINEAR_LIMIT_LOWER=1
Constant for accessinglinear_limit/lower_distance. The minimum difference between the pivot points on their X axis before damping happens.
ParamPARAM_LINEAR_LIMIT_SOFTNESS=2
Constant for accessinglinear_limit/softness. A factor applied to the movement across the slider axis once the limits get surpassed. The lower, the slower the movement.
ParamPARAM_LINEAR_LIMIT_RESTITUTION=3
Constant for accessinglinear_limit/restitution. The amount of restitution once the limits are surpassed. The lower, the more velocity-energy gets lost.
ParamPARAM_LINEAR_LIMIT_DAMPING=4
Constant for accessinglinear_limit/damping. The amount of damping once the slider limits are surpassed.
ParamPARAM_LINEAR_MOTION_SOFTNESS=5
Constant for accessinglinear_motion/softness. A factor applied to the movement across the slider axis as long as the slider is in the limits. The lower, the slower the movement.
ParamPARAM_LINEAR_MOTION_RESTITUTION=6
Constant for accessinglinear_motion/restitution. The amount of restitution inside the slider limits.
ParamPARAM_LINEAR_MOTION_DAMPING=7
Constant for accessinglinear_motion/damping. The amount of damping inside the slider limits.
ParamPARAM_LINEAR_ORTHOGONAL_SOFTNESS=8
Constant for accessinglinear_ortho/softness. A factor applied to the movement across axes orthogonal to the slider.
ParamPARAM_LINEAR_ORTHOGONAL_RESTITUTION=9
Constant for accessinglinear_motion/restitution. The amount of restitution when movement is across axes orthogonal to the slider.
ParamPARAM_LINEAR_ORTHOGONAL_DAMPING=10
Constant for accessinglinear_motion/damping. The amount of damping when movement is across axes orthogonal to the slider.
ParamPARAM_ANGULAR_LIMIT_UPPER=11
Constant for accessingangular_limit/upper_angle. The upper limit of rotation in the slider.
ParamPARAM_ANGULAR_LIMIT_LOWER=12
Constant for accessingangular_limit/lower_angle. The lower limit of rotation in the slider.
ParamPARAM_ANGULAR_LIMIT_SOFTNESS=13
Constant for accessingangular_limit/softness. A factor applied to the all rotation once the limit is surpassed.
ParamPARAM_ANGULAR_LIMIT_RESTITUTION=14
Constant for accessingangular_limit/restitution. The amount of restitution of the rotation when the limit is surpassed.
ParamPARAM_ANGULAR_LIMIT_DAMPING=15
Constant for accessingangular_limit/damping. The amount of damping of the rotation when the limit is surpassed.
ParamPARAM_ANGULAR_MOTION_SOFTNESS=16
Constant for accessingangular_motion/softness. A factor applied to the all rotation in the limits.
ParamPARAM_ANGULAR_MOTION_RESTITUTION=17
Constant for accessingangular_motion/restitution. The amount of restitution of the rotation in the limits.
ParamPARAM_ANGULAR_MOTION_DAMPING=18
Constant for accessingangular_motion/damping. The amount of damping of the rotation in the limits.
ParamPARAM_ANGULAR_ORTHOGONAL_SOFTNESS=19
Constant for accessingangular_ortho/softness. A factor applied to the all rotation across axes orthogonal to the slider.
ParamPARAM_ANGULAR_ORTHOGONAL_RESTITUTION=20
Constant for accessingangular_ortho/restitution. The amount of restitution of the rotation across axes orthogonal to the slider.
ParamPARAM_ANGULAR_ORTHOGONAL_DAMPING=21
Constant for accessingangular_ortho/damping. The amount of damping of the rotation across axes orthogonal to the slider.
ParamPARAM_MAX=22
Represents the size of theParamenum.

## Property Descriptions
floatangular_limit/damping=0.0🔗
- voidset_param(param:Param, value:float)
voidset_param(param:Param, value:float)
- floatget_param(param:Param)const
floatget_param(param:Param)const
The amount of damping of the rotation when the limit is surpassed.
A lower damping value allows a rotation initiated by body A to travel to body B slower.
floatangular_limit/lower_angle=0.0🔗
- voidset_param(param:Param, value:float)
voidset_param(param:Param, value:float)
- floatget_param(param:Param)const
floatget_param(param:Param)const
The lower limit of rotation in the slider.
floatangular_limit/restitution=0.7🔗
- voidset_param(param:Param, value:float)
voidset_param(param:Param, value:float)
- floatget_param(param:Param)const
floatget_param(param:Param)const
The amount of restitution of the rotation when the limit is surpassed.
Does not affect damping.
floatangular_limit/softness=1.0🔗
- voidset_param(param:Param, value:float)
voidset_param(param:Param, value:float)
- floatget_param(param:Param)const
floatget_param(param:Param)const
A factor applied to the all rotation once the limit is surpassed.
Makes all rotation slower when between 0 and 1.
floatangular_limit/upper_angle=0.0🔗
- voidset_param(param:Param, value:float)
voidset_param(param:Param, value:float)
- floatget_param(param:Param)const
floatget_param(param:Param)const
The upper limit of rotation in the slider.
floatangular_motion/damping=1.0🔗
- voidset_param(param:Param, value:float)
voidset_param(param:Param, value:float)
- floatget_param(param:Param)const
floatget_param(param:Param)const
The amount of damping of the rotation in the limits.
floatangular_motion/restitution=0.7🔗
- voidset_param(param:Param, value:float)
voidset_param(param:Param, value:float)
- floatget_param(param:Param)const
floatget_param(param:Param)const
The amount of restitution of the rotation in the limits.
floatangular_motion/softness=1.0🔗
- voidset_param(param:Param, value:float)
voidset_param(param:Param, value:float)
- floatget_param(param:Param)const
floatget_param(param:Param)const
A factor applied to the all rotation in the limits.
floatangular_ortho/damping=1.0🔗
- voidset_param(param:Param, value:float)
voidset_param(param:Param, value:float)
- floatget_param(param:Param)const
floatget_param(param:Param)const
The amount of damping of the rotation across axes orthogonal to the slider.
floatangular_ortho/restitution=0.7🔗
- voidset_param(param:Param, value:float)
voidset_param(param:Param, value:float)
- floatget_param(param:Param)const
floatget_param(param:Param)const
The amount of restitution of the rotation across axes orthogonal to the slider.
floatangular_ortho/softness=1.0🔗
- voidset_param(param:Param, value:float)
voidset_param(param:Param, value:float)
- floatget_param(param:Param)const
floatget_param(param:Param)const
A factor applied to the all rotation across axes orthogonal to the slider.
floatlinear_limit/damping=1.0🔗
- voidset_param(param:Param, value:float)
voidset_param(param:Param, value:float)
- floatget_param(param:Param)const
floatget_param(param:Param)const
The amount of damping that happens once the limit defined bylinear_limit/lower_distanceandlinear_limit/upper_distanceis surpassed.
floatlinear_limit/lower_distance=-1.0🔗
- voidset_param(param:Param, value:float)
voidset_param(param:Param, value:float)
- floatget_param(param:Param)const
floatget_param(param:Param)const
The minimum difference between the pivot points on their X axis before damping happens.
floatlinear_limit/restitution=0.7🔗
- voidset_param(param:Param, value:float)
voidset_param(param:Param, value:float)
- floatget_param(param:Param)const
floatget_param(param:Param)const
The amount of restitution once the limits are surpassed. The lower, the more velocity-energy gets lost.
floatlinear_limit/softness=1.0🔗
- voidset_param(param:Param, value:float)
voidset_param(param:Param, value:float)
- floatget_param(param:Param)const
floatget_param(param:Param)const
A factor applied to the movement across the slider axis once the limits get surpassed. The lower, the slower the movement.
floatlinear_limit/upper_distance=1.0🔗
- voidset_param(param:Param, value:float)
voidset_param(param:Param, value:float)
- floatget_param(param:Param)const
floatget_param(param:Param)const
The maximum difference between the pivot points on their X axis before damping happens.
floatlinear_motion/damping=0.0🔗
- voidset_param(param:Param, value:float)
voidset_param(param:Param, value:float)
- floatget_param(param:Param)const
floatget_param(param:Param)const
The amount of damping inside the slider limits.
floatlinear_motion/restitution=0.7🔗
- voidset_param(param:Param, value:float)
voidset_param(param:Param, value:float)
- floatget_param(param:Param)const
floatget_param(param:Param)const
The amount of restitution inside the slider limits.
floatlinear_motion/softness=1.0🔗
- voidset_param(param:Param, value:float)
voidset_param(param:Param, value:float)
- floatget_param(param:Param)const
floatget_param(param:Param)const
A factor applied to the movement across the slider axis as long as the slider is in the limits. The lower, the slower the movement.
floatlinear_ortho/damping=1.0🔗
- voidset_param(param:Param, value:float)
voidset_param(param:Param, value:float)
- floatget_param(param:Param)const
floatget_param(param:Param)const
The amount of damping when movement is across axes orthogonal to the slider.
floatlinear_ortho/restitution=0.7🔗
- voidset_param(param:Param, value:float)
voidset_param(param:Param, value:float)
- floatget_param(param:Param)const
floatget_param(param:Param)const
The amount of restitution when movement is across axes orthogonal to the slider.
floatlinear_ortho/softness=1.0🔗
- voidset_param(param:Param, value:float)
voidset_param(param:Param, value:float)
- floatget_param(param:Param)const
floatget_param(param:Param)const
A factor applied to the movement across axes orthogonal to the slider.

## Method Descriptions
floatget_param(param:Param)const🔗
Returns the value of the given parameter.
voidset_param(param:Param, value:float)🔗
Assignsvalueto the given parameter.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.