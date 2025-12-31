# Source: https://docs.frigade.com/sdk/styling/theming.md

# Theming

The easiest way to get Frigade components integrated into your designs is by customizing the base theme that all of our components inherit from.

The base theme covers common style properties like colors, typography, spacing, and borders. If you need deeper customization, you can dig into CSS overrides or even custom components.

To override the base theme, pass the properties you want to change into the `theme` prop of the `Provider` component. In the example below we override the default blue primary color to be `#000000`:

```tsx
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

```tsx
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

```tsx
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

<img src="https://mintlify.s3.us-west-1.amazonaws.com/frigade-docs/images/sdk/finding-colors.png" className="rounded-md" style={{border: '1px solid #E8EBF0',}} />

In the above example, we see that the theme variable is `--fr-colors-neutral-400`, which also corresponds to `colors.neutral.400` in the theme object.
