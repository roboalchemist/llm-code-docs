# Source: https://networkx.github.io/documentation/networkx-0.99

Title: Overview — NetworkX v0.99 documentation

URL Source: https://networkx.github.io/documentation/networkx-0.99

Markdown Content:
> _This documentation is currently being updated for release 0.99 of NetworkX. This update includes significant changes to the underlying Graph and DiGraph objects to reflect our common use case of weighted graphs and to improve performance. See the [API changes](https://networkx.org/documentation/networkx-0.99/reference/api\_changes.html) for detailed information._

High productivity software for complex networks
-----------------------------------------------

![Image 1: NetworkX art](https://networkx.org/documentation/networkx-0.99/_static/art1.png)

> NetworkX is a Python package for the creation, manipulation, and study of the structure, dynamics, and functions of complex networks.

Quick Example
-------------

> >>> import networkx as nx
> >>> G=nx.Graph()
> >>> G.add_edge(1,2)
> >>> G.add_node("spam")
> >>> print G.nodes()
> [1, 2, 'spam']
> >>> print G.edges()
> [(1, 2)]

[Tutorial](https://networkx.org/documentation/networkx-0.99/tutorial/index.html)

start here

[Reference](https://networkx.org/documentation/networkx-0.99/reference/index.html)

guide to all functions and classes

[Examples](https://networkx.org/documentation/networkx-0.99/examples/index.html)

using the library

[Gallery](https://networkx.org/documentation/networkx-0.99/gallery.html)

network drawings[Contents](https://networkx.org/documentation/networkx-0.99/contents.html)

a complete overview

[Search Page](https://networkx.org/documentation/networkx-0.99/search.html)

search the documentation

[General Index](https://networkx.org/documentation/networkx-0.99/genindex.html)

all functions, classes, terms

[Module Index](https://networkx.org/documentation/networkx-0.99/modindex.html)

quick access to all documented modules

Features:
---------

> *   Includes standard graph-theoretic and statistical physics functions
> *   Easy exchange of network algorithms between applications, disciplines, and platforms
> *   Includes many classic graphs and synthetic networks
> *   Nodes and edges can be "anything" (e.g. time-series, text, images, XML records)
> *   Exploits existing code from high-quality legacy software in C, C++, Fortran, etc.
> *   Open source (encourages community input)
> *   Unit-tested
> 
> 
> Additional benefits due to Python:
> 
> 
> *   Allows fast prototyping of new algorithms
> *   Easy to teach
> *   Multi-platform
> *   Allows easy access to almost any database

Get NetworkX
------------

> NetworkX is available as an [easy-install](http://peak.telecommunity.com/DevCenter/EasyInstall)able package on the [Python Package Index](http://pypi.python.org/pypi/networkx).
> 
> 
> The code can be found on the NetworkX SVN server at [http://networkx.lanl.gov/svn/networkx/trunk](http://networkx.lanl.gov/svn/networkx/trunk).
