# Panda CSS Documentation
# Source: https://panda-css.com/llms.txt/concepts
# Section: llms.txt/concepts

# Panda CSS Core Concepts

> This document contains all concepts documentation for Panda CSS

## Table of Contents

- [Cascade Layers](#cascade-layers)
- [Color opacity modifier](#color-opacity-modifier)
- [Conditional Styles](#conditional-styles)
- [The extend keyword](#the-extend-keyword)
- [Global Styles](#global-styles)
- [Panda Integration Hooks](#panda-integration-hooks)
- [JSX Style Context](#jsx-style-context)
- [Merging Styles](#merging-styles)
- [Patterns](#patterns)
- [Recipes](#recipes)
- [Responsive Design](#responsive-design)
- [Slot Recipes](#slot-recipes)
- [Style props](#style-props)
- [Styled System](#styled-system)
- [Template Literals](#template-literals)
- [Virtual Color](#virtual-color)
- [Writing Styles](#writing-styles)

---


## Cascade Layers

CSS cascade layers refer to the order in which CSS rules are applied to an HTML element.

When multiple CSS rules apply
to the same element, the browser uses the cascade to determine which rule should take precedence. See the
[MDN article](https://developer.mozilla.org/en-US/docs/Web/CSS/@layer) to learn more.

Panda takes advantage of the cascade to provide a more efficient and flexible way to organize styles. This allows you to
define styles in a modular way, using CSS rules that are scoped to specific components or elements.

## Layer Types

Panda supports five types of cascade layers out of the box:

- `@layer reset` - The reset layer is used to reset the default styles of HTML elements. This is used when
  `preflight: true` is set in the config. You can also use this layer to add your own reset styles.

The generated CSS for the reset layer looks like this:

```css
@layer reset {
  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }
  /* ... */
}
```

- `@layer base` - The base layer contains global styles defined in the `globalStyles` key in the config. You can also
  use this layer to add your own global styles.

The generated CSS for the base layer looks like this:

```css
@layer base {
  a {
    color: #000;
    text-decoration: none;
  }
  /* ... */
}
```

- `@layer recipes` - The recipes layer contains styles for recipes created within the config (aka config recipes). You
  can also use this layer to add your own component styles.

The generated CSS for the recipes layer looks like this:

```css
@layer recipes {
  .button {
    /* ... */
  }

  .button--variant-primary {
    /* ... */
  }
  /* ... */
}
```

- `@layer tokens` - The tokens layer contains css variables for tokens and semantic tokens. You can also use this layer
  to add your own design tokens.

The generated CSS for the tokens layer looks like this:

```css
@layer tokens {
  :root {
    --color-primary: #000;
    --color-secondary: #fff;
    --color-tertiary: #ccc;
    --shadow-sm: 0 0 0 1px rgba(0, 0, 0, 0.05);
  }
  /* ... */
}
```

- `@layer utilities` - Styles that are scoped to a specific utility class. These styles are only applied to elements
  that have the utility class applied.

## Layer Order

The cascade layers are applied in the following order:

- `@layer utilities` (Highest priority)
- `@layer recipes`
- `@layer tokens`
- `@layer base`
- `@layer reset` (Lowest priority)

This means that styles defined in the `@layer utilities` will take precedence over styles defined in the
`@layer recipes`. This is useful when you want to override the default styles of a component.

## Layer CSS

The generated CSS in Panda is organized into layers. This allows you to define styles in a modular way, using CSS rules
that are scoped to specific components or elements.

Here's what the first line of the generated CSS looks like:

```css
@layer reset, base, tokens, recipes, utilities;
```

Adding this line to the top of your CSS file will determine the order in which the layers are applied. This is the most
exciting feature of CSS cascade layers.

## Customize layers

Panda lets you customize the cascade layers, so your project can coexist with other solutions. Learn more about customizing layers [here](/docs/references/config#layers).

## Polyfills

In event that you need to support older browsers, you can use the following postcss plugin in your PostCSS config:

- [postcss-cascade-layers](https://www.npmjs.com/package/@csstools/postcss-cascade-layers): Adds support for CSS Cascade Layers.

Here is an example of a `postcss.config.js` file that uses these polyfills:

```js
module.exports = {
  plugins: ['@pandacss/dev/postcss', '@csstools/postcss-cascade-layers']
}
```

Since CSS `@layer`s have a lower priority than other CSS rules, this postcss plugin is also useful in cases where your styles are being overridden by some other stylesheets that you're not in total control of, since it will remove the `@layer` rules and still emulate their specificity.


---


## Color opacity modifier

How to dynamically set the opacity of a raw color or color token

Every utilities connected to the `colors` tokens in the `@pandacss/preset-base` (included by default) can use the
[`color-mix`](https://developer.mozilla.org/en-US/docs/Web/CSS/color_value/color-mix) CSS function. This means for
example: `background`, `backgroundColor`, `color`, `border`, `borderColor`, etc.

This function allows you to mix two colors together, and we use it to change the opacity of a color using the
`{color}/{opacity}` syntax.

You can use it like this:

```ts
css({
  bg: 'red.300/40',
  color: 'white'
})
```

This will generate:

```css
@layer utilities {
  .bg_red\.300\/40 {
    --mix-background: color-mix(in srgb, var(--colors-red-300) 40%, transparent);
    background: var(--mix-background, var(--colors-red-300));
  }

  .text_white {
    color: var(--colors-white);
  }
}
```

- If you're not using any opacity, the utility will **not** use `color-mix`
- The utility will automatically fallback to the original color if the `color-mix` function is not supported by the
  browser.
- You can use any of the color tokens, and any of the opacity tokens.

---

The `utilities` transform function also receives a `utils` object that contains the `colorMix` function, so you can also
use it on your own utilities:

```ts
export default defineConfig({
  utilities: {
    background: {
      shorthand: 'bg',
      className: 'bg',
      values: 'colors',
      transform(value, args) {
        const mix = args.utils.colorMix(value)
        // This can happen if the value format is invalid (e.g. `bg: red.300/invalid` or `bg: red.300//10`)
        if (mix.invalid) return { background: value }

        return {
          background: mix.value
        }
      }
    }
  }
})
```

---

Here's a cool snippet (that we use internally !) that makes it easier to create a utility transform for a given
property:

```ts
import type { PropertyTransform } from '@pandacss/types'
export const createColorMixTransform =
  (prop: string): PropertyTransform =>
  (value, args) => {
    const mix = args.utils.colorMix(value)
    if (mix.invalid) return { [prop]: value }
    const cssVar = '--mix-' + prop
    return {
      [cssVar]: mix.value,
      [prop]: `var(${cssVar}, ${mix.color})`
    }
  }
```

then the same utility transform as above can be written like this:

```ts
export default defineConfig({
  utilities: {
    background: {
      shorthand: "bg",
      className: "bg",
      values: "colors",
      transform: createColorMixTransform("background"),
  },
});
```


---


## Conditional Styles

Learn how to use conditional and responsive styles in Panda.

When writing styles, you might need to apply specific changes depending on a specific condition, whether it's based on
breakpoint, css pseudo state, media query or custom data attributes.

Panda allows you to write conditional styles, and provides common condition shortcuts to make your life easier. Let's
say you want to change the background color of a button when it's hovered. You can do it like this:

```jsx
<button
  className={css({
    bg: 'red.500',
    _hover: { bg: 'red.700' }
  })}
>
  Hover me
</button>
```

## Overview

### Property based condition

This works great, but might be a bit verbose. You can apply the condition `_hover` directly to the `bg` property,
leading to a more concise syntax:

```diff
<button
  className={css({
-   bg: 'red.500',
-   _hover: { bg: 'red.700' }
+   bg: { base: 'red.500', _hover: 'red.700' }
  })}
>
  Hover me
</button>
```

> Note: The `base` key is used to define the default value of the property, without any condition.

### Nested condition

Conditions in Panda can be nested, which means you can apply multiple conditions to a single property or another
condition.

Let's say you want to change the background color of a button when it's focused and hovered. You can do it like this:

```jsx
<button
  className={css({
    bg: { base: 'red.500', _hover: { _focus: 'red.700' } }
  })}
>
  Hover me
</button>
```

### Built-in conditions

Panda includes a set of common pseudo states that you can use to style your components:

- Pseudo Class: `_hover`, `_active`, `_focus`, `_focusVisible`, `_focusWithin`, `_disabled`
- Pseudo Element: `_before`, `_after`
- Media Query: `sm`, `md`, `lg`, `xl`, `2xl`
- Data Attribute Selector: `_horizontal`, `_vertical`, `_portrait`, `_landscape`

## Arbitrary selectors

What if you need a one-off selector that is not defined in your config's conditions? You can use the `css` function to
generate classes for arbitrary selectors:

```tsx
import { css } from '../styled-system/css'

const App = () => {
  return (
    <div
      className={css({
        '&[data-state=closed]': { color: 'red.300' },
        '& > *': { margin: '2' }
      })}
    />
  )
}
```

This also works with the supported at-rules (`@media`, `@layer`, `@container`, `@supports`, and `@page`):

```tsx
import { css } from '../styled-system/css'

const App = () => {
  return (
    <div className={css({ display: 'flex', containerType: 'size' })}>
      <div
        className={css({
          '@media (min-width: 768px)': {
            color: 'red.300'
          },
          '@container (min-width: 10px)': {
            color: 'green.300'
          },
          '@supports (display: flex)': {
            fontSize: '3xl',
            color: 'blue.300'
          }
        })}
      />
    </div>
  )
}
```

## Pseudo Classes

### Hover, Active, Focus, and Disabled

You can style the hover, active, focus, and disabled states of an element using their `_` modifier:

```jsx
<button
  className={css({
    bg: 'red.500',
    _hover: { bg: 'red.700' },
    _active: { bg: 'red.900' }
  })}
>
  Hover me
</button>
```

### First, Last, Odd, Even

You can style the first, last, odd, and even elements of a group using their `_` modifier:

```jsx
<ul>
  {items.map(item => (
    <li key={item} className={css({ _first: { color: 'red.500' } })}>
      {item}
    </li>
  ))}
</ul>
```

You can also style even and odd elements using the `_even` and `_odd` modifier:

```jsx
<table>
  <tbody>
    {items.map(item => (
      <tr
        key={item}
        className={css({
          _even: { bg: 'gray.100' },
          _odd: { bg: 'white' }
        })}
      >
        <td>{item}</td>
      </tr>
    ))}
  </tbody>
</table>
```

## Pseudo Elements

### Before and After

You can style the `::before` and `::after` pseudo elements of an element using their `_before` and `_after` modifier:

```jsx
<div
  className={css({
    _before: { content: '"👋"' }
  })}
>
  Hello
</div>
```

#### Notes

- **Before and After**: Ensure you wrap the content value in double quotes.
- **Mixing with Conditions**: When using condition and pseudo elements, prefer to place the condition **before** the
  pseudo element.

```jsx
css({
  // This works ✅
  _dark: { _backdrop: { color: 'red' } }
  // This doesn't work ❌
  _backdrop: { _dark: { color: 'red' } }
})
```

The reason `_backdrop: { _dark: { color: 'red' } }` doesn't work is because it generated an invalid CSS structure that
looks like:

```css
&::backdrop {
  &.dark,
  .dark & {
    color: red;
  }
}
```

### Placeholder

Style the placeholder text of any input or textarea using the `_placeholder` modifier:

```jsx
<input
  placeholder="Enter your name"
  className={css({
    _placeholder: { color: 'gray.500' }
  })}
/>
```

### File Inputs

Style the file input button using the `_file` modifier:

```jsx
<input
  type="file"
  className={css({
    _file: { bg: 'gray.500', px: '4', py: '2', marginEnd: '3' }
  })}
/>
```

## Media Queries

### Reduced Motion

Use the `_motionReduce` and `_motionSafe` modifiers to style an element based on the user's motion preference:

```jsx
<div
  className={css({
    _motionReduce: { transition: 'none' },
    _motionSafe: { transition: 'all 0.3s' }
  })}
>
  Hello
</div>
```

### Color Scheme

The `prefers-color-scheme` media feature is used to detect if the user has requested the system use a light or dark
color theme.

Use the `_osLight` and `_osDark` modifiers to style an element based on the user's color scheme preference:

```jsx
<div
  className={css({
    bg: 'white',
    _osDark: { bg: 'black' }
  })}
>
  Hello
</div>
```

Let's say your app is dark by default, but you want to allow users to switch to a light theme. You can do it like this:

```jsx
<div
  className={css({
    bg: 'black',
    _osLight: { bg: 'white' }
  })}
>
  Hello
</div>
```

### Color Contrast

The `prefers-contrast` media feature is used to detect if the user has requested the system use a high or low contrast
theme.

Use the `_highContrast` and `_lessContrast` modifiers to style an element based on the user's color contrast preference:

```jsx
<div
  className={css({
    bg: 'white',
    _highContrast: { bg: 'black' }
  })}
>
  Hello
</div>
```

### Orientation

The `orientation` media feature is used to detect if the user has a device in portrait or landscape mode.

Use the `_portrait` and `_landscape` modifiers to style an element based on the user's device orientation:

```jsx
<div
  className={css({
    pb: '4',
    _portrait: { pb: '8' }
  })}
>
  Hello
</div>
```

## Group Selectors

When you need to style an element based on its parent element's state or attribute, you can add the `group` class to the
parent element, and use any of the `_group*` modifiers on the child element.

```jsx
<div className="group">
  <p className={css({ _groupHover: { bg: 'red.500' } })}>Hover me</p>
</div>
```

This modifer for every pseudo class modifiers like `_groupHover`, `_groupActive`, `_groupFocus`, and `_groupDisabled`,
etc.

## Sibling Selectors

When you need to style an element based on its sibling element's state or attribute, you can add the `peer` class to the
sibling element, and use any of the `_peer*` modifiers on the target element.

```jsx
<div>
  <p className="peer">Hover me</p>
  <p className={css({ _peerHover: { bg: 'red.500' } })}>I'll change by bg</p>
</div>
```

> Note: This only works for when the element marked with `peer` is a previous siblings, that is, it comes before the
> element you want to start.

## Data Attribute

### LTR and RTL

You can style an element based on the direction of the text using the `_ltr` and `_rtl` modifiers:

```jsx
<div dir="ltr">
  <div
    className={css({
      _ltr: { ml: '3' },
      _rtl: { mr: '3' }
    })}
  >
    Hello
  </div>
</div>
```

For this to work, you need to set the `dir` attribute on the parent element. In most cases,you can set this on the
`html` element.

> **Note:** Consider using logical css properties like `marginInlineStart` and `marginInlineEnd` instead their physical
> counterparts like `marginLeft` and `marginRight`. This will reduce the need to use the `_ltr` and `_rtl` modifiers.

### State

You can style an element based on its `data-{state}` attribute using the corresponding `_{state}` modifier:

```jsx
<div
  data-loading
  className={css({
    _loading: { bg: 'gray.500' }
  })}
>
  Hello
</div>
```

This also works for common states like `data-active`, `data-disabled`, `data-focus`, `data-hover`, `data-invalid`,
`data-required`, and `data-valid`.

```jsx
<div
  data-active
  className={css({
    _active: { bg: 'gray.500' }
  })}
>
  Hello
</div>
```

> Most of the `data-{state}` attributes typically mirror the corresponding browser pseudo class. For example,
> `data-hover` is equivalent to `:hover`, `data-focus` is equivalent to `:focus`, and `data-active` is equivalent to
> `:active`.

### Orientation

You can style an element based on its `data-orientation` attribute using the `_horizontal` and `_vertical` modifiers:

```jsx
<div
  data-orientation="horizontal"
  className={css({
    _horizontal: { bg: 'red.500' },
    _vertical: { bg: 'blue.500' }
  })}
>
  Hello
</div>
```

## ARIA Attribute

You can style an element based on its `aria-{state}=true` attribute using the corresponding `_{state}` modifier:

```jsx
<div
  aria-expanded="true"
  className={css({
    _expanded: { bg: 'gray.500' }
  })}
>
  Hello
</div>
```

> Most of the `aria-{state}` attributes typically mirror the support ARIA states in the browser pseudo class. For
> example, `aria-checked=true` is styled with `_checked`, `aria-disabled=true` is styled with `_disabled`.

## Container queries

You can define container names and sizes in your theme configuration and use them in your styles.

```ts
export default defineConfig({
  // ...
  theme: {
    extend: {
      containerNames: ['sidebar', 'content'],
      containerSizes: {
        xs: '40em',
        sm: '60em',
        md: '80em'
      }
    }
  }
})
```

The default container sizes in the `@pandacss/preset-panda` preset are shown below:

```ts
export const containerSizes = {
  xs: '320px',
  sm: '384px',
  md: '448px',
  lg: '512px',
  xl: '576px',
  '2xl': '672px',
  '3xl': '768px',
  '4xl': '896px',
  '5xl': '1024px',
  '6xl': '1152px',
  '7xl': '1280px',
  '8xl': '1440px'
}
```

Then use them in your styles by referencing using `@<container-name>/<container-size>` syntax:

> The default container syntax is `@/<container-size>`.

```ts
import { css } from '/styled-system/css'

function Demo() {
  return (
    <nav className={css({ containerType: 'inline-size' })}>
      <div
        className={css({
          fontSize: { '@/sm': 'md' }
        })}
      />
    </nav>
  )
}
```

This will generate the following CSS:

```css
.cq-type_inline-size {
  container-type: inline-size;
}

@container (min-width: 60em) {
  .\@\/sm:fs_md {
    container-type: inline-size;
  }
}
```

You can also named container queries:

```ts
import { cq } from 'styled-system/patterns'

function Demo() {
  return (
    <nav className={cq({ name: 'sidebar' })}>
      <div
        className={css({
          fontSize: { base: 'lg', '@sidebar/sm': 'md' }
        })}
      />
    </nav>
  )
}
```

## Reference

Here's a list of all the condition shortcuts you can use in Panda:

| Condition name         | Selector                                                                                         |
| ---------------------- | -------------------------------------------------------------------------------------------------|
| \_hover                | `&:is(:hover, [data-hover])`                                                                     |
| \_focus                | `&:is(:focus, [data-focus])`                                                                     |
| \_focusWithin          | `&:focus-within`                                                                                 |
| \_focusVisible         | `&:is(:focus-visible, [data-focus-visible])`                                                     |
| \_disabled             | `&:is(:disabled, [disabled], [data-disabled], [aria-disabled=true])`                             |
| \_active               | `&:is(:active, [data-active])`                                                                   |
| \_visited              | `&:visited`                                                                                      |
| \_target               | `&:target`                                                                                       |
| \_readOnly             | `&:is(:read-only, [data-read-only], [aria-readonly=true])`                                       |
| \_readWrite            | `&:read-write`                                                                                   |
| \_empty                | `&:is(:empty, [data-empty])`                                                                     |
| \_checked              | `&:is(:checked, [data-checked], [aria-checked=true], [data-state="checked"])`                    |
| \_enabled              | `&:enabled`                                                                                      |
| \_expanded             | `&:is([aria-expanded=true], [data-expanded], [data-state="expanded"])`                           |
| \_highlighted          | `&[data-highlighted]`                                                                            |
| \_complete             | `&[data-complete]`                                                                               |
| \_incomplete           | `&[data-incomplete]`                                                                             |
| \_dragging             | `&[data-dragging]`                                                                               |
| \_before               | `&::before`                                                                                      |
| \_after                | `&::after`                                                                                       |
| \_firstLetter          | `&::first-letter`                                                                                |
| \_firstLine            | `&::first-line`                                                                                  |
| \_marker               | `&::marker, &::-webkit-details-marker`                                                           |
| \_selection            | `&::selection`                                                                                   |
| \_file                 | `&::file-selector-button`                                                                        |
| \_backdrop             | `&::backdrop`                                                                                    |
| \_first                | `&:first-child`                                                                                  |
| \_last                 | `&:last-child`                                                                                   |
| \_only                 | `&:only-child`                                                                                   |
| \_even                 | `&:nth-child(even)`                                                                              |
| \_odd                  | `&:nth-child(odd)`                                                                               |
| \_firstOfType          | `&:first-of-type`                                                                                |
| \_lastOfType           | `&:last-of-type`                                                                                 |
| \_onlyOfType           | `&:only-of-type`                                                                                 |
| \_peerFocus            | `.peer:is(:focus, [data-focus]) ~ &`                                                             |
| \_peerHover            | `.peer:is(:hover, [data-hover]) ~ &`                                                             |
| \_peerActive           | `.peer:is(:active, [data-active]) ~ &`                                                           |
| \_peerFocusWithin      | `.peer:focus-within ~ &`                                                                         |
| \_peerFocusVisible     | `.peer:is(:focus-visible, [data-focus-visible]) ~ &`                                             |
| \_peerDisabled         | `.peer:is(:disabled, [disabled], [data-disabled], [aria-disabled=true]) ~ &`                     |
| \_peerChecked          | `.peer:is(:checked, [data-checked], [aria-checked=true], [data-state="checked"]) ~ &`            |
| \_peerInvalid          | `.peer:is(:invalid, [data-invalid], [aria-invalid=true]) ~ &`                                    |
| \_peerExpanded         | `.peer:is([aria-expanded=true], [data-expanded], [data-state="expanded"]) ~ &`                   |
| \_peerPlaceholderShown | `.peer:placeholder-shown ~ &`                                                                    |
| \_groupFocus           | `.group:is(:focus, [data-focus]) &`                                                              |
| \_groupHover           | `.group:is(:hover, [data-hover]) &`                                                              |
| \_groupActive          | `.group:is(:active, [data-active]) &`                                                            |
| \_groupFocusWithin     | `.group:focus-within &`                                                                          |
| \_groupFocusVisible    | `.group:is(:focus-visible, [data-focus-visible]) &`                                              |
| \_groupDisabled        | `.group:is(:disabled, [disabled], [data-disabled], [aria-disabled=true]) &`                      |
| \_groupChecked         | `.group:is(:checked, [data-checked], [aria-checked=true], [data-state="checked"]) &`             |
| \_groupExpanded        | `.group:is([aria-expanded=true], [data-expanded], [data-state="expanded"]) &`                    |
| \_groupInvalid         | `.group:is(:invalid, [data-invalid], [aria-invalid=true]) &`                                     |
| \_indeterminate        | `&:is(:indeterminate, [data-indeterminate], [aria-checked=mixed], [data-state="indeterminate"])` |
| \_required             | `&:is(:required, [data-required], [aria-required=true])`                                         |
| \_valid                | `&:is(:valid, [data-valid])`                                                                     |
| \_invalid              | `&:is(:invalid, [data-invalid], [aria-invalid=true])`                                            |
| \_autofill             | `&:autofill`                                                                                     |
| \_inRange              | `&:is(:in-range, [data-in-range])`                                                               |
| \_outOfRange           | `&:is(:out-of-range, [data-outside-range])`                                                      |
| \_placeholder          | `&::placeholder, &[data-placeholder]`                                                            |
| \_placeholderShown     | `&:is(:placeholder-shown, [data-placeholder-shown])`                                             |
| \_pressed              | `&:is([aria-pressed=true], [data-pressed])`                                                      |
| \_selected             | `&:is([aria-selected=true], [data-selected])`                                                    |
| \_grabbed              | `&:is([aria-grabbed=true], [data-grabbed])`                                                      |
| \_underValue           | `&[data-state=under-value]`                                                                      |
| \_overValue            | `&[data-state=over-value]`                                                                       |
| \_atValue              | `&[data-state=at-value]`                                                                         |
| \_default              | `&:default`                                                                                      |
| \_optional             | `&:optional`                                                                                     |
| \_open                 | `&:is([open], [data-open], [data-state="open"], :popover-open)`                                  |
| \_closed               | `&:is([closed], [data-closed], [data-state="closed"])`                                           |
| \_fullscreen           | `&:is(:fullscreen, [data-fullscreen])`                                                           |
| \_loading              | `&:is([data-loading], [aria-busy=true])`                                                         |
| \_hidden               | `&:is([hidden], [data-hidden])`                                                                  |
| \_current              | `&:is([aria-current=true], [data-current])`                                                      |
| \_currentPage          | `&[aria-current=page]`                                                                           |
| \_currentStep          | `&[aria-current=step]`                                                                           |
| \_today                | `&[data-today]`                                                                                  |
| \_unavailable          | `&[data-unavailable]`                                                                            |
| \_rangeStart           | `&[data-range-start]`                                                                            |
| \_rangeEnd             | `&[data-range-end]`                                                                              |
| \_now                  | `&[data-now]`                                                                                    |
| \_topmost              | `&[data-topmost]`                                                                                |
| \_motionReduce         | `@media (prefers-reduced-motion: reduce)`                                                        |
| \_motionSafe           | `@media (prefers-reduced-motion: no-preference)`                                                 |
| \_print                | `@media print`                                                                                   |
| \_landscape            | `@media (orientation: landscape)`                                                                |
| \_portrait             | `@media (orientation: portrait)`                                                                 |
| \_dark                 | `.dark &`                                                                                        |
| \_light                | `.light &`                                                                                       |
| \_osDark               | `@media (prefers-color-scheme: dark)`                                                            |
| \_osLight              | `@media (prefers-color-scheme: light)`                                                           |
| \_highContrast         | `@media (forced-colors: active)`                                                                 |
| \_lessContrast         | `@media (prefers-contrast: less)`                                                                |
| \_moreContrast         | `@media (prefers-contrast: more)`                                                                |
| \_ltr                  | `:where([dir=ltr], :dir(ltr)) &`                                                                 |
| \_rtl                  | `:where([dir=rtl], :dir(rtl)) &`                                                                 |
| \_scrollbar            | `&::-webkit-scrollbar`                                                                           |
| \_scrollbarThumb       | `&::-webkit-scrollbar-thumb`                                                                     |
| \_scrollbarTrack       | `&::-webkit-scrollbar-track`                                                                     |
| \_horizontal           | `&[data-orientation=horizontal]`                                                                 |
| \_vertical             | `&[data-orientation=vertical]`                                                                   |
| \_icon                 | `& :where(svg)`                                                                                  |
| \_starting             | `@starting-style`                                                                                |
| \_noscript             | `@media (scripting: none)`                                                                       |
| \_invertedColors       | `@media (inverted-colors: inverted)`                                                             |

## Custom conditions

Panda lets you create your own conditions, so you're not limited to the ones in the default preset. Learn more about
customizing conditions [here](/docs/customization/conditions).


---


## The extend keyword

What is and how to to use the extend keyword

The `extend` keyword allows you to extend the default Panda configuration. It is useful when you want to add your own
customizations to Panda, without erasing the default `presets` values (`conditions`, `tokens`, `utilities`, etc).

It will (deeply) merge your customizations with the default ones, instead of replacing them.

The `extend` keyword allows you to extend the following parts of Panda:

- [conditions](/docs/customization/conditions)
- [theme](/docs/customization/theme)
- [recipes](/docs/concepts/recipes) (included in theme)
- [patterns](/docs/customization/patterns)
- [utilities](/docs/customization/utilities)
- [globalCss](/docs/concepts/writing-styles#global-styles)
- [staticCss](/docs/guides/static)

> These keys are all allowed in [presets](/docs/customization/presets).

## Example

After running the `panda init` command you should see something similar to this:

```ts
import { defineConfig } from '@pandacss/dev'

export default defineConfig({
  // ...

  // Useful for theme customization
  theme: {
    extend: {} // 👈 it's already there! perfect, now you just need to add your customizations in this object
  }

  // ...
})
```

Let's say you want to add a new color to the default theme. You can do it like this:

```ts
import { defineConfig } from '@pandacss/dev'

export default defineConfig({
  theme: {
    extend: {
      colors: {
        primary: { value: '#ff0000' }
      }
    }
  }
})
```

This will add a new color to the default theme, without erasing the other ones.

Now, let's say we want to create new property `br` that applies a border radius to an element.

```ts
import { defineConfig } from '@pandacss/dev'

export default defineConfig({
  utilities: {
    extend: {
      br: {
        className: 'rounded', // css({ br: "sm" }) => rounded-sm
        values: 'radii', // connect values to the radii tokens
        transform(value) {
          return { borderRadius: value }
        }
      }
    }
  }
})
```

What if this utility was coming from a preset (`@acme/my-preset`) ? You can extend any specific part, as it will be
deeply merged with the existing one:

```ts
import { defineConfig } from '@pandacss/dev'

export default defineConfig({
  presets: ['@acme/my-preset']
  utilities: {
    extend: {
      br: {
        className: 'br' // css({ br: "sm" }) => br-sm
      }
    }
  }
})
```

## Removing something from a preset

Let's say you want to remove the `br` utility from the `@acme/my-preset` preset. You can do it like this:

```ts
import { defineConfig } from '@pandacss/dev'
import myPreset from '@acme/my-preset'

const { br, ...utilities } = myPreset.utilities

export default defineConfig({
  presets: ['@acme/my-preset']
  utilities: {
    extend: {
      ...utilities, // 👈 we still want the other utilities from this preset
      // your customizations here
    }
  }
})
```

## Removing something from the base presets

Let's say you want to remove the `stack` pattern from the `@pandacss/preset-base` preset (included by default).

You can pick only the parts that you need with and spread the rest, like this:

```ts
import pandaBasePreset from '@pandacss/preset-base'

// omitting stack here
const { stack, ...pandaBasePresetPatterns } = pandaBasePreset.patterns

export default defineConfig({
  presets: ['@pandacss/preset-panda'], // 👈 we still want the tokens, breakpoints and textStyles from this preset

  // ⚠️ we need to eject to prevent the `@pandacss/preset-base` from being resolved
  // https://panda-css.com/docs/customization/presets#which-panda-presets-will-be-included-
  eject: true,
  patterns: {
    extend: {
      ...pandaBasePresetPatterns
      // your customizations here
    }
  }
})
```

## Minimal setup

If you want to use Panda with the bare minimum, without any of the defaults, you can read more about it
[here](/docs/guides/minimal-setup)

## FAQ

### Why is my preset overriding the base one, even after adding it to the array?

You might have forgotten to include the `extend` keyword in your config. Without `extend`, your preset will completely
replace the base one, instead of merging with it.


---


## Global Styles

How to work with resets, global styles, and global CSS variables in Panda.

Panda groups global styles into reset and base layers so you can control defaults predictably and override them safely.

## Layers overview

- **@layer reset**: Preflight/reset styles, enabled with `preflight`.
- **@layer base**: Your additional global styles via `globalCss`.

> See also: [Cascade layers](/docs/concepts/cascade-layers)

## Reset (preflight)

Enable or scope the reset styles.

```ts filename="panda.config.ts"
import { defineConfig } from '@pandacss/dev'

export default defineConfig({
  preflight: true
})
```

Scope and level:

```ts filename="panda.config.ts"
import { defineConfig } from '@pandacss/dev'

export default defineConfig({
  preflight: { scope: '.extension', level: 'element' }
})
```

## Exposed global CSS variables

These variables are used by the reset and defaults. Set them in `globalCss`:

- `--global-font-body`
- `--global-font-mono`
- `--global-color-border`
- `--global-color-placeholder`
- `--global-color-selection`
- `--global-color-focus-ring`

## Setting global styles (base)

Use `globalCss` to define additional global styles and set variables.

```ts filename="panda.config.ts"
import { defineConfig } from '@pandacss/dev'

export default defineConfig({
  // ...
  globalCss: {
    html: {
      '--global-font-body': 'Inter, sans-serif',
      '--global-font-mono': 'Mononoki Nerd Font, monospace',
      '--global-color-border': 'colors.gray.400',
      '--global-color-placeholder': 'rgba(0,0,0,0.5)',
      '--global-color-selection': 'rgba(0,115,255,0.3)',
      '--global-color-focus-ring': 'colors.blue.400'
    }
  }
})
```

### Theming patterns

You can set variables on `:root`, a `.dark` class, or via media queries.

```css
:root {
  --global-color-border: oklch(0.8 0 0);
}
.dark {
  --global-color-border: oklch(0.72 0 0);
}

@media (prefers-color-scheme: dark) {
  :root {
    --global-color-border: oklch(0.72 0 0);
  }
}
```

## Custom global variables (`globalVars`)

Define additional global CSS variables or `@property` entries.

```ts filename="panda.config.ts"
import { defineConfig } from '@pandacss/dev'

export default defineConfig({
  globalVars: {
    '--button-color': {
      syntax: '<color>',
      inherits: false,
      initialValue: 'blue'
    }
  }
})
```

> Keys from `globalVars` are suggestable in style objects and generated near your tokens at `cssVarRoot`.

## Troubleshooting

- **Global styles aren't applied:** Confirm `preflight` is enabled (if you expect reset), and ensure your selector
  (`html`, `:root`, `.dark`, etc.) matches the element where variables are set.

- **Global styles are overridden by utilities or component styles:** Verify layer order and specificity. Ensure
  `@layer reset` and `@layer base` are emitted before utilities. If you customize insertion or injection order (SSR,
  framework plugins), preserve `@layer` order so globals are not overridden.


---


## Panda Integration Hooks

Leveraging hooks in Panda to create custom functionality.

Panda hooks can be used to add new functionality or modify existing behavior during certian parts of the compiler
lifecycle.

Hooks are mostly callbacks that can be added to the panda config via the `hooks` property, or installed via `plugins`.

Here are some examples of what you can do with hooks:

- modify the resolved config (`config:resolved`), like strip out tokens or keyframes.
- modify presets after they are resolved (`preset:resolved`), like removing specific tokens or theme properties from a
  preset.
- tweak the design token or classname engine (`tokens:created`, `utility:created`), like prefixing token names, or
  customizing the hashing function
- transform a source file to a `tsx` friendly syntax before it's parsed (`parser:before`) so that Panda can
  automatically extract its styles usage
- create your own styles parser (`parser:before`, `parser:after`) using the file's content so that Panda could be used
  with any templating language
- alter the generated JS and DTS code (`codegen:prepare`)
- modify the generated CSS (`cssgen:done`), allowing all kinds of customizations like removing the unused CSS variables,
  etc.
- restrict `strictTokens` to a specific set of token categories, ex: only affect `colors` and `spacing` tokens and
  therefore allow any value for `fontSizes` and `lineHeights`

## Examples

### Prefixing token names

This is especially useful when migrating from other css-in-js libraries, [like Stitches.](/docs/migration/stitches)

```ts
import { defineConfig } from '@pandacss/dev'

export default defineConfig({
  // ...
  hooks: {
    'tokens:created': ({ configure }) => {
      configure({
        formatTokenName: path => '$' + path.join('-')
      })
    }
  }
})
```

### Customizing the hash function

When using the [`hash: true`](/docs/concepts/writing-styles) config property, you can customize the function used to
hash the classnames.

```ts
export default defineConfig({
  // ...
  hash: true,
  hooks: {
    'utility:created': ({ configure }) => {
      configure({
        toHash: (paths, toHash) => {
          const stringConds = paths.join(':')
          const splitConds = stringConds.split('_')
          const hashConds = splitConds.map(toHash)
          return hashConds.join('_')
        }
      })
    }
  }
})
```

### Modifying the config

Here's an example of how to leveraging the provided `utils` functions in the `config:resolved` hook to remove the
`stack` pattern from the resolved config.

```ts
import { defineConfig } from '@pandacss/dev'

export default defineConfig({
  // ...
  hooks: {
    'config:resolved': ({ config, utils }) => {
      return utils.omit(config, ['patterns.stack'])
    }
  }
})
```

### Modifying presets

You can use the `preset:resolved` hook to modify presets after they are resolved. This is useful for customizing or
filtering out parts of a preset.

```ts
import { defineConfig } from '@pandacss/dev'

export default defineConfig({
  // ...
  hooks: {
    'preset:resolved': ({ utils, preset, name }) => {
      if (name === '@pandacss/preset-panda') {
        return utils.omit(preset, ['theme.tokens.colors', 'theme.semanticTokens.colors'])
      }
      return preset
    }
  }
})
```

### Configuring JSX extraction

Use the `matchTag` / `matchTagProp` functions to customize the way Panda extracts your JSX.

This can be especially useful when working with libraries that have properties that look like CSS properties but are not
and should be ignored.

Let's see a Radix UI example where the `Select.Content` component has a `position` property that should be ignored:

```js
// Here, the `position` property will be extracted because `position` is a valid CSS property, but we don't want that
<Select.Content position="popper" sideOffset={5}>
```

```ts
export default defineConfig({
  // ...
  hooks: {
    'parser:before': ({ configure }) => {
      configure({
        // ignore the Select.Content entirely
        matchTag: tag => tag !== 'Select.Content',
        // ...or specifically ignore the `position` property
        matchTagProp: (tag, prop) => tag === 'Select.Content' && prop !== 'position'
      })
    }
  }
})
```

### Remove unused variables from final css

Here's an example of how to transform the generated css in the `cssgen:done` hook.

```ts file="panda.config.ts"
import { defineConfig } from '@pandacss/dev'
import { removeUnusedCssVars } from './remove-unused-css-vars'
import { removeUnusedKeyframes } from './remove-unused-keyframes'

export default defineConfig({
  // ...
  hooks: {
    'cssgen:done': ({ artifact, content }) => {
      if (artifact === 'styles.css') {
        return removeUnusedCssVars(removeUnusedKeyframes(content))
      }
    }
  }
})
```

Get the snippets for the removal logic from our Github Sandbox in the
[remove-unused-css-vars](https://github.com/chakra-ui/panda/blob/main/sandbox/vite-ts/remove-unused-css-vars.ts) and
[remove-unused-keyframes](https://github.com/chakra-ui/panda/blob/main/sandbox/vite-ts/remove-unused-keyframes.ts)
files.

> Note: Using this means you can't use the JS function [`token.var`](/docs/guides/dynamic-styling#using-tokenvar) (or
> [token(xxx)](/docs/guides/dynamic-styling#using-token) where `xxx` is the path to a
> [semanticToken](/docs/theming/tokens#semantic-tokens)) from `styled-system/tokens` as the CSS variables will be
> removed based on the usage found in the generated CSS

## Sharing hooks

Hooks can be shared as a snippet or as a `plugin`. Plugins are currently simple objects that contain a `name` associated
with a `hooks` object with the same structure as the `hooks` object in the config.

> Plugins differ from `presets` as they can't be extended, but they will be called in sequence in the order they are
> defined in the `plugins` array, with the user's config called last.

```ts
import { defineConfig } from '@pandacss/dev'

export default defineConfig({
  // ...
  plugins: [
    {
      name: 'token-format',
      hooks: {
        'tokens:created': ({ configure }) => {
          configure({
            formatTokenName: path => '$' + path.join('-')
          })
        }
      }
    }
  ]
})
```

## Reference

```ts
export interface PandaHooks {
  /**
   * Called when the config is resolved, after all the presets are loaded and merged.
   * This is the first hook called, you can use it to tweak the config before the context is created.
   */
  'config:resolved': (args: ConfigResolvedHookArgs) => MaybeAsyncReturn<void | ConfigResolvedHookArgs['config']>
  /**
   * Called when a preset is resolved, allowing you to modify it before it's merged into the config.
   */
  'preset:resolved': (args: PresetResolvedHookArgs) => MaybeAsyncReturn<void | PresetResolvedHookArgs['preset']>
  /**
   * Called when the token engine has been created
   */
  'tokens:created': (args: TokenCreatedHookArgs) => MaybeAsyncReturn
  /**
   * Called when the classname engine has been created
   */
  'utility:created': (args: UtilityCreatedHookArgs) => MaybeAsyncReturn
  /**
   * Called when the Panda context has been created and the API is ready to be used.
   */
  'context:created': (args: ContextCreatedHookArgs) => void
  /**
   * Called when the config file or one of its dependencies (imports) has changed.
   */
  'config:change': (args: ConfigChangeHookArgs) => MaybeAsyncReturn
  /**
   * Called after reading the file content but before parsing it.
   * You can use this hook to transform the file content to a tsx-friendly syntax so that Panda's parser can parse it.
   * You can also use this hook to parse the file's content on your side using a custom parser, in this case you don't have to return anything.
   */
  'parser:before': (args: ParserResultBeforeHookArgs) => string | void
  /**
   * Called after the file styles are extracted and processed into the resulting ParserResult object.
   * You can also use this hook to add your own extraction results from your custom parser to the ParserResult object.
   */
  'parser:after': (args: ParserResultAfterHookArgs) => void
  /**
   * Called right before writing the codegen files to disk.
   * You can use this hook to tweak the codegen files before they are written to disk.
   */
  'codegen:prepare': (args: CodegenPrepareHookArgs) => MaybeAsyncReturn<Artifact[]>
  /**
   * Called after the codegen is completed
   */
  'codegen:done': (args: CodegenDoneHookArgs) => MaybeAsyncReturn
  /**
   * Called right before adding the design-system CSS (global, static, preflight, tokens, keyframes) to the final CSS
   * Called right before writing/injecting the final CSS (styles.css) that contains the design-system CSS and the parser CSS
   * You can use it to tweak the CSS content before it's written to disk or injected through the postcss plugin.
   */
  'cssgen:done': (args: CssgenDoneHookArgs) => string | void
}
```


---


## JSX Style Context

JSX Style Context provides an ergonomic way to style compound components with slot recipes.

It uses a context-based approach to distribute recipe styles across multiple child components, making it easier to style
headless UI libraries like Ark UI, and Radix UI.

## Atomic Slot Recipe

- Create a slot recipe using the `sva` function
- Pass the slot recipe to the `createStyleContext` function
- Use the `withProvider` and `withContext` functions to create compound components

```tsx
// components/ui/card.tsx

import { sva } from 'styled-system/css'
import { createStyleContext } from 'styled-system/jsx'

const card = sva({
  slots: ['root', 'label'],
  base: {
    root: {},
    label: {}
  },
  variants: {
    size: {
      sm: { root: {} },
      md: { root: {} }
    }
  },
  defaultVariants: {
    size: 'sm'
  }
})

const { withProvider, withContext } = createStyleContext(card)

const Root = withProvider('div', 'root')
const Label = withContext('label', 'label')

export const Card = {
  Root,
  Label
}
```

Then you can use the `Root` and `Label` components to create a card.

```tsx
// app/page.tsx

import { Card } from './components/ui/card'

export default function App() {
  return (
    <Card.Root>
      <Card.Label>Hello</Card.Label>
    </Card.Root>
  )
}
```

## Config Slot Recipe

The `createStyleContext` function can also be used with slot recipes defined in the `panda.config.ts` file.

- Pass the config recipe to the `createStyleContext` function
- Use the `withProvider` and `withContext` functions to create compound components

```tsx
// components/ui/card.tsx

import { card } from '../styled-system/recipes'
import { createStyleContext } from 'styled-system/jsx'

const { withProvider, withContext } = createStyleContext(card)

const Root = withProvider('div', 'root')
const Label = withContext('label', 'label')

export const Card = {
  Root,
  Label
}
```

Then you can use the `Root` and `Label` components to create a card.

```tsx
// app/page.tsx

import { Card } from './components/ui/card'

export default function App() {
  return (
    <Card.Root>
      <Card.Label>Hello</Card.Label>
    </Card.Root>
  )
}
```

## createStyleContext

This function is a factory function that returns three functions: `withRootProvider`, `withProvider`, and `withContext`.

### withRootProvider

Creates the root component that provides the style context. Use this when the root component **does not render an
underlying DOM element**.

```tsx
import { Dialog } from '@ark-ui/react'

//...

const DialogRoot = withRootProvider(Dialog.Root)
```

### withProvider

Creates a component that both provides context and applies the root slot styles. Use this when the root component
**renders an underlying DOM element**.

> **Note:** It requires the root `slot` parameter to be passed.

```tsx
import { Avatar } from '@ark-ui/react'

//...

const AvatarRoot = withProvider(Avatar.Root, 'root')
```

### withContext

Creates a component that consumes the style context and applies slot styles. It does not accept variant props directly,
but gets them from context.

```tsx
import { Avatar } from '@ark-ui/react'

//...

const AvatarImage = withContext(Avatar.Image, 'image')
const AvatarFallback = withContext(Avatar.Fallback, 'fallback')
```

### unstyled prop

Every component created with `createStyleContext` supports the `unstyled` prop to disable styling. It is useful when you
want to opt-out of the recipe styles.

- When applied the root component, will disable all styles
- When applied to a child component, will disable the styles for that specific slot

```tsx
// Removes all styles
<AvatarRoot unstyled>
  <AvatarImage />
  <AvatarFallback />
</AvatarRoot>

// Removes only the styles for the image slot
<AvatarRoot>
  <AvatarImage unstyled css={{ bg: 'red' }} />
  <AvatarFallback />
</AvatarRoot>
```

## Guides

### Config Recipes

The rules of config recipes still applies when using `createStyleContext`. Ensure the name of the final component
matches the name of the recipe.

> If you want to use a custom name, you can configure the recipe's `jsx` property in the `panda.config.ts` file.

```tsx
// recipe name is "card"
import { card } from '../styled-system/recipes'

const { withRootProvider, withContext } = createStyleContext(card)

const Root = withRootProvider('div')
const Header = withContext('header', 'header')
const Body = withContext('body', 'body')

// The final component name must be "Card"
export const Card = {
  Root,
  Header,
  Body
}
```

### Default Props

Use `defaultProps` option to provide default props to the component.

```tsx
const { withContext } = createStyleContext(card)

export const CardHeader = withContext('header', 'header', {
  defaultProps: {
    role: 'banner'
  }
})
```


---


## Merging Styles

Learn how to merge multiple styles without conflicts.

## Merging `css` objects

You can merge multiple style objects together using the `css` function.

```js
import { css } from 'styled-system/css'

const style1 = {
  bg: 'red',
  color: 'white'
}

const style2 = {
  bg: 'blue'
}

const className = css(style1, style2) // => 'bg_blue text_white'
```

In some cases though, the style object might not be colocated in the same file as the component. In this case, you can
use the `css.raw` function to preserve the original style object.

> All `.raw(...)` signatures are identity functions that return the same value as the input, but serve as a hint to the
> compiler that the value is a style object.

```js
// style.js
import { css } from 'styled-system/css'

export const style1 = css.raw({
  bg: 'red',
  color: 'white'
})

// component.js
import { css } from 'styled-system/css'
import { style1 } from './style.js'

const style2 = css.raw({
  bg: 'blue'
})

const className = css(style1, style2) // => 'bg_blue text_white'
```

## Spreading `css.raw` objects

> **Added in v1.6.1**

You can also spread `css.raw` objects within style declarations. This is particularly useful for reusing styles in
nested selectors, conditions, and complex compositions:

### Child selectors

```js
import { css } from 'styled-system/css'

const baseStyles = css.raw({ margin: 0, padding: 0 })

const component = css({
  '& p': { ...baseStyles, fontSize: '1rem' },
  '& h1': { ...baseStyles, fontSize: '2rem' }
})
```

### Nested conditions

```js
import { css } from 'styled-system/css'

const interactive = css.raw({ cursor: 'pointer', transition: 'all 0.2s' })

const card = css({
  _hover: {
    ...interactive,
    _dark: { ...interactive, color: 'white' }
  }
})
```

## Merging `cva` + `css` styles

The same technique can be used to merge an atomic `cva` recipe and a style object.

```js
import { css, cx, cva } from 'styled-system/css'

const overrideStyles = css.raw({
  bg: 'red',
  color: 'white'
})

const buttonStyles = cva({
  base: {
    bg: 'blue',
    border: '1px solid black'
  },
  variants: {
    size: {
      small: { fontSize: '12px' }
    }
  }
})

const className = css(
  // returns the resolved style object
  buttonStyles.raw({ size: 'small' }),
  // add the override styles
  overrideStyles
)

// => 'bg_red border_1px_solid_black color_white font-size_12px'
```

## Merging `sva` + `css` styles

The same technique can be used to merge an atomic `sva` recipe and a style object.

```js
import { css, sva } from 'styled-system/css'

const overrideStyles = css.raw({
  bg: 'red',
  color: 'white'
})

const buttonStyles = sva({
  slots: ['root']
  base: {
    root: {
      bg: 'blue',
      border: '1px solid black'
    }
  },
  variants: {
    size: {
      root: {
        small: { fontSize: '12px' }
      }
    }
  }
})

// returns the resolved style object for all slots
const { root } = buttonStyles.raw({ size: 'small' })

const className = css(
  root,
  // add the override styles
  overrideStyles
)

// => 'bg_red border_1px_solid_black color_white font-size_12px'
```

## Merging config recipe and style object

Due to the fact that the generated styles of a config recipe are saved in the `@layer recipe` cascade layer, they can be
overridden with any atomic styles. Use the `cx` function to achieve that.

> The `utilties` layer has more precedence than the `recipe` layer.

```js
import { css, cx } from 'styled-system/css'
import { button } from 'styled-system/recipes'

const className = cx(
  // returns the resolved class name: `button button--size-small`
  button({ size: 'small' }),
  // add the override styles
  css({ bg: 'red' }) // => 'bg_red'
)

// => 'button button--size-small bg_red'
```

## Merging within JSX component

Using these techniques, you can apply them to a component by exposing a `css` prop and merge with local styles.

> **Note:** For this to work, Panda requires that you set `jsxFramework` config option to `react`

```jsx
const cardStyles = css.raw({
  bg: 'red',
  color: 'white'
})

function Card({ title, description, css: cssProp }) {
  return (
    // merge the `cardStyles` with the `cssProp` passed in
    <div className={css(cardStyles, cssProp)}>
      <h1>{title}</h1>
      <p>{description}</p>
    </div>
  )
}

// usage
function Demo() {
  return <Card title="Hello World" description="This is a card component" css={{ bg: 'blue' }} />
}
```

If you use any other prop name other than `css`, then you must use the `css.raw(...)` function to ensure Panda extracts
the style object.

```jsx
const cardStyles = css.raw({
  bg: 'red',
  color: 'white'
})

function Card({ title, description, style }) {
  return (
    // merge the `cardStyles` with the `style` passed in
    <div className={css(cardStyles, style)}>
      <h1>{title}</h1>
      <p>{description}</p>
    </div>
  )
}

// usage
function Demo() {
  return (
    <Card
      title="Hello World"
      description="This is a card component"
      // use `css.raw(...)` to ensure Panda extracts the style object
      style={css.raw({ bg: 'blue' })}
    />
  )
}
```


---


## Patterns

Patterns are layout primitives that can be used to create robust and responsive layouts with ease. Panda comes with predefined patterns like stack, hstack, vstack, wrap, etc. These patterns can be used as functions or JSX elements.

Think of patterns as a set of predefined styles to reduce repetition and improve readability. You can override the
properties as needed, just like in the `css` function.

## Creating Patterns

To learn how to create patterns, check out the [customization](/docs/customization/patterns) section.

## Predefined Patterns

### Box

The Box pattern does not contain any additional styles. With its function form it's the equivalent of the `css`
function. It can be useful with its JSX form and is the equivalent of a `styled.div` component, serving mostly to get
style props available in JSX.

```tsx
import { Box } from '../styled-system/jsx'

function App() {
  return (
    <Box color="blue.300">
      <div>Cool !</div>
    </Box>
  )
}
```

### Container

The Container pattern is used to create a container with a max-width and center the content.

By default, the container sets the following properties:

- `maxWidth: 8xl`
- `marginX: auto`
- `position: relative`
- `paddingX: { base: 4, md: 6, lg: 8 }`

<Tabs items={['Function', 'JSX']}>
<Tab>

```tsx
import { container } from '../styled-system/patterns'

function App() {
  return (
    <div className={container()}>
      <div>First</div>
      <div>Second</div>
      <div>Third</div>
    </div>
  )
}
```

  </Tab>
  <Tab>

```tsx
import { Container } from '../styled-system/jsx'

function App() {
  return (
    <Container>
      <div>First</div>
      <div>Second</div>
      <div>Third</div>
    </Container>
  )
}
```

  </Tab>
</Tabs>

### Stack

The Stack pattern is a layout primitive that can be used to create a vertical or horizontal stack of elements.

The `stack` function accepts the following properties:

- `direction`: An alias for the css `flex-direction` property. Default is `column`.
- `gap`: The gap between the elements in the stack.
- `align`: An alias for the css `align-items` property.
- `justify`: An alias for the css `justify-content` property.

<Tabs items={['Function', 'JSX']}>
<Tab>

```tsx
import { stack } from '../styled-system/patterns'

function App() {
  return (
    <div className={stack({ gap: '6', padding: '4' })}>
      <div>First</div>
      <div>Second</div>
      <div>Third</div>
    </div>
  )
}
```

  </Tab>
  <Tab>

```tsx
import { Stack } from '../styled-system/jsx'

function App() {
  return (
    <Stack gap="6" padding="4">
      <div>First</div>
      <div>Second</div>
      <div>Third</div>
    </Stack>
  )
}
```

  </Tab>
</Tabs>

#### HStack

The HStack pattern is a wrapper around the `stack` pattern that sets the `direction` property to `horizontal`, and
centers the elements vertically.

<Tabs items={['Function', 'JSX']}>
<Tab>

```tsx
import { hstack } from '../styled-system/patterns'

function App() {
  return (
    <div className={hstack({ gap: '6' })}>
      <div>First</div>
      <div>Second</div>
      <div>Third</div>
    </div>
  )
}
```

  </Tab>
  <Tab>

```tsx
import { HStack } from '../styled-system/jsx'

function App() {
  return (
    <HStack gap="6">
      <div>First</div>
      <div>Second</div>
      <div>Third</div>
    </HStack>
  )
}
```

  </Tab>
</Tabs>

#### VStack

The VStack pattern is a wrapper around the `stack` pattern that sets the `direction` property to `vertical`, and centers
the elements horizontally.

<Tabs items={['Function', 'JSX']}>
<Tab>

```tsx
import { vstack } from '../styled-system/patterns'

function App() {
  return (
    <div className={vstack({ gap: '6' })}>
      <div>First</div>
      <div>Second</div>
      <div>Third</div>
    </div>
  )
}
```

  </Tab>
  <Tab>

```tsx
import { VStack } from '../styled-system/jsx'

function App() {
  return (
    <VStack gap="6">
      <div>First</div>
      <div>Second</div>
      <div>Third</div>
    </VStack>
  )
}
```

  </Tab>
</Tabs>

### Wrap

The Wrap pattern is used to add space between elements and wraps automatically if there isn't enough space.

The `wrap` function accepts the following properties:

- `gap`: The gap between the elements in the stack.
- `columnGap`: The gap between the elements in the stack horizontally.
- `rowGap`: The gap between the elements in the stack vertically.
- `align`: An alias for the css `align-items` property.
- `justify`: An alias for the css `justify-content` property.

<Tabs items={['Function', 'JSX']}>
<Tab>

```tsx
import { wrap } from '../styled-system/patterns'

function App() {
  return (
    <div className={wrap({ gap: '6' })}>
      <div>First</div>
      <div>Second</div>
      <div>Third</div>
    </div>
  )
}
```

  </Tab>
  <Tab>

```tsx
import { Wrap } from '../styled-system/jsx'

function App() {
  return (
    <Wrap gap="6">
      <div>First</div>
      <div>Second</div>
      <div>Third</div>
    </Wrap>
  )
}
```

  </Tab>
</Tabs>

### Aspect Ratio

The Aspect Ratio pattern is used to create a container with a fixed aspect ratio. It is used when displaying images,
maps, videos and other media.

> **Note:** In most cases, we recommend using the `aspectRatio` property instead of the pattern.

The `aspectRatio` function accepts the following properties:

- `ratio`: The aspect ratio of the container. Can be a number or a string.

<Tabs items={['Function', 'JSX']}>
<Tab>

```tsx
import { aspectRatio } from '../styled-system/patterns'

function App() {
  return (
    <div className={aspectRatio({ ratio: 16 / 9 })}>
      <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m1" title="Google map" frameBorder="0" />
    </div>
  )
}
```

  </Tab>
  <Tab>

```tsx
import { AspectRatio } from '../styled-system/jsx'

function App() {
  return (
    <AspectRatio ratio={16 / 9}>
      <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m1" title="Google map" frameBorder="0" />
    </AspectRatio>
  )
}
```

  </Tab>
</Tabs>

### Flex

The Flex pattern is used to create a flex container and provides some shortcuts for the `flex` property.

The `flex` function accepts the following properties:

- `direction`: The flex direction of the container. Can be `row`, `column`, `row-reverse` or `column-reverse`.
- `wrap`: Whether to wrap the flex items. The value is a boolean.
- `align`: An alias for the css `align-items` property.
- `justify`: An alias for the css `justify-content` property.
- `basis`: An alias for the css `flex-basis` property.
- `grow`: An alias for the css `flex-grow` property.
- `shrink`: An alias for the css `flex-shrink` property.

<Tabs items={['Function', 'JSX']}>
<Tab>

```tsx
import { flex } from '../styled-system/patterns'

function App() {
  return (
    <div className={flex({ direction: 'row', align: 'center' })}>
      <div>First</div>
      <div>Second</div>
      <div>Third</div>
    </div>
  )
}
```

  </Tab>
  <Tab>

```tsx
import { Flex } from '../styled-system/jsx'

function App() {
  return (
    <Flex direction="row" align="center">
      <div>First</div>
      <div>Second</div>
      <div>Third</div>
    </Flex>
  )
}
```

  </Tab>
</Tabs>

### Center

The Center pattern is used to center the content of a container.

The `center` function accepts the following properties:

- `inline`: Whether to use `inline-flex` or `flex` for the container. The value is a boolean.

<Tabs items={['Function', 'JSX']}>
<Tab>

```tsx
import { center } from '../styled-system/patterns'

function App() {
  return (
    <div className={center({ bg: 'red.200' })}>
      <Icon />
    </div>
  )
}
```

  </Tab>
  <Tab>

```tsx
import { Center } from '../styled-system/jsx'

function App() {
  return (
    <Center bg="red.200">
      <div>First</div>
      <div>Second</div>
      <div>Third</div>
    </Center>
  )
}
```

  </Tab>
</Tabs>

### LinkOverlay

The link overlay pattern is used to expand a link's clickable area to its nearest parent with `position: relative`.

> We recommend using this pattern when the relative parent contains at most one clickable link.

<Tabs items={['Function', 'JSX']}>
<Tab>

```tsx
import { css } from '../styled-system/css'
import { linkOverlay } from '../styled-system/patterns'

function App() {
  return (
    <div className={css({ pos: 'relative' })}>
      <img src="https://via.placeholder.com/150" alt="placeholder" />
      <a href="#" className={linkOverlay()}>
        View more
      </a>
    </div>
  )
}
```

</Tab>

<Tab>

```tsx
import { Box, LinkOverlay } from '../styled-system/jsx'

function App() {
  return (
    <Box pos="relative">
      <img src="https://via.placeholder.com/150" alt="placeholder" />
      <LinkOverlay href="#">View more</LinkOverlay>
    </Box>
  )
}
```

</Tab>
</Tabs>

### Float

The Float pattern is used to anchor an element to the top, bottom, left or right of the container.

> It requires a parent element with `position: relative` styles.

The `float` function accepts the following properties:

- `placement`: The placement of the element. Can be `top-start`, `top`, `top-end`, `bottom-start`, `bottom`,
  `bottom-end`, `left-start`, `left`, `left-end`, `right-start`, `right` or `right-end`.
- `offset`: The offset of the element from the edge of the container. Can be a number or a string.
- `offsetX`: Same as `offset`, but only for the horizontal axis.
- `offsetY`: Same as `offset`, but only for the vertical axis.

<Tabs items={['Function', 'JSX']}>
<Tab>

```tsx
import { css } from '../styled-system/css'
import { float } from '../styled-system/patterns'

function App() {
  return (
    <div className={css({ position: 'relative' })}>
      <div className={float({ placement: 'top-start' })}>3</div>
    </div>
  )
}
```

  </Tab>
  <Tab>

```tsx
import { css } from '../styled-system/css'
import { Float } from '../styled-system/jsx'

function App() {
  return (
    <div className={css({ position: 'relative' })}>
      <Float placement="top-start">3</Float>
    </div>
  )
}
```

  </Tab>
</Tabs>

### Grid

The Grid pattern is used to create a grid layout.

The `grid` function accepts the following properties:

- `columns`: The number of columns in the grid.
- `gap`: The gap between the elements in the stack.
- `columnGap`: The gap between the elements in the stack horizontally.
- `rowGap`: The gap between the elements in the stack vertically.
- `minChildWidth`: The minimum width of the child elements before wrapping (must not be used with `columns`).

<Tabs items={['Function', 'JSX']}>
<Tab>

```tsx
import { grid } from '../styled-system/patterns'

function App() {
  return (
    <div className={grid({ columns: 3, gap: '6' })}>
      <div>First</div>
      <div>Second</div>
      <div>Third</div>
    </div>
  )
}
```

  </Tab>
  <Tab>

```tsx
import { Grid } from '../styled-system/jsx'

function App() {
  return (
    <Grid columns={3} gap="6">
      <div>First</div>
      <div>Second</div>
      <div>Third</div>
    </Grid>
  )
}
```

  </Tab>
</Tabs>

#### Grid Item

The Grid Item pattern is used to style the children of a grid container.

The `gridItem` function accepts the following properties:

- `colSpan`: The number of columns the item spans.
- `rowSpan`: The number of rows the item spans.
- `rowStart`: The row the item starts at.
- `rowEnd`: The row the item ends at.
- `colStart`: The column the item starts at.
- `colEnd`: The column the item ends at.

<Tabs items={['Function', 'JSX']}>
<Tab>

```tsx
import { grid, gridItem } from '../styled-system/patterns'

function App() {
  return (
    <div className={grid({ columns: 3, gap: '6' })}>
      <div className={gridItem({ colSpan: 2 })}>First</div>
      <div>Second</div>
      <div>Third</div>
    </div>
  )
}
```

  </Tab>
  <Tab>

```tsx
import { Grid, GridItem } from '../styled-system/jsx'

function App() {
  return (
    <Grid columns={3} gap="6">
      <GridItem colSpan={2}>First</GridItem>
      <GridItem>Second</GridItem>
      <GridItem>Third</GridItem>
    </Grid>
  )
}
```

  </Tab>
</Tabs>

### Divider

The Divider pattern is used to create a horizontal or vertical divider.

The `divider` function accepts the following properties:

- `orientation`: The orientation of the divider. Can be `horizontal` or `vertical`.
- `thickness`: The thickness of the divider. Can be a sizing token, or arbitrary value.
- `color`: The color of the divider. Can be a color token, or arbitrary value.

<Tabs items={['Function', 'JSX']}>
<Tab>

```tsx
import { divider, stack } from '../styled-system/patterns'

function App() {
  return (
    <div className={stack()}>
      <button>First</button>
      <div className={divider({ orientation: 'horizontal' })} />
      <button>Second</button>
    </div>
  )
}
```

  </Tab>
  <Tab>

```tsx
import { Divider, Stack } from '../styled-system/jsx'

function App() {
  return (
    <Stack>
      <button>First</button>
      <Divider orientation="horizontal" />
      <button>Second</button>
    </Stack>
  )
}
```

  </Tab>
</Tabs>

### Circle

The Circle pattern is used to create a circle.

The `circle` function accepts the following properties:

- `size`: The size of the circle. Can be a sizing token, or arbitrary value.

<Tabs items={['Function', 'JSX']}>
<Tab>

```tsx
import { circle } from '../styled-system/patterns'

function App() {
  return <div className={circle({ size: '12', bg: 'red.300' })} />
}
```

  </Tab>
  <Tab>

```tsx
import { Circle } from '../styled-system/jsx'

function App() {
  return <Circle size="12" bg="red.300" />
}
```

  </Tab>
</Tabs>

### Square

The Square pattern is used to create a square with equal width and height.

The `square` function accepts the following properties:

- `size`: The size of the square. Can be a sizing token, or arbitrary value.

<Tabs items={['Function', 'JSX']}>
<Tab>

```tsx
import { square } from '../styled-system/patterns'

function App() {
  return <div className={square({ size: '12', bg: 'red.300' })} />
}
```

  </Tab>
  <Tab>

```tsx
import { Square } from '../styled-system/jsx'

function App() {
  return <Square size="12" bg="red.300" />
}
```

  </Tab>
</Tabs>

### Visually Hidden

The Visually Hidden pattern is used to hide an element visually, but keep it accessible to screen readers.

```tsx
import { visuallyHidden } from '../styled-system/patterns'

export function Checkbox() {
  return (
    <label>
      <input type="checkbox" className={visuallyHidden()}>
        I'm hidden
      </input>
      <span>Checkbox</span>
    </label>
  )
}
```

### Bleed

The Bleed pattern is used to create a full width element by negating the padding applied to its parent container.

The `bleed` function accepts the following properties:

- `inline`: The amount of padding to negate on the horizontal axis. Should match the parent's padding.
- `block`: The amount of padding to negate on the vertical axis. Should match the parent's padding.

<Tabs items={['Function', 'JSX']}>
  <Tab>

```tsx
import { css } from '../styled-system/css'
import { bleed } from '../styled-system/patterns'

export function Page() {
  return (
    <div className={css({ px: '6' })}>
      <div className={bleed({ inline: '6' })}>Welcome</div>
    </div>
  )
}
```

  </Tab>
  <Tab>

```tsx
import { css } from '../styled-system/css'
import { Bleed } from '../styled-system/jsx'

export function Page() {
  return (
    <div className={css({ px: '6' })}>
      <Bleed inline="6">Welcome</div>
    </div>
  )
}
```

  </Tab>
</Tabs>

### cq (Container Query)

To make it easier to use container queries, we've added a new `cq` pattern to `@pandacss/preset-base`. It is used to
apply styles based on the width of the container.

The `cq` function accepts the following properties:

- `name`: The name of the container query, Maps to the
  [`containerName` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/container-name).
- `type`: The type of the container query. Maps to the
  [`containerType` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/container-type). Defaults to
  `inline-size`.

```ts
import { cq } from 'styled-system/patterns'

function Demo() {
  return (
    <nav className={cq()}>
      <div
        className={css({
          fontSize: { base: 'lg', '@/sm': 'md' },
        })}
      />
    </nav>
  )
}
```

You can also named container queries:

```tsx
// 1 - Define container conditions

export default defineConfig({
  // ...
  theme: {
    containerNames: ['sidebar', 'content'],
    containerSizes: {
      xs: '40em',
      sm: '60em',
      md: '80em'
    }
  }
})
```

```tsx
// 2 - Automatically generate container query pattern

import { cq } from 'styled-system/patterns'

function Demo() {
  return (
    <nav className={cq({ name: 'sidebar' })}>
      <div
        className={css({
          // When the sidebar container reaches the `sm` size
          // change font size to `md`
          fontSize: { base: 'lg', '@sidebar/sm': 'md' }
        })}
      />
    </nav>
  )
}
```

Read more about container queries [here](/docs/concepts/conditional-styles#container-queries).

## Usage with JSX

To use the pattern in JSX, you need to set the `jsxFramework` property in the config. When this is set, Panda will emit
files for JSX elements based on the framework.

Every pattern can be used as a JSX element and imported from the `/jsx` entrypoint. By default, the pattern name is the
function name in PascalCase. You can override both the component name (with the `jsx` config property) and the element
rendered (with the `jsxElement` config property).

Learn more about pattern customization [here](/docs/customization/patterns).

```tsx
import { VStack, Center } from '../styled-system/jsx'

function App() {
  return (
    <VStack gap="6" mt="4">
      <div>First</div>
      <div>Second</div>
      <div>Third</div>
      <Center>4</Center>
    </VStack>
  )
}
```

### Advanced JSX Tracking

We recommend that you use the pattern functions in most cases, in design systems there might be a need to compose
existing components to create new components.

To track the usage of the patterns in these cases, you'll need to add the `jsx` hint for the pattern config

```js {12} filename="button.pattern.ts"
import { definePattern } from '@pandacss/dev'

const scrollable = definePattern({
  // ...
  // Add the jsx hint to track the usage of the pattern in JSX, you can also use a regex to match multiple components
  jsx: ['Scrollable', 'PageScrollable']
})
```

Then you can create a new component that uses the `PageScrollable` component and Panda will track the usage of the
`scrollable` pattern as well.

```tsx
const PageScrollable = (props: ButtonProps) => {
  const { children, size } = props
  return (
    <Scrollable {...props} size={size}>
      {children}
    </Scrollable>
  )
}
```


---


## Recipes

Panda provides a way to write CSS-in-JS with better performance, developer experience, and composability.

Recipes are a way to create multi-variant styles with a type-safe runtime API.

A recipe consists of four properties:

- `base`: The base styles for the component
- `variants`: The different visual styles for the component
- `compoundVariants`: The different combinations of variants for the component
- `defaultVariants`: The default variant values for the component

> **Credit:** This API was inspired by [Stitches](https://stitches.dev/),
> [Vanilla Extract](https://vanilla-extract.style/), and [Class Variance Authority](https://cva.style/).

[Comparison table between the different types of recipes here: "Should I use atomic or config recipes ?"](/docs/concepts/recipes#should-i-use-atomic-or-config-recipes-)

## Atomic Recipe (or cva)

Atomic recipes are a way to create multi-variant atomic styles with a type-safe runtime API.

They are defined using the `cva` function which was inspired by [Class Variance Authority](https://cva.style/). The
`cva` function which takes an object as its argument.

> **Note:** `cva` is not the same as [Class Variance Authority](https://cva.style/). The `cva` from Panda is a
> purpose-built function for creating atomic recipes that are connected to your design tokens and utilities.

### Defining the recipe

```jsx
import { cva } from '../styled-system/css'

const button = cva({
  base: {
    display: 'flex'
  },
  variants: {
    visual: {
      solid: { bg: 'red.200', color: 'white' },
      outline: { borderWidth: '1px', borderColor: 'red.200' }
    },
    size: {
      sm: { padding: '4', fontSize: '12px' },
      lg: { padding: '8', fontSize: '24px' }
    }
  }
})
```

### Using the recipe

The returned value from the `cva` function is a function that can be used to apply the recipe to a component. Here's an
example of how to use the `button` recipe:

```jsx
import { button } from './button'

const Button = () => {
  return <button className={button({ visual: 'solid', size: 'lg' })}>Click Me</button>
}
```

When a recipe is created, Panda will extract and generate CSS for every variant and compoundVariant `css` ahead of time,
as atomic classes.

```css
@layer utilities {
  .d_flex {
    display: flex;
  }

  .bg_red_200 {
    background-color: #fed7d7;
  }

  .color_white {
    color: #fff;
  }

  .border_width_1px {
    border-width: 1px;
  }
  /* ... */
}
```

### Setting the default variants

The `defaultVariants` property is used to set the default variant values for the recipe. This is useful when you want to
apply a variant by default. Here's an example of how to use `defaultVariants`:

```jsx
import { cva } from '../styled-system/css'

const button = cva({
  base: {
    display: 'flex'
  },
  variants: {
    visual: {
      solid: { bg: 'red.200', color: 'white' },
      outline: { borderWidth: '1px', borderColor: 'red.200' }
    },
    size: {
      sm: { padding: '4', fontSize: '12px' },
      lg: { padding: '8', fontSize: '24px' }
    }
  },
  defaultVariants: {
    visual: 'solid',
    size: 'lg'
  }
})
```

### Compound Variants

Compound variants are a way to combine multiple variants together to create more complex sets of styles. They are
defined using the `compoundVariants` property , which takes an array of objects as its argument. Each object in the
array represents a set of conditions that must be met in order for the corresponding styles to be applied.

Here's an example of how to use `compoundVariants` in Panda:

```js
import { cva } from '../styled-system/css'

const button = cva({
  base: {
    padding: '8px 16px',
    borderRadius: '4px',
    fontSize: '16px',
    fontWeight: 'bold'
  },

  variants: {
    size: {
      small: {
        fontSize: '14px',
        padding: '4px 8px'
      },
      medium: {
        fontSize: '16px',
        padding: '8px 16px'
      },
      large: {
        fontSize: '18px',
        padding: '12px 24px'
      }
    },
    color: {
      primary: {
        backgroundColor: 'blue',
        color: 'white'
      },
      secondary: {
        backgroundColor: 'gray',
        color: 'black'
      }
    },
    disabled: {
      true: {
        opacity: 0.5,
        cursor: 'not-allowed'
      }
    }
  },

  // compound variants
  compoundVariants: [
    // apply when both small size and primary color are selected
    {
      size: 'small',
      color: 'primary',
      css: {
        border: '2px solid blue'
      }
    },
    // apply when both large size and secondary color are selected and the button is disabled
    {
      size: 'large',
      color: 'secondary',
      disabled: true,
      css: {
        backgroundColor: 'lightgray',
        color: 'darkgray',
        border: 'none'
      }
    },
    // apply when both small or medium size, and secondary color variants are applied
    {
      size: ['small', 'medium'],
      color: 'secondary',
      css: {
        fontWeight: 'extrabold'
      }
    }
  ]
})
```

Here's an example usage of the `button` recipe:

```jsx
import { button } from './button'

const Button = () => {
  // will apply size: small, color: primary, css: { border: '2px solid blue' }
  return <button className={button({ size: 'small', color: 'primary' })}>Click Me</button>
}
```

Overall, using compound variants allows you to create more complex sets of styles that can be applied to your components
based on multiple conditions.

By combining simple variants together in this way, you can create a wide range of visual styles without cluttering up
your code with lots of conditional logic.

### TypeScript Guide

Panda provides a `RecipeVariantProps` type utility that can be used to infer the variant properties of a recipe.

This is useful when you want to use the recipe in JSX and want to get type safety for the variants.

```tsx
import { styled } from '../styled-system/jsx'
import { cva, type RecipeVariantProps } from '../styled-system/css'

const buttonStyle = cva({
  base: {
    color: 'red',
    textAlign: 'center'
  },
  variants: {
    size: {
      small: {
        fontSize: '1rem'
      },
      large: {
        fontSize: '2rem'
      }
    }
  }
})

export type ButtonVariants = RecipeVariantProps<typeof buttonStyle> // { size?: 'small' | 'large' }

export const Button = styled('button', buttonStyle)
```

### Usage in JSX

You can create a JSX component from any existing atomic recipe by using the `styled` function from the `/jsx`
entrypoint.

The `styled` function takes the element type as its first argument, and the recipe as its second argument.

> Make sure to add the `jsxFramework` option to your `panda.config` file, and run `panda codegen` to generate the JSX
> entrypoint.

```js
import { cva } from '../styled-system/css'
import { styled } from '../styled-system/jsx'

const buttonStyle = cva({
  base: {
    color: 'red',
    textAlign: 'center'
  },
  variants: {
    size: {
      small: {
        fontSize: '1rem'
      },
      large: {
        fontSize: '2rem'
      }
    }
  }
})

const Button = styled('button', buttonStyle)
```

Then you can use the component in JSX

```jsx
<Button size="large">Click me</Button>
```

## Config Recipe

Config recipes are extracted and generated just in time, this means regardless of the number of recipes in the config,
only the recipes and variants you use will exist in the generated CSS.

The config recipe takes the following additional properties:

- `className`: The name of the recipe. Used in the generated class name
- `jsx`: An array of JSX components that use the recipe. Defaults to the uppercase version of the recipe name
- `description`: An optional description of the recipe (used in the js-doc comments)

> As of v0.9, the `name` property is removed in favor of `className`

### Defining the recipe

To define a config recipe, import the `defineRecipe` helper function

```jsx filename="button.recipe.ts"
import { defineRecipe } from '@pandacss/dev'

export const buttonRecipe = defineRecipe({
  className: 'button',
  description: 'The styles for the Button component',
  base: {
    display: 'flex'
  },
  variants: {
    visual: {
      funky: { bg: 'red.200', color: 'white' },
      edgy: { border: '1px solid {colors.red.500}' }
    },
    size: {
      sm: { padding: '4', fontSize: '12px' },
      lg: { padding: '8', fontSize: '40px' }
    },
    shape: {
      square: { borderRadius: '0' },
      circle: { borderRadius: 'full' }
    }
  },
  defaultVariants: {
    visual: 'funky',
    size: 'sm',
    shape: 'circle'
  }
})
```

### Adding recipe to config

To add the recipe to the config, you’d need to add it to the `theme.recipes` object.

```jsx filename="panda.config.ts"
import { defineConfig } from '@pandacss/dev'
import { buttonRecipe } from './button.recipe'

export default defineConfig({
  //...
  jsxFramework: 'react',
  theme: {
    extend: {
      recipes: {
        button: buttonRecipe
      }
    }
  }
})
```

### Generate JS code

This generates a recipes folder the specified `outdir` which is `styled-system` by default. If Panda doesn’t
automatically generate your CSS file, you can run the `panda codegen` command.

You only need to import the recipes into the component files where you need to use them.

### Using the recipe

To use the recipe, you can import the recipe from the `<outdir>/recipes` entrypoint and use it in your component. Panda
tracks the usage of the recipe and only generates CSS of the variants used in your application.

```js
import { button } from '../styled-system/recipes'

function App() {
  return (
    <div>
      <button className={button()}>Click me</button>
      <button className={button({ shape: 'circle' })}>Click me</button>
    </div>
  )
}
```

The generated css is registered under the `recipe` [cascade layer](/docs/concepts/cascade-layers.mdx) with the class
name that matches the recipe-variant name pattern `<recipe-className>--<variant-name>`.

> **Technical Notes 📝:** Only the recipe and variants used in your application are generated. Not more!

```css
@layer recipes {
  @layer base {
    .button {
      font-size: var(--font-sizes-lg);
    }
  }

  .button--visual-funky {
    background-color: var(--colors-red-200);
    color: var(--colors-white);
  }

  .button--size-lg {
    padding: var(--space-8);
    font-size: var(--font-sizes-40px);
  }
}
```

### Responsive and Conditional variants

Recipes created in the config have a **special** feature; they can be applied based on a specific breakpoints or
conditions.

Here's how to tweak the size variant of the button recipe based on breakpoints.

```jsx
import { button } from '../styled-system/recipes'

function App() {
  return (
    <div>
      <button className={button({ size: { base: 'sm', md: 'lg' } })}>Click me</button>
    </div>
  )
}
```

> In most cases, we don't recommend applying conditional variants inline. Ideally, you might want to render different
> views for your responsive breakpoints.

### TypeScript Guide

Every recipe ships a type interface for its accepted variants. You can import them from the `styled-system/recipes`
entrypoint.

For the button recipe, we can import the `ButtonVariants` type like so:

```ts
import React from 'react'
import type { ButtonVariants } from '../styled-system/recipes'

type ButtonProps = ButtonVariants & {
  children: React.ReactNode
}
```

### Usage in JSX

Layer recipes can be consumed directly in your custom JSX components. Panda will automatically track the usage of the
recipe if the component name matches the recipe name.

For example, if your recipe is called `button` and you create a `Button` component from it, Panda will automatically
track the usage of the variant properties.

```tsx
import React from 'react'
import { button, type ButtonVariants } from '../styled-system/recipes'

type ButtonProps = ButtonVariants & {
  children: React.ReactNode
}

const Button = (props: ButtonProps) => {
  const { children, size } = props
  return (
    <button {...props} className={button({ size })}>
      {children}
    </button>
  )
}

const App = () => {
  return (
    <div>
      <Button size="lg">Click me</Button>
    </div>
  )
}
```

### Advanced JSX Tracking

We recommend that you use the recipe functions in most cases, in design systems there might be a need to compose
existing components (like Button) to create new components.

To track the usage of the recipes in these cases, you'll need to add the `jsx` hint for the recipe config

```js {12} filename="button.recipe.ts"
import { defineRecipe } from '@pandacss/dev'

const button = defineRecipe({
  base: {
    color: 'red',
    fontSize: '1.5rem'
  },
  variants: {
    // ...
  },
  // Add the jsx hint to track the usage of the recipe in JSX, you can use regex to match multiple components
  jsx: ['Button', 'PageButton']
})
```

Then you can create a new component that uses the `Button` component and Panda will track the usage of the `button`
recipe as well.

```tsx
const PageButton = (props: ButtonProps) => {
  const { children, size } = props
  return (
    <Button {...props} size={size}>
      {children}
    </Button>
  )
}
```

#### Extending a preset recipe

If you're using a recipe from a preset, you can still extend it in your config.

```js
import { defineConfig } from '@pandacss/dev'

export default defineConfig({
  //...
  jsxFramework: 'react',
  theme: {
    extend: {
      recipes: {
        button: {
          className: 'something-else', // 👈 override the className
          base: {
            color: 'red', // 👈 replace some part of the recipe
            fontSize: '1.5rem' // or add new styles
          },
          variants: {
            // ... // 👈 add or extend new variants
          },
          jsx: ['Button', 'PageButton'] // 👈 extend the jsx tracking hint
        }
      }
    }
  }
})
```

Learn more about the [extend](/docs/concepts/extend.md) keyword.

## Methods and Properties

Both atomic and config recipe ships a helper methods and properties that can be used to get information about the
recipe.

- `variantKeys`: An array of the recipe variant keys
- `variantMap`: An object of the recipe variant keys and their values
- `splitVariantProps`: A function that takes an object as its argument and returns an array containing the recipe
  variant props and the rest of the props

```js
import { cva } from '../styled-system/css'

const buttonRecipe = cva({
  base: {
    color: 'red',
    fontSize: '1.5rem'
  },
  variants: {
    size: {
      sm: {
        fontSize: '1rem'
      },
      md: {
        fontSize: '2rem'
      }
    }
  }
})

buttonRecipe.variantKeys
// => ['size']

buttonRecipe.variantMap
// => { size: ['sm', 'md'] }

buttonRecipe.splitVariantProps({ size: 'sm', onClick() {} })
// => [{ size: 'sm'}, { onClick() {} }]
```

These methods and properties are useful when creating custom components or writing Storybook stories for your recipes.

Here's a Storybook example.

```tsx filename="button.stories.tsx"
import { Button, buttonRecipe } from './components/button'

export default {
  title: 'Button',
  component: Button,
  argTypes: {
    size: {
      control: {
        type: 'select',
        options: buttonRecipe.variantMap.size
      }
    }
  }
}

export const Demo = {
  render: args => <Button {...args}>Click me</Button>
}
```

## Best Practices

- Leverage css variables in the base styles as much as possible. Makes it easier to theme the component with JS
- Don't mix styles by writing complex selectors. Separate concerns and group them in logical variants
- Use the `compoundVariants` property to create more complex sets of styles

## Limitations

- Recipes created from `cva` cannot have responsive or conditional values. Only layer recipes can have responsive or
  conditional values.

- Due to static nature of Panda, it's not possible to track the usage of the recipes in all cases. Here are some of use
  cases that Panda won't be able to track the usage of the recipe variants:

  **When you change the name of the variant prop in the JSX component**

  In below example, the `size` prop is renamed to `buttonSize`

  ```tsx
  const Button = ({ buttonSize, children }) => {
    return (
      <button {...props} className={button({ size: buttonSize })}>
        {children}
      </button>
    )
  }
  ```

  **When you use the recipe in a custom component that is not named as per the recipe name, Panda won't be able to track
  the usage of the recipe variants.**

  In below example, the component name `Button` is renamed to `Random` and we are using `button` recipe.

  ```tsx
  const Random = ({ size, children }) => {
    return (
      <button {...props} className={button({ size })}>
        {children}
      </button>
    )
  }
  ```

- When using `compoundVariants` in the recipe, you're not able to use responsive values in the variants.

```tsx
const button = defineRecipe({
  base: {
    color: 'red',
    fontSize: '1.5rem'
  },
  variants: {
    size: {
      sm: {
        fontSize: '1rem'
      },
      md: {
        fontSize: '2rem'
      }
    }
  },
  // this  will disable responsive values for the variants
  compoundVariants: [
    {
      size: 'sm',
      visual: 'funky',
      css: {
        color: 'blue'
      }
    },
    {
      size: 'md',
      visual: 'funky',
      css: {
        color: 'green'
      }
    }
  ]
})
```

## Static CSS

Panda provides a way to generate `static CSS` for your recipes. This is useful when you want to generate CSS for a
recipe without using the recipe in your code or if you use dynamic styling that Panda can't keep track of.

More information about static CSS can be found [here](/docs/guides/static.md#generating-recipes).

## Should I use atomic or config recipes ?

[Config recipes](/docs/concepts/recipes#config-recipe) are generated just in time, meaning that only the recipes and
variants you use will exist in the generated CSS, regardless of the number of recipes in the config.

This contrasts with [Atomic recipes](/docs/concepts/recipes#atomic-recipe-or-cva) (cva), which generates all of the
variants regardless of what was used in your code. The reason for this difference is that all `config.recipes` are known
at the start of the panda process when we evaluate your config.

In contrast, the CVA recipes are scattered throughout your code. To get all of them and find their usage across your
code, we would need to scan your app code multiple times, which would not be ideal performance-wise.

When dealing with simple use cases, or if you need code colocation, or even avoiding dynamic styling, atomic recipes
shine by providing all style variants. Config recipes are preferred for design system components, delivering leaner CSS
with only the styles used. Choose according to your component needs.

|                                                        | Config recipe                                                                                                                                                                                                             | Atomic recipe (cva)                                                                                                                                                                                                  |
| ------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Can both use any theme tokens, utilities or conditions | ✅ yes                                                                                                                                                                                                                    | ✅ yes                                                                                                                                                                                                               |
| Are generated just in time (JIT) based on usage        | ✅ yes, only the recipe variants found in your code will be generated                                                                                                                                                     | ❌ no, all variants found in your `cva` recipes will always be generated                                                                                                                                             |
| Can be shared in a preset                              | ✅ yes, you can include it in your `preset.theme.recipes`                                                                                                                                                                 | ❌ no                                                                                                                                                                                                                |
| Can be applied responsively                            | ✅ yes, `button({ size: { base: 'sm', md: 'lg' } })`                                                                                                                                                                      | ❌ no, only the styles in the recipe can be responsive                                                                                                                                                               |
| Can be colocated in your markup code                   | ❌ no, they must be defined or imported in your `panda.config`                                                                                                                                                            | ✅ yes, you can place it anywhere in your app                                                                                                                                                                        |
| Generate atomic classes                                | ❌ no, a specific className will be generated using your `recipe.className`                                                                                                                                               | ✅ yes                                                                                                                                                                                                               |
| Can be composed/merged at runtime                      | ❌ no, a specific className will be generated using your `recipe.className`, [you need to use `cx` to add each recipe classes](https://panda-css.com/docs/concepts/merging-styles#merging-config-recipe-and-style-object) | ✅ [yes, you can use the `.raw` function (ex: `button.raw({ size: "md" })`) to get the atomic style object and merge them all in a `css(xxx, yyy, zzz)` call](/docs/concepts/merging-styles#merging-cva--css-styles) |


---


## Responsive Design

How to write mobile responsive designs in your CSS in Panda

Responsive design is a fundamental aspect of modern web development, allowing websites and applications to adapt
seamlessly to different screen sizes and devices.

Panda provides a comprehensive set of responsive utilities and features to facilitate the creation of responsive
layouts. It lets you do this through conditional styles for different breakpoints.

Let's say you want to change the font weight of a text on large screens, you can do it like this:

```jsx
<span
  className={css({
    fontWeight: 'medium',
    lg: { fontWeight: 'bold' }
  })}
>
  Text
</span>
```

> Panda uses a mobile-first breakpoint system and leverages min-width media queries `@media(min-width)` when you write
> responsive styles.

Panda provides five breakpoints by default:

```ts
const breakpoints = {
  sm: '640px',
  md: '768px',
  lg: '1024px',
  xl: '1280px',
  '2xl': '1536px'
}
```

## Overview

### Property based modifier

Panda allows you apply the responsive condition directly to a style property, resulting in a more concise syntax:

```diff
<span
  className={css({
-   fontWeight: 'medium',
-   lg: { fontWeight: 'bold' }
+   fontWeight: { base: 'medium', lg: 'bold' }
  })}
>
  Text
</span>
```

### The Array syntax

Panda also accepts arrays as values for responsive styles. Pass the corresponding value for each breakpoint in the
array. Using our previous code as an example:

```jsx
<span
  className={css({
    fontWeight: ['medium', undefined, undefined, 'bold']
  })}
>
  Text
</span>
```

> We're leaving the corresponding values of the unused breakpoints `md` and `lg` as undefined.

### Targeting a breakpoint range

By default, styles assigned to a specific breakpoint will be effective at that breakpoint and will persist as applied
styles at larger breakpoints.

If you wish to apply a utility exclusively when a particular range of breakpoints is active, Panda offers properties
that restrict the style to that specific range. To construct the property, combine the minimum and maximum breakpoints
using the "To" notation in camelCase format.

Let's say we want to apply styles between the `md` and `xl` breakpoints, we use the `mdToXl` property:

```jsx
<span
  className={css({
    fontWeight: { mdToXl: 'bold' }
  })}
>
  Text
</span>
```

> This text will only be bold in `md`, `lg` and `xl` breakpoints.

### Targeting a single breakpoint

To target a single breakpoint, you can easily achieve this by simply adding the suffix "Only" to the breakpoint name in
camelCase format.

Let's say we want to apply styles only in the `lg` breakpoint, we use the `lgOnly` property:

```jsx
<span
  className={css({
    fontWeight: { lgOnly: 'bold' }
  })}
>
  Text
</span>
```

### Customizing Breakpoints

When encountering certain scenarios, it may become necessary to establish custom breakpoints tailored to your
application's needs. It is advisable to utilize commonly used aliases such as `sm`, `md`, `lg`, and `xl` for this
purpose.

In order to define custom breakpoints, you can easily accomplish this by passing them as an object within your Panda
config.

> Note: Make sure that the CSS units of your breakpoints are consistent. Use either all pixels (`px`) or all `em`, but
> do not mix them.

```js filename="panda.config.ts"
import { defineConfig } from '@pandacss/dev'

export default defineConfig({
  // ...
  theme: {
    extend: {
      breakpoints: {
        sm: '640px',
        md: '768px',
        lg: '1024px',
        xl: '1280px',
        '2xl': '1536px'
      }
    }
  }
})
```

### Hiding elements by breakpoint

If you need to limit the visibility of an element to any breakpoint, Panda provides
[display utilities](/docs/utilities/display) to help you achieve this.


---


## Slot Recipes

Learn how to style multiple parts components with slot recipes.

When using `cva` or `defineRecipe` might be enough for simple cases, slot recipes are a better fit for more complex
cases.

A slot recipe consists of these properties:

- `slots`: An array of component parts to style
- `base`: The base styles per slot
- `variants`: The different visual styles for each slot
- `defaultVariants`: The default variant for the component
- `compoundVariants`: The compound variant combination and style overrides for each slot.

> **Credit:** This API was inspired by multipart components in
> [Chakra UI](https://chakra-ui.com/docs/styled-system/component-style) and slot variants in
> [Tailwind Variants](https://tailwind-variants.org)

[See the comparison table between atomic recipes (`cva`) and `config recipes` here.](/docs/concepts/recipes#should-i-use-atomic-or-config-recipes-)
The same comparison applies to `sva` and `slot recipes`.

## Atomic Slot Recipe (or sva)

The `sva` function is a shorthand for creating a slot recipe with atomic variants. It takes the same arguments as `cva`
but returns a slot recipe instead.

### Defining the Recipe

```jsx filename="checkbox.recipe.ts"
import { sva } from '../styled-system/css'

const checkbox = sva({
  slots: ['root', 'control', 'label'],
  base: {
    root: { display: 'flex', alignItems: 'center', gap: '2' },
    control: { borderWidth: '1px', borderRadius: 'sm' },
    label: { marginStart: '2' }
  },
  variants: {
    size: {
      sm: {
        control: { width: '8', height: '8' },
        label: { fontSize: 'sm' }
      },
      md: {
        control: { width: '10', height: '10' },
        label: { fontSize: 'md' }
      }
    }
  },
  defaultVariants: {
    size: 'sm'
  }
})
```

### Using the recipe

The returned value from `sva` is a function that can be used to apply the recipe for each component part. Here's an
example of how to use the `checkbox` recipe:

```jsx filename="Checkbox.tsx"
import { css } from '../styled-system/css'
import { checkbox } from './checkbox.recipe'

const Checkbox = () => {
  const classes = checkbox({ size: 'sm' })
  return (
    <label className={classes.root}>
      <input type="checkbox" className={css({ srOnly: true })} />
      <div className={classes.control} />
      <span className={classes.label}>Checkbox Label</span>
    </label>
  )
}
```

When a slot recipe is created, Panda will pre-generate the css of all the possible combinations of variants and compound
variants as atomic classes.

```css
@layer utilities {
  .border_width_1px {
    border-width: 1px;
  }

  .rounded_sm {
    border-radius: var(--radii-sm);
  }

  .margin_start_2 {
    margin-inline-start: var(--spacing-2);
  }

  .w_8 {
    width: var(--sizing-8);
  }

  .h_8 {
    height: var(--sizing-8);
  }

  .font_size_sm {
    font-size: var(--fontSizes-sm);
  }

  .w_10 {
    width: var(--sizing-10);
  }

  .h_10 {
    height: var(--sizing-10);
  }

  .font_size_md {
    font-size: var(--fontSizes-md);
  }
  /* ... */
}
```

### Compound Variants

Compound variants are a way to apply style overrides to a slot based on the combination of variants.

Let's say you want to apply a different border color to the checkbox control based on its `size` and the `isChecked`
variant, here's how to do it:

```jsx filename="checkbox.recipe.ts" {14-22}
import { sva } from '../styled-system/css'
const checkbox = sva({
  slots: ['root', 'control', 'label'],
  base: {...},
  variants: {
    size: {
      sm: {...},
      md: {...}
    },
    isChecked: {
      true: { control: {}, label: {} }
    }
  },
  compoundVariants: [
    {
      size: 'sm',
      isChecked: true,
      css: {
        control: { borderColor: 'green.500' }
      }
    }
  ],
  defaultVariants: {...}
})
```

### Targeting slots

You can set an optional `className` property in the `sva` config which can be used to target slots in the DOM.

> Each slot will contain a `${className}__${slotName}` class in addition to the atomic styles.

Let's say you want to apply a different border color to the button text directly from the `root` slot. Here's how you
would do it:

```tsx
import { sva } from '../styled-system/css'

const button = sva({
  className: 'btn',
  slots: ['root', 'text'],
  base: {
    root: {
      bg: 'blue.500',
      _hover: {
        // v--- 🎯 this will target the `text` slot
        '& .btn__text': {
          color: 'white'
        }
      }
    }
  }
})
```

> Note: This doesn't work when you have the `hash: true` option in your panda config. We recommend using `data-x`
> selectors to target slots.

### TypeScript Guide

Panda provides a `RecipeVariantProps` type utility that can be used to infer the variant properties of a slot recipe.

This is useful when you want to use the recipe in JSX and want to get type safety for the variants.

```tsx
import { sva, type RecipeVariantProps } from '../styled-system/css'

const checkbox = sva({...})

export type CheckboxVariants = RecipeVariantProps<typeof checkbox>
//  => { size?: 'sm' | 'md', isChecked?: boolean }
```

### Usage in JSX

Unlike the atomic recipe or `cva`, slot recipes are not meant to be used directly in the `styled` factory since it
returns an object of classes instead of a single class.

```jsx
import { css } from '../styled-system/css'
import { styled } from '../styled-system/jsx'
import { checkbox, type CheckboxVariants } from './checkbox.recipe'

// ❌ Won't work
const Checkbox = styled('label', checkbox)

// ✅ Works
const Checkbox = (props: CheckboxVariants) => {
  const classes = checkbox(props)
  return (
    <label className={classes.root}>
      <input type="checkbox" className={css({ srOnly: true })} />
      <div className={classes.control} />
      <span className={classes.label}>Checkbox Label</span>
    </label>
  )
}
```

### Styling JSX Compound Components

Compound components are a great way to create reusable components for better composition. Slot recipes play nicely with
this pattern and requires a context provider for the component.

> **Note:** This is an advanced topic and you don't need to understand it to use slot recipes. If you use React, be
> aware that context require adding 'use client' to the top of the file.

Let's say you want to design a Checkbox component that can be used like this:

```jsx
<Checkbox size="sm|md" isChecked>
  <Checkbox.Control />
  <Checkbox.Label>Checkbox Label</Checkbox.Label>
</Checkbox>
```

First, create a shared context for ths styles

```jsx filename="style-context.tsx"
'use client'
import { createContext, forwardRef, useContext } from 'react'

export const createStyleContext = recipe => {
  const StyleContext = createContext(null)

  const withProvider = (Component, part) => {
    const Comp = forwardRef((props, ref) => {
      const [variantProps, rest] = recipe.splitVariantProps(props)
      const styles = recipe(variantProps)
      return (
        <StyleContext.Provider value={styles}>
          <Component ref={ref} className={styles?.[part ?? '']} {...rest} />
        </StyleContext.Provider>
      )
    })
    Comp.displayName = Component.displayName || Component.name
    return Comp
  }

  const withContext = (Component, part) => {
    if (!part) return Component

    const Comp = forwardRef((props, ref) => {
      const styles = useContext(StyleContext)
      return <Component ref={ref} className={styles?.[part ?? '']} {...props} />
    })
    Comp.displayName = Component.displayName || Component.name
    return Comp
  }

  return { withProvider, withContext }
}
```

> Note: For the TypeScript version of this file, refer to
> [create-style-context.tsx](https://github.com/cschroeter/park-ui/blob/main/website/src/lib/create-style-context.tsx)
> in Park UI

Then, use the context to create compound components connected to the recipe

```jsx filename="Checkbox.tsx"
import { createStyleContext } from './style-context'
import { checkbox } from './checkbox.recipe'

const { withProvider, withContext } = createStyleContext(checkbox)

//                                  👇🏻 points to the root slot
const Root = withProvider('label', 'root')
//                                    👇🏻 points to the control slot
const Control = withContext('div', 'control')
//                                  👇🏻 points to the label slot
const Label = withContext('span', 'label')

const Checkbox = { Root, Control, Label }
```

## Config Slot Recipe

Config slot recipes are very similar atomic recipes except that they use well-defined classNames and store the styles in
the `recipes` cascade layer.

The config slot recipe takes the following additional properties:

- `className`: The name of the recipe. Used in the generated class name
- `jsx`: An array of JSX components that use the recipe. Defaults to the uppercase version of the recipe name
- `description`: An optional description of the recipe (used in the js-doc comments)

### Defining the recipe

To define a config slot recipe, import the `defineSlotRecipe` function

```jsx filename="checkbox.recipe.ts"
import { defineSlotRecipe } from '@pandacss/dev'

export const checkboxRecipe = defineSlotRecipe({
  className: 'checkbox',
  description: 'The styles for the Checkbox component',
  slots: ['root', 'control', 'label'],
  base: {
    root: { display: 'flex', alignItems: 'center', gap: '2' },
    control: { borderWidth: '1px', borderRadius: 'sm' },
    label: { marginStart: '2' }
  },
  variants: {
    size: {
      sm: {
        control: { width: '8', height: '8' },
        label: { fontSize: 'sm' }
      },
      md: {
        control: { width: '10', height: '10' },
        label: { fontSize: 'md' }
      }
    }
  },
  defaultVariants: {
    size: 'sm'
  }
})
```

### Adding recipe to config

To add the recipe to the config, you’d need to add it to the `slotRecipes` property of the `theme`

```jsx filename="panda.config.ts"
import { defineConfig } from '@pandacss/dev'
import { checkboxRecipe } from './checkbox.recipe'

export default defineConfig({
  //...
  jsxFramework: 'react',
  theme: {
    extend: {
      slotRecipes: {
        checkbox: checkboxRecipe
      }
    }
  }
})
```

### Generate JS code

This generates a recipes folder the specified `outdir` which is `styled-system` by default. If Panda doesn’t
automatically generate your CSS file, you can run the `panda codegen` command.

You only need to import the recipes into the component files where you need to use them.

### Using the recipe

To use the recipe, you can import the recipe from the `<outdir>/recipes` entrypoint and use it in your component. Panda
tracks the usage of the recipe and only generates CSS of the variants used in your application.

```js
import { css } from '../styled-system/css'
import { checkbox } from '../styled-system/recipes'

const Checkbox = () => {
  const classes = checkbox({ size: 'sm' })
  return (
    <label className={classes.root}>
      <input type="checkbox" className={css({ srOnly: true })} />
      <div className={classes.control} />
      <span className={classes.label}>Checkbox Label</span>
    </label>
  )
}
```

The generated css is registered under the `recipe` [cascade layer](/docs/concepts/cascade-layers.mdx) with the class
name that matches the recipe-slot-variant name pattern `<recipe-className>__<slot-name>--<variant-name>`.

```css
@layer recipes {
  @layer base {
    .checkbox__root {
      display: flex;
      align-items: center;
      gap: var(--space-2);
    }

    .checkbox__control {
      border-width: var(--border-widths-1px);
      border-radius: var(--radii-sm);
    }

    .checkbox__label {
      margin-start: var(--space-2);
    }
  }

  .checkbox__control--size-sm {
    width: var(--space-8);
    height: var(--space-8);
  }

  .checkbox__label--size-sm {
    font-size: var(--font-sizes-sm);
  }

  .checkbox__control--size-md {
    width: var(--space-10);
    height: var(--space-10);
  }

  .checkbox__label--size-md {
    font-size: var(--font-sizes-md);
  }
}
```

### TypeScript Guide

Every slot recipe ships a type interface for its accepted variants. You can import them from the `styled-system/recipes`
entrypoint.

For the checkbox recipe, we can import the `CheckboxVariants` type like so:

```ts
import React from 'react'
import type { CheckboxVariants } from '../styled-system/recipes'

type CheckboxProps = CheckboxVariants & {
  children: React.ReactNode
  value?: string
  onChange?: (value: string) => void
}
```

### `defineParts`

It can be useful when you want to have the equivalent of a slot recipe without needing to split the class names bindings
and instead just having a className that handles children on 1 DOM element.

It pairs well with [ZagJs](https://zagjs.com/) and [Ark-UI](https://ark-ui.com/)

Let's refactor the previous example to use parts instead of slots:

```ts
import { defineParts, definetRecipe } from '@pandacss/dev'

const parts = defineParts({
  root: { selector: '& [data-part="root"]' },
  control: { selector: '& [data-part="control"]' },
  label: { selector: '& [data-part="label"]' }
})

export const checkboxRecipe = defineRecipe({
  className: 'checkbox',
  description: 'A checkbox style',
  base: parts({
    root: { display: 'flex', alignItems: 'center', gap: '2' },
    control: { borderWidth: '1px', borderRadius: 'sm' },
    label: { marginStart: '2' }
  }),
  variants: {
    size: {
      sm: parts({
        control: { width: '8', height: '8' },
        label: { fontSize: 'sm' }
      }),
      md: parts({
        control: { width: '10', height: '10' },
        label: { fontSize: 'md' }
      })
    }
  },
  defaultVariants: {
    size: 'sm'
  }
})
```


---


## Style props

Build UIs quickly by passing css properties as "props" to your components.

While you can get very far by using the `className` prop and function from Panda, style props provide a more ergonomic
way of expressing styles.

Panda will extract the style props through static analysis and generate the CSS at build time.

> If you use Chakra UI, Styled System, or Theme UI, you'll feel right at home right away 😊

```jsx
import { css } from '../styled-system/css'
import { styled } from '../styled-system/jsx'

// The className approach
const Button = ({ children }) => (
  <button
    className={css({
      bg: 'blue.500',
      color: 'white',
      py: '2',
      px: '4',
      rounded: 'md'
    })}
  >
    {children}
  </button>
)

// The style props approach
const Button = ({ children }) => (
  <styled.button bg="blue.500" color="white" py="2" px="4" rounded="md">
    {children}
  </styled.button>
)
```

## Configure JSX

Using JSX style props is turned off by default in Panda, but you can opt-in to this feature by using the `jsxFramework`
property in the panda config.

> ⚠️ Panda will not extract style props from JSX elements if you don't set the `jsxFramework` property. This is to avoid
> unnecessary work for projects that don't use JSX.

### Choose Framework

JSX is a JavaScript syntax extension that allows you to write HTML-like code directly within your JavaScript code and is
supported by most popular frameworks. Panda supports JSX style props in React, Preact, Vue 3, Qwik and Solid.js.

```js filename="panda.config.ts"
import { defineConfig } from '@pandacss/dev'

export default defineConfig({
  // ...
  jsxFramework: 'react'
})
```

### Generate JSX runtime

Next, you need to run `panda codegen` to generate the JSX runtime for your framework.

<Tabs items={['pnpm', 'npm', 'yarn', 'bun']}>
  {/* <!-- prettier-ignore-start --> */}
  <Tab>
  ```bash
  pnpm panda codegen --clean
  ```
  </Tab>
  <Tab>
  ```bash
  npm panda codegen --clean
  ```
  </Tab>
  <Tab>
  ```bash
  yarn panda codegen --clean
  ```
  </Tab>
  <Tab>
  ```bash
  bun panda codegen --clean
  ```
  </Tab>
  {/* <!-- prettier-ignore-end --> */}
</Tabs>

That's it! You can now use JSX style props in your components.

## Using Style Props

### JSX Element

Style props are just CSS properties that you can pass to your components as props. With the JSX runtime, you can use
`styled.<element>` syntax to create supercharged JSX elements that support style props.

```jsx
import { styled } from '../styled-system/jsx'

const Button = ({ children }) => (
  <styled.button bg="blue.500" color="white" py="2" px="4" rounded="md">
    {children}
  </styled.button>
)
```

### Property Renaming

<Callout type="warning">Due to the static nature of Panda, you can't rename properties at runtime.</Callout>

```tsx filename="App.tsx"
import { Circle, CircleProps } from '../styled-system/jsx'

type Props = {
  circleSize?: CircleProps['size']
}

const CustomCircle = (props: Props) => {
  const { circleSize = '3' } = props
  return (
    <Circle
      // ❌ Avoid: Panda can't know that you're mapping `circleSize` to `size`
      size={circleSize}
    />
  )
}

// ...

const App = () => {
  return (
    // In this case, you should keep the `size` naming
    <CustomCircle circleSize="4" />
  )
}
```

The same principles apply to all style props, recipe variants, and pattern props.

<Callout type="info">
  If you still need to rename properties at runtime, you can use `config.staticCss` as an escape-hatch to pre-generate
  the CSS anyway for the properties you need.
</Callout>

### Recipe

You can use recipe variants as JSX props to quickly change the styles of your components, as long as
[you're tracking those components in your recipe config](/docs/concepts/recipes#advanced-jsx-tracking).

```tsx
import { styled } from '../styled-system/jsx'
import { button, type ButtonVariantProps } from '../styled-system/recipes'

const Button = (props: ButtonVariantProps) => <button className={button(props)}>Button</button>

const App = () => <Button variant="secondary">Button</Button>
```

## Factory Function

You can also use the `styled` function to create a styled component from any component or JSX intrinsic element (like
"a", "button").

```jsx
import { styled } from '../styled-system/jsx'
import { Button } from 'component-library'

const StyledButton = styled(Button)

const App = () => (
  <StyledButton bg="blue.500" color="white" py="2" px="4" rounded="md">
    Button
  </StyledButton>
)
```

> You can configure the `styled` function name using the [`config.jsxFactory`](/docs/references/config#jsxfactory)
> option.

### Factory Recipe

You can define a recipe for your component using the `styled` function. This is useful when you want to create a
component that has a specific set of style props.

```jsx
import { styled } from '../styled-system/jsx'

const Button = styled('button', {
  base: {
    py: '2',
    px: '4',
    rounded: 'md'
  },
  variants: {
    variant: {
      primary: {
        bg: 'blue.500',
        color: 'white'
      },
      secondary: {
        bg: 'gray.500',
        color: 'white'
      }
    }
  }
})

const App = () => (
  <Button variant="secondary" mt="10px">
    Button
  </Button>
)
```

### Factory Options

There's a few options you can pass to the `styled` function to customize the behavior of the generated component.

```ts
interface FactoryOptions<TProps extends Dict> {
  dataAttr?: boolean
  defaultProps?: TProps
  shouldForwardProp?(prop: string, variantKeys: string[]): boolean
}
```

#### `dataAttr`

Setting `dataAttr` to true will add a `data-recipe="{recipeName}"` attribute to the element with the recipe name. This
is useful for testing and debugging.

```jsx
import { styled } from '../styled-system/jsx'
import { button } from '../styled-system/recipes'

const Button = styled('button', button, { dataAttr: true })

const App = () => <Button variant="secondary">Button</Button>
// => <button data-recipe="button" class="btn btn--variant_purple">Button</button>
```

#### `defaultProps`

allows you to skip writing wrapper components just to set a few props. It also allows you to locall override the default
variants or base styles of a recipe.

```jsx
import { styled } from '../styled-system/jsx'
import { button } from '../styled-system/recipes'

const Button = styled('button', button, {
  defaultProps: {
    variant: 'secondary',
    px: '10px'
  }
})

const App = () => <Button>Button</Button>
// => <button class="btn btn--variant_secondary px_10px">Button</button>
```

#### `shouldForwardProp`

Used to customize which props are forwarded to the underlying element. By default, all props except recipe variants and
style props are forwarded.

For example, you could use it to integrate with [Framer Motion](https://www.framer.com/motion/).

```jsx
import { styled } from '../styled-system/jsx'
import { button } from '../styled-system/recipes'
import { motion, isValidMotionProp } from 'framer-motion'

const StyledMotion = styled(
  motion.div,
  {},
  {
    shouldForwardProp: (prop, variantKeys) =>
      isValidMotionProp(prop) || (!variantKeys.includes(prop) && !isCssProperty(prop))
  }
)
```

### Unstyled prop

All styled components accept an `unstyled` prop that allows you to disable the recipe styles. This is useful when you
want to use a component's structure but apply completely custom styling.

```jsx
import { styled } from '../styled-system/jsx'
import { button } from '../styled-system/recipes'

const Button = styled('button', button)

const App = () => (
  <>
    {/* With recipe styles */}
    <Button>Styled Button</Button>

    {/* Without recipe styles, but inline styles still work */}
    <Button unstyled bg="red.500" color="white">
      Unstyled Button
    </Button>
  </>
)
```

### Reducing the allowed style props

You can reduce the allowed JSX properties on the factory using
[`config.jsxStyleProps`](/docs/references/config#jsxstyleprops):

- When set to 'all', all style props are allowed.
- When set to 'minimal', only the `css` prop is allowed.
- When set to 'none', no style props are allowed and therefore the `jsxFactory` will not be usable as a component:
  - `<styled.div />` and `styled("div")` aren't valid
  - but the recipe usage is still valid `styled("div", { base: { color: "red.300" }, variants: { ...} })`

> Removing style props (from `all` to either `minimal` or `none`) will reduce the size of the generated code due to not
> having to check which props are style props at runtime.

## JSX Patterns

Patterns are common layout patterns like `stack`, `grid`, `circle` that can be used to speed up your css. Think of them
as a way to avoid repetitive layout styles.

All the patterns provided by Panda are available as JSX components.

> Learn more about the [patterns](/docs/customization/patterns) we provide.

```jsx
import { Stack, Circle } from '../styled-system/jsx'

const App = () => (
  <Stack gap="4" align="flex-start">
    <button>Button</button>
    <Circle size="4" bg="red.300">
      4
    </Circle>
  </Stack>
)
```

## Making your own styled components

To make a custom JSX component that accepts style props, Use the `splitCssProps` function to split style props from
other component props.

> For this to work correctly, set the `jsxFramework` to the framework you're using in your panda config.

```tsx
import { splitCssProps } from '../styled-system/jsx'
import type { HTMLStyledProps } from '../styled-system/types'

export function Component(props: HTMLStyledProps<'div'>) {
  const [cssProps, restProps] = splitCssProps(props)
  const { css: cssProp, ...styleProps } = cssProps

  const className = css({ display: 'flex', height: '20', width: '20' }, styleProps, cssProp)

  return <div {...restProps} className={className} />
}

// Usage
function App() {
  return <Component w="2">Click me</Component>
}
```

## TypeScript

Panda provides type definitions for all the style props that are supported by the JSX runtime.

You can use these types to get type safety in your components.

### Style Object

Use the `JsxStyleProps` to get the types of the style object that is compatible with JSX elements.

```tsx
import { styled } from '../styled-system/jsx'
import type { JsxStyleProps } from '../styled-system/types'

interface ButtonProps {
  color?: JsxStyleProps['color']
}

const Button = (props: ButtonProps) => {
  return <styled.button {...props}>
}
```

### Style Props

Use the `HTMLStyledProps` type to get the types of an element in addition to the style props.

```tsx {2}
import { styled } from '../styled-system/jsx'
import type { HTMLStyledProps } from '../styled-system/jsx'

type ButtonProps = HTMLStyledProps<'button'>

const Button = (props: ButtonProps) => {
  return <styled.button {...props}>
}
```

### Variant Props

Use the `StyledVariantProps` type to extract the variants from a styled component.

```tsx {2}
import { styled } from '../styled-system/jsx'
import type { StyledVariantProps } from '../styled-system/jsx'

const Button = styled('button', {
  base: { color: 'black' },
  variants: {
    state: {
      error: { color: 'red' },
      success: { color: 'green' }
    }
  }
})

type ButtonVariantProps = StyledVariantProps<typeof Button>
//   ^ { state?: 'error' | 'success' | undefined }
```

### Patterns

Every pattern provided by Panda has a corresponding type that you can use to get type safety in your components.

```tsx {2}
import { Stack } from '../styled-system/jsx'
import type { StackProps } from '../styled-system/jsx'
```


---


## Styled System

What is the styled-system folder and how does it work?

While Panda generates your CSS at **build-time** using static extraction, we still need a lightweight runtime to
transform the CSS-in-JS syntax (either [`object`](/docs/concepts/writing-styles#atomic-styles) or
[`template-literal`](/docs/concepts/template-literals)) to class names strings. This is where the `styled-system` folder
comes in.

When running the `panda` or `panda codegen` commands, the [`config.outdir`](/docs/references/config#outdir) will be used
as output path to generate the `styled-system` in.

This is the core of what the `styled-system` does:

```ts
css({ color: 'blue.300' }) // => "text_blue_300"
```

Since Panda doesn't rely on any bundler's (`vite`, `webpack`, etc) plugin, there is no code transformation happening to
convert the CSS-in-JS syntax to class names at compile-time. This is why we need a lightweight runtime to do that.

The same principles applies to `patterns`, `recipes` and even `jsx` components, as they all use the `css` function under
the hood.

If you look inside your `styled-system` folder, you should see the main entrypoints for the runtime:

<FileTree>
  <FileTree.Folder name="styled-system" defaultOpen>
    <FileTree.Folder name="css" />
    <FileTree.Folder name="jsx" />
    <FileTree.Folder name="recipes" />
    <FileTree.Folder name="patterns" />
    <FileTree.Folder name="tokens" />
    <FileTree.Folder name="types" />
    <FileTree.File name="styles.css" />
  </FileTree.Folder>
</FileTree>

Feel free to explore the files inside the `styled-system` folder to get a better understanding of how it works in
details!

> Note: The `styled-system` folder is not meant to be edited manually. It is generated by Panda and should be treated as
> a build artifact. This also means you don't need to commit it to your repository.

## How does it work?

When running the `panda` command or with the postcss plugin, here's what's happening under the hood:

1. **Load Panda context**:

- Find and evaluate app config, merge result with presets.
- Create panda context: prepare code generator from config, parse user's file as AST.

2. **Generating artifacts**:

- Write lightweight JS runtime and types to output directory

3. **Extracting used styles in app code**:

- Run parser on each user's file: identify and extract styles, compute CSS, write to styles.css.

That `2. Generating artifacts` step is where the `styled-system` folder is generated, using the resolved config that
contains all your tokens, patterns, recipes, utilities etc. We generate a tailored runtime for your app, so that it only
contains enough code (and types!) to support the styles you're using.

## Pre-rendering

If you use some way to pre-render your components to static HTML, for example using Astro or RSC, the `styled-system`
functions like `css` and others will be removed at build-time and replaced by the generated class names, so that you
don't have to ship the runtime to your users.


---


## Template Literals

Panda allows you to write styles using template literals.

Writing styles using template literals provides a similar experience to
[styled-components](https://styled-components.com/) and [emotion](https://emotion.sh/), except that Panda generates
atomic class names instead of a single unique class name.

> Emitting atomic class names allows Panda to generate smaller CSS bundles.

Panda provides two functions to write template literal styles: `css` and `styled`.

## Getting started

To use template literals, you need to set the `syntax` option in your `panda.config.ts` file to `templateLiteral`:

```ts
// panda.config.ts
export default defineConfig({
  // ...
  syntax: 'template-literal', // required
  jsxFramework: 'react' // required for JSX utilities, e.g. `styled`
})
```

Then run the codegen command to generate the functions:

```sh
panda codegen --clean
```

## The `css` function

This the basic way of writing template styles. It converts the template literal into a set of atomic class name which
you can pass to the `className` prop of an element.

```js
import { css } from '../styled-system/css'

const className = css`
  font-size: 16px;
  font-weight: bold;
`

function Heading() {
  return <h1 className={className}>This is a title</h1>
}

// => <h1 className='font-size_16px font-weight_bold'></h1>
```

Here's what the emitted atomic CSS looks like:

```css
.font-size_16px {
  font-size: 16px;
}

.font-weight_bold {
  font-weight: bold;
}
```

## The `styled` tag

The `styled` tag allows you to create a component with encapsulated styles. It's similar to the `styled-components` or
`emotion` library.

```js
import { styled } from '../styled-system/jsx'

// Create a styled component
const Heading = styled.h1`
  font-size: 16px;
  font-weight: bold;
`

function Demo() {
  // Use the styled component
  return <Heading>This is a title</Heading>
}

// => <h1 class='font-size_16px font-weight_bold'>This is a title</h1>
```

Here's what the emitted atomic CSS looks like:

```css
.font-size_16px {
  font-size: 16px;
}

.font-weight_bold {
  font-weight: bold;
}
```

## Nested styles

You can nest selectors, pseudo-elements and pseudo-selectors.

```js
const Button = styled.button`
  color: black;

  &:hover {
    color: blue;
  }
`
```

Using css nesting syntax, pseudo-elements, pseudo-selectors and combinators are also supported:

```js
const Demo = styled.div`
  color: black;

  &::after {
    content: '🐼';
  }

  & + & {
    background: yellow;
  }

  &.bordered {
    border: 1px solid black;
  }

  .parent & {
    color: red;
  }
`
```

Nested media and container queries are also supported:

```js
const Demo = styled.div`
  color: black;

  @media (min-width: 200px) {
    color: blue;
  }

  @container (min-width: 200px) {
    color: red;
  }
`
```

## Hashing class names

In some cases, it might be useful to shorten the class names by hashing them. Set the `hash: true` option in your
`panda.config.ts` file to enable this. This will generate shorter class names but will make it harder to debug.

To achieve this, set the `hash` option in your `panda.config.ts` file to `true`:

```ts
// panda.config.ts

export default defineConfig({
  // ...
  hash: true // optional
})
```

> Run the `codegen` command to regenerate the functions with hashing enabled.

When hashing is enabled, the class names will go from this:

```css
.font-size_16px {
  font-size: 16px;
}

.font-weight_bold {
  font-weight: bold;
}
```

To a unique six character hash regardless of the length of the selector or the number of declarations:

```css
.adfg5r {
  font-size: 16px;
}

.bsdf35 {
  font-weight: bold;
}
```

## Using tokens

Use the `token()` function or `{}` syntax in your template literals to reference design tokens in your styles. Panda
will automatically generate the corresponding CSS variables.

```js
import { css } from '../styled-system/css'

const className = css`
  font-size: {fontSizes.md};
  font-weight: token(fontWeights.bold, 700);
`
```

## Caveats

The object literal syntax is the recommended way of writing styles. But, if you stick with the template literal syntax,
there are some caveats to be aware of:

- Patterns and recipes are not generated
- Dynamic interpolation or component targeting is not supported
- Lack of autocompletion for tokens within the template literal Our
  [Eslint plugin](https://github.com/chakra-ui/eslint-plugin-panda/blob/main/docs/rules/no-invalid-token-paths.md) can
  help you overcome this by detecting invalid tokens
- JSX Style props are not supported


---


## Virtual Color

Panda allows you to create a virtual color or color placeholder in your project.

The `colorPalette` property is how you create virtual colors.

```js
import { css } from '../styled-system/css'

const className = css({
  colorPalette: 'blue',
  bg: 'colorPalette.100',
  _hover: {
    bg: 'colorPalette.200'
  }
})
```

This will translate to the `blue.100` background color and `blue.200` background color on hover.

Virtual colors are useful when creating easily customizable components.

## Using with recipes

You can also use virtual colors with recipes.

```js
import { css, cva, cx } from '../styled-system/css'

const button = cva({
  base: {
    padding: 4
    // you can also specify a default colorPalette in the `base` recipe key
    // colorPalette: 'blue',
    // ^^^^^^^^^^^^^^^^^^^^
  },
  variants: {
    variant: {
      primary: { color: 'colorPalette.500' }
    }
  },
  defaultVariants: { variant: 'primary' }
})
```

## Using with different color modes

You can also use virtual colors with different conditions, such as color modes.

```js
import { css, cva, cx } from '../styled-system/css'

const someButton = cva({
  base: { padding: 4 },
  variants: {
    variant: {
      primary: {
        bg: { base: 'colorPalette.500', _dark: 'colorPalette.200' },
        color: { base: 'white', _dark: 'gray.900' }
      }
    }
  },
  defaultVariants: { variant: 'primary' }
})

export const App = () => {
  return (
    <>
      <div className="light">
        <button className={cx(css({ colorPalette: 'blue' }), someButton())}>Click me</button>
        <button className={cx(css({ colorPalette: 'green' }), someButton())}>Click me</button>
        <button className={cx(css({ colorPalette: 'red' }), someButton())}>Click me</button>
      </div>
      <div className="dark">
        <button className={cx(css({ colorPalette: 'blue' }), someButton())}>Click me</button>
        <button className={cx(css({ colorPalette: 'green' }), someButton())}>Click me</button>
        <button className={cx(css({ colorPalette: 'red' }), someButton())}>Click me</button>
      </div>
    </>
  )
}
```

## Semantic Virtual Colors

Semantic virtual colors gives you an ability to create a virtual color organized by category, variant and state.
Hierarchically organized virtual colors are useful when creating easily customizable components.

```js
const theme = {
  extend: {
    semanticTokens: {
      colors: {
        button: {
          dark: {
            value: 'navy'
          },
          light: {
            DEFAULT: {
              value: 'skyblue'
            },
            accent: {
              DEFAULT: {
                value: 'cyan'
              },
              secondary: {
                value: 'blue'
              }
            }
          }
        }
      }
    }
  }
}
```

You can now use the root `button` color palette and its values directly:

```tsx
import { css } from '../styled-system/css'

export const App = () => {
  return (
    <button
      className={css({
        colorPalette: 'button',
        color: 'colorPalette.light',
        backgroundColor: 'colorPalette.dark',
        _hover: {
          color: 'colorPalette.light.accent',
          background: 'colorPalette.light.accent.secondary'
        }
      })}
    >
      Root color palette
    </button>
  )
}
```

Or you can use any deeply nested property (e.g. `button.light.accent`) as a root color palette:

```tsx
import { css } from '../styled-system/css'

export const App = () => {
  return (
    <button
      className={css({
        colorPalette: 'button.light.accent',
        color: 'colorPalette.secondary'
      })}
    >
      Nested color palette leaf
    </button>
  )
}
```

> **Note**: Nested tokens require glob patterns in the `colorPalette` config (e.g., `'button.*'`) to generate proper CSS
> variables.

## Pregenerated Virtual Colors

Use the `staticCss` option in the config to pre-generate values for the `colorPalette` property.

This is useful when you want to use a color palette that can be changed at runtime (e.g. in Storybook knobs).

> Learn more about [static css generation](/docs/guides/static).

```tsx
export default defineConfig({
  staticCss: {
    css: [
      {
        properties: { colorPalette: ['red', 'blue'] }
      }
    ]
  }
})
```

Then in your code, you can design components that use the `colorPalette` property:

```tsx
import { css } from '../styled-system/css'

function ButtonShowcase() {
  const [colorPalette, setColorPalette] = useState('red')
  return (
    <div>
      <select value={colorPalette} onChange={e => setColorPalette(e.currentTarget.value)}>
        <option value="red">Red</option>
        <option value="blue">Blue</option>
      </select>

      <button
        className={css({
          bg: 'colorPalette.50',
          color: 'colorPalette.500',
          colorPalette
        })}
      >
        Click me
      </button>
    </div>
  )
}
```

## Configuration

By default, color palette generation is enabled and includes all colors defined in your theme.

You can control which colors are used to generate color palettes by configuring the `colorPalette` property in your
theme.

### Disable Color Palette

To completely disable color palette generation, set `enabled` to `false`:

```ts filename="panda.config.ts"
import { defineConfig } from '@pandacss/dev'

export default defineConfig({
  theme: {
    colorPalette: {
      enabled: false
    }
  }
})
```

### Include Specific Colors

To generate color palettes for only specific colors, use the `include` option:

```ts filename="panda.config.ts"
import { defineConfig } from '@pandacss/dev'

export default defineConfig({
  theme: {
    colorPalette: {
      include: ['gray', 'blue', 'red']
    }
  }
})
```

This will only generate color palettes for `gray`, `blue`, and `red` colors, even if you have other colors defined in
your theme.

**Glob patterns** are supported for nested tokens:

```ts filename="panda.config.ts"
colorPalette: {
  include: ['gray.*', 'blue.*'] // Includes all nested tokens
}
```

### Exclude Specific Colors

To exclude certain colors from color palette generation, use the `exclude` option:

```ts filename="panda.config.ts"
import { defineConfig } from '@pandacss/dev'

export default defineConfig({
  theme: {
    colorPalette: {
      exclude: ['yellow', 'orange']
    }
  }
})
```

This will generate color palettes for all colors except `yellow` and `orange`.

### Combination of Options

You can combine the `enabled`, `include`, and `exclude` options as needed:

```ts filename="panda.config.ts"
import { defineConfig } from '@pandacss/dev'

export default defineConfig({
  theme: {
    colorPalette: {
      enabled: true,
      include: ['gray', 'blue', 'red', 'green'],
      exclude: ['red'] // This will override the include for 'red'
    }
  }
})
```

In this example, color palettes will be generated for `gray`, `blue`, and `green`, but not for `red` (since it's
excluded).

## Nested Semantic Tokens

If nested tokens show as raw paths (e.g., `colors.base.accent`) instead of CSS variables, use glob patterns:

```ts filename="panda.config.ts"
semanticTokens: {
  colors: {
    button: {
      primary: {
        DEFAULT: { value: '{colors.blue.500}' },
        hover: { value: '{colors.blue.600}' }
      }
    }
  }
},
colorPalette: {
  include: ['button.*']  // Include all nested paths
}
```

Usage:

```tsx
className={css({
  colorPalette: 'button.primary',
  bg: 'colorPalette',
  _hover: { bg: 'colorPalette.hover' }
})}
```


---


## Writing Styles

Panda generates the utilities you need to style your components with confidence.

Using the object syntax is a fundamental approach to writing styles in Panda. It not only provides a type-safe style
authoring experience, but also improves readability and ensures a consistent experience with style overrides.

## Atomic Styles

When you write styles in Panda, it generates a modern atomic stylesheet that is automatically scoped to the
`@layer utilities` cascade layer.

The atomic stylesheets approach offers several advantages, such as improved code maintainability and reusability, as
well as a smaller overall CSS footprint.

Panda exposes a `css` function that can be used to author styles. It accepts a style object and returns a className
string.

```jsx
import { css } from '../styled-system/css'

const styles = css({
  backgroundColor: 'gainsboro',
  borderRadius: '9999px',
  fontSize: '13px',
  padding: '10px 15px'
})

// Generated className:
// --> bg_gainsboro rounded_9999px fs_13px p_10px_15px

<div className={styles}>
  <p>Hello World</p>
</div>
```

The styles generated at build time end up like this:

```css
@layer utilities {
  .bg_gainsboro {
    background-color: gainsboro;
  }

  .rounded_9999px {
    border-radius: 9999px;
  }

  .fs_13px {
    font-size: 13px;
  }

  .p_10px_15px {
    padding: 10px 15px;
  }
}
```

### Shorthand Properties

Panda provides shorthands for common css properties to help improve the speed of development and reduce the visual
density of your style declarations.

Properties like `borderRadius`, `backgroundColor`, and `padding` can be swapped to their shorthand equivalent `rounded`,
`bg`, and `p`.

```jsx
import { css } from '../styled-system/css'

// BEFORE - Good
const styles = css({
  backgroundColor: 'gainsboro',
  borderRadius: '9999px',
  fontSize: '13px',
  padding: '10px 15px'
})

// AFTER - Better
const styles = css({
  bg: 'gainsboro',
  rounded: '9999px',
  fontSize: '13px',
  p: '10px 15px'
})
```

> Shorthands are documented alongside their respective properties in the [utilities](/docs/utilities/background)
> section.

### Type safety

Panda is built with TypeScript and provides type safety for all style properties and shorthands. Most of the style
properties are connected to either the native CSS properties or their respective token value defined as defined in the
`theme` object.

```ts
import { css } from '../styled-system/css'

//                       ⤵ you'll get autocomplete for colors
const styles = css({ bg: '|' })
```

> You can also enable the `strictTokens: true` setting in the Panda configuration. This allows only token values and
> prevents the use of custom or raw CSS values.

- `config.strictTokens` will only affect properties that have config tokens, such as `color`, `bg`, `borderColor`, etc.
- `config.strictPropertyValues` will throw for properties that do not have config tokens, such as `display`, `content`,
  `willChange`, etc. when the value is not a predefined CSS value.

> In both cases, you can use the `[xxx]` escape-hatch syntax to use custom or raw CSS values without TypeScript errors.

#### strictTokens

With `config.strictTokens` enabled, you can only use token values in your styles. This prevents the use of custom or raw
CSS values.

```ts filename="panda.config.ts"
import { css } from '../styled-system/css'

css({ bg: 'red' }) // ❌ Error: "red" is not a valid token value
css({ fontSize: '123px' }) // ❌ Error: "123px" is not a valid token value

css({ bg: 'red.400' }) // ✅ Valid
css({ fontSize: '[123px]' }) // ✅ Valid, since `[123px]` is using the escape-hatch syntax
css({ content: 'abc' }) // ✅ Valid, since `content` isn't bound to a config token
```

For one-off styles, you can always use the escape-hatch syntax `[xxx]` to use custom or raw CSS values without
TypeScript errors.

```ts filename="panda.config.ts"
import { css } from '../styled-system/css'

css({ bg: '[red]' }) // ✅ Valid, since `[red]` is using the escape-hatch syntax
css({ fontSize: '[123px]' }) // ✅ Valid, since `[123px]` is using the escape-hatch syntax
```

#### strictPropertyValues

With `config.strictPropertyValues` enabled, you can only use valid CSS values for properties that do have a predefined
list of values in your styles. This prevents the use of custom or raw CSS values.

```ts filename="panda.config.ts"
css({ display: 'flex' }) // ✅ Valid
css({ display: 'block' }) // ✅ Valid

css({ display: 'abc' }) // ❌ will throw since 'abc' is not part of predefined values of 'display'
css({ pos: 'absolute123' }) // ❌ will throw since 'absolute123' is not part of predefined values of 'position'
css({ display: '[var(--btn-display)]' }) // ✅ Valid, since `[var(--btn-display)]` is using the escape-hatch syntax

css({ content: '""' }) // ✅ Valid, since `content` does not have a predefined list of values
css({ flex: '0 1' }) // ✅ Valid, since `flex` does not have a predefined list of values
```

The `config.strictPropertyValues` option will only be applied to this exhaustive list of properties:

```ts
type StrictableProps =
  | 'alignContent'
  | 'alignItems'
  | 'alignSelf'
  | 'all'
  | 'animationComposition'
  | 'animationDirection'
  | 'animationFillMode'
  | 'appearance'
  | 'backfaceVisibility'
  | 'backgroundAttachment'
  | 'backgroundClip'
  | 'borderCollapse'
  | 'border'
  | 'borderBlock'
  | 'borderBlockEnd'
  | 'borderBlockStart'
  | 'borderBottom'
  | 'borderInline'
  | 'borderInlineEnd'
  | 'borderInlineStart'
  | 'borderLeft'
  | 'borderRight'
  | 'borderTop'
  | 'borderBlockEndStyle'
  | 'borderBlockStartStyle'
  | 'borderBlockStyle'
  | 'borderBottomStyle'
  | 'borderInlineEndStyle'
  | 'borderInlineStartStyle'
  | 'borderInlineStyle'
  | 'borderLeftStyle'
  | 'borderRightStyle'
  | 'borderTopStyle'
  | 'boxDecorationBreak'
  | 'boxSizing'
  | 'breakAfter'
  | 'breakBefore'
  | 'breakInside'
  | 'captionSide'
  | 'clear'
  | 'columnFill'
  | 'columnRuleStyle'
  | 'contentVisibility'
  | 'direction'
  | 'display'
  | 'emptyCells'
  | 'flexDirection'
  | 'flexWrap'
  | 'float'
  | 'fontKerning'
  | 'forcedColorAdjust'
  | 'isolation'
  | 'lineBreak'
  | 'mixBlendMode'
  | 'objectFit'
  | 'outlineStyle'
  | 'overflow'
  | 'overflowX'
  | 'overflowY'
  | 'overflowBlock'
  | 'overflowInline'
  | 'overflowWrap'
  | 'pointerEvents'
  | 'position'
  | 'resize'
  | 'scrollBehavior'
  | 'touchAction'
  | 'transformBox'
  | 'transformStyle'
  | 'userSelect'
  | 'visibility'
  | 'wordBreak'
  | 'writingMode'
```

## Nested Styles

Panda provides different ways of nesting style declarations. You can use the native css nesting syntax, or the built-in
pseudo props like `_hover` and `_focus`. Pseudo props are covered more in-depth in the next section.

### Native CSS Nesting

Panda supports the native css nesting syntax. You can use the `&` selector to create nested styles.

> **Important:** It is required to use the "&" character when nesting styles.

```jsx
<div
  className={css({
    bg: 'red.400',
    '&:hover': {
      bg: 'orange.400'
    }
  })}
/>
```

You can also target children and siblings using the `&` syntax.

```jsx
<div
  className={css({
    bg: 'red.400',
    '& span': {
      color: 'pink.400'
    }
  })}
/>
```

We recommend not using descendant selectors as they can lead to specificity issues when managing style overrides.
Colocating styles directly on the element is the preferred way of writing styles in Panda.

### Using Pseudo Props

Panda provides a set of pseudo props that can be used to create nested styles. The pseudo props are prefixed with an
underscore `_` to avoid conflicts with the native pseudo selectors.

For example, to create a hover style, you can use the `_hover` pseudo prop.

```jsx
<div
  className={css({
    bg: 'red.400',
    _hover: {
      bg: 'orange.400'
    }
  })}
/>
```

> See the [pseudo props](/docs/concepts/conditional-styles#reference) section for a list of all available pseudo props.

## Global styles

Global styles are useful for applying additional global resets or font faces. Use the `globalCss` property in the
`panda.config.ts` file to define global styles.

Global styles are inserted at the top of the stylesheet and are scoped to the `@layer base` cascade layer.

> For resets, global variables, theming patterns, and more examples, see [Global styles](/docs/concepts/global-styles).

```js filename="panda.config.ts"
import { defineConfig, defineGlobalStyles } from '@pandacss/dev'

const globalCss = defineGlobalStyles({
  'html, body': {
    color: 'gray.900',
    lineHeight: '1.5'
  }
})

export default defineConfig({
  // ...
  globalCss
})
```

The styles generated at build time will look like this:

```css
@layer base {
  html,
  body {
    color: var(--colors-gray-900);
    line-height: 1.5;
  }
}
```

## Style Composition

### Merging styles

Passing multiple styles to the `css` function will deeply merge the styles, allowing you to override styles in a
predictable way.

```jsx
import { css } from '../styled-system/css'

const result = css({ mx: '3', paddingTop: '4' }, { mx: '10', pt: '6' })
//    ^? result = "mx_10 pt_6"
```

To design a component that supports style overrides, you can provide the `css` prop as a style object, and it'll be
merged correctly.

```tsx filename="src/components/Button.tsx"
import { css } from '../styled-system/css'

export const Button = ({ css: cssProp = {}, children }) => {
  const className = css({ display: 'flex', alignItems: 'center', color: 'black' }, cssProp)
  return <button className={className}>{children}</button>
}
```

Then you can use the `Button` component like this:

```tsx filename="src/app/page.tsx"
import { Button } from './Button'

export default function Page() {
  return (
    <Button css={{ color: 'pink', _hover: { color: 'red' } }}>
      will result in `class="d_flex items_center text_pink hover:text_red"`
    </Button>
  )
}
```

---

You can use this approach as well with the `{cvaFn}.raw`, `{svaFn.raw}` and `{patternFn}.raw` functions, allowing style
objects to be merged as expected in any situation.

**Pattern Example:**

```tsx filename="src/components/Button.tsx"
import { hstack } from '../styled-system/patterns'
import { css } from '../styled-system/css'

export const Button = ({ css: cssProp = {}, children }) => {
  // using the flex pattern
  const hstackProps = hstack.raw({
    border: '1px solid',
    _hover: { color: 'blue.400' }
  })

  // merging the styles
  const className = css(hstackProps, cssProp)

  return <button className={className}>{children}</button>
}
```

**CVA Example:**

```tsx filename="src/components/Button.tsx"
import { css, cva } from '../styled-system/css'

const buttonRecipe = cva({
  base: { display: 'flex', fontSize: 'lg' },
  variants: {
    variant: {
      primary: { color: 'white', backgroundColor: 'blue.500' }
    }
  }
})

export const Button = ({ css: cssProp = {}, children }) => {
  const className = css(
    // using the button recipe
    buttonRecipe.raw({ variant: 'primary' }),

    // adding style overrides (internal)
    { _hover: { color: 'blue.400' } },

    // adding style overrides (external)
    cssProp
  )

  return <button className={className}>{children}</button>
}
```

**SVA Example:**

```tsx filename="src/components/Button.tsx"
import { css, sva } from '../styled-system/css'

const checkbox = sva({
  slots: ['root', 'control', 'label'],
  base: {
    root: { display: 'flex', alignItems: 'center', gap: '2' },
    control: { borderWidth: '1px', borderRadius: 'sm' },
    label: { marginStart: '2' }
  },
  variants: {
    size: {
      sm: {
        control: { width: '8', height: '8' },
        label: { fontSize: 'sm' }
      },
      md: {
        control: { width: '10', height: '10' },
        label: { fontSize: 'md' }
      }
    }
  },
  defaultVariants: {
    size: 'sm'
  }
})

export const Checkbox = ({ rootProps, controlProps, labelProps }) => {
  // using the checkbox recipe
  const slotStyles = checkbox.raw({ size: 'md' })

  return (
    <label className={css(slotStyles.root, rootProps)}>
      <input type="checkbox" className={css({ srOnly: true })} />
      <div className={css(slotStyles.control, controlProps)} />
      <span className={css(slotStyles.label, labelProps)}>Checkbox Label</span>
    </label>
  )
}

// Usage

const App = () => {
  return (
    <Checkbox
      rootProps={css.raw({ gap: 4 })}
      controlProps={css.raw({ borderColor: 'yellow.400' })}
      labelProps={css.raw({ fontSize: 'lg' })}
    />
  )
}
```

### Classname concatenation

Panda provides a simple `cx` function to join classnames. It accepts a list of classnames and returns a string.

```jsx
import { css, cx } from '../styled-system/css'

const styles = css({
  borderWidth: '1px',
  borderRadius: '8px',
  paddingX: '12px',
  paddingY: '24px'
})

const Card = ({ className, ...props }) => {
  const rootClassName = cx('group', styles, className)
  return <div className={rootClassName} {...props} />
}
```

### Hashing

When debugging or previewing DOM elements in the browser, the length of the generated atomic `className` can get quite
long, and a bit annoying. If you prefer to have terser classnames, use the `hash` option to enable className and css
variable name hashing.

```ts filename="panda.config.ts"
import { defineConfig } from '@pandacss/dev'

export default defineConfig({
  // ...
  hash: true
})
```

> You might need to generate a new code artifact by running `panda codegen --clean`

When you write a style like this:

```jsx
import { css } from '../styled-system/css'

const styles = css({
  display: 'flex',
  flexDirection: 'row',
  _hover: {
    bg: 'red.50'
  }
})
```

The hash generated css will look like:

```css
.fPSBzf {
  display: flex;
}

.ksWBqx {
  flex-direction: row;
}

.btpEVp:is(:hover, [data-hover]) {
  background: var(--bINrJX);
}
```

> We recommend that you use this in production builds only, as it can make debugging a bit harder.

## Important styles

Applying important styles works just like CSS

```js
css({
  color: 'red !important'
})
```

You can also apply important using just the exclamation syntax `!`

```js
css({
  color: 'red!'
})
```

## TypeScript

Use the `SystemStyleObject` type if you want to type your styles.

```ts {2}
import { css } from '../styled-system/css'
import type { SystemStyleObject } from '../styled-system/types'

const styles: SystemStyleObject = {
  color: 'red'
}
```

## Property conflicts

When you combine shorthand and longhand properties, Panda will resolve the styles in a predictable way. The shorthand
property will take precedence over the longhand property.

```jsx
import { css } from '../styled-system/css'

const styles = css({
  paddingTop: '20px'
  padding: "10px",
})
```

The styles generated at build time will look like this:

```css
@layer utilities {
  .p_10px {
    padding: 10px;
  }

  .pt_20px {
    padding-top: 20px;
  }
}
```

## Global vars

You can use the `globalVars` property to define global
[CSS variables](https://developer.mozilla.org/en-US/docs/Web/CSS/--*) or custom CSS
[`@property`](https://developer.mozilla.org/en-US/docs/Web/CSS/@property) definitions.

Panda will automatically generate the corresponding CSS variables and suggest them in your style objects.

> They will be generated in the [`cssVarRoot`](/docs/references/config#cssvarroot) near your tokens.

This can be especially useful when using a 3rd party library that provides custom CSS variables, like a popper library
that exposes a `--popper-reference-width`.

```ts filename="panda.config.ts"
import { defineConfig } from '@pandacss/dev'

export default defineConfig({
  // ...
  globalVars: {
    '--popper-reference-width': '4px',
    // you can also generate a CSS @property
    '--button-color': {
      syntax: '<color>',
      inherits: false,
      initialValue: 'blue'
    }
  }
})
```

> Note: Keys defined in `globalVars` will be available as a value for _every_ utilities, as they're not bound to token
> categories.

```ts
import { css } from '../styled-system/css'

const className = css({
  '--button-color': 'colors.red.300',
  // ^^^^^^^^^^^^  will be suggested

  backgroundColor: 'var(--button-color)'
  //                ^^^^^^^^^^^^^^^^^^  will be suggested
})
```


---

_This content is automatically generated from the official Panda CSS documentation._
