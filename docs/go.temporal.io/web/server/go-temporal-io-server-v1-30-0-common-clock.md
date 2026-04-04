# Source: https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock

Title: clock package - go.temporal.io/server/common/clock - Go Packages

URL Source: https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock

Markdown Content:
clock package - go.temporal.io/server/common/clock - Go Packages
===============

[![Image 1: Go](https://pkg.go.dev/static/shared/logo/go-white.svg)](https://go.dev/)

[Skip to Main Content](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#main-content)

![Image 2](https://pkg.go.dev/static/shared/icon/search_gm_grey_24dp.svg)![Image 3](https://pkg.go.dev/static/shared/icon/search_gm_grey_24dp.svg)

*   [Why Go ![Image 4: submenu dropdown icon](https://pkg.go.dev/static/shared/icon/arrow_drop_down_gm_grey_24dp.svg)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#)
    *   [Case Studies](https://go.dev/solutions#case-studies) 
Common problems companies solve with Go

    *   [Use Cases](https://go.dev/solutions#use-cases) 
Stories about how and why companies use Go

    *   [Security](https://go.dev/security/) 
How Go can help keep you secure by default

*   [Learn](https://go.dev/learn/)
*   [Docs ![Image 5: submenu dropdown icon](https://pkg.go.dev/static/shared/icon/arrow_drop_down_gm_grey_24dp.svg)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#)
    *   [Effective Go](https://go.dev/doc/effective_go) 
Tips for writing clear, performant, and idiomatic Go code

    *   [Go User Manual](https://go.dev/doc/) 
A complete introduction to building software with Go

    *   [Standard library](https://pkg.go.dev/std) 
Reference documentation for Go's standard library

    *   [Release Notes](https://go.dev/doc/devel/release) 
Learn what's new in each Go release

*   [Packages](https://pkg.go.dev/)
*   [Community ![Image 6: submenu dropdown icon](https://pkg.go.dev/static/shared/icon/arrow_drop_down_gm_grey_24dp.svg)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#)
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

*   [Why Go _![Image 16](https://pkg.go.dev/static/shared/icon/navigate\_next\_gm\_grey\_24dp.svg)_](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#)

[_![Image 17](https://pkg.go.dev/static/shared/icon/navigate\_before\_gm\_grey\_24dp.svg)_ Why Go](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#) 
    *   [Case Studies](https://go.dev/solutions#case-studies)
    *   [Use Cases](https://go.dev/solutions#use-cases)
    *   [Security](https://go.dev/security/)

*   [Learn](https://go.dev/learn/)
*   [Docs _![Image 18](https://pkg.go.dev/static/shared/icon/navigate\_next\_gm\_grey\_24dp.svg)_](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#)

[_![Image 19](https://pkg.go.dev/static/shared/icon/navigate\_before\_gm\_grey\_24dp.svg)_ Docs](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#) 
    *   [Effective Go](https://go.dev/doc/effective_go)
    *   [Go User Manual](https://go.dev/doc/)
    *   [Standard library](https://pkg.go.dev/std)
    *   [Release Notes](https://go.dev/doc/devel/release)

*   [Packages](https://pkg.go.dev/)
*   [Community _![Image 20](https://pkg.go.dev/static/shared/icon/navigate\_next\_gm\_grey\_24dp.svg)_](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#)

[_![Image 21](https://pkg.go.dev/static/shared/icon/navigate\_before\_gm\_grey\_24dp.svg)_ Community](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#) 
    *   [Recorded Talks](https://go.dev/talks/)
    *   [Meetups _![Image 22](https://pkg.go.dev/static/shared/icon/launch\_gm\_grey\_24dp.svg)_](https://www.meetup.com/pro/go)
    *   [Conferences _![Image 23](https://pkg.go.dev/static/shared/icon/launch\_gm\_grey\_24dp.svg)_](https://github.com/golang/go/wiki/Conferences)
    *   [Go blog](https://go.dev/blog)
    *   [Go project](https://go.dev/help)
    *   Get connected [![Image 24](https://pkg.go.dev/static/shared/logo/social/google-groups.svg)](https://groups.google.com/g/golang-nuts)[![Image 25](https://pkg.go.dev/static/shared/logo/social/github.svg)](https://github.com/golang)[![Image 26](https://pkg.go.dev/static/shared/logo/social/twitter.svg)](https://twitter.com/golang)[![Image 27](https://pkg.go.dev/static/shared/logo/social/reddit.svg)](https://www.reddit.com/r/golang/)[![Image 28](https://pkg.go.dev/static/shared/logo/social/slack.svg)](https://invite.slack.golangbridge.org/)[![Image 29](https://pkg.go.dev/static/shared/logo/social/stack-overflow.svg)](https://stackoverflow.com/collectives/go) 

1.   [Discover Packages](https://pkg.go.dev/)
2.   [go.temporal.io/server](https://pkg.go.dev/go.temporal.io/server@v1.30.0)
3.   [common](https://pkg.go.dev/go.temporal.io/server/common@v1.30.0)
4.   [clock](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock)![Image 30](https://pkg.go.dev/static/shared/icon/content_copy_gm_grey_24dp.svg)

[![Image 31: Go](https://pkg.go.dev/static/shared/logo/go-blue.svg)](https://go.dev/)
clock
=====

package![Image 32](https://pkg.go.dev/static/shared/icon/content_copy_gm_grey_24dp.svg)

[Version: v1.30.0](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock?tab=versions)

 Opens a new window with list of versions in this module. 

Latest Latest 

![Image 33: Warning](https://pkg.go.dev/static/shared/icon/alert_gm_grey_24dp.svg)
This package is not in the latest version of its module.

[Go to latest](https://pkg.go.dev/go.temporal.io/server/common/clock) Published: Feb 4, 2026  License: [MIT](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock?tab=licenses)

 Opens a new window with license information. 

[Imports: 4](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock?tab=imports)

 Opens a new window with list of imports. 

[Imported by: 2](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock?tab=importedby)

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

*   [Documentation](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#section-documentation)
    *   [Overview](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#pkg-overview)
    *   [Index](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#pkg-index)
    *   [Examples](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#pkg-examples)
        *   [EventTimeSource](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#example-EventTimeSource "EventTimeSource")

    *   [Constants](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#pkg-constants)
    *   [Variables](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#pkg-variables)
    *   [Functions](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#pkg-functions)
        *   [ContextWithDeadline(ctx, deadline, timeSource)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#ContextWithDeadline "ContextWithDeadline(ctx, deadline, timeSource)")
        *   [ContextWithTimeout(ctx, timeout, timeSource)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#ContextWithTimeout "ContextWithTimeout(ctx, timeout, timeSource)")

    *   [Types](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#pkg-types)
        *   [type EventTimeSource](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#EventTimeSource "type EventTimeSource")
            *   [NewEventTimeSource()](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#NewEventTimeSource "NewEventTimeSource()")
            *   [(ts) Advance(d)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#EventTimeSource.Advance "(ts) Advance(d)")
            *   [(ts) AdvanceNext()](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#EventTimeSource.AdvanceNext "(ts) AdvanceNext()")
            *   [(ts) AfterFunc(d, f)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#EventTimeSource.AfterFunc "(ts) AfterFunc(d, f)")
            *   [(ts) NewTimer(d)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#EventTimeSource.NewTimer "(ts) NewTimer(d)")
            *   [(ts) Now()](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#EventTimeSource.Now "(ts) Now()")
            *   [(ts) NumTimers()](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#EventTimeSource.NumTimers "(ts) NumTimers()")
            *   [(ts) Since(t)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#EventTimeSource.Since "(ts) Since(t)")
            *   [(ts) Sleep(d)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#EventTimeSource.Sleep "(ts) Sleep(d)")
            *   [(ts) Update(now)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#EventTimeSource.Update "(ts) Update(now)")
            *   [(ts) UseAsyncTimers(async)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#EventTimeSource.UseAsyncTimers "(ts) UseAsyncTimers(async)")

        *   [type RealTimeSource](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#RealTimeSource "type RealTimeSource")
            *   [NewRealTimeSource()](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#NewRealTimeSource "NewRealTimeSource()")
            *   [(ts) AfterFunc(d, f)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#RealTimeSource.AfterFunc "(ts) AfterFunc(d, f)")
            *   [(ts) NewTimer(d)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#RealTimeSource.NewTimer "(ts) NewTimer(d)")
            *   [(ts) Now()](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#RealTimeSource.Now "(ts) Now()")
            *   [(ts) Since(t)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#RealTimeSource.Since "(ts) Since(t)")

        *   [type TimeSource](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#TimeSource "type TimeSource")
        *   [type Timer](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#Timer "type Timer")

*   [Source Files](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#section-sourcefiles)
*   [Directories](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#section-directories)

![Image 43](https://pkg.go.dev/static/shared/icon/code_gm_grey_24dp.svg) Documentation [¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#section-documentation "Go to Documentation")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Overview [¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#pkg-overview "Go to Overview")

Package clock provides extensions to the [time](https://pkg.go.dev/time) package.

### Index [¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#pkg-index "Go to Index")

*   [func ContextWithDeadline(ctx context.Context, deadline time.Time, timeSource TimeSource) (context.Context, context.CancelFunc)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#ContextWithDeadline)
*   [func ContextWithTimeout(ctx context.Context, timeout time.Duration, timeSource TimeSource) (context.Context, context.CancelFunc)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#ContextWithTimeout)
*   [type EventTimeSource](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#EventTimeSource)
*       *   [func NewEventTimeSource() *EventTimeSource](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#NewEventTimeSource)

*       *   [func (ts *EventTimeSource) Advance(d time.Duration)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#EventTimeSource.Advance)
    *   [func (ts *EventTimeSource) AdvanceNext()](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#EventTimeSource.AdvanceNext)
    *   [func (ts *EventTimeSource) AfterFunc(d time.Duration, f func()) Timer](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#EventTimeSource.AfterFunc)
    *   [func (ts *EventTimeSource) NewTimer(d time.Duration) (<-chan time.Time, Timer)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#EventTimeSource.NewTimer)
    *   [func (ts *EventTimeSource) Now() time.Time](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#EventTimeSource.Now)
    *   [func (ts *EventTimeSource) NumTimers() int](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#EventTimeSource.NumTimers)
    *   [func (ts *EventTimeSource) Since(t time.Time) time.Duration](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#EventTimeSource.Since)
    *   [func (ts *EventTimeSource) Sleep(d time.Duration)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#EventTimeSource.Sleep)
    *   [func (ts *EventTimeSource) Update(now time.Time) *EventTimeSource](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#EventTimeSource.Update)
    *   [func (ts *EventTimeSource) UseAsyncTimers(async bool)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#EventTimeSource.UseAsyncTimers)

*   [type RealTimeSource](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#RealTimeSource)
*       *   [func NewRealTimeSource() RealTimeSource](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#NewRealTimeSource)

*       *   [func (ts RealTimeSource) AfterFunc(d time.Duration, f func()) Timer](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#RealTimeSource.AfterFunc)
    *   [func (ts RealTimeSource) NewTimer(d time.Duration) (<-chan time.Time, Timer)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#RealTimeSource.NewTimer)
    *   [func (ts RealTimeSource) Now() time.Time](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#RealTimeSource.Now)
    *   [func (ts RealTimeSource) Since(t time.Time) time.Duration](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#RealTimeSource.Since)

*   [type TimeSource](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#TimeSource)
*   [type Timer](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#Timer)

### Examples [¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#pkg-examples "Go to Examples")

*   [EventTimeSource](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#example-EventTimeSource)

### Constants [¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#pkg-constants "Go to Constants")

This section is empty.

### Variables [¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#pkg-variables "Go to Variables")

This section is empty.

### Functions [¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#pkg-functions "Go to Functions")

#### func [ContextWithDeadline](https://github.com/temporalio/temporal/blob/v1.30.0/common/clock/context.go#L53)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#ContextWithDeadline "Go to ContextWithDeadline")added in v1.23.0

func ContextWithDeadline(
	ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context),
	deadline [time](https://pkg.go.dev/time).[Time](https://pkg.go.dev/time#Time),
	timeSource [TimeSource](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#TimeSource),
) ([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), [context](https://pkg.go.dev/context).[CancelFunc](https://pkg.go.dev/context#CancelFunc))

#### func [ContextWithTimeout](https://github.com/temporalio/temporal/blob/v1.30.0/common/clock/context.go#L68)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#ContextWithTimeout "Go to ContextWithTimeout")added in v1.23.0

func ContextWithTimeout(
	ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context),
	timeout [time](https://pkg.go.dev/time).[Duration](https://pkg.go.dev/time#Duration),
	timeSource [TimeSource](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#TimeSource),
) ([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), [context](https://pkg.go.dev/context).[CancelFunc](https://pkg.go.dev/context#CancelFunc))

### Types [¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#pkg-types "Go to Types")

#### type [EventTimeSource](https://github.com/temporalio/temporal/blob/v1.30.0/common/clock/event_time_source.go#L14)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#EventTimeSource "Go to EventTimeSource")

type EventTimeSource struct {
	// contains filtered or unexported fields
}

EventTimeSource is a fake TimeSource. Unlike other fake clock implementations, the methods are synchronous, so when you call Advance or Update, all triggered timers from AfterFunc will fire before the method returns, in the same goroutine.

Example [¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#example-EventTimeSource "Go to Example")

package main

import (
	"fmt"
	"time"

	"go.temporal.io/server/common/clock"
)

func main() {
	// Create a new fake timeSource.
	source := clock.NewEventTimeSource()

	// Create a timer which fires after 1 second.
	source.AfterFunc(time.Second, func() {
		fmt.Println("timer fired")
	})

	// Advance the time source by 1 second.
	fmt.Println("advancing time source by 1 second")
	source.Advance(time.Second)
	fmt.Println("time source advanced")

}
Output:

advancing time source by 1 second timer fired time source advanced 

Share Format Run

#### func [NewEventTimeSource](https://github.com/temporalio/temporal/blob/v1.30.0/common/clock/event_time_source.go#L41)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#NewEventTimeSource "Go to NewEventTimeSource")

func NewEventTimeSource() *[EventTimeSource](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#EventTimeSource)

NewEventTimeSource returns a EventTimeSource with the current time set to Unix zero: 1970-01-01 00:00:00 +0000 UTC.

#### func (*EventTimeSource) [Advance](https://github.com/temporalio/temporal/blob/v1.30.0/common/clock/event_time_source.go#L118)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#EventTimeSource.Advance "Go to EventTimeSource.Advance")added in v1.22.0

func (ts *[EventTimeSource](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#EventTimeSource)) Advance(d [time](https://pkg.go.dev/time).[Duration](https://pkg.go.dev/time#Duration))

Advance the timer by the specified duration.

#### func (*EventTimeSource) [AdvanceNext](https://github.com/temporalio/temporal/blob/v1.30.0/common/clock/event_time_source.go#L127)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#EventTimeSource.AdvanceNext "Go to EventTimeSource.AdvanceNext")added in v1.27.0

func (ts *[EventTimeSource](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#EventTimeSource)) AdvanceNext()

AdvanceNext advances to the next timer.

#### func (*EventTimeSource) [AfterFunc](https://github.com/temporalio/temporal/blob/v1.30.0/common/clock/event_time_source.go#L73)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#EventTimeSource.AfterFunc "Go to EventTimeSource.AfterFunc")added in v1.22.0

func (ts *[EventTimeSource](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#EventTimeSource)) AfterFunc(d [time](https://pkg.go.dev/time).[Duration](https://pkg.go.dev/time#Duration), f func()) [Timer](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#Timer)

AfterFunc return a timer that will fire after the specified duration. It is important to note that the timeSource is locked while the callback is called. This means that you must be cautious about calling any other mutating methods on the timeSource from within the callback. Doing so will probably result in a deadlock. To avoid this, you may want to wrap all such calls in a goroutine. If the duration is non-positive, the callback will fire immediately before AfterFunc returns.

#### func (*EventTimeSource) [NewTimer](https://github.com/temporalio/temporal/blob/v1.30.0/common/clock/event_time_source.go#L84)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#EventTimeSource.NewTimer "Go to EventTimeSource.NewTimer")added in v1.25.0

func (ts *[EventTimeSource](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#EventTimeSource)) NewTimer(d [time](https://pkg.go.dev/time).[Duration](https://pkg.go.dev/time#Duration)) (<-chan [time](https://pkg.go.dev/time).[Time](https://pkg.go.dev/time#Time), [Timer](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#Timer))

NewTimer creates a Timer that will send the current time on a channel after at least duration d. It returns the channel and the Timer.

#### func (*EventTimeSource) [Now](https://github.com/temporalio/temporal/blob/v1.30.0/common/clock/event_time_source.go#L57)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#EventTimeSource.Now "Go to EventTimeSource.Now")

func (ts *[EventTimeSource](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#EventTimeSource)) Now() [time](https://pkg.go.dev/time).[Time](https://pkg.go.dev/time#Time)

Now return the current time.

#### func (*EventTimeSource) [NumTimers](https://github.com/temporalio/temporal/blob/v1.30.0/common/clock/event_time_source.go#L144)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#EventTimeSource.NumTimers "Go to EventTimeSource.NumTimers")added in v1.25.0

func (ts *[EventTimeSource](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#EventTimeSource)) NumTimers() [int](https://pkg.go.dev/builtin#int)

NumTimers returns the number of outstanding timers.

#### func (*EventTimeSource) [Since](https://github.com/temporalio/temporal/blob/v1.30.0/common/clock/event_time_source.go#L64)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#EventTimeSource.Since "Go to EventTimeSource.Since")added in v1.25.0

func (ts *[EventTimeSource](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#EventTimeSource)) Since(t [time](https://pkg.go.dev/time).[Time](https://pkg.go.dev/time#Time)) [time](https://pkg.go.dev/time).[Duration](https://pkg.go.dev/time#Duration)

#### func (*EventTimeSource) [Sleep](https://github.com/temporalio/temporal/blob/v1.30.0/common/clock/event_time_source.go#L152)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#EventTimeSource.Sleep "Go to EventTimeSource.Sleep")added in v1.27.0

func (ts *[EventTimeSource](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#EventTimeSource)) Sleep(d [time](https://pkg.go.dev/time).[Duration](https://pkg.go.dev/time#Duration))

Sleep is a convenience function for waiting on a new timer.

#### func (*EventTimeSource) [Update](https://github.com/temporalio/temporal/blob/v1.30.0/common/clock/event_time_source.go#L108)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#EventTimeSource.Update "Go to EventTimeSource.Update")

func (ts *[EventTimeSource](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#EventTimeSource)) Update(now [time](https://pkg.go.dev/time).[Time](https://pkg.go.dev/time#Time)) *[EventTimeSource](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#EventTimeSource)

Update the fake current time. It returns the timeSource so that you can chain calls like this: timeSource := NewEventTimeSource().Update(time.Now())

#### func (*EventTimeSource) [UseAsyncTimers](https://github.com/temporalio/temporal/blob/v1.30.0/common/clock/event_time_source.go#L49)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#EventTimeSource.UseAsyncTimers "Go to EventTimeSource.UseAsyncTimers")added in v1.28.0

func (ts *[EventTimeSource](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#EventTimeSource)) UseAsyncTimers(async [bool](https://pkg.go.dev/builtin#bool))

Some clients depend on the fact that the runtime's timers do _not_ run synchronously. If UseAsyncTimers(true) is called, then EventTimeSource will behave that way also.

#### type [RealTimeSource](https://github.com/temporalio/temporal/blob/v1.30.0/common/clock/time_source.go#L27)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#RealTimeSource "Go to RealTimeSource")

type RealTimeSource struct{}

RealTimeSource is a timeSource that uses the real wall timeSource time. The zero value is valid.

#### func [NewRealTimeSource](https://github.com/temporalio/temporal/blob/v1.30.0/common/clock/time_source.go#L33)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#NewRealTimeSource "Go to NewRealTimeSource")

func NewRealTimeSource() [RealTimeSource](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#RealTimeSource)

NewRealTimeSource returns a timeSource that uses the real wall timeSource time.

#### func (RealTimeSource) [AfterFunc](https://github.com/temporalio/temporal/blob/v1.30.0/common/clock/time_source.go#L48)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#RealTimeSource.AfterFunc "Go to RealTimeSource.AfterFunc")added in v1.22.0

func (ts [RealTimeSource](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#RealTimeSource)) AfterFunc(d [time](https://pkg.go.dev/time).[Duration](https://pkg.go.dev/time#Duration), f func()) [Timer](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#Timer)

AfterFunc is a pass-through to time.AfterFunc.

#### func (RealTimeSource) [NewTimer](https://github.com/temporalio/temporal/blob/v1.30.0/common/clock/time_source.go#L53)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#RealTimeSource.NewTimer "Go to RealTimeSource.NewTimer")added in v1.25.0

func (ts [RealTimeSource](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#RealTimeSource)) NewTimer(d [time](https://pkg.go.dev/time).[Duration](https://pkg.go.dev/time#Duration)) (<-chan [time](https://pkg.go.dev/time).[Time](https://pkg.go.dev/time#Time), [Timer](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#Timer))

NewTimer is a pass-through to time.NewTimer.

#### func (RealTimeSource) [Now](https://github.com/temporalio/temporal/blob/v1.30.0/common/clock/time_source.go#L38)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#RealTimeSource.Now "Go to RealTimeSource.Now")

func (ts [RealTimeSource](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#RealTimeSource)) Now() [time](https://pkg.go.dev/time).[Time](https://pkg.go.dev/time#Time)

Now returns the current time, with the location set to UTC.

#### func (RealTimeSource) [Since](https://github.com/temporalio/temporal/blob/v1.30.0/common/clock/time_source.go#L43)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#RealTimeSource.Since "Go to RealTimeSource.Since")added in v1.25.0

func (ts [RealTimeSource](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#RealTimeSource)) Since(t [time](https://pkg.go.dev/time).[Time](https://pkg.go.dev/time#Time)) [time](https://pkg.go.dev/time).[Duration](https://pkg.go.dev/time#Duration)

Since returns the time elapsed since t

#### type [TimeSource](https://github.com/temporalio/temporal/blob/v1.30.0/common/clock/time_source.go#L10)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#TimeSource "Go to TimeSource")

type TimeSource interface {
 Now() [time](https://pkg.go.dev/time).[Time](https://pkg.go.dev/time#Time) Since(t [time](https://pkg.go.dev/time).[Time](https://pkg.go.dev/time#Time)) [time](https://pkg.go.dev/time).[Duration](https://pkg.go.dev/time#Duration) AfterFunc(d [time](https://pkg.go.dev/time).[Duration](https://pkg.go.dev/time#Duration), f func()) [Timer](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#Timer) NewTimer(d [time](https://pkg.go.dev/time).[Duration](https://pkg.go.dev/time#Duration)) (<-chan [time](https://pkg.go.dev/time).[Time](https://pkg.go.dev/time#Time), [Timer](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#Timer)) }

TimeSource is an interface to make it easier to test code that uses time.

#### type [Timer](https://github.com/temporalio/temporal/blob/v1.30.0/common/clock/time_source.go#L18)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#Timer "Go to Timer")added in v1.22.0

type Timer interface {
// Reset changes the expiration time of the timer. It returns true if the timer had been active, false if the	// timer had expired or been stopped.
	Reset(d [time](https://pkg.go.dev/time).[Duration](https://pkg.go.dev/time#Duration)) [bool](https://pkg.go.dev/builtin#bool)
// Stop prevents the Timer from firing. It returns true if the call stops the timer, false if the timer has	// already expired or been stopped.
	Stop() [bool](https://pkg.go.dev/builtin#bool)
}

Timer is a timer returned by TimeSource.AfterFunc. Unlike the timers returned by [time.NewTimer](https://pkg.go.dev/time#NewTimer) or time.Ticker, this timer does not have a channel. That is because the callback already reacts to the timer firing.

![Image 44](https://pkg.go.dev/static/shared/icon/insert_drive_file_gm_grey_24dp.svg) Source Files [¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#section-sourcefiles "Go to Source Files")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[View all Source files](https://github.com/temporalio/temporal/tree/v1.30.0/common/clock)

*   [context.go](https://github.com/temporalio/temporal/blob/v1.30.0/common/clock/context.go "context.go")
*   [event_time_source.go](https://github.com/temporalio/temporal/blob/v1.30.0/common/clock/event_time_source.go "event_time_source.go")
*   [time_source.go](https://github.com/temporalio/temporal/blob/v1.30.0/common/clock/time_source.go "time_source.go")

![Image 45](https://pkg.go.dev/static/shared/icon/folder_gm_grey_24dp.svg) Directories [¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#section-directories "Go to Directories")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

 Show internal  Expand all 

| Path | Synopsis |
| --- | --- |
| [hybrid_logical_clock](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock/hybrid_logical_clock) |  |

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
