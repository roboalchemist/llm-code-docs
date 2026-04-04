# Source: https://icflorescu.github.io/mantine-datatable/examples/row-dragging/

Title: Examples › Row dragging | Mantine DataTable

URL Source: https://icflorescu.github.io/mantine-datatable/examples/row-dragging/

Markdown Content:
Examples › Row dragging | Mantine DataTable
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

Examples › Row dragging
-----------------------

Starting with `v7.11.3`, Mantine DataTable also supports row dragging (implemented with[@hello-pangea/dnd library](https://github.com/hello-pangea/dnd) in[this PR](https://github.com/icflorescu/mantine-datatable/pull/616)).

Here is how you would implement it in your project:

RowDraggingExample.tsx RowDraggingExample.module.css companies.json

```
'use client';

import { DragDropContext, Draggable, type DropResult, Droppable } from '@hello-pangea/dnd';
import { Center, TableTd } from '@mantine/core';
import { notifications } from '@mantine/notifications';
import { IconGripVertical } from '@tabler/icons-react';
import type { DataTableColumn } from 'mantine-datatable';
import { DataTable, DataTableDraggableRow } from 'mantine-datatable';
import clsx from 'clsx';
import { useState } from 'react';
import companies from '~/data/companies.json';
import classes from './RowDraggingExample.module.css';

interface RecordData {
  id: string;
  name: string;
  streetAddress: string;
  city: string;
  state: string;
  missionStatement: string;
}

export function RowDraggingExample() {
  const [records, setRecords] = useState<RecordData[]>(companies);

  const handleDragEnd = (result: DropResult) => {
    if (!result.destination) return;

    const items = Array.from(records);
    const sourceIndex = result.source.index;
    const destinationIndex = result.destination.index;
    const [reorderedItem] = items.splice(sourceIndex, 1);
    items.splice(destinationIndex, 0, reorderedItem);

    setRecords(items);
    notifications.show({
      title: 'Table reordered',
      message: `The company named "${items[sourceIndex].name}" has been moved from position ${sourceIndex + 1} to ${destinationIndex + 1}.`,
      color: 'blue',
    });
  };

  const columns: DataTableColumn<RecordData>[] = [
    // add empty header column for the drag handle
    { accessor: '', hiddenContent: true, width: 30 },
    { accessor: 'name', width: 150 },
    { accessor: 'streetAddress', width: 150 },
    { accessor: 'city', width: 150 },
    { accessor: 'state', width: 150 },
  ];

  return (
    <DragDropContext onDragEnd={handleDragEnd}>
      <DataTable<RecordData>
        columns={columns}
        records={records}
        height={400}
        withTableBorder
        withColumnBorders
        tableWrapper={({ children }) => (
          <Droppable droppableId="datatable">
            {(provided) => (
              <div {...provided.droppableProps} ref={provided.innerRef}>
                {children}
                {provided.placeholder}
              </div>
            )}
          </Droppable>
        )}
        styles={{ table: { tableLayout: 'fixed' } }}
        rowFactory={({ record, index, rowProps, children }) => (
          <Draggable key={record.id} draggableId={record.id} index={index}>
            {(provided, snapshot) => (
              <DataTableDraggableRow
                isDragging={snapshot.isDragging}
                {...rowProps}
                // 👇 custom class name for styling
                className={clsx(rowProps.className, classes.draggableRow)}
                {...provided.draggableProps}
              >
                <TableTd>
                  {/** 👇 custom drag handle */}
                  <Center {...provided.dragHandleProps} ref={provided.innerRef}>
                    <IconGripVertical size={16} />
                  </Center>
                </TableTd>
                {children}
              </DataTableDraggableRow>
            )}
          </Draggable>
        )}
      />
    </DragDropContext>
  );
}
```

Expand code

The code above will produce the following result:

|  | Name | Street address | City | State |
| --- | --- | --- | --- | --- |
|  | Feest, Bogan and Herzog | 21716 Ratke Drive | Stromanport | WY |
|  | Cummerata - Kuhlman | 6389 Dicki Stream | South Gate | NH |
|  | Goyette Inc | 8873 Mertz Rapid | Dorthyside | ID |
|  | Runte Inc | 2996 Ronny Mount | McAllen | MA |
|  | Goldner, Rohan and Lehner | 632 Broadway Avenue | North Louie | WY |
|  | Doyle, Hodkiewicz and O'Connell | 576 Joyce Ways | Tyraburgh | KS |
|  | Rau - O'Hara | 7508 Lansdowne Road | Shieldsborough | MI |
|  | Tillman - Jacobi | 57918 Gwendolyn Circles | Sheridanport | MI |
|  | Connelly, Feest and Hodkiewicz | 7057 Stanley Road | Kearaburgh | CA |
|  | Shanahan, Robel and Beier | 378 Berta Crescent | West Gerry | KS |
|  | Kling - McLaughlin | 8346 Kertzmann Square | South Joesph | ID |
|  | Jogi - McLaughlin | 83462 Shazam Street | North Joesph | ID |
|  | Jogi - McLaughlin | 83462 Shazam Street | North Joesph | ID |

No records

[Go back Examples › Column dragging and toggling](https://icflorescu.github.io/mantine-datatable/examples/column-dragging-and-toggling/)[Up next Examples › Column resizing](https://icflorescu.github.io/mantine-datatable/examples/column-resizing/)

Mantine DataTable is used and trusted by
----------------------------------------

[![Image 1: Microsoft is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/microsoft.svg)](https://www.microsoft.com/ "Microsoft is using Mantine DataTable")[![Image 2: Namecheap is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/namecheap-light.svg)![Image 3: Namecheap is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/namecheap-dark.svg)](https://www.namecheap.com/ "Namecheap is using Mantine DataTable")[![Image 4: EasyWP is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/easywp-light.svg)![Image 5: EasyWP is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/easywp-dark.svg)](https://www.easywp.com/ "EasyWP is using Mantine DataTable")[![Image 6: LeasingSH.ro is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/leasingsh-ro-light.png)![Image 7: LeasingSH.ro is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/leasingsh-ro-dark.png)](https://leasingsh.ro/ "LeasingSH.ro is using Mantine DataTable")[![Image 8: CodeParrot.AI is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/codeparrot.svg) CodeParrot.AI](https://codeparrot.ai/ "CodeParrot.AI is using Mantine DataTable")[![Image 9: OmicsStudio is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/omicsstudio-light.svg)![Image 10: OmicsStudio is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/omicsstudio-dark.svg)](https://omicsstudio.com/ "OmicsStudio is using Mantine DataTable")[![Image 11: SegmentX is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/segmentx.png) SegmentX](https://segmentx.ai/ "SegmentX is using Mantine DataTable")[![Image 12: Aquarino is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/aquarino.svg)](http://aquarino.com.br/ "Aquarino is using Mantine DataTable")[![Image 13: Dera is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/dera.webp) Dera](https://getdera.com/ "Dera is using Mantine DataTable")[![Image 14: kappa.ai is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/kapa-light.png)![Image 15: kappa.ai is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/kapa-dark.png)](https://kapa.ai/ "kappa.ai is using Mantine DataTable")[![Image 16: exdatis is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/exdatis-light.svg)![Image 17: exdatis is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/exdatis-dark.svg)](https://exdatis.ai/ "exdatis is using Mantine DataTable")[![Image 18: teachfloor is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/teachfloor-light.svg)![Image 19: teachfloor is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/teachfloor-dark.svg)](https://www.teachfloor.com/ "teachfloor is using Mantine DataTable")[![Image 20: MARKUP is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/markup-light.png)![Image 21: MARKUP is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/markup-dark.png)](https://www.getmarkup.com/ "MARKUP is using Mantine DataTable")[![Image 22: InvenTree is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/inventree-light.png)![Image 23: InvenTree is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/inventree-dark.png)](https://inventree.org/ "InvenTree is using Mantine DataTable")[![Image 24: BookieBase is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/bookiebase-light.svg)![Image 25: BookieBase is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/bookiebase-dark.svg)](https://bookiebase.ie/ "BookieBase is using Mantine DataTable")[![Image 26: Zipline is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/zipline.png)](https://zipline.diced.sh/ "Zipline is using Mantine DataTable")[![Image 27: Pachtop is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/pachtop.png) Pachtop](https://pachtop.com/ "Pachtop is using Mantine DataTable")[![Image 28: Ganymede is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/ganymede.png) Ganymede](https://github.com/Zibbp/ganymede "Ganymede is using Mantine DataTable")[![Image 29: Pipedash is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/pipedash.png) Pipedash](https://github.com/hcavarsan/pipedash "Pipedash is using Mantine DataTable")[![Image 30: COH3 Stats is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/coh3-stats.png) COH3 Stats](https://coh3stats.com/ "COH3 Stats is using Mantine DataTable")[![Image 31: ccrentals.org is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/ccrentals-light.svg)![Image 32: ccrentals.org is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/ccrentals-dark.svg) ccrentals.org](https://www.ccrentals.org/ "ccrentals.org is using Mantine DataTable")

[![Image 33: MIT License](https://img.shields.io/npm/l/mantine-datatable.svg?style=flat&color=1c7ed6)](https://github.com/icflorescu/mantine-datatable/blob/main/LICENSE)[![Image 34: Sponsor the author](https://img.shields.io/static/v1?label=github&message=sponsor&color=1c7ed6)](https://github.com/sponsors/icflorescu)

Built by [Ionut-Cristian Florescu](https://github.com/icflorescu) and[these awesome people](https://github.com/icflorescu/mantine-datatable/graphs/contributors).

Please [sponsor my work](https://github.com/sponsors/icflorescu) if you find it useful.

[![Image 35: GitHub Stars](https://img.shields.io/github/stars/icflorescu/mantine-datatable?style=flat&color=1c7ed6)](https://github.com/icflorescu/mantine-datatable)[![Image 36: NPM Downloads](https://img.shields.io/npm/dm/mantine-datatable.svg?style=flat&color=1c7ed6)](https://www.npmjs.com/package/mantine-datatable)

 Press space bar to start a drag. When dragging you can use the arrow keys to move the item around and escape to cancel. Some screen readers may require you to be in focus mode or to use your pass through key
