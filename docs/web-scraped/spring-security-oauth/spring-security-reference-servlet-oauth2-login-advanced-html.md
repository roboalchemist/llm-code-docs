# Source: https://docs.spring.io/spring-security/reference/servlet/oauth2/login/advanced.html

Title: Advanced Configuration :: Spring Security

URL Source: https://docs.spring.io/spring-security/reference/servlet/oauth2/login/advanced.html

Markdown Content:
`HttpSecurity.oauth2Login()` provides a number of configuration options for customizing OAuth 2.0 Login. The main configuration options are grouped into their protocol endpoint counterparts.

For example, `oauth2Login().authorizationEndpoint()` allows configuring the _Authorization Endpoint_, whereas `oauth2Login().tokenEndpoint()` allows configuring the _Token Endpoint_.

The following code shows an example:

Advanced OAuth2 Login Configuration

*   Java

*   Kotlin

```
@Configuration
@EnableWebSecurity
public class OAuth2LoginSecurityConfig {

	@Bean
	public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
		http
			.oauth2Login((oauth2) -> oauth2
			    .authorizationEndpoint((authorization) -> authorization
			            ...
			    )
			    .redirectionEndpoint((redirection) -> redirection
			            ...
			    )
			    .tokenEndpoint((token) -> token
			            ...
			    )
			    .userInfoEndpoint((userInfo) -> userInfo
			            ...
			    )
			);
		return http.build();
	}
}
```

The main goal of the `oauth2Login()` DSL was to closely align with the naming, as defined in the specifications.

The OAuth 2.0 Authorization Framework defines the [Protocol Endpoints](https://tools.ietf.org/html/rfc6749#section-3) as follows:

The authorization process uses two authorization server endpoints (HTTP resources):

*   Authorization Endpoint: Used by the client to obtain authorization from the resource owner through user-agent redirection.

*   Token Endpoint: Used by the client to exchange an authorization grant for an access token, typically with client authentication.

The authorization process also uses one client endpoint:

*   Redirection Endpoint: Used by the authorization server to return responses that contain authorization credentials to the client through the resource owner user-agent.

The OpenID Connect Core 1.0 specification defines the [UserInfo Endpoint](https://openid.net/specs/openid-connect-core-1_0.html#UserInfo) as follows:

The UserInfo Endpoint is an OAuth 2.0 Protected Resource that returns claims about the authenticated end-user. To obtain the requested claims about the end-user, the client makes a request to the UserInfo Endpoint by using an access token obtained through OpenID Connect Authentication. These claims are normally represented by a JSON object that contains a collection of name-value pairs for the claims.

The following code shows the complete configuration options available for the `oauth2Login()` DSL:

OAuth2 Login Configuration Options

*   Java

*   Kotlin

```
@Configuration
@EnableWebSecurity
public class OAuth2LoginSecurityConfig {

	@Bean
	public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
		http
			.oauth2Login((oauth2) -> oauth2
			    .clientRegistrationRepository(this.clientRegistrationRepository())
			    .authorizedClientRepository(this.authorizedClientRepository())
			    .authorizedClientService(this.authorizedClientService())
			    .loginPage("/login")
			    .authorizationEndpoint((authorization) -> authorization
			        .baseUri(this.authorizationRequestBaseUri())
			        .authorizationRequestRepository(this.authorizationRequestRepository())
			        .authorizationRequestResolver(this.authorizationRequestResolver())
			    )
			    .redirectionEndpoint((redirection) -> redirection
			        .baseUri(this.authorizationResponseBaseUri())
			    )
			    .tokenEndpoint((token) -> token
			        .accessTokenResponseClient(this.accessTokenResponseClient())
			    )
			    .userInfoEndpoint((userInfo) -> userInfo
			        .userAuthoritiesMapper(this.userAuthoritiesMapper())
			        .userService(this.oauth2UserService())
			        .oidcUserService(this.oidcUserService())
			    )
			);
		return http.build();
	}
}
```

In addition to the `oauth2Login()` DSL, XML configuration is also supported.

The following code shows the complete configuration options available in the [security namespace](https://docs.spring.io/spring-security/reference/servlet/appendix/namespace/http.html#nsa-oauth2-login):

OAuth2 Login XML Configuration Options

```
<http>
	<oauth2-login client-registration-repository-ref="clientRegistrationRepository"
				  authorized-client-repository-ref="authorizedClientRepository"
				  authorized-client-service-ref="authorizedClientService"
				  authorization-request-repository-ref="authorizationRequestRepository"
				  authorization-request-resolver-ref="authorizationRequestResolver"
				  access-token-response-client-ref="accessTokenResponseClient"
				  user-authorities-mapper-ref="userAuthoritiesMapper"
				  user-service-ref="oauth2UserService"
				  oidc-user-service-ref="oidcUserService"
				  login-processing-url="/login/oauth2/code/*"
				  login-page="/login"
				  authentication-success-handler-ref="authenticationSuccessHandler"
				  authentication-failure-handler-ref="authenticationFailureHandler"
				  jwt-decoder-factory-ref="jwtDecoderFactory"/>
</http>
```

The following sections go into more detail on each of the configuration options available:

*   [OAuth 2.0 Login Page](https://docs.spring.io/spring-security/reference/servlet/oauth2/login/advanced.html#oauth2login-advanced-login-page)

*   [Redirection Endpoint](https://docs.spring.io/spring-security/reference/servlet/oauth2/login/advanced.html#oauth2login-advanced-redirection-endpoint)

*   [UserInfo Endpoint](https://docs.spring.io/spring-security/reference/servlet/oauth2/login/advanced.html#oauth2login-advanced-userinfo-endpoint)

*   [ID Token Signature Verification](https://docs.spring.io/spring-security/reference/servlet/oauth2/login/advanced.html#oauth2login-advanced-idtoken-verify)

*   [[oauth2login-advanced-oidc-logout]](https://docs.spring.io/spring-security/reference/servlet/oauth2/login/advanced.html#oauth2login-advanced-oidc-logout)

[](https://docs.spring.io/spring-security/reference/servlet/oauth2/login/advanced.html#oauth2login-advanced-login-page)OAuth 2.0 Login Page
-------------------------------------------------------------------------------------------------------------------------------------------

By default, the OAuth 2.0 Login Page is auto-generated by the `DefaultLoginPageGeneratingFilter`. The default login page shows each configured OAuth Client with its `ClientRegistration.clientName` as a link, which is capable of initiating the Authorization Request (or OAuth 2.0 Login).

For `DefaultLoginPageGeneratingFilter` to show links for configured OAuth Clients, the registered `ClientRegistrationRepository` needs to also implement `Iterable<ClientRegistration>`. See `InMemoryClientRegistrationRepository` for reference.

The link’s destination for each OAuth Client defaults to the following:

`OAuth2AuthorizationRequestRedirectFilter.DEFAULT_AUTHORIZATION_REQUEST_BASE_URI + "/{registrationId}"`

The following line shows an example:

`<a href="/oauth2/authorization/google">Google</a>`

To override the default login page, configure `oauth2Login().loginPage()` and (optionally) `oauth2Login().authorizationEndpoint().baseUri()`.

The following listing shows an example:

OAuth2 Login Page Configuration

*   Java

*   Kotlin

*   Xml

```
@Configuration
@EnableWebSecurity
public class OAuth2LoginSecurityConfig {

	@Bean
	public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
		http
			.oauth2Login((oauth2) -> oauth2
			    .loginPage("/login/oauth2")
			    ...
			    .authorizationEndpoint((authorization) -> authorization
			        .baseUri("/login/oauth2/authorization")
			        ...
			    )
			);
		return http.build();
	}
}
```

You need to provide a `@Controller` with a `@RequestMapping("/login/oauth2")` that is capable of rendering the custom login page.

As noted earlier, configuring `oauth2Login().authorizationEndpoint().baseUri()` is optional. However, if you choose to customize it, ensure the link to each OAuth Client matches the `authorizationEndpoint().baseUri()`.

The following line shows an example:

`<a href="/login/oauth2/authorization/google">Google</a>`

[](https://docs.spring.io/spring-security/reference/servlet/oauth2/login/advanced.html#oauth2login-advanced-redirection-endpoint)Redirection Endpoint
-----------------------------------------------------------------------------------------------------------------------------------------------------

The Redirection Endpoint is used by the Authorization Server for returning the Authorization Response (which contains the authorization credentials) to the client through the Resource Owner user-agent.

OAuth 2.0 Login leverages the Authorization Code Grant. Therefore, the authorization credential is the authorization code.

The default Authorization Response `baseUri` (redirection endpoint) is `/login/oauth2/code/*`, which is defined in `OAuth2LoginAuthenticationFilter.DEFAULT_FILTER_PROCESSES_URI`.

If you would like to customize the Authorization Response `baseUri`, configure it as follows:

Redirection Endpoint Configuration

*   Java

*   Kotlin

*   Xml

```
@Configuration
@EnableWebSecurity
public class OAuth2LoginSecurityConfig {

    @Bean
	public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
		http
			.oauth2Login((oauth2) -> oauth2
			    .redirectionEndpoint((redirection) -> redirection
			        .baseUri("/login/oauth2/callback/*")
			        ...
			    )
			);
		return http.build();
	}
}
```

You also need to ensure the `ClientRegistration.redirectUri` matches the custom Authorization Response `baseUri`.

The following listing shows an example:

*   Java

*   Kotlin

```
return CommonOAuth2Provider.GOOGLE.getBuilder("google")
	.clientId("google-client-id")
	.clientSecret("google-client-secret")
	.redirectUri("{baseUrl}/login/oauth2/callback/{registrationId}")
	.build();
```

[](https://docs.spring.io/spring-security/reference/servlet/oauth2/login/advanced.html#oauth2login-advanced-userinfo-endpoint)UserInfo Endpoint
-----------------------------------------------------------------------------------------------------------------------------------------------

The UserInfo Endpoint includes a number of configuration options, as described in the following sub-sections:

*   [Mapping User Authorities](https://docs.spring.io/spring-security/reference/servlet/oauth2/login/advanced.html#oauth2login-advanced-map-authorities)

*   [OAuth 2.0 UserService](https://docs.spring.io/spring-security/reference/servlet/oauth2/login/advanced.html#oauth2login-advanced-oauth2-user-service)

*   [OpenID Connect 1.0 UserService](https://docs.spring.io/spring-security/reference/servlet/oauth2/login/advanced.html#oauth2login-advanced-oidc-user-service)

After the user successfully authenticates with the OAuth 2.0 Provider, the `OAuth2User.getAuthorities()` (or `OidcUser.getAuthorities()`) contains a list of granted authorities populated from `OAuth2UserRequest.getAccessToken().getScopes()` and prefixed with `SCOPE_`. These granted authorities can be mapped to a new set of `GrantedAuthority` instances, which are supplied to `OAuth2AuthenticationToken` when completing the authentication.

`OAuth2AuthenticationToken.getAuthorities()` is used for authorizing requests, such as in `hasRole('USER')` or `hasRole('ADMIN')`.

There are a couple of options to choose from when mapping user authorities:

*   [Using a GrantedAuthoritiesMapper](https://docs.spring.io/spring-security/reference/servlet/oauth2/login/advanced.html#oauth2login-advanced-map-authorities-grantedauthoritiesmapper)

*   [Delegation-based Strategy with OAuth2UserService](https://docs.spring.io/spring-security/reference/servlet/oauth2/login/advanced.html#oauth2login-advanced-map-authorities-oauth2userservice)

#### [](https://docs.spring.io/spring-security/reference/servlet/oauth2/login/advanced.html#oauth2login-advanced-map-authorities-grantedauthoritiesmapper)Using a GrantedAuthoritiesMapper

The `GrantedAuthoritiesMapper` is given a list of granted authorities which contains a special authority of type `OAuth2UserAuthority` and the authority string `OAUTH2_USER` (or `OidcUserAuthority` and the authority string `OIDC_USER`).

Provide an implementation of `GrantedAuthoritiesMapper` and configure it, as follows:

Granted Authorities Mapper Configuration

*   Java

*   Kotlin

*   Xml

```
@Configuration
@EnableWebSecurity
public class OAuth2LoginSecurityConfig {

    @Bean
	public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
		http
			.oauth2Login((oauth2) -> oauth2
			    .userInfoEndpoint((userInfo) -> userInfo
			        .userAuthoritiesMapper(this.userAuthoritiesMapper())
			        ...
			    )
			);
		return http.build();
	}

	private GrantedAuthoritiesMapper userAuthoritiesMapper() {
		return (authorities) -> {
			Set<GrantedAuthority> mappedAuthorities = new HashSet<>();

			authorities.forEach(authority -> {
				if (OidcUserAuthority.class.isInstance(authority)) {
					OidcUserAuthority oidcUserAuthority = (OidcUserAuthority)authority;

					OidcIdToken idToken = oidcUserAuthority.getIdToken();
					OidcUserInfo userInfo = oidcUserAuthority.getUserInfo();

					// Map the claims found in idToken and/or userInfo
					// to one or more GrantedAuthority's and add it to mappedAuthorities

				} else if (OAuth2UserAuthority.class.isInstance(authority)) {
					OAuth2UserAuthority oauth2UserAuthority = (OAuth2UserAuthority)authority;

					Map<String, Object> userAttributes = oauth2UserAuthority.getAttributes();

					// Map the attributes found in userAttributes
					// to one or more GrantedAuthority's and add it to mappedAuthorities

				}
			});

			return mappedAuthorities;
		};
	}
}
```

Alternatively, you can register a `GrantedAuthoritiesMapper``@Bean` to have it automatically applied to the configuration, as follows:

Granted Authorities Mapper Bean Configuration

*   Java

*   Kotlin

```
@Configuration
@EnableWebSecurity
public class OAuth2LoginSecurityConfig {

	@Bean
	public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
		http
		    .oauth2Login(withDefaults());
		return http.build();
	}

	@Bean
	public GrantedAuthoritiesMapper userAuthoritiesMapper() {
		...
	}
}
```

Once authentication completes, it also contains the `FACTOR_AUTHORIZATION_CODE` granted authority.

#### [](https://docs.spring.io/spring-security/reference/servlet/oauth2/login/advanced.html#oauth2login-advanced-map-authorities-oauth2userservice)Delegation-based Strategy with OAuth2UserService

This strategy is advanced compared to using a `GrantedAuthoritiesMapper`. However, it is also more flexible, as it gives you access to the `OAuth2UserRequest` and `OAuth2User` (when using an OAuth 2.0 UserService) or `OidcUserRequest` and `OidcUser` (when using an OpenID Connect 1.0 UserService).

The `OAuth2UserRequest` (and `OidcUserRequest`) provides you access to the associated `OAuth2AccessToken`, which is very useful in cases where the _delegator_ needs to fetch authority information from a protected resource before it can map the custom authorities for the user.

The following example shows how to implement and configure a delegation-based strategy using an OpenID Connect 1.0 UserService:

OAuth2UserService Configuration

*   Java

*   Kotlin

*   Xml

```
@Configuration
@EnableWebSecurity
public class OAuth2LoginSecurityConfig {

	@Bean
	public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
		http
			.oauth2Login((oauth2) -> oauth2
			    .userInfoEndpoint((userInfo) -> userInfo
			        .oidcUserService(this.oidcUserService())
			        ...
			    )
			);
		return http.build();
	}

	private OAuth2UserService<OidcUserRequest, OidcUser> oidcUserService() {
		final OidcUserService delegate = new OidcUserService();

		return (userRequest) -> {
			// Delegate to the default implementation for loading a user
			OidcUser oidcUser = delegate.loadUser(userRequest);

			OAuth2AccessToken accessToken = userRequest.getAccessToken();
			Set<GrantedAuthority> mappedAuthorities = new HashSet<>();

			// TODO
			// 1) Fetch the authority information from the protected resource using accessToken
			// 2) Map the authority information to one or more GrantedAuthority's and add it to mappedAuthorities

			// 3) Create a copy of oidcUser but use the mappedAuthorities instead
			ProviderDetails providerDetails = userRequest.getClientRegistration().getProviderDetails();
			String userNameAttributeName = providerDetails.getUserInfoEndpoint().getUserNameAttributeName();
			if (StringUtils.hasText(userNameAttributeName)) {
				oidcUser = new DefaultOidcUser(mappedAuthorities, oidcUser.getIdToken(), oidcUser.getUserInfo(), userNameAttributeName);
			} else {
				oidcUser = new DefaultOidcUser(mappedAuthorities, oidcUser.getIdToken(), oidcUser.getUserInfo());
			}

			return oidcUser;
		};
	}
}
```

### [](https://docs.spring.io/spring-security/reference/servlet/oauth2/login/advanced.html#oauth2login-advanced-oauth2-user-service)OAuth 2.0 UserService

`DefaultOAuth2UserService` is an implementation of an `OAuth2UserService` that supports standard OAuth 2.0 Provider’s.

`OAuth2UserService` obtains the user attributes of the end-user (the resource owner) from the UserInfo Endpoint (by using the access token granted to the client during the authorization flow) and returns an `AuthenticatedPrincipal` in the form of an `OAuth2User`.

`DefaultOAuth2UserService` uses a `RestOperations` instance when requesting the user attributes at the UserInfo Endpoint.

If you need to customize the pre-processing of the UserInfo Request, you can provide `DefaultOAuth2UserService.setRequestEntityConverter()` with a custom `Converter<OAuth2UserRequest, RequestEntity<?>>`. The default implementation `OAuth2UserRequestEntityConverter` builds a `RequestEntity` representation of a UserInfo Request that sets the `OAuth2AccessToken` in the `Authorization` header by default.

On the other end, if you need to customize the post-handling of the UserInfo Response, you need to provide `DefaultOAuth2UserService.setRestOperations()` with a custom configured `RestOperations`. The default `RestOperations` is configured as follows:

```
RestTemplate restTemplate = new RestTemplate();
restTemplate.setErrorHandler(new OAuth2ErrorResponseErrorHandler());
```

`OAuth2ErrorResponseErrorHandler` is a `ResponseErrorHandler` that can handle an OAuth 2.0 Error (400 Bad Request). It uses an `OAuth2ErrorHttpMessageConverter` for converting the OAuth 2.0 Error parameters to an `OAuth2Error`.

Whether you customize `DefaultOAuth2UserService` or provide your own implementation of `OAuth2UserService`, you need to configure it as follows:

*   Java

*   Kotlin

```
@Configuration
@EnableWebSecurity
public class OAuth2LoginSecurityConfig {

	@Bean
	public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
		http
			.oauth2Login((oauth2) -> oauth2
			    .userInfoEndpoint((userInfo) -> userInfo
			        .userService(this.oauth2UserService())
			        ...
			    )
			);
		return http.build();
	}

	private OAuth2UserService<OAuth2UserRequest, OAuth2User> oauth2UserService() {
		...
	}
}
```

### [](https://docs.spring.io/spring-security/reference/servlet/oauth2/login/advanced.html#oauth2login-advanced-oidc-user-service)OpenID Connect 1.0 UserService

`OidcUserService` is an implementation of an `OAuth2UserService` that supports OpenID Connect 1.0 Provider’s.

The `OidcUserService` leverages the `DefaultOAuth2UserService` when requesting the user attributes at the UserInfo Endpoint.

If you need to customize the pre-processing of the UserInfo Request or the post-handling of the UserInfo Response, you need to provide `OidcUserService.setOauth2UserService()` with a custom configured `DefaultOAuth2UserService`.

Whether you customize `OidcUserService` or provide your own implementation of `OAuth2UserService` for OpenID Connect 1.0 Provider’s, you need to configure it as follows:

*   Java

*   Kotlin

```
@Configuration
@EnableWebSecurity
public class OAuth2LoginSecurityConfig {

	@Bean
	public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
		http
			.oauth2Login((oauth2) -> oauth2
				.userInfoEndpoint((userInfo) -> userInfo
				    .oidcUserService(this.oidcUserService())
				    ...
			    )
			);
		return http.build();
	}

	private OAuth2UserService<OidcUserRequest, OidcUser> oidcUserService() {
		...
	}
}
```

[](https://docs.spring.io/spring-security/reference/servlet/oauth2/login/advanced.html#oauth2login-advanced-idtoken-verify)ID Token Signature Verification
----------------------------------------------------------------------------------------------------------------------------------------------------------

OpenID Connect 1.0 Authentication introduces the [ID Token](https://openid.net/specs/openid-connect-core-1_0.html#IDToken), which is a security token that contains Claims about the Authentication of an End-User by an Authorization Server when used by a Client.

The `OidcIdTokenDecoderFactory` provides a `JwtDecoder` used for `OidcIdToken` signature verification. The default algorithm is `RS256` but may be different when assigned during client registration. For these cases, you can configure a resolver to return the expected JWS algorithm assigned for a specific client.

The JWS algorithm resolver is a `Function` that accepts a `ClientRegistration` and returns the expected `JwsAlgorithm` for the client, such as `SignatureAlgorithm.RS256` or `MacAlgorithm.HS256`

The following code shows how to configure the `OidcIdTokenDecoderFactory``@Bean` to default to `MacAlgorithm.HS256` for all `ClientRegistration` instances:

*   Java

*   Kotlin

```
@Bean
public JwtDecoderFactory<ClientRegistration> idTokenDecoderFactory() {
	OidcIdTokenDecoderFactory idTokenDecoderFactory = new OidcIdTokenDecoderFactory();
	idTokenDecoderFactory.setJwsAlgorithmResolver((clientRegistration) -> clientRegistration.HS256);
	return idTokenDecoderFactory;
}
```

For MAC-based algorithms (such as `HS256`, `HS384`, or `HS512`), the `client-secret` that corresponds to the `client-id` is used as the symmetric key for signature verification.

If more than one `ClientRegistration` is configured for OpenID Connect 1.0 Authentication, the JWS algorithm resolver may evaluate the provided `ClientRegistration` to determine which algorithm to return.

Then, you can proceed to configure [logout](https://docs.spring.io/spring-security/reference/servlet/oauth2/login/logout.html)
