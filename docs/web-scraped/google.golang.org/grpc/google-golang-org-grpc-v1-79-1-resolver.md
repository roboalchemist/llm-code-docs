# Source: https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver

Title: resolver package - google.golang.org/grpc/resolver - Go Packages

URL Source: https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver

Markdown Content:
resolver package - google.golang.org/grpc/resolver - Go Packages
===============

[![Image 1: Go](https://pkg.go.dev/static/shared/logo/go-white.svg)](https://go.dev/)

[Skip to Main Content](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#main-content)

![Image 2](https://pkg.go.dev/static/shared/icon/search_gm_grey_24dp.svg)![Image 3](https://pkg.go.dev/static/shared/icon/search_gm_grey_24dp.svg)

*   [Why Go ![Image 4: submenu dropdown icon](https://pkg.go.dev/static/shared/icon/arrow_drop_down_gm_grey_24dp.svg)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#)
    *   [Case Studies](https://go.dev/solutions#case-studies) 
Common problems companies solve with Go

    *   [Use Cases](https://go.dev/solutions#use-cases) 
Stories about how and why companies use Go

    *   [Security](https://go.dev/security/) 
How Go can help keep you secure by default

*   [Learn](https://go.dev/learn/)
*   [Docs ![Image 5: submenu dropdown icon](https://pkg.go.dev/static/shared/icon/arrow_drop_down_gm_grey_24dp.svg)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#)
    *   [Effective Go](https://go.dev/doc/effective_go) 
Tips for writing clear, performant, and idiomatic Go code

    *   [Go User Manual](https://go.dev/doc/) 
A complete introduction to building software with Go

    *   [Standard library](https://pkg.go.dev/std) 
Reference documentation for Go's standard library

    *   [Release Notes](https://go.dev/doc/devel/release) 
Learn what's new in each Go release

*   [Packages](https://pkg.go.dev/)
*   [Community ![Image 6: submenu dropdown icon](https://pkg.go.dev/static/shared/icon/arrow_drop_down_gm_grey_24dp.svg)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#)
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

*   [Why Go _![Image 16](https://pkg.go.dev/static/shared/icon/navigate\_next\_gm\_grey\_24dp.svg)_](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#)

[_![Image 17](https://pkg.go.dev/static/shared/icon/navigate\_before\_gm\_grey\_24dp.svg)_ Why Go](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#) 
    *   [Case Studies](https://go.dev/solutions#case-studies)
    *   [Use Cases](https://go.dev/solutions#use-cases)
    *   [Security](https://go.dev/security/)

*   [Learn](https://go.dev/learn/)
*   [Docs _![Image 18](https://pkg.go.dev/static/shared/icon/navigate\_next\_gm\_grey\_24dp.svg)_](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#)

[_![Image 19](https://pkg.go.dev/static/shared/icon/navigate\_before\_gm\_grey\_24dp.svg)_ Docs](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#) 
    *   [Effective Go](https://go.dev/doc/effective_go)
    *   [Go User Manual](https://go.dev/doc/)
    *   [Standard library](https://pkg.go.dev/std)
    *   [Release Notes](https://go.dev/doc/devel/release)

*   [Packages](https://pkg.go.dev/)
*   [Community _![Image 20](https://pkg.go.dev/static/shared/icon/navigate\_next\_gm\_grey\_24dp.svg)_](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#)

[_![Image 21](https://pkg.go.dev/static/shared/icon/navigate\_before\_gm\_grey\_24dp.svg)_ Community](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#) 
    *   [Recorded Talks](https://go.dev/talks/)
    *   [Meetups _![Image 22](https://pkg.go.dev/static/shared/icon/launch\_gm\_grey\_24dp.svg)_](https://www.meetup.com/pro/go)
    *   [Conferences _![Image 23](https://pkg.go.dev/static/shared/icon/launch\_gm\_grey\_24dp.svg)_](https://github.com/golang/go/wiki/Conferences)
    *   [Go blog](https://go.dev/blog)
    *   [Go project](https://go.dev/help)
    *   Get connected [![Image 24](https://pkg.go.dev/static/shared/logo/social/google-groups.svg)](https://groups.google.com/g/golang-nuts)[![Image 25](https://pkg.go.dev/static/shared/logo/social/github.svg)](https://github.com/golang)[![Image 26](https://pkg.go.dev/static/shared/logo/social/twitter.svg)](https://twitter.com/golang)[![Image 27](https://pkg.go.dev/static/shared/logo/social/reddit.svg)](https://www.reddit.com/r/golang/)[![Image 28](https://pkg.go.dev/static/shared/logo/social/slack.svg)](https://invite.slack.golangbridge.org/)[![Image 29](https://pkg.go.dev/static/shared/logo/social/stack-overflow.svg)](https://stackoverflow.com/collectives/go) 

1.   [Discover Packages](https://pkg.go.dev/)
2.   [google.golang.org/grpc](https://pkg.go.dev/google.golang.org/grpc@v1.79.1)
3.   [resolver](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver)![Image 30](https://pkg.go.dev/static/shared/icon/content_copy_gm_grey_24dp.svg)

[![Image 31: Go](https://pkg.go.dev/static/shared/logo/go-blue.svg)](https://go.dev/)
resolver
========

package![Image 32](https://pkg.go.dev/static/shared/icon/content_copy_gm_grey_24dp.svg)

[Version: v1.79.1](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver?tab=versions)

 Opens a new window with list of versions in this module. 

Latest Latest 

![Image 33: Warning](https://pkg.go.dev/static/shared/icon/alert_gm_grey_24dp.svg)
This package is not in the latest version of its module.

[Go to latest](https://pkg.go.dev/google.golang.org/grpc/resolver) Published: Feb 13, 2026  License: [Apache-2.0](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver?tab=licenses)

 Opens a new window with license information. 

[Imports: 13](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver?tab=imports)

 Opens a new window with list of imports. 

[Imported by: 3,206](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver?tab=importedby)

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

*   [Documentation](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#section-documentation)
    *   [Overview](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#pkg-overview)
    *   [Index](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#pkg-index)
    *   [Constants](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#pkg-constants)
    *   [Variables](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#pkg-variables)
    *   [Functions](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#pkg-functions)
        *   [GetDefaultScheme()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#GetDefaultScheme "GetDefaultScheme()")
        *   [Register(b)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#Register "Register(b)")
        *   [SetDefaultScheme(scheme)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#SetDefaultScheme "SetDefaultScheme(scheme)")
        *   [ValidateEndpoints(endpoints)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#ValidateEndpoints "ValidateEndpoints(endpoints)")

    *   [Types](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#pkg-types)
        *   [type Address](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#Address "type Address")
            *   [(a) Equal(o)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#Address.Equal "(a) Equal(o)")
            *   [(a) String()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#Address.String "(a) String()")

        *   [type AddressMap](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#AddressMap "type AddressMap")
            *   [NewAddressMap()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#NewAddressMap "NewAddressMap()")

        *   [type AddressMapV2](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#AddressMapV2 "type AddressMapV2")
            *   [NewAddressMapV2()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#NewAddressMapV2 "NewAddressMapV2()")
            *   [(a) Delete(addr)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#AddressMapV2.Delete "(a) Delete(addr)")
            *   [(a) Get(addr)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#AddressMapV2.Get "(a) Get(addr)")
            *   [(a) Keys()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#AddressMapV2.Keys "(a) Keys()")
            *   [(a) Len()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#AddressMapV2.Len "(a) Len()")
            *   [(a) Set(addr, value)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#AddressMapV2.Set "(a) Set(addr, value)")
            *   [(a) Values()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#AddressMapV2.Values "(a) Values()")

        *   [type AuthorityOverrider](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#AuthorityOverrider "type AuthorityOverrider")
        *   [type BuildOptions](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#BuildOptions "type BuildOptions")
        *   [type Builder](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#Builder "type Builder")
            *   [Get(scheme)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#Get "Get(scheme)")

        *   [type ClientConn](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#ClientConn "type ClientConn")
        *   [type Endpoint](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#Endpoint "type Endpoint")
        *   [type EndpointMap](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#EndpointMap "type EndpointMap")
            *   [NewEndpointMap()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#NewEndpointMap "NewEndpointMap()")
            *   [(em) Delete(e)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#EndpointMap.Delete "(em) Delete(e)")
            *   [(em) Get(e)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#EndpointMap.Get "(em) Get(e)")
            *   [(em) Keys()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#EndpointMap.Keys "(em) Keys()")
            *   [(em) Len()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#EndpointMap.Len "(em) Len()")
            *   [(em) Set(e, value)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#EndpointMap.Set "(em) Set(e, value)")
            *   [(em) Values()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#EndpointMap.Values "(em) Values()")

        *   [type ResolveNowOptions](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#ResolveNowOptions "type ResolveNowOptions")
        *   [type Resolver](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#Resolver "type Resolver")
        *   [type State](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#State "type State")
        *   [type Target](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#Target "type Target")
            *   [(t) Endpoint()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#Target.Endpoint "(t) Endpoint()")
            *   [(t) String()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#Target.String "(t) String()")

*   [Source Files](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#section-sourcefiles)
*   [Directories](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#section-directories)

![Image 43](https://pkg.go.dev/static/shared/icon/code_gm_grey_24dp.svg) Documentation [¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#section-documentation "Go to Documentation")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Overview [¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#pkg-overview "Go to Overview")

Package resolver defines APIs for name resolution in gRPC. All APIs in this package are experimental.

### Index [¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#pkg-index "Go to Index")

*   [func GetDefaultScheme() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#GetDefaultScheme)
*   [func Register(b Builder)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#Register)
*   [func SetDefaultScheme(scheme string)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#SetDefaultScheme)
*   [func ValidateEndpoints(endpoints []Endpoint) error](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#ValidateEndpoints)
*   [type Address](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#Address)
*       *   [func (a Address) Equal(o Address) bool](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#Address.Equal)
    *   [func (a Address) String() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#Address.String)

*   [type AddressMap](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#AddressMap)deprecated
*       *   [func NewAddressMap() *AddressMap](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#NewAddressMap)deprecated

*   [type AddressMapV2](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#AddressMapV2)
*       *   [func NewAddressMapV2[T any]() *AddressMapV2[T]](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#NewAddressMapV2)

*       *   [func (a *AddressMapV2[T]) Delete(addr Address)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#AddressMapV2.Delete)
    *   [func (a *AddressMapV2[T]) Get(addr Address) (value T, ok bool)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#AddressMapV2.Get)
    *   [func (a *AddressMapV2[T]) Keys() []Address](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#AddressMapV2.Keys)
    *   [func (a *AddressMapV2[T]) Len() int](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#AddressMapV2.Len)
    *   [func (a *AddressMapV2[T]) Set(addr Address, value T)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#AddressMapV2.Set)
    *   [func (a *AddressMapV2[T]) Values() []T](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#AddressMapV2.Values)

*   [type AuthorityOverrider](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#AuthorityOverrider)
*   [type BuildOptions](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#BuildOptions)
*   [type Builder](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#Builder)
*       *   [func Get(scheme string) Builder](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#Get)

*   [type ClientConn](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#ClientConn)
*   [type Endpoint](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#Endpoint)
*   [type EndpointMap](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#EndpointMap)
*       *   [func NewEndpointMap[T any]() *EndpointMap[T]](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#NewEndpointMap)

*       *   [func (em *EndpointMap[T]) Delete(e Endpoint)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#EndpointMap.Delete)
    *   [func (em *EndpointMap[T]) Get(e Endpoint) (value T, ok bool)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#EndpointMap.Get)
    *   [func (em *EndpointMap[T]) Keys() []Endpoint](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#EndpointMap.Keys)
    *   [func (em *EndpointMap[T]) Len() int](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#EndpointMap.Len)
    *   [func (em *EndpointMap[T]) Set(e Endpoint, value T)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#EndpointMap.Set)
    *   [func (em *EndpointMap[T]) Values() []T](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#EndpointMap.Values)

*   [type ResolveNowOptions](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#ResolveNowOptions)
*   [type Resolver](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#Resolver)
*   [type State](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#State)
*   [type Target](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#Target)
*       *   [func (t Target) Endpoint() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#Target.Endpoint)
    *   [func (t Target) String() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#Target.String)

### Constants [¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#pkg-constants "Go to Constants")

This section is empty.

### Variables [¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#pkg-variables "Go to Variables")

This section is empty.

### Functions [¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#pkg-functions "Go to Functions")

#### func [GetDefaultScheme](https://github.com/grpc/grpc-go/blob/v1.79.1/resolver/resolver.go#L81)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#GetDefaultScheme "Go to GetDefaultScheme")added in v1.10.1

func GetDefaultScheme() [string](https://pkg.go.dev/builtin#string)

GetDefaultScheme gets the default scheme that will be used by grpc.Dial. If SetDefaultScheme is never called, the default scheme used by grpc.NewClient is "dns" instead.

#### func [Register](https://github.com/grpc/grpc-go/blob/v1.79.1/resolver/resolver.go#L54)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#Register "Go to Register")

func Register(b [Builder](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#Builder))

Register registers the resolver builder to the resolver map. b.Scheme will be used as the scheme registered with this builder. The registry is case sensitive, and schemes should not contain any uppercase characters.

NOTE: this function must only be called during initialization time (i.e. in an init() function), and is not thread-safe. If multiple Resolvers are registered with the same name, the one registered last will take effect.

#### func [SetDefaultScheme](https://github.com/grpc/grpc-go/blob/v1.79.1/resolver/resolver.go#L74)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#SetDefaultScheme "Go to SetDefaultScheme")

func SetDefaultScheme(scheme [string](https://pkg.go.dev/builtin#string))

SetDefaultScheme sets the default scheme that will be used. The default scheme is initially set to "passthrough".

NOTE: this function must only be called during initialization time (i.e. in an init() function), and is not thread-safe. The scheme set last overrides previously set values.

#### func [ValidateEndpoints](https://github.com/grpc/grpc-go/blob/v1.79.1/resolver/resolver.go#L348)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#ValidateEndpoints "Go to ValidateEndpoints")added in v1.69.0

func ValidateEndpoints(endpoints [][Endpoint](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#Endpoint)) [error](https://pkg.go.dev/builtin#error)

ValidateEndpoints validates endpoints from a petiole policy's perspective. Petiole policies should call this before calling into their children. See [gRPC A61]([https://github.com/grpc/proposal/blob/master/A61-IPv4-IPv6-dualstack-backends.md](https://github.com/grpc/proposal/blob/master/A61-IPv4-IPv6-dualstack-backends.md)) for details.

### Types [¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#pkg-types "Go to Types")

#### type [Address](https://github.com/grpc/grpc-go/blob/v1.79.1/resolver/resolver.go#L91)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#Address "Go to Address")

type Address struct {
// Addr is the server address on which a connection will be established.	Addr [string](https://pkg.go.dev/builtin#string)

// ServerName is the name of this address.	// If non-empty, the ServerName is used as the transport certification authority for
	// the address, instead of the hostname from the Dial target string. In most cases,
	// this should not be set.
	//
	// WARNING: ServerName must only be populated with trusted values. It
	// is insecure to populate it with data from untrusted inputs since untrusted
	// values could be used to bypass the authority checks performed by TLS.
	ServerName [string](https://pkg.go.dev/builtin#string)

// Attributes contains arbitrary data about this address intended for	// consumption by the SubConn.
	Attributes *[attributes](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/attributes).[Attributes](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/attributes#Attributes)

// BalancerAttributes contains arbitrary data about this address intended	// for consumption by the LB policy. These attributes do not affect SubConn
	// creation, connection establishment, handshaking, etc.
	//
	// Deprecated: when an Address is inside an Endpoint, this field should not
	// be used, and it will eventually be removed entirely.
	BalancerAttributes *[attributes](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/attributes).[Attributes](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/attributes#Attributes)

// Metadata is the information associated with Addr, which may be used	// to make load balancing decision.
	//
	// Deprecated: use Attributes instead.
	Metadata [any](https://pkg.go.dev/builtin#any)
}

*   [Experimental](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#hdr-Experimental-Address)

Address represents a server the client connects to.

#### Experimental [¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#hdr-Experimental-Address "Go to Experimental")

Notice: This type is EXPERIMENTAL and may be changed or removed in a later release.

#### func (Address) [Equal](https://github.com/grpc/grpc-go/blob/v1.79.1/resolver/resolver.go#L130)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#Address.Equal "Go to Address.Equal")added in v1.42.0

func (a [Address](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#Address)) Equal(o [Address](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#Address)) [bool](https://pkg.go.dev/builtin#bool)

Equal returns whether a and o are identical. Metadata is compared directly, not with any recursive introspection.

This method compares all fields of the address. When used to tell apart addresses during subchannel creation or connection establishment, it might be more appropriate for the caller to implement custom equality logic.

#### func (Address) [String](https://github.com/grpc/grpc-go/blob/v1.79.1/resolver/resolver.go#L138)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#Address.String "Go to Address.String")added in v1.46.0

func (a [Address](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#Address)) String() [string](https://pkg.go.dev/builtin#string)

String returns JSON formatted string representation of the address.

#### type [AddressMap](https://github.com/grpc/grpc-go/blob/v1.79.1/resolver/map.go#L36)deprecated added in v1.42.0

type AddressMap = [AddressMapV2](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#AddressMapV2)[[any](https://pkg.go.dev/builtin#any)]

AddressMap is an AddressMapV2[any]. It will be deleted in an upcoming release of grpc-go.

Deprecated: use the generic AddressMapV2 type instead.

#### func [NewAddressMap](https://github.com/grpc/grpc-go/blob/v1.79.1/resolver/map.go#L68)deprecated added in v1.42.0

func NewAddressMap() *[AddressMap](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#AddressMap)

NewAddressMap creates a new AddressMapV2[any].

Deprecated: use the generic NewAddressMapV2 constructor instead.

#### type [AddressMapV2](https://github.com/grpc/grpc-go/blob/v1.79.1/resolver/map.go#L42)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#AddressMapV2 "Go to AddressMapV2")added in v1.72.0

type AddressMapV2[T [any](https://pkg.go.dev/builtin#any)] struct {
	// contains filtered or unexported fields
}

AddressMapV2 is a map of addresses to arbitrary values taking into account Attributes. BalancerAttributes are ignored, as are Metadata and Type. Multiple accesses may not be performed concurrently. Must be created via NewAddressMap; do not construct directly.

#### func [NewAddressMapV2](https://github.com/grpc/grpc-go/blob/v1.79.1/resolver/map.go#L73)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#NewAddressMapV2 "Go to NewAddressMapV2")added in v1.72.0

func NewAddressMapV2[T [any](https://pkg.go.dev/builtin#any)]() *[AddressMapV2](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#AddressMapV2)[T]

NewAddressMapV2 creates a new AddressMapV2.

#### func (*AddressMapV2[T]) [Delete](https://github.com/grpc/grpc-go/blob/v1.79.1/resolver/map.go#L112)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#AddressMapV2.Delete "Go to AddressMapV2.Delete")added in v1.72.0

func (a *[AddressMapV2](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#AddressMapV2)[T]) Delete(addr [Address](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#Address))

Delete removes addr from the map.

#### func (*AddressMapV2[T]) [Get](https://github.com/grpc/grpc-go/blob/v1.79.1/resolver/map.go#L91)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#AddressMapV2.Get "Go to AddressMapV2.Get")added in v1.72.0

func (a *[AddressMapV2](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#AddressMapV2)[T]) Get(addr [Address](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#Address)) (value T, ok [bool](https://pkg.go.dev/builtin#bool))

Get returns the value for the address in the map, if present.

#### func (*AddressMapV2[T]) [Keys](https://github.com/grpc/grpc-go/blob/v1.79.1/resolver/map.go#L138)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#AddressMapV2.Keys "Go to AddressMapV2.Keys")added in v1.72.0

func (a *[AddressMapV2](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#AddressMapV2)[T]) Keys() [][Address](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#Address)

Keys returns a slice of all current map keys.

#### func (*AddressMapV2[T]) [Len](https://github.com/grpc/grpc-go/blob/v1.79.1/resolver/map.go#L129)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#AddressMapV2.Len "Go to AddressMapV2.Len")added in v1.72.0

func (a *[AddressMapV2](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#AddressMapV2)[T]) Len() [int](https://pkg.go.dev/builtin#int)

Len returns the number of entries in the map.

#### func (*AddressMapV2[T]) [Set](https://github.com/grpc/grpc-go/blob/v1.79.1/resolver/map.go#L101)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#AddressMapV2.Set "Go to AddressMapV2.Set")added in v1.72.0

func (a *[AddressMapV2](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#AddressMapV2)[T]) Set(addr [Address](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#Address), value T)

Set updates or adds the value to the address in the map.

#### func (*AddressMapV2[T]) [Values](https://github.com/grpc/grpc-go/blob/v1.79.1/resolver/map.go#L149)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#AddressMapV2.Values "Go to AddressMapV2.Values")added in v1.72.0

func (a *[AddressMapV2](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#AddressMapV2)[T]) Values() []T

Values returns a slice of all current map values.

#### type [AuthorityOverrider](https://github.com/grpc/grpc-go/blob/v1.79.1/resolver/resolver.go#L332)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#AuthorityOverrider "Go to AuthorityOverrider")added in v1.61.0

type AuthorityOverrider interface {
// OverrideAuthority returns the authority to use for a ClientConn with the	// given target. The implementation must generate it without blocking,
	// typically in line, and must keep it unchanged.
	//
	// The returned string must be a valid ":authority" header value, i.e. be
	// encoded according to
	// [RFC3986]([https://datatracker.ietf.org/doc/html/rfc3986#section-3.2](https://datatracker.ietf.org/doc/html/rfc3986#section-3.2)) as
	// necessary.
	OverrideAuthority([Target](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#Target)) [string](https://pkg.go.dev/builtin#string)
}

AuthorityOverrider is implemented by Builders that wish to override the default authority for the ClientConn. By default, the authority used is target.Endpoint().

#### type [BuildOptions](https://github.com/grpc/grpc-go/blob/v1.79.1/resolver/resolver.go#L154)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#BuildOptions "Go to BuildOptions")added in v1.26.0

type BuildOptions struct {
// DisableServiceConfig indicates whether a resolver implementation should	// fetch service config data.
	DisableServiceConfig [bool](https://pkg.go.dev/builtin#bool)
// DialCreds is the transport credentials used by the ClientConn for	// communicating with the target gRPC service (set via
	// WithTransportCredentials). In cases where a name resolution service
	// requires the same credentials, the resolver may use this field. In most
	// cases though, it is not appropriate, and this field may be ignored.
	DialCreds [credentials](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials).[TransportCredentials](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#TransportCredentials)
// CredsBundle is the credentials bundle used by the ClientConn for	// communicating with the target gRPC service (set via
	// WithCredentialsBundle). In cases where a name resolution service
	// requires the same credentials, the resolver may use this field. In most
	// cases though, it is not appropriate, and this field may be ignored.
	CredsBundle [credentials](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials).[Bundle](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#Bundle)
// Dialer is the custom dialer used by the ClientConn for dialling the	// target gRPC service (set via WithDialer). In cases where a name
	// resolution service requires the same dialer, the resolver may use this
	// field. In most cases though, it is not appropriate, and this field may
	// be ignored.
	Dialer func([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), [string](https://pkg.go.dev/builtin#string)) ([net](https://pkg.go.dev/net).[Conn](https://pkg.go.dev/net#Conn), [error](https://pkg.go.dev/builtin#error))
// Authority is the effective authority of the clientconn for which the	// resolver is built.
	Authority [string](https://pkg.go.dev/builtin#string)
// MetricsRecorder is the metrics recorder to do recording.	MetricsRecorder [stats](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats).[MetricsRecorder](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#MetricsRecorder)
}

BuildOptions includes additional information for the builder to create the resolver.

#### type [Builder](https://github.com/grpc/grpc-go/blob/v1.79.1/resolver/resolver.go#L301)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#Builder "Go to Builder")

type Builder interface {
// Build creates a new resolver for the given target.	//
	// gRPC dial calls Build synchronously, and fails if the returned error is
	// not nil.
	Build(target [Target](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#Target), cc [ClientConn](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#ClientConn), opts [BuildOptions](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#BuildOptions)) ([Resolver](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#Resolver), [error](https://pkg.go.dev/builtin#error))
// Scheme returns the scheme supported by this resolver. Scheme is defined	// at [https://github.com/grpc/grpc/blob/master/doc/naming.md](https://github.com/grpc/grpc/blob/master/doc/naming.md). The returned
	// string should not contain uppercase characters, as they will not match
	// the parsed target's scheme as defined in [RFC 3986](https://rfc-editor.org/rfc/rfc3986.html).
	Scheme() [string](https://pkg.go.dev/builtin#string)
}

Builder creates a resolver that will be used to watch name resolution updates.

#### func [Get](https://github.com/grpc/grpc-go/blob/v1.79.1/resolver/resolver.go#L61)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#Get "Go to Get")

func Get(scheme [string](https://pkg.go.dev/builtin#string)) [Builder](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#Builder)

Get returns the resolver builder registered with the given scheme.

If no builder is register with the scheme, nil will be returned.

#### type [ClientConn](https://github.com/grpc/grpc-go/blob/v1.79.1/resolver/resolver.go#L232)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#ClientConn "Go to ClientConn")

type ClientConn interface {
// UpdateState updates the state of the ClientConn appropriately.	//
	// If an error is returned, the resolver should try to resolve the
	// target again. The resolver should use a backoff timer to prevent
	// overloading the server with requests. If a resolver is certain that
	// reresolving will not change the result, e.g. because it is
	// a watch-based resolver, returned errors can be ignored.
	//
	// If the resolved State is the same as the last reported one, calling
	// UpdateState can be omitted.
	UpdateState([State](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#State)) [error](https://pkg.go.dev/builtin#error)
// ReportError notifies the ClientConn that the Resolver encountered an	// error. The ClientConn then forwards this error to the load balancing
	// policy.
	ReportError([error](https://pkg.go.dev/builtin#error))
// NewAddress is called by resolver to notify ClientConn a new list	// of resolved addresses.
	// The address list should be the complete list of resolved addresses.
	//
	// Deprecated: Use UpdateState instead.
	NewAddress(addresses [][Address](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#Address))
// ParseServiceConfig parses the provided service config and returns an	// object that provides the parsed config.
	ParseServiceConfig(serviceConfigJSON [string](https://pkg.go.dev/builtin#string)) *[serviceconfig](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/serviceconfig).[ParseResult](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/serviceconfig#ParseResult)
}

ClientConn contains the callbacks for resolver to notify any updates to the gRPC ClientConn.

This interface is to be implemented by gRPC. Users should not need a brand new implementation of this interface. For the situations like testing, the new implementation should embed this interface. This allows gRPC to add new methods to this interface.

#### type [Endpoint](https://github.com/grpc/grpc-go/blob/v1.79.1/resolver/resolver.go#L186)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#Endpoint "Go to Endpoint")added in v1.58.0

type Endpoint struct {
// Addresses contains a list of addresses used to access this endpoint.	Addresses [][Address](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#Address)

// Attributes contains arbitrary data about this endpoint intended for	// consumption by the LB policy.
	Attributes *[attributes](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/attributes).[Attributes](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/attributes#Attributes)
}

An Endpoint is one network endpoint, or server, which may have multiple addresses with which it can be accessed. TODO(i/8773) : make resolver.Endpoint and resolver.Address immutable

#### type [EndpointMap](https://github.com/grpc/grpc-go/blob/v1.79.1/resolver/map.go#L165)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#EndpointMap "Go to EndpointMap")added in v1.60.0

type EndpointMap[T [any](https://pkg.go.dev/builtin#any)] struct {
	// contains filtered or unexported fields
}

EndpointMap is a map of endpoints to arbitrary values keyed on only the unordered set of address strings within an endpoint. This map is not thread safe, thus it is unsafe to access concurrently. Must be created via NewEndpointMap; do not construct directly.

#### func [NewEndpointMap](https://github.com/grpc/grpc-go/blob/v1.79.1/resolver/map.go#L177)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#NewEndpointMap "Go to NewEndpointMap")added in v1.60.0

func NewEndpointMap[T [any](https://pkg.go.dev/builtin#any)]() *[EndpointMap](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#EndpointMap)[T]

NewEndpointMap creates a new EndpointMap.

#### func (*EndpointMap[T]) [Delete](https://github.com/grpc/grpc-go/blob/v1.79.1/resolver/map.go#L244)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#EndpointMap.Delete "Go to EndpointMap.Delete")added in v1.60.0

func (em *[EndpointMap](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#EndpointMap)[T]) Delete(e [Endpoint](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#Endpoint))

Delete removes the specified endpoint from the map.

#### func (*EndpointMap[T]) [Get](https://github.com/grpc/grpc-go/blob/v1.79.1/resolver/map.go#L199)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#EndpointMap.Get "Go to EndpointMap.Get")added in v1.60.0

func (em *[EndpointMap](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#EndpointMap)[T]) Get(e [Endpoint](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#Endpoint)) (value T, ok [bool](https://pkg.go.dev/builtin#bool))

Get returns the value for the address in the map, if present.

#### func (*EndpointMap[T]) [Keys](https://github.com/grpc/grpc-go/blob/v1.79.1/resolver/map.go#L226)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#EndpointMap.Keys "Go to EndpointMap.Keys")added in v1.60.0

func (em *[EndpointMap](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#EndpointMap)[T]) Keys() [][Endpoint](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#Endpoint)

Keys returns a slice of all current map keys, as endpoints specifying the addresses present in the endpoint keys, in which uniqueness is determined by the unordered set of addresses. Thus, endpoint information returned is not the full endpoint data (drops duplicated addresses and attributes) but can be used for EndpointMap accesses.

#### func (*EndpointMap[T]) [Len](https://github.com/grpc/grpc-go/blob/v1.79.1/resolver/map.go#L217)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#EndpointMap.Len "Go to EndpointMap.Len")added in v1.60.0

func (em *[EndpointMap](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#EndpointMap)[T]) Len() [int](https://pkg.go.dev/builtin#int)

Len returns the number of entries in the map.

#### func (*EndpointMap[T]) [Set](https://github.com/grpc/grpc-go/blob/v1.79.1/resolver/map.go#L208)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#EndpointMap.Set "Go to EndpointMap.Set")added in v1.60.0

func (em *[EndpointMap](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#EndpointMap)[T]) Set(e [Endpoint](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#Endpoint), value T)

Set updates or adds the value to the address in the map.

#### func (*EndpointMap[T]) [Values](https://github.com/grpc/grpc-go/blob/v1.79.1/resolver/map.go#L235)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#EndpointMap.Values "Go to EndpointMap.Values")added in v1.60.0

func (em *[EndpointMap](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#EndpointMap)[T]) Values() []T

Values returns a slice of all current map values.

#### type [ResolveNowOptions](https://github.com/grpc/grpc-go/blob/v1.79.1/resolver/resolver.go#L315)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#ResolveNowOptions "Go to ResolveNowOptions")added in v1.26.0

type ResolveNowOptions struct{}

ResolveNowOptions includes additional information for ResolveNow.

#### type [Resolver](https://github.com/grpc/grpc-go/blob/v1.79.1/resolver/resolver.go#L319)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#Resolver "Go to Resolver")

type Resolver interface {
// ResolveNow will be called by gRPC to try to resolve the target name	// again. It's just a hint, resolver can ignore this if it's not necessary.
	//
	// It could be called multiple times concurrently.
	ResolveNow([ResolveNowOptions](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#ResolveNowOptions))
// Close closes the resolver.	Close()
}

Resolver watches for the updates on the specified target. Updates include address updates and service config updates.

#### type [State](https://github.com/grpc/grpc-go/blob/v1.79.1/resolver/resolver.go#L196)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#State "Go to State")added in v1.20.0

type State struct {
// Addresses is the latest set of resolved addresses for the target.	//
	// If a resolver sets Addresses but does not set Endpoints, one Endpoint
	// will be created for each Address before the State is passed to the LB
	// policy. The BalancerAttributes of each entry in Addresses will be set
	// in Endpoints.Attributes, and be cleared in the Endpoint's Address's
	// BalancerAttributes.
	//
	// Soon, Addresses will be deprecated and replaced fully by Endpoints.
	Addresses [][Address](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#Address)

// Endpoints is the latest set of resolved endpoints for the target.	//
	// If a resolver produces a State containing Endpoints but not Addresses,
	// it must take care to ensure the LB policies it selects will support
	// Endpoints.
	Endpoints [][Endpoint](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#Endpoint)

// ServiceConfig contains the result from parsing the latest service	// config. If it is nil, it indicates no service config is present or the
	// resolver does not provide service configs.
	ServiceConfig *[serviceconfig](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/serviceconfig).[ParseResult](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/serviceconfig#ParseResult)

// Attributes contains arbitrary data about the resolver intended for	// consumption by the load balancing policy.
	Attributes *[attributes](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/attributes).[Attributes](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/attributes#Attributes)
}

State contains the current Resolver state relevant to the ClientConn.

#### type [Target](https://github.com/grpc/grpc-go/blob/v1.79.1/resolver/resolver.go#L269)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#Target "Go to Target")

type Target struct {
// URL contains the parsed dial target with an optional default scheme added	// to it if the original dial target contained no scheme or contained an
	// unregistered scheme. Any query params specified in the original dial
	// target can be accessed from here.
	URL [url](https://pkg.go.dev/net/url).[URL](https://pkg.go.dev/net/url#URL)
}

Target represents a target for gRPC, as specified in: [https://github.com/grpc/grpc/blob/master/doc/naming.md](https://github.com/grpc/grpc/blob/master/doc/naming.md). It is parsed from the target string that gets passed into Dial or DialContext by the user. And gRPC passes it to the resolver and the balancer.

If the target follows the naming spec, and the parsed scheme is registered with gRPC, we will parse the target string according to the spec. If the target does not contain a scheme or if the parsed scheme is not registered (i.e. no corresponding resolver available to resolve the endpoint), we will apply the default scheme, and will attempt to reparse it.

#### func (Target) [Endpoint](https://github.com/grpc/grpc-go/blob/v1.79.1/resolver/resolver.go#L279)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#Target.Endpoint "Go to Target.Endpoint")

func (t [Target](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#Target)) Endpoint() [string](https://pkg.go.dev/builtin#string)

Endpoint retrieves endpoint without leading "/" from either `URL.Path` or `URL.Opaque`. The latter is used when the former is empty.

#### func (Target) [String](https://github.com/grpc/grpc-go/blob/v1.79.1/resolver/resolver.go#L296)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#Target.String "Go to Target.String")added in v1.60.0

func (t [Target](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#Target)) String() [string](https://pkg.go.dev/builtin#string)

String returns the canonical string representation of Target.

![Image 44](https://pkg.go.dev/static/shared/icon/insert_drive_file_gm_grey_24dp.svg) Source Files [¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#section-sourcefiles "Go to Source Files")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[View all Source files](https://github.com/grpc/grpc-go/tree/v1.79.1/resolver)

*   [map.go](https://github.com/grpc/grpc-go/blob/v1.79.1/resolver/map.go "map.go")
*   [resolver.go](https://github.com/grpc/grpc-go/blob/v1.79.1/resolver/resolver.go "resolver.go")

![Image 45](https://pkg.go.dev/static/shared/icon/folder_gm_grey_24dp.svg) Directories [¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver#section-directories "Go to Directories")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

 Show internal  Expand all 

| Path | Synopsis |
| --- | --- |
| [dns](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver/dns) Package dns implements a dns resolver to be installed as the default resolver in grpc. | Package dns implements a dns resolver to be installed as the default resolver in grpc. |
| [manual](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver/manual) Package manual defines a resolver that can be used to manually send resolved addresses to ClientConn. | Package manual defines a resolver that can be used to manually send resolved addresses to ClientConn. |
| [passthrough](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver/passthrough) Package passthrough implements a pass-through resolver. | Package passthrough implements a pass-through resolver. |
| [ringhash](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/resolver/ringhash) Package ringhash implements resolver related functions for the ring_hash load balancing policy. | Package ringhash implements resolver related functions for the ring_hash load balancing policy. |

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
