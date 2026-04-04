# Source: https://mui.com/x/api/charts/scatter.md

# Source: https://mui.com/x/react-charts/scatter.md

---
title: React Scatter chart
productId: x-charts
components: ScatterChart, ScatterChartPro, ScatterPlot, ChartsGrid, ChartsWrapper
---

# Charts - Scatter

Scatter charts express the relation between two variables, using points in a surface.

## Overview

Scatter charts are ideal for visualizing relationships or correlations as they show how one variable changes relative to another, identifying clusters, trends, and outliers in datasets.
Each point represents an individual data observation, positioned by its values on the two axes, often revealing patterns.
Scatter charts are commonly used for statistical analysis, scientific data, and performance metrics.
```tsx
import { ScatterChart, ScatterSeries } from '@mui/x-charts/ScatterChart';
import { ChartsTooltipContainer, useItemTooltip } from '@mui/x-charts/ChartsTooltip';
import { styled } from '@mui/material/styles';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import Divider from '@mui/material/Divider';
import Stack from '@mui/material/Stack';
import data from '../dataset/transistorCPUdata';

const chartSetting = {
  yAxis: [{ width: 50, scaleType: 'log' as const }],
  xAxis: [{ valueFormatter: (v: number | null) => (v ? v.toString() : '') }],
};

const constructors = ['Intel', 'Apple', 'AMD'];

const series = [
  {
    type: 'scatter',
    label: 'Other',
    highlightScope: { highlight: 'series', fade: 'global' },
    markerSize: 3,
    data: data
      .filter(
        (item) => !constructors.includes(item.constructor) && item.density !== null,
      )
      .map((item) => ({ x: item.year, y: item.density as number, id: item.id })),
  },
  ...constructors.map(
    (constructor): ScatterSeries => ({
      label: constructor,
      highlightScope: { highlight: 'series', fade: 'global' },
      markerSize: 3,
      data: data
        .filter((item) => item.constructor === constructor && item.density !== null)
        .map((item) => ({ x: item.year, y: item.density as number, id: item.id })),
    }),
  ),
] satisfies ScatterSeries[];

const numberFormatter = new Intl.NumberFormat('en-US').format;

const TooltipPaper = styled('div', {
  name: 'Tooltip',
  slot: 'Paper',
})(({ theme }) => {
  return {
    padding: theme.spacing(1),
    backgroundColor: (theme.vars || theme).palette.background.paper,
    color: (theme.vars || theme).palette.text.primary,
    borderRadius: (theme.vars || theme).shape?.borderRadius,
    border: `solid ${(theme.vars || theme).palette.divider} 1px`,
  };
});

function CustomTooltip() {
  const item = useItemTooltip<'scatter'>();

  return (
    <ChartsTooltipContainer trigger="item">
      <TooltipPaper>
        <Box sx={{ display: 'flex', flexDirection: 'row', alignItems: 'center' }}>
          <Box
            sx={{
              width: 20,
              height: 20,
              backgroundColor: item?.color,
              borderRadius: 1,
              mr: 2,
            }}
          />
          <Typography>{item?.label}</Typography>
        </Box>
        <Divider sx={{ my: 1 }} />
        <Box
          sx={{
            display: 'flex',
            flexDirection: 'row',
            justifyContent: 'space-between',
          }}
        >
          <Typography sx={{ mr: 3 }}>{item?.value.x}</Typography>
          <Typography>
            {item?.value.y == null
              ? 'NaN'
              : `${numberFormatter(item?.value.y)} transistor/mm²`}
          </Typography>
        </Box>
      </TooltipPaper>
    </ChartsTooltipContainer>
  );
}

export default function ScatterOverview() {
  return (
    <Stack width="100%">
      <Typography align="center">Processor density (in transistor/mm²)</Typography>
      <ScatterChart
        height={300}
        series={series}
        grid={{ horizontal: true, vertical: true }}
        voronoiMaxRadius={20}
        slots={{ tooltip: CustomTooltip }}
        {...chartSetting}
      />
    </Stack>
  );
}

```

## Basics

Scatter chart series should contain a `data` property containing an array of objects.
Those objects require the `x` and `y` properties.
With an optional `id` property if more optimization is needed.

```tsx
import { ScatterChart } from '@mui/x-charts/ScatterChart';
import data from '../dataset/random/scatterParallel.json';

export default function BasicScatter() {
  return (
    <ScatterChart
      height={300}
      series={[
        {
          label: 'Series A',
          data: data.map((v) => ({ x: v.x1, y: v.y1, id: v.id })),
        },
        {
          label: 'Series B',
          data: data.map((v) => ({ x: v.x2, y: v.y2, id: v.id })),
        },
      ]}
    />
  );
}

```

### Using a dataset

If your data is stored in an array of objects, you can use the `dataset` helper prop.
It accepts an array of objects such as `dataset={[{a: 1, b: 32, c: 873}, {a: 2, b: 41, c: 182}, ...]}`.

You can reuse this data when defining the series.
The scatter series work a bit differently than in other charts.
You need to specify the `datasetKeys` properties which is an object that requires the `x` and `y` keys.
With an optional `id` and `z` keys if needed.

```tsx
import { ScatterChart } from '@mui/x-charts/ScatterChart';

export default function ScatterDataset() {
  return (
    <ScatterChart
      dataset={dataset}
      series={[
        { datasetKeys: { x: 'x1', y: 'y1' }, label: 'Series A' },
        { datasetKeys: { x: 'x2', y: 'y2' }, label: 'Series B' },
      ]}
      {...chartSetting}
    />
  );
}

const dataset = [
  { x1: 373, y1: 434, x2: 304, y2: 349 },
  { x1: 173, y1: 437, x2: 208, y2: 347 },
  { x1: 68, y1: 292, x2: 151, y2: 280 },
  { x1: 121, y1: 116, x2: 185, y2: 176 },
  { x1: 322, y1: 61, x2: 278, y2: 170 },
  { x1: 466, y1: 210, x2: 346, y2: 246 },
  { x1: 418, y1: 403, x2: 326, y2: 333 },
  { x1: 224, y1: 449, x2: 235, y2: 352 },
  { x1: 87, y1: 335, x2: 158, y2: 311 },
  { x1: 104, y1: 167, x2: 166, y2: 218 },
  { x1: 262, y1: 70, x2: 251, y2: 161 },
  { x1: 421, y1: 167, x2: 335, y2: 199 },
  { x1: 442, y1: 352, x2: 341, y2: 302 },
  { x1: 294, y1: 474, x2: 264, y2: 366 },
  { x1: 101, y1: 386, x2: 174, y2: 318 },
  { x1: 64, y1: 198, x2: 154, y2: 227 },
  { x1: 222, y1: 75, x2: 223, y2: 181 },
  { x1: 411, y1: 105, x2: 316, y2: 204 },
  { x1: 457, y1: 290, x2: 349, y2: 274 },
  { x1: 348, y1: 455, x2: 291, y2: 357 },
  { x1: 165, y1: 427, x2: 195, y2: 358 },
  { x1: 65, y1: 277, x2: 150, y2: 265 },
  { x1: 153, y1: 94, x2: 197, y2: 175 },
  { x1: 340, y1: 93, x2: 294, y2: 163 },
  { x1: 476, y1: 253, x2: 352, y2: 264 },
  { x1: 385, y1: 425, x2: 317, y2: 332 },
  { x1: 221, y1: 448, x2: 221, y2: 376 },
  { x1: 60, y1: 327, x2: 154, y2: 281 },
  { x1: 129, y1: 128, x2: 175, y2: 213 },
  { x1: 304, y1: 67, x2: 267, y2: 173 },
  { x1: 447, y1: 175, x2: 343, y2: 223 },
  { x1: 425, y1: 378, x2: 335, y2: 313 },
  { x1: 273, y1: 463, x2: 250, y2: 377 },
  { x1: 80, y1: 387, x2: 166, y2: 304 },
  { x1: 86, y1: 172, x2: 159, y2: 224 },
  { x1: 247, y1: 64, x2: 238, y2: 172 },
  { x1: 419, y1: 126, x2: 328, y2: 200 },
  { x1: 463, y1: 317, x2: 347, y2: 301 },
  { x1: 308, y1: 473, x2: 278, y2: 352 },
  { x1: 147, y1: 405, x2: 183, y2: 356 },
  { x1: 64, y1: 224, x2: 151, y2: 246 },
  { x1: 175, y1: 78, x2: 210, y2: 163 },
  { x1: 384, y1: 96, x2: 308, y2: 187 },
  { x1: 473, y1: 275, x2: 354, y2: 273 },
  { x1: 387, y1: 455, x2: 306, y2: 367 },
  { x1: 193, y1: 445, x2: 208, y2: 372 },
  { x1: 51, y1: 298, x2: 151, y2: 264 },
  { x1: 154, y1: 116, x2: 187, y2: 205 },
  { x1: 342, y1: 73, x2: 283, y2: 184 },
  { x1: 467, y1: 199, x2: 348, y2: 246 },
];

const chartSetting = {
  yAxis: [
    {
      label: 'rainfall (mm)',
      width: 60,
    },
  ],
  height: 300,
};

```

## Interaction

Since scatter elements can be small, interactions do not require hovering exactly over an element.
When the pointer is in the drawing area, the closest scatter element will be used for interactions (tooltip or highlights).
To do so, the chart computes [Voronoi cells](https://en.wikipedia.org/wiki/Voronoi_diagram) which map the pointer position to the closest element.

You can define a maximal radius with the `voronoiMaxRadius` prop.
If the distance with the pointer is larger than this radius, no item will be selected.
Alternatively, set the `voronoiMaxRadius` prop to `item` to trigger interactions only when hovering exactly over an element instead of Voronoi cells.

```tsx
/* eslint-disable no-nested-ternary */

import * as React from 'react';
import Stack from '@mui/material/Stack';
import FormControlLabel from '@mui/material/FormControlLabel';
import Typography from '@mui/material/Typography';
import Slider from '@mui/material/Slider';
import { ScatterChart } from '@mui/x-charts/ScatterChart';
import Radio from '@mui/material/Radio';
import RadioGroup from '@mui/material/RadioGroup';
import data from '../dataset/random/scatterParallel.json';

export default function VoronoiInteraction() {
  const [option, setOption] = React.useState<'item' | 'undefined' | 'numeric'>(
    'numeric',
  );
  const [voronoiMaxRadius, setVoronoiMaxRadius] = React.useState<number>(25);

  const handleMaxRadiusChange = (event: Event, newValue: number | number[]) => {
    if (typeof newValue !== 'number') {
      return;
    }
    setVoronoiMaxRadius(newValue);
  };

  return (
    <Stack direction="column" sx={{ width: '100%' }}>
      <ScatterChart
        height={300}
        voronoiMaxRadius={
          option === 'undefined'
            ? undefined
            : option === 'item'
              ? 'item'
              : voronoiMaxRadius
        }
        dataset={data}
        series={[
          {
            label: 'Series A',
            data: data.map((v) => ({ x: v.x1, y: v.y1, id: v.id })),
          },
          {
            label: 'Series B',
            data: data.map((v) => ({ x: v.x2, y: v.y2, id: v.id })),
          },
        ]}
      />
      <div>
        <Typography gutterBottom>Maximum radius</Typography>
        <RadioGroup
          onChange={(event) =>
            setOption(event.target.value as 'item' | 'undefined' | 'numeric')
          }
        >
          <Stack direction="row">
            <FormControlLabel
              checked={option === 'item'}
              control={<Radio />}
              label="'item'"
              labelPlacement="end"
              value="item"
            />
            <FormControlLabel
              checked={option === 'undefined'}
              control={<Radio />}
              label="undefined"
              labelPlacement="end"
              value="undefined"
            />
            <FormControlLabel
              checked={option === 'numeric'}
              control={<Radio />}
              label="numeric radius"
              labelPlacement="end"
              value="numeric"
            />
          </Stack>
        </RadioGroup>

        <Typography id="max-radius-value" gutterBottom>
          Numeric radius
        </Typography>
        <Slider
          value={voronoiMaxRadius}
          onChange={handleMaxRadiusChange}
          valueLabelDisplay="auto"
          min={1}
          max={100}
          aria-labelledby="max-radius-value"
          disabled={option !== 'numeric'}
        />
      </div>
    </Stack>
  );
}

```

## Click event

Scatter Chart provides an `onItemClick` handler for handling clicks on specific scatter items.
It has the following signature.

```js
const onItemClick = (
  event, // The mouse event.
  params, // An object that identifies the clicked elements.
) => {};
```

```tsx
import * as React from 'react';
import Stack from '@mui/material/Stack';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import IconButton from '@mui/material/IconButton';
import UndoOutlinedIcon from '@mui/icons-material/UndoOutlined';

import { ScatterChart } from '@mui/x-charts/ScatterChart';

import { HighlightedCode } from '@mui/docs/HighlightedCode';
import { ScatterItemIdentifier } from '@mui/x-charts/models';

const scatterChartsParams = {
  series: [
    {
      id: 'series-1',
      data: [
        { x: 6.5e-2, y: -1.3, id: 0 },
        { x: -2.1, y: -7.0e-1, id: 1 },
        { x: -7.6e-1, y: -6.7e-1, id: 2 },
        { x: -1.5e-2, y: -2.0e-1, id: 3 },
        { x: -1.4, y: -9.9e-1, id: 4 },
        { x: -1.1, y: -1.5, id: 5 },
        { x: -7.0e-1, y: -2.7e-1, id: 6 },
        { x: -5.1e-1, y: -8.8e-1, id: 7 },
        { x: -4.0e-3, y: -1.4, id: 8 },
        { x: -1.3, y: -2.2, id: 9 },
      ],
      label: 'A',
      highlightScope: {
        highlight: 'item',
      },
    },
    {
      id: 'series-2',
      data: [
        { x: 1.8, y: -1.7e-2, id: 0 },
        { x: 7.1e-1, y: 2.6e-1, id: 1 },
        { x: -1.2, y: 9.8e-1, id: 2 },
        { x: 2.0, y: -2.0e-1, id: 3 },
        { x: 9.4e-1, y: -2.7e-1, id: 4 },
        { x: -4.8e-1, y: -1.6e-1, id: 5 },
        { x: -1.5, y: 1.1, id: 6 },
        { x: 1.3, y: 3.4e-1, id: 7 },
        { x: -4.2e-1, y: 1.0e-1, id: 8 },
        { x: 5.4e-2, y: 4.0e-1, id: 9 },
      ],
      label: 'B',
      highlightScope: {
        highlight: 'item',
      },
    },
  ],
  height: 400,
} as const;

export default function ScatterClick() {
  const [data, setData] = React.useState<ScatterItemIdentifier>();

  const { ...other } = data ?? {};
  const dataDisplayed = data && {
    ...other,
  };
  return (
    <Stack
      direction={{ xs: 'column', md: 'row' }}
      spacing={{ xs: 0, md: 4 }}
      sx={{ width: '100%' }}
    >
      <Box sx={{ flexGrow: 1 }}>
        <ScatterChart
          {...scatterChartsParams}
          onItemClick={(_: any, d: ScatterItemIdentifier) => setData(d)}
        />
      </Box>
      <Stack direction="column" sx={{ width: { xs: '100%', md: '40%' } }}>
        <Box
          sx={{
            display: 'flex',
            justifyContent: 'space-between',
            alignItems: 'center',
          }}
        >
          <Typography>Click on the chart</Typography>
          <IconButton
            aria-label="reset"
            size="small"
            onClick={() => setData(undefined)}
          >
            <UndoOutlinedIcon fontSize="small" />
          </IconButton>
        </Box>
        <HighlightedCode
          code={
            dataDisplayed
              ? JSON.stringify(dataDisplayed, null, 1)
              : '// The data will appear here'
          }
          language="json"
          copyButtonHidden
        />
      </Stack>
    </Stack>
  );
}

```

If `voronoiMaxRadius` is `item`, users need to click precisely on the scatter element, and the mouse event will come from this element.

Otherwise, the click behavior will be the same as defined in the [interaction section](#interaction) and the mouse event will come from the svg component.

## Styling

### Color scale

As with other charts, you can modify the [series color](/x/react-charts/styling/#colors) either directly, or with the color palette.

You can also modify the color by using axes `colorMap` which maps values to colors.
The scatter charts use by priority:

1. The z-axis color
2. The y-axis color
3. The x-axis color
4. The series color

:::info
The z-axis is a third axis that lets you customize scatter points independently from their positions.
It can be provided with `zAxis` props.

The value to map can either come from the `z` property of series data, or from the zAxis data.
Here are three ways to set z value to 5.

```jsx
<ScatterChart
  // First option
  series={[{ data: [{ id: 0, x: 1, y: 1, z: 5 }] }]}
  // Second option
  zAxis={[{ data: [5] }]}
  // Third option
  dataset={[{ price: 5 }]}
  zAxis={[{ dataKey: 'price' }]}
/>
```

:::

Learn more about the `colorMap` properties in the [Styling docs](/x/react-charts/styling/#values-color).

```tsx
import * as React from 'react';
import { ScatterChart } from '@mui/x-charts/ScatterChart';
import { ScatterValueType } from '@mui/x-charts/models';
import Stack from '@mui/material/Stack';
import Typography from '@mui/material/Typography';
import ToggleButtonGroup from '@mui/material/ToggleButtonGroup';
import ToggleButton from '@mui/material/ToggleButton';
import { HighlightedCode } from '@mui/docs/HighlightedCode';
import { Chance } from 'chance';

const POINTS_NUMBER = 50;
const chance = new Chance(42);

export default function ColorScale() {
  const [colorX, setColorX] = React.useState<'None' | 'piecewise' | 'continuous'>(
    'piecewise',
  );
  const [colorY, setColorY] = React.useState<'None' | 'piecewise' | 'continuous'>(
    'None',
  );
  const [colorZ, setColorZ] = React.useState<
    'None' | 'piecewise' | 'continuous' | 'ordinal'
  >('None');

  return (
    <Stack direction="column" spacing={1} sx={{ width: '100%', maxWidth: 600 }}>
      <Stack
        direction="row"
        gap={1}
        sx={{
          width: '100%',
          '&>div': {
            display: 'flex',
            flexDirection: 'column',
          },
        }}
        flexWrap="wrap"
      >
        <div>
          <Typography variant="caption">x-axis colorMap</Typography>
          <ToggleButtonGroup
            color="primary"
            size="small"
            exclusive
            value={colorX}
            onChange={(_, value: 'None' | 'piecewise' | 'continuous') =>
              setColorX(value)
            }
            aria-label="Platform"
          >
            <ToggleButton value="None">None</ToggleButton>
            <ToggleButton value="piecewise">piecewise</ToggleButton>
            <ToggleButton value="continuous">continuous</ToggleButton>
          </ToggleButtonGroup>
        </div>
        <div>
          <Typography variant="caption">y-axis colorMap</Typography>
          <ToggleButtonGroup
            color="primary"
            size="small"
            exclusive
            value={colorY}
            onChange={(_, value: 'None' | 'piecewise' | 'continuous') =>
              setColorY(value)
            }
            aria-label="Platform"
          >
            <ToggleButton value="None">None</ToggleButton>
            <ToggleButton value="piecewise">piecewise</ToggleButton>
            <ToggleButton value="continuous">continuous</ToggleButton>
          </ToggleButtonGroup>
        </div>
        <div>
          <Typography variant="caption">z-axis colorMap</Typography>
          <ToggleButtonGroup
            color="primary"
            size="small"
            exclusive
            value={colorZ}
            onChange={(_, value: 'None' | 'piecewise' | 'continuous' | 'ordinal') =>
              setColorZ(value)
            }
            aria-label="Platform"
          >
            <ToggleButton value="None">None</ToggleButton>
            <ToggleButton value="piecewise">piecewise</ToggleButton>
            <ToggleButton value="continuous">continuous</ToggleButton>
            <ToggleButton value="ordinal">ordinal</ToggleButton>
          </ToggleButtonGroup>
        </div>
      </Stack>

      <ScatterChart
        height={300}
        grid={{ horizontal: true, vertical: true }}
        series={series}
        yAxis={[
          {
            min: -3,
            max: 3,
            tickInterval: [-3, -1.5, 0, 1.5, 3],
            colorMap:
              (colorY === 'continuous' && {
                type: 'continuous',
                min: -2,
                max: 2,
                color: ['blue', 'red'],
              }) ||
              (colorY === 'piecewise' && {
                type: 'piecewise',
                thresholds: [-1.5, 0, 1.5],
                colors: ['lightblue', 'blue', 'orange', 'red'],
              }) ||
              undefined,
          },
        ]}
        xAxis={[
          {
            min: -3,
            max: 3,
            tickInterval: [-3, -1.5, 0, 1.5, 3],
            colorMap:
              (colorX === 'continuous' && {
                type: 'continuous',
                min: -2,
                max: 2,
                color: ['green', 'orange'],
              }) ||
              (colorX === 'piecewise' && {
                type: 'piecewise',
                thresholds: [-1.5, 0, 1.5],
                colors: ['#d01c8b', '#f1b6da', '#b8e186', '#4dac26'],
              }) ||
              undefined,
          },
        ]}
        zAxis={[
          {
            data:
              colorZ === 'ordinal'
                ? [
                    ...[...Array(POINTS_NUMBER)].map(() => 'A'),
                    ...[...Array(POINTS_NUMBER)].map(() => 'B'),
                    ...[...Array(POINTS_NUMBER)].map(() => 'C'),
                    ...[...Array(POINTS_NUMBER)].map(() => 'D'),
                  ]
                : undefined,
            colorMap:
              (colorZ === 'continuous' && {
                type: 'continuous',
                min: -2,
                max: 2,
                color: ['green', 'orange'],
              }) ||
              (colorZ === 'piecewise' && {
                type: 'piecewise',
                thresholds: [-1.5, 0, 1.5],
                colors: ['#d01c8b', '#f1b6da', '#b8e186', '#4dac26'],
              }) ||
              (colorZ === 'ordinal' && {
                type: 'ordinal',

                values: ['A', 'B', 'C', 'D'],
                colors: ['#d01c8b', '#f1b6da', '#b8e186', '#4dac26'],
              }) ||
              undefined,
          },
        ]}
      />
      <HighlightedCode
        code={[
          `<ScatterChart`,
          '  /* ... */',
          '  series={[{ data: data.map(point => ({...point, z: point.x + point.y})) }]}',
          // ColorX
          ...(colorX === 'None' ? ['  xAxis={[{}]}'] : []),
          ...(colorX === 'continuous'
            ? [
                '  xAxis={[{',
                `    colorMap: {`,
                `      type: 'continuous',`,
                `      min: -2,`,
                `      max: 2,`,
                `      color: ['green', 'orange']`,
                `    }`,
                '  }]}',
              ]
            : []),
          ...(colorX === 'piecewise'
            ? [
                '  xAxis={[{',
                `    colorMap: {`,
                `      type: 'piecewise',`,
                `      thresholds: [-1.5, 0, 1.5],`,
                `      colors: ['#d01c8b', '#f1b6da', '#b8e186', '#4dac26'],`,
                `    }`,
                '  }]}',
              ]
            : []),

          // ColorY
          ...(colorY === 'None' ? ['  yAxis={[{}]}'] : []),
          ...(colorY === 'continuous'
            ? [
                '  yAxis={[{',
                `    colorMap: {`,
                `      type: 'continuous',`,
                `      min: -2,`,
                `      max: 2,`,
                `      color: ['blue', 'red']`,
                `    }`,
                '  }]}',
              ]
            : []),
          ...(colorY === 'piecewise'
            ? [
                '  yAxis={[{',
                `    colorMap: {`,
                `      type: 'piecewise',`,
                `      thresholds: [-1.5, 0, 1.5],`,
                `      colors: ['lightblue', 'blue', 'orange', 'red'],`,
                `    }`,
                '  }]}',
              ]
            : []),

          // ColorZ
          ...(colorZ === 'None' ? ['  zAxis={[{}]}'] : []),
          ...(colorZ === 'continuous'
            ? [
                '  zAxis={[{',
                `    colorMap: {`,
                `      type: 'continuous',`,
                `      min: -2,`,
                `      max: 2,`,
                `      color: ['green', 'orange'],`,
                `    }`,
                '  }]}',
              ]
            : []),
          ...(colorZ === 'piecewise'
            ? [
                '  zAxis={[{',
                `    colorMap: {`,
                `      type: 'piecewise',`,
                `      thresholds: [-1.5, 0, 1.5],`,
                `      colors: ['#d01c8b', '#f1b6da', '#b8e186', '#4dac26'],`,
                `    }`,
                '  }]}',
              ]
            : []),
          ...(colorZ === 'ordinal'
            ? [
                '  zAxis={[{',
                `    data: ['A', ..., 'B', ..., 'C', ..., 'D', ...],`,
                `    colorMap: {`,
                `      type: 'ordinal',`,
                `      values: ['A', 'B', 'C', 'D'],`,
                `      colors: ['#d01c8b', '#f1b6da', '#b8e186', '#4dac26'],`,
                `    }`,
                '  }]}',
              ]
            : []),
          `/>`,
        ].join('\n')}
        language="jsx"
        copyButtonHidden
      />
    </Stack>
  );
}

const series = [
  {
    data: [
      ...getGaussianSeriesData([-1, -1]),
      ...getGaussianSeriesData([-1, 1]),
      ...getGaussianSeriesData([1, 1]),
      ...getGaussianSeriesData([1, -1]),
    ],
  },
].map((s) => ({
  ...s,
  valueFormatter: (v: ScatterValueType | null) =>
    v && `(${v.x.toFixed(1)}, ${v.y.toFixed(1)})`,
}));

function getGaussianSeriesData(
  mean: [number, number],
  stdev: [number, number] = [0.5, 0.5],
  N: number = 50,
) {
  return [...Array(N)].map((_, i) => {
    const x =
      Math.sqrt(-2.0 * Math.log(1 - chance.floating({ min: 0, max: 0.99 }))) *
        Math.cos(2.0 * Math.PI * chance.floating({ min: 0, max: 0.99 })) *
        stdev[0] +
      mean[0];
    const y =
      Math.sqrt(-2.0 * Math.log(1 - chance.floating({ min: 0, max: 0.99 }))) *
        Math.cos(2.0 * Math.PI * chance.floating({ min: 0, max: 0.99 })) *
        stdev[1] +
      mean[1];
    return { x, y, z: x + y, id: `${mean.join(',')}${i}` };
  });
}

```

### Grid

You can add a grid in the background of the chart with the `grid` prop.

See [Axis—Grid](/x/react-charts/axis/#grid) documentation for more information.

```tsx
import { ScatterChart } from '@mui/x-charts/ScatterChart';
import data from '../dataset/random/scatterParallel.json';

export default function GridDemo() {
  return (
    <ScatterChart
      height={300}
      series={[
        {
          label: 'Series A',
          data: data.map((v) => ({ x: v.x1, y: v.y1, id: v.id })),
        },
        {
          label: 'Series B',
          data: data.map((v) => ({ x: v.x2, y: v.y2, id: v.id })),
        },
      ]}
      grid={{ vertical: true, horizontal: true }}
    />
  );
}

```

### CSS

You can target scatter markers with the following CSS selectors:

- `[data-series='<series id>']` Selects the group containing markers of the series with the given id.
- `[data-highlighted=true]` Selects markers with highlighted state.
- `[data-faded=true]` Selects markers with faded state.

To select all marker groups, use the `scatterClasses.root` class name.

Here is an example that customizes the look of highlighted items depending on the series they belong to.

```tsx
import { ScatterChart, ScatterSeries } from '@mui/x-charts/ScatterChart';
import data from '../dataset/random/scatterParallel.json';

const series: ScatterSeries[] = [
  {
    id: 'series-1',
    label: 'Series A',
    data: data.map((v) => ({ x: v.x1, y: v.y1, id: v.id })),
    highlightScope: { highlight: 'item', fade: 'global' },
  },
  {
    id: 'series-2',
    label: 'Series B',
    data: data.map((v) => ({ x: v.x2, y: v.y2, id: v.id })),
    highlightScope: { highlight: 'item', fade: 'global' },
  },
];

export default function ScatterCSSSelectors() {
  return (
    <ScatterChart
      height={300}
      voronoiMaxRadius={30}
      series={series}
      sx={{
        '& [data-faded=true]': { opacity: 0.4 },
        "& [data-series='series-1'] [data-faded=true]": { fill: 'gray' },
        "& [data-series='series-1'] [data-highlighted=true]": {
          stroke: 'blue',
          strokeWidth: 3,
          fill: 'none',
        },
      }}
    />
  );
}

```

### Shape

The shape of points in a scatter chart can be customized by passing a component to the `marker` slot.

If you want the legend and tooltip to match, then you also need to customize the `labelMarkType` of each series, as shown in the example below.

```tsx
import { ScatterChart, ScatterMarkerProps } from '@mui/x-charts/ScatterChart';
import { ChartsLabelCustomMarkProps } from '@mui/x-charts/ChartsLabel';
import data from '../dataset/random/scatterParallel.json';

export default function ScatterCustomShape() {
  return (
    <ScatterChart
      height={300}
      series={[
        {
          id: '1',
          label: 'Series A',
          data: data.map((v) => ({ x: v.x1, y: v.y1, id: v.id })),
          markerSize: 1,
          labelMarkType: StarLabelMark,
        },
        {
          id: '2',
          label: 'Series B',
          data: data.map((v) => ({ x: v.x2, y: v.y2, id: v.id })),
          markerSize: 1,
          labelMarkType: DiamondLabelMark,
        },
      ]}
      slots={{ marker: CustomMarker }}
    />
  );
}

const star =
  'M0,-7.528L1.69,-2.326L7.16,-2.326L2.735,0.889L4.425,6.09L0,2.875L-4.425,6.09L-2.735,0.889L-7.16,-2.326L-1.69,-2.326Z';
const diamond = 'M0,-7.423L4.285,0L0,7.423L-4.285,0Z';

function CustomMarker({
  size,
  x,
  y,
  seriesId,
  isHighlighted,
  isFaded,
  dataIndex,
  color,
  ...other
}: ScatterMarkerProps) {
  const props = {
    x: 0,
    y: 0,
    width: (isHighlighted ? 1.2 : 1) * size,
    height: (isHighlighted ? 1.2 : 1) * size,
    transform: `translate(${x}, ${y})`,
    fill: color,
    opacity: isFaded ? 0.3 : 1,
    ...other,
  };

  return (
    <g {...props}>
      <path
        d={seriesId === '1' ? star : diamond}
        scale={(isHighlighted ? 1.2 : 1) * size}
      />
    </g>
  );
}

function StarLabelMark({ color, ...props }: ChartsLabelCustomMarkProps) {
  return (
    <svg viewBox="-7.423 -7.423 14.846 14.846">
      <path {...props} d={star} fill={color} />
    </svg>
  );
}

function DiamondLabelMark({ color, ...props }: ChartsLabelCustomMarkProps) {
  return (
    <svg viewBox="-7.423 -7.423 14.846 14.846">
      <path {...props} d={diamond} fill={color} />
    </svg>
  );
}

```

### Size

You can customize the size of points in a scatter chart using the `markerSize` prop of every series.
For circles, the `markerSize` is the radius of the point in pixels.

```tsx
import { ScatterChart } from '@mui/x-charts/ScatterChart';
import data from '../dataset/random/scatterParallel.json';

export default function ScatterCustomSize() {
  return (
    <ScatterChart
      height={300}
      series={[
        {
          label: 'Series A',
          data: data.map((v) => ({ x: v.x1, y: v.y1, id: v.id })),
          markerSize: 8,
        },
        {
          label: 'Series B',
          data: data.map((v) => ({ x: v.x2, y: v.y2, id: v.id })),
          markerSize: 4,
        },
      ]}
    />
  );
}

```

## Plot customization

You can customize the plotting of the data in a scatter chart by providing custom components as `children` of the `ScatterChart` component.

A scatter chart's series can be accessed through the `useScatterSeries` hook.
This hook returns the order of the series and information about the series themselves, including their data points, color, etc.

See [Custom components](/x/react-charts/components/) to learn how to further customize your charts.

```tsx
import { ScatterChart } from '@mui/x-charts/ScatterChart';
import { useScatterSeries, useXScale, useYScale } from '@mui/x-charts/hooks';

const data1 = [
  { x: 95, y: 200, id: 1 },
  { x: 120, y: 100, id: 2 },
  { x: 170, y: 300, id: 3 },
  { x: 140, y: 250, id: 4 },
  { x: 150, y: 400, id: 5 },
  { x: 110, y: 280, id: 6 },
];
const data2 = [
  { x: 300, y: 300, id: 1 },
  { x: 200, y: 700, id: 2 },
  { x: 400, y: 500, id: 3 },
  { x: 340, y: 350, id: 4 },
  { x: 420, y: 280, id: 5 },
];
const series = [
  { id: 's1', data: data1, label: 'Open' },
  { id: 's2', data: data2, label: 'Closed' },
];

function LinkPoints({ seriesId, close }: { seriesId: string; close?: boolean }) {
  const scatter = useScatterSeries(seriesId);
  const xScale = useXScale();
  const yScale = useYScale();

  if (!scatter) {
    return null;
  }
  const { color, data } = scatter;

  if (!data) {
    return null;
  }

  return (
    <path
      fill="none"
      stroke={color}
      strokeWidth={2}
      d={`M ${data.map(({ x, y }) => `${xScale(x)}, ${yScale(y)}`).join(' L')}${
        close ? 'Z' : ''
      }`}
    />
  );
}

export default function CustomScatter() {
  return (
    <ScatterChart series={series} height={300}>
      <LinkPoints seriesId="s1" />
      <LinkPoints seriesId="s2" close />
    </ScatterChart>
  );
}

```

## Performance

Scatter charts can have a lot of data points, which can impact performance. The default rendering of scatter points uses SVG `circle` elements, which can be slow for a large number of points.

To improve performance, you can use the `renderer` prop set to `"svg-batch"`, which renders the circles more efficiently.
However, this comes with the following limitations:

- CSS styling of single `circle` elements is no longer possible;
- Overriding the `marker` slot is not supported;
- Transparent highlight style: for performance reasons, the highlighted state creates a highlighted circle on top of the original marker. Applying transparency to the highlighted circle can cause the original circle to be partially visible;
- `disableHover` for scatter series does not work.

On top of that, there's also some differences in behavior:

- The rendering order might be different, which might cause overlapping circles to render at different depths when compared to the default rendering;
- When `disableVoronoi` is true, `onItemClick` does not work as it requires that plugin to work.

The example below uses the `renderer` prop to improve performance when rendering a dataset with 16,000 data points.

```tsx
import Stack from '@mui/material/Stack';
import Paper from '@mui/material/Paper';
import Divider from '@mui/material/Divider';
import { ChartsTooltipContainer, useItemTooltip } from '@mui/x-charts/ChartsTooltip';
import { ScatterChart, ScatterChartProps } from '@mui/x-charts/ScatterChart';
import Typography from '@mui/material/Typography';
import { schemePaired } from 'd3-scale-chromatic';
import { electricityGeneration2024Every6Hours } from '../dataset/electricityGeneration2024Every6Hours';
import { carbonEmissions2024Every6Hours } from '../dataset/carbonEmissions2024Every6Hours';
import { countryData, flags } from '../dataset/countryData';

const dateFormat = new Intl.DateTimeFormat(undefined, {
  month: 'short',
  day: 'numeric',
});

const timeRangeFormat = new Intl.DateTimeFormat(undefined, {
  hour: '2-digit',
  minute: '2-digit',
});

function getDatesFromIndex(index: number): [Date, Date] {
  const from = new Date(2024, 0, 1, index * 6);
  const to = new Date(2024, 0, 1, index * 6 + 6);
  return [from, to];
}

const scatterChartsParams = {
  series: Object.entries(electricityGeneration2024Every6Hours).map(
    ([countryCode, electricity]) => ({
      id: countryCode,
      data: electricity.map((value, index) => ({
        x: value / 1000,
        y: carbonEmissions2024Every6Hours[
          countryCode as keyof typeof electricityGeneration2024Every6Hours
        ][index],
      })),
      markerSize: 1,
      label:
        countryData[countryCode as keyof typeof electricityGeneration2024Every6Hours]
          .country,
      highlightScope: {
        highlight: 'series',
        fade: 'global',
      },
    }),
  ),
  xAxis: [{ min: 0, label: 'Electricity Generation (GWh)' }],
  yAxis: [{ min: 0, width: 60, label: 'Life-cycle Carbon Intensity (gCO₂eq/kWh)' }],
  height: 400,
  colors: schemePaired,
  slotProps: {
    legend: {
      position: { vertical: 'bottom' },
      sx: { justifyContent: 'center' },
    },
  },
  slots: {
    tooltip: ElectricityTooltip,
  },
} satisfies ScatterChartProps;

export default function ScatterBatchRenderer() {
  return (
    <Stack spacing={{ xs: 0, md: 2 }} sx={{ width: '100%' }}>
      <Typography variant="h6" sx={{ alignSelf: 'center', textAlign: 'center' }}>
        Life-cycle Carbon Intensity of Electricity Generation - 2024
      </Typography>
      <ScatterChart {...scatterChartsParams} renderer="svg-batch" />
      <Typography variant="caption">Source: ENTSO-E, ElectricityMaps.com</Typography>
    </Stack>
  );
}

function ElectricityTooltip() {
  return (
    <ChartsTooltipContainer trigger="item">
      <ElectricityTooltipContent />
    </ChartsTooltipContainer>
  );
}

function ElectricityTooltipContent() {
  const item = useItemTooltip<'scatter'>();

  if (!item) {
    return null;
  }

  const [from, to] = getDatesFromIndex(item.identifier.dataIndex);

  return (
    <Paper sx={{ p: 1.5 }} elevation={4}>
      <Typography
        variant="subtitle2"
        justifyContent={'space-between'}
        display="flex"
      >
        {item.label} {flags[item.identifier.seriesId as keyof typeof flags]}
      </Typography>
      <Typography variant="body2">
        {`${dateFormat.format(from)} ${timeRangeFormat.format(from)} - ${timeRangeFormat.format(to)}`}
      </Typography>
      <Divider sx={{ my: 1 }} />
      <Typography variant="body1">
        Generated:{' '}
        <Typography component="span" variant="body2">
          {item.value.x.toFixed(2)} GWh
        </Typography>
      </Typography>
      <Typography variant="body1">
        Emitting:{' '}
        <Typography component="span" variant="body2">
          {item.value.y.toFixed(2)} gCO₂eq/kWh
        </Typography>
      </Typography>
    </Paper>
  );
}

```

## Composition

Use the `<ChartDataProvider />` to provide `series`, `xAxis`, and `yAxis` props for composition.

In addition to the common chart components available for [composition](/x/react-charts/composition/), you can use the `<ScatterPlot />` component that renders the scatter marks.

Here's how the Scatter Chart is composed:

```jsx
<ChartDataProvider>
  <ChartsWrapper>
    <ChartsLegend />
    <ChartsSurface>
      <ChartsAxis />
      <ChartsGrid />
      <g data-drawing-container>
        {/* Elements able to overflow the drawing area. */}
        <ScatterPlot />
      </g>
      <ChartsOverlay />
      <ChartsAxisHighlight />
    </ChartsSurface>
    <ChartsTooltip trigger="item" />
  </ChartsWrapper>
</ChartDataProvider>
```

:::info
The `data-drawing-container` indicates that children of this element should be considered part of the drawing area, even if they overflow.

See the [Composition—clipping](/x/react-charts/composition/#clipping) for more info.
:::

### Regression line

You add a regression line to a scatter plot by leveraging composition.

```tsx
import * as React from 'react';
import { ScatterChart } from '@mui/x-charts/ScatterChart';
import { useSeries, useXScale, useYScale } from '@mui/x-charts/hooks';
import { ChartsClipPath } from '@mui/x-charts/ChartsClipPath';
import useId from '@mui/utils/useId';
import Stack from '@mui/material/Stack';
import Typography from '@mui/material/Typography';
import { useTheme } from '@mui/material/styles';
import { rainbowSurgePalette } from '@mui/x-charts/colorPalettes';
import { diamonds } from '../dataset/diamonds';

const dollarFormatter = new Intl.NumberFormat('en-US', {
  style: 'currency',
  currency: 'USD',
  maximumFractionDigits: 0,
});

export default function ScatterRegressionLine() {
  return (
    <Stack width="100%">
      <Typography variant="h6" component="span" textAlign="center">
        Relation between Weight and Price of Diamonds
      </Typography>
      <ScatterChart
        dataset={diamonds}
        height={300}
        xAxis={[{ min: 0, label: 'Weight (carats)' }]}
        yAxis={[
          {
            min: 0,
            width: 80,
            valueFormatter: (value: number) => dollarFormatter.format(value),
            label: 'Price (USD)',
          },
        ]}
        series={[
          {
            id: 'diamonds',
            datasetKeys: { x: 'carat', y: 'price' },
            markerSize: 2,
            valueFormatter: (v) =>
              `${dollarFormatter.format(v!.y)} for ${v!.x} carat`,
          },
        ]}
      >
        <RegressionLine seriesId="diamonds" />
      </ScatterChart>

      <Typography variant="caption">Source: OpenML</Typography>
    </Stack>
  );
}

function RegressionLine({ seriesId }: { seriesId: string }) {
  const theme = useTheme();
  const palette = rainbowSurgePalette(theme.palette.mode);
  const stroke = palette[2];
  const allSeries = useSeries();
  const series = allSeries.scatter!.series[seriesId]!;
  const xScale = useXScale(series.xAxisId!);
  const yScale = useYScale(series.yAxisId!);
  const clipPathId = `linear-regression-clip-${useId()}`;

  const { m, b } = linearRegression(series.data ?? []);

  const xDomain = xScale.domain() as [number, number];
  const x1 = xScale(xDomain[0]);
  const x2 = xScale(xDomain[1]);
  const y1 = yScale(m * xDomain[0] + b);
  const y2 = yScale(m * xDomain[1] + b);

  return (
    <React.Fragment>
      <ChartsClipPath id={clipPathId} />
      <g clipPath={`url(#${clipPathId})`}>
        <line x1={x1} y1={y1} x2={x2} y2={y2} stroke={stroke} strokeWidth={2} />
      </g>
    </React.Fragment>
  );
}

function linearRegression(points: ReadonlyArray<{ x: number; y: number }>) {
  const n = points.length;

  // Calculate sums
  let sumX = 0,
    sumY = 0,
    sumXY = 0,
    sumX2 = 0;

  for (let i = 0; i < n; i += 1) {
    const x = points[i].x;
    const y = points[i].y;
    sumX += x;
    sumY += y;
    sumXY += x * y;
    sumX2 += x * x;
  }

  // Calculate slope (m) and intercept (b)
  const m = (n * sumXY - sumX * sumY) / (n * sumX2 - sumX * sumX);
  const b = (sumY - m * sumX) / n;

  return { m, b };
}

```
