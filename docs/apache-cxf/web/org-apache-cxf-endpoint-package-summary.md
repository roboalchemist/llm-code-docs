# Package org.apache.cxf.endpoint

---

package org.apache.cxf.endpoint

Client and Server related classes.

- 

Related Packages

Package
Description
org.apache.cxf

Contains the Bus, which is the central touch point of CXF, and its related classes.

- 

Class
Description
AbstractConduitSelector

Abstract base class holding logic common to any ConduitSelector
 that retrieves a Conduit from the ConduitInitiator.

AbstractEndpointFactory
 
Client
 
Client.Contexts

Wrappers the contexts in a way that allows the contexts
 to be cleared and released in an try-with-resources block

ClientCallback

Asynchronous callback object for calls to `Client.invoke(ClientCallback, String, Object...)`
 and related functions.

ClientImpl
 
ClientLifeCycleListener
 
ClientLifeCycleManager
 
ConduitSelector

Strategy for retrieving a Conduit to mediate an outbound message.

ConduitSelectorHolder
 
DeferredConduitSelector

Strategy for lazy deferred retreival of a Conduit to mediate an
 outbound message.

Endpoint

Represents an endpoint that receives messages.

EndpointException
 
EndpointImpl
 
EndpointImplFactory

This interface defines an object that can create EndpointImpl
 objects.

EndpointResolver

Implementations of this interface are responsible for mapping
 between abstract and concrete endpoint references, and/or
 renewing stale references.

EndpointResolverRegistry

Implementations of this interface are responsible for mediating
 access to registered EndpointResolvers, which themselves map
 between abstract and concrete endpoint references, and/or
 facilitate renewal of stale references.

ListenerRegistrationException
 
ManagedEndpoint
 
NullConduitSelector

Strategy for null Conduit retrieval.

PreexistingConduitSelector

Strategy for retreival of a pre-existing Conduit to mediate an
 outbound message.

Retryable

Implemented by Clients that are willing to accept retried invocations.

Server
 
ServerImpl
 
ServerLifeCycleListener
 
ServerLifeCycleManager
 
ServerRegistry
 
ServiceContractResolver

A `ServiceContractResolver` resolves a service's QName to the URI
 of the service's WSDL contract.

ServiceContractResolverRegistry

A registry for maintaining a collection of contract resolvers.

SimpleEndpointImplFactory

Create ordinary EndpointImpl objects.

UpfrontConduitSelector

Strategy for eager upfront retreival of a Conduit to mediate an
 outbound message.