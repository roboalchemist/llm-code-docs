:github_url: hide



# AnimationNodeSub2

**Inherits:** [AnimationNodeSync<class_AnimationNodeSync>] **<** [AnimationNode<class_AnimationNode>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Blends two animations subtractively inside of an [AnimationNodeBlendTree<class_AnimationNodeBlendTree>].


## Description

A resource to add to an [AnimationNodeBlendTree<class_AnimationNodeBlendTree>]. Blends two animations subtractively based on the amount value.

This animation node is usually used for pre-calculation to cancel out any extra poses from the animation for the "add" animation source in [AnimationNodeAdd2<class_AnimationNodeAdd2>] or [AnimationNodeAdd3<class_AnimationNodeAdd3>].

In general, the blend value should be in the `[0.0, 1.0]` range, but values outside of this range can be used for amplified or inverted animations.

\ **Note:** This calculation is different from using a negative value in [AnimationNodeAdd2<class_AnimationNodeAdd2>], since the transformation matrices do not satisfy the commutative law. **AnimationNodeSub2** multiplies the transformation matrix of the inverted animation from the left side, while negative [AnimationNodeAdd2<class_AnimationNodeAdd2>] multiplies it from the right side.


## Tutorials

- [../tutorials/animation/animation_tree](AnimationTree .md)

