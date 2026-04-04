# Source: https://mui.com/x/api/charts/range-bar-plot.md

# RangeBarPlot API

## Demos

For examples and details on the usage of this React component, visit the component demo pages:

- Charts - Range Bar

## Import

```jsx
import { RangeBarPlot } from '@mui/x-charts-premium/BarChartPremium';
// or
import { RangeBarPlot } from '@mui/x-charts-premium';
```

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| borderRadius | `number` | - | No |  |
| onItemClick | `function(event: React.MouseEvent<SVGElement, MouseEvent>, barItemIdentifier: RangeBarItemIdentifier) => void` | - | No |  |
| skipAnimation | `bool` | `undefined` | No |  |
| slotProps | `object` | `{}` | No |  |
| slots | `object` | `{}` | No |  |

> **Note**: The `ref` is forwarded to the root element.

## Slots

| Name | Default | Class | Description |
|------|---------|-------|-------------|
| bar | `BarElementPath` | - | The component that renders the bar. |
| barLabel | `BarLabel` | - | The component that renders the bar label. |

## Source code

If you did not find the information on this page, consider having a look at the implementation of the component for more detail.

- [/packages/x-charts-premium/src/BarChartPremium/RangeBar/RangeBarPlot.tsx](https://github.com/mui/material-ui/tree/HEAD/packages/x-charts-premium/src/BarChartPremium/RangeBar/RangeBarPlot.tsx)