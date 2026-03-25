# Source: https://docs.spring.io/spring-security/reference/servlet/authentication/logout.html

Title: Handling Logouts :: Spring Security

URL Source: https://docs.spring.io/spring-security/reference/servlet/authentication/logout.html

Markdown Content:
Handling Logouts :: Spring Security
===============

[![Image 1: Spring](https://docs.spring.io/spring-security/reference/_/img/spring-logo.svg)](https://spring.io/)

[Why Spring](https://docs.spring.io/spring-security/reference/servlet/authentication/logout.html#)

[Overview](https://spring.io/why-spring)[Microservices](https://spring.io/microservices)[Reactive](https://spring.io/reactive)[Event Driven](https://spring.io/event-driven)[Cloud](https://spring.io/cloud)[Web Applications](https://spring.io/web-applications)[Serverless](https://spring.io/serverless)[Batch](https://spring.io/batch)

[Learn](https://docs.spring.io/spring-security/reference/servlet/authentication/logout.html#)

[Overview](https://spring.io/learn)[Quickstart](https://spring.io/quickstart)[Guides](https://spring.io/guides)[Blog](https://spring.io/blog)

[Projects](https://docs.spring.io/spring-security/reference/servlet/authentication/logout.html#)

[Overview](https://spring.io/projects)[Spring Boot](https://spring.io/projects/spring-boot)[Spring Framework](https://spring.io/projects/spring-framework)[Spring Cloud](https://spring.io/projects/spring-cloud)[Spring Cloud Data Flow](https://spring.io/projects/spring-cloud-dataflow)[Spring Data](https://spring.io/projects/spring-data)[Spring Integration](https://spring.io/projects/spring-integration)[Spring Batch](https://spring.io/projects/spring-batch)[Spring Security](https://spring.io/projects/spring-security)[View all projects](https://spring.io/projects)*   DEVELOPMENT TOOLS
[Spring Tools 4](https://spring.io/tools)[Spring Initializr](https://start.spring.io/)

[Academy](https://docs.spring.io/spring-security/reference/servlet/authentication/logout.html#)

[Courses](https://spring.academy/courses)[Get Certified](https://spring.academy/learning-path)

[Solutions](https://docs.spring.io/spring-security/reference/servlet/authentication/logout.html#)

[Overview](https://spring.io/solutions)[Spring Runtime](https://spring.io/support)[Spring Consulting](https://spring.io/consulting)[Spring Academy For Teams](https://spring.academy/teams)[Security Advisories](https://spring.io/security)

[Community](https://docs.spring.io/spring-security/reference/servlet/authentication/logout.html#)

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

### Handling Logouts

*   [Understanding Logout’s Architecture](https://docs.spring.io/spring-security/reference/servlet/authentication/logout.html#logout-java-configuration)
*   [Customizing Logout URIs](https://docs.spring.io/spring-security/reference/servlet/authentication/logout.html#customizing-logout-uris)
*   [Adding Clean-up Actions](https://docs.spring.io/spring-security/reference/servlet/authentication/logout.html#add-logout-handler)
*   [Using Clear-Site-Data to Log Out the User](https://docs.spring.io/spring-security/reference/servlet/authentication/logout.html#clear-all-site-data)
*   [Customizing Logout Success](https://docs.spring.io/spring-security/reference/servlet/authentication/logout.html#customizing-logout-success)
*   [Creating a Custom Logout Endpoint](https://docs.spring.io/spring-security/reference/servlet/authentication/logout.html#creating-custom-logout-endpoint)
*   [Testing Logout](https://docs.spring.io/spring-security/reference/servlet/authentication/logout.html#testing-logout)
*   [Further Logout-Related References](https://docs.spring.io/spring-security/reference/servlet/authentication/logout.html#jc-logout-references)

[Edit this Page](https://github.com/spring-projects/spring-security/blob/7.0.3/docs/modules/ROOT/pages/servlet/authentication/logout.adoc)[GitHub Project](https://github.com/spring-projects/spring-security "GitHub")[Stack Overflow](https://stackoverflow.com/tags/spring-security)

*   [Spring Security](https://docs.spring.io/spring-security/reference/index.html)
*   [Servlet Applications](https://docs.spring.io/spring-security/reference/servlet/index.html)
*   [Authentication](https://docs.spring.io/spring-security/reference/servlet/authentication/index.html)
*   [Logout](https://docs.spring.io/spring-security/reference/servlet/authentication/logout.html)

Handling Logouts
================

### Handling Logouts

*   [Understanding Logout’s Architecture](https://docs.spring.io/spring-security/reference/servlet/authentication/logout.html#logout-java-configuration)
*   [Customizing Logout URIs](https://docs.spring.io/spring-security/reference/servlet/authentication/logout.html#customizing-logout-uris)
*   [Adding Clean-up Actions](https://docs.spring.io/spring-security/reference/servlet/authentication/logout.html#add-logout-handler)
*   [Using Clear-Site-Data to Log Out the User](https://docs.spring.io/spring-security/reference/servlet/authentication/logout.html#clear-all-site-data)
*   [Customizing Logout Success](https://docs.spring.io/spring-security/reference/servlet/authentication/logout.html#customizing-logout-success)
*   [Creating a Custom Logout Endpoint](https://docs.spring.io/spring-security/reference/servlet/authentication/logout.html#creating-custom-logout-endpoint)
*   [Testing Logout](https://docs.spring.io/spring-security/reference/servlet/authentication/logout.html#testing-logout)
*   [Further Logout-Related References](https://docs.spring.io/spring-security/reference/servlet/authentication/logout.html#jc-logout-references)

In an application where end users can [login](https://docs.spring.io/spring-security/reference/servlet/authentication/index.html), they should also be able to logout.

By default, Spring Security stands up a `/logout` endpoint, so no additional code is necessary.

The rest of this section covers a number of use cases for you to consider:

*   I want to [understand logout’s architecture](https://docs.spring.io/spring-security/reference/servlet/authentication/logout.html#logout-java-configuration)

*   I want to [customize the logout or logout success URI](https://docs.spring.io/spring-security/reference/servlet/authentication/logout.html#customizing-logout-uris)

*   I want to know when I need to [explicitly permit the `/logout` endpoint](https://docs.spring.io/spring-security/reference/servlet/authentication/logout.html#permit-logout-endpoints)

*   I want to [clear cookies, storage, and/or cache](https://docs.spring.io/spring-security/reference/servlet/authentication/logout.html#clear-all-site-data) when the user logs out

*   I am using OAuth 2.0 and I want to [coordinate logout with an Authorization Server](https://docs.spring.io/spring-security/reference/servlet/oauth2/login/advanced.html#oauth2login-advanced-oidc-logout)

*   I am using SAML 2.0 and I want to [coordinate logout with an Identity Provider](https://docs.spring.io/spring-security/reference/servlet/saml2/logout.html)

*   I am using CAS and I want to [coordinate logout with an Identity Provider](https://docs.spring.io/spring-security/reference/servlet/authentication/cas.html#cas-singlelogout)

[](https://docs.spring.io/spring-security/reference/servlet/authentication/logout.html#logout-java-configuration)Understanding Logout’s Architecture
----------------------------------------------------------------------------------------------------------------------------------------------------

When you include [the `spring-boot-starter-security` dependency](https://docs.spring.io/spring-boot/4.0.0-SNAPSHOT/reference/using/build-systems.html#using.build-systems.starters) or use the `@EnableWebSecurity` annotation, Spring Security will add its logout support and by default respond both to `GET /logout` and `POST /logout`.

If you request `GET /logout`, then Spring Security displays a logout confirmation page. Aside from providing a valuable double-checking mechanism for the user, it also provides a simple way to provide [the needed CSRF token](https://docs.spring.io/spring-security/reference/servlet/exploits/csrf.html) to `POST /logout`.

Please note that if [CSRF protection](https://docs.spring.io/spring-security/reference/servlet/exploits/csrf.html) is disabled in configuration, no logout confirmation page is shown to the user and the logout is performed directly.

In your application it is not necessary to use `GET /logout` to perform a logout. So long as [the needed CSRF token](https://docs.spring.io/spring-security/reference/servlet/exploits/csrf.html) is present in the request, your application can simply `POST /logout` to induce a logout.

If you request `POST /logout`, then it will perform the following default operations using a series of [`LogoutHandler`](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/authentication/logout/LogoutHandler.html) instances:

*   Invalidate the HTTP session ([`SecurityContextLogoutHandler`](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/authentication/logout/SecurityContextLogoutHandler.html))

*   Clear the [`SecurityContextHolderStrategy`](https://docs.spring.io/spring-security/reference/servlet/authentication/session-management.html#use-securitycontextholderstrategy) ([`SecurityContextLogoutHandler`](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/authentication/logout/SecurityContextLogoutHandler.html))

*   Clear the [`SecurityContextRepository`](https://docs.spring.io/spring-security/reference/servlet/authentication/persistence.html#securitycontextrepository) ([`SecurityContextLogoutHandler`](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/authentication/logout/SecurityContextLogoutHandler.html))

*   Clean up any [RememberMe authentication](https://docs.spring.io/spring-security/reference/servlet/authentication/rememberme.html) (`TokenRememberMeServices` / `PersistentTokenRememberMeServices`)

*   Clear out any saved [CSRF token](https://docs.spring.io/spring-security/reference/servlet/exploits/csrf.html) ([`CsrfLogoutHandler`](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/csrf/CsrfLogoutHandler.html))

*   [Fire](https://docs.spring.io/spring-security/reference/servlet/authentication/events.html) a `LogoutSuccessEvent` ([`LogoutSuccessEventPublishingLogoutHandler`](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/authentication/logout/LogoutSuccessEventPublishingLogoutHandler.html))

Once completed, then it will exercise its default [`LogoutSuccessHandler`](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/authentication/logout/LogoutSuccessHandler.html) which redirects to `/login?logout`.

[](https://docs.spring.io/spring-security/reference/servlet/authentication/logout.html#customizing-logout-uris)Customizing Logout URIs
--------------------------------------------------------------------------------------------------------------------------------------

Since the `LogoutFilter` appears before [the `AuthorizationFilter`](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html) in [the filter chain](https://docs.spring.io/spring-security/reference/servlet/architecture.html#servlet-filterchain-figure), it is not necessary by default to explicitly permit the `/logout` endpoint. Thus, only [custom logout endpoints](https://docs.spring.io/spring-security/reference/servlet/authentication/logout.html#permit-logout-endpoints) that you create yourself generally require a `permitAll` configuration to be reachable.

For example, if you want to simply change the URI that Spring Security is matching, you can do so in the `logout` DSL in following way:

Custom Logout Uri

*   Java

*   Kotlin

*   Xml

```java
http
    .logout((logout) -> logout.logoutUrl("/my/logout/uri"))
```

Copied!

```kotlin
http {
    logout {
        logoutUrl = "/my/logout/uri"
    }
}
```

Copied!

```xml
<logout logout-url="/my/logout/uri"/>
```

Copied!

and no authorization changes are necessary since it simply adjusts the `LogoutFilter`.

However, if you stand up your own logout success endpoint (or in a rare case, [your own logout endpoint](https://docs.spring.io/spring-security/reference/servlet/authentication/logout.html#creating-custom-logout-endpoint)), say using [Spring MVC](https://docs.spring.io/spring-framework/reference/7.0.4/web.html#spring-web), you will need to permit it in Spring Security. This is because Spring MVC processes your request after Spring Security does.

You can do this using `authorizeHttpRequests` or `<intercept-url>` like so:

Custom Logout Endpoint

*   Java

*   Kotlin

*   Xml

```java
http
    .authorizeHttpRequests((authorize) -> authorize
        .requestMatchers("/my/success/endpoint").permitAll()
        // ...
    )
    .logout((logout) -> logout.logoutSuccessUrl("/my/success/endpoint"))
```

Copied!

```kotlin
http {
    authorizeHttpRequests {
        authorize("/my/success/endpoint", permitAll)
    }
    logout {
        logoutSuccessUrl = "/my/success/endpoint"
    }
}
```

Copied!

```xml
<http>
    <filter-url pattern="/my/success/endpoint" access="permitAll"/>
    <logout logout-success-url="/my/success/endpoint"/>
</http>
```

Copied!

In this example, you tell the `LogoutFilter` to redirect to `/my/success/endpoint` when it is done. And, you explicitly permit the `/my/success/endpoint` endpoint in [the `AuthorizationFilter`](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html).

Specifying it twice can be cumbersome, though. If you are using Java configuration, you can instead set the `permitAll` property in the logout DSL like so:

Permitting Custom Logout Endpoints

*   Java

*   Kotlin

```java
http
    .authorizeHttpRequests((authorize) -> authorize
        // ...
    )
    .logout((logout) -> logout
        .logoutSuccessUrl("/my/success/endpoint")
        .permitAll()
    )
```

Copied!

```kotlin
http
    authorizeHttpRequests {
        // ...
    }
    logout {
        logoutSuccessUrl = "/my/success/endpoint"
        permitAll = true
    }
```

Copied!

which will add all logout URIs to the permit list for you.

[](https://docs.spring.io/spring-security/reference/servlet/authentication/logout.html#add-logout-handler)Adding Clean-up Actions
---------------------------------------------------------------------------------------------------------------------------------

If you are using Java configuration, you can add clean up actions of your own by calling the `addLogoutHandler` method in the `logout` DSL, like so:

Custom Logout Handler

*   Java

*   Kotlin

```java
CookieClearingLogoutHandler cookies = new CookieClearingLogoutHandler("our-custom-cookie");
http
    .logout((logout) -> logout.addLogoutHandler(cookies))
```

Copied!

```kotlin
http {
    logout {
        addLogoutHandler(CookieClearingLogoutHandler("our-custom-cookie"))
    }
}
```

Copied!

Because [`LogoutHandler`](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/authentication/logout/LogoutHandler.html) instances are for the purposes of cleanup, they should not throw exceptions.

Since [`LogoutHandler`](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/authentication/logout/LogoutHandler.html) is a functional interface, you can provide a custom one as a lambda.

Some logout handler configurations are common enough that they are exposed directly in the `logout` DSL and `<logout>` element. One example is configuring session invalidation and another is which additional cookies should be deleted.

For example, you can configure the [`CookieClearingLogoutHandler`](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/authentication/logout/CookieClearingLogoutHandler.html) as seen above.

Or you can instead set the appropriate configuration value like so:

*   Java

*   Kotlin

*   Xml

```java
http
    .logout((logout) -> logout.deleteCookies("our-custom-cookie"))
```

Copied!

```kotlin
http {
    logout {
        deleteCookies("our-custom-cookie")
    }
}
```

Copied!

```kotlin
<http>
    <logout delete-cookies="our-custom-cookie"/>
</http>
```

Copied!

Specifying that the `JSESSIONID` cookie is not necessary since [`SecurityContextLogoutHandler`](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/authentication/logout/SecurityContextLogoutHandler.html) removes it by virtue of invalidating the session.

### [](https://docs.spring.io/spring-security/reference/servlet/authentication/logout.html#clear-all-site-data)Using Clear-Site-Data to Log Out the User

The `Clear-Site-Data` HTTP header is one that browsers support as an instruction to clear cookies, storage, and cache that belong to the owning website. This is a handy and secure way to ensure that everything, including the session cookie, is cleaned up on logout.

You can add configure Spring Security to write the `Clear-Site-Data` header on logout like so:

Using Clear-Site-Data

*   Java

*   Kotlin

```java
HeaderWriterLogoutHandler clearSiteData = new HeaderWriterLogoutHandler(new ClearSiteDataHeaderWriter(Directives.ALL));
http
    .logout((logout) -> logout.addLogoutHandler(clearSiteData))
```

Copied!

```kotlin
val clearSiteData = HeaderWriterLogoutHandler(ClearSiteDataHeaderWriter(Directives.ALL))
http {
    logout {
        addLogoutHandler(clearSiteData)
    }
}
```

Copied!

You give the `ClearSiteDataHeaderWriter` constructor the list of things that you want to be cleared out.

The above configuration clears out all site data, but you can also configure it to remove just cookies like so:

Using Clear-Site-Data to Clear Cookies

*   Java

*   Kotlin

```java
HeaderWriterLogoutHandler clearSiteData = new HeaderWriterLogoutHandler(new ClearSiteDataHeaderWriter(Directive.COOKIES));
http
    .logout((logout) -> logout.addLogoutHandler(clearSiteData))
```

Copied!

```kotlin
val clearSiteData = HeaderWriterLogoutHandler(ClearSiteDataHeaderWriter(Directive.COOKIES))
http {
    logout {
        addLogoutHandler(clearSiteData)
    }
}
```

Copied!

[](https://docs.spring.io/spring-security/reference/servlet/authentication/logout.html#customizing-logout-success)Customizing Logout Success
--------------------------------------------------------------------------------------------------------------------------------------------

While using `logoutSuccessUrl` will suffice for most cases, you may need to do something different from redirecting to a URL once logout is complete. [`LogoutSuccessHandler`](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/authentication/logout/LogoutSuccessHandler.html) is the Spring Security component for customizing logout success actions.

For example, instead of redirecting, you may want to only return a status code. In this case, you can provide a success handler instance, like so:

Customizing Logout Success to Return HTTP Status Code

*   Java

*   Kotlin

*   Xml

```java
http
    .logout((logout) -> logout.logoutSuccessHandler(new HttpStatusReturningLogoutSuccessHandler()))
```

Copied!

```kotlin
http {
    logout {
        logoutSuccessHandler = HttpStatusReturningLogoutSuccessHandler()
    }
}
```

Copied!

```xml
<bean name="mySuccessHandlerBean" class="org.springframework.security.web.authentication.logout.HttpStatusReturningLogoutSuccessHandler"/>
<http>
    <logout success-handler-ref="mySuccessHandlerBean"/>
</http>
```

Copied!

Since [`LogoutSuccessHandler`](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/authentication/logout/LogoutSuccessHandler.html) is a functional interface, you can provide a custom one as a lambda.

[](https://docs.spring.io/spring-security/reference/servlet/authentication/logout.html#creating-custom-logout-endpoint)Creating a Custom Logout Endpoint
--------------------------------------------------------------------------------------------------------------------------------------------------------

It is strongly recommended that you use the provided `logout` DSL to configure logout. One reason is that its easy to forget to call the needed Spring Security components to ensure a proper and complete logout.

In fact, it is often simpler to [register a custom `LogoutHandler`](https://docs.spring.io/spring-security/reference/servlet/authentication/logout.html#add-logout-handler) than create a [Spring MVC](https://docs.spring.io/spring-framework/reference/7.0.4/web.html#spring-web) endpoint for performing logout.

That said, if you find yourself in a circumstance where a custom logout endpoint is needed, like the following one:

Custom Logout Endpoint

*   Java

*   Kotlin

```java
@PostMapping("/my/logout")
public String performLogout() {
    // .. perform logout
    return "redirect:/home";
}
```

Copied!

```kotlin
@PostMapping("/my/logout")
fun performLogout(): String {
    // .. perform logout
    return "redirect:/home"
}
```

Copied!

then you will need to have that endpoint invoke Spring Security’s [`SecurityContextLogoutHandler`](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/authentication/logout/SecurityContextLogoutHandler.html) to ensure a secure and complete logout. Something like the following is needed at a minimum:

Custom Logout Endpoint

*   Java

*   Kotlin

```java
SecurityContextLogoutHandler logoutHandler = new SecurityContextLogoutHandler();

@PostMapping("/my/logout")
public String performLogout(Authentication authentication, HttpServletRequest request, HttpServletResponse response) {
    // .. perform logout
    this.logoutHandler.logout(request, response, authentication);
    return "redirect:/home";
}
```

Copied!

```kotlin
val logoutHandler = SecurityContextLogoutHandler()

@PostMapping("/my/logout")
fun performLogout(val authentication: Authentication, val request: HttpServletRequest, val response: HttpServletResponse): String {
    // .. perform logout
    this.logoutHandler.logout(request, response, authentication)
    return "redirect:/home"
}
```

Copied!

Such will clear out the [`SecurityContextHolderStrategy`](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/core/context/SecurityContextHolderStrategy.html) and [`SecurityContextRepository`](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/context/SecurityContextRepository.html) as needed.

Also, you’ll need to [explicitly permit the endpoint](https://docs.spring.io/spring-security/reference/servlet/authentication/logout.html#permit-logout-endpoints).

Failing to call [`SecurityContextLogoutHandler`](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/authentication/logout/SecurityContextLogoutHandler.html) means that [the `SecurityContext`](https://docs.spring.io/spring-security/reference/servlet/authentication/architecture.html#servlet-authentication-securitycontext) could still be available on subsequent requests, meaning that the user is not actually logged out.

[](https://docs.spring.io/spring-security/reference/servlet/authentication/logout.html#testing-logout)Testing Logout
--------------------------------------------------------------------------------------------------------------------

Once you have logout configured you can test it using [Spring Security’s MockMvc support](https://docs.spring.io/spring-security/reference/servlet/test/mockmvc/logout.html).

[](https://docs.spring.io/spring-security/reference/servlet/authentication/logout.html#jc-logout-references)Further Logout-Related References
---------------------------------------------------------------------------------------------------------------------------------------------

*   [Testing Logout](https://docs.spring.io/spring-security/reference/servlet/test/mockmvc/logout.html#test-logout)

*   [HttpServletRequest.logout()](https://docs.spring.io/spring-security/reference/servlet/integrations/servlet-api.html#servletapi-logout)

*   [Remember-Me Interfaces and Implementations](https://docs.spring.io/spring-security/reference/servlet/authentication/rememberme.html#remember-me-impls)

*   [Logging Out](https://docs.spring.io/spring-security/reference/servlet/exploits/csrf.html#csrf-considerations-logout) in section CSRF Caveats

*   Section [Single Logout](https://docs.spring.io/spring-security/reference/servlet/authentication/cas.html#cas-singlelogout) (CAS protocol)

*   Documentation for the [logout element](https://docs.spring.io/spring-security/reference/servlet/appendix/namespace/http.html#nsa-logout) in the Spring Security XML Namespace section

*   [Spring Security](https://docs.spring.io/spring-security/reference/index.html) 

 Stable  
    *   [7.0.3](https://docs.spring.io/spring-security/reference/servlet/authentication/logout.html)
    *   [6.5.8](https://docs.spring.io/spring-security/reference/6.5/servlet/authentication/logout.html)

 Preview 

    *   [7.1.0-M2](https://docs.spring.io/spring-security/reference/7.1/servlet/authentication/logout.html)

 Snapshot 

    *   [7.1.0-SNAPSHOT](https://docs.spring.io/spring-security/reference/7.1-SNAPSHOT/servlet/authentication/logout.html)
    *   [7.0.4-SNAPSHOT](https://docs.spring.io/spring-security/reference/7.0-SNAPSHOT/servlet/authentication/logout.html)
    *   [6.5.9-SNAPSHOT](https://docs.spring.io/spring-security/reference/6.5-SNAPSHOT/servlet/authentication/logout.html)

*    Related Spring Documentation 
    *   [Spring Framework](https://docs.spring.io/spring-framework/reference/)
    *   [](https://docs.spring.io/spring-security/reference/servlet/authentication/logout.html)[Spring Security](https://docs.spring.io/spring-security/reference/)
        *   [Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/)
        *   [Spring LDAP](https://docs.spring.io/spring-ldap/reference/)
        *   [Spring Security Kerberos](https://docs.spring.io/spring-security-kerberos/reference/)
        *   [Spring Session](https://docs.spring.io/spring-session/reference/)
        *   [Spring Vault](https://docs.spring.io/spring-vault/reference/)

    *   [Spring GraphQL](https://docs.spring.io/spring-graphql/reference/)

[All Docs...](https://docs.spring.io/spring-security/reference/spring-projects.html)

![Image 2: Spring](https://docs.spring.io/spring-security/reference/_/img/spring-logo.svg)
Copyright © 2005 - 2026 Broadcom. All Rights Reserved. The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

[Terms of Use](https://www.vmware.com/help/legal.html) • [Privacy](https://www.vmware.com/help/privacy.html) • [Trademark Guidelines](https://spring.io/trademarks)• [Thank you](https://spring.io/thank-you) • [Your California Privacy Rights](https://www.vmware.com/help/privacy/california-privacy-rights.html) • [Cookies Settings](https://docs.spring.io/spring-security/reference/servlet/authentication/logout.html)

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
