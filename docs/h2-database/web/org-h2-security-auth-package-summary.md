# Package org.h2.security.auth

---

package org.h2.security.auth

Authentication classes.

- 

Related Packages

Package
Description
org.h2.security

Security classes, such as encryption and cryptographically secure hash
 algorithms.

org.h2.security.auth.impl

Authentication classes.

- 

Class
Description
AuthConfigException

Exception thrown when an issue occurs during the authentication configuration

AuthenticationException

Exception thrown in case of errors during authentication

AuthenticationInfo

Input data for authenticators; it wraps ConnectionInfo

Authenticator

Low level interface to implement full authentication process.

AuthenticatorFactory

Authenticator factory

ConfigProperties

wrapper for configuration properties

Configurable

describe how to perform objects runtime configuration

DefaultAuthenticator

Default authenticator implementation.

H2AuthConfig

Describe configuration of H2 DefaultAuthenticator.

H2AuthConfigXml

Parser of external authentication XML configuration file

HasConfigProperties

Interface for objects with configuration properties.

PropertyConfig

Configuration property

RealmConfig

Configuration for authentication realm.

UserToRolesMapperConfig

Configuration for class that maps users to their roles.