# Source: https://icflorescu.github.io/mantine-datatable/examples/column-properties-and-styling/

Title: Examples › Column properties and styling | Mantine DataTable

URL Source: https://icflorescu.github.io/mantine-datatable/examples/column-properties-and-styling/

Markdown Content:
Examples › Column properties and styling | Mantine DataTable
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

Examples › Column properties and styling
----------------------------------------

### [The accessor](https://icflorescu.github.io/mantine-datatable/examples/column-properties-and-styling/)

The only property you **have** to specify for a column is its `accessor` (the name of the record property you want to display in each column cell).

The `accessor` supports dot-notation for nested objects property drilling (i.e. `'department.company.name'`).

The component will try to derive a column header title by “humanizing” the provided accessor (i.e. `'firstName'` → `'First name'` or `'department.company.name'` → `'Department company name'`).

If you’re not happy with the automatically derived title, you can override it by setting your own column `title`.

### [Basic column properties](https://icflorescu.github.io/mantine-datatable/examples/column-properties-and-styling/)

In addition, each column can be customized by specifying the following properties:

*   `width: number | string`

Desired column width.
*   `ellipsis: boolean`

If true, cell content in this column will not wrap to multiple lines and will be truncated with ellipsis if/as needed.

You can either set this property to `true` or set `noWrap` to `true`, but not both.
*   `noWrap: boolean`

If true, cell content in this column will not wrap on multiple lines (i.e. `white-space: nowrap`).

You can either set this property to `true` or set `ellipsis` to `true`, but not both.
*   `textAlign: 'left' | 'center' | 'right'`

Defaults to `'left'` if not specified.
*   `hidden: boolean`

If true, the column will not be visible.
*   `visibleMediaQuery`

A media query `string` or a function accepting the current `MantineTheme` as its argument and returning a media-query string.

If set, the column will only be visible according to the specified media query.
*   `render`

A method that accepts the current record as its argument and returns a `ReactNode` (keep in mind that strings and numbers are valid react nodes).
*   `filter`

An optional property which provides the user with filtering options. It can be either a `ReactNode` or a function returning a `ReactNode`.

If a `ReactNode` is provided, a filter button will be added to the column header. Upon clicking the button, a popover showing the provided node will be opened.

Alternatively, you can provide a function returning a `ReactNode`. The function will be called with an object containing a `close()` method, which you can call to close the popover.
*   `filtering: boolean`

If true, the column will be styled as an active filtering column. Defaults to `false` if not specified.

See the [searching and filtering](https://icflorescu.github.io/mantine-datatable/examples/searching-and-filtering/) example to learn how to use the `filter` and `filtering` properties.

You can create a _“virtual column”_ by providing an accessor that doesn’t to refer an existing property (or nested property) name. In this case, you **must** provide a custom `render` method. Also, keep in mind that each accessor name must be unique amongst the collection of columns.

Consider this example:

| # | Full name | Email | Department name | Company | Birthday | Age |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Jerald Howell | Jerald.Howell32@yahoo.com | Industrial | Runte Inc | May 21 | 75 |
| 2 | Kathleen Ruecker | Kathleen_Ruecker@hotmail.com | Computers | Shanahan, Robel and Beier | Dec 19 | 82 |
| 3 | Erica Volkman | Erica.Volkman37@gmail.com | Toys | Goyette Inc | Jan 29 | 71 |
| 4 | Clifford Oberbrunner | Clifford.Oberbrunner@hotmail.com | Automotive | Rau - O'Hara | Mar 6 | 47 |
| 5 | Alison Kling | Alison16@gmail.com | Jewelery | Goyette Inc | Jan 27 | 29 |
| 6 | Sue Zieme | Sue.Zieme29@hotmail.com | Books | Cummerata - Kuhlman | Sep 12 | 65 |
| 7 | Felicia Gleason | Felicia30@yahoo.com | Shoes | Doyle, Hodkiewicz and O'Connell | Mar 9 | 49 |
| 8 | Alfredo Zemlak | Alfredo22@yahoo.com | Games | Runte Inc | Nov 12 | 37 |
| 9 | Emily Bartoletti | Emily.Bartoletti@gmail.com | Automotive | Rau - O'Hara | Jan 5 | 58 |
| 10 | Delores Reynolds | Delores.Reynolds@yahoo.com | Industrial | Runte Inc | Jun 4 | 21 |

No records

Here’s the code for the example above:

ColumnPropertiesExample.tsx data/index.ts

```
'use client';

import { DataTable } from 'mantine-datatable';
import dayjs from 'dayjs';
import { employees } from '~/data';

const records = employees.slice(0, 10);

export function ColumnPropertiesExample() {
  return (
    <DataTable
      withTableBorder
      withColumnBorders
      striped
      records={records}
      columns={[
        {
          accessor: 'index',
          title: '#',
          textAlign: 'right',
          width: 40,
          render: (record) => records.indexOf(record) + 1,
        },
        {
          accessor: 'name',
          title: 'Full name',
          render: ({ firstName, lastName }) => `${firstName} ${lastName}`,
          width: 160,
        },
        { accessor: 'email' },
        { accessor: 'department.name', width: 150 },
        {
          // 👇 using dot-notation to access nested object property
          accessor: 'department.company.name',
          title: 'Company',
          width: 150,
          // 👇 truncate with ellipsis if text overflows the available width
          ellipsis: true,
        },
        {
          accessor: 'birthDate',
          title: 'Birthday',
          width: 100,
          render: ({ birthDate }) => dayjs(birthDate).format('MMM D'),
          // 👇 column is only visible when screen width is over `theme.breakpoints.xs`
          visibleMediaQuery: (theme) => `(min-width: ${theme.breakpoints.xs})`,
        },
        {
          // 👇 "virtual column"
          accessor: 'age',
          width: 60,
          textAlign: 'right',
          // 👇 column is only visible when screen width is over `theme.breakpoints.xs`
          visibleMediaQuery: (theme) => `(min-width: ${theme.breakpoints.xs})`,
          render: ({ birthDate }) => dayjs().diff(birthDate, 'years'),
        },
      ]}
    />
  );
}
```

Expand code

### [Column footers](https://icflorescu.github.io/mantine-datatable/examples/column-properties-and-styling/)

The DataTable component will display a footer row at the bottom of the table if you specify a `footer` property for at least one column:

| Full name | Department name | Company | Age |
| --- | --- | --- | --- |
| Jerald Howell | Industrial | Runte Inc | 75 |
| Kathleen Ruecker | Computers | Shanahan, Robel and Beier | 82 |
| Erica Volkman | Toys | Goyette Inc | 71 |
| Clifford Oberbrunner | Automotive | Rau - O'Hara | 47 |
| Alison Kling | Jewelery | Goyette Inc | 29 |
| Sue Zieme | Books | Cummerata - Kuhlman | 65 |
| Felicia Gleason | Shoes | Doyle, Hodkiewicz and O'Connell | 49 |
| Alfredo Zemlak | Games | Runte Inc | 37 |
| Emily Bartoletti | Automotive | Rau - O'Hara | 58 |
| Delores Reynolds | Industrial | Runte Inc | 21 |
| 10 employees |  | 6 companies | Avg: 53 |

No records

Here’s the code for the example above:

ColumnFooterExample.tsx data/index.ts

```
<DataTable
  withTableBorder
  withColumnBorders
  striped
  records={records}
  height={height}
  withRowBorders
  columns={[
    {
      accessor: 'name',
      title: 'Full name',
      render: ({ firstName, lastName }) => `${firstName} ${lastName}`,
      width: 160,
      // 👇 this column has a footer
      footer: (
        <Group gap="xs">
          <Box mb={-4}>
            <IconSum size="1.25em" />
          </Box>
          <div>{records.length} employees</div>
        </Group>
      ),
    },
    // 👇 this column has NO footer
    { accessor: 'department.name', width: 150 },
    {
      accessor: 'department.company.name',
      title: 'Company',
      width: 150,
      ellipsis: true,
      // 👇 this column has a footer
      footer: (
        <Group gap="xs">
          <Box mb={-4}>
            <IconSum size={16} />
          </Box>
          <div>{uniqBy(records, (record) => record.department.company.name).length} companies</div>
        </Group>
      ),
    },
    {
      accessor: 'age',
      width: 60,
      textAlign: 'right',
      visibleMediaQuery: (theme) => `(min-width: ${theme.breakpoints.xs})`,
      render: ({ birthDate }) => dayjs().diff(birthDate, 'years'),
      // 👇 this column has a footer
      footer: `Avg: ${Math.round(
        records.map((record) => dayjs().diff(record.birthDate, 'years')).reduce((a, b) => a + b, 0) / records.length
      )}`,
    },
  ]}
/>
```

Expand code

The footer is always visible and sticks at the bottom. For example, if the table is scrollable:

| Full name | Department name | Company | Age |
| --- | --- | --- | --- |
| Jerald Howell | Industrial | Runte Inc | 75 |
| Kathleen Ruecker | Computers | Shanahan, Robel and Beier | 82 |
| Erica Volkman | Toys | Goyette Inc | 71 |
| Clifford Oberbrunner | Automotive | Rau - O'Hara | 47 |
| Alison Kling | Jewelery | Goyette Inc | 29 |
| Sue Zieme | Books | Cummerata - Kuhlman | 65 |
| Felicia Gleason | Shoes | Doyle, Hodkiewicz and O'Connell | 49 |
| Alfredo Zemlak | Games | Runte Inc | 37 |
| Emily Bartoletti | Automotive | Rau - O'Hara | 58 |
| Delores Reynolds | Industrial | Runte Inc | 21 |
| 10 employees |  | 6 companies | Avg: 53 |

No records

Or if the table is higher than the amount of data:

| Full name | Department name | Company | Age |
| --- | --- | --- | --- |
| Jerald Howell | Industrial | Runte Inc | 75 |
| Kathleen Ruecker | Computers | Shanahan, Robel and Beier | 82 |
| Erica Volkman | Toys | Goyette Inc | 71 |
| Clifford Oberbrunner | Automotive | Rau - O'Hara | 47 |
| Alison Kling | Jewelery | Goyette Inc | 29 |
| Sue Zieme | Books | Cummerata - Kuhlman | 65 |
| Felicia Gleason | Shoes | Doyle, Hodkiewicz and O'Connell | 49 |
| Alfredo Zemlak | Games | Runte Inc | 37 |
| Emily Bartoletti | Automotive | Rau - O'Hara | 58 |
| Delores Reynolds | Industrial | Runte Inc | 21 |
| 10 employees |  | 6 companies | Avg: 53 |

No records

### [Styling column titles, cells and footers](https://icflorescu.github.io/mantine-datatable/examples/column-properties-and-styling/)

In addition, each column can be further customized by specifying the following styling properties:

*   `titleClassName: string`

A custom class name for the column title.
*   `titleStyle`

A custom style object for the column title, or a function accepting the current theme and returning a style object.
*   `cellsClassName: string`

A function that accepts the current record as its argument and returns a `string` representing a custom class name for the column cells.
*   `cellsStyle`

A function that accepts the current record as its argument and returns either a style object for the column cells, or a function accepting the current theme and returning a style object.
*   `footerClassName: string`

A custom class name for the column footer.
*   `footerStyle`

A custom style object for the column footer, or a function accepting the current theme and returning a style object.

Consider this example:

| # | Full name | Email | Department name | Company | Birthday | Age |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Jerald Howell | Jerald.Howell32@yahoo.com | Industrial | Runte Inc | May 21 | 75 |
| 2 | Kathleen Ruecker | Kathleen_Ruecker@hotmail.com | Computers | Shanahan, Robel and Beier | Dec 19 | 82 |
| 3 | Erica Volkman | Erica.Volkman37@gmail.com | Toys | Goyette Inc | Jan 29 | 71 |
| 4 | Clifford Oberbrunner | Clifford.Oberbrunner@hotmail.com | Automotive | Rau - O'Hara | Mar 6 | 47 |
| 5 | Alison Kling | Alison16@gmail.com | Jewelery | Goyette Inc | Jan 27 | 29 |
| 6 | Sue Zieme | Sue.Zieme29@hotmail.com | Books | Cummerata - Kuhlman | Sep 12 | 65 |
| 7 | Felicia Gleason | Felicia30@yahoo.com | Shoes | Doyle, Hodkiewicz and O'Connell | Mar 9 | 49 |
| 8 | Alfredo Zemlak | Alfredo22@yahoo.com | Games | Runte Inc | Nov 12 | 37 |
| 9 | Emily Bartoletti | Emily.Bartoletti@gmail.com | Automotive | Rau - O'Hara | Jan 5 | 58 |
| 10 | Delores Reynolds | Delores.Reynolds@yahoo.com | Industrial | Runte Inc | Jun 4 | 21 |
|  | 10 employees |  |  | 6 companies |  | Avg: 53 |

No records

Here’s the code for the example above:

ColumnStylingExample.tsx ColumnStylingExample.module.css data/index.ts

```
'use client';

import { rgba } from '@mantine/core';
import { DataTable, uniqBy } from 'mantine-datatable';
import clsx from 'clsx';
import dayjs from 'dayjs';
import { employees } from '~/data';
import classes from './ColumnStylingExample.module.css';

const records = employees.slice(0, 10);

export function ColumnStylingExample() {
  return (
    <DataTable
      withTableBorder
      withColumnBorders
      striped
      records={records}
      columns={[
        {
          accessor: 'index',
          title: '#',
          textAlign: 'right',
          width: 40,
          // 👇 style cells with a class name
          cellsClassName: classes.idColumnCells,
          render: (record) => records.indexOf(record) + 1,
        },
        {
          accessor: 'name',
          title: 'Full name',
          width: 160,
          // 👇 style cells with a function returning a style object
          //    this function receives the current record as its argument, but we're not using it here
          cellsStyle: () => ({ fontStyle: 'italic' }),
          // 👇 style cells with a class name depending on current record
          cellsClassName: ({ sex }) => clsx({ [classes.male]: sex === 'male', [classes.female]: sex === 'female' }),
          footer: `${records.length} employees`,
          // style footer with a style object
          footerStyle: { fontStyle: 'italic' },
          render: ({ firstName, lastName }) => `${firstName} ${lastName}`,
        },
        { accessor: 'email' },
        {
          accessor: 'department.name',
          width: 150,
          // 👇 style title with a function returning a style object
          titleStyle: (theme) => ({ color: theme.colors.green[6] }),
          // 👇 style cells with a function returning a style function
          cellsStyle: () => (theme) => ({
            color: theme.colors.green[8],
            background: rgba(theme.colors.orange[6], 0.25),
          }),
        },
        {
          accessor: 'department.company.name',
          title: 'Company',
          width: 150,
          ellipsis: true,
          footer: `${uniqBy(records, (record) => record.department.company.name).length} companies`,
          // 👇 style footer with a function returning a style object
          footerStyle: (theme) => ({ color: theme.colors.blue[6] }),
        },
        {
          accessor: 'birthDate',
          title: 'Birthday',
          width: 100,
          // 👇 style title with a custom class name
          titleClassName: classes.birthdayColumnTitle,
          // 👇 style cells with a function accepting the current record and returning another
          //    function that accepts the current theme and returns a style object
          //    (i.e. people born in winter will have their birthday in blue)
          cellsStyle:
            ({ birthDate }) =>
            (theme) => ({
              color: ['Dec', 'Jan', 'Feb'].includes(dayjs(birthDate).format('MMM')) ? theme.colors.blue[6] : undefined,
            }),
          render: ({ birthDate }) => dayjs(birthDate).format('MMM D'),
        },
        {
          accessor: 'age',
          width: 80,
          textAlign: 'right',
          // 👇 style title with a style object
          titleStyle: { fontStyle: 'italic' },
          // 👇 style cells depending on current record, with a function returning a style object
          cellsStyle: ({ birthDate }) =>
            dayjs().diff(birthDate, 'years') <= 40
              ? {
                  fontWeight: 'bold',
                  color: 'green',
                  background: '#FF332222',
                }
              : undefined,
          render: ({ birthDate }) => dayjs().diff(birthDate, 'years'),
          footer: `Avg: ${Math.round(
            records.map((record) => dayjs().diff(record.birthDate, 'years')).reduce((a, b) => a + b, 0) / records.length
          )}`,
          footerClassName: classes.ageFooter,
        },
      ]}
    />
  );
}
```

Expand code

Head over to the next example to discover more features.

[Go back Examples › Overriding the default styles](https://icflorescu.github.io/mantine-datatable/examples/overriding-the-default-styles/)[Up next Examples › Column grouping](https://icflorescu.github.io/mantine-datatable/examples/column-grouping/)

Mantine DataTable is used and trusted by
----------------------------------------

[![Image 1: Microsoft is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/microsoft.svg)](https://www.microsoft.com/ "Microsoft is using Mantine DataTable")[![Image 2: Namecheap is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/namecheap-light.svg)![Image 3: Namecheap is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/namecheap-dark.svg)](https://www.namecheap.com/ "Namecheap is using Mantine DataTable")[![Image 4: EasyWP is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/easywp-light.svg)![Image 5: EasyWP is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/easywp-dark.svg)](https://www.easywp.com/ "EasyWP is using Mantine DataTable")[![Image 6: LeasingSH.ro is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/leasingsh-ro-light.png)![Image 7: LeasingSH.ro is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/leasingsh-ro-dark.png)](https://leasingsh.ro/ "LeasingSH.ro is using Mantine DataTable")[![Image 8: CodeParrot.AI is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/codeparrot.svg) CodeParrot.AI](https://codeparrot.ai/ "CodeParrot.AI is using Mantine DataTable")[![Image 9: OmicsStudio is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/omicsstudio-light.svg)![Image 10: OmicsStudio is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/omicsstudio-dark.svg)](https://omicsstudio.com/ "OmicsStudio is using Mantine DataTable")[![Image 11: SegmentX is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/segmentx.png) SegmentX](https://segmentx.ai/ "SegmentX is using Mantine DataTable")[![Image 12: Aquarino is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/aquarino.svg)](http://aquarino.com.br/ "Aquarino is using Mantine DataTable")[![Image 13: Dera is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/dera.webp) Dera](https://getdera.com/ "Dera is using Mantine DataTable")[![Image 14: kappa.ai is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/kapa-light.png)![Image 15: kappa.ai is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/kapa-dark.png)](https://kapa.ai/ "kappa.ai is using Mantine DataTable")[![Image 16: exdatis is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/exdatis-light.svg)![Image 17: exdatis is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/exdatis-dark.svg)](https://exdatis.ai/ "exdatis is using Mantine DataTable")[![Image 18: teachfloor is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/teachfloor-light.svg)![Image 19: teachfloor is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/teachfloor-dark.svg)](https://www.teachfloor.com/ "teachfloor is using Mantine DataTable")[![Image 20: MARKUP is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/markup-light.png)![Image 21: MARKUP is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/markup-dark.png)](https://www.getmarkup.com/ "MARKUP is using Mantine DataTable")[![Image 22: InvenTree is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/inventree-light.png)![Image 23: InvenTree is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/inventree-dark.png)](https://inventree.org/ "InvenTree is using Mantine DataTable")[![Image 24: BookieBase is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/bookiebase-light.svg)![Image 25: BookieBase is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/bookiebase-dark.svg)](https://bookiebase.ie/ "BookieBase is using Mantine DataTable")[![Image 26: Zipline is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/zipline.png)](https://zipline.diced.sh/ "Zipline is using Mantine DataTable")[![Image 27: Pachtop is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/pachtop.png) Pachtop](https://pachtop.com/ "Pachtop is using Mantine DataTable")[![Image 28: Ganymede is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/ganymede.png) Ganymede](https://github.com/Zibbp/ganymede "Ganymede is using Mantine DataTable")[![Image 29: Pipedash is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/pipedash.png) Pipedash](https://github.com/hcavarsan/pipedash "Pipedash is using Mantine DataTable")[![Image 30: COH3 Stats is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/coh3-stats.png) COH3 Stats](https://coh3stats.com/ "COH3 Stats is using Mantine DataTable")[![Image 31: ccrentals.org is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/ccrentals-light.svg)![Image 32: ccrentals.org is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/ccrentals-dark.svg) ccrentals.org](https://www.ccrentals.org/ "ccrentals.org is using Mantine DataTable")

[![Image 33: MIT License](https://img.shields.io/npm/l/mantine-datatable.svg?style=flat&color=1c7ed6)](https://github.com/icflorescu/mantine-datatable/blob/main/LICENSE)[![Image 34: Sponsor the author](https://img.shields.io/static/v1?label=github&message=sponsor&color=1c7ed6)](https://github.com/sponsors/icflorescu)

Built by [Ionut-Cristian Florescu](https://github.com/icflorescu) and [these awesome people](https://github.com/icflorescu/mantine-datatable/graphs/contributors).

Please [sponsor my work](https://github.com/sponsors/icflorescu) if you find it useful.

[![Image 35: GitHub Stars](https://img.shields.io/github/stars/icflorescu/mantine-datatable?style=flat&color=1c7ed6)](https://github.com/icflorescu/mantine-datatable)[![Image 36: NPM Downloads](https://img.shields.io/npm/dm/mantine-datatable.svg?style=flat&color=1c7ed6)](https://www.npmjs.com/package/mantine-datatable)
