# Source: https://kreya.app/docs/scripting-and-tests/general.md

# General script API reference

The following scripting modules and namespaces are available in all Kreya scripts ([Kreya Scripts](/docs/scripting-and-tests/invoker-scripts.md) and [Kreya Operation scripts](/docs/scripting-and-tests/operation-scripts.md)). It is also possible to import external modules, see [importing external modules](#importing-external-modules) and [Sharing code](#sharing-code).

## Namespaces[​](#namespaces "Direct link to Namespaces")

Namespaces can be accessed directly through their name. An example for the [`trace`](/docs/scripting-and-tests/general/kreya-base-script-api.md#trace) function of the [`kreya`](/docs/scripting-and-tests/general/kreya-base-script-api.md) namespace:

```
kreya.trace('Hello world!');
```

| Namespace                                                             | Description                  |
| --------------------------------------------------------------------- | ---------------------------- |
| [`kreya`](/docs/scripting-and-tests/general/kreya-base-script-api.md) | General Kreya Scripting APIs |

## Modules[​](#modules "Direct link to Modules")

These modules are provided and can be imported. An example for the `join` function of the `path` module:

```
import { join } from "path";`

const grpcOperationPath = join("../", "gRPC", "my-operation");
```

| Module                                                         | Description                                                            |
| -------------------------------------------------------------- | ---------------------------------------------------------------------- |
| [`chai`](https://www.chaijs.com)                               | Chai is an assertion library and can be used to assert in Kreya tests. |
| [`path`](/docs/scripting-and-tests/general/path-script-api.md) | Provides utilities for working with file and directory paths.          |

### Importing external modules[​](#importing-external-modules "Direct link to Importing external modules")

While Kreya bundles some modules, that may not be enough for some use cases. That is why importing external modules is also possible. Currently, only external ESM modules are supported. You may import external modules directly by URL or as local dependencies.

#### Import from CDNs[​](#import-from-cdns "Direct link to Import from CDNs")

```
// Imported directly from a CDN URL
import { snakeCase } from 'https://esm.sh/change-case';

const snakeCased = snakeCase('my message');
kreya.test('Snake case', () => expect(snakeCased).to.eq('my_message'));
```

#### Import from a local source[​](#import-from-a-local-source "Direct link to Import from a local source")

Kreya supports importing local modules. Kreya searches for the file in the same directory as the script file and in all parent directories. Either the module is declared in a package.json file (the module must be installed, Kreya does not perform a package restore) or the file is directly available as `{module-name}.js` or `{module-name}/index.js`.

```
import { formatDistance } from 'date-fns';

const dayDistance = formatDistance(new Date(2020, 1, 1), new Date(2020, 1, 3), {
  addSuffix: true,
});
kreya.test('Day distance', () => expect(dayDistance).to.eq('2 days ago'));
```

## Sharing code[​](#sharing-code "Direct link to Sharing code")

A typical scenario is to share test code among multiple operations. This is where [importing external modules](#importing-external-modules) comes in handy. As an example, place a file named `shared.js` in the Kreya project directory with the following content:

shared.js

```
import { expect } from 'chai';

export function init() {
  kreya.trace('hello from shared file');
}

export function addTestForSuccessfulResponse() {
  kreya.rest.onCallCompleted(call => {
    kreya.test('status is success', () => expect(call.status.isSuccess).to.be.true);
    kreya.test('Status code', () => expect(call.status.code).to.equal(200));
  });
}
```

Then, in the Script tab of a REST operation, we can import these shared functions:

```
import { init, addTestForSuccessfulResponse } from 'shared.js';

init();
addTestForSuccessfulResponse();
```
