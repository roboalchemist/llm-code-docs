# StreamPeerBuffer in English

# StreamPeerBuffer

Inherits:StreamPeer<RefCounted<Object
A stream peer used to handle binary data streams.

## Description

A data buffer stream peer that uses a byte array as the stream. This object can be used to handle binary data from network sessions. To handle binary data stored in files,FileAccesscan be used directly.
AStreamPeerBufferobject keeps an internal cursor which is the offset in bytes to the start of the buffer. Get and put operations are performed at the cursor position and will move the cursor accordingly.

## Properties

| PackedByteArray | data_array | PackedByteArray() |

PackedByteArray
data_array
PackedByteArray()

## Methods

| void | clear() |
|---|---|
| StreamPeerBuffer | duplicate()const |
| int | get_position()const |
| int | get_size()const |
| void | resize(size:int) |
| void | seek(position:int) |

void
clear()
StreamPeerBuffer
duplicate()const
get_position()const
get_size()const
void
resize(size:int)
void
seek(position:int)

## Property Descriptions

PackedByteArraydata_array=PackedByteArray()🔗

- voidset_data_array(value:PackedByteArray)
voidset_data_array(value:PackedByteArray)
- PackedByteArrayget_data_array()
PackedByteArrayget_data_array()
The underlying data buffer. Setting this value resets the cursor.
Note:The returned array iscopiedand any changes to it will not update the original property value. SeePackedByteArrayfor more details.

## Method Descriptions

voidclear()🔗
Clears thedata_arrayand resets the cursor.
StreamPeerBufferduplicate()const🔗
Returns a newStreamPeerBufferwith the samedata_arraycontent.
intget_position()const🔗
Returns the current cursor position.
intget_size()const🔗
Returns the size ofdata_array.
voidresize(size:int)🔗
Resizes thedata_array. Thisdoesn'tupdate the cursor.
voidseek(position:int)🔗
Moves the cursor to the specified position.positionmust be a valid index ofdata_array.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
