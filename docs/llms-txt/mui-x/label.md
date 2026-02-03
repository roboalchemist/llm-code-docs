# Source: https://mui.com/x/react-charts/label.md

---
title: Charts - Label
productId: x-charts
components: BarChart, ScatterChart, LineChart, PieChart
---

# Charts - Label

Customize how series and data points are labeled in charts.

A label is the text that identifies a series or data point in a chart, appearing in locations such as the legend, tooltip, or directly on chart elements.

You can set a series label by passing a string to the `label` property of a series.
The label appears in different locations such as the legend and tooltip.

:::info
The Pie chart has specific behavior described in [Pie chart labels](#pie-chart-labels) below.
:::

```tsx
import { BarChart } from '@mui/x-charts/BarChart';

export default function BasicLabel() {
  return (
    <BarChart
      {...props}
      series={[
        {
          data: [2400, 1398, 9800],
          label: 'label 1',
        },
      ]}
    />
  );
}

const props = {
  height: 300,
  xAxis: [{ data: ['A', 'B', 'C'] }],
  yAxis: [{ width: 50 }],
};

```

## Conditional formatting

The `label` property accepts a function that lets you change the label content based on location.
The function receives `location` as its first argument, which can have the following values:

- `'legend'`: Format the label in the [Legend](/x/react-charts/legend/)
- `'tooltip'`: Format the label in the [Tooltip](/x/react-charts/tooltip/)

```tsx
import { BarChart } from '@mui/x-charts/BarChart';

export default function FunctionLabel() {
  return (
    <BarChart
      {...props}
      series={[
        { data: [2400, 1398, 9800], label: 'simple label' },
        { data: [500, 2398, 4300], label: (location) => `${location} label` },
      ]}
    />
  );
}

const props = {
  height: 300,
  xAxis: [{ data: ['A', 'B', 'C'] }],
  yAxis: [{ width: 50 }],
};

```

## Pie chart labels

The [Pie chart](/x/react-charts/pie/) behaves differently due to its nature.
It has labels per slice instead of per series, and provides one additional location where labels can be rendered.
Instead of receiving the `label` as part of the series, it receives it as part of the `data` set inside a series.

The `location` argument can have the following values:

- `'legend'`: Format the label in the [Legend](/x/react-charts/legend/)
- `'tooltip'`: Format the label in the [Tooltip](/x/react-charts/tooltip/)
- `'arc'`: Format the [Arc label](/x/react-charts/pie/#labels) when `arcLabel` is set to `'label'`

```tsx
import { PieChart } from '@mui/x-charts/PieChart';

export default function PieLabel() {
  return (
    <PieChart
      {...props}
      series={[
        {
          data: [
            { id: 0, value: 10, label: (location) => `${location}+A` },
            { id: 1, value: 15, label: (location) => `${location}+B` },
            { id: 2, value: 20, label: (location) => `${location}+C` },
          ],
          type: 'pie',
          arcLabel: 'label',
        },
      ]}
    />
  );
}

const props = {
  width: 200,
  height: 200,
};

```
