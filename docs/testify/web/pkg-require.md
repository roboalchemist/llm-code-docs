# require Package Documentation

**Source:** [pkg.go.dev/github.com/stretchr/testify/require](https://pkg.go.dev/github.com/stretchr/testify/require)

- **Version:** v1.11.1
- **License:** MIT

## Overview

Package `require` implements the same assertions as the `assert` package but **stops test execution when a test fails** by calling `t.FailNow()`. This is the key difference from `assert`, which continues test execution after a failure.

> The `require` package have same global functions as in the `assert` package, but instead of returning a boolean result they call `t.FailNow()`. A consequence of this is that it must be called from the goroutine running the test function, not from other goroutines created during the test. Otherwise race conditions may occur.

See [t.FailNow](https://pkg.go.dev/testing#T.FailNow) for details.

## Key Differences: require vs assert

| Feature | require | assert |
|---------|---------|--------|
| **On Failure** | Calls `t.FailNow()` - stops test immediately | Returns `false` - continues test |
| **Use Case** | When failure should prevent further assertions | When you want to collect all failures |
| **Goroutine Safe** | Must be called from test goroutine | More flexible |

## Example Usage

```go
import (
  "testing"
  "github.com/stretchr/testify/require"
)

func TestSomething(t *testing.T) {
  var a string = "Hello"
  var b string = "Hello"

  // Test stops here if this fails
  require.Equal(t, a, b, "The two words should be the same.")

  // This line never executes if Equal fails
  require.NotEmpty(t, a)
}
```

## Exported Functions

The require package mirrors every function in the assert package. Each function has the same signature as its assert counterpart, except that instead of returning a bool, it calls `t.FailNow()` on failure.

### Equality and Comparison

- `Equal(t TestingT, expected, actual interface{}, msgAndArgs ...interface{})`
- `Equalf(t TestingT, expected, actual interface{}, msg string, args ...interface{})`
- `EqualValues(t TestingT, expected, actual interface{}, msgAndArgs ...interface{})`
- `EqualValuesf(t TestingT, expected, actual interface{}, msg string, args ...interface{})`
- `EqualError(t TestingT, theError error, errString string, msgAndArgs ...interface{})`
- `EqualErrorf(t TestingT, theError error, errString string, msg string, args ...interface{})`
- `EqualExportedValues(t TestingT, expected, actual interface{}, msgAndArgs ...interface{})`
- `EqualExportedValuesf(t TestingT, expected, actual interface{}, msg string, args ...interface{})`
- `NotEqual(t TestingT, expected, actual interface{}, msgAndArgs ...interface{})`
- `NotEqualf(t TestingT, expected, actual interface{}, msg string, args ...interface{})`
- `NotEqualValues(t TestingT, expected, actual interface{}, msgAndArgs ...interface{})`
- `NotEqualValuesf(t TestingT, expected, actual interface{}, msg string, args ...interface{})`
- `Exactly(t TestingT, expected, actual interface{}, msgAndArgs ...interface{})`
- `Exactlyf(t TestingT, expected, actual interface{}, msg string, args ...interface{})`
- `Greater(t TestingT, e1, e2 interface{}, msgAndArgs ...interface{})`
- `Greaterf(t TestingT, e1, e2 interface{}, msg string, args ...interface{})`
- `GreaterOrEqual(t TestingT, e1, e2 interface{}, msgAndArgs ...interface{})`
- `GreaterOrEqualf(t TestingT, e1, e2 interface{}, msg string, args ...interface{})`
- `Less(t TestingT, e1, e2 interface{}, msgAndArgs ...interface{})`
- `Lessf(t TestingT, e1, e2 interface{}, msg string, args ...interface{})`
- `LessOrEqual(t TestingT, e1, e2 interface{}, msgAndArgs ...interface{})`
- `LessOrEqualf(t TestingT, e1, e2 interface{}, msg string, args ...interface{})`

### Nil, Empty, and Zero

- `Nil(t TestingT, object interface{}, msgAndArgs ...interface{})`
- `Nilf(t TestingT, object interface{}, msg string, args ...interface{})`
- `NotNil(t TestingT, object interface{}, msgAndArgs ...interface{})`
- `NotNilf(t TestingT, object interface{}, msg string, args ...interface{})`
- `Empty(t TestingT, object interface{}, msgAndArgs ...interface{})`
- `Emptyf(t TestingT, object interface{}, msg string, args ...interface{})`
- `NotEmpty(t TestingT, object interface{}, msgAndArgs ...interface{})`
- `NotEmptyf(t TestingT, object interface{}, msg string, args ...interface{})`
- `Zero(t TestingT, i interface{}, msgAndArgs ...interface{})`
- `Zerof(t TestingT, i interface{}, msg string, args ...interface{})`
- `NotZero(t TestingT, i interface{}, msgAndArgs ...interface{})`
- `NotZerof(t TestingT, i interface{}, msg string, args ...interface{})`

### Collections

- `Contains(t TestingT, s, contains interface{}, msgAndArgs ...interface{})`
- `Containsf(t TestingT, s, contains interface{}, msg string, args ...interface{})`
- `NotContains(t TestingT, s, contains interface{}, msgAndArgs ...interface{})`
- `NotContainsf(t TestingT, s, contains interface{}, msg string, args ...interface{})`
- `ElementsMatch(t TestingT, listA, listB interface{}, msgAndArgs ...interface{})`
- `ElementsMatchf(t TestingT, listA, listB interface{}, msg string, args ...interface{})`
- `NotElementsMatch(t TestingT, listA, listB interface{}, msgAndArgs ...interface{})`
- `NotElementsMatchf(t TestingT, listA, listB interface{}, msg string, args ...interface{})`
- `Len(t TestingT, object interface{}, length int, msgAndArgs ...interface{})`
- `Lenf(t TestingT, object interface{}, length int, msg string, args ...interface{})`
- `Subset(t TestingT, list, subset interface{}, msgAndArgs ...interface{})`
- `Subsetf(t TestingT, list, subset interface{}, msg string, args ...interface{})`
- `NotSubset(t TestingT, list, subset interface{}, msgAndArgs ...interface{})`
- `NotSubsetf(t TestingT, list, subset interface{}, msg string, args ...interface{})`

### Error Handling

- `Error(t TestingT, err error, msgAndArgs ...interface{})`
- `Errorf(t TestingT, err error, msg string, args ...interface{})`
- `NoError(t TestingT, err error, msgAndArgs ...interface{})`
- `NoErrorf(t TestingT, err error, msg string, args ...interface{})`
- `ErrorAs(t TestingT, err error, target interface{}, msgAndArgs ...interface{})`
- `ErrorAsf(t TestingT, err error, target interface{}, msg string, args ...interface{})`
- `NotErrorAs(t TestingT, err error, target interface{}, msgAndArgs ...interface{})`
- `NotErrorAsf(t TestingT, err error, target interface{}, msg string, args ...interface{})`
- `ErrorIs(t TestingT, err, target error, msgAndArgs ...interface{})`
- `ErrorIsf(t TestingT, err, target error, msg string, args ...interface{})`
- `NotErrorIs(t TestingT, err, target error, msgAndArgs ...interface{})`
- `NotErrorIsf(t TestingT, err, target error, msg string, args ...interface{})`
- `ErrorContains(t TestingT, theError error, contains string, msgAndArgs ...interface{})`
- `ErrorContainsf(t TestingT, theError error, contains string, msg string, args ...interface{})`

### Type and Value Assertions

- `IsType(t TestingT, expectedType, object interface{}, msgAndArgs ...interface{})`
- `IsTypef(t TestingT, expectedType, object interface{}, msg string, args ...interface{})`
- `IsNotType(t TestingT, expectedType, object interface{}, msgAndArgs ...interface{})`
- `IsNotTypef(t TestingT, expectedType, object interface{}, msg string, args ...interface{})`
- `Implements(t TestingT, interfaceObject, object interface{}, msgAndArgs ...interface{})`
- `Implementsf(t TestingT, interfaceObject, object interface{}, msg string, args ...interface{})`
- `NotImplements(t TestingT, interfaceObject, object interface{}, msgAndArgs ...interface{})`
- `NotImplementsf(t TestingT, interfaceObject, object interface{}, msg string, args ...interface{})`

### Boolean

- `True(t TestingT, value bool, msgAndArgs ...interface{})`
- `Truef(t TestingT, value bool, msg string, args ...interface{})`
- `False(t TestingT, value bool, msgAndArgs ...interface{})`
- `Falsef(t TestingT, value bool, msg string, args ...interface{})`

### Async and Timing

- `Eventually(t TestingT, condition func() bool, waitFor time.Duration, tick time.Duration, msgAndArgs ...interface{})`
- `Eventuallyf(t TestingT, condition func() bool, waitFor time.Duration, tick time.Duration, msg string, args ...interface{})`
- `EventuallyWithT(t TestingT, condition func(collect *assert.CollectT), waitFor time.Duration, tick time.Duration, msgAndArgs ...interface{})`
- `EventuallyWithTf(t TestingT, condition func(collect *assert.CollectT), waitFor time.Duration, tick time.Duration, msg string, args ...interface{})`
- `Never(t TestingT, condition func() bool, waitFor time.Duration, tick time.Duration, msgAndArgs ...interface{})`
- `Neverf(t TestingT, condition func() bool, waitFor time.Duration, tick time.Duration, msg string, args ...interface{})`
- `WithinDuration(t TestingT, expected, actual time.Time, delta time.Duration, msgAndArgs ...interface{})`
- `WithinDurationf(t TestingT, expected, actual time.Time, delta time.Duration, msg string, args ...interface{})`
- `WithinRange(t TestingT, actual, start, end time.Time, msgAndArgs ...interface{})`
- `WithinRangef(t TestingT, actual, start, end time.Time, msg string, args ...interface{})`

### File System

- `FileExists(t TestingT, path string, msgAndArgs ...interface{})`
- `FileExistsf(t TestingT, path string, msg string, args ...interface{})`
- `NoFileExists(t TestingT, path string, msgAndArgs ...interface{})`
- `NoFileExistsf(t TestingT, path string, msg string, args ...interface{})`
- `DirExists(t TestingT, path string, msgAndArgs ...interface{})`
- `DirExistsf(t TestingT, path string, msg string, args ...interface{})`
- `NoDirExists(t TestingT, path string, msgAndArgs ...interface{})`
- `NoDirExistsf(t TestingT, path string, msg string, args ...interface{})`

### Panics

- `Panics(t TestingT, f assert.PanicTestFunc, msgAndArgs ...interface{})`
- `Panicsf(t TestingT, f assert.PanicTestFunc, msg string, args ...interface{})`
- `NotPanics(t TestingT, f assert.PanicTestFunc, msgAndArgs ...interface{})`
- `NotPanicsf(t TestingT, f assert.PanicTestFunc, msg string, args ...interface{})`
- `PanicsWithError(t TestingT, errString string, f assert.PanicTestFunc, msgAndArgs ...interface{})`
- `PanicsWithErrorf(t TestingT, errString string, f assert.PanicTestFunc, msg string, args ...interface{})`
- `PanicsWithValue(t TestingT, expected interface{}, f assert.PanicTestFunc, msgAndArgs ...interface{})`
- `PanicsWithValuef(t TestingT, expected interface{}, f assert.PanicTestFunc, msg string, args ...interface{})`

### String and Regex

- `Regexp(t TestingT, rx, str interface{}, msgAndArgs ...interface{})`
- `Regexpf(t TestingT, rx, str interface{}, msg string, args ...interface{})`
- `NotRegexp(t TestingT, rx, str interface{}, msgAndArgs ...interface{})`
- `NotRegexpf(t TestingT, rx, str interface{}, msg string, args ...interface{})`
- `JSONEq(t TestingT, expected, actual string, msgAndArgs ...interface{})`
- `JSONEqf(t TestingT, expected, actual string, msg string, args ...interface{})`
- `YAMLEq(t TestingT, expected, actual string, msgAndArgs ...interface{})`
- `YAMLEqf(t TestingT, expected, actual string, msg string, args ...interface{})`

### Numeric

- `Positive(t TestingT, e interface{}, msgAndArgs ...interface{})`
- `Positivef(t TestingT, e interface{}, msg string, args ...interface{})`
- `Negative(t TestingT, e interface{}, msgAndArgs ...interface{})`
- `Negativef(t TestingT, e interface{}, msg string, args ...interface{})`
- `InDelta(t TestingT, expected, actual interface{}, delta float64, msgAndArgs ...interface{})`
- `InDeltaf(t TestingT, expected, actual interface{}, delta float64, msg string, args ...interface{})`
- `InDeltaMapValues(t TestingT, expected, actual interface{}, delta float64, msgAndArgs ...interface{})`
- `InDeltaMapValuesf(t TestingT, expected, actual interface{}, delta float64, msg string, args ...interface{})`
- `InDeltaSlice(t TestingT, expected, actual interface{}, delta float64, msgAndArgs ...interface{})`
- `InDeltaSlicef(t TestingT, expected, actual interface{}, delta float64, msg string, args ...interface{})`
- `InEpsilon(t TestingT, expected, actual interface{}, epsilon float64, msgAndArgs ...interface{})`
- `InEpsilonf(t TestingT, expected, actual interface{}, epsilon float64, msg string, args ...interface{})`
- `InEpsilonSlice(t TestingT, expected, actual interface{}, epsilon float64, msgAndArgs ...interface{})`
- `InEpsilonSlicef(t TestingT, expected, actual interface{}, epsilon float64, msg string, args ...interface{})`

### Ordering

- `IsDecreasing(t TestingT, object interface{}, msgAndArgs ...interface{})`
- `IsDecreasingf(t TestingT, object interface{}, msg string, args ...interface{})`
- `IsIncreasing(t TestingT, object interface{}, msgAndArgs ...interface{})`
- `IsIncreasingf(t TestingT, object interface{}, msg string, args ...interface{})`
- `IsNonDecreasing(t TestingT, object interface{}, msgAndArgs ...interface{})`
- `IsNonDecreasingf(t TestingT, object interface{}, msg string, args ...interface{})`
- `IsNonIncreasing(t TestingT, object interface{}, msgAndArgs ...interface{})`
- `IsNonIncreasingf(t TestingT, object interface{}, msg string, args ...interface{})`

### Pointer

- `Same(t TestingT, expected, actual interface{}, msgAndArgs ...interface{})`
- `Samef(t TestingT, expected, actual interface{}, msg string, args ...interface{})`
- `NotSame(t TestingT, expected, actual interface{}, msgAndArgs ...interface{})`
- `NotSamef(t TestingT, expected, actual interface{}, msg string, args ...interface{})`

### Other

- `Condition(t TestingT, comp assert.Comparison, msgAndArgs ...interface{})`
- `Conditionf(t TestingT, comp assert.Comparison, msg string, args ...interface{})`
- `Fail(t TestingT, failureMessage string, msgAndArgs ...interface{})`
- `FailNow(t TestingT, failureMessage string, msgAndArgs ...interface{})`
- `HTTPBody(handler http.HandlerFunc, method, url string, values url.Values) string`
- `HTTPBodyContains(t TestingT, handler http.HandlerFunc, method, url string, values url.Values, str string, msgAndArgs ...interface{})`
- `HTTPBodyNotContains(t TestingT, handler http.HandlerFunc, method, url string, values url.Values, str string, msgAndArgs ...interface{})`
- `HTTPError(t TestingT, handler http.HandlerFunc, method, url string, values url.Values, msgAndArgs ...interface{})`
- `HTTPRedirect(t TestingT, handler http.HandlerFunc, method, url string, values url.Values, msgAndArgs ...interface{})`
- `HTTPStatusCode(t TestingT, handler http.HandlerFunc, method, url string, values url.Values, statuscode int, msgAndArgs ...interface{})`
- `HTTPSuccess(t TestingT, handler http.HandlerFunc, method, url string, values url.Values, msgAndArgs ...interface{})`

## Types

### Assertions

```go
type Assertions struct {
    t TestingT
}
```

Create with `require.New(t)`:

```go
require := require.New(t)
require.Equal(a, b)
require.NoError(err)
```

### TestingT

```go
type TestingT interface {
    Errorf(format string, args ...interface{})
    FailNow()
    Helper()
}
```

### BoolAssertionFunc

```go
type BoolAssertionFunc func(TestingT, bool, ...interface{})
```

### ComparisonAssertionFunc

```go
type ComparisonAssertionFunc func(TestingT, assert.Comparison, ...interface{})
```

### ErrorAssertionFunc

```go
type ErrorAssertionFunc func(TestingT, error, ...interface{})
```

### ValueAssertionFunc

```go
type ValueAssertionFunc func(TestingT, interface{}, ...interface{})
```

## Source Files

- `doc.go`
- `forward_requirements.go`
- `require.go`
- `require_forward.go`
- `requirements.go`
