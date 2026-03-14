Package org.java_websocket.drafts

# Class Draft


java.lang.Object
org.java_websocket.drafts.Draft



Direct Known Subclasses:
`Draft_6455`


---

public abstract class Draft
extends Object
Base class for everything of a websocket specification which is not common such as the way the
 handshake is read or frames are transferred.






- 


## Field Summary

Fields

Modifier and Type
Field
Description
`protected Opcode`
`continuousFrameType`
 
`protected Role`
`role`

In some cases the handshake will be parsed different depending on whether






- 


## Constructor Summary

Constructors

Constructor
Description
`Draft()`
 





- 


## Method Summary





Modifier and Type
Method
Description
`abstract HandshakeState`
`acceptHandshakeAsClient(ClientHandshake request,
 ServerHandshake response)`
 
`abstract HandshakeState`
`acceptHandshakeAsServer(ClientHandshake handshakedata)`
 
`protected boolean`
`basicAccept(Handshakedata handshakedata)`
 
`int`
`checkAlloc(int bytecount)`
 
`List<Framedata>`
`continuousFrame(Opcode op,
 ByteBuffer buffer,
 boolean fin)`
 
`abstract Draft`
`copyInstance()`

Drafts must only be by one websocket at all.

`abstract ByteBuffer`
`createBinaryFrame(Framedata framedata)`
 
`abstract List<Framedata>`
`createFrames(String text,
 boolean mask)`
 
`abstract List<Framedata>`
`createFrames(ByteBuffer binary,
 boolean mask)`
 
`List<ByteBuffer>`
`createHandshake(Handshakedata handshakedata)`
 
`List<ByteBuffer>`
`createHandshake(Handshakedata handshakedata,
 boolean withcontent)`
 
`List<ByteBuffer>`
`createHandshake(Handshakedata handshakedata,
 Role ownrole)`

Deprecated.
use createHandshake without the role


`List<ByteBuffer>`
`createHandshake(Handshakedata handshakedata,
 Role ownrole,
 boolean withcontent)`

Deprecated.
use createHandshake without the role since it does not have any effect


`abstract CloseHandshakeType`
`getCloseHandshakeType()`
 
`Role`
`getRole()`
 
`abstract ClientHandshakeBuilder`
`postProcessHandshakeRequestAsClient(ClientHandshakeBuilder request)`
 
`abstract HandshakeBuilder`
`postProcessHandshakeResponseAsServer(ClientHandshake request,
 ServerHandshakeBuilder response)`
 
`abstract void`
`processFrame(WebSocketImpl webSocketImpl,
 Framedata frame)`

Handle the frame specific to the draft

`static ByteBuffer`
`readLine(ByteBuffer buf)`
 
`static String`
`readStringLine(ByteBuffer buf)`
 
`abstract void`
`reset()`
 
`void`
`setParseMode(Role role)`
 
`String`
`toString()`
 
`abstract List<Framedata>`
`translateFrame(ByteBuffer buffer)`
 
`Handshakedata`
`translateHandshake(ByteBuffer buf)`
 
`static HandshakeBuilder`
`translateHandshakeHttp(ByteBuffer buf,
 Role role)`
 





### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`










- 


## Field Details




  - 


### role

protected Role role
In some cases the handshake will be parsed different depending on whether



  - 


### continuousFrameType

protected Opcode continuousFrameType








- 


## Constructor Details




  - 


### Draft

public Draft()








- 


## Method Details




  - 


### readLine

public static ByteBuffer readLine(ByteBuffer buf)



  - 


### readStringLine

public static String readStringLine(ByteBuffer buf)



  - 


### translateHandshakeHttp

public static HandshakeBuilder translateHandshakeHttp(ByteBuffer buf,
 Role role)
                                               throws InvalidHandshakeException

Throws:
`InvalidHandshakeException`




  - 


### acceptHandshakeAsClient

public abstract HandshakeState acceptHandshakeAsClient(ClientHandshake request,
 ServerHandshake response)
                                                throws InvalidHandshakeException

Throws:
`InvalidHandshakeException`




  - 


### acceptHandshakeAsServer

public abstract HandshakeState acceptHandshakeAsServer(ClientHandshake handshakedata)
                                                throws InvalidHandshakeException

Throws:
`InvalidHandshakeException`




  - 


### basicAccept

protected boolean basicAccept(Handshakedata handshakedata)



  - 


### createBinaryFrame

public abstract ByteBuffer createBinaryFrame(Framedata framedata)



  - 


### createFrames

public abstract List<Framedata> createFrames(ByteBuffer binary,
 boolean mask)



  - 


### createFrames

public abstract List<Framedata> createFrames(String text,
 boolean mask)



  - 


### processFrame

public abstract void processFrame(WebSocketImpl webSocketImpl,
 Framedata frame)
                           throws InvalidDataException
Handle the frame specific to the draft

Parameters:
`webSocketImpl` - the websocketimpl used for this draft
`frame` - the frame which is supposed to be handled
Throws:
`InvalidDataException` - will be thrown on invalid data




  - 


### continuousFrame

public List<Framedata> continuousFrame(Opcode op,
 ByteBuffer buffer,
 boolean fin)



  - 


### reset

public abstract void reset()



  - 


### createHandshake

@Deprecated
public List<ByteBuffer> createHandshake(Handshakedata handshakedata,
 Role ownrole)
Deprecated.
use createHandshake without the role




  - 


### createHandshake

public List<ByteBuffer> createHandshake(Handshakedata handshakedata)



  - 


### createHandshake

@Deprecated
public List<ByteBuffer> createHandshake(Handshakedata handshakedata,
 Role ownrole,
 boolean withcontent)
Deprecated.
use createHandshake without the role since it does not have any effect




  - 


### createHandshake

public List<ByteBuffer> createHandshake(Handshakedata handshakedata,
 boolean withcontent)



  - 


### postProcessHandshakeRequestAsClient

public abstract ClientHandshakeBuilder postProcessHandshakeRequestAsClient(ClientHandshakeBuilder request)
                                                                    throws InvalidHandshakeException

Throws:
`InvalidHandshakeException`




  - 


### postProcessHandshakeResponseAsServer

public abstract HandshakeBuilder postProcessHandshakeResponseAsServer(ClientHandshake request,
 ServerHandshakeBuilder response)
                                                               throws InvalidHandshakeException

Throws:
`InvalidHandshakeException`




  - 


### translateFrame

public abstract List<Framedata> translateFrame(ByteBuffer buffer)
                                        throws InvalidDataException

Throws:
`InvalidDataException`




  - 


### getCloseHandshakeType

public abstract CloseHandshakeType getCloseHandshakeType()



  - 


### copyInstance

public abstract Draft copyInstance()
Drafts must only be by one websocket at all. To prevent drafts to be used more than once the
 Websocket implementation should call this method in order to create a new usable version of a
 given draft instance.
 The copy can be safely used in conjunction with a new websocket
 connection.

Returns:
a copy of the draft




  - 


### translateHandshake

public Handshakedata translateHandshake(ByteBuffer buf)
                                 throws InvalidHandshakeException

Throws:
`InvalidHandshakeException`




  - 


### checkAlloc

public int checkAlloc(int bytecount)
               throws InvalidDataException

Throws:
`InvalidDataException`




  - 


### setParseMode

public void setParseMode(Role role)



  - 


### getRole

public Role getRole()



  - 


### toString

public String toString()

Overrides:
`toString` in class `Object`