# Source: https://docs.frigade.com/sdk/styling/css-overrides.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.frigade.com/llms.txt
> Use this file to discover all available pages before exploring further.

# CSS Overrides

## CSS Prop

We use [Emotion's css prop](https://emotion.sh/docs/css-prop#use-the-css-prop) under the hood in our components. You can pass a `css` object in at the top level of any of our components to create scoped styles for that specific instance of that component.

Since the `css` prop is scoped to each component, you can treat it as though it were a `style` prop with added functionality. For example:

```tsx  theme={"system"}
// This CSS will be compiled at runtime by Emotion and applied to
// the `.fr-card` wrapper at the top level of the Card component

<Frigade.Card
  css={{
    backgroundColor: "goldenrod",
  }}
/>
```

## Styling sub-components

We also assign stable class names to each internal part of each component, to make style overrides as easy as:

```tsx  theme={"system"}
<Frigade.Tour
  css={{
    ".fr-tooltip-content .fr-tooltip-close": {
      backgroundColor: "pink",
    },
    ".fr-button-primary": {
      backgroundColor: "fuchsia",
    },
  }}

  {...}
/>
```

To find the stable class names for any given component, you can either:

1. Inspect the component in your browser's dev tools and look for classes prefixed with `fr-`
2. [View the source](https://github.com/FrigadeHQ/javascript/tree/main/packages/react/src/components) for the component and use the value of the `part` prop (class name will always be `fr-${part}`)

## Global overrides

If you want to style every instance of a Frigade component (or write any other general CSS), the `<Frigade.Provider />` component also accepts a `css` prop. It writes global CSS into the document, so use it with caution.

Since every Frigade Component has its own stable classname, you can override every `<Button.Primary />` simply by writing CSS in object syntax:

```tsx  theme={"system"}
<Frigade.Provider
  css={{
    ".fr-button-primary": {
      backgroundColor: "aquamarine",

      "&:hover": {
        backgroundColor: "honeydew",
      },
    },
  }}

  {...}
/>
```

To override the styles for every Frigade Button, use a [wildcard attribute selector](https://developer.mozilla.org/en-US/docs/Web/CSS/Attribute_selectors):

```tsx  theme={"system"}
<Frigade.Provider
  css={{
    "[class*='fr-button']": {
      backgroundColor: "maroon",

      "&:hover": {
        backgroundColor: "cornsilk",
      },
    },
  }}

  {...}
/>
```

## Overriding CSS from the Flow editor

You can override the `css` prop or any other attribute from the Flow editor by providing the `props` field in the Advanced YAML editor:

```yaml  theme={"system"}
props:
  css:
    backgroundColor: "blue"
    ".fr-button-primary":
      backgroundColor: "chartreuse"
steps: ...
```

You can also override the styling on specific Steps by providing the `props` field on the given Step. This will override the styling for that specific Step only:

```yaml  theme={"system"}
steps:
  - id: step-1
    props:
      css:
        ".fr-button-primary":
          backgroundColor: "chartreuse"
```

## External CSS

If you prefer to use your own CSS workflow, any old CSS will work. You can provide a top-level `className` prop to a component via a static stylesheet, CSS Modules, etc. then scope your styles to that:

```jsx  theme={"system"}
<Frigade.Tour className="my-scoped-component" {...} />
```

```css  theme={"system"}
.my-scoped-component {
  & .fr-button-primary {
    backgroundcolor: "chartreuse";
  }
}
```

Note: If you use external CSS to target `.fr-` classnames, your CSS must be source-ordered *after* Frigade's CSS in order to properly override the built-in Component styles.

If you don't have control over source-ordering in your app, you can increase the specificity of your selectors instead:

```css  theme={"system"}
body :is(.fr-title) {
  font-size: 42px;
}
```

## Tailwind

You can use Tailwind's [arbitrary variants](https://tailwindcss.com/docs/hover-focus-and-other-states#using-arbitrary-variants) to style the inner sub-components of a Frigade component:

```jsx  theme={"system"}
<Frigade.Banner className="[&_.fr-title]:text-fuchsia-500" {...} />
```
