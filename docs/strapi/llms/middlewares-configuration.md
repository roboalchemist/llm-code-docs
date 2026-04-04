# Middlewares configuration

</Tabs>

:::tip
If you aren't sure where to place a middleware in the stack, add it to the end of the list.
:::

## Naming conventions

Global middlewares can be classified into different types depending on their origin, which defines the following naming conventions:

| Middleware type   | Origin                                                                                                                                                                                                                                  | Naming convention                                                                                                    |
|-------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| Internal          | Built-in middlewares (i.e. included with Strapi), automatically loaded                                                                                                                                                                  | `strapi::middleware-name`                                                                                            |
| Application-level | Loaded from the `./src/middlewares` folder                                                                                                                                                                                              | `global::middleware-name`                                                                                            |
| API-level         | Loaded from the `./src/api/[api-name]/middlewares` folder                                                                                                                                                                               | `api::api-name.middleware-name`                                                                                      |
| Plugin            | Exported from `strapi-server.js` in the [`middlewares` property of the plugin interface](/cms/plugins-development/server-api#middlewares)                                                                                               | `plugin::plugin-name.middleware-name`                                                                                |
| External          | Can be:<ul><li>either node modules installed with 

</Tabs>

</details>

### `compression`

The `compression` middleware is based on 

</Tabs>

</details>

### `cors`

This security middleware is about cross-origin resource sharing (CORS) and is based on 

</Tabs>

</details>

<details>
<summary> Example: Custom configuration for the cors middleware within a function as parameter</summary>

`origin` can take a Function as parameter following this signature 

```ts title="./config/middlewares.ts"

  // ...
  {
    name: 'strapi::cors',
    config: {
      origin: (ctx): string | string[] => {
        const origin = ctx.request.header.origin;
        if (origin === 'http://localhost:3000') {
          return origin; // The returns will be part of the Access-Control-Allow-Origin header
        }
        
        return ''; // Fail cors check
      }
    },
  },
  // ...
]
```

</details>

### `errors`

The errors middleware handles [errors](/cms/error-handling.md) thrown by the code. Based on the type of error it sets the appropriate HTTP status to the response. By default, any error not supposed to be exposed to the end user will result in a 500 HTTP response.

The middleware doesn't have any configuration options.

### `favicon`

The `favicon` middleware serves the favicon and is based on 

</Tabs>

</details>

#### `ip`

The `ip` middleware is an IP filter middleware based on 

</Tabs>

</details>

### `logger`

The `logger` middleware is used to log requests.

To define a custom configuration for the `logger` middleware, create a dedicated configuration file (`./config/logger.js`). It should export an object that must be a complete or partial 

</Tabs>

</details>

### `poweredBy`

The `poweredBy` middleware adds a `X-Powered-By` parameter to the response header. It accepts the following options:

| Option      | Description                        | Type     | Default value          |
|-------------|------------------------------------|----------|------------------------|
| `poweredBy` | Value of the `X-Powered-By` header | `String` | `'Strapi <strapi.io>'` |

<details>
<summary> details Example: Custom configuration for the poweredBy middleware</summary>

</Tabs>

</details>

### `query`

The `query` middleware is a query parser based on 

</Tabs>

</details>

### `response-time`

The `response-time` middleware enables the `X-Response-Time` (in milliseconds) for the response header.

The middleware doesn't have any configuration options.

### `public`

The `public` middleware is a static file serving middleware, based on 

</Tabs>

</details>

### `security`

The security middleware is based on 

</Tabs>

</details>

### `session`

The `session` middleware allows the use of cookie-based sessions, based on 

</Tabs>

</details>