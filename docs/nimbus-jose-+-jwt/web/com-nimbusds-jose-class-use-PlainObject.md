# Uses of Class
com.nimbusds.jose.PlainObject

Packages that use PlainObject

Package
Description
com.nimbusds.jose

Base Javascript Object Signing and Encryption (JOSE) interfaces and classes.

com.nimbusds.jose.proc

Framework for application-specific verification and decryption of JOSE
 objects (with arbitrary payloads).

com.nimbusds.jwt

JSON Web Token (JWT) interfaces and classes.

- 

## Uses of PlainObject in com.nimbusds.jose

Methods in com.nimbusds.jose that return PlainObject

Modifier and Type
Method
Description
`static PlainObject`
PlainObject.`parse(String s)`

Parses an unsecured JOSE object from the specified string in compact
 format.

- 

## Uses of PlainObject in com.nimbusds.jose.proc

Methods in com.nimbusds.jose.proc with parameters of type PlainObject

Modifier and Type
Method
Description
`Payload`
DefaultJOSEProcessor.`process(PlainObject plainObject,
 C context)`
 
`Payload`
JOSEProcessor.`process(PlainObject plainObject,
 C context)`

Processes the specified unsecured (plain) JOSE object, typically by
 checking its context.

- 

## Uses of PlainObject in com.nimbusds.jwt

Subclasses of PlainObject in com.nimbusds.jwt

Modifier and Type
Class
Description
`class `
`PlainJWT`

Unsecured (plain) JSON Web Token (JWT).