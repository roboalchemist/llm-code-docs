:github_url: hide



# SkeletonProfileHumanoid

**Inherits:** [SkeletonProfile<class_SkeletonProfile>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

A humanoid [SkeletonProfile<class_SkeletonProfile>] preset.


## Description

A [SkeletonProfile<class_SkeletonProfile>] as a preset that is optimized for the human form. This exists for standardization, so all parameters are read-only.

A humanoid skeleton profile contains 56 bones divided into 4 groups: `"Body"`, `"Face"`, `"LeftHand"`, and `"RightHand"`. It is structured as follows:

> **CODE**
>
> Root
> └─ Hips
> ├─ LeftUpperLeg
> │  └─ LeftLowerLeg
> │     └─ LeftFoot
> │        └─ LeftToes
> ├─ RightUpperLeg
> │  └─ RightLowerLeg
> │     └─ RightFoot
> │        └─ RightToes
> └─ Spine
> └─ Chest
> └─ UpperChest
> ├─ Neck
> │   └─ Head
> │       ├─ Jaw
> │       ├─ LeftEye
> │       └─ RightEye
> ├─ LeftShoulder
> │  └─ LeftUpperArm
> │     └─ LeftLowerArm
> │        └─ LeftHand
> │           ├─ LeftThumbMetacarpal
> │           │  └─ LeftThumbProximal
> │           │    └─ LeftThumbDistal
> │           ├─ LeftIndexProximal
> │           │  └─ LeftIndexIntermediate
> │           │    └─ LeftIndexDistal
> │           ├─ LeftMiddleProximal
> │           │  └─ LeftMiddleIntermediate
> │           │    └─ LeftMiddleDistal
> │           ├─ LeftRingProximal
> │           │  └─ LeftRingIntermediate
> │           │    └─ LeftRingDistal
> │           └─ LeftLittleProximal
> │              └─ LeftLittleIntermediate
> │                └─ LeftLittleDistal
> └─ RightShoulder
> └─ RightUpperArm
> └─ RightLowerArm
> └─ RightHand
> ├─ RightThumbMetacarpal
> │  └─ RightThumbProximal
> │     └─ RightThumbDistal
> ├─ RightIndexProximal
> │  └─ RightIndexIntermediate
> │     └─ RightIndexDistal
> ├─ RightMiddleProximal
> │  └─ RightMiddleIntermediate
> │     └─ RightMiddleDistal
> ├─ RightRingProximal
> │  └─ RightRingIntermediate
> │     └─ RightRingDistal
> └─ RightLittleProximal
> └─ RightLittleIntermediate
> └─ RightLittleDistal
>

## Tutorials

- [../tutorials/assets_pipeline/retargeting_3d_skeletons](Retargeting 3D Skeletons .md)


## Properties

> **TABLE**
> :widths: auto
>
> +-------------------------------------+-----------------+------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`               | bone_size       | ``56`` (overrides :ref:`SkeletonProfile<class_SkeletonProfile_property_bone_size>`)            |
> +-------------------------------------+-----------------+------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`               | group_size      | ``4`` (overrides :ref:`SkeletonProfile<class_SkeletonProfile_property_group_size>`)            |
> +-------------------------------------+-----------------+------------------------------------------------------------------------------------------------+
> | :ref:`StringName<class_StringName>` | root_bone       | ``&"Root"`` (overrides :ref:`SkeletonProfile<class_SkeletonProfile_property_root_bone>`)       |
> +-------------------------------------+-----------------+------------------------------------------------------------------------------------------------+
> | :ref:`StringName<class_StringName>` | scale_base_bone | ``&"Hips"`` (overrides :ref:`SkeletonProfile<class_SkeletonProfile_property_scale_base_bone>`) |
> +-------------------------------------+-----------------+------------------------------------------------------------------------------------------------+
>
