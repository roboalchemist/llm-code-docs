Package org.java_websocket.framing

# Interface Framedata




All Known Implementing Classes:
`BinaryFrame`, `CloseFrame`, `ContinuousFrame`, `ControlFrame`, `DataFrame`, `FramedataImpl1`, `PingFrame`, `PongFrame`, `TextFrame`


---

public interface Framedata
The interface for the frame






- 


## Method Summary





Modifier and Type
Method
Description
`void`
`append(Framedata nextframe)`

Appends an additional frame to the current frame

`Opcode`
`getOpcode()`

Defines the interpretation of the "Payload data".

`ByteBuffer`
`getPayloadData()`

The "Payload data" which was sent in this frame

`boolean`
`getTransfereMasked()`

Defines whether the "Payload data" is masked.

`boolean`
`isFin()`

Indicates that this is the final fragment in a message.

`boolean`
`isRSV1()`

Indicates that this frame has the rsv1 bit set.

`boolean`
`isRSV2()`

Indicates that this frame has the rsv2 bit set.

`boolean`
`isRSV3()`

Indicates that this frame has the rsv3 bit set.














- 


## Method Details




  - 


### isFin

boolean isFin()
Indicates that this is the final fragment in a message.  The first fragment MAY also be the
 final fragment.

Returns:
true, if this frame is the final fragment




  - 


### isRSV1

boolean isRSV1()
Indicates that this frame has the rsv1 bit set.

Returns:
true, if this frame has the rsv1 bit set




  - 


### isRSV2

boolean isRSV2()
Indicates that this frame has the rsv2 bit set.

Returns:
true, if this frame has the rsv2 bit set




  - 


### isRSV3

boolean isRSV3()
Indicates that this frame has the rsv3 bit set.

Returns:
true, if this frame has the rsv3 bit set




  - 


### getTransfereMasked

boolean getTransfereMasked()
Defines whether the "Payload data" is masked.

Returns:
true, "Payload data" is masked




  - 


### getOpcode

Opcode getOpcode()
Defines the interpretation of the "Payload data".

Returns:
the interpretation as a Opcode




  - 


### getPayloadData

ByteBuffer getPayloadData()
The "Payload data" which was sent in this frame

Returns:
the "Payload data" as ByteBuffer




  - 


### append

void append(Framedata nextframe)
Appends an additional frame to the current frame
 


 This methods does not override the opcode, but does override the fin

Parameters:
`nextframe` - the additional frame