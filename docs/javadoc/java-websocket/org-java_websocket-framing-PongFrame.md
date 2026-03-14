Package org.java_websocket.framing

# Class PongFrame


java.lang.Object
org.java_websocket.framing.FramedataImpl1
org.java_websocket.framing.ControlFrame
org.java_websocket.framing.PongFrame





All Implemented Interfaces:
`Framedata`


---

public class PongFrame
extends ControlFrame
Class to represent a pong frame






- 


## Constructor Summary

Constructors

Constructor
Description
`PongFrame()`

constructor which sets the opcode of this frame to pong

`PongFrame(PingFrame pingFrame)`

constructor which sets the opcode of this frame to ping copying over the payload of the ping






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


### PongFrame

public PongFrame()
constructor which sets the opcode of this frame to pong



  - 


### PongFrame

public PongFrame(PingFrame pingFrame)
constructor which sets the opcode of this frame to ping copying over the payload of the ping

Parameters:
`pingFrame` - the PingFrame which payload is to copy