# Source: https://mui.com/x/react-charts/hooks/use-series.md

---
title: Charts - useSeries
productId: x-charts
---

# useSeries

Access raw series data for all chart types.

The `use[Type]Series` hooks provide access to specific series data for a particular chart type.

## Usage

```js
import { useBarSeries, useLineSeries } from '@mui/x-charts/hooks';

function CustomComponent() {
  const barSeries = useBarSeries(); // Array of bar chart series data
  const lineSeries = useLineSeries(); // Array of line chart series data
}
```

You can also pick specific series by either providing the series id as a parameter, or an array of series ids to get.

```js
const barSeries = useBarSeries('id1');

const barSeries = useBarSeries(['id1', 'id2']);
```

The following hooks exist to access series data specific to each chart type:

- `useBarSeries`
- `useLineSeries`
- `useScatterSeries`
- `usePieSeries`
- `useRadarSeries`
- `useHeatmapSeries`
- `useFunnelSeries`
- `useSankeySeries`

This example demonstrates using the `useBarSeries` hook to access specific bar chart series data:

```tsx
import { useBarSeries } from '@mui/x-charts/hooks';
import { BarChart } from '@mui/x-charts/BarChart';
import { useTheme } from '@mui/material/styles';

const dataset = [
  { month: 'Jan', revenue: 4000, expenses: 2400 },
  { month: 'Feb', revenue: 3000, expenses: 1398 },
  { month: 'Mar', revenue: 5000, expenses: 2800 },
  { month: 'Apr', revenue: 7000, expenses: 3908 },
  { month: 'May', revenue: 6000, expenses: 4800 },
  { month: 'Jun', revenue: 3000, expenses: 8000 },
];

const inUSD = (value: number | null | undefined) => {
  if (value == null) {
    return '';
  }
  return `$${value.toLocaleString()}`;
};

function BarSeriesInfo() {
  const barSeries = useBarSeries();
  const theme = useTheme();

  const revenue = barSeries
    .find((s) => s.id === 'revenue')
    ?.data.reduce((acc, v) => acc! + (v ?? 0), 0);

  const expenses = barSeries
    .find((s) => s.id === 'expenses')
    ?.data.reduce((acc, v) => acc! + (v ?? 0), 0);

  const profit = (revenue ?? 0) - (expenses ?? 0);

  return (
    <div
      style={{
        position: 'absolute',
        top: 20,
        left: 70,
        background: `color(from ${theme.palette.text.primary} srgb r g b / ${theme.palette.mode === 'dark' ? 0.2 : 0.1})`,
        padding: 12,
        borderRadius: 4,
        fontSize: '12px',
        border: '1px solid #e0e0e0',
        zIndex: 10,
      }}
    >
      <h4 style={{ margin: '0 0 8px 0', fontSize: '14px' }}>Half Year Details</h4>
      {barSeries.map((series) => (
        <div key={series.id}>
          <span style={{ fontWeight: 600 }}>
            {typeof series.label === 'function'
              ? series.label('legend')
              : series.label}
          </span>
          <span> {inUSD(series.data.reduce((a, b) => (a ?? 0) + (b ?? 0), 0))}</span>
        </div>
      ))}
      <div>
        <span style={{ fontWeight: 600 }}>Profit</span>
        <span> {inUSD(profit)}</span>
      </div>
    </div>
  );
}

export default function UseBarSeries() {
  return (
    <div>
      <BarChart
        dataset={dataset}
        xAxis={[{ scaleType: 'band', dataKey: 'month' }]}
        sx={{ position: 'relative', height: '100%', width: '100%' }}
        yAxis={[
          {
            scaleType: 'linear',
            valueFormatter: (v) => `${inUSD(v).slice(0, 2)}k`,
          },
        ]}
        series={[
          {
            id: 'revenue',
            dataKey: 'revenue',
            label: 'Revenue',
            color: '#8884d8',
            valueFormatter: inUSD,
          },
          {
            id: 'expenses',
            dataKey: 'expenses',
            label: 'Expenses',
            color: '#82ca9d',
            valueFormatter: inUSD,
          },
        ]}
        width={500}
        height={350}
        slots={{ legend: BarSeriesInfo }}
      />
    </div>
  );
}

```

## Advanced usage

The `useSeries` hook can be used to access all series data at once.
In the example below, the `useSeries` hook is used to create a custom component that displays a line over each series max value.

:::warning
It is generally recommended to use the specific series hooks (for example, `useBarSeries`, `useLineSeries`) when working with a specific chart type, as their API is easier to use.
The `useSeries` hook is more suitable for advanced use cases where you need to work with multiple unknown chart types at once.
:::

```tsx
import * as React from 'react';
import { useSeries, useXAxis, useYAxis } from '@mui/x-charts/hooks';
import { BarPlot } from '@mui/x-charts/BarChart';
import { LinePlot } from '@mui/x-charts/LineChart';
import { ChartsXAxis } from '@mui/x-charts/ChartsXAxis';
import { ChartsYAxis } from '@mui/x-charts/ChartsYAxis';
import { ChartDataProvider } from '@mui/x-charts/ChartDataProvider';
import { ChartsSurface } from '@mui/x-charts/ChartsSurface';

const barData = [4, 3, 5, 7, 2] as const;
const barData2 = [1, 2, 1, 2, 3] as const;
const lineData = [2, 5, 3, 8, 4] as const;
const xLabels = ['Jan', 'Feb', 'Mar', 'Apr', 'May'] as const;

function MaxLineOnEachSeries() {
  const series = useSeries();
  const yAxis = useYAxis();
  const xAxis = useXAxis<'point'>('pointId');

  const maxEach = Object.entries(series).flatMap(([_, typeSeries]) => {
    return Object.values(typeSeries.series).map((s) => ({
      id: s.id,
      max: Math.max(...s.data),
    }));
  });

  return (
    <React.Fragment>
      {maxEach.map(({ id, max }) => (
        <line
          key={id}
          x1={xAxis.scale(xAxis.scale.domain().at(0)!)}
          x2={xAxis.scale(xAxis.scale.domain().at(-1)!)}
          y1={yAxis.scale(max)}
          y2={yAxis.scale(max)}
          stroke="gray"
          strokeDasharray="4 4"
        />
      ))}
    </React.Fragment>
  );
}

export default function UseSeries() {
  return (
    <div>
      <ChartDataProvider
        series={[
          {
            data: barData,
            label: 'Revenue',
            type: 'bar',
          },

          {
            data: lineData,
            label: 'Profit',
            type: 'line',
            xAxisId: 'pointId',
          },
          {
            data: barData2,
            label: 'Expenses',
            type: 'bar',
          },
        ]}
        xAxis={[
          { scaleType: 'band', data: xLabels },
          { id: 'pointId', scaleType: 'point', data: xLabels },
        ]}
        yAxis={[{ scaleType: 'linear' }]}
        width={400}
        height={300}
      >
        <ChartsSurface>
          <BarPlot />
          <LinePlot />
          <ChartsXAxis />
          <ChartsYAxis />
          <MaxLineOnEachSeries />
        </ChartsSurface>
      </ChartDataProvider>
    </div>
  );
}

```

## Caveats

This hook must be used within a chart context. See the [hooks overview](/x/react-charts/hooks/) for more information about proper usage.
