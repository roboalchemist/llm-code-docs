:github_url: hide



# AudioStreamPlaybackInteractive

**Inherits:** [AudioStreamPlayback<class_AudioStreamPlayback>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Playback component of [AudioStreamInteractive<class_AudioStreamInteractive>].


## Description

Playback component of [AudioStreamInteractive<class_AudioStreamInteractive>]. Contains functions to change the currently played clip.


## Methods

> **TABLE**
> :widths: auto
>
> +-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>` | :ref:`get_current_clip_index<class_AudioStreamPlaybackInteractive_method_get_current_clip_index>`\ (\ ) |const|                                          |
> +-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                | :ref:`switch_to_clip<class_AudioStreamPlaybackInteractive_method_switch_to_clip>`\ (\ clip_index\: :ref:`int<class_int>`\ )                              |
> +-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                | :ref:`switch_to_clip_by_name<class_AudioStreamPlaybackInteractive_method_switch_to_clip_by_name>`\ (\ clip_name\: :ref:`StringName<class_StringName>`\ ) |
> +-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Method Descriptions



[int<class_int>] **get_current_clip_index**\ (\ ) |const| [🔗<class_AudioStreamPlaybackInteractive_method_get_current_clip_index>]

Return the index of the currently playing clip. You can use this to get the name of the currently playing clip with [AudioStreamInteractive.get_clip_name()<class_AudioStreamInteractive_method_get_clip_name>].

\ **Example:** Get the currently playing clip name from inside an [AudioStreamPlayer<class_AudioStreamPlayer>] node.


> **TABS**
>

    var playing_clip_name = stream.get_clip_name(get_stream_playback().get_current_clip_index())




----



|void| **switch_to_clip**\ (\ clip_index\: [int<class_int>]\ ) [🔗<class_AudioStreamPlaybackInteractive_method_switch_to_clip>]

Switch to a clip (by index).


----



|void| **switch_to_clip_by_name**\ (\ clip_name\: [StringName<class_StringName>]\ ) [🔗<class_AudioStreamPlaybackInteractive_method_switch_to_clip_by_name>]

Switch to a clip (by name).

