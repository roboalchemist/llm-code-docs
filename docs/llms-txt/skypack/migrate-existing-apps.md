# Source: https://docs.skypack.dev/skypack-cdn/code/migrate-existing-apps.md

# Migrate Existing Apps

## Webpack Plugin (Coming soon)

See [Plugins](https://docs.skypack.dev/skypack-cdn/code/broken-reference)

## deps.js

This is a pattern already popular within the Deno community. To manage multiple dependency URLs in one place, you can create a `deps.js` file somewhere in your application.

```javascript
// src/deps.js
export {default as React} from 'https://cdn.skypack.dev/react';
export {default as ReactDOM} from 'https://cdn.skypack.dev/react-dom';
```

Then, anywhere in your application you can do:

```javascript
// src/index.js
import {React, ReactDOM} from './deps.js';
```

## Import Maps (Experimental)
