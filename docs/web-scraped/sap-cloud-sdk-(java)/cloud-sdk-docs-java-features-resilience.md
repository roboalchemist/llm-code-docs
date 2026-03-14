# Source: https://sap.github.io/cloud-sdk/docs/java/features/resilience

Title: Resilience Capabilities | SAP Cloud SDK

URL Source: https://sap.github.io/cloud-sdk/docs/java/features/resilience

Markdown Content:
The SAP Cloud SDK for Java provides abstractions for some frequently used resilience patterns like timeout, retry, rate limiter, or circuit breaker. Applying such patterns helps to make an application more resilient against failures it might encounter.

The following article describes which resilience features the SAP Cloud SDK offers and how to apply them. If you are looking for a quick start with resilience also check out our [dedicated tutorial](https://developers.sap.com/tutorials/s4sdk-resilience.html) on the topic!

Using the Resilience API[​](https://sap.github.io/cloud-sdk/docs/java/features/resilience#using-the-resilience-api "Direct link to Using the Resilience API")
-------------------------------------------------------------------------------------------------------------------------------------------------------------

To make use of the resilience capabilities by the SAP Cloud SDK, add the following dependency to your project:

`<dependency>    <groupId>com.sap.cloud.sdk.cloudplatform</groupId>    <artifactId>resilience</artifactId></dependency>`

The SAP Cloud SDK allows running any code in the context of one or more resilience patterns. There are two essential building blocks for achieving this:

1.   The `ResilienceConfiguration` that determines which patterns should be applied.
2.   The `ResilienceDecorator` is capable of applying the configuration to an operation.

The fluent [Resilience Configuration API](https://sap.github.io/cloud-sdk/java-api/v5/com/sap/cloud/sdk/cloudplatform/resilience/ResilienceConfiguration.html) provides builders that help with assembling different resilience patterns and their associated parameters. Which patterns are available and how to use them is explained in the [dedicated section below](https://sap.github.io/cloud-sdk/docs/java/features/resilience#building-a-resilience-configuration).

The [Resilience Decorator](https://sap.github.io/cloud-sdk/java-api/v5/com/sap/cloud/sdk/cloudplatform/resilience/ResilienceDecorator.html) is capable of applying such a configuration to a given `Callable` or `Supplier`.

### Executing Operations[​](https://sap.github.io/cloud-sdk/docs/java/features/resilience#executing-operations "Direct link to Executing Operations")

Consider the following code:

`result = ResilienceDecorator.executeSupplier(() -> operation(), configuration);`

This code executes `operation()` in a resilient manner according to a `ResilienceConfiguration`. The decorator will apply all in `configuration` configured patterns and all logic that is needed to combine these patterns.

Some resilience patterns are applied over multiple executions of the same operation. For example, the circuit breaker will prevent further executions if a significant portion of previous attempts failed.

To understand how the SAP Cloud SDK applies this concept consider the following snippet:

`configuration1 = ResilienceConfiguration.of("config-id-1");configuration2 = ResilienceConfiguration.of("config-id-1");configuration3 = ResilienceConfiguration.of("config-id-2");ResilienceDecorator.executeSupplier(() -> operation(), configuration1);ResilienceDecorator.executeSupplier(() -> operation(), configuration1);ResilienceDecorator.executeSupplier(() -> operation(), configuration2);ResilienceDecorator.executeSupplier(() -> operation(), configuration3);`

Here executions one, two, and three will all share the same "resilience state". This means that they will share the same instance of a circuit breaker or bulkhead. The state is shared via [the identifier](https://sap.github.io/cloud-sdk/docs/java/features/resilience#building-a-resilience-configuration) of the associated configuration.

#### Operation Types[​](https://sap.github.io/cloud-sdk/docs/java/features/resilience#operation-types "Direct link to Operation Types")

The decorator operates with two kinds of operations:

[Callable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/Callable.html)May throw checked or unchecked Exceptions
[Supplier](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html)May only throw unchecked Exceptions

Noticeable is the difference in signatures: _Callable_ throws a _checked exception_ while _Supplier_ does not. You can choose whatever fits your use case best.

#### Execution Variants[​](https://sap.github.io/cloud-sdk/docs/java/features/resilience#execution-variants "Direct link to Execution Variants")

The decorator allows for three different ways of applying a configuration:

_Execute_ Immediately runs the operation
_Decorate_ Returns a new operation to be run later
_Queue_ Immediately runs the operation asynchronously

In case your operation should run asynchronously we highly recommend you leverage the `queue` functionality. The decorator will ensure the [Thread Context](https://sap.github.io/cloud-sdk/docs/java/features/multi-tenancy/thread-context) with Tenant and Principal information is propagated correctly to new Threads.

note

Note that the Resilience Decorator will try to propagate the current [Thread Context](https://sap.github.io/cloud-sdk/docs/java/features/multi-tenancy/thread-context) at the _time the decorator is invoked_. This is important when you are decorating a Callable or Supplier and running it later. The Thread Context must be available whenever `decorateCallable` or `decorateSupplier` is evaluated. If the call to `ResilienceDecorator` should take place asynchronously, you should [follow these steps](https://sap.github.io/cloud-sdk/docs/java/features/multi-tenancy/thread-context#running-asynchronous-operations) to ensure the Thread Context is available.

#### Failures and Fallbacks[​](https://sap.github.io/cloud-sdk/docs/java/features/resilience#failures-and-fallbacks "Direct link to Failures and Fallbacks")

An operation might fail for two reasons:

1.   The operation itself encounters a failure and throws an error or exception
2.   A resilience pattern causes the operation to fail (e.g. the circuit breaker prevents further invocations)

The SAP Cloud SDK wraps all kind of checked and unchecked exceptions into a `ResilienceRuntimeException` and throws them.

To deal with failures one can either catch the `ResilienceRuntimeException` or provide a fallback function:

`executeCallable(() -> operation(), configuration,(throwable) -> {    log.debug("Encountered a failure in operation: ", throwable);    log.debug("Proceeding with fallback value: {}", fallback);    return fallback;});`

In the case of `Callable`, this relieves you of the need to catch the exception at the outer level.

### Building a Resilience Configuration[​](https://sap.github.io/cloud-sdk/docs/java/features/resilience#building-a-resilience-configuration "Direct link to Building a Resilience Configuration")

A new `ResilienceConfiguration`_with default values_ is created by providing an identifier for it:

`configuration = ResilienceConfiguration.of("identifier");`

The identifier can be either a string or a class. In the case of the latter, the (full) class name will be used as the identifier. The identifier will be used to apply resilience patterns across [multiple invocations to operations](https://sap.github.io/cloud-sdk/docs/java/features/resilience#executing-operations).

Check [the Javadoc](https://sap.github.io/cloud-sdk/java-api/v5/com/sap/cloud/sdk/cloudplatform/resilience/ResilienceConfiguration.html#of-java.lang.String-) for which patterns and parameters will be applied by default. You can also create a configuration with all patterns disabled:

`configuration = ResilienceConfiguration.empty("identifier");`

Individual resilience patterns are configured via dedicated builder classes like `TimeLimiterConfiguration` and are added to the configuration via dedicated setters, e.g. `timeLimiterConfiguration()`. For details see the list of [Resilience Capabilities](https://sap.github.io/cloud-sdk/docs/java/features/resilience#resilience-capabilities) below.

#### Multi Tenancy[​](https://sap.github.io/cloud-sdk/docs/java/features/resilience#multi-tenancy "Direct link to Multi Tenancy")

The SAP Cloud SDK is capable of applying the different resilience patterns in a tenant and principal aware manner. Consider for example the Bulkhead pattern which limits the number of parallel executions. If the operation is tenant-specific then you would probably want to avoid one tenant blocking all others.

For this reason, the SAP Cloud SDK _by default_ isolates resilience patterns based on tenant and principal, if they are available. This strategy can be configured, e.g. for running _without any isolation_ use:

`configuration.isolationMode(ResilienceIsolationMode.NO_ISOLATION);`

Other than no isolation there are essentially two modes for tenant and/or principal isolation:

Required Always isolates on tenant and/or principal level, will throw an exception if no tenant/principal is available
Optional Only isolates if tenant and/or principal information is available

Details can be found on the API reference of [`ResilienceIsolationMode`](https://sap.github.io/cloud-sdk/java-api/v5/com/sap/cloud/sdk/cloudplatform/resilience/ResilienceIsolationMode.html).

Resilience Capabilities[​](https://sap.github.io/cloud-sdk/docs/java/features/resilience#resilience-capabilities "Direct link to Resilience Capabilities")
----------------------------------------------------------------------------------------------------------------------------------------------------------

The following resilience patterns are available and can be configured in a Resilience Configuration:

Timeout _[TimeLimiterConfiguration](pathname:///java-api/v5/com/sap/cloud/sdk/cloudplatform/resilience/ResilienceConfiguration.TimeLimiterConfiguration.html)_ Limit how long an operation may run before it should be interrupted
Rate Limiter _RateLimiterConfiguration_ Limit the number of operations accepted in a window of time
Retry _[RetryConfiguration](pathname:///java-api/v5/com/sap/cloud/sdk/cloudplatform/resilience/ResilienceConfiguration.RetryConfiguration.html)_ Retry a failed operation a limited amount of times before failing
Circuit Breaker _[CircuitBreakerConfiguration](pathname:///java-api/v5/com/sap/cloud/sdk/cloudplatform/resilience/ResilienceConfiguration.CircuitBreakerConfiguration.html)_ Reject attempts if too many failures occurred in the past
Bulkhead

(also known as Shed Load or Load Shedding)_[BulkheadConfiguration](pathname:///java-api/v5/com/sap/cloud/sdk/cloudplatform/resilience/ResilienceConfiguration.BulkheadConfiguration.html)_ Limit how many instances of this operation may run in parallel

You can find good explanations on how the individual patterns behave on the [documentation of resilience4j](https://resilience4j.readme.io/docs/) which the SAP Cloud SDK uses under the hood to perform resilient operations.

Be aware that the patterns interact with each other. They are applied in the following order:

Fallback ( Retry ( CircuitBreaker ( RateLimiter ( TimeLimiter ( Bulkhead ( Function ) ) ) ) ) )

If you read from right to left, it shows you the order in which the aspects will be applied. For example, `Fallbacks` are called last while `Bulkhead` is the first aspect applied. Hence, exceptions are also propagated from right to left.

Based on the order, the following inferences (not exhaustive) can be made:

*   Every timeout will trigger a retry, if configured.
*   Only if all retries failed the fallback function will be considered.

You can get more details in the Resilience4j [official documentation.](https://resilience4j.readme.io/docs/getting-started-3#aspect-order)
