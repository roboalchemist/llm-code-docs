# Source: https://docs.upsun.com/languages/nodejs.md

# JavaScript/Node.js


p:last-child]:mb-0 [&>h3]:mt-0 rounded-lg" >

### Note
You can now use composable image to install runtimes and tools in your application container. To find out more, see the [Composable image](https://docs.upsun.com/create-apps/app-reference/composable-image.md) topic.

Node.js is a popular asynchronous JavaScript runtime.
Deploy scalable Node.js apps of all sizes on Upsun.
You can also develop a microservice architecture mixing JavaScript and other apps with [multi-app projects](https://docs.upsun.com../../create-apps/multi-app.md).

## Supported versions

You can select the major version. But the latest compatible minor version is applied automatically and can’t be overridden.

Patch versions are applied periodically for bug fixes and the like. When you deploy your app, you always get the latest available patches.

   - 24

   - 22

   - 20

### Specify the language

To use Node.js, specify ``nodejs`` as your [app’s type](https://docs.upsun.com/create-apps/app-reference/single-runtime-image.md#types):

```yaml  {location=".upsun/config.yaml"}
applications:
  # The app's name, which must be unique within the project.
  <APP_NAME>:
    type: 'nodejs:<VERSION_NUMBER>'
```

For example:

```yaml  {location=".upsun/config.yaml"}
applications:
  # The app's name, which must be unique within the project.
  myapp:
    type: 'nodejs:24'
```

To use a specific version in a container with a different language, [use a version manager](node-version.md).

### Deprecated versions

The following versions are [deprecated](https://docs.upsun.com/glossary.md#deprecated-versions).
They're available, but they don't receive security updates from upstream and aren't guaranteed to work.
They'll be removed in the future – consider migrating to a [supported version](#supported-versions).

   - 18

   - 16

   - 8.9

   - 6.10

   - 6.9

   - 6.8

   - 6.6

   - 6.3

   - 6.2

   - 4.7

   - 4.6

   - 4.5

   - 4.4

   - 4.3

   - 4.2

## Usage example

To use JavaScript with Node.js on Upsun, configure your [app configuration](https://docs.upsun.com../../create-apps.md)
(a complete example is included at the end).

### 1. Specify the version

Choose a version from the [list of supported versions](#supported-versions)
and add it to your app configuration:

```yaml  {location=".upsun/config.yaml"}
applications:
  # The app's name, which must be unique within the project.
  myapp:
    type: 'nodejs:24'
```

### 2. Specify any global dependencies

Add the following to your app configuration:

```yaml  {location=".upsun/config.yaml"}
applications:
  # The app's name, which must be unique within the project.
  myapp:
    type: 'nodejs:24'
    dependencies:
      nodejs:
        sharp: "*"
```

These are now available as commands, the same as installing with `npm install -g`.

### 3. Build your app

Include any commands needed to build and setup your app in the `hooks`, as in the following example:

```yaml  {location=".upsun/config.yaml"}
applications:
  # The app's name, which must be unique within the project.
  myapp:
    type: 'nodejs:24'
    dependencies:
      nodejs:
        sharp: "*"
    hooks:
      build: |
        npm run setup-assets
        npm run build
```

### 4. Start your app

Specify a command to start serving your app (it must be a process running in the foreground):

```yaml  {location=".upsun/config.yaml"}
applications:
  # The app's name, which must be unique within the project.
  myapp:
    type: 'nodejs:24'
    dependencies:
      nodejs:
        sharp: "*"
    hooks:
      build: |
        npm run setup-assets
        npm run build
    web:
      commands:
        start: node index.js
```

### 5. Listen on the right port

Make sure your Node.js application is configured to listen over the port given by the environment.

```js
// Load the http module to create an http server.
const http = require('http');
const PORT = process.env.PORT || 8888;

const server = http.createServer(function (request, response) {
    response.writeHead(200, {"Content-Type": "application/json"});
    response.end("Hello world!");
});

// Listen on the port from the Upsun configuration
server.listen(PORT, () => {
  console.log(`Server is listening on port: ${PORT}`);
});
```
### Complete example

A complete basic app configuration looks like the following:

```yaml  {location=".upsun/config.yaml"}
applications:
  # The app's name, which must be unique within the project.
  'node-app':
    type: 'nodejs:24'
    dependencies:
      nodejs:
        sharp: "*"
    hooks:
      build: |
        npm run setup-assets
        npm run build
    web:
      commands:
        start: "node index.js"
```

## Dependencies

By default, Upsun assumes you're using npm as a package manager.
If your code has a `package.json`, the following command is run as part of the default [build flavor](https://docs.upsun.com/create-apps/app-reference/single-runtime-image.md#build):

```bash
npm prune --userconfig .npmrc && npm install --userconfig .npmrc
```

This means you can specify configuration in a `.npmrc` file in [your app root](https://docs.upsun.com/create-apps/app-reference/single-runtime-image.md#root-directory).

### Use Yarn as a package manager

To switch to Yarn to manage dependencies, follow these steps:

1. Turn off the default use of npm:

```yaml  {location=".upsun/config.yaml"}
applications:
  # The app's name, which must be unique within the project.
  myapp:
    type: 'nodejs:24'
    build:
      flavor: none
```

2. Specify the version of Yarn you want:

   ```json  {location="package.json"}
   {
     ...
     "packageManager": "yarn@3.2.1"
   }
   ```

What you do next depends on the versions of Yarn and Node.js you want.

```yaml {}
applications:
  # The name of the app container. Must be unique within a project.
  myapp:
    # The location of the application's code.
    source:
      root: "/"
    type: 'nodejs:24'
    hooks:
      build: |
        corepack yarn install        
```

 - Enable Corepack (which is opt-in):

    .upsun/config.yaml

```yaml {}
applications:
  # The name of the app container. Must be unique within a project.
  myapp:
    # The location of the application's code.
    source:
      root: "/"
    type: 'nodejs:24'
    dependencies:
      nodejs:
        corepack: "*"
```

 - Use Corepack to run Yarn in your build hook:

    .upsun/config.yaml

```yaml {}
applications:
  # The name of the app container. Must be unique within a project.
  myapp:
    # The location of the application's code.
    source:
      root: "/"
    type: 'nodejs:24'
    hooks:
      build: |
        corepack yarn install        
```

 - Add Yarn as a global dependency:

    .upsun/config.yaml

```yaml {}
applications:
  # The name of the app container. Must be unique within a project.
  myapp:
    # The location of the application's code.
    source:
      root: "/"
    type: 'nodejs:24'
    dependencies:
      nodejs:
        yarn: "1.22.19"
```

 - Install dependencies in the ``build`` hook:

    .upsun/config.yaml

```yaml {}
applications:
  # The name of the app container. Must be unique within a project.
  myapp:
    # The location of the application's code.
    source:
      root: "/"
    type: 'nodejs:24'
    hooks:
      build: |
        yarn --frozen-lockfile        
```

### Use Bun as a package manager

  **Availability**

  [Bun is available as a runtime and package manager](https://devcenter.upsun.com/posts/bun-support-is-here/) for Node.js **versions 20 or above**.

To switch to Bun to manage dependencies,
use the following configuration:

```yaml  {location=".upsun/config.yaml"}
applications:
  # The name of your app.
  myapp:
  # Choose Node.js version 20 or above.
    type: 'nodejs:20'
    # Override the default Node.js build flavor.
    build:
      flavor: none
    # Use Bun to install the dependencies.
    hooks:
      build: bun install
```

#### Use Bun as a runtime

You can even [use Bun as a runtime](https://devcenter.upsun.com/posts/bun-support-is-here/) by adjusting the `start` command as follows:

```yaml  {location=".upsun/config.yaml"}
applications:
  # The name of your app.
  myapp:
    # Choose Node.js version 20 or above.
    type: 'nodejs:20'
    # Override the default Node.js build flavor.
    build:
      flavor: none
    # Use Bun to install the dependencies.
    hooks:
      build: bun install
    # In the start command replace node with Bun.
    web:
      commands:
        start: 'bun app.js'
```

## Connecting to services

You can access service credentials to connect to [managed services](https://docs.upsun.com/add-services/) from environment variables present in the application container.
Consult each of the individual service documentation to see how to retrieve and surface credentials into your application.

- [Chroma](https://docs.upsun.com/add-services/chroma.md#3-use-the-relationship-in-your-application)

- [ClickHouse](https://docs.upsun.com/add-services/clickhouse.md#usage-example)

- [Elasticsearch](https://docs.upsun.com/add-services/elasticsearch.md#use-in-app)

- [Edgee (Edge Analytics)](https://docs.upsun.com/add-services/edgee.md#setup-edgee)

- [Gotenberg](https://docs.upsun.com/add-services/gotenberg.md#usage-example)

- [Headless Chrome](https://docs.upsun.com/add-services/headless-chrome.md#use-in-app)

- [InfluxDB](https://docs.upsun.com/add-services/influxdb.md#use-in-app)

- [Kafka](https://docs.upsun.com/add-services/kafka.md#use-in-app)

- [MariaDB/MySQL](https://docs.upsun.com/add-services/mysql.md#use-in-app)

- [Memcached](https://docs.upsun.com/add-services/memcached.md#use-in-app)

- [Mercure](https://docs.upsun.com/add-services/mercure.md#use-in-app)

- [MongoDB](https://docs.upsun.com/add-services/mongodb.md#use-in-app)

- [Network Storage](https://docs.upsun.com/add-services/network-storage.md#usage-example)

- [OpenSearch](https://docs.upsun.com/add-services/opensearch.md#use-in-app)

- [PostgreSQL](https://docs.upsun.com/add-services/postgresql.md#use-in-app)

- [Qdrant](https://docs.upsun.com/add-services/qdrant.md#4-use-the-relationship-in-your-application)

- [RabbitMQ](https://docs.upsun.com/add-services/rabbitmq.md#use-in-app)

- [Redis](https://docs.upsun.com/add-services/redis.md#use-in-app)

- [Solr](https://docs.upsun.com/add-services/solr.md#use-in-app)

- [Valkey](https://docs.upsun.com/add-services/valkey.md#use-in-app)

- [Varnish](https://docs.upsun.com/add-services/varnish.md#usage-example)

- [Vault KMS](https://docs.upsun.com/add-services/vault.md#use-vault-kms)

## Frameworks

All major Javascript/Node.js web frameworks can be deployed on Upsun.
See dedicated guides for deploying and working with them:

- [Express](https://docs.upsun.com/get-started/stacks/express.md)
- [Next.js](https://docs.upsun.com/get-started/stacks/nextjs.md)
- [Strapi](https://docs.upsun.com/get-started/stacks/strapi.md)

