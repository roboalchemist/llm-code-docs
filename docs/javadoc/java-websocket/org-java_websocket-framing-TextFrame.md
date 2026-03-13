Package org.java_websocket.framing

# Class TextFrame


java.lang.Object
org.java_websocket.framing.FramedataImpl1
org.java_websocket.framing.DataFrame
org.java_websocket.framing.TextFrame





All Implemented Interfaces:
`Framedata`


---

public class TextFrame
extends DataFrame
Class to represent a text frames






- 


## Constructor Summary

Constructors

Constructor
Description
`TextFrame()`

constructor which sets the opcode of this frame to text






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


### TextFrame

public TextFrame()
constructor which sets the opcode of this frame to text








- 


## Method Details




  - 


### isValid

public void isValid()
             throws InvalidDataException
Description copied from class: `FramedataImpl1`
Check if the frame is valid due to specification

Overrides:
`isValid` in class `DataFrame`
Throws:
`InvalidDataException` - thrown if the frame is not a valid frame