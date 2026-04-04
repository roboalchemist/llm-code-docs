# Source: https://mui.com/x/react-data-grid/components/charts-panel.md

---
title: Data Grid - Charts Panel component
productId: x-data-grid
components: ChartsPanelTrigger
packageName: '@mui/x-data-grid-premium'
githubLabel: 'scope: data grid'
---

# Data Grid - Charts Panel component [<span class="plan-premium"></span>](/x/introduction/licensing/#premium-plan 'Premium plan') 🚧

Customize the Data Grid's Charts panel.

:::warning
This component is incomplete.

Currently, the Charts Panel Trigger is the only part of the Charts Panel component available.
Future versions of the Charts Panel component will make it possible to compose each of its parts for full customization.

:::

The Charts panel is part of the [Charts integration feature](/x/react-data-grid/charts-integration/).

You can use the Charts Panel Trigger and [Toolbar](/x/react-data-grid/components/toolbar/) components when you need to customize the Charts panel trigger, or when implementing a custom toolbar.

## Basic usage

The demo below shows how to add a Charts Panel Trigger to a custom toolbar.

```tsx
import {
  DataGridPremium,
  Toolbar,
  ToolbarButton,
  ChartsPanelTrigger,
  GridChartsPanel,
  GridChartsIcon,
  GridChartsIntegrationContextProvider,
  GridChartsRendererProxy,
} from '@mui/x-data-grid-premium';
import { useDemoData } from '@mui/x-data-grid-generator';
import Tooltip from '@mui/material/Tooltip';
import { configurationOptions } from '@mui/x-charts-premium/ChartsRenderer';

function CustomToolbar() {
  return (
    <Toolbar>
      <Tooltip title="Charts">
        <ChartsPanelTrigger render={<ToolbarButton />}>
          <GridChartsIcon fontSize="small" />
        </ChartsPanelTrigger>
      </Tooltip>
    </Toolbar>
  );
}

export default function GridChartsPanelTrigger() {
  const { data, loading } = useDemoData({
    dataSet: 'Employee',
    rowLength: 10,
    maxColumns: 10,
  });

  return (
    <GridChartsIntegrationContextProvider>
      <div style={{ height: 400, width: '100%' }}>
        <DataGridPremium
          {...data}
          loading={loading}
          chartsIntegration
          slots={{ toolbar: CustomToolbar, chartsPanel: GridChartsPanel }}
          slotProps={{
            chartsPanel: {
              schema: configurationOptions,
            },
          }}
          showToolbar
          initialState={{
            ...data.initialState,
            chartsIntegration: {
              charts: {
                main: {
                  chartType: 'column',
                },
              },
            },
          }}
          experimentalFeatures={{
            charts: true,
          }}
        />
      </div>
      <GridChartsRendererProxy id="main" renderer={() => null} />
    </GridChartsIntegrationContextProvider>
  );
}

```

## Anatomy

```tsx
import { ChartsPanelTrigger } from '@mui/x-data-grid-premium';

<ChartsPanelTrigger />;
```

### Charts Panel Trigger

`<ChartsPanelTrigger />` is a button that opens and closes the Charts panel.
It renders the `baseButton` slot.

## Custom elements

Use the `render` prop to replace default elements.
See [Components usage—Customization](/x/react-data-grid/components/usage/#customization) for more details.

## Accessibility

### ARIA

You must apply a text label or an `aria-label` attribute to the `<ChartsPanelTrigger />`.


# ChartsPanelTrigger API

## Demos

For examples and details on the usage of this React component, visit the component demo pages:

- Data Grid - Charts Panel component 🚧

## Import

```jsx
import { ChartsPanelTrigger } from '@mui/x-data-grid-premium/components';
// or
import { ChartsPanelTrigger } from '@mui/x-data-grid-premium';
```

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| className | `func \| string` | - | No |  |
| render | `element \| func` | - | No |  |

> **Note**: The `ref` is forwarded to the root element (GridRoot).

## Source code

If you did not find the information on this page, consider having a look at the implementation of the component for more detail.

- [/packages/x-data-grid-premium/src/components/chartsPanel/ChartsPanelTrigger.tsx](https://github.com/mui/material-ui/tree/HEAD/packages/x-data-grid-premium/src/components/chartsPanel/ChartsPanelTrigger.tsx)