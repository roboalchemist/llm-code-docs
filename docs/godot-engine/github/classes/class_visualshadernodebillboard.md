:github_url: hide



# VisualShaderNodeBillboard

**Inherits:** [VisualShaderNode<class_VisualShaderNode>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

A node that controls how the object faces the camera to be used within the visual shader graph.


## Description

The output port of this node needs to be connected to `Model View Matrix` port of [VisualShaderNodeOutput<class_VisualShaderNodeOutput>].


## Properties

> **TABLE**
> :widths: auto
>
> +--------------------------------------------------------------------+--------------------------------------------------------------------------------+-----------+
> | :ref:`BillboardType<enum_VisualShaderNodeBillboard_BillboardType>` | :ref:`billboard_type<class_VisualShaderNodeBillboard_property_billboard_type>` | ``1``     |
> +--------------------------------------------------------------------+--------------------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>`                                            | :ref:`keep_scale<class_VisualShaderNodeBillboard_property_keep_scale>`         | ``false`` |
> +--------------------------------------------------------------------+--------------------------------------------------------------------------------+-----------+
>

----


## Enumerations



enum **BillboardType**: [🔗<enum_VisualShaderNodeBillboard_BillboardType>]



[BillboardType<enum_VisualShaderNodeBillboard_BillboardType>] **BILLBOARD_TYPE_DISABLED** = `0`

Billboarding is disabled and the node does nothing.



[BillboardType<enum_VisualShaderNodeBillboard_BillboardType>] **BILLBOARD_TYPE_ENABLED** = `1`

A standard billboarding algorithm is enabled.



[BillboardType<enum_VisualShaderNodeBillboard_BillboardType>] **BILLBOARD_TYPE_FIXED_Y** = `2`

A billboarding algorithm to rotate around Y-axis is enabled.



[BillboardType<enum_VisualShaderNodeBillboard_BillboardType>] **BILLBOARD_TYPE_PARTICLES** = `3`

A billboarding algorithm designed to use on particles is enabled.



[BillboardType<enum_VisualShaderNodeBillboard_BillboardType>] **BILLBOARD_TYPE_MAX** = `4`

Represents the size of the [BillboardType<enum_VisualShaderNodeBillboard_BillboardType>] enum.


----


## Property Descriptions



[BillboardType<enum_VisualShaderNodeBillboard_BillboardType>] **billboard_type** = `1` [🔗<class_VisualShaderNodeBillboard_property_billboard_type>]


- |void| **set_billboard_type**\ (\ value\: [BillboardType<enum_VisualShaderNodeBillboard_BillboardType>]\ )
- [BillboardType<enum_VisualShaderNodeBillboard_BillboardType>] **get_billboard_type**\ (\ )

Controls how the object faces the camera.


----



[bool<class_bool>] **keep_scale** = `false` [🔗<class_VisualShaderNodeBillboard_property_keep_scale>]


- |void| **set_keep_scale_enabled**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_keep_scale_enabled**\ (\ )

If `true`, the shader will keep the scale set for the mesh. Otherwise, the scale is lost when billboarding.

