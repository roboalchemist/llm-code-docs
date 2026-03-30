# Source: https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator

Title: iterator package - gonum.org/v1/gonum/graph/iterator - Go Packages

URL Source: https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator

Markdown Content:
iterator package - gonum.org/v1/gonum/graph/iterator - Go Packages
===============

[![Image 1: Go](https://pkg.go.dev/static/shared/logo/go-white.svg)](https://go.dev/)

[Skip to Main Content](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#main-content)

![Image 2](https://pkg.go.dev/static/shared/icon/search_gm_grey_24dp.svg)![Image 3](https://pkg.go.dev/static/shared/icon/search_gm_grey_24dp.svg)

*   [Why Go ![Image 4: submenu dropdown icon](https://pkg.go.dev/static/shared/icon/arrow_drop_down_gm_grey_24dp.svg)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#)
    *   [Case Studies](https://go.dev/solutions#case-studies) 
Common problems companies solve with Go

    *   [Use Cases](https://go.dev/solutions#use-cases) 
Stories about how and why companies use Go

    *   [Security](https://go.dev/security/) 
How Go can help keep you secure by default

*   [Learn](https://go.dev/learn/)
*   [Docs ![Image 5: submenu dropdown icon](https://pkg.go.dev/static/shared/icon/arrow_drop_down_gm_grey_24dp.svg)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#)
    *   [Effective Go](https://go.dev/doc/effective_go) 
Tips for writing clear, performant, and idiomatic Go code

    *   [Go User Manual](https://go.dev/doc/) 
A complete introduction to building software with Go

    *   [Standard library](https://pkg.go.dev/std) 
Reference documentation for Go's standard library

    *   [Release Notes](https://go.dev/doc/devel/release) 
Learn what's new in each Go release

*   [Packages](https://pkg.go.dev/)
*   [Community ![Image 6: submenu dropdown icon](https://pkg.go.dev/static/shared/icon/arrow_drop_down_gm_grey_24dp.svg)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#)
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

*   [Why Go _![Image 16](https://pkg.go.dev/static/shared/icon/navigate\_next\_gm\_grey\_24dp.svg)_](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#)

[_![Image 17](https://pkg.go.dev/static/shared/icon/navigate\_before\_gm\_grey\_24dp.svg)_ Why Go](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#) 
    *   [Case Studies](https://go.dev/solutions#case-studies)
    *   [Use Cases](https://go.dev/solutions#use-cases)
    *   [Security](https://go.dev/security/)

*   [Learn](https://go.dev/learn/)
*   [Docs _![Image 18](https://pkg.go.dev/static/shared/icon/navigate\_next\_gm\_grey\_24dp.svg)_](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#)

[_![Image 19](https://pkg.go.dev/static/shared/icon/navigate\_before\_gm\_grey\_24dp.svg)_ Docs](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#) 
    *   [Effective Go](https://go.dev/doc/effective_go)
    *   [Go User Manual](https://go.dev/doc/)
    *   [Standard library](https://pkg.go.dev/std)
    *   [Release Notes](https://go.dev/doc/devel/release)

*   [Packages](https://pkg.go.dev/)
*   [Community _![Image 20](https://pkg.go.dev/static/shared/icon/navigate\_next\_gm\_grey\_24dp.svg)_](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#)

[_![Image 21](https://pkg.go.dev/static/shared/icon/navigate\_before\_gm\_grey\_24dp.svg)_ Community](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#) 
    *   [Recorded Talks](https://go.dev/talks/)
    *   [Meetups _![Image 22](https://pkg.go.dev/static/shared/icon/launch\_gm\_grey\_24dp.svg)_](https://www.meetup.com/pro/go)
    *   [Conferences _![Image 23](https://pkg.go.dev/static/shared/icon/launch\_gm\_grey\_24dp.svg)_](https://github.com/golang/go/wiki/Conferences)
    *   [Go blog](https://go.dev/blog)
    *   [Go project](https://go.dev/help)
    *   Get connected [![Image 24](https://pkg.go.dev/static/shared/logo/social/google-groups.svg)](https://groups.google.com/g/golang-nuts)[![Image 25](https://pkg.go.dev/static/shared/logo/social/github.svg)](https://github.com/golang)[![Image 26](https://pkg.go.dev/static/shared/logo/social/twitter.svg)](https://twitter.com/golang)[![Image 27](https://pkg.go.dev/static/shared/logo/social/reddit.svg)](https://www.reddit.com/r/golang/)[![Image 28](https://pkg.go.dev/static/shared/logo/social/slack.svg)](https://invite.slack.golangbridge.org/)[![Image 29](https://pkg.go.dev/static/shared/logo/social/stack-overflow.svg)](https://stackoverflow.com/collectives/go) 

1.   [Discover Packages](https://pkg.go.dev/)
2.   [gonum.org/v1/gonum](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0)
3.   [graph](https://pkg.go.dev/gonum.org/v1/gonum/graph@v0.17.0)
4.   [iterator](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator)![Image 30](https://pkg.go.dev/static/shared/icon/content_copy_gm_grey_24dp.svg)

[![Image 31: Go](https://pkg.go.dev/static/shared/logo/go-blue.svg)](https://go.dev/)
iterator
========

package![Image 32](https://pkg.go.dev/static/shared/icon/content_copy_gm_grey_24dp.svg)

[Version: v0.17.0](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator?tab=versions)

 Opens a new window with list of versions in this module. 

Latest Latest 

![Image 33: Warning](https://pkg.go.dev/static/shared/icon/alert_gm_grey_24dp.svg)
This package is not in the latest version of its module.

[Go to latest](https://pkg.go.dev/gonum.org/v1/gonum/graph/iterator) Published: Dec 29, 2025  License: [BSD-3-Clause](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator?tab=licenses)

 Opens a new window with license information. 

[Imports: 2](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator?tab=imports)

 Opens a new window with list of imports. 

[Imported by: 69](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator?tab=importedby)

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

*   [Documentation](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#section-documentation)
    *   [Overview](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#pkg-overview)
    *   [Index](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#pkg-index)
    *   [Constants](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#pkg-constants)
    *   [Variables](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#pkg-variables)
    *   [Functions](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#pkg-functions)
    *   [Types](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#pkg-types)
        *   [type ImplicitNodes](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#ImplicitNodes "type ImplicitNodes")
            *   [NewImplicitNodes(beg, end, new)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#NewImplicitNodes "NewImplicitNodes(beg, end, new)")
            *   [(n) Len()](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#ImplicitNodes.Len "(n) Len()")
            *   [(n) Next()](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#ImplicitNodes.Next "(n) Next()")
            *   [(n) Node()](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#ImplicitNodes.Node "(n) Node()")
            *   [(n) NodeSlice()](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#ImplicitNodes.NodeSlice "(n) NodeSlice()")
            *   [(n) Reset()](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#ImplicitNodes.Reset "(n) Reset()")

        *   [type LazyOrderedNodes](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodes "type LazyOrderedNodes")
            *   [NewLazyOrderedNodes(nodes)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#NewLazyOrderedNodes "NewLazyOrderedNodes(nodes)")
            *   [(n) Len()](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodes.Len "(n) Len()")
            *   [(n) Next()](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodes.Next "(n) Next()")
            *   [(n) Node()](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodes.Node "(n) Node()")
            *   [(n) NodeSlice()](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodes.NodeSlice "(n) NodeSlice()")
            *   [(n) Reset()](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodes.Reset "(n) Reset()")

        *   [type LazyOrderedNodesByEdge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodesByEdge "type LazyOrderedNodesByEdge")
            *   [NewLazyOrderedNodesByEdge(nodes, edges)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#NewLazyOrderedNodesByEdge "NewLazyOrderedNodesByEdge(nodes, edges)")
            *   [(n) Len()](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodesByEdge.Len "(n) Len()")
            *   [(n) Next()](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodesByEdge.Next "(n) Next()")
            *   [(n) Node()](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodesByEdge.Node "(n) Node()")
            *   [(n) NodeSlice()](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodesByEdge.NodeSlice "(n) NodeSlice()")
            *   [(n) Reset()](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodesByEdge.Reset "(n) Reset()")

        *   [type LazyOrderedNodesByLines](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodesByLines "type LazyOrderedNodesByLines")
            *   [NewLazyOrderedNodesByLines(nodes, edges)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#NewLazyOrderedNodesByLines "NewLazyOrderedNodesByLines(nodes, edges)")
            *   [(n) Len()](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodesByLines.Len "(n) Len()")
            *   [(n) Next()](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodesByLines.Next "(n) Next()")
            *   [(n) Node()](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodesByLines.Node "(n) Node()")
            *   [(n) NodeSlice()](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodesByLines.NodeSlice "(n) NodeSlice()")
            *   [(n) Reset()](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodesByLines.Reset "(n) Reset()")

        *   [type LazyOrderedNodesByWeightedEdge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodesByWeightedEdge "type LazyOrderedNodesByWeightedEdge")
            *   [NewLazyOrderedNodesByWeightedEdge(nodes, edges)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#NewLazyOrderedNodesByWeightedEdge "NewLazyOrderedNodesByWeightedEdge(nodes, edges)")
            *   [(n) Len()](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodesByWeightedEdge.Len "(n) Len()")
            *   [(n) Next()](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodesByWeightedEdge.Next "(n) Next()")
            *   [(n) Node()](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodesByWeightedEdge.Node "(n) Node()")
            *   [(n) NodeSlice()](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodesByWeightedEdge.NodeSlice "(n) NodeSlice()")
            *   [(n) Reset()](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodesByWeightedEdge.Reset "(n) Reset()")

        *   [type LazyOrderedNodesByWeightedLines](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodesByWeightedLines "type LazyOrderedNodesByWeightedLines")
            *   [NewLazyOrderedNodesByWeightedLines(nodes, edges)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#NewLazyOrderedNodesByWeightedLines "NewLazyOrderedNodesByWeightedLines(nodes, edges)")
            *   [(n) Len()](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodesByWeightedLines.Len "(n) Len()")
            *   [(n) Next()](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodesByWeightedLines.Next "(n) Next()")
            *   [(n) Node()](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodesByWeightedLines.Node "(n) Node()")
            *   [(n) NodeSlice()](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodesByWeightedLines.NodeSlice "(n) NodeSlice()")
            *   [(n) Reset()](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodesByWeightedLines.Reset "(n) Reset()")

        *   [type Lines](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#Lines "type Lines")
            *   [NewLines(lines)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#NewLines "NewLines(lines)")
            *   [(l) Len()](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#Lines.Len "(l) Len()")
            *   [(l) Line()](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#Lines.Line "(l) Line()")
            *   [(l) LineSlice()](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#Lines.LineSlice "(l) LineSlice()")
            *   [(l) Next()](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#Lines.Next "(l) Next()")
            *   [(l) Reset()](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#Lines.Reset "(l) Reset()")

        *   [type Nodes](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#Nodes "type Nodes")
            *   [NewNodes(nodes)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#NewNodes "NewNodes(nodes)")
            *   [(n) Len()](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#Nodes.Len "(n) Len()")
            *   [(n) Next()](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#Nodes.Next "(n) Next()")
            *   [(n) Node()](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#Nodes.Node "(n) Node()")
            *   [(n) NodeSlice()](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#Nodes.NodeSlice "(n) NodeSlice()")
            *   [(n) Reset()](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#Nodes.Reset "(n) Reset()")

        *   [type NodesByEdge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#NodesByEdge "type NodesByEdge")
            *   [NewNodesByEdge(nodes, edges)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#NewNodesByEdge "NewNodesByEdge(nodes, edges)")
            *   [NewNodesByLines(nodes, lines)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#NewNodesByLines "NewNodesByLines(nodes, lines)")
            *   [NewNodesByWeightedEdge(nodes, edges)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#NewNodesByWeightedEdge "NewNodesByWeightedEdge(nodes, edges)")
            *   [NewNodesByWeightedLines(nodes, lines)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#NewNodesByWeightedLines "NewNodesByWeightedLines(nodes, lines)")
            *   [(n) Len()](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#NodesByEdge.Len "(n) Len()")
            *   [(n) Next()](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#NodesByEdge.Next "(n) Next()")
            *   [(n) Node()](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#NodesByEdge.Node "(n) Node()")
            *   [(n) NodeSlice()](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#NodesByEdge.NodeSlice "(n) NodeSlice()")
            *   [(n) Reset()](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#NodesByEdge.Reset "(n) Reset()")

        *   [type OrderedEdges](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedEdges "type OrderedEdges")
            *   [NewOrderedEdges(edges)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#NewOrderedEdges "NewOrderedEdges(edges)")
            *   [(e) Edge()](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedEdges.Edge "(e) Edge()")
            *   [(e) EdgeSlice()](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedEdges.EdgeSlice "(e) EdgeSlice()")
            *   [(e) Len()](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedEdges.Len "(e) Len()")
            *   [(e) Next()](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedEdges.Next "(e) Next()")
            *   [(e) Reset()](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedEdges.Reset "(e) Reset()")

        *   [type OrderedLines](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedLines "type OrderedLines")
            *   [NewOrderedLines(lines)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#NewOrderedLines "NewOrderedLines(lines)")
            *   [(e) Len()](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedLines.Len "(e) Len()")
            *   [(e) Line()](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedLines.Line "(e) Line()")
            *   [(e) LineSlice()](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedLines.LineSlice "(e) LineSlice()")
            *   [(e) Next()](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedLines.Next "(e) Next()")
            *   [(e) Reset()](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedLines.Reset "(e) Reset()")

        *   [type OrderedNodes](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedNodes "type OrderedNodes")
            *   [NewOrderedNodes(nodes)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#NewOrderedNodes "NewOrderedNodes(nodes)")
            *   [(n) Len()](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedNodes.Len "(n) Len()")
            *   [(n) Next()](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedNodes.Next "(n) Next()")
            *   [(n) Node()](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedNodes.Node "(n) Node()")
            *   [(n) NodeSlice()](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedNodes.NodeSlice "(n) NodeSlice()")
            *   [(n) Reset()](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedNodes.Reset "(n) Reset()")

        *   [type OrderedWeightedEdges](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedWeightedEdges "type OrderedWeightedEdges")
            *   [NewOrderedWeightedEdges(edges)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#NewOrderedWeightedEdges "NewOrderedWeightedEdges(edges)")
            *   [(e) Len()](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedWeightedEdges.Len "(e) Len()")
            *   [(e) Next()](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedWeightedEdges.Next "(e) Next()")
            *   [(e) Reset()](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedWeightedEdges.Reset "(e) Reset()")
            *   [(e) WeightedEdge()](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedWeightedEdges.WeightedEdge "(e) WeightedEdge()")
            *   [(e) WeightedEdgeSlice()](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedWeightedEdges.WeightedEdgeSlice "(e) WeightedEdgeSlice()")

        *   [type OrderedWeightedLines](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedWeightedLines "type OrderedWeightedLines")
            *   [NewOrderedWeightedLines(lines)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#NewOrderedWeightedLines "NewOrderedWeightedLines(lines)")
            *   [(e) Len()](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedWeightedLines.Len "(e) Len()")
            *   [(e) Next()](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedWeightedLines.Next "(e) Next()")
            *   [(e) Reset()](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedWeightedLines.Reset "(e) Reset()")
            *   [(e) WeightedLine()](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedWeightedLines.WeightedLine "(e) WeightedLine()")
            *   [(e) WeightedLineSlice()](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedWeightedLines.WeightedLineSlice "(e) WeightedLineSlice()")

        *   [type WeightedLines](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#WeightedLines "type WeightedLines")
            *   [NewWeightedLines(lines)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#NewWeightedLines "NewWeightedLines(lines)")
            *   [(l) Len()](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#WeightedLines.Len "(l) Len()")
            *   [(l) Next()](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#WeightedLines.Next "(l) Next()")
            *   [(l) Reset()](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#WeightedLines.Reset "(l) Reset()")
            *   [(l) WeightedLine()](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#WeightedLines.WeightedLine "(l) WeightedLine()")
            *   [(l) WeightedLineSlice()](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#WeightedLines.WeightedLineSlice "(l) WeightedLineSlice()")

*   [Source Files](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#section-sourcefiles)

![Image 43](https://pkg.go.dev/static/shared/icon/code_gm_grey_24dp.svg) Documentation [¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#section-documentation "Go to Documentation")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Overview [¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#pkg-overview "Go to Overview")

Package iterator provides node, edge and line iterators.

The iterators provided satisfy the graph.Nodes, graph.Edges and graph.Lines interfaces.

### Index [¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#pkg-index "Go to Index")

*   [type ImplicitNodes](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#ImplicitNodes)
*       *   [func NewImplicitNodes(beg, end int, new func(id int) graph.Node) *ImplicitNodes](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#NewImplicitNodes)

*       *   [func (n *ImplicitNodes) Len() int](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#ImplicitNodes.Len)
    *   [func (n *ImplicitNodes) Next() bool](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#ImplicitNodes.Next)
    *   [func (n *ImplicitNodes) Node() graph.Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#ImplicitNodes.Node)
    *   [func (n *ImplicitNodes) NodeSlice() []graph.Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#ImplicitNodes.NodeSlice)
    *   [func (n *ImplicitNodes) Reset()](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#ImplicitNodes.Reset)

*   [type LazyOrderedNodes](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodes)
*       *   [func NewLazyOrderedNodes(nodes map[int64]graph.Node) *LazyOrderedNodes](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#NewLazyOrderedNodes)

*       *   [func (n *LazyOrderedNodes) Len() int](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodes.Len)
    *   [func (n *LazyOrderedNodes) Next() bool](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodes.Next)
    *   [func (n *LazyOrderedNodes) Node() graph.Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodes.Node)
    *   [func (n *LazyOrderedNodes) NodeSlice() []graph.Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodes.NodeSlice)
    *   [func (n *LazyOrderedNodes) Reset()](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodes.Reset)

*   [type LazyOrderedNodesByEdge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodesByEdge)
*       *   [func NewLazyOrderedNodesByEdge(nodes map[int64]graph.Node, edges map[int64]graph.Edge) *LazyOrderedNodesByEdge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#NewLazyOrderedNodesByEdge)

*       *   [func (n *LazyOrderedNodesByEdge) Len() int](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodesByEdge.Len)
    *   [func (n *LazyOrderedNodesByEdge) Next() bool](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodesByEdge.Next)
    *   [func (n *LazyOrderedNodesByEdge) Node() graph.Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodesByEdge.Node)
    *   [func (n *LazyOrderedNodesByEdge) NodeSlice() []graph.Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodesByEdge.NodeSlice)
    *   [func (n *LazyOrderedNodesByEdge) Reset()](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodesByEdge.Reset)

*   [type LazyOrderedNodesByLines](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodesByLines)
*       *   [func NewLazyOrderedNodesByLines(nodes map[int64]graph.Node, edges map[int64]map[int64]graph.Line) *LazyOrderedNodesByLines](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#NewLazyOrderedNodesByLines)

*       *   [func (n *LazyOrderedNodesByLines) Len() int](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodesByLines.Len)
    *   [func (n *LazyOrderedNodesByLines) Next() bool](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodesByLines.Next)
    *   [func (n *LazyOrderedNodesByLines) Node() graph.Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodesByLines.Node)
    *   [func (n *LazyOrderedNodesByLines) NodeSlice() []graph.Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodesByLines.NodeSlice)
    *   [func (n *LazyOrderedNodesByLines) Reset()](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodesByLines.Reset)

*   [type LazyOrderedNodesByWeightedEdge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodesByWeightedEdge)
*       *   [func NewLazyOrderedNodesByWeightedEdge(nodes map[int64]graph.Node, edges map[int64]graph.WeightedEdge) *LazyOrderedNodesByWeightedEdge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#NewLazyOrderedNodesByWeightedEdge)

*       *   [func (n *LazyOrderedNodesByWeightedEdge) Len() int](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodesByWeightedEdge.Len)
    *   [func (n *LazyOrderedNodesByWeightedEdge) Next() bool](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodesByWeightedEdge.Next)
    *   [func (n *LazyOrderedNodesByWeightedEdge) Node() graph.Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodesByWeightedEdge.Node)
    *   [func (n *LazyOrderedNodesByWeightedEdge) NodeSlice() []graph.Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodesByWeightedEdge.NodeSlice)
    *   [func (n *LazyOrderedNodesByWeightedEdge) Reset()](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodesByWeightedEdge.Reset)

*   [type LazyOrderedNodesByWeightedLines](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodesByWeightedLines)
*       *   [func NewLazyOrderedNodesByWeightedLines(nodes map[int64]graph.Node, edges map[int64]map[int64]graph.WeightedLine) *LazyOrderedNodesByWeightedLines](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#NewLazyOrderedNodesByWeightedLines)

*       *   [func (n *LazyOrderedNodesByWeightedLines) Len() int](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodesByWeightedLines.Len)
    *   [func (n *LazyOrderedNodesByWeightedLines) Next() bool](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodesByWeightedLines.Next)
    *   [func (n *LazyOrderedNodesByWeightedLines) Node() graph.Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodesByWeightedLines.Node)
    *   [func (n *LazyOrderedNodesByWeightedLines) NodeSlice() []graph.Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodesByWeightedLines.NodeSlice)
    *   [func (n *LazyOrderedNodesByWeightedLines) Reset()](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodesByWeightedLines.Reset)

*   [type Lines](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#Lines)
*       *   [func NewLines(lines map[int64]graph.Line) *Lines](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#NewLines)

*       *   [func (l *Lines) Len() int](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#Lines.Len)
    *   [func (l *Lines) Line() graph.Line](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#Lines.Line)
    *   [func (l *Lines) LineSlice() []graph.Line](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#Lines.LineSlice)
    *   [func (l *Lines) Next() bool](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#Lines.Next)
    *   [func (l *Lines) Reset()](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#Lines.Reset)

*   [type Nodes](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#Nodes)
*       *   [func NewNodes(nodes map[int64]graph.Node) *Nodes](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#NewNodes)

*       *   [func (n *Nodes) Len() int](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#Nodes.Len)
    *   [func (n *Nodes) Next() bool](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#Nodes.Next)
    *   [func (n *Nodes) Node() graph.Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#Nodes.Node)
    *   [func (n *Nodes) NodeSlice() []graph.Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#Nodes.NodeSlice)
    *   [func (n *Nodes) Reset()](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#Nodes.Reset)

*   [type NodesByEdge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#NodesByEdge)
*       *   [func NewNodesByEdge(nodes map[int64]graph.Node, edges map[int64]graph.Edge) *NodesByEdge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#NewNodesByEdge)
    *   [func NewNodesByLines(nodes map[int64]graph.Node, lines map[int64]map[int64]graph.Line) *NodesByEdge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#NewNodesByLines)
    *   [func NewNodesByWeightedEdge(nodes map[int64]graph.Node, edges map[int64]graph.WeightedEdge) *NodesByEdge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#NewNodesByWeightedEdge)
    *   [func NewNodesByWeightedLines(nodes map[int64]graph.Node, lines map[int64]map[int64]graph.WeightedLine) *NodesByEdge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#NewNodesByWeightedLines)

*       *   [func (n *NodesByEdge) Len() int](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#NodesByEdge.Len)
    *   [func (n *NodesByEdge) Next() bool](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#NodesByEdge.Next)
    *   [func (n *NodesByEdge) Node() graph.Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#NodesByEdge.Node)
    *   [func (n *NodesByEdge) NodeSlice() []graph.Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#NodesByEdge.NodeSlice)
    *   [func (n *NodesByEdge) Reset()](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#NodesByEdge.Reset)

*   [type OrderedEdges](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedEdges)
*       *   [func NewOrderedEdges(edges []graph.Edge) *OrderedEdges](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#NewOrderedEdges)

*       *   [func (e *OrderedEdges) Edge() graph.Edge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedEdges.Edge)
    *   [func (e *OrderedEdges) EdgeSlice() []graph.Edge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedEdges.EdgeSlice)
    *   [func (e *OrderedEdges) Len() int](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedEdges.Len)
    *   [func (e *OrderedEdges) Next() bool](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedEdges.Next)
    *   [func (e *OrderedEdges) Reset()](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedEdges.Reset)

*   [type OrderedLines](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedLines)
*       *   [func NewOrderedLines(lines []graph.Line) *OrderedLines](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#NewOrderedLines)

*       *   [func (e *OrderedLines) Len() int](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedLines.Len)
    *   [func (e *OrderedLines) Line() graph.Line](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedLines.Line)
    *   [func (e *OrderedLines) LineSlice() []graph.Line](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedLines.LineSlice)
    *   [func (e *OrderedLines) Next() bool](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedLines.Next)
    *   [func (e *OrderedLines) Reset()](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedLines.Reset)

*   [type OrderedNodes](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedNodes)
*       *   [func NewOrderedNodes(nodes []graph.Node) *OrderedNodes](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#NewOrderedNodes)

*       *   [func (n *OrderedNodes) Len() int](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedNodes.Len)
    *   [func (n *OrderedNodes) Next() bool](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedNodes.Next)
    *   [func (n *OrderedNodes) Node() graph.Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedNodes.Node)
    *   [func (n *OrderedNodes) NodeSlice() []graph.Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedNodes.NodeSlice)
    *   [func (n *OrderedNodes) Reset()](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedNodes.Reset)

*   [type OrderedWeightedEdges](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedWeightedEdges)
*       *   [func NewOrderedWeightedEdges(edges []graph.WeightedEdge) *OrderedWeightedEdges](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#NewOrderedWeightedEdges)

*       *   [func (e *OrderedWeightedEdges) Len() int](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedWeightedEdges.Len)
    *   [func (e *OrderedWeightedEdges) Next() bool](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedWeightedEdges.Next)
    *   [func (e *OrderedWeightedEdges) Reset()](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedWeightedEdges.Reset)
    *   [func (e *OrderedWeightedEdges) WeightedEdge() graph.WeightedEdge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedWeightedEdges.WeightedEdge)
    *   [func (e *OrderedWeightedEdges) WeightedEdgeSlice() []graph.WeightedEdge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedWeightedEdges.WeightedEdgeSlice)

*   [type OrderedWeightedLines](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedWeightedLines)
*       *   [func NewOrderedWeightedLines(lines []graph.WeightedLine) *OrderedWeightedLines](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#NewOrderedWeightedLines)

*       *   [func (e *OrderedWeightedLines) Len() int](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedWeightedLines.Len)
    *   [func (e *OrderedWeightedLines) Next() bool](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedWeightedLines.Next)
    *   [func (e *OrderedWeightedLines) Reset()](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedWeightedLines.Reset)
    *   [func (e *OrderedWeightedLines) WeightedLine() graph.WeightedLine](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedWeightedLines.WeightedLine)
    *   [func (e *OrderedWeightedLines) WeightedLineSlice() []graph.WeightedLine](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedWeightedLines.WeightedLineSlice)

*   [type WeightedLines](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#WeightedLines)
*       *   [func NewWeightedLines(lines map[int64]graph.WeightedLine) *WeightedLines](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#NewWeightedLines)

*       *   [func (l *WeightedLines) Len() int](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#WeightedLines.Len)
    *   [func (l *WeightedLines) Next() bool](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#WeightedLines.Next)
    *   [func (l *WeightedLines) Reset()](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#WeightedLines.Reset)
    *   [func (l *WeightedLines) WeightedLine() graph.WeightedLine](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#WeightedLines.WeightedLine)
    *   [func (l *WeightedLines) WeightedLineSlice() []graph.WeightedLine](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#WeightedLines.WeightedLineSlice)

### Constants [¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#pkg-constants "Go to Constants")

This section is empty.

### Variables [¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#pkg-variables "Go to Variables")

This section is empty.

### Functions [¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#pkg-functions "Go to Functions")

This section is empty.

### Types [¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#pkg-types "Go to Types")

#### type [ImplicitNodes](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/nodes.go#L374)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#ImplicitNodes "Go to ImplicitNodes")

type ImplicitNodes struct {
	// contains filtered or unexported fields
}

ImplicitNodes implements the graph.Nodes interface for a set of nodes over a contiguous ID range.

#### func [NewImplicitNodes](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/nodes.go#L383)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#NewImplicitNodes "Go to NewImplicitNodes")

func NewImplicitNodes(beg, end [int](https://pkg.go.dev/builtin#int), new func(id [int](https://pkg.go.dev/builtin#int)) [graph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph#Node)) *[ImplicitNodes](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#ImplicitNodes)

NewImplicitNodes returns a new implicit node iterator spanning nodes in [beg,end). The provided new func maps the id to a graph.Node. NewImplicitNodes will panic if beg is greater than end.

#### func (*ImplicitNodes) [Len](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/nodes.go#L391)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#ImplicitNodes.Len "Go to ImplicitNodes.Len")

func (n *[ImplicitNodes](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#ImplicitNodes)) Len() [int](https://pkg.go.dev/builtin#int)

Len returns the remaining number of nodes to be iterated over.

#### func (*ImplicitNodes) [Next](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/nodes.go#L399)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#ImplicitNodes.Next "Go to ImplicitNodes.Next")

func (n *[ImplicitNodes](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#ImplicitNodes)) Next() [bool](https://pkg.go.dev/builtin#bool)

Next returns whether the next call of Node will return a valid node.

#### func (*ImplicitNodes) [Node](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/nodes.go#L409)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#ImplicitNodes.Node "Go to ImplicitNodes.Node")

func (n *[ImplicitNodes](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#ImplicitNodes)) Node() [graph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph#Node)

Node returns the current node of the iterator. Next must have been called prior to a call to Node.

#### func (*ImplicitNodes) [NodeSlice](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/nodes.go#L423)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#ImplicitNodes.NodeSlice "Go to ImplicitNodes.NodeSlice")

func (n *[ImplicitNodes](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#ImplicitNodes)) NodeSlice() [][graph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph#Node)

NodeSlice returns all the remaining nodes in the iterator and advances the iterator.

#### func (*ImplicitNodes) [Reset](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/nodes.go#L417)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#ImplicitNodes.Reset "Go to ImplicitNodes.Reset")

func (n *[ImplicitNodes](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#ImplicitNodes)) Reset()

Reset returns the iterator to its initial state.

#### type [LazyOrderedNodes](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/nodes.go#L68)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodes "Go to LazyOrderedNodes")added in v0.8.0

type LazyOrderedNodes struct {
	// contains filtered or unexported fields
}

LazyOrderedNodes implements the graph.Nodes and graph.NodeSlicer interfaces. The iteration order of LazyOrderedNodes is not determined until the first call to Next or NodeSlice. After that, the iteration order is fixed.

#### func [NewLazyOrderedNodes](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/nodes.go#L74)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#NewLazyOrderedNodes "Go to NewLazyOrderedNodes")added in v0.8.0

func NewLazyOrderedNodes(nodes map[[int64](https://pkg.go.dev/builtin#int64)][graph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph#Node)) *[LazyOrderedNodes](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodes)

NewLazyOrderedNodes returns a LazyOrderedNodes initialized with the provided nodes.

#### func (*LazyOrderedNodes) [Len](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/nodes.go#L79)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodes.Len "Go to LazyOrderedNodes.Len")added in v0.8.0

func (n *[LazyOrderedNodes](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodes)) Len() [int](https://pkg.go.dev/builtin#int)

Len returns the remaining number of nodes to be iterated over.

#### func (*LazyOrderedNodes) [Next](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/nodes.go#L87)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodes.Next "Go to LazyOrderedNodes.Next")added in v0.8.0

func (n *[LazyOrderedNodes](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodes)) Next() [bool](https://pkg.go.dev/builtin#bool)

Next returns whether the next call of Node will return a valid node.

#### func (*LazyOrderedNodes) [Node](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/nodes.go#L96)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodes.Node "Go to LazyOrderedNodes.Node")added in v0.8.0

func (n *[LazyOrderedNodes](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodes)) Node() [graph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph#Node)

Node returns the current node of the iterator. Next must have been called prior to a call to Node.

#### func (*LazyOrderedNodes) [NodeSlice](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/nodes.go#L102)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodes.NodeSlice "Go to LazyOrderedNodes.NodeSlice")added in v0.8.0

func (n *[LazyOrderedNodes](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodes)) NodeSlice() [][graph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph#Node)

NodeSlice returns all the remaining nodes in the iterator and advances the iterator.

#### func (*LazyOrderedNodes) [Reset](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/nodes.go#L110)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodes.Reset "Go to LazyOrderedNodes.Reset")added in v0.8.0

func (n *[LazyOrderedNodes](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodes)) Reset()

Reset returns the iterator to its initial state.

#### type [LazyOrderedNodesByEdge](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/nodes.go#L127)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodesByEdge "Go to LazyOrderedNodesByEdge")added in v0.8.0

type LazyOrderedNodesByEdge struct {
	// contains filtered or unexported fields
}

LazyOrderedNodesByEdge implements the graph.Nodes and graph.NodeSlicer interfaces. The iteration order of LazyOrderedNodesByEdge is not determined until the first call to Next or NodeSlice. After that, the iteration order is fixed.

#### func [NewLazyOrderedNodesByEdge](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/nodes.go#L135)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#NewLazyOrderedNodesByEdge "Go to NewLazyOrderedNodesByEdge")added in v0.8.0

func NewLazyOrderedNodesByEdge(nodes map[[int64](https://pkg.go.dev/builtin#int64)][graph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph#Node), edges map[[int64](https://pkg.go.dev/builtin#int64)][graph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph).[Edge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph#Edge)) *[LazyOrderedNodesByEdge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodesByEdge)

NewLazyOrderedNodesByEdge returns a LazyOrderedNodesByEdge initialized with the provided nodes.

#### func (*LazyOrderedNodesByEdge) [Len](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/nodes.go#L140)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodesByEdge.Len "Go to LazyOrderedNodesByEdge.Len")added in v0.8.0

func (n *[LazyOrderedNodesByEdge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodesByEdge)) Len() [int](https://pkg.go.dev/builtin#int)

Len returns the remaining number of nodes to be iterated over.

#### func (*LazyOrderedNodesByEdge) [Next](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/nodes.go#L148)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodesByEdge.Next "Go to LazyOrderedNodesByEdge.Next")added in v0.8.0

func (n *[LazyOrderedNodesByEdge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodesByEdge)) Next() [bool](https://pkg.go.dev/builtin#bool)

Next returns whether the next call of Node will return a valid node.

#### func (*LazyOrderedNodesByEdge) [Node](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/nodes.go#L157)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodesByEdge.Node "Go to LazyOrderedNodesByEdge.Node")added in v0.8.0

func (n *[LazyOrderedNodesByEdge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodesByEdge)) Node() [graph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph#Node)

Node returns the current node of the iterator. Next must have been called prior to a call to Node.

#### func (*LazyOrderedNodesByEdge) [NodeSlice](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/nodes.go#L163)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodesByEdge.NodeSlice "Go to LazyOrderedNodesByEdge.NodeSlice")added in v0.8.0

func (n *[LazyOrderedNodesByEdge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodesByEdge)) NodeSlice() [][graph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph#Node)

NodeSlice returns all the remaining nodes in the iterator and advances the iterator.

#### func (*LazyOrderedNodesByEdge) [Reset](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/nodes.go#L171)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodesByEdge.Reset "Go to LazyOrderedNodesByEdge.Reset")added in v0.8.0

func (n *[LazyOrderedNodesByEdge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodesByEdge)) Reset()

Reset returns the iterator to its initial state.

#### type [LazyOrderedNodesByLines](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/nodes.go#L251)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodesByLines "Go to LazyOrderedNodesByLines")added in v0.8.0

type LazyOrderedNodesByLines struct {
	// contains filtered or unexported fields
}

LazyOrderedNodesByLines implements the graph.Nodes and graph.NodeSlicer interfaces. The iteration order of LazyOrderedNodesByLines is not determined until the first call to Next or NodeSlice. After that, the iteration order is fixed.

#### func [NewLazyOrderedNodesByLines](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/nodes.go#L259)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#NewLazyOrderedNodesByLines "Go to NewLazyOrderedNodesByLines")added in v0.8.0

func NewLazyOrderedNodesByLines(nodes map[[int64](https://pkg.go.dev/builtin#int64)][graph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph#Node), edges map[[int64](https://pkg.go.dev/builtin#int64)]map[[int64](https://pkg.go.dev/builtin#int64)][graph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph).[Line](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph#Line)) *[LazyOrderedNodesByLines](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodesByLines)

NewLazyOrderedNodesByLines returns a LazyOrderedNodesByLines initialized with the provided nodes.

#### func (*LazyOrderedNodesByLines) [Len](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/nodes.go#L264)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodesByLines.Len "Go to LazyOrderedNodesByLines.Len")added in v0.8.0

func (n *[LazyOrderedNodesByLines](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodesByLines)) Len() [int](https://pkg.go.dev/builtin#int)

Len returns the remaining number of nodes to be iterated over.

#### func (*LazyOrderedNodesByLines) [Next](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/nodes.go#L272)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodesByLines.Next "Go to LazyOrderedNodesByLines.Next")added in v0.8.0

func (n *[LazyOrderedNodesByLines](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodesByLines)) Next() [bool](https://pkg.go.dev/builtin#bool)

Next returns whether the next call of Node will return a valid node.

#### func (*LazyOrderedNodesByLines) [Node](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/nodes.go#L281)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodesByLines.Node "Go to LazyOrderedNodesByLines.Node")added in v0.8.0

func (n *[LazyOrderedNodesByLines](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodesByLines)) Node() [graph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph#Node)

Node returns the current node of the iterator. Next must have been called prior to a call to Node.

#### func (*LazyOrderedNodesByLines) [NodeSlice](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/nodes.go#L287)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodesByLines.NodeSlice "Go to LazyOrderedNodesByLines.NodeSlice")added in v0.8.0

func (n *[LazyOrderedNodesByLines](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodesByLines)) NodeSlice() [][graph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph#Node)

NodeSlice returns all the remaining nodes in the iterator and advances the iterator.

#### func (*LazyOrderedNodesByLines) [Reset](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/nodes.go#L295)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodesByLines.Reset "Go to LazyOrderedNodesByLines.Reset")added in v0.8.0

func (n *[LazyOrderedNodesByLines](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodesByLines)) Reset()

Reset returns the iterator to its initial state.

#### type [LazyOrderedNodesByWeightedEdge](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/nodes.go#L189)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodesByWeightedEdge "Go to LazyOrderedNodesByWeightedEdge")added in v0.8.0

type LazyOrderedNodesByWeightedEdge struct {
	// contains filtered or unexported fields
}

LazyOrderedNodesByWeightedEdge implements the graph.Nodes and graph.NodeSlicer interfaces. The iteration order of LazyOrderedNodesByEeightedEdge is not determined until the first call to Next or NodeSlice. After that, the iteration order is fixed.

#### func [NewLazyOrderedNodesByWeightedEdge](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/nodes.go#L197)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#NewLazyOrderedNodesByWeightedEdge "Go to NewLazyOrderedNodesByWeightedEdge")added in v0.8.0

func NewLazyOrderedNodesByWeightedEdge(nodes map[[int64](https://pkg.go.dev/builtin#int64)][graph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph#Node), edges map[[int64](https://pkg.go.dev/builtin#int64)][graph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph).[WeightedEdge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph#WeightedEdge)) *[LazyOrderedNodesByWeightedEdge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodesByWeightedEdge)

NewLazyOrderedNodesByWeightedEdge returns a LazyOrderedNodesByEdge initialized with the provided nodes.

#### func (*LazyOrderedNodesByWeightedEdge) [Len](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/nodes.go#L202)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodesByWeightedEdge.Len "Go to LazyOrderedNodesByWeightedEdge.Len")added in v0.8.0

func (n *[LazyOrderedNodesByWeightedEdge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodesByWeightedEdge)) Len() [int](https://pkg.go.dev/builtin#int)

Len returns the remaining number of nodes to be iterated over.

#### func (*LazyOrderedNodesByWeightedEdge) [Next](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/nodes.go#L210)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodesByWeightedEdge.Next "Go to LazyOrderedNodesByWeightedEdge.Next")added in v0.8.0

func (n *[LazyOrderedNodesByWeightedEdge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodesByWeightedEdge)) Next() [bool](https://pkg.go.dev/builtin#bool)

Next returns whether the next call of Node will return a valid node.

#### func (*LazyOrderedNodesByWeightedEdge) [Node](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/nodes.go#L219)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodesByWeightedEdge.Node "Go to LazyOrderedNodesByWeightedEdge.Node")added in v0.8.0

func (n *[LazyOrderedNodesByWeightedEdge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodesByWeightedEdge)) Node() [graph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph#Node)

Node returns the current node of the iterator. Next must have been called prior to a call to Node.

#### func (*LazyOrderedNodesByWeightedEdge) [NodeSlice](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/nodes.go#L225)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodesByWeightedEdge.NodeSlice "Go to LazyOrderedNodesByWeightedEdge.NodeSlice")added in v0.8.0

func (n *[LazyOrderedNodesByWeightedEdge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodesByWeightedEdge)) NodeSlice() [][graph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph#Node)

NodeSlice returns all the remaining nodes in the iterator and advances the iterator.

#### func (*LazyOrderedNodesByWeightedEdge) [Reset](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/nodes.go#L233)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodesByWeightedEdge.Reset "Go to LazyOrderedNodesByWeightedEdge.Reset")added in v0.8.0

func (n *[LazyOrderedNodesByWeightedEdge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodesByWeightedEdge)) Reset()

Reset returns the iterator to its initial state.

#### type [LazyOrderedNodesByWeightedLines](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/nodes.go#L313)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodesByWeightedLines "Go to LazyOrderedNodesByWeightedLines")added in v0.8.0

type LazyOrderedNodesByWeightedLines struct {
	// contains filtered or unexported fields
}

LazyOrderedNodesByWeightedLines implements the graph.Nodes and graph.NodeSlicer interfaces. The iteration order of LazyOrderedNodesByEeightedLine is not determined until the first call to Next or NodeSlice. After that, the iteration order is fixed.

#### func [NewLazyOrderedNodesByWeightedLines](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/nodes.go#L321)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#NewLazyOrderedNodesByWeightedLines "Go to NewLazyOrderedNodesByWeightedLines")added in v0.8.0

func NewLazyOrderedNodesByWeightedLines(nodes map[[int64](https://pkg.go.dev/builtin#int64)][graph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph#Node), edges map[[int64](https://pkg.go.dev/builtin#int64)]map[[int64](https://pkg.go.dev/builtin#int64)][graph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph).[WeightedLine](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph#WeightedLine)) *[LazyOrderedNodesByWeightedLines](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodesByWeightedLines)

NewLazyOrderedNodesByWeightedLines returns a LazyOrderedNodesByLines initialized with the provided nodes.

#### func (*LazyOrderedNodesByWeightedLines) [Len](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/nodes.go#L326)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodesByWeightedLines.Len "Go to LazyOrderedNodesByWeightedLines.Len")added in v0.8.0

func (n *[LazyOrderedNodesByWeightedLines](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodesByWeightedLines)) Len() [int](https://pkg.go.dev/builtin#int)

Len returns the remaining number of nodes to be iterated over.

#### func (*LazyOrderedNodesByWeightedLines) [Next](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/nodes.go#L334)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodesByWeightedLines.Next "Go to LazyOrderedNodesByWeightedLines.Next")added in v0.8.0

func (n *[LazyOrderedNodesByWeightedLines](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodesByWeightedLines)) Next() [bool](https://pkg.go.dev/builtin#bool)

Next returns whether the next call of Node will return a valid node.

#### func (*LazyOrderedNodesByWeightedLines) [Node](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/nodes.go#L343)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodesByWeightedLines.Node "Go to LazyOrderedNodesByWeightedLines.Node")added in v0.8.0

func (n *[LazyOrderedNodesByWeightedLines](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodesByWeightedLines)) Node() [graph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph#Node)

Node returns the current node of the iterator. Next must have been called prior to a call to Node.

#### func (*LazyOrderedNodesByWeightedLines) [NodeSlice](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/nodes.go#L349)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodesByWeightedLines.NodeSlice "Go to LazyOrderedNodesByWeightedLines.NodeSlice")added in v0.8.0

func (n *[LazyOrderedNodesByWeightedLines](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodesByWeightedLines)) NodeSlice() [][graph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph#Node)

NodeSlice returns all the remaining nodes in the iterator and advances the iterator.

#### func (*LazyOrderedNodesByWeightedLines) [Reset](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/nodes.go#L357)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodesByWeightedLines.Reset "Go to LazyOrderedNodesByWeightedLines.Reset")added in v0.8.0

func (n *[LazyOrderedNodesByWeightedLines](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#LazyOrderedNodesByWeightedLines)) Reset()

Reset returns the iterator to its initial state.

#### type [Lines](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/lines_map.go#L14)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#Lines "Go to Lines")added in v0.11.0

type Lines struct {
	// contains filtered or unexported fields
}

Lines implements the graph.Lines interfaces. The iteration order of Lines is randomized.

#### func [NewLines](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/lines_map.go#L27)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#NewLines "Go to NewLines")added in v0.11.0

func NewLines(lines map[[int64](https://pkg.go.dev/builtin#int64)][graph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph).[Line](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph#Line)) *[Lines](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#Lines)

NewLines returns a Lines initialized with the provided lines, a map of line IDs to graph.Lines. No check is made that the keys match the graph.Line IDs, and the map keys are not used.

Behavior of the Lines is unspecified if lines is mutated after the call to NewLines.

#### func (*Lines) [Len](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/lines_map.go#L32)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#Lines.Len "Go to Lines.Len")added in v0.11.0

func (l *[Lines](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#Lines)) Len() [int](https://pkg.go.dev/builtin#int)

Len returns the remaining number of lines to be iterated over.

#### func (*Lines) [Line](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/lines_map.go#L51)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#Lines.Line "Go to Lines.Line")added in v0.11.0

func (l *[Lines](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#Lines)) Line() [graph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph).[Line](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph#Line)

Line returns the current line of the iterator. Next must have been called prior to a call to Line.

#### func (*Lines) [LineSlice](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/lines_map.go#L65)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#Lines.LineSlice "Go to Lines.LineSlice")added in v0.11.0

func (l *[Lines](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#Lines)) LineSlice() [][graph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph).[Line](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph#Line)

LineSlice returns all the remaining lines in the iterator and advances the iterator. The order of lines within the returned slice is not specified.

#### func (*Lines) [Next](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/lines_map.go#L37)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#Lines.Next "Go to Lines.Next")added in v0.11.0

func (l *[Lines](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#Lines)) Next() [bool](https://pkg.go.dev/builtin#bool)

Next returns whether the next call of Line will return a valid line.

#### func (*Lines) [Reset](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/lines_map.go#L56)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#Lines.Reset "Go to Lines.Reset")added in v0.11.0

func (l *[Lines](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#Lines)) Reset()

Reset returns the iterator to its initial state.

#### type [Nodes](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/nodes_map.go#L14)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#Nodes "Go to Nodes")

type Nodes struct {
	// contains filtered or unexported fields
}

Nodes implements the graph.Nodes interfaces. The iteration order of Nodes is randomized.

#### func [NewNodes](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/nodes_map.go#L27)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#NewNodes "Go to NewNodes")

func NewNodes(nodes map[[int64](https://pkg.go.dev/builtin#int64)][graph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph#Node)) *[Nodes](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#Nodes)

NewNodes returns a Nodes initialized with the provided nodes, a map of node IDs to graph.Nodes. No check is made that the keys match the graph.Node IDs, and the map keys are not used.

Behavior of the Nodes is unspecified if nodes is mutated after the call to NewNodes.

#### func (*Nodes) [Len](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/nodes_map.go#L32)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#Nodes.Len "Go to Nodes.Len")

func (n *[Nodes](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#Nodes)) Len() [int](https://pkg.go.dev/builtin#int)

Len returns the remaining number of nodes to be iterated over.

#### func (*Nodes) [Next](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/nodes_map.go#L37)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#Nodes.Next "Go to Nodes.Next")

func (n *[Nodes](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#Nodes)) Next() [bool](https://pkg.go.dev/builtin#bool)

Next returns whether the next call of Node will return a valid node.

#### func (*Nodes) [Node](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/nodes_map.go#L51)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#Nodes.Node "Go to Nodes.Node")

func (n *[Nodes](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#Nodes)) Node() [graph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph#Node)

Node returns the current node of the iterator. Next must have been called prior to a call to Node.

#### func (*Nodes) [NodeSlice](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/nodes_map.go#L65)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#Nodes.NodeSlice "Go to Nodes.NodeSlice")added in v0.8.0

func (n *[Nodes](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#Nodes)) NodeSlice() [][graph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph#Node)

NodeSlice returns all the remaining nodes in the iterator and advances the iterator. The order of nodes within the returned slice is not specified.

#### func (*Nodes) [Reset](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/nodes_map.go#L56)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#Nodes.Reset "Go to Nodes.Reset")

func (n *[Nodes](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#Nodes)) Reset()

Reset returns the iterator to its initial state.

#### type [NodesByEdge](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/nodes_map.go#L79)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#NodesByEdge "Go to NodesByEdge")added in v0.8.0

type NodesByEdge struct {
	// contains filtered or unexported fields
}

NodesByEdge implements the graph.Nodes interfaces. The iteration order of Nodes is randomized.

#### func [NewNodesByEdge](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/nodes_map.go#L96)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#NewNodesByEdge "Go to NewNodesByEdge")added in v0.8.0

func NewNodesByEdge(nodes map[[int64](https://pkg.go.dev/builtin#int64)][graph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph#Node), edges map[[int64](https://pkg.go.dev/builtin#int64)][graph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph).[Edge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph#Edge)) *[NodesByEdge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#NodesByEdge)

NewNodesByEdge returns a NodesByEdge initialized with the provided nodes, a map of node IDs to graph.Nodes, and the set of edges, a map of to-node IDs to graph.Edge, that can be traversed to reach the nodes that the NodesByEdge will iterate over. No check is made that the keys match the graph.Node IDs, and the map keys are not used.

Behavior of the NodesByEdge is unspecified if nodes or edges is mutated after the call to NewNodes.

#### func [NewNodesByLines](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/nodes_map.go#L122)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#NewNodesByLines "Go to NewNodesByLines")added in v0.8.0

func NewNodesByLines(nodes map[[int64](https://pkg.go.dev/builtin#int64)][graph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph#Node), lines map[[int64](https://pkg.go.dev/builtin#int64)]map[[int64](https://pkg.go.dev/builtin#int64)][graph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph).[Line](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph#Line)) *[NodesByEdge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#NodesByEdge)

NewNodesByLines returns a NodesByEdge initialized with the provided nodes, a map of node IDs to graph.Nodes, and the set of lines, a map to-node IDs to map of graph.Line, that can be traversed to reach the nodes that the NodesByEdge will iterate over. No check is made that the keys match the graph.Node IDs, and the map keys are not used.

Behavior of the NodesByEdge is unspecified if nodes or lines is mutated after the call to NewNodes.

#### func [NewNodesByWeightedEdge](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/nodes_map.go#L109)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#NewNodesByWeightedEdge "Go to NewNodesByWeightedEdge")added in v0.8.0

func NewNodesByWeightedEdge(nodes map[[int64](https://pkg.go.dev/builtin#int64)][graph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph#Node), edges map[[int64](https://pkg.go.dev/builtin#int64)][graph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph).[WeightedEdge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph#WeightedEdge)) *[NodesByEdge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#NodesByEdge)

NewNodesByWeightedEdge returns a NodesByEdge initialized with the provided nodes, a map of node IDs to graph.Nodes, and the set of edges, a map of to-node IDs to graph.WeightedEdge, that can be traversed to reach the nodes that the NodesByEdge will iterate over. No check is made that the keys match the graph.Node IDs, and the map keys are not used.

Behavior of the NodesByEdge is unspecified if nodes or edges is mutated after the call to NewNodes.

#### func [NewNodesByWeightedLines](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/nodes_map.go#L135)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#NewNodesByWeightedLines "Go to NewNodesByWeightedLines")added in v0.8.0

func NewNodesByWeightedLines(nodes map[[int64](https://pkg.go.dev/builtin#int64)][graph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph#Node), lines map[[int64](https://pkg.go.dev/builtin#int64)]map[[int64](https://pkg.go.dev/builtin#int64)][graph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph).[WeightedLine](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph#WeightedLine)) *[NodesByEdge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#NodesByEdge)

NewNodesByWeightedLines returns a NodesByEdge initialized with the provided nodes, a map of node IDs to graph.Nodes, and the set of lines, a map to-node IDs to map of graph.WeightedLine, that can be traversed to reach the nodes that the NodesByEdge will iterate over. No check is made that the keys match the graph.Node IDs, and the map keys are not used.

Behavior of the NodesByEdge is unspecified if nodes or lines is mutated after the call to NewNodes.

#### func (*NodesByEdge) [Len](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/nodes_map.go#L140)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#NodesByEdge.Len "Go to NodesByEdge.Len")added in v0.8.0

func (n *[NodesByEdge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#NodesByEdge)) Len() [int](https://pkg.go.dev/builtin#int)

Len returns the remaining number of nodes to be iterated over.

#### func (*NodesByEdge) [Next](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/nodes_map.go#L145)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#NodesByEdge.Next "Go to NodesByEdge.Next")added in v0.8.0

func (n *[NodesByEdge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#NodesByEdge)) Next() [bool](https://pkg.go.dev/builtin#bool)

Next returns whether the next call of Node will return a valid node.

#### func (*NodesByEdge) [Node](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/nodes_map.go#L159)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#NodesByEdge.Node "Go to NodesByEdge.Node")added in v0.8.0

func (n *[NodesByEdge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#NodesByEdge)) Node() [graph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph#Node)

Node returns the current node of the iterator. Next must have been called prior to a call to Node.

#### func (*NodesByEdge) [NodeSlice](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/nodes_map.go#L173)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#NodesByEdge.NodeSlice "Go to NodesByEdge.NodeSlice")added in v0.8.0

func (n *[NodesByEdge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#NodesByEdge)) NodeSlice() [][graph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph#Node)

NodeSlice returns all the remaining nodes in the iterator and advances the iterator. The order of nodes within the returned slice is not specified.

#### func (*NodesByEdge) [Reset](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/nodes_map.go#L164)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#NodesByEdge.Reset "Go to NodesByEdge.Reset")added in v0.8.0

func (n *[NodesByEdge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#NodesByEdge)) Reset()

Reset returns the iterator to its initial state.

#### type [OrderedEdges](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/edges.go#L12)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedEdges "Go to OrderedEdges")

type OrderedEdges struct {
	// contains filtered or unexported fields
}

OrderedEdges implements the graph.Edges and graph.EdgeSlicer interfaces. The iteration order of OrderedEdges is the order of edges passed to NewEdgeIterator.

#### func [NewOrderedEdges](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/edges.go#L18)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#NewOrderedEdges "Go to NewOrderedEdges")

func NewOrderedEdges(edges [][graph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph).[Edge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph#Edge)) *[OrderedEdges](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedEdges)

NewOrderedEdges returns an OrderedEdges initialized with the provided edges.

#### func (*OrderedEdges) [Edge](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/edges.go#L45)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedEdges.Edge "Go to OrderedEdges.Edge")

func (e *[OrderedEdges](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedEdges)) Edge() [graph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph).[Edge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph#Edge)

Edge returns the current edge of the iterator. Next must have been called prior to a call to Edge.

#### func (*OrderedEdges) [EdgeSlice](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/edges.go#L54)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedEdges.EdgeSlice "Go to OrderedEdges.EdgeSlice")

func (e *[OrderedEdges](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedEdges)) EdgeSlice() [][graph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph).[Edge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph#Edge)

EdgeSlice returns all the remaining edges in the iterator and advances the iterator.

#### func (*OrderedEdges) [Len](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/edges.go#L23)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedEdges.Len "Go to OrderedEdges.Len")

func (e *[OrderedEdges](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedEdges)) Len() [int](https://pkg.go.dev/builtin#int)

Len returns the remaining number of edges to be iterated over.

#### func (*OrderedEdges) [Next](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/edges.go#L34)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedEdges.Next "Go to OrderedEdges.Next")

func (e *[OrderedEdges](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedEdges)) Next() [bool](https://pkg.go.dev/builtin#bool)

Next returns whether the next call of Edge will return a valid edge.

#### func (*OrderedEdges) [Reset](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/edges.go#L67)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedEdges.Reset "Go to OrderedEdges.Reset")

func (e *[OrderedEdges](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedEdges)) Reset()

Reset returns the iterator to its initial state.

#### type [OrderedLines](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/lines.go#L12)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedLines "Go to OrderedLines")

type OrderedLines struct {
	// contains filtered or unexported fields
}

OrderedLines implements the graph.Lines and graph.LineSlicer interfaces. The iteration order of OrderedLines is the order of lines passed to NewLineIterator.

#### func [NewOrderedLines](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/lines.go#L18)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#NewOrderedLines "Go to NewOrderedLines")

func NewOrderedLines(lines [][graph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph).[Line](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph#Line)) *[OrderedLines](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedLines)

NewOrderedLines returns an OrderedLines initialized with the provided lines.

#### func (*OrderedLines) [Len](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/lines.go#L23)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedLines.Len "Go to OrderedLines.Len")

func (e *[OrderedLines](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedLines)) Len() [int](https://pkg.go.dev/builtin#int)

Len returns the remaining number of lines to be iterated over.

#### func (*OrderedLines) [Line](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/lines.go#L45)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedLines.Line "Go to OrderedLines.Line")

func (e *[OrderedLines](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedLines)) Line() [graph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph).[Line](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph#Line)

Line returns the current line of the iterator. Next must have been called prior to a call to Line.

#### func (*OrderedLines) [LineSlice](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/lines.go#L54)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedLines.LineSlice "Go to OrderedLines.LineSlice")

func (e *[OrderedLines](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedLines)) LineSlice() [][graph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph).[Line](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph#Line)

LineSlice returns all the remaining lines in the iterator and advances the iterator.

#### func (*OrderedLines) [Next](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/lines.go#L34)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedLines.Next "Go to OrderedLines.Next")

func (e *[OrderedLines](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedLines)) Next() [bool](https://pkg.go.dev/builtin#bool)

Next returns whether the next call of Line will return a valid line.

#### func (*OrderedLines) [Reset](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/lines.go#L67)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedLines.Reset "Go to OrderedLines.Reset")

func (e *[OrderedLines](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedLines)) Reset()

Reset returns the iterator to its initial state.

#### type [OrderedNodes](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/nodes.go#L12)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedNodes "Go to OrderedNodes")

type OrderedNodes struct {
	// contains filtered or unexported fields
}

OrderedNodes implements the graph.Nodes and graph.NodeSlicer interfaces. The iteration order of OrderedNodes is the order of nodes passed to NewNodeIterator.

#### func [NewOrderedNodes](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/nodes.go#L18)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#NewOrderedNodes "Go to NewOrderedNodes")

func NewOrderedNodes(nodes [][graph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph#Node)) *[OrderedNodes](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedNodes)

NewOrderedNodes returns a OrderedNodes initialized with the provided nodes.

#### func (*OrderedNodes) [Len](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/nodes.go#L23)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedNodes.Len "Go to OrderedNodes.Len")

func (n *[OrderedNodes](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedNodes)) Len() [int](https://pkg.go.dev/builtin#int)

Len returns the remaining number of nodes to be iterated over.

#### func (*OrderedNodes) [Next](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/nodes.go#L31)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedNodes.Next "Go to OrderedNodes.Next")

func (n *[OrderedNodes](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedNodes)) Next() [bool](https://pkg.go.dev/builtin#bool)

Next returns whether the next call of Node will return a valid node.

#### func (*OrderedNodes) [Node](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/nodes.go#L42)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedNodes.Node "Go to OrderedNodes.Node")

func (n *[OrderedNodes](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedNodes)) Node() [graph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph#Node)

Node returns the current node of the iterator. Next must have been called prior to a call to Node.

#### func (*OrderedNodes) [NodeSlice](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/nodes.go#L51)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedNodes.NodeSlice "Go to OrderedNodes.NodeSlice")

func (n *[OrderedNodes](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedNodes)) NodeSlice() [][graph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph).[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph#Node)

NodeSlice returns all the remaining nodes in the iterator and advances the iterator.

#### func (*OrderedNodes) [Reset](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/nodes.go#L61)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedNodes.Reset "Go to OrderedNodes.Reset")

func (n *[OrderedNodes](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedNodes)) Reset()

Reset returns the iterator to its initial state.

#### type [OrderedWeightedEdges](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/edges.go#L74)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedWeightedEdges "Go to OrderedWeightedEdges")

type OrderedWeightedEdges struct {
	// contains filtered or unexported fields
}

OrderedWeightedEdges implements the graph.Edges and graph.EdgeSlicer interfaces. The iteration order of OrderedWeightedEdges is the order of edges passed to NewEdgeIterator.

#### func [NewOrderedWeightedEdges](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/edges.go#L80)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#NewOrderedWeightedEdges "Go to NewOrderedWeightedEdges")

func NewOrderedWeightedEdges(edges [][graph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph).[WeightedEdge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph#WeightedEdge)) *[OrderedWeightedEdges](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedWeightedEdges)

NewOrderedWeightedEdges returns an OrderedWeightedEdges initialized with the provided edges.

#### func (*OrderedWeightedEdges) [Len](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/edges.go#L85)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedWeightedEdges.Len "Go to OrderedWeightedEdges.Len")

func (e *[OrderedWeightedEdges](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedWeightedEdges)) Len() [int](https://pkg.go.dev/builtin#int)

Len returns the remaining number of edges to be iterated over.

#### func (*OrderedWeightedEdges) [Next](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/edges.go#L96)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedWeightedEdges.Next "Go to OrderedWeightedEdges.Next")

func (e *[OrderedWeightedEdges](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedWeightedEdges)) Next() [bool](https://pkg.go.dev/builtin#bool)

Next returns whether the next call of WeightedEdge will return a valid edge.

#### func (*OrderedWeightedEdges) [Reset](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/edges.go#L129)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedWeightedEdges.Reset "Go to OrderedWeightedEdges.Reset")

func (e *[OrderedWeightedEdges](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedWeightedEdges)) Reset()

Reset returns the iterator to its initial state.

#### func (*OrderedWeightedEdges) [WeightedEdge](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/edges.go#L107)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedWeightedEdges.WeightedEdge "Go to OrderedWeightedEdges.WeightedEdge")

func (e *[OrderedWeightedEdges](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedWeightedEdges)) WeightedEdge() [graph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph).[WeightedEdge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph#WeightedEdge)

WeightedEdge returns the current edge of the iterator. Next must have been called prior to a call to WeightedEdge.

#### func (*OrderedWeightedEdges) [WeightedEdgeSlice](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/edges.go#L116)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedWeightedEdges.WeightedEdgeSlice "Go to OrderedWeightedEdges.WeightedEdgeSlice")

func (e *[OrderedWeightedEdges](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedWeightedEdges)) WeightedEdgeSlice() [][graph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph).[WeightedEdge](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph#WeightedEdge)

WeightedEdgeSlice returns all the remaining edges in the iterator and advances the iterator.

#### type [OrderedWeightedLines](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/lines.go#L74)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedWeightedLines "Go to OrderedWeightedLines")

type OrderedWeightedLines struct {
	// contains filtered or unexported fields
}

OrderedWeightedLines implements the graph.Lines and graph.LineSlicer interfaces. The iteration order of OrderedWeightedLines is the order of lines passed to NewLineIterator.

#### func [NewOrderedWeightedLines](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/lines.go#L80)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#NewOrderedWeightedLines "Go to NewOrderedWeightedLines")

func NewOrderedWeightedLines(lines [][graph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph).[WeightedLine](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph#WeightedLine)) *[OrderedWeightedLines](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedWeightedLines)

NewOrderedWeightedLines returns an OrderedWeightedLines initialized with the provided lines.

#### func (*OrderedWeightedLines) [Len](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/lines.go#L85)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedWeightedLines.Len "Go to OrderedWeightedLines.Len")

func (e *[OrderedWeightedLines](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedWeightedLines)) Len() [int](https://pkg.go.dev/builtin#int)

Len returns the remaining number of lines to be iterated over.

#### func (*OrderedWeightedLines) [Next](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/lines.go#L96)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedWeightedLines.Next "Go to OrderedWeightedLines.Next")

func (e *[OrderedWeightedLines](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedWeightedLines)) Next() [bool](https://pkg.go.dev/builtin#bool)

Next returns whether the next call of WeightedLine will return a valid line.

#### func (*OrderedWeightedLines) [Reset](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/lines.go#L129)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedWeightedLines.Reset "Go to OrderedWeightedLines.Reset")

func (e *[OrderedWeightedLines](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedWeightedLines)) Reset()

Reset returns the iterator to its initial state.

#### func (*OrderedWeightedLines) [WeightedLine](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/lines.go#L107)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedWeightedLines.WeightedLine "Go to OrderedWeightedLines.WeightedLine")

func (e *[OrderedWeightedLines](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedWeightedLines)) WeightedLine() [graph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph).[WeightedLine](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph#WeightedLine)

WeightedLine returns the current line of the iterator. Next must have been called prior to a call to WeightedLine.

#### func (*OrderedWeightedLines) [WeightedLineSlice](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/lines.go#L116)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedWeightedLines.WeightedLineSlice "Go to OrderedWeightedLines.WeightedLineSlice")

func (e *[OrderedWeightedLines](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#OrderedWeightedLines)) WeightedLineSlice() [][graph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph).[WeightedLine](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph#WeightedLine)

WeightedLineSlice returns all the remaining lines in the iterator and advances the iterator.

#### type [WeightedLines](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/lines_map.go#L79)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#WeightedLines "Go to WeightedLines")added in v0.11.0

type WeightedLines struct {
	// contains filtered or unexported fields
}

WeightedLines implements the graph.WeightedLines interfaces. The iteration order of WeightedLines is randomized.

#### func [NewWeightedLines](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/lines_map.go#L92)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#NewWeightedLines "Go to NewWeightedLines")added in v0.11.0

func NewWeightedLines(lines map[[int64](https://pkg.go.dev/builtin#int64)][graph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph).[WeightedLine](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph#WeightedLine)) *[WeightedLines](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#WeightedLines)

NewWeightedLines returns a WeightedLines initialized with the provided lines, a map of line IDs to graph.WeightedLines. No check is made that the keys match the graph.WeightedLine IDs, and the map keys are not used.

Behavior of the WeightedLines is unspecified if lines is mutated after the call to NewWeightedLines.

#### func (*WeightedLines) [Len](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/lines_map.go#L97)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#WeightedLines.Len "Go to WeightedLines.Len")added in v0.11.0

func (l *[WeightedLines](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#WeightedLines)) Len() [int](https://pkg.go.dev/builtin#int)

Len returns the remaining number of lines to be iterated over.

#### func (*WeightedLines) [Next](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/lines_map.go#L102)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#WeightedLines.Next "Go to WeightedLines.Next")added in v0.11.0

func (l *[WeightedLines](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#WeightedLines)) Next() [bool](https://pkg.go.dev/builtin#bool)

Next returns whether the next call of Line will return a valid line.

#### func (*WeightedLines) [Reset](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/lines_map.go#L121)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#WeightedLines.Reset "Go to WeightedLines.Reset")added in v0.11.0

func (l *[WeightedLines](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#WeightedLines)) Reset()

Reset returns the iterator to its initial state.

#### func (*WeightedLines) [WeightedLine](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/lines_map.go#L116)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#WeightedLines.WeightedLine "Go to WeightedLines.WeightedLine")added in v0.11.0

func (l *[WeightedLines](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#WeightedLines)) WeightedLine() [graph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph).[WeightedLine](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph#WeightedLine)

WeightedLine returns the current line of the iterator. Next must have been called prior to a call to WeightedLine.

#### func (*WeightedLines) [WeightedLineSlice](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/lines_map.go#L130)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#WeightedLines.WeightedLineSlice "Go to WeightedLines.WeightedLineSlice")added in v0.11.0

func (l *[WeightedLines](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#WeightedLines)) WeightedLineSlice() [][graph](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph).[WeightedLine](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph#WeightedLine)

WeightedLineSlice returns all the remaining lines in the iterator and advances the iterator. The order of lines within the returned slice is not specified.

![Image 44](https://pkg.go.dev/static/shared/icon/insert_drive_file_gm_grey_24dp.svg) Source Files [¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/graph/iterator#section-sourcefiles "Go to Source Files")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[View all Source files](https://github.com/gonum/gonum/tree/v0.17.0/graph/iterator)

*   [doc.go](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/doc.go "doc.go")
*   [edges.go](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/edges.go "edges.go")
*   [hiter_swiss.go](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/hiter_swiss.go "hiter_swiss.go")
*   [lines.go](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/lines.go "lines.go")
*   [lines_map.go](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/lines_map.go "lines_map.go")
*   [map.go](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/map.go "map.go")
*   [nodes.go](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/nodes.go "nodes.go")
*   [nodes_map.go](https://github.com/gonum/gonum/blob/v0.17.0/graph/iterator/nodes_map.go "nodes_map.go")

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
