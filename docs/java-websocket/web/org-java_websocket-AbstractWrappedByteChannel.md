Package org.java_websocket

# Class AbstractWrappedByteChannel


java.lang.Object
org.java_websocket.AbstractWrappedByteChannel



All Implemented Interfaces:
`Closeable`, `AutoCloseable`, `ByteChannel`, `Channel`, `ReadableByteChannel`, `WritableByteChannel`, `WrappedByteChannel`


---

@Deprecated
public class AbstractWrappedByteChannel
extends Object
implements WrappedByteChannel
Deprecated.






- 


## Constructor Summary

Constructors

Constructor
Description
`AbstractWrappedByteChannel(ByteChannel towrap)`

Deprecated. 

`AbstractWrappedByteChannel(WrappedByteChannel towrap)`

Deprecated. 






- 


## Method Summary





Modifier and Type
Method
Description
`void`
`close()`

Deprecated.
 
`boolean`
`isBlocking()`

Deprecated.
This function returns the blocking state of the channel

`boolean`
`isNeedRead()`

Deprecated.
returns whether readMore should be called to fetch data which has been decoded but not yet been
 returned.

`boolean`
`isNeedWrite()`

Deprecated.
returns whether writeMore should be called write additional data.

`boolean`
`isOpen()`

Deprecated.
 
`int`
`read(ByteBuffer dst)`

Deprecated.
 
`int`
`readMore(ByteBuffer dst)`

Deprecated.
This function does not read data from the underlying channel at all.

`int`
`write(ByteBuffer src)`

Deprecated.
 
`void`
`writeMore()`

Deprecated.
Gets called when `WrappedByteChannel.isNeedWrite()` ()} requires a additional rite






### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`










- 


## Constructor Details




  - 


### AbstractWrappedByteChannel

@Deprecated
public AbstractWrappedByteChannel(ByteChannel towrap)
Deprecated.



  - 


### AbstractWrappedByteChannel

@Deprecated
public AbstractWrappedByteChannel(WrappedByteChannel towrap)
Deprecated.








- 


## Method Details




  - 


### read

public int read(ByteBuffer dst)
         throws IOException
Deprecated.

Specified by:
`read` in interface `ReadableByteChannel`
Throws:
`IOException`




  - 


### isOpen

public boolean isOpen()
Deprecated.

Specified by:
`isOpen` in interface `Channel`




  - 


### close

public void close()
           throws IOException
Deprecated.

Specified by:
`close` in interface `AutoCloseable`
Specified by:
`close` in interface `Channel`
Specified by:
`close` in interface `Closeable`
Throws:
`IOException`




  - 


### write

public int write(ByteBuffer src)
          throws IOException
Deprecated.

Specified by:
`write` in interface `WritableByteChannel`
Throws:
`IOException`




  - 


### isNeedWrite

public boolean isNeedWrite()
Deprecated.
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
Deprecated.
Description copied from interface: `WrappedByteChannel`
Gets called when `WrappedByteChannel.isNeedWrite()` ()} requires a additional rite

Specified by:
`writeMore` in interface `WrappedByteChannel`
Throws:
`IOException` - may be thrown due to an error while writing




  - 


### isNeedRead

public boolean isNeedRead()
Deprecated.
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
Deprecated.
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
Deprecated.
Description copied from interface: `WrappedByteChannel`
This function returns the blocking state of the channel

Specified by:
`isBlocking` in interface `WrappedByteChannel`
Returns:
is the channel blocking