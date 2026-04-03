:github_url: hide



# SkinReference

**Inherits:** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

A reference-counted holder object for a skeleton RID used in the [RenderingServer<class_RenderingServer>].


## Description

An internal object containing a mapping from a [Skin<class_Skin>] used within the context of a particular [MeshInstance3D<class_MeshInstance3D>] to refer to the skeleton's [RID<class_RID>] in the RenderingServer.

See also [MeshInstance3D.get_skin_reference()<class_MeshInstance3D_method_get_skin_reference>] and [RenderingServer.instance_attach_skeleton()<class_RenderingServer_method_instance_attach_skeleton>].

Note that despite the similar naming, the skeleton RID used in the [RenderingServer<class_RenderingServer>] does not have a direct one-to-one correspondence to a [Skeleton3D<class_Skeleton3D>] node.

In particular, a [Skeleton3D<class_Skeleton3D>] node with no [MeshInstance3D<class_MeshInstance3D>] children may be unknown to the [RenderingServer<class_RenderingServer>].

On the other hand, a [Skeleton3D<class_Skeleton3D>] with multiple [MeshInstance3D<class_MeshInstance3D>] nodes which each have different [MeshInstance3D.skin<class_MeshInstance3D_property_skin>] objects may have multiple SkinReference instances (and hence, multiple skeleton [RID<class_RID>]\ s).


## Methods

> **TABLE**
> :widths: auto
>
> +-------------------------+----------------------------------------------------------------------------+
> | :ref:`RID<class_RID>`   | :ref:`get_skeleton<class_SkinReference_method_get_skeleton>`\ (\ ) |const| |
> +-------------------------+----------------------------------------------------------------------------+
> | :ref:`Skin<class_Skin>` | :ref:`get_skin<class_SkinReference_method_get_skin>`\ (\ ) |const|         |
> +-------------------------+----------------------------------------------------------------------------+
>

----


## Method Descriptions



[RID<class_RID>] **get_skeleton**\ (\ ) |const| [🔗<class_SkinReference_method_get_skeleton>]

Returns the [RID<class_RID>] owned by this SkinReference, as returned by [RenderingServer.skeleton_create()<class_RenderingServer_method_skeleton_create>].


----



[Skin<class_Skin>] **get_skin**\ (\ ) |const| [🔗<class_SkinReference_method_get_skin>]

Returns the [Skin<class_Skin>] connected to this SkinReference. In the case of [MeshInstance3D<class_MeshInstance3D>] with no [MeshInstance3D.skin<class_MeshInstance3D_property_skin>] assigned, this will reference an internal default [Skin<class_Skin>] owned by that [MeshInstance3D<class_MeshInstance3D>].

Note that a single [Skin<class_Skin>] may have more than one **SkinReference** in the case that it is shared by meshes across multiple [Skeleton3D<class_Skeleton3D>] nodes.

