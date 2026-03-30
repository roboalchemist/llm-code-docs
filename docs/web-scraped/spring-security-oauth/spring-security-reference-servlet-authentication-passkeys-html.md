# Source: https://docs.spring.io/spring-security/reference/servlet/authentication/passkeys.html

Title: Passkeys :: Spring Security

URL Source: https://docs.spring.io/spring-security/reference/servlet/authentication/passkeys.html

Markdown Content:
Passkeys :: Spring Security
===============

[![Image 1: Spring](https://docs.spring.io/spring-security/reference/_/img/spring-logo.svg)](https://spring.io/)

[Why Spring](https://docs.spring.io/spring-security/reference/servlet/authentication/passkeys.html#)

[Overview](https://spring.io/why-spring)[Microservices](https://spring.io/microservices)[Reactive](https://spring.io/reactive)[Event Driven](https://spring.io/event-driven)[Cloud](https://spring.io/cloud)[Web Applications](https://spring.io/web-applications)[Serverless](https://spring.io/serverless)[Batch](https://spring.io/batch)

[Learn](https://docs.spring.io/spring-security/reference/servlet/authentication/passkeys.html#)

[Overview](https://spring.io/learn)[Quickstart](https://spring.io/quickstart)[Guides](https://spring.io/guides)[Blog](https://spring.io/blog)

[Projects](https://docs.spring.io/spring-security/reference/servlet/authentication/passkeys.html#)

[Overview](https://spring.io/projects)[Spring Boot](https://spring.io/projects/spring-boot)[Spring Framework](https://spring.io/projects/spring-framework)[Spring Cloud](https://spring.io/projects/spring-cloud)[Spring Cloud Data Flow](https://spring.io/projects/spring-cloud-dataflow)[Spring Data](https://spring.io/projects/spring-data)[Spring Integration](https://spring.io/projects/spring-integration)[Spring Batch](https://spring.io/projects/spring-batch)[Spring Security](https://spring.io/projects/spring-security)[View all projects](https://spring.io/projects)*   DEVELOPMENT TOOLS
[Spring Tools 4](https://spring.io/tools)[Spring Initializr](https://start.spring.io/)

[Academy](https://docs.spring.io/spring-security/reference/servlet/authentication/passkeys.html#)

[Courses](https://spring.academy/courses)[Get Certified](https://spring.academy/learning-path)

[Solutions](https://docs.spring.io/spring-security/reference/servlet/authentication/passkeys.html#)

[Overview](https://spring.io/solutions)[Spring Runtime](https://spring.io/support)[Spring Consulting](https://spring.io/consulting)[Spring Academy For Teams](https://spring.academy/teams)[Security Advisories](https://spring.io/security)

[Community](https://docs.spring.io/spring-security/reference/servlet/authentication/passkeys.html#)

[Overview](https://spring.io/community)[Events](https://spring.io/events)[Team](https://spring.io/team)

- [x] light 

Spring Security 7.0.3

Search CTRL + k

*       *   [Overview](https://docs.spring.io/spring-security/reference/index.html)
    *   [Prerequisites](https://docs.spring.io/spring-security/reference/prerequisites.html)
    *   [Community](https://docs.spring.io/spring-security/reference/community.html)
    *   [What’s New](https://docs.spring.io/spring-security/reference/whats-new.html)
    *   [Preparing for 8.0](https://docs.spring.io/spring-security/reference/migration-8/index.html)
    *   [Migrating to 7](https://docs.spring.io/spring-security/reference/migration/index.html)
        *   [Servlet](https://docs.spring.io/spring-security/reference/migration/servlet/index.html)
            *   [Authorization](https://docs.spring.io/spring-security/reference/migration/servlet/authorization.html)
            *   [OAuth 2.0](https://docs.spring.io/spring-security/reference/migration/servlet/oauth2.html)
            *   [SAML 2.0](https://docs.spring.io/spring-security/reference/migration/servlet/saml2.html)

        *   [Reactive](https://docs.spring.io/spring-security/reference/migration/reactive.html)

    *   [Getting Spring Security](https://docs.spring.io/spring-security/reference/getting-spring-security.html)
    *   [Javadoc](https://docs.spring.io/spring-security/reference/api/java/index.html)
    *   [Features](https://docs.spring.io/spring-security/reference/features/index.html)
        *   [Authentication](https://docs.spring.io/spring-security/reference/features/authentication/index.html)
            *   [Password Storage](https://docs.spring.io/spring-security/reference/features/authentication/password-storage.html)

        *   [Authorization](https://docs.spring.io/spring-security/reference/features/authorization/index.html)
        *   [Protection Against Exploits](https://docs.spring.io/spring-security/reference/features/exploits/index.html)
            *   [CSRF](https://docs.spring.io/spring-security/reference/features/exploits/csrf.html)
            *   [HTTP Headers](https://docs.spring.io/spring-security/reference/features/exploits/headers.html)
            *   [HTTP Requests](https://docs.spring.io/spring-security/reference/features/exploits/http.html)

        *   [Integrations](https://docs.spring.io/spring-security/reference/features/integrations/index.html)
            *   REST Client
                *   [HTTP Service Clients](https://docs.spring.io/spring-security/reference/features/integrations/rest/http-service-client.html)

            *   [Cryptography](https://docs.spring.io/spring-security/reference/features/integrations/cryptography.html)
            *   [Spring Data](https://docs.spring.io/spring-security/reference/features/integrations/data.html)
            *   [Java’s Concurrency APIs](https://docs.spring.io/spring-security/reference/features/integrations/concurrency.html)
            *   [Jackson](https://docs.spring.io/spring-security/reference/features/integrations/jackson.html)
            *   [Localization](https://docs.spring.io/spring-security/reference/features/integrations/localization.html)

    *   [Project Modules](https://docs.spring.io/spring-security/reference/modules.html)
    *   [Samples](https://docs.spring.io/spring-security/reference/samples.html)
    *   [Servlet Applications](https://docs.spring.io/spring-security/reference/servlet/index.html)
        *   [Getting Started](https://docs.spring.io/spring-security/reference/servlet/getting-started.html)
        *   [Architecture](https://docs.spring.io/spring-security/reference/servlet/architecture.html)
        *   [Authentication](https://docs.spring.io/spring-security/reference/servlet/authentication/index.html)
            *   [Authentication Architecture](https://docs.spring.io/spring-security/reference/servlet/authentication/architecture.html)
            *   [Username/Password](https://docs.spring.io/spring-security/reference/servlet/authentication/passwords/index.html)
                *   [Reading Username/Password](https://docs.spring.io/spring-security/reference/servlet/authentication/passwords/input.html)
                    *   [Form](https://docs.spring.io/spring-security/reference/servlet/authentication/passwords/form.html)
                    *   [Basic](https://docs.spring.io/spring-security/reference/servlet/authentication/passwords/basic.html)
                    *   [Digest](https://docs.spring.io/spring-security/reference/servlet/authentication/passwords/digest.html)

                *   [Password Storage](https://docs.spring.io/spring-security/reference/servlet/authentication/passwords/storage.html)
                    *   [In Memory](https://docs.spring.io/spring-security/reference/servlet/authentication/passwords/in-memory.html)
                    *   [JDBC](https://docs.spring.io/spring-security/reference/servlet/authentication/passwords/jdbc.html)
                    *   [UserDetails](https://docs.spring.io/spring-security/reference/servlet/authentication/passwords/user-details.html)
                    *   [CredentialsContainer](https://docs.spring.io/spring-security/reference/servlet/authentication/passwords/credentials-container.html)
                    *   [Password Erasure](https://docs.spring.io/spring-security/reference/servlet/authentication/passwords/erasure.html)
                    *   [UserDetailsService](https://docs.spring.io/spring-security/reference/servlet/authentication/passwords/user-details-service.html)
                    *   [PasswordEncoder](https://docs.spring.io/spring-security/reference/servlet/authentication/passwords/password-encoder.html)
                    *   [DaoAuthenticationProvider](https://docs.spring.io/spring-security/reference/servlet/authentication/passwords/dao-authentication-provider.html)
                    *   [LDAP](https://docs.spring.io/spring-security/reference/servlet/authentication/passwords/ldap.html)

            *   [Multi-Factor Authentication](https://docs.spring.io/spring-security/reference/servlet/authentication/mfa.html)
            *   [Persistence](https://docs.spring.io/spring-security/reference/servlet/authentication/persistence.html)
            *   [Passkeys](https://docs.spring.io/spring-security/reference/servlet/authentication/passkeys.html)
            *   [One-Time Token](https://docs.spring.io/spring-security/reference/servlet/authentication/onetimetoken.html)
            *   [Session Management](https://docs.spring.io/spring-security/reference/servlet/authentication/session-management.html)
            *   [Remember Me](https://docs.spring.io/spring-security/reference/servlet/authentication/rememberme.html)
            *   [Anonymous](https://docs.spring.io/spring-security/reference/servlet/authentication/anonymous.html)
            *   [Pre-Authentication](https://docs.spring.io/spring-security/reference/servlet/authentication/preauth.html)
            *   [JAAS](https://docs.spring.io/spring-security/reference/servlet/authentication/jaas.html)
            *   [CAS](https://docs.spring.io/spring-security/reference/servlet/authentication/cas.html)
            *   [X509](https://docs.spring.io/spring-security/reference/servlet/authentication/x509.html)
            *   [Run-As](https://docs.spring.io/spring-security/reference/servlet/authentication/runas.html)
            *   [Logout](https://docs.spring.io/spring-security/reference/servlet/authentication/logout.html)
            *   [Authentication Events](https://docs.spring.io/spring-security/reference/servlet/authentication/events.html)

        *   [Kerberos](https://docs.spring.io/spring-security/reference/servlet/authentication/kerberos/index.html)
            *   [Introduction](https://docs.spring.io/spring-security/reference/servlet/authentication/kerberos/introduction.html)
            *   [Reference](https://docs.spring.io/spring-security/reference/servlet/authentication/kerberos/ssk.html)
            *   [Samples](https://docs.spring.io/spring-security/reference/servlet/authentication/kerberos/samples.html)
            *   [Appendices](https://docs.spring.io/spring-security/reference/servlet/authentication/kerberos/appendix.html)

        *   [Authorization](https://docs.spring.io/spring-security/reference/servlet/authorization/index.html)
            *   [Authorization Architecture](https://docs.spring.io/spring-security/reference/servlet/authorization/architecture.html)
            *   [Authorize HTTP Requests](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html)
            *   [Method Security](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html)
            *   [Domain Object Security ACLs](https://docs.spring.io/spring-security/reference/servlet/authorization/acls.html)
            *   [Authorization Events](https://docs.spring.io/spring-security/reference/servlet/authorization/events.html)

        *   [OAuth2](https://docs.spring.io/spring-security/reference/servlet/oauth2/index.html)
            *   [OAuth2 Log In](https://docs.spring.io/spring-security/reference/servlet/oauth2/login/index.html)
                *   [Core Configuration](https://docs.spring.io/spring-security/reference/servlet/oauth2/login/core.html)
                *   [Advanced Configuration](https://docs.spring.io/spring-security/reference/servlet/oauth2/login/advanced.html)
                *   [OIDC Logout](https://docs.spring.io/spring-security/reference/servlet/oauth2/login/logout.html)

            *   [OAuth2 Client](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/index.html)
                *   [Core Interfaces and Classes](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/core.html)
                *   [OAuth2 Authorization Grants](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorization-grants.html)
                *   [OAuth2 Client Authentication](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/client-authentication.html)
                *   [OAuth2 Authorized Clients](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorized-clients.html)

            *   [OAuth2 Resource Server](https://docs.spring.io/spring-security/reference/servlet/oauth2/resource-server/index.html)
                *   [JWT](https://docs.spring.io/spring-security/reference/servlet/oauth2/resource-server/jwt.html)
                *   [Opaque Token](https://docs.spring.io/spring-security/reference/servlet/oauth2/resource-server/opaque-token.html)
                *   [Multitenancy](https://docs.spring.io/spring-security/reference/servlet/oauth2/resource-server/multitenancy.html)
                *   [Bearer Tokens](https://docs.spring.io/spring-security/reference/servlet/oauth2/resource-server/bearer-tokens.html)
                *   [DPoP-bound Access Tokens](https://docs.spring.io/spring-security/reference/servlet/oauth2/resource-server/dpop-tokens.html)
                *   [Protected Resource Metadata](https://docs.spring.io/spring-security/reference/servlet/oauth2/resource-server/protected-resource-metadata.html)

            *   [OAuth2 Authorization Server](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/index.html)
                *   [Getting Started](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/getting-started.html)
                *   [Configuration Model](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/configuration-model.html)
                *   [Core Model / Components](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/core-model-components.html)
                *   [Protocol Endpoints](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/protocol-endpoints.html)

        *   [SAML2](https://docs.spring.io/spring-security/reference/servlet/saml2/index.html)
            *   [SAML2 Log In](https://docs.spring.io/spring-security/reference/servlet/saml2/login/index.html)
                *   [SAML2 Log In Overview](https://docs.spring.io/spring-security/reference/servlet/saml2/login/overview.html)
                *   [SAML2 Authentication Requests](https://docs.spring.io/spring-security/reference/servlet/saml2/login/authentication-requests.html)
                *   [SAML2 Authentication Responses](https://docs.spring.io/spring-security/reference/servlet/saml2/login/authentication.html)

            *   [SAML2 Logout](https://docs.spring.io/spring-security/reference/servlet/saml2/logout.html)
            *   [SAML2 Metadata](https://docs.spring.io/spring-security/reference/servlet/saml2/metadata.html)
            *   [Migrating from Spring Security SAML Extension](https://docs.spring.io/spring-security/reference/servlet/saml2/saml-extension-migration.html)

        *   [Protection Against Exploits](https://docs.spring.io/spring-security/reference/servlet/exploits/index.html)
            *   [Cross Site Request Forgery (CSRF)](https://docs.spring.io/spring-security/reference/servlet/exploits/csrf.html)
            *   [Security HTTP Response Headers](https://docs.spring.io/spring-security/reference/servlet/exploits/headers.html)
            *   [HTTP](https://docs.spring.io/spring-security/reference/servlet/exploits/http.html)
            *   [HttpFirewall](https://docs.spring.io/spring-security/reference/servlet/exploits/firewall.html)

        *   [Integrations](https://docs.spring.io/spring-security/reference/servlet/integrations/index.html)
            *   [Concurrency](https://docs.spring.io/spring-security/reference/servlet/integrations/concurrency.html)
            *   [Localization](https://docs.spring.io/spring-security/reference/servlet/integrations/localization.html)
            *   [Servlet APIs](https://docs.spring.io/spring-security/reference/servlet/integrations/servlet-api.html)
            *   [Spring Data](https://docs.spring.io/spring-security/reference/servlet/integrations/data.html)
            *   [Spring MVC](https://docs.spring.io/spring-security/reference/servlet/integrations/mvc.html)
            *   [WebSocket](https://docs.spring.io/spring-security/reference/servlet/integrations/websocket.html)
            *   [Spring’s CORS Support](https://docs.spring.io/spring-security/reference/servlet/integrations/cors.html)
            *   [JSP Taglib](https://docs.spring.io/spring-security/reference/servlet/integrations/jsp-taglibs.html)
            *   [Observability](https://docs.spring.io/spring-security/reference/servlet/integrations/observability.html)

        *   Configuration
            *   [Java Configuration](https://docs.spring.io/spring-security/reference/servlet/configuration/java.html)
            *   [Kotlin Configuration](https://docs.spring.io/spring-security/reference/servlet/configuration/kotlin.html)
            *   [Namespace Configuration](https://docs.spring.io/spring-security/reference/servlet/configuration/xml-namespace.html)

        *   [Testing](https://docs.spring.io/spring-security/reference/servlet/test/index.html)
            *   [Method Security](https://docs.spring.io/spring-security/reference/servlet/test/method.html)
            *   [MockMvc Support](https://docs.spring.io/spring-security/reference/servlet/test/mockmvc/index.html)
            *   [MockMvc Setup](https://docs.spring.io/spring-security/reference/servlet/test/mockmvc/setup.html)
            *   [Security RequestPostProcessors](https://docs.spring.io/spring-security/reference/servlet/test/mockmvc/request-post-processors.html)
                *   [Mocking Users](https://docs.spring.io/spring-security/reference/servlet/test/mockmvc/authentication.html)
                *   [Mocking CSRF](https://docs.spring.io/spring-security/reference/servlet/test/mockmvc/csrf.html)
                *   [Mocking Form Login](https://docs.spring.io/spring-security/reference/servlet/test/mockmvc/form-login.html)
                *   [Mocking HTTP Basic](https://docs.spring.io/spring-security/reference/servlet/test/mockmvc/http-basic.html)
                *   [Mocking OAuth2](https://docs.spring.io/spring-security/reference/servlet/test/mockmvc/oauth2.html)
                *   [Mocking Logout](https://docs.spring.io/spring-security/reference/servlet/test/mockmvc/logout.html)

            *   [Security RequestBuilders](https://docs.spring.io/spring-security/reference/servlet/test/mockmvc/request-builders.html)
            *   [Security ResultMatchers](https://docs.spring.io/spring-security/reference/servlet/test/mockmvc/result-matchers.html)
            *   [Security ResultHandlers](https://docs.spring.io/spring-security/reference/servlet/test/mockmvc/result-handlers.html)

        *   [Appendix](https://docs.spring.io/spring-security/reference/servlet/appendix/index.html)
            *   [Database Schemas](https://docs.spring.io/spring-security/reference/servlet/appendix/database-schema.html)
            *   [XML Namespace](https://docs.spring.io/spring-security/reference/servlet/appendix/namespace/index.html)
                *   [Authentication Services](https://docs.spring.io/spring-security/reference/servlet/appendix/namespace/authentication-manager.html)
                *   [Web Security](https://docs.spring.io/spring-security/reference/servlet/appendix/namespace/http.html)
                *   [Method Security](https://docs.spring.io/spring-security/reference/servlet/appendix/namespace/method-security.html)
                *   [LDAP Security](https://docs.spring.io/spring-security/reference/servlet/appendix/namespace/ldap.html)
                *   [WebSocket Security](https://docs.spring.io/spring-security/reference/servlet/appendix/namespace/websocket.html)

            *   [Proxy Server Configuration](https://docs.spring.io/spring-security/reference/servlet/appendix/proxy-server.html)
            *   [FAQ](https://docs.spring.io/spring-security/reference/servlet/appendix/faq.html)

    *   [Reactive Applications](https://docs.spring.io/spring-security/reference/reactive/index.html)
        *   [Getting Started](https://docs.spring.io/spring-security/reference/reactive/getting-started.html)
        *   [Authentication](https://docs.spring.io/spring-security/reference/reactive/authentication/index.html)
            *   [X.509 Authentication](https://docs.spring.io/spring-security/reference/reactive/authentication/x509.html)
            *   [Logout](https://docs.spring.io/spring-security/reference/reactive/authentication/logout.html)
            *   Session Management
                *   [Concurrent Sessions Control](https://docs.spring.io/spring-security/reference/reactive/authentication/concurrent-sessions-control.html)

        *   Authorization
            *   [Authorize HTTP Requests](https://docs.spring.io/spring-security/reference/reactive/authorization/authorize-http-requests.html)
            *   [EnableReactiveMethodSecurity](https://docs.spring.io/spring-security/reference/reactive/authorization/method.html)

        *   [OAuth2](https://docs.spring.io/spring-security/reference/reactive/oauth2/index.html)
            *   [OAuth2 Log In](https://docs.spring.io/spring-security/reference/reactive/oauth2/login/index.html)
                *   [Core Configuration](https://docs.spring.io/spring-security/reference/reactive/oauth2/login/core.html)
                *   [Advanced Configuration](https://docs.spring.io/spring-security/reference/reactive/oauth2/login/advanced.html)
                *   [OIDC Logout](https://docs.spring.io/spring-security/reference/reactive/oauth2/login/logout.html)

            *   [OAuth2 Client](https://docs.spring.io/spring-security/reference/reactive/oauth2/client/index.html)
                *   [Core Interfaces and Classes](https://docs.spring.io/spring-security/reference/reactive/oauth2/client/core.html)
                *   [OAuth2 Authorization Grants](https://docs.spring.io/spring-security/reference/reactive/oauth2/client/authorization-grants.html)
                *   [OAuth2 Client Authentication](https://docs.spring.io/spring-security/reference/reactive/oauth2/client/client-authentication.html)
                *   [OAuth2 Authorized Clients](https://docs.spring.io/spring-security/reference/reactive/oauth2/client/authorized-clients.html)

            *   [OAuth2 Resource Server](https://docs.spring.io/spring-security/reference/reactive/oauth2/resource-server/index.html)
                *   [JWT](https://docs.spring.io/spring-security/reference/reactive/oauth2/resource-server/jwt.html)
                *   [Opaque Token](https://docs.spring.io/spring-security/reference/reactive/oauth2/resource-server/opaque-token.html)
                *   [Multitenancy](https://docs.spring.io/spring-security/reference/reactive/oauth2/resource-server/multitenancy.html)
                *   [Bearer Tokens](https://docs.spring.io/spring-security/reference/reactive/oauth2/resource-server/bearer-tokens.html)

        *   [Protection Against Exploits](https://docs.spring.io/spring-security/reference/reactive/exploits/index.html)
            *   [CSRF](https://docs.spring.io/spring-security/reference/reactive/exploits/csrf.html)
            *   [Headers](https://docs.spring.io/spring-security/reference/reactive/exploits/headers.html)
            *   [HTTP Requests](https://docs.spring.io/spring-security/reference/reactive/exploits/http.html)
            *   [ServerWebExchangeFirewall](https://docs.spring.io/spring-security/reference/reactive/exploits/firewall.html)

        *   Integrations
            *   [CORS](https://docs.spring.io/spring-security/reference/reactive/integrations/cors.html)
            *   [RSocket](https://docs.spring.io/spring-security/reference/reactive/integrations/rsocket.html)
            *   [Observability](https://docs.spring.io/spring-security/reference/reactive/integrations/observability.html)

        *   [Testing](https://docs.spring.io/spring-security/reference/reactive/test/index.html)
            *   [Testing Method Security](https://docs.spring.io/spring-security/reference/reactive/test/method.html)
            *   [Testing Web Security](https://docs.spring.io/spring-security/reference/reactive/test/web/index.html)
                *   [WebTestClient Setup](https://docs.spring.io/spring-security/reference/reactive/test/web/setup.html)
                *   [Testing Authentication](https://docs.spring.io/spring-security/reference/reactive/test/web/authentication.html)
                *   [Testing CSRF](https://docs.spring.io/spring-security/reference/reactive/test/web/csrf.html)
                *   [Testing OAuth 2.0](https://docs.spring.io/spring-security/reference/reactive/test/web/oauth2.html)
                *   [Testing X509](https://docs.spring.io/spring-security/reference/reactive/test/web/x509.html)

        *   [WebFlux Security](https://docs.spring.io/spring-security/reference/reactive/configuration/webflux.html)

    *   [GraalVM Native Image Support](https://docs.spring.io/spring-security/reference/native-image/index.html)
        *   [Method Security](https://docs.spring.io/spring-security/reference/native-image/method-security.html)

Search CTRL + k

### Passkeys

*   [Required Dependencies](https://docs.spring.io/spring-security/reference/servlet/authentication/passkeys.html#passkeys-dependencies)
*   [Configuration](https://docs.spring.io/spring-security/reference/servlet/authentication/passkeys.html#passkeys-configuration)
*   [JDBC & Custom Persistence](https://docs.spring.io/spring-security/reference/servlet/authentication/passkeys.html#passkeys-configuration-persistence)
*   [Custom PublicKeyCredentialCreationOptionsRepository](https://docs.spring.io/spring-security/reference/servlet/authentication/passkeys.html#passkeys-configuration-pkccor)
*   [Register a New Credential](https://docs.spring.io/spring-security/reference/servlet/authentication/passkeys.html#passkeys-register)
*   [Request the Registration Options](https://docs.spring.io/spring-security/reference/servlet/authentication/passkeys.html#passkeys-register-options)
*   [Registering the Credential](https://docs.spring.io/spring-security/reference/servlet/authentication/passkeys.html#passkeys-register-create)
*   [Verifying an Authentication Assertion](https://docs.spring.io/spring-security/reference/servlet/authentication/passkeys.html#passkeys-verify)
*   [Request the Verification Options](https://docs.spring.io/spring-security/reference/servlet/authentication/passkeys.html#passkeys-verify-options)
*   [Verifying the Credential](https://docs.spring.io/spring-security/reference/servlet/authentication/passkeys.html#passkeys-verify-get)

[Edit this Page](https://github.com/spring-projects/spring-security/blob/7.0.3/docs/modules/ROOT/pages/servlet/authentication/passkeys.adoc)[GitHub Project](https://github.com/spring-projects/spring-security "GitHub")[Stack Overflow](https://stackoverflow.com/tags/spring-security)

*   [Spring Security](https://docs.spring.io/spring-security/reference/index.html)
*   [Servlet Applications](https://docs.spring.io/spring-security/reference/servlet/index.html)
*   [Authentication](https://docs.spring.io/spring-security/reference/servlet/authentication/index.html)
*   [Passkeys](https://docs.spring.io/spring-security/reference/servlet/authentication/passkeys.html)

Passkeys
========

### Passkeys

*   [Required Dependencies](https://docs.spring.io/spring-security/reference/servlet/authentication/passkeys.html#passkeys-dependencies)
*   [Configuration](https://docs.spring.io/spring-security/reference/servlet/authentication/passkeys.html#passkeys-configuration)
*   [JDBC & Custom Persistence](https://docs.spring.io/spring-security/reference/servlet/authentication/passkeys.html#passkeys-configuration-persistence)
*   [Custom PublicKeyCredentialCreationOptionsRepository](https://docs.spring.io/spring-security/reference/servlet/authentication/passkeys.html#passkeys-configuration-pkccor)
*   [Register a New Credential](https://docs.spring.io/spring-security/reference/servlet/authentication/passkeys.html#passkeys-register)
*   [Request the Registration Options](https://docs.spring.io/spring-security/reference/servlet/authentication/passkeys.html#passkeys-register-options)
*   [Registering the Credential](https://docs.spring.io/spring-security/reference/servlet/authentication/passkeys.html#passkeys-register-create)
*   [Verifying an Authentication Assertion](https://docs.spring.io/spring-security/reference/servlet/authentication/passkeys.html#passkeys-verify)
*   [Request the Verification Options](https://docs.spring.io/spring-security/reference/servlet/authentication/passkeys.html#passkeys-verify-options)
*   [Verifying the Credential](https://docs.spring.io/spring-security/reference/servlet/authentication/passkeys.html#passkeys-verify-get)

Spring Security provides support for [passkeys](https://www.passkeys.com/). Passkeys are a more secure method of authenticating than passwords and are built using [WebAuthn](https://www.w3.org/TR/webauthn-3/).

In order to use a passkey to authenticate, a user must first [Register a New Credential](https://docs.spring.io/spring-security/reference/servlet/authentication/passkeys.html#passkeys-register). After the credential is registered, it can be used to authenticate by [verifying an authentication assertion](https://docs.spring.io/spring-security/reference/servlet/authentication/passkeys.html#passkeys-verify).

[](https://docs.spring.io/spring-security/reference/servlet/authentication/passkeys.html#passkeys-dependencies)Required Dependencies
------------------------------------------------------------------------------------------------------------------------------------

To get started, add the `webauthn4j-core` dependency to your project.

This assumes that you are managing Spring Security’s versions with Spring Boot or Spring Security’s BOM as described in [Getting Spring Security](https://docs.spring.io/spring-security/reference/getting-spring-security.html).

Passkeys Dependencies

*   Maven

*   Gradle

```xml
<dependency>
    <groupId>org.springframework.security</groupId>
    <artifactId>spring-security-web</artifactId>
</dependency>
<dependency>
    <groupId>com.webauthn4j</groupId>
    <artifactId>webauthn4j-core</artifactId>
    <version>0.31.0.RELEASE</version>
</dependency>
```

Copied!

```groovy
dependencies {
    implementation "org.springframework.security:spring-security-web"
    implementation "com.webauthn4j:webauthn4j-core:0.31.0.RELEASE"
}
```

Copied!

[](https://docs.spring.io/spring-security/reference/servlet/authentication/passkeys.html#passkeys-configuration)Configuration
-----------------------------------------------------------------------------------------------------------------------------

The following configuration enables passkey authentication. It provides a way to [Register a New Credential](https://docs.spring.io/spring-security/reference/servlet/authentication/passkeys.html#passkeys-register) at `/webauthn/register` and a default log in page that allows [authenticating with passkeys](https://docs.spring.io/spring-security/reference/servlet/authentication/passkeys.html#passkeys-verify).

*   Java

*   Kotlin

```java
@Bean
SecurityFilterChain filterChain(HttpSecurity http) {
	// ...
	http
		// ...
		.formLogin(withDefaults())
		.webAuthn((webAuthn) -> webAuthn
			.rpId("example.com")
			.allowedOrigins("https://example.com")
			// optional properties
			.creationOptionsRepository(new CustomPublicKeyCredentialCreationOptionsRepository())
			.messageConverter(new CustomHttpMessageConverter())
		);
	return http.build();
}

@Bean
UserDetailsService userDetailsService() {
	UserDetails userDetails = User.withDefaultPasswordEncoder()
		.username("user")
		.password("password")
		.roles("USER")
		.build();

	return new InMemoryUserDetailsManager(userDetails);
}
```

Copied!

```kotlin
@Bean
open fun filterChain(http: HttpSecurity): SecurityFilterChain {
	// ...
	http {
		webAuthn {
			rpId = "example.com"
			allowedOrigins = setOf("https://example.com")
			// optional properties
			creationOptionsRepository = CustomPublicKeyCredentialCreationOptionsRepository()
			messageConverter = CustomHttpMessageConverter()
		}
	}
}

@Bean
open fun userDetailsService(): UserDetailsService {
	val userDetails = User.withDefaultPasswordEncoder()
		.username("user")
		.password("password")
		.roles("USER")
		.build()
	return InMemoryUserDetailsManager(userDetails)
}
```

Copied!

### [](https://docs.spring.io/spring-security/reference/servlet/authentication/passkeys.html#passkeys-configuration-persistence)JDBC & Custom Persistence

WebAuthn performs persistence with [`PublicKeyCredentialUserEntityRepository`](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/webauthn/management/PublicKeyCredentialUserEntityRepository.html) and [`UserCredentialRepository`](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/webauthn/management/UserCredentialRepository.html). The default is to use in memory persistence, but JDBC persistence is support with [`JdbcPublicKeyCredentialUserEntityRepository`](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/webauthn/management/JdbcPublicKeyCredentialUserEntityRepository.html) and [`JdbcUserCredentialRepository`](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/webauthn/management/JdbcUserCredentialRepository.html). To configure JDBC based persistence, expose the repositories as a Bean:

*   Java

*   Kotlin

```java
@Bean
JdbcPublicKeyCredentialUserEntityRepository jdbcPublicKeyCredentialRepository(JdbcOperations jdbc) {
	return new JdbcPublicKeyCredentialUserEntityRepository(jdbc);
}

@Bean
JdbcUserCredentialRepository jdbcUserCredentialRepository(JdbcOperations jdbc) {
	return new JdbcUserCredentialRepository(jdbc);
}
```

Copied!

```kotlin
@Bean
fun jdbcPublicKeyCredentialRepository(jdbc: JdbcOperations): JdbcPublicKeyCredentialUserEntityRepository {
    return JdbcPublicKeyCredentialUserEntityRepository(jdbc)
}

@Bean
fun jdbcUserCredentialRepository(jdbc: JdbcOperations): JdbcUserCredentialRepository {
    return JdbcUserCredentialRepository(jdbc)
}
```

Copied!

If JDBC does not meet your needs, you can create your own implementations of the interfaces and use them by exposing them as a Bean similar to the example above.

### [](https://docs.spring.io/spring-security/reference/servlet/authentication/passkeys.html#passkeys-configuration-pkccor)Custom PublicKeyCredentialCreationOptionsRepository

The `PublicKeyCredentialCreationOptionsRepository` is used to persist the `PublicKeyCredentialCreationOptions` between requests. The default is to persist it the `HttpSession`, but at times users may need to customize this behavior. This can be done by setting the optional property `creationOptionsRepository` demonstrated in [Configuration](https://docs.spring.io/spring-security/reference/servlet/authentication/passkeys.html#passkeys-configuration) or by exposing a `PublicKeyCredentialCreationOptionsRepository` Bean:

*   Java

*   Kotlin

```java
@Bean
CustomPublicKeyCredentialCreationOptionsRepository creationOptionsRepository() {
	return new CustomPublicKeyCredentialCreationOptionsRepository();
}
```

Copied!

```kotlin
@Bean
open fun creationOptionsRepository(): CustomPublicKeyCredentialCreationOptionsRepository {
	return CustomPublicKeyCredentialCreationOptionsRepository()
}
```

Copied!

[](https://docs.spring.io/spring-security/reference/servlet/authentication/passkeys.html#passkeys-register)Register a New Credential
------------------------------------------------------------------------------------------------------------------------------------

In order to use a passkey, a user must first [Register a New Credential](https://www.w3.org/TR/webauthn-3/#sctn-registering-a-new-credential).

Registering a new credential is composed of two steps:

1.   Requesting the Registration Options

2.   Registering the Credential

### [](https://docs.spring.io/spring-security/reference/servlet/authentication/passkeys.html#passkeys-register-options)Request the Registration Options

The first step in registration of a new credential is to request the registration options. In Spring Security, a request for the registration options is typically done using JavaScript and looks like:

Spring Security provides a default registration page that can be used as a reference on how to register credentials.

Request for Registration Options

```http
POST /webauthn/register/options
X-CSRF-TOKEN: 4bfd1575-3ad1-4d21-96c7-4ef2d9f86721
```

Copied!

The request above will obtain the registration options for the currently authenticated user. Since the challenge is persisted (state is changed) to be compared at the time of registration, the request must be a POST and include a CSRF token.

Response for Registration Options

```json
{
  "rp": {
    "name": "SimpleWebAuthn Example",
    "id": "example.localhost"
  },
  "user": {
    "name": "user@example.localhost",
    "id": "oWJtkJ6vJ_m5b84LB4_K7QKTCTEwLIjCh4tFMCGHO4w",
    "displayName": "user@example.localhost"
  },
  "challenge": "q7lCdd3SVQxdC-v8pnRAGEn1B2M-t7ZECWPwCAmhWvc",
  "pubKeyCredParams": [
    {
      "type": "public-key",
      "alg": -8
    },
    {
      "type": "public-key",
      "alg": -7
    },
    {
      "type": "public-key",
      "alg": -257
    }
  ],
  "timeout": 300000,
  "excludeCredentials": [],
  "authenticatorSelection": {
    "residentKey": "required",
    "userVerification": "preferred"
  },
  "attestation": "none",
  "extensions": {
    "credProps": true
  }
}
```

Copied!

### [](https://docs.spring.io/spring-security/reference/servlet/authentication/passkeys.html#passkeys-register-create)Registering the Credential

After the registration options are obtained, they are used to create the credentials that are registered. To register a new credential, the application should pass the options to [`navigator.credentials.create`](https://w3c.github.io/webappsec-credential-management/#dom-credentialscontainer-create) after base64url decoding the binary values such as `user.id`, `challenge`, and `excludeCredentials[].id`.

The returned value can then be sent to the server as a JSON request. An example registration request can be found below:

Example Registration Request

```http
POST /webauthn/register
X-CSRF-TOKEN: 4bfd1575-3ad1-4d21-96c7-4ef2d9f86721

{
  "publicKey": { (1)
    "credential": {
      "id": "dYF7EGnRFFIXkpXi9XU2wg",
      "rawId": "dYF7EGnRFFIXkpXi9XU2wg",
      "response": {
        "attestationObject": "o2NmbXRkbm9uZWdhdHRTdG10oGhhdXRoRGF0YViUy9GqwTRaMpzVDbXq1dyEAXVOxrou08k22ggRC45MKNhdAAAAALraVWanqkAfvZZFYZpVEg0AEHWBexBp0RRSF5KV4vV1NsKlAQIDJiABIVggQjmrekPGzyqtoKK9HPUH-8Z2FLpoqkklFpFPQVICQ3IiWCD6I9Jvmor685fOZOyGXqUd87tXfvJk8rxj9OhuZvUALA",
        "clientDataJSON": "eyJ0eXBlIjoid2ViYXV0aG4uY3JlYXRlIiwiY2hhbGxlbmdlIjoiSl9RTi10SFJYRWVKYjlNcUNrWmFPLUdOVmlibXpGVGVWMk43Z0ptQUdrQSIsIm9yaWdpbiI6Imh0dHBzOi8vZXhhbXBsZS5sb2NhbGhvc3Q6ODQ0MyIsImNyb3NzT3JpZ2luIjpmYWxzZX0",
        "transports": [
          "internal",
          "hybrid"
        ]
      },
      "type": "public-key",
      "clientExtensionResults": {},
      "authenticatorAttachment": "platform"
    },
    "label": "1password" (2)
  }
}
```

Copied!

**1**The result of calling `navigator.credentials.create` with binary values base64url encoded.
**2**A label that the user selects to have associated with this credential to help the user distinguish the credential.

Example Successful Registration Response

```http
HTTP/1.1 200 OK

{
  "success": true
}
```

Copied!

[](https://docs.spring.io/spring-security/reference/servlet/authentication/passkeys.html#passkeys-verify)Verifying an Authentication Assertion
----------------------------------------------------------------------------------------------------------------------------------------------

After [Register a New Credential](https://docs.spring.io/spring-security/reference/servlet/authentication/passkeys.html#passkeys-register) the passkey can be [verified](https://www.w3.org/TR/webauthn-3/#sctn-verifying-assertion) (authenticated).

Verifying a credential is composed of two steps:

1.   Requesting the Verification Options

2.   Verifying the Credential

### [](https://docs.spring.io/spring-security/reference/servlet/authentication/passkeys.html#passkeys-verify-options)Request the Verification Options

The first step in verification of a credential is to request the verification options. In Spring Security, a request for the verification options is typically done using JavaScript and looks like:

Spring Security provides a default log in page that can be used as a reference on how to verify credentials.

Request for Verification Options

```http
POST /webauthn/authenticate/options
X-CSRF-TOKEN: 4bfd1575-3ad1-4d21-96c7-4ef2d9f86721
```

Copied!

The request above will obtain the verification options. Since the challenge is persisted (state is changed) to be compared at the time of authentication, the request must be a POST and include a CSRF token.

The response will contain the options for obtaining a credential with binary values such as `challenge` base64url encoded.

Example Response for Verification Options

```json
{
  "challenge": "cQfdGrj9zDg3zNBkOH3WPL954FTOShVy0-CoNgSewNM",
  "timeout": 300000,
  "rpId": "example.localhost",
  "allowCredentials": [],
  "userVerification": "preferred",
  "extensions": {}
}
```

Copied!

### [](https://docs.spring.io/spring-security/reference/servlet/authentication/passkeys.html#passkeys-verify-get)Verifying the Credential

After the verification options are obtained, they are used to get a credential. To get a credential, the application should pass the options to [`navigator.credentials.get`](https://w3c.github.io/webappsec-credential-management/#dom-credentialscontainer-create) after base64url decoding the binary values such as `challenge`.

The returned value of `navigator.credentials.get` can then be sent to the server as a JSON request. Binary values such as `rawId` and `response.*` must be base64url encoded. An example authentication request can be found below:

Example Authentication Request

```http
POST /login/webauthn
X-CSRF-TOKEN: 4bfd1575-3ad1-4d21-96c7-4ef2d9f86721

{
  "id": "dYF7EGnRFFIXkpXi9XU2wg",
  "rawId": "dYF7EGnRFFIXkpXi9XU2wg",
  "response": {
    "authenticatorData": "y9GqwTRaMpzVDbXq1dyEAXVOxrou08k22ggRC45MKNgdAAAAAA",
    "clientDataJSON": "eyJ0eXBlIjoid2ViYXV0aG4uZ2V0IiwiY2hhbGxlbmdlIjoiRFVsRzRDbU9naWhKMG1vdXZFcE9HdUk0ZVJ6MGRRWmxUQmFtbjdHQ1FTNCIsIm9yaWdpbiI6Imh0dHBzOi8vZXhhbXBsZS5sb2NhbGhvc3Q6ODQ0MyIsImNyb3NzT3JpZ2luIjpmYWxzZX0",
    "signature": "MEYCIQCW2BcUkRCAXDmGxwMi78jknenZ7_amWrUJEYoTkweldAIhAMD0EMp1rw2GfwhdrsFIeDsL7tfOXVPwOtfqJntjAo4z",
    "userHandle": "Q3_0Xd64_HW0BlKRAJnVagJTpLKLgARCj8zjugpRnVo"
  },
  "clientExtensionResults": {},
  "authenticatorAttachment": "platform"
}
```

Copied!

Example Successful Authentication Response

```http
HTTP/1.1 200 OK

{
  "redirectUrl": "/", (1)
  "authenticated": true (2)
}
```

Copied!

**1**The URL to redirect to
**2**Indicates that the user is authenticated

Example Authentication Failure Response

```http
HTTP/1.1 401 OK
```

Copied!

*   [Spring Security](https://docs.spring.io/spring-security/reference/index.html) 

 Stable  
    *   [7.0.3](https://docs.spring.io/spring-security/reference/servlet/authentication/passkeys.html)
    *   [6.5.8](https://docs.spring.io/spring-security/reference/6.5/servlet/authentication/passkeys.html)

 Preview 

    *   [7.1.0-M2](https://docs.spring.io/spring-security/reference/7.1/servlet/authentication/passkeys.html)

 Snapshot 

    *   [7.1.0-SNAPSHOT](https://docs.spring.io/spring-security/reference/7.1-SNAPSHOT/servlet/authentication/passkeys.html)
    *   [7.0.4-SNAPSHOT](https://docs.spring.io/spring-security/reference/7.0-SNAPSHOT/servlet/authentication/passkeys.html)
    *   [6.5.9-SNAPSHOT](https://docs.spring.io/spring-security/reference/6.5-SNAPSHOT/servlet/authentication/passkeys.html)

*    Related Spring Documentation 
    *   [Spring Framework](https://docs.spring.io/spring-framework/reference/)
    *   [](https://docs.spring.io/spring-security/reference/servlet/authentication/passkeys.html)[Spring Security](https://docs.spring.io/spring-security/reference/)
        *   [Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/)
        *   [Spring LDAP](https://docs.spring.io/spring-ldap/reference/)
        *   [Spring Security Kerberos](https://docs.spring.io/spring-security-kerberos/reference/)
        *   [Spring Session](https://docs.spring.io/spring-session/reference/)
        *   [Spring Vault](https://docs.spring.io/spring-vault/reference/)

    *   [Spring GraphQL](https://docs.spring.io/spring-graphql/reference/)

[All Docs...](https://docs.spring.io/spring-security/reference/spring-projects.html)

![Image 2: Spring](https://docs.spring.io/spring-security/reference/_/img/spring-logo.svg)
Copyright © 2005 - 2026 Broadcom. All Rights Reserved. The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

[Terms of Use](https://www.vmware.com/help/legal.html) • [Privacy](https://www.vmware.com/help/privacy.html) • [Trademark Guidelines](https://spring.io/trademarks)• [Thank you](https://spring.io/thank-you) • [Your California Privacy Rights](https://www.vmware.com/help/privacy/california-privacy-rights.html) • [Cookies Settings](https://docs.spring.io/spring-security/reference/servlet/authentication/passkeys.html)

Apache®, Apache Tomcat®, Apache Kafka®, Apache Cassandra™, and Apache Geode™ are trademarks or registered trademarks of the Apache Software Foundation in the United States and/or other countries. Java™, Java™ SE, Java™ EE, and OpenJDK™ are trademarks of Oracle and/or its affiliates. Kubernetes® is a registered trademark of the Linux Foundation in the United States and other countries. Linux® is the registered trademark of Linus Torvalds in the United States and other countries. Windows® and Microsoft® Azure are registered trademarks of Microsoft Corporation. “AWS” and “Amazon Web Services” are trademarks or registered trademarks of Amazon.com Inc. or its affiliates. All other trademarks and copyrights are property of their respective owners and are only mentioned for informative purposes. Other names may be trademarks of their respective owners.

[](https://www.youtube.com/user/SpringSourceDev "Youtube")[](https://github.com/spring-projects "GitHub")[](https://twitter.com/springcentral "Twitter")

[Search in all Spring Docs](https://docs.spring.io/spring-security/reference/search.html)

[![Image 3](https://docs.spring.io/spring-security/reference/_/img/algolia-light.svg)![Image 4](https://docs.spring.io/spring-security/reference/_/img/algolia-dark.svg)](https://www.algolia.com/)

Cookies
-------

Broadcom and third-party partners use technology, including cookies to, among other things, analyze site usage, improve your experience and help us advertise. By using our site, you agree to our use of cookies as described in our [Cookie Notice](https://www.broadcom.com/company/legal/cookie-policy)

Allow All

Required Only

Cookies Settings

![Image 5: Company Logo](https://cdn.cookielaw.org/logos/8153b982-ae11-46a0-b7c2-6e4e3b591d72/8a37f712-8eb0-4967-9ca7-343409702cfa/5228da75-715f-4d1a-9262-2662775eb1ce/Broadcom_Logo_Red-Black_no-tag.png)

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

[![Image 6: Powered by Onetrust](https://cdn.cookielaw.org/logos/static/powered_by_logo.svg)](https://www.onetrust.com/products/cookie-consent/)
