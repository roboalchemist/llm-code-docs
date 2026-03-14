Package org.java_websocket.extensions

# Class ExtensionRequestData


java.lang.Object
org.java_websocket.extensions.ExtensionRequestData



---

public class ExtensionRequestData
extends Object






- 


## Field Summary

Fields

Modifier and Type
Field
Description
`static final String`
`EMPTY_VALUE`
 





- 


## Method Summary





Modifier and Type
Method
Description
`String`
`getExtensionName()`
 
`Map<String,String>`
`getExtensionParameters()`
 
`static ExtensionRequestData`
`parseExtensionRequest(String extensionRequest)`
 





### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`










- 


## Field Details




  - 


### EMPTY_VALUE

public static final String EMPTY_VALUE

See Also:




    - Constant Field Values












- 


## Method Details




  - 


### parseExtensionRequest

public static ExtensionRequestData parseExtensionRequest(String extensionRequest)



  - 


### getExtensionName

public String getExtensionName()



  - 


### getExtensionParameters

public Map<String,String> getExtensionParameters()