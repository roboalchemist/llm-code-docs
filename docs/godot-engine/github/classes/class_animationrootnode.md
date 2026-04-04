:github_url: hide



# AnimationRootNode

**Inherits:** [AnimationNode<class_AnimationNode>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

**Inherited By:** [AnimationNodeAnimation<class_AnimationNodeAnimation>], [AnimationNodeBlendSpace1D<class_AnimationNodeBlendSpace1D>], [AnimationNodeBlendSpace2D<class_AnimationNodeBlendSpace2D>], [AnimationNodeBlendTree<class_AnimationNodeBlendTree>], [AnimationNodeStateMachine<class_AnimationNodeStateMachine>]

Base class for [AnimationNode<class_AnimationNode>]\ s that hold one or multiple composite animations. Usually used for [AnimationTree.tree_root<class_AnimationTree_property_tree_root>].


## Description

**AnimationRootNode** is a base class for [AnimationNode<class_AnimationNode>]\ s that hold a complete animation. A complete animation refers to the output of an [AnimationNodeOutput<class_AnimationNodeOutput>] in an [AnimationNodeBlendTree<class_AnimationNodeBlendTree>] or the output of another **AnimationRootNode**. Used for [AnimationTree.tree_root<class_AnimationTree_property_tree_root>] or in other **AnimationRootNode**\ s.

Examples of built-in root nodes include [AnimationNodeBlendTree<class_AnimationNodeBlendTree>] (allows blending nodes between each other using various modes), [AnimationNodeStateMachine<class_AnimationNodeStateMachine>] (allows to configure blending and transitions between nodes using a state machine pattern), [AnimationNodeBlendSpace2D<class_AnimationNodeBlendSpace2D>] (allows linear blending between **three** [AnimationNode<class_AnimationNode>]\ s), [AnimationNodeBlendSpace1D<class_AnimationNodeBlendSpace1D>] (allows linear blending only between **two** [AnimationNode<class_AnimationNode>]\ s).


## Tutorials

- [../tutorials/animation/animation_tree](Using AnimationTree .md)

