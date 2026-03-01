# Source: https://pkg.go.dev/go.uber.org/goleak@v1.3.0/internal/stack

Title: stack package - go.uber.org/goleak/internal/stack - Go Packages

URL Source: https://pkg.go.dev/go.uber.org/goleak@v1.3.0/internal/stack

Markdown Content:
stack package - go.uber.org/goleak/internal/stack - Go Packages
===============

[![Image 2: Go](https://pkg.go.dev/static/shared/logo/go-white.svg)](https://go.dev/)

[Skip to Main Content](https://pkg.go.dev/go.uber.org/goleak@v1.3.0/internal/stack#main-content)

![Image 3](https://pkg.go.dev/static/shared/icon/search_gm_grey_24dp.svg)![Image 4](https://pkg.go.dev/static/shared/icon/search_gm_grey_24dp.svg)

*   [Why Go ![Image 5: submenu dropdown icon](https://pkg.go.dev/static/shared/icon/arrow_drop_down_gm_grey_24dp.svg)](https://pkg.go.dev/go.uber.org/goleak@v1.3.0/internal/stack#)
    *   [Case Studies](https://go.dev/solutions#case-studies) 
Common problems companies solve with Go

    *   [Use Cases](https://go.dev/solutions#use-cases) 
Stories about how and why companies use Go

    *   [Security](https://go.dev/security/) 
How Go can help keep you secure by default

*   [Learn](https://go.dev/learn/)
*   [Docs ![Image 6: submenu dropdown icon](https://pkg.go.dev/static/shared/icon/arrow_drop_down_gm_grey_24dp.svg)](https://pkg.go.dev/go.uber.org/goleak@v1.3.0/internal/stack#)
    *   [Effective Go](https://go.dev/doc/effective_go) 
Tips for writing clear, performant, and idiomatic Go code

    *   [Go User Manual](https://go.dev/doc/) 
A complete introduction to building software with Go

    *   [Standard library](https://pkg.go.dev/std) 
Reference documentation for Go's standard library

    *   [Release Notes](https://go.dev/doc/devel/release) 
Learn what's new in each Go release

*   [Packages](https://pkg.go.dev/)
*   [Community ![Image 7: submenu dropdown icon](https://pkg.go.dev/static/shared/icon/arrow_drop_down_gm_grey_24dp.svg)](https://pkg.go.dev/go.uber.org/goleak@v1.3.0/internal/stack#)
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

*   [Why Go _![Image 17](https://pkg.go.dev/static/shared/icon/navigate\_next\_gm\_grey\_24dp.svg)_](https://pkg.go.dev/go.uber.org/goleak@v1.3.0/internal/stack#)

[_![Image 18](https://pkg.go.dev/static/shared/icon/navigate\_before\_gm\_grey\_24dp.svg)_ Why Go](https://pkg.go.dev/go.uber.org/goleak@v1.3.0/internal/stack#) 
    *   [Case Studies](https://go.dev/solutions#case-studies)
    *   [Use Cases](https://go.dev/solutions#use-cases)
    *   [Security](https://go.dev/security/)

*   [Learn](https://go.dev/learn/)
*   [Docs _![Image 19](https://pkg.go.dev/static/shared/icon/navigate\_next\_gm\_grey\_24dp.svg)_](https://pkg.go.dev/go.uber.org/goleak@v1.3.0/internal/stack#)

[_![Image 20](https://pkg.go.dev/static/shared/icon/navigate\_before\_gm\_grey\_24dp.svg)_ Docs](https://pkg.go.dev/go.uber.org/goleak@v1.3.0/internal/stack#) 
    *   [Effective Go](https://go.dev/doc/effective_go)
    *   [Go User Manual](https://go.dev/doc/)
    *   [Standard library](https://pkg.go.dev/std)
    *   [Release Notes](https://go.dev/doc/devel/release)

*   [Packages](https://pkg.go.dev/)
*   [Community _![Image 21](https://pkg.go.dev/static/shared/icon/navigate\_next\_gm\_grey\_24dp.svg)_](https://pkg.go.dev/go.uber.org/goleak@v1.3.0/internal/stack#)

[_![Image 22](https://pkg.go.dev/static/shared/icon/navigate\_before\_gm\_grey\_24dp.svg)_ Community](https://pkg.go.dev/go.uber.org/goleak@v1.3.0/internal/stack#) 
    *   [Recorded Talks](https://go.dev/talks/)
    *   [Meetups _![Image 23](https://pkg.go.dev/static/shared/icon/launch\_gm\_grey\_24dp.svg)_](https://www.meetup.com/pro/go)
    *   [Conferences _![Image 24](https://pkg.go.dev/static/shared/icon/launch\_gm\_grey\_24dp.svg)_](https://github.com/golang/go/wiki/Conferences)
    *   [Go blog](https://go.dev/blog)
    *   [Go project](https://go.dev/help)
    *   Get connected [![Image 25](https://pkg.go.dev/static/shared/logo/social/google-groups.svg)](https://groups.google.com/g/golang-nuts)[![Image 26](https://pkg.go.dev/static/shared/logo/social/github.svg)](https://github.com/golang)[![Image 27](https://pkg.go.dev/static/shared/logo/social/twitter.svg)](https://twitter.com/golang)[![Image 28](https://pkg.go.dev/static/shared/logo/social/reddit.svg)](https://www.reddit.com/r/golang/)[![Image 29](https://pkg.go.dev/static/shared/logo/social/slack.svg)](https://invite.slack.golangbridge.org/)[![Image 30](https://pkg.go.dev/static/shared/logo/social/stack-overflow.svg)](https://stackoverflow.com/collectives/go) 

1.   [Discover Packages](https://pkg.go.dev/)
2.   [go.uber.org/goleak](https://pkg.go.dev/go.uber.org/goleak@v1.3.0)
3.   [internal](https://pkg.go.dev/go.uber.org/goleak/internal@v1.3.0)
4.   [stack](https://pkg.go.dev/go.uber.org/goleak@v1.3.0/internal/stack)![Image 31](https://pkg.go.dev/static/shared/icon/content_copy_gm_grey_24dp.svg)

[![Image 32: Go](https://pkg.go.dev/static/shared/logo/go-blue.svg)](https://go.dev/)
stack
=====

package![Image 33](https://pkg.go.dev/static/shared/icon/content_copy_gm_grey_24dp.svg)

[Version: v1.3.0](https://pkg.go.dev/go.uber.org/goleak@v1.3.0/internal/stack?tab=versions)

 Opens a new window with list of versions in this module. 

Latest Latest 

![Image 34: Warning](https://pkg.go.dev/static/shared/icon/alert_gm_grey_24dp.svg)
This package is not in the latest version of its module.

[Go to latest](https://pkg.go.dev/go.uber.org/goleak/internal/stack) Published: Oct 24, 2023  License: [MIT](https://pkg.go.dev/go.uber.org/goleak@v1.3.0/internal/stack?tab=licenses)

 Opens a new window with license information. 

[Imports: 8](https://pkg.go.dev/go.uber.org/goleak@v1.3.0/internal/stack?tab=imports)

 Opens a new window with list of imports. 

[Imported by: 0](https://pkg.go.dev/go.uber.org/goleak@v1.3.0/internal/stack?tab=importedby)

 Opens a new window with list of known importers. 

Details
-------

*   ![Image 35: checked](https://pkg.go.dev/static/shared/icon/check_circle_gm_grey_24dp.svg) Valid [go.mod](https://github.com/uber-go/goleak/tree/v1.3.0/go.mod) file ![Image 36](https://pkg.go.dev/static/shared/icon/help_gm_grey_24dp.svg)
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

[github.com/uber-go/goleak](https://github.com/uber-go/goleak "https://github.com/uber-go/goleak")

Links
-----

*   [![Image 43: Open Source Insights Logo](https://pkg.go.dev/static/shared/icon/depsdev-logo.svg) Open Source Insights](https://deps.dev/go/go.uber.org%2Fgoleak/v1.3.0 "View this module on Open Source Insights")

 Jump to ... 

*   [Documentation](https://pkg.go.dev/go.uber.org/goleak@v1.3.0/internal/stack#section-documentation)
    *   [Overview](https://pkg.go.dev/go.uber.org/goleak@v1.3.0/internal/stack#pkg-overview)
    *   [Index](https://pkg.go.dev/go.uber.org/goleak@v1.3.0/internal/stack#pkg-index)
    *   [Constants](https://pkg.go.dev/go.uber.org/goleak@v1.3.0/internal/stack#pkg-constants)
    *   [Variables](https://pkg.go.dev/go.uber.org/goleak@v1.3.0/internal/stack#pkg-variables)
    *   [Functions](https://pkg.go.dev/go.uber.org/goleak@v1.3.0/internal/stack#pkg-functions)
    *   [Types](https://pkg.go.dev/go.uber.org/goleak@v1.3.0/internal/stack#pkg-types)
        *   [type Stack](https://pkg.go.dev/go.uber.org/goleak@v1.3.0/internal/stack#Stack "type Stack")
            *   [All()](https://pkg.go.dev/go.uber.org/goleak@v1.3.0/internal/stack#All "All()")
            *   [Current()](https://pkg.go.dev/go.uber.org/goleak@v1.3.0/internal/stack#Current "Current()")
            *   [(s) FirstFunction()](https://pkg.go.dev/go.uber.org/goleak@v1.3.0/internal/stack#Stack.FirstFunction "(s) FirstFunction()")
            *   [(s) Full()](https://pkg.go.dev/go.uber.org/goleak@v1.3.0/internal/stack#Stack.Full "(s) Full()")
            *   [(s) HasFunction(name)](https://pkg.go.dev/go.uber.org/goleak@v1.3.0/internal/stack#Stack.HasFunction "(s) HasFunction(name)")
            *   [(s) ID()](https://pkg.go.dev/go.uber.org/goleak@v1.3.0/internal/stack#Stack.ID "(s) ID()")
            *   [(s) State()](https://pkg.go.dev/go.uber.org/goleak@v1.3.0/internal/stack#Stack.State "(s) State()")
            *   [(s) String()](https://pkg.go.dev/go.uber.org/goleak@v1.3.0/internal/stack#Stack.String "(s) String()")

*   [Source Files](https://pkg.go.dev/go.uber.org/goleak@v1.3.0/internal/stack#section-sourcefiles)

![Image 44](https://pkg.go.dev/static/shared/icon/code_gm_grey_24dp.svg) Documentation [¶](https://pkg.go.dev/go.uber.org/goleak@v1.3.0/internal/stack#section-documentation "Go to Documentation")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Overview [¶](https://pkg.go.dev/go.uber.org/goleak@v1.3.0/internal/stack#pkg-overview "Go to Overview")

Package stack is used for parsing stacks from `runtime.Stack`.

### Index [¶](https://pkg.go.dev/go.uber.org/goleak@v1.3.0/internal/stack#pkg-index "Go to Index")

*   [type Stack](https://pkg.go.dev/go.uber.org/goleak@v1.3.0/internal/stack#Stack)
*       *   [func All() []Stack](https://pkg.go.dev/go.uber.org/goleak@v1.3.0/internal/stack#All)
    *   [func Current() Stack](https://pkg.go.dev/go.uber.org/goleak@v1.3.0/internal/stack#Current)

*       *   [func (s Stack) FirstFunction() string](https://pkg.go.dev/go.uber.org/goleak@v1.3.0/internal/stack#Stack.FirstFunction)
    *   [func (s Stack) Full() string](https://pkg.go.dev/go.uber.org/goleak@v1.3.0/internal/stack#Stack.Full)
    *   [func (s Stack) HasFunction(name string) bool](https://pkg.go.dev/go.uber.org/goleak@v1.3.0/internal/stack#Stack.HasFunction)
    *   [func (s Stack) ID() int](https://pkg.go.dev/go.uber.org/goleak@v1.3.0/internal/stack#Stack.ID)
    *   [func (s Stack) State() string](https://pkg.go.dev/go.uber.org/goleak@v1.3.0/internal/stack#Stack.State)
    *   [func (s Stack) String() string](https://pkg.go.dev/go.uber.org/goleak@v1.3.0/internal/stack#Stack.String)

### Constants [¶](https://pkg.go.dev/go.uber.org/goleak@v1.3.0/internal/stack#pkg-constants "Go to Constants")

This section is empty.

### Variables [¶](https://pkg.go.dev/go.uber.org/goleak@v1.3.0/internal/stack#pkg-variables "Go to Variables")

This section is empty.

### Functions [¶](https://pkg.go.dev/go.uber.org/goleak@v1.3.0/internal/stack#pkg-functions "Go to Functions")

This section is empty.

### Types [¶](https://pkg.go.dev/go.uber.org/goleak@v1.3.0/internal/stack#pkg-types "Go to Types")

#### type [Stack](https://github.com/uber-go/goleak/blob/v1.3.0/internal/stack/stacks.go#L36)[¶](https://pkg.go.dev/go.uber.org/goleak@v1.3.0/internal/stack#Stack "Go to Stack")

type Stack struct {
	// contains filtered or unexported fields
}

Stack represents a single Goroutine's stack.

#### func [All](https://github.com/uber-go/goleak/blob/v1.3.0/internal/stack/stacks.go#L228)[¶](https://pkg.go.dev/go.uber.org/goleak@v1.3.0/internal/stack#All "Go to All")

func All() [][Stack](https://pkg.go.dev/go.uber.org/goleak@v1.3.0/internal/stack#Stack)

All returns the stacks for all running goroutines.

#### func [Current](https://github.com/uber-go/goleak/blob/v1.3.0/internal/stack/stacks.go#L233)[¶](https://pkg.go.dev/go.uber.org/goleak@v1.3.0/internal/stack#Current "Go to Current")

func Current() [Stack](https://pkg.go.dev/go.uber.org/goleak@v1.3.0/internal/stack#Stack)

Current returns the stack for the current goroutine.

#### func (Stack) [FirstFunction](https://github.com/uber-go/goleak/blob/v1.3.0/internal/stack/stacks.go#L66)[¶](https://pkg.go.dev/go.uber.org/goleak@v1.3.0/internal/stack#Stack.FirstFunction "Go to Stack.FirstFunction")

func (s [Stack](https://pkg.go.dev/go.uber.org/goleak@v1.3.0/internal/stack#Stack)) FirstFunction() [string](https://pkg.go.dev/builtin#string)

FirstFunction returns the name of the first function on the stack.

#### func (Stack) [Full](https://github.com/uber-go/goleak/blob/v1.3.0/internal/stack/stacks.go#L61)[¶](https://pkg.go.dev/go.uber.org/goleak@v1.3.0/internal/stack#Stack.Full "Go to Stack.Full")

func (s [Stack](https://pkg.go.dev/go.uber.org/goleak@v1.3.0/internal/stack#Stack)) Full() [string](https://pkg.go.dev/builtin#string)

Full returns the full stack trace for this goroutine.

#### func (Stack) [HasFunction](https://github.com/uber-go/goleak/blob/v1.3.0/internal/stack/stacks.go#L72)[¶](https://pkg.go.dev/go.uber.org/goleak@v1.3.0/internal/stack#Stack.HasFunction "Go to Stack.HasFunction")added in v1.3.0

func (s [Stack](https://pkg.go.dev/go.uber.org/goleak@v1.3.0/internal/stack#Stack)) HasFunction(name [string](https://pkg.go.dev/builtin#string)) [bool](https://pkg.go.dev/builtin#bool)

HasFunction reports whether the stack has the given function anywhere in it.

#### func (Stack) [ID](https://github.com/uber-go/goleak/blob/v1.3.0/internal/stack/stacks.go#L51)[¶](https://pkg.go.dev/go.uber.org/goleak@v1.3.0/internal/stack#Stack.ID "Go to Stack.ID")

func (s [Stack](https://pkg.go.dev/go.uber.org/goleak@v1.3.0/internal/stack#Stack)) ID() [int](https://pkg.go.dev/builtin#int)

ID returns the goroutine ID.

#### func (Stack) [State](https://github.com/uber-go/goleak/blob/v1.3.0/internal/stack/stacks.go#L56)[¶](https://pkg.go.dev/go.uber.org/goleak@v1.3.0/internal/stack#Stack.State "Go to Stack.State")

func (s [Stack](https://pkg.go.dev/go.uber.org/goleak@v1.3.0/internal/stack#Stack)) State() [string](https://pkg.go.dev/builtin#string)

State returns the Goroutine's state.

#### func (Stack) [String](https://github.com/uber-go/goleak/blob/v1.3.0/internal/stack/stacks.go#L77)[¶](https://pkg.go.dev/go.uber.org/goleak@v1.3.0/internal/stack#Stack.String "Go to Stack.String")

func (s [Stack](https://pkg.go.dev/go.uber.org/goleak@v1.3.0/internal/stack#Stack)) String() [string](https://pkg.go.dev/builtin#string)

![Image 45](https://pkg.go.dev/static/shared/icon/insert_drive_file_gm_grey_24dp.svg) Source Files [¶](https://pkg.go.dev/go.uber.org/goleak@v1.3.0/internal/stack#section-sourcefiles "Go to Source Files")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[View all Source files](https://github.com/uber-go/goleak/tree/v1.3.0/internal/stack)

*   [doc.go](https://github.com/uber-go/goleak/blob/v1.3.0/internal/stack/doc.go "doc.go")
*   [scan.go](https://github.com/uber-go/goleak/blob/v1.3.0/internal/stack/scan.go "scan.go")
*   [stacks.go](https://github.com/uber-go/goleak/blob/v1.3.0/internal/stack/stacks.go "stacks.go")

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
