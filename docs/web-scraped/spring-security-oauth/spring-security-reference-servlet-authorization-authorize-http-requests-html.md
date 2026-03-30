# Source: https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html

Title: Authorize HttpServletRequests :: Spring Security

URL Source: https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html

Published Time: Mon, 09 Mar 2026 15:09:15 GMT

Markdown Content:
Authorize HttpServletRequests :: Spring Security
===============

[![Image 1: Spring](https://docs.spring.io/spring-security/reference/_/img/spring-logo.svg)](https://spring.io/)

[Why Spring](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html#)

[Overview](https://spring.io/why-spring)[Microservices](https://spring.io/microservices)[Reactive](https://spring.io/reactive)[Event Driven](https://spring.io/event-driven)[Cloud](https://spring.io/cloud)[Web Applications](https://spring.io/web-applications)[Serverless](https://spring.io/serverless)[Batch](https://spring.io/batch)

[Learn](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html#)

[Overview](https://spring.io/learn)[Quickstart](https://spring.io/quickstart)[Guides](https://spring.io/guides)[Blog](https://spring.io/blog)

[Projects](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html#)

[Overview](https://spring.io/projects)[Spring Boot](https://spring.io/projects/spring-boot)[Spring Framework](https://spring.io/projects/spring-framework)[Spring Cloud](https://spring.io/projects/spring-cloud)[Spring Cloud Data Flow](https://spring.io/projects/spring-cloud-dataflow)[Spring Data](https://spring.io/projects/spring-data)[Spring Integration](https://spring.io/projects/spring-integration)[Spring Batch](https://spring.io/projects/spring-batch)[Spring Security](https://spring.io/projects/spring-security)[View all projects](https://spring.io/projects)*   DEVELOPMENT TOOLS
[Spring Tools 4](https://spring.io/tools)[Spring Initializr](https://start.spring.io/)

[Academy](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html#)

[Courses](https://spring.academy/courses)[Get Certified](https://spring.academy/learning-path)

[Solutions](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html#)

[Overview](https://spring.io/solutions)[Spring Runtime](https://spring.io/support)[Spring Consulting](https://spring.io/consulting)[Spring Academy For Teams](https://spring.academy/teams)[Security Advisories](https://spring.io/security)

[Community](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html#)

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

### Authorize HttpServletRequests

*   [Understanding How Request Authorization Components Work](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html#request-authorization-architecture)
*   [AuthorizationFilter Is Last By Default](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html#_authorizationfilter_is_last_by_default)
*   [All Dispatches Are Authorized](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html#_all_dispatches_are_authorized)
*   [Authentication Lookup is Deferred](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html#_authentication_lookup_is_deferred)
*   [Authorizing an Endpoint](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html#authorizing-endpoints)
*   [Matching Requests](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html#match-requests)
*   [Matching Using Ant](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html#match-by-ant)
*   [Matching Using Regular Expressions](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html#match-by-regex)
*   [Matching By Http Method](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html#match-by-httpmethod)
*   [Matching By Dispatcher Type](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html#match-by-dispatcher-type)
*   [Matching by Servlet Path](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html#match-by-mvc)
*   [Using a Custom Matcher](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html#match-by-custom)
*   [Authorizing Requests](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html#authorize-requests)
*   [Customizing Authorization Managers](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html#customizing-authorization-managers)
*   [Expressing Authorization with SpEL](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html#authorization-expressions)
*   [Using Authorization Expression Fields and Methods](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html#using-authorization-expression-fields-and-methods)
*   [Using Path Parameters](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html#using_path_parameters)
*   [Use an Authorization Database, Policy Agent, or Other Service](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html#remote-authorization-manager)
*   [Favor permitAll over ignoring](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html#favor-permitall)
*   [Migrating from authorizeRequests](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html#migrate-authorize-requests)
*   [Migrating Expressions](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html#_migrating_expressions)
*   [Security Matchers](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html#security-matchers)
*   [Further Reading](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html#_further_reading)

[Edit this Page](https://github.com/spring-projects/spring-security/blob/7.0.3/docs/modules/ROOT/pages/servlet/authorization/authorize-http-requests.adoc)[GitHub Project](https://github.com/spring-projects/spring-security "GitHub")[Stack Overflow](https://stackoverflow.com/tags/spring-security)

*   [Spring Security](https://docs.spring.io/spring-security/reference/index.html)
*   [Servlet Applications](https://docs.spring.io/spring-security/reference/servlet/index.html)
*   [Authorization](https://docs.spring.io/spring-security/reference/servlet/authorization/index.html)
*   [Authorize HTTP Requests](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html)

Authorize HttpServletRequests
=============================

### Authorize HttpServletRequests

*   [Understanding How Request Authorization Components Work](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html#request-authorization-architecture)
*   [AuthorizationFilter Is Last By Default](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html#_authorizationfilter_is_last_by_default)
*   [All Dispatches Are Authorized](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html#_all_dispatches_are_authorized)
*   [Authentication Lookup is Deferred](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html#_authentication_lookup_is_deferred)
*   [Authorizing an Endpoint](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html#authorizing-endpoints)
*   [Matching Requests](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html#match-requests)
*   [Matching Using Ant](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html#match-by-ant)
*   [Matching Using Regular Expressions](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html#match-by-regex)
*   [Matching By Http Method](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html#match-by-httpmethod)
*   [Matching By Dispatcher Type](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html#match-by-dispatcher-type)
*   [Matching by Servlet Path](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html#match-by-mvc)
*   [Using a Custom Matcher](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html#match-by-custom)
*   [Authorizing Requests](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html#authorize-requests)
*   [Customizing Authorization Managers](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html#customizing-authorization-managers)
*   [Expressing Authorization with SpEL](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html#authorization-expressions)
*   [Using Authorization Expression Fields and Methods](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html#using-authorization-expression-fields-and-methods)
*   [Using Path Parameters](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html#using_path_parameters)
*   [Use an Authorization Database, Policy Agent, or Other Service](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html#remote-authorization-manager)
*   [Favor permitAll over ignoring](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html#favor-permitall)
*   [Migrating from authorizeRequests](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html#migrate-authorize-requests)
*   [Migrating Expressions](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html#_migrating_expressions)
*   [Security Matchers](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html#security-matchers)
*   [Further Reading](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html#_further_reading)

Spring Security allows you to [model your authorization](https://docs.spring.io/spring-security/reference/servlet/authorization/index.html) at the request level. For example, with Spring Security you can say that all pages under `/admin` require one authority while all other pages simply require authentication.

By default, Spring Security requires that every request be authenticated. That said, any time you use [an `HttpSecurity` instance](https://docs.spring.io/spring-security/reference/servlet/configuration/java.html#jc-httpsecurity), it’s necessary to declare your authorization rules.

Whenever you have an `HttpSecurity` instance, you should at least do:

Use authorizeHttpRequests

*   Java

*   Kotlin

*   Xml

```java
http
    .authorizeHttpRequests((authorize) -> authorize
        .anyRequest().authenticated()
    )
```

Copied!

```kotlin
http {
    authorizeHttpRequests {
        authorize(anyRequest, authenticated)
    }
}
```

Copied!

```xml
<http>
    <intercept-url pattern="/**" access="authenticated"/>
</http>
```

Copied!

This tells Spring Security that any endpoint in your application requires that the security context at a minimum be authenticated in order to allow it.

In many cases, your authorization rules will be more sophisticated than that, so please consider the following use cases:

*   I have an app that uses `authorizeRequests` and I want to [migrate it to `authorizeHttpRequests`](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html#migrate-authorize-requests)

*   I want to [understand how the `AuthorizationFilter` components work](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html#request-authorization-architecture)

*   I want to [match requests](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html#match-requests) based on a pattern; specifically [regex](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html#match-by-regex)

*   I want to match request, and I map Spring MVC to [something other than the default servlet](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html#mvc-not-default-servlet)

*   I want to [authorize requests](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html#authorize-requests)

*   I want to [match a request programmatically](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html#match-by-custom)

*   I want to [authorize a request programmatically](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html#authorize-requests)

*   I want to [delegate request authorization](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html#remote-authorization-manager) to a policy agent

*   I want to [customize how authorization managers are created](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html#customizing-authorization-managers)

[](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html#request-authorization-architecture)Understanding How Request Authorization Components Work
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

This section builds on [Servlet Architecture and Implementation](https://docs.spring.io/spring-security/reference/servlet/architecture.html#servlet-architecture) by digging deeper into how [authorization](https://docs.spring.io/spring-security/reference/servlet/authorization/index.html#servlet-authorization) works at the request level in Servlet-based applications.

![Image 2: authorizationfilter](https://docs.spring.io/spring-security/reference/_images/servlet/authorization/authorizationfilter.png)

Figure 1. Authorize HttpServletRequest

*   ![Image 3: number 1](https://docs.spring.io/spring-security/reference/_images/icons/number_1.png) First, the `AuthorizationFilter` constructs a `Supplier` that retrieves an [Authentication](https://docs.spring.io/spring-security/reference/servlet/authentication/architecture.html#servlet-authentication-authentication) from the [SecurityContextHolder](https://docs.spring.io/spring-security/reference/servlet/authentication/architecture.html#servlet-authentication-securitycontextholder).

*   ![Image 4: number 2](https://docs.spring.io/spring-security/reference/_images/icons/number_2.png) Second, it passes the `Supplier<Authentication>` and the `HttpServletRequest` to the [`AuthorizationManager`](https://docs.spring.io/spring-security/reference/servlet/architecture.html#authz-authorization-manager). The `AuthorizationManager` matches the request to the patterns in `authorizeHttpRequests`, and runs the corresponding rule.

    *   ![Image 5: number 3](https://docs.spring.io/spring-security/reference/_images/icons/number_3.png) If authorization is denied, [an `AuthorizationDeniedEvent` is published](https://docs.spring.io/spring-security/reference/servlet/authorization/events.html), and an `AccessDeniedException` is thrown. In this case the [`ExceptionTranslationFilter`](https://docs.spring.io/spring-security/reference/servlet/architecture.html#servlet-exceptiontranslationfilter) handles the `AccessDeniedException`.

    *   ![Image 6: number 4](https://docs.spring.io/spring-security/reference/_images/icons/number_4.png) If access is granted, [an `AuthorizationGrantedEvent` is published](https://docs.spring.io/spring-security/reference/servlet/authorization/events.html) and `AuthorizationFilter` continues with the [FilterChain](https://docs.spring.io/spring-security/reference/servlet/architecture.html#servlet-filters-review) which allows the application to process normally.

### [](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html#_authorizationfilter_is_last_by_default)`AuthorizationFilter` Is Last By Default

The `AuthorizationFilter` is last in [the Spring Security filter chain](https://docs.spring.io/spring-security/reference/servlet/architecture.html#servlet-filterchain-figure) by default. This means that Spring Security’s [authentication filters](https://docs.spring.io/spring-security/reference/servlet/authentication/index.html), [exploit protections](https://docs.spring.io/spring-security/reference/servlet/exploits/index.html), and other filter integrations do not require authorization. If you add filters of your own before the `AuthorizationFilter`, they will also not require authorization; otherwise, they will.

A place where this typically becomes important is when you are adding [Spring MVC](https://docs.spring.io/spring-framework/reference/7.0.4/web.html#spring-web) endpoints. Because they are executed by the [`DispatcherServlet`](https://docs.spring.io/spring-framework/reference/7.0.4/web.html#mvc-servlet) and this comes after the `AuthorizationFilter`, your endpoints need to be [included in `authorizeHttpRequests` to be permitted](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html#authorizing-endpoints).

### [](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html#_all_dispatches_are_authorized)All Dispatches Are Authorized

The `AuthorizationFilter` runs not just on every request, but on every dispatch. This means that the `REQUEST` dispatch needs authorization, but also `FORWARD`s, `ERROR`s, and `INCLUDE`s.

For example, [Spring MVC](https://docs.spring.io/spring-framework/reference/7.0.4/web.html#spring-web) can `FORWARD` the request to a view resolver that renders a Thymeleaf template, like so:

Sample Forwarding Spring MVC Controller

*   Java

*   Kotlin

```java
@Controller
public class MyController {
    @GetMapping("/endpoint")
    public String endpoint() {
        return "endpoint";
    }
}
```

Copied!

```kotlin
@Controller
class MyController {
    @GetMapping("/endpoint")
    fun endpoint(): String {
        return "endpoint"
    }
}
```

Copied!

In this case, authorization happens twice; once for authorizing `/endpoint` and once for forwarding to Thymeleaf to render the "endpoint" template.

For that reason, you may want to [permit all `FORWARD` dispatches](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html#match-by-dispatcher-type).

Another example of this principle is [how Spring Boot handles errors](https://docs.spring.io/spring-boot/4.0.0-SNAPSHOT/reference/web/servlet.html#web.servlet.spring-mvc.error-handling). If the container catches an exception, say like the following:

Sample Erroring Spring MVC Controller

*   Java

*   Kotlin

```java
@Controller
public class MyController {
    @GetMapping("/endpoint")
    public String endpoint() {
        throw new UnsupportedOperationException("unsupported");
    }
}
```

Copied!

```kotlin
@Controller
class MyController {
    @GetMapping("/endpoint")
    fun endpoint(): String {
        throw UnsupportedOperationException("unsupported")
    }
}
```

Copied!

then Boot will dispatch it to the `ERROR` dispatch.

In that case, authorization also happens twice; once for authorizing `/endpoint` and once for dispatching the error.

For that reason, you may want to [permit all `ERROR` dispatches](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html#match-by-dispatcher-type).

### [](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html#_authentication_lookup_is_deferred)`Authentication` Lookup is Deferred

Remember that [the `AuthorizationManager` API uses a `Supplier<Authentication>`](https://docs.spring.io/spring-security/reference/servlet/authorization/architecture.html#_the_authorizationmanager).

This matters with `authorizeHttpRequests` when requests are [always permitted or always denied](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html#authorize-requests). In those cases, [the `Authentication`](https://docs.spring.io/spring-security/reference/servlet/authentication/architecture.html#servlet-authentication-authentication) is not queried, making for a faster request.

[](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html#authorizing-endpoints)Authorizing an Endpoint
----------------------------------------------------------------------------------------------------------------------------------------------------

You can configure Spring Security to have different rules by adding more rules in order of precedence.

If you want to require that `/endpoint` only be accessible by end users with the `USER` authority, then you can do:

Authorize an Endpoint

*   Java

*   Kotlin

*   Xml

```java
@Bean
public SecurityFilterChain web(HttpSecurity http) throws Exception {
    http
        .authorizeHttpRequests((authorize) -> authorize
	    .requestMatchers("/endpoint").hasAuthority("USER")
            .anyRequest().authenticated()
        )
        // ...

    return http.build();
}
```

Copied!

```kotlin
@Bean
fun web(http: HttpSecurity): SecurityFilterChain {
    http {
        authorizeHttpRequests {
            authorize("/endpoint", hasAuthority("USER"))
            authorize(anyRequest, authenticated)
        }
    }

    return http.build()
}
```

Copied!

```xml
<http>
    <intercept-url pattern="/endpoint" access="hasAuthority('USER')"/>
    <intercept-url pattern="/**" access="authenticated"/>
</http>
```

Copied!

As you can see, the declaration can be broken up in to pattern/rule pairs.

`AuthorizationFilter` processes these pairs in the order listed, applying only the first match to the request. This means that even though `/**` would also match for `/endpoint` the above rules are not a problem. The way to read the above rules is "if the request is `/endpoint`, then require the `USER` authority; else, only require authentication".

Spring Security supports several patterns and several rules; you can also programmatically create your own of each.

Once authorized, you can test it using [Security’s test support](https://docs.spring.io/spring-security/reference/servlet/test/method.html#test-method-withmockuser) in the following way:

Test Endpoint Authorization

*   Java

```java
@WithMockUser(authorities="USER")
@Test
void endpointWhenUserAuthorityThenAuthorized() {
    this.mvc.perform(get("/endpoint"))
        .andExpect(status().isOk());
}

@WithMockUser
@Test
void endpointWhenNotUserAuthorityThenForbidden() {
    this.mvc.perform(get("/endpoint"))
        .andExpect(status().isForbidden());
}

@Test
void anyWhenUnauthenticatedThenUnauthorized() {
    this.mvc.perform(get("/any"))
        .andExpect(status().isUnauthorized());
}
```

Copied!

[](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html#match-requests)Matching Requests
---------------------------------------------------------------------------------------------------------------------------------------

Above you’ve already seen [two ways to match requests](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html#authorizing-endpoints).

The first you saw was the simplest, which is to match any request.

The second is to match by a URI pattern. Spring Security supports two languages for URI pattern-matching: [Ant](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html#match-by-ant) (as seen above) and [Regular Expressions](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html#match-by-regex).

### [](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html#match-by-ant)Matching Using Ant

Ant is the default language that Spring Security uses to match requests.

You can use it to match a single endpoint or a directory, and you can even capture placeholders for later use. You can also refine it to match a specific set of HTTP methods.

Let’s say that you instead of wanting to match the `/endpoint` endpoint, you want to match all endpoints under the `/resource` directory. In that case, you can do something like the following:

Match with Ant

*   Java

*   Kotlin

*   Xml

```java
http
    .authorizeHttpRequests((authorize) -> authorize
        .requestMatchers("/resource/**").hasAuthority("USER")
        .anyRequest().authenticated()
    )
```

Copied!

```kotlin
http {
    authorizeHttpRequests {
        authorize("/resource/**", hasAuthority("USER"))
        authorize(anyRequest, authenticated)
    }
}
```

Copied!

```xml
<http>
    <intercept-url pattern="/resource/**" access="hasAuthority('USER')"/>
    <intercept-url pattern="/**" access="authenticated"/>
</http>
```

Copied!

The way to read this is "if the request is `/resource` or some subdirectory, require the `USER` authority; otherwise, only require authentication"

You can also extract path values from the request, as seen below:

Authorize and Extract

*   Java

*   Kotlin

*   Xml

```java
http
    .authorizeHttpRequests((authorize) -> authorize
        .requestMatchers("/resource/{name}").access(new WebExpressionAuthorizationManager("#name == authentication.name"))
        .anyRequest().authenticated()
    )
```

Copied!

```kotlin
http {
    authorizeHttpRequests {
        authorize("/resource/{name}", WebExpressionAuthorizationManager("#name == authentication.name"))
        authorize(anyRequest, authenticated)
    }
}
```

Copied!

```xml
<http>
    <intercept-url pattern="/resource/{name}" access="#name == authentication.name"/>
    <intercept-url pattern="/**" access="authenticated"/>
</http>
```

Copied!

Once authorized, you can test it using [Security’s test support](https://docs.spring.io/spring-security/reference/servlet/test/method.html#test-method-withmockuser) in the following way:

Test Directory Authorization

*   Java

```java
@WithMockUser(authorities="USER")
@Test
void endpointWhenUserAuthorityThenAuthorized() {
    this.mvc.perform(get("/endpoint/jon"))
        .andExpect(status().isOk());
}

@WithMockUser
@Test
void endpointWhenNotUserAuthorityThenForbidden() {
    this.mvc.perform(get("/endpoint/jon"))
        .andExpect(status().isForbidden());
}

@Test
void anyWhenUnauthenticatedThenUnauthorized() {
    this.mvc.perform(get("/any"))
        .andExpect(status().isUnauthorized());
}
```

Copied!

Spring Security only matches paths. If you want to match query parameters, you will need a custom request matcher.

### [](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html#match-by-regex)Matching Using Regular Expressions

Spring Security supports matching requests against a regular expression. This can come in handy if you want to apply more strict matching criteria than `**` on a subdirectory.

For example, consider a path that contains the username and the rule that all usernames must be alphanumeric. You can use [`RegexRequestMatcher`](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/util/matcher/RegexRequestMatcher.html) to respect this rule, like so:

Match with Regex

*   Java

*   Kotlin

*   Xml

```java
http
    .authorizeHttpRequests((authorize) -> authorize
        .requestMatchers(RegexRequestMatcher.regexMatcher("/resource/[A-Za-z0-9]+")).hasAuthority("USER")
        .anyRequest().denyAll()
    )
```

Copied!

```kotlin
http {
    authorizeHttpRequests {
        authorize(RegexRequestMatcher.regexMatcher("/resource/[A-Za-z0-9]+"), hasAuthority("USER"))
        authorize(anyRequest, denyAll)
    }
}
```

Copied!

```xml
<http>
    <intercept-url request-matcher="regex" pattern="/resource/[A-Za-z0-9]+" access="hasAuthority('USER')"/>
    <intercept-url pattern="/**" access="denyAll"/>
</http>
```

Copied!

### [](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html#match-by-httpmethod)Matching By Http Method

You can also match rules by HTTP method. One place where this is handy is when authorizing by permissions granted, like being granted a `read` or `write` privilege.

To require all `GET`s to have the `read` permission and all `POST`s to have the `write` permission, you can do something like this:

Match by HTTP Method

*   Java

*   Kotlin

*   Xml

```java
http
    .authorizeHttpRequests((authorize) -> authorize
        .requestMatchers(HttpMethod.GET).hasAuthority("read")
        .requestMatchers(HttpMethod.POST).hasAuthority("write")
        .anyRequest().denyAll()
    )
```

Copied!

```kotlin
http {
    authorizeHttpRequests {
        authorize(HttpMethod.GET, hasAuthority("read"))
        authorize(HttpMethod.POST, hasAuthority("write"))
        authorize(anyRequest, denyAll)
    }
}
```

Copied!

```xml
<http>
    <intercept-url http-method="GET" pattern="/**" access="hasAuthority('read')"/>
    <intercept-url http-method="POST" pattern="/**" access="hasAuthority('write')"/>
    <intercept-url pattern="/**" access="denyAll"/>
</http>
```

Copied!

These authorization rules should read as: "if the request is a GET, then require `read` permission; else, if the request is a POST, then require `write` permission; else, deny the request"

Denying the request by default is a healthy security practice since it turns the set of rules into an allow list.

Once authorized, you can test it using [Security’s test support](https://docs.spring.io/spring-security/reference/servlet/test/method.html#test-method-withmockuser) in the following way:

Test Http Method Authorization

*   Java

```java
@WithMockUser(authorities="read")
@Test
void getWhenReadAuthorityThenAuthorized() {
    this.mvc.perform(get("/any"))
        .andExpect(status().isOk());
}

@WithMockUser
@Test
void getWhenNoReadAuthorityThenForbidden() {
    this.mvc.perform(get("/any"))
        .andExpect(status().isForbidden());
}

@WithMockUser(authorities="write")
@Test
void postWhenWriteAuthorityThenAuthorized() {
    this.mvc.perform(post("/any").with(csrf()))
        .andExpect(status().isOk());
}

@WithMockUser(authorities="read")
@Test
void postWhenNoWriteAuthorityThenForbidden() {
    this.mvc.perform(get("/any").with(csrf()))
        .andExpect(status().isForbidden());
}
```

Copied!

### [](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html#match-by-dispatcher-type)Matching By Dispatcher Type

This feature is not currently supported in XML

As stated earlier, Spring Security [authorizes all dispatcher types by default](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html#_all_dispatches_are_authorized). And even though [the security context](https://docs.spring.io/spring-security/reference/servlet/authentication/architecture.html#servlet-authentication-securitycontext) established on the `REQUEST` dispatch carries over to subsequent dispatches, subtle mismatches can sometimes cause an unexpected `AccessDeniedException`.

To address that, you can configure Spring Security Java configuration to allow dispatcher types like `FORWARD` and `ERROR`, like so:

Match by Dispatcher Type

*   Java

*   Kotlin

```java
http
    .authorizeHttpRequests((authorize) -> authorize
        .dispatcherTypeMatchers(DispatcherType.FORWARD, DispatcherType.ERROR).permitAll()
        .requestMatchers("/endpoint").permitAll()
        .anyRequest().denyAll()
    )
```

Copied!

```kotlin
http {
    authorizeHttpRequests {
        authorize(DispatcherTypeRequestMatcher(DispatcherType.FORWARD), permitAll)
        authorize(DispatcherTypeRequestMatcher(DispatcherType.ERROR), permitAll)
        authorize("/endpoint", permitAll)
        authorize(anyRequest, denyAll)
    }
}
```

Copied!

### [](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html#match-by-mvc)Matching by Servlet Path

Generally speaking, you can use `requestMatchers(String)` as demonstrated above.

However, if you have authorization rules from multiple servlets, you need to specify those:

Match by PathPatternRequestMatcher

*   Java

*   Kotlin

*   Xml

```java
import static org.springframework.security.web.servlet.util.matcher.PathPatternRequestMatcher.withDefaults;

@Bean
SecurityFilterChain appEndpoints(HttpSecurity http) {
	PathPatternRequestMatcher.Builder mvc = withDefaults().basePath("/spring-mvc");
	http
        .authorizeHttpRequests((authorize) -> authorize
            .requestMatchers(mvc.matcher("/admin/**")).hasAuthority("admin")
            .requestMatchers(mvc.matcher("/my/controller/**")).hasAuthority("controller")
            .anyRequest().authenticated()
        );

	return http.build();
}
```

Copied!

```kotlin
@Bean
fun appEndpoints(http: HttpSecurity): SecurityFilterChain {
    http {
        authorizeHttpRequests {
            authorize("/spring-mvc", "/admin/**", hasAuthority("admin"))
            authorize("/spring-mvc", "/my/controller/**", hasAuthority("controller"))
            authorize(anyRequest, authenticated)
        }
    }
}
```

Copied!

```xml
<http>
    <intercept-url servlet-path="/spring-mvc" pattern="/admin/**" access="hasAuthority('admin')"/>
    <intercept-url servlet-path="/spring-mvc" pattern="/my/controller/**" access="hasAuthority('controller')"/>
    <intercept-url pattern="/**" access="authenticated"/>
</http>
```

Copied!

This is because Spring Security requires all URIs to be absolute (minus the context path).

There are several other components that create request matchers for you like [`PathRequest#toStaticResources#atCommonLocations`](https://docs.spring.io/spring-boot/4.0.0-SNAPSHOT/api/java/org/springframework/boot/security/autoconfigure/web/servlet/PathRequest.html)

### [](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html#match-by-custom)Using a Custom Matcher

This feature is not currently supported in XML

In Java configuration, you can create your own [`RequestMatcher`](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/util/matcher/RequestMatcher.html) and supply it to the DSL like so:

Authorize by Dispatcher Type

*   Java

*   Kotlin

```java
RequestMatcher printview = (request) -> request.getParameter("print") != null;
http
    .authorizeHttpRequests((authorize) -> authorize
        .requestMatchers(printview).hasAuthority("print")
        .anyRequest().authenticated()
    )
```

Copied!

```kotlin
val printview: RequestMatcher = { (request) -> request.getParameter("print") != null }
http {
    authorizeHttpRequests {
        authorize(printview, hasAuthority("print"))
        authorize(anyRequest, authenticated)
    }
}
```

Copied!

Because [`RequestMatcher`](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/util/matcher/RequestMatcher.html) is a functional interface, you can supply it as a lambda in the DSL. However, if you want to extract values from the request, you will need to have a concrete class since that requires overriding a `default` method.

Once authorized, you can test it using [Security’s test support](https://docs.spring.io/spring-security/reference/servlet/test/method.html#test-method-withmockuser) in the following way:

Test Custom Authorization

*   Java

```java
@WithMockUser(authorities="print")
@Test
void printWhenPrintAuthorityThenAuthorized() {
    this.mvc.perform(get("/any?print"))
        .andExpect(status().isOk());
}

@WithMockUser
@Test
void printWhenNoPrintAuthorityThenForbidden() {
    this.mvc.perform(get("/any?print"))
        .andExpect(status().isForbidden());
}
```

Copied!

[](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html#authorize-requests)Authorizing Requests
----------------------------------------------------------------------------------------------------------------------------------------------

Once a request is matched, you can authorize it in several ways [already seen](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html#match-requests) like `permitAll`, `denyAll`, and `hasAuthority`.

As a quick summary, here are the authorization rules built into the DSL:

*   `permitAll` - The request requires no authorization and is a public endpoint; note that in this case, [the `Authentication`](https://docs.spring.io/spring-security/reference/servlet/authentication/architecture.html#servlet-authentication-authentication) is never retrieved from the session

*   `denyAll` - The request is not allowed under any circumstances; note that in this case, the `Authentication` is never retrieved from the session

*   `hasAuthority` - The request requires that the `Authentication` have [a `GrantedAuthority`](https://docs.spring.io/spring-security/reference/servlet/authorization/architecture.html#authz-authorities) that matches the given value

*   `hasRole` - A shortcut for `hasAuthority` that prefixes `ROLE_` or whatever is configured as the default prefix

*   `hasAnyAuthority` - The request requires that the `Authentication` have a `GrantedAuthority` that matches any of the given values

*   `hasAnyRole` - A shortcut for `hasAnyAuthority` that prefixes `ROLE_` or whatever is configured as the default prefix* `hasAnyAuthority` - The request requires that the `Authentication` have a `GrantedAuthority` that matches any of the given values

*   `hasAllRoles` - A shortcut for `hasAllAuthorities` that prefixes `ROLE_` or whatever is configured as the default prefix

*   `hasAllAuthorities` - The request requires that the `Authentication` have a `GrantedAuthority` that matches all of the given values

*   `access` - The request uses this custom `AuthorizationManager` to determine access

Having now learned the patterns, rules, and how they can be paired together, you should be able to understand what is going on in this more complex example:

Authorize Requests

*   Java

```java
import static jakarta.servlet.DispatcherType.*;

import static org.springframework.security.authorization.AuthorizationManagers.allOf;
import static org.springframework.security.authorization.AuthorityAuthorizationManager.hasAuthority;
import static org.springframework.security.authorization.AuthorityAuthorizationManager.hasRole;

@Bean
SecurityFilterChain web(HttpSecurity http) throws Exception {
	http
		// ...
		.authorizeHttpRequests((authorize) -> authorize                                  (1)
            .dispatcherTypeMatchers(FORWARD, ERROR).permitAll() (2)
			.requestMatchers("/static/**", "/signup", "/about").permitAll()         (3)
			.requestMatchers("/admin/**").hasRole("ADMIN")                             (4)
			.requestMatchers("/db/**").hasAllAuthorities("db", "ROLE_ADMIN")   (5)
			.anyRequest().denyAll()                                                (6)
		);

	return http.build();
}
```

Copied!

**1**There are multiple authorization rules specified. Each rule is considered in the order they were declared.
**2**Dispatches `FORWARD` and `ERROR` are permitted to allow [Spring MVC](https://docs.spring.io/spring-framework/reference/7.0.4/web.html#spring-web) to render views and Spring Boot to render errors
**3**We specified multiple URL patterns that any user can access. Specifically, any user can access a request if the URL starts with "/static/", equals "/signup", or equals "/about".
**4**Any URL that starts with "/admin/" will be restricted to users who have the role "ROLE_ADMIN". You will notice that since we are invoking the `hasRole` method we do not need to specify the "ROLE_" prefix.
**5**Any URL that starts with "/db/" requires the user to have both been granted the "db" permission as well as be a "ROLE_ADMIN". You will notice that since we are using the `hasAllAuthorities` expression we must specify the "ROLE_" prefix.
**6**Any URL that has not already been matched on is denied access. This is a good strategy if you do not want to accidentally forget to update your authorization rules.

[](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html#customizing-authorization-managers)Customizing Authorization Managers
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

When you use the `authorizeHttpRequests` DSL, Spring Security takes care of creating the appropriate `AuthorizationManager` instances for you. In certain cases, you may want to customize what is created in order to have complete control over how authorization decisions are made [at the framework level](https://docs.spring.io/spring-security/reference/servlet/authorization/architecture.html#authz-delegate-authorization-manager).

In order to take control of creating instances of `AuthorizationManager` for authorizing HTTP requests, you can create a custom [`AuthorizationManagerFactory`](https://docs.spring.io/spring-security/reference/servlet/authorization/architecture.html#authz-authorization-manager-factory). For example, let’s say you want to create a convention that authenticated users must be authenticated _AND_ have the `USER` role. To do this, you can create a custom implementation for HTTP requests as in the following example:

*   Java

*   Kotlin

```java
@Component
public class CustomHttpRequestsAuthorizationManagerFactory
		implements AuthorizationManagerFactory<RequestAuthorizationContext> {

	private final AuthorizationManagerFactory<RequestAuthorizationContext> delegate =
			new DefaultAuthorizationManagerFactory<>();

	@Override
	public AuthorizationManager<RequestAuthorizationContext> authenticated() {
		return AuthorizationManagers.allOf(
			this.delegate.authenticated(),
			this.delegate.hasRole("USER")
		);
	}

}
```

Copied!

```kotlin
@Component
class CustomHttpRequestsAuthorizationManagerFactory : AuthorizationManagerFactory<RequestAuthorizationContext> {
    private val delegate = DefaultAuthorizationManagerFactory<RequestAuthorizationContext>()

    override fun authenticated(): AuthorizationManager<RequestAuthorizationContext> {
        return AuthorizationManagers.allOf(
            delegate.authenticated(),
            delegate.hasRole("USER")
        )
    }
}
```

Copied!

Now, whenever you [require authentication](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html#activate-request-security), Spring Security will automatically invoke your custom factory to create an instance of `AuthorizationManager` that requires authentication _AND_ the `USER` role.

We use this as a simple example of creating a custom `AuthorizationManagerFactory`, though it is also possible (and often simpler) to replace a specific `AuthorizationManager` only for a particular request. See [Use an Authorization Database, Policy Agent, or Other Service](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html#remote-authorization-manager) for an example.

[](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html#authorization-expressions)Expressing Authorization with SpEL
-------------------------------------------------------------------------------------------------------------------------------------------------------------------

While using a concrete `AuthorizationManager` is recommended, there are some cases where an expression is necessary, like with `<intercept-url>` or with JSP Taglibs. For that reason, this section will focus on examples from those domains.

Given that, let’s cover Spring Security’s Web Security Authorization SpEL API a bit more in depth.

Spring Security encapsulates all of its authorization fields and methods in a set of root objects. The most generic root object is called `SecurityExpressionRoot` and it forms the basis for `WebSecurityExpressionRoot`. Spring Security supplies this root object to `StandardEvaluationContext` when preparing to evaluate an authorization expression.

### [](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html#using-authorization-expression-fields-and-methods)Using Authorization Expression Fields and Methods

The first thing this provides is an enhanced set of authorization fields and methods to your SpEL expressions. What follows is a quick overview of the most common methods:

*   `permitAll` - The request requires no authorization to be invoked; note that in this case, [the `Authentication`](https://docs.spring.io/spring-security/reference/servlet/authentication/architecture.html#servlet-authentication-authentication) is never retrieved from the session

*   `denyAll` - The request is not allowed under any circumstances; note that in this case, the `Authentication` is never retrieved from the session

*   `hasAuthority` - The request requires that the `Authentication` have [a `GrantedAuthority`](https://docs.spring.io/spring-security/reference/servlet/authorization/architecture.html#authz-authorities) that matches the given value

*   `hasRole` - A shortcut for `hasAuthority` that prefixes `ROLE_` or whatever is configured as the default prefix

*   `hasAnyAuthority` - The request requires that the `Authentication` have a `GrantedAuthority` that matches any of the given values

*   `hasAnyRole` - A shortcut for `hasAnyAuthority` that prefixes `ROLE_` or whatever is configured as the default prefix

*   `hasPermission` - A hook into your `PermissionEvaluator` instance for doing object-level authorization

And here is a brief look at the most common fields:

*   `authentication` - The `Authentication` instance associated with this method invocation

*   `principal` - The `Authentication#getPrincipal` associated with this method invocation

Having now learned the patterns, rules, and how they can be paired together, you should be able to understand what is going on in this more complex example:

Authorize Requests Using SpEL

*   Xml

```java
<http>
    <intercept-url pattern="/static/**" access="permitAll"/> (1)
    <intercept-url pattern="/admin/**" access="hasRole('ADMIN')"/> (2)
    <intercept-url pattern="/db/**" access="hasAuthority('db') and hasRole('ADMIN')"/> (3)
    <intercept-url pattern="/**" access="denyAll"/> (4)
</http>
```

Copied!

**1**We specified a URL pattern that any user can access. Specifically, any user can access a request if the URL starts with "/static/".
**2**Any URL that starts with "/admin/" will be restricted to users who have the role "ROLE_ADMIN". You will notice that since we are invoking the `hasRole` method we do not need to specify the "ROLE_" prefix.
**3**Any URL that starts with "/db/" requires the user to have both been granted the "db" permission as well as be a "ROLE_ADMIN". You will notice that since we are using the `hasRole` expression we do not need to specify the "ROLE_" prefix.
**4**Any URL that has not already been matched on is denied access. This is a good strategy if you do not want to accidentally forget to update your authorization rules.

### [](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html#using_path_parameters)Using Path Parameters

Additionally, Spring Security provides a mechanism for discovering path parameters so they can also be accessed in the SpEL expression as well.

For example, you can access a path parameter in your SpEL expression in the following way:

Authorize Request using SpEL path variable

*   Xml

```xml
<http>
    <intercept-url pattern="/resource/{name}" access="#name == authentication.name"/>
    <intercept-url pattern="/**" access="authenticated"/>
</http>
```

Copied!

This expression refers to the path variable after `/resource/` and requires that it is equal to `Authentication#getName`.

### [](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html#remote-authorization-manager)Use an Authorization Database, Policy Agent, or Other Service

If you want to configure Spring Security to use a separate service for authorization, you can create your own `AuthorizationManager` and match it to `anyRequest`.

First, your `AuthorizationManager` may look something like this:

Open Policy Agent Authorization Manager

*   Java

```java
@Component
public final class OpenPolicyAgentAuthorizationManager implements AuthorizationManager<RequestAuthorizationContext> {
    @Override
    public AuthorizationResult authorize(Supplier<Authentication> authentication, RequestAuthorizationContext context) {
        // make request to Open Policy Agent
    }
}
```

Copied!

Then, you can wire it into Spring Security in the following way:

Any Request Goes to Remote Service

*   Java

```java
@Bean
SecurityFilterChain web(HttpSecurity http, AuthorizationManager<RequestAuthorizationContext> authz) throws Exception {
	http
		// ...
		.authorizeHttpRequests((authorize) -> authorize
            .anyRequest().access(authz)
		);

	return http.build();
}
```

Copied!

### [](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html#favor-permitall)Favor `permitAll` over `ignoring`

When you have static resources it can be tempting to configure the filter chain to ignore these values. A more secure approach is to permit them using `permitAll` like so:

Permit Static Resources

*   Java

*   Kotlin

```java
http
    .authorizeHttpRequests((authorize) -> authorize
        .requestMatchers("/css/**").permitAll()
        .anyRequest().authenticated()
    )
```

Copied!

```kotlin
http {
    authorizeHttpRequests {
        authorize("/css/**", permitAll)
        authorize(anyRequest, authenticated)
    }
}
```

Copied!

It’s more secure because even with static resources it’s important to write secure headers, which Spring Security cannot do if the request is ignored.

In this past, this came with a performance tradeoff since the session was consulted by Spring Security on every request. As of Spring Security 6, however, the session is no longer pinged unless required by the authorization rule. Because the performance impact is now addressed, Spring Security recommends using at least `permitAll` for all requests.

[](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html#migrate-authorize-requests)Migrating from `authorizeRequests`
--------------------------------------------------------------------------------------------------------------------------------------------------------------------

`AuthorizationFilter` supersedes [`FilterSecurityInterceptor`](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/access/intercept/FilterSecurityInterceptor.html). To remain backward compatible, `FilterSecurityInterceptor` remains the default. This section discusses how `AuthorizationFilter` works and how to override the default configuration.

The [`AuthorizationFilter`](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/access/intercept/AuthorizationFilter.html) provides [authorization](https://docs.spring.io/spring-security/reference/servlet/authorization/index.html#servlet-authorization) for `HttpServletRequest`s. It is inserted into the [FilterChainProxy](https://docs.spring.io/spring-security/reference/servlet/architecture.html#servlet-filterchainproxy) as one of the [Security Filters](https://docs.spring.io/spring-security/reference/servlet/architecture.html#servlet-security-filters).

You can override the default when you declare a `SecurityFilterChain`. Instead of using [authorizeRequests](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/config/annotation/web/builders/HttpSecurity.html#authorizeRequests()), use `authorizeHttpRequests`, like so:

Use authorizeHttpRequests

*   Java

```java
@Bean
SecurityFilterChain web(HttpSecurity http) throws AuthenticationException {
    http
        .authorizeHttpRequests((authorize) -> authorize
            .anyRequest().authenticated();
        )
        // ...

    return http.build();
}
```

Copied!

This improves on `authorizeRequests` in a number of ways:

1.   Uses the simplified `AuthorizationManager` API instead of metadata sources, config attributes, decision managers, and voters. This simplifies reuse and customization.

2.   Delays `Authentication` lookup. Instead of the authentication needing to be looked up for every request, it will only look it up in requests where an authorization decision requires authentication.

3.   Bean-based configuration support.

When `authorizeHttpRequests` is used instead of `authorizeRequests`, then [`AuthorizationFilter`](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/access/intercept/AuthorizationFilter.html) is used instead of [`FilterSecurityInterceptor`](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/access/intercept/FilterSecurityInterceptor.html).

### [](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html#_migrating_expressions)Migrating Expressions

Where possible, it is recommended that you use type-safe authorization managers instead of SpEL. For Java configuration, [`WebExpressionAuthorizationManager`](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/access/expression/WebExpressionAuthorizationManager.html) is available to help migrate legacy SpEL.

To use `WebExpressionAuthorizationManager`, you can construct one with the expression you are trying to migrate, like so:

*   Java

*   Kotlin

```java
.requestMatchers("/test/**").access(new WebExpressionAuthorizationManager("hasRole('ADMIN') && hasRole('USER')"))
```

Copied!

```kotlin
.requestMatchers("/test/**").access(WebExpressionAuthorizationManager("hasRole('ADMIN') && hasRole('USER')"))
```

Copied!

To migrate several, you can use `WebExpressionAuthorizationManager#withDefaults`:

*   Java

*   Kotlin

```java
WebExpressionAuthorizationManager.Builder authz = WebExpressionAuthorizationManager.withDefaults();
.requestMatchers("/test/**").access(authz.expression("hasRole('ADMIN') && hasRole('USER')"))
.requestMatchers("/test/**").access(authz.expression("permitAll"))
```

Copied!

```kotlin
var authz = WebExpressionAuthorizationManager.withDefaults()
.requestMatchers("/test/**").access(authz.expression("hasRole('ADMIN') && hasRole('USER')"))
.requestMatchers("/test/**").access(authz.expression("permitAll"))
```

Copied!

If you are referring to a bean in your expression like so: `@webSecurity.check(authentication, request)`, it’s recommended that you instead call the bean directly, which will look something like the following:

*   Java

*   Kotlin

```java
.requestMatchers("/test/**").access((authentication, context) ->
    new AuthorizationDecision(webSecurity.check(authentication.get(), context.getRequest())))
```

Copied!

```kotlin
.requestMatchers("/test/**").access((authentication, context): AuthorizationManager<RequestAuthorizationContext> ->
    AuthorizationDecision(webSecurity.check(authentication.get(), context.getRequest())))
```

Copied!

For complex instructions that include bean references as well as other expressions, it is recommended that you change those to implement `AuthorizationManager` and refer to them by calling `.access(AuthorizationManager)`.

If you are not able to do that, you can publish [`WebExpressionAuthorizationManager.Builder`](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/access/expression/WebExpressionAuthorizationManager.Builder.html) as a bean:

*   Java

*   Kotlin

```java
@Bean
WebExpressionAuthorizationManager.Builder authz() {
	return WebExpressionAuthorizationManager.withDefaults();
}
```

Copied!

```kotlin
@Bean
fun authz(): WebExpressionAuthorizationManager.Builder {
	return WebExpressionAuthorizationManager.withDefaults()
}
```

Copied!

Then, expressions passed to that builder will be able to refer to beans.

[](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html#security-matchers)Security Matchers
------------------------------------------------------------------------------------------------------------------------------------------

The [`RequestMatcher`](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/util/matcher/RequestMatcher.html) interface is used to determine if a request matches a given rule. We use `securityMatchers` to determine if [a given `HttpSecurity`](https://docs.spring.io/spring-security/reference/servlet/configuration/java.html#jc-httpsecurity) should be applied to a given request. The same way, we can use `requestMatchers` to determine the authorization rules that we should apply to a given request. Look at the following example:

*   Java

*   Kotlin

```java
@Configuration
@EnableWebSecurity
public class SecurityConfig {

	@Bean
	public SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
		http
			.securityMatcher("/api/**")                            (1)
			.authorizeHttpRequests((authorize) -> authorize
				.requestMatchers("/api/user/**").hasRole("USER")   (2)
				.requestMatchers("/api/admin/**").hasRole("ADMIN") (3)
				.anyRequest().authenticated()                      (4)
			)
			.formLogin(withDefaults());
		return http.build();
	}
}
```

Copied!

```kotlin
@Configuration
@EnableWebSecurity
open class SecurityConfig {

    @Bean
    open fun web(http: HttpSecurity): SecurityFilterChain {
        http {
            securityMatcher("/api/**")                                           (1)
            authorizeHttpRequests {
                authorize("/api/user/**", hasRole("USER"))                       (2)
                authorize("/api/admin/**", hasRole("ADMIN"))                     (3)
                authorize(anyRequest, authenticated)                             (4)
            }
        }
        return http.build()
    }

}
```

Copied!

**1**Configure `HttpSecurity` to only be applied to URLs that start with `/api/`
**2**Allow access to URLs that start with `/api/user/` to users with the `USER` role
**3**Allow access to URLs that start with `/api/admin/` to users with the `ADMIN` role
**4**Any other request that doesn’t match the rules above, will require authentication

The `securityMatcher(s)` and `requestMatcher(s)` methods will construct `RequestMatcher`s using a [`PathPatternRequestMatcher.Builder`](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/servlet/util/matcher/PathPatternRequestMatcher.Builder.html) bean, if available. You can read more about the Spring MVC integration [here](https://docs.spring.io/spring-security/reference/servlet/integrations/mvc.html).

If you want to use a specific `RequestMatcher`, just pass an implementation to the `securityMatcher` and/or `requestMatcher` methods:

*   Java

*   Kotlin

```java
import static org.springframework.security.web.servlet.util.matcher.PathPatternRequestMatcher.withDefaults; (1)
import static org.springframework.security.web.util.matcher.RegexRequestMatcher.regexMatcher;

@Configuration
@EnableWebSecurity
public class SecurityConfig {

	@Bean
	public SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
		http
			.securityMatcher(antMatcher("/api/**"))                              (2)
			.authorizeHttpRequests((authorize) -> authorize
				.requestMatchers(withDefaults().matcher("/api/user/**")).hasRole("USER")     (3)
				.requestMatchers(regexMatcher("/api/admin/.*")).hasRole("ADMIN") (4)
				.requestMatchers(new MyCustomRequestMatcher()).hasRole("SUPERVISOR")     (5)
				.anyRequest().authenticated()
			)
			.formLogin(withDefaults());
		return http.build();
	}
}

public class MyCustomRequestMatcher implements RequestMatcher {

    @Override
    public boolean matches(HttpServletRequest request) {
        // ...
    }
}
```

Copied!

```kotlin
import org.springframework.security.web.servlet.util.matcher.PathPatternRequestMatcher.withDefaults (1)
import org.springframework.security.web.util.matcher.RegexRequestMatcher.regexMatcher

@Configuration
@EnableWebSecurity
open class SecurityConfig {

    @Bean
    open fun web(http: HttpSecurity): SecurityFilterChain {
        http {
            securityMatcher(antMatcher("/api/**"))                               (2)
            authorizeHttpRequests {
                authorize(withDefaults().matcher("/api/user/**"), hasRole("USER"))           (3)
                authorize(regexMatcher("/api/admin/**"), hasRole("ADMIN"))       (4)
                authorize(MyCustomRequestMatcher(), hasRole("SUPERVISOR"))       (5)
                authorize(anyRequest, authenticated)
            }
        }
        return http.build()
    }

}
```

Copied!

**1**Import the static factory methods from `PathPatternRequestMatcher` and `RegexRequestMatcher` to create `RequestMatcher` instances.
**2**Configure `HttpSecurity` to only be applied to URLs that start with `/api/`, using `PathPatternRequestMatcher`
**3**Allow access to URLs that start with `/api/user/` to users with the `USER` role, using `PathPatternRequestMatcher`
**4**Allow access to URLs that start with `/api/admin/` to users with the `ADMIN` role, using `RegexRequestMatcher`
**5**Allow access to URLs that match the `MyCustomRequestMatcher` to users with the `SUPERVISOR` role, using a custom `RequestMatcher`

[](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html#_further_reading)Further Reading
---------------------------------------------------------------------------------------------------------------------------------------

Now that you have secured your application’s requests, consider [securing its methods](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html). You can also read further on [testing your application](https://docs.spring.io/spring-security/reference/servlet/test/index.html) or on integrating Spring Security with other aspects of you application like [the data layer](https://docs.spring.io/spring-security/reference/servlet/integrations/data.html) or [tracing and metrics](https://docs.spring.io/spring-security/reference/servlet/integrations/observability.html).

*   [Spring Security](https://docs.spring.io/spring-security/reference/index.html) 

 Stable  
    *   [7.0.3](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html)
    *   [6.5.8](https://docs.spring.io/spring-security/reference/6.5/servlet/authorization/authorize-http-requests.html)

 Preview 

    *   [7.1.0-M2](https://docs.spring.io/spring-security/reference/7.1/servlet/authorization/authorize-http-requests.html)

 Snapshot 

    *   [7.1.0-SNAPSHOT](https://docs.spring.io/spring-security/reference/7.1-SNAPSHOT/servlet/authorization/authorize-http-requests.html)
    *   [7.0.4-SNAPSHOT](https://docs.spring.io/spring-security/reference/7.0-SNAPSHOT/servlet/authorization/authorize-http-requests.html)
    *   [6.5.9-SNAPSHOT](https://docs.spring.io/spring-security/reference/6.5-SNAPSHOT/servlet/authorization/authorize-http-requests.html)

*    Related Spring Documentation 
    *   [Spring Framework](https://docs.spring.io/spring-framework/reference/)
    *   [](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html)[Spring Security](https://docs.spring.io/spring-security/reference/)
        *   [Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/)
        *   [Spring LDAP](https://docs.spring.io/spring-ldap/reference/)
        *   [Spring Security Kerberos](https://docs.spring.io/spring-security-kerberos/reference/)
        *   [Spring Session](https://docs.spring.io/spring-session/reference/)
        *   [Spring Vault](https://docs.spring.io/spring-vault/reference/)

    *   [Spring GraphQL](https://docs.spring.io/spring-graphql/reference/)

[All Docs...](https://docs.spring.io/spring-security/reference/spring-projects.html)

![Image 7: Spring](https://docs.spring.io/spring-security/reference/_/img/spring-logo.svg)
Copyright © 2005 - 2026 Broadcom. All Rights Reserved. The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

[Terms of Use](https://www.vmware.com/help/legal.html) • [Privacy](https://www.vmware.com/help/privacy.html) • [Trademark Guidelines](https://spring.io/trademarks)• [Thank you](https://spring.io/thank-you) • [Your California Privacy Rights](https://www.vmware.com/help/privacy/california-privacy-rights.html) • [Cookies Settings](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html)

Apache®, Apache Tomcat®, Apache Kafka®, Apache Cassandra™, and Apache Geode™ are trademarks or registered trademarks of the Apache Software Foundation in the United States and/or other countries. Java™, Java™ SE, Java™ EE, and OpenJDK™ are trademarks of Oracle and/or its affiliates. Kubernetes® is a registered trademark of the Linux Foundation in the United States and other countries. Linux® is the registered trademark of Linus Torvalds in the United States and other countries. Windows® and Microsoft® Azure are registered trademarks of Microsoft Corporation. “AWS” and “Amazon Web Services” are trademarks or registered trademarks of Amazon.com Inc. or its affiliates. All other trademarks and copyrights are property of their respective owners and are only mentioned for informative purposes. Other names may be trademarks of their respective owners.

[](https://www.youtube.com/user/SpringSourceDev "Youtube")[](https://github.com/spring-projects "GitHub")[](https://twitter.com/springcentral "Twitter")

[Search in all Spring Docs](https://docs.spring.io/spring-security/reference/search.html)

[![Image 8](https://docs.spring.io/spring-security/reference/_/img/algolia-light.svg)![Image 9](https://docs.spring.io/spring-security/reference/_/img/algolia-dark.svg)](https://www.algolia.com/)

Cookies
-------

Broadcom and third-party partners use technology, including cookies to, among other things, analyze site usage, improve your experience and help us advertise. By using our site, you agree to our use of cookies as described in our [Cookie Notice](https://www.broadcom.com/company/legal/cookie-policy)

Allow All

Required Only

Cookies Settings

![Image 10: Company Logo](https://cdn.cookielaw.org/logos/8153b982-ae11-46a0-b7c2-6e4e3b591d72/8a37f712-8eb0-4967-9ca7-343409702cfa/5228da75-715f-4d1a-9262-2662775eb1ce/Broadcom_Logo_Red-Black_no-tag.png)

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

[![Image 11: Powered by Onetrust](https://cdn.cookielaw.org/logos/static/powered_by_logo.svg)](https://www.onetrust.com/products/cookie-consent/)
