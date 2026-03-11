# GraphML Schema Documentation

---
| Â [Home](/index.html)Â  | Â [Download](/download.html)Â  | Â [Specification](/specification.html)Â  | Â [About](/about.html)Â |
---|---|---|---
![](/images/void.gif)
| Links:
---
File Format Links
**[GXL](http://www.gupro.de/GXL/)** \-  an XML-based graph exchange format developed for software
re-engineering.

**[GML](http://www.fmi.uni-passau.de/Graphlet/GML/)** \-  a widely used graph exchange format (non-
XML).

**[XGMML](http://www.cs.rpi.edu/~puninj/XGMML/)** \-  an XML-based file format for graphs based on
GML.

**[SVG](http://www.w3.org/Graphics/SVG/)** \-  an XML-based graphics format.

Graph Drawing Links
**[graphdrawing.org](http://www.graphdrawing.org/)** \-  home of graph drawing

**[GD 2010](http://www.graphdrawing.org/gd2010/)** \-  18th Intl. Symp. Graph Drawing, 21-24 Sep
2010, Konstanz, Germany

XML Links
**[XML](http://www.w3.org/XML/)** \-  home of the E**x** tensible **M** arkup **L** anguage at the
[World Wide Web Consortium](http://www.w3.org/).

The schema corresponding to this document defines the structural layer of the Graph Markup Language
(GraphML). Although a DTD is provided, this schema is, together with its extensions
http://graphml.graphdrawing.org/xmlns/1.0/graphml-attributes.xsd and
http://graphml.graphdrawing.org/xmlns/1.0/graphml-parseinfo.xsd, the only normative reference.

## Contents

* desc
* locator
* data
* key
* default
* graphml
* graph
* node
* port
* edge
* hyperedge
* endpoint

The attribute groups <element_name>.extra.attrib may be used for adding user defined attributes to
the elements <element_name>. The attribute group common.extra.attrib may be used for adding user
defined attributes to all elements.  Complex type definitions for the GraphML structural layer
elements: <data>, <default>, <key>, <graphml>, <graph>, <node>, <port>, <edge>, <hyperedge>,
<endpoint> and <locator>. The names of the complex types are constructed corresponding to the
pattern element_name.type. (The only remaining GraphML structural layer element <desc> is of simple
type xs:string.)

### Element: desc

Description: Provides human-readable descriptions for the GraphML element containing this <desc> as
its first child. Occurence: <key>, <graphml>, <graph>, <node>, <port>, <edge>, <hyperedge>, and
<endpoint>.  back to the overview

### Element: locator

Description: Graphs and nodes are declared by the elements <graph> and <node>, respectively. The
optional <locator>-child of these elements point to their definition. (If there is no
<locator>-child the graphs/nodes are defined by their content). Occurence: <graph>, and <node>.

#### Type: locator.type

Complex type for the <locator> element. Content type: (empty)

#### Attributes:

**xlink:href** (required)

     points to the resource of this locator. 
**xlink:type**

     type of the hyperlink (fixed as simple).

#### locator.extra.attrib

user defined extra attributes for <locator> elements.

back to the overview

### Element: data

Description: In GraphML there may be data-functions attached to graphs, nodes, ports, edges,
hyperedges and endpoint and to the whole collection of graphs described by the content of <graphml>.
These functions are declared by <key> elements (children of <graphml>) and defined by <data>
elements. Occurence: <graphml>, <graph>, <node>, <port>, <edge>, <hyperedge>, and <endpoint>.

#### Type: data.type

Complex type for the <data> element. data.type is mixed, that is, <data> may contain #PCDATA.
Content type: extension of data-extension.type which is empty per default.

#### Identity Constraint Definitions:

#### data_data_key_unique

Ensures: uniqueness of the key attributes of <data> children of this <data> element.

back to the overview

### Element: key

Description: In GraphML there may be data-functions attached to graphs, nodes, ports, edges,
hyperedges and endpoint and to the whole collection of graphs described by the content of <graphml>.
These functions are declared by <key> elements (children of <graphml>) and defined by <data>
elements. Occurence: <graphml>.

#### Type: key.type

Complex type for the <key> element.

#### Attributes:

**id** (required) of type xs:NMTOKEN

    identifies this <key>. 
**for** of type key.for.type

     describes the domain of definition for the corresponding graph attribute.

#### Type: key.for.type

Simple type for the for attribute of <key>. key.for.type is a restriction of xs:NMTOKEN Allowed
values: all, graph, node, edge, hyperedge, port and endpoint.

#### key.extra.attrib

user defined extra attributes for <key> elements.

#### Contents:

desc?, default? back to the overview

### Element: default

Description: In GraphML there may be data-functions attached to graphs, nodes, ports, edges,
hyperedges and endpoint and to the whole collection of graphs described by the content of <graphml>.
These functions are declared by <key> elements (children of <graphml>) and defined by <data>
elements. The (optional) <default> child of <key> gives the default value for the corresponding
function. Occurence: <key>.

#### Type: default.type

Complex type for the <default> element. default.type is mixed, that is, data may contain #PCDATA.
Content type: extension of data-extension.type which is empty per default.  back to the overview

### Element: graphml

Description: <graphml> is the root element of each GraphML document. Occurence: root.

#### Type: graphml.type

Complex type for the <graphml> element.

#### Attributes:

#### graphml.extra.attrib

user defined extra attributes for <graphml> elements.

#### Contents:

desc?, key*, ( graph | data )*

#### Identity Constraint Definitions:

#### graphml_data_key_unique

Ensures: uniqueness of the key attributes of <data> children of this <graphml> element.

#### key_id_key

Ensures: existence and uniqueness of the id attributes of each <key> element in this document.

#### graph_id_unique

Ensures: uniqueness of the id attributes of each <graph> element in this document.

#### data_key_ref

_refers_ key_id_key

Ensures: for the key attribute of each <data> in this document, the existence of an id attribute of <key> which matches the value of it.

back to the overview

### Element: graph

Description: Describes one graph in this document. Occurence: <graphml>, <node>, <edge>,
<hyperedge>.

#### Type: graph.type

Complex type for the <graph> element.

#### Attributes:

**id** of type xs:NMTOKEN

     identifies this graph . 
**edgedefault** (required) of type graph.edgedefault.type

     describes whether edges of this graph are considered as directed or undirected per default (unless specified by the attribute directed of <edge>).

#### Type: graph.edgedefault.type

Simple type for the edgedefault attribute of <graph>. graph.edgedefault.type is a restriction of
xs:NMTOKEN Allowed values: directed, undirected.

#### graph.extra.attrib

user defined extra attributes for <graph> elements.

#### Contents:

desc?, ( ( data | node | edge | hyperedge )* | locator )

#### Identity Constraint Definitions:

#### graph_data_key_unique

Ensures: uniqueness of the key attributes of <data> children of this <graph> element.

#### node_id_key

Ensures: existence and uniqueness of the id attributes of each <node> element in this graph.

#### edge_id_unique

Ensures: uniqueness of the id attributes of each <edge> element in this graph.

#### hyperedge_id_unique

Ensures: uniqueness of the id attributes of each <hyperedge> element in this graph.

#### endpoint_id_unique

Ensures: uniqueness of the id attributes of each <endpoint> element in this graph.

#### edge_source_ref

_refers_ node_id_key

     Ensures: for the source attribute of each <edge> in this graph, the existence of an id attribute of <node> which matches the value of it. 
**edge_target_ref** _refers_ node_id_key

     Ensures: for the target attribute of each <edge> in this graph, the existence of an id attribute of <node> which matches the value of it. 
**endpoint_node_ref** _refers_ node_id_key

     Ensures: for the node attribute of each <endpoint> in this graph, the existence of an id attribute of <node> which matches the value of it. 
back to the overview

### Element: node

Description: Describes one node in the <graph> containing this <node>. Occurence: <graph>.

#### Type: node.type

Complex type for the <node> element.

#### Attributes:

**id** (required) of type xs:NMTOKEN

     identifies this node.

#### node.extra.attrib

user defined extra attributes for <node elements.

#### Contents:

desc?, ( ( data | port )*, graph? | locator )

#### Identity Constraint Definitions:

#### port_name_key

Ensures: existence and uniqueness of the name attributes of each <port> element within this <node>.

#### node_data_key_unique

Ensures: uniqueness of the key attributes of <data> children of this <node> element.

back to the overview

### Element: port

Description: Nodes may be structured by ports; thus edges are not only attached to a node but to a
certain port in this node. Occurence: <node>, <port>.

#### Type: port.type

Complex type for the <port> element.

#### Attributes:

**name** (required) of type xs:NMTOKEN

     identifies this port, within the node it is contained in.

#### port.extra.attrib

user defined extra attributes for <port> elements.

#### Contents:

desc?, ( data | port )*

#### Identity Constraint Definitions:

#### port_data_key_unique

Ensures: uniqueness of the key attributes of <data> children of this <port> element.

back to the overview

### Element: edge

Description: Describes an edge in the <graph> which contains this <edge>. Occurence: <graph>.

#### Type: edge.type

Complex type for the <edge> element.

#### Attributes:

**id** of type xs:NMTOKEN

     identifies this edge . 
**directed** of type xs:boolean

     overwrites the edgedefault attribute of <graph> . 
**source** (required) of type xs:NMTOKEN

     points to the id attribute of the source <node>. 
**target** (required) of type xs:NMTOKEN

     points to the id attribute of the target <node>. 
**sourceport** of type xs:NMTOKEN

     points to the name attribute of the source <port>. 
**targetport** of type xs:NMTOKEN

     points to the name attribute of the target <port>.

#### edge.extra.attrib

user defined extra attributes for <edge> elements.

#### Contents:

desc?, data*, graph?

#### Identity Constraint Definitions:

#### edge_data_key_unique

Ensures: uniqueness of the key attributes of <data> children of this <edge> element.

back to the overview

### Element: hyperedge

Description: While edges describe relations between two nodes, a hyperedge describes a relation
between an arbitrary number of nodes. Occurence: <graph>.

#### Type: hyperedge.type

Complex type for the <hyperedge> element.

#### Attributes:

**id** of type xs:NMTOKEN

     identifies this <hyperedge> .

#### hyperedge.extra.attrib

user defined extra attributes for <hyperedge> elements.

#### Contents:

desc?, ( data | endpoint )*, graph?

#### Identity Constraint Definitions:

#### hyperedge_data_key_unique

Ensures: uniqueness of the key attributes of <data> children of this <hyperedge> element.

back to the overview

### Element: endpoint

Description: The list of <endpoints> within a hyperedge points to the nodes contained in this
hyperedge. Occurence: <hyperedge>.

#### Type: endpoint.type

Complex type for the <endpoint> element.

#### Attributes:

**id** of type xs:NMTOKEN

     identifies this <endpoint> . 
**port** of type xs:NMTOKEN

     points to the name of the port, to which this endpoint is connected . 
**node** (required) of type xs:NMTOKEN

     points to the id of the node, to which this endpoint is connected. 
**type** of type endpoint.type.type

     defines the direction on this endpoint (undirected per default).

#### Type: endpoint.type.type

Simple type for the type attribute of <endpoint>. endpoint.type.type is a restriction of xs:NMTOKEN
Allowed values: in, out, undir.

#### endpoint.extra.attrib

user defined extra attributes for <endpoint> elements.

#### Contents:

desc?

back to the overview

## News

| Date | Event |
|------|-------|
| 05 April 2007 | Licensing status clarified: GraphML is free for everyone. |
| 22 February 2007 | GraphML 1.0 schema inclusion altered to avoid problems with some parsers. |
| 03 August 2004 | LEDA extension package for GraphML (release candidate). Download [graphml_lep.zip](/download/graphml_lep.zip) |
| 01 June 2004 | [GraphML Primer](/primer/graphml-primer.html) released. |
| 18 March 2003 | XML Schema specification and documentation available for GraphML 1.0rc (release candidate) |
| 23 July 2002 | GraphML presentation at the [annual meeting](http://www.dfg-schwerpunkt-1126.de/veranstaltungen/jk2002.php) of DFG Research Priority 1126 [Algorithmic Aspects of Large and Complex Networks](http://www.dfg-schwerpunkt-1126.de/). ([ps](/publications/dfg02.ps), [pdf](/publications/dfg02.pdf)) |
| 28 June 2002 | [yFiles](http://www.yworks.de/en/products_yfiles_ep_graphml.htm) extension package for GraphML version 1.0 released. |
| 22 May 2002 | Release candidates for extensions _graphml-attributes_ (for data attributes) and _graphml-parseinfo_ (for lightweight parsers) completed. See current [specification](/specification.html). |
| 12 March 2002 | GraphML proposed as the standard format for the network data archive to be created within EU FET Open Project [COSIN](http://www.cosin.org). |

![](/images/void.gif)

---

[![Valid HTML 4.01!](http://www.w3.org/Icons/valid-html401)](http://validator.w3.org/check?uri=referer)

Copyright 2001-2007 GraphML Working Group

Last update: Monday, 18-Feb-2019 15:41:00 CET
