# AnimationNode in English

# AnimationNode

Inherits:Resource<RefCounted<Object
Inherited By:AnimationNodeExtension,AnimationNodeOutput,AnimationNodeSync,AnimationNodeTimeScale,AnimationNodeTimeSeek,AnimationRootNode
Base class forAnimationTreenodes. Not related to scene nodes.

## Description

Base resource forAnimationTreenodes. In general, it's not used directly, but you can create custom ones with custom blending formulas.
Inherit this when creating animation nodes mainly for use inAnimationNodeBlendTree, otherwiseAnimationRootNodeshould be used instead.
You can access the time information as read-only parameter which is processed and stored in the previous frame for all nodes exceptAnimationNodeOutput.
Note:If multiple inputs exist in theAnimationNode, which time information takes precedence depends on the type ofAnimationNode.

```
var current_length = $AnimationTree["parameters/AnimationNodeName/current_length"]
var current_position = $AnimationTree["parameters/AnimationNodeName/current_position"]
var current_delta = $AnimationTree["parameters/AnimationNodeName/current_delta"]
```

## Tutorials

- Using AnimationTree
Using AnimationTree

## Properties

| bool | filter_enabled |

bool
filter_enabled

## Methods

| String | _get_caption()virtualconst |
|---|---|
| AnimationNode | _get_child_by_name(name:StringName)virtualconst |
| Dictionary | _get_child_nodes()virtualconst |
| Variant | _get_parameter_default_value(parameter:StringName)virtualconst |
| Array | _get_parameter_list()virtualconst |
| bool | _has_filter()virtualconst |
| bool | _is_parameter_read_only(parameter:StringName)virtualconst |
| float | _process(time:float, seek:bool, is_external_seeking:bool, test_only:bool)virtual |
| bool | add_input(name:String) |
| void | blend_animation(animation:StringName, time:float, delta:float, seeked:bool, is_external_seeking:bool, blend:float, looped_flag:LoopedFlag= 0) |
| float | blend_input(input_index:int, time:float, seek:bool, is_external_seeking:bool, blend:float, filter:FilterAction= 0, sync:bool= true, test_only:bool= false) |
| float | blend_node(name:StringName, node:AnimationNode, time:float, seek:bool, is_external_seeking:bool, blend:float, filter:FilterAction= 0, sync:bool= true, test_only:bool= false) |
| int | find_input(name:String)const |
| int | get_input_count()const |
| String | get_input_name(input:int)const |
| Variant | get_parameter(name:StringName)const |
| int | get_processing_animation_tree_instance_id()const |
| bool | is_path_filtered(path:NodePath)const |
| bool | is_process_testing()const |
| void | remove_input(index:int) |
| void | set_filter_path(path:NodePath, enable:bool) |
| bool | set_input_name(input:int, name:String) |
| void | set_parameter(name:StringName, value:Variant) |

String
_get_caption()virtualconst
AnimationNode
_get_child_by_name(name:StringName)virtualconst
Dictionary
_get_child_nodes()virtualconst
Variant
_get_parameter_default_value(parameter:StringName)virtualconst
Array
_get_parameter_list()virtualconst
bool
_has_filter()virtualconst
bool
_is_parameter_read_only(parameter:StringName)virtualconst
float
_process(time:float, seek:bool, is_external_seeking:bool, test_only:bool)virtual
bool
add_input(name:String)
void
blend_animation(animation:StringName, time:float, delta:float, seeked:bool, is_external_seeking:bool, blend:float, looped_flag:LoopedFlag= 0)
float
blend_input(input_index:int, time:float, seek:bool, is_external_seeking:bool, blend:float, filter:FilterAction= 0, sync:bool= true, test_only:bool= false)
float
blend_node(name:StringName, node:AnimationNode, time:float, seek:bool, is_external_seeking:bool, blend:float, filter:FilterAction= 0, sync:bool= true, test_only:bool= false)
find_input(name:String)const
get_input_count()const
String
get_input_name(input:int)const
Variant
get_parameter(name:StringName)const
get_processing_animation_tree_instance_id()const
bool
is_path_filtered(path:NodePath)const
bool
is_process_testing()const
void
remove_input(index:int)
void
set_filter_path(path:NodePath, enable:bool)
bool
set_input_name(input:int, name:String)
void
set_parameter(name:StringName, value:Variant)

## Signals

animation_node_removed(object_id:int, name:String)🔗
Emitted by nodes that inherit from this class and that have an internal tree when one of their animation nodes removes. The animation nodes that emit this signal areAnimationNodeBlendSpace1D,AnimationNodeBlendSpace2D,AnimationNodeStateMachine, andAnimationNodeBlendTree.
animation_node_renamed(object_id:int, old_name:String, new_name:String)🔗
Emitted by nodes that inherit from this class and that have an internal tree when one of their animation node names changes. The animation nodes that emit this signal areAnimationNodeBlendSpace1D,AnimationNodeBlendSpace2D,AnimationNodeStateMachine, andAnimationNodeBlendTree.
tree_changed()🔗
Emitted by nodes that inherit from this class and that have an internal tree when one of their animation nodes changes. The animation nodes that emit this signal areAnimationNodeBlendSpace1D,AnimationNodeBlendSpace2D,AnimationNodeStateMachine,AnimationNodeBlendTreeandAnimationNodeTransition.

## Enumerations

enumFilterAction:🔗
FilterActionFILTER_IGNORE=0
Do not use filtering.
FilterActionFILTER_PASS=1
Paths matching the filter will be allowed to pass.
FilterActionFILTER_STOP=2
Paths matching the filter will be discarded.
FilterActionFILTER_BLEND=3
Paths matching the filter will be blended (by the blend value).

## Property Descriptions

boolfilter_enabled🔗

- voidset_filter_enabled(value:bool)
voidset_filter_enabled(value:bool)
- boolis_filter_enabled()
boolis_filter_enabled()
Iftrue, filtering is enabled.

## Method Descriptions

String_get_caption()virtualconst🔗
When inheriting fromAnimationRootNode, implement this virtual method to override the text caption for this animation node.
AnimationNode_get_child_by_name(name:StringName)virtualconst🔗
When inheriting fromAnimationRootNode, implement this virtual method to return a child animation node by itsname.
Dictionary_get_child_nodes()virtualconst🔗
When inheriting fromAnimationRootNode, implement this virtual method to return all child animation nodes in order as aname:nodedictionary.
Variant_get_parameter_default_value(parameter:StringName)virtualconst🔗
When inheriting fromAnimationRootNode, implement this virtual method to return the default value of aparameter. Parameters are custom local memory used for your animation nodes, given a resource can be reused in multiple trees.
Array_get_parameter_list()virtualconst🔗
When inheriting fromAnimationRootNode, implement this virtual method to return a list of the properties on this animation node. Parameters are custom local memory used for your animation nodes, given a resource can be reused in multiple trees. Format is similar toObject.get_property_list().
bool_has_filter()virtualconst🔗
When inheriting fromAnimationRootNode, implement this virtual method to return whether the blend tree editor should display filter editing on this animation node.
bool_is_parameter_read_only(parameter:StringName)virtualconst🔗
When inheriting fromAnimationRootNode, implement this virtual method to return whether theparameteris read-only. Parameters are custom local memory used for your animation nodes, given a resource can be reused in multiple trees.
float_process(time:float, seek:bool, is_external_seeking:bool, test_only:bool)virtual🔗
Deprecated:Currently this is mostly useless as there is a lack of many APIs to extend AnimationNode by GDScript. It is planned that a more flexible API using structures will be provided in the future.
When inheriting fromAnimationRootNode, implement this virtual method to run some code when this animation node is processed. Thetimeparameter is a relative delta, unlessseekistrue, in which case it is absolute.
Here, call theblend_input(),blend_node()orblend_animation()functions. You can also useget_parameter()andset_parameter()to modify local memory.
This function should return the delta.
booladd_input(name:String)🔗
Adds an input to the animation node. This is only useful for animation nodes created for use in anAnimationNodeBlendTree. If the addition fails, returnsfalse.
voidblend_animation(animation:StringName, time:float, delta:float, seeked:bool, is_external_seeking:bool, blend:float, looped_flag:LoopedFlag= 0)🔗
Blends an animation byblendamount (name must be valid in the linkedAnimationPlayer). Atimeanddeltamay be passed, as well as whetherseekedhappened.
Alooped_flagis used by internal processing immediately after the loop.
floatblend_input(input_index:int, time:float, seek:bool, is_external_seeking:bool, blend:float, filter:FilterAction= 0, sync:bool= true, test_only:bool= false)🔗
Blends an input. This is only useful for animation nodes created for anAnimationNodeBlendTree. Thetimeparameter is a relative delta, unlessseekistrue, in which case it is absolute. A filter mode may be optionally passed.
floatblend_node(name:StringName, node:AnimationNode, time:float, seek:bool, is_external_seeking:bool, blend:float, filter:FilterAction= 0, sync:bool= true, test_only:bool= false)🔗
Blend another animation node (in case this animation node contains child animation nodes). This function is only useful if you inherit fromAnimationRootNodeinstead, otherwise editors will not display your animation node for addition.
intfind_input(name:String)const🔗
Returns the input index which corresponds toname. If not found, returns-1.
intget_input_count()const🔗
Amount of inputs in this animation node, only useful for animation nodes that go intoAnimationNodeBlendTree.
Stringget_input_name(input:int)const🔗
Gets the name of an input by index.
Variantget_parameter(name:StringName)const🔗
Gets the value of a parameter. Parameters are custom local memory used for your animation nodes, given a resource can be reused in multiple trees.
intget_processing_animation_tree_instance_id()const🔗
Returns the object id of theAnimationTreethat owns this node.
Note:This method should only be called from within theAnimationNodeExtension._process_animation_node()method, and will return an invalid id otherwise.
boolis_path_filtered(path:NodePath)const🔗
Returnstrueif the given path is filtered.
boolis_process_testing()const🔗
Returnstrueif this animation node is being processed in test-only mode.
voidremove_input(index:int)🔗
Removes an input, call this only when inactive.
voidset_filter_path(path:NodePath, enable:bool)🔗
Adds or removes a path for the filter.
boolset_input_name(input:int, name:String)🔗
Sets the name of the input at the giveninputindex. If the setting fails, returnsfalse.
voidset_parameter(name:StringName, value:Variant)🔗
Sets a custom parameter. These are used as local memory, because resources can be reused across the tree or scenes.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
