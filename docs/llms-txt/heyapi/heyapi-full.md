# Heyapi Documentation

Source: https://heyapi.dev/llms-full.txt

---

---
url: /CHANGELOG.md
---
# @docs/openapi-ts

## 0.10.4

### Patch Changes

* docs: add bigint section to transformers ([#2865](https://github.com/hey-api/openapi-ts/pull/2865)) ([`ba4d9bf`](https://github.com/hey-api/openapi-ts/commit/ba4d9bf603d8c897016fd1775d13e184111ace17)) by [@wn-mitch](https://github.com/wn-mitch)

## 0.10.3

### Patch Changes

* chore: clarify TanStack Query reactivity in Vue ([#2745](https://github.com/hey-api/openapi-ts/pull/2745)) ([`5d06dbd`](https://github.com/hey-api/openapi-ts/commit/5d06dbdf8c2a834ecefdd7305b59572470f45a7e)) by [@9M6](https://github.com/9M6)

## 0.10.2

### Patch Changes

* [#2117](https://github.com/hey-api/openapi-ts/pull/2117) [`a1435b9`](https://github.com/hey-api/openapi-ts/commit/a1435b915a272d9ffa599c194ee52c2a33f77fcd) Thanks [@johnny-mh](https://github.com/johnny-mh)! - docs: add docs for `input.patch` feature

## 0.10.1

### Patch Changes

* [#1774](https://github.com/hey-api/openapi-ts/pull/1774) [`c0b36b9`](https://github.com/hey-api/openapi-ts/commit/c0b36b95645d484034c3af145c5554867568979b) Thanks [@mrlubos](https://github.com/mrlubos)! - docs: announce Hey API platform

## 0.10.0

### Minor Changes

* [#1568](https://github.com/hey-api/openapi-ts/pull/1568) [`465410c`](https://github.com/hey-api/openapi-ts/commit/465410c201eb19e737e3143ad53a146e95f80107) Thanks [@mrlubos](https://github.com/mrlubos)! - feat: change the default parser

## 0.9.0

### Minor Changes

* [#1511](https://github.com/hey-api/openapi-ts/pull/1511) [`4e8064d`](https://github.com/hey-api/openapi-ts/commit/4e8064d9a589e14b42d2b1a329e2436f242884da) Thanks [@mrlubos](https://github.com/mrlubos)! - feat: add watch mode

  ## Watch Mode

  ::: warning
  Watch mode currently supports only remote files via URL.
  :::

  If your schema changes frequently, you may want to automatically regenerate the output during development. To watch your input file for changes, enable `watch` mode in your configuration or pass the `--watch` flag to the CLI.

  ### Config

  ```js
  export default {
    client: '@hey-api/client-fetch',
    input: 'path/to/openapi.json',
    output: 'src/client',
    watch: true,
  };
  ```

  ### CLI

  ```sh
  npx @hey-api/openapi-ts \
    -c @hey-api/client-fetch \
    -i path/to/openapi.json \
    -o src/client \
    -w
  ```

### Patch Changes

* [#1496](https://github.com/hey-api/openapi-ts/pull/1496) [`1e418ba`](https://github.com/hey-api/openapi-ts/commit/1e418ba760b9903326ec37009651c32e195e24a9) Thanks [@mrlubos](https://github.com/mrlubos)! - docs: split output section into multiple pages

## 0.8.0

### Minor Changes

* [#1447](https://github.com/hey-api/openapi-ts/pull/1447) [`200821b`](https://github.com/hey-api/openapi-ts/commit/200821b3ceea8ffca7656fe3f6e2ef98b7110a2a) Thanks [@mrlubos](https://github.com/mrlubos)! - fix: revert license to MIT

### Patch Changes

* [#1430](https://github.com/hey-api/openapi-ts/pull/1430) [`9cec9e8`](https://github.com/hey-api/openapi-ts/commit/9cec9e8582c12a8c041b922d9587e16f6f19782a) Thanks [@mrlubos](https://github.com/mrlubos)! - docs: add validators page

## 0.7.4

### Patch Changes

* [#1420](https://github.com/hey-api/openapi-ts/pull/1420) [`8010dbb`](https://github.com/hey-api/openapi-ts/commit/8010dbb1ab8b91d1d49d5cf16276183764a63ff3) Thanks [@mrlubos](https://github.com/mrlubos)! - docs: add buildUrl() method to Axios client page

## 0.7.3

### Patch Changes

* [#1316](https://github.com/hey-api/openapi-ts/pull/1316) [`a79fac8`](https://github.com/hey-api/openapi-ts/commit/a79fac8919ed29eec7195cbd441ffa38b559d63c) Thanks [@mrlubos](https://github.com/mrlubos)! - docs: add Plugins page

## 0.7.2

### Patch Changes

* [#1253](https://github.com/hey-api/openapi-ts/pull/1253) [`01dee3d`](https://github.com/hey-api/openapi-ts/commit/01dee3df879232939e43355231147b3d910fb482) Thanks [@mrlubos](https://github.com/mrlubos)! - fix: update sponsorship links

## 0.7.1

### Patch Changes

* [#1222](https://github.com/hey-api/openapi-ts/pull/1222) [`ceb4363`](https://github.com/hey-api/openapi-ts/commit/ceb4363d52893ebe947e21aac402b868ff2820d4) Thanks [@mrlubos](https://github.com/mrlubos)! - feat: add support for @tanstack/angular-query-experimental package

## 0.7.0

### Minor Changes

* [#1201](https://github.com/hey-api/openapi-ts/pull/1201) [`972a93a`](https://github.com/hey-api/openapi-ts/commit/972a93a91a945cc9ead73c08bb0fa9ee120433ba) Thanks [@mrlubos](https://github.com/mrlubos)! - feat: make plugins first-class citizens

  This release makes plugins first-class citizens. In order to achieve that, the following breaking changes were introduced.

  ### Removed CLI options

  The `--types`, `--schemas`, and `--services` CLI options have been removed. You can list which plugins you'd like to use explicitly by passing a list of plugins as `--plugins <plugin1> <plugin2>`

  ### Removed `*.export` option

  Previously, you could explicitly disable export of certain artifacts using the `*.export` option or its shorthand variant. These were both removed. You can now disable export of specific artifacts by manually defining an array of `plugins` and excluding the unwanted plugin.

  ::: code-group

  ```js [shorthand]
  export default {
    client: '@hey-api/client-fetch',
    input: 'path/to/openapi.json',
    output: 'src/client',
    schemas: false, // [!code --]
    plugins: ['@hey-api/types', '@hey-api/services'], // [!code ++]
  };
  ```

  ```js [*.export]
  export default {
    client: '@hey-api/client-fetch',
    input: 'path/to/openapi.json',
    output: 'src/client',
    schemas: {
      export: false, // [!code --]
    },
    plugins: ['@hey-api/types', '@hey-api/services'], // [!code ++]
  };
  ```

  :::

  ### Renamed `schemas.name` option

  Each plugin definition contains a `name` field. This was conflicting with the `schemas.name` option. As a result, it has been renamed to `nameBuilder`.

  ```js
  export default {
    client: '@hey-api/client-fetch',
    input: 'path/to/openapi.json',
    output: 'src/client',
    schemas: {
      name: (name) => `${name}Schema`, // [!code --]
    },
    plugins: [
      // ...other plugins
      {
        nameBuilder: (name) => `${name}Schema`, // [!code ++]
        name: '@hey-api/schemas',
      },
    ],
  };
  ```

  ### Removed `services.include` shorthand option

  Previously, you could use a string value as a shorthand for the `services.include` configuration option. You can now achieve the same result using the `include` option.

  ```js
  export default {
    client: '@hey-api/client-fetch',
    input: 'path/to/openapi.json',
    output: 'src/client',
    services: '^MySchema', // [!code --]
    plugins: [
      // ...other plugins
      {
        include: '^MySchema', // [!code ++]
        name: '@hey-api/services',
      },
    ],
  };
  ```

  ### Renamed `services.name` option

  Each plugin definition contains a `name` field. This was conflicting with the `services.name` option. As a result, it has been renamed to `serviceNameBuilder`.

  ```js
  export default {
    client: '@hey-api/client-fetch',
    input: 'path/to/openapi.json',
    output: 'src/client',
    services: {
      name: '{{name}}Service', // [!code --]
    },
    plugins: [
      // ...other plugins
      {
        serviceNameBuilder: '{{name}}Service', // [!code ++]
        name: '@hey-api/services',
      },
    ],
  };
  ```

  ### Renamed `types.dates` option

  Previously, you could set `types.dates` to a boolean or a string value, depending on whether you wanted to transform only type strings into dates, or runtime code too. Many people found these options confusing, so they have been simplified to a boolean and extracted into a separate `@hey-api/transformers` plugin.

  ```js
  export default {
    client: '@hey-api/client-fetch',
    input: 'path/to/openapi.json',
    output: 'src/client',
    types: {
      dates: 'types+transform', // [!code --]
    },
    plugins: [
      // ...other plugins
      {
        dates: true, // [!code ++]
        name: '@hey-api/transformers',
      },
    ],
  };
  ```

  ### Removed `types.include` shorthand option

  Previously, you could use a string value as a shorthand for the `types.include` configuration option. You can now achieve the same result using the `include` option.

  ```js
  export default {
    client: '@hey-api/client-fetch',
    input: 'path/to/openapi.json',
    output: 'src/client',
    types: '^MySchema', // [!code --]
    plugins: [
      // ...other plugins
      {
        include: '^MySchema', // [!code ++]
        name: '@hey-api/types',
      },
    ],
  };
  ```

  ### Renamed `types.name` option

  Each plugin definition contains a `name` field. This was conflicting with the `types.name` option. As a result, it has been renamed to `style`.

  ```js
  export default {
    client: '@hey-api/client-fetch',
    input: 'path/to/openapi.json',
    output: 'src/client',
    types: {
      name: 'PascalCase', // [!code --]
    },
    plugins: [
      // ...other plugins
      {
        name: '@hey-api/types',
        style: 'PascalCase', // [!code ++]
      },
    ],
  };
  ```

## 0.6.2

### Patch Changes

* [#1162](https://github.com/hey-api/openapi-ts/pull/1162) [`1c85c24`](https://github.com/hey-api/openapi-ts/commit/1c85c24af514e9781aab1960298caa28effef5d3) Thanks [@mrlubos](https://github.com/mrlubos)! - docs: add Zod plugin page

## 0.6.1

### Patch Changes

* [#1151](https://github.com/hey-api/openapi-ts/pull/1151) [`587791d`](https://github.com/hey-api/openapi-ts/commit/587791dfede0167fbed229281467e4c4875936f5) Thanks [@mrlubos](https://github.com/mrlubos)! - fix: update website domain, add license documentation

## 0.6.0

### Minor Changes

* [#1009](https://github.com/hey-api/openapi-ts/pull/1009) [`c6b044d`](https://github.com/hey-api/openapi-ts/commit/c6b044d0bc9dc54cb0eb58d23438f4e1d050cb38) Thanks [@mrlubos](https://github.com/mrlubos)! - feat: change schemas name pattern, add schemas.name option

## 0.5.11

### Patch Changes

* [#978](https://github.com/hey-api/openapi-ts/pull/978) [`2e051a5`](https://github.com/hey-api/openapi-ts/commit/2e051a596302c2e103dca25951a07b4aae1e9e23) Thanks [@mrlubos](https://github.com/mrlubos)! - docs: add basic TanStack Query plugin description

## 0.5.10

### Patch Changes

* [#830](https://github.com/hey-api/openapi-ts/pull/830) [`babf11a`](https://github.com/hey-api/openapi-ts/commit/babf11ae082af642ac71cfee9c523cc976132a50) Thanks [@mrlubos](https://github.com/mrlubos)! - docs: split clients documentation into separate pages

* [#830](https://github.com/hey-api/openapi-ts/pull/830) [`323d0a0`](https://github.com/hey-api/openapi-ts/commit/323d0a03c6560f27d0ce5eee1708ee16dc395532) Thanks [@mrlubos](https://github.com/mrlubos)! - docs: remove interceptors page in favour of per-client sections

* [#830](https://github.com/hey-api/openapi-ts/pull/830) [`babf11a`](https://github.com/hey-api/openapi-ts/commit/babf11ae082af642ac71cfee9c523cc976132a50) Thanks [@mrlubos](https://github.com/mrlubos)! - docs: add v0.52.0 migration

## 0.5.9

### Patch Changes

* [#828](https://github.com/hey-api/openapi-ts/pull/828) [`82a4696`](https://github.com/hey-api/openapi-ts/commit/82a4696b0b209ea2d9147f47f213479e61aed3d7) Thanks [@mrlubos](https://github.com/mrlubos)! - fix: add migration guide for v0.51.0

## 0.5.8

### Patch Changes

* [#613](https://github.com/hey-api/openapi-ts/pull/613) [`b3786dc`](https://github.com/hey-api/openapi-ts/commit/b3786dc6749d8d4ae26bb63322e124663f881741) Thanks [@mrlubos](https://github.com/mrlubos)! - docs: add Axios client documentation

## 0.5.7

### Patch Changes

* [#632](https://github.com/hey-api/openapi-ts/pull/632) [`9c16bc7`](https://github.com/hey-api/openapi-ts/commit/9c16bc71cde48c0cb700b7e720a9e2ad56ec5f02) Thanks [@mrlubos](https://github.com/mrlubos)! - docs: add output page

## 0.5.6

### Patch Changes

* docs: add fetch client documentation ([#602](https://github.com/hey-api/openapi-ts/pull/602))

* docs: add migration notes for v0.46.0 ([#602](https://github.com/hey-api/openapi-ts/pull/602))

## 0.5.5

### Patch Changes

* docs: add migration for v0.45.0 ([#569](https://github.com/hey-api/openapi-ts/pull/569))

## 0.5.4

### Patch Changes

* docs: add format and lint migration for 0.44.0 ([#546](https://github.com/hey-api/openapi-ts/pull/546))

## 0.5.3

### Patch Changes

* docs: add links to homepage ([#489](https://github.com/hey-api/openapi-ts/pull/489))

* feat: remove enum postfix, use typescript enums in types when generated, export enums from types.gen.ts ([#498](https://github.com/hey-api/openapi-ts/pull/498))

* docs: add examples ([#476](https://github.com/hey-api/openapi-ts/pull/476))

## 0.5.2

### Patch Changes

* docs: add github action to integrations ([#451](https://github.com/hey-api/openapi-ts/pull/451))

## 0.5.1

### Patch Changes

* docs: add tanstack-query and http clients sections ([#436](https://github.com/hey-api/openapi-ts/pull/436))

## 0.5.0

### Minor Changes

* feat: allow choosing naming convention for types ([#402](https://github.com/hey-api/openapi-ts/pull/402))

## 0.4.0

### Minor Changes

* docs: add integrations ([#394](https://github.com/hey-api/openapi-ts/pull/394))

* feat: rename generated files ([#363](https://github.com/hey-api/openapi-ts/pull/363))

### Patch Changes

* docs: add enums migration ([#358](https://github.com/hey-api/openapi-ts/pull/358))

## 0.3.0

### Minor Changes

* fix: rename write to dryRun and invert value ([#326](https://github.com/hey-api/openapi-ts/pull/326))

### Patch Changes

* docs: update contributing guidelines ([#347](https://github.com/hey-api/openapi-ts/pull/347))

## 0.2.2

### Patch Changes

* docs: add migration notes ([#306](https://github.com/hey-api/openapi-ts/pull/306))

## 0.2.1

### Patch Changes

* fix(config): rename exportSchemas to schemas ([#288](https://github.com/hey-api/openapi-ts/pull/288))

## 0.2.0

### Minor Changes

* docs: add support for localization of docs ([#251](https://github.com/hey-api/openapi-ts/pull/251))

### Patch Changes

* docs: add logo ([#250](https://github.com/hey-api/openapi-ts/pull/250))

---

---
url: /openapi-ts/plugins/adonis.md
description: AdonisJS plugin for Hey API. Compatible with all our features.
---

# AdonisJS soon

### About

[AdonisJS](https://adonisjs.com) is a TypeScript-first web framework for building web apps and API servers. It comes with support for testing, modern tooling, an ecosystem of official packages, and more.

## Sponsors

Hey API is sponsor-funded. If you rely on Hey API in production, consider becoming a [sponsor](https://github.com/sponsors/hey-api) to accelerate the roadmap.

---

---
url: /openapi-ts/plugins/ajv.md
description: Ajv plugin for Hey API. Compatible with all our features.
---

# Ajv soon

### About

[Ajv](https://ajv.js.org) is the fastest JSON validator for Node.js and browser.

## Sponsors

Hey API is sponsor-funded. If you rely on Hey API in production, consider becoming a [sponsor](https://github.com/sponsors/hey-api) to accelerate the roadmap.

---

---
url: /openapi-ts/clients/angular/v19.md
description: >-
  Generate a type-safe Angular v19 client from OpenAPI with the Angular client
  for openapi-ts. Fully compatible with validators, transformers, and all core
  features.
---

::: warning
Angular client is currently in beta. The interface might change before it becomes stable. We encourage you to leave feedback on [GitHub](https://github.com/hey-api/openapi-ts/issues).
:::

### About

[Angular](https://angular.dev/) is a web framework that empowers developers to build fast, reliable applications.

The Angular client for Hey API generates a type-safe client from your OpenAPI spec, fully compatible with validators, transformers, and all core features.

### Collaborators

## Features

* Angular v19 support
* seamless integration with `@hey-api/openapi-ts` ecosystem
* type-safe response data and errors
* support for [`@Injectable()`](https://angular.dev/api/core/Injectable) decorators
* response data validation and transformation
* access to the original request and response
* granular request and response customization options
* minimal learning curve thanks to extending the underlying technology
* support bundling inside the generated output

## Installation

In your [configuration](/openapi-ts/get-started), add `@hey-api/client-angular` to your plugins and you'll be ready to generate client artifacts. :tada:

::: code-group

```js [config]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: ['@hey-api/client-angular'], // [!code ++]
};
```

```sh [cli]
npx @hey-api/openapi-ts \
  -i hey-api/backend \
  -o src/client \
  -c @hey-api/client-angular # [!code ++]
```

:::

### Providers

You can use the Angular client in your application by adding `provideHeyApiClient` to your providers.

```ts
import { provideHeyApiClient, client } from './client/client.gen';

export const appConfig: ApplicationConfig = {
  providers: [
    provideHttpClient(withFetch()),
    provideHeyApiClient(client), // [!code ++]
  ],
};
```

## Configuration

The Angular client is built as a thin wrapper on top of Angular, extending its functionality to work with Hey API. If you're already familiar with Angular, configuring your client will feel like working directly with Angular.

When we installed the client above, it created a [`client.gen.ts`](/openapi-ts/output#client) file. You will most likely want to configure the exported `client` instance. There are two ways to do that.

### `setConfig()`

This is the simpler approach. You can call the `setConfig()` method at the beginning of your application or anytime you need to update the client configuration. You can pass any `HttpRequest` configuration option to `setConfig()`, and even your own [`httpClient`](#custom-httpclient) implementation.

```js
import { client } from 'client/client.gen';

client.setConfig({
  baseUrl: 'https://example.com',
});
```

The disadvantage of this approach is that your code may call the `client` instance before it's configured for the first time. Depending on your use case, you might need to use the second approach.

### Runtime API

Since `client.gen.ts` is a generated file, we can't directly modify it. Instead, we can tell our configuration to use a custom file implementing the Runtime API. We do that by specifying the `runtimeConfigPath` option.

```js
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    {
      name: '@hey-api/client-angular',
      runtimeConfigPath: './src/hey-api.ts', // [!code ++]
    },
  ],
};
```

In our custom file, we need to export a `createClientConfig()` method. This function is a simple wrapper allowing us to override configuration values.

::: code-group

```ts [hey-api.ts]
import type { CreateClientConfig } from './client/client.gen';

export const createClientConfig: CreateClientConfig = (config) => ({
  ...config,
  baseUrl: 'https://example.com',
});
```

:::

With this approach, `client.gen.ts` will call `createClientConfig()` before initializing the `client` instance. If needed, you can still use `setConfig()` to update the client configuration later.

### `createClient()`

You can also create your own client instance. You can use it to manually send requests or point it to a different domain.

```js
import { createClient } from './client/client';

const myClient = createClient({
  baseUrl: 'https://example.com',
});
```

You can also pass this instance to any SDK function through the `client` option. This will override the default instance from `client.gen.ts`.

```js
const response = await getFoo({
  client: myClient,
});
```

### SDKs

Alternatively, you can pass the client configuration options to each SDK function. This is useful if you don't want to create a client instance for one-off use cases.

```js
const response = await getFoo({
  baseUrl: 'https://example.com', // <-- override default configuration
});
```

## `@Injectable`

If you prefer to use the [`@Injectable()`](https://angular.dev/api/core/Injectable) decorators, set the `asClass` option in your SDK plugin to `true`.

::: code-group

```ts [example]
@Injectable({ providedIn: 'root' })
export class FooService {
  // class methods
}
```

```js [config]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    '@hey-api/client-angular',
    {
      name: '@hey-api/sdk',
      asClass: true, // [!code ++]
    },
  ],
};
```

:::

## Interceptors

::: warning
This section is under construction. We appreciate your patience.
:::

## Auth

::: warning
This section is under construction. We appreciate your patience.
:::

## Build URL

If you need to access the compiled URL, you can use the `buildUrl()` method. It's loosely typed by default to accept almost any value; in practice, you will want to pass a type hint.

```ts
type FooData = {
  path: {
    fooId: number;
  };
  query?: {
    bar?: string;
  };
  url: '/foo/{fooId}';
};

const url = client.buildUrl<FooData>({
  path: {
    fooId: 1,
  },
  query: {
    bar: 'baz',
  },
  url: '/foo/{fooId}',
});
console.log(url); // prints '/foo/1?bar=baz'
```

## Custom Instance

You can provide a custom `httpClient` instance. This is useful if you need to extend the default instance with extra functionality, or replace it altogether.

```js
import { client } from 'client/client.gen';

client.setConfig({
  httpClient: inject(CustomHttpClient),
});
```

You can use any of the approaches mentioned in [Configuration](#configuration), depending on how granular you want your custom instance to be.

## Plugins

You might be also interested in the [Angular](/openapi-ts/plugins/angular/v19) plugin.

## API

You can view the complete list of options in the [UserConfig](https://github.com/hey-api/openapi-ts/blob/main/packages/openapi-ts/src/plugins/@hey-api/client-angular/types.d.ts) interface.

## Examples

You can view live examples on [StackBlitz](https://stackblitz.com/orgs/github/hey-api/collections/openapi-ts-examples).

## Sponsors

Hey API is sponsor-funded. If you rely on Hey API in production, consider becoming a [sponsor](https://github.com/sponsors/hey-api) to accelerate the roadmap.

---

---
url: /openapi-ts/plugins/angular/v19.md
description: >-
  Generate Angular v19 HTTP requests and resources from OpenAPI with the Angular
  plugin for openapi-ts. Fully compatible with validators, transformers, and all
  core features.
---

::: warning
Angular client is currently in beta. The interface might change before it becomes stable. We encourage you to leave feedback on [GitHub](https://github.com/hey-api/openapi-ts/issues).
:::

### About

[Angular](https://angular.dev/) is a web framework that empowers developers to build fast, reliable applications.

The Angular plugin for Hey API generates HTTP requests and resources from your OpenAPI spec, fully compatible with validators, transformers, and all core features.

### Collaborators

## Features

* Angular v19 support
* seamless integration with `@hey-api/openapi-ts` ecosystem
* generate HTTP requests
* generate HTTP resources
* minimal learning curve thanks to extending the underlying technology

## Installation

In your [configuration](/openapi-ts/get-started), add `@angular/common` to your plugins and you'll be ready to generate Angular artifacts. :tada:

```js
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    // ...other plugins
    '@angular/common', // [!code ++]
  ],
};
```

## Output

The Angular plugin will generate the following artifacts, depending on the input specification.

## Requests

A single function is generated for each endpoint. It returns an [`HttpRequest`](https://v19.angular.dev/api/common/http/HttpRequest) result.

::: code-group

```ts [example]
export const addPetRequest = (options) =>
  client.requestOptions({
    method: 'POST',
    responseStyle: 'data',
    url: '/pet',
    ...options,
  });
```

```js [config]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    // ...other plugins
    {
      name: '@angular/common',
      httpRequests: true, // [!code ++]
    },
  ],
};
```

:::

## Resources

A single function is generated for each endpoint. It returns a result from [`httpResource`](https://v19.angular.dev/api/common/http/httpResource) call.

::: code-group

```ts [example]
export const addPetResource = (options) =>
  httpResource(() => addPetRequest(options()));
```

```js [config]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    // ...other plugins
    {
      name: '@angular/common',
      httpResources: true, // [!code ++]
    },
  ],
};
```

:::

## API

You can view the complete list of options in the [UserConfig](https://github.com/hey-api/openapi-ts/blob/main/packages/openapi-ts/src/plugins/@angular/common/types.d.ts) interface.

---

---
url: /openapi-ts/clients/angular.md
description: >-
  Generate a type-safe Angular v20 client from OpenAPI with the Angular client
  for openapi-ts. Fully compatible with validators, transformers, and all core
  features.
---

::: warning
Angular client is currently in beta. The interface might change before it becomes stable. We encourage you to leave feedback on [GitHub](https://github.com/hey-api/openapi-ts/issues).
:::

### About

[Angular](https://angular.dev/) is a web framework that empowers developers to build fast, reliable applications.

The Angular client for Hey API generates a type-safe client from your OpenAPI spec, fully compatible with validators, transformers, and all core features.

### Collaborators

## Features

* Angular v20 support
* seamless integration with `@hey-api/openapi-ts` ecosystem
* type-safe response data and errors
* support for [`@Injectable()`](https://angular.dev/api/core/Injectable) decorators
* response data validation and transformation
* access to the original request and response
* granular request and response customization options
* minimal learning curve thanks to extending the underlying technology
* support bundling inside the generated output

## Installation

In your [configuration](/openapi-ts/get-started), add `@hey-api/client-angular` to your plugins and you'll be ready to generate client artifacts. :tada:

::: code-group

```js [config]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: ['@hey-api/client-angular'], // [!code ++]
};
```

```sh [cli]
npx @hey-api/openapi-ts \
  -i hey-api/backend \
  -o src/client \
  -c @hey-api/client-angular # [!code ++]
```

:::

### Providers

You can use the Angular client in your application by adding `provideHeyApiClient` to your providers.

```ts
import { provideHeyApiClient, client } from './client/client.gen';

export const appConfig: ApplicationConfig = {
  providers: [
    provideHttpClient(withFetch()),
    provideHeyApiClient(client), // [!code ++]
  ],
};
```

## Configuration

The Angular client is built as a thin wrapper on top of Angular, extending its functionality to work with Hey API. If you're already familiar with Angular, configuring your client will feel like working directly with Angular.

When we installed the client above, it created a [`client.gen.ts`](/openapi-ts/output#client) file. You will most likely want to configure the exported `client` instance. There are two ways to do that.

### `setConfig()`

This is the simpler approach. You can call the `setConfig()` method at the beginning of your application or anytime you need to update the client configuration. You can pass any `HttpRequest` configuration option to `setConfig()`, and even your own [`httpClient`](#custom-instance) implementation.

```js
import { client } from 'client/client.gen';

client.setConfig({
  baseUrl: 'https://example.com',
});
```

The disadvantage of this approach is that your code may call the `client` instance before it's configured for the first time. Depending on your use case, you might need to use the second approach.

### Runtime API

Since `client.gen.ts` is a generated file, we can't directly modify it. Instead, we can tell our configuration to use a custom file implementing the Runtime API. We do that by specifying the `runtimeConfigPath` option.

```js
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    {
      name: '@hey-api/client-angular',
      runtimeConfigPath: './src/hey-api.ts', // [!code ++]
    },
  ],
};
```

In our custom file, we need to export a `createClientConfig()` method. This function is a simple wrapper allowing us to override configuration values.

::: code-group

```ts [hey-api.ts]
import type { CreateClientConfig } from './client/client.gen';

export const createClientConfig: CreateClientConfig = (config) => ({
  ...config,
  baseUrl: 'https://example.com',
});
```

:::

With this approach, `client.gen.ts` will call `createClientConfig()` before initializing the `client` instance. If needed, you can still use `setConfig()` to update the client configuration later.

### `createClient()`

You can also create your own client instance. You can use it to manually send requests or point it to a different domain.

```js
import { createClient } from './client/client';

const myClient = createClient({
  baseUrl: 'https://example.com',
});
```

You can also pass this instance to any SDK function through the `client` option. This will override the default instance from `client.gen.ts`.

```js
const response = await getFoo({
  client: myClient,
});
```

### SDKs

Alternatively, you can pass the client configuration options to each SDK function. This is useful if you don't want to create a client instance for one-off use cases.

```js
const response = await getFoo({
  baseUrl: 'https://example.com', // <-- override default configuration
});
```

## `@Injectable`

If you prefer to use the [`@Injectable()`](https://angular.dev/api/core/Injectable) decorators, set the `asClass` option in your SDK plugin to `true`.

::: code-group

```ts [example]
@Injectable({ providedIn: 'root' })
export class FooService {
  // class methods
}
```

```js [config]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    '@hey-api/client-angular',
    {
      name: '@hey-api/sdk',
      asClass: true, // [!code ++]
    },
  ],
};
```

:::

## Interceptors

::: warning
This section is under construction. We appreciate your patience.
:::

## Auth

::: warning
This section is under construction. We appreciate your patience.
:::

## Build URL

If you need to access the compiled URL, you can use the `buildUrl()` method. It's loosely typed by default to accept almost any value; in practice, you will want to pass a type hint.

```ts
type FooData = {
  path: {
    fooId: number;
  };
  query?: {
    bar?: string;
  };
  url: '/foo/{fooId}';
};

const url = client.buildUrl<FooData>({
  path: {
    fooId: 1,
  },
  query: {
    bar: 'baz',
  },
  url: '/foo/{fooId}',
});
console.log(url); // prints '/foo/1?bar=baz'
```

## Custom Instance

You can provide a custom `httpClient` instance. This is useful if you need to extend the default instance with extra functionality, or replace it altogether.

```js
import { client } from 'client/client.gen';

client.setConfig({
  httpClient: inject(CustomHttpClient),
});
```

You can use any of the approaches mentioned in [Configuration](#configuration), depending on how granular you want your custom instance to be.

## Plugins

You might be also interested in the [Angular](/openapi-ts/plugins/angular) plugin.

## API

You can view the complete list of options in the [UserConfig](https://github.com/hey-api/openapi-ts/blob/main/packages/openapi-ts/src/plugins/@hey-api/client-angular/types.d.ts) interface.

## Examples

You can view live examples on [StackBlitz](https://stackblitz.com/orgs/github/hey-api/collections/openapi-ts-examples).

## Sponsors

Hey API is sponsor-funded. If you rely on Hey API in production, consider becoming a [sponsor](https://github.com/sponsors/hey-api) to accelerate the roadmap.

---

---
url: /openapi-ts/plugins/angular.md
description: >-
  Generate Angular v20 HTTP requests and resources from OpenAPI with the Angular
  plugin for openapi-ts. Fully compatible with validators, transformers, and all
  core features.
---

::: warning
Angular client is currently in beta. The interface might change before it becomes stable. We encourage you to leave feedback on [GitHub](https://github.com/hey-api/openapi-ts/issues).
:::

### About

[Angular](https://angular.dev/) is a web framework that empowers developers to build fast, reliable applications.

The Angular plugin for Hey API generates HTTP requests and resources from your OpenAPI spec, fully compatible with validators, transformers, and all core features.

### Collaborators

## Features

* Angular v20 support
* seamless integration with `@hey-api/openapi-ts` ecosystem
* generate HTTP requests
* generate HTTP resources
* minimal learning curve thanks to extending the underlying technology

## Installation

In your [configuration](/openapi-ts/get-started), add `@angular/common` to your plugins and you'll be ready to generate Angular artifacts. :tada:

```js
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    // ...other plugins
    '@angular/common', // [!code ++]
  ],
};
```

## Output

The Angular plugin will generate the following artifacts, depending on the input specification.

## Requests

A single function is generated for each endpoint. It returns an [`HttpRequest`](https://angular.dev/api/common/http/HttpRequest) result.

::: code-group

```ts [example]
export const addPetRequest = (options) =>
  client.requestOptions({
    method: 'POST',
    responseStyle: 'data',
    url: '/pet',
    ...options,
  });
```

```js [config]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    // ...other plugins
    {
      name: '@angular/common',
      httpRequests: true, // [!code ++]
    },
  ],
};
```

:::

## Resources

A single function is generated for each endpoint. It returns a result from [`httpResource`](https://angular.dev/api/common/http/httpResource) call.

::: code-group

```ts [example]
export const addPetResource = (options) =>
  httpResource(() => addPetRequest(options()));
```

```js [config]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    // ...other plugins
    {
      name: '@angular/common',
      httpResources: true, // [!code ++]
    },
  ],
};
```

:::

## API

You can view the complete list of options in the [UserConfig](https://github.com/hey-api/openapi-ts/blob/main/packages/openapi-ts/src/plugins/@angular/common/types.d.ts) interface.

## Examples

You can view live examples on [StackBlitz](https://stackblitz.com/orgs/github/hey-api/collections/openapi-ts-examples).

## Sponsors

Hey API is sponsor-funded. If you rely on Hey API in production, consider becoming a [sponsor](https://github.com/sponsors/hey-api) to accelerate the roadmap.

---

---
url: /openapi-ts/plugins/arktype.md
description: Arktype plugin for Hey API. Compatible with all our features.
---

# Arktype soon

### About

[Arktype](https://arktype.io) is a TypeScript's 1:1 validator, optimized from editor to runtime.

## Sponsors

Hey API is sponsor-funded. If you rely on Hey API in production, consider becoming a [sponsor](https://github.com/sponsors/hey-api) to accelerate the roadmap.

---

---
url: /openapi-ts/clients/axios.md
description: >-
  Generate a type-safe Axios v1 client from OpenAPI with the Axios client for
  openapi-ts. Fully compatible with validators, transformers, and all core
  features.
---

### About

[Axios](https://axios-http.com) is a simple promise based HTTP client for the browser and Node.js. Axios provides a simple to use library in a small package with a very extensible interface.

The Axios client for Hey API generates a type-safe client from your OpenAPI spec, fully compatible with validators, transformers, and all core features.

### Demo

\<button class="buttonLink" @click="(event) => embedProject('hey-api-client-axios-example')(event)">
Launch demo


## Features

* Axios v1 support
* seamless integration with `@hey-api/openapi-ts` ecosystem
* type-safe response data and errors
* response data validation and transformation
* access to the original request and response
* granular request and response customization options
* minimal learning curve thanks to extending the underlying technology
* support bundling inside the generated output

## Installation

In your [configuration](/openapi-ts/get-started), add `@hey-api/client-axios` to your plugins and you'll be ready to generate client artifacts. :tada:

::: code-group

```js [config]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: ['@hey-api/client-axios'], // [!code ++]
};
```

```sh [cli]
npx @hey-api/openapi-ts \
  -i hey-api/backend \
  -o src/client \
  -c @hey-api/client-axios # [!code ++]
```

:::

## Configuration

The Axios client is built as a thin wrapper on top of Axios, extending its functionality to work with Hey API. If you're already familiar with Axios, configuring your client will feel like working directly with Axios.

When we installed the client above, it created a [`client.gen.ts`](/openapi-ts/output#client) file. You will most likely want to configure the exported `client` instance. There are two ways to do that.

### `setConfig()`

This is the simpler approach. You can call the `setConfig()` method at the beginning of your application or anytime you need to update the client configuration. You can pass any Axios configuration option to `setConfig()` (except for `auth`), and even your own [Axios](#custom-instance) implementation.

```js
import { client } from 'client/client.gen';

client.setConfig({
  baseURL: 'https://example.com',
});
```

The disadvantage of this approach is that your code may call the `client` instance before it's configured for the first time. Depending on your use case, you might need to use the second approach.

### Runtime API

Since `client.gen.ts` is a generated file, we can't directly modify it. Instead, we can tell our configuration to use a custom file implementing the Runtime API. We do that by specifying the `runtimeConfigPath` option.

```js
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    {
      name: '@hey-api/client-axios',
      runtimeConfigPath: './src/hey-api.ts', // [!code ++]
    },
  ],
};
```

In our custom file, we need to export a `createClientConfig()` method. This function is a simple wrapper allowing us to override configuration values.

::: code-group

```ts [hey-api.ts]
import type { CreateClientConfig } from './client/client.gen';

export const createClientConfig: CreateClientConfig = (config) => ({
  ...config,
  baseURL: 'https://example.com',
});
```

:::

With this approach, `client.gen.ts` will call `createClientConfig()` before initializing the `client` instance. If needed, you can still use `setConfig()` to update the client configuration later.

### `createClient()`

You can also create your own client instance. You can use it to manually send requests or point it to a different domain.

```js
import { createClient } from './client/client';

const myClient = createClient({
  baseURL: 'https://example.com',
});
```

You can also pass this instance to any SDK function through the `client` option. This will override the default instance from `client.gen.ts`.

```js
const response = await getFoo({
  client: myClient,
});
```

### SDKs

Alternatively, you can pass the client configuration options to each SDK function. This is useful if you don't want to create a client instance for one-off use cases.

```js
const response = await getFoo({
  baseURL: 'https://example.com', // <-- override default configuration
});
```

## Interceptors

Interceptors (middleware) can be used to modify requests before they're sent or responses before they're returned to your application. Axios provides interceptors, please refer to their documentation on [interceptors](https://axios-http.com/docs/interceptors).

We expose the Axios instance through the `instance` field.

```js
import { client } from 'client/client.gen';

client.instance.interceptors.request.use((config) => {
  // do something
  return config;
});
```

## Auth

The SDKs include auth mechanisms for every endpoint. You will want to configure the `auth` field to pass the right token for each request. The `auth` field can be a string or a function returning a string representing the token. The returned value will be attached only to requests that require auth.

```js
import { client } from 'client/client.gen';

client.setConfig({
  auth: () => '<my_token>', // [!code ++]
  baseURL: 'https://example.com',
});
```

If you're not using SDKs or generating auth, using interceptors is a common approach to configuring auth for each request.

```js
import { client } from 'client/client.gen';

client.instance.interceptors.request.use((config) => {
  config.headers.set('Authorization', 'Bearer <my_token>'); // [!code ++]
  return config;
});
```

## Build URL

If you need to access the compiled URL, you can use the `buildUrl()` method. It's loosely typed by default to accept almost any value; in practice, you will want to pass a type hint.

```ts
type FooData = {
  path: {
    fooId: number;
  };
  query?: {
    bar?: string;
  };
  url: '/foo/{fooId}';
};

const url = client.buildUrl<FooData>({
  path: {
    fooId: 1,
  },
  query: {
    bar: 'baz',
  },
  url: '/foo/{fooId}',
});
console.log(url); // prints '/foo/1?bar=baz'
```

## Custom Instance

You can provide a custom `axios` instance. This is useful if you need to extend the default instance with extra functionality, or replace it altogether.

```js
import axios from 'axios';
import { client } from 'client/client.gen';

// Customize the default axios instance
axios.defaults.baseURL = 'https://example.com';

client.setConfig({
  axios: axios,
});
```

or you can pass an `AxiosInstance` created with `axios.create()`:

```js
import axios from 'axios';
import { client } from 'client/client.gen';

const customAxiosInstance = axios.create({
  baseURL: 'https://example.com',
});

client.setConfig({
  axios: customAxiosInstance,
});
```

You can use any of the approaches mentioned in [Configuration](#configuration), depending on how granular you want your custom instance to be.

## API

You can view the complete list of options in the [UserConfig](https://github.com/hey-api/openapi-ts/blob/main/packages/openapi-ts/src/plugins/@hey-api/client-axios/types.d.ts) interface.

## Examples

You can view live examples on [StackBlitz](https://stackblitz.com/orgs/github/hey-api/collections/openapi-ts-examples).

## Sponsors

Hey API is sponsor-funded. If you rely on Hey API in production, consider becoming a [sponsor](https://github.com/sponsors/hey-api) to accelerate the roadmap.

---

---
url: /openapi-ts/community/contributing/building.md
description: Learn how to contribute to Hey API.
---

# Building

::: warning
This page is under construction. We appreciate your patience.
:::

## Prerequisites

You should have a working knowledge of [git](https://git-scm.com), [node](https://nodejs.org/en), and [pnpm](https://pnpm.io).

## Guidelines

Your [pull request](https://help.github.com/articles/using-pull-requests) must:

* address a single issue or add a single item of functionality
* contain a clean history of small, incremental, logically separate commits, with no merge commits
* use clear commit messages
* be possible to merge automatically

## Start `@hey-api/openapi-ts`

Run `pnpm --filter @hey-api/openapi-ts dev`.

---

---
url: /openapi-ts/plugins/chance.md
description: Chance plugin for Hey API. Compatible with all our features.
---

# Chance soon

### About

[Chance](https://chancejs.com/) is a minimalist generator of random strings, numbers, etc. to help reduce some monotony particularly while writing automated tests or anywhere else you need anything random.

## Sponsors

Hey API is sponsor-funded. If you rely on Hey API in production, consider becoming a [sponsor](https://github.com/sponsors/hey-api) to accelerate the roadmap.

---

---
url: /openapi-ts/clients.md
description: HTTP clients for Hey API. Compatible with all our features.
---

# HTTP Clients

We all send HTTP requests in a slightly different way. Hey API doesn't force you to use any specific technology. What we do, however, is support your choice with great clients. All seamlessly integrated with our other features.

## Features

* seamless integration with `@hey-api/openapi-ts` ecosystem
* type-safe response data and errors
* response data validation and transformation
* access to the original request and response
* granular request and response customization options
* minimal learning curve thanks to extending the underlying technology
* support bundling inside the generated output

## Options

Hey API natively supports the following clients.

* [Fetch API](/openapi-ts/clients/fetch)
* [Angular](/openapi-ts/clients/angular)
* [Axios](/openapi-ts/clients/axios)
* [Ky](/openapi-ts/clients/ky)
* [Next.js](/openapi-ts/clients/next-js)
* [Nuxt](/openapi-ts/clients/nuxt)
* [OFetch](/openapi-ts/clients/ofetch)
* [Effect](/openapi-ts/clients/effect) Soon
* [Got](/openapi-ts/clients/got) Soon

Don't see your client? [Build your own](/openapi-ts/clients/custom) or let us know your interest by [opening an issue](https://github.com/hey-api/openapi-ts/issues).

## Examples

You can view live examples on [StackBlitz](https://stackblitz.com/orgs/github/hey-api/collections/openapi-ts-examples).

## Sponsors

Hey API is sponsor-funded. If you rely on Hey API in production, consider becoming a [sponsor](https://github.com/sponsors/hey-api) to accelerate the roadmap.

---

---
url: /openapi-ts/configuration.md
description: Configure @hey-api/openapi-ts.
---

# Configuration

`@hey-api/openapi-ts` supports loading configuration from any file inside your project root folder supported by [jiti loader](https://github.com/unjs/c12?tab=readme-ov-file#-features). Below are the most common file formats.

::: code-group

```js [openapi-ts.config.ts]
import { defineConfig } from '@hey-api/openapi-ts';

export default defineConfig({
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
});
```

```js [openapi-ts.config.cjs]
/** @type {import('@hey-api/openapi-ts').UserConfig} */
module.exports = {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
};
```

```js [openapi-ts.config.mjs]
/** @type {import('@hey-api/openapi-ts').UserConfig} */
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
};
```

:::

Alternatively, you can use `openapi-ts.config.js` and configure the export statement depending on your project setup.

## Input

You must provide an input so we can load your OpenAPI specification.

The input can be a string path, URL, [API registry](/openapi-ts/configuration/input#api-registry) shorthand, an object containing any of these, or an object representing an OpenAPI specification. Hey API supports all valid OpenAPI versions and file formats.

You can learn more on the [Input](/openapi-ts/configuration/input) page.

::: code-group

```js [path]
export default {
  input: './path/to/openapi.json', // [!code ++]
};
```

```js [url]
export default {
  input: 'https://get.heyapi.dev/hey-api/backend', // sign up at app.heyapi.dev // [!code ++]
};
```

```js [registry]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev // [!code ++]
};
```

```js [object]
export default {
  input: { // [!code ++]
    path: 'hey-api/backend', // sign up at app.heyapi.dev // [!code ++]
    // ...other options // [!code ++]
  }, // [!code ++]
};
```

```js [spec]
export default {
  input: { // [!code ++]
    openapi: '3.1.1', // [!code ++]
    // ...rest of your spec // [!code ++]
  }, // [!code ++]
};
```

:::

::: info
If you use an HTTPS URL with a self-signed certificate in development, you will need to set [`NODE_TLS_REJECT_UNAUTHORIZED=0`](https://github.com/hey-api/openapi-ts/issues/276#issuecomment-2043143501) in your environment.
:::

## Output

You must set the output so we know where to generate your files. It can be a path to the destination folder or an object containing the destination folder path and optional settings.

You can learn more on the [Output](/openapi-ts/configuration/output) page.

::: code-group

```js [path]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client', // [!code ++]
};
```

```js [object]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: { // [!code ++]
    path: 'src/client', // [!code ++]
    // ...other options // [!code ++]
  }, // [!code ++]
};
```

:::

::: tip
You should treat the output folder as a dependency. Do not directly modify its contents as your changes might be erased when you run `@hey-api/openapi-ts` again.
:::

## Parser

We parse your input before making it available to plugins. Configuring the parser is optional, but it provides an ideal opportunity to modify or validate your input as needed.

You can learn more on the [Parser](/openapi-ts/configuration/parser) page.

## Plugins

Plugins are responsible for generating artifacts from your input. By default, Hey API will generate TypeScript interfaces and SDK from your OpenAPI specification. You can add, remove, or customize any of the plugins. In fact, we highly encourage you to do so!

You can learn more on the [Output](/openapi-ts/output) page.

## Advanced

More complex configuration scenarios can be handled by providing an array of inputs, outputs, or configurations.

### Multiple jobs

Throughout this documentation, we generally reference single job configurations. However, you can easily run multiple jobs by providing an array of configuration objects.

::: code-group

```js [config]
export default [
  {
    input: 'foo.yaml',
    output: 'src/foo',
  },
  {
    input: 'bar.yaml',
    output: 'src/bar',
  },
];
```

```txt [example]
src/
├── foo/
│ ├── client/
│ ├── core/
│ ├── client.gen.ts
│ ├── index.ts
│ ├── sdk.gen.ts
│ └── types.gen.ts
└── bar/
  ├── client/
  ├── core/
  ├── client.gen.ts
  ├── index.ts
  ├── sdk.gen.ts
  └── types.gen.ts
```

:::

### Job matrix

Reusing configuration across multiple jobs is possible by defining a job matrix. You can create a job matrix by providing `input` and `output` arrays of matching length.

::: code-group

```js [config]
export default {
  input: ['foo.yaml', 'bar.yaml'],
  output: ['src/foo', 'src/bar'],
};
```

```txt [example]
src/
├── foo/
│ ├── client/
│ ├── core/
│ ├── client.gen.ts
│ ├── index.ts
│ ├── sdk.gen.ts
│ └── types.gen.ts
└── bar/
  ├── client/
  ├── core/
  ├── client.gen.ts
  ├── index.ts
  ├── sdk.gen.ts
  └── types.gen.ts
```

:::

### Merging inputs

You can merge inputs by defining multiple inputs and a single output.

::: code-group

```js [config]
export default {
  input: ['foo.yaml', 'bar.yaml'],
  output: 'src/client',
};
```

```txt [example]
src/
└── client/
  ├── client/
  ├── core/
  ├── client.gen.ts
  ├── index.ts
  ├── sdk.gen.ts
  └── types.gen.ts
```

:::

## API

You can view the complete list of options in the [UserConfig](https://github.com/hey-api/openapi-ts/blob/main/packages/openapi-ts/src/types/config.d.ts) interface.

## Examples

You can view live examples on [StackBlitz](https://stackblitz.com/orgs/github/hey-api/collections/openapi-ts-examples).

## Sponsors

Hey API is sponsor-funded. If you rely on Hey API in production, consider becoming a [sponsor](https://github.com/sponsors/hey-api) to accelerate the roadmap.

---

---
url: /openapi-ts/community/contributing.md
description: Learn how to contribute to Hey API.
---

# Contributor Manual

## Foreword

Hey API is building an OpenAPI to TypeScript code generator ecosystem. It's trusted by thousands of companies – from YC startups to Fortune 500 enterprises – and powers products used by millions worldwide.

We welcome contributors of all backgrounds and experience levels. Whether you're fixing a typo or building a new feature, your input matters. If you need guidance, help with technical writing, or want to bring a feature idea to life, we're here to support you.

::: tip

New to open source? Take a look at the [Open Source](https://opensource.guide/) or [First Contributions](https://github.com/firstcontributions/first-contributions) guides for helpful information on contributing to open source projects.

:::

## First Steps

There are many ways to contribute to Hey API. Most of them don't involve writing any code!

* **Read the documentation**. Start with the [Get Started](/openapi-ts/get-started) guide. If you find anything broken or confusing, you can suggest improvements by clicking "Edit" at the bottom of any page.

* **Browse open issues**. Help others by providing workarounds, asking for clarification, triaging, or suggesting labels on [open issues](https://github.com/hey-api/openapi-ts/issues). If you see something you would like to work on, consider opening a pull request.

* **Participate in discussions**. Ask or [answer questions](https://github.com/orgs/hey-api/discussions), provide feedback, or suggest new ideas. Every idea is welcome, no matter how big or small.

* **Engage on social media**. Help others discover Hey API by engaging with our posts on [LinkedIn](https://linkedin.com/company/heyapi), [Bluesky](https://bsky.app/profile/heyapi.dev), or [X](https://x.com/mrlubos). Share your experiences with Hey API on Reddit, Slack, or in your own communities and group chats.

* **Create a new issue**. If you can't find a solution, [open an issue](https://github.com/hey-api/openapi-ts/issues). The issue template will guide you through the process.

* **Open a pull request**. If you find an issue you would like to fix, open a pull request. If you need help, tag [`@mrlubos`](https://github.com/mrlubos) on GitHub, provide enough relevant information, and we will do our best to assist you.

These are some of the best ways not only to contribute to Hey API, but also to learn, connect with others, and share ideas.

## Pull Requests

Ready to write some code? We have dedicated guides to help you [build](/openapi-ts/community/contributing/building), [develop](/openapi-ts/community/contributing/developing), and [test](/openapi-ts/community/contributing/testing) your feature before it's released.

We are excited to see what you'll contribute!

---

---
url: /openapi-ts/core.md
description: Learn about the core plugins provided by Hey API.
---

# Core

Apart from being responsible for the default output, core plugins are the foundation for other plugins. Instead of creating their own primitives, other plugins can reuse the artifacts from core plugins. This results in a smaller output size and a better user experience.

## Options

Hey API provides the following core plugins.

* [TypeScript](/openapi-ts/plugins/typescript)
* [SDK](/openapi-ts/plugins/sdk)
* [Transformers](/openapi-ts/plugins/transformers)
* [Schemas](/openapi-ts/plugins/schemas)

Need another core plugin? Let us know your interest by [opening an issue](https://github.com/hey-api/openapi-ts/issues).

## Examples

You can view live examples on [StackBlitz](https://stackblitz.com/orgs/github/hey-api/collections/openapi-ts-examples).

## Sponsors

Hey API is sponsor-funded. If you rely on Hey API in production, consider becoming a [sponsor](https://github.com/sponsors/hey-api) to accelerate the roadmap.

---

---
url: /openapi-ts/clients/custom.md
description: Learn how to create your own Hey API client.
---

# Custom Client

::: warning
Client API is in development. The interface might change before it becomes stable. We encourage you to leave feedback on [GitHub](https://github.com/hey-api/openapi-ts/issues/1213).
:::

You may need to write your own client if the available clients do not suit your needs or you're working on a proprietary use case. This can be easily achieved using the Client API. But don't take our word for it – all Hey API clients are written this way!

::: warning
Custom clients documentation will be finalized after further testing. Simplified [instructions](https://github.com/hey-api/openapi-ts/issues/1213#issuecomment-2765206344) can be found in the GitHub thread.
:::

## Examples

You can view live examples on [StackBlitz](https://stackblitz.com/orgs/github/hey-api/collections/openapi-ts-examples).

## Sponsors

Hey API is sponsor-funded. If you rely on Hey API in production, consider becoming a [sponsor](https://github.com/sponsors/hey-api) to accelerate the roadmap.

---

---
url: /openapi-ts/plugins/custom.md
description: Learn how to create your own Hey API plugin.
---

# Custom Plugin

::: warning
Plugin API is in development. The interface might change before it becomes stable. We encourage you to leave feedback on [GitHub](https://github.com/hey-api/openapi-ts/issues).
:::

::: warning
This page is out of date as of [v0.83.0](/openapi-ts/migrating#v0-83-0). If you have an existing custom plugin, we recommend waiting for a more stable Plugin API to avoid multiple plugin rewrites.
:::

You may need to write your own plugin if the available plugins do not suit your needs or you're working on a proprietary use case. This can be easily achieved using the Plugin API. But don't take our word for it – all Hey API plugins are written this way!

## File Structure

We recommend following the design pattern of the native plugins. You can browse the code on [GitHub](https://github.com/hey-api/openapi-ts/tree/main/packages/openapi-ts/src/plugins) as you follow this tutorial. First, create a `my-plugin` folder for your plugin files. Inside, create a barrel file `index.ts` exporting the plugin.

::: code-group

```ts [index.ts]
export { defaultConfig, defineConfig } from './config';
export type { MyPlugin } from './types';
```

:::

## TypeScript

`index.ts` references two files, so we need to create them. `types.d.ts` contains the TypeScript interface for your plugin options. It must have the reserved `name` and `output` fields, everything else will become user-configurable options.

::: code-group

```ts [types.d.ts]
import type { DefinePlugin } from '@hey-api/openapi-ts';

export type UserConfig = {
  /**
   * Plugin name. Must be unique.
   */
  name: 'my-plugin';
  /**
   * Name of the generated file.
   *
   * @default 'my-plugin'
   */
  output?: string;
  /**
   * User-configurable option for your plugin.
   *
   * @default false
   */
  myOption?: boolean;
};

export type MyPlugin = DefinePlugin<UserConfig>;
```

:::

## Configuration

`config.ts` contains the runtime configuration for your plugin. It must implement the `MyPlugin` interface we created above and define the `handler()` function from the `MyPlugin['Config']` interface.

::: code-group

```ts [config.ts]
import { definePluginConfig } from '@hey-api/openapi-ts';

import { handler } from './plugin';
import type { MyPlugin } from './types';

export const defaultConfig: MyPlugin['Config'] = {
  config: {
    myOption: false, // implements default value from types
  },
  dependencies: ['@hey-api/typescript'],
  handler,
  name: 'my-plugin',
};

/**
 * Type helper for `my-plugin` plugin, returns {@link Plugin.Config} object
 */
export const defineConfig = definePluginConfig(defaultConfig);
```

:::

In the file above, we define a `my-plugin` plugin which will generate a `my-plugin.gen.ts` file. We also demonstrate declaring `@hey-api/typescript` as a dependency for our plugin, so we can safely import artifacts from `types.gen.ts`.

By default, your plugin output won't be re-exported from the `index.ts` file. To enable this feature, add `exportFromIndex: true` to your `config.ts` file.

::: warning
Re-exporting your plugin from index file may result in broken output due to naming conflicts. Ensure your exported identifiers are unique.
:::

## Handler

Notice we defined `handler` in our `config.ts` file. This method is responsible for generating the actual output. We recommend implementing it in `plugin.ts`.

::: code-group

```ts [plugin.ts]
import type { MyPlugin } from './types';

export const handler: MyPlugin['Handler'] = ({ plugin }) => {
  // create an output file. it will not be
  // generated until it contains nodes
  const file = plugin.createFile({
    id: plugin.name,
    path: plugin.output,
  });

  plugin.forEach('operation', 'schema', (event) => {
    if (event.type === 'operation') {
      // do something with the operation model
    } else if (event.type === 'schema') {
      // do something with the schema model
    }
  });

  // we're using the TypeScript Compiler API
  const stringLiteral = ts.factory.createStringLiteral('Hello, world!');
  const variableDeclaration = ts.factory.createVariableDeclaration(
    'foo',
    undefined,
    undefined,
    stringLiteral,
  );
  const node = ts.factory.createVariableStatement(
    [ts.factory.createModifier(ts.SyntaxKind.ExportKeyword)],
    ts.factory.createVariableDeclarationList(
      [variableDeclaration],
      ts.NodeFlags.Const,
    ),
  );

  // add a node to our file
  file.add(node);
};
```

:::

### Legacy Handler

You can also define an optional `handlerLegacy` function in `config.ts`. This method is responsible for generating the output when using the legacy parser. We do not recommend implementing this method unless you must use the legacy parser. You can use one of our [`plugin-legacy.ts`](https://github.com/hey-api/openapi-ts/blob/main/packages/openapi-ts/src/plugins/%40hey-api/typescript/plugin-legacy.ts) files as an inspiration for potential implementation.

## Usage

Once we're satisfied with our plugin, we can register it in the [configuration](/openapi-ts/configuration) file.

```js
import { defineConfig } from 'path/to/my-plugin';

export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    defineConfig({
      myOption: true,
    }),
  ],
};
```

## Output

Putting all of this together will generate the following `my-plugin.gen.ts` file.

::: code-group

```ts [my-plugin.gen.ts]
export const foo = 'Hello, world!';
```

:::

Congratulations! You've successfully created your own plugin! :tada:

## Examples

You can view live examples on [StackBlitz](https://stackblitz.com/orgs/github/hey-api/collections/openapi-ts-examples).

## Sponsors

Hey API is sponsor-funded. If you rely on Hey API in production, consider becoming a [sponsor](https://github.com/sponsors/hey-api) to accelerate the roadmap.

---

---
url: /openapi-ts/community/contributing/developing.md
description: Learn how to contribute to Hey API.
---

# Developing

::: warning
This page is under construction. We appreciate your patience.
:::

## Working with Examples

The `examples` folder contains various integration examples that demonstrate how to use `@hey-api/openapi-ts` with different frameworks and libraries. These examples are kept in sync with the codebase through automated checks.

### Generating Example Code

When you make changes to the core packages that affect code generation, you need to regenerate the client code in all examples:

```bash
pnpm examples:generate
```

This command will:

* Find all examples with an `openapi-ts` script
* Run the OpenAPI code generator for each example
* Update the generated client code in each example

### Checking Example Code

Before committing changes, ensure that all generated example code is up-to-date:

```bash
pnpm examples:check
```

This command will:

* Regenerate all example code
* Check if any files were modified
* Exit with an error if generated code is out of sync

This check is also run automatically in CI to ensure examples stay in sync with the main codebase.

### Example Workflow

1. Make changes to core packages
2. Build the packages: `pnpm build --filter="@hey-api/**"`
3. Regenerate examples: `pnpm examples:generate`
4. Commit all changes including the updated generated code
5. The CI will verify that examples are in sync

::: tip
Think of generated example code as snapshot tests - they should always reflect the current state of the code generator.
:::

---

---
url: /openapi-ts/clients/effect.md
description: Effect client for Hey API. Compatible with all our features.
---

# Effect soon

### About

[Effect](https://effect.website/) is a powerful TypeScript library designed to help developers easily create complex, synchronous, and asynchronous programs.

## Sponsors

Hey API is sponsor-funded. If you rely on Hey API in production, consider becoming a [sponsor](https://github.com/sponsors/hey-api) to accelerate the roadmap.

---

---
url: /openapi-ts/plugins/elysia.md
description: Elysia plugin for Hey API. Compatible with all our features.
---

# Elysia soon

### About

[Elysia](https://elysiajs.com/) is an ergonomic framework for humans. TypeScript with end-to-end type safety, type integrity, and exceptional developer experience. Supercharged by Bun.

## Sponsors

Hey API is sponsor-funded. If you rely on Hey API in production, consider becoming a [sponsor](https://github.com/sponsors/hey-api) to accelerate the roadmap.

---

---
url: /openapi-ts/plugins/express.md
description: Express plugin for Hey API. Compatible with all our features.
---

# Express soon

### About

[Express](https://expressjs.com) is a minimal and flexible Node.js web application framework that provides a robust set of features for web and mobile applications.

## Sponsors

Hey API is sponsor-funded. If you rely on Hey API in production, consider becoming a [sponsor](https://github.com/sponsors/hey-api) to accelerate the roadmap.

---

---
url: /openapi-ts/plugins/faker.md
description: Faker plugin for Hey API. Compatible with all our features.
---

# Faker soon

### About

[Faker](https://fakerjs.dev) is a popular library that generates fake (but reasonable) data that can be used for things such as unit testing, performance testing, building demos, and working without a completed backend.

## Sponsors

Hey API is sponsor-funded. If you rely on Hey API in production, consider becoming a [sponsor](https://github.com/sponsors/hey-api) to accelerate the roadmap.

---

---
url: /openapi-ts/plugins/falso.md
description: Falso plugin for Hey API. Compatible with all our features.
---

# Falso soon

### About

[Falso](https://ngneat.github.io/falso/) creates massive amounts of fake data in the browser and NodeJS. Tree shakeable & fully typed.

## Sponsors

Hey API is sponsor-funded. If you rely on Hey API in production, consider becoming a [sponsor](https://github.com/sponsors/hey-api) to accelerate the roadmap.

---

---
url: /openapi-ts/plugins/fastify.md
description: >-
  Generate Fastify v5 route handlers from OpenAPI with the Fastify plugin for
  openapi-ts. Fully compatible with validators, transformers, and all core
  features.
---

::: warning
Fastify plugin is currently in beta. The interface might change before it becomes stable. We encourage you to leave feedback on [GitHub](https://github.com/hey-api/openapi-ts/issues).
:::

### About

[Fastify](https://fastify.dev) is a fast and low overhead web framework for Node.js.

The Fastify plugin for Hey API generates route handlers from your OpenAPI spec, fully compatible with all core features.

### Collaborators

## Features

* Fastify v5 support
* seamless integration with `@hey-api/openapi-ts` ecosystem
* type-safe route handlers
* minimal learning curve thanks to extending the underlying technology

## Installation

In your [configuration](/openapi-ts/get-started), add `fastify` to your plugins and you'll be ready to generate Fastify artifacts. :tada:

```js
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    // ...other plugins
    'fastify', // [!code ++]
  ],
};
```

## Output

The Fastify plugin will generate the following artifacts, depending on the input specification.

## Route Handlers

Route handlers are generated from all endpoints. The generated interface follows the naming convention of SDK functions.

::: code-group

```ts [example]
const fastify = Fastify();
const serviceHandlers: RouteHandlers = {
  createPets(request, reply) {
    reply.code(201).send();
  },
  listPets(request, reply) {
    reply.code(200).send([]);
  },
  showPetById(request, reply) {
    reply.code(200).send({
      id: Number(request.params.petId),
      name: 'Kitty',
    });
  },
};
fastify.register(glue, { serviceHandlers });
```

```js [config]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    // ...other plugins
    {
      name: 'fastify',
    },
  ],
};
```

:::

## API

You can view the complete list of options in the [UserConfig](https://github.com/hey-api/openapi-ts/blob/main/packages/openapi-ts/src/plugins/fastify/types.d.ts) interface.

## Examples

You can view live examples on [StackBlitz](https://stackblitz.com/orgs/github/hey-api/collections/openapi-ts-examples).

## Sponsors

Hey API is sponsor-funded. If you rely on Hey API in production, consider becoming a [sponsor](https://github.com/sponsors/hey-api) to accelerate the roadmap.

---

---
url: /openapi-ts/clients/fetch.md
description: >-
  Generate a type-safe Fetch API client from OpenAPI with the Fetch API client
  for openapi-ts. Fully compatible with validators, transformers, and all core
  features.
---

# Fetch API

### About

The [Fetch API](https://developer.mozilla.org/docs/Web/API/Fetch_API) provides an interface for fetching resources (including across the network). It is a more powerful and flexible replacement for XMLHttpRequest.

The Fetch API client for Hey API generates a type-safe client from your OpenAPI spec, fully compatible with validators, transformers, and all core features.

### Demo

\<button class="buttonLink" @click="(event) => embedProject('hey-api-client-fetch-example')(event)">
Launch demo


## Features

* seamless integration with `@hey-api/openapi-ts` ecosystem
* type-safe response data and errors
* response data validation and transformation
* access to the original request and response
* granular request and response customization options
* minimal learning curve thanks to extending the underlying technology
* support bundling inside the generated output

## Installation

In your [configuration](/openapi-ts/get-started), add `@hey-api/client-fetch` to your plugins and you'll be ready to generate client artifacts. :tada:

::: code-group

```js [config]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: ['@hey-api/client-fetch'], // [!code ++]
};
```

```sh [cli]
npx @hey-api/openapi-ts \
  -i hey-api/backend \
  -o src/client \
  -c @hey-api/client-fetch # [!code ++]
```

:::

::: tip

This step is optional because Fetch is the default client.

:::

## Configuration

The Fetch client is built as a thin wrapper on top of Fetch API, extending its functionality to work with Hey API. If you're already familiar with Fetch, configuring your client will feel like working directly with Fetch API.

When we installed the client above, it created a [`client.gen.ts`](/openapi-ts/output#client) file. You will most likely want to configure the exported `client` instance. There are two ways to do that.

### `setConfig()`

This is the simpler approach. You can call the `setConfig()` method at the beginning of your application or anytime you need to update the client configuration. You can pass any Fetch API configuration option to `setConfig()`, and even your own [Fetch](#custom-instance) implementation.

```js
import { client } from 'client/client.gen';

client.setConfig({
  baseUrl: 'https://example.com',
});
```

The disadvantage of this approach is that your code may call the `client` instance before it's configured for the first time. Depending on your use case, you might need to use the second approach.

### Runtime API

Since `client.gen.ts` is a generated file, we can't directly modify it. Instead, we can tell our configuration to use a custom file implementing the Runtime API. We do that by specifying the `runtimeConfigPath` option.

```js
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    {
      name: '@hey-api/client-fetch',
      runtimeConfigPath: './src/hey-api.ts', // [!code ++]
    },
  ],
};
```

In our custom file, we need to export a `createClientConfig()` method. This function is a simple wrapper allowing us to override configuration values.

::: code-group

```ts [hey-api.ts]
import type { CreateClientConfig } from './client/client.gen';

export const createClientConfig: CreateClientConfig = (config) => ({
  ...config,
  baseUrl: 'https://example.com',
});
```

:::

With this approach, `client.gen.ts` will call `createClientConfig()` before initializing the `client` instance. If needed, you can still use `setConfig()` to update the client configuration later.

### `createClient()`

You can also create your own client instance. You can use it to manually send requests or point it to a different domain.

```js
import { createClient } from './client/client';

const myClient = createClient({
  baseUrl: 'https://example.com',
});
```

You can also pass this instance to any SDK function through the `client` option. This will override the default instance from `client.gen.ts`.

```js
const response = await getFoo({
  client: myClient,
});
```

### SDKs

Alternatively, you can pass the client configuration options to each SDK function. This is useful if you don't want to create a client instance for one-off use cases.

```js
const response = await getFoo({
  baseUrl: 'https://example.com', // <-- override default configuration
});
```

## Interceptors

Interceptors (middleware) can be used to modify requests before they're sent or responses before they're returned to your application.

They can be added with `use`, removed with `eject`, and updated wth `update`. The `use` and `update` methods will return the ID of the interceptor for use with `eject` and `update`. Fetch API does not have the interceptor functionality, so we implement our own.

### Example: Request interceptor

::: code-group

```js [use]
import { client } from 'client/client.gen';

async function myInterceptor(request) {
  // do something
  return request;
}

interceptorId = client.interceptors.request.use(myInterceptor);
```

```js [eject]
import { client } from 'client/client.gen';

// eject by ID
client.interceptors.request.eject(interceptorId);

// eject by reference
client.interceptors.request.eject(myInterceptor);
```

```js [update]
import { client } from 'client/client.gen';

async function myNewInterceptor(request) {
  // do something
  return request;
}

// update by ID
client.interceptors.request.update(interceptorId, myNewInterceptor);

// update by reference
client.interceptors.request.update(myInterceptor, myNewInterceptor);
```

:::

### Example: Response interceptor

::: code-group

```js [use]
import { client } from 'client/client.gen';

async function myInterceptor(response) {
  // do something
  return response;
}

interceptorId = client.interceptors.response.use(myInterceptor);
```

```js [eject]
import { client } from 'client/client.gen';

// eject by ID
client.interceptors.response.eject(interceptorId);

// eject by reference
client.interceptors.response.eject(myInterceptor);
```

```js [update]
import { client } from 'client/client.gen';

async function myNewInterceptor(response) {
  // do something
  return response;
}

// update by ID
client.interceptors.response.update(interceptorId, myNewInterceptor);

// update by reference
client.interceptors.response.update(myInterceptor, myNewInterceptor);
```

:::

::: tip
To eject, you must provide the ID or reference of the interceptor passed to `use()`, the ID is the value returned by `use()` and `update()`.
:::

## Auth

The SDKs include auth mechanisms for every endpoint. You will want to configure the `auth` field to pass the right token for each request. The `auth` field can be a string or a function returning a string representing the token. The returned value will be attached only to requests that require auth.

```js
import { client } from 'client/client.gen';

client.setConfig({
  auth: () => '<my_token>', // [!code ++]
  baseUrl: 'https://example.com',
});
```

If you're not using SDKs or generating auth, using interceptors is a common approach to configuring auth for each request.

```js
import { client } from 'client/client.gen';

client.interceptors.request.use((request, options) => {
  request.headers.set('Authorization', 'Bearer <my_token>'); // [!code ++]
  return request;
});
```

## Build URL

If you need to access the compiled URL, you can use the `buildUrl()` method. It's loosely typed by default to accept almost any value; in practice, you will want to pass a type hint.

```ts
type FooData = {
  path: {
    fooId: number;
  };
  query?: {
    bar?: string;
  };
  url: '/foo/{fooId}';
};

const url = client.buildUrl<FooData>({
  path: {
    fooId: 1,
  },
  query: {
    bar: 'baz',
  },
  url: '/foo/{fooId}',
});
console.log(url); // prints '/foo/1?bar=baz'
```

## Custom Instance

You can provide a custom `fetch` instance. This is useful if you need to extend the default instance with extra functionality, or replace it altogether.

```js
import { client } from 'client/client.gen';

client.setConfig({
  fetch: () => {
    /* custom `fetch` method */
  },
});
```

You can use any of the approaches mentioned in [Configuration](#configuration), depending on how granular you want your custom instance to be.

## API

You can view the complete list of options in the [UserConfig](https://github.com/hey-api/openapi-ts/blob/main/packages/openapi-ts/src/plugins/@hey-api/client-fetch/types.d.ts) interface.

## Examples

You can view live examples on [StackBlitz](https://stackblitz.com/orgs/github/hey-api/collections/openapi-ts-examples).

## Sponsors

Hey API is sponsor-funded. If you rely on Hey API in production, consider becoming a [sponsor](https://github.com/sponsors/hey-api) to accelerate the roadmap.

---

---
url: /openapi-ts/get-started.md
description: Get started with @hey-api/openapi-ts.
---

# Get Started

[@hey-api/openapi-ts](https://github.com/hey-api/openapi-ts) generates TypeScript code from OpenAPI specifications. Point it at your spec, pick your plugins, and get production-ready code in seconds.

Used by companies like Vercel, OpenCode, and PayPal.

> *“OpenAPI codegen that just works.”*
>
> — Guillermo Rauch, CEO of Vercel

### Demo

\<button class="buttonLink" @click="(event) => embedProject('hey-api-example')(event)">
Launch demo


## Features

* production-ready code that compiles
* runs in any Node.js 20+ environment
* accepts any OpenAPI specification
* core plugins for SDKs, types, and schemas
* HTTP clients for Fetch API, Angular, Axios, Next.js, Nuxt, and more
* 20+ plugins to reduce third-party boilerplate
* highly customizable via plugins
* [sync with Hey API Registry](/openapi-ts/integrations) for spec management

## Quick Start

The fastest way to use `@hey-api/openapi-ts` is via npx

```sh
npx @hey-api/openapi-ts -i hey-api/backend -o src/client
```

Congratulations on creating your first client! 🎉 You can learn more about the generated files on the [Output](/openapi-ts/output) page.

## Installation

You can download `@hey-api/openapi-ts` from npm using your favorite package manager.

::: code-group

```sh [npm]
npm install @hey-api/openapi-ts -D -E
```

```sh [pnpm]
pnpm add @hey-api/openapi-ts -D -E
```

```sh [yarn]
yarn add @hey-api/openapi-ts -D -E
```

```sh [bun]
bun add @hey-api/openapi-ts -D -E
```

:::

### Versioning

This package does NOT follow the [semantic versioning](https://semver.org/) strategy. Please pin an exact version so you can safely upgrade when you're ready.

Due to the nature of the package, we use the following versioning strategy.

* `1.x.x`: significant breaking changes, reserved for v1 release
* `x.1.x`: breaking changes
* `x.x.1`: new features, bug fixes, and non-breaking changes

We publish [migration notes](/openapi-ts/migrating) for every breaking release. You might not be impacted by a breaking release if you don't use the affected plugin(s).

## Usage

### CLI

Most people run `@hey-api/openapi-ts` via CLI. To do that, add a script to your `package.json` file which will make `openapi-ts` executable through script.

```json
"scripts": {
  "openapi-ts": "openapi-ts"
}
```

The above script can be executed by running `npm run openapi-ts` or equivalent command in other package managers. Next, we will create a [configuration](/openapi-ts/configuration) file and move our options from Quick Start to it.

### Node.js

You can also generate output programmatically by calling `createClient()` in a JavaScript/TypeScript file.

::: code-group

```ts [script.ts]
import { createClient } from '@hey-api/openapi-ts';

createClient({
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
});
```

:::

### Configuration

It's a good practice to extract your configuration into a separate file. Learn how to do that and discover available options on the [Configuration](/openapi-ts/configuration) page.

## Examples

You can view live examples on [StackBlitz](https://stackblitz.com/orgs/github/hey-api/collections/openapi-ts-examples).

## Sponsors

Hey API is sponsor-funded. If you rely on Hey API in production, consider becoming a [sponsor](https://github.com/sponsors/hey-api) to accelerate the roadmap.

---

---
url: /openapi-ts/clients/got.md
description: Got client for Hey API. Compatible with all our features.
---

# Got soon

### About

[Got](https://github.com/sindresorhus/got) is a human-friendly and powerful HTTP request library for Node.js.

## Sponsors

Hey API is sponsor-funded. If you rely on Hey API in production, consider becoming a [sponsor](https://github.com/sponsors/hey-api) to accelerate the roadmap.

---

---
url: /openapi-ts/integrations.md
description: Automate your client generation with our OpenAPI specifications storage.
---

# Hey API Platform

::: warning
This feature is in development! :tada: Try it out and provide feedback on [GitHub](https://github.com/orgs/hey-api/discussions/1773).
:::

You can automate your client generation with Hey API Platform thanks to reproducible builds. Create dependency links between your clients and APIs, and watch the magic unfold. It's completely language and codegen agnostic.

## Features

* API version history
* real-time updates
* reproducible builds
* language and codegen agnostic (TypeScript/Python/Go/Java/etc codegens are welcome)

## Upload Specifications

Before you can generate clients, you must publish your OpenAPI specifications to Hey API.

### Prerequisites

1. Create a **free account** with [Hey API](https://app.heyapi.dev).
2. Create a new **organization** and **project** for your API provider. We recommend your naming matches your GitHub structure as it will be referenced by API clients. For example, we are using **hey-api/backend** for the platform.
3. Inside your project, go to *Integrations* > *APIs* and generate an **API key**. Keep this value secret, it will be used to upload files.

### Add GitHub CI workflow

Once you have your API key, you can start uploading OpenAPI specifications on every API build. We'll use our [GitHub Action](https://github.com/marketplace/actions/upload-openapi-spec-by-hey-api), but you can also make the API call manually if you're not using GitHub.

Create a new GitHub workflow or add an upload step to an existing workflow inside your API codebase. The example below will upload your OpenAPI specification to Hey API on every pull request and push to the `main` branch.

```yaml
name: Upload OpenAPI Specification

on:
  push:
    branches:
      - main
  pull_request:

jobs:
  upload-openapi-spec:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Upload OpenAPI spec
        uses: hey-api/upload-openapi-spec@v1.3.0
        with:
          path-to-file: path/to/openapi.json
          tags: optional,custom,tags
        env:
          API_KEY: ${{ secrets.HEY_API_TOKEN }}
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

### Inputs

To successfully upload an OpenAPI specification, you need to provide the following inputs (see `with` in the example above)

#### `path-to-file`

A relative path to your OpenAPI file within the repository. Note that you might need an additional step in your GitHub workflow to generate this file (see [FastAPI example](https://fastapi.tiangolo.com/how-to/extending-openapi/#generate-the-openapi-schema)).

#### `tags` (optional)

A comma-separated string value representing any custom tags you wish to add to your OpenAPI specification.

### Environment Variables

In addition to the required `path-to-file` input, you must provide the following environment variables.

#### `API_KEY`

This is the project API key you obtained from [Hey API](https://app.heyapi.dev).

::: warning
Personal API keys can't be used to upload specifications.
:::

#### `GITHUB_TOKEN`

This variable will be available inside your workflow by default. It's used to
fetch information about your repository, i.e. default branch.

## Generate Clients

You can generate clients from public projects or any private projects you can access. The setup is largely the same, you want to configure the input path used by your codegen.

::: code-group

```sh [Hey API]
npx @hey-api/openapi-ts -i hey-api/backend -o src/client
```

```sh [OpenAPI TypeScript]
npx openapi-typescript \
  https://get.heyapi.dev/hey-api/backend \
  -o schema.ts
```

```sh [Orval]
npx orval \
  --input https://get.heyapi.dev/hey-api/backend \
  --output ./src/client.ts
```

```sh [Other]
other-cli \
  --input https://get.heyapi.dev/hey-api/backend \  # [!code ++]
  --output refer/to/other/tools/docs
```

:::

By default, we preserve the current behavior and return the latest specification. Let's have a closer look at the input path and change that.

## Get API

As you can deduce from the examples above, the default command for fetching OpenAPI specifications looks like this.

```
https://get.heyapi.dev/<organization>/<project>
```

If you created an organization `foo` with project `bar` earlier, your URL would look like this.

```
https://get.heyapi.dev/foo/bar
```

### Auth

Projects are private by default, you will need to be authenticated to download OpenAPI specifications. We recommend using [project API keys](#prerequisites) in CI workflows and [personal API keys](https://app.heyapi.dev/settings/user/apis) for local development.

Once you have your API key, you can authenticate the request using the `Authorization` header or `api_key` query parameter.

```
https://get.heyapi.dev/foo/bar?api_key=<my_api_key>
```

Congratulations on fetching your first OpenAPI specification! 🎉

### Filters

The default behavior returns the last uploaded specification. This might not be what you want. You can use a range of filters to narrow down the possible specifications, or pin your builds to an exact version.

#### `branch`

You can fetch the last build from branch by providing the `branch` query parameter.

```
https://get.heyapi.dev/foo/bar?branch=production
```

#### `commit_sha`

You can fetch an exact specification by providing the `commit_sha` query parameter. This will always return the same file.

```
https://get.heyapi.dev/foo/bar?commit_sha=0eb34c2024841ce95620f3ec02a2fea164ea4e9d
```

#### `tags`

If you're tagging your specifications with [custom tags](#tags-optional), you can use them to filter the results. When you provide multiple tags, only the first match will be returned.

```
https://get.heyapi.dev/foo/bar?tags=optional,custom,tags
```

#### `version`

Every OpenAPI document contains a required version field. You can use this value to fetch the last uploaded specification matching the value.

```
https://get.heyapi.dev/foo/bar?version=1.0.0
```

## Feedback

We'd love your feedback! You can contact us on social media (search Hey API), [email](mailto:lubos@heyapi.dev), or [GitHub](https://github.com/orgs/hey-api/discussions/1773).

## Pricing

The platform is currently in beta with our focus being on delivering a great experience. We plan to announce pricing once we have gathered enough data around usage patterns. However, we can guarantee there will always be a free plan available. Our mission to bring the finest tooling for working with APIs remains unchanged.

## Sponsors

Hey API is sponsor-funded. If you rely on Hey API in production, consider becoming a [sponsor](https://github.com/sponsors/hey-api) to accelerate the roadmap.

---

---
url: /openapi-ts/plugins/hono.md
description: Hono plugin for Hey API. Compatible with all our features.
---

# Hono soon

### About

[Hono](https://hono.dev) is a small, simple, and ultrafast web framework built on Web Standards. It works on any JavaScript runtime: Cloudflare Workers, Fastly Compute, Deno, Bun, Vercel, Netlify, AWS Lambda, Lambda@Edge, and Node.js.

## Sponsors

Hey API is sponsor-funded. If you rely on Hey API in production, consider becoming a [sponsor](https://github.com/sponsors/hey-api) to accelerate the roadmap.

---

---
url: /openapi-ts/configuration/input.md
description: Configure @hey-api/openapi-ts.
---

# Input

You must provide an input so we can load your OpenAPI specification.

## Input

The input can be a string path, URL, [API registry](#api-registry), an object containing any of these, or an object representing an OpenAPI specification. Hey API supports all valid OpenAPI versions and file formats.

::: code-group

```js [path]
export default {
  input: './path/to/openapi.json', // [!code ++]
};
```

```js [url]
export default {
  input: 'https://get.heyapi.dev/hey-api/backend', // sign up at app.heyapi.dev // [!code ++]
};
```

```js [registry]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev // [!code ++]
};
```

```js [object]
export default {
  input: { // [!code ++]
    path: 'hey-api/backend', // sign up at app.heyapi.dev // [!code ++]
    // ...other options // [!code ++]
  }, // [!code ++]
};
```

```js [spec]
export default {
  input: { // [!code ++]
    openapi: '3.1.1', // [!code ++]
    // ...rest of your spec // [!code ++]
  }, // [!code ++]
};
```

:::

You can learn more about complex use cases in the [Advanced](/openapi-ts/configuration#advanced) section.

::: info
If you use an HTTPS URL with a self-signed certificate in development, you will need to set [`NODE_TLS_REJECT_UNAUTHORIZED=0`](https://github.com/hey-api/openapi-ts/issues/276#issuecomment-2043143501) in your environment.
:::

### Request options

You can pass any valid Fetch API [options](https://developer.mozilla.org/docs/Web/API/RequestInit) to the request for fetching your specification. This is useful if your file is behind auth for example.

```js
export default {
  input: {
    path: 'https://secret.com/protected-spec',
    fetch: { // [!code ++]
      headers: { // [!code ++]
        Authorization: 'Bearer xxx', // [!code ++]
      }, // [!code ++]
    }, // [!code ++]
  },
};
```

## API Registry

You can store your specifications in an API registry to serve as a single source of truth. This helps prevent drift, improves discoverability, enables version tracking, and more.

### Hey API

You can learn more about [Hey API Platform](https://app.heyapi.dev) on the [Integrations](/openapi-ts/integrations) page.

```js [uuid]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev // [!code ++]
};
```

The `input` object lets you provide additional options to construct the correct URL.

```js
export default {
  input: {
    path: 'hey-api/backend', // sign up at app.heyapi.dev
    branch: 'main', // [!code ++]
  },
};
```

We also provide shorthands for other registries:

::: details Scalar
Prefix your input with `scalar:` to use the Scalar API Registry.

```js [long]
export default {
  input: 'scalar:@scalar/access-service', // [!code ++]
};
```

:::

::: details ReadMe
Prefix your input with `readme:` to use the ReadMe API Registry.

::: code-group

```js [uuid]
export default {
  input: 'readme:nysezql0wwo236', // [!code ++]
};
```

```js [long]
export default {
  input: 'readme:@developers/v2.0#nysezql0wwo236', // [!code ++]
};
```

:::

## Watch Mode

::: warning
Watch mode currently supports only remote files via URL.
:::

If your schema changes frequently, you may want to automatically regenerate the output during development. To watch your input file for changes, enable `input.watch` mode in your configuration or pass the `--watch` flag to the CLI.

::: code-group

```js [config]
export default {
  input: {
    path: 'hey-api/backend', // sign up at app.heyapi.dev
    watch: true, // [!code ++]
  },
};
```

```sh [cli]
npx @hey-api/openapi-ts \
  -i hey-api/backend \
  -o src/client \
  -w  # [!code ++]
```

:::

## Examples

You can view live examples on [StackBlitz](https://stackblitz.com/orgs/github/hey-api/collections/openapi-ts-examples).

## Sponsors

Hey API is sponsor-funded. If you rely on Hey API in production, consider becoming a [sponsor](https://github.com/sponsors/hey-api) to accelerate the roadmap.

---

---
url: /openapi-ts/plugins/joi.md
description: Joi plugin for Hey API. Compatible with all our features.
---

# Joi soon

### About

[Joi](https://joi.dev) is the most powerful schema description language and data validator for JavaScript.

## Sponsors

Hey API is sponsor-funded. If you rely on Hey API in production, consider becoming a [sponsor](https://github.com/sponsors/hey-api) to accelerate the roadmap.

---

---
url: /openapi-ts/plugins/schemas.md
description: Learn about files generated with @hey-api/openapi-ts.
---

# JSON Schemas

Schemas are located in the `schemas.gen.ts` file. This file contains runtime schemas generated from your OpenAPI specification definitions located in `#/components/schemas`. If you're using OpenAPI 3.1, your schemas are fully JSON Schema compliant and can be used with other tools supporting JSON Schema.

## Configuration

You can modify the contents of `schemas.gen.ts` by configuring the `@hey-api/schemas` plugin. Note that you must specify the default plugins to preserve the default output.

::: code-group

```js [json]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    // ...other plugins
    {
      name: '@hey-api/schemas',
      type: 'json', // [!code ++]
    },
  ],
};
```

```js [form]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    // ...other plugins
    {
      name: '@hey-api/schemas',
      type: 'form', // [!code ++]
    },
  ],
};
```

```js [disabled]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    // ...other plugins
    '@hey-api/schemas', // [!code --]
  ],
};
```

:::

## Output

Below is an example output generated in the `type: 'form'` style. Disabling schemas will not generate the `schemas.gen.ts` file.

```ts
export const PetSchema = {
  required: ['name'],
  properties: {
    id: {
      type: 'integer',
      format: 'int64',
      example: 10,
    },
    name: {
      type: 'string',
      example: 'doggie',
    },
  },
  type: 'object',
} as const;
```

## Usage

A great use case for schemas is client-side form input validation.

```ts
import { $Schema } from './client/schemas.gen';

const maxInputLength = $Schema.properties.text.maxLength;

if (userInput.length > maxInputLength) {
  throw new Error(`Text length can't exceed ${maxInputLength} characters!`);
}
```

## API

You can view the complete list of options in the [UserConfig](https://github.com/hey-api/openapi-ts/blob/main/packages/openapi-ts/src/plugins/@hey-api/schemas/types.d.ts) interface.

## Examples

You can view live examples on [StackBlitz](https://stackblitz.com/orgs/github/hey-api/collections/openapi-ts-examples).

## Sponsors

Hey API is sponsor-funded. If you rely on Hey API in production, consider becoming a [sponsor](https://github.com/sponsors/hey-api) to accelerate the roadmap.

---

---
url: /openapi-ts/plugins/koa.md
description: Koa plugin for Hey API. Compatible with all our features.
---

# Koa soon

### About

[Koa](https://koajs.com) is a new web framework designed by the team behind Express, which aims to be a smaller, more expressive, and more robust foundation for web applications and APIs.

## Sponsors

Hey API is sponsor-funded. If you rely on Hey API in production, consider becoming a [sponsor](https://github.com/sponsors/hey-api) to accelerate the roadmap.

---

---
url: /openapi-ts/clients/ky.md
description: >-
  Generate a type-safe Ky v1 client from OpenAPI with the Ky client for
  openapi-ts. Fully compatible with validators, transformers, and all core
  features.
---

### About

[Ky](https://github.com/sindresorhus/ky) is a tiny and elegant JavaScript HTTP client based on the Fetch API.

The Ky client for Hey API generates a type-safe client from your OpenAPI spec, fully compatible with validators, transformers, and all core features.

### Collaborators

## Features

* seamless integration with `@hey-api/openapi-ts` ecosystem
* type-safe response data and errors
* response data validation and transformation
* access to the original request and response
* granular request and response customization options
* minimal learning curve thanks to extending the underlying technology
* support bundling inside the generated output

## Installation

In your [configuration](/openapi-ts/get-started), add `@hey-api/client-ky` to your plugins and you'll be ready to generate client artifacts. :tada:

::: code-group

```js [config]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: ['@hey-api/client-ky'], // [!code ++]
};
```

```sh [cli]
npx @hey-api/openapi-ts \
  -i hey-api/backend \
  -o src/client \
  -c @hey-api/client-ky # [!code ++]
```

:::

## Configuration

The Ky client is built as a thin wrapper on top of Ky, extending its functionality to work with Hey API. If you're already familiar with Ky, configuring your client will feel like working directly with Ky.

When we installed the client above, it created a [`client.gen.ts`](/openapi-ts/output#client) file. You will most likely want to configure the exported `client` instance. There are two ways to do that.

### `setConfig()`

This is the simpler approach. You can call the `setConfig()` method at the beginning of your application or anytime you need to update the client configuration. You can pass any Ky configuration option to `setConfig()`, and even your own [`ky`](#custom-instance) instance.

```js
import { client } from 'client/client.gen';

client.setConfig({
  baseUrl: 'https://example.com',
});
```

The disadvantage of this approach is that your code may call the `client` instance before it's configured for the first time. Depending on your use case, you might need to use the second approach.

### Runtime API

Since `client.gen.ts` is a generated file, we can't directly modify it. Instead, we can tell our configuration to use a custom file implementing the Runtime API. We do that by specifying the `runtimeConfigPath` option.

```js
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    {
      name: '@hey-api/client-ky',
      runtimeConfigPath: './src/hey-api.ts', // [!code ++]
    },
  ],
};
```

In our custom file, we need to export a `createClientConfig()` method. This function is a simple wrapper allowing us to override configuration values.

::: code-group

```ts [hey-api.ts]
import type { CreateClientConfig } from './client/client.gen';

export const createClientConfig: CreateClientConfig = (config) => ({
  ...config,
  baseUrl: 'https://example.com',
});
```

:::

With this approach, `client.gen.ts` will call `createClientConfig()` before initializing the `client` instance. If needed, you can still use `setConfig()` to update the client configuration later.

### `createClient()`

You can also create your own client instance. You can use it to manually send requests or point it to a different domain.

```js
import { createClient } from './client/client';

const myClient = createClient({
  baseUrl: 'https://example.com',
});
```

You can also pass this instance to any SDK function through the `client` option. This will override the default instance from `client.gen.ts`.

```js
const response = await getFoo({
  client: myClient,
});
```

### SDKs

Alternatively, you can pass the client configuration options to each SDK function. This is useful if you don't want to create a client instance for one-off use cases.

```js
const response = await getFoo({
  baseUrl: 'https://example.com', // <-- override default configuration
});
```

## Interceptors

Interceptors (middleware) can be used to modify requests before they're sent or responses before they're returned to your application.

They can be added with `use`, removed with `eject`, and updated wth `update`. The `use` and `update` methods will return the ID of the interceptor for use with `eject` and `update`. Ky does not have the interceptor functionality, so we implement our own.

### Example: Request interceptor

::: code-group

```js [use]
import { client } from 'client/client.gen';

async function myInterceptor(request) {
  // do something
  return request;
}

interceptorId = client.interceptors.request.use(myInterceptor);
```

```js [eject]
import { client } from 'client/client.gen';

// eject by ID
client.interceptors.request.eject(interceptorId);

// eject by reference
client.interceptors.request.eject(myInterceptor);
```

```js [update]
import { client } from 'client/client.gen';

async function myNewInterceptor(request) {
  // do something
  return request;
}

// update by ID
client.interceptors.request.update(interceptorId, myNewInterceptor);

// update by reference
client.interceptors.request.update(myInterceptor, myNewInterceptor);
```

:::

### Example: Response interceptor

::: code-group

```js [use]
import { client } from 'client/client.gen';

async function myInterceptor(response) {
  // do something
  return response;
}

interceptorId = client.interceptors.response.use(myInterceptor);
```

```js [eject]
import { client } from 'client/client.gen';

// eject by ID
client.interceptors.response.eject(interceptorId);

// eject by reference
client.interceptors.response.eject(myInterceptor);
```

```js [update]
import { client } from 'client/client.gen';

async function myNewInterceptor(response) {
  // do something
  return response;
}

// update by ID
client.interceptors.response.update(interceptorId, myNewInterceptor);

// update by reference
client.interceptors.response.update(myInterceptor, myNewInterceptor);
```

:::

::: tip
To eject, you must provide the ID or reference of the interceptor passed to `use()`, the ID is the value returned by `use()` and `update()`.
:::

## Auth

The SDKs include auth mechanisms for every endpoint. You will want to configure the `auth` field to pass the right token for each request. The `auth` field can be a string or a function returning a string representing the token. The returned value will be attached only to requests that require auth.

```js
import { client } from 'client/client.gen';

client.setConfig({
  auth: () => '<my_token>', // [!code ++]
  baseUrl: 'https://example.com',
});
```

If you're not using SDKs or generating auth, using interceptors is a common approach to configuring auth for each request.

```js
import { client } from 'client/client.gen';

client.interceptors.request.use((request, options) => {
  request.headers.set('Authorization', 'Bearer <my_token>'); // [!code ++]
  return request;
});
```

## Build URL

If you need to access the compiled URL, you can use the `buildUrl()` method. It's loosely typed by default to accept almost any value; in practice, you will want to pass a type hint.

```ts
type FooData = {
  path: {
    fooId: number;
  };
  query?: {
    bar?: string;
  };
  url: '/foo/{fooId}';
};

const url = client.buildUrl<FooData>({
  path: {
    fooId: 1,
  },
  query: {
    bar: 'baz',
  },
  url: '/foo/{fooId}',
});
console.log(url); // prints '/foo/1?bar=baz'
```

## Custom Instance

You can provide a custom `ky` instance. This is useful if you need to extend the default instance with extra functionality, or replace it altogether.

```js
import { client } from 'client/client.gen';

client.setConfig({
  ky: ky.create({
    /* custom `ky` instance */
  }),
});
```

You can use any of the approaches mentioned in [Configuration](#configuration), depending on how granular you want your custom instance to be.

## API

You can view the complete list of options in the [UserConfig](https://github.com/hey-api/openapi-ts/blob/main/packages/openapi-ts/src/plugins/@hey-api/client-ky/types.d.ts) interface.

## Examples

You can view live examples on [StackBlitz](https://stackblitz.com/orgs/github/hey-api/collections/openapi-ts-examples).

## Sponsors

Hey API is sponsor-funded. If you rely on Hey API in production, consider becoming a [sponsor](https://github.com/sponsors/hey-api) to accelerate the roadmap.

---

---
url: /openapi-ts/license.md
description: License FAQ.
---

# License

### MIT License

Copyright (c) Hey API

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

---

---
url: /openapi-ts/migrating.md
description: Migrating to @hey-api/openapi-ts.
---

# Migrating

While we try to avoid breaking changes, sometimes it's unavoidable in order to offer you the latest features. This page lists changes that require updates to your code. If you run into a problem with migration, please [open an issue](https://github.com/hey-api/openapi-ts/issues).

## v0.90.0

### Resolvers API

The [Resolvers API](/openapi-ts/plugins/concepts/resolvers) has been simplified and expanded to provide a more consistent behavior across plugins. You can view a few common examples on the [Resolvers](/openapi-ts/plugins/concepts/resolvers) page.

### Structure API

The [SDK plugin](/openapi-ts/plugins/sdk) and [Angular plugin](/openapi-ts/plugins/angular) now implement the Structure API, enabling more complex structures and fixing several known issues.

Some Structure APIs are incompatible with the previous configuration, most notably the `methodNameBuilder` function, which accepted the operation object as an argument. You can read the [SDK Output](/openapi-ts/plugins/sdk#output) section to familiarize yourself with the Structure API.

Please [open an issue](https://github.com/hey-api/openapi-ts/issues) if you're unable to migrate your configuration to the new syntax.

## v0.89.0

### Prefer named exports

This release changes the default for `index.ts` to prefer named exports. Named exports may lead to better IDE and bundler performance compared to asterisk (`*`) as your tooling doesn't have to inspect the underlying module to discover exports.

While this change is merely cosmetic, you can set `output.preferExportAll` to `true` if you prefer to use the asterisk.

```js
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: {
    path: 'src/client',
    preferExportAll: true, // [!code ++]
  },
};
```

### Removed `symbol:setValue:*` events

These events have been removed in favor of `node:set:*` events.

## v0.88.0

### Removed `compiler` and `tsc` exports

This release removes the `compiler` utility functions. Instead, it introduces a new TypeScript DSL exposed under the `$` symbol. All plugins now use this interface, so you may notice slight changes in the generated output.

## v0.87.0

### Removed legacy clients

This release removes support for legacy clients and plugins. Please migrate to the new clients if you haven't done so yet. If you're unable to do so due to a missing feature, let us know on [GitHub](https://github.com/hey-api/openapi-ts/issues).

## v0.86.0

### Removed Node 18 support

This release bumps the minimum required Node version to 20.19.

## v0.85.0

### Updated `output` options

We made the `output` configuration more consistent by using `null` to represent disabled options. This change does not affect boolean options.

```js
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: {
    format: false, // [!code --]
    format: null, // [!code ++]
    lint: false, // [!code --]
    lint: null, // [!code ++]
    path: 'src/client',
    tsConfigPath: 'off', // [!code --]
    tsConfigPath: null, // [!code ++]
  },
};
```

### Updated Pinia Colada query options

Pinia Colada query options now use `defineQueryOptions` to improve reactivity support. Instead of calling the query options function, you can use one of the following approaches.

::: code-group

```ts [no params]
useQuery(getPetsQuery);
```

```ts [constant]
useQuery(getPetByIdQuery, () => ({
  path: {
    petId: 1,
  },
}));
```

```ts [reactive]
const petId = ref<number | null>(1);

useQuery(getPetByIdQuery, () => ({
  path: {
    petId: petId.value,
  },
}));
```

```ts [properties]
const petId = ref<number | null>(1);

useQuery(() => ({
  ...getPetByIdQuery({
    path: { petId: petId.value as number },
  }),
  enabled: () => petId.value != null,
}));
```

:::

## v0.84.0

### Symbol API

This release improves the Symbol API, which adds the capability to place symbols in arbitrary files. We preserved the previous output structure for all plugins except Angular.

You can preserve the previous Angular output by writing your own [placement function](/openapi-ts/configuration/parser#hooks-symbols).

### TypeScript renderer

We ship a dedicated TypeScript renderer for `.ts` files. This release improves the renderer's ability to group and sort imported modules, resulting in a more polished output.

### Removed `output` plugin option

Due to the Symbol API release, this option has been removed from the Plugin API.

## v0.83.0

### Symbol API

This release adds the Symbol API, which significantly reduces the risk of naming collisions. While the generated output should only include formatting changes, this feature introduces breaking changes to the Plugin API that affect custom plugins.

We will update the [custom plugin guide](/openapi-ts/plugins/custom) once the Plugin API becomes more stable.

### Removed `groupByTag` Pinia Colada option

This option has been removed to provide a more consistent API across plugins. We plan to bring it back in a future release.

## v0.82.0

### Hooks API

This release adds the [Hooks API](/openapi-ts/configuration/parser#hooks), giving you granular control over which operations generate queries and mutations. As a result, we tightened the previous behavior and POST operations no longer generate queries by default. To preserve the old behavior, add a custom matcher.

```js
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  parser: {
    hooks: {
      operations: {
        isQuery: (op) => (op.method === 'post' ? true : undefined), // [!code ++]
      },
    },
  },
};
```

## v0.81.0

### Server-Sent Events (SSE)

This release adds support for server-sent events (SSE). Instead of treating `text/event-stream` content types as regular HTTP methods, we now generate SSE streams. In practice, you will want to update your affected endpoints to process streamed events.

::: code-group

```js [before]
const { data } = await foo();
console.log(data.type);
```

```js [after]
const { stream } = await foo();
for await (const event of stream) {
  console.log(event.type);
}
```

:::

## v0.80.0

### Added Zod 4 and Zod Mini

This release adds support for Zod 4 and Zod Mini. By default, the `zod` plugin will generate output for Zod 4. If you want to preserve the previous output for Zod 3 or use Zod Mini, set `compatibilityVersion` to `3` or `mini`.

::: code-group

```js [Zod 3]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    // ...other plugins
    {
      name: 'zod',
      compatibilityVersion: 3, // [!code ++]
    },
  ],
};
```

```js [Zod Mini]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    // ...other plugins
    {
      name: 'zod',
      compatibilityVersion: 'mini', // [!code ++]
    },
  ],
};
```

:::

## v0.79.0

### Removed `typescript+namespace` enums mode

Due to a simpler TypeScript plugin implementation, the `typescript+namespace` enums mode is no longer necessary. This mode was used in the past to group inline enums under the same namespace. With the latest changes, this behavior is no longer supported. You can either choose to ignore inline enums (default), or use the `enums` transform (added in v0.78.0) to convert them into reusable components which will get exported as usual.

## v0.78.0

### Added `parser` options

Previously, `@hey-api/typescript` would generate correct types, but the validator plugins would have to re-implement the same logic or generate schemas that didn't match the generated types.

Since neither option was ideal, this release adds a dedicated place for `parser` options. Parser is responsible for preparing the input so plugins can generate more accurate output with less effort.

You can learn more about configuring parser on the [Parser](/openapi-ts/configuration/parser) page.

### Moved `input` options

The following options were moved to the new `parser` group.

* `input.filters` moved to `parser.filters`
* `input.pagination` moved to `parser.pagination`
* `input.patch` moved to `parser.patch`
* `input.validate_EXPERIMENTAL` moved to `parser.validate_EXPERIMENTAL`

### Updated `typescript` options

The following options were renamed.

* `enumsCase` moved to `enums.case`
* `enumsConstantsIgnoreNull` moved to `enums.constantsIgnoreNull`

### Moved `typescript` options

The following options were moved to the new `parser` group.

* `exportInlineEnums` moved to `parser.transforms.enums`
* `readOnlyWriteOnlyBehavior` moved to `parser.transforms.readWrite.enabled`
* `readableNameBuilder` moved to `parser.transforms.readWrite.responses.name`
* `writableNameBuilder` moved to `parser.transforms.readWrite.requests.name`

### Updated `readWrite.responses` name

Additionally, the naming pattern for response schemas has changed from `{name}Readable` to `{name}`. This is to prevent your code from breaking by default when using a schema that gets updated with a write-only field.

## v0.77.0

### Updated `sdk.validator` option

Clients can now validate both request and response data. As a result, passing a boolean or string to `validator` will control both of these options. To preserve the previous behavior, set `validator.request` to `false` and `validator.response` to your previous configuration.

```js
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    // ...other plugins
    {
      name: '@hey-api/sdk',
      validator: true, // [!code --]
      validator: { // [!code ++]
        request: false, // [!code ++]
        response: true, // [!code ++]
      }, // [!code ++]
    },
  ],
};
```

### Updated Plugin API

Please refer to the [custom plugin](/openapi-ts/plugins/custom) tutorial for the latest guide.

## v0.76.0

### Single Valibot schema per request

Previously, we generated a separate schema for each endpoint parameter and request body. In v0.76.0, a single request schema is generated for the whole endpoint. It may contain a request body, parameters, and headers.

```ts
const vData = v.object({
  body: v.optional(
    v.object({
      foo: v.optional(v.string()),
      bar: v.optional(v.union([v.number(), v.null()])),
    }),
  ),
  headers: v.optional(v.never()),
  path: v.object({
    baz: v.string(),
  }),
  query: v.optional(v.never()),
});
```

If you need to access individual fields, you can do so using the [`.entries`](https://valibot.dev/api/object/) API. For example, we can get the request body schema with `vData.entries.body`.

## v0.75.0

### Updated TanStack Query options

The TanStack Query plugin options have been expanded to support more naming and casing patterns. As a result, the following options have been renamed.

* `queryOptionsNameBuilder` renamed to `queryOptions`
* `infiniteQueryOptionsNameBuilder` renamed to `infiniteQueryOptions`
* `mutationOptionsNameBuilder` renamed to `mutationOptions`
* `queryKeyNameBuilder` renamed to `queryKeys`
* `infiniteQueryKeyNameBuilder` renamed to `infiniteQueryKeys`

### Added `plugin.forEach()` method

This method replaces the `.subscribe()` method. Additionally, `.forEach()` is executed immediately, which means we don't need the `before` and `after` events – simply move your code before and after the `.forEach()` block.

```ts
plugin.subscribe('operation', (event) => { // [!code --]
  // do something with event // [!code --]
}); // [!code --]
plugin.subscribe('schema', (event) => { // [!code --]
plugin.forEach('operation', 'schema', (event) => { // [!code ++]
  // do something with event
});
```

## v0.74.0

### Single Zod schema per request

Previously, we generated a separate schema for each endpoint parameter and request body. In v0.74.0, a single request schema is generated for the whole endpoint. It may contain a request body, parameters, and headers.

```ts
const zData = z.object({
  body: z
    .object({
      foo: z.string().optional(),
      bar: z.union([z.number(), z.null()]).optional(),
    })
    .optional(),
  headers: z.never().optional(),
  path: z.object({
    baz: z.string(),
  }),
  query: z.never().optional(),
});
```

If you need to access individual fields, you can do so using the [`.shape`](https://zod.dev/api?id=shape) API. For example, we can get the request body schema with `zData.shape.body`.

## v0.73.0

### Bundle `@hey-api/client-*` plugins

In previous releases, you had to install a separate client package to generate a fully working output, e.g. `npm install @hey-api/client-fetch`. This created a few challenges: getting started was slower, upgrading was sometimes painful, and bundling too. Beginning with v0.73.0, all Hey API clients are bundled by default and don't require installing any additional dependencies. You can remove any installed client packages and re-run `@hey-api/openapi-ts`.

```sh
npm uninstall @hey-api/client-fetch
```

## v0.72.0

### Added `sdk.classStructure` option

When generating class-based SDKs, we now try to infer the ideal structure using `operationId` keywords. If you'd like to preserve the previous behavior, set `classStructure` to `off`.

```js
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    // ...other plugins
    {
      classStructure: 'off', // [!code ++]
      name: '@hey-api/sdk',
    },
  ],
};
```

## v0.71.0

### Renamed `sdk.serviceNameBuilder` option

This option has been renamed to `sdk.classNameBuilder` to better represent its functionality. Additionally, it's no longer set by default. To preserve the previous behavior, update your configuration.

```js
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    // ...other plugins
    {
      classNameBuilder: '{{name}}Service', // [!code ++]
      name: '@hey-api/sdk',
      serviceNameBuilder: '{{name}}Service', // [!code --]
    },
  ],
};
```

## v0.68.0

### Upgraded input filters

Input filters now avoid generating invalid output without requiring you to specify every missing schema as in the previous releases. As part of this release, we changed the way filters are configured and removed the support for regular expressions. Let us know if regular expressions are still useful for you and want to bring them back!

::: code-group

```js [include]
export default {
  input: {
    // match only the schema named `foo` and `GET` operation for the `/api/v1/foo` path
    filters: {
      operations: {
        include: ['GET /api/v1/foo'], // [!code ++]
      },
      schemas: {
        include: ['foo'], // [!code ++]
      },
    },
    include: '^(#/components/schemas/foo|#/paths/api/v1/foo/get)$', // [!code --]
    path: 'hey-api/backend', // sign up at app.heyapi.dev
  },
  output: 'src/client',
  plugins: ['@hey-api/client-fetch'],
};
```

```js [exclude]
export default {
  input: {
    // match everything except for the schema named `foo` and `GET` operation for the `/api/v1/foo` path
    exclude: '^(#/components/schemas/foo|#/paths/api/v1/foo/get)$', // [!code --]
    filters: {
      operations: {
        exclude: ['GET /api/v1/foo'], // [!code ++]
      },
      schemas: {
        exclude: ['foo'], // [!code ++]
      },
    },
    path: 'hey-api/backend', // sign up at app.heyapi.dev
  },
  output: 'src/client',
  plugins: ['@hey-api/client-fetch'],
};
```

:::

## v0.67.0

### Respecting `moduleResolution` value in `tsconfig.json`

This release introduces functionality related to your `tsconfig.json` file. The initial feature properly respects the value of your `moduleResolution` field. If you're using `nodenext`, the relative module paths in your output will be appended with `.js`. To preserve the previous behavior where we never appended `.js` to relative module paths, set `output.tsConfigPath` to `off`.

```js
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: {
    path: 'src/client',
    tsConfigPath: 'off', // [!code ++]
  },
};
```

## v0.66.0

### Read-only and write-only fields

Starting with v0.66.0, `@hey-api/typescript` will generate separate types for payloads and responses if it detects any read-only or write-only fields. To preserve the previous behavior and generate a single type regardless, set `readOnlyWriteOnlyBehavior` to `off`.

```js
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    // ...other plugins
    {
      name: '@hey-api/typescript',
      readOnlyWriteOnlyBehavior: 'off', // [!code ++]
    },
  ],
};
```

## v0.64.0

### Added `ClientOptions` interface

The `Config` interface now accepts an optional generic extending `ClientOptions` instead of `boolean` type `ThrowOnError`.

```ts
type Foo = Config<false>; // [!code --]
type Foo = Config<{ throwOnError: false }>; // [!code ++]
```

### Added `client.baseUrl` option

You can use this option to configure the default base URL for the generated client. By default, we will attempt to resolve the first defined server or infer the base URL from the input path. If you'd like to preserve the previous behavior, set `baseUrl` to `false`.

```js
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    {
      baseUrl: false, // [!code ++]
      name: '@hey-api/client-fetch',
    },
  ],
};
```

## v0.63.0

### Client plugins

Clients are now plugins generating their own `client.gen.ts` file. There's no migration needed if you're using CLI. If you're using the configuration file, move `client` options to `plugins`.

```js
export default {
  client: '@hey-api/client-fetch', // [!code --]
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: ['@hey-api/client-fetch'], // [!code ++]
};
```

### Added `client.gen.ts` file

Related to above, the internal `client` instance previously located in `sdk.gen.ts` is now defined in `client.gen.ts`. If you're importing it in your code, update the import module.

```js
import { client } from 'client/sdk.gen'; // [!code --]
import { client } from 'client/client.gen'; // [!code ++]
```

### Moved `sdk.throwOnError` option

This SDK configuration option has been moved to the client plugins where applicable. Not every client can be configured to throw on error, so it didn't make sense to expose the option when it didn't have any effect.

```js
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    {
      name: '@hey-api/client-fetch',
      throwOnError: true, // [!code ++]
    },
    {
      name: '@hey-api/sdk',
      throwOnError: true, // [!code --]
    },
  ],
};
```

## v0.62.0

### Changed parser

Formerly known as the experimental parser, this is now the default parser. This change should not impact the generated output's functionality. However, there might be cases where this results in breaking changes due to different handling of certain scenarios. If you need to revert to the legacy parser, set the `experimentalParser` flag to `false`.

```js
export default {
  client: '@hey-api/client-fetch',
  experimentalParser: false, // [!code ++]
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
};
```

Note that the legacy parser is no longer supported and will be removed in the v1 release.

## v0.61.0

### Added `auth` option

Client package functions `accessToken` and `apiKey` were replaced with a single `auth` function for fetching auth tokens. If your API supports multiple auth mechanisms, you can use the `auth` argument to return the appropriate token.

```js
import { client } from 'client/sdk.gen';

client.setConfig({
  accessToken: () => '<my_token>', // [!code --]
  apiKey: () => '<my_token>', // [!code --]
  auth: (auth) => '<my_token>', // [!code ++]
});
```

Due to conflict with the Axios native `auth` option, we removed support for configuring Axios auth. Please let us know if you require this feature added back.

### Added `watch` option

While this is a new feature, supporting it involved replacing the `@apidevtools/json-schema-ref-parser` dependency with our own implementation. Since this was a big change, we're applying caution and marking this as a breaking change.

### Changed `parseAs: 'auto'` behavior

The Fetch API client will return raw response body as `ReadableStream` when `Content-Type` response header is undefined and `parseAs` is `auto`.

## v0.60.0

### Added `sdk.transformer` option

When generating SDKs, you now have to specify `transformer` in order to modify response data. By default, adding `@hey-api/transformers` to your plugins will only produce additional output. To preserve the previous functionality, set `sdk.transformer` to `true`.

```js
export default {
  client: '@hey-api/client-fetch',
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    // ...other plugins
    {
      dates: true,
      name: '@hey-api/transformers',
    },
    {
      name: '@hey-api/sdk',
      transformer: true, // [!code ++]
    },
  ],
};
```

## v0.59.0

### Added `logs.level` option

You can now configure different log levels. As part of this feature, we had to introduce a breaking change by moving the `debug` option to `logs.level`. This will affect you if you're calling `@hey-api/openapi-ts` from Node.js (not CLI) or using the configuration file.

```js
export default {
  client: '@hey-api/client-fetch',
  debug: true, // [!code --]
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  logs: {
    level: 'debug', // [!code ++]
  },
  output: 'src/client',
};
```

### Updated default `plugins`

`@hey-api/schemas` has been removed from the default plugins. To continue using it, add it to your plugins array.

```js
export default {
  client: '@hey-api/client-fetch',
  experimentalParser: true,
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    // ...other plugins
    '@hey-api/schemas', // [!code ++]
  ],
};
```

## v0.58.0

### Removed `schemas.gen.ts` re-export

`index.ts` will no longer re-export `schemas.gen.ts` to reduce the chance of producing broken output. Please update your code to import from `schemas.gen.ts` directly.

```js
import { mySchema } from 'client'; // [!code --]
import { mySchema } from 'client/schemas.gen'; // [!code ++]
```

### Removed `transformers.gen.ts` re-export

`index.ts` will no longer re-export `transformers.gen.ts` to reduce the chance of producing broken output. Please update your code to import from `transformers.gen.ts` directly.

```js
import { myTransformer } from 'client'; // [!code --]
import { myTransformer } from 'client/transformers.gen'; // [!code ++]
```

### Added `output.clean` option

By default, the `output.path` folder will be emptied on every run. To preserve the previous behavior, set `output.clean` to `false`.

```js
export default {
  client: '@hey-api/client-fetch',
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: {
    clean: false, // [!code ++]
    path: 'src/client',
  },
};
```

### Added `typescript.identifierCase` option

**This change affects only the experimental parser.** By default, the generated TypeScript interfaces will follow the PascalCase naming convention. In the previous versions, we tried to preserve the original name as much as possible. To keep the previous behavior, set `typescript.identifierCase` to `preserve`.

```js
export default {
  client: '@hey-api/client-fetch',
  experimentalParser: true,
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    // ...other plugins
    {
      identifierCase: 'preserve', // [!code ++]
      name: '@hey-api/typescript',
    },
  ],
};
```

## v0.57.0

### Renamed `@hey-api/services` plugin

This plugin has been renamed to `@hey-api/sdk`.

### Changed `sdk.output` value

To align with the updated name, the `@hey-api/sdk` plugin will generate an `sdk.gen.ts` file. This will result in a breaking change if you're importing from `services.gen.ts`. Please update your imports to reflect this change.

```js
import { client } from 'client/services.gen'; // [!code --]
import { client } from 'client/sdk.gen'; // [!code ++]
```

### Renamed `@hey-api/types` plugin

This plugin has been renamed to `@hey-api/typescript`.

### Added `typescript.exportInlineEnums` option

By default, inline enums (enums not defined as reusable components in the input file) will be generated only as inlined union types. You can set `exportInlineEnums` to `true` to treat inline enums as reusable components. When `true`, the exported enums will follow the style defined in `enums`.

This is a breaking change since in the previous versions, inline enums were always treated as reusable components. To preserve your current output, set `exportInlineEnums` to `true`. This feature works only with the experimental parser.

```js
export default {
  client: '@hey-api/client-fetch',
  experimentalParser: true,
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    // ...other plugins
    {
      exportInlineEnums: true, // [!code ++]
      name: '@hey-api/typescript',
    },
  ],
};
```

## v0.56.0

### Deprecated `tree` in `@hey-api/types`

This config option is deprecated and will be removed when the experimental parser becomes the default.

## v0.55.0

This release adds the ability to filter your OpenAPI specification before it's processed. This feature will be useful if you are working with a large specification and are interested in generating output only from a small subset.

This feature is available only in the experimental parser. In the future, this will become the default parser. To opt-in to the experimental parser, set the `experimentalParser` flag in your configuration to `true`.

### Deprecated `include` in `@hey-api/types`

This config option is deprecated and will be removed when the experimental parser becomes the default.

### Deprecated `filter` in `@hey-api/services`

This config option is deprecated and will be removed when the experimental parser becomes the default.

### Added `input.include` option

This config option can be used to replace the deprecated options. It accepts a regular expression string matching against references within the bundled specification.

```js
export default {
  client: '@hey-api/client-fetch',
  experimentalParser: true,
  input: {
    include: '^(#/components/schemas/foo|#/paths/api/v1/foo/get)$', // [!code ++]
    path: 'hey-api/backend', // sign up at app.heyapi.dev
  },
  output: 'src/client',
};
```

The configuration above will process only the schema named `foo` and `GET` operation for the `/api/v1/foo` path.

## v0.54.0

This release makes plugins first-class citizens. In order to achieve that, the following breaking changes were introduced.

### Removed CLI options

The `--types`, `--schemas`, and `--services` CLI options have been removed. You can list which plugins you'd like to use explicitly by passing a list of plugins as `--plugins <plugin1> <plugin2>`

### Removed `*.export` option

Previously, you could explicitly disable export of certain artifacts using the `*.export` option or its shorthand variant. These were both removed. You can now disable export of specific artifacts by manually defining an array of `plugins` and excluding the unwanted plugin.

::: code-group

```js [shorthand]
export default {
  client: '@hey-api/client-fetch',
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  schemas: false, // [!code --]
  plugins: ['@hey-api/types', '@hey-api/services'], // [!code ++]
};
```

```js [*.export]
export default {
  client: '@hey-api/client-fetch',
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  schemas: {
    export: false, // [!code --]
  },
  plugins: ['@hey-api/types', '@hey-api/services'], // [!code ++]
};
```

:::

### Renamed `schemas.name` option

Each plugin definition contains a `name` field. This was conflicting with the `schemas.name` option. As a result, it has been renamed to `nameBuilder`.

```js
export default {
  client: '@hey-api/client-fetch',
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  schemas: {
    name: (name) => `${name}Schema`, // [!code --]
  },
  plugins: [
    // ...other plugins
    {
      nameBuilder: (name) => `${name}Schema`, // [!code ++]
      name: '@hey-api/schemas',
    },
  ],
};
```

### Removed `services.include` shorthand option

Previously, you could use a string value as a shorthand for the `services.include` configuration option. You can now achieve the same result using the `include` option.

```js
export default {
  client: '@hey-api/client-fetch',
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  services: '^MySchema', // [!code --]
  plugins: [
    // ...other plugins
    {
      include: '^MySchema', // [!code ++]
      name: '@hey-api/services',
    },
  ],
};
```

### Renamed `services.name` option

Each plugin definition contains a `name` field. This was conflicting with the `services.name` option. As a result, it has been renamed to `serviceNameBuilder`.

```js
export default {
  client: '@hey-api/client-fetch',
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  services: {
    name: '{{name}}Service', // [!code --]
  },
  plugins: [
    // ...other plugins
    {
      serviceNameBuilder: '{{name}}Service', // [!code ++]
      name: '@hey-api/services',
    },
  ],
};
```

### Renamed `types.dates` option

Previously, you could set `types.dates` to a boolean or a string value, depending on whether you wanted to transform only type strings into dates, or runtime code too. Many people found these options confusing, so they have been simplified to a boolean and extracted into a separate `@hey-api/transformers` plugin.

```js
export default {
  client: '@hey-api/client-fetch',
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  types: {
    dates: 'types+transform', // [!code --]
  },
  plugins: [
    // ...other plugins
    {
      dates: true, // [!code ++]
      name: '@hey-api/transformers',
    },
  ],
};
```

### Removed `types.include` shorthand option

Previously, you could use a string value as a shorthand for the `types.include` configuration option. You can now achieve the same result using the `include` option.

```js
export default {
  client: '@hey-api/client-fetch',
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  types: '^MySchema', // [!code --]
  plugins: [
    // ...other plugins
    {
      include: '^MySchema', // [!code ++]
      name: '@hey-api/types',
    },
  ],
};
```

### Renamed `types.name` option

Each plugin definition contains a `name` field. This was conflicting with the `types.name` option. As a result, it has been renamed to `style`.

```js
export default {
  client: '@hey-api/client-fetch',
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  types: {
    name: 'PascalCase', // [!code --]
  },
  plugins: [
    // ...other plugins
    {
      name: '@hey-api/types',
      style: 'PascalCase', // [!code ++]
    },
  ],
};
```

## v0.53.0

### Changed schemas name pattern

Previously, generated schemas would have their definition names prefixed with `$`. This was problematic when using them with Svelte due to reserved keyword conflicts. The new naming pattern for schemas suffixes their definition names with `Schema`. You can continue using the previous pattern by setting the `schemas.name` configuration option.

```js
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  schemas: {
    name: (name) => `$${name}`, // [!code ++]
  },
};
```

### Renamed legacy clients

Legacy clients were renamed to signal they are deprecated more clearly. To continue using legacy clients, you will need to update your configuration and prefix them with `legacy/`.

::: code-group

```js [fetch]
export default {
  client: 'fetch', // [!code --]
  client: 'legacy/fetch', // [!code ++]
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
};
```

```js [axios]
export default {
  client: 'axios', // [!code --]
  client: 'legacy/axios', // [!code ++]
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
};
```

```js [angular]
export default {
  client: 'angular', // [!code --]
  client: 'legacy/angular', // [!code ++]
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
};
```

```js [node]
export default {
  client: 'node', // [!code --]
  client: 'legacy/node', // [!code ++]
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
};
```

```js [xhr]
export default {
  client: 'xhr', // [!code --]
  client: 'legacy/xhr', // [!code ++]
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
};
```

:::

## v0.52.0

### Removed internal `client` export

Previously, client packages would create a default client which you'd then import and configure.

```js
import { client, createClient } from '@hey-api/client-fetch';

createClient({
  baseUrl: 'https://example.com',
});

console.log(client.getConfig().baseUrl); // <-- 'https://example.com'
```

This client instance was used internally by services unless overridden. Apart from running `createClient()` twice, people were confused about the meaning of `global` configuration option.

Starting with v0.52.0, client packages will not create a default client. Instead, services will define their own client. You can now achieve the same configuration by importing `client` from services and using the new `setConfig()` method.

```js
import { client } from 'client/services.gen';

client.setConfig({
  baseUrl: 'https://example.com',
});

console.log(client.getConfig().baseUrl); // <-- 'https://example.com'
```

## v0.51.0

### Required `client` option

Client now has to be explicitly specified and `@hey-api/openapi-ts` will no longer generate a legacy Fetch API client by default. To preserve the previous default behavior, set the `client` option to `fetch`.

```js
export default {
  client: 'fetch', // [!code ++]
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
};
```

## v0.48.0

### Changed `methodNameBuilder()` signature

The `services.methodNameBuilder()` function now provides a single `operation` argument instead of multiple cherry-picked properties from it.

```js
import { createClient } from '@hey-api/openapi-ts';

createClient({
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  services: {
    methodNameBuilder: (service, name) => name, // [!code --]
    methodNameBuilder: (operation) => operation.name, // [!code ++]
  },
});
```

## v0.46.0

### Tree-shakeable services

By default, your services will now support [tree-shaking](https://developer.mozilla.org/docs/Glossary/Tree_shaking). You can either use wildcard imports

```js
import { DefaultService } from 'client/services.gen'; // [!code --]
import * as DefaultService from 'client/services.gen'; // [!code ++]

DefaultService.foo(); // only import needs to be changed
```

or update all references to service classes

```js
import { DefaultService } from 'client/services.gen'; // [!code --]
import { foo } from 'client/services.gen'; // [!code ++]

foo(); // all references need to be changed
```

If you want to preserve the old behavior, you can set the newly exposed `services.asClass` option to `true.`

```js
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  services: {
    asClass: true, // [!code ++]
  },
};
```

## v0.45.0

### Removed `client` inference

`@hey-api/openapi-ts` will no longer infer which client you want to generate. By default, we will create a `fetch` client. If you want a different client, you can specify it using the `client` option.

```js
export default {
  client: 'axios', // [!code ++]
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
};
```

## v0.44.0

### Moved `format`

This config option has been moved. You can now configure formatter using the `output.format` option.

```js
export default {
  format: 'prettier', // [!code --]
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: {
    format: 'prettier', // [!code ++]
    path: 'src/client',
  },
};
```

### Moved `lint`

This config option has been moved. You can now configure linter using the `output.lint` option.

```js
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  lint: 'eslint', // [!code --]
  output: {
    lint: 'eslint', // [!code ++]
    path: 'src/client',
  },
};
```

## v0.43.0

### Removed `enums.gen.ts`

This file has been removed. Instead, enums are exported from `types.gen.ts`. If you use imports from `enums.gen.ts`, you should be able to easily find and replace all instances.

```js
import { Foo } from 'client/enums.gen'; // [!code --]
import { Foo } from 'client/types.gen'; // [!code ++]
```

### Removed `Enum` postfix

Generated enum names are no longer postfixed with `Enum`. You can either alias your imports

```js
import { FooEnum } from 'client/types.gen'; // [!code --]
import { Foo as FooEnum } from 'client/types.gen'; // [!code ++]

console.log(FooEnum.value); // only import needs to be changed
```

or update all references to enums

```js
import { FooEnum } from 'client/types.gen'; // [!code --]
import { Foo } from 'client/types.gen'; // [!code ++]

console.log(Foo.value); // all references need to be changed
```

### Moved `enums`

This config option has been moved. You can now configure enums using the `types.enums` option.

```js
export default {
  enums: 'javascript', // [!code --]
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  types: {
    enums: 'javascript', // [!code ++]
  },
};
```

## v0.42.0

### Changed `format`

This config option has changed. You now need to specify a value (`biome` or `prettier`) to format the output (default: `false`).

```js{2}
export default {
  format: 'prettier',
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
}
```

### Changed `lint`

This config option has changed. You now need to specify a value (`biome` or `eslint`) to lint the output (default: `false`).

```js{3}
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  lint: 'eslint',
  output: 'src/client',
}
```

### Moved `operationId`

This config option has been moved. You can now configure it using the `services.operationId` option.

```js{5}
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  services: {
    operationId: true,
  },
}
```

## v0.41.0

### Removed `postfixServices`

This config option has been removed. You can now transform service names using the string pattern parameter.

```js{5}
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  services: {
    name: 'myAwesome{{name}}Api',
  },
}
```

### Removed `serviceResponse`

This config option has been removed. You can now configure service responses using the `services.response` option.

```js{5}
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  services: {
    response: 'body',
  },
}
```

### Removed `useDateType`

This config option has been removed. You can now configure date type using the `types.dates` option.

```js{5}
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  type: {
    dates: true,
  },
}
```

## v0.40.0

### Renamed `models.gen.ts` file

`models.gen.ts` is now called `types.gen.ts`. If you use imports from `models.gen.ts`, you should be able to easily find and replace all instances.

```js
import type { Model } from 'client/models.gen' // [!code --]
import type { Model } from 'client/types.gen' // [!code ++]
```

### Renamed `exportModels`

This config option is now called `types`.

### PascalCase for types

You can now choose to export types using the PascalCase naming convention.

```js{5}
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  types: {
    name: 'PascalCase',
  },
}
```

### Exported `enums.gen.ts` file

Enums are now re-exported from the main `index.ts` file.

## v0.39.0

### Single `enums.gen.ts` file

Enums are now exported from a separate file. If you use imports from `models.ts`, you can change them to `enums.gen.ts`.

```js
import { Enum } from 'client/models'; // [!code --]
import { Enum } from 'client/enums.gen'; // [!code ++]
```

### Renamed `models.ts` file

`models.ts` is now called `models.gen.ts`. If you use imports from `models.ts`, you should be able to easily find and replace all instances.

```js
import type { Model } from 'client/models' // [!code --]
import type { Model } from 'client/models.gen' // [!code ++]
```

### Renamed `schemas.ts` file

`schemas.ts` is now called `schemas.gen.ts`. If you use imports from `schemas.ts`, you should be able to easily find and replace all instances.

```js
import { $Schema } from 'client/schemas'; // [!code --]
import { $Schema } from 'client/schemas.gen'; // [!code ++]
```

### Renamed `services.ts` file

`services.ts` is now called `services.gen.ts`. If you use imports from `services.ts`, you should be able to easily find and replace all instances.

```js
import { DefaultService } from 'client/services'; // [!code --]
import { DefaultService } from 'client/services.gen'; // [!code ++]
```

### Deprecated exports from `index.ts`

Until this release, `index.ts` file exported all generated artifacts. Starting from this release, enums are no longer exported from `index.ts`. Models, schemas, and services will continue to be exported from `index.ts` to avoid a huge migration lift, but we recommend migrating to import groups per artifact type.

```js
import { Enum, type Model, $Schema, DefaultService } from 'client' // [!code --]
import { Enum } from 'client/enums.gen' // [!code ++]
import type { Model } from 'client/models.gen' // [!code ++]
import { $Schema } from 'client/schemas.gen' // [!code ++]
import { DefaultService } from 'client/services.gen' // [!code ++]
```

### Prefer `unknown`

Types that cannot be determined will now be generated as `unknown` instead of `any`. To dismiss any errors, you can cast your variables back to `any`, but we recommend updating your code to work with `unknown` types.

```js
const foo = bar as any
```

## v0.38.0

### Renamed `write`

This config option is now called `dryRun` (file) or `--dry-run` (CLI). To restore existing functionality, invert the value, ie. `write: true` is `dryRun: false` and `write: false` is `dryRun: true`.

## v0.36.0

### JSON Schema 2020-12

Schemas are exported directly from OpenAPI specification. This means your schemas might change depending on which OpenAPI version you're using. If this release caused a field to be removed, consult the JSON Schema documentation on how to obtain the same value from JSON Schema (eg. [required properties](https://json-schema.org/understanding-json-schema/reference/object#required)).

### Renamed `exportSchemas`

This config option is now called `schemas`.

## v0.35.0

### Removed `postfixModels`

This config option has been removed.

## v0.34.0

### Single `services.ts` file

Services are now exported from a single file. If you used imports from individual service files, these will need to be updated to refer to the single `services.ts` file.

## v0.31.1

### Merged enums options

`useLegacyEnums` config option is now `enums: 'typescript'` and existing `enums: true` option is now `enums: 'javascript'`.

## v0.31.0

### Single `models.ts` file

TypeScript interfaces are now exported from a single file. If you used imports from individual model files, these will need to be updated to refer to the single `models.ts` file.

### Single `schemas.ts` file

Schemas are now exported from a single file. If you used imports from individual schema files, these will need to be updated to refer to the single `schemas.ts` file.

## v0.27.38

### `useOptions: true`

By default, generated clients will use a single object argument to pass values to API calls. This is a significant change from the previous default of unspecified array of arguments. If migrating your application in one go isn't feasible, we recommend deprecating your old client and generating a new client.

```ts
import { DefaultService } from 'client/services'; // <-- old client with array arguments

import { DefaultService } from 'client_v2/services'; // <-- new client with options argument
```

This way, you can gradually switch over to the new syntax as you update parts of your code. Once you've removed all instances of `client` imports, you can safely delete the old `client` folder and find and replace all `client_v2` calls to `client`.

## v0.27.36

### `exportSchemas: true`

By default, we will create schemas from your OpenAPI specification. Use `exportSchemas: false` to preserve the old behavior.

## v0.27.32

### Renamed `Config` interface

This interface is now called `UserConfig`.

## v0.27.29

### Renamed `openapi` CLI command

This command is now called `openapi-ts`.

## v0.27.26

### Removed `indent`

This config option has been removed. Use a [code formatter](/openapi-ts/configuration#formatting) to modify the generated files code style according to your preferences.

## v0.27.24

### Removed `useUnionTypes`

This config option has been removed. Generated types will behave the same as `useUnionTypes: true` before.

## OpenAPI TypeScript Codegen

`@hey-api/openapi-ts` was originally forked from Ferdi Koomen's [openapi-typescript-codegen](https://github.com/ferdikoomen/openapi-typescript-codegen). Therefore, we want you to be able to migrate your projects. Migration should be relatively straightforward if you follow the release notes on this page. Start on [v0.27.24](#v0-27-24) and scroll to the release you're migrating to.

---

---
url: /openapi-ts/mocks.md
description: Learn about mocking HTTP servers with @hey-api/openapi-ts.
---

# Mocks

Realistic mock data is an important component of every robust development process, testing strategy, and product presentation.

## Options

Hey API natively supports the following mocking frameworks.

* [Chance](/openapi-ts/plugins/chance) Soon
* [Faker](/openapi-ts/plugins/faker) Soon
* [Falso](/openapi-ts/plugins/falso) Soon
* [MSW](/openapi-ts/plugins/msw) Soon
* [Nock](/openapi-ts/plugins/nock) Soon
* [Supertest](/openapi-ts/plugins/supertest) Soon

Don't see your framework? Let us know your interest by [opening an issue](https://github.com/hey-api/openapi-ts/issues).

## Examples

You can view live examples on [StackBlitz](https://stackblitz.com/orgs/github/hey-api/collections/openapi-ts-examples).

## Sponsors

Hey API is sponsor-funded. If you rely on Hey API in production, consider becoming a [sponsor](https://github.com/sponsors/hey-api) to accelerate the roadmap.

---

---
url: /openapi-ts/plugins/msw.md
description: MSW plugin for Hey API. Compatible with all our features.
---

# MSW soon

### About

[MSW](https://mswjs.io) is an API mocking library that allows you to write client-agnostic mocks and reuse them across any frameworks, tools, and environments.

## Sponsors

Hey API is sponsor-funded. If you rely on Hey API in production, consider becoming a [sponsor](https://github.com/sponsors/hey-api) to accelerate the roadmap.

---

---
url: /openapi-ts/plugins/nest.md
description: Nest plugin for Hey API. Compatible with all our features.
---

# Nest soon

### About

[Nest](https://nestjs.com) is a progressive Node.js framework for building efficient, reliable and scalable server-side applications.

## Sponsors

Hey API is sponsor-funded. If you rely on Hey API in production, consider becoming a [sponsor](https://github.com/sponsors/hey-api) to accelerate the roadmap.

---

---
url: /openapi-ts/clients/next-js.md
description: >-
  Generate a type-safe Next.js client from OpenAPI with the Next.js client for
  openapi-ts. Fully compatible with validators, transformers, and all core
  features.
---

# Next.js

### About

[Next.js](https://nextjs.org) is the React framework for the web. Used by some of the world's largest companies, Next.js enables you to create high-quality web applications with the power of React components.

The Next.js client for Hey API generates a type-safe client from your OpenAPI spec, fully compatible with validators, transformers, and all core features.

## Features

* seamless integration with `@hey-api/openapi-ts` ecosystem
* type-safe response data and errors
* response data validation and transformation
* access to the original request and response
* granular request and response customization options
* minimal learning curve thanks to extending the underlying technology
* support bundling inside the generated output

## Installation

In your [configuration](/openapi-ts/get-started), add `@hey-api/client-next` to your plugins and you'll be ready to generate client artifacts. :tada:

::: code-group

```js [config]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: ['@hey-api/client-next'], // [!code ++]
};
```

```sh [cli]
npx @hey-api/openapi-ts \
  -i hey-api/backend \
  -o src/client \
  -c @hey-api/client-next # [!code ++]
```

:::

## Configuration

The Next.js client is built as a thin wrapper on top of [fetch](https://nextjs.org/docs/app/api-reference/functions/fetch), extending its functionality to work with Hey API. If you're already familiar with Fetch, configuring your client will feel like working directly with Fetch API.

When we installed the client above, it created a [`client.gen.ts`](/openapi-ts/output#client) file. You will most likely want to configure the exported `client` instance. There are two ways to do that.

### Runtime API

Since `client.gen.ts` is a generated file, we can't directly modify it. Instead, we can tell our configuration to use a custom file implementing the Runtime API. We do that by specifying the `runtimeConfigPath` option.

```js
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    {
      name: '@hey-api/client-next',
      runtimeConfigPath: './src/hey-api.ts', // [!code ++]
    },
  ],
};
```

In our custom file, we need to export a `createClientConfig()` method. This function is a simple wrapper allowing us to override configuration values.

::: code-group

```ts [hey-api.ts]
import type { CreateClientConfig } from './client/client.gen';

export const createClientConfig: CreateClientConfig = (config) => ({
  ...config,
  baseUrl: 'https://example.com',
});
```

:::

With this approach, `client.gen.ts` will call `createClientConfig()` before initializing the `client` instance. This is the recommended approach because it guarantees the client will be initialized in both server and client environment. If needed, you can still use `setConfig()` to update the client configuration later.

### `setConfig()`

This is the simpler approach. You can call the `setConfig()` method at the beginning of your application or anytime you need to update the client configuration. You can pass any Fetch API configuration option to `setConfig()`, and even your own [Fetch](#custom-instance) implementation.

```js
import { client } from 'client/client.gen';

client.setConfig({
  baseUrl: 'https://example.com',
});
```

The disadvantage of this approach is that your code may call the `client` instance before it's configured for the first time. Depending on your use case, this might be an acceptable trade-off. However, our Next.js users usually want to use the first approach.

### `createClient()`

You can also create your own client instance. You can use it to manually send requests or point it to a different domain.

```js
import { createClient } from './client/client';

const myClient = createClient({
  baseUrl: 'https://example.com',
});
```

You can also pass this instance to any SDK function through the `client` option. This will override the default instance from `client.gen.ts`.

```js
const response = await getFoo({
  client: myClient,
});
```

### SDKs

Alternatively, you can pass the client configuration options to each SDK function. This is useful if you don't want to create a client instance for one-off use cases.

```js
const response = await getFoo({
  baseUrl: 'https://example.com', // <-- override default configuration
});
```

## Interceptors

Interceptors (middleware) can be used to modify requests before they're sent or responses before they're returned to your application.

They can be added with `use`, removed with `eject`, and updated wth `update`. The `use` and `update` methods will return the ID of the interceptor for use with `eject` and `update`. Fetch API does not have the interceptor functionality, so we implement our own.

### Example: Request interceptor

::: code-group

```js [use]
import { client } from 'client/client.gen';

async function myInterceptor(request) {
  // do something
  return request;
}

interceptorId = client.interceptors.request.use(myInterceptor);
```

```js [eject]
import { client } from 'client/client.gen';

// eject by ID
client.interceptors.request.eject(interceptorId);

// eject by reference
client.interceptors.request.eject(myInterceptor);
```

```js [update]
import { client } from 'client/client.gen';

async function myNewInterceptor(request) {
  // do something
  return request;
}

// update by ID
client.interceptors.request.update(interceptorId, myNewInterceptor);

// update by reference
client.interceptors.request.update(myInterceptor, myNewInterceptor);
```

:::

### Example: Response interceptor

::: code-group

```js [use]
import { client } from 'client/client.gen';

async function myInterceptor(response) {
  // do something
  return response;
}

interceptorId = client.interceptors.response.use(myInterceptor);
```

```js [eject]
import { client } from 'client/client.gen';

// eject by ID
client.interceptors.response.eject(interceptorId);

// eject by reference
client.interceptors.response.eject(myInterceptor);
```

```js [update]
import { client } from 'client/client.gen';

async function myNewInterceptor(response) {
  // do something
  return response;
}

// update by ID
client.interceptors.response.update(interceptorId, myNewInterceptor);

// update by reference
client.interceptors.response.update(myInterceptor, myNewInterceptor);
```

:::

::: tip
To eject, you must provide the ID or reference of the interceptor passed to `use()`, the ID is the value returned by `use()` and `update()`.
:::

## Auth

The SDKs include auth mechanisms for every endpoint. You will want to configure the `auth` field to pass the right token for each request. The `auth` field can be a string or a function returning a string representing the token. The returned value will be attached only to requests that require auth.

```js
import { client } from 'client/client.gen';

client.setConfig({
  auth: () => '<my_token>', // [!code ++]
  baseUrl: 'https://example.com',
});
```

If you're not using SDKs or generating auth, using interceptors is a common approach to configuring auth for each request.

```js
import { client } from 'client/client.gen';

client.interceptors.request.use((options) => {
  options.headers.set('Authorization', 'Bearer <my_token>'); // [!code ++]
});
```

## Build URL

If you need to access the compiled URL, you can use the `buildUrl()` method. It's loosely typed by default to accept almost any value; in practice, you will want to pass a type hint.

```ts
type FooData = {
  path: {
    fooId: number;
  };
  query?: {
    bar?: string;
  };
  url: '/foo/{fooId}';
};

const url = client.buildUrl<FooData>({
  path: {
    fooId: 1,
  },
  query: {
    bar: 'baz',
  },
  url: '/foo/{fooId}',
});
console.log(url); // prints '/foo/1?bar=baz'
```

## Custom Instance

You can provide a custom `fetch` instance. This is useful if you need to extend the default instance with extra functionality, or replace it altogether.

```js
import { client } from 'client/client.gen';

client.setConfig({
  fetch: () => {
    /* custom `fetch` method */
  },
});
```

You can use any of the approaches mentioned in [Configuration](#configuration), depending on how granular you want your custom instance to be.

## API

You can view the complete list of options in the [UserConfig](https://github.com/hey-api/openapi-ts/blob/main/packages/openapi-ts/src/plugins/@hey-api/client-next/types.d.ts) interface.

## Examples

You can view live examples on [StackBlitz](https://stackblitz.com/orgs/github/hey-api/collections/openapi-ts-examples).

## Sponsors

Hey API is sponsor-funded. If you rely on Hey API in production, consider becoming a [sponsor](https://github.com/sponsors/hey-api) to accelerate the roadmap.

---

---
url: /openapi-ts/plugins/nock.md
description: Nock plugin for Hey API. Compatible with all our features.
---

# Nock soon

### About

[Nock](https://github.com/nock/nock) is an HTTP server mocking and expectations library for Node.js.

## Sponsors

Hey API is sponsor-funded. If you rely on Hey API in production, consider becoming a [sponsor](https://github.com/sponsors/hey-api) to accelerate the roadmap.

---

---
url: /openapi-ts/clients/nuxt.md
description: >-
  Generate a type-safe Nuxt v3 client from OpenAPI with the Nuxt client for
  openapi-ts. Fully compatible with validators, transformers, and all core
  features.
---

::: warning
Nuxt client is currently in beta. The interface might change before it becomes stable. We encourage you to leave feedback on [GitHub](https://github.com/hey-api/openapi-ts/issues).
:::

### About

[Nuxt](https://nuxt.com) is an open source framework that makes web development intuitive and powerful.

The Nuxt client for Hey API generates a type-safe client from your OpenAPI spec, fully compatible with validators, transformers, and all core features.

## Features

* Nuxt v3 support
* seamless integration with `@hey-api/openapi-ts` ecosystem
* type-safe response data and errors
* response data validation and transformation
* access to the original request and response
* granular request and response customization options
* minimal learning curve thanks to extending the underlying technology
* support bundling inside the generated output

## Installation

Start by adding `@hey-api/nuxt` to your dependencies.

::: code-group

```sh [npm]
npm install @hey-api/nuxt
```

```sh [pnpm]
pnpm add @hey-api/nuxt
```

```sh [yarn]
yarn add @hey-api/nuxt
```

```sh [bun]
bun add @hey-api/nuxt
```

:::

In your [configuration](/openapi-ts/get-started), add `@hey-api/client-nuxt` to your plugins and you'll be ready to generate client artifacts. :tada:

::: code-group

```js [config]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: ['@hey-api/client-nuxt'], // [!code ++]
};
```

```sh [cli]
npx @hey-api/openapi-ts \
  -i hey-api/backend \
  -o src/client \
  -c @hey-api/client-nuxt # [!code ++]
```

:::

::: tip

If you add `@hey-api/nuxt` to your Nuxt modules, this step is not needed.

:::

## Configuration

The Nuxt client is built as a thin wrapper on top of Nuxt, extending its functionality to work with Hey API. If you're already familiar with Nuxt, configuring your client will feel like working directly with Nuxt.

When we installed the client above, it created a [`client.gen.ts`](/openapi-ts/output#client) file. You will most likely want to configure the exported `client` instance. There are two ways to do that.

### `setConfig()`

This is the simpler approach. You can call the `setConfig()` method at the beginning of your application or anytime you need to update the client configuration. You can pass any Nuxt configuration option to `setConfig()`, and even your own [`$fetch`](#custom-instance) implementation.

```js
import { client } from 'client/client.gen';

client.setConfig({
  baseURL: 'https://example.com',
});
```

The disadvantage of this approach is that your code may call the `client` instance before it's configured for the first time. Depending on your use case, you might need to use the second approach.

### Runtime API

Since `client.gen.ts` is a generated file, we can't directly modify it. Instead, we can tell our configuration to use a custom file implementing the Runtime API. We do that by specifying the `runtimeConfigPath` option.

```js
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    {
      name: '@hey-api/client-nuxt',
      runtimeConfigPath: './src/hey-api.ts', // [!code ++]
    },
  ],
};
```

In our custom file, we need to export a `createClientConfig()` method. This function is a simple wrapper allowing us to override configuration values.

::: code-group

```ts [hey-api.ts]
import type { CreateClientConfig } from './client/client.gen';

export const createClientConfig: CreateClientConfig = (config) => ({
  ...config,
  baseURL: 'https://example.com',
});
```

:::

With this approach, `client.gen.ts` will call `createClientConfig()` before initializing the `client` instance. If needed, you can still use `setConfig()` to update the client configuration later.

### `createClient()`

You can also create your own client instance. You can use it to manually send requests or point it to a different domain.

```js
import { createClient } from './client/client';

const myClient = createClient({
  baseURL: 'https://example.com',
});
```

You can also pass this instance to any SDK function through the `client` option. This will override the default instance from `client.gen.ts`.

```js
const response = await getFoo({
  client: myClient,
});
```

### SDKs

Alternatively, you can pass the client configuration options to each SDK function. This is useful if you don't want to create a client instance for one-off use cases.

```js
const response = await getFoo({
  baseURL: 'https://example.com', // <-- override default configuration
});
```

## Interceptors

Interceptors (middleware) can be used to modify requests before they're sent or responses before they're returned to your application. Nuxt provides interceptors through ofetch, please refer to their documentation on [$fetch](https://nuxt.com/docs/api/utils/dollarfetch).

You can pass any Nuxt/ofetch arguments to the client instance.

::: tip
If you omit `composable`, `$fetch` is used by default.
:::

```js
import { client } from 'client/client.gen';

const result = await client.get({
  composable: '$fetch',
  onRequest: (context) => {
    // do something
  },
  url: '/foo',
});
```

## Auth

The SDKs include auth mechanisms for every endpoint. You will want to configure the `auth` field to pass the right token for each request. The `auth` field can be a string or a function returning a string representing the token. The returned value will be attached only to requests that require auth.

```js
import { client } from 'client/client.gen';

client.setConfig({
  auth: () => '<my_token>', // [!code ++]
  baseURL: 'https://example.com',
});
```

If you're not using SDKs or generating auth, using interceptors is a common approach to configuring auth for each request.

```js
import { client } from 'client/client.gen';

client.setConfig({
  onRequest: ({ options }) => {
    options.headers.set('Authorization', 'Bearer <my_token>'); // [!code ++]
  },
});
```

## Build URL

If you need to access the compiled URL, you can use the `buildUrl()` method. It's loosely typed by default to accept almost any value; in practice, you will want to pass a type hint.

```ts
type FooData = {
  path: {
    fooId: number;
  };
  query?: {
    bar?: string;
  };
  url: '/foo/{fooId}';
};

const url = client.buildUrl<FooData>({
  path: {
    fooId: 1,
  },
  query: {
    bar: 'baz',
  },
  url: '/foo/{fooId}',
});
console.log(url); // prints '/foo/1?bar=baz'
```

## Custom Instance

You can provide a custom `$fetch` instance. This is useful if you need to extend the default instance with extra functionality, or replace it altogether.

```js
import { client } from 'client/client.gen';

client.setConfig({
  $fetch: () => {
    /* custom `$fetch` method */
  },
});
```

You can use any of the approaches mentioned in [Configuration](#configuration), depending on how granular you want your custom instance to be.

## API

You can view the complete list of options in the [UserConfig](https://github.com/hey-api/openapi-ts/blob/main/packages/openapi-ts/src/plugins/@hey-api/client-nuxt/types.d.ts) interface.

## Examples

You can view live examples on [StackBlitz](https://stackblitz.com/orgs/github/hey-api/collections/openapi-ts-examples).

## Sponsors

Hey API is sponsor-funded. If you rely on Hey API in production, consider becoming a [sponsor](https://github.com/sponsors/hey-api) to accelerate the roadmap.

---

---
url: /openapi-ts/clients/ofetch.md
description: >-
  Generate a type-safe ofetch client from OpenAPI with the ofetch client for
  openapi-ts. Fully compatible with validators, transformers, and all core
  features.
---

# OFetch

### About

[`ofetch`](https://github.com/unjs/ofetch) is a better Fetch API that adds useful defaults and features such as automatic response parsing, request/response hooks, and it works in Node, browser, and workers.

The `ofetch` client for Hey API generates a type-safe client from your OpenAPI spec, fully compatible with validators, transformers, and all core features.

### Collaborators

## Features

* seamless integration with `@hey-api/openapi-ts` ecosystem
* type-safe response data and errors
* response data validation and transformation
* access to the original request and response
* granular request and response customization options
* minimal learning curve thanks to extending the underlying technology
* support bundling inside the generated output

## Installation

In your [configuration](/openapi-ts/get-started), add `@hey-api/client-ofetch` to your plugins and you'll be ready to generate client artifacts. :tada:

::: code-group

```js [config]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: ['@hey-api/client-ofetch'], // [!code ++]
};
```

```sh [cli]
npx @hey-api/openapi-ts \
  -i hey-api/backend \
  -o src/client \
  -c @hey-api/client-ofetch # [!code ++]
```

:::

## Configuration

The `ofetch` client is built as a thin wrapper on top of `ofetch`, extending its functionality to work with Hey API. If you're already familiar with `ofetch`, configuring your client will feel like working directly with `ofetch`.

When we installed the client above, it created a [`client.gen.ts`](/openapi-ts/output#client) file. You will most likely want to configure the exported `client` instance. There are two ways to do that.

### `setConfig()`

This is the simpler approach. You can call the `setConfig()` method at the beginning of your application or anytime you need to update the client configuration. You can pass any `ofetch` configuration option to `setConfig()`, and even your own [`ofetch`](#custom-instance) instance.

```js
import { client } from 'client/client.gen';

client.setConfig({
  baseUrl: 'https://example.com',
});
```

The disadvantage of this approach is that your code may call the `client` instance before it's configured for the first time. Depending on your use case, you might need to use the second approach.

### Runtime API

Since `client.gen.ts` is a generated file, we can't directly modify it. Instead, we can tell our configuration to use a custom file implementing the Runtime API. We do that by specifying the `runtimeConfigPath` option.

```js
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    {
      name: '@hey-api/client-ofetch',
      runtimeConfigPath: './src/hey-api.ts', // [!code ++]
    },
  ],
};
```

In our custom file, we need to export a `createClientConfig()` method. This function is a simple wrapper allowing us to override configuration values.

::: code-group

```ts [hey-api.ts]
import type { CreateClientConfig } from './client/client.gen';

export const createClientConfig: CreateClientConfig = (config) => ({
  ...config,
  baseUrl: 'https://example.com',
});
```

:::

With this approach, `client.gen.ts` will call `createClientConfig()` before initializing the `client` instance. If needed, you can still use `setConfig()` to update the client configuration later.

### `createClient()`

You can also create your own client instance. You can use it to manually send requests or point it to a different domain.

```js
import { createClient } from './client/client';

const myClient = createClient({
  baseUrl: 'https://example.com',
});
```

You can also pass this instance to any SDK function through the `client` option. This will override the default instance from `client.gen.ts`.

```js
const response = await getFoo({
  client: myClient,
});
```

### SDKs

Alternatively, you can pass the client configuration options to each SDK function. This is useful if you don't want to create a client instance for one-off use cases.

```js
const response = await getFoo({
  baseUrl: 'https://example.com', // <-- override default configuration
});
```

## Interceptors

Interceptors (middleware) can be used to modify requests before they're sent or responses before they're returned to your application.

The `ofetch` client supports two complementary options:

* built-in Hey API interceptors exposed via `client.interceptors`
* native `ofetch` hooks passed through config (e.g. `onRequest`)

### Example: Request interceptor

::: code-group

```js [use]
import { client } from 'client/client.gen';

async function myInterceptor(request) {
  // do something
  return request;
}

interceptorId = client.interceptors.request.use(myInterceptor);
```

```js [eject]
import { client } from 'client/client.gen';

// eject by ID
client.interceptors.request.eject(interceptorId);

// eject by reference
client.interceptors.request.eject(myInterceptor);
```

```js [update]
import { client } from 'client/client.gen';

async function myNewInterceptor(request) {
  // do something
  return request;
}

// update by ID
client.interceptors.request.update(interceptorId, myNewInterceptor);

// update by reference
client.interceptors.request.update(myInterceptor, myNewInterceptor);
```

:::

### Example: Response interceptor

::: code-group

```js [use]
import { client } from 'client/client.gen';

async function myInterceptor(response) {
  // do something
  return response;
}

interceptorId = client.interceptors.response.use(myInterceptor);
```

```js [eject]
import { client } from 'client/client.gen';

// eject by ID
client.interceptors.response.eject(interceptorId);

// eject by reference
client.interceptors.response.eject(myInterceptor);
```

```js [update]
import { client } from 'client/client.gen';

async function myNewInterceptor(response) {
  // do something
  return response;
}

// update interceptor by interceptor ID
client.interceptors.response.update(interceptorId, myNewInterceptor);

// update interceptor by reference to interceptor function
client.interceptors.response.update(myInterceptor, myNewInterceptor);
```

:::

::: tip
To eject, you must provide the ID or reference of the interceptor passed to `use()`, the ID is the value returned by `use()` and `update()`.
:::

### Example: `ofetch` hooks

```js
import { client } from 'client/client.gen';

client.setConfig({
  onRequest: ({ options }) => {
    // mutate ofetch options (headers, query, etc.)
  },
  onResponse: ({ response }) => {
    // inspect/transform the raw Response
  },
  onRequestError: (ctx) => {
    // handle request errors
  },
  onResponseError: (ctx) => {
    // handle response errors
  },
});
```

## Auth

The SDKs include auth mechanisms for every endpoint. You will want to configure the `auth` field to pass the right token for each request. The `auth` field can be a string or a function returning a string representing the token. The returned value will be attached only to requests that require auth.

```js
import { client } from 'client/client.gen';

client.setConfig({
  auth: () => '<my_token>', // [!code ++]
  baseUrl: 'https://example.com',
});
```

If you're not using SDKs or generating auth, using interceptors is a common approach to configuring auth for each request.

```js
import { client } from 'client/client.gen';

client.interceptors.request.use((request, options) => {
  request.headers.set('Authorization', 'Bearer <my_token>'); // [!code ++]
  return request;
});
```

You can also use the `ofetch` hooks.

```js
import { client } from 'client/client.gen';

client.setConfig({
  onRequest: ({ options }) => {
    options.headers.set('Authorization', 'Bearer <my_token>'); // [!code ++]
  },
});
```

## Build URL

If you need to access the compiled URL, you can use the `buildUrl()` method. It's loosely typed by default to accept almost any value; in practice, you will want to pass a type hint.

```ts
type FooData = {
  path: {
    fooId: number;
  };
  query?: {
    bar?: string;
  };
  url: '/foo/{fooId}';
};

const url = client.buildUrl<FooData>({
  path: {
    fooId: 1,
  },
  query: {
    bar: 'baz',
  },
  url: '/foo/{fooId}',
});
console.log(url); // prints '/foo/1?bar=baz'
```

## Custom Instance

You can provide a custom `ofetch` instance. This is useful if you need to extend the default instance with extra functionality, or replace it altogether.

```js
import { ofetch } from 'ofetch';
import { client } from 'client/client.gen';

const customOFetchInstance = ofetch.create({
  onRequest: ({ options }) => {
    // customize request
  },
  onResponse: ({ response }) => {
    // customize response
  },
});

client.setConfig({
  ofetch: customOFetchInstance,
});
```

You can use any of the approaches mentioned in [Configuration](#configuration), depending on how granular you want your custom instance to be.

## API

You can view the complete list of options in the [UserConfig](https://github.com/hey-api/openapi-ts/blob/main/packages/openapi-ts/src/plugins/@hey-api/client-ofetch/types.d.ts) interface.

## Examples

You can view live examples on [StackBlitz](https://stackblitz.com/orgs/github/hey-api/collections/openapi-ts-examples).

## Sponsors

Hey API is sponsor-funded. If you rely on Hey API in production, consider becoming a [sponsor](https://github.com/sponsors/hey-api) to accelerate the roadmap.

---

---
url: /openapi-ts/configuration/output.md
description: Configure @hey-api/openapi-ts.
---

# Output

You must set the output so we know where to generate your files.

## Output

Output can be a path to the destination folder or an object containing the destination folder path and optional settings.

::: code-group

```js [path]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client', // [!code ++]
};
```

```js [object]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: { // [!code ++]
    path: 'src/client', // [!code ++]
    // ...other options // [!code ++]
  }, // [!code ++]
};
```

:::

You can learn more about complex use cases in the [Advanced](/openapi-ts/configuration#advanced) section.

## File Name

You can customize the naming and casing pattern for files using the `fileName` option.

::: code-group

```js [default]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: {
    fileName: '{{name}}', // [!code ++]
    path: 'src/client',
  },
};
```

```js [snake_case]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: {
    fileName: {
      case: 'snake_case', // [!code ++]
    },
    path: 'src/client',
  },
};
```

:::

By default, we append every file name with a `.gen` suffix to highlight it's automatically generated. You can customize or disable this suffix using the `fileName.suffix` option.

::: code-group

```js [default]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: {
    fileName: {
      suffix: '.gen', // [!code ++]
    },
    path: 'src/client',
  },
};
```

```js [disabled]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: {
    fileName: {
      suffix: null, // [!code ++]
    },
    path: 'src/client',
  },
};
```

```js [custom]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: {
    fileName: {
      suffix: '.generated', // [!code ++]
    },
    path: 'src/client',
  },
};
```

:::

## Module Extension

You can customize the extension used for TypeScript modules.

::: code-group

```js [default]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: {
    importFileExtension: undefined, // [!code ++]
    path: 'src/client',
  },
};
```

```js [disabled]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: {
    importFileExtension: null, // [!code ++]
    path: 'src/client',
  },
};
```

```js [js]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: {
    importFileExtension: '.js', // [!code ++]
    path: 'src/client',
  },
};
```

```js [ts]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: {
    importFileExtension: '.ts', // [!code ++]
    path: 'src/client',
  },
};
```

:::

By default, we don't add a file extension and let the runtime resolve it.

```js
import foo from './foo';
```

If we detect a [TSConfig file](#tsconfig-path) with `moduleResolution` option set to `nodenext`, we default the extension to `.js`.

```js
import foo from './foo.js';
```

## Source

Source is a copy of the input specification used to generate your output. It can be used to power documentation tools or to persist a stable snapshot alongside your generated files.

Enabling the `source` option with `true` creates a `source.json` file in your output folder.

```js
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: {
    path: 'src/client',
    source: true, // [!code ++]
  },
};
```

You can customize the file name and location using `fileName` and `path`. For example, this configuration will create an `openapi.json` file inside `src/client/source` directory.

```js
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: {
    path: 'src/client',
    source: {
      fileName: 'openapi', // [!code ++]
      path: './source', // [!code ++]
    },
  },
};
```

To use the source without writing it to disk, you can provide a `callback` function. This is useful for logging or integrating with external systems.

```js
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: {
    path: 'src/client',
    source: {
      callback: (source) => console.log(source), // [!code ++]
      path: null, // [!code ++]
    },
  },
};
```

## Format

To format your output folder contents, set `format` to a valid formatter.

::: code-group

```js [disabled]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: {
    format: null, // [!code ++]
    path: 'src/client',
  },
};
```

```js [prettier]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: {
    format: 'prettier', // [!code ++]
    path: 'src/client',
  },
};
```

```js [biome]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: {
    format: 'biome', // [!code ++]
    path: 'src/client',
  },
};
```

:::

You can also prevent your output from being formatted by adding your output path to the formatter's ignore file.

## Lint

To lint your output folder contents, set `lint` to a valid linter.

::: code-group

```js [disabled]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: {
    lint: null, // [!code ++]
    path: 'src/client',
  },
};
```

```js [eslint]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: {
    lint: 'eslint', // [!code ++]
    path: 'src/client',
  },
};
```

```js [biome]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: {
    lint: 'biome', // [!code ++]
    path: 'src/client',
  },
};
```

```js [oxlint]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: {
    lint: 'oxlint', // [!code ++]
    path: 'src/client',
  },
};
```

:::

You can also prevent your output from being linted by adding your output path to the linter's ignore file.

## Name Conflicts

As your project grows, the chances of name conflicts increase. We use a simple conflict resolver that appends numeric suffixes to duplicate identifiers. If you prefer a different strategy, you can provide your own `nameConflictResolver` function.

::: code-group

```js [config]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: {
    nameConflictResolver({ attempt, baseName }) { // [!code ++]
      return attempt === 0 ? baseName : `${baseName}_N${attempt + 1}`; // [!code ++]
    }, // [!code ++]
    path: 'src/client',
  },
};
```

```ts [example]
export type ChatCompletion = string;

export type ChatCompletion_N2 = number;
```

:::

## File Header

The generated output includes a notice in every file warning that any modifications will be lost when the files are regenerated. You can customize or disable this notice using the `header` option.

::: code-group

```js [config]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: {
    header: [
      '/* eslint-disable */', // [!code ++]
      '// This file is auto-generated by @hey-api/openapi-ts', // [!code ++]
    ],
    path: 'src/client',
  },
};
```

```ts [example]
/* eslint-disable */
// This file is auto-generated by @hey-api/openapi-ts

/** ... */
```

:::

## TSConfig Path

We use the [TSConfig file](https://www.typescriptlang.org/tsconfig/) to generate output matching your project's settings. By default, we attempt to find a TSConfig file starting from the location of the `@hey-api/openapi-ts` configuration file and traversing up.

::: code-group

```js [default]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: {
    path: 'src/client',
    tsConfigPath: undefined, // [!code ++]
  },
};
```

```js [custom]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: {
    path: 'src/client',
    tsConfigPath: './config/tsconfig.custom.json', // [!code ++]
  },
};
```

```js [disabled]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: {
    path: 'src/client',
    tsConfigPath: null, // [!code ++]
  },
};
```

:::

## Custom Files

By default, you can't keep custom files in the `path` folder because it's emptied on every run. If you're sure you need to disable this behavior, set `clean` to `false`.

```js
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: {
    clean: false, // [!code ++]
    path: 'src/client',
  },
};
```

::: warning
Setting `clean` to `false` may result in broken output. Ensure you typecheck your code.
:::

## Examples

You can view live examples on [StackBlitz](https://stackblitz.com/orgs/github/hey-api/collections/openapi-ts-examples).

## Sponsors

Hey API is sponsor-funded. If you rely on Hey API in production, consider becoming a [sponsor](https://github.com/sponsors/hey-api) to accelerate the roadmap.

---

---
url: /openapi-ts/output.md
description: Learn about files generated with @hey-api/openapi-ts.
---

# Output

Every generated file in your output folder is created by a plugin. This page describes the default output, but similar logic applies to all plugins.

## Overview

If you use the default configuration, your [project](https://stackblitz.com/edit/hey-api-example?file=openapi-ts.config.ts,src%2Fclient%2Fschemas.gen.ts,src%2Fclient%2Fsdk.gen.ts,src%2Fclient%2Ftypes.gen.ts) might look like this.

```txt
my-app/
├── node_modules/
├── src/
│ ├── client/
│ │ ├── client/
│ │ ├── core/
│ │ ├── client.gen.ts
│ │ ├── index.ts
│ │ ├── sdk.gen.ts
│ │ └── types.gen.ts
│ └── index.ts
└── package.json
```

Your actual output depends on your Hey API configuration. It may contain a different number of files and their contents might differ.

Let's go through each file in the `src/client` folder and explain what it looks like, what it does, and how to use it.

## Client

`client.gen.ts` is generated by [client plugins](/openapi-ts/clients). If you choose to generate SDKs (enabled by default), we use the Fetch client unless specified otherwise.

::: code-group

```ts [client.gen.ts]
import { createClient, createConfig } from './client';

export const client = createClient(createConfig());
```

:::

The contents of this file are consumed by SDKs, but you can also import `client` in your application to perform additional configuration or send manual requests.

### Bundle

Client plugins provide their bundles inside `client` and `core` folders. The contents of these folders don't depend on the provided input. Everything inside these folders serves as a scaffolding so the generated code can make HTTP requests.

## TypeScript

You can learn more on the [TypeScript](/openapi-ts/plugins/typescript) page.

## SDK

You can learn more on the [SDK](/openapi-ts/plugins/sdk) page.

## Barrel File

`index.ts` is not generated by any specific plugin. It's meant for convenience and by default, it re-exports every artifact generated by default plugins (TypeScript and SDK).

::: code-group

```ts [index.ts]
export * from './sdk.gen';
export * from './types.gen';
```

:::

### Disable index file

We recommend importing artifacts from their respective files to avoid ambiguity, but we leave this choice up to you.

```ts
import type { Pet } from './client';
// or
import type { Pet } from './client/types.gen';
```

If you're not importing artifacts from the index file, you can skip generating it altogether by setting the `output.indexFile` option to `false`.

```js
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: {
    indexFile: false, // [!code ++]
    path: 'src/client',
  },
};
```

### Re-export more files

You can choose which files should be re-exported by setting the `exportFromIndex` option to `true` on any plugin. For example, here's how you would re-export [Zod](/openapi-ts/plugins/zod) plugin exports.

```js
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    // ...other plugins
    {
      exportFromIndex: true, // [!code ++]
      name: 'zod',
    },
  ],
};
```

## Examples

You can view live examples on [StackBlitz](https://stackblitz.com/orgs/github/hey-api/collections/openapi-ts-examples).

## Sponsors

Hey API is sponsor-funded. If you rely on Hey API in production, consider becoming a [sponsor](https://github.com/sponsors/hey-api) to accelerate the roadmap.

---

---
url: /openapi-ts/configuration/parser.md
description: Configure @hey-api/openapi-ts.
---

# Parser

We parse your input before making it available to plugins. Configuring the parser is optional, but it provides an ideal opportunity to modify or validate your input as needed.

## Patch

Sometimes you need to modify raw input before it's processed further. A common use case is fixing an invalid specification or adding a missing field. For this reason, custom patches are applied before any parsing takes place.

You can add custom patches with `patch`.

```js
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  parser: {
    patch: {
      schemas: {
        Foo: (schema) => { // [!code ++]
          // convert date-time format to timestamp // [!code ++]
          delete schema.properties.updatedAt.format; // [!code ++]
          schema.properties.updatedAt.type = 'number'; // [!code ++]
        }, // [!code ++]
        Bar: (schema) => { // [!code ++]
          // add missing property // [!code ++]
          schema.properties.meta = { // [!code ++]
            additionalProperties: true, // [!code ++]
            type: 'object', // [!code ++]
          }; // [!code ++]
          schema.required = ['meta']; // [!code ++]
        }, // [!code ++]
        Baz: (schema) => { // [!code ++]
          // remove property // [!code ++]
          delete schema.properties.internalField; // [!code ++]
        }, // [!code ++]
      },
    },
  },
};
```

## Validate

::: warning
The validator feature is very limited. You can help improve it by submitting more [use cases](https://github.com/hey-api/openapi-ts/issues/1970#issuecomment-2933189789).
:::

If you don't control or trust your input, you might want to validate it. Any detected errors in your input will exit `@hey-api/openapi-ts` and no plugins will be executed.

To validate your input, set `validate_EXPERIMENTAL` to `true`.

```js
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  parser: {
    validate_EXPERIMENTAL: true, // [!code ++]
  },
};
```

## Filters

Filters allow you to trim your input before it's processed further, so your output contains only relevant resources.

### Operations

Set `include` to match operations to be included or `exclude` to match operations to be excluded. Both exact keys and regular expressions are supported. When both rules match the same operation, `exclude` takes precedence over `include`.

::: code-group

```js [include]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  parser: {
    filters: {
      operations: {
        include: ['GET /api/v1/foo', '/^[A-Z]+ /api/v1//'], // [!code ++]
      },
    },
  },
};
```

```js [exclude]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  parser: {
    filters: {
      operations: {
        exclude: ['GET /api/v1/foo', '/^[A-Z]+ /api/v1//'], // [!code ++]
      },
    },
  },
};
```

:::

### Tags

Set `include` to match tags to be included or `exclude` to match tags to be excluded. When both rules match the same tag, `exclude` takes precedence over `include`.

::: code-group

```js [include]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  parser: {
    filters: {
      tags: {
        include: ['v2'], // [!code ++]
      },
    },
  },
};
```

```js [exclude]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  parser: {
    filters: {
      tags: {
        exclude: ['v1'], // [!code ++]
      },
    },
  },
};
```

:::

### Deprecated

You can filter out deprecated resources by setting `deprecated` to `false`.

```js
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  parser: {
    filters: {
      deprecated: false, // [!code ++]
    },
  },
};
```

### Schemas

Set `include` to match schemas to be included or `exclude` to match schemas to be excluded. Both exact keys and regular expressions are supported. When both rules match the same schema, `exclude` takes precedence over `include`.

::: code-group

```js [include]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  parser: {
    filters: {
      schemas: {
        include: ['Foo', '/^Bar/'], // [!code ++]
      },
    },
  },
};
```

```js [exclude]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  parser: {
    filters: {
      schemas: {
        exclude: ['Foo', '/^Bar/'], // [!code ++]
      },
    },
  },
};
```

:::

### Parameters

Set `include` to match parameters to be included or `exclude` to match parameters to be excluded. Both exact keys and regular expressions are supported. When both rules match the same parameter, `exclude` takes precedence over `include`.

::: code-group

```js [include]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  parser: {
    filters: {
      parameters: {
        include: ['QueryParameter', '/^MyQueryParameter/'], // [!code ++]
      },
    },
  },
};
```

```js [exclude]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  parser: {
    filters: {
      parameters: {
        exclude: ['QueryParameter', '/^MyQueryParameter/'], // [!code ++]
      },
    },
  },
};
```

:::

### Request Bodies

Set `include` to match request bodies to be included or `exclude` to match request bodies to be excluded. Both exact keys and regular expressions are supported. When both rules match the same request body, `exclude` takes precedence over `include`.

::: code-group

```js [include]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  parser: {
    filters: {
      requestBodies: {
        include: ['Payload', '/^SpecialPayload/'], // [!code ++]
      },
    },
  },
};
```

```js [exclude]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  parser: {
    filters: {
      requestBodies: {
        exclude: ['Payload', '/^SpecialPayload/'], // [!code ++]
      },
    },
  },
};
```

:::

### Responses

Set `include` to match responses to be included or `exclude` to match responses to be excluded. Both exact keys and regular expressions are supported. When both rules match the same response, `exclude` takes precedence over `include`.

::: code-group

```js [include]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  parser: {
    filters: {
      responses: {
        include: ['Foo', '/^Bar/'], // [!code ++]
      },
    },
  },
};
```

```js [exclude]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  parser: {
    filters: {
      responses: {
        exclude: ['Foo', '/^Bar/'], // [!code ++]
      },
    },
  },
};
```

:::

### Orphaned resources

If you only want to exclude orphaned resources, set `orphans` to `false`. This is the default value when combined with any other filters. If this isn't the desired behavior, you may want to set `orphans` to `true` to always preserve unused resources.

```js
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  parser: {
    filters: {
      orphans: false, // [!code ++]
    },
  },
};
```

### Order

For performance reasons, we don't preserve the original order when filtering out resources. If maintaining the original order is important to you, set `preserveOrder` to `true`.

```js
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  parser: {
    filters: {
      preserveOrder: true, // [!code ++]
    },
  },
};
```

## Transforms

You can think of transforms as deterministic [patches](#patch). They provide an easy way to apply the most commonly used input transformations.

### Enums

Your input might contain two types of enums:

* enums defined as reusable components (root enums)
* non-reusable enums nested within other schemas (inline enums)

You may want all enums to be reusable. This is because only root enums are typically exported by plugins. Inline enums will never be directly importable since they're nested inside other schemas.

::: code-group

```js [root]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  parser: {
    transforms: {
      enums: 'root', // [!code ++]
    },
  },
};
```

```js [inline]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  parser: {
    transforms: {
      enums: 'inline', // [!code ++]
    },
  },
};
```

:::

You can customize the naming and casing pattern for `enums` schemas using the `.name` and `.case` options.

### Properties required by default

By default, any object schema with a missing `required` keyword is interpreted as "no properties are required." This is the correct behavior according to the OpenAPI standard. However, some specifications interpret a missing `required` keyword as "all properties should be required."

This option allows you to change the default behavior so that properties are required by default unless explicitly marked as optional.

::: code-group

```js [default]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  parser: {
    transforms: {
      propertiesRequiredByDefault: false, // [!code ++]
    },
  },
};
```

```js [required]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  parser: {
    transforms: {
      propertiesRequiredByDefault: true, // [!code ++]
    },
  },
};
```

:::

### Read-write

Your schemas might contain read-only or write-only fields. Using such schemas directly could mean asking the user to provide a read-only field in requests, or expecting a write-only field in responses. We separate schemas for requests and responses if direct usage would result in such scenarios.

::: code-group

```js [default]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  parser: {
    transforms: {
      readWrite: {
        requests: '{{name}}Writable', // [!code ++]
        responses: '{{name}}', // [!code ++]
      },
    },
  },
};
```

```js [disabled]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  parser: {
    transforms: {
      readWrite: false, // [!code ++]
    },
  },
};
```

:::

You can customize the naming and casing pattern for `requests` and `responses` schemas using the `.name` and `.case` options.

## Pagination

Paginated operations are detected by having a pagination keyword in its parameters or request body. By default, we consider the following to be pagination keywords: `after`, `before`, `cursor`, `offset`, `page`, and `start`.

You can provide custom pagination keywords using `pagination.keywords`.

::: code-group

```js [extend]
import { defaultPaginationKeywords } from '@hey-api/openapi-ts';

export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  parser: {
    pagination: {
      keywords: [
        ...defaultPaginationKeywords, // [!code ++]
        'extra', // [!code ++]
        'pagination', // [!code ++]
        'keywords', // [!code ++]
      ],
    },
  },
};
```

```js [override]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  parser: {
    pagination: {
      keywords: [
        'custom', // [!code ++]
        'pagination', // [!code ++]
        'keywords', // [!code ++]
      ],
    },
  },
};
```

:::

## Hooks

Hooks affect runtime behavior but aren't tied to any single plugin. They can be configured globally via `hooks` or per plugin through the `~hooks` property.

::: code-group

```js [parser]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  parser: {
    hooks: {}, // configure global hooks here // [!code ++]
  },
};
```

```js [plugin]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    {
      name: '@tanstack/react-query',
      '~hooks': {}, // configure plugin hooks here // [!code ++]
    },
  ],
};
```

:::

We always use the first hook that returns a value. If a hook returns no value, we fall back to less specific hooks until one does.

### Operations {#hooks-operations}

Each operation has a list of classifiers that can include `query`, `mutation`, both, or none. Plugins may use these values to decide whether to generate specific output. For example, you usually don't want to generate [TanStack Query options](/openapi-ts/plugins/tanstack-query#queries) for PATCH operations.

#### Query operations {#hooks-query-operations}

By default, GET operations are classified as `query` operations.

#### Mutation operations {#hooks-mutation-operations}

By default, DELETE, PATCH, POST, and PUT operations are classified as `mutation` operations.

#### Example: POST search query

Imagine your API has a POST `/search` endpoint that accepts a large payload. By default, it's classified as a `mutation`, but in practice it behaves like a `query`, and your [state management](/openapi-ts/state-management) plugin should generate query hooks.

You can achieve this by classifying the operation as `query` in a matcher.

::: code-group

```js [isQuery]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  parser: {
    hooks: {
      operations: {
        isQuery: (op) => {
          if (op.method === 'post' && op.path === '/search') { // [!code ++]
            return true; // [!code ++]
          } // [!code ++]
        },
      },
    },
  },
};
```

```js [getKind]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  parser: {
    hooks: {
      operations: {
        getKind: (op) => {
          if (op.method === 'post' && op.path === '/search') { // [!code ++]
            return ['query']; // [!code ++]
          } // [!code ++]
        },
      },
    },
  },
};
```

:::

### Symbols {#hooks-symbols}

Each symbol can have a placement function deciding its output location.

#### Example: Alphabetic sort

While we work on a better example, let's imagine a world where it's desirable to place every symbol in a file named after its initial letter. For example, a function named `Foo` should end up in the file `f.ts`.

You can achieve this by using the symbol's name.

```js [getKind]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  parser: {
    hooks: {
      symbols: {
        getFilePath: (symbol) => {
          if (symbol.name) { // [!code ++]
            return symbol.name[0]?.toLowerCase(); // [!code ++]
          } // [!code ++]
        },
      },
    },
  },
};
```

## Examples

You can view live examples on [StackBlitz](https://stackblitz.com/orgs/github/hey-api/collections/openapi-ts-examples).

## Sponsors

Hey API is sponsor-funded. If you rely on Hey API in production, consider becoming a [sponsor](https://github.com/sponsors/hey-api) to accelerate the roadmap.

---

---
url: /openapi-ts/plugins/pinia-colada.md
description: >-
  Generate Pinia Colada v0 functions and query keys from OpenAPI with the Pinia
  Colada plugin for openapi-ts. Fully compatible with validators, transformers,
  and all core features.
---

### About

[Pinia Colada](https://pinia-colada.esm.dev) is the perfect companion to Pinia to handle async state management in your Vue applications.

The Pinia Colada plugin for Hey API generates functions and query keys from your OpenAPI spec, fully compatible with SDKs, transformers, and all core features.

### Collaborators

## Features

* Pinia Colada v0 support
* seamless integration with `@hey-api/openapi-ts` ecosystem
* create query keys following the best practices
* type-safe query options and mutation options
* minimal learning curve thanks to extending the underlying technology

## Installation

In your [configuration](/openapi-ts/get-started), add `@pinia/colada` to your plugins and you'll be ready to generate Pinia Colada artifacts. :tada:

```js
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    // ...other plugins
    '@pinia/colada', // [!code ++]
  ],
};
```

::: tip
When using this plugin in a Nuxt app, prefer the [ofetch client](/openapi-ts/clients/ofetch) for universal compatibility.

The [nuxt client](/openapi-ts/clients/nuxt) is tailored for working directly with Nuxt composables (`$fetch` / `useFetch` / `useAsyncData`) and is not intended as a universal HTTP client for libraries like `@pinia/colada`.
:::

## Output

The Pinia Colada plugin will generate the following artifacts, depending on the input specification.

## Queries

Queries are generated from [query operations](/openapi-ts/configuration/parser#hooks-query-operations). The generated query functions follow the naming convention of SDK functions and by default append `Query`, e.g. `getPetByIdQuery()`.

::: code-group

```ts [example]
const query = useQuery(getPetByIdQuery, () => ({
  path: {
    petId: 1,
  },
}));
```

```js [config]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    // ...other plugins
    {
      name: '@pinia/colada',
      queryOptions: true, // [!code ++]
    },
  ],
};
```

:::

You can customize the naming and casing pattern for `queryOptions` functions using the `.name` and `.case` options.

## Query Keys

Query keys contain normalized SDK function parameters and additional metadata.

::: code-group

```ts [example]
const queryKey = [
  {
    _id: 'getPetById',
    baseUrl: 'https://app.heyapi.dev',
    path: {
      petId: 1,
    },
  },
];
```

```js [config]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    // ...other plugins
    {
      name: '@pinia/colada',
      queryKeys: true, // [!code ++]
    },
  ],
};
```

:::

### Tags

You can include operation tags in your query keys by setting `tags` to `true`. This will make query keys larger but provides better cache invalidation capabilities.

::: code-group

```ts [example]
const key = [
  {
    _id: 'getPetById',
    baseUrl: 'https://app.heyapi.dev',
    path: {
      petId: 1,
    },
    tags: ['pets', 'one', 'get'], // [!code ++]
  },
];
```

```js [config]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    // ...other plugins
    {
      name: '@pinia/colada',
      queryKeys: {
        tags: true, // [!code ++]
      },
    },
  ],
};
```

:::

### Accessing Query Keys

If you have access to the result of query options function, you can get the query key from the `key` field.

::: code-group

```ts [example]
const { key } = getPetByIdQuery({
  path: {
    petId: 1,
  },
});
```

```js [config]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    // ...other plugins
    {
      name: '@pinia/colada',
      queryOptions: true, // [!code ++]
    },
  ],
};
```

:::

Alternatively, you can access the same query key by calling query key functions. The generated query key functions follow the naming convention of SDK functions and by default append `QueryKey`, e.g. `getPetByIdQueryKey()`.

::: code-group

```ts [example]
const key = getPetByIdQueryKey({
  path: {
    petId: 1,
  },
});
```

```js [config]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    // ...other plugins
    {
      name: '@pinia/colada',
      queryKeys: true, // [!code ++]
    },
  ],
};
```

:::

You can customize the naming and casing pattern for `queryKeys` functions using the `.name` and `.case` options.

## Mutations

Mutations are generated from [mutation operations](/openapi-ts/configuration/parser#hooks-mutation-operations). The generated mutation functions follow the naming convention of SDK functions and by default append `Mutation`, e.g. `addPetMutation()`.

::: code-group

```ts [example]
const addPet = useMutation({
  ...addPetMutation(),
  onError: (error) => {
    console.log(error);
  },
});

addPet.mutate({
  body: {
    name: 'Kitty',
  },
});
```

```js [config]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    // ...other plugins
    {
      name: '@pinia/colada',
      mutationOptions: true, // [!code ++]
    },
  ],
};
```

:::

You can customize the naming and casing pattern for `mutationOptions` functions using the `.name` and `.case` options.

## API

You can view the complete list of options in the [UserConfig](https://github.com/hey-api/openapi-ts/blob/main/packages/openapi-ts/src/plugins/@pinia/colada/types.d.ts) interface.

## Examples

You can view live examples on [StackBlitz](https://stackblitz.com/orgs/github/hey-api/collections/openapi-ts-examples).

## Sponsors

Hey API is sponsor-funded. If you rely on Hey API in production, consider becoming a [sponsor](https://github.com/sponsors/hey-api) to accelerate the roadmap.

---

---
url: /openapi-ts/plugins/concepts/resolvers.md
description: Understand the concepts behind plugins.
---

# Resolvers

Sometimes the default plugin behavior isn't what you need or expect. Resolvers let you patch plugins in a safe and performant way, without forking or reimplementing core logic.

Currently available for [Valibot](/openapi-ts/plugins/valibot) and [Zod](/openapi-ts/plugins/zod).

## Examples

This page demonstrates resolvers through a few common scenarios.

1. [Handle arbitrary schema formats](#example-1)
2. [Validate high precision numbers](#example-2)
3. [Replace default base](#example-3)

## Terminology

Before we look at examples, let's go through the resolvers API to help you understand how they work. Plugins that support resolvers expose them through the `~resolvers` option. Each resolver is a function that receives context and returns an implemented node (or patches existing ones).

The resolver context will usually contain:

* `$` - The node builder interface. Use it to build your custom logic.
* `nodes` - Parts of the plugin logic. You can use these to avoid reimplementing the functionality, or replace them with custom implementation.
* `plugin` - The plugin instance. You'll most likely use it to register new symbols.
* `symbols` - Frequently used symbols. These are effectively shorthands for commonly used `plugin.referenceSymbol()` calls.

Other fields may include the current schema or relevant utilities.

## Example 1

### Handle arbitrary schema formats

By default, the Valibot plugin may produce the following schemas for `date` and `date-time` strings.

```js
export const vDates = v.object({
  created: v.pipe(v.string(), v.isoDate()),
  modified: v.pipe(v.string(), v.isoTimestamp()),
});
```

We can override this behavior by patching the `nodes.format` function only for strings with `date` or `date-time` formats.

```js
{
  name: 'valibot',
  '~resolvers': {
    string(ctx) {
      const { $, schema, symbols } = ctx;
      const { v } = symbols;
      if (schema.format === 'date' || schema.format === 'date-time') {
        ctx.nodes.format = () => $(v).attr('isoDateTime').call();
      }
    }
  }
}
```

This applies custom logic with surgical precision, without affecting the rest of the default behavior.

::: code-group

```js [after]
export const vDates = v.object({
  created: v.pipe(v.string(), v.isoDateTime()),
  modified: v.pipe(v.string(), v.isoDateTime()),
});
```

```js [before]
export const vDates = v.object({
  created: v.pipe(v.string(), v.isoDate()),
  modified: v.pipe(v.string(), v.isoTimestamp()),
});
```

:::

## Example 2

### Validate high precision numbers

Let's say you're dealing with very large or unsafe numbers.

```js
export const vAmount = v.number();
```

In this case, you'll want to use a third-party library to validate your values. We can use big.js to validate all numbers by replacing the whole resolver.

```js
{
  name: 'valibot',
  '~resolvers': {
    number(ctx) {
      const { $, plugin, symbols } = ctx;
      const { v } = symbols;
      const big = plugin.symbolOnce('Big', {
        external: 'big.js',
        importKind: 'default',
      });
      return $(v).attr('instance').call(big);
    }
  }
}
```

We're calling `plugin.symbolOnce()` to ensure we always use the same symbol reference.

::: code-group

```js [after]
import Big from 'big.js';

export const vAmount = v.instance(Big);
```

```js [before]
export const vAmount = v.number();
```

:::

## Example 3

### Replace default base

You might want to replace the default base schema, e.g. `v.object()`.

```js
export const vUser = v.object({
  age: v.number(),
});
```

Let's say we want to interpret any schema without explicitly defined additional properties as a loose object.

```js
{
  name: 'valibot',
  '~resolvers': {
    object(ctx) {
      const { $, symbols } = ctx;
      const { v } = symbols;
      const additional = ctx.nodes.additionalProperties(ctx);
      if (additional === undefined) {
        const shape = ctx.nodes.shape(ctx);
        ctx.nodes.base = () => $(v).attr('looseObject').call(shape);
      }
    }
  }
}
```

Above we demonstrate patching a node based on the result of another node.

::: code-group

```js [after]
export const vUser = v.looseObject({
  age: v.number(),
});
```

```js [before]
export const vUser = v.object({
  age: v.number(),
});
```

:::

## Feedback

We welcome feedback on the Resolvers API. [Open a GitHub issue](https://github.com/hey-api/openapi-ts/issues) to request support for additional plugins.

## Sponsors

Hey API is sponsor-funded. If you rely on Hey API in production, consider becoming a [sponsor](https://github.com/sponsors/hey-api) to accelerate the roadmap.

---

---
url: /openapi-ts/plugins/sdk.md
description: >-
  Generate SDKs from OpenAPI with the SDK plugin for openapi-ts. Fully
  compatible with validators, transformers, and all core features.
---

# SDK

### About

The SDK plugin generates a high-level, ergonomic API layer on top of the low-level HTTP client.

It exposes typed functions or methods for each operation, with built-in auth handling, configurable request and response validation, and ready-to-use code examples.

## Features

* high-level SDK layer on top of the HTTP client
* typed functions or methods per operation
* built-in authentication handling
* request and response validation
* ready-to-use code examples

## Installation

In your [configuration](/openapi-ts/get-started), add `@hey-api/sdk` to your plugins and you'll be ready to generate SDK artifacts. :tada:

```js
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    // ...other plugins
    '@hey-api/sdk', // [!code ++]
  ],
};
```

## Output

The SDK plugin supports a wide range of configuration options. This guide focuses on two main SDK formats: tree-shakeable functions and instantiable classes, but you can apply the same concepts to create more advanced configurations.

## Flat

This is the default setting. Flat SDKs support tree-shaking, which can lead to a reduced bundle size. You select flat mode by setting `operations.strategy` to `flat`.

::: code-group

```ts [example]
import type { AddPetData } from './types.gen';

export const addPet = (options: Options<AddPetData>) => {
  /** ... */
};
```

```js [config]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    // ...other plugins
    {
      name: '@hey-api/sdk',
      operations: {
        strategy: 'flat', // [!code ++]
      },
    },
  ],
};
```

:::

## Instance

Class SDKs do not support tree-shaking, which results in a larger bundle size, but you may prefer their syntax. You select class mode by setting `operations.strategy` to `single`.

::: code-group

```ts [example]
import type { AddPetData } from './types.gen';

export class Sdk extends HeyApiClient {
  public addPet(options: Options<AddPetData>) {
    /** ... */
  }
}
```

```js [config]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    // ...other plugins
    {
      name: '@hey-api/sdk',
      operations: {
        strategy: 'single', // [!code ++]
      },
    },
  ],
};
```

:::

### Name

As shown above, by default our SDK class is called `Sdk`. The first thing you'll likely want to do is change this to your preferred name, which you can do using `operation.containerName`.

::: code-group

```ts [example]
import { client } from './client.gen';
import type { AddPetData, AddPetErrors, AddPetResponses } from './types.gen';

export class PetStore extends HeyApiClient { // [!code ++]
  /** ... */
}
```

```js [config]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    // ...other plugins
    {
      name: '@hey-api/sdk',
      operations: {
        containerName: 'PetStore', // [!code ++]
        strategy: 'single',
      },
    },
  ],
};
```

:::

### Structure

While we try to infer the SDK structure from `operationId` fields, you'll likely want to customize it further. You can do this using `operations.nesting`.

Similar to the `operations.strategy` option, we provide a few presets. However, you gain the most control by providing your own function.

To demonstrate the power of this feature, let's nest a few endpoints inside a `Pet` class and rename them. Our original `addPet()` method will now become `pet.add()`. Notice that we use the built-in `OperationPath.fromOperationId()` helper to handle the remaining operations.

::: code-group

```ts [example]
import { client } from './client.gen';
import type { AddPetData, AddPetErrors, AddPetResponses } from './types.gen';

export class Pet extends HeyApiClient {
  public add(options: Options<PostPetData>) { // [!code ++]
    /** ... */
  }
}

export class PetStore extends HeyApiClient {
  get pet(): Pet { // [!code ++]
    /** ... */
  }
}
```

```js [config]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    // ...other plugins
    {
      name: '@hey-api/sdk',
      operations: {
        containerName: 'PetStore',
        nesting(operation) {
          if (operation.path === '/pet/{petId}' || operation.path === '/pet') { // [!code ++]
            return ['pet', operation.operationId?.replace(/Pet/, '') // [!code ++]
              || operation.method.toLocaleLowerCase()]; // [!code ++]
          } // [!code ++]
          return OperationPath.fromOperationId()(operation); // [!code ++]
        },
        strategy: 'single',
      },
    },
  ],
};
```

:::

## Auth

Most APIs require some form of authentication, which is why the SDK plugin provides built-in auth mechanisms by default. All you need to do is return the data from the `auth()` function, and the SDK will handle serialization and encoding for you. There are several ways to do this, for example on the client instance.

::: code-group

```ts [example]
import { client } from './client.gen';

client.setConfig({
  auth() {
    return '<token>';
  },
});
```

```js [config]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    // ...other plugins
    {
      auth: true, // [!code ++]
      name: '@hey-api/sdk',
    },
  ],
};
```

:::

::: info
The SDK plugin currently supports only the `bearer` and `basic` auth schemes. [Open an issue](https://github.com/hey-api/openapi-ts/issues) if you'd like support for additional mechanisms.
:::

## Validators

Validating data at runtime comes with a performance cost, which is why it's not enabled by default. To enable validation, set `validator` to `zod` or one of the available [validator plugins](/openapi-ts/validators). This will implicitly add the selected plugin with default values.

For a more granular approach, manually add a validator plugin and set `validator` to the plugin name or `true` to automatically select a compatible plugin. Until you customize the validator plugin, both approaches will produce the same default output.

::: code-group

```ts [example]
import * as v from 'valibot';

export const addPet = (options: Options<AddPetData>) =>
  (options.client ?? client).post<AddPetResponses, AddPetErrors>({
    requestValidator: async (data) => // [!code ++]
      await v.parseAsync(vAddPetData, data), // [!code ++]
    responseValidator: async (data) => // [!code ++]
      await v.parseAsync(vAddPetResponse, data), // [!code ++]
    /** ... */
  });
```

```js [config]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    // ...other plugins
    {
      name: '@hey-api/sdk',
      validator: true, // or 'valibot' // [!code ++]
    },
    {
      name: 'valibot', // customize (optional) // [!code ++]
      // other options
    },
  ],
};
```

:::

You can choose to validate only requests or responses.

::: code-group

```js [requests]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    // ...other plugins
    {
      name: '@hey-api/sdk',
      validator: {
        request: 'zod', // [!code ++]
      },
    },
  ],
};
```

```js [responses]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    // ...other plugins
    {
      name: '@hey-api/sdk',
      validator: {
        response: 'zod', // [!code ++]
      },
    },
  ],
};
```

:::

Learn more about available validators on the [Validators](/openapi-ts/validators) page.

## Code Examples

The SDK plugin can generate ready-to-use code examples for each operation, showing how to call the SDK methods with proper parameters and setup.

Examples are not generated by default, but you can enable and customize them through the `examples` option. With the default settings, an example might look like this.

::: code-group

```ts [example]
import { PetStore } from 'your-package';

await new PetStore().addPet();
```

```js [config]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    // ...other plugins
    {
      examples: true, // [!code ++]
      name: '@hey-api/sdk',
      operations: {
        containerName: 'PetStore',
        strategy: 'single',
      },
    },
  ],
};
```

:::

### Module and Setup

To make examples more practical, configure `moduleName` to specify the package from which users import your SDK.

Next, set `setupName` to indicate how users should instantiate the SDK, typically only once per application.

::: code-group

```ts [example]
import { PetStore } from '@petstore/client'; // [!code ++]

const client = new PetStore(); // [!code ++]

await client.addPet();
```

```js [config]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    // ...other plugins
    {
      examples: {
        moduleName: '@petstore/client', // [!code ++]
        setupName: 'client', // [!code ++]
      },
      name: '@hey-api/sdk',
      operations: {
        containerName: 'PetStore',
        strategy: 'single',
      },
    },
  ],
};
```

:::

### Initialization

Often, your SDK needs to be instantiated with an API key or other configuration. In examples, `importSetup` lets you control how the SDK is initialized.

::: code-group

```ts [example]
import { PetStore } from '@petstore/client';

const client = new PetStore({ // [!code ++]
  apiKey: 'YOUR_API_KEY', // [!code ++]
}); // [!code ++]

await client.addPet();
```

```js [config]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    // ...other plugins
    {
      examples: {
        importSetup: ({ $, node }) => // [!code ++]
          $.new( // [!code ++]
            node.name, // [!code ++]
            $.object() // [!code ++]
              .pretty() // [!code ++]
              .prop('apiKey', $.literal('YOUR_API_KEY')), // [!code ++]
          ), // [!code ++]
        moduleName: '@petstore/client',
        setupName: 'client',
      },
      name: '@hey-api/sdk',
      operations: {
        containerName: 'PetStore',
        strategy: 'single',
      },
    },
  ],
};
```

:::

### Import Style

If you re-export the generated SDK from your own module, you can adjust `importName` and `importKind` to match your actual import style.

::: code-group

```ts [example]
import CatStore from '@petstore/client'; // [!code ++]

const client = new CatStore({ // [!code ++]
  apiKey: 'YOUR_API_KEY',
});

await client.addPet();
```

```js [config]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    // ...other plugins
    {
      examples: {
        importKind: 'default', // [!code ++]
        importName: 'CatStore', // [!code ++]
        importSetup: ({ $, node }) =>
          $(node.name).call(
            $.object().pretty().prop('apiKey', $.literal('YOUR_API_KEY')),
          ),
        moduleName: '@petstore/client',
        setupName: 'client',
      },
      name: '@hey-api/sdk',
      operations: {
        containerName: 'PetStore',
        strategy: 'single',
      },
    },
  ],
};
```

:::

### Payload

You can customize the example request using the `payload` option. Requests can also be customized selectively. For example, we can provide a default payload only for the `addPet()` method.

::: code-group

```ts [example]
import CatStore from '@petstore/client';

const client = new CatStore({
  apiKey: 'YOUR_API_KEY',
});

await client.addPet({ // [!code ++]
  petId: 1234, // [!code ++]
}); // [!code ++]
```

```js [config]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    // ...other plugins
    {
      examples: {
        importKind: 'default',
        importName: 'CatStore',
        importSetup: ({ $, node }) =>
          $(node.name).call(
            $.object().pretty().prop('apiKey', $.literal('YOUR_API_KEY')),
          ),
        moduleName: '@petstore/client',
        payload(operation, ctx) { // [!code ++]
          const { $ } = ctx; // [!code ++]
          if (operation.path === '/pet/{petId}' || operation.path === '/pet') { // [!code ++]
            return $.object().pretty().prop('petId', $.literal(1234)); // [!code ++]
          } // [!code ++]
        }, // [!code ++]
        setupName: 'client',
      },
      name: '@hey-api/sdk',
      operations: {
        containerName: 'PetStore',
        strategy: 'single',
      },
    },
  ],
};
```

:::

### Display

Enabling examples does not produce visible output on its own. Examples are written into the source specification and can be consumed by documentation tools such as [Mintlify](https://kutt.it/6vrYy9) or [Scalar](https://kutt.it/skQUVd). To persist that specification, enable [Source](/openapi-ts/configuration/output#source) generation.

## API

You can view the complete list of options in the [UserConfig](https://github.com/hey-api/openapi-ts/blob/main/packages/openapi-ts/src/plugins/@hey-api/sdk/types.d.ts) interface.

## Examples

You can view live examples on [StackBlitz](https://stackblitz.com/orgs/github/hey-api/collections/openapi-ts-examples).

## Sponsors

Hey API is sponsor-funded. If you rely on Hey API in production, consider becoming a [sponsor](https://github.com/sponsors/hey-api) to accelerate the roadmap.

---

---
url: /openapi-ts/community/spotlight.md
description: Meet the people behind Hey API.
---

# Spotlight

Meet the people behind Hey API. To join this list, please refer to the [contributing](/openapi-ts/community/contributing) guide.

## Core Team

These people actively maintain Hey API.

Do you want to join the core team? Send us a short [email](mailto:lubos@heyapi.dev?subject=Join%20Core%20Team) describing your interest in Hey API, any relevant experience, and what you're hoping to work on.

## Hall of Fame

These are the people with significant contributions to Hey API. A special thank you goes to [Ferdi Koomen](https://madebyferdi.com) for allowing us to use the original source code from OpenAPI TypeScript Codegen. None of this would've been possible without you!

## Contributors

The complete list of contributors to Hey API.

* [Ahmed Rowaihi](https://github.com/ahmedrowaihi)
* [Alessandro](https://github.com/ale18V)
* [Alex Sarychev](https://github.com/Freddis)
* [Alex Vukadinov](https://github.com/alexvuka1)
* [Alex Yang](https://github.com/himself65)
* [Alexander Horner](https://github.com/alexanderhorner)
* [Alexander Skvortcov](https://github.com/askvortcov)
* [Andrea](https://github.com/andreasciamanna)
* [Andreas Adam](https://github.com/pixelmord)
* [Ben Vincent](https://github.com/bvincent1)
* [Björn Henriksson](https://github.com/bjornhenriksson)
* [Bogdan ](https://github.com/BogdanMaier)
* [Brian Tarricone](https://github.com/kelnos)
* [Carl Kittelberger](https://github.com/icedream)
* [Changwan](https://github.com/WooWan)
* [Chris Wiggins](https://github.com/chriswiggins)
* [Daniel Roe](https://github.com/danielroe)
* [Daschi](https://github.com/Daschi1)
* [David Bieregger](https://github.com/BierDav)
* [David Ovčačík](https://github.com/dovca)
* [Dmitriy Brolnickij](https://github.com/brolnickij)
* [Finn Poppinga](https://github.com/fpoppinga)
* [Flo Edelmann](https://github.com/FloEdelmann)
* [Florian Lutze](https://github.com/flow96)
* [Francisco García](https://github.com/goltra)
* [George Smith](https://github.com/georgesmith46)
* [Gergan Penkov](https://github.com/gergan)
* [Hector Ayala](https://github.com/bombillazo)
* [Hiram Chirino](https://github.com/chirino)
* [Idan Ben Ami](https://github.com/idbenami)
* [Jacob Cohen](https://github.com/jacobinu)
* [Jan](https://github.com/JanST123)
* [Jason Lee](https://github.com/LeeChSien)
* [Jianqi Pan](https://github.com/Jannchie)
* [John Gozde](https://github.com/jgoz)
* [Jordan Shatford](https://github.com/jordanshatford)
* [Josh](https://github.com/josh-hemphill)
* [Joshua](https://github.com/Joshua-hypt)
* [Jostein Stuhaug](https://github.com/josstn)
* [Juan Ibarra](https://github.com/j-ibarra)
* [Julian Klumpers](https://github.com/julianklumpers)
* [Karl Stoney](https://github.com/Stono)
* [Keigo Ando](https://github.com/anchan828)
* [Kenneth Apeland](https://github.com/kennidenni)
* [Landon Gavin](https://github.com/seriouslag)
* [Laurin](https://github.com/lausek)
* [Lee Lian Hoy](https://github.com/bakakaba)
* [Leo Developer](https://github.com/Le0Developer)
* [Louis Duchemin](https://github.com/lsdch)
* [Lubos](https://github.com/mrlubos)
* [Maarten Knijnenberg](https://github.com/mknijnenberg)
* [Mads Hougesen](https://github.com/hougesen)
* [Malcolm Kee](https://github.com/malcolm-kee)
* [Marcel Richter](https://github.com/mrclrchtr)
* [Marek Lukáš](https://github.com/tajnymag)
* [Martín Fernández](https://github.com/bilby91)
* [Matsu](https://github.com/Matsuuu)
* [Maurici Abad Gutierrez](https://github.com/mauriciabad)
* [Max Scopp](https://github.com/max-scopp)
* [Maximilian Dewald](https://github.com/maxdewald)
* [Michał Grezel](https://github.com/dracomithril)
* [Michiel Lankamp](https://github.com/mlankamp)
* [Mika Vilpas](https://github.com/mikavilpas)
* [Miklos](https://github.com/jumika)
* [Nacho García](https://github.com/nachogarcia)
* [Nicolas Chaulet](https://github.com/nicolas-chaulet)
* [Nimo Beeren](https://github.com/nimobeeren)
* [Novak Antonijevic](https://github.com/NovakAnton)
* [Ondřej Maxa](https://github.com/maxa-ondrej)
* [Pascal Ernst](https://github.com/LinuCC)
* [Philipp Katz](https://github.com/qqilihq)
* [Phuc Tran](https://github.com/Glup3)
* [Rico](https://github.com/btmnk)
* [Ryo Yamada](https://github.com/Liooo)
* [Sebastiaan Wouters](https://github.com/SebastiaanWouters)
* [Shinigami](https://github.com/Shinigami92)
* [Simen Bekkhus](https://github.com/SimenB)
* [Sjoerd Scheffer](https://github.com/ixnas)
* [Stian Jensen](https://github.com/stianjensen)
* [Vincent Olesen](https://github.com/volesen)
* [Warren Seine](https://github.com/warrenseine)
* [Will Mitchell](https://github.com/wn-mitch)
* [a1mer](https://github.com/a1mersnow)
* [carson](https://github.com/carson2222)
* [johnny kim](https://github.com/johnny-mh)
* [0xfurai](https://github.com/0xfurai)
* [9M6](https://github.com/9M6)
* [Ben-Pfirsich](https://github.com/Ben-Pfirsich)
* [Mxwllas](https://github.com/Mxwllas)
* [RndUsername](https://github.com/RndUsername)
* [Schroedi](https://github.com/Schroedi)
* [alexedme](https://github.com/alexedme)
* [ben-pietsch](https://github.com/ben-pietsch)
* [fml09](https://github.com/fml09)
* [henry-encord](https://github.com/henry-encord)
* [hunshcn](https://github.com/hunshcn)
* [maxdew-envelio](https://github.com/maxdew-envelio)
* [nnzhadow](https://github.com/nnzhadow)
* [renoschubert](https://github.com/renoschubert)

A sincere thank you for your contributions.

---

---
url: /openapi-ts/state-management.md
description: Learn about handling state with @hey-api/openapi-ts.
---

# State Management

Any reasonably large application will have to deal with state management at some point. State-related code is often one of the biggest boilerplates in your codebase. Well, at least until you start using our state management plugins.

## Options

Hey API natively supports the following state managers.

* [Pinia Colada](/openapi-ts/plugins/pinia-colada)
* [TanStack Query](/openapi-ts/plugins/tanstack-query)
* [SWR](/openapi-ts/plugins/swr) Soon
* [Zustand](/openapi-ts/plugins/zustand) Soon

Don't see your state manager? Let us know your interest by [opening an issue](https://github.com/hey-api/openapi-ts/issues).

## Examples

You can view live examples on [StackBlitz](https://stackblitz.com/orgs/github/hey-api/collections/openapi-ts-examples).

## Sponsors

Hey API is sponsor-funded. If you rely on Hey API in production, consider becoming a [sponsor](https://github.com/sponsors/hey-api) to accelerate the roadmap.

---

---
url: /openapi-ts/plugins/superstruct.md
description: Superstruct plugin for Hey API. Compatible with all our features.
---

# Superstruct soon

### About

[Superstruct](https://docs.superstructjs.org) makes it easy to define interfaces and then validate JavaScript data against them.

## Sponsors

Hey API is sponsor-funded. If you rely on Hey API in production, consider becoming a [sponsor](https://github.com/sponsors/hey-api) to accelerate the roadmap.

---

---
url: /openapi-ts/plugins/supertest.md
description: Supertest plugin for Hey API. Compatible with all our features.
---

# Supertest soon

### About

[Supertest](https://github.com/ladjs/supertest) is a super-agent driven library for testing node.js HTTP servers using a fluent API.

## Sponsors

Hey API is sponsor-funded. If you rely on Hey API in production, consider becoming a [sponsor](https://github.com/sponsors/hey-api) to accelerate the roadmap.

---

---
url: /openapi-ts/plugins/swr.md
description: SWR plugin for Hey API. Compatible with all our features.
---

# SWR soon

### About

[SWR](https://swr.vercel.app) is a strategy to first return the data from cache (stale), then send the fetch request (revalidate), and finally come with the up-to-date data.

## Sponsors

Hey API is sponsor-funded. If you rely on Hey API in production, consider becoming a [sponsor](https://github.com/sponsors/hey-api) to accelerate the roadmap.

---

---
url: /openapi-ts/plugins/tanstack-query.md
description: >-
  Generate TanStack Query v5 functions and query keys from OpenAPI with the
  TanStack Query plugin for openapi-ts. Fully compatible with validators,
  transformers, and all core features.
---

### About

[TanStack Query](https://tanstack.com/query) is a powerful asynchronous state management solution for TypeScript/JavaScript, React, Solid, Vue, Svelte, and Angular.

The TanStack Query plugin for Hey API generates functions and query keys from your OpenAPI spec, fully compatible with SDKs, transformers, and all core features.

### Demo

\<button class="buttonLink" @click="(event) => embedProject('hey-api-client-fetch-plugin-tanstack-react-query-example')(event)">
Launch demo


## Features

* TanStack Query v5 support
* seamless integration with `@hey-api/openapi-ts` ecosystem
* create query keys following the best practices
* type-safe query options, infinite query options, and mutation options
* minimal learning curve thanks to extending the underlying technology

## Installation

In your [configuration](/openapi-ts/get-started), add TanStack Query to your plugins and you'll be ready to generate TanStack Query artifacts. :tada:

::: code-group

```js [react]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    // ...other plugins
    '@tanstack/react-query', // [!code ++]
  ],
};
```

```js [vue]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    // ...other plugins
    '@tanstack/vue-query', // [!code ++]
  ],
};
```

```js [angular]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    // ...other plugins
    '@tanstack/angular-query-experimental', // [!code ++]
  ],
};
```

```js [svelte]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    // ...other plugins
    '@tanstack/svelte-query', // [!code ++]
  ],
};
```

```js [solid]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    // ...other plugins
    '@tanstack/solid-query', // [!code ++]
  ],
};
```

:::

## Output

The TanStack Query plugin will generate the following artifacts, depending on the input specification.

## Queries

Queries are generated from [query operations](/openapi-ts/configuration/parser#hooks-query-operations). The generated query functions follow the naming convention of SDK functions and by default append `Options`, e.g. `getPetByIdOptions()`.

::: code-group

```ts [example]
const query = useQuery({
  ...getPetByIdOptions({
    path: {
      petId: 1,
    },
  }),
});
```

```js [config]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    // ...other plugins
    {
      name: '@tanstack/react-query',
      queryOptions: true, // [!code ++]
    },
  ],
};
```

:::

You can customize the naming and casing pattern for `queryOptions` functions using the `.name` and `.case` options.

### Meta

You can use the `meta` field to attach arbitrary information to a query. To generate metadata for `queryOptions`, provide a function to the `.meta` option.

::: code-group

```ts [example]
queryOptions({
  // ...other fields
  meta: {
    id: 'getPetById',
  },
});
```

```js [config]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    // ...other plugins
    {
      name: '@tanstack/react-query',
      queryOptions: {
        meta: (operation) => ({ id: operation.id }), // [!code ++]
      },
    },
  ],
};
```

:::

## Query Keys

Query keys contain normalized SDK function parameters and additional metadata.

::: code-group

```ts [example]
const queryKey = [
  {
    _id: 'getPetById',
    baseUrl: 'https://app.heyapi.dev',
    path: {
      petId: 1,
    },
  },
];
```

```js [config]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    // ...other plugins
    {
      name: '@tanstack/react-query',
      queryKeys: true, // [!code ++]
    },
  ],
};
```

:::

### Tags

You can include operation tags in your query keys by setting `tags` to `true`. This will make query keys larger but provides better cache invalidation capabilities.

::: code-group

```ts [example]
const queryKey = [
  {
    _id: 'getPetById',
    baseUrl: 'https://app.heyapi.dev',
    path: {
      petId: 1,
    },
    tags: ['pets', 'one', 'get'], // [!code ++]
  },
];
```

```js [config]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    // ...other plugins
    {
      name: '@tanstack/react-query',
      queryKeys: {
        tags: true, // [!code ++]
      },
    },
  ],
};
```

:::

### Accessing Query Keys

If you have access to the result of query options function, you can get the query key from the `queryKey` field.

::: code-group

```ts [example]
const { queryKey } = getPetByIdOptions({
  path: {
    petId: 1,
  },
});
```

```js [config]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    // ...other plugins
    {
      name: '@tanstack/react-query',
      queryOptions: true, // [!code ++]
    },
  ],
};
```

:::

Alternatively, you can access the same query key by calling query key functions. The generated query key functions follow the naming convention of SDK functions and by default append `QueryKey`, e.g. `getPetByIdQueryKey()`.

::: code-group

```ts [example]
const queryKey = getPetByIdQueryKey({
  path: {
    petId: 1,
  },
});
```

```js [config]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    // ...other plugins
    {
      name: '@tanstack/react-query',
      queryKeys: true, // [!code ++]
    },
  ],
};
```

:::

You can customize the naming and casing pattern for `queryKeys` functions using the `.name` and `.case` options.

## Infinite Queries

Infinite queries are generated from [query operations](/openapi-ts/configuration/parser#hooks-query-operations) if we detect a [pagination](/openapi-ts/configuration/parser#pagination) parameter. The generated infinite query functions follow the naming convention of SDK functions and by default append `InfiniteOptions`, e.g. `getFooInfiniteOptions()`.

::: code-group

```ts [example]
const query = useInfiniteQuery({
  ...getFooInfiniteOptions({
    path: {
      fooId: 1,
    },
  }),
  getNextPageParam: (lastPage, pages) => lastPage.nextCursor,
  initialPageParam: 0,
});
```

```js [config]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    // ...other plugins
    {
      name: '@tanstack/react-query',
      infiniteQueryOptions: true, // [!code ++]
    },
  ],
};
```

:::

You can customize the naming and casing pattern for `infiniteQueryOptions` functions using the `.name` and `.case` options.

### Meta

You can use the `meta` field to attach arbitrary information to a query. To generate metadata for `infiniteQueryOptions`, provide a function to the `.meta` option.

::: code-group

```ts [example]
infiniteQueryOptions({
  // ...other fields
  meta: {
    id: 'getPetById',
  },
});
```

```js [config]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    // ...other plugins
    {
      name: '@tanstack/react-query',
      infiniteQueryOptions: {
        meta: (operation) => ({ id: operation.id }), // [!code ++]
      },
    },
  ],
};
```

:::

## Infinite Query Keys

Infinite query keys contain normalized SDK function parameters and additional metadata.

::: code-group

```ts [example]
const queryKey = [
  {
    _id: 'getPetById',
    _infinite: true,
    baseUrl: 'https://app.heyapi.dev',
    path: {
      petId: 1,
    },
  },
];
```

```js [config]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    // ...other plugins
    {
      name: '@tanstack/react-query',
      infiniteQueryKeys: true, // [!code ++]
    },
  ],
};
```

:::

### Tags

You can include operation tags in your infinite query keys by setting `tags` to `true`. This will make query keys larger but provides better cache invalidation capabilities.

::: code-group

```ts [example]
const queryKey = [
  {
    _id: 'getPetById',
    _infinite: true,
    baseUrl: 'https://app.heyapi.dev',
    path: {
      petId: 1,
    },
    tags: ['pets', 'one', 'get'], // [!code ++]
  },
];
```

```js [config]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    // ...other plugins
    {
      name: '@tanstack/react-query',
      infiniteQueryKeys: {
        tags: true, // [!code ++]
      },
    },
  ],
};
```

:::

### Accessing Infinite Query Keys

If you have access to the result of infinite query options function, you can get the query key from the `queryKey` field.

::: code-group

```ts [example]
const { queryKey } = getPetByIdInfiniteOptions({
  path: {
    petId: 1,
  },
});
```

```js [config]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    // ...other plugins
    {
      name: '@tanstack/react-query',
      infiniteQueryOptions: true, // [!code ++]
    },
  ],
};
```

:::

Alternatively, you can access the same query key by calling query key functions. The generated query key functions follow the naming convention of SDK functions and by default append `InfiniteQueryKey`, e.g. `getPetByIdInfiniteQueryKey()`.

::: code-group

```ts [example]
const queryKey = getPetByIdInfiniteQueryKey({
  path: {
    petId: 1,
  },
});
```

```js [config]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    // ...other plugins
    {
      name: '@tanstack/react-query',
      infiniteQueryKeys: true, // [!code ++]
    },
  ],
};
```

:::

You can customize the naming and casing pattern for `infiniteQueryKeys` functions using the `.name` and `.case` options.

## Mutations

Mutations are generated from [mutation operations](/openapi-ts/configuration/parser#hooks-mutation-operations). The generated mutation functions follow the naming convention of SDK functions and by default append `Mutation`, e.g. `addPetMutation()`.

::: code-group

```ts [example]
const addPet = useMutation({
  ...addPetMutation(),
  onError: (error) => {
    console.log(error);
  },
});

addPet.mutate({
  body: {
    name: 'Kitty',
  },
});
```

```js [config]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    // ...other plugins
    {
      name: '@tanstack/react-query',
      mutationOptions: true, // [!code ++]
    },
  ],
};
```

:::

You can customize the naming and casing pattern for `mutationOptions` functions using the `.name` and `.case` options.

### Meta

You can use the `meta` field to attach arbitrary information to a mutation. To generate metadata for `mutationOptions`, provide a function to the `.meta` option.

::: code-group

```ts [example]
const mutationOptions = {
  // ...other fields
  meta: {
    id: 'getPetById',
  },
};
```

```js [config]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    // ...other plugins
    {
      name: '@tanstack/react-query',
      mutationOptions: {
        meta: (operation) => ({ id: operation.id }), // [!code ++]
      },
    },
  ],
};
```

:::

## Reactivity

In Vue applications, you need to wrap the options functions in [`computed()`](https://vuejs.org/guide/essentials/computed) to make them reactive. Otherwise, TanStack Query won't know it should execute the query when its dependencies change.

::: code-group

```js [reactive]
// ✅ Query will execute on `petId` change
const query = useQuery(
  computed(() =>
    getPetByIdOptions({
      path: {
        petId: petId.value,
      },
    }),
  ),
);
```

```js [static]
// ❌ Query will execute only once
const query = useQuery(
  getPetByIdOptions({
    path: {
      petId: petId.value,
    },
  }),
);
```

:::

## API

You can view the complete list of options in the [UserConfig](https://github.com/hey-api/openapi-ts/blob/main/packages/openapi-ts/src/plugins/@tanstack/react-query/types.d.ts) interface.

## Examples

You can view live examples on [StackBlitz](https://stackblitz.com/orgs/github/hey-api/collections/openapi-ts-examples).

## Sponsors

Hey API is sponsor-funded. If you rely on Hey API in production, consider becoming a [sponsor](https://github.com/sponsors/hey-api) to accelerate the roadmap.

---

---
url: /openapi-ts/community/contributing/testing.md
description: Learn how to contribute to Hey API.
---

# Testing

::: warning
This page is under construction. We appreciate your patience.
:::

---

---
url: /openapi-ts/plugins/transformers.md
description: Learn about transforming data with @hey-api/openapi-ts.
---

# Transformers

JSON is the most commonly used data format in REST APIs. However, it does not map well to complex data types. For example, both regular strings and date strings become simple strings in JSON.

One approach to this problem is using a [JSON superset](https://github.com/blitz-js/superjson). For most people, switching formats is not feasible. That's why we provide the `@hey-api/transformers` plugin.

::: warning
Transformers currently handle only the most common use cases. If your data isn't being transformed as expected, we encourage you to leave feedback on [GitHub](https://github.com/hey-api/openapi-ts/issues).
:::

## Considerations

Before deciding whether transformers are right for you, let's explain how they work. Transformers generate a runtime file, therefore they impact the bundle size. We generate a single transformer per operation response for the most efficient result, just like a human engineer would.

### Limitations

Transformers handle only the most common scenarios. Some of the known limitations are:

* union types are not transformed (e.g. if you have multiple possible response shapes)
* only types defined through `$ref` are transformed
* error responses are not transformed

If your data isn't being transformed as expected, we encourage you to leave feedback on [GitHub](https://github.com/hey-api/openapi-ts/issues).

## Installation

In your [configuration](/openapi-ts/get-started), add `@hey-api/transformers` to your plugins and you'll be ready to generate transformers. :tada:

```js
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    // ...other plugins
    '@hey-api/transformers', // [!code ++]
  ],
};
```

## SDKs

To automatically transform response data in your SDKs, set `sdk.transformer` to `true`.

```js
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    // ...other plugins
    '@hey-api/transformers',
    {
      name: '@hey-api/sdk', // [!code ++]
      transformer: true, // [!code ++]
    },
  ],
};
```

## Dates

To convert date strings into `Date` objects, use the `dates` configuration option.

```js
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    // ...other plugins
    {
      dates: true, // [!code ++]
      name: '@hey-api/transformers',
    },
  ],
};
```

This will generate types that use `Date` instead of `string` and appropriate transformers. Note that third-party date packages are not supported at the moment.

## BigInt

The `@hey-api/transformers` plugin will natively type all BigInts as `bigint` instead of `number`, which can affect arithmetic operations if your application previously used `number`. To force BigInts to be numbers, use the `bigint` configuration option.

```js
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    // ...other plugins
    {
      bigint: true, // [!code ++]
      name: '@hey-api/transformers',
    },
  ],
};
```

## Example

A generated response transformer might look something like this. Please note the example has been edited for brevity.

::: code-group

```ts [transformers.gen.ts]
import type { GetFooResponse } from './types.gen';

const quxSchemaResponseTransformer = (data: any) => {
  if (data.baz) {
    data.baz = new Date(data.baz);
  }
  return data;
};

const bazSchemaResponseTransformer = (data: any) => {
  data = quxSchemaResponseTransformer(data);
  data.bar = new Date(data.bar);
  return data;
};

export const getFooResponseTransformer = async (
  data: any,
): Promise<GetFooResponse> => {
  data = bazSchemaResponseTransformer(data);
  return data;
};
```

```ts [types.gen.ts]
export type Baz = Qux & {
  id: 'Baz';
} & {
  foo: number;
  bar: Date;
  baz: 'foo' | 'bar' | 'baz';
  qux: number;
};

export type Qux = {
  foo: number;
  bar: number;
  baz?: Date;
  id: string;
};

export type GetFooResponse = Baz;
```

:::

## API

You can view the complete list of options in the [UserConfig](https://github.com/hey-api/openapi-ts/blob/main/packages/openapi-ts/src/plugins/@hey-api/transformers/types.d.ts) interface.

---

---
url: /openapi-ts/plugins/typebox.md
description: TypeBox plugin for Hey API. Compatible with all our features.
---

# TypeBox soon

### About

[TypeBox](https://github.com/sinclairzx81/typebox) is a JSON Schema type builder with static type resolution for TypeScript.

## Sponsors

Hey API is sponsor-funded. If you rely on Hey API in production, consider becoming a [sponsor](https://github.com/sponsors/hey-api) to accelerate the roadmap.

---

---
url: /openapi-ts/plugins/typescript.md
description: Learn about files generated with @hey-api/openapi-ts.
---

# TypeScript

TypeScript interfaces are located in the `types.gen.ts` file. This is the only file that does not impact your bundle size and runtime performance. It will get discarded during build time, unless you configured to emit runtime [enums](#enums).

## Installation

In your [configuration](/openapi-ts/get-started), add `@hey-api/typescript` to your plugins and you'll be ready to generate TypeScript artifacts. :tada:

```js
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    // ...other plugins
    '@hey-api/typescript', // [!code ++]
  ],
};
```

:::tip
The `@hey-api/typescript` plugin might be implicitly added to your `plugins` if another plugin depends on it.
:::

## Output

The TypeScript plugin will generate the following artifacts, depending on the input specification.

## Requests

A single request type is generated for each endpoint. It may contain a request body, parameters, and headers.

```ts
export type AddPetData = {
  body: {
    id?: number;
    name: string;
  };
  path?: never;
  query?: never;
  url: '/pets';
};
```

You can customize the naming and casing pattern for `requests` types using the `.name` and `.case` options.

## Responses

A single type is generated for all endpoint's responses.

```ts
export type AddPetResponses = {
  200: {
    id?: number;
    name: string;
  };
};

export type AddPetResponse = AddPetResponses[keyof AddPetResponses];
```

You can customize the naming and casing pattern for `responses` types using the `.name` and `.case` options.

## Definitions

A type is generated for every reusable definition from your input.

```ts
export type Pet = {
  id?: number;
  name: string;
};
```

You can customize the naming and casing pattern for `definitions` types using the `.name` and `.case` options.

## Enums

By default, `@hey-api/typescript` will emit enums only as types. You may want to generate runtime artifacts. A good use case is iterating through possible field values without manually typing arrays. To emit runtime enums, set `enums` to a valid option.

::: code-group

```js [disabled]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    // ...other plugins
    {
      enums: false, // default // [!code ++]
      name: '@hey-api/typescript',
    },
  ],
};
```

```js [javascript]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    // ...other plugins
    {
      enums: 'javascript', // [!code ++]
      name: '@hey-api/typescript',
    },
  ],
};
```

```js [typescript]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    // ...other plugins
    {
      enums: 'typescript', // [!code ++]
      name: '@hey-api/typescript',
    },
  ],
};
```

:::

We recommend exporting enums as plain JavaScript objects. [TypeScript enums](https://www.typescriptlang.org/docs/handbook/enums.html) are not a type-level extension of JavaScript and pose [typing challenges](https://dev.to/ivanzm123/dont-use-enums-in-typescript-they-are-very-dangerous-57bh).

## API

You can view the complete list of options in the [UserConfig](https://github.com/hey-api/openapi-ts/blob/main/packages/openapi-ts/src/plugins/@hey-api/typescript/types.d.ts) interface.

## Examples

You can view live examples on [StackBlitz](https://stackblitz.com/orgs/github/hey-api/collections/openapi-ts-examples).

## Sponsors

Hey API is sponsor-funded. If you rely on Hey API in production, consider becoming a [sponsor](https://github.com/sponsors/hey-api) to accelerate the roadmap.

---

---
url: /email-form.md
---
### Newsletter

Subscribe to product updates.

---

---
url: /partials/contributors-list.md
---
* [Ahmed Rowaihi](https://github.com/ahmedrowaihi)
* [Alessandro](https://github.com/ale18V)
* [Alex Sarychev](https://github.com/Freddis)
* [Alex Vukadinov](https://github.com/alexvuka1)
* [Alex Yang](https://github.com/himself65)
* [Alexander Horner](https://github.com/alexanderhorner)
* [Alexander Skvortcov](https://github.com/askvortcov)
* [Andrea](https://github.com/andreasciamanna)
* [Andreas Adam](https://github.com/pixelmord)
* [Ben Vincent](https://github.com/bvincent1)
* [Björn Henriksson](https://github.com/bjornhenriksson)
* [Bogdan ](https://github.com/BogdanMaier)
* [Brian Tarricone](https://github.com/kelnos)
* [Carl Kittelberger](https://github.com/icedream)
* [Changwan](https://github.com/WooWan)
* [Chris Wiggins](https://github.com/chriswiggins)
* [Daniel Roe](https://github.com/danielroe)
* [Daschi](https://github.com/Daschi1)
* [David Bieregger](https://github.com/BierDav)
* [David Ovčačík](https://github.com/dovca)
* [Dmitriy Brolnickij](https://github.com/brolnickij)
* [Finn Poppinga](https://github.com/fpoppinga)
* [Flo Edelmann](https://github.com/FloEdelmann)
* [Florian Lutze](https://github.com/flow96)
* [Francisco García](https://github.com/goltra)
* [George Smith](https://github.com/georgesmith46)
* [Gergan Penkov](https://github.com/gergan)
* [Hector Ayala](https://github.com/bombillazo)
* [Hiram Chirino](https://github.com/chirino)
* [Idan Ben Ami](https://github.com/idbenami)
* [Jacob Cohen](https://github.com/jacobinu)
* [Jan](https://github.com/JanST123)
* [Jason Lee](https://github.com/LeeChSien)
* [Jianqi Pan](https://github.com/Jannchie)
* [John Gozde](https://github.com/jgoz)
* [Jordan Shatford](https://github.com/jordanshatford)
* [Josh](https://github.com/josh-hemphill)
* [Joshua](https://github.com/Joshua-hypt)
* [Jostein Stuhaug](https://github.com/josstn)
* [Juan Ibarra](https://github.com/j-ibarra)
* [Julian Klumpers](https://github.com/julianklumpers)
* [Karl Stoney](https://github.com/Stono)
* [Keigo Ando](https://github.com/anchan828)
* [Kenneth Apeland](https://github.com/kennidenni)
* [Landon Gavin](https://github.com/seriouslag)
* [Laurin](https://github.com/lausek)
* [Lee Lian Hoy](https://github.com/bakakaba)
* [Leo Developer](https://github.com/Le0Developer)
* [Louis Duchemin](https://github.com/lsdch)
* [Lubos](https://github.com/mrlubos)
* [Maarten Knijnenberg](https://github.com/mknijnenberg)
* [Mads Hougesen](https://github.com/hougesen)
* [Malcolm Kee](https://github.com/malcolm-kee)
* [Marcel Richter](https://github.com/mrclrchtr)
* [Marek Lukáš](https://github.com/tajnymag)
* [Martín Fernández](https://github.com/bilby91)
* [Matsu](https://github.com/Matsuuu)
* [Maurici Abad Gutierrez](https://github.com/mauriciabad)
* [Max Scopp](https://github.com/max-scopp)
* [Maximilian Dewald](https://github.com/maxdewald)
* [Michał Grezel](https://github.com/dracomithril)
* [Michiel Lankamp](https://github.com/mlankamp)
* [Mika Vilpas](https://github.com/mikavilpas)
* [Miklos](https://github.com/jumika)
* [Nacho García](https://github.com/nachogarcia)
* [Nicolas Chaulet](https://github.com/nicolas-chaulet)
* [Nimo Beeren](https://github.com/nimobeeren)
* [Novak Antonijevic](https://github.com/NovakAnton)
* [Ondřej Maxa](https://github.com/maxa-ondrej)
* [Pascal Ernst](https://github.com/LinuCC)
* [Philipp Katz](https://github.com/qqilihq)
* [Phuc Tran](https://github.com/Glup3)
* [Rico](https://github.com/btmnk)
* [Ryo Yamada](https://github.com/Liooo)
* [Sebastiaan Wouters](https://github.com/SebastiaanWouters)
* [Shinigami](https://github.com/Shinigami92)
* [Simen Bekkhus](https://github.com/SimenB)
* [Sjoerd Scheffer](https://github.com/ixnas)
* [Stian Jensen](https://github.com/stianjensen)
* [Vincent Olesen](https://github.com/volesen)
* [Warren Seine](https://github.com/warrenseine)
* [Will Mitchell](https://github.com/wn-mitch)
* [a1mer](https://github.com/a1mersnow)
* [carson](https://github.com/carson2222)
* [johnny kim](https://github.com/johnny-mh)
* [0xfurai](https://github.com/0xfurai)
* [9M6](https://github.com/9M6)
* [Ben-Pfirsich](https://github.com/Ben-Pfirsich)
* [Mxwllas](https://github.com/Mxwllas)
* [RndUsername](https://github.com/RndUsername)
* [Schroedi](https://github.com/Schroedi)
* [alexedme](https://github.com/alexedme)
* [ben-pietsch](https://github.com/ben-pietsch)
* [fml09](https://github.com/fml09)
* [henry-encord](https://github.com/henry-encord)
* [hunshcn](https://github.com/hunshcn)
* [maxdew-envelio](https://github.com/maxdew-envelio)
* [nnzhadow](https://github.com/nnzhadow)
* [renoschubert](https://github.com/renoschubert)

---

---
url: /partials/examples.md
---
## Examples

You can view live examples on [StackBlitz](https://stackblitz.com/orgs/github/hey-api/collections/openapi-ts-examples).

---

---
url: /partials/sponsors-list.md
---
### Gold

### Silver

### Bronze

### Friends

---

---
url: /partials/sponsors.md
---
## Sponsors

Hey API is sponsor-funded. If you rely on Hey API in production, consider becoming a [sponsor](https://github.com/sponsors/hey-api) to accelerate the roadmap.

### Gold

### Silver

### Bronze

### Friends

---

---
url: /openapi-ts/plugins/valibot.md
description: >-
  Generate Valibot v1 schemas from OpenAPI with the Valibot plugin for
  openapi-ts. Fully compatible with validators, transformers, and all core
  features.
---

### About

[Valibot](https://valibot.dev) is the open source schema library for TypeScript with bundle size, type safety and developer experience in mind.

The Valibot plugin for Hey API generates schemas from your OpenAPI spec, fully compatible with validators, transformers, and all core features.

## Features

* Valibot v1 support
* seamless integration with `@hey-api/openapi-ts` ecosystem
* Valibot schemas for requests, responses, and reusable definitions
* minimal learning curve thanks to extending the underlying technology

## Installation

In your [configuration](/openapi-ts/get-started), add `valibot` to your plugins and you'll be ready to generate Valibot artifacts. :tada:

```js
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    // ...other plugins
    'valibot', // [!code ++]
  ],
};
```

### SDKs

To add data validators to your SDKs, set `sdk.validator` to `true`.

```js
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    // ...other plugins
    'valibot',
    {
      name: '@hey-api/sdk', // [!code ++]
      validator: true, // [!code ++]
    },
  ],
};
```

Learn more about data validators in your SDKs on the [SDKs](/openapi-ts/plugins/sdk#validators) page.

## Output

The Valibot plugin will generate the following artifacts, depending on the input specification.

## Requests

A single request schema is generated for each endpoint. It may contain a request body, parameters, and headers.

::: code-group

```ts [example]
const vData = v.object({
  body: v.optional(
    v.object({
      foo: v.optional(v.string()),
      bar: v.optional(v.union([v.number(), v.null()])),
    }),
  ),
  path: v.object({
    baz: v.string(),
  }),
  query: v.optional(v.never()),
});
```

```js [config]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    // ...other plugins
    {
      name: 'valibot',
      requests: true, // [!code ++]
    },
  ],
};
```

:::

::: tip
If you need to access individual fields, you can do so using the [`.entries`](https://valibot.dev/api/object/) API. For example, we can get the request body schema with `vData.entries.body`.
:::

You can customize the naming and casing pattern for `requests` schemas using the `.name` and `.case` options.

## Responses

A single Valibot schema is generated for all endpoint's responses. If the endpoint describes multiple responses, the generated schema is a union of all possible response shapes.

::: code-group

```ts [example]
const vResponse = v.union([
  v.object({
    foo: v.optional(v.string()),
  }),
  v.object({
    bar: v.optional(v.number()),
  }),
]);
```

```js [config]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    // ...other plugins
    {
      name: 'valibot',
      responses: true, // [!code ++]
    },
  ],
};
```

:::

You can customize the naming and casing pattern for `responses` schemas using the `.name` and `.case` options.

## Definitions

A Valibot schema is generated for every reusable definition from your input.

::: code-group

```ts [example]
const vFoo = v.pipe(v.number(), v.integer());

const vBar = v.object({
  bar: v.optional(v.array(v.pipe(v.number(), v.integer()))),
});
```

```js [config]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    // ...other plugins
    {
      name: 'valibot',
      definitions: true, // [!code ++]
    },
  ],
};
```

:::

You can customize the naming and casing pattern for `definitions` schemas using the `.name` and `.case` options.

## Metadata

It's often useful to associate a schema with some additional [metadata](https://valibot.dev/api/metadata/) for documentation, code generation, AI structured outputs, form validation, and other purposes. If this is your use case, you can set `metadata` to `true` to generate additional metadata about schemas.

::: code-group

```ts [example]
export const vFoo = v.pipe(
  v.string(),
  v.metadata({
    description: 'Additional metadata',
  }),
);
```

```js [config]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    // ...other plugins
    {
      name: 'valibot',
      metadata: true, // [!code ++]
    },
  ],
};
```

:::

## Resolvers

You can further customize this plugin's behavior using [resolvers](/openapi-ts/plugins/concepts/resolvers).

## API

You can view the complete list of options in the [UserConfig](https://github.com/hey-api/openapi-ts/blob/main/packages/openapi-ts/src/plugins/valibot/types.d.ts) interface.

## Examples

You can view live examples on [StackBlitz](https://stackblitz.com/orgs/github/hey-api/collections/openapi-ts-examples).

## Sponsors

Hey API is sponsor-funded. If you rely on Hey API in production, consider becoming a [sponsor](https://github.com/sponsors/hey-api) to accelerate the roadmap.

---

---
url: /openapi-ts/validators.md
description: Learn about validating data with @hey-api/openapi-ts.
---

# Validators

There are times when you cannot blindly trust the server to return the correct data. You might be working on a critical application where any mistakes would be costly, or you're simply dealing with a legacy or undocumented system.

Whatever your reason to use validators might be, you can rest assured that you're working with the correct data.

## Features

* seamless integration with `@hey-api/openapi-ts` ecosystem
* schemas for requests, responses, and reusable definitions

## Options

Hey API natively supports the following validators.

* [Valibot](/openapi-ts/plugins/valibot)
* [Zod](/openapi-ts/plugins/zod)
* [Ajv](/openapi-ts/plugins/ajv) Soon
* [Arktype](/openapi-ts/plugins/arktype) Soon
* [Joi](/openapi-ts/plugins/joi) Soon
* [TypeBox](/openapi-ts/plugins/typebox) Soon
* [Yup](/openapi-ts/plugins/yup) Soon

Don't see your validator? Let us know your interest by [opening an issue](https://github.com/hey-api/openapi-ts/issues).

## Examples

You can view live examples on [StackBlitz](https://stackblitz.com/orgs/github/hey-api/collections/openapi-ts-examples).

## Sponsors

Hey API is sponsor-funded. If you rely on Hey API in production, consider becoming a [sponsor](https://github.com/sponsors/hey-api) to accelerate the roadmap.

---

---
url: /openapi-ts/web-frameworks.md
description: Learn about generating web framework code with @hey-api/openapi-ts.
---

# Web Frameworks

There are two approaches to developing APIs: code-first, where you start with the code, or spec-first, where you begin with the specification. If you use the latter, you can ensure your APIs adhere to the specification with our web framework plugins.

## Options

Hey API natively supports the following frameworks.

* [Angular](/openapi-ts/plugins/angular)
* [Fastify](/openapi-ts/plugins/fastify)
* [Adonis](/openapi-ts/plugins/adonis) Soon
* [Elysia](/openapi-ts/plugins/elysia) Soon
* [Express](/openapi-ts/plugins/express) Soon
* [Hono](/openapi-ts/plugins/hono) Soon
* [Koa](/openapi-ts/plugins/koa) Soon
* [Nest](/openapi-ts/plugins/nest) Soon

Don't see your framework? Let us know your interest by [opening an issue](https://github.com/hey-api/openapi-ts/issues).

## Examples

You can view live examples on [StackBlitz](https://stackblitz.com/orgs/github/hey-api/collections/openapi-ts-examples).

## Sponsors

Hey API is sponsor-funded. If you rely on Hey API in production, consider becoming a [sponsor](https://github.com/sponsors/hey-api) to accelerate the roadmap.

---

---
url: /openapi-ts/plugins/yup.md
description: Yup plugin for Hey API. Compatible with all our features.
---

# Yup soon

### About

[Yup](https://github.com/jquense/yup) is a schema builder for runtime value parsing and validation.

## Sponsors

Hey API is sponsor-funded. If you rely on Hey API in production, consider becoming a [sponsor](https://github.com/sponsors/hey-api) to accelerate the roadmap.

---

---
url: /openapi-ts/plugins/zod/mini.md
description: >-
  Generate Zod Mini schemas from OpenAPI with the Zod plugin for openapi-ts.
  Fully compatible with validators, transformers, and all core features.
---

### About

[Zod](https://zod.dev) is a TypeScript-first schema validation library with static type inference.

The Zod plugin for Hey API generates schemas from your OpenAPI spec, fully compatible with validators, transformers, and all core features.

## Features

* Zod Mini support
* seamless integration with `@hey-api/openapi-ts` ecosystem
* Zod schemas for requests, responses, and reusable definitions
* minimal learning curve thanks to extending the underlying technology

## Installation

In your [configuration](/openapi-ts/get-started), add `zod` to your plugins and you'll be ready to generate Zod artifacts. :tada:

```js
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    // ...other plugins
    {
      name: 'zod', // [!code ++]
      compatibilityVersion: 'mini', // [!code ++]
    },
  ],
};
```

### SDKs

To add data validators to your SDKs, set `sdk.validator` to `true`.

```js
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    // ...other plugins
    {
      name: 'zod',
      compatibilityVersion: 'mini',
    },
    {
      name: '@hey-api/sdk', // [!code ++]
      validator: true, // [!code ++]
    },
  ],
};
```

Learn more about data validators in your SDKs on the [SDKs](/openapi-ts/plugins/sdk#validators) page.

## Output

The Zod plugin will generate the following artifacts, depending on the input specification.

## Requests

A single request schema is generated for each endpoint. It may contain a request body, parameters, and headers.

::: code-group

```ts [example]
const zData = z.object({
  body: z
    .object({
      foo: z.optional(z.string()),
      bar: z.optional(z.union([z.number(), z.null()])),
    })
    .optional(),
  path: z.object({
    baz: z.string(),
  }),
  query: z.optional(z.never()),
});
```

```js [config]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    // ...other plugins
    {
      name: 'zod',
      compatibilityVersion: 'mini',
      requests: true, // [!code ++]
    },
  ],
};
```

:::

::: tip
If you need to access individual fields, you can do so using the [`.def.shape`](https://zod.dev/api?id=shape) API. For example, we can get the request body schema with `zData.def.shape.body`.
:::

You can customize the naming and casing pattern for `requests` schemas using the `.name` and `.case` options.

## Responses

A single Zod schema is generated for all endpoint's responses. If the endpoint describes multiple responses, the generated schema is a union of all possible response shapes.

::: code-group

```ts [example]
const zResponse = z.union([
  z.object({
    foo: z.optional(z.string()),
  }),
  z.object({
    bar: z.optional(z.number()),
  }),
]);
```

```js [config]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    // ...other plugins
    {
      name: 'zod',
      compatibilityVersion: 'mini',
      responses: true, // [!code ++]
    },
  ],
};
```

:::

You can customize the naming and casing pattern for `responses` schemas using the `.name` and `.case` options.

## Definitions

A Zod schema is generated for every reusable definition from your input.

::: code-group

```ts [example]
const zFoo = z.int();

const zBar = z.object({
  bar: z.optional(z.array(z.int())),
});
```

```js [config]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    // ...other plugins
    {
      name: 'zod',
      compatibilityVersion: 'mini',
      definitions: true, // [!code ++]
    },
  ],
};
```

:::

You can customize the naming and casing pattern for `definitions` schemas using the `.name` and `.case` options.

## ISO Datetimes

By default, values without a timezone or with a timezone offset are not allowed in the `z.iso.datetime()` method.

### Timezone offsets

You can allow values with timezone offsets by setting `dates.offset` to `true`.

::: code-group

```ts [example]
export const zFoo = z.iso.datetime({ offset: true });
```

```js [config]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    // ...other plugins
    {
      name: 'zod',
      compatibilityVersion: 'mini',
      dates: {
        offset: true, // [!code ++]
      },
    },
  ],
};
```

:::

### Local times

You can allow values without a timezone by setting `dates.local` to `true`.

::: code-group

```ts [example]
export const zFoo = z.iso.datetime({ local: true });
```

```js [config]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    // ...other plugins
    {
      name: 'zod',
      compatibilityVersion: 'mini',
      dates: {
        local: true, // [!code ++]
      },
    },
  ],
};
```

:::

## Metadata

It's often useful to associate a schema with some additional [metadata](https://zod.dev/metadata) for documentation, code generation, AI structured outputs, form validation, and other purposes. If this is your use case, you can set `metadata` to `true` to generate additional metadata about schemas.

::: code-group

```ts [example]
export const zFoo = z.string().register(z.globalRegistry, {
  description: 'Additional metadata',
});
```

```js [config]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    // ...other plugins
    {
      name: 'zod',
      compatibilityVersion: 'mini',
      metadata: true, // [!code ++]
    },
  ],
};
```

:::

## Types

In addition to Zod schemas, you can generate schema-specific types. These can be generated for all schemas or for specific resources.

::: code-group

```ts [example]
export type ResponseZodType = z.infer<typeof zResponse>;
```

```js [config]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    // ...other plugins
    {
      name: 'zod',
      compatibilityVersion: 'mini',
      types: {
        infer: false, // by default, no `z.infer` types [!code ++]
      },
      responses: {
        types: {
          infer: true, // `z.infer` types only for response schemas [!code ++]
        },
      },
    },
  ],
};
```

:::

You can customize the naming and casing pattern for schema-specific `types` using the `.name` and `.case` options.

## Resolvers

You can further customize this plugin's behavior using [resolvers](/openapi-ts/plugins/concepts/resolvers).

## API

You can view the complete list of options in the [UserConfig](https://github.com/hey-api/openapi-ts/blob/main/packages/openapi-ts/src/plugins/zod/types.d.ts) interface.

## Examples

You can view live examples on [StackBlitz](https://stackblitz.com/orgs/github/hey-api/collections/openapi-ts-examples).

## Sponsors

Hey API is sponsor-funded. If you rely on Hey API in production, consider becoming a [sponsor](https://github.com/sponsors/hey-api) to accelerate the roadmap.

---

---
url: /openapi-ts/plugins/zod/v3.md
description: >-
  Generate Zod v3 schemas from OpenAPI with the Zod plugin for openapi-ts. Fully
  compatible with validators, transformers, and all core features.
---

### About

[Zod](https://v3.zod.dev/) is a TypeScript-first schema validation library with static type inference.

The Zod plugin for Hey API generates schemas from your OpenAPI spec, fully compatible with validators, transformers, and all core features.

## Features

* Zod v3 support
* seamless integration with `@hey-api/openapi-ts` ecosystem
* Zod schemas for requests, responses, and reusable definitions
* minimal learning curve thanks to extending the underlying technology

## Installation

In your [configuration](/openapi-ts/get-started), add `zod` to your plugins and you'll be ready to generate Zod artifacts. :tada:

```js
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    // ...other plugins
    {
      name: 'zod', // [!code ++]
      compatibilityVersion: 3, // [!code ++]
    },
  ],
};
```

### SDKs

To add data validators to your SDKs, set `sdk.validator` to `true`.

```js
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    // ...other plugins
    {
      name: 'zod',
      compatibilityVersion: 3,
    },
    {
      name: '@hey-api/sdk', // [!code ++]
      validator: true, // [!code ++]
    },
  ],
};
```

Learn more about data validators in your SDKs on the [SDKs](/openapi-ts/plugins/sdk#validators) page.

## Output

The Zod plugin will generate the following artifacts, depending on the input specification.

## Requests

A single request schema is generated for each endpoint. It may contain a request body, parameters, and headers.

::: code-group

```ts [example]
const zData = z.object({
  body: z
    .object({
      foo: z.string().optional(),
      bar: z.union([z.number(), z.null()]).optional(),
    })
    .optional(),
  path: z.object({
    baz: z.string(),
  }),
  query: z.never().optional(),
});
```

```js [config]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    // ...other plugins
    {
      name: 'zod',
      compatibilityVersion: 3,
      requests: true, // [!code ++]
    },
  ],
};
```

:::

::: tip
If you need to access individual fields, you can do so using the [`.shape`](https://v3.zod.dev/?id=shape) API. For example, we can get the request body schema with `zData.shape.body`.
:::

You can customize the naming and casing pattern for `requests` schemas using the `.name` and `.case` options.

## Responses

A single Zod schema is generated for all endpoint's responses. If the endpoint describes multiple responses, the generated schema is a union of all possible response shapes.

::: code-group

```ts [example]
const zResponse = z.union([
  z.object({
    foo: z.string().optional(),
  }),
  z.object({
    bar: z.number().optional(),
  }),
]);
```

```js [config]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    // ...other plugins
    {
      name: 'zod',
      compatibilityVersion: 3,
      responses: true, // [!code ++]
    },
  ],
};
```

:::

You can customize the naming and casing pattern for `responses` schemas using the `.name` and `.case` options.

## Definitions

A Zod schema is generated for every reusable definition from your input.

::: code-group

```ts [example]
const zFoo = z.number().int();

const zBar = z.object({
  bar: z.array(z.number().int()).optional(),
});
```

```js [config]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    // ...other plugins
    {
      name: 'zod',
      compatibilityVersion: 3,
      definitions: true, // [!code ++]
    },
  ],
};
```

:::

You can customize the naming and casing pattern for `definitions` schemas using the `.name` and `.case` options.

## ISO Datetimes

By default, values without a timezone or with a timezone offset are not allowed in the `z.string().datetime()` method.

### Timezone offsets

You can allow values with timezone offsets by setting `dates.offset` to `true`.

::: code-group

```ts [example]
export const zFoo = z.string().datetime({ offset: true });
```

```js [config]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    // ...other plugins
    {
      name: 'zod',
      compatibilityVersion: 3,
      dates: {
        offset: true, // [!code ++]
      },
    },
  ],
};
```

:::

### Local times

You can allow values without a timezone by setting `dates.local` to `true`.

::: code-group

```ts [example]
export const zFoo = z.string().datetime({ local: true });
```

```js [config]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    // ...other plugins
    {
      name: 'zod',
      compatibilityVersion: 3,
      dates: {
        local: true, // [!code ++]
      },
    },
  ],
};
```

:::

## Metadata

It's often useful to associate a schema with some additional [metadata](https://v3.zod.dev/?id=describe) for documentation, code generation, AI structured outputs, form validation, and other purposes. If this is your use case, you can set `metadata` to `true` to generate additional metadata about schemas.

::: code-group

```ts [example]
export const zFoo = z.string().describe('Additional metadata');
```

```js [config]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    // ...other plugins
    {
      name: 'zod',
      compatibilityVersion: 3,
      metadata: true, // [!code ++]
    },
  ],
};
```

:::

## Types

In addition to Zod schemas, you can generate schema-specific types. These can be generated for all schemas or for specific resources.

::: code-group

```ts [example]
export type ResponseZodType = z.infer<typeof zResponse>;
```

```js [config]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    // ...other plugins
    {
      name: 'zod',
      compatibilityVersion: 3,
      types: {
        infer: false, // by default, no `z.infer` types [!code ++]
      },
      responses: {
        types: {
          infer: true, // `z.infer` types only for response schemas [!code ++]
        },
      },
    },
  ],
};
```

:::

You can customize the naming and casing pattern for schema-specific `types` using the `.name` and `.case` options.

## Resolvers

You can further customize this plugin's behavior using [resolvers](/openapi-ts/plugins/concepts/resolvers).

## API

You can view the complete list of options in the [UserConfig](https://github.com/hey-api/openapi-ts/blob/main/packages/openapi-ts/src/plugins/zod/types.d.ts) interface.

## Examples

You can view live examples on [StackBlitz](https://stackblitz.com/orgs/github/hey-api/collections/openapi-ts-examples).

## Sponsors

Hey API is sponsor-funded. If you rely on Hey API in production, consider becoming a [sponsor](https://github.com/sponsors/hey-api) to accelerate the roadmap.

---

---
url: /openapi-ts/plugins/zod.md
description: >-
  Generate Zod v4 schemas from OpenAPI with the Zod plugin for openapi-ts. Fully
  compatible with validators, transformers, and all core features.
---

### About

[Zod](https://zod.dev) is a TypeScript-first schema validation library with static type inference.

The Zod plugin for Hey API generates schemas from your OpenAPI spec, fully compatible with validators, transformers, and all core features.

## Features

* Zod v4 support
* seamless integration with `@hey-api/openapi-ts` ecosystem
* Zod schemas for requests, responses, and reusable definitions
* minimal learning curve thanks to extending the underlying technology

## Installation

In your [configuration](/openapi-ts/get-started), add `zod` to your plugins and you'll be ready to generate Zod artifacts. :tada:

```js
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    // ...other plugins
    'zod', // [!code ++]
  ],
};
```

### SDKs

To add data validators to your SDKs, set `sdk.validator` to `true`.

```js
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    // ...other plugins
    'zod',
    {
      name: '@hey-api/sdk', // [!code ++]
      validator: true, // [!code ++]
    },
  ],
};
```

Learn more about data validators in your SDKs on the [SDKs](/openapi-ts/plugins/sdk#validators) page.

## Output

The Zod plugin will generate the following artifacts, depending on the input specification.

## Requests

A single request schema is generated for each endpoint. It may contain a request body, parameters, and headers.

::: code-group

```ts [example]
const zData = z.object({
  body: z
    .object({
      foo: z.optional(z.string()),
      bar: z.optional(z.union([z.number(), z.null()])),
    })
    .optional(),
  path: z.object({
    baz: z.string(),
  }),
  query: z.optional(z.never()),
});
```

```js [config]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    // ...other plugins
    {
      name: 'zod',
      requests: true, // [!code ++]
    },
  ],
};
```

:::

::: tip
If you need to access individual fields, you can do so using the [`.shape`](https://zod.dev/api?id=shape) API. For example, we can get the request body schema with `zData.shape.body`.
:::

You can customize the naming and casing pattern for `requests` schemas using the `.name` and `.case` options.

## Responses

A single Zod schema is generated for all endpoint's responses. If the endpoint describes multiple responses, the generated schema is a union of all possible response shapes.

::: code-group

```ts [example]
const zResponse = z.union([
  z.object({
    foo: z.optional(z.string()),
  }),
  z.object({
    bar: z.optional(z.number()),
  }),
]);
```

```js [config]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    // ...other plugins
    {
      name: 'zod',
      responses: true, // [!code ++]
    },
  ],
};
```

:::

You can customize the naming and casing pattern for `responses` schemas using the `.name` and `.case` options.

## Definitions

A Zod schema is generated for every reusable definition from your input.

::: code-group

```ts [example]
const zFoo = z.int();

const zBar = z.object({
  bar: z.optional(z.array(z.int())),
});
```

```js [config]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    // ...other plugins
    {
      name: 'zod',
      definitions: true, // [!code ++]
    },
  ],
};
```

:::

You can customize the naming and casing pattern for `definitions` schemas using the `.name` and `.case` options.

## ISO Datetimes

By default, values without a timezone or with a timezone offset are not allowed in the `z.iso.datetime()` method.

### Timezone offsets

You can allow values with timezone offsets by setting `dates.offset` to `true`.

::: code-group

```ts [example]
export const zFoo = z.iso.datetime({ offset: true });
```

```js [config]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    // ...other plugins
    {
      name: 'zod',
      dates: {
        offset: true, // [!code ++]
      },
    },
  ],
};
```

:::

### Local times

You can allow values without a timezone by setting `dates.local` to `true`.

::: code-group

```ts [example]
export const zFoo = z.iso.datetime({ local: true });
```

```js [config]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    // ...other plugins
    {
      name: 'zod',
      dates: {
        local: true, // [!code ++]
      },
    },
  ],
};
```

:::

## Metadata

It's often useful to associate a schema with some additional [metadata](https://zod.dev/metadata) for documentation, code generation, AI structured outputs, form validation, and other purposes. If this is your use case, you can set `metadata` to `true` to generate additional metadata about schemas.

::: code-group

```ts [example]
export const zFoo = z.string().register(z.globalRegistry, {
  description: 'Additional metadata',
});
```

```js [config]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    // ...other plugins
    {
      name: 'zod',
      metadata: true, // [!code ++]
    },
  ],
};
```

:::

## Types

In addition to Zod schemas, you can generate schema-specific types. These can be generated for all schemas or for specific resources.

::: code-group

```ts [example]
export type ResponseZodType = z.infer<typeof zResponse>;
```

```js [config]
export default {
  input: 'hey-api/backend', // sign up at app.heyapi.dev
  output: 'src/client',
  plugins: [
    // ...other plugins
    {
      name: 'zod',
      types: {
        infer: false, // by default, no `z.infer` types [!code ++]
      },
      responses: {
        types: {
          infer: true, // `z.infer` types only for response schemas [!code ++]
        },
      },
    },
  ],
};
```

:::

You can customize the naming and casing pattern for schema-specific `types` using the `.name` and `.case` options.

## Resolvers

You can further customize this plugin's behavior using [resolvers](/openapi-ts/plugins/concepts/resolvers).

## API

You can view the complete list of options in the [UserConfig](https://github.com/hey-api/openapi-ts/blob/main/packages/openapi-ts/src/plugins/zod/types.d.ts) interface.

## Examples

You can view live examples on [StackBlitz](https://stackblitz.com/orgs/github/hey-api/collections/openapi-ts-examples).

## Sponsors

Hey API is sponsor-funded. If you rely on Hey API in production, consider becoming a [sponsor](https://github.com/sponsors/hey-api) to accelerate the roadmap.

---

---
url: /openapi-ts/plugins/zustand.md
description: Zustand plugin for Hey API. Compatible with all our features.
---

# Zustand soon

### About

[Zustand](https://zustand-demo.pmnd.rs) is a small, fast, and scalable bearbones state management solution.

## Sponsors

Hey API is sponsor-funded. If you rely on Hey API in production, consider becoming a [sponsor](https://github.com/sponsors/hey-api) to accelerate the roadmap.
