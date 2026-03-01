# Source: https://pkg.go.dev/go.uber.org/goleak

Title: goleak package - go.uber.org/goleak - Go Packages

URL Source: https://pkg.go.dev/go.uber.org/goleak

Markdown Content:
goleak package - go.uber.org/goleak - Go Packages
===============

[![Image 4: Go](https://pkg.go.dev/static/shared/logo/go-white.svg)](https://go.dev/)

[Skip to Main Content](https://pkg.go.dev/go.uber.org/goleak#main-content)

![Image 5](https://pkg.go.dev/static/shared/icon/search_gm_grey_24dp.svg)![Image 6](https://pkg.go.dev/static/shared/icon/search_gm_grey_24dp.svg)

*   [Why Go ![Image 7: submenu dropdown icon](https://pkg.go.dev/static/shared/icon/arrow_drop_down_gm_grey_24dp.svg)](https://pkg.go.dev/go.uber.org/goleak#)
    *   [Case Studies](https://go.dev/solutions#case-studies) 
Common problems companies solve with Go

    *   [Use Cases](https://go.dev/solutions#use-cases) 
Stories about how and why companies use Go

    *   [Security](https://go.dev/security/) 
How Go can help keep you secure by default

*   [Learn](https://go.dev/learn/)
*   [Docs ![Image 8: submenu dropdown icon](https://pkg.go.dev/static/shared/icon/arrow_drop_down_gm_grey_24dp.svg)](https://pkg.go.dev/go.uber.org/goleak#)
    *   [Effective Go](https://go.dev/doc/effective_go) 
Tips for writing clear, performant, and idiomatic Go code

    *   [Go User Manual](https://go.dev/doc/) 
A complete introduction to building software with Go

    *   [Standard library](https://pkg.go.dev/std) 
Reference documentation for Go's standard library

    *   [Release Notes](https://go.dev/doc/devel/release) 
Learn what's new in each Go release

*   [Packages](https://pkg.go.dev/)
*   [Community ![Image 9: submenu dropdown icon](https://pkg.go.dev/static/shared/icon/arrow_drop_down_gm_grey_24dp.svg)](https://pkg.go.dev/go.uber.org/goleak#)
    *   [Recorded Talks](https://go.dev/talks/) 
Videos from prior events

    *   [Meetups _![Image 10](https://pkg.go.dev/static/shared/icon/launch\_gm\_grey\_24dp.svg)_](https://www.meetup.com/pro/go) 
Meet other local Go developers

    *   [Conferences _![Image 11](https://pkg.go.dev/static/shared/icon/launch\_gm\_grey\_24dp.svg)_](https://github.com/golang/go/wiki/Conferences) 
Learn and network with Go developers from around the world

    *   [Go blog](https://go.dev/blog) 
The Go project's official blog.

    *   [Go project](https://go.dev/help) 
Get help and stay informed from Go

    *    Get connected  [![Image 12](https://pkg.go.dev/static/shared/logo/social/google-groups.svg)](https://groups.google.com/g/golang-nuts "Get connected with google-groups (Opens in new window)")[![Image 13](https://pkg.go.dev/static/shared/logo/social/github.svg)](https://github.com/golang "Get connected with github (Opens in new window)")[![Image 14](https://pkg.go.dev/static/shared/logo/social/twitter.svg)](https://twitter.com/golang "Get connected with twitter (Opens in new window)")[![Image 15](https://pkg.go.dev/static/shared/logo/social/reddit.svg)](https://www.reddit.com/r/golang/ "Get connected with reddit (Opens in new window)")[![Image 16](https://pkg.go.dev/static/shared/logo/social/slack.svg)](https://invite.slack.golangbridge.org/ "Get connected with slack (Opens in new window)")[![Image 17](https://pkg.go.dev/static/shared/logo/social/stack-overflow.svg)](https://stackoverflow.com/collectives/go) 

[![Image 18: Go](https://pkg.go.dev/static/shared/logo/go-blue.svg)](https://go.dev/)

*   [Why Go _![Image 19](https://pkg.go.dev/static/shared/icon/navigate\_next\_gm\_grey\_24dp.svg)_](https://pkg.go.dev/go.uber.org/goleak#)

[_![Image 20](https://pkg.go.dev/static/shared/icon/navigate\_before\_gm\_grey\_24dp.svg)_ Why Go](https://pkg.go.dev/go.uber.org/goleak#) 
    *   [Case Studies](https://go.dev/solutions#case-studies)
    *   [Use Cases](https://go.dev/solutions#use-cases)
    *   [Security](https://go.dev/security/)

*   [Learn](https://go.dev/learn/)
*   [Docs _![Image 21](https://pkg.go.dev/static/shared/icon/navigate\_next\_gm\_grey\_24dp.svg)_](https://pkg.go.dev/go.uber.org/goleak#)

[_![Image 22](https://pkg.go.dev/static/shared/icon/navigate\_before\_gm\_grey\_24dp.svg)_ Docs](https://pkg.go.dev/go.uber.org/goleak#) 
    *   [Effective Go](https://go.dev/doc/effective_go)
    *   [Go User Manual](https://go.dev/doc/)
    *   [Standard library](https://pkg.go.dev/std)
    *   [Release Notes](https://go.dev/doc/devel/release)

*   [Packages](https://pkg.go.dev/)
*   [Community _![Image 23](https://pkg.go.dev/static/shared/icon/navigate\_next\_gm\_grey\_24dp.svg)_](https://pkg.go.dev/go.uber.org/goleak#)

[_![Image 24](https://pkg.go.dev/static/shared/icon/navigate\_before\_gm\_grey\_24dp.svg)_ Community](https://pkg.go.dev/go.uber.org/goleak#) 
    *   [Recorded Talks](https://go.dev/talks/)
    *   [Meetups _![Image 25](https://pkg.go.dev/static/shared/icon/launch\_gm\_grey\_24dp.svg)_](https://www.meetup.com/pro/go)
    *   [Conferences _![Image 26](https://pkg.go.dev/static/shared/icon/launch\_gm\_grey\_24dp.svg)_](https://github.com/golang/go/wiki/Conferences)
    *   [Go blog](https://go.dev/blog)
    *   [Go project](https://go.dev/help)
    *   Get connected [![Image 27](https://pkg.go.dev/static/shared/logo/social/google-groups.svg)](https://groups.google.com/g/golang-nuts)[![Image 28](https://pkg.go.dev/static/shared/logo/social/github.svg)](https://github.com/golang)[![Image 29](https://pkg.go.dev/static/shared/logo/social/twitter.svg)](https://twitter.com/golang)[![Image 30](https://pkg.go.dev/static/shared/logo/social/reddit.svg)](https://www.reddit.com/r/golang/)[![Image 31](https://pkg.go.dev/static/shared/logo/social/slack.svg)](https://invite.slack.golangbridge.org/)[![Image 32](https://pkg.go.dev/static/shared/logo/social/stack-overflow.svg)](https://stackoverflow.com/collectives/go) 

1.   [Discover Packages](https://pkg.go.dev/)
2.   [go.uber.org/goleak](https://pkg.go.dev/go.uber.org/goleak@v1.3.0)![Image 33](https://pkg.go.dev/static/shared/icon/content_copy_gm_grey_24dp.svg)

[![Image 34: Go](https://pkg.go.dev/static/shared/logo/go-blue.svg)](https://go.dev/)
goleak
======

package module![Image 35](https://pkg.go.dev/static/shared/icon/content_copy_gm_grey_24dp.svg)

[Version: v1.3.0](https://pkg.go.dev/go.uber.org/goleak?tab=versions)

 Opens a new window with list of versions in this module. 

Latest Latest 

![Image 36: Warning](https://pkg.go.dev/static/shared/icon/alert_gm_grey_24dp.svg)
This package is not in the latest version of its module.

[Go to latest](https://pkg.go.dev/go.uber.org/goleak) Published: Oct 24, 2023  License: [MIT](https://pkg.go.dev/go.uber.org/goleak?tab=licenses)

 Opens a new window with license information. 

[Imports: 7](https://pkg.go.dev/go.uber.org/goleak?tab=imports)

 Opens a new window with list of imports. 

[Imported by: 101](https://pkg.go.dev/go.uber.org/goleak?tab=importedby)

 Opens a new window with list of known importers. 

Details
-------

*   ![Image 37: checked](https://pkg.go.dev/static/shared/icon/check_circle_gm_grey_24dp.svg) Valid [go.mod](https://github.com/uber-go/goleak/tree/v1.3.0/go.mod) file ![Image 38](https://pkg.go.dev/static/shared/icon/help_gm_grey_24dp.svg)
The Go module system was introduced in Go 1.11 and is the official dependency management solution for Go. 
*   ![Image 39: checked](https://pkg.go.dev/static/shared/icon/check_circle_gm_grey_24dp.svg) Redistributable license ![Image 40](https://pkg.go.dev/static/shared/icon/help_gm_grey_24dp.svg)
Redistributable licenses place minimal restrictions on how software can be used, modified, and redistributed. 
*   ![Image 41: checked](https://pkg.go.dev/static/shared/icon/check_circle_gm_grey_24dp.svg) Tagged version ![Image 42](https://pkg.go.dev/static/shared/icon/help_gm_grey_24dp.svg)
Modules with tagged versions give importers more predictable builds. 
*   ![Image 43: checked](https://pkg.go.dev/static/shared/icon/check_circle_gm_grey_24dp.svg) Stable version ![Image 44](https://pkg.go.dev/static/shared/icon/help_gm_grey_24dp.svg)
When a project reaches major version v1 it is considered stable. 
*   [Learn more about best practices](https://pkg.go.dev/about#best-practices)

Repository
----------

[github.com/uber-go/goleak](https://github.com/uber-go/goleak "https://github.com/uber-go/goleak")

Links
-----

*   [![Image 45: Open Source Insights Logo](https://pkg.go.dev/static/shared/icon/depsdev-logo.svg) Open Source Insights](https://deps.dev/go/go.uber.org%2Fgoleak/v1.3.0 "View this module on Open Source Insights")

 Jump to ... 

*   [README](https://pkg.go.dev/go.uber.org/goleak#section-readme)
    *   [Installation](https://pkg.go.dev/go.uber.org/goleak#readme-installation)
    *   [Quick Start](https://pkg.go.dev/go.uber.org/goleak#readme-quick-start)
    *   [Determine Source of Package Leaks](https://pkg.go.dev/go.uber.org/goleak#readme-determine-source-of-package-leaks)
    *   [Stability](https://pkg.go.dev/go.uber.org/goleak#readme-stability)

*   [Documentation](https://pkg.go.dev/go.uber.org/goleak#section-documentation)
    *   [Overview](https://pkg.go.dev/go.uber.org/goleak#pkg-overview)
    *   [Index](https://pkg.go.dev/go.uber.org/goleak#pkg-index)
    *   [Constants](https://pkg.go.dev/go.uber.org/goleak#pkg-constants)
    *   [Variables](https://pkg.go.dev/go.uber.org/goleak#pkg-variables)
    *   [Functions](https://pkg.go.dev/go.uber.org/goleak#pkg-functions)
        *   [Find(options)](https://pkg.go.dev/go.uber.org/goleak#Find "Find(options)")
        *   [VerifyNone(t, options)](https://pkg.go.dev/go.uber.org/goleak#VerifyNone "VerifyNone(t, options)")
        *   [VerifyTestMain(m, options)](https://pkg.go.dev/go.uber.org/goleak#VerifyTestMain "VerifyTestMain(m, options)")

    *   [Types](https://pkg.go.dev/go.uber.org/goleak#pkg-types)
        *   [type Option](https://pkg.go.dev/go.uber.org/goleak#Option "type Option")
            *   [Cleanup(cleanupFunc)](https://pkg.go.dev/go.uber.org/goleak#Cleanup "Cleanup(cleanupFunc)")
            *   [IgnoreAnyFunction(f)](https://pkg.go.dev/go.uber.org/goleak#IgnoreAnyFunction "IgnoreAnyFunction(f)")
            *   [IgnoreCurrent()](https://pkg.go.dev/go.uber.org/goleak#IgnoreCurrent "IgnoreCurrent()")
            *   [IgnoreTopFunction(f)](https://pkg.go.dev/go.uber.org/goleak#IgnoreTopFunction "IgnoreTopFunction(f)")

        *   [type TestingM](https://pkg.go.dev/go.uber.org/goleak#TestingM "type TestingM")
        *   [type TestingT](https://pkg.go.dev/go.uber.org/goleak#TestingT "type TestingT")

*   [Source Files](https://pkg.go.dev/go.uber.org/goleak#section-sourcefiles)
*   [Directories](https://pkg.go.dev/go.uber.org/goleak#section-directories)

![Image 46](https://pkg.go.dev/static/shared/icon/chrome_reader_mode_gm_grey_24dp.svg) README [¶](https://pkg.go.dev/go.uber.org/goleak#section-readme "Go to Readme")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------

### goleak [![Image 47: GoDoc](https://godoc.org/go.uber.org/goleak?status.svg)](https://godoc.org/go.uber.org/goleak)[![Image 48: Build Status](https://github.com/uber-go/goleak/actions/workflows/ci.yml/badge.svg)](https://github.com/uber-go/goleak/actions/workflows/ci.yml)[![Image 49: Coverage Status](https://codecov.io/gh/uber-go/goleak/branch/master/graph/badge.svg)](https://codecov.io/gh/uber-go/goleak)

Goroutine leak detector to help avoid Goroutine leaks.

#### Installation

You can use `go get` to get the latest version:

`go get -u go.uber.org/goleak`

`goleak` also supports semver releases.

Note that go-leak only [supports](https://go.dev/doc/devel/release#policy) the two most recent minor versions of Go.

#### Quick Start

To verify that there are no unexpected goroutines running at the end of a test:

```
func TestA(t *testing.T) {
	defer goleak.VerifyNone(t)

	// test logic here.
}
```

Instead of checking for leaks at the end of every test, `goleak` can also be run at the end of every test package by creating a `TestMain` function for your package:

```
func TestMain(m *testing.M) {
	goleak.VerifyTestMain(m)
}
```

#### Determine Source of Package Leaks

When verifying leaks using `TestMain`, the leak test is only run once after all tests have been run. This is typically enough to ensure there's no goroutines leaked from tests, but when there are leaks, it's hard to determine which test is causing them.

You can use the following bash script to determine the source of the failing test:

```
# Create a test binary which will be used to run each test individually
$ go test -c -o tests

# Run each test individually, printing "." for successful tests, or the test name
# for failing tests.
$ for test in $(go test -list . | grep -E "^(Test|Example)"); do ./tests -test.run "^$test\$" &>/dev/null && echo -n "." || echo -e "\n$test failed"; done
```

This will only print names of failing tests which can be investigated individually. E.g.,

```
.....
TestLeakyTest failed
.......
```

#### Stability

goleak is v1 and follows [SemVer](http://semver.org/) strictly.

No breaking changes will be made to exported APIs before 2.0.

Expand ▾Collapse ▴

![Image 50](https://pkg.go.dev/static/shared/icon/code_gm_grey_24dp.svg) Documentation [¶](https://pkg.go.dev/go.uber.org/goleak#section-documentation "Go to Documentation")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Overview [¶](https://pkg.go.dev/go.uber.org/goleak#pkg-overview "Go to Overview")

Package goleak is a Goroutine leak detector.

### Index [¶](https://pkg.go.dev/go.uber.org/goleak#pkg-index "Go to Index")

*   [func Find(options ...Option) error](https://pkg.go.dev/go.uber.org/goleak#Find)
*   [func VerifyNone(t TestingT, options ...Option)](https://pkg.go.dev/go.uber.org/goleak#VerifyNone)
*   [func VerifyTestMain(m TestingM, options ...Option)](https://pkg.go.dev/go.uber.org/goleak#VerifyTestMain)
*   [type Option](https://pkg.go.dev/go.uber.org/goleak#Option)
*       *   [func Cleanup(cleanupFunc func(exitCode int)) Option](https://pkg.go.dev/go.uber.org/goleak#Cleanup)
    *   [func IgnoreAnyFunction(f string) Option](https://pkg.go.dev/go.uber.org/goleak#IgnoreAnyFunction)
    *   [func IgnoreCurrent() Option](https://pkg.go.dev/go.uber.org/goleak#IgnoreCurrent)
    *   [func IgnoreTopFunction(f string) Option](https://pkg.go.dev/go.uber.org/goleak#IgnoreTopFunction)

*   [type TestingM](https://pkg.go.dev/go.uber.org/goleak#TestingM)
*   [type TestingT](https://pkg.go.dev/go.uber.org/goleak#TestingT)

### Constants [¶](https://pkg.go.dev/go.uber.org/goleak#pkg-constants "Go to Constants")

This section is empty.

### Variables [¶](https://pkg.go.dev/go.uber.org/goleak#pkg-variables "Go to Variables")

This section is empty.

### Functions [¶](https://pkg.go.dev/go.uber.org/goleak#pkg-functions "Go to Functions")

#### func [Find](https://github.com/uber-go/goleak/blob/v1.3.0/leaks.go#L55)[¶](https://pkg.go.dev/go.uber.org/goleak#Find "Go to Find")

func Find(options ...[Option](https://pkg.go.dev/go.uber.org/goleak#Option)) [error](https://pkg.go.dev/builtin#error)

Find looks for extra goroutines, and returns a descriptive error if any are found.

#### func [VerifyNone](https://github.com/uber-go/goleak/blob/v1.3.0/leaks.go#L91)[¶](https://pkg.go.dev/go.uber.org/goleak#VerifyNone "Go to VerifyNone")

func VerifyNone(t [TestingT](https://pkg.go.dev/go.uber.org/goleak#TestingT), options ...[Option](https://pkg.go.dev/go.uber.org/goleak#Option))

VerifyNone marks the given TestingT as failed if any extra goroutines are found by Find. This is a helper method to make it easier to integrate in tests by doing:

defer VerifyNone(t)

VerifyNone is currently incompatible with t.Parallel because it cannot associate specific goroutines with specific tests. Thus, non-leaking goroutines from other tests running in parallel could fail this check. If you need to run tests in parallel, use [VerifyTestMain](https://pkg.go.dev/go.uber.org/goleak#VerifyTestMain) instead, which will verify that no leaking goroutines exist after ALL tests finish.

#### func [VerifyTestMain](https://github.com/uber-go/goleak/blob/v1.3.0/testmain.go#L52)[¶](https://pkg.go.dev/go.uber.org/goleak#VerifyTestMain "Go to VerifyTestMain")

func VerifyTestMain(m [TestingM](https://pkg.go.dev/go.uber.org/goleak#TestingM), options ...[Option](https://pkg.go.dev/go.uber.org/goleak#Option))

VerifyTestMain can be used in a TestMain function for package tests to verify that there were no goroutine leaks. To use it, your TestMain function should look like:

func TestMain(m *testing.M) {
  goleak.VerifyTestMain(m)
}

See [https://golang.org/pkg/testing/#hdr-Main](https://golang.org/pkg/testing/#hdr-Main) for more details.

This will run all tests as per normal, and if they were successful, look for any goroutine leaks and fail the tests if any leaks were found.

### Types [¶](https://pkg.go.dev/go.uber.org/goleak#pkg-types "Go to Types")

#### type [Option](https://github.com/uber-go/goleak/blob/v1.3.0/options.go#L31)[¶](https://pkg.go.dev/go.uber.org/goleak#Option "Go to Option")

type Option interface {
	// contains filtered or unexported methods
}

Option lets users specify custom verifications.

#### func [Cleanup](https://github.com/uber-go/goleak/blob/v1.3.0/options.go#L92)[¶](https://pkg.go.dev/go.uber.org/goleak#Cleanup "Go to Cleanup")added in v1.2.0

func Cleanup(cleanupFunc func(exitCode [int](https://pkg.go.dev/builtin#int))) [Option](https://pkg.go.dev/go.uber.org/goleak#Option)

Cleanup sets up a cleanup function that will be executed at the end of the leak check. When passed to [VerifyTestMain](https://pkg.go.dev/go.uber.org/goleak#VerifyTestMain), the exit code passed to cleanupFunc will be set to the exit code of TestMain. When passed to [VerifyNone](https://pkg.go.dev/go.uber.org/goleak#VerifyNone), the exit code will be set to 0. This cannot be passed to [Find](https://pkg.go.dev/go.uber.org/goleak#Find).

#### func [IgnoreAnyFunction](https://github.com/uber-go/goleak/blob/v1.3.0/options.go#L80)[¶](https://pkg.go.dev/go.uber.org/goleak#IgnoreAnyFunction "Go to IgnoreAnyFunction")added in v1.3.0

func IgnoreAnyFunction(f [string](https://pkg.go.dev/builtin#string)) [Option](https://pkg.go.dev/go.uber.org/goleak#Option)

IgnoreAnyFunction ignores goroutines where the specified function is present anywhere in the stack.

The function name must be fully qualified, e.g.,

go.uber.org/goleak.IgnoreAnyFunction

For methods, the fully qualified form looks like:

go.uber.org/goleak.(*MyType).MyMethod

#### func [IgnoreCurrent](https://github.com/uber-go/goleak/blob/v1.3.0/options.go#L100)[¶](https://pkg.go.dev/go.uber.org/goleak#IgnoreCurrent "Go to IgnoreCurrent")added in v1.1.0

func IgnoreCurrent() [Option](https://pkg.go.dev/go.uber.org/goleak#Option)

IgnoreCurrent records all current goroutines when the option is created, and ignores them in any future Find/Verify calls.

#### func [IgnoreTopFunction](https://github.com/uber-go/goleak/blob/v1.3.0/options.go#L64)[¶](https://pkg.go.dev/go.uber.org/goleak#IgnoreTopFunction "Go to IgnoreTopFunction")

func IgnoreTopFunction(f [string](https://pkg.go.dev/builtin#string)) [Option](https://pkg.go.dev/go.uber.org/goleak#Option)

IgnoreTopFunction ignores any goroutines where the specified function is at the top of the stack. The function name should be fully qualified, e.g., go.uber.org/goleak.IgnoreTopFunction

#### type [TestingM](https://github.com/uber-go/goleak/blob/v1.3.0/testmain.go#L36)[¶](https://pkg.go.dev/go.uber.org/goleak#TestingM "Go to TestingM")

type TestingM interface {
 Run() [int](https://pkg.go.dev/builtin#int)}

TestingM is the minimal subset of testing.M that we use.

#### type [TestingT](https://github.com/uber-go/goleak/blob/v1.3.0/leaks.go#L31)[¶](https://pkg.go.dev/go.uber.org/goleak#TestingT "Go to TestingT")

type TestingT interface {
 Error(...interface{}) }

TestingT is the minimal subset of testing.TB that we use.

![Image 51](https://pkg.go.dev/static/shared/icon/insert_drive_file_gm_grey_24dp.svg) Source Files [¶](https://pkg.go.dev/go.uber.org/goleak#section-sourcefiles "Go to Source Files")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[View all Source files](https://github.com/uber-go/goleak/tree/v1.3.0)

*   [doc.go](https://github.com/uber-go/goleak/blob/v1.3.0/doc.go "doc.go")
*   [leaks.go](https://github.com/uber-go/goleak/blob/v1.3.0/leaks.go "leaks.go")
*   [options.go](https://github.com/uber-go/goleak/blob/v1.3.0/options.go "options.go")
*   [testmain.go](https://github.com/uber-go/goleak/blob/v1.3.0/testmain.go "testmain.go")
*   [tracestack_new.go](https://github.com/uber-go/goleak/blob/v1.3.0/tracestack_new.go "tracestack_new.go")

![Image 52](https://pkg.go.dev/static/shared/icon/folder_gm_grey_24dp.svg) Directories [¶](https://pkg.go.dev/go.uber.org/goleak#section-directories "Go to Directories")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

 Show internal  Expand all 

| Path | Synopsis |
| --- | --- |
| ![Image 53](https://pkg.go.dev/static/shared/icon/arrow_right_gm_grey_24dp.svg)internal |  |
| [stack](https://pkg.go.dev/go.uber.org/goleak@v1.3.0/internal/stack) Package stack is used for parsing stacks from `runtime.Stack`. | Package stack is used for parsing stacks from `runtime.Stack`. |

 Click to show internal directories. 

 Click to hide internal directories. 

[Why Go](https://go.dev/solutions)[Use Cases](https://go.dev/solutions#use-cases)[Case Studies](https://go.dev/solutions#case-studies)

[Get Started](https://learn.go.dev/)[Playground](https://play.golang.org/)[Tour](https://tour.golang.org/)[Stack Overflow](https://stackoverflow.com/questions/tagged/go?tab=Newest)[Help](https://go.dev/help)

[Packages](https://pkg.go.dev/)[Standard Library](https://pkg.go.dev/std)[Sub-repositories](https://pkg.go.dev/golang.org/x)[About Go Packages](https://pkg.go.dev/about)

[About](https://go.dev/project)[Download](https://go.dev/dl/)[Blog](https://go.dev/blog)[Issue Tracker](https://github.com/golang/go/issues)[Release Notes](https://go.dev/doc/devel/release.html)[Brand Guidelines](https://go.dev/brand)[Code of Conduct](https://go.dev/conduct)

[Connect](https://www.twitter.com/golang)[Twitter](https://www.twitter.com/golang)[GitHub](https://github.com/golang)[Slack](https://invite.slack.golangbridge.org/)[r/golang](https://reddit.com/r/golang)[Meetup](https://www.meetup.com/pro/go)[Golang Weekly](https://golangweekly.com/)

![Image 54: Gopher in flight goggles](https://pkg.go.dev/static/shared/gopher/pilot-bust-1431x901.svg)
*   [Copyright](https://go.dev/copyright)
*   [Terms of Service](https://go.dev/tos)
*   [Privacy Policy](http://www.google.com/intl/en/policies/privacy/)
*   [Report an Issue](https://go.dev/s/pkgsite-feedback)
*   ![Image 55: System theme](https://pkg.go.dev/static/shared/icon/brightness_6_gm_grey_24dp.svg)![Image 56: Dark theme](https://pkg.go.dev/static/shared/icon/brightness_2_gm_grey_24dp.svg)![Image 57: Light theme](https://pkg.go.dev/static/shared/icon/light_mode_gm_grey_24dp.svg)
Theme Toggle

*   ![Image 58](https://pkg.go.dev/static/shared/icon/keyboard_grey_24dp.svg)
Shortcuts Modal

[![Image 59: Google logo](https://pkg.go.dev/static/shared/logo/google-white.svg)](https://google.com/)

Jump to
-------

![Image 60](https://pkg.go.dev/static/shared/icon/close_gm_grey_24dp.svg)

Close

Keyboard shortcuts
------------------

![Image 61](https://pkg.go.dev/static/shared/icon/close_gm_grey_24dp.svg)

**?**: This menu
**/**: Search site
**f** or **F**: Jump to
**y** or **Y**: Canonical URL

Close

go.dev uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay
