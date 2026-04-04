# Animation

# Animation

Inherits:Resource<RefCounted<Object
Holds data that can be used to animate anything in the engine.

## Description

This resource holds data that can be used to animate anything in the engine. Animations are divided into tracks and each track must be linked to a node. The state of that node can be changed through time, by adding timed keys (events) to the track.

```
# This creates an animation that makes the node "Enemy" move to the right by
# 100 pixels in 2.0 seconds.
var animation = Animation.new()
var track_index = animation.add_track(Animation.TYPE_VALUE)
animation.track_set_path(track_index, "Enemy:position:x")
animation.track_insert_key(track_index, 0.0, 0)
animation.track_insert_key(track_index, 2.0, 100)
animation.length = 2.0
```

```
// This creates an animation that makes the node "Enemy" move to the right by
// 100 pixels in 2.0 seconds.
var animation = new Animation();
int trackIndex = animation.AddTrack(Animation.TrackType.Value);
animation.TrackSetPath(trackIndex, "Enemy:position:x");
animation.TrackInsertKey(trackIndex, 0.0f, 0);
animation.TrackInsertKey(trackIndex, 2.0f, 100);
animation.Length = 2.0f;
```

Animations are just data containers, and must be added to nodes such as anAnimationPlayerto be played back. Animation tracks have different types, each with its own set of dedicated methods. CheckTrackTypeto see available types.
Note:For 3D position/rotation/scale, using the dedicatedTYPE_POSITION_3D,TYPE_ROTATION_3DandTYPE_SCALE_3Dtrack types instead ofTYPE_VALUEis recommended for performance reasons.

## Tutorials

- Animation documentation index
Animation documentation index

## Properties

| bool | capture_included | false |
|---|---|---|
| float | length | 1.0 |
| LoopMode | loop_mode | 0 |
| float | step | 0.033333335 |

bool
capture_included
false
float
length
LoopMode
loop_mode
float
step
0.033333335

## Methods

| void | add_marker(name:StringName, time:float) |
|---|---|
| int | add_track(type:TrackType, at_position:int= -1) |
| StringName | animation_track_get_key_animation(track_idx:int, key_idx:int)const |
| int | animation_track_insert_key(track_idx:int, time:float, animation:StringName) |
| void | animation_track_set_key_animation(track_idx:int, key_idx:int, animation:StringName) |
| float | audio_track_get_key_end_offset(track_idx:int, key_idx:int)const |
| float | audio_track_get_key_start_offset(track_idx:int, key_idx:int)const |
| Resource | audio_track_get_key_stream(track_idx:int, key_idx:int)const |
| int | audio_track_insert_key(track_idx:int, time:float, stream:Resource, start_offset:float= 0, end_offset:float= 0) |
| bool | audio_track_is_use_blend(track_idx:int)const |
| void | audio_track_set_key_end_offset(track_idx:int, key_idx:int, offset:float) |
| void | audio_track_set_key_start_offset(track_idx:int, key_idx:int, offset:float) |
| void | audio_track_set_key_stream(track_idx:int, key_idx:int, stream:Resource) |
| void | audio_track_set_use_blend(track_idx:int, enable:bool) |
| Vector2 | bezier_track_get_key_in_handle(track_idx:int, key_idx:int)const |
| Vector2 | bezier_track_get_key_out_handle(track_idx:int, key_idx:int)const |
| float | bezier_track_get_key_value(track_idx:int, key_idx:int)const |
| int | bezier_track_insert_key(track_idx:int, time:float, value:float, in_handle:Vector2= Vector2(0, 0), out_handle:Vector2= Vector2(0, 0)) |
| float | bezier_track_interpolate(track_idx:int, time:float)const |
| void | bezier_track_set_key_in_handle(track_idx:int, key_idx:int, in_handle:Vector2, balanced_value_time_ratio:float= 1.0) |
| void | bezier_track_set_key_out_handle(track_idx:int, key_idx:int, out_handle:Vector2, balanced_value_time_ratio:float= 1.0) |
| void | bezier_track_set_key_value(track_idx:int, key_idx:int, value:float) |
| int | blend_shape_track_insert_key(track_idx:int, time:float, amount:float) |
| float | blend_shape_track_interpolate(track_idx:int, time_sec:float, backward:bool= false)const |
| void | clear() |
| void | compress(page_size:int= 8192, fps:int= 120, split_tolerance:float= 4.0) |
| void | copy_track(track_idx:int, to_animation:Animation) |
| int | find_track(path:NodePath, type:TrackType)const |
| StringName | get_marker_at_time(time:float)const |
| Color | get_marker_color(name:StringName)const |
| PackedStringArray | get_marker_names()const |
| float | get_marker_time(name:StringName)const |
| StringName | get_next_marker(time:float)const |
| StringName | get_prev_marker(time:float)const |
| int | get_track_count()const |
| bool | has_marker(name:StringName)const |
| StringName | method_track_get_name(track_idx:int, key_idx:int)const |
| Array | method_track_get_params(track_idx:int, key_idx:int)const |
| void | optimize(allowed_velocity_err:float= 0.01, allowed_angular_err:float= 0.01, precision:int= 3) |
| int | position_track_insert_key(track_idx:int, time:float, position:Vector3) |
| Vector3 | position_track_interpolate(track_idx:int, time_sec:float, backward:bool= false)const |
| void | remove_marker(name:StringName) |
| void | remove_track(track_idx:int) |
| int | rotation_track_insert_key(track_idx:int, time:float, rotation:Quaternion) |
| Quaternion | rotation_track_interpolate(track_idx:int, time_sec:float, backward:bool= false)const |
| int | scale_track_insert_key(track_idx:int, time:float, scale:Vector3) |
| Vector3 | scale_track_interpolate(track_idx:int, time_sec:float, backward:bool= false)const |
| void | set_marker_color(name:StringName, color:Color) |
| int | track_find_key(track_idx:int, time:float, find_mode:FindMode= 0, limit:bool= false, backward:bool= false)const |
| bool | track_get_interpolation_loop_wrap(track_idx:int)const |
| InterpolationType | track_get_interpolation_type(track_idx:int)const |
| int | track_get_key_count(track_idx:int)const |
| float | track_get_key_time(track_idx:int, key_idx:int)const |
| float | track_get_key_transition(track_idx:int, key_idx:int)const |
| Variant | track_get_key_value(track_idx:int, key_idx:int)const |
| NodePath | track_get_path(track_idx:int)const |
| TrackType | track_get_type(track_idx:int)const |
| int | track_insert_key(track_idx:int, time:float, key:Variant, transition:float= 1) |
| bool | track_is_compressed(track_idx:int)const |
| bool | track_is_enabled(track_idx:int)const |
| bool | track_is_imported(track_idx:int)const |
| void | track_move_down(track_idx:int) |
| void | track_move_to(track_idx:int, to_idx:int) |
| void | track_move_up(track_idx:int) |
| void | track_remove_key(track_idx:int, key_idx:int) |
| void | track_remove_key_at_time(track_idx:int, time:float) |
| void | track_set_enabled(track_idx:int, enabled:bool) |
| void | track_set_imported(track_idx:int, imported:bool) |
| void | track_set_interpolation_loop_wrap(track_idx:int, interpolation:bool) |
| void | track_set_interpolation_type(track_idx:int, interpolation:InterpolationType) |
| void | track_set_key_time(track_idx:int, key_idx:int, time:float) |
| void | track_set_key_transition(track_idx:int, key_idx:int, transition:float) |
| void | track_set_key_value(track_idx:int, key:int, value:Variant) |
| void | track_set_path(track_idx:int, path:NodePath) |
| void | track_swap(track_idx:int, with_idx:int) |
| UpdateMode | value_track_get_update_mode(track_idx:int)const |
| Variant | value_track_interpolate(track_idx:int, time_sec:float, backward:bool= false)const |
| void | value_track_set_update_mode(track_idx:int, mode:UpdateMode) |

void
add_marker(name:StringName, time:float)
add_track(type:TrackType, at_position:int= -1)
StringName
animation_track_get_key_animation(track_idx:int, key_idx:int)const
animation_track_insert_key(track_idx:int, time:float, animation:StringName)
void
animation_track_set_key_animation(track_idx:int, key_idx:int, animation:StringName)
float
audio_track_get_key_end_offset(track_idx:int, key_idx:int)const
float
audio_track_get_key_start_offset(track_idx:int, key_idx:int)const
Resource
audio_track_get_key_stream(track_idx:int, key_idx:int)const
audio_track_insert_key(track_idx:int, time:float, stream:Resource, start_offset:float= 0, end_offset:float= 0)
bool
audio_track_is_use_blend(track_idx:int)const
void
audio_track_set_key_end_offset(track_idx:int, key_idx:int, offset:float)
void
audio_track_set_key_start_offset(track_idx:int, key_idx:int, offset:float)
void
audio_track_set_key_stream(track_idx:int, key_idx:int, stream:Resource)
void
audio_track_set_use_blend(track_idx:int, enable:bool)
Vector2
bezier_track_get_key_in_handle(track_idx:int, key_idx:int)const
Vector2
bezier_track_get_key_out_handle(track_idx:int, key_idx:int)const
float
bezier_track_get_key_value(track_idx:int, key_idx:int)const
bezier_track_insert_key(track_idx:int, time:float, value:float, in_handle:Vector2= Vector2(0, 0), out_handle:Vector2= Vector2(0, 0))
float
bezier_track_interpolate(track_idx:int, time:float)const
void
bezier_track_set_key_in_handle(track_idx:int, key_idx:int, in_handle:Vector2, balanced_value_time_ratio:float= 1.0)
void
bezier_track_set_key_out_handle(track_idx:int, key_idx:int, out_handle:Vector2, balanced_value_time_ratio:float= 1.0)
void
bezier_track_set_key_value(track_idx:int, key_idx:int, value:float)
blend_shape_track_insert_key(track_idx:int, time:float, amount:float)
float
blend_shape_track_interpolate(track_idx:int, time_sec:float, backward:bool= false)const
void
clear()
void
compress(page_size:int= 8192, fps:int= 120, split_tolerance:float= 4.0)
void
copy_track(track_idx:int, to_animation:Animation)
find_track(path:NodePath, type:TrackType)const
StringName
get_marker_at_time(time:float)const
Color
get_marker_color(name:StringName)const
PackedStringArray
get_marker_names()const
float
get_marker_time(name:StringName)const
StringName
get_next_marker(time:float)const
StringName
get_prev_marker(time:float)const
get_track_count()const
bool
has_marker(name:StringName)const
StringName
method_track_get_name(track_idx:int, key_idx:int)const
Array
method_track_get_params(track_idx:int, key_idx:int)const
void
optimize(allowed_velocity_err:float= 0.01, allowed_angular_err:float= 0.01, precision:int= 3)
position_track_insert_key(track_idx:int, time:float, position:Vector3)
Vector3
position_track_interpolate(track_idx:int, time_sec:float, backward:bool= false)const
void
remove_marker(name:StringName)
void
remove_track(track_idx:int)
rotation_track_insert_key(track_idx:int, time:float, rotation:Quaternion)
Quaternion
rotation_track_interpolate(track_idx:int, time_sec:float, backward:bool= false)const
scale_track_insert_key(track_idx:int, time:float, scale:Vector3)
Vector3
scale_track_interpolate(track_idx:int, time_sec:float, backward:bool= false)const
void
set_marker_color(name:StringName, color:Color)
track_find_key(track_idx:int, time:float, find_mode:FindMode= 0, limit:bool= false, backward:bool= false)const
bool
track_get_interpolation_loop_wrap(track_idx:int)const
InterpolationType
track_get_interpolation_type(track_idx:int)const
track_get_key_count(track_idx:int)const
float
track_get_key_time(track_idx:int, key_idx:int)const
float
track_get_key_transition(track_idx:int, key_idx:int)const
Variant
track_get_key_value(track_idx:int, key_idx:int)const
NodePath
track_get_path(track_idx:int)const
TrackType
track_get_type(track_idx:int)const
track_insert_key(track_idx:int, time:float, key:Variant, transition:float= 1)
bool
track_is_compressed(track_idx:int)const
bool
track_is_enabled(track_idx:int)const
bool
track_is_imported(track_idx:int)const
void
track_move_down(track_idx:int)
void
track_move_to(track_idx:int, to_idx:int)
void
track_move_up(track_idx:int)
void
track_remove_key(track_idx:int, key_idx:int)
void
track_remove_key_at_time(track_idx:int, time:float)
void
track_set_enabled(track_idx:int, enabled:bool)
void
track_set_imported(track_idx:int, imported:bool)
void
track_set_interpolation_loop_wrap(track_idx:int, interpolation:bool)
void
track_set_interpolation_type(track_idx:int, interpolation:InterpolationType)
void
track_set_key_time(track_idx:int, key_idx:int, time:float)
void
track_set_key_transition(track_idx:int, key_idx:int, transition:float)
void
track_set_key_value(track_idx:int, key:int, value:Variant)
void
track_set_path(track_idx:int, path:NodePath)
void
track_swap(track_idx:int, with_idx:int)
UpdateMode
value_track_get_update_mode(track_idx:int)const
Variant
value_track_interpolate(track_idx:int, time_sec:float, backward:bool= false)const
void
value_track_set_update_mode(track_idx:int, mode:UpdateMode)

## Enumerations

enumTrackType:🔗
TrackTypeTYPE_VALUE=0
Value tracks set values in node properties, but only those which can be interpolated. For 3D position/rotation/scale, using the dedicatedTYPE_POSITION_3D,TYPE_ROTATION_3DandTYPE_SCALE_3Dtrack types instead ofTYPE_VALUEis recommended for performance reasons.
TrackTypeTYPE_POSITION_3D=1
3D position track (values are stored inVector3s).
TrackTypeTYPE_ROTATION_3D=2
3D rotation track (values are stored inQuaternions).
TrackTypeTYPE_SCALE_3D=3
3D scale track (values are stored inVector3s).
TrackTypeTYPE_BLEND_SHAPE=4
Blend shape track.
TrackTypeTYPE_METHOD=5
Method tracks call functions with given arguments per key.
TrackTypeTYPE_BEZIER=6
Bezier tracks are used to interpolate a value using custom curves. They can also be used to animate sub-properties of vectors and colors (e.g. alpha value of aColor).
TrackTypeTYPE_AUDIO=7
Audio tracks are used to play an audio stream with either type ofAudioStreamPlayer. The stream can be trimmed and previewed in the animation.
TrackTypeTYPE_ANIMATION=8
Animation tracks play animations in otherAnimationPlayernodes.
enumInterpolationType:🔗
InterpolationTypeINTERPOLATION_NEAREST=0
No interpolation (nearest value).
InterpolationTypeINTERPOLATION_LINEAR=1
Linear interpolation.
InterpolationTypeINTERPOLATION_CUBIC=2
Cubic interpolation. This looks smoother than linear interpolation, but is more expensive to interpolate. Stick toINTERPOLATION_LINEARfor complex 3D animations imported from external software, even if it requires using a higher animation framerate in return.
InterpolationTypeINTERPOLATION_LINEAR_ANGLE=3
Linear interpolation with shortest path rotation.
Note:The result value is always normalized and may not match the key value.
InterpolationTypeINTERPOLATION_CUBIC_ANGLE=4
Cubic interpolation with shortest path rotation.
Note:The result value is always normalized and may not match the key value.
enumUpdateMode:🔗
UpdateModeUPDATE_CONTINUOUS=0
Update between keyframes and hold the value.
UpdateModeUPDATE_DISCRETE=1
Update at the keyframes.
UpdateModeUPDATE_CAPTURE=2
Same asUPDATE_CONTINUOUSbut works as a flag to capture the value of the current object and perform interpolation in some methods. See alsoAnimationMixer.capture(),AnimationPlayer.playback_auto_capture, andAnimationPlayer.play_with_capture().
enumLoopMode:🔗
LoopModeLOOP_NONE=0
At both ends of the animation, the animation will stop playing.
LoopModeLOOP_LINEAR=1
At both ends of the animation, the animation will be repeated without changing the playback direction.
LoopModeLOOP_PINGPONG=2
Repeats playback and reverse playback at both ends of the animation.
enumLoopedFlag:🔗
LoopedFlagLOOPED_FLAG_NONE=0
This flag indicates that the animation proceeds without any looping.
LoopedFlagLOOPED_FLAG_END=1
This flag indicates that the animation has reached the end of the animation and just after loop processed.
LoopedFlagLOOPED_FLAG_START=2
This flag indicates that the animation has reached the start of the animation and just after loop processed.
enumFindMode:🔗
FindModeFIND_MODE_NEAREST=0
Finds the nearest time key.
FindModeFIND_MODE_APPROX=1
Finds only the key with approximating the time.
FindModeFIND_MODE_EXACT=2
Finds only the key with matching the time.

## Property Descriptions

boolcapture_included=false🔗

- boolis_capture_included()
boolis_capture_included()
Returnstrueif the capture track is included. This is a cached readonly value for performance.
floatlength=1.0🔗
- voidset_length(value:float)
voidset_length(value:float)
- floatget_length()
floatget_length()
The total length of the animation (in seconds).
Note:Length is not delimited by the last key, as this one may be before or after the end to ensure correct interpolation and looping.
LoopModeloop_mode=0🔗
- voidset_loop_mode(value:LoopMode)
voidset_loop_mode(value:LoopMode)
- LoopModeget_loop_mode()
LoopModeget_loop_mode()
Determines the behavior of both ends of the animation timeline during animation playback. This indicates whether and how the animation should be restarted, and is also used to correctly interpolate animation cycles.
floatstep=0.033333335🔗
- voidset_step(value:float)
voidset_step(value:float)
- floatget_step()
floatget_step()
The animation step value.

## Method Descriptions

voidadd_marker(name:StringName, time:float)🔗
Adds a marker to this Animation.
intadd_track(type:TrackType, at_position:int= -1)🔗
Adds a track to the Animation.
StringNameanimation_track_get_key_animation(track_idx:int, key_idx:int)const🔗
Returns the animation name at the key identified bykey_idx. Thetrack_idxmust be the index of an Animation Track.
intanimation_track_insert_key(track_idx:int, time:float, animation:StringName)🔗
Inserts a key with valueanimationat the giventime(in seconds). Thetrack_idxmust be the index of an Animation Track.
voidanimation_track_set_key_animation(track_idx:int, key_idx:int, animation:StringName)🔗
Sets the key identified bykey_idxto valueanimation. Thetrack_idxmust be the index of an Animation Track.
floataudio_track_get_key_end_offset(track_idx:int, key_idx:int)const🔗
Returns the end offset of the key identified bykey_idx. Thetrack_idxmust be the index of an Audio Track.
End offset is the number of seconds cut off at the ending of the audio stream.
floataudio_track_get_key_start_offset(track_idx:int, key_idx:int)const🔗
Returns the start offset of the key identified bykey_idx. Thetrack_idxmust be the index of an Audio Track.
Start offset is the number of seconds cut off at the beginning of the audio stream.
Resourceaudio_track_get_key_stream(track_idx:int, key_idx:int)const🔗
Returns the audio stream of the key identified bykey_idx. Thetrack_idxmust be the index of an Audio Track.
intaudio_track_insert_key(track_idx:int, time:float, stream:Resource, start_offset:float= 0, end_offset:float= 0)🔗
Inserts an Audio Track key at the giventimein seconds. Thetrack_idxmust be the index of an Audio Track.
streamis theAudioStreamresource to play.start_offsetis the number of seconds cut off at the beginning of the audio stream, whileend_offsetis at the ending.
boolaudio_track_is_use_blend(track_idx:int)const🔗
Returnstrueif the track attrack_idxwill be blended with other animations.
voidaudio_track_set_key_end_offset(track_idx:int, key_idx:int, offset:float)🔗
Sets the end offset of the key identified bykey_idxto valueoffset. Thetrack_idxmust be the index of an Audio Track.
voidaudio_track_set_key_start_offset(track_idx:int, key_idx:int, offset:float)🔗
Sets the start offset of the key identified bykey_idxto valueoffset. Thetrack_idxmust be the index of an Audio Track.
voidaudio_track_set_key_stream(track_idx:int, key_idx:int, stream:Resource)🔗
Sets the stream of the key identified bykey_idxto valuestream. Thetrack_idxmust be the index of an Audio Track.
voidaudio_track_set_use_blend(track_idx:int, enable:bool)🔗
Sets whether the track will be blended with other animations. Iftrue, the audio playback volume changes depending on the blend value.
Vector2bezier_track_get_key_in_handle(track_idx:int, key_idx:int)const🔗
Returns the in handle of the key identified bykey_idx. Thetrack_idxmust be the index of a Bezier Track.
Vector2bezier_track_get_key_out_handle(track_idx:int, key_idx:int)const🔗
Returns the out handle of the key identified bykey_idx. Thetrack_idxmust be the index of a Bezier Track.
floatbezier_track_get_key_value(track_idx:int, key_idx:int)const🔗
Returns the value of the key identified bykey_idx. Thetrack_idxmust be the index of a Bezier Track.
intbezier_track_insert_key(track_idx:int, time:float, value:float, in_handle:Vector2= Vector2(0, 0), out_handle:Vector2= Vector2(0, 0))🔗
Inserts a Bezier Track key at the giventimein seconds. Thetrack_idxmust be the index of a Bezier Track.
in_handleis the left-side weight of the added Bezier curve point,out_handleis the right-side one, whilevalueis the actual value at this point.
floatbezier_track_interpolate(track_idx:int, time:float)const🔗
Returns the interpolated value at the giventime(in seconds). Thetrack_idxmust be the index of a Bezier Track.
voidbezier_track_set_key_in_handle(track_idx:int, key_idx:int, in_handle:Vector2, balanced_value_time_ratio:float= 1.0)🔗
Sets the in handle of the key identified bykey_idxto valuein_handle. Thetrack_idxmust be the index of a Bezier Track.
voidbezier_track_set_key_out_handle(track_idx:int, key_idx:int, out_handle:Vector2, balanced_value_time_ratio:float= 1.0)🔗
Sets the out handle of the key identified bykey_idxto valueout_handle. Thetrack_idxmust be the index of a Bezier Track.
voidbezier_track_set_key_value(track_idx:int, key_idx:int, value:float)🔗
Sets the value of the key identified bykey_idxto the given value. Thetrack_idxmust be the index of a Bezier Track.
intblend_shape_track_insert_key(track_idx:int, time:float, amount:float)🔗
Inserts a key in a given blend shape track. Returns the key index.
floatblend_shape_track_interpolate(track_idx:int, time_sec:float, backward:bool= false)const🔗
Returns the interpolated blend shape value at the given time (in seconds). Thetrack_idxmust be the index of a blend shape track.
voidclear()🔗
Clear the animation (clear all tracks and reset all).
voidcompress(page_size:int= 8192, fps:int= 120, split_tolerance:float= 4.0)🔗
Compress the animation and all its tracks in-place. This will maketrack_is_compressed()returntrueonce called on thisAnimation. Compressed tracks require less memory to be played, and are designed to be used for complex 3D animations (such as cutscenes) imported from external 3D software. Compression is lossy, but the difference is usually not noticeable in real world conditions.
Note:Compressed tracks have various limitations (such as not being editable from the editor), so only use compressed animations if you actually need them.
voidcopy_track(track_idx:int, to_animation:Animation)🔗
Adds a new track toto_animationthat is a copy of the given track from this animation.
intfind_track(path:NodePath, type:TrackType)const🔗
Returns the index of the specified track. If the track is not found, return -1.
StringNameget_marker_at_time(time:float)const🔗
Returns the name of the marker located at the given time.
Colorget_marker_color(name:StringName)const🔗
Returns the given marker's color.
PackedStringArrayget_marker_names()const🔗
Returns every marker in this Animation, sorted ascending by time.
floatget_marker_time(name:StringName)const🔗
Returns the given marker's time.
StringNameget_next_marker(time:float)const🔗
Returns the closest marker that comes after the given time. If no such marker exists, an empty string is returned.
StringNameget_prev_marker(time:float)const🔗
Returns the closest marker that comes before the given time. If no such marker exists, an empty string is returned.
intget_track_count()const🔗
Returns the amount of tracks in the animation.
boolhas_marker(name:StringName)const🔗
Returnstrueif this Animation contains a marker with the given name.
StringNamemethod_track_get_name(track_idx:int, key_idx:int)const🔗
Returns the method name of a method track.
Arraymethod_track_get_params(track_idx:int, key_idx:int)const🔗
Returns the arguments values to be called on a method track for a given key in a given track.
voidoptimize(allowed_velocity_err:float= 0.01, allowed_angular_err:float= 0.01, precision:int= 3)🔗
Optimize the animation and all its tracks in-place. This will preserve only as many keys as are necessary to keep the animation within the specified bounds.
intposition_track_insert_key(track_idx:int, time:float, position:Vector3)🔗
Inserts a key in a given 3D position track. Returns the key index.
Vector3position_track_interpolate(track_idx:int, time_sec:float, backward:bool= false)const🔗
Returns the interpolated position value at the given time (in seconds). Thetrack_idxmust be the index of a 3D position track.
voidremove_marker(name:StringName)🔗
Removes the marker with the given name from this Animation.
voidremove_track(track_idx:int)🔗
Removes a track by specifying the track index.
introtation_track_insert_key(track_idx:int, time:float, rotation:Quaternion)🔗
Inserts a key in a given 3D rotation track. Returns the key index.
Quaternionrotation_track_interpolate(track_idx:int, time_sec:float, backward:bool= false)const🔗
Returns the interpolated rotation value at the given time (in seconds). Thetrack_idxmust be the index of a 3D rotation track.
intscale_track_insert_key(track_idx:int, time:float, scale:Vector3)🔗
Inserts a key in a given 3D scale track. Returns the key index.
Vector3scale_track_interpolate(track_idx:int, time_sec:float, backward:bool= false)const🔗
Returns the interpolated scale value at the given time (in seconds). Thetrack_idxmust be the index of a 3D scale track.
voidset_marker_color(name:StringName, color:Color)🔗
Sets the given marker's color.
inttrack_find_key(track_idx:int, time:float, find_mode:FindMode= 0, limit:bool= false, backward:bool= false)const🔗
Finds the key index by time in a given track. Optionally, only find it if the approx/exact time is given.
Iflimitistrue, it does not return keys outside the animation range.
Ifbackwardistrue, the direction is reversed in methods that rely on one directional processing.
For example, in casefind_modeisFIND_MODE_NEAREST, if there is no key in the current position just after seeked, the first key found is retrieved by searching before the position, but ifbackwardistrue, the first key found is retrieved after the position.
booltrack_get_interpolation_loop_wrap(track_idx:int)const🔗
Returnstrueif the track attrack_idxwraps the interpolation loop. New tracks wrap the interpolation loop by default.
InterpolationTypetrack_get_interpolation_type(track_idx:int)const🔗
Returns the interpolation type of a given track.
inttrack_get_key_count(track_idx:int)const🔗
Returns the number of keys in a given track.
floattrack_get_key_time(track_idx:int, key_idx:int)const🔗
Returns the time at which the key is located.
floattrack_get_key_transition(track_idx:int, key_idx:int)const🔗
Returns the transition curve (easing) for a specific key (see the built-in math function@GlobalScope.ease()).
Varianttrack_get_key_value(track_idx:int, key_idx:int)const🔗
Returns the value of a given key in a given track.
NodePathtrack_get_path(track_idx:int)const🔗
Gets the path of a track. For more information on the path format, seetrack_set_path().
TrackTypetrack_get_type(track_idx:int)const🔗
Gets the type of a track.
inttrack_insert_key(track_idx:int, time:float, key:Variant, transition:float= 1)🔗
Inserts a generic key in a given track. Returns the key index.
booltrack_is_compressed(track_idx:int)const🔗
Returnstrueif the track is compressed,falseotherwise. See alsocompress().
booltrack_is_enabled(track_idx:int)const🔗
Returnstrueif the track at indextrack_idxis enabled.
booltrack_is_imported(track_idx:int)const🔗
Returnstrueif the given track is imported. Else, returnfalse.
voidtrack_move_down(track_idx:int)🔗
Moves a track down.
voidtrack_move_to(track_idx:int, to_idx:int)🔗
Changes the index position of tracktrack_idxto the one defined into_idx.
voidtrack_move_up(track_idx:int)🔗
Moves a track up.
voidtrack_remove_key(track_idx:int, key_idx:int)🔗
Removes a key by index in a given track.
voidtrack_remove_key_at_time(track_idx:int, time:float)🔗
Removes a key attimein a given track.
voidtrack_set_enabled(track_idx:int, enabled:bool)🔗
Enables/disables the given track. Tracks are enabled by default.
voidtrack_set_imported(track_idx:int, imported:bool)🔗
Sets the given track as imported or not.
voidtrack_set_interpolation_loop_wrap(track_idx:int, interpolation:bool)🔗
Iftrue, the track attrack_idxwraps the interpolation loop.
voidtrack_set_interpolation_type(track_idx:int, interpolation:InterpolationType)🔗
Sets the interpolation type of a given track.
voidtrack_set_key_time(track_idx:int, key_idx:int, time:float)🔗
Sets the time of an existing key.
voidtrack_set_key_transition(track_idx:int, key_idx:int, transition:float)🔗
Sets the transition curve (easing) for a specific key (see the built-in math function@GlobalScope.ease()).
voidtrack_set_key_value(track_idx:int, key:int, value:Variant)🔗
Sets the value of an existing key.
voidtrack_set_path(track_idx:int, path:NodePath)🔗
Sets the path of a track. Paths must be valid scene-tree paths to a node and must be specified starting from theAnimationMixer.root_nodethat will reproduce the animation. Tracks that control properties or bones must append their name after the path, separated by":".
For example,"character/skeleton:ankle"or"character/mesh:transform/local".
voidtrack_swap(track_idx:int, with_idx:int)🔗
Swaps the tracktrack_idx's index position with the trackwith_idx.
UpdateModevalue_track_get_update_mode(track_idx:int)const🔗
Returns the update mode of a value track.
Variantvalue_track_interpolate(track_idx:int, time_sec:float, backward:bool= false)const🔗
Returns the interpolated value at the given time (in seconds). Thetrack_idxmust be the index of a value track.
Abackwardmainly affects the direction of key retrieval of the track withUPDATE_DISCRETEconverted byAnimationMixer.ANIMATION_CALLBACK_MODE_DISCRETE_FORCE_CONTINUOUSto match the result withtrack_find_key().
voidvalue_track_set_update_mode(track_idx:int, mode:UpdateMode)🔗
Sets the update mode of a value track.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
