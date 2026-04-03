:github_url: hide



# SkeletonModification2D

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

**Inherited By:** [SkeletonModification2DCCDIK<class_SkeletonModification2DCCDIK>], [SkeletonModification2DFABRIK<class_SkeletonModification2DFABRIK>], [SkeletonModification2DJiggle<class_SkeletonModification2DJiggle>], [SkeletonModification2DLookAt<class_SkeletonModification2DLookAt>], [SkeletonModification2DPhysicalBones<class_SkeletonModification2DPhysicalBones>], [SkeletonModification2DStackHolder<class_SkeletonModification2DStackHolder>], [SkeletonModification2DTwoBoneIK<class_SkeletonModification2DTwoBoneIK>]

Base class for resources that operate on [Bone2D<class_Bone2D>]\ s in a [Skeleton2D<class_Skeleton2D>].


## Description

This resource provides an interface that can be expanded so code that operates on [Bone2D<class_Bone2D>] nodes in a [Skeleton2D<class_Skeleton2D>] can be mixed and matched together to create complex interactions.

This is used to provide Godot with a flexible and powerful Inverse Kinematics solution that can be adapted for many different uses.


## Properties

> **TABLE**
> :widths: auto
>
> +-------------------------+-----------------------------------------------------------------------------+----------+
> | :ref:`bool<class_bool>` | :ref:`enabled<class_SkeletonModification2D_property_enabled>`               | ``true`` |
> +-------------------------+-----------------------------------------------------------------------------+----------+
> | :ref:`int<class_int>`   | :ref:`execution_mode<class_SkeletonModification2D_property_execution_mode>` | ``0``    |
> +-------------------------+-----------------------------------------------------------------------------+----------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +-----------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                | :ref:`_draw_editor_gizmo<class_SkeletonModification2D_private_method__draw_editor_gizmo>`\ (\ ) |virtual|                                                                                                        |
> +-----------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                | :ref:`_execute<class_SkeletonModification2D_private_method__execute>`\ (\ delta\: :ref:`float<class_float>`\ ) |virtual|                                                                                         |
> +-----------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                | :ref:`_setup_modification<class_SkeletonModification2D_private_method__setup_modification>`\ (\ modification_stack\: :ref:`SkeletonModificationStack2D<class_SkeletonModificationStack2D>`\ ) |virtual|          |
> +-----------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`                                             | :ref:`clamp_angle<class_SkeletonModification2D_method_clamp_angle>`\ (\ angle\: :ref:`float<class_float>`, min\: :ref:`float<class_float>`, max\: :ref:`float<class_float>`, invert\: :ref:`bool<class_bool>`\ ) |
> +-----------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                               | :ref:`get_editor_draw_gizmo<class_SkeletonModification2D_method_get_editor_draw_gizmo>`\ (\ ) |const|                                                                                                            |
> +-----------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                               | :ref:`get_is_setup<class_SkeletonModification2D_method_get_is_setup>`\ (\ ) |const|                                                                                                                              |
> +-----------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`SkeletonModificationStack2D<class_SkeletonModificationStack2D>` | :ref:`get_modification_stack<class_SkeletonModification2D_method_get_modification_stack>`\ (\ )                                                                                                                  |
> +-----------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                | :ref:`set_editor_draw_gizmo<class_SkeletonModification2D_method_set_editor_draw_gizmo>`\ (\ draw_gizmo\: :ref:`bool<class_bool>`\ )                                                                              |
> +-----------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                | :ref:`set_is_setup<class_SkeletonModification2D_method_set_is_setup>`\ (\ is_setup\: :ref:`bool<class_bool>`\ )                                                                                                  |
> +-----------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Property Descriptions



[bool<class_bool>] **enabled** = `true` [🔗<class_SkeletonModification2D_property_enabled>]


- |void| **set_enabled**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_enabled**\ (\ )

If `true`, the modification's [_execute()<class_SkeletonModification2D_private_method__execute>] function will be called by the [SkeletonModificationStack2D<class_SkeletonModificationStack2D>].


----



[int<class_int>] **execution_mode** = `0` [🔗<class_SkeletonModification2D_property_execution_mode>]


- |void| **set_execution_mode**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_execution_mode**\ (\ )

The execution mode for the modification. This tells the modification stack when to execute the modification. Some modifications have settings that are only available in certain execution modes.


----


## Method Descriptions



|void| **_draw_editor_gizmo**\ (\ ) |virtual| [🔗<class_SkeletonModification2D_private_method__draw_editor_gizmo>]

Used for drawing **editor-only** modification gizmos. This function will only be called in the Godot editor and can be overridden to draw custom gizmos.

\ **Note:** You will need to use the Skeleton2D from [SkeletonModificationStack2D.get_skeleton()<class_SkeletonModificationStack2D_method_get_skeleton>] and it's draw functions, as the **SkeletonModification2D** resource cannot draw on its own.


----



|void| **_execute**\ (\ delta\: [float<class_float>]\ ) |virtual| [🔗<class_SkeletonModification2D_private_method__execute>]

Executes the given modification. This is where the modification performs whatever function it is designed to do.


----



|void| **_setup_modification**\ (\ modification_stack\: [SkeletonModificationStack2D<class_SkeletonModificationStack2D>]\ ) |virtual| [🔗<class_SkeletonModification2D_private_method__setup_modification>]

Called when the modification is setup. This is where the modification performs initialization.


----



[float<class_float>] **clamp_angle**\ (\ angle\: [float<class_float>], min\: [float<class_float>], max\: [float<class_float>], invert\: [bool<class_bool>]\ ) [🔗<class_SkeletonModification2D_method_clamp_angle>]

Takes an angle and clamps it so it is within the passed-in `min` and `max` range. `invert` will inversely clamp the angle, clamping it to the range outside of the given bounds.


----



[bool<class_bool>] **get_editor_draw_gizmo**\ (\ ) |const| [🔗<class_SkeletonModification2D_method_get_editor_draw_gizmo>]

Returns whether this modification will call [_draw_editor_gizmo()<class_SkeletonModification2D_private_method__draw_editor_gizmo>] in the Godot editor to draw modification-specific gizmos.


----



[bool<class_bool>] **get_is_setup**\ (\ ) |const| [🔗<class_SkeletonModification2D_method_get_is_setup>]

Returns whether this modification has been successfully setup or not.


----



[SkeletonModificationStack2D<class_SkeletonModificationStack2D>] **get_modification_stack**\ (\ ) [🔗<class_SkeletonModification2D_method_get_modification_stack>]

Returns the [SkeletonModificationStack2D<class_SkeletonModificationStack2D>] that this modification is bound to. Through the modification stack, you can access the Skeleton2D the modification is operating on.


----



|void| **set_editor_draw_gizmo**\ (\ draw_gizmo\: [bool<class_bool>]\ ) [🔗<class_SkeletonModification2D_method_set_editor_draw_gizmo>]

Sets whether this modification will call [_draw_editor_gizmo()<class_SkeletonModification2D_private_method__draw_editor_gizmo>] in the Godot editor to draw modification-specific gizmos.


----



|void| **set_is_setup**\ (\ is_setup\: [bool<class_bool>]\ ) [🔗<class_SkeletonModification2D_method_set_is_setup>]

Manually allows you to set the setup state of the modification. This function should only rarely be used, as the [SkeletonModificationStack2D<class_SkeletonModificationStack2D>] the modification is bound to should handle setting the modification up.

