:github_url: hide



# VideoStreamPlayer

**Inherits:** [Control<class_Control>] **<** [CanvasItem<class_CanvasItem>] **<** [Node<class_Node>] **<** [Object<class_Object>]

A control used for video playback.


## Description

A control used for playback of [VideoStream<class_VideoStream>] resources.

Supported video formats are [Ogg Theora ](https://www.theora.org/)_ (`.ogv`, [VideoStreamTheora<class_VideoStreamTheora>]) and any format exposed via a GDExtension plugin.

\ **Warning:** On Web, video playback *will* perform poorly due to missing architecture-specific assembly optimizations.


## Tutorials

- [../tutorials/animation/playing_videos](Playing videos .md)


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------------------+--------------------------------------------------------------------------+---------------+
> | :ref:`int<class_int>`                 | :ref:`audio_track<class_VideoStreamPlayer_property_audio_track>`         | ``0``         |
> +---------------------------------------+--------------------------------------------------------------------------+---------------+
> | :ref:`bool<class_bool>`               | :ref:`autoplay<class_VideoStreamPlayer_property_autoplay>`               | ``false``     |
> +---------------------------------------+--------------------------------------------------------------------------+---------------+
> | :ref:`int<class_int>`                 | :ref:`buffering_msec<class_VideoStreamPlayer_property_buffering_msec>`   | ``500``       |
> +---------------------------------------+--------------------------------------------------------------------------+---------------+
> | :ref:`StringName<class_StringName>`   | :ref:`bus<class_VideoStreamPlayer_property_bus>`                         | ``&"Master"`` |
> +---------------------------------------+--------------------------------------------------------------------------+---------------+
> | :ref:`bool<class_bool>`               | :ref:`expand<class_VideoStreamPlayer_property_expand>`                   | ``false``     |
> +---------------------------------------+--------------------------------------------------------------------------+---------------+
> | :ref:`bool<class_bool>`               | :ref:`loop<class_VideoStreamPlayer_property_loop>`                       | ``false``     |
> +---------------------------------------+--------------------------------------------------------------------------+---------------+
> | :ref:`bool<class_bool>`               | :ref:`paused<class_VideoStreamPlayer_property_paused>`                   | ``false``     |
> +---------------------------------------+--------------------------------------------------------------------------+---------------+
> | :ref:`float<class_float>`             | :ref:`speed_scale<class_VideoStreamPlayer_property_speed_scale>`         | ``1.0``       |
> +---------------------------------------+--------------------------------------------------------------------------+---------------+
> | :ref:`VideoStream<class_VideoStream>` | :ref:`stream<class_VideoStreamPlayer_property_stream>`                   |               |
> +---------------------------------------+--------------------------------------------------------------------------+---------------+
> | :ref:`float<class_float>`             | :ref:`stream_position<class_VideoStreamPlayer_property_stream_position>` |               |
> +---------------------------------------+--------------------------------------------------------------------------+---------------+
> | :ref:`float<class_float>`             | :ref:`volume<class_VideoStreamPlayer_property_volume>`                   |               |
> +---------------------------------------+--------------------------------------------------------------------------+---------------+
> | :ref:`float<class_float>`             | :ref:`volume_db<class_VideoStreamPlayer_property_volume_db>`             | ``0.0``       |
> +---------------------------------------+--------------------------------------------------------------------------+---------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +-----------------------------------+------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`         | :ref:`get_stream_length<class_VideoStreamPlayer_method_get_stream_length>`\ (\ ) |const| |
> +-----------------------------------+------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`       | :ref:`get_stream_name<class_VideoStreamPlayer_method_get_stream_name>`\ (\ ) |const|     |
> +-----------------------------------+------------------------------------------------------------------------------------------+
> | :ref:`Texture2D<class_Texture2D>` | :ref:`get_video_texture<class_VideoStreamPlayer_method_get_video_texture>`\ (\ ) |const| |
> +-----------------------------------+------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`           | :ref:`is_playing<class_VideoStreamPlayer_method_is_playing>`\ (\ ) |const|               |
> +-----------------------------------+------------------------------------------------------------------------------------------+
> | |void|                            | :ref:`play<class_VideoStreamPlayer_method_play>`\ (\ )                                   |
> +-----------------------------------+------------------------------------------------------------------------------------------+
> | |void|                            | :ref:`stop<class_VideoStreamPlayer_method_stop>`\ (\ )                                   |
> +-----------------------------------+------------------------------------------------------------------------------------------+
>

----


## Signals



**finished**\ (\ ) [🔗<class_VideoStreamPlayer_signal_finished>]

Emitted when playback is finished.


----


## Property Descriptions



[int<class_int>] **audio_track** = `0` [🔗<class_VideoStreamPlayer_property_audio_track>]


- |void| **set_audio_track**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_audio_track**\ (\ )

The embedded audio track to play.


----



[bool<class_bool>] **autoplay** = `false` [🔗<class_VideoStreamPlayer_property_autoplay>]


- |void| **set_autoplay**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **has_autoplay**\ (\ )

If `true`, playback starts when the scene loads.


----



[int<class_int>] **buffering_msec** = `500` [🔗<class_VideoStreamPlayer_property_buffering_msec>]


- |void| **set_buffering_msec**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_buffering_msec**\ (\ )

Amount of time in milliseconds to store in buffer while playing.


----



[StringName<class_StringName>] **bus** = `&"Master"` [🔗<class_VideoStreamPlayer_property_bus>]


- |void| **set_bus**\ (\ value\: [StringName<class_StringName>]\ )
- [StringName<class_StringName>] **get_bus**\ (\ )

Audio bus to use for sound playback.


----



[bool<class_bool>] **expand** = `false` [🔗<class_VideoStreamPlayer_property_expand>]


- |void| **set_expand**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **has_expand**\ (\ )

If `true`, the video scales to the control size. Otherwise, the control minimum size will be automatically adjusted to match the video stream's dimensions.


----



[bool<class_bool>] **loop** = `false` [🔗<class_VideoStreamPlayer_property_loop>]


- |void| **set_loop**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **has_loop**\ (\ )

If `true`, the video restarts when it reaches its end.


----



[bool<class_bool>] **paused** = `false` [🔗<class_VideoStreamPlayer_property_paused>]


- |void| **set_paused**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_paused**\ (\ )

If `true`, the video is paused.


----



[float<class_float>] **speed_scale** = `1.0` [🔗<class_VideoStreamPlayer_property_speed_scale>]


- |void| **set_speed_scale**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_speed_scale**\ (\ )

The stream's current speed scale. `1.0` is the normal speed, while `2.0` is double speed and `0.5` is half speed. A speed scale of `0.0` pauses the video, similar to setting [paused<class_VideoStreamPlayer_property_paused>] to `true`.


----



[VideoStream<class_VideoStream>] **stream** [🔗<class_VideoStreamPlayer_property_stream>]


- |void| **set_stream**\ (\ value\: [VideoStream<class_VideoStream>]\ )
- [VideoStream<class_VideoStream>] **get_stream**\ (\ )

The assigned video stream. See description for supported formats.


----



[float<class_float>] **stream_position** [🔗<class_VideoStreamPlayer_property_stream_position>]


- |void| **set_stream_position**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_stream_position**\ (\ )

The current position of the stream, in seconds.


----



[float<class_float>] **volume** [🔗<class_VideoStreamPlayer_property_volume>]


- |void| **set_volume**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_volume**\ (\ )

Audio volume as a linear value.


----



[float<class_float>] **volume_db** = `0.0` [🔗<class_VideoStreamPlayer_property_volume_db>]


- |void| **set_volume_db**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_volume_db**\ (\ )

Audio volume in dB.


----


## Method Descriptions



[float<class_float>] **get_stream_length**\ (\ ) |const| [🔗<class_VideoStreamPlayer_method_get_stream_length>]

The length of the current stream, in seconds.


----



[String<class_String>] **get_stream_name**\ (\ ) |const| [🔗<class_VideoStreamPlayer_method_get_stream_name>]

Returns the video stream's name, or `"<No Stream>"` if no video stream is assigned.


----



[Texture2D<class_Texture2D>] **get_video_texture**\ (\ ) |const| [🔗<class_VideoStreamPlayer_method_get_video_texture>]

Returns the current frame as a [Texture2D<class_Texture2D>].


----



[bool<class_bool>] **is_playing**\ (\ ) |const| [🔗<class_VideoStreamPlayer_method_is_playing>]

Returns `true` if the video is playing.

\ **Note:** The video is still considered playing if paused during playback.


----



|void| **play**\ (\ ) [🔗<class_VideoStreamPlayer_method_play>]

Starts the video playback from the beginning. If the video is paused, this will not unpause the video.


----



|void| **stop**\ (\ ) [🔗<class_VideoStreamPlayer_method_stop>]

Stops the video playback and sets the stream position to 0.

\ **Note:** Although the stream position will be set to 0, the first frame of the video stream won't become the current frame.

