# Source: https://icflorescu.github.io/mantine-datatable/examples/column-dragging-and-toggling/

Title: Examples › Column dragging and toggling | Mantine DataTable

URL Source: https://icflorescu.github.io/mantine-datatable/examples/column-dragging-and-toggling/

Markdown Content:
Examples › Column dragging and toggling | Mantine DataTable
===============

[Mantine DataTable =================](https://icflorescu.github.io/mantine-datatable/)

8.3.13

Search

[Source code](https://github.com/icflorescu/mantine-datatable)[287.6k/mo nth](https://www.npmjs.com/package/mantine-datatable)[Sponsor](https://github.com/sponsors/icflorescu)

[Home](https://icflorescu.github.io/mantine-datatable/)[Getting started](https://icflorescu.github.io/mantine-datatable/getting-started/)[Styling](https://icflorescu.github.io/mantine-datatable/styling/)

Examples

[Basic usage](https://icflorescu.github.io/mantine-datatable/examples/basic-usage/)[Basic table properties](https://icflorescu.github.io/mantine-datatable/examples/basic-table-properties/)[Overriding the default styles](https://icflorescu.github.io/mantine-datatable/examples/overriding-the-default-styles/)[Column properties and styling](https://icflorescu.github.io/mantine-datatable/examples/column-properties-and-styling/)[Column grouping](https://icflorescu.github.io/mantine-datatable/examples/column-grouping/)[Default column properties](https://icflorescu.github.io/mantine-datatable/examples/default-column-properties/)[Default column render](https://icflorescu.github.io/mantine-datatable/examples/default-column-render/)[Row styling](https://icflorescu.github.io/mantine-datatable/examples/row-styling/)[Non-standard record IDs](https://icflorescu.github.io/mantine-datatable/examples/non-standard-record-ids/)[Scrollable vs. auto-height](https://icflorescu.github.io/mantine-datatable/examples/scrollable-vs-auto-height/)[Scrolling a row into view](https://icflorescu.github.io/mantine-datatable/examples/scrolling-a-row-into-view/)[Empty state](https://icflorescu.github.io/mantine-datatable/examples/empty-state/)[Pagination](https://icflorescu.github.io/mantine-datatable/examples/pagination/)[Sorting](https://icflorescu.github.io/mantine-datatable/examples/sorting/)[Column dragging and toggling](https://icflorescu.github.io/mantine-datatable/examples/column-dragging-and-toggling/)[Row dragging](https://icflorescu.github.io/mantine-datatable/examples/row-dragging/)[Column resizing](https://icflorescu.github.io/mantine-datatable/examples/column-resizing/)[Infinite scrolling](https://icflorescu.github.io/mantine-datatable/examples/infinite-scrolling/)[Searching and filtering](https://icflorescu.github.io/mantine-datatable/examples/searching-and-filtering/)[Records selection](https://icflorescu.github.io/mantine-datatable/examples/records-selection/)[Handling row clicks](https://icflorescu.github.io/mantine-datatable/examples/handling-row-clicks/)[Handling cell clicks](https://icflorescu.github.io/mantine-datatable/examples/handling-cell-clicks/)[Using with Mantine ContextMenu](https://icflorescu.github.io/mantine-datatable/examples/using-with-mantine-contextmenu/)[Expanding rows](https://icflorescu.github.io/mantine-datatable/examples/expanding-rows/)[Nested tables](https://icflorescu.github.io/mantine-datatable/examples/nested-tables/)[Nested tables with async data loading](https://icflorescu.github.io/mantine-datatable/examples/nested-tables-with-async-data-loading/)[Nested tables with async data loading and sorting](https://icflorescu.github.io/mantine-datatable/examples/nested-tables-with-async-data-loading-and-sorting/)[Row actions cell](https://icflorescu.github.io/mantine-datatable/examples/row-actions-cell/)[Pinning the last column](https://icflorescu.github.io/mantine-datatable/examples/pinning-the-last-column/)[Pinning the first column](https://icflorescu.github.io/mantine-datatable/examples/pinning-the-first-column/)[RTL support](https://icflorescu.github.io/mantine-datatable/examples/rtl-support/)[Links or buttons inside clickable rows or cells](https://icflorescu.github.io/mantine-datatable/examples/links-or-buttons-inside-clickable-rows-or-cells/)[Disabling text selection](https://icflorescu.github.io/mantine-datatable/examples/disabling-text-selection/)[Asynchronous data loading](https://icflorescu.github.io/mantine-datatable/examples/asynchronous-data-loading/)[Custom row or cell attributes](https://icflorescu.github.io/mantine-datatable/examples/custom-row-or-cell-attributes/)[Using bodyRef with AutoAnimate](https://icflorescu.github.io/mantine-datatable/examples/using-with-auto-animate/)[Complex usage scenario](https://icflorescu.github.io/mantine-datatable/examples/complex-usage-scenario/)

[Type definitions](https://icflorescu.github.io/mantine-datatable/type-definitions/)[Mantine V6 support](https://icflorescu.github.io/mantine-datatable/mantine-v6-support/)[Contribute and support](https://icflorescu.github.io/mantine-datatable/contribute-and-support/)[Hire the author](https://icflorescu.github.io/mantine-datatable/hire-the-author/)[Changelog](https://github.com/icflorescu/mantine-datatable/blob/main/CHANGELOG.md)

[View source code](https://github.com/icflorescu/mantine-datatable)[Go to the npm package (287.6k/mo)](https://www.npmjs.com/package/mantine-datatable)[Sponsor the author](https://github.com/sponsors/icflorescu)

Examples › Column dragging and toggling
---------------------------------------

Starting with `v7.3`, Mantine DataTable supports column toggling and drag-and-drop reordering, thanks to the [outstanding work](https://github.com/icflorescu/mantine-datatable/pull/483) of[Giovambattista Fazioli](https://github.com/gfazioli).

### [Column drag-and-drop reordering](https://icflorescu.github.io/mantine-datatable/examples/column-dragging-and-toggling/)

| Name | Street address | City | State |
| --- | --- | --- | --- |
| Feest, Bogan and Herzog | 21716 Ratke Drive | Stromanport | WY |
| Cummerata - Kuhlman | 6389 Dicki Stream | South Gate | NH |
| Goyette Inc | 8873 Mertz Rapid | Dorthyside | ID |
| Runte Inc | 2996 Ronny Mount | McAllen | MA |
| Goldner, Rohan and Lehner | 632 Broadway Avenue | North Louie | WY |
| Doyle, Hodkiewicz and O'Connell | 576 Joyce Ways | Tyraburgh | KS |
| Rau - O'Hara | 7508 Lansdowne Road | Shieldsborough | MI |
| Tillman - Jacobi | 57918 Gwendolyn Circles | Sheridanport | MI |
| Connelly, Feest and Hodkiewicz | 7057 Stanley Road | Kearaburgh | CA |
| Shanahan, Robel and Beier | 378 Berta Crescent | West Gerry | KS |
| Kling - McLaughlin | 8346 Kertzmann Square | South Joesph | ID |
| Jogi - McLaughlin | 83462 Shazam Street | North Joesph | ID |
| Jogi - McLaughlin | 83462 Shazam Street | North Joesph | ID |

No records

Reset Column Order

In order to enable **column dragging** you’ll have to:

*   add a `storeColumnsKey: 'your_key'` property to the DataTable (since the order of the columns is persisted in the local storage);
*   add a `draggable: true` property to each **dragging candidate** column;
*   use the `useDataTableColumns()` hook to get the sorted columns.

```
'use client';

import { Button, Group, Stack } from '@mantine/core';
import { DataTable, useDataTableColumns } from 'mantine-datatable';
import { companies, type Company } from '~/data';

export default function DraggingExample() {
  const key = 'draggable-example';

  const { effectiveColumns, resetColumnsOrder } = useDataTableColumns<Company>({
    key,
    columns: [
      { accessor: 'name', width: '40%', draggable: true },
      { accessor: 'streetAddress', width: '60%', draggable: true },
      { accessor: 'city', width: 160, draggable: true },
      { accessor: 'state', textAlign: 'right' },
    ],
  });

  return (
    <Stack>
      <DataTable
        withTableBorder
        withColumnBorders
        storeColumnsKey={key}
        records={companies}
        columns={effectiveColumns}
      />
      <Group justify="right">
        <Button onClick={resetColumnsOrder}>Reset Column Order</Button>
      </Group>
    </Stack>
  );
}
```

Expand code

The default order of the columns is the order in which they are defined in the `columns` prop.

### [Column toggling](https://icflorescu.github.io/mantine-datatable/examples/column-dragging-and-toggling/)

In the example below:

*   you can toggle the first 3 columns;
*   the last column is not toggleable and will always be visible;
*   the first column is toggled off by default.

Right-click on the header to select the columns you want to toggle.

| Street Address | City |  |
| --- | --- | --- |
| 21716 Ratke Drive | Stromanport | WY |
| 6389 Dicki Stream | South Gate | NH |
| 8873 Mertz Rapid | Dorthyside | ID |
| 2996 Ronny Mount | McAllen | MA |
| 632 Broadway Avenue | North Louie | WY |
| 576 Joyce Ways | Tyraburgh | KS |
| 7508 Lansdowne Road | Shieldsborough | MI |
| 57918 Gwendolyn Circles | Sheridanport | MI |
| 7057 Stanley Road | Kearaburgh | CA |
| 378 Berta Crescent | West Gerry | KS |
| 8346 Kertzmann Square | South Joesph | ID |
| 83462 Shazam Street | North Joesph | ID |
| 83462 Shazam Street | North Joesph | ID |

No records

Reset toggled columns

In order to enable **column toggling** you’ll have to:

*   add a `storeColumnsKey: 'your_key'` property to the DataTable (since the order of the columns is persisted in the local storage);
*   add a `toggleable: true` property to each **toggling candidate** column;
*   use the `useDataTableColumns()` hook to get the sorted columns.

```
'use client';

import { Button, Group, Stack, Text } from '@mantine/core';
import { IconBuildingCommunity, IconBuildingSkyscraper, IconMap, IconRoadSign } from '@tabler/icons-react';
import { DataTable, useDataTableColumns } from 'mantine-datatable';
import { companies } from '~/data';

export default function TogglingExample() {
  const key = 'toggleable-example';

  const { effectiveColumns, resetColumnsToggle } = useDataTableColumns({
    key,
    columns: [
      {
        accessor: 'name',
        title: (
          <Group gap={4} mt={-1}>
            <IconBuildingSkyscraper size={16} />
            <Text inherit mt={1}>
              Company
            </Text>
          </Group>
        ),
        width: '40%',
        toggleable: true,
        defaultToggle: false,
      },
      {
        accessor: 'streetAddress',
        title: (
          <Group gap={4} mt={-1}>
            <IconRoadSign size={16} />
            <Text inherit mt={1}>
              Street Address
            </Text>
          </Group>
        ),
        width: '60%',
        toggleable: true,
      },
      {
        accessor: 'city',
        title: (
          <Group gap={4} mt={-1}>
            <IconBuildingCommunity size={16} />
            <Text inherit mt={1}>
              City
            </Text>
          </Group>
        ),
        width: 160,
        toggleable: true,
      },
      {
        accessor: 'state',
        textAlign: 'right',
        title: (
          <Group justify="right">
            <IconMap size={16} />
          </Group>
        ),
      },
    ],
  });

  return (
    <Stack>
      <DataTable
        withTableBorder
        withColumnBorders
        storeColumnsKey={key}
        records={companies}
        columns={effectiveColumns}
      />
      <Group justify="right">
        <Button onClick={resetColumnsToggle}>Reset toggled columns</Button>
      </Group>
    </Stack>
  );
}
```

Expand code

You may define which columns will be toggled by default by setting the `defaultToggle` property to`false`.

### [Add & Remove column at run-time](https://icflorescu.github.io/mantine-datatable/examples/column-dragging-and-toggling/)

Of course, you may need to add or remove columns at run-time. In this case, you can directly modify the array of columns without needing to perform any operations.

Toggle Mission Statement column

| Street Address | City |  |
| --- | --- | --- |
| 21716 Ratke Drive | Stromanport | WY |
| 6389 Dicki Stream | South Gate | NH |
| 8873 Mertz Rapid | Dorthyside | ID |
| 2996 Ronny Mount | McAllen | MA |
| 632 Broadway Avenue | North Louie | WY |
| 576 Joyce Ways | Tyraburgh | KS |
| 7508 Lansdowne Road | Shieldsborough | MI |
| 57918 Gwendolyn Circles | Sheridanport | MI |
| 7057 Stanley Road | Kearaburgh | CA |
| 378 Berta Crescent | West Gerry | KS |
| 8346 Kertzmann Square | South Joesph | ID |
| 83462 Shazam Street | North Joesph | ID |
| 83462 Shazam Street | North Joesph | ID |

No records

Reset toggled columns

```
'use client';

import { Button, Group, Stack, Text } from '@mantine/core';
import { IconBuildingCommunity, IconBuildingSkyscraper, IconMap, IconRoadSign } from '@tabler/icons-react';
import type { DataTableColumn } from 'mantine-datatable';
import { DataTable, useDataTableColumns } from 'mantine-datatable';
import { useState } from 'react';
import { companies } from '~/data';

export default function DynamicColumnExample() {
  const key = 'dynamic-column-example';

  const [columns, setColumns] = useState<DataTableColumn[]>([
    {
      accessor: 'name',
      title: (
        <Group gap={4} mt={-1}>
          <IconBuildingSkyscraper size={16} />
          <Text inherit mt={1}>
            Company
          </Text>
        </Group>
      ),
      width: '40%',
      toggleable: true,
      defaultToggle: false,
    },
    {
      accessor: 'streetAddress',
      title: (
        <Group gap={4} mt={-1}>
          <IconRoadSign size={16} />
          <Text inherit mt={1}>
            Street Address
          </Text>
        </Group>
      ),
      width: '60%',
      toggleable: true,
    },
    {
      accessor: 'city',
      title: (
        <Group gap={4} mt={-1}>
          <IconBuildingCommunity size={16} />
          <Text inherit mt={1}>
            City
          </Text>
        </Group>
      ),
      width: 160,
      toggleable: true,
    },
    {
      accessor: 'state',
      textAlign: 'right',
      title: (
        <Group justify="right">
          <IconMap size={16} />
        </Group>
      ),
    },
  ]);

  const { effectiveColumns, resetColumnsToggle } = useDataTableColumns({
    key,
    columns,
  });

  // add or remove the whole record with missionStatement accessor
  function toggleColumnMissionStatement() {
    const newColumns = columns.filter((col) => col.accessor !== 'missionStatement');
    if (columns.length === newColumns.length) {
      newColumns.push({
        accessor: 'missionStatement',
        title: (
          <Group gap={4} mt={-1} wrap="nowrap">
            <IconBuildingSkyscraper size={16} />
            <Text inherit mt={1}>
              Mission Statement
            </Text>
          </Group>
        ),
        width: '40%',
        toggleable: true,
        defaultToggle: true,
      });
    }
    setColumns(newColumns);
  }

  return (
    <Stack>
      <Group>
        <Button onClick={toggleColumnMissionStatement}>Toggle Mission Statement column</Button>
      </Group>
      <DataTable
        withTableBorder
        withColumnBorders
        storeColumnsKey={key}
        records={companies}
        columns={effectiveColumns}
      />
      <Group justify="right">
        <Button onClick={resetColumnsToggle}>Reset toggled columns</Button>
      </Group>
    </Stack>
  );
}
```

Expand code

### [Dragging and toggling with context menu reset](https://icflorescu.github.io/mantine-datatable/examples/column-dragging-and-toggling/)

| Name | Street address | City | State |
| --- | --- | --- | --- |
| Feest, Bogan and Herzog | 21716 Ratke Drive | Stromanport | WY |
| Cummerata - Kuhlman | 6389 Dicki Stream | South Gate | NH |
| Goyette Inc | 8873 Mertz Rapid | Dorthyside | ID |
| Runte Inc | 2996 Ronny Mount | McAllen | MA |
| Goldner, Rohan and Lehner | 632 Broadway Avenue | North Louie | WY |
| Doyle, Hodkiewicz and O'Connell | 576 Joyce Ways | Tyraburgh | KS |
| Rau - O'Hara | 7508 Lansdowne Road | Shieldsborough | MI |
| Tillman - Jacobi | 57918 Gwendolyn Circles | Sheridanport | MI |
| Connelly, Feest and Hodkiewicz | 7057 Stanley Road | Kearaburgh | CA |
| Shanahan, Robel and Beier | 378 Berta Crescent | West Gerry | KS |
| Kling - McLaughlin | 8346 Kertzmann Square | South Joesph | ID |
| Jogi - McLaughlin | 83462 Shazam Street | North Joesph | ID |
| Jogi - McLaughlin | 83462 Shazam Street | North Joesph | ID |

No records

```
'use client';

import { IconColumnRemove, IconColumns3 } from '@tabler/icons-react';
import { DataTable, useDataTableColumns } from 'mantine-datatable';
import { useContextMenu } from 'mantine-contextmenu';
import { companies } from '~/data';

export default function DraggingTogglingResetExample() {
  const { showContextMenu } = useContextMenu();

  const key = 'toggleable-reset-example';

  const { effectiveColumns, resetColumnsOrder, resetColumnsToggle } = useDataTableColumns({
    key,
    columns: [
      { accessor: 'name', width: '40%', toggleable: true, draggable: true },
      { accessor: 'streetAddress', width: '60%', toggleable: true, draggable: true },
      { accessor: 'city', width: 160, toggleable: true, draggable: true },
      { accessor: 'state', textAlign: 'right' },
    ],
  });

  return (
    <DataTable
      withTableBorder
      withColumnBorders
      storeColumnsKey={key}
      records={companies}
      columns={effectiveColumns}
      onRowContextMenu={({ event }) =>
        showContextMenu([
          {
            key: 'reset-toggled-columns',
            icon: <IconColumnRemove size={16} />,
            onClick: resetColumnsToggle,
          },
          {
            key: 'reset-columns-order',
            icon: <IconColumns3 size={16} />,
            onClick: resetColumnsOrder,
          },
        ])(event)
      }
    />
  );
}
```

Expand code

### [Complex usage](https://icflorescu.github.io/mantine-datatable/examples/column-dragging-and-toggling/)

| Name | Street address | City | State |
| --- | --- | --- | --- |
| Connelly, Feest and Hodkiewicz | 7057 Stanley Road | Kearaburgh | CA |
| Cummerata - Kuhlman | 6389 Dicki Stream | South Gate | NH |
| Doyle, Hodkiewicz and O'Connell | 576 Joyce Ways | Tyraburgh | KS |
| Feest, Bogan and Herzog | 21716 Ratke Drive | Stromanport | WY |
| Goldner, Rohan and Lehner | 632 Broadway Avenue | North Louie | WY |
| Goyette Inc | 8873 Mertz Rapid | Dorthyside | ID |
| Jogi - McLaughlin | 83462 Shazam Street | North Joesph | ID |
| Jogi - McLaughlin | 83462 Shazam Street | North Joesph | ID |
| Kling - McLaughlin | 8346 Kertzmann Square | South Joesph | ID |
| Rau - O'Hara | 7508 Lansdowne Road | Shieldsborough | MI |
| Runte Inc | 2996 Ronny Mount | McAllen | MA |
| Shanahan, Robel and Beier | 378 Berta Crescent | West Gerry | KS |
| Tillman - Jacobi | 57918 Gwendolyn Circles | Sheridanport | MI |

No records

```
'use client';

import { IconColumnRemove, IconColumns3 } from '@tabler/icons-react';
import { DataTable, useDataTableColumns, type DataTableSortStatus } from 'mantine-datatable';
import sortBy from 'lodash/sortBy';
import { useContextMenu } from 'mantine-contextmenu';
import { useEffect, useState } from 'react';
import { companies, type Company } from '~/data';

export default function DraggingTogglingComplexExample() {
  const { showContextMenu } = useContextMenu();

  const [sortStatus, setSortStatus] = useState<DataTableSortStatus<Company>>({
    columnAccessor: 'name',
    direction: 'asc',
  });

  const [records, setRecords] = useState(sortBy(companies, 'name'));

  useEffect(() => {
    const data = sortBy(companies, sortStatus.columnAccessor) as Company[];
    // eslint-disable-next-line react-hooks/set-state-in-effect
    setRecords(sortStatus.direction === 'desc' ? data.reverse() : data);
  }, [sortStatus]);

  const key = 'toggleable-reset-example';

  const { effectiveColumns, resetColumnsOrder, resetColumnsToggle } = useDataTableColumns({
    key,
    columns: [
      { accessor: 'name', width: '40%', toggleable: true, draggable: true, sortable: true },
      { accessor: 'streetAddress', width: '60%', toggleable: true, draggable: true },
      { accessor: 'city', width: 160, toggleable: true, draggable: true },
      { accessor: 'state', textAlign: 'right' },
    ],
  });

  return (
    <DataTable
      withTableBorder
      withColumnBorders
      storeColumnsKey={key}
      records={records}
      columns={effectiveColumns}
      sortStatus={sortStatus}
      onSortStatusChange={setSortStatus}
      onRowContextMenu={({ event }) =>
        showContextMenu([
          {
            key: 'reset-toggled-columns',
            icon: <IconColumnRemove size={16} />,
            onClick: resetColumnsToggle,
          },
          {
            key: 'reset-columns-order',
            icon: <IconColumns3 size={16} />,
            onClick: resetColumnsOrder,
          },
        ])(event)
      }
    />
  );
}
```

Expand code

[Go back Examples › Sorting](https://icflorescu.github.io/mantine-datatable/examples/sorting/)[Up next Examples › Row dragging](https://icflorescu.github.io/mantine-datatable/examples/row-dragging/)

Mantine DataTable is used and trusted by
----------------------------------------

[![Image 1: Microsoft is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/microsoft.svg)](https://www.microsoft.com/ "Microsoft is using Mantine DataTable")[![Image 2: Namecheap is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/namecheap-light.svg)![Image 3: Namecheap is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/namecheap-dark.svg)](https://www.namecheap.com/ "Namecheap is using Mantine DataTable")[![Image 4: EasyWP is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/easywp-light.svg)![Image 5: EasyWP is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/easywp-dark.svg)](https://www.easywp.com/ "EasyWP is using Mantine DataTable")[![Image 6: LeasingSH.ro is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/leasingsh-ro-light.png)![Image 7: LeasingSH.ro is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/leasingsh-ro-dark.png)](https://leasingsh.ro/ "LeasingSH.ro is using Mantine DataTable")[![Image 8: CodeParrot.AI is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/codeparrot.svg) CodeParrot.AI](https://codeparrot.ai/ "CodeParrot.AI is using Mantine DataTable")[![Image 9: OmicsStudio is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/omicsstudio-light.svg)![Image 10: OmicsStudio is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/omicsstudio-dark.svg)](https://omicsstudio.com/ "OmicsStudio is using Mantine DataTable")[![Image 11: SegmentX is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/segmentx.png) SegmentX](https://segmentx.ai/ "SegmentX is using Mantine DataTable")[![Image 12: Aquarino is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/aquarino.svg)](http://aquarino.com.br/ "Aquarino is using Mantine DataTable")[![Image 13: Dera is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/dera.webp) Dera](https://getdera.com/ "Dera is using Mantine DataTable")[![Image 14: kappa.ai is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/kapa-light.png)![Image 15: kappa.ai is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/kapa-dark.png)](https://kapa.ai/ "kappa.ai is using Mantine DataTable")[![Image 16: exdatis is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/exdatis-light.svg)![Image 17: exdatis is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/exdatis-dark.svg)](https://exdatis.ai/ "exdatis is using Mantine DataTable")[![Image 18: teachfloor is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/teachfloor-light.svg)![Image 19: teachfloor is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/teachfloor-dark.svg)](https://www.teachfloor.com/ "teachfloor is using Mantine DataTable")[![Image 20: MARKUP is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/markup-light.png)![Image 21: MARKUP is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/markup-dark.png)](https://www.getmarkup.com/ "MARKUP is using Mantine DataTable")[![Image 22: InvenTree is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/inventree-light.png)![Image 23: InvenTree is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/inventree-dark.png)](https://inventree.org/ "InvenTree is using Mantine DataTable")[![Image 24: BookieBase is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/bookiebase-light.svg)![Image 25: BookieBase is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/bookiebase-dark.svg)](https://bookiebase.ie/ "BookieBase is using Mantine DataTable")[![Image 26: Zipline is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/zipline.png)](https://zipline.diced.sh/ "Zipline is using Mantine DataTable")[![Image 27: Pachtop is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/pachtop.png) Pachtop](https://pachtop.com/ "Pachtop is using Mantine DataTable")[![Image 28: Ganymede is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/ganymede.png) Ganymede](https://github.com/Zibbp/ganymede "Ganymede is using Mantine DataTable")[![Image 29: Pipedash is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/pipedash.png) Pipedash](https://github.com/hcavarsan/pipedash "Pipedash is using Mantine DataTable")[![Image 30: COH3 Stats is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/coh3-stats.png) COH3 Stats](https://coh3stats.com/ "COH3 Stats is using Mantine DataTable")[![Image 31: ccrentals.org is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/ccrentals-light.svg)![Image 32: ccrentals.org is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/ccrentals-dark.svg) ccrentals.org](https://www.ccrentals.org/ "ccrentals.org is using Mantine DataTable")

[![Image 33: MIT License](https://img.shields.io/npm/l/mantine-datatable.svg?style=flat&color=1c7ed6)](https://github.com/icflorescu/mantine-datatable/blob/main/LICENSE)[![Image 34: Sponsor the author](https://img.shields.io/static/v1?label=github&message=sponsor&color=1c7ed6)](https://github.com/sponsors/icflorescu)

Built by [Ionut-Cristian Florescu](https://github.com/icflorescu) and[these awesome people](https://github.com/icflorescu/mantine-datatable/graphs/contributors).

Please [sponsor my work](https://github.com/sponsors/icflorescu) if you find it useful.

[![Image 35: GitHub Stars](https://img.shields.io/github/stars/icflorescu/mantine-datatable?style=flat&color=1c7ed6)](https://github.com/icflorescu/mantine-datatable)[![Image 36: NPM Downloads](https://img.shields.io/npm/dm/mantine-datatable.svg?style=flat&color=1c7ed6)](https://www.npmjs.com/package/mantine-datatable)
