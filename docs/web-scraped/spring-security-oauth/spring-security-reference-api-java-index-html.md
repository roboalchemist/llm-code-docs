# Source: https://docs.spring.io/spring-security/reference/api/java/index.html

Title: Overview (spring-security-docs 7.0.3 API)

URL Source: https://docs.spring.io/spring-security/reference/api/java/index.html

Published Time: Mon, 09 Mar 2026 15:09:17 GMT

Markdown Content:
Overview (spring-security-docs 7.0.3 API)
===============

[Skip navigation links](https://docs.spring.io/spring-security/reference/api/java/index.html#skip-navbar-top "Skip navigation links")

*   Overview
*   Package
*   Class
*   [Tree](https://docs.spring.io/spring-security/reference/api/java/overview-tree.html)
*   [Deprecated](https://docs.spring.io/spring-security/reference/api/java/deprecated-list.html)
*   [Index](https://docs.spring.io/spring-security/reference/api/java/index-all.html)
*   [Help](https://docs.spring.io/spring-security/reference/api/java/help-doc.html#overview)

SEARCH: 

spring-security-docs 7.0.3 API
==============================

Packages

Package

Description

[org.springframework.security.access](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/access/package-summary.html)

Core access-control related code, including security metadata related classes, interception code, access control annotations, EL support and voter-based implementations of the central [`AccessDecisionManager`](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/access/AccessDecisionManager.html "interface in org.springframework.security.access") interface.

[org.springframework.security.access.annotation](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/access/annotation/package-summary.html)

Support for JSR-250 and Spring Security `@Secured` annotations.

[org.springframework.security.access.event](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/access/event/package-summary.html)

Authorization event and listener classes.

[org.springframework.security.access.expression](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/access/expression/package-summary.html)

Expression handling code to support the use of Spring-EL based expressions in `@PreAuthorize`, `@PreFilter`, `@PostAuthorize` and `@PostFilter` annotations.

[org.springframework.security.access.expression.method](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/access/expression/method/package-summary.html)

Implementation of expression-based method security.

[org.springframework.security.access.hierarchicalroles](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/access/hierarchicalroles/package-summary.html)

Role hierarchy implementation.

[org.springframework.security.access.intercept](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/access/intercept/package-summary.html)

Abstract level security interception classes which are responsible for enforcing the configured security constraints for a secure object.

[org.springframework.security.access.intercept.aopalliance](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/access/intercept/aopalliance/package-summary.html)

Enforces security for AOP Alliance `MethodInvocation`s, such as via Spring AOP.

[org.springframework.security.access.intercept.aspectj](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/access/intercept/aspectj/package-summary.html)

Enforces security for AspectJ `JointPoint`s, delegating secure object callbacks to the calling aspect.

[org.springframework.security.access.method](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/access/method/package-summary.html)

Provides `SecurityMetadataSource` implementations for securing Java method invocations via different AOP libraries.

[org.springframework.security.access.prepost](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/access/prepost/package-summary.html)

Contains the infrastructure classes for handling the `@PreAuthorize`, `@PreFilter`, `@PostAuthorize` and `@PostFilter` annotations.

[org.springframework.security.access.vote](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/access/vote/package-summary.html)

Implements a vote-based approach to authorization decisions.

[org.springframework.security.acls](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/acls/package-summary.html)

The Spring Security ACL package which implements instance-based security for domain objects.

[org.springframework.security.acls.afterinvocation](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/acls/afterinvocation/package-summary.html)

After-invocation providers for collection and array filtering.

[org.springframework.security.acls.domain](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/acls/domain/package-summary.html)

Basic implementation of access control lists (ACLs) interfaces.

[org.springframework.security.acls.jdbc](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/acls/jdbc/package-summary.html)

JDBC-based persistence of ACL information

[org.springframework.security.acls.model](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/acls/model/package-summary.html)

Interfaces and shared classes to manage access control lists (ACLs) for domain object instances.

[org.springframework.security.aot.hint](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/aot/hint/package-summary.html)

[org.springframework.security.authentication](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/authentication/package-summary.html)

Core classes and interfaces related to user authentication, which are used throughout Spring Security.

[org.springframework.security.authentication.dao](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/authentication/dao/package-summary.html)

An `AuthenticationProvider` which relies upon a data access object.

[org.springframework.security.authentication.event](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/authentication/event/package-summary.html)

Authentication success and failure events which can be published to the Spring application context.

[org.springframework.security.authentication.jaas](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/authentication/jaas/package-summary.html)

An authentication provider for JAAS.

[org.springframework.security.authentication.jaas.event](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/authentication/jaas/event/package-summary.html)

JAAS authentication events which can be published to the Spring application context by the JAAS authentication provider.

[org.springframework.security.authentication.jaas.memory](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/authentication/jaas/memory/package-summary.html)

An in memory JAAS implementation.

[org.springframework.security.authentication.ott](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/authentication/ott/package-summary.html)

[org.springframework.security.authentication.ott.reactive](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/authentication/ott/reactive/package-summary.html)

[org.springframework.security.authentication.password](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/authentication/password/package-summary.html)

[org.springframework.security.authorization](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/authorization/package-summary.html)

[org.springframework.security.authorization.event](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/authorization/event/package-summary.html)

[org.springframework.security.authorization.method](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/authorization/method/package-summary.html)

[org.springframework.security.cas](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/cas/package-summary.html)

Spring Security support for Apereo's Central Authentication Service ([CAS](https://github.com/apereo/cas)).

[org.springframework.security.cas.authentication](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/cas/authentication/package-summary.html)

An `AuthenticationProvider` that can process CAS service tickets and proxy tickets.

[org.springframework.security.cas.jackson](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/cas/jackson/package-summary.html)

Jackson 3+ serialization support for CAS.

[org.springframework.security.cas.jackson2](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/cas/jackson2/package-summary.html)

Jackson 2 support for CAS.

[org.springframework.security.cas.userdetails](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/cas/userdetails/package-summary.html)

[`UserDetails`](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/core/userdetails/UserDetails.html "interface in org.springframework.security.core.userdetails") abstractions for CAS.

[org.springframework.security.cas.web](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/cas/web/package-summary.html)

Authenticates standard web browser users via CAS.

[org.springframework.security.cas.web.authentication](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/cas/web/authentication/package-summary.html)

Authentication processing mechanisms which respond to the submission of authentication credentials using CAS.

[org.springframework.security.concurrent](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/concurrent/package-summary.html)

[org.springframework.security.config](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/config/package-summary.html)

Support classes for the Spring Security namespace.

[org.springframework.security.config.annotation](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/config/annotation/package-summary.html)

[org.springframework.security.config.annotation.authentication](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/config/annotation/authentication/package-summary.html)

[org.springframework.security.config.annotation.authentication.builders](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/config/annotation/authentication/builders/package-summary.html)

[org.springframework.security.config.annotation.authentication.configuration](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/config/annotation/authentication/configuration/package-summary.html)

[org.springframework.security.config.annotation.authentication.configurers.ldap](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/config/annotation/authentication/configurers/ldap/package-summary.html)

[org.springframework.security.config.annotation.authentication.configurers.provisioning](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/config/annotation/authentication/configurers/provisioning/package-summary.html)

[org.springframework.security.config.annotation.authentication.configurers.userdetails](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/config/annotation/authentication/configurers/userdetails/package-summary.html)

[org.springframework.security.config.annotation.authorization](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/config/annotation/authorization/package-summary.html)

[org.springframework.security.config.annotation.configuration](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/config/annotation/configuration/package-summary.html)

[org.springframework.security.config.annotation.method.configuration](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/config/annotation/method/configuration/package-summary.html)

[org.springframework.security.config.annotation.rsocket](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/config/annotation/rsocket/package-summary.html)

[org.springframework.security.config.annotation.web](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/config/annotation/web/package-summary.html)

[org.springframework.security.config.annotation.web.builders](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/config/annotation/web/builders/package-summary.html)

[org.springframework.security.config.annotation.web.configuration](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/config/annotation/web/configuration/package-summary.html)

[org.springframework.security.config.annotation.web.configurers](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/config/annotation/web/configurers/package-summary.html)

[org.springframework.security.config.annotation.web.configurers.oauth2.client](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/config/annotation/web/configurers/oauth2/client/package-summary.html)

[org.springframework.security.config.annotation.web.configurers.oauth2.server.authorization](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/config/annotation/web/configurers/oauth2/server/authorization/package-summary.html)

[org.springframework.security.config.annotation.web.configurers.oauth2.server.resource](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/config/annotation/web/configurers/oauth2/server/resource/package-summary.html)

[org.springframework.security.config.annotation.web.configurers.ott](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/config/annotation/web/configurers/ott/package-summary.html)

[org.springframework.security.config.annotation.web.configurers.saml2](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/config/annotation/web/configurers/saml2/package-summary.html)

[org.springframework.security.config.annotation.web.reactive](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/config/annotation/web/reactive/package-summary.html)

[org.springframework.security.config.annotation.web.servlet.configuration](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/config/annotation/web/servlet/configuration/package-summary.html)

[org.springframework.security.config.annotation.web.socket](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/config/annotation/web/socket/package-summary.html)

[org.springframework.security.config.authentication](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/config/authentication/package-summary.html)

Parsing of <authentication-manager> and related elements.

[org.springframework.security.config.core](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/config/core/package-summary.html)

[org.springframework.security.config.core.userdetails](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/config/core/userdetails/package-summary.html)

[org.springframework.security.config.crypto](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/config/crypto/package-summary.html)

[org.springframework.security.config.debug](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/config/debug/package-summary.html)

[org.springframework.security.config.http](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/config/http/package-summary.html)

Parsing of the <http> namespace element.

[org.springframework.security.config.ldap](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/config/ldap/package-summary.html)

Security namespace support for LDAP authentication.

[org.springframework.security.config.method](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/config/method/package-summary.html)

Support for parsing of the <global-method-security> and <intercept-methods> elements.

[org.springframework.security.config.oauth2.client](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/config/oauth2/client/package-summary.html)

[org.springframework.security.config.observation](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/config/observation/package-summary.html)

[org.springframework.security.config.provisioning](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/config/provisioning/package-summary.html)

[org.springframework.security.config.saml2](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/config/saml2/package-summary.html)

[org.springframework.security.config.web](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/config/web/package-summary.html)

[org.springframework.security.config.web.messaging](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/config/web/messaging/package-summary.html)

[org.springframework.security.config.web.server](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/config/web/server/package-summary.html)

[org.springframework.security.config.websocket](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/config/websocket/package-summary.html)

[org.springframework.security.context](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/context/package-summary.html)

[org.springframework.security.converter](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/converter/package-summary.html)

[org.springframework.security.core](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/core/package-summary.html)

Core classes and interfaces related to user authentication and authorization, as well as the maintenance of a security context.

[org.springframework.security.core.annotation](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/core/annotation/package-summary.html)

[org.springframework.security.core.authority](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/core/authority/package-summary.html)

The default implementation of the `GrantedAuthority` interface.

[org.springframework.security.core.authority.mapping](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/core/authority/mapping/package-summary.html)

Strategies for mapping a list of attributes (such as roles or LDAP groups) to a list of `GrantedAuthority`s.

[org.springframework.security.core.context](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/core/context/package-summary.html)

Classes related to the establishment of a security context for the duration of a request (such as an HTTP or RMI invocation).

[org.springframework.security.core.parameters](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/core/parameters/package-summary.html)

[org.springframework.security.core.session](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/core/session/package-summary.html)

Session abstraction which is provided by the 
```
org.springframework.security.core.session.SessionInformation
 SessionInformation
```
 class.

[org.springframework.security.core.token](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/core/token/package-summary.html)

A service for building secure random tokens.

[org.springframework.security.core.userdetails](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/core/userdetails/package-summary.html)

The standard interfaces for implementing user data DAOs.

[org.springframework.security.core.userdetails.cache](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/core/userdetails/cache/package-summary.html)

Implementations of [`UserCache`](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/core/userdetails/UserCache.html "interface in org.springframework.security.core.userdetails").

[org.springframework.security.core.userdetails.jdbc](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/core/userdetails/jdbc/package-summary.html)

Exposes a JDBC-based authentication repository, implementing `org.springframework.security.core.userdetails.UserDetailsService UserDetailsService`.

[org.springframework.security.core.userdetails.memory](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/core/userdetails/memory/package-summary.html)

Exposes an in-memory authentication repository.

[org.springframework.security.crypto.argon2](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/crypto/argon2/package-summary.html)

[org.springframework.security.crypto.bcrypt](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/crypto/bcrypt/package-summary.html)

[org.springframework.security.crypto.codec](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/crypto/codec/package-summary.html)

Internal codec classes.

[org.springframework.security.crypto.encrypt](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/crypto/encrypt/package-summary.html)

[org.springframework.security.crypto.factory](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/crypto/factory/package-summary.html)

[org.springframework.security.crypto.keygen](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/crypto/keygen/package-summary.html)

[org.springframework.security.crypto.password](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/crypto/password/package-summary.html)

[org.springframework.security.crypto.password4j](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/crypto/password4j/package-summary.html)

[org.springframework.security.crypto.scrypt](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/crypto/scrypt/package-summary.html)

[org.springframework.security.crypto.util](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/crypto/util/package-summary.html)

[org.springframework.security.data.aot.hint](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/data/aot/hint/package-summary.html)

AOT integration for Spring Security's Data integration.

[org.springframework.security.data.repository.query](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/data/repository/query/package-summary.html)

Spring Security extensions for Spring Data queries.

[org.springframework.security.jackson](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/jackson/package-summary.html)

Jackson 3+ serialization support.

[org.springframework.security.jackson2](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/jackson2/package-summary.html)

Jackson 2 serialization support.

[org.springframework.security.kerberos.authentication](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/kerberos/authentication/package-summary.html)

[org.springframework.security.kerberos.authentication.sun](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/kerberos/authentication/sun/package-summary.html)

[org.springframework.security.kerberos.client](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/kerberos/client/package-summary.html)

[org.springframework.security.kerberos.client.config](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/kerberos/client/config/package-summary.html)

[org.springframework.security.kerberos.client.ldap](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/kerberos/client/ldap/package-summary.html)

[org.springframework.security.kerberos.test](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/kerberos/test/package-summary.html)

[org.springframework.security.kerberos.web.authentication](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/kerberos/web/authentication/package-summary.html)

[org.springframework.security.ldap](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/ldap/package-summary.html)

Spring Security's LDAP module.

[org.springframework.security.ldap.authentication](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/ldap/authentication/package-summary.html)

The LDAP authentication provider package.

[org.springframework.security.ldap.authentication.ad](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/ldap/authentication/ad/package-summary.html)

[org.springframework.security.ldap.jackson](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/ldap/jackson/package-summary.html)

Jackson 3+ serialization support for LDAP.

[org.springframework.security.ldap.jackson2](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/ldap/jackson2/package-summary.html)

Jackson 2 serialization support for LDAP.

[org.springframework.security.ldap.ppolicy](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/ldap/ppolicy/package-summary.html)

Implementation of password policy functionality based on the [Password Policy for LDAP Directories](https://tools.ietf.org/draft/draft-behera-ldap-password-policy/draft-behera-ldap-password-policy-09.txt).

[org.springframework.security.ldap.search](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/ldap/search/package-summary.html)

`LdapUserSearch` implementations.

[org.springframework.security.ldap.server](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/ldap/server/package-summary.html)

Embedded UnboundID Server implementation, as used by the configuration namespace.

[org.springframework.security.ldap.userdetails](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/ldap/userdetails/package-summary.html)

LDAP-focused `UserDetails` implementations which map from a ubset of the data contained in some of the standard LDAP types (such as `InetOrgPerson`).

[org.springframework.security.messaging.access.expression](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/messaging/access/expression/package-summary.html)

Security expression support for `Message`.

[org.springframework.security.messaging.access.intercept](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/messaging/access/intercept/package-summary.html)

Authorization support for `Message`.

[org.springframework.security.messaging.context](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/messaging/context/package-summary.html)

Support for establishing the [`SecurityContext`](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/core/context/SecurityContext.html "interface in org.springframework.security.core.context") within messaging.

[org.springframework.security.messaging.handler.invocation.reactive](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/messaging/handler/invocation/reactive/package-summary.html)

Reactive support for resolving security related arguments.

[org.springframework.security.messaging.util.matcher](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/messaging/util/matcher/package-summary.html)

Support for matching messages.

[org.springframework.security.messaging.web.csrf](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/messaging/web/csrf/package-summary.html)

Support CSRF protection in messages.

[org.springframework.security.messaging.web.socket.server](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/messaging/web/socket/server/package-summary.html)

Reactive Security CSRF protection.

[org.springframework.security.oauth2.client](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/oauth2/client/package-summary.html)

Core classes and interfaces providing support for OAuth 2.0 Client.

[org.springframework.security.oauth2.client.annotation](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/oauth2/client/annotation/package-summary.html)

[org.springframework.security.oauth2.client.authentication](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/oauth2/client/authentication/package-summary.html)

Support classes and interfaces for authenticating and authorizing a client with an OAuth 2.0 Authorization Server using a specific authorization grant flow.

[org.springframework.security.oauth2.client.endpoint](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/oauth2/client/endpoint/package-summary.html)

Classes and interfaces providing support to the client for initiating requests to the Authorization Server's Protocol Endpoints.

[org.springframework.security.oauth2.client.event](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/oauth2/client/event/package-summary.html)

[org.springframework.security.oauth2.client.http](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/oauth2/client/http/package-summary.html)

[org.springframework.security.oauth2.client.jackson](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/oauth2/client/jackson/package-summary.html)

Jackson 3+ serialization support for OAuth2 client.

[org.springframework.security.oauth2.client.jackson2](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/oauth2/client/jackson2/package-summary.html)

Jackson 2 serialization support for OAuth2 client.

[org.springframework.security.oauth2.client.oidc.authentication](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/oauth2/client/oidc/authentication/package-summary.html)

Support classes and interfaces for authenticating and authorizing a client with an OpenID Connect 1.0 Provider using a specific authorization grant flow.

[org.springframework.security.oauth2.client.oidc.authentication.event](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/oauth2/client/oidc/authentication/event/package-summary.html)

[org.springframework.security.oauth2.client.oidc.authentication.logout](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/oauth2/client/oidc/authentication/logout/package-summary.html)

[org.springframework.security.oauth2.client.oidc.server.session](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/oauth2/client/oidc/server/session/package-summary.html)

[org.springframework.security.oauth2.client.oidc.session](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/oauth2/client/oidc/session/package-summary.html)

[org.springframework.security.oauth2.client.oidc.userinfo](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/oauth2/client/oidc/userinfo/package-summary.html)

Classes and interfaces providing support to the client for initiating requests to the OpenID Connect 1.0 Provider's UserInfo Endpoint.

[org.springframework.security.oauth2.client.oidc.web.logout](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/oauth2/client/oidc/web/logout/package-summary.html)

[org.springframework.security.oauth2.client.oidc.web.server.logout](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/oauth2/client/oidc/web/server/logout/package-summary.html)

[org.springframework.security.oauth2.client.registration](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/oauth2/client/registration/package-summary.html)

Classes and interfaces that provide support for [`ClientRegistration`](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/oauth2/client/registration/ClientRegistration.html "class in org.springframework.security.oauth2.client.registration").

[org.springframework.security.oauth2.client.userinfo](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/oauth2/client/userinfo/package-summary.html)

Classes and interfaces providing support to the client for initiating requests to the OAuth 2.0 Authorization Server's UserInfo Endpoint.

[org.springframework.security.oauth2.client.web](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/oauth2/client/web/package-summary.html)

OAuth 2.0 Client `Filter`'s and supporting classes and interfaces.

[org.springframework.security.oauth2.client.web.client](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/oauth2/client/web/client/package-summary.html)

[org.springframework.security.oauth2.client.web.client.support](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/oauth2/client/web/client/support/package-summary.html)

[org.springframework.security.oauth2.client.web.method.annotation](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/oauth2/client/web/method/annotation/package-summary.html)

[org.springframework.security.oauth2.client.web.reactive.function.client](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/oauth2/client/web/reactive/function/client/package-summary.html)

[org.springframework.security.oauth2.client.web.reactive.function.client.support](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/oauth2/client/web/reactive/function/client/support/package-summary.html)

[org.springframework.security.oauth2.client.web.reactive.result.method.annotation](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/oauth2/client/web/reactive/result/method/annotation/package-summary.html)

[org.springframework.security.oauth2.client.web.server](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/oauth2/client/web/server/package-summary.html)

[org.springframework.security.oauth2.client.web.server.authentication](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/oauth2/client/web/server/authentication/package-summary.html)

[org.springframework.security.oauth2.core](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/oauth2/core/package-summary.html)

Core classes and interfaces providing support for the OAuth 2.0 Authorization Framework.

[org.springframework.security.oauth2.core.authorization](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/oauth2/core/authorization/package-summary.html)

[org.springframework.security.oauth2.core.converter](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/oauth2/core/converter/package-summary.html)

[org.springframework.security.oauth2.core.endpoint](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/oauth2/core/endpoint/package-summary.html)

Support classes that model the OAuth 2.0 Request and Response messages from the Authorization Endpoint and Token Endpoint.

[org.springframework.security.oauth2.core.http.converter](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/oauth2/core/http/converter/package-summary.html)

[org.springframework.security.oauth2.core.oidc](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/oauth2/core/oidc/package-summary.html)

Core classes and interfaces providing support for OpenID Connect Core 1.0.

[org.springframework.security.oauth2.core.oidc.endpoint](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/oauth2/core/oidc/endpoint/package-summary.html)

Support classes that model the OpenID Connect Core 1.0 Request and Response messages from the Authorization Endpoint and Token Endpoint.

[org.springframework.security.oauth2.core.oidc.user](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/oauth2/core/oidc/user/package-summary.html)

Provides a model for an OpenID Connect Core 1.0 representation of a user `Principal`.

[org.springframework.security.oauth2.core.user](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/oauth2/core/user/package-summary.html)

Provides a model for an OAuth 2.0 representation of a user `Principal`.

[org.springframework.security.oauth2.core.web.reactive.function](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/oauth2/core/web/reactive/function/package-summary.html)

[org.springframework.security.oauth2.jose](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/oauth2/jose/package-summary.html)

[org.springframework.security.oauth2.jose.jws](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/oauth2/jose/jws/package-summary.html)

Core classes and interfaces providing support for JSON Web Signature (JWS).

[org.springframework.security.oauth2.jwt](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/oauth2/jwt/package-summary.html)

Core classes and interfaces providing support for JSON Web Token (JWT).

[org.springframework.security.oauth2.server.authorization](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/oauth2/server/authorization/package-summary.html)

[org.springframework.security.oauth2.server.authorization.authentication](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/oauth2/server/authorization/authentication/package-summary.html)

[org.springframework.security.oauth2.server.authorization.client](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/oauth2/server/authorization/client/package-summary.html)

[org.springframework.security.oauth2.server.authorization.context](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/oauth2/server/authorization/context/package-summary.html)

[org.springframework.security.oauth2.server.authorization.converter](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/oauth2/server/authorization/converter/package-summary.html)

[org.springframework.security.oauth2.server.authorization.http.converter](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/oauth2/server/authorization/http/converter/package-summary.html)

[org.springframework.security.oauth2.server.authorization.jackson](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/oauth2/server/authorization/jackson/package-summary.html)

[org.springframework.security.oauth2.server.authorization.jackson2](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/oauth2/server/authorization/jackson2/package-summary.html)

[org.springframework.security.oauth2.server.authorization.oidc](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/oauth2/server/authorization/oidc/package-summary.html)

[org.springframework.security.oauth2.server.authorization.oidc.authentication](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/oauth2/server/authorization/oidc/authentication/package-summary.html)

[org.springframework.security.oauth2.server.authorization.oidc.converter](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/oauth2/server/authorization/oidc/converter/package-summary.html)

[org.springframework.security.oauth2.server.authorization.oidc.http.converter](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/oauth2/server/authorization/oidc/http/converter/package-summary.html)

[org.springframework.security.oauth2.server.authorization.oidc.web](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/oauth2/server/authorization/oidc/web/package-summary.html)

[org.springframework.security.oauth2.server.authorization.oidc.web.authentication](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/oauth2/server/authorization/oidc/web/authentication/package-summary.html)

[org.springframework.security.oauth2.server.authorization.settings](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/oauth2/server/authorization/settings/package-summary.html)

[org.springframework.security.oauth2.server.authorization.token](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/oauth2/server/authorization/token/package-summary.html)

[org.springframework.security.oauth2.server.authorization.web](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/oauth2/server/authorization/web/package-summary.html)

[org.springframework.security.oauth2.server.authorization.web.authentication](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/oauth2/server/authorization/web/authentication/package-summary.html)

[org.springframework.security.oauth2.server.resource](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/oauth2/server/resource/package-summary.html)

OAuth 2.0 Resource Server core classes and interfaces providing support.

[org.springframework.security.oauth2.server.resource.authentication](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/oauth2/server/resource/authentication/package-summary.html)

OAuth 2.0 Resource Server `Authentication`s and supporting classes and interfaces.

[org.springframework.security.oauth2.server.resource.introspection](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/oauth2/server/resource/introspection/package-summary.html)

OAuth 2.0 Introspection supporting classes and interfaces.

[org.springframework.security.oauth2.server.resource.web](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/oauth2/server/resource/web/package-summary.html)

OAuth 2.0 Resource Server `Filter`'s and supporting classes and interfaces.

[org.springframework.security.oauth2.server.resource.web.access](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/oauth2/server/resource/web/access/package-summary.html)

OAuth 2.0 Resource Server access denial classes and interfaces.

[org.springframework.security.oauth2.server.resource.web.access.server](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/oauth2/server/resource/web/access/server/package-summary.html)

[org.springframework.security.oauth2.server.resource.web.authentication](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/oauth2/server/resource/web/authentication/package-summary.html)

[org.springframework.security.oauth2.server.resource.web.reactive.function.client](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/oauth2/server/resource/web/reactive/function/client/package-summary.html)

[org.springframework.security.oauth2.server.resource.web.server](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/oauth2/server/resource/web/server/package-summary.html)

[org.springframework.security.oauth2.server.resource.web.server.authentication](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/oauth2/server/resource/web/server/authentication/package-summary.html)

[org.springframework.security.provisioning](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/provisioning/package-summary.html)

Contains simple user and authority group account provisioning interfaces together with a a JDBC-based implementation.

[org.springframework.security.rsocket.api](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/rsocket/api/package-summary.html)

Spring Security RSocket APIs.

[org.springframework.security.rsocket.authentication](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/rsocket/authentication/package-summary.html)

Spring Security RSocket Authentication integration.

[org.springframework.security.rsocket.authorization](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/rsocket/authorization/package-summary.html)

Spring Security RSocket authorization integration.

[org.springframework.security.rsocket.core](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/rsocket/core/package-summary.html)

Spring Security RSocket core integration.

[org.springframework.security.rsocket.metadata](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/rsocket/metadata/package-summary.html)

Spring Security RSocket metadata integration.

[org.springframework.security.rsocket.util.matcher](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/rsocket/util/matcher/package-summary.html)

Spring Security RSocket matching APIs.

[org.springframework.security.saml2](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/saml2/package-summary.html)

[org.springframework.security.saml2.core](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/saml2/core/package-summary.html)

[org.springframework.security.saml2.jackson](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/saml2/jackson/package-summary.html)

Jackson 3+ serialization support for SAML2.

[org.springframework.security.saml2.jackson2](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/saml2/jackson2/package-summary.html)

Jackson 2 serialization support for SAML2.

[org.springframework.security.saml2.provider.service.authentication](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/saml2/provider/service/authentication/package-summary.html)

[org.springframework.security.saml2.provider.service.authentication.logout](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/saml2/provider/service/authentication/logout/package-summary.html)

[org.springframework.security.saml2.provider.service.metadata](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/saml2/provider/service/metadata/package-summary.html)

[org.springframework.security.saml2.provider.service.registration](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/saml2/provider/service/registration/package-summary.html)

[org.springframework.security.saml2.provider.service.web](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/saml2/provider/service/web/package-summary.html)

[org.springframework.security.saml2.provider.service.web.authentication](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/saml2/provider/service/web/authentication/package-summary.html)

[org.springframework.security.saml2.provider.service.web.authentication.logout](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/saml2/provider/service/web/authentication/logout/package-summary.html)

[org.springframework.security.saml2.provider.service.web.metadata](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/saml2/provider/service/web/metadata/package-summary.html)

[org.springframework.security.scheduling](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/scheduling/package-summary.html)

[org.springframework.security.taglibs](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/taglibs/package-summary.html)

Security related tag libraries that can be used in JSPs and templates.

[org.springframework.security.taglibs.authz](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/taglibs/authz/package-summary.html)

JSP Security tag library implementation.

[org.springframework.security.taglibs.csrf](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/taglibs/csrf/package-summary.html)

JSP Security tag library integration with CSRF protection.

[org.springframework.security.task](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/task/package-summary.html)

[org.springframework.security.test.context](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/test/context/package-summary.html)

Spring Security support managing the [`SecurityContext`](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/core/context/SecurityContext.html "interface in org.springframework.security.core.context").

[org.springframework.security.test.context.annotation](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/test/context/annotation/package-summary.html)

Support for Framework's Test annotations.

[org.springframework.security.test.context.support](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/test/context/support/package-summary.html)

Spring Security support classes for the Spring TestContext Framework.

[org.springframework.security.test.web.reactive.server](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/test/web/reactive/server/package-summary.html)

Spring Security upport for testing Spring WebFlux server endpoints via WebTestClient.

[org.springframework.security.test.web.servlet.request](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/test/web/servlet/request/package-summary.html)

Spring Security built-in org.springframework.test.web.servlet.RequestBuilder implementations.

[org.springframework.security.test.web.servlet.response](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/test/web/servlet/response/package-summary.html)

Spring Security server-side support for testing Spring MVC applications.

[org.springframework.security.test.web.servlet.setup](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/test/web/servlet/setup/package-summary.html)

Spring Security built-in MockMvcBuilder implementations.

[org.springframework.security.test.web.support](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/test/web/support/package-summary.html)

Spring Security supporting the org.springframework.web.context package, such as WebApplicationContext implementations and various utility classes.

[org.springframework.security.util](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/util/package-summary.html)

General utility classes used throughout the Spring Security framework.

[org.springframework.security.web](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/package-summary.html)

Spring Security's web security module.

[org.springframework.security.web.access](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/access/package-summary.html)

Access-control related classes and packages.

[org.springframework.security.web.access.channel](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/access/channel/package-summary.html)

Classes that ensure web requests are received over required transport channels.

[org.springframework.security.web.access.expression](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/access/expression/package-summary.html)

Implementation of web security expressions.

[org.springframework.security.web.access.intercept](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/access/intercept/package-summary.html)

Enforcement of security for HTTP requests, typically by the URL requested.

[org.springframework.security.web.authentication](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/authentication/package-summary.html)

Authentication processing mechanisms, which respond to the submission of authentication credentials using various protocols (eg BASIC, CAS, form login etc).

[org.springframework.security.web.authentication.logout](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/authentication/logout/package-summary.html)

Logout functionality based around a filter which handles a specific logout URL.

[org.springframework.security.web.authentication.ott](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/authentication/ott/package-summary.html)

Package for One Time Token usage.

[org.springframework.security.web.authentication.password](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/authentication/password/package-summary.html)

Classes for Password APIs.

[org.springframework.security.web.authentication.preauth](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/authentication/preauth/package-summary.html)

Support for "pre-authenticated" scenarios, where Spring Security assumes the incoming request has already been authenticated by some externally configured system.

[org.springframework.security.web.authentication.preauth.j2ee](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/authentication/preauth/j2ee/package-summary.html)

Pre-authentication support for container-authenticated requests.

[org.springframework.security.web.authentication.preauth.websphere](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/authentication/preauth/websphere/package-summary.html)

Websphere-specific pre-authentication classes.

[org.springframework.security.web.authentication.preauth.x509](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/authentication/preauth/x509/package-summary.html)

X.509 client certificate authentication support.

[org.springframework.security.web.authentication.rememberme](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/authentication/rememberme/package-summary.html)

Support for remembering a user between different web sessions.

[org.springframework.security.web.authentication.session](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/authentication/session/package-summary.html)

Strategy interface and implementations for handling session-related behaviour for a newly authenticated user.

[org.springframework.security.web.authentication.switchuser](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/authentication/switchuser/package-summary.html)

Provides HTTP-based "switch user" (su) capabilities.

[org.springframework.security.web.authentication.ui](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/authentication/ui/package-summary.html)

Authentication user-interface rendering code.

[org.springframework.security.web.authentication.www](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/authentication/www/package-summary.html)

WWW-Authenticate based authentication mechanism implementations: Basic and Digest authentication.

[org.springframework.security.web.bind.annotation](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/bind/annotation/package-summary.html)

Annotations for binding web security APIs.

[org.springframework.security.web.bind.support](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/bind/support/package-summary.html)

Support for binding web security APIs.

[org.springframework.security.web.context](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/context/package-summary.html)

Classes which are responsible for maintaining the security context between HTTP requests.

[org.springframework.security.web.context.request.async](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/context/request/async/package-summary.html)

Async request context APIs.

[org.springframework.security.web.context.support](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/context/support/package-summary.html)

Async support for request context.

[org.springframework.security.web.csrf](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/csrf/package-summary.html)

APIs for protection against CSRF attacks.

[org.springframework.security.web.debug](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/debug/package-summary.html)

APIs for debugging web security.

[org.springframework.security.web.firewall](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/firewall/package-summary.html)

APIs for web security firewall support.

[org.springframework.security.web.header](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/header/package-summary.html)

APIs for writing security HTTP Headers.

[org.springframework.security.web.header.writers](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/header/writers/package-summary.html)

APIs for writing security HTTP Headers.

[org.springframework.security.web.header.writers.frameoptions](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/header/writers/frameoptions/package-summary.html)

APIs for writing security HTTP Headers related to frame options.

[org.springframework.security.web.http](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/http/package-summary.html)

HTTP based security APIs.

[org.springframework.security.web.jaasapi](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/jaasapi/package-summary.html)

Makes a JAAS Subject available as the current Subject.

[org.springframework.security.web.jackson](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/jackson/package-summary.html)

Jackson 3+ serialization support for web.

[org.springframework.security.web.jackson2](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/jackson2/package-summary.html)

Jackson 2 serialization support for web.

[org.springframework.security.web.method.annotation](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/method/annotation/package-summary.html)

Support for Spring Framework's handler method processing.

[org.springframework.security.web.reactive.result.method.annotation](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/reactive/result/method/annotation/package-summary.html)

Support for Spring Framework's reactive handler method processing.

[org.springframework.security.web.reactive.result.view](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/reactive/result/view/package-summary.html)

Support for Spring Framework's reactive view processing.

[org.springframework.security.web.savedrequest](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/savedrequest/package-summary.html)

Classes related to the caching of an `HttpServletRequest` which requires authentication.

[org.springframework.security.web.server](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/server/package-summary.html)

WebFlux Spring Security support.

[org.springframework.security.web.server.authentication](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/server/authentication/package-summary.html)

Reactive web Authorization APIs.

[org.springframework.security.web.server.authentication.logout](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/server/authentication/logout/package-summary.html)

Reactive logout APIs.

[org.springframework.security.web.server.authentication.ott](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/server/authentication/ott/package-summary.html)

Reactive OTT APIs.

[org.springframework.security.web.server.authorization](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/server/authorization/package-summary.html)

Reactive web OTT APIs.

[org.springframework.security.web.server.context](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/server/context/package-summary.html)

Reactive web context APIs.

[org.springframework.security.web.server.csrf](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/server/csrf/package-summary.html)

Reactive APIs for protecting against CSRF attacks.

[org.springframework.security.web.server.firewall](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/server/firewall/package-summary.html)

Reactive HTTP Firewall APIs.

[org.springframework.security.web.server.header](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/server/header/package-summary.html)

Reactive APIs for adding HTTP Header based security.

[org.springframework.security.web.server.jackson](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/server/jackson/package-summary.html)

Jackson 3+ serialization support for reactive web server.

[org.springframework.security.web.server.jackson2](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/server/jackson2/package-summary.html)

Jackson 2 serialization support for reactive web server.

[org.springframework.security.web.server.savedrequest](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/server/savedrequest/package-summary.html)

Reactive support for saving requests (to replay them after interrupted by security workflows like authentication).

[org.springframework.security.web.server.transport](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/server/transport/package-summary.html)

WebFlux based transport security.

[org.springframework.security.web.server.ui](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/server/ui/package-summary.html)

Support for rendering UIs (e.g.

[org.springframework.security.web.server.util.matcher](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/server/util/matcher/package-summary.html)

Reactive APIs for matching requests which are used for, among other things, mapping authorization rules.

[org.springframework.security.web.servlet.support.csrf](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/servlet/support/csrf/package-summary.html)

CSRF support classes for Spring's web MVC framework.

[org.springframework.security.web.servlet.util.matcher](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/servlet/util/matcher/package-summary.html)

Integration with Spring Framework's support for matching HTTP request paths.

[org.springframework.security.web.servletapi](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/servletapi/package-summary.html)

Populates a Servlet request with a new Spring Security compliant `HttpServletRequestWrapper`.

[org.springframework.security.web.session](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/session/package-summary.html)

Session management filters, `HttpSession` events and publisher classes.

[org.springframework.security.web.transport](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/transport/package-summary.html)

Spring Security HTTP transport support.

[org.springframework.security.web.util](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/util/package-summary.html)

Web utility classes.

[org.springframework.security.web.util.matcher](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/util/matcher/package-summary.html)

Servlet APIs for matching requests which are used for, among other things, mapping authorization rules.

[org.springframework.security.web.webauthn.api](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/webauthn/api/package-summary.html)

WebAuthn APIs.

[org.springframework.security.web.webauthn.authentication](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/webauthn/authentication/package-summary.html)

WebAuthn Authentication support.

[org.springframework.security.web.webauthn.jackson](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/webauthn/jackson/package-summary.html)

WebAuthn Jackson Support.

[org.springframework.security.web.webauthn.management](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/webauthn/management/package-summary.html)

Management of the WebAuthn APIs.

[org.springframework.security.web.webauthn.registration](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/webauthn/registration/package-summary.html)

WebAuthn Registration support.

Cookies
-------

Broadcom and third-party partners use technology, including cookies to, among other things, analyze site usage, improve your experience and help us advertise. By using our site, you agree to our use of cookies as described in our [Cookie Notice](https://www.broadcom.com/company/legal/cookie-policy)

Allow All

Required Only

Cookies Settings

![Image 1: Company Logo](https://cdn.cookielaw.org/logos/8153b982-ae11-46a0-b7c2-6e4e3b591d72/8a37f712-8eb0-4967-9ca7-343409702cfa/5228da75-715f-4d1a-9262-2662775eb1ce/Broadcom_Logo_Red-Black_no-tag.png)

Privacy Preference Center
-------------------------

Privacy Preference Center
-------------------------

*   ### Your Privacy 
*   ### Strictly Necessary Cookies 
*   ### Performance Cookies 
*   ### Targeting Cookies 

#### Your Privacy

When you interact with Broadcom as set forth in the Privacy Policy through visiting any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. 

[Cookie Policy](https://www.broadcom.com/company/legal/privacy/cookie-policy)[Privacy Policy](https://www.broadcom.com/company/legal/privacy/policy)

#### Strictly Necessary Cookies

Always Active

These cookies are necessary for the website to function and cannot be switched off in Broadcom’s systems. They are usually only set in response to actions made by you which amount to a request for services, such as setting your privacy preferences, logging in or filling in forms. You can set your browser to block or alert you about these cookies, but some parts of the site will not then work. These cookies do not store any personally identifiable information.

#### Performance Cookies

- [x] Performance Cookies 

These cookies allow Broadcom to count visits and traffic sources so Broadcom can measure and improve the performance of its site. They help Broadcom to know which pages are the most and least popular and see how visitors move around the site. All information these cookies collect is aggregated and therefore anonymous. If you do not allow these cookies Broadcom will not know when you have visited our site and will not be able to monitor its performance.

#### Targeting Cookies

- [x] Targeting Cookies 

These cookies may be set through Broadcom’s site by its advertising partners. They may be used by those companies to build a profile of your interests and show you relevant adverts on other sites. They do not store directly personal information, but are based on uniquely identifying your browser and internet device. If you do not allow these cookies, you will experience less targeted advertising.

### Cookie List

Consent Leg.Interest

- [x] checkbox label label

- [x] checkbox label label

- [x] checkbox label label

Clear

*   - [x] checkbox label label 

Apply Cancel

Confirm My Choices

Required Only Allow All

[![Image 2: Powered by Onetrust](https://cdn.cookielaw.org/logos/static/powered_by_logo.svg)](https://www.onetrust.com/products/cookie-consent/)
