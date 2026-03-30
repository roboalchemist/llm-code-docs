# Source: https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html

Title: Method Security :: Spring Security

URL Source: https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html

Published Time: Mon, 09 Mar 2026 15:09:15 GMT

Markdown Content:
You can activate it in your application by annotating any `@Configuration` class with `@EnableMethodSecurity` or adding `<method-security>` to any XML configuration file, like so:

*   Java

*   Kotlin

*   Xml

`@EnableMethodSecurity`

Then, you are immediately able to annotate any Spring-managed class or method with [`@PreAuthorize`](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#use-preauthorize), [`@PostAuthorize`](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#use-postauthorize), [`@PreFilter`](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#use-prefilter), and [`@PostFilter`](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#use-postfilter) to authorize method invocations, including the input parameters and return values.

Method Security supports many other use cases as well including [AspectJ support](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#use-aspectj), [custom annotations](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#use-programmatic-authorization), and several configuration points. Consider learning about the following use cases:

*   [Migrating from `@EnableGlobalMethodSecurity`](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#migration-enableglobalmethodsecurity)

*   Understanding [how method security works](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#method-security-architecture) and reasons to use it

*   Comparing [request-level and method-level authorization](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#request-vs-method)

*   Authorizing methods with [`@PreAuthorize`](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#use-preauthorize) and [`@PostAuthorize`](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#use-postauthorize)

*   Providing [fallback values when authorization is denied](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#fallback-values-authorization-denied)

*   Filtering methods with [`@PreFilter`](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#use-prefilter) and [`@PostFilter`](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#use-postfilter)

*   Authorizing methods with [JSR-250 annotations](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#use-jsr250)

*   Authorizing methods with [AspectJ expressions](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#use-aspectj)

*   Integrating with [AspectJ byte-code weaving](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#weave-aspectj)

*   Coordinating with [@Transactional and other AOP-based annotations](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#changing-the-order)

*   Customizing [SpEL expression handling](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#customizing-expression-handling)

*   Integrating with [custom authorization systems](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#custom-authorization-managers)

[](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#method-security-architecture)How Method Security Works
-----------------------------------------------------------------------------------------------------------------------------------------------------

Spring Security’s method authorization support is handy for:

*   Extracting fine-grained authorization logic; for example, when the method parameters and return values contribute to the authorization decision.

*   Enforcing security at the service layer

*   Stylistically favoring annotation-based over `HttpSecurity`-based configuration

And since Method Security is built using [Spring AOP](https://docs.spring.io/spring-framework/reference/7.0.4/core.html#aop-api), you have access to all its expressive power to override Spring Security’s defaults as needed.

As already mentioned, you begin by adding `@EnableMethodSecurity` to a `@Configuration` class or `<sec:method-security/>` in a Spring XML configuration file.

This annotation and XML element supercede `@EnableGlobalMethodSecurity` and `<sec:global-method-security/>`, respectively. They offer the following improvements:

1.   Uses the simplified `AuthorizationManager` API instead of metadata sources, config attributes, decision managers, and voters. This simplifies reuse and customization.

2.   Favors direct bean-based configuration, instead of requiring extending `GlobalMethodSecurityConfiguration` to customize beans

3.   Is built using native Spring AOP, removing abstractions and allowing you to use Spring AOP building blocks to customize

4.   Checks for conflicting annotations to ensure an unambiguous security configuration

5.   Complies with JSR-250

6.   Enables `@PreAuthorize`, `@PostAuthorize`, `@PreFilter`, and `@PostFilter` by default

If you are using `@EnableGlobalMethodSecurity` or `<global-method-security/>`, these are now deprecated, and you are encouraged to migrate.

Method authorization is a combination of before- and after-method authorization. Consider a service bean that is annotated in the following way:

*   Java

*   Kotlin

```
@Service
public class MyCustomerService {
    @PreAuthorize("hasAuthority('permission:read')")
    @PostAuthorize("returnObject.owner == authentication.name")
    public Customer readCustomer(String id) { ... }
}
```

A given invocation to `MyCustomerService#readCustomer` may look something like this when Method Security [is activated](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#activate-method-security):

![Image 1: methodsecurity](https://docs.spring.io/spring-security/reference/_images/servlet/authorization/methodsecurity.png)

1.   Spring AOP invokes its proxy method for `readCustomer`. Among the proxy’s other advisors, it invokes an [`AuthorizationManagerBeforeMethodInterceptor`](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/authorization/method/AuthorizationManagerBeforeMethodInterceptor.html) that matches [the `@PreAuthorize` pointcut](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#annotation-method-pointcuts)

2.   The interceptor invokes [`PreAuthorizeAuthorizationManager#authorize`](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/authorization/method/PreAuthorizeAuthorizationManager.html)

3.   The authorization manager uses a `MethodSecurityExpressionHandler` to parse the annotation’s [SpEL expression](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#authorization-expressions) and constructs a corresponding `EvaluationContext` from a `MethodSecurityExpressionRoot` containing [a `Supplier<Authentication>`](https://docs.spring.io/spring-security/reference/servlet/authentication/architecture.html#servlet-authentication-authentication) and `MethodInvocation`.

4.   The interceptor uses this context to evaluate the expression; specifically, it reads [the `Authentication`](https://docs.spring.io/spring-security/reference/servlet/authentication/architecture.html#servlet-authentication-authentication) from the `Supplier` and checks whether it has `permission:read` in its collection of [authorities](https://docs.spring.io/spring-security/reference/servlet/authorization/architecture.html#authz-authorities)

5.   If the evaluation passes, then Spring AOP proceeds to invoke the method.

6.   If not, the interceptor publishes an `AuthorizationDeniedEvent` and throws an [`AccessDeniedException`](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/access/AccessDeniedException.html) which [the `ExceptionTranslationFilter`](https://docs.spring.io/spring-security/reference/servlet/architecture.html#servlet-exceptiontranslationfilter) catches and returns a 403 status code to the response

7.   After the method returns, Spring AOP invokes an [`AuthorizationManagerAfterMethodInterceptor`](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/authorization/method/AuthorizationManagerAfterMethodInterceptor.html) that matches [the `@PostAuthorize` pointcut](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#annotation-method-pointcuts), operating the same as above, but with [`PostAuthorizeAuthorizationManager`](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/authorization/method/PostAuthorizeAuthorizationManager.html)

8.   If the evaluation passes (in this case, the return value belongs to the logged-in user), processing continues normally

9.   If not, the interceptor publishes an `AuthorizationDeniedEvent` and throws an [`AccessDeniedException`](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/access/AccessDeniedException.html), which [the `ExceptionTranslationFilter`](https://docs.spring.io/spring-security/reference/servlet/architecture.html#servlet-exceptiontranslationfilter) catches and returns a 403 status code to the response

If the method is not being called in the context of an HTTP request, you will likely need to handle the `AccessDeniedException` yourself

As demonstrated above, if a method invocation involves multiple [Method Security annotations](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#authorizing-with-annotations), each of those is processed one at a time. This means that they can collectively be thought of as being "anded" together. In other words, for an invocation to be authorized, all annotation inspections need to pass authorization.

### [](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#repeated-annotations)Repeated Annotations Are Not Supported

That said, it is not supported to repeat the same annotation on the same method. For example, you cannot place `@PreAuthorize` twice on the same method.

Instead, use SpEL’s boolean support or its support for delegating to a separate bean.

### [](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#annotation-method-pointcuts)Each Annotation Has Its Own Pointcut

Each annotation has its own pointcut instance that looks for that annotation or its [meta-annotation](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#meta-annotations) counterparts across the entire object hierarchy, starting at [the method and its enclosing class](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#class-or-interface-annotations).

### [](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#annotation-method-interceptors)Each Annotation Has Its Own Method Interceptor

Each annotation has its own dedicated method interceptor. The reason for this is to make things more composable. For example, if needed, you can disable the Spring Security defaults and [publish only the `@PostAuthorize` method interceptor](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#_enabling_certain_annotations).

The method interceptors are as follows:

*   For [`@PreAuthorize`](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#use-preauthorize), Spring Security uses [`AuthorizationManagerBeforeMethodInterceptor#preAuthorize`](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/authorization/method/AuthorizationManagerBeforeMethodInterceptor.html), which in turn uses [`PreAuthorizeAuthorizationManager`](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/authorization/method/PreAuthorizeAuthorizationManager.html)

*   For [`@PostAuthorize`](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#use-postauthorize), Spring Security uses [`AuthorizationManagerAfterMethodInterceptor#postAuthorize`](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/authorization/method/AuthorizationManagerAfterMethodInterceptor.html), which in turn uses [`PostAuthorizeAuthorizationManager`](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/authorization/method/PostAuthorizeAuthorizationManager.html)

*   For [`@PreFilter`](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#use-prefilter), Spring Security uses [`PreFilterAuthorizationMethodInterceptor`](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/authorization/method/PreFilterAuthorizationMethodInterceptor.html)

*   For [`@PostFilter`](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#use-postfilter), Spring Security uses [`PostFilterAuthorizationMethodInterceptor`](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/authorization/method/PostFilterAuthorizationMethodInterceptor.html)

*   For [`@Secured`](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#use-secured), Spring Security uses [`AuthorizationManagerBeforeMethodInterceptor#secured`](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/authorization/method/AuthorizationManagerBeforeMethodInterceptor.html), which in turn uses [`SecuredAuthorizationManager`](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/authorization/method/SecuredAuthorizationManager.html)

*   For JSR-250 annotations, Spring Security uses [`AuthorizationManagerBeforeMethodInterceptor#jsr250`](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/authorization/method/AuthorizationManagerBeforeMethodInterceptor.html), which in turn uses [`Jsr250AuthorizationManager`](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/authorization/method/Jsr250AuthorizationManager.html)

Generally speaking, you can consider the following listing as representative of what interceptors Spring Security publishes when you add `@EnableMethodSecurity`:

*   Java

```
@Bean
@Role(BeanDefinition.ROLE_INFRASTRUCTURE)
static Advisor preAuthorizeMethodInterceptor() {
    return AuthorizationManagerBeforeMethodInterceptor.preAuthorize();
}

@Bean
@Role(BeanDefinition.ROLE_INFRASTRUCTURE)
static Advisor postAuthorizeMethodInterceptor() {
    return AuthorizationManagerAfterMethodInterceptor.postAuthorize();
}

@Bean
@Role(BeanDefinition.ROLE_INFRASTRUCTURE)
static Advisor preFilterMethodInterceptor() {
    return AuthorizationManagerBeforeMethodInterceptor.preFilter();
}

@Bean
@Role(BeanDefinition.ROLE_INFRASTRUCTURE)
static Advisor postFilterMethodInterceptor() {
    return AuthorizationManagerAfterMethodInterceptor.postFilter();
}
```

### [](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#favor-granting-authorities)Favor Granting Authorities Over Complicated SpEL Expressions

Quite often it can be tempting to introduce a complicated SpEL expression like the following:

*   Java

*   Kotlin

`@PreAuthorize("hasAuthority('permission:read') || hasRole('ADMIN')")`

However, you could instead grant `permission:read` to those with `ROLE_ADMIN`. One way to do this is with a `RoleHierarchy` like so:

*   Java

*   Kotlin

*   Xml

```
@Bean
static RoleHierarchy roleHierarchy() {
    return RoleHierarchyImpl.fromHierarchy("ROLE_ADMIN > permission:read");
}
```

and then [set that in a `MethodSecurityExpressionHandler` instance](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#customizing-expression-handling). This then allows you to have a simpler [`@PreAuthorize`](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#use-preauthorize) expression like this one:

*   Java

*   Kotlin

`@PreAuthorize("hasAuthority('permission:read')")`

Or, where possible, adapt application-specific authorization logic into granted authorities at login time.

[](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#request-vs-method)Comparing Request-level vs Method-level Authorization
----------------------------------------------------------------------------------------------------------------------------------------------------------------------

When should you favor method-level authorization over [request-level authorization](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html)? Some of it comes down to taste; however, consider the following strengths list of each to help you decide.

**request-level****method-level**
**authorization type**coarse-grained fine-grained
**configuration location**declared in a config class local to method declaration
**configuration style**DSL Annotations
**authorization definitions**programmatic SpEL

The main tradeoff seems to be where you want your authorization rules to live.

It’s important to remember that when you use annotation-based Method Security, then unannotated methods are not secured. To protect against this, declare [a catch-all authorization rule](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html#activate-request-security) in your [`HttpSecurity`](https://docs.spring.io/spring-security/reference/servlet/configuration/java.html#jc-httpsecurity) instance.

[](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#authorizing-with-annotations)Authorizing with Annotations
--------------------------------------------------------------------------------------------------------------------------------------------------------

The primary way Spring Security enables method-level authorization support is through annotations that you can add to methods, classes, and interfaces.

### [](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#use-preauthorize)Authorizing Method Invocation with `@PreAuthorize`

When [Method Security is active](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#activate-method-security), you can annotate a method with the [`@PreAuthorize`](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/access/prepost/PreAuthorize.html) annotation like so:

*   Java

*   Kotlin

```
@Component
public class BankService {
	@PreAuthorize("hasRole('ADMIN')")
	public Account readAccount(Long id) {
        // ... is only invoked if the `Authentication` has the `ROLE_ADMIN` authority
	}
}
```

This is meant to indicate that the method can only be invoked if the provided expression `hasRole('ADMIN')` passes.

You can then [test the class](https://docs.spring.io/spring-security/reference/servlet/test/method.html) to confirm it is enforcing the authorization rule like so:

*   Java

*   Kotlin

```
@Autowired
BankService bankService;

@WithMockUser(roles="ADMIN")
@Test
void readAccountWithAdminRoleThenInvokes() {
    Account account = this.bankService.readAccount("12345678");
    // ... assertions
}

@WithMockUser(roles="WRONG")
@Test
void readAccountWithWrongRoleThenAccessDenied() {
    assertThatExceptionOfType(AccessDeniedException.class).isThrownBy(
        () -> this.bankService.readAccount("12345678"));
}
```

`@PreAuthorize` also can be a [meta-annotation](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#meta-annotations), be defined [at the class or interface level](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#class-or-interface-annotations), and use [SpEL Authorization Expressions](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#authorization-expressions).

While `@PreAuthorize` is quite helpful for declaring needed authorities, it can also be used to evaluate more complex [expressions that involve the method parameters](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#using_method_parameters).

### [](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#use-postauthorize)Authorization Method Results with `@PostAuthorize`

When Method Security is active, you can annotate a method with the [`@PostAuthorize`](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/access/prepost/PostAuthorize.html) annotation like so:

*   Java

*   Kotlin

```
@Component
public class BankService {
	@PostAuthorize("returnObject.owner == authentication.name")
	public Account readAccount(Long id) {
        // ... is only returned if the `Account` belongs to the logged in user
	}
}
```

This is meant to indicate that the method can only return the value if the provided expression `returnObject.owner == authentication.name` passes. `returnObject` represents the `Account` object to be returned.

You can then [test the class](https://docs.spring.io/spring-security/reference/servlet/test/method.html) to confirm it is enforcing the authorization rule:

*   Java

*   Kotlin

```
@Autowired
BankService bankService;

@WithMockUser(username="owner")
@Test
void readAccountWhenOwnedThenReturns() {
    Account account = this.bankService.readAccount("12345678");
    // ... assertions
}

@WithMockUser(username="wrong")
@Test
void readAccountWhenNotOwnedThenAccessDenied() {
    assertThatExceptionOfType(AccessDeniedException.class).isThrownBy(
        () -> this.bankService.readAccount("12345678"));
}
```

`@PostAuthorize` also can be a [meta-annotation](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#meta-annotations), be defined [at the class or interface level](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#class-or-interface-annotations), and use [SpEL Authorization Expressions](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#authorization-expressions).

`@PostAuthorize` is particularly helpful when defending against [Insecure Direct Object Reference](https://cheatsheetseries.owasp.org/cheatsheets/Insecure_Direct_Object_Reference_Prevention_Cheat_Sheet.html). In fact, it can be defined as a [meta-annotation](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#meta-annotations) like so:

*   Java

*   Kotlin

```
@Target({ ElementType.METHOD, ElementType.TYPE })
@Retention(RetentionPolicy.RUNTIME)
@PostAuthorize("returnObject.owner == authentication.name")
public @interface RequireOwnership {}
```

Allowing you to instead annotate the service in the following way:

*   Java

*   Kotlin

```
@Component
public class BankService {
	@RequireOwnership
	public Account readAccount(Long id) {
        // ... is only returned if the `Account` belongs to the logged in user
	}
}
```

The result is that the above method will only return the `Account` if its `owner` attribute matches the logged-in user’s `name`. If not, Spring Security will throw an `AccessDeniedException` and return a 403 status code.

Note that `@PostAuthorize` is not recommended for classes that perform database writes since that typically means that a database change was made before the security invariants were checked. A common example of doing this is if you have `@Transactional` and `@PostAuthorize` on the same method. Instead, read the value first, using `@PostAuthorize` on the read, and then perform the database write, should that read is authorized. If you must do something like this, you can [ensure that `@EnableTransactionManagement` comes before `@EnableMethodSecurity`](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#changing-the-order).

### [](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#use-prefilter)Filtering Method Parameters with `@PreFilter`

When Method Security is active, you can annotate a method with the [`@PreFilter`](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/access/prepost/PreFilter.html) annotation like so:

*   Java

*   Kotlin

```
@Component
public class BankService {
	@PreFilter("filterObject.owner == authentication.name")
	public Collection<Account> updateAccounts(Account... accounts) {
        // ... `accounts` will only contain the accounts owned by the logged-in user
        return updated;
	}
}
```

This is meant to filter out any values from `accounts` where the expression `filterObject.owner == authentication.name` fails. `filterObject` represents each `account` in `accounts` and is used to test each `account`.

You can then test the class in the following way to confirm it is enforcing the authorization rule:

*   Java

*   Kotlin

```
@Autowired
BankService bankService;

@WithMockUser(username="owner")
@Test
void updateAccountsWhenOwnedThenReturns() {
    Account ownedBy = ...
    Account notOwnedBy = ...
    Collection<Account> updated = this.bankService.updateAccounts(ownedBy, notOwnedBy);
    assertThat(updated).containsOnly(ownedBy);
}
```

`@PreFilter` also can be a [meta-annotation](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#meta-annotations), be defined [at the class or interface level](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#class-or-interface-annotations), and use [SpEL Authorization Expressions](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#authorization-expressions).

`@PreFilter` supports arrays, collections, maps, and streams (so long as the stream is still open).

For example, the above `updateAccounts` declaration will function the same way as the following other four:

*   Java

*   Kotlin

```
@PreFilter("filterObject.owner == authentication.name")
public Collection<Account> updateAccounts(Account[] accounts)

@PreFilter("filterObject.owner == authentication.name")
public Collection<Account> updateAccounts(Collection<Account> accounts)

@PreFilter("filterObject.value.owner == authentication.name")
public Collection<Account> updateAccounts(Map<String, Account> accounts)

@PreFilter("filterObject.owner == authentication.name")
public Collection<Account> updateAccounts(Stream<Account> accounts)
```

The result is that the above method will only have the `Account` instances where their `owner` attribute matches the logged-in user’s `name`.

### [](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#use-postfilter)Filtering Method Results with `@PostFilter`

When Method Security is active, you can annotate a method with the [`@PostFilter`](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/access/prepost/PostFilter.html) annotation like so:

*   Java

*   Kotlin

```
@Component
public class BankService {
	@PostFilter("filterObject.owner == authentication.name")
	public Collection<Account> readAccounts(String... ids) {
        // ... the return value will be filtered to only contain the accounts owned by the logged-in user
        return accounts;
	}
}
```

This is meant to filter out any values from the return value where the expression `filterObject.owner == authentication.name` fails. `filterObject` represents each `account` in `accounts` and is used to test each `account`.

You can then test the class like so to confirm it is enforcing the authorization rule:

*   Java

*   Kotlin

```
@Autowired
BankService bankService;

@WithMockUser(username="owner")
@Test
void readAccountsWhenOwnedThenReturns() {
    Collection<Account> accounts = this.bankService.updateAccounts("owner", "not-owner");
    assertThat(accounts).hasSize(1);
    assertThat(accounts.get(0).getOwner()).isEqualTo("owner");
}
```

`@PostFilter` also can be a [meta-annotation](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#meta-annotations), be defined [at the class or interface level](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#class-or-interface-annotations), and use [SpEL Authorization Expressions](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#authorization-expressions).

`@PostFilter` supports arrays, collections, maps, and streams (so long as the stream is still open).

For example, the above `readAccounts` declaration will function the same way as the following other three:

*   Java

*   Kotlin

```
@PostFilter("filterObject.owner == authentication.name")
public Collection<Account> readAccounts(String... ids)

@PostFilter("filterObject.owner == authentication.name")
public Account[] readAccounts(String... ids)

@PostFilter("filterObject.value.owner == authentication.name")
public Map<String, Account> readAccounts(String... ids)

@PostFilter("filterObject.owner == authentication.name")
public Stream<Account> readAccounts(String... ids)
```

The result is that the above method will return the `Account` instances where their `owner` attribute matches the logged-in user’s `name`.

### [](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#use-secured)Authorizing Method Invocation with `@Secured`

[`@Secured`](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/access/annotation/Secured.html) is a legacy option for authorizing invocations. [`@PreAuthorize`](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#use-preauthorize) supersedes it and is recommended instead.

To use the `@Secured` annotation, you should first change your Method Security declaration to enable it like so:

*   Java

*   Kotlin

*   Xml

`@EnableMethodSecurity(securedEnabled = true)`

This will cause Spring Security to publish [the corresponding method interceptor](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#annotation-method-interceptors) that authorizes methods, classes, and interfaces annotated with `@Secured`.

### [](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#use-jsr250)Authorizing Method Invocation with JSR-250 Annotations

In case you would like to use [JSR-250](https://jcp.org/en/jsr/detail?id=250) annotations, Spring Security also supports that. [`@PreAuthorize`](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#use-preauthorize) has more expressive power and is thus recommended.

To use the JSR-250 annotations, you should first change your Method Security declaration to enable them like so:

*   Java

*   Kotlin

*   Xml

`@EnableMethodSecurity(jsr250Enabled = true)`

This will cause Spring Security to publish [the corresponding method interceptor](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#annotation-method-interceptors) that authorizes methods, classes, and interfaces annotated with `@RolesAllowed`, `@PermitAll`, and `@DenyAll`.

### [](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#class-or-interface-annotations)Declaring Annotations at the Class or Interface Level

It’s also supported to have Method Security annotations at the class and interface level.

If it is at the class level like so:

*   Java

*   Kotlin

```
@Controller
@PreAuthorize("hasAuthority('ROLE_USER')")
public class MyController {
    @GetMapping("/endpoint")
    public String endpoint() { ... }
}
```

then all methods inherit the class-level behavior.

Or, if it’s declared like the following at both the class and method level:

*   Java

*   Kotlin

```
@Controller
@PreAuthorize("hasAuthority('ROLE_USER')")
public class MyController {
    @GetMapping("/endpoint")
    @PreAuthorize("hasAuthority('ROLE_ADMIN')")
    public String endpoint() { ... }
}
```

then methods declaring the annotation override the class-level annotation.

The same is true for interfaces, with the exception that if a class inherits the annotation from two different interfaces, then startup will fail. This is because Spring Security has no way to tell which one you want to use.

In cases like this, you can resolve the ambiguity by adding the annotation to the concrete method.

### [](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#meta-annotations)Using Meta Annotations

Method Security supports meta annotations. This means that you can take any annotation and improve readability based on your application-specific use cases.

For example, you can simplify `@PreAuthorize("hasRole('ADMIN')")` to `@IsAdmin` like so:

*   Java

*   Kotlin

```
@Target({ ElementType.METHOD, ElementType.TYPE })
@Retention(RetentionPolicy.RUNTIME)
@PreAuthorize("hasRole('ADMIN')")
public @interface IsAdmin {}
```

And the result is that on your secured methods you can now do the following instead:

*   Java

*   Kotlin

```
@Component
public class BankService {
	@IsAdmin
	public Account readAccount(Long id) {
        // ... is only returned if the `Account` belongs to the logged in user
	}
}
```

This results in more readable method definitions.

#### [](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#_templating_meta_annotation_expressions)Templating Meta-Annotation Expressions

You can also opt into using meta-annotation templates, which allow for much more powerful annotation definitions.

First, publish the following bean:

*   Java

*   Kotlin

```
@Bean
static AnnotationTemplateExpressionDefaults templateExpressionDefaults() {
	return new AnnotationTemplateExpressionDefaults();
}
```

Now instead of `@IsAdmin`, you can create something more powerful like `@HasRole` like so:

*   Java

*   Kotlin

```
@Target({ ElementType.METHOD, ElementType.TYPE })
@Retention(RetentionPolicy.RUNTIME)
@PreAuthorize("hasRole('{value}')")
public @interface HasRole {
	String value();
}
```

And the result is that on your secured methods you can now do the following instead:

*   Java

*   Kotlin

```
@Component
public class BankService {
	@HasRole("ADMIN")
	public Account readAccount(Long id) {
        // ... is only returned if the `Account` belongs to the logged in user
	}
}
```

Note that this works with method variables and all annotation types, too, though you will want to be careful to correctly take care of quotation marks so the resulting SpEL expression is correct.

For example, consider the following `@HasAnyRole` annotation:

*   Java

*   Kotlin

```
@Target({ ElementType.METHOD, ElementType.TYPE })
@Retention(RetentionPolicy.RUNTIME)
@PreAuthorize("hasAnyRole({roles})")
public @interface HasAnyRole {
	String[] roles();
}
```

In that case, you’ll notice that you should not use the quotation marks in the expression, but instead in the parameter value like so:

*   Java

*   Kotlin

```
@Component
public class BankService {
	@HasAnyRole(roles = { "'USER'", "'ADMIN'" })
	public Account readAccount(Long id) {
        // ... is only returned if the `Account` belongs to the logged in user
	}
}
```

so that, once replaced, the expression becomes `@PreAuthorize("hasAnyRole('USER', 'ADMIN')")`.

### [](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#enable-annotation)Enabling Certain Annotations

You can turn off `@EnableMethodSecurity`'s pre-configuration and replace it with you own. You may choose to do this if you want to [customize the `AuthorizationManager`](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#custom-authorization-managers) or `Pointcut`. Or you may simply want to only enable a specific annotation, like `@PostAuthorize`.

You can do this in the following way:

Only @PostAuthorize Configuration

*   Java

*   Kotlin

*   Xml

```
@Configuration
@EnableMethodSecurity(prePostEnabled = false)
class MethodSecurityConfig {
	@Bean
	@Role(BeanDefinition.ROLE_INFRASTRUCTURE)
	Advisor postAuthorize() {
		return AuthorizationManagerAfterMethodInterceptor.postAuthorize();
	}
}
```

The above snippet achieves this by first disabling Method Security’s pre-configurations and then publishing [the `@PostAuthorize` interceptor](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#annotation-method-interceptors) itself.

[](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#use-intercept-methods)Authorizing with `<intercept-methods>`
-----------------------------------------------------------------------------------------------------------------------------------------------------------

While using Spring Security’s [annotation-based support](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#authorizing-with-annotations) is preferred for method security, you can also use XML to declare bean authorization rules.

If you need to declare it in your XML configuration instead, you can use [`<intercept-methods>`](https://docs.spring.io/spring-security/reference/servlet/appendix/namespace/method-security.html#nsa-intercept-methods) like so:

*   Xml

```
<bean class="org.mycompany.MyController">
    <intercept-methods>
        <protect method="get*" access="hasAuthority('read')"/>
        <protect method="*" access="hasAuthority('write')"/>
    </intercept-methods>
</bean>
```

This only supports matching method by prefix or by name. If your needs are more complex than that, [use annotation support](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#authorizing-with-annotations) instead.

[](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#use-programmatic-authorization)Authorizing Methods Programmatically
------------------------------------------------------------------------------------------------------------------------------------------------------------------

As you’ve already seen, there are several ways that you can specify non-trivial authorization rules using [Method Security SpEL expressions](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#authorization-expressions).

There are a number of ways that you can instead allow your logic to be Java-based instead of SpEL-based. This gives use access the entire Java language for increased testability and flow control.

### [](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#_using_a_custom_bean_in_spel)Using a Custom Bean in SpEL

The first way to authorize a method programmatically is a two-step process.

First, declare a bean that has a method that takes a `MethodSecurityExpressionOperations` instance like the following:

*   Java

*   Kotlin

```
@Component("authz")
public class AuthorizationLogic {
    public boolean decide(MethodSecurityExpressionOperations operations) {
        // ... authorization logic
    }
}
```

Then, reference that bean in your annotations in the following way:

*   Java

*   Kotlin

```
@Controller
public class MyController {
    @PreAuthorize("@authz.decide(#root)")
    @GetMapping("/endpoint")
    public String endpoint() {
        // ...
    }
}
```

Spring Security will invoke the given method on that bean for each method invocation.

What’s nice about this is all your authorization logic is in a separate class that can be independently unit tested and verified for correctness. It also has access to the full Java language.

In addition to returning a `Boolean`, you can also return `null` to indicate that the code abstains from making a decision.

If you want to include more information about the nature of the decision, you can instead return a custom `AuthorizationDecision` like this:

*   Java

*   Kotlin

```
@Component("authz")
public class AuthorizationLogic {
    public AuthorizationDecision decide(MethodSecurityExpressionOperations operations) {
        // ... authorization logic
        return new MyAuthorizationDecision(false, details);
    }
}
```

Or throw a custom `AuthorizationDeniedException` instance. Note, though, that returning an object is preferred as this doesn’t incur the expense of generating a stacktrace.

Then, you can access the custom details when you [customize how the authorization result is handled](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#fallback-values-authorization-denied).

Further, you can return an `AuthorizationManager` itself. This is helpful when unifying custom web authorization rules with method security ones since web security by default requires specifying an `AuthorizationManager` instance.

### [](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#custom-authorization-managers)Using a Custom Authorization Manager

The second way to authorize a method programmatically is to create a custom [`AuthorizationManager`](https://docs.spring.io/spring-security/reference/servlet/authorization/architecture.html#_the_authorizationmanager).

First, declare an authorization manager instance, perhaps like this one:

*   Java

*   Kotlin

```
@Component
public class MyAuthorizationManager implements AuthorizationManager<MethodInvocation>, AuthorizationManager<MethodInvocationResult> {
    @Override
    public AuthorizationResult authorize(Supplier<Authentication> authentication, MethodInvocation invocation) {
        // ... authorization logic
    }

    @Override
    public AuthorizationResult authorize(Supplier<Authentication> authentication, MethodInvocationResult invocation) {
        // ... authorization logic
    }
}
```

Then, publish the method interceptor with a pointcut that corresponds to when you want that `AuthorizationManager` to run. For example, you could replace how `@PreAuthorize` and `@PostAuthorize` work like so:

Only @PreAuthorize and @PostAuthorize Configuration

*   Java

*   Kotlin

*   Xml

```
@Configuration
@EnableMethodSecurity(prePostEnabled = false)
class MethodSecurityConfig {
    @Bean
	@Role(BeanDefinition.ROLE_INFRASTRUCTURE)
	Advisor preAuthorize(MyAuthorizationManager manager) {
		return AuthorizationManagerBeforeMethodInterceptor.preAuthorize(manager);
	}

	@Bean
	@Role(BeanDefinition.ROLE_INFRASTRUCTURE)
	Advisor postAuthorize(MyAuthorizationManager manager) {
		return AuthorizationManagerAfterMethodInterceptor.postAuthorize(manager);
	}
}
```

You can place your interceptor in between Spring Security method interceptors using the order constants specified in `AuthorizationInterceptorsOrder`.

### [](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#customizing-expression-handling)Customizing Expression Handling

Or, third, you can customize how each SpEL expression is handled. To do that, you can expose a custom [`MethodSecurityExpressionHandler`](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/access/expression/method/MethodSecurityExpressionHandler.html), like so:

Custom MethodSecurityExpressionHandler

*   Java

*   Kotlin

*   Xml

```
@Bean
static MethodSecurityExpressionHandler methodSecurityExpressionHandler(RoleHierarchy roleHierarchy) {
	DefaultMethodSecurityExpressionHandler handler = new DefaultMethodSecurityExpressionHandler();
	handler.setRoleHierarchy(roleHierarchy);
	return handler;
}
```

We expose `MethodSecurityExpressionHandler` using a `static` method to ensure that Spring publishes it before it initializes Spring Security’s method security `@Configuration` classes

You can also [subclass `DefaultMessageSecurityExpressionHandler`](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#subclass-defaultmethodsecurityexpressionhandler) to add your own custom authorization expressions beyond the defaults.

### [](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#pre-post-authorize-aot)Working with AOT

Spring Security will scan all beans in the application context for methods that use `@PreAuthorize` or `@PostAuthorize`. When it finds one, it will resolve any beans used inside the security expression and register the appropriate runtime hints for that bean. If it finds a method that uses `@AuthorizeReturnObject`, it will recursively search inside the method’s return type for `@PreAuthorize` and `@PostAuthorize` annotations and register them accordingly.

For example, consider the following Spring Boot application:

*   Java

*   Kotlin

```
@Service
public class AccountService { (1)

    @PreAuthorize("@authz.decide()") (2)
    @AuthorizeReturnObject (3)
    public Account getAccountById(String accountId) {
        // ...
    }

}

public class Account {

    private final String accountNumber;

    // ...

    @PreAuthorize("@accountAuthz.canViewAccountNumber()") (4)
    public String getAccountNumber() {
        return this.accountNumber;
    }

    @AuthorizeReturnObject (5)
    public User getUser() {
        return new User("John Doe");
    }

}

public class User {

    private final String fullName;

    // ...

    @PostAuthorize("@myOtherAuthz.decide()") (6)
    public String getFullName() {
        return this.fullName;
    }

}
```

**1**Spring Security finds the `AccountService` bean
**2**Finding a method that uses `@PreAuthorize`, it will resolve any bean names used inside the expression, `authz` in that case, and register runtime hints for the bean class
**3**Finding a method that uses `@AuthorizeReturnObject`, it will look into the method’s return type for any `@PreAuthorize` or `@PostAuthorize`
**4**Then, it finds a `@PreAuthorize` with another bean name: `accountAuthz`; the runtime hints are registered for the bean class as well
**5**Finding another `@AuthorizeReturnObject` it will look again into the method’s return type
**6**Now, a `@PostAuthorize` is found with yet another bean name used: `myOtherAuthz`; the runtime hints are registered for the bean class as well

There will be many times when Spring Security cannot determine the actual return type of the method ahead of time since it may be hidden in an erased generic type.

Consider the following service:

*   Java

*   Kotlin

```
@Service
public class AccountService {

    @AuthorizeReturnObject
    public List<Account> getAllAccounts() {
        // ...
    }

}
```

In this case, the generic type is erased and so it isn’t apparent to Spring Security ahead-of-time that `Account` needs to be visited in order to check for `@PreAuthorize` and `@PostAuthorize`.

*   Java

*   Kotlin

```
@Bean
@Role(BeanDefinition.ROLE_INFRASTRUCTURE)
static SecurityHintsRegistrar registerTheseToo() {
    return new PrePostAuthorizeExpressionBeanHintsRegistrar(Account.class);
}
```

[](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#use-aspectj)Authorizing with AspectJ
-----------------------------------------------------------------------------------------------------------------------------------

### [](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#match-by-pointcut)Matching Methods with Custom Pointcuts

Being built on Spring AOP, you can declare patterns that are not related to annotations, similar to [request-level authorization](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html). This has the potential advantage of centralizing method-level authorization rules.

For example, you can use publish your own `Advisor` or use [`<protect-pointcut>`](https://docs.spring.io/spring-security/reference/servlet/appendix/namespace/method-security.html#nsa-protect-pointcut) to match AOP expressions to authorization rules for your service layer like so:

*   Java

*   Kotlin

*   Xml

```
import static org.springframework.security.authorization.AuthorityAuthorizationManager.hasRole

@Bean
@Role(BeanDefinition.ROLE_INFRASTRUCTURE)
static Advisor protectServicePointcut() {
    AspectJExpressionPointcut pattern = new AspectJExpressionPointcut()
    pattern.setExpression("execution(* com.mycompany.*Service.*(..))")
    return new AuthorizationManagerBeforeMethodInterceptor(pattern, hasRole("USER"))
}
```

### [](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#weave-aspectj)Integrate with AspectJ Byte-weaving

Performance can at times be enhanced by using AspectJ to weave Spring Security advice into the byte code of your beans.

After setting up AspectJ, you can quite simply state in the `@EnableMethodSecurity` annotation or `<method-security>` element that you are using AspectJ:

*   Java

*   Kotlin

*   Xml

`@EnableMethodSecurity(mode=AdviceMode.ASPECTJ)`

And the result will be that Spring Security will publish its advisors as AspectJ advice so that they can be woven in accordingly.

[](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#changing-the-order)Specifying Order
----------------------------------------------------------------------------------------------------------------------------------

As already noted, there is a Spring AOP method interceptor for each annotation, and each of these has a location in the Spring AOP advisor chain.

Namely, the `@PreFilter` method interceptor’s order is 100, `@PreAuthorize`'s is 200, and so on.

You can use the `offset` parameter on `@EnableMethodSecurity` to move all interceptors en masse to provide their advice earlier or later in a method invocation.

[](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#authorization-expressions)Expressing Authorization with SpEL
-----------------------------------------------------------------------------------------------------------------------------------------------------------

You’ve already seen several examples using SpEL, so now let’s cover the API a bit more in depth.

Spring Security encapsulates all of its authorization fields and methods in a set of root objects. The most generic root object is called `SecurityExpressionRoot` and it forms the basis for `MethodSecurityExpressionRoot`. Spring Security supplies this root object to `MethodSecurityEvaluationContext` when preparing to evaluate an authorization expression.

### [](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#using-authorization-expression-fields-and-methods)Using Authorization Expression Fields and Methods

The first thing this provides is an enhanced set of authorization fields and methods to your SpEL expressions. What follows is a quick overview of the most common methods:

*   `permitAll` - The method requires no authorization to be invoked; note that in this case, [the `Authentication`](https://docs.spring.io/spring-security/reference/servlet/authentication/architecture.html#servlet-authentication-authentication) is never retrieved from the session

*   `denyAll` - The method is not allowed under any circumstances; note that in this case, the `Authentication` is never retrieved from the session

*   `hasAuthority` - The method requires that the `Authentication` have [a `GrantedAuthority`](https://docs.spring.io/spring-security/reference/servlet/authorization/architecture.html#authz-authorities) that matches the given value

*   `hasRole` - A shortcut for `hasAuthority` that prefixes `ROLE_` or whatever is configured as the default prefix

*   `hasAnyAuthority` - The method requires that the `Authentication` have a `GrantedAuthority` that matches any of the given values

*   `hasAnyRole` - A shortcut for `hasAnyAuthority` that prefixes `ROLE_` or whatever is configured as the default prefix

*   `hasAllAuthorities` - The method requires that the `Authentication` have `GrantedAuthority`s that matches all of the given values

*   `hasAllRoles` - A shortcut for `hasAllAuthorities` that prefixes `ROLE_` or whatever is configured as the default prefix

*   `hasPermission` - A hook into your `PermissionEvaluator` instance for doing object-level authorization

And here is a brief look at the most common fields:

*   `authentication` - The `Authentication` instance associated with this method invocation

*   `principal` - The `Authentication#getPrincipal` associated with this method invocation

Having now learned the patterns, rules, and how they can be paired together, you should be able to understand what is going on in this more complex example:

Authorize Requests

*   Java

*   Kotlin

*   Xml

```
@Component
public class MyService {
    @PreAuthorize("denyAll") (1)
    MyResource myDeprecatedMethod(...);

    @PreAuthorize("hasRole('ADMIN')") (2)
    MyResource writeResource(...)

    @PreAuthorize("hasAuthority('db') and hasRole('ADMIN')") (3)
    MyResource deleteResource(...)

    @PreAuthorize("principal.claims['aud'] == 'my-audience'") (4)
    MyResource readResource(...);

	@PreAuthorize("@authz.check(authentication, #root)")
    MyResource shareResource(...);
}
```

**1**This method may not be invoked by anyone for any reason
**2**This method may only be invoked by `Authentication`s granted the `ROLE_ADMIN` authority
**3**This method may only be invoked by `Authentication`s granted the `db` and `ROLE_ADMIN` authorities
**4**This method may only be invoked by `Princpal`s with an `aud` claim equal to "my-audience"
**5**This method may only be invoked if the bean `authz`'s `check` method returns `true`

You can use a bean like `authz` above to [add programmatic authorization](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#_using_a_custom_bean_in_spel).

### [](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#using_method_parameters)Using Method Parameters

Additionally, Spring Security provides a mechanism for discovering method parameters so they can also be accessed in the SpEL expression as well.

For a complete reference, Spring Security uses `DefaultSecurityParameterNameDiscoverer` to discover the parameter names. By default, the following options are tried for a method.

1.   If Spring Security’s `@P` annotation is present on a single argument to the method, the value is used. The following example uses the `@P` annotation:

    *   Java

    *   Kotlin

```
import org.springframework.security.access.method.P;

...

@PreAuthorize("hasPermission(#c, 'write')")
public void updateContact(@P("c") Contact contact);
```

The intention of this expression is to require that the current `Authentication` have `write` permission specifically for this `Contact` instance.

Behind the scenes, this is implemented by using `AnnotationParameterNameDiscoverer`, which you can customize to support the value attribute of any specified annotation.

2.   If [Spring Data’s](https://docs.spring.io/spring-security/reference/servlet/integrations/data.html)`@Param` annotation is present on at least one parameter for the method, the value is used. The following example uses the `@Param` annotation:

    *   Java

    *   Kotlin

```
import org.springframework.data.repository.query.Param;

...

@PreAuthorize("#n == authentication.name")
Contact findContactByName(@Param("n") String name);
```

The intention of this expression is to require that `name` be equal to `Authentication#getName` for the invocation to be authorized.

Behind the scenes, this is implemented by using `AnnotationParameterNameDiscoverer`, which you can customize to support the value attribute of any specified annotation.

3.   If you compile your code with the `-parameters` argument, the standard JDK reflection API is used to discover the parameter names. This works on both classes and interfaces.

4.   Finally, if you compile your code with debug symbols, the parameter names are discovered by using the debug symbols. This does not work for interfaces, since they do not have debug information about the parameter names. For interfaces, either annotations or the `-parameters` approach must be used.

[](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#customizing-authorization-managers)Customizing Authorization Managers
--------------------------------------------------------------------------------------------------------------------------------------------------------------------

When you use SpEL expressions with [`@PreAuthorize`](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#use-preauthorize), [`@PostAuthorize`](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#use-postauthorize), [`@PreFilter`](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#use-prefilter) and [`@PostFilter`](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#use-postfilter), Spring Security takes care of creating the appropriate `AuthorizationManager` instances for you. In certain cases, you may want to customize what is created in order to have complete control over how authorization decisions are made [at the framework level](https://docs.spring.io/spring-security/reference/servlet/authorization/architecture.html#authz-delegate-authorization-manager).

In order to take control of creating instances of `AuthorizationManager` for pre- and post-annotations, you can create a custom [`AuthorizationManagerFactory`](https://docs.spring.io/spring-security/reference/servlet/authorization/architecture.html#authz-authorization-manager-factory). For example, let’s say you want to allow users with the `ADMIN` role whenever any other role is required. To do this, you can create a custom implementation for method security as in the following example:

*   Java

*   Kotlin

```
@Component
public class CustomMethodInvocationAuthorizationManagerFactory
		implements AuthorizationManagerFactory<MethodInvocation> {

	private final AuthorizationManagerFactory<MethodInvocation> delegate =
			new DefaultAuthorizationManagerFactory<>();

	@Override
	public AuthorizationManager<MethodInvocation> hasRole(String role) {
		return AuthorizationManagers.anyOf(
			this.delegate.hasRole(role),
			this.delegate.hasRole("ADMIN")
		);
	}

	@Override
	public AuthorizationManager<MethodInvocation> hasAnyRole(String... roles) {
		return AuthorizationManagers.anyOf(
			this.delegate.hasAnyRole(roles),
			this.delegate.hasRole("ADMIN")
		);
	}

}
```

Now, whenever you [use the `@PreAuthorize` annotation](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#use-preauthorize) with `hasRole` or `hasAnyRole`, Spring Security will automatically invoke your custom factory to create an instance of `AuthorizationManager` that allows access for the given role(s) _OR_ the `ADMIN` role.

We use this as a simple example of creating a custom `AuthorizationManagerFactory`, though the same outcome could be accomplished with [a role hierarchy](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#favor-granting-authorities). Use whichever approach fits best in your situation.

[](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#authorize-object)Authorizing Arbitrary Objects
---------------------------------------------------------------------------------------------------------------------------------------------

Spring Security also supports wrapping any object that is annotated its method security annotations.

The simplest way to achieve this is to mark any method that returns the object you wish to authorize with the `@AuthorizeReturnObject` annotation.

For example, consider the following `User` class:

*   Java

*   Kotlin

```
public class User {
	private String name;
	private String email;

	public User(String name, String email) {
		this.name = name;
		this.email = email;
	}

	public String getName() {
		return this.name;
	}

    @PreAuthorize("hasAuthority('user:read')")
    public String getEmail() {
		return this.email;
    }
}
```

Given an interface like this one:

*   Java

*   Kotlin

```
public class UserRepository {
	@AuthorizeReturnObject
    Optional<User> findByName(String name) {
		// ...
    }
}
```

Then any `User` that is returned from `findById` will be secured like other Spring Security-protected components:

*   Java

*   Kotlin

```
@Autowired
UserRepository users;

@Test
void getEmailWhenProxiedThenAuthorizes() {
    Optional<User> securedUser = users.findByName("name");
    assertThatExceptionOfType(AccessDeniedException.class).isThrownBy(() -> securedUser.get().getEmail());
}
```

### [](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#_using_authorizereturnobject_at_the_class_level)Using `@AuthorizeReturnObject` at the class level

`@AuthorizeReturnObject` can be placed at the class level. Note, though, that this means Spring Security will attempt to proxy any return object, including `String`, `Integer` and other types. This is often not what you want to do.

If you want to use `@AuthorizeReturnObject` on a class or interface whose methods return value types, like `int`, `String`, `Double` or collections of those types, then you should also publish the appropriate `AuthorizationAdvisorProxyFactory.TargetVisitor` as follows:

*   Java

*   Kotlin

```
import org.springframework.security.authorization.method.AuthorizationAdvisorProxyFactory.TargetVisitor;

// ...

@Bean
static TargetVisitor skipValueTypes() {
    return TargetVisitor.defaultsSkipValueTypes();
}
```

You can set your own `AuthorizationAdvisorProxyFactory.TargetVisitor` to customize the proxying for any set of types

### [](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#_programmatically_proxying)Programmatically Proxying

You can also programmatically proxy a given object.

To achieve this, you can autowire the provided `AuthorizationProxyFactory` instance, which is based on which method security interceptors you have configured. If you are using `@EnableMethodSecurity`, then this means that it will by default have the interceptors for `@PreAuthorize`, `@PostAuthorize`, `@PreFilter`, and `@PostFilter`.

You can proxy an instance of user in the following way:

*   Java

*   Kotlin

```
@Autowired
AuthorizationProxyFactory proxyFactory;

@Test
void getEmailWhenProxiedThenAuthorizes() {
    User user = new User("name", "email");
    assertThat(user.getEmail()).isNotNull();
    User securedUser = proxyFactory.proxy(user);
    assertThatExceptionOfType(AccessDeniedException.class).isThrownBy(securedUser::getEmail);
}
```

### [](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#_manual_construction)Manual Construction

You can also define your own instance if you need something different from the Spring Security default.

For example, if you define an `AuthorizationProxyFactory` instance like so:

*   Java

*   Kotlin

```
import org.springframework.security.authorization.method.AuthorizationAdvisorProxyFactory.TargetVisitor;
import static org.springframework.security.authorization.method.AuthorizationManagerBeforeMethodInterceptor.preAuthorize;
// ...

AuthorizationProxyFactory proxyFactory = AuthorizationAdvisorProxyFactory.withDefaults();
// and if needing to skip value types
proxyFactory.setTargetVisitor(TargetVisitor.defaultsSkipValueTypes());
```

Then you can wrap any instance of `User` as follows:

*   Java

*   Kotlin

```
@Test
void getEmailWhenProxiedThenAuthorizes() {
	AuthorizationProxyFactory proxyFactory = AuthorizationAdvisorProxyFactory.withDefaults();
    User user = new User("name", "email");
    assertThat(user.getEmail()).isNotNull();
    User securedUser = proxyFactory.proxy(user);
    assertThatExceptionOfType(AccessDeniedException.class).isThrownBy(securedUser::getEmail);
}
```

### [](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#_proxying_collections)Proxying Collections

`AuthorizationProxyFactory` supports Java collections, streams, arrays, optionals, and iterators by proxying the element type and maps by proxying the value type.

This means that when proxying a `List` of objects, the following also works:

*   Java

```
@Test
void getEmailWhenProxiedThenAuthorizes() {
	AuthorizationProxyFactory proxyFactory = AuthorizationAdvisorProxyFactory.withDefaults();
    List<User> users = List.of(ada, albert, marie);
    List<User> securedUsers = proxyFactory.proxy(users);
	securedUsers.forEach((securedUser) ->
        assertThatExceptionOfType(AccessDeniedException.class).isThrownBy(securedUser::getEmail));
}
```

### [](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#_proxying_classes)Proxying Classes

In limited circumstances, it may be valuable to proxy a `Class` itself, and `AuthorizationProxyFactory` also supports this. This is roughly the equivalent of calling `ProxyFactory#getProxyClass` in Spring Framework’s support for creating proxies.

One place where this is handy is when you need to construct the proxy class ahead-of-time, like with Spring AOT.

### [](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#_support_for_all_method_security_annotations)Support for All Method Security Annotations

`AuthorizationProxyFactory` supports whichever method security annotations are enabled in your application. It is based off of whatever `AuthorizationAdvisor` classes are published as a bean.

Since `@EnableMethodSecurity` publishes `@PreAuthorize`, `@PostAuthorize`, `@PreFilter`, and `@PostFilter` advisors by default, you will typically need to do nothing to activate the ability.

SpEL expressions that use `returnObject` or `filterObject` sit behind the proxy and so have full access to the object.

### [](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#custom_advice)Custom Advice

If you have security advice that you also want applied, you can publish your own `AuthorizationAdvisor` like so:

*   Java

*   Kotlin

```
@EnableMethodSecurity
class SecurityConfig {
    @Bean
    static AuthorizationAdvisor myAuthorizationAdvisor() {
        return new AuthorizationAdvisor();
    }
}
```

And Spring Security will add that advisor into the set of advice that `AuthorizationProxyFactory` adds when proxying an object.

### [](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#_working_with_jackson)Working with Jackson

One powerful use of this feature is to return a secured value from a controller like so:

*   Java

*   Kotlin

```
@RestController
public class UserController {
    @Autowired
    AuthorizationProxyFactory proxyFactory;

    @GetMapping
    User currentUser(@AuthenticationPrincipal User user) {
        return this.proxyFactory.proxy(user);
    }
}
```

You will need to [add a `MethodAuthorizationDeniedHandler`](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#fallback-values-authorization-denied) like this one:

*   Java

*   Kotlin

```
@Component
public class Null implements MethodAuthorizationDeniedHandler {
    @Override
    public Object handleDeniedInvocation(MethodInvocation methodInvocation, AuthorizationResult authorizationResult) {
        return null;
    }
}

// ...

@HandleAuthorizationDenied(handlerClass = Null.class)
public class User {
	...
}
```

Then, you’ll see a different JSON serialization based on the authorization level of the user. If they don’t have the `user:read` authority, then they’ll see:

```
{
    "name" : "name",
    "email" : null
}
```

And if they do have that authority, they’ll see:

```
{
    "name" : "name",
    "email" : "email"
}
```

You can also add the Spring Boot property `spring.jackson.default-property-inclusion=non_null` to exclude the null value from serialization, if you also don’t want to reveal the JSON key to an unauthorized user.

### [](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#authorize-return-object-aot)Working with AOT

Spring Security will scan all beans in the application context for methods that use `@AuthorizeReturnObject`. When it finds one, it will create and register the appropriate proxy class ahead of time. It will also recursively search for other nested objects that also use `@AuthorizeReturnObject` and register them accordingly.

For example, consider the following Spring Boot application:

*   Java

*   Kotlin

```
@SpringBootApplication
public class MyApplication {
	@RestController
    public static class MyController { (1)
		@GetMapping
        @AuthorizeReturnObject
        Message getMessage() { (2)
			return new Message(someUser, "hello!");
        }
    }

	public static class Message { (3)
		User to;
		String text;

		// ...

        @AuthorizeReturnObject
        public User getTo() { (4)
			return this.to;
        }

		// ...
	}

	public static class User { (5)
		// ...
	}

	public static void main(String[] args) {
		SpringApplication.run(MyApplication.class);
	}
}
```

**1**- First, Spring Security finds the `MyController` bean
**2**- Finding a method that uses `@AuthorizeReturnObject`, it proxies `Message`, the return value, and registers that proxy class to `RuntimeHints`
**3**- Then, it traverses `Message` to see if it uses `@AuthorizeReturnObject`
**4**- Finding a method that uses `@AuthorizeReturnObject`, it proxies `User`, the return value, and registers that proxy class to `RuntimeHints`
**5**- Finally, it traverses `User` to see if it uses `@AuthorizeReturnObject`; finding nothing, the algorithm completes

There will be many times when Spring Security cannot determine the proxy class ahead of time since it may be hidden in an erased generic type.

Consider the following change to `MyController`:

*   Java

*   Kotlin

```
@RestController
public static class MyController {
    @GetMapping
    @AuthorizeReturnObject
    List<Message> getMessages() {
        return List.of(new Message(someUser, "hello!"));
    }
}
```

In this case, the generic type is erased and so it isn’t apparent to Spring Security ahead-of-time that `Message` will need to be proxied at runtime.

To address this, you can publish `AuthorizeProxyFactoryHintsRegistrar` like so:

*   Java

*   Kotlin

```
@Bean
@Role(BeanDefinition.ROLE_INFRASTRUCTURE)
static SecurityHintsRegsitrar registerTheseToo(AuthorizationProxyFactory proxyFactory) {
	return new AuthorizeReturnObjectHintsRegistrar(proxyFactory, Message.class);
}
```

Spring Security will register that class and then traverse its type as before.

[](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#fallback-values-authorization-denied)Providing Fallback Values When Authorization is Denied
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

There are some scenarios where you may not wish to throw an `AuthorizationDeniedException` when a method is invoked without the required permissions. Instead, you might wish to return a post-processed result, like a masked result, or a default value in cases where authorization denied happened before invoking the method.

Spring Security provides support for handling authorization denied on method invocation by using the [`@HandleAuthorizationDenied`](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/authorization/method/HandleAuthorizationDenied.html). The handler works for denied authorizations that happened in the [`@PreAuthorize` and `@PostAuthorize` annotations](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#authorizing-with-annotations) as well as [`AuthorizationDeniedException`](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/authorization/AuthorizationDeniedException.html) thrown from the method invocation itself.

Let’s consider the example from the [previous section](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#authorize-object), but instead of creating the `AccessDeniedExceptionInterceptor` to transform an `AccessDeniedException` to a `null` return value, we will use the `handlerClass` attribute from `@HandleAuthorizationDenied`:

*   Java

*   Kotlin

```
public class NullMethodAuthorizationDeniedHandler implements MethodAuthorizationDeniedHandler { (1)

    @Override
    public Object handleDeniedInvocation(MethodInvocation methodInvocation, AuthorizationResult authorizationResult) {
        return null;
    }

}

@Configuration
@EnableMethodSecurity
public class SecurityConfig {

    @Bean (2)
    public NullMethodAuthorizationDeniedHandler nullMethodAuthorizationDeniedHandler() {
        return new NullMethodAuthorizationDeniedHandler();
    }

}

public class User {
    // ...

    @PreAuthorize(value = "hasAuthority('user:read')")
    @HandleAuthorizationDenied(handlerClass = NullMethodAuthorizationDeniedHandler.class)
    public String getEmail() {
        return this.email;
    }
}
```

**1**Create an implementation of `MethodAuthorizationDeniedHandler` that returns a `null` value
**2**Register the `NullMethodAuthorizationDeniedHandler` as a bean
**3**Annotate the method with `@HandleAuthorizationDenied` and pass the `NullMethodAuthorizationDeniedHandler` to the `handlerClass` attribute

And then you can verify that a `null` value is returned instead of the `AccessDeniedException`:

You can also annotate your class with `@Component` instead of creating a `@Bean` method

*   Java

*   Kotlin

```
@Autowired
UserRepository users;

@Test
void getEmailWhenProxiedThenNullEmail() {
    Optional<User> securedUser = users.findByName("name");
    assertThat(securedUser.get().getEmail()).isNull();
}
```

### [](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#_using_the_denied_result_from_the_method_invocation)Using the Denied Result From the Method Invocation

There are some scenarios where you might want to return a secure result derived from the denied result. For example, if a user is not authorized to see email addresses, you might want to apply some masking on the original email address, i.e. _useremail@example.com_ would become _use******@example.com_.

For those scenarios, you can override the `handleDeniedInvocationResult` from the `MethodAuthorizationDeniedHandler`, which has the [`MethodInvocationResult`](https://docs.spring.io/spring-security/reference/api/java/org/springframework/security/authorization/method/MethodInvocationResult.html) as an argument. Let’s continue with the previous example, but instead of returning `null`, we will return a masked value of the email:

*   Java

*   Kotlin

```
public class EmailMaskingMethodAuthorizationDeniedHandler implements MethodAuthorizationDeniedHandler { (1)

    @Override
    public Object handleDeniedInvocation(MethodInvocation methodInvocation, AuthorizationResult authorizationResult) {
        return "***";
    }

    @Override
    public Object handleDeniedInvocationResult(MethodInvocationResult methodInvocationResult, AuthorizationResult authorizationResult) {
        String email = (String) methodInvocationResult.getResult();
        return email.replaceAll("(^[^@]{3}|(?!^)\\G)[^@]", "$1*");
    }

}

@Configuration
@EnableMethodSecurity
public class SecurityConfig {

    @Bean (2)
    public EmailMaskingMethodAuthorizationDeniedHandler emailMaskingMethodAuthorizationDeniedHandler() {
        return new EmailMaskingMethodAuthorizationDeniedHandler();
    }

}

public class User {
    // ...

    @PostAuthorize(value = "hasAuthority('user:read')")
    @HandleAuthorizationDenied(handlerClass = EmailMaskingMethodAuthorizationDeniedHandler.class)
    public String getEmail() {
        return this.email;
    }
}
```

**1**Create an implementation of `MethodAuthorizationDeniedHandler` that returns a masked value of the unauthorized result value
**2**Register the `EmailMaskingMethodAuthorizationDeniedHandler` as a bean
**3**Annotate the method with `@HandleAuthorizationDenied` and pass the `EmailMaskingMethodAuthorizationDeniedHandler` to the `handlerClass` attribute

And then you can verify that a masked email is returned instead of an `AccessDeniedException`:

Since you have access to the original denied value, make sure that you correctly handle it and do not return it to the caller.

*   Java

*   Kotlin

```
@Autowired
UserRepository users;

@Test
void getEmailWhenProxiedThenMaskedEmail() {
    Optional<User> securedUser = users.findByName("name");
    // email is useremail@example.com
    assertThat(securedUser.get().getEmail()).isEqualTo("use******@example.com");
}
```

When implementing the `MethodAuthorizationDeniedHandler` you have a few options on what type you can return:

*   A `null` value.

*   A non-null value, respecting the method’s return type.

*   Throw an exception, usually an instance of `AuthorizationDeniedException`. This is the default behavior.

*   A `Mono` type for reactive applications.

Note that since the handler must be registered as beans in your application context, you can inject dependencies into them if you need a more complex logic. In addition to that, you have available the `MethodInvocation` or the `MethodInvocationResult`, as well as the `AuthorizationResult` for more details related to the authorization decision.

### [](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#deciding-return-based-parameters)Deciding What to Return Based on Available Parameters

Consider a scenario where there might be multiple mask values for different methods, it would be not so productive if we had to create a handler for each of those methods, although it is perfectly fine to do that. In such cases, we can use the information passed via parameters to decide what to do. For example, we can create a custom `@Mask` annotation and a handler that detects that annotation to decide what mask value to return:

*   Java

*   Kotlin

```
import org.springframework.core.annotation.AnnotationUtils;

@Target({ ElementType.METHOD, ElementType.TYPE })
@Retention(RetentionPolicy.RUNTIME)
public @interface Mask {

    String value();

}

public class MaskAnnotationDeniedHandler implements MethodAuthorizationDeniedHandler {

    @Override
    public Object handleDeniedInvocation(MethodInvocation methodInvocation, AuthorizationResult authorizationResult) {
        Mask mask = AnnotationUtils.getAnnotation(methodInvocation.getMethod(), Mask.class);
        return mask.value();
    }

}

@Configuration
@EnableMethodSecurity
public class SecurityConfig {

    @Bean
    public MaskAnnotationDeniedHandler maskAnnotationDeniedHandler() {
        return new MaskAnnotationDeniedHandler();
    }

}

@Component
public class MyService {

    @PreAuthorize(value = "hasAuthority('user:read')")
    @HandleAuthorizationDenied(handlerClass = MaskAnnotationDeniedHandler.class)
    @Mask("***")
    public String foo() {
        return "foo";
    }

    @PreAuthorize(value = "hasAuthority('user:read')")
    @HandleAuthorizationDenied(handlerClass = MaskAnnotationDeniedHandler.class)
    @Mask("???")
    public String bar() {
        return "bar";
    }

}
```

Now the return values when access is denied will be decided based on the `@Mask` annotation:

*   Java

*   Kotlin

```
@Autowired
MyService myService;

@Test
void fooWhenDeniedThenReturnStars() {
    String value = this.myService.foo();
    assertThat(value).isEqualTo("***");
}

@Test
void barWhenDeniedThenReturnQuestionMarks() {
    String value = this.myService.foo();
    assertThat(value).isEqualTo("???");
}
```

### [](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#_combining_with_meta_annotation_support)Combining with Meta Annotation Support

You can also combine the `@HandleAuthorizationDenied` with other annotations in order to reduce and simplify the annotations in a method. Let’s consider the [example from the previous section](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#deciding-return-based-parameters) and merge `@HandleAuthorizationDenied` with `@Mask`:

*   Java

*   Kotlin

```
@Target({ ElementType.METHOD, ElementType.TYPE })
@Retention(RetentionPolicy.RUNTIME)
@HandleAuthorizationDenied(handlerClass = MaskAnnotationDeniedHandler.class)
public @interface Mask {

    String value();

}

@Mask("***")
public String myMethod() {
    // ...
}
```

Now you do not have to remember to add both annotations when you need a mask behavior in your method. Make sure to read the [Meta Annotations Support](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#meta-annotations) section for more details on the usage.

[](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#migration-enableglobalmethodsecurity)Migrating from `@EnableGlobalMethodSecurity`
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

If you are using `@EnableGlobalMethodSecurity`, you should migrate to `@EnableMethodSecurity`.

If you cannot migrate at this time, please include the `spring-security-access` module as a dependency like so:

*   Maven

*   Gradle

```
<dependency>
    <groupId>org.springframework.security</groupId>
    <artifactId>spring-security-access</artifactId>
</dependency>
```

### [](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#servlet-replace-globalmethodsecurity-with-methodsecurity)Replace [global method security](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#jc-enable-global-method-security) with [method security](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#jc-enable-method-security)

This means that the following two listings are functionally equivalent:

*   Java

*   Kotlin

*   Xml

`@EnableGlobalMethodSecurity(prePostEnabled = true)`

and:

*   Java

*   Kotlin

*   Xml

`@EnableMethodSecurity`

For applications not using the pre-post annotations, make sure to turn it off to avoid activating unwanted behavior.

For example, a listing like:

*   Java

*   Kotlin

*   Xml

`@EnableGlobalMethodSecurity(securedEnabled = true)`

should change to:

*   Java

*   Kotlin

*   Xml

`@EnableMethodSecurity(securedEnabled = true, prePostEnabled = false)`

### [](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#_use_a_custom_bean_instead_of_subclassing_defaultmethodsecurityexpressionhandler)Use a Custom `@Bean` instead of subclassing `DefaultMethodSecurityExpressionHandler`

As a performance optimization, a new method was introduced to `MethodSecurityExpressionHandler` that takes a `Supplier<Authentication>` instead of an `Authentication`.

This allows Spring Security to defer the lookup of the `Authentication`, and is taken advantage of automatically when you use `@EnableMethodSecurity` instead of `@EnableGlobalMethodSecurity`.

However, let’s say that your code extends `DefaultMethodSecurityExpressionHandler` and overrides `createSecurityExpressionRoot(Authentication, MethodInvocation)` to return a custom `SecurityExpressionRoot` instance. This will no longer work because the arrangement that `@EnableMethodSecurity` sets up calls `createEvaluationContext(Supplier<Authentication>, MethodInvocation)` instead.

Happily, such a level of customization is often unnecessary. Instead, you can create a custom bean with the authorization methods that you need.

For example, let’s say you are wanting a custom evaluation of `@PostAuthorize("hasAuthority('ADMIN')")`. You can create a custom `@Bean` like this one:

*   Java

*   Kotlin

```
class MyAuthorizer {
	boolean isAdmin(MethodSecurityExpressionOperations root) {
		boolean decision = root.hasAuthority("ADMIN");
		// custom work ...
        return decision;
	}
}
```

and then refer to it in the annotation like so:

*   Java

*   Kotlin

`@PreAuthorize("@authz.isAdmin(#root)")`

#### [](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html#subclass-defaultmethodsecurityexpressionhandler)I’d still prefer to subclass `DefaultMethodSecurityExpressionHandler`

If you must continue subclassing `DefaultMethodSecurityExpressionHandler`, you can still do so. Instead, override the `createEvaluationContext(Supplier<Authentication>, MethodInvocation)` method like so:

*   Java

*   Kotlin

```
@Component
class MyExpressionHandler extends DefaultMethodSecurityExpressionHandler {
    @Override
    public EvaluationContext createEvaluationContext(Supplier<Authentication> authentication, MethodInvocation mi) {
		StandardEvaluationContext context = (StandardEvaluationContext) super.createEvaluationContext(authentication, mi);
        MethodSecurityExpressionOperations delegate = (MethodSecurityExpressionOperations) context.getRootObject().getValue();
        MySecurityExpressionRoot root = new MySecurityExpressionRoot(delegate);
        context.setRootObject(root);
        return context;
    }
}
```
