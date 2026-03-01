# Source: https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider

Title: certprovider package - google.golang.org/grpc/credentials/tls/certprovider - Go Packages

URL Source: https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider

Markdown Content:
certprovider package - google.golang.org/grpc/credentials/tls/certprovider - Go Packages
===============

[![Image 1: Go](https://pkg.go.dev/static/shared/logo/go-white.svg)](https://go.dev/)

[Skip to Main Content](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider#main-content)

![Image 2](https://pkg.go.dev/static/shared/icon/search_gm_grey_24dp.svg)![Image 3](https://pkg.go.dev/static/shared/icon/search_gm_grey_24dp.svg)

*   [Why Go ![Image 4: submenu dropdown icon](https://pkg.go.dev/static/shared/icon/arrow_drop_down_gm_grey_24dp.svg)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider#)
    *   [Case Studies](https://go.dev/solutions#case-studies) 
Common problems companies solve with Go

    *   [Use Cases](https://go.dev/solutions#use-cases) 
Stories about how and why companies use Go

    *   [Security](https://go.dev/security/) 
How Go can help keep you secure by default

*   [Learn](https://go.dev/learn/)
*   [Docs ![Image 5: submenu dropdown icon](https://pkg.go.dev/static/shared/icon/arrow_drop_down_gm_grey_24dp.svg)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider#)
    *   [Effective Go](https://go.dev/doc/effective_go) 
Tips for writing clear, performant, and idiomatic Go code

    *   [Go User Manual](https://go.dev/doc/) 
A complete introduction to building software with Go

    *   [Standard library](https://pkg.go.dev/std) 
Reference documentation for Go's standard library

    *   [Release Notes](https://go.dev/doc/devel/release) 
Learn what's new in each Go release

*   [Packages](https://pkg.go.dev/)
*   [Community ![Image 6: submenu dropdown icon](https://pkg.go.dev/static/shared/icon/arrow_drop_down_gm_grey_24dp.svg)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider#)
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

*   [Why Go _![Image 16](https://pkg.go.dev/static/shared/icon/navigate\_next\_gm\_grey\_24dp.svg)_](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider#)

[_![Image 17](https://pkg.go.dev/static/shared/icon/navigate\_before\_gm\_grey\_24dp.svg)_ Why Go](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider#) 
    *   [Case Studies](https://go.dev/solutions#case-studies)
    *   [Use Cases](https://go.dev/solutions#use-cases)
    *   [Security](https://go.dev/security/)

*   [Learn](https://go.dev/learn/)
*   [Docs _![Image 18](https://pkg.go.dev/static/shared/icon/navigate\_next\_gm\_grey\_24dp.svg)_](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider#)

[_![Image 19](https://pkg.go.dev/static/shared/icon/navigate\_before\_gm\_grey\_24dp.svg)_ Docs](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider#) 
    *   [Effective Go](https://go.dev/doc/effective_go)
    *   [Go User Manual](https://go.dev/doc/)
    *   [Standard library](https://pkg.go.dev/std)
    *   [Release Notes](https://go.dev/doc/devel/release)

*   [Packages](https://pkg.go.dev/)
*   [Community _![Image 20](https://pkg.go.dev/static/shared/icon/navigate\_next\_gm\_grey\_24dp.svg)_](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider#)

[_![Image 21](https://pkg.go.dev/static/shared/icon/navigate\_before\_gm\_grey\_24dp.svg)_ Community](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider#) 
    *   [Recorded Talks](https://go.dev/talks/)
    *   [Meetups _![Image 22](https://pkg.go.dev/static/shared/icon/launch\_gm\_grey\_24dp.svg)_](https://www.meetup.com/pro/go)
    *   [Conferences _![Image 23](https://pkg.go.dev/static/shared/icon/launch\_gm\_grey\_24dp.svg)_](https://github.com/golang/go/wiki/Conferences)
    *   [Go blog](https://go.dev/blog)
    *   [Go project](https://go.dev/help)
    *   Get connected [![Image 24](https://pkg.go.dev/static/shared/logo/social/google-groups.svg)](https://groups.google.com/g/golang-nuts)[![Image 25](https://pkg.go.dev/static/shared/logo/social/github.svg)](https://github.com/golang)[![Image 26](https://pkg.go.dev/static/shared/logo/social/twitter.svg)](https://twitter.com/golang)[![Image 27](https://pkg.go.dev/static/shared/logo/social/reddit.svg)](https://www.reddit.com/r/golang/)[![Image 28](https://pkg.go.dev/static/shared/logo/social/slack.svg)](https://invite.slack.golangbridge.org/)[![Image 29](https://pkg.go.dev/static/shared/logo/social/stack-overflow.svg)](https://stackoverflow.com/collectives/go) 

1.   [Discover Packages](https://pkg.go.dev/)
2.   [google.golang.org/grpc](https://pkg.go.dev/google.golang.org/grpc@v1.79.1)
3.   [credentials](https://pkg.go.dev/google.golang.org/grpc/credentials@v1.79.1)
4.   [tls](https://pkg.go.dev/google.golang.org/grpc/credentials/tls@v1.79.1)
5.   [certprovider](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider)![Image 30](https://pkg.go.dev/static/shared/icon/content_copy_gm_grey_24dp.svg)

[![Image 31: Go](https://pkg.go.dev/static/shared/logo/go-blue.svg)](https://go.dev/)
certprovider
============

package![Image 32](https://pkg.go.dev/static/shared/icon/content_copy_gm_grey_24dp.svg)

[Version: v1.79.1](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider?tab=versions)

 Opens a new window with list of versions in this module. 

Latest Latest 

![Image 33: Warning](https://pkg.go.dev/static/shared/icon/alert_gm_grey_24dp.svg)
This package is not in the latest version of its module.

[Go to latest](https://pkg.go.dev/google.golang.org/grpc/credentials/tls/certprovider) Published: Feb 13, 2026  License: [Apache-2.0](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider?tab=licenses)

 Opens a new window with license information. 

[Imports: 10](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider?tab=imports)

 Opens a new window with list of imports. 

[Imported by: 35](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider?tab=importedby)

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

*   [Documentation](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider#section-documentation)
    *   [Overview](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider#pkg-overview)
    *   [Index](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider#pkg-index)
    *   [Constants](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider#pkg-constants)
    *   [Variables](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider#pkg-variables)
    *   [Functions](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider#pkg-functions)
        *   [Register(b)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider#Register "Register(b)")

    *   [Types](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider#pkg-types)
        *   [type BuildOptions](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider#BuildOptions "type BuildOptions")
        *   [type BuildableConfig](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider#BuildableConfig "type BuildableConfig")
            *   [NewBuildableConfig(name, config, starter)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider#NewBuildableConfig "NewBuildableConfig(name, config, starter)")
            *   [ParseConfig(name, config)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider#ParseConfig "ParseConfig(name, config)")
            *   [(bc) Build(opts)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider#BuildableConfig.Build "(bc) Build(opts)")
            *   [(bc) String()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider#BuildableConfig.String "(bc) String()")

        *   [type Builder](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider#Builder "type Builder")
        *   [type Distributor](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider#Distributor "type Distributor")
            *   [NewDistributor()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider#NewDistributor "NewDistributor()")
            *   [(d) KeyMaterial(ctx)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider#Distributor.KeyMaterial "(d) KeyMaterial(ctx)")
            *   [(d) Set(km, err)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider#Distributor.Set "(d) Set(km, err)")
            *   [(d) Stop()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider#Distributor.Stop "(d) Stop()")

        *   [type KeyMaterial](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider#KeyMaterial "type KeyMaterial")
        *   [type Provider](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider#Provider "type Provider")
            *   [GetProvider(name, config, opts)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider#GetProvider "GetProvider(name, config, opts)")

*   [Source Files](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider#section-sourcefiles)
*   [Directories](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider#section-directories)

![Image 43](https://pkg.go.dev/static/shared/icon/code_gm_grey_24dp.svg) Documentation [¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider#section-documentation "Go to Documentation")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Overview [¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider#pkg-overview "Go to Overview")

*   [Experimental](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider#hdr-Experimental)

Package certprovider defines APIs for Certificate Providers in gRPC.

#### Experimental [¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider#hdr-Experimental "Go to Experimental")

Notice: All APIs in this package are experimental and may be removed in a later release.

### Index [¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider#pkg-index "Go to Index")

*   [func Register(b Builder)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider#Register)
*   [type BuildOptions](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider#BuildOptions)
*   [type BuildableConfig](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider#BuildableConfig)
*       *   [func NewBuildableConfig(name string, config []byte, starter func(BuildOptions) Provider) *BuildableConfig](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider#NewBuildableConfig)
    *   [func ParseConfig(name string, config any) (*BuildableConfig, error)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider#ParseConfig)

*       *   [func (bc *BuildableConfig) Build(opts BuildOptions) (Provider, error)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider#BuildableConfig.Build)
    *   [func (bc *BuildableConfig) String() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider#BuildableConfig.String)

*   [type Builder](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider#Builder)
*   [type Distributor](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider#Distributor)
*       *   [func NewDistributor() *Distributor](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider#NewDistributor)

*       *   [func (d *Distributor) KeyMaterial(ctx context.Context) (*KeyMaterial, error)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider#Distributor.KeyMaterial)
    *   [func (d *Distributor) Set(km *KeyMaterial, err error)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider#Distributor.Set)
    *   [func (d *Distributor) Stop()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider#Distributor.Stop)

*   [type KeyMaterial](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider#KeyMaterial)
*   [type Provider](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider#Provider)
*       *   [func GetProvider(name string, config any, opts BuildOptions) (Provider, error)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider#GetProvider)

### Constants [¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider#pkg-constants "Go to Constants")

This section is empty.

### Variables [¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider#pkg-variables "Go to Variables")

This section is empty.

### Functions [¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider#pkg-functions "Go to Functions")

#### func [Register](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/tls/certprovider/provider.go#L53)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider#Register "Go to Register")

func Register(b [Builder](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider#Builder))

Register registers the Provider builder, whose name as returned by its Name() method will be used as the name registered with this builder. Registered Builders are used by the Store to create Providers.

### Types [¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider#pkg-types "Go to Types")

#### type [BuildOptions](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/tls/certprovider/provider.go#L106)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider#BuildOptions "Go to BuildOptions")added in v1.34.0

type BuildOptions struct {
// CertName holds the certificate name, whose key material is of interest to	// the caller.
	CertName [string](https://pkg.go.dev/builtin#string)
// WantRoot indicates if the caller is interested in the root certificate.	WantRoot [bool](https://pkg.go.dev/builtin#bool)
// WantIdentity indicates if the caller is interested in the identity	// certificate.
	WantIdentity [bool](https://pkg.go.dev/builtin#bool)
}

BuildOptions contains parameters passed to a Provider at build time.

#### type [BuildableConfig](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/tls/certprovider/store.go#L120)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider#BuildableConfig "Go to BuildableConfig")added in v1.34.0

type BuildableConfig struct {
	// contains filtered or unexported fields
}

BuildableConfig wraps parsed provider configuration and functionality to instantiate provider instances.

#### func [NewBuildableConfig](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/tls/certprovider/store.go#L132)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider#NewBuildableConfig "Go to NewBuildableConfig")added in v1.34.0

func NewBuildableConfig(name [string](https://pkg.go.dev/builtin#string), config [][byte](https://pkg.go.dev/builtin#byte), starter func([BuildOptions](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider#BuildOptions)) [Provider](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider#Provider)) *[BuildableConfig](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider#BuildableConfig)

NewBuildableConfig creates a new BuildableConfig with the given arguments. Provider implementations are expected to invoke this function after parsing the given configuration as part of their ParseConfig() method. Equivalent configurations are expected to invoke this function with the same config argument.

#### func [ParseConfig](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/tls/certprovider/store.go#L180)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider#ParseConfig "Go to ParseConfig")added in v1.34.0

func ParseConfig(name [string](https://pkg.go.dev/builtin#string), config [any](https://pkg.go.dev/builtin#any)) (*[BuildableConfig](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider#BuildableConfig), [error](https://pkg.go.dev/builtin#error))

ParseConfig is a convenience function to create a BuildableConfig given a provider name and configuration. Returns an error if there is no registered builder for the given name or if the config parsing fails.

#### func (*BuildableConfig) [Build](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/tls/certprovider/store.go#L144)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider#BuildableConfig.Build "Go to BuildableConfig.Build")added in v1.34.0

func (bc *[BuildableConfig](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider#BuildableConfig)) Build(opts [BuildOptions](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider#BuildOptions)) ([Provider](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider#Provider), [error](https://pkg.go.dev/builtin#error))

Build kicks off a provider instance with the wrapped configuration. Multiple invocations of this method with the same opts will result in provider instances being reused.

#### func (*BuildableConfig) [String](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/tls/certprovider/store.go#L173)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider#BuildableConfig.String "Go to BuildableConfig.String")added in v1.34.0

func (bc *[BuildableConfig](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider#BuildableConfig)) String() [string](https://pkg.go.dev/builtin#string)

String returns the provider name and config as a colon separated string.

#### type [Builder](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/tls/certprovider/provider.go#L67)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider#Builder "Go to Builder")

type Builder interface {
// ParseConfig parses the given config, which is in a format specific to individual	// implementations, and returns a BuildableConfig on success.
	ParseConfig([any](https://pkg.go.dev/builtin#any)) (*[BuildableConfig](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider#BuildableConfig), [error](https://pkg.go.dev/builtin#error))

// Name returns the name of providers built by this builder.	Name() [string](https://pkg.go.dev/builtin#string)
}

Builder creates a Provider.

#### type [Distributor](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/tls/certprovider/distributor.go#L39)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider#Distributor "Go to Distributor")

type Distributor struct {
	// contains filtered or unexported fields
}

Distributor makes it easy for provider implementations to furnish new key materials by handling synchronization between the producer and consumers of the key material.

Provider implementations which choose to use a Distributor should do the following:

*   create a new Distributor using the NewDistributor() function.
*   invoke the Set() method whenever they have new key material or errors to report.
*   delegate to the distributor when handing calls to KeyMaterial().
*   invoke the Stop() method when they are done using the distributor.

#### func [NewDistributor](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/tls/certprovider/distributor.go#L54)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider#NewDistributor "Go to NewDistributor")

func NewDistributor() *[Distributor](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider#Distributor)

NewDistributor returns a new Distributor.

#### func (*Distributor) [KeyMaterial](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/tls/certprovider/distributor.go#L85)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider#Distributor.KeyMaterial "Go to Distributor.KeyMaterial")

func (d *[Distributor](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider#Distributor)) KeyMaterial(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context)) (*[KeyMaterial](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider#KeyMaterial), [error](https://pkg.go.dev/builtin#error))

KeyMaterial returns the most recent key material provided to the Distributor. If no key material was provided at the time of this call, it will block until the deadline on the context expires or fresh key material arrives.

#### func (*Distributor) [Set](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/tls/certprovider/distributor.go#L70)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider#Distributor.Set "Go to Distributor.Set")

func (d *[Distributor](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider#Distributor)) Set(km *[KeyMaterial](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider#KeyMaterial), err [error](https://pkg.go.dev/builtin#error))

Set updates the key material in the distributor with km.

Provider implementations which use the distributor must not modify the contents of the KeyMaterial struct pointed to by km.

A non-nil err value indicates the error that the provider implementation ran into when trying to fetch key material, and makes it possible to surface the error to the user. A non-nil error value passed here causes distributor's KeyMaterial() method to return nil key material.

#### func (*Distributor) [Stop](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/tls/certprovider/distributor.go#L112)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider#Distributor.Stop "Go to Distributor.Stop")

func (d *[Distributor](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider#Distributor)) Stop()

Stop turns down the distributor, releases allocated resources and fails any active KeyMaterial() call waiting for new key material.

#### type [KeyMaterial](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/tls/certprovider/provider.go#L93)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider#KeyMaterial "Go to KeyMaterial")

type KeyMaterial struct {
// Certs contains a slice of cert/key pairs used to prove local identity.	Certs [][tls](https://pkg.go.dev/crypto/tls).[Certificate](https://pkg.go.dev/crypto/tls#Certificate)
// Roots contains the set of trusted roots to validate the peer's identity.	// This field will only be used if the `SPIFFEBundleMap` field is unset.
	Roots *[x509](https://pkg.go.dev/crypto/x509).[CertPool](https://pkg.go.dev/crypto/x509#CertPool)
// SPIFFEBundleMap is an in-memory representation of a spiffe trust bundle	// map. If this value exists, it will be used to find the roots for a given
	// trust domain rather than the Roots in this struct.
	SPIFFEBundleMap map[[string](https://pkg.go.dev/builtin#string)]*[spiffebundle](https://pkg.go.dev/github.com/spiffe/go-spiffe/v2/bundle/spiffebundle).[Bundle](https://pkg.go.dev/github.com/spiffe/go-spiffe/v2/bundle/spiffebundle#Bundle)
}

KeyMaterial wraps the certificates and keys returned by a Provider instance.

#### type [Provider](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/tls/certprovider/provider.go#L83)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider#Provider "Go to Provider")

type Provider interface {
// KeyMaterial returns the key material sourced by the Provider.	// Callers are expected to use the returned value as read-only.
	KeyMaterial(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context)) (*[KeyMaterial](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider#KeyMaterial), [error](https://pkg.go.dev/builtin#error))

// Close cleans up resources allocated by the Provider.	Close()
}

Provider makes it possible to keep channel credential implementations up to date with secrets that they rely on to secure communications on the underlying channel.

Provider implementations are free to rely on local or remote sources to fetch the latest secrets, and free to share any state between different instantiations as they deem fit.

#### func [GetProvider](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/tls/certprovider/store.go#L190)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider#GetProvider "Go to GetProvider")

func GetProvider(name [string](https://pkg.go.dev/builtin#string), config [any](https://pkg.go.dev/builtin#any), opts [BuildOptions](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider#BuildOptions)) ([Provider](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider#Provider), [error](https://pkg.go.dev/builtin#error))

GetProvider is a convenience function to create a provider given the name, config and build options.

![Image 44](https://pkg.go.dev/static/shared/icon/insert_drive_file_gm_grey_24dp.svg) Source Files [¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider#section-sourcefiles "Go to Source Files")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[View all Source files](https://github.com/grpc/grpc-go/tree/v1.79.1/credentials/tls/certprovider)

*   [distributor.go](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/tls/certprovider/distributor.go "distributor.go")
*   [provider.go](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/tls/certprovider/provider.go "provider.go")
*   [store.go](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/tls/certprovider/store.go "store.go")

![Image 45](https://pkg.go.dev/static/shared/icon/folder_gm_grey_24dp.svg) Directories [¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider#section-directories "Go to Directories")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

 Show internal Collapse all

| Path | Synopsis |
| --- | --- |
| [pemfile](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/tls/certprovider/pemfile) Package pemfile provides a file watching certificate provider plugin implementation which works for files with PEM contents. | Package pemfile provides a file watching certificate provider plugin implementation which works for files with PEM contents. |

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
