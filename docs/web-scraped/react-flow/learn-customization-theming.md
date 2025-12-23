# Source: https://reactflow.dev/learn/customization/theming

# Theming 

React Flow has been built with deep customization in mind. Many of our users fully transform the look and feel of React Flow to match their own brand or design system. This guide will introduce you to the different ways you can customize React Flow's appearance.

## Default styles[](#default-styles) 

React Flow's default styles are enough to get going with the built-in nodes. They provide some sensible defaults for styles like padding, border radius, and animated edges. You can see what they look like below:

App.tsx

index.css

index.tsx

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9Im5vbmUiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBhcmlhLWhpZGRlbj0idHJ1ZSIgZGF0YS1zbG90PSJpY29uIiBjbGFzcz0ic2l6ZS01IHN0cm9rZS0yIj48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xNS42NjYgMy44ODhBMi4yNSAyLjI1IDAgMCAwIDEzLjUgMi4yNWgtM2MtMS4wMyAwLTEuOS42OTMtMi4xNjYgMS42MzhtNy4zMzIgMGMuMDU1LjE5NC4wODQuNC4wODQuNjEydjBhLjc1Ljc1IDAgMCAxLS43NS43NUg5YS43NS43NSAwIDAgMS0uNzUtLjc1djBjMC0uMjEyLjAzLS40MTguMDg0LS42MTJtNy4zMzIgMGMuNjQ2LjA0OSAxLjI4OC4xMSAxLjkyNy4xODQgMS4xLjEyOCAxLjkwNyAxLjA3NyAxLjkwNyAyLjE4NVYxOS41YTIuMjUgMi4yNSAwIDAgMS0yLjI1IDIuMjVINi43NUEyLjI1IDIuMjUgMCAwIDEgNC41IDE5LjVWNi4yNTdjMC0xLjEwOC44MDYtMi4wNTcgMS45MDctMi4xODVhNDguMjA4IDQ4LjIwOCAwIDAgMSAxLjkyNy0uMTg0IiAvPjwvc3ZnPg==)

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9Im5vbmUiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBhcmlhLWhpZGRlbj0idHJ1ZSIgZGF0YS1zbG90PSJpY29uIiBjbGFzcz0ic2l6ZS02Ij48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xNy4yNSA2Ljc1IDIyLjUgMTJsLTUuMjUgNS4yNW0tMTAuNSAwTDEuNSAxMmw1LjI1LTUuMjVtNy41LTMtNC41IDE2LjUiIC8+PC9zdmc+)

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9Im5vbmUiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBhcmlhLWhpZGRlbj0idHJ1ZSIgZGF0YS1zbG90PSJpY29uIiBjbGFzcz0ic2l6ZS01IHN0cm9rZS0yIj48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xNi4wMjMgOS4zNDhoNC45OTJ2LS4wMDFNMi45ODUgMTkuNjQ0di00Ljk5Mm0wIDBoNC45OTJtLTQuOTkzIDAgMy4xODEgMy4xODNhOC4yNSA4LjI1IDAgMCAwIDEzLjgwMy0zLjdNNC4wMzEgOS44NjVhOC4yNSA4LjI1IDAgMCAxIDEzLjgwMy0zLjdsMy4xODEgMy4xODJtMC00Ljk5MXY0Ljk5IiAvPjwvc3ZnPg==)

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0ic2l6ZS00IGZpbGwtc2xhdGUtNzAwIHN0cm9rZS1zbGF0ZS03MDAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgdmlld2JveD0iMCAwIDU2IDc4Ij48cGF0aCBkPSJNMjMuNDI3MyA0OC4yODUzQzIzLjc5MzEgNDcuNTg0NSAyMy4wNjE0IDQ2Ljg4MzcgMjIuMzI5OCA0Ni44ODM3SDEuMTEyMjhDMC4wMTQ4MjI0IDQ2Ljg4MzcgLTAuMzUwOTk3IDQ1LjgzMjYgMC4zODA2NDIgNDUuMTMxOEw0MC45ODY2IDAuMjgyMDg0QzQxLjcxODIgLTAuNDE4NjkzIDQzLjE4MTUgMC4yODIwODQgNDIuODE1NyAxLjMzMzI1TDMyLjkzODYgMzAuMDY1MUMzMi41NzI3IDMwLjc2NTkgMzIuOTM4NiAzMS40NjY2IDMzLjY3MDIgMzEuNDY2Nkg1NC44ODc3QzU1Ljk4NTIgMzEuNDY2NiA1Ni4zNTEgMzIuNTE3OCA1NS42MTk0IDMzLjIxODZMMTUuMDEzNCA3Ny43MTc5QzE0LjI4MTggNzguNDE4NyAxMi44MTg1IDc3LjcxNzkgMTMuMTg0MyA3Ni42NjY3TDIzLjQyNzMgNDguMjg1M1oiIC8+PC9zdmc+)

``` 
import React,  from 'react';
import  from '@xyflow/react';
 
import '@xyflow/react/dist/style.css';
 
 
const nodeDefaults = ;
 
const initialNodes = [
  ,
    data: ,
    ...nodeDefaults,
  },
  ,
    data: ,
    ...nodeDefaults,
  },
  ,
    data: ,
    ...nodeDefaults,
  },
  ,
    data: ,
    ...nodeDefaults,
  },
];
 
const initialEdges = [
  ,
  ,
  ,
];
 
const Flow = () => 
      edges=
      onNodesChange=
      onEdgesChange=
      onConnect=
      fitView
    >
      <Background />
      <Controls />
      <MiniMap />
    </ReactFlow>
  );
};
 
export default Flow;
```

You'll typically load these default styles by importing them in you `App.jsx` file or other entry point:

``` 
import '@xyflow/react/dist/style.css';
```

Without dipping into [custom nodes](/examples/nodes/custom-node) and [edges](/examples/edges/custom-edges), there are three ways you can style React Flow's basic look:

- Passing inline styles through `style` props
- Overriding the built-in classes with custom CSS
- Overriding the CSS variables React Flow uses

### Built in dark and light mode[](#built-in-dark-and-light-mode) 

You can choose one of the built-in color modes by using the `colorMode` prop ('dark', 'light' or 'system') as seen in the [dark mode example](/examples/styling/dark-mode).

``` 
import ReactFlow from '@xyflow/react';
 
export default function Flow()  edges= />
}
```

When you use the `colorMode` prop, React Flow adds a class to the root element (`.react-flow`) that you can use to style your flow based on the color mode:

``` 
.dark .react-flow__node 
 
.light .react-flow__node 
```

### Customizing with `style` props[](#customizing-with-style-props) 

The easiest way to start customizing the look and feel of your flows is to use the `style` prop found on many of React Flow's components to inline your own CSS.

``` 
import ReactFlow from '@xyflow/react'
 
const styles = ;
 
export default function Flow()  nodes= edges= />
}
```

### CSS variables[](#css-variables) 

If you don't want to replace the default styles entirely but just want to tweak the overall look and feel, you can override some of the CSS variables we use throughout the library. For an example of how to use these CSS variables, check out our [Feature Overview](/examples/overview) example.

These variables are mostly self-explanatory. Below is a table of all the variables you might want to tweak and their default values for reference:

  Variable name                                                                   Default
  ------------------------------------------------------------------------------- -------------------------------------------------------------
  `--xy-edge-stroke-default`                              `#b1b1b7`
  `--xy-edge-stroke-width-default`                        `1`
  `--xy-edge-stroke-selected-default`                     `#555`
  `--xy-connectionline-stroke-default`                    `#b1b1b7`
  `--xy-connectionline-stroke-width-default`              `1`
  `--xy-attribution-background-color-default`             `rgba(255, 255, 255, 0.5)`
  `--xy-minimap-background-color-default`                 `#fff`
  `--xy-background-pattern-dots-color-default`            `#91919a`
  `--xy-background-pattern-line-color-default`            `#eee`
  `--xy-background-pattern-cross-color-default`           `#e2e2e2`
  `--xy-node-color-default`                               `inherit`
  `--xy-node-border-default`                              `1px solid #1a192b`
  `--xy-node-background-color-default`                    `#fff`
  `--xy-node-group-background-color-default`              `rgba(240, 240, 240, 0.25)`
  `--xy-node-boxshadow-hover-default`                     `0 1px 4px 1px rgba(0, 0, 0, 0.08)`
  `--xy-node-boxshadow-selected-default`                  `0 0 0 0.5px #1a192b`
  `--xy-handle-background-color-default`                  `#1a192b`
  `--xy-handle-border-color-default`                      `#fff`
  `--xy-selection-background-color-default`               `rgba(0, 89, 220, 0.08)`
  `--xy-selection-border-default`                         `1px dotted rgba(0, 89, 220, 0.8)`
  `--xy-controls-button-background-color-default`         `#fefefe`
  `--xy-controls-button-background-color-hover-default`   `#f4f4f4`
  `--xy-controls-button-color-default`                    `inherit`
  `--xy-controls-button-color-hover-default`              `inherit`
  `--xy-controls-button-border-color-default`             `#eee`
  `--xy-controls-box-shadow-default`                      `0 0 2px 1px rgba(0, 0, 0, 0.08)`
  `--xy-resize-background-color-default`                  `#3367d9`

These variables are used to define the *defaults* for the various elements of React Flow. This means they can still be overridden by inline styles or custom classes on a per-element basis. If you want to override these variables, you can do so by adding:

``` 
.react-flow 
```

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGZpbGw9ImN1cnJlbnRDb2xvciIgaGVpZ2h0PSIuOGVtIiBjbGFzcz0ieDptdC1bLjNlbV0iPjxwYXRoIGQ9Ik02LjQ1NyAxLjA0N2MuNjU5LTEuMjM0IDIuNDI3LTEuMjM0IDMuMDg2IDBsNi4wODIgMTEuMzc4QTEuNzUgMS43NSAwIDAgMSAxNC4wODIgMTVIMS45MThhMS43NSAxLjc1IDAgMCAxLTEuNTQzLTIuNTc1Wm0xLjc2My43MDdhLjI1LjI1IDAgMCAwLS40NCAwTDEuNjk4IDEzLjEzMmEuMjUuMjUgMCAwIDAgLjIyLjM2OGgxMi4xNjRhLjI1LjI1IDAgMCAwIC4yMi0uMzY4Wm0uNTMgMy45OTZ2Mi41YS43NS43NSAwIDAgMS0xLjUgMHYtMi41YS43NS43NSAwIDAgMSAxLjUgMFpNOSAxMWExIDEgMCAxIDEtMiAwIDEgMSAwIDAgMSAyIDBaIiAvPjwvc3ZnPg==)

Be aware that these variables are defined under `.react-flow` and under `:root`.

### Overriding built-in classes[](#overriding-built-in-classes) 

Some consider heavy use of inline styles to be an anti-pattern. In that case, you can override the built-in classes that React Flow uses with your own CSS. There are many classes attached to all sorts of elements in React Flow, but the ones you'll likely want to override are listed below:

  Class name                                                   Description
  ------------------------------------------------------------ -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  `.react-flow`                        The outermost container
  `.react-flow__renderer`              The inner container
  `.react-flow__zoompane`              Zoom & pan pane
  `.react-flow__selectionpane`         Selection pane
  `.react-flow__selection`             User selection
  `.react-flow__edges`                 The element containing all edges in the flow
  `.react-flow__edge`                  Applied to each [`Edge`](/api-reference/types/edge) in the flow
  `.react-flow__edge.selected`         Added to an [`Edge`](/api-reference/types/edge) when selected
  `.react-flow__edge.animated`         Added to an [`Edge`](/api-reference/types/edge) when its `animated` prop is `true`
  `.react-flow__edge.updating`         Added to an [`Edge`](/api-reference/types/edge) while it gets updated via `onReconnect`
  `.react-flow__edge-path`             The SVG `<path />` element of an [`Edge`](/api-reference/types/edge)
  `.react-flow__edge-text`             The SVG `<text />` element of an [`Edge`](/api-reference/types/edge) label
  `.react-flow__edge-textbg`           The SVG `<text />` element behind an [`Edge`](/api-reference/types/edge) label
  `.react-flow__connection`            Applied to the current connection line
  `.react-flow__connection-path`       The SVG `<path />` of a connection line
  `.react-flow__nodes`                 The element containing all nodes in the flow
  `.react-flow__node`                  Applied to each [`Node`](/api-reference/types/node) in the flow
  `.react-flow__node.selected`         Added to a [`Node`](/api-reference/types/node) when selected.
  `.react-flow__node-default`          Added when [`Node`](/api-reference/types/node) type is `"default"`
  `.react-flow__node-input`            Added when [`Node`](/api-reference/types/node) type is `"input"`
  `.react-flow__node-output`           Added when [`Node`](/api-reference/types/node) type is `"output"`
  `.react-flow__nodesselection`        Nodes selection
  `.react-flow__nodesselection-rect`   Nodes selection rect
  `.react-flow__handle`                Applied to each [`<Handle />`](/api-reference/components/handle) component
  `.react-flow__handle-top`            Applied when a handle's [`Position`](/api-reference/types/position) is set to `"top"`
  `.react-flow__handle-right`          Applied when a handle's [`Position`](/api-reference/types/position) is set to `"right"`
  `.react-flow__handle-bottom`         Applied when a handle's [`Position`](/api-reference/types/position) is set to `"bottom"`
  `.react-flow__handle-left`           Applied when a handle's [`Position`](/api-reference/types/position) is set to `"left"`
  `.connectingfrom`                    Added to a Handle when a connection line is above a handle.
  `.connectingto`                      Added to a Handle when a connection line is above a handle.
  `.valid`                             Added to a Handle when a connection line is above **and** the connection is valid
  `.react-flow__background`            Applied to the [`<Background />`](/api-reference/components/background) component
  `.react-flow__minimap`               Applied to the [`<MiniMap />`](/api-reference/components/minimap) component
  `.react-flow__controls`              Applied to the [`<Controls />`](/api-reference/components/controls) component

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGZpbGw9ImN1cnJlbnRDb2xvciIgaGVpZ2h0PSIuOGVtIiBjbGFzcz0ieDptdC1bLjNlbV0iPjxwYXRoIGQ9Ik02LjQ1NyAxLjA0N2MuNjU5LTEuMjM0IDIuNDI3LTEuMjM0IDMuMDg2IDBsNi4wODIgMTEuMzc4QTEuNzUgMS43NSAwIDAgMSAxNC4wODIgMTVIMS45MThhMS43NSAxLjc1IDAgMCAxLTEuNTQzLTIuNTc1Wm0xLjc2My43MDdhLjI1LjI1IDAgMCAwLS40NCAwTDEuNjk4IDEzLjEzMmEuMjUuMjUgMCAwIDAgLjIyLjM2OGgxMi4xNjRhLjI1LjI1IDAgMCAwIC4yMi0uMzY4Wm0uNTMgMy45OTZ2Mi41YS43NS43NSAwIDAgMS0xLjUgMHYtMi41YS43NS43NSAwIDAgMSAxLjUgMFpNOSAxMWExIDEgMCAxIDEtMiAwIDEgMSAwIDAgMSAyIDBaIiAvPjwvc3ZnPg==)

Be careful if you go poking around the source code looking for other classes to override. Some classes are used internally and are required in order for the library to be functional. If you replace them you may end up with unexpected bugs or errors!

## Third-party solutions[](#third-party-solutions) 

You can choose to opt-out of React Flow's default styling altogether and use a third-party styling solution instead. If you want to do this, you must make sure you still import the base styles.

``` 
import '@xyflow/react/dist/base.css';
```

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGZpbGw9ImN1cnJlbnRDb2xvciIgaGVpZ2h0PSIuOGVtIiBjbGFzcz0ieDptdC1bLjNlbV0iPjxwYXRoIGQ9Ik02LjQ1NyAxLjA0N2MuNjU5LTEuMjM0IDIuNDI3LTEuMjM0IDMuMDg2IDBsNi4wODIgMTEuMzc4QTEuNzUgMS43NSAwIDAgMSAxNC4wODIgMTVIMS45MThhMS43NSAxLjc1IDAgMCAxLTEuNTQzLTIuNTc1Wm0xLjc2My43MDdhLjI1LjI1IDAgMCAwLS40NCAwTDEuNjk4IDEzLjEzMmEuMjUuMjUgMCAwIDAgLjIyLjM2OGgxMi4xNjRhLjI1LjI1IDAgMCAwIC4yMi0uMzY4Wm0uNTMgMy45OTZ2Mi41YS43NS43NSAwIDAgMS0xLjUgMHYtMi41YS43NS43NSAwIDAgMSAxLjUgMFpNOSAxMWExIDEgMCAxIDEtMiAwIDEgMSAwIDAgMSAyIDBaIiAvPjwvc3ZnPg==)

These base styles are **required** for React Flow to function correctly. If you don't import them or you override them with your own styles, some things might not work as expected!

App.jsx

index.css

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9Im5vbmUiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBhcmlhLWhpZGRlbj0idHJ1ZSIgZGF0YS1zbG90PSJpY29uIiBjbGFzcz0ic2l6ZS01IHN0cm9rZS0yIj48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xNS42NjYgMy44ODhBMi4yNSAyLjI1IDAgMCAwIDEzLjUgMi4yNWgtM2MtMS4wMyAwLTEuOS42OTMtMi4xNjYgMS42MzhtNy4zMzIgMGMuMDU1LjE5NC4wODQuNC4wODQuNjEydjBhLjc1Ljc1IDAgMCAxLS43NS43NUg5YS43NS43NSAwIDAgMS0uNzUtLjc1djBjMC0uMjEyLjAzLS40MTguMDg0LS42MTJtNy4zMzIgMGMuNjQ2LjA0OSAxLjI4OC4xMSAxLjkyNy4xODQgMS4xLjEyOCAxLjkwNyAxLjA3NyAxLjkwNyAyLjE4NVYxOS41YTIuMjUgMi4yNSAwIDAgMS0yLjI1IDIuMjVINi43NUEyLjI1IDIuMjUgMCAwIDEgNC41IDE5LjVWNi4yNTdjMC0xLjEwOC44MDYtMi4wNTcgMS45MDctMi4xODVhNDguMjA4IDQ4LjIwOCAwIDAgMSAxLjkyNy0uMTg0IiAvPjwvc3ZnPg==)

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9Im5vbmUiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBhcmlhLWhpZGRlbj0idHJ1ZSIgZGF0YS1zbG90PSJpY29uIiBjbGFzcz0ic2l6ZS02Ij48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xNy4yNSA2Ljc1IDIyLjUgMTJsLTUuMjUgNS4yNW0tMTAuNSAwTDEuNSAxMmw1LjI1LTUuMjVtNy41LTMtNC41IDE2LjUiIC8+PC9zdmc+)

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9Im5vbmUiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBhcmlhLWhpZGRlbj0idHJ1ZSIgZGF0YS1zbG90PSJpY29uIiBjbGFzcz0ic2l6ZS01IHN0cm9rZS0yIj48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xNi4wMjMgOS4zNDhoNC45OTJ2LS4wMDFNMi45ODUgMTkuNjQ0di00Ljk5Mm0wIDBoNC45OTJtLTQuOTkzIDAgMy4xODEgMy4xODNhOC4yNSA4LjI1IDAgMCAwIDEzLjgwMy0zLjdNNC4wMzEgOS44NjVhOC4yNSA4LjI1IDAgMCAxIDEzLjgwMy0zLjdsMy4xODEgMy4xODJtMC00Ljk5MXY0Ljk5IiAvPjwvc3ZnPg==)

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0ic2l6ZS00IGZpbGwtc2xhdGUtNzAwIHN0cm9rZS1zbGF0ZS03MDAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgdmlld2JveD0iMCAwIDU2IDc4Ij48cGF0aCBkPSJNMjMuNDI3MyA0OC4yODUzQzIzLjc5MzEgNDcuNTg0NSAyMy4wNjE0IDQ2Ljg4MzcgMjIuMzI5OCA0Ni44ODM3SDEuMTEyMjhDMC4wMTQ4MjI0IDQ2Ljg4MzcgLTAuMzUwOTk3IDQ1LjgzMjYgMC4zODA2NDIgNDUuMTMxOEw0MC45ODY2IDAuMjgyMDg0QzQxLjcxODIgLTAuNDE4NjkzIDQzLjE4MTUgMC4yODIwODQgNDIuODE1NyAxLjMzMzI1TDMyLjkzODYgMzAuMDY1MUMzMi41NzI3IDMwLjc2NTkgMzIuOTM4NiAzMS40NjY2IDMzLjY3MDIgMzEuNDY2Nkg1NC44ODc3QzU1Ljk4NTIgMzEuNDY2NiA1Ni4zNTEgMzIuNTE3OCA1NS42MTk0IDMzLjIxODZMMTUuMDEzNCA3Ny43MTc5QzE0LjI4MTggNzguNDE4NyAxMi44MTg1IDc3LjcxNzkgMTMuMTg0MyA3Ni42NjY3TDIzLjQyNzMgNDguMjg1M1oiIC8+PC9zdmc+)

``` 
import React,  from 'react';
import  from '@xyflow/react';
 
import '@xyflow/react/dist/base.css';
 
const nodeDefaults = ;
 
const initialNodes = [
  ,
    data: ,
    ...nodeDefaults,
  },
  ,
    data: ,
    ...nodeDefaults,
  },
  ,
    data: ,
    ...nodeDefaults,
  },
  ,
    data: ,
    ...nodeDefaults,
  },
];
 
const initialEdges = [
  ,
  ,
  ,
];
 
const Flow = () => 
      edges=
      onNodesChange=
      onEdgesChange=
      onConnect=
      fitView
    >
      <Background />
      <Controls />
      <MiniMap />
    </ReactFlow>
  );
};
 
export default Flow;
```

### TailwindCSS[](#tailwindcss) 

Custom nodes and edges are just React components, and you can use any styling solution you'd like to style them. For example, you might want to use [Tailwind ![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNyIgdmlld2JveD0iMCAwIDI0IDI0IiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6aW5saW5lIHg6YWxpZ24tYmFzZWxpbmUgeDpzaHJpbmstMCI+PHBhdGggZD0iTTcgMTdMMTcgNyIgLz48cGF0aCBkPSJNNyA3aDEwdjEwIiAvPjwvc3ZnPg==)](https://tailwindcss.com/) to style your nodes:

``` 
function CustomNode() 
        </div>
        <div className="ml-2">
          <div className="text-lg font-bold"></div>
          <div className="text-gray-500"></div>
        </div>
      </div>
 
      <Handle
        type="target"
        position=
        className="w-16 !bg-teal-500"
      />
      <Handle
        type="source"
        position=
        className="w-16 !bg-teal-500"
      />
    </div>
  );
}
```

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGZpbGw9ImN1cnJlbnRDb2xvciIgaGVpZ2h0PSIuOGVtIiBjbGFzcz0ieDptdC1bLjNlbV0iPjxwYXRoIGQ9Ik02LjQ1NyAxLjA0N2MuNjU5LTEuMjM0IDIuNDI3LTEuMjM0IDMuMDg2IDBsNi4wODIgMTEuMzc4QTEuNzUgMS43NSAwIDAgMSAxNC4wODIgMTVIMS45MThhMS43NSAxLjc1IDAgMCAxLTEuNTQzLTIuNTc1Wm0xLjc2My43MDdhLjI1LjI1IDAgMCAwLS40NCAwTDEuNjk4IDEzLjEzMmEuMjUuMjUgMCAwIDAgLjIyLjM2OGgxMi4xNjRhLjI1LjI1IDAgMCAwIC4yMi0uMzY4Wm0uNTMgMy45OTZ2Mi41YS43NS43NSAwIDAgMS0xLjUgMHYtMi41YS43NS43NSAwIDAgMSAxLjUgMFpNOSAxMWExIDEgMCAxIDEtMiAwIDEgMSAwIDAgMSAyIDBaIiAvPjwvc3ZnPg==)

If you want to overwrite default styles, make sure to import Tailwinds entry point after React Flows base styles.

``` 
import '@xyflow/react/dist/style.css';
import 'tailwind.css';
```

For a complete example of using Tailwind with React Flow, check out [the example](/examples/styling/tailwind)!