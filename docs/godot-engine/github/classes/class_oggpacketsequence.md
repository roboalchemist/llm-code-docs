:github_url: hide



# OggPacketSequence

**Inherits:** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

A sequence of Ogg packets.


## Description

A sequence of Ogg packets.


## Properties

> **TABLE**
> :widths: auto
>
> +--------------------------------------------------------+------------------------------------------------------------------------------+------------------------+
> | :ref:`PackedInt64Array<class_PackedInt64Array>`        | :ref:`granule_positions<class_OggPacketSequence_property_granule_positions>` | ``PackedInt64Array()`` |
> +--------------------------------------------------------+------------------------------------------------------------------------------+------------------------+
> | :ref:`Array<class_Array>`\[:ref:`Array<class_Array>`\] | :ref:`packet_data<class_OggPacketSequence_property_packet_data>`             | ``[]``                 |
> +--------------------------------------------------------+------------------------------------------------------------------------------+------------------------+
> | :ref:`float<class_float>`                              | :ref:`sampling_rate<class_OggPacketSequence_property_sampling_rate>`         | ``0.0``                |
> +--------------------------------------------------------+------------------------------------------------------------------------------+------------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +---------------------------+----------------------------------------------------------------------------+
> | :ref:`float<class_float>` | :ref:`get_length<class_OggPacketSequence_method_get_length>`\ (\ ) |const| |
> +---------------------------+----------------------------------------------------------------------------+
>

----


## Property Descriptions



[PackedInt64Array<class_PackedInt64Array>] **granule_positions** = `PackedInt64Array()` [🔗<class_OggPacketSequence_property_granule_positions>]


- |void| **set_packet_granule_positions**\ (\ value\: [PackedInt64Array<class_PackedInt64Array>]\ )
- [PackedInt64Array<class_PackedInt64Array>] **get_packet_granule_positions**\ (\ )

Contains the granule positions for each page in this packet sequence.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedInt64Array<class_PackedInt64Array>] for more details.


----



[Array<class_Array>]\[[Array<class_Array>]\] **packet_data** = `[]` [🔗<class_OggPacketSequence_property_packet_data>]


- |void| **set_packet_data**\ (\ value\: [Array<class_Array>]\[[Array<class_Array>]\]\ )
- [Array<class_Array>]\[[Array<class_Array>]\] **get_packet_data**\ (\ )

Contains the raw packets that make up this OggPacketSequence.


----



[float<class_float>] **sampling_rate** = `0.0` [🔗<class_OggPacketSequence_property_sampling_rate>]


- |void| **set_sampling_rate**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_sampling_rate**\ (\ )

Holds sample rate information about this sequence. Must be set by another class that actually understands the codec.


----


## Method Descriptions



[float<class_float>] **get_length**\ (\ ) |const| [🔗<class_OggPacketSequence_method_get_length>]

The length of this stream, in seconds.

