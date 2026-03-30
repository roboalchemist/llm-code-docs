# Source: https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/circuitbreaker

Title: circuitbreaker package - go.temporal.io/server/common/circuitbreaker - Go Packages

URL Source: https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/circuitbreaker

Markdown Content:
circuitbreaker package - go.temporal.io/server/common/circuitbreaker - Go Packages
===============

[![Image 1: Go](https://pkg.go.dev/static/shared/logo/go-white.svg)](https://go.dev/)

[Skip to Main Content](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/circuitbreaker#main-content)

![Image 2](https://pkg.go.dev/static/shared/icon/search_gm_grey_24dp.svg)![Image 3](https://pkg.go.dev/static/shared/icon/search_gm_grey_24dp.svg)

*   [Why Go ![Image 4: submenu dropdown icon](https://pkg.go.dev/static/shared/icon/arrow_drop_down_gm_grey_24dp.svg)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/circuitbreaker#)
    *   [Case Studies](https://go.dev/solutions#case-studies) 
Common problems companies solve with Go

    *   [Use Cases](https://go.dev/solutions#use-cases) 
Stories about how and why companies use Go

    *   [Security](https://go.dev/security/) 
How Go can help keep you secure by default

*   [Learn](https://go.dev/learn/)
*   [Docs ![Image 5: submenu dropdown icon](https://pkg.go.dev/static/shared/icon/arrow_drop_down_gm_grey_24dp.svg)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/circuitbreaker#)
    *   [Effective Go](https://go.dev/doc/effective_go) 
Tips for writing clear, performant, and idiomatic Go code

    *   [Go User Manual](https://go.dev/doc/) 
A complete introduction to building software with Go

    *   [Standard library](https://pkg.go.dev/std) 
Reference documentation for Go's standard library

    *   [Release Notes](https://go.dev/doc/devel/release) 
Learn what's new in each Go release

*   [Packages](https://pkg.go.dev/)
*   [Community ![Image 6: submenu dropdown icon](https://pkg.go.dev/static/shared/icon/arrow_drop_down_gm_grey_24dp.svg)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/circuitbreaker#)
    *   [Recorded Talks](https://go.dev/talks/) 
Videos from prior events

    *   [Meetups _![Image 7](https://pkg.go.dev/static/shared/icon/launch\_gm\_grey\_24dp.svg)_](https://www.meetup.com/pro/go) 
Meet other local Go developers

    *   [Conferences _![Image 8](https://pkg.go.dev/static/shared/icon/launch\_gm\_grey\_24dp.svg)_](https://github.com/golang/go/wiki/Conferences) 
Learn and network with Go developers from around the world

    *   [Go blog](https://go.dev/blog) 
The Go project's official blog.

    *   [Go project](https://go.dev/help) 
Get help and stay informed from Go

    *    Get connected  [![Image 9](https://pkg.go.dev/static/shared/logo/social/google-groups.svg)](https://groups.google.com/g/golang-nuts "Get connected with google-groups (Opens in new window)")[![Image 10](https://pkg.go.dev/static/shared/logo/social/github.svg)](https://github.com/golang "Get connected with github (Opens in new window)")[![Image 11](https://pkg.go.dev/static/shared/logo/social/twitter.svg)](https://twitter.com/golang "Get connected with twitter (Opens in new window)")[![Image 12](https://pkg.go.dev/static/shared/logo/social/reddit.svg)](https://www.reddit.com/r/golang/ "Get connected with reddit (Opens in new window)")[![Image 13](https://pkg.go.dev/static/shared/logo/social/slack.svg)](https://invite.slack.golangbridge.org/ "Get connected with slack (Opens in new window)")[![Image 14](https://pkg.go.dev/static/shared/logo/social/stack-overflow.svg)](https://stackoverflow.com/collectives/go) 

[![Image 15: Go](https://pkg.go.dev/static/shared/logo/go-blue.svg)](https://go.dev/)

*   [Why Go _![Image 16](https://pkg.go.dev/static/shared/icon/navigate\_next\_gm\_grey\_24dp.svg)_](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/circuitbreaker#)

[_![Image 17](https://pkg.go.dev/static/shared/icon/navigate\_before\_gm\_grey\_24dp.svg)_ Why Go](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/circuitbreaker#) 
    *   [Case Studies](https://go.dev/solutions#case-studies)
    *   [Use Cases](https://go.dev/solutions#use-cases)
    *   [Security](https://go.dev/security/)

*   [Learn](https://go.dev/learn/)
*   [Docs _![Image 18](https://pkg.go.dev/static/shared/icon/navigate\_next\_gm\_grey\_24dp.svg)_](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/circuitbreaker#)

[_![Image 19](https://pkg.go.dev/static/shared/icon/navigate\_before\_gm\_grey\_24dp.svg)_ Docs](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/circuitbreaker#) 
    *   [Effective Go](https://go.dev/doc/effective_go)
    *   [Go User Manual](https://go.dev/doc/)
    *   [Standard library](https://pkg.go.dev/std)
    *   [Release Notes](https://go.dev/doc/devel/release)

*   [Packages](https://pkg.go.dev/)
*   [Community _![Image 20](https://pkg.go.dev/static/shared/icon/navigate\_next\_gm\_grey\_24dp.svg)_](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/circuitbreaker#)

[_![Image 21](https://pkg.go.dev/static/shared/icon/navigate\_before\_gm\_grey\_24dp.svg)_ Community](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/circuitbreaker#) 
    *   [Recorded Talks](https://go.dev/talks/)
    *   [Meetups _![Image 22](https://pkg.go.dev/static/shared/icon/launch\_gm\_grey\_24dp.svg)_](https://www.meetup.com/pro/go)
    *   [Conferences _![Image 23](https://pkg.go.dev/static/shared/icon/launch\_gm\_grey\_24dp.svg)_](https://github.com/golang/go/wiki/Conferences)
    *   [Go blog](https://go.dev/blog)
    *   [Go project](https://go.dev/help)
    *   Get connected [![Image 24](https://pkg.go.dev/static/shared/logo/social/google-groups.svg)](https://groups.google.com/g/golang-nuts)[![Image 25](https://pkg.go.dev/static/shared/logo/social/github.svg)](https://github.com/golang)[![Image 26](https://pkg.go.dev/static/shared/logo/social/twitter.svg)](https://twitter.com/golang)[![Image 27](https://pkg.go.dev/static/shared/logo/social/reddit.svg)](https://www.reddit.com/r/golang/)[![Image 28](https://pkg.go.dev/static/shared/logo/social/slack.svg)](https://invite.slack.golangbridge.org/)[![Image 29](https://pkg.go.dev/static/shared/logo/social/stack-overflow.svg)](https://stackoverflow.com/collectives/go) 

1.   [Discover Packages](https://pkg.go.dev/)
2.   [go.temporal.io/server](https://pkg.go.dev/go.temporal.io/server@v1.30.0)
3.   [common](https://pkg.go.dev/go.temporal.io/server/common@v1.30.0)
4.   [circuitbreaker](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/circuitbreaker)![Image 30](https://pkg.go.dev/static/shared/icon/content_copy_gm_grey_24dp.svg)

[![Image 31: Go](https://pkg.go.dev/static/shared/logo/go-blue.svg)](https://go.dev/)
circuitbreaker
==============

package![Image 32](https://pkg.go.dev/static/shared/icon/content_copy_gm_grey_24dp.svg)

[Version: v1.30.0](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/circuitbreaker?tab=versions)

 Opens a new window with list of versions in this module. 

Latest Latest 

![Image 33: Warning](https://pkg.go.dev/static/shared/icon/alert_gm_grey_24dp.svg)
This package is not in the latest version of its module.

[Go to latest](https://pkg.go.dev/go.temporal.io/server/common/circuitbreaker) Published: Feb 4, 2026  License: [MIT](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/circuitbreaker?tab=licenses)

 Opens a new window with license information. 

[Imports: 4](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/circuitbreaker?tab=imports)

 Opens a new window with list of imports. 

[Imported by: 0](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/circuitbreaker?tab=importedby)

 Opens a new window with list of known importers. 

Details
-------

*   ![Image 34: checked](https://pkg.go.dev/static/shared/icon/check_circle_gm_grey_24dp.svg) Valid [go.mod](https://github.com/temporalio/temporal/tree/v1.30.0/go.mod) file ![Image 35](https://pkg.go.dev/static/shared/icon/help_gm_grey_24dp.svg)
The Go module system was introduced in Go 1.11 and is the official dependency management solution for Go. 
*   ![Image 36: checked](https://pkg.go.dev/static/shared/icon/check_circle_gm_grey_24dp.svg) Redistributable license ![Image 37](https://pkg.go.dev/static/shared/icon/help_gm_grey_24dp.svg)
Redistributable licenses place minimal restrictions on how software can be used, modified, and redistributed. 
*   ![Image 38: checked](https://pkg.go.dev/static/shared/icon/check_circle_gm_grey_24dp.svg) Tagged version ![Image 39](https://pkg.go.dev/static/shared/icon/help_gm_grey_24dp.svg)
Modules with tagged versions give importers more predictable builds. 
*   ![Image 40: checked](https://pkg.go.dev/static/shared/icon/check_circle_gm_grey_24dp.svg) Stable version ![Image 41](https://pkg.go.dev/static/shared/icon/help_gm_grey_24dp.svg)
When a project reaches major version v1 it is considered stable. 
*   [Learn more about best practices](https://pkg.go.dev/about#best-practices)

Repository
----------

[github.com/temporalio/temporal](https://github.com/temporalio/temporal "https://github.com/temporalio/temporal")

Links
-----

*   [![Image 42: Open Source Insights Logo](https://pkg.go.dev/static/shared/icon/depsdev-logo.svg) Open Source Insights](https://deps.dev/go/go.temporal.io%2Fserver/v1.30.0 "View this module on Open Source Insights")

 Jump to ... 

*   [Documentation](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/circuitbreaker#section-documentation)
    *   [Index](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/circuitbreaker#pkg-index)
    *   [Constants](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/circuitbreaker#pkg-constants)
    *   [Variables](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/circuitbreaker#pkg-variables)
    *   [Functions](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/circuitbreaker#pkg-functions)
    *   [Types](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/circuitbreaker#pkg-types)
        *   [type Settings](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/circuitbreaker#Settings "type Settings")
        *   [type TwoStepCircuitBreaker](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/circuitbreaker#TwoStepCircuitBreaker "type TwoStepCircuitBreaker")
        *   [type TwoStepCircuitBreakerWithDynamicSettings](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/circuitbreaker#TwoStepCircuitBreakerWithDynamicSettings "type TwoStepCircuitBreakerWithDynamicSettings")
            *   [NewTwoStepCircuitBreakerWithDynamicSettings(settings)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/circuitbreaker#NewTwoStepCircuitBreakerWithDynamicSettings "NewTwoStepCircuitBreakerWithDynamicSettings(settings)")
            *   [(c) Allow()](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/circuitbreaker#TwoStepCircuitBreakerWithDynamicSettings.Allow "(c) Allow()")
            *   [(c) Counts()](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/circuitbreaker#TwoStepCircuitBreakerWithDynamicSettings.Counts "(c) Counts()")
            *   [(c) Name()](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/circuitbreaker#TwoStepCircuitBreakerWithDynamicSettings.Name "(c) Name()")
            *   [(c) State()](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/circuitbreaker#TwoStepCircuitBreakerWithDynamicSettings.State "(c) State()")
            *   [(c) UpdateSettings(ds)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/circuitbreaker#TwoStepCircuitBreakerWithDynamicSettings.UpdateSettings "(c) UpdateSettings(ds)")

*   [Source Files](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/circuitbreaker#section-sourcefiles)

![Image 43](https://pkg.go.dev/static/shared/icon/code_gm_grey_24dp.svg) Documentation [¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/circuitbreaker#section-documentation "Go to Documentation")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Index [¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/circuitbreaker#pkg-index "Go to Index")

*   [type Settings](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/circuitbreaker#Settings)
*   [type TwoStepCircuitBreaker](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/circuitbreaker#TwoStepCircuitBreaker)
*   [type TwoStepCircuitBreakerWithDynamicSettings](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/circuitbreaker#TwoStepCircuitBreakerWithDynamicSettings)
*       *   [func NewTwoStepCircuitBreakerWithDynamicSettings(settings Settings) *TwoStepCircuitBreakerWithDynamicSettings](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/circuitbreaker#NewTwoStepCircuitBreakerWithDynamicSettings)

*       *   [func (c *TwoStepCircuitBreakerWithDynamicSettings) Allow() (done func(success bool), err error)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/circuitbreaker#TwoStepCircuitBreakerWithDynamicSettings.Allow)
    *   [func (c *TwoStepCircuitBreakerWithDynamicSettings) Counts() gobreaker.Counts](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/circuitbreaker#TwoStepCircuitBreakerWithDynamicSettings.Counts)
    *   [func (c *TwoStepCircuitBreakerWithDynamicSettings) Name() string](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/circuitbreaker#TwoStepCircuitBreakerWithDynamicSettings.Name)
    *   [func (c *TwoStepCircuitBreakerWithDynamicSettings) State() gobreaker.State](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/circuitbreaker#TwoStepCircuitBreakerWithDynamicSettings.State)
    *   [func (c *TwoStepCircuitBreakerWithDynamicSettings) UpdateSettings(ds dynamicconfig.CircuitBreakerSettings)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/circuitbreaker#TwoStepCircuitBreakerWithDynamicSettings.UpdateSettings)

### Constants [¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/circuitbreaker#pkg-constants "Go to Constants")

This section is empty.

### Variables [¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/circuitbreaker#pkg-variables "Go to Variables")

This section is empty.

### Functions [¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/circuitbreaker#pkg-functions "Go to Functions")

This section is empty.

### Types [¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/circuitbreaker#pkg-types "Go to Types")

#### type [Settings](https://github.com/temporalio/temporal/blob/v1.30.0/common/circuitbreaker/circuitbreaker.go#L33)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/circuitbreaker#Settings "Go to Settings")

type Settings struct {
	// For the following options, check gobreaker docs for details.
 Name [string](https://pkg.go.dev/builtin#string) ReadyToTrip func(counts [gobreaker](https://pkg.go.dev/github.com/sony/gobreaker).[Counts](https://pkg.go.dev/github.com/sony/gobreaker#Counts)) [bool](https://pkg.go.dev/builtin#bool) OnStateChange func(name [string](https://pkg.go.dev/builtin#string), from [gobreaker](https://pkg.go.dev/github.com/sony/gobreaker).[State](https://pkg.go.dev/github.com/sony/gobreaker#State), to [gobreaker](https://pkg.go.dev/github.com/sony/gobreaker).[State](https://pkg.go.dev/github.com/sony/gobreaker#State)) }

#### type [TwoStepCircuitBreaker](https://github.com/temporalio/temporal/blob/v1.30.0/common/circuitbreaker/circuitbreaker.go#L12)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/circuitbreaker#TwoStepCircuitBreaker "Go to TwoStepCircuitBreaker")

type TwoStepCircuitBreaker interface {
 Name() [string](https://pkg.go.dev/builtin#string) State() [gobreaker](https://pkg.go.dev/github.com/sony/gobreaker).[State](https://pkg.go.dev/github.com/sony/gobreaker#State) Counts() [gobreaker](https://pkg.go.dev/github.com/sony/gobreaker).[Counts](https://pkg.go.dev/github.com/sony/gobreaker#Counts) Allow() (done func(success [bool](https://pkg.go.dev/builtin#bool)), err [error](https://pkg.go.dev/builtin#error)) }

#### type [TwoStepCircuitBreakerWithDynamicSettings](https://github.com/temporalio/temporal/blob/v1.30.0/common/circuitbreaker/circuitbreaker.go#L23)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/circuitbreaker#TwoStepCircuitBreakerWithDynamicSettings "Go to TwoStepCircuitBreakerWithDynamicSettings")

type TwoStepCircuitBreakerWithDynamicSettings struct {
	// contains filtered or unexported fields
}

TwoStepCircuitBreakerWithDynamicSettings is a wrapper of gobreaker.TwoStepCircuitBreaker that calls the settingsFn everytime the Allow function is called and replaces the circuit breaker if there is a change in the settings object. Note that in this case, the previous state of the circuit breaker is lost.

#### func [NewTwoStepCircuitBreakerWithDynamicSettings](https://github.com/temporalio/temporal/blob/v1.30.0/common/circuitbreaker/circuitbreaker.go#L44)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/circuitbreaker#NewTwoStepCircuitBreakerWithDynamicSettings "Go to NewTwoStepCircuitBreakerWithDynamicSettings")

func NewTwoStepCircuitBreakerWithDynamicSettings(
	settings [Settings](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/circuitbreaker#Settings),
) *[TwoStepCircuitBreakerWithDynamicSettings](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/circuitbreaker#TwoStepCircuitBreakerWithDynamicSettings)

Caller must call UpdateSettings once before using this object.

#### func (*TwoStepCircuitBreakerWithDynamicSettings) [Allow](https://github.com/temporalio/temporal/blob/v1.30.0/common/circuitbreaker/circuitbreaker.go#L85)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/circuitbreaker#TwoStepCircuitBreakerWithDynamicSettings.Allow "Go to TwoStepCircuitBreakerWithDynamicSettings.Allow")

func (c *[TwoStepCircuitBreakerWithDynamicSettings](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/circuitbreaker#TwoStepCircuitBreakerWithDynamicSettings)) Allow() (done func(success [bool](https://pkg.go.dev/builtin#bool)), err [error](https://pkg.go.dev/builtin#error))

#### func (*TwoStepCircuitBreakerWithDynamicSettings) [Counts](https://github.com/temporalio/temporal/blob/v1.30.0/common/circuitbreaker/circuitbreaker.go#L81)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/circuitbreaker#TwoStepCircuitBreakerWithDynamicSettings.Counts "Go to TwoStepCircuitBreakerWithDynamicSettings.Counts")

func (c *[TwoStepCircuitBreakerWithDynamicSettings](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/circuitbreaker#TwoStepCircuitBreakerWithDynamicSettings)) Counts() [gobreaker](https://pkg.go.dev/github.com/sony/gobreaker).[Counts](https://pkg.go.dev/github.com/sony/gobreaker#Counts)

#### func (*TwoStepCircuitBreakerWithDynamicSettings) [Name](https://github.com/temporalio/temporal/blob/v1.30.0/common/circuitbreaker/circuitbreaker.go#L73)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/circuitbreaker#TwoStepCircuitBreakerWithDynamicSettings.Name "Go to TwoStepCircuitBreakerWithDynamicSettings.Name")

func (c *[TwoStepCircuitBreakerWithDynamicSettings](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/circuitbreaker#TwoStepCircuitBreakerWithDynamicSettings)) Name() [string](https://pkg.go.dev/builtin#string)

#### func (*TwoStepCircuitBreakerWithDynamicSettings) [State](https://github.com/temporalio/temporal/blob/v1.30.0/common/circuitbreaker/circuitbreaker.go#L77)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/circuitbreaker#TwoStepCircuitBreakerWithDynamicSettings.State "Go to TwoStepCircuitBreakerWithDynamicSettings.State")

func (c *[TwoStepCircuitBreakerWithDynamicSettings](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/circuitbreaker#TwoStepCircuitBreakerWithDynamicSettings)) State() [gobreaker](https://pkg.go.dev/github.com/sony/gobreaker).[State](https://pkg.go.dev/github.com/sony/gobreaker#State)

#### func (*TwoStepCircuitBreakerWithDynamicSettings) [UpdateSettings](https://github.com/temporalio/temporal/blob/v1.30.0/common/circuitbreaker/circuitbreaker.go#L54)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/circuitbreaker#TwoStepCircuitBreakerWithDynamicSettings.UpdateSettings "Go to TwoStepCircuitBreakerWithDynamicSettings.UpdateSettings")

func (c *[TwoStepCircuitBreakerWithDynamicSettings](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/circuitbreaker#TwoStepCircuitBreakerWithDynamicSettings)) UpdateSettings(
	ds [dynamicconfig](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/dynamicconfig).[CircuitBreakerSettings](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/dynamicconfig#CircuitBreakerSettings),
)

![Image 44](https://pkg.go.dev/static/shared/icon/insert_drive_file_gm_grey_24dp.svg) Source Files [¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/circuitbreaker#section-sourcefiles "Go to Source Files")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[View all Source files](https://github.com/temporalio/temporal/tree/v1.30.0/common/circuitbreaker)

*   [circuitbreaker.go](https://github.com/temporalio/temporal/blob/v1.30.0/common/circuitbreaker/circuitbreaker.go "circuitbreaker.go")

 Click to show internal directories. 

 Click to hide internal directories. 

[Why Go](https://go.dev/solutions)[Use Cases](https://go.dev/solutions#use-cases)[Case Studies](https://go.dev/solutions#case-studies)

[Get Started](https://learn.go.dev/)[Playground](https://play.golang.org/)[Tour](https://tour.golang.org/)[Stack Overflow](https://stackoverflow.com/questions/tagged/go?tab=Newest)[Help](https://go.dev/help)

[Packages](https://pkg.go.dev/)[Standard Library](https://pkg.go.dev/std)[Sub-repositories](https://pkg.go.dev/golang.org/x)[About Go Packages](https://pkg.go.dev/about)

[About](https://go.dev/project)[Download](https://go.dev/dl/)[Blog](https://go.dev/blog)[Issue Tracker](https://github.com/golang/go/issues)[Release Notes](https://go.dev/doc/devel/release.html)[Brand Guidelines](https://go.dev/brand)[Code of Conduct](https://go.dev/conduct)

[Connect](https://www.twitter.com/golang)[Twitter](https://www.twitter.com/golang)[GitHub](https://github.com/golang)[Slack](https://invite.slack.golangbridge.org/)[r/golang](https://reddit.com/r/golang)[Meetup](https://www.meetup.com/pro/go)[Golang Weekly](https://golangweekly.com/)

![Image 45: Gopher in flight goggles](https://pkg.go.dev/static/shared/gopher/pilot-bust-1431x901.svg)
*   [Copyright](https://go.dev/copyright)
*   [Terms of Service](https://go.dev/tos)
*   [Privacy Policy](http://www.google.com/intl/en/policies/privacy/)
*   [Report an Issue](https://go.dev/s/pkgsite-feedback)
*   ![Image 46: System theme](https://pkg.go.dev/static/shared/icon/brightness_6_gm_grey_24dp.svg)![Image 47: Dark theme](https://pkg.go.dev/static/shared/icon/brightness_2_gm_grey_24dp.svg)![Image 48: Light theme](https://pkg.go.dev/static/shared/icon/light_mode_gm_grey_24dp.svg)
Theme Toggle

*   ![Image 49](https://pkg.go.dev/static/shared/icon/keyboard_grey_24dp.svg)
Shortcuts Modal

[![Image 50: Google logo](https://pkg.go.dev/static/shared/logo/google-white.svg)](https://google.com/)

Jump to
-------

![Image 51](https://pkg.go.dev/static/shared/icon/close_gm_grey_24dp.svg)

Close

Keyboard shortcuts
------------------

![Image 52](https://pkg.go.dev/static/shared/icon/close_gm_grey_24dp.svg)

**?**: This menu
**/**: Search site
**f** or **F**: Jump to
**y** or **Y**: Canonical URL

Close

go.dev uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay
