Package org.java_websocket.client

# Interface DnsResolver




---

public interface DnsResolver
Users may implement this interface to override the default DNS lookup offered by the OS.

Since:
1.4.1







- 


## Method Summary





Modifier and Type
Method
Description
`InetAddress`
`resolve(URI uri)`

Resolves the IP address for the given URI.














- 


## Method Details




  - 


### resolve

InetAddress resolve(URI uri)
             throws UnknownHostException
Resolves the IP address for the given URI.
 


 This method should never return null. If it's not able to resolve the IP address then it should
 throw an UnknownHostException

Parameters:
`uri` - The URI to be resolved
Returns:
The resolved IP address
Throws:
`UnknownHostException` - if no IP address for the `uri` could be found.