# Source: https://www.courier.com/docs/platform/content/content-blocks/list-blocks.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List

> Courier List Blocks render dynamic arrays as styled lists across channels. Support includes simple, nested, and image-based lists. Configure using JSONPath, with scoped variables and conditional formatting.

List Blocks dynamically render arrays of data in your notifications. They're available across all channels and come in four types:

1. Simple list
2. List with children
3. List with images (email only)
4. List with children and images (email only)

## Working With List Blocks

**Availability:** All channels

<Frame caption="New List Block">
  <img src="https://mintcdn.com/courier-4f1f25dc/oLXFxRwf6FuGv1s3/assets/platform/content/list-block-new.png?fit=max&auto=format&n=oLXFxRwf6FuGv1s3&q=85&s=69b1a4c5438b249f81518cebffa1b240" alt="New List Block" width="1300" height="614" data-path="assets/platform/content/list-block-new.png" />
</Frame>

The repeatable list block allows you to easily display more complex layered data. This data is passed in the data object as an array during a send. The option to display an image differs by channel.

<Tip>
  The rendered output of a list block is an HTML table element. For more list customization options, use a [template block](/platform/content/content-blocks/template-blocks) with [Handlebars helpers](/platform/content/template-designer/handlebars-helpers).
</Tip>

<Frame caption="Simple List Block">
  <img src="https://mintcdn.com/courier-4f1f25dc/oLXFxRwf6FuGv1s3/assets/platform/content/list-block-simple.png?fit=max&auto=format&n=oLXFxRwf6FuGv1s3&q=85&s=040f2529ba0ba77a76872e4c73923eec" alt="Simple List Block" width="1524" height="700" data-path="assets/platform/content/list-block-simple.png" />
</Frame>

To switch from a simple list to numbered lists, add a list then open the list details:

<Frame caption="List Block Details">
  <img src="https://mintcdn.com/courier-4f1f25dc/oLXFxRwf6FuGv1s3/assets/platform/content/list-block-details.png?fit=max&auto=format&n=oLXFxRwf6FuGv1s3&q=85&s=fa02b9df4b2cfd040999544ec24e5544" alt="List Block Details" width="583" height="287" data-path="assets/platform/content/list-block-details.png" />
</Frame>

## Types of List Blocks

### Simple List

Displays a row for each item in the specified array, similar to a [text block](/platform/content/content-blocks/text-blocks) with variables scoped to the array.

To render a bulleted simple list, the background color for the list block must be set to `transparent`.

<Frame caption="List Block Background Color">
  <img src="https://mintcdn.com/courier-4f1f25dc/oLXFxRwf6FuGv1s3/assets/platform/content/list-bg-color.png?fit=max&auto=format&n=oLXFxRwf6FuGv1s3&q=85&s=630688d00b032426f1490755aae48204" alt="List Block Background Color" width="794" height="772" data-path="assets/platform/content/list-bg-color.png" />
</Frame>

<Frame caption="Rendered Bulleted List">
  <img src="https://mintcdn.com/courier-4f1f25dc/oLXFxRwf6FuGv1s3/assets/platform/content/list-bullet.png?fit=max&auto=format&n=oLXFxRwf6FuGv1s3&q=85&s=16e5fb6fe17213436b2674aef50d8f5f" alt="Rendered Bulleted List" width="1038" height="544" data-path="assets/platform/content/list-bullet.png" />
</Frame>

### List With Children

Similar to a simple list, but includes child rows for nested array data.

### List With Images

<Note>
  Available for email channels only. Other channels display as a list with children.
</Note>

Includes images alongside list items. Images can be linked and customized using variables.

### List With Children and Images

Combines features of lists with children and lists with images, allowing for complex, hierarchical data representation with visual elements.

## Configuring List Blocks

### Path

Set the JSONPath expression to point to the array you want to display. For example:

```json  theme={null}
{
  "data": {
    "trainers": [ "Ash", "Misty", "Brock"],
    "name": "Ash Ketchum",
    "region": "Kanto",
    "pokemon": [
      {
        "name": "Bulbasaur",
        "image": "https://example.com/001.png",
        "types": [
          { "name": "grass", "image": "https://example.com/grass.png" },
          { "name": "poison", "image": "https://example.com/poison.png" }
        ]
      },
      {
        "name": "Ivysaur",
        "image": "https://example.com/002.png",
        "types": [
          { "name": "grass", "image": "https://example.com/grass.png" },
          { "name": "poison", "image": "https://example.com/poison.png" }
        ]
      },
      {
        "name": "Venusaur",
        "image": "https://example.com/003.png",
        "types": [
          { "name": "grass", "image": "https://example.com/grass.png" },
          { "name": "poison", "image": "https://example.com/poison.png" }
        ]
      }
    ],
  }
}
```

To list all Pokemon, set the path to `pokemon`.

### Data References

* Inside path scope: Use `{propertyName}` to reference each item in the array
  * e.g. to display the name of the Pokemon, if the path is set to `pokemon`, you can use the variable `{name}`.
* Outside path scope: Use `{$.data.propertyName}` or `{propertyName}` if there isn't a property name conflict.
  * e.g. to display the top level `name` (Ash Ketchum), you can use the variable `{$.data.name}`.
  * e.g. to display the region, you can use the variable `{region}`.
* Array of strings: Use `{@}` to reference each item
  * e.g. to display each trainer in the `trainers` array, you can use the variable `{@}`.

### Styling

* Switch between bulleted and numbered lists in the list details
* Set background color for supported channels using the color picker

<Frame caption="List Block Configuration Details">
  <img src="https://mintcdn.com/courier-4f1f25dc/oLXFxRwf6FuGv1s3/assets/platform/content/list-block-details.png?fit=max&auto=format&n=oLXFxRwf6FuGv1s3&q=85&s=fa02b9df4b2cfd040999544ec24e5544" alt="List Block Configuration Details" width="583" height="287" data-path="assets/platform/content/list-block-details.png" />
</Frame>

<CardGroup cols={2}>
  <Card title="Content Block Basics" href="/platform/content/content-blocks/content-block-basics" icon="cube">
    Adding, reordering, and filtering blocks
  </Card>

  <Card title="Template Blocks" href="/platform/content/content-blocks/template-blocks" icon="code">
    Custom HTML for advanced list rendering
  </Card>

  <Card title="Handlebars Helpers" href="/platform/content/template-designer/handlebars-helpers" icon="bicycle">
    Loop helpers for dynamic list content
  </Card>

  <Card title="Variables" href="/platform/content/variables/inserting-variables" icon="brackets-curly">
    JSONPath expressions for list data
  </Card>
</CardGroup>
