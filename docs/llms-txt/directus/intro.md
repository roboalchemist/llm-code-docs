# Source: https://directus.io/docs/raw/configuration/intro.md

# Configuration Options

> Environment variables are used for all configuration within a Directus project. These variables can be defined in a
> number of ways, which we cover below.

## Configuration Files

By default, Directus will read the `.env` file located next to your project's `package.json` (typically in the root
folder of your project) for its configuration. You can change this path and filename by setting the `CONFIG_PATH`
environment variable before starting Directus. For example:

```bash
CONFIG_PATH="/path/to/config.js" npx directus start
```

In case you prefer using a configuration file instead of environment variables, you can also use the `CONFIG_PATH`
environment variable to instruct Directus to use a local configuration file instead of environment variables. The config
file can be one of the following formats:

- [.env](#env)
- [config.json](#config-json)
- [config.yaml](#config-yaml)
- [config.js](#config-js)

### .env

If the config path has no file extension, or a file extension that's not one of the other supported formats, Directus
will try reading the file config path as environment variables. This has the following structure:

```text
HOST="0.0.0.0"
PORT=8055

DB_CLIENT="pg"
DB_HOST="localhost"
DB_PORT=5432

etc
```

### config.json

If you prefer a single JSON file for your configuration, create a JSON file with the environment variables as keys, for
example:

```text
CONFIG_PATH="/path/to/config.json"
```

```json
{
  "HOST": "0.0.0.0",
  "PORT": 8055,

  "DB_CLIENT": "pg",
  "DB_HOST": "localhost",
  "DB_PORT": 5432

  // etc
}
```

### config.yaml

Similar to JSON, you can use a `.yaml` (or `.yml`) file for your config:

```text
CONFIG_PATH="/path/to/config.yaml"
```

```yaml
HOST: 0.0.0.0
PORT: 8055

DB_CLIENT: pg
DB_HOST: localhost
DB_PORT: 5432
#
# etc
```

### config.js

Using a JavaScript file for your config allows you to dynamically generate the configuration of the project during
startup.

By default, the file is expected to be a ESM, while CommonJS is supported too by using `.cjs` as the file extension.

The JavaScript configuration supports two different formats, either an **Object Structure** where the key is the
environment variable name:

<code-group>

```js [config.js]
export default {
  HOST: "0.0.0.0",
  PORT: 8055,

  DB_CLIENT: "pg",
  DB_HOST: "localhost",
  DB_PORT: 5432,

  // etc
};
```

```js [config.cjs]
module.exports = {
  HOST: "0.0.0.0",
  PORT: 8055,

  DB_CLIENT: "pg",
  DB_HOST: "localhost",
  DB_PORT: 5432,

  // etc
};
```

</code-group>

Or a **Function Structure** that *returns* the same object format as above. The function gets `process.env` as its
parameter.

<code-group>

```js [config.js]
export default function (env) {
  return {
    HOST: "0.0.0.0",
    PORT: 8055,

    DB_CLIENT: "pg",
    DB_HOST: "localhost",
    DB_PORT: 5432,

    // etc
  };
}
```

```js [config.cjs]
module.exports = function (env) {
  return {
    HOST: "0.0.0.0",
    PORT: 8055,

    DB_CLIENT: "pg",
    DB_HOST: "localhost",
    DB_PORT: 5432,

    // etc
  };
};
```

</code-group>

## Environment Variable Files

Any of the environment variable values can be imported from a file, by appending `_FILE` to a [Directus environment variable name](https://github.com/directus/directus/blob/main/packages/env/src/constants/directus-variables.ts). This is especially useful when used in conjunction with Docker Secrets, so you can keep sensitive data out of your compose files. For example:

```text
DB_PASSWORD_FILE="/run/secrets/db_password"
```

## Type Casting and Nesting

Environment variables are automatically type cast based on the structure of the variable, for example:

```text
PUBLIC_URL="https://example.com"
// "https://example.com"

DB_HOST="3306"
// 3306

CORS_ENABLED="false"
// false

STORAGE_LOCATIONS="s3,local,example"
// ["s3", "local", "example"]
```

In cases where the environment variables are converted to a configuration object for third party library use, like in
`DB_*` or `REDIS_*`, the environment variable will be converted to camelCase. You can use a double underscore (`__`) for
nested objects:

```text
DB_CLIENT="pg"
DB_CONNECTION_STRING="postgresql://postgres:example@127.0.0.1"
DB_SSL__REJECT_UNAUTHORIZED="false"

{
    client: "pg",
    connectionString: "postgresql://postgres:example@127.0.0.1",
    ssl: {
        rejectUnauthorized: false
    }
}
```

## Environment Syntax Prefix

Directus will attempt to [automatically type cast environment variables](#type-casting-and-nesting) based on context
clues. If you have a specific need for a given type, you can tell Directus what type to use for the given value by
prefixing the value with `{type}:`. The following types are available:

<table>
<thead>
  <tr>
    <th>
      Syntax Prefix
    </th>
    
    <th>
      Example
    </th>
    
    <th>
      Output
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        string
      </code>
    </td>
    
    <td>
      <code>
        string:value
      </code>
    </td>
    
    <td>
      <code>
        "value"
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        number
      </code>
    </td>
    
    <td>
      <code>
        number:3306
      </code>
    </td>
    
    <td>
      <code>
        3306
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        regex
      </code>
    </td>
    
    <td>
      <code>
        regex:\.example\.com$
      </code>
    </td>
    
    <td>
      <code>
        /\.example\.com$/
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        array
      </code>
    </td>
    
    <td>
      <code>
        array:https://example.com,https://example2.com
      </code>
      
       <br />
      
       <code>
        array:string:https://example.com,regex:\.example3\.com$
      </code>
    </td>
    
    <td>
      <code>
        ["https://example.com", "https://example2.com"]
      </code>
      
       <br />
      
       <code>
        ["https://example.com", /\.example3\.com$/]
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        json
      </code>
    </td>
    
    <td>
      <code>
        json:{"items": ["example1", "example2"]}
      </code>
    </td>
    
    <td>
      <code>
        {"items": ["example1", "example2"]}
      </code>
    </td>
  </tr>
</tbody>
</table>

Explicit casting is also available when reading from a file with the `_FILE` suffix.
