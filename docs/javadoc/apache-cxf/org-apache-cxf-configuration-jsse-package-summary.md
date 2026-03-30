# Package org.apache.cxf.configuration.jsse

---

package org.apache.cxf.configuration.jsse

- 

Related Packages

Package
Description
org.apache.cxf.configuration
 
org.apache.cxf.configuration.security
 
org.apache.cxf.configuration.spring
 

- 

Classes

Class
Description
MultiKeyPasswordKeyManager
 
SSLContextServerParameters

Allows to supply to the HTTP Server the complete SSLContext already preconfigured.

SSLUtils

Holder for utility methods related to manipulating SSL settings, common
 to the connection and listener factories (previously duplicated).

TLSClientParameters

This class extends `TLSParameterBase` with client-specific
 SSL/TLS parameters.

TLSClientParametersConfig

This class provides the TLSClientParameters that programmatically
 configure a HTTPConduit.

TLSClientParametersConfig.TLSClientParametersTypeInternal
 
TLSParameterBase

This class is the base class for SSL/TLS parameters that are common
 to both client and server sides.

TLSParameterJaxBUtils

This class provides some functionality to convert the JAXB
 generated types in the security.xsd to the items needed
 to programatically configure the HTTPConduit and HTTPDestination
 with TLSClientParameters and TLSServerParameters respectively.

TLSServerParameters

This class extends `TLSParameterBase` with service-specific
 SSL/TLS parameters.

TLSServerParametersConfig

This class is used by Spring Config to convert the TLSServerParameters
 JAXB generated type into programmatic TLS Server Parameters for the
 configuration of the http-destination.

TLSServerParametersConfig.TLSServerParametersTypeInternal