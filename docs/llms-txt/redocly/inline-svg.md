# Source: https://redocly.com/docs/realm/content/markdoc-tags/inline-svg.md

# Source: https://redocly.com/learn/markdoc/tags/inline-svg.md

# Inline SVG Tag [](/learn/markdoc/tags/tag-library#redocly-tag-badge)

The inline SVG tag is used to render and style an SVG image in your document.

## Syntax and usage

The `inline-svg` tag requires a `file` attribute, which provides a file path to an SVG file.

The following example embeds a Redocly logo from an svg file:


```
{% inline-svg file="./images/redocly-logo.svg" /%}
```

Before the SVG renders on the document, it's optimized using [SVGO](https://github.com/svg/svgo). The `id` attribute is also prefixed with the relative file path to avoid conflicts.

### Styling the SVG

SVGs can be styled using CSS rules added to your project, but you need a way to reference the SVG. There's two ways to add an identifier to the SVG:

1. Modify the HTML in the SVG file and add a class.
2. Apply a CSS class directly to the `inline-svg` tag, as in the following example:

```
{% inline-svg file="./images/redocly-logo.svg" .some-custom-class /%}
```


The second approach provides more flexibility to writers using the Markdoc tag.

## Attributes

| Attribute | Type | Description |
|  --- | --- | --- |
| `file` | string | Absolute or relative path to the svg file. |


## Examples

### Render SVG from file

The following example adds an inline SVG to your document:


```
{% inline-svg file="./images/ramen-icon.svg" /%}
```

### Apply styling to SVG

This example adds custom styling to change the size and color. The following CSS has been added to the `@theme/styles.css` file:


```css @theme/styles.css
.example-svg-styles {
    svg {
        width: 80px;
        height: auto;
    }

    path {
        fill: blue;
    }
}
```

The example below adds that class to the inline SVG:


```
{% inline-svg file="./images/ramen-icon.svg" .example-svg-styles /%}
```

## Best practices

You can improve page performance by using a single SVG file and applying styling changes using CSS. That way you don't have to load separate files.