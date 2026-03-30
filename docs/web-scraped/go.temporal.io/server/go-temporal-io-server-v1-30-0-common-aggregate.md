# Source: https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/aggregate

Title: aggregate package - go.temporal.io/server/common/aggregate - Go Packages

URL Source: https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/aggregate

Markdown Content:
aggregate package - go.temporal.io/server/common/aggregate - Go Packages
===============

[![Image 2: Go](https://pkg.go.dev/static/shared/logo/go-white.svg)](https://go.dev/)

[Skip to Main Content](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/aggregate#main-content)

![Image 3](https://pkg.go.dev/static/shared/icon/search_gm_grey_24dp.svg)![Image 4](https://pkg.go.dev/static/shared/icon/search_gm_grey_24dp.svg)

*   [Why Go ![Image 5: submenu dropdown icon](https://pkg.go.dev/static/shared/icon/arrow_drop_down_gm_grey_24dp.svg)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/aggregate#)
    *   [Case Studies](https://go.dev/solutions#case-studies) 
Common problems companies solve with Go

    *   [Use Cases](https://go.dev/solutions#use-cases) 
Stories about how and why companies use Go

    *   [Security](https://go.dev/security/) 
How Go can help keep you secure by default

*   [Learn](https://go.dev/learn/)
*   [Docs ![Image 6: submenu dropdown icon](https://pkg.go.dev/static/shared/icon/arrow_drop_down_gm_grey_24dp.svg)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/aggregate#)
    *   [Effective Go](https://go.dev/doc/effective_go) 
Tips for writing clear, performant, and idiomatic Go code

    *   [Go User Manual](https://go.dev/doc/) 
A complete introduction to building software with Go

    *   [Standard library](https://pkg.go.dev/std) 
Reference documentation for Go's standard library

    *   [Release Notes](https://go.dev/doc/devel/release) 
Learn what's new in each Go release

*   [Packages](https://pkg.go.dev/)
*   [Community ![Image 7: submenu dropdown icon](https://pkg.go.dev/static/shared/icon/arrow_drop_down_gm_grey_24dp.svg)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/aggregate#)
    *   [Recorded Talks](https://go.dev/talks/) 
Videos from prior events

    *   [Meetups _![Image 8](https://pkg.go.dev/static/shared/icon/launch\_gm\_grey\_24dp.svg)_](https://www.meetup.com/pro/go) 
Meet other local Go developers

    *   [Conferences _![Image 9](https://pkg.go.dev/static/shared/icon/launch\_gm\_grey\_24dp.svg)_](https://github.com/golang/go/wiki/Conferences) 
Learn and network with Go developers from around the world

    *   [Go blog](https://go.dev/blog) 
The Go project's official blog.

    *   [Go project](https://go.dev/help) 
Get help and stay informed from Go

    *    Get connected  [![Image 10](https://pkg.go.dev/static/shared/logo/social/google-groups.svg)](https://groups.google.com/g/golang-nuts "Get connected with google-groups (Opens in new window)")[![Image 11](https://pkg.go.dev/static/shared/logo/social/github.svg)](https://github.com/golang "Get connected with github (Opens in new window)")[![Image 12](https://pkg.go.dev/static/shared/logo/social/twitter.svg)](https://twitter.com/golang "Get connected with twitter (Opens in new window)")[![Image 13](https://pkg.go.dev/static/shared/logo/social/reddit.svg)](https://www.reddit.com/r/golang/ "Get connected with reddit (Opens in new window)")[![Image 14](https://pkg.go.dev/static/shared/logo/social/slack.svg)](https://invite.slack.golangbridge.org/ "Get connected with slack (Opens in new window)")[![Image 15](https://pkg.go.dev/static/shared/logo/social/stack-overflow.svg)](https://stackoverflow.com/collectives/go) 

[![Image 16: Go](https://pkg.go.dev/static/shared/logo/go-blue.svg)](https://go.dev/)

*   [Why Go _![Image 17](https://pkg.go.dev/static/shared/icon/navigate\_next\_gm\_grey\_24dp.svg)_](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/aggregate#)

[_![Image 18](https://pkg.go.dev/static/shared/icon/navigate\_before\_gm\_grey\_24dp.svg)_ Why Go](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/aggregate#) 
    *   [Case Studies](https://go.dev/solutions#case-studies)
    *   [Use Cases](https://go.dev/solutions#use-cases)
    *   [Security](https://go.dev/security/)

*   [Learn](https://go.dev/learn/)
*   [Docs _![Image 19](https://pkg.go.dev/static/shared/icon/navigate\_next\_gm\_grey\_24dp.svg)_](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/aggregate#)

[_![Image 20](https://pkg.go.dev/static/shared/icon/navigate\_before\_gm\_grey\_24dp.svg)_ Docs](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/aggregate#) 
    *   [Effective Go](https://go.dev/doc/effective_go)
    *   [Go User Manual](https://go.dev/doc/)
    *   [Standard library](https://pkg.go.dev/std)
    *   [Release Notes](https://go.dev/doc/devel/release)

*   [Packages](https://pkg.go.dev/)
*   [Community _![Image 21](https://pkg.go.dev/static/shared/icon/navigate\_next\_gm\_grey\_24dp.svg)_](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/aggregate#)

[_![Image 22](https://pkg.go.dev/static/shared/icon/navigate\_before\_gm\_grey\_24dp.svg)_ Community](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/aggregate#) 
    *   [Recorded Talks](https://go.dev/talks/)
    *   [Meetups _![Image 23](https://pkg.go.dev/static/shared/icon/launch\_gm\_grey\_24dp.svg)_](https://www.meetup.com/pro/go)
    *   [Conferences _![Image 24](https://pkg.go.dev/static/shared/icon/launch\_gm\_grey\_24dp.svg)_](https://github.com/golang/go/wiki/Conferences)
    *   [Go blog](https://go.dev/blog)
    *   [Go project](https://go.dev/help)
    *   Get connected [![Image 25](https://pkg.go.dev/static/shared/logo/social/google-groups.svg)](https://groups.google.com/g/golang-nuts)[![Image 26](https://pkg.go.dev/static/shared/logo/social/github.svg)](https://github.com/golang)[![Image 27](https://pkg.go.dev/static/shared/logo/social/twitter.svg)](https://twitter.com/golang)[![Image 28](https://pkg.go.dev/static/shared/logo/social/reddit.svg)](https://www.reddit.com/r/golang/)[![Image 29](https://pkg.go.dev/static/shared/logo/social/slack.svg)](https://invite.slack.golangbridge.org/)[![Image 30](https://pkg.go.dev/static/shared/logo/social/stack-overflow.svg)](https://stackoverflow.com/collectives/go) 

1.   [Discover Packages](https://pkg.go.dev/)
2.   [go.temporal.io/server](https://pkg.go.dev/go.temporal.io/server@v1.30.0)
3.   [common](https://pkg.go.dev/go.temporal.io/server/common@v1.30.0)
4.   [aggregate](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/aggregate)![Image 31](https://pkg.go.dev/static/shared/icon/content_copy_gm_grey_24dp.svg)

[![Image 32: Go](https://pkg.go.dev/static/shared/logo/go-blue.svg)](https://go.dev/)
aggregate
=========

package![Image 33](https://pkg.go.dev/static/shared/icon/content_copy_gm_grey_24dp.svg)

[Version: v1.30.0](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/aggregate?tab=versions)

 Opens a new window with list of versions in this module. 

Latest Latest 

![Image 34: Warning](https://pkg.go.dev/static/shared/icon/alert_gm_grey_24dp.svg)
This package is not in the latest version of its module.

[Go to latest](https://pkg.go.dev/go.temporal.io/server/common/aggregate) Published: Feb 4, 2026  License: [MIT](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/aggregate?tab=licenses)

 Opens a new window with license information. 

[Imports: 2](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/aggregate?tab=imports)

 Opens a new window with list of imports. 

[Imported by: 0](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/aggregate?tab=importedby)

 Opens a new window with list of known importers. 

Details
-------

*   ![Image 35: checked](https://pkg.go.dev/static/shared/icon/check_circle_gm_grey_24dp.svg) Valid [go.mod](https://github.com/temporalio/temporal/tree/v1.30.0/go.mod) file ![Image 36](https://pkg.go.dev/static/shared/icon/help_gm_grey_24dp.svg)
The Go module system was introduced in Go 1.11 and is the official dependency management solution for Go. 
*   ![Image 37: checked](https://pkg.go.dev/static/shared/icon/check_circle_gm_grey_24dp.svg) Redistributable license ![Image 38](https://pkg.go.dev/static/shared/icon/help_gm_grey_24dp.svg)
Redistributable licenses place minimal restrictions on how software can be used, modified, and redistributed. 
*   ![Image 39: checked](https://pkg.go.dev/static/shared/icon/check_circle_gm_grey_24dp.svg) Tagged version ![Image 40](https://pkg.go.dev/static/shared/icon/help_gm_grey_24dp.svg)
Modules with tagged versions give importers more predictable builds. 
*   ![Image 41: checked](https://pkg.go.dev/static/shared/icon/check_circle_gm_grey_24dp.svg) Stable version ![Image 42](https://pkg.go.dev/static/shared/icon/help_gm_grey_24dp.svg)
When a project reaches major version v1 it is considered stable. 
*   [Learn more about best practices](https://pkg.go.dev/about#best-practices)

Repository
----------

[github.com/temporalio/temporal](https://github.com/temporalio/temporal "https://github.com/temporalio/temporal")

Links
-----

*   [![Image 43: Open Source Insights Logo](https://pkg.go.dev/static/shared/icon/depsdev-logo.svg) Open Source Insights](https://deps.dev/go/go.temporal.io%2Fserver/v1.30.0 "View this module on Open Source Insights")

 Jump to ... 

*   [Documentation](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/aggregate#section-documentation)
    *   [Index](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/aggregate#pkg-index)
    *   [Constants](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/aggregate#pkg-constants)
    *   [Variables](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/aggregate#pkg-variables)
    *   [Functions](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/aggregate#pkg-functions)
    *   [Types](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/aggregate#pkg-types)
        *   [type MovingWindowAverage](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/aggregate#MovingWindowAverage "type MovingWindowAverage")
        *   [type MovingWindowAvgImpl](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/aggregate#MovingWindowAvgImpl "type MovingWindowAvgImpl")
            *   [NewMovingWindowAvgImpl(windowSize, maxBufferSize)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/aggregate#NewMovingWindowAvgImpl "NewMovingWindowAvgImpl(windowSize, maxBufferSize)")
            *   [(a) Average()](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/aggregate#MovingWindowAvgImpl.Average "(a) Average()")
            *   [(a) Record(val)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/aggregate#MovingWindowAvgImpl.Record "(a) Record(val)")

*   [Source Files](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/aggregate#section-sourcefiles)

![Image 44](https://pkg.go.dev/static/shared/icon/code_gm_grey_24dp.svg) Documentation [¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/aggregate#section-documentation "Go to Documentation")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Index [¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/aggregate#pkg-index "Go to Index")

*   [type MovingWindowAverage](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/aggregate#MovingWindowAverage)
*   [type MovingWindowAvgImpl](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/aggregate#MovingWindowAvgImpl)
*       *   [func NewMovingWindowAvgImpl(windowSize time.Duration, maxBufferSize int) *MovingWindowAvgImpl](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/aggregate#NewMovingWindowAvgImpl)

*       *   [func (a *MovingWindowAvgImpl) Average() float64](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/aggregate#MovingWindowAvgImpl.Average)
    *   [func (a *MovingWindowAvgImpl) Record(val int64)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/aggregate#MovingWindowAvgImpl.Record)

### Constants [¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/aggregate#pkg-constants "Go to Constants")

This section is empty.

### Variables [¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/aggregate#pkg-variables "Go to Variables")

This section is empty.

### Functions [¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/aggregate#pkg-functions "Go to Functions")

This section is empty.

### Types [¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/aggregate#pkg-types "Go to Types")

#### type [MovingWindowAverage](https://github.com/temporalio/temporal/blob/v1.30.0/common/aggregate/moving_window_average.go#L9)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/aggregate#MovingWindowAverage "Go to MovingWindowAverage")

type MovingWindowAverage interface {
 Record(val [int64](https://pkg.go.dev/builtin#int64))  Average() [float64](https://pkg.go.dev/builtin#float64)}

var NoopMovingWindowAverage [MovingWindowAverage](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/aggregate#MovingWindowAverage) = newNoopMovingWindowAverage()

#### type [MovingWindowAvgImpl](https://github.com/temporalio/temporal/blob/v1.30.0/common/aggregate/moving_window_average.go#L19)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/aggregate#MovingWindowAvgImpl "Go to MovingWindowAvgImpl")

type MovingWindowAvgImpl struct {
[sync](https://pkg.go.dev/sync).[Mutex](https://pkg.go.dev/sync#Mutex)	// contains filtered or unexported fields
}

#### func [NewMovingWindowAvgImpl](https://github.com/temporalio/temporal/blob/v1.30.0/common/aggregate/moving_window_average.go#L31)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/aggregate#NewMovingWindowAvgImpl "Go to NewMovingWindowAvgImpl")

func NewMovingWindowAvgImpl(
	windowSize [time](https://pkg.go.dev/time).[Duration](https://pkg.go.dev/time#Duration),
	maxBufferSize [int](https://pkg.go.dev/builtin#int),
) *[MovingWindowAvgImpl](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/aggregate#MovingWindowAvgImpl)

#### func (*MovingWindowAvgImpl) [Average](https://github.com/temporalio/temporal/blob/v1.30.0/common/aggregate/moving_window_average.go#L60)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/aggregate#MovingWindowAvgImpl.Average "Go to MovingWindowAvgImpl.Average")

func (a *[MovingWindowAvgImpl](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/aggregate#MovingWindowAvgImpl)) Average() [float64](https://pkg.go.dev/builtin#float64)

#### func (*MovingWindowAvgImpl) [Record](https://github.com/temporalio/temporal/blob/v1.30.0/common/aggregate/moving_window_average.go#L42)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/aggregate#MovingWindowAvgImpl.Record "Go to MovingWindowAvgImpl.Record")

func (a *[MovingWindowAvgImpl](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/aggregate#MovingWindowAvgImpl)) Record(val [int64](https://pkg.go.dev/builtin#int64))

![Image 45](https://pkg.go.dev/static/shared/icon/insert_drive_file_gm_grey_24dp.svg) Source Files [¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/aggregate#section-sourcefiles "Go to Source Files")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[View all Source files](https://github.com/temporalio/temporal/tree/v1.30.0/common/aggregate)

*   [moving_window_average.go](https://github.com/temporalio/temporal/blob/v1.30.0/common/aggregate/moving_window_average.go "moving_window_average.go")
*   [noop_moving_window_average.go](https://github.com/temporalio/temporal/blob/v1.30.0/common/aggregate/noop_moving_window_average.go "noop_moving_window_average.go")

 Click to show internal directories. 

 Click to hide internal directories. 

[Why Go](https://go.dev/solutions)[Use Cases](https://go.dev/solutions#use-cases)[Case Studies](https://go.dev/solutions#case-studies)

[Get Started](https://learn.go.dev/)[Playground](https://play.golang.org/)[Tour](https://tour.golang.org/)[Stack Overflow](https://stackoverflow.com/questions/tagged/go?tab=Newest)[Help](https://go.dev/help)

[Packages](https://pkg.go.dev/)[Standard Library](https://pkg.go.dev/std)[Sub-repositories](https://pkg.go.dev/golang.org/x)[About Go Packages](https://pkg.go.dev/about)

[About](https://go.dev/project)[Download](https://go.dev/dl/)[Blog](https://go.dev/blog)[Issue Tracker](https://github.com/golang/go/issues)[Release Notes](https://go.dev/doc/devel/release.html)[Brand Guidelines](https://go.dev/brand)[Code of Conduct](https://go.dev/conduct)

[Connect](https://www.twitter.com/golang)[Twitter](https://www.twitter.com/golang)[GitHub](https://github.com/golang)[Slack](https://invite.slack.golangbridge.org/)[r/golang](https://reddit.com/r/golang)[Meetup](https://www.meetup.com/pro/go)[Golang Weekly](https://golangweekly.com/)

![Image 46: Gopher in flight goggles](https://pkg.go.dev/static/shared/gopher/pilot-bust-1431x901.svg)
*   [Copyright](https://go.dev/copyright)
*   [Terms of Service](https://go.dev/tos)
*   [Privacy Policy](http://www.google.com/intl/en/policies/privacy/)
*   [Report an Issue](https://go.dev/s/pkgsite-feedback)
*   ![Image 47: System theme](https://pkg.go.dev/static/shared/icon/brightness_6_gm_grey_24dp.svg)![Image 48: Dark theme](https://pkg.go.dev/static/shared/icon/brightness_2_gm_grey_24dp.svg)![Image 49: Light theme](https://pkg.go.dev/static/shared/icon/light_mode_gm_grey_24dp.svg)
Theme Toggle

*   ![Image 50](https://pkg.go.dev/static/shared/icon/keyboard_grey_24dp.svg)
Shortcuts Modal

[![Image 51: Google logo](https://pkg.go.dev/static/shared/logo/google-white.svg)](https://google.com/)

Jump to
-------

![Image 52](https://pkg.go.dev/static/shared/icon/close_gm_grey_24dp.svg)

Close

Keyboard shortcuts
------------------

![Image 53](https://pkg.go.dev/static/shared/icon/close_gm_grey_24dp.svg)

**?**: This menu
**/**: Search site
**f** or **F**: Jump to
**y** or **Y**: Canonical URL

Close

go.dev uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay
