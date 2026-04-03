# AnimationNodeBlend3 in English

# AnimationNodeBlend3

Inherits:AnimationNodeSync<AnimationNode<Resource<RefCounted<Object
Blends two of three animations linearly inside of anAnimationNodeBlendTree.

## Description

A resource to add to anAnimationNodeBlendTree. Blends two animations out of three linearly out of three based on the amount value.
This animation node has three inputs:

- The base animation to blend with
The base animation to blend with
- A "-blend" animation to blend with when the blend amount is negative value
A "-blend" animation to blend with when the blend amount is negative value
- A "+blend" animation to blend with when the blend amount is positive value
A "+blend" animation to blend with when the blend amount is positive value
In general, the blend value should be in the[-1.0,1.0]range. Values outside of this range can blend amplified animations, however,AnimationNodeAdd3works better for this purpose.

## Tutorials

- Using AnimationTree
Using AnimationTree

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
