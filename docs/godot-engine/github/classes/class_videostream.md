:github_url: hide



# VideoStream

**Inherits:** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

**Inherited By:** [VideoStreamTheora<class_VideoStreamTheora>]

Base resource for video streams.


## Description

Base resource type for all video streams. Classes that derive from **VideoStream** can all be used as resource types to play back videos in [VideoStreamPlayer<class_VideoStreamPlayer>].


## Tutorials

- [../tutorials/animation/playing_videos](Playing videos .md)

- [../tutorials/io/runtime_file_loading_and_saving](Runtime file loading and saving .md)


## Properties

> **TABLE**
> :widths: auto
>
> +-----------------------------+----------------------------------------------+--------+
> | :ref:`String<class_String>` | :ref:`file<class_VideoStream_property_file>` | ``""`` |
> +-----------------------------+----------------------------------------------+--------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
> | :ref:`VideoStreamPlayback<class_VideoStreamPlayback>` | :ref:`_instantiate_playback<class_VideoStream_private_method__instantiate_playback>`\ (\ ) |virtual| |required| |
> +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
>

----


## Property Descriptions



[String<class_String>] **file** = `""` [🔗<class_VideoStream_property_file>]


- |void| **set_file**\ (\ value\: [String<class_String>]\ )
- [String<class_String>] **get_file**\ (\ )

The video file path or URI that this **VideoStream** resource handles.

For [VideoStreamTheora<class_VideoStreamTheora>], this filename should be an Ogg Theora video file with the `.ogv` extension.


----


## Method Descriptions



[VideoStreamPlayback<class_VideoStreamPlayback>] **_instantiate_playback**\ (\ ) |virtual| |required| [🔗<class_VideoStream_private_method__instantiate_playback>]

Called when the video starts playing, to initialize and return a subclass of [VideoStreamPlayback<class_VideoStreamPlayback>].

