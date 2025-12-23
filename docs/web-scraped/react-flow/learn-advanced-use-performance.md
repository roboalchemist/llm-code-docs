# Source: https://reactflow.dev/learn/advanced-use/performance

# Performance 

When dealing with a large number of nodes or complex components, managing performance can be challenging. Here are a few effective strategies to optimize the performance of React Flow.

## Use memoization[](#use-memoization) 

One of the main reasons for performance issues in React Flow is unnecessary re-renders. Since node movements trigger frequent state updates, this can lead to performance bottlenecks, especially in larger diagrams.

### Memoize components[](#memoize-components) 

Components provided as props to the `<ReactFlow>` component, including custom node and edge components, should either be memoized using `React.memo` or declared outside the parent component. This ensures that React does not create a new reference for the component on every render, which would otherwise trigger unnecessary re-renders.

``` 
const NodeComponent = memo(() => </div>;
});
```

### Memoize functions[](#memoize-functions) 

Similarly, functions passed as props to `<ReactFlow>` should be memoized using `useCallback`. This prevents React from creating a new function reference on every render, which could also trigger unnecessary re-renders. Additionally, arrays and objects like `defaultEdgeOptions` or `snapGrid` should be memoized using `useMemo` to prevent unnecessary re-renders.

``` 
import React,  from 'react';
 
const MyDiagram = () => , []);
 
  return <ReactFlow onNodeClick= />;
};
 
export default MyDiagram;
```

## Avoid accessing nodes in components[](#avoid-accessing-nodes-in-components) 

One of the most common performance pitfalls in React Flow is directly accessing the `nodes` or `edges` in the components or the viewport. These objects change frequently during operations like dragging, panning, or zooming, which can cause unnecessary re-renders of components that depend on them.

For example, if you fetch the entire `nodes` array from the store and filter it to display selected node IDs, this approach can lead to performance degradation. Every update to the `nodes` array triggers a re-render of all dependent components, even if the change is unrelated to the selected nodes.

### Inefficient example[](#inefficient-example) 

``` 
const SelectedNodeIds = () => ></div>
      ))}
    </div>
  );
};
```

In this example, every update to the `nodes` array causes the `SelectedNodeIds` component to re-render, even if the selection hasn't changed.

### Optimized solution[](#optimized-solution) 

To avoid unnecessary re-renders, store the selected nodes in a separate field in your state (using Zustand, Redux, or any other state management solution). This ensures that the component only re-renders when the selection changes.

``` 
const SelectedNodeIds = () => ></div>
      ))}
    </div>
  );
};
```

By decoupling the selected nodes from the `nodes` array, you prevent unnecessary updates and improve performance. For more information, view our [State Management guide](/learn/advanced-use/state-management).

## Collapse large node trees[](#collapse-large-node-trees) 

If your node tree is deeply nested, rendering all nodes at once can be inefficient. Instead, show only a limited number of nodes and allow users to expand them as needed. You can do this by modifying the node's `hidden` property dynamically to toggle visibility.

``` 
const handleNodeClick = (targetNode) => 
          : node,
      ),
    );
  }
};
```

By hiding nodes initially and rendering them only when expanded, we optimize performance while maintaining usability.

## Simplify node and edge styles[](#simplify-node-and-edge-styles) 

If you've optimized performance in every other way, and you are still finding performance issues with large numbers of nodes, complex CSS styles, particularly those involving animations, shadows, or gradients, can significantly impact performance. Consider reducing complexity on your node styles in these cases.

## Additional resources[](#additional-resources) 

Here are a few helpful resources on performance in React Flow that you can check out:

- [Guide to Optimize React Flow Project Performance ![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNyIgdmlld2JveD0iMCAwIDI0IDI0IiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6aW5saW5lIHg6YWxpZ24tYmFzZWxpbmUgeDpzaHJpbmstMCI+PHBhdGggZD0iTTcgMTdMMTcgNyIgLz48cGF0aCBkPSJNNyA3aDEwdjEwIiAvPjwvc3ZnPg==)](https://www.synergycodes.com/blog/guide-to-optimize-react-flow-project-performance)
- [Tuning Edge Animations ReactFlow Optimal Performance ![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNyIgdmlld2JveD0iMCAwIDI0IDI0IiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6aW5saW5lIHg6YWxpZ24tYmFzZWxpbmUgeDpzaHJpbmstMCI+PHBhdGggZD0iTTcgMTdMMTcgNyIgLz48cGF0aCBkPSJNNyA3aDEwdjEwIiAvPjwvc3ZnPg==)](https://liambx.com/blog/tuning-edge-animations-reactflow-optimal-performance)
- [5 Ways to Optimize React Flow in 10 minutes ![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNyIgdmlld2JveD0iMCAwIDI0IDI0IiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6aW5saW5lIHg6YWxpZ24tYmFzZWxpbmUgeDpzaHJpbmstMCI+PHBhdGggZD0iTTcgMTdMMTcgNyIgLz48cGF0aCBkPSJNNyA3aDEwdjEwIiAvPjwvc3ZnPg==)](https://www.youtube.com/watch?v=8M2qZ69iM20)