# Source: https://mui.com/x/api/charts/charts-x-axis.md

# ChartsXAxis API

## Demos

For examples and details on the usage of this React component, visit the component demo pages:

- [Charts - Axis](/x/react-charts/axis/)

## Import

```jsx
import { ChartsXAxis } from '@mui/x-charts/ChartsXAxis';
// or
import { ChartsXAxis } from '@mui/x-charts';
// or
import { ChartsXAxis } from '@mui/x-charts-pro';
// or
import { ChartsXAxis } from '@mui/x-charts-premium';
```

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| axisId | `number \| string` | - | No |  |
| classes | `object` | - | No | Override or extend the styles applied to the component. |
| disableLine | `bool` | `false` | No |  |
| disableTicks | `bool` | `false` | No |  |
| label | `string` | - | No |  |
| labelStyle | `object` | - | No |  |
| slotProps | `object` | `{}` | No |  |
| slots | `object` | `{}` | No |  |
| tickInterval | `'auto' \| array \| func` | `'auto'` | No |  |
| tickLabelInterval | `'auto' \| func` | `'auto'` | No |  |
| tickLabelMinGap | `number` | `4` | No |  |
| tickLabelPlacement | `'middle' \| 'tick'` | `'middle'` | No |  |
| tickLabelStyle | `object` | - | No |  |
| tickMaxStep | `number` | - | No |  |
| tickMinStep | `number` | - | No |  |
| tickNumber | `number` | - | No |  |
| tickPlacement | `'end' \| 'extremities' \| 'middle' \| 'start'` | `'extremities'` | No |  |
| tickSize | `number` | `6` | No |  |

> **Note**: The `ref` is forwarded to the root element.

> Any other props supplied will be provided to the root element (native element).

## Source code

If you did not find the information on this page, consider having a look at the implementation of the component for more detail.

- [/packages/x-charts/src/ChartsXAxis/ChartsXAxis.tsx](https://github.com/mui/material-ui/tree/HEAD/packages/x-charts/src/ChartsXAxis/ChartsXAxis.tsx)