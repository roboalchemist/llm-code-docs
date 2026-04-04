# Source: https://docs.spring.io/spring-security/reference/servlet/oauth2/index.html

Title: OAuth2 :: Spring Security

URL Source: https://docs.spring.io/spring-security/reference/servlet/oauth2/index.html

Markdown Content:
To get started, add the `spring-security-oauth2-client` dependency to your project. When using Spring Boot, add the following starter:

OAuth2 Client with Spring Boot

*   Gradle

*   Maven

`implementation 'org.springframework.boot:spring-boot-starter-oauth2-client'`

Consider the following use cases for OAuth2 Client:

*   I want to [log users in using OAuth 2.0 or OpenID Connect 1.0](https://docs.spring.io/spring-security/reference/servlet/oauth2/index.html#oauth2-client-log-users-in)

*   I want to [use `RestClient` to obtain an access token for users](https://docs.spring.io/spring-security/reference/servlet/oauth2/index.html#oauth2-client-access-protected-resources) in order to access a third-party API

*   I want to [use `WebClient` to obtain an access token for users](https://docs.spring.io/spring-security/reference/servlet/oauth2/index.html#oauth2-client-access-protected-resources-webclient) in order to access a third-party API

*   I want to [do both](https://docs.spring.io/spring-security/reference/servlet/oauth2/index.html#oauth2-client-access-protected-resources-current-user) (log users in _and_ access a third-party API)

*   I want to [use the `client_credentials` grant type](https://docs.spring.io/spring-security/reference/servlet/oauth2/index.html#oauth2-client-client-credentials) to obtain a single token per application

*   I want to [enable an extension grant type](https://docs.spring.io/spring-security/reference/servlet/oauth2/index.html#oauth2-client-enable-extension-grant-type)

*   I want to [customize an existing grant type](https://docs.spring.io/spring-security/reference/servlet/oauth2/index.html#oauth2-client-customize-existing-grant-type)

*   I want to [customize token request parameters](https://docs.spring.io/spring-security/reference/servlet/oauth2/index.html#oauth2-client-customize-request-parameters)

*   I want to [customize the `RestClient` used by OAuth2 Client components](https://docs.spring.io/spring-security/reference/servlet/oauth2/index.html#oauth2-client-customize-rest-client)

### [](https://docs.spring.io/spring-security/reference/servlet/oauth2/index.html#oauth2-client-log-users-in)Log Users In with OAuth2

It is very common to require users to log in via OAuth2. [OpenID Connect 1.0](https://openid.net/specs/openid-connect-core-1_0.html) provides a special token called the `id_token` which is designed to provide an OAuth2 Client with the ability to perform user identity verification and log users in. In certain cases, OAuth2 can be used directly to log users in (as is the case with popular social login providers that do not implement OpenID Connect such as GitHub and Facebook).

The following example configures the application to act as an OAuth2 Client capable of logging users in with OAuth2 or OpenID Connect:

Configure OAuth2 Login

*   Java

*   Kotlin

```
@Configuration
@EnableWebSecurity
public class SecurityConfig {

	@Bean
	public SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
		http
			// ...
			.oauth2Login(Customizer.withDefaults());
		return http.build();
	}

}
```

In addition to the above configuration, the application requires at least one `ClientRegistration` to be configured through the use of a `ClientRegistrationRepository` bean. The following example configures an `InMemoryClientRegistrationRepository` bean using Spring Boot configuration properties:

```
spring:
  security:
    oauth2:
      client:
        registration:
          my-oidc-client:
            provider: my-oidc-provider
            client-id: my-client-id
            client-secret: my-client-secret
            authorization-grant-type: authorization_code
            scope: openid,profile
        provider:
          my-oidc-provider:
            issuer-uri: https://my-oidc-provider.com
```

With the above configuration, the application now supports two additional endpoints:

1.   The login endpoint (e.g. `/oauth2/authorization/my-oidc-client`) is used to initiate login and perform a redirect to the third party authorization server.

2.   The redirection endpoint (e.g. `/login/oauth2/code/my-oidc-client`) is used by the authorization server to redirect back to the client application, and will contain a `code` parameter used to obtain an `id_token` and/or `access_token` via the access token request.

The presence of the `openid` scope in the above configuration indicates that OpenID Connect 1.0 should be used. This instructs Spring Security to use OIDC-specific components (such as `OidcUserService`) during request processing. Without this scope, Spring Security will use OAuth2-specific components (such as `DefaultOAuth2UserService`) instead.

### [](https://docs.spring.io/spring-security/reference/servlet/oauth2/index.html#oauth2-client-access-protected-resources)Access Protected Resources

Making requests to a third party API that is protected by OAuth2 is a core use case of OAuth2 Client. This is accomplished by authorizing a client (represented by the `OAuth2AuthorizedClient` class in Spring Security) and accessing protected resources by placing a `Bearer` token in the `Authorization` header of an outbound request.

The following example configures the application to act as an OAuth2 Client capable of requesting protected resources from a third party API:

Configure OAuth2 Client

*   Java

*   Kotlin

```
@Configuration
@EnableWebSecurity
public class SecurityConfig {

	@Bean
	public SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
		http
			// ...
			.oauth2Client(Customizer.withDefaults());
		return http.build();
	}

}
```

The above example does not provide a way to log users in. You can use any other login mechanism (such as `formLogin()`). See the [next section](https://docs.spring.io/spring-security/reference/servlet/oauth2/index.html#oauth2-client-access-protected-resources-current-user) for an example combining `oauth2Client()` with `oauth2Login()`.

In addition to the above configuration, the application requires at least one `ClientRegistration` to be configured through the use of a `ClientRegistrationRepository` bean. The following example configures an `InMemoryClientRegistrationRepository` bean using Spring Boot configuration properties:

```
spring:
  security:
    oauth2:
      client:
        registration:
          my-oauth2-client:
            provider: my-auth-server
            client-id: my-client-id
            client-secret: my-client-secret
            authorization-grant-type: authorization_code
            scope: message.read,message.write
        provider:
          my-auth-server:
            issuer-uri: https://my-auth-server.com
```

In addition to configuring Spring Security to support OAuth2 Client features, you will also need to decide how you will be accessing protected resources and configure your application accordingly. Spring Security provides implementations of `OAuth2AuthorizedClientManager` for obtaining access tokens that can be used to access protected resources.

Spring Security registers a default `OAuth2AuthorizedClientManager` bean for you when one does not exist.

The easiest way to use an `OAuth2AuthorizedClientManager` is via a `ClientHttpRequestInterceptor` that intercepts requests through a `RestClient`, which is already available when `spring-web` is on the classpath.

The following example uses the default `OAuth2AuthorizedClientManager` to configure a `RestClient` capable of accessing protected resources by placing `Bearer` tokens in the `Authorization` header of each request:

Configure `RestClient` with `ClientHttpRequestInterceptor`

*   Java

*   Kotlin

```
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

This configured `RestClient` can be used as in the following example:

Use `RestClient` to Access Protected Resources

*   Java

*   Kotlin

```
import static org.springframework.security.oauth2.client.web.client.RequestAttributeClientRegistrationIdResolver.clientRegistrationId;

@RestController
public class MessagesController {

	private final RestClient restClient;

	public MessagesController(RestClient restClient) {
		this.restClient = restClient;
	}

	@GetMapping("/messages")
	public ResponseEntity<List<Message>> messages() {
		Message[] messages = this.restClient.get()
				.uri("http://localhost:8090/messages")
				.attributes(clientRegistrationId("my-oauth2-client"))
				.retrieve()
				.body(Message[].class);
		return ResponseEntity.ok(Arrays.asList(messages));
	}

	public record Message(String message) {
	}

}
```

### [](https://docs.spring.io/spring-security/reference/servlet/oauth2/index.html#oauth2-client-access-protected-resources-webclient)Access Protected Resources with `WebClient`

Making requests to a third party API that is protected by OAuth2 is a core use case of OAuth2 Client. This is accomplished by authorizing a client (represented by the `OAuth2AuthorizedClient` class in Spring Security) and accessing protected resources by placing a `Bearer` token in the `Authorization` header of an outbound request.

The following example configures the application to act as an OAuth2 Client capable of requesting protected resources from a third party API:

Configure OAuth2 Client

*   Java

*   Kotlin

```
@Configuration
@EnableWebSecurity
public class SecurityConfig {

	@Bean
	public SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
		http
			// ...
			.oauth2Client(Customizer.withDefaults());
		return http.build();
	}

}
```

The above example does not provide a way to log users in. You can use any other login mechanism (such as `formLogin()`). See the [previous section](https://docs.spring.io/spring-security/reference/servlet/oauth2/index.html#oauth2-client-access-protected-resources-current-user) for an example combining `oauth2Client()` with `oauth2Login()`.

In addition to the above configuration, the application requires at least one `ClientRegistration` to be configured through the use of a `ClientRegistrationRepository` bean. The following example configures an `InMemoryClientRegistrationRepository` bean using Spring Boot configuration properties:

```
spring:
  security:
    oauth2:
      client:
        registration:
          my-oauth2-client:
            provider: my-auth-server
            client-id: my-client-id
            client-secret: my-client-secret
            authorization-grant-type: authorization_code
            scope: message.read,message.write
        provider:
          my-auth-server:
            issuer-uri: https://my-auth-server.com
```

In addition to configuring Spring Security to support OAuth2 Client features, you will also need to decide how you will be accessing protected resources and configure your application accordingly. Spring Security provides implementations of `OAuth2AuthorizedClientManager` for obtaining access tokens that can be used to access protected resources.

Spring Security registers a default `OAuth2AuthorizedClientManager` bean for you when one does not exist.

[Instead of configuring a `RestClient`](https://docs.spring.io/spring-security/reference/servlet/oauth2/index.html#oauth2-client-access-protected-resources), another way to use an `OAuth2AuthorizedClientManager` is via an `ExchangeFilterFunction` that intercepts requests through a `WebClient`. To use `WebClient`, you will need to add the `spring-webflux` dependency along with a reactive client implementation:

Add Spring WebFlux Dependency

*   Gradle

*   Maven

```
implementation 'org.springframework:spring-webflux'
implementation 'io.projectreactor.netty:reactor-netty'
```

The following example uses the default `OAuth2AuthorizedClientManager` to configure a `WebClient` capable of accessing protected resources by placing `Bearer` tokens in the `Authorization` header of each request:

Configure `WebClient` with `ExchangeFilterFunction`

*   Java

*   Kotlin

```
@Configuration
public class WebClientConfig {

	@Bean
	public WebClient webClient(OAuth2AuthorizedClientManager authorizedClientManager) {
		ServletOAuth2AuthorizedClientExchangeFilterFunction filter =
				new ServletOAuth2AuthorizedClientExchangeFilterFunction(authorizedClientManager);
		return WebClient.builder()
				.apply(filter.oauth2Configuration())
				.build();
	}

}
```

This configured `WebClient` can be used as in the following example:

Use `WebClient` to Access Protected Resources

*   Java

*   Kotlin

```
import static org.springframework.security.oauth2.client.web.reactive.function.client.ServletOAuth2AuthorizedClientExchangeFilterFunction.clientRegistrationId;

@RestController
public class MessagesController {

	private final WebClient webClient;

	public MessagesController(WebClient webClient) {
		this.webClient = webClient;
	}

	@GetMapping("/messages")
	public ResponseEntity<List<Message>> messages() {
		return this.webClient.get()
				.uri("http://localhost:8090/messages")
				.attributes(clientRegistrationId("my-oauth2-client"))
				.retrieve()
				.toEntityList(Message.class)
				.block();
	}

	public record Message(String message) {
	}

}
```

### [](https://docs.spring.io/spring-security/reference/servlet/oauth2/index.html#oauth2-client-access-protected-resources-current-user)Access Protected Resources for the Current User

When a user is logged in via OAuth2 or OpenID Connect, the authorization server may provide an access token that can be used directly to access protected resources. This is convenient because it only requires a single `ClientRegistration` to be configured for both use cases simultaneously.

This section combines [Log Users In with OAuth2](https://docs.spring.io/spring-security/reference/servlet/oauth2/index.html#oauth2-client-log-users-in) and [Access Protected Resources](https://docs.spring.io/spring-security/reference/servlet/oauth2/index.html#oauth2-client-access-protected-resources) into a single configuration. Other advanced scenarios exist, such as configuring one `ClientRegistration` for login and another for accessing protected resources. All such scenarios would use the same basic configuration.

The following example configures the application to act as an OAuth2 Client capable of logging the user in _and_ requesting protected resources from a third party API:

Configure OAuth2 Login and OAuth2 Client

*   Java

*   Kotlin

```
@Configuration
@EnableWebSecurity
public class SecurityConfig {

	@Bean
	public SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
		http
			// ...
			.oauth2Login(Customizer.withDefaults())
			.oauth2Client(Customizer.withDefaults());
		return http.build();
	}

}
```

In addition to the above configuration, the application requires at least one `ClientRegistration` to be configured through the use of a `ClientRegistrationRepository` bean. The following example configures an `InMemoryClientRegistrationRepository` bean using Spring Boot configuration properties:

```
spring:
  security:
    oauth2:
      client:
        registration:
          my-combined-client:
            provider: my-auth-server
            client-id: my-client-id
            client-secret: my-client-secret
            authorization-grant-type: authorization_code
            scope: openid,profile,message.read,message.write
        provider:
          my-auth-server:
            issuer-uri: https://my-auth-server.com
```

The main difference between the previous examples ([Log Users In with OAuth2](https://docs.spring.io/spring-security/reference/servlet/oauth2/index.html#oauth2-client-log-users-in), [Access Protected Resources](https://docs.spring.io/spring-security/reference/servlet/oauth2/index.html#oauth2-client-access-protected-resources)) and this one is what is configured via the `scope` property, which combines the standard scopes `openid` and `profile` with the custom scopes `message.read` and `message.write`.

In addition to configuring Spring Security to support OAuth2 Client features, you will also need to decide how you will be accessing protected resources and configure your application accordingly. Spring Security provides implementations of `OAuth2AuthorizedClientManager` for obtaining access tokens that can be used to access protected resources.

Spring Security registers a default `OAuth2AuthorizedClientManager` bean for you when one does not exist.

The easiest way to use an `OAuth2AuthorizedClientManager` is via a `ClientHttpRequestInterceptor` that intercepts requests through a `RestClient`, which is already available when `spring-web` is on the classpath.

The following example uses the default `OAuth2AuthorizedClientManager` to configure a `RestClient` capable of accessing protected resources by placing `Bearer` tokens in the `Authorization` header of each request:

Configure `RestClient` with `ClientHttpRequestInterceptor`

*   Java

*   Kotlin

```
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
				? principal.getAuthorizedClientRegistrationId()
				: null;
		};
	}

}
```

This configured `RestClient` can be used as in the following example:

Use `RestClient` to Access Protected Resources (Current User)

*   Java

*   Kotlin

```
@RestController
public class MessagesController {

	private final RestClient restClient;

	public MessagesController(RestClient restClient) {
		this.restClient = restClient;
	}

	@GetMapping("/messages")
	public ResponseEntity<List<Message>> messages() {
		Message[] messages = this.restClient.get()
				.uri("http://localhost:8090/messages")
				.retrieve()
				.body(Message[].class);
		return ResponseEntity.ok(Arrays.asList(messages));
	}

	public record Message(String message) {
	}

}
```

Unlike the [previous example](https://docs.spring.io/spring-security/reference/servlet/oauth2/index.html#oauth2-client-accessing-protected-resources-example), notice that we do not need to tell Spring Security about the `clientRegistrationId` we’d like to use. This is because it can be derived from the currently logged in user.

### [](https://docs.spring.io/spring-security/reference/servlet/oauth2/index.html#oauth2-client-client-credentials)Use the Client Credentials Grant

This section focuses on additional considerations for the client credentials grant type. See [Access Protected Resources](https://docs.spring.io/spring-security/reference/servlet/oauth2/index.html#oauth2-client-access-protected-resources) for general setup and usage with all grant types.

The [client credentials grant](https://tools.ietf.org/html/rfc6749#section-1.3.4) allows a client to obtain an `access_token` on behalf of itself. The client credentials grant is a simple flow that does not involve a resource owner (i.e. a user).

It is important to note that typical use of the client credentials grant implies that any request (or user) can potentially obtain an access token and make protected resources requests to a resource server. Exercise caution when designing applications to ensure that users cannot make unauthorized requests since every request will be able to obtain an access token.

When obtaining access tokens within a web application where users can log in, the default behavior of Spring Security is to obtain an access token per user.

By default, access tokens are scoped to the principal name of the current user which means every user will receive a unique access token.

Clients using the client credentials grant typically require access tokens to be scoped to the application instead of to individual users so there is only one access token per application. In order to scope access tokens to the application, you will need to set a strategy for resolving a custom principal name. The following example does this by configuring a `RestClient` with the `RequestAttributePrincipalResolver`:

Configure `RestClient` for `client_credentials`

*   Java

*   Kotlin

```
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

With the above configuration in place, a principal name can be specified for each request. The following example demonstrates how to scope access tokens to the application by specifying a principal name:

Scope Access Tokens to the Application

*   Java

*   Kotlin

```
import static org.springframework.security.oauth2.client.web.client.RequestAttributeClientRegistrationIdResolver.clientRegistrationId;
import static org.springframework.security.oauth2.client.web.client.RequestAttributePrincipalResolver.principal;

@RestController
public class MessagesController {

	private final RestClient restClient;

	public MessagesController(RestClient restClient) {
		this.restClient = restClient;
	}

	@GetMapping("/messages")
	public ResponseEntity<List<Message>> messages() {
		Message[] messages = this.restClient.get()
				.uri("http://localhost:8090/messages")
				.attributes(clientRegistrationId("my-oauth2-client"))
				.attributes(principal("my-application"))
				.retrieve()
				.body(Message[].class);
		return ResponseEntity.ok(Arrays.asList(messages));
	}

	public record Message(String message) {
	}

}
```

When specifying a principal name via attributes as in the above example, there will only be a single access token and it will be used for all requests.

### [](https://docs.spring.io/spring-security/reference/servlet/oauth2/index.html#oauth2-client-enable-extension-grant-type)Enable an Extension Grant Type

A common use case involves enabling and/or configuring an extension grant type. For example, Spring Security provides support for the `jwt-bearer` and `token-exchange` grant types, but does not enable them by default because they are not part of the core OAuth 2.0 specification.

With Spring Security 6.2 and later, we can simply publish a bean for one or more `OAuth2AuthorizedClientProvider` and they will be picked up automatically. The following example simply enables the `jwt-bearer` grant type:

Enable `jwt-bearer` Grant Type

*   Java

*   Kotlin

```
@Configuration
public class SecurityConfig {

	@Bean
	public OAuth2AuthorizedClientProvider jwtBearer() {
		return new JwtBearerOAuth2AuthorizedClientProvider();
	}

}
```

A default `OAuth2AuthorizedClientManager` will be published automatically by Spring Security when one is not already provided.

Any custom `OAuth2AuthorizedClientProvider` bean will also be picked up and applied to the provided `OAuth2AuthorizedClientManager` after the default grant types.

In order to achieve the above configuration prior to Spring Security 6.2, we had to publish this bean ourselves and ensure we re-enabled default grant types as well. To understand what is being configured behind the scenes, here’s what the configuration might have looked like:

Enable `jwt-bearer` Grant Type (prior to 6.2)

*   Java

*   Kotlin

```
@Configuration
public class SecurityConfig {

	@Bean
	public OAuth2AuthorizedClientManager authorizedClientManager(
			ClientRegistrationRepository clientRegistrationRepository,
			OAuth2AuthorizedClientRepository authorizedClientRepository) {

		OAuth2AuthorizedClientProvider authorizedClientProvider =
			OAuth2AuthorizedClientProviderBuilder.builder()
				.authorizationCode()
				.refreshToken()
				.clientCredentials()
				.provider(new JwtBearerOAuth2AuthorizedClientProvider())
				.build();

		DefaultOAuth2AuthorizedClientManager authorizedClientManager =
			new DefaultOAuth2AuthorizedClientManager(
				clientRegistrationRepository, authorizedClientRepository);
		authorizedClientManager.setAuthorizedClientProvider(authorizedClientProvider);

		return authorizedClientManager;
	}

}
```

### [](https://docs.spring.io/spring-security/reference/servlet/oauth2/index.html#oauth2-client-customize-existing-grant-type)Customize an Existing Grant Type

The ability to [enable extension grant types](https://docs.spring.io/spring-security/reference/servlet/oauth2/index.html#oauth2-client-enable-extension-grant-type) by publishing a bean also provides the opportunity for customizing an existing grant type without the need to re-define the defaults. For example, if we want to customize the clock skew of the `OAuth2AuthorizedClientProvider` for the `client_credentials` grant, we can simply publish a bean like so:

Customize Client Credentials Grant Type

*   Java

*   Kotlin

```
@Configuration
public class SecurityConfig {

	@Bean
	public OAuth2AuthorizedClientProvider clientCredentials() {
		ClientCredentialsOAuth2AuthorizedClientProvider authorizedClientProvider =
				new ClientCredentialsOAuth2AuthorizedClientProvider();
		authorizedClientProvider.setClockSkew(Duration.ofMinutes(5));

		return authorizedClientProvider;
	}

}
```

### [](https://docs.spring.io/spring-security/reference/servlet/oauth2/index.html#oauth2-client-customize-request-parameters)Customize Token Request Parameters

The need to customize request parameters when obtaining an access token is fairly common. For example, let’s say we want to add a custom `audience` parameter to the token request because the provider requires this parameter for the `authorization_code` grant.

With Spring Security 6.2 and later, we can simply publish a bean of type `OAuth2AccessTokenResponseClient` with the generic type `OAuth2AuthorizationCodeGrantRequest` and it will be used by Spring Security to configure OAuth2 Client components.

The following example customizes token request parameters for the `authorization_code` grant without the DSL:

Customize Token Request Parameters for Authorization Code Grant

*   Java

*   Kotlin

```
@Configuration
public class SecurityConfig {

	@Bean
	public OAuth2AccessTokenResponseClient<OAuth2AuthorizationCodeGrantRequest> authorizationCodeAccessTokenResponseClient() {
		RestClientAuthorizationCodeTokenResponseClient accessTokenResponseClient =
			new RestClientAuthorizationCodeTokenResponseClient();
		accessTokenResponseClient.addParametersConverter(parametersConverter());

		return accessTokenResponseClient;
	}

	private static Converter<OAuth2AuthorizationCodeGrantRequest, MultiValueMap<String, String>> parametersConverter() {
		return (grantRequest) -> {
			MultiValueMap<String, String> parameters = new LinkedMultiValueMap<>();
			parameters.set("audience", "xyz_value");

			return parameters;
		};
	}

}
```

Notice that we don’t need to customize the `SecurityFilterChain` bean in this case, and can stick with the defaults. If using Spring Boot with no additional customizations, we can actually omit the `SecurityFilterChain` bean entirely.

Prior to Spring Security 6.2, we had to ensure that this customization was applied for both OAuth2 Login (if we are using this feature) and OAuth2 Client components using the Spring Security DSL. To understand what is being configured behind the scenes, here’s what the configuration might have looked like:

Customize Token Request Parameters for Authorization Code Grant (prior to 6.2)

*   Java

*   Kotlin

```
@Configuration
@EnableWebSecurity
public class SecurityConfig {

	@Bean
	public SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
		RestClientAuthorizationCodeTokenResponseClient accessTokenResponseClient =
			new RestClientAuthorizationCodeTokenResponseClient();
		accessTokenResponseClient.addParametersConverter(parametersConverter());

		http
			.authorizeHttpRequests((authorize) -> authorize
				.anyRequest().authenticated()
			)
			.oauth2Login((oauth2Login) -> oauth2Login
				.tokenEndpoint((tokenEndpoint) -> tokenEndpoint
					.accessTokenResponseClient(accessTokenResponseClient)
				)
			)
			.oauth2Client((oauth2Client) -> oauth2Client
				.authorizationCodeGrant((authorizationCode) -> authorizationCode
					.accessTokenResponseClient(accessTokenResponseClient)
				)
			);

		return http.build();
	}

	private static Converter<OAuth2AuthorizationCodeGrantRequest, MultiValueMap<String, String>> parametersConverter() {
		// ...
	}

}
```

For other grant types we can publish additional `OAuth2AccessTokenResponseClient` beans to override the defaults. For example, to customize token requests for the `client_credentials` grant we can publish the following bean:

Customize Token Request Parameters for Client Credentials Grant

*   Java

*   Kotlin

```
@Configuration
public class SecurityConfig {

	@Bean
	public OAuth2AccessTokenResponseClient<OAuth2ClientCredentialsGrantRequest> clientCredentialsAccessTokenResponseClient() {
		RestClientClientCredentialsTokenResponseClient accessTokenResponseClient =
				new RestClientClientCredentialsTokenResponseClient();
		accessTokenResponseClient.addParametersConverter(parametersConverter());

		return accessTokenResponseClient;
	}

	private static Converter<OAuth2ClientCredentialsGrantRequest, MultiValueMap<String, String>> parametersConverter() {
		// ...
	}

}
```

Spring Security automatically resolves the following generic types of `OAuth2AccessTokenResponseClient` beans:

*   `OAuth2AuthorizationCodeGrantRequest` (see `RestClientAuthorizationCodeTokenResponseClient`)

*   `OAuth2RefreshTokenGrantRequest` (see `RestClientRefreshTokenTokenResponseClient`)

*   `OAuth2ClientCredentialsGrantRequest` (see `RestClientClientCredentialsTokenResponseClient`)

*   `JwtBearerGrantRequest` (see `RestClientJwtBearerTokenResponseClient`)

*   `TokenExchangeGrantRequest` (see `RestClientTokenExchangeTokenResponseClient`)

Publishing a bean of type `OAuth2AccessTokenResponseClient<JwtBearerGrantRequest>` will automatically enable the `jwt-bearer` grant type without the need to [configure it separately](https://docs.spring.io/spring-security/reference/servlet/oauth2/index.html#oauth2-client-enable-extension-grant-type).

Publishing a bean of type `OAuth2AccessTokenResponseClient<TokenExchangeGrantRequest>` will automatically enable the `token-exchange` grant type without the need to [configure it separately](https://docs.spring.io/spring-security/reference/servlet/oauth2/index.html#oauth2-client-enable-extension-grant-type).

### [](https://docs.spring.io/spring-security/reference/servlet/oauth2/index.html#oauth2-client-customize-rest-client)Customize the `RestClient` used by OAuth2 Client Components

Another common use case is the need to customize the `RestClient` used when obtaining an access token. We might need to do this to customize processing of the response (via a custom `HttpMessageConverter`) or to apply proxy settings for a corporate network (via a customized `ClientHttpRequestFactory`).

With Spring Security 6.2 and later, we can simply publish beans of type `OAuth2AccessTokenResponseClient` and Spring Security will configure and publish an `OAuth2AuthorizedClientManager` bean for us.

The following example customizes the `RestClient` for all of the supported grant types:

Customize `RestClient` for OAuth2 Client

*   Java

*   Kotlin

```
@Configuration
public class SecurityConfig {

	@Bean
	public OAuth2AccessTokenResponseClient<OAuth2AuthorizationCodeGrantRequest> authorizationCodeAccessTokenResponseClient() {
		RestClientAuthorizationCodeTokenResponseClient accessTokenResponseClient =
			new RestClientAuthorizationCodeTokenResponseClient();
		accessTokenResponseClient.setRestClient(restClient());

		return accessTokenResponseClient;
	}

	@Bean
	public OAuth2AccessTokenResponseClient<OAuth2RefreshTokenGrantRequest> refreshTokenAccessTokenResponseClient() {
		RestClientRefreshTokenTokenResponseClient accessTokenResponseClient =
			new RestClientRefreshTokenTokenResponseClient();
		accessTokenResponseClient.setRestClient(restClient());

		return accessTokenResponseClient;
	}

	@Bean
	public OAuth2AccessTokenResponseClient<OAuth2ClientCredentialsGrantRequest> clientCredentialsAccessTokenResponseClient() {
		RestClientClientCredentialsTokenResponseClient accessTokenResponseClient =
			new RestClientClientCredentialsTokenResponseClient();
		accessTokenResponseClient.setRestClient(restClient());

		return accessTokenResponseClient;
	}

	@Bean
	public OAuth2AccessTokenResponseClient<JwtBearerGrantRequest> jwtBearerAccessTokenResponseClient() {
		RestClientJwtBearerTokenResponseClient accessTokenResponseClient =
			new RestClientJwtBearerTokenResponseClient();
		accessTokenResponseClient.setRestClient(restClient());

		return accessTokenResponseClient;
	}

	@Bean
	public OAuth2AccessTokenResponseClient<TokenExchangeGrantRequest> tokenExchangeAccessTokenResponseClient() {
		RestClientTokenExchangeTokenResponseClient accessTokenResponseClient =
			new RestClientTokenExchangeTokenResponseClient();
		accessTokenResponseClient.setRestClient(restClient());

		return accessTokenResponseClient;
	}

	@Bean
	public RestClient restClient() {
		// ...
	}

}
```

A default `OAuth2AuthorizedClientManager` will be published automatically by Spring Security when one is not already provided.

Notice that we don’t need to customize the `SecurityFilterChain` bean in this case, and can stick with the defaults. If using Spring Boot with no additional customizations, we can actually omit the `SecurityFilterChain` bean entirely.

Prior to Spring Security 6.2, we had to ensure this customization was applied to both OAuth2 Login (if we are using this feature) and OAuth2 Client components. We had to use both the Spring Security DSL (for the `authorization_code` grant) and publish a bean of type `OAuth2AuthorizedClientManager` for other grant types. To understand what is being configured behind the scenes, here’s what the configuration might have looked like:

Customize `RestClient` for OAuth2 Client (prior to 6.2)

*   Java

*   Kotlin

```
@Configuration
@EnableWebSecurity
public class SecurityConfig {

	@Bean
	public SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
		RestClientAuthorizationCodeTokenResponseClient accessTokenResponseClient =
			new RestClientAuthorizationCodeTokenResponseClient();
		accessTokenResponseClient.setRestClient(restClient());

		http
			// ...
			.oauth2Login((oauth2Login) -> oauth2Login
				.tokenEndpoint((tokenEndpoint) -> tokenEndpoint
					.accessTokenResponseClient(accessTokenResponseClient)
				)
			)
			.oauth2Client((oauth2Client) -> oauth2Client
				.authorizationCodeGrant((authorizationCode) -> authorizationCode
					.accessTokenResponseClient(accessTokenResponseClient)
				)
			);

		return http.build();
	}

	@Bean
	public OAuth2AuthorizedClientManager authorizedClientManager(
			ClientRegistrationRepository clientRegistrationRepository,
			OAuth2AuthorizedClientRepository authorizedClientRepository) {

		RestClientRefreshTokenTokenResponseClient refreshTokenAccessTokenResponseClient =
			new RestClientRefreshTokenTokenResponseClient();
		refreshTokenAccessTokenResponseClient.setRestClient(restClient());

		RestClientClientCredentialsTokenResponseClient clientCredentialsAccessTokenResponseClient =
			new RestClientClientCredentialsTokenResponseClient();
		clientCredentialsAccessTokenResponseClient.setRestClient(restClient());

		RestClientJwtBearerTokenResponseClient jwtBearerAccessTokenResponseClient =
			new RestClientJwtBearerTokenResponseClient();
		jwtBearerAccessTokenResponseClient.setRestClient(restClient());

		JwtBearerOAuth2AuthorizedClientProvider jwtBearerAuthorizedClientProvider =
			new JwtBearerOAuth2AuthorizedClientProvider();
		jwtBearerAuthorizedClientProvider.setAccessTokenResponseClient(jwtBearerAccessTokenResponseClient);

		RestClientTokenExchangeTokenResponseClient tokenExchangeAccessTokenResponseClient =
			new RestClientTokenExchangeTokenResponseClient();
		tokenExchangeAccessTokenResponseClient.setRestClient(restClient());

		TokenExchangeOAuth2AuthorizedClientProvider tokenExchangeAuthorizedClientProvider =
			new TokenExchangeOAuth2AuthorizedClientProvider();
		tokenExchangeAuthorizedClientProvider.setAccessTokenResponseClient(tokenExchangeAccessTokenResponseClient);

		OAuth2AuthorizedClientProvider authorizedClientProvider =
			OAuth2AuthorizedClientProviderBuilder.builder()
				.authorizationCode()
				.refreshToken((refreshToken) -> refreshToken
					.accessTokenResponseClient(refreshTokenAccessTokenResponseClient)
				)
				.clientCredentials((clientCredentials) -> clientCredentials
					.accessTokenResponseClient(clientCredentialsAccessTokenResponseClient)
				)
				.provider(jwtBearerAuthorizedClientProvider)
				.provider(tokenExchangeAuthorizedClientProvider)
				.build();

		DefaultOAuth2AuthorizedClientManager authorizedClientManager =
			new DefaultOAuth2AuthorizedClientManager(
				clientRegistrationRepository, authorizedClientRepository);
		authorizedClientManager.setAuthorizedClientProvider(authorizedClientProvider);

		return authorizedClientManager;
	}

	@Bean
	public RestClient restClient() {
		// ...
	}

}
```
