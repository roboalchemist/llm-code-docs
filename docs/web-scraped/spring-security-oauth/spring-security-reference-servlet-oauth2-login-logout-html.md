# Source: https://docs.spring.io/spring-security/reference/servlet/oauth2/login/logout.html

Title: OIDC Logout :: Spring Security

URL Source: https://docs.spring.io/spring-security/reference/servlet/oauth2/login/logout.html

Markdown Content:
OIDC Logout :: Spring Security
===============

[![Image 1: Spring](https://docs.spring.io/spring-security/reference/_/img/spring-logo.svg)](https://spring.io/)

[Why Spring](https://docs.spring.io/spring-security/reference/servlet/oauth2/login/logout.html#)

[Overview](https://spring.io/why-spring)[Microservices](https://spring.io/microservices)[Reactive](https://spring.io/reactive)[Event Driven](https://spring.io/event-driven)[Cloud](https://spring.io/cloud)[Web Applications](https://spring.io/web-applications)[Serverless](https://spring.io/serverless)[Batch](https://spring.io/batch)

[Learn](https://docs.spring.io/spring-security/reference/servlet/oauth2/login/logout.html#)

[Overview](https://spring.io/learn)[Quickstart](https://spring.io/quickstart)[Guides](https://spring.io/guides)[Blog](https://spring.io/blog)

[Projects](https://docs.spring.io/spring-security/reference/servlet/oauth2/login/logout.html#)

[Overview](https://spring.io/projects)[Spring Boot](https://spring.io/projects/spring-boot)[Spring Framework](https://spring.io/projects/spring-framework)[Spring Cloud](https://spring.io/projects/spring-cloud)[Spring Cloud Data Flow](https://spring.io/projects/spring-cloud-dataflow)[Spring Data](https://spring.io/projects/spring-data)[Spring Integration](https://spring.io/projects/spring-integration)[Spring Batch](https://spring.io/projects/spring-batch)[Spring Security](https://spring.io/projects/spring-security)[View all projects](https://spring.io/projects)*   DEVELOPMENT TOOLS
[Spring Tools 4](https://spring.io/tools)[Spring Initializr](https://start.spring.io/)

[Academy](https://docs.spring.io/spring-security/reference/servlet/oauth2/login/logout.html#)

[Courses](https://spring.academy/courses)[Get Certified](https://spring.academy/learning-path)

[Solutions](https://docs.spring.io/spring-security/reference/servlet/oauth2/login/logout.html#)

[Overview](https://spring.io/solutions)[Spring Runtime](https://spring.io/support)[Spring Consulting](https://spring.io/consulting)[Spring Academy For Teams](https://spring.academy/teams)[Security Advisories](https://spring.io/security)

[Community](https://docs.spring.io/spring-security/reference/servlet/oauth2/login/logout.html#)

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

### OIDC Logout

*   [Local Logout](https://docs.spring.io/spring-security/reference/servlet/oauth2/login/logout.html#configure-local-logout)
*   [OpenID Connect 1.0 Client-Initiated Logout](https://docs.spring.io/spring-security/reference/servlet/oauth2/login/logout.html#configure-client-initiated-oidc-logout)
*   [OpenID Connect 1.0 Back-Channel Logout](https://docs.spring.io/spring-security/reference/servlet/oauth2/login/logout.html#configure-provider-initiated-oidc-logout)
*   [Back-Channel Logout Architecture](https://docs.spring.io/spring-security/reference/servlet/oauth2/login/logout.html#_back_channel_logout_architecture)
*   [Customizing the Session Logout Endpoint](https://docs.spring.io/spring-security/reference/servlet/oauth2/login/logout.html#_customizing_the_session_logout_endpoint)
*   [Customizing the Session Logout Cookie Name](https://docs.spring.io/spring-security/reference/servlet/oauth2/login/logout.html#_customizing_the_session_logout_cookie_name)
*   [Customizing the OIDC Provider Session Registry](https://docs.spring.io/spring-security/reference/servlet/oauth2/login/logout.html#oidc-backchannel-logout-session-registry)

[Edit this Page](https://github.com/spring-projects/spring-security/blob/7.0.3/docs/modules/ROOT/pages/servlet/oauth2/login/logout.adoc)[GitHub Project](https://github.com/spring-projects/spring-security "GitHub")[Stack Overflow](https://stackoverflow.com/tags/spring-security)

*   [Spring Security](https://docs.spring.io/spring-security/reference/index.html)
*   [Servlet Applications](https://docs.spring.io/spring-security/reference/servlet/index.html)
*   [OAuth2](https://docs.spring.io/spring-security/reference/servlet/oauth2/index.html)
*   [OAuth2 Log In](https://docs.spring.io/spring-security/reference/servlet/oauth2/login/index.html)
*   [OIDC Logout](https://docs.spring.io/spring-security/reference/servlet/oauth2/login/logout.html)

OIDC Logout
===========

### OIDC Logout

*   [Local Logout](https://docs.spring.io/spring-security/reference/servlet/oauth2/login/logout.html#configure-local-logout)
*   [OpenID Connect 1.0 Client-Initiated Logout](https://docs.spring.io/spring-security/reference/servlet/oauth2/login/logout.html#configure-client-initiated-oidc-logout)
*   [OpenID Connect 1.0 Back-Channel Logout](https://docs.spring.io/spring-security/reference/servlet/oauth2/login/logout.html#configure-provider-initiated-oidc-logout)
*   [Back-Channel Logout Architecture](https://docs.spring.io/spring-security/reference/servlet/oauth2/login/logout.html#_back_channel_logout_architecture)
*   [Customizing the Session Logout Endpoint](https://docs.spring.io/spring-security/reference/servlet/oauth2/login/logout.html#_customizing_the_session_logout_endpoint)
*   [Customizing the Session Logout Cookie Name](https://docs.spring.io/spring-security/reference/servlet/oauth2/login/logout.html#_customizing_the_session_logout_cookie_name)
*   [Customizing the OIDC Provider Session Registry](https://docs.spring.io/spring-security/reference/servlet/oauth2/login/logout.html#oidc-backchannel-logout-session-registry)

Once an end user is able to login to your application, it’s important to consider how they will log out.

Generally speaking, there are three use cases for you to consider:

1.   I want to perform only a local logout

2.   I want to log out both my application and the OIDC Provider, initiated by my application

3.   I want to log out both my application and the OIDC Provider, initiated by the OIDC Provider

[](https://docs.spring.io/spring-security/reference/servlet/oauth2/login/logout.html#configure-local-logout)Local Logout
------------------------------------------------------------------------------------------------------------------------

To perform a local logout, no special OIDC configuration is needed. Spring Security automatically stands up a local logout endpoint, which you can [configure through the `logout()` DSL](https://docs.spring.io/spring-security/reference/servlet/authentication/logout.html).

[](https://docs.spring.io/spring-security/reference/servlet/oauth2/login/logout.html#configure-client-initiated-oidc-logout)OpenID Connect 1.0 Client-Initiated Logout
----------------------------------------------------------------------------------------------------------------------------------------------------------------------

OpenID Connect Session Management 1.0 allows the ability to log out the end user at the Provider by using the Client. One of the strategies available is [RP-Initiated Logout](https://openid.net/specs/openid-connect-rpinitiated-1_0.html).

If the OpenID Provider supports both Session Management and [Discovery](https://openid.net/specs/openid-connect-discovery-1_0.html), the client can obtain the `end_session_endpoint``URL` from the OpenID Provider’s [Discovery Metadata](https://openid.net/specs/openid-connect-session-1_0.html#OPMetadata). You can do so by configuring the `ClientRegistration` with the `issuer-uri`, as follows:

```yaml
spring:
  security:
    oauth2:
      client:
        registration:
          okta:
            client-id: okta-client-id
            client-secret: okta-client-secret
            ...
        provider:
          okta:
            issuer-uri: https://dev-1234.oktapreview.com
```

Copied!

Also, you should configure `OidcClientInitiatedLogoutSuccessHandler`, which implements RP-Initiated Logout, as follows:

*   Java

*   Kotlin

```java
@Configuration
@EnableWebSecurity
public class OAuth2LoginSecurityConfig {

	@Autowired
	private ClientRegistrationRepository clientRegistrationRepository;

	@Bean
	public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
		http
			.authorizeHttpRequests((authorize) -> authorize
				.anyRequest().authenticated()
			)
			.oauth2Login(withDefaults())
			.logout((logout) -> logout
				.logoutSuccessHandler(oidcLogoutSuccessHandler())
			);
		return http.build();
	}

	private LogoutSuccessHandler oidcLogoutSuccessHandler() {
		OidcClientInitiatedLogoutSuccessHandler oidcLogoutSuccessHandler =
				new OidcClientInitiatedLogoutSuccessHandler(this.clientRegistrationRepository);

		// Sets the location that the End-User's User Agent will be redirected to
		// after the logout has been performed at the Provider
		oidcLogoutSuccessHandler.setPostLogoutRedirectUri("{baseUrl}");

		return oidcLogoutSuccessHandler;
	}
}
```

Copied!

```kotlin
@Configuration
@EnableWebSecurity
class OAuth2LoginSecurityConfig {
    @Autowired
    private lateinit var clientRegistrationRepository: ClientRegistrationRepository

    @Bean
    open fun filterChain(http: HttpSecurity): SecurityFilterChain {
        http {
            authorizeHttpRequests {
                authorize(anyRequest, authenticated)
            }
            oauth2Login { }
            logout {
                logoutSuccessHandler = oidcLogoutSuccessHandler()
            }
        }
        return http.build()
    }

    private fun oidcLogoutSuccessHandler(): LogoutSuccessHandler {
        val oidcLogoutSuccessHandler = OidcClientInitiatedLogoutSuccessHandler(clientRegistrationRepository)

        // Sets the location that the End-User's User Agent will be redirected to
        // after the logout has been performed at the Provider
        oidcLogoutSuccessHandler.setPostLogoutRedirectUri("{baseUrl}")
        return oidcLogoutSuccessHandler
    }
}
```

Copied!

`OidcClientInitiatedLogoutSuccessHandler` supports the `{baseUrl}` placeholder. If used, the application’s base URL, such as `app.example.org`, replaces it at request time.

By default, `OidcClientInitiatedLogoutSuccessHandler` redirects to the logout URL using a standard HTTP redirect with the `GET` method. To perform the logout using a `POST` request, set the redirect strategy to `FormPostRedirectStrategy`, for example with `OidcClientInitiatedLogoutSuccessHandler.setRedirectStrategy(new FormPostRedirectStrategy())`.

[](https://docs.spring.io/spring-security/reference/servlet/oauth2/login/logout.html#configure-provider-initiated-oidc-logout)OpenID Connect 1.0 Back-Channel Logout
--------------------------------------------------------------------------------------------------------------------------------------------------------------------

OpenID Connect Session Management 1.0 allows the ability to log out the end user at the Client by having the Provider make an API call to the Client. This is referred to as [OIDC Back-Channel Logout](https://openid.net/specs/openid-connect-backchannel-1_0.html).

To enable this, you can stand up the Back-Channel Logout endpoint in the DSL like so:

*   Java

*   Kotlin

```java
@Bean
OidcBackChannelLogoutHandler oidcLogoutHandler() {
	return new OidcBackChannelLogoutHandler();
}

@Bean
public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
    http
        .authorizeHttpRequests((authorize) -> authorize
            .anyRequest().authenticated()
        )
        .oauth2Login(withDefaults())
        .oidcLogout((logout) -> logout
            .backChannel(Customizer.withDefaults())
        );
    return http.build();
}
```

Copied!

```kotlin
@Bean
fun oidcLogoutHandler(): OidcBackChannelLogoutHandler {
    return OidcBackChannelLogoutHandler()
}

@Bean
open fun filterChain(http: HttpSecurity): SecurityFilterChain {
    http {
        authorizeHttpRequests {
            authorize(anyRequest, authenticated)
        }
        oauth2Login { }
        oidcLogout {
            backChannel { }
        }
    }
    return http.build()
}
```

Copied!

Then, you need a way listen to events published by Spring Security to remove old `OidcSessionInformation` entries, like so:

*   Java

*   Kotlin

```java
@Bean
public HttpSessionEventPublisher sessionEventPublisher() {
    return new HttpSessionEventPublisher();
}
```

Copied!

```kotlin
@Bean
open fun sessionEventPublisher(): HttpSessionEventPublisher {
    return HttpSessionEventPublisher()
}
```

Copied!

This will make so that if `HttpSession#invalidate` is called, then the session is also removed from memory.

And that’s it!

This will stand up the endpoint `/logout/connect/back-channel/{registrationId}` which the OIDC Provider can request to invalidate a given session of an end user in your application.

`oidcLogout` requires that `oauth2Login` also be configured.

`oidcLogout` requires that the session cookie be called `JSESSIONID` in order to correctly log out each session through a backchannel.

### [](https://docs.spring.io/spring-security/reference/servlet/oauth2/login/logout.html#_back_channel_logout_architecture)Back-Channel Logout Architecture

Consider a `ClientRegistration` whose identifier is `registrationId`.

The overall flow for a Back-Channel logout is like this:

1.   At login time, Spring Security correlates the ID Token, CSRF Token, and Provider Session ID (if any) to your application’s session id in its `OidcSessionRegistry` implementation.

2.   Then at logout time, your OIDC Provider makes an API call to `/logout/connect/back-channel/registrationId` including a Logout Token that indicates either the `sub` (the End User) or the `sid` (the Provider Session ID) to logout.

3.   Spring Security validates the token’s signature and claims.

4.   If the token contains a `sid` claim, then only the Client’s session that correlates to that provider session is terminated.

5.   Otherwise, if the token contains a `sub` claim, then all that Client’s sessions for that End User are terminated.

Remember that Spring Security’s OIDC support is multi-tenant. This means that it will only terminate sessions whose Client matches the `aud` claim in the Logout Token.

One notable part of this architecture’s implementation is that it propagates the incoming back-channel request internally for each corresponding session. Initially, this may seem unnecessary. However, recall that the Servlet API does not give direct access to the `HttpSession` store. By making an internal logout call, the corresponding session can now be invalidated.

Additionally, forging a logout call internally allows for each set of `LogoutHandler`s to be run against that session and corresponding `SecurityContext`.

### [](https://docs.spring.io/spring-security/reference/servlet/oauth2/login/logout.html#_customizing_the_session_logout_endpoint)Customizing the Session Logout Endpoint

With `OidcBackChannelLogoutHandler` published, the session logout endpoint is `{baseUrl}/logout/connect/back-channel/{registrationId}`.

If `OidcBackChannelLogoutHandler` is not wired, then the URL is `{baseUrl}/logout/connect/back-channel/{registrationId}`, which is not recommended since it requires passing a CSRF token, which can be challenging depending on the kind of repository your application uses.

In the event that you need to customize the endpoint, you can provide the URL as follows:

*   Java

*   Kotlin

http
    // ...
    .oidcLogout((oidc) -> oidc
        .backChannel((backChannel) -> backChannel
            .logoutUri("http://localhost:9000/logout/connect/back-channel/+{registrationId}+")
        )
    );

http {
    oidcLogout {
        backChannel {
            logoutUri = "http://localhost:9000/logout/connect/back-channel/+{registrationId}+"
        }
    }
}

### [](https://docs.spring.io/spring-security/reference/servlet/oauth2/login/logout.html#_customizing_the_session_logout_cookie_name)Customizing the Session Logout Cookie Name

By default, the session logout endpoint uses the `JSESSIONID` cookie to correlate the session to the corresponding `OidcSessionInformation`.

However, the default cookie name in Spring Session is `SESSION`.

You can configure Spring Session’s cookie name in the DSL like so:

*   Java

*   Kotlin

@Bean
OidcBackChannelLogoutHandler oidcLogoutHandler(OidcSessionRegistry oidcSessionRegistry) {
    OidcBackChannelLogoutHandler logoutHandler = new OidcBackChannelLogoutHandler(oidcSessionRegistry);
    logoutHandler.setSessionCookieName("SESSION");
    return logoutHandler;
}

@Bean
open fun oidcLogoutHandler(val sessionRegistry: OidcSessionRegistry): OidcBackChannelLogoutHandler {
    val logoutHandler = OidcBackChannelLogoutHandler(sessionRegistry)
    logoutHandler.setSessionCookieName("SESSION")
    return logoutHandler
}

### [](https://docs.spring.io/spring-security/reference/servlet/oauth2/login/logout.html#oidc-backchannel-logout-session-registry)Customizing the OIDC Provider Session Registry

By default, Spring Security stores in-memory all links between the OIDC Provider session and the Client session.

There are a number of circumstances, like a clustered application, where it would be nice to store this instead in a separate location, like a database.

You can achieve this by configuring a custom `OidcSessionRegistry`, like so:

*   Java

*   Kotlin

```java
@Component
public final class MySpringDataOidcSessionRegistry implements OidcSessionRegistry {
    private final OidcProviderSessionRepository sessions;

    // ...

    @Override
    public void saveSessionInformation(OidcSessionInformation info) {
        this.sessions.save(info);
    }

    @Override
    public OidcSessionInformation removeSessionInformation(String clientSessionId) {
       return this.sessions.removeByClientSessionId(clientSessionId);
    }

    @Override
    public Iterable<OidcSessionInformation> removeSessionInformation(OidcLogoutToken token) {
        return token.getSessionId() != null ?
            this.sessions.removeBySessionIdAndIssuerAndAudience(...) :
            this.sessions.removeBySubjectAndIssuerAndAudience(...);
    }
}
```

Copied!

```kotlin
@Component
class MySpringDataOidcSessionRegistry: OidcSessionRegistry {
    val sessions: OidcProviderSessionRepository

    // ...

    @Override
    fun saveSessionInformation(info: OidcSessionInformation) {
        this.sessions.save(info)
    }

    @Override
    fun removeSessionInformation(clientSessionId: String): OidcSessionInformation {
       return this.sessions.removeByClientSessionId(clientSessionId);
    }

    @Override
    fun removeSessionInformation(token: OidcLogoutToken): Iterable<OidcSessionInformation> {
        return token.getSessionId() != null ?
            this.sessions.removeBySessionIdAndIssuerAndAudience(...) :
            this.sessions.removeBySubjectAndIssuerAndAudience(...);
    }
}
```

Copied!

*   [Spring Security](https://docs.spring.io/spring-security/reference/index.html) 

 Stable  
    *   [7.0.3](https://docs.spring.io/spring-security/reference/servlet/oauth2/login/logout.html)
    *   [6.5.8](https://docs.spring.io/spring-security/reference/6.5/servlet/oauth2/login/logout.html)

 Preview 

    *   [7.1.0-M2](https://docs.spring.io/spring-security/reference/7.1/servlet/oauth2/login/logout.html)

 Snapshot 

    *   [7.1.0-SNAPSHOT](https://docs.spring.io/spring-security/reference/7.1-SNAPSHOT/servlet/oauth2/login/logout.html)
    *   [7.0.4-SNAPSHOT](https://docs.spring.io/spring-security/reference/7.0-SNAPSHOT/servlet/oauth2/login/logout.html)
    *   [6.5.9-SNAPSHOT](https://docs.spring.io/spring-security/reference/6.5-SNAPSHOT/servlet/oauth2/login/logout.html)

*    Related Spring Documentation 
    *   [Spring Framework](https://docs.spring.io/spring-framework/reference/)
    *   [](https://docs.spring.io/spring-security/reference/servlet/oauth2/login/logout.html)[Spring Security](https://docs.spring.io/spring-security/reference/)
        *   [Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/)
        *   [Spring LDAP](https://docs.spring.io/spring-ldap/reference/)
        *   [Spring Security Kerberos](https://docs.spring.io/spring-security-kerberos/reference/)
        *   [Spring Session](https://docs.spring.io/spring-session/reference/)
        *   [Spring Vault](https://docs.spring.io/spring-vault/reference/)

    *   [Spring GraphQL](https://docs.spring.io/spring-graphql/reference/)

[All Docs...](https://docs.spring.io/spring-security/reference/spring-projects.html)

![Image 2: Spring](https://docs.spring.io/spring-security/reference/_/img/spring-logo.svg)
Copyright © 2005 - 2026 Broadcom. All Rights Reserved. The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

[Terms of Use](https://www.vmware.com/help/legal.html) • [Privacy](https://www.vmware.com/help/privacy.html) • [Trademark Guidelines](https://spring.io/trademarks)• [Thank you](https://spring.io/thank-you) • [Your California Privacy Rights](https://www.vmware.com/help/privacy/california-privacy-rights.html) • [Cookies Settings](https://docs.spring.io/spring-security/reference/servlet/oauth2/login/logout.html)

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
