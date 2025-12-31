# Source: https://docs.upsun.com/languages/go.md

# Go


p:last-child]:mb-0 [&>h3]:mt-0 rounded-lg" >

### Note
You can now use composable image (BETA) to install runtimes and tools in your application container. To find out more, see the [dedicated documentation page](https://docs.upsun.com/create-apps/app-reference/composable-image.md).

Upsun supports building and deploying applications written in Go using Go modules. They’re compiled during the Build hook phase, and support both committed dependencies and download-on-demand.

## Supported versions

You can select the major and minor version.

Patch versions are applied periodically for bug fixes and the like.
When you deploy your app, you always get the latest available patches.

   - 1.25

   - 1.24

   - 1.23

   - 1.22

   - 1.21

   - 1.20

### Specify the language

To use Go, specify `golang` as your [app's `type`](https://docs.upsun.com/create-apps/app-reference/single-runtime-image.md#types):

```yaml  {location=".upsun/config.yaml"}
applications:
  # The app's name, which must be unique within the project.
  <APP_NAME>:
    type: 'golang:<VERSION_NUMBER>'
```

For example:

```yaml  {location=".upsun/config.yaml"}
applications:
  # The app's name, which must be unique within the project.
  myapp:
    type: 'golang:1.25'
```

### Deprecated versions

The following versions are [deprecated](https://docs.upsun.com/glossary.md#deprecated-versions).
They're available, but they don't receive security updates from upstream and aren't guaranteed to work.
They'll be removed in the future – consider migrating to a [supported version](#supported-versions).

   - 1.19

   - 1.18

   - 1.17

   - 1.16

   - 1.15

   - 1.14

   - 1.13

   - 1.12

   - 1.11

   - 1.10

   - 1.9

   - 1.8

## Go toolchain auto download

Even though you select a specific version of Go, starting in Go 1.21, the `go` command will automatically download and use a different toolchain version as requested by the `toolchain` directive in `go.mod`, or the `GOTOOLCHAIN` environmental variable (see [Go Toolchains](https://go.dev/doc/toolchain)).

**Note**: 

Still, it is important to keep your chosen version of Go updated in your yaml configuration file. This will ensure that you are using the most up to date software for your projects.

## Go modules

The recommended way to handle Go dependencies on Upsun is using Go module support in Go 1.11 and later. That allows the build process to use `go build` directly without any extra steps, and you can specify an output executable file of your choice. (See the examples below.)

## Building and running the application

Assuming your `go.mod` and `go.sum` files are present in your repository, your application can be built with the command `go build`, to produce a working executable. You can then start it from the `web.commands.start` directive. Note that the start command _must_ run in the foreground. If the program terminates for any reason it is automatically restarted.

The following basic `.upsun/config.yaml` file is sufficient to run most Go applications.

```yaml  {location=".upsun/config.yaml"}
applications:
  # The app's name, which must be unique within the project.
  myapp:
    type: 'golang:1.25'

    hooks:
      build: |
        # Modify this line if you want to build differently or
        # use an alternate name for your executable.
        go build -o bin/app

    web:
      upstream:
        socket_family: tcp
        protocol: http

      commands:
        # If you change the build output in the build hook above, update this line as well.
        start: ./bin/app

      locations:
        /:
          # Route all requests to the Go app, unconditionally.
          allow: false
          passthru: true
```

Note that there is still an Nginx proxy server sitting in front of your application.
If desired, certain paths may be served directly by Nginx without hitting your application (for static files, primarily)
or you may route all requests to the Go application unconditionally, as in the example above.

## Accessing services

To access various [services](https://docs.upsun.com../add-services.md) with Go, see the following examples. The individual service pages have more information on configuring each service.

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


