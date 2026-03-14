Package org.java_websocket

# Interface WrappedByteChannel




All Superinterfaces:
`AutoCloseable`, `ByteChannel`, `Channel`, `Closeable`, `ReadableByteChannel`, `WritableByteChannel`


All Known Implementing Classes:
`AbstractWrappedByteChannel`, `SSLSocketChannel`, `SSLSocketChannel2`


---

public interface WrappedByteChannel
extends ByteChannel






- 


## Method Summary





Modifier and Type
Method
Description
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

`int`
`readMore(ByteBuffer dst)`

This function does not read data from the underlying channel at all.

`void`
`writeMore()`

Gets called when `isNeedWrite()` ()} requires a additional rite






### Methods inherited from interface java.nio.channels.Channel

`close, isOpen`


### Methods inherited from interface java.nio.channels.ReadableByteChannel

`read`


### Methods inherited from interface java.nio.channels.WritableByteChannel

`write`










- 


## Method Details




  - 


### isNeedWrite

boolean isNeedWrite()
returns whether writeMore should be called write additional data.

Returns:
is a additional write needed




  - 


### writeMore

void writeMore()
        throws IOException
Gets called when `isNeedWrite()` ()} requires a additional rite

Throws:
`IOException` - may be thrown due to an error while writing




  - 


### isNeedRead

boolean isNeedRead()
returns whether readMore should be called to fetch data which has been decoded but not yet been
 returned.

Returns:
is a additional read needed
See Also:




    - `ReadableByteChannel.read(ByteBuffer)`

    - `readMore(ByteBuffer)`







  - 


### readMore

int readMore(ByteBuffer dst)
      throws IOException
This function does not read data from the underlying channel at all. It is just a way to fetch
 data which has already be received or decoded but was but was not yet returned to the user.
 This could be the case when the decoded data did not fit into the buffer the user passed to
 `ReadableByteChannel.read(ByteBuffer)`.

Parameters:
`dst` - the destiny of the read
Returns:
the amount of remaining data
Throws:
`IOException` - when a error occurred during unwrapping




  - 


### isBlocking

boolean isBlocking()
This function returns the blocking state of the channel

Returns:
is the channel blocking