# Dynamic Styles

There are three ways to make styles dynamic in styled-jsx: template interpolation, className toggling, and inline styles.

## Via Interpolated Dynamic Props

Any value from the component's scope (props, state, constants) can be interpolated directly in the style template. These are treated as dynamic:

```jsx
const Button = props => (
  <button>
    {props.children}
    <style jsx>{`
      button {
        padding: ${'large' in props ? '50' : '20'}px;
        background: ${props.theme.background};
        color: #999;
        display: inline-block;
        font-size: 1em;
      }
    `}</style>
  </button>
)
```

**Performance Optimization:** When CSS is mostly static, split static and dynamic styles into separate `<style>` tags so only dynamic parts are recomputed:

```jsx
const Button = props => (
  <button>
    {props.children}
    <style jsx>{`
      /* Static styles */
      button {
        color: #999;
        display: inline-block;
        font-size: 2em;
      }
    `}</style>
    <style jsx>{`
      /* Dynamic styles - only this block is recomputed */
      button {
        padding: ${'large' in props ? '50' : '20'}px;
        background: ${props.theme.background};
      }
    `}</style>
  </button>
)
```

## Via className Toggling

Toggle class names based on props or state:

```jsx
const Button = props => (
  <button className={'large' in props && 'large'}>
    {props.children}
    <style jsx>{`
      button {
        padding: 20px;
        background: #eee;
        color: #999;
      }
      .large {
        padding: 50px;
      }
    `}</style>
  </button>
)
```

Usage:
```jsx
<Button>Normal</Button>
<Button large>Big</Button>
```

## Via Inline Styles

**Best for animations.** Override CSS with inline styles:

```jsx
const Button = ({ padding, children }) => (
  <button style={{ padding }}>
    {children}
    <style jsx>{`
      button {
        padding: 20px;
        background: #eee;
        color: #999;
      }
    `}</style>
  </button>
)
```

Usage:
```jsx
<Button>Default 20px padding</Button>
<Button padding="30px">Custom 30px padding</Button>
```

Inline styles override CSS-defined padding.

## Using Constants

Constants defined outside component scope are treated as static:

```jsx
import { colors, spacing } from '../theme'
import { invertColor } from '../theme/utils'

const Button = ({ children }) => (
  <button>
    {children}
    <style jsx>{`
      button {
        padding: ${spacing.medium};
        background: ${colors.primary};
        color: ${invertColor(colors.primary)};
      }
    `}</style>
  </button>
)
```

These constants are baked into the style at compile time, not re-evaluated at runtime.

## Dynamic Styles with External CSS

External styles (via `styled-jsx/css`) do NOT support dynamic interpolation:

```jsx
// ❌ This won't work
import css from 'styled-jsx/css'

export const buttonStyles = css`
  button { padding: ${props.size}px; }  // ❌ Can't use props
`
```

For dynamic external styles, use the `css.resolve` tag instead (see External Styles guide).

## Best Practices

1. **Split static and dynamic**: Separate `<style>` tags for better performance
2. **Use className toggling** for multiple discrete variants (small/medium/large)
3. **Use inline styles** for truly continuous values (colors, dimensions)
4. **Use template interpolation** for moderate dynamic styling
5. **Avoid excessive re-renders**: Memoize theme objects if they're created inline
