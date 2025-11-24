# Source: https://www.aptible.com/docs/how-to-guides/observability-guides/setup-kibana.md

# How to set up Kibana on Aptible

> ❗️ These instructions apply only to Kibana/Elasticsearch versions 7.0 or higher. Earlier versions on Deploy did not make use of Elasaticsearch's native authentication or encryption, so we built our own Kibana App compatible with those versions, which you can find here: [aptible/docker-kibana](https://github.com/aptible/docker-kibana)

Deploying Kibana on Aptible is not materially different from deploying any other prepackaged software. Below we will outline the basic configuration and best practices for deploying [Elastic's official Kibana image](https://hub.docker.com/_/kibana).

## Deploying Kibana

Since Elastic provides prebuilt Docker images for Kibana, you can deploy their image directly using the [`aptible deploy`](/reference/aptible-cli/cli-commands/cli-deploy) command:

```sql  theme={null}
aptible deploy --app $HANDLE --docker-image kibana:7.8.1 \
  RELEASE_HEALTHCHECK_TIMEOUT=300 \
  FORCE_SSL=true \
  ELASTICSEARCH_HOSTS="$URL" \
  ELASTICSEARCH_USERNAME="$USERNAME" \
  ELASTICSEARCH_PASSWORD="$PASSWORD"
```

For the above Elasticsearch settings, refer to the [database credentials](/core-concepts/managed-databases/connecting-databases/database-credentials) of your Elasticsearch Database. You must input the `ELASTICSEARCH_HOSTS` variable in this format:`https://$HOSTNAME:$PORT/`.

> 📘 Specifying a Kibana image requires a specific version number tag. The `latest` tag is not supported. You must specify the same version for Kibana that your Elasticsearch database is running.

You can make additional customizations using environment variables; refer to Elastic's [Kibana environment variable documentation](https://www.elastic.co/guide/en/kibana/current/docker.html#environment-variable-config) for a list of available variables.

## Exposing Kibana

You will need to create an [HTTP(S) endpoint](/core-concepts/apps/connecting-to-apps/app-endpoints/https-endpoints/overview) to expose Kibana for access. While Kibana requires authentication, and you should force users to connect via HTTPS, you should also consider using [IP Filtering](/core-concepts/apps/connecting-to-apps/app-endpoints/ip-filtering) to prevent unwanted intrusion attempts.

## Logging in to Kibana

You can connect to Kibana using the username and password provided by your Elasticsearch database's [credentials](/core-concepts/managed-databases/connecting-databases/database-credentials), or any other user credentials with appropriate permissions.

## Scaling Kibana

The [default memory limit](https://www.elastic.co/guide/en/kibana/current/production.html#memory) that Kibana ships with is 1.4 GB, so you should use a 2 GB container size at a minimum to avoid exceeding the memory limit. As an example, at the 1 GB default Container size, it takes 3 minutes before Kibana starts accepting HTTP requests - hence the `RELEASE_HEALTHCHECK_TIMEOUT` [Configuration](/core-concepts/apps/deploying-apps/configuration) variable is set to 5 minutes above.

You should not scale the Kibana App to more than one container. User session information is not shared between containers, and if you scale the service to more than one container, you will get stuck in an authentication loop.
