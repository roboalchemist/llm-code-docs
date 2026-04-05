# assert Package Documentation

**Source:** [pkg.go.dev/github.com/stretchr/testify/assert](https://pkg.go.dev/github.com/stretchr/testify/assert)

- **Version:** v1.11.1
- **License:** MIT

## Overview

Package assert provides a set of comprehensive testing tools for use with the normal Go testing system. All functions in this package return a bool value indicating whether the assertion has passed.

### Example Usage

Basic usage with assert functions:

```go
import (
  "testing"
  "github.com/stretchr/testify/assert"
)

func TestSomething(t *testing.T) {
  var a string = "Hello"
  var b string = "Hello"
  assert.Equal(t, a, b, "The two words should be the same.")
}
```

For multiple assertions, use the Assertions object:

```go
func TestSomething(t *testing.T) {
  assert := assert.New(t)
  var a string = "Hello"
  var b string = "Hello"
  assert.Equal(a, b, "The two words should be the same.")
}
```

---

## Functions

### CallerInfo

```go
func CallerInfo() []string
```

CallerInfo returns an array of strings containing the file and line number of each stack frame leading from the current test to the assert call that failed.

### Condition

```go
func Condition(t TestingT, comp Comparison, msgAndArgs ...interface{}) bool
```

Condition uses a Comparison to assert a complex condition.

### Conditionf

```go
func Conditionf(t TestingT, comp Comparison, msg string, args ...interface{}) bool
```

Conditionf uses a Comparison to assert a complex condition.

### Contains

```go
func Contains(t TestingT, s, contains interface{}, msgAndArgs ...interface{}) bool
```

Contains asserts that the specified string, list(array, slice...) or map contains the specified substring or element.

```go
assert.Contains(t, "Hello World", "World")
assert.Contains(t, ["Hello", "World"], "World")
assert.Contains(t, {"Hello": "World"}, "Hello")
```

### Containsf

```go
func Containsf(t TestingT, s interface{}, contains interface{}, msg string, args ...interface{}) bool
```

Containsf asserts that the specified string, list(array, slice...) or map contains the specified substring or element.

### DirExists

```go
func DirExists(t TestingT, path string, msgAndArgs ...interface{}) bool
```

DirExists checks whether a directory exists in the given path. It also fails if the path is a file rather a directory or there is an error checking whether it exists.

### DirExistsf

```go
func DirExistsf(t TestingT, path string, msg string, args ...interface{}) bool
```

DirExistsf checks whether a directory exists in the given path.

### ElementsMatch

```go
func ElementsMatch(t TestingT, listA, listB interface{}, msgAndArgs ...interface{}) (ok bool)
```

ElementsMatch asserts that the specified listA(array, slice...) is equal to specified listB(array, slice...) ignoring the order of the elements. If there are duplicate elements, the number of appearances of each of them in both lists should match.

```go
assert.ElementsMatch(t, [1, 3, 2, 3], [1, 3, 3, 2])
```

### ElementsMatchf

```go
func ElementsMatchf(t TestingT, listA interface{}, listB interface{}, msg string, args ...interface{}) bool
```

ElementsMatchf asserts that the specified listA(array, slice...) is equal to specified listB(array, slice...) ignoring the order of the elements.

### Empty

```go
func Empty(t TestingT, object interface{}, msgAndArgs ...interface{}) bool
```

Empty asserts that the given value is "empty".

- [Zero values](https://go.dev/ref/spec#The_zero_value) are "empty"
- Arrays are "empty" if every element is the zero value of the type
- Slices, maps and channels with zero length are "empty"
- Pointer values are "empty" if the pointer is nil or if the pointed value is "empty"

```go
assert.Empty(t, obj)
```

### Emptyf

```go
func Emptyf(t TestingT, object interface{}, msg string, args ...interface{}) bool
```

Emptyf asserts that the given value is "empty".

### Equal

```go
func Equal(t TestingT, expected, actual interface{}, msgAndArgs ...interface{}) bool
```

Equal asserts that two objects are equal.

```go
assert.Equal(t, 123, 123)
```

Pointer variable equality is determined based on the equality of the referenced values (as opposed to the memory addresses). Function equality cannot be determined and will always fail.

### EqualError

```go
func EqualError(t TestingT, theError error, errString string, msgAndArgs ...interface{}) bool
```

EqualError asserts that a function returned an error (i.e. not `nil`) and that it is equal to the provided error.

```go
actualObj, err := SomeFunction()
assert.EqualError(t, err, expectedErrorString)
```

### EqualErrorf

```go
func EqualErrorf(t TestingT, theError error, errString string, msg string, args ...interface{}) bool
```

EqualErrorf asserts that a function returned an error (i.e. not `nil`) and that it is equal to the provided error.

### EqualExportedValues

```go
func EqualExportedValues(t TestingT, expected, actual interface{}, msgAndArgs ...interface{}) bool
```

EqualExportedValues asserts that the types of two objects are equal and their public fields are also equal. This is useful for comparing structs that have private fields that could potentially differ.

```go
type S struct {
  Exported     int
  notExported  int
}
assert.EqualExportedValues(t, S{1, 2}, S{1, 3}) // => true
assert.EqualExportedValues(t, S{1, 2}, S{2, 3}) // => false
```

### EqualExportedValuesf

```go
func EqualExportedValuesf(t TestingT, expected interface{}, actual interface{}, msg string, args ...interface{}) bool
```

EqualExportedValuesf asserts that the types of two objects are equal and their public fields are also equal.

### EqualValues

```go
func EqualValues(t TestingT, expected, actual interface{}, msgAndArgs ...interface{}) bool
```

EqualValues asserts that two objects are equal or convertible to the larger type and equal.

```go
assert.EqualValues(t, uint32(123), int32(123))
```

### EqualValuesf

```go
func EqualValuesf(t TestingT, expected interface{}, actual interface{}, msg string, args ...interface{}) bool
```

EqualValuesf asserts that two objects are equal or convertible to the larger type and equal.

### Equalf

```go
func Equalf(t TestingT, expected interface{}, actual interface{}, msg string, args ...interface{}) bool
```

Equalf asserts that two objects are equal.

### Error

```go
func Error(t TestingT, err error, msgAndArgs ...interface{}) bool
```

Error asserts that a function returned an error (i.e. not `nil`).

```go
actualObj, err := SomeFunction()
assert.Error(t, err)
```

### ErrorAs

```go
func ErrorAs(t TestingT, err error, target interface{}, msgAndArgs ...interface{}) bool
```

ErrorAs asserts that at least one of the errors in err's chain matches target, and if so, sets target to that error value. This is a wrapper for errors.As.

### ErrorContains

```go
func ErrorContains(t TestingT, theError error, contains string, msgAndArgs ...interface{}) bool
```

ErrorContains asserts that a function returned an error (i.e. not `nil`) and that the error contains the specified substring.

```go
actualObj, err := SomeFunction()
assert.ErrorContains(t, err, expectedErrorSubString)
```

### ErrorIs

```go
func ErrorIs(t TestingT, err, target error, msgAndArgs ...interface{}) bool
```

ErrorIs asserts that at least one of the errors in err's chain matches target. This is a wrapper for errors.Is.

### Eventually

```go
func Eventually(t TestingT, condition func() bool, waitFor time.Duration, tick time.Duration, msgAndArgs ...interface{}) bool
```

Eventually asserts that given condition will be met in waitFor duration. The condition is evaluated every tick duration.

### Exactly

```go
func Exactly(t TestingT, expected, actual interface{}, msgAndArgs ...interface{}) bool
```

Exactly asserts that two objects are equal in both type and value. Differs from Equal as it performs a strict type check.

```go
assert.Exactly(t, int32(123), int32(123))
```

### Fail

```go
func Fail(t TestingT, failureMessage string, msgAndArgs ...interface{}) bool
```

Fails the test with the given failure message. Continues test execution.

### FailNow

```go
func FailNow(t TestingT, failureMessage string, msgAndArgs ...interface{}) bool
```

Fails the test with the given failure message and stops test execution immediately.

### False

```go
func False(t TestingT, value bool, msgAndArgs ...interface{}) bool
```

False asserts that the specified value is false.

```go
assert.False(t, myBool)
```

### FileExists

```go
func FileExists(t TestingT, path string, msgAndArgs ...interface{}) bool
```

FileExists checks whether a file exists in the given path. Fails if the path is a directory rather than a file or if there is an error checking whether it exists.

### Greater

```go
func Greater(t TestingT, e1 interface{}, e2 interface{}, msgAndArgs ...interface{}) bool
```

Greater asserts that the first element is greater than the second.

```go
assert.Greater(t, 2, 1)
assert.Greater(t, float64(2), float64(1))
assert.Greater(t, "b", "a")
```

### GreaterOrEqual

```go
func GreaterOrEqual(t TestingT, e1 interface{}, e2 interface{}, msgAndArgs ...interface{}) bool
```

Greater asserts that the first element is greater than or equal to the second.

```go
assert.GreaterOrEqual(t, 2, 1)
assert.GreaterOrEqual(t, 2, 2)
```

### HTTPBody

```go
func HTTPBody(handler http.HandlerFunc, method, url string, values url.Values) string
```

HTTPBody returns the response body of the given http handler as a string.

### HTTPBodyContains

```go
func HTTPBodyContains(t TestingT, handler http.HandlerFunc, method, url string, values url.Values, str string, msgAndArgs ...interface{}) bool
```

HTTPBodyContains asserts that the response body of the given HTTP handler contains the specified string.

### HTTPBodyNotContains

```go
func HTTPBodyNotContains(t TestingT, handler http.HandlerFunc, method, url string, values url.Values, str string, msgAndArgs ...interface{}) bool
```

HTTPBodyNotContains asserts that the response body of the given HTTP handler does not contain the specified string.

### HTTPError

```go
func HTTPError(t TestingT, handler http.HandlerFunc, method, url string, values url.Values, msgAndArgs ...interface{}) bool
```

HTTPError asserts that the given HTTP handler returns an error status code (4xx or 5xx).

### HTTPRedirect

```go
func HTTPRedirect(t TestingT, handler http.HandlerFunc, method, url string, values url.Values, msgAndArgs ...interface{}) bool
```

HTTPRedirect asserts that the given HTTP handler returns a redirect status code (3xx).

### HTTPStatusCode

```go
func HTTPStatusCode(t TestingT, handler http.HandlerFunc, method, url string, values url.Values, statuscode int, msgAndArgs ...interface{}) bool
```

HTTPStatusCode asserts that the given HTTP handler returns the specified status code.

### HTTPSuccess

```go
func HTTPSuccess(t TestingT, handler http.HandlerFunc, method, url string, values url.Values, msgAndArgs ...interface{}) bool
```

HTTPSuccess asserts that the given HTTP handler returns a success status code (2xx).

### Implements

```go
func Implements(t TestingT, interfaceObject interface{}, object interface{}, msgAndArgs ...interface{}) bool
```

Implements asserts that the object implements the interface.

```go
assert.Implements(t, (*Reader)(nil), new(os.File))
```

### InDelta

```go
func InDelta(t TestingT, expected, actual interface{}, delta float64, msgAndArgs ...interface{}) bool
```

InDelta asserts that the difference between expected and actual is less than or equal to delta.

```go
assert.InDelta(t, 100.01, 100.001, 0.01)
```

### InDeltaMapValues

```go
func InDeltaMapValues(t TestingT, expected, actual interface{}, delta float64, msgAndArgs ...interface{}) bool
```

InDeltaMapValues asserts that all values in two maps are equal within delta of each other.

### InDeltaSlice

```go
func InDeltaSlice(t TestingT, expected, actual interface{}, delta float64, msgAndArgs ...interface{}) bool
```

InDeltaSlice asserts that all elements in two slices are equal within delta of each other.

### InEpsilon

```go
func InEpsilon(t TestingT, expected, actual interface{}, epsilon float64, msgAndArgs ...interface{}) bool
```

InEpsilon asserts that the relative error between expected and actual is less than or equal to epsilon. Epsilon is a relative value (0 < epsilon <= 1).

```go
assert.InEpsilon(t, 100, 101, 0.01)
```

### InEpsilonSlice

```go
func InEpsilonSlice(t TestingT, expected, actual interface{}, epsilon float64, msgAndArgs ...interface{}) bool
```

InEpsilonSlice asserts that all elements in two slices have a relative error less than or equal to epsilon.

### IsDecreasing

```go
func IsDecreasing(t TestingT, object interface{}, msgAndArgs ...interface{}) bool
```

IsDecreasing asserts that the values in the specified slice/array are in strictly decreasing order.

```go
assert.IsDecreasing(t, []int{7, 5, 3, 2, 1})
```

### IsIncreasing

```go
func IsIncreasing(t TestingT, object interface{}, msgAndArgs ...interface{}) bool
```

IsIncreasing asserts that the values in the specified slice/array are in strictly increasing order.

```go
assert.IsIncreasing(t, []int{1, 2, 3, 5, 7})
```

### IsNonDecreasing

```go
func IsNonDecreasing(t TestingT, object interface{}, msgAndArgs ...interface{}) bool
```

IsNonDecreasing asserts that the values in the specified slice/array are in non-decreasing order (allows equal consecutive values).

### IsNonIncreasing

```go
func IsNonIncreasing(t TestingT, object interface{}, msgAndArgs ...interface{}) bool
```

IsNonIncreasing asserts that the values in the specified slice/array are in non-increasing order (allows equal consecutive values).

### IsType

```go
func IsType(t TestingT, expectedType, object interface{}, msgAndArgs ...interface{}) bool
```

IsType asserts that the object is of the specified type.

```go
assert.IsType(t, 0, uint32(10))
```

### JSONEq

```go
func JSONEq(t TestingT, expected string, actual string, msgAndArgs ...interface{}) bool
```

JSONEq asserts that two JSON strings are equal. Ignores whitespace and key ordering.

```go
assert.JSONEq(t, `{"hello": "world"}`, `{"world": "hello"}`)
```

### Len

```go
func Len(t TestingT, object interface{}, length int, msgAndArgs ...interface{}) bool
```

Len asserts that the specified object has the specified length. Applicable to strings, arrays, slices, maps, and channels.

```go
assert.Len(t, "Hello", 5)
assert.Len(t, [1, 2, 3], 3)
```

### Less

```go
func Less(t TestingT, e1 interface{}, e2 interface{}, msgAndArgs ...interface{}) bool
```

Less asserts that the first element is less than the second.

```go
assert.Less(t, 1, 2)
assert.Less(t, float64(1), float64(2))
assert.Less(t, "a", "b")
```

### LessOrEqual

```go
func LessOrEqual(t TestingT, e1 interface{}, e2 interface{}, msgAndArgs ...interface{}) bool
```

LessOrEqual asserts that the first element is less than or equal to the second.

```go
assert.LessOrEqual(t, 1, 2)
assert.LessOrEqual(t, 2, 2)
```

### Negative

```go
func Negative(t TestingT, e interface{}, msgAndArgs ...interface{}) bool
```

Negative asserts that the specified element is negative (< 0).

```go
assert.Negative(t, -5)
assert.Negative(t, -0.23)
```

### Never

```go
func Never(t TestingT, condition func() bool, waitFor time.Duration, tick time.Duration, msgAndArgs ...interface{}) bool
```

Never asserts that the given condition never returns true within the specified duration. The condition is evaluated every tick duration.

### New

```go
func New(t TestingT) *Assertions
```

New creates a new Assertions object for the given TestingT. This allows you to use assertion methods without passing the TestingT to each call.

```go
assert := assert.New(t)
assert.Equal(a, b)
```

### Nil

```go
func Nil(t TestingT, object interface{}, msgAndArgs ...interface{}) bool
```

Nil asserts that the specified object is nil.

```go
assert.Nil(t, err)
```

### NoDirExists

```go
func NoDirExists(t TestingT, path string, msgAndArgs ...interface{}) bool
```

NoDirExists asserts that a directory does not exist at the given path.

### NoError

```go
func NoError(t TestingT, err error, msgAndArgs ...interface{}) bool
```

NoError asserts that a function returned no error (i.e. `nil`).

```go
actualObj, err := SomeFunction()
assert.NoError(t, err)
```

### NoFileExists

```go
func NoFileExists(t TestingT, path string, msgAndArgs ...interface{}) bool
```

NoFileExists asserts that a file does not exist at the given path.

### NotContains

```go
func NotContains(t TestingT, s, contains interface{}, msgAndArgs ...interface{}) bool
```

NotContains asserts that the specified string, list (array, slice...) or map does not contain the specified substring or element.

```go
assert.NotContains(t, "Hello World", "Jane")
assert.NotContains(t, ["Hello", "World"], "Jane")
assert.NotContains(t, {"Hello": "World"}, "Jane")
```

### NotElementsMatch

```go
func NotElementsMatch(t TestingT, listA, listB interface{}, msgAndArgs ...interface{}) (ok bool)
```

NotElementsMatch asserts that the specified listA (array, slice...) is not equal to listB (array, slice...) when ignoring order.

```go
assert.NotElementsMatch(t, [1, 3, 2, 3], [1, 2, 3])
```

### NotEmpty

```go
func NotEmpty(t TestingT, object interface{}, msgAndArgs ...interface{}) bool
```

NotEmpty asserts that the given object is not "empty".

```go
assert.NotEmpty(t, obj)
```

### NotEqual

```go
func NotEqual(t TestingT, expected, actual interface{}, msgAndArgs ...interface{}) bool
```

NotEqual asserts that two objects are not equal.

```go
assert.NotEqual(t, obj1, obj2)
```

### NotEqualValues

```go
func NotEqualValues(t TestingT, expected, actual interface{}, msgAndArgs ...interface{}) bool
```

NotEqualValues asserts that two objects are not equal when converted to comparable types.

### NotErrorAs

```go
func NotErrorAs(t TestingT, err error, target interface{}, msgAndArgs ...interface{}) bool
```

NotErrorAs asserts that an error does not match the target type. This is a wrapper checking that errors.As would fail.

### NotErrorIs

```go
func NotErrorIs(t TestingT, err, target error, msgAndArgs ...interface{}) bool
```

NotErrorIs asserts that an error does not match the target error. This is a wrapper checking that errors.Is would fail.

### NotImplements

```go
func NotImplements(t TestingT, interfaceObject interface{}, object interface{}, msgAndArgs ...interface{}) bool
```

NotImplements asserts that the object does not implement the interface.

```go
assert.NotImplements(t, (*Reader)(nil), new(MyType))
```

### NotNil

```go
func NotNil(t TestingT, object interface{}, msgAndArgs ...interface{}) bool
```

NotNil asserts that the specified object is not nil.

```go
assert.NotNil(t, obj)
```

### NotPanics

```go
func NotPanics(t TestingT, f PanicTestFunc, msgAndArgs ...interface{}) bool
```

NotPanics asserts that the code in the function does not panic.

```go
assert.NotPanics(t, func() {
    someFunctionThatShouldNotPanic()
})
```

### NotRegexp

```go
func NotRegexp(t TestingT, rx interface{}, str interface{}, msgAndArgs ...interface{}) bool
```

NotRegexp asserts that a regexp does not match a string.

```go
assert.NotRegexp(t, regexp.MustCompile("starts"), "it does not start")
assert.NotRegexp(t, "^start", "it does not start")
```

### NotSame

```go
func NotSame(t TestingT, expected, actual interface{}, msgAndArgs ...interface{}) bool
```

NotSame asserts that two pointers do not reference the same object.

### NotSubset

```go
func NotSubset(t TestingT, list, subset interface{}, msgAndArgs ...interface{}) (ok bool)
```

NotSubset asserts that the first list does not contain all elements of the second list.

```go
assert.NotSubset(t, [1, 3, 4], [1, 2])
```

### NotZero

```go
func NotZero(t TestingT, i interface{}, msgAndArgs ...interface{}) bool
```

NotZero asserts that the specified element is not the zero value for its type.

```go
assert.NotZero(t, 1)
assert.NotZero(t, "hello")
```

### ObjectsAreEqual

```go
func ObjectsAreEqual(expected, actual interface{}) bool
```

ObjectsAreEqual compares two objects for equality. Returns true if they are equal.

### ObjectsAreEqualValues

```go
func ObjectsAreEqualValues(expected, actual interface{}) bool
```

ObjectsAreEqualValues compares two objects for equality, converting to the larger type if necessary.

### ObjectsExportedFieldsAreEqual

```go
func ObjectsExportedFieldsAreEqual(expected, actual interface{}) bool
```

**Deprecated** - Compares only the exported fields of two objects for equality.

### Panics

```go
func Panics(t TestingT, f PanicTestFunc, msgAndArgs ...interface{}) bool
```

Panics asserts that the code inside the function panics.

```go
assert.Panics(t, func() {
    panic("oops")
})
```

### PanicsWithError

```go
func PanicsWithError(t TestingT, errString string, f PanicTestFunc, msgAndArgs ...interface{}) bool
```

PanicsWithError asserts that the code panics with a specific error message.

### PanicsWithValue

```go
func PanicsWithValue(t TestingT, expected interface{}, f PanicTestFunc, msgAndArgs ...interface{}) bool
```

PanicsWithValue asserts that the code panics with a specific value.

### Positive

```go
func Positive(t TestingT, e interface{}, msgAndArgs ...interface{}) bool
```

Positive asserts that the given value is positive (greater than zero).

### Regexp

```go
func Regexp(t TestingT, rx interface{}, str interface{}, msgAndArgs ...interface{}) bool
```

Regexp asserts that a string matches a given regular expression.

```go
assert.Regexp(t, regexp.MustCompile("start"), "it's a start")
assert.Regexp(t, "start...$", "it's a start")
```

### Same

```go
func Same(t TestingT, expected, actual interface{}, msgAndArgs ...interface{}) bool
```

Same asserts that two pointers reference the same object (same memory address).

```go
assert.Same(t, ptr1, ptr2)
```

### Subset

```go
func Subset(t TestingT, list, subset interface{}, msgAndArgs ...interface{}) (ok bool)
```

Subset asserts that all elements of subset are contained in list.

```go
assert.Subset(t, [1, 3, 2], [1, 2])
```

### True

```go
func True(t TestingT, value bool, msgAndArgs ...interface{}) bool
```

True asserts that the given boolean value is true.

```go
assert.True(t, myBool)
```

### WithinDuration

```go
func WithinDuration(t TestingT, expected, actual time.Time, delta time.Duration, msgAndArgs ...interface{}) bool
```

WithinDuration asserts that two time values are within the specified duration of each other.

```go
assert.WithinDuration(t, time.Now(), time.Now().Add(100*time.Millisecond), 200*time.Millisecond)
```

### WithinRange

```go
func WithinRange(t TestingT, actual, start, end time.Time, msgAndArgs ...interface{}) bool
```

WithinRange asserts that a time value is within the range [start, end].

### YAMLEq

```go
func YAMLEq(t TestingT, expected string, actual string, msgAndArgs ...interface{}) bool
```

YAMLEq asserts that two YAML strings are equivalent.

### Zero

```go
func Zero(t TestingT, i interface{}, msgAndArgs ...interface{}) bool
```

Zero asserts that the given value is the zero value for its type.

```go
assert.Zero(t, 0)
assert.Zero(t, "")
```

---

## Types

### Assertions

```go
type Assertions struct {
    t TestingT
}
```

Assertions provides assertion methods that can be chained. Create with `assert.New(t)`.

```go
assert := assert.New(t)
assert.Equal(123, 123)
assert.NotNil(obj)
```

### BoolAssertionFunc

```go
type BoolAssertionFunc func(TestingT, bool, ...interface{}) bool
```

A function type for assertions that take a boolean value.

### CollectT

```go
type CollectT struct {
    // contains unexported fields
}
```

CollectT collects assertion errors and can be used with `EventuallyWithT`.

**Methods:**

- `Errorf(format string, args ...interface{})`
- `FailNow()`
- `Helper()`
- `Copy(TestingT)` - **Deprecated**
- `Reset()` - **Deprecated**

### CompareType

```go
type CompareType int
```

**Deprecated** - Type for comparison operations.

### Comparison

```go
type Comparison func() bool
```

A function type that returns a boolean for custom condition assertions.

```go
assert.Condition(t, func() bool {
    return myValue > 0
})
```

### ComparisonAssertionFunc

```go
type ComparisonAssertionFunc func(TestingT, Comparison, ...interface{}) bool
```

A function type for assertions that take a Comparison.

### ErrorAssertionFunc

```go
type ErrorAssertionFunc func(TestingT, error, ...interface{}) bool
```

A function type for assertions that take an error value.

### PanicAssertionFunc

```go
type PanicAssertionFunc func(TestingT, PanicTestFunc, ...interface{}) bool
```

A function type for assertions that check for panics.

### PanicTestFunc

```go
type PanicTestFunc func()
```

A function type for code that is expected to panic.

### TestingT

```go
type TestingT interface {
    Errorf(format string, args ...interface{})
    FailNow()
    Helper()
}
```

Interface that any test object must implement to work with assert functions.

### ValueAssertionFunc

```go
type ValueAssertionFunc func(TestingT, interface{}, ...interface{}) bool
```

A function type for assertions that take a generic value.

---

## Notes

- Every assert function also has an `f` variant (e.g., `Equalf`, `Containsf`) that accepts a format string and args for the failure message.
- All functions return a `bool` indicating whether the assertion passed.
- The `Assertions` struct provides method versions of all package-level functions, so you can write `assert.Equal(a, b)` instead of `assert.Equal(t, a, b)`.

## Source Files

- `assertion_compare.go`
- `assertion_compare_can_convert.go`
- `assertion_format.go`
- `assertion_forward.go`
- `assertion_order.go`
- `assertions.go`
- `doc.go`
- `errors.go`
- `forward_assertions.go`
- `http_assertions.go`
