# Source: https://www.mintlify.com/docs/components/columns.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.mintlify.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Columns

> Show elements side by side

The `Columns` component lets you group multiple `Card` components together. It's most often used to put cards in a grid, by specifying the number of grid columns. Columns are responsive and automatically adjust for smaller screens.

<Columns cols={2}>
  <Card title="Get started" icon="rocket">
    Set up your project with our quickstart guide.
  </Card>

  <Card title="API reference" icon="code">
    Explore endpoints, parameters, and examples for your API.
  </Card>
</Columns>

```mdx Columns example theme={null}
<Columns cols={2}>
  <Card title="Get started">
    Set up your project with our quickstart guide.
  </Card>
  <Card title="API reference">
    Explore endpoints, parameters, and examples for your API.
  </Card>
</Columns>
```

## Properties

<ResponseField name="cols" type="number" default={2}>
  The number of columns per row. Accepts values from 1 to 4.
</ResponseField>
