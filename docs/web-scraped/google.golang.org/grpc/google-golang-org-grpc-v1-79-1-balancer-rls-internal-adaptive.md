# Source: https://pkg.go.dev/google.golang.org/grpc@v1.79.1/balancer/rls/internal/adaptive

Title: adaptive package - google.golang.org/grpc/balancer/rls/internal/adaptive - Go Packages

URL Source: https://pkg.go.dev/google.golang.org/grpc@v1.79.1/balancer/rls/internal/adaptive

Markdown Content:
adaptive package - google.golang.org/grpc/balancer/rls/internal/adaptive - Go Packages
===============

[![Image 1: Go](https://pkg.go.dev/static/shared/logo/go-white.svg)](https://go.dev/)

[Skip to Main Content](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/balancer/rls/internal/adaptive#main-content)

![Image 2](https://pkg.go.dev/static/shared/icon/search_gm_grey_24dp.svg)![Image 3](https://pkg.go.dev/static/shared/icon/search_gm_grey_24dp.svg)

*   [Why Go ![Image 4: submenu dropdown icon](https://pkg.go.dev/static/shared/icon/arrow_drop_down_gm_grey_24dp.svg)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/balancer/rls/internal/adaptive#)
    *   [Case Studies](https://go.dev/solutions#case-studies) 
Common problems companies solve with Go

    *   [Use Cases](https://go.dev/solutions#use-cases) 
Stories about how and why companies use Go

    *   [Security](https://go.dev/security/) 
How Go can help keep you secure by default

*   [Learn](https://go.dev/learn/)
*   [Docs ![Image 5: submenu dropdown icon](https://pkg.go.dev/static/shared/icon/arrow_drop_down_gm_grey_24dp.svg)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/balancer/rls/internal/adaptive#)
    *   [Effective Go](https://go.dev/doc/effective_go) 
Tips for writing clear, performant, and idiomatic Go code

    *   [Go User Manual](https://go.dev/doc/) 
A complete introduction to building software with Go

    *   [Standard library](https://pkg.go.dev/std) 
Reference documentation for Go's standard library

    *   [Release Notes](https://go.dev/doc/devel/release) 
Learn what's new in each Go release

*   [Packages](https://pkg.go.dev/)
*   [Community ![Image 6: submenu dropdown icon](https://pkg.go.dev/static/shared/icon/arrow_drop_down_gm_grey_24dp.svg)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/balancer/rls/internal/adaptive#)
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

*   [Why Go _![Image 16](https://pkg.go.dev/static/shared/icon/navigate\_next\_gm\_grey\_24dp.svg)_](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/balancer/rls/internal/adaptive#)

[_![Image 17](https://pkg.go.dev/static/shared/icon/navigate\_before\_gm\_grey\_24dp.svg)_ Why Go](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/balancer/rls/internal/adaptive#) 
    *   [Case Studies](https://go.dev/solutions#case-studies)
    *   [Use Cases](https://go.dev/solutions#use-cases)
    *   [Security](https://go.dev/security/)

*   [Learn](https://go.dev/learn/)
*   [Docs _![Image 18](https://pkg.go.dev/static/shared/icon/navigate\_next\_gm\_grey\_24dp.svg)_](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/balancer/rls/internal/adaptive#)

[_![Image 19](https://pkg.go.dev/static/shared/icon/navigate\_before\_gm\_grey\_24dp.svg)_ Docs](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/balancer/rls/internal/adaptive#) 
    *   [Effective Go](https://go.dev/doc/effective_go)
    *   [Go User Manual](https://go.dev/doc/)
    *   [Standard library](https://pkg.go.dev/std)
    *   [Release Notes](https://go.dev/doc/devel/release)

*   [Packages](https://pkg.go.dev/)
*   [Community _![Image 20](https://pkg.go.dev/static/shared/icon/navigate\_next\_gm\_grey\_24dp.svg)_](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/balancer/rls/internal/adaptive#)

[_![Image 21](https://pkg.go.dev/static/shared/icon/navigate\_before\_gm\_grey\_24dp.svg)_ Community](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/balancer/rls/internal/adaptive#) 
    *   [Recorded Talks](https://go.dev/talks/)
    *   [Meetups _![Image 22](https://pkg.go.dev/static/shared/icon/launch\_gm\_grey\_24dp.svg)_](https://www.meetup.com/pro/go)
    *   [Conferences _![Image 23](https://pkg.go.dev/static/shared/icon/launch\_gm\_grey\_24dp.svg)_](https://github.com/golang/go/wiki/Conferences)
    *   [Go blog](https://go.dev/blog)
    *   [Go project](https://go.dev/help)
    *   Get connected [![Image 24](https://pkg.go.dev/static/shared/logo/social/google-groups.svg)](https://groups.google.com/g/golang-nuts)[![Image 25](https://pkg.go.dev/static/shared/logo/social/github.svg)](https://github.com/golang)[![Image 26](https://pkg.go.dev/static/shared/logo/social/twitter.svg)](https://twitter.com/golang)[![Image 27](https://pkg.go.dev/static/shared/logo/social/reddit.svg)](https://www.reddit.com/r/golang/)[![Image 28](https://pkg.go.dev/static/shared/logo/social/slack.svg)](https://invite.slack.golangbridge.org/)[![Image 29](https://pkg.go.dev/static/shared/logo/social/stack-overflow.svg)](https://stackoverflow.com/collectives/go) 

1.   [Discover Packages](https://pkg.go.dev/)
2.   [google.golang.org/grpc](https://pkg.go.dev/google.golang.org/grpc@v1.79.1)
3.   [balancer](https://pkg.go.dev/google.golang.org/grpc/balancer@v1.79.1)
4.   [rls](https://pkg.go.dev/google.golang.org/grpc/balancer/rls@v1.79.1)
5.   [internal](https://pkg.go.dev/google.golang.org/grpc/balancer/rls/internal@v1.79.1)
6.   [adaptive](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/balancer/rls/internal/adaptive)![Image 30](https://pkg.go.dev/static/shared/icon/content_copy_gm_grey_24dp.svg)

[![Image 31: Go](https://pkg.go.dev/static/shared/logo/go-blue.svg)](https://go.dev/)
adaptive
========

package![Image 32](https://pkg.go.dev/static/shared/icon/content_copy_gm_grey_24dp.svg)

[Version: v1.79.1](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/balancer/rls/internal/adaptive?tab=versions)

 Opens a new window with list of versions in this module. 

Latest Latest 

![Image 33: Warning](https://pkg.go.dev/static/shared/icon/alert_gm_grey_24dp.svg)
This package is not in the latest version of its module.

[Go to latest](https://pkg.go.dev/google.golang.org/grpc/balancer/rls/internal/adaptive) Published: Feb 13, 2026  License: [Apache-2.0](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/balancer/rls/internal/adaptive?tab=licenses)

 Opens a new window with license information. 

[Imports: 3](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/balancer/rls/internal/adaptive?tab=imports)

 Opens a new window with list of imports. 

[Imported by: 0](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/balancer/rls/internal/adaptive?tab=importedby)

 Opens a new window with list of known importers. 

Details
-------

*   ![Image 34: checked](https://pkg.go.dev/static/shared/icon/check_circle_gm_grey_24dp.svg) Valid [go.mod](https://github.com/grpc/grpc-go/tree/v1.79.1/go.mod) file ![Image 35](https://pkg.go.dev/static/shared/icon/help_gm_grey_24dp.svg)
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

[github.com/grpc/grpc-go](https://github.com/grpc/grpc-go "https://github.com/grpc/grpc-go")

Links
-----

*   [![Image 42: Open Source Insights Logo](https://pkg.go.dev/static/shared/icon/depsdev-logo.svg) Open Source Insights](https://deps.dev/go/google.golang.org%2Fgrpc/v1.79.1 "View this module on Open Source Insights")

 Jump to ... 

*   [Documentation](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/balancer/rls/internal/adaptive#section-documentation)
    *   [Overview](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/balancer/rls/internal/adaptive#pkg-overview)
    *   [Index](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/balancer/rls/internal/adaptive#pkg-index)
    *   [Constants](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/balancer/rls/internal/adaptive#pkg-constants)
    *   [Variables](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/balancer/rls/internal/adaptive#pkg-variables)
    *   [Functions](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/balancer/rls/internal/adaptive#pkg-functions)
    *   [Types](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/balancer/rls/internal/adaptive#pkg-types)
        *   [type Throttler](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/balancer/rls/internal/adaptive#Throttler "type Throttler")
            *   [New()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/balancer/rls/internal/adaptive#New "New()")
            *   [(t) RegisterBackendResponse(throttled)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/balancer/rls/internal/adaptive#Throttler.RegisterBackendResponse "(t) RegisterBackendResponse(throttled)")
            *   [(t) ShouldThrottle()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/balancer/rls/internal/adaptive#Throttler.ShouldThrottle "(t) ShouldThrottle()")

*   [Source Files](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/balancer/rls/internal/adaptive#section-sourcefiles)

![Image 43](https://pkg.go.dev/static/shared/icon/code_gm_grey_24dp.svg) Documentation [¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/balancer/rls/internal/adaptive#section-documentation "Go to Documentation")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Overview [¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/balancer/rls/internal/adaptive#pkg-overview "Go to Overview")

Package adaptive provides functionality for adaptive client-side throttling.

### Index [¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/balancer/rls/internal/adaptive#pkg-index "Go to Index")

*   [type Throttler](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/balancer/rls/internal/adaptive#Throttler)
*       *   [func New() *Throttler](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/balancer/rls/internal/adaptive#New)

*       *   [func (t *Throttler) RegisterBackendResponse(throttled bool)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/balancer/rls/internal/adaptive#Throttler.RegisterBackendResponse)
    *   [func (t *Throttler) ShouldThrottle() bool](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/balancer/rls/internal/adaptive#Throttler.ShouldThrottle)

### Constants [¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/balancer/rls/internal/adaptive#pkg-constants "Go to Constants")

This section is empty.

### Variables [¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/balancer/rls/internal/adaptive#pkg-variables "Go to Variables")

This section is empty.

### Functions [¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/balancer/rls/internal/adaptive#pkg-functions "Go to Functions")

This section is empty.

### Types [¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/balancer/rls/internal/adaptive#pkg-types "Go to Types")

#### type [Throttler](https://github.com/grpc/grpc-go/blob/v1.79.1/balancer/rls/internal/adaptive/adaptive.go#L69)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/balancer/rls/internal/adaptive#Throttler "Go to Throttler")

type Throttler struct {
	// contains filtered or unexported fields
}

Throttler implements a client-side throttling recommendation system. All methods are safe for concurrent use by multiple goroutines.

The throttler has the following knobs for which we will use defaults for now. If there is a need to make them configurable at a later point in time, support for the same will be added.

*   Duration: amount of recent history that will be taken into account for making client-side throttling decisions. A default of 30 seconds is used.
*   Bins: number of bins to be used for bucketing historical data. A default of 100 is used.
*   RatioForAccepts: ratio by which accepts are multiplied, typically a value slightly larger than 1.0. This is used to make the throttler behave as if the backend had accepted more requests than it actually has, which lets us err on the side of sending to the backend more requests than we think it will accept for the sake of speeding up the propagation of state. A default of 2.0 is used.
*   RequestsPadding: is used to decrease the (client-side) throttling probability in the low QPS regime (to speed up propagation of state), as well as to safeguard against hitting a client-side throttling probability of 100%. The weight of this value decreases as the number of requests in recent history grows. A default of 8 is used.

The adaptive throttler attempts to estimate the probability that a request will be throttled using recent history. Server requests (both throttled and accepted) are registered with the throttler (via the RegisterBackendResponse method), which then recommends client-side throttling (via the ShouldThrottle method) with probability given by: (requests - RatioForAccepts * accepts) / (requests + RequestsPadding)

#### func [New](https://github.com/grpc/grpc-go/blob/v1.79.1/balancer/rls/internal/adaptive/adaptive.go#L80)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/balancer/rls/internal/adaptive#New "Go to New")

func New() *[Throttler](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/balancer/rls/internal/adaptive#Throttler)

New initializes a new adaptive throttler with the default values.

#### func (*Throttler) [RegisterBackendResponse](https://github.com/grpc/grpc-go/blob/v1.79.1/balancer/rls/internal/adaptive/adaptive.go#L121)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/balancer/rls/internal/adaptive#Throttler.RegisterBackendResponse "Go to Throttler.RegisterBackendResponse")

func (t *[Throttler](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/balancer/rls/internal/adaptive#Throttler)) RegisterBackendResponse(throttled [bool](https://pkg.go.dev/builtin#bool))

RegisterBackendResponse registers a response received from the backend for a request allowed by ShouldThrottle. This should be called for every response received from the backend (i.e., once for each request for which ShouldThrottle returned false).

#### func (*Throttler) [ShouldThrottle](https://github.com/grpc/grpc-go/blob/v1.79.1/balancer/rls/internal/adaptive/adaptive.go#L99)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/balancer/rls/internal/adaptive#Throttler.ShouldThrottle "Go to Throttler.ShouldThrottle")

func (t *[Throttler](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/balancer/rls/internal/adaptive#Throttler)) ShouldThrottle() [bool](https://pkg.go.dev/builtin#bool)

ShouldThrottle returns a probabilistic estimate of whether the server would throttle the next request. This should be called for every request before allowing it to hit the network. If the returned value is true, the request should be aborted immediately (as if it had been throttled by the server).

![Image 44](https://pkg.go.dev/static/shared/icon/insert_drive_file_gm_grey_24dp.svg) Source Files [¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/balancer/rls/internal/adaptive#section-sourcefiles "Go to Source Files")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[View all Source files](https://github.com/grpc/grpc-go/tree/v1.79.1/balancer/rls/internal/adaptive)

*   [adaptive.go](https://github.com/grpc/grpc-go/blob/v1.79.1/balancer/rls/internal/adaptive/adaptive.go "adaptive.go")
*   [lookback.go](https://github.com/grpc/grpc-go/blob/v1.79.1/balancer/rls/internal/adaptive/lookback.go "lookback.go")

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
