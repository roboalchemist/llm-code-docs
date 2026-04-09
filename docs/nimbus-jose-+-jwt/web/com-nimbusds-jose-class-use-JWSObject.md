# Uses of Class
com.nimbusds.jose.JWSObject

Packages that use JWSObject

Package
Description
com.nimbusds.jose

Base Javascript Object Signing and Encryption (JOSE) interfaces and classes.

com.nimbusds.jose.mint

JSON Web Signature (JWS) minting framework.

com.nimbusds.jose.proc

Framework for application-specific verification and decryption of JOSE
 objects (with arbitrary payloads).

com.nimbusds.jwt

JSON Web Token (JWT) interfaces and classes.

- 

## Uses of JWSObject in com.nimbusds.jose

Methods in com.nimbusds.jose that return JWSObject

Modifier and Type
Method
Description
`static JWSObject`
JWSObject.`parse(String s)`

Parses a JWS object from the specified string in compact format.

`static JWSObject`
JWSObject.`parse(String s,
 Payload detachedPayload)`

Parses a JWS object from the specified string in compact format and
 a detached payload which can be optionally unencoded (RFC 7797).

`JWSObject`
JWSObjectJSON.Signature.`toJWSObject()`

Returns the compact JWS object representation of this
 individual signature.

`JWSObject`
Payload.`toJWSObject()`

Returns a JWS object representation of this payload.

Constructors in com.nimbusds.jose with parameters of type JWSObject

Modifier
Constructor
Description
` `
`Payload(JWSObject jwsObject)`

Creates a new payload from the specified JWS object.

- 

## Uses of JWSObject in com.nimbusds.jose.mint

Methods in com.nimbusds.jose.mint that return JWSObject

Modifier and Type
Method
Description
`JWSObject`
DefaultJWSMinter.`mint(JWSHeader header,
 Payload payload,
 C context)`

Creates a new JSON Web Signature (JWS) object using the provided
 `JWSHeader` and `Payload`.

`JWSObject`
JWSMinter.`mint(JWSHeader header,
 Payload payload,
 C context)`

Creates a new JSON Web Signature (JWS) object using the provided
 `JWSHeader` and `Payload`.

- 

## Uses of JWSObject in com.nimbusds.jose.proc

Methods in com.nimbusds.jose.proc with parameters of type JWSObject

Modifier and Type
Method
Description
`Payload`
DefaultJOSEProcessor.`process(JWSObject jwsObject,
 C context)`
 
`Payload`
JOSEProcessor.`process(JWSObject jwsObject,
 C context)`

Processes the specified JWS object by verifying its signature.

- 

## Uses of JWSObject in com.nimbusds.jwt

Subclasses of JWSObject in com.nimbusds.jwt

Modifier and Type
Class
Description
`class `
`SignedJWT`

Signed JSON Web Token (JWT).