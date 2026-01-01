# Core Concepts

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
