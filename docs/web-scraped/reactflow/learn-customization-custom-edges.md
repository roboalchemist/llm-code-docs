# Source: https://reactflow.dev/learn/customization/custom-edges

Title: Custom Edges - React Flow

URL Source: https://reactflow.dev/learn/customization/custom-edges

Markdown Content:
Custom Edges - React Flow
===============

[Skip to Content](https://reactflow.dev/learn/customization/custom-edges#nextra-skip-nav)

[React Flow](https://reactflow.dev/)

[Learn](https://reactflow.dev/learn)[Reference](https://reactflow.dev/api-reference)[Examples](https://reactflow.dev/examples)[UI](https://reactflow.dev/ui)[Showcase](https://reactflow.dev/showcase)More

Search[](https://github.com/xyflow/xyflow)[](https://discord.gg/RVmnytFmGW)[React Flow Pro](https://reactflow.dev/pro)

* Learn

  * [Quick Start](https://reactflow.dev/learn)
  * Core Concepts

    * [Overview](https://reactflow.dev/learn/concepts/terms-and-definitions)
    * [Building a Flow](https://reactflow.dev/learn/concepts/building-a-flow)
    * [Adding Interactivity](https://reactflow.dev/learn/concepts/adding-interactivity)
    * [The Viewport](https://reactflow.dev/learn/concepts/the-viewport)
    * [Built-In Components](https://reactflow.dev/learn/concepts/built-in-components)

  * Customization

    * [Nodes](https://reactflow.dev/learn/customization/custom-nodes)
    * [Handles](https://reactflow.dev/learn/customization/handles)
    * [Edges](https://reactflow.dev/learn/customization/custom-edges)
    * [Edge Labels](https://reactflow.dev/learn/customization/edge-labels)
    * [Utility Classes](https://reactflow.dev/learn/customization/utility-classes)
    * [Theming](https://reactflow.dev/learn/customization/theming)

  * Layouting

    * [Overview](https://reactflow.dev/learn/layouting/layouting)
    * [Sub Flows](https://reactflow.dev/learn/layouting/sub-flows)

  * Advanced Use

    * [Hooks and Providers](https://reactflow.dev/learn/advanced-use/hooks-providers)
    * [Accessibility](https://reactflow.dev/learn/advanced-use/accessibility)
    * [Testing](https://reactflow.dev/learn/advanced-use/testing)
    * [TypeScript](https://reactflow.dev/learn/advanced-use/typescript)
    * [Uncontrolled Flow](https://reactflow.dev/learn/advanced-use/uncontrolled-flow)
    * [Performance](https://reactflow.dev/learn/advanced-use/performance)
    * [State Management](https://reactflow.dev/learn/advanced-use/state-management)
    * [Computing Flows](https://reactflow.dev/learn/advanced-use/computing-flows)
    * [Server Side Rendering](https://reactflow.dev/learn/advanced-use/ssr-ssg-configuration)
    * [Devtools](https://reactflow.dev/learn/advanced-use/devtools-and-debugging)
    * [Multiplayer](https://reactflow.dev/learn/advanced-use/multiplayer)
    * [Whiteboard Features](https://reactflow.dev/learn/advanced-use/whiteboard)

  * Tutorials

    * [Slideshow App](https://reactflow.dev/learn/tutorials/slide-shows-with-react-flow)
    * [Web Audio API](https://reactflow.dev/learn/tutorials/react-flow-and-the-web-audio-api)
    * [Mind Map App](https://reactflow.dev/learn/tutorials/mind-map-app-with-react-flow)
    * [React Flow UI](https://reactflow.dev/learn/tutorials/getting-started-with-react-flow-components)

  * Troubleshooting

    * [Common Errors](https://reactflow.dev/learn/troubleshooting/common-errors)
    * [Remove Attribution](https://reactflow.dev/learn/troubleshooting/remove-attribution)
    * [Migrate to v12](https://reactflow.dev/learn/troubleshooting/migrate-to-v12)
    * [Migrate to v11](https://reactflow.dev/learn/troubleshooting/migrate-to-v11)
    * [Migrate to v10](https://reactflow.dev/learn/troubleshooting/migrate-to-v10)

  * [API Reference](https://reactflow.dev/api-reference)

* Reference

  * [API Reference](https://reactflow.dev/api-reference)
  * [<ReactFlow />](https://reactflow.dev/api-reference/react-flow)
  * [<ReactFlowProvider />](https://reactflow.dev/api-reference/react-flow-provider)
  * [Components](https://reactflow.dev/api-reference/components)

    * [<Background />](https://reactflow.dev/api-reference/components/background)
    * [<BaseEdge />](https://reactflow.dev/api-reference/components/base-edge)
    * [<ControlButton />](https://reactflow.dev/api-reference/components/control-button)
    * [<Controls />](https://reactflow.dev/api-reference/components/controls)
    * [<EdgeLabelRenderer />](https://reactflow.dev/api-reference/components/edge-label-renderer)
    * [<EdgeText />](https://reactflow.dev/api-reference/components/edge-text)
    * [<EdgeToolbar />](https://reactflow.dev/api-reference/components/edge-toolbar)
    * [<Handle />](https://reactflow.dev/api-reference/components/handle)
    * [<MiniMap />](https://reactflow.dev/api-reference/components/minimap)
    * [<NodeResizeControl />](https://reactflow.dev/api-reference/components/node-resize-control)
    * [<NodeResizer />](https://reactflow.dev/api-reference/components/node-resizer)
    * [<NodeToolbar />](https://reactflow.dev/api-reference/components/node-toolbar)
    * [<Panel />](https://reactflow.dev/api-reference/components/panel)
    * [<ViewportPortal />](https://reactflow.dev/api-reference/components/viewport-portal)

  * [Hooks](https://reactflow.dev/api-reference/hooks)

    * [useConnection()](https://reactflow.dev/api-reference/hooks/use-connection)
    * [useEdges()](https://reactflow.dev/api-reference/hooks/use-edges)
    * [useEdgesState()](https://reactflow.dev/api-reference/hooks/use-edges-state)
    * [useHandleConnections()](https://reactflow.dev/api-reference/hooks/use-handle-connections)
    * [useInternalNode()](https://reactflow.dev/api-reference/hooks/use-internal-node)
    * [useKeyPress()](https://reactflow.dev/api-reference/hooks/use-key-press)
    * [useNodeConnections()](https://reactflow.dev/api-reference/hooks/use-node-connections)
    * [useNodeId()](https://reactflow.dev/api-reference/hooks/use-node-id)
    * [useNodes()](https://reactflow.dev/api-reference/hooks/use-nodes)
    * [useNodesData()](https://reactflow.dev/api-reference/hooks/use-nodes-data)
    * [useNodesInitialized()](https://reactflow.dev/api-reference/hooks/use-nodes-initialized)
    * [useNodesState()](https://reactflow.dev/api-reference/hooks/use-nodes-state)
    * [useOnSelectionChange()](https://reactflow.dev/api-reference/hooks/use-on-selection-change)
    * [useOnViewportChange()](https://reactflow.dev/api-reference/hooks/use-on-viewport-change)
    * [useReactFlow()](https://reactflow.dev/api-reference/hooks/use-react-flow)
    * [useStore()](https://reactflow.dev/api-reference/hooks/use-store)
    * [useStoreApi()](https://reactflow.dev/api-reference/hooks/use-store-api)
    * [useUpdateNodeInternals()](https://reactflow.dev/api-reference/hooks/use-update-node-internals)
    * [useViewport()](https://reactflow.dev/api-reference/hooks/use-viewport)

  * [Types](https://reactflow.dev/api-reference/types)

    * [Align](https://reactflow.dev/api-reference/types/align)
    * [AriaLabelConfig](https://reactflow.dev/api-reference/types/aria-label-config)
    * [BackgroundVariant](https://reactflow.dev/api-reference/types/background-variant)
    * [ColorMode](https://reactflow.dev/api-reference/types/color-mode)
    * [Connection](https://reactflow.dev/api-reference/types/connection)
    * [ConnectionLineComponent](https://reactflow.dev/api-reference/types/connection-line-component)
    * [ConnectionLineComponentProps](https://reactflow.dev/api-reference/types/connection-line-component-props)
    * [ConnectionLineType](https://reactflow.dev/api-reference/types/connection-line-type)
    * [ConnectionMode](https://reactflow.dev/api-reference/types/connection-mode)
    * [ConnectionState](https://reactflow.dev/api-reference/types/connection-state)
    * [CoordinateExtent](https://reactflow.dev/api-reference/types/coordinate-extent)
    * [DefaultEdgeOptions](https://reactflow.dev/api-reference/types/default-edge-options)
    * [DeleteElements](https://reactflow.dev/api-reference/types/delete-elements)
    * [Edge](https://reactflow.dev/api-reference/types/edge)
    * [EdgeChange](https://reactflow.dev/api-reference/types/edge-change)
    * [EdgeMarker](https://reactflow.dev/api-reference/types/edge-marker)
    * [EdgeMouseHandler](https://reactflow.dev/api-reference/types/edge-mouse-handler)
    * [EdgeProps](https://reactflow.dev/api-reference/types/edge-props)
    * [EdgeTypes](https://reactflow.dev/api-reference/types/edge-types)
    * [FitViewOptions](https://reactflow.dev/api-reference/types/fit-view-options)
    * [Handle](https://reactflow.dev/api-reference/types/handle)
    * [HandleConnection](https://reactflow.dev/api-reference/types/handle-connection)
    * [InternalNode](https://reactflow.dev/api-reference/types/internal-node)
    * [IsValidConnection](https://reactflow.dev/api-reference/types/is-valid-connection)
    * [KeyCode](https://reactflow.dev/api-reference/types/key-code)
    * [MarkerType](https://reactflow.dev/api-reference/types/marker-type)
    * [MiniMapNodeProps](https://reactflow.dev/api-reference/types/mini-map-node-props)
    * [Node](https://reactflow.dev/api-reference/types/node)
    * [NodeChange](https://reactflow.dev/api-reference/types/node-change)
    * [NodeConnection](https://reactflow.dev/api-reference/types/node-connection)
    * [NodeHandle](https://reactflow.dev/api-reference/types/node-handle)
    * [NodeMouseHandler](https://reactflow.dev/api-reference/types/node-mouse-handler)
    * [NodeOrigin](https://reactflow.dev/api-reference/types/node-origin)
    * [NodeProps](https://reactflow.dev/api-reference/types/node-props)
    * [NodeTypes](https://reactflow.dev/api-reference/types/node-types)
    * [OnBeforeDelete](https://reactflow.dev/api-reference/types/on-before-delete)
    * [OnConnect](https://reactflow.dev/api-reference/types/on-connect)
    * [OnConnectEnd](https://reactflow.dev/api-reference/types/on-connect-end)
    * [OnConnectStart](https://reactflow.dev/api-reference/types/on-connect-start)
    * [OnDelete](https://reactflow.dev/api-reference/types/on-delete)
    * [OnEdgesChange](https://reactflow.dev/api-reference/types/on-edges-change)
    * [OnEdgesDelete](https://reactflow.dev/api-reference/types/on-edges-delete)
    * [OnError](https://reactflow.dev/api-reference/types/on-error)
    * [OnInit](https://reactflow.dev/api-reference/types/on-init)
    * [OnMove](https://reactflow.dev/api-reference/types/on-move)
    * [OnNodeDrag](https://reactflow.dev/api-reference/types/on-node-drag)
    * [OnNodesChange](https://reactflow.dev/api-reference/types/on-nodes-change)
    * [OnNodesDelete](https://reactflow.dev/api-reference/types/on-nodes-delete)
    * [OnReconnect](https://reactflow.dev/api-reference/types/on-reconnect)
    * [OnSelectionChangeFunc](https://reactflow.dev/api-reference/types/on-selection-change-func)
    * [PanOnScrollMode](https://reactflow.dev/api-reference/types/pan-on-scroll-mode)
    * [PanelPosition](https://reactflow.dev/api-reference/types/panel-position)
    * [Position](https://reactflow.dev/api-reference/types/position)
    * [ProOptions](https://reactflow.dev/api-reference/types/pro-options)
    * [ReactFlowInstance](https://reactflow.dev/api-reference/types/react-flow-instance)
    * [ReactFlowJsonObject](https://reactflow.dev/api-reference/types/react-flow-json-object)
    * [Rect](https://reactflow.dev/api-reference/types/rect)
    * [ResizeParams](https://reactflow.dev/api-reference/types/resize-params)
    * [SelectionDragHandler](https://reactflow.dev/api-reference/types/selection-drag-handler)
    * [SelectionMode](https://reactflow.dev/api-reference/types/selection-mode)
    * [SnapGrid](https://reactflow.dev/api-reference/types/snap-grid)
    * [Viewport](https://reactflow.dev/api-reference/types/viewport)
    * [XYPosition](https://reactflow.dev/api-reference/types/xy-position)
    * [ZIndexMode](https://reactflow.dev/api-reference/types/z-index-mode)

  * [Utils](https://reactflow.dev/api-reference/utils)

    * [addEdge()](https://reactflow.dev/api-reference/utils/add-edge)
    * [applyEdgeChanges()](https://reactflow.dev/api-reference/utils/apply-edge-changes)
    * [applyNodeChanges()](https://reactflow.dev/api-reference/utils/apply-node-changes)
    * [getBezierPath()](https://reactflow.dev/api-reference/utils/get-bezier-path)
    * [getConnectedEdges()](https://reactflow.dev/api-reference/utils/get-connected-edges)
    * [getIncomers()](https://reactflow.dev/api-reference/utils/get-incomers)
    * [getNodesBounds()](https://reactflow.dev/api-reference/utils/get-nodes-bounds)
    * [getOutgoers()](https://reactflow.dev/api-reference/utils/get-outgoers)
    * [getSimpleBezierPath()](https://reactflow.dev/api-reference/utils/get-simple-bezier-path)
    * [getSmoothStepPath()](https://reactflow.dev/api-reference/utils/get-smooth-step-path)
    * [getStraightPath()](https://reactflow.dev/api-reference/utils/get-straight-path)
    * [getViewportForBounds()](https://reactflow.dev/api-reference/utils/get-viewport-for-bounds)
    * [isEdge()](https://reactflow.dev/api-reference/utils/is-edge)
    * [isNode()](https://reactflow.dev/api-reference/utils/is-node)
    * [reconnectEdge()](https://reactflow.dev/api-reference/utils/reconnect-edge)

* Examples

  * [Examples](https://reactflow.dev/examples)
  * [Feature Overview](https://reactflow.dev/examples/overview)
  * Nodes

    * [Add Node on Edge Drop](https://reactflow.dev/examples/nodes/add-node-on-edge-drop)
    * [Connection Limit](https://reactflow.dev/examples/nodes/connection-limit)
    * [Custom Node](https://reactflow.dev/examples/nodes/custom-node)
    * [Delete Middle Node](https://reactflow.dev/examples/nodes/delete-middle-node)
    * [Drag Handle](https://reactflow.dev/examples/nodes/drag-handle)
    * [Easy Connect](https://reactflow.dev/examples/nodes/easy-connect)
    * [Intersections](https://reactflow.dev/examples/nodes/intersections)
    * [Node Resizer](https://reactflow.dev/examples/nodes/node-resizer)
    * [Node Toolbar](https://reactflow.dev/examples/nodes/node-toolbar)
    * [Proximity Connect](https://reactflow.dev/examples/nodes/proximity-connect)
    * [Rotatable Node](https://reactflow.dev/examples/nodes/rotatable-node)
    * [Node Position Animation](https://reactflow.dev/examples/nodes/node-position-animation)
    * [Stress](https://reactflow.dev/examples/nodes/stress)
    * [Update Node](https://reactflow.dev/examples/nodes/update-node)
    * [Shapes](https://reactflow.dev/examples/nodes/shapes)

  * Edges

    * [Animating Edges](https://reactflow.dev/examples/edges/animating-edges)
    * [Custom Connection Line](https://reactflow.dev/examples/edges/custom-connectionline)
    * [Custom Edges](https://reactflow.dev/examples/edges/custom-edges)
    * [Delete Edge on Drop](https://reactflow.dev/examples/edges/delete-edge-on-drop)
    * [Edge Label Renderer](https://reactflow.dev/examples/edges/edge-label-renderer)
    * [Edge Intersection](https://reactflow.dev/examples/edges/edge-intersection)
    * [Edge Toolbar](https://reactflow.dev/examples/edges/edge-toolbar)
    * [Edge Types](https://reactflow.dev/examples/edges/edge-types)
    * [Floating Edges](https://reactflow.dev/examples/edges/floating-edges)
    * [Markers](https://reactflow.dev/examples/edges/markers)
    * [Multi Connection Line](https://reactflow.dev/examples/edges/multi-connection-line)
    * [Reconnect Edge](https://reactflow.dev/examples/edges/reconnect-edge)
    * [Simple Floating Edges](https://reactflow.dev/examples/edges/simple-floating-edges)
    * [Temporary Edges](https://reactflow.dev/examples/edges/temporary-edges)
    * [Editable Edge](https://reactflow.dev/examples/edges/editable-edge)

  * Interaction

    * [Computing Flows](https://reactflow.dev/examples/interaction/computing-flows)
    * [Connection Events](https://reactflow.dev/examples/interaction/connection-events)
    * [Context Menu](https://reactflow.dev/examples/interaction/context-menu)
    * [Contextual Zoom](https://reactflow.dev/examples/interaction/contextual-zoom)
    * [Drag and Drop](https://reactflow.dev/examples/interaction/drag-and-drop)
    * [Prevent Cycles](https://reactflow.dev/examples/interaction/prevent-cycles)
    * [Save and Restore](https://reactflow.dev/examples/interaction/save-and-restore)
    * [Touch Device](https://reactflow.dev/examples/interaction/touch-device)
    * [Validation](https://reactflow.dev/examples/interaction/validation)
    * [Helper Lines](https://reactflow.dev/examples/interaction/helper-lines)
    * [Collaborative](https://reactflow.dev/examples/interaction/collaborative)
    * [Copy Paste](https://reactflow.dev/examples/interaction/copy-paste)
    * [Undo Redo](https://reactflow.dev/examples/interaction/undo-redo)

  * Subflows & Grouping

    * [Selection Grouping](https://reactflow.dev/examples/grouping/selection-grouping)
    * [Parent Child Relation](https://reactflow.dev/examples/grouping/parent-child-relation)
    * [Sub Flows](https://reactflow.dev/examples/grouping/sub-flows)

  * Layout

    * [Dagre](https://reactflow.dev/examples/layout/dagre)
    * [Elkjs](https://reactflow.dev/examples/layout/elkjs)
    * [Elkjs Multiple Handles](https://reactflow.dev/examples/layout/elkjs-multiple-handles)
    * [Horizontal](https://reactflow.dev/examples/layout/horizontal)
    * [Expand Collapse](https://reactflow.dev/examples/layout/expand-collapse)
    * [Auto Layout](https://reactflow.dev/examples/layout/auto-layout)
    * [Force Layout](https://reactflow.dev/examples/layout/force-layout)
    * [Dynamic Layouting](https://reactflow.dev/examples/layout/dynamic-layouting)
    * [Node Collisions](https://reactflow.dev/examples/layout/node-collisions)

  * Styling

    * [Base Style](https://reactflow.dev/examples/styling/base-style)
    * [Dark Mode](https://reactflow.dev/examples/styling/dark-mode)
    * [Tailwind](https://reactflow.dev/examples/styling/tailwind)
    * [Turbo Flow](https://reactflow.dev/examples/styling/turbo-flow)

  * Whiteboard

    * [Eraser](https://reactflow.dev/examples/whiteboard/eraser)
    * [Lasso Selection](https://reactflow.dev/examples/whiteboard/lasso-selection)
    * [Rectangle](https://reactflow.dev/examples/whiteboard/rectangle)
    * [Freehand Draw](https://reactflow.dev/examples/whiteboard/freehand-draw)

  * Misc

    * [Download Image](https://reactflow.dev/examples/misc/download-image)
    * [Server Side Image Creation](https://reactflow.dev/examples/misc/server-side-image-creation)

* UI

  * [Introduction](https://reactflow.dev/ui)
  * Templates

    * [AI Workflow Editor](https://reactflow.dev/ui/templates/ai-workflow-editor)
    * [Workflow Editor](https://reactflow.dev/ui/templates/workflow-editor)

  * Components

    * Node Utilities
    * [Base Node](https://reactflow.dev/ui/components/base-node)
    * [Status Indicator](https://reactflow.dev/ui/components/node-status-indicator)
    * [Appendix](https://reactflow.dev/ui/components/node-appendix)
    * [Tooltip](https://reactflow.dev/ui/components/node-tooltip)
    * Custom Nodes
    * [Database Schema](https://reactflow.dev/ui/components/database-schema-node)
    * [Placeholder](https://reactflow.dev/ui/components/placeholder-node)
    * [Labeled Group](https://reactflow.dev/ui/components/labeled-group-node)
    * Handles
    * [Base Handle](https://reactflow.dev/ui/components/base-handle)
    * [Labeled Handle](https://reactflow.dev/ui/components/labeled-handle)
    * [Button Handle](https://reactflow.dev/ui/components/button-handle)
    * Custom Edges
    * [Edge with Button](https://reactflow.dev/ui/components/button-edge)
    * [Edge with Node Data](https://reactflow.dev/ui/components/data-edge)
    * [Animated SVG Edge](https://reactflow.dev/ui/components/animated-svg-edge)
    * Controls
    * [Node Search](https://reactflow.dev/ui/components/node-search)
    * [Zoom Slider](https://reactflow.dev/ui/components/zoom-slider)
    * [Zoom Select](https://reactflow.dev/ui/components/zoom-select)
    * Misc
    * [DevTools](https://reactflow.dev/ui/components/devtools)

  *

* * *

    *   [Request a Component](https://github.com/xyflow/web/discussions/new?category=ui-component-requests)

* [Showcase](https://reactflow.dev/showcase)
* More

  * [Changelog](https://reactflow.dev/whats-new)
  * [Blog](https://xyflow.com/blog)
  * [Contact Us](https://xyflow.com/contact)
  * [Playground](https://play.reactflow.dev/)

* [Quick Start](https://reactflow.dev/learn)
* Core Concepts

  * [Overview](https://reactflow.dev/learn/concepts/terms-and-definitions)
  * [Building a Flow](https://reactflow.dev/learn/concepts/building-a-flow)
  * [Adding Interactivity](https://reactflow.dev/learn/concepts/adding-interactivity)
  * [The Viewport](https://reactflow.dev/learn/concepts/the-viewport)
  * [Built-In Components](https://reactflow.dev/learn/concepts/built-in-components)

* Customization

  * [Nodes](https://reactflow.dev/learn/customization/custom-nodes)
  * [Handles](https://reactflow.dev/learn/customization/handles)
  * [Edges](https://reactflow.dev/learn/customization/custom-edges)
  * [Edge Labels](https://reactflow.dev/learn/customization/edge-labels)
  * [Utility Classes](https://reactflow.dev/learn/customization/utility-classes)
  * [Theming](https://reactflow.dev/learn/customization/theming)

* Layouting

  * [Overview](https://reactflow.dev/learn/layouting/layouting)
  * [Sub Flows](https://reactflow.dev/learn/layouting/sub-flows)

* Advanced Use

  * [Hooks and Providers](https://reactflow.dev/learn/advanced-use/hooks-providers)
  * [Accessibility](https://reactflow.dev/learn/advanced-use/accessibility)
  * [Testing](https://reactflow.dev/learn/advanced-use/testing)
  * [TypeScript](https://reactflow.dev/learn/advanced-use/typescript)
  * [Uncontrolled Flow](https://reactflow.dev/learn/advanced-use/uncontrolled-flow)
  * [Performance](https://reactflow.dev/learn/advanced-use/performance)
  * [State Management](https://reactflow.dev/learn/advanced-use/state-management)
  * [Computing Flows](https://reactflow.dev/learn/advanced-use/computing-flows)
  * [Server Side Rendering](https://reactflow.dev/learn/advanced-use/ssr-ssg-configuration)
  * [Devtools](https://reactflow.dev/learn/advanced-use/devtools-and-debugging)
  * [Multiplayer](https://reactflow.dev/learn/advanced-use/multiplayer)
  * [Whiteboard Features](https://reactflow.dev/learn/advanced-use/whiteboard)

* Tutorials

  * [Slideshow App](https://reactflow.dev/learn/tutorials/slide-shows-with-react-flow)
  * [Web Audio API](https://reactflow.dev/learn/tutorials/react-flow-and-the-web-audio-api)
  * [Mind Map App](https://reactflow.dev/learn/tutorials/mind-map-app-with-react-flow)
  * [React Flow UI](https://reactflow.dev/learn/tutorials/getting-started-with-react-flow-components)

* Troubleshooting

  * [Common Errors](https://reactflow.dev/learn/troubleshooting/common-errors)
  * [Remove Attribution](https://reactflow.dev/learn/troubleshooting/remove-attribution)
  * [Migrate to v12](https://reactflow.dev/learn/troubleshooting/migrate-to-v12)
  * [Migrate to v11](https://reactflow.dev/learn/troubleshooting/migrate-to-v11)
  * [Migrate to v10](https://reactflow.dev/learn/troubleshooting/migrate-to-v10)

* [API Reference](https://reactflow.dev/api-reference)

On This Page

* [A basic custom edge](https://reactflow.dev/learn/customization/custom-edges#a-basic-custom-edge)
* [Create the component](https://reactflow.dev/learn/customization/custom-edges#create-the-component)
* [Create `edgeTypes`](https://reactflow.dev/learn/customization/custom-edges#create-edgetypes)
* [Pass the `edgeTypes` prop](https://reactflow.dev/learn/customization/custom-edges#pass-the-edgetypes-prop)
* [Use the new edge type](https://reactflow.dev/learn/customization/custom-edges#use-the-new-edge-type)
* [Flow with a custom edge](https://reactflow.dev/learn/customization/custom-edges#flow-with-a-custom-edge)
* [Custom SVG edge paths](https://reactflow.dev/learn/customization/custom-edges#custom-svg-edge-paths)

[Edit this page on GitHub](https://github.com/xyflow/web/tree/main/sites/reactflow.dev/src/content/learn/customization/custom-edges.mdx)

[Questions? Contact Us](https://xyflow.com/contact)
What's new?

[React Flow 12.10.1](https://reactflow.dev/whats-new/2026-02-19)[React Flow 12.10.0](https://reactflow.dev/whats-new/2025-12-04)[React Flow UI Components updated to React 19 and Tailwind CSS 4](https://reactflow.dev/whats-new/2025-10-28)[...and more!](https://reactflow.dev/whats-new)

### React Flow Playground

Explore different props, options and layout algorithms in our interactive playground

[Launch](https://play.reactflow.dev/)

[Learn](https://reactflow.dev/learn "Learn")[Customization](https://reactflow.dev/learn/customization/custom-nodes "Customization")Edges

Copy page

Custom Edges
============

Like [custom nodes](https://reactflow.dev/learn/customization/custom-nodes), parts of a custom edge in React Flow are just React components. That means you can render anything you want along an edge! This guide shows you how to implement a custom edge with some additional controls. For a comprehensive reference of props available for custom edges, see the [Edge](https://reactflow.dev/api-reference/types/edge-props) reference.

A basic custom edge[](https://reactflow.dev/learn/customization/custom-edges#a-basic-custom-edge)
-------------------------------------------------------------------------------------------------

An edge isn’t much use to us if it doesn’t render a path between two connected nodes. These paths are always SVG-based and are typically rendered using the [`<BaseEdge />`](https://reactflow.dev/api-reference/components/base-edge) component. To calculate the actual SVG path to render, React Flow comes with some handy utility functions:

* [`getBezierPath`](https://reactflow.dev/api-reference/utils/get-bezier-path)
* [`getSimpleBezierPath`](https://reactflow.dev/api-reference/utils/get-simple-bezier-path)
* [`getSmoothStepPath`](https://reactflow.dev/api-reference/utils/get-smooth-step-path)
* [`getStraightPath`](https://reactflow.dev/api-reference/utils/get-straight-path)

To kickstart our custom edge, we’ll just render a straight path between the source and target.

### Create the component[](https://reactflow.dev/learn/customization/custom-edges#create-the-component)

We start by creating a new React component called `CustomEdge`. Then we render the [`<BaseEdge />`](https://reactflow.dev/api-reference/components/base-edge) component with the calculated path. This gives us a straight edge that behaves the same as the built-in default [edge version](https://reactflow.dev/api-reference/types/edge#default-edge-types)`"straight"`.

```
import { BaseEdge, getStraightPath } from '@xyflow/react';
 
export function CustomEdge({ id, sourceX, sourceY, targetX, targetY }) {
  const [edgePath] = getStraightPath({
    sourceX,
    sourceY,
    targetX,
    targetY,
  });
 
  return (
    <>
      <BaseEdge id={id} path={edgePath} />
    </>
  );
}
```

**Using TypeScript?** You can head on over to our [TypeScript guide](https://reactflow.dev/learn/advanced-use/typescript#custom-edges) to learn how to set up your custom edges with the right types. This will make sure you’ll have typed access to your edge’s props and `data`.

### Create `edgeTypes`[](https://reactflow.dev/learn/customization/custom-edges#create-edgetypes)

Outside of our component, we define an `edgeTypes` object. We name our new edge type `"custom-edge"` and assign the `CustomEdge` component we just created to it.

```
const edgeTypes = {
  'custom-edge': CustomEdge,
};
```

### Pass the `edgeTypes` prop[](https://reactflow.dev/learn/customization/custom-edges#pass-the-edgetypes-prop)

To use it, we also need to update the [`edgeTypes`](https://reactflow.dev/api-reference/react-flow#edge-types) prop on the `<ReactFlow />` component.

```
export function Flow() {
  return <ReactFlow edgeTypes={edgeTypes} />;
}
```

### Use the new edge type[](https://reactflow.dev/learn/customization/custom-edges#use-the-new-edge-type)

After defining the `edgeTypes` object, we can use our new custom edge by setting the `type` field of an edge to `"custom-edge"`.

```
const initialEdges = [
  {
    id: 'e1',
    source: 'n1',
    target: 'n2',
    type: 'custom-edge',
  },
];
```

### Flow with a custom edge[](https://reactflow.dev/learn/customization/custom-edges#flow-with-a-custom-edge)

Custom SVG edge paths[](https://reactflow.dev/learn/customization/custom-edges#custom-svg-edge-paths)
-----------------------------------------------------------------------------------------------------

As discussed previously, if you want to make a custom edge in React Flow, you have to use either of the four path creation functions discussed above (e.g [`getBezierPath`](https://reactflow.dev/api-reference/utils/get-bezier-path)). However if you want to make some other path shape like a Sinusoidal edge or some other edge type then you will have to make the edge path yourself.

The edge path we get from functions like [`getBezierPath`](https://reactflow.dev/api-reference/utils/get-bezier-path) is just a path string which we pass into the `path` prop of the `<BaseEdge />` component. It contains the necessary information needed in order to draw that path, like where it should start from, where it should curve, where it should end, etc. A simple straight path string between two points `(x1, y1)` to `(x2, y2)` would look like:

`M x1 y1 L x2 y2`

An SVG path is a concatenated list of commands like `M`, `L`, `Q`, etc, along with their values. Some of these commands are listed below, along with their supported values.

* `M x1 y1` is the Move To command which moves the current point to the x1, y1 coordinate.
* `L x1 y1` is the Line To command which draws a line from the current point to x1, y1 coordinate.
* `Q x1 y1 x2 y2` is the Quadratic Bezier Curve command which draws a bezier curve from the current point to the x2, y2 coordinate. x1, y1 is the control point of the curve which determines the curviness of the curve.

Whenever we want to start a path for our custom edge, we use the `M` command to move our current point to `sourceX, sourceY` which we get as props in the custom edge component. Then based on the shape we want, we will use other commands like `L`(to make lines), `Q`(to make curves) and then finally end our path at `targetX, targetY` which we get as props in the custom edge component.

If you want to learn more about SVG paths, you can check out [SVG-Path-Editor](https://yqnn.github.io/svg-path-editor/). You can paste any SVG path there and analyze individual path commands via an intuitive UI.

Here is an example with two types of custom edge paths, a Step edge and a Sinusoidal edge. You should look at the Step edge first to get your hands dirty with custom SVG paths since it’s simple, and then look at how the Sinusoidal edge is made. After going through this example, you will have the necessary knowledge to make custom SVG paths for your custom edges.

Last updated on February 4, 2026

[Handles](https://reactflow.dev/learn/customization/handles "Handles")[Edge Labels](https://reactflow.dev/learn/customization/edge-labels "Edge Labels")

A project by the xyflow team

We are building and maintaining open source software for node-based UIs since 2019.

Docs

[Getting Started](https://reactflow.dev/learn)[API Reference](https://reactflow.dev/api-reference)[Examples](https://reactflow.dev/examples)[Components](https://reactflow.dev/components)[Showcase](https://reactflow.dev/showcase)[Playground](https://play.reactflow.dev/)

Social

[Discord](https://discord.gg/RVmnytFmGW)[Github](https://github.com/xyflow)[X / Twitter](https://x.com/xyflowdev)[Bluesky](https://bsky.app/profile/xyflow.com)

xyflow

[Blog](https://xyflow.com/blog)[Open Source](https://xyflow.com/open-source)[About](https://xyflow.com/about)[Contact](https://xyflow.com/contact)[Careers](https://xyflow.com/careers)

Legal

[MIT License](https://github.com/xyflow/xyflow/blob/main/LICENSE)[Code of Conduct](https://github.com/xyflow/xyflow/blob/main/CODE_OF_CONDUCT.md)[Imprint](https://xyflow.com/imprint)

[info@xyflow.com](mailto:info@xyflow.com) — Copyright ©2026[webkid GmbH](https://webkid.io/). All rights reserved— website design by[Facu Montanaro](https://facumontanaro.com/)
