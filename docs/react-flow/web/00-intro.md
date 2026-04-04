# React Flow Documentation

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
