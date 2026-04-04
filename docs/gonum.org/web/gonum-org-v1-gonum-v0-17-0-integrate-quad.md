# Source: https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/integrate/quad

Title: quad package - gonum.org/v1/gonum/integrate/quad - Go Packages

URL Source: https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/integrate/quad

Markdown Content:
quad package - gonum.org/v1/gonum/integrate/quad - Go Packages
===============

[![Image 1: Go](https://pkg.go.dev/static/shared/logo/go-white.svg)](https://go.dev/)

[Skip to Main Content](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/integrate/quad#main-content)

![Image 2](https://pkg.go.dev/static/shared/icon/search_gm_grey_24dp.svg)![Image 3](https://pkg.go.dev/static/shared/icon/search_gm_grey_24dp.svg)

*   [Why Go ![Image 4: submenu dropdown icon](https://pkg.go.dev/static/shared/icon/arrow_drop_down_gm_grey_24dp.svg)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/integrate/quad#)
    *   [Case Studies](https://go.dev/solutions#case-studies) 
Common problems companies solve with Go

    *   [Use Cases](https://go.dev/solutions#use-cases) 
Stories about how and why companies use Go

    *   [Security](https://go.dev/security/) 
How Go can help keep you secure by default

*   [Learn](https://go.dev/learn/)
*   [Docs ![Image 5: submenu dropdown icon](https://pkg.go.dev/static/shared/icon/arrow_drop_down_gm_grey_24dp.svg)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/integrate/quad#)
    *   [Effective Go](https://go.dev/doc/effective_go) 
Tips for writing clear, performant, and idiomatic Go code

    *   [Go User Manual](https://go.dev/doc/) 
A complete introduction to building software with Go

    *   [Standard library](https://pkg.go.dev/std) 
Reference documentation for Go's standard library

    *   [Release Notes](https://go.dev/doc/devel/release) 
Learn what's new in each Go release

*   [Packages](https://pkg.go.dev/)
*   [Community ![Image 6: submenu dropdown icon](https://pkg.go.dev/static/shared/icon/arrow_drop_down_gm_grey_24dp.svg)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/integrate/quad#)
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

*   [Why Go _![Image 16](https://pkg.go.dev/static/shared/icon/navigate\_next\_gm\_grey\_24dp.svg)_](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/integrate/quad#)

[_![Image 17](https://pkg.go.dev/static/shared/icon/navigate\_before\_gm\_grey\_24dp.svg)_ Why Go](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/integrate/quad#) 
    *   [Case Studies](https://go.dev/solutions#case-studies)
    *   [Use Cases](https://go.dev/solutions#use-cases)
    *   [Security](https://go.dev/security/)

*   [Learn](https://go.dev/learn/)
*   [Docs _![Image 18](https://pkg.go.dev/static/shared/icon/navigate\_next\_gm\_grey\_24dp.svg)_](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/integrate/quad#)

[_![Image 19](https://pkg.go.dev/static/shared/icon/navigate\_before\_gm\_grey\_24dp.svg)_ Docs](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/integrate/quad#) 
    *   [Effective Go](https://go.dev/doc/effective_go)
    *   [Go User Manual](https://go.dev/doc/)
    *   [Standard library](https://pkg.go.dev/std)
    *   [Release Notes](https://go.dev/doc/devel/release)

*   [Packages](https://pkg.go.dev/)
*   [Community _![Image 20](https://pkg.go.dev/static/shared/icon/navigate\_next\_gm\_grey\_24dp.svg)_](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/integrate/quad#)

[_![Image 21](https://pkg.go.dev/static/shared/icon/navigate\_before\_gm\_grey\_24dp.svg)_ Community](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/integrate/quad#) 
    *   [Recorded Talks](https://go.dev/talks/)
    *   [Meetups _![Image 22](https://pkg.go.dev/static/shared/icon/launch\_gm\_grey\_24dp.svg)_](https://www.meetup.com/pro/go)
    *   [Conferences _![Image 23](https://pkg.go.dev/static/shared/icon/launch\_gm\_grey\_24dp.svg)_](https://github.com/golang/go/wiki/Conferences)
    *   [Go blog](https://go.dev/blog)
    *   [Go project](https://go.dev/help)
    *   Get connected [![Image 24](https://pkg.go.dev/static/shared/logo/social/google-groups.svg)](https://groups.google.com/g/golang-nuts)[![Image 25](https://pkg.go.dev/static/shared/logo/social/github.svg)](https://github.com/golang)[![Image 26](https://pkg.go.dev/static/shared/logo/social/twitter.svg)](https://twitter.com/golang)[![Image 27](https://pkg.go.dev/static/shared/logo/social/reddit.svg)](https://www.reddit.com/r/golang/)[![Image 28](https://pkg.go.dev/static/shared/logo/social/slack.svg)](https://invite.slack.golangbridge.org/)[![Image 29](https://pkg.go.dev/static/shared/logo/social/stack-overflow.svg)](https://stackoverflow.com/collectives/go) 

1.   [Discover Packages](https://pkg.go.dev/)
2.   [gonum.org/v1/gonum](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0)
3.   [integrate](https://pkg.go.dev/gonum.org/v1/gonum/integrate@v0.17.0)
4.   [quad](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/integrate/quad)![Image 30](https://pkg.go.dev/static/shared/icon/content_copy_gm_grey_24dp.svg)

[![Image 31: Go](https://pkg.go.dev/static/shared/logo/go-blue.svg)](https://go.dev/)
quad
====

package![Image 32](https://pkg.go.dev/static/shared/icon/content_copy_gm_grey_24dp.svg)

[Version: v0.17.0](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/integrate/quad?tab=versions)

 Opens a new window with list of versions in this module. 

Latest Latest 

![Image 33: Warning](https://pkg.go.dev/static/shared/icon/alert_gm_grey_24dp.svg)
This package is not in the latest version of its module.

[Go to latest](https://pkg.go.dev/gonum.org/v1/gonum/integrate/quad) Published: Dec 29, 2025  License: [BSD-3-Clause](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/integrate/quad?tab=licenses)

 Opens a new window with license information. 

[Imports: 4](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/integrate/quad?tab=imports)

 Opens a new window with list of imports. 

[Imported by: 15](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/integrate/quad?tab=importedby)

 Opens a new window with list of known importers. 

Details
-------

*   ![Image 34: checked](https://pkg.go.dev/static/shared/icon/check_circle_gm_grey_24dp.svg) Valid [go.mod](https://github.com/gonum/gonum/tree/v0.17.0/go.mod) file ![Image 35](https://pkg.go.dev/static/shared/icon/help_gm_grey_24dp.svg)
The Go module system was introduced in Go 1.11 and is the official dependency management solution for Go. 
*   ![Image 36: checked](https://pkg.go.dev/static/shared/icon/check_circle_gm_grey_24dp.svg) Redistributable license ![Image 37](https://pkg.go.dev/static/shared/icon/help_gm_grey_24dp.svg)
Redistributable licenses place minimal restrictions on how software can be used, modified, and redistributed. 
*   ![Image 38: checked](https://pkg.go.dev/static/shared/icon/check_circle_gm_grey_24dp.svg) Tagged version ![Image 39](https://pkg.go.dev/static/shared/icon/help_gm_grey_24dp.svg)
Modules with tagged versions give importers more predictable builds. 
*   ![Image 40: unchecked](https://pkg.go.dev/static/shared/icon/cancel_gm_grey_24dp.svg) Stable version ![Image 41](https://pkg.go.dev/static/shared/icon/help_gm_grey_24dp.svg)
When a project reaches major version v1 it is considered stable. 
*   [Learn more about best practices](https://pkg.go.dev/about#best-practices)

Repository
----------

[github.com/gonum/gonum](https://github.com/gonum/gonum "https://github.com/gonum/gonum")

Links
-----

*   [![Image 42: Open Source Insights Logo](https://pkg.go.dev/static/shared/icon/depsdev-logo.svg) Open Source Insights](https://deps.dev/go/gonum.org%2Fv1%2Fgonum/v0.17.0 "View this module on Open Source Insights")

 Jump to ... 

*   [Documentation](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/integrate/quad#section-documentation)
    *   [Overview](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/integrate/quad#pkg-overview)
    *   [Index](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/integrate/quad#pkg-index)
    *   [Examples](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/integrate/quad#pkg-examples)
        *   [Package](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/integrate/quad#example-package "Package")

    *   [Constants](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/integrate/quad#pkg-constants)
    *   [Variables](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/integrate/quad#pkg-variables)
    *   [Functions](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/integrate/quad#pkg-functions)
        *   [Fixed(f, min, max, n, rule, concurrent)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/integrate/quad#Fixed "Fixed(f, min, max, n, rule, concurrent)")

    *   [Types](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/integrate/quad#pkg-types)
        *   [type FixedLocationSingler](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/integrate/quad#FixedLocationSingler "type FixedLocationSingler")
        *   [type FixedLocationer](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/integrate/quad#FixedLocationer "type FixedLocationer")
        *   [type Hermite](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/integrate/quad#Hermite "type Hermite")
            *   [(h) FixedLocations(x, weight, min, max)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/integrate/quad#Hermite.FixedLocations "(h) FixedLocations(x, weight, min, max)")

        *   [type Legendre](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/integrate/quad#Legendre "type Legendre")
            *   [(l) FixedLocationSingle(n, k, min, max)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/integrate/quad#Legendre.FixedLocationSingle "(l) FixedLocationSingle(n, k, min, max)")
            *   [(l) FixedLocations(x, weight, min, max)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/integrate/quad#Legendre.FixedLocations "(l) FixedLocations(x, weight, min, max)")

*   [Source Files](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/integrate/quad#section-sourcefiles)

![Image 43](https://pkg.go.dev/static/shared/icon/code_gm_grey_24dp.svg) Documentation [¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/integrate/quad#section-documentation "Go to Documentation")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Overview [¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/integrate/quad#pkg-overview "Go to Overview")

Package quad provides numerical evaluation of definite integrals of single-variable functions.

Example [¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/integrate/quad#example-package "Go to Example")

package main

import (
	"fmt"
	"math"
	"runtime"

	"gonum.org/v1/gonum/integrate/quad"
	"gonum.org/v1/gonum/stat/distuv"
)

func main() {
	fmt.Println("Evaluate the expected value of x^2 + 3 under a Weibull distribution")
	f := func(x float64) float64 {
		d := distuv.Weibull{Lambda: 1, K: 1.5}
		return (x*x + 3) * d.Prob(x)
	}
	ev := quad.Fixed(f, 0, math.Inf(1), 10, nil, 0)
	fmt.Printf("EV with 10 points = %0.6v\n", ev)

	ev = quad.Fixed(f, 0, math.Inf(1), 30, nil, 0)
	fmt.Printf("EV with 30 points = %0.6v\n", ev)

	ev = quad.Fixed(f, 0, math.Inf(1), 100, nil, 0)
	fmt.Printf("EV with 100 points = %0.6v\n", ev)

	ev = quad.Fixed(f, 0, math.Inf(1), 10000, nil, 0)
	fmt.Printf("EV with 10000 points = %0.6v\n\n", ev)

	fmt.Println("Estimate using parallel evaluations of f.")
	concurrent := runtime.GOMAXPROCS(0)
	ev = quad.Fixed(f, 0, math.Inf(1), 100, nil, concurrent)
	fmt.Printf("EV = %0.6v\n", ev)
}
Output:

Evaluate the expected value of x^2 + 3 under a Weibull distribution EV with 10 points = 4.20175 EV with 30 points = 4.19066 EV with 100 points = 4.19064 EV with 10000 points = 4.19064 Estimate using parallel evaluations of f. EV = 4.19064 

Share Format Run

### Index [¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/integrate/quad#pkg-index "Go to Index")

*   [func Fixed(f func(float64) float64, min, max float64, n int, rule FixedLocationer, ...) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/integrate/quad#Fixed)
*   [type FixedLocationSingler](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/integrate/quad#FixedLocationSingler)
*   [type FixedLocationer](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/integrate/quad#FixedLocationer)
*   [type Hermite](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/integrate/quad#Hermite)
*       *   [func (h Hermite) FixedLocations(x, weight []float64, min, max float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/integrate/quad#Hermite.FixedLocations)

*   [type Legendre](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/integrate/quad#Legendre)
*       *   [func (l Legendre) FixedLocationSingle(n, k int, min, max float64) (x, weight float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/integrate/quad#Legendre.FixedLocationSingle)
    *   [func (l Legendre) FixedLocations(x, weight []float64, min, max float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/integrate/quad#Legendre.FixedLocations)

### Examples [¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/integrate/quad#pkg-examples "Go to Examples")

*   [Package](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/integrate/quad#example-package)

### Constants [¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/integrate/quad#pkg-constants "Go to Constants")

This section is empty.

### Variables [¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/integrate/quad#pkg-variables "Go to Variables")

This section is empty.

### Functions [¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/integrate/quad#pkg-functions "Go to Functions")

#### func [Fixed](https://github.com/gonum/gonum/blob/v0.17.0/integrate/quad/quad.go#L46)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/integrate/quad#Fixed "Go to Fixed")

func Fixed(f func([float64](https://pkg.go.dev/builtin#float64)) [float64](https://pkg.go.dev/builtin#float64), min, max [float64](https://pkg.go.dev/builtin#float64), n [int](https://pkg.go.dev/builtin#int), rule [FixedLocationer](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/integrate/quad#FixedLocationer), concurrent [int](https://pkg.go.dev/builtin#int)) [float64](https://pkg.go.dev/builtin#float64)

Fixed approximates the integral of the function f from min to max using a fixed n-point quadrature rule. During evaluation, f will be evaluated n times using the weights and locations specified by rule. That is, Fixed estimates

int_min^max f(x) dx ≈ \sum_i w_i f(x_i)

If rule is nil, an acceptable default is chosen, otherwise it is assumed that the properties of the integral match the assumptions of rule. For example, Legendre assumes that the integration bounds are finite. If rule is also a FixedLocationSingler, the quadrature points are computed individually rather than as a unit.

If concurrent <= 0, f is evaluated serially, while if concurrent > 0, f may be evaluated with at most concurrent simultaneous evaluations.

min must be less than or equal to max, and n must be positive, otherwise Fixed will panic.

### Types [¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/integrate/quad#pkg-types "Go to Types")

#### type [FixedLocationSingler](https://github.com/gonum/gonum/blob/v0.17.0/integrate/quad/quad.go#L22)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/integrate/quad#FixedLocationSingler "Go to FixedLocationSingler")

type FixedLocationSingler interface {
// FixedLocationSingle returns the location and weight for	// element k in a fixed quadrature rule with n total samples
	// and integral bounds from min to max.
	FixedLocationSingle(n, k [int](https://pkg.go.dev/builtin#int), min, max [float64](https://pkg.go.dev/builtin#float64)) (x, weight [float64](https://pkg.go.dev/builtin#float64))
}

FixedLocationSingler wraps the FixedLocationSingle method.

#### type [FixedLocationer](https://github.com/gonum/gonum/blob/v0.17.0/integrate/quad/quad.go#L17)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/integrate/quad#FixedLocationer "Go to FixedLocationer")

type FixedLocationer interface {
 FixedLocations(x, weight [][float64](https://pkg.go.dev/builtin#float64), min, max [float64](https://pkg.go.dev/builtin#float64)) }

FixedLocationer computes a set of quadrature locations and weights and stores them in-place into x and weight respectively. The number of points generated is equal to the len(x). The weights and locations should be chosen such that

int_min^max f(x) dx ≈ \sum_i w_i f(x_i)

#### type [Hermite](https://github.com/gonum/gonum/blob/v0.17.0/integrate/quad/hermite.go#L18)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/integrate/quad#Hermite "Go to Hermite")

type Hermite struct{}

Hermite generates sample locations and weights for performing quadrature with a squared-exponential weight

int_-inf^inf e^(-x^2) f(x) dx .

#### func (Hermite) [FixedLocations](https://github.com/gonum/gonum/blob/v0.17.0/integrate/quad/hermite.go#L20)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/integrate/quad#Hermite.FixedLocations "Go to Hermite.FixedLocations")

func (h [Hermite](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/integrate/quad#Hermite)) FixedLocations(x, weight [][float64](https://pkg.go.dev/builtin#float64), min, max [float64](https://pkg.go.dev/builtin#float64))

#### type [Legendre](https://github.com/gonum/gonum/blob/v0.17.0/integrate/quad/legendre.go#L12)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/integrate/quad#Legendre "Go to Legendre")

type Legendre struct{}

Legendre integrates an unweighted function over finite bounds

int_min^max f(x) dx

#### func (Legendre) [FixedLocationSingle](https://github.com/gonum/gonum/blob/v0.17.0/integrate/quad/legendre.go#L41)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/integrate/quad#Legendre.FixedLocationSingle "Go to Legendre.FixedLocationSingle")

func (l [Legendre](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/integrate/quad#Legendre)) FixedLocationSingle(n, k [int](https://pkg.go.dev/builtin#int), min, max [float64](https://pkg.go.dev/builtin#float64)) (x, weight [float64](https://pkg.go.dev/builtin#float64))

#### func (Legendre) [FixedLocations](https://github.com/gonum/gonum/blob/v0.17.0/integrate/quad/legendre.go#L14)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/integrate/quad#Legendre.FixedLocations "Go to Legendre.FixedLocations")

func (l [Legendre](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/integrate/quad#Legendre)) FixedLocations(x, weight [][float64](https://pkg.go.dev/builtin#float64), min, max [float64](https://pkg.go.dev/builtin#float64))

![Image 44](https://pkg.go.dev/static/shared/icon/insert_drive_file_gm_grey_24dp.svg) Source Files [¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/integrate/quad#section-sourcefiles "Go to Source Files")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[View all Source files](https://github.com/gonum/gonum/tree/v0.17.0/integrate/quad)

*   [doc.go](https://github.com/gonum/gonum/blob/v0.17.0/integrate/quad/doc.go "doc.go")
*   [hermite.go](https://github.com/gonum/gonum/blob/v0.17.0/integrate/quad/hermite.go "hermite.go")
*   [hermite_data.go](https://github.com/gonum/gonum/blob/v0.17.0/integrate/quad/hermite_data.go "hermite_data.go")
*   [legendre.go](https://github.com/gonum/gonum/blob/v0.17.0/integrate/quad/legendre.go "legendre.go")
*   [quad.go](https://github.com/gonum/gonum/blob/v0.17.0/integrate/quad/quad.go "quad.go")

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
