# Source: https://icflorescu.github.io/mantine-datatable/examples/expanding-rows/

Title: Examples › Expanding rows | Mantine DataTable

URL Source: https://icflorescu.github.io/mantine-datatable/examples/expanding-rows/

Markdown Content:
Examples › Expanding rows | Mantine DataTable
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

Examples › Expanding rows
-------------------------

The `rowExpansion` property allows you to define the _“row expansion”_ behavior of the DataTable.

### [Basic usage](https://icflorescu.github.io/mantine-datatable/examples/expanding-rows/)

In its most basic usage scenario, the feature only requires specifying the content to be _lazily rendered_ when a row is expanded.

Heads up

Styling the expanded content falls within your responsibility.

Don’t forget to set the `idAccessor` property if your unique record key is not`'id'`.

See [non-standard record IDs](https://icflorescu.github.io/mantine-datatable/examples/non-standard-record-ids/) for more info.

RowExpansionExampleSimple.tsx RowExpansionExampleSimple.module.css

```
return (
  <DataTable
    withTableBorder
    withColumnBorders
    columns={[{ accessor: 'name' }, { accessor: 'city' }, { accessor: 'state' }]}
    records={records}
    rowExpansion={{
      content: ({ record }) => (
        <Stack className={classes.details} p="xs" gap={6}>
          <Group gap={6}>
            <div className={classes.label}>Postal address:</div>
            <div>
              {record.streetAddress}, {record.city}, {record.state}
            </div>
          </Group>
          <Group gap={6}>
            <div className={classes.label}>Mission statement:</div>
            <Box fs="italic">“{record.missionStatement}”</Box>
          </Group>
        </Stack>
      ),
    }}
  />
);
```

Expand code

Click on a row to test the behavior:

| Name | City | State |
| --- | --- | --- |
| Feest, Bogan and Herzog | Stromanport | WY |
| Cummerata - Kuhlman | South Gate | NH |
| Goyette Inc | Dorthyside | ID |
| Runte Inc | McAllen | MA |
| Goldner, Rohan and Lehner | North Louie | WY |

No records

### [Specifying collapse properties](https://icflorescu.github.io/mantine-datatable/examples/expanding-rows/)

Internally, the expanded content is rendered inside a Mantine[Collapse](https://mantine.dev/core/collapse/) component. You can customize the underlying Collapse component like so:

| Name | City | State |
| --- | --- | --- |
| Feest, Bogan and Herzog | Stromanport | WY |
| Cummerata - Kuhlman | South Gate | NH |
| Goyette Inc | Dorthyside | ID |
| Runte Inc | McAllen | MA |
| Goldner, Rohan and Lehner | North Louie | WY |

No records

Here is the code for the above example:

```
return (
  <DataTable
    // ...
    rowExpansion={{
      collapseProps: {
        transitionDuration: 500,
        animateOpacity: false,
        transitionTimingFunction: 'ease-out',
      },
      // ...
    }}
  />
);
```

Expand code

### [Allowing multiple rows to be expanded at once](https://icflorescu.github.io/mantine-datatable/examples/expanding-rows/)

By default, a single row can be expanded at a certain time. You can override the default behavior like so:

| Name | City | State |
| --- | --- | --- |
| Feest, Bogan and Herzog | Stromanport | WY |
| Cummerata - Kuhlman | South Gate | NH |
| Goyette Inc | Dorthyside | ID |
| Runte Inc | McAllen | MA |
| Goldner, Rohan and Lehner | North Louie | WY |

No records

Here is the code for the above example:

```
return (
  <DataTable
    withTableBorder
    withColumnBorders
    columns={[{ accessor: 'name' }, { accessor: 'city' }, { accessor: 'state' }]}
    records={records}
    rowExpansion={{
      allowMultiple: true, // 👈 allow multiple rows to be expanded at the same time
      // ...
    }}
  />
);
```

Expand code

### [Specifying which rows are expandable](https://icflorescu.github.io/mantine-datatable/examples/expanding-rows/)

You can specify which rows are expandable like so:

| Name | City | State |
| --- | --- | --- |
| Feest, Bogan and Herzog | Stromanport | WY |
| Cummerata - Kuhlman | South Gate | NH |
| Goyette Inc | Dorthyside | ID |
| Runte Inc | McAllen | MA |
| Goldner, Rohan and Lehner | North Louie | WY |

No records

Here is the code for the above example:

```
return (
  <DataTable
    withTableBorder
    withColumnBorders
    columns={[{ accessor: 'name' }, { accessor: 'city' }, { accessor: 'state' }]}
    records={records}
    rowExpansion={{
      allowMultiple: true,
      expandable: ({ record: { state } }) => state === 'WY', // 👈 enable expansion only on rows where state is WY
      // ...
    }}
  />
);
```

Expand code

### [Specifying which rows are initially expanded](https://icflorescu.github.io/mantine-datatable/examples/expanding-rows/)

You can specify which rows are initially expanded like so:

| Name | City | State |
| --- | --- | --- |
| Feest, Bogan and Herzog | Stromanport | WY |
|  |
| Postal address: 21716 Ratke Drive, Stromanport, WY Mission statement: “Innovate bricks-and-clicks metrics.” |
| Cummerata - Kuhlman | South Gate | NH |
| Goyette Inc | Dorthyside | ID |
| Runte Inc | McAllen | MA |
| Goldner, Rohan and Lehner | North Louie | WY |
|  |
| Postal address: 632 Broadway Avenue, North Louie, WY Mission statement: “Incubate cross-platform metrics.” |

No records

Here is the code for the above example:

```
return (
  <DataTable
    withTableBorder
    withColumnBorders
    columns={[{ accessor: 'name' }, { accessor: 'city' }, { accessor: 'state' }]}
    records={records}
    rowExpansion={{
      allowMultiple: true,
      initiallyExpanded: ({ record: { state } }) => state === 'WY', // 👈 expand rows where state is WY
      // ...
    }}
  />
);
```

Expand code

### [Always expand all rows](https://icflorescu.github.io/mantine-datatable/examples/expanding-rows/)

If you want all rows to be locked in their expanded state, just set the row expansion `trigger`property to `'always'`:

| Name | City | State |
| --- | --- | --- |
| Feest, Bogan and Herzog | Stromanport | WY |
|  |
| Postal address: 21716 Ratke Drive, Stromanport, WY Mission statement: “Innovate bricks-and-clicks metrics.” |
| Cummerata - Kuhlman | South Gate | NH |
|  |
| Postal address: 6389 Dicki Stream, South Gate, NH Mission statement: “Harness real-time channels.” |
| Goyette Inc | Dorthyside | ID |
|  |
| Postal address: 8873 Mertz Rapid, Dorthyside, ID Mission statement: “Productize front-end web services.” |
| Runte Inc | McAllen | MA |
|  |
| Postal address: 2996 Ronny Mount, McAllen, MA Mission statement: “Engage synergistic infrastructures.” |
| Goldner, Rohan and Lehner | North Louie | WY |
|  |
| Postal address: 632 Broadway Avenue, North Louie, WY Mission statement: “Incubate cross-platform metrics.” |

No records

Here is the code for the above example:

```
return (
  <DataTable
    withTableBorder
    withColumnBorders
    columns={[{ accessor: 'name' }, { accessor: 'city' }, { accessor: 'state' }]}
    records={records}
    rowExpansion={{
      trigger: 'always', // 👈 always expand all rows
      // ...
    }}
  />
);
```

Expand code

### [Using collapse() function in row expansion content](https://icflorescu.github.io/mantine-datatable/examples/expanding-rows/)

Besides the current record, the `content` function also receives a `collapse` callback that could be used, for instance, in an inline editor like so:

| Name | City | State |
| --- | --- | --- |
| Feest, Bogan and Herzog | Stromanport | WY |
| Cummerata - Kuhlman | South Gate | NH |
| Goyette Inc | Dorthyside | ID |
| Runte Inc | McAllen | MA |
| Goldner, Rohan and Lehner | North Louie | WY |

No records

Here is the code for the above example:

```
type CompanyEditorProps = {
  initialData: Company;
  onDone: (data: Company) => void;
  onCancel: () => void;
};

function CompanyEditor({ initialData, onDone, onCancel }: CompanyEditorProps) {
  const [name, setName] = useState(initialData.name);
  const [city, setCity] = useState(initialData.city);
  const [state, setState] = useState(initialData.state);
  const [streetAddress, setStreetAddress] = useState(initialData.streetAddress);
  const [missionStatement, setMissionStatement] = useState(initialData.missionStatement);

  return (
    <Box className={classes.details} p="md">
      <Grid>
        <GridCol span={{ base: 12, xs: 6 }}>
          <TextInput label="Name" size="xs" value={name} onChange={(e) => setName(e.currentTarget.value)} />
        </GridCol>
        {/* other fields... */}
        <Grid.Col span={12}>
          <Group justify="center">
            <Button variant="default" size="xs" leftSection={<IconArrowBackUp size={16} />} onClick={() => onCancel()}>
              Cancel
            </Button>
            <Button
              size="xs"
              leftSection={<IconCheck size={16} />}
              onClick={() =>
                onDone({
                  ...initialData,
                  name: name.trim(),
                  city: city.trim(),
                  state: state.trim(),
                  streetAddress: streetAddress.trim(),
                  missionStatement: missionStatement.trim(),
                })
              }
            >
              Save
            </Button>
          </Group>
        </Grid.Col>
      </Grid>
    </Box>
  );
}

export function RowExpansionExampleWithInlineEditor() {
  const [companies, setCompanies] = useState(initialRecords);
  return (
    <DataTable
      withTableBorder
      withColumnBorders
      columns={[{ accessor: 'name' }, { accessor: 'city' }, { accessor: 'state' }]}
      records={companies}
      rowExpansion={{
        content: ({ record, collapse }) => (
          <CompanyEditor
            initialData={record}
            onDone={(data) => {
              const index = companies.findIndex((c) => c.id === data.id);
              setCompanies([...companies.slice(0, index), data, ...companies.slice(index + 1)]);
              collapse(); // 👈 collapse the row after editing
            }}
            onCancel={collapse} // 👈 collapse the row if editing is cancelled
          />
        ),
      }}
    />
  );
}
```

Expand code

### [Lazy-loading row expansion data](https://icflorescu.github.io/mantine-datatable/examples/expanding-rows/)

As mentioned above, the `content` function is _lazily executed_ when a row is expanded to prevent creating unnecessary DOM elements.

If your row expansion content needs to show data that comes from outside the table `records`, you could exploit this behavior to lazy-load it only when a row is expanded:

| Name | City | State |
| --- | --- | --- |
| Feest, Bogan and Herzog | Stromanport | WY |
| Cummerata - Kuhlman | South Gate | NH |
| Goyette Inc | Dorthyside | ID |
| Runte Inc | McAllen | MA |
| Goldner, Rohan and Lehner | North Louie | WY |

No records

Here is the code for the above example:

```
function CompanyDetails({ companyId }: { companyId: string }) {
  const isMounted = useIsMounted();
  const [loading, setLoading] = useState(true);
  const [numberOfDepartments, setNumberOfDepartments] = useState<number | null>(null);
  const [numberOfEmployees, setNumberOfEmployees] = useState<number | null>(null);

  useEffect(() => {
    // simulate expensive async loading operation
    (async () => {
      setLoading(true);
      const delay = { min: 800, max: 1200 };
      const [departments, employees] = await Promise.all([
        countCompanyDepartmentsAsync({ companyId, delay }),
        countCompanyEmployeesAsync({ companyId, delay }),
      ]);
      if (isMounted()) {
        setNumberOfDepartments(departments);
        setNumberOfEmployees(employees);
        setLoading(false);
      }
    })();
  }, [companyId, isMounted]);

  return (
    <Center className={classes.details} p="sm">
      <Stack gap={6}>
        <LoadingOverlay visible={loading} />
        <Group gap={6}>
          <Box className={classes.label}>Number of departments:</Box>
          <Box className={classes.number} ta="right">
            {numberOfDepartments ?? 'loading...'}
          </Box>
        </Group>
        <Group gap={6}>
          <Box className={classes.label}>Number of employees:</Box>
          <Box className={classes.number} ta="right">
            {numberOfEmployees ?? 'loading...'}
          </Box>
        </Group>
      </Stack>
    </Center>
  );
}

export function RowExpansionExampleWithLazyLoading() {
  return (
    <DataTable
      withTableBorder
      withColumnBorders
      columns={[{ accessor: 'name' }, { accessor: 'city' }, { accessor: 'state' }]}
      records={records}
      rowExpansion={{ content: ({ record }) => <CompanyDetails companyId={record.id} /> }}
    />
  );
}
```

Expand code

### [Controlled mode](https://icflorescu.github.io/mantine-datatable/examples/expanding-rows/)

You can control the row expansion feature by pointing the `rowExpansion`/`expanded`property to an object containing:

*   `recordIds` → an array containing the currently expanded record IDs
*   `onRecordIdsChange` → a callback function that gets called when the currently expanded records change

When using the row expansion feature in controlled mode, if you want to prevent the default behavior of toggling the expansion state on click, set the `rowExpansion`/`trigger` property to`'never'`.

Expand first and third row Expand second and fourth row Collapse all rows

| # | Name | City | State |
| --- | --- | --- | --- |
| 1 | Feest, Bogan and Herzog | Stromanport | WY |
| 2 | Cummerata - Kuhlman | South Gate | NH |
| 3 | Goyette Inc | Dorthyside | ID |
| 4 | Runte Inc | McAllen | MA |
| 5 | Goldner, Rohan and Lehner | North Louie | WY |

No records

Here is the code for the above example:

```
const [expandedRecordIds, setExpandedRecordIds] = useState<string[]>([]);

const expandFirstAndThirdRow = () => {
  setExpandedRecordIds([firstRowId, thirdRowId]);
};

const expandSecondAndFourthRow = () => {
  setExpandedRecordIds([secondRowId, fourthRowId]);
};

const collapseAllRows = () => {
  setExpandedRecordIds([]);
};

return (
  <>
    {/* buttons triggering the above callbacks... */}
    <DataTable
      mt="md"
      withTableBorder
      withColumnBorders
      columns={[
        { accessor: 'number', title: '#', render: (_, index) => index + 1 },
        { accessor: 'name', width: '100%' },
        { accessor: 'city', ellipsis: true },
        { accessor: 'state' },
      ]}
      records={records}
      rowExpansion={{
        // trigger: 'never', // 👈 uncomment this if you want to disable expanding/collapsing on click
        allowMultiple: true,
        expanded: {
          recordIds: expandedRecordIds,
          onRecordIdsChange: setExpandedRecordIds,
        },
        content: ({ record }) => (
          // expansion content...
        ),
      }}
    />
  </>
);
```

Expand code

If you need to combine the row expansion behavior with links, buttons,[row action cells](https://icflorescu.github.io/mantine-datatable/examples/row-actions-cell/) or any kind of clickable components inside cells, make sure to intercept the `click` event on those components and[invoke its `.stopPropagation()` method](https://developer.mozilla.org/en-US/docs/Web/API/Event/stopPropagation).

See [this example](https://icflorescu.github.io/mantine-datatable/examples/links-or-buttons-inside-clickable-rows-or-cells/) for more information.

Head over to the [next example](https://icflorescu.github.io/mantine-datatable/examples/nested-tables/) to see how you can abuse the row expansion feature to display nested tables.

[Go back Examples › Using with Mantine ContextMenu](https://icflorescu.github.io/mantine-datatable/examples/using-with-mantine-contextmenu/)[Up next Examples › Nested tables](https://icflorescu.github.io/mantine-datatable/examples/nested-tables/)

Mantine DataTable is used and trusted by
----------------------------------------

[![Image 1: Microsoft is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/microsoft.svg)](https://www.microsoft.com/ "Microsoft is using Mantine DataTable")[![Image 2: Namecheap is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/namecheap-light.svg)![Image 3: Namecheap is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/namecheap-dark.svg)](https://www.namecheap.com/ "Namecheap is using Mantine DataTable")[![Image 4: EasyWP is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/easywp-light.svg)![Image 5: EasyWP is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/easywp-dark.svg)](https://www.easywp.com/ "EasyWP is using Mantine DataTable")[![Image 6: LeasingSH.ro is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/leasingsh-ro-light.png)![Image 7: LeasingSH.ro is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/leasingsh-ro-dark.png)](https://leasingsh.ro/ "LeasingSH.ro is using Mantine DataTable")[![Image 8: CodeParrot.AI is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/codeparrot.svg) CodeParrot.AI](https://codeparrot.ai/ "CodeParrot.AI is using Mantine DataTable")[![Image 9: OmicsStudio is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/omicsstudio-light.svg)![Image 10: OmicsStudio is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/omicsstudio-dark.svg)](https://omicsstudio.com/ "OmicsStudio is using Mantine DataTable")[![Image 11: SegmentX is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/segmentx.png) SegmentX](https://segmentx.ai/ "SegmentX is using Mantine DataTable")[![Image 12: Aquarino is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/aquarino.svg)](http://aquarino.com.br/ "Aquarino is using Mantine DataTable")[![Image 13: Dera is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/dera.webp) Dera](https://getdera.com/ "Dera is using Mantine DataTable")[![Image 14: kappa.ai is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/kapa-light.png)![Image 15: kappa.ai is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/kapa-dark.png)](https://kapa.ai/ "kappa.ai is using Mantine DataTable")[![Image 16: exdatis is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/exdatis-light.svg)![Image 17: exdatis is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/exdatis-dark.svg)](https://exdatis.ai/ "exdatis is using Mantine DataTable")[![Image 18: teachfloor is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/teachfloor-light.svg)![Image 19: teachfloor is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/teachfloor-dark.svg)](https://www.teachfloor.com/ "teachfloor is using Mantine DataTable")[![Image 20: MARKUP is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/markup-light.png)![Image 21: MARKUP is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/markup-dark.png)](https://www.getmarkup.com/ "MARKUP is using Mantine DataTable")[![Image 22: InvenTree is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/inventree-light.png)![Image 23: InvenTree is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/inventree-dark.png)](https://inventree.org/ "InvenTree is using Mantine DataTable")[![Image 24: BookieBase is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/bookiebase-light.svg)![Image 25: BookieBase is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/bookiebase-dark.svg)](https://bookiebase.ie/ "BookieBase is using Mantine DataTable")[![Image 26: Zipline is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/zipline.png)](https://zipline.diced.sh/ "Zipline is using Mantine DataTable")[![Image 27: Pachtop is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/pachtop.png) Pachtop](https://pachtop.com/ "Pachtop is using Mantine DataTable")[![Image 28: Ganymede is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/ganymede.png) Ganymede](https://github.com/Zibbp/ganymede "Ganymede is using Mantine DataTable")[![Image 29: Pipedash is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/pipedash.png) Pipedash](https://github.com/hcavarsan/pipedash "Pipedash is using Mantine DataTable")[![Image 30: COH3 Stats is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/coh3-stats.png) COH3 Stats](https://coh3stats.com/ "COH3 Stats is using Mantine DataTable")[![Image 31: ccrentals.org is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/ccrentals-light.svg)![Image 32: ccrentals.org is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/ccrentals-dark.svg) ccrentals.org](https://www.ccrentals.org/ "ccrentals.org is using Mantine DataTable")

[![Image 33: MIT License](https://img.shields.io/npm/l/mantine-datatable.svg?style=flat&color=1c7ed6)](https://github.com/icflorescu/mantine-datatable/blob/main/LICENSE)[![Image 34: Sponsor the author](https://img.shields.io/static/v1?label=github&message=sponsor&color=1c7ed6)](https://github.com/sponsors/icflorescu)

Built by [Ionut-Cristian Florescu](https://github.com/icflorescu) and[these awesome people](https://github.com/icflorescu/mantine-datatable/graphs/contributors).

Please [sponsor my work](https://github.com/sponsors/icflorescu) if you find it useful.

[![Image 35: GitHub Stars](https://img.shields.io/github/stars/icflorescu/mantine-datatable?style=flat&color=1c7ed6)](https://github.com/icflorescu/mantine-datatable)[![Image 36: NPM Downloads](https://img.shields.io/npm/dm/mantine-datatable.svg?style=flat&color=1c7ed6)](https://www.npmjs.com/package/mantine-datatable)
