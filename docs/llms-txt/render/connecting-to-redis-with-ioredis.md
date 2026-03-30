# Source: https://render.com/docs/connecting-to-redis-with-ioredis.md

# Connect to Render Key Value with ioredis

This guide walks through connecting to a [Render Key Value](key-value) instance with [ioredis](https://github.com/luin/ioredis), the popular Node.js Redis client.

> We recommend using the latest version of ioredis. This guide assumes a minimum version of `5.0.0`.

## Key Value setup

1. Create a Render Key Value instance with [these steps](key-value#create-your-key-value-instance).
2. Obtain your instance's internal URL from its *Connect* menu in the [Render Dashboard](https://dashboard.render.com).
   - You can use this URL to connect to your instance from your other services in the same region.

> If you want to connect to your instance from outside Render (for testing, dev environments, etc.), you also need to [enable external connections](key-value#enabling-external-connections) and add the IP addresses you want to connect from. After you do, you can view your instance's external URL.

## Configure ioredis

Next, we'll provide our ioredis client with connection details for our Render Key Value instance.

> We strongly recommend storing connection details in [environment variables](configure-environment-variables), such as `REDIS_URL`.

### Connecting via URL

We recommend configuring ioredis by passing in the provided internal or external Key Value URL. When used in Blueprints, you can pass this URL to your services using the `fromService` syntax ([docs](blueprint-spec#environment-variables)).

```javascript
const Redis = require('ioredis')

const { REDIS_URL } = process.env
// Internal URL example:
// "redis://red-xxxxxxxxxxxxxxxxxxxx:6379"
// External URL is slightly different:
// "rediss://red-xxxxxxxxxxxxxxxxxxxx:PASSWORD@HOST:6379"

const keyValueClient = new Redis(REDIS_URL)

keyValueClient.set('animal', 'cat')

keyValueClient.get('animal').then((result) => {
  console.log(result) // Prints "cat"
})
```

### Setting detailed connection config

To explicitly configure ioredis you can use the following examples:

#### Internal connection

```javascript
const Redis = require('ioredis')

// Internal URL, extract the details into environment variables.
// "redis://red-xxxxxxxxxxxxxxxxxxxx:6379"

const keyValueClient = new Redis({
  host: process.env.REDIS_SERVICE_NAME, // Render Key Value service name, red-xxxxxxxxxxxxxxxxxxxx
  port: process.env.REDIS_PORT || 6379, // Key Value port
})
```

#### External connection

```javascript
const Redis = require('ioredis')

// External Key Value URL, extract the details into environment variables.
// "rediss://red-xxxxxxxxxxxxxxxxxxxx:PASSWORD@HOST:6379"

const keyValueClient = new Redis({
  username: process.env.REDIS_SERVICE_NAME, // Key Value name, red-xxxxxxxxxxxxxxxxxxxx
  host: process.env.REDIS_HOST, // Key Value hostname, REGION-kv.render.com
  password: process.env.REDIS_PASSWORD, // Provided password
  port: process.env.REDIS_PORT || 6379, // Connection port
  tls: true, // TLS required when externally connecting to Key Value
})
```

## Code examples

[Full examples for ioredis](https://github.com/render-examples/ioredis) of the above are available in our [Render Examples](https://github.com/render-examples) repo.