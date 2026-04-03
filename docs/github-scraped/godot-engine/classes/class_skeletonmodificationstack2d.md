:github_url: hide



# SkeletonModificationStack2D

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

A resource that holds a stack of [SkeletonModification2D<class_SkeletonModification2D>]\ s.


## Description

This resource is used by the Skeleton and holds a stack of [SkeletonModification2D<class_SkeletonModification2D>]\ s.

This controls the order of the modifications and how they are applied. Modification order is especially important for full-body IK setups, as you need to execute the modifications in the correct order to get the desired results. For example, you want to execute a modification on the spine *before* the arms on a humanoid skeleton.

This resource also controls how strongly all of the modifications are applied to the [Skeleton2D<class_Skeleton2D>].


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------+------------------------------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>`   | :ref:`enabled<class_SkeletonModificationStack2D_property_enabled>`                       | ``false`` |
> +---------------------------+------------------------------------------------------------------------------------------+-----------+
> | :ref:`int<class_int>`     | :ref:`modification_count<class_SkeletonModificationStack2D_property_modification_count>` | ``0``     |
> +---------------------------+------------------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>` | :ref:`strength<class_SkeletonModificationStack2D_property_strength>`                     | ``1.0``   |
> +---------------------------+------------------------------------------------------------------------------------------+-----------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +-------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                      | :ref:`add_modification<class_SkeletonModificationStack2D_method_add_modification>`\ (\ modification\: :ref:`SkeletonModification2D<class_SkeletonModification2D>`\ )                                  |
> +-------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                      | :ref:`delete_modification<class_SkeletonModificationStack2D_method_delete_modification>`\ (\ mod_idx\: :ref:`int<class_int>`\ )                                                                       |
> +-------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                      | :ref:`enable_all_modifications<class_SkeletonModificationStack2D_method_enable_all_modifications>`\ (\ enabled\: :ref:`bool<class_bool>`\ )                                                           |
> +-------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                      | :ref:`execute<class_SkeletonModificationStack2D_method_execute>`\ (\ delta\: :ref:`float<class_float>`, execution_mode\: :ref:`int<class_int>`\ )                                                     |
> +-------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                     | :ref:`get_is_setup<class_SkeletonModificationStack2D_method_get_is_setup>`\ (\ ) |const|                                                                                                              |
> +-------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`SkeletonModification2D<class_SkeletonModification2D>` | :ref:`get_modification<class_SkeletonModificationStack2D_method_get_modification>`\ (\ mod_idx\: :ref:`int<class_int>`\ ) |const|                                                                     |
> +-------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Skeleton2D<class_Skeleton2D>`                         | :ref:`get_skeleton<class_SkeletonModificationStack2D_method_get_skeleton>`\ (\ ) |const|                                                                                                              |
> +-------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                      | :ref:`set_modification<class_SkeletonModificationStack2D_method_set_modification>`\ (\ mod_idx\: :ref:`int<class_int>`, modification\: :ref:`SkeletonModification2D<class_SkeletonModification2D>`\ ) |
> +-------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                      | :ref:`setup<class_SkeletonModificationStack2D_method_setup>`\ (\ )                                                                                                                                    |
> +-------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Property Descriptions



[bool<class_bool>] **enabled** = `false` [🔗<class_SkeletonModificationStack2D_property_enabled>]


- |void| **set_enabled**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_enabled**\ (\ )

If `true`, the modification's in the stack will be called. This is handled automatically through the [Skeleton2D<class_Skeleton2D>] node.


----



[int<class_int>] **modification_count** = `0` [🔗<class_SkeletonModificationStack2D_property_modification_count>]


- |void| **set_modification_count**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_modification_count**\ (\ )

The number of modifications in the stack.


----



[float<class_float>] **strength** = `1.0` [🔗<class_SkeletonModificationStack2D_property_strength>]


- |void| **set_strength**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_strength**\ (\ )

The interpolation strength of the modifications in stack. A value of `0` will make it where the modifications are not applied, a strength of `0.5` will be half applied, and a strength of `1` will allow the modifications to be fully applied and override the [Skeleton2D<class_Skeleton2D>] [Bone2D<class_Bone2D>] poses.


----


## Method Descriptions



|void| **add_modification**\ (\ modification\: [SkeletonModification2D<class_SkeletonModification2D>]\ ) [🔗<class_SkeletonModificationStack2D_method_add_modification>]

Adds the passed-in [SkeletonModification2D<class_SkeletonModification2D>] to the stack.


----



|void| **delete_modification**\ (\ mod_idx\: [int<class_int>]\ ) [🔗<class_SkeletonModificationStack2D_method_delete_modification>]

Deletes the [SkeletonModification2D<class_SkeletonModification2D>] at the index position `mod_idx`, if it exists.


----



|void| **enable_all_modifications**\ (\ enabled\: [bool<class_bool>]\ ) [🔗<class_SkeletonModificationStack2D_method_enable_all_modifications>]

Enables all [SkeletonModification2D<class_SkeletonModification2D>]\ s in the stack.


----



|void| **execute**\ (\ delta\: [float<class_float>], execution_mode\: [int<class_int>]\ ) [🔗<class_SkeletonModificationStack2D_method_execute>]

Executes all of the [SkeletonModification2D<class_SkeletonModification2D>]\ s in the stack that use the same execution mode as the passed-in `execution_mode`, starting from index `0` to [modification_count<class_SkeletonModificationStack2D_property_modification_count>].

\ **Note:** The order of the modifications can matter depending on the modifications. For example, modifications on a spine should operate before modifications on the arms in order to get proper results.


----



[bool<class_bool>] **get_is_setup**\ (\ ) |const| [🔗<class_SkeletonModificationStack2D_method_get_is_setup>]

Returns a boolean that indicates whether the modification stack is setup and can execute.


----



[SkeletonModification2D<class_SkeletonModification2D>] **get_modification**\ (\ mod_idx\: [int<class_int>]\ ) |const| [🔗<class_SkeletonModificationStack2D_method_get_modification>]

Returns the [SkeletonModification2D<class_SkeletonModification2D>] at the passed-in index, `mod_idx`.


----



[Skeleton2D<class_Skeleton2D>] **get_skeleton**\ (\ ) |const| [🔗<class_SkeletonModificationStack2D_method_get_skeleton>]

Returns the [Skeleton2D<class_Skeleton2D>] node that the SkeletonModificationStack2D is bound to.


----



|void| **set_modification**\ (\ mod_idx\: [int<class_int>], modification\: [SkeletonModification2D<class_SkeletonModification2D>]\ ) [🔗<class_SkeletonModificationStack2D_method_set_modification>]

Sets the modification at `mod_idx` to the passed-in modification, `modification`.


----



|void| **setup**\ (\ ) [🔗<class_SkeletonModificationStack2D_method_setup>]

Sets up the modification stack so it can execute. This function should be called by [Skeleton2D<class_Skeleton2D>] and shouldn't be manually called unless you know what you are doing.

