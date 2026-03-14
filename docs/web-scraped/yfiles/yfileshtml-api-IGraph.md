# Source: https://docs.yworks.com/yfileshtml/api/IGraph/

Title: IGraph | yFiles for HTML Docs

URL Source: https://docs.yworks.com/yfileshtml/api/IGraph/

Markdown Content:
Visit www.yfiles.com for more information!
Home
API
Guide
Search
View
Graph
E
AdjacencyTypes
C
BendAnchoredPortLocationModel
C
BendDecorator
C
BendEventArgs
C
BezierEdgePathLabelModel
C
BezierEdgeSegmentLabelModel
C
ClipboardGraphCopier
C
ClipboardOperationContext
E
CloneTypes
C
CompositeLabelModel
C
CompositePortLocationModel
E
CompositePortLocationModelPortSide
C
EdgeDecorator
C
EdgeDefaults
C
EdgeEventArgs
C
EdgePathLabelModel
C
EdgePathPortLocationModel
C
EdgeSegmentLabelModel
C
EdgeSegmentPortLocationModel
E
EdgeSides
C
ExcludingFoldingEdgeConverter
C
ExteriorNodeLabelModel
E
ExteriorNodeLabelModelPosition
C
FilteredGraphWrapper
C
FolderNodeConverter
C
FolderNodeDefaults
C
FolderNodeState
C
FoldingBendState
C
FoldingEdgeConverter
C
FoldingEdgeDefaults
C
FoldingEdgeState
C
FoldingEdgeStateId
C
FoldingLabelDefaults
C
FoldingLabelOwnerState
C
FoldingLabelState
C
FoldingManager
C
FoldingPortDefaults
C
FoldingPortState
E
FoldingPortType
E
FoldingSynchronizationOptions
C
FreeEdgeLabelModel
C
FreeLabelModel
C
FreeNodeLabelModel
C
FreeNodePortLocationModel
C
FreePortLabelModel
C
Graph
C
GraphClipboard
C
GraphClipboardEventArgs
C
GraphCopier
C
GraphDecorator
E
GraphItemTypes
C
GraphWrapperBase
C
GroupingSupport
C
GroupNodeLabelModel
I
IBend
I
IClipboardHelper
I
IClipboardIdProvider
I
IColumn
I
ICompoundEdit
I
IEdge
I
IEdgeDefaults
I
IFolderNodeConverter
I
IFoldingEdgeConverter
I
IFoldingEdgeConverterContext
I
IFoldingView
I
IGraph
I
IGraphClipboardContext
I
IGroupBoundsCalculator
I
ILabel
I
ILabelDefaults
I
ILabelModel
I
ILabelModelParameter
I
ILabelModelParameterFinder
I
ILabelModelParameterProvider
I
ILabelOwner
I
IMementoSupport
I
IModelItem
I
INode
I
INodeDefaults
C
InsideOutsidePortLabelModel
C
InteriorNodeLabelModel
E
InteriorNodeLabelModelPosition
I
IPort
I
IPortDefaults
I
IPortLocationModel
I
IPortLocationModelParameter
I
IPortOwner
I
IRow
I
IStripe
I
IStripeDefaults
I
ITable
C
ItemChangedEventArgs
C
ItemCopiedEventArgs
I
IUndoUnit
C
LabelDecorator
C
LabelDefaults
C
LabelEventArgs
C
MergingFoldingEdgeConverter
C
NinePositionsEdgeLabelModel
E
NinePositionsEdgeLabelModelPosition
C
NodeDecorator
C
NodeDefaults
C
NodeEventArgs
C
NodeLabelModelStripeLabelModelAdapter
E
ParentNodeDetectionModes
E
PlaceAlongEdge
C
PortDecorator
C
PortDefaults
C
PortEventArgs
C
SimpleBend
C
SimpleEdge
C
SimpleLabel
C
SimpleNode
C
SimplePort
C
SmartEdgeLabelModel
C
StretchNodeLabelModel
E
StretchNodeLabelModelPosition
C
StretchStripeLabelModel
E
StretchStripeLabelModelPosition
C
StripeDecorator
C
StripeDefaults
C
StripeEventArgs
C
StripeLabelDecorator
C
StripeLabelModel
E
StripeLabelModelPosition
E
StripeTypes
C
Table
C
TableDecorator
C
UndoEngine
C
AbsoluteFreeLabelModelParameter
expert
C
AnchoredFreeLabelModelParameter
expert
C
BendAnchoredPortLocationModelParameter
expert
C
BezierEdgePathLabelModelParameter
expert
C
BezierEdgeSegmentLabelModelParameter
expert
C
CompositeLabelModelParameter
expert
C
CompositePortLocationModelParameter
expert
C
DynamicFreeLabelModelParameter
expert
C
EdgePathLabelModelParameter
expert
C
EdgePathPortLocationModelParameter
expert
C
EdgeSegmentLabelModelParameter
expert
C
EdgeSegmentPortLocationModelParameter
expert
C
ExteriorNodeLabelModelParameter
expert
C
FreeEdgeLabelModelParameter
expert
C
FreeNodeLabelModelParameter
expert
C
FreeNodePortLocationModelParameter
expert
C
FreePortLabelModelParameter
expert
C
GroupNodeLabelModelParameter
expert
C
InsideOutsidePortLabelModelParameter
expert
C
InteriorNodeLabelModelParameter
expert
C
NinePositionsEdgeLabelModelParameter
expert
C
NodeLabelModelStripeLabelModelAdapterParameter
expert
C
SmartEdgeLabelModelParameter
expert
C
StretchNodeLabelModelParameter
expert
C
StretchStripeLabelModelParameter
expert
C
StripeLabelModelParameter
expert
UI Components
User Interaction
Graph Item Styles
Data Binding
Geometry
GraphML
Layout
Base
I
IGraph
Show Usages
Central interface that models a graph which can be displayed in a canvas or GraphComponent.
Implements
I
ILookup
I
ITagOwner
Inheritance Hierarchy
I
IGraph
Remarks

This interface can be used to query structural information, it also offers methods that change the structure of the graph and its attributes. Furthermore, a number of events will be triggered if the structure of the graph changes.

The graph is made up of collections of nodes and edges. Each node and edge can be associated with a number of labels and possibly ports to which edges connect. An edge connects to two ports and may consist of zero or more bends. The graph is treated as a directed graph, i.e. edges have a sourcePort and a targetPort. It is up to the algorithms and the visualization to possibly treat them as undirected.

This interface also provides support for hierarchically organized, i.e. grouped graphs. This means that nodes together with their connecting edges can be put into other nodes. The containing node is referred to as a "group node." To create and edit group nodes interactively use the GraphEditorInputMode as input mode and enable the grouping operations.

The edgesAt and edgesAt methods can be used to query adjacency information from the graph's structure.

Each element in the graph can be associated with a style that is used for the visualization of the element. Styles can be shared between multiple instances.

To associate data with the elements in the graph, code can make use of the tag property that all IModelItems provide. In order to associate more than one data element with the graph items, compound data objects can be used. Alternatively additional dictionaries can be used to associate arbitrary data sets with the items in this graph.

This interface provides a number of events that can be used to get notified for changes in the graph structure. These events are raised whenever the corresponding state change occurs, e.g. also when loading the graph from a file. If you are only interested in changes that are triggered interactively, you should subscribe to the corresponding events on the IInputMode implementations that implement the user interaction. Especially, you may not modify the graph structure in handlers for these event, e.g. try to prevent or undo the change that has raised the event.

Examples

New elements can be created either using defaults or with explicitly provided styles:

Creating graph elements
const graph = graphComponent.graph

// set defaults for newly created elements

// appearance of nodes
graph.nodeDefaults.style = new ShapeNodeStyle({
  shape: ShapeNodeShape.RECTANGLE,
  fill: Color.ORANGE,
})
// placement and appearance of node labels
graph.nodeDefaults.labels.layoutParameter = InteriorNodeLabelModel.CENTER
graph.nodeDefaults.labels.style = new LabelStyle({
  backgroundStroke: Stroke.BLACK,
  backgroundFill: Color.WHITE,
})

// create some nodes and edges
const node1 = graph.createNode()
const node2 = graph.createNode(
  new Rect(100, 0, 60, 40),
  new GroupNodeStyle(),
  'some tag',
)
const edge1 = graph.createEdge(
  node1,
  node2,
  new PolylineEdgeStyle({ targetArrow: new Arrow(ArrowType.STEALTH) }),
)
Copy

Existing elements can be changed using methods provided by IGraph:

Changing the graph
let index = 0
for (const node of graph.nodes) {
  if (node.labels.size === 0) {
    // if the node has no label, yet, add one
    graph.addLabel(node, `New label for node ${index}`)
  } else {
    // otherwise change the first label's text
    graph.setLabelText(
      node.labels.get(0),
      `Change text for node ${index}`,
    )
  }
  // set another style for the node
  graph.setStyle(
    node,
    new ShapeNodeStyle({
      shape: ShapeNodeShape.RECTANGLE,
      fill: Color.GREEN,
    }),
  )
  index++
}
Copy

The graph can be traversed along the edges with the help of a number of methods which provide adjacency information from the graph's structure.

Analyzing the graph structure
for (const node of graph.nodes) {
  const nodeName = node.labels.get(0).text
  // no predecessors: the node is a root
  if (!graph.predecessors(node).some()) {
    console.log(`Node ${nodeName} is a root.`)
  }
  // no successor: the node is a leaf
  if (!graph.successors(node).some()) {
    console.log(`Node ${nodeName} is a leaf.`)
  }
  // list all nodes which are linked to the current node
  for (const edge of graph.edgesAt(node)) {
    const otherNode = edge.opposite(node) as INode
    console.log(
      `Node ${nodeName} is linked to ${otherNode.labels.get(0).text}.`,
    )
  }
}
Copy

Finally, graph items can also be removed.

Removing graph elements and clearing the graph
// IMPORTANT: graph.nodes will throw exception if it is changed during iteration
// therefore we have to iterate over a copy of the node collection
// while we remove the nodes
const nodesToRemove = graph.nodes.toList()
for (const node of nodesToRemove) {
  graph.remove(node)
}

// clear the existing graph
graph.clear()
Copy

IGraph also provides support for hierarchically organized, i.e. grouped graphs. This means that nodes together with their connecting edges can be put into other nodes.

Grouping features overview
const graph = graphComponent.graph

// set the defaults for a newly created group node
graph.groupNodeDefaults.style = new ShapeNodeStyle({
  shape: ShapeNodeShape.ROUND_RECTANGLE,
  stroke: Stroke.AQUAMARINE,
  fill: null,
})
// create a group node
const groupNode = graph.createGroupNode()
// add existing nodes as children

graph.groupNodes(groupNode, [node1, node2, node3])

// whether the node is a group node
console.log(graph.isGroupNode(groupNode)) // true
console.log(graph.isGroupNode(node1)) // false

// get the parent of a node
console.log(graph.getParent(node1)) // groupNode
console.log(graph.getParent(groupNode)) // null

// get the children of a group node
const children = graph.getChildren(groupNode) // node1, node2, node3
console.log(children.size) // 3
Copy
See Also

The graph model with all relevant types and their relationships is presented in detail in the section The Graph Model.

More information on visual styles can be found in the section Visualization of Graph Elements.

Developer's Guide
Getting Started
Creating a Simple Web Application
Creating Graph Elements
Getting Started
Creating a Simple Web Application
Automatic Graph Layout
The Graph Model
The Graph Model
IGraph
The Graph Model
Ports
The Graph Model
Finding Adjacent Nodes and Edges
Automatic Layouts
Automatic Layouts
Applying an Automatic Layout
Automatic Layout Features
Label Placement
Generic Labeling
Creating a Graph from Business Data
Common Features
Creating And Updating Graphs
Customizing User Interaction
Undo and Redo
Customizing Automatic Layout
General Concepts for Customization
Service Locator Pattern: Lookup
Examples for Lookup Decoration
Advanced Concepts
WebGL2 Rendering
WebGL Styles
API
Graph, INode, IEdge, IPort, ILabel, IBend
Members
Show:
inherited
Search Members
I
IGraph
To the top
Remarks
Members
Properties
bends
decorator
edgeDefaults
edgeLabels
edges
foldingView
groupingSupport
groupNodeDefaults
labels
nodeDefaults
nodeLabels
nodes
portLabels
ports
tag
undoEngine
undoEngineEnabled
Methods
addBend(IEdge, Point, number)
addBends(IEdge, IEnumerable<Point>)
addEventListener(string, function(evt: EventArgs, sender: this), ListenerOptions)
addLabel(ILabelOwner, string, ILabelModelParameter, ILabelStyle, Size, ILabel['tag'])
addPort(IPortOwner, IPortLocationModelParameter, IPortStyle, IPort['tag'])
addPortAt(IPortOwner, Point, IPortStyle, IPort['tag'])
addRelativePort(INode, Point)
addUndoUnit(string, string, function(), function())
adjustGroupNodeLayout(INode)
adjustLabelPreferredSize(ILabel)
applyLayout(ILayoutAlgorithm, LayoutData<INode, IEdge, ILabel, ILabel>, TimeSpan, TimeSpan, ItemMapping<IPort, PortAdjustmentPolicy>, ItemMapping<IPort, PortPlacementPolicy>, ItemMapping<ILabel, PortLabelPolicy>, ItemMapping<IModelItem, LayoutAnchoringPolicy>, ItemMapping<ILabel, LabelPlacementPolicy>, function(INode, INode): number, function(IEdge, IEdge): number)
beginEdit(string, string)
beginEdit(string, string, IEnumerable<T>, function(T)IMementoSupport)
calculateLabelPreferredSize(ILabelOwner, string, ILabelModelParameter, ILabelStyle, ILabel['tag'])
clear()
clearBends(IEdge)
clearLabels(ILabelOwner)
clearPorts(IPortOwner)
contains(IModelItem)
createCompositeLayoutData(...LayoutData<INode, IEdge, ILabel, ILabel>)
createDefaultLabelLayoutParameter(ILabelOwner)
createDefaultPortLocationParameter(IPortOwner, Point)
createEdge(IPort, IPort, IEdgeStyle, IEdge['tag'])
createEdge(INode, INode, IEdgeStyle, IEdge['tag'])
createGenericLayoutData()
createGroupNode(INode, Rect, INodeStyle, INode['tag'])
createNode(Rect, INodeStyle, INode['tag'])
createNode(INode, Rect, INodeStyle, INode['tag'])
createNodeAt(Point, INodeStyle, INode['tag'])
degree(IPortOwner)
degree(IPort)
edgesAt(IPort, AdjacencyTypes)
edgesAt(IPortOwner, AdjacencyTypes)
getChildren(INode)
getEdge(IPortOwner, IPortOwner)
getEdge(IPort, IPort)
getEdgesBetween(IPortOwner, IPortOwner, boolean)
getEdgesBetween(IPort, IPort, boolean)
getLabelDefaults(ILabelOwner)
getParent(INode)
getPortDefaults(IPortOwner)
groupNodes(INode, IEnumerable<INode>)
groupNodes(IEnumerable<INode>, INodeStyle, any)
inDegree(IPortOwner)
inDegree(IPort)
inEdgesAt(IPortOwner)
inEdgesAt(IPort)
invalidateDisplays()
isGroupNode(INode)
lookup(Constructor<T>)
neighbors(INode)
outDegree(IPortOwner)
outDegree(IPort)
outEdgesAt(IPortOwner)
outEdgesAt(IPort)
predecessors(INode)
remove(IModelItem)
removeEventListener(string, function(evt: EventArgs, sender: this), ListenerOptions)
reverse(IEdge)
setBendLocation(IBend, Point)
setEdgePorts(IEdge, IPort, IPort)
setIsGroupNode(INode, boolean)
setLabelLayoutParameter(ILabel, ILabelModelParameter)
setLabelPreferredSize(ILabel, Size)
setLabelText(ILabel, string)
setNodeCenter(INode, Point)
setNodeLayout(INode, Rect)
setParent(INode, INode)
setPortLocation(IPort, Point)
setPortLocationParameter(IPort, IPortLocationModelParameter)
setRelativePortLocation(IPort, Point)
setStyle(INode, INodeStyle)
setStyle(ILabel, ILabelStyle)
setStyle(IEdge, IEdgeStyle)
setStyle(IPort, IPortStyle)
successors(INode)
Events
bend-added
bend-location-changed
bend-removed
bend-tag-changed
displays-invalidated
edge-created
edge-ports-changed
edge-removed
edge-style-changed
edge-tag-changed
graph-tag-changed
is-group-node-changed
label-added
label-layout-parameter-changed
label-preferred-size-changed
label-removed
label-style-changed
label-tag-changed
label-text-changed
node-created
node-layout-changed
node-removed
node-style-changed
node-tag-changed
parent-changed
port-added
port-location-parameter-changed
port-removed
port-style-changed
port-tag-changed
yFiles
Playground
yWorks
Imprint
Terms of use
Privacy Policy
Sitemap

Copyright © 2026 yWorks GmbH · All rights reserved
