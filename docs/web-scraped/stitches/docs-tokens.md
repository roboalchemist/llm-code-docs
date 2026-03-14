# Source: https://stitches.dev/docs/tokens

Title: Theme tokens — Stitches

URL Source: https://stitches.dev/docs/tokens

Markdown Content:
Define reusable design tokens.

[### Defining tokens](https://stitches.dev/docs/tokens#defining-tokens)

You can define your tokens as part of the `createStitches`[configuration](https://stitches.dev/docs/installation#create-your-config-file). There are 14 token types available.

```
export const { styled, css } = createStitches({
  theme: {
    colors: {
      gray500: 'hsl(206,10%,76%)',
      blue500: 'hsl(206,100%,50%)',
      purple500: 'hsl(252,78%,60%)',
      green500: 'hsl(148,60%,60%)',
      red500: 'hsl(352,100%,62%)',
},
    space: {
1: '5px',
2: '10px',
3: '15px',
},
    fontSizes: {
1: '12px',
2: '13px',
3: '15px',
},
    fonts: {
      untitled: 'Untitled Sans, apple-system, sans-serif',
      mono: 'Söhne Mono, menlo, monospace',
},
    fontWeights: {},
    lineHeights: {},
    letterSpacings: {},
    sizes: {},
    borderWidths: {},
    borderStyles: {},
    radii: {},
    shadows: {},
    zIndices: {},
    transitions: {},
},
});
```

[### Using tokens](https://stitches.dev/docs/tokens#using-tokens)

After your tokens are defined, you can use them to style components.

```
const { styled } = createStitches({
  theme: {
    colors: {
violet800: 'hsl(252 62% 54.9%)',
},
},
});
const Button = styled('button', {
  backgroundColor: '$violet800',
});
() => <Button>Button</Button>;
```

Tokens also work inside the `css` prop.

```
const Button = styled('button', {});
() => (
<Button
    css={{
      backgroundColor: '$violet800',
    }}
  >
    Button
  </Button>
);
```

Tokens even work with shorthand CSS properties.

```
const Button = styled('button', {
  margin: '$1 $2',
  border: '1px solid $violet800',
});
() => <Button>Button</Button>;
```

[### Token aliases](https://stitches.dev/docs/tokens#token-aliases)

You can create semantic tokens by referencing tokens on the same scale. As always, use the `$` to reference a token.

```
createStitches({
  theme: {
    colors: {
gray500: 'hsl(206,10%,76%)',
      primary: '$gray500',
},
},
});
```

[### Locally scoped tokens](https://stitches.dev/docs/tokens#locally-scoped-tokens)

You can create a token directly within a style object by prefixing it with two dollar signs (`$$`).

```
const Button = styled('button', {
  $$shadowColor: 'red',
  boxShadow: '0 0 0 15px $$shadowColor',
});
```

[### Scale-prefixed tokens](https://stitches.dev/docs/tokens#scale-prefixed-tokens)

You can pick a token from any of your available [theme](https://stitches.dev/docs/tokens) scales by prefixing them with the scale name.

```
const Button = styled('button', {
// apply a color token to a locally scoped token
  $$shadowColor: '$colors$purple500',
  boxShadow: '0 0 0 15px $$shadowColor'
// use a token from the sizes scale
  marginTop: '$sizes$1'
})
```

[### Naming convention](https://stitches.dev/docs/tokens#naming-convention)

We recommend using camel case, pascal case or snake case for your theme tokens. Other word separators may not work as expected.

```
// recommended
tokenName
token_name
token-name
// avoid
token.name
token$name
token*name
```

You can read more about [this here](https://github.com/stitchesjs/stitches/issues/493#issuecomment-801241038).

[### Property Mapping](https://stitches.dev/docs/tokens#property-mapping)

Token types are automatically mapped to CSS Properties for an improved developer experience.

| Token | Properties |
| --- | --- |
| `colors` | `background` `backgroundColor` `backgroundImage` `border` `borderBlock` `borderBlockEnd` `borderBlockStart` `borderBottom` `borderBottomColor` `borderColor` `borderInline` `borderInlineEnd` `borderInlineStart` `borderLeft` `borderLeftColor` `borderRight` `borderRightColor` `borderTop` `borderTopColor` `caretColor` `color` `columnRuleColor` `fill` `outlineColor` `stroke` `textDecorationColor` |
| `fonts` | `fontFamily` |
| `fontSizes` | `fontSize` |
| `fontWeights` | `fontWeight` |
| `lineHeights` | `lineHeight` |
| `letterSpacings` | `letterSpacing` |
| `radii` | `borderRadius` `borderTopLeftRadius` `borderTopRightRadius` `borderBottomRightRadius` `borderBottomLeftRadius` |
| `sizes` | `blockSize` `minBlockSize` `maxBlockSize` `inlineSize` `minInlineSize` `maxInlineSize` `width` `minWidth` `maxWidth` `height` `minHeight` `maxHeight` `flexBasis` `gridTemplateColumns` `gridTemplateRows` |
| `space` | `gap` `gridGap` `columnGap` `gridColumnGap` `rowGap` `gridRowGap` `inset` `insetBlock` `insetBlockEnd` `insetBlockStart` `insetInline` `insetInlineEnd` `insetInlineStart` `margin` `marginTop` `marginRight` `marginBottom` `marginLeft` `marginBlock` `marginBlockEnd` `marginBlockStart` `marginInline` `marginInlineEnd` `marginInlineStart` `padding` `paddingTop` `paddingRight` `paddingBottom` `paddingLeft` `paddingBlock` `paddingBlockEnd` `paddingBlockStart` `paddingInline` `paddingInlineEnd` `paddingInlineStart` `top` `right` `bottom` `left` `scrollMargin` `scrollMarginTop` `scrollMarginRight` `scrollMarginBottom` `scrollMarginLeft` `scrollMarginX` `scrollMarginY` `scrollMarginBlock` `scrollMarginBlockEnd` `scrollMarginBlockStart` `scrollMarginInline` `scrollMarginInlineEnd` `scrollMarginInlineStart` `scrollPadding` `scrollPaddingTop` `scrollPaddingRight` `scrollPaddingBottom` `scrollPaddingLeft` `scrollPaddingX` `scrollPaddingY` `scrollPaddingBlock` `scrollPaddingBlockEnd` `scrollPaddingBlockStart` `scrollPaddingInline` `scrollPaddingInlineEnd` `scrollPaddingInlineStart` |
| `zIndices` | `zIndex` |
| `shadows` | `boxShadow` `textShadow` |
| `transitions` | `transition` |
| `borderWidths` | `borderWidth` `borderTopWidth` `borderRightWidth` `borderBottomWidth` `borderLeftWidth` |
| `borderStyles` | `borderStyle` `borderTopStyle` `borderRightStyle` `borderBottomStyle` `borderLeftStyle` |
