# GraphML Specification  
  
---  
|  [Home](/index.html)  |  [Download](/download.html)  |  [Specification](/specification.html)  |  [About](/about.html)   
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
  
  
  

##

**The GraphML DTD version 1.0rc (release candidate) is located
at<http://graphml.graphdrawing.org/dtds/1.0rc/graphml.dtd> **

## Structural View

The following DTD version of the specification is provided to communicate the basic design of the
structural layer. See the following paper for more detailed explanations:  U. Brandes, M.
Eiglsperger, I. Herman, M. Himsolt, and M.S. Marshall:  
[GraphML Progress Report: Structural Layer Proposal](http://www.inf.uni-
konstanz.de/~brandes/publications/behhm-gprsl-01.pdf).  
_Proc. 9th Intl. Symp. Graph Drawing (GD  "'01), LNCS 2265, pp. 501-512.  
(C) Springer-Verlag, 2002. _ | ![](/images/void.gif)| ![](/images/void.gif)| ![](/images/void.gif)  
---|---|---  
![](/images/void.gif)|

    
    
    [graphml](dtd.html#graphml)
        [desc](dtd.html#desc)
        [key](dtd.html#key)
            [desc](dtd.html#desc)
        [data](dtd.html#data)
        [graph](dtd.html#graph)
            [desc](dtd.html#desc)
            [data](dtd.html#data)
            [node](dtd.html#node)
                [desc](dtd.html#desc)
                [data](dtd.html#data)
                [port](dtd.html#port)
                [graph](dtd.html#graph)
            [edge](dtd.html#edge)
                [desc](dtd.html#desc)
                [data](dtd.html#data)
                [graph](dtd.html#graph)
            [hyperedge](dtd.html#hyperedge)
                [desc](dtd.html#desc)
                [data](dtd.html#data)
                [endpoint](dtd.html#endpoint)
                    [desc](dtd.html#desc)
                [graph](dtd.html#graph)
            [locator](dtd.html#locator)
    
    

| ![](/images/void.gif)  
![](/images/void.gif)| ![](/images/void.gif)| ![](/images/void.gif)  
  
## Descriptions

### data

#### DTD Definition

![](/images/void.gif)| ![](/images/void.gif)| ![](/images/void.gif)  
---|---|---  
![](/images/void.gif)|

    
    
    <!ELEMENT data  (#PCDATA)>
    <!ATTLIST data 
              key      IDREF        #REQUIRED
              id       ID           #IMPLIED
    >
    

| ![](/images/void.gif)  
![](/images/void.gif)| ![](/images/void.gif)| ![](/images/void.gif)  
  
#### Contents

Anything, including further _data_ elements.

#### Attributes

_key_ (required)

    The key specifies the kind of data entered here. The value of _key_ must be the id of one of the [_key_](dtd.html#key) elements of [_graphml_](dtd.html#graphml).
_id_ (optional)

    An optional id for the data.
[back to the structural view](dtd.html#top)  
---  
  
### desc

The idea behind the _desc_ element is that applications writing GraphML documents are encouraged to
describe the content of elements. Therefore, each element has an optional _desc_ element as its
first child.

#### DTD Definition

![](/images/void.gif)| ![](/images/void.gif)| ![](/images/void.gif)  
---|---|---  
![](/images/void.gif)|

    
    
    <!ELEMENT desc (#PCDATA)>
    

| ![](/images/void.gif)  
![](/images/void.gif)| ![](/images/void.gif)| ![](/images/void.gif)  
  
#### Contents

_desc_ elements should contain meta information useful for human readers of a graphml document. For
example, they may contain a specification of the level of sophistication of the contained graph.
Another example would be a brief description of the data associated with a particular key.

#### Attributes

None

#### Examples

![](/images/void.gif)| ![](/images/void.gif)| ![](/images/void.gif)  
---|---|---  
![](/images/void.gif)|

    
    
    <graphml>
     <desc>This graph intentionally kept blank.</desc>
    </graphml>
    

| ![](/images/void.gif)  
![](/images/void.gif)| ![](/images/void.gif)| ![](/images/void.gif)  
  
[back to the structural view](dtd.html#top)  
---  
  
### edge

Edges are incident to a source and a target node. Their precise attachment may be specified via the
optional _sourcePort_ and _targetPort_ attributes.

#### DTD Definition

![](/images/void.gif)| ![](/images/void.gif)| ![](/images/void.gif)  
---|---|---  
![](/images/void.gif)|

    
    
    <!ELEMENT edge (desc?,data*,graph?)>
    <!ATTLIST edge 
              id         ID           #IMPLIED
              source     IDREF        #REQUIRED
              sourceport NMTOKEN      #IMPLIED
              target     IDREF        #REQUIRED
              targetport NMTOKEN      #IMPLIED
              directed   (true|false) #IMPLIED
    >
    

| ![](/images/void.gif)  
![](/images/void.gif)| ![](/images/void.gif)| ![](/images/void.gif)  
  
#### Contents

An _edge_ element may contain

[_desc_](dtd.html#desc) (Optional)

    A human readable description of the edge. This must be the first element in the list.
[_data_](dtd.html#data) (Optional)

    Application specific data for the edge. There may be any number of such elements, but they must come after the description and before the subgraphs.
[_graph_](dtd.html#graph) (Optional)

    Like nodes, edges may also contain a graph. For example, the decomposition tree of a series-parallel graph is best described as graphs within edges.

#### Attributes

Edges may have the following attributes:

_id_

     _Optional_ _id_ tag for the edge.
_source_

    Specifies the source node of this edge. The value of _source_ must be a valid node _id_.
_sourcePort_

    Specifies the source port of this edge. The value of _sourcePort_ must match the value of the _name_ attribute of a port of the source node of this edge.
_target_

    Specifies the target node of this edge. The value of _target_ must be a valid node _id_.
_targetPort_

    Specifies the target port of this edge. The value of _targetPort_ must match the value of the _name_ attribute of a port of the target node of this edge.
directed

    Whether an edge is directed is determined by the _directed_ attribute of the surrounding _graph_ element, unless it is explicitly overwritten by the edge's own _directed_ attribute.

#### Remarks

_In the corresponding Schemas definition,_graph_ , _node_ , and _edge_ _id_ "s are distinguished as
different types, so as to ensure that edges attach to nodes, etc. With DTD-validated documents, a
parser encounter edges omething other than a node as source or target, so that an exception should
be thrown. _

[back to the structural view](dtd.html#top)  
---  
  
### endpoint

The end points of nodes and edges are specified with the _source_ and _target_ attributes.
Hyperedges, however, can have any number of end points, so XML attributes are no longer appropriate.
Instead, the _hyperedge_ element contains a number of _endpoint_ elements.

#### DTD Definition

![](/images/void.gif)| ![](/images/void.gif)| ![](/images/void.gif)  
---|---|---  
![](/images/void.gif)|

    
    
    <!ELEMENT endpoint (desc?)>
    <!ATTLIST endpoint
              id    ID       	#IMPLIED
              node  IDREF    	#REQUIRED
              port  NMTOKEN  	#IMPLIED
              type  (in|out|undir) 	"undir"
    >
    

| ![](/images/void.gif)  
![](/images/void.gif)| ![](/images/void.gif)| ![](/images/void.gif)  
  
#### Contents

[_desc_](dtd.html#desc)

     _Optional_ endpoint description of the endpoint.

#### Attributes

_id_

     _Optional_ _id_ tag for the hyperedge.
_node_

    The endnode that is addressed by this hyperedge.
_port_

    The port of the endnode that is addressed by this hyperedge. The value of _port_ must match the _name_ of one of the ports of the _node_.
_type_

    The _type_ specifies how this endpoint is attatched to the hyperedge. There are three possible values: 

`in`

    Incoming (from the endnode to the hyperedge) connection
`out`

    Outgoing (from the hyperedge to the endnode) connection
`undir`

    Undirected connection
Note that the _directed_ attribute of the graph does not influence the default value of _type_.

#### Remarks

_Technically, edges are subsumed under hyperedges. We chose to differentiate between the two to ease
the recognition of non-hypergraphs. Another advantage is that edges are represented more compactly._

_Hyperedges can be used to model (potentially overlapping) clusters of nodes._

_Applications not dealing with hyperedges may ignore this element._

[back to the structural view](dtd.html#top)  
---  
  
### graph

In GraphML, graphs are represented by lists of nodes, edges and hyperedges (rather than, e.g., an
adjacency list). The _node_ , _edge_ and _hyperedge_ elements may appear in any order, to allow
applications to write out their graphs with a single pass over their internal representation.

#### DTD Definition

![](/images/void.gif)| ![](/images/void.gif)| ![](/images/void.gif)  
---|---|---  
![](/images/void.gif)|

    
    
    <!ELEMENT graph    (desc?,((data|node|edge|hyperedge)*|external))>
    <!ATTLIST graph    
              id          ID                    #IMPLIED
              edgedefault (directed|undirected) #IMPLIED
    >   
    

| ![](/images/void.gif)  
![](/images/void.gif)| ![](/images/void.gif)| ![](/images/void.gif)  
  
#### Contents

A _graph_ element may contain the following elements:

[_desc_](dtd.html#desc) (optional)

    A human readable brief description of the graph. This must be the first element in the list.
[_data_](dtd.html#data)

    Optional application specific data for the graph.
[_node_](dtd.html#node)

    A node in this graph.
[_edge_](dtd.html#edge)

    An edge in this graph.
[_hyperedge_](dtd.html#hyperedge)

    A hyperedge in this graph.
[_external_](dtd.html#external)

    Describes the external definition of the graph. 

#### Attributes

Standard attributes for _graph_ are _id_ and _edgedefault_ :

_id_ (optional)

    A graph may have an id, so it can be referenced in another place. It may also have a ref attribute signalling that it is defined somewhere else.
_edgedefault_ (optional)

    The _edgedefault_ attribute defines the default value of the edge attribute [_directed_](dtd.html#edge). The default value for _directed_ is `directed`.  

#### Examples

**Simple, undirected graph**

![](/images/void.gif)| ![](/images/void.gif)| ![](/images/void.gif)  
---|---|---  
![](/images/void.gif)|

    
    
    <graphml>
     <graph edgedefault="undirected">
      <node id="n1"/>
      <node id="n2"/>
      <edge source="n1" target="n2"/>
     </graph>
    </graphml>
    

| ![](/images/void.gif)  
![](/images/void.gif)| ![](/images/void.gif)| ![](/images/void.gif)  
  
**A graph with directed and undirected edges**  
Here is a graph with mixed directed and undirected edges. Note that the edge _e2_ gets the default
value as specified by the _directed_ attribute of the _graph_ element.

![](/images/void.gif)| ![](/images/void.gif)| ![](/images/void.gif)  
---|---|---  
![](/images/void.gif)|

    
    
    <graphml>
     <graph edgedefault="undirected">
      <node id="n1"/>
      <node id="n2"/>
      <node id="n3"/>
      <edge id="e1" source="n1" target="n2" directed="true"/>
      <edge id="e2" source="n2" target="n3" directed="false"/>
      <edge id="e3" source="n3" target="n1"/>
     </graph>
    </graphml>
    

| ![](/images/void.gif)  
![](/images/void.gif)| ![](/images/void.gif)| ![](/images/void.gif)  
  
Unlike graphs in "traditional" graph theory, this graph contains directed and undirected edges. This
shows that **all** edges must be scanned to find out wether a graph is directed or undirected.

**A hierarchical graph**  
The next example shows a GraphML file with two graphs, where the second graph is contained in the
first graph (more precisely, in a node of the first graph).

![](/images/void.gif)| ![](/images/void.gif)| ![](/images/void.gif)  
---|---|---  
![](/images/void.gif)|

    
    
    <graphml>
     <graph id="g1">
      <node id="g1n1">
       <graph id="g2"/>
        <node id="g2n1"/>
        <node id="g2n2"/>
        <edge source="g2n1" target="g2n2"/>
       </graph>
      </node>
     </graph>
    </graphml>
    

| ![](/images/void.gif)  
![](/images/void.gif)| ![](/images/void.gif)| ![](/images/void.gif)  
  
**Another hierarchical graph**  
This is a variation of the previous example. Here, the subgraph is not defined in place, but the
_xlink::href_ attribute is used to address a graph that is defined elsewhere:

![](/images/void.gif)| ![](/images/void.gif)| ![](/images/void.gif)  
---|---|---  
![](/images/void.gif)|

    
    
    <graphml>
     <graph id="g1">
      <node id="g1n1">
       <graph xlink::href="#g2">
      </node>
     </graph>
     <graph id="g2"/>
      <node id="g2n1"/>
      <node id="g2n2"/>
      <edge source="g2n1" target="g2n2"/>
     </graph>
    </graphml>
    

| ![](/images/void.gif)  
![](/images/void.gif)| ![](/images/void.gif)| ![](/images/void.gif)  
  
#### Remarks

_The fact that nodes, edges and hyperedges may come in any order implies that most parsers must use
more than one pass over their internal data structures. With the` graphml-parseinfo` extension, some
standard orderings may be signalled to ease the burden on parsers. A light-weight parser may thus
refuse to process a file that does not signify the required ordering using this extension. _

__

[back to the structural view](dtd.html#top)  
---  
  
### graphml

The element _graphml_ is the root tag of each GraphML file. A GraphML file consists of exactly one
_graphml_ element.

#### DTD Definition

![](/images/void.gif)| ![](/images/void.gif)| ![](/images/void.gif)  
---|---|---  
![](/images/void.gif)|

    
    
    <!ELEMENT graphml (desc?,key*,(data|graph)*)>

| ![](/images/void.gif)  
![](/images/void.gif)| ![](/images/void.gif)| ![](/images/void.gif)  
  
#### Contents

A _graphml_ element has a description, the keys that may be used in this file, a set of data and
finally a list of keys:

[_desc_](dtd.html#desc) (optional)

    A human readable description of the graph.
[_key_](dtd.html#key)

    The set of keys which are used in this file. This tag is intended for listing the keys together with a short description.
[_data_](dtd.html#data)

    A set of user defined data for this GraphML file.
[_graph_](dtd.html#graph)

    The set of graphs in this file.

#### Attributes

None.

#### Examples

This is a simple graph with three nodes (no edges, hence a discrete graph), and a user supplied data
element named "size":

![](/images/void.gif)| ![](/images/void.gif)| ![](/images/void.gif)  
---|---|---  
![](/images/void.gif)|

    
    
    <graphml>
     <desc>A graph with three nodes and size data</desc>
     <key id="size" for="graph">
      <desc>The number of nodes in this graph</desc>
     </key>
     <graph>
      <data key="size">3</data>
      <node id="1"/>
      <node id="2"/>
      <node id="3"/>
     </graph>
    </graphml>
    

| ![](/images/void.gif)  
![](/images/void.gif)| ![](/images/void.gif)| ![](/images/void.gif)  
  
[graphml_example.xml](graphml_example.xml.code)

[back to the structural view](dtd.html#top)  
---  
  
### hyperedge

Hyperedges are edges incident to any number of nodes (rather just two). As a generalization of
edges, each incidence may be _incoming_ , _outgoing_ , or _undirected_. and attached to a specific
port. Hence, an element endpoint encapsulates the relation between a hyperedge and a node it is
incident to.

#### DTD Definition

![](/images/void.gif)| ![](/images/void.gif)| ![](/images/void.gif)  
---|---|---  
![](/images/void.gif)|

    
    
    <!ELEMENT hyperedge (desc?,data*,(endpoint)*,graph?)>
    <!ATTLIST hyperedge id ID #IMPLIED>
    

| ![](/images/void.gif)  
![](/images/void.gif)| ![](/images/void.gif)| ![](/images/void.gif)  
  
#### Contents

An _hyperedge_ element may contain

[_desc_](dtd.html#desc)

    An _optional_ brief description of the edge. This must be the first element in the list.
[_data_](dtd.html#data)

     _Optional_ application specific data for the edge. There may be any number of such elements, but they must come after the description and before the subgraphs.
[_endpoint_](dtd.html#endpoint)

    The set of endpoints of this hyperedge.
[_graph_](dtd.html#graph)

    Like nodes and edges, hyperedges may also contain a graph.

**Order**  
The attributes must come in exactly the same order as given in the above list.

#### Attributes

_id_

     _Optional_ _id_ tag for the hyperedge.
[back to the structural view](dtd.html#top)  
---  
  
### key

Each [_data_](dtd.html#data) element must have a _key_ attribute. The value of this attribute must
match the _id_ of a key element in [_graphml_](dtd.html#graphml).

In turn, the [_graphml_](dtd.html#graphml) element contains a list of _key_ s for the graph. The
idea being that this list serves as a reference (and description via the [_desc_](dtd.html#desc)
elements) for data attributes which are potentially used in the document.

#### DTD Definition

![](/images/void.gif)| ![](/images/void.gif)| ![](/images/void.gif)  
---|---|---  
![](/images/void.gif)|

    
    
    <!ELEMENT key (desc?, default?)>
    <!ATTLIST key 
              id  ID    #REQUIRED
              for (graph|node|edge|hyperedge|port|endpoint|all) "all"
    >   
    

| ![](/images/void.gif)  
![](/images/void.gif)| ![](/images/void.gif)| ![](/images/void.gif)  
  
#### Contents

[_desc_](dtd.html#desc)

    A human-readable description for the key.
[_default_](dtd.html#default)

    

#### Attributes

_id_

    The id (name) for the key.
_xlink:type_

    No description yet.
_xlink:href_

    No description yet.
[back to the structural view](dtd.html#top)  
---  
  
### locator

The _locator_ element specifies that an object - either a _graph_ or a _data_ element - is actually
defined in a remote location. The attribute _xlink::href_ is the URL for this location.

#### DTD Definition

![](/images/void.gif)| ![](/images/void.gif)| ![](/images/void.gif)  
---|---|---  
![](/images/void.gif)|

    
    
    <!ELEMENT locator EMPTY>
    <!ATTLIST locator 
              xmlns:xlink   CDATA    #FIXED    
    		"http://www.w3.org/TR/2000/PR-xlink-20001220/"
              xlink:href    CDATA    #REQUIRED
              xlink:type    (simple) #FIXED    "simple"
    >
    

| ![](/images/void.gif)  
![](/images/void.gif)| ![](/images/void.gif)| ![](/images/void.gif)  
  
#### Contents

The element _locator_ is empty.

#### Attributes

_xlink:href_ (required)

    The URL for the actual location of the parent element.

#### Examples

![](/images/void.gif)| ![](/images/void.gif)| ![](/images/void.gif)  
---|---|---  
![](/images/void.gif)|

    
    
    <graphml>
      <graph>
        <desc>This is an example for a graph 
    	that is defined externally</desc>
        <locator xlink:href="http://www.host.org/example.xml">
      </graph>
    </graphml>
    

| ![](/images/void.gif)  
![](/images/void.gif)| ![](/images/void.gif)| ![](/images/void.gif)  
  
[external_example.xml](external_example.xml.code)

[back to the structural view](dtd.html#top)  
---  
  
### node

#### DTD Definition

![](/images/void.gif)| ![](/images/void.gif)| ![](/images/void.gif)  
---|---|---  
![](/images/void.gif)|

    
    
    <!ELEMENT node (desc?,(((data|port)*,graph?)|locator))>
    <!ATTLIST node id ID #REQUIRED>
    

| ![](/images/void.gif)  
![](/images/void.gif)| ![](/images/void.gif)| ![](/images/void.gif)  
  
#### Contents

A _node_ element may contain

[_desc_](dtd.html#desc)

    A _optional_ brief description of the node. This must be the first element in the list.
[_data_](dtd.html#data)

     _Optional_ application specific data for the node. There may be any number of such elements, but they must come after the description and before the ports. 
[_port_](dtd.html#port)

    For applications requiring grouping of incident edges, nodes may contain _port_ elements, which in turn may be hierarchical. Edges may specifiy which port they attach to.
[_graph_](dtd.html#graph)

    The set of subgraphs of this node.
[_locator_](dtd.html#locator)

    The remote location where the node is defined.

#### Attributes

_id_

    Nodes must have an _id_ , so that they can be referred to by edges.

#### Remarks

_Applications may or may not be able to deal with recursive definitions. The fall-back
interpretation for an application not dealing with nested graphs is to ignore the contained graph
element, while applications not dealing with cyclic or non-tree containment throw an exception when
encountering such situation._

[back to the structural view](dtd.html#top)  
---  
  
### port

#### DTD Definition

![](/images/void.gif)| ![](/images/void.gif)| ![](/images/void.gif)  
---|---|---  
![](/images/void.gif)|

    
    
    <!ELEMENT port (desc?,(data|port)*)>
    <!ATTLIST port
              name    NMTOKEN  #REQUIRED
    >
    

| ![](/images/void.gif)  
![](/images/void.gif)| ![](/images/void.gif)| ![](/images/void.gif)  
  
#### Contents

A _port_ element may contain a description and any number of _data_ and _port_ elements:

[_desc_](dtd.html#desc)

     An _optional_ brief description of the edge. This must be the first element in the list. 
[_port_](dtd.html#port)

     Ports have a hierarchical structure. Therefore, each port may contain any number of sub-ports. 
[_data_](dtd.html#data)

     Application specific data for this port. 

#### Attributes

_name_

     The name of this port. The edge attributes _sourceport_ and _targetport_ use this attribute to address the port. 

#### Remarks

_Port _name_ s are of type `NMTOKEN` (rather than `ID`) to allow reuse of names in different nodes
(e.g., north/west/...). _

_In the Schema specification, port ids are scoped and required to be unique within a node, like node
ids are to be unique within a graph. Thus, the potential for naming conflicts of ports is
eliminated._

[back to the structural view](dtd.html#top)  
---  
| News:  
---  
05 April 2007  
Licensing status clarified: GraphML is free for everyone. | 22 February 2007  
GraphML 1.0 schema inclusion altered to avoid problems with some parsers. | 03 August 2004  
LEDA extension package for GraphML (release candidate).  
Download [graphml_lep.zip](/download/graphml_lep.zip)  
01 June 2004  
[GraphML Primer](/primer/graphml-primer.html) released.  
18 March 2003  
XML Schema specification and documentation available for GraphML 1.0rc (release candidate)  
23 July 2002  
GraphML presentation at the [annual meeting](http://www.dfg-
schwerpunkt-1126.de/veranstaltungen/jk2002.php) of DFG Research Priority 1126 [Algorithmic Aspects
of Large and Complex Networks](http://www.dfg-schwerpunkt-1126.de/). ([ps](/publications/dfg02.ps),
[pdf](/publications/dfg02.pdf))  
28 June 2002  
[yFiles](http://www.yworks.de/en/products_yfiles_ep_graphml.htm) extension package for GraphML
version 1.0 released.  
22 May 2002  
Release candidates for extensions _graphml-attributes_ (for data attributes) and _graphml-parseinfo_
(for lightweight parsers) completed. See current [specification](/specification.html).  
12 March 2002  
GraphML proposed as the standard format for the network data archive to be created within EU FET
Open Project [COSIN](http://www.cosin.org).  
  
  
  
![](/images/void.gif)  
---  
  
[ ![Valid HTML 4.01!](http://www.w3.org/Icons/valid-
html401)](http://validator.w3.org/check?uri=referer)

(C) 2000-2002 GraphML Project Group

Last update: Friday, 25-Jan-2019 16:33:16 CET

