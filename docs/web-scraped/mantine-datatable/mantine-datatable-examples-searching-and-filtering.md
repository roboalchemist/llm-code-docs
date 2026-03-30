# Source: https://icflorescu.github.io/mantine-datatable/examples/searching-and-filtering/

Title: Examples › Searching and filtering | Mantine DataTable

URL Source: https://icflorescu.github.io/mantine-datatable/examples/searching-and-filtering/

Markdown Content:
Examples › Searching and filtering | Mantine DataTable
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

Examples › Searching and filtering
----------------------------------

Adjust the array of `records` you’re feeding to Mantine DataTable based on your own logic in order to perform searching and filtering.

In order to support column-based filtering you can use the `filter` and `filtering`[column properties](https://icflorescu.github.io/mantine-datatable/examples/column-properties-and-styling/).

Here’s a possible (rather naive and rough around the edges) implementation:

| Name | Department name | Company | Birth date | Age |
| --- | --- | --- | --- | --- |
| Jerald Howell | Industrial | Runte Inc | May 21 1950 | 75 |
| Kathleen Ruecker | Computers | Shanahan, Robel and Beier | Dec 19 1943 | 82 |
| Erica Volkman | Toys | Goyette Inc | Jan 29 1955 | 71 |
| Clifford Oberbrunner | Automotive | Rau - O'Hara | Mar 06 1979 | 47 |
| Alison Kling | Jewelery | Goyette Inc | Jan 27 1997 | 29 |
| Sue Zieme | Books | Cummerata - Kuhlman | Sep 12 1960 | 65 |
| Felicia Gleason | Shoes | Doyle, Hodkiewicz and O'Connell | Mar 09 1977 | 49 |
| Alfredo Zemlak | Games | Runte Inc | Nov 12 1988 | 37 |
| Emily Bartoletti | Automotive | Rau - O'Hara | Jan 05 1968 | 58 |
| Delores Reynolds | Industrial | Runte Inc | Jun 04 2004 | 21 |
| Louis Schamberger | Tools | Cummerata - Kuhlman | Sep 07 1994 | 31 |
| Beverly Heller | Beauty | Runte Inc | Nov 29 2001 | 24 |
| Eugene Feest | Kids | Goyette Inc | Feb 20 1954 | 72 |
| Martin Bahringer | Beauty | Rau - O'Hara | May 26 1945 | 80 |
| Ellis Miller | Electronics | Connelly, Feest and Hodkiewicz | May 24 1950 | 75 |
| Gloria Cole | Home | Doyle, Hodkiewicz and O'Connell | Dec 09 1996 | 29 |
| Linda Witting | Baby | Doyle, Hodkiewicz and O'Connell | May 16 1965 | 60 |
| Gregg Kutch | Movies | Shanahan, Robel and Beier | Nov 28 1986 | 39 |
| Mamie Raynor | Grocery | Cummerata - Kuhlman | Nov 05 1992 | 33 |
| Erick Bruen | Electronics | Goyette Inc | Sep 26 1952 | 73 |
| Faith Langworth | Clothing | Runte Inc | Nov 27 1983 | 42 |
| Alicia Leannon | Sports | Feest, Bogan and Herzog | Dec 27 2005 | 20 |
| Boyd Mohr | Jewelery | Goyette Inc | Jun 18 1951 | 74 |
| Lindsey Heidenreich | Games | Shanahan, Robel and Beier | Jul 13 1997 | 28 |
| Elsa Marvin | Books | Tillman - Jacobi | Oct 07 1982 | 43 |
| Debbie Hagenes | Clothing | Runte Inc | Jan 24 1968 | 58 |
| Lionel McCullough | Kids | Goldner, Rohan and Lehner | Feb 23 1986 | 40 |
| Kim Lebsack | Jewelery | Cummerata - Kuhlman | Jun 11 1970 | 55 |
| Rolando Weissnat | Home | Rau - O'Hara | Apr 25 1951 | 74 |
| Jacqueline Lesch | Games | Runte Inc | Jul 22 1978 | 47 |
| Felix Stokes | Kids | Goyette Inc | Mar 21 1984 | 41 |
| Renee Tillman | Industrial | Goldner, Rohan and Lehner | Nov 24 1953 | 72 |
| Richard Watsica | Outdoors | Runte Inc | Jun 10 1971 | 54 |
| Nathan Wolf | Games | Goldner, Rohan and Lehner | Jul 02 1998 | 27 |
| Jonathan Keebler-Crona | Music | Goyette Inc | Oct 22 2002 | 23 |
| Kathleen Spinka | Jewelery | Goldner, Rohan and Lehner | Feb 28 1947 | 79 |
| Bernice Schinner | Garden | Tillman - Jacobi | Dec 23 2005 | 20 |
| Adam Pagac | Books | Doyle, Hodkiewicz and O'Connell | Dec 04 1961 | 64 |
| Earl Ryan | Beauty | Rau - O'Hara | Jan 08 1961 | 65 |
| Greg Bailey | Home | Rau - O'Hara | Jan 02 1967 | 59 |
| Anne Powlowski | Music | Connelly, Feest and Hodkiewicz | Jan 26 1957 | 69 |
| Abraham Dooley | Jewelery | Tillman - Jacobi | Oct 05 1956 | 69 |
| Myron Lemke | Shoes | Feest, Bogan and Herzog | Sep 27 1978 | 47 |
| Dianna Gislason-Lesch | Games | Cummerata - Kuhlman | May 29 1966 | 59 |
| Reginald Hagenes | Industrial | Runte Inc | May 19 1950 | 75 |
| Shelia Turcotte | Music | Goyette Inc | Jul 22 1959 | 66 |
| Carlton Jenkins | Sports | Runte Inc | Jun 07 1943 | 82 |
| Lance Wiegand | Grocery | Cummerata - Kuhlman | Jul 12 1966 | 59 |
| Ruby Graham | Sports | Feest, Bogan and Herzog | May 30 1970 | 55 |
| Hattie Collier | Outdoors | Goyette Inc | Apr 14 1954 | 71 |
| Viola Rath | Movies | Runte Inc | Mar 24 1970 | 55 |
| Roland Huel | Jewelery | Doyle, Hodkiewicz and O'Connell | Apr 20 1973 | 52 |
| Leticia Wiegand | Kids | Goyette Inc | Jan 13 1958 | 68 |
| Jacqueline Kulas | Beauty | Feest, Bogan and Herzog | Aug 30 1960 | 65 |
| Cristina Jaskolski | Sports | Feest, Bogan and Herzog | Jan 25 1966 | 60 |
| Felipe Daugherty | Music | Connelly, Feest and Hodkiewicz | Aug 12 1969 | 56 |
| Timothy Heaney | Kids | Doyle, Hodkiewicz and O'Connell | Dec 05 2005 | 20 |
| Alonzo Kutch | Sports | Tillman - Jacobi | May 02 1982 | 43 |
| Keith Kling | Sports | Goyette Inc | Feb 16 1961 | 65 |
| Janice Goyette | Sports | Runte Inc | Mar 14 1963 | 62 |
| Helen Kunze-MacGyver | Jewelery | Doyle, Hodkiewicz and O'Connell | Feb 11 2002 | 24 |
| Barry Jast | Grocery | Runte Inc | May 09 1978 | 47 |
| Ramiro Cummings | Sports | Goyette Inc | Apr 09 1966 | 59 |
| Antonio Little-Bahringer | Games | Shanahan, Robel and Beier | Nov 21 1988 | 37 |
| Samuel Zemlak | Electronics | Goyette Inc | Apr 28 1964 | 61 |
| Doris Emard | Games | Runte Inc | May 04 2003 | 22 |
| Olivia Abernathy | Outdoors | Runte Inc | Apr 30 1969 | 56 |
| Justin Kohler | Health | Goyette Inc | Jan 11 1980 | 46 |
| Scott Oberbrunner | Sports | Goyette Inc | Jan 22 1997 | 29 |
| Yolanda Spinka | Music | Connelly, Feest and Hodkiewicz | Jan 19 1981 | 45 |
| Brad Ullrich-Orn | Games | Feest, Bogan and Herzog | Aug 08 1952 | 73 |
| Gloria Fisher | Health | Goyette Inc | Nov 20 1995 | 30 |
| Sergio Crist | Books | Goldner, Rohan and Lehner | May 31 1995 | 30 |
| Theresa Sporer | Sports | Goyette Inc | May 15 2003 | 22 |
| Theodore Wiegand | Games | Cummerata - Kuhlman | May 18 2000 | 25 |
| Rudy Rowe | Grocery | Tillman - Jacobi | Oct 01 1962 | 63 |
| Kurt Raynor | Toys | Goyette Inc | Aug 20 1957 | 68 |
| Ruth Medhurst | Home | Doyle, Hodkiewicz and O'Connell | Jan 09 1947 | 79 |
| Tim Abernathy | Shoes | Doyle, Hodkiewicz and O'Connell | Oct 23 1984 | 41 |
| Rebecca Runolfsdottir | Grocery | Runte Inc | Jul 07 1964 | 61 |
| Angel Aufderhar | Health | Runte Inc | Jun 22 1959 | 66 |
| Javier Bergstrom | Movies | Cummerata - Kuhlman | Oct 20 1993 | 32 |
| Leigh Klocko | Music | Rau - O'Hara | Jun 14 1955 | 70 |
| Taylor Rice | Beauty | Goldner, Rohan and Lehner | Sep 10 1948 | 77 |
| Cindy Goldner | Shoes | Doyle, Hodkiewicz and O'Connell | Nov 30 1978 | 47 |
| Shannon Crist | Outdoors | Connelly, Feest and Hodkiewicz | Nov 12 1994 | 31 |
| Sarah Maggio | Books | Goyette Inc | Nov 09 2000 | 25 |
| Carlton Langosh-Glover | Baby | Runte Inc | Dec 06 1966 | 59 |
| Felicia Roob | Games | Doyle, Hodkiewicz and O'Connell | Dec 21 1968 | 57 |
| Simon Kuhic | Kids | Goldner, Rohan and Lehner | May 07 1958 | 67 |
| Sharon Daniel | Music | Runte Inc | Jul 05 1999 | 26 |
| Erin Bayer | Books | Tillman - Jacobi | Jul 04 1982 | 43 |
| Erika Powlowski-Corwin | Sports | Connelly, Feest and Hodkiewicz | Oct 10 1949 | 76 |
| Vicky Pollich | Books | Cummerata - Kuhlman | May 22 1986 | 39 |
| Felicia Ziemann | Industrial | Runte Inc | Dec 15 1991 | 34 |
| Colleen Crooks | Automotive | Rau - O'Hara | Jun 06 1998 | 27 |
| Jimmy Fisher | Kids | Goyette Inc | Dec 10 1945 | 80 |
| Lula Reichert | Games | Cummerata - Kuhlman | Mar 17 1995 | 30 |
| Bethany Schinner | Movies | Cummerata - Kuhlman | Nov 12 1951 | 74 |
| Allen Hackett | Health | Tillman - Jacobi | May 07 1984 | 41 |

No records

The code for this example is as follows:

```
'use client';

import { ActionIcon, Button, Checkbox, MultiSelect, Stack, TextInput } from '@mantine/core';
import { DatePicker, type DatesRangeValue } from '@mantine/dates';
import { useDebouncedValue } from '@mantine/hooks';
import { IconSearch, IconX } from '@tabler/icons-react';
import { DataTable } from 'mantine-datatable';
import dayjs from 'dayjs';
import { useEffect, useMemo, useState } from 'react';
import { employees } from '~/data';

const initialRecords = employees.slice(0, 100);

export function SearchingAndFilteringExample() {
  const [records, setRecords] = useState(initialRecords);

  const departments = useMemo(() => {
    const departments = new Set(employees.map((e) => e.department.name));
    return [...departments];
  }, []);

  const [query, setQuery] = useState('');
  const [selectedDepartments, setSelectedDepartments] = useState<string[]>([]);
  const [birthdaySearchRange, setBirthdaySearchRange] = useState<DatesRangeValue>();
  const [seniors, setSeniors] = useState(false);
  const [debouncedQuery] = useDebouncedValue(query, 200);

  useEffect(() => {
    // eslint-disable-next-line react-hooks/set-state-in-effect
    setRecords(
      initialRecords.filter(({ firstName, lastName, department, birthDate }) => {
        if (
          debouncedQuery !== '' &&
          !`${firstName} ${lastName}`.toLowerCase().includes(debouncedQuery.trim().toLowerCase())
        )
          return false;

        if (
          birthdaySearchRange &&
          birthdaySearchRange[0] &&
          birthdaySearchRange[1] &&
          (dayjs(birthdaySearchRange[0]).isAfter(birthDate, 'day') ||
            dayjs(birthdaySearchRange[1]).isBefore(birthDate, 'day'))
        )
          return false;

        if (selectedDepartments.length && !selectedDepartments.some((d) => d === department.name)) return false;

        if (seniors && dayjs().diff(birthDate, 'y') < 70) return false;

        return true;
      })
    );
  }, [debouncedQuery, birthdaySearchRange, selectedDepartments, seniors]);

  return (
    <DataTable
      height={300}
      withTableBorder
      withColumnBorders
      records={records}
      columns={[
        {
          accessor: 'name',
          render: ({ firstName, lastName }) => `${firstName} ${lastName}`,
          filter: (
            <TextInput
              label="Employees"
              description="Show employees whose names include the specified text"
              placeholder="Search employees..."
              leftSection={<IconSearch size={16} />}
              rightSection={
                <ActionIcon size="sm" variant="transparent" c="dimmed" onClick={() => setQuery('')}>
                  <IconX size={14} />
                </ActionIcon>
              }
              value={query}
              onChange={(e) => setQuery(e.currentTarget.value)}
            />
          ),
          filtering: query !== '',
        },
        {
          accessor: 'department.name',
          filter: (
            <MultiSelect
              label="Departments"
              description="Show all employees working at the selected departments"
              data={departments}
              value={selectedDepartments}
              placeholder="Search departments…"
              onChange={setSelectedDepartments}
              leftSection={<IconSearch size={16} />}
              comboboxProps={{ withinPortal: false }}
              clearable
              searchable
            />
          ),
          filtering: selectedDepartments.length > 0,
        },
        { accessor: 'department.company.name', title: 'Company' },
        {
          accessor: 'birthDate',
          textAlign: 'right',
          render: ({ birthDate }) => dayjs(birthDate).format('MMM DD YYYY'),
          filter: ({ close }) => (
            <Stack>
              <DatePicker
                maxDate={new Date()}
                type="range"
                value={birthdaySearchRange}
                onChange={setBirthdaySearchRange}
              />
              <Button
                disabled={!birthdaySearchRange}
                variant="light"
                onClick={() => {
                  setBirthdaySearchRange(undefined);
                  close();
                }}
              >
                Clear
              </Button>
            </Stack>
          ),
          filtering: Boolean(birthdaySearchRange),
        },
        {
          accessor: 'age',
          textAlign: 'right',
          render: ({ birthDate }) => dayjs().diff(birthDate, 'y'),
          filter: () => (
            <Checkbox
              label="Seniors"
              description="Show employees who are older than 70 years"
              checked={seniors}
              onChange={() => {
                setSeniors((current) => !current);
              }}
            />
          ),
        },
      ]}
    />
  );
}
```

Expand code

To use the Mantine Component with a popover inside the filter column property, you need to render the child properties without using a Portal. Please refer to the Mantine documentation on [Nested Popovers](https://mantine.dev/core/popover/#nested-popovers) for more details.

Why no built-in “Excel-like” searching and filtering support?

You’ll often have to implement searching and filtering data in your projects.

However there’s simply no way for Mantine DataTable to accommodate every possible usage scenario out there. Most of the times you’d have to deal with pagination, sorting, asynchronous loading; sometimes you’d have to place a search box or custom filtering criteria selectors in the header of your entire website/application.

Not to mention that in real-life you’d most often do the actual filtering and/or searching in a server API.

The responsibilities and areas of control are most of the times spread across your application’s UI and architectural layers, and trying to fit all this in a standard component design and behavior would needlessly constrain the developer.

Head over to the next example to discover more features.

[Go back Examples › Infinite scrolling](https://icflorescu.github.io/mantine-datatable/examples/infinite-scrolling/)[Up next Examples › Records selection](https://icflorescu.github.io/mantine-datatable/examples/records-selection/)

Mantine DataTable is used and trusted by
----------------------------------------

[![Image 1: Microsoft is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/microsoft.svg)](https://www.microsoft.com/ "Microsoft is using Mantine DataTable")[![Image 2: Namecheap is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/namecheap-light.svg)![Image 3: Namecheap is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/namecheap-dark.svg)](https://www.namecheap.com/ "Namecheap is using Mantine DataTable")[![Image 4: EasyWP is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/easywp-light.svg)![Image 5: EasyWP is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/easywp-dark.svg)](https://www.easywp.com/ "EasyWP is using Mantine DataTable")[![Image 6: LeasingSH.ro is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/leasingsh-ro-light.png)![Image 7: LeasingSH.ro is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/leasingsh-ro-dark.png)](https://leasingsh.ro/ "LeasingSH.ro is using Mantine DataTable")[![Image 8: CodeParrot.AI is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/codeparrot.svg) CodeParrot.AI](https://codeparrot.ai/ "CodeParrot.AI is using Mantine DataTable")[![Image 9: OmicsStudio is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/omicsstudio-light.svg)![Image 10: OmicsStudio is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/omicsstudio-dark.svg)](https://omicsstudio.com/ "OmicsStudio is using Mantine DataTable")[![Image 11: SegmentX is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/segmentx.png) SegmentX](https://segmentx.ai/ "SegmentX is using Mantine DataTable")[![Image 12: Aquarino is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/aquarino.svg)](http://aquarino.com.br/ "Aquarino is using Mantine DataTable")[![Image 13: Dera is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/dera.webp) Dera](https://getdera.com/ "Dera is using Mantine DataTable")[![Image 14: kappa.ai is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/kapa-light.png)![Image 15: kappa.ai is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/kapa-dark.png)](https://kapa.ai/ "kappa.ai is using Mantine DataTable")[![Image 16: exdatis is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/exdatis-light.svg)![Image 17: exdatis is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/exdatis-dark.svg)](https://exdatis.ai/ "exdatis is using Mantine DataTable")[![Image 18: teachfloor is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/teachfloor-light.svg)![Image 19: teachfloor is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/teachfloor-dark.svg)](https://www.teachfloor.com/ "teachfloor is using Mantine DataTable")[![Image 20: MARKUP is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/markup-light.png)![Image 21: MARKUP is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/markup-dark.png)](https://www.getmarkup.com/ "MARKUP is using Mantine DataTable")[![Image 22: InvenTree is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/inventree-light.png)![Image 23: InvenTree is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/inventree-dark.png)](https://inventree.org/ "InvenTree is using Mantine DataTable")[![Image 24: BookieBase is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/bookiebase-light.svg)![Image 25: BookieBase is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/bookiebase-dark.svg)](https://bookiebase.ie/ "BookieBase is using Mantine DataTable")[![Image 26: Zipline is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/zipline.png)](https://zipline.diced.sh/ "Zipline is using Mantine DataTable")[![Image 27: Pachtop is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/pachtop.png) Pachtop](https://pachtop.com/ "Pachtop is using Mantine DataTable")[![Image 28: Ganymede is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/ganymede.png) Ganymede](https://github.com/Zibbp/ganymede "Ganymede is using Mantine DataTable")[![Image 29: Pipedash is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/pipedash.png) Pipedash](https://github.com/hcavarsan/pipedash "Pipedash is using Mantine DataTable")[![Image 30: COH3 Stats is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/coh3-stats.png) COH3 Stats](https://coh3stats.com/ "COH3 Stats is using Mantine DataTable")[![Image 31: ccrentals.org is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/ccrentals-light.svg)![Image 32: ccrentals.org is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/ccrentals-dark.svg) ccrentals.org](https://www.ccrentals.org/ "ccrentals.org is using Mantine DataTable")

[![Image 33: MIT License](https://img.shields.io/npm/l/mantine-datatable.svg?style=flat&color=1c7ed6)](https://github.com/icflorescu/mantine-datatable/blob/main/LICENSE)[![Image 34: Sponsor the author](https://img.shields.io/static/v1?label=github&message=sponsor&color=1c7ed6)](https://github.com/sponsors/icflorescu)

Built by [Ionut-Cristian Florescu](https://github.com/icflorescu) and [these awesome people](https://github.com/icflorescu/mantine-datatable/graphs/contributors).

Please [sponsor my work](https://github.com/sponsors/icflorescu) if you find it useful.

[![Image 35: GitHub Stars](https://img.shields.io/github/stars/icflorescu/mantine-datatable?style=flat&color=1c7ed6)](https://github.com/icflorescu/mantine-datatable)[![Image 36: NPM Downloads](https://img.shields.io/npm/dm/mantine-datatable.svg?style=flat&color=1c7ed6)](https://www.npmjs.com/package/mantine-datatable)
