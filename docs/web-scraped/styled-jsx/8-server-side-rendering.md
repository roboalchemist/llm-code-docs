# Server-Side Rendering

styled-jsx v5+ introduces `StyledRegistry` component and `useStyleRegistry` hook for concurrent-safe SSR.

## Core Concepts

- `StyleRegistry` — Container for all styles rendered in a request
- `useStyleRegistry` — Hook to access the current registry
- `registry.styles()` — Returns array of React components for style tags
- `registry.flush()` — Clears styles from the registry (optional)

> Next.js 12+ automatically manages the registry for you.

## Basic SSR Pattern

```jsx
import React from 'react'
import ReactDOM from 'react-dom/server'
import { StyleRegistry, useStyleRegistry } from 'styled-jsx'
import App from './app'

function Styles() {
  const registry = useStyleRegistry()
  const styles = registry.styles()
  return <>{styles}</>
}

export default (req, res) => {
  const app = ReactDOM.renderToString(<App />)
  const html = ReactDOM.renderToStaticMarkup(
    <StyleRegistry>
      <html>
        <head>
          <Styles />
        </head>
        <body>
          <div id="root" dangerouslySetInnerHTML={{ __html: app }} />
        </body>
      </html>
    </StyleRegistry>
  )
  res.end('<!doctype html>' + html)
}
```

## Using createStyleRegistry

For manual control over the registry, use `createStyleRegistry`:

```jsx
import React from 'react'
import ReactDOM from 'react-dom/server'
import { StyleRegistry, createStyleRegistry } from 'styled-jsx'
import App from './app'

const registry = createStyleRegistry()

function Page() {
  return (
    <StyleRegistry registry={registry}>
      <App />
    </StyleRegistry>
  )
}

export default (req, res) => {
  const app = ReactDOM.renderToString(<Page />)
  const styles = registry.styles() // Get rendered styles
  
  const html = `<!doctype html>
    <html>
      <head>
        ${styles.map(s => ReactDOM.renderToString(s)).join('')}
      </head>
      <body>
        <div id="root">${app}</div>
      </body>
    </html>`
  
  res.end(html)
}
```

## Registry Hierarchy

By default, `<StyleRegistry />` uses the registry from the root top `StyleRegistry`. This means there's only one registry in the React tree:

```jsx
<StyleRegistry>
  <App />
  {/* All nested components share the same registry */}
</StyleRegistry>
```

You can override with a custom registry:

```jsx
const registry = createStyleRegistry()

<StyleRegistry registry={registry}>
  <App />
</StyleRegistry>
```

## Content Security Policy (CSP)

Strict CSP is supported. Generate a unique nonce per request:

```js
import nanoid from 'nanoid'

const nonce = Buffer.from(nanoid()).toString('base64')
// Example: "N2M0MDhkN2EtMmRkYi00MTExLWFhM2YtNDhkNTc4NGJhMjA3"
```

Pass the nonce to `registry.styles()`:

```jsx
const styles = registry.styles({ nonce })
```

Set the corresponding meta tag and CSP header:

```jsx
<meta property="csp-nonce" content={nonce} />
```

CSP header:
```
Content-Security-Policy: default-src 'self'; style-src 'self' 'nonce-N2M0MDhkN2EtMmRkYi00MTExLWFhM2YtNDhkNTc4NGJhMjA3';
```

**Important:** The nonce must:
- Be generated per request
- Remain unpredictable
- Match across the `<meta>` tag, `registry.styles({ nonce })`, and CSP header

## Style Deduplication

styled-jsx automatically deduplicates styles across the tree. When the client loads, it:

1. Checks for styles already in the HTML
2. Only injects new styles that weren't server-rendered
3. Removes duplicate styles

This is why using `StyleRegistry` is **paramount** — it ensures correct style diffing between server and client.

## Next.js Integration

Next.js 12+ automatically handles SSR. Simply use `<style jsx>` in your components:

```jsx
// pages/index.js
export default function Home() {
  return (
    <div>
      <h1>Hello World</h1>
      <style jsx>{`
        h1 { color: blue; }
      `}</style>
    </div>
  )
}
```

Next.js manages the `StyleRegistry` automatically during server rendering.

## Performance Considerations

- Each SSR request should have its own registry to avoid style leakage between requests
- Call `registry.flush()` after extracting styles if doing multiple renders
- The registry system is designed for concurrent requests and is thread-safe
