# Source: https://mui.com/x/react-charts/bars.md

---
title: React Bar chart
productId: x-charts
components: BarChart, BarChartPro, BarElement, BarPlot, ChartsGrid, BarLabel
---

# Charts - Bars

Bar charts express quantities through a bar's length, using a common baseline.

## Overview

Bar charts are ideal for comparing discrete categories.
They excel at visualizing differences in magnitude across categories (or a group of categories), highlight trends, and compare proportions at a glance.
The categories can represent progressive values such as time periods, or independent groups such as products, countries, age brackets, etc.
Here are the basic requirements to create a bar chart:

- One categorical dimension (x-axis for vertical bars, y-axis for horizontal bars)
- One or more numerical metric for length of each bar

The horizontal bar chart below compares voter turnout in some European countries:

```tsx
import * as React from 'react';
import { useTheme, styled } from '@mui/material/styles';
import Typography from '@mui/material/Typography';
import { BarChart, type BarLabelProps, type BarProps } from '@mui/x-charts/BarChart';
import { useAnimate, useAnimateBar, useDrawingArea } from '@mui/x-charts/hooks';
import { PiecewiseColorLegend } from '@mui/x-charts/ChartsLegend';
import { interpolateObject } from '@mui/x-charts-vendor/d3-interpolate';
import Box from '@mui/material/Box';
import votesTurnout from '../dataset/votes.json';

export default function ShinyBarChartHorizontal() {
  return (
    <Box width="100%">
      <Typography marginBottom={2}>
        European countries with lowest & highest voter turnout
      </Typography>
      <BarChart
        height={300}
        dataset={votesTurnout}
        series={[
          {
            id: 'turnout',
            dataKey: 'turnout',
            stack: 'voter turnout',
            valueFormatter: (value: number | null) => `${value}%`,
          },
        ]}
        layout="horizontal"
        xAxis={[
          {
            id: 'color',
            min: 0,
            max: 100,
            colorMap: {
              type: 'piecewise',
              thresholds: [50, 85],
              colors: ['#d32f2f', '#78909c', '#1976d2'],
            },
            valueFormatter: (value: number) => `${value}%`,
          },
        ]}
        barLabel={(v) => `${v.value}%`}
        yAxis={[
          {
            scaleType: 'band',
            dataKey: 'country',
            width: 140,
          },
        ]}
        slots={{
          legend: PiecewiseColorLegend,
          barLabel: BarLabelAtBase,
          bar: BarShadedBackground,
        }}
        slotProps={{
          legend: {
            axisDirection: 'x',
            markType: 'square',
            labelPosition: 'inline-start',
            labelFormatter: ({ index }) => {
              if (index === 0) {
                return 'lowest turnout';
              }
              if (index === 1) {
                return 'average';
              }
              return 'highest turnout';
            },
          },
        }}
      />
    </Box>
  );
}

export function BarShadedBackground(props: BarProps) {
  const { ownerState, skipAnimation, id, dataIndex, xOrigin, yOrigin, ...other } =
    props;
  const theme = useTheme();

  const animatedProps = useAnimateBar(props);
  const { width } = useDrawingArea();
  return (
    <React.Fragment>
      <rect
        {...other}
        fill={(theme.vars || theme).palette.text.primary}
        opacity={theme.palette.mode === 'dark' ? 0.05 : 0.1}
        x={other.x}
        width={width}
      />
      <rect
        {...other}
        filter={ownerState.isHighlighted ? 'brightness(120%)' : undefined}
        opacity={ownerState.isFaded ? 0.3 : 1}
        data-highlighted={ownerState.isHighlighted || undefined}
        data-faded={ownerState.isFaded || undefined}
        {...animatedProps}
      />
    </React.Fragment>
  );
}

const Text = styled('text')(({ theme }) => ({
  ...theme?.typography?.body2,
  stroke: 'none',
  fill: (theme.vars || theme).palette.common.white,
  transition: 'opacity 0.2s ease-in, fill 0.2s ease-in',
  textAnchor: 'start',
  dominantBaseline: 'central',
  pointerEvents: 'none',
  fontWeight: 600,
}));

function BarLabelAtBase(props: BarLabelProps) {
  const {
    seriesId,
    dataIndex,
    color,
    isFaded,
    isHighlighted,
    classes,
    xOrigin,
    yOrigin,
    x,
    y,
    width,
    height,
    layout,
    skipAnimation,
    ...otherProps
  } = props;

  const animatedProps = useAnimate(
    { x: xOrigin + 8, y: y + height / 2 },
    {
      initialProps: { x: xOrigin, y: y + height / 2 },
      createInterpolator: interpolateObject,
      transformProps: (p) => p,
      applyProps: (element: SVGTextElement, p) => {
        element.setAttribute('x', p.x.toString());
        element.setAttribute('y', p.y.toString());
      },
      skip: skipAnimation,
    },
  );

  return <Text {...otherProps} {...animatedProps} />;
}

```

## Basics

Bar charts series should contain a `data` property containing an array of values.

You can specify bar ticks with the `xAxis` prop.
This axis might have `scaleType='band'` and its `data` should have the same length as your series.

```tsx
import { BarChart } from '@mui/x-charts/BarChart';

export default function BasicBars() {
  return (
    <BarChart
      xAxis={[{ data: ['group A', 'group B', 'group C'] }]}
      series={[{ data: [4, 3, 5] }, { data: [1, 6, 3] }, { data: [2, 5, 6] }]}
      height={300}
    />
  );
}

```

### Using a dataset

If your data is stored in an array of objects, you can use the `dataset` helper prop.
It accepts an array of objects such as `dataset={[{x: 1, y: 32}, {x: 2, y: 41}, ...]}`.

You can reuse this data when defining the series and axis, thanks to the `dataKey` property.

For example `xAxis={[{ dataKey: 'x'}]}` or `series={[{ dataKey: 'y'}]}`.

```tsx
import { BarChart } from '@mui/x-charts/BarChart';
import { dataset, valueFormatter } from '../dataset/weather';

const chartSetting = {
  yAxis: [
    {
      label: 'rainfall (mm)',
      width: 60,
    },
  ],
  height: 300,
};

export default function BarsDataset() {
  return (
    <BarChart
      dataset={dataset}
      xAxis={[{ dataKey: 'month' }]}
      series={[
        { dataKey: 'london', label: 'London', valueFormatter },
        { dataKey: 'paris', label: 'Paris', valueFormatter },
        { dataKey: 'newYork', label: 'New York', valueFormatter },
        { dataKey: 'seoul', label: 'Seoul', valueFormatter },
      ]}
      {...chartSetting}
    />
  );
}

```

## Bar size

You can define bar dimensions with `categoryGapRatio` and `barGapRatio` properties.

The `categoryGapRatio` defines the gap between two categories.
The ratio is obtained by dividing the size of the gap by the size of the category (the space used by bars).

The `barGapRatio` defines the gap between two bars of the same category.
It's the size of the gap divided by the size of the bar.
So a value of `1` will result in a gap between bars equal to the bar width.
And a value of `-1` will make bars overlap on top of each other.

```tsx
import Typography from '@mui/material/Typography';
import ChartsUsageDemo from 'docsx/src/modules/components/ChartsUsageDemo';
import { BarChart } from '@mui/x-charts/BarChart';
import { balanceSheet, addLabels } from './netflixsBalanceSheet';

const series = addLabels([
  { dataKey: 'totAss' },
  { dataKey: 'totLia', stack: 'passive' },
  { dataKey: 'totEq', stack: 'passive' },
]);

export default function BarGap() {
  return (
    <ChartsUsageDemo
      componentName="Bar gap"
      data={{
        categoryGapRatio: {
          knob: 'number',
          defaultValue: 0.3,
          step: 0.1,
          min: 0,
          max: 1,
        },
        barGapRatio: {
          knob: 'number',
          defaultValue: 0.1,
          step: 0.1,
          min: -2,
          max: 5,
        },
      }}
      renderDemo={(props) => (
        <div style={{ width: '100%' }}>
          <Typography>Netflix balance sheet</Typography>
          <BarChart
            dataset={balanceSheet}
            series={series}
            height={300}
            xAxis={[
              {
                dataKey: 'year',
                categoryGapRatio: props.categoryGapRatio,
                barGapRatio: props.barGapRatio,
              },
            ]}
            yAxis={[{ valueFormatter: (v: number) => `$ ${v / 1000000}B` }]}
            hideLegend
          />
        </div>
      )}
      getCode={({ props }) => {
        return `import { BarChart } from '@mui/x-charts/BarChart';

<BarChart
  // ...
  xAxis={[
    {
      scaleType: 'band',
      data: ['Page 1', 'Page 2', 'Page 3'],
      categoryGapRatio: ${props.categoryGapRatio},
      barGapRatio: ${props.barGapRatio},
    },
  ]}
/>`;
      }}
    />
  );
}

```

## Stacking

Bar series accept a string property named `stack`.
Series with the same `stack` value are stacked on top of each other.

```tsx
import Typography from '@mui/material/Typography';
import { BarChart, BarChartProps } from '@mui/x-charts/BarChart';
import { addLabels, balanceSheet, valueFormatter } from './netflixsBalanceSheet';

export default function StackBars() {
  return (
    <div style={{ width: '100%' }}>
      <Typography>Netflix balance sheet</Typography>
      <BarChart
        dataset={balanceSheet}
        series={addLabels([
          { dataKey: 'currAss', stack: 'assets' },
          { dataKey: 'nCurrAss', stack: 'assets' },
          { dataKey: 'curLia', stack: 'liability' },
          { dataKey: 'nCurLia', stack: 'liability' },
          { dataKey: 'capStock', stack: 'equity' },
          { dataKey: 'retEarn', stack: 'equity' },
          { dataKey: 'treas', stack: 'equity' },
        ])}
        xAxis={[{ dataKey: 'year' }]}
        {...config}
      />
    </div>
  );
}

const config: Partial<BarChartProps> = {
  height: 350,
  margin: { left: 0 },
  yAxis: [{ width: 50, valueFormatter }],
  hideLegend: true,
};

```

### Stacking strategy

You can use the `stackOffset` and `stackOrder` properties to define how the series will be stacked.

By default, they are stacked in the order you defined them, with positive values stacked above 0 and negative values stacked below 0.

For more information, see [stacking docs](/x/react-charts/stacking/).

## Layout

### Bar direction

Bar charts can be rendered with a horizontal layout by providing the `layout="horizontal"` prop.
If you're using [composition](/x/react-charts/composition/), you should set the property `layout: 'horizontal'` to each bar series object.

```tsx
import { BarChart } from '@mui/x-charts/BarChart';
import { dataset, valueFormatter } from '../dataset/weather';

const chartSetting = {
  xAxis: [
    {
      label: 'rainfall (mm)',
    },
  ],
  height: 400,
  margin: { left: 0 },
};

export default function HorizontalBars() {
  return (
    <BarChart
      dataset={dataset}
      yAxis={[{ scaleType: 'band', dataKey: 'month' }]}
      series={[{ dataKey: 'seoul', label: 'Seoul rainfall', valueFormatter }]}
      layout="horizontal"
      {...chartSetting}
    />
  );
}

```

### Tick placement

When using a `"band"` scale, the axis has some additional customization properties about the tick position.

- `tickPlacement` for the position of ticks
- `tickLabelPlacement` for the position of the label associated with the tick

You can test all configuration options in the following demo:

```tsx
import * as React from 'react';
import Stack from '@mui/material/Stack';
import FormControl from '@mui/material/FormControl';
import FormLabel from '@mui/material/FormLabel';
import RadioGroup from '@mui/material/RadioGroup';
import FormControlLabel from '@mui/material/FormControlLabel';
import Radio from '@mui/material/Radio';
import { BarChart } from '@mui/x-charts/BarChart';
import { dataset, valueFormatter } from '../dataset/weather';

type TickParamsSelectorProps = {
  tickPlacement: 'end' | 'start' | 'middle' | 'extremities';
  tickLabelPlacement: 'tick' | 'middle';
  setTickPlacement: React.Dispatch<
    React.SetStateAction<'end' | 'start' | 'middle' | 'extremities'>
  >;
  setTickLabelPlacement: React.Dispatch<React.SetStateAction<'tick' | 'middle'>>;
};

function TickParamsSelector({
  tickPlacement,
  tickLabelPlacement,
  setTickPlacement,
  setTickLabelPlacement,
}: TickParamsSelectorProps) {
  return (
    <Stack direction="column" justifyContent="space-between" sx={{ width: '100%' }}>
      <FormControl>
        <FormLabel id="tick-placement-radio-buttons-group-label">
          tickPlacement
        </FormLabel>
        <RadioGroup
          row
          aria-labelledby="tick-placement-radio-buttons-group-label"
          name="tick-placement"
          value={tickPlacement}
          onChange={(event) =>
            setTickPlacement(
              event.target.value as 'start' | 'end' | 'middle' | 'extremities',
            )
          }
        >
          <FormControlLabel value="start" control={<Radio />} label="start" />
          <FormControlLabel value="end" control={<Radio />} label="end" />
          <FormControlLabel value="middle" control={<Radio />} label="middle" />
          <FormControlLabel
            value="extremities"
            control={<Radio />}
            label="extremities"
          />
        </RadioGroup>
      </FormControl>
      <FormControl>
        <FormLabel id="label-placement-radio-buttons-group-label">
          tickLabelPlacement
        </FormLabel>
        <RadioGroup
          row
          aria-labelledby="label-placement-radio-buttons-group-label"
          name="label-placement"
          value={tickLabelPlacement}
          onChange={(event) =>
            setTickLabelPlacement(event.target.value as 'tick' | 'middle')
          }
        >
          <FormControlLabel value="tick" control={<Radio />} label="tick" />
          <FormControlLabel value="middle" control={<Radio />} label="middle" />
        </RadioGroup>
      </FormControl>
    </Stack>
  );
}

const chartSetting = {
  yAxis: [
    {
      label: 'rainfall (mm)',
      width: 60,
    },
  ],
  series: [{ dataKey: 'seoul', label: 'Seoul rainfall', valueFormatter }],
  height: 300,
  margin: { left: 0 },
};

export default function TickPlacementBars() {
  const [tickPlacement, setTickPlacement] = React.useState<
    'start' | 'end' | 'middle' | 'extremities'
  >('middle');
  const [tickLabelPlacement, setTickLabelPlacement] = React.useState<
    'middle' | 'tick'
  >('middle');

  return (
    <div style={{ width: '100%' }}>
      <TickParamsSelector
        tickPlacement={tickPlacement}
        tickLabelPlacement={tickLabelPlacement}
        setTickPlacement={setTickPlacement}
        setTickLabelPlacement={setTickLabelPlacement}
      />
      <BarChart
        dataset={dataset}
        xAxis={[{ dataKey: 'month', tickPlacement, tickLabelPlacement }]}
        {...chartSetting}
      />
    </div>
  );
}

```

### Date axis

If your band axis represents dates in a usual way (they are sorted and evenly spaced), you can set `ordinalTimeTicks` to pick some date frequencies.
This modifies the [tick management](/x/react-charts/axis/#ordinal-tick-management).

Instead of one tick per band, the axis renders ticks according to the provided frequencies and the tick number.

### Minimum bar size

You can set a minimum bar size with the `minBarSize` property.
This property is useful when you want to ensure that bars are always visible, even when the data is sparse or the chart is small.

The `minBarSize` property is ignored if the series value is `null` or `0`.
It also doesn't work with stacked series.

```tsx
import * as React from 'react';
import Stack from '@mui/material/Stack';
import Typography from '@mui/material/Typography';
import Slider from '@mui/material/Slider';
import { BarChart } from '@mui/x-charts/BarChart';

// Create sparse data where some bars would be very small
const sparseData: (number | null)[] = [0.02, 5, null, 7, 0.01, 0, -0.03];

export default function MinBarSize(): React.JSX.Element {
  const [minBarSize, setMinBarSize] = React.useState<number>(10);

  const handleChange = (event: Event, newValue: number | number[]) => {
    if (typeof newValue !== 'number') {
      return;
    }
    setMinBarSize(newValue);
  };

  return (
    <Stack spacing={2} justifyContent={'center'} alignItems={'center'}>
      <Typography id="min-bar-size-slider" gutterBottom>
        minBarSize: {minBarSize}px
      </Typography>
      <Slider
        value={minBarSize}
        onChange={handleChange}
        aria-labelledby="min-bar-size-slider"
        min={0}
        max={50}
        sx={{ width: 300 }}
      />
      <BarChart
        xAxis={[{ data: sparseData.map((v) => `${v}`), scaleType: 'band' }]}
        series={[{ data: sparseData, minBarSize }]}
        height={300}
        width={400}
      />
    </Stack>
  );
}

```

### Log scale

A bar chart renders a bar from 0 to the value of a data point. However, the logarithm of zero is undefined, meaning that a y-axis with a log scale cannot plot the bar.

You can work around this limitation by using a [symlog scale](/x/react-charts/axis/#symlog-scale).

## Customization

### Grid

You can add a grid in the background of the chart with the `grid` prop.

See [Axis—Grid](/x/react-charts/axis/#grid) documentation for more information.

```tsx
import { BarChart } from '@mui/x-charts/BarChart';
import { dataset, valueFormatter } from '../dataset/weather';

const chartSetting = {
  xAxis: [{ label: 'rainfall (mm)' }],
  height: 400,
  margin: { left: 0 },
};

export default function GridDemo() {
  return (
    <BarChart
      dataset={dataset}
      yAxis={[{ scaleType: 'band', dataKey: 'month' }]}
      series={[{ dataKey: 'seoul', label: 'Seoul rainfall', valueFormatter }]}
      layout="horizontal"
      grid={{ vertical: true }}
      {...chartSetting}
    />
  );
}

```

### Color scale

As with other charts, you can modify the [series color](/x/react-charts/styling/#colors) either directly, or with the color palette.

You can also modify the color by using axes `colorMap` which maps values to colors.
The bar charts use by priority:

1. The value axis color
2. The band axis color
3. The series color

Learn more about the `colorMap` properties in the [Styling docs](/x/react-charts/styling/#values-color).

```tsx
import * as React from 'react';
import { BarChart } from '@mui/x-charts/BarChart';
import Stack from '@mui/material/Stack';
import TextField from '@mui/material/TextField';
import MenuItem from '@mui/material/MenuItem';
import { HighlightedCode } from '@mui/docs/HighlightedCode';

const series = [{ data: [-2, -9, 12, 11, 6, -4] }];

export default function ColorScale() {
  const [colorX, setColorX] = React.useState<
    'None' | 'piecewise' | 'continuous' | 'ordinal'
  >('piecewise');
  const [colorY, setColorY] = React.useState<'None' | 'piecewise' | 'continuous'>(
    'None',
  );

  return (
    <Stack direction="column" spacing={1} sx={{ width: '100%', maxWidth: 600 }}>
      <Stack direction="row" spacing={1}>
        <TextField
          select
          sx={{ minWidth: 150 }}
          label="x-axis colorMap"
          value={colorX}
          onChange={(event) =>
            setColorX(
              event.target.value as 'None' | 'piecewise' | 'continuous' | 'ordinal',
            )
          }
        >
          <MenuItem value="None">None</MenuItem>
          <MenuItem value="piecewise">piecewise</MenuItem>
          <MenuItem value="continuous">continuous</MenuItem>
          <MenuItem value="ordinal">ordinal</MenuItem>
        </TextField>
        <TextField
          select
          sx={{ minWidth: 150 }}
          label="y-axis colorMap"
          value={colorY}
          onChange={(event) =>
            setColorY(event.target.value as 'None' | 'piecewise' | 'continuous')
          }
        >
          <MenuItem value="None">None</MenuItem>
          <MenuItem value="piecewise">piecewise</MenuItem>
          <MenuItem value="continuous">continuous</MenuItem>
        </TextField>
      </Stack>

      <BarChart
        height={300}
        grid={{ horizontal: true }}
        series={series}
        yAxis={[
          {
            colorMap:
              (colorY === 'continuous' && {
                type: 'continuous',
                min: -10,
                max: 10,
                color: ['red', 'green'],
              }) ||
              (colorY === 'piecewise' && {
                type: 'piecewise',
                thresholds: [0],
                colors: ['red', 'green'],
              }) ||
              undefined,
          },
        ]}
        xAxis={[
          {
            data: [
              new Date(2019, 1, 1),
              new Date(2020, 1, 1),
              new Date(2021, 1, 1),
              new Date(2022, 1, 1),
              new Date(2023, 1, 1),
              new Date(2024, 1, 1),
            ],
            valueFormatter: (value: Date) => value.getFullYear().toString(),
            colorMap:
              (colorX === 'ordinal' && {
                type: 'ordinal',
                colors: [
                  '#ccebc5',
                  '#a8ddb5',
                  '#7bccc4',
                  '#4eb3d3',
                  '#2b8cbe',
                  '#08589e',
                ],
              }) ||
              (colorX === 'continuous' && {
                type: 'continuous',
                min: new Date(2019, 1, 1),
                max: new Date(2024, 1, 1),
                color: ['green', 'orange'],
              }) ||
              (colorX === 'piecewise' && {
                type: 'piecewise',
                thresholds: [new Date(2021, 1, 1), new Date(2023, 1, 1)],
                colors: ['blue', 'red', 'blue'],
              }) ||
              undefined,
          },
        ]}
        margin={{ left: 0 }}
      />
      <HighlightedCode
        code={[
          `<BarChart`,
          '  /* ... */',
          // ColorX
          ...(colorX === 'None' ? ['  xAxis={[{}]}'] : []),
          ...(colorX === 'ordinal'
            ? [
                '  xAxis={[{',
                `    colorMap: {`,
                `      type: 'ordinal',`,
                `      colors: ['#ccebc5', '#a8ddb5', '#7bccc4', '#4eb3d3', '#2b8cbe', '#08589e']`,
                `    }`,
                '  }]}',
              ]
            : []),
          ...(colorX === 'continuous'
            ? [
                '  xAxis={[{',
                `    colorMap: {`,
                `      type: 'continuous',`,
                `      min: new Date(2019, 1, 1),`,
                `      max: new Date(2024, 1, 1),`,
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
                `      thresholds: [new Date(2021, 1, 1), new Date(2023, 1, 1)],`,
                `      colors: ['blue', 'red', 'blue'],`,
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
                `      min: -10,`,
                `      max: 10,`,
                `      color: ['red', 'green'],`,
                `    }`,
                '  }]}',
              ]
            : []),
          ...(colorY === 'piecewise'
            ? [
                '  yAxis={[{',
                `    colorMap: {`,
                `      type: 'piecewise',`,
                `      thresholds: [0],`,
                `      colors: ['red', 'green'],`,
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

```

### Border radius

To give your bar chart rounded corners, you can change the value of the `borderRadius` property on the [BarChart](/x/api/charts/bar-chart/#bar-chart-prop-slots).

It works with any positive value and is properly applied to horizontal layouts, stacks, and negative values.

When using composition, you can set the `borderRadius` prop on the `BarPlot` component.

```tsx
import * as React from 'react';
import { BarChart, BarChartProps } from '@mui/x-charts/BarChart';
import Stack from '@mui/material/Stack';
import { HighlightedCode } from '@mui/docs/HighlightedCode';
import TextField from '@mui/material/TextField';
import MenuItem from '@mui/material/MenuItem';
import Slider from '@mui/material/Slider';
import Typography from '@mui/material/Typography';
import Checkbox from '@mui/material/Checkbox';
import FormControlLabel from '@mui/material/FormControlLabel';

export default function BorderRadius() {
  const [layout, setLayout] = React.useState<'horizontal' | 'vertical'>('vertical');
  const [radius, setRadius] = React.useState(10);
  const [reverse, setReverse] = React.useState(false);

  return (
    <Stack direction="column" spacing={1} sx={{ width: '100%', maxWidth: 600 }}>
      <Stack direction="row" spacing={4} flexWrap="wrap" justifyContent="center">
        <Stack direction="column" spacing={1} flex={1}>
          <Typography gutterBottom>Border Radius</Typography>
          <Slider
            value={radius}
            onChange={(event, value) => setRadius(value as number)}
            valueLabelDisplay="auto"
            min={0}
            max={50}
            sx={{ mt: 2 }}
          />
        </Stack>
        <TextField
          select
          sx={{ minWidth: 150 }}
          label="layout"
          value={layout}
          onChange={(event) =>
            setLayout(event.target.value as 'horizontal' | 'vertical')
          }
        >
          <MenuItem value="horizontal">Horizontal</MenuItem>
          <MenuItem value="vertical">Vertical</MenuItem>
        </TextField>
        <FormControlLabel
          checked={reverse}
          control={
            <Checkbox onChange={(event) => setReverse(event.target.checked)} />
          }
          label="Reverse"
          labelPlacement="end"
        />
      </Stack>
      <BarChart
        series={[
          { dataKey: 'high', label: 'High', layout, stack: 'stack' },
          { dataKey: 'low', label: 'Low', layout, stack: 'stack' },
        ]}
        margin={{ left: 0 }}
        {...getChartSettings(layout, reverse)}
        borderRadius={radius}
      />
      <HighlightedCode
        code={`<BarChart
  // ...
  borderRadius={${radius}}
/>`}
        language="jsx"
        copyButtonHidden
      />
    </Stack>
  );
}

const dataset = [
  [3, -7, '1st'],
  [0, -5, '2nd'],
  [10, 0, '3rd'],
  [9, 6, '4th'],
].map(([high, low, order]) => ({
  high,
  low,
  order,
}));

function getChartSettings(
  layout: 'vertical' | 'horizontal',
  reverse: boolean,
): Partial<BarChartProps> {
  return {
    dataset,
    height: 300,
    xAxis: layout === 'horizontal' ? [{ reverse }] : [{ dataKey: 'order' }],
    yAxis:
      layout === 'horizontal'
        ? [{ scaleType: 'band', dataKey: 'order' }]
        : [{ reverse }],
    slotProps: {
      legend: {
        direction: 'horizontal',
        position: { vertical: 'bottom', horizontal: 'center' },
      },
    },
  };
}

```

### CSS

You can customize the bar chart elements using CSS selectors.

Each series renders a `g` element that contains a `data-series` attribute.
You can use this attribute to target elements based on their series.

```tsx
import * as React from 'react';
import {
  BarChart,
  barClasses,
  barElementClasses,
  barLabelClasses,
} from '@mui/x-charts/BarChart';

const settings = {
  xAxis: [{ data: ['group A', 'group B', 'group C'] }],
  series: [
    { id: '1', data: [4, 3, 5] },
    { id: '2', data: [1, 6, 3] },
    { id: '3', data: [2, 5, 6] },
  ],
  height: 300,
  barLabel: 'value',
  margin: { left: 0 },
} as const;

export default function BarGradient() {
  return (
    <BarChart
      {...settings}
      sx={{
        [`& .${barClasses.series}[data-series="2"] .${barElementClasses.root}`]: {
          fill: 'url(#bar-gradient)',
        },
        [`& .${barClasses.seriesLabels}[data-series="2"] .${barLabelClasses.root}`]:
          {
            fontWeight: 'bold',
          },
      }}
    >
      <defs>
        <Gradient id="bar-gradient" />
      </defs>
    </BarChart>
  );
}

function Gradient(props: React.SVGProps<SVGLinearGradientElement>) {
  return (
    <linearGradient gradientTransform="rotate(90)" {...props}>
      <stop offset="5%" stopColor="gold" />
      <stop offset="95%" stopColor="red" />
    </linearGradient>
  );
}

```

### Gradients

By default, a gradient's units are set to [`objectBoundingBox`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/gradientUnits#objectboundingbox).
When applied to a bar, the gradient stretches to fill the entire size of the bar, regardless of the bar's value.

Alternatively, you can set `gradientUnits` to `userSpaceOnUse`, which stretches the gradient to fill the entire size of the chart.
`userSpaceOnUse` means that the gradient's coordinates are relative to the SVG, meaning that a gradient with `x1="0"` and `x2="100%"` stretches across the entire width of the SVG.
This effectively reveals the gradient depending on the bar's value, as the gradient is clipped to the bar's size.

```tsx
import * as React from 'react';
import { BarChart, BarChartProps, barElementClasses } from '@mui/x-charts/BarChart';
import Stack from '@mui/material/Stack';
import Typography from '@mui/material/Typography';
import FormControl from '@mui/material/FormControl';
import FormLabel from '@mui/material/FormLabel';
import RadioGroup from '@mui/material/RadioGroup';
import FormControlLabel from '@mui/material/FormControlLabel';
import Radio from '@mui/material/Radio';
import { countryData } from '../dataset/countryData';
import householdSavings from '../dataset/oecdHouseholdSavings2024.json';

/* Source: https://www.oecd.org/en/data/indicators/household-savings.html */
const savings = Object.entries(householdSavings)
  .map(([country, value]) => ({
    country,
    value,
  }))
  .sort((a, b) => a.value - b.value);

const percentageFormatter = new Intl.NumberFormat('en-US', {
  style: 'percent',
  maximumFractionDigits: 1,
});

const settings = {
  height: 600,
  xAxis: [{ label: 'Household Savings (%)' }],
  layout: 'horizontal',
  hideLegend: true,
} satisfies Partial<BarChartProps>;

export default function BarOECDHouseholdSavings() {
  const [gradientUnits, setGradientUnits] = React.useState<
    'objectBoundingBox' | 'userSpaceOnUse'
  >('userSpaceOnUse');

  return (
    <Stack width="100%">
      <Typography variant="h6" textAlign="center">
        Household Savings in OECD Countries (2016)
      </Typography>

      <FormControl fullWidth>
        <FormLabel id="gradient-units-label">Gradient Units</FormLabel>
        <RadioGroup
          row
          aria-labelledby="gradient-units-label"
          name="gradient-units"
          value={gradientUnits}
          onChange={(event) =>
            setGradientUnits(
              event.target.value as 'objectBoundingBox' | 'userSpaceOnUse',
            )
          }
        >
          <FormControlLabel
            value="objectBoundingBox"
            control={<Radio />}
            label="objectBoundingBox (default)"
          />
          <FormControlLabel
            value="userSpaceOnUse"
            control={<Radio />}
            label="userSpaceOnUse"
          />
        </RadioGroup>
      </FormControl>

      <BarChart
        {...settings}
        yAxis={[
          {
            data: savings.map((v) => v.country),
            valueFormatter: (value: keyof typeof countryData) =>
              countryData[value].country,
            width: 100,
          },
        ]}
        series={[
          {
            label: 'Household Savings',
            data: savings.map((v) => v.value),
            color: 'url(#savings-gradient)',
            valueFormatter: (value) => percentageFormatter.format(value! / 100),
          },
        ]}
        sx={
          gradientUnits === 'userSpaceOnUse'
            ? {
                [`.${barElementClasses.root}`]: {
                  fill: 'url(#savings-gradient-user-space)',
                },
              }
            : undefined
        }
      >
        <Gradient id="savings-gradient" x1="0" x2="100%" />
        <Gradient
          id="savings-gradient-user-space"
          gradientUnits="userSpaceOnUse"
          x1="150"
          x2="100%"
        />
      </BarChart>
      <Typography variant="caption">Source: Our World in Data</Typography>
    </Stack>
  );
}

function Gradient(props: React.SVGProps<SVGLinearGradientElement>) {
  return (
    <linearGradient x1="0" y1="0%" x2="100%" y2="0%" {...props}>
      <stop offset="0" stopColor="#ff2f1b" />
      <stop offset="0.5" stopColor="#fce202" />
      <stop offset="1" stopColor="#02b32b" />
    </linearGradient>
  );
}

```

Note that, in the example above, there are two gradients:

- The series `color` property references the gradient with `gradientUnits="objectBoundingBox"`, which is applied to the tooltip, legend, and other elements that reference the series color.
- The bar's `fill` property is overridden using CSS to reference the gradient with `gradientUnits="userSpaceOnUse"`.

The first gradient is used for elements showing the whole gradient, such as tooltips and legend.
The second one is shown in the bars themselves that display the part of the gradient that corresponds to their value.

## Labels

You can display labels on the bars. This can be useful to show the value of each bar directly on the chart.

If you provide `'value'` to the `barLabel` property of a bar series, the value of that bar is shown.
Alternatively, the `barLabel` property accepts a function that is called with the bar item and context about the bar.

In the example below, the value of the first series is displayed using the default formatter, and format the value of the second series as US dollars. The labels of the third series are hidden.

```tsx
import { BarChart } from '@mui/x-charts/BarChart';

const dollarFormatter = new Intl.NumberFormat('en-US', {
  style: 'currency',
  currency: 'USD',
  maximumFractionDigits: 0,
});

export default function BarLabel() {
  return (
    <BarChart
      xAxis={[{ data: ['group A', 'group B', 'group C'] }]}
      series={[
        { data: [4, 3, 5], barLabel: 'value' },
        {
          data: [1, 6, 3],
          barLabel: (item) => dollarFormatter.format(item.value!),
        },
        { data: [2, 5, 6] },
      ]}
      height={300}
      margin={{ left: 0 }}
      yAxis={[{ width: 30 }]}
    />
  );
}

```

### Label placement

The position of the bar label can be customized.
To do so, set a series' `barLabelPlacement` property to one of the following values:

- `center`: the label is centered on the bar;
- `outside`: the label is placed after the end of the bar, from the point of the view of the origin. For a vertical positive bar, the label is above its top edge; for a horizontal negative bar, the label is placed to the left of its leftmost limit.

```tsx
import { BarChart } from '@mui/x-charts/BarChart';

export default function BarLabelPlacement() {
  return (
    <BarChart
      xAxis={[{ data: ['group A', 'group B', 'group C'] }]}
      series={[
        { data: [1, 1, -4], barLabel: 'value', barLabelPlacement: 'outside' },
        { data: [2, 0, -1], barLabel: 'value', barLabelPlacement: 'center' },
        { data: [3, -1, 4], barLabel: 'value' },
      ]}
      height={300}
      yAxis={[{ width: 30, min: -5 }]}
    />
  );
}

```

:::info
When using `outside` placement, if the label does not fit in the chart area, it will be clipped.
To avoid this, you can decrease/increase the axis min/max respectively so that there's enough space for the labels.
:::

### Custom labels

You can display, change, or hide labels based on conditional logic.
To do so, provide a function to the `barLabel`.
Labels are not displayed if the function returns `null`.

In the example we display a `'High'` text on values higher than 10, and hide values when the generated bar height is lower than 60px.

```tsx
import { BarChart } from '@mui/x-charts/BarChart';

export default function CustomLabels() {
  return (
    <BarChart
      series={[
        { data: [4, 2, 5, 4, 1], stack: 'A', label: 'Series A1' },
        { data: [2, 8, 1, 3, 1], stack: 'A', label: 'Series A2' },
        { data: [14, 6, 5, 8, 9], label: 'Series B1' },
      ]}
      barLabel={(item, context) => {
        if ((item.value ?? 0) > 10) {
          return 'High';
        }
        return context.bar.height < 60 ? null : item.value?.toString();
      }}
      height={350}
      margin={{ left: 0 }}
    />
  );
}

```

You can further customize the labels by providing a component to the `barLabel` slot.

In the example below, we position the labels above the bars they refer to.

```tsx
import { useAnimate } from '@mui/x-charts/hooks';
import { ChartContainer } from '@mui/x-charts/ChartContainer';
import { BarLabelProps, BarPlot } from '@mui/x-charts/BarChart';
import { ChartsXAxis } from '@mui/x-charts/ChartsXAxis';
import { ChartsYAxis } from '@mui/x-charts/ChartsYAxis';
import { styled } from '@mui/material/styles';
import { interpolateObject } from '@mui/x-charts-vendor/d3-interpolate';

export default function LabelsAboveBars() {
  return (
    <ChartContainer
      xAxis={[{ scaleType: 'band', data: ['A', 'B', 'C'] }]}
      series={[{ type: 'bar', id: 'base', data: [5, 17, 11] }]}
      height={400}
      yAxis={[{ width: 30 }]}
      margin={{ left: 0, right: 10 }}
    >
      <BarPlot barLabel="value" slots={{ barLabel: BarLabel }} />
      <ChartsXAxis />
      <ChartsYAxis />
    </ChartContainer>
  );
}

const Text = styled('text')(({ theme }) => ({
  ...theme?.typography?.body2,
  stroke: 'none',
  fill: (theme.vars || theme)?.palette?.text?.primary,
  transition: 'opacity 0.2s ease-in, fill 0.2s ease-in',
  textAnchor: 'middle',
  dominantBaseline: 'central',
  pointerEvents: 'none',
}));

function BarLabel(props: BarLabelProps) {
  const {
    seriesId,
    dataIndex,
    color,
    isFaded,
    isHighlighted,
    classes,
    xOrigin,
    yOrigin,
    x,
    y,
    width,
    height,
    layout,
    skipAnimation,
    ...otherProps
  } = props;

  const animatedProps = useAnimate(
    { x: x + width / 2, y: y - 8 },
    {
      initialProps: { x: x + width / 2, y: yOrigin },
      createInterpolator: interpolateObject,
      transformProps: (p) => p,
      applyProps: (element: SVGTextElement, p) => {
        element.setAttribute('x', p.x.toString());
        element.setAttribute('y', p.y.toString());
      },
      skip: skipAnimation,
    },
  );

  return (
    <Text {...otherProps} fill={color} textAnchor="middle" {...animatedProps} />
  );
}

```

## Click event

Bar charts provides two click handlers:

- `onItemClick` for click on a specific bar.
- `onAxisClick` for a click anywhere in the chart

They both provide the following signature.

```js
const clickHandler = (
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

import { BarChart } from '@mui/x-charts/BarChart';

import { HighlightedCode } from '@mui/docs/HighlightedCode';
import { BarItemIdentifier, ChartsAxisData } from '@mui/x-charts/models';

const barChartsParams = {
  series: [
    {
      id: 'series-1',
      data: [3, 4, 1, 6, 5],
      label: 'A',
      stack: 'total',
      highlightScope: {
        highlight: 'item',
      },
    },
    {
      id: 'series-2',
      data: [4, 3, 1, 5, 8],
      label: 'B',
      stack: 'total',
      highlightScope: {
        highlight: 'item',
      },
    },
    {
      id: 'series-3',
      data: [4, 2, 5, 4, 1],
      label: 'C',
      highlightScope: {
        highlight: 'item',
      },
    },
  ],
  xAxis: [{ data: ['0', '3', '6', '9', '12'], id: 'axis1' }],
  height: 400,
  margin: { left: 0 },
} as const;

export default function BarClick() {
  const [itemData, setItemData] = React.useState<BarItemIdentifier>();
  const [axisData, setAxisData] = React.useState<ChartsAxisData | null>();

  return (
    <Stack
      direction={{ xs: 'column', md: 'row' }}
      spacing={{ xs: 0, md: 4 }}
      sx={{ width: '100%' }}
    >
      <Box sx={{ flexGrow: 1 }}>
        <BarChart
          {...barChartsParams}
          onItemClick={(event, d) => setItemData(d)}
          onAxisClick={(event, d) => setAxisData(d)}
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
            onClick={() => {
              setItemData(undefined);
              setAxisData(null);
            }}
          >
            <UndoOutlinedIcon fontSize="small" />
          </IconButton>
        </Box>
        <HighlightedCode
          code={`// Data from item click
${itemData ? JSON.stringify(itemData, null, 2) : '// The data will appear here'}

// Data from axis click
${axisData ? JSON.stringify(axisData, null, 2) : '// The data will appear here'}
`}
          language="json"
          copyButtonHidden
        />
      </Stack>
    </Stack>
  );
}

```

:::info
There is a slight difference between the `event` of `onItemClick` and `onAxisClick`:

- For `onItemClick` it's a React synthetic mouse event emitted by the bar component.
- For `onAxisClick` it's a native mouse event emitted by the svg component.

:::

If you're composing a custom component, you can incorporate click events as shown in the code snippet below.
Note that `onAxisClick` can handle both bar and line series if you mix them.

```jsx
<ChartContainer onAxisClick={onAxisClick}>
  {/* ... */}
  <BarPlot onItemClick={onItemClick} />
</ChartContainer>
```

## Animation

Chart containers respect [`prefers-reduced-motion`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-reduced-motion), but you can also disable animations manually by setting the `skipAnimation` prop to `true`.

When `skipAnimation` is enabled, the chart renders without any animations.

```jsx
// For a single component chart
<BarChart skipAnimation />

// For a composed chart
<ChartContainer>
  <BarPlot skipAnimation />
</ChartContainer>
```

```tsx
import * as React from 'react';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import Slider from '@mui/material/Slider';
import FormControlLabel from '@mui/material/FormControlLabel';
import Checkbox from '@mui/material/Checkbox';
import { BarChart } from '@mui/x-charts/BarChart';
import { HighlightScope } from '@mui/x-charts/context';

export default function BarAnimation() {
  const [seriesNb, setSeriesNb] = React.useState(2);
  const [itemNb, setItemNb] = React.useState(5);
  const [skipAnimation, setSkipAnimation] = React.useState(false);

  const handleItemNbChange = (event: Event, newValue: number | number[]) => {
    if (typeof newValue !== 'number') {
      return;
    }
    setItemNb(newValue);
  };
  const handleSeriesNbChange = (event: Event, newValue: number | number[]) => {
    if (typeof newValue !== 'number') {
      return;
    }
    setSeriesNb(newValue);
  };

  return (
    <Box sx={{ width: '100%' }}>
      <BarChart
        height={300}
        series={series
          .slice(0, seriesNb)
          .map((s) => ({ ...s, data: s.data.slice(0, itemNb) }))}
        skipAnimation={skipAnimation}
        margin={{ left: 0 }}
      />
      <FormControlLabel
        checked={skipAnimation}
        control={
          <Checkbox onChange={(event) => setSkipAnimation(event.target.checked)} />
        }
        label="skipAnimation"
        labelPlacement="end"
      />
      <Typography id="input-item-number" gutterBottom>
        Number of items
      </Typography>
      <Slider
        value={itemNb}
        onChange={handleItemNbChange}
        valueLabelDisplay="auto"
        min={1}
        max={20}
        aria-labelledby="input-item-number"
      />
      <Typography id="input-series-number" gutterBottom>
        Number of series
      </Typography>
      <Slider
        value={seriesNb}
        onChange={handleSeriesNbChange}
        valueLabelDisplay="auto"
        min={1}
        max={10}
        aria-labelledby="input-series-number"
      />
    </Box>
  );
}

const highlightScope: HighlightScope = {
  highlight: 'series',
  fade: 'global',
};

const series = [
  {
    label: 'series 1',
    data: [
      2423, 2210, 764, 1879, 1478, 1373, 1891, 2171, 620, 1269, 724, 1707, 1188,
      1879, 626, 1635, 2177, 516, 1793, 1598,
    ],
  },
  {
    label: 'series 2',
    data: [
      2362, 2254, 1962, 1336, 586, 1069, 2194, 1629, 2173, 2031, 1757, 862, 2446,
      910, 2430, 2300, 805, 1835, 1684, 2197,
    ],
  },
  {
    label: 'series 3',
    data: [
      1145, 1214, 975, 2266, 1768, 2341, 747, 1282, 1780, 1766, 2115, 1720, 1057,
      2000, 1716, 2253, 619, 1626, 1209, 1786,
    ],
  },
  {
    label: 'series 4',
    data: [
      2361, 979, 2430, 1768, 1913, 2342, 1868, 1319, 1038, 2139, 1691, 935, 2262,
      1580, 692, 1559, 1344, 1442, 1593, 1889,
    ],
  },
  {
    label: 'series 5',
    data: [
      968, 1371, 1381, 1060, 1327, 934, 1779, 1361, 878, 1055, 1737, 2380, 875, 2408,
      1066, 1802, 1442, 1567, 1552, 1742,
    ],
  },
  {
    label: 'series 6',
    data: [
      2316, 1845, 2057, 1479, 1859, 1015, 1569, 1448, 1354, 1007, 799, 1748, 1454,
      1968, 1129, 1196, 2158, 540, 1482, 880,
    ],
  },
  {
    label: 'series 7',
    data: [
      2140, 2082, 708, 2032, 554, 1365, 2121, 1639, 2430, 2440, 814, 1328, 883, 1811,
      2322, 1743, 700, 2131, 1473, 957,
    ],
  },
  {
    label: 'series 8',
    data: [
      1074, 744, 2487, 823, 2252, 2317, 2139, 1818, 2256, 1769, 1123, 1461, 672,
      1335, 960, 1871, 2305, 1231, 2005, 908,
    ],
  },
  {
    label: 'series 9',
    data: [
      1792, 886, 2472, 1546, 2164, 2323, 2435, 1268, 2368, 2158, 2200, 1316, 552,
      1874, 1771, 1038, 1838, 2029, 1793, 1117,
    ],
  },
  {
    label: 'series 10',
    data: [
      1433, 1161, 1107, 1517, 1410, 1058, 676, 1280, 1936, 1774, 698, 1721, 1421,
      785, 1752, 800, 990, 1809, 1985, 665,
    ],
  },
].map((s) => ({ ...s, highlightScope }));

```

## Composition

Use the `<ChartDataProvider />` to provide `series`, `xAxis`, and `yAxis` props for composition.

In addition to the common chart components available for [composition](/x/react-charts/composition/), you can use the `<BarPlot />` component that renders the bars and their labels.

Here's how the Bar Chart is composed:

```jsx
<ChartDataProvider>
  <ChartsWrapper>
    <ChartsLegend />
    <ChartsSurface>
      <ChartsGrid />
      <g clipPath={`url(#${clipPathId})`}>
        <BarPlot />
        <ChartsOverlay />
        <ChartsAxisHighlight />
      </g>
      <ChartsAxis />
      <ChartsClipPath id={clipPathId} />
    </ChartsSurface>
    <ChartsTooltip />
  </ChartsWrapper>
</ChartDataProvider>
```

```tsx
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import { BarPlot } from '@mui/x-charts/BarChart';
import { ScatterPlot } from '@mui/x-charts/ScatterChart';
import { ChartsXAxis } from '@mui/x-charts/ChartsXAxis';
import { ChartsYAxis } from '@mui/x-charts/ChartsYAxis';
import { ChartsGrid } from '@mui/x-charts/ChartsGrid';
import { ChartDataProvider } from '@mui/x-charts/ChartDataProvider';
import { ChartsSurface } from '@mui/x-charts/ChartsSurface';
import { ChartsTooltip } from '@mui/x-charts/ChartsTooltip';
import { legendClasses, ChartsLegend } from '@mui/x-charts/ChartsLegend';
import { GDPdata } from '../dataset/gdpGrowth';

const chartSetting = {
  xAxis: [
    {
      id: 'bar',
      label: 'GDP growth rate',
      dataKey: '2024',
      colorMap: {
        type: 'piecewise' as const,
        thresholds: [0],
        colors: ['#ff4d4f', '#1976d2'],
      },
    },
    {
      id: 'scatter',
      label: '2010-19 Average',
      dataKey: '2010_19',
      color: '#FFFF00',
    },
  ],
  height: 800,
};

const valueFormatter = (value: number | null) =>
  value ? `${value.toFixed(2)}%` : '';

const scatterValueFormatter = (value: { x: number } | null) =>
  value ? `${value.x.toFixed(2)}%` : '';

function Gradient() {
  return (
    <linearGradient id="diagonalGradient" x1="0%" y1="50%" x2="100%" y2="50%">
      <stop offset="0%" stopColor="#ff4d4f" />
      <stop offset="50%" stopColor="#ff4d4f" />
      <stop offset="50%" stopColor="#1976d2" />
      <stop offset="100%" stopColor="#1976d2" />
    </linearGradient>
  );
}

export default function BarScatterCompostion() {
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
      <Typography variant="h6">
        GDP growth rate comparison (2024 vs 2010-19 Avg)
      </Typography>
      <ChartDataProvider
        dataset={GDPdata}
        series={[
          {
            id: 'bar',
            type: 'bar',
            layout: 'horizontal',
            dataKey: '2024',
            label: '2024 ',
            valueFormatter,
          },
          {
            id: 'scatter',
            type: 'scatter',
            datasetKeys: { id: 'country', x: '2010_19', y: 'country' },
            label: '2010-19 Average',
            valueFormatter: scatterValueFormatter,
            markerSize: 4,
            xAxisId: 'scatter',
          },
        ]}
        yAxis={[{ scaleType: 'band', dataKey: 'country', width: 100 }]}
        {...chartSetting}
      >
        <ChartsLegend
          sx={{
            [`[data-series="bar"] .${legendClasses.mark} rect`]: {
              fill: 'url(#diagonalGradient)',
            },
          }}
        />
        <ChartsTooltip />
        <ChartsSurface>
          <Gradient />
          <ChartsGrid vertical />
          <BarPlot />
          <ScatterPlot />
          <ChartsXAxis axisId="bar" />
          <ChartsYAxis />
        </ChartsSurface>
      </ChartDataProvider>
    </Box>
  );
}

```
