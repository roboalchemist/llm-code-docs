# Package org.apache.cxf.phase

---

package org.apache.cxf.phase

An InterceptorChain implementation which uses the concept of 
Phases to order message chains.

- 

Related Packages

Package
Description
org.apache.cxf

Contains the Bus, which is the central touch point of CXF, and its related classes.

- 

Class
Description
AbortedInvocationException

Represents transport-specific exceptions which are used to indicate that
 a given invocation was suspended

AbstractPhaseInterceptor<T extends Message>

Provides a starting point implementation for a interceptors that
 participate in phased message processing.

Phase
 
PhaseChainCache

The PhaseChainCache provides default interceptor chains for SOAP requests
 and responses, both from the client and web service side.

PhaseComparator
 
PhaseInterceptor<T extends Message>

A phase interceptor is an intercetor that participates in a
 PhaseInterceptorChain.

PhaseInterceptorChain

A PhaseInterceptorChain orders Interceptors according to the phase they
 participate in and also according to the before invalid input: '&' after properties on an
 Interceptor.

PhaseManager