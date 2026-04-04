# AnimationTree

# AnimationTree
Inherits:AnimationMixer<Node<Object
A node used for advanced animation transitions in anAnimationPlayer.

## Description
A node used for advanced animation transitions in anAnimationPlayer.
Note:When linked with anAnimationPlayer, several properties and methods of the correspondingAnimationPlayerwill not function as expected. Playback and transitions should be handled using only theAnimationTreeand its constituentAnimationNode(s). TheAnimationPlayernode should be used solely for adding, deleting, and editing animations.

## Tutorials
- Using AnimationTree
Using AnimationTree
- Third Person Shooter (TPS) Demo
Third Person Shooter (TPS) Demo

## Properties

| NodePath | advance_expression_base_node | NodePath(".") |
|---|---|---|
| NodePath | anim_player | NodePath("") |
| AnimationCallbackModeDiscrete | callback_mode_discrete | 2(overridesAnimationMixer) |
| bool | deterministic | true(overridesAnimationMixer) |
| AnimationRootNode | tree_root |  |

NodePath
advance_expression_base_node
NodePath(".")
NodePath
anim_player
NodePath("")
AnimationCallbackModeDiscrete
callback_mode_discrete
2(overridesAnimationMixer)
bool
deterministic
true(overridesAnimationMixer)
AnimationRootNode
tree_root

## Methods

| AnimationProcessCallback | get_process_callback()const |
|---|---|
| void | set_process_callback(mode:AnimationProcessCallback) |

AnimationProcessCallback
get_process_callback()const
void
set_process_callback(mode:AnimationProcessCallback)

## Signals
animation_player_changed()🔗
Emitted when theanim_playeris changed.

## Enumerations
enumAnimationProcessCallback:🔗
AnimationProcessCallbackANIMATION_PROCESS_PHYSICS=0
Deprecated:SeeAnimationMixer.ANIMATION_CALLBACK_MODE_PROCESS_PHYSICS.
AnimationProcessCallbackANIMATION_PROCESS_IDLE=1
Deprecated:SeeAnimationMixer.ANIMATION_CALLBACK_MODE_PROCESS_IDLE.
AnimationProcessCallbackANIMATION_PROCESS_MANUAL=2
Deprecated:SeeAnimationMixer.ANIMATION_CALLBACK_MODE_PROCESS_MANUAL.

## Property Descriptions
NodePathadvance_expression_base_node=NodePath(".")🔗
- voidset_advance_expression_base_node(value:NodePath)
voidset_advance_expression_base_node(value:NodePath)
- NodePathget_advance_expression_base_node()
NodePathget_advance_expression_base_node()
The path to theNodeused to evaluate theAnimationNodeExpressionif one is not explicitly specified internally.
NodePathanim_player=NodePath("")🔗
- voidset_animation_player(value:NodePath)
voidset_animation_player(value:NodePath)
- NodePathget_animation_player()
NodePathget_animation_player()
The path to theAnimationPlayerused for animating.
AnimationRootNodetree_root🔗
- voidset_tree_root(value:AnimationRootNode)
voidset_tree_root(value:AnimationRootNode)
- AnimationRootNodeget_tree_root()
AnimationRootNodeget_tree_root()
The root animation node of thisAnimationTree. SeeAnimationRootNode.

## Method Descriptions
AnimationProcessCallbackget_process_callback()const🔗
Deprecated:UseAnimationMixer.callback_mode_processinstead.
Returns the process notification in which to update animations.
voidset_process_callback(mode:AnimationProcessCallback)🔗
Deprecated:UseAnimationMixer.callback_mode_processinstead.
Sets the process notification in which to update animations.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.