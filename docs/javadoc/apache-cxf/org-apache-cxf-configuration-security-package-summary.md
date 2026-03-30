# Package org.apache.cxf.configuration.security

---

package org.apache.cxf.configuration.security

- 

Related Packages

Package
Description
org.apache.cxf.configuration
 
org.apache.cxf.configuration.jsse
 
org.apache.cxf.configuration.spring
 

- 

Class
Description
AuthorizationPolicy

This structure holds parameters that may govern authentication
             that use a User Password strategy.

CertificateConstraintsType

This structure holds a list of regular expressions that corresponds to a sequence of
         Certificate Constraints on either the Subject or Issuer DN.

CertStoreType

A CertStoreType represents a catenated sequence of X.509 certificates, 
         in PEM or DER format.

CipherSuites

This structure holds a list of ciphersuite names that are to be
         supported.

ClientAuthentication

<p>Java class for ClientAuthentication complex type</p>.

CombinatorType

This type refers to whether ALL or ANY of the DNConstraintsType regular expressions 
         must be satisfied.

DNConstraintsType

This structure holds a list of regular expressions that corresponds to a sequence of
         Certificate Constraints.

ExcludeProtocols

This structure holds a list of protocols that are to be excluded.

FiltersType

<p>Java class for FiltersType complex type</p>.

IncludeProtocols

This structure holds a list of protocols that are to be included.

KeyManagersType

This structure specifies the JSSE based KeyManagers for a single
         Keystore.

KeyStoreType

A KeyStoreType represents the information needed to load a collection
         of key and certificate material from a desired location.

ObjectFactory

This object contains factory methods for each 
 Java content interface and Java element interface 
 generated in the org.apache.cxf.configuration.security package.

ProxyAuthorizationPolicy

<p>Java class for ProxyAuthorizationPolicy complex type</p>.

SecureRandomParameters

This structure holds the parameters for the Secure Random Number
         generator used in the JSSE.

ServerNames

This structure holds the list of SNI server names.

TLSClientParametersType

<p>Java class for TLSClientParametersType complex type</p>.

TLSServerParametersType

<p>Java class for TLSServerParametersType complex type</p>.

TrustManagersType

This structure contains the specification of JSSE TrustManagers for
         a single Keystore used for trusted certificates.