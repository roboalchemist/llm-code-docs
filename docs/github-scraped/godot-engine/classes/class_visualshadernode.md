:github_url: hide



# VisualShaderNode

**Inherits:** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

**Inherited By:** [VisualShaderNodeBillboard<class_VisualShaderNodeBillboard>], [VisualShaderNodeClamp<class_VisualShaderNodeClamp>], [VisualShaderNodeColorFunc<class_VisualShaderNodeColorFunc>], [VisualShaderNodeColorOp<class_VisualShaderNodeColorOp>], [VisualShaderNodeCompare<class_VisualShaderNodeCompare>], [VisualShaderNodeConstant<class_VisualShaderNodeConstant>], [VisualShaderNodeCubemap<class_VisualShaderNodeCubemap>], [VisualShaderNodeCustom<class_VisualShaderNodeCustom>], [VisualShaderNodeDerivativeFunc<class_VisualShaderNodeDerivativeFunc>], [VisualShaderNodeDeterminant<class_VisualShaderNodeDeterminant>], [VisualShaderNodeDistanceFade<class_VisualShaderNodeDistanceFade>], [VisualShaderNodeDotProduct<class_VisualShaderNodeDotProduct>], [VisualShaderNodeFloatFunc<class_VisualShaderNodeFloatFunc>], [VisualShaderNodeFloatOp<class_VisualShaderNodeFloatOp>], [VisualShaderNodeFresnel<class_VisualShaderNodeFresnel>], [VisualShaderNodeIf<class_VisualShaderNodeIf>], [VisualShaderNodeInput<class_VisualShaderNodeInput>], [VisualShaderNodeIntFunc<class_VisualShaderNodeIntFunc>], [VisualShaderNodeIntOp<class_VisualShaderNodeIntOp>], [VisualShaderNodeIs<class_VisualShaderNodeIs>], [VisualShaderNodeLinearSceneDepth<class_VisualShaderNodeLinearSceneDepth>], [VisualShaderNodeMix<class_VisualShaderNodeMix>], [VisualShaderNodeMultiplyAdd<class_VisualShaderNodeMultiplyAdd>], [VisualShaderNodeOuterProduct<class_VisualShaderNodeOuterProduct>], [VisualShaderNodeOutput<class_VisualShaderNodeOutput>], [VisualShaderNodeParameter<class_VisualShaderNodeParameter>], [VisualShaderNodeParameterRef<class_VisualShaderNodeParameterRef>], [VisualShaderNodeParticleAccelerator<class_VisualShaderNodeParticleAccelerator>], [VisualShaderNodeParticleConeVelocity<class_VisualShaderNodeParticleConeVelocity>], [VisualShaderNodeParticleEmit<class_VisualShaderNodeParticleEmit>], [VisualShaderNodeParticleEmitter<class_VisualShaderNodeParticleEmitter>], [VisualShaderNodeParticleMultiplyByAxisAngle<class_VisualShaderNodeParticleMultiplyByAxisAngle>], [VisualShaderNodeParticleRandomness<class_VisualShaderNodeParticleRandomness>], [VisualShaderNodeProximityFade<class_VisualShaderNodeProximityFade>], [VisualShaderNodeRandomRange<class_VisualShaderNodeRandomRange>], [VisualShaderNodeRemap<class_VisualShaderNodeRemap>], [VisualShaderNodeReroute<class_VisualShaderNodeReroute>], [VisualShaderNodeResizableBase<class_VisualShaderNodeResizableBase>], [VisualShaderNodeRotationByAxis<class_VisualShaderNodeRotationByAxis>], [VisualShaderNodeSample3D<class_VisualShaderNodeSample3D>], [VisualShaderNodeScreenNormalWorldSpace<class_VisualShaderNodeScreenNormalWorldSpace>], [VisualShaderNodeScreenUVToSDF<class_VisualShaderNodeScreenUVToSDF>], [VisualShaderNodeSDFRaymarch<class_VisualShaderNodeSDFRaymarch>], [VisualShaderNodeSDFToScreenUV<class_VisualShaderNodeSDFToScreenUV>], [VisualShaderNodeSmoothStep<class_VisualShaderNodeSmoothStep>], [VisualShaderNodeStep<class_VisualShaderNodeStep>], [VisualShaderNodeSwitch<class_VisualShaderNodeSwitch>], [VisualShaderNodeTexture<class_VisualShaderNodeTexture>], [VisualShaderNodeTextureSDF<class_VisualShaderNodeTextureSDF>], [VisualShaderNodeTextureSDFNormal<class_VisualShaderNodeTextureSDFNormal>], [VisualShaderNodeTransformCompose<class_VisualShaderNodeTransformCompose>], [VisualShaderNodeTransformDecompose<class_VisualShaderNodeTransformDecompose>], [VisualShaderNodeTransformFunc<class_VisualShaderNodeTransformFunc>], [VisualShaderNodeTransformOp<class_VisualShaderNodeTransformOp>], [VisualShaderNodeTransformVecMult<class_VisualShaderNodeTransformVecMult>], [VisualShaderNodeUIntFunc<class_VisualShaderNodeUIntFunc>], [VisualShaderNodeUIntOp<class_VisualShaderNodeUIntOp>], [VisualShaderNodeUVFunc<class_VisualShaderNodeUVFunc>], [VisualShaderNodeUVPolarCoord<class_VisualShaderNodeUVPolarCoord>], [VisualShaderNodeVarying<class_VisualShaderNodeVarying>], [VisualShaderNodeVectorBase<class_VisualShaderNodeVectorBase>], [VisualShaderNodeWorldPositionFromDepth<class_VisualShaderNodeWorldPositionFromDepth>]

Base class for [VisualShader<class_VisualShader>] nodes. Not related to scene nodes.


## Description

Visual shader graphs consist of various nodes. Each node in the graph is a separate object and they are represented as a rectangular boxes with title and a set of properties. Each node also has connection ports that allow to connect it to another nodes and control the flow of the shader.


## Tutorials

- [../tutorials/shaders/visual_shaders](Using VisualShaders .md)


## Properties

> **TABLE**
> :widths: auto
>
> +-----------------------+---------------------------------------------------------------------------------------------+--------+
> | :ref:`int<class_int>` | :ref:`linked_parent_graph_frame<class_VisualShaderNode_property_linked_parent_graph_frame>` | ``-1`` |
> +-----------------------+---------------------------------------------------------------------------------------------+--------+
> | :ref:`int<class_int>` | :ref:`output_port_for_preview<class_VisualShaderNode_property_output_port_for_preview>`     | ``-1`` |
> +-----------------------+---------------------------------------------------------------------------------------------+--------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +-------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                        | :ref:`clear_default_input_values<class_VisualShaderNode_method_clear_default_input_values>`\ (\ )                                                                                                                             |
> +-------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`         | :ref:`get_default_input_port<class_VisualShaderNode_method_get_default_input_port>`\ (\ type\: :ref:`PortType<enum_VisualShaderNode_PortType>`\ ) |const|                                                                     |
> +-------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`     | :ref:`get_default_input_values<class_VisualShaderNode_method_get_default_input_values>`\ (\ ) |const|                                                                                                                         |
> +-------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Variant<class_Variant>` | :ref:`get_input_port_default_value<class_VisualShaderNode_method_get_input_port_default_value>`\ (\ port\: :ref:`int<class_int>`\ ) |const|                                                                                   |
> +-------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                        | :ref:`remove_input_port_default_value<class_VisualShaderNode_method_remove_input_port_default_value>`\ (\ port\: :ref:`int<class_int>`\ )                                                                                     |
> +-------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                        | :ref:`set_default_input_values<class_VisualShaderNode_method_set_default_input_values>`\ (\ values\: :ref:`Array<class_Array>`\ )                                                                                             |
> +-------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                        | :ref:`set_input_port_default_value<class_VisualShaderNode_method_set_input_port_default_value>`\ (\ port\: :ref:`int<class_int>`, value\: :ref:`Variant<class_Variant>`, prev_value\: :ref:`Variant<class_Variant>` = null\ ) |
> +-------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Enumerations



enum **PortType**: [🔗<enum_VisualShaderNode_PortType>]



[PortType<enum_VisualShaderNode_PortType>] **PORT_TYPE_SCALAR** = `0`

Floating-point scalar. Translated to `float` type in shader code.



[PortType<enum_VisualShaderNode_PortType>] **PORT_TYPE_SCALAR_INT** = `1`

Integer scalar. Translated to `int` type in shader code.



[PortType<enum_VisualShaderNode_PortType>] **PORT_TYPE_SCALAR_UINT** = `2`

Unsigned integer scalar. Translated to `uint` type in shader code.



[PortType<enum_VisualShaderNode_PortType>] **PORT_TYPE_VECTOR_2D** = `3`

2D vector of floating-point values. Translated to `vec2` type in shader code.



[PortType<enum_VisualShaderNode_PortType>] **PORT_TYPE_VECTOR_3D** = `4`

3D vector of floating-point values. Translated to `vec3` type in shader code.



[PortType<enum_VisualShaderNode_PortType>] **PORT_TYPE_VECTOR_4D** = `5`

4D vector of floating-point values. Translated to `vec4` type in shader code.



[PortType<enum_VisualShaderNode_PortType>] **PORT_TYPE_BOOLEAN** = `6`

Boolean type. Translated to `bool` type in shader code.



[PortType<enum_VisualShaderNode_PortType>] **PORT_TYPE_TRANSFORM** = `7`

Transform type. Translated to `mat4` type in shader code.



[PortType<enum_VisualShaderNode_PortType>] **PORT_TYPE_SAMPLER** = `8`

Sampler type. Translated to reference of sampler uniform in shader code. Can only be used for input ports in non-uniform nodes.



[PortType<enum_VisualShaderNode_PortType>] **PORT_TYPE_MAX** = `9`

Represents the size of the [PortType<enum_VisualShaderNode_PortType>] enum.


----


## Property Descriptions



[int<class_int>] **linked_parent_graph_frame** = `-1` [🔗<class_VisualShaderNode_property_linked_parent_graph_frame>]


- |void| **set_frame**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_frame**\ (\ )

Represents the index of the frame this node is linked to. If set to `-1` the node is not linked to any frame.


----



[int<class_int>] **output_port_for_preview** = `-1` [🔗<class_VisualShaderNode_property_output_port_for_preview>]


- |void| **set_output_port_for_preview**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_output_port_for_preview**\ (\ )

Sets the output port index which will be showed for preview. If set to `-1` no port will be open for preview.


----


## Method Descriptions



|void| **clear_default_input_values**\ (\ ) [🔗<class_VisualShaderNode_method_clear_default_input_values>]

Clears the default input ports value.


----



[int<class_int>] **get_default_input_port**\ (\ type\: [PortType<enum_VisualShaderNode_PortType>]\ ) |const| [🔗<class_VisualShaderNode_method_get_default_input_port>]

Returns the input port which should be connected by default when this node is created as a result of dragging a connection from an existing node to the empty space on the graph.


----



[Array<class_Array>] **get_default_input_values**\ (\ ) |const| [🔗<class_VisualShaderNode_method_get_default_input_values>]

Returns an [Array<class_Array>] containing default values for all of the input ports of the node in the form `[index0, value0, index1, value1, ...]`.


----



[Variant<class_Variant>] **get_input_port_default_value**\ (\ port\: [int<class_int>]\ ) |const| [🔗<class_VisualShaderNode_method_get_input_port_default_value>]

Returns the default value of the input `port`.


----



|void| **remove_input_port_default_value**\ (\ port\: [int<class_int>]\ ) [🔗<class_VisualShaderNode_method_remove_input_port_default_value>]

Removes the default value of the input `port`.


----



|void| **set_default_input_values**\ (\ values\: [Array<class_Array>]\ ) [🔗<class_VisualShaderNode_method_set_default_input_values>]

Sets the default input ports values using an [Array<class_Array>] of the form `[index0, value0, index1, value1, ...]`. For example: `[0, Vector3(0, 0, 0), 1, Vector3(0, 0, 0)]`.


----



|void| **set_input_port_default_value**\ (\ port\: [int<class_int>], value\: [Variant<class_Variant>], prev_value\: [Variant<class_Variant>] = null\ ) [🔗<class_VisualShaderNode_method_set_input_port_default_value>]

Sets the default `value` for the selected input `port`.

