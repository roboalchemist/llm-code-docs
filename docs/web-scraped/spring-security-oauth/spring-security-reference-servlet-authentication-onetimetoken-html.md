# Source: https://docs.spring.io/spring-security/reference/servlet/authentication/onetimetoken.html

Title: One-Time Token Login :: Spring Security

URL Source: https://docs.spring.io/spring-security/reference/servlet/authentication/onetimetoken.html

Markdown Content:
One-Time Token Login :: Spring Security
===============

[![Image 1: Spring](https://docs.spring.io/spring-security/reference/_/img/spring-logo.svg)](https://spring.io/)

[Why Spring](https://docs.spring.io/spring-security/reference/servlet/authentication/onetimetoken.html#)

[Overview](https://spring.io/why-spring)[Microservices](https://spring.io/microservices)[Reactive](https://spring.io/reactive)[Event Driven](https://spring.io/event-driven)[Cloud](https://spring.io/cloud)[Web Applications](https://spring.io/web-applications)[Serverless](https://spring.io/serverless)[Batch](https://spring.io/batch)

[Learn](https://docs.spring.io/spring-security/reference/servlet/authentication/onetimetoken.html#)

[Overview](https://spring.io/learn)[Quickstart](https://spring.io/quickstart)[Guides](https://spring.io/guides)[Blog](https://spring.io/blog)

[Projects](https://docs.spring.io/spring-security/reference/servlet/authentication/onetimetoken.html#)

[Overview](https://spring.io/projects)[Spring Boot](https://spring.io/projects/spring-boot)[Spring Framework](https://spring.io/projects/spring-framework)[Spring Cloud](https://spring.io/projects/spring-cloud)[Spring Cloud Data Flow](https://spring.io/projects/spring-cloud-dataflow)[Spring Data](https://spring.io/projects/spring-data)[Spring Integration](https://spring.io/projects/spring-integration)[Spring Batch](https://spring.io/projects/spring-batch)[Spring Security](https://spring.io/projects/spring-security)[View all projects](https://spring.io/projects)*   DEVELOPMENT TOOLS
[Spring Tools 4](https://spring.io/tools)[Spring Initializr](https://start.spring.io/)

[Academy](https://docs.spring.io/spring-security/reference/servlet/authentication/onetimetoken.html#)

[Courses](https://spring.academy/courses)[Get Certified](https://spring.academy/learning-path)

[Solutions](https://docs.spring.io/spring-security/reference/servlet/authentication/onetimetoken.html#)

[Overview](https://spring.io/solutions)[Spring Runtime](https://spring.io/support)[Spring Consulting](https://spring.io/consulting)[Spring Academy For Teams](https://spring.academy/teams)[Security Advisories](https://spring.io/security)

[Community](https://docs.spring.io/spring-security/reference/servlet/authentication/onetimetoken.html#)

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

### One-Time Token Login

*   [Understanding One-Time Tokens vs. One-Time Passwords](https://docs.spring.io/spring-security/reference/servlet/authentication/onetimetoken.html#_understanding_one_time_tokens_vs_one_time_passwords)
*   [Setup Requirements](https://docs.spring.io/spring-security/reference/servlet/authentication/onetimetoken.html#_setup_requirements)
*   [Token Delivery](https://docs.spring.io/spring-security/reference/servlet/authentication/onetimetoken.html#_token_delivery)
*   [Token Generation](https://docs.spring.io/spring-security/reference/servlet/authentication/onetimetoken.html#_token_generation)
*   [Default Login Page and Default One-Time Token Submit Page](https://docs.spring.io/spring-security/reference/servlet/authentication/onetimetoken.html#default-pages)
*   [Sending the Token to the User](https://docs.spring.io/spring-security/reference/servlet/authentication/onetimetoken.html#sending-token-to-user)
*   [Changing the One-Time Token Generate URL](https://docs.spring.io/spring-security/reference/servlet/authentication/onetimetoken.html#changing-generate-url)
*   [Changing the Default Submit Page URL](https://docs.spring.io/spring-security/reference/servlet/authentication/onetimetoken.html#changing-submit-page-url)
*   [Disabling the Default Submit Page](https://docs.spring.io/spring-security/reference/servlet/authentication/onetimetoken.html#disabling-default-submit-page)
*   [Customize How to Generate and Consume One-Time Tokens](https://docs.spring.io/spring-security/reference/servlet/authentication/onetimetoken.html#customize-generate-consume-token)
*   [Customize GenerateOneTimeTokenRequest Instance](https://docs.spring.io/spring-security/reference/servlet/authentication/onetimetoken.html#customize-generate-token-request)

[Edit this Page](https://github.com/spring-projects/spring-security/blob/7.0.3/docs/modules/ROOT/pages/servlet/authentication/onetimetoken.adoc)[GitHub Project](https://github.com/spring-projects/spring-security "GitHub")[Stack Overflow](https://stackoverflow.com/tags/spring-security)

*   [Spring Security](https://docs.spring.io/spring-security/reference/index.html)
*   [Servlet Applications](https://docs.spring.io/spring-security/reference/servlet/index.html)
*   [Authentication](https://docs.spring.io/spring-security/reference/servlet/authentication/index.html)
*   [One-Time Token](https://docs.spring.io/spring-security/reference/servlet/authentication/onetimetoken.html)

One-Time Token Login
====================

### One-Time Token Login

*   [Understanding One-Time Tokens vs. One-Time Passwords](https://docs.spring.io/spring-security/reference/servlet/authentication/onetimetoken.html#_understanding_one_time_tokens_vs_one_time_passwords)
*   [Setup Requirements](https://docs.spring.io/spring-security/reference/servlet/authentication/onetimetoken.html#_setup_requirements)
*   [Token Delivery](https://docs.spring.io/spring-security/reference/servlet/authentication/onetimetoken.html#_token_delivery)
*   [Token Generation](https://docs.spring.io/spring-security/reference/servlet/authentication/onetimetoken.html#_token_generation)
*   [Default Login Page and Default One-Time Token Submit Page](https://docs.spring.io/spring-security/reference/servlet/authentication/onetimetoken.html#default-pages)
*   [Sending the Token to the User](https://docs.spring.io/spring-security/reference/servlet/authentication/onetimetoken.html#sending-token-to-user)
*   [Changing the One-Time Token Generate URL](https://docs.spring.io/spring-security/reference/servlet/authentication/onetimetoken.html#changing-generate-url)
*   [Changing the Default Submit Page URL](https://docs.spring.io/spring-security/reference/servlet/authentication/onetimetoken.html#changing-submit-page-url)
*   [Disabling the Default Submit Page](https://docs.spring.io/spring-security/reference/servlet/authentication/onetimetoken.html#disabling-default-submit-page)
*   [Customize How to Generate and Consume One-Time Tokens](https://docs.spring.io/spring-security/reference/servlet/authentication/onetimetoken.html#customize-generate-consume-token)
*   [Customize GenerateOneTimeTokenRequest Instance](https://docs.spring.io/spring-security/reference/servlet/authentication/onetimetoken.html#customize-generate-token-request)

Spring Security offers support for One-Time Token (OTT) authentication via the `oneTimeTokenLogin()` DSL. Before diving into implementation details, it’s important to clarify the scope of the OTT feature within the framework, highlighting what is supported and what isn’t.

[](https://docs.spring.io/spring-security/reference/servlet/authentication/onetimetoken.html#_understanding_one_time_tokens_vs_one_time_passwords)Understanding One-Time Tokens vs. One-Time Passwords
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

It’s common to confuse One-Time Tokens (OTT) with [One-Time Passwords](https://en.wikipedia.org/wiki/One-time_password) (OTP), but in Spring Security, these concepts differ in several key ways. For clarity, we’ll assume OTP refers to [TOTP](https://en.wikipedia.org/wiki/Time-based_one-time_password) (Time-Based One-Time Password) or [HOTP](https://en.wikipedia.org/wiki/HMAC-based_one-time_password) (HMAC-Based One-Time Password).

### [](https://docs.spring.io/spring-security/reference/servlet/authentication/onetimetoken.html#_setup_requirements)Setup Requirements

*   OTT: No initial setup is required. The user doesn’t need to configure anything in advance.

*   OTP: Typically requires setup, such as generating and sharing a secret key with an external tool to produce the one-time passwords.

### [](https://docs.spring.io/spring-security/reference/servlet/authentication/onetimetoken.html#_token_delivery)Token Delivery

*   OTT: Usually a custom [`OneTimeTokenGenerationSuccessHandler`](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/authentication/ott/OneTimeTokenGenerationSuccessHandler.html) must be implemented, responsible for delivering the token to the end user.

*   OTP: The token is often generated by an external tool, so there’s no need to send it to the user via the application.

### [](https://docs.spring.io/spring-security/reference/servlet/authentication/onetimetoken.html#_token_generation)Token Generation

*   OTT: The [`OneTimeTokenService.generate(GenerateOneTimeTokenRequest)`](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/authentication/ott/OneTimeTokenService.html#generate(org.springframework.security.authentication.ott.GenerateOneTimeTokenRequest)) method requires a [`OneTimeToken`](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/authentication/ott/OneTimeToken.html) to be returned, emphasizing server-side generation.

*   OTP: The token is not necessarily generated on the server side, it’s often created by the client using the shared secret.

In summary, One-Time Tokens (OTT) provide a way to authenticate users without additional account setup, differentiating them from One-Time Passwords (OTP), which typically involve a more complex setup process and rely on external tools for token generation.

The One-Time Token Login works in two major steps.

1.   User requests a token by submitting their user identifier, usually the username, and the token is delivered to them, often as a Magic Link, via e-mail, SMS, etc.

2.   User submits the token to the one-time token login endpoint and, if valid, the user gets logged in.

In the following sections we will explore how to configure OTT Login for your needs.

*   [Understanding the integration with the default generated login page](https://docs.spring.io/spring-security/reference/servlet/authentication/onetimetoken.html#default-pages)

*   [Sending the token to the user](https://docs.spring.io/spring-security/reference/servlet/authentication/onetimetoken.html#sending-token-to-user)

*   [Configuring the One-Time Token submit page](https://docs.spring.io/spring-security/reference/servlet/authentication/onetimetoken.html#changing-submit-page-url)

*   [Changing the One-Time Token generate URL](https://docs.spring.io/spring-security/reference/servlet/authentication/onetimetoken.html#changing-generate-url)

*   [Customize how to generate and consume tokens](https://docs.spring.io/spring-security/reference/servlet/authentication/onetimetoken.html#customize-generate-consume-token)

[](https://docs.spring.io/spring-security/reference/servlet/authentication/onetimetoken.html#default-pages)Default Login Page and Default One-Time Token Submit Page
--------------------------------------------------------------------------------------------------------------------------------------------------------------------

When the `oneTimeTokenLogin()` DSL is used, by default the One-Time Token Login Page is auto-generated by the org.springframework.security.web.authentication.ui:DefaultLoginPageGeneratingFilter[]. The DSL will also set up the [`DefaultOneTimeTokenSubmitPageGeneratingFilter`](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/authentication/ui/DefaultOneTimeTokenSubmitPageGeneratingFilter.html) to generate a default One-Time Token submit page.

[](https://docs.spring.io/spring-security/reference/servlet/authentication/onetimetoken.html#sending-token-to-user)Sending the Token to the User
------------------------------------------------------------------------------------------------------------------------------------------------

It is not possible for Spring Security to reasonably determine the way the token should be delivered to your users. Therefore, a custom [`OneTimeTokenGenerationSuccessHandler`](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/authentication/ott/OneTimeTokenGenerationSuccessHandler.html) must be provided to deliver the token to the user based on your needs. One of the most common delivery strategies is a Magic Link, via e-mail, SMS, etc. In the following example, we are going to create a magic link and sent it to the user’s email.

One-Time Token Login Configuration

*   Java

*   Kotlin

```java
@Configuration
@EnableWebSecurity
public class SecurityConfig {

    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) {
        http
            // ...
            .formLogin(Customizer.withDefaults())
            .oneTimeTokenLogin(Customizer.withDefaults());
        return http.build();
    }

}

import org.springframework.mail.SimpleMailMessage;
import org.springframework.mail.javamail.JavaMailSender;

@Component (1)
public class MagicLinkOneTimeTokenGenerationSuccessHandler implements OneTimeTokenGenerationSuccessHandler {

    private final MailSender mailSender;

    private final OneTimeTokenGenerationSuccessHandler redirectHandler = new RedirectOneTimeTokenGenerationSuccessHandler("/ott/sent");

    // constructor omitted

    @Override
    public void handle(HttpServletRequest request, HttpServletResponse response, OneTimeToken oneTimeToken) throws IOException, ServletException {
        UriComponentsBuilder builder = UriComponentsBuilder.fromHttpUrl(UrlUtils.buildFullRequestUrl(request))
                .replacePath(request.getContextPath())
                .replaceQuery(null)
                .fragment(null)
                .path("/login/ott")
                .queryParam("token", oneTimeToken.getTokenValue()); (2)
        String magicLink = builder.toUriString();
        String email = getUserEmail(oneTimeToken.getUsername()); (3)
        this.mailSender.send(email, "Your Spring Security One Time Token", "Use the following link to sign in into the application: " + magicLink); (4)
        this.redirectHandler.handle(request, response, oneTimeToken); (5)
    }

    private String getUserEmail() {
        // ...
    }

}

@Controller
class PageController {

    @GetMapping("/ott/sent")
    String ottSent() {
        return "my-template";
    }

}
```

Copied!

```kotlin
@Configuration
@EnableWebSecurity
class SecurityConfig {

        @Bean
        open fun filterChain(http: HttpSecurity): SecurityFilterChain {
            http{
                formLogin {}
                oneTimeTokenLogin {  }
            }
            return http.build()
        }
}

import org.springframework.mail.SimpleMailMessage;
import org.springframework.mail.javamail.JavaMailSender;

@Component (1)
class MagicLinkOneTimeTokenGenerationSuccessHandler(
    private val mailSender: MailSender,
    private val redirectHandler: OneTimeTokenGenerationSuccessHandler = RedirectOneTimeTokenGenerationSuccessHandler("/ott/sent")
) : OneTimeTokenGenerationSuccessHandler {

    override fun handle(request: HttpServletRequest, response: HttpServletResponse, oneTimeToken: OneTimeToken) {
        val builder = UriComponentsBuilder.fromHttpUrl(UrlUtils.buildFullRequestUrl(request))
            .replacePath(request.contextPath)
            .replaceQuery(null)
            .fragment(null)
            .path("/login/ott")
            .queryParam("token", oneTimeToken.getTokenValue()) (2)
        val magicLink = builder.toUriString()
        val email = getUserEmail(oneTimeToken.getUsername()) (3)
        this.mailSender.send(email, "Your Spring Security One Time Token", "Use the following link to sign in into the application: $magicLink")(4)
        this.redirectHandler.handle(request, response, oneTimeToken) (5)
    }

    private fun getUserEmail(): String {
        // ...
    }
}

@Controller
class PageController {

    @GetMapping("/ott/sent")
    fun ottSent(): String {
        return "my-template"
    }
}
```

Copied!

**1**Make the `MagicLinkOneTimeTokenGenerationSuccessHandler` a Spring bean
**2**Create a login processing URL with the `token` as a query param
**3**Retrieve the user’s email based on the username
**4**Use the `JavaMailSender` API to send the email to the user with the magic link
**5**Use the `RedirectOneTimeTokenGenerationSuccessHandler` to perform a redirect to your desired URL

The email content will look similar to:

> Use the following link to sign in into the application: http://localhost:8080/login/ott?token=a830c444-29d8-4d98-9b46-6aba7b22fe5b

The default submit page will detect that the URL has the `token` query param and will automatically fill the form field with the token value.

[](https://docs.spring.io/spring-security/reference/servlet/authentication/onetimetoken.html#changing-generate-url)Changing the One-Time Token Generate URL
-----------------------------------------------------------------------------------------------------------------------------------------------------------

By default, the [`GenerateOneTimeTokenFilter`](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/authentication/ott/GenerateOneTimeTokenFilter.html) listens to `POST /ott/generate` requests. That URL can be changed by using the `generateTokenUrl(String)` DSL method:

Changing the Generate URL

*   Java

*   Kotlin

```java
@Configuration
@EnableWebSecurity
public class SecurityConfig {

    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) {
        http
            // ...
            .formLogin(Customizer.withDefaults())
            .oneTimeTokenLogin((ott) -> ott
                .generateTokenUrl("/ott/my-generate-url")
            );
        return http.build();
    }

}

@Component
public class MagicLinkOneTimeTokenGenerationSuccessHandler implements OneTimeTokenGenerationSuccessHandler {
    // ...
}
```

Copied!

```kotlin
@Configuration
@EnableWebSecurity
class SecurityConfig {

        @Bean
        open fun filterChain(http: HttpSecurity): SecurityFilterChain {
            http {
                //...
                formLogin { }
                oneTimeTokenLogin {
                    generateTokenUrl = "/ott/my-generate-url"
                }
            }
            return http.build()
        }
}

@Component
class MagicLinkOneTimeTokenGenerationSuccessHandler : OneTimeTokenGenerationSuccessHandler {
     // ...
}
```

Copied!

[](https://docs.spring.io/spring-security/reference/servlet/authentication/onetimetoken.html#changing-submit-page-url)Changing the Default Submit Page URL
----------------------------------------------------------------------------------------------------------------------------------------------------------

The default One-Time Token submit page is generated by the [`DefaultOneTimeTokenSubmitPageGeneratingFilter`](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/authentication/ui/DefaultOneTimeTokenSubmitPageGeneratingFilter.html) and listens to `GET /login/ott`. The URL can also be changed, like so:

Configuring the Default Submit Page URL

*   Java

*   Kotlin

```java
@Configuration
@EnableWebSecurity
public class SecurityConfig {

    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) {
        http
            // ...
            .formLogin(Customizer.withDefaults())
            .oneTimeTokenLogin((ott) -> ott
                .submitPageUrl("/ott/submit")
            );
        return http.build();
    }

}

@Component
public class MagicLinkGenerationSuccessHandler implements OneTimeTokenGenerationSuccessHandler {
    // ...
}
```

Copied!

```kotlin
@Configuration
@EnableWebSecurity
class SecurityConfig {

        @Bean
        open fun filterChain(http: HttpSecurity): SecurityFilterChain {
            http {
                //...
                formLogin { }
                oneTimeTokenLogin {
                    submitPageUrl = "/ott/submit"
                }
            }
            return http.build()
        }
}

@Component
class MagicLinkOneTimeTokenGenerationSuccessHandler : OneTimeTokenGenerationSuccessHandler {
     // ...
}
```

Copied!

[](https://docs.spring.io/spring-security/reference/servlet/authentication/onetimetoken.html#disabling-default-submit-page)Disabling the Default Submit Page
------------------------------------------------------------------------------------------------------------------------------------------------------------

If you want to use your own One-Time Token submit page, you can disable the default page and then provide your own endpoint.

Disabling the Default Submit Page

*   Java

*   Kotlin

```java
@Configuration
@EnableWebSecurity
public class SecurityConfig {

    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) {
        http
            .authorizeHttpRequests((authorize) -> authorize
                .requestMatchers("/my-ott-submit").permitAll()
                .anyRequest().authenticated()
            )
            .formLogin(Customizer.withDefaults())
            .oneTimeTokenLogin((ott) -> ott
                .showDefaultSubmitPage(false)
            );
        return http.build();
    }

}

@Controller
public class MyController {

    @GetMapping("/my-ott-submit")
    public String ottSubmitPage() {
        return "my-ott-submit";
    }

}

@Component
public class OneTimeTokenGenerationSuccessHandler implements OneTimeTokenGenerationSuccessHandler {
    // ...
}
```

Copied!

```kotlin
@Configuration
@EnableWebSecurity
class SecurityConfig {

   @Bean
   open fun filterChain(http: HttpSecurity): SecurityFilterChain {
            http {
                authorizeHttpRequests {
                    authorize("/my-ott-submit", authenticated)
                    authorize(anyRequest, authenticated)
                }
                formLogin { }
                oneTimeTokenLogin {
                    showDefaultSubmitPage = false
                }
            }
            return http.build()
    }
}

@Controller
class MyController {

   @GetMapping("/my-ott-submit")
   fun ottSubmitPage(): String {
       return "my-ott-submit"
   }
}

@Component
class MagicLinkOneTimeTokenGenerationSuccessHandler : OneTimeTokenGenerationSuccessHandler {
     // ...
}
```

Copied!

[](https://docs.spring.io/spring-security/reference/servlet/authentication/onetimetoken.html#customize-generate-consume-token)Customize How to Generate and Consume One-Time Tokens
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The interface that define the common operations for generating and consuming one-time tokens is the [`OneTimeTokenService`](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/authentication/ott/OneTimeTokenService.html). Spring Security uses the [`InMemoryOneTimeTokenService`](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/authentication/ott/InMemoryOneTimeTokenService.html) as the default implementation of that interface, if none is provided. For production environments consider using [`JdbcOneTimeTokenService`](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/authentication/ott/JdbcOneTimeTokenService.html).

Some of the most common reasons to customize the `OneTimeTokenService` are, but not limited to:

*   Changing the one-time token expire time

*   Storing more information from the generate token request

*   Changing how the token value is created

*   Additional validation when consuming a one-time token

There are two options to customize the `OneTimeTokenService`. One option is to provide it as a bean, so it can be automatically be picked-up by the `oneTimeTokenLogin()` DSL:

Passing the OneTimeTokenService as a Bean

*   Java

*   Kotlin

```java
@Configuration
@EnableWebSecurity
public class SecurityConfig {

    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) {
        http
            // ...
            .formLogin(Customizer.withDefaults())
            .oneTimeTokenLogin(Customizer.withDefaults());
        return http.build();
    }

    @Bean
    public OneTimeTokenService oneTimeTokenService() {
        return new MyCustomOneTimeTokenService();
    }

}

@Component
public class MagicLinkOneTimeTokenGenerationSuccessHandler implements OneTimeTokenGenerationSuccessHandler {
    // ...
}
```

Copied!

```kotlin
@Configuration
@EnableWebSecurity
class SecurityConfig {

    @Bean
    open fun filterChain(http: HttpSecurity): SecurityFilterChain {
        http {
            //...
            formLogin { }
            oneTimeTokenLogin { }
        }
        return http.build()
    }

    @Bean
    open fun oneTimeTokenService(): OneTimeTokenService {
        return MyCustomOneTimeTokenService()
    }
}

@Component
class MagicLinkOneTimeTokenGenerationSuccessHandler : OneTimeTokenGenerationSuccessHandler {
     // ...
}
```

Copied!

The second option is to pass the `OneTimeTokenService` instance to the DSL, which is useful if there are multiple `SecurityFilterChain` and a different `OneTimeTokenService` is needed for each of them.

Passing the OneTimeTokenService using the DSL

*   Java

*   Kotlin

```java
@Configuration
@EnableWebSecurity
public class SecurityConfig {

    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) {
        http
            // ...
            .formLogin(Customizer.withDefaults())
            .oneTimeTokenLogin((ott) -> ott
                .oneTimeTokenService(new MyCustomOneTimeTokenService())
            );
        return http.build();
    }

}

@Component
public class MagicLinkOneTimeTokenGenerationSuccessHandler implements OneTimeTokenGenerationSuccessHandler {
    // ...
}
```

Copied!

```kotlin
@Configuration
@EnableWebSecurity
class SecurityConfig {

    @Bean
    open fun filterChain(http: HttpSecurity): SecurityFilterChain {
        http {
            //...
            formLogin { }
            oneTimeTokenLogin {
                oneTimeTokenService = MyCustomOneTimeTokenService()
            }
        }
        return http.build()
    }

}

@Component
class MagicLinkOneTimeTokenGenerationSuccessHandler : OneTimeTokenGenerationSuccessHandler {
     // ...
}
```

Copied!

[](https://docs.spring.io/spring-security/reference/servlet/authentication/onetimetoken.html#customize-generate-token-request)Customize GenerateOneTimeTokenRequest Instance
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

There are a number of reasons that you may want to adjust an GenerateOneTimeTokenRequest. For example, you may want expiresIn to be set to 10 mins, which Spring Security sets to 5 mins by default.

You can customize elements of GenerateOneTimeTokenRequest by publishing an GenerateOneTimeTokenRequestResolver as a @Bean, like so:

*   Java

*   Kotlin

```java
@Bean
GenerateOneTimeTokenRequestResolver generateOneTimeTokenRequestResolver() {
    DefaultGenerateOneTimeTokenRequestResolver delegate = new DefaultGenerateOneTimeTokenRequestResolver();
        return (request) -> {
		    GenerateOneTimeTokenRequest generate = delegate.resolve(request);
		    return new GenerateOneTimeTokenRequest(generate.getUsername(), Duration.ofSeconds(600));
	};
}
```

Copied!

```kotlin
@Bean
fun generateRequestResolver() : GenerateOneTimeTokenRequestResolver {
    return DefaultGenerateOneTimeTokenRequestResolver().apply {
        this.setExpiresIn(Duration.ofMinutes(10))
    }
}
```

Copied!

*   [Spring Security](https://docs.spring.io/spring-security/reference/index.html) 

 Stable  
    *   [7.0.3](https://docs.spring.io/spring-security/reference/servlet/authentication/onetimetoken.html)
    *   [6.5.8](https://docs.spring.io/spring-security/reference/6.5/servlet/authentication/onetimetoken.html)

 Preview 

    *   [7.1.0-M2](https://docs.spring.io/spring-security/reference/7.1/servlet/authentication/onetimetoken.html)

 Snapshot 

    *   [7.1.0-SNAPSHOT](https://docs.spring.io/spring-security/reference/7.1-SNAPSHOT/servlet/authentication/onetimetoken.html)
    *   [7.0.4-SNAPSHOT](https://docs.spring.io/spring-security/reference/7.0-SNAPSHOT/servlet/authentication/onetimetoken.html)
    *   [6.5.9-SNAPSHOT](https://docs.spring.io/spring-security/reference/6.5-SNAPSHOT/servlet/authentication/onetimetoken.html)

*    Related Spring Documentation 
    *   [Spring Framework](https://docs.spring.io/spring-framework/reference/)
    *   [](https://docs.spring.io/spring-security/reference/servlet/authentication/onetimetoken.html)[Spring Security](https://docs.spring.io/spring-security/reference/)
        *   [Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/)
        *   [Spring LDAP](https://docs.spring.io/spring-ldap/reference/)
        *   [Spring Security Kerberos](https://docs.spring.io/spring-security-kerberos/reference/)
        *   [Spring Session](https://docs.spring.io/spring-session/reference/)
        *   [Spring Vault](https://docs.spring.io/spring-vault/reference/)

    *   [Spring GraphQL](https://docs.spring.io/spring-graphql/reference/)

[All Docs...](https://docs.spring.io/spring-security/reference/spring-projects.html)

![Image 2: Spring](https://docs.spring.io/spring-security/reference/_/img/spring-logo.svg)
Copyright © 2005 - 2026 Broadcom. All Rights Reserved. The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

[Terms of Use](https://www.vmware.com/help/legal.html) • [Privacy](https://www.vmware.com/help/privacy.html) • [Trademark Guidelines](https://spring.io/trademarks)• [Thank you](https://spring.io/thank-you) • [Your California Privacy Rights](https://www.vmware.com/help/privacy/california-privacy-rights.html) • [Cookies Settings](https://docs.spring.io/spring-security/reference/servlet/authentication/onetimetoken.html)

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
