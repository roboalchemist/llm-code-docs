# Source: https://reactflow.dev/api-reference/types

Title: Types - React Flow

URL Source: https://reactflow.dev/api-reference/types

Markdown Content:
[Align](https://reactflow.dev/api-reference/types/align)
--------------------------------------------------------

The Align type contains the values expected by the align prop of the NodeToolbar component

[Read more](https://reactflow.dev/api-reference/types/align)
[AriaLabelConfig](https://reactflow.dev/api-reference/types/aria-label-config)
------------------------------------------------------------------------------

With the AriaLabelConfig you can customize the aria labels and descriptions used by React Flow.

[Read more](https://reactflow.dev/api-reference/types/aria-label-config)
[BackgroundVariant](https://reactflow.dev/api-reference/types/background-variant)
---------------------------------------------------------------------------------

The three variants are exported as an enum for convenience. You can either import the enum and use it like BackgroundVariant.Lines or you can use the raw string value directly.

[Read more](https://reactflow.dev/api-reference/types/background-variant)
[ColorMode](https://reactflow.dev/api-reference/types/color-mode)
-----------------------------------------------------------------

The ColorMode type defines the available color modes for the ReactFlow component.

[Read more](https://reactflow.dev/api-reference/types/color-mode)
[Connection](https://reactflow.dev/api-reference/types/connection)
------------------------------------------------------------------

The Connection type is the basic minimal description of an Edge between two nodes. The addEdge util can be used to upgrade a Connection to an Edge.

[Read more](https://reactflow.dev/api-reference/types/connection)
[ConnectionLineComponent](https://reactflow.dev/api-reference/types/connection-line-component)
----------------------------------------------------------------------------------------------

Custom React component for rendering the connection line during edge creation.

[Read more](https://reactflow.dev/api-reference/types/connection-line-component)
[ConnectionLineComponentProps](https://reactflow.dev/api-reference/types/connection-line-component-props)
---------------------------------------------------------------------------------------------------------

If you want to render a custom component for connection lines, you can set the connectionLineComponent prop on the ReactFlow component. The ConnectionLineComponentProps are passed to your custom component.

[Read more](https://reactflow.dev/api-reference/types/connection-line-component-props)
[ConnectionLineType](https://reactflow.dev/api-reference/types/connection-line-type)
------------------------------------------------------------------------------------

If you set the connectionLineType prop on your ReactFlow component, it will dictate the style of connection line rendered when creating new edges.

[Read more](https://reactflow.dev/api-reference/types/connection-line-type)
[ConnectionMode](https://reactflow.dev/api-reference/types/connection-mode)
---------------------------------------------------------------------------

Specifies the rules for how connections between nodes are established.

[Read more](https://reactflow.dev/api-reference/types/connection-mode)
[ConnectionState](https://reactflow.dev/api-reference/types/connection-state)
-----------------------------------------------------------------------------

Data about an ongoing connection.

[Read more](https://reactflow.dev/api-reference/types/connection-state)
[CoordinateExtent](https://reactflow.dev/api-reference/types/coordinate-extent)
-------------------------------------------------------------------------------

A coordinate extent represents two points in a coordinate system: one in the top left corner and one in the bottom right corner. It is used to represent the bounds of nodes in the flow or the bounds of the viewport.

[Read more](https://reactflow.dev/api-reference/types/coordinate-extent)
[DefaultEdgeOptions](https://reactflow.dev/api-reference/types/default-edge-options)
------------------------------------------------------------------------------------

Many properties on an Edge are optional. When a new edge is created, the properties that are not provided will be filled in with the default values passed to the defaultEdgeOptions prop of the ReactFlow component.

[Read more](https://reactflow.dev/api-reference/types/default-edge-options)
[DeleteElements](https://reactflow.dev/api-reference/types/delete-elements)
---------------------------------------------------------------------------

DeleteElements deletes nodes and edges from the flow and return the deleted edges and nodes asynchronously.

[Read more](https://reactflow.dev/api-reference/types/delete-elements)
[Edge](https://reactflow.dev/api-reference/types/edge)
------------------------------------------------------

Where a Connection is the minimal description of an edge between two nodes, an `Edge` is the complete description with everything React Flow needs to know in order to render it.

[Read more](https://reactflow.dev/api-reference/types/edge)
[EdgeChange](https://reactflow.dev/api-reference/types/edge-change)
-------------------------------------------------------------------

The onEdgesChange callback takes an array of EdgeChange objects that you should use to update your flow's state. The EdgeChange type is a union of four different object types that represent that various ways an edge can change in a flow.

[Read more](https://reactflow.dev/api-reference/types/edge-change)
[EdgeMarker](https://reactflow.dev/api-reference/types/edge-marker)
-------------------------------------------------------------------

Edges can optionally have markers at the start and end of an edge. The EdgeMarker type is used to configure those markers! Check the docs for MarkerType for details on what types of edge marker are available.

[Read more](https://reactflow.dev/api-reference/types/edge-marker)
[EdgeMouseHandler](https://reactflow.dev/api-reference/types/edge-mouse-handler)
--------------------------------------------------------------------------------

The EdgeMouseHandler type defines the callback function that is called when mouse events occur on an edge.

[Read more](https://reactflow.dev/api-reference/types/edge-mouse-handler)
[EdgeProps](https://reactflow.dev/api-reference/types/edge-props)
-----------------------------------------------------------------

When you implement a custom edge it is wrapped in a component that enables some basic functionality. Your custom edge component receives the following props:

[Read more](https://reactflow.dev/api-reference/types/edge-props)
[EdgeTypes](https://reactflow.dev/api-reference/types/edge-types)
-----------------------------------------------------------------

The EdgeTypes type is used to define custom edge types.

[Read more](https://reactflow.dev/api-reference/types/edge-types)
[FitViewOptions](https://reactflow.dev/api-reference/types/fit-view-options)
----------------------------------------------------------------------------

When calling fitView these options can be used to customize the behavior. For example, the duration option can be used to transform the viewport smoothly over a given amount of time.

[Read more](https://reactflow.dev/api-reference/types/fit-view-options)
[Handle](https://reactflow.dev/api-reference/types/handle)
----------------------------------------------------------

Handle attributes like id, position, and type.

[Read more](https://reactflow.dev/api-reference/types/handle)
[HandleConnection](https://reactflow.dev/api-reference/types/handle-connection)
-------------------------------------------------------------------------------

The HandleConnection type is a Connection that includes the edgeId.

[Read more](https://reactflow.dev/api-reference/types/handle-connection)
[InternalNode](https://reactflow.dev/api-reference/types/internal-node)
-----------------------------------------------------------------------

The InternalNode is an extension of the base Node type with additional properties React Flow uses internally for rendering.

[Read more](https://reactflow.dev/api-reference/types/internal-node)
[IsValidConnection](https://reactflow.dev/api-reference/types/is-valid-connection)
----------------------------------------------------------------------------------

Function type that determines whether a connection between nodes is valid.

[Read more](https://reactflow.dev/api-reference/types/is-valid-connection)
[KeyCode](https://reactflow.dev/api-reference/types/key-code)
-------------------------------------------------------------

Represents keyboard key codes or combinations.

[Read more](https://reactflow.dev/api-reference/types/key-code)
[MarkerType](https://reactflow.dev/api-reference/types/marker-type)
-------------------------------------------------------------------

Edges may optionally have a marker on either end. The MarkerType type enumerates the options available to you when configuring a given marker.

[Read more](https://reactflow.dev/api-reference/types/marker-type)
[MiniMapNodeProps](https://reactflow.dev/api-reference/types/mini-map-node-props)
---------------------------------------------------------------------------------

The MiniMapNodeProps type defines the properties for nodes in a minimap component.

[Read more](https://reactflow.dev/api-reference/types/mini-map-node-props)
[Node](https://reactflow.dev/api-reference/types/node)
------------------------------------------------------

The Node type represents everything React Flow needs to know about a given node. Many of these properties can be manipulated both by React Flow or by you, but some such as width and height should be considered read-only.

[Read more](https://reactflow.dev/api-reference/types/node)
[NodeChange](https://reactflow.dev/api-reference/types/node-change)
-------------------------------------------------------------------

The onNodesChange callback takes an array of NodeChange objects that you should use to update your flow's state. The NodeChange type is a union of six different object types that represent that various ways an node can change in a flow.

[Read more](https://reactflow.dev/api-reference/types/node-change)
[NodeConnection](https://reactflow.dev/api-reference/types/node-connection)
---------------------------------------------------------------------------

The NodeConnection type is a Connection that includes the edgeId.

[Read more](https://reactflow.dev/api-reference/types/node-connection)
[NodeHandle](https://reactflow.dev/api-reference/types/node-handle)
-------------------------------------------------------------------

The NodeHandle type is used to define a handle for a node if server side rendering is used.

[Read more](https://reactflow.dev/api-reference/types/node-handle)
[NodeMouseHandler](https://reactflow.dev/api-reference/types/node-mouse-handler)
--------------------------------------------------------------------------------

The NodeMouseHandler type defines the callback function that is called when mouse events occur on a node.

[Read more](https://reactflow.dev/api-reference/types/node-mouse-handler)
[NodeOrigin](https://reactflow.dev/api-reference/types/node-origin)
-------------------------------------------------------------------

The origin of a Node determines how it is placed relative to its own coordinates.

[Read more](https://reactflow.dev/api-reference/types/node-origin)
[NodeProps](https://reactflow.dev/api-reference/types/node-props)
-----------------------------------------------------------------

When you implement a custom node it is wrapped in a component that enables basic functionality like selection and dragging. Your custom node receives the following props:

[Read more](https://reactflow.dev/api-reference/types/node-props)
[NodeTypes](https://reactflow.dev/api-reference/types/node-types)
-----------------------------------------------------------------

The NodeTypes type is used to define custom node types.

[Read more](https://reactflow.dev/api-reference/types/node-types)
[OnBeforeDelete](https://reactflow.dev/api-reference/types/on-before-delete)
----------------------------------------------------------------------------

The OnBeforeDelete type defines the callback function that is called before nodes or edges are deleted.

[Read more](https://reactflow.dev/api-reference/types/on-before-delete)
[OnConnect](https://reactflow.dev/api-reference/types/on-connect)
-----------------------------------------------------------------

Callback function triggered when a new connection is created between nodes.

[Read more](https://reactflow.dev/api-reference/types/on-connect)
[OnConnectEnd](https://reactflow.dev/api-reference/types/on-connect-end)
------------------------------------------------------------------------

Callback function triggered when finishing or canceling a connection attempt between nodes.

[Read more](https://reactflow.dev/api-reference/types/on-connect-end)
[OnConnectStart](https://reactflow.dev/api-reference/types/on-connect-start)
----------------------------------------------------------------------------

Callback function triggered when starting to create a connection between nodes.

[Read more](https://reactflow.dev/api-reference/types/on-connect-start)
[OnDelete](https://reactflow.dev/api-reference/types/on-delete)
---------------------------------------------------------------

The OnDelete type defines the callback function that is called when nodes or edges are deleted.

[Read more](https://reactflow.dev/api-reference/types/on-delete)
[OnEdgesChange](https://reactflow.dev/api-reference/types/on-edges-change)
--------------------------------------------------------------------------

[Read more](https://reactflow.dev/api-reference/types/on-edges-change)
[OnEdgesDelete](https://reactflow.dev/api-reference/types/on-edges-delete)
--------------------------------------------------------------------------

The OnEdgesDelete type defines the callback function that is called when edges are deleted.

[Read more](https://reactflow.dev/api-reference/types/on-edges-delete)
[OnError](https://reactflow.dev/api-reference/types/on-error)
-------------------------------------------------------------

The OnError type defines the callback function that is called when an error occurs.

[Read more](https://reactflow.dev/api-reference/types/on-error)
[OnInit](https://reactflow.dev/api-reference/types/on-init)
-----------------------------------------------------------

The OnInit type defines the callback function that is called when the ReactFlow instance is initialized.

[Read more](https://reactflow.dev/api-reference/types/on-init)
[OnMove](https://reactflow.dev/api-reference/types/on-move)
-----------------------------------------------------------

Invoked when the viewport is moved, such as by panning or zooming.

[Read more](https://reactflow.dev/api-reference/types/on-move)
[OnNodeDrag](https://reactflow.dev/api-reference/types/on-node-drag)
--------------------------------------------------------------------

The OnNodeDrag type defines the callback function that is called when a node is being dragged.

[Read more](https://reactflow.dev/api-reference/types/on-node-drag)
[OnNodesChange](https://reactflow.dev/api-reference/types/on-nodes-change)
--------------------------------------------------------------------------

[Read more](https://reactflow.dev/api-reference/types/on-nodes-change)
[OnNodesDelete](https://reactflow.dev/api-reference/types/on-nodes-delete)
--------------------------------------------------------------------------

The OnNodesDelete type defines the callback function that is called when nodes are deleted.

[Read more](https://reactflow.dev/api-reference/types/on-nodes-delete)
[OnReconnect](https://reactflow.dev/api-reference/types/on-reconnect)
---------------------------------------------------------------------

Callback function triggered when an existing edge is reconnected to a different node or handle.

[Read more](https://reactflow.dev/api-reference/types/on-reconnect)
[OnSelectionChangeFunc](https://reactflow.dev/api-reference/types/on-selection-change-func)
-------------------------------------------------------------------------------------------

Called whenever the selection of nodes or edges changes in the flow diagram.

[Read more](https://reactflow.dev/api-reference/types/on-selection-change-func)
[PanOnScrollMode](https://reactflow.dev/api-reference/types/pan-on-scroll-mode)
-------------------------------------------------------------------------------

Configures how the viewport responds to scroll events, allowing free, vertical, or horizontal panning.

[Read more](https://reactflow.dev/api-reference/types/pan-on-scroll-mode)
[PanelPosition](https://reactflow.dev/api-reference/types/panel-position)
-------------------------------------------------------------------------

This type is mostly used to help position things on top of the flow viewport. For example both the MiniMap and Controls components take a position prop of this type.

[Read more](https://reactflow.dev/api-reference/types/panel-position)
[Position](https://reactflow.dev/api-reference/types/position)
--------------------------------------------------------------

While PanelPosition can be used to place a component in the corners of a container, the Position enum is less precise and used primarily in relation to edges and handles.

[Read more](https://reactflow.dev/api-reference/types/position)
[ProOptions](https://reactflow.dev/api-reference/types/pro-options)
-------------------------------------------------------------------

By default, we render a small attribution in the corner of your flows that links back to the project.

[Read more](https://reactflow.dev/api-reference/types/pro-options)
[ReactFlowInstance](https://reactflow.dev/api-reference/types/react-flow-instance)
----------------------------------------------------------------------------------

The ReactFlowInstance provides a collection of methods to query and manipulate the internal state of your flow. You can get an instance by using the useReactFlow hook or attaching a listener to the onInit event.

[Read more](https://reactflow.dev/api-reference/types/react-flow-instance)
[ReactFlowJsonObject](https://reactflow.dev/api-reference/types/react-flow-json-object)
---------------------------------------------------------------------------------------

A JSON-compatible representation of your flow. You can use this to save the flow to a database for example and load it back in later.

[Read more](https://reactflow.dev/api-reference/types/react-flow-json-object)
[Rect](https://reactflow.dev/api-reference/types/rect)
------------------------------------------------------

The Rect type defines a rectangle with dimensions and a position.

[Read more](https://reactflow.dev/api-reference/types/rect)
[ResizeParams](https://reactflow.dev/api-reference/types/resize-params)
-----------------------------------------------------------------------

The ResizeParams type is used to type the various events that are emitted by the NodeResizer component. You'll sometimes see this type extended with an additional direction field too.

[Read more](https://reactflow.dev/api-reference/types/resize-params)
[SelectionDragHandler](https://reactflow.dev/api-reference/types/selection-drag-handler)
----------------------------------------------------------------------------------------

Handles drag events for selected nodes during interactive operations.

[Read more](https://reactflow.dev/api-reference/types/selection-drag-handler)
[SelectionMode](https://reactflow.dev/api-reference/types/selection-mode)
-------------------------------------------------------------------------

Controls how nodes are selected in the flow diagram, offering either full or partial selection behavior.

[Read more](https://reactflow.dev/api-reference/types/selection-mode)
[SnapGrid](https://reactflow.dev/api-reference/types/snap-grid)
---------------------------------------------------------------

The SnapGrid type defines the grid size for snapping nodes on the pane.

[Read more](https://reactflow.dev/api-reference/types/snap-grid)
[Viewport](https://reactflow.dev/api-reference/types/viewport)
--------------------------------------------------------------

Internally, React Flow maintains a coordinate system that is independent of the rest of the page. The Viewport type tells you where in that system your flow is currently being display at and how zoomed in or out it is.

[Read more](https://reactflow.dev/api-reference/types/viewport)
[XYPosition](https://reactflow.dev/api-reference/types/xy-position)
-------------------------------------------------------------------

All positions are stored in an object with x and y coordinates.

[Read more](https://reactflow.dev/api-reference/types/xy-position)
[ZIndexMode](https://reactflow.dev/api-reference/types/z-index-mode)
--------------------------------------------------------------------

The ZIndexMode type is used to define how z-indexing is calculated for nodes and edges.

[Read more](https://reactflow.dev/api-reference/types/z-index-mode)
