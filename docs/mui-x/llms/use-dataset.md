# Source: https://mui.com/x/react-charts/hooks/use-dataset.md

---
title: Charts - useDataset
productId: x-charts
---

# useDataset

Access the dataset used to populate series and axes data.

The `useDataset` hook provides access to the dataset array that was passed to the chart. This is useful when you need to access the raw data for custom components or calculations.

To access the computed series and axes data, use the [useSeries](/x/react-charts/hooks/use-series/) and `useAxes` hooks instead.

## Usage

```js
import { useDataset } from '@mui/x-charts/hooks';

function CustomComponent() {
  const dataset = useDataset();
  // Access the raw dataset array
}
```

The hook returns the dataset array that was passed to the `dataset` prop of the chart, or `undefined` if no dataset was provided.

## Basic example

This example demonstrates using the `useDataset` hook to display dataset statistics above a chart:

```tsx
import * as React from 'react';
import { useDataset } from '@mui/x-charts/hooks';
import { ChartDataProvider } from '@mui/x-charts/ChartDataProvider';
import { ChartsSurface } from '@mui/x-charts/ChartsSurface';
import { LineHighlightPlot, LinePlot } from '@mui/x-charts/LineChart';
import { ChartsXAxis } from '@mui/x-charts/ChartsXAxis';
import { ChartsYAxis } from '@mui/x-charts/ChartsYAxis';
import { ChartsLegend } from '@mui/x-charts/ChartsLegend';
import { ChartsTooltip } from '@mui/x-charts/ChartsTooltip';
import { ChartsAxisHighlight } from '@mui/x-charts/ChartsAxisHighlight';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import Paper from '@mui/material/Paper';

const dataset = [
  { month: 'Jan', revenue: 4000, expenses: 2400 },
  { month: 'Feb', revenue: 3000, expenses: 1398 },
  { month: 'Mar', revenue: 2000, expenses: 9800 },
  { month: 'Apr', revenue: 2780, expenses: 3908 },
  { month: 'May', revenue: 1890, expenses: 4800 },
  { month: 'Jun', revenue: 2390, expenses: 3800 },
  { month: 'Jul', revenue: 3490, expenses: 4300 },
];

function DatasetStats() {
  const chartDataset = useDataset();

  if (!chartDataset) {
    return null;
  }

  const totalRevenue = chartDataset.reduce(
    (sum, item) => sum + (typeof item.revenue === 'number' ? item.revenue : 0),
    0,
  );
  const totalExpenses = chartDataset.reduce(
    (sum, item) => sum + (typeof item.expenses === 'number' ? item.expenses : 0),
    0,
  );
  const profit = totalRevenue - totalExpenses;

  return (
    <Paper
      elevation={2}
      sx={{
        p: 2,
        mb: 2,
        display: 'flex',
        gap: 3,
        justifyContent: 'space-around',
      }}
    >
      <div>
        <Typography variant="caption" color="text.secondary">
          Total Revenue
        </Typography>
        <Typography variant="h6" color="primary">
          ${totalRevenue.toLocaleString()}
        </Typography>
      </div>
      <div>
        <Typography variant="caption" color="text.secondary">
          Total Expenses
        </Typography>
        <Typography variant="h6" color="error">
          ${totalExpenses.toLocaleString()}
        </Typography>
      </div>
      <div>
        <Typography variant="caption" color="text.secondary">
          Net Profit
        </Typography>
        <Typography variant="h6" color={profit >= 0 ? 'success.main' : 'error.main'}>
          ${profit.toLocaleString()}
        </Typography>
      </div>
      <div>
        <Typography variant="caption" color="text.secondary">
          Data Points
        </Typography>
        <Typography variant="h6">{chartDataset.length}</Typography>
      </div>
    </Paper>
  );
}

export default function UseDataset() {
  return (
    <ChartDataProvider
      dataset={dataset}
      xAxis={[{ dataKey: 'month', scaleType: 'point' }]}
      series={[
        {
          dataKey: 'revenue',
          label: 'Revenue',
          color: '#1976d2',
          type: 'line',
        },
        {
          dataKey: 'expenses',
          label: 'Expenses',
          color: '#d32f2f',
          type: 'line',
        },
      ]}
      height={300}
    >
      <Box sx={{ width: '100%' }}>
        <DatasetStats />
        <ChartsSurface>
          <LinePlot />
          <ChartsXAxis />
          <ChartsYAxis />
          <ChartsAxisHighlight x="line" />
          <ChartsTooltip />
          <LineHighlightPlot />
        </ChartsSurface>
        <Box sx={{ display: 'flex', justifyContent: 'center' }}>
          <ChartsLegend direction="horizontal" />
        </Box>
      </Box>
    </ChartDataProvider>
  );
}

```

## Advanced example

This example shows how to use the dataset to create a custom data table that synchronizes with the chart:

```tsx
import * as React from 'react';
import { useDataset } from '@mui/x-charts/hooks';
import { ChartDataProvider } from '@mui/x-charts/ChartDataProvider';
import { ChartsSurface } from '@mui/x-charts/ChartsSurface';
import { BarPlot } from '@mui/x-charts/BarChart';
import { ChartsXAxis } from '@mui/x-charts/ChartsXAxis';
import { ChartsYAxis } from '@mui/x-charts/ChartsYAxis';
import { ChartsLegend } from '@mui/x-charts/ChartsLegend';
import { ChartsTooltip } from '@mui/x-charts/ChartsTooltip';
import { ChartsAxisHighlight } from '@mui/x-charts/ChartsAxisHighlight';
import { AxisItemIdentifier } from '@mui/x-charts/models';
import Box from '@mui/material/Box';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import Typography from '@mui/material/Typography';

const dataset = [
  { product: 'Product A', q1: 4000, q2: 3000, q3: 2000, q4: 2780 },
  { product: 'Product B', q1: 3000, q2: 1398, q3: 9800, q4: 3908 },
  { product: 'Product C', q1: 2000, q2: 9800, q3: 3000, q4: 4800 },
  { product: 'Product D', q1: 2780, q2: 3908, q3: 4000, q4: 3800 },
  { product: 'Product E', q1: 1890, q2: 4800, q3: 2390, q4: 3800 },
];

function DataTable({
  highlightedIndex,
  onHighlightedIndexChange,
}: {
  highlightedIndex: number | undefined;
  onHighlightedIndexChange: (index: number | null) => void;
}) {
  const chartDataset = useDataset();

  if (!chartDataset) {
    return null;
  }

  const calculateTotal = (item: any) => {
    return ['q1', 'q2', 'q3', 'q4'].reduce((sum, quarter) => {
      const value = item[quarter];
      return sum + (typeof value === 'number' ? value : 0);
    }, 0);
  };

  const calculateQuarterTotal = (quarter: string) => {
    return chartDataset.reduce((sum, item) => {
      const value = item[quarter];
      return sum + (typeof value === 'number' ? value : 0);
    }, 0);
  };

  const grandTotal = chartDataset.reduce(
    (sum, item) => sum + calculateTotal(item),
    0,
  );

  return (
    <TableContainer component={Paper} sx={{ mt: 3 }}>
      <Table size="small">
        <TableHead>
          <TableRow>
            <TableCell>
              <strong>Product</strong>
            </TableCell>
            <TableCell align="right">
              <strong>Q1</strong>
            </TableCell>
            <TableCell align="right">
              <strong>Q2</strong>
            </TableCell>
            <TableCell align="right">
              <strong>Q3</strong>
            </TableCell>
            <TableCell align="right">
              <strong>Q4</strong>
            </TableCell>
            <TableCell align="right">
              <strong>Total</strong>
            </TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {chartDataset.map((row, index) => (
            <TableRow
              key={String(row.product)}
              onPointerEnter={() => onHighlightedIndexChange(index)}
              onPointerLeave={() => onHighlightedIndexChange(null)}
              sx={{
                backgroundColor:
                  highlightedIndex === index ? 'action.hover' : 'transparent',
                transition: 'background-color 0.2s',
                cursor: 'pointer',
              }}
            >
              <TableCell component="th" scope="row">
                {String(row.product)}
              </TableCell>
              <TableCell align="right">
                ${typeof row.q1 === 'number' ? row.q1.toLocaleString() : 0}
              </TableCell>
              <TableCell align="right">
                ${typeof row.q2 === 'number' ? row.q2.toLocaleString() : 0}
              </TableCell>
              <TableCell align="right">
                ${typeof row.q3 === 'number' ? row.q3.toLocaleString() : 0}
              </TableCell>
              <TableCell align="right">
                ${typeof row.q4 === 'number' ? row.q4.toLocaleString() : 0}
              </TableCell>
              <TableCell align="right">
                <strong>${calculateTotal(row).toLocaleString()}</strong>
              </TableCell>
            </TableRow>
          ))}
          <TableRow sx={{ backgroundColor: 'action.hover' }}>
            <TableCell>
              <strong>Total</strong>
            </TableCell>
            <TableCell align="right">
              <strong>${calculateQuarterTotal('q1').toLocaleString()}</strong>
            </TableCell>
            <TableCell align="right">
              <strong>${calculateQuarterTotal('q2').toLocaleString()}</strong>
            </TableCell>
            <TableCell align="right">
              <strong>${calculateQuarterTotal('q3').toLocaleString()}</strong>
            </TableCell>
            <TableCell align="right">
              <strong>${calculateQuarterTotal('q4').toLocaleString()}</strong>
            </TableCell>
            <TableCell align="right">
              <strong>${grandTotal.toLocaleString()}</strong>
            </TableCell>
          </TableRow>
        </TableBody>
      </Table>
    </TableContainer>
  );
}

export default function UseDatasetAdvanced() {
  const [highlightedAxis, setHighlightedAxis] = React.useState<AxisItemIdentifier[]>(
    [],
  );

  const setHighlightedIndexCallback = React.useCallback((index: number | null) => {
    if (index === null) {
      setHighlightedAxis([]);
    } else {
      setHighlightedAxis([{ axisId: 'x-axis-id', dataIndex: index }]);
    }
  }, []);

  return (
    <ChartDataProvider
      dataset={dataset}
      xAxis={[{ id: 'x-axis-id', dataKey: 'product', scaleType: 'band' }]}
      series={[
        { dataKey: 'q1', label: 'Q1', stack: 'total', type: 'bar' },
        { dataKey: 'q2', label: 'Q2', stack: 'total', type: 'bar' },
        { dataKey: 'q3', label: 'Q3', stack: 'total', type: 'bar' },
        { dataKey: 'q4', label: 'Q4', stack: 'total', type: 'bar' },
      ]}
      height={300}
      highlightedAxis={highlightedAxis}
      onHighlightedAxisChange={setHighlightedAxis}
    >
      <Box sx={{ width: '100%' }}>
        <Typography variant="h6" gutterBottom>
          Quarterly Sales Report
        </Typography>
        <ChartsSurface>
          <BarPlot />
          <ChartsXAxis />
          <ChartsYAxis />
          <ChartsAxisHighlight x="band" />
          <ChartsTooltip />
        </ChartsSurface>
        <Box sx={{ display: 'flex', justifyContent: 'center' }}>
          <ChartsLegend direction="horizontal" />
        </Box>
        <DataTable
          highlightedIndex={highlightedAxis[0]?.dataIndex}
          onHighlightedIndexChange={setHighlightedIndexCallback}
        />
      </Box>
    </ChartDataProvider>
  );
}

```

## Return value

The hook returns:

| Type                                 | Description                                                                       |
| :----------------------------------- | :-------------------------------------------------------------------------------- |
| `Readonly<DatasetType> \| undefined` | The dataset array passed to the chart, or `undefined` if no dataset was provided. |

The `DatasetType` is an array of objects where each object represents a data point with various properties. For example:

```ts
const dataset = [
  { month: 'Jan', sales: 100, expenses: 80 },
  { month: 'Feb', sales: 150, expenses: 90 },
  { month: 'Mar', sales: 120, expenses: 70 },
];
```

:::info
The `useDataset` hook only works when using the `dataset` prop. If you're passing data directly to series via the `data` prop, this hook will return `undefined`.
:::

## When to use

The `useDataset` hook is particularly useful when:

- Creating custom components that need access to the raw data
- Building data tables or summaries alongside your charts
- Performing calculations on the full dataset

## Caveats

This hook must be used within a chart context. See the [hooks overview](/x/react-charts/hooks/) for more information about proper usage.
