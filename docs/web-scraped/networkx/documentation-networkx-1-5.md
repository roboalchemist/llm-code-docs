# Source: https://networkx.github.io/documentation/networkx-1.5

Title: Overview — NetworkX v1.5 documentation

URL Source: https://networkx.github.io/documentation/networkx-1.5

Markdown Content:
High productivity software for complex networks
-----------------------------------------------

> NetworkX is a Python package for the creation, manipulation, and study of the structure, dynamics, and functions of complex networks.

Quick Example
-------------

>>> import networkx as nx

>>> G=nx.Graph()
>>> G.add_node("spam")
>>> G.add_edge(1,2)
>>> print(G.nodes())
[1, 2, 'spam']
>>> print(G.edges())
[(1, 2)]![Image 1: NetworkX art](https://networkx.org/documentation/networkx-1.5/_static/art1.png)

[Tutorial](https://networkx.org/documentation/networkx-1.5/tutorial/index.html)

start here

[Reference](https://networkx.org/documentation/networkx-1.5/reference/index.html)

guide to all functions and classes

[Examples](https://networkx.org/documentation/networkx-1.5/examples/index.html)

using the library

[Gallery](https://networkx.org/documentation/networkx-1.5/gallery.html)

network drawings[Contents](https://networkx.org/documentation/networkx-1.5/contents.html)

a complete overview

[Search Page](https://networkx.org/documentation/networkx-1.5/search.html)

search the documentation

[General Index](https://networkx.org/documentation/networkx-1.5/genindex.html)

all functions, classes, terms

[Module Index](https://networkx.org/documentation/networkx-1.5/modindex.html)

quick access to all documented modules

Features
--------

*    Standard graph-theoretic and statistical physics functions
*   Easy exchange of network algorithms between applications, disciplines, and platforms
*    Many classic graphs and synthetic networks
*    Nodes and edges can be "anything" (e.g. time-series, text, images, XML records)
*   Exploits existing code from high-quality legacy software in C, C++, Fortran, etc.
*   Open source [BSD license](https://networkx.org/documentation/networkx-1.5/reference/legal.html)
*   More than 1000 unit tests

_Additional benefits from Python_

*   Fast prototyping of new algorithms
*   Easy to teach
*   Multi-platform
*   Allows easy access to almost any database
