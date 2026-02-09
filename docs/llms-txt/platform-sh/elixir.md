# Source: https://docs.upsun.com/languages/elixir.md

# Elixir


p:last-child]:mb-0 [&>h3]:mt-0 rounded-lg" >

### Note
You can now use composable image to install runtimes and tools in your application container. To find out more, see the [Composable image](https://docs.upsun.com/create-apps/app-reference/composable-image.md) topic.

Upsun supports building and deploying applications written in Elixir. There is no default flavor for the build phase, but you can define it explicitly in your build hook. Upsun Elixir images support both committed dependencies and download-on-demand. The underlying Erlang version is 22.0.7.

## Supported versions

You can select the major and minor version.

Patch versions are applied periodically for bug fixes and the like.
When you deploy your app, you always get the latest available patches.

   - 1.18

   - 1.15

### Specify the language

To use Elixir, specify `elixir` as your [app's `type`](https://docs.upsun.com/create-apps/app-reference/single-runtime-image.md#types):

```yaml  {location=".upsun/config.yaml"}
applications:
  # The app's name, which must be unique within the project.
  <APP_NAME>:
    type: 'elixir:<VERSION_NUMBER>'
```

For example:

```yaml  {location=".upsun/config.yaml"}
applications:
  # The app's name, which must be unique within the project.
  myapp:
    type: 'elixir:1.18'
```

## Built-in variables

Upsun exposes relationships and other configuration as [environment variables](https://docs.upsun.com../development/variables.md).
Most notably, it allows a program to determine at runtime what HTTP port it should listen on
and what the credentials are to access [other services](https://docs.upsun.com../add-services.md).

To get the `PORT` environment variable (the port on which your web application is supposed to listen) you would:

```elixir
String.to_integer(System.get_env("PORT") || "8888")
```

Some of the environment variables are in JSON format and are base64 encoded. You would need to import a JSON parsing library such as [JSON](https://hexdocs.pm/json/readme.md) or [Poison](https://hexdocs.pm/poison/api-reference.md) to read those. (There is an example for doing this to decode the `PLATFORM_RELATIONSHIPS` environment variable in the section [below](#accessing-services-manually).)

**Tip**: 

Remember ``config/prod.exs`` is evaluated at **build time** and has no access to runtime configuration. Use ``config/releases.exs`` to configure your runtime environment.

## Building and running the application

If you are using Hex to manage your dependencies, you need to specify the `MIX_ENV` environment variable:

```yaml  {location=".upsun/config.yaml"}
applications:
  myapp:
    type: 'elixir:1.18'
    variables:
      env:
        MIX_ENV: 'prod'
```
The `SECRET_KEY_BASE` variable is generated automatically based on the [`PLATFORM_PROJECT_ENTROPY` variable](https://docs.upsun.com../development/variables/use-variables.md#use-provided-variables).
You can change it.

Include in your build hook the steps to retrieve a local Hex and `rebar`, and then run `mix do deps.get, deps.compile, compile` on your application to build a binary.

```yaml  {location=".upsun/config.yaml"}
applications:
  myapp:
    type: 'elixir:1.18'
    hooks:
      build: |
        mix local.hex --force
        mix local.rebar --force
        mix do deps.get --only prod, deps.compile, compile
```

**Note**: 

That build hook works for most cases and assumes that your ``mix.exs`` file is located at [your app root](https://docs.upsun.com/create-apps/app-reference/single-runtime-image.md#root-directory).

Assuming `mix.exs` is present at your app root and your build hook matches the above,
you can then start it from the `web.commands.start` directive.

The following basic app configuration is sufficient to run most Elixir applications.

```yaml  {location=".upsun/config.yaml"}
applications:
  myapp:
    type: 'elixir:1.18'

    variables:
      env:
        MIX_ENV: 'prod'

    hooks:
      build: |
        mix local.hex --force
        mix local.rebar --force
        mix do deps.get --only prod, deps.compile, compile

    web:
      commands:
        start: mix phx.server
      locations:
        /:
          allow: false
          passthru: true
```

Note that there is still an Nginx proxy server sitting in front of your application. If desired, certain paths may be served directly by Nginx without hitting your application (for static files, primarily) or you may route all requests to the Elixir application unconditionally, as in the example above.

## Dependencies

The recommended way to handle Elixir dependencies on Upsun is using Hex.
You can commit a `mix.exs` file in your repository and the system downloads the dependencies in your `deps` section using the build hook above.

```elixir
  defp deps do
    [
	  {:platformshconfig, "~> 0.1.0"}
    ]
  end
```

## Accessing Services

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

### Accessing Services Manually

The services configuration is available in the environment variable `PLATFORM_RELATIONSHIPS`.

Given a [relationship](https://docs.upsun.com/create-apps/image-properties/relationships.md) defined in `.upsun/config.yaml`:

```yaml  {location=".upsun/config.yaml"}
applications:
  myapp:
    type: 'elixir:1.18'

    [...]

    # Relationships enable an app container's access to a service.
    # The example below shows simplified configuration leveraging a default service
    # (identified from the relationship name) and a default endpoint.
    # See the Application reference for all options for defining relationships and endpoints.
    relationships:
      postgresql:
```

Assuming you have in `mix.exs` the Poison library to parse JSON:

```elixir
  defp deps do
    [
      {:poison, "~> 3.0"}
    ]
  end
```

And assuming you use `ecto` you could put in `config/config.exs`:

```elixir
relationships = Poison.decode!(Base.decode64!(System.get_env("PLATFORM_RELATIONSHIPS")))
[postgresql_config | _tail] = relationships["postgresql"]

config :my_app, Repo,
  database: postgresql_config["path"],
  username: postgresql_config["username"],
  password: postgresql_config["password"],
  hostname: postgresql_config["host"]
```

and setup Ecto during the deploy hook:

```yaml  {location=".upsun/config.yaml"}
applications:
  myapp:
    hooks:
      deploy: |
        mix do ecto.setup
```
## View application instance details {#view-application-instance-details}

To understand how an application's instances are distributed, you can view the 
instance details in the project's `/run/peers.json` file. To learn more, see [View application instance details](https://docs.upsun.com/manage-resources/adjust-resources.md#view-application-instance-details) in the "Resource configuration" topic.


