# Source: https://docs.upsun.com/create-apps/multi-app/relationships.md

# Define relationships between your multiple apps

When you set up a project containing multiple applications,
by default your apps can't communicate with each other.
To enable connections, define relationships between apps using the `http` endpoint.

You can't define circular relationships.
If `app1` has a relationship to `app2`, then `app2` can't have a relationship to `app1`.
If you need data to go both ways, consider coordinating through a shared data store,
like a database or [RabbitMQ server](https://docs.upsun.com/add-services/rabbitmq.md).

Relationships between apps use HTTP, not HTTPS.
This is still secure because they're internal and not exposed to the outside world.

## Relationships example

You have two apps, `app1` and `app2`, and `app1` needs data from `app2`.

In your app configuration for `app1`, define a relationship to `app2`:

```yaml  {location=".upsun/config.yaml"}
applications:
  app1:
    relationships:
      api:
        service: "app2"
        endpoint: "http"
```

Once they're both built, `app1` can access `app2` at the following URL: `http://api.internal`. 
The specific URL is always available through the [service environment variables](https://docs.upsun.com/development/variables.md#service-environment-variables),
or through the [`PLATFORM_RELATIONSHIPS` variable](https://docs.upsun.com/development/variables/use-variables.md#use-provided-variables):

```bash {}
$ echo $API_HOST
api.internal
```

It uses the ``jq`` library, which is included in all app containers for this purpose.

    Terminal on app1 container

```bash {}
$ echo $PLATFORM_RELATIONSHIPS | base64 --decode | jq '.api[0].host'
api.internal
```


