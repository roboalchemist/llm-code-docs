# Source: https://docs.xano.com/the-function-stack/filters.md

# Source: https://docs.xano.com/building/logic/core-components/filters.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Filters

> Use filters to manipulate data throughout your logic

Filters are used to manipulate data throughout your logic. They can be applied almost anywhere that data is generated or referenced; anything from creating a variable to manipulating the response object on the fly.

## Adding Filters

<Tabs>
  <Tab title="Visually" icon="eye">
    Hover over a value box and click **Add Filter.**

    <Frame>    <img src="https://mintcdn.com/xano-997cb9ee/bCVIC1Tg3ccBy86J/images/filters-20251013-114317.png?fit=max&auto=format&n=bCVIC1Tg3ccBy86J&q=85&s=1faa3dbc3d086bae2f7cbf9d22901943" alt="filters-20251013-114317" width="663" height="335" data-path="images/filters-20251013-114317.png" /></Frame>

    You can search for filters using the search bar, navigate using the categories, or scroll through the list.

    <Frame>    <img src="https://mintcdn.com/xano-997cb9ee/bCVIC1Tg3ccBy86J/images/filters-20251013-114406.png?fit=max&auto=format&n=bCVIC1Tg3ccBy86J&q=85&s=cb33ed3270a0b9578ec7b86a47fd360e" alt="filters-20251013-114406" width="483" height="842" data-path="images/filters-20251013-114406.png" /></Frame>

    Filters will have various options available depending on the filter chosen, so it's best to consult that filter's specific documentation for more information.

    <Frame>    <img src="https://mintcdn.com/xano-997cb9ee/bCVIC1Tg3ccBy86J/images/filters-20251013-114506.png?fit=max&auto=format&n=bCVIC1Tg3ccBy86J&q=85&s=8b0b33059922cd10926a8ef76e2f06f7" alt="filters-20251013-114506" width="489" height="724" data-path="images/filters-20251013-114506.png" /></Frame>

    Hover over an existing filter to see some additional actions.

    <Frame>    <img src="https://mintcdn.com/xano-997cb9ee/bCVIC1Tg3ccBy86J/images/filters-20251013-123331.png?fit=max&auto=format&n=bCVIC1Tg3ccBy86J&q=85&s=6621714a9d4471ad9bbd3ca47f39eea3" alt="filters-20251013-123331" width="436" height="527" data-path="images/filters-20251013-123331.png" /></Frame>

    |                                                     | Action                                                                    |
    | --------------------------------------------------- | ------------------------------------------------------------------------- |
    | <Icon icon="arrows-up-down-left-right" size={18} /> | Click and drag to reorder filters.                                        |
    | <Icon icon="eye" size={18} />                       | Click to disable the filter. Upon execution, this filter will be skipped. |
    | <Icon icon="copy" size={18} />                      | Click to clone the filter.                                                |
    | <Icon icon="x" size={18} />                         | Click to delete the filter.                                               |

    You can nest filters by adding them to an existing filter's value box(es).

    <Frame caption="An example of a nested filter">    <img src="https://mintcdn.com/xano-997cb9ee/bCVIC1Tg3ccBy86J/images/filters-20251013-124131.png?fit=max&auto=format&n=bCVIC1Tg3ccBy86J&q=85&s=d29933edfdff0d4b15876e0c80c4cefa" alt="filters-20251013-124131" width="485" height="689" data-path="images/filters-20251013-124131.png" /></Frame>
  </Tab>

  <Tab title="XanoScript" icon="code">
    Filters are defined immediately after the target value using the `|` pipe character.

    ```javascript lines icon="code" Filter syntax format theme={null}
    <data>|<filter_name>:<filter_option_1>:<filter_option_2>
    ```

    You can also nest filters by adding them to an existing filter's values in parantheses.

    ```javascript lines icon="code" Nested filter syntax format theme={null}
    <data>|(<filter_name>:<filter_option_1>:<filter_option_2>)|<filter_name>
    ```
  </Tab>
</Tabs>

## Filter Reference

Review all available filters below by selecting the section you're interested in.

<Columns col={2}>
  <Card title="Manipulation" icon="wand-magic-sparkles" href="/the-function-stack/filters/manipulation">
    Transform or traverse data using conditional or object-based filters.
  </Card>

  <Card title="Math" icon="calculator" href="/the-function-stack/filters/math">
    Perform arithmetic operations.
  </Card>

  <Card title="Timestamp" icon="clock" href="/the-function-stack/filters/timestamp">
    Convert or adjust timestamps.
  </Card>

  <Card title="Text" icon="font" href="/the-function-stack/filters/text">
    Trim, format, or modify text.
  </Card>

  <Card title="Array" icon="list-ul" href="/the-function-stack/filters/array">
    Add, remove, or manipulate array items.
  </Card>

  <Card title="Transform" icon="shuffle" href="/the-function-stack/filters/transform">
    Convert data between types or formats.
  </Card>

  <Card title="Comparison" icon="scale-balanced" href="/the-function-stack/filters/comparison">
    Compare values for equality or other conditions.
  </Card>

  <Card title="Security" icon="shield-halved" href="/the-function-stack/filters/security">
    Encrypt, validate, or secure data.
  </Card>
</Columns>


Built with [Mintlify](https://mintlify.com).