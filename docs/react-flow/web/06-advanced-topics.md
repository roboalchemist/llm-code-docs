# Advanced Topics

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
