Package org.java_websocket.framing

# Class ControlFrame


java.lang.Object
org.java_websocket.framing.FramedataImpl1
org.java_websocket.framing.ControlFrame




All Implemented Interfaces:
`Framedata`


Direct Known Subclasses:
`CloseFrame`, `PingFrame`, `PongFrame`


---

public abstract class ControlFrame
extends FramedataImpl1
Abstract class to represent control frames






- 


## Constructor Summary

Constructors

Constructor
Description
`ControlFrame(Opcode opcode)`

Class to represent a control frame






- 


## Method Summary





Modifier and Type
Method
Description
`void`
`isValid()`

Check if the frame is valid due to specification






### Methods inherited from class org.java_websocket.framing.FramedataImpl1

`append, equals, get, getOpcode, getPayloadData, getTransfereMasked, hashCode, isFin, isRSV1, isRSV2, isRSV3, setFin, setPayload, setRSV1, setRSV2, setRSV3, setTransferemasked, toString`


### Methods inherited from class java.lang.Object

`clone, finalize, getClass, notify, notifyAll, wait, wait, wait`










- 


## Constructor Details




  - 


### ControlFrame

public ControlFrame(Opcode opcode)
Class to represent a control frame

Parameters:
`opcode` - the opcode to use









- 


## Method Details




  - 


### isValid

public void isValid()
             throws InvalidDataException
Description copied from class: `FramedataImpl1`
Check if the frame is valid due to specification

Specified by:
`isValid` in class `FramedataImpl1`
Throws:
`InvalidDataException` - thrown if the frame is not a valid frame