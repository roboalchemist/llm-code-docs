# Source: https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/handshaker

Title: handshaker package - google.golang.org/grpc/credentials/alts/internal/handshaker - Go Packages

URL Source: https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/handshaker

Markdown Content:
handshaker package - google.golang.org/grpc/credentials/alts/internal/handshaker - Go Packages
===============

[![Image 1: Go](https://pkg.go.dev/static/shared/logo/go-white.svg)](https://go.dev/)

[Skip to Main Content](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/handshaker#main-content)

![Image 2](https://pkg.go.dev/static/shared/icon/search_gm_grey_24dp.svg)![Image 3](https://pkg.go.dev/static/shared/icon/search_gm_grey_24dp.svg)

*   [Why Go ![Image 4: submenu dropdown icon](https://pkg.go.dev/static/shared/icon/arrow_drop_down_gm_grey_24dp.svg)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/handshaker#)
    *   [Case Studies](https://go.dev/solutions#case-studies) 
Common problems companies solve with Go

    *   [Use Cases](https://go.dev/solutions#use-cases) 
Stories about how and why companies use Go

    *   [Security](https://go.dev/security/) 
How Go can help keep you secure by default

*   [Learn](https://go.dev/learn/)
*   [Docs ![Image 5: submenu dropdown icon](https://pkg.go.dev/static/shared/icon/arrow_drop_down_gm_grey_24dp.svg)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/handshaker#)
    *   [Effective Go](https://go.dev/doc/effective_go) 
Tips for writing clear, performant, and idiomatic Go code

    *   [Go User Manual](https://go.dev/doc/) 
A complete introduction to building software with Go

    *   [Standard library](https://pkg.go.dev/std) 
Reference documentation for Go's standard library

    *   [Release Notes](https://go.dev/doc/devel/release) 
Learn what's new in each Go release

*   [Packages](https://pkg.go.dev/)
*   [Community ![Image 6: submenu dropdown icon](https://pkg.go.dev/static/shared/icon/arrow_drop_down_gm_grey_24dp.svg)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/handshaker#)
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

*   [Why Go _![Image 16](https://pkg.go.dev/static/shared/icon/navigate\_next\_gm\_grey\_24dp.svg)_](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/handshaker#)

[_![Image 17](https://pkg.go.dev/static/shared/icon/navigate\_before\_gm\_grey\_24dp.svg)_ Why Go](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/handshaker#) 
    *   [Case Studies](https://go.dev/solutions#case-studies)
    *   [Use Cases](https://go.dev/solutions#use-cases)
    *   [Security](https://go.dev/security/)

*   [Learn](https://go.dev/learn/)
*   [Docs _![Image 18](https://pkg.go.dev/static/shared/icon/navigate\_next\_gm\_grey\_24dp.svg)_](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/handshaker#)

[_![Image 19](https://pkg.go.dev/static/shared/icon/navigate\_before\_gm\_grey\_24dp.svg)_ Docs](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/handshaker#) 
    *   [Effective Go](https://go.dev/doc/effective_go)
    *   [Go User Manual](https://go.dev/doc/)
    *   [Standard library](https://pkg.go.dev/std)
    *   [Release Notes](https://go.dev/doc/devel/release)

*   [Packages](https://pkg.go.dev/)
*   [Community _![Image 20](https://pkg.go.dev/static/shared/icon/navigate\_next\_gm\_grey\_24dp.svg)_](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/handshaker#)

[_![Image 21](https://pkg.go.dev/static/shared/icon/navigate\_before\_gm\_grey\_24dp.svg)_ Community](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/handshaker#) 
    *   [Recorded Talks](https://go.dev/talks/)
    *   [Meetups _![Image 22](https://pkg.go.dev/static/shared/icon/launch\_gm\_grey\_24dp.svg)_](https://www.meetup.com/pro/go)
    *   [Conferences _![Image 23](https://pkg.go.dev/static/shared/icon/launch\_gm\_grey\_24dp.svg)_](https://github.com/golang/go/wiki/Conferences)
    *   [Go blog](https://go.dev/blog)
    *   [Go project](https://go.dev/help)
    *   Get connected [![Image 24](https://pkg.go.dev/static/shared/logo/social/google-groups.svg)](https://groups.google.com/g/golang-nuts)[![Image 25](https://pkg.go.dev/static/shared/logo/social/github.svg)](https://github.com/golang)[![Image 26](https://pkg.go.dev/static/shared/logo/social/twitter.svg)](https://twitter.com/golang)[![Image 27](https://pkg.go.dev/static/shared/logo/social/reddit.svg)](https://www.reddit.com/r/golang/)[![Image 28](https://pkg.go.dev/static/shared/logo/social/slack.svg)](https://invite.slack.golangbridge.org/)[![Image 29](https://pkg.go.dev/static/shared/logo/social/stack-overflow.svg)](https://stackoverflow.com/collectives/go) 

1.   [Discover Packages](https://pkg.go.dev/)
2.   [google.golang.org/grpc](https://pkg.go.dev/google.golang.org/grpc@v1.79.1)
3.   [credentials](https://pkg.go.dev/google.golang.org/grpc/credentials@v1.79.1)
4.   [alts](https://pkg.go.dev/google.golang.org/grpc/credentials/alts@v1.79.1)
5.   [internal](https://pkg.go.dev/google.golang.org/grpc/credentials/alts/internal@v1.79.1)
6.   [handshaker](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/handshaker)![Image 30](https://pkg.go.dev/static/shared/icon/content_copy_gm_grey_24dp.svg)

[![Image 31: Go](https://pkg.go.dev/static/shared/logo/go-blue.svg)](https://go.dev/)
handshaker
==========

package![Image 32](https://pkg.go.dev/static/shared/icon/content_copy_gm_grey_24dp.svg)

[Version: v1.79.1](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/handshaker?tab=versions)

 Opens a new window with list of versions in this module. 

Latest Latest 

![Image 33: Warning](https://pkg.go.dev/static/shared/icon/alert_gm_grey_24dp.svg)
This package is not in the latest version of its module.

[Go to latest](https://pkg.go.dev/google.golang.org/grpc/credentials/alts/internal/handshaker) Published: Feb 13, 2026  License: [Apache-2.0](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/handshaker?tab=licenses)

 Opens a new window with license information. 

[Imports: 15](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/handshaker?tab=imports)

 Opens a new window with list of imports. 

[Imported by: 0](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/handshaker?tab=importedby)

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

*   [Documentation](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/handshaker#section-documentation)
    *   [Overview](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/handshaker#pkg-overview)
    *   [Index](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/handshaker#pkg-index)
    *   [Constants](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/handshaker#pkg-constants)
    *   [Variables](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/handshaker#pkg-variables)
    *   [Functions](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/handshaker#pkg-functions)
        *   [NewClientHandshaker(_, conn, c, opts)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/handshaker#NewClientHandshaker "NewClientHandshaker(_, conn, c, opts)")
        *   [NewServerHandshaker(_, conn, c, opts)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/handshaker#NewServerHandshaker "NewServerHandshaker(_, conn, c, opts)")
        *   [ResetConcurrentHandshakeSemaphoreForTesting(numberOfAllowedHandshakes)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/handshaker#ResetConcurrentHandshakeSemaphoreForTesting "ResetConcurrentHandshakeSemaphoreForTesting(numberOfAllowedHandshakes)")

    *   [Types](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/handshaker#pkg-types)
        *   [type ClientHandshakerOptions](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/handshaker#ClientHandshakerOptions "type ClientHandshakerOptions")
            *   [DefaultClientHandshakerOptions()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/handshaker#DefaultClientHandshakerOptions "DefaultClientHandshakerOptions()")

        *   [type ServerHandshakerOptions](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/handshaker#ServerHandshakerOptions "type ServerHandshakerOptions")
            *   [DefaultServerHandshakerOptions()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/handshaker#DefaultServerHandshakerOptions "DefaultServerHandshakerOptions()")

*   [Source Files](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/handshaker#section-sourcefiles)
*   [Directories](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/handshaker#section-directories)

![Image 43](https://pkg.go.dev/static/shared/icon/code_gm_grey_24dp.svg) Documentation [¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/handshaker#section-documentation "Go to Documentation")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Overview [¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/handshaker#pkg-overview "Go to Overview")

Package handshaker provides ALTS handshaking functionality for GCP.

### Index [¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/handshaker#pkg-index "Go to Index")

*   [func NewClientHandshaker(_ context.Context, conn *grpc.ClientConn, c net.Conn, ...) (core.Handshaker, error)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/handshaker#NewClientHandshaker)
*   [func NewServerHandshaker(_ context.Context, conn *grpc.ClientConn, c net.Conn, ...) (core.Handshaker, error)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/handshaker#NewServerHandshaker)
*   [func ResetConcurrentHandshakeSemaphoreForTesting(numberOfAllowedHandshakes int64)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/handshaker#ResetConcurrentHandshakeSemaphoreForTesting)
*   [type ClientHandshakerOptions](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/handshaker#ClientHandshakerOptions)
*       *   [func DefaultClientHandshakerOptions() *ClientHandshakerOptions](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/handshaker#DefaultClientHandshakerOptions)

*   [type ServerHandshakerOptions](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/handshaker#ServerHandshakerOptions)
*       *   [func DefaultServerHandshakerOptions() *ServerHandshakerOptions](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/handshaker#DefaultServerHandshakerOptions)

### Constants [¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/handshaker#pkg-constants "Go to Constants")

This section is empty.

### Variables [¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/handshaker#pkg-variables "Go to Variables")

This section is empty.

### Functions [¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/handshaker#pkg-functions "Go to Functions")

#### func [NewClientHandshaker](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/alts/internal/handshaker/handshaker.go#L133)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/handshaker#NewClientHandshaker "Go to NewClientHandshaker")

func NewClientHandshaker(_ [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), conn *[grpc](https://pkg.go.dev/google.golang.org/grpc@v1.79.1).[ClientConn](https://pkg.go.dev/google.golang.org/grpc@v1.79.1#ClientConn), c [net](https://pkg.go.dev/net).[Conn](https://pkg.go.dev/net#Conn), opts *[ClientHandshakerOptions](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/handshaker#ClientHandshakerOptions)) ([core](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal).[Handshaker](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal#Handshaker), [error](https://pkg.go.dev/builtin#error))

NewClientHandshaker creates a core.Handshaker that performs a client-side ALTS handshake by acting as a proxy between the peer and the ALTS handshaker service in the metadata server.

#### func [NewServerHandshaker](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/alts/internal/handshaker/handshaker.go#L146)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/handshaker#NewServerHandshaker "Go to NewServerHandshaker")

func NewServerHandshaker(_ [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), conn *[grpc](https://pkg.go.dev/google.golang.org/grpc@v1.79.1).[ClientConn](https://pkg.go.dev/google.golang.org/grpc@v1.79.1#ClientConn), c [net](https://pkg.go.dev/net).[Conn](https://pkg.go.dev/net#Conn), opts *[ServerHandshakerOptions](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/handshaker#ServerHandshakerOptions)) ([core](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal).[Handshaker](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal#Handshaker), [error](https://pkg.go.dev/builtin#error))

NewServerHandshaker creates a core.Handshaker that performs a server-side ALTS handshake by acting as a proxy between the peer and the ALTS handshaker service in the metadata server.

#### func [ResetConcurrentHandshakeSemaphoreForTesting](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/alts/internal/handshaker/handshaker.go#L374)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/handshaker#ResetConcurrentHandshakeSemaphoreForTesting "Go to ResetConcurrentHandshakeSemaphoreForTesting")added in v1.57.0

func ResetConcurrentHandshakeSemaphoreForTesting(numberOfAllowedHandshakes [int64](https://pkg.go.dev/builtin#int64))

ResetConcurrentHandshakeSemaphoreForTesting resets the handshake semaphores to allow numberOfAllowedHandshakes concurrent handshakes each.

### Types [¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/handshaker#pkg-types "Go to Types")

#### type [ClientHandshakerOptions](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/alts/internal/handshaker/handshaker.go#L79)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/handshaker#ClientHandshakerOptions "Go to ClientHandshakerOptions")

type ClientHandshakerOptions struct {
// ClientIdentity is the handshaker client local identity.	ClientIdentity *[altspb](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp).[Identity](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#Identity)
// TargetName is the server service account name for secure name	// checking.
	TargetName [string](https://pkg.go.dev/builtin#string)
// TargetServiceAccounts contains a list of expected target service	// accounts. One of these accounts should match one of the accounts in
	// the handshaker results. Otherwise, the handshake fails.
	TargetServiceAccounts [][string](https://pkg.go.dev/builtin#string)
// RPCVersions specifies the gRPC versions accepted by the client.	RPCVersions *[altspb](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp).[RpcProtocolVersions](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#RpcProtocolVersions)
// BoundAccessToken is a bound access token to be sent to the server for authentication.	BoundAccessToken [string](https://pkg.go.dev/builtin#string)
}

ClientHandshakerOptions contains the client handshaker options that can provided by the caller.

#### func [DefaultClientHandshakerOptions](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/alts/internal/handshaker/handshaker.go#L103)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/handshaker#DefaultClientHandshakerOptions "Go to DefaultClientHandshakerOptions")

func DefaultClientHandshakerOptions() *[ClientHandshakerOptions](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/handshaker#ClientHandshakerOptions)

DefaultClientHandshakerOptions returns the default client handshaker options.

#### type [ServerHandshakerOptions](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/alts/internal/handshaker/handshaker.go#L97)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/handshaker#ServerHandshakerOptions "Go to ServerHandshakerOptions")

type ServerHandshakerOptions struct {
// RPCVersions specifies the gRPC versions accepted by the server.	RPCVersions *[altspb](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp).[RpcProtocolVersions](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#RpcProtocolVersions)
}

ServerHandshakerOptions contains the server handshaker options that can provided by the caller.

#### func [DefaultServerHandshakerOptions](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/alts/internal/handshaker/handshaker.go#L108)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/handshaker#DefaultServerHandshakerOptions "Go to DefaultServerHandshakerOptions")

func DefaultServerHandshakerOptions() *[ServerHandshakerOptions](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/handshaker#ServerHandshakerOptions)

DefaultServerHandshakerOptions returns the default client handshaker options.

![Image 44](https://pkg.go.dev/static/shared/icon/insert_drive_file_gm_grey_24dp.svg) Source Files [¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/handshaker#section-sourcefiles "Go to Source Files")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[View all Source files](https://github.com/grpc/grpc-go/tree/v1.79.1/credentials/alts/internal/handshaker)

*   [handshaker.go](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/alts/internal/handshaker/handshaker.go "handshaker.go")

![Image 45](https://pkg.go.dev/static/shared/icon/folder_gm_grey_24dp.svg) Directories [¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/handshaker#section-directories "Go to Directories")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

 Show internal  Expand all 

| Path | Synopsis |
| --- | --- |
| [service](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/handshaker/service) Package service manages connections between the VM application and the ALTS handshaker service. | Package service manages connections between the VM application and the ALTS handshaker service. |

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
