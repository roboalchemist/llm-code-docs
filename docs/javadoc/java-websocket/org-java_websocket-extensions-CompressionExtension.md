Package org.java_websocket.extensions

# Class CompressionExtension


java.lang.Object
org.java_websocket.extensions.DefaultExtension
org.java_websocket.extensions.CompressionExtension




All Implemented Interfaces:
`IExtension`


Direct Known Subclasses:
`PerMessageDeflateExtension`


---

public abstract class CompressionExtension
extends DefaultExtension
Implementation for a compression extension specified by https://tools.ietf.org/html/rfc7692

Since:
1.3.5







- 


## Constructor Summary

Constructors

Constructor
Description
`CompressionExtension()`
 





- 


## Method Summary





Modifier and Type
Method
Description
`void`
`isFrameValid(Framedata inputFrame)`

Check if the received frame is correctly implemented by the other endpoint and there are no
 specification errors (like wrongly set RSV)






### Methods inherited from class org.java_websocket.extensions.DefaultExtension

`acceptProvidedExtensionAsClient, acceptProvidedExtensionAsServer, copyInstance, decodeFrame, encodeFrame, equals, getProvidedExtensionAsClient, getProvidedExtensionAsServer, hashCode, reset, toString`


### Methods inherited from class java.lang.Object

`clone, finalize, getClass, notify, notifyAll, wait, wait, wait`










- 


## Constructor Details




  - 


### CompressionExtension

public CompressionExtension()








- 


## Method Details




  - 


### isFrameValid

public void isFrameValid(Framedata inputFrame)
                  throws InvalidDataException
Description copied from interface: `IExtension`
Check if the received frame is correctly implemented by the other endpoint and there are no
 specification errors (like wrongly set RSV)

Specified by:
`isFrameValid` in interface `IExtension`
Overrides:
`isFrameValid` in class `DefaultExtension`
Parameters:
`inputFrame` - the received frame
Throws:
`InvalidDataException` - Throw InvalidDataException if the received frame is not correctly
                              implementing the specification for the specific extension