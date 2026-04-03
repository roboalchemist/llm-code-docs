# AnimationNodeStateMachine in English

# AnimationNodeStateMachine

Inherits:AnimationRootNode<AnimationNode<Resource<RefCounted<Object
A state machine with multipleAnimationRootNodes, used byAnimationTree.

## Description

Contains multipleAnimationRootNodes representing animation states, connected in a graph. State transitions can be configured to happen automatically or via code, using a shortest-path algorithm. Retrieve theAnimationNodeStateMachinePlaybackobject from theAnimationTreenode to control it programmatically.

```
var state_machine = $AnimationTree.get("parameters/playback")
state_machine.travel("some_state")
```

```
var stateMachine = GetNode<AnimationTree>("AnimationTree").Get("parameters/playback") as AnimationNodeStateMachinePlayback;
stateMachine.Travel("some_state");
```

## Tutorials

- Using AnimationTree
Using AnimationTree

## Properties

| bool | allow_transition_to_self | false |
|---|---|---|
| bool | reset_ends | false |
| StateMachineType | state_machine_type | 0 |

bool
allow_transition_to_self
false
bool
reset_ends
false
StateMachineType
state_machine_type

## Methods

| void | add_node(name:StringName, node:AnimationNode, position:Vector2= Vector2(0, 0)) |
|---|---|
| void | add_transition(from:StringName, to:StringName, transition:AnimationNodeStateMachineTransition) |
| Vector2 | get_graph_offset()const |
| AnimationNode | get_node(name:StringName)const |
| Array[StringName] | get_node_list()const |
| StringName | get_node_name(node:AnimationNode)const |
| Vector2 | get_node_position(name:StringName)const |
| AnimationNodeStateMachineTransition | get_transition(idx:int)const |
| int | get_transition_count()const |
| StringName | get_transition_from(idx:int)const |
| StringName | get_transition_to(idx:int)const |
| bool | has_node(name:StringName)const |
| bool | has_transition(from:StringName, to:StringName)const |
| void | remove_node(name:StringName) |
| void | remove_transition(from:StringName, to:StringName) |
| void | remove_transition_by_index(idx:int) |
| void | rename_node(name:StringName, new_name:StringName) |
| void | replace_node(name:StringName, node:AnimationNode) |
| void | set_graph_offset(offset:Vector2) |
| void | set_node_position(name:StringName, position:Vector2) |

void
add_node(name:StringName, node:AnimationNode, position:Vector2= Vector2(0, 0))
void
add_transition(from:StringName, to:StringName, transition:AnimationNodeStateMachineTransition)
Vector2
get_graph_offset()const
AnimationNode
get_node(name:StringName)const
Array[StringName]
get_node_list()const
StringName
get_node_name(node:AnimationNode)const
Vector2
get_node_position(name:StringName)const
AnimationNodeStateMachineTransition
get_transition(idx:int)const
get_transition_count()const
StringName
get_transition_from(idx:int)const
StringName
get_transition_to(idx:int)const
bool
has_node(name:StringName)const
bool
has_transition(from:StringName, to:StringName)const
void
remove_node(name:StringName)
void
remove_transition(from:StringName, to:StringName)
void
remove_transition_by_index(idx:int)
void
rename_node(name:StringName, new_name:StringName)
void
replace_node(name:StringName, node:AnimationNode)
void
set_graph_offset(offset:Vector2)
void
set_node_position(name:StringName, position:Vector2)

## Enumerations

enumStateMachineType:🔗
StateMachineTypeSTATE_MACHINE_TYPE_ROOT=0
Seeking to the beginning is treated as playing from the start state. Transition to the end state is treated as exiting the state machine.
StateMachineTypeSTATE_MACHINE_TYPE_NESTED=1
Seeking to the beginning is treated as seeking to the beginning of the animation in the current state. Transition to the end state, or the absence of transitions in each state, is treated as exiting the state machine.
StateMachineTypeSTATE_MACHINE_TYPE_GROUPED=2
This is a grouped state machine that can be controlled from a parent state machine. It does not work independently. There must be a state machine withstate_machine_typeofSTATE_MACHINE_TYPE_ROOTorSTATE_MACHINE_TYPE_NESTEDin the parent or ancestor.

## Property Descriptions

boolallow_transition_to_self=false🔗

- voidset_allow_transition_to_self(value:bool)
voidset_allow_transition_to_self(value:bool)
- boolis_allow_transition_to_self()
boolis_allow_transition_to_self()
Iftrue, allows teleport to the self state withAnimationNodeStateMachinePlayback.travel(). When the reset option is enabled inAnimationNodeStateMachinePlayback.travel(), the animation is restarted. Iffalse, nothing happens on the teleportation to the self state.
boolreset_ends=false🔗
- voidset_reset_ends(value:bool)
voidset_reset_ends(value:bool)
- boolare_ends_reset()
boolare_ends_reset()
Iftrue, treat the cross-fade to the start and end nodes as a blend with the RESET animation.
In most cases, when additional cross-fades are performed in the parentAnimationNodeof the state machine, setting this property tofalseand matching the cross-fade time of the parentAnimationNodeand the state machine's start node and end node gives good results.
StateMachineTypestate_machine_type=0🔗
- voidset_state_machine_type(value:StateMachineType)
voidset_state_machine_type(value:StateMachineType)
- StateMachineTypeget_state_machine_type()
StateMachineTypeget_state_machine_type()
This property can define the process of transitions for different use cases. See alsoStateMachineType.

## Method Descriptions

voidadd_node(name:StringName, node:AnimationNode, position:Vector2= Vector2(0, 0))🔗
Adds a new animation node to the graph. Thepositionis used for display in the editor.
voidadd_transition(from:StringName, to:StringName, transition:AnimationNodeStateMachineTransition)🔗
Adds a transition between the given animation nodes.
Vector2get_graph_offset()const🔗
Returns the draw offset of the graph. Used for display in the editor.
AnimationNodeget_node(name:StringName)const🔗
Returns the animation node with the given name.
Array[StringName]get_node_list()const🔗
Returns a list containing the names of all animation nodes in this state machine.
StringNameget_node_name(node:AnimationNode)const🔗
Returns the given animation node's name.
Vector2get_node_position(name:StringName)const🔗
Returns the given animation node's coordinates. Used for display in the editor.
AnimationNodeStateMachineTransitionget_transition(idx:int)const🔗
Returns the given transition.
intget_transition_count()const🔗
Returns the number of connections in the graph.
StringNameget_transition_from(idx:int)const🔗
Returns the given transition's start node.
StringNameget_transition_to(idx:int)const🔗
Returns the given transition's end node.
boolhas_node(name:StringName)const🔗
Returnstrueif the graph contains the given animation node.
boolhas_transition(from:StringName, to:StringName)const🔗
Returnstrueif there is a transition between the given animation nodes.
voidremove_node(name:StringName)🔗
Deletes the given animation node from the graph.
voidremove_transition(from:StringName, to:StringName)🔗
Deletes the transition between the two specified animation nodes.
voidremove_transition_by_index(idx:int)🔗
Deletes the given transition by index.
voidrename_node(name:StringName, new_name:StringName)🔗
Renames the given animation node.
voidreplace_node(name:StringName, node:AnimationNode)🔗
Replaces the given animation node with a new animation node.
voidset_graph_offset(offset:Vector2)🔗
Sets the draw offset of the graph. Used for display in the editor.
voidset_node_position(name:StringName, position:Vector2)🔗
Sets the animation node's coordinates. Used for display in the editor.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
