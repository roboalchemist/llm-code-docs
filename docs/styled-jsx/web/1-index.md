# styled-jsx Documentation

**styled-jsx** is a lightweight CSS-in-JS library providing full, scoped, and component-friendly CSS support for JSX. It enables writing CSS directly in React components with automatic style scoping, supporting both server-side rendering (SSR) and client-side rendering.

## Key Features

- **Full CSS Support**: Complete CSS feature set with no power tradeoffs
- **Complete Scope Isolation**: Selectors, animations, and keyframes are automatically scoped
- **Small Bundle Size**: ~3KB gzipped (from 12KB)
- **Vendor Prefixing**: Built-in automatic vendor prefixing
- **Dynamic Styles**: Theme and dynamic style support via template interpolation
- **Server-Side Rendering**: Native SSR support with registry system
- **Plugin System**: CSS preprocessing via plugins (Sass, Less, PostCSS)
- **Performance Optimized**: Fast transpilation and efficient style injection

## Quick Start

```bash
npm install --save styled-jsx
```

Add to Babel config:

```json
{
  "plugins": ["styled-jsx/babel"]
}
```

Use in components:

```jsx
export default () => (
  <div>
    <p>Styled paragraph</p>
    <style jsx>{`
      p {
        color: red;
      }
    `}</style>
  </div>
)
```

## Documentation Structure

- **Getting Started** — Installation, Babel config, first component
- **Configuration** — Babel plugin options (optimizeForSpeed, sourceMaps, vendorPrefixes)
- **Scoping & Isolation** — How scoping works, targeting root elements
- **Global Styles** — Writing global CSS, `:global()` selectors
- **Dynamic Styles** — Props-based, className-based, inline-style approaches
- **External Styles** — CSS files, modules, resolve tag
- **Server-Side Rendering** — StyleRegistry, StyledRegistry, SSR patterns
- **CSS Plugins** — Preprocessor integration, plugin development
- **Testing** — Rendering in tests, babel-test plugin
- **Advanced** — TypeScript, ESLint, syntax highlighting, Content Security Policy
- **FAQ & Troubleshooting** — Common issues and solutions
