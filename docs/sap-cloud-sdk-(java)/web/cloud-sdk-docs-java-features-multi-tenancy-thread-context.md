# Source: https://sap.github.io/cloud-sdk/docs/java/features/multi-tenancy/thread-context

Title: Multitenancy With the Thread Context | SAP Cloud SDK

URL Source: https://sap.github.io/cloud-sdk/docs/java/features/multi-tenancy/thread-context

Markdown Content:
What Is a Thread Context?[​](https://sap.github.io/cloud-sdk/docs/java/features/multi-tenancy/thread-context#what-is-a-thread-context "Direct link to What Is a Thread Context?")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The SAP Cloud SDK for Java provides a so-called `ThreadContext`. It serves as thread-safe storage for potentially sensitive information. Specifically, the following three objects are stored:

*   The current _Tenant_
*   The current _Principal_ (User)
*   The [JSON Web Token](https://jwt.io/) (JWT)

This information is used throughout the SAP Cloud SDK to provide features like tenant and principal isolation, JWT verification and authorization against other systems and services. To ensure different tenants and users are properly isolated in an application, this information is always limited to the thread it was created on unless it is explicitly passed on by the application (see [Propagating the Thread Context](https://sap.github.io/cloud-sdk/docs/java/features/multi-tenancy/thread-context#running-asynchronous-operations)).

info

Multi-tenancy describes the access of different, technically separated user groups to the same instance of an application. These user groups are called _Tenants_.

The SAP Cloud SDK uses the `Tenant` interface to represent them.

How Is a Thread Context Created?[​](https://sap.github.io/cloud-sdk/docs/java/features/multi-tenancy/thread-context#how-is-a-thread-context-created "Direct link to How Is a Thread Context Created?")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The SAP Cloud SDK provides a [`RequestFilter`](https://sap.github.io/cloud-sdk/java-api/v5/com/sap/cloud/sdk/cloudplatform/servletjakarta/RequestAccessorFilter.html) that will listen to incoming HTTP requests. This filter will extract **all** provided HTTP headers from the incoming request and store them in the `ThreadContext`. Additionally, if the `Authorization` header contains a `JWT` (typically forwarded from the [`AppRouter`](https://blogs.sap.com/2020/04/03/sap-application-router/)), the filter will:

*   Parse this token
*   Store it in the `ThreadContext` and
*   Pull the _Tenant_ and _Principal_ information from it

To ensure this logic is executed at runtime you need to add the following annotations to your application:

Application.java

`@ComponentScan({"com.sap.cloud.sdk", <your.own.package>})@ServletComponentScan({"com.sap.cloud.sdk", <your.own.package>})`

You can verify these annotations are effective at runtime by checking the application logs on debug level. Or, in case you get an exception, search the stack trace for `RequestAccessorFilter.doFilter`.

Integration with CAP

In case you are using CAP (with the `cds-integration-cloud-sdk` dependency) the Tenant, Principal, and Headers will **instead** be derived from the [CAP Request Context](https://cap.cloud.sap/docs/java/request-contexts). That also means that the `ThreadContext` will not be used when accessing this information.

For other information (e.g. the current authentication token) the `ThreadContext` will still be used.

Running Asynchronous Operations[​](https://sap.github.io/cloud-sdk/docs/java/features/multi-tenancy/thread-context#running-asynchronous-operations "Direct link to Running Asynchronous Operations")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

As the name suggests, the `ThreadContext` is bound to a thread, more specifically to the one it was created in. In consequence, other threads, i.e. asynchronous operations, cannot access the stored information if it hasn't been explicitly propagated.

The SAP Cloud SDK offers a dedicated API to execute asynchronous operations while preserving the `ThreadContext`.

Given any operation:

`Callable myTask = () -> doStuff();// orRunnable myTask = () -> doStuff();`

The operation can be executed asynchronously via:

`Future runningTask = ThreadContextExecutors.submit(myTask);`

Operations that are submitted this way will be executed by a single instance of `ThreadContextExecutorService`. By default, this instance is based on a `CachedThreadPool`, which manages the concurrency internally.

For executing multiple asynchronous operations we recommend the following:

`List<Callable> tasks;ThreadContextExecutorService executor = ThreadContextExecutors.getExecutor();List<Future> runningTasks = executor.invokeAll(tasks);`

### Spring Integration[​](https://sap.github.io/cloud-sdk/docs/java/features/multi-tenancy/thread-context#spring-integration "Direct link to Spring Integration")

You can conveniently integrate this functionality to work with Springs `@Async` annotation.

The configuration below will ensure all methods annotated with `@Async` will have the `ThreadContext` available:

`@EnableAsync@Configurationpublic class AsynchronousConfiguration implements AsyncConfigurer {  @Override  public Executor getAsyncExecutor() {    return ThreadContextExecutors.getExecutor();  }}`

You can read more about the `@Async` functionality [here](https://www.baeldung.com/spring-async).

Security Context

The Spring `SecurityContext` can be propagated to `@Async` calls. Replace the above executor with this one:

`new DelegatingSecurityContextExecutor(ThreadContextExecutors.getExecutor());`

And add this dependency:

`<dependency>    <groupId>org.springframework.security</groupId>    <artifactId>spring-security-core</artifactId></dependency>`

### Passing on Other ThreadLocals[​](https://sap.github.io/cloud-sdk/docs/java/features/multi-tenancy/thread-context#passing-on-other-threadlocals "Direct link to Passing on Other ThreadLocals")

Other libraries and frameworks may also rely on `ThreadLocal` variables to hold contextual data. For example, the CAP `RequestContext` is also bound to the current Thread.

To not lose this state when creating a new Thread they can be passed on by implementing a `ThreadContextDecorator`. A typical implementation for this purpose should look like this:

`@Overridepublic <T> Callable<T> decorateCallable( @Nonnull final Callable<T> callable ) {  Object valueToPass = YourThreadLocal.get();  return () -> {    Object initial = YourThreadLocal.get();    YourThreadLocal.set(valueToPass);    try {      return callable.call();    }    finally {      YourThreadLocal.set(initial);    }  };}`

Such a custom `ThreadContextDecorator` can be registered via `DefaultThreadContextDecoratorChain.registerDefaultDecorator`.

tip

The SAP Cloud SDK already comes with a default decorator that passes on the `SecurityContext` of `com.sap.cloud.security:java-api`. If the [CAP integration](https://sap.github.io/cloud-sdk/docs/java/guides/cap-sdk-integration) is used, also the `RequestContext` is passed on (requires CDS version `2.4.0` or higher).

### Configuring the Executor[​](https://sap.github.io/cloud-sdk/docs/java/features/multi-tenancy/thread-context#configuring-the-executor "Direct link to Configuring the Executor")

The `ThreadContextExecutors` class leverages a single `ThreadContextExecutorService` instance that can be configured.

You can create a custom `ThreadContextExecutorService`, for example to use a different thread pool, via:

`ThreadContextExecutorService executor =  DefaultThreadContextExecutorService.of(Executors.newFixedThreadPool(3));// use it directly:executor.submit(myTask);// or set it to be used by the static ThreadContextExecutors API:ThreadContextExecutors.setExecutor(executor);ThreadContextExecutors.submit(myTask);`

The above API is also compatible with Java virtual threads (JDK21).

`ThreadContextExecutorService executor =  DefaultThreadContextExecutorService.of(Executors.newVirtualThreadPerTaskExecutor());`

### Modifying the ThreadContext[​](https://sap.github.io/cloud-sdk/docs/java/features/multi-tenancy/thread-context#modifying-the-threadcontext "Direct link to Modifying the ThreadContext")

Caution

Modifying the `ThreadContext` as depicted below is currently supported only when using the default `Facade` (e.g. `DefaultTenantFacade`) implementations. This is an issue especially when using the CAP integration dependency `cds-integration-cloud-sdk`. To still manipulate the request context, please refer to [the CAP documentation](https://cap.cloud.sap/docs/java/request-contexts#defining-requestcontext).

You may want to run an asynchronous operation in a completely new or custom context. By default, the executor will transfer any existing context to the new thread.

To run something in a completely new, empty context, use:

`ThreadContextExecutors.submit(myTask, new DefaultThreadContext());`

By contrast, to pass on the current context, but modifying the tenant (and only the tenant), use:

`Tenant myTenant = new DefaultTenant("foo");Callable myTaskWithTenant = () -> TenantAccessor.executeWithTenant(myTenant, myTask);ThreadContextExecutors.submit(myTaskWithTenant);`

To avoid multiple wrappings, in particular when changing multiple values, you can also build a custom executor:

`Tenant myTenant = new DefaultTenant("foo");Principal myPrincipal = new DefaultPrincipal("bar");ThreadContextExecutor customExecutor = ThreadContextExecutor.fromNewContext()            .withListeners(                new TenantThreadContextListener(myTenant),                new PrincipalThreadContextListener(myPrincipal)            );ThreadContextExecutors.submit(myTask, customExecutor);`

How Can the Thread Context Be Used?[​](https://sap.github.io/cloud-sdk/docs/java/features/multi-tenancy/thread-context#how-can-the-thread-context-be-used "Direct link to How Can the Thread Context Be Used?")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Accessing Information[​](https://sap.github.io/cloud-sdk/docs/java/features/multi-tenancy/thread-context#accessing-information "Direct link to Accessing Information")

The Thread context can be accessed via the static [`ThreadContextAccessor`](https://sap.github.io/cloud-sdk/java-api/v5/com/sap/cloud/sdk/cloudplatform/thread/ThreadContextAccessor.html).

For the frequently needed _HTTP Headers_, _Tenant_, _Principal_, and _JWT_ there are also dedicated accessors:

*   [`RequestHeaderAccessor`](https://sap.github.io/cloud-sdk/java-api/v5/com/sap/cloud/sdk/cloudplatform/requestheader/RequestHeaderAccessor.html)
*   [`TenantAccessor`](https://sap.github.io/cloud-sdk/java-api/v5/com/sap/cloud/sdk/cloudplatform/tenant/TenantAccessor.html)
*   [`PrincipalAccessor`](https://sap.github.io/cloud-sdk/java-api/v5/com/sap/cloud/sdk/cloudplatform/security/principal/PrincipalAccessor.html)
*   [`AuthTokenAccessor`](https://sap.github.io/cloud-sdk/java-api/v5/com/sap/cloud/sdk/cloudplatform/security/AuthTokenAccessor.html)

### Storing Information[​](https://sap.github.io/cloud-sdk/docs/java/features/multi-tenancy/thread-context#storing-information "Direct link to Storing Information")

The [`ThreadContext`](https://sap.github.io/cloud-sdk/java-api/v5/com/sap/cloud/sdk/cloudplatform/thread/ThreadContext.html) allows for some manipulation by the application. However, oftentimes it is more convenient to leverage the `executeWith...()` functionality offered by the dedicated accessors.

Consider a scenario where some part of the code should run on behalf of a specific tenant. In that case you can override the current tenant explicitly:

`TenantAccessor.executeWithTenant(customTenant, () -> doStuff());`

CAP Integration

The above does not apply for accessors like `TenantAccessor`, `PrincipalAccessor`, `RequestHeaderAccessor` when using the CAP framework (with the `cds-integration-cloud-sdk` dependency). When using CAP the Tenant, Principal, and Headers are derived from the `RequestContext`. Please refer to [this section](https://cap.cloud.sap/docs/java/request-contexts#defining-requestcontext) on how to override existing values in the CAP context.

caution

Be aware, that the `executeWith` methods shown above only replaces the given property, but does not update properties derived from it.

Example: You have a special `AuthToken`, that you propagate with `AuthTokenAccessor.executeWithAuthToken`. Inside the given code block only the `AuthToken` will be replaced, while e.g. the `Tenant` is the same as in the original context.

If you want to start a fresh context based on a given `AuthToken`, for example accessing information of the provider tenant while in a subscriber context, have a look at this code:

`Tenant retrieveProviderTenant(){    // retrieves an access token from the provider context    AuthToken providerXsuaaAccessToken = new ScpCfAuthTokenFacade().tryGetXsuaaServiceToken().get();    ThreadContextExecutor        // create a new, empty context        .fromNewContext()        // add the provider token into the new context        .withListeners(new AuthTokenThreadContextListener(providerXsuaaAccessToken))        // return the actual provider tenant        .execute(TenantAccessor::getCurrentTenant);}`

The `RequestHeaderAccessor#getHeaderContainer()` method provides convenient access to the HTTP headers of the current incoming request. It returns an instance of `RequestHeaderContainer`, which is, by API contract, an **immutable** container that allows _case insensitive_ access to HTTP header values. Although the `RequestHeaderContainer` cannot be altered once created, there are scenarios where manipulating HTTP headers is required. In such cases, a new instance of `RequestHeaderContainer` can be created in a few different ways.

A common way to represent HTTP headers is to use `Map<String, String>` for `1:1` relationships between header names and values or even `Map<String, Collection<String>>` for `1:n` relationships. To make the transition from either of those representations to the SAP Cloud SDK's `RequestHeaderContainer` as easy as possible, the `DefaultRequestHeaderContainer` offers corresponding factory methods:

*   `fromSingleValueMap(Map<String, String>)` and
*   `fromMultiValueMap(Map<String, ? extends Iterable<String>>)`

The latter one also enables convenient interoperability with the [Spring Headers](https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/http/HttpHeaders.html):

`@RequestMapping( method = RequestMethod.GET )public ResponseEntity<ExampleResponse> getExample( @RequestHeader final HttpHeaders headers){  final RequestHeaderContainer container = DefaultRequestHeaderContainer.fromMultiValueMap(headers);  RequestHeaderAccessor.executeWithHeaderContainer(container, () -> {      Tenant tenant = TenantAccessor.getCurrentTenant();  });}`

Besides these two factory methods, the `DefaultRequestHeaderContainer` also offers the possibility to create an instance of `RequestHeaderContainer.Builder` through the static `builder()` method. An example for how the returned `Builder` can be used is shown in the chapter below.

Additionally, to make customizing the current HTTP headers even easier, the `RequestHeaderAccessor` comes with an overload of the `executeWithHeaderContainer` method that accepts a `Map<String, String>`.

As pointed out above, the `RequestHeaderContainer` is an **immutable** structure. Therefore, updating an already existing instance is impossible.

**However**, in cases where you would like to, for example, just add a new custom header to the set of existing headers, the `RequestHeaderContainer` offers the `toBuilder` method. As the name suggests, this method can be used to retrieve an instance of `RequestHeaderContainer.Builder`. In contrast to the `RequestHeaderContainer`, the `Builder` can be **mutated** as much as needed. Additionally, the `toBuilder` method will make sure that the returned `Builder` instance is already pre-filled with all HTTP headers that are also present in the instance of `RequestHeaderContainer`.

To make things less theoretical, let's examine an example.

Example: Usage of the Builder
