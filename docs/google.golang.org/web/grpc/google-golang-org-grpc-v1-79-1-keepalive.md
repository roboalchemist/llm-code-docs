# Source: https://pkg.go.dev/google.golang.org/grpc@v1.79.1/keepalive

Title: keepalive package - google.golang.org/grpc/keepalive - Go Packages

URL Source: https://pkg.go.dev/google.golang.org/grpc@v1.79.1/keepalive

Markdown Content:
keepalive package - google.golang.org/grpc/keepalive - Go Packages
===============

[![Image 2: Go](https://pkg.go.dev/static/shared/logo/go-white.svg)](https://go.dev/)

[Skip to Main Content](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/keepalive#main-content)

![Image 3](https://pkg.go.dev/static/shared/icon/search_gm_grey_24dp.svg)![Image 4](https://pkg.go.dev/static/shared/icon/search_gm_grey_24dp.svg)

*   [Why Go ![Image 5: submenu dropdown icon](https://pkg.go.dev/static/shared/icon/arrow_drop_down_gm_grey_24dp.svg)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/keepalive#)
    *   [Case Studies](https://go.dev/solutions#case-studies) 
Common problems companies solve with Go

    *   [Use Cases](https://go.dev/solutions#use-cases) 
Stories about how and why companies use Go

    *   [Security](https://go.dev/security/) 
How Go can help keep you secure by default

*   [Learn](https://go.dev/learn/)
*   [Docs ![Image 6: submenu dropdown icon](https://pkg.go.dev/static/shared/icon/arrow_drop_down_gm_grey_24dp.svg)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/keepalive#)
    *   [Effective Go](https://go.dev/doc/effective_go) 
Tips for writing clear, performant, and idiomatic Go code

    *   [Go User Manual](https://go.dev/doc/) 
A complete introduction to building software with Go

    *   [Standard library](https://pkg.go.dev/std) 
Reference documentation for Go's standard library

    *   [Release Notes](https://go.dev/doc/devel/release) 
Learn what's new in each Go release

*   [Packages](https://pkg.go.dev/)
*   [Community ![Image 7: submenu dropdown icon](https://pkg.go.dev/static/shared/icon/arrow_drop_down_gm_grey_24dp.svg)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/keepalive#)
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

*   [Why Go _![Image 17](https://pkg.go.dev/static/shared/icon/navigate\_next\_gm\_grey\_24dp.svg)_](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/keepalive#)

[_![Image 18](https://pkg.go.dev/static/shared/icon/navigate\_before\_gm\_grey\_24dp.svg)_ Why Go](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/keepalive#) 
    *   [Case Studies](https://go.dev/solutions#case-studies)
    *   [Use Cases](https://go.dev/solutions#use-cases)
    *   [Security](https://go.dev/security/)

*   [Learn](https://go.dev/learn/)
*   [Docs _![Image 19](https://pkg.go.dev/static/shared/icon/navigate\_next\_gm\_grey\_24dp.svg)_](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/keepalive#)

[_![Image 20](https://pkg.go.dev/static/shared/icon/navigate\_before\_gm\_grey\_24dp.svg)_ Docs](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/keepalive#) 
    *   [Effective Go](https://go.dev/doc/effective_go)
    *   [Go User Manual](https://go.dev/doc/)
    *   [Standard library](https://pkg.go.dev/std)
    *   [Release Notes](https://go.dev/doc/devel/release)

*   [Packages](https://pkg.go.dev/)
*   [Community _![Image 21](https://pkg.go.dev/static/shared/icon/navigate\_next\_gm\_grey\_24dp.svg)_](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/keepalive#)

[_![Image 22](https://pkg.go.dev/static/shared/icon/navigate\_before\_gm\_grey\_24dp.svg)_ Community](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/keepalive#) 
    *   [Recorded Talks](https://go.dev/talks/)
    *   [Meetups _![Image 23](https://pkg.go.dev/static/shared/icon/launch\_gm\_grey\_24dp.svg)_](https://www.meetup.com/pro/go)
    *   [Conferences _![Image 24](https://pkg.go.dev/static/shared/icon/launch\_gm\_grey\_24dp.svg)_](https://github.com/golang/go/wiki/Conferences)
    *   [Go blog](https://go.dev/blog)
    *   [Go project](https://go.dev/help)
    *   Get connected [![Image 25](https://pkg.go.dev/static/shared/logo/social/google-groups.svg)](https://groups.google.com/g/golang-nuts)[![Image 26](https://pkg.go.dev/static/shared/logo/social/github.svg)](https://github.com/golang)[![Image 27](https://pkg.go.dev/static/shared/logo/social/twitter.svg)](https://twitter.com/golang)[![Image 28](https://pkg.go.dev/static/shared/logo/social/reddit.svg)](https://www.reddit.com/r/golang/)[![Image 29](https://pkg.go.dev/static/shared/logo/social/slack.svg)](https://invite.slack.golangbridge.org/)[![Image 30](https://pkg.go.dev/static/shared/logo/social/stack-overflow.svg)](https://stackoverflow.com/collectives/go) 

1.   [Discover Packages](https://pkg.go.dev/)
2.   [google.golang.org/grpc](https://pkg.go.dev/google.golang.org/grpc@v1.79.1)
3.   [keepalive](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/keepalive)![Image 31](https://pkg.go.dev/static/shared/icon/content_copy_gm_grey_24dp.svg)

[![Image 32: Go](https://pkg.go.dev/static/shared/logo/go-blue.svg)](https://go.dev/)
keepalive
=========

package![Image 33](https://pkg.go.dev/static/shared/icon/content_copy_gm_grey_24dp.svg)

[Version: v1.79.1](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/keepalive?tab=versions)

 Opens a new window with list of versions in this module. 

Latest Latest 

![Image 34: Warning](https://pkg.go.dev/static/shared/icon/alert_gm_grey_24dp.svg)
This package is not in the latest version of its module.

[Go to latest](https://pkg.go.dev/google.golang.org/grpc/keepalive) Published: Feb 13, 2026  License: [Apache-2.0](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/keepalive?tab=licenses)

 Opens a new window with license information. 

[Imports: 1](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/keepalive?tab=imports)

 Opens a new window with list of imports. 

[Imported by: 5,352](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/keepalive?tab=importedby)

 Opens a new window with list of known importers. 

Details
-------

*   ![Image 35: checked](https://pkg.go.dev/static/shared/icon/check_circle_gm_grey_24dp.svg) Valid [go.mod](https://github.com/grpc/grpc-go/tree/v1.79.1/go.mod) file ![Image 36](https://pkg.go.dev/static/shared/icon/help_gm_grey_24dp.svg)
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

[github.com/grpc/grpc-go](https://github.com/grpc/grpc-go "https://github.com/grpc/grpc-go")

Links
-----

*   [![Image 43: Open Source Insights Logo](https://pkg.go.dev/static/shared/icon/depsdev-logo.svg) Open Source Insights](https://deps.dev/go/google.golang.org%2Fgrpc/v1.79.1 "View this module on Open Source Insights")

 Jump to ... 

*   [Documentation](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/keepalive#section-documentation)
    *   [Overview](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/keepalive#pkg-overview)
    *   [Index](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/keepalive#pkg-index)
    *   [Constants](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/keepalive#pkg-constants)
    *   [Variables](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/keepalive#pkg-variables)
    *   [Functions](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/keepalive#pkg-functions)
    *   [Types](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/keepalive#pkg-types)
        *   [type ClientParameters](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/keepalive#ClientParameters "type ClientParameters")
        *   [type EnforcementPolicy](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/keepalive#EnforcementPolicy "type EnforcementPolicy")
        *   [type ServerParameters](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/keepalive#ServerParameters "type ServerParameters")

*   [Source Files](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/keepalive#section-sourcefiles)

![Image 44](https://pkg.go.dev/static/shared/icon/code_gm_grey_24dp.svg) Documentation [¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/keepalive#section-documentation "Go to Documentation")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Overview [¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/keepalive#pkg-overview "Go to Overview")

Package keepalive defines configurable parameters for point-to-point healthcheck.

### Index [¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/keepalive#pkg-index "Go to Index")

*   [type ClientParameters](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/keepalive#ClientParameters)
*   [type EnforcementPolicy](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/keepalive#EnforcementPolicy)
*   [type ServerParameters](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/keepalive#ServerParameters)

### Constants [¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/keepalive#pkg-constants "Go to Constants")

This section is empty.

### Variables [¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/keepalive#pkg-variables "Go to Variables")

This section is empty.

### Functions [¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/keepalive#pkg-functions "Go to Functions")

This section is empty.

### Types [¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/keepalive#pkg-types "Go to Types")

#### type [ClientParameters](https://github.com/grpc/grpc-go/blob/v1.79.1/keepalive/keepalive.go#L33)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/keepalive#ClientParameters "Go to ClientParameters")

type ClientParameters struct {
// After a duration of this time if the client doesn't see any activity it	// pings the server to see if the transport is still alive.
	// If set below 10s, a minimum value of 10s will be used instead.
	//
	// Note that gRPC servers have a default EnforcementPolicy.MinTime of 5
	// minutes (which means the client shouldn't ping more frequently than every
	// 5 minutes).
	//
	// Though not ideal, it's not a strong requirement for Time to be less than
	// EnforcementPolicy.MinTime. Time will automatically double if the server
	// disconnects due to its enforcement policy.
	//
	// For more details, see
	// [https://github.com/grpc/proposal/blob/master/A8-client-side-keepalive.md](https://github.com/grpc/proposal/blob/master/A8-client-side-keepalive.md)
	Time [time](https://pkg.go.dev/time).[Duration](https://pkg.go.dev/time#Duration)
// After having pinged for keepalive check, the client waits for a duration	// of Timeout and if no activity is seen even after that the connection is
	// closed.
	//
	// If keepalive is enabled, and this value is not explicitly set, the default
	// is 20 seconds.
	Timeout [time](https://pkg.go.dev/time).[Duration](https://pkg.go.dev/time#Duration)
// If true, client sends keepalive pings even with no active RPCs. If false,	// when there are no active RPCs, Time and Timeout will be ignored and no
	// keepalive pings will be sent.
	PermitWithoutStream [bool](https://pkg.go.dev/builtin#bool)
}

ClientParameters is used to set keepalive parameters on the client-side. These configure how the client will actively probe to notice when a connection is broken and send pings so intermediaries will be aware of the liveness of the connection. Make sure these parameters are set in coordination with the keepalive policy on the server, as incompatible settings can result in closing of connection.

#### type [EnforcementPolicy](https://github.com/grpc/grpc-go/blob/v1.79.1/keepalive/keepalive.go#L91)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/keepalive#EnforcementPolicy "Go to EnforcementPolicy")added in v1.3.0

type EnforcementPolicy struct {
// MinTime is the minimum amount of time a client should wait before sending	// a keepalive ping.
	MinTime [time](https://pkg.go.dev/time).[Duration](https://pkg.go.dev/time#Duration) // The current default value is 5 minutes.
// If true, server allows keepalive pings even when there are no active	// streams(RPCs). If false, and client sends ping when there are no active
	// streams, server will send GOAWAY and close the connection.
	PermitWithoutStream [bool](https://pkg.go.dev/builtin#bool) // false by default.
}

EnforcementPolicy is used to set keepalive enforcement policy on the server-side. Server will close connection with a client that violates this policy.

#### type [ServerParameters](https://github.com/grpc/grpc-go/blob/v1.79.1/keepalive/keepalive.go#L64)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/keepalive#ServerParameters "Go to ServerParameters")added in v1.3.0

type ServerParameters struct {
// MaxConnectionIdle is a duration for the amount of time after which an	// idle connection would be closed by sending a GoAway. Idleness duration is
	// defined since the most recent time the number of outstanding RPCs became
	// zero or the connection establishment.
	MaxConnectionIdle [time](https://pkg.go.dev/time).[Duration](https://pkg.go.dev/time#Duration) // The current default value is infinity.
// MaxConnectionAge is a duration for the maximum amount of time a	// connection may exist before it will be closed by sending a GoAway. A
	// random jitter of +/-10% will be added to MaxConnectionAge to spread out
	// connection storms.
	MaxConnectionAge [time](https://pkg.go.dev/time).[Duration](https://pkg.go.dev/time#Duration) // The current default value is infinity.
// MaxConnectionAgeGrace is an additive period after MaxConnectionAge after	// which the connection will be forcibly closed.
	MaxConnectionAgeGrace [time](https://pkg.go.dev/time).[Duration](https://pkg.go.dev/time#Duration) // The current default value is infinity.
// After a duration of this time if the server doesn't see any activity it	// pings the client to see if the transport is still alive.
	// If set below 1s, a minimum value of 1s will be used instead.
	Time [time](https://pkg.go.dev/time).[Duration](https://pkg.go.dev/time#Duration) // The current default value is 2 hours.
// After having pinged for keepalive check, the server waits for a duration	// of Timeout and if no activity is seen even after that the connection is
	// closed.
	Timeout [time](https://pkg.go.dev/time).[Duration](https://pkg.go.dev/time#Duration) // The current default value is 20 seconds.
}

ServerParameters is used to set keepalive and max-age parameters on the server-side.

![Image 45](https://pkg.go.dev/static/shared/icon/insert_drive_file_gm_grey_24dp.svg) Source Files [¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/keepalive#section-sourcefiles "Go to Source Files")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[View all Source files](https://github.com/grpc/grpc-go/tree/v1.79.1/keepalive)

*   [keepalive.go](https://github.com/grpc/grpc-go/blob/v1.79.1/keepalive/keepalive.go "keepalive.go")

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
