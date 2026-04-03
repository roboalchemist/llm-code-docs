:github_url: hide



# PhysicalBoneSimulator3D

**Inherits:** [SkeletonModifier3D<class_SkeletonModifier3D>] **<** [Node3D<class_Node3D>] **<** [Node<class_Node>] **<** [Object<class_Object>]

Node that can be the parent of [PhysicalBone3D<class_PhysicalBone3D>] and can apply the simulation results to [Skeleton3D<class_Skeleton3D>].


## Description

Node that can be the parent of [PhysicalBone3D<class_PhysicalBone3D>] and can apply the simulation results to [Skeleton3D<class_Skeleton3D>].


## Methods

> **TABLE**
> :widths: auto
>
> +-------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>` | :ref:`is_simulating_physics<class_PhysicalBoneSimulator3D_method_is_simulating_physics>`\ (\ ) |const|                                                                                            |
> +-------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                  | :ref:`physical_bones_add_collision_exception<class_PhysicalBoneSimulator3D_method_physical_bones_add_collision_exception>`\ (\ exception\: :ref:`RID<class_RID>`\ )                               |
> +-------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                  | :ref:`physical_bones_remove_collision_exception<class_PhysicalBoneSimulator3D_method_physical_bones_remove_collision_exception>`\ (\ exception\: :ref:`RID<class_RID>`\ )                         |
> +-------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                  | :ref:`physical_bones_start_simulation<class_PhysicalBoneSimulator3D_method_physical_bones_start_simulation>`\ (\ bones\: :ref:`Array<class_Array>`\[:ref:`StringName<class_StringName>`\] = []\ ) |
> +-------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                  | :ref:`physical_bones_stop_simulation<class_PhysicalBoneSimulator3D_method_physical_bones_stop_simulation>`\ (\ )                                                                                  |
> +-------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Method Descriptions



[bool<class_bool>] **is_simulating_physics**\ (\ ) |const| [🔗<class_PhysicalBoneSimulator3D_method_is_simulating_physics>]

Returns a boolean that indicates whether the **PhysicalBoneSimulator3D** is running and simulating.


----



|void| **physical_bones_add_collision_exception**\ (\ exception\: [RID<class_RID>]\ ) [🔗<class_PhysicalBoneSimulator3D_method_physical_bones_add_collision_exception>]

Adds a collision exception to the physical bone.

Works just like the [RigidBody3D<class_RigidBody3D>] node.


----



|void| **physical_bones_remove_collision_exception**\ (\ exception\: [RID<class_RID>]\ ) [🔗<class_PhysicalBoneSimulator3D_method_physical_bones_remove_collision_exception>]

Removes a collision exception to the physical bone.

Works just like the [RigidBody3D<class_RigidBody3D>] node.


----



|void| **physical_bones_start_simulation**\ (\ bones\: [Array<class_Array>]\[[StringName<class_StringName>]\] = []\ ) [🔗<class_PhysicalBoneSimulator3D_method_physical_bones_start_simulation>]

Tells the [PhysicalBone3D<class_PhysicalBone3D>] nodes in the Skeleton to start simulating and reacting to the physics world.

Optionally, a list of bone names can be passed-in, allowing only the passed-in bones to be simulated.


----



|void| **physical_bones_stop_simulation**\ (\ ) [🔗<class_PhysicalBoneSimulator3D_method_physical_bones_stop_simulation>]

Tells the [PhysicalBone3D<class_PhysicalBone3D>] nodes in the Skeleton to stop simulating.

