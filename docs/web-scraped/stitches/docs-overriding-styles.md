# Source: https://stitches.dev/docs/overriding-styles

Title: Overriding Styles — Stitches

URL Source: https://stitches.dev/docs/overriding-styles

Markdown Content:
How to override styles in the consumption layer.

Stitches provides a `css` prop for overriding styles easily. It’s like the style attribute, but it supports tokens, media queries, nesting and token-aware values.

[### The `css` prop](https://stitches.dev/docs/overriding-styles#the-css-prop)

All Stitches Components include a `css` prop. Use it to pass in overrides.

```
const Button = styled('button', {});
() => (
<Button
    css={{
      borderRadius: '0',
      '&:hover': {
        backgroundColor: 'black',
        color: 'white',
      },
    }}
  >
    Button
  </Button>
);
```

You can use tokens in the `css` prop.

```
const Button = styled('button', {});
() => (
<Button
    css={{
      borderRadius: '$1',
      '&:hover': {
        backgroundColor: '$blue9',
      },
    }}
  >
    Button
  </Button>
);
```

You can also use media queries in the `css` prop.

```
const Button = styled('button', {});
() => (
<Button
    css={{
      borderRadius: '0',
      color: 'white',
      '&:hover': { backgroundColor: '$blue9' },
      '@bp1': { backgroundColor: '$green9' },
      '@bp2': { backgroundColor: '$purple9' },
    }}
  >
    Button
  </Button>
);
```

[### Merging `css` prop on custom components](https://stitches.dev/docs/overriding-styles#merging-css-prop-on-custom-components)

You may want to make the `css` prop available on a custom component which already contains some pre-defined overrides.

If you're setting responsive styles, you need to make sure to deep merge the style objects.

```
const PageTitle = styled('h1', {});
function BlogTitle({ css, ...props }) {
return (
<PageTitle
      css={{
        ...css,
        '@bp1': {
          ...css['@bp1'],
          lineHeight: 1.2,
        },
        '@bp2': {
          ...css['@bp2'],
          lineHeight: 1.4,
        },
      }}
      {...props}
    />
);
}
() => (
<BlogTitle
    css={{
      marginBottom: 10,
      '@bp1': { marginBottom: 20 },
      '@bp2': { marginBottom: 30 },
    }}
  >
    Blog title
  </BlogTitle>
);
```

Note: You can use `lodash.merge` to do that for you!

[### Overriding the HTML tag](https://stitches.dev/docs/overriding-styles#overriding-the-html-tag)

Stitches provides an `as` prop for changing which tag a component outputs.

```
const Button = styled('button', {});
() => (
<Button as="a" href="#">
    Button
  </Button>
);
```
