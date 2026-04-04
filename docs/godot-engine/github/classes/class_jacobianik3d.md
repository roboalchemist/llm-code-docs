:github_url: hide



# JacobianIK3D

**Inherits:** [IterateIK3D<class_IterateIK3D>] **<** [ChainIK3D<class_ChainIK3D>] **<** [IKModifier3D<class_IKModifier3D>] **<** [SkeletonModifier3D<class_SkeletonModifier3D>] **<** [Node3D<class_Node3D>] **<** [Node<class_Node>] **<** [Object<class_Object>]

Jacobian transpose based inverse kinematics solver.


## Description

**JacobianIK3D** calculates rotations for all joints simultaneously, producing natural and smooth movement. It is particularly suited for biological animations.

The resulting twist around the forward vector will always be kept from the previous pose.

\ **Note:** It converges more slowly than other IK solvers, leading to gentler and less immediate tracking of targets.

