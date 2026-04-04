# Customization Guide

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
