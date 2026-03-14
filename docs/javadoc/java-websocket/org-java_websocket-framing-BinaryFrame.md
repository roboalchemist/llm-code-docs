Package org.java_websocket.framing

# Class BinaryFrame


java.lang.Object
org.java_websocket.framing.FramedataImpl1
org.java_websocket.framing.DataFrame
org.java_websocket.framing.BinaryFrame





All Implemented Interfaces:
`Framedata`


---

public class BinaryFrame
extends DataFrame
Class to represent a binary frame






- 


## Constructor Summary

Constructors

Constructor
Description
`BinaryFrame()`

constructor which sets the opcode of this frame to binary






- 


## Method Summary



### Methods inherited from class org.java_websocket.framing.DataFrame

`isValid`


### Methods inherited from class org.java_websocket.framing.FramedataImpl1

`append, equals, get, getOpcode, getPayloadData, getTransfereMasked, hashCode, isFin, isRSV1, isRSV2, isRSV3, setFin, setPayload, setRSV1, setRSV2, setRSV3, setTransferemasked, toString`


### Methods inherited from class java.lang.Object

`clone, finalize, getClass, notify, notifyAll, wait, wait, wait`










- 


## Constructor Details




  - 


### BinaryFrame

public BinaryFrame()
constructor which sets the opcode of this frame to binary