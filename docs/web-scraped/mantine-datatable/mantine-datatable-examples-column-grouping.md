# Source: https://icflorescu.github.io/mantine-datatable/examples/column-grouping/

Title: Examples › Column grouping | Mantine DataTable

URL Source: https://icflorescu.github.io/mantine-datatable/examples/column-grouping/

Markdown Content:
Examples › Column grouping | Mantine DataTable
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

Examples › Column grouping
--------------------------

Sometimes a sub-set of data is very closely related. In such a case it might make sense to group the headers of those columns. This can be easily achieved by specifying `groups` instead of `columns`.

Each group requires the following properties:

*   `id`

Used as a[key](https://react.dev/learn/rendering-lists#keeping-list-items-in-order-with-key). Can be any string, as long as it is unique among the groups.

A humanized version of this value is used as header if no `title` is provided.
*   `columns`

An array of [column definitions](https://icflorescu.github.io/mantine-datatable/examples/column-properties-and-styling/) that are part of this group.

In addition to the aforementioned required properties, a group accepts some optional props for customization purposes:

*   `title`

A `ReactNode` that will be rendered inside the column group. If not specified (or set to`undefined`), the `id` is humanized to generate a string.
*   `textAlign: 'left' | 'center' | 'right'`

The text alignment for all columns in this group.
*   `className: string`

Optional class to apply to the group header.
*   `style`

Optional style to be applied to the group header.

Can be a style object or a function that receives the current theme and returns a style object.

Groups are hidden if they don’t have any visible columns. This could be the result of all columns being hidden due to the `hidden` or `visibleMediaQuery` attribute, or by simply providing an empty array of columns.

| Company | Contact information |
| --- | --- |
| Name | Mission statement | Street address | City | State |
| Feest, Bogan and Herzog | Innovate bricks-and-clicks metrics. | 21716 Ratke Drive | Stromanport | WY |
| Cummerata - Kuhlman | Harness real-time channels. | 6389 Dicki Stream | South Gate | NH |
| Goyette Inc | Productize front-end web services. | 8873 Mertz Rapid | Dorthyside | ID |
| Runte Inc | Engage synergistic infrastructures. | 2996 Ronny Mount | McAllen | MA |
| Goldner, Rohan and Lehner | Incubate cross-platform metrics. | 632 Broadway Avenue | North Louie | WY |
| Doyle, Hodkiewicz and O'Connell | Scale web-enabled e-business. | 576 Joyce Ways | Tyraburgh | KS |
| Rau - O'Hara | Innovate real-time applications. | 7508 Lansdowne Road | Shieldsborough | MI |
| Tillman - Jacobi | Matrix viral synergies. | 57918 Gwendolyn Circles | Sheridanport | MI |
| Connelly, Feest and Hodkiewicz | Maximize dynamic e-commerce. | 7057 Stanley Road | Kearaburgh | CA |
| Shanahan, Robel and Beier | Synthesize customized portals. | 378 Berta Crescent | West Gerry | KS |
| Kling - McLaughlin | Reinvent cross-platform channels. | 8346 Kertzmann Square | South Joesph | ID |
| Jogi - McLaughlin | Eliminate best-of-breed e-markets. | 83462 Shazam Street | North Joesph | ID |
| Jogi - McLaughlin | Eliminate best-of-breed e-markets. | 83462 Shazam Street | North Joesph | ID |

No records

Here is the code used to generate the table above:

ColumnGroupingExample.tsx companies.json

```
'use client';

import { DataTable } from 'mantine-datatable';
import { companies } from '~/data';

export function ColumnGroupingExample() {
  return (
    <DataTable
      withTableBorder
      withColumnBorders
      records={companies}
      groups={[
        {
          id: 'company',
          style: { fontStyle: 'italic' },
          columns: [
            { accessor: 'name' },
            { accessor: 'missionStatement', visibleMediaQuery: (theme) => `(min-width: ${theme.breakpoints.md})` },
          ],
        },
        {
          id: 'contact-info',
          title: 'Contact information',
          textAlign: 'center',
          style: (theme) => ({ color: theme.colors.blue[6] }),
          columns: [{ accessor: 'streetAddress' }, { accessor: 'city' }, { accessor: 'state', textAlign: 'right' }],
        },
        // 👇 all columns in this group are hidden, so it will not be rendered
        {
          id: 'other',
          columns: [{ accessor: 'id', hidden: true }],
        },
        // 👇 this group has no columns, so it will not be rendered
        {
          id: 'empty-group',
          title: 'Empty group',
          columns: [],
        },
      ]}
    />
  );
}
```

Expand code

### [Multilevel column grouping](https://icflorescu.github.io/mantine-datatable/examples/column-grouping/)

| Personal Information | Contact Information | Work Information |
| --- | --- | --- |
| Name | Demographics | Email | IDs |
| First Name | Last Name | Gender | Birth Date | Email Address | Employee ID | Department ID |
| Jerald | Howell | male | 5/21/1950 | Jerald.Howell32@yahoo.com | 69f81cf4-aac7-45f4-8567-0c03405edc52 | 72bc79a2-eb57-473e-bd35-8c72ce68f65d |
| Kathleen | Ruecker | female | 12/19/1943 | Kathleen_Ruecker@hotmail.com | 7cd87585-5e02-45f6-881a-80cbb2c83cea | 9a9af102-cf80-4393-a3a5-f54c1ad0ad24 |
| Erica | Volkman | female | 1/29/1955 | Erica.Volkman37@gmail.com | 060b7b1b-deba-4e38-9b75-82e69f1bae06 | d7cca8f2-cb18-4e2c-a207-88257f540341 |
| Clifford | Oberbrunner | male | 3/6/1979 | Clifford.Oberbrunner@hotmail.com | 84e46e16-efb9-4640-87a2-5108cb386cf2 | cee34a9b-e68b-49f8-a368-66f097f5c6fe |
| Alison | Kling | female | 1/27/1997 | Alison16@gmail.com | f14ab942-f6f2-413e-9495-a3a1c1fa0f8c | 049d164f-1649-4737-8c42-37348588d3bc |
| Sue | Zieme | female | 9/12/1960 | Sue.Zieme29@hotmail.com | bca16bee-ff3e-4b58-8c60-e39e4199ecaf | b7841b69-7207-41ed-9327-270c674619eb |
| Felicia | Gleason | female | 3/9/1977 | Felicia30@yahoo.com | d7e6a066-12bd-4f26-876b-4dc2eed3eabf | 2c664bed-50e2-439a-b4fd-af874f3eba53 |
| Alfredo | Zemlak | male | 11/12/1988 | Alfredo22@yahoo.com | e0624354-4d3c-48b0-b579-492954da168e | 4d1e93ad-5189-469b-8aec-d92e794c20be |
| Emily | Bartoletti | female | 1/5/1968 | Emily.Bartoletti@gmail.com | e57eaa3f-a968-49dc-9db4-cbfd463aa0e5 | cee34a9b-e68b-49f8-a368-66f097f5c6fe |
| Delores | Reynolds | female | 6/4/2004 | Delores.Reynolds@yahoo.com | c27a6249-5c0b-40cc-a519-fa4ed9ac4b96 | 72bc79a2-eb57-473e-bd35-8c72ce68f65d |

No records

Here is the code used to generate the table above:

MultilevelColumnGroupingExample.tsx companies.json

```
'use client';

import { DataTable } from 'mantine-datatable';
import { employees } from '~/data';

export function MultilevelColumnGroupingExample() {
  return (
    <DataTable
      withTableBorder
      withColumnBorders
      records={employees.slice(0, 10)}
      groups={[
        {
          id: 'personal-info',
          title: 'Personal Information',
          groups: [
            {
              id: 'name-group',
              title: 'Name',
              columns: [
                {
                  accessor: 'firstName',
                  title: 'First Name',
                  width: 120,
                },
                {
                  accessor: 'lastName',
                  title: 'Last Name',
                  width: 120,
                },
              ],
            },
            {
              id: 'demographics',
              title: 'Demographics',
              columns: [
                {
                  accessor: 'sex',
                  title: 'Gender',
                  width: 80,
                },
                {
                  accessor: 'birthDate',
                  title: 'Birth Date',
                  width: 120,
                  render: ({ birthDate }) => new Date(birthDate).toLocaleDateString(),
                },
              ],
            },
          ],
        },
        {
          id: 'contact-info',
          title: 'Contact Information',
          groups: [
            {
              id: 'email-group',
              title: 'Email',
              columns: [
                {
                  accessor: 'email',
                  title: 'Email Address',
                  width: 250,
                  ellipsis: true,
                },
              ],
            },
          ],
        },
        {
          id: 'work-info',
          title: 'Work Information',
          groups: [
            {
              id: 'identifiers',
              title: 'IDs',
              columns: [
                {
                  accessor: 'id',
                  title: 'Employee ID',
                  width: 100,
                  ellipsis: true,
                },
                {
                  accessor: 'department.id',
                  title: 'Department ID',
                  width: 100,
                  ellipsis: true,
                },
              ],
            },
          ],
        },
      ]}
    />
  );
}
```

Expand code

Head over to the next example to discover more features.

[Go back Examples › Column properties and styling](https://icflorescu.github.io/mantine-datatable/examples/column-properties-and-styling/)[Up next Examples › Default column properties](https://icflorescu.github.io/mantine-datatable/examples/default-column-properties/)

Mantine DataTable is used and trusted by
----------------------------------------

[![Image 1: Microsoft is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/microsoft.svg)](https://www.microsoft.com/ "Microsoft is using Mantine DataTable")[![Image 2: Namecheap is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/namecheap-light.svg)![Image 3: Namecheap is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/namecheap-dark.svg)](https://www.namecheap.com/ "Namecheap is using Mantine DataTable")[![Image 4: EasyWP is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/easywp-light.svg)![Image 5: EasyWP is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/easywp-dark.svg)](https://www.easywp.com/ "EasyWP is using Mantine DataTable")[![Image 6: LeasingSH.ro is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/leasingsh-ro-light.png)![Image 7: LeasingSH.ro is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/leasingsh-ro-dark.png)](https://leasingsh.ro/ "LeasingSH.ro is using Mantine DataTable")[![Image 8: CodeParrot.AI is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/codeparrot.svg) CodeParrot.AI](https://codeparrot.ai/ "CodeParrot.AI is using Mantine DataTable")[![Image 9: OmicsStudio is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/omicsstudio-light.svg)![Image 10: OmicsStudio is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/omicsstudio-dark.svg)](https://omicsstudio.com/ "OmicsStudio is using Mantine DataTable")[![Image 11: SegmentX is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/segmentx.png) SegmentX](https://segmentx.ai/ "SegmentX is using Mantine DataTable")[![Image 12: Aquarino is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/aquarino.svg)](http://aquarino.com.br/ "Aquarino is using Mantine DataTable")[![Image 13: Dera is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/dera.webp) Dera](https://getdera.com/ "Dera is using Mantine DataTable")[![Image 14: kappa.ai is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/kapa-light.png)![Image 15: kappa.ai is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/kapa-dark.png)](https://kapa.ai/ "kappa.ai is using Mantine DataTable")[![Image 16: exdatis is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/exdatis-light.svg)![Image 17: exdatis is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/exdatis-dark.svg)](https://exdatis.ai/ "exdatis is using Mantine DataTable")[![Image 18: teachfloor is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/teachfloor-light.svg)![Image 19: teachfloor is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/teachfloor-dark.svg)](https://www.teachfloor.com/ "teachfloor is using Mantine DataTable")[![Image 20: MARKUP is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/markup-light.png)![Image 21: MARKUP is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/markup-dark.png)](https://www.getmarkup.com/ "MARKUP is using Mantine DataTable")[![Image 22: InvenTree is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/inventree-light.png)![Image 23: InvenTree is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/inventree-dark.png)](https://inventree.org/ "InvenTree is using Mantine DataTable")[![Image 24: BookieBase is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/bookiebase-light.svg)![Image 25: BookieBase is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/bookiebase-dark.svg)](https://bookiebase.ie/ "BookieBase is using Mantine DataTable")[![Image 26: Zipline is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/zipline.png)](https://zipline.diced.sh/ "Zipline is using Mantine DataTable")[![Image 27: Pachtop is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/pachtop.png) Pachtop](https://pachtop.com/ "Pachtop is using Mantine DataTable")[![Image 28: Ganymede is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/ganymede.png) Ganymede](https://github.com/Zibbp/ganymede "Ganymede is using Mantine DataTable")[![Image 29: Pipedash is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/pipedash.png) Pipedash](https://github.com/hcavarsan/pipedash "Pipedash is using Mantine DataTable")[![Image 30: COH3 Stats is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/coh3-stats.png) COH3 Stats](https://coh3stats.com/ "COH3 Stats is using Mantine DataTable")[![Image 31: ccrentals.org is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/ccrentals-light.svg)![Image 32: ccrentals.org is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/ccrentals-dark.svg) ccrentals.org](https://www.ccrentals.org/ "ccrentals.org is using Mantine DataTable")

[![Image 33: MIT License](https://img.shields.io/npm/l/mantine-datatable.svg?style=flat&color=1c7ed6)](https://github.com/icflorescu/mantine-datatable/blob/main/LICENSE)[![Image 34: Sponsor the author](https://img.shields.io/static/v1?label=github&message=sponsor&color=1c7ed6)](https://github.com/sponsors/icflorescu)

Built by [Ionut-Cristian Florescu](https://github.com/icflorescu) and[these awesome people](https://github.com/icflorescu/mantine-datatable/graphs/contributors).

Please [sponsor my work](https://github.com/sponsors/icflorescu) if you find it useful.

[![Image 35: GitHub Stars](https://img.shields.io/github/stars/icflorescu/mantine-datatable?style=flat&color=1c7ed6)](https://github.com/icflorescu/mantine-datatable)[![Image 36: NPM Downloads](https://img.shields.io/npm/dm/mantine-datatable.svg?style=flat&color=1c7ed6)](https://www.npmjs.com/package/mantine-datatable)
