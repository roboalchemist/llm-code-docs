:github_url: hide



# VisualShaderNodeTransformCompose

**Inherits:** [VisualShaderNode<class_VisualShaderNode>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Composes a [Transform3D<class_Transform3D>] from four [Vector3<class_Vector3>]\ s within the visual shader graph.


## Description

Creates a 4×4 transform matrix using four vectors of type `vec3`. Each vector is one row in the matrix and the last column is a `vec4(0, 0, 0, 1)`.

