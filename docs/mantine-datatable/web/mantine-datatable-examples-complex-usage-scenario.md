# Source: https://icflorescu.github.io/mantine-datatable/examples/complex-usage-scenario/

Title: Examples › Complex usage scenario | Mantine DataTable

URL Source: https://icflorescu.github.io/mantine-datatable/examples/complex-usage-scenario/

Published Time: Tue, 20 Jan 2026 11:41:51 GMT

Markdown Content:
Examples › Complex usage scenario | Mantine DataTable
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

Examples › Complex usage scenario
---------------------------------

Here is a complex usage scenario featuring[custom column definitions](https://icflorescu.github.io/mantine-datatable/examples/column-properties-and-styling/),[asynchronous data loading](https://icflorescu.github.io/mantine-datatable/examples/asynchronous-data-loading/) with[TanStack Query](https://tanstack.com/query/latest),[sorting](https://icflorescu.github.io/mantine-datatable/examples/sorting/),[pagination](https://icflorescu.github.io/mantine-datatable/examples/pagination/), custom cell data rendering,[multiple row selection](https://icflorescu.github.io/mantine-datatable/examples/records-selection/),[row expansion](https://icflorescu.github.io/mantine-datatable/examples/expanding-rows/),[action cells](https://icflorescu.github.io/mantine-datatable/examples/row-actions-cell/), and[row context-menu](https://icflorescu.github.io/mantine-datatable/examples/using-with-mantine-contextmenu/).

| - [x] | Name | Email | Company | Department | City | State | Age |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| - [x] | Abraham Dooley | Abraham_Dooley@gmail.com | Tillman - Jacobi | Jewelery | Sheridanport | MI | 69 |  |
| - [x] | Adam Krajcik | Adam93@yahoo.com | Runte Inc | Outdoors | McAllen | MA | 71 |  |
| - [x] | Adam Pagac | Adam58@hotmail.com | Doyle, Hodkiewicz and O'Connell | Books | Tyraburgh | KS | 64 |  |
| - [x] | Adrian Padberg | Adrian.Padberg@yahoo.com | Goldner, Rohan and Lehner | Games | North Louie | WY | 60 |  |
| - [x] | Adrian Schiller | Adrian_Schiller@yahoo.com | Goyette Inc | Sports | Dorthyside | ID | 58 |  |
| - [x] | Agnes Conn | Agnes_Conn@yahoo.com | Doyle, Hodkiewicz and O'Connell | Jewelery | Tyraburgh | KS | 73 |  |
| - [x] | Agnes Simonis | Agnes.Simonis27@hotmail.com | Goldner, Rohan and Lehner | Kids | North Louie | WY | 24 |  |
| - [x] | Albert Jacobi | Albert8@hotmail.com | Connelly, Feest and Hodkiewicz | Jewelery | Kearaburgh | CA | 64 |  |
| - [x] | Albert Prosacco | Albert_Prosacco76@hotmail.com | Feest, Bogan and Herzog | Games | Stromanport | WY | 22 |  |
| - [x] | Alex Hills | Alex.Hills@hotmail.com | Rau - O'Hara | Automotive | Shieldsborough | MI | 81 |  |
| - [x] | Alexandra Ziemann | Alexandra.Ziemann@hotmail.com | Doyle, Hodkiewicz and O'Connell | Music | Tyraburgh | KS | 28 |  |
| - [x] | Alexis Davis | Alexis_Davis42@hotmail.com | Runte Inc | Beauty | McAllen | MA | 64 |  |
| - [x] | Alfonso Larson | Alfonso.Larson@hotmail.com | Connelly, Feest and Hodkiewicz | Outdoors | Kearaburgh | CA | 65 |  |
| - [x] | Alfredo Altenwerth | Alfredo.Altenwerth@hotmail.com | Shanahan, Robel and Beier | Movies | West Gerry | KS | 39 |  |
| - [x] | Alfredo Zemlak | Alfredo22@yahoo.com | Runte Inc | Games | McAllen | MA | 37 |  |
| - [x] | Alicia Leannon | Alicia62@yahoo.com | Feest, Bogan and Herzog | Sports | Stromanport | WY | 20 |  |
| - [x] | Alicia Wehner | Alicia_Wehner@yahoo.com | Rau - O'Hara | Home | Shieldsborough | MI | 72 |  |
| - [x] | Alison Kling | Alison16@gmail.com | Goyette Inc | Jewelery | Dorthyside | ID | 29 |  |
| - [x] | Allan Hilll | Allan.Hilll52@yahoo.com | Runte Inc | Games | McAllen | MA | 54 |  |
| - [x] | Allan Mertz | Allan_Mertz@yahoo.com | Feest, Bogan and Herzog | Sports | Stromanport | WY | 81 |  |
| - [x] | Allen Hackett | Allen44@hotmail.com | Tillman - Jacobi | Health | Sheridanport | MI | 41 |  |
| - [x] | Alma Lind | Alma.Lind@hotmail.com | Runte Inc | Baby | McAllen | MA | 28 |  |
| - [x] | Alonzo Kutch | Alonzo12@yahoo.com | Tillman - Jacobi | Sports | Sheridanport | MI | 43 |  |
| - [x] | Alton Langosh | Alton_Langosh46@hotmail.com | Doyle, Hodkiewicz and O'Connell | Kids | Tyraburgh | KS | 71 |  |
| - [x] | Alvin Kunde | Alvin55@hotmail.com | Cummerata - Kuhlman | Clothing | South Gate | NH | 69 |  |
| - [x] | Alyssa Kirlin-Rippin | Alyssa_Kirlin-Rippin@yahoo.com | Doyle, Hodkiewicz and O'Connell | Books | Tyraburgh | KS | 77 |  |
| - [x] | Amber Dietrich | Amber29@hotmail.com | Connelly, Feest and Hodkiewicz | Electronics | Kearaburgh | CA | 42 |  |
| - [x] | Amelia Bernhard-Lang | Amelia_Bernhard-Lang@gmail.com | Rau - O'Hara | Toys | Shieldsborough | MI | 24 |  |
| - [x] | Andy McClure | Andy29@yahoo.com | Runte Inc | Movies | McAllen | MA | 28 |  |
| - [x] | Angel Aufderhar | Angel.Aufderhar19@yahoo.com | Runte Inc | Health | McAllen | MA | 66 |  |
| - [x] | Angel Koss | Angel.Koss@yahoo.com | Runte Inc | Industrial | McAllen | MA | 55 |  |
| - [x] | Angela Mosciski | Angela35@hotmail.com | Rau - O'Hara | Beauty | Shieldsborough | MI | 68 |  |
| - [x] | Angelo Dietrich | Angelo.Dietrich@hotmail.com | Rau - O'Hara | Home | Shieldsborough | MI | 43 |  |
| - [x] | Angie Abbott | Angie57@hotmail.com | Runte Inc | Baby | McAllen | MA | 34 |  |
| - [x] | Anna Bayer | Anna_Bayer@gmail.com | Tillman - Jacobi | Music | Sheridanport | MI | 30 |  |
| - [x] | Anne King | Anne65@yahoo.com | Feest, Bogan and Herzog | Beauty | Stromanport | WY | 35 |  |
| - [x] | Anne Powlowski | Anne_Powlowski69@gmail.com | Connelly, Feest and Hodkiewicz | Music | Kearaburgh | CA | 69 |  |
| - [x] | Antonio Little-Bahringer | Antonio.Little-Bahringer@gmail.com | Shanahan, Robel and Beier | Games | West Gerry | KS | 37 |  |
| - [x] | April Baumbach | April58@gmail.com | Rau - O'Hara | Sports | Shieldsborough | MI | 31 |  |
| - [x] | Armando Lind | Armando_Lind@gmail.com | Feest, Bogan and Herzog | Games | Stromanport | WY | 62 |  |
| - [x] | Armando Okuneva | Armando56@gmail.com | Goyette Inc | Outdoors | Dorthyside | ID | 38 |  |
| - [x] | Arthur Roberts | Arthur_Roberts@hotmail.com | Feest, Bogan and Herzog | Games | Stromanport | WY | 33 |  |
| - [x] | Arturo Murray | Arturo.Murray17@yahoo.com | Cummerata - Kuhlman | Jewelery | South Gate | NH | 28 |  |
| - [x] | Austin O'Conner | Austin33@yahoo.com | Connelly, Feest and Hodkiewicz | Jewelery | Kearaburgh | CA | 25 |  |
| - [x] | Barbara McClure | Barbara.McClure79@hotmail.com | Doyle, Hodkiewicz and O'Connell | Shoes | Tyraburgh | KS | 38 |  |
| - [x] | Barry Jast | Barry.Jast@yahoo.com | Runte Inc | Grocery | McAllen | MA | 47 |  |
| - [x] | Benjamin Gottlieb | Benjamin23@yahoo.com | Doyle, Hodkiewicz and O'Connell | Shoes | Tyraburgh | KS | 30 |  |
| - [x] | Benjamin Yost-Johns | Benjamin73@hotmail.com | Rau - O'Hara | Sports | Shieldsborough | MI | 77 |  |
| - [x] | Benny Fahey | Benny.Fahey5@yahoo.com | Goyette Inc | Music | Dorthyside | ID | 67 |  |
| - [x] | Bernice Schinner | Bernice45@hotmail.com | Tillman - Jacobi | Garden | Sheridanport | MI | 20 |  |
| - [x] | Bernice Tillman | Bernice.Tillman15@hotmail.com | Connelly, Feest and Hodkiewicz | Sports | Kearaburgh | CA | 33 |  |
| - [x] | Bernice Upton | Bernice90@hotmail.com | Tillman - Jacobi | Games | Sheridanport | MI | 54 |  |
| - [x] | Bert Dicki | Bert_Dicki45@hotmail.com | Doyle, Hodkiewicz and O'Connell | Beauty | Tyraburgh | KS | 55 |  |
| - [x] | Bethany Schinner | Bethany.Schinner@yahoo.com | Cummerata - Kuhlman | Movies | South Gate | NH | 74 |  |
| - [x] | Betsy McClure-Wilderman | Betsy_McClure-Wilderman@gmail.com | Cummerata - Kuhlman | Games | South Gate | NH | 59 |  |
| - [x] | Beverly Heller | Beverly_Heller@gmail.com | Runte Inc | Beauty | McAllen | MA | 24 |  |
| - [x] | Blanche Luettgen | Blanche.Luettgen@gmail.com | Doyle, Hodkiewicz and O'Connell | Books | Tyraburgh | KS | 44 |  |
| - [x] | Blanche Zulauf | Blanche24@gmail.com | Feest, Bogan and Herzog | Sports | Stromanport | WY | 48 |  |
| - [x] | Bobby Trantow | Bobby_Trantow61@hotmail.com | Feest, Bogan and Herzog | Sports | Stromanport | WY | 44 |  |
| - [x] | Boyd Mohr | Boyd.Mohr@hotmail.com | Goyette Inc | Jewelery | Dorthyside | ID | 74 |  |
| - [x] | Brad Ullrich-Orn | Brad30@yahoo.com | Feest, Bogan and Herzog | Games | Stromanport | WY | 73 |  |
| - [x] | Bradford Trantow | Bradford.Trantow82@gmail.com | Feest, Bogan and Herzog | Toys | Stromanport | WY | 79 |  |
| - [x] | Brandi Ferry | Brandi.Ferry22@gmail.com | Runte Inc | Movies | McAllen | MA | 33 |  |
| - [x] | Brendan Williamson-D'Amore | Brendan34@yahoo.com | Feest, Bogan and Herzog | Sports | Stromanport | WY | 48 |  |
| - [x] | Brent Lockman | Brent_Lockman@yahoo.com | Goyette Inc | Kids | Dorthyside | ID | 37 |  |
| - [x] | Bridget Cummerata | Bridget_Cummerata@gmail.com | Cummerata - Kuhlman | Books | South Gate | NH | 65 |  |
| - [x] | Bruce Quitzon | Bruce20@yahoo.com | Shanahan, Robel and Beier | Movies | West Gerry | KS | 64 |  |
| - [x] | Bruce Veum | Bruce_Veum93@gmail.com | Shanahan, Robel and Beier | Clothing | West Gerry | KS | 81 |  |
| - [x] | Byron Champlin | Byron47@yahoo.com | Shanahan, Robel and Beier | Movies | West Gerry | KS | 41 |  |
| - [x] | Byron Romaguera | Byron_Romaguera34@hotmail.com | Connelly, Feest and Hodkiewicz | Games | Kearaburgh | CA | 66 |  |
| - [x] | Camille Wisoky | Camille37@gmail.com | Connelly, Feest and Hodkiewicz | Sports | Kearaburgh | CA | 43 |  |
| - [x] | Candace Grady | Candace.Grady@yahoo.com | Doyle, Hodkiewicz and O'Connell | Kids | Tyraburgh | KS | 81 |  |
| - [x] | Carl Crona | Carl29@hotmail.com | Runte Inc | Beauty | McAllen | MA | 48 |  |
| - [x] | Carl Kautzer | Carl_Kautzer@hotmail.com | Doyle, Hodkiewicz and O'Connell | Shoes | Tyraburgh | KS | 77 |  |
| - [x] | Carlton Jenkins | Carlton_Jenkins62@gmail.com | Runte Inc | Sports | McAllen | MA | 82 |  |
| - [x] | Carlton Langosh-Glover | Carlton.Langosh-Glover@gmail.com | Runte Inc | Baby | McAllen | MA | 59 |  |
| - [x] | Carol Littel | Carol.Littel@gmail.com | Rau - O'Hara | Beauty | Shieldsborough | MI | 74 |  |
| - [x] | Carroll Crooks | Carroll.Crooks@yahoo.com | Runte Inc | Music | McAllen | MA | 54 |  |
| - [x] | Carroll Heaney | Carroll.Heaney21@hotmail.com | Tillman - Jacobi | Games | Sheridanport | MI | 51 |  |
| - [x] | Cary Kerluke | Cary18@hotmail.com | Tillman - Jacobi | Games | Sheridanport | MI | 54 |  |
| - [x] | Cassandra Schneider | Cassandra_Schneider51@hotmail.com | Runte Inc | Industrial | McAllen | MA | 36 |  |
| - [x] | Cecilia Anderson | Cecilia.Anderson92@yahoo.com | Connelly, Feest and Hodkiewicz | Jewelery | Kearaburgh | CA | 80 |  |
| - [x] | Cedric Hagenes | Cedric78@hotmail.com | Goldner, Rohan and Lehner | Kids | North Louie | WY | 58 |  |
| - [x] | Charles Gutmann | Charles68@yahoo.com | Goyette Inc | Jewelery | Dorthyside | ID | 23 |  |
| - [x] | Charlie Beier | Charlie.Beier37@yahoo.com | Tillman - Jacobi | Sports | Sheridanport | MI | 33 |  |
| - [x] | Charlie Rosenbaum | Charlie.Rosenbaum58@gmail.com | Tillman - Jacobi | Grocery | Sheridanport | MI | 76 |  |
| - [x] | Chelsea Wilderman | Chelsea26@hotmail.com | Goyette Inc | Books | Dorthyside | ID | 74 |  |
| - [x] | Christie Kuvalis | Christie85@hotmail.com | Goldner, Rohan and Lehner | Games | North Louie | WY | 40 |  |
| - [x] | Cindy Goldner | Cindy_Goldner47@yahoo.com | Doyle, Hodkiewicz and O'Connell | Shoes | Tyraburgh | KS | 47 |  |
| - [x] | Claude Emard | Claude_Emard95@yahoo.com | Doyle, Hodkiewicz and O'Connell | Beauty | Tyraburgh | KS | 35 |  |
| - [x] | Claude Kuvalis | Claude_Kuvalis88@hotmail.com | Doyle, Hodkiewicz and O'Connell | Shoes | Tyraburgh | KS | 29 |  |
| - [x] | Claudia Windler | Claudia.Windler@hotmail.com | Cummerata - Kuhlman | Computers | South Gate | NH | 35 |  |
| - [x] | Clay Heidenreich | Clay_Heidenreich@yahoo.com | Runte Inc | Baby | McAllen | MA | 32 |  |
| - [x] | Clay Shields | Clay.Shields@yahoo.com | Goyette Inc | Health | Dorthyside | ID | 64 |  |
| - [x] | Clifford Oberbrunner | Clifford.Oberbrunner@hotmail.com | Rau - O'Hara | Automotive | Shieldsborough | MI | 47 |  |
| - [x] | Clifton Feeney | Clifton60@yahoo.com | Cummerata - Kuhlman | Movies | South Gate | NH | 59 |  |
| - [x] | Colin Leuschke | Colin3@gmail.com | Doyle, Hodkiewicz and O'Connell | Shoes | Tyraburgh | KS | 48 |  |
| - [x] | Colleen Block | Colleen_Block@yahoo.com | Shanahan, Robel and Beier | Games | West Gerry | KS | 80 |  |
| - [x] | Colleen Crooks | Colleen84@hotmail.com | Rau - O'Hara | Automotive | Shieldsborough | MI | 27 |  |
| - [x] | Connie Zemlak | Connie_Zemlak@gmail.com | Runte Inc | Games | McAllen | MA | 46 |  |

1 - 100 / 500

1 2 3 4 5

No records

Since this example is using TanStack Query, we have to wrap everything in a `QueryClientProvider`like so:

```
'use client';

import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { useState } from 'react';

export function ComplexUsageExampleWrapper({ children }: React.PropsWithChildren) {
  const [queryClient] = useState(
    () =>
      new QueryClient({
        defaultOptions: {
          queries: {
            // With SSR, we usually want to set some default staleTime
            // above 0 to avoid refetching immediately on the client
            staleTime: 60 * 1000,
          },
        },
      })
  );

  return <QueryClientProvider client={queryClient}>{children}</QueryClientProvider>;
}
```

Expand code

Here is the actual code:

ComplexUsageExample.tsx ComplexUsageExample.module.css data/async.ts data/index.ts

```
'use client';

import type { MantineTheme } from '@mantine/core';
import { ActionIcon, Button, Center, Flex, Group, Image, Text, TextInput, rem } from '@mantine/core';
import { closeAllModals, openModal } from '@mantine/modals';
import { showNotification } from '@mantine/notifications';
import { IconClick, IconEdit, IconMessage, IconTrash, IconTrashX } from '@tabler/icons-react';
import { useQuery } from '@tanstack/react-query';
import type { DataTableColumn, DataTableProps, DataTableSortStatus } from 'mantine-datatable';
import { DataTable } from 'mantine-datatable';
import dayjs from 'dayjs';
import { useContextMenu } from 'mantine-contextmenu';
import { useCallback, useState } from 'react';
import type { Employee } from '~/data';
import { getEmployeesAsync } from '~/data/async';
import classes from './ComplexUsageExample.module.css';

const PAGE_SIZE = 100;

export function ComplexUsageExample() {
  const { showContextMenu, hideContextMenu } = useContextMenu();

  const [page, setPage] = useState(1);
  const [sortStatus, setSortStatus] = useState<DataTableSortStatus<Employee>>({
    columnAccessor: 'name',
    direction: 'asc',
  });

  const { data, isFetching } = useQuery({
    queryKey: ['employees', sortStatus.columnAccessor, sortStatus.direction, page],
    queryFn: () => getEmployeesAsync({ recordsPerPage: PAGE_SIZE, page, sortStatus, delay: { min: 300, max: 500 } }),
  });

  const [selectedRecords, setSelectedRecords] = useState<Employee[]>([]);

  const handleSortStatusChange = (status: DataTableSortStatus<Employee>) => {
    setPage(1);
    setSortStatus(status);
  };

  const editRecord = useCallback(({ firstName, lastName }: Employee) => {
    showNotification({
      withBorder: true,
      title: 'Editing record',
      message: `In a real application we could show a popup to edit ${firstName} ${lastName}, but this is just a demo, so we're not going to do that`,
    });
  }, []);

  const deleteRecord = useCallback(({ firstName, lastName }: Employee) => {
    showNotification({
      withBorder: true,
      color: 'red',
      title: 'Deleting record',
      message: `Should delete ${firstName} ${lastName}, but we're not going to, because this is just a demo`,
    });
  }, []);

  const deleteSelectedRecords = useCallback(() => {
    showNotification({
      withBorder: true,
      color: 'red',
      title: 'Deleting multiple records',
      message: `Should delete ${selectedRecords.length} records, but we're not going to do that because deleting data is bad... and this is just a demo anyway`,
    });
  }, [selectedRecords.length]);

  const sendMessage = useCallback(({ firstName, lastName }: Employee) => {
    showNotification({
      withBorder: true,
      title: 'Sending message',
      message: `A real application could send a message to ${firstName} ${lastName}, but this is just a demo and we're not going to do that because we don't have a backend`,
      color: 'green',
    });
  }, []);

  const renderActions: DataTableColumn<Employee>['render'] = (record) => (
    <Group gap={4} justify="right" wrap="nowrap">
      <ActionIcon
        size="sm"
        variant="transparent"
        color="green"
        onClick={(e) => {
          e.stopPropagation(); // 👈 prevent triggering the row click function
          openModal({
            title: `Send message to ${record.firstName} ${record.lastName}`,
            classNames: { header: classes.modalHeader, title: classes.modalTitle },
            children: (
              <>
                <TextInput mt="md" placeholder="Your message..." />
                <Group mt="md" gap="sm" justify="flex-end">
                  <Button variant="transparent" c="dimmed" onClick={() => closeAllModals()}>
                    Cancel
                  </Button>
                  <Button
                    color="green"
                    onClick={() => {
                      sendMessage(record);
                      closeAllModals();
                    }}
                  >
                    Send
                  </Button>
                </Group>
              </>
            ),
          });
        }}
      >
        <IconMessage size={16} />
      </ActionIcon>
      <ActionIcon
        size="sm"
        variant="transparent"
        onClick={(e) => {
          e.stopPropagation(); // 👈 prevent triggering the row click function
          editRecord(record);
        }}
      >
        <IconEdit size={16} />
      </ActionIcon>
    </Group>
  );

  const rowExpansion: DataTableProps<Employee>['rowExpansion'] = {
    allowMultiple: true,
    content: ({ record: { id, sex, firstName, lastName, birthDate, department } }) => (
      <Flex p="xs" pl={rem(50)} gap="md" align="center">
        <Image
          radius="sm"
          w={50}
          h={50}
          alt={`${firstName} ${lastName}`}
          src={`https://xsgames.co/randomusers/avatar.php?g=${sex}&q=${id}`}
        />
        <Text size="sm" fs="italic">
          {firstName} {lastName}, born on {dayjs(birthDate).format('MMM D YYYY')}, works in {department.name} department
          at {department.company.name}.
          <br />
          His office address is {department.company.streetAddress}, {department.company.city},{' '}
          {department.company.state}.
        </Text>
      </Flex>
    ),
  };

  const handleContextMenu: DataTableProps<Employee>['onRowContextMenu'] = ({ record, event }) =>
    showContextMenu([
      {
        key: 'edit',
        icon: <IconEdit size={14} />,
        title: `Edit ${record.firstName} ${record.lastName}`,
        onClick: () => editRecord(record),
      },
      {
        key: 'delete',
        title: `Delete ${record.firstName} ${record.lastName}`,
        icon: <IconTrashX size={14} />,
        color: 'red',
        onClick: () => deleteRecord(record),
      },
      { key: 'divider' },
      {
        key: 'deleteMany',
        hidden: selectedRecords.length <= 1 || !selectedRecords.map((r) => r.id).includes(record.id),
        title: `Delete ${selectedRecords.length} selected records`,
        icon: <IconTrash size={14} />,
        color: 'red',
        onClick: deleteSelectedRecords,
      },
    ])(event);

  const now = dayjs();
  const aboveXs = (theme: MantineTheme) => `(min-width: ${theme.breakpoints.xs})`;

  const columns: DataTableProps<Employee>['columns'] = [
    {
      accessor: 'name',
      noWrap: true,
      sortable: true,
      render: ({ firstName, lastName }) => `${firstName} ${lastName}`,
    },
    {
      accessor: 'email',
      sortable: true,
    },
    {
      accessor: 'department.company.name',
      title: 'Company',
      noWrap: true,
      sortable: true,
      visibleMediaQuery: aboveXs,
    },
    {
      accessor: 'department.name',
      title: 'Department',
      sortable: true,
      visibleMediaQuery: aboveXs,
    },
    {
      accessor: 'department.company.city',
      title: 'City',
      noWrap: true,
      visibleMediaQuery: aboveXs,
    },
    {
      accessor: 'department.company.state',
      title: 'State',
      visibleMediaQuery: aboveXs,
    },
    {
      accessor: 'age',
      width: 80,
      textAlign: 'right',
      sortable: true,
      render: ({ birthDate }) => now.diff(birthDate, 'years'),
      visibleMediaQuery: aboveXs,
    },
    {
      accessor: 'actions',
      title: (
        <Center>
          <IconClick size={16} />
        </Center>
      ),
      width: '0%', // 👈 use minimal width
      render: renderActions,
    },
  ];

  return (
    <DataTable
      height="70dvh"
      minHeight={400}
      maxHeight={1000}
      withTableBorder
      highlightOnHover
      borderRadius="sm"
      withColumnBorders
      striped
      verticalAlign="top"
      pinLastColumn
      columns={columns}
      fetching={isFetching}
      records={data?.employees}
      page={page}
      onPageChange={setPage}
      totalRecords={data?.total}
      recordsPerPage={PAGE_SIZE}
      sortStatus={sortStatus}
      onSortStatusChange={handleSortStatusChange}
      selectedRecords={selectedRecords}
      onSelectedRecordsChange={setSelectedRecords}
      rowExpansion={rowExpansion}
      onRowContextMenu={handleContextMenu}
      onScroll={hideContextMenu}
    />
  );
}
```

Expand code

Head over to the next page to see Mantine DataTable type definitions.

[Go back Examples › Using bodyRef with AutoAnimate](https://icflorescu.github.io/mantine-datatable/examples/using-with-auto-animate/)[Up next Type definitions](https://icflorescu.github.io/mantine-datatable/type-definitions/)

Mantine DataTable is used and trusted by
----------------------------------------

[![Image 1: Microsoft is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/microsoft.svg)](https://www.microsoft.com/ "Microsoft is using Mantine DataTable")[![Image 2: Namecheap is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/namecheap-light.svg)![Image 3: Namecheap is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/namecheap-dark.svg)](https://www.namecheap.com/ "Namecheap is using Mantine DataTable")[![Image 4: EasyWP is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/easywp-light.svg)![Image 5: EasyWP is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/easywp-dark.svg)](https://www.easywp.com/ "EasyWP is using Mantine DataTable")[![Image 6: LeasingSH.ro is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/leasingsh-ro-light.png)![Image 7: LeasingSH.ro is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/leasingsh-ro-dark.png)](https://leasingsh.ro/ "LeasingSH.ro is using Mantine DataTable")[![Image 8: CodeParrot.AI is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/codeparrot.svg) CodeParrot.AI](https://codeparrot.ai/ "CodeParrot.AI is using Mantine DataTable")[![Image 9: OmicsStudio is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/omicsstudio-light.svg)![Image 10: OmicsStudio is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/omicsstudio-dark.svg)](https://omicsstudio.com/ "OmicsStudio is using Mantine DataTable")[![Image 11: SegmentX is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/segmentx.png) SegmentX](https://segmentx.ai/ "SegmentX is using Mantine DataTable")[![Image 12: Aquarino is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/aquarino.svg)](http://aquarino.com.br/ "Aquarino is using Mantine DataTable")[![Image 13: Dera is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/dera.webp) Dera](https://getdera.com/ "Dera is using Mantine DataTable")[![Image 14: kappa.ai is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/kapa-light.png)![Image 15: kappa.ai is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/kapa-dark.png)](https://kapa.ai/ "kappa.ai is using Mantine DataTable")[![Image 16: exdatis is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/exdatis-light.svg)![Image 17: exdatis is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/exdatis-dark.svg)](https://exdatis.ai/ "exdatis is using Mantine DataTable")[![Image 18: teachfloor is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/teachfloor-light.svg)![Image 19: teachfloor is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/teachfloor-dark.svg)](https://www.teachfloor.com/ "teachfloor is using Mantine DataTable")[![Image 20: MARKUP is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/markup-light.png)![Image 21: MARKUP is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/markup-dark.png)](https://www.getmarkup.com/ "MARKUP is using Mantine DataTable")[![Image 22: InvenTree is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/inventree-light.png)![Image 23: InvenTree is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/inventree-dark.png)](https://inventree.org/ "InvenTree is using Mantine DataTable")[![Image 24: BookieBase is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/bookiebase-light.svg)![Image 25: BookieBase is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/bookiebase-dark.svg)](https://bookiebase.ie/ "BookieBase is using Mantine DataTable")[![Image 26: Zipline is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/zipline.png)](https://zipline.diced.sh/ "Zipline is using Mantine DataTable")[![Image 27: Pachtop is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/pachtop.png) Pachtop](https://pachtop.com/ "Pachtop is using Mantine DataTable")[![Image 28: Ganymede is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/ganymede.png) Ganymede](https://github.com/Zibbp/ganymede "Ganymede is using Mantine DataTable")[![Image 29: Pipedash is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/pipedash.png) Pipedash](https://github.com/hcavarsan/pipedash "Pipedash is using Mantine DataTable")[![Image 30: COH3 Stats is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/coh3-stats.png) COH3 Stats](https://coh3stats.com/ "COH3 Stats is using Mantine DataTable")[![Image 31: ccrentals.org is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/ccrentals-light.svg)![Image 32: ccrentals.org is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/ccrentals-dark.svg) ccrentals.org](https://www.ccrentals.org/ "ccrentals.org is using Mantine DataTable")

[![Image 33: MIT License](https://img.shields.io/npm/l/mantine-datatable.svg?style=flat&color=1c7ed6)](https://github.com/icflorescu/mantine-datatable/blob/main/LICENSE)[![Image 34: Sponsor the author](https://img.shields.io/static/v1?label=github&message=sponsor&color=1c7ed6)](https://github.com/sponsors/icflorescu)

Built by [Ionut-Cristian Florescu](https://github.com/icflorescu) and[these awesome people](https://github.com/icflorescu/mantine-datatable/graphs/contributors).

Please [sponsor my work](https://github.com/sponsors/icflorescu) if you find it useful.

[![Image 35: GitHub Stars](https://img.shields.io/github/stars/icflorescu/mantine-datatable?style=flat&color=1c7ed6)](https://github.com/icflorescu/mantine-datatable)[![Image 36: NPM Downloads](https://img.shields.io/npm/dm/mantine-datatable.svg?style=flat&color=1c7ed6)](https://www.npmjs.com/package/mantine-datatable)
