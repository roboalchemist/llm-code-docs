# Source: https://stitches.dev/docs/responsive-styles

Title: Responsive Styles — Stitches

URL Source: https://stitches.dev/docs/responsive-styles

Markdown Content:
How to configure breakpoints and apply variants responsively.

[### Configure your breakpoints](https://stitches.dev/docs/responsive-styles#configure-your-breakpoints)

Define your media at-rules in the `media` object. You can add as many as you need.

```
export const { styled, css } = createStitches({
  media: {
    bp1: '(min-width: 640px)',
    bp2: '(min-width: 768px)',
    bp3: '(min-width: 1024px)',
},
});
```

Note: Choose the naming convention you prefer. We recommend either `bp1`, `bp2`, `bp3` etc. or `sm`, `md`, `lg` etc.

[### Responsive variants](https://stitches.dev/docs/responsive-styles#responsive-variants)

Once configured, you can apply different variants at different [breakpoints](https://stitches.dev/docs/breakpoints).

In the example below, we apply the `violet` color variant at the `bp2` condition.

```
const Button = styled('button', {
// base styles
  variants: {
    color: {
violet: {},
      gray: {},
},
},
});
() => (
<Button
    color={{
      '@bp2': 'violet'
    }}
  >
    Button
  </Button>
);
```

Note: If you're using TypeScript, your variants will be typed.

[### Setting an initial variant](https://stitches.dev/docs/responsive-styles#setting-an-initial-variant)

You must use the `@initial` breakpoint to declare the initial variant before any breakpoints are applied.

In the example below, we apply `gray` initially, then the `violet` color variant at the `bp2` condition.

```
const Button = styled('button', {
// base styles
  variants: {
    color: {
      violet: {},
gray: {},
},
},
});
() => (
<Button
    color={{
      '@initial': 'gray',
      '@bp2': 'violet'
    }}
  >
    Button
  </Button>
);
```

[### Using breakpoints in the style objects](https://stitches.dev/docs/responsive-styles#using-breakpoints-in-the-style-objects)

```
const Button = styled('button', {
// base styles
'@bp1': {
// Styles for bp1
},
});
```

Note: In most cases, we do not recommend applying responsive breakpoints inline. Ideally, your component styles should be immutable.
