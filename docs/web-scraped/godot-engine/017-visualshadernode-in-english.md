# VisualShaderNode in English

# VisualShaderNode

Inherits:Resource<RefCounted<Object
Inherited By:VisualShaderNodeBillboard,VisualShaderNodeClamp,VisualShaderNodeColorFunc,VisualShaderNodeColorOp,VisualShaderNodeCompare,VisualShaderNodeConstant,VisualShaderNodeCubemap,VisualShaderNodeCustom,VisualShaderNodeDerivativeFunc,VisualShaderNodeDeterminant,VisualShaderNodeDistanceFade,VisualShaderNodeDotProduct,VisualShaderNodeFloatFunc,VisualShaderNodeFloatOp,VisualShaderNodeFresnel,VisualShaderNodeIf,VisualShaderNodeInput,VisualShaderNodeIntFunc,VisualShaderNodeIntOp,VisualShaderNodeIs,VisualShaderNodeLinearSceneDepth,VisualShaderNodeMix,VisualShaderNodeMultiplyAdd,VisualShaderNodeOuterProduct,VisualShaderNodeOutput,VisualShaderNodeParameter,VisualShaderNodeParameterRef,VisualShaderNodeParticleAccelerator,VisualShaderNodeParticleConeVelocity,VisualShaderNodeParticleEmit,VisualShaderNodeParticleEmitter,VisualShaderNodeParticleMultiplyByAxisAngle,VisualShaderNodeParticleRandomness,VisualShaderNodeProximityFade,VisualShaderNodeRandomRange,VisualShaderNodeRemap,VisualShaderNodeReroute,VisualShaderNodeResizableBase,VisualShaderNodeRotationByAxis,VisualShaderNodeSample3D,VisualShaderNodeScreenNormalWorldSpace,VisualShaderNodeScreenUVToSDF,VisualShaderNodeSDFRaymarch,VisualShaderNodeSDFToScreenUV,VisualShaderNodeSmoothStep,VisualShaderNodeStep,VisualShaderNodeSwitch,VisualShaderNodeTexture,VisualShaderNodeTextureSDF,VisualShaderNodeTextureSDFNormal,VisualShaderNodeTransformCompose,VisualShaderNodeTransformDecompose,VisualShaderNodeTransformFunc,VisualShaderNodeTransformOp,VisualShaderNodeTransformVecMult,VisualShaderNodeUIntFunc,VisualShaderNodeUIntOp,VisualShaderNodeUVFunc,VisualShaderNodeUVPolarCoord,VisualShaderNodeVarying,VisualShaderNodeVectorBase,VisualShaderNodeWorldPositionFromDepth
Base class forVisualShadernodes. Not related to scene nodes.

## Description

Visual shader graphs consist of various nodes. Each node in the graph is a separate object and they are represented as a rectangular boxes with title and a set of properties. Each node also has connection ports that allow to connect it to another nodes and control the flow of the shader.

## Tutorials

- Using VisualShaders
Using VisualShaders

## Properties

| int | linked_parent_graph_frame | -1 |
|---|---|---|
| int | output_port_for_preview | -1 |

linked_parent_graph_frame
output_port_for_preview

## Methods

| void | clear_default_input_values() |
|---|---|
| int | get_default_input_port(type:PortType)const |
| Array | get_default_input_values()const |
| Variant | get_input_port_default_value(port:int)const |
| void | remove_input_port_default_value(port:int) |
| void | set_default_input_values(values:Array) |
| void | set_input_port_default_value(port:int, value:Variant, prev_value:Variant= null) |

void
clear_default_input_values()
get_default_input_port(type:PortType)const
Array
get_default_input_values()const
Variant
get_input_port_default_value(port:int)const
void
remove_input_port_default_value(port:int)
void
set_default_input_values(values:Array)
void
set_input_port_default_value(port:int, value:Variant, prev_value:Variant= null)

## Enumerations

enumPortType:🔗
PortTypePORT_TYPE_SCALAR=0
Floating-point scalar. Translated tofloattype in shader code.
PortTypePORT_TYPE_SCALAR_INT=1
Integer scalar. Translated tointtype in shader code.
PortTypePORT_TYPE_SCALAR_UINT=2
Unsigned integer scalar. Translated touinttype in shader code.
PortTypePORT_TYPE_VECTOR_2D=3
2D vector of floating-point values. Translated tovec2type in shader code.
PortTypePORT_TYPE_VECTOR_3D=4
3D vector of floating-point values. Translated tovec3type in shader code.
PortTypePORT_TYPE_VECTOR_4D=5
4D vector of floating-point values. Translated tovec4type in shader code.
PortTypePORT_TYPE_BOOLEAN=6
Boolean type. Translated tobooltype in shader code.
PortTypePORT_TYPE_TRANSFORM=7
Transform type. Translated tomat4type in shader code.
PortTypePORT_TYPE_SAMPLER=8
Sampler type. Translated to reference of sampler uniform in shader code. Can only be used for input ports in non-uniform nodes.
PortTypePORT_TYPE_MAX=9
Represents the size of thePortTypeenum.

## Property Descriptions

intlinked_parent_graph_frame=-1🔗

- voidset_frame(value:int)
voidset_frame(value:int)
- intget_frame()
intget_frame()
Represents the index of the frame this node is linked to. If set to-1the node is not linked to any frame.
intoutput_port_for_preview=-1🔗
- voidset_output_port_for_preview(value:int)
voidset_output_port_for_preview(value:int)
- intget_output_port_for_preview()
intget_output_port_for_preview()
Sets the output port index which will be showed for preview. If set to-1no port will be open for preview.

## Method Descriptions

voidclear_default_input_values()🔗
Clears the default input ports value.
intget_default_input_port(type:PortType)const🔗
Returns the input port which should be connected by default when this node is created as a result of dragging a connection from an existing node to the empty space on the graph.
Arrayget_default_input_values()const🔗
Returns anArraycontaining default values for all of the input ports of the node in the form[index0,value0,index1,value1,...].
Variantget_input_port_default_value(port:int)const🔗
Returns the default value of the inputport.
voidremove_input_port_default_value(port:int)🔗
Removes the default value of the inputport.
voidset_default_input_values(values:Array)🔗
Sets the default input ports values using anArrayof the form[index0,value0,index1,value1,...]. For example:[0,Vector3(0,0,0),1,Vector3(0,0,0)].
voidset_input_port_default_value(port:int, value:Variant, prev_value:Variant= null)🔗
Sets the defaultvaluefor the selected inputport.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
