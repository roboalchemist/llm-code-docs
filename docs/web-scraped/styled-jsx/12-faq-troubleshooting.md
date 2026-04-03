# FAQ and Troubleshooting

## Common Issues

### Warning: unknown `jsx` prop on `<style>` tag

**Error:**
```
Warning: Received `true` for a non-boolean attribute `jsx`.
```

**Cause:** Your styles were not compiled by styled-jsx's Babel plugin.

**Solution:** 
1. Verify `styled-jsx/babel` is in your `.babelrc` plugins array
2. Ensure the file is being transpiled by Babel
3. Clear your build cache and rebuild

## Styling Third-Party Components

### How do I style a third-party component that doesn't accept a className prop?

Use `:global()` to create global selectors within scoped styles:

```jsx
import ExternalComponent from 'external-lib'

export default () => (
  <div>
    <ExternalComponent />

    <style jsx>{`
      /* "div" is scoped, but ".nested-element" is global */
      div > :global(.nested-element) {
        color: red;
      }
    `}</style>
  </div>
)
```

**Best Practice:** Use the child selector `>` to limit the scope of global rules.

### How do I style child components from a parent?

Option 1: Use `css.resolve` if the child component accepts a className prop:

```jsx
import Link from 'some-library'
import css from 'styled-jsx/css'

const { className, styles } = css.resolve`
  a { color: green }
`

export default () => (
  <div>
    <Link className={className}>About</Link>
    {styles}
  </div>
)
```

Option 2: Use `:global()` for components that don't accept a className:

```jsx
<style jsx>{`
  div > :global(.child) {
    color: blue;
  }
`}</style>
```

## Returning Arrays of Components

### Can I return an array of components when using React 16?

No. However, React Fragments are supported in React 16.2.0+:

```jsx
const StyledImage = ({ src, alt = '' }) => (
  <React.Fragment>
    <img src={src} alt={alt} />
    <style jsx>{`
      img {
        max-width: 100%;
      }
    `}</style>
  </React.Fragment>
)
```

Or use the shorthand syntax:

```jsx
const StyledImage = ({ src, alt = '' }) => (
  <>
    <img src={src} alt={alt} />
    <style jsx>{`
      img {
        max-width: 100%;
      }
    `}</style>
  </>
)
```

## Production Issues

### Some styles are missing in production

**Cause:** The `optimizeForSpeed` option can sometimes cause issues with style collection on the client.

**Solution:** Ensure you're using the correct SSR registry pattern:

```jsx
import { StyleRegistry, useStyleRegistry } from 'styled-jsx'

function Styles() {
  const registry = useStyleRegistry()
  return <>{registry.styles()}</>
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

Reference: [GitHub Issue #319](https://github.com/vercel/styled-jsx/issues/319#issuecomment-349239326)

## Testing and Snapshots

### How do I avoid styled-jsx artifacts in test snapshots?

Use `styled-jsx/babel-test` plugin in your test environment:

```json
{
  "env": {
    "test": {
      "plugins": ["styled-jsx/babel-test"]
    }
  }
}
```

This removes the `jsx` attribute from `<style>` tags, keeping snapshots clean.

### styled-jsx/css throws an error in tests

When using `styled-jsx/babel-test`, you must mock `styled-jsx/css`:

```js
jest.mock('styled-jsx/css', () => ({
  default: '',
  global: '',
  resolve: { className: '', styles: '' }
}))
```

## Advanced Usage

### How do I build a component library with styled-jsx?

See [Building Component Libraries](#advanced-topics) in the Advanced Topics section.

Key steps:
1. List styled-jsx as a peer dependency
2. Include the Babel plugin configuration
3. Test in consuming projects

### How do I use styled-jsx with TypeScript?

Add a triple-slash reference:

```typescript
/// <reference types="styled-jsx" />
```

Or configure in `tsconfig.json`:

```json
{
  "compilerOptions": {
    "types": ["styled-jsx"]
  }
}
```

When using Babel with TypeScript, set `"jsx": "preserve"` in tsconfig.json.

### How do I enable strict CSP?

Generate a nonce per request and pass it to `registry.styles({ nonce })`:

```js
const nonce = Buffer.from(nanoid()).toString('base64')
const styles = registry.styles({ nonce })
```

Set the meta tag and CSP header with the same nonce value.

## Performance

### Is styled-jsx fast?

Yes. styled-jsx features:
- ~3KB gzipped bundle size
- Fast Babel transpilation
- Optimized runtime style injection
- Efficient style de-duplication

Runtime overhead is minimal, especially with `optimizeForSpeed` enabled.

### How do I optimize performance?

1. **Split static and dynamic CSS** into separate `<style>` tags
2. **Use className toggling** for preset variants
3. **Enable `optimizeForSpeed`** in production
4. **Memoize theme objects** to avoid unnecessary re-renders
5. **Use the `resolve` tag** for external styles with dynamic props

## Compatibility

### What React versions are supported?

styled-jsx works with React 16.8+ (with Hooks in 16.8.0+).

For React 16.2+, use React Fragments instead of arrays.

### Does styled-jsx work with Next.js?

Yes. Next.js 12+ automatically configures styled-jsx. Earlier versions require manual setup.

### What about SSR frameworks other than Next.js?

styled-jsx supports any React SSR framework. Use the `StyleRegistry` and `useStyleRegistry` patterns for manual setup.

## Getting Help

- [GitHub Issues](https://github.com/vercel/styled-jsx/issues)
- [GitHub Discussions](https://github.com/vercel/styled-jsx/discussions)
- [Vercel Community](https://vercel.community)
