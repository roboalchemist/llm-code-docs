# Source: https://docs.spring.io/spring-security/reference/servlet/authentication/session-management.html

Title: Authentication Persistence and Session Management :: Spring Security

URL Source: https://docs.spring.io/spring-security/reference/servlet/authentication/session-management.html

Markdown Content:
Once you have got an application that is [authenticating requests](https://docs.spring.io/spring-security/reference/servlet/authentication/index.html), it is important to consider how that resulting authentication will be persisted and restored on future requests.

This is done automatically by default, so no additional code is necessary, though it is important to know what `requireExplicitSave` means in `HttpSecurity`.

If you like, [you can read more about what requireExplicitSave is doing](https://docs.spring.io/spring-security/reference/servlet/authentication/session-management.html#how-it-works-requireexplicitsave) or [why it’s important](https://docs.spring.io/spring-security/reference/servlet/authentication/session-management.html#requireexplicitsave). Otherwise, in most cases you are done with this section.

But before you leave, consider if any of these use cases fit your application:

*   I want to [Understand Session Management’s components](https://docs.spring.io/spring-security/reference/servlet/authentication/session-management.html#understanding-session-management-components)

*   I want to [restrict the number of times](https://docs.spring.io/spring-security/reference/servlet/authentication/session-management.html#ns-concurrent-sessions) a user can be logged in concurrently

*   I want [to store the authentication directly](https://docs.spring.io/spring-security/reference/servlet/authentication/session-management.html#store-authentication-manually) myself instead of Spring Security doing it for me

*   I am storing the authentication manually and I want [to remove it](https://docs.spring.io/spring-security/reference/servlet/authentication/session-management.html#properly-clearing-authentication)

*   I am using [`SessionManagementFilter`](https://docs.spring.io/spring-security/reference/servlet/authentication/session-management.html#the-sessionmanagementfilter) and I need [guidance on moving away from that](https://docs.spring.io/spring-security/reference/servlet/authentication/session-management.html#moving-away-from-sessionmanagementfilter)

*   I want to store the authentication [in something other than the session](https://docs.spring.io/spring-security/reference/servlet/authentication/session-management.html#customizing-where-authentication-is-stored)

*   I am using a [stateless authentication](https://docs.spring.io/spring-security/reference/servlet/authentication/session-management.html#stateless-authentication), but [I’d still like to store it in the session](https://docs.spring.io/spring-security/reference/servlet/authentication/session-management.html#storing-stateless-authentication-in-the-session)

*   I am using `SessionCreationPolicy.NEVER` but [the application is still creating sessions](https://docs.spring.io/spring-security/reference/servlet/authentication/session-management.html#never-policy-session-still-created).

[](https://docs.spring.io/spring-security/reference/servlet/authentication/session-management.html#understanding-session-management-components)Understanding Session Management’s Components
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In Spring Security 6, the `SecurityContextPersistenceFilter` and `SessionManagementFilter` are not set by default. In addition to that, any application should only have either `SecurityContextHolderFilter` or `SecurityContextPersistenceFilter` set, never both.

### [](https://docs.spring.io/spring-security/reference/servlet/authentication/session-management.html#the-sessionmanagementfilter)The `SessionManagementFilter`

The `SessionManagementFilter` checks the contents of the `SecurityContextRepository` against the current contents of the `SecurityContextHolder` to determine whether a user has been authenticated during the current request, typically by a non-interactive authentication mechanism, such as pre-authentication or remember-me [[1](https://docs.spring.io/spring-security/reference/servlet/authentication/session-management.html#_footnotedef_1 "View footnote.")]. If the repository contains a security context, the filter does nothing. If it doesn’t, and the thread-local `SecurityContext` contains a (non-anonymous) `Authentication` object, the filter assumes they have been authenticated by a previous filter in the stack. It will then invoke the configured `SessionAuthenticationStrategy`.

If the user is not currently authenticated, the filter will check whether an invalid session ID has been requested (because of a timeout, for example) and will invoke the configured `InvalidSessionStrategy`, if one is set. The most common behaviour is just to redirect to a fixed URL and this is encapsulated in the standard implementation `SimpleRedirectInvalidSessionStrategy`. The latter is also used when configuring an invalid session URL through the namespace, [as described earlier](https://docs.spring.io/spring-security/reference/servlet/authentication/session-management.html#session-mgmt).

#### [](https://docs.spring.io/spring-security/reference/servlet/authentication/session-management.html#moving-away-from-sessionmanagementfilter)Moving Away From `SessionManagementFilter`

In Spring Security 5, the default configuration relies on `SessionManagementFilter` to detect if a user just authenticated and invoke the [SessionAuthenticationStrategy](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/authentication/session/SessionAuthenticationStrategy.html). The problem with this is that it means that in a typical setup, the `HttpSession` must be read for every request.

In Spring Security 6, the default is that authentication mechanisms themselves must invoke the `SessionAuthenticationStrategy`. This means that there is no need to detect when `Authentication` is done and thus the `HttpSession` does not need to be read for every request.

#### [](https://docs.spring.io/spring-security/reference/servlet/authentication/session-management.html#_things_to_consider_when_moving_away_from_sessionmanagementfilter)Things To Consider When Moving Away From `SessionManagementFilter`

In Spring Security 6, the `SessionManagementFilter` is not used by default, therefore, some methods from the `sessionManagement` DSL will not have any effect.

| Method | Replacement |
| --- | --- |
| `sessionAuthenticationErrorUrl` | Configure an [`AuthenticationFailureHandler`](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/authentication/AuthenticationFailureHandler.html) in your authentication mechanism |
| `sessionAuthenticationFailureHandler` | Configure an [`AuthenticationFailureHandler`](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/authentication/AuthenticationFailureHandler.html) in your authentication mechanism |
| `sessionAuthenticationStrategy` | Configure an `SessionAuthenticationStrategy` in your authentication mechanism as [discussed above](https://docs.spring.io/spring-security/reference/servlet/authentication/session-management.html#moving-away-from-sessionmanagementfilter) |

If you try to use any of these methods, an exception will be thrown.

[](https://docs.spring.io/spring-security/reference/servlet/authentication/session-management.html#customizing-where-authentication-is-stored)Customizing Where the Authentication Is Stored
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

By default, Spring Security stores the security context for you in the HTTP session. However, here are several reasons you may want to customize that:

*   You may want to call individual setters on the `HttpSessionSecurityContextRepository` instance

*   You may want to store the security context in a cache or database to enable horizontal scaling

First, you need to create an implementation of `SecurityContextRepository` or use an existing implementation like `HttpSessionSecurityContextRepository`, then you can set it in `HttpSecurity`.

Customizing the `SecurityContextRepository`

*   Java

*   Kotlin

*   XML

```
@Bean
public SecurityFilterChain filterChain(HttpSecurity http) {
    SecurityContextRepository repo = new MyCustomSecurityContextRepository();
    http
        // ...
        .securityContext((context) -> context
            .securityContextRepository(repo)
        );
    return http.build();
}
```

The above configuration sets the `SecurityContextRepository` on the `SecurityContextHolderFilter` and **participating** authentication filters, like `UsernamePasswordAuthenticationFilter`. To also set it in stateless filters, please see [how to customize the `SecurityContextRepository` for Stateless Authentication](https://docs.spring.io/spring-security/reference/servlet/authentication/session-management.html#storing-stateless-authentication-in-the-session).

If you are using a custom authentication mechanism, you might want to [store the `Authentication` by yourself](https://docs.spring.io/spring-security/reference/servlet/authentication/session-management.html#store-authentication-manually).

### [](https://docs.spring.io/spring-security/reference/servlet/authentication/session-management.html#store-authentication-manually)Storing the `Authentication` manually

In some cases, for example, you might be authenticating a user manually instead of relying on Spring Security filters. You can use a custom filters or a [Spring MVC controller](https://docs.spring.io/spring-framework/reference/7.0.4//web.html#mvc-controller) endpoint to do that. If you want to save the authentication between requests, in the `HttpSession`, for example, you have to do so:

*   Java

```
private SecurityContextRepository securityContextRepository =
        new HttpSessionSecurityContextRepository(); (1)

@PostMapping("/login")
public void login(@RequestBody LoginRequest loginRequest, HttpServletRequest request, HttpServletResponse response) { (2)
    UsernamePasswordAuthenticationToken token = UsernamePasswordAuthenticationToken.unauthenticated(
        loginRequest.getUsername(), loginRequest.getPassword()); (3)
    Authentication authentication = authenticationManager.authenticate(token); (4)
    SecurityContext context = securityContextHolderStrategy.createEmptyContext();
    context.setAuthentication(authentication); (5)
    securityContextHolderStrategy.setContext(context);
    securityContextRepository.saveContext(context, request, response); (6)
}

class LoginRequest {

    private String username;
    private String password;

    // getters and setters
}
```

**1**Add the `SecurityContextRepository` to the controller
**2**Inject the `HttpServletRequest` and `HttpServletResponse` to be able to save the `SecurityContext`
**3**Create an unauthenticated `UsernamePasswordAuthenticationToken` using the provided credentials
**4**Call `AuthenticationManager#authenticate` to authenticate the user
**5**Create a `SecurityContext` and set the `Authentication` in it
**6**Save the `SecurityContext` in the `SecurityContextRepository`

And that’s it. If you are not sure what `securityContextHolderStrategy` is in the above example, you can read more about it in the [Using `SecurityContextStrategy` section](https://docs.spring.io/spring-security/reference/servlet/authentication/session-management.html#use-securitycontextholderstrategy).

### [](https://docs.spring.io/spring-security/reference/servlet/authentication/session-management.html#properly-clearing-authentication)Properly Clearing an Authentication

If you are using Spring Security’s [Logout Support](https://docs.spring.io/spring-security/reference/servlet/authentication/logout.html) then it handles a lot of stuff for you including clearing and saving the context. But, let’s say you need to manually log users out of your app. In that case, you’ll need to make sure you’re [clearing and saving the context properly](https://docs.spring.io/spring-security/reference/servlet/authentication/logout.html#creating-custom-logout-endpoint).

### [](https://docs.spring.io/spring-security/reference/servlet/authentication/session-management.html#stateless-authentication)Configuring Persistence for Stateless Authentication

Sometimes there is no need to create and maintain a `HttpSession` for example, to persist the authentication across requests. Some authentication mechanisms like [HTTP Basic](https://docs.spring.io/spring-security/reference/servlet/authentication/passwords/basic.html) are stateless and, therefore, re-authenticates the user on every request.

If you do not wish to create sessions, you can use `SessionCreationPolicy.STATELESS`, like so:

*   Java

*   Kotlin

*   XML

```
@Bean
public SecurityFilterChain filterChain(HttpSecurity http) {
    http
        // ...
        .sessionManagement((session) -> session
            .sessionCreationPolicy(SessionCreationPolicy.STATELESS)
        );
    return http.build();
}
```

If you are using `SessionCreationPolicy.NEVER`, you might notice that the application is still creating a `HttpSession`. In most cases, this happens because the [request is saved in the session](https://docs.spring.io/spring-security/reference/servlet/architecture.html#savedrequests) for the authenticated resource to re-request after authentication is successful. To avoid that, please refer to [how to prevent the request of being saved](https://docs.spring.io/spring-security/reference/servlet/architecture.html#requestcache-prevent-saved-request) section.

#### [](https://docs.spring.io/spring-security/reference/servlet/authentication/session-management.html#storing-stateless-authentication-in-the-session)Storing Stateless Authentication in the Session

If, for some reason, you are using a stateless authentication mechanism, but you still want to store the authentication in the session you can use the `HttpSessionSecurityContextRepository` instead of the `NullSecurityContextRepository`.

For the [HTTP Basic](https://docs.spring.io/spring-security/reference/servlet/authentication/passwords/basic.html), you can add [a `ObjectPostProcessor`](https://docs.spring.io/spring-security/reference/servlet/configuration/java.html#post-processing-configured-objects) that changes the `SecurityContextRepository` used by the `BasicAuthenticationFilter`:

Store HTTP Basic authentication in the `HttpSession`

*   Java

```
@Bean
SecurityFilterChain web(HttpSecurity http) throws Exception {
    http
        // ...
        .httpBasic((basic) -> basic
            .addObjectPostProcessor(new ObjectPostProcessor<BasicAuthenticationFilter>() {
                @Override
                public <O extends BasicAuthenticationFilter> O postProcess(O filter) {
                    filter.setSecurityContextRepository(new HttpSessionSecurityContextRepository());
                    return filter;
                }
            })
        );

    return http.build();
}
```

[](https://docs.spring.io/spring-security/reference/servlet/authentication/session-management.html#requireexplicitsave)Understanding Require Explicit Save
----------------------------------------------------------------------------------------------------------------------------------------------------------

In Spring Security 5, the default behavior is for the [`SecurityContext`](https://docs.spring.io/spring-security/reference/servlet/authentication/architecture.html#servlet-authentication-securitycontext) to automatically be saved to the [`SecurityContextRepository`](https://docs.spring.io/spring-security/reference/servlet/authentication/persistence.html#securitycontextrepository) using the [`SecurityContextPersistenceFilter`](https://docs.spring.io/spring-security/reference/servlet/authentication/session-management.html#securitycontextpersistencefilter). Saving must be done just prior to the `HttpServletResponse` being committed and just before `SecurityContextPersistenceFilter`. Unfortunately, automatic persistence of the `SecurityContext` can surprise users when it is done prior to the request completing (i.e. just prior to committing the `HttpServletResponse`). It also is complex to keep track of the state to determine if a save is necessary causing unnecessary writes to the `SecurityContextRepository` (i.e. `HttpSession`) at times.

For these reasons, the `SecurityContextPersistenceFilter` has been deprecated to be replaced with the `SecurityContextHolderFilter`. In Spring Security 6, the default behavior is that [the `SecurityContextHolderFilter`](https://docs.spring.io/spring-security/reference/servlet/authentication/persistence.html#securitycontextholderfilter) will only read the `SecurityContext` from `SecurityContextRepository` and populate it in the `SecurityContextHolder`. Users now must explicitly save the `SecurityContext` with the `SecurityContextRepository` if they want the `SecurityContext` to persist between requests. This removes ambiguity and improves performance by only requiring writing to the `SecurityContextRepository` (i.e. `HttpSession`) when it is necessary.

[](https://docs.spring.io/spring-security/reference/servlet/authentication/session-management.html#ns-concurrent-sessions)Configuring Concurrent Session Control
----------------------------------------------------------------------------------------------------------------------------------------------------------------

If you wish to place constraints on a single user’s ability to log in to your application, Spring Security supports this out of the box with the following simple additions. First, you need to add the following listener to your configuration to keep Spring Security updated about session lifecycle events:

*   Java

*   Kotlin

*   web.xml

```
@Bean
public HttpSessionEventPublisher httpSessionEventPublisher() {
    return new HttpSessionEventPublisher();
}
```

Then add the following lines to your security configuration:

*   Java

*   Kotlin

*   XML

```
@Bean
public SecurityFilterChain filterChain(HttpSecurity http) {
    http
        .sessionManagement((session) -> session
            .maximumSessions(1)
        );
    return http.build();
}
```

This will prevent a user from logging in multiple times - a second login will cause the first to be invalidated.

You can also adjust this based on who the user is. For example, administrators may be able to have more than one session:

*   Java

*   Kotlin

*   XML

```
@Bean
public SecurityFilterChain filterChain(HttpSecurity http) {
	AuthorizationManager<?> isAdmin = AuthorityAuthorizationManager.hasRole("ADMIN");
    http
        .sessionManagement((session) -> session
            .maximumSessions((authentication) -> isAdmin.authorize(() -> authentication, null).isGranted() ? -1 : 1)
        );
    return http.build();
}
```

Using Spring Boot, you can test the above configurations in the following way:

*   Java

```
@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT)
@AutoConfigureMockMvc
public class MaximumSessionsTests {

    @Autowired
    private MockMvc mvc;

    @Test
    void loginOnSecondLoginThenFirstSessionTerminated() throws Exception {
        MvcResult mvcResult = this.mvc.perform(formLogin())
                .andExpect(authenticated())
                .andReturn();

        MockHttpSession firstLoginSession = (MockHttpSession) mvcResult.getRequest().getSession();

        this.mvc.perform(get("/").session(firstLoginSession))
                .andExpect(authenticated());

        this.mvc.perform(formLogin()).andExpect(authenticated());

        // first session is terminated by second login
        this.mvc.perform(get("/").session(firstLoginSession))
                .andExpect(unauthenticated());
    }

}
```

It is also common that you would prefer to prevent a second login, in which case you can use:

*   Java

*   Kotlin

*   XML

```
@Bean
public SecurityFilterChain filterChain(HttpSecurity http) {
    http
        .sessionManagement((session) -> session
            .maximumSessions(1)
            .maxSessionsPreventsLogin(true)
        );
    return http.build();
}
```

The second login will then be rejected. By "rejected", we mean that the user will be sent to the `authentication-failure-url` if form-based login is being used. If the second authentication takes place through another non-interactive mechanism, such as "remember-me", an "unauthorized" (401) error will be sent to the client. If instead you want to use an error page, you can add the attribute `session-authentication-error-url` to the `session-management` element.

Using Spring Boot, you can test the above configuration the following way:

*   Java

```
@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT)
@AutoConfigureMockMvc
public class MaximumSessionsPreventLoginTests {

    @Autowired
    private MockMvc mvc;

    @Test
    void loginOnSecondLoginThenPreventLogin() throws Exception {
        MvcResult mvcResult = this.mvc.perform(formLogin())
                .andExpect(authenticated())
                .andReturn();

        MockHttpSession firstLoginSession = (MockHttpSession) mvcResult.getRequest().getSession();

        this.mvc.perform(get("/").session(firstLoginSession))
                .andExpect(authenticated());

        // second login is prevented
        this.mvc.perform(formLogin()).andExpect(unauthenticated());

        // first session is still valid
        this.mvc.perform(get("/").session(firstLoginSession))
                .andExpect(authenticated());
    }

}
```

If you are using a customized authentication filter for form-based login, then you have to configure concurrent session control support explicitly. You can try it using the [Maximum Sessions Prevent Login sample](https://github.com/spring-projects/spring-security-samples/tree/main/servlet/spring-boot/java/session-management/maximum-sessions-prevent-login).

If you are using a custom implementation of `UserDetails`, ensure you override the **equals()** and **hashCode()** methods. The default `SessionRegistry` implementation in Spring Security relies on an in-memory Map that uses these methods to correctly identify and manage user sessions. Failing to override them may lead to issues where session tracking and user comparison behave unexpectedly.

[](https://docs.spring.io/spring-security/reference/servlet/authentication/session-management.html#_detecting_timeouts)Detecting Timeouts
-----------------------------------------------------------------------------------------------------------------------------------------

Sessions expire on their own, and there is nothing that needs to be done to ensure that a security context gets removed. That said, Spring Security can detect when a session has expired and take specific actions that you indicate. For example, you may want to redirect to a specific endpoint when a user makes a request with an already-expired session. This is achieved through the `invalidSessionUrl` in `HttpSecurity`:

*   Java

*   Kotlin

*   XML

```
@Bean
public SecurityFilterChain filterChain(HttpSecurity http) {
    http
        .sessionManagement((session) -> session
            .invalidSessionUrl("/invalidSession")
        );
    return http.build();
}
```

Note that if you use this mechanism to detect session timeouts, it may falsely report an error if the user logs out and then logs back in without closing the browser. This is because the session cookie is not cleared when you invalidate the session and will be resubmitted even if the user has logged out. If that is your case, you might want to [configure logout to clear the session cookie](https://docs.spring.io/spring-security/reference/servlet/authentication/session-management.html#clearing-session-cookie-on-logout).

### [](https://docs.spring.io/spring-security/reference/servlet/authentication/session-management.html#_customizing_the_invalid_session_strategy)Customizing the Invalid Session Strategy

The `invalidSessionUrl` is a convenience method for setting the `InvalidSessionStrategy` using the [`SimpleRedirectInvalidSessionStrategy` implementation](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/session/SimpleRedirectInvalidSessionStrategy.html). If you want to customize the behavior, you can implement the [`InvalidSessionStrategy`](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/session/InvalidSessionStrategy.html) interface and configure it using the `invalidSessionStrategy` method:

*   Java

*   Kotlin

*   XML

```
@Bean
public SecurityFilterChain filterChain(HttpSecurity http) {
    http
        .sessionManagement((session) -> session
            .invalidSessionStrategy(new MyCustomInvalidSessionStrategy())
        );
    return http.build();
}
```

[](https://docs.spring.io/spring-security/reference/servlet/authentication/session-management.html#clearing-session-cookie-on-logout)Clearing Session Cookies on Logout
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

You can explicitly delete the JSESSIONID cookie on logging out, for example by using the [`Clear-Site-Data` header](https://w3c.github.io/webappsec-clear-site-data/) in the logout handler:

*   Java

*   Kotlin

*   XML

```
@Bean
public SecurityFilterChain filterChain(HttpSecurity http) {
    http
        .logout((logout) -> logout
            .addLogoutHandler(new HeaderWriterLogoutHandler(new ClearSiteDataHeaderWriter(COOKIES)))
        );
    return http.build();
}
```

This has the advantage of being container agnostic and will work with any container that supports the `Clear-Site-Data` header.

As an alternative, you can also use the following syntax in the logout handler:

*   Java

*   Kotlin

*   XML

```
@Bean
public SecurityFilterChain filterChain(HttpSecurity http) {
    http
        .logout((logout) -> logout
            .deleteCookies("JSESSIONID")
        );
    return http.build();
}
```

Unfortunately, this cannot be guaranteed to work with every servlet container, so you need to test it in your environment.

If you run your application behind a proxy, you may also be able to remove the session cookie by configuring the proxy server. For example, by using Apache HTTPD’s `mod_headers`, the following directive deletes the `JSESSIONID` cookie by expiring it in the response to a logout request (assuming the application is deployed under the `/tutorial` path):

```
<LocationMatch "/tutorial/logout">
Header always set Set-Cookie "JSESSIONID=;Path=/tutorial;Expires=Thu, 01 Jan 1970 00:00:00 GMT"
</LocationMatch>
```

[](https://docs.spring.io/spring-security/reference/servlet/authentication/session-management.html#ns-session-fixation)Understanding Session Fixation Attack Protection
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Session fixation](https://en.wikipedia.org/wiki/Session_fixation) attacks are a potential risk where it is possible for a malicious attacker to create a session by accessing a site, then persuade another user to log in with the same session (by sending them a link containing the session identifier as a parameter, for example). Spring Security protects against this automatically by creating a new session or otherwise changing the session ID when a user logs in.

### [](https://docs.spring.io/spring-security/reference/servlet/authentication/session-management.html#_configuring_session_fixation_protection)Configuring Session Fixation Protection

You can control the strategy for Session Fixation Protection by choosing between three recommended options:

*   `changeSessionId` - Do not create a new session. Instead, use the session fixation protection provided by the Servlet container (`HttpServletRequest#changeSessionId()`). This option is only available in Servlet 3.1 (Java EE 7) and newer containers. Specifying it in older containers will result in an exception. This is the default in Servlet 3.1 and newer containers.

*   `newSession` - Create a new "clean" session, without copying the existing session data (Spring Security-related attributes will still be copied).

*   `migrateSession` - Create a new session and copy all existing session attributes to the new session. This is the default in Servlet 3.0 or older containers.

You can configure the session fixation protection by doing:

*   Java

*   Kotlin

*   XML

```
@Bean
public SecurityFilterChain filterChain(HttpSecurity http) {
    http
        .sessionManagement((session) -> session
            .sessionFixation((sessionFixation) -> sessionFixation
                .newSession()
            )
        );
    return http.build();
}
```

When session fixation protection occurs, it results in a `SessionFixationProtectionEvent` being published in the application context. If you use `changeSessionId`, this protection will _also_ result in any `jakarta.servlet.http.HttpSessionIdListener`s being notified, so use caution if your code listens for both events.

You can also set the session fixation protection to `none` to disable it, but this is not recommended as it leaves your application vulnerable.

[](https://docs.spring.io/spring-security/reference/servlet/authentication/session-management.html#use-securitycontextholderstrategy)Using `SecurityContextHolderStrategy`
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Consider the following block of code:

*   Java

```
UsernamePasswordAuthenticationToken token = new UsernamePasswordAuthenticationToken(
        loginRequest.getUsername(), loginRequest.getPassword());
Authentication authentication = this.authenticationManager.authenticate(token);
// ...
SecurityContext context = SecurityContextHolder.createEmptyContext(); (1)
context.setAuthentication(authentication); (2)
SecurityContextHolder.setContext(context); (3)
```

1.   Creates an empty `SecurityContext` instance by accessing the `SecurityContextHolder` statically.

2.   Sets the `Authentication` object in the `SecurityContext` instance.

3.   Sets the `SecurityContext` instance in the `SecurityContextHolder` statically.

While the above code works fine, it can produce some undesired effects: when components access the `SecurityContext` statically through `SecurityContextHolder`, this can create race conditions when there are multiple application contexts that want to specify the `SecurityContextHolderStrategy`. This is because in `SecurityContextHolder` there is one strategy per classloader instead of one per application context.

To address this, components can wire `SecurityContextHolderStrategy` from the application context. By default, they will still look up the strategy from `SecurityContextHolder`.

These changes are largely internal, but they present the opportunity for applications to autowire the `SecurityContextHolderStrategy` instead of accessing the `SecurityContext` statically. To do so, you should change the code to the following:

*   Java

```
public class SomeClass {

    private final SecurityContextHolderStrategy securityContextHolderStrategy = SecurityContextHolder.getContextHolderStrategy();

    public void someMethod() {
        UsernamePasswordAuthenticationToken token = UsernamePasswordAuthenticationToken.unauthenticated(
                loginRequest.getUsername(), loginRequest.getPassword());
        Authentication authentication = this.authenticationManager.authenticate(token);
        // ...
        SecurityContext context = this.securityContextHolderStrategy.createEmptyContext(); (1)
        context.setAuthentication(authentication); (2)
        this.securityContextHolderStrategy.setContext(context); (3)
    }

}
```

1.   Creates an empty `SecurityContext` instance using the configured `SecurityContextHolderStrategy`.

2.   Sets the `Authentication` object in the `SecurityContext` instance.

3.   Sets the `SecurityContext` instance in the `SecurityContextHolderStrategy`.

[](https://docs.spring.io/spring-security/reference/servlet/authentication/session-management.html#session-mgmt-force-session-creation)Forcing Eager Session Creation
---------------------------------------------------------------------------------------------------------------------------------------------------------------------

At times, it can be valuable to eagerly create sessions. This can be done by using the [`ForceEagerSessionCreationFilter`](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/web/session/ForceEagerSessionCreationFilter.html) which can be configured using:

*   Java

*   Kotlin

*   XML

```
@Bean
public SecurityFilterChain filterChain(HttpSecurity http) {
    http
        .sessionManagement((session) -> session
            .sessionCreationPolicy(SessionCreationPolicy.ALWAYS)
        );
    return http.build();
}
```

* * *

[1](https://docs.spring.io/spring-security/reference/servlet/authentication/session-management.html#_footnoteref_1). Authentication by mechanisms which perform a redirect after authenticating (such as form-login) will not be detected by `SessionManagementFilter`, as the filter will not be invoked during the authenticating request. Session-management functionality has to be handled separately in these cases.
