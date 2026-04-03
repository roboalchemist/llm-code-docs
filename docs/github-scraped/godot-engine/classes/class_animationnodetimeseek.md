:github_url: hide



# AnimationNodeTimeSeek

**Inherits:** [AnimationNode<class_AnimationNode>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

A time-seeking animation node used in [AnimationTree<class_AnimationTree>].


## Description

This animation node can be used to cause a seek command to happen to any sub-children of the animation graph. Use to play an [Animation<class_Animation>] from the start or a certain playback position inside the [AnimationNodeBlendTree<class_AnimationNodeBlendTree>].

After setting the time and changing the animation playback, the time seek node automatically goes into sleep mode on the next process frame by setting its `seek_request` value to `-1.0`.


> **TABS**
>

    # Play child animation from the start.
    animation_tree.set("parameters/TimeSeek/seek_request", 0.0)
    # Alternative syntax (same result as above).
    animation_tree["parameters/TimeSeek/seek_request"] = 0.0

    # Play child animation from 12 second timestamp.
    animation_tree.set("parameters/TimeSeek/seek_request", 12.0)
    # Alternative syntax (same result as above).
    animation_tree["parameters/TimeSeek/seek_request"] = 12.0


    // Play child animation from the start.
    animationTree.Set("parameters/TimeSeek/seek_request", 0.0);

    // Play child animation from 12 second timestamp.
    animationTree.Set("parameters/TimeSeek/seek_request", 12.0);




## Tutorials

- [../tutorials/animation/animation_tree](Using AnimationTree .md)


## Properties

> **TABLE**
> :widths: auto
>
> +-------------------------+------------------------------------------------------------------------------+----------+
> | :ref:`bool<class_bool>` | :ref:`explicit_elapse<class_AnimationNodeTimeSeek_property_explicit_elapse>` | ``true`` |
> +-------------------------+------------------------------------------------------------------------------+----------+
>

----


## Property Descriptions



[bool<class_bool>] **explicit_elapse** = `true` [🔗<class_AnimationNodeTimeSeek_property_explicit_elapse>]


- |void| **set_explicit_elapse**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_explicit_elapse**\ (\ )

If `true`, some processes are executed to handle keys between seeks, such as calculating root motion and finding the nearest discrete key.

