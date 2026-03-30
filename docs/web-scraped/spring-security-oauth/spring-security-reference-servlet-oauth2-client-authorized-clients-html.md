# Source: https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorized-clients.html

Title: Authorized Client Features :: Spring Security

URL Source: https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorized-clients.html

Markdown Content:
Authorized Client Features :: Spring Security
===============

[![Image 1: Spring](https://docs.spring.io/spring-security/reference/_/img/spring-logo.svg)](https://spring.io/)

[Why Spring](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorized-clients.html#)

[Overview](https://spring.io/why-spring)[Microservices](https://spring.io/microservices)[Reactive](https://spring.io/reactive)[Event Driven](https://spring.io/event-driven)[Cloud](https://spring.io/cloud)[Web Applications](https://spring.io/web-applications)[Serverless](https://spring.io/serverless)[Batch](https://spring.io/batch)

[Learn](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorized-clients.html#)

[Overview](https://spring.io/learn)[Quickstart](https://spring.io/quickstart)[Guides](https://spring.io/guides)[Blog](https://spring.io/blog)

[Projects](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorized-clients.html#)

[Overview](https://spring.io/projects)[Spring Boot](https://spring.io/projects/spring-boot)[Spring Framework](https://spring.io/projects/spring-framework)[Spring Cloud](https://spring.io/projects/spring-cloud)[Spring Cloud Data Flow](https://spring.io/projects/spring-cloud-dataflow)[Spring Data](https://spring.io/projects/spring-data)[Spring Integration](https://spring.io/projects/spring-integration)[Spring Batch](https://spring.io/projects/spring-batch)[Spring Security](https://spring.io/projects/spring-security)[View all projects](https://spring.io/projects)*   DEVELOPMENT TOOLS
[Spring Tools 4](https://spring.io/tools)[Spring Initializr](https://start.spring.io/)

[Academy](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorized-clients.html#)

[Courses](https://spring.academy/courses)[Get Certified](https://spring.academy/learning-path)

[Solutions](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorized-clients.html#)

[Overview](https://spring.io/solutions)[Spring Runtime](https://spring.io/support)[Spring Consulting](https://spring.io/consulting)[Spring Academy For Teams](https://spring.academy/teams)[Security Advisories](https://spring.io/security)

[Community](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorized-clients.html#)

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

### Authorized Client Features

*   [Resolving an Authorized Client](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorized-clients.html#oauth2-client-registered-authorized-client)
*   [RestClient Integration](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorized-clients.html#oauth2-client-rest-client)
*   [Providing the clientRegistrationId](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorized-clients.html#oauth2-client-rest-client-registration-id)
*   [Providing the principal](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorized-clients.html#oauth2-client-rest-client-principal)
*   [Handling Failure](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorized-clients.html#oauth2-client-rest-client-authorization-failure-handler)
*   [HTTP Service Clients](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorized-clients.html#oauth2-client-rest-client-interface)
*   [WebClient Integration for Servlet Environments](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorized-clients.html#oauth2-client-web-client)
*   [Providing the Authorized Client](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorized-clients.html#oauth2-client-web-client-authorized-client)
*   [Defaulting the Authorized Client](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorized-clients.html#oauth2-client-web-client-default-authorized-client)

[Edit this Page](https://github.com/spring-projects/spring-security/blob/7.0.3/docs/modules/ROOT/pages/servlet/oauth2/client/authorized-clients.adoc)[GitHub Project](https://github.com/spring-projects/spring-security "GitHub")[Stack Overflow](https://stackoverflow.com/tags/spring-security)

*   [Spring Security](https://docs.spring.io/spring-security/reference/index.html)
*   [Servlet Applications](https://docs.spring.io/spring-security/reference/servlet/index.html)
*   [OAuth2](https://docs.spring.io/spring-security/reference/servlet/oauth2/index.html)
*   [OAuth2 Client](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/index.html)
*   [OAuth2 Authorized Clients](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorized-clients.html)

[](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorized-clients.html)Authorized Client Features
============================================================================================================================

### Authorized Client Features

*   [Resolving an Authorized Client](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorized-clients.html#oauth2-client-registered-authorized-client)
*   [RestClient Integration](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorized-clients.html#oauth2-client-rest-client)
*   [Providing the clientRegistrationId](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorized-clients.html#oauth2-client-rest-client-registration-id)
*   [Providing the principal](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorized-clients.html#oauth2-client-rest-client-principal)
*   [Handling Failure](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorized-clients.html#oauth2-client-rest-client-authorization-failure-handler)
*   [HTTP Service Clients](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorized-clients.html#oauth2-client-rest-client-interface)
*   [WebClient Integration for Servlet Environments](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorized-clients.html#oauth2-client-web-client)
*   [Providing the Authorized Client](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorized-clients.html#oauth2-client-web-client-authorized-client)
*   [Defaulting the Authorized Client](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorized-clients.html#oauth2-client-web-client-default-authorized-client)

This section covers additional features provided by Spring Security for OAuth2 client.

[](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorized-clients.html#oauth2-client-registered-authorized-client)[](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorized-clients.html)Resolving an Authorized Client
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The `@RegisteredOAuth2AuthorizedClient` annotation provides the ability to resolve a method parameter to an argument value of type `OAuth2AuthorizedClient`. This is a convenient alternative compared to accessing the `OAuth2AuthorizedClient` by using the `OAuth2AuthorizedClientManager` or `OAuth2AuthorizedClientService`. The following example shows how to use `@RegisteredOAuth2AuthorizedClient`:

*   Java

*   Kotlin

```java
@Controller
public class OAuth2ClientController {

	@GetMapping("/")
	public String index(@RegisteredOAuth2AuthorizedClient("okta") OAuth2AuthorizedClient authorizedClient) {
		OAuth2AccessToken accessToken = authorizedClient.getAccessToken();

		...

		return "index";
	}
}
```

Copied!

```kotlin
@Controller
class OAuth2ClientController {
    @GetMapping("/")
    fun index(@RegisteredOAuth2AuthorizedClient("okta") authorizedClient: OAuth2AuthorizedClient): String {
        val accessToken = authorizedClient.accessToken

        ...

        return "index"
    }
}
```

Copied!

The `@RegisteredOAuth2AuthorizedClient` annotation is handled by `OAuth2AuthorizedClientArgumentResolver`, which directly uses an [`OAuth2AuthorizedClientManager`](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/core.html#oauth2Client-authorized-manager-provider) and, therefore, inherits its capabilities.

[](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorized-clients.html#oauth2-client-rest-client)RestClient Integration
--------------------------------------------------------------------------------------------------------------------------------------------------

Support for `RestClient` is provided by `OAuth2ClientHttpRequestInterceptor`. This interceptor provides the ability to make protected resources requests by placing a `Bearer` token in the `Authorization` header of an outbound request. The interceptor directly uses an `OAuth2AuthorizedClientManager` and therefore inherits the following capabilities:

*   Performs an OAuth 2.0 Access Token request to obtain `OAuth2AccessToken` if the client has not yet been authorized

    *   `authorization_code`: Triggers the Authorization Request redirect to initiate the flow

    *   `client_credentials`: The access token is obtained directly from the Token Endpoint

    *   Additional grant types are supported by [enabling extension grant types](https://docs.spring.io/spring-security/reference/servlet/oauth2/index.html#oauth2-client-enable-extension-grant-type)

*   If an existing `OAuth2AccessToken` is expired, it is refreshed (or renewed)

The following example uses the default `OAuth2AuthorizedClientManager` to configure a `RestClient` capable of accessing protected resources by placing `Bearer` tokens in the `Authorization` header of each request:

Configure `RestClient` with `ClientHttpRequestInterceptor`

*   Java

*   Kotlin

```java
@Configuration
public class RestClientConfig {

	@Bean
	public RestClient restClient(OAuth2AuthorizedClientManager authorizedClientManager) {
		OAuth2ClientHttpRequestInterceptor requestInterceptor =
				new OAuth2ClientHttpRequestInterceptor(authorizedClientManager);

		return RestClient.builder()
				.requestInterceptor(requestInterceptor)
				.build();
	}

}
```

Copied!

```kotlin
@Configuration
class RestClientConfig {

	@Bean
	fun restClient(authorizedClientManager: OAuth2AuthorizedClientManager): RestClient {
		val requestInterceptor = OAuth2ClientHttpRequestInterceptor(authorizedClientManager)

		return RestClient.builder()
			.requestInterceptor(requestInterceptor)
			.build()
	}

}
```

Copied!

### [](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorized-clients.html#oauth2-client-rest-client-registration-id)Providing the `clientRegistrationId`

`OAuth2ClientHttpRequestInterceptor` uses a `ClientRegistrationIdResolver` to determine which client is used to obtain an access token. By default, `RequestAttributeClientRegistrationIdResolver` is used to resolve the `clientRegistrationId` from `HttpRequest#attributes()`.

The following example demonstrates providing a `clientRegistrationId` via attributes:

Provide `clientRegistrationId` via attributes

*   Java

*   Kotlin

```java
import static org.springframework.security.oauth2.client.web.client.RequestAttributeClientRegistrationIdResolver.clientRegistrationId;

@Controller
public class ResourceController {

	private final RestClient restClient;

	public ResourceController(RestClient restClient) {
		this.restClient = restClient;
	}

	@GetMapping("/")
	public String index() {
		String resourceUri = "...";

		String body = this.restClient.get()
				.uri(resourceUri)
				.attributes(clientRegistrationId("okta"))   (1)
				.retrieve()
				.body(String.class);

		// ...

		return "index";
	}

}
```

Copied!

```kotlin
import org.springframework.security.oauth2.client.web.client.RequestAttributeClientRegistrationIdResolver.clientRegistrationId
import org.springframework.web.client.body

@Controller
class ResourceController(private restClient: RestClient) {

	@GetMapping("/")
	fun index(): String {
		val resourceUri = "..."

		val body: String = restClient.get()
				.uri(resourceUri)
				.attributes(clientRegistrationId("okta"))   (1)
				.retrieve()
				.body<String>()

		// ...

		return "index"
	}

}
```

Copied!

**1**`clientRegistrationId()` is a `static` method in `RequestAttributeClientRegistrationIdResolver`.

Alternatively, a custom `ClientRegistrationIdResolver` can be provided. The following example configures a custom implementation that resolves the `clientRegistrationId` from the current user.

Configure `ClientHttpRequestInterceptor` with custom `ClientRegistrationIdResolver`

*   Java

*   Kotlin

```java
@Configuration
public class RestClientConfig {

	@Bean
	public RestClient restClient(OAuth2AuthorizedClientManager authorizedClientManager) {
		OAuth2ClientHttpRequestInterceptor requestInterceptor =
				new OAuth2ClientHttpRequestInterceptor(authorizedClientManager);
		requestInterceptor.setClientRegistrationIdResolver(clientRegistrationIdResolver());

		return RestClient.builder()
				.requestInterceptor(requestInterceptor)
				.build();
	}

	private static ClientRegistrationIdResolver clientRegistrationIdResolver() {
		return (request) -> {
			Authentication authentication = SecurityContextHolder.getContext().getAuthentication();
			return (authentication instanceof OAuth2AuthenticationToken principal)
					? principal.getAuthorizedClientRegistrationId() : null;
		};
	}

}
```

Copied!

```kotlin
@Configuration
class RestClientConfig {

	@Bean
	fun restClient(authorizedClientManager: OAuth2AuthorizedClientManager): RestClient {
		val requestInterceptor = OAuth2ClientHttpRequestInterceptor(authorizedClientManager)
		requestInterceptor.setClientRegistrationIdResolver(clientRegistrationIdResolver())

		return RestClient.builder()
			.requestInterceptor(requestInterceptor)
			.build()
	}

	fun clientRegistrationIdResolver(): ClientRegistrationIdResolver {
		return ClientRegistrationIdResolver { request ->
			val authentication = SecurityContextHolder.getContext().getAuthentication()
			return if (authentication instanceof OAuth2AuthenticationToken) {
				authentication.getAuthorizedClientRegistrationId()
			} else {
                null
			}
		}
	}

}
```

Copied!

### [](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorized-clients.html#oauth2-client-rest-client-principal)Providing the `principal`

`OAuth2ClientHttpRequestInterceptor` uses a `PrincipalResolver` to determine which principal name is associated with the access token, which allows an application to choose how to scope the `OAuth2AuthorizedClient` that is stored. By default, `SecurityContextHolderPrincipalResolver` is used to resolve the current `principal` from the `SecurityContextHolder`.

Alternatively, the `principal` can be resolved from `HttpRequest#attributes()` by configuring `RequestAttributePrincipalResolver`, as the following example shows:

Configure `ClientHttpRequestInterceptor` with `RequestAttributePrincipalResolver`

*   Java

*   Kotlin

```java
@Configuration
public class RestClientConfig {

	@Bean
	public RestClient restClient(OAuth2AuthorizedClientManager authorizedClientManager) {
		OAuth2ClientHttpRequestInterceptor requestInterceptor =
				new OAuth2ClientHttpRequestInterceptor(authorizedClientManager);
		requestInterceptor.setPrincipalResolver(new RequestAttributePrincipalResolver());

		return RestClient.builder()
				.requestInterceptor(requestInterceptor)
				.build();
	}

}
```

Copied!

```kotlin
@Configuration
class RestClientConfig {

	@Bean
	fun restClient(authorizedClientManager: OAuth2AuthorizedClientManager): RestClient {
		val requestInterceptor = OAuth2ClientHttpRequestInterceptor(authorizedClientManager)
		requestInterceptor.setPrincipalResolver(RequestAttributePrincipalResolver())

		return RestClient.builder()
			.requestInterceptor(requestInterceptor)
			.build()
	}

}
```

Copied!

The following example demonstrates providing a `principal` name via attributes that scopes the `OAuth2AuthorizedClient` to the application instead of the current user:

Provide `principal` name via attributes

*   Java

*   Kotlin

```java
import static org.springframework.security.oauth2.client.web.client.RequestAttributeClientRegistrationIdResolver.clientRegistrationId;
import static org.springframework.security.oauth2.client.web.client.RequestAttributePrincipalResolver.principal;

@Controller
public class ResourceController {

	private final RestClient restClient;

	public ResourceController(RestClient restClient) {
		this.restClient = restClient;
	}

	@GetMapping("/")
	public String index() {
		String resourceUri = "...";

		String body = this.restClient.get()
				.uri(resourceUri)
				.attributes(clientRegistrationId("okta"))
				.attributes(principal("my-application"))   (1)
				.retrieve()
				.body(String.class);

		// ...

		return "index";
	}

}
```

Copied!

```kotlin
import org.springframework.security.oauth2.client.web.client.RequestAttributeClientRegistrationIdResolver.clientRegistrationId
import org.springframework.security.oauth2.client.web.client.RequestAttributePrincipalResolver.principal
import org.springframework.web.client.body

@Controller
class ResourceController(private restClient: RestClient) {

    @GetMapping("/")
	fun index(): String {
		val resourceUri = "..."

		val body: String = restClient.get()
				.uri(resourceUri)
				.attributes(clientRegistrationId("okta"))
				.attributes(principal("my-application"))   (1)
				.retrieve()
				.body<String>()

		// ...

		return "index"
	}

}
```

Copied!

**1**`principal()` is a `static` method in `RequestAttributePrincipalResolver`.

### [](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorized-clients.html#oauth2-client-rest-client-authorization-failure-handler)Handling Failure

If an access token is invalid for any reason (e.g. expired token), it can be beneficial to handle the failure by removing the access token so that it cannot be used again. You can set up the interceptor to do this automatically by providing an `OAuth2AuthorizationFailureHandler` to remove the access token.

The following example uses an `OAuth2AuthorizedClientRepository` to set up an `OAuth2AuthorizationFailureHandler` that removes an invalid `OAuth2AuthorizedClient`**within** the context of an `HttpServletRequest`:

Configure `OAuth2AuthorizationFailureHandler` using `OAuth2AuthorizedClientRepository`

*   Java

*   Kotlin

```java
@Configuration
public class RestClientConfig {

	@Bean
	public RestClient restClient(OAuth2AuthorizedClientManager authorizedClientManager,
			OAuth2AuthorizedClientRepository authorizedClientRepository) {

		OAuth2ClientHttpRequestInterceptor requestInterceptor =
				new OAuth2ClientHttpRequestInterceptor(authorizedClientManager);

		OAuth2AuthorizationFailureHandler authorizationFailureHandler =
			OAuth2ClientHttpRequestInterceptor.authorizationFailureHandler(authorizedClientRepository);
		requestInterceptor.setAuthorizationFailureHandler(authorizationFailureHandler);

		return RestClient.builder()
				.requestInterceptor(requestInterceptor)
				.build();
	}

}
```

Copied!

```kotlin
@Configuration
class RestClientConfig {

	@Bean
	fun restClient(authorizedClientManager: OAuth2AuthorizedClientManager,
			authorizedClientRepository: OAuth2AuthorizedClientRepository): RestClient {

		val requestInterceptor = OAuth2ClientHttpRequestInterceptor(authorizedClientManager)

		val authorizationFailureHandler = OAuth2ClientHttpRequestInterceptor
			.authorizationFailureHandler(authorizedClientRepository)
		requestInterceptor.setAuthorizationFailureHandler(authorizationFailureHandler)

		return RestClient.builder()
			.requestInterceptor(requestInterceptor)
			.build()
	}

}
```

Copied!

Alternatively, an `OAuth2AuthorizedClientService` can be used to remove an invalid `OAuth2AuthorizedClient`**outside** the context of an `HttpServletRequest`, as the following example shows:

Configure `OAuth2AuthorizationFailureHandler` using `OAuth2AuthorizedClientService`

*   Java

*   Kotlin

```java
@Configuration
public class RestClientConfig {

	@Bean
	public RestClient restClient(OAuth2AuthorizedClientManager authorizedClientManager,
			OAuth2AuthorizedClientService authorizedClientService) {

		OAuth2ClientHttpRequestInterceptor requestInterceptor =
				new OAuth2ClientHttpRequestInterceptor(authorizedClientManager);

		OAuth2AuthorizationFailureHandler authorizationFailureHandler =
			OAuth2ClientHttpRequestInterceptor.authorizationFailureHandler(authorizedClientService);
		requestInterceptor.setAuthorizationFailureHandler(authorizationFailureHandler);

		return RestClient.builder()
				.requestInterceptor(requestInterceptor)
				.build();
	}

}
```

Copied!

```kotlin
@Configuration
class RestClientConfig {

	@Bean
	fun restClient(authorizedClientManager: OAuth2AuthorizedClientManager,
			authorizedClientService: OAuth2AuthorizedClientService): RestClient {

		val requestInterceptor = OAuth2ClientHttpRequestInterceptor(authorizedClientManager)

		val authorizationFailureHandler = OAuth2ClientHttpRequestInterceptor
			.authorizationFailureHandler(authorizedClientService)
		requestInterceptor.setAuthorizationFailureHandler(authorizationFailureHandler)

		return RestClient.builder()
			.requestInterceptor(requestInterceptor)
			.build()
	}

}
```

Copied!

### [](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorized-clients.html#oauth2-client-rest-client-interface)HTTP Service Clients

Spring Security’s OAuth support integrates with [HTTP Service Clients Integration](https://docs.spring.io/spring-security/reference/features/integrations/rest/http-service-client.html).

[](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorized-clients.html#oauth2-client-web-client)[](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorized-clients.html)WebClient Integration for Servlet Environments
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The OAuth 2.0 Client support integrates with `WebClient` by using an `ExchangeFilterFunction`.

The `ServletOAuth2AuthorizedClientExchangeFilterFunction` provides a mechanism for requesting protected resources by using an `OAuth2AuthorizedClient` and including the associated `OAuth2AccessToken` as a Bearer Token. It directly uses an [`OAuth2AuthorizedClientManager`](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/core.html#oauth2Client-authorized-manager-provider) and, therefore, inherits the following capabilities:

*   An `OAuth2AccessToken` is requested if the client has not yet been authorized.

    *   `authorization_code`: Triggers the Authorization Request redirect to initiate the flow.

    *   `client_credentials`: The access token is obtained directly from the Token Endpoint.

*   If the `OAuth2AccessToken` is expired, it is refreshed (or renewed) if an `OAuth2AuthorizedClientProvider` is available to perform the authorization

The following code shows an example of how to configure `WebClient` with OAuth 2.0 Client support:

*   Java

*   Kotlin

```java
@Bean
WebClient webClient(OAuth2AuthorizedClientManager authorizedClientManager) {
	ServletOAuth2AuthorizedClientExchangeFilterFunction oauth2Client =
			new ServletOAuth2AuthorizedClientExchangeFilterFunction(authorizedClientManager);
	return WebClient.builder()
			.apply(oauth2Client.oauth2Configuration())
			.build();
}
```

Copied!

```kotlin
@Bean
fun webClient(authorizedClientManager: OAuth2AuthorizedClientManager?): WebClient {
    val oauth2Client = ServletOAuth2AuthorizedClientExchangeFilterFunction(authorizedClientManager)
    return WebClient.builder()
            .apply(oauth2Client.oauth2Configuration())
            .build()
}
```

Copied!

### [](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorized-clients.html#oauth2-client-web-client-authorized-client)Providing the Authorized Client

The `ServletOAuth2AuthorizedClientExchangeFilterFunction` determines the client to use (for a request) by resolving the `OAuth2AuthorizedClient` from the `ClientRequest.attributes()` (request attributes).

The following code shows how to set an `OAuth2AuthorizedClient` as a request attribute:

*   Java

*   Kotlin

```java
@GetMapping("/")
public String index(@RegisteredOAuth2AuthorizedClient("okta") OAuth2AuthorizedClient authorizedClient) {
	String resourceUri = ...

	String body = webClient
			.get()
			.uri(resourceUri)
			.attributes(oauth2AuthorizedClient(authorizedClient))   (1)
			.retrieve()
			.bodyToMono(String.class)
			.block();

	...

	return "index";
}
```

Copied!

```kotlin
@GetMapping("/")
fun index(@RegisteredOAuth2AuthorizedClient("okta") authorizedClient: OAuth2AuthorizedClient): String {
    val resourceUri: String = ...
    val body: String = webClient
            .get()
            .uri(resourceUri)
            .attributes(oauth2AuthorizedClient(authorizedClient)) (1)
            .retrieve()
            .bodyToMono()
            .block()

    ...

    return "index"
}
```

Copied!

**1**`oauth2AuthorizedClient()` is a `static` method in `ServletOAuth2AuthorizedClientExchangeFilterFunction`.

The following code shows how to set the `ClientRegistration.getRegistrationId()` as a request attribute:

*   Java

*   Kotlin

```java
@GetMapping("/")
public String index() {
	String resourceUri = ...

	String body = webClient
			.get()
			.uri(resourceUri)
			.attributes(clientRegistrationId("okta"))   (1)
			.retrieve()
			.bodyToMono(String.class)
			.block();

	...

	return "index";
}
```

Copied!

```kotlin
@GetMapping("/")
fun index(): String {
    val resourceUri: String = ...

    val body: String = webClient
            .get()
            .uri(resourceUri)
            .attributes(clientRegistrationId("okta"))  (1)
            .retrieve()
            .bodyToMono()
            .block()

    ...

    return "index"
}
```

Copied!

**1**`clientRegistrationId()` is a `static` method in `ServletOAuth2AuthorizedClientExchangeFilterFunction`.

The following code shows how to set an `Authentication` as a request attribute:

*   Java

*   Kotlin

```java
@GetMapping("/")
public String index() {
	String resourceUri = ...

	Authentication anonymousAuthentication = new AnonymousAuthenticationToken(
			"anonymous", "anonymousUser", AuthorityUtils.createAuthorityList("ROLE_ANONYMOUS"));
	String body = webClient
			.get()
			.uri(resourceUri)
			.attributes(authentication(anonymousAuthentication))   (1)
			.retrieve()
			.bodyToMono(String.class)
			.block();

	...

	return "index";
}
```

Copied!

```kotlin
@GetMapping("/")
fun index(): String {
    val resourceUri: String = ...

    val anonymousAuthentication: Authentication = AnonymousAuthenticationToken(
            "anonymous", "anonymousUser", AuthorityUtils.createAuthorityList("ROLE_ANONYMOUS"))
    val body: String = webClient
            .get()
            .uri(resourceUri)
            .attributes(authentication(anonymousAuthentication))  (1)
            .retrieve()
            .bodyToMono()
            .block()

    ...

    return "index"
}
```

Copied!

**1**`authentication()` is a `static` method in `ServletOAuth2AuthorizedClientExchangeFilterFunction`.

It is recommended to be cautious with this feature since all HTTP requests will receive an access token bound to the provided principal.

### [](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorized-clients.html#oauth2-client-web-client-default-authorized-client)Defaulting the Authorized Client

If neither `OAuth2AuthorizedClient` or `ClientRegistration.getRegistrationId()` is provided as a request attribute, the `ServletOAuth2AuthorizedClientExchangeFilterFunction` can determine the _default_ client to use, depending on its configuration.

If `setDefaultOAuth2AuthorizedClient(true)` is configured and the user has authenticated by using `HttpSecurity.oauth2Login()`, the `OAuth2AccessToken` associated with the current `OAuth2AuthenticationToken` is used.

The following code shows the specific configuration:

*   Java

*   Kotlin

```java
@Bean
WebClient webClient(OAuth2AuthorizedClientManager authorizedClientManager) {
	ServletOAuth2AuthorizedClientExchangeFilterFunction oauth2Client =
			new ServletOAuth2AuthorizedClientExchangeFilterFunction(authorizedClientManager);
	oauth2Client.setDefaultOAuth2AuthorizedClient(true);
	return WebClient.builder()
			.apply(oauth2Client.oauth2Configuration())
			.build();
}
```

Copied!

```kotlin
@Bean
fun webClient(authorizedClientManager: OAuth2AuthorizedClientManager?): WebClient {
    val oauth2Client = ServletOAuth2AuthorizedClientExchangeFilterFunction(authorizedClientManager)
    oauth2Client.setDefaultOAuth2AuthorizedClient(true)
    return WebClient.builder()
            .apply(oauth2Client.oauth2Configuration())
            .build()
}
```

Copied!

Be cautious with this feature, since all HTTP requests receive the access token.

Alternatively, if `setDefaultClientRegistrationId("okta")` is configured with a valid `ClientRegistration`, the `OAuth2AccessToken` associated with the `OAuth2AuthorizedClient` is used.

The following code shows the specific configuration:

*   Java

*   Kotlin

```java
@Bean
WebClient webClient(OAuth2AuthorizedClientManager authorizedClientManager) {
	ServletOAuth2AuthorizedClientExchangeFilterFunction oauth2Client =
			new ServletOAuth2AuthorizedClientExchangeFilterFunction(authorizedClientManager);
	oauth2Client.setDefaultClientRegistrationId("okta");
	return WebClient.builder()
			.apply(oauth2Client.oauth2Configuration())
			.build();
}
```

Copied!

```kotlin
@Bean
fun webClient(authorizedClientManager: OAuth2AuthorizedClientManager?): WebClient {
    val oauth2Client = ServletOAuth2AuthorizedClientExchangeFilterFunction(authorizedClientManager)
    oauth2Client.setDefaultClientRegistrationId("okta")
    return WebClient.builder()
            .apply(oauth2Client.oauth2Configuration())
            .build()
}
```

Copied!

Be cautious with this feature, since all HTTP requests receive the access token.

*   [Spring Security](https://docs.spring.io/spring-security/reference/index.html) 

 Stable  
    *   [7.0.3](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorized-clients.html)
    *   [6.5.8](https://docs.spring.io/spring-security/reference/6.5/servlet/oauth2/client/authorized-clients.html)

 Preview 

    *   [7.1.0-M2](https://docs.spring.io/spring-security/reference/7.1/servlet/oauth2/client/authorized-clients.html)

 Snapshot 

    *   [7.1.0-SNAPSHOT](https://docs.spring.io/spring-security/reference/7.1-SNAPSHOT/servlet/oauth2/client/authorized-clients.html)
    *   [7.0.4-SNAPSHOT](https://docs.spring.io/spring-security/reference/7.0-SNAPSHOT/servlet/oauth2/client/authorized-clients.html)
    *   [6.5.9-SNAPSHOT](https://docs.spring.io/spring-security/reference/6.5-SNAPSHOT/servlet/oauth2/client/authorized-clients.html)

*    Related Spring Documentation 
    *   [Spring Framework](https://docs.spring.io/spring-framework/reference/)
    *   [](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorized-clients.html)[Spring Security](https://docs.spring.io/spring-security/reference/)
        *   [Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/)
        *   [Spring LDAP](https://docs.spring.io/spring-ldap/reference/)
        *   [Spring Security Kerberos](https://docs.spring.io/spring-security-kerberos/reference/)
        *   [Spring Session](https://docs.spring.io/spring-session/reference/)
        *   [Spring Vault](https://docs.spring.io/spring-vault/reference/)

    *   [Spring GraphQL](https://docs.spring.io/spring-graphql/reference/)

[All Docs...](https://docs.spring.io/spring-security/reference/spring-projects.html)

![Image 2: Spring](https://docs.spring.io/spring-security/reference/_/img/spring-logo.svg)
Copyright © 2005 - 2026 Broadcom. All Rights Reserved. The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

[Terms of Use](https://www.vmware.com/help/legal.html) • [Privacy](https://www.vmware.com/help/privacy.html) • [Trademark Guidelines](https://spring.io/trademarks)• [Thank you](https://spring.io/thank-you) • [Your California Privacy Rights](https://www.vmware.com/help/privacy/california-privacy-rights.html) • [Cookies Settings](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorized-clients.html)

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
