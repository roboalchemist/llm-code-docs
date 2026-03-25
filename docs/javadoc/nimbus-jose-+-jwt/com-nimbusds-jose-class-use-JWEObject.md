# Uses of Class
com.nimbusds.jose.JWEObject

Packages that use JWEObject

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

## Uses of JWEObject in com.nimbusds.jose

Methods in com.nimbusds.jose that return JWEObject

Modifier and Type
Method
Description
`static JWEObject`
JWEObject.`parse(String s)`

Parses a JWE object from the specified string in compact form.

Constructors in com.nimbusds.jose with parameters of type JWEObject

Modifier
Constructor
Description
` `
`JWEObjectJSON(JWEObject jweObject)`

Creates a new JWE JSON object from the specified JWE object with
 compact serialisation.

- 

## Uses of JWEObject in com.nimbusds.jose.proc

Methods in com.nimbusds.jose.proc with parameters of type JWEObject

Modifier and Type
Method
Description
`Payload`
DefaultJOSEProcessor.`process(JWEObject jweObject,
 C context)`
 
`Payload`
JOSEProcessor.`process(JWEObject jweObject,
 C context)`

Processes the specified JWE object by decrypting it.

- 

## Uses of JWEObject in com.nimbusds.jwt

Subclasses of JWEObject in com.nimbusds.jwt

Modifier and Type
Class
Description
`class `
`EncryptedJWT`

Encrypted JSON Web Token (JWT).