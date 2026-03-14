Package org.java_websocket

# Class SocketChannelIOHelper


java.lang.Object
org.java_websocket.SocketChannelIOHelper



---

public class SocketChannelIOHelper
extends Object






- 


## Method Summary





Modifier and Type
Method
Description
`static boolean`
`batch(WebSocketImpl ws,
 ByteChannel sockchannel)`

Returns whether the whole outQueue has been flushed

`static boolean`
`read(ByteBuffer buf,
 WebSocketImpl ws,
 ByteChannel channel)`
 
`static boolean`
`readMore(ByteBuffer buf,
 WebSocketImpl ws,
 WrappedByteChannel channel)`
 





### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`










- 


## Method Details




  - 


### read

public static boolean read(ByteBuffer buf,
 WebSocketImpl ws,
 ByteChannel channel)
                    throws IOException

Throws:
`IOException`




  - 


### readMore

public static boolean readMore(ByteBuffer buf,
 WebSocketImpl ws,
 WrappedByteChannel channel)
                        throws IOException

Parameters:
`buf` - The ByteBuffer to read from
`ws` - The WebSocketImpl associated with the channels
`channel` - The channel to read from
Returns:
returns Whether there is more data left which can be obtained via `WrappedByteChannel.readMore(ByteBuffer)`
Throws:
`IOException` - May be thrown by `WrappedByteChannel.readMore(ByteBuffer)`#
See Also:




    - `WrappedByteChannel.readMore(ByteBuffer)`







  - 


### batch

public static boolean batch(WebSocketImpl ws,
 ByteChannel sockchannel)
                     throws IOException
Returns whether the whole outQueue has been flushed

Parameters:
`ws` - The WebSocketImpl associated with the channels
`sockchannel` - The channel to write to
Returns:
returns Whether there is more data to write
Throws:
`IOException` - May be thrown by `WrappedByteChannel.writeMore()`