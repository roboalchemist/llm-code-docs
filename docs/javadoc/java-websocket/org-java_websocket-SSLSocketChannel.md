Package org.java_websocket

# Class SSLSocketChannel


java.lang.Object
org.java_websocket.SSLSocketChannel



All Implemented Interfaces:
`Closeable`, `AutoCloseable`, `ByteChannel`, `Channel`, `ReadableByteChannel`, `WritableByteChannel`, `ISSLChannel`, `WrappedByteChannel`


---

public class SSLSocketChannel
extends Object
implements WrappedByteChannel, ByteChannel, ISSLChannel
A class that represents an SSL/TLS peer, and can be extended to create a client or a server.
 


 It makes use of the JSSE framework, and specifically the `SSLEngine` logic, which is
 described by Oracle as "an advanced API, not appropriate for casual use", since it requires the
 user to implement much of the communication establishment procedure himself. More information
 about it can be found here: http://docs.oracle.com/javase/8/docs/technotes/guides/security/jsse/JSSERefGuide.html#SSLEngine
 


 `SSLSocketChannel` implements the handshake protocol, required to establish a connection
 between two peers, which is common for both client and server and provides the abstract `read(ByteBuffer)` and `write(ByteBuffer)` (String)}
 methods, that need to be implemented by the specific SSL/TLS peer that is going to extend this
 class.

Author:
Alex Karnezis
 


 Modified by marci4 to allow the usage as a ByteChannel
 


 Permission for usage received at May 25, 2017 by Alex Karnezis







- 


## Constructor Summary

Constructors

Constructor
Description
`SSLSocketChannel(SocketChannel inputSocketChannel,
 SSLEngine inputEngine,
 ExecutorService inputExecutor,
 SelectionKey key)`
 





- 


## Method Summary





Modifier and Type
Method
Description
`void`
`close()`
 
`SSLEngine`
`getSSLEngine()`

Get the ssl engine used for the de- and encryption of the communication.

`boolean`
`isBlocking()`

This function returns the blocking state of the channel

`boolean`
`isNeedRead()`

returns whether readMore should be called to fetch data which has been decoded but not yet been
 returned.

`boolean`
`isNeedWrite()`

returns whether writeMore should be called write additional data.

`boolean`
`isOpen()`
 
`int`
`read(ByteBuffer dst)`
 
`int`
`readMore(ByteBuffer dst)`

This function does not read data from the underlying channel at all.

`int`
`write(ByteBuffer output)`
 
`void`
`writeMore()`

Gets called when `WrappedByteChannel.isNeedWrite()` ()} requires a additional rite






### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`










- 


## Constructor Details




  - 


### SSLSocketChannel

public SSLSocketChannel(SocketChannel inputSocketChannel,
 SSLEngine inputEngine,
 ExecutorService inputExecutor,
 SelectionKey key)
                 throws IOException

Throws:
`IOException`









- 


## Method Details




  - 


### read

public int read(ByteBuffer dst)
         throws IOException

Specified by:
`read` in interface `ReadableByteChannel`
Throws:
`IOException`




  - 


### write

public int write(ByteBuffer output)
          throws IOException

Specified by:
`write` in interface `WritableByteChannel`
Throws:
`IOException`




  - 


### isNeedWrite

public boolean isNeedWrite()
Description copied from interface: `WrappedByteChannel`
returns whether writeMore should be called write additional data.

Specified by:
`isNeedWrite` in interface `WrappedByteChannel`
Returns:
is a additional write needed




  - 


### writeMore

public void writeMore()
               throws IOException
Description copied from interface: `WrappedByteChannel`
Gets called when `WrappedByteChannel.isNeedWrite()` ()} requires a additional rite

Specified by:
`writeMore` in interface `WrappedByteChannel`
Throws:
`IOException` - may be thrown due to an error while writing




  - 


### isNeedRead

public boolean isNeedRead()
Description copied from interface: `WrappedByteChannel`
returns whether readMore should be called to fetch data which has been decoded but not yet been
 returned.

Specified by:
`isNeedRead` in interface `WrappedByteChannel`
Returns:
is a additional read needed
See Also:




    - `ReadableByteChannel.read(ByteBuffer)`

    - `WrappedByteChannel.readMore(ByteBuffer)`







  - 


### readMore

public int readMore(ByteBuffer dst)
             throws IOException
Description copied from interface: `WrappedByteChannel`
This function does not read data from the underlying channel at all. It is just a way to fetch
 data which has already be received or decoded but was but was not yet returned to the user.
 This could be the case when the decoded data did not fit into the buffer the user passed to
 `ReadableByteChannel.read(ByteBuffer)`.

Specified by:
`readMore` in interface `WrappedByteChannel`
Parameters:
`dst` - the destiny of the read
Returns:
the amount of remaining data
Throws:
`IOException` - when a error occurred during unwrapping




  - 


### isBlocking

public boolean isBlocking()
Description copied from interface: `WrappedByteChannel`
This function returns the blocking state of the channel

Specified by:
`isBlocking` in interface `WrappedByteChannel`
Returns:
is the channel blocking




  - 


### isOpen

public boolean isOpen()

Specified by:
`isOpen` in interface `Channel`




  - 


### close

public void close()
           throws IOException

Specified by:
`close` in interface `AutoCloseable`
Specified by:
`close` in interface `Channel`
Specified by:
`close` in interface `Closeable`
Throws:
`IOException`




  - 


### getSSLEngine

public SSLEngine getSSLEngine()
Description copied from interface: `ISSLChannel`
Get the ssl engine used for the de- and encryption of the communication.

Specified by:
`getSSLEngine` in interface `ISSLChannel`
Returns:
the ssl engine of this channel