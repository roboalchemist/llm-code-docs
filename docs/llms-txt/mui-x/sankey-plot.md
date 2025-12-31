# Source: https://mui.com/x/api/charts/sankey-plot.md

# SankeyPlot API

## Demos

For examples and details on the usage of this React component, visit the component demo pages:

- Charts - Sankey 🧪

## Import

```jsx
import { SankeyPlot } from '@mui/x-charts-pro/SankeyChart';
// or
import { SankeyPlot } from '@mui/x-charts-pro';
```

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| classes | `object` | - | No | Override or extend the styles applied to the component. |
| onLinkClick | `function(event: React.MouseEvent<SVGElement, MouseEvent>, link: SankeyLinkIdentifierWithData) => void` | - | No |  |
| onNodeClick | `function(event: React.MouseEvent<SVGElement, MouseEvent>, node: SankeyNodeIdentifierWithData) => void` | - | No |  |

> **Note**: The `ref` is forwarded to the root element.

## CSS

### Rule name

| Global class | Rule name | Description |
|--------------|-----------|-------------|
| - | linkLabels | Styles applied to the link label container. |
| - | links | Styles applied to the links container. |
| - | nodeLabels | Styles applied to the node label container. |
| - | nodes | Styles applied to the nodes container. |
| - | root | Styles applied to the root element. |

## Source code

If you did not find the information on this page, consider having a look at the implementation of the component for more detail.

- [/packages/x-charts-pro/src/SankeyChart/SankeyPlot.tsx](https://github.com/mui/material-ui/tree/HEAD/packages/x-charts-pro/src/SankeyChart/SankeyPlot.tsx)