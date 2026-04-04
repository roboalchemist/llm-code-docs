# Source: https://rspack.dev/api/loader-api/context.md

# Source: https://rspack.dev/config/context.md

CC 4.0 License> The content of this section is derived from the content of the following links and is subject to the CC BY 4.0 license.
> 
> - [https://webpack.js.org/configuration/entry-context/#context](https://webpack.js.org/configuration/entry-context/#context)
> 
> The following contents can be assumed to be the result of modifications and deletions based on the original contents if not specifically stated.
> 
> 


# Context

- Type: `string`
- Default:`process.cwd()`


The `context` configuration is used to set the base directory for Rspack builds.

`context` is an absolute path that is used as the base path for relative paths in Rspack configurations such as [entry](/config/entry.md) and [output](/config/output.md).

By default, Rspack uses the current working directory of the Node.js process as the base directory. In most cases, it is recommended to set a base directory manually, rather than relying on the current working directory of Node.js.

## Example

For example, you can use [`__dirname`](https://nodejs.org/docs/latest/api/modules.html#__dirname) as the base directory:


**ESM**

```js title="rspack.config.mjs"
import { dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = dirname(fileURLToPath(import.meta.url));

export default {
  context: __dirname,
  entry: {
    main: './src/index.js',
  },
};
```


**CJS**

```js title="rspack.config.cjs"
module.exports = {
  context: __dirname,
  entry: {
    main: './src/index.js',
  },
};
```


In the above example, the `main` entry will be resolved based on the `path.join(__dirname, './src/index.js')` path.
