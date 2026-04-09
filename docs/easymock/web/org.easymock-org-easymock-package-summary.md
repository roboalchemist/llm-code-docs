Module org.easymock

# Package org.easymock

- 

Interface Summary 

Interface
Description

IAnswer<T>

Used to answer expected calls.

IArgumentMatcher

Decides whether an actual argument is accepted.

IExpectationSetters<T>

Allows setting expectations for an associated expected invocation.

IMockBuilder<T>

Helps the creation of partial mocks with `EasyMock`.

IMocksControl

Controls all the mock objects created by it.

- 

Class Summary 

Class
Description

Capture<T>

Will contain what was captured by the `capture()` matcher.

ConstructorArgs

Class wrapping arguments to create a partial class mock that gets
 instantiated by calling one of its constructors.

EasyMock

Main EasyMock class.

EasyMockExtension

JUnit 5 replaced the previous `RunWith` annotation
 (which made use of `EasyMockRunner`) with the new
 `ExtendWith` annotation.

EasyMockListener
 

EasyMockRule

JUnit Rule used to process `Mock` and `TestSubject` annotations.

EasyMockRunner

JUnit runner used to process `Mock` and `TestSubject` annotations.

EasyMockSupport

Helper class to keep track of mocks easily.

- 

Enum Summary 

Enum
Description

CaptureType

Defines how arguments will be captured by a `Capture` object.

LogicalOperator

See `EasyMock.cmp(T, java.util.Comparator<? super T>, org.easymock.LogicalOperator)`

MockType

Enum describing the 3 possibles kind of mocks

- 

Annotation Types Summary 

Annotation Type
Description

Mock

Annotation to set on a field so that `EasyMockRunner`, `EasyMockRule` or `EasyMockSupport.injectMocks(Object)`
 will inject a mock to it.

Preview

Indicated that the annotated item is new and might be tweaked a little if needed.

TestSubject

Annotation to set on a field so that `EasyMockRunner`, `EasyMockRule` or `EasyMockSupport.injectMocks(Object)`
 will inject mocks created with `Mock` on its fields.