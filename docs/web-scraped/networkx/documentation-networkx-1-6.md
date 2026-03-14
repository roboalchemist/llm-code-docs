# Source: https://networkx.github.io/documentation/networkx-1.6

Title: Overview — NetworkX 1.6 documentation

URL Source: https://networkx.github.io/documentation/networkx-1.6

Markdown Content:
High productivity software for complex networks
-----------------------------------------------

> NetworkX is a Python language software package for the creation, manipulation, and study of the structure, dynamics, and functions of complex networks.

Quick Example
-------------

>>> import networkx as nx

>>> G=nx.Graph()
>>> G.add_node("spam")
>>> G.add_edge(1,2)
>>> print(G.nodes())
[1, 2, 'spam']
>>> print(G.edges())
[(1, 2)]

[Overview](https://networkx.org/documentation/networkx-1.6/overview.html)

the big picture

[Tutorial](https://networkx.org/documentation/networkx-1.6/tutorial/index.html)

get started here

[Reference](https://networkx.org/documentation/networkx-1.6/reference/index.html)

guide to all functions and classes[Contents](https://networkx.org/documentation/networkx-1.6/contents.html)

all documentation

[Examples](https://networkx.org/documentation/networkx-1.6/examples/index.html)

using the library

[Gallery](https://networkx.org/documentation/networkx-1.6/gallery.html)

network drawings

Features
--------

*    Python language data structures for graphs, digraphs, and multigraphs. 
*    Nodes can be "anything" (e.g. text, images, XML records)
*    Edges can hold arbitrary data (e.g. weights, time-series) 
*    Generators for classic graphs, random graphs, and synthetic networks
*    Standard graph algorithms
*    Network structure and analysis measures
*    Basic graph drawing
*    Open source [BSD license](https://networkx.org/documentation/networkx-1.6/reference/legal.html)
*    Well tested: more than 1500 unit tests
*    Additional benefits from Python: fast prototyping, easy to teach, multi-platform
