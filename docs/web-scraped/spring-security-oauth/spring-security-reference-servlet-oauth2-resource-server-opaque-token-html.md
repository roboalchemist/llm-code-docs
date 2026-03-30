# Source: https://docs.spring.io/spring-security/reference/servlet/oauth2/resource-server/opaque-token.html

Title: OAuth 2.0 Resource Server Opaque Token :: Spring Security

URL Source: https://docs.spring.io/spring-security/reference/servlet/oauth2/resource-server/opaque-token.html

Markdown Content:
[](https://docs.spring.io/spring-security/reference/servlet/oauth2/resource-server/opaque-token.html#oauth2resourceserver-opaque-minimaldependencies)Minimal Dependencies for Introspection
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

As described in [Minimal Dependencies for JWT](https://docs.spring.io/spring-security/reference/servlet/oauth2/resource-server/jwt.html#oauth2resourceserver-jwt-minimaldependencies) most of Resource Server support is collected in `spring-security-oauth2-resource-server`. However unless a custom [`OpaqueTokenIntrospector`](https://docs.spring.io/spring-security/reference/servlet/oauth2/resource-server/opaque-token.html#oauth2resourceserver-opaque-introspector) is provided, the Resource Server will fallback to `SpringOpaqueTokenIntrospector`. This means that only `spring-security-oauth2-resource-server` is necessary in order to have a working minimal Resource Server that supports opaque Bearer Tokens.

[](https://docs.spring.io/spring-security/reference/servlet/oauth2/resource-server/opaque-token.html#oauth2resourceserver-opaque-minimalconfiguration)Minimal Configuration for Introspection
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Typically, an opaque token can be verified via an [OAuth 2.0 Introspection Endpoint](https://tools.ietf.org/html/rfc7662), hosted by the authorization server. This can be handy when revocation is a requirement.

When using [Spring Boot](https://spring.io/projects/spring-boot), configuring an application as a resource server that uses introspection consists of two basic steps. First, include the needed dependencies and second, indicate the introspection endpoint details.

### [](https://docs.spring.io/spring-security/reference/servlet/oauth2/resource-server/opaque-token.html#oauth2resourceserver-opaque-introspectionuri)Specifying the Authorization Server

To specify where the introspection endpoint is, simply do:

```
spring:
  security:
    oauth2:
      resourceserver:
        opaquetoken:
          introspection-uri: https://idp.example.com/introspect
          client-id: client
          client-secret: secret
```

Where `idp.example.com/introspect` is the introspection endpoint hosted by your authorization server and `client-id` and `client-secret` are the credentials needed to hit that endpoint.

Resource Server will use these properties to further self-configure and subsequently validate incoming JWTs.

When using introspection, the authorization server’s word is the law. If the authorization server responses that the token is valid, then it is.

And that’s it!

### [](https://docs.spring.io/spring-security/reference/servlet/oauth2/resource-server/opaque-token.html#_startup_expectations)Startup Expectations

When this property and these dependencies are used, Resource Server will automatically configure itself to validate Opaque Bearer Tokens.

This startup process is quite a bit simpler than for JWTs since no endpoints need to be discovered and no additional validation rules get added.

### [](https://docs.spring.io/spring-security/reference/servlet/oauth2/resource-server/opaque-token.html#_runtime_expectations)Runtime Expectations

Once the application is started up, Resource Server will attempt to process any request containing an `Authorization: Bearer` header:

```
GET / HTTP/1.1
Authorization: Bearer some-token-value # Resource Server will process this
```

So long as this scheme is indicated, Resource Server will attempt to process the request according to the Bearer Token specification.

Given an Opaque Token, Resource Server will

1.   Query the provided introspection endpoint using the provided credentials and the token

2.   Inspect the response for an `{ 'active' : true }` attribute

3.   Map each scope to an authority with the prefix `SCOPE_`

The resulting `Authentication#getPrincipal`, by default, is a Spring Security [`OAuth2AuthenticatedPrincipal`](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/oauth2/core/OAuth2AuthenticatedPrincipal.html) object, and `Authentication#getName` maps to the token’s `sub` property, if one is present.

From here, you may want to jump to:

*   [How Opaque Token Authentication Works](https://docs.spring.io/spring-security/reference/servlet/oauth2/resource-server/opaque-token.html#oauth2resourceserver-opaque-architecture)

*   [Looking Up Attributes Post-Authentication](https://docs.spring.io/spring-security/reference/servlet/oauth2/resource-server/opaque-token.html#oauth2resourceserver-opaque-attributes)

*   [Extracting Authorities Manually](https://docs.spring.io/spring-security/reference/servlet/oauth2/resource-server/opaque-token.html#oauth2resourceserver-opaque-authorization-extraction)

*   [Using Introspection with JWTs](https://docs.spring.io/spring-security/reference/servlet/oauth2/resource-server/opaque-token.html#oauth2resourceserver-opaque-jwt-introspector)

[](https://docs.spring.io/spring-security/reference/servlet/oauth2/resource-server/opaque-token.html#oauth2resourceserver-opaque-architecture)How Opaque Token Authentication Works
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Next, let’s see the architectural components that Spring Security uses to support [opaque token](https://tools.ietf.org/html/rfc7662) Authentication in servlet-based applications, like the one we just saw.

Let’s take a look at how `OpaqueTokenAuthenticationProvider` works within Spring Security. The figure explains details of how the [`AuthenticationManager`](https://docs.spring.io/spring-security/reference/servlet/authentication/architecture.html#servlet-authentication-authenticationmanager) in figures from [Reading the Bearer Token](https://docs.spring.io/spring-security/reference/servlet/oauth2/resource-server/index.html#oauth2resourceserver-authentication-bearertokenauthenticationfilter) works.

![Image 1: opaquetokenauthenticationprovider](https://docs.spring.io/spring-security/reference/_images/servlet/oauth2/opaquetokenauthenticationprovider.png)

Figure 1. `OpaqueTokenAuthenticationProvider` Usage

![Image 2: number 1](https://docs.spring.io/spring-security/reference/_images/icons/number_1.png) The authentication `Filter` from [Reading the Bearer Token](https://docs.spring.io/spring-security/reference/servlet/oauth2/resource-server/index.html#oauth2resourceserver-authentication-bearertokenauthenticationfilter) passes a `BearerTokenAuthenticationToken` to the `AuthenticationManager` which is implemented by [`ProviderManager`](https://docs.spring.io/spring-security/reference/servlet/authentication/architecture.html#servlet-authentication-providermanager).

![Image 3: number 2](https://docs.spring.io/spring-security/reference/_images/icons/number_2.png) The `ProviderManager` is configured to use an [AuthenticationProvider](https://docs.spring.io/spring-security/reference/servlet/authentication/architecture.html#servlet-authentication-authenticationprovider) of type `OpaqueTokenAuthenticationProvider`.

![Image 4: number 3](https://docs.spring.io/spring-security/reference/_images/icons/number_3.png)`OpaqueTokenAuthenticationProvider` introspects the opaque token and adds granted authorities using an [`OpaqueTokenIntrospector`](https://docs.spring.io/spring-security/reference/servlet/oauth2/resource-server/opaque-token.html#oauth2resourceserver-opaque-introspector). When authentication is successful, the [`Authentication`](https://docs.spring.io/spring-security/reference/servlet/authentication/architecture.html#servlet-authentication-authentication) that is returned is of type `BearerTokenAuthentication` and has a principal that is the `OAuth2AuthenticatedPrincipal` returned by the configured [`OpaqueTokenIntrospector`](https://docs.spring.io/spring-security/reference/servlet/oauth2/resource-server/opaque-token.html#oauth2resourceserver-opaque-introspector) and a set of authorities that contains at least `FACTOR_BEARER`. Ultimately, the returned `BearerTokenAuthentication` will be set on the [`SecurityContextHolder`](https://docs.spring.io/spring-security/reference/servlet/authentication/architecture.html#servlet-authentication-securitycontextholder) by the authentication `Filter`.

[](https://docs.spring.io/spring-security/reference/servlet/oauth2/resource-server/opaque-token.html#oauth2resourceserver-opaque-attributes)Looking Up Attributes Post-Authentication
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Once a token is authenticated, an instance of `BearerTokenAuthentication` is set in the `SecurityContext`.

This means that it’s available in `@Controller` methods when using `@EnableWebMvc` in your configuration:

*   Java

*   Kotlin

```
@GetMapping("/foo")
public String foo(BearerTokenAuthentication authentication) {
    return authentication.getTokenAttributes().get("sub") + " is the subject";
}
```

Since `BearerTokenAuthentication` holds an `OAuth2AuthenticatedPrincipal`, that also means that it’s available to controller methods, too:

*   Java

*   Kotlin

```
@GetMapping("/foo")
public String foo(@AuthenticationPrincipal OAuth2AuthenticatedPrincipal principal) {
    return principal.getAttribute("sub") + " is the subject";
}
```

### [](https://docs.spring.io/spring-security/reference/servlet/oauth2/resource-server/opaque-token.html#_looking_up_attributes_via_spel)Looking Up Attributes Via SpEL

Of course, this also means that attributes can be accessed via SpEL.

For example, if using `@EnableGlobalMethodSecurity` so that you can use `@PreAuthorize` annotations, you can do:

*   Java

*   Kotlin

```
@PreAuthorize("principal?.attributes['sub'] == 'foo'")
public String forFoosEyesOnly() {
    return "foo";
}
```

[](https://docs.spring.io/spring-security/reference/servlet/oauth2/resource-server/opaque-token.html#oauth2resourceserver-opaque-sansboot)Overriding or Replacing Boot Auto Configuration
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

There are two `@Bean`s that Spring Boot generates on Resource Server’s behalf.

The first is a `SecurityFilterChain` that configures the app as a resource server. When use Opaque Token, this `SecurityFilterChain` looks like:

Default Opaque Token Configuration

*   Java

*   Kotlin

```
@Bean
public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
    http
        .authorizeHttpRequests((authorize) -> authorize
            .anyRequest().authenticated()
        )
        .oauth2ResourceServer((oauth2) -> oauth2
            .opaqueToken(Customizer.withDefaults())
        );
    return http.build();
}
```

If the application doesn’t expose a `SecurityFilterChain` bean, then Spring Boot will expose the above default one.

Replacing this is as simple as exposing the bean within the application:

Custom Opaque Token Configuration

*   Java

*   Kotlin

```
import static org.springframework.security.oauth2.core.authorization.OAuth2AuthorizationManagers.hasScope;

@Configuration
@EnableWebSecurity
public class MyCustomSecurityConfiguration {
    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
        http
            .authorizeHttpRequests((authorize) -> authorize
                .requestMatchers("/messages/**").access(hasScope("message:read"))
                .anyRequest().authenticated()
            )
            .oauth2ResourceServer((oauth2) -> oauth2
                .opaqueToken((opaqueToken) -> opaqueToken
                    .introspector(myIntrospector())
                )
            );
        return http.build();
    }
}
```

The above requires the scope of `message:read` for any URL that starts with `/messages/`.

Methods on the `oauth2ResourceServer` DSL will also override or replace auto configuration.

For example, the second `@Bean` Spring Boot creates is an `OpaqueTokenIntrospector`, [which decodes `String` tokens into validated instances of `OAuth2AuthenticatedPrincipal`](https://docs.spring.io/spring-security/reference/servlet/oauth2/resource-server/opaque-token.html#oauth2resourceserver-opaque-architecture-introspector):

*   Java

*   Kotlin

```
@Bean
public OpaqueTokenIntrospector introspector() {
    return SpringOpaqueTokenIntrospector.withIntrospectionUri(introspectionUri)
            .clientId(clientId).clientSecret(clientSecret).build();
}
```

If the application doesn’t expose an [`OpaqueTokenIntrospector`](https://docs.spring.io/spring-security/reference/servlet/oauth2/resource-server/opaque-token.html#oauth2resourceserver-opaque-architecture-introspector) bean, then Spring Boot will expose the above default one.

And its configuration can be overridden using `introspectionUri()` and `introspectionClientCredentials()` or replaced using `introspector()`.

If the application doesn’t expose an `OpaqueTokenAuthenticationConverter` bean, then spring-security will build `BearerTokenAuthentication`.

Or, if you’re not using Spring Boot at all, then all of these components - the filter chain, an [`OpaqueTokenIntrospector`](https://docs.spring.io/spring-security/reference/servlet/oauth2/resource-server/opaque-token.html#oauth2resourceserver-opaque-architecture-introspector) and an `OpaqueTokenAuthenticationConverter` can be specified in XML.

The filter chain is specified like so:

Default Opaque Token Configuration

*   Xml

```
<http>
    <intercept-uri pattern="/**" access="authenticated"/>
    <oauth2-resource-server>
        <opaque-token introspector-ref="opaqueTokenIntrospector"
                authentication-converter-ref="opaqueTokenAuthenticationConverter"/>
    </oauth2-resource-server>
</http>
```

And the [`OpaqueTokenIntrospector`](https://docs.spring.io/spring-security/reference/servlet/oauth2/resource-server/opaque-token.html#oauth2resourceserver-opaque-architecture-introspector) like so:

Opaque Token Introspector

*   Xml

```
<bean id="opaqueTokenIntrospector"
        class="org.springframework.security.oauth2.server.resource.introspection.SpringOpaqueTokenIntrospector">
    <constructor-arg value="${spring.security.oauth2.resourceserver.opaquetoken.introspection_uri}"/>
    <constructor-arg value="${spring.security.oauth2.resourceserver.opaquetoken.client_id}"/>
    <constructor-arg value="${spring.security.oauth2.resourceserver.opaquetoken.client_secret}"/>
</bean>
```

And the `OpaqueTokenAuthenticationConverter` like so:

Opaque Token Authentication Converter

*   Xml

```
<bean id="opaqueTokenAuthenticationConverter"
        class="com.example.CustomOpaqueTokenAuthenticationConverter"/>
```

### [](https://docs.spring.io/spring-security/reference/servlet/oauth2/resource-server/opaque-token.html#oauth2resourceserver-opaque-introspectionuri-dsl)Using `introspectionUri()`

An authorization server’s Introspection Uri can be configured [as a configuration property](https://docs.spring.io/spring-security/reference/servlet/oauth2/resource-server/opaque-token.html#oauth2resourceserver-opaque-introspectionuri) or it can be supplied in the DSL:

Introspection URI Configuration

*   Java

*   Kotlin

*   Xml

```
@Configuration
@EnableWebSecurity
public class DirectlyConfiguredIntrospectionUri {
    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
        http
            .authorizeHttpRequests((authorize) -> authorize
                .anyRequest().authenticated()
            )
            .oauth2ResourceServer((oauth2) -> oauth2
                .opaqueToken((opaqueToken) -> opaqueToken
                    .introspectionUri("https://idp.example.com/introspect")
                    .introspectionClientCredentials("client", "secret")
                )
            );
        return http.build();
    }
}
```

Using `introspectionUri()` takes precedence over any configuration property.

### [](https://docs.spring.io/spring-security/reference/servlet/oauth2/resource-server/opaque-token.html#oauth2resourceserver-opaque-introspector-dsl)Using `introspector()`

More powerful than `introspectionUri()` is `introspector()`, which will completely replace any Boot auto configuration of [`OpaqueTokenIntrospector`](https://docs.spring.io/spring-security/reference/servlet/oauth2/resource-server/opaque-token.html#oauth2resourceserver-opaque-architecture-introspector):

Introspector Configuration

*   Java

*   Kotlin

*   Xml

```
@Configuration
@EnableWebSecurity
public class DirectlyConfiguredIntrospector {
    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
        http
            .authorizeHttpRequests((authorize) -> authorize
                .anyRequest().authenticated()
            )
            .oauth2ResourceServer((oauth2) -> oauth2
                .opaqueToken((opaqueToken) -> opaqueToken
                    .introspector(myCustomIntrospector())
                )
            );
        return http.build();
    }
}
```

This is handy when deeper configuration, like [authority mapping](https://docs.spring.io/spring-security/reference/servlet/oauth2/resource-server/opaque-token.html#oauth2resourceserver-opaque-authorization-extraction), [JWT revocation](https://docs.spring.io/spring-security/reference/servlet/oauth2/resource-server/opaque-token.html#oauth2resourceserver-opaque-jwt-introspector), or [request timeouts](https://docs.spring.io/spring-security/reference/servlet/oauth2/resource-server/opaque-token.html#oauth2resourceserver-opaque-timeouts), is necessary.

### [](https://docs.spring.io/spring-security/reference/servlet/oauth2/resource-server/opaque-token.html#oauth2resourceserver-opaque-introspector-bean)Exposing a `OpaqueTokenIntrospector``@Bean`

Or, exposing a [`OpaqueTokenIntrospector`](https://docs.spring.io/spring-security/reference/servlet/oauth2/resource-server/opaque-token.html#oauth2resourceserver-opaque-architecture-introspector)`@Bean` has the same effect as `introspector()`:

```
@Bean
public OpaqueTokenIntrospector introspector() {
    return return SpringOpaqueTokenIntrospector.withIntrospectionUri(introspectionUri)
            .clientId(clientId).clientSecret(clientSecret).build();
}
```

An OAuth 2.0 Introspection endpoint will typically return a `scope` attribute, indicating the scopes (or authorities) it’s been granted, for example:

`{ …​, "scope" : "messages contacts"}`

When this is the case, Resource Server will attempt to coerce these scopes into a list of granted authorities, prefixing each scope with the string "SCOPE_".

This means that to protect an endpoint or method with a scope derived from an Opaque Token, the corresponding expressions should include this prefix:

Authorization Opaque Token Configuration

*   Java

*   Kotlin

*   Xml

```
import static org.springframework.security.oauth2.core.authorization.OAuth2AuthorizationManagers.hasScope;

@Configuration
@EnableWebSecurity
public class MappedAuthorities {
    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
        http
            .authorizeHttpRequests((authorizeRequests) -> authorizeRequests
                .requestMatchers("/contacts/**").access(hasScope("contacts"))
                .requestMatchers("/messages/**").access(hasScope("messages"))
                .anyRequest().authenticated()
            )
            .oauth2ResourceServer((oauth2) -> oauth2
                .opaqueToken(Customizer.withDefaults())
            );
        return http.build();
    }
}
```

Or similarly with method security:

*   Java

*   Kotlin

```
@PreAuthorize("hasAuthority('SCOPE_messages')")
public List<Message> getMessages(...) {}
```

By default, Opaque Token support will extract the scope claim from an introspection response and parse it into individual `GrantedAuthority` instances.

For example, if the introspection response were:

```
{
    "active" : true,
    "scope" : "message:read message:write"
}
```

Then Resource Server would generate an `Authentication` with two authorities, one for `message:read` and the other for `message:write`.

This can, of course, be customized using a custom [`OpaqueTokenIntrospector`](https://docs.spring.io/spring-security/reference/servlet/oauth2/resource-server/opaque-token.html#oauth2resourceserver-opaque-architecture-introspector) that takes a look at the attribute set and converts in its own way:

*   Java

*   Kotlin

```
public class CustomAuthoritiesOpaqueTokenIntrospector implements OpaqueTokenIntrospector {
    private OpaqueTokenIntrospector delegate = SpringOpaqueTokenIntrospector
            .withIntrospectionUri("https://idp.example.org/introspect")
            .clientId("client").clientSecret("secret").build();

    public OAuth2AuthenticatedPrincipal introspect(String token) {
        OAuth2AuthenticatedPrincipal principal = this.delegate.introspect(token);
        return new DefaultOAuth2AuthenticatedPrincipal(
                principal.getName(), principal.getAttributes(), extractAuthorities(principal));
    }

    private Collection<GrantedAuthority> extractAuthorities(OAuth2AuthenticatedPrincipal principal) {
        List<String> scopes = principal.getAttribute(OAuth2IntrospectionClaimNames.SCOPE);
        return scopes.stream()
                .map(SimpleGrantedAuthority::new)
                .collect(Collectors.toList());
    }
}
```

Thereafter, this custom introspector can be configured simply by exposing it as a `@Bean`:

*   Java

*   Kotlin

```
@Bean
public OpaqueTokenIntrospector introspector() {
    return new CustomAuthoritiesOpaqueTokenIntrospector();
}
```

[](https://docs.spring.io/spring-security/reference/servlet/oauth2/resource-server/opaque-token.html#oauth2resourceserver-opaque-timeouts)Configuring Timeouts
--------------------------------------------------------------------------------------------------------------------------------------------------------------

By default, Resource Server uses connection and socket timeouts of 30 seconds each for coordinating with the authorization server.

This may be too short in some scenarios. Further, it doesn’t take into account more sophisticated patterns like back-off and discovery.

To adjust the way in which Resource Server connects to the authorization server, `SpringOpaqueTokenIntrospector` accepts an instance of `RestOperations`:

*   Java

*   Kotlin

```
@Bean
public OpaqueTokenIntrospector introspector(RestTemplateBuilder builder, OAuth2ResourceServerProperties properties) {
    RestOperations rest = builder
            .basicAuthentication(properties.getOpaquetoken().getClientId(), properties.getOpaquetoken().getClientSecret())
            .setConnectTimeout(Duration.ofSeconds(60))
            .setReadTimeout(Duration.ofSeconds(60))
            .build();

    return SpringOpaqueTokenIntrospector(introspectionUri, rest);
}
```

[](https://docs.spring.io/spring-security/reference/servlet/oauth2/resource-server/opaque-token.html#oauth2resourceserver-opaque-jwt-introspector)Using Introspection with JWTs
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

A common question is whether or not introspection is compatible with JWTs. Spring Security’s Opaque Token support has been designed to not care about the format of the token — it will gladly pass any token to the introspection endpoint provided.

So, let’s say that you’ve got a requirement that requires you to check with the authorization server on each request, in case the JWT has been revoked.

Even though you are using the JWT format for the token, your validation method is introspection, meaning you’d want to do:

```
spring:
  security:
    oauth2:
      resourceserver:
        opaquetoken:
          introspection-uri: https://idp.example.org/introspection
          client-id: client
          client-secret: secret
```

In this case, the resulting `Authentication` would be `BearerTokenAuthentication`. Any attributes in the corresponding `OAuth2AuthenticatedPrincipal` would be whatever was returned by the introspection endpoint.

But, let’s say that, oddly enough, the introspection endpoint only returns whether or not the token is active. Now what?

In this case, you can create a custom [`OpaqueTokenIntrospector`](https://docs.spring.io/spring-security/reference/servlet/oauth2/resource-server/opaque-token.html#oauth2resourceserver-opaque-architecture-introspector) that still hits the endpoint, but then updates the returned principal to have the JWTs claims as the attributes:

*   Java

*   Kotlin

```
public class JwtOpaqueTokenIntrospector implements OpaqueTokenIntrospector {
    private OpaqueTokenIntrospector delegate = SpringOpaqueTokenIntrospector
            .withIntrospectionUri("https://idp.example.org/introspect")
            .clientId("client").clientSecret("secret").build();
    private JwtDecoder jwtDecoder = new NimbusJwtDecoder(new ParseOnlyJWTProcessor());

    public OAuth2AuthenticatedPrincipal introspect(String token) {
        OAuth2AuthenticatedPrincipal principal = this.delegate.introspect(token);
        try {
            Jwt jwt = this.jwtDecoder.decode(token);
            return new DefaultOAuth2AuthenticatedPrincipal(jwt.getClaims(), NO_AUTHORITIES);
        } catch (JwtException ex) {
            throw new OAuth2IntrospectionException(ex);
        }
    }

    private static class ParseOnlyJWTProcessor extends DefaultJWTProcessor<SecurityContext> {
    	JWTClaimsSet process(SignedJWT jwt, SecurityContext context)
                throws JOSEException {
            return jwt.getJWTClaimsSet();
        }
    }
}
```

Thereafter, this custom introspector can be configured simply by exposing it as a `@Bean`:

*   Java

*   Kotlin

```
@Bean
public OpaqueTokenIntrospector introspector() {
    return new JwtOpaqueTokenIntrospector();
}
```

[](https://docs.spring.io/spring-security/reference/servlet/oauth2/resource-server/opaque-token.html#oauth2resourceserver-opaque-userinfo)Calling a `/userinfo` Endpoint
------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Generally speaking, a Resource Server doesn’t care about the underlying user, but instead about the authorities that have been granted.

That said, at times it can be valuable to tie the authorization statement back to a user.

If an application is also using `spring-security-oauth2-client`, having set up the appropriate `ClientRegistrationRepository`, then this is quite simple with a custom [`OpaqueTokenIntrospector`](https://docs.spring.io/spring-security/reference/servlet/oauth2/resource-server/opaque-token.html#oauth2resourceserver-opaque-architecture-introspector). This implementation below does three things:

*   Delegates to the introspection endpoint, to affirm the token’s validity

*   Looks up the appropriate client registration associated with the `/userinfo` endpoint

*   Invokes and returns the response from the `/userinfo` endpoint

*   Java

*   Kotlin

```
public class UserInfoOpaqueTokenIntrospector implements OpaqueTokenIntrospector {
    private final OpaqueTokenIntrospector delegate = SpringOpaqueTokenIntrospector
            .withIntrospectionUri("https://idp.example.org/introspect")
            .clientId("client").clientSecret("secret").build();
    private final OAuth2UserService oauth2UserService = new DefaultOAuth2UserService();

    private final ClientRegistrationRepository repository;

    // ... constructor

    @Override
    public OAuth2AuthenticatedPrincipal introspect(String token) {
        OAuth2AuthenticatedPrincipal authorized = this.delegate.introspect(token);
        Instant issuedAt = authorized.getAttribute(ISSUED_AT);
        Instant expiresAt = authorized.getAttribute(EXPIRES_AT);
        ClientRegistration clientRegistration = this.repository.findByRegistrationId("registration-id");
        OAuth2AccessToken token = new OAuth2AccessToken(BEARER, token, issuedAt, expiresAt);
        OAuth2UserRequest oauth2UserRequest = new OAuth2UserRequest(clientRegistration, token);
        return this.oauth2UserService.loadUser(oauth2UserRequest);
    }
}
```

If you aren’t using `spring-security-oauth2-client`, it’s still quite simple. You will simply need to invoke the `/userinfo` with your own instance of `WebClient`:

*   Java

*   Kotlin

```
public class UserInfoOpaqueTokenIntrospector implements OpaqueTokenIntrospector {
    private final OpaqueTokenIntrospector delegate = SpringOpaqueTokenIntrospector
            .withIntrospectionUri("https://idp.example.org/introspect")
            .clientId("client").clientSecret("secret").build();
    private final WebClient rest = WebClient.create();

    @Override
    public OAuth2AuthenticatedPrincipal introspect(String token) {
        OAuth2AuthenticatedPrincipal authorized = this.delegate.introspect(token);
        return makeUserInfoRequest(authorized);
    }
}
```

Either way, having created your [`OpaqueTokenIntrospector`](https://docs.spring.io/spring-security/reference/servlet/oauth2/resource-server/opaque-token.html#oauth2resourceserver-opaque-architecture-introspector), you should publish it as a `@Bean` to override the defaults:

*   Java

*   Kotlin

```
@Bean
OpaqueTokenIntrospector introspector() {
    return new UserInfoOpaqueTokenIntrospector(...);
}
```
