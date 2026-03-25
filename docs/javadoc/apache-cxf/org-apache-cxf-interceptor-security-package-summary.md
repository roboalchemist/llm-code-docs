# Package org.apache.cxf.interceptor.security

---

package org.apache.cxf.interceptor.security

- 

Related Packages

Package
Description
org.apache.cxf.interceptor

Core interceptor interfaces which form the basis for message processing chains
in CXF.

org.apache.cxf.interceptor.security.callback
 
org.apache.cxf.interceptor.transform
 

- 

Class
Description
AbstractAuthorizingInInterceptor
 
AbstractSecurityContextInInterceptor
 
AbstractUsernameTokenInInterceptor
 
AccessDeniedException
 
AuthenticationException
 
DefaultSecurityContext

SecurityContext which implements isUserInRole using the
 following approach : skip the first Subject principal, and then checks
 Groups the principal is a member of

DelegatingAuthenticationInterceptor
 
DepthRestrictingStreamInterceptor

Creates an XMLStreamReader from the InputStream on the Message.

JAASAuthenticationFeature

Feature to do JAAS authentication with defaults for karaf integration

JAASAuthenticationFeature.Portable
 
JAASLoginInterceptor
 
NameDigestPasswordCallbackHandler
 
NamePasswordCallbackHandler
 
OperationInfoAuthorizingInterceptor
 
RolePrefixSecurityContextImpl
 
SecureAnnotationsInterceptor
 
SimpleAuthorizingInterceptor