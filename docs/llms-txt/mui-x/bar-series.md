# Source: https://mui.com/x/api/charts/bar-series.md

# BarSeries API

## Import

```jsx
import { BarSeries } from '@mui/x-charts-premium'
// or
import { BarSeries } from '@mui/x-charts-pro'
// or
import { BarSeries } from '@mui/x-charts'
```

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| type | `'bar'` | - | Yes |  |
| barLabel | `'value' \| ((item: BarItem, context: BarLabelContext) => string \| null \| undefined)` | - | No |  |
| barLabelPlacement | `'center' \| 'outside'` | `'center'` | No |  |
| color | `string` | - | No |  |
| colorGetter | `(data: ColorCallbackValue<TValue>) => string` | - | No |  |
| data | `ReadonlyArray<BarValueType \| null>` | - | No |  |
| dataKey | `string` | - | No |  |
| highlightScope | `HighlightScope` | - | No |  |
| id | `SeriesId` | - | No |  |
| label | `string \| ((location: 'tooltip' \| 'legend') => string)` | - | No |  |
| labelMarkType | `ChartsLabelMarkType` | - | No |  |
| layout | `'horizontal' \| 'vertical'` | `'vertical'` | No |  |
| minBarSize | `number` | `0px` | No |  |
| stack | `string` | - | No |  |
| stackOffset | `StackOffsetType` | `'diverging'` | No |  |
| stackOrder | `StackOrderType` | `'none'` | No |  |
| valueFormatter | `SeriesValueFormatter<TValue>` | - | No |  |
| xAxisId | `AxisId` | - | No |  |
| yAxisId | `AxisId` | - | No |  |

> **Note**: The `ref` is forwarded to the root element.