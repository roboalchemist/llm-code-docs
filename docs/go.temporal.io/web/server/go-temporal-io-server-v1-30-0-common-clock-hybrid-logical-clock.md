# Source: https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock/hybrid_logical_clock

Title: hybrid_logical_clock package - go.temporal.io/server/common/clock/hybrid_logical_clock - Go Packages

URL Source: https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock/hybrid_logical_clock

Markdown Content:
hybrid_logical_clock package - go.temporal.io/server/common/clock/hybrid_logical_clock - Go Packages
===============

[![Image 1: Go](https://pkg.go.dev/static/shared/logo/go-white.svg)](https://go.dev/)

[Skip to Main Content](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock/hybrid_logical_clock#main-content)

![Image 2](https://pkg.go.dev/static/shared/icon/search_gm_grey_24dp.svg)![Image 3](https://pkg.go.dev/static/shared/icon/search_gm_grey_24dp.svg)

*   [Why Go ![Image 4: submenu dropdown icon](https://pkg.go.dev/static/shared/icon/arrow_drop_down_gm_grey_24dp.svg)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock/hybrid_logical_clock#)
    *   [Case Studies](https://go.dev/solutions#case-studies) 
Common problems companies solve with Go

    *   [Use Cases](https://go.dev/solutions#use-cases) 
Stories about how and why companies use Go

    *   [Security](https://go.dev/security/) 
How Go can help keep you secure by default

*   [Learn](https://go.dev/learn/)
*   [Docs ![Image 5: submenu dropdown icon](https://pkg.go.dev/static/shared/icon/arrow_drop_down_gm_grey_24dp.svg)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock/hybrid_logical_clock#)
    *   [Effective Go](https://go.dev/doc/effective_go) 
Tips for writing clear, performant, and idiomatic Go code

    *   [Go User Manual](https://go.dev/doc/) 
A complete introduction to building software with Go

    *   [Standard library](https://pkg.go.dev/std) 
Reference documentation for Go's standard library

    *   [Release Notes](https://go.dev/doc/devel/release) 
Learn what's new in each Go release

*   [Packages](https://pkg.go.dev/)
*   [Community ![Image 6: submenu dropdown icon](https://pkg.go.dev/static/shared/icon/arrow_drop_down_gm_grey_24dp.svg)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock/hybrid_logical_clock#)
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

*   [Why Go _![Image 16](https://pkg.go.dev/static/shared/icon/navigate\_next\_gm\_grey\_24dp.svg)_](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock/hybrid_logical_clock#)

[_![Image 17](https://pkg.go.dev/static/shared/icon/navigate\_before\_gm\_grey\_24dp.svg)_ Why Go](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock/hybrid_logical_clock#) 
    *   [Case Studies](https://go.dev/solutions#case-studies)
    *   [Use Cases](https://go.dev/solutions#use-cases)
    *   [Security](https://go.dev/security/)

*   [Learn](https://go.dev/learn/)
*   [Docs _![Image 18](https://pkg.go.dev/static/shared/icon/navigate\_next\_gm\_grey\_24dp.svg)_](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock/hybrid_logical_clock#)

[_![Image 19](https://pkg.go.dev/static/shared/icon/navigate\_before\_gm\_grey\_24dp.svg)_ Docs](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock/hybrid_logical_clock#) 
    *   [Effective Go](https://go.dev/doc/effective_go)
    *   [Go User Manual](https://go.dev/doc/)
    *   [Standard library](https://pkg.go.dev/std)
    *   [Release Notes](https://go.dev/doc/devel/release)

*   [Packages](https://pkg.go.dev/)
*   [Community _![Image 20](https://pkg.go.dev/static/shared/icon/navigate\_next\_gm\_grey\_24dp.svg)_](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock/hybrid_logical_clock#)

[_![Image 21](https://pkg.go.dev/static/shared/icon/navigate\_before\_gm\_grey\_24dp.svg)_ Community](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock/hybrid_logical_clock#) 
    *   [Recorded Talks](https://go.dev/talks/)
    *   [Meetups _![Image 22](https://pkg.go.dev/static/shared/icon/launch\_gm\_grey\_24dp.svg)_](https://www.meetup.com/pro/go)
    *   [Conferences _![Image 23](https://pkg.go.dev/static/shared/icon/launch\_gm\_grey\_24dp.svg)_](https://github.com/golang/go/wiki/Conferences)
    *   [Go blog](https://go.dev/blog)
    *   [Go project](https://go.dev/help)
    *   Get connected [![Image 24](https://pkg.go.dev/static/shared/logo/social/google-groups.svg)](https://groups.google.com/g/golang-nuts)[![Image 25](https://pkg.go.dev/static/shared/logo/social/github.svg)](https://github.com/golang)[![Image 26](https://pkg.go.dev/static/shared/logo/social/twitter.svg)](https://twitter.com/golang)[![Image 27](https://pkg.go.dev/static/shared/logo/social/reddit.svg)](https://www.reddit.com/r/golang/)[![Image 28](https://pkg.go.dev/static/shared/logo/social/slack.svg)](https://invite.slack.golangbridge.org/)[![Image 29](https://pkg.go.dev/static/shared/logo/social/stack-overflow.svg)](https://stackoverflow.com/collectives/go) 

1.   [Discover Packages](https://pkg.go.dev/)
2.   [go.temporal.io/server](https://pkg.go.dev/go.temporal.io/server@v1.30.0)
3.   [common](https://pkg.go.dev/go.temporal.io/server/common@v1.30.0)
4.   [clock](https://pkg.go.dev/go.temporal.io/server/common/clock@v1.30.0)
5.   [hybrid_logical_clock](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock/hybrid_logical_clock)![Image 30](https://pkg.go.dev/static/shared/icon/content_copy_gm_grey_24dp.svg)

[![Image 31: Go](https://pkg.go.dev/static/shared/logo/go-blue.svg)](https://go.dev/)
hybrid_logical_clock
====================

package![Image 32](https://pkg.go.dev/static/shared/icon/content_copy_gm_grey_24dp.svg)

[Version: v1.30.0](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock/hybrid_logical_clock?tab=versions)

 Opens a new window with list of versions in this module. 

Latest Latest 

![Image 33: Warning](https://pkg.go.dev/static/shared/icon/alert_gm_grey_24dp.svg)
This package is not in the latest version of its module.

[Go to latest](https://pkg.go.dev/go.temporal.io/server/common/clock/hybrid_logical_clock) Published: Feb 4, 2026  License: [MIT](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock/hybrid_logical_clock?tab=licenses)

 Opens a new window with license information. 

[Imports: 4](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock/hybrid_logical_clock?tab=imports)

 Opens a new window with list of imports. 

[Imported by: 0](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock/hybrid_logical_clock?tab=importedby)

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

*   [Documentation](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock/hybrid_logical_clock#section-documentation)
    *   [Index](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock/hybrid_logical_clock#pkg-index)
    *   [Constants](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock/hybrid_logical_clock#pkg-constants)
    *   [Variables](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock/hybrid_logical_clock#pkg-variables)
    *   [Functions](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock/hybrid_logical_clock#pkg-functions)
        *   [Compare(a, b)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock/hybrid_logical_clock#Compare "Compare(a, b)")
        *   [Equal(a, b)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock/hybrid_logical_clock#Equal "Equal(a, b)")
        *   [Greater(a, b)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock/hybrid_logical_clock#Greater "Greater(a, b)")
        *   [Less(a, b)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock/hybrid_logical_clock#Less "Less(a, b)")
        *   [ProtoTimestamp(c)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock/hybrid_logical_clock#ProtoTimestamp "ProtoTimestamp(c)")
        *   [Since(c)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock/hybrid_logical_clock#Since "Since(c)")
        *   [UTC(c)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock/hybrid_logical_clock#UTC "UTC(c)")

    *   [Types](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock/hybrid_logical_clock#pkg-types)
        *   [type Clock](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock/hybrid_logical_clock#Clock "type Clock")
            *   [Max(a, b)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock/hybrid_logical_clock#Max "Max(a, b)")
            *   [Min(a, b)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock/hybrid_logical_clock#Min "Min(a, b)")
            *   [Next(prior, source)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock/hybrid_logical_clock#Next "Next(prior, source)")
            *   [Zero(clusterID)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock/hybrid_logical_clock#Zero "Zero(clusterID)")

*   [Source Files](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock/hybrid_logical_clock#section-sourcefiles)

![Image 43](https://pkg.go.dev/static/shared/icon/code_gm_grey_24dp.svg) Documentation [¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock/hybrid_logical_clock#section-documentation "Go to Documentation")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Index [¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock/hybrid_logical_clock#pkg-index "Go to Index")

*   [func Compare(a *Clock, b *Clock) int](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock/hybrid_logical_clock#Compare)
*   [func Equal(a *Clock, b *Clock) bool](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock/hybrid_logical_clock#Equal)
*   [func Greater(a *Clock, b *Clock) bool](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock/hybrid_logical_clock#Greater)
*   [func Less(a *Clock, b *Clock) bool](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock/hybrid_logical_clock#Less)
*   [func ProtoTimestamp(c *Clock) *timestamppb.Timestamp](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock/hybrid_logical_clock#ProtoTimestamp)
*   [func Since(c *Clock) time.Duration](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock/hybrid_logical_clock#Since)
*   [func UTC(c *Clock) time.Time](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock/hybrid_logical_clock#UTC)
*   [type Clock](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock/hybrid_logical_clock#Clock)
*       *   [func Max(a *Clock, b *Clock) *Clock](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock/hybrid_logical_clock#Max)
    *   [func Min(a *Clock, b *Clock) *Clock](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock/hybrid_logical_clock#Min)
    *   [func Next(prior *Clock, source commonclock.TimeSource) *Clock](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock/hybrid_logical_clock#Next)
    *   [func Zero(clusterID int64) *Clock](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock/hybrid_logical_clock#Zero)

### Constants [¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock/hybrid_logical_clock#pkg-constants "Go to Constants")

This section is empty.

### Variables [¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock/hybrid_logical_clock#pkg-variables "Go to Variables")

This section is empty.

### Functions [¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock/hybrid_logical_clock#pkg-functions "Go to Functions")

#### func [Compare](https://github.com/temporalio/temporal/blob/v1.30.0/common/clock/hybrid_logical_clock/hybrid_logical_clock.go#L47)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock/hybrid_logical_clock#Compare "Go to Compare")

func Compare(a *[Clock](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock/hybrid_logical_clock#Clock), b *[Clock](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock/hybrid_logical_clock#Clock)) [int](https://pkg.go.dev/builtin#int)

Compare 2 Clocks, returns 0 if a == b, -1 if a > b, 1 if a < b

#### func [Equal](https://github.com/temporalio/temporal/blob/v1.30.0/common/clock/hybrid_logical_clock/hybrid_logical_clock.go#L84)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock/hybrid_logical_clock#Equal "Go to Equal")

func Equal(a *[Clock](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock/hybrid_logical_clock#Clock), b *[Clock](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock/hybrid_logical_clock#Clock)) [bool](https://pkg.go.dev/builtin#bool)

Equal returns whether two Clocks are equal

#### func [Greater](https://github.com/temporalio/temporal/blob/v1.30.0/common/clock/hybrid_logical_clock/hybrid_logical_clock.go#L58)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock/hybrid_logical_clock#Greater "Go to Greater")

func Greater(a *[Clock](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock/hybrid_logical_clock#Clock), b *[Clock](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock/hybrid_logical_clock#Clock)) [bool](https://pkg.go.dev/builtin#bool)

Greater returns true if a is greater than b

#### func [Less](https://github.com/temporalio/temporal/blob/v1.30.0/common/clock/hybrid_logical_clock/hybrid_logical_clock.go#L63)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock/hybrid_logical_clock#Less "Go to Less")

func Less(a *[Clock](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock/hybrid_logical_clock#Clock), b *[Clock](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock/hybrid_logical_clock#Clock)) [bool](https://pkg.go.dev/builtin#bool)

Greater returns true if a is greater than b

#### func [ProtoTimestamp](https://github.com/temporalio/temporal/blob/v1.30.0/common/clock/hybrid_logical_clock/hybrid_logical_clock.go#L102)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock/hybrid_logical_clock#ProtoTimestamp "Go to ProtoTimestamp")added in v1.24.0

func ProtoTimestamp(c *[Clock](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock/hybrid_logical_clock#Clock)) *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

ProtoTimestamp returns timestamppb.New(UTC(c))

#### func [Since](https://github.com/temporalio/temporal/blob/v1.30.0/common/clock/hybrid_logical_clock/hybrid_logical_clock.go#L97)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock/hybrid_logical_clock#Since "Go to Since")added in v1.22.1

func Since(c *[Clock](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock/hybrid_logical_clock#Clock)) [time](https://pkg.go.dev/time).[Duration](https://pkg.go.dev/time#Duration)

Since returns time.Since(UTC(c))

#### func [UTC](https://github.com/temporalio/temporal/blob/v1.30.0/common/clock/hybrid_logical_clock/hybrid_logical_clock.go#L89)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock/hybrid_logical_clock#UTC "Go to UTC")

func UTC(c *[Clock](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock/hybrid_logical_clock#Clock)) [time](https://pkg.go.dev/time).[Time](https://pkg.go.dev/time#Time)

UTC returns a Time from a Clock in millisecond resolution. The Time's Location is set to UTC.

### Types [¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock/hybrid_logical_clock#pkg-types "Go to Types")

#### type [Clock](https://github.com/temporalio/temporal/blob/v1.30.0/common/clock/hybrid_logical_clock/hybrid_logical_clock.go#L11)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock/hybrid_logical_clock#Clock "Go to Clock")

type Clock = [clockspb](https://pkg.go.dev/go.temporal.io/server@v1.30.0/api/clock/v1).[HybridLogicalClock](https://pkg.go.dev/go.temporal.io/server@v1.30.0/api/clock/v1#HybridLogicalClock)

#### func [Max](https://github.com/temporalio/temporal/blob/v1.30.0/common/clock/hybrid_logical_clock/hybrid_logical_clock.go#L68)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock/hybrid_logical_clock#Max "Go to Max")

func Max(a *[Clock](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock/hybrid_logical_clock#Clock), b *[Clock](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock/hybrid_logical_clock#Clock)) *[Clock](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock/hybrid_logical_clock#Clock)

Max returns the maximum of two Clocks

#### func [Min](https://github.com/temporalio/temporal/blob/v1.30.0/common/clock/hybrid_logical_clock/hybrid_logical_clock.go#L76)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock/hybrid_logical_clock#Min "Go to Min")added in v1.21.1

func Min(a *[Clock](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock/hybrid_logical_clock#Clock), b *[Clock](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock/hybrid_logical_clock#Clock)) *[Clock](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock/hybrid_logical_clock#Clock)

Min returns the minimum of two Clocks

#### func [Next](https://github.com/temporalio/temporal/blob/v1.30.0/common/clock/hybrid_logical_clock/hybrid_logical_clock.go#L16)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock/hybrid_logical_clock#Next "Go to Next")

func Next(prior *[Clock](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock/hybrid_logical_clock#Clock), source [commonclock](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock).[TimeSource](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#TimeSource)) *[Clock](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock/hybrid_logical_clock#Clock)

Next generates the next clock timestamp given the current clock. HybridLogicalClock requires the previous clock to ensure that time doesn't move backwards and the next clock is monotonically increasing.

#### func [Zero](https://github.com/temporalio/temporal/blob/v1.30.0/common/clock/hybrid_logical_clock/hybrid_logical_clock.go#L32)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock/hybrid_logical_clock#Zero "Go to Zero")

func Zero(clusterID [int64](https://pkg.go.dev/builtin#int64)) *[Clock](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock/hybrid_logical_clock#Clock)

Zero generates a zeroed logical clock for the cluster ID.

![Image 44](https://pkg.go.dev/static/shared/icon/insert_drive_file_gm_grey_24dp.svg) Source Files [¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock/hybrid_logical_clock#section-sourcefiles "Go to Source Files")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[View all Source files](https://github.com/temporalio/temporal/tree/v1.30.0/common/clock/hybrid_logical_clock)

*   [hybrid_logical_clock.go](https://github.com/temporalio/temporal/blob/v1.30.0/common/clock/hybrid_logical_clock/hybrid_logical_clock.go "hybrid_logical_clock.go")

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
