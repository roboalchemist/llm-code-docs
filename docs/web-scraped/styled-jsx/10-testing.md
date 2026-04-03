# Testing with styled-jsx

## Testing in Jest and Enzyme

When testing components with styled-jsx, the generated artifacts (scoped classnames like `jsx-123` and vendor prefixes) can create noisy snapshots.

### Excluding styled-jsx from Tests

Configure Babel to exclude the `styled-jsx/babel` plugin in the test environment:

```json
{
  "env": {
    "production": {
      "plugins": ["styled-jsx/babel"]
    },
    "development": {
      "plugins": ["styled-jsx/babel"]
    },
    "test": {
      "plugins": ["styled-jsx/babel-test"]
    }
  }
}
```

However, this causes warnings:

```
console.error node_modules/react-dom/cjs/react-dom.development.js:527
   Warning: Received `true` for a non-boolean attribute `jsx`.
```

### Using babel-test Plugin

Use `styled-jsx/babel-test` which strips `jsx` attributes from all `<style>` tags:

```json
{
  "env": {
    "test": {
      "plugins": ["styled-jsx/babel-test"]
    }
  }
}
```

This eliminates the warning and keeps snapshots clean by removing styled-jsx artifacts.

## Using styled-jsx/css in Tests

When using `styled-jsx/babel-test`, `styled-jsx/css` throws an error:

```
styled-jsx/css: if you are getting this error it means that your `css` 
tagged template literals were not transpiled.
```

### Solution: Mock styled-jsx/css

Create a mock for `styled-jsx/css`:

```js
// __mocks__/styled-jsx-css.js
module.exports = {
  default: '',
  global: '',
  resolve: { className: '', styles: '' }
}
```

Tell Jest to use the mock:

```js
// jest.config.js
module.exports = {
  moduleNameMapper: {
    '^styled-jsx/css$': '<rootDir>/__mocks__/styled-jsx-css.js'
  }
}
```

Or mock it directly in your test:

```js
jest.mock('styled-jsx/css', () => ({
  default: '',
  global: '',
  resolve: { className: '', styles: '' }
}))

// Your tests here
```

Reference: [Reducing styled-jsx noise in Jest snapshots](https://kevinjalbert.com/jest-snapshots-reducing-styled-jsx-noise/)

## Example Test Setup

```js
// package.json
{
  "jest": {
    "testEnvironment": "jsdom",
    "moduleNameMapper": {
      "^styled-jsx/css$": "<rootDir>/__mocks__/styled-jsx-css.js"
    }
  }
}

// .babelrc
{
  "env": {
    "test": {
      "plugins": ["styled-jsx/babel-test"]
    }
  }
}
```

## Testing SSR

For server-side rendering tests, you need to handle the `StyleRegistry`:

```jsx
import React from 'react'
import ReactDOM from 'react-dom/server'
import { StyleRegistry } from 'styled-jsx'
import MyComponent from './MyComponent'

test('renders with styles', () => {
  const html = ReactDOM.renderToString(
    <StyleRegistry>
      <MyComponent />
    </StyleRegistry>
  )
  
  expect(html).toContain('<style')
})
```

## Testing Dynamic Styles

For components with dynamic styles, test both static and dynamic variants:

```jsx
const DynamicButton = ({ size, color }) => (
  <button style={{ padding: size }}>
    Click me
    <style jsx>{`
      button {
        background: ${color};
      }
    `}</style>
  </button>
)

test('renders with custom size and color', () => {
  const { container } = render(
    <DynamicButton size="20px" color="red" />
  )
  
  const button = container.querySelector('button')
  expect(button).toHaveStyle('padding: 20px')
})
```

## Performance Testing

styled-jsx is optimized for performance. Test rendering performance with:

```js
import React from 'react'
import ReactDOM from 'react-dom'
import MyComponent from './MyComponent'

performance.mark('render-start')
ReactDOM.render(<MyComponent />, document.getElementById('root'))
performance.mark('render-end')
performance.measure('render', 'render-start', 'render-end')

const measure = performance.getEntriesByName('render')[0]
console.log(`Render time: ${measure.duration}ms`)
```

## Snapshot Testing Best Practices

1. **Use babel-test plugin** to remove styled-jsx artifacts
2. **Update snapshots carefully** when making style changes
3. **Test behavior separately** from snapshots (verify styles work in the browser)
4. **Mock external styles** from `styled-jsx/css`
