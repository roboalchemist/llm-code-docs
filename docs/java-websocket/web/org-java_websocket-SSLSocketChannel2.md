Package org.java_websocket

# Class SSLSocketChannel2


java.lang.Object
org.java_websocket.SSLSocketChannel2



All Implemented Interfaces:
`Closeable`, `AutoCloseable`, `ByteChannel`, `Channel`, `ReadableByteChannel`, `WritableByteChannel`, `ISSLChannel`, `WrappedByteChannel`


---

public class SSLSocketChannel2
extends Object
implements ByteChannel, WrappedByteChannel, ISSLChannel
Implements the relevant portions of the SocketChannel interface with the SSLEngine wrapper.






- 


## Field Summary

Fields

Modifier and Type
Field
Description
`protected int`
`bufferallocations`

Should be used to count the buffer allocations.

`protected static ByteBuffer`
`emptybuffer`

This object is used to feed the `SSLEngine`'s wrap and unwrap methods during the
 handshake phase.

`protected ExecutorService`
`exec`
 
`protected ByteBuffer`
`inCrypt`

encrypted data incoming

`protected ByteBuffer`
`inData`

raw payload incoming

`protected ByteBuffer`
`outCrypt`

encrypted data outgoing

`protected SSLEngineResult`
`readEngineResult`
 
`protected SelectionKey`
`selectionKey`

used to set interestOP SelectionKey.OP_WRITE for the underlying channel

`protected SocketChannel`
`socketChannel`

the underlying channel

`protected SSLEngine`
`sslEngine`
 
`protected List<Future<?>>`
`tasks`
 
`protected SSLEngineResult`
`writeEngineResult`
 





- 


## Constructor Summary

Constructors

Constructor
Description
`SSLSocketChannel2(SocketChannel channel,
 SSLEngine sslEngine,
 ExecutorService exec,
 SelectionKey key)`
 





- 


## Method Summary





Modifier and Type
Method
Description
`void`
`close()`
 
`SelectableChannel`
`configureBlocking(boolean b)`
 
`boolean`
`connect(SocketAddress remote)`
 
`protected void`
`consumeDelegatedTasks()`
 
`protected void`
`createBuffers(SSLSession session)`
 
`boolean`
`finishConnect()`
 
`SSLEngine`
`getSSLEngine()`

Get the ssl engine used for the de- and encryption of the communication.

`boolean`
`isBlocking()`

This function returns the blocking state of the channel

`boolean`
`isConnected()`
 
`boolean`
`isInboundDone()`
 
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

Blocks when in blocking mode until at least one byte has been decoded.
 When not in blocking
 mode 0 may be returned.

`int`
`readMore(ByteBuffer dst)`

This function does not read data from the underlying channel at all.

`Socket`
`socket()`
 
`int`
`write(ByteBuffer src)`
 
`void`
`writeMore()`

Gets called when `WrappedByteChannel.isNeedWrite()` ()} requires a additional rite






### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`










- 


## Field Details




  - 


### emptybuffer

protected static ByteBuffer emptybuffer
This object is used to feed the `SSLEngine`'s wrap and unwrap methods during the
 handshake phase.



  - 


### exec

protected ExecutorService exec



  - 


### tasks

protected List<Future<?>> tasks



  - 


### inData

protected ByteBuffer inData
raw payload incoming



  - 


### outCrypt

protected ByteBuffer outCrypt
encrypted data outgoing



  - 


### inCrypt

protected ByteBuffer inCrypt
encrypted data incoming



  - 


### socketChannel

protected SocketChannel socketChannel
the underlying channel



  - 


### selectionKey

protected SelectionKey selectionKey
used to set interestOP SelectionKey.OP_WRITE for the underlying channel



  - 


### sslEngine

protected SSLEngine sslEngine



  - 


### readEngineResult

protected SSLEngineResult readEngineResult



  - 


### writeEngineResult

protected SSLEngineResult writeEngineResult



  - 


### bufferallocations

protected int bufferallocations
Should be used to count the buffer allocations. But because of #190 where
 HandshakeStatus.FINISHED is not properly returned by nio wrap/unwrap this variable is used to
 check whether `createBuffers(SSLSession)` needs to be called.








- 


## Constructor Details




  - 


### SSLSocketChannel2

public SSLSocketChannel2(SocketChannel channel,
 SSLEngine sslEngine,
 ExecutorService exec,
 SelectionKey key)
                  throws IOException

Throws:
`IOException`









- 


## Method Details




  - 


### consumeDelegatedTasks

protected void consumeDelegatedTasks()



  - 


### createBuffers

protected void createBuffers(SSLSession session)



  - 


### write

public int write(ByteBuffer src)
          throws IOException

Specified by:
`write` in interface `WritableByteChannel`
Throws:
`IOException`




  - 


### read

public int read(ByteBuffer dst)
         throws IOException
Blocks when in blocking mode until at least one byte has been decoded.
 When not in blocking
 mode 0 may be returned.

Specified by:
`read` in interface `ReadableByteChannel`
Returns:
the number of bytes read.
Throws:
`IOException`




  - 


### isConnected

public boolean isConnected()



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


### configureBlocking

public SelectableChannel configureBlocking(boolean b)
                                    throws IOException

Throws:
`IOException`




  - 


### connect

public boolean connect(SocketAddress remote)
                throws IOException

Throws:
`IOException`




  - 


### finishConnect

public boolean finishConnect()
                      throws IOException

Throws:
`IOException`




  - 


### socket

public Socket socket()



  - 


### isInboundDone

public boolean isInboundDone()



  - 


### isOpen

public boolean isOpen()

Specified by:
`isOpen` in interface `Channel`




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
             throws SSLException
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
`SSLException`




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


### getSSLEngine

public SSLEngine getSSLEngine()
Description copied from interface: `ISSLChannel`
Get the ssl engine used for the de- and encryption of the communication.

Specified by:
`getSSLEngine` in interface `ISSLChannel`
Returns:
the ssl engine of this channel