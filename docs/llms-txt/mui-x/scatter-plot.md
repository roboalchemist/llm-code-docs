# Source: https://mui.com/x/api/charts/scatter-plot.md

# ScatterPlot API

## Demos

For examples and details on the usage of this React component, visit the component demo pages:

- [Charts - Scatter](/x/react-charts/scatter/)
- [Charts - Scatter demos](/x/react-charts/scatter-demo/)

## Import

```jsx
import { ScatterPlot } from '@mui/x-charts/ScatterChart';
// or
import { ScatterPlot } from '@mui/x-charts';
// or
import { ScatterPlot } from '@mui/x-charts-pro';
// or
import { ScatterPlot } from '@mui/x-charts-premium';
```

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| onItemClick | `function(event: MouseEvent, scatterItemIdentifier: ScatterItemIdentifier) => void` | - | No |  |
| renderer | `'svg-batch' \| 'svg-single'` | `'svg-single'` | No |  |
| slotProps | `object` | `{}` | No |  |
| slots | `object` | `{}` | No |  |

> **Note**: The `ref` is forwarded to the root element.

## Slots

| Name | Default | Class | Description |
|------|---------|-------|-------------|
| marker | `ScatterMarker` | - | The component that renders the marker for a scatter point. |
| scatter | `undefined` | - |  |

## Source code

If you did not find the information on this page, consider having a look at the implementation of the component for more detail.

- [/packages/x-charts/src/ScatterChart/ScatterPlot.tsx](https://github.com/mui/material-ui/tree/HEAD/packages/x-charts/src/ScatterChart/ScatterPlot.tsx)