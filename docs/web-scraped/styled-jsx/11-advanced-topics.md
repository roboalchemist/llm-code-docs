# Advanced Topics

## TypeScript

To enable TypeScript support for `<style jsx>`, add a triple-slash reference at the top of your TypeScript file:

```typescript
/// <reference types="styled-jsx" />

import React from 'react'

const Button: React.FC<{ color: string }> = ({ color }) => (
  <button>
    Click me
    <style jsx>{`
      button {
        color: ${color};
      }
    `}</style>
  </button>
)

export default Button
```

Or add the reference to your `tsconfig.json`:

```json
{
  "compilerOptions": {
    "types": ["styled-jsx"]
  }
}
```

### Babel with TypeScript

When using Babel to transform styled-jsx code with TypeScript, set `"jsx": "preserve"` in `tsconfig.json` to let Babel handle the JSX transformation:

```json
{
  "compilerOptions": {
    "jsx": "preserve",
    "module": "esnext"
  }
}
```

## ESLint Configuration

If using `eslint-plugin-import`, the `css` import from `styled-jsx/css` will generate errors since it's a "magic" import not listed in package.json.

### Solution: Add to ESLint Config

```json
{
  "settings": {
    "import/core-modules": ["styled-jsx/css"]
  }
}
```

This tells ESLint to treat `styled-jsx/css` as a core module.

## Syntax Highlighting

### Visual Studio Code

Install the styled-jsx syntax highlighting extension:

```bash
ext install Divlo.vscode-styled-jsx-syntax
```

For Stylus instead of CSS:

```bash
ext install samuelroy.vscode-styled-jsx-stylus
```

### VS Code Autocomplete

Install the language server extension:

```bash
ext install Divlo.vscode-styled-jsx-languageserver
```

### WebStorm / IntelliJ IDEA

Use "Inject language or reference" (default Alt+Enter) in intention actions. Select CSS for full syntax highlighting and autocompletion.

Or use language injection comments:

```jsx
const Button = ({ children }) => (
  <button>
    {children}

    {/*language=CSS*/}
    <style jsx>{`
      button {
        padding: 10px;
        background: #eee;
      }
    `}</style>
  </button>
)
```

### Atom

Install the `language-babel` package for Atom:

https://github.com/gandm/language-babel

Add this to your Atom settings for CSS syntax highlighting in styled-jsx tags:

```
"(?<=<style jsx>{)|(?<=<style jsx global>{)|(?<=css)":source.css.styled
```

### Vim

Install [vim-styled-jsx](https://github.com/alampros/vim-styled-jsx) with your plugin manager:

```vim
" vim-plug example
Plug 'alampros/vim-styled-jsx'
```

### Emmet

Add a snippet to `~/emmet/snippets-styledjsx.json`:

```json
{
  "html": {
    "snippets": {
      "style-jsx": "<style jsx>{`\n\t$1\n`}</style>"
    }
  }
}
```

Then use it:
- Type `style-jsx` and press Ctrl+Alt+Enter (or your Emmet expand key)
- Gets expanded to `<style jsx>{\`\n\t\n\`}</style>`

## Building Component Libraries

To build a React component library with styled-jsx, bundle styled-jsx as an external dependency:

Reference: [Guide to Building a React Components Library with Rollup and styled-jsx](https://medium.com/@tomaszmularczyk89/guide-to-building-a-react-components-library-with-rollup-and-styled-jsx-694ec66bd2)

Key considerations:
1. Keep styled-jsx as a peer dependency
2. Ensure the Babel plugin is configured in consuming projects
3. Test that styles work in consuming apps

## Content Security Policy (Strict CSP)

styled-jsx supports strict Content Security Policy. Generate a unique nonce per request:

```js
import nanoid from 'nanoid'

const nonce = Buffer.from(nanoid()).toString('base64')
// Example: "N2M0MDhkN2EtMmRkYi00MTExLWFhM2YtNDhkNTc4NGJhMjA3"
```

When rendering styles:

```jsx
const styles = registry.styles({ nonce })
```

Set the meta tag:

```jsx
<meta property="csp-nonce" content={nonce} />
```

And the CSP header:

```
Content-Security-Policy: default-src 'self'; style-src 'self' 'nonce-N2M0MDhkN2EtMmRkYi00MTExLWFhM2YtNDhkNTc4NGJhMjA3';
```

**Critical:** The nonce must be:
- Generated per request
- Unpredictable
- Identical across meta tag, `registry.styles()`, and CSP header

## Performance Optimization

### Use `optimizeForSpeed` in Production

```json
{
  "plugins": [["styled-jsx/babel", { "optimizeForSpeed": true }]]
}
```

This enables CSSOM-based style injection for maximum performance but disables source maps.

### Split Static and Dynamic Styles

Separate static and dynamic CSS into different `<style>` tags to minimize re-rendering:

```jsx
const Button = props => (
  <button>
    <style jsx>{`
      button { color: #999; }  /* Static */
    `}</style>
    <style jsx>{`
      button { padding: ${props.large ? '50' : '20'}px; }  /* Dynamic */
    `}</style>
  </button>
)
```

### Use className Toggling for Variants

For preset variants, use className toggling rather than continuous interpolation:

```jsx
// ✅ Better for performance
<button className={size === 'large' && 'large'}>

// ⚠️ Less efficient for many variants
<style>{`button { padding: ${getSizeValue(size)}px; }`}</style>
```
