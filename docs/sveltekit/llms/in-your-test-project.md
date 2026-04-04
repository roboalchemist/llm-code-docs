# In your test project
npx sv add file:../path/to/my-addon
```

This allows you to iterate quickly without publishing to npm.

## Testing with `sv/testing`

The `sv/testing` module provides utilities for testing your add-on:

```js
import { test, expect } from 'vitest';
import { setupTest } from 'sv/testing';
import addon from './index.js';

test('adds hello message', async () => {
 const { content } = await setupTest({
  addon,
  options: { who: 'World' },
  files: {
   'src/routes/+page.svelte': '<h1>Welcome</h1>'
  }
 });

 expect(content('src/routes/+page.svelte')).toContain('Hello World!');
});
```

## Publishing to npm

### Package structure

Your add-on must have `sv` as a dependency in `package.json`:

```json
{
 "name": "@your-org/sv",
 "version": "1.0.0",
 "type": "module",
 "exports": {
  ".": "./dist/index.js"
 },
 "dependencies": {
  "sv": "^0.11.0"
 },
 "keywords": ["sv-add"]
}
```

> [!NOTE]
> Add the `sv-add` keyword so users can discover your add-on on npm.

### Export options

Your package can export the add-on in two ways:

1. **Default export** (recommended for dedicated add-on packages):

   ```json
   {
    "exports": {
     ".": "./dist/index.js"
    }
   }
   ```

2. **`/sv` export** (for packages that have other functionality):

   ```json
   {
    "exports": {
     ".": "./dist/main.js",
     "./sv": "./dist/addon.js"
    }
   }
   ```

### Naming conventions

- **Scoped packages**: Use `@your-org/sv` as the package name. Users can then install with just `npx sv add @your-org`.
- **Regular packages**: Any name works. Users install with `npx sv add your-package-name`.

## Version compatibility

Your add-on should specify the minimum `sv` version it requires in `package.json`. If a user's `sv` version has a different major version than what your add-on was built for, they will see a compatibility warning.