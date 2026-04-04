:github_url: hide



# VisibleOnScreenNotifier3D

**Inherits:** [VisualInstance3D<class_VisualInstance3D>] **<** [Node3D<class_Node3D>] **<** [Node<class_Node>] **<** [Object<class_Object>]

**Inherited By:** [VisibleOnScreenEnabler3D<class_VisibleOnScreenEnabler3D>]

A box-shaped region of 3D space that detects whether it is visible on screen.


## Description

**VisibleOnScreenNotifier3D** represents a box-shaped region of 3D space. When any part of this region becomes visible on screen or in a [Camera3D<class_Camera3D>]'s view, it will emit a [screen_entered<class_VisibleOnScreenNotifier3D_signal_screen_entered>] signal, and likewise it will emit a [screen_exited<class_VisibleOnScreenNotifier3D_signal_screen_exited>] signal when no part of it remains visible.

If you want a node to be enabled automatically when this region is visible on screen, use [VisibleOnScreenEnabler3D<class_VisibleOnScreenEnabler3D>].

\ **Note:** **VisibleOnScreenNotifier3D** uses an approximate heuristic that doesn't take walls and other occlusion into account, unless occlusion culling is used. It also won't function unless [Node3D.visible<class_Node3D_property_visible>] is set to `true`.


## Properties

> **TABLE**
> :widths: auto
>
> +-------------------------+------------------------------------------------------------+-------------------------------+
> | :ref:`AABB<class_AABB>` | :ref:`aabb<class_VisibleOnScreenNotifier3D_property_aabb>` | ``AABB(-1, -1, -1, 2, 2, 2)`` |
> +-------------------------+------------------------------------------------------------+-------------------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +-------------------------+----------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>` | :ref:`is_on_screen<class_VisibleOnScreenNotifier3D_method_is_on_screen>`\ (\ ) |const| |
> +-------------------------+----------------------------------------------------------------------------------------+
>

----


## Signals



**screen_entered**\ (\ ) [🔗<class_VisibleOnScreenNotifier3D_signal_screen_entered>]

Emitted when the **VisibleOnScreenNotifier3D** enters the screen.


----



**screen_exited**\ (\ ) [🔗<class_VisibleOnScreenNotifier3D_signal_screen_exited>]

Emitted when the **VisibleOnScreenNotifier3D** exits the screen.


----


## Property Descriptions



[AABB<class_AABB>] **aabb** = `AABB(-1, -1, -1, 2, 2, 2)` [🔗<class_VisibleOnScreenNotifier3D_property_aabb>]


- |void| **set_aabb**\ (\ value\: [AABB<class_AABB>]\ )
- [AABB<class_AABB>] **get_aabb**\ (\ )

The **VisibleOnScreenNotifier3D**'s bounding box.


----


## Method Descriptions



[bool<class_bool>] **is_on_screen**\ (\ ) |const| [🔗<class_VisibleOnScreenNotifier3D_method_is_on_screen>]

Returns `true` if the bounding box is on the screen.

\ **Note:** It takes one frame for the **VisibleOnScreenNotifier3D**'s visibility to be assessed once added to the scene tree, so this method will always return `false` right after it is instantiated.

