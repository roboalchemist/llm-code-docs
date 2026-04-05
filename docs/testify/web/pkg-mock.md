# mock Package Documentation

**Source:** [pkg.go.dev/github.com/stretchr/testify/mock](https://pkg.go.dev/github.com/stretchr/testify/mock)

- **Version:** v1.11.1
- **License:** MIT

## Overview

Package `mock` provides a system for mocking objects and verifying that calls are happening as expected. The `Mock` struct is typically embedded into a test object to track activity on another object.

### Example Usage

```go
type MyTestObject struct {
  mock.Mock
  // other fields go here as normal
}

func (o *MyTestObject) SavePersonDetails(firstname, lastname string, age int) (int, error) {
  args := o.Called(firstname, lastname, age)
  return args.Int(0), args.Error(1)
}
```

Reading arguments strongly typed:

```go
args.Int(0)      // First argument as int
args.Bool(1)     // Second argument as bool
args.String(2)   // Third argument as string
```

For custom types, use `Arguments.Get(index)` with type assertion:

```go
return args.Get(0).(*MyObject), args.Get(1).(*AnotherObjectOfMine)
```

## Constants

```go
const Anything = "mock.Anything"
```

`Anything` is used in `Diff` and `Assert` when the argument being tested shouldn't be taken into consideration.

## Functions

### AssertExpectationsForObjects

```go
func AssertExpectationsForObjects(t TestingT, testObjects ...interface{}) bool
```

Asserts that everything specified with `On` and `Return` of the specified objects was in fact called as expected. Calls may have occurred in any order.

### InOrder

```go
func InOrder(calls ...*Call)
```

Defines the order in which the calls should be made.

Example:

```go
InOrder(
	Mock.On("init").Return(nil),
	Mock.On("Do").Return(nil),
)
```

### MatchedBy

```go
func MatchedBy(fn interface{}) argumentMatcher
```

Can be used to match a mock call based on only certain properties from a complex struct or some calculation. It takes a function that will be evaluated with the called argument and will return `true` when there's a match and `false` otherwise.

Example:

```go
m.On("Do", MatchedBy(func(req *http.Request) bool {
  return req.Host == "example.com"
}))
```

`fn` must be a function accepting a single argument (of the expected type) which returns a bool. If `fn` doesn't match the required signature, `MatchedBy()` panics.

## Types

### AnythingOfTypeArgument

```go
type AnythingOfTypeArgument = anythingOfTypeArgument
```

**Deprecated:** This is an implementation detail. Use the `AnythingOfType` constructor instead.

#### AnythingOfType

```go
func AnythingOfType(t string) AnythingOfTypeArgument
```

Returns a special value containing the name of the type to check for. The type name will be matched against the type name returned by `reflect.Type.String()`.

Used in `Diff` and `Assert`.

Example:

```go
args.Assert(t, AnythingOfType("string"), AnythingOfType("int"))
```

### Arguments

```go
type Arguments []interface{}
```

`Arguments` holds an array of method arguments or return values.

#### Arguments.Assert

```go
func (args Arguments) Assert(t TestingT, objects ...interface{}) bool
```

Compares the arguments with the specified objects and fails if they do not exactly match.

#### Arguments.Bool

```go
func (args Arguments) Bool(index int) bool
```

Gets the argument at the specified index. Panics if there is no argument, or if the argument is of the wrong type.

#### Arguments.Diff

```go
func (args Arguments) Diff(objects []interface{}) (string, int)
```

Gets a string describing the differences between the arguments and the specified objects.

Returns the diff string and number of differences found.

#### Arguments.Error

```go
func (args Arguments) Error(index int) error
```

Gets the argument at the specified index. Panics if there is no argument, or if the argument is of the wrong type.

#### Arguments.Get

```go
func (args Arguments) Get(index int) interface{}
```

Returns the argument at the specified index.

#### Arguments.Int

```go
func (args Arguments) Int(index int) int
```

Gets the argument at the specified index. Panics if there is no argument, or if the argument is of the wrong type.

#### Arguments.Is

```go
func (args Arguments) Is(objects ...interface{}) bool
```

Gets whether the objects match the arguments specified.

#### Arguments.String

```go
func (args Arguments) String(indexOrNil ...int) string
```

Gets the argument at the specified index. Panics if there is no argument, or if the argument is of the wrong type.

If no index is provided, `String()` returns a complete string representation of the arguments.

### Call

```go
type Call struct {
	Parent          *Mock
	Method          string
	Arguments       Arguments
	ReturnArguments Arguments
	Repeatability   int
	WaitFor         <-chan time.Time
	RunFn           func(Arguments)
	PanicMsg        *string
}
```

`Call` represents a method call and is used for setting expectations, as well as recording activity.

#### Call.After

```go
func (c *Call) After(d time.Duration) *Call
```

Sets how long to block until the call returns.

```go
Mock.On("MyMethod", arg1, arg2).After(time.Second)
```

#### Call.Maybe

```go
func (c *Call) Maybe() *Call
```

Allows the method call to be optional. Not calling an optional method will not cause an error while asserting expectations.

#### Call.NotBefore

```go
func (c *Call) NotBefore(calls ...*Call) *Call
```

Indicates that the mock should only be called after the referenced calls have been called as expected. The referenced calls may be from the same mock instance and/or other mock instances.

```go
Mock.On("Do").Return(nil).NotBefore(
    Mock.On("Init").Return(nil)
)
```

#### Call.On

```go
func (c *Call) On(methodName string, arguments ...interface{}) *Call
```

Chains a new expectation description onto the mocked interface.

```go
Mock.
   On("MyMethod", 1).Return(nil).
   On("MyOtherMethod", 'a', 'b', 'c').Return(errors.New("Some Error"))
```

#### Call.Once

```go
func (c *Call) Once() *Call
```

Indicates that the mock should only return the value once.

```go
Mock.On("MyMethod", arg1, arg2).Return(returnArg1, returnArg2).Once()
```

#### Call.Panic

```go
func (c *Call) Panic(msg string) *Call
```

Specifies if the function call should fail and the panic message.

```go
Mock.On("DoSomething").Panic("test panic")
```

#### Call.Return

```go
func (c *Call) Return(returnArguments ...interface{}) *Call
```

Specifies the return arguments for the expectation.

```go
Mock.On("DoSomething").Return(errors.New("failed"))
```

#### Call.Run

```go
func (c *Call) Run(fn func(args Arguments)) *Call
```

Sets a handler to be called before returning. It can be used when mocking a method (such as an unmarshaler) that takes a pointer to a struct and sets properties in such struct.

```go
Mock.On("Unmarshal", AnythingOfType("*map[string]interface{}")).Return().Run(func(args Arguments) {
	arg := args.Get(0).(*map[string]interface{})
	arg["foo"] = "bar"
})
```

#### Call.Times

```go
func (c *Call) Times(i int) *Call
```

Indicates that the mock should only return the indicated number of times.

```go
Mock.On("MyMethod", arg1, arg2).Return(returnArg1, returnArg2).Times(5)
```

#### Call.Twice

```go
func (c *Call) Twice() *Call
```

Indicates that the mock should only return the value twice.

```go
Mock.On("MyMethod", arg1, arg2).Return(returnArg1, returnArg2).Twice()
```

#### Call.Unset

```go
func (c *Call) Unset() *Call
```

Removes all mock handlers that satisfy the call instance arguments from being called. Only supported on call instances with static input arguments.

Example:

```go
Mock.
   On("MyMethod", 2, 2).Return(0).
   On("MyMethod", 3, 3).Return(0).
   On("MyMethod", Anything, Anything).Return(0)
Mock.On("MyMethod", 3, 3).Unset()
```

After this, the only handler remaining would be `"MyMethod(2, 2)"`.

#### Call.WaitUntil

```go
func (c *Call) WaitUntil(w <-chan time.Time) *Call
```

Sets the channel that will block the mock's return until its closed or a message is received.

```go
Mock.On("MyMethod", arg1, arg2).WaitUntil(time.After(time.Second))
```

### FunctionalOptionsArgument

```go
type FunctionalOptionsArgument struct {
	// contains filtered or unexported fields
}
```

`FunctionalOptionsArgument` contains a list of functional options arguments expected for use when matching a list of arguments.

#### FunctionalOptions

```go
func FunctionalOptions(values ...interface{}) *FunctionalOptionsArgument
```

Returns a `FunctionalOptionsArgument` object containing the expected functional-options to check for.

Example:

```go
args.Assert(t, FunctionalOptions(foo.Opt1("strValue"), foo.Opt2(613)))
```

#### FunctionalOptionsArgument.String

```go
func (f *FunctionalOptionsArgument) String() string
```

Returns the string representation of `FunctionalOptionsArgument`.

### IsTypeArgument

```go
type IsTypeArgument struct {
	// contains filtered or unexported fields
}
```

`IsTypeArgument` is a struct that contains the type of an argument for use when type checking. This is an alternative to `AnythingOfType`. Used in `Arguments.Diff` and `Arguments.Assert`.

#### IsType

```go
func IsType(t interface{}) *IsTypeArgument
```

Returns an `IsTypeArgument` object containing the type to check for. You can provide a zero-value of the type to check. This is an alternative to `AnythingOfType`. Used in `Arguments.Diff` and `Arguments.Assert`.

Example:

```go
args.Assert(t, IsType(""), IsType(0))
```

### Mock

```go
type Mock struct {
	ExpectedCalls []*Call
	Calls         []Call
}
```

`Mock` is the workhorse used to track activity on another object.

#### Mock.AssertCalled

```go
func (m *Mock) AssertCalled(t TestingT, methodName string, arguments ...interface{}) bool
```

Asserts that the method was called. It can produce a false result when an argument is a pointer type and the underlying value changed after calling the mocked method.

#### Mock.AssertExpectations

```go
func (m *Mock) AssertExpectations(t TestingT) bool
```

Asserts that everything specified with `On` and `Return` was in fact called as expected. Calls may have occurred in any order.

#### Mock.AssertNotCalled

```go
func (m *Mock) AssertNotCalled(t TestingT, methodName string, arguments ...interface{}) bool
```

Asserts that the method was not called. It can produce a false result when an argument is a pointer type and the underlying value changed after calling the mocked method.

#### Mock.AssertNumberOfCalls

```go
func (m *Mock) AssertNumberOfCalls(t TestingT, methodName string, expectedCalls int) bool
```

Asserts that the method was called `expectedCalls` times.

#### Mock.Called

```go
func (m *Mock) Called(arguments ...interface{}) Arguments
```

Tells the mock object that a method has been called, and gets an array of arguments to return. Panics if the call is unexpected (i.e. not preceded by appropriate `.On` `.Return()` calls). If `Call.WaitFor` is set, blocks until the channel is closed or receives a message.

#### Mock.IsMethodCallable

```go
func (m *Mock) IsMethodCallable(t TestingT, methodName string, arguments ...interface{}) bool
```

Checks that the method can be called. If the method was called more than `Repeatability` return false.

#### Mock.MethodCalled

```go
func (m *Mock) MethodCalled(methodName string, arguments ...interface{}) Arguments
```

Tells the mock object that the given method has been called, and gets an array of arguments to return. Panics if the call is unexpected (i.e. not preceded by appropriate `.On` `.Return()` calls). If `Call.WaitFor` is set, blocks until the channel is closed or receives a message.

#### Mock.On

```go
func (m *Mock) On(methodName string, arguments ...interface{}) *Call
```

Starts a description of an expectation of the specified method being called.

```go
Mock.On("MyMethod", arg1, arg2)
```

#### Mock.String

```go
func (m *Mock) String() string
```

Provides a `%v` format string for `Mock`. Note: this is used implicitly by `Arguments.Diff` if a `Mock` is passed. It exists because go's default `%v` formatting traverses the struct without acquiring the mutex, which is detected by `go test -race`.

#### Mock.Test

```go
func (m *Mock) Test(t TestingT)
```

Sets the `TestingT` on which errors will be reported, otherwise errors will cause a panic. `Test` should not be called on an object that is going to be used in a goroutine other than the one running the test function.

#### Mock.TestData

```go
func (m *Mock) TestData() objx.Map
```

Holds any data that might be useful for testing. Testify ignores this data completely allowing you to do whatever you like with it.

### TestingT

```go
type TestingT interface {
	Logf(format string, args ...interface{})
	Errorf(format string, args ...interface{})
	FailNow()
}
```

`TestingT` is an interface wrapper around `*testing.T`.

## Source Files

- `doc.go`
- `mock.go`
