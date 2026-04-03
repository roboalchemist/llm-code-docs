# XRBodyTracker

# XRBodyTracker
Experimental:This class may be changed or removed in future versions.
Inherits:XRPositionalTracker<XRTracker<RefCounted<Object
A tracked body in XR.

## Description
A body tracking system will create an instance of this object and add it to theXRServer. This tracking system will then obtain skeleton data, convert it to the Godot Humanoid skeleton and store this data on theXRBodyTrackerobject.
UseXRBodyModifier3Dto animate a body mesh using body tracking data.

## Tutorials
- XR documentation index
XR documentation index

## Properties

| BitField[BodyFlags] | body_flags | 0 |
|---|---|---|
| bool | has_tracking_data | false |
| TrackerType | type | 32(overridesXRTracker) |

BitField[BodyFlags]
body_flags
bool
has_tracking_data
false
TrackerType
type
32(overridesXRTracker)

## Methods

| BitField[JointFlags] | get_joint_flags(joint:Joint)const |
|---|---|
| Transform3D | get_joint_transform(joint:Joint)const |
| void | set_joint_flags(joint:Joint, flags:BitField[JointFlags]) |
| void | set_joint_transform(joint:Joint, transform:Transform3D) |

BitField[JointFlags]
get_joint_flags(joint:Joint)const
Transform3D
get_joint_transform(joint:Joint)const
void
set_joint_flags(joint:Joint, flags:BitField[JointFlags])
void
set_joint_transform(joint:Joint, transform:Transform3D)

## Enumerations
flagsBodyFlags:🔗
BodyFlagsBODY_FLAG_UPPER_BODY_SUPPORTED=1
Upper body tracking supported.
BodyFlagsBODY_FLAG_LOWER_BODY_SUPPORTED=2
Lower body tracking supported.
BodyFlagsBODY_FLAG_HANDS_SUPPORTED=4
Hand tracking supported.
enumJoint:🔗
JointJOINT_ROOT=0
Root joint.
JointJOINT_HIPS=1
Hips joint.
JointJOINT_SPINE=2
Spine joint.
JointJOINT_CHEST=3
Chest joint.
JointJOINT_UPPER_CHEST=4
Upper chest joint.
JointJOINT_NECK=5
Neck joint.
JointJOINT_HEAD=6
Head joint.
JointJOINT_HEAD_TIP=7
Head tip joint.
JointJOINT_LEFT_SHOULDER=8
Left shoulder joint.
JointJOINT_LEFT_UPPER_ARM=9
Left upper arm joint.
JointJOINT_LEFT_LOWER_ARM=10
Left lower arm joint.
JointJOINT_RIGHT_SHOULDER=11
Right shoulder joint.
JointJOINT_RIGHT_UPPER_ARM=12
Right upper arm joint.
JointJOINT_RIGHT_LOWER_ARM=13
Right lower arm joint.
JointJOINT_LEFT_UPPER_LEG=14
Left upper leg joint.
JointJOINT_LEFT_LOWER_LEG=15
Left lower leg joint.
JointJOINT_LEFT_FOOT=16
Left foot joint.
JointJOINT_LEFT_TOES=17
Left toes joint.
JointJOINT_RIGHT_UPPER_LEG=18
Right upper leg joint.
JointJOINT_RIGHT_LOWER_LEG=19
Right lower leg joint.
JointJOINT_RIGHT_FOOT=20
Right foot joint.
JointJOINT_RIGHT_TOES=21
Right toes joint.
JointJOINT_LEFT_HAND=22
Left hand joint.
JointJOINT_LEFT_PALM=23
Left palm joint.
JointJOINT_LEFT_WRIST=24
Left wrist joint.
JointJOINT_LEFT_THUMB_METACARPAL=25
Left thumb metacarpal joint.
JointJOINT_LEFT_THUMB_PHALANX_PROXIMAL=26
Left thumb phalanx proximal joint.
JointJOINT_LEFT_THUMB_PHALANX_DISTAL=27
Left thumb phalanx distal joint.
JointJOINT_LEFT_THUMB_TIP=28
Left thumb tip joint.
JointJOINT_LEFT_INDEX_FINGER_METACARPAL=29
Left index finger metacarpal joint.
JointJOINT_LEFT_INDEX_FINGER_PHALANX_PROXIMAL=30
Left index finger phalanx proximal joint.
JointJOINT_LEFT_INDEX_FINGER_PHALANX_INTERMEDIATE=31
Left index finger phalanx intermediate joint.
JointJOINT_LEFT_INDEX_FINGER_PHALANX_DISTAL=32
Left index finger phalanx distal joint.
JointJOINT_LEFT_INDEX_FINGER_TIP=33
Left index finger tip joint.
JointJOINT_LEFT_MIDDLE_FINGER_METACARPAL=34
Left middle finger metacarpal joint.
JointJOINT_LEFT_MIDDLE_FINGER_PHALANX_PROXIMAL=35
Left middle finger phalanx proximal joint.
JointJOINT_LEFT_MIDDLE_FINGER_PHALANX_INTERMEDIATE=36
Left middle finger phalanx intermediate joint.
JointJOINT_LEFT_MIDDLE_FINGER_PHALANX_DISTAL=37
Left middle finger phalanx distal joint.
JointJOINT_LEFT_MIDDLE_FINGER_TIP=38
Left middle finger tip joint.
JointJOINT_LEFT_RING_FINGER_METACARPAL=39
Left ring finger metacarpal joint.
JointJOINT_LEFT_RING_FINGER_PHALANX_PROXIMAL=40
Left ring finger phalanx proximal joint.
JointJOINT_LEFT_RING_FINGER_PHALANX_INTERMEDIATE=41
Left ring finger phalanx intermediate joint.
JointJOINT_LEFT_RING_FINGER_PHALANX_DISTAL=42
Left ring finger phalanx distal joint.
JointJOINT_LEFT_RING_FINGER_TIP=43
Left ring finger tip joint.
JointJOINT_LEFT_PINKY_FINGER_METACARPAL=44
Left pinky finger metacarpal joint.
JointJOINT_LEFT_PINKY_FINGER_PHALANX_PROXIMAL=45
Left pinky finger phalanx proximal joint.
JointJOINT_LEFT_PINKY_FINGER_PHALANX_INTERMEDIATE=46
Left pinky finger phalanx intermediate joint.
JointJOINT_LEFT_PINKY_FINGER_PHALANX_DISTAL=47
Left pinky finger phalanx distal joint.
JointJOINT_LEFT_PINKY_FINGER_TIP=48
Left pinky finger tip joint.
JointJOINT_RIGHT_HAND=49
Right hand joint.
JointJOINT_RIGHT_PALM=50
Right palm joint.
JointJOINT_RIGHT_WRIST=51
Right wrist joint.
JointJOINT_RIGHT_THUMB_METACARPAL=52
Right thumb metacarpal joint.
JointJOINT_RIGHT_THUMB_PHALANX_PROXIMAL=53
Right thumb phalanx proximal joint.
JointJOINT_RIGHT_THUMB_PHALANX_DISTAL=54
Right thumb phalanx distal joint.
JointJOINT_RIGHT_THUMB_TIP=55
Right thumb tip joint.
JointJOINT_RIGHT_INDEX_FINGER_METACARPAL=56
Right index finger metacarpal joint.
JointJOINT_RIGHT_INDEX_FINGER_PHALANX_PROXIMAL=57
Right index finger phalanx proximal joint.
JointJOINT_RIGHT_INDEX_FINGER_PHALANX_INTERMEDIATE=58
Right index finger phalanx intermediate joint.
JointJOINT_RIGHT_INDEX_FINGER_PHALANX_DISTAL=59
Right index finger phalanx distal joint.
JointJOINT_RIGHT_INDEX_FINGER_TIP=60
Right index finger tip joint.
JointJOINT_RIGHT_MIDDLE_FINGER_METACARPAL=61
Right middle finger metacarpal joint.
JointJOINT_RIGHT_MIDDLE_FINGER_PHALANX_PROXIMAL=62
Right middle finger phalanx proximal joint.
JointJOINT_RIGHT_MIDDLE_FINGER_PHALANX_INTERMEDIATE=63
Right middle finger phalanx intermediate joint.
JointJOINT_RIGHT_MIDDLE_FINGER_PHALANX_DISTAL=64
Right middle finger phalanx distal joint.
JointJOINT_RIGHT_MIDDLE_FINGER_TIP=65
Right middle finger tip joint.
JointJOINT_RIGHT_RING_FINGER_METACARPAL=66
Right ring finger metacarpal joint.
JointJOINT_RIGHT_RING_FINGER_PHALANX_PROXIMAL=67
Right ring finger phalanx proximal joint.
JointJOINT_RIGHT_RING_FINGER_PHALANX_INTERMEDIATE=68
Right ring finger phalanx intermediate joint.
JointJOINT_RIGHT_RING_FINGER_PHALANX_DISTAL=69
Right ring finger phalanx distal joint.
JointJOINT_RIGHT_RING_FINGER_TIP=70
Right ring finger tip joint.
JointJOINT_RIGHT_PINKY_FINGER_METACARPAL=71
Right pinky finger metacarpal joint.
JointJOINT_RIGHT_PINKY_FINGER_PHALANX_PROXIMAL=72
Right pinky finger phalanx proximal joint.
JointJOINT_RIGHT_PINKY_FINGER_PHALANX_INTERMEDIATE=73
Right pinky finger phalanx intermediate joint.
JointJOINT_RIGHT_PINKY_FINGER_PHALANX_DISTAL=74
Right pinky finger phalanx distal joint.
JointJOINT_RIGHT_PINKY_FINGER_TIP=75
Right pinky finger tip joint.
JointJOINT_LOWER_CHEST=76
Lower chest joint.
JointJOINT_LEFT_SCAPULA=77
Left scapula joint.
JointJOINT_LEFT_WRIST_TWIST=78
Left wrist twist joint.
JointJOINT_RIGHT_SCAPULA=79
Right scapula joint.
JointJOINT_RIGHT_WRIST_TWIST=80
Right wrist twist joint.
JointJOINT_LEFT_FOOT_TWIST=81
Left foot twist joint.
JointJOINT_LEFT_HEEL=82
Left heel joint.
JointJOINT_LEFT_MIDDLE_FOOT=83
Left middle foot joint.
JointJOINT_RIGHT_FOOT_TWIST=84
Right foot twist joint.
JointJOINT_RIGHT_HEEL=85
Right heel joint.
JointJOINT_RIGHT_MIDDLE_FOOT=86
Right middle foot joint.
JointJOINT_MAX=87
Represents the size of theJointenum.
flagsJointFlags:🔗
JointFlagsJOINT_FLAG_ORIENTATION_VALID=1
The joint's orientation data is valid.
JointFlagsJOINT_FLAG_ORIENTATION_TRACKED=2
The joint's orientation is actively tracked. May not be set if tracking has been temporarily lost.
JointFlagsJOINT_FLAG_POSITION_VALID=4
The joint's position data is valid.
JointFlagsJOINT_FLAG_POSITION_TRACKED=8
The joint's position is actively tracked. May not be set if tracking has been temporarily lost.

## Property Descriptions
BitField[BodyFlags]body_flags=0🔗
- voidset_body_flags(value:BitField[BodyFlags])
voidset_body_flags(value:BitField[BodyFlags])
- BitField[BodyFlags]get_body_flags()
BitField[BodyFlags]get_body_flags()
The type of body tracking data captured.
boolhas_tracking_data=false🔗
- voidset_has_tracking_data(value:bool)
voidset_has_tracking_data(value:bool)
- boolget_has_tracking_data()
boolget_has_tracking_data()
Iftrue, the body tracking data is valid.

## Method Descriptions
BitField[JointFlags]get_joint_flags(joint:Joint)const🔗
Returns flags about the validity of the tracking data for the given body joint.
Transform3Dget_joint_transform(joint:Joint)const🔗
Returns the transform for the given body joint.
voidset_joint_flags(joint:Joint, flags:BitField[JointFlags])🔗
Sets flags about the validity of the tracking data for the given body joint.
voidset_joint_transform(joint:Joint, transform:Transform3D)🔗
Sets the transform for the given body joint.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.