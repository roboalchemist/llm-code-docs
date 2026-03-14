Package org.java_websocket.drafts

# Class Draft_6455


java.lang.Object
org.java_websocket.drafts.Draft
org.java_websocket.drafts.Draft_6455




---

public class Draft_6455
extends Draft
Implementation for the RFC 6455 websocket protocol This is the recommended class for your
 websocket connection






- 


## Field Summary



### Fields inherited from class org.java_websocket.drafts.Draft

`continuousFrameType, role`




- 


## Constructor Summary

Constructors

Constructor
Description
`Draft_6455()`

Constructor for the websocket protocol specified by RFC 6455 with default extensions

`Draft_6455(List<IExtension> inputExtensions)`

Constructor for the websocket protocol specified by RFC 6455 with custom extensions

`Draft_6455(List<IExtension> inputExtensions,
 int inputMaxFrameSize)`

Constructor for the websocket protocol specified by RFC 6455 with custom extensions and
 protocols

`Draft_6455(List<IExtension> inputExtensions,
 List<IProtocol> inputProtocols)`

Constructor for the websocket protocol specified by RFC 6455 with custom extensions and
 protocols

`Draft_6455(List<IExtension> inputExtensions,
 List<IProtocol> inputProtocols,
 int inputMaxFrameSize)`

Constructor for the websocket protocol specified by RFC 6455 with custom extensions and
 protocols

`Draft_6455(IExtension inputExtension)`

Constructor for the websocket protocol specified by RFC 6455 with custom extensions






- 


## Method Summary





Modifier and Type
Method
Description
`HandshakeState`
`acceptHandshakeAsClient(ClientHandshake request,
 ServerHandshake response)`
 
`HandshakeState`
`acceptHandshakeAsServer(ClientHandshake handshakedata)`
 
`Draft`
`copyInstance()`

Drafts must only be by one websocket at all.

`ByteBuffer`
`createBinaryFrame(Framedata framedata)`
 
`List<Framedata>`
`createFrames(String text,
 boolean mask)`
 
`List<Framedata>`
`createFrames(ByteBuffer binary,
 boolean mask)`
 
`boolean`
`equals(Object o)`
 
`CloseHandshakeType`
`getCloseHandshakeType()`
 
`IExtension`
`getExtension()`

Getter for the extension which is used by this draft

`List<IExtension>`
`getKnownExtensions()`

Getter for all available extensions for this draft

`List<IProtocol>`
`getKnownProtocols()`

Getter for all available protocols for this draft

`int`
`getMaxFrameSize()`

Getter for the maximum allowed payload size which is used by this draft

`IProtocol`
`getProtocol()`

Getter for the protocol which is used by this draft

`int`
`hashCode()`
 
`ClientHandshakeBuilder`
`postProcessHandshakeRequestAsClient(ClientHandshakeBuilder request)`
 
`HandshakeBuilder`
`postProcessHandshakeResponseAsServer(ClientHandshake request,
 ServerHandshakeBuilder response)`
 
`void`
`processFrame(WebSocketImpl webSocketImpl,
 Framedata frame)`

Handle the frame specific to the draft

`void`
`reset()`
 
`String`
`toString()`
 
`List<Framedata>`
`translateFrame(ByteBuffer buffer)`
 





### Methods inherited from class org.java_websocket.drafts.Draft

`basicAccept, checkAlloc, continuousFrame, createHandshake, createHandshake, createHandshake, createHandshake, getRole, readLine, readStringLine, setParseMode, translateHandshake, translateHandshakeHttp`


### Methods inherited from class java.lang.Object

`clone, finalize, getClass, notify, notifyAll, wait, wait, wait`










- 


## Constructor Details




  - 


### Draft_6455

public Draft_6455()
Constructor for the websocket protocol specified by RFC 6455 with default extensions

Since:
1.3.5




  - 


### Draft_6455

public Draft_6455(IExtension inputExtension)
Constructor for the websocket protocol specified by RFC 6455 with custom extensions

Parameters:
`inputExtension` - the extension which should be used for this draft
Since:
1.3.5




  - 


### Draft_6455

public Draft_6455(List<IExtension> inputExtensions)
Constructor for the websocket protocol specified by RFC 6455 with custom extensions

Parameters:
`inputExtensions` - the extensions which should be used for this draft
Since:
1.3.5




  - 


### Draft_6455

public Draft_6455(List<IExtension> inputExtensions,
 List<IProtocol> inputProtocols)
Constructor for the websocket protocol specified by RFC 6455 with custom extensions and
 protocols

Parameters:
`inputExtensions` - the extensions which should be used for this draft
`inputProtocols` - the protocols which should be used for this draft
Since:
1.3.7




  - 


### Draft_6455

public Draft_6455(List<IExtension> inputExtensions,
 int inputMaxFrameSize)
Constructor for the websocket protocol specified by RFC 6455 with custom extensions and
 protocols

Parameters:
`inputExtensions` - the extensions which should be used for this draft
`inputMaxFrameSize` - the maximum allowed size of a frame (the real payload size, decoded
                          frames can be bigger)
Since:
1.4.0




  - 


### Draft_6455

public Draft_6455(List<IExtension> inputExtensions,
 List<IProtocol> inputProtocols,
 int inputMaxFrameSize)
Constructor for the websocket protocol specified by RFC 6455 with custom extensions and
 protocols

Parameters:
`inputExtensions` - the extensions which should be used for this draft
`inputProtocols` - the protocols which should be used for this draft
`inputMaxFrameSize` - the maximum allowed size of a frame (the real payload size, decoded
                          frames can be bigger)
Since:
1.4.0









- 


## Method Details




  - 


### acceptHandshakeAsServer

public HandshakeState acceptHandshakeAsServer(ClientHandshake handshakedata)
                                       throws InvalidHandshakeException

Specified by:
`acceptHandshakeAsServer` in class `Draft`
Throws:
`InvalidHandshakeException`




  - 


### acceptHandshakeAsClient

public HandshakeState acceptHandshakeAsClient(ClientHandshake request,
 ServerHandshake response)
                                       throws InvalidHandshakeException

Specified by:
`acceptHandshakeAsClient` in class `Draft`
Throws:
`InvalidHandshakeException`




  - 


### getExtension

public IExtension getExtension()
Getter for the extension which is used by this draft

Returns:
the extension which is used or null, if handshake is not yet done




  - 


### getKnownExtensions

public List<IExtension> getKnownExtensions()
Getter for all available extensions for this draft

Returns:
the extensions which are enabled for this draft




  - 


### getProtocol

public IProtocol getProtocol()
Getter for the protocol which is used by this draft

Returns:
the protocol which is used or null, if handshake is not yet done or no valid protocols
Since:
1.3.7




  - 


### getMaxFrameSize

public int getMaxFrameSize()
Getter for the maximum allowed payload size which is used by this draft

Returns:
the size, which is allowed for the payload
Since:
1.4.0




  - 


### getKnownProtocols

public List<IProtocol> getKnownProtocols()
Getter for all available protocols for this draft

Returns:
the protocols which are enabled for this draft
Since:
1.3.7




  - 


### postProcessHandshakeRequestAsClient

public ClientHandshakeBuilder postProcessHandshakeRequestAsClient(ClientHandshakeBuilder request)

Specified by:
`postProcessHandshakeRequestAsClient` in class `Draft`




  - 


### postProcessHandshakeResponseAsServer

public HandshakeBuilder postProcessHandshakeResponseAsServer(ClientHandshake request,
 ServerHandshakeBuilder response)
                                                      throws InvalidHandshakeException

Specified by:
`postProcessHandshakeResponseAsServer` in class `Draft`
Throws:
`InvalidHandshakeException`




  - 


### copyInstance

public Draft copyInstance()
Description copied from class: `Draft`
Drafts must only be by one websocket at all. To prevent drafts to be used more than once the
 Websocket implementation should call this method in order to create a new usable version of a
 given draft instance.
 The copy can be safely used in conjunction with a new websocket
 connection.

Specified by:
`copyInstance` in class `Draft`
Returns:
a copy of the draft




  - 


### createBinaryFrame

public ByteBuffer createBinaryFrame(Framedata framedata)

Specified by:
`createBinaryFrame` in class `Draft`




  - 


### translateFrame

public List<Framedata> translateFrame(ByteBuffer buffer)
                               throws InvalidDataException

Specified by:
`translateFrame` in class `Draft`
Throws:
`InvalidDataException`




  - 


### createFrames

public List<Framedata> createFrames(ByteBuffer binary,
 boolean mask)

Specified by:
`createFrames` in class `Draft`




  - 


### createFrames

public List<Framedata> createFrames(String text,
 boolean mask)

Specified by:
`createFrames` in class `Draft`




  - 


### reset

public void reset()

Specified by:
`reset` in class `Draft`




  - 


### processFrame

public void processFrame(WebSocketImpl webSocketImpl,
 Framedata frame)
                  throws InvalidDataException
Description copied from class: `Draft`
Handle the frame specific to the draft

Specified by:
`processFrame` in class `Draft`
Parameters:
`webSocketImpl` - the websocketimpl used for this draft
`frame` - the frame which is supposed to be handled
Throws:
`InvalidDataException` - will be thrown on invalid data




  - 


### getCloseHandshakeType

public CloseHandshakeType getCloseHandshakeType()

Specified by:
`getCloseHandshakeType` in class `Draft`




  - 


### toString

public String toString()

Overrides:
`toString` in class `Draft`




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