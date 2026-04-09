# Package org.apache.cxf.interceptor

---

package org.apache.cxf.interceptor

Core interceptor interfaces which form the basis for message processing chains
in CXF.  Interceptors are grouped into ordered lists called an interceptor
chains.  There is both an outbound and an inbound interceptor chain for both 
a CXF-based SOAP client, and a CXF-based web service.  Additionally, in 
the case of SOAPFaults, a CXF web service will create a separate outbound 
error handling chain and the client an inbound one.

- 

Related Packages

Package
Description
org.apache.cxf

Contains the Bus, which is the central touch point of CXF, and its related classes.

org.apache.cxf.interceptor.security
 
org.apache.cxf.interceptor.transform
 

- 

Class
Description
AbstractAttributedInterceptorProvider
 
AbstractBasicInterceptorProvider
 
AbstractFaultChainInitiatorObserver
 
AbstractInDatabindingInterceptor
 
AbstractLoggingInterceptor
Deprecated. 
AbstractOutDatabindingInterceptor
 
AnnotationInterceptors
 
AttachmentInInterceptor
 
AttachmentOutInterceptor
 
ClientFaultConverter

Takes a Fault and converts it to a local exception type if possible.

ClientOutFaultObserver
 
Fault

A Fault that occurs during invocation processing.

FaultOutInterceptor
 
FaultOutInterceptor.FaultInfoException

Marker interfaces for Exceptions that have a
 getFaultInfo() method that returns some sort
 of object that the FaultOutInterceptor can
 marshal into a fault detail element

FIStaxInInterceptor

Creates an XMLStreamReader from the InputStream on the Message.

FIStaxOutInterceptor

Creates an XMLStreamReader from the InputStream on the Message.

InFaultChainInitiatorObserver
 
InFaultInterceptors

Specifies a list of classes that are added to the inbound fault
 interceptor chain.

InInterceptors

Specifies a list of classes that are added to the inbound interceptor
 chain.

Interceptor<T extends Message>

Base interface for all interceptors.

InterceptorChain

Base interface for all interceptor chains.

InterceptorChain.State
 
InterceptorProvider

The `InterceptorProvider` interface is implemented by objects
 that have interceptor chains associated with them.

MessageSenderInterceptor

Takes the Conduit from the exchange and sends the message through it.

MessageSenderInterceptor.MessageSenderEndingInterceptor
 
OneWayInterceptor<T extends Message>

Base interface for client interceptors that are compatible with one way 
 message processing (primarily, JAX-WS).

OneWayProcessorInterceptor
 
OutFaultChainInitiatorObserver
 
OutFaultInterceptors

Specifies a list of classes that are added to the outbound fault
 interceptor chain.

OutgoingChainInterceptor
 
OutInterceptors

Specifies a list of classes that are added to the outbound
 interceptor chain.

ServiceInvokerInterceptor

Invokes a Binding's invoker with the `INVOCATION_INPUT` from
 the Exchange.

StaxInEndingInterceptor
 
StaxInInterceptor

Creates an XMLStreamReader from the InputStream on the Message.

StaxOutEndingInterceptor
 
StaxOutInterceptor

Creates an XMLStreamWriter from the OutputStream on the Message.