# External Styles and CSS Modules

Define styles outside of your component using `styled-jsx/css` library.

## CSS Module Exports

`styled-jsx/css` provides three main exports:

### 1. `css` (Default) - Scoped Styles

Define scoped styles for use in components:

```js
/* styles.js */
import css from 'styled-jsx/css'

export const button = css`
  button {
    color: hotpink;
  }
`

export default css`
  div {
    color: green;
  }
`
```

Import and use:

```jsx
import styles, { button } from './styles'

export default () => (
  <div>
    <button>Click me</button>
    <style jsx>{styles}</style>
    <style jsx>{button}</style>
  </div>
)
```

### 2. `css.global` - Global Styles

Define global styles that apply everywhere:

```js
/* styles.js */
import css from 'styled-jsx/css'

export const globalReset = css.global`
  * {
    margin: 0;
    padding: 0;
  }
  body {
    margin: 0;
  }
`
```

Use:

```jsx
import { globalReset } from './styles'

export default () => (
  <div>
    <h1>Title</h1>
    <style jsx global>{globalReset}</style>
  </div>
)
```

### 3. `css.resolve` - Scoped Styles with Class Names

Get both a scoped className and the styles element:

```js
/* styles.js */
import css from 'styled-jsx/css'

export const link = css.resolve`
  a {
    color: green;
  }
`
// link.className -> scoped className (e.g., "jsx-123")
// link.styles -> styles element to render
```

Use in a component:

```jsx
import Link from 'some-library'
import { link } from './styles'

export default () => (
  <div>
    <Link className={link.className}>About</Link>
    {link.styles}
  </div>
)
```

## Dynamic Styles with `css.resolve`

The `resolve` tag supports dynamic styles via template interpolation:

```js
/* styles.js */
import css from 'styled-jsx/css'

export function getLinkStyles(color) {
  return css.resolve`
    a { color: ${color} }
  `
}
```

Use:

```jsx
import { getLinkStyles } from './styles'

export default props => {
  const { className, styles } = getLinkStyles(props.theme.color)

  return (
    <div>
      <Link className={className}>About</Link>
      {styles}
    </div>
  )
}
```

## Styling Third-Party Components

The `resolve` tag is ideal for styling third-party components from the parent:

```jsx
import Select from 'react-select'
import css from 'styled-jsx/css'

const { className, styles } = css.resolve`
  .custom-select {
    border: 1px solid #ccc;
  }
  .custom-select:focus {
    border-color: blue;
  }
`

export default () => (
  <div>
    <Select className={className} />
    {styles}
  </div>
)
```

## Styles Outside Components

Define styles in your component file but outside the component:

```jsx
import css from 'styled-jsx/css'

export default () => (
  <div>
    <button>Click me</button>
    <style jsx>{button}</style>
  </div>
)

const button = css`
  button {
    color: hotpink;
  }
`
```

This helps keep render methods smaller and more readable.

## CSS in Regular CSS Files

styled-jsx v3 includes a webpack loader to import styles from regular `.css` files:

```js
/* component.js */
import styles from '../components/button/styles.css'

export default () => (
  <div>
    <button>Click me</button>
    <style jsx>{styles}</style>
  </div>
)
```

### Webpack Configuration

Add the loader before `babel-loader`:

```js
config.module.rules.push({
  test: /\.css$/,
  use: [
    {
      loader: require('styled-jsx/webpack').loader,
      options: {
        type: 'scoped' // 'scoped', 'global', or 'resolve'
      }
    }
  ]
})
```

### Next.js Integration

Example `next.config.js`:

```js
module.exports = {
  webpack: (config, { defaultLoaders }) => {
    config.module.rules.push({
      test: /\.css$/,
      use: [
        defaultLoaders.babel,
        {
          loader: require('styled-jsx/webpack').loader,
          options: {
            type: 'scoped'
          }
        }
      ]
    })

    return config
  }
}
```

## Limitations

**Important:** External CSS files and `css` exports don't support dynamic styles. Use `css.resolve` for dynamic interpolation or inline `<style jsx>` for fully dynamic content.

## Import Best Practices

For Prettier compatibility, use the default export:

```js
// ✅ Good - Prettier compatible
import styles from './styles.js'

// ⚠️ May have issues with Prettier
import { button, link } from './styles.js'
```

Individual imports can also be used:

```js
import { resolve } from 'styled-jsx/css'
import { global } from 'styled-jsx/css'
```
