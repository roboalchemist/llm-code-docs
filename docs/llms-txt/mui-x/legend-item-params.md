# Source: https://mui.com/x/api/charts/legend-item-params.md

# LegendItemParams API

## Import

```jsx
import { LegendItemParams } from '@mui/x-charts-premium'
// or
import { LegendItemParams } from '@mui/x-charts-pro'
// or
import { LegendItemParams } from '@mui/x-charts'
```

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| color | `string` | - | Yes |  |
| id | `number \| string` | - | Yes |  |
| label | `string` | - | Yes |  |
| markType | `ChartsLabelMarkProps['type']` | - | Yes |  |
| maxValue | `number \| Date \| null` | - | Yes |  |
| minValue | `number \| Date \| null` | - | Yes |  |
| seriesId | `SeriesId` | - | Yes |  |
| itemId | `PieItemId` | - | No |  |

> **Note**: The `ref` is forwarded to the root element.