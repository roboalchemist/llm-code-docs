# Source: https://mui.com/x/react-charts/composition.md

---
title: React Chart composition
productId: x-charts
githubLabel: 'scope: charts'
components: ChartContainer, ChartContainerPro, ChartsGrid, ChartDataProvider, ChartDataProviderPro, ChartsSurface
packageName: '@mui/x-charts'
---

# Charts - Composition

Learn how to use composition to build advanced custom Charts.

The MUI X Charts components follow an architecture based on context providers: you can pass your series and axes definitions to specialized components that transform the data and make it available to its descendants.
These descendants can then be composed.

There are two main types of components used to create Charts: [structural](#structural-components) and [graphical](#graphical-components).

## Structural components

Structural components are used to define a chart's dimensions, surfaces, and data.

- Basics
  - `ChartDataProvider` provides data to descendants.
  - `ChartsSurface` renders the SVG element.
- Helpers
  - `ChartContainer` combines the Data Provider and Surface components.
  - `ChartsWrapper` styled div that positions surface, tooltip, and legend on a grid.

:::info
Demos in this doc use the `ChartContainer` component.
For demos using `ChartDataProvider` and `ChartsSurface`, see [HTML components](/x/react-charts/components/#html-components).
:::

### Chart Data Provider and Surface usage

Notice that the `width` and `height` props are passed to `ChartDataProvider` and not `ChartsSurface`.

`ChartsLegend` is placed inside `ChartDataProvider` to get access to the context, but outside `ChartsSurface` since it's not an SVG component.

```jsx
<ChartDataProvider
  // The configuration of the chart
  series={[{ type: 'bar', data: [100, 200] }]}
  xAxis={[{ scaleType: 'band', data: ['A', 'B'] }]}
  width={500}
  height={300}
>
  <ChartsLegend />
  <ChartsSurface
    // Ref needs to be directly on ChartsSurface
    ref={mySvgRef}
  >
    {children}
  </ChartsSurface>
</ChartDataProvider>
```

### Chart Container usage

`ChartContainer` is the direct concatenation of `ChartDataProvider` and `ChartsSurface`.
It takes care of dispatching props between the two components.

Using `ChartContainer` has one major drawback: all the children will be inside `ChartsSurface`.
You can't render HTML elements such as `ChartsLegend` as shown in the previous example.

```jsx
<ChartContainer
  // The configuration of the chart
  series={[{ type: 'bar', data: [100, 200] }]}
  xAxis={[{ scaleType: 'band', data: ['A', 'B'] }]}
  width={500}
  height={300}
  // Ref is forwarded internally to ChartsSurface
  ref={mySvgRef}
>
  {children} // Only SVG component here
</ChartContainer>
```

### Chart Wrapper usage

Charts are often constructed of a graphic with a legend.
`ChartsWrapper` helps position those elements in a grid structure.

The children should have a CSS `gridArea` property set to `'chart'`, `'legend'`, or `'toolbar'`.
This is done by default on built-in components.

The layout can be modified with the [wrapper props](/x/api/charts/charts-wrapper/).

```jsx
<ChartDataProvider height={300} series={ /* ... */ }>
  <ChartsWrapper legendDirection='horizontal' legendPosition={{ vertical: 'bottom' }}>
    <ChartsLegend direction='horizontal' />
    <ChartsSurface>
      {children}
    </ChartsSurface>
  </ChartsWrapper>
</ChartDataProvider>
```

## Graphical components

Graphical components are used to render the visual elements of a chart.
They are descendants of [`ChartDataProvider`](#structural-components) described above.
These are too numerous to list, but common examples include:

- `LinePlot`
- `BarPlot`
- `ChartsXAxis`
- `ChartsLegend`
- `ChartsTooltip`

You can also [create your own custom components](/x/react-charts/components/) for this purpose.

## Container options

### Responsive dimensions

`ChartContainer` is responsive by default: it automatically adjusts its dimensions to fit the available space defined by the parent element.

Provide the `width` and `height` props to define the dimensions of a chart.

:::warning
For a chart to be responsive, its parent element must have intrinsic dimensions.
If the parent's dimensions rely on its content, the responsive chart will not render.
:::

The demo below lets you switch between a chart with discrete dimensions (`width={500} height={300}`) and one with no dimensions defined, so you see how they differ.

```tsx
import * as React from 'react';
import Paper from '@mui/material/Paper';
import Box from '@mui/material/Box';
import Checkbox from '@mui/material/Checkbox';
import FormControlLabel from '@mui/material/FormControlLabel';
import { ChartContainer } from '@mui/x-charts/ChartContainer';
import { BarPlot } from '@mui/x-charts/BarChart';
import { LinePlot, MarkPlot } from '@mui/x-charts/LineChart';
import { ChartsXAxis } from '@mui/x-charts/ChartsXAxis';

export default function BasicComposition() {
  const [isResponsive, setIsResponsive] = React.useState(false);

  const sizingProps = isResponsive ? {} : { width: 500, height: 300 };
  return (
    <Box sx={{ width: '100%', overflow: 'auto' }}>
      <FormControlLabel
        checked={isResponsive}
        control={
          <Checkbox onChange={(event) => setIsResponsive(event.target.checked)} />
        }
        label="Use responsive container"
        labelPlacement="end"
      />

      <Paper sx={{ margin: 1, height: 300 }} elevation={3}>
        <ChartContainer
          series={[
            {
              type: 'bar',
              data: [1, 2, 3, 2, 1],
            },
            {
              type: 'line',
              data: [4, 3, 1, 3, 4],
            },
          ]}
          xAxis={[
            {
              data: ['A', 'B', 'C', 'D', 'E'],
              scaleType: 'band',
              id: 'x-axis-id',
              height: 48,
            },
          ]}
          {...sizingProps}
        >
          <BarPlot />
          <LinePlot />
          <MarkPlot />
          <ChartsXAxis label="X axis" axisId="x-axis-id" />
        </ChartContainer>
      </Paper>
    </Box>
  );
}

```

### Properties

`ChartContainer` takes all props that are not specific to a single graphical element.
This includes:

- The `xAxis` and `yAxis` props—see [Axis](/x/react-charts/axis/) for details
- The `colors` prop—see [Styling—Color palette](/x/react-charts/styling/#color-palette) for details
- The `series` and `dataset` props

#### Series

The `series` prop is an array of series definitions.
See the following documents to learn more about each specific series type:

- [Line](/x/react-charts/lines/)
- [Bar](/x/react-charts/bars/)
- [Pie](/x/react-charts/pie/)
- [Scatter](/x/react-charts/scatter/)

When using a [self-contained Chart component](/x/react-charts/quickstart/#self-contained-charts), it's assumed that the series type corresponds to the Chart type.
For example, `BarChart` assumes that `series` is of type `'bar'`.

```jsx
<BarChart
  series={[
    {
      // No need to specify the series type
      data: [1, 2, 3],
    },
  ]}
/>
```

When composing a custom chart, `ChartContainer` doesn't know the series type, so you must explicitly define it.
For example, the custom chart below uses both `BarPlot` and `LinePlot`, and each one requires a corresponding `type` for its `data`.

```jsx
<ChartContainer
  series={[
    // This series is for the bar plot
    { data: [1, 2, 3], type: 'bar' },
    // This series is for the line plot
    { data: [3, 2, 1], type: 'line' },
  ]}
>
  <BarPlot /> {/* Only displays the series with type: 'bar' */}
  <LinePlot /> {/* Only displays series with type: 'line' */}
</ChartContainer>
```

Those series can use the `dataset` prop the same way that a single-component chart does.
See [Bars—Using a dataset](/x/react-charts/bars/#using-a-dataset) for more details.

In the demo below, the chart is constructed by combining `BarPlot` and `LinePlot`.
You can modify the series `type` property to switch between rendering a line and a bar.

```jsx
<ChartContainer
  series={[
    { type, data: [1, 2, 3, 2, 1] },
    { type, data: [4, 3, 1, 3, 4] },
  ]}
>
  <BarPlot />
  <LinePlot />
  <ChartsXAxis label="X axis" axisId="x-axis-id" />
</ChartContainer>
```

```tsx
import * as React from 'react';
import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';
import MenuItem from '@mui/material/MenuItem';
import { ChartContainer } from '@mui/x-charts/ChartContainer';
import { BarPlot } from '@mui/x-charts/BarChart';
import { LinePlot } from '@mui/x-charts/LineChart';
import { ChartsXAxis } from '@mui/x-charts/ChartsXAxis';

export default function SwitchSeriesType() {
  const [type, setType] = React.useState<'line' | 'bar'>('line');

  return (
    <Box sx={{ width: '100%' }}>
      <TextField
        select
        value={type}
        onChange={(event) => setType(event.target.value as 'line' | 'bar')}
        label="series type"
        sx={{ minWidth: 150 }}
      >
        <MenuItem value="line">line</MenuItem>
        <MenuItem value="bar">bar</MenuItem>
      </TextField>

      <div>
        <ChartContainer
          series={[
            {
              type,
              data: [1, 2, 3, 2, 1],
            },
            {
              type,
              data: [4, 3, 1, 3, 4],
            },
          ]}
          xAxis={[
            {
              data: ['A', 'B', 'C', 'D', 'E'],
              scaleType: 'band',
              id: 'x-axis-id',
              height: 48,
            },
          ]}
          height={200}
        >
          <BarPlot />
          <LinePlot />
          <ChartsXAxis label="X axis" axisId="x-axis-id" />
        </ChartContainer>
      </div>
    </Box>
  );
}

```

## Subcomponents

:::info
The CSS `z-index` property does not exist on SVG elements, so the order of SVG elements in the composed component is the only way to define how they overlap.
Elements rendered later display above elements rendered earlier.
:::

### Plotting

To display data, you can use the components named `[Type]Plot` such as `LinePlot`, `AreaPlot`, `MarkPlot`, `BarPlot`, and more.

### Clipping

Use the `ChartsClipPath` component to ensure chart elements stay confined to the designated drawing area.
This component defines a rectangular clip path that acts as a boundary.

Here's how to apply it:

1. Define the clip path: Use `<ChartsClipPath id={clipPathId} />` to establish the clip path for the drawing area. `clipPathId` must be a unique identifier.
2. Wrap the Chart: Enclose the chart elements you want to clip within a `<g>` element. Set the `clipPath` attribute to `url(#${clipPathId})` to reference the previously defined clip path. Example: ``<g clipPath={`url(#${clipPathId})`}>``

```jsx
<ChartContainer>
  <g clipPath={`url(#${clipPathId})`}>
    // The plotting to clip in the drawing area.
    <ScatterPlot />
    <LinePlot />
  </g>
  <ChartsClipPath id={clipPathId} /> // Defines the clip path of the drawing area.
</ChartContainer>
```

The demo below lets you toggle clipping for scatter and line plots.
Observe how the line markers extend beyond the clip area, rendering on top of the axes.

```tsx
import * as React from 'react';
import Slider from '@mui/material/Slider';
import Box from '@mui/material/Box';
import FormControlLabel from '@mui/material/FormControlLabel';
import Checkbox from '@mui/material/Checkbox';
import useId from '@mui/utils/useId';

import { ChartContainer } from '@mui/x-charts/ChartContainer';
import { ScatterPlot } from '@mui/x-charts/ScatterChart';
import { LinePlot, MarkPlot } from '@mui/x-charts/LineChart';
import { ChartsClipPath } from '@mui/x-charts/ChartsClipPath';
import { ChartsXAxis } from '@mui/x-charts/ChartsXAxis';
import { ChartsYAxis } from '@mui/x-charts/ChartsYAxis';
import { ChartsGrid } from '@mui/x-charts/ChartsGrid';

import { Chance } from 'chance';

const chance = new Chance(42);

const data = Array.from({ length: 100 }, () => ({
  x: chance.floating({ min: -25, max: 25 }),
  y: chance.floating({ min: -25, max: 25 }),
})).map((d, index) => ({ ...d, id: index }));

const minDistance = 10;

export default function LimitOverflow() {
  const [isLimited, setIsLimited] = React.useState(false);
  const [xLimits, setXLimites] = React.useState<number[]>([-20, 20]);

  const id = useId();
  const clipPathId = `${id}-clip-path`;

  const handleChange = (
    event: Event,
    newValue: number | number[],
    activeThumb: number,
  ) => {
    if (!Array.isArray(newValue)) {
      return;
    }

    if (newValue[1] - newValue[0] < minDistance) {
      if (activeThumb === 0) {
        const clamped = Math.min(newValue[0], 100 - minDistance);
        setXLimites([clamped, clamped + minDistance]);
      } else {
        const clamped = Math.max(newValue[1], minDistance);
        setXLimites([clamped - minDistance, clamped]);
      }
    } else {
      setXLimites(newValue as number[]);
    }
  };

  return (
    <Box sx={{ width: '100%', maxWidth: 500 }}>
      <FormControlLabel
        checked={isLimited}
        control={
          <Checkbox onChange={(event) => setIsLimited(event.target.checked)} />
        }
        label="Clip the plot"
        labelPlacement="end"
      />
      <ChartContainer
        xAxis={[
          {
            label: 'x',
            min: xLimits[0],
            max: xLimits[1],
            data: [-30, -25, -20, -15, -10, -5, 0, 5, 10, 15, 20, 25],
            height: 48,
          },
        ]}
        series={[
          { type: 'scatter', data, markerSize: 8 },
          {
            type: 'line',
            data: [10, 13, 12, 5, -6, -3, 4, 20, 18, 17, 12, 11],
            showMark: true,
          },
        ]}
        height={300}
      >
        <ChartsGrid vertical horizontal />
        <g clipPath={`url(#${clipPathId})`}>
          <ScatterPlot />
          <LinePlot />
        </g>
        <ChartsXAxis />
        <ChartsYAxis />
        <MarkPlot />
        {isLimited && <ChartsClipPath id={clipPathId} />}
      </ChartContainer>

      <Slider
        value={xLimits}
        onChange={handleChange}
        valueLabelDisplay="auto"
        min={-40}
        max={40}
      />
    </Box>
  );
}

```

:::warning
The demo above generates a unique ID with `useId()`.

```js
const id = useId();
const clipPathId = `${id}-clip-path`;
```

It's important to generate unique IDs for clip paths, especially when dealing with multiple charts on a page.
Assigning a static ID like `"my-id"` leads to conflicts.
:::

### Axis

To add axes, use `ChartsXAxis` and `ChartsYAxis` as described in [Axis—Composition](/x/react-charts/axis/#composition).
These components take an `axisId` prop that indicates which axis defined in the container should be rendered.
If `axisId` is not provided, the first axis is used by default.

### Grid

Use `ChartsGrid` to add a grid to the component.
See [Axis—Grid](/x/react-charts/axis/#grid) for more information.

### Legend

Use `ChartsLegend` to display a legend with information about the chart.

:::warning
`ChartsLegend` is an HTML element since v8.
It must be rendered inside `ChartDataProvider` to gain access to the data, but outside of `ChartsSurface` since it's not an SVG element.

This means you can't use it inside `ChartContainer`.
You must use `ChartDataProvider` and `ChartsSurface` instead.

```jsx
// ✅ Correct
<ChartDataProvider>
  <ChartsLegend />
  <ChartsSurface>{/* SVG components */}</ChartsSurface>
</ChartDataProvider>

// ❌ Incorrect
<ChartContainer>
  <ChartsLegend />
</ChartContainer>
```

:::

See [HTML components](/x/react-charts/components/#html-components) for more information about custom legends.

### Interaction

You can add interactive elements such as `ChartsAxisHighlight` and `ChartsTooltip` as illustrated in the demo below.

```tsx
import { ChartDataProvider } from '@mui/x-charts/ChartDataProvider';
import { ChartsSurface } from '@mui/x-charts/ChartsSurface';
import { LinePlot, MarkPlot } from '@mui/x-charts/LineChart';
import { ChartsLegend } from '@mui/x-charts/ChartsLegend';
import { ChartsTooltip } from '@mui/x-charts/ChartsTooltip';
import { ChartsXAxis } from '@mui/x-charts/ChartsXAxis';
import { ChartsYAxis } from '@mui/x-charts/ChartsYAxis';
import { ChartsAxisHighlight } from '@mui/x-charts/ChartsAxisHighlight';
import Box from '@mui/material/Box';

const pData = [2400, 1398, 9800, 3908, 4800, 3800, 4300];
const xLabels = [
  'Page A',
  'Page B',
  'Page C',
  'Page D',
  'Page E',
  'Page F',
  'Page G',
];

export default function LegendTooltipComposition() {
  return (
    <Box
      sx={{
        width: '100%',
        overflow: 'auto',
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
      }}
    >
      <ChartDataProvider
        height={300}
        series={[{ type: 'line', data: pData, label: 'Sales Data' }]}
        xAxis={[{ scaleType: 'point', data: xLabels }]}
        yAxis={[{ width: 50 }]}
        margin={{ top: 30, right: 30, bottom: 20, left: 20 }}
      >
        <ChartsLegend />
        <ChartsTooltip />
        <ChartsSurface>
          <ChartsXAxis />
          <ChartsYAxis />
          <LinePlot />
          <MarkPlot />
          <ChartsAxisHighlight x="line" />
        </ChartsSurface>
      </ChartDataProvider>
    </Box>
  );
}

```

:::info
By default, `ChartContainer` listens to mouse events to keep track of where the mouse is located on the chart.

If you're not using the axis highlight or the tooltip, consider disabling this feature with the `disableAxisListener` prop.

```jsx
<ChartContainer {...} disableAxisListener>
```

:::

## Examples

### Bell curve

This example demonstrates how to combine scatter and line plots to overlay a normal distribution curve (known as a bell curve) over scattered data points.
The bell curve is calculated based on the mean and standard deviation of the data.

```tsx
import { ChartContainer } from '@mui/x-charts/ChartContainer';
import { ScatterPlot } from '@mui/x-charts/ScatterChart';
import { LinePlot } from '@mui/x-charts/LineChart';
import { ChartsXAxis } from '@mui/x-charts/ChartsXAxis';
import { ChartsYAxis } from '@mui/x-charts/ChartsYAxis';
import { ChartsReferenceLine } from '@mui/x-charts/ChartsReferenceLine';
import { internetUsageByCountry } from '../dataset/internetUsageByCountry';

const data = Object.values(internetUsageByCountry);

function calculateStatistics(values: number[]) {
  const n = values.length;
  const mean = values.reduce((sum, val) => sum + val, 0) / n;
  const variance = values.reduce((sum, val) => sum + Math.pow(val - mean, 2), 0) / n;
  const stdDev = Math.sqrt(variance);
  return { mean, stdDev };
}

function normalDistribution(x: number, mean: number, stdDev: number) {
  const exponent = -Math.pow(x - mean, 2) / (2 * Math.pow(stdDev, 2));
  return (1 / (stdDev * Math.sqrt(2 * Math.PI))) * Math.exp(exponent);
}

export default function BellCurveOverlay() {
  const { mean, stdDev } = calculateStatistics(data);

  // Generate bell curve data
  const min = Math.min(...data);
  const max = Math.max(...data);
  const range = max - min;
  const bellCurveData: number[] = [];
  const xValues: number[] = [];
  const numPoints = 100;

  for (let i = 0; i <= numPoints; i += 1) {
    const x = min - range * 0.1 + ((max - min + range * 0.2) * i) / numPoints;
    xValues.push(x);
    bellCurveData.push(normalDistribution(x, mean, stdDev));
  }

  // Stack points that are close together
  const binWidth = range / 70; // Adjust this to control stacking sensitivity
  const sortedData = [...data].sort((a, b) => a - b);
  const bins: Map<number, number[]> = new Map();

  // Group values into bins
  sortedData.forEach((value) => {
    const binIndex = Math.round(value / binWidth);
    if (!bins.has(binIndex)) {
      bins.set(binIndex, []);
    }
    bins.get(binIndex)!.push(value);
  });

  // Create scatter data with stacked y-positions
  const scatterData: Array<{ x: number; y: number; id: number }> = [];
  let globalIndex = 0;
  const baseY = 0.0005;
  const stackHeight = 0.001;

  bins.forEach((values) => {
    values.forEach((value, stackIndex) => {
      scatterData.push({
        x: value,
        y: baseY + stackIndex * stackHeight,
        id: globalIndex,
      });
      globalIndex += 1;
    });
  });

  return (
    <div style={{ width: '100%' }}>
      <ChartContainer
        series={[
          {
            type: 'scatter',
            data: scatterData,
            label: 'Data points',
            id: 'scatter',
            markerSize: 4,
          },
          {
            type: 'line',
            data: bellCurveData,
            label: 'Normal distribution',
            id: 'bell-curve',
            color: '#f97316',
            curve: 'natural',
            showMark: false,
          },
        ]}
        xAxis={[
          {
            data: xValues,
            min: min - range * 0.1,
            max: max + range * 0.1,
            label: 'Individuals using the Internet (% of population)',
            valueFormatter: (value: string) => `${value}%`,
          },
        ]}
        yAxis={[
          {
            position: 'none',
          },
        ]}
        height={400}
      >
        <ScatterPlot />
        <LinePlot />
        <ChartsReferenceLine
          x={mean}
          label="Mean"
          lineStyle={{ strokeWidth: 2 }}
          labelStyle={{ fontWeight: 'bold' }}
          labelAlign="start"
          spacing={{ y: 40 }}
        />
        <ChartsReferenceLine
          x={mean - stdDev}
          label="-1σ"
          lineStyle={{ strokeWidth: 1.5, strokeDasharray: '5 5' }}
          labelAlign="start"
          spacing={{ y: 40 }}
        />
        <ChartsReferenceLine
          x={mean + stdDev}
          label="+1σ"
          lineStyle={{ strokeWidth: 1.5, strokeDasharray: '5 5' }}
          labelAlign="start"
          spacing={{ y: 40 }}
        />
        <ChartsXAxis />
        <ChartsYAxis />
      </ChartContainer>
    </div>
  );
}

```
