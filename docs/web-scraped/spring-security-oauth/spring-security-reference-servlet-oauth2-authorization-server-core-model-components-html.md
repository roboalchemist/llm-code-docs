# Source: https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/core-model-components.html

Title: Core Model / Components :: Spring Security

URL Source: https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/core-model-components.html

Markdown Content:
A `RegisteredClient` is a representation of a client that is [registered](https://datatracker.ietf.org/doc/html/rfc6749#section-2) with the authorization server. A client must be registered with the authorization server before it can initiate an authorization grant flow, such as `authorization_code` or `client_credentials`.

During client registration, the client is assigned a unique [client identifier](https://datatracker.ietf.org/doc/html/rfc6749#section-2.2), (optionally) a client secret (depending on [client type](https://datatracker.ietf.org/doc/html/rfc6749#section-2.1)), and metadata associated with its unique client identifier. The client’s metadata can range from human-facing display strings (such as client name) to items specific to a protocol flow (such as the list of valid redirect URIs).

The corresponding client registration model in Spring Security’s OAuth2 Client support is [ClientRegistration](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/core.html#oauth2Client-client-registration).

The primary purpose of a client is to request access to protected resources. The client first requests an access token by authenticating with the authorization server and presenting the authorization grant. The authorization server authenticates the client and authorization grant, and, if they are valid, issues an access token. The client can now request the protected resource from the resource server by presenting the access token.

The following example shows how to configure a `RegisteredClient` that is allowed to perform the [authorization_code grant](https://datatracker.ietf.org/doc/html/rfc6749#section-4.1) flow to request an access token:

```
RegisteredClient registeredClient = RegisteredClient.withId(UUID.randomUUID().toString())
	.clientId("client-a")
	.clientSecret("{noop}secret")   (1)
	.clientAuthenticationMethod(ClientAuthenticationMethod.CLIENT_SECRET_BASIC)
	.authorizationGrantType(AuthorizationGrantType.AUTHORIZATION_CODE)
	.redirectUri("http://127.0.0.1:8080/authorized")
	.scope("scope-a")
	.clientSettings(ClientSettings.builder().requireAuthorizationConsent(true).build())
	.build();
```

```
spring:
  security:
    oauth2:
      client:
        registration:
          client-a:
            provider: spring
            client-id: client-a
            client-secret: secret
            authorization-grant-type: authorization_code
            redirect-uri: "http://127.0.0.1:8080/authorized"
            scope: scope-a
        provider:
          spring:
            issuer-uri: http://localhost:9000
```

A `RegisteredClient` has metadata (attributes) associated with its unique Client Identifier and is defined as follows:

```
public class RegisteredClient implements Serializable {
	private String id;  (1)
	private String clientId;    (2)
	private Instant clientIdIssuedAt;   (3)
	private String clientSecret;    (4)
	private Instant clientSecretExpiresAt;  (5)
	private String clientName;  (6)
	private Set<ClientAuthenticationMethod> clientAuthenticationMethods;    (7)
	private Set<AuthorizationGrantType> authorizationGrantTypes;    (8)
	private Set<String> redirectUris;   (9)
	private Set<String> postLogoutRedirectUris; (10)
	private Set<String> scopes; (11)
	private ClientSettings clientSettings;  (12)
	private TokenSettings tokenSettings;    (13)

	...

}
```

**1**`id`: The ID that uniquely identifies the `RegisteredClient`.
**2**`clientId`: The client identifier.
**3**`clientIdIssuedAt`: The time at which the client identifier was issued.
**4**`clientSecret`: The client’s secret. The value should be encoded using Spring Security’s [PasswordEncoder](https://docs.spring.io/spring-security/reference/features/authentication/password-storage.html#authentication-password-storage-dpe).
**5**`clientSecretExpiresAt`: The time at which the client secret expires.
**6**`clientName`: A descriptive name used for the client. The name may be used in certain scenarios, such as when displaying the client name in the consent page.
**7**`clientAuthenticationMethods`: The authentication method(s) that the client may use. The supported values are `client_secret_basic`, `client_secret_post`, [`private_key_jwt`](https://datatracker.ietf.org/doc/html/rfc7523), `client_secret_jwt`, and `none`[(public clients)](https://datatracker.ietf.org/doc/html/rfc7636).
**8**`authorizationGrantTypes`: The [authorization grant type(s)](https://datatracker.ietf.org/doc/html/rfc6749#section-1.3) that the client can use. The supported values are `authorization_code`, `client_credentials`, `refresh_token`, `urn:ietf:params:oauth:grant-type:device_code`, and `urn:ietf:params:oauth:grant-type:token-exchange`.
**9**`redirectUris`: The registered [redirect URI(s)](https://datatracker.ietf.org/doc/html/rfc6749#section-3.1.2) that the client may use in redirect-based flows – for example, `authorization_code` grant.
**10**`postLogoutRedirectUris`: The post logout redirect URI(s) that the client may use for logout.
**11**`scopes`: The scope(s) that the client is allowed to request.
**12**`clientSettings`: The custom settings for the client – for example, require [PKCE](https://datatracker.ietf.org/doc/html/rfc7636), require authorization consent, and others.
**13**`tokenSettings`: The custom settings for the OAuth2 tokens issued to the client – for example, access/refresh token time-to-live, reuse refresh tokens, and others.

[](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/core-model-components.html#oauth2AuthorizationServer-registered-client-repository)RegisteredClientRepository
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The `RegisteredClientRepository` is the central component where new clients can be registered and existing clients can be queried. It is used by other components when following a specific protocol flow, such as client authentication, authorization grant processing, token introspection, dynamic client registration, and others.

The provided implementations of `RegisteredClientRepository` are `InMemoryRegisteredClientRepository` and `JdbcRegisteredClientRepository`. The `InMemoryRegisteredClientRepository` implementation stores `RegisteredClient` instances in-memory and is recommended **ONLY** to be used during development and testing. `JdbcRegisteredClientRepository` is a JDBC implementation that persists `RegisteredClient` instances by using `JdbcOperations`.

The `RegisteredClientRepository` is a **REQUIRED** component.

The following example shows how to register a `RegisteredClientRepository``@Bean`:

```
@Bean
public RegisteredClientRepository registeredClientRepository() {
	List<RegisteredClient> registrations = ...
	return new InMemoryRegisteredClientRepository(registrations);
}
```

```
@Bean
public SecurityFilterChain authorizationServerSecurityFilterChain(HttpSecurity http) throws Exception {
	http
		.oauth2AuthorizationServer((authorizationServer) ->
			authorizationServer
				.registeredClientRepository(registeredClientRepository)
		)
	    ...

	return http.build();
}
```

The `OAuth2AuthorizationServerConfigurer` is useful when applying multiple configuration options simultaneously.

[](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/core-model-components.html#oauth2AuthorizationServer-oauth2-authorization)OAuth2Authorization
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

An `OAuth2Authorization` is a representation of an OAuth2 authorization, which holds state related to the authorization granted to a [client](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/core-model-components.html#oauth2AuthorizationServer-registered-client), by the resource owner or itself in the case of the `client_credentials` authorization grant type.

After the successful completion of an authorization grant flow, an `OAuth2Authorization` is created and associates an [`OAuth2AccessToken`](https://docs.spring.io/spring-security/site/docs/7.0.3/api//org/springframework/security/oauth2/core/OAuth2AccessToken.html), an (optional) [`OAuth2RefreshToken`](https://docs.spring.io/spring-security/site/docs/7.0.3/api//org/springframework/security/oauth2/core/OAuth2RefreshToken.html), and additional state specific to the executed authorization grant type.

The [`OAuth2Token`](https://docs.spring.io/spring-security/site/docs/7.0.3/api//org/springframework/security/oauth2/core/OAuth2Token.html) instances associated with an `OAuth2Authorization` vary, depending on the authorization grant type.

For the OAuth2 [authorization_code grant](https://datatracker.ietf.org/doc/html/rfc6749#section-4.1), an `OAuth2AuthorizationCode`, an `OAuth2AccessToken`, and an (optional) `OAuth2RefreshToken` are associated.

For the OpenID Connect 1.0 [authorization_code grant](https://openid.net/specs/openid-connect-core-1_0.html#CodeFlowAuth), an `OAuth2AuthorizationCode`, an [`OidcIdToken`](https://docs.spring.io/spring-security/site/docs/7.0.3/api//org/springframework/security/oauth2/core/oidc/OidcIdToken.html), an `OAuth2AccessToken`, and an (optional) `OAuth2RefreshToken` are associated.

`OAuth2Authorization` and its attributes are defined as follows:

```
public class OAuth2Authorization implements Serializable {
	private String id;  (1)
	private String registeredClientId;  (2)
	private String principalName;   (3)
	private AuthorizationGrantType authorizationGrantType;  (4)
	private Set<String> authorizedScopes;   (5)
	private Map<Class<? extends OAuth2Token>, Token<?>> tokens; (6)
	private Map<String, Object> attributes; (7)

	...

}
```

**1**`id`: The ID that uniquely identifies the `OAuth2Authorization`.
**2**`registeredClientId`: The ID that uniquely identifies the [RegisteredClient](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/core-model-components.html#oauth2AuthorizationServer-registered-client).
**3**`principalName`: The principal name of the resource owner (or client).
**4**`authorizationGrantType`: The `AuthorizationGrantType` used.
**5**`authorizedScopes`: The `Set` of scope(s) authorized for the client.
**6**`tokens`: The `OAuth2Token` instances (and associated metadata) specific to the executed authorization grant type.
**7**`attributes`: The additional attributes specific to the executed authorization grant type – for example, the authenticated `Principal`, `OAuth2AuthorizationRequest`, and others.

`OAuth2Authorization` and its associated `OAuth2Token` instances have a set lifespan. A newly issued `OAuth2Token` is active and becomes inactive when it either expires or is invalidated (revoked). The `OAuth2Authorization` is (implicitly) inactive when all associated `OAuth2Token` instances are inactive. Each `OAuth2Token` is held in an `OAuth2Authorization.Token`, which provides accessors for `isExpired()`, `isInvalidated()`, and `isActive()`.

`OAuth2Authorization.Token` also provides `getClaims()`, which returns the claims (if any) associated with the `OAuth2Token`.

[](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/core-model-components.html#oauth2AuthorizationServer-oauth2-authorization-service)OAuth2AuthorizationService
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The `OAuth2AuthorizationService` is the central component where new authorizations are stored and existing authorizations are queried. It is used by other components when following a specific protocol flow – for example, client authentication, authorization grant processing, token introspection, token revocation, dynamic client registration, and others.

The provided implementations of `OAuth2AuthorizationService` are `InMemoryOAuth2AuthorizationService` and `JdbcOAuth2AuthorizationService`. The `InMemoryOAuth2AuthorizationService` implementation stores `OAuth2Authorization` instances in-memory and is recommended **ONLY** to be used during development and testing. `JdbcOAuth2AuthorizationService` is a JDBC implementation that persists `OAuth2Authorization` instances by using `JdbcOperations`.

The `OAuth2AuthorizationService` is an **OPTIONAL** component and defaults to `InMemoryOAuth2AuthorizationService`.

The following example shows how to register an `OAuth2AuthorizationService``@Bean`:

```
@Bean
public OAuth2AuthorizationService authorizationService() {
	return new InMemoryOAuth2AuthorizationService();
}
```

```
@Bean
public SecurityFilterChain authorizationServerSecurityFilterChain(HttpSecurity http) throws Exception {
	http
		.oauth2AuthorizationServer((authorizationServer) ->
			authorizationServer
				.authorizationService(authorizationService)
		)
	    ...

	return http.build();
}
```

The `OAuth2AuthorizationServerConfigurer` is useful when applying multiple configuration options simultaneously.

[](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/core-model-components.html#oauth2AuthorizationServer-oauth2-authorization-consent)OAuth2AuthorizationConsent
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

An `OAuth2AuthorizationConsent` is a representation of an authorization "consent" (decision) from an [OAuth2 authorization request flow](https://datatracker.ietf.org/doc/html/rfc6749#section-4.1.1) – for example, the `authorization_code` grant, which holds the authorities granted to a [client](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/core-model-components.html#oauth2AuthorizationServer-registered-client) by the resource owner.

When authorizing access to a client, the resource owner may grant only a subset of the authorities requested by the client. The typical use case is the `authorization_code` grant flow, in which the client requests scope(s) and the resource owner grants (or denies) access to the requested scope(s).

After the completion of an OAuth2 authorization request flow, an `OAuth2AuthorizationConsent` is created (or updated) and associates the granted authorities with the client and resource owner.

`OAuth2AuthorizationConsent` and its attributes are defined as follows:

```
public final class OAuth2AuthorizationConsent implements Serializable {
	private final String registeredClientId;    (1)
	private final String principalName; (2)
	private final Set<GrantedAuthority> authorities;    (3)

	...

}
```

**1**`registeredClientId`: The ID that uniquely identifies the [RegisteredClient](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/core-model-components.html#oauth2AuthorizationServer-registered-client).
**2**`principalName`: The principal name of the resource owner.
**3**`authorities`: The authorities granted to the client by the resource owner. An authority can represent a scope, a claim, a permission, a role, and others.

[](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/core-model-components.html#oauth2AuthorizationServer-oauth2-authorization-consent-service)OAuth2AuthorizationConsentService
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The `OAuth2AuthorizationConsentService` is the central component where new authorization consents are stored and existing authorization consents are queried. It is primarily used by components that implement an OAuth2 authorization request flow – for example, the `authorization_code` grant.

The provided implementations of `OAuth2AuthorizationConsentService` are `InMemoryOAuth2AuthorizationConsentService` and `JdbcOAuth2AuthorizationConsentService`. The `InMemoryOAuth2AuthorizationConsentService` implementation stores `OAuth2AuthorizationConsent` instances in-memory and is recommended **ONLY** for development and testing. `JdbcOAuth2AuthorizationConsentService` is a JDBC implementation that persists `OAuth2AuthorizationConsent` instances by using `JdbcOperations`.

The `OAuth2AuthorizationConsentService` is an **OPTIONAL** component and defaults to `InMemoryOAuth2AuthorizationConsentService`.

The following example shows how to register an `OAuth2AuthorizationConsentService``@Bean`:

```
@Bean
public OAuth2AuthorizationConsentService authorizationConsentService() {
	return new InMemoryOAuth2AuthorizationConsentService();
}
```

```
@Bean
public SecurityFilterChain authorizationServerSecurityFilterChain(HttpSecurity http) throws Exception {
	http
		.oauth2AuthorizationServer((authorizationServer) ->
			authorizationServer
				.authorizationConsentService(authorizationConsentService)
		)
	    ...

	return http.build();
}
```

The `OAuth2AuthorizationServerConfigurer` is useful when applying multiple configuration options simultaneously.

[](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/core-model-components.html#oauth2AuthorizationServer-oauth2-token-context)OAuth2TokenContext
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

An `OAuth2TokenContext` is a context object that holds information associated with an `OAuth2Token` and is used by an [OAuth2TokenGenerator](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/core-model-components.html#oauth2AuthorizationServer-oauth2-token-generator) and [OAuth2TokenCustomizer](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/core-model-components.html#oauth2AuthorizationServer-oauth2-token-customizer).

`OAuth2TokenContext` provides the following accessors:

```
public interface OAuth2TokenContext extends Context {

	default RegisteredClient getRegisteredClient() ...  (1)

	default <T extends Authentication> T getPrincipal() ... (2)

	default AuthorizationServerContext getAuthorizationServerContext() ...    (3)

	@Nullable
	default OAuth2Authorization getAuthorization() ...  (4)

	default Set<String> getAuthorizedScopes() ...   (5)

	default OAuth2TokenType getTokenType() ...  (6)

	default AuthorizationGrantType getAuthorizationGrantType() ...  (7)

	default <T extends Authentication> T getAuthorizationGrant() ...    (8)

	...

}
```

**1**`getRegisteredClient()`: The [RegisteredClient](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/core-model-components.html#oauth2AuthorizationServer-registered-client) associated with the authorization grant.
**2**`getPrincipal()`: The `Authentication` instance of the resource owner (or client).
**3**`getAuthorizationServerContext()`: The [`AuthorizationServerContext`](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/configuration-model.html#oauth2AuthorizationServer-configuring-authorization-server-settings) object that holds information of the Authorization Server runtime environment.
**4**`getAuthorization()`: The [OAuth2Authorization](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/core-model-components.html#oauth2AuthorizationServer-oauth2-authorization) associated with the authorization grant.
**5**`getAuthorizedScopes()`: The scope(s) authorized for the client.
**6**`getTokenType()`: The `OAuth2TokenType` to generate. The supported values are `code`, `access_token`, `refresh_token`, and `id_token`.
**7**`getAuthorizationGrantType()`: The `AuthorizationGrantType` associated with the authorization grant.
**8**`getAuthorizationGrant()`: The `Authentication` instance used by the `AuthenticationProvider` that processes the authorization grant.

[](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/core-model-components.html#oauth2AuthorizationServer-oauth2-token-generator)OAuth2TokenGenerator
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

An `OAuth2TokenGenerator` is responsible for generating an `OAuth2Token` from the information contained in the provided [OAuth2TokenContext](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/core-model-components.html#oauth2AuthorizationServer-oauth2-token-context).

The `OAuth2Token` generated primarily depends on the type of `OAuth2TokenType` specified in the `OAuth2TokenContext`.

For example, when the `value` for `OAuth2TokenType` is:

*   `code`, then `OAuth2AuthorizationCode` is generated.

*   `access_token`, then `OAuth2AccessToken` is generated.

*   `refresh_token`, then `OAuth2RefreshToken` is generated.

*   `id_token`, then `OidcIdToken` is generated.

Furthermore, the format of the generated `OAuth2AccessToken` varies, depending on the `TokenSettings.getAccessTokenFormat()` configured for the [RegisteredClient](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/core-model-components.html#oauth2AuthorizationServer-registered-client). If the format is `OAuth2TokenFormat.SELF_CONTAINED` (the default), then a `Jwt` is generated. If the format is `OAuth2TokenFormat.REFERENCE`, then an "opaque" token is generated.

Finally, if the generated `OAuth2Token` has a set of claims and implements `ClaimAccessor`, the claims are made accessible from [OAuth2Authorization.Token.getClaims()](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/core-model-components.html#oauth2AuthorizationServer-oauth2-authorization).

The `OAuth2TokenGenerator` is primarily used by components that implement authorization grant processing – for example, `authorization_code`, `client_credentials`, and `refresh_token`.

The provided implementations are `OAuth2AccessTokenGenerator`, `OAuth2RefreshTokenGenerator`, and `JwtGenerator`. The `OAuth2AccessTokenGenerator` generates an "opaque" (`OAuth2TokenFormat.REFERENCE`) access token, and the `JwtGenerator` generates a `Jwt` (`OAuth2TokenFormat.SELF_CONTAINED`).

The `OAuth2TokenGenerator` is an **OPTIONAL** component and defaults to a `DelegatingOAuth2TokenGenerator` composed of an `OAuth2AccessTokenGenerator` and `OAuth2RefreshTokenGenerator`.

If a `JwtEncoder``@Bean` or `JWKSource<SecurityContext>``@Bean` is registered, then a `JwtGenerator` is additionally composed in the `DelegatingOAuth2TokenGenerator`.

The `OAuth2TokenGenerator` provides great flexibility, as it can support any custom token format for `access_token` and `refresh_token`.

The following example shows how to register an `OAuth2TokenGenerator``@Bean`:

```
@Bean
public OAuth2TokenGenerator<?> tokenGenerator() {
	JwtEncoder jwtEncoder = ...
	JwtGenerator jwtGenerator = new JwtGenerator(jwtEncoder);
	OAuth2AccessTokenGenerator accessTokenGenerator = new OAuth2AccessTokenGenerator();
	OAuth2RefreshTokenGenerator refreshTokenGenerator = new OAuth2RefreshTokenGenerator();
	return new DelegatingOAuth2TokenGenerator(
			jwtGenerator, accessTokenGenerator, refreshTokenGenerator);
}
```

```
@Bean
public SecurityFilterChain authorizationServerSecurityFilterChain(HttpSecurity http) throws Exception {
	http
		.oauth2AuthorizationServer((authorizationServer) ->
			authorizationServer
				.tokenGenerator(tokenGenerator)
		)
	    ...

	return http.build();
}
```

The `OAuth2AuthorizationServerConfigurer` is useful when applying multiple configuration options simultaneously.

[](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/core-model-components.html#oauth2AuthorizationServer-oauth2-token-customizer)OAuth2TokenCustomizer
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

An `OAuth2TokenCustomizer` provides the ability to customize the attributes of an `OAuth2Token`, which are accessible in the provided [OAuth2TokenContext](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/core-model-components.html#oauth2AuthorizationServer-oauth2-token-context). It is used by an [OAuth2TokenGenerator](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/core-model-components.html#oauth2AuthorizationServer-oauth2-token-generator) to let it customize the attributes of the `OAuth2Token` before it is generated.

An `OAuth2TokenCustomizer<OAuth2TokenClaimsContext>` declared with a generic type of `OAuth2TokenClaimsContext` (`implements OAuth2TokenContext`) provides the ability to customize the claims of an "opaque" `OAuth2AccessToken`. `OAuth2TokenClaimsContext.getClaims()` provides access to the `OAuth2TokenClaimsSet.Builder`, allowing the ability to add, replace, and remove claims.

The following example shows how to implement an `OAuth2TokenCustomizer<OAuth2TokenClaimsContext>` and configure it with an `OAuth2AccessTokenGenerator`:

```
@Bean
public OAuth2TokenGenerator<?> tokenGenerator() {
	JwtEncoder jwtEncoder = ...
	JwtGenerator jwtGenerator = new JwtGenerator(jwtEncoder);
	OAuth2AccessTokenGenerator accessTokenGenerator = new OAuth2AccessTokenGenerator();
	accessTokenGenerator.setAccessTokenCustomizer(accessTokenCustomizer());
	OAuth2RefreshTokenGenerator refreshTokenGenerator = new OAuth2RefreshTokenGenerator();
	return new DelegatingOAuth2TokenGenerator(
			jwtGenerator, accessTokenGenerator, refreshTokenGenerator);
}

@Bean
public OAuth2TokenCustomizer<OAuth2TokenClaimsContext> accessTokenCustomizer() {
	return context -> {
		OAuth2TokenClaimsSet.Builder claims = context.getClaims();
		// Customize claims

	};
}
```

If the `OAuth2TokenGenerator` is not provided as a `@Bean` or is not configured through the `OAuth2AuthorizationServerConfigurer`, an `OAuth2TokenCustomizer<OAuth2TokenClaimsContext>``@Bean` will automatically be configured with an `OAuth2AccessTokenGenerator`.

An `OAuth2TokenCustomizer<JwtEncodingContext>` declared with a generic type of `JwtEncodingContext` (`implements OAuth2TokenContext`) provides the ability to customize the headers and claims of a `Jwt`. `JwtEncodingContext.getJwsHeader()` provides access to the `JwsHeader.Builder`, allowing the ability to add, replace, and remove headers. `JwtEncodingContext.getClaims()` provides access to the `JwtClaimsSet.Builder`, allowing the ability to add, replace, and remove claims.

The following example shows how to implement an `OAuth2TokenCustomizer<JwtEncodingContext>` and configure it with a `JwtGenerator`:

```
@Bean
public OAuth2TokenGenerator<?> tokenGenerator() {
	JwtEncoder jwtEncoder = ...
	JwtGenerator jwtGenerator = new JwtGenerator(jwtEncoder);
	jwtGenerator.setJwtCustomizer(jwtCustomizer());
	OAuth2AccessTokenGenerator accessTokenGenerator = new OAuth2AccessTokenGenerator();
	OAuth2RefreshTokenGenerator refreshTokenGenerator = new OAuth2RefreshTokenGenerator();
	return new DelegatingOAuth2TokenGenerator(
			jwtGenerator, accessTokenGenerator, refreshTokenGenerator);
}

@Bean
public OAuth2TokenCustomizer<JwtEncodingContext> jwtCustomizer() {
	return context -> {
		JwsHeader.Builder headers = context.getJwsHeader();
		JwtClaimsSet.Builder claims = context.getClaims();
		if (context.getTokenType().equals(OAuth2TokenType.ACCESS_TOKEN)) {
			// Customize headers/claims for access_token

		} else if (context.getTokenType().getValue().equals(OidcParameterNames.ID_TOKEN)) {
			// Customize headers/claims for id_token

		}
	};
}
```

If the `OAuth2TokenGenerator` is not provided as a `@Bean` or is not configured through the `OAuth2AuthorizationServerConfigurer`, an `OAuth2TokenCustomizer<JwtEncodingContext>``@Bean` will automatically be configured with a `JwtGenerator`.

[](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/core-model-components.html#oauth2AuthorizationServer-session-registry)SessionRegistry
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

If OpenID Connect 1.0 is enabled, a `SessionRegistry` instance is used to track authenticated sessions. The `SessionRegistry` is used by the default implementation of `SessionAuthenticationStrategy` associated to the [OAuth2 Authorization Endpoint](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/protocol-endpoints.html#oauth2AuthorizationServer-oauth2-authorization-endpoint) for registering new authenticated sessions.

If a `SessionRegistry``@Bean` is not registered, the default implementation `SessionRegistryImpl` will be used.

If a `SessionRegistry``@Bean` is registered and is an instance of `SessionRegistryImpl`, a `HttpSessionEventPublisher``@Bean`**SHOULD** also be registered as it’s responsible for notifying `SessionRegistryImpl` of session lifecycle events, for example, `SessionDestroyedEvent`, to provide the ability to remove the `SessionInformation` instance.

When a logout is requested by an End-User, the [OpenID Connect 1.0 Logout Endpoint](https://docs.spring.io/spring-security/reference/servlet/oauth2/authorization-server/protocol-endpoints.html#oauth2AuthorizationServer-oidc-logout-endpoint) uses the `SessionRegistry` to lookup the `SessionInformation` associated to the authenticated End-User to perform the logout.

If Spring Security’s [Concurrent Session Control](https://docs.spring.io/spring-security/reference/servlet/authentication/session-management.html#ns-concurrent-sessions) feature is being used, it is **RECOMMENDED** to register a `SessionRegistry``@Bean` to ensure it’s shared between Spring Security’s Concurrent Session Control and Spring Security Authorization Server’s Logout feature.

The following example shows how to register a `SessionRegistry``@Bean` and `HttpSessionEventPublisher``@Bean` (required by `SessionRegistryImpl`):

```
@Bean
public SessionRegistry sessionRegistry() {
	return new SessionRegistryImpl();
}

@Bean
public HttpSessionEventPublisher httpSessionEventPublisher() {
	return new HttpSessionEventPublisher();
}
```
