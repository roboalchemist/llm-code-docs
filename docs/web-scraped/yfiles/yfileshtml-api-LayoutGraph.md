# Source: https://docs.yworks.com/yfileshtml/api/LayoutGraph/

Title: LayoutGraph | yFiles for HTML Docs

URL Source: https://docs.yworks.com/yfileshtml/api/LayoutGraph/

Markdown Content:
C

Represents a directed graph structure that contains layout information for its elements and to which layout algorithms ([ILayoutAlgorithm](https://docs.yworks.com/yfileshtml/api/ILayoutAlgorithm/)) can be applied.

**Inheritance Hierarchy**

Remarks
-------

A directed graph consists of a collection of "nodes" (represented by instances of [LayoutNode](https://docs.yworks.com/yfileshtml/api/LayoutNode/)) and "edges" (represented by instances of [LayoutEdge](https://docs.yworks.com/yfileshtml/api/LayoutEdge/)) that connect pairs of nodes.

By default, the [LayoutGraph](https://docs.yworks.com/yfileshtml/api/LayoutGraph/) contains layout information, such as the position and size of nodes ([layout](https://docs.yworks.com/yfileshtml/api/LayoutNode/#layout)), and edge paths ([pathPoints](https://docs.yworks.com/yfileshtml/api/LayoutEdge/#pathPoints)). Therefore, a [LayoutGraph](https://docs.yworks.com/yfileshtml/api/LayoutGraph/) instance typically represents a visual drawing of a graph. If layout information is unnecessary, a more lightweight graph instance can be created using [createStructureGraph](https://docs.yworks.com/yfileshtml/api/LayoutGraph/#createStructureGraph), which only maintains the graph's structure without layout or labels. This is useful for performance-critical scenarios where only structural algorithms like [shortestPath](https://docs.yworks.com/yfileshtml/api/LayoutGraphAlgorithms/#shortestPath) or [pageRank](https://docs.yworks.com/yfileshtml/api/LayoutGraphAlgorithms/#pageRank) are applied.

The class supports operations such as node and edge creation, deletion, access, and iteration through properties like [nodes](https://docs.yworks.com/yfileshtml/api/LayoutGraph/#nodes) and [edges](https://docs.yworks.com/yfileshtml/api/LayoutGraph/#edges). Additionally, nodes and edges can have associated labels, accessible via [nodeLabels](https://docs.yworks.com/yfileshtml/api/LayoutGraph/#nodeLabels) and [edgeLabels](https://docs.yworks.com/yfileshtml/api/LayoutGraph/#edgeLabels).

Structural changes to the graph (such as adding or removing nodes/edges) must be made through the [LayoutGraph](https://docs.yworks.com/yfileshtml/api/LayoutGraph/) instance, ensuring consistent graph manipulation.

In addition to basic node and edge management, the [LayoutGraph](https://docs.yworks.com/yfileshtml/api/LayoutGraph/) supports the hierarchical grouping of nodes. Nodes can be designated as group nodes, which can contain other nodes, including other group nodes, forming a hierarchical structure. Methods such as [createGroupNode](https://docs.yworks.com/yfileshtml/api/LayoutGraph/#createGroupNode), [setParent](https://docs.yworks.com/yfileshtml/api/LayoutGraph/#setParent), and [setIsGroupNode](https://docs.yworks.com/yfileshtml/api/LayoutGraph/#setIsGroupNode) allow the creation and manipulation of such groups.

Group nodes are useful for organizing complex graph structures, where nodes can be logically grouped together. The grouping hierarchy can be queried using methods like [getChildren](https://docs.yworks.com/yfileshtml/api/LayoutGraph/#getChildren) and [getParent](https://docs.yworks.com/yfileshtml/api/LayoutGraph/#getParent), enabling navigation and management of the nested structure. This functionality is particularly helpful in scenarios where visual grouping or compartmentalization of nodes is required.

[Data access and manipulation](https://docs.yworks.com/yfileshtml/api/LayoutGraph/#context) are also supported via [IMapper<K, V>](https://docs.yworks.com/yfileshtml/api/IMapper/), allowing custom data to be associated with nodes and edges.

See Also
--------

### Developer's Guide

1. [Automatic Layouts](https://docs.yworks.com/yfileshtml/dguide/automatic-layouts-main-chapter/)
2. [Applying an Automatic Layout](https://docs.yworks.com/yfileshtml/dguide/layout-applying_a_layout/)

3. [Automatic Layouts](https://docs.yworks.com/yfileshtml/dguide/automatic-layouts-main-chapter/)
4. [Multi-page Layout](https://docs.yworks.com/yfileshtml/dguide/multi_page_layout/)
5. [Running a Multi-Page Layout](https://docs.yworks.com/yfileshtml/dguide/multi_page_layout/#multipage_running)

6. [Automatic Layout Features](https://docs.yworks.com/yfileshtml/dguide/layout-features/)
7. [Label Placement](https://docs.yworks.com/yfileshtml/dguide/label_placement/)
8. [Generic Labeling](https://docs.yworks.com/yfileshtml/dguide/label_placement/#label_placement-generic_labeling)

9. [Graph Analysis](https://docs.yworks.com/yfileshtml/dguide/analysis/)

10. [Customizing Automatic Layout](https://docs.yworks.com/yfileshtml/dguide/layout_graph_model/)

11. [Customizing Automatic Layout](https://docs.yworks.com/yfileshtml/dguide/layout_graph_model/)
12. [The LayoutGraph API - Part 1: Structure](https://docs.yworks.com/yfileshtml/dguide/layout_graph_api-structure/)
13. [Layout Graph Context](https://docs.yworks.com/yfileshtml/dguide/layout_graph_api-structure/#layout_graph_maps)

14. [Customizing Automatic Layout](https://docs.yworks.com/yfileshtml/dguide/layout_graph_model/)
15. [The LayoutGraph API - Part 2: Layout](https://docs.yworks.com/yfileshtml/dguide/layout_graph_api-layout/)
16. [Applying a Layout on LayoutGraph](https://docs.yworks.com/yfileshtml/dguide/layout_graph_api-layout/#layout-apply-layout-graph)

17. [Customizing Automatic Layout](https://docs.yworks.com/yfileshtml/dguide/layout_graph_model/)
18. [Customizing Table Layout](https://docs.yworks.com/yfileshtml/dguide/layout-customizing_partition_grid/)

Members
-------

Constructors
------------

### LayoutGraph

()

Properties
----------

This is a view of the currently contained bends - a new enumerable instance is provided on each invocation. Changes to the graph structure during traversal should be avoided.

readonly final

Gets the context associated with this graph.

Changes to the graph's structure or labels will be reflected in this view.

readonly final

#### Property Value

A dynamic view of all edge labels in the graph.

### isEmpty

: boolean

readonly

Gets a value indicating whether this graph is empty, that is, contains no nodes.

readonly final

#### Property Value

`true` if this graph contains no nodes; otherwise, `false`.

readonly final

#### Property Value

A dynamic view of all node labels in the graph. Any changes to the graph's structure or labels will be reflected in this view.

Methods
-------

Creates a new bend point for the given `edge` with the specified coordinates.

If the `edge` already contains bend points and no `reference` is specified, the new bend will be appended closest to the edge's target node, after all existing bends. If a `reference` is provided, the new bend will be inserted relative to that reference bend, based on the `insertion`.

final

#### Parameters

edge: [LayoutEdge](https://docs.yworks.com/yfileshtml/api/LayoutEdge/)
The edge to which the bend will be added.

x: number
The x-coordinate of the new bend.

y: number
The y-coordinate of the new bend.

reference?: [LayoutBend](https://docs.yworks.com/yfileshtml/api/LayoutBend/)
An optional existing bend adjacent to which the new bend will be created. If omitted, the bend is appended near the edge's target port.

insertion?: [RelativePosition](https://docs.yworks.com/yfileshtml/api/RelativePosition/)
conversion

Specifies whether the new bend should be inserted before or after the `reference`. If `reference` is `null`, this parameter is ignored. Use [BEFORE](https://docs.yworks.com/yfileshtml/api/RelativePosition/#BEFORE) to insert the bend in the direction of the source node, or [AFTER](https://docs.yworks.com/yfileshtml/api/RelativePosition/#AFTER) to insert it toward the target node.

#### Return Value

#### Throws

[Exception](https://docs.yworks.com/yfileshtml/api/Exception/) ({ name: 'ArgumentError' })
Thrown if `edge` does not belong to this graph, or if `x` or `y` contain a [Number.NaN](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number/NaN) value.

Creates a new label for the specified `node` with the given layout.

Creates a new label for the specified `edge` with the given layout.

Creates a new label for the specified `node` with the given dimensions.

final

#### Parameters

node: [LayoutNode](https://docs.yworks.com/yfileshtml/api/LayoutNode/)
The node to which the label will be added.

width: number
The width of the label's boundary.

height: number
The height of the label's boundary.

#### Return Value

#### Throws

[Exception](https://docs.yworks.com/yfileshtml/api/Exception/) ({ name: 'ArgumentError' })
Thrown if `node` does not belong to this graph, or if `width` or `height` contain a [Number.NaN](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number/NaN) value.

Creates a new label for the specified `edge` with the given dimensions.

final

#### Parameters

edge: [LayoutEdge](https://docs.yworks.com/yfileshtml/api/LayoutEdge/)
The edge to which the label will be added.

width: number
The width of the label's boundary.

height: number
The height of the label's boundary.

#### Return Value

#### Throws

[Exception](https://docs.yworks.com/yfileshtml/api/Exception/) ({ name: 'ArgumentError' })
Thrown if `edge` does not belong to this graph, or if `width` or `height` contain a [Number.NaN](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number/NaN) value.

### changeEdge

()

Redefines the endpoints of the specified edge, changing its [source](https://docs.yworks.com/yfileshtml/api/LayoutEdge/#source) and [target](https://docs.yworks.com/yfileshtml/api/LayoutEdge/#target) nodes.

You can specify the order in which the edge should be inserted into the incoming/outgoing edges of the source/target nodes using the reference edge parameters.

The actual new source/target node will be determined based on the reference edges provided. If the reference edges are omitted, the edge will be appended to the lists of incoming and outgoing edges at the new source and target nodes, respectively.

For example, providing [AFTER](https://docs.yworks.com/yfileshtml/api/RelativePosition/#AFTER) as `sourceInsertion` will insert the edge after the `sourceReference` edge when iterating through the outgoing edges at the source node.

final

#### Parameters

edge: [LayoutEdge](https://docs.yworks.com/yfileshtml/api/LayoutEdge/)
The edge to be modified.

newSource: [LayoutNode](https://docs.yworks.com/yfileshtml/api/LayoutNode/)
The new source node for the specified edge.

newTarget: [LayoutNode](https://docs.yworks.com/yfileshtml/api/LayoutNode/)
The new target node for the specified edge.

sourceReference?: [LayoutEdge](https://docs.yworks.com/yfileshtml/api/LayoutEdge/)
Optional. A reference edge for insertion at the new source node. If provided, its target must be the given node `newSource`.

sourceInsertion?: [RelativePosition](https://docs.yworks.com/yfileshtml/api/RelativePosition/)
Optional. Specifies whether to insert the edge immediately [BEFORE](https://docs.yworks.com/yfileshtml/api/RelativePosition/#BEFORE) or [AFTER](https://docs.yworks.com/yfileshtml/api/RelativePosition/#AFTER) the `sourceReference` edge. This parameter is ignored if the source reference is `null`.

targetReference?: [LayoutEdge](https://docs.yworks.com/yfileshtml/api/LayoutEdge/)
Optional. A reference edge for insertion at the new target node. If provided, its target must be the given node `newTarget`.

targetInsertion?: [RelativePosition](https://docs.yworks.com/yfileshtml/api/RelativePosition/)
Optional. Specifies whether to insert the edge immediately [BEFORE](https://docs.yworks.com/yfileshtml/api/RelativePosition/#BEFORE) or [AFTER](https://docs.yworks.com/yfileshtml/api/RelativePosition/#AFTER) the `targetReference` edge. This parameter is ignored if the target reference is `null`.

#### Throws

[Exception](https://docs.yworks.com/yfileshtml/api/Exception/) ({ name: 'ArgumentError' })
Thrown if the new source or target node is `null`.

[Exception](https://docs.yworks.com/yfileshtml/api/Exception/) ({ name: 'ArgumentError' })
If the new source is not the [source](https://docs.yworks.com/yfileshtml/api/LayoutEdge/#source) of the given `sourceReference` edge or the target node is not the [target](https://docs.yworks.com/yfileshtml/api/LayoutEdge/#target) of the given `targetReference` edge.

#### See Also

##### Developer's Guide

1. [Customizing Automatic Layout](https://docs.yworks.com/yfileshtml/dguide/layout_graph_model/)
2. [The LayoutGraph API - Part 1: Structure](https://docs.yworks.com/yfileshtml/dguide/layout_graph_api-structure/)
3. [Creating and Removing Graph Elements](https://docs.yworks.com/yfileshtml/dguide/layout_graph_api-structure/#layout_graph_creation)

### clear

()

Removes all nodes and edges from this graph.

Determines whether this graph contains the specified node.

final

#### Parameters

node: [LayoutNode](https://docs.yworks.com/yfileshtml/api/LayoutNode/)
The node to check for existence in the graph.

#### Return Value

boolean
`true` if this graph contains the specified node; otherwise, `false`.

Determines whether this graph contains the specified edge.

final

#### Parameters

edge: [LayoutEdge](https://docs.yworks.com/yfileshtml/api/LayoutEdge/)
The edge to check for existence in the graph.

#### Return Value

boolean
`true` if this graph contains the specified edge; otherwise, `false`.

Determines whether this graph contains the specified node label.

final

#### Parameters

#### Return Value

boolean
`true` if this graph contains the specified node label; otherwise, `false`.

Determines whether this graph contains the specified edge label.

final

#### Parameters

#### Return Value

boolean
`true` if this graph contains the specified edge label; otherwise, `false`.

Determines whether this graph contains the specified bend.

final

#### Parameters

bend: [LayoutBend](https://docs.yworks.com/yfileshtml/api/LayoutBend/)
The bend to check for existence in the graph.

#### Return Value

boolean
`true` if this graph contains the specified bend; otherwise, `false`.

The generic type arguments of the created [layout data](https://docs.yworks.com/yfileshtml/api/CompositeLayoutData/) are compatible with instances of [LayoutGraph](https://docs.yworks.com/yfileshtml/api/LayoutGraph/), but the layout data is not bound to a specific graph instance. Therefore, the created layout data still has to be passed as an argument of [applyLayout](https://docs.yworks.com/yfileshtml/api/LayoutGraph/#applyLayout) in order to be applied.

#### Parameters

#### Return Value

Creates a new edge between the specified `source` and `target` nodes.

The edge can be inserted in a specific position relative to existing edges of the source and target nodes using the `sourceReference` and `targetReference` parameters. If no reference edges are provided, the edge is added at the end of the lists of incoming/outgoing edges.

final

#### Parameters

source: [LayoutNode](https://docs.yworks.com/yfileshtml/api/LayoutNode/)
The source node of the edge.

target: [LayoutNode](https://docs.yworks.com/yfileshtml/api/LayoutNode/)
The target node of the edge.

sourceReference?: [LayoutEdge](https://docs.yworks.com/yfileshtml/api/LayoutEdge/)
The reference edge for positioning at the source node.

sourceInsertion?: [RelativePosition](https://docs.yworks.com/yfileshtml/api/RelativePosition/)
conversion

Defines whether the edge is inserted before or after `sourceReference`.

targetReference?: [LayoutEdge](https://docs.yworks.com/yfileshtml/api/LayoutEdge/)
The reference edge for positioning at the target node.

targetInsertion?: [RelativePosition](https://docs.yworks.com/yfileshtml/api/RelativePosition/)
conversion

Defines whether the edge is inserted before or after `targetReference`.

#### Return Value

#### Throws

[Exception](https://docs.yworks.com/yfileshtml/api/Exception/) ({ name: 'ArgumentError' })
Thrown if `source`, `target`, the source of `sourceReference` or the target of `targetReference` are not part of this graph.

The generic type arguments of the created [layout data](https://docs.yworks.com/yfileshtml/api/GenericLayoutData/) are compatible with instances of [LayoutGraph](https://docs.yworks.com/yfileshtml/api/LayoutGraph/), but the layout data is not bound to a specific graph instance. Therefore, the created layout data still has to be passed as an argument of [applyLayout](https://docs.yworks.com/yfileshtml/api/LayoutGraph/#applyLayout) in order to be applied.

#### Return Value

Creates a new group node as a direct descendant of `parent` using the optional specified layout.

Creates a new node using the specified layout.

final

#### Parameters

layout: [Rect](https://docs.yworks.com/yfileshtml/api/Rect/)
conversion

The layout to use for the node's initial position and size.

#### Return Value

#### See Also

##### API

[layout](https://docs.yworks.com/yfileshtml/api/LayoutNode/#LayoutNode-property-layout)

Creates a new node as a direct descendant of `parent` using the optional specified layout.

final

#### Parameters

parent?: [LayoutNode](https://docs.yworks.com/yfileshtml/api/LayoutNode/)
The parent node in the grouping hierarchy. If `null`, the new node becomes a top-level node. To change the parent after creation, use [setParent](https://docs.yworks.com/yfileshtml/api/LayoutGraph/#setParent).

layout?: [Rect](https://docs.yworks.com/yfileshtml/api/Rect/)
conversion

The initial layout for the node, including position and size. The layout is copied to the node's [layout](https://docs.yworks.com/yfileshtml/api/LayoutNode/#layout) property. If not specified, the node's position is set to (0, 0), and its size is set to 30x30.

#### Return Value

#### Throws

[Exception](https://docs.yworks.com/yfileshtml/api/Exception/) ({ name: 'ArgumentError' })
Thrown if `parent` is not a valid node in this graph or if `layout` contains invalid values (e.g., [Number.NaN](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number/NaN)).

#### See Also

##### API

[setParent](https://docs.yworks.com/yfileshtml/api/LayoutGraph/#LayoutGraph-method-setParent), [getParent](https://docs.yworks.com/yfileshtml/api/LayoutGraph/#LayoutGraph-method-getParent), [layout](https://docs.yworks.com/yfileshtml/api/LayoutNode/#LayoutNode-property-layout), [createNode](https://docs.yworks.com/yfileshtml/api/LayoutGraph/#LayoutGraph-method-createNode(yfiles.geometry.Rect))

### getBounds

(
includeNodeLabels?: boolean

includeEdgeLabels?: boolean

includeMargins?: boolean

): [Rect](https://docs.yworks.com/yfileshtml/api/Rect/)

Returns the bounds of the graph, optionally considering the specified nodes and edges, including node labels, edge labels, or node margins.

final

#### Parameters

nodes?: [IEnumerable](https://docs.yworks.com/yfileshtml/api/IEnumerable/?parameter-types=LayoutNode)<[LayoutNode](https://docs.yworks.com/yfileshtml/api/LayoutNode/)>
conversion

The nodes whose geometry contributes to the bounds. If `null` or omitted, all nodes of the graph will be considered.

edges?: [IEnumerable](https://docs.yworks.com/yfileshtml/api/IEnumerable/?parameter-types=LayoutEdge)<[LayoutEdge](https://docs.yworks.com/yfileshtml/api/LayoutEdge/)>
conversion

The edges whose geometry contributes to the bounds. If `null` or omitted, all edges of the graph will be considered.

includeNodeLabels?: boolean
A flag indicating whether to include node labels in the bounds calculation.

includeEdgeLabels?: boolean
A flag indicating whether to include edge labels in the bounds calculation.

includeMargins?: boolean
A flag indicating whether to include node margins in the bounds calculation.

#### Return Value

[Rect](https://docs.yworks.com/yfileshtml/api/Rect/)
The calculated bounds of the specified nodes and edges.

Returns the children of the specified group node.

Returns the edges between the specified source and target nodes.

By default, only directed edges are returned. To retrieve all edges (both incoming and outgoing), set directed to `false`.

final

#### Parameters

source: [LayoutNode](https://docs.yworks.com/yfileshtml/api/LayoutNode/)
The node from which the edges start.

target: [LayoutNode](https://docs.yworks.com/yfileshtml/api/LayoutNode/)
The node at which the edges end.

directed?: boolean
Specifies whether to return only directed edges (default) or all edges regardless of direction.

#### Return Value

#### Throws

[Exception](https://docs.yworks.com/yfileshtml/api/Exception/) ({ name: 'ArgumentError' })
Thrown if either `source` or `target` is not contained in this graph.

Returns the parent node of a specified node, or `null` if the node is a top-level node.

Determines whether the specified node is a group node.

Reinserts a previously removed node back into this graph.

The reinserted node is appended to the sequence of nodes in this graph. Its new position will likely differ from its position prior to removal.

final

#### Parameters

#### Throws

[Exception](https://docs.yworks.com/yfileshtml/api/Exception/) ({ name: 'ArgumentError' })
Thrown if `node` is already present in the graph.

#### See Also

##### API

[remove](https://docs.yworks.com/yfileshtml/api/LayoutGraph/#LayoutGraph-method-remove(yfiles.layout.LayoutNode))

Reinserts a previously removed edge back into this graph.

The reinserted edge is appended to the sequence of edges in this graph. Its new position will likely differ from its position prior to removal, including the edge's positions in the incoming and outgoing edges of its source and target nodes.

Attempting to reinsert an edge whose source or target node is not present in the graph will result in an exception. Therefore, the corresponding endpoints must be reinserted first.

final

#### Parameters

#### Throws

[Exception](https://docs.yworks.com/yfileshtml/api/Exception/) ({ name: 'ArgumentError' })
Thrown if `edge` is already present in a graph, or if either the source or target of `edge` is not present in this graph.

#### See Also

##### API

[remove](https://docs.yworks.com/yfileshtml/api/LayoutGraph/#LayoutGraph-method-remove(yfiles.layout.LayoutEdge))

Removes the specified edge from this graph.

If the edge is intended to be temporarily hidden, it can be reinserted using the [reinsert](https://docs.yworks.com/yfileshtml/api/LayoutGraph/#reinsert) method.

final

#### Parameters

#### Throws

[Exception](https://docs.yworks.com/yfileshtml/api/Exception/) ({ name: 'ArgumentError' })
Thrown if `edge` is not present in this graph.

Removes the specified node from this graph.

Removes the given `bend` from the edge it belongs to and thus from this graph.

final

#### Parameters

#### Throws

[Exception](https://docs.yworks.com/yfileshtml/api/Exception/) ({ name: 'ArgumentError' })
`bend` is not in this graph.

Removes the given `label` from its node.

Removes the given `label` from its edge.

Reverses the specified edge.

### setIsGroupNode

(node: [LayoutNode](https://docs.yworks.com/yfileshtml/api/LayoutNode/), isGroup: boolean)

Updates the group node status of a specified node.

This method allows the modification of a node's status to indicate whether it is a group node, which can have children as indicated by [getChildren](https://docs.yworks.com/yfileshtml/api/LayoutGraph/#getChildren).

When this method is used to turn a group node into a normal node, it must first be assured that the `node` does not have any [child nodes](https://docs.yworks.com/yfileshtml/api/LayoutGraphGrouping/#hasChildren).

final

#### Parameters

node: [LayoutNode](https://docs.yworks.com/yfileshtml/api/LayoutNode/)
The node for which to set the group node status.

isGroup: boolean
A boolean indicating whether to make the node a group node (`true`) or not (`false`).

#### Throws

[Exception](https://docs.yworks.com/yfileshtml/api/Exception/) ({ name: 'ArgumentError' })
Thrown if `node` is not part of this graph or if `node` still has child nodes

#### See Also

##### Developer's Guide

1. [Customizing Automatic Layout](https://docs.yworks.com/yfileshtml/dguide/layout_graph_model/)
2. [The LayoutGraph API - Part 1: Structure](https://docs.yworks.com/yfileshtml/dguide/layout_graph_api-structure/)
3. [Group Nodes](https://docs.yworks.com/yfileshtml/dguide/layout_graph_api-structure/#layout_graph_group_nodes)

##### API

[getChildren](https://docs.yworks.com/yfileshtml/api/LayoutGraph/#LayoutGraph-method-getChildren), [isGroupNode](https://docs.yworks.com/yfileshtml/api/LayoutGraph/#LayoutGraph-method-isGroupNode)

Sets the parent node for a specified node.

Use `null` as `parent` to designate `node` as a top-level node in the graph.

If `parent` is not already a [group node](https://docs.yworks.com/yfileshtml/api/LayoutGraph/#isGroupNode) prior to this call, it will be automatically converted into a group node.

To retrieve the parent of a node, utilize the [getParent](https://docs.yworks.com/yfileshtml/api/LayoutGraph/#getParent) method.

final

#### Parameters

node: [LayoutNode](https://docs.yworks.com/yfileshtml/api/LayoutNode/)
The node to which a new parent will be assigned.

parent: [LayoutNode](https://docs.yworks.com/yfileshtml/api/LayoutNode/)
The parent group node to be assigned to `node`, or `null` to make `node` a top-level node.

#### Throws

[Exception](https://docs.yworks.com/yfileshtml/api/Exception/) ({ name: 'ArgumentError' })
Thrown if `node` or `parent` are not part of this graph.

[Exception](https://docs.yworks.com/yfileshtml/api/Exception/) ({ name: 'InvalidOperationError' })
Thrown if the `parent` is a descendant of `node` or the `node` itself.

#### See Also

##### Developer's Guide

1. [Customizing Automatic Layout](https://docs.yworks.com/yfileshtml/dguide/layout_graph_model/)
2. [The LayoutGraph API - Part 1: Structure](https://docs.yworks.com/yfileshtml/dguide/layout_graph_api-structure/)
3. [Group Nodes](https://docs.yworks.com/yfileshtml/dguide/layout_graph_api-structure/#layout_graph_group_nodes)

##### API

[getParent](https://docs.yworks.com/yfileshtml/api/LayoutGraph/#LayoutGraph-method-getParent)

Sorts the list of [LayoutEdge](https://docs.yworks.com/yfileshtml/api/LayoutEdge/) objects in this graph.

final

#### Parameters

comparator: function([LayoutEdge](https://docs.yworks.com/yfileshtml/api/LayoutEdge/), [LayoutEdge](https://docs.yworks.com/yfileshtml/api/LayoutEdge/)): number
A comparison delegate that defines the criteria for sorting the edges.

Sorts incoming and outgoing edges at each node of the graph.

If a given comparison function is `null`, then the corresponding edges (i.e., incoming/outgoing) will not be sorted. This method sorts the order of edges as returned by [inEdges](https://docs.yworks.com/yfileshtml/api/LayoutNode/#inEdges) and [outEdges](https://docs.yworks.com/yfileshtml/api/LayoutNode/#outEdges) respectively.

final

#### Parameters

inEdgeComparator: function([LayoutEdge](https://docs.yworks.com/yfileshtml/api/LayoutEdge/), [LayoutEdge](https://docs.yworks.com/yfileshtml/api/LayoutEdge/)): number
The comparison function used for sorting the incoming edges at each node. Set to `null` to skip sorting incoming edges.

outEdgeComparator: function([LayoutEdge](https://docs.yworks.com/yfileshtml/api/LayoutEdge/), [LayoutEdge](https://docs.yworks.com/yfileshtml/api/LayoutEdge/)): number
The comparison function used for sorting the outgoing edges at each node. Set to `null` to skip sorting outgoing edges.

Sorts the list of [LayoutNode](https://docs.yworks.com/yfileshtml/api/LayoutNode/) objects in this graph.

final

#### Parameters

comparator: function([LayoutNode](https://docs.yworks.com/yfileshtml/api/LayoutNode/), [LayoutNode](https://docs.yworks.com/yfileshtml/api/LayoutNode/)): number
A comparison delegate that defines the criteria for sorting the nodes.

### toString

(): string

Returns a string representation of this graph.

The result contains the string representations of all nodes followed by the string representations of all edges in the graph.

final

#### Return Value

string
A string representation of this graph.

Static Methods
--------------

Creates a graph that represents a plain graph structure without layout information for its nodes and edges.

Creating an optimized graph is recommended for performance-critical applications where only the graph structure is relevant, and no [ILayoutAlgorithm](https://docs.yworks.com/yfileshtml/api/ILayoutAlgorithm/) will be applied.

A graph created using this method cannot be processed by [ILayoutAlgorithm](https://docs.yworks.com/yfileshtml/api/ILayoutAlgorithm/)s. To create a [LayoutGraph](https://docs.yworks.com/yfileshtml/api/LayoutGraph/) with layout capabilities, use the standard constructor.

Layout properties of [LayoutNode](https://docs.yworks.com/yfileshtml/api/LayoutNode/)s and [LayoutEdge](https://docs.yworks.com/yfileshtml/api/LayoutEdge/)s can be written and accessed without exceptions, but they have no meaningful effect on a graph created with this method. The same applies when trying to [add bends](https://docs.yworks.com/yfileshtml/api/LayoutGraph/#addBend) or [add labels](https://docs.yworks.com/yfileshtml/api/LayoutGraph/#addLabel). Therefore, it must be avoided to read and write layout-related information on a graph created with this method!

static

#### Return Value
