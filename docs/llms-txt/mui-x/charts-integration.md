# Source: https://mui.com/x/react-data-grid/charts-integration.md

---
title: Data Grid and Charts integration
---

# Charts integration [<span class="plan-premium"></span>](/x/introduction/licensing/#premium-plan 'Premium plan') 🧪

Use the MUI X Charts to visualize data from the Data Grid.

Data Grid seamlessly integrates with [MUI X Charts](/x/react-charts/) for data visualization with dynamic Chart updates based on the Data Grid state changes (whether through the Data Grid API or user interactions).

:::warning
This feature is in preview. It is ready for production use, but its API, visuals and behavior may change in future minor or patch releases.

To use the feature, add `charts` experimental flag on top of other props described below.

```tsx
<DataGridPremium
  // ...other props
  experimentalFeatures={{
    charts: true,
  }}
/>
```

:::

This integration is possible via the `<GridChartsIntegrationContextProvider />` and `<GridChartsRendererProxy />` components from `@mui/x-data-grid-premium` and the `<ChartRenderer />` component from the `@mui/x-charts-premium` package.

Based on its internal models, the Grid calculates and stores the data in a format that is easy to use for chart rendering.
`<ChartRenderer />` reads that data and renders an appropriate chart component with props that depend on the configuration stored in the context.

## Implementing Charts and Data Grid integration

To enable chart integration, pass the `chartsIntegration` prop to the Grid and `<GridChartsPanel />` to the `chartsPanel` slot.
This enables the charts panel and makes it possible for the charts integration context provider state to receive updates.

```tsx
import { DataGridPremium, GridChartsPanel } from '@mui/x-data-grid-premium';
// ...

return (
  <DataGridPremium
    chartsIntegration
    slots={{
      chartsPanel: GridChartsPanel,
      // ...other slots
    }}
    // ...other props
  />
);
```

Wrap your Grid and chart renderer in a `<GridChartsIntegrationContextProvider />`.
Use `<GridChartsRendererProxy />` to connect the chart renderer to the Grid's state updates.

```tsx
import {
  DataGridPremium,
  GridChartsIntegrationContextProvider,
  GridChartsRendererProxy,
} from '@mui/x-data-grid-premium';
import { ChartsRenderer } from '@mui/x-charts-premium/ChartsRenderer';
// ...

return (
  <GridChartsIntegrationContextProvider>
    <DataGridPremium
    // ...props
    />
    <GridChartsRendererProxy id="main" renderer={ChartsRenderer} />
  </GridChartsIntegrationContextProvider>
);
```

### Basic integration

The demo below shows all the basic elements needed to get the charts integration working.
Use `initialState` to set the initial configuration for the chart renderer.

```tsx
import { useDemoData } from '@mui/x-data-grid-generator';
import {
  DataGridPremium,
  GridChartsPanel,
  GridChartsIntegrationContextProvider,
  GridChartsRendererProxy,
  GridSidebarValue,
} from '@mui/x-data-grid-premium';
import {
  ChartsRenderer,
  configurationOptions,
} from '@mui/x-charts-premium/ChartsRenderer';

export default function GridChartsIntegrationBasic() {
  const { data } = useDemoData({
    dataSet: 'Employee',
    rowLength: 20,
    editable: true,
  });

  return (
    <GridChartsIntegrationContextProvider>
      <div style={{ gap: 32, width: '100%' }}>
        <div style={{ height: 420, paddingBottom: 16 }}>
          <DataGridPremium
            {...data}
            showToolbar
            chartsIntegration
            slots={{
              chartsPanel: GridChartsPanel,
            }}
            slotProps={{
              chartsPanel: {
                schema: configurationOptions,
              },
            }}
            initialState={{
              sidebar: {
                open: true,
                value: GridSidebarValue.Charts,
              },
              chartsIntegration: {
                charts: {
                  main: {
                    dimensions: ['name'],
                    values: ['salary'],
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
        <GridChartsRendererProxy id="main" renderer={ChartsRenderer} />
      </div>
    </GridChartsIntegrationContextProvider>
  );
}

```

## Row grouping

You can integrate charts with grouped and aggregated data.
The Grid's grouping and aggregation states are reflected in the chart.

```tsx
import * as React from 'react';
import {
  DataGridPremium,
  GridChartsPanel,
  GridChartsIntegrationContextProvider,
  GridChartsRendererProxy,
  useGridApiRef,
  useKeepGroupedColumnsHidden,
  GridSidebarValue,
} from '@mui/x-data-grid-premium';
import {
  ChartsRenderer,
  configurationOptions,
} from '@mui/x-charts-premium/ChartsRenderer';
import { useDemoData } from '@mui/x-data-grid-generator';

// make sure that the commodity labels are not overlapping on the initial load
// this is just for the demo
// the logic needs an update to cover other possible configurations
const onRender = (
  type: string,
  props: Record<string, any>,
  Component: React.ComponentType<any>,
) => {
  if (type === 'pie') {
    return <Component {...props} />;
  }

  const axisProp = type === 'bar' ? 'yAxis' : 'xAxis';
  const adjustedProps = {
    ...props,
    [axisProp]: props[axisProp].map((axisProps: Record<string, any>) => ({
      ...axisProps,
      groups: axisProps.groups?.map(
        (axisGroup: { getValue: (value: any) => string }, index: number) => ({
          ...axisGroup,
          getValue: (value: string[]) => {
            const targetIndex = axisProps.groups.length - 1 - index;
            if (targetIndex === 0) {
              return value[0];
            }

            return value[targetIndex][0];
          },
        }),
      ),
    })),
  };

  return <Component {...adjustedProps} />;
};

export default function GridChartsIntegrationRowGrouping() {
  const { data } = useDemoData({
    dataSet: 'Commodity',
    rowLength: 100,
    editable: true,
  });

  const apiRef = useGridApiRef();

  const initialState = useKeepGroupedColumnsHidden({
    apiRef,
    initialState: {
      ...data.initialState,
      rowGrouping: {
        ...data.initialState?.rowGrouping,
        model: ['status', 'commodity'],
      },
      aggregation: {
        ...data.initialState?.aggregation,
        model: {
          filledQuantity: 'avg',
          feeRate: 'sum',
        },
      },
      sidebar: {
        open: true,
        value: GridSidebarValue.Charts,
      },
      chartsIntegration: {
        charts: {
          main: {
            dimensions: ['status', 'commodity'],
            values: ['filledQuantity', 'feeRate'],
            chartType: 'column',
          },
        },
      },
    },
  });

  return (
    <GridChartsIntegrationContextProvider>
      <div style={{ gap: 32, width: '100%' }}>
        <div style={{ height: 420, paddingBottom: 16 }}>
          <DataGridPremium
            {...data}
            showToolbar
            chartsIntegration
            slots={{
              chartsPanel: GridChartsPanel,
            }}
            slotProps={{
              chartsPanel: {
                schema: configurationOptions,
              },
            }}
            initialState={initialState}
            experimentalFeatures={{
              charts: true,
            }}
          />
        </div>
        <GridChartsRendererProxy
          id="main"
          renderer={ChartsRenderer}
          onRender={onRender}
        />
      </div>
    </GridChartsIntegrationContextProvider>
  );
}

```

## Pivoting

[Pivoting](/x/react-data-grid/pivoting/) creates columns dynamically, based on the pivoting model.
The names of those columns are determined by the values used to generate them, which makes it impossible to initialize `values` with those values.
Use the [`updateChartValuesData()`](/x/api/data-grid/grid-api/#grid-api-prop-updateChartValuesData) to update the chart's value datasets after the columns are created.

```tsx
const apiRef = useGridApiRef();

React.useEffect(() => {
  const handleColumnVisibilityModelChange = () => {
    // Get dynamically created columns
    const unwrappedGroupingModel = Object.keys(
      gridColumnGroupsUnwrappedModelSelector(apiRef),
    );
    // Update chart value datasets
    apiRef.current?.updateChartValuesData(
      'main',
      unwrappedGroupingModel
        .filter((field) => field.endsWith('quantity'))
        .slice(0, 5)
        .map((field, index) => ({ field, hidden: index >= 3 })),
    );
  };
  return apiRef.current?.subscribeEvent(
    'columnVisibilityModelChange',
    handleColumnVisibilityModelChange,
  );
}, [apiRef]);
```

```tsx
import * as React from 'react';
import {
  DataGridPremium,
  GridChartsPanel,
  GridChartsIntegrationContextProvider,
  GridChartsRendererProxy,
  gridColumnGroupsUnwrappedModelSelector,
  GridEventListener,
  GridPivotModel,
  useGridApiRef,
} from '@mui/x-data-grid-premium';
import {
  ChartsRenderer,
  configurationOptions,
} from '@mui/x-charts-premium/ChartsRenderer';
import { useDemoData } from '@mui/x-data-grid-generator';

export default function GridChartsIntegrationPivoting() {
  const { data } = useDemoData({
    dataSet: 'Commodity',
    rowLength: 1000,
    editable: true,
  });
  const apiRef = useGridApiRef();

  const pivotModel: GridPivotModel = {
    rows: [{ field: 'commodity' }],
    columns: [
      { field: 'maturityDate-year', sort: 'asc' },
      { field: 'maturityDate-quarter', sort: 'asc' },
    ],
    values: [
      { field: 'quantity', aggFunc: 'sum' },
      { field: 'feeRate', aggFunc: 'avg' },
    ],
  };

  const initialState = {
    ...data.initialState,
    pivoting: {
      model: pivotModel,
      enabled: true,
    },
    chartsIntegration: {
      charts: {
        main: {
          dimensions: ['commodity'],
          chartType: 'column',
        },
      },
    },
  };

  const hasInitializedPivotingSeries = React.useRef(false);
  React.useEffect(() => {
    const handleColumnVisibilityModelChange: GridEventListener<
      'columnVisibilityModelChange'
    > = () => {
      if (!apiRef.current || hasInitializedPivotingSeries.current) {
        return;
      }

      const unwrappedGroupingModel = Object.keys(
        gridColumnGroupsUnwrappedModelSelector(apiRef),
      );
      // wait until pivoting creates column grouping model
      if (unwrappedGroupingModel.length === 0) {
        return;
      }

      hasInitializedPivotingSeries.current = true;
      // pick up the first 5 dyamically created columns with quantity in the name and enable first 3
      apiRef.current.updateChartValuesData(
        'main',
        unwrappedGroupingModel
          .filter((field) => field.endsWith('quantity'))
          .slice(0, 5)
          .map((field, index) => ({ field, hidden: index >= 3 })),
      );
    };

    return apiRef.current?.subscribeEvent(
      'columnVisibilityModelChange',
      handleColumnVisibilityModelChange,
    );
  }, [apiRef]);

  return (
    <GridChartsIntegrationContextProvider>
      <div style={{ gap: 32, width: '100%' }}>
        <div style={{ height: 575, paddingBottom: 16 }}>
          <DataGridPremium
            {...data}
            apiRef={apiRef}
            showToolbar
            chartsIntegration
            slots={{
              chartsPanel: GridChartsPanel,
            }}
            slotProps={{
              chartsPanel: {
                schema: configurationOptions,
              },
            }}
            initialState={initialState}
            checkboxSelection
            columnGroupHeaderHeight={35}
            experimentalFeatures={{
              charts: true,
            }}
          />
        </div>
        <GridChartsRendererProxy id="main" renderer={ChartsRenderer} />
      </div>
    </GridChartsIntegrationContextProvider>
  );
}

```

## Server-side data

The following demo shows charts integration with the grid using [Server-side data](/x/react-data-grid/server-side-data/).

```tsx
import * as React from 'react';
import { useMockServer } from '@mui/x-data-grid-generator';
import {
  DataGridPremium,
  GridChartsPanel,
  GridChartsIntegrationContextProvider,
  GridChartsRendererProxy,
  GridSidebarValue,
  useKeepGroupedColumnsHidden,
  GridDataSource,
  useGridApiRef,
  GridPivotModel,
  GridEventListener,
  gridColumnGroupsUnwrappedModelSelector,
  gridPivotModelSelector,
  DataGridPremiumProps,
} from '@mui/x-data-grid-premium';
import {
  ChartsRenderer,
  configurationOptions,
} from '@mui/x-charts-premium/ChartsRenderer';

const initialPivotModel: GridPivotModel = {
  rows: [{ field: 'commodity' }],
  columns: [{ field: 'incoTerm' }],
  values: [{ field: 'quantity', aggFunc: 'sum' }],
};

const aggregationFunctions = {
  sum: { columnTypes: ['number'] },
  avg: { columnTypes: ['number'] },
  min: { columnTypes: ['number', 'date', 'dateTime'] },
  max: { columnTypes: ['number', 'date', 'dateTime'] },
  size: {},
};

const pivotingColDef: DataGridPremiumProps['pivotingColDef'] = (
  originalColumnField,
  columnGroupPath,
) => ({
  field: columnGroupPath.concat(originalColumnField).join('>->'),
});

export default function GridChartsIntegrationDataSource() {
  const apiRef = useGridApiRef();

  const { fetchRows, initialState, columns } = useMockServer(
    {
      rowLength: 1000,
      dataSet: 'Commodity',
      maxColumns: 20,
    },
    { useCursorPagination: false },
  );

  const dataSource: GridDataSource = React.useMemo(() => {
    return {
      getRows: async (params) => {
        const urlParams = new URLSearchParams({
          paginationModel: JSON.stringify(params.paginationModel),
          filterModel: JSON.stringify(params.filterModel),
          sortModel: JSON.stringify(params.sortModel),
          groupKeys: JSON.stringify(params.groupKeys),
          groupFields: JSON.stringify(params.groupFields),
          aggregationModel: JSON.stringify(params.aggregationModel),
          pivotModel: JSON.stringify(params.pivotModel),
        });
        const getRowsResponse = await fetchRows(
          `https://mui.com/x/api/data-grid?${urlParams.toString()}`,
        );
        return {
          rows: getRowsResponse.rows,
          rowCount: getRowsResponse.rowCount,
          aggregateRow: getRowsResponse.aggregateRow,
          pivotColumns: getRowsResponse.pivotColumns,
        };
      },
      getGroupKey: (row) => row.group,
      getChildrenCount: (row) => row.descendantCount,
      getAggregatedValue: (row, field) => row[field],
    };
  }, [fetchRows]);

  const initialStateUpdated = useKeepGroupedColumnsHidden({
    apiRef,
    initialState: {
      ...initialState,
      pivoting: {
        model: initialPivotModel,
        enabled: true,
      },
      sidebar: {
        open: true,
        value: GridSidebarValue.Charts,
      },
      chartsIntegration: {
        charts: {
          main: {
            dimensions: ['commodity'],
            values: [],
            chartType: 'column',
          },
        },
      },
    },
  });

  const hasInitializedPivotingSeries = React.useRef(false);
  React.useEffect(() => {
    const handleColumnsChange: GridEventListener<'columnsChange'> = () => {
      if (!apiRef.current || hasInitializedPivotingSeries.current) {
        return;
      }

      const unwrappedGroupingModel = Object.keys(
        gridColumnGroupsUnwrappedModelSelector(apiRef),
      );
      // wait until pivoting creates column grouping model
      if (unwrappedGroupingModel.length === 0) {
        return;
      }

      const pivotModel = gridPivotModelSelector(apiRef);
      const targetField = pivotModel.values.find(
        (value) => value.hidden !== true,
      )?.field;

      hasInitializedPivotingSeries.current = true;

      if (targetField) {
        apiRef.current.updateChartValuesData(
          'main',
          unwrappedGroupingModel
            .filter((field) => field.endsWith(targetField))
            .map((field) => ({ field })),
        );
      }
    };

    return apiRef.current?.subscribeEvent('columnsChange', handleColumnsChange);
  }, [apiRef]);

  return (
    <GridChartsIntegrationContextProvider>
      <div style={{ gap: 32, width: '100%' }}>
        <div style={{ height: 600, paddingBottom: 16 }}>
          <DataGridPremium
            columns={columns}
            dataSource={dataSource}
            apiRef={apiRef}
            showToolbar
            chartsIntegration
            slots={{
              chartsPanel: GridChartsPanel,
            }}
            slotProps={{
              chartsPanel: {
                schema: configurationOptions,
              },
            }}
            initialState={initialStateUpdated}
            aggregationFunctions={aggregationFunctions}
            pivotingColDef={pivotingColDef}
            experimentalFeatures={{
              charts: true,
            }}
          />
        </div>
        <GridChartsRendererProxy id="main" renderer={ChartsRenderer} />
      </div>
    </GridChartsIntegrationContextProvider>
  );
}

```

## Multiple charts

Control multiple charts with one grid by adding more `<GridChartsRendererProxy />` components with unique IDs.
Each chart can have its own configuration and state.

```tsx
<GridChartsRendererProxy id="quantity" label="Quantity" renderer={ChartsRenderer} />
<GridChartsRendererProxy id="feeRate" label="Fee Rate" renderer={ChartsRenderer} />
```

```tsx
import * as React from 'react';
import {
  DataGridPremium,
  GridChartsPanel,
  GridChartsIntegrationContextProvider,
  GridChartsRendererProxy,
  gridColumnGroupsUnwrappedModelSelector,
  GridEventListener,
  GridPivotModel,
  useGridApiRef,
} from '@mui/x-data-grid-premium';
import {
  ChartsRenderer,
  configurationOptions,
} from '@mui/x-charts-premium/ChartsRenderer';
import { useDemoData } from '@mui/x-data-grid-generator';

export default function GridChartsIntegrationMultipleCharts() {
  const { data } = useDemoData({
    dataSet: 'Commodity',
    rowLength: 1000,
    editable: true,
  });
  const apiRef = useGridApiRef();

  const pivotModel: GridPivotModel = {
    rows: [{ field: 'dateCreated-quarter' }],
    columns: [
      { field: 'maturityDate-year', sort: 'asc' },
      { field: 'maturityDate-quarter', sort: 'asc' },
    ],
    values: [
      { field: 'quantity', aggFunc: 'sum' },
      { field: 'feeRate', aggFunc: 'avg' },
    ],
  };

  const initialState = {
    ...data.initialState,
    pivoting: {
      model: pivotModel,
      enabled: true,
    },
    chartsIntegration: {
      charts: {
        quantity: {
          chartType: 'bar',
        },
        feeRate: {
          chartType: 'line',
        },
      },
    },
  };

  const hasInitializedPivotingSeries = React.useRef(false);
  React.useEffect(() => {
    const handleColumnVisibilityModelChange: GridEventListener<
      'columnVisibilityModelChange'
    > = () => {
      if (hasInitializedPivotingSeries.current) {
        return;
      }

      const unwrappedGroupingModel = Object.keys(
        gridColumnGroupsUnwrappedModelSelector(apiRef),
      );
      // wait until pivoting creates column grouping model
      if (unwrappedGroupingModel.length === 0) {
        return;
      }

      hasInitializedPivotingSeries.current = true;

      // add columns dynamically created by pivoting
      // they cannot be added to the initial state because they are not available at that time and will be cleaned up by the state initializer
      apiRef.current?.updateChartDimensionsData('quantity', [
        { field: 'dateCreated-quarter', hidden: false },
      ]);
      apiRef.current?.updateChartValuesData(
        'quantity',
        unwrappedGroupingModel
          .filter((field) => field.endsWith('quantity'))
          .slice(0, 5)
          .map((field, index) => ({ field, hidden: index >= 3 })),
      );
      apiRef.current?.updateChartDimensionsData('feeRate', [
        { field: 'dateCreated-quarter', hidden: false },
      ]);
      apiRef.current?.updateChartValuesData(
        'feeRate',
        unwrappedGroupingModel
          .filter((field) => field.endsWith('feeRate'))
          .slice(0, 5)
          .map((field, index) => ({ field, hidden: index >= 3 })),
      );
    };

    return apiRef.current?.subscribeEvent(
      'columnVisibilityModelChange',
      handleColumnVisibilityModelChange,
    );
  }, [apiRef]);

  return (
    <GridChartsIntegrationContextProvider>
      <div style={{ gap: 32, width: '100%' }}>
        <div style={{ height: 575, paddingBottom: 16 }}>
          <DataGridPremium
            {...data}
            apiRef={apiRef}
            showToolbar
            chartsIntegration
            slots={{
              chartsPanel: GridChartsPanel,
            }}
            slotProps={{
              chartsPanel: {
                schema: configurationOptions,
              },
            }}
            initialState={initialState}
            checkboxSelection
            columnGroupHeaderHeight={35}
            experimentalFeatures={{
              charts: true,
            }}
          />
        </div>
        <div style={{ marginTop: 32, marginRight: 32, display: 'flex' }}>
          <GridChartsRendererProxy
            id="quantity"
            label="Quantity"
            renderer={ChartsRenderer}
          />
          <GridChartsRendererProxy
            id="feeRate"
            label="Fee Rate"
            renderer={ChartsRenderer}
          />
        </div>
      </div>
    </GridChartsIntegrationContextProvider>
  );
}

```

## Customization

Customize the chart configuration and rendering by:

- Overriding configuration options to force certain values.
  Use it to hide or lock configuration controls in the panel.
- Using the `onRender()` prop on `<GridChartsRendererProxy />` to customize chart rendering for one or all chart types.

The demo below overrides the configuration and removes the option to change the color palette.
Additionally, it adds axes formatting for line and area chart that cannot be controlled via the default customization panel.

If needed, you can extend the configuration to render the UI elements for the additional customized axes.

```tsx
import * as React from 'react';
import {
  DataGridPremium,
  GridChartsPanel,
  GridChartsIntegrationContextProvider,
  GridChartsRendererProxy,
  GridSidebarValue,
  GridColDef,
  GridRowModel,
  GridPivotModel,
  DataGridPremiumProps,
  GridChartsPanelProps,
  useGridApiRef,
  GridEventListener,
  gridColumnGroupsUnwrappedModelSelector,
} from '@mui/x-data-grid-premium';
import {
  ChartsRenderer,
  configurationOptions,
  GridChartsConfigurationSection,
} from '@mui/x-charts-premium/ChartsRenderer';
import { downloads } from './dataset';

const columns: GridColDef[] = [
  { field: 'id', chartable: false },
  { field: 'timestamp', headerName: 'Timestamp', type: 'date' },
  { field: 'version', headerName: 'Version', width: 100 },
  { field: 'downloads', headerName: 'Downloads', type: 'number' },
];

const versions = Object.keys(
  downloads.versionDownloads,
) as (keyof typeof downloads.versionDownloads)[];

const rows: GridRowModel[] = [];
for (let i = 0; i < downloads.timestamps.length; i += 1) {
  for (let j = 0; j < versions.length; j += 1) {
    rows.push({
      id: `${i}-${j}`,
      timestamp: new Date(downloads.timestamps[i]),
      version: versions[j],
      downloads: downloads.versionDownloads[versions[j]][i],
    });
  }
}

const hideColorsControl = (sections: GridChartsConfigurationSection[]) =>
  sections.map((section) => ({
    ...section,
    controls: {
      ...section.controls,
      colors: {
        ...section.controls.colors,
        isHidden: () => true,
      },
    },
  }));

const customConfiguration = {
  bar: {
    ...configurationOptions.bar,
    customization: hideColorsControl(configurationOptions.bar.customization),
    maxDimensions: 1,
  },
  column: {
    ...configurationOptions.column,
    customization: hideColorsControl(configurationOptions.column.customization),
    maxDimensions: 1,
  },
  line: {
    ...configurationOptions.line,
    customization: hideColorsControl(configurationOptions.line.customization),
    maxDimensions: 1,
  },
  area: {
    ...configurationOptions.area,
    customization: hideColorsControl(configurationOptions.area.customization),
    maxDimensions: 1,
  },
};

const gridPivotModel: GridPivotModel = {
  rows: [{ field: 'timestamp' }],
  columns: [{ field: 'majorVersion', sort: 'asc' }],
  values: [{ field: 'downloads', aggFunc: 'sum' }],
};

const getPivotDerivedColumns: DataGridPremiumProps['getPivotDerivedColumns'] = (
  column,
) => {
  if (column.field === 'version') {
    return [
      {
        field: 'majorVersion',
        headerName: `Major version`,
        type: 'number',
        valueGetter: (_, row) => Number(row.version.split('.')[0]),
        valueFormatter: (value: string) => `v${value}`,
      },
    ];
  }
  return undefined;
};

const initialState = {
  sidebar: {
    open: true,
    value: GridSidebarValue.Charts,
  },
  pivoting: {
    enabled: true,
    model: gridPivotModel,
  },
  chartsIntegration: {
    charts: {
      main: {
        dimensions: ['timestamp'],
        values: [],
        chartType: 'line',
        configuration: {
          showMark: false,
          grid: 'both',
          height: 400,
        },
      },
    },
  },
};

const getColumnName: GridChartsPanelProps['getColumnName'] = (field) => {
  if (field === 'downloads') {
    return 'Downloads';
  }
  if (!field.endsWith('downloads')) {
    return undefined;
  }
  return `v${field[0]}`;
};

const dateFormatter = (value: string | Date) =>
  new Date(value).toLocaleDateString('en-US', {
    month: '2-digit',
    year: '2-digit',
  });
const downloadsFormatter = (value: number) =>
  value === 0 ? '0' : `${Math.round(value / 1000)}k`;

const onRender = (
  type: string,
  props: Record<string, any>,
  Component: React.ComponentType<any>,
) => {
  let adjustedProps = props;

  if (type === 'line' || type === 'area') {
    adjustedProps = {
      ...adjustedProps,
      xAxis: props.xAxis.map((axis: any) => ({
        ...axis,
        scaleType: 'time',
        domainLimit: 'strict',
        valueFormatter: dateFormatter,
      })),
      yAxis: props.yAxis.map((axis: any) => ({
        ...axis,
        valueFormatter: downloadsFormatter,
      })),
    };
  }

  if (type === 'bar') {
    adjustedProps = {
      ...adjustedProps,
      xAxis: [
        {
          valueFormatter: downloadsFormatter,
        },
      ],
      yAxis: adjustedProps.yAxis.map((axis: any) => ({
        ...axis,
        valueFormatter: dateFormatter,
        tickInterval: (_: any, index: number) => index % 10 === 0,
      })),
    };
  }

  if (type === 'column') {
    adjustedProps = {
      ...adjustedProps,
      xAxis: adjustedProps.xAxis.map((axis: any) => ({
        ...axis,
        valueFormatter: dateFormatter,
      })),
      yAxis: [
        {
          valueFormatter: downloadsFormatter,
        },
      ],
    };
  }

  return <Component {...adjustedProps} />;
};

export default function GridChartsIntegrationCustomization() {
  const apiRef = useGridApiRef();

  React.useEffect(() => {
    const handleColumnsChange: GridEventListener<'columnsChange'> = () => {
      const unwrappedGroupingModel = Object.keys(
        gridColumnGroupsUnwrappedModelSelector(apiRef),
      );
      if (unwrappedGroupingModel.length === 0) {
        return;
      }

      // pick up the all major versions
      apiRef.current?.updateChartValuesData(
        'main',
        unwrappedGroupingModel.map((field) => ({ field })),
      );

      if (unsubscribe) {
        unsubscribe();
      }
    };

    const unsubscribe = apiRef.current?.subscribeEvent(
      'columnsChange',
      handleColumnsChange,
    );
  }, [apiRef]);

  return (
    <GridChartsIntegrationContextProvider>
      <div style={{ gap: 32, width: '100%' }}>
        <div style={{ height: 575, paddingBottom: 16 }}>
          <DataGridPremium
            apiRef={apiRef}
            columns={columns}
            rows={rows}
            showToolbar
            label="Data Grid downloads"
            chartsIntegration
            slots={{
              chartsPanel: GridChartsPanel,
            }}
            slotProps={{
              chartsPanel: {
                schema: customConfiguration,
                getColumnName,
              },
            }}
            getPivotDerivedColumns={getPivotDerivedColumns}
            initialState={initialState}
            experimentalFeatures={{
              charts: true,
            }}
          />
        </div>
        <GridChartsRendererProxy
          id="main"
          renderer={ChartsRenderer}
          onRender={onRender}
        />
      </div>
    </GridChartsIntegrationContextProvider>
  );
}

```

## Live data

The demo below shows how the Charts react to live data updates in the Grid.

```tsx
import * as React from 'react';
import { interval } from 'rxjs';
import {
  DataGridPremium,
  GridChartsPanel,
  GridChartsIntegrationContextProvider,
  GridChartsRendererProxy,
  GridColDef,
  useGridApiRef,
} from '@mui/x-data-grid-premium';
import { randomInt } from '@mui/x-data-grid-generator';
import {
  ChartsRenderer,
  configurationOptions,
} from '@mui/x-charts-premium/ChartsRenderer';
import { BarChartPro, BarChartProProps } from '@mui/x-charts-pro/BarChartPro';
import { AxisConfig } from '@mui/x-charts/models';

const columns: GridColDef[] = [
  { field: 'id' },
  { field: 'process', headerName: 'Process', width: 150 },
  {
    field: 'cpu',
    headerName: 'CPU',
    width: 100,
    type: 'number',
    valueFormatter: (value) => `${value}%`,
  },
  {
    field: 'memory',
    headerName: 'Memory',
    width: 100,
    type: 'number',
    valueFormatter: (value) => `${value} MB`,
  },
];

const processDefinitions = [
  { name: 'chrome', minCpu: 20, maxCpu: 80, minMemory: 950, maxMemory: 1000 },
  { name: 'finder', minCpu: 0, maxCpu: 5, minMemory: 250, maxMemory: 300 },
  { name: 'mail', minCpu: 0, maxCpu: 5, minMemory: 375, maxMemory: 400 },
  { name: 'terminal', minCpu: 3, maxCpu: 10, minMemory: 120, maxMemory: 160 },
  { name: 'adobe', minCpu: 50, maxCpu: 90, minMemory: 3700, maxMemory: 3900 },
  { name: 'firefox', minCpu: 3, maxCpu: 20, minMemory: 670, maxMemory: 700 },
  { name: 'slack', minCpu: 1, maxCpu: 10, minMemory: 480, maxMemory: 500 },
  { name: 'chrome', minCpu: 3, maxCpu: 30, minMemory: 770, maxMemory: 790 },
  { name: 'spotify', minCpu: 1, maxCpu: 10, minMemory: 220, maxMemory: 250 },
  { name: 'chrome', minCpu: 12, maxCpu: 25, minMemory: 350, maxMemory: 400 },
  { name: 'chrome', minCpu: 20, maxCpu: 30, minMemory: 550, maxMemory: 600 },
];

const customConfigurationOptions = Object.fromEntries(
  Object.entries(configurationOptions).filter(([key]) => key === 'column'),
);

export default function GridChartsIntegrationLiveData() {
  const apiRef = useGridApiRef();

  React.useEffect(() => {
    const subscription = interval(1000).subscribe(() => {
      apiRef.current?.updateRows(generateRows());
    });

    return () => {
      subscription.unsubscribe();
    };
  }, [apiRef]);

  return (
    <GridChartsIntegrationContextProvider>
      <div style={{ gap: 32, width: '100%' }}>
        <div style={{ height: 420, paddingBottom: 16 }}>
          <DataGridPremium
            apiRef={apiRef}
            columns={columns}
            rows={generateRows()}
            showToolbar
            chartsIntegration
            slots={{
              chartsPanel: GridChartsPanel,
            }}
            slotProps={{
              chartsPanel: {
                schema: customConfigurationOptions,
              },
            }}
            initialState={{
              columns: {
                columnVisibilityModel: {
                  id: false,
                },
              },
              chartsIntegration: {
                charts: {
                  left: {
                    dimensions: ['process'],
                    values: ['cpu'],
                    chartType: 'column',
                    configuration: {
                      grid: 'horizontal',
                      colors: 'blueberryTwilightPalette',
                    },
                  },
                  right: {
                    dimensions: ['process'],
                    values: ['memory'],
                    chartType: 'column',
                    configuration: {
                      grid: 'horizontal',
                      colors: 'mangoFusionPalette',
                    },
                  },
                },
              },
              sorting: {
                sortModel: [{ field: 'cpu', sort: 'desc' }],
              },
            }}
            experimentalFeatures={{
              charts: true,
            }}
          />
        </div>
        <div style={{ marginTop: 32, marginRight: 32, display: 'flex' }}>
          <GridChartsRendererProxy
            id="left"
            label="CPU"
            renderer={ChartsRenderer}
            onRender={getOnRender(100, '%')}
          />
          <GridChartsRendererProxy
            id="right"
            label="Memory"
            renderer={ChartsRenderer}
            onRender={getOnRender(4096, 'MB')}
          />
        </div>
      </div>
    </GridChartsIntegrationContextProvider>
  );
}

function generateRows() {
  return processDefinitions.map((process, index) => ({
    id: index,
    process: process.name,
    cpu: randomInt(process.minCpu, process.maxCpu),
    memory: randomInt(process.minMemory, process.maxMemory),
  }));
}

function getOnRender(max: number, unit: string) {
  return function onRender(
    type: string,
    props: Record<string, any>,
    Component: React.ComponentType<any>,
  ) {
    if (type !== 'column') {
      return <Component {...props} />;
    }

    const series = props.series.map((seriesItem: AxisConfig) => ({
      ...seriesItem,
      label: `${seriesItem.label} (${unit})`,
    }));

    const yAxis = [
      {
        min: 0,
        max,
        valueFormatter: (value: number) => `${value} ${unit}`,
        width: 60,
      },
    ];

    return (
      <BarChartPro {...(props as BarChartProProps)} series={series} yAxis={yAxis} />
    );
  };
}

```

## Localization

To localize all components included in the Charts integration, choose one method for both the [Grid](/x/react-data-grid/localization/) and [Charts](/x/react-charts/localization/).
We recommend using `createTheme()` and `ThemeProvider`.

To get localized configuration options, use `getLocalizedConfigurationOptions()` instead of `configurationOptions`.

The demo below shows how to incorporate localization into the integration using the `frFr` locale.

```tsx
import * as React from 'react';
import { createTheme, useTheme, ThemeProvider } from '@mui/material/styles';
import { useDemoData } from '@mui/x-data-grid-generator';
import {
  DataGridPremium,
  GridChartsPanel,
  GridChartsIntegrationContextProvider,
  GridChartsRendererProxy,
  gridColumnGroupsUnwrappedModelSelector,
  GridEventListener,
  GridPivotModel,
  useGridApiRef,
  GridSidebarValue,
} from '@mui/x-data-grid-premium';
import { frFR as frFRGrid } from '@mui/x-data-grid-premium/locales';
import {
  ChartsRenderer,
  getLocalizedConfigurationOptions,
} from '@mui/x-charts-premium/ChartsRenderer';
import { frFR as frFRCharts, frFRLocalText } from '@mui/x-charts-premium/locales';

const configurationOptions = getLocalizedConfigurationOptions(frFRLocalText); // localized chart configuration options

const frColumnHeaderNames = {
  commodity: 'Matière première',
  maturityDate: 'Date de maturité',
  quantity: 'Quantité',
  feeRate: 'Taux de frais',
};

export default function GridChartsIntegrationLocalization() {
  const { data } = useDemoData({
    dataSet: 'Commodity',
    rowLength: 1000,
    editable: true,
  });
  const apiRef = useGridApiRef();

  // Inherit the theme from the docs site (dark/light mode)
  const existingTheme = useTheme();
  const theme = React.useMemo(
    () => createTheme(frFRGrid, frFRCharts, existingTheme),
    [existingTheme],
  );

  const columns = React.useMemo(
    () =>
      data.columns.map((column) =>
        frColumnHeaderNames[column.field as keyof typeof frColumnHeaderNames]
          ? {
              ...column,
              headerName:
                frColumnHeaderNames[
                  column.field as keyof typeof frColumnHeaderNames
                ],
            }
          : column,
      ),
    [data.columns],
  );

  const pivotModel: GridPivotModel = {
    rows: [{ field: 'commodity' }],
    columns: [
      { field: 'maturityDate-year', sort: 'asc' },
      { field: 'maturityDate-quarter', sort: 'asc' },
    ],
    values: [
      { field: 'quantity', aggFunc: 'sum' },
      { field: 'feeRate', aggFunc: 'avg' },
    ],
  };

  const initialState = {
    ...data.initialState,
    pivoting: {
      model: pivotModel,
      enabled: true,
    },
    sidebar: {
      open: true,
      value: GridSidebarValue.Charts,
    },
    chartsIntegration: {
      charts: {
        main: {
          dimensions: ['commodity'],
          chartType: 'column',
        },
      },
    },
  };

  const hasInitializedPivotingSeries = React.useRef(false);
  React.useEffect(() => {
    const handleColumnVisibilityModelChange: GridEventListener<
      'columnVisibilityModelChange'
    > = () => {
      if (hasInitializedPivotingSeries.current) {
        return;
      }

      const unwrappedGroupingModel = Object.keys(
        gridColumnGroupsUnwrappedModelSelector(apiRef),
      );
      // wait until pivoting creates column grouping model
      if (unwrappedGroupingModel.length === 0) {
        return;
      }

      hasInitializedPivotingSeries.current = true;
      // pick up the first 5 dyamically created columns with quantity in the name and enable first 3
      apiRef.current?.updateChartValuesData(
        'main',
        unwrappedGroupingModel
          .filter((field) => field.endsWith('quantity'))
          .slice(0, 5)
          .map((field, index) => ({ field, hidden: index >= 3 })),
      );
    };

    return apiRef.current?.subscribeEvent(
      'columnVisibilityModelChange',
      handleColumnVisibilityModelChange,
    );
  }, [apiRef]);

  return (
    <GridChartsIntegrationContextProvider>
      <ThemeProvider theme={theme}>
        <div style={{ gap: 32, width: '100%' }}>
          <div style={{ height: 575, paddingBottom: 16 }}>
            <DataGridPremium
              {...data}
              apiRef={apiRef}
              columns={columns}
              showToolbar
              chartsIntegration
              slots={{
                chartsPanel: GridChartsPanel,
              }}
              slotProps={{
                chartsPanel: {
                  schema: configurationOptions,
                },
              }}
              initialState={initialState}
              checkboxSelection
              columnGroupHeaderHeight={35}
              experimentalFeatures={{
                charts: true,
              }}
            />
          </div>
          <GridChartsRendererProxy id="main" renderer={ChartsRenderer} />
        </div>
      </ThemeProvider>
    </GridChartsIntegrationContextProvider>
  );
}

```

## API

- [DataGrid](/x/api/data-grid/data-grid/)
- [DataGridPro](/x/api/data-grid/data-grid-pro/)
- [DataGridPremium](/x/api/data-grid/data-grid-premium/)
