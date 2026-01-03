# Quick Start Guide

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
