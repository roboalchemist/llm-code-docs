# Global Styles

## Global Styles with `global` Prop

To skip scoping and apply styles globally, add the `global` prop to `<style jsx>`:

```jsx
export default () => (
  <div>
    <style jsx global>{`
      body {
        background: red;
      }
    `}</style>
  </div>
)
```

**Advantages over `<style>` tag:**
- No need for `dangerouslySetInnerHTML` to avoid CSS escaping issues
- Takes advantage of styled-jsx's de-duping system to prevent styles from being inserted multiple times

## One-Off Global Selectors with `:global()`

Sometimes you need to skip scoping for specific selectors only. Use `:global()` to target elements outside your component:

```jsx
import Select from 'react-select'

export default () => (
  <div>
    <Select optionClassName="react-select" />

    <style jsx>{`
      /* "div" will be prefixed, but ".react-select" won't */
      div :global(.react-select) {
        color: red;
      }
    `}</style>
  </div>
)
```

This is inspired by CSS Modules and is useful for:
- Styling third-party components that accept a custom class
- Styling child components from a parent component
- Creating global utility classes within scoped styles

## Example: Styling react-select

```jsx
import Select from 'react-select'

export default function App() {
  return (
    <div>
      <Select
        options={options}
        optionClassName="select-option"
      />

      <style jsx>{`
        div :global(.select-option) {
          padding: 10px;
          font-size: 14px;
        }
        div :global(.select-option:hover) {
          background: #eee;
        }
      `}</style>
    </div>
  )
}
```

Note the use of `:global()` to prevent the classname from being scoped, allowing it to match the class that react-select applies.

## External Global Styles

You can also define global styles using the `styled-jsx/css` module:

```js
/* styles.js */
import css from 'styled-jsx/css'

export const body = css.global`body { margin: 0; }`
```

Import and use in your component:

```jsx
import { body } from './styles'

export default () => (
  <div>
    <style jsx global>{body}</style>
  </div>
)
```

## Scoping Behavior

Remember that `:global()` selectors are NOT scoped, so they apply globally. Use them carefully:

```jsx
<style jsx>{`
  /* This is scoped */
  div { color: blue; }

  /* This is global */
  div > :global(.item) { color: red; }

  /* Best practice: use child selector (>) to limit scope */
  div > :global(.item) { }
`}</style>
```

The `>` (child combinator) helps limit the blast radius of global selectors.
