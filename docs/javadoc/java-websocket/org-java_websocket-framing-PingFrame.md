Package org.java_websocket.framing

# Class PingFrame


java.lang.Object
org.java_websocket.framing.FramedataImpl1
org.java_websocket.framing.ControlFrame
org.java_websocket.framing.PingFrame





All Implemented Interfaces:
`Framedata`


---

public class PingFrame
extends ControlFrame
Class to represent a ping frame






- 


## Constructor Summary

Constructors

Constructor
Description
`PingFrame()`

constructor which sets the opcode of this frame to ping






- 


## Method Summary



### Methods inherited from class org.java_websocket.framing.ControlFrame

`isValid`


### Methods inherited from class org.java_websocket.framing.FramedataImpl1

`append, equals, get, getOpcode, getPayloadData, getTransfereMasked, hashCode, isFin, isRSV1, isRSV2, isRSV3, setFin, setPayload, setRSV1, setRSV2, setRSV3, setTransferemasked, toString`


### Methods inherited from class java.lang.Object

`clone, finalize, getClass, notify, notifyAll, wait, wait, wait`










- 


## Constructor Details




  - 


### PingFrame

public PingFrame()
constructor which sets the opcode of this frame to ping