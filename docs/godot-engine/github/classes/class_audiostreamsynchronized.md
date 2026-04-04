:github_url: hide



# AudioStreamSynchronized

**Inherits:** [AudioStream<class_AudioStream>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Stream that can be fitted with sub-streams, which will be played in-sync.


## Description

This is a stream that can be fitted with sub-streams, which will be played in-sync. The streams begin at exactly the same time when play is pressed, and will end when the last of them ends. If one of the sub-streams loops, then playback will continue.


## Properties

> **TABLE**
> :widths: auto
>
> +-----------------------+--------------------------------------------------------------------------+-------+
> | :ref:`int<class_int>` | :ref:`stream_count<class_AudioStreamSynchronized_property_stream_count>` | ``0`` |
> +-----------------------+--------------------------------------------------------------------------+-------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +---------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`AudioStream<class_AudioStream>` | :ref:`get_sync_stream<class_AudioStreamSynchronized_method_get_sync_stream>`\ (\ stream_index\: :ref:`int<class_int>`\ ) |const|                                               |
> +---------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`             | :ref:`get_sync_stream_volume<class_AudioStreamSynchronized_method_get_sync_stream_volume>`\ (\ stream_index\: :ref:`int<class_int>`\ ) |const|                                 |
> +---------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                | :ref:`set_sync_stream<class_AudioStreamSynchronized_method_set_sync_stream>`\ (\ stream_index\: :ref:`int<class_int>`, audio_stream\: :ref:`AudioStream<class_AudioStream>`\ ) |
> +---------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                | :ref:`set_sync_stream_volume<class_AudioStreamSynchronized_method_set_sync_stream_volume>`\ (\ stream_index\: :ref:`int<class_int>`, volume_db\: :ref:`float<class_float>`\ )  |
> +---------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Constants



**MAX_STREAMS** = `32` [🔗<class_AudioStreamSynchronized_constant_MAX_STREAMS>]

Maximum amount of streams that can be synchronized.


----


## Property Descriptions



[int<class_int>] **stream_count** = `0` [🔗<class_AudioStreamSynchronized_property_stream_count>]


- |void| **set_stream_count**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_stream_count**\ (\ )

Set the total amount of streams that will be played back synchronized.


----


## Method Descriptions



[AudioStream<class_AudioStream>] **get_sync_stream**\ (\ stream_index\: [int<class_int>]\ ) |const| [🔗<class_AudioStreamSynchronized_method_get_sync_stream>]

Get one of the synchronized streams, by index.


----



[float<class_float>] **get_sync_stream_volume**\ (\ stream_index\: [int<class_int>]\ ) |const| [🔗<class_AudioStreamSynchronized_method_get_sync_stream_volume>]

Get the volume of one of the synchronized streams, by index.


----



|void| **set_sync_stream**\ (\ stream_index\: [int<class_int>], audio_stream\: [AudioStream<class_AudioStream>]\ ) [🔗<class_AudioStreamSynchronized_method_set_sync_stream>]

Set one of the synchronized streams, by index.


----



|void| **set_sync_stream_volume**\ (\ stream_index\: [int<class_int>], volume_db\: [float<class_float>]\ ) [🔗<class_AudioStreamSynchronized_method_set_sync_stream_volume>]

Set the volume of one of the synchronized streams, by index.

