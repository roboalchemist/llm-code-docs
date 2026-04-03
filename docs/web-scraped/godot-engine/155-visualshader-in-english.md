# VisualShader in English

# VisualShader
Inherits:Shader<Resource<RefCounted<Object
A custom shader program with a visual editor.

## Description
This class provides a graph-like visual editor for creating aShader. AlthoughVisualShaders do not require coding, they share the same logic with script shaders. They useVisualShaderNodes that can be connected to each other to control the flow of the shader. The visual shader graph is converted to a script shader behind the scenes.

## Tutorials
- Using VisualShaders
Using VisualShaders

## Properties

| Vector2 | graph_offset |

Vector2
graph_offset

## Methods

| void | add_node(type:Type, node:VisualShaderNode, position:Vector2, id:int) |
|---|---|
| void | add_varying(name:String, mode:VaryingMode, type:VaryingType) |
| void | attach_node_to_frame(type:Type, id:int, frame:int) |
| bool | can_connect_nodes(type:Type, from_node:int, from_port:int, to_node:int, to_port:int)const |
| Error | connect_nodes(type:Type, from_node:int, from_port:int, to_node:int, to_port:int) |
| void | connect_nodes_forced(type:Type, from_node:int, from_port:int, to_node:int, to_port:int) |
| void | detach_node_from_frame(type:Type, id:int) |
| void | disconnect_nodes(type:Type, from_node:int, from_port:int, to_node:int, to_port:int) |
| VisualShaderNode | get_node(type:Type, id:int)const |
| Array[Dictionary] | get_node_connections(type:Type)const |
| PackedInt32Array | get_node_list(type:Type)const |
| Vector2 | get_node_position(type:Type, id:int)const |
| int | get_valid_node_id(type:Type)const |
| bool | has_varying(name:String)const |
| bool | is_node_connection(type:Type, from_node:int, from_port:int, to_node:int, to_port:int)const |
| void | remove_node(type:Type, id:int) |
| void | remove_varying(name:String) |
| void | replace_node(type:Type, id:int, new_class:StringName) |
| void | set_mode(mode:Mode) |
| void | set_node_position(type:Type, id:int, position:Vector2) |

void
add_node(type:Type, node:VisualShaderNode, position:Vector2, id:int)
void
add_varying(name:String, mode:VaryingMode, type:VaryingType)
void
attach_node_to_frame(type:Type, id:int, frame:int)
bool
can_connect_nodes(type:Type, from_node:int, from_port:int, to_node:int, to_port:int)const
Error
connect_nodes(type:Type, from_node:int, from_port:int, to_node:int, to_port:int)
void
connect_nodes_forced(type:Type, from_node:int, from_port:int, to_node:int, to_port:int)
void
detach_node_from_frame(type:Type, id:int)
void
disconnect_nodes(type:Type, from_node:int, from_port:int, to_node:int, to_port:int)
VisualShaderNode
get_node(type:Type, id:int)const
Array[Dictionary]
get_node_connections(type:Type)const
PackedInt32Array
get_node_list(type:Type)const
Vector2
get_node_position(type:Type, id:int)const
get_valid_node_id(type:Type)const
bool
has_varying(name:String)const
bool
is_node_connection(type:Type, from_node:int, from_port:int, to_node:int, to_port:int)const
void
remove_node(type:Type, id:int)
void
remove_varying(name:String)
void
replace_node(type:Type, id:int, new_class:StringName)
void
set_mode(mode:Mode)
void
set_node_position(type:Type, id:int, position:Vector2)

## Enumerations
enumType:🔗
TypeTYPE_VERTEX=0
A vertex shader, operating on vertices.
TypeTYPE_FRAGMENT=1
A fragment shader, operating on fragments (pixels).
TypeTYPE_LIGHT=2
A shader for light calculations.
TypeTYPE_START=3
A function for the "start" stage of particle shader.
TypeTYPE_PROCESS=4
A function for the "process" stage of particle shader.
TypeTYPE_COLLIDE=5
A function for the "collide" stage (particle collision handler) of particle shader.
TypeTYPE_START_CUSTOM=6
A function for the "start" stage of particle shader, with customized output.
TypeTYPE_PROCESS_CUSTOM=7
A function for the "process" stage of particle shader, with customized output.
TypeTYPE_SKY=8
A shader for 3D environment's sky.
TypeTYPE_FOG=9
A compute shader that runs for each froxel of the volumetric fog map.
TypeTYPE_MAX=10
Represents the size of theTypeenum.
enumVaryingMode:🔗
VaryingModeVARYING_MODE_VERTEX_TO_FRAG_LIGHT=0
Varying is passed fromVertexfunction toFragmentandLightfunctions.
VaryingModeVARYING_MODE_FRAG_TO_LIGHT=1
Varying is passed fromFragmentfunction toLightfunction.
VaryingModeVARYING_MODE_MAX=2
Represents the size of theVaryingModeenum.
enumVaryingType:🔗
VaryingTypeVARYING_TYPE_FLOAT=0
Varying is of typefloat.
VaryingTypeVARYING_TYPE_INT=1
Varying is of typeint.
VaryingTypeVARYING_TYPE_UINT=2
Varying is of type unsignedint.
VaryingTypeVARYING_TYPE_VECTOR_2D=3
Varying is of typeVector2.
VaryingTypeVARYING_TYPE_VECTOR_3D=4
Varying is of typeVector3.
VaryingTypeVARYING_TYPE_VECTOR_4D=5
Varying is of typeVector4.
VaryingTypeVARYING_TYPE_BOOLEAN=6
Varying is of typebool.
VaryingTypeVARYING_TYPE_TRANSFORM=7
Varying is of typeTransform3D.
VaryingTypeVARYING_TYPE_MAX=8
Represents the size of theVaryingTypeenum.

## Constants
NODE_ID_INVALID=-1🔗
Indicates an invalidVisualShadernode.
NODE_ID_OUTPUT=0🔗
Indicates an output node ofVisualShader.

## Property Descriptions
Vector2graph_offset🔗
- voidset_graph_offset(value:Vector2)
voidset_graph_offset(value:Vector2)
- Vector2get_graph_offset()
Vector2get_graph_offset()
Deprecated:This property does nothing and always equals to zero.
Deprecated.

## Method Descriptions
voidadd_node(type:Type, node:VisualShaderNode, position:Vector2, id:int)🔗
Adds the specifiednodeto the shader.
voidadd_varying(name:String, mode:VaryingMode, type:VaryingType)🔗
Adds a new varying value node to the shader.
voidattach_node_to_frame(type:Type, id:int, frame:int)🔗
Attaches the given node to the given frame.
boolcan_connect_nodes(type:Type, from_node:int, from_port:int, to_node:int, to_port:int)const🔗
Returnstrueif the specified nodes and ports can be connected together.
Errorconnect_nodes(type:Type, from_node:int, from_port:int, to_node:int, to_port:int)🔗
Connects the specified nodes and ports.
voidconnect_nodes_forced(type:Type, from_node:int, from_port:int, to_node:int, to_port:int)🔗
Connects the specified nodes and ports, even if they can't be connected. Such connection is invalid and will not function properly.
voiddetach_node_from_frame(type:Type, id:int)🔗
Detaches the given node from the frame it is attached to.
voiddisconnect_nodes(type:Type, from_node:int, from_port:int, to_node:int, to_port:int)🔗
Connects the specified nodes and ports.
VisualShaderNodeget_node(type:Type, id:int)const🔗
Returns the shader node instance with specifiedtypeandid.
Array[Dictionary]get_node_connections(type:Type)const🔗
Returns the list of connected nodes with the specified type.
PackedInt32Arrayget_node_list(type:Type)const🔗
Returns the list of all nodes in the shader with the specified type.
Vector2get_node_position(type:Type, id:int)const🔗
Returns the position of the specified node within the shader graph.
intget_valid_node_id(type:Type)const🔗
Returns next valid node ID that can be added to the shader graph.
boolhas_varying(name:String)const🔗
Returnstrueif the shader has a varying with the givenname.
boolis_node_connection(type:Type, from_node:int, from_port:int, to_node:int, to_port:int)const🔗
Returnstrueif the specified node and port connection exist.
voidremove_node(type:Type, id:int)🔗
Removes the specified node from the shader.
voidremove_varying(name:String)🔗
Removes a varying value node with the givenname. Prints an error if a node with this name is not found.
voidreplace_node(type:Type, id:int, new_class:StringName)🔗
Replaces the specified node with a node of new class type.
voidset_mode(mode:Mode)🔗
Sets the mode of this shader.
voidset_node_position(type:Type, id:int, position:Vector2)🔗
Sets the position of the specified node.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.