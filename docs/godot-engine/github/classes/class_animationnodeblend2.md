:github_url: hide



# AnimationNodeBlend2

**Inherits:** [AnimationNodeSync<class_AnimationNodeSync>] **<** [AnimationNode<class_AnimationNode>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Blends two animations linearly inside of an [AnimationNodeBlendTree<class_AnimationNodeBlendTree>].


## Description

A resource to add to an [AnimationNodeBlendTree<class_AnimationNodeBlendTree>]. Blends two animations linearly based on the amount value.

In general, the blend value should be in the `[0.0, 1.0]` range. Values outside of this range can blend amplified or inverted animations, however, [AnimationNodeAdd2<class_AnimationNodeAdd2>] works better for this purpose.


## Tutorials

- [../tutorials/animation/animation_tree](Using AnimationTree .md)

- [3D Platformer Demo ](https://godotengine.org/asset-library/asset/2748)_

- [Third Person Shooter (TPS) Demo ](https://godotengine.org/asset-library/asset/2710)_

