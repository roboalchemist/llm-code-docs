# Source: https://docs.spring.io/spring-security/reference/servlet/authorization/architecture.html

Title: Authorization Architecture :: Spring Security

URL Source: https://docs.spring.io/spring-security/reference/servlet/authorization/architecture.html

Markdown Content:
This section describes the Spring Security architecture that applies to authorization.

[`Authentication`](https://docs.spring.io/spring-security/reference/servlet/authentication/architecture.html#servlet-authentication-authentication) discusses how all `Authentication` implementations store a list of `GrantedAuthority` objects. These represent the authorities that have been granted to the principal. The `GrantedAuthority` objects are inserted into the `Authentication` object by the `AuthenticationManager` and are later read by `AuthorizationManager` instances when making authorization decisions.

The `GrantedAuthority` interface has only one method:

`String getAuthority();`

This method is used by an `AuthorizationManager` instance to obtain a precise `String` representation of the `GrantedAuthority`. By returning a representation as a `String`, a `GrantedAuthority` can be easily "read" by most `AuthorizationManager` implementations. If a `GrantedAuthority` cannot be precisely represented as a `String`, the `GrantedAuthority` is considered "complex" and `getAuthority()` must return `null`.

An example of a complex `GrantedAuthority` would be an implementation that stores a list of operations and authority thresholds that apply to different customer account numbers. Representing this complex `GrantedAuthority` as a `String` would be quite difficult. As a result, the `getAuthority()` method should return `null`. This indicates to any `AuthorizationManager` that it needs to support the specific `GrantedAuthority` implementation to understand its contents.

Spring Security includes one concrete `GrantedAuthority` implementation: `SimpleGrantedAuthority`. This implementation lets any user-specified `String` be converted into a `GrantedAuthority`. All `AuthenticationProvider` instances included with the security architecture use `SimpleGrantedAuthority` to populate the `Authentication` object.

By default, role-based authorization rules include `ROLE_` as a prefix. This means that if there is an authorization rule that requires a security context to have a role of "USER", Spring Security will by default look for a `GrantedAuthority#getAuthority` that returns "ROLE_USER".

You can customize this with `GrantedAuthorityDefaults`. `GrantedAuthorityDefaults` exists to allow customizing the prefix to use for role-based authorization rules.

You can configure the authorization rules to use a different prefix by exposing a `GrantedAuthorityDefaults` bean, like so:

Custom MethodSecurityExpressionHandler

*   Java

*   Kotlin

*   Xml

```
@Bean
static GrantedAuthorityDefaults grantedAuthorityDefaults() {
	return new GrantedAuthorityDefaults("MYPREFIX_");
}
```

You expose `GrantedAuthorityDefaults` using a `static` method to ensure that Spring publishes it before it initializes Spring Security’s method security `@Configuration` classes

[](https://docs.spring.io/spring-security/reference/servlet/authorization/architecture.html#authz-pre-invocation)Invocation Handling
------------------------------------------------------------------------------------------------------------------------------------

Spring Security provides interceptors that control access to secure objects, such as method invocations or web requests. A pre-invocation decision on whether the invocation is allowed to proceed is made by `AuthorizationManager` instances. Also post-invocation decisions on whether a given value may be returned is made by `AuthorizationManager` instances.

### [](https://docs.spring.io/spring-security/reference/servlet/authorization/architecture.html#_the_authorizationmanager)The AuthorizationManager

`AuthorizationManager` supersedes both [`AccessDecisionManager` and `AccessDecisionVoter`](https://docs.spring.io/spring-security/reference/servlet/authorization/architecture.html#authz-legacy-note).

Applications that customize an `AccessDecisionManager` or `AccessDecisionVoter` are encouraged to [change to using `AuthorizationManager`](https://docs.spring.io/spring-security/reference/servlet/authorization/architecture.html#authz-voter-adaptation).

`AuthorizationManager`s are called by Spring Security’s [request-based](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html), [method-based](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html), and [message-based](https://docs.spring.io/spring-security/reference/servlet/integrations/websocket.html) authorization components and are responsible for making final access control decisions. The `AuthorizationManager` interface contains two methods:

```
AuthorizationResult authorize(Supplier<Authentication> authentication, Object secureObject);

default void verify(Supplier<Authentication> authentication, Object secureObject)
        throws AccessDeniedException {
    // ...
}
```

The `AuthorizationManager`'s `authorize` method is passed all the relevant information it needs in order to make an authorization decision. In particular, passing the secure `Object` enables those arguments contained in the actual secure object invocation to be inspected. For example, let’s assume the secure object was a `MethodInvocation`. It would be easy to query the `MethodInvocation` for any `Customer` argument, and then implement some sort of security logic in the `AuthorizationManager` to ensure the principal is permitted to operate on that customer. Implementations are expected to return a positive `AuthorizationDecision` if access is granted, negative `AuthorizationDecision` if access is denied, and a null `AuthorizationDecision` when abstaining from making a decision.

`verify` calls `authorize` and subsequently throws an `AccessDeniedException` in the case of a negative `AuthorizationDecision`.

### [](https://docs.spring.io/spring-security/reference/servlet/authorization/architecture.html#authz-delegate-authorization-manager)Delegate-based AuthorizationManager Implementations

Whilst users can implement their own `AuthorizationManager` to control all aspects of authorization, Spring Security ships with a delegating `AuthorizationManager` that can collaborate with individual `AuthorizationManager`s.

`RequestMatcherDelegatingAuthorizationManager` will match the request with the most appropriate delegate `AuthorizationManager`. For method security, you can use `AuthorizationManagerBeforeMethodInterceptor` and `AuthorizationManagerAfterMethodInterceptor`.

[Authorization Manager Implementations](https://docs.spring.io/spring-security/reference/servlet/authorization/architecture.html#authz-authorization-manager-implementations) illustrates the relevant classes.

![Image 1: authorizationhierarchy](https://docs.spring.io/spring-security/reference/_images/servlet/authorization/authorizationhierarchy.png)

Figure 1. Authorization Manager Implementations

Using this approach, a composition of `AuthorizationManager` implementations can be polled on an authorization decision.

#### [](https://docs.spring.io/spring-security/reference/servlet/authorization/architecture.html#authz-authority-authorization-manager)AuthorityAuthorizationManager

The most common `AuthorizationManager` provided with Spring Security is `AuthorityAuthorizationManager`. It is configured with a given set of authorities to look for on the current `Authentication`. It will return positive `AuthorizationDecision` should the `Authentication` contain any of the configured authorities. It will return a negative `AuthorizationDecision` otherwise.

#### [](https://docs.spring.io/spring-security/reference/servlet/authorization/architecture.html#authz-authenticated-authorization-manager)AuthenticatedAuthorizationManager

Another manager is the `AuthenticatedAuthorizationManager`. It can be used to differentiate between anonymous, fully-authenticated and remember-me authenticated users. Many sites allow certain limited access under remember-me authentication, but require a user to confirm their identity by logging in for full access.

### [](https://docs.spring.io/spring-security/reference/servlet/authorization/architecture.html#authz-authorization-manager-factory)Creating AuthorizationManager instances

The [`AuthorizationManagerFactory`](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/authorization/AuthorizationManagerFactory.html) interface (introduced in Spring Security 7.0) is used to create generic `AuthorizationManager`s in [request-based](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html) and [method-based](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html) authorization components. The following is a sketch of the `AuthorizationManagerFactory` interface:

```
public interface AuthorizationManagerFactory<T> {
	AuthorizationManager<T> permitAll();
	AuthorizationManager<T> denyAll();
	AuthorizationManager<T> hasRole(String role);
	AuthorizationManager<T> hasAnyRole(String... roles);
	AuthorizationManager<T> hasAllRoles(String... roles);
	AuthorizationManager<T> hasAuthority(String authority);
	AuthorizationManager<T> hasAnyAuthority(String... authorities);
	AuthorizationManager<T> hasAllAuthorities(String... authorities);
	AuthorizationManager<T> authenticated();
	AuthorizationManager<T> fullyAuthenticated();
	AuthorizationManager<T> rememberMe();
	AuthorizationManager<T> anonymous();
}
```

The default implementation is [`DefaultAuthorizationManagerFactory`](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/authorization/DefaultAuthorizationManagerFactory.html), which allows for customizing the `rolePrefix` (defaults to `"ROLE_"`), `RoleHierarchy` and `AuthenticationTrustManager` that are provided to the `AuthorizationManager`s created by the factory.

In order to customize the default instance used by Spring Security, simply publish a bean as in the following example:

*   Java

*   Kotlin

*   Xml

```
@Bean
<T> AuthorizationManagerFactory<T> authorizationManagerFactory() {
	DefaultAuthorizationManagerFactory<T> authorizationManagerFactory =
			new DefaultAuthorizationManagerFactory<>();
	authorizationManagerFactory.setTrustResolver(getAuthenticationTrustResolver());
	authorizationManagerFactory.setRoleHierarchy(getRoleHierarchy());
	authorizationManagerFactory.setRolePrefix("role_");

	return authorizationManagerFactory;
}
```

It is also possible to target a specific usage of this factory within Spring Security by providing a concrete parameterized type instead of a generic type. See examples of each in the [request-based](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html#customizing-authorization-managers) and [method-based](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#customizing-authorization-managers) sections of the documentation.

In addition to simply customizing the default instance of `AuthorizationManagerFactory`, you can provide your own implementation to fully customize the instances created by the factory and provide your own implementations.

The [actual interface](https://github.com/spring-projects/spring-security/tree/7.0.3/core/src/main/java/org/springframework/security/authorization/AuthorizationManagerFactory.java) provides default implementations for all factory methods, which allows custom implementations to only implement the methods that need to be customized.

#### [](https://docs.spring.io/spring-security/reference/servlet/authorization/architecture.html#authz-authorization-managers)AuthorizationManagers

There are also helpful static factories in [`AuthorizationManagers`](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/authorization/AuthorizationManagers.html) for composing individual `AuthorizationManager`s into more sophisticated expressions.

#### [](https://docs.spring.io/spring-security/reference/servlet/authorization/architecture.html#authz-custom-authorization-manager)Custom Authorization Managers

Obviously, you can also implement a custom `AuthorizationManager` and you can put just about any access-control logic you want in it. It might be specific to your application (business-logic related) or it might implement some security administration logic. For example, you can create an implementation that can query Open Policy Agent or your own authorization database.

You’ll find a [blog article](https://spring.io/blog/2009/01/03/spring-security-customization-part-2-adjusting-secured-session-in-real-time) on the Spring web site which describes how to use the legacy `AccessDecisionVoter` to deny access in real-time to users whose accounts have been suspended. You can achieve the same outcome by implementing `AuthorizationManager` instead.

[](https://docs.spring.io/spring-security/reference/servlet/authorization/architecture.html#authz-voter-adaptation)Adapting AccessDecisionManager and AccessDecisionVoters
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Previous to `AuthorizationManager`, Spring Security published [`AccessDecisionManager` and `AccessDecisionVoter`](https://docs.spring.io/spring-security/reference/servlet/authorization/architecture.html#authz-legacy-note).

In some cases, like migrating an older application, it may be desirable to introduce an `AuthorizationManager` that invokes an `AccessDecisionManager` or `AccessDecisionVoter`.

To call an existing `AccessDecisionManager`, you can do:

Adapting an AccessDecisionManager

*   Java

```
@Component
public class AccessDecisionManagerAuthorizationManagerAdapter implements AuthorizationManager {
    private final AccessDecisionManager accessDecisionManager;
    private final SecurityMetadataSource securityMetadataSource;

    @Override
    public AuthorizationResult authorize(Supplier<Authentication> authentication, Object object) {
        try {
            Collection<ConfigAttribute> attributes = this.securityMetadataSource.getAttributes(object);
            this.accessDecisionManager.decide(authentication.get(), object, attributes);
            return new AuthorizationDecision(true);
        } catch (AccessDeniedException ex) {
            return new AuthorizationDecision(false);
        }
    }

    @Override
    public void verify(Supplier<Authentication> authentication, Object object) {
        Collection<ConfigAttribute> attributes = this.securityMetadataSource.getAttributes(object);
        this.accessDecisionManager.decide(authentication.get(), object, attributes);
    }
}
```

And then wire it into your `SecurityFilterChain`.

Or to only call an `AccessDecisionVoter`, you can do:

Adapting an AccessDecisionVoter

*   Java

```
@Component
public class AccessDecisionVoterAuthorizationManagerAdapter implements AuthorizationManager {
    private final AccessDecisionVoter accessDecisionVoter;
    private final SecurityMetadataSource securityMetadataSource;

    @Override
    public AuthorizationResult authorize(Supplier<Authentication> authentication, Object object) {
        Collection<ConfigAttribute> attributes = this.securityMetadataSource.getAttributes(object);
        int decision = this.accessDecisionVoter.vote(authentication.get(), object, attributes);
        switch (decision) {
        case ACCESS_GRANTED:
            return new AuthorizationDecision(true);
        case ACCESS_DENIED:
            return new AuthorizationDecision(false);
        }
        return null;
    }
}
```

And then wire it into your `SecurityFilterChain`.

[](https://docs.spring.io/spring-security/reference/servlet/authorization/architecture.html#authz-hierarchical-roles)Hierarchical Roles
---------------------------------------------------------------------------------------------------------------------------------------

It is a common requirement that a particular role in an application should automatically "include" other roles. For example, in an application which has the concept of an "admin" and a "user" role, you may want an admin to be able to do everything a normal user can. To achieve this, you can either make sure that all admin users are also assigned the "user" role. Alternatively, you can modify every access constraint which requires the "user" role to also include the "admin" role. This can get quite complicated if you have a lot of different roles in your application.

The use of a role-hierarchy allows you to configure which roles (or authorities) should include others. This is supported for filter-based authorization in `HttpSecurity#authorizeHttpRequests` and for method-based authorization through `DefaultMethodSecurityExpressionHandler` for pre-post annotations, `SecuredAuthorizationManager` for `@Secured`, and `Jsr250AuthorizationManager` for JSR-250 annotations. You can configure the behavior for all of them at once in the following way:

Hierarchical Roles Configuration

*   Java

*   Xml

```
@Bean
static RoleHierarchy roleHierarchy() {
    return RoleHierarchyImpl.withDefaultRolePrefix()
        .role("ADMIN").implies("STAFF")
        .role("STAFF").implies("USER")
        .role("USER").implies("GUEST")
        .build();
}

// and, if using pre-post method security also add
@Bean
static MethodSecurityExpressionHandler methodSecurityExpressionHandler(RoleHierarchy roleHierarchy) {
	DefaultMethodSecurityExpressionHandler expressionHandler = new DefaultMethodSecurityExpressionHandler();
	expressionHandler.setRoleHierarchy(roleHierarchy);
	return expressionHandler;
}
```

Here we have four roles in a hierarchy `ROLE_ADMIN ⇒ ROLE_STAFF ⇒ ROLE_USER ⇒ ROLE_GUEST`. A user who is authenticated with `ROLE_ADMIN`, will behave as if they have all four roles when security constraints are evaluated against any filter- or method-based rules.

The `>` symbol can be thought of as meaning "includes".

Role hierarchies offer a convenient means of simplifying the access-control configuration data for your application and/or reducing the number of authorities which you need to assign to a user. For more complex requirements you may wish to define a logical mapping between the specific access-rights your application requires and the roles that are assigned to users, translating between the two when loading the user information.

[](https://docs.spring.io/spring-security/reference/servlet/authorization/architecture.html#authz-legacy-note)Legacy Authorization Components
---------------------------------------------------------------------------------------------------------------------------------------------

Spring Security contains some legacy components. Since they are not yet removed, documentation is included for historical purposes. Their recommended replacements are above.

When accessing legacy authorization components, please also include the `spring-security-access` dependency like so:

*   Maven

*   Gradle

```
<dependency>
    <groupId>org.springframework.security</groupId>
    <artifactId>spring-security-access</artifactId>
</dependency>
```

### [](https://docs.spring.io/spring-security/reference/servlet/authorization/architecture.html#authz-access-decision-manager)The AccessDecisionManager

The `AccessDecisionManager` is called by the `AbstractSecurityInterceptor` and is responsible for making final access control decisions. The `AccessDecisionManager` interface contains three methods:

```
void decide(Authentication authentication, Object secureObject,
	Collection<ConfigAttribute> attrs) throws AccessDeniedException;

boolean supports(ConfigAttribute attribute);

boolean supports(Class clazz);
```

The `decide` method of the `AccessDecisionManager` is passed all the relevant information it needs to make an authorization decision. In particular, passing the secure `Object` lets those arguments contained in the actual secure object invocation be inspected. For example, assume the secure object is a `MethodInvocation`. You can query the `MethodInvocation` for any `Customer` argument and then implement some sort of security logic in the `AccessDecisionManager` to ensure the principal is permitted to operate on that customer. Implementations are expected to throw an `AccessDeniedException` if access is denied.

The `supports(ConfigAttribute)` method is called by the `AbstractSecurityInterceptor` at startup time to determine if the `AccessDecisionManager` can process the passed `ConfigAttribute`. The `supports(Class)` method is called by a security interceptor implementation to ensure the configured `AccessDecisionManager` supports the type of secure object that the security interceptor presents.

### [](https://docs.spring.io/spring-security/reference/servlet/authorization/architecture.html#authz-voting-based)Voting-Based AccessDecisionManager Implementations

While users can implement their own `AccessDecisionManager` to control all aspects of authorization, Spring Security includes several `AccessDecisionManager` implementations that are based on voting. [Voting Decision Manager](https://docs.spring.io/spring-security/reference/servlet/authorization/architecture.html#authz-access-voting) describes the relevant classes.

The following image shows the `AccessDecisionManager` interface:

![Image 2: access decision voting](https://docs.spring.io/spring-security/reference/_images/servlet/authorization/access-decision-voting.png)

Figure 2. Voting Decision Manager

By using this approach, a series of `AccessDecisionVoter` implementations are polled on an authorization decision. The `AccessDecisionManager` then decides whether or not to throw an `AccessDeniedException` based on its assessment of the votes.

The `AccessDecisionVoter` interface has three methods:

```
int vote(Authentication authentication, Object object, Collection<ConfigAttribute> attrs);

boolean supports(ConfigAttribute attribute);

boolean supports(Class clazz);
```

Concrete implementations return an `int`, with possible values being reflected in the `AccessDecisionVoter` static fields named `ACCESS_ABSTAIN`, `ACCESS_DENIED` and `ACCESS_GRANTED`. A voting implementation returns `ACCESS_ABSTAIN` if it has no opinion on an authorization decision. If it does have an opinion, it must return either `ACCESS_DENIED` or `ACCESS_GRANTED`.

There are three concrete `AccessDecisionManager` implementations provided with Spring Security to tally the votes. The `ConsensusBased` implementation grants or denies access based on the consensus of non-abstain votes. Properties are provided to control behavior in the event of an equality of votes or if all votes are abstain. The `AffirmativeBased` implementation grants access if one or more `ACCESS_GRANTED` votes were received (in other words, a deny vote will be ignored, provided there was at least one grant vote). Like the `ConsensusBased` implementation, there is a parameter that controls the behavior if all voters abstain. The `UnanimousBased` provider expects unanimous `ACCESS_GRANTED` votes in order to grant access, ignoring abstains. It denies access if there is any `ACCESS_DENIED` vote. Like the other implementations, there is a parameter that controls the behavior if all voters abstain.

You can implement a custom `AccessDecisionManager` that tallies votes differently. For example, votes from a particular `AccessDecisionVoter` might receive additional weighting, while a deny vote from a particular voter may have a veto effect.

#### [](https://docs.spring.io/spring-security/reference/servlet/authorization/architecture.html#authz-role-voter)RoleVoter

The most commonly used `AccessDecisionVoter` provided with Spring Security is the `RoleVoter`, which treats configuration attributes as role names and votes to grant access if the user has been assigned that role.

It votes if any `ConfigAttribute` begins with the `ROLE_` prefix. It votes to grant access if there is a `GrantedAuthority` that returns a `String` representation (from the `getAuthority()` method) exactly equal to one or more `ConfigAttributes` that start with the `ROLE_` prefix. If there is no exact match of any `ConfigAttribute` starting with `ROLE_`, `RoleVoter` votes to deny access. If no `ConfigAttribute` begins with `ROLE_`, the voter abstains.

#### [](https://docs.spring.io/spring-security/reference/servlet/authorization/architecture.html#authz-authenticated-voter)AuthenticatedVoter

Another voter which we have implicitly seen is the `AuthenticatedVoter`, which can be used to differentiate between anonymous, fully-authenticated, and remember-me authenticated users. Many sites allow certain limited access under remember-me authentication but require a user to confirm their identity by logging in for full access.

When we have used the `IS_AUTHENTICATED_ANONYMOUSLY` attribute to grant anonymous access, this attribute was being processed by the `AuthenticatedVoter`. For more information, see [`AuthenticatedVoter`](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/access/vote/AuthenticatedVoter.html).

#### [](https://docs.spring.io/spring-security/reference/servlet/authorization/architecture.html#authz-custom-voter)Custom Voters

You can also implement a custom `AccessDecisionVoter` and put just about any access-control logic you want in it. It might be specific to your application (business-logic related) or it might implement some security administration logic. For example, on the Spring web site, you can find a [blog article](https://spring.io/blog/2009/01/03/spring-security-customization-part-2-adjusting-secured-session-in-real-time) that describes how to use a voter to deny access in real-time to users whose accounts have been suspended.

![Image 3: after invocation](https://docs.spring.io/spring-security/reference/_images/servlet/authorization/after-invocation.png)

Figure 3. After Invocation Implementation

Like many other parts of Spring Security, `AfterInvocationManager` has a single concrete implementation, `AfterInvocationProviderManager`, which polls a list of `AfterInvocationProvider`s. Each `AfterInvocationProvider` is allowed to modify the return object or throw an `AccessDeniedException`. Indeed multiple providers can modify the object, as the result of the previous provider is passed to the next in the list.

Please be aware that if you’re using `AfterInvocationManager`, you will still need configuration attributes that allow the `MethodSecurityInterceptor`'s `AccessDecisionManager` to allow an operation. If you’re using the typical Spring Security included `AccessDecisionManager` implementations, having no configuration attributes defined for a particular secure method invocation will cause each `AccessDecisionVoter` to abstain from voting. In turn, if the `AccessDecisionManager` property “allowIfAllAbstainDecisions” is `false`, an `AccessDeniedException` will be thrown. You may avoid this potential issue by either (i) setting “allowIfAllAbstainDecisions” to `true` (although this is generally not recommended) or (ii) simply ensure that there is at least one configuration attribute that an `AccessDecisionVoter` will vote to grant access for. This latter (recommended) approach is usually achieved through a `ROLE_USER` or `ROLE_AUTHENTICATED` configuration attribute.
