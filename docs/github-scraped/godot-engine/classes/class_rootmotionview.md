:github_url: hide



# RootMotionView

**Inherits:** [VisualInstance3D<class_VisualInstance3D>] **<** [Node3D<class_Node3D>] **<** [Node<class_Node>] **<** [Object<class_Object>]

Editor-only helper for setting up root motion in [AnimationMixer<class_AnimationMixer>].


## Description

*Root motion* refers to an animation technique where a mesh's skeleton is used to give impulse to a character. When working with 3D animations, a popular technique is for animators to use the root skeleton bone to give motion to the rest of the skeleton. This allows animating characters in a way where steps actually match the floor below. It also allows precise interaction with objects during cinematics. See also [AnimationMixer<class_AnimationMixer>].

\ **Note:** **RootMotionView** is only visible in the editor. It will be hidden automatically in the running project.


## Tutorials

- [Using AnimationTree - Root motion ](../tutorials/animation/animation_tree.html#root-motion)_


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------------+---------------------------------------------------------------------+---------------------------+
> | :ref:`NodePath<class_NodePath>` | :ref:`animation_path<class_RootMotionView_property_animation_path>` | ``NodePath("")``          |
> +---------------------------------+---------------------------------------------------------------------+---------------------------+
> | :ref:`float<class_float>`       | :ref:`cell_size<class_RootMotionView_property_cell_size>`           | ``1.0``                   |
> +---------------------------------+---------------------------------------------------------------------+---------------------------+
> | :ref:`Color<class_Color>`       | :ref:`color<class_RootMotionView_property_color>`                   | ``Color(0.5, 0.5, 1, 1)`` |
> +---------------------------------+---------------------------------------------------------------------+---------------------------+
> | :ref:`float<class_float>`       | :ref:`radius<class_RootMotionView_property_radius>`                 | ``10.0``                  |
> +---------------------------------+---------------------------------------------------------------------+---------------------------+
> | :ref:`bool<class_bool>`         | :ref:`zero_y<class_RootMotionView_property_zero_y>`                 | ``true``                  |
> +---------------------------------+---------------------------------------------------------------------+---------------------------+
>

----


## Property Descriptions



[NodePath<class_NodePath>] **animation_path** = `NodePath("")` [🔗<class_RootMotionView_property_animation_path>]


- |void| **set_animation_path**\ (\ value\: [NodePath<class_NodePath>]\ )
- [NodePath<class_NodePath>] **get_animation_path**\ (\ )

Path to an [AnimationMixer<class_AnimationMixer>] node to use as a basis for root motion.


----



[float<class_float>] **cell_size** = `1.0` [🔗<class_RootMotionView_property_cell_size>]


- |void| **set_cell_size**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_cell_size**\ (\ )

The grid's cell size in 3D units.


----



[Color<class_Color>] **color** = `Color(0.5, 0.5, 1, 1)` [🔗<class_RootMotionView_property_color>]


- |void| **set_color**\ (\ value\: [Color<class_Color>]\ )
- [Color<class_Color>] **get_color**\ (\ )

The grid's color.


----



[float<class_float>] **radius** = `10.0` [🔗<class_RootMotionView_property_radius>]


- |void| **set_radius**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_radius**\ (\ )

The grid's radius in 3D units. The grid's opacity will fade gradually as the distance from the origin increases until this [radius<class_RootMotionView_property_radius>] is reached.


----



[bool<class_bool>] **zero_y** = `true` [🔗<class_RootMotionView_property_zero_y>]


- |void| **set_zero_y**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_zero_y**\ (\ )

If `true`, the grid's points will all be on the same Y coordinate (*local* Y = 0). If `false`, the points' original Y coordinate is preserved.

