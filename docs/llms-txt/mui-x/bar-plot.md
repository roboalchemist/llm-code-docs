# Source: https://mui.com/x/api/charts/bar-plot.md

# BarPlot API

## Demos

For examples and details on the usage of this React component, visit the component demo pages:

- [Charts - Bar demos](/x/react-charts/bar-demo/)
- [Charts - Bars](/x/react-charts/bars/)

## Import

```jsx
import { BarPlot } from '@mui/x-charts/BarChart';
// or
import { BarPlot } from '@mui/x-charts';
// or
import { BarPlot } from '@mui/x-charts-pro';
// or
import { BarPlot } from '@mui/x-charts-premium';
```

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| borderRadius | `number` | - | No |  |
| onItemClick | `function(event: React.MouseEvent<SVGElement, MouseEvent>, barItemIdentifier: BarItemIdentifier) => void` | - | No |  |
| renderer | `'svg-batch' \| 'svg-single'` | `'svg-single'` | No |  |
| skipAnimation | `bool` | `undefined` | No |  |
| slotProps | `object` | `{}` | No |  |
| slots | `object` | `{}` | No |  |

> **Note**: The `ref` is forwarded to the root element.

> Any other props supplied will be provided to the root element (native element).

## Slots

| Name | Default | Class | Description |
|------|---------|-------|-------------|
| bar | `BarElementPath` | - | The component that renders the bar. |
| barLabel | `BarLabel` | - | The component that renders the bar label. |

## Source code

If you did not find the information on this page, consider having a look at the implementation of the component for more detail.

- [/packages/x-charts/src/BarChart/BarPlot.tsx](https://github.com/mui/material-ui/tree/HEAD/packages/x-charts/src/BarChart/BarPlot.tsx)