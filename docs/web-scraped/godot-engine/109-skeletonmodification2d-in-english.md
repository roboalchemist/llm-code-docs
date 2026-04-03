# SkeletonModification2D in English

# SkeletonModification2D
Experimental:This class may be changed or removed in future versions.
Inherits:Resource<RefCounted<Object
Inherited By:SkeletonModification2DCCDIK,SkeletonModification2DFABRIK,SkeletonModification2DJiggle,SkeletonModification2DLookAt,SkeletonModification2DPhysicalBones,SkeletonModification2DStackHolder,SkeletonModification2DTwoBoneIK
Base class for resources that operate onBone2Ds in aSkeleton2D.

## Description
This resource provides an interface that can be expanded so code that operates onBone2Dnodes in aSkeleton2Dcan be mixed and matched together to create complex interactions.
This is used to provide Godot with a flexible and powerful Inverse Kinematics solution that can be adapted for many different uses.

## Properties

| bool | enabled | true |
|---|---|---|
| int | execution_mode | 0 |

bool
enabled
true
execution_mode

## Methods

| void | _draw_editor_gizmo()virtual |
|---|---|
| void | _execute(delta:float)virtual |
| void | _setup_modification(modification_stack:SkeletonModificationStack2D)virtual |
| float | clamp_angle(angle:float, min:float, max:float, invert:bool) |
| bool | get_editor_draw_gizmo()const |
| bool | get_is_setup()const |
| SkeletonModificationStack2D | get_modification_stack() |
| void | set_editor_draw_gizmo(draw_gizmo:bool) |
| void | set_is_setup(is_setup:bool) |

void
_draw_editor_gizmo()virtual
void
_execute(delta:float)virtual
void
_setup_modification(modification_stack:SkeletonModificationStack2D)virtual
float
clamp_angle(angle:float, min:float, max:float, invert:bool)
bool
get_editor_draw_gizmo()const
bool
get_is_setup()const
SkeletonModificationStack2D
get_modification_stack()
void
set_editor_draw_gizmo(draw_gizmo:bool)
void
set_is_setup(is_setup:bool)

## Property Descriptions
boolenabled=true🔗
- voidset_enabled(value:bool)
voidset_enabled(value:bool)
- boolget_enabled()
boolget_enabled()
Iftrue, the modification's_execute()function will be called by theSkeletonModificationStack2D.
intexecution_mode=0🔗
- voidset_execution_mode(value:int)
voidset_execution_mode(value:int)
- intget_execution_mode()
intget_execution_mode()
The execution mode for the modification. This tells the modification stack when to execute the modification. Some modifications have settings that are only available in certain execution modes.

## Method Descriptions
void_draw_editor_gizmo()virtual🔗
Used for drawingeditor-onlymodification gizmos. This function will only be called in the Godot editor and can be overridden to draw custom gizmos.
Note:You will need to use the Skeleton2D fromSkeletonModificationStack2D.get_skeleton()and it's draw functions, as theSkeletonModification2Dresource cannot draw on its own.
void_execute(delta:float)virtual🔗
Executes the given modification. This is where the modification performs whatever function it is designed to do.
void_setup_modification(modification_stack:SkeletonModificationStack2D)virtual🔗
Called when the modification is setup. This is where the modification performs initialization.
floatclamp_angle(angle:float, min:float, max:float, invert:bool)🔗
Takes an angle and clamps it so it is within the passed-inminandmaxrange.invertwill inversely clamp the angle, clamping it to the range outside of the given bounds.
boolget_editor_draw_gizmo()const🔗
Returns whether this modification will call_draw_editor_gizmo()in the Godot editor to draw modification-specific gizmos.
boolget_is_setup()const🔗
Returns whether this modification has been successfully setup or not.
SkeletonModificationStack2Dget_modification_stack()🔗
Returns theSkeletonModificationStack2Dthat this modification is bound to. Through the modification stack, you can access the Skeleton2D the modification is operating on.
voidset_editor_draw_gizmo(draw_gizmo:bool)🔗
Sets whether this modification will call_draw_editor_gizmo()in the Godot editor to draw modification-specific gizmos.
voidset_is_setup(is_setup:bool)🔗
Manually allows you to set the setup state of the modification. This function should only rarely be used, as theSkeletonModificationStack2Dthe modification is bound to should handle setting the modification up.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.