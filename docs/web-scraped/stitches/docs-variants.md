# Source: https://stitches.dev/docs/variants

Title: Variants — Stitches

URL Source: https://stitches.dev/docs/variants

Markdown Content:
Stitches supports a first-class variant API.

[### Adding variants](https://stitches.dev/docs/variants#adding-variants)

You can add variants by using the `variants` key. There is no limit to how many variants you can add.

```
const Button = styled('button', {
// base styles
  variants: {
    color: {
      violet: {
        backgroundColor: 'blueviolet',
        color: 'white',
'&:hover': {
          backgroundColor: 'darkviolet',
},
},
      gray: {
        backgroundColor: 'gainsboro',
'&:hover': {
          backgroundColor: 'lightgray',
},
},
},
},
});
() => <Button color="violet">Button</Button>;
```

A variant accepts the same style object as the [base styles](https://stitches.dev/docs/styling).

[### Multiple variants](https://stitches.dev/docs/variants#multiple-variants)

```
const Button = styled('button', {
// base styles
  variants: {
    color: {
      violet: { ...violetStyles },
      gray: { ...grayStyles },
},
    size: {
      small: {
        fontSize: '13px',
        height: '25px',
        paddingRight: '10px',
        paddingLeft: '10px',
},
      large: {
        fontSize: '15px',
        height: '35px',
        paddingLeft: '15px',
        paddingRight: '15px',
},
},
},
});
() => (
<Button color="violet" size="large">
    Button
  </Button>
);
```

[### Boolean variants](https://stitches.dev/docs/variants#boolean-variants)

Variants can be booleans by using `true` as the key.

```
const Button = styled('button', {
// base styles
  variants: {
    outlined: {
true: {
        borderColor: 'lightgray',
},
},
},
});
() => <Button outlined>Button</Button>;
```

[### Compound variants](https://stitches.dev/docs/variants#compound-variants)

In the case of needing to set styles of a variant, based on a combination of other variants, you can use the `compoundVariants` feature.

```
const Button = styled('button', {
...styles,
  variants: {
    color: {
      violet: { ...violetStyles },
      gray: { ...grayStyles },
},
    outlined: {
true: { ...outlineVariants },
},
},
  compoundVariants: [
{
      color: 'violet',
      outlined: true,
      css: {
        color: 'blueviolet',
        borderColor: 'darkviolet',
'&:hover': {
          color: 'white',
},
},
},
{
      color: 'gray',
      outlined: true,
      css: {
        color: 'gray',
        borderColor: 'lightgray',
'&:hover': {
          color: 'black',
},
},
},
],
});
() => (
<Button color="violet" outlined>
    Button
  </Button>
);
```

[### Default variants](https://stitches.dev/docs/variants#default-variants)

You can use the `defaultVariants` feature to set a variant by default:

```
const Button = styled('button', {
...styles
  variants: {
    color: {
      violet: { ...violetStyles },
      gray: { ...grayStyles }
},
},
  defaultVariants: {
    color: 'violet'
}
});
() => <Button>Button</Button>
```

[### Responsive variants](https://stitches.dev/docs/variants#responsive-variants)

Once configured, you can apply different variants at different [breakpoints](https://stitches.dev/docs/breakpoints). You must use the `@initial` breakpoint to declare the initial variant before any breakpoints are applied.

In the example below, we apply `gray` initially, then the `violet` color variant at the `@bp1` condition.

```
const Button = styled('button', {
// base styles
  variants: {
    color: {
      violet: { ...violetStyles },
      gray: { ...grayStyles },
},
},
});
() => (
<Button
    color={{
      '@initial': 'gray',
      '@bp1': 'violet',
    }}
  >
    Button
  </Button>
);
```
