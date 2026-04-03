# AnimationMixer in English

# AnimationMixer
Inherits:Node<Object
Inherited By:AnimationPlayer,AnimationTree
Base class forAnimationPlayerandAnimationTree.

## Description
Base class forAnimationPlayerandAnimationTreeto manage animation lists. It also has general properties and methods for playback and blending.
After instantiating the playback information data within the extended class, the blending is processed by theAnimationMixer.

## Tutorials
- Migrating Animations from Godot 4.0 to 4.3
Migrating Animations from Godot 4.0 to 4.3

## Properties

| bool | active | true |
|---|---|---|
| int | audio_max_polyphony | 32 |
| AnimationCallbackModeDiscrete | callback_mode_discrete | 1 |
| AnimationCallbackModeMethod | callback_mode_method | 0 |
| AnimationCallbackModeProcess | callback_mode_process | 1 |
| bool | deterministic | false |
| bool | reset_on_save | true |
| bool | root_motion_local | false |
| NodePath | root_motion_track | NodePath("") |
| NodePath | root_node | NodePath("..") |

bool
active
true
audio_max_polyphony
AnimationCallbackModeDiscrete
callback_mode_discrete
AnimationCallbackModeMethod
callback_mode_method
AnimationCallbackModeProcess
callback_mode_process
bool
deterministic
false
bool
reset_on_save
true
bool
root_motion_local
false
NodePath
root_motion_track
NodePath("")
NodePath
root_node
NodePath("..")

## Methods

| Variant | _post_process_key_value(animation:Animation, track:int, value:Variant, object_id:int, object_sub_idx:int)virtualconst |
|---|---|
| Error | add_animation_library(name:StringName, library:AnimationLibrary) |
| void | advance(delta:float) |
| void | capture(name:StringName, duration:float, trans_type:TransitionType= 0, ease_type:EaseType= 0) |
| void | clear_caches() |
| StringName | find_animation(animation:Animation)const |
| StringName | find_animation_library(animation:Animation)const |
| Animation | get_animation(name:StringName)const |
| AnimationLibrary | get_animation_library(name:StringName)const |
| Array[StringName] | get_animation_library_list()const |
| PackedStringArray | get_animation_list()const |
| Vector3 | get_root_motion_position()const |
| Vector3 | get_root_motion_position_accumulator()const |
| Quaternion | get_root_motion_rotation()const |
| Quaternion | get_root_motion_rotation_accumulator()const |
| Vector3 | get_root_motion_scale()const |
| Vector3 | get_root_motion_scale_accumulator()const |
| bool | has_animation(name:StringName)const |
| bool | has_animation_library(name:StringName)const |
| void | remove_animation_library(name:StringName) |
| void | rename_animation_library(name:StringName, newname:StringName) |

Variant
_post_process_key_value(animation:Animation, track:int, value:Variant, object_id:int, object_sub_idx:int)virtualconst
Error
add_animation_library(name:StringName, library:AnimationLibrary)
void
advance(delta:float)
void
capture(name:StringName, duration:float, trans_type:TransitionType= 0, ease_type:EaseType= 0)
void
clear_caches()
StringName
find_animation(animation:Animation)const
StringName
find_animation_library(animation:Animation)const
Animation
get_animation(name:StringName)const
AnimationLibrary
get_animation_library(name:StringName)const
Array[StringName]
get_animation_library_list()const
PackedStringArray
get_animation_list()const
Vector3
get_root_motion_position()const
Vector3
get_root_motion_position_accumulator()const
Quaternion
get_root_motion_rotation()const
Quaternion
get_root_motion_rotation_accumulator()const
Vector3
get_root_motion_scale()const
Vector3
get_root_motion_scale_accumulator()const
bool
has_animation(name:StringName)const
bool
has_animation_library(name:StringName)const
void
remove_animation_library(name:StringName)
void
rename_animation_library(name:StringName, newname:StringName)

## Signals
animation_finished(anim_name:StringName)🔗
Notifies when an animation finished playing.
Note:This signal is not emitted if an animation is looping.
animation_libraries_updated()🔗
Notifies when the animation libraries have changed.
animation_list_changed()🔗
Notifies when an animation list is changed.
animation_started(anim_name:StringName)🔗
Notifies when an animation starts playing.
Note:This signal is not emitted if an animation is looping.
caches_cleared()🔗
Notifies when the caches have been cleared, either automatically, or manually viaclear_caches().
mixer_applied()🔗
Notifies when the blending result related have been applied to the target objects.
mixer_updated()🔗
Notifies when the property related process have been updated.

## Enumerations
enumAnimationCallbackModeProcess:🔗
AnimationCallbackModeProcessANIMATION_CALLBACK_MODE_PROCESS_PHYSICS=0
Process animation during physics frames (seeNode.NOTIFICATION_INTERNAL_PHYSICS_PROCESS). This is especially useful when animating physics bodies.
AnimationCallbackModeProcessANIMATION_CALLBACK_MODE_PROCESS_IDLE=1
Process animation during process frames (seeNode.NOTIFICATION_INTERNAL_PROCESS).
AnimationCallbackModeProcessANIMATION_CALLBACK_MODE_PROCESS_MANUAL=2
Do not process animation. Useadvance()to process the animation manually.
enumAnimationCallbackModeMethod:🔗
AnimationCallbackModeMethodANIMATION_CALLBACK_MODE_METHOD_DEFERRED=0
Batch method calls during the animation process, then do the calls after events are processed. This avoids bugs involving deleting nodes or modifying the AnimationPlayer while playing.
AnimationCallbackModeMethodANIMATION_CALLBACK_MODE_METHOD_IMMEDIATE=1
Make method calls immediately when reached in the animation.
enumAnimationCallbackModeDiscrete:🔗
AnimationCallbackModeDiscreteANIMATION_CALLBACK_MODE_DISCRETE_DOMINANT=0
AnAnimation.UPDATE_DISCRETEtrack value takes precedence when blendingAnimation.UPDATE_CONTINUOUSorAnimation.UPDATE_CAPTUREtrack values andAnimation.UPDATE_DISCRETEtrack values.
AnimationCallbackModeDiscreteANIMATION_CALLBACK_MODE_DISCRETE_RECESSIVE=1
AnAnimation.UPDATE_CONTINUOUSorAnimation.UPDATE_CAPTUREtrack value takes precedence when blending theAnimation.UPDATE_CONTINUOUSorAnimation.UPDATE_CAPTUREtrack values and theAnimation.UPDATE_DISCRETEtrack values. This is the default behavior forAnimationPlayer.
AnimationCallbackModeDiscreteANIMATION_CALLBACK_MODE_DISCRETE_FORCE_CONTINUOUS=2
Always treat theAnimation.UPDATE_DISCRETEtrack value asAnimation.UPDATE_CONTINUOUSwithAnimation.INTERPOLATION_NEAREST. This is the default behavior forAnimationTree.
If a value track has un-interpolatable type key values, it is internally converted to useANIMATION_CALLBACK_MODE_DISCRETE_RECESSIVEwithAnimation.UPDATE_DISCRETE.
Un-interpolatable type list:
- @GlobalScope.TYPE_NIL
@GlobalScope.TYPE_NIL
- @GlobalScope.TYPE_NODE_PATH
@GlobalScope.TYPE_NODE_PATH
- @GlobalScope.TYPE_RID
@GlobalScope.TYPE_RID
- @GlobalScope.TYPE_OBJECT
@GlobalScope.TYPE_OBJECT
- @GlobalScope.TYPE_CALLABLE
@GlobalScope.TYPE_CALLABLE
- @GlobalScope.TYPE_SIGNAL
@GlobalScope.TYPE_SIGNAL
- @GlobalScope.TYPE_DICTIONARY
@GlobalScope.TYPE_DICTIONARY
- @GlobalScope.TYPE_PACKED_BYTE_ARRAY
@GlobalScope.TYPE_PACKED_BYTE_ARRAY
@GlobalScope.TYPE_BOOLand@GlobalScope.TYPE_INTare treated as@GlobalScope.TYPE_FLOATduring blending and rounded when the result is retrieved.
It is same for arrays and vectors with them such as@GlobalScope.TYPE_PACKED_INT32_ARRAYor@GlobalScope.TYPE_VECTOR2I, they are treated as@GlobalScope.TYPE_PACKED_FLOAT32_ARRAYor@GlobalScope.TYPE_VECTOR2. Also note that for arrays, the size is also interpolated.
@GlobalScope.TYPE_STRINGand@GlobalScope.TYPE_STRING_NAMEare interpolated between character codes and lengths, but note that there is a difference in algorithm between interpolation between keys and interpolation by blending.

## Property Descriptions
boolactive=true🔗
- voidset_active(value:bool)
voidset_active(value:bool)
- boolis_active()
boolis_active()
Iftrue, theAnimationMixerwill be processing.
intaudio_max_polyphony=32🔗
- voidset_audio_max_polyphony(value:int)
voidset_audio_max_polyphony(value:int)
- intget_audio_max_polyphony()
intget_audio_max_polyphony()
The number of possible simultaneous sounds for each of the assigned AudioStreamPlayers.
For example, if this value is32and the animation has two audio tracks, the twoAudioStreamPlayers assigned can play simultaneously up to32voices each.
AnimationCallbackModeDiscretecallback_mode_discrete=1🔗
- voidset_callback_mode_discrete(value:AnimationCallbackModeDiscrete)
voidset_callback_mode_discrete(value:AnimationCallbackModeDiscrete)
- AnimationCallbackModeDiscreteget_callback_mode_discrete()
AnimationCallbackModeDiscreteget_callback_mode_discrete()
Ordinarily, tracks can be set toAnimation.UPDATE_DISCRETEto update infrequently, usually when using nearest interpolation.
However, when blending withAnimation.UPDATE_CONTINUOUSseveral results are considered. Thecallback_mode_discretespecify it explicitly. See alsoAnimationCallbackModeDiscrete.
To make the blended results look good, it is recommended to set this toANIMATION_CALLBACK_MODE_DISCRETE_FORCE_CONTINUOUSto update every frame during blending. Other values exist for compatibility and they are fine if there is no blending, but not so, may produce artifacts.
AnimationCallbackModeMethodcallback_mode_method=0🔗
- voidset_callback_mode_method(value:AnimationCallbackModeMethod)
voidset_callback_mode_method(value:AnimationCallbackModeMethod)
- AnimationCallbackModeMethodget_callback_mode_method()
AnimationCallbackModeMethodget_callback_mode_method()
The call mode used for "Call Method" tracks.
AnimationCallbackModeProcesscallback_mode_process=1🔗
- voidset_callback_mode_process(value:AnimationCallbackModeProcess)
voidset_callback_mode_process(value:AnimationCallbackModeProcess)
- AnimationCallbackModeProcessget_callback_mode_process()
AnimationCallbackModeProcessget_callback_mode_process()
The process notification in which to update animations.
booldeterministic=false🔗
- voidset_deterministic(value:bool)
voidset_deterministic(value:bool)
- boolis_deterministic()
boolis_deterministic()
Iftrue, the blending uses the deterministic algorithm. The total weight is not normalized and the result is accumulated with an initial value (0or a"RESET"animation if present).
This means that if the total amount of blending is0.0, the result is equal to the"RESET"animation.
If the number of tracks between the blended animations is different, the animation with the missing track is treated as if it had the initial value.
Iffalse, The blend does not use the deterministic algorithm. The total weight is normalized and always1.0. If the number of tracks between the blended animations is different, nothing is done about the animation that is missing a track.
Note:InAnimationTree, the blending withAnimationNodeAdd2,AnimationNodeAdd3,AnimationNodeSub2or the weight greater than1.0may produce unexpected results.
For example, ifAnimationNodeAdd2blends two nodes with the amount1.0, then total weight is2.0but it will be normalized to make the total amount1.0and the result will be equal toAnimationNodeBlend2with the amount0.5.
boolreset_on_save=true🔗
- voidset_reset_on_save_enabled(value:bool)
voidset_reset_on_save_enabled(value:bool)
- boolis_reset_on_save_enabled()
boolis_reset_on_save_enabled()
This is used by the editor. If set totrue, the scene will be saved with the effects of the reset animation (the animation with the key"RESET") applied as if it had been seeked to time 0, with the editor keeping the values that the scene had before saving.
This makes it more convenient to preview and edit animations in the editor, as changes to the scene will not be saved as long as they are set in the reset animation.
boolroot_motion_local=false🔗
- voidset_root_motion_local(value:bool)
voidset_root_motion_local(value:bool)
- boolis_root_motion_local()
boolis_root_motion_local()
Iftrue,get_root_motion_position()value is extracted as a local translation value before blending. In other words, it is treated like the translation is done after the rotation.
NodePathroot_motion_track=NodePath("")🔗
- voidset_root_motion_track(value:NodePath)
voidset_root_motion_track(value:NodePath)
- NodePathget_root_motion_track()
NodePathget_root_motion_track()
The path to the Animation track used for root motion. Paths must be valid scene-tree paths to a node, and must be specified starting from the parent node of the node that will reproduce the animation. Theroot_motion_trackuses the same format asAnimation.track_set_path(), but note that a bone must be specified.
If the track has typeAnimation.TYPE_POSITION_3D,Animation.TYPE_ROTATION_3D, orAnimation.TYPE_SCALE_3Dthe transformation will be canceled visually, and the animation will appear to stay in place. See alsoget_root_motion_position(),get_root_motion_rotation(),get_root_motion_scale(), andRootMotionView.
NodePathroot_node=NodePath("..")🔗
- voidset_root_node(value:NodePath)
voidset_root_node(value:NodePath)
- NodePathget_root_node()
NodePathget_root_node()
The node which node path references will travel from.

## Method Descriptions
Variant_post_process_key_value(animation:Animation, track:int, value:Variant, object_id:int, object_sub_idx:int)virtualconst🔗
A virtual function for processing after getting a key during playback.
Erroradd_animation_library(name:StringName, library:AnimationLibrary)🔗
Addslibraryto the animation player, under the keyname.
AnimationMixer has a global library by default with an empty string as key. For adding an animation to the global library:
```
var global_library = mixer.get_animation_library("")
global_library.add_animation("animation_name", animation_resource)
```
voidadvance(delta:float)🔗
Manually advance the animations by the specified time (in seconds).
voidcapture(name:StringName, duration:float, trans_type:TransitionType= 0, ease_type:EaseType= 0)🔗
If the animation track specified bynamehas an optionAnimation.UPDATE_CAPTURE, stores current values of the objects indicated by the track path as a cache. If there is already a captured cache, the old cache is discarded.
After this it will interpolate with current animation blending result during the playback process for the time specified byduration, working like a crossfade.
You can specifytrans_typeas the curve for the interpolation. For better results, it may be appropriate to specifyTween.TRANS_LINEARfor cases where the first key of the track begins with a non-zero value or where the key value does not change, andTween.TRANS_QUADfor cases where the key value changes linearly.
voidclear_caches()🔗
AnimationMixercaches animated nodes. It may not notice if a node disappears;clear_caches()forces it to update the cache again.
StringNamefind_animation(animation:Animation)const🔗
Returns the key ofanimationor an emptyStringNameif not found.
StringNamefind_animation_library(animation:Animation)const🔗
Returns the key for theAnimationLibrarythat containsanimationor an emptyStringNameif not found.
Animationget_animation(name:StringName)const🔗
Returns theAnimationwith the keyname. If the animation does not exist,nullis returned and an error is logged.
AnimationLibraryget_animation_library(name:StringName)const🔗
Returns the firstAnimationLibrarywith keynameornullif not found.
To get theAnimationMixer's global animation library, useget_animation_library("").
Array[StringName]get_animation_library_list()const🔗
Returns the list of stored library keys.
PackedStringArrayget_animation_list()const🔗
Returns the list of stored animation keys.
Vector3get_root_motion_position()const🔗
Retrieve the motion delta of position with theroot_motion_trackas aVector3that can be used elsewhere.
Ifroot_motion_trackis not a path to a track of typeAnimation.TYPE_POSITION_3D, returnsVector3(0,0,0).
See alsoroot_motion_trackandRootMotionView.
The most basic example is applying position toCharacterBody3D:
```
var current_rotation

func _process(delta):
    if Input.is_action_just_pressed("animate"):
        current_rotation = get_quaternion()
        state_machine.travel("Animate")
    var velocity = current_rotation * animation_tree.get_root_motion_position() / delta
    set_velocity(velocity)
    move_and_slide()
```
By using this in combination withget_root_motion_rotation_accumulator(), you can apply the root motion position more correctly to account for the rotation of the node.
```
func _process(delta):
    if Input.is_action_just_pressed("animate"):
        state_machine.travel("Animate")
    set_quaternion(get_quaternion() * animation_tree.get_root_motion_rotation())
    var velocity = (animation_tree.get_root_motion_rotation_accumulator().inverse() * get_quaternion()) * animation_tree.get_root_motion_position() / delta
    set_velocity(velocity)
    move_and_slide()
```
Ifroot_motion_localistrue, returns the pre-multiplied translation value with the inverted rotation.
In this case, the code can be written as follows:
```
func _process(delta):
    if Input.is_action_just_pressed("animate"):
        state_machine.travel("Animate")
    set_quaternion(get_quaternion() * animation_tree.get_root_motion_rotation())
    var velocity = get_quaternion() * animation_tree.get_root_motion_position() / delta
    set_velocity(velocity)
    move_and_slide()
```
Vector3get_root_motion_position_accumulator()const🔗
Retrieve the blended value of the position tracks with theroot_motion_trackas aVector3that can be used elsewhere.
This is useful in cases where you want to respect the initial key values of the animation.
For example, if an animation with only one keyVector3(0,0,0)is played in the previous frame and then an animation with only one keyVector3(1,0,1)is played in the next frame, the difference can be calculated as follows:
```
var prev_root_motion_position_accumulator

func _process(delta):
    if Input.is_action_just_pressed("animate"):
        state_machine.travel("Animate")
    var current_root_motion_position_accumulator = animation_tree.get_root_motion_position_accumulator()
    var difference = current_root_motion_position_accumulator - prev_root_motion_position_accumulator
    prev_root_motion_position_accumulator = current_root_motion_position_accumulator
    transform.origin += difference
```
However, if the animation loops, an unintended discrete change may occur, so this is only useful for some simple use cases.
Quaternionget_root_motion_rotation()const🔗
Retrieve the motion delta of rotation with theroot_motion_trackas aQuaternionthat can be used elsewhere.
Ifroot_motion_trackis not a path to a track of typeAnimation.TYPE_ROTATION_3D, returnsQuaternion(0,0,0,1).
See alsoroot_motion_trackandRootMotionView.
The most basic example is applying rotation toCharacterBody3D:
```
func _process(delta):
    if Input.is_action_just_pressed("animate"):
        state_machine.travel("Animate")
    set_quaternion(get_quaternion() * animation_tree.get_root_motion_rotation())
```
Quaternionget_root_motion_rotation_accumulator()const🔗
Retrieve the blended value of the rotation tracks with theroot_motion_trackas aQuaternionthat can be used elsewhere.
This is necessary to apply the root motion position correctly, taking rotation into account. See alsoget_root_motion_position().
Also, this is useful in cases where you want to respect the initial key values of the animation.
For example, if an animation with only one keyQuaternion(0,0,0,1)is played in the previous frame and then an animation with only one keyQuaternion(0,0.707,0,0.707)is played in the next frame, the difference can be calculated as follows:
```
var prev_root_motion_rotation_accumulator

func _process(delta):
    if Input.is_action_just_pressed("animate"):
        state_machine.travel("Animate")
    var current_root_motion_rotation_accumulator = animation_tree.get_root_motion_rotation_accumulator()
    var difference = prev_root_motion_rotation_accumulator.inverse() * current_root_motion_rotation_accumulator
    prev_root_motion_rotation_accumulator = current_root_motion_rotation_accumulator
    transform.basis *=  Basis(difference)
```
However, if the animation loops, an unintended discrete change may occur, so this is only useful for some simple use cases.
Vector3get_root_motion_scale()const🔗
Retrieve the motion delta of scale with theroot_motion_trackas aVector3that can be used elsewhere.
Ifroot_motion_trackis not a path to a track of typeAnimation.TYPE_SCALE_3D, returnsVector3(0,0,0).
See alsoroot_motion_trackandRootMotionView.
The most basic example is applying scale toCharacterBody3D:
```
var current_scale = Vector3(1, 1, 1)
var scale_accum = Vector3(1, 1, 1)

func _process(delta):
    if Input.is_action_just_pressed("animate"):
        current_scale = get_scale()
        scale_accum = Vector3(1, 1, 1)
        state_machine.travel("Animate")
    scale_accum += animation_tree.get_root_motion_scale()
    set_scale(current_scale * scale_accum)
```
Vector3get_root_motion_scale_accumulator()const🔗
Retrieve the blended value of the scale tracks with theroot_motion_trackas aVector3that can be used elsewhere.
For example, if an animation with only one keyVector3(1,1,1)is played in the previous frame and then an animation with only one keyVector3(2,2,2)is played in the next frame, the difference can be calculated as follows:
```
var prev_root_motion_scale_accumulator

func _process(delta):
    if Input.is_action_just_pressed("animate"):
        state_machine.travel("Animate")
    var current_root_motion_scale_accumulator = animation_tree.get_root_motion_scale_accumulator()
    var difference = current_root_motion_scale_accumulator - prev_root_motion_scale_accumulator
    prev_root_motion_scale_accumulator = current_root_motion_scale_accumulator
    transform.basis = transform.basis.scaled(difference)
```
However, if the animation loops, an unintended discrete change may occur, so this is only useful for some simple use cases.
boolhas_animation(name:StringName)const🔗
Returnstrueif theAnimationMixerstores anAnimationwith keyname.
boolhas_animation_library(name:StringName)const🔗
Returnstrueif theAnimationMixerstores anAnimationLibrarywith keyname.
voidremove_animation_library(name:StringName)🔗
Removes theAnimationLibraryassociated with the keyname.
voidrename_animation_library(name:StringName, newname:StringName)🔗
Moves theAnimationLibraryassociated with the keynameto the keynewname.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.