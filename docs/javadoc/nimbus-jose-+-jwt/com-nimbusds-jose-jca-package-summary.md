# Package com.nimbusds.jose.jca

---

package com.nimbusds.jose.jca

Java Cryptography Architecture (JCA) context interfaces and classes.

 

References:

 

     
- Java
     Cryptography Architecture (JCA) Reference Guide
 

- 

Related Packages

Package
Description
com.nimbusds.jose

Base Javascript Object Signing and Encryption (JOSE) interfaces and classes.

- 

Class
Description
JCAAware<T extends JCAContext>

Interface for a Java Cryptography Architecture (JCA) aware object, intended
 for setting a JCA `provider` and
 `secure random generator`.

JCAContext

Java Cryptography Architecture (JCA) context, consisting of a JCA
 `provider` and
 `secure random generator`.

JCASupport

Java Cryptography Architecture (JCA) support helper.

JWEJCAContext

Java Cryptography Architecture (JCA) context intended specifically for
 JSON Web Encryption (JWE) providers.