Module org.easymock

# Package org.easymock.internal

- 

Interface Summary 

Interface
Description

IClassInstantiator

Used to instantiate a given class.

IMocksBehavior

The behavior of a mock.

IMocksControlState

Current state of a mocks control.

IProxyFactory

Reponsible of creating proxies for objects.

- 

Class Summary 

Class
Description

AndroidClassProxyFactory

Mocks concrete classes for Android's runtime by generating dex files.

AndroidSupport

Android-specific support.

ArgumentToString

Utility class to convert method arguments to Strings

BridgeMethodResolver

Code taken from the Spring
 framework.

ClassInstantiatorFactory

Factory returning a `IClassInstantiator`for the current JVM

ClassMockingData

Class containing the data required for a class mock to work.

ClassProxyFactory

Factory generating a mock for a class.

ClassProxyFactory.MockMethodInterceptor
 

DefaultClassInstantiator

Default class instantiator that is pretty limited.

EasyMockProperties

Contains properties used by EasyMock to change its default behavior.

EasyMockStatement

JUnit Statement for use by JUnit Rule or JUnit Runner to process `Mock` and `TestSubject` annotations.

ErrorMessage

The full content of an error message reporting to the user.

ExpectedInvocation

One expected invocation.

ExpectedInvocationAndResult

One expected invocation and its result.

ExpectedInvocationAndResults

The pair of an expected invocation and its results.

Injection

Described mock instance for injection.

InjectionPlan

Container for mock injections and test subject injection targets.

InjectionTarget

Applies an `Injection` to a target field.

Injector

Performs creation of mocks and injection into test subjects in accordance with annotations present in the host object.

Invocation

Represents a method invocation on a mock object.

JavaProxyFactory

Proxy factory creating proxies from an interface using the standard JDK proxy API.

LastControl

The last mocks control used in the current thread.

MethodSerializationWrapper

Wrapper used to serialize a `java.lang.reflect.Method` object when a mock is serialized.

MockBuilder<T>

Default implementation of IMockBuilder.

MockInvocationHandler

The handler of all invocations on a mock interface.

MocksBehavior

Default implementation of `IMocksBehavior`.

MocksControl

Controls all the mocks created by `EasyMock`.

ObjectMethodsFilter

The filter catching all calls to the mock.

ObjenesisClassInstantiator

Class instantiator using Objenesis to perform the instantiation without calling any constructor.

PrimitiveUtils

Helper class for primitive types.

Range

The range of a number of invocations.

RecordState

State in which a mock is recording its behavior.

ReflectionUtils

Helper class for reflection.

ReplayState

A mock has two states, record and replay.

Result

The result of an invocation on a mock.

Results

The results of a specific call on a mock.

ThrowableWrapper

Wraps a Throwable that was thrown by a method invocation so that EasyMock knows the difference between an invocation
 exception and an real unexpected one.

UnorderedBehavior

A bit badly named since this class is used for both ordered and unordered expectations.

- 

Exception Summary 

Exception
Description

AssertionErrorWrapper

Wraps an AssertionError that was thrown by a method invocation so that EasyMock knows the difference between an invocation
 exception and an real unexpected one.

RuntimeExceptionWrapper

Wraps a RuntimeException that was thrown by a method invocation so that EasyMock knows the difference between an invocation
 exception and an real unexpected one.

- 

Annotation Types Summary 

Annotation Type
Description

IgnoreAnimalSniffer