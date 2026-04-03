# AnimationNodeTimeSeek in English

# AnimationNodeTimeSeek
Inherits:AnimationNode<Resource<RefCounted<Object
A time-seeking animation node used inAnimationTree.

## Description
This animation node can be used to cause a seek command to happen to any sub-children of the animation graph. Use to play anAnimationfrom the start or a certain playback position inside theAnimationNodeBlendTree.
After setting the time and changing the animation playback, the time seek node automatically goes into sleep mode on the next process frame by setting itsseek_requestvalue to-1.0.
```
# Play child animation from the start.
animation_tree.set("parameters/TimeSeek/seek_request", 0.0)
# Alternative syntax (same result as above).
animation_tree["parameters/TimeSeek/seek_request"] = 0.0

# Play child animation from 12 second timestamp.
animation_tree.set("parameters/TimeSeek/seek_request", 12.0)
# Alternative syntax (same result as above).
animation_tree["parameters/TimeSeek/seek_request"] = 12.0
```
```
// Play child animation from the start.
animationTree.Set("parameters/TimeSeek/seek_request", 0.0);

// Play child animation from 12 second timestamp.
animationTree.Set("parameters/TimeSeek/seek_request", 12.0);
```

## Tutorials
- Using AnimationTree
Using AnimationTree

## Properties

| bool | explicit_elapse | true |

bool
explicit_elapse
true

## Property Descriptions
boolexplicit_elapse=true🔗
- voidset_explicit_elapse(value:bool)
voidset_explicit_elapse(value:bool)
- boolis_explicit_elapse()
boolis_explicit_elapse()
Iftrue, some processes are executed to handle keys between seeks, such as calculating root motion and finding the nearest discrete key.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.