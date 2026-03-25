# Source: https://docs.spring.io/spring-security/reference/servlet/oauth2/resource-server/multitenancy.html

Title: OAuth 2.0 Resource Server Multi-tenancy :: Spring Security

URL Source: https://docs.spring.io/spring-security/reference/servlet/oauth2/resource-server/multitenancy.html

Markdown Content:
OAuth 2.0 Resource Server Multi-tenancy :: Spring Security
===============

[![Image 1: Spring](https://docs.spring.io/spring-security/reference/_/img/spring-logo.svg)](https://spring.io/)

[Why Spring](https://docs.spring.io/spring-security/reference/servlet/oauth2/resource-server/multitenancy.html#)

[Overview](https://spring.io/why-spring)[Microservices](https://spring.io/microservices)[Reactive](https://spring.io/reactive)[Event Driven](https://spring.io/event-driven)[Cloud](https://spring.io/cloud)[Web Applications](https://spring.io/web-applications)[Serverless](https://spring.io/serverless)[Batch](https://spring.io/batch)

[Learn](https://docs.spring.io/spring-security/reference/servlet/oauth2/resource-server/multitenancy.html#)

[Overview](https://spring.io/learn)[Quickstart](https://spring.io/quickstart)[Guides](https://spring.io/guides)[Blog](https://spring.io/blog)

[Projects](https://docs.spring.io/spring-security/reference/servlet/oauth2/resource-server/multitenancy.html#)

[Overview](https://spring.io/projects)[Spring Boot](https://spring.io/projects/spring-boot)[Spring Framework](https://spring.io/projects/spring-framework)[Spring Cloud](https://spring.io/projects/spring-cloud)[Spring Cloud Data Flow](https://spring.io/projects/spring-cloud-dataflow)[Spring Data](https://spring.io/projects/spring-data)[Spring Integration](https://spring.io/projects/spring-integration)[Spring Batch](https://spring.io/projects/spring-batch)[Spring Security](https://spring.io/projects/spring-security)[View all projects](https://spring.io/projects)*   DEVELOPMENT TOOLS
[Spring Tools 4](https://spring.io/tools)[Spring Initializr](https://start.spring.io/)

[Academy](https://docs.spring.io/spring-security/reference/servlet/oauth2/resource-server/multitenancy.html#)

[Courses](https://spring.academy/courses)[Get Certified](https://spring.academy/learning-path)

[Solutions](https://docs.spring.io/spring-security/reference/servlet/oauth2/resource-server/multitenancy.html#)

[Overview](https://spring.io/solutions)[Spring Runtime](https://spring.io/support)[Spring Consulting](https://spring.io/consulting)[Spring Academy For Teams](https://spring.academy/teams)[Security Advisories](https://spring.io/security)

[Community](https://docs.spring.io/spring-security/reference/servlet/oauth2/resource-server/multitenancy.html#)

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

### OAuth 2.0 Resource Server Multi-tenancy

*   [Supporting both JWT and Opaque Token](https://docs.spring.io/spring-security/reference/servlet/oauth2/resource-server/multitenancy.html#oauth2reourceserver-opaqueandjwt)
*   [Multi-tenancy](https://docs.spring.io/spring-security/reference/servlet/oauth2/resource-server/multitenancy.html#oauth2resourceserver-multitenancy)
*   [Resolving the Tenant By Claim](https://docs.spring.io/spring-security/reference/servlet/oauth2/resource-server/multitenancy.html#_resolving_the_tenant_by_claim)

[Edit this Page](https://github.com/spring-projects/spring-security/blob/7.0.3/docs/modules/ROOT/pages/servlet/oauth2/resource-server/multitenancy.adoc)[GitHub Project](https://github.com/spring-projects/spring-security "GitHub")[Stack Overflow](https://stackoverflow.com/tags/spring-security)

*   [Spring Security](https://docs.spring.io/spring-security/reference/index.html)
*   [Servlet Applications](https://docs.spring.io/spring-security/reference/servlet/index.html)
*   [OAuth2](https://docs.spring.io/spring-security/reference/servlet/oauth2/index.html)
*   [OAuth2 Resource Server](https://docs.spring.io/spring-security/reference/servlet/oauth2/resource-server/index.html)
*   [Multitenancy](https://docs.spring.io/spring-security/reference/servlet/oauth2/resource-server/multitenancy.html)

OAuth 2.0 Resource Server Multi-tenancy
=======================================

### OAuth 2.0 Resource Server Multi-tenancy

*   [Supporting both JWT and Opaque Token](https://docs.spring.io/spring-security/reference/servlet/oauth2/resource-server/multitenancy.html#oauth2reourceserver-opaqueandjwt)
*   [Multi-tenancy](https://docs.spring.io/spring-security/reference/servlet/oauth2/resource-server/multitenancy.html#oauth2resourceserver-multitenancy)
*   [Resolving the Tenant By Claim](https://docs.spring.io/spring-security/reference/servlet/oauth2/resource-server/multitenancy.html#_resolving_the_tenant_by_claim)

[](https://docs.spring.io/spring-security/reference/servlet/oauth2/resource-server/multitenancy.html#oauth2reourceserver-opaqueandjwt)Supporting both JWT and Opaque Token
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In some cases, you may have a need to access both kinds of tokens. For example, you may support more than one tenant where one tenant issues JWTs and the other issues opaque tokens.

If this decision must be made at request-time, then you can use an `AuthenticationManagerResolver` to achieve it, like so:

*   Java

*   Kotlin

```java
@Bean
AuthenticationManagerResolver<HttpServletRequest> tokenAuthenticationManagerResolver
        (JwtDecoder jwtDecoder, OpaqueTokenIntrospector opaqueTokenIntrospector) {
    AuthenticationManager jwt = new ProviderManager(new JwtAuthenticationProvider(jwtDecoder));
    AuthenticationManager opaqueToken = new ProviderManager(
            new OpaqueTokenAuthenticationProvider(opaqueTokenIntrospector));
    return (request) -> useJwt(request) ? jwt : opaqueToken;
}
```

Copied!

```kotlin
@Bean
fun tokenAuthenticationManagerResolver
        (jwtDecoder: JwtDecoder, opaqueTokenIntrospector: OpaqueTokenIntrospector):
        AuthenticationManagerResolver<HttpServletRequest> {
    val jwt = ProviderManager(JwtAuthenticationProvider(jwtDecoder))
    val opaqueToken = ProviderManager(OpaqueTokenAuthenticationProvider(opaqueTokenIntrospector));

    return AuthenticationManagerResolver { request ->
        if (useJwt(request)) {
            jwt
        } else {
            opaqueToken
        }
    }
}
```

Copied!

The implementation of `useJwt(HttpServletRequest)` will likely depend on custom request material like the path.

And then specify this `AuthenticationManagerResolver` in the DSL:

Authentication Manager Resolver

*   Java

*   Kotlin

*   Xml

```java
http
    .authorizeHttpRequests((authorize) -> authorize
        .anyRequest().authenticated()
    )
    .oauth2ResourceServer((oauth2) -> oauth2
        .authenticationManagerResolver(this.tokenAuthenticationManagerResolver)
    );
```

Copied!

```kotlin
http {
    authorizeHttpRequests {
        authorize(anyRequest, authenticated)
    }
    oauth2ResourceServer {
        authenticationManagerResolver = tokenAuthenticationManagerResolver()
    }
}
```

Copied!

```xml
<http>
    <oauth2-resource-server authentication-manager-resolver-ref="tokenAuthenticationManagerResolver"/>
</http>
```

Copied!

[](https://docs.spring.io/spring-security/reference/servlet/oauth2/resource-server/multitenancy.html#oauth2resourceserver-multitenancy)Multi-tenancy
----------------------------------------------------------------------------------------------------------------------------------------------------

A resource server is considered multi-tenant when there are multiple strategies for verifying a bearer token, keyed by some tenant identifier.

For example, your resource server may accept bearer tokens from two different authorization servers. Or, your authorization server may represent a multiplicity of issuers.

In each case, there are two things that need to be done and trade-offs associated with how you choose to do them:

1.   Resolve the tenant

2.   Propagate the tenant

### [](https://docs.spring.io/spring-security/reference/servlet/oauth2/resource-server/multitenancy.html#_resolving_the_tenant_by_claim)Resolving the Tenant By Claim

One way to differentiate tenants is by the issuer claim. Since the issuer claim accompanies signed JWTs, this can be done with the `JwtIssuerAuthenticationManagerResolver`, like so:

Multi-tenancy Tenant by JWT Claim

*   Java

*   Kotlin

*   Xml

```java
JwtIssuerAuthenticationManagerResolver authenticationManagerResolver = JwtIssuerAuthenticationManagerResolver
    .fromTrustedIssuers("https://idp.example.org/issuerOne", "https://idp.example.org/issuerTwo");

http
    .authorizeHttpRequests((authorize) -> authorize
        .anyRequest().authenticated()
    )
    .oauth2ResourceServer((oauth2) -> oauth2
        .authenticationManagerResolver(authenticationManagerResolver)
    );
```

Copied!

```kotlin
val customAuthenticationManagerResolver = JwtIssuerAuthenticationManagerResolver
    .fromTrustedIssuers("https://idp.example.org/issuerOne", "https://idp.example.org/issuerTwo")
http {
    authorizeHttpRequests {
        authorize(anyRequest, authenticated)
    }
    oauth2ResourceServer {
        authenticationManagerResolver = customAuthenticationManagerResolver
    }
}
```

Copied!

```xml
<http>
    <oauth2-resource-server authentication-manager-resolver-ref="authenticationManagerResolver"/>
</http>

<bean id="authenticationManagerResolver"
        class="org.springframework.security.oauth2.server.resource.authentication.JwtIssuerAuthenticationManagerResolver">
    <constructor-arg>
        <list>
            <value>https://idp.example.org/issuerOne</value>
            <value>https://idp.example.org/issuerTwo</value>
        </list>
    </constructor-arg>
</bean>
```

Copied!

This is nice because the issuer endpoints are loaded lazily. In fact, the corresponding `JwtAuthenticationProvider` is instantiated only when the first request with the corresponding issuer is sent. This allows for an application startup that is independent from those authorization servers being up and available.

#### [](https://docs.spring.io/spring-security/reference/servlet/oauth2/resource-server/multitenancy.html#_dynamic_tenants)Dynamic Tenants

Of course, you may not want to restart the application each time a new tenant is added. In this case, you can configure the `JwtIssuerAuthenticationManagerResolver` with a repository of `AuthenticationManager` instances, which you can edit at runtime, like so:

*   Java

*   Kotlin

```java
private void addManager(Map<String, AuthenticationManager> authenticationManagers, String issuer) {
	JwtAuthenticationProvider authenticationProvider = new JwtAuthenticationProvider
	        (JwtDecoders.fromIssuerLocation(issuer));
	authenticationManagers.put(issuer, authenticationProvider::authenticate);
}

// ...

JwtIssuerAuthenticationManagerResolver authenticationManagerResolver =
        new JwtIssuerAuthenticationManagerResolver(authenticationManagers::get);

http
    .authorizeHttpRequests((authorize) -> authorize
        .anyRequest().authenticated()
    )
    .oauth2ResourceServer((oauth2) -> oauth2
        .authenticationManagerResolver(authenticationManagerResolver)
    );
```

Copied!

```kotlin
private fun addManager(authenticationManagers: MutableMap<String, AuthenticationManager>, issuer: String) {
    val authenticationProvider = JwtAuthenticationProvider(JwtDecoders.fromIssuerLocation(issuer))
    authenticationManagers[issuer] = AuthenticationManager {
        authentication: Authentication? -> authenticationProvider.authenticate(authentication)
    }
}

// ...

val customAuthenticationManagerResolver: JwtIssuerAuthenticationManagerResolver =
    JwtIssuerAuthenticationManagerResolver(authenticationManagers::get)
http {
    authorizeHttpRequests {
        authorize(anyRequest, authenticated)
    }
    oauth2ResourceServer {
        authenticationManagerResolver = customAuthenticationManagerResolver
    }
}
```

Copied!

In this case, you construct `JwtIssuerAuthenticationManagerResolver` with a strategy for obtaining the `AuthenticationManager` given the issuer. This approach allows us to add and remove elements from the repository (shown as a `Map` in the snippet) at runtime.

It would be unsafe to simply take any issuer and construct an `AuthenticationManager` from it. The issuer should be one that the code can verify from a trusted source like a list of allowed issuers.

#### [](https://docs.spring.io/spring-security/reference/servlet/oauth2/resource-server/multitenancy.html#_parsing_the_claim_only_once)Parsing the Claim Only Once

You may have observed that this strategy, while simple, comes with the trade-off that the JWT is parsed once by the `AuthenticationManagerResolver` and then again by the [`JwtDecoder`](https://docs.spring.io/spring-security/reference/servlet/oauth2/resource-server/jwt.html#oauth2resourceserver-jwt-architecture-jwtdecoder) later on in the request.

This extra parsing can be alleviated by configuring the [`JwtDecoder`](https://docs.spring.io/spring-security/reference/servlet/oauth2/resource-server/jwt.html#oauth2resourceserver-jwt-architecture-jwtdecoder) directly with a `JWTClaimsSetAwareJWSKeySelector` from Nimbus:

*   Java

*   Kotlin

```java
@Component
public class TenantJWSKeySelector
    implements JWTClaimsSetAwareJWSKeySelector<SecurityContext> {

	private final TenantRepository tenants; (1)
	private final Map<String, JWSKeySelector<SecurityContext>> selectors = new ConcurrentHashMap<>(); (2)

	public TenantJWSKeySelector(TenantRepository tenants) {
		this.tenants = tenants;
	}

	@Override
	public List<? extends Key> selectKeys(JWSHeader jwsHeader, JWTClaimsSet jwtClaimsSet, SecurityContext securityContext)
			throws KeySourceException {
		return this.selectors.computeIfAbsent(toTenant(jwtClaimsSet), this::fromTenant)
				.selectJWSKeys(jwsHeader, securityContext);
	}

	private String toTenant(JWTClaimsSet claimSet) {
		return (String) claimSet.getClaim("iss");
	}

	private JWSKeySelector<SecurityContext> fromTenant(String tenant) {
		return Optional.ofNullable(this.tenants.findById(tenant)) (3)
		        .map((t) -> t.getAttrbute("jwks_uri"))
				.map(this::fromUri)
				.orElseThrow(() -> new IllegalArgumentException("unknown tenant"));
	}

	private JWSKeySelector<SecurityContext> fromUri(String uri) {
		try {
			return JWSAlgorithmFamilyJWSKeySelector.fromJWKSetURL(new URL(uri)); (4)
		} catch (Exception ex) {
			throw new IllegalArgumentException(ex);
		}
	}
}
```

Copied!

```kotlin
@Component
class TenantJWSKeySelector(tenants: TenantRepository) : JWTClaimsSetAwareJWSKeySelector<SecurityContext> {
    private val tenants: TenantRepository (1)
    private val selectors: MutableMap<String, JWSKeySelector<SecurityContext>> = ConcurrentHashMap() (2)

    init {
        this.tenants = tenants
    }

    fun selectKeys(jwsHeader: JWSHeader?, jwtClaimsSet: JWTClaimsSet, securityContext: SecurityContext): List<Key?> {
        return selectors.computeIfAbsent(toTenant(jwtClaimsSet)) { tenant: String -> fromTenant(tenant) }
                .selectJWSKeys(jwsHeader, securityContext)
    }

    private fun toTenant(claimSet: JWTClaimsSet): String {
        return claimSet.getClaim("iss") as String
    }

    private fun fromTenant(tenant: String): JWSKeySelector<SecurityContext> {
        return Optional.ofNullable(this.tenants.findById(tenant)) (3)
                .map { t -> t.getAttrbute("jwks_uri") }
                .map { uri: String -> fromUri(uri) }
                .orElseThrow { IllegalArgumentException("unknown tenant") }
    }

    private fun fromUri(uri: String): JWSKeySelector<SecurityContext?> {
        return try {
            JWSAlgorithmFamilyJWSKeySelector.fromJWKSetURL(URL(uri)) (4)
        } catch (ex: Exception) {
            throw IllegalArgumentException(ex)
        }
    }
}
```

Copied!

**1**A hypothetical source for tenant information
**2**A cache for `JWSKeySelector`s, keyed by tenant identifier
**3**Looking up the tenant is more secure than simply calculating the JWK Set endpoint on the fly - the lookup acts as a list of allowed tenants
**4**Create a `JWSKeySelector` via the types of keys that come back from the JWK Set endpoint - the lazy lookup here means that you don’t need to configure all tenants at startup

The above key selector is a composition of many key selectors. It chooses which key selector to use based on the `iss` claim in the JWT.

To use this approach, make sure that the authorization server is configured to include the claim set as part of the token’s signature. Without this, you have no guarantee that the issuer hasn’t been altered by a bad actor.

Next, we can construct a `JWTProcessor`:

*   Java

*   Kotlin

```java
@Bean
JWTProcessor jwtProcessor(JWTClaimsSetAwareJWSKeySelector keySelector) {
	ConfigurableJWTProcessor<SecurityContext> jwtProcessor =
            new DefaultJWTProcessor();
	jwtProcessor.setJWTClaimSetJWSKeySelector(keySelector);
	return jwtProcessor;
}
```

Copied!

```kotlin
@Bean
fun jwtProcessor(keySelector: JWTClaimsSetAwareJWSKeySelector<SecurityContext>): JWTProcessor<SecurityContext> {
    val jwtProcessor = DefaultJWTProcessor<SecurityContext>()
    jwtProcessor.jwtClaimsSetAwareJWSKeySelector = keySelector
    return jwtProcessor
}
```

Copied!

As you are already seeing, the trade-off for moving tenant-awareness down to this level is more configuration. We have just a bit more.

Next, we still want to make sure you are validating the issuer. But, since the issuer may be different per JWT, then you’ll need a tenant-aware validator, too:

*   Java

*   Kotlin

```java
@Component
public class TenantJwtIssuerValidator implements OAuth2TokenValidator<Jwt> {
    private final TenantRepository tenants;

    private final OAuth2Error error = new OAuth2Error(OAuth2ErrorCodes.INVALID_TOKEN, "The iss claim is not valid",
            "https://tools.ietf.org/html/rfc6750#section-3.1");

    public TenantJwtIssuerValidator(TenantRepository tenants) {
        this.tenants = tenants;
    }

    @Override
    public OAuth2TokenValidatorResult validate(Jwt token) {
        if(this.tenants.findById(token.getIssuer()) != null) {
            return OAuth2TokenValidatorResult.success();
        }
        return OAuth2TokenValidatorResult.failure(this.error);
    }
}
```

Copied!

```kotlin
@Component
class TenantJwtIssuerValidator(private val tenants: TenantRepository) : OAuth2TokenValidator<Jwt> {
    private val error: OAuth2Error = OAuth2Error(OAuth2ErrorCodes.INVALID_TOKEN, "The iss claim is not valid",
            "https://tools.ietf.org/html/rfc6750#section-3.1")

    override fun validate(token: Jwt): OAuth2TokenValidatorResult {
        return if (tenants.findById(token.issuer) != null)
            OAuth2TokenValidatorResult.success() else OAuth2TokenValidatorResult.failure(error)
    }
}
```

Copied!

Now that we have a tenant-aware processor and a tenant-aware validator, we can proceed with creating our [`JwtDecoder`](https://docs.spring.io/spring-security/reference/servlet/oauth2/resource-server/jwt.html#oauth2resourceserver-jwt-architecture-jwtdecoder):

*   Java

*   Kotlin

```java
@Bean
JwtDecoder jwtDecoder(JWTProcessor jwtProcessor, OAuth2TokenValidator<Jwt> jwtValidator) {
	NimbusJwtDecoder decoder = new NimbusJwtDecoder(jwtProcessor);
	OAuth2TokenValidator<Jwt> validator = new DelegatingOAuth2TokenValidator<>
			(JwtValidators.createDefault(), jwtValidator);
	decoder.setJwtValidator(validator);
	return decoder;
}
```

Copied!

```kotlin
@Bean
fun jwtDecoder(jwtProcessor: JWTProcessor<SecurityContext>?, jwtValidator: OAuth2TokenValidator<Jwt>?): JwtDecoder {
    val decoder = NimbusJwtDecoder(jwtProcessor)
    val validator: OAuth2TokenValidator<Jwt> = DelegatingOAuth2TokenValidator(JwtValidators.createDefault(), jwtValidator)
    decoder.setJwtValidator(validator)
    return decoder
}
```

Copied!

We’ve finished talking about resolving the tenant.

If you’ve chosen to resolve the tenant by something other than a JWT claim, then you’ll need to make sure you address your downstream resource servers in the same way. For example, if you are resolving it by subdomain, you may need to address the downstream resource server using the same subdomain.

However, if you resolve it by a claim in the bearer token, read on to learn about [Spring Security’s support for bearer token propagation](https://docs.spring.io/spring-security/reference/servlet/oauth2/resource-server/bearer-tokens.html#oauth2resourceserver-bearertoken-resolver).

*   [Spring Security](https://docs.spring.io/spring-security/reference/index.html) 

 Stable  
    *   [7.0.3](https://docs.spring.io/spring-security/reference/servlet/oauth2/resource-server/multitenancy.html)
    *   [6.5.8](https://docs.spring.io/spring-security/reference/6.5/servlet/oauth2/resource-server/multitenancy.html)

 Preview 

    *   [7.1.0-M2](https://docs.spring.io/spring-security/reference/7.1/servlet/oauth2/resource-server/multitenancy.html)

 Snapshot 

    *   [7.1.0-SNAPSHOT](https://docs.spring.io/spring-security/reference/7.1-SNAPSHOT/servlet/oauth2/resource-server/multitenancy.html)
    *   [7.0.4-SNAPSHOT](https://docs.spring.io/spring-security/reference/7.0-SNAPSHOT/servlet/oauth2/resource-server/multitenancy.html)
    *   [6.5.9-SNAPSHOT](https://docs.spring.io/spring-security/reference/6.5-SNAPSHOT/servlet/oauth2/resource-server/multitenancy.html)

*    Related Spring Documentation 
    *   [Spring Framework](https://docs.spring.io/spring-framework/reference/)
    *   [](https://docs.spring.io/spring-security/reference/servlet/oauth2/resource-server/multitenancy.html)[Spring Security](https://docs.spring.io/spring-security/reference/)
        *   [Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/)
        *   [Spring LDAP](https://docs.spring.io/spring-ldap/reference/)
        *   [Spring Security Kerberos](https://docs.spring.io/spring-security-kerberos/reference/)
        *   [Spring Session](https://docs.spring.io/spring-session/reference/)
        *   [Spring Vault](https://docs.spring.io/spring-vault/reference/)

    *   [Spring GraphQL](https://docs.spring.io/spring-graphql/reference/)

[All Docs...](https://docs.spring.io/spring-security/reference/spring-projects.html)

![Image 2: Spring](https://docs.spring.io/spring-security/reference/_/img/spring-logo.svg)
Copyright © 2005 - 2026 Broadcom. All Rights Reserved. The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

[Terms of Use](https://www.vmware.com/help/legal.html) • [Privacy](https://www.vmware.com/help/privacy.html) • [Trademark Guidelines](https://spring.io/trademarks)• [Thank you](https://spring.io/thank-you) • [Your California Privacy Rights](https://www.vmware.com/help/privacy/california-privacy-rights.html) • [Cookies Settings](https://docs.spring.io/spring-security/reference/servlet/oauth2/resource-server/multitenancy.html)

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
