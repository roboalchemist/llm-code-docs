Package org.java_websocket.framing

# Class FramedataImpl1


java.lang.Object
org.java_websocket.framing.FramedataImpl1



All Implemented Interfaces:
`Framedata`


Direct Known Subclasses:
`ControlFrame`, `DataFrame`


---

public abstract class FramedataImpl1
extends Object
implements Framedata
Abstract implementation of a frame






- 


## Constructor Summary

Constructors

Constructor
Description
`FramedataImpl1(Opcode op)`

Constructor for a FramedataImpl without any attributes set apart from the opcode






- 


## Method Summary





Modifier and Type
Method
Description
`void`
`append(Framedata nextframe)`

Appends an additional frame to the current frame

`boolean`
`equals(Object o)`
 
`static FramedataImpl1`
`get(Opcode opcode)`

Get a frame with a specific opcode

`Opcode`
`getOpcode()`

Defines the interpretation of the "Payload data".

`ByteBuffer`
`getPayloadData()`

The "Payload data" which was sent in this frame

`boolean`
`getTransfereMasked()`

Defines whether the "Payload data" is masked.

`int`
`hashCode()`
 
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

`abstract void`
`isValid()`

Check if the frame is valid due to specification

`void`
`setFin(boolean fin)`

Set the fin of this frame to the provided boolean

`void`
`setPayload(ByteBuffer payload)`

Set the payload of this frame to the provided payload

`void`
`setRSV1(boolean rsv1)`

Set the rsv1 of this frame to the provided boolean

`void`
`setRSV2(boolean rsv2)`

Set the rsv2 of this frame to the provided boolean

`void`
`setRSV3(boolean rsv3)`

Set the rsv3 of this frame to the provided boolean

`void`
`setTransferemasked(boolean transferemasked)`

Set the tranferemask of this frame to the provided boolean

`String`
`toString()`
 





### Methods inherited from class java.lang.Object

`clone, finalize, getClass, notify, notifyAll, wait, wait, wait`










- 


## Constructor Details




  - 


### FramedataImpl1

public FramedataImpl1(Opcode op)
Constructor for a FramedataImpl without any attributes set apart from the opcode

Parameters:
`op` - the opcode to use









- 


## Method Details




  - 


### isValid

public abstract void isValid()
                      throws InvalidDataException
Check if the frame is valid due to specification

Throws:
`InvalidDataException` - thrown if the frame is not a valid frame




  - 


### isRSV1

public boolean isRSV1()
Description copied from interface: `Framedata`
Indicates that this frame has the rsv1 bit set.

Specified by:
`isRSV1` in interface `Framedata`
Returns:
true, if this frame has the rsv1 bit set




  - 


### isRSV2

public boolean isRSV2()
Description copied from interface: `Framedata`
Indicates that this frame has the rsv2 bit set.

Specified by:
`isRSV2` in interface `Framedata`
Returns:
true, if this frame has the rsv2 bit set




  - 


### isRSV3

public boolean isRSV3()
Description copied from interface: `Framedata`
Indicates that this frame has the rsv3 bit set.

Specified by:
`isRSV3` in interface `Framedata`
Returns:
true, if this frame has the rsv3 bit set




  - 


### isFin

public boolean isFin()
Description copied from interface: `Framedata`
Indicates that this is the final fragment in a message.  The first fragment MAY also be the
 final fragment.

Specified by:
`isFin` in interface `Framedata`
Returns:
true, if this frame is the final fragment




  - 


### getOpcode

public Opcode getOpcode()
Description copied from interface: `Framedata`
Defines the interpretation of the "Payload data".

Specified by:
`getOpcode` in interface `Framedata`
Returns:
the interpretation as a Opcode




  - 


### getTransfereMasked

public boolean getTransfereMasked()
Description copied from interface: `Framedata`
Defines whether the "Payload data" is masked.

Specified by:
`getTransfereMasked` in interface `Framedata`
Returns:
true, "Payload data" is masked




  - 


### getPayloadData

public ByteBuffer getPayloadData()
Description copied from interface: `Framedata`
The "Payload data" which was sent in this frame

Specified by:
`getPayloadData` in interface `Framedata`
Returns:
the "Payload data" as ByteBuffer




  - 


### append

public void append(Framedata nextframe)
Description copied from interface: `Framedata`
Appends an additional frame to the current frame
 


 This methods does not override the opcode, but does override the fin

Specified by:
`append` in interface `Framedata`
Parameters:
`nextframe` - the additional frame




  - 


### toString

public String toString()

Overrides:
`toString` in class `Object`




  - 


### setPayload

public void setPayload(ByteBuffer payload)
Set the payload of this frame to the provided payload

Parameters:
`payload` - the payload which is to set




  - 


### setFin

public void setFin(boolean fin)
Set the fin of this frame to the provided boolean

Parameters:
`fin` - true if fin has to be set




  - 


### setRSV1

public void setRSV1(boolean rsv1)
Set the rsv1 of this frame to the provided boolean

Parameters:
`rsv1` - true if rsv1 has to be set




  - 


### setRSV2

public void setRSV2(boolean rsv2)
Set the rsv2 of this frame to the provided boolean

Parameters:
`rsv2` - true if rsv2 has to be set




  - 


### setRSV3

public void setRSV3(boolean rsv3)
Set the rsv3 of this frame to the provided boolean

Parameters:
`rsv3` - true if rsv3 has to be set




  - 


### setTransferemasked

public void setTransferemasked(boolean transferemasked)
Set the tranferemask of this frame to the provided boolean

Parameters:
`transferemasked` - true if transferemasked has to be set




  - 


### get

public static FramedataImpl1 get(Opcode opcode)
Get a frame with a specific opcode

Parameters:
`opcode` - the opcode representing the frame
Returns:
the frame with a specific opcode




  - 


### equals

public boolean equals(Object o)

Overrides:
`equals` in class `Object`




  - 


### hashCode

public int hashCode()

Overrides:
`hashCode` in class `Object`