# Source: https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization

Title: authorization package - go.temporal.io/server/common/authorization - Go Packages

URL Source: https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization

Markdown Content:
authorization package - go.temporal.io/server/common/authorization - Go Packages
===============

[![Image 1: Go](https://pkg.go.dev/static/shared/logo/go-white.svg)](https://go.dev/)

[Skip to Main Content](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#main-content)

![Image 2](https://pkg.go.dev/static/shared/icon/search_gm_grey_24dp.svg)![Image 3](https://pkg.go.dev/static/shared/icon/search_gm_grey_24dp.svg)

*   [Why Go ![Image 4: submenu dropdown icon](https://pkg.go.dev/static/shared/icon/arrow_drop_down_gm_grey_24dp.svg)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#)
    *   [Case Studies](https://go.dev/solutions#case-studies) 
Common problems companies solve with Go

    *   [Use Cases](https://go.dev/solutions#use-cases) 
Stories about how and why companies use Go

    *   [Security](https://go.dev/security/) 
How Go can help keep you secure by default

*   [Learn](https://go.dev/learn/)
*   [Docs ![Image 5: submenu dropdown icon](https://pkg.go.dev/static/shared/icon/arrow_drop_down_gm_grey_24dp.svg)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#)
    *   [Effective Go](https://go.dev/doc/effective_go) 
Tips for writing clear, performant, and idiomatic Go code

    *   [Go User Manual](https://go.dev/doc/) 
A complete introduction to building software with Go

    *   [Standard library](https://pkg.go.dev/std) 
Reference documentation for Go's standard library

    *   [Release Notes](https://go.dev/doc/devel/release) 
Learn what's new in each Go release

*   [Packages](https://pkg.go.dev/)
*   [Community ![Image 6: submenu dropdown icon](https://pkg.go.dev/static/shared/icon/arrow_drop_down_gm_grey_24dp.svg)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#)
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

*   [Why Go _![Image 16](https://pkg.go.dev/static/shared/icon/navigate\_next\_gm\_grey\_24dp.svg)_](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#)

[_![Image 17](https://pkg.go.dev/static/shared/icon/navigate\_before\_gm\_grey\_24dp.svg)_ Why Go](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#) 
    *   [Case Studies](https://go.dev/solutions#case-studies)
    *   [Use Cases](https://go.dev/solutions#use-cases)
    *   [Security](https://go.dev/security/)

*   [Learn](https://go.dev/learn/)
*   [Docs _![Image 18](https://pkg.go.dev/static/shared/icon/navigate\_next\_gm\_grey\_24dp.svg)_](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#)

[_![Image 19](https://pkg.go.dev/static/shared/icon/navigate\_before\_gm\_grey\_24dp.svg)_ Docs](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#) 
    *   [Effective Go](https://go.dev/doc/effective_go)
    *   [Go User Manual](https://go.dev/doc/)
    *   [Standard library](https://pkg.go.dev/std)
    *   [Release Notes](https://go.dev/doc/devel/release)

*   [Packages](https://pkg.go.dev/)
*   [Community _![Image 20](https://pkg.go.dev/static/shared/icon/navigate\_next\_gm\_grey\_24dp.svg)_](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#)

[_![Image 21](https://pkg.go.dev/static/shared/icon/navigate\_before\_gm\_grey\_24dp.svg)_ Community](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#) 
    *   [Recorded Talks](https://go.dev/talks/)
    *   [Meetups _![Image 22](https://pkg.go.dev/static/shared/icon/launch\_gm\_grey\_24dp.svg)_](https://www.meetup.com/pro/go)
    *   [Conferences _![Image 23](https://pkg.go.dev/static/shared/icon/launch\_gm\_grey\_24dp.svg)_](https://github.com/golang/go/wiki/Conferences)
    *   [Go blog](https://go.dev/blog)
    *   [Go project](https://go.dev/help)
    *   Get connected [![Image 24](https://pkg.go.dev/static/shared/logo/social/google-groups.svg)](https://groups.google.com/g/golang-nuts)[![Image 25](https://pkg.go.dev/static/shared/logo/social/github.svg)](https://github.com/golang)[![Image 26](https://pkg.go.dev/static/shared/logo/social/twitter.svg)](https://twitter.com/golang)[![Image 27](https://pkg.go.dev/static/shared/logo/social/reddit.svg)](https://www.reddit.com/r/golang/)[![Image 28](https://pkg.go.dev/static/shared/logo/social/slack.svg)](https://invite.slack.golangbridge.org/)[![Image 29](https://pkg.go.dev/static/shared/logo/social/stack-overflow.svg)](https://stackoverflow.com/collectives/go) 

1.   [Discover Packages](https://pkg.go.dev/)
2.   [go.temporal.io/server](https://pkg.go.dev/go.temporal.io/server@v1.30.0)
3.   [common](https://pkg.go.dev/go.temporal.io/server/common@v1.30.0)
4.   [authorization](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization)![Image 30](https://pkg.go.dev/static/shared/icon/content_copy_gm_grey_24dp.svg)

[![Image 31: Go](https://pkg.go.dev/static/shared/logo/go-blue.svg)](https://go.dev/)
authorization
=============

package![Image 32](https://pkg.go.dev/static/shared/icon/content_copy_gm_grey_24dp.svg)

[Version: v1.30.0](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization?tab=versions)

 Opens a new window with list of versions in this module. 

Latest Latest 

![Image 33: Warning](https://pkg.go.dev/static/shared/icon/alert_gm_grey_24dp.svg)
This package is not in the latest version of its module.

[Go to latest](https://pkg.go.dev/go.temporal.io/server/common/authorization) Published: Feb 4, 2026  License: [MIT](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization?tab=licenses)

 Opens a new window with license information. 

[Imports: 34](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization?tab=imports)

 Opens a new window with list of imports. 

[Imported by: 15](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization?tab=importedby)

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

*   [Documentation](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#section-documentation)
    *   [Overview](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#pkg-overview)
    *   [Index](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#pkg-index)
    *   [Constants](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#pkg-constants)
    *   [Variables](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#pkg-variables)
    *   [Functions](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#pkg-functions)
        *   [IsHealthCheckAPI(fullApi)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#IsHealthCheckAPI "IsHealthCheckAPI(fullApi)")
        *   [IsNoopAuthorizer(authorizer)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#IsNoopAuthorizer "IsNoopAuthorizer(authorizer)")
        *   [IsReadOnlyGlobalAPI(workflowServiceMethod)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#IsReadOnlyGlobalAPI "IsReadOnlyGlobalAPI(workflowServiceMethod)")
        *   [IsReadOnlyNamespaceAPI(workflowServiceMethod)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#IsReadOnlyNamespaceAPI "IsReadOnlyNamespaceAPI(workflowServiceMethod)")
        *   [NewDefaultTokenKeyProvider(cfg, logger)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#NewDefaultTokenKeyProvider "NewDefaultTokenKeyProvider(cfg, logger)")
        *   [PeerCert(tlsInfo)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#PeerCert "PeerCert(tlsInfo)")
        *   [TLSInfoFromContext(ctx)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#TLSInfoFromContext "TLSInfoFromContext(ctx)")

    *   [Types](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#pkg-types)
        *   [type AudienceMapper](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#AudienceMapper "type AudienceMapper")
            *   [(m) Audience(ctx, req, info)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#AudienceMapper.Audience "(m) Audience(ctx, req, info)")

        *   [type AuthInfo](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#AuthInfo "type AuthInfo")
        *   [type Authorizer](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#Authorizer "type Authorizer")
            *   [GetAuthorizerFromConfig(config)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#GetAuthorizerFromConfig "GetAuthorizerFromConfig(config)")
            *   [NewDefaultAuthorizer()](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#NewDefaultAuthorizer "NewDefaultAuthorizer()")
            *   [NewNoopAuthorizer()](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#NewNoopAuthorizer "NewNoopAuthorizer()")

        *   [type CallTarget](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#CallTarget "type CallTarget")
        *   [type ClaimMapper](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#ClaimMapper "type ClaimMapper")
            *   [GetClaimMapperFromConfig(config, logger)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#GetClaimMapperFromConfig "GetClaimMapperFromConfig(config, logger)")
            *   [NewDefaultJWTClaimMapper(provider, cfg, logger)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#NewDefaultJWTClaimMapper "NewDefaultJWTClaimMapper(provider, cfg, logger)")
            *   [NewNoopClaimMapper()](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#NewNoopClaimMapper "NewNoopClaimMapper()")

        *   [type ClaimMapperWithAuthInfoRequired](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#ClaimMapperWithAuthInfoRequired "type ClaimMapperWithAuthInfoRequired")
        *   [type Claims](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#Claims "type Claims")
        *   [type Decision](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#Decision "type Decision")
        *   [type Interceptor](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#Interceptor "type Interceptor")
            *   [NewInterceptor(claimMapper, authorizer, metricsHandler, logger, namespaceChecker, ...)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#NewInterceptor "NewInterceptor(claimMapper, authorizer, metricsHandler, logger, namespaceChecker, ...)")
            *   [(a) Authorize(ctx, claims, ct)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#Interceptor.Authorize "(a) Authorize(ctx, claims, ct)")
            *   [(a) EnhanceContext(ctx, authInfo, claims)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#Interceptor.EnhanceContext "(a) EnhanceContext(ctx, authInfo, claims)")
            *   [(a) GetAuthInfo(tlsConnection, header, audienceGetter)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#Interceptor.GetAuthInfo "(a) GetAuthInfo(tlsConnection, header, audienceGetter)")
            *   [(a) GetClaims(authInfo)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#Interceptor.GetClaims "(a) GetClaims(authInfo)")
            *   [(a) Intercept(ctx, req, info, handler)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#Interceptor.Intercept "(a) Intercept(ctx, req, info, handler)")

        *   [type JWTAudienceMapper](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#JWTAudienceMapper "type JWTAudienceMapper")
            *   [GetAudienceMapperFromConfig(cfg)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#GetAudienceMapperFromConfig "GetAudienceMapperFromConfig(cfg)")
            *   [NewAudienceMapper(audience)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#NewAudienceMapper "NewAudienceMapper(audience)")

        *   [type MockAuthorizer](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#MockAuthorizer "type MockAuthorizer")
            *   [NewMockAuthorizer(ctrl)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#NewMockAuthorizer "NewMockAuthorizer(ctrl)")
            *   [(m) Authorize(ctx, caller, target)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#MockAuthorizer.Authorize "(m) Authorize(ctx, caller, target)")
            *   [(m) EXPECT()](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#MockAuthorizer.EXPECT "(m) EXPECT()")

        *   [type MockAuthorizerMockRecorder](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#MockAuthorizerMockRecorder "type MockAuthorizerMockRecorder")
            *   [(mr) Authorize(ctx, caller, target)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#MockAuthorizerMockRecorder.Authorize "(mr) Authorize(ctx, caller, target)")

        *   [type MockClaimMapper](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#MockClaimMapper "type MockClaimMapper")
            *   [NewMockClaimMapper(ctrl)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#NewMockClaimMapper "NewMockClaimMapper(ctrl)")
            *   [(m) EXPECT()](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#MockClaimMapper.EXPECT "(m) EXPECT()")
            *   [(m) GetClaims(authInfo)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#MockClaimMapper.GetClaims "(m) GetClaims(authInfo)")

        *   [type MockClaimMapperMockRecorder](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#MockClaimMapperMockRecorder "type MockClaimMapperMockRecorder")
            *   [(mr) GetClaims(authInfo)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#MockClaimMapperMockRecorder.GetClaims "(mr) GetClaims(authInfo)")

        *   [type MockClaimMapperWithAuthInfoRequired](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#MockClaimMapperWithAuthInfoRequired "type MockClaimMapperWithAuthInfoRequired")
            *   [NewMockClaimMapperWithAuthInfoRequired(ctrl)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#NewMockClaimMapperWithAuthInfoRequired "NewMockClaimMapperWithAuthInfoRequired(ctrl)")
            *   [(m) AuthInfoRequired()](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#MockClaimMapperWithAuthInfoRequired.AuthInfoRequired "(m) AuthInfoRequired()")
            *   [(m) EXPECT()](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#MockClaimMapperWithAuthInfoRequired.EXPECT "(m) EXPECT()")

        *   [type MockClaimMapperWithAuthInfoRequiredMockRecorder](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#MockClaimMapperWithAuthInfoRequiredMockRecorder "type MockClaimMapperWithAuthInfoRequiredMockRecorder")
            *   [(mr) AuthInfoRequired()](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#MockClaimMapperWithAuthInfoRequiredMockRecorder.AuthInfoRequired "(mr) AuthInfoRequired()")

        *   [type MockJWTAudienceMapper](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#MockJWTAudienceMapper "type MockJWTAudienceMapper")
            *   [NewMockJWTAudienceMapper(ctrl)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#NewMockJWTAudienceMapper "NewMockJWTAudienceMapper(ctrl)")
            *   [(m) Audience(ctx, req, info)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#MockJWTAudienceMapper.Audience "(m) Audience(ctx, req, info)")
            *   [(m) EXPECT()](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#MockJWTAudienceMapper.EXPECT "(m) EXPECT()")

        *   [type MockJWTAudienceMapperMockRecorder](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#MockJWTAudienceMapperMockRecorder "type MockJWTAudienceMapperMockRecorder")
            *   [(mr) Audience(ctx, req, info)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#MockJWTAudienceMapperMockRecorder.Audience "(mr) Audience(ctx, req, info)")

        *   [type MockhasNamespace](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#MockhasNamespace "type MockhasNamespace")
            *   [NewMockhasNamespace(ctrl)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#NewMockhasNamespace "NewMockhasNamespace(ctrl)")
            *   [(m) EXPECT()](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#MockhasNamespace.EXPECT "(m) EXPECT()")
            *   [(m) GetNamespace()](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#MockhasNamespace.GetNamespace "(m) GetNamespace()")

        *   [type MockhasNamespaceMockRecorder](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#MockhasNamespaceMockRecorder "type MockhasNamespaceMockRecorder")
            *   [(mr) GetNamespace()](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#MockhasNamespaceMockRecorder.GetNamespace "(mr) GetNamespace()")

        *   [type NamespaceChecker](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#NamespaceChecker "type NamespaceChecker")
        *   [type RawTokenKeyProvider](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#RawTokenKeyProvider "type RawTokenKeyProvider")
        *   [type Result](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#Result "type Result")
        *   [type Role](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#Role "type Role")
            *   [(b) IsValid()](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#Role.IsValid "(b) IsValid()")

        *   [type TokenKeyProvider](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#TokenKeyProvider "type TokenKeyProvider")

*   [Source Files](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#section-sourcefiles)

![Image 43](https://pkg.go.dev/static/shared/icon/code_gm_grey_24dp.svg) Documentation [¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#section-documentation "Go to Documentation")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Overview [¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#pkg-overview "Go to Overview")

Package authorization is a generated GoMock package.

Package authorization is a generated GoMock package.

Package authorization is a generated GoMock package.

### Index [¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#pkg-index "Go to Index")

*   [Constants](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#pkg-constants)
*   [Variables](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#pkg-variables)
*   [func IsHealthCheckAPI(fullApi string) bool](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#IsHealthCheckAPI)
*   [func IsNoopAuthorizer(authorizer Authorizer) bool](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#IsNoopAuthorizer)
*   [func IsReadOnlyGlobalAPI(workflowServiceMethod string) bool](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#IsReadOnlyGlobalAPI)
*   [func IsReadOnlyNamespaceAPI(workflowServiceMethod string) bool](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#IsReadOnlyNamespaceAPI)
*   [func NewDefaultTokenKeyProvider(cfg *config.Authorization, logger log.Logger) *defaultTokenKeyProvider](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#NewDefaultTokenKeyProvider)
*   [func PeerCert(tlsInfo *credentials.TLSInfo) *x509.Certificate](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#PeerCert)
*   [func TLSInfoFromContext(ctx context.Context) *credentials.TLSInfo](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#TLSInfoFromContext)
*   [type AudienceMapper](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#AudienceMapper)
*       *   [func (m *AudienceMapper) Audience(ctx context.Context, req interface{}, info *grpc.UnaryServerInfo) string](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#AudienceMapper.Audience)

*   [type AuthInfo](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#AuthInfo)
*   [type Authorizer](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#Authorizer)
*       *   [func GetAuthorizerFromConfig(config *config.Authorization) (Authorizer, error)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#GetAuthorizerFromConfig)
    *   [func NewDefaultAuthorizer() Authorizer](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#NewDefaultAuthorizer)
    *   [func NewNoopAuthorizer() Authorizer](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#NewNoopAuthorizer)

*   [type CallTarget](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#CallTarget)
*   [type ClaimMapper](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#ClaimMapper)
*       *   [func GetClaimMapperFromConfig(config *config.Authorization, logger log.Logger) (ClaimMapper, error)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#GetClaimMapperFromConfig)
    *   [func NewDefaultJWTClaimMapper(provider TokenKeyProvider, cfg *config.Authorization, logger log.Logger) ClaimMapper](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#NewDefaultJWTClaimMapper)
    *   [func NewNoopClaimMapper() ClaimMapper](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#NewNoopClaimMapper)

*   [type ClaimMapperWithAuthInfoRequired](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#ClaimMapperWithAuthInfoRequired)
*   [type Claims](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#Claims)
*   [type Decision](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#Decision)
*   [type Interceptor](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#Interceptor)
*       *   [func NewInterceptor(claimMapper ClaimMapper, authorizer Authorizer, metricsHandler metrics.Handler, ...) *Interceptor](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#NewInterceptor)

*       *   [func (a *Interceptor) Authorize(ctx context.Context, claims *Claims, ct *CallTarget) error](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#Interceptor.Authorize)
    *   [func (a *Interceptor) EnhanceContext(ctx context.Context, authInfo *AuthInfo, claims *Claims) context.Context](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#Interceptor.EnhanceContext)
    *   [func (a *Interceptor) GetAuthInfo(tlsConnection *credentials.TLSInfo, header headers.HeaderGetter, ...) *AuthInfo](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#Interceptor.GetAuthInfo)
    *   [func (a *Interceptor) GetClaims(authInfo *AuthInfo) (*Claims, error)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#Interceptor.GetClaims)
    *   [func (a *Interceptor) Intercept(ctx context.Context, req interface{}, info *grpc.UnaryServerInfo, ...) (interface{}, error)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#Interceptor.Intercept)

*   [type JWTAudienceMapper](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#JWTAudienceMapper)
*       *   [func GetAudienceMapperFromConfig(cfg *config.Authorization) (JWTAudienceMapper, error)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#GetAudienceMapperFromConfig)
    *   [func NewAudienceMapper(audience string) JWTAudienceMapper](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#NewAudienceMapper)

*   [type MockAuthorizer](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#MockAuthorizer)
*       *   [func NewMockAuthorizer(ctrl *gomock.Controller) *MockAuthorizer](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#NewMockAuthorizer)

*       *   [func (m *MockAuthorizer) Authorize(ctx context.Context, caller *Claims, target *CallTarget) (Result, error)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#MockAuthorizer.Authorize)
    *   [func (m *MockAuthorizer) EXPECT() *MockAuthorizerMockRecorder](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#MockAuthorizer.EXPECT)

*   [type MockAuthorizerMockRecorder](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#MockAuthorizerMockRecorder)
*       *   [func (mr *MockAuthorizerMockRecorder) Authorize(ctx, caller, target any) *gomock.Call](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#MockAuthorizerMockRecorder.Authorize)

*   [type MockClaimMapper](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#MockClaimMapper)
*       *   [func NewMockClaimMapper(ctrl *gomock.Controller) *MockClaimMapper](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#NewMockClaimMapper)

*       *   [func (m *MockClaimMapper) EXPECT() *MockClaimMapperMockRecorder](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#MockClaimMapper.EXPECT)
    *   [func (m *MockClaimMapper) GetClaims(authInfo *AuthInfo) (*Claims, error)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#MockClaimMapper.GetClaims)

*   [type MockClaimMapperMockRecorder](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#MockClaimMapperMockRecorder)
*       *   [func (mr *MockClaimMapperMockRecorder) GetClaims(authInfo any) *gomock.Call](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#MockClaimMapperMockRecorder.GetClaims)

*   [type MockClaimMapperWithAuthInfoRequired](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#MockClaimMapperWithAuthInfoRequired)
*       *   [func NewMockClaimMapperWithAuthInfoRequired(ctrl *gomock.Controller) *MockClaimMapperWithAuthInfoRequired](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#NewMockClaimMapperWithAuthInfoRequired)

*       *   [func (m *MockClaimMapperWithAuthInfoRequired) AuthInfoRequired() bool](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#MockClaimMapperWithAuthInfoRequired.AuthInfoRequired)
    *   [func (m *MockClaimMapperWithAuthInfoRequired) EXPECT() *MockClaimMapperWithAuthInfoRequiredMockRecorder](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#MockClaimMapperWithAuthInfoRequired.EXPECT)

*   [type MockClaimMapperWithAuthInfoRequiredMockRecorder](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#MockClaimMapperWithAuthInfoRequiredMockRecorder)
*       *   [func (mr *MockClaimMapperWithAuthInfoRequiredMockRecorder) AuthInfoRequired() *gomock.Call](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#MockClaimMapperWithAuthInfoRequiredMockRecorder.AuthInfoRequired)

*   [type MockJWTAudienceMapper](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#MockJWTAudienceMapper)
*       *   [func NewMockJWTAudienceMapper(ctrl *gomock.Controller) *MockJWTAudienceMapper](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#NewMockJWTAudienceMapper)

*       *   [func (m *MockJWTAudienceMapper) Audience(ctx context.Context, req interface{}, info *grpc.UnaryServerInfo) string](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#MockJWTAudienceMapper.Audience)
    *   [func (m *MockJWTAudienceMapper) EXPECT() *MockJWTAudienceMapperMockRecorder](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#MockJWTAudienceMapper.EXPECT)

*   [type MockJWTAudienceMapperMockRecorder](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#MockJWTAudienceMapperMockRecorder)
*       *   [func (mr *MockJWTAudienceMapperMockRecorder) Audience(ctx, req, info interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#MockJWTAudienceMapperMockRecorder.Audience)

*   [type MockhasNamespace](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#MockhasNamespace)
*       *   [func NewMockhasNamespace(ctrl *gomock.Controller) *MockhasNamespace](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#NewMockhasNamespace)

*       *   [func (m *MockhasNamespace) EXPECT() *MockhasNamespaceMockRecorder](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#MockhasNamespace.EXPECT)
    *   [func (m *MockhasNamespace) GetNamespace() string](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#MockhasNamespace.GetNamespace)

*   [type MockhasNamespaceMockRecorder](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#MockhasNamespaceMockRecorder)
*       *   [func (mr *MockhasNamespaceMockRecorder) GetNamespace() *gomock.Call](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#MockhasNamespaceMockRecorder.GetNamespace)

*   [type NamespaceChecker](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#NamespaceChecker)
*   [type RawTokenKeyProvider](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#RawTokenKeyProvider)
*   [type Result](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#Result)
*   [type Role](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#Role)
*       *   [func (b Role) IsValid() bool](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#Role.IsValid)

*   [type TokenKeyProvider](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#TokenKeyProvider)

### Constants [¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#pkg-constants "Go to Constants")

[View Source](https://github.com/temporalio/temporal/blob/v1.30.0/common/authorization/roles.go#L8)const (
 RoleWorker = [Role](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#Role)(1 << [iota](https://pkg.go.dev/builtin#iota))  RoleReader  RoleWriter  RoleAdmin  RoleUndefined = [Role](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#Role)(0) )

@@@SNIPSTART temporal-common-authorization-role-enum User authz within the context of an entity, such as system, namespace or workflow. User may have any combination of these authz within each context, except for RoleUndefined, as a bitmask.

[View Source](https://github.com/temporalio/temporal/blob/v1.30.0/common/authorization/interceptor.go#L42)const (
 RequestUnauthorized = "Request unauthorized." )

### Variables [¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#pkg-variables "Go to Variables")

[View Source](https://github.com/temporalio/temporal/blob/v1.30.0/common/authorization/interceptor.go#L49)var (
 MappedClaims contextKeyMappedClaims  AuthHeader contextKeyAuthHeader )

### Functions [¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#pkg-functions "Go to Functions")

#### func [IsHealthCheckAPI](https://github.com/temporalio/temporal/blob/v1.30.0/common/authorization/frontend_api.go#L25)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#IsHealthCheckAPI "Go to IsHealthCheckAPI")added in v1.20.0

func IsHealthCheckAPI(fullApi [string](https://pkg.go.dev/builtin#string)) [bool](https://pkg.go.dev/builtin#bool)

#### func [IsNoopAuthorizer](https://github.com/temporalio/temporal/blob/v1.30.0/common/authorization/authorizer.go#L72)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#IsNoopAuthorizer "Go to IsNoopAuthorizer")added in v1.18.0

func IsNoopAuthorizer(authorizer [Authorizer](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#Authorizer)) [bool](https://pkg.go.dev/builtin#bool)

#### func [IsReadOnlyGlobalAPI](https://github.com/temporalio/temporal/blob/v1.30.0/common/authorization/frontend_api.go#L19)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#IsReadOnlyGlobalAPI "Go to IsReadOnlyGlobalAPI")added in v1.11.0

func IsReadOnlyGlobalAPI(workflowServiceMethod [string](https://pkg.go.dev/builtin#string)) [bool](https://pkg.go.dev/builtin#bool)

#### func [IsReadOnlyNamespaceAPI](https://github.com/temporalio/temporal/blob/v1.30.0/common/authorization/frontend_api.go#L13)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#IsReadOnlyNamespaceAPI "Go to IsReadOnlyNamespaceAPI")added in v1.11.0

func IsReadOnlyNamespaceAPI(workflowServiceMethod [string](https://pkg.go.dev/builtin#string)) [bool](https://pkg.go.dev/builtin#bool)

#### func [NewDefaultTokenKeyProvider](https://github.com/temporalio/temporal/blob/v1.30.0/common/authorization/default_token_key_provider.go#L34)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#NewDefaultTokenKeyProvider "Go to NewDefaultTokenKeyProvider")added in v1.5.0

func NewDefaultTokenKeyProvider(cfg *[config](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config).[Authorization](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#Authorization), logger [log](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/log).[Logger](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/log#Logger)) *defaultTokenKeyProvider

#### func [PeerCert](https://github.com/temporalio/temporal/blob/v1.30.0/common/authorization/interceptor.go#L69)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#PeerCert "Go to PeerCert")added in v1.11.0

func PeerCert(tlsInfo *[credentials](https://pkg.go.dev/google.golang.org/grpc/credentials).[TLSInfo](https://pkg.go.dev/google.golang.org/grpc/credentials#TLSInfo)) *[x509](https://pkg.go.dev/crypto/x509).[Certificate](https://pkg.go.dev/crypto/x509#Certificate)

PeerCert extracts an x509 certificate from given tlsInfo.

#### func [TLSInfoFromContext](https://github.com/temporalio/temporal/blob/v1.30.0/common/authorization/interceptor.go#L57)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#TLSInfoFromContext "Go to TLSInfoFromContext")added in v1.24.0

func TLSInfoFromContext(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context)) *[credentials](https://pkg.go.dev/google.golang.org/grpc/credentials).[TLSInfo](https://pkg.go.dev/google.golang.org/grpc/credentials#TLSInfo)

TLSInfoFromContext extracts TLS information from the context's peer value.

### Types [¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#pkg-types "Go to Types")

#### type [AudienceMapper](https://github.com/temporalio/temporal/blob/v1.30.0/common/authorization/audience_mapper.go#L11)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#AudienceMapper "Go to AudienceMapper")added in v1.29.0

type AudienceMapper struct {
 JwtAudience [string](https://pkg.go.dev/builtin#string)}

AudienceMapper is a simple implementation of JWTAudienceMapper that returns the configured audience string.

#### func (*AudienceMapper) [Audience](https://github.com/temporalio/temporal/blob/v1.30.0/common/authorization/audience_mapper.go#L16)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#AudienceMapper.Audience "Go to AudienceMapper.Audience")added in v1.29.0

func (m *[AudienceMapper](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#AudienceMapper)) Audience(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req interface{}, info *[grpc](https://pkg.go.dev/google.golang.org/grpc).[UnaryServerInfo](https://pkg.go.dev/google.golang.org/grpc#UnaryServerInfo)) [string](https://pkg.go.dev/builtin#string)

Audience returns the configured audience string.

#### type [AuthInfo](https://github.com/temporalio/temporal/blob/v1.30.0/common/authorization/claim_mapper.go#L17)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#AuthInfo "Go to AuthInfo")added in v1.4.0

type AuthInfo struct {
 AuthToken [string](https://pkg.go.dev/builtin#string) TLSSubject *[pkix](https://pkg.go.dev/crypto/x509/pkix).[Name](https://pkg.go.dev/crypto/x509/pkix#Name) TLSConnection *[credentials](https://pkg.go.dev/google.golang.org/grpc/credentials).[TLSInfo](https://pkg.go.dev/google.golang.org/grpc/credentials#TLSInfo) ExtraData [string](https://pkg.go.dev/builtin#string) Audience [string](https://pkg.go.dev/builtin#string)}

@@@SNIPSTART temporal-common-authorization-authinfo Authentication information from subject's JWT token or/and mTLS certificate

#### type [Authorizer](https://github.com/temporalio/temporal/blob/v1.30.0/common/authorization/authorizer.go#L51)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#Authorizer "Go to Authorizer")

type Authorizer interface {
 Authorize(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), caller *[Claims](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#Claims), target *[CallTarget](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#CallTarget)) ([Result](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#Result), [error](https://pkg.go.dev/builtin#error)) }

@@@SNIPSTART temporal-common-authorization-authorizer-interface Authorizer is an interface for implementing authorization logic

#### func [GetAuthorizerFromConfig](https://github.com/temporalio/temporal/blob/v1.30.0/common/authorization/authorizer.go#L61)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#GetAuthorizerFromConfig "Go to GetAuthorizerFromConfig")added in v1.5.7

func GetAuthorizerFromConfig(config *[config](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config).[Authorization](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#Authorization)) ([Authorizer](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#Authorizer), [error](https://pkg.go.dev/builtin#error))

#### func [NewDefaultAuthorizer](https://github.com/temporalio/temporal/blob/v1.30.0/common/authorization/default_authorizer.go#L17)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#NewDefaultAuthorizer "Go to NewDefaultAuthorizer")added in v1.4.0

func NewDefaultAuthorizer() [Authorizer](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#Authorizer)

NewDefaultAuthorizer creates a default authorizer

#### func [NewNoopAuthorizer](https://github.com/temporalio/temporal/blob/v1.30.0/common/authorization/noop_authorizer.go#L8)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#NewNoopAuthorizer "Go to NewNoopAuthorizer")added in v1.5.7

func NewNoopAuthorizer() [Authorizer](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#Authorizer)

NewNoopAuthorizer creates a no-op authorizer

#### type [CallTarget](https://github.com/temporalio/temporal/blob/v1.30.0/common/authorization/authorizer.go#L23)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#CallTarget "Go to CallTarget")added in v1.4.0

type CallTarget struct {
// APIName must be the full API function name.	// Example: "/temporal.api.workflowservice.v1.WorkflowService/StartWorkflowExecution".
	APIName [string](https://pkg.go.dev/builtin#string)
// If a Namespace is not being targeted this be set to an empty string.	Namespace [string](https://pkg.go.dev/builtin#string)
// The nexus endpoint name being targeted (if any).	NexusEndpointName [string](https://pkg.go.dev/builtin#string)
// Request contains a deserialized copy of the API request object	Request interface{}
}

@@@SNIPSTART temporal-common-authorization-authorizer-calltarget CallTarget is contains information for Authorizer to make a decision. It can be extended to include resources like WorkflowType and TaskQueue

#### type [ClaimMapper](https://github.com/temporalio/temporal/blob/v1.30.0/common/authorization/claim_mapper.go#L29)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#ClaimMapper "Go to ClaimMapper")added in v1.4.0

type ClaimMapper interface {
 GetClaims(authInfo *[AuthInfo](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#AuthInfo)) (*[Claims](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#Claims), [error](https://pkg.go.dev/builtin#error)) }

@@@SNIPSTART temporal-common-authorization-claimmapper-interface ClaimMapper converts authorization info of a subject into Temporal claims (permissions) for authorization

#### func [GetClaimMapperFromConfig](https://github.com/temporalio/temporal/blob/v1.30.0/common/authorization/claim_mapper.go#L61)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#GetClaimMapperFromConfig "Go to GetClaimMapperFromConfig")added in v1.5.7

func GetClaimMapperFromConfig(config *[config](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config).[Authorization](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#Authorization), logger [log](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/log).[Logger](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/log#Logger)) ([ClaimMapper](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#ClaimMapper), [error](https://pkg.go.dev/builtin#error))

#### func [NewDefaultJWTClaimMapper](https://github.com/temporalio/temporal/blob/v1.30.0/common/authorization/default_jwt_claim_mapper.go#L37)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#NewDefaultJWTClaimMapper "Go to NewDefaultJWTClaimMapper")added in v1.4.0

func NewDefaultJWTClaimMapper(provider [TokenKeyProvider](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#TokenKeyProvider), cfg *[config](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config).[Authorization](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#Authorization), logger [log](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/log).[Logger](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/log#Logger)) [ClaimMapper](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#ClaimMapper)

#### func [NewNoopClaimMapper](https://github.com/temporalio/temporal/blob/v1.30.0/common/authorization/claim_mapper.go#L48)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#NewNoopClaimMapper "Go to NewNoopClaimMapper")added in v1.4.0

func NewNoopClaimMapper() [ClaimMapper](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#ClaimMapper)

#### type [ClaimMapperWithAuthInfoRequired](https://github.com/temporalio/temporal/blob/v1.30.0/common/authorization/claim_mapper.go#L38)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#ClaimMapperWithAuthInfoRequired "Go to ClaimMapperWithAuthInfoRequired")added in v1.20.3

type ClaimMapperWithAuthInfoRequired interface {
 AuthInfoRequired() [bool](https://pkg.go.dev/builtin#bool)}

Normally, GetClaims will never be called without either an auth token or TLS metadata set in AuthInfo. However, if you want your ClaimMapper to be called in all cases, you can implement this additional interface and return false.

#### type [Claims](https://github.com/temporalio/temporal/blob/v1.30.0/common/authorization/roles.go#L25)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#Claims "Go to Claims")added in v1.4.0

type Claims struct {
// Identity of the subject	Subject [string](https://pkg.go.dev/builtin#string)
// Role within the context of the whole Temporal cluster or a multi-cluster setup	System [Role](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#Role)
// Roles within specific namespaces	Namespaces map[[string](https://pkg.go.dev/builtin#string)][Role](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#Role)
// Free form bucket for extra data	Extensions interface{}
}

@@@SNIPSTART temporal-common-authorization-claims Claims contains the identity of the subject and subject's roles at the system level and for individual namespaces

#### type [Decision](https://github.com/temporalio/temporal/blob/v1.30.0/common/authorization/authorizer.go#L46)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#Decision "Go to Decision")

type Decision [int](https://pkg.go.dev/builtin#int)

Decision is enum type for auth decision

const (
// DecisionDeny means auth decision is deny	DecisionDeny [Decision](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#Decision) = [iota](https://pkg.go.dev/builtin#iota) + 1
// DecisionAllow means auth decision is allow	DecisionAllow
)

#### type [Interceptor](https://github.com/temporalio/temporal/blob/v1.30.0/common/authorization/interceptor.go#L82)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#Interceptor "Go to Interceptor")added in v1.24.0

type Interceptor struct {
	// contains filtered or unexported fields
}

#### func [NewInterceptor](https://github.com/temporalio/temporal/blob/v1.30.0/common/authorization/interceptor.go#L96)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#NewInterceptor "Go to NewInterceptor")added in v1.24.0

func NewInterceptor(
	claimMapper [ClaimMapper](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#ClaimMapper),
	authorizer [Authorizer](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#Authorizer),
	metricsHandler [metrics](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/metrics).[Handler](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/metrics#Handler),
	logger [log](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/log).[Logger](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/log#Logger),
	namespaceChecker [NamespaceChecker](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#NamespaceChecker),
	audienceGetter [JWTAudienceMapper](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#JWTAudienceMapper),
	authHeaderName [string](https://pkg.go.dev/builtin#string),
	authExtraHeaderName [string](https://pkg.go.dev/builtin#string),
	exposeAuthorizerErrors [dynamicconfig](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/dynamicconfig).[BoolPropertyFn](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/dynamicconfig#BoolPropertyFn),
	enableCrossNamespaceCommands [dynamicconfig](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/dynamicconfig).[BoolPropertyFn](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/dynamicconfig#BoolPropertyFn),
) *[Interceptor](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#Interceptor)

NewInterceptor creates an authorization interceptor.

#### func (*Interceptor) [Authorize](https://github.com/temporalio/temporal/blob/v1.30.0/common/authorization/interceptor.go#L227)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#Interceptor.Authorize "Go to Interceptor.Authorize")added in v1.24.0

func (a *[Interceptor](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#Interceptor)) Authorize(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), claims *[Claims](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#Claims), ct *[CallTarget](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#CallTarget)) [error](https://pkg.go.dev/builtin#error)

Authorize uses the policy's authorizer to authorize a request based on provided claims and call target. Logs and emits metrics when unauthorized.

#### func (*Interceptor) [EnhanceContext](https://github.com/temporalio/temporal/blob/v1.30.0/common/authorization/interceptor.go#L217)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#Interceptor.EnhanceContext "Go to Interceptor.EnhanceContext")added in v1.24.0

func (a *[Interceptor](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#Interceptor)) EnhanceContext(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), authInfo *[AuthInfo](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#AuthInfo), claims *[Claims](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#Claims)) [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context)

EnhanceContext returns a new context with [MappedClaims](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#MappedClaims) and [AuthHeader](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#AuthHeader) values.

#### func (*Interceptor) [GetAuthInfo](https://github.com/temporalio/temporal/blob/v1.30.0/common/authorization/interceptor.go#L175)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#Interceptor.GetAuthInfo "Go to Interceptor.GetAuthInfo")added in v1.24.0

func (a *[Interceptor](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#Interceptor)) GetAuthInfo(tlsConnection *[credentials](https://pkg.go.dev/google.golang.org/grpc/credentials).[TLSInfo](https://pkg.go.dev/google.golang.org/grpc/credentials#TLSInfo), header [headers](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/headers).[HeaderGetter](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/headers#HeaderGetter), audienceGetter func() [string](https://pkg.go.dev/builtin#string)) *[AuthInfo](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#AuthInfo)

GetAuthInfo extracts auth info from TLS info and headers. Returns nil if either the policy's claimMapper or authorizer are nil or when there is no auth information in the provided TLS info or headers.

#### func (*Interceptor) [GetClaims](https://github.com/temporalio/temporal/blob/v1.30.0/common/authorization/interceptor.go#L212)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#Interceptor.GetClaims "Go to Interceptor.GetClaims")added in v1.24.0

func (a *[Interceptor](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#Interceptor)) GetClaims(authInfo *[AuthInfo](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#AuthInfo)) (*[Claims](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#Claims), [error](https://pkg.go.dev/builtin#error))

GetClaims uses the policy's claimMapper to map the provided authInfo to claims.

#### func (*Interceptor) [Intercept](https://github.com/temporalio/temporal/blob/v1.30.0/common/authorization/interceptor.go#L122)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#Interceptor.Intercept "Go to Interceptor.Intercept")added in v1.24.0

func (a *[Interceptor](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#Interceptor)) Intercept(
	ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context),
	req interface{},
	info *[grpc](https://pkg.go.dev/google.golang.org/grpc).[UnaryServerInfo](https://pkg.go.dev/google.golang.org/grpc#UnaryServerInfo),
	handler [grpc](https://pkg.go.dev/google.golang.org/grpc).[UnaryHandler](https://pkg.go.dev/google.golang.org/grpc#UnaryHandler),
) (interface{}, [error](https://pkg.go.dev/builtin#error))

#### type [JWTAudienceMapper](https://github.com/temporalio/temporal/blob/v1.30.0/common/authorization/interceptor.go#L32)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#JWTAudienceMapper "Go to JWTAudienceMapper")added in v1.10.3

type JWTAudienceMapper interface {
 Audience(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req interface{}, info *[grpc](https://pkg.go.dev/google.golang.org/grpc).[UnaryServerInfo](https://pkg.go.dev/google.golang.org/grpc#UnaryServerInfo)) [string](https://pkg.go.dev/builtin#string)}

JWTAudienceMapper returns JWT audience for a given request

#### func [GetAudienceMapperFromConfig](https://github.com/temporalio/temporal/blob/v1.30.0/common/authorization/audience_mapper.go#L27)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#GetAudienceMapperFromConfig "Go to GetAudienceMapperFromConfig")added in v1.29.0

func GetAudienceMapperFromConfig(cfg *[config](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config).[Authorization](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#Authorization)) ([JWTAudienceMapper](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#JWTAudienceMapper), [error](https://pkg.go.dev/builtin#error))

GetAudienceMapperFromConfig returns a JWTAudienceMapper based on the provided Authorization config. Currently, it returns a static audience mapper using the Audience field.

#### func [NewAudienceMapper](https://github.com/temporalio/temporal/blob/v1.30.0/common/authorization/audience_mapper.go#L21)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#NewAudienceMapper "Go to NewAudienceMapper")added in v1.29.0

func NewAudienceMapper(audience [string](https://pkg.go.dev/builtin#string)) [JWTAudienceMapper](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#JWTAudienceMapper)

NewAudienceMapper returns a JWTAudienceMapper that always returns the given audience string.

#### type [MockAuthorizer](https://github.com/temporalio/temporal/blob/v1.30.0/common/authorization/authorizer_mock.go#L20)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#MockAuthorizer "Go to MockAuthorizer")

type MockAuthorizer struct {
	// contains filtered or unexported fields
}

MockAuthorizer is a mock of Authorizer interface.

#### func [NewMockAuthorizer](https://github.com/temporalio/temporal/blob/v1.30.0/common/authorization/authorizer_mock.go#L32)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#NewMockAuthorizer "Go to NewMockAuthorizer")

func NewMockAuthorizer(ctrl *[gomock](https://pkg.go.dev/go.uber.org/mock/gomock).[Controller](https://pkg.go.dev/go.uber.org/mock/gomock#Controller)) *[MockAuthorizer](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#MockAuthorizer)

NewMockAuthorizer creates a new mock instance.

#### func (*MockAuthorizer) [Authorize](https://github.com/temporalio/temporal/blob/v1.30.0/common/authorization/authorizer_mock.go#L44)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#MockAuthorizer.Authorize "Go to MockAuthorizer.Authorize")

func (m *[MockAuthorizer](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#MockAuthorizer)) Authorize(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), caller *[Claims](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#Claims), target *[CallTarget](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#CallTarget)) ([Result](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#Result), [error](https://pkg.go.dev/builtin#error))

Authorize mocks base method.

#### func (*MockAuthorizer) [EXPECT](https://github.com/temporalio/temporal/blob/v1.30.0/common/authorization/authorizer_mock.go#L39)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#MockAuthorizer.EXPECT "Go to MockAuthorizer.EXPECT")

func (m *[MockAuthorizer](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#MockAuthorizer)) EXPECT() *[MockAuthorizerMockRecorder](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#MockAuthorizerMockRecorder)

EXPECT returns an object that allows the caller to indicate expected use.

#### type [MockAuthorizerMockRecorder](https://github.com/temporalio/temporal/blob/v1.30.0/common/authorization/authorizer_mock.go#L27)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#MockAuthorizerMockRecorder "Go to MockAuthorizerMockRecorder")

type MockAuthorizerMockRecorder struct {
	// contains filtered or unexported fields
}

MockAuthorizerMockRecorder is the mock recorder for MockAuthorizer.

#### func (*MockAuthorizerMockRecorder) [Authorize](https://github.com/temporalio/temporal/blob/v1.30.0/common/authorization/authorizer_mock.go#L53)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#MockAuthorizerMockRecorder.Authorize "Go to MockAuthorizerMockRecorder.Authorize")

func (mr *[MockAuthorizerMockRecorder](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#MockAuthorizerMockRecorder)) Authorize(ctx, caller, target [any](https://pkg.go.dev/builtin#any)) *[gomock](https://pkg.go.dev/go.uber.org/mock/gomock).[Call](https://pkg.go.dev/go.uber.org/mock/gomock#Call)

Authorize indicates an expected call of Authorize.

#### type [MockClaimMapper](https://github.com/temporalio/temporal/blob/v1.30.0/common/authorization/claim_mapper_mock.go#L19)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#MockClaimMapper "Go to MockClaimMapper")added in v1.4.0

type MockClaimMapper struct {
	// contains filtered or unexported fields
}

MockClaimMapper is a mock of ClaimMapper interface.

#### func [NewMockClaimMapper](https://github.com/temporalio/temporal/blob/v1.30.0/common/authorization/claim_mapper_mock.go#L31)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#NewMockClaimMapper "Go to NewMockClaimMapper")added in v1.4.0

func NewMockClaimMapper(ctrl *[gomock](https://pkg.go.dev/go.uber.org/mock/gomock).[Controller](https://pkg.go.dev/go.uber.org/mock/gomock#Controller)) *[MockClaimMapper](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#MockClaimMapper)

NewMockClaimMapper creates a new mock instance.

#### func (*MockClaimMapper) [EXPECT](https://github.com/temporalio/temporal/blob/v1.30.0/common/authorization/claim_mapper_mock.go#L38)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#MockClaimMapper.EXPECT "Go to MockClaimMapper.EXPECT")added in v1.4.0

func (m *[MockClaimMapper](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#MockClaimMapper)) EXPECT() *[MockClaimMapperMockRecorder](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#MockClaimMapperMockRecorder)

EXPECT returns an object that allows the caller to indicate expected use.

#### func (*MockClaimMapper) [GetClaims](https://github.com/temporalio/temporal/blob/v1.30.0/common/authorization/claim_mapper_mock.go#L43)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#MockClaimMapper.GetClaims "Go to MockClaimMapper.GetClaims")added in v1.4.0

func (m *[MockClaimMapper](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#MockClaimMapper)) GetClaims(authInfo *[AuthInfo](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#AuthInfo)) (*[Claims](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#Claims), [error](https://pkg.go.dev/builtin#error))

GetClaims mocks base method.

#### type [MockClaimMapperMockRecorder](https://github.com/temporalio/temporal/blob/v1.30.0/common/authorization/claim_mapper_mock.go#L26)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#MockClaimMapperMockRecorder "Go to MockClaimMapperMockRecorder")added in v1.4.0

type MockClaimMapperMockRecorder struct {
	// contains filtered or unexported fields
}

MockClaimMapperMockRecorder is the mock recorder for MockClaimMapper.

#### func (*MockClaimMapperMockRecorder) [GetClaims](https://github.com/temporalio/temporal/blob/v1.30.0/common/authorization/claim_mapper_mock.go#L52)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#MockClaimMapperMockRecorder.GetClaims "Go to MockClaimMapperMockRecorder.GetClaims")added in v1.4.0

func (mr *[MockClaimMapperMockRecorder](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#MockClaimMapperMockRecorder)) GetClaims(authInfo [any](https://pkg.go.dev/builtin#any)) *[gomock](https://pkg.go.dev/go.uber.org/mock/gomock).[Call](https://pkg.go.dev/go.uber.org/mock/gomock#Call)

GetClaims indicates an expected call of GetClaims.

#### type [MockClaimMapperWithAuthInfoRequired](https://github.com/temporalio/temporal/blob/v1.30.0/common/authorization/claim_mapper_mock.go#L58)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#MockClaimMapperWithAuthInfoRequired "Go to MockClaimMapperWithAuthInfoRequired")added in v1.20.3

type MockClaimMapperWithAuthInfoRequired struct {
	// contains filtered or unexported fields
}

MockClaimMapperWithAuthInfoRequired is a mock of ClaimMapperWithAuthInfoRequired interface.

#### func [NewMockClaimMapperWithAuthInfoRequired](https://github.com/temporalio/temporal/blob/v1.30.0/common/authorization/claim_mapper_mock.go#L70)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#NewMockClaimMapperWithAuthInfoRequired "Go to NewMockClaimMapperWithAuthInfoRequired")added in v1.20.3

func NewMockClaimMapperWithAuthInfoRequired(ctrl *[gomock](https://pkg.go.dev/go.uber.org/mock/gomock).[Controller](https://pkg.go.dev/go.uber.org/mock/gomock#Controller)) *[MockClaimMapperWithAuthInfoRequired](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#MockClaimMapperWithAuthInfoRequired)

NewMockClaimMapperWithAuthInfoRequired creates a new mock instance.

#### func (*MockClaimMapperWithAuthInfoRequired) [AuthInfoRequired](https://github.com/temporalio/temporal/blob/v1.30.0/common/authorization/claim_mapper_mock.go#L82)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#MockClaimMapperWithAuthInfoRequired.AuthInfoRequired "Go to MockClaimMapperWithAuthInfoRequired.AuthInfoRequired")added in v1.20.3

func (m *[MockClaimMapperWithAuthInfoRequired](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#MockClaimMapperWithAuthInfoRequired)) AuthInfoRequired() [bool](https://pkg.go.dev/builtin#bool)

AuthInfoRequired mocks base method.

#### func (*MockClaimMapperWithAuthInfoRequired) [EXPECT](https://github.com/temporalio/temporal/blob/v1.30.0/common/authorization/claim_mapper_mock.go#L77)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#MockClaimMapperWithAuthInfoRequired.EXPECT "Go to MockClaimMapperWithAuthInfoRequired.EXPECT")added in v1.20.3

func (m *[MockClaimMapperWithAuthInfoRequired](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#MockClaimMapperWithAuthInfoRequired)) EXPECT() *[MockClaimMapperWithAuthInfoRequiredMockRecorder](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#MockClaimMapperWithAuthInfoRequiredMockRecorder)

EXPECT returns an object that allows the caller to indicate expected use.

#### type [MockClaimMapperWithAuthInfoRequiredMockRecorder](https://github.com/temporalio/temporal/blob/v1.30.0/common/authorization/claim_mapper_mock.go#L65)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#MockClaimMapperWithAuthInfoRequiredMockRecorder "Go to MockClaimMapperWithAuthInfoRequiredMockRecorder")added in v1.20.3

type MockClaimMapperWithAuthInfoRequiredMockRecorder struct {
	// contains filtered or unexported fields
}

MockClaimMapperWithAuthInfoRequiredMockRecorder is the mock recorder for MockClaimMapperWithAuthInfoRequired.

#### func (*MockClaimMapperWithAuthInfoRequiredMockRecorder) [AuthInfoRequired](https://github.com/temporalio/temporal/blob/v1.30.0/common/authorization/claim_mapper_mock.go#L90)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#MockClaimMapperWithAuthInfoRequiredMockRecorder.AuthInfoRequired "Go to MockClaimMapperWithAuthInfoRequiredMockRecorder.AuthInfoRequired")added in v1.20.3

func (mr *[MockClaimMapperWithAuthInfoRequiredMockRecorder](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#MockClaimMapperWithAuthInfoRequiredMockRecorder)) AuthInfoRequired() *[gomock](https://pkg.go.dev/go.uber.org/mock/gomock).[Call](https://pkg.go.dev/go.uber.org/mock/gomock#Call)

AuthInfoRequired indicates an expected call of AuthInfoRequired.

#### type [MockJWTAudienceMapper](https://github.com/temporalio/temporal/blob/v1.30.0/common/authorization/audience_mapper_mock.go#L21)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#MockJWTAudienceMapper "Go to MockJWTAudienceMapper")added in v1.29.0

type MockJWTAudienceMapper struct {
	// contains filtered or unexported fields
}

MockJWTAudienceMapper is a mock of JWTAudienceMapper interface.

#### func [NewMockJWTAudienceMapper](https://github.com/temporalio/temporal/blob/v1.30.0/common/authorization/audience_mapper_mock.go#L33)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#NewMockJWTAudienceMapper "Go to NewMockJWTAudienceMapper")added in v1.29.0

func NewMockJWTAudienceMapper(ctrl *[gomock](https://pkg.go.dev/go.uber.org/mock/gomock).[Controller](https://pkg.go.dev/go.uber.org/mock/gomock#Controller)) *[MockJWTAudienceMapper](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#MockJWTAudienceMapper)

NewMockJWTAudienceMapper creates a new mock instance.

#### func (*MockJWTAudienceMapper) [Audience](https://github.com/temporalio/temporal/blob/v1.30.0/common/authorization/audience_mapper_mock.go#L45)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#MockJWTAudienceMapper.Audience "Go to MockJWTAudienceMapper.Audience")added in v1.29.0

func (m *[MockJWTAudienceMapper](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#MockJWTAudienceMapper)) Audience(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req interface{}, info *[grpc](https://pkg.go.dev/google.golang.org/grpc).[UnaryServerInfo](https://pkg.go.dev/google.golang.org/grpc#UnaryServerInfo)) [string](https://pkg.go.dev/builtin#string)

Audience mocks base method.

#### func (*MockJWTAudienceMapper) [EXPECT](https://github.com/temporalio/temporal/blob/v1.30.0/common/authorization/audience_mapper_mock.go#L40)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#MockJWTAudienceMapper.EXPECT "Go to MockJWTAudienceMapper.EXPECT")added in v1.29.0

func (m *[MockJWTAudienceMapper](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#MockJWTAudienceMapper)) EXPECT() *[MockJWTAudienceMapperMockRecorder](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#MockJWTAudienceMapperMockRecorder)

EXPECT returns an object that allows the caller to indicate expected use.

#### type [MockJWTAudienceMapperMockRecorder](https://github.com/temporalio/temporal/blob/v1.30.0/common/authorization/audience_mapper_mock.go#L28)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#MockJWTAudienceMapperMockRecorder "Go to MockJWTAudienceMapperMockRecorder")added in v1.29.0

type MockJWTAudienceMapperMockRecorder struct {
	// contains filtered or unexported fields
}

MockJWTAudienceMapperMockRecorder is the mock recorder for MockJWTAudienceMapper.

#### func (*MockJWTAudienceMapperMockRecorder) [Audience](https://github.com/temporalio/temporal/blob/v1.30.0/common/authorization/audience_mapper_mock.go#L53)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#MockJWTAudienceMapperMockRecorder.Audience "Go to MockJWTAudienceMapperMockRecorder.Audience")added in v1.29.0

func (mr *[MockJWTAudienceMapperMockRecorder](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#MockJWTAudienceMapperMockRecorder)) Audience(ctx, req, info interface{}) *[gomock](https://pkg.go.dev/go.uber.org/mock/gomock).[Call](https://pkg.go.dev/go.uber.org/mock/gomock#Call)

Audience indicates an expected call of Audience.

#### type [MockhasNamespace](https://github.com/temporalio/temporal/blob/v1.30.0/common/authorization/authorizer_mock.go#L59)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#MockhasNamespace "Go to MockhasNamespace")added in v1.8.2

type MockhasNamespace struct {
	// contains filtered or unexported fields
}

MockhasNamespace is a mock of hasNamespace interface.

#### func [NewMockhasNamespace](https://github.com/temporalio/temporal/blob/v1.30.0/common/authorization/authorizer_mock.go#L71)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#NewMockhasNamespace "Go to NewMockhasNamespace")added in v1.8.2

func NewMockhasNamespace(ctrl *[gomock](https://pkg.go.dev/go.uber.org/mock/gomock).[Controller](https://pkg.go.dev/go.uber.org/mock/gomock#Controller)) *[MockhasNamespace](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#MockhasNamespace)

NewMockhasNamespace creates a new mock instance.

#### func (*MockhasNamespace) [EXPECT](https://github.com/temporalio/temporal/blob/v1.30.0/common/authorization/authorizer_mock.go#L78)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#MockhasNamespace.EXPECT "Go to MockhasNamespace.EXPECT")added in v1.8.2

func (m *[MockhasNamespace](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#MockhasNamespace)) EXPECT() *[MockhasNamespaceMockRecorder](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#MockhasNamespaceMockRecorder)

EXPECT returns an object that allows the caller to indicate expected use.

#### func (*MockhasNamespace) [GetNamespace](https://github.com/temporalio/temporal/blob/v1.30.0/common/authorization/authorizer_mock.go#L83)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#MockhasNamespace.GetNamespace "Go to MockhasNamespace.GetNamespace")added in v1.8.2

func (m *[MockhasNamespace](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#MockhasNamespace)) GetNamespace() [string](https://pkg.go.dev/builtin#string)

GetNamespace mocks base method.

#### type [MockhasNamespaceMockRecorder](https://github.com/temporalio/temporal/blob/v1.30.0/common/authorization/authorizer_mock.go#L66)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#MockhasNamespaceMockRecorder "Go to MockhasNamespaceMockRecorder")added in v1.8.2

type MockhasNamespaceMockRecorder struct {
	// contains filtered or unexported fields
}

MockhasNamespaceMockRecorder is the mock recorder for MockhasNamespace.

#### func (*MockhasNamespaceMockRecorder) [GetNamespace](https://github.com/temporalio/temporal/blob/v1.30.0/common/authorization/authorizer_mock.go#L91)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#MockhasNamespaceMockRecorder.GetNamespace "Go to MockhasNamespaceMockRecorder.GetNamespace")added in v1.8.2

func (mr *[MockhasNamespaceMockRecorder](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#MockhasNamespaceMockRecorder)) GetNamespace() *[gomock](https://pkg.go.dev/go.uber.org/mock/gomock).[Call](https://pkg.go.dev/go.uber.org/mock/gomock#Call)

GetNamespace indicates an expected call of GetNamespace.

#### type [NamespaceChecker](https://github.com/temporalio/temporal/blob/v1.30.0/common/authorization/interceptor.go#L36)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#NamespaceChecker "Go to NamespaceChecker")added in v1.24.0

type NamespaceChecker interface {
// Exists returns nil if the namespace exists, otherwise an error.	Exists(name [namespace](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/namespace).[Name](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/namespace#Name)) [error](https://pkg.go.dev/builtin#error)
}

#### type [RawTokenKeyProvider](https://github.com/temporalio/temporal/blob/v1.30.0/common/authorization/token_key_provider.go#L22)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#RawTokenKeyProvider "Go to RawTokenKeyProvider")added in v1.15.0

type RawTokenKeyProvider interface {
 GetKey(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), token *[jwt](https://pkg.go.dev/github.com/golang-jwt/jwt/v4).[Token](https://pkg.go.dev/github.com/golang-jwt/jwt/v4#Token)) (interface{}, [error](https://pkg.go.dev/builtin#error))  SupportedMethods() [][string](https://pkg.go.dev/builtin#string) Close() }

RawTokenKeyProvider is a TokenKeyProvider that provides keys for validating JWT tokens

#### type [Result](https://github.com/temporalio/temporal/blob/v1.30.0/common/authorization/authorizer.go#L39)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#Result "Go to Result")

type Result struct {
 Decision [Decision](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#Decision)// Reason may contain a message explaining the value of the Decision field.	Reason [string](https://pkg.go.dev/builtin#string)
}

Result is result from authority.

#### type [Role](https://github.com/temporalio/temporal/blob/v1.30.0/common/authorization/roles.go#L3)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#Role "Go to Role")added in v1.4.0

type Role [int16](https://pkg.go.dev/builtin#int16)

#### func (Role) [IsValid](https://github.com/temporalio/temporal/blob/v1.30.0/common/authorization/roles.go#L19)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#Role.IsValid "Go to Role.IsValid")added in v1.4.0

func (b [Role](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#Role)) IsValid() [bool](https://pkg.go.dev/builtin#bool)

Checks if the provided role bitmask represents a valid combination of authz

#### type [TokenKeyProvider](https://github.com/temporalio/temporal/blob/v1.30.0/common/authorization/token_key_provider.go#L13)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#TokenKeyProvider "Go to TokenKeyProvider")added in v1.4.0

type TokenKeyProvider interface {
 EcdsaKey(alg [string](https://pkg.go.dev/builtin#string), kid [string](https://pkg.go.dev/builtin#string)) (*[ecdsa](https://pkg.go.dev/crypto/ecdsa).[PublicKey](https://pkg.go.dev/crypto/ecdsa#PublicKey), [error](https://pkg.go.dev/builtin#error))  HmacKey(alg [string](https://pkg.go.dev/builtin#string), kid [string](https://pkg.go.dev/builtin#string)) ([][byte](https://pkg.go.dev/builtin#byte), [error](https://pkg.go.dev/builtin#error))  RsaKey(alg [string](https://pkg.go.dev/builtin#string), kid [string](https://pkg.go.dev/builtin#string)) (*[rsa](https://pkg.go.dev/crypto/rsa).[PublicKey](https://pkg.go.dev/crypto/rsa#PublicKey), [error](https://pkg.go.dev/builtin#error))  SupportedMethods() [][string](https://pkg.go.dev/builtin#string) Close() }

@@@SNIPSTART temporal-common-authorization-tokenkeyprovider-interface Provides keys for validating JWT tokens

![Image 44](https://pkg.go.dev/static/shared/icon/insert_drive_file_gm_grey_24dp.svg) Source Files [¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/authorization#section-sourcefiles "Go to Source Files")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[View all Source files](https://github.com/temporalio/temporal/tree/v1.30.0/common/authorization)

*   [audience_mapper.go](https://github.com/temporalio/temporal/blob/v1.30.0/common/authorization/audience_mapper.go "audience_mapper.go")
*   [audience_mapper_mock.go](https://github.com/temporalio/temporal/blob/v1.30.0/common/authorization/audience_mapper_mock.go "audience_mapper_mock.go")
*   [authorizer.go](https://github.com/temporalio/temporal/blob/v1.30.0/common/authorization/authorizer.go "authorizer.go")
*   [authorizer_mock.go](https://github.com/temporalio/temporal/blob/v1.30.0/common/authorization/authorizer_mock.go "authorizer_mock.go")
*   [claim_mapper.go](https://github.com/temporalio/temporal/blob/v1.30.0/common/authorization/claim_mapper.go "claim_mapper.go")
*   [claim_mapper_mock.go](https://github.com/temporalio/temporal/blob/v1.30.0/common/authorization/claim_mapper_mock.go "claim_mapper_mock.go")
*   [default_authorizer.go](https://github.com/temporalio/temporal/blob/v1.30.0/common/authorization/default_authorizer.go "default_authorizer.go")
*   [default_jwt_claim_mapper.go](https://github.com/temporalio/temporal/blob/v1.30.0/common/authorization/default_jwt_claim_mapper.go "default_jwt_claim_mapper.go")
*   [default_token_key_provider.go](https://github.com/temporalio/temporal/blob/v1.30.0/common/authorization/default_token_key_provider.go "default_token_key_provider.go")
*   [frontend_api.go](https://github.com/temporalio/temporal/blob/v1.30.0/common/authorization/frontend_api.go "frontend_api.go")
*   [interceptor.go](https://github.com/temporalio/temporal/blob/v1.30.0/common/authorization/interceptor.go "interceptor.go")
*   [noop_authorizer.go](https://github.com/temporalio/temporal/blob/v1.30.0/common/authorization/noop_authorizer.go "noop_authorizer.go")
*   [roles.go](https://github.com/temporalio/temporal/blob/v1.30.0/common/authorization/roles.go "roles.go")
*   [token_key_provider.go](https://github.com/temporalio/temporal/blob/v1.30.0/common/authorization/token_key_provider.go "token_key_provider.go")

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
