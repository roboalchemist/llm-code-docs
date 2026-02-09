# Source: https://docs.frigade.com/sdk/styling/theming.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.frigade.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Theming

The easiest way to get Frigade components integrated into your designs is by customizing the base theme that all of our components inherit from.

The base theme covers common style properties like colors, typography, spacing, and borders. If you need deeper customization, you can dig into CSS overrides or even custom components.

To override the base theme, pass the properties you want to change into the `theme` prop of the `Provider` component. In the example below we override the default blue primary color to be `#000000`:

```tsx  theme={"system"}
<Frigade.Provider
  apiKey="..."
  theme={{
    colors: {
      "primary": {
        "background": "#000000",
        "border": "#000000",
        "surface": "#000000",
      }
    }
  }}
/>
```

## Tailwind CSS and Shadcn

If you're using Tailwind CSS with Shadcn, you can use the `theme` mappings below to automatically match your existing theme.

```tsx  theme={"system"}
<Frigade.Provider
  apiKey="..."
  theme={{
    colors: {
      primary: {
        foreground: 'hsl(var(--primary-foreground))',
        background: 'hsl(var(--primary))',
        surface: 'hsl(var(--primary))',
        border: 'hsl(var(--primary))',
        hover: {
          background: 'hsl(var(--primary) / 0.9)',
          surface: 'hsl(var(--primary) / 0.9)',
          border: 'hsl(var(--primary) / 0.9)',
        },
      },
      secondary: {
        foreground: 'hsl(var(--secondary-foreground))',
        background: 'hsl(var(--secondary))',
        surface: 'hsl(var(--secondary))',
        border: 'hsl(var(--secondary))',
        hover: {
          background: 'hsl(var(--secondary) / 0.8)',
          surface: 'hsl(var(--secondary) / 0.8)',
          border: 'hsl(var(--secondary) / 0.8)',
        },
      },
      neutral: {
        background: 'hsl(var(--card))',
        foreground: 'hsl(var(--neutral-foreground))',
        border: 'hsl(var(--border))',
        '100': 'hsl(var(--neutral))',
        '200': 'hsl(var(--neutral))',
        '300': 'hsl(var(--neutral))',
        '400': 'hsl(var(--neutral))',
        '500': 'hsl(var(--accent))',
        '600': 'hsl(var(--accent))',
        '700': 'hsl(var(--accent))',
        '800': 'hsl(var(--accent))',
        '900': 'hsl(var(--accent))',
      },
    },
  }}
/>
```

If using a `<ThemeProvider />` to enable theming such as dark mode, make sure the `<Frigade.Provider />` is a child of the `<ThemeProvider />` component.

## CSS Variables

Our theme runs on a set of [CSS custom properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Using_CSS_custom_properties) that map 1:1 to the properties in the theme. For any part of the theme, you can override the related CSS var and any themed value in that CSS scope will be changed accordingly.

This is especially useful in conjunction with the `css` prop, as it allows you to create temporary sub-themes that apply only to one Component, e.g.:

```tsx  theme={"system"}
<Frigade.Tour
  css={{
    // Change primary elements (i.e. buttons) in this Tour to be black
    "--fr-color-primary-surface": "var(--fr-colors-black)",
  }}
/>
```

The full list of CSS variables used in our theme can be found [here](/sdk/styling/css-variables).

## Finding a specific theme variable

You can use your browser's developer tools to inspect the CSS properties of any Frigade component. For instance, to find the theme variable for the secondary text in the [Form](/component/form) component, you can inspect the element and look for the `color` property:

<img src="https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/sdk/finding-colors.png?fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=671d8130f0dbf45d51e3cd346e236b76" className="rounded-md" style={{border: '1px solid #E8EBF0',}} data-og-width="3470" width="3470" data-og-height="1820" height="1820" data-path="images/sdk/finding-colors.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/sdk/finding-colors.png?w=280&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=93ac6afd9a803410844c5ae0a0cc79b8 280w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/sdk/finding-colors.png?w=560&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=229f456f304729452c5d8aaea0aa2879 560w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/sdk/finding-colors.png?w=840&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=bddcc50287f03dd21b7d7530668aa68e 840w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/sdk/finding-colors.png?w=1100&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=b19566c57594d7e99c6a262ecad618fe 1100w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/sdk/finding-colors.png?w=1650&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=d058e4558bc17d4efc054f2967442ea2 1650w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/sdk/finding-colors.png?w=2500&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=9fd77f23cca4b81d9530d3cb922f7de3 2500w" />

In the above example, we see that the theme variable is `--fr-colors-neutral-400`, which also corresponds to `colors.neutral.400` in the theme object.
