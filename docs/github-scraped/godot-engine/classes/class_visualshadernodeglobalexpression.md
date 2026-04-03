:github_url: hide



# VisualShaderNodeGlobalExpression

**Inherits:** [VisualShaderNodeExpression<class_VisualShaderNodeExpression>] **<** [VisualShaderNodeGroupBase<class_VisualShaderNodeGroupBase>] **<** [VisualShaderNodeResizableBase<class_VisualShaderNodeResizableBase>] **<** [VisualShaderNode<class_VisualShaderNode>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

A custom global visual shader graph expression written in Godot Shading Language.


## Description

Custom Godot Shader Language expression, which is placed on top of the generated shader. You can place various function definitions inside to call later in [VisualShaderNodeExpression<class_VisualShaderNodeExpression>]\ s (which are injected in the main shader functions). You can also declare varyings, uniforms and global constants.

