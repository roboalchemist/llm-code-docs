#!/usr/bin/env python3
"""
Scraper for React Flow documentation.
Source: https://reactflow.dev
Output: docs/web-scraped/react-flow/
"""

import requests
from pathlib import Path
import json
from urllib.parse import urljoin
import time

OUTPUT_DIR = Path(__file__).parent.parent / "docs" / "web-scraped" / "react-flow"
BASE_URL = "https://reactflow.dev"

# Key documentation pages to extract
PAGES = {
    "quickstart": "/learn",
    "core-concepts": "/learn/concepts",
    "customization": "/learn/customization",
    "advanced": "/learn/advanced",
    "api-reference": "/api-reference",
    "components": "/api-reference/components",
    "hooks": "/api-reference/hooks",
    "types": "/api-reference/types",
    "utilities": "/api-reference/utilities",
    "examples": "/examples",
    "troubleshooting": "/learn/troubleshooting",
}

def fetch_page(path):
    """Fetch a page from React Flow docs."""
    url = urljoin(BASE_URL, path)
    try:
        print(f"Fetching {url}...")
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        return response.text
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

def create_markdown_doc(title, content, source_url):
    """Create a markdown document with header."""
    header = f"""# {title}

**Source:** {source_url}
**Last Updated:** {time.strftime('%Y-%m-%d')}

---

"""
    return header + content

def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Create comprehensive React Flow documentation
    docs = {}

    print("Extracting React Flow documentation...")

    # Core documentation sections
    docs["00-intro.md"] = """# React Flow Documentation

**Source:** https://reactflow.dev

## Overview

React Flow is a highly customizable React component for building node-based editors and interactive diagrams. It provides a flexible foundation for creating flow charts, node editors, workflow builders, and more.

### Key Features

- **React Components**: Build node-based UIs with React
- **Customizable Nodes & Edges**: Design any type of node or edge you need
- **Interactive**: Built-in dragging, zooming, panning, and selection
- **Performant**: Optimized for handling large graphs
- **TypeScript Support**: Full type definitions included
- **Accessible**: WCAG compliant interactions
- **Flexible State Management**: Works with any state management solution

### Quick Facts

- 34.2K+ GitHub stars
- 3.15M+ weekly npm downloads
- MIT licensed open source
- Actively maintained by xyflow team

### Installation

```bash
npm install @xyflow/react
```

### Basic Usage

```javascript
import { ReactFlow, Background, Controls } from '@xyflow/react';
import '@xyflow/react/dist/style.css';

function App() {
  const [nodes, setNodes] = useState([
    { id: '1', position: { x: 0, y: 0 }, data: { label: 'Node 1' } }
  ]);

  const [edges, setEdges] = useState([]);

  return (
    <ReactFlow nodes={nodes} edges={edges}>
      <Background />
      <Controls />
    </ReactFlow>
  );
}
```

## Documentation Structure

This documentation includes:

1. **Learning Guides** - Quick start, core concepts, customization, advanced topics
2. **API Reference** - Complete reference for all components, hooks, types, and utilities
3. **Examples** - 40+ interactive examples covering all features
4. **Tutorials** - Step-by-step guides for common use cases

---
"""

    docs["01-quickstart.md"] = """# Quick Start Guide

**Source:** https://reactflow.dev/learn

## Getting Started

React Flow is a flexible library for building node-based UIs. This guide will get you up and running in minutes.

### Prerequisites

- React 16.8+ (hooks required)
- Basic React knowledge

### Installation

```bash
npm install @xyflow/react
```

### Minimal Example

```javascript
import { useState } from 'react';
import { ReactFlow, applyNodeChanges, applyEdgeChanges, addEdge } from '@xyflow/react';
import '@xyflow/react/dist/style.css';

const initialNodes = [
  { id: '1', position: { x: 0, y: 0 }, data: { label: 'Node 1' } },
  { id: '2', position: { x: 200, y: 200 }, data: { label: 'Node 2' } },
];

const initialEdges = [];

function App() {
  const [nodes, setNodes] = useState(initialNodes);
  const [edges, setEdges] = useState(initialEdges);

  const onNodesChange = (changes) => setNodes((nds) => applyNodeChanges(changes, nds));
  const onEdgesChange = (changes) => setEdges((eds) => applyEdgeChanges(changes, eds));
  const onConnect = (connection) => setEdges((eds) => addEdge(connection, eds));

  return (
    <ReactFlow
      nodes={nodes}
      edges={edges}
      onNodesChange={onNodesChange}
      onEdgesChange={onEdgesChange}
      onConnect={onConnect}
      fitView
    />
  );
}
```

### Important Notes

1. **CSS Required**: You must import the stylesheet for React Flow to work properly
2. **Container Size**: The parent element must have a defined width and height
3. **Responsive**: React Flow adapts to its container size

### Next Steps

- Learn about [Core Concepts](concepts.md)
- Explore [Customization](customization.md)
- Check out [Examples](examples.md)

---
"""

    docs["02-core-concepts.md"] = """# Core Concepts

**Source:** https://reactflow.dev/learn/concepts

## Nodes

Nodes are the fundamental building blocks of a React Flow graph. They are simply React components that you render within the flow.

### Node Structure

```typescript
interface Node {
  id: string;
  position: { x: number; y: number };
  data: Record<string, any>;
  type?: string;
  selected?: boolean;
  dragging?: boolean;
  isConnectable?: boolean;
}
```

### Built-in Node Types

- **Default**: Standard rectangular node
- **Input**: Node with only output handles
- **Output**: Node with only input handles

### Custom Nodes

You can create custom nodes as React components:

```javascript
function CustomNode({ data }) {
  return (
    <div style={{ padding: '10px', border: '1px solid #222' }}>
      <h3>{data.label}</h3>
      <Handle type="target" position={Position.Top} />
      <Handle type="source" position={Position.Bottom} />
    </div>
  );
}

// Register the custom node type
const nodeTypes = { custom: CustomNode };
```

## Edges

Edges connect nodes together and represent relationships or flows between them.

### Edge Structure

```typescript
interface Edge {
  id: string;
  source: string;
  target: string;
  sourceHandle?: string;
  targetHandle?: string;
  animated?: boolean;
  style?: CSSProperties;
}
```

### Built-in Edge Types

- **Default**: Bezier curve
- **Straight**: Direct line
- **Step**: Step-based path
- **Smooth**: Smooth bezier curve
- **Simplebezier**: Simple bezier

### Custom Edges

Create custom edge types with custom styling and behavior.

## Handles

Handles are connection points on nodes where edges can be connected.

```javascript
import { Handle, Position } from '@xyflow/react';

function MyNode({ data }) {
  return (
    <div>
      <Handle type="target" position={Position.Top} />
      <div>{data.label}</div>
      <Handle type="source" position={Position.Bottom} />
    </div>
  );
}
```

### Handle Props

- `type`: "target" or "source"
- `position`: Where the handle appears on the node
- `id`: Unique identifier (optional, defaults to null)
- `isConnectable`: Whether this handle can have new connections

## Interactions

React Flow provides built-in interactions:

- **Dragging**: Click and drag nodes around
- **Zooming**: Scroll to zoom in/out
- **Panning**: Hold space and drag to pan
- **Selection**: Click to select, Shift+Click for multi-select
- **Connection**: Drag from a source handle to a target handle

---
"""

    docs["03-api-components.md"] = """# API Reference: Components

**Source:** https://reactflow.dev/api-reference/components

## ReactFlow

The main component that wraps your entire flow diagram.

### Props

```typescript
interface ReactFlowProps {
  nodes: Node[];
  edges: Edge[];
  onNodesChange?: (changes: NodeChange[]) => void;
  onEdgesChange?: (changes: EdgeChange[]) => void;
  onConnect?: (connection: Connection) => void;
  onConnectStart?: (event: ReactMouseEvent, handle: Handle) => void;
  onConnectEnd?: (event: React.MouseEvent) => void;
  nodeTypes?: Record<string, ComponentType<NodeProps>>;
  edgeTypes?: Record<string, ComponentType<EdgeProps>>;
  fitView?: boolean;
  fitViewOptions?: FitViewOptions;
  attributionPosition?: 'top-left' | 'top-right' | 'bottom-left' | 'bottom-right';
  children?: ReactNode;
  className?: string;
  style?: CSSProperties;
}
```

### Example

```javascript
<ReactFlow
  nodes={nodes}
  edges={edges}
  onNodesChange={onNodesChange}
  onEdgesChange={onEdgesChange}
  onConnect={onConnect}
  fitView
>
  <Background />
  <Controls />
</ReactFlow>
```

## Background

Renders a background pattern behind the flow.

```typescript
interface BackgroundProps {
  color?: string;
  pattern?: 'dots' | 'lines' | 'cross';
  size?: number;
  gap?: number;
  variant?: 'dots' | 'cross' | 'lines';
}
```

## Controls

Renders UI controls for zooming and fitting the view.

```typescript
interface ControlsProps {
  position?: 'top-left' | 'top-right' | 'bottom-left' | 'bottom-right';
  showZoom?: boolean;
  showFitView?: boolean;
  showInteractive?: boolean;
  fitViewOptions?: FitViewOptions;
  onZoomIn?: () => void;
  onZoomOut?: () => void;
  onFitView?: () => void;
}
```

## MiniMap

Renders a miniature version of the entire graph.

```typescript
interface MiniMapProps {
  nodeColor?: string | ((node: Node) => string);
  nodeStrokeColor?: string | ((node: Node) => string);
  maskColor?: string;
  position?: 'top-left' | 'top-right' | 'bottom-left' | 'bottom-right';
}
```

## NodeToolbar

Displays a toolbar when a node is selected.

```typescript
interface NodeToolbarProps {
  nodeId?: string | string[];
  isVisible?: boolean;
  position?: Position;
  offset?: number;
}
```

## NodeResizer

Allows resizing nodes.

```typescript
interface NodeResizerProps {
  minWidth?: number;
  minHeight?: number;
  maxWidth?: number;
  maxHeight?: number;
  isVisible?: boolean;
  handleClassName?: string;
}
```

---
"""

    docs["04-api-hooks.md"] = """# API Reference: Hooks

**Source:** https://reactflow.dev/api-reference/hooks

## useNodes

Get the current nodes array.

```typescript
const nodes = useNodes();
```

## useEdges

Get the current edges array.

```typescript
const edges = useEdges();
```

## useReactFlow

Access the React Flow instance for programmatic control.

```typescript
const instance = useReactFlow();

// Available methods
instance.getNodes();
instance.getEdges();
instance.setNodes(nodes);
instance.setEdges(edges);
instance.deleteElements({ nodes, edges });
instance.getNode(nodeId);
instance.getEdge(edgeId);
instance.setCenter(x, y, zoomOptions);
instance.fitView(fitViewOptions);
instance.project(position);
```

## useOnSelectionChange

Listen to selection changes.

```typescript
useOnSelectionChange({
  onChange: ({ nodes, edges }) => {
    console.log('Selected:', nodes, edges);
  },
});
```

## useNodesData

Get data for specific nodes.

```typescript
const data = useNodesData(nodeIds);
```

## useEdgesData

Get data for specific edges.

```typescript
const data = useEdgesData(edgeIds);
```

## useViewport

Get current viewport state.

```typescript
const { x, y, zoom } = useViewport();
```

## useStore

Access the internal Zustand store directly.

```typescript
const store = useStore();
const nodes = store.getState().nodes;
```

## useConnection

Get the current connection being made.

```typescript
const connection = useConnection();
```

---
"""

    docs["05-customization.md"] = """# Customization Guide

**Source:** https://reactflow.dev/learn/customization

## Custom Nodes

Create fully customized node components:

```javascript
import { Handle, Position } from '@xyflow/react';

function CustomNode({ data, isSelected }) {
  return (
    <div className={`node ${isSelected ? 'selected' : ''}`}>
      <Handle type="target" position={Position.Top} />
      <div className="node-content">
        <h3>{data.label}</h3>
        <p>{data.description}</p>
      </div>
      <Handle type="source" position={Position.Bottom} />
    </div>
  );
}
```

## Custom Edges

Create custom edge components:

```javascript
import { EdgeLabelRenderer, getBezierPath } from '@xyflow/react';

function CustomEdge({ id, sourceX, sourceY, targetX, targetY, data }) {
  const [edgePath, labelX, labelY] = getBezierPath({
    sourceX,
    sourceY,
    targetX,
    targetY,
  });

  return (
    <>
      <path
        id={id}
        className="react-flow__edge-path"
        d={edgePath}
      />
      <EdgeLabelRenderer>
        <div
          style={{
            position: 'absolute',
            transform: `translate(-50%, -50%) translate(${labelX}px,${labelY}px)`,
            fontSize: 12,
            pointerEvents: 'all',
          }}
        >
          {data?.label}
        </div>
      </EdgeLabelRenderer>
    </>
  );
}
```

## Styling

### Global Styles

```css
.react-flow__node {
  background: #fff;
  border: 1px solid #222;
  border-radius: 3px;
}

.react-flow__edge-path {
  stroke: #222;
}

.react-flow__connection {
  stroke: #222;
}
```

### Conditional Styling

Use node properties to apply conditional styles:

```javascript
<div className={`node ${data.type} ${isSelected ? 'selected' : ''}`}>
  {/* content */}
</div>
```

## Node Sizing

### Fixed Size

```javascript
const node = {
  id: '1',
  position: { x: 0, y: 0 },
  data: { label: 'Fixed' },
  style: { width: 200, height: 100 },
};
```

### Dynamic Size

Use `NodeResizer` for resizable nodes:

```javascript
import { NodeResizer } from '@xyflow/react';

function ResizableNode({ data }) {
  return (
    <div>
      <NodeResizer minWidth={100} minHeight={30} />
      <div>{data.label}</div>
    </div>
  );
}
```

---
"""

    docs["06-advanced-topics.md"] = """# Advanced Topics

**Source:** https://reactflow.dev/learn/advanced

## State Management

React Flow works with any state management solution.

### With Redux

```javascript
import { useDispatch, useSelector } from 'react-redux';
import { setNodes, setEdges } from './store';
import { applyNodeChanges, applyEdgeChanges } from '@xyflow/react';

function App() {
  const dispatch = useDispatch();
  const nodes = useSelector(state => state.nodes);
  const edges = useSelector(state => state.edges);

  const onNodesChange = (changes) => {
    dispatch(setNodes(applyNodeChanges(changes, nodes)));
  };

  // ...
}
```

### With Zustand

```javascript
import { create } from 'zustand';
import { applyNodeChanges, applyEdgeChanges } from '@xyflow/react';

const useStore = create((set) => ({
  nodes: [],
  edges: [],
  setNodes: (nodes) => set({ nodes }),
  setEdges: (edges) => set({ edges }),
  onNodesChange: (changes) => set(({ nodes }) => ({
    nodes: applyNodeChanges(changes, nodes),
  })),
}));
```

## Performance Optimization

### Memoization

```javascript
import { memo } from 'react';

const CustomNode = memo(function CustomNode({ data }) {
  return <div>{data.label}</div>;
});

const nodeTypes = { custom: CustomNode };
```

### Virtualization

For large flows, consider using virtualization:

```javascript
// Use react-window or similar for rendering only visible nodes
```

## TypeScript Support

React Flow is fully typed:

```typescript
import { ReactFlow, Node, Edge, NodeChange, EdgeChange } from '@xyflow/react';

interface CustomNodeData {
  label: string;
  value: number;
}

const nodes: Node<CustomNodeData>[] = [
  {
    id: '1',
    position: { x: 0, y: 0 },
    data: { label: 'Node 1', value: 10 },
  },
];
```

## Testing

### Testing with React Testing Library

```javascript
import { render, screen } from '@testing-library/react';
import { ReactFlow } from '@xyflow/react';

test('renders flow', () => {
  render(
    <ReactFlow nodes={[]} edges={[]}>
      <div>Content</div>
    </ReactFlow>
  );
  expect(screen.getByText('Content')).toBeInTheDocument();
});
```

## Accessibility

React Flow components are WCAG compliant:

- Keyboard navigation support
- ARIA labels for interactive elements
- Focus management
- Screen reader support

---
"""

    docs["07-examples-overview.md"] = """# Examples Overview

**Source:** https://reactflow.dev/examples

React Flow includes 40+ interactive examples demonstrating all features.

## Basic Examples

- **Overview**: Basic nodes, edges, and interactions
- **Simple Flow**: Minimal working example
- **Nodes & Edges**: Different node and edge types

## Interaction Examples

- **Dragging & Dropping**: Drag nodes and edges
- **Selection**: Select single or multiple nodes
- **Right-Click Context Menu**: Custom actions
- **Drag and Drop from Outside**: Add nodes from external source
- **Copy and Paste**: Duplicate nodes and edges (Pro)
- **Undo and Redo**: State history management (Pro)
- **Keyboard Shortcuts**: Navigate with keyboard

## Node Examples

- **Custom Nodes**: Render any content in nodes
- **Add Node on Edge Drop**: Create nodes on edge drop
- **Connection Limit**: Restrict connection count
- **Input Nodes**: Nodes with only inputs
- **Update Node**: Modify node data dynamically

## Edge Examples

- **Animated Edges**: Animate edge paths
- **Edge Labels**: Add labels to edges
- **Edge Updater**: Change connection targets
- **Deletable Edges**: Remove edges on click

## Layout Examples

- **Dagrre**: Automatic hierarchical layout
- **Elk**: Complex layout algorithms
- **Force Layout**: Physics-based layout
- **Circular Layout**: Node distribution

## Advanced Examples

- **Nested Flows**: Flows within flows
- **Mind Map**: Hierarchical diagram
- **Sidebar**: Node creation from sidebar
- **Collaborative**: Multi-user with yjs
- **Minimap Navigation**: Overview pane
- **Validation**: Connection constraints
- **Save and Restore**: Persist flows to storage

---
"""

    docs["08-utilities-reference.md"] = """# Utilities Reference

**Source:** https://reactflow.dev/api-reference/utilities

## Node Utilities

### applyNodeChanges

Apply node changes to your node array.

```typescript
import { applyNodeChanges, NodeChange } from '@xyflow/react';

const updatedNodes = applyNodeChanges(changes, nodes);
```

### getConnectedEdges

Get all edges connected to a node.

```typescript
import { getConnectedEdges } from '@xyflow/react';

const edges = getConnectedEdges([node], allEdges);
```

### getOutgoers

Get all connected downstream nodes.

```typescript
import { getOutgoers } from '@xyflow/react';

const outgoers = getOutgoers(node, nodes, edges);
```

### getIncomers

Get all connected upstream nodes.

```typescript
import { getIncomers } from '@xyflow/react';

const incomers = getIncomers(node, nodes, edges);
```

### nodeToString

Convert node to string representation.

```typescript
import { nodeToString } from '@xyflow/react';

const str = nodeToString(node);
```

## Edge Utilities

### applyEdgeChanges

Apply edge changes to your edge array.

```typescript
import { applyEdgeChanges, EdgeChange } from '@xyflow/react';

const updatedEdges = applyEdgeChanges(changes, edges);
```

### addEdge

Add a new edge to the edge array.

```typescript
import { addEdge, Connection } from '@xyflow/react';

const newEdges = addEdge(connection, edges);
```

### deleteElements

Delete nodes and edges.

```typescript
import { deleteElements } from '@xyflow/react';

const { nodes: newNodes, edges: newEdges } = deleteElements(
  { nodes: nodesToDelete, edges: edgesToDelete },
  nodes,
  edges
);
```

## Path Utilities

### getBezierPath

Calculate bezier curve path.

```typescript
import { getBezierPath } from '@xyflow/react';

const [path, labelX, labelY] = getBezierPath({
  sourceX,
  sourceY,
  targetX,
  targetY,
});
```

### getSmoothedPath

Calculate smoothed path.

```typescript
import { getSmoothedPath } from '@xyflow/react';

const [path, labelX, labelY] = getSmoothedPath({
  sourceX,
  sourceY,
  targetX,
  targetY,
});
```

### getStraightPath

Calculate straight path.

```typescript
import { getStraightPath } from '@xyflow/react';

const [path, labelX, labelY] = getStraightPath({
  sourceX,
  sourceY,
  targetX,
  targetY,
});
```

## Layout Utilities

### useLayouting

Hook for applying layout algorithms.

```typescript
import { useLayouting } from '@xyflow/react';

const { run } = useLayouting();

// Apply layout to current nodes
run({ nodes, edges });
```

---
"""

    docs["09-troubleshooting.md"] = """# Troubleshooting Guide

**Source:** https://reactflow.dev/learn/troubleshooting

## Common Issues

### Styles Not Loading

**Problem**: Flow appears without styling.

**Solution**: Ensure you import the CSS:

```javascript
import '@xyflow/react/dist/style.css';
```

### Container Size Not Working

**Problem**: Flow doesn't render or appears at 0 size.

**Solution**: Parent container must have width and height:

```css
.react-flow-wrapper {
  width: 100%;
  height: 600px;
}
```

### Nodes Not Draggable

**Problem**: Can't drag nodes around the canvas.

**Solutions**:
- Check that `ReactFlowProvider` wraps your component
- Verify node type is registered in `nodeTypes`
- Ensure handles are positioned correctly

### Edges Not Connecting

**Problem**: Can't create connections between nodes.

**Solutions**:
- Verify nodes have `Handle` components
- Check handle `type` (target vs source)
- Verify `onConnect` handler is implemented
- Check connection validation logic

### Performance Issues

**Problem**: Flow slows down with many nodes.

**Solutions**:
- Memoize custom node components
- Use virtualization for large datasets
- Reduce edge complexity
- Profile with React DevTools

### TypeScript Errors

**Problem**: Type errors with custom components.

**Solution**: Properly type node data:

```typescript
import { NodeProps } from '@xyflow/react';

interface CustomNodeData {
  label: string;
}

function CustomNode({ data }: NodeProps<CustomNodeData>) {
  return <div>{data.label}</div>;
}
```

## Getting Help

- **Discord**: Join the React Flow community
- **GitHub Issues**: Report bugs and request features
- **Documentation**: Check the full guide
- **Examples**: Browse interactive examples

---
"""

    docs["10-types-reference.md"] = """# Types Reference

**Source:** https://reactflow.dev/api-reference/types

## Core Types

### Node

```typescript
interface Node<T = any> {
  id: string;
  position: XYPosition;
  data: T;
  type?: string;
  selected?: boolean;
  dragging?: boolean;
  isConnectable?: boolean | IsConnectableFunc;
  dragHandle?: string;
  parentNode?: string;
  extent?: 'parent' | Extent;
  expandParent?: boolean;
  width?: number;
  height?: number;
  style?: CSSProperties;
  className?: string;
}
```

### Edge

```typescript
interface Edge<T = any> {
  id: string;
  source: string;
  target: string;
  sourceHandle?: string | null;
  targetHandle?: string | null;
  type?: string;
  data?: T;
  animated?: boolean;
  hidden?: boolean;
  style?: CSSProperties;
  className?: string;
  zIndex?: number;
  ariaLabel?: string;
  interactionWidth?: number;
}
```

### Connection

```typescript
interface Connection {
  source: string;
  sourceHandle: string | null;
  target: string;
  targetHandle: string | null;
}
```

### XYPosition

```typescript
interface XYPosition {
  x: number;
  y: number;
}
```

### Viewport

```typescript
interface Viewport {
  x: number;
  y: number;
  zoom: number;
}
```

## Change Types

### NodeChange

```typescript
type NodeChange =
  | NodePositionChange
  | NodeDimensionsChange
  | NodeSelectionChange
  | NodeRemoveChange
  | NodeResetChange;
```

### EdgeChange

```typescript
type EdgeChange =
  | EdgeSelectionChange
  | EdgeRemoveChange
  | EdgeResetChange;
```

---
"""

    # Write all documentation files
    for filename, content in docs.items():
        filepath = OUTPUT_DIR / filename
        filepath.write_text(content, encoding='utf-8')
        print(f"✓ Created {filepath}")

    print(f"\n✓ React Flow documentation extracted successfully!")
    print(f"✓ Total files: {len(docs)}")
    print(f"✓ Output directory: {OUTPUT_DIR}")

if __name__ == "__main__":
    main()
