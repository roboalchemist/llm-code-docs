# testify - Package Overview

**Source:** [pkg.go.dev/github.com/stretchr/testify](https://pkg.go.dev/github.com/stretchr/testify)

- **Module**: `github.com/stretchr/testify`
- **Version**: v1.11.1
- **Published**: Aug 27, 2025
- **License**: MIT
- **Repository**: https://github.com/stretchr/testify

## Overview

Module testify is a set of packages that provide many tools for testifying that your code will behave as you intend.

Testify contains the following packages:

- **assert**: Comprehensive set of assertion functions that tie in to the Go testing system
- **require**: Same assertions as assert but stops test execution when a test fails
- **mock**: System for mocking objects and verifying calls are happening as expected
- **suite**: Basic structure for using structs as testing suites with setup/teardown functionality

## Key Features

- Easy assertions
- Mocking
- Testing suite interfaces and functions

## Sub-packages

### [assert](https://pkg.go.dev/github.com/stretchr/testify@v1.11.1/assert)

Package assert provides a set of comprehensive testing tools for use with the normal Go testing system.

**Example Usage:**

```go
package yours

import (
	"testing"
	"github.com/stretchr/testify/assert"
)

func TestSomething(t *testing.T) {
	// assert equality
	assert.Equal(t, 123, 123, "they should be equal")

	// assert inequality
	assert.NotEqual(t, 123, 456, "they should not be equal")

	// assert for nil (good for errors)
	assert.Nil(t, object)

	// assert for not nil (good when you expect something)
	if assert.NotNil(t, object) {
		// now we know that object isn't nil, we are safe to make
		// further assertions without causing any errors
		assert.Equal(t, "Something", object.Value)
	}
}
```

**Using assert.New():**

```go
package yours

import (
	"testing"
	"github.com/stretchr/testify/assert"
)

func TestSomething(t *testing.T) {
	assert := assert.New(t)

	// assert equality
	assert.Equal(123, 123, "they should be equal")

	// assert inequality
	assert.NotEqual(123, 456, "they should not be equal")

	// assert for nil (good for errors)
	assert.Nil(object)

	// assert for not nil (good when you expect something)
	if assert.NotNil(object) {
		assert.Equal("Something", object.Value)
	}
}
```

### [require](https://pkg.go.dev/github.com/stretchr/testify@v1.11.1/require)

Package require implements the same assertions as the `assert` package but stops test execution when a test fails. These functions must be called from the goroutine running the test or benchmark function, not from other goroutines created during the test. Otherwise race conditions may occur.

See [t.FailNow](https://pkg.go.dev/testing#T.FailNow) for details.

### [mock](https://pkg.go.dev/github.com/stretchr/testify@v1.11.1/mock)

Package mock provides a system by which it is possible to mock your objects and verify calls are happening as expected.

**Example Usage:**

```go
package yours

import (
	"testing"
	"github.com/stretchr/testify/mock"
)

// MyMockedObject is a mocked object that implements an interface
// that describes an object that the code I am testing relies on.
type MyMockedObject struct {
	mock.Mock
}

// DoSomething is a method on MyMockedObject that implements some interface
// and just records the activity, and returns what the Mock object tells it to.
func (m *MyMockedObject) DoSomething(number int) (bool, error) {
	args := m.Called(number)
	return args.Bool(0), args.Error(1)
}

func TestSomething(t *testing.T) {
	testObj := new(MyMockedObject)
	testObj.On("DoSomething", 123).Return(true, nil)
	targetFuncThatDoesSomethingWithObj(testObj)
	testObj.AssertExpectations(t)
}

func TestSomethingWithPlaceholder(t *testing.T) {
	testObj := new(MyMockedObject)
	testObj.On("DoSomething", mock.Anything).Return(true, nil)
	targetFuncThatDoesSomethingWithObj(testObj)
	testObj.AssertExpectations(t)
}

func TestSomethingElse2(t *testing.T) {
	testObj := new(MyMockedObject)
	mockCall := testObj.On("DoSomething", mock.Anything).Return(true, nil)
	targetFuncThatDoesSomethingWithObj(testObj)
	testObj.AssertExpectations(t)
	mockCall.Unset()
	testObj.On("DoSomething", mock.Anything).Return(false, nil)
	testObj.AssertExpectations(t)
}
```

You can use the [mockery tool](https://vektra.github.io/mockery/latest/) to autogenerate the mock code against an interface as well, making using mocks much quicker.

### [suite](https://pkg.go.dev/github.com/stretchr/testify@v1.11.1/suite)

Package suite contains logic for creating testing suite structs and running the methods on those structs as tests.

> **WARNING**: The suite package does not support parallel tests. See [#934](https://github.com/stretchr/testify/issues/934).

**Example Usage:**

```go
import (
	"testing"
	"github.com/stretchr/testify/assert"
	"github.com/stretchr/testify/suite"
)

type ExampleTestSuite struct {
	suite.Suite
	VariableThatShouldStartAtFive int
}

func (suite *ExampleTestSuite) SetupTest() {
	suite.VariableThatShouldStartAtFive = 5
}

func (suite *ExampleTestSuite) TestExample() {
	assert.Equal(suite.T(), 5, suite.VariableThatShouldStartAtFive)
}

func TestExampleTestSuite(t *testing.T) {
	suite.Run(t, new(ExampleTestSuite))
}
```

**Suite with Built-in Assertion Methods:**

```go
import (
	"testing"
	"github.com/stretchr/testify/suite"
)

type ExampleTestSuite struct {
	suite.Suite
	VariableThatShouldStartAtFive int
}

func (suite *ExampleTestSuite) SetupTest() {
	suite.VariableThatShouldStartAtFive = 5
}

func (suite *ExampleTestSuite) TestExample() {
	suite.Equal(suite.VariableThatShouldStartAtFive, 5)
}

func TestExampleTestSuite(t *testing.T) {
	suite.Run(t, new(ExampleTestSuite))
}
```

### Additional Directories

- [_codegen](https://pkg.go.dev/github.com/stretchr/testify/_codegen): Code generation module
- [assert/internal/unsafetests](https://pkg.go.dev/github.com/stretchr/testify@v1.11.1/assert/internal/unsafetests): Isolated tests that reference the unsafe package
- [assert/yaml](https://pkg.go.dev/github.com/stretchr/testify@v1.11.1/assert/yaml): YAML deserialization indirection
- [http](https://pkg.go.dev/github.com/stretchr/testify@v1.11.1/http): **Deprecated** - Use net/http/httptest instead

## Installation

To install Testify, use `go get`:

```bash
go get github.com/stretchr/testify
```

This makes the following packages available:

- `github.com/stretchr/testify/assert`
- `github.com/stretchr/testify/require`
- `github.com/stretchr/testify/mock`
- `github.com/stretchr/testify/suite`
- `github.com/stretchr/testify/http` (deprecated)

**Import Example:**

```go
package yours

import (
	"testing"
	"github.com/stretchr/testify/assert"
)

func TestSomething(t *testing.T) {
	assert.True(t, true, "True is true!")
}
```

## Staying Up to Date

To update Testify to the latest version:

```bash
go get -u github.com/stretchr/testify
```

## Supported Go Versions

Currently supports the most recent major Go versions from 1.19 onward.

## Contributing

- Submit issues and pull requests on GitHub
- Include complete test functions demonstrating issues
- Code generation is used - Run `go generate ./...` to update generated files
- Chat on the [Gophers Slack](https://gophers.slack.com) group in `#testify` and `#testify-dev` channels

## Additional Resources

- [Introduction to testing in Go](https://go.dev/doc/code#Testing)
- [API Documentation](https://pkg.go.dev/github.com/stretchr/testify)
- [testifylint](https://github.com/Antonboom/testifylint) - golangci-lint compatible linter for testify
- [Test-Driven Development (TDD)](https://en.wikipedia.org/wiki/Test-driven_development)
- [mockery tool](https://vektra.github.io/mockery/latest/) - Auto-generate mock code

## Package Status

Testify is being maintained at v1; no breaking changes will be accepted in this repo. [See discussion about v2](https://github.com/stretchr/testify/discussions/1560).
