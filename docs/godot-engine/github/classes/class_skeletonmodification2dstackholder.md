:github_url: hide



# SkeletonModification2DStackHolder

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [SkeletonModification2D<class_SkeletonModification2D>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

A modification that holds and executes a [SkeletonModificationStack2D<class_SkeletonModificationStack2D>].


## Description

This [SkeletonModification2D<class_SkeletonModification2D>] holds a reference to a [SkeletonModificationStack2D<class_SkeletonModificationStack2D>], allowing you to use multiple modification stacks on a single [Skeleton2D<class_Skeleton2D>].

\ **Note:** The modifications in the held [SkeletonModificationStack2D<class_SkeletonModificationStack2D>] will only be executed if their execution mode matches the execution mode of the SkeletonModification2DStackHolder.


## Methods

> **TABLE**
> :widths: auto
>
> +-----------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`SkeletonModificationStack2D<class_SkeletonModificationStack2D>` | :ref:`get_held_modification_stack<class_SkeletonModification2DStackHolder_method_get_held_modification_stack>`\ (\ ) |const|                                                                                          |
> +-----------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                | :ref:`set_held_modification_stack<class_SkeletonModification2DStackHolder_method_set_held_modification_stack>`\ (\ held_modification_stack\: :ref:`SkeletonModificationStack2D<class_SkeletonModificationStack2D>`\ ) |
> +-----------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Method Descriptions



[SkeletonModificationStack2D<class_SkeletonModificationStack2D>] **get_held_modification_stack**\ (\ ) |const| [🔗<class_SkeletonModification2DStackHolder_method_get_held_modification_stack>]

Returns the [SkeletonModificationStack2D<class_SkeletonModificationStack2D>] that this modification is holding.


----



|void| **set_held_modification_stack**\ (\ held_modification_stack\: [SkeletonModificationStack2D<class_SkeletonModificationStack2D>]\ ) [🔗<class_SkeletonModification2DStackHolder_method_set_held_modification_stack>]

Sets the [SkeletonModificationStack2D<class_SkeletonModificationStack2D>] that this modification is holding. This modification stack will then be executed when this modification is executed.

