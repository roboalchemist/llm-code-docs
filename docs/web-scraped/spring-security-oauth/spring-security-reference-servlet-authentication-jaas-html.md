# Source: https://docs.spring.io/spring-security/reference/servlet/authentication/jaas.html

Title: Java Authentication and Authorization Service (JAAS) Provider :: Spring Security

URL Source: https://docs.spring.io/spring-security/reference/servlet/authentication/jaas.html

Markdown Content:
Java Authentication and Authorization Service (JAAS) Provider :: Spring Security
===============

[![Image 1: Spring](https://docs.spring.io/spring-security/reference/_/img/spring-logo.svg)](https://spring.io/)

[Why Spring](https://docs.spring.io/spring-security/reference/servlet/authentication/jaas.html#)

[Overview](https://spring.io/why-spring)[Microservices](https://spring.io/microservices)[Reactive](https://spring.io/reactive)[Event Driven](https://spring.io/event-driven)[Cloud](https://spring.io/cloud)[Web Applications](https://spring.io/web-applications)[Serverless](https://spring.io/serverless)[Batch](https://spring.io/batch)

[Learn](https://docs.spring.io/spring-security/reference/servlet/authentication/jaas.html#)

[Overview](https://spring.io/learn)[Quickstart](https://spring.io/quickstart)[Guides](https://spring.io/guides)[Blog](https://spring.io/blog)

[Projects](https://docs.spring.io/spring-security/reference/servlet/authentication/jaas.html#)

[Overview](https://spring.io/projects)[Spring Boot](https://spring.io/projects/spring-boot)[Spring Framework](https://spring.io/projects/spring-framework)[Spring Cloud](https://spring.io/projects/spring-cloud)[Spring Cloud Data Flow](https://spring.io/projects/spring-cloud-dataflow)[Spring Data](https://spring.io/projects/spring-data)[Spring Integration](https://spring.io/projects/spring-integration)[Spring Batch](https://spring.io/projects/spring-batch)[Spring Security](https://spring.io/projects/spring-security)[View all projects](https://spring.io/projects)*   DEVELOPMENT TOOLS
[Spring Tools 4](https://spring.io/tools)[Spring Initializr](https://start.spring.io/)

[Academy](https://docs.spring.io/spring-security/reference/servlet/authentication/jaas.html#)

[Courses](https://spring.academy/courses)[Get Certified](https://spring.academy/learning-path)

[Solutions](https://docs.spring.io/spring-security/reference/servlet/authentication/jaas.html#)

[Overview](https://spring.io/solutions)[Spring Runtime](https://spring.io/support)[Spring Consulting](https://spring.io/consulting)[Spring Academy For Teams](https://spring.academy/teams)[Security Advisories](https://spring.io/security)

[Community](https://docs.spring.io/spring-security/reference/servlet/authentication/jaas.html#)

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

### Java Authentication and Authorization Service (JAAS) Provider

*   [AbstractJaasAuthenticationProvider](https://docs.spring.io/spring-security/reference/servlet/authentication/jaas.html#jaas-abstractjaasauthenticationprovider)
*   [JAAS CallbackHandler](https://docs.spring.io/spring-security/reference/servlet/authentication/jaas.html#jaas-callbackhandler)
*   [JAAS AuthorityGranter](https://docs.spring.io/spring-security/reference/servlet/authentication/jaas.html#jaas-authoritygranter)
*   [DefaultJaasAuthenticationProvider](https://docs.spring.io/spring-security/reference/servlet/authentication/jaas.html#jaas-defaultjaasauthenticationprovider)
*   [InMemoryConfiguration](https://docs.spring.io/spring-security/reference/servlet/authentication/jaas.html#jaas-inmemoryconfiguration)
*   [DefaultJaasAuthenticationProvider Example Configuration](https://docs.spring.io/spring-security/reference/servlet/authentication/jaas.html#jaas-djap-config)
*   [JaasAuthenticationProvider](https://docs.spring.io/spring-security/reference/servlet/authentication/jaas.html#jaas-jaasauthenticationprovider)
*   [Running as a Subject](https://docs.spring.io/spring-security/reference/servlet/authentication/jaas.html#jaas-apiprovision)

[Edit this Page](https://github.com/spring-projects/spring-security/blob/7.0.3/docs/modules/ROOT/pages/servlet/authentication/jaas.adoc)[GitHub Project](https://github.com/spring-projects/spring-security "GitHub")[Stack Overflow](https://stackoverflow.com/tags/spring-security)

*   [Spring Security](https://docs.spring.io/spring-security/reference/index.html)
*   [Servlet Applications](https://docs.spring.io/spring-security/reference/servlet/index.html)
*   [Authentication](https://docs.spring.io/spring-security/reference/servlet/authentication/index.html)
*   [JAAS](https://docs.spring.io/spring-security/reference/servlet/authentication/jaas.html)

Java Authentication and Authorization Service (JAAS) Provider
=============================================================

### Java Authentication and Authorization Service (JAAS) Provider

*   [AbstractJaasAuthenticationProvider](https://docs.spring.io/spring-security/reference/servlet/authentication/jaas.html#jaas-abstractjaasauthenticationprovider)
*   [JAAS CallbackHandler](https://docs.spring.io/spring-security/reference/servlet/authentication/jaas.html#jaas-callbackhandler)
*   [JAAS AuthorityGranter](https://docs.spring.io/spring-security/reference/servlet/authentication/jaas.html#jaas-authoritygranter)
*   [DefaultJaasAuthenticationProvider](https://docs.spring.io/spring-security/reference/servlet/authentication/jaas.html#jaas-defaultjaasauthenticationprovider)
*   [InMemoryConfiguration](https://docs.spring.io/spring-security/reference/servlet/authentication/jaas.html#jaas-inmemoryconfiguration)
*   [DefaultJaasAuthenticationProvider Example Configuration](https://docs.spring.io/spring-security/reference/servlet/authentication/jaas.html#jaas-djap-config)
*   [JaasAuthenticationProvider](https://docs.spring.io/spring-security/reference/servlet/authentication/jaas.html#jaas-jaasauthenticationprovider)
*   [Running as a Subject](https://docs.spring.io/spring-security/reference/servlet/authentication/jaas.html#jaas-apiprovision)

Spring Security provides a package to delegate authentication requests to the Java Authentication and Authorization Service (JAAS). This section discusses that package.

[](https://docs.spring.io/spring-security/reference/servlet/authentication/jaas.html#jaas-abstractjaasauthenticationprovider)AbstractJaasAuthenticationProvider
---------------------------------------------------------------------------------------------------------------------------------------------------------------

The `AbstractJaasAuthenticationProvider` class is the basis for the provided JAAS `AuthenticationProvider` implementations. Subclasses must implement a method that creates the `LoginContext`. The `AbstractJaasAuthenticationProvider` has a number of dependencies that can be injected into it, as discussed in the remainder of this section.

### [](https://docs.spring.io/spring-security/reference/servlet/authentication/jaas.html#jaas-callbackhandler)JAAS CallbackHandler

Most JAAS `LoginModule` instances require a callback of some sort. These callbacks are usually used to obtain the username and password from the user.

In a Spring Security deployment, Spring Security is responsible for this user interaction (through the authentication mechanism). Thus, by the time the authentication request is delegated through to JAAS, Spring Security’s authentication mechanism has already fully populated an `Authentication` object that contains all the information required by the JAAS `LoginModule`.

Therefore, the JAAS package for Spring Security provides two default callback handlers: `JaasNameCallbackHandler` and `JaasPasswordCallbackHandler`. Each of these callback handlers implements `JaasAuthenticationCallbackHandler`. In most cases, these callback handlers can be used without understanding the internal mechanics.

For those needing full control over the callback behavior, `AbstractJaasAuthenticationProvider` internally wraps these `JaasAuthenticationCallbackHandler` instances with an `InternalCallbackHandler`. The `InternalCallbackHandler` is the class that actually implements the JAAS normal `CallbackHandler` interface. Any time that the JAAS `LoginModule` is used, it is passed a list of application contexts configured `InternalCallbackHandler` instances. If the `LoginModule` requests a callback against the `InternalCallbackHandler` instances, the callback is, in turn, passed to the `JaasAuthenticationCallbackHandler` instances being wrapped.

### [](https://docs.spring.io/spring-security/reference/servlet/authentication/jaas.html#jaas-authoritygranter)JAAS AuthorityGranter

JAAS works with principals. Even “roles” are represented as principals in JAAS. Spring Security, on the other hand, works with `Authentication` objects. Each `Authentication` object contains a single principal and multiple `GrantedAuthority` instances. To facilitate mapping between these different concepts, Spring Security’s JAAS package includes an `AuthorityGranter` interface.

An `AuthorityGranter` is responsible for inspecting a JAAS principal and returning a set of `String` objects that represent the authorities assigned to the principal. For each returned authority string, the `AbstractJaasAuthenticationProvider` creates a `JaasGrantedAuthority` (which implements Spring Security’s `GrantedAuthority` interface) that contains the authority string and the JAAS principal that the `AuthorityGranter` was passed. The `AbstractJaasAuthenticationProvider` obtains the JAAS principals by first successfully authenticating the user’s credentials by using the JAAS `LoginModule` and then accessing the `LoginContext` it returns. A call to `LoginContext.getSubject().getPrincipals()` is made, with each resulting principal passed to each `AuthorityGranter` defined against the `AbstractJaasAuthenticationProvider.setAuthorityGranters(List)` property.

Spring Security does not include any production `AuthorityGranter` instances, given that every JAAS principal has an implementation-specific meaning. However, Spring Security does issue the `FACTOR_PASSWORD` authority by default when authentication suceeds.

There is a `TestAuthorityGranter` in the unit tests that demonstrates a simple `AuthorityGranter` implementation.

[](https://docs.spring.io/spring-security/reference/servlet/authentication/jaas.html#jaas-defaultjaasauthenticationprovider)DefaultJaasAuthenticationProvider
-------------------------------------------------------------------------------------------------------------------------------------------------------------

The `DefaultJaasAuthenticationProvider` lets a JAAS `Configuration` object be injected into it as a dependency. It then creates a `LoginContext` by using the injected JAAS `Configuration`. This means that `DefaultJaasAuthenticationProvider` is not bound to any particular implementation of `Configuration`, as `JaasAuthenticationProvider` is.

### [](https://docs.spring.io/spring-security/reference/servlet/authentication/jaas.html#jaas-inmemoryconfiguration)InMemoryConfiguration

To make it easy to inject a `Configuration` into `DefaultJaasAuthenticationProvider`, a default in-memory implementation named `InMemoryConfiguration` is provided. The implementation constructor accepts a `Map` where each key represents a login configuration name, and the value represents an `Array` of `AppConfigurationEntry` instances. `InMemoryConfiguration` also supports a default `Array` of `AppConfigurationEntry` objects that is used if no mapping is found within the provided `Map`. For details, see the Javadoc of [`InMemoryConfiguration`](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/authentication/jaas/memory/InMemoryConfiguration.html).

### [](https://docs.spring.io/spring-security/reference/servlet/authentication/jaas.html#jaas-djap-config)DefaultJaasAuthenticationProvider Example Configuration

While the Spring configuration for `InMemoryConfiguration` can be more verbose than the standard JAAS configuration files, using it in conjunction with `DefaultJaasAuthenticationProvider` is more flexible than `JaasAuthenticationProvider`, since it not dependent on the default `Configuration` implementation.

The next example provides a configuration of `DefaultJaasAuthenticationProvider` that uses `InMemoryConfiguration`. Note that custom implementations of `Configuration` can easily be injected into `DefaultJaasAuthenticationProvider` as well.

```xml
<bean id="jaasAuthProvider"
class="org.springframework.security.authentication.jaas.DefaultJaasAuthenticationProvider">
<property name="configuration">
<bean class="org.springframework.security.authentication.jaas.memory.InMemoryConfiguration">
<constructor-arg>
	<map>
	<!--
	SPRINGSECURITY is the default loginContextName
	for AbstractJaasAuthenticationProvider
	-->
	<entry key="SPRINGSECURITY">
	<array>
	<bean class="javax.security.auth.login.AppConfigurationEntry">
		<constructor-arg value="sample.SampleLoginModule" />
		<constructor-arg>
		<util:constant static-field=
			"javax.security.auth.login.AppConfigurationEntry$LoginModuleControlFlag.REQUIRED"/>
		</constructor-arg>
		<constructor-arg>
		<map></map>
		</constructor-arg>
		</bean>
	</array>
	</entry>
	</map>
	</constructor-arg>
</bean>
</property>
<property name="authorityGranters">
<list>
	<!-- You will need to write your own implementation of AuthorityGranter -->
	<bean class="org.springframework.security.authentication.jaas.TestAuthorityGranter"/>
</list>
</property>
</bean>
```

Copied!

[](https://docs.spring.io/spring-security/reference/servlet/authentication/jaas.html#jaas-jaasauthenticationprovider)JaasAuthenticationProvider
-----------------------------------------------------------------------------------------------------------------------------------------------

The `JaasAuthenticationProvider` assumes that the default `Configuration` is an instance of [`ConfigFile`](https://docs.oracle.com/javase/8/docs/jre/api/security/jaas/spec/com/sun/security/auth/login/ConfigFile.html). This assumption is made in order to try to update the `Configuration`. The `JaasAuthenticationProvider` then uses the default `Configuration` to create the `LoginContext`.

Assume that we have a JAAS login configuration file, `/WEB-INF/login.conf`, with the following contents:

```txt
JAASTest {
	sample.SampleLoginModule required;
};
```

Copied!

Like all Spring Security beans, the `JaasAuthenticationProvider` is configured through the application context. The following definitions would correspond to the above JAAS login configuration file:

```xml
<bean id="jaasAuthenticationProvider"
class="org.springframework.security.authentication.jaas.JaasAuthenticationProvider">
<property name="loginConfig" value="/WEB-INF/login.conf"/>
<property name="loginContextName" value="JAASTest"/>
<property name="callbackHandlers">
<list>
<bean
	class="org.springframework.security.authentication.jaas.JaasNameCallbackHandler"/>
<bean
	class="org.springframework.security.authentication.jaas.JaasPasswordCallbackHandler"/>
</list>
</property>
<property name="authorityGranters">
	<list>
	<bean class="org.springframework.security.authentication.jaas.TestAuthorityGranter"/>
	</list>
</property>
</bean>
```

Copied!

[](https://docs.spring.io/spring-security/reference/servlet/authentication/jaas.html#jaas-apiprovision)Running as a Subject
---------------------------------------------------------------------------------------------------------------------------

If configured, the `JaasApiIntegrationFilter` tries to run as the `Subject` on the `JaasAuthenticationToken`. This means that the `Subject` can be accessed using:

```java
Subject subject = Subject.getSubject(AccessController.getContext());
```

Copied!

You can configure this integration by using the [jaas-api-provision](https://docs.spring.io/spring-security/reference/servlet/appendix/namespace/http.html#nsa-http-jaas-api-provision) attribute. This feature is useful when integrating with legacy or external API’s that rely on the JAAS Subject being populated.

*   [Spring Security](https://docs.spring.io/spring-security/reference/index.html) 

 Stable  
    *   [7.0.3](https://docs.spring.io/spring-security/reference/servlet/authentication/jaas.html)
    *   [6.5.8](https://docs.spring.io/spring-security/reference/6.5/servlet/authentication/jaas.html)

 Preview 

    *   [7.1.0-M2](https://docs.spring.io/spring-security/reference/7.1/servlet/authentication/jaas.html)

 Snapshot 

    *   [7.1.0-SNAPSHOT](https://docs.spring.io/spring-security/reference/7.1-SNAPSHOT/servlet/authentication/jaas.html)
    *   [7.0.4-SNAPSHOT](https://docs.spring.io/spring-security/reference/7.0-SNAPSHOT/servlet/authentication/jaas.html)
    *   [6.5.9-SNAPSHOT](https://docs.spring.io/spring-security/reference/6.5-SNAPSHOT/servlet/authentication/jaas.html)

*    Related Spring Documentation 
    *   [Spring Framework](https://docs.spring.io/spring-framework/reference/)
    *   [](https://docs.spring.io/spring-security/reference/servlet/authentication/jaas.html)[Spring Security](https://docs.spring.io/spring-security/reference/)
        *   [Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/)
        *   [Spring LDAP](https://docs.spring.io/spring-ldap/reference/)
        *   [Spring Security Kerberos](https://docs.spring.io/spring-security-kerberos/reference/)
        *   [Spring Session](https://docs.spring.io/spring-session/reference/)
        *   [Spring Vault](https://docs.spring.io/spring-vault/reference/)

    *   [Spring GraphQL](https://docs.spring.io/spring-graphql/reference/)

[All Docs...](https://docs.spring.io/spring-security/reference/spring-projects.html)

![Image 2: Spring](https://docs.spring.io/spring-security/reference/_/img/spring-logo.svg)
Copyright © 2005 - 2026 Broadcom. All Rights Reserved. The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

[Terms of Use](https://www.vmware.com/help/legal.html) • [Privacy](https://www.vmware.com/help/privacy.html) • [Trademark Guidelines](https://spring.io/trademarks)• [Thank you](https://spring.io/thank-you) • [Your California Privacy Rights](https://www.vmware.com/help/privacy/california-privacy-rights.html) • [Cookies Settings](https://docs.spring.io/spring-security/reference/servlet/authentication/jaas.html)

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
