# Source: https://pkg.go.dev/go.uber.org/atomic@v1.11.0

Title: atomic package - go.uber.org/atomic - Go Packages

URL Source: https://pkg.go.dev/go.uber.org/atomic@v1.11.0

Markdown Content:
atomic package - go.uber.org/atomic - Go Packages
===============

[![Image 1: Go](https://pkg.go.dev/static/shared/logo/go-white.svg)](https://go.dev/)

[Skip to Main Content](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#main-content)

![Image 2](https://pkg.go.dev/static/shared/icon/search_gm_grey_24dp.svg)![Image 3](https://pkg.go.dev/static/shared/icon/search_gm_grey_24dp.svg)

*   [Why Go ![Image 4: submenu dropdown icon](https://pkg.go.dev/static/shared/icon/arrow_drop_down_gm_grey_24dp.svg)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#)
    *   [Case Studies](https://go.dev/solutions#case-studies) 
Common problems companies solve with Go

    *   [Use Cases](https://go.dev/solutions#use-cases) 
Stories about how and why companies use Go

    *   [Security](https://go.dev/security/) 
How Go can help keep you secure by default

*   [Learn](https://go.dev/learn/)
*   [Docs ![Image 5: submenu dropdown icon](https://pkg.go.dev/static/shared/icon/arrow_drop_down_gm_grey_24dp.svg)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#)
    *   [Effective Go](https://go.dev/doc/effective_go) 
Tips for writing clear, performant, and idiomatic Go code

    *   [Go User Manual](https://go.dev/doc/) 
A complete introduction to building software with Go

    *   [Standard library](https://pkg.go.dev/std) 
Reference documentation for Go's standard library

    *   [Release Notes](https://go.dev/doc/devel/release) 
Learn what's new in each Go release

*   [Packages](https://pkg.go.dev/)
*   [Community ![Image 6: submenu dropdown icon](https://pkg.go.dev/static/shared/icon/arrow_drop_down_gm_grey_24dp.svg)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#)
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

*   [Why Go _![Image 16](https://pkg.go.dev/static/shared/icon/navigate\_next\_gm\_grey\_24dp.svg)_](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#)

[_![Image 17](https://pkg.go.dev/static/shared/icon/navigate\_before\_gm\_grey\_24dp.svg)_ Why Go](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#) 
    *   [Case Studies](https://go.dev/solutions#case-studies)
    *   [Use Cases](https://go.dev/solutions#use-cases)
    *   [Security](https://go.dev/security/)

*   [Learn](https://go.dev/learn/)
*   [Docs _![Image 18](https://pkg.go.dev/static/shared/icon/navigate\_next\_gm\_grey\_24dp.svg)_](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#)

[_![Image 19](https://pkg.go.dev/static/shared/icon/navigate\_before\_gm\_grey\_24dp.svg)_ Docs](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#) 
    *   [Effective Go](https://go.dev/doc/effective_go)
    *   [Go User Manual](https://go.dev/doc/)
    *   [Standard library](https://pkg.go.dev/std)
    *   [Release Notes](https://go.dev/doc/devel/release)

*   [Packages](https://pkg.go.dev/)
*   [Community _![Image 20](https://pkg.go.dev/static/shared/icon/navigate\_next\_gm\_grey\_24dp.svg)_](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#)

[_![Image 21](https://pkg.go.dev/static/shared/icon/navigate\_before\_gm\_grey\_24dp.svg)_ Community](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#) 
    *   [Recorded Talks](https://go.dev/talks/)
    *   [Meetups _![Image 22](https://pkg.go.dev/static/shared/icon/launch\_gm\_grey\_24dp.svg)_](https://www.meetup.com/pro/go)
    *   [Conferences _![Image 23](https://pkg.go.dev/static/shared/icon/launch\_gm\_grey\_24dp.svg)_](https://github.com/golang/go/wiki/Conferences)
    *   [Go blog](https://go.dev/blog)
    *   [Go project](https://go.dev/help)
    *   Get connected [![Image 24](https://pkg.go.dev/static/shared/logo/social/google-groups.svg)](https://groups.google.com/g/golang-nuts)[![Image 25](https://pkg.go.dev/static/shared/logo/social/github.svg)](https://github.com/golang)[![Image 26](https://pkg.go.dev/static/shared/logo/social/twitter.svg)](https://twitter.com/golang)[![Image 27](https://pkg.go.dev/static/shared/logo/social/reddit.svg)](https://www.reddit.com/r/golang/)[![Image 28](https://pkg.go.dev/static/shared/logo/social/slack.svg)](https://invite.slack.golangbridge.org/)[![Image 29](https://pkg.go.dev/static/shared/logo/social/stack-overflow.svg)](https://stackoverflow.com/collectives/go) 

1.   [Discover Packages](https://pkg.go.dev/)
2.   [go.uber.org/atomic](https://pkg.go.dev/go.uber.org/atomic@v1.11.0)![Image 30](https://pkg.go.dev/static/shared/icon/content_copy_gm_grey_24dp.svg)

[![Image 31: Go](https://pkg.go.dev/static/shared/logo/go-blue.svg)](https://go.dev/)
atomic
======

package module![Image 32](https://pkg.go.dev/static/shared/icon/content_copy_gm_grey_24dp.svg)

[Version: v1.11.0](https://pkg.go.dev/go.uber.org/atomic@v1.11.0?tab=versions)

 Opens a new window with list of versions in this module. 

Latest Latest 

![Image 33: Warning](https://pkg.go.dev/static/shared/icon/alert_gm_grey_24dp.svg)
This package is not in the latest version of its module.

[Go to latest](https://pkg.go.dev/go.uber.org/atomic) Published: May 3, 2023  License: [MIT](https://pkg.go.dev/go.uber.org/atomic@v1.11.0?tab=licenses)

 Opens a new window with license information. 

[Imports: 7](https://pkg.go.dev/go.uber.org/atomic@v1.11.0?tab=imports)

 Opens a new window with list of imports. 

[Imported by: 6,374](https://pkg.go.dev/go.uber.org/atomic@v1.11.0?tab=importedby)

 Opens a new window with list of known importers. 

Details
-------

*   ![Image 34: checked](https://pkg.go.dev/static/shared/icon/check_circle_gm_grey_24dp.svg) Valid [go.mod](https://github.com/uber-go/atomic/tree/v1.11.0/go.mod) file ![Image 35](https://pkg.go.dev/static/shared/icon/help_gm_grey_24dp.svg)
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

[github.com/uber-go/atomic](https://github.com/uber-go/atomic "https://github.com/uber-go/atomic")

Links
-----

*   [![Image 42: Open Source Insights Logo](https://pkg.go.dev/static/shared/icon/depsdev-logo.svg) Open Source Insights](https://deps.dev/go/go.uber.org%2Fatomic/v1.11.0 "View this module on Open Source Insights")

 Jump to ... 

*   [README](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#section-readme)
    *   [Installation](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#readme-installation)
        *   [Legacy Import Path](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#readme-legacy-import-path)

    *   [Usage](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#readme-usage)
    *   [Development Status](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#readme-development-status)

*   [Documentation](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#section-documentation)
    *   [Overview](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#pkg-overview)
    *   [Index](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#pkg-index)
    *   [Examples](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#pkg-examples)
        *   [Package](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#example-package "Package")

    *   [Constants](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#pkg-constants)
    *   [Variables](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#pkg-variables)
    *   [Functions](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#pkg-functions)
    *   [Types](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#pkg-types)
        *   [type Bool](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Bool "type Bool")
            *   [NewBool(val)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#NewBool "NewBool(val)")
            *   [(x) CAS(old, new)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Bool.CAS "(x) CAS(old, new)")
            *   [(x) CompareAndSwap(old, new)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Bool.CompareAndSwap "(x) CompareAndSwap(old, new)")
            *   [(x) Load()](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Bool.Load "(x) Load()")
            *   [(x) MarshalJSON()](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Bool.MarshalJSON "(x) MarshalJSON()")
            *   [(x) Store(val)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Bool.Store "(x) Store(val)")
            *   [(b) String()](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Bool.String "(b) String()")
            *   [(x) Swap(val)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Bool.Swap "(x) Swap(val)")
            *   [(b) Toggle()](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Bool.Toggle "(b) Toggle()")
            *   [(x) UnmarshalJSON(b)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Bool.UnmarshalJSON "(x) UnmarshalJSON(b)")

        *   [type Duration](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Duration "type Duration")
            *   [NewDuration(val)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#NewDuration "NewDuration(val)")
            *   [(d) Add(delta)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Duration.Add "(d) Add(delta)")
            *   [(x) CAS(old, new)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Duration.CAS "(x) CAS(old, new)")
            *   [(x) CompareAndSwap(old, new)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Duration.CompareAndSwap "(x) CompareAndSwap(old, new)")
            *   [(x) Load()](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Duration.Load "(x) Load()")
            *   [(x) MarshalJSON()](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Duration.MarshalJSON "(x) MarshalJSON()")
            *   [(x) Store(val)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Duration.Store "(x) Store(val)")
            *   [(d) String()](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Duration.String "(d) String()")
            *   [(d) Sub(delta)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Duration.Sub "(d) Sub(delta)")
            *   [(x) Swap(val)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Duration.Swap "(x) Swap(val)")
            *   [(x) UnmarshalJSON(b)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Duration.UnmarshalJSON "(x) UnmarshalJSON(b)")

        *   [type Error](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Error "type Error")
            *   [NewError(val)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#NewError "NewError(val)")
            *   [(x) CompareAndSwap(old, new)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Error.CompareAndSwap "(x) CompareAndSwap(old, new)")
            *   [(x) Load()](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Error.Load "(x) Load()")
            *   [(x) Store(val)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Error.Store "(x) Store(val)")
            *   [(x) Swap(val)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Error.Swap "(x) Swap(val)")

        *   [type Float32](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Float32 "type Float32")
            *   [NewFloat32(val)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#NewFloat32 "NewFloat32(val)")
            *   [(f) Add(delta)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Float32.Add "(f) Add(delta)")
            *   [(f) CAS(old, new)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Float32.CAS "(f) CAS(old, new)")
            *   [(f) CompareAndSwap(old, new)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Float32.CompareAndSwap "(f) CompareAndSwap(old, new)")
            *   [(x) Load()](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Float32.Load "(x) Load()")
            *   [(x) MarshalJSON()](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Float32.MarshalJSON "(x) MarshalJSON()")
            *   [(x) Store(val)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Float32.Store "(x) Store(val)")
            *   [(f) String()](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Float32.String "(f) String()")
            *   [(f) Sub(delta)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Float32.Sub "(f) Sub(delta)")
            *   [(x) Swap(val)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Float32.Swap "(x) Swap(val)")
            *   [(x) UnmarshalJSON(b)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Float32.UnmarshalJSON "(x) UnmarshalJSON(b)")

        *   [type Float64](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Float64 "type Float64")
            *   [NewFloat64(val)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#NewFloat64 "NewFloat64(val)")
            *   [(f) Add(delta)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Float64.Add "(f) Add(delta)")
            *   [(f) CAS(old, new)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Float64.CAS "(f) CAS(old, new)")
            *   [(f) CompareAndSwap(old, new)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Float64.CompareAndSwap "(f) CompareAndSwap(old, new)")
            *   [(x) Load()](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Float64.Load "(x) Load()")
            *   [(x) MarshalJSON()](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Float64.MarshalJSON "(x) MarshalJSON()")
            *   [(x) Store(val)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Float64.Store "(x) Store(val)")
            *   [(f) String()](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Float64.String "(f) String()")
            *   [(f) Sub(delta)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Float64.Sub "(f) Sub(delta)")
            *   [(x) Swap(val)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Float64.Swap "(x) Swap(val)")
            *   [(x) UnmarshalJSON(b)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Float64.UnmarshalJSON "(x) UnmarshalJSON(b)")

        *   [type Int32](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Int32 "type Int32")
            *   [NewInt32(val)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#NewInt32 "NewInt32(val)")
            *   [(i) Add(delta)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Int32.Add "(i) Add(delta)")
            *   [(i) CAS(old, new)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Int32.CAS "(i) CAS(old, new)")
            *   [(i) CompareAndSwap(old, new)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Int32.CompareAndSwap "(i) CompareAndSwap(old, new)")
            *   [(i) Dec()](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Int32.Dec "(i) Dec()")
            *   [(i) Inc()](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Int32.Inc "(i) Inc()")
            *   [(i) Load()](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Int32.Load "(i) Load()")
            *   [(i) MarshalJSON()](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Int32.MarshalJSON "(i) MarshalJSON()")
            *   [(i) Store(val)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Int32.Store "(i) Store(val)")
            *   [(i) String()](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Int32.String "(i) String()")
            *   [(i) Sub(delta)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Int32.Sub "(i) Sub(delta)")
            *   [(i) Swap(val)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Int32.Swap "(i) Swap(val)")
            *   [(i) UnmarshalJSON(b)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Int32.UnmarshalJSON "(i) UnmarshalJSON(b)")

        *   [type Int64](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Int64 "type Int64")
            *   [NewInt64(val)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#NewInt64 "NewInt64(val)")
            *   [(i) Add(delta)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Int64.Add "(i) Add(delta)")
            *   [(i) CAS(old, new)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Int64.CAS "(i) CAS(old, new)")
            *   [(i) CompareAndSwap(old, new)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Int64.CompareAndSwap "(i) CompareAndSwap(old, new)")
            *   [(i) Dec()](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Int64.Dec "(i) Dec()")
            *   [(i) Inc()](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Int64.Inc "(i) Inc()")
            *   [(i) Load()](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Int64.Load "(i) Load()")
            *   [(i) MarshalJSON()](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Int64.MarshalJSON "(i) MarshalJSON()")
            *   [(i) Store(val)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Int64.Store "(i) Store(val)")
            *   [(i) String()](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Int64.String "(i) String()")
            *   [(i) Sub(delta)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Int64.Sub "(i) Sub(delta)")
            *   [(i) Swap(val)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Int64.Swap "(i) Swap(val)")
            *   [(i) UnmarshalJSON(b)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Int64.UnmarshalJSON "(i) UnmarshalJSON(b)")

        *   [type Pointer](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Pointer "type Pointer")
            *   [NewPointer(v)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#NewPointer "NewPointer(v)")
            *   [(p) CompareAndSwap(old, new)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Pointer.CompareAndSwap "(p) CompareAndSwap(old, new)")
            *   [(p) Load()](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Pointer.Load "(p) Load()")
            *   [(p) Store(val)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Pointer.Store "(p) Store(val)")
            *   [(p) String()](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Pointer.String "(p) String()")
            *   [(p) Swap(val)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Pointer.Swap "(p) Swap(val)")

        *   [type String](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#String "type String")
            *   [NewString(val)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#NewString "NewString(val)")
            *   [(x) CompareAndSwap(old, new)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#String.CompareAndSwap "(x) CompareAndSwap(old, new)")
            *   [(x) Load()](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#String.Load "(x) Load()")
            *   [(s) MarshalText()](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#String.MarshalText "(s) MarshalText()")
            *   [(x) Store(val)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#String.Store "(x) Store(val)")
            *   [(s) String()](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#String.String "(s) String()")
            *   [(x) Swap(val)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#String.Swap "(x) Swap(val)")
            *   [(s) UnmarshalText(b)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#String.UnmarshalText "(s) UnmarshalText(b)")

        *   [type Time](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Time "type Time")
            *   [NewTime(val)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#NewTime "NewTime(val)")
            *   [(x) Load()](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Time.Load "(x) Load()")
            *   [(x) Store(val)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Time.Store "(x) Store(val)")

        *   [type Uint32](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uint32 "type Uint32")
            *   [NewUint32(val)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#NewUint32 "NewUint32(val)")
            *   [(i) Add(delta)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uint32.Add "(i) Add(delta)")
            *   [(i) CAS(old, new)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uint32.CAS "(i) CAS(old, new)")
            *   [(i) CompareAndSwap(old, new)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uint32.CompareAndSwap "(i) CompareAndSwap(old, new)")
            *   [(i) Dec()](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uint32.Dec "(i) Dec()")
            *   [(i) Inc()](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uint32.Inc "(i) Inc()")
            *   [(i) Load()](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uint32.Load "(i) Load()")
            *   [(i) MarshalJSON()](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uint32.MarshalJSON "(i) MarshalJSON()")
            *   [(i) Store(val)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uint32.Store "(i) Store(val)")
            *   [(i) String()](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uint32.String "(i) String()")
            *   [(i) Sub(delta)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uint32.Sub "(i) Sub(delta)")
            *   [(i) Swap(val)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uint32.Swap "(i) Swap(val)")
            *   [(i) UnmarshalJSON(b)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uint32.UnmarshalJSON "(i) UnmarshalJSON(b)")

        *   [type Uint64](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uint64 "type Uint64")
            *   [NewUint64(val)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#NewUint64 "NewUint64(val)")
            *   [(i) Add(delta)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uint64.Add "(i) Add(delta)")
            *   [(i) CAS(old, new)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uint64.CAS "(i) CAS(old, new)")
            *   [(i) CompareAndSwap(old, new)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uint64.CompareAndSwap "(i) CompareAndSwap(old, new)")
            *   [(i) Dec()](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uint64.Dec "(i) Dec()")
            *   [(i) Inc()](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uint64.Inc "(i) Inc()")
            *   [(i) Load()](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uint64.Load "(i) Load()")
            *   [(i) MarshalJSON()](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uint64.MarshalJSON "(i) MarshalJSON()")
            *   [(i) Store(val)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uint64.Store "(i) Store(val)")
            *   [(i) String()](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uint64.String "(i) String()")
            *   [(i) Sub(delta)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uint64.Sub "(i) Sub(delta)")
            *   [(i) Swap(val)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uint64.Swap "(i) Swap(val)")
            *   [(i) UnmarshalJSON(b)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uint64.UnmarshalJSON "(i) UnmarshalJSON(b)")

        *   [type Uintptr](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uintptr "type Uintptr")
            *   [NewUintptr(val)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#NewUintptr "NewUintptr(val)")
            *   [(i) Add(delta)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uintptr.Add "(i) Add(delta)")
            *   [(i) CAS(old, new)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uintptr.CAS "(i) CAS(old, new)")
            *   [(i) CompareAndSwap(old, new)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uintptr.CompareAndSwap "(i) CompareAndSwap(old, new)")
            *   [(i) Dec()](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uintptr.Dec "(i) Dec()")
            *   [(i) Inc()](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uintptr.Inc "(i) Inc()")
            *   [(i) Load()](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uintptr.Load "(i) Load()")
            *   [(i) MarshalJSON()](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uintptr.MarshalJSON "(i) MarshalJSON()")
            *   [(i) Store(val)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uintptr.Store "(i) Store(val)")
            *   [(i) String()](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uintptr.String "(i) String()")
            *   [(i) Sub(delta)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uintptr.Sub "(i) Sub(delta)")
            *   [(i) Swap(val)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uintptr.Swap "(i) Swap(val)")
            *   [(i) UnmarshalJSON(b)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uintptr.UnmarshalJSON "(i) UnmarshalJSON(b)")

        *   [type UnsafePointer](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#UnsafePointer "type UnsafePointer")
            *   [NewUnsafePointer(val)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#NewUnsafePointer "NewUnsafePointer(val)")
            *   [(p) CAS(old, new)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#UnsafePointer.CAS "(p) CAS(old, new)")
            *   [(p) CompareAndSwap(old, new)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#UnsafePointer.CompareAndSwap "(p) CompareAndSwap(old, new)")
            *   [(p) Load()](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#UnsafePointer.Load "(p) Load()")
            *   [(p) Store(val)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#UnsafePointer.Store "(p) Store(val)")
            *   [(p) Swap(val)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#UnsafePointer.Swap "(p) Swap(val)")

        *   [type Value](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Value "type Value")

*   [Source Files](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#section-sourcefiles)
*   [Directories](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#section-directories)

![Image 43](https://pkg.go.dev/static/shared/icon/chrome_reader_mode_gm_grey_24dp.svg) README [¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#section-readme "Go to Readme")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### atomic [![Image 44: GoDoc](https://godoc.org/github.com/uber-go/atomic?status.svg)](https://godoc.org/go.uber.org/atomic)[![Image 45: Build Status](https://github.com/uber-go/atomic/actions/workflows/go.yml/badge.svg)](https://github.com/uber-go/atomic/actions/workflows/go.yml)[![Image 46: Coverage Status](https://codecov.io/gh/uber-go/atomic/branch/master/graph/badge.svg)](https://codecov.io/gh/uber-go/atomic)[![Image 47: Go Report Card](https://goreportcard.com/badge/go.uber.org/atomic)](https://goreportcard.com/report/go.uber.org/atomic)

Simple wrappers for primitive types to enforce atomic access.

#### Installation

```
$ go get -u go.uber.org/atomic@v1
```

##### Legacy Import Path

As of v1.5.0, the import path `go.uber.org/atomic` is the only supported way of using this package. If you are using Go modules, this package will fail to compile with the legacy import path path `github.com/uber-go/atomic`.

We recommend migrating your code to the new import path but if you're unable to do so, or if your dependencies are still using the old import path, you will have to add a `replace` directive to your `go.mod` file downgrading the legacy import path to an older version.

```
replace github.com/uber-go/atomic => github.com/uber-go/atomic v1.4.0
```

You can do so automatically by running the following command.

```
$ go mod edit -replace github.com/uber-go/atomic=github.com/uber-go/atomic@v1.4.0
```

#### Usage

The standard library's `sync/atomic` is powerful, but it's easy to forget which variables must be accessed atomically. `go.uber.org/atomic` preserves all the functionality of the standard library, but wraps the primitive types to provide a safer, more convenient API.

```
var atom atomic.Uint32
atom.Store(42)
atom.Sub(2)
atom.CAS(40, 11)
```

See the [documentation](https://godoc.org/go.uber.org/atomic) for a complete API specification.

#### Development Status

Stable.

* * *

Released under the [MIT License](https://github.com/uber-go/atomic/blob/v1.11.0/LICENSE.txt).

Expand ▾Collapse ▴

![Image 48](https://pkg.go.dev/static/shared/icon/code_gm_grey_24dp.svg) Documentation [¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#section-documentation "Go to Documentation")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Overview [¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#pkg-overview "Go to Overview")

Package atomic provides simple wrappers around numerics to enforce atomic access.

Example [¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#example-package "Go to Example")

Output:

43 true 0 

Share Format Run

### Index [¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#pkg-index "Go to Index")

*   [type Bool](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Bool)
*       *   [func NewBool(val bool) *Bool](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#NewBool)

*       *   [func (x *Bool) CAS(old, new bool) (swapped bool)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Bool.CAS)deprecated
    *   [func (x *Bool) CompareAndSwap(old, new bool) (swapped bool)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Bool.CompareAndSwap)
    *   [func (x *Bool) Load() bool](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Bool.Load)
    *   [func (x *Bool) MarshalJSON() ([]byte, error)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Bool.MarshalJSON)
    *   [func (x *Bool) Store(val bool)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Bool.Store)
    *   [func (b *Bool) String() string](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Bool.String)
    *   [func (x *Bool) Swap(val bool) (old bool)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Bool.Swap)
    *   [func (b *Bool) Toggle() (old bool)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Bool.Toggle)
    *   [func (x *Bool) UnmarshalJSON(b []byte) error](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Bool.UnmarshalJSON)

*   [type Duration](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Duration)
*       *   [func NewDuration(val time.Duration) *Duration](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#NewDuration)

*       *   [func (d *Duration) Add(delta time.Duration) time.Duration](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Duration.Add)
    *   [func (x *Duration) CAS(old, new time.Duration) (swapped bool)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Duration.CAS)deprecated
    *   [func (x *Duration) CompareAndSwap(old, new time.Duration) (swapped bool)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Duration.CompareAndSwap)
    *   [func (x *Duration) Load() time.Duration](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Duration.Load)
    *   [func (x *Duration) MarshalJSON() ([]byte, error)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Duration.MarshalJSON)
    *   [func (x *Duration) Store(val time.Duration)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Duration.Store)
    *   [func (d *Duration) String() string](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Duration.String)
    *   [func (d *Duration) Sub(delta time.Duration) time.Duration](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Duration.Sub)
    *   [func (x *Duration) Swap(val time.Duration) (old time.Duration)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Duration.Swap)
    *   [func (x *Duration) UnmarshalJSON(b []byte) error](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Duration.UnmarshalJSON)

*   [type Error](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Error)
*       *   [func NewError(val error) *Error](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#NewError)

*       *   [func (x *Error) CompareAndSwap(old, new error) (swapped bool)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Error.CompareAndSwap)
    *   [func (x *Error) Load() error](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Error.Load)
    *   [func (x *Error) Store(val error)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Error.Store)
    *   [func (x *Error) Swap(val error) (old error)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Error.Swap)

*   [type Float32](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Float32)
*       *   [func NewFloat32(val float32) *Float32](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#NewFloat32)

*       *   [func (f *Float32) Add(delta float32) float32](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Float32.Add)
    *   [func (f *Float32) CAS(old, new float32) (swapped bool)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Float32.CAS)deprecated
    *   [func (f *Float32) CompareAndSwap(old, new float32) (swapped bool)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Float32.CompareAndSwap)
    *   [func (x *Float32) Load() float32](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Float32.Load)
    *   [func (x *Float32) MarshalJSON() ([]byte, error)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Float32.MarshalJSON)
    *   [func (x *Float32) Store(val float32)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Float32.Store)
    *   [func (f *Float32) String() string](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Float32.String)
    *   [func (f *Float32) Sub(delta float32) float32](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Float32.Sub)
    *   [func (x *Float32) Swap(val float32) (old float32)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Float32.Swap)
    *   [func (x *Float32) UnmarshalJSON(b []byte) error](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Float32.UnmarshalJSON)

*   [type Float64](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Float64)
*       *   [func NewFloat64(val float64) *Float64](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#NewFloat64)

*       *   [func (f *Float64) Add(delta float64) float64](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Float64.Add)
    *   [func (f *Float64) CAS(old, new float64) (swapped bool)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Float64.CAS)deprecated
    *   [func (f *Float64) CompareAndSwap(old, new float64) (swapped bool)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Float64.CompareAndSwap)
    *   [func (x *Float64) Load() float64](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Float64.Load)
    *   [func (x *Float64) MarshalJSON() ([]byte, error)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Float64.MarshalJSON)
    *   [func (x *Float64) Store(val float64)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Float64.Store)
    *   [func (f *Float64) String() string](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Float64.String)
    *   [func (f *Float64) Sub(delta float64) float64](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Float64.Sub)
    *   [func (x *Float64) Swap(val float64) (old float64)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Float64.Swap)
    *   [func (x *Float64) UnmarshalJSON(b []byte) error](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Float64.UnmarshalJSON)

*   [type Int32](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Int32)
*       *   [func NewInt32(val int32) *Int32](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#NewInt32)

*       *   [func (i *Int32) Add(delta int32) int32](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Int32.Add)
    *   [func (i *Int32) CAS(old, new int32) (swapped bool)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Int32.CAS)deprecated
    *   [func (i *Int32) CompareAndSwap(old, new int32) (swapped bool)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Int32.CompareAndSwap)
    *   [func (i *Int32) Dec() int32](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Int32.Dec)
    *   [func (i *Int32) Inc() int32](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Int32.Inc)
    *   [func (i *Int32) Load() int32](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Int32.Load)
    *   [func (i *Int32) MarshalJSON() ([]byte, error)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Int32.MarshalJSON)
    *   [func (i *Int32) Store(val int32)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Int32.Store)
    *   [func (i *Int32) String() string](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Int32.String)
    *   [func (i *Int32) Sub(delta int32) int32](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Int32.Sub)
    *   [func (i *Int32) Swap(val int32) (old int32)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Int32.Swap)
    *   [func (i *Int32) UnmarshalJSON(b []byte) error](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Int32.UnmarshalJSON)

*   [type Int64](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Int64)
*       *   [func NewInt64(val int64) *Int64](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#NewInt64)

*       *   [func (i *Int64) Add(delta int64) int64](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Int64.Add)
    *   [func (i *Int64) CAS(old, new int64) (swapped bool)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Int64.CAS)deprecated
    *   [func (i *Int64) CompareAndSwap(old, new int64) (swapped bool)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Int64.CompareAndSwap)
    *   [func (i *Int64) Dec() int64](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Int64.Dec)
    *   [func (i *Int64) Inc() int64](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Int64.Inc)
    *   [func (i *Int64) Load() int64](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Int64.Load)
    *   [func (i *Int64) MarshalJSON() ([]byte, error)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Int64.MarshalJSON)
    *   [func (i *Int64) Store(val int64)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Int64.Store)
    *   [func (i *Int64) String() string](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Int64.String)
    *   [func (i *Int64) Sub(delta int64) int64](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Int64.Sub)
    *   [func (i *Int64) Swap(val int64) (old int64)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Int64.Swap)
    *   [func (i *Int64) UnmarshalJSON(b []byte) error](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Int64.UnmarshalJSON)

*   [type Pointer](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Pointer)
*       *   [func NewPointer[T any](v *T) *Pointer[T]](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#NewPointer)

*       *   [func (p *Pointer[T]) CompareAndSwap(old, new *T) (swapped bool)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Pointer.CompareAndSwap)
    *   [func (p *Pointer[T]) Load() *T](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Pointer.Load)
    *   [func (p *Pointer[T]) Store(val *T)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Pointer.Store)
    *   [func (p *Pointer[T]) String() string](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Pointer.String)
    *   [func (p *Pointer[T]) Swap(val *T) (old *T)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Pointer.Swap)

*   [type String](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#String)
*       *   [func NewString(val string) *String](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#NewString)

*       *   [func (x *String) CompareAndSwap(old, new string) (swapped bool)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#String.CompareAndSwap)
    *   [func (x *String) Load() string](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#String.Load)
    *   [func (s *String) MarshalText() ([]byte, error)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#String.MarshalText)
    *   [func (x *String) Store(val string)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#String.Store)
    *   [func (s *String) String() string](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#String.String)
    *   [func (x *String) Swap(val string) (old string)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#String.Swap)
    *   [func (s *String) UnmarshalText(b []byte) error](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#String.UnmarshalText)

*   [type Time](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Time)
*       *   [func NewTime(val time.Time) *Time](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#NewTime)

*       *   [func (x *Time) Load() time.Time](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Time.Load)
    *   [func (x *Time) Store(val time.Time)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Time.Store)

*   [type Uint32](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uint32)
*       *   [func NewUint32(val uint32) *Uint32](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#NewUint32)

*       *   [func (i *Uint32) Add(delta uint32) uint32](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uint32.Add)
    *   [func (i *Uint32) CAS(old, new uint32) (swapped bool)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uint32.CAS)deprecated
    *   [func (i *Uint32) CompareAndSwap(old, new uint32) (swapped bool)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uint32.CompareAndSwap)
    *   [func (i *Uint32) Dec() uint32](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uint32.Dec)
    *   [func (i *Uint32) Inc() uint32](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uint32.Inc)
    *   [func (i *Uint32) Load() uint32](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uint32.Load)
    *   [func (i *Uint32) MarshalJSON() ([]byte, error)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uint32.MarshalJSON)
    *   [func (i *Uint32) Store(val uint32)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uint32.Store)
    *   [func (i *Uint32) String() string](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uint32.String)
    *   [func (i *Uint32) Sub(delta uint32) uint32](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uint32.Sub)
    *   [func (i *Uint32) Swap(val uint32) (old uint32)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uint32.Swap)
    *   [func (i *Uint32) UnmarshalJSON(b []byte) error](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uint32.UnmarshalJSON)

*   [type Uint64](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uint64)
*       *   [func NewUint64(val uint64) *Uint64](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#NewUint64)

*       *   [func (i *Uint64) Add(delta uint64) uint64](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uint64.Add)
    *   [func (i *Uint64) CAS(old, new uint64) (swapped bool)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uint64.CAS)deprecated
    *   [func (i *Uint64) CompareAndSwap(old, new uint64) (swapped bool)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uint64.CompareAndSwap)
    *   [func (i *Uint64) Dec() uint64](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uint64.Dec)
    *   [func (i *Uint64) Inc() uint64](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uint64.Inc)
    *   [func (i *Uint64) Load() uint64](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uint64.Load)
    *   [func (i *Uint64) MarshalJSON() ([]byte, error)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uint64.MarshalJSON)
    *   [func (i *Uint64) Store(val uint64)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uint64.Store)
    *   [func (i *Uint64) String() string](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uint64.String)
    *   [func (i *Uint64) Sub(delta uint64) uint64](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uint64.Sub)
    *   [func (i *Uint64) Swap(val uint64) (old uint64)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uint64.Swap)
    *   [func (i *Uint64) UnmarshalJSON(b []byte) error](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uint64.UnmarshalJSON)

*   [type Uintptr](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uintptr)
*       *   [func NewUintptr(val uintptr) *Uintptr](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#NewUintptr)

*       *   [func (i *Uintptr) Add(delta uintptr) uintptr](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uintptr.Add)
    *   [func (i *Uintptr) CAS(old, new uintptr) (swapped bool)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uintptr.CAS)deprecated
    *   [func (i *Uintptr) CompareAndSwap(old, new uintptr) (swapped bool)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uintptr.CompareAndSwap)
    *   [func (i *Uintptr) Dec() uintptr](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uintptr.Dec)
    *   [func (i *Uintptr) Inc() uintptr](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uintptr.Inc)
    *   [func (i *Uintptr) Load() uintptr](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uintptr.Load)
    *   [func (i *Uintptr) MarshalJSON() ([]byte, error)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uintptr.MarshalJSON)
    *   [func (i *Uintptr) Store(val uintptr)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uintptr.Store)
    *   [func (i *Uintptr) String() string](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uintptr.String)
    *   [func (i *Uintptr) Sub(delta uintptr) uintptr](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uintptr.Sub)
    *   [func (i *Uintptr) Swap(val uintptr) (old uintptr)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uintptr.Swap)
    *   [func (i *Uintptr) UnmarshalJSON(b []byte) error](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uintptr.UnmarshalJSON)

*   [type UnsafePointer](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#UnsafePointer)
*       *   [func NewUnsafePointer(val unsafe.Pointer) *UnsafePointer](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#NewUnsafePointer)

*       *   [func (p *UnsafePointer) CAS(old, new unsafe.Pointer) (swapped bool)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#UnsafePointer.CAS)deprecated
    *   [func (p *UnsafePointer) CompareAndSwap(old, new unsafe.Pointer) (swapped bool)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#UnsafePointer.CompareAndSwap)
    *   [func (p *UnsafePointer) Load() unsafe.Pointer](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#UnsafePointer.Load)
    *   [func (p *UnsafePointer) Store(val unsafe.Pointer)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#UnsafePointer.Store)
    *   [func (p *UnsafePointer) Swap(val unsafe.Pointer) (old unsafe.Pointer)](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#UnsafePointer.Swap)

*   [type Value](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Value)

### Examples [¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#pkg-examples "Go to Examples")

*   [Package](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#example-package)

### Constants [¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#pkg-constants "Go to Constants")

This section is empty.

### Variables [¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#pkg-variables "Go to Variables")

This section is empty.

### Functions [¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#pkg-functions "Go to Functions")

This section is empty.

### Types [¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#pkg-types "Go to Types")

#### type [Bool](https://github.com/uber-go/atomic/blob/v1.11.0/bool.go#L30)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Bool "Go to Bool")

type Bool struct {
	// contains filtered or unexported fields
}

Bool is an atomic type-safe wrapper for bool values.

#### func [NewBool](https://github.com/uber-go/atomic/blob/v1.11.0/bool.go#L39)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#NewBool "Go to NewBool")

func NewBool(val [bool](https://pkg.go.dev/builtin#bool)) *[Bool](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Bool)

NewBool creates a new Bool.

#### func (*Bool) [CAS](https://github.com/uber-go/atomic/blob/v1.11.0/bool.go#L60)deprecated added in v1.3.0

func (x *[Bool](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Bool)) CAS(old, new [bool](https://pkg.go.dev/builtin#bool)) (swapped [bool](https://pkg.go.dev/builtin#bool))

CAS is an atomic compare-and-swap for bool values.

Deprecated: Use CompareAndSwap.

#### func (*Bool) [CompareAndSwap](https://github.com/uber-go/atomic/blob/v1.11.0/bool.go#L65)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Bool.CompareAndSwap "Go to Bool.CompareAndSwap")added in v1.10.0

func (x *[Bool](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Bool)) CompareAndSwap(old, new [bool](https://pkg.go.dev/builtin#bool)) (swapped [bool](https://pkg.go.dev/builtin#bool))

CompareAndSwap is an atomic compare-and-swap for bool values.

#### func (*Bool) [Load](https://github.com/uber-go/atomic/blob/v1.11.0/bool.go#L48)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Bool.Load "Go to Bool.Load")

func (x *[Bool](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Bool)) Load() [bool](https://pkg.go.dev/builtin#bool)

Load atomically loads the wrapped bool.

#### func (*Bool) [MarshalJSON](https://github.com/uber-go/atomic/blob/v1.11.0/bool.go#L76)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Bool.MarshalJSON "Go to Bool.MarshalJSON")added in v1.7.0

func (x *[Bool](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Bool)) MarshalJSON() ([][byte](https://pkg.go.dev/builtin#byte), [error](https://pkg.go.dev/builtin#error))

MarshalJSON encodes the wrapped bool into JSON.

#### func (*Bool) [Store](https://github.com/uber-go/atomic/blob/v1.11.0/bool.go#L53)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Bool.Store "Go to Bool.Store")

func (x *[Bool](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Bool)) Store(val [bool](https://pkg.go.dev/builtin#bool))

Store atomically stores the passed bool.

#### func (*Bool) [String](https://github.com/uber-go/atomic/blob/v1.11.0/bool_ext.go#L51)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Bool.String "Go to Bool.String")added in v1.7.0

func (b *[Bool](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Bool)) String() [string](https://pkg.go.dev/builtin#string)

String encodes the wrapped value as a string.

#### func (*Bool) [Swap](https://github.com/uber-go/atomic/blob/v1.11.0/bool.go#L71)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Bool.Swap "Go to Bool.Swap")

func (x *[Bool](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Bool)) Swap(val [bool](https://pkg.go.dev/builtin#bool)) (old [bool](https://pkg.go.dev/builtin#bool))

Swap atomically stores the given bool and returns the old value.

#### func (*Bool) [Toggle](https://github.com/uber-go/atomic/blob/v1.11.0/bool_ext.go#L41)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Bool.Toggle "Go to Bool.Toggle")

func (b *[Bool](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Bool)) Toggle() (old [bool](https://pkg.go.dev/builtin#bool))

Toggle atomically negates the Boolean and returns the previous value.

#### func (*Bool) [UnmarshalJSON](https://github.com/uber-go/atomic/blob/v1.11.0/bool.go#L81)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Bool.UnmarshalJSON "Go to Bool.UnmarshalJSON")added in v1.7.0

func (x *[Bool](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Bool)) UnmarshalJSON(b [][byte](https://pkg.go.dev/builtin#byte)) [error](https://pkg.go.dev/builtin#error)

UnmarshalJSON decodes a bool from JSON.

#### type [Duration](https://github.com/uber-go/atomic/blob/v1.11.0/duration.go#L31)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Duration "Go to Duration")added in v1.3.2

type Duration struct {
	// contains filtered or unexported fields
}

Duration is an atomic type-safe wrapper for time.Duration values.

#### func [NewDuration](https://github.com/uber-go/atomic/blob/v1.11.0/duration.go#L40)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#NewDuration "Go to NewDuration")added in v1.3.2

func NewDuration(val [time](https://pkg.go.dev/time).[Duration](https://pkg.go.dev/time#Duration)) *[Duration](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Duration)

NewDuration creates a new Duration.

#### func (*Duration) [Add](https://github.com/uber-go/atomic/blob/v1.11.0/duration_ext.go#L28)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Duration.Add "Go to Duration.Add")added in v1.3.2

func (d *[Duration](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Duration)) Add(delta [time](https://pkg.go.dev/time).[Duration](https://pkg.go.dev/time#Duration)) [time](https://pkg.go.dev/time).[Duration](https://pkg.go.dev/time#Duration)

Add atomically adds to the wrapped time.Duration and returns the new value.

#### func (*Duration) [CAS](https://github.com/uber-go/atomic/blob/v1.11.0/duration.go#L61)deprecated added in v1.3.2

func (x *[Duration](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Duration)) CAS(old, new [time](https://pkg.go.dev/time).[Duration](https://pkg.go.dev/time#Duration)) (swapped [bool](https://pkg.go.dev/builtin#bool))

CAS is an atomic compare-and-swap for time.Duration values.

Deprecated: Use CompareAndSwap.

#### func (*Duration) [CompareAndSwap](https://github.com/uber-go/atomic/blob/v1.11.0/duration.go#L66)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Duration.CompareAndSwap "Go to Duration.CompareAndSwap")added in v1.10.0

func (x *[Duration](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Duration)) CompareAndSwap(old, new [time](https://pkg.go.dev/time).[Duration](https://pkg.go.dev/time#Duration)) (swapped [bool](https://pkg.go.dev/builtin#bool))

CompareAndSwap is an atomic compare-and-swap for time.Duration values.

#### func (*Duration) [Load](https://github.com/uber-go/atomic/blob/v1.11.0/duration.go#L49)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Duration.Load "Go to Duration.Load")added in v1.3.2

func (x *[Duration](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Duration)) Load() [time](https://pkg.go.dev/time).[Duration](https://pkg.go.dev/time#Duration)

Load atomically loads the wrapped time.Duration.

#### func (*Duration) [MarshalJSON](https://github.com/uber-go/atomic/blob/v1.11.0/duration.go#L77)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Duration.MarshalJSON "Go to Duration.MarshalJSON")added in v1.7.0

func (x *[Duration](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Duration)) MarshalJSON() ([][byte](https://pkg.go.dev/builtin#byte), [error](https://pkg.go.dev/builtin#error))

MarshalJSON encodes the wrapped time.Duration into JSON.

#### func (*Duration) [Store](https://github.com/uber-go/atomic/blob/v1.11.0/duration.go#L54)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Duration.Store "Go to Duration.Store")added in v1.3.2

func (x *[Duration](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Duration)) Store(val [time](https://pkg.go.dev/time).[Duration](https://pkg.go.dev/time#Duration))

Store atomically stores the passed time.Duration.

#### func (*Duration) [String](https://github.com/uber-go/atomic/blob/v1.11.0/duration_ext.go#L38)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Duration.String "Go to Duration.String")added in v1.7.0

func (d *[Duration](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Duration)) String() [string](https://pkg.go.dev/builtin#string)

String encodes the wrapped value as a string.

#### func (*Duration) [Sub](https://github.com/uber-go/atomic/blob/v1.11.0/duration_ext.go#L33)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Duration.Sub "Go to Duration.Sub")added in v1.3.2

func (d *[Duration](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Duration)) Sub(delta [time](https://pkg.go.dev/time).[Duration](https://pkg.go.dev/time#Duration)) [time](https://pkg.go.dev/time).[Duration](https://pkg.go.dev/time#Duration)

Sub atomically subtracts from the wrapped time.Duration and returns the new value.

#### func (*Duration) [Swap](https://github.com/uber-go/atomic/blob/v1.11.0/duration.go#L72)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Duration.Swap "Go to Duration.Swap")added in v1.3.2

func (x *[Duration](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Duration)) Swap(val [time](https://pkg.go.dev/time).[Duration](https://pkg.go.dev/time#Duration)) (old [time](https://pkg.go.dev/time).[Duration](https://pkg.go.dev/time#Duration))

Swap atomically stores the given time.Duration and returns the old value.

#### func (*Duration) [UnmarshalJSON](https://github.com/uber-go/atomic/blob/v1.11.0/duration.go#L82)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Duration.UnmarshalJSON "Go to Duration.UnmarshalJSON")added in v1.7.0

func (x *[Duration](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Duration)) UnmarshalJSON(b [][byte](https://pkg.go.dev/builtin#byte)) [error](https://pkg.go.dev/builtin#error)

UnmarshalJSON decodes a time.Duration from JSON.

#### type [Error](https://github.com/uber-go/atomic/blob/v1.11.0/error.go#L26)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Error "Go to Error")added in v1.4.0

type Error struct {
	// contains filtered or unexported fields
}

Error is an atomic type-safe wrapper for error values.

#### func [NewError](https://github.com/uber-go/atomic/blob/v1.11.0/error.go#L35)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#NewError "Go to NewError")added in v1.4.0

func NewError(val [error](https://pkg.go.dev/builtin#error)) *[Error](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Error)

NewError creates a new Error.

#### func (*Error) [CompareAndSwap](https://github.com/uber-go/atomic/blob/v1.11.0/error.go#L54)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Error.CompareAndSwap "Go to Error.CompareAndSwap")added in v1.10.0

func (x *[Error](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Error)) CompareAndSwap(old, new [error](https://pkg.go.dev/builtin#error)) (swapped [bool](https://pkg.go.dev/builtin#bool))

CompareAndSwap is an atomic compare-and-swap for error values.

#### func (*Error) [Load](https://github.com/uber-go/atomic/blob/v1.11.0/error.go#L44)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Error.Load "Go to Error.Load")added in v1.4.0

func (x *[Error](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Error)) Load() [error](https://pkg.go.dev/builtin#error)

Load atomically loads the wrapped error.

#### func (*Error) [Store](https://github.com/uber-go/atomic/blob/v1.11.0/error.go#L49)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Error.Store "Go to Error.Store")added in v1.4.0

func (x *[Error](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Error)) Store(val [error](https://pkg.go.dev/builtin#error))

Store atomically stores the passed error.

#### func (*Error) [Swap](https://github.com/uber-go/atomic/blob/v1.11.0/error.go#L70)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Error.Swap "Go to Error.Swap")added in v1.10.0

func (x *[Error](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Error)) Swap(val [error](https://pkg.go.dev/builtin#error)) (old [error](https://pkg.go.dev/builtin#error))

Swap atomically stores the given error and returns the old value.

#### type [Float32](https://github.com/uber-go/atomic/blob/v1.11.0/float32.go#L31)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Float32 "Go to Float32")added in v1.10.0

type Float32 struct {
	// contains filtered or unexported fields
}

Float32 is an atomic type-safe wrapper for float32 values.

#### func [NewFloat32](https://github.com/uber-go/atomic/blob/v1.11.0/float32.go#L40)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#NewFloat32 "Go to NewFloat32")added in v1.10.0

func NewFloat32(val [float32](https://pkg.go.dev/builtin#float32)) *[Float32](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Float32)

NewFloat32 creates a new Float32.

#### func (*Float32) [Add](https://github.com/uber-go/atomic/blob/v1.11.0/float32_ext.go#L31)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Float32.Add "Go to Float32.Add")added in v1.10.0

func (f *[Float32](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Float32)) Add(delta [float32](https://pkg.go.dev/builtin#float32)) [float32](https://pkg.go.dev/builtin#float32)

Add atomically adds to the wrapped float32 and returns the new value.

#### func (*Float32) [CAS](https://github.com/uber-go/atomic/blob/v1.11.0/float32_ext.go#L49)deprecated added in v1.10.0

func (f *[Float32](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Float32)) CAS(old, new [float32](https://pkg.go.dev/builtin#float32)) (swapped [bool](https://pkg.go.dev/builtin#bool))

CAS is an atomic compare-and-swap for float32 values.

Deprecated: Use CompareAndSwap

#### func (*Float32) [CompareAndSwap](https://github.com/uber-go/atomic/blob/v1.11.0/float32_ext.go#L68)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Float32.CompareAndSwap "Go to Float32.CompareAndSwap")added in v1.10.0

func (f *[Float32](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Float32)) CompareAndSwap(old, new [float32](https://pkg.go.dev/builtin#float32)) (swapped [bool](https://pkg.go.dev/builtin#bool))

CompareAndSwap is an atomic compare-and-swap for float32 values.

Note: CompareAndSwap handles NaN incorrectly. NaN != NaN using Go's inbuilt operators but CompareAndSwap allows a stored NaN to compare equal to a passed in NaN. This avoids typical CompareAndSwap loops from blocking forever, e.g.,

for {
  old := atom.Load()
  new = f(old)
  if atom.CompareAndSwap(old, new) {
    break
  }
}

If CompareAndSwap did not match NaN to match, then the above would loop forever.

#### func (*Float32) [Load](https://github.com/uber-go/atomic/blob/v1.11.0/float32.go#L49)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Float32.Load "Go to Float32.Load")added in v1.10.0

func (x *[Float32](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Float32)) Load() [float32](https://pkg.go.dev/builtin#float32)

Load atomically loads the wrapped float32.

#### func (*Float32) [MarshalJSON](https://github.com/uber-go/atomic/blob/v1.11.0/float32.go#L65)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Float32.MarshalJSON "Go to Float32.MarshalJSON")added in v1.10.0

func (x *[Float32](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Float32)) MarshalJSON() ([][byte](https://pkg.go.dev/builtin#byte), [error](https://pkg.go.dev/builtin#error))

MarshalJSON encodes the wrapped float32 into JSON.

#### func (*Float32) [Store](https://github.com/uber-go/atomic/blob/v1.11.0/float32.go#L54)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Float32.Store "Go to Float32.Store")added in v1.10.0

func (x *[Float32](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Float32)) Store(val [float32](https://pkg.go.dev/builtin#float32))

Store atomically stores the passed float32.

#### func (*Float32) [String](https://github.com/uber-go/atomic/blob/v1.11.0/float32_ext.go#L73)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Float32.String "Go to Float32.String")added in v1.10.0

func (f *[Float32](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Float32)) String() [string](https://pkg.go.dev/builtin#string)

String encodes the wrapped value as a string.

#### func (*Float32) [Sub](https://github.com/uber-go/atomic/blob/v1.11.0/float32_ext.go#L42)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Float32.Sub "Go to Float32.Sub")added in v1.10.0

func (f *[Float32](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Float32)) Sub(delta [float32](https://pkg.go.dev/builtin#float32)) [float32](https://pkg.go.dev/builtin#float32)

Sub atomically subtracts from the wrapped float32 and returns the new value.

#### func (*Float32) [Swap](https://github.com/uber-go/atomic/blob/v1.11.0/float32.go#L60)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Float32.Swap "Go to Float32.Swap")added in v1.10.0

func (x *[Float32](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Float32)) Swap(val [float32](https://pkg.go.dev/builtin#float32)) (old [float32](https://pkg.go.dev/builtin#float32))

Swap atomically stores the given float32 and returns the old value.

#### func (*Float32) [UnmarshalJSON](https://github.com/uber-go/atomic/blob/v1.11.0/float32.go#L70)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Float32.UnmarshalJSON "Go to Float32.UnmarshalJSON")added in v1.10.0

func (x *[Float32](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Float32)) UnmarshalJSON(b [][byte](https://pkg.go.dev/builtin#byte)) [error](https://pkg.go.dev/builtin#error)

UnmarshalJSON decodes a float32 from JSON.

#### type [Float64](https://github.com/uber-go/atomic/blob/v1.11.0/float64.go#L31)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Float64 "Go to Float64")added in v1.1.0

type Float64 struct {
	// contains filtered or unexported fields
}

Float64 is an atomic type-safe wrapper for float64 values.

#### func [NewFloat64](https://github.com/uber-go/atomic/blob/v1.11.0/float64.go#L40)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#NewFloat64 "Go to NewFloat64")added in v1.1.0

func NewFloat64(val [float64](https://pkg.go.dev/builtin#float64)) *[Float64](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Float64)

NewFloat64 creates a new Float64.

#### func (*Float64) [Add](https://github.com/uber-go/atomic/blob/v1.11.0/float64_ext.go#L31)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Float64.Add "Go to Float64.Add")added in v1.1.0

func (f *[Float64](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Float64)) Add(delta [float64](https://pkg.go.dev/builtin#float64)) [float64](https://pkg.go.dev/builtin#float64)

Add atomically adds to the wrapped float64 and returns the new value.

#### func (*Float64) [CAS](https://github.com/uber-go/atomic/blob/v1.11.0/float64_ext.go#L49)deprecated added in v1.1.0

func (f *[Float64](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Float64)) CAS(old, new [float64](https://pkg.go.dev/builtin#float64)) (swapped [bool](https://pkg.go.dev/builtin#bool))

CAS is an atomic compare-and-swap for float64 values.

Deprecated: Use CompareAndSwap

#### func (*Float64) [CompareAndSwap](https://github.com/uber-go/atomic/blob/v1.11.0/float64_ext.go#L68)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Float64.CompareAndSwap "Go to Float64.CompareAndSwap")added in v1.10.0

func (f *[Float64](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Float64)) CompareAndSwap(old, new [float64](https://pkg.go.dev/builtin#float64)) (swapped [bool](https://pkg.go.dev/builtin#bool))

CompareAndSwap is an atomic compare-and-swap for float64 values.

Note: CompareAndSwap handles NaN incorrectly. NaN != NaN using Go's inbuilt operators but CompareAndSwap allows a stored NaN to compare equal to a passed in NaN. This avoids typical CompareAndSwap loops from blocking forever, e.g.,

for {
  old := atom.Load()
  new = f(old)
  if atom.CompareAndSwap(old, new) {
    break
  }
}

If CompareAndSwap did not match NaN to match, then the above would loop forever.

#### func (*Float64) [Load](https://github.com/uber-go/atomic/blob/v1.11.0/float64.go#L49)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Float64.Load "Go to Float64.Load")added in v1.1.0

func (x *[Float64](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Float64)) Load() [float64](https://pkg.go.dev/builtin#float64)

Load atomically loads the wrapped float64.

#### func (*Float64) [MarshalJSON](https://github.com/uber-go/atomic/blob/v1.11.0/float64.go#L65)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Float64.MarshalJSON "Go to Float64.MarshalJSON")added in v1.7.0

func (x *[Float64](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Float64)) MarshalJSON() ([][byte](https://pkg.go.dev/builtin#byte), [error](https://pkg.go.dev/builtin#error))

MarshalJSON encodes the wrapped float64 into JSON.

#### func (*Float64) [Store](https://github.com/uber-go/atomic/blob/v1.11.0/float64.go#L54)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Float64.Store "Go to Float64.Store")added in v1.1.0

func (x *[Float64](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Float64)) Store(val [float64](https://pkg.go.dev/builtin#float64))

Store atomically stores the passed float64.

#### func (*Float64) [String](https://github.com/uber-go/atomic/blob/v1.11.0/float64_ext.go#L73)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Float64.String "Go to Float64.String")added in v1.7.0

func (f *[Float64](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Float64)) String() [string](https://pkg.go.dev/builtin#string)

String encodes the wrapped value as a string.

#### func (*Float64) [Sub](https://github.com/uber-go/atomic/blob/v1.11.0/float64_ext.go#L42)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Float64.Sub "Go to Float64.Sub")added in v1.1.0

func (f *[Float64](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Float64)) Sub(delta [float64](https://pkg.go.dev/builtin#float64)) [float64](https://pkg.go.dev/builtin#float64)

Sub atomically subtracts from the wrapped float64 and returns the new value.

#### func (*Float64) [Swap](https://github.com/uber-go/atomic/blob/v1.11.0/float64.go#L60)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Float64.Swap "Go to Float64.Swap")added in v1.9.0

func (x *[Float64](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Float64)) Swap(val [float64](https://pkg.go.dev/builtin#float64)) (old [float64](https://pkg.go.dev/builtin#float64))

Swap atomically stores the given float64 and returns the old value.

#### func (*Float64) [UnmarshalJSON](https://github.com/uber-go/atomic/blob/v1.11.0/float64.go#L70)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Float64.UnmarshalJSON "Go to Float64.UnmarshalJSON")added in v1.7.0

func (x *[Float64](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Float64)) UnmarshalJSON(b [][byte](https://pkg.go.dev/builtin#byte)) [error](https://pkg.go.dev/builtin#error)

UnmarshalJSON decodes a float64 from JSON.

#### type [Int32](https://github.com/uber-go/atomic/blob/v1.11.0/int32.go#L32)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Int32 "Go to Int32")

type Int32 struct {
	// contains filtered or unexported fields
}

Int32 is an atomic wrapper around int32.

#### func [NewInt32](https://github.com/uber-go/atomic/blob/v1.11.0/int32.go#L39)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#NewInt32 "Go to NewInt32")

func NewInt32(val [int32](https://pkg.go.dev/builtin#int32)) *[Int32](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Int32)

NewInt32 creates a new Int32.

#### func (*Int32) [Add](https://github.com/uber-go/atomic/blob/v1.11.0/int32.go#L49)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Int32.Add "Go to Int32.Add")

func (i *[Int32](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Int32)) Add(delta [int32](https://pkg.go.dev/builtin#int32)) [int32](https://pkg.go.dev/builtin#int32)

Add atomically adds to the wrapped int32 and returns the new value.

#### func (*Int32) [CAS](https://github.com/uber-go/atomic/blob/v1.11.0/int32.go#L71)deprecated

func (i *[Int32](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Int32)) CAS(old, new [int32](https://pkg.go.dev/builtin#int32)) (swapped [bool](https://pkg.go.dev/builtin#bool))

CAS is an atomic compare-and-swap.

Deprecated: Use CompareAndSwap.

#### func (*Int32) [CompareAndSwap](https://github.com/uber-go/atomic/blob/v1.11.0/int32.go#L76)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Int32.CompareAndSwap "Go to Int32.CompareAndSwap")added in v1.10.0

func (i *[Int32](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Int32)) CompareAndSwap(old, new [int32](https://pkg.go.dev/builtin#int32)) (swapped [bool](https://pkg.go.dev/builtin#bool))

CompareAndSwap is an atomic compare-and-swap.

#### func (*Int32) [Dec](https://github.com/uber-go/atomic/blob/v1.11.0/int32.go#L64)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Int32.Dec "Go to Int32.Dec")

func (i *[Int32](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Int32)) Dec() [int32](https://pkg.go.dev/builtin#int32)

Dec atomically decrements the wrapped int32 and returns the new value.

#### func (*Int32) [Inc](https://github.com/uber-go/atomic/blob/v1.11.0/int32.go#L59)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Int32.Inc "Go to Int32.Inc")

func (i *[Int32](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Int32)) Inc() [int32](https://pkg.go.dev/builtin#int32)

Inc atomically increments the wrapped int32 and returns the new value.

#### func (*Int32) [Load](https://github.com/uber-go/atomic/blob/v1.11.0/int32.go#L44)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Int32.Load "Go to Int32.Load")

func (i *[Int32](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Int32)) Load() [int32](https://pkg.go.dev/builtin#int32)

Load atomically loads the wrapped value.

#### func (*Int32) [MarshalJSON](https://github.com/uber-go/atomic/blob/v1.11.0/int32.go#L91)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Int32.MarshalJSON "Go to Int32.MarshalJSON")added in v1.7.0

func (i *[Int32](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Int32)) MarshalJSON() ([][byte](https://pkg.go.dev/builtin#byte), [error](https://pkg.go.dev/builtin#error))

MarshalJSON encodes the wrapped int32 into JSON.

#### func (*Int32) [Store](https://github.com/uber-go/atomic/blob/v1.11.0/int32.go#L81)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Int32.Store "Go to Int32.Store")

func (i *[Int32](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Int32)) Store(val [int32](https://pkg.go.dev/builtin#int32))

Store atomically stores the passed value.

#### func (*Int32) [String](https://github.com/uber-go/atomic/blob/v1.11.0/int32.go#L106)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Int32.String "Go to Int32.String")added in v1.7.0

func (i *[Int32](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Int32)) String() [string](https://pkg.go.dev/builtin#string)

String encodes the wrapped value as a string.

#### func (*Int32) [Sub](https://github.com/uber-go/atomic/blob/v1.11.0/int32.go#L54)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Int32.Sub "Go to Int32.Sub")

func (i *[Int32](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Int32)) Sub(delta [int32](https://pkg.go.dev/builtin#int32)) [int32](https://pkg.go.dev/builtin#int32)

Sub atomically subtracts from the wrapped int32 and returns the new value.

#### func (*Int32) [Swap](https://github.com/uber-go/atomic/blob/v1.11.0/int32.go#L86)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Int32.Swap "Go to Int32.Swap")

func (i *[Int32](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Int32)) Swap(val [int32](https://pkg.go.dev/builtin#int32)) (old [int32](https://pkg.go.dev/builtin#int32))

Swap atomically swaps the wrapped int32 and returns the old value.

#### func (*Int32) [UnmarshalJSON](https://github.com/uber-go/atomic/blob/v1.11.0/int32.go#L96)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Int32.UnmarshalJSON "Go to Int32.UnmarshalJSON")added in v1.7.0

func (i *[Int32](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Int32)) UnmarshalJSON(b [][byte](https://pkg.go.dev/builtin#byte)) [error](https://pkg.go.dev/builtin#error)

UnmarshalJSON decodes JSON into the wrapped int32.

#### type [Int64](https://github.com/uber-go/atomic/blob/v1.11.0/int64.go#L32)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Int64 "Go to Int64")

type Int64 struct {
	// contains filtered or unexported fields
}

Int64 is an atomic wrapper around int64.

#### func [NewInt64](https://github.com/uber-go/atomic/blob/v1.11.0/int64.go#L39)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#NewInt64 "Go to NewInt64")

func NewInt64(val [int64](https://pkg.go.dev/builtin#int64)) *[Int64](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Int64)

NewInt64 creates a new Int64.

#### func (*Int64) [Add](https://github.com/uber-go/atomic/blob/v1.11.0/int64.go#L49)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Int64.Add "Go to Int64.Add")

func (i *[Int64](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Int64)) Add(delta [int64](https://pkg.go.dev/builtin#int64)) [int64](https://pkg.go.dev/builtin#int64)

Add atomically adds to the wrapped int64 and returns the new value.

#### func (*Int64) [CAS](https://github.com/uber-go/atomic/blob/v1.11.0/int64.go#L71)deprecated

func (i *[Int64](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Int64)) CAS(old, new [int64](https://pkg.go.dev/builtin#int64)) (swapped [bool](https://pkg.go.dev/builtin#bool))

CAS is an atomic compare-and-swap.

Deprecated: Use CompareAndSwap.

#### func (*Int64) [CompareAndSwap](https://github.com/uber-go/atomic/blob/v1.11.0/int64.go#L76)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Int64.CompareAndSwap "Go to Int64.CompareAndSwap")added in v1.10.0

func (i *[Int64](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Int64)) CompareAndSwap(old, new [int64](https://pkg.go.dev/builtin#int64)) (swapped [bool](https://pkg.go.dev/builtin#bool))

CompareAndSwap is an atomic compare-and-swap.

#### func (*Int64) [Dec](https://github.com/uber-go/atomic/blob/v1.11.0/int64.go#L64)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Int64.Dec "Go to Int64.Dec")

func (i *[Int64](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Int64)) Dec() [int64](https://pkg.go.dev/builtin#int64)

Dec atomically decrements the wrapped int64 and returns the new value.

#### func (*Int64) [Inc](https://github.com/uber-go/atomic/blob/v1.11.0/int64.go#L59)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Int64.Inc "Go to Int64.Inc")

func (i *[Int64](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Int64)) Inc() [int64](https://pkg.go.dev/builtin#int64)

Inc atomically increments the wrapped int64 and returns the new value.

#### func (*Int64) [Load](https://github.com/uber-go/atomic/blob/v1.11.0/int64.go#L44)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Int64.Load "Go to Int64.Load")

func (i *[Int64](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Int64)) Load() [int64](https://pkg.go.dev/builtin#int64)

Load atomically loads the wrapped value.

#### func (*Int64) [MarshalJSON](https://github.com/uber-go/atomic/blob/v1.11.0/int64.go#L91)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Int64.MarshalJSON "Go to Int64.MarshalJSON")added in v1.7.0

func (i *[Int64](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Int64)) MarshalJSON() ([][byte](https://pkg.go.dev/builtin#byte), [error](https://pkg.go.dev/builtin#error))

MarshalJSON encodes the wrapped int64 into JSON.

#### func (*Int64) [Store](https://github.com/uber-go/atomic/blob/v1.11.0/int64.go#L81)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Int64.Store "Go to Int64.Store")

func (i *[Int64](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Int64)) Store(val [int64](https://pkg.go.dev/builtin#int64))

Store atomically stores the passed value.

#### func (*Int64) [String](https://github.com/uber-go/atomic/blob/v1.11.0/int64.go#L106)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Int64.String "Go to Int64.String")added in v1.7.0

func (i *[Int64](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Int64)) String() [string](https://pkg.go.dev/builtin#string)

String encodes the wrapped value as a string.

#### func (*Int64) [Sub](https://github.com/uber-go/atomic/blob/v1.11.0/int64.go#L54)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Int64.Sub "Go to Int64.Sub")

func (i *[Int64](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Int64)) Sub(delta [int64](https://pkg.go.dev/builtin#int64)) [int64](https://pkg.go.dev/builtin#int64)

Sub atomically subtracts from the wrapped int64 and returns the new value.

#### func (*Int64) [Swap](https://github.com/uber-go/atomic/blob/v1.11.0/int64.go#L86)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Int64.Swap "Go to Int64.Swap")

func (i *[Int64](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Int64)) Swap(val [int64](https://pkg.go.dev/builtin#int64)) (old [int64](https://pkg.go.dev/builtin#int64))

Swap atomically swaps the wrapped int64 and returns the old value.

#### func (*Int64) [UnmarshalJSON](https://github.com/uber-go/atomic/blob/v1.11.0/int64.go#L96)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Int64.UnmarshalJSON "Go to Int64.UnmarshalJSON")added in v1.7.0

func (i *[Int64](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Int64)) UnmarshalJSON(b [][byte](https://pkg.go.dev/builtin#byte)) [error](https://pkg.go.dev/builtin#error)

UnmarshalJSON decodes JSON into the wrapped int64.

#### type [Pointer](https://github.com/uber-go/atomic/blob/v1.11.0/pointer_go119.go#L29)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Pointer "Go to Pointer")added in v1.10.0

type Pointer[T [any](https://pkg.go.dev/builtin#any)] struct {
	// contains filtered or unexported fields
}

Pointer is an atomic pointer of type *T.

#### func [NewPointer](https://github.com/uber-go/atomic/blob/v1.11.0/pointer_go119.go#L35)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#NewPointer "Go to NewPointer")added in v1.10.0

func NewPointer[T [any](https://pkg.go.dev/builtin#any)](v *T) *[Pointer](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Pointer)[T]

NewPointer creates a new Pointer.

#### func (*Pointer[T]) [CompareAndSwap](https://github.com/uber-go/atomic/blob/v1.11.0/pointer_go119.go#L59)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Pointer.CompareAndSwap "Go to Pointer.CompareAndSwap")added in v1.10.0

func (p *[Pointer](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Pointer)[T]) CompareAndSwap(old, new *T) (swapped [bool](https://pkg.go.dev/builtin#bool))

CompareAndSwap is an atomic compare-and-swap.

#### func (*Pointer[T]) [Load](https://github.com/uber-go/atomic/blob/v1.11.0/pointer_go119.go#L44)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Pointer.Load "Go to Pointer.Load")added in v1.10.0

func (p *[Pointer](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Pointer)[T]) Load() *T

Load atomically loads the wrapped value.

#### func (*Pointer[T]) [Store](https://github.com/uber-go/atomic/blob/v1.11.0/pointer_go119.go#L49)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Pointer.Store "Go to Pointer.Store")added in v1.10.0

func (p *[Pointer](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Pointer)[T]) Store(val *T)

Store atomically stores the passed value.

#### func (*Pointer[T]) [String](https://github.com/uber-go/atomic/blob/v1.11.0/pointer_go118.go#L29)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Pointer.String "Go to Pointer.String")added in v1.11.0

func (p *[Pointer](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Pointer)[T]) String() [string](https://pkg.go.dev/builtin#string)

String returns a human readable representation of a Pointer's underlying value.

#### func (*Pointer[T]) [Swap](https://github.com/uber-go/atomic/blob/v1.11.0/pointer_go119.go#L54)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Pointer.Swap "Go to Pointer.Swap")added in v1.10.0

func (p *[Pointer](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Pointer)[T]) Swap(val *T) (old *T)

Swap atomically swaps the wrapped pointer and returns the old value.

#### type [String](https://github.com/uber-go/atomic/blob/v1.11.0/string.go#L26)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#String "Go to String")

type String struct {
	// contains filtered or unexported fields
}

String is an atomic type-safe wrapper for string values.

#### func [NewString](https://github.com/uber-go/atomic/blob/v1.11.0/string.go#L35)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#NewString "Go to NewString")

func NewString(val [string](https://pkg.go.dev/builtin#string)) *[String](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#String)

NewString creates a new String.

#### func (*String) [CompareAndSwap](https://github.com/uber-go/atomic/blob/v1.11.0/string.go#L54)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#String.CompareAndSwap "Go to String.CompareAndSwap")added in v1.10.0

func (x *[String](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#String)) CompareAndSwap(old, new [string](https://pkg.go.dev/builtin#string)) (swapped [bool](https://pkg.go.dev/builtin#bool))

CompareAndSwap is an atomic compare-and-swap for string values.

#### func (*String) [Load](https://github.com/uber-go/atomic/blob/v1.11.0/string.go#L44)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#String.Load "Go to String.Load")

func (x *[String](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#String)) Load() [string](https://pkg.go.dev/builtin#string)

Load atomically loads the wrapped string.

#### func (*String) [MarshalText](https://github.com/uber-go/atomic/blob/v1.11.0/string_ext.go#L44)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#String.MarshalText "Go to String.MarshalText")added in v1.7.0

func (s *[String](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#String)) MarshalText() ([][byte](https://pkg.go.dev/builtin#byte), [error](https://pkg.go.dev/builtin#error))

MarshalText encodes the wrapped string into a textual form.

This makes it encodable as JSON, YAML, XML, and more.

#### func (*String) [Store](https://github.com/uber-go/atomic/blob/v1.11.0/string.go#L49)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#String.Store "Go to String.Store")

func (x *[String](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#String)) Store(val [string](https://pkg.go.dev/builtin#string))

Store atomically stores the passed string.

#### func (*String) [String](https://github.com/uber-go/atomic/blob/v1.11.0/string_ext.go#L37)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#String.String "Go to String.String")added in v1.7.0

func (s *[String](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#String)) String() [string](https://pkg.go.dev/builtin#string)

String returns the wrapped value.

#### func (*String) [Swap](https://github.com/uber-go/atomic/blob/v1.11.0/string.go#L70)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#String.Swap "Go to String.Swap")added in v1.10.0

func (x *[String](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#String)) Swap(val [string](https://pkg.go.dev/builtin#string)) (old [string](https://pkg.go.dev/builtin#string))

Swap atomically stores the given string and returns the old value.

#### func (*String) [UnmarshalText](https://github.com/uber-go/atomic/blob/v1.11.0/string_ext.go#L51)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#String.UnmarshalText "Go to String.UnmarshalText")added in v1.7.0

func (s *[String](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#String)) UnmarshalText(b [][byte](https://pkg.go.dev/builtin#byte)) [error](https://pkg.go.dev/builtin#error)

UnmarshalText decodes text and replaces the wrapped string with it.

This makes it decodable from JSON, YAML, XML, and more.

#### type [Time](https://github.com/uber-go/atomic/blob/v1.11.0/time.go#L30)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Time "Go to Time")added in v1.9.0

type Time struct {
	// contains filtered or unexported fields
}

Time is an atomic type-safe wrapper for time.Time values.

#### func [NewTime](https://github.com/uber-go/atomic/blob/v1.11.0/time.go#L39)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#NewTime "Go to NewTime")added in v1.9.0

func NewTime(val [time](https://pkg.go.dev/time).[Time](https://pkg.go.dev/time#Time)) *[Time](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Time)

NewTime creates a new Time.

#### func (*Time) [Load](https://github.com/uber-go/atomic/blob/v1.11.0/time.go#L48)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Time.Load "Go to Time.Load")added in v1.9.0

func (x *[Time](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Time)) Load() [time](https://pkg.go.dev/time).[Time](https://pkg.go.dev/time#Time)

Load atomically loads the wrapped time.Time.

#### func (*Time) [Store](https://github.com/uber-go/atomic/blob/v1.11.0/time.go#L53)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Time.Store "Go to Time.Store")added in v1.9.0

func (x *[Time](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Time)) Store(val [time](https://pkg.go.dev/time).[Time](https://pkg.go.dev/time#Time))

Store atomically stores the passed time.Time.

#### type [Uint32](https://github.com/uber-go/atomic/blob/v1.11.0/uint32.go#L32)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uint32 "Go to Uint32")

type Uint32 struct {
	// contains filtered or unexported fields
}

Uint32 is an atomic wrapper around uint32.

#### func [NewUint32](https://github.com/uber-go/atomic/blob/v1.11.0/uint32.go#L39)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#NewUint32 "Go to NewUint32")

func NewUint32(val [uint32](https://pkg.go.dev/builtin#uint32)) *[Uint32](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uint32)

NewUint32 creates a new Uint32.

#### func (*Uint32) [Add](https://github.com/uber-go/atomic/blob/v1.11.0/uint32.go#L49)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uint32.Add "Go to Uint32.Add")

func (i *[Uint32](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uint32)) Add(delta [uint32](https://pkg.go.dev/builtin#uint32)) [uint32](https://pkg.go.dev/builtin#uint32)

Add atomically adds to the wrapped uint32 and returns the new value.

#### func (*Uint32) [CAS](https://github.com/uber-go/atomic/blob/v1.11.0/uint32.go#L71)deprecated

func (i *[Uint32](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uint32)) CAS(old, new [uint32](https://pkg.go.dev/builtin#uint32)) (swapped [bool](https://pkg.go.dev/builtin#bool))

CAS is an atomic compare-and-swap.

Deprecated: Use CompareAndSwap.

#### func (*Uint32) [CompareAndSwap](https://github.com/uber-go/atomic/blob/v1.11.0/uint32.go#L76)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uint32.CompareAndSwap "Go to Uint32.CompareAndSwap")added in v1.10.0

func (i *[Uint32](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uint32)) CompareAndSwap(old, new [uint32](https://pkg.go.dev/builtin#uint32)) (swapped [bool](https://pkg.go.dev/builtin#bool))

CompareAndSwap is an atomic compare-and-swap.

#### func (*Uint32) [Dec](https://github.com/uber-go/atomic/blob/v1.11.0/uint32.go#L64)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uint32.Dec "Go to Uint32.Dec")

func (i *[Uint32](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uint32)) Dec() [uint32](https://pkg.go.dev/builtin#uint32)

Dec atomically decrements the wrapped uint32 and returns the new value.

#### func (*Uint32) [Inc](https://github.com/uber-go/atomic/blob/v1.11.0/uint32.go#L59)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uint32.Inc "Go to Uint32.Inc")

func (i *[Uint32](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uint32)) Inc() [uint32](https://pkg.go.dev/builtin#uint32)

Inc atomically increments the wrapped uint32 and returns the new value.

#### func (*Uint32) [Load](https://github.com/uber-go/atomic/blob/v1.11.0/uint32.go#L44)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uint32.Load "Go to Uint32.Load")

func (i *[Uint32](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uint32)) Load() [uint32](https://pkg.go.dev/builtin#uint32)

Load atomically loads the wrapped value.

#### func (*Uint32) [MarshalJSON](https://github.com/uber-go/atomic/blob/v1.11.0/uint32.go#L91)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uint32.MarshalJSON "Go to Uint32.MarshalJSON")added in v1.7.0

func (i *[Uint32](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uint32)) MarshalJSON() ([][byte](https://pkg.go.dev/builtin#byte), [error](https://pkg.go.dev/builtin#error))

MarshalJSON encodes the wrapped uint32 into JSON.

#### func (*Uint32) [Store](https://github.com/uber-go/atomic/blob/v1.11.0/uint32.go#L81)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uint32.Store "Go to Uint32.Store")

func (i *[Uint32](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uint32)) Store(val [uint32](https://pkg.go.dev/builtin#uint32))

Store atomically stores the passed value.

#### func (*Uint32) [String](https://github.com/uber-go/atomic/blob/v1.11.0/uint32.go#L106)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uint32.String "Go to Uint32.String")added in v1.7.0

func (i *[Uint32](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uint32)) String() [string](https://pkg.go.dev/builtin#string)

String encodes the wrapped value as a string.

#### func (*Uint32) [Sub](https://github.com/uber-go/atomic/blob/v1.11.0/uint32.go#L54)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uint32.Sub "Go to Uint32.Sub")

func (i *[Uint32](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uint32)) Sub(delta [uint32](https://pkg.go.dev/builtin#uint32)) [uint32](https://pkg.go.dev/builtin#uint32)

Sub atomically subtracts from the wrapped uint32 and returns the new value.

#### func (*Uint32) [Swap](https://github.com/uber-go/atomic/blob/v1.11.0/uint32.go#L86)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uint32.Swap "Go to Uint32.Swap")

func (i *[Uint32](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uint32)) Swap(val [uint32](https://pkg.go.dev/builtin#uint32)) (old [uint32](https://pkg.go.dev/builtin#uint32))

Swap atomically swaps the wrapped uint32 and returns the old value.

#### func (*Uint32) [UnmarshalJSON](https://github.com/uber-go/atomic/blob/v1.11.0/uint32.go#L96)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uint32.UnmarshalJSON "Go to Uint32.UnmarshalJSON")added in v1.7.0

func (i *[Uint32](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uint32)) UnmarshalJSON(b [][byte](https://pkg.go.dev/builtin#byte)) [error](https://pkg.go.dev/builtin#error)

UnmarshalJSON decodes JSON into the wrapped uint32.

#### type [Uint64](https://github.com/uber-go/atomic/blob/v1.11.0/uint64.go#L32)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uint64 "Go to Uint64")

type Uint64 struct {
	// contains filtered or unexported fields
}

Uint64 is an atomic wrapper around uint64.

#### func [NewUint64](https://github.com/uber-go/atomic/blob/v1.11.0/uint64.go#L39)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#NewUint64 "Go to NewUint64")

func NewUint64(val [uint64](https://pkg.go.dev/builtin#uint64)) *[Uint64](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uint64)

NewUint64 creates a new Uint64.

#### func (*Uint64) [Add](https://github.com/uber-go/atomic/blob/v1.11.0/uint64.go#L49)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uint64.Add "Go to Uint64.Add")

func (i *[Uint64](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uint64)) Add(delta [uint64](https://pkg.go.dev/builtin#uint64)) [uint64](https://pkg.go.dev/builtin#uint64)

Add atomically adds to the wrapped uint64 and returns the new value.

#### func (*Uint64) [CAS](https://github.com/uber-go/atomic/blob/v1.11.0/uint64.go#L71)deprecated

func (i *[Uint64](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uint64)) CAS(old, new [uint64](https://pkg.go.dev/builtin#uint64)) (swapped [bool](https://pkg.go.dev/builtin#bool))

CAS is an atomic compare-and-swap.

Deprecated: Use CompareAndSwap.

#### func (*Uint64) [CompareAndSwap](https://github.com/uber-go/atomic/blob/v1.11.0/uint64.go#L76)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uint64.CompareAndSwap "Go to Uint64.CompareAndSwap")added in v1.10.0

func (i *[Uint64](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uint64)) CompareAndSwap(old, new [uint64](https://pkg.go.dev/builtin#uint64)) (swapped [bool](https://pkg.go.dev/builtin#bool))

CompareAndSwap is an atomic compare-and-swap.

#### func (*Uint64) [Dec](https://github.com/uber-go/atomic/blob/v1.11.0/uint64.go#L64)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uint64.Dec "Go to Uint64.Dec")

func (i *[Uint64](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uint64)) Dec() [uint64](https://pkg.go.dev/builtin#uint64)

Dec atomically decrements the wrapped uint64 and returns the new value.

#### func (*Uint64) [Inc](https://github.com/uber-go/atomic/blob/v1.11.0/uint64.go#L59)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uint64.Inc "Go to Uint64.Inc")

func (i *[Uint64](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uint64)) Inc() [uint64](https://pkg.go.dev/builtin#uint64)

Inc atomically increments the wrapped uint64 and returns the new value.

#### func (*Uint64) [Load](https://github.com/uber-go/atomic/blob/v1.11.0/uint64.go#L44)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uint64.Load "Go to Uint64.Load")

func (i *[Uint64](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uint64)) Load() [uint64](https://pkg.go.dev/builtin#uint64)

Load atomically loads the wrapped value.

#### func (*Uint64) [MarshalJSON](https://github.com/uber-go/atomic/blob/v1.11.0/uint64.go#L91)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uint64.MarshalJSON "Go to Uint64.MarshalJSON")added in v1.7.0

func (i *[Uint64](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uint64)) MarshalJSON() ([][byte](https://pkg.go.dev/builtin#byte), [error](https://pkg.go.dev/builtin#error))

MarshalJSON encodes the wrapped uint64 into JSON.

#### func (*Uint64) [Store](https://github.com/uber-go/atomic/blob/v1.11.0/uint64.go#L81)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uint64.Store "Go to Uint64.Store")

func (i *[Uint64](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uint64)) Store(val [uint64](https://pkg.go.dev/builtin#uint64))

Store atomically stores the passed value.

#### func (*Uint64) [String](https://github.com/uber-go/atomic/blob/v1.11.0/uint64.go#L106)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uint64.String "Go to Uint64.String")added in v1.7.0

func (i *[Uint64](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uint64)) String() [string](https://pkg.go.dev/builtin#string)

String encodes the wrapped value as a string.

#### func (*Uint64) [Sub](https://github.com/uber-go/atomic/blob/v1.11.0/uint64.go#L54)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uint64.Sub "Go to Uint64.Sub")

func (i *[Uint64](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uint64)) Sub(delta [uint64](https://pkg.go.dev/builtin#uint64)) [uint64](https://pkg.go.dev/builtin#uint64)

Sub atomically subtracts from the wrapped uint64 and returns the new value.

#### func (*Uint64) [Swap](https://github.com/uber-go/atomic/blob/v1.11.0/uint64.go#L86)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uint64.Swap "Go to Uint64.Swap")

func (i *[Uint64](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uint64)) Swap(val [uint64](https://pkg.go.dev/builtin#uint64)) (old [uint64](https://pkg.go.dev/builtin#uint64))

Swap atomically swaps the wrapped uint64 and returns the old value.

#### func (*Uint64) [UnmarshalJSON](https://github.com/uber-go/atomic/blob/v1.11.0/uint64.go#L96)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uint64.UnmarshalJSON "Go to Uint64.UnmarshalJSON")added in v1.7.0

func (i *[Uint64](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uint64)) UnmarshalJSON(b [][byte](https://pkg.go.dev/builtin#byte)) [error](https://pkg.go.dev/builtin#error)

UnmarshalJSON decodes JSON into the wrapped uint64.

#### type [Uintptr](https://github.com/uber-go/atomic/blob/v1.11.0/uintptr.go#L32)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uintptr "Go to Uintptr")added in v1.8.0

type Uintptr struct {
	// contains filtered or unexported fields
}

Uintptr is an atomic wrapper around uintptr.

#### func [NewUintptr](https://github.com/uber-go/atomic/blob/v1.11.0/uintptr.go#L39)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#NewUintptr "Go to NewUintptr")added in v1.8.0

func NewUintptr(val [uintptr](https://pkg.go.dev/builtin#uintptr)) *[Uintptr](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uintptr)

NewUintptr creates a new Uintptr.

#### func (*Uintptr) [Add](https://github.com/uber-go/atomic/blob/v1.11.0/uintptr.go#L49)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uintptr.Add "Go to Uintptr.Add")added in v1.8.0

func (i *[Uintptr](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uintptr)) Add(delta [uintptr](https://pkg.go.dev/builtin#uintptr)) [uintptr](https://pkg.go.dev/builtin#uintptr)

Add atomically adds to the wrapped uintptr and returns the new value.

#### func (*Uintptr) [CAS](https://github.com/uber-go/atomic/blob/v1.11.0/uintptr.go#L71)deprecated added in v1.8.0

func (i *[Uintptr](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uintptr)) CAS(old, new [uintptr](https://pkg.go.dev/builtin#uintptr)) (swapped [bool](https://pkg.go.dev/builtin#bool))

CAS is an atomic compare-and-swap.

Deprecated: Use CompareAndSwap.

#### func (*Uintptr) [CompareAndSwap](https://github.com/uber-go/atomic/blob/v1.11.0/uintptr.go#L76)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uintptr.CompareAndSwap "Go to Uintptr.CompareAndSwap")added in v1.10.0

func (i *[Uintptr](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uintptr)) CompareAndSwap(old, new [uintptr](https://pkg.go.dev/builtin#uintptr)) (swapped [bool](https://pkg.go.dev/builtin#bool))

CompareAndSwap is an atomic compare-and-swap.

#### func (*Uintptr) [Dec](https://github.com/uber-go/atomic/blob/v1.11.0/uintptr.go#L64)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uintptr.Dec "Go to Uintptr.Dec")added in v1.8.0

func (i *[Uintptr](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uintptr)) Dec() [uintptr](https://pkg.go.dev/builtin#uintptr)

Dec atomically decrements the wrapped uintptr and returns the new value.

#### func (*Uintptr) [Inc](https://github.com/uber-go/atomic/blob/v1.11.0/uintptr.go#L59)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uintptr.Inc "Go to Uintptr.Inc")added in v1.8.0

func (i *[Uintptr](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uintptr)) Inc() [uintptr](https://pkg.go.dev/builtin#uintptr)

Inc atomically increments the wrapped uintptr and returns the new value.

#### func (*Uintptr) [Load](https://github.com/uber-go/atomic/blob/v1.11.0/uintptr.go#L44)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uintptr.Load "Go to Uintptr.Load")added in v1.8.0

func (i *[Uintptr](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uintptr)) Load() [uintptr](https://pkg.go.dev/builtin#uintptr)

Load atomically loads the wrapped value.

#### func (*Uintptr) [MarshalJSON](https://github.com/uber-go/atomic/blob/v1.11.0/uintptr.go#L91)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uintptr.MarshalJSON "Go to Uintptr.MarshalJSON")added in v1.8.0

func (i *[Uintptr](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uintptr)) MarshalJSON() ([][byte](https://pkg.go.dev/builtin#byte), [error](https://pkg.go.dev/builtin#error))

MarshalJSON encodes the wrapped uintptr into JSON.

#### func (*Uintptr) [Store](https://github.com/uber-go/atomic/blob/v1.11.0/uintptr.go#L81)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uintptr.Store "Go to Uintptr.Store")added in v1.8.0

func (i *[Uintptr](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uintptr)) Store(val [uintptr](https://pkg.go.dev/builtin#uintptr))

Store atomically stores the passed value.

#### func (*Uintptr) [String](https://github.com/uber-go/atomic/blob/v1.11.0/uintptr.go#L106)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uintptr.String "Go to Uintptr.String")added in v1.8.0

func (i *[Uintptr](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uintptr)) String() [string](https://pkg.go.dev/builtin#string)

String encodes the wrapped value as a string.

#### func (*Uintptr) [Sub](https://github.com/uber-go/atomic/blob/v1.11.0/uintptr.go#L54)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uintptr.Sub "Go to Uintptr.Sub")added in v1.8.0

func (i *[Uintptr](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uintptr)) Sub(delta [uintptr](https://pkg.go.dev/builtin#uintptr)) [uintptr](https://pkg.go.dev/builtin#uintptr)

Sub atomically subtracts from the wrapped uintptr and returns the new value.

#### func (*Uintptr) [Swap](https://github.com/uber-go/atomic/blob/v1.11.0/uintptr.go#L86)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uintptr.Swap "Go to Uintptr.Swap")added in v1.8.0

func (i *[Uintptr](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uintptr)) Swap(val [uintptr](https://pkg.go.dev/builtin#uintptr)) (old [uintptr](https://pkg.go.dev/builtin#uintptr))

Swap atomically swaps the wrapped uintptr and returns the old value.

#### func (*Uintptr) [UnmarshalJSON](https://github.com/uber-go/atomic/blob/v1.11.0/uintptr.go#L96)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uintptr.UnmarshalJSON "Go to Uintptr.UnmarshalJSON")added in v1.8.0

func (i *[Uintptr](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Uintptr)) UnmarshalJSON(b [][byte](https://pkg.go.dev/builtin#byte)) [error](https://pkg.go.dev/builtin#error)

UnmarshalJSON decodes JSON into the wrapped uintptr.

#### type [UnsafePointer](https://github.com/uber-go/atomic/blob/v1.11.0/unsafe_pointer.go#L29)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#UnsafePointer "Go to UnsafePointer")added in v1.8.0

type UnsafePointer struct {
	// contains filtered or unexported fields
}

UnsafePointer is an atomic wrapper around unsafe.Pointer.

#### func [NewUnsafePointer](https://github.com/uber-go/atomic/blob/v1.11.0/unsafe_pointer.go#L36)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#NewUnsafePointer "Go to NewUnsafePointer")added in v1.8.0

func NewUnsafePointer(val [unsafe](https://pkg.go.dev/unsafe).[Pointer](https://pkg.go.dev/unsafe#Pointer)) *[UnsafePointer](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#UnsafePointer)

NewUnsafePointer creates a new UnsafePointer.

#### func (*UnsafePointer) [CAS](https://github.com/uber-go/atomic/blob/v1.11.0/unsafe_pointer.go#L58)deprecated added in v1.8.0

func (p *[UnsafePointer](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#UnsafePointer)) CAS(old, new [unsafe](https://pkg.go.dev/unsafe).[Pointer](https://pkg.go.dev/unsafe#Pointer)) (swapped [bool](https://pkg.go.dev/builtin#bool))

CAS is an atomic compare-and-swap.

Deprecated: Use CompareAndSwap

#### func (*UnsafePointer) [CompareAndSwap](https://github.com/uber-go/atomic/blob/v1.11.0/unsafe_pointer.go#L63)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#UnsafePointer.CompareAndSwap "Go to UnsafePointer.CompareAndSwap")added in v1.10.0

func (p *[UnsafePointer](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#UnsafePointer)) CompareAndSwap(old, new [unsafe](https://pkg.go.dev/unsafe).[Pointer](https://pkg.go.dev/unsafe#Pointer)) (swapped [bool](https://pkg.go.dev/builtin#bool))

CompareAndSwap is an atomic compare-and-swap.

#### func (*UnsafePointer) [Load](https://github.com/uber-go/atomic/blob/v1.11.0/unsafe_pointer.go#L41)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#UnsafePointer.Load "Go to UnsafePointer.Load")added in v1.8.0

func (p *[UnsafePointer](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#UnsafePointer)) Load() [unsafe](https://pkg.go.dev/unsafe).[Pointer](https://pkg.go.dev/unsafe#Pointer)

Load atomically loads the wrapped value.

#### func (*UnsafePointer) [Store](https://github.com/uber-go/atomic/blob/v1.11.0/unsafe_pointer.go#L46)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#UnsafePointer.Store "Go to UnsafePointer.Store")added in v1.8.0

func (p *[UnsafePointer](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#UnsafePointer)) Store(val [unsafe](https://pkg.go.dev/unsafe).[Pointer](https://pkg.go.dev/unsafe#Pointer))

Store atomically stores the passed value.

#### func (*UnsafePointer) [Swap](https://github.com/uber-go/atomic/blob/v1.11.0/unsafe_pointer.go#L51)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#UnsafePointer.Swap "Go to UnsafePointer.Swap")added in v1.8.0

func (p *[UnsafePointer](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#UnsafePointer)) Swap(val [unsafe](https://pkg.go.dev/unsafe).[Pointer](https://pkg.go.dev/unsafe#Pointer)) (old [unsafe](https://pkg.go.dev/unsafe).[Pointer](https://pkg.go.dev/unsafe#Pointer))

Swap atomically swaps the wrapped unsafe.Pointer and returns the old value.

#### type [Value](https://github.com/uber-go/atomic/blob/v1.11.0/value.go#L27)[¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#Value "Go to Value")added in v1.2.0

type Value struct {
[atomic](https://pkg.go.dev/sync/atomic).[Value](https://pkg.go.dev/sync/atomic#Value)	// contains filtered or unexported fields
}

Value shadows the type of the same name from sync/atomic [https://godoc.org/sync/atomic#Value](https://godoc.org/sync/atomic#Value)

![Image 49](https://pkg.go.dev/static/shared/icon/insert_drive_file_gm_grey_24dp.svg) Source Files [¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#section-sourcefiles "Go to Source Files")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[View all Source files](https://github.com/uber-go/atomic/tree/v1.11.0)

*   [bool.go](https://github.com/uber-go/atomic/blob/v1.11.0/bool.go "bool.go")
*   [bool_ext.go](https://github.com/uber-go/atomic/blob/v1.11.0/bool_ext.go "bool_ext.go")
*   [doc.go](https://github.com/uber-go/atomic/blob/v1.11.0/doc.go "doc.go")
*   [duration.go](https://github.com/uber-go/atomic/blob/v1.11.0/duration.go "duration.go")
*   [duration_ext.go](https://github.com/uber-go/atomic/blob/v1.11.0/duration_ext.go "duration_ext.go")
*   [error.go](https://github.com/uber-go/atomic/blob/v1.11.0/error.go "error.go")
*   [error_ext.go](https://github.com/uber-go/atomic/blob/v1.11.0/error_ext.go "error_ext.go")
*   [float32.go](https://github.com/uber-go/atomic/blob/v1.11.0/float32.go "float32.go")
*   [float32_ext.go](https://github.com/uber-go/atomic/blob/v1.11.0/float32_ext.go "float32_ext.go")
*   [float64.go](https://github.com/uber-go/atomic/blob/v1.11.0/float64.go "float64.go")
*   [float64_ext.go](https://github.com/uber-go/atomic/blob/v1.11.0/float64_ext.go "float64_ext.go")
*   [gen.go](https://github.com/uber-go/atomic/blob/v1.11.0/gen.go "gen.go")
*   [int32.go](https://github.com/uber-go/atomic/blob/v1.11.0/int32.go "int32.go")
*   [int64.go](https://github.com/uber-go/atomic/blob/v1.11.0/int64.go "int64.go")
*   [nocmp.go](https://github.com/uber-go/atomic/blob/v1.11.0/nocmp.go "nocmp.go")
*   [pointer_go118.go](https://github.com/uber-go/atomic/blob/v1.11.0/pointer_go118.go "pointer_go118.go")
*   [pointer_go119.go](https://github.com/uber-go/atomic/blob/v1.11.0/pointer_go119.go "pointer_go119.go")
*   [string.go](https://github.com/uber-go/atomic/blob/v1.11.0/string.go "string.go")
*   [string_ext.go](https://github.com/uber-go/atomic/blob/v1.11.0/string_ext.go "string_ext.go")
*   [time.go](https://github.com/uber-go/atomic/blob/v1.11.0/time.go "time.go")
*   [time_ext.go](https://github.com/uber-go/atomic/blob/v1.11.0/time_ext.go "time_ext.go")
*   [uint32.go](https://github.com/uber-go/atomic/blob/v1.11.0/uint32.go "uint32.go")
*   [uint64.go](https://github.com/uber-go/atomic/blob/v1.11.0/uint64.go "uint64.go")
*   [uintptr.go](https://github.com/uber-go/atomic/blob/v1.11.0/uintptr.go "uintptr.go")
*   [unsafe_pointer.go](https://github.com/uber-go/atomic/blob/v1.11.0/unsafe_pointer.go "unsafe_pointer.go")
*   [value.go](https://github.com/uber-go/atomic/blob/v1.11.0/value.go "value.go")

![Image 50](https://pkg.go.dev/static/shared/icon/folder_gm_grey_24dp.svg) Directories [¶](https://pkg.go.dev/go.uber.org/atomic@v1.11.0#section-directories "Go to Directories")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

 Show internal Expand all

| Path | Synopsis |
| --- | --- |
| ![Image 51](https://pkg.go.dev/static/shared/icon/arrow_right_gm_grey_24dp.svg)internal |  |
| [gen-atomicint](https://pkg.go.dev/go.uber.org/atomic@v1.11.0/internal/gen-atomicint)command gen-atomicint generates an atomic wrapper around an integer type. | gen-atomicint generates an atomic wrapper around an integer type. |
| [gen-atomicwrapper](https://pkg.go.dev/go.uber.org/atomic@v1.11.0/internal/gen-atomicwrapper)command gen-atomicwrapper generates wrapper types around other atomic types. | gen-atomicwrapper generates wrapper types around other atomic types. |

 Click to show internal directories. 

 Click to hide internal directories. 

[Why Go](https://go.dev/solutions)[Use Cases](https://go.dev/solutions#use-cases)[Case Studies](https://go.dev/solutions#case-studies)

[Get Started](https://learn.go.dev/)[Playground](https://play.golang.org/)[Tour](https://tour.golang.org/)[Stack Overflow](https://stackoverflow.com/questions/tagged/go?tab=Newest)[Help](https://go.dev/help)

[Packages](https://pkg.go.dev/)[Standard Library](https://pkg.go.dev/std)[Sub-repositories](https://pkg.go.dev/golang.org/x)[About Go Packages](https://pkg.go.dev/about)

[About](https://go.dev/project)[Download](https://go.dev/dl/)[Blog](https://go.dev/blog)[Issue Tracker](https://github.com/golang/go/issues)[Release Notes](https://go.dev/doc/devel/release.html)[Brand Guidelines](https://go.dev/brand)[Code of Conduct](https://go.dev/conduct)

[Connect](https://www.twitter.com/golang)[Twitter](https://www.twitter.com/golang)[GitHub](https://github.com/golang)[Slack](https://invite.slack.golangbridge.org/)[r/golang](https://reddit.com/r/golang)[Meetup](https://www.meetup.com/pro/go)[Golang Weekly](https://golangweekly.com/)

![Image 52: Gopher in flight goggles](https://pkg.go.dev/static/shared/gopher/pilot-bust-1431x901.svg)
*   [Copyright](https://go.dev/copyright)
*   [Terms of Service](https://go.dev/tos)
*   [Privacy Policy](http://www.google.com/intl/en/policies/privacy/)
*   [Report an Issue](https://go.dev/s/pkgsite-feedback)
*   ![Image 53: System theme](https://pkg.go.dev/static/shared/icon/brightness_6_gm_grey_24dp.svg)![Image 54: Dark theme](https://pkg.go.dev/static/shared/icon/brightness_2_gm_grey_24dp.svg)![Image 55: Light theme](https://pkg.go.dev/static/shared/icon/light_mode_gm_grey_24dp.svg)
Theme Toggle

*   ![Image 56](https://pkg.go.dev/static/shared/icon/keyboard_grey_24dp.svg)
Shortcuts Modal

[![Image 57: Google logo](https://pkg.go.dev/static/shared/logo/google-white.svg)](https://google.com/)

Jump to
-------

![Image 58](https://pkg.go.dev/static/shared/icon/close_gm_grey_24dp.svg)

Close

Keyboard shortcuts
------------------

![Image 59](https://pkg.go.dev/static/shared/icon/close_gm_grey_24dp.svg)

**?**: This menu
**/**: Search site
**f** or **F**: Jump to
**y** or **Y**: Canonical URL

Close

go.dev uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay
