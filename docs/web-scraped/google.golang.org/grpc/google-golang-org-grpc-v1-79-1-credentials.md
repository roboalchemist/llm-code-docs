# Source: https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials

Title: credentials package - google.golang.org/grpc/credentials - Go Packages

URL Source: https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials

Markdown Content:
credentials package - google.golang.org/grpc/credentials - Go Packages
===============

[![Image 1: Go](https://pkg.go.dev/static/shared/logo/go-white.svg)](https://go.dev/)

[Skip to Main Content](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#main-content)

![Image 2](https://pkg.go.dev/static/shared/icon/search_gm_grey_24dp.svg)![Image 3](https://pkg.go.dev/static/shared/icon/search_gm_grey_24dp.svg)

*   [Why Go ![Image 4: submenu dropdown icon](https://pkg.go.dev/static/shared/icon/arrow_drop_down_gm_grey_24dp.svg)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#)
    *   [Case Studies](https://go.dev/solutions#case-studies) 
Common problems companies solve with Go

    *   [Use Cases](https://go.dev/solutions#use-cases) 
Stories about how and why companies use Go

    *   [Security](https://go.dev/security/) 
How Go can help keep you secure by default

*   [Learn](https://go.dev/learn/)
*   [Docs ![Image 5: submenu dropdown icon](https://pkg.go.dev/static/shared/icon/arrow_drop_down_gm_grey_24dp.svg)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#)
    *   [Effective Go](https://go.dev/doc/effective_go) 
Tips for writing clear, performant, and idiomatic Go code

    *   [Go User Manual](https://go.dev/doc/) 
A complete introduction to building software with Go

    *   [Standard library](https://pkg.go.dev/std) 
Reference documentation for Go's standard library

    *   [Release Notes](https://go.dev/doc/devel/release) 
Learn what's new in each Go release

*   [Packages](https://pkg.go.dev/)
*   [Community ![Image 6: submenu dropdown icon](https://pkg.go.dev/static/shared/icon/arrow_drop_down_gm_grey_24dp.svg)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#)
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

*   [Why Go _![Image 16](https://pkg.go.dev/static/shared/icon/navigate\_next\_gm\_grey\_24dp.svg)_](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#)

[_![Image 17](https://pkg.go.dev/static/shared/icon/navigate\_before\_gm\_grey\_24dp.svg)_ Why Go](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#) 
    *   [Case Studies](https://go.dev/solutions#case-studies)
    *   [Use Cases](https://go.dev/solutions#use-cases)
    *   [Security](https://go.dev/security/)

*   [Learn](https://go.dev/learn/)
*   [Docs _![Image 18](https://pkg.go.dev/static/shared/icon/navigate\_next\_gm\_grey\_24dp.svg)_](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#)

[_![Image 19](https://pkg.go.dev/static/shared/icon/navigate\_before\_gm\_grey\_24dp.svg)_ Docs](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#) 
    *   [Effective Go](https://go.dev/doc/effective_go)
    *   [Go User Manual](https://go.dev/doc/)
    *   [Standard library](https://pkg.go.dev/std)
    *   [Release Notes](https://go.dev/doc/devel/release)

*   [Packages](https://pkg.go.dev/)
*   [Community _![Image 20](https://pkg.go.dev/static/shared/icon/navigate\_next\_gm\_grey\_24dp.svg)_](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#)

[_![Image 21](https://pkg.go.dev/static/shared/icon/navigate\_before\_gm\_grey\_24dp.svg)_ Community](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#) 
    *   [Recorded Talks](https://go.dev/talks/)
    *   [Meetups _![Image 22](https://pkg.go.dev/static/shared/icon/launch\_gm\_grey\_24dp.svg)_](https://www.meetup.com/pro/go)
    *   [Conferences _![Image 23](https://pkg.go.dev/static/shared/icon/launch\_gm\_grey\_24dp.svg)_](https://github.com/golang/go/wiki/Conferences)
    *   [Go blog](https://go.dev/blog)
    *   [Go project](https://go.dev/help)
    *   Get connected [![Image 24](https://pkg.go.dev/static/shared/logo/social/google-groups.svg)](https://groups.google.com/g/golang-nuts)[![Image 25](https://pkg.go.dev/static/shared/logo/social/github.svg)](https://github.com/golang)[![Image 26](https://pkg.go.dev/static/shared/logo/social/twitter.svg)](https://twitter.com/golang)[![Image 27](https://pkg.go.dev/static/shared/logo/social/reddit.svg)](https://www.reddit.com/r/golang/)[![Image 28](https://pkg.go.dev/static/shared/logo/social/slack.svg)](https://invite.slack.golangbridge.org/)[![Image 29](https://pkg.go.dev/static/shared/logo/social/stack-overflow.svg)](https://stackoverflow.com/collectives/go) 

1.   [Discover Packages](https://pkg.go.dev/)
2.   [google.golang.org/grpc](https://pkg.go.dev/google.golang.org/grpc@v1.79.1)
3.   [credentials](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials)![Image 30](https://pkg.go.dev/static/shared/icon/content_copy_gm_grey_24dp.svg)

[![Image 31: Go](https://pkg.go.dev/static/shared/logo/go-blue.svg)](https://go.dev/)
credentials
===========

package![Image 32](https://pkg.go.dev/static/shared/icon/content_copy_gm_grey_24dp.svg)

[Version: v1.79.1](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials?tab=versions)

 Opens a new window with list of versions in this module. 

Latest Latest 

![Image 33: Warning](https://pkg.go.dev/static/shared/icon/alert_gm_grey_24dp.svg)
This package is not in the latest version of its module.

[Go to latest](https://pkg.go.dev/google.golang.org/grpc/credentials) Published: Feb 13, 2026  License: [Apache-2.0](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials?tab=licenses)

 Opens a new window with license information. 

[Imports: 13](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials?tab=imports)

 Opens a new window with list of imports. 

[Imported by: 22,597](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials?tab=importedby)

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

*   [Documentation](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#section-documentation)
    *   [Overview](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#pkg-overview)
    *   [Index](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#pkg-index)
    *   [Constants](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#pkg-constants)
    *   [Variables](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#pkg-variables)
    *   [Functions](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#pkg-functions)
        *   [CheckSecurityLevel(ai, level)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#CheckSecurityLevel "CheckSecurityLevel(ai, level)")
        *   [NewContextWithRequestInfo(ctx, ri)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#NewContextWithRequestInfo "NewContextWithRequestInfo(ctx, ri)")

    *   [Types](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#pkg-types)
        *   [type AuthInfo](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#AuthInfo "type AuthInfo")
        *   [type AuthorityValidator](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#AuthorityValidator "type AuthorityValidator")
        *   [type Bundle](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#Bundle "type Bundle")
        *   [type ChannelzSecurityInfo](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#ChannelzSecurityInfo "type ChannelzSecurityInfo")
        *   [type ChannelzSecurityValue](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#ChannelzSecurityValue "type ChannelzSecurityValue")
        *   [type ClientHandshakeInfo](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#ClientHandshakeInfo "type ClientHandshakeInfo")
            *   [ClientHandshakeInfoFromContext(ctx)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#ClientHandshakeInfoFromContext "ClientHandshakeInfoFromContext(ctx)")

        *   [type CommonAuthInfo](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#CommonAuthInfo "type CommonAuthInfo")
            *   [(c) GetCommonAuthInfo()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#CommonAuthInfo.GetCommonAuthInfo "(c) GetCommonAuthInfo()")

        *   [type OtherChannelzSecurityValue](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#OtherChannelzSecurityValue "type OtherChannelzSecurityValue")
        *   [type PerRPCCredentials](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#PerRPCCredentials "type PerRPCCredentials")
        *   [type ProtocolInfo](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#ProtocolInfo "type ProtocolInfo")
        *   [type RequestInfo](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#RequestInfo "type RequestInfo")
            *   [RequestInfoFromContext(ctx)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#RequestInfoFromContext "RequestInfoFromContext(ctx)")

        *   [type SecurityLevel](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#SecurityLevel "type SecurityLevel")
            *   [(s) String()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#SecurityLevel.String "(s) String()")

        *   [type TLSChannelzSecurityValue](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#TLSChannelzSecurityValue "type TLSChannelzSecurityValue")
        *   [type TLSInfo](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#TLSInfo "type TLSInfo")
            *   [(t) AuthType()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#TLSInfo.AuthType "(t) AuthType()")
            *   [(t) GetSecurityValue()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#TLSInfo.GetSecurityValue "(t) GetSecurityValue()")
            *   [(t) ValidateAuthority(authority)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#TLSInfo.ValidateAuthority "(t) ValidateAuthority(authority)")

        *   [type TransportCredentials](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#TransportCredentials "type TransportCredentials")
            *   [NewClientTLSFromCert(cp, serverNameOverride)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#NewClientTLSFromCert "NewClientTLSFromCert(cp, serverNameOverride)")
            *   [NewClientTLSFromFile(certFile, serverNameOverride)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#NewClientTLSFromFile "NewClientTLSFromFile(certFile, serverNameOverride)")
            *   [NewServerTLSFromCert(cert)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#NewServerTLSFromCert "NewServerTLSFromCert(cert)")
            *   [NewServerTLSFromFile(certFile, keyFile)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#NewServerTLSFromFile "NewServerTLSFromFile(certFile, keyFile)")
            *   [NewTLS(c)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#NewTLS "NewTLS(c)")

*   [Source Files](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#section-sourcefiles)
*   [Directories](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#section-directories)

![Image 43](https://pkg.go.dev/static/shared/icon/code_gm_grey_24dp.svg) Documentation [¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#section-documentation "Go to Documentation")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Overview [¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#pkg-overview "Go to Overview")

Package credentials implements various credentials supported by gRPC library, which encapsulate all the state needed by a client to authenticate with a server and make various assertions, e.g., about the client's identity, role, or whether it is authorized to make a particular call.

### Index [¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#pkg-index "Go to Index")

*   [Variables](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#pkg-variables)
*   [func CheckSecurityLevel(ai AuthInfo, level SecurityLevel) error](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#CheckSecurityLevel)
*   [func NewContextWithRequestInfo(ctx context.Context, ri RequestInfo) context.Context](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#NewContextWithRequestInfo)
*   [type AuthInfo](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#AuthInfo)
*   [type AuthorityValidator](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#AuthorityValidator)
*   [type Bundle](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#Bundle)
*   [type ChannelzSecurityInfo](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#ChannelzSecurityInfo)
*   [type ChannelzSecurityValue](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#ChannelzSecurityValue)
*   [type ClientHandshakeInfo](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#ClientHandshakeInfo)
*       *   [func ClientHandshakeInfoFromContext(ctx context.Context) ClientHandshakeInfo](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#ClientHandshakeInfoFromContext)

*   [type CommonAuthInfo](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#CommonAuthInfo)
*       *   [func (c CommonAuthInfo) GetCommonAuthInfo() CommonAuthInfo](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#CommonAuthInfo.GetCommonAuthInfo)

*   [type OtherChannelzSecurityValue](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#OtherChannelzSecurityValue)
*   [type PerRPCCredentials](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#PerRPCCredentials)
*   [type ProtocolInfo](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#ProtocolInfo)
*   [type RequestInfo](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#RequestInfo)
*       *   [func RequestInfoFromContext(ctx context.Context) (ri RequestInfo, ok bool)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#RequestInfoFromContext)

*   [type SecurityLevel](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#SecurityLevel)
*       *   [func (s SecurityLevel) String() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#SecurityLevel.String)

*   [type TLSChannelzSecurityValue](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#TLSChannelzSecurityValue)
*   [type TLSInfo](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#TLSInfo)
*       *   [func (t TLSInfo) AuthType() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#TLSInfo.AuthType)
    *   [func (t TLSInfo) GetSecurityValue() ChannelzSecurityValue](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#TLSInfo.GetSecurityValue)
    *   [func (t TLSInfo) ValidateAuthority(authority string) error](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#TLSInfo.ValidateAuthority)

*   [type TransportCredentials](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#TransportCredentials)
*       *   [func NewClientTLSFromCert(cp *x509.CertPool, serverNameOverride string) TransportCredentials](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#NewClientTLSFromCert)
    *   [func NewClientTLSFromFile(certFile, serverNameOverride string) (TransportCredentials, error)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#NewClientTLSFromFile)
    *   [func NewServerTLSFromCert(cert *tls.Certificate) TransportCredentials](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#NewServerTLSFromCert)
    *   [func NewServerTLSFromFile(certFile, keyFile string) (TransportCredentials, error)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#NewServerTLSFromFile)
    *   [func NewTLS(c *tls.Config) TransportCredentials](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#NewTLS)

### Constants [¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#pkg-constants "Go to Constants")

This section is empty.

### Variables [¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#pkg-variables "Go to Variables")

[View Source](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/credentials.go#L148)var ErrConnDispatched = [errors](https://pkg.go.dev/errors).[New](https://pkg.go.dev/errors#New)("credentials: rawConn is dispatched out of gRPC")

ErrConnDispatched indicates that rawConn has been dispatched out of gRPC and the caller should not close rawConn.

### Functions [¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#pkg-functions "Go to Functions")

#### func [CheckSecurityLevel](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/credentials.go#L290)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#CheckSecurityLevel "Go to CheckSecurityLevel")added in v1.27.0

func CheckSecurityLevel(ai [AuthInfo](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#AuthInfo), level [SecurityLevel](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#SecurityLevel)) [error](https://pkg.go.dev/builtin#error)

CheckSecurityLevel checks if a connection's security level is greater than or equal to the specified one. It returns success if 1) the condition is satisfied or 2) AuthInfo struct does not implement GetCommonAuthInfo() method or 3) CommonAuthInfo.SecurityLevel has an invalid zero value. For 2) and 3), it is for the purpose of backward-compatibility.

This API is experimental.

#### func [NewContextWithRequestInfo](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/credentials.go#L260)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#NewContextWithRequestInfo "Go to NewContextWithRequestInfo")added in v1.73.0

func NewContextWithRequestInfo(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), ri [RequestInfo](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#RequestInfo)) [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context)

NewContextWithRequestInfo creates a new context from ctx and attaches ri to it.

This RequestInfo will be accessible via RequestInfoFromContext.

Intended to be used from tests for PerRPCCredentials implementations (that often need to check connection's SecurityLevel). Should not be used from non-test code: the gRPC client already prepares a context with the correct RequestInfo attached when calling PerRPCCredentials.GetRequestMetadata.

This API is experimental.

### Types [¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#pkg-types "Go to Types")

#### type [AuthInfo](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/credentials.go#L128)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#AuthInfo "Go to AuthInfo")

type AuthInfo interface {
 AuthType() [string](https://pkg.go.dev/builtin#string)}

AuthInfo defines the common interface for the auth information the users are interested in. A struct that implements AuthInfo should embed CommonAuthInfo by including additional information about the credentials in it.

#### type [AuthorityValidator](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/credentials.go#L137)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#AuthorityValidator "Go to AuthorityValidator")added in v1.73.0

type AuthorityValidator interface {
// ValidateAuthority checks the authority value used to override the	// `:authority` header. The authority parameter is the override value
	// provided by the application via the CallAuthority option. This value
	// typically corresponds to the server hostname or endpoint the RPC is
	// targeting. It returns non-nil error if the validation fails.
	ValidateAuthority(authority [string](https://pkg.go.dev/builtin#string)) [error](https://pkg.go.dev/builtin#error)
}

AuthorityValidator validates the authority used to override the `:authority` header. This is an optional interface that implementations of AuthInfo can implement if they support per-RPC authority overrides. It is invoked when the application attempts to override the HTTP/2 `:authority` header using the CallAuthority call option.

#### type [Bundle](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/credentials.go#L208)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#Bundle "Go to Bundle")added in v1.16.0

type Bundle interface {
// TransportCredentials returns the transport credentials from the Bundle.	//
	// Implementations must return non-nil transport credentials. If transport
	// security is not needed by the Bundle, implementations may choose to
	// return insecure.NewCredentials().
	TransportCredentials() [TransportCredentials](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#TransportCredentials)

// PerRPCCredentials returns the per-RPC credentials from the Bundle.	//
	// May be nil if per-RPC credentials are not needed.
	PerRPCCredentials() [PerRPCCredentials](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#PerRPCCredentials)

// NewWithMode should make a copy of Bundle, and switch mode. Modifying the	// existing Bundle may cause races.
	//
	// NewWithMode returns nil if the requested mode is not supported.
	NewWithMode(mode [string](https://pkg.go.dev/builtin#string)) ([Bundle](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#Bundle), [error](https://pkg.go.dev/builtin#error))
}

Bundle is a combination of TransportCredentials and PerRPCCredentials.

It also contains a mode switching method, so it can be used as a combination of different credential policies.

Bundle cannot be used together with individual TransportCredentials. PerRPCCredentials from Bundle will be appended to other PerRPCCredentials.

This API is experimental.

#### type [ChannelzSecurityInfo](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/credentials.go#L314)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#ChannelzSecurityInfo "Go to ChannelzSecurityInfo")added in v1.14.0

type ChannelzSecurityInfo interface {
 GetSecurityValue() [ChannelzSecurityValue](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#ChannelzSecurityValue)}

ChannelzSecurityInfo defines the interface that security protocols should implement in order to provide security info to channelz.

This API is experimental.

#### type [ChannelzSecurityValue](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/credentials.go#L323)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#ChannelzSecurityValue "Go to ChannelzSecurityValue")added in v1.14.0

type ChannelzSecurityValue interface {
	// contains filtered or unexported methods
}

ChannelzSecurityValue defines the interface that GetSecurityValue() return value should satisfy. This interface should only be satisfied by *TLSChannelzSecurityValue and *OtherChannelzSecurityValue.

This API is experimental.

#### type [ClientHandshakeInfo](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/credentials.go#L270)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#ClientHandshakeInfo "Go to ClientHandshakeInfo")added in v1.30.0

type ClientHandshakeInfo struct {
// Attributes contains the attributes for the address. It could be provided	// by the gRPC, resolver, balancer etc.
	Attributes *[attributes](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/attributes).[Attributes](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/attributes#Attributes)
}

ClientHandshakeInfo holds data to be passed to ClientHandshake. This makes it possible to pass arbitrary data to the handshaker from gRPC, resolver, balancer etc. Individual credential implementations control the actual format of the data that they are willing to receive.

This API is experimental.

#### func [ClientHandshakeInfoFromContext](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/credentials.go#L280)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#ClientHandshakeInfoFromContext "Go to ClientHandshakeInfoFromContext")added in v1.30.0

func ClientHandshakeInfoFromContext(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context)) [ClientHandshakeInfo](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#ClientHandshakeInfo)

ClientHandshakeInfoFromContext returns the ClientHandshakeInfo struct stored in ctx.

This API is experimental.

#### type [CommonAuthInfo](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/credentials.go#L89)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#CommonAuthInfo "Go to CommonAuthInfo")added in v1.27.0

type CommonAuthInfo struct {
 SecurityLevel [SecurityLevel](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#SecurityLevel)}

CommonAuthInfo contains authenticated information common to AuthInfo implementations. It should be embedded in a struct implementing AuthInfo to provide additional information about the credentials.

This API is experimental.

#### func (CommonAuthInfo) [GetCommonAuthInfo](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/credentials.go#L94)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#CommonAuthInfo.GetCommonAuthInfo "Go to CommonAuthInfo.GetCommonAuthInfo")added in v1.27.0

func (c [CommonAuthInfo](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#CommonAuthInfo)) GetCommonAuthInfo() [CommonAuthInfo](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#CommonAuthInfo)

GetCommonAuthInfo returns the pointer to CommonAuthInfo struct.

#### type [OtherChannelzSecurityValue](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/credentials.go#L333)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#OtherChannelzSecurityValue "Go to OtherChannelzSecurityValue")added in v1.14.0

type OtherChannelzSecurityValue struct {
[ChannelzSecurityValue](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#ChannelzSecurityValue) Name [string](https://pkg.go.dev/builtin#string) Value [proto](https://pkg.go.dev/google.golang.org/protobuf/proto).[Message](https://pkg.go.dev/google.golang.org/protobuf/proto#Message)}

OtherChannelzSecurityValue defines the struct that non-TLS protocol should return from GetSecurityValue(), which contains protocol specific security info. Note the Value field will be sent to users of channelz requesting channel info, and thus sensitive info should better be avoided.

This API is experimental.

#### type [PerRPCCredentials](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/credentials.go#L38)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#PerRPCCredentials "Go to PerRPCCredentials")

type PerRPCCredentials interface {
// GetRequestMetadata gets the current request metadata, refreshing tokens	// if required. This should be called by the transport layer on each
	// request, and the data should be populated in headers or other
	// context. If a status code is returned, it will be used as the status for
	// the RPC (restricted to an allowable set of codes as defined by gRFC
	// A54). uri is the URI of the entry point for the request. When supported
	// by the underlying implementation, ctx can be used for timeout and
	// cancellation. Additionally, RequestInfo data will be available via ctx
	// to this call.
	GetRequestMetadata(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), uri ...[string](https://pkg.go.dev/builtin#string)) (map[[string](https://pkg.go.dev/builtin#string)][string](https://pkg.go.dev/builtin#string), [error](https://pkg.go.dev/builtin#error))
// RequireTransportSecurity indicates whether the credentials requires	// transport security.
	RequireTransportSecurity() [bool](https://pkg.go.dev/builtin#bool)
}

PerRPCCredentials defines the common interface for the credentials which need to attach security information to every RPC (e.g., oauth2).

#### type [ProtocolInfo](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/credentials.go#L99)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#ProtocolInfo "Go to ProtocolInfo")

type ProtocolInfo struct {
// ProtocolVersion is the gRPC wire protocol version.	//
	// Deprecated: this is unused by gRPC.
	ProtocolVersion [string](https://pkg.go.dev/builtin#string)
// SecurityProtocol is the security protocol in use.	SecurityProtocol [string](https://pkg.go.dev/builtin#string)
// SecurityVersion is the security protocol version. It is a static version string from the	// credentials, not a value that reflects per-connection protocol negotiation. To retrieve
	// details about the credentials used for a connection, use the Peer's AuthInfo field instead.
	//
	// Deprecated: please use Peer.AuthInfo.
	SecurityVersion [string](https://pkg.go.dev/builtin#string)
// ServerName is the user-configured server name. If set, this overrides	// the default :authority header used for all RPCs on the channel using the
	// containing credentials, unless grpc.WithAuthority is set on the channel,
	// in which case that setting will take precedence.
	//
	// This must be a valid `:authority` header according to
	// [RFC3986]([https://datatracker.ietf.org/doc/html/rfc3986#section-3.2](https://datatracker.ietf.org/doc/html/rfc3986#section-3.2)).
	//
	// Deprecated: Users should use grpc.WithAuthority to override the authority
	// on a channel instead of configuring the credentials.
	ServerName [string](https://pkg.go.dev/builtin#string)
}

ProtocolInfo provides static information regarding transport credentials.

#### type [RequestInfo](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/credentials.go#L231)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#RequestInfo "Go to RequestInfo")added in v1.25.0

type RequestInfo struct {
// The method passed to Invoke or NewStream for this RPC. (For proto methods, this has the format "/some.Service/Method")	Method [string](https://pkg.go.dev/builtin#string)
// AuthInfo contains the information from a security handshake (TransportCredentials.ClientHandshake, TransportCredentials.ServerHandshake)	AuthInfo [AuthInfo](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#AuthInfo)
}

RequestInfo contains request data attached to the context passed to GetRequestMetadata calls.

This API is experimental.

#### func [RequestInfoFromContext](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/credentials.go#L245)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#RequestInfoFromContext "Go to RequestInfoFromContext")added in v1.25.0

func RequestInfoFromContext(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context)) (ri [RequestInfo](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#RequestInfo), ok [bool](https://pkg.go.dev/builtin#bool))

RequestInfoFromContext extracts the RequestInfo from the context if it exists.

This API is experimental.

#### type [SecurityLevel](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/credentials.go#L57)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#SecurityLevel "Go to SecurityLevel")added in v1.27.0

type SecurityLevel [int](https://pkg.go.dev/builtin#int)

SecurityLevel defines the protection level on an established connection.

This API is experimental.

const (
// InvalidSecurityLevel indicates an invalid security level.	// The zero SecurityLevel value is invalid for backward compatibility.
	InvalidSecurityLevel [SecurityLevel](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#SecurityLevel) = [iota](https://pkg.go.dev/builtin#iota)
// NoSecurity indicates a connection is insecure.	NoSecurity
// IntegrityOnly indicates a connection only provides integrity protection.	IntegrityOnly
// PrivacyAndIntegrity indicates a connection provides both privacy and integrity protection.	PrivacyAndIntegrity
)

#### func (SecurityLevel) [String](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/credentials.go#L72)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#SecurityLevel.String "Go to SecurityLevel.String")added in v1.27.0

func (s [SecurityLevel](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#SecurityLevel)) String() [string](https://pkg.go.dev/builtin#string)

String returns SecurityLevel in a string format.

#### type [TLSChannelzSecurityValue](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/tls.go#L319)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#TLSChannelzSecurityValue "Go to TLSChannelzSecurityValue")added in v1.14.0

type TLSChannelzSecurityValue struct {
[ChannelzSecurityValue](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#ChannelzSecurityValue) StandardName [string](https://pkg.go.dev/builtin#string) LocalCertificate [][byte](https://pkg.go.dev/builtin#byte) RemoteCertificate [][byte](https://pkg.go.dev/builtin#byte)}

*   [Experimental](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#hdr-Experimental-TLSChannelzSecurityValue)

TLSChannelzSecurityValue defines the struct that TLS protocol should return from GetSecurityValue(), containing security info like cipher and certificate used.

#### Experimental [¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#hdr-Experimental-TLSChannelzSecurityValue "Go to Experimental")

Notice: This type is EXPERIMENTAL and may be changed or removed in a later release.

#### type [TLSInfo](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/tls.go#L42)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#TLSInfo "Go to TLSInfo")

type TLSInfo struct {
 State [tls](https://pkg.go.dev/crypto/tls).[ConnectionState](https://pkg.go.dev/crypto/tls#ConnectionState)[CommonAuthInfo](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#CommonAuthInfo)// This API is experimental.	SPIFFEID *[url](https://pkg.go.dev/net/url).[URL](https://pkg.go.dev/net/url#URL)
}

TLSInfo contains the auth information for a TLS authenticated connection. It implements the AuthInfo interface.

#### func (TLSInfo) [AuthType](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/tls.go#L50)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#TLSInfo.AuthType "Go to TLSInfo.AuthType")

func (t [TLSInfo](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#TLSInfo)) AuthType() [string](https://pkg.go.dev/builtin#string)

AuthType returns the type of TLSInfo as a string.

#### func (TLSInfo) [GetSecurityValue](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/tls.go#L89)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#TLSInfo.GetSecurityValue "Go to TLSInfo.GetSecurityValue")added in v1.17.0

func (t [TLSInfo](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#TLSInfo)) GetSecurityValue() [ChannelzSecurityValue](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#ChannelzSecurityValue)

GetSecurityValue returns security info requested by channelz.

#### func (TLSInfo) [ValidateAuthority](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/tls.go#L57)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#TLSInfo.ValidateAuthority "Go to TLSInfo.ValidateAuthority")added in v1.73.0

func (t [TLSInfo](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#TLSInfo)) ValidateAuthority(authority [string](https://pkg.go.dev/builtin#string)) [error](https://pkg.go.dev/builtin#error)

ValidateAuthority validates the provided authority being used to override the :authority header by verifying it against the peer certificates. It returns a non-nil error if the validation fails.

#### type [TransportCredentials](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/credentials.go#L152)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#TransportCredentials "Go to TransportCredentials")

type TransportCredentials interface {
// ClientHandshake does the authentication handshake specified by the	// corresponding authentication protocol on rawConn for clients. It returns
	// the authenticated connection and the corresponding auth information
	// about the connection. The auth information should embed CommonAuthInfo
	// to return additional information about the credentials. Implementations
	// must use the provided context to implement timely cancellation. gRPC
	// will try to reconnect if the error returned is a temporary error
	// (io.EOF, context.DeadlineExceeded or err.Temporary() == true). If the
	// returned error is a wrapper error, implementations should make sure that
	// the error implements Temporary() to have the correct retry behaviors.
	// Additionally, ClientHandshakeInfo data will be available via the context
	// passed to this call.
	//
	// The second argument to this method is the `:authority` header value used
	// while creating new streams on this connection after authentication
	// succeeds. Implementations must use this as the server name during the
	// authentication handshake.
	//
	// If the returned net.Conn is closed, it MUST close the net.Conn provided.
	ClientHandshake([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), [string](https://pkg.go.dev/builtin#string), [net](https://pkg.go.dev/net).[Conn](https://pkg.go.dev/net#Conn)) ([net](https://pkg.go.dev/net).[Conn](https://pkg.go.dev/net#Conn), [AuthInfo](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#AuthInfo), [error](https://pkg.go.dev/builtin#error))
// ServerHandshake does the authentication handshake for servers. It returns	// the authenticated connection and the corresponding auth information about
	// the connection. The auth information should embed CommonAuthInfo to return additional information
	// about the credentials.
	//
	// If the returned net.Conn is closed, it MUST close the net.Conn provided.
	ServerHandshake([net](https://pkg.go.dev/net).[Conn](https://pkg.go.dev/net#Conn)) ([net](https://pkg.go.dev/net).[Conn](https://pkg.go.dev/net#Conn), [AuthInfo](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#AuthInfo), [error](https://pkg.go.dev/builtin#error))
// Info provides the ProtocolInfo of this TransportCredentials.	Info() [ProtocolInfo](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#ProtocolInfo)
// Clone makes a copy of this TransportCredentials.	Clone() [TransportCredentials](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#TransportCredentials)
// OverrideServerName specifies the value used for the following:	//
	// - verifying the hostname on the returned certificates
	// - as SNI in the client's handshake to support virtual hosting
	// - as the value for `:authority` header at stream creation time
	//
	// The provided string should be a valid `:authority` header according to
	// [RFC3986]([https://datatracker.ietf.org/doc/html/rfc3986#section-3.2](https://datatracker.ietf.org/doc/html/rfc3986#section-3.2)).
	//
	// Deprecated: this method is unused by gRPC. Users should use
	// grpc.WithAuthority to override the authority on a channel instead of
	// configuring the credentials.
	OverrideServerName([string](https://pkg.go.dev/builtin#string)) [error](https://pkg.go.dev/builtin#error)
}

TransportCredentials defines the common interface for all the live gRPC wire protocols and supported transport security protocols (e.g., TLS, SSL).

#### func [NewClientTLSFromCert](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/tls.go#L271)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#NewClientTLSFromCert "Go to NewClientTLSFromCert")

func NewClientTLSFromCert(cp *[x509](https://pkg.go.dev/crypto/x509).[CertPool](https://pkg.go.dev/crypto/x509#CertPool), serverNameOverride [string](https://pkg.go.dev/builtin#string)) [TransportCredentials](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#TransportCredentials)

NewClientTLSFromCert constructs TLS credentials from the provided root certificate authority certificate(s) to validate server connections. If certificates to establish the identity of the client need to be included in the credentials (eg: for mTLS), use NewTLS instead, where a complete tls.Config can be specified.

serverNameOverride is for testing only. If set to a non empty string, it will override the virtual host name of authority (e.g. :authority header field) in requests. Users should use grpc.WithAuthority passed to grpc.NewClient to override the authority of the client instead.

#### func [NewClientTLSFromFile](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/tls.go#L285)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#NewClientTLSFromFile "Go to NewClientTLSFromFile")

func NewClientTLSFromFile(certFile, serverNameOverride [string](https://pkg.go.dev/builtin#string)) ([TransportCredentials](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#TransportCredentials), [error](https://pkg.go.dev/builtin#error))

NewClientTLSFromFile constructs TLS credentials from the provided root certificate authority certificate file(s) to validate server connections. If certificates to establish the identity of the client need to be included in the credentials (eg: for mTLS), use NewTLS instead, where a complete tls.Config can be specified.

serverNameOverride is for testing only. If set to a non empty string, it will override the virtual host name of authority (e.g. :authority header field) in requests. Users should use grpc.WithAuthority passed to grpc.NewClient to override the authority of the client instead.

#### func [NewServerTLSFromCert](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/tls.go#L298)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#NewServerTLSFromCert "Go to NewServerTLSFromCert")

func NewServerTLSFromCert(cert *[tls](https://pkg.go.dev/crypto/tls).[Certificate](https://pkg.go.dev/crypto/tls#Certificate)) [TransportCredentials](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#TransportCredentials)

NewServerTLSFromCert constructs TLS credentials from the input certificate for server.

#### func [NewServerTLSFromFile](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/tls.go#L304)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#NewServerTLSFromFile "Go to NewServerTLSFromFile")

func NewServerTLSFromFile(certFile, keyFile [string](https://pkg.go.dev/builtin#string)) ([TransportCredentials](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#TransportCredentials), [error](https://pkg.go.dev/builtin#error))

NewServerTLSFromFile constructs TLS credentials from the input certificate file and key file for server.

#### func [NewTLS](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/tls.go#L224)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#NewTLS "Go to NewTLS")

func NewTLS(c *[tls](https://pkg.go.dev/crypto/tls).[Config](https://pkg.go.dev/crypto/tls#Config)) [TransportCredentials](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#TransportCredentials)

NewTLS uses c to construct a TransportCredentials based on TLS.

![Image 44](https://pkg.go.dev/static/shared/icon/insert_drive_file_gm_grey_24dp.svg) Source Files [¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#section-sourcefiles "Go to Source Files")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[View all Source files](https://github.com/grpc/grpc-go/tree/v1.79.1/credentials)

*   [credentials.go](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/credentials.go "credentials.go")
*   [tls.go](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/tls.go "tls.go")

![Image 45](https://pkg.go.dev/static/shared/icon/folder_gm_grey_24dp.svg) Directories [¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials#section-directories "Go to Directories")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

 Show internal  Expand all 

| Path | Synopsis |
| --- | --- |
| ![Image 46](https://pkg.go.dev/static/shared/icon/arrow_right_gm_grey_24dp.svg)[alts](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts) Package alts implements the ALTS credential support by gRPC library, which encapsulates all the state needed by a client to authenticate with a server using ALTS and make various assertions, e.g., about the client's identity, role, or whether it is authorized to make a particular call. | Package alts implements the ALTS credential support by gRPC library, which encapsulates all the state needed by a client to authenticate with a server using ALTS and make various assertions, e.g., about the client's identity, role, or whether it is authorized to make a particular call. |
| [internal](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal) Package internal contains common core functionality for ALTS. | Package internal contains common core functionality for ALTS. |
| [internal/authinfo](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/authinfo) Package authinfo provide authentication information returned by handshakers. | Package authinfo provide authentication information returned by handshakers. |
| [internal/conn](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/conn) Package conn contains an implementation of a secure channel created by gRPC handshakers. | Package conn contains an implementation of a secure channel created by gRPC handshakers. |
| [internal/handshaker](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/handshaker) Package handshaker provides ALTS handshaking functionality for GCP. | Package handshaker provides ALTS handshaking functionality for GCP. |
| [internal/handshaker/service](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/handshaker/service) Package service manages connections between the VM application and the ALTS handshaker service. | Package service manages connections between the VM application and the ALTS handshaker service. |
| [internal/proto/grpc_gcp](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp) |  |
| [internal/testutil](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/testutil) Package testutil include useful test utilities for the handshaker. | Package testutil include useful test utilities for the handshaker. |
| [google](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/google) Package google defines credentials for google cloud services. | Package google defines credentials for google cloud services. |
| [insecure](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/insecure) Package insecure provides an implementation of the credentials.TransportCredentials interface which disables transport security. | Package insecure provides an implementation of the credentials.TransportCredentials interface which disables transport security. |
| [jwt](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/jwt) Package jwt implements JWT token file-based call credentials. | Package jwt implements JWT token file-based call credentials. |
| [local](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/local) Package local implements local transport credentials. | Package local implements local transport credentials. |
| [oauth](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/oauth) Package oauth implements gRPC credentials using OAuth. | Package oauth implements gRPC credentials using OAuth. |
| [sts](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/sts) Package sts implements call credentials using STS (Security Token Service) as defined in https://tools.ietf.org/html/rfc8693. | Package sts implements call credentials using STS (Security Token Service) as defined in https://tools.ietf.org/html/rfc8693. |
| ![Image 47](https://pkg.go.dev/static/shared/icon/arrow_right_gm_grey_24dp.svg)tls |  |
| [certprovider](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider) Package certprovider defines APIs for Certificate Providers in gRPC. | Package certprovider defines APIs for Certificate Providers in gRPC. |
| [certprovider/pemfile](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider/pemfile) Package pemfile provides a file watching certificate provider plugin implementation which works for files with PEM contents. | Package pemfile provides a file watching certificate provider plugin implementation which works for files with PEM contents. |
| [xds](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/xds) Package xds provides a transport credentials implementation where the security configuration is pushed by a management server using xDS APIs. | Package xds provides a transport credentials implementation where the security configuration is pushed by a management server using xDS APIs. |

 Click to show internal directories. 

 Click to hide internal directories. 

[Why Go](https://go.dev/solutions)[Use Cases](https://go.dev/solutions#use-cases)[Case Studies](https://go.dev/solutions#case-studies)

[Get Started](https://learn.go.dev/)[Playground](https://play.golang.org/)[Tour](https://tour.golang.org/)[Stack Overflow](https://stackoverflow.com/questions/tagged/go?tab=Newest)[Help](https://go.dev/help)

[Packages](https://pkg.go.dev/)[Standard Library](https://pkg.go.dev/std)[Sub-repositories](https://pkg.go.dev/golang.org/x)[About Go Packages](https://pkg.go.dev/about)

[About](https://go.dev/project)[Download](https://go.dev/dl/)[Blog](https://go.dev/blog)[Issue Tracker](https://github.com/golang/go/issues)[Release Notes](https://go.dev/doc/devel/release.html)[Brand Guidelines](https://go.dev/brand)[Code of Conduct](https://go.dev/conduct)

[Connect](https://www.twitter.com/golang)[Twitter](https://www.twitter.com/golang)[GitHub](https://github.com/golang)[Slack](https://invite.slack.golangbridge.org/)[r/golang](https://reddit.com/r/golang)[Meetup](https://www.meetup.com/pro/go)[Golang Weekly](https://golangweekly.com/)

![Image 48: Gopher in flight goggles](https://pkg.go.dev/static/shared/gopher/pilot-bust-1431x901.svg)
*   [Copyright](https://go.dev/copyright)
*   [Terms of Service](https://go.dev/tos)
*   [Privacy Policy](http://www.google.com/intl/en/policies/privacy/)
*   [Report an Issue](https://go.dev/s/pkgsite-feedback)
*   ![Image 49: System theme](https://pkg.go.dev/static/shared/icon/brightness_6_gm_grey_24dp.svg)![Image 50: Dark theme](https://pkg.go.dev/static/shared/icon/brightness_2_gm_grey_24dp.svg)![Image 51: Light theme](https://pkg.go.dev/static/shared/icon/light_mode_gm_grey_24dp.svg)
Theme Toggle

*   ![Image 52](https://pkg.go.dev/static/shared/icon/keyboard_grey_24dp.svg)
Shortcuts Modal

[![Image 53: Google logo](https://pkg.go.dev/static/shared/logo/google-white.svg)](https://google.com/)

Jump to
-------

![Image 54](https://pkg.go.dev/static/shared/icon/close_gm_grey_24dp.svg)

Close

Keyboard shortcuts
------------------

![Image 55](https://pkg.go.dev/static/shared/icon/close_gm_grey_24dp.svg)

**?**: This menu
**/**: Search site
**f** or **F**: Jump to
**y** or **Y**: Canonical URL

Close

go.dev uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay
