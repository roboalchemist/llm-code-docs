# Source: https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorization-grants.html

Title: Authorization Grant Support :: Spring Security

URL Source: https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorization-grants.html

Markdown Content:
See the OAuth 2.0 Authorization Framework for further details on the [Authorization Code](https://tools.ietf.org/html/rfc6749#section-1.3.1) grant.

### [](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorization-grants.html#oauth2-client-authorization-code-authorization-request)Initiating the Authorization Request

The `OAuth2AuthorizationRequestRedirectFilter` uses an `OAuth2AuthorizationRequestResolver` to resolve an `OAuth2AuthorizationRequest` and initiate the Authorization Code grant flow by redirecting the end-user’s user-agent to the Authorization Server’s Authorization Endpoint.

The primary role of the `OAuth2AuthorizationRequestResolver` is to resolve an `OAuth2AuthorizationRequest` from the provided web request. The default implementation `DefaultOAuth2AuthorizationRequestResolver` matches on the (default) path `/oauth2/authorization/{registrationId}`, extracting the `registrationId`, and using it to build the `OAuth2AuthorizationRequest` for the associated `ClientRegistration`.

Consider the following Spring Boot properties for an OAuth 2.0 Client registration:

```
spring:
  security:
    oauth2:
      client:
        registration:
          okta:
            client-id: okta-client-id
            client-secret: okta-client-secret
            authorization-grant-type: authorization_code
            redirect-uri: "{baseUrl}/authorized/okta"
            scope: read, write
        provider:
          okta:
            authorization-uri: https://dev-1234.oktapreview.com/oauth2/v1/authorize
            token-uri: https://dev-1234.oktapreview.com/oauth2/v1/token
```

Given the preceding properties, a request with the base path `/oauth2/authorization/okta` initiates the Authorization Request redirect by the `OAuth2AuthorizationRequestRedirectFilter` and ultimately starts the Authorization Code grant flow.

The `AuthorizationCodeOAuth2AuthorizedClientProvider` is an implementation of `OAuth2AuthorizedClientProvider` for the Authorization Code grant, which also initiates the Authorization Request redirect by the `OAuth2AuthorizationRequestRedirectFilter`.

If the OAuth 2.0 Client is a [Public Client](https://tools.ietf.org/html/rfc6749#section-2.1), configure the OAuth 2.0 Client registration as follows:

```
spring:
  security:
    oauth2:
      client:
        registration:
          okta:
            client-id: okta-client-id
            client-authentication-method: none
            authorization-grant-type: authorization_code
            redirect-uri: "{baseUrl}/authorized/okta"
            # ...
```

Public Clients are supported by using [Proof Key for Code Exchange](https://tools.ietf.org/html/rfc7636) (PKCE). If the client is running in an untrusted environment (such as a native application or web browser-based application) and is therefore incapable of maintaining the confidentiality of its credentials, PKCE is automatically used when the following conditions are true:

1.   `client-secret` is omitted (or empty)

2.   `client-authentication-method` is set to `none` (`ClientAuthenticationMethod.NONE`)

or

1.   When `ClientRegistration.clientSettings.requireProofKey` is `true` (in this case `ClientRegistration.authorizationGrantType` must be `authorization_code`)

If the OAuth 2.0 Provider doesn’t support PKCE for [Confidential Clients](https://tools.ietf.org/html/rfc6749#section-2.1), you need to disable it by setting `ClientRegistration.clientSettings.requireProofKey` to `false`.

[](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorization-grants.html)The `DefaultOAuth2AuthorizationRequestResolver` also supports `URI` template variables for the `redirect-uri` by using `UriComponentsBuilder`.

The following configuration uses all the supported `URI` template variables:

```
spring:
  security:
    oauth2:
      client:
        registration:
          okta:
            # ...
            redirect-uri: "{baseScheme}://{baseHost}{basePort}{basePath}/authorized/{registrationId}"
            # ...
```

`{baseUrl}` resolves to `{baseScheme}://{baseHost}{basePort}{basePath}`

Configuring the `redirect-uri` with `URI` template variables is especially useful when the OAuth 2.0 Client is running behind a [Proxy Server](https://docs.spring.io/spring-security/reference/features/exploits/http.html#http-proxy-server). Doing so ensures that the `X-Forwarded-*` headers are used when expanding the `redirect-uri`.

### [](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorization-grants.html#oauth2-client-authorization-code-authorization-request-resolver)Customizing the Authorization Request

One of the primary use cases an `OAuth2AuthorizationRequestResolver` can realize is the ability to customize the Authorization Request with additional parameters above the standard parameters defined in the OAuth 2.0 Authorization Framework.

For example, OpenID Connect defines additional OAuth 2.0 request parameters for the [Authorization Code Flow](https://openid.net/specs/openid-connect-core-1_0.html#AuthRequest) extending from the standard parameters defined in the [OAuth 2.0 Authorization Framework](https://tools.ietf.org/html/rfc6749#section-4.1.1). One of those extended parameters is the `prompt` parameter.

The `prompt` parameter is optional. Space delimited, case sensitive list of ASCII string values that specifies whether the Authorization Server prompts the End-User for re-authentication and consent. The defined values are: `none`, `login`, `consent`, and `select_account`.

The following example shows how to configure the `DefaultOAuth2AuthorizationRequestResolver` with a `Consumer<OAuth2AuthorizationRequest.Builder>` that customizes the Authorization Request for `oauth2Login()`, by including the request parameter `prompt=consent`.

*   Java

*   Kotlin

```
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
			.oauth2Login((oauth2) -> oauth2
				.authorizationEndpoint((authorization) -> authorization
					.authorizationRequestResolver(
						authorizationRequestResolver(this.clientRegistrationRepository)
					)
				)
			);
		return http.build();
	}

	private OAuth2AuthorizationRequestResolver authorizationRequestResolver(
			ClientRegistrationRepository clientRegistrationRepository) {

		DefaultOAuth2AuthorizationRequestResolver authorizationRequestResolver =
				new DefaultOAuth2AuthorizationRequestResolver(
						clientRegistrationRepository, "/oauth2/authorization");
		authorizationRequestResolver.setAuthorizationRequestCustomizer(
				authorizationRequestCustomizer());

		return  authorizationRequestResolver;
	}

	private Consumer<OAuth2AuthorizationRequest.Builder> authorizationRequestCustomizer() {
		return customizer -> customizer
					.additionalParameters((params) -> params.put("prompt", "consent"));
	}
}
```

For the simple use case where the additional request parameter is always the same for a specific provider, you can add it directly in the `authorization-uri` property.

For example, if the value for the request parameter `prompt` is always `consent` for the provider `okta`, you can configure it as follows:

```
spring:
  security:
    oauth2:
      client:
        provider:
          okta:
            authorization-uri: https://dev-1234.oktapreview.com/oauth2/v1/authorize?prompt=consent
```

The preceding example shows the common use case of adding a custom parameter on top of the standard parameters. Alternatively, if your requirements are more advanced, you can take full control in building the Authorization Request URI by overriding the `OAuth2AuthorizationRequest.authorizationRequestUri` property.

`OAuth2AuthorizationRequest.Builder.build()` constructs the `OAuth2AuthorizationRequest.authorizationRequestUri`, which represents the Authorization Request URI including all query parameters using the `application/x-www-form-urlencoded` format.

The following example shows a variation of `authorizationRequestCustomizer()` from the preceding example and instead overrides the `OAuth2AuthorizationRequest.authorizationRequestUri` property:

*   Java

*   Kotlin

```
private Consumer<OAuth2AuthorizationRequest.Builder> authorizationRequestCustomizer() {
	return customizer -> customizer
				.authorizationRequestUri((uriBuilder) -> uriBuilder
					.queryParam("prompt", "consent").build());
}
```

### [](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorization-grants.html#oauth2-client-authorization-code-authorization-request-repository)Storing the Authorization Request

The `AuthorizationRequestRepository` is responsible for the persistence of the `OAuth2AuthorizationRequest` from the time the Authorization Request is initiated to the time the Authorization Response is received (the callback).

The `OAuth2AuthorizationRequest` is used to correlate and validate the Authorization Response.

The default implementation of `AuthorizationRequestRepository` is `HttpSessionOAuth2AuthorizationRequestRepository`, which stores the `OAuth2AuthorizationRequest` in the `HttpSession`.

If you have a custom implementation of `AuthorizationRequestRepository`, you can configure it as follows:

AuthorizationRequestRepository Configuration

*   Java

*   Kotlin

*   Xml

```
@Configuration
@EnableWebSecurity
public class OAuth2ClientSecurityConfig {

	@Bean
	public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
		http
			.oauth2Client((oauth2) -> oauth2
				.authorizationCodeGrant((codeGrant) -> codeGrant
					.authorizationRequestRepository(this.authorizationRequestRepository())
					// ...
				)
			)
            .oauth2Login((oauth2) -> oauth2
                .authorizationEndpoint((endpoint) -> endpoint
                    .authorizationRequestRepository(this.authorizationRequestRepository())
                    // ...
                )
            );
			return http.build();
	}

    @Bean
    public AuthorizationRequestRepository<OAuth2AuthorizationRequest> authorizationRequestRepository() {
        return new CustomOAuth2AuthorizationRequestRepository();
    }
}
```

### [](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorization-grants.html#oauth2-client-authorization-code-access-token)Requesting an Access Token

The default implementation of `OAuth2AccessTokenResponseClient` for the Authorization Code grant is `RestClientAuthorizationCodeTokenResponseClient`, which uses a `RestClient` instance to exchange an authorization code for an access token at the Authorization Server’s Token Endpoint.

`RestClientAuthorizationCodeTokenResponseClient` is very flexible and provides several options for customizing the OAuth 2.0 Access Token request and response for the Authorization Code grant. Choose from the following use cases to learn more:

*   I want to [customize headers of the Access Token request](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorization-grants.html#oauth2-client-authorization-code-access-token-request-headers)

*   I want to [customize parameters of the Access Token request](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorization-grants.html#oauth2-client-authorization-code-access-token-request-parameters)

*   I want to [customize the instance of `RestClient` that is used](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorization-grants.html#oauth2-client-authorization-code-access-token-response-rest-client)

*   I want to [customize parameters of the Access Token response](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorization-grants.html#oauth2-client-authorization-code-access-token-response-parameters)

*   I want to [customize error handling of the Access Token response](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorization-grants.html#oauth2-client-authorization-code-access-token-response-errors)

### [](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorization-grants.html#oauth2-client-authorization-code-access-token-request)Customizing the Access Token Request

`RestClientAuthorizationCodeTokenResponseClient` provides hooks for customizing HTTP headers and request parameters of the OAuth 2.0 Access Token Request.

There are two options for customizing HTTP headers:

*   Add additional headers by calling `addHeadersConverter()`

*   Fully customize headers by calling `setHeadersConverter()`

You can include additional headers without affecting the default headers added to every request using `addHeadersConverter()`. The following example adds a `User-Agent` header to the request when the `registrationId` is `spring`:

Include Additional HTTP Headers

*   Java

*   Kotlin

```
RestClientAuthorizationCodeTokenResponseClient accessTokenResponseClient =
	new RestClientAuthorizationCodeTokenResponseClient();
accessTokenResponseClient.addHeadersConverter(grantRequest -> {
	ClientRegistration clientRegistration = grantRequest.getClientRegistration();
	HttpHeaders headers = new HttpHeaders();
	if (clientRegistration.getRegistrationId().equals("spring")) {
		headers.set(HttpHeaders.USER_AGENT, "my-user-agent");
	}
	return headers;
});
```

You can fully customize headers by re-using `DefaultOAuth2TokenRequestHeadersConverter` or providing a custom implementation using `setHeadersConverter()`. The following example re-uses `DefaultOAuth2TokenRequestHeadersConverter` and disables `encodeClientCredentials` so that HTTP Basic credentials are no longer encoded with `application/x-www-form-urlencoded`:

Customize HTTP Headers

*   Java

*   Kotlin

```
DefaultOAuth2TokenRequestHeadersConverter headersConverter =
	new DefaultOAuth2TokenRequestHeadersConverter();
headersConverter.setEncodeClientCredentials(false);

RestClientAuthorizationCodeTokenResponseClient accessTokenResponseClient =
	new RestClientAuthorizationCodeTokenResponseClient();
accessTokenResponseClient.setHeadersConverter(headersConverter);
```

#### [](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorization-grants.html#oauth2-client-authorization-code-access-token-request-parameters)Customizing Request Parameters

There are three options for customizing request parameters:

*   Add additional parameters by calling `addParametersConverter()`

*   Override parameters by calling `setParametersConverter()`

*   Fully customize parameters by calling `setParametersCustomizer()`

Using `setParametersConverter()` does not fully customize parameters because it would require the user to provide all default parameters themselves. Default parameters are always provided, but can be fully customized or omitted by calling `setParametersCustomizer()`.

You can include additional parameters without affecting the default parameters added to every request using `addParametersConverter()`. The following example adds an `audience` parameter to the request when the `registrationId` is `keycloak`:

Include Additional Request Parameters

*   Java

*   Kotlin

```
RestClientAuthorizationCodeTokenResponseClient accessTokenResponseClient =
	new RestClientAuthorizationCodeTokenResponseClient();
accessTokenResponseClient.addParametersConverter(grantRequest -> {
	ClientRegistration clientRegistration = grantRequest.getClientRegistration();
	MultiValueMap<String, String> parameters = new LinkedMultiValueMap<String, String>();
	if (clientRegistration.getRegistrationId().equals("keycloak")) {
		parameters.set(OAuth2ParameterNames.AUDIENCE, "my-audience");
	}
	return parameters;
});
```

You can override default parameters using `setParametersConverter()`. The following example overrides the `client_id` parameter when the `registrationId` is `okta`:

Override Request Parameters

*   Java

*   Kotlin

```
RestClientAuthorizationCodeTokenResponseClient accessTokenResponseClient =
	new RestClientAuthorizationCodeTokenResponseClient();
accessTokenResponseClient.setParametersConverter(grantRequest -> {
	ClientRegistration clientRegistration = grantRequest.getClientRegistration();
	LinkedMultiValueMap<String, String> parameters = new LinkedMultiValueMap<>();
	if (clientRegistration.getRegistrationId().equals("okta")) {
		parameters.set(OAuth2ParameterNames.CLIENT_ID, "my-client");
	}
	return parameters;
});
```

You can fully customize parameters (including omitting default parameters) using `setParametersCustomizer()`. The following example omits the `client_id` parameter when the `client_assertion` parameter is present in the request:

Omit Request Parameters

*   Java

*   Kotlin

```
RestClientAuthorizationCodeTokenResponseClient accessTokenResponseClient =
	new RestClientAuthorizationCodeTokenResponseClient();
accessTokenResponseClient.setParametersCustomizer(parameters -> {
	if (parameters.containsKey(OAuth2ParameterNames.CLIENT_ASSERTION)) {
		parameters.remove(OAuth2ParameterNames.CLIENT_ID);
	}
});
```

### [](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorization-grants.html#oauth2-client-authorization-code-access-token-response)Customizing the Access Token Response

`RestClientAuthorizationCodeTokenResponseClient` provides hooks for customizing response parameters and error handling of the OAuth 2.0 Access Token Response.

#### [](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorization-grants.html#oauth2-client-authorization-code-access-token-response-rest-client)Customizing the `RestClient`

You can customize the Token Response by providing a pre-configured `RestClient` to `setRestClient()`. The default `RestClient` is configured as follows:

Default `RestClient` Configuration

*   Java

*   Kotlin

```
RestClient restClient = RestClient.builder()
	.messageConverters(messageConverters -> {
		messageConverters.clear();
		messageConverters.add(new FormHttpMessageConverter());
		messageConverters.add(new OAuth2AccessTokenResponseHttpMessageConverter());
	})
	.defaultStatusHandler(new OAuth2ErrorResponseErrorHandler())
	.build();

RestClientAuthorizationCodeTokenResponseClient accessTokenResponseClient =
	new RestClientAuthorizationCodeTokenResponseClient();
accessTokenResponseClient.setRestClient(restClient);
```

`OAuth2AccessTokenResponseHttpMessageConverter` is an `HttpMessageConverter` for an OAuth 2.0 Access Token Response. You can customize the conversion of Token Response parameters to an `OAuth2AccessTokenResponse` by calling `setAccessTokenResponseConverter()`. The default implementation is `DefaultMapOAuth2AccessTokenResponseConverter`.

`OAuth2ErrorResponseErrorHandler` is a `ResponseErrorHandler` that can handle an OAuth 2.0 Error, such as `400 Bad Request`. It uses an `OAuth2ErrorHttpMessageConverter` for converting the OAuth 2.0 Error parameters to an `OAuth2Error`. You can customize the conversion of Token Response parameters to an `OAuth2Error` by calling `setErrorConverter()`.

Spring MVC `FormHttpMessageConverter` is required, as it is used when sending the OAuth 2.0 Access Token Request.

#### [](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorization-grants.html#oauth2-client-authorization-code-access-token-response-parameters)Customizing Response Parameters

The following example provides a starting point for customizing the conversion of Token Response parameters to an `OAuth2AccessTokenResponse`:

Customize Access Token Response Converter

*   Java

*   Kotlin

```
OAuth2AccessTokenResponseHttpMessageConverter accessTokenResponseMessageConverter =
	new OAuth2AccessTokenResponseHttpMessageConverter();
accessTokenResponseMessageConverter.setAccessTokenResponseConverter(parameters -> {
	// ...
	return OAuth2AccessTokenResponse.withToken("custom-token")
		// ...
		.build();
});
```

#### [](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorization-grants.html#oauth2-client-authorization-code-access-token-response-errors)Customizing Error Handling

The following example provides a starting point for customizing the conversion of Error parameters to an `OAuth2Error`:

Customize Access Token Error Handler

*   Java

*   Kotlin

```
OAuth2ErrorHttpMessageConverter errorConverter =
	new OAuth2ErrorHttpMessageConverter();
errorConverter.setErrorConverter(parameters -> {
	// ...
	return new OAuth2Error("custom-error", "custom description", "custom-uri");
});

OAuth2ErrorResponseErrorHandler errorHandler =
	new OAuth2ErrorResponseErrorHandler();
errorHandler.setErrorConverter(errorConverter);
```

### [](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorization-grants.html#oauth2-client-authorization-code-access-token-response-client-dsl)Customize using the DSL

Whether you customize `RestClientAuthorizationCodeTokenResponseClient` or provide your own implementation of `OAuth2AccessTokenResponseClient`, you can configure it using the DSL (as an alternative to [publishing a bean](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorization-grants.html#oauth2-client-authorization-code-access-token-response-client-bean)) as follows:

Access Token Response Configuration via DSL

*   Java

*   Kotlin

*   Xml

```
@Configuration
@EnableWebSecurity
public class OAuth2ClientSecurityConfig {

	@Bean
	public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
		http
			.oauth2Client((oauth2) -> oauth2
				.authorizationCodeGrant((codeGrant) -> codeGrant
					.accessTokenResponseClient(this.accessTokenResponseClient())
					// ...
				)
			);
		return http.build();
	}
}
```

[](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorization-grants.html#oauth2-client-refresh-token)[](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorization-grants.html)Refresh Token
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

See the OAuth 2.0 Authorization Framework for further details on the [Refresh Token](https://tools.ietf.org/html/rfc6749#section-1.5).

### [](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorization-grants.html#oauth2-client-refresh-token-access-token)Refreshing an Access Token

The default implementation of `OAuth2AccessTokenResponseClient` for the Refresh Token grant is `RestClientRefreshTokenTokenResponseClient`, which uses a `RestClient` instance to obtain an access token at the Authorization Server’s Token Endpoint.

`RestClientRefreshTokenTokenResponseClient` is very flexible and provides several options for customizing the OAuth 2.0 Access Token request and response for the Refresh Token grant. Choose from the following use cases to learn more:

*   I want to [customize headers of the Access Token request](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorization-grants.html#oauth2-client-refresh-token-access-token-request-headers)

*   I want to [customize parameters of the Access Token request](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorization-grants.html#oauth2-client-refresh-token-access-token-request-parameters)

*   I want to [customize the instance of `RestClient` that is used](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorization-grants.html#oauth2-client-refresh-token-access-token-response-rest-client)

*   I want to [customize parameters of the Access Token response](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorization-grants.html#oauth2-client-refresh-token-access-token-response-parameters)

*   I want to [customize error handling of the Access Token response](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorization-grants.html#oauth2-client-refresh-token-access-token-response-errors)

### [](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorization-grants.html#oauth2-client-refresh-token-access-token-request)Customizing the Access Token Request

`RestClientRefreshTokenTokenResponseClient` provides hooks for customizing HTTP headers and request parameters of the OAuth 2.0 Access Token Request.

There are two options for customizing HTTP headers:

*   Add additional headers by calling `addHeadersConverter()`

*   Fully customize headers by calling `setHeadersConverter()`

You can include additional headers without affecting the default headers added to every request using `addHeadersConverter()`. The following example adds a `User-Agent` header to the request when the `registrationId` is `spring`:

Include Additional HTTP Headers

*   Java

*   Kotlin

```
RestClientRefreshTokenTokenResponseClient accessTokenResponseClient =
	new RestClientRefreshTokenTokenResponseClient();
accessTokenResponseClient.addHeadersConverter(grantRequest -> {
	ClientRegistration clientRegistration = grantRequest.getClientRegistration();
	HttpHeaders headers = new HttpHeaders();
	if (clientRegistration.getRegistrationId().equals("spring")) {
		headers.set(HttpHeaders.USER_AGENT, "my-user-agent");
	}
	return headers;
});
```

You can fully customize headers by re-using `DefaultOAuth2TokenRequestHeadersConverter` or providing a custom implementation using `setHeadersConverter()`. The following example re-uses `DefaultOAuth2TokenRequestHeadersConverter` and disables `encodeClientCredentials` so that HTTP Basic credentials are no longer encoded with `application/x-www-form-urlencoded`:

Customize HTTP Headers

*   Java

*   Kotlin

```
DefaultOAuth2TokenRequestHeadersConverter headersConverter =
	new DefaultOAuth2TokenRequestHeadersConverter();
headersConverter.setEncodeClientCredentials(false);

RestClientRefreshTokenTokenResponseClient accessTokenResponseClient =
	new RestClientRefreshTokenTokenResponseClient();
accessTokenResponseClient.setHeadersConverter(headersConverter);
```

#### [](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorization-grants.html#oauth2-client-refresh-token-access-token-request-parameters)Customizing Request Parameters

There are three options for customizing request parameters:

*   Add additional parameters by calling `addParametersConverter()`

*   Override parameters by calling `setParametersConverter()`

*   Fully customize parameters by calling `setParametersCustomizer()`

Using `setParametersConverter()` does not fully customize parameters because it would require the user to provide all default parameters themselves. Default parameters are always provided, but can be fully customized or omitted by calling `setParametersCustomizer()`.

You can include additional parameters without affecting the default parameters added to every request using `addParametersConverter()`. The following example adds an `audience` parameter to the request when the `registrationId` is `keycloak`:

Include Additional Request Parameters

*   Java

*   Kotlin

```
RestClientRefreshTokenTokenResponseClient accessTokenResponseClient =
	new RestClientRefreshTokenTokenResponseClient();
accessTokenResponseClient.addParametersConverter(grantRequest -> {
	ClientRegistration clientRegistration = grantRequest.getClientRegistration();
	MultiValueMap<String, String> parameters = new LinkedMultiValueMap<String, String>();
	if (clientRegistration.getRegistrationId().equals("keycloak")) {
		parameters.set(OAuth2ParameterNames.AUDIENCE, "my-audience");
	}
	return parameters;
});
```

You can override default parameters using `setParametersConverter()`. The following example overrides the `client_id` parameter when the `registrationId` is `okta`:

Override Request Parameters

*   Java

*   Kotlin

```
RestClientRefreshTokenTokenResponseClient accessTokenResponseClient =
	new RestClientRefreshTokenTokenResponseClient();
accessTokenResponseClient.setParametersConverter(grantRequest -> {
	ClientRegistration clientRegistration = grantRequest.getClientRegistration();
	LinkedMultiValueMap<String, String> parameters = new LinkedMultiValueMap<>();
	if (clientRegistration.getRegistrationId().equals("okta")) {
		parameters.set(OAuth2ParameterNames.CLIENT_ID, "my-client");
	}
	return parameters;
});
```

You can fully customize parameters (including omitting default parameters) using `setParametersCustomizer()`. The following example omits the `client_id` parameter when the `client_assertion` parameter is present in the request:

Omit Request Parameters

*   Java

*   Kotlin

```
RestClientRefreshTokenTokenResponseClient accessTokenResponseClient =
	new RestClientRefreshTokenTokenResponseClient();
accessTokenResponseClient.setParametersCustomizer(parameters -> {
	if (parameters.containsKey(OAuth2ParameterNames.CLIENT_ASSERTION)) {
		parameters.remove(OAuth2ParameterNames.CLIENT_ID);
	}
});
```

### [](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorization-grants.html#oauth2-client-refresh-token-access-token-response)Customizing the Access Token Response

`RestClientRefreshTokenTokenResponseClient` provides hooks for customizing response parameters and error handling of the OAuth 2.0 Access Token Response.

#### [](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorization-grants.html#oauth2-client-refresh-token-access-token-response-rest-client)Customizing the `RestClient`

You can customize the Token Response by providing a pre-configured `RestClient` to `setRestClient()`. The default `RestClient` is configured as follows:

Default `RestClient` Configuration

*   Java

*   Kotlin

```
RestClient restClient = RestClient.builder()
	.messageConverters(messageConverters -> {
		messageConverters.clear();
		messageConverters.add(new FormHttpMessageConverter());
		messageConverters.add(new OAuth2AccessTokenResponseHttpMessageConverter());
	})
	.defaultStatusHandler(new OAuth2ErrorResponseErrorHandler())
	.build();

RestClientRefreshTokenTokenResponseClient accessTokenResponseClient =
	new RestClientRefreshTokenTokenResponseClient();
accessTokenResponseClient.setRestClient(restClient);
```

`OAuth2AccessTokenResponseHttpMessageConverter` is an `HttpMessageConverter` for an OAuth 2.0 Access Token Response. You can customize the conversion of Token Response parameters to an `OAuth2AccessTokenResponse` by calling `setAccessTokenResponseConverter()`. The default implementation is `DefaultMapOAuth2AccessTokenResponseConverter`.

`OAuth2ErrorResponseErrorHandler` is a `ResponseErrorHandler` that can handle an OAuth 2.0 Error, such as `400 Bad Request`. It uses an `OAuth2ErrorHttpMessageConverter` for converting the OAuth 2.0 Error parameters to an `OAuth2Error`. You can customize the conversion of Token Response parameters to an `OAuth2Error` by calling `setErrorConverter()`.

Spring MVC `FormHttpMessageConverter` is required, as it is used when sending the OAuth 2.0 Access Token Request.

#### [](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorization-grants.html#oauth2-client-refresh-token-access-token-response-parameters)Customizing Response Parameters

The following example provides a starting point for customizing the conversion of Token Response parameters to an `OAuth2AccessTokenResponse`:

Customize Access Token Response Converter

*   Java

*   Kotlin

```
OAuth2AccessTokenResponseHttpMessageConverter accessTokenResponseMessageConverter =
	new OAuth2AccessTokenResponseHttpMessageConverter();
accessTokenResponseMessageConverter.setAccessTokenResponseConverter(parameters -> {
	// ...
	return OAuth2AccessTokenResponse.withToken("custom-token")
		// ...
		.build();
});
```

#### [](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorization-grants.html#oauth2-client-refresh-token-access-token-response-errors)Customizing Error Handling

The following example provides a starting point for customizing the conversion of Error parameters to an `OAuth2Error`:

Customize Access Token Error Handler

*   Java

*   Kotlin

```
OAuth2ErrorHttpMessageConverter errorConverter =
	new OAuth2ErrorHttpMessageConverter();
errorConverter.setErrorConverter(parameters -> {
	// ...
	return new OAuth2Error("custom-error", "custom description", "custom-uri");
});

OAuth2ErrorResponseErrorHandler errorHandler =
	new OAuth2ErrorResponseErrorHandler();
errorHandler.setErrorConverter(errorConverter);
```

### [](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorization-grants.html#oauth2-client-refresh-token-authorized-client-provider-builder)Customize using the Builder

Whether you customize `RestClientRefreshTokenTokenResponseClient` or provide your own implementation of `OAuth2AccessTokenResponseClient`, you can configure it using the `OAuth2AuthorizedClientProviderBuilder` (as an alternative to [publishing a bean](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorization-grants.html#oauth2-client-refresh-token-access-token-response-client-bean)) as follows:

Access Token Response Configuration via Builder

*   Java

*   Kotlin

```
// Customize
OAuth2AccessTokenResponseClient<OAuth2RefreshTokenGrantRequest> refreshTokenTokenResponseClient = ...

OAuth2AuthorizedClientProvider authorizedClientProvider =
		OAuth2AuthorizedClientProviderBuilder.builder()
				.authorizationCode()
				.refreshToken((configurer) -> configurer.accessTokenResponseClient(refreshTokenTokenResponseClient))
				.build();

// ...

authorizedClientManager.setAuthorizedClientProvider(authorizedClientProvider);
```

`OAuth2AuthorizedClientProviderBuilder.builder().refreshToken()` configures a `RefreshTokenOAuth2AuthorizedClientProvider`, which is an implementation of an `OAuth2AuthorizedClientProvider` for the Refresh Token grant.

The `OAuth2RefreshToken` can optionally be returned in the Access Token Response for the `authorization_code` grant type. If the `OAuth2AuthorizedClient.getRefreshToken()` is available and the `OAuth2AuthorizedClient.getAccessToken()` is expired, it is automatically refreshed by the `RefreshTokenOAuth2AuthorizedClientProvider`.

[](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorization-grants.html#oauth2-client-client-credentials)[](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorization-grants.html)Client Credentials
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Please refer to the OAuth 2.0 Authorization Framework for further details on the [Client Credentials](https://tools.ietf.org/html/rfc6749#section-1.3.4) grant.

### [](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorization-grants.html#oauth2-client-client-credentials-access-token)Requesting an Access Token

The default implementation of `OAuth2AccessTokenResponseClient` for the Client Credentials grant is `RestClientClientCredentialsTokenResponseClient`, which uses a `RestClient` instance to obtain an access token at the Authorization Server’s Token Endpoint.

`RestClientClientCredentialsTokenResponseClient` is very flexible and provides several options for customizing the OAuth 2.0 Access Token request and response for the Client Credentials grant. Choose from the following use cases to learn more:

*   I want to [customize headers of the Access Token request](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorization-grants.html#oauth2-client-client-credentials-access-token-request-headers)

*   I want to [customize parameters of the Access Token request](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorization-grants.html#oauth2-client-client-credentials-access-token-request-parameters)

*   I want to [customize the instance of `RestClient` that is used](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorization-grants.html#oauth2-client-client-credentials-access-token-response-rest-client)

*   I want to [customize parameters of the Access Token response](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorization-grants.html#oauth2-client-client-credentials-access-token-response-parameters)

*   I want to [customize error handling of the Access Token response](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorization-grants.html#oauth2-client-client-credentials-access-token-response-errors)

### [](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorization-grants.html#oauth2-client-client-credentials-access-token-request)Customizing the Access Token Request

`RestClientClientCredentialsTokenResponseClient` provides hooks for customizing HTTP headers and request parameters of the OAuth 2.0 Access Token Request.

There are two options for customizing HTTP headers:

*   Add additional headers by calling `addHeadersConverter()`

*   Fully customize headers by calling `setHeadersConverter()`

You can include additional headers without affecting the default headers added to every request using `addHeadersConverter()`. The following example adds a `User-Agent` header to the request when the `registrationId` is `spring`:

Include Additional HTTP Headers

*   Java

*   Kotlin

```
RestClientClientCredentialsTokenResponseClient accessTokenResponseClient =
	new RestClientClientCredentialsTokenResponseClient();
accessTokenResponseClient.addHeadersConverter(grantRequest -> {
	ClientRegistration clientRegistration = grantRequest.getClientRegistration();
	HttpHeaders headers = new HttpHeaders();
	if (clientRegistration.getRegistrationId().equals("spring")) {
		headers.set(HttpHeaders.USER_AGENT, "my-user-agent");
	}
	return headers;
});
```

You can fully customize headers by re-using `DefaultOAuth2TokenRequestHeadersConverter` or providing a custom implementation using `setHeadersConverter()`. The following example re-uses `DefaultOAuth2TokenRequestHeadersConverter` and disables `encodeClientCredentials` so that HTTP Basic credentials are no longer encoded with `application/x-www-form-urlencoded`:

Customize HTTP Headers

*   Java

*   Kotlin

```
DefaultOAuth2TokenRequestHeadersConverter headersConverter =
	new DefaultOAuth2TokenRequestHeadersConverter();
headersConverter.setEncodeClientCredentials(false);

RestClientClientCredentialsTokenResponseClient accessTokenResponseClient =
	new RestClientClientCredentialsTokenResponseClient();
accessTokenResponseClient.setHeadersConverter(headersConverter);
```

#### [](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorization-grants.html#oauth2-client-client-credentials-access-token-request-parameters)Customizing Request Parameters

There are three options for customizing request parameters:

*   Add additional parameters by calling `addParametersConverter()`

*   Override parameters by calling `setParametersConverter()`

*   Fully customize parameters by calling `setParametersCustomizer()`

Using `setParametersConverter()` does not fully customize parameters because it would require the user to provide all default parameters themselves. Default parameters are always provided, but can be fully customized or omitted by calling `setParametersCustomizer()`.

You can include additional parameters without affecting the default parameters added to every request using `addParametersConverter()`. The following example adds an `audience` parameter to the request when the `registrationId` is `keycloak`:

Include Additional Request Parameters

*   Java

*   Kotlin

```
RestClientClientCredentialsTokenResponseClient accessTokenResponseClient =
	new RestClientClientCredentialsTokenResponseClient();
accessTokenResponseClient.addParametersConverter(grantRequest -> {
	ClientRegistration clientRegistration = grantRequest.getClientRegistration();
	MultiValueMap<String, String> parameters = new LinkedMultiValueMap<String, String>();
	if (clientRegistration.getRegistrationId().equals("keycloak")) {
		parameters.set(OAuth2ParameterNames.AUDIENCE, "my-audience");
	}
	return parameters;
});
```

You can override default parameters using `setParametersConverter()`. The following example overrides the `client_id` parameter when the `registrationId` is `okta`:

Override Request Parameters

*   Java

*   Kotlin

```
RestClientClientCredentialsTokenResponseClient accessTokenResponseClient =
	new RestClientClientCredentialsTokenResponseClient();
accessTokenResponseClient.setParametersConverter(grantRequest -> {
	ClientRegistration clientRegistration = grantRequest.getClientRegistration();
	LinkedMultiValueMap<String, String> parameters = new LinkedMultiValueMap<>();
	if (clientRegistration.getRegistrationId().equals("okta")) {
		parameters.set(OAuth2ParameterNames.CLIENT_ID, "my-client");
	}
	return parameters;
});
```

You can fully customize parameters (including omitting default parameters) using `setParametersCustomizer()`. The following example omits the `client_id` parameter when the `client_assertion` parameter is present in the request:

Omit Request Parameters

*   Java

*   Kotlin

```
RestClientClientCredentialsTokenResponseClient accessTokenResponseClient =
	new RestClientClientCredentialsTokenResponseClient();
accessTokenResponseClient.setParametersCustomizer(parameters -> {
	if (parameters.containsKey(OAuth2ParameterNames.CLIENT_ASSERTION)) {
		parameters.remove(OAuth2ParameterNames.CLIENT_ID);
	}
});
```

### [](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorization-grants.html#oauth2-client-client-credentials-access-token-response)Customizing the Access Token Response

`RestClientClientCredentialsTokenResponseClient` provides hooks for customizing response parameters and error handling of the OAuth 2.0 Access Token Response.

#### [](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorization-grants.html#oauth2-client-client-credentials-access-token-response-rest-client)Customizing the `RestClient`

You can customize the Token Response by providing a pre-configured `RestClient` to `setRestClient()`. The default `RestClient` is configured as follows:

Default `RestClient` Configuration

*   Java

*   Kotlin

```
RestClient restClient = RestClient.builder()
	.messageConverters(messageConverters -> {
		messageConverters.clear();
		messageConverters.add(new FormHttpMessageConverter());
		messageConverters.add(new OAuth2AccessTokenResponseHttpMessageConverter());
	})
	.defaultStatusHandler(new OAuth2ErrorResponseErrorHandler())
	.build();

RestClientClientCredentialsTokenResponseClient accessTokenResponseClient =
	new RestClientClientCredentialsTokenResponseClient();
accessTokenResponseClient.setRestClient(restClient);
```

`OAuth2AccessTokenResponseHttpMessageConverter` is an `HttpMessageConverter` for an OAuth 2.0 Access Token Response. You can customize the conversion of Token Response parameters to an `OAuth2AccessTokenResponse` by calling `setAccessTokenResponseConverter()`. The default implementation is `DefaultMapOAuth2AccessTokenResponseConverter`.

`OAuth2ErrorResponseErrorHandler` is a `ResponseErrorHandler` that can handle an OAuth 2.0 Error, such as `400 Bad Request`. It uses an `OAuth2ErrorHttpMessageConverter` for converting the OAuth 2.0 Error parameters to an `OAuth2Error`. You can customize the conversion of Token Response parameters to an `OAuth2Error` by calling `setErrorConverter()`.

Spring MVC `FormHttpMessageConverter` is required, as it is used when sending the OAuth 2.0 Access Token Request.

#### [](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorization-grants.html#oauth2-client-client-credentials-access-token-response-parameters)Customizing Response Parameters

The following example provides a starting point for customizing the conversion of Token Response parameters to an `OAuth2AccessTokenResponse`:

Customize Access Token Response Converter

*   Java

*   Kotlin

```
OAuth2AccessTokenResponseHttpMessageConverter accessTokenResponseMessageConverter =
	new OAuth2AccessTokenResponseHttpMessageConverter();
accessTokenResponseMessageConverter.setAccessTokenResponseConverter(parameters -> {
	// ...
	return OAuth2AccessTokenResponse.withToken("custom-token")
		// ...
		.build();
});
```

#### [](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorization-grants.html#oauth2-client-client-credentials-access-token-response-errors)Customizing Error Handling

The following example provides a starting point for customizing the conversion of Error parameters to an `OAuth2Error`:

Customize Access Token Error Handler

*   Java

*   Kotlin

```
OAuth2ErrorHttpMessageConverter errorConverter =
	new OAuth2ErrorHttpMessageConverter();
errorConverter.setErrorConverter(parameters -> {
	// ...
	return new OAuth2Error("custom-error", "custom description", "custom-uri");
});

OAuth2ErrorResponseErrorHandler errorHandler =
	new OAuth2ErrorResponseErrorHandler();
errorHandler.setErrorConverter(errorConverter);
```

### [](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorization-grants.html#oauth2-client-client-credentials-authorized-client-provider-builder)Customize using the Builder

Whether you customize `RestClientClientCredentialsTokenResponseClient` or provide your own implementation of `OAuth2AccessTokenResponseClient`, you can configure it using the `OAuth2AuthorizedClientProviderBuilder` (as an alternative to [publishing a bean](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorization-grants.html#oauth2-client-client-credentials-access-token-response-client-bean)) as follows:

Access Token Response Configuration via Builder

*   Java

*   Kotlin

```
// Customize
OAuth2AccessTokenResponseClient<OAuth2ClientCredentialsGrantRequest> clientCredentialsTokenResponseClient = ...

OAuth2AuthorizedClientProvider authorizedClientProvider =
		OAuth2AuthorizedClientProviderBuilder.builder()
				.clientCredentials((configurer) -> configurer.accessTokenResponseClient(clientCredentialsTokenResponseClient))
				.build();

// ...

authorizedClientManager.setAuthorizedClientProvider(authorizedClientProvider);
```

`OAuth2AuthorizedClientProviderBuilder.builder().clientCredentials()` configures a `ClientCredentialsOAuth2AuthorizedClientProvider`, which is an implementation of an `OAuth2AuthorizedClientProvider` for the Client Credentials grant.

### [](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorization-grants.html#oauth2-client-client-credentials-authorized-client-manager)Using the Access Token

Consider the following Spring Boot properties for an OAuth 2.0 Client registration:

```
spring:
  security:
    oauth2:
      client:
        registration:
          okta:
            client-id: okta-client-id
            client-secret: okta-client-secret
            authorization-grant-type: client_credentials
            scope: read, write
        provider:
          okta:
            token-uri: https://dev-1234.oktapreview.com/oauth2/v1/token
```

Further consider the following `OAuth2AuthorizedClientManager``@Bean`:

*   Java

*   Kotlin

```
@Bean
public OAuth2AuthorizedClientManager authorizedClientManager(
		ClientRegistrationRepository clientRegistrationRepository,
		OAuth2AuthorizedClientRepository authorizedClientRepository) {

	OAuth2AuthorizedClientProvider authorizedClientProvider =
			OAuth2AuthorizedClientProviderBuilder.builder()
					.clientCredentials()
					.build();

	DefaultOAuth2AuthorizedClientManager authorizedClientManager =
			new DefaultOAuth2AuthorizedClientManager(
					clientRegistrationRepository, authorizedClientRepository);
	authorizedClientManager.setAuthorizedClientProvider(authorizedClientProvider);

	return authorizedClientManager;
}
```

Given the preceding properties and bean, you can obtain the `OAuth2AccessToken` as follows:

*   Java

*   Kotlin

```
@Controller
public class OAuth2ClientController {

	@Autowired
	private OAuth2AuthorizedClientManager authorizedClientManager;

	@GetMapping("/")
	public String index(Authentication authentication,
						HttpServletRequest servletRequest,
						HttpServletResponse servletResponse) {

		OAuth2AuthorizeRequest authorizeRequest = OAuth2AuthorizeRequest.withClientRegistrationId("okta")
				.principal(authentication)
				.attributes(attrs -> {
					attrs.put(HttpServletRequest.class.getName(), servletRequest);
					attrs.put(HttpServletResponse.class.getName(), servletResponse);
				})
				.build();
		OAuth2AuthorizedClient authorizedClient = this.authorizedClientManager.authorize(authorizeRequest);

		OAuth2AccessToken accessToken = authorizedClient.getAccessToken();

		// ...

		return "index";
	}
}
```

`HttpServletRequest` and `HttpServletResponse` are both OPTIONAL attributes. If not provided, they default to `ServletRequestAttributes` by using `RequestContextHolder.getRequestAttributes()`.

[](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorization-grants.html#oauth2-client-jwt-bearer)JWT Bearer
---------------------------------------------------------------------------------------------------------------------------------------

Please refer to JSON Web Token (JWT) Profile for OAuth 2.0 Client Authentication and Authorization Grants for further details on the [JWT Bearer](https://datatracker.ietf.org/doc/html/rfc7523) grant.

### [](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorization-grants.html#oauth2-client-jwt-bearer-access-token)Requesting an Access Token

The default implementation of `OAuth2AccessTokenResponseClient` for the JWT Bearer grant is `RestClientJwtBearerTokenResponseClient`, which uses a `RestClient` instance to obtain an access token at the Authorization Server’s Token Endpoint.

`RestClientJwtBearerTokenResponseClient` is very flexible and provides several options for customizing the OAuth 2.0 Access Token request and response for the JWT Bearer grant. Choose from the following use cases to learn more:

*   I want to [customize headers of the Access Token request](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorization-grants.html#oauth2-client-jwt-bearer-access-token-request-headers)

*   I want to [customize parameters of the Access Token request](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorization-grants.html#oauth2-client-jwt-bearer-access-token-request-parameters)

*   I want to [customize the instance of `RestClient` that is used](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorization-grants.html#oauth2-client-jwt-bearer-access-token-response-rest-client)

*   I want to [customize parameters of the Access Token response](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorization-grants.html#oauth2-client-jwt-bearer-access-token-response-parameters)

*   I want to [customize error handling of the Access Token response](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorization-grants.html#oauth2-client-jwt-bearer-access-token-response-errors)

### [](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorization-grants.html#oauth2-client-jwt-bearer-access-token-request)Customizing the Access Token Request

`RestClientJwtBearerTokenResponseClient` provides hooks for customizing HTTP headers and request parameters of the OAuth 2.0 Access Token Request.

There are two options for customizing HTTP headers:

*   Add additional headers by calling `addHeadersConverter()`

*   Fully customize headers by calling `setHeadersConverter()`

You can include additional headers without affecting the default headers added to every request using `addHeadersConverter()`. The following example adds a `User-Agent` header to the request when the `registrationId` is `spring`:

Include Additional HTTP Headers

*   Java

*   Kotlin

```
RestClientJwtBearerTokenResponseClient accessTokenResponseClient =
	new RestClientJwtBearerTokenResponseClient();
accessTokenResponseClient.addHeadersConverter(grantRequest -> {
	ClientRegistration clientRegistration = grantRequest.getClientRegistration();
	HttpHeaders headers = new HttpHeaders();
	if (clientRegistration.getRegistrationId().equals("spring")) {
		headers.set(HttpHeaders.USER_AGENT, "my-user-agent");
	}
	return headers;
});
```

You can fully customize headers by re-using `DefaultOAuth2TokenRequestHeadersConverter` or providing a custom implementation using `setHeadersConverter()`. The following example re-uses `DefaultOAuth2TokenRequestHeadersConverter` and disables `encodeClientCredentials` so that HTTP Basic credentials are no longer encoded with `application/x-www-form-urlencoded`:

Customize HTTP Headers

*   Java

*   Kotlin

```
DefaultOAuth2TokenRequestHeadersConverter headersConverter =
	new DefaultOAuth2TokenRequestHeadersConverter();
headersConverter.setEncodeClientCredentials(false);

RestClientJwtBearerTokenResponseClient accessTokenResponseClient =
	new RestClientJwtBearerTokenResponseClient();
accessTokenResponseClient.setHeadersConverter(headersConverter);
```

#### [](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorization-grants.html#oauth2-client-jwt-bearer-access-token-request-parameters)Customizing Request Parameters

There are three options for customizing request parameters:

*   Add additional parameters by calling `addParametersConverter()`

*   Override parameters by calling `setParametersConverter()`

*   Fully customize parameters by calling `setParametersCustomizer()`

Using `setParametersConverter()` does not fully customize parameters because it would require the user to provide all default parameters themselves. Default parameters are always provided, but can be fully customized or omitted by calling `setParametersCustomizer()`.

You can include additional parameters without affecting the default parameters added to every request using `addParametersConverter()`. The following example adds an `audience` parameter to the request when the `registrationId` is `keycloak`:

Include Additional Request Parameters

*   Java

*   Kotlin

```
RestClientJwtBearerTokenResponseClient accessTokenResponseClient =
	new RestClientJwtBearerTokenResponseClient();
accessTokenResponseClient.addParametersConverter(grantRequest -> {
	ClientRegistration clientRegistration = grantRequest.getClientRegistration();
	MultiValueMap<String, String> parameters = new LinkedMultiValueMap<String, String>();
	if (clientRegistration.getRegistrationId().equals("keycloak")) {
		parameters.set(OAuth2ParameterNames.AUDIENCE, "my-audience");
	}
	return parameters;
});
```

You can override default parameters using `setParametersConverter()`. The following example overrides the `client_id` parameter when the `registrationId` is `okta`:

Override Request Parameters

*   Java

*   Kotlin

```
RestClientJwtBearerTokenResponseClient accessTokenResponseClient =
	new RestClientJwtBearerTokenResponseClient();
accessTokenResponseClient.setParametersConverter(grantRequest -> {
	ClientRegistration clientRegistration = grantRequest.getClientRegistration();
	LinkedMultiValueMap<String, String> parameters = new LinkedMultiValueMap<>();
	if (clientRegistration.getRegistrationId().equals("okta")) {
		parameters.set(OAuth2ParameterNames.CLIENT_ID, "my-client");
	}
	return parameters;
});
```

You can fully customize parameters (including omitting default parameters) using `setParametersCustomizer()`. The following example omits the `client_id` parameter when the `client_assertion` parameter is present in the request:

Omit Request Parameters

*   Java

*   Kotlin

```
RestClientJwtBearerTokenResponseClient accessTokenResponseClient =
	new RestClientJwtBearerTokenResponseClient();
accessTokenResponseClient.setParametersCustomizer(parameters -> {
	if (parameters.containsKey(OAuth2ParameterNames.CLIENT_ASSERTION)) {
		parameters.remove(OAuth2ParameterNames.CLIENT_ID);
	}
});
```

### [](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorization-grants.html#oauth2-client-jwt-bearer-access-token-response)Customizing the Access Token Response

`RestClientJwtBearerTokenResponseClient` provides hooks for customizing response parameters and error handling of the OAuth 2.0 Access Token Response.

#### [](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorization-grants.html#oauth2-client-jwt-bearer-access-token-response-rest-client)Customizing the `RestClient`

You can customize the Token Response by providing a pre-configured `RestClient` to `setRestClient()`. The default `RestClient` is configured as follows:

Default `RestClient` Configuration

*   Java

*   Kotlin

```
RestClient restClient = RestClient.builder()
	.messageConverters(messageConverters -> {
		messageConverters.clear();
		messageConverters.add(new FormHttpMessageConverter());
		messageConverters.add(new OAuth2AccessTokenResponseHttpMessageConverter());
	})
	.defaultStatusHandler(new OAuth2ErrorResponseErrorHandler())
	.build();

RestClientJwtBearerTokenResponseClient accessTokenResponseClient =
	new RestClientJwtBearerTokenResponseClient();
accessTokenResponseClient.setRestClient(restClient);
```

`OAuth2AccessTokenResponseHttpMessageConverter` is an `HttpMessageConverter` for an OAuth 2.0 Access Token Response. You can customize the conversion of Token Response parameters to an `OAuth2AccessTokenResponse` by calling `setAccessTokenResponseConverter()`. The default implementation is `DefaultMapOAuth2AccessTokenResponseConverter`.

`OAuth2ErrorResponseErrorHandler` is a `ResponseErrorHandler` that can handle an OAuth 2.0 Error, such as `400 Bad Request`. It uses an `OAuth2ErrorHttpMessageConverter` for converting the OAuth 2.0 Error parameters to an `OAuth2Error`. You can customize the conversion of Token Response parameters to an `OAuth2Error` by calling `setErrorConverter()`.

Spring MVC `FormHttpMessageConverter` is required, as it is used when sending the OAuth 2.0 Access Token Request.

#### [](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorization-grants.html#oauth2-client-jwt-bearer-access-token-response-parameters)Customizing Response Parameters

The following example provides a starting point for customizing the conversion of Token Response parameters to an `OAuth2AccessTokenResponse`:

Customize Access Token Response Converter

*   Java

*   Kotlin

```
OAuth2AccessTokenResponseHttpMessageConverter accessTokenResponseMessageConverter =
	new OAuth2AccessTokenResponseHttpMessageConverter();
accessTokenResponseMessageConverter.setAccessTokenResponseConverter(parameters -> {
	// ...
	return OAuth2AccessTokenResponse.withToken("custom-token")
		// ...
		.build();
});
```

#### [](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorization-grants.html#oauth2-client-jwt-bearer-access-token-response-errors)Customizing Error Handling

The following example provides a starting point for customizing the conversion of Error parameters to an `OAuth2Error`:

Customize Access Token Error Handler

*   Java

*   Kotlin

```
OAuth2ErrorHttpMessageConverter errorConverter =
	new OAuth2ErrorHttpMessageConverter();
errorConverter.setErrorConverter(parameters -> {
	// ...
	return new OAuth2Error("custom-error", "custom description", "custom-uri");
});

OAuth2ErrorResponseErrorHandler errorHandler =
	new OAuth2ErrorResponseErrorHandler();
errorHandler.setErrorConverter(errorConverter);
```

### [](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorization-grants.html#oauth2-client-jwt-bearer-authorized-client-provider-builder)Customize using the Builder

Whether you customize `RestClientJwtBearerTokenResponseClient` or provide your own implementation of `OAuth2AccessTokenResponseClient`, you can configure it using the `OAuth2AuthorizedClientProviderBuilder` (as an alternative to [publishing a bean](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorization-grants.html#oauth2-client-jwt-bearer-access-token-response-client-bean)) as follows:

Access Token Response Configuration via Builder

*   Java

*   Kotlin

```
// Customize
OAuth2AccessTokenResponseClient<JwtBearerGrantRequest> jwtBearerTokenResponseClient = ...

JwtBearerOAuth2AuthorizedClientProvider jwtBearerAuthorizedClientProvider = new JwtBearerOAuth2AuthorizedClientProvider();
jwtBearerAuthorizedClientProvider.setAccessTokenResponseClient(jwtBearerTokenResponseClient);

OAuth2AuthorizedClientProvider authorizedClientProvider =
		OAuth2AuthorizedClientProviderBuilder.builder()
				.provider(jwtBearerAuthorizedClientProvider)
				.build();

// ...

authorizedClientManager.setAuthorizedClientProvider(authorizedClientProvider);
```

### [](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorization-grants.html#oauth2-client-jwt-bearer-authorized-client-manager)Using the Access Token

Given the following Spring Boot properties for an OAuth 2.0 Client registration:

```
spring:
  security:
    oauth2:
      client:
        registration:
          okta:
            client-id: okta-client-id
            client-secret: okta-client-secret
            authorization-grant-type: urn:ietf:params:oauth:grant-type:jwt-bearer
            scope: read
        provider:
          okta:
            token-uri: https://dev-1234.oktapreview.com/oauth2/v1/token
```

…​and the `OAuth2AuthorizedClientManager``@Bean`:

*   Java

*   Kotlin

```
@Bean
public OAuth2AuthorizedClientManager authorizedClientManager(
		ClientRegistrationRepository clientRegistrationRepository,
		OAuth2AuthorizedClientRepository authorizedClientRepository) {

	JwtBearerOAuth2AuthorizedClientProvider jwtBearerAuthorizedClientProvider =
			new JwtBearerOAuth2AuthorizedClientProvider();

	OAuth2AuthorizedClientProvider authorizedClientProvider =
			OAuth2AuthorizedClientProviderBuilder.builder()
					.provider(jwtBearerAuthorizedClientProvider)
					.build();

	DefaultOAuth2AuthorizedClientManager authorizedClientManager =
			new DefaultOAuth2AuthorizedClientManager(
					clientRegistrationRepository, authorizedClientRepository);
	authorizedClientManager.setAuthorizedClientProvider(authorizedClientProvider);

	return authorizedClientManager;
}
```

You may obtain the `OAuth2AccessToken` as follows:

*   Java

*   Kotlin

```
@RestController
public class OAuth2ResourceServerController {

	@Autowired
	private OAuth2AuthorizedClientManager authorizedClientManager;

	@GetMapping("/resource")
	public String resource(JwtAuthenticationToken jwtAuthentication) {
		OAuth2AuthorizeRequest authorizeRequest = OAuth2AuthorizeRequest.withClientRegistrationId("okta")
				.principal(jwtAuthentication)
				.build();
		OAuth2AuthorizedClient authorizedClient = this.authorizedClientManager.authorize(authorizeRequest);
		OAuth2AccessToken accessToken = authorizedClient.getAccessToken();

		// ...

	}
}
```

`JwtBearerOAuth2AuthorizedClientProvider` resolves the `Jwt` assertion via `OAuth2AuthorizationContext.getPrincipal().getPrincipal()` by default, hence the use of `JwtAuthenticationToken` in the preceding example.

If you need to resolve the `Jwt` assertion from a different source, you can provide `JwtBearerOAuth2AuthorizedClientProvider.setJwtAssertionResolver()` with a custom `Function<OAuth2AuthorizationContext, Jwt>`.

[](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorization-grants.html#oauth2-client-token-exchange)[](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorization-grants.html)Token Exchange
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Please refer to OAuth 2.0 Token Exchange for further details on the [Token Exchange](https://datatracker.ietf.org/doc/html/rfc8693) grant.

### [](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorization-grants.html#oauth2-client-token-exchange-access-token)Requesting an Access Token

The default implementation of `OAuth2AccessTokenResponseClient` for the Token Exchange grant is `RestClientTokenExchangeTokenResponseClient`, which uses a `RestClient` instance to obtain an access token at the Authorization Server’s Token Endpoint.

`RestClientTokenExchangeTokenResponseClient` is very flexible and provides several options for customizing the OAuth 2.0 Access Token request and response for the Token Exchange grant. Choose from the following use cases to learn more:

*   I want to [customize headers of the Access Token request](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorization-grants.html#oauth2-client-token-exchange-access-token-request-headers)

*   I want to [customize parameters of the Access Token request](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorization-grants.html#oauth2-client-token-exchange-access-token-request-parameters)

*   I want to [customize the instance of `RestClient` that is used](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorization-grants.html#oauth2-client-token-exchange-access-token-response-rest-client)

*   I want to [customize parameters of the Access Token response](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorization-grants.html#oauth2-client-token-exchange-access-token-response-parameters)

*   I want to [customize error handling of the Access Token response](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorization-grants.html#oauth2-client-token-exchange-access-token-response-errors)

### [](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorization-grants.html#oauth2-client-token-exchange-access-token-request)Customizing the Access Token Request

`RestClientTokenExchangeTokenResponseClient` provides hooks for customizing HTTP headers and request parameters of the OAuth 2.0 Access Token Request.

There are two options for customizing HTTP headers:

*   Add additional headers by calling `addHeadersConverter()`

*   Fully customize headers by calling `setHeadersConverter()`

You can include additional headers without affecting the default headers added to every request using `addHeadersConverter()`. The following example adds a `User-Agent` header to the request when the `registrationId` is `spring`:

Include Additional HTTP Headers

*   Java

*   Kotlin

```
RestClientTokenExchangeTokenResponseClient accessTokenResponseClient =
	new RestClientTokenExchangeTokenResponseClient();
accessTokenResponseClient.addHeadersConverter(grantRequest -> {
	ClientRegistration clientRegistration = grantRequest.getClientRegistration();
	HttpHeaders headers = new HttpHeaders();
	if (clientRegistration.getRegistrationId().equals("spring")) {
		headers.set(HttpHeaders.USER_AGENT, "my-user-agent");
	}
	return headers;
});
```

You can fully customize headers by re-using `DefaultOAuth2TokenRequestHeadersConverter` or providing a custom implementation using `setHeadersConverter()`. The following example re-uses `DefaultOAuth2TokenRequestHeadersConverter` and disables `encodeClientCredentials` so that HTTP Basic credentials are no longer encoded with `application/x-www-form-urlencoded`:

Customize HTTP Headers

*   Java

*   Kotlin

```
DefaultOAuth2TokenRequestHeadersConverter headersConverter =
	new DefaultOAuth2TokenRequestHeadersConverter();
headersConverter.setEncodeClientCredentials(false);

RestClientTokenExchangeTokenResponseClient accessTokenResponseClient =
	new RestClientTokenExchangeTokenResponseClient();
accessTokenResponseClient.setHeadersConverter(headersConverter);
```

#### [](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorization-grants.html#oauth2-client-token-exchange-access-token-request-parameters)Customizing Request Parameters

There are three options for customizing request parameters:

*   Add additional parameters by calling `addParametersConverter()`

*   Override parameters by calling `setParametersConverter()`

*   Fully customize parameters by calling `setParametersCustomizer()`

Using `setParametersConverter()` does not fully customize parameters because it would require the user to provide all default parameters themselves. Default parameters are always provided, but can be fully customized or omitted by calling `setParametersCustomizer()`.

You can include additional parameters without affecting the default parameters added to every request using `addParametersConverter()`. The following example adds an `audience` parameter to the request when the `registrationId` is `keycloak`:

Include Additional Request Parameters

*   Java

*   Kotlin

```
RestClientTokenExchangeTokenResponseClient accessTokenResponseClient =
	new RestClientTokenExchangeTokenResponseClient();
accessTokenResponseClient.addParametersConverter(grantRequest -> {
	ClientRegistration clientRegistration = grantRequest.getClientRegistration();
	MultiValueMap<String, String> parameters = new LinkedMultiValueMap<String, String>();
	if (clientRegistration.getRegistrationId().equals("keycloak")) {
		parameters.set(OAuth2ParameterNames.AUDIENCE, "my-audience");
	}
	return parameters;
});
```

You can override default parameters using `setParametersConverter()`. The following example overrides the `client_id` parameter when the `registrationId` is `okta`:

Override Request Parameters

*   Java

*   Kotlin

```
RestClientTokenExchangeTokenResponseClient accessTokenResponseClient =
	new RestClientTokenExchangeTokenResponseClient();
accessTokenResponseClient.setParametersConverter(grantRequest -> {
	ClientRegistration clientRegistration = grantRequest.getClientRegistration();
	LinkedMultiValueMap<String, String> parameters = new LinkedMultiValueMap<>();
	if (clientRegistration.getRegistrationId().equals("okta")) {
		parameters.set(OAuth2ParameterNames.CLIENT_ID, "my-client");
	}
	return parameters;
});
```

You can fully customize parameters (including omitting default parameters) using `setParametersCustomizer()`. The following example omits the `client_id` parameter when the `client_assertion` parameter is present in the request:

Omit Request Parameters

*   Java

*   Kotlin

```
RestClientTokenExchangeTokenResponseClient accessTokenResponseClient =
	new RestClientTokenExchangeTokenResponseClient();
accessTokenResponseClient.setParametersCustomizer(parameters -> {
	if (parameters.containsKey(OAuth2ParameterNames.CLIENT_ASSERTION)) {
		parameters.remove(OAuth2ParameterNames.CLIENT_ID);
	}
});
```

### [](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorization-grants.html#oauth2-client-token-exchange-access-token-response)Customizing the Access Token Response

`RestClientTokenExchangeTokenResponseClient` provides hooks for customizing response parameters and error handling of the OAuth 2.0 Access Token Response.

#### [](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorization-grants.html#oauth2-client-token-exchange-access-token-response-rest-client)Customizing the `RestClient`

You can customize the Token Response by providing a pre-configured `RestClient` to `setRestClient()`. The default `RestClient` is configured as follows:

Default `RestClient` Configuration

*   Java

*   Kotlin

```
RestClient restClient = RestClient.builder()
	.messageConverters(messageConverters -> {
		messageConverters.clear();
		messageConverters.add(new FormHttpMessageConverter());
		messageConverters.add(new OAuth2AccessTokenResponseHttpMessageConverter());
	})
	.defaultStatusHandler(new OAuth2ErrorResponseErrorHandler())
	.build();

RestClientTokenExchangeTokenResponseClient accessTokenResponseClient =
	new RestClientTokenExchangeTokenResponseClient();
accessTokenResponseClient.setRestClient(restClient);
```

`OAuth2AccessTokenResponseHttpMessageConverter` is an `HttpMessageConverter` for an OAuth 2.0 Access Token Response. You can customize the conversion of Token Response parameters to an `OAuth2AccessTokenResponse` by calling `setAccessTokenResponseConverter()`. The default implementation is `DefaultMapOAuth2AccessTokenResponseConverter`.

`OAuth2ErrorResponseErrorHandler` is a `ResponseErrorHandler` that can handle an OAuth 2.0 Error, such as `400 Bad Request`. It uses an `OAuth2ErrorHttpMessageConverter` for converting the OAuth 2.0 Error parameters to an `OAuth2Error`. You can customize the conversion of Token Response parameters to an `OAuth2Error` by calling `setErrorConverter()`.

Spring MVC `FormHttpMessageConverter` is required, as it is used when sending the OAuth 2.0 Access Token Request.

#### [](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorization-grants.html#oauth2-client-token-exchange-access-token-response-parameters)Customizing Response Parameters

The following example provides a starting point for customizing the conversion of Token Response parameters to an `OAuth2AccessTokenResponse`:

Customize Access Token Response Converter

*   Java

*   Kotlin

```
OAuth2AccessTokenResponseHttpMessageConverter accessTokenResponseMessageConverter =
	new OAuth2AccessTokenResponseHttpMessageConverter();
accessTokenResponseMessageConverter.setAccessTokenResponseConverter(parameters -> {
	// ...
	return OAuth2AccessTokenResponse.withToken("custom-token")
		// ...
		.build();
});
```

#### [](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorization-grants.html#oauth2-client-token-exchange-access-token-response-errors)Customizing Error Handling

The following example provides a starting point for customizing the conversion of Error parameters to an `OAuth2Error`:

Customize Access Token Error Handler

*   Java

*   Kotlin

```
OAuth2ErrorHttpMessageConverter errorConverter =
	new OAuth2ErrorHttpMessageConverter();
errorConverter.setErrorConverter(parameters -> {
	// ...
	return new OAuth2Error("custom-error", "custom description", "custom-uri");
});

OAuth2ErrorResponseErrorHandler errorHandler =
	new OAuth2ErrorResponseErrorHandler();
errorHandler.setErrorConverter(errorConverter);
```

### [](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorization-grants.html#oauth2-client-token-exchange-authorized-client-provider-builder)Customize using the Builder

Whether you customize `RestClientTokenExchangeTokenResponseClient` or provide your own implementation of `OAuth2AccessTokenResponseClient`, you can configure it using the `OAuth2AuthorizedClientProviderBuilder` (as an alternative to [publishing a bean](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorization-grants.html#oauth2-client-token-exchange-access-token-response-client-bean)) as follows:

Access Token Response Configuration via Builder

*   Java

*   Kotlin

```
// Customize
OAuth2AccessTokenResponseClient<TokenExchangeGrantRequest> tokenExchangeTokenResponseClient = ...

TokenExchangeOAuth2AuthorizedClientProvider tokenExchangeAuthorizedClientProvider = new TokenExchangeOAuth2AuthorizedClientProvider();
tokenExchangeAuthorizedClientProvider.setAccessTokenResponseClient(tokenExchangeTokenResponseClient);

OAuth2AuthorizedClientProvider authorizedClientProvider =
		OAuth2AuthorizedClientProviderBuilder.builder()
				.provider(tokenExchangeAuthorizedClientProvider)
				.build();

// ...

authorizedClientManager.setAuthorizedClientProvider(authorizedClientProvider);
```

### [](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorization-grants.html#oauth2-client-token-exchange-authorized-client-manager)[](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorization-grants.html)Using the Access Token

Given the following Spring Boot properties for an OAuth 2.0 Client registration:

```
spring:
  security:
    oauth2:
      client:
        registration:
          okta:
            client-id: okta-client-id
            client-secret: okta-client-secret
            authorization-grant-type: urn:ietf:params:oauth:grant-type:token-exchange
            scope: read
        provider:
          okta:
            token-uri: https://dev-1234.oktapreview.com/oauth2/v1/token
```

…​and the `OAuth2AuthorizedClientManager``@Bean`:

*   Java

*   Kotlin

```
@Bean
public OAuth2AuthorizedClientManager authorizedClientManager(
		ClientRegistrationRepository clientRegistrationRepository,
		OAuth2AuthorizedClientRepository authorizedClientRepository) {

	TokenExchangeOAuth2AuthorizedClientProvider tokenExchangeAuthorizedClientProvider =
			new TokenExchangeOAuth2AuthorizedClientProvider();

	OAuth2AuthorizedClientProvider authorizedClientProvider =
			OAuth2AuthorizedClientProviderBuilder.builder()
					.provider(tokenExchangeAuthorizedClientProvider)
					.build();

	DefaultOAuth2AuthorizedClientManager authorizedClientManager =
			new DefaultOAuth2AuthorizedClientManager(
					clientRegistrationRepository, authorizedClientRepository);
	authorizedClientManager.setAuthorizedClientProvider(authorizedClientProvider);

	return authorizedClientManager;
}
```

You may obtain the `OAuth2AccessToken` as follows:

*   Java

*   Kotlin

```
@RestController
public class OAuth2ResourceServerController {

	@Autowired
	private OAuth2AuthorizedClientManager authorizedClientManager;

	@GetMapping("/resource")
	public String resource(JwtAuthenticationToken jwtAuthentication) {
		OAuth2AuthorizeRequest authorizeRequest = OAuth2AuthorizeRequest.withClientRegistrationId("okta")
				.principal(jwtAuthentication)
				.build();
		OAuth2AuthorizedClient authorizedClient = this.authorizedClientManager.authorize(authorizeRequest);
		OAuth2AccessToken accessToken = authorizedClient.getAccessToken();

		// ...

	}
}
```

`TokenExchangeOAuth2AuthorizedClientProvider` resolves the subject token (as an `OAuth2Token`) via `OAuth2AuthorizationContext.getPrincipal().getPrincipal()` by default, hence the use of `JwtAuthenticationToken` in the preceding example. An actor token is not resolved by default.

If you need to resolve the subject token from a different source, you can provide `TokenExchangeOAuth2AuthorizedClientProvider.setSubjectTokenResolver()` with a custom `Function<OAuth2AuthorizationContext, OAuth2Token>`.

If you need to resolve an actor token, you can provide `TokenExchangeOAuth2AuthorizedClientProvider.setActorTokenResolver()` with a custom `Function<OAuth2AuthorizationContext, OAuth2Token>`.
