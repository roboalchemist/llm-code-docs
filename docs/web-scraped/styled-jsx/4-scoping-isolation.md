# Scoping and Style Isolation

## How Scoping Works

styled-jsx automatically scopes all styles to their component by:

1. Generating unique classnames (`jsx-123`, `jsx-456`, etc.)
2. Adding the classname to all elements in the component
3. Prefixing all selectors with the classname

This ensures styles only affect the intended component and its children.

## Complete Isolation

styled-jsx provides complete isolation for:
- **Selectors** — All selectors are scoped
- **Animations** — Keyframe names are scoped
- **Media Queries** — Media queries respect scoping
- **Pseudo-elements and Pseudo-classes** — `:hover`, `:focus`, etc. are scoped

Example:

```jsx
const Button = () => (
  <button>Click me</button>
  <style jsx>{`
    button {
      padding: 10px;
    }
    button:hover {
      background: blue;
    }
    @keyframes spin {
      from { transform: rotate(0deg); }
      to { transform: rotate(360deg); }
    }
  `}</style>
)
```

Transpiles to scoped versions where all selectors are prefixed with the unique classname.

## Targeting the Root Element

The root (outer) element of your component gets the scoped classname, allowing you to target it directly. To make this explicit and clear, use a class:

```jsx
export default () => (
  <div className="root">
    <p>paragraph</p>
    <style jsx>{`
      .root {
        color: green;
      }
      p {
        font-size: 1.2em;
      }
    `}</style>
  </div>
)
```

The `.root` class gets scoped, so styles only apply to this specific component instance.

## Nested Components

Styles don't leak between components, even when components are nested:

```jsx
const Parent = () => (
  <div>
    <Child />
    <style jsx>{`
      div { color: red; }
    `}</style>
  </div>
)

const Child = () => (
  <div>
    <p>This won't be red</p>
    <style jsx>{`
      div { color: blue; }
      p { font-weight: bold; }
    `}</style>
  </div>
)
```

The Parent's `div { color: red; }` only applies to the parent's div, not the Child's div.

## Multiple Style Tags

You can include multiple `<style jsx>` tags in the same component:

```jsx
export default () => (
  <button>
    {children}
    <style jsx>{`
      button {
        color: #999;
        display: inline-block;
        font-size: 2em;
      }
    `}</style>
    <style jsx>{`
      button {
        padding: ${large ? '50' : '20'}px;
        background: ${theme};
      }
    `}</style>
  </button>
)
```

Each `<style jsx>` tag gets the same scoped classname, so they all apply to the component.
