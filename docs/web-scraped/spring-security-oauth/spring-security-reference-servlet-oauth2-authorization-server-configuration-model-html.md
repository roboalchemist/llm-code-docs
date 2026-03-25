# Source: https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/configuration-model.html

Title: Configuration Model :: Spring Security

URL Source: https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/configuration-model.html

Markdown Content:
Configuration Model :: Spring Security
===============

[![Image 1: Spring](https://docs.spring.io/spring-security/reference/_/img/spring-logo.svg)](https://spring.io/)

[Why Spring](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/configuration-model.html#)

[Overview](https://spring.io/why-spring)[Microservices](https://spring.io/microservices)[Reactive](https://spring.io/reactive)[Event Driven](https://spring.io/event-driven)[Cloud](https://spring.io/cloud)[Web Applications](https://spring.io/web-applications)[Serverless](https://spring.io/serverless)[Batch](https://spring.io/batch)

[Learn](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/configuration-model.html#)

[Overview](https://spring.io/learn)[Quickstart](https://spring.io/quickstart)[Guides](https://spring.io/guides)[Blog](https://spring.io/blog)

[Projects](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/configuration-model.html#)

[Overview](https://spring.io/projects)[Spring Boot](https://spring.io/projects/spring-boot)[Spring Framework](https://spring.io/projects/spring-framework)[Spring Cloud](https://spring.io/projects/spring-cloud)[Spring Cloud Data Flow](https://spring.io/projects/spring-cloud-dataflow)[Spring Data](https://spring.io/projects/spring-data)[Spring Integration](https://spring.io/projects/spring-integration)[Spring Batch](https://spring.io/projects/spring-batch)[Spring Security](https://spring.io/projects/spring-security)[View all projects](https://spring.io/projects)*   DEVELOPMENT TOOLS
[Spring Tools 4](https://spring.io/tools)[Spring Initializr](https://start.spring.io/)

[Academy](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/configuration-model.html#)

[Courses](https://spring.academy/courses)[Get Certified](https://spring.academy/learning-path)

[Solutions](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/configuration-model.html#)

[Overview](https://spring.io/solutions)[Spring Runtime](https://spring.io/support)[Spring Consulting](https://spring.io/consulting)[Spring Academy For Teams](https://spring.academy/teams)[Security Advisories](https://spring.io/security)

[Community](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/configuration-model.html#)

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

### Configuration Model

*   [Default configuration](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/configuration-model.html#oauth2AuthorizationServer-default-configuration)
*   [Customizing the configuration](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/configuration-model.html#oauth2AuthorizationServer-customizing-the-configuration)
*   [Configuring Authorization Server Settings](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/configuration-model.html#oauth2AuthorizationServer-configuring-authorization-server-settings)
*   [Configuring Client Authentication](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/configuration-model.html#oauth2AuthorizationServer-configuring-client-authentication)
*   [Customizing Jwt Client Assertion Validation](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/configuration-model.html#oauth2AuthorizationServer-customizing-jwt-client-assertion-validation)
*   [Customizing Mutual-TLS Client Authentication](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/configuration-model.html#oauth2AuthorizationServer-customizing-mutual-tls-client-authentication)

[Edit this Page](https://github.com/spring-projects/spring-security/blob/7.0.3/docs/modules/ROOT/pages/servlet/oauth2/authorization-server/configuration-model.adoc)[GitHub Project](https://github.com/spring-projects/spring-security "GitHub")[Stack Overflow](https://stackoverflow.com/tags/spring-security)

*   [Spring Security](https://docs.spring.io/spring-security/reference/index.html)
*   [Servlet Applications](https://docs.spring.io/spring-security/reference/servlet/index.html)
*   [OAuth2](https://docs.spring.io/spring-security/reference/servlet/oauth2/index.html)
*   [OAuth2 Authorization Server](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/index.html)
*   [Configuration Model](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/configuration-model.html)

Configuration Model
===================

### Configuration Model

*   [Default configuration](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/configuration-model.html#oauth2AuthorizationServer-default-configuration)
*   [Customizing the configuration](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/configuration-model.html#oauth2AuthorizationServer-customizing-the-configuration)
*   [Configuring Authorization Server Settings](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/configuration-model.html#oauth2AuthorizationServer-configuring-authorization-server-settings)
*   [Configuring Client Authentication](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/configuration-model.html#oauth2AuthorizationServer-configuring-client-authentication)
*   [Customizing Jwt Client Assertion Validation](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/configuration-model.html#oauth2AuthorizationServer-customizing-jwt-client-assertion-validation)
*   [Customizing Mutual-TLS Client Authentication](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/configuration-model.html#oauth2AuthorizationServer-customizing-mutual-tls-client-authentication)

[](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/configuration-model.html#oauth2AuthorizationServer-default-configuration)Default configuration
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

`OAuth2AuthorizationServerConfiguration` is a `@Configuration` that provides the minimal default configuration for an OAuth2 authorization server.

`OAuth2AuthorizationServerConfiguration` uses [`OAuth2AuthorizationServerConfigurer`](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/configuration-model.html#oauth2AuthorizationServer-customizing-the-configuration) to apply the default configuration and registers a `SecurityFilterChain``@Bean` composed of all the infrastructure components supporting an OAuth2 authorization server.

The OAuth2 authorization server `SecurityFilterChain``@Bean` is configured with the following default protocol endpoints:

*   [OAuth2 Authorization endpoint](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/protocol-endpoints.html#oauth2AuthorizationServer-oauth2-authorization-endpoint)

*   [OAuth2 Token endpoint](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/protocol-endpoints.html#oauth2AuthorizationServer-oauth2-token-endpoint)

*   [OAuth2 Token Introspection endpoint](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/protocol-endpoints.html#oauth2AuthorizationServer-oauth2-token-introspection-endpoint)

*   [OAuth2 Token Revocation endpoint](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/protocol-endpoints.html#oauth2AuthorizationServer-oauth2-token-revocation-endpoint)

*   [OAuth2 Authorization Server Metadata endpoint](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/protocol-endpoints.html#oauth2AuthorizationServer-oauth2-authorization-server-metadata-endpoint)

*   [JWK Set endpoint](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/protocol-endpoints.html#oauth2AuthorizationServer-jwk-set-endpoint)

The JWK Set endpoint is configured **only** if a `JWKSource<SecurityContext>``@Bean` is registered.

The following protocol endpoints are disabled by default:

*   [OAuth2 Device Authorization Endpoint](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/protocol-endpoints.html#oauth2AuthorizationServer-oauth2-device-authorization-endpoint)

*   [OAuth2 Device Verification Endpoint](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/protocol-endpoints.html#oauth2AuthorizationServer-oauth2-device-verification-endpoint)

*   [OAuth2 Client Registration endpoint](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/protocol-endpoints.html#oauth2AuthorizationServer-oauth2-client-registration-endpoint)

The following example shows how to use `OAuth2AuthorizationServerConfiguration` to apply the minimal default configuration:

```java
@Configuration
@Import(OAuth2AuthorizationServerConfiguration.class)
public class AuthorizationServerConfig {

	@Bean
	public RegisteredClientRepository registeredClientRepository() {
		List<RegisteredClient> registrations = ...
		return new InMemoryRegisteredClientRepository(registrations);
	}

	@Bean
	public JWKSource<SecurityContext> jwkSource() {
		RSAKey rsaKey = ...
		JWKSet jwkSet = new JWKSet(rsaKey);
		return (jwkSelector, securityContext) -> jwkSelector.select(jwkSet);
	}

}
```

Copied!

The [authorization_code grant](https://datatracker.ietf.org/doc/html/rfc6749#section-4.1) requires the resource owner to be authenticated. Therefore, a user authentication mechanism **must** be configured in addition to the default OAuth2 security configuration.

[OpenID Connect 1.0](https://openid.net/specs/openid-connect-core-1_0.html) is disabled in the default configuration. The following example shows how to enable OpenID Connect 1.0 by initializing the `OidcConfigurer`:

```java
@Bean
public SecurityFilterChain authorizationServerSecurityFilterChain(HttpSecurity http) throws Exception {
	http
		.oauth2AuthorizationServer((authorizationServer) ->
			authorizationServer
				.oidc(Customizer.withDefaults())	// Initialize `OidcConfigurer`
		);
	return http.build();
}
```

Copied!

In addition to the default protocol endpoints, the OAuth2 authorization server `SecurityFilterChain``@Bean` is configured with the following OpenID Connect 1.0 protocol endpoints:

*   [OpenID Connect 1.0 Provider Configuration endpoint](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/protocol-endpoints.html#oauth2AuthorizationServer-oidc-provider-configuration-endpoint)

*   [OpenID Connect 1.0 Logout endpoint](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/protocol-endpoints.html#oauth2AuthorizationServer-oidc-logout-endpoint)

*   [OpenID Connect 1.0 UserInfo endpoint](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/protocol-endpoints.html#oauth2AuthorizationServer-oidc-user-info-endpoint)

The [OpenID Connect 1.0 Client Registration endpoint](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/protocol-endpoints.html#oauth2AuthorizationServer-oidc-client-registration-endpoint) is disabled by default.

`OAuth2AuthorizationServerConfiguration.jwtDecoder(JWKSource<SecurityContext>)` is a convenience (`static`) utility method that can be used to register a `JwtDecoder``@Bean`, which is **REQUIRED** for the [OpenID Connect 1.0 UserInfo endpoint](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/protocol-endpoints.html#oauth2AuthorizationServer-oidc-user-info-endpoint) and the [OpenID Connect 1.0 Client Registration endpoint](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/protocol-endpoints.html#oauth2AuthorizationServer-oidc-client-registration-endpoint).

The following example shows how to register a `JwtDecoder``@Bean`:

```java
@Bean
public JwtDecoder jwtDecoder(JWKSource<SecurityContext> jwkSource) {
	return OAuth2AuthorizationServerConfiguration.jwtDecoder(jwkSource);
}
```

Copied!

The main intent of `OAuth2AuthorizationServerConfiguration` is to provide a convenient method to apply the minimal default configuration for an OAuth2 authorization server. However, in most cases, customizing the configuration will be required.

[](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/configuration-model.html#oauth2AuthorizationServer-customizing-the-configuration)Customizing the configuration
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

`OAuth2AuthorizationServerConfigurer` provides the ability to fully customize the security configuration for an OAuth2 authorization server. It lets you specify the core components to use - for example, [`RegisteredClientRepository`](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/core-model-components.html#oauth2AuthorizationServer-registered-client-repository), [`OAuth2AuthorizationService`](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/core-model-components.html#oauth2AuthorizationServer-oauth2-authorization-service), [`OAuth2TokenGenerator`](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/core-model-components.html#oauth2AuthorizationServer-oauth2-token-generator), and others. Furthermore, it lets you customize the request processing logic for the protocol endpoints – for example, [authorization endpoint](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/protocol-endpoints.html#oauth2AuthorizationServer-oauth2-authorization-endpoint), [device authorization endpoint](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/protocol-endpoints.html#oauth2AuthorizationServer-oauth2-device-authorization-endpoint), [device verification endpoint](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/protocol-endpoints.html#oauth2AuthorizationServer-oauth2-device-verification-endpoint), [token endpoint](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/protocol-endpoints.html#oauth2AuthorizationServer-oauth2-token-endpoint), [token introspection endpoint](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/protocol-endpoints.html#oauth2AuthorizationServer-oauth2-token-introspection-endpoint), and others.

`OAuth2AuthorizationServerConfigurer` provides the following configuration options:

```java
@Bean
public SecurityFilterChain authorizationServerSecurityFilterChain(HttpSecurity http) throws Exception {
	http
		.oauth2AuthorizationServer((authorizationServer) ->
			authorizationServer
				.registeredClientRepository(registeredClientRepository)	(1)
				.authorizationService(authorizationService)	(2)
				.authorizationConsentService(authorizationConsentService)	(3)
				.authorizationServerSettings(authorizationServerSettings)	(4)
				.tokenGenerator(tokenGenerator)	(5)
				.clientAuthentication(clientAuthentication -> { })	(6)
				.authorizationEndpoint(authorizationEndpoint -> { })	(7)
				.pushedAuthorizationRequestEndpoint(pushedAuthorizationRequestEndpoint -> { })  (8)
				.deviceAuthorizationEndpoint(deviceAuthorizationEndpoint -> { })	(9)
				.deviceVerificationEndpoint(deviceVerificationEndpoint -> { })	(10)
				.tokenEndpoint(tokenEndpoint -> { })	(11)
				.tokenIntrospectionEndpoint(tokenIntrospectionEndpoint -> { })	(12)
				.tokenRevocationEndpoint(tokenRevocationEndpoint -> { })	(13)
				.clientRegistrationEndpoint(clientRegistrationEndpoint -> { })  (14)
				.authorizationServerMetadataEndpoint(authorizationServerMetadataEndpoint -> { })	(15)
				.oidc(oidc -> oidc
					.providerConfigurationEndpoint(providerConfigurationEndpoint -> { })	(16)
					.logoutEndpoint(logoutEndpoint -> { })	(17)
					.userInfoEndpoint(userInfoEndpoint -> { })	(18)
					.clientRegistrationEndpoint(clientRegistrationEndpoint -> { })	(19)
				)
		);

	return http.build();
}
```

Copied!

**1**`registeredClientRepository()`: The [`RegisteredClientRepository`](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/core-model-components.html#oauth2AuthorizationServer-registered-client-repository) (**REQUIRED**) for managing new and existing clients.
**2**`authorizationService()`: The [`OAuth2AuthorizationService`](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/core-model-components.html#oauth2AuthorizationServer-oauth2-authorization-service) for managing new and existing authorizations.
**3**`authorizationConsentService()`: The [`OAuth2AuthorizationConsentService`](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/core-model-components.html#oauth2AuthorizationServer-oauth2-authorization-consent-service) for managing new and existing authorization consents.
**4**`authorizationServerSettings()`: The [`AuthorizationServerSettings`](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/configuration-model.html#oauth2AuthorizationServer-configuring-authorization-server-settings) (**REQUIRED**) for customizing configuration settings for the OAuth2 authorization server.
**5**`tokenGenerator()`: The [`OAuth2TokenGenerator`](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/core-model-components.html#oauth2AuthorizationServer-oauth2-token-generator) for generating tokens supported by the OAuth2 authorization server.
**6**`clientAuthentication()`: The configurer for [OAuth2 Client Authentication](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/configuration-model.html#oauth2AuthorizationServer-configuring-client-authentication).
**7**`authorizationEndpoint()`: The configurer for the [OAuth2 Authorization endpoint](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/protocol-endpoints.html#oauth2AuthorizationServer-oauth2-authorization-endpoint).
**8**`pushedAuthorizationRequestEndpoint()`: The configurer for the [OAuth2 Pushed Authorization Request endpoint](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/protocol-endpoints.html#oauth2AuthorizationServer-oauth2-pushed-authorization-request-endpoint).
**9**`deviceAuthorizationEndpoint()`: The configurer for the [OAuth2 Device Authorization endpoint](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/protocol-endpoints.html#oauth2AuthorizationServer-oauth2-device-authorization-endpoint).
**10**`deviceVerificationEndpoint()`: The configurer for the [OAuth2 Device Verification endpoint](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/protocol-endpoints.html#oauth2AuthorizationServer-oauth2-device-verification-endpoint).
**11**`tokenEndpoint()`: The configurer for the [OAuth2 Token endpoint](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/protocol-endpoints.html#oauth2AuthorizationServer-oauth2-token-endpoint).
**12**`tokenIntrospectionEndpoint()`: The configurer for the [OAuth2 Token Introspection endpoint](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/protocol-endpoints.html#oauth2AuthorizationServer-oauth2-token-introspection-endpoint).
**13**`tokenRevocationEndpoint()`: The configurer for the [OAuth2 Token Revocation endpoint](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/protocol-endpoints.html#oauth2AuthorizationServer-oauth2-token-revocation-endpoint).
**14**`clientRegistrationEndpoint()`: The configurer for the [OAuth2 Client Registration endpoint](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/protocol-endpoints.html#oauth2AuthorizationServer-oauth2-client-registration-endpoint).
**15**`authorizationServerMetadataEndpoint()`: The configurer for the [OAuth2 Authorization Server Metadata endpoint](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/protocol-endpoints.html#oauth2AuthorizationServer-oauth2-authorization-server-metadata-endpoint).
**16**`providerConfigurationEndpoint()`: The configurer for the [OpenID Connect 1.0 Provider Configuration endpoint](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/protocol-endpoints.html#oauth2AuthorizationServer-oidc-provider-configuration-endpoint).
**17**`logoutEndpoint()`: The configurer for the [OpenID Connect 1.0 Logout endpoint](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/protocol-endpoints.html#oauth2AuthorizationServer-oidc-logout-endpoint).
**18**`userInfoEndpoint()`: The configurer for the [OpenID Connect 1.0 UserInfo endpoint](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/protocol-endpoints.html#oauth2AuthorizationServer-oidc-user-info-endpoint).
**19**`clientRegistrationEndpoint()`: The configurer for the [OpenID Connect 1.0 Client Registration endpoint](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/protocol-endpoints.html#oauth2AuthorizationServer-oidc-client-registration-endpoint).

[](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/configuration-model.html#oauth2AuthorizationServer-configuring-authorization-server-settings)Configuring Authorization Server Settings
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

`AuthorizationServerSettings` contains the configuration settings for the OAuth2 authorization server. It specifies the `URI` for the protocol endpoints as well as the [issuer identifier](https://datatracker.ietf.org/doc/html/rfc8414#section-2). The default `URI` for the protocol endpoints are as follows:

```java
public final class AuthorizationServerSettings extends AbstractSettings {

	...

	public static Builder builder() {
		return new Builder()
			.authorizationEndpoint("/oauth2/authorize")
			.pushedAuthorizationRequestEndpoint("/oauth2/par")
			.deviceAuthorizationEndpoint("/oauth2/device_authorization")
			.deviceVerificationEndpoint("/oauth2/device_verification")
			.tokenEndpoint("/oauth2/token")
			.tokenIntrospectionEndpoint("/oauth2/introspect")
			.tokenRevocationEndpoint("/oauth2/revoke")
			.clientRegistrationEndpoint("/oauth2/register")
			.jwkSetEndpoint("/oauth2/jwks")
			.oidcLogoutEndpoint("/connect/logout")
			.oidcUserInfoEndpoint("/userinfo")
			.oidcClientRegistrationEndpoint("/connect/register");
	}

	...

}
```

Copied!

`AuthorizationServerSettings` is a **REQUIRED** component.

[`@Import(OAuth2AuthorizationServerConfiguration.class)`](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/configuration-model.html#oauth2AuthorizationServer-default-configuration) automatically registers an `AuthorizationServerSettings``@Bean`, if not already provided.

The following example shows how to customize the configuration settings and register an `AuthorizationServerSettings``@Bean`:

```java
@Bean
public AuthorizationServerSettings authorizationServerSettings() {
	return AuthorizationServerSettings.builder()
		.issuer("https://example.com")
		.authorizationEndpoint("/oauth2/v1/authorize")
		.pushedAuthorizationRequestEndpoint("/oauth2/v1/par")
		.deviceAuthorizationEndpoint("/oauth2/v1/device_authorization")
		.deviceVerificationEndpoint("/oauth2/v1/device_verification")
		.tokenEndpoint("/oauth2/v1/token")
		.tokenIntrospectionEndpoint("/oauth2/v1/introspect")
		.tokenRevocationEndpoint("/oauth2/v1/revoke")
		.clientRegistrationEndpoint("/oauth2/v1/register")
		.jwkSetEndpoint("/oauth2/v1/jwks")
		.oidcLogoutEndpoint("/connect/v1/logout")
		.oidcUserInfoEndpoint("/connect/v1/userinfo")
		.oidcClientRegistrationEndpoint("/connect/v1/register")
		.build();
}
```

Copied!

The `AuthorizationServerContext` is a context object that holds information of the Authorization Server runtime environment. It provides access to the `AuthorizationServerSettings` and the “current” issuer identifier.

If the issuer identifier is not configured in `AuthorizationServerSettings.builder().issuer(String)`, it is resolved from the current request.

The `AuthorizationServerContext` is accessible through the `AuthorizationServerContextHolder`, which associates it with the current request thread by using a `ThreadLocal`.

[](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/configuration-model.html#oauth2AuthorizationServer-configuring-client-authentication)Configuring Client Authentication
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

`OAuth2ClientAuthenticationConfigurer` provides the ability to customize [OAuth2 client authentication](https://datatracker.ietf.org/doc/html/rfc6749#section-2.3). It defines extension points that let you customize the pre-processing, main processing, and post-processing logic for client authentication requests.

`OAuth2ClientAuthenticationConfigurer` provides the following configuration options:

```java
@Bean
public SecurityFilterChain authorizationServerSecurityFilterChain(HttpSecurity http) throws Exception {
	http
		.oauth2AuthorizationServer((authorizationServer) ->
			authorizationServer
				.clientAuthentication(clientAuthentication ->
					clientAuthentication
						.authenticationConverter(authenticationConverter)	(1)
						.authenticationConverters(authenticationConvertersConsumer)	(2)
						.authenticationProvider(authenticationProvider)	(3)
						.authenticationProviders(authenticationProvidersConsumer)	(4)
						.authenticationSuccessHandler(authenticationSuccessHandler)	(5)
						.errorResponseHandler(errorResponseHandler)	(6)
				)
		);

	return http.build();
}
```

Copied!

**1**`authenticationConverter()`: Adds an `AuthenticationConverter` (_pre-processor_) used when attempting to extract client credentials from `HttpServletRequest` to an instance of `OAuth2ClientAuthenticationToken`.
**2**`authenticationConverters()`: Sets the `Consumer` providing access to the `List` of default and (optionally) added `AuthenticationConverter`'s allowing the ability to add, remove, or customize a specific `AuthenticationConverter`.
**3**`authenticationProvider()`: Adds an `AuthenticationProvider` (_main processor_) used for authenticating the `OAuth2ClientAuthenticationToken`.
**4**`authenticationProviders()`: Sets the `Consumer` providing access to the `List` of default and (optionally) added `AuthenticationProvider`'s allowing the ability to add, remove, or customize a specific `AuthenticationProvider`.
**5**`authenticationSuccessHandler()`: The `AuthenticationSuccessHandler` (_post-processor_) used for handling a successful client authentication and associating the `OAuth2ClientAuthenticationToken` to the `SecurityContext`.
**6**`errorResponseHandler()`: The `AuthenticationFailureHandler` (_post-processor_) used for handling a failed client authentication and returning the [`OAuth2Error` response](https://datatracker.ietf.org/doc/html/rfc6749#section-5.2).

`OAuth2ClientAuthenticationConfigurer` configures the `OAuth2ClientAuthenticationFilter` and registers it with the OAuth2 authorization server `SecurityFilterChain``@Bean`. `OAuth2ClientAuthenticationFilter` is the `Filter` that processes client authentication requests.

By default, client authentication is required for the [OAuth2 Token endpoint](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/protocol-endpoints.html#oauth2AuthorizationServer-oauth2-token-endpoint), the [OAuth2 Token Introspection endpoint](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/protocol-endpoints.html#oauth2AuthorizationServer-oauth2-token-introspection-endpoint), and the [OAuth2 Token Revocation endpoint](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/protocol-endpoints.html#oauth2AuthorizationServer-oauth2-token-revocation-endpoint). The supported client authentication methods are `client_secret_basic`, `client_secret_post`, `private_key_jwt`, `client_secret_jwt`, `tls_client_auth`, `self_signed_tls_client_auth`, and `none` (public clients).

`OAuth2ClientAuthenticationFilter` is configured with the following defaults:

*   `AuthenticationConverter` — A `DelegatingAuthenticationConverter` composed of `JwtClientAssertionAuthenticationConverter`, `X509ClientCertificateAuthenticationConverter`, `ClientSecretBasicAuthenticationConverter`, `ClientSecretPostAuthenticationConverter`, and `PublicClientAuthenticationConverter`.

*   `AuthenticationManager` — An `AuthenticationManager` composed of `JwtClientAssertionAuthenticationProvider`, `X509ClientCertificateAuthenticationProvider`, `ClientSecretAuthenticationProvider`, and `PublicClientAuthenticationProvider`.

*   `AuthenticationSuccessHandler` — An internal implementation that associates the “authenticated” `OAuth2ClientAuthenticationToken` (current `Authentication`) to the `SecurityContext`.

*   `AuthenticationFailureHandler` — An internal implementation that uses the `OAuth2Error` associated with the `OAuth2AuthenticationException` to return the OAuth2 error response.

### [](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/configuration-model.html#oauth2AuthorizationServer-customizing-jwt-client-assertion-validation)Customizing Jwt Client Assertion Validation

`JwtClientAssertionDecoderFactory.DEFAULT_JWT_VALIDATOR_FACTORY` is the default factory that provides an `OAuth2TokenValidator<Jwt>` for the specified `RegisteredClient` and is used for validating the `iss`, `sub`, `aud`, `exp` and `nbf` claims of the `Jwt` client assertion.

`JwtClientAssertionDecoderFactory` provides the ability to override the default `Jwt` client assertion validation by supplying a custom factory of type `Function<RegisteredClient, OAuth2TokenValidator<Jwt>>` to `setJwtValidatorFactory()`.

`JwtClientAssertionDecoderFactory` is the default `JwtDecoderFactory` used by `JwtClientAssertionAuthenticationProvider` that provides a `JwtDecoder` for the specified `RegisteredClient` and is used for authenticating a `Jwt` Bearer Token during OAuth2 client authentication.

A common use case for customizing `JwtClientAssertionDecoderFactory` is to validate additional claims in the `Jwt` client assertion.

The following example shows how to configure `JwtClientAssertionAuthenticationProvider` with a customized `JwtClientAssertionDecoderFactory` that validates an additional claim in the `Jwt` client assertion:

```java
@Bean
public SecurityFilterChain authorizationServerSecurityFilterChain(HttpSecurity http) throws Exception {
	http
		.oauth2AuthorizationServer((authorizationServer) ->
			authorizationServer
				.clientAuthentication(clientAuthentication ->
					clientAuthentication
						.authenticationProviders(configureJwtClientAssertionValidator())
				)
		);

	return http.build();
}

private Consumer<List<AuthenticationProvider>> configureJwtClientAssertionValidator() {
	return (authenticationProviders) ->
		authenticationProviders.forEach((authenticationProvider) -> {
			if (authenticationProvider instanceof JwtClientAssertionAuthenticationProvider) {
				// Customize JwtClientAssertionDecoderFactory
				JwtClientAssertionDecoderFactory jwtDecoderFactory = new JwtClientAssertionDecoderFactory();
				Function<RegisteredClient, OAuth2TokenValidator<Jwt>> jwtValidatorFactory = (registeredClient) ->
					new DelegatingOAuth2TokenValidator<>(
						// Use default validators
						JwtClientAssertionDecoderFactory.DEFAULT_JWT_VALIDATOR_FACTORY.apply(registeredClient),
						// Add custom validator
						new JwtClaimValidator<>("claim", "value"::equals));
				jwtDecoderFactory.setJwtValidatorFactory(jwtValidatorFactory);

				((JwtClientAssertionAuthenticationProvider) authenticationProvider)
					.setJwtDecoderFactory(jwtDecoderFactory);
			}
		});
}
```

Copied!

### [](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/configuration-model.html#oauth2AuthorizationServer-customizing-mutual-tls-client-authentication)Customizing Mutual-TLS Client Authentication

`X509ClientCertificateAuthenticationProvider` is used for authenticating the client `X509Certificate` chain received when `ClientAuthenticationMethod.TLS_CLIENT_AUTH` or `ClientAuthenticationMethod.SELF_SIGNED_TLS_CLIENT_AUTH` method is used during OAuth2 client authentication. It is also composed with a _"Certificate Verifier"_, which is used to verify the contents of the client `X509Certificate` after the TLS handshake has successfully completed.

#### [](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/configuration-model.html#oauth2AuthorizationServer-customizing-mutual-tls-client-authentication-pki-mutual-tls-method)PKI Mutual-TLS Method

For the PKI Mutual-TLS (`ClientAuthenticationMethod.TLS_CLIENT_AUTH`) method, the default implementation of the certificate verifier verifies the subject distinguished name of the client `X509Certificate` against the setting `RegisteredClient.getClientSettings.getX509CertificateSubjectDN()`.

If you need to verify another attribute of the client `X509Certificate`, for example, a Subject Alternative Name (SAN) entry, the following example shows how to configure `X509ClientCertificateAuthenticationProvider` with a custom implementation of a certificate verifier:

```java
@Bean
public SecurityFilterChain authorizationServerSecurityFilterChain(HttpSecurity http) throws Exception {
	http
		.oauth2AuthorizationServer((authorizationServer) ->
			authorizationServer
				.clientAuthentication(clientAuthentication ->
					clientAuthentication
						.authenticationProviders(configureX509ClientCertificateVerifier())
				)
		);

	return http.build();
}

private Consumer<List<AuthenticationProvider>> configureX509ClientCertificateVerifier() {
	return (authenticationProviders) ->
			authenticationProviders.forEach((authenticationProvider) -> {
				if (authenticationProvider instanceof X509ClientCertificateAuthenticationProvider) {
					Consumer<OAuth2ClientAuthenticationContext> certificateVerifier = (clientAuthenticationContext) -> {
						OAuth2ClientAuthenticationToken clientAuthentication = clientAuthenticationContext.getAuthentication();
						RegisteredClient registeredClient = clientAuthenticationContext.getRegisteredClient();
						X509Certificate[] clientCertificateChain = (X509Certificate[]) clientAuthentication.getCredentials();
						X509Certificate clientCertificate = clientCertificateChain[0];

						// TODO Verify Subject Alternative Name (SAN) entry

					};

					((X509ClientCertificateAuthenticationProvider) authenticationProvider)
							.setCertificateVerifier(certificateVerifier);
				}
			});
}
```

Copied!

#### [](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/configuration-model.html#oauth2AuthorizationServer-customizing-mutual-tls-client-authentication-self-signed-certificate-mutual-tls-method)Self-Signed Certificate Mutual-TLS Method

For the Self-Signed Certificate Mutual-TLS (`ClientAuthenticationMethod.SELF_SIGNED_TLS_CLIENT_AUTH`) method, the default implementation of the certificate verifier will retrieve the client’s JSON Web Key Set using the setting `RegisteredClient.getClientSettings.getJwkSetUrl()` and expect to find a match against the client `X509Certificate` received during the TLS handshake.

The `RegisteredClient.getClientSettings.getJwkSetUrl()` setting is used to retrieve the client’s certificates via a JSON Web Key (JWK) Set. A certificate is represented with the `x5c` parameter of an individual JWK within the set.

#### [](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/configuration-model.html#oauth2AuthorizationServer-customizing-mutual-tls-client-authentication-client-certificate-bound-access-tokens)Client Certificate-Bound Access Tokens

When Mutual-TLS client authentication is used at the token endpoint, the authorization server is able to bind the issued access token to the client’s `X509Certificate`. The binding is accomplished by computing the SHA-256 thumbprint of the client’s `X509Certificate` and associating the thumbprint with the access token. For example, a JWT access token would include a `x5t#S256` claim, containing the `X509Certificate` thumbprint, within the top-level `cnf` (confirmation method) claim.

Binding the access token to the client’s `X509Certificate` provides the ability to implement a proof-of-possession mechanism during protected resource access. For example, the protected resource would obtain the client’s `X509Certificate` used during Mutual-TLS authentication and then verify that the certificate thumbprint matches the `x5t#S256` claim associated with the access token.

The following example shows how to enable certificate-bound access tokens for a client:

```java
RegisteredClient mtlsClient = RegisteredClient.withId(UUID.randomUUID().toString())
		.clientId("mtls-client")
		.clientAuthenticationMethod(ClientAuthenticationMethod.TLS_CLIENT_AUTH)
		.authorizationGrantType(AuthorizationGrantType.CLIENT_CREDENTIALS)
		.scope("scope-a")
		.clientSettings(
				ClientSettings.builder()
						.x509CertificateSubjectDN("CN=mtls-client,OU=Spring Samples,O=Spring,C=US")
						.build()
		)
		.tokenSettings(
				TokenSettings.builder()
						.x509CertificateBoundAccessTokens(true)
						.build()
		)
		.build();
```

Copied!

*   [Spring Security](https://docs.spring.io/spring-security/reference/index.html) 

 Stable  
    *   [7.0.3](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/configuration-model.html)
    *   [6.5.8](https://docs.spring.io/spring-security/reference/6.5/index.html)

 Preview 

    *   [7.1.0-M2](https://docs.spring.io/spring-security/reference/7.1/servlet/oauth2/authorization-server/configuration-model.html)

 Snapshot 

    *   [7.1.0-SNAPSHOT](https://docs.spring.io/spring-security/reference/7.1-SNAPSHOT/servlet/oauth2/authorization-server/configuration-model.html)
    *   [7.0.4-SNAPSHOT](https://docs.spring.io/spring-security/reference/7.0-SNAPSHOT/servlet/oauth2/authorization-server/configuration-model.html)
    *   [6.5.9-SNAPSHOT](https://docs.spring.io/spring-security/reference/6.5-SNAPSHOT/index.html)

*    Related Spring Documentation 
    *   [Spring Framework](https://docs.spring.io/spring-framework/reference/)
    *   [](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/configuration-model.html)[Spring Security](https://docs.spring.io/spring-security/reference/)
        *   [Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/)
        *   [Spring LDAP](https://docs.spring.io/spring-ldap/reference/)
        *   [Spring Security Kerberos](https://docs.spring.io/spring-security-kerberos/reference/)
        *   [Spring Session](https://docs.spring.io/spring-session/reference/)
        *   [Spring Vault](https://docs.spring.io/spring-vault/reference/)

    *   [Spring GraphQL](https://docs.spring.io/spring-graphql/reference/)

[All Docs...](https://docs.spring.io/spring-security/reference/spring-projects.html)

![Image 2: Spring](https://docs.spring.io/spring-security/reference/_/img/spring-logo.svg)
Copyright © 2005 - 2026 Broadcom. All Rights Reserved. The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

[Terms of Use](https://www.vmware.com/help/legal.html) • [Privacy](https://www.vmware.com/help/privacy.html) • [Trademark Guidelines](https://spring.io/trademarks)• [Thank you](https://spring.io/thank-you) • [Your California Privacy Rights](https://www.vmware.com/help/privacy/california-privacy-rights.html) • [Cookies Settings](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/configuration-model.html)

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
