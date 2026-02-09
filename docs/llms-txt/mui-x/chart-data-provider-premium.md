# Source: https://mui.com/x/api/charts/chart-data-provider-premium.md

# ChartDataProviderPremium API

## Demos

For examples and details on the usage of this React component, visit the component demo pages:

- Charts - Range Bar

## Import

```jsx
import { ChartDataProviderPremium } from '@mui/x-charts-premium/ChartDataProviderPremium';
// or
import { ChartDataProviderPremium } from '@mui/x-charts-premium';
```

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| colors | `Array<string> \| func` | `rainbowSurgePalette` | No |  |
| dataset | `Array<object>` | - | No |  |
| experimentalFeatures | `{ preferStrictDomainInLineCharts?: bool }` | - | No |  |
| height | `number` | - | No |  |
| id | `string` | - | No |  |
| localeText | `object` | - | No |  |
| margin | `number \| { bottom?: number, left?: number, right?: number, top?: number }` | - | No |  |
| series | `Array<object>` | - | No |  |
| skipAnimation | `bool` | - | No |  |
| slotProps | `object` | - | No |  |
| slots | `object` | - | No |  |
| width | `number` | - | No |  |

> **Note**: The `ref` is forwarded to the root element (SVGSVGElement).

## Source code

If you did not find the information on this page, consider having a look at the implementation of the component for more detail.

- [/packages/x-charts-premium/src/ChartDataProviderPremium/ChartDataProviderPremium.tsx](https://github.com/mui/material-ui/tree/HEAD/packages/x-charts-premium/src/ChartDataProviderPremium/ChartDataProviderPremium.tsx)