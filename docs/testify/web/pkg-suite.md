# suite Package Documentation

**Source:** [pkg.go.dev/github.com/stretchr/testify/suite](https://pkg.go.dev/github.com/stretchr/testify/suite)

- **Version:** v1.11.1
- **License:** MIT

## Overview

Package suite contains logic for creating testing suite structs and running the methods on those structs as tests. The most useful piece of this package is that you can create setup/teardown methods on your testing suites, which will run before/after the whole suite or individual tests (depending on which interface(s) you implement).

**Note:** The suite package does not support parallel tests. See [issue 934](https://github.com/stretchr/testify/issues/934).

A testing suite is usually built by first extending the built-in suite functionality from `suite.Suite` in testify. Alternatively, you could reproduce that logic on your own if you wanted (you just need to implement the `TestingSuite` interface from suite/interfaces.go).

After that, you can implement any of the interfaces in suite/interfaces.go to add setup/teardown functionality to your suite, and add any methods that start with "Test" to add tests. Methods that do not match any suite interfaces and do not begin with "Test" will not be run by testify, and can safely be used as helper methods.

Once you've built your testing suite, you need to run the suite (using `suite.Run` from testify) inside any function that matches the identity that "go test" is already looking for (i.e. `func(*testing.T)`).

## Example Usage

```go
// Basic imports
import (
    "testing"
    "github.com/stretchr/testify/assert"
    "github.com/stretchr/testify/suite"
)

// Define the suite, and absorb the built-in basic suite
// functionality from testify - including a T() method which
// returns the current testing context
type ExampleTestSuite struct {
    suite.Suite
    VariableThatShouldStartAtFive int
}

// Make sure that VariableThatShouldStartAtFive is set to five
// before each test
func (suite *ExampleTestSuite) SetupTest() {
    suite.VariableThatShouldStartAtFive = 5
}

// All methods that begin with "Test" are run as tests within a
// suite.
func (suite *ExampleTestSuite) TestExample() {
    assert.Equal(suite.T(), 5, suite.VariableThatShouldStartAtFive)
    suite.Equal(5, suite.VariableThatShouldStartAtFive)
}

// In order for 'go test' to run this suite, we need to create
// a normal test function and pass our suite to suite.Run
func TestExampleTestSuite(t *testing.T) {
    suite.Run(t, new(ExampleTestSuite))
}
```

## Functions

### Run

```go
func Run(t *testing.T, suite TestingSuite)
```

Run takes a testing suite and runs all of the tests attached to it.

## Types

### AfterTest

```go
type AfterTest interface {
	AfterTest(suiteName, testName string)
}
```

AfterTest has a function to be executed right after the test finishes and receives the suite and test names as input.

### BeforeTest

```go
type BeforeTest interface {
	BeforeTest(suiteName, testName string)
}
```

BeforeTest has a function to be executed right before the test starts and receives the suite and test names as input.

### SetupAllSuite

```go
type SetupAllSuite interface {
	SetupSuite()
}
```

SetupAllSuite has a SetupSuite method, which will run before the tests in the suite are run.

### SetupSubTest

```go
type SetupSubTest interface {
	SetupSubTest()
}
```

SetupSubTest has a SetupSubTest method, which will run before each subtest in the suite.

### SetupTestSuite

```go
type SetupTestSuite interface {
	SetupTest()
}
```

SetupTestSuite has a SetupTest method, which will run before each test in the suite.

### Suite

```go
type Suite struct {
	*assert.Assertions
	// contains filtered or unexported fields
}
```

Suite is a basic testing suite with methods for storing and retrieving the current `*testing.T` context.

#### (*Suite) Assert

```go
func (suite *Suite) Assert() *assert.Assertions
```

Assert returns an assert context for suite. Normally, you can call `suite.NoError(expected, actual)`, but for situations where the embedded methods are overridden (for example, you might want to override assert.Assertions with require.Assertions), this method is provided so you can call `suite.Assert().NoError()`.

#### (*Suite) Require

```go
func (suite *Suite) Require() *require.Assertions
```

Require returns a require context for suite.

#### (*Suite) Run

```go
func (suite *Suite) Run(name string, subtest func()) bool
```

Run provides suite functionality around golang subtests. It should be called in place of `t.Run(name, func(t *testing.T))` in test suite code. The passed-in func will be executed as a subtest with a fresh instance of t. Provides compatibility with `go test pkg -run TestSuite/TestName/SubTestName`.

#### (*Suite) SetS

```go
func (suite *Suite) SetS(s TestingSuite)
```

SetS needs to set the current test suite as parent to get access to the parent methods.

#### (*Suite) SetT

```go
func (suite *Suite) SetT(t *testing.T)
```

SetT sets the current `*testing.T` context.

#### (*Suite) T

```go
func (suite *Suite) T() *testing.T
```

T retrieves the current `*testing.T` context.

### SuiteInformation

```go
type SuiteInformation struct {
	Start, End time.Time
	TestStats  map[string]*TestInformation
}
```

SuiteInformation stats stores stats for the whole suite execution.

#### (*SuiteInformation) Passed

```go
func (s *SuiteInformation) Passed() bool
```

### TearDownAllSuite

```go
type TearDownAllSuite interface {
	TearDownSuite()
}
```

TearDownAllSuite has a TearDownSuite method, which will run after all the tests in the suite have been run.

### TearDownSubTest

```go
type TearDownSubTest interface {
	TearDownSubTest()
}
```

TearDownSubTest has a TearDownSubTest method, which will run after each subtest in the suite have been run.

### TearDownTestSuite

```go
type TearDownTestSuite interface {
	TearDownTest()
}
```

TearDownTestSuite has a TearDownTest method, which will run after each test in the suite.

### TestInformation

```go
type TestInformation struct {
	TestName   string
	Start, End time.Time
	Passed     bool
}
```

TestInformation stores information about the execution of each test.

### TestingSuite

```go
type TestingSuite interface {
	T() *testing.T
	SetT(*testing.T)
	SetS(suite TestingSuite)
}
```

TestingSuite can store and return the current `*testing.T` context generated by 'go test'.

### WithStats

```go
type WithStats interface {
	HandleStats(suiteName string, stats *SuiteInformation)
}
```

WithStats implements HandleStats, a function that will be executed when a test suite is finished. The stats contain information about the execution of that suite and its tests.

## Suite Lifecycle Interfaces Summary

| Interface | Method | When it runs |
|-----------|--------|--------------|
| `SetupAllSuite` | `SetupSuite()` | Once, before all tests |
| `TearDownAllSuite` | `TearDownSuite()` | Once, after all tests |
| `SetupTestSuite` | `SetupTest()` | Before each test |
| `TearDownTestSuite` | `TearDownTest()` | After each test |
| `SetupSubTest` | `SetupSubTest()` | Before each subtest |
| `TearDownSubTest` | `TearDownSubTest()` | After each subtest |
| `BeforeTest` | `BeforeTest(suite, test)` | Before each test (with names) |
| `AfterTest` | `AfterTest(suite, test)` | After each test (with names) |
| `WithStats` | `HandleStats(suite, stats)` | After suite completes |

## Source Files

- [doc.go](https://github.com/stretchr/testify/blob/v1.11.1/suite/doc.go)
- [interfaces.go](https://github.com/stretchr/testify/blob/v1.11.1/suite/interfaces.go)
- [stats.go](https://github.com/stretchr/testify/blob/v1.11.1/suite/stats.go)
- [suite.go](https://github.com/stretchr/testify/blob/v1.11.1/suite/suite.go)
