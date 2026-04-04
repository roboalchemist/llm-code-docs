:github_url: hide



# VisualShaderNodeResizableBase

**Inherits:** [VisualShaderNode<class_VisualShaderNode>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

**Inherited By:** [VisualShaderNodeCurveTexture<class_VisualShaderNodeCurveTexture>], [VisualShaderNodeCurveXYZTexture<class_VisualShaderNodeCurveXYZTexture>], [VisualShaderNodeFrame<class_VisualShaderNodeFrame>], [VisualShaderNodeGroupBase<class_VisualShaderNodeGroupBase>]

Base class for resizable nodes in a visual shader graph.


## Description

Resizable nodes have a handle that allows the user to adjust their size as needed.


## Properties

> **TABLE**
> :widths: auto
>
> +-------------------------------+----------------------------------------------------------------+-------------------+
> | :ref:`Vector2<class_Vector2>` | :ref:`size<class_VisualShaderNodeResizableBase_property_size>` | ``Vector2(0, 0)`` |
> +-------------------------------+----------------------------------------------------------------+-------------------+
>

----


## Property Descriptions



[Vector2<class_Vector2>] **size** = `Vector2(0, 0)` [🔗<class_VisualShaderNodeResizableBase_property_size>]


- |void| **set_size**\ (\ value\: [Vector2<class_Vector2>]\ )
- [Vector2<class_Vector2>] **get_size**\ (\ )

The size of the node in the visual shader graph.

