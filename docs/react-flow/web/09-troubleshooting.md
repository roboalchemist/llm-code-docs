# Troubleshooting Guide

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
