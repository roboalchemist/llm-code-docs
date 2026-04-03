:github_url: hide



# CCDIK3D

**Inherits:** [IterateIK3D<class_IterateIK3D>] **<** [ChainIK3D<class_ChainIK3D>] **<** [IKModifier3D<class_IKModifier3D>] **<** [SkeletonModifier3D<class_SkeletonModifier3D>] **<** [Node3D<class_Node3D>] **<** [Node<class_Node>] **<** [Object<class_Object>]

Rotation based cyclic coordinate descent inverse kinematics solver.


## Description

**CCDIK3D** is rotation based IK, enabling fast and effective tracking even with large joint rotations. It's especially suitable for chains with limitations, providing smoother and more stable target tracking compared to [FABRIK3D<class_FABRIK3D>].

The resulting twist around the forward vector will always be kept from the previous pose.

\ **Note:** When the target is close to the root, it can cause unnatural movement, including joint flips and oscillations.

