# Source: https://www.mintlify.com/docs/components/icons.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.mintlify.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Icons

> Use icons from popular libraries, external URLs, or files in your project.

Use icons from Font Awesome, Lucide, SVGs, external URLs, or files in your project to enhance your documentation.

<Icon icon="flag" size={32} />

```mdx Icon example theme={null}
<Icon icon="flag" size={32} />
```

## Inline icons

Icons are placed inline when used within a sentence, paragraph, or heading. <Icon icon="flag" iconType="solid" /> Use icons for decoration or to add visual emphasis.

```markdown Inline icon example theme={null}
Icons are placed inline when used within a sentence, paragraph, or heading. <Icon icon="flag" iconType="solid" /> Use icons for decoration or to add visual emphasis.
```

## Properties

<ResponseField name="icon" type="string" required>
  The icon to display.

  Options:

  * [Font Awesome icon](https://fontawesome.com/icons) name, if you have the `icons.library` [property](/organize/settings#param-icons) set to `fontawesome` in your `docs.json`
  * [Lucide icon](https://lucide.dev/icons) name, if you have the `icons.library` [property](/organize/settings#param-icons) set to `lucide` in your `docs.json`
  * URL to an externally hosted icon
  * Path to an icon file in your project
</ResponseField>

<ResponseField name="iconType" type="string">
  The [Font Awesome](https://fontawesome.com/icons) icon style. Only used with Font Awesome icons.

  Options: `regular`, `solid`, `light`, `thin`, `sharp-solid`, `duotone`, `brands`.
</ResponseField>

<ResponseField name="color" type="string">
  The color of the icon as a hex code (for example, `#FF5733`).
</ResponseField>

<ResponseField name="size" type="number">
  The size of the icon in pixels.
</ResponseField>

<ResponseField name="className" type="string">
  Custom CSS class name to apply to the icon.
</ResponseField>
