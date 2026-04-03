# Getting Started with styled-jsx

## Installation

```bash
npm install --save styled-jsx
```

## Babel Configuration

Add `styled-jsx/babel` to the `plugins` array in your `.babelrc`:

```json
{
  "plugins": ["styled-jsx/babel"]
}
```

For Next.js, this is configured automatically — no manual setup required.

## Your First Component

```jsx
export default () => (
  <div>
    <p>only this paragraph will get the style :)</p>

    {/* you can include <Component />s here that include
         other <p>s that don't get unexpected styles! */}

    <style jsx>{`
      p {
        color: red;
      }
    `}</style>
  </div>
)
```

## How It Works: Transpilation

The above code transpiles to:

```jsx
import _JSXStyle from 'styled-jsx/style'

export default () => (
  <div className="jsx-123">
    <p className="jsx-123">only this paragraph will get the style :)</p>
    <_JSXStyle id="123">{`p.jsx-123 {color: red;}`}</_JSXStyle>
  </div>
)
```

Key points:
- Unique classnames (`jsx-123`) provide style encapsulation
- The `_JSXStyle` component is optimized for:
  - Injecting styles upon render
  - Only injecting a component's style once (even if included multiple times)
  - Removing unused styles
  - Tracking styles for server-side rendering

## Targeting the Root Element

Both the outer div and all elements inside get the scoped classname. You can target the root element explicitly:

```jsx
export default () => (
  <div className="root">
    <style jsx>{`
      .root {
        color: green;
      }
    `}</style>
  </div>
)
```

This pattern works like the `:host` pseudo-element in Shadow DOM.

## Using in Next.js

Next.js automatically configures `styled-jsx` with Babel or SWC. Simply use `<style jsx>` without manual configuration:

```jsx
// In a Next.js page or component
export default function Page() {
  return (
    <div>
      <h1>Welcome</h1>
      <style jsx>{`
        h1 {
          font-size: 2rem;
        }
      `}</style>
    </div>
  )
}
```
