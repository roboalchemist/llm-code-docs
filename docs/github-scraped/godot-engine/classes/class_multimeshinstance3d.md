:github_url: hide

> **META**
	:keywords: batch



# MultiMeshInstance3D

**Inherits:** [GeometryInstance3D<class_GeometryInstance3D>] **<** [VisualInstance3D<class_VisualInstance3D>] **<** [Node3D<class_Node3D>] **<** [Node<class_Node>] **<** [Object<class_Object>]

Node that instances a [MultiMesh<class_MultiMesh>].


## Description

**MultiMeshInstance3D** is a specialized node to instance [GeometryInstance3D<class_GeometryInstance3D>]\ s based on a [MultiMesh<class_MultiMesh>] resource.

This is useful to optimize the rendering of a high number of instances of a given mesh (for example trees in a forest or grass strands).


## Tutorials

- [../tutorials/3d/using_multi_mesh_instance](Using MultiMeshInstance .md)

- [../tutorials/performance/using_multimesh](Optimization using MultiMeshes .md)

- [../tutorials/performance/vertex_animation/animating_thousands_of_fish](Animating thousands of fish with MultiMeshInstance .md)


## Properties

> **TABLE**
> :widths: auto
>
> +-----------------------------------+----------------------------------------------------------------+
> | :ref:`MultiMesh<class_MultiMesh>` | :ref:`multimesh<class_MultiMeshInstance3D_property_multimesh>` |
> +-----------------------------------+----------------------------------------------------------------+
>

----


## Property Descriptions



[MultiMesh<class_MultiMesh>] **multimesh** [🔗<class_MultiMeshInstance3D_property_multimesh>]


- |void| **set_multimesh**\ (\ value\: [MultiMesh<class_MultiMesh>]\ )
- [MultiMesh<class_MultiMesh>] **get_multimesh**\ (\ )

The [MultiMesh<class_MultiMesh>] resource that will be used and shared among all instances of the **MultiMeshInstance3D**.

