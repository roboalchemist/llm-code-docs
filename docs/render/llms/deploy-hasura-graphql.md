# Source: https://render.com/docs/deploy-hasura-graphql.md

# Deploy Hasura GraphQL Engine on Render

The [Hasura GraphQL engine](https://hasura.io/docs/2.0/index/) makes your data instantly accessible over a real-time GraphQL API, so you can build and ship modern apps and APIs faster. Hasura connects to your databases, REST servers, GraphQL servers, and third party APIs to provide a unified realtime GraphQL API across all your data sources.

## One-Click Deploy

Click *Deploy to Render* below to set up Hasura GraphQL Engine in your Render workspace. This will deploy the Hasura GraphQL Engine web service and create a PostgreSQL database used to store both your application data and GraphQL Engine's metadata.

<deploy-to-render repo="https://github.com/render-examples/hasura-graphql">
</deploy-to-render>

By default, the Hasura GraphQL web console is not password-protected. To secure it, create an environment variable named `HASURA_GRAPHQL_ADMIN_SECRET` for the web service you just deployed in the Render Dashboard.

Now you can start working with Hasura:

- [Create a table](https://hasura.io/docs/2.0/getting-started/docker-simple/#create-a-table-and-insert-some-demo-data).
- [Test GraphQL queries](https://hasura.io/docs/2.0/getting-started/docker-simple/#try-out-a-query).
- [Read how Hasura GraphQL Engine works](https://hasura.io/docs/2.0/getting-started/how-it-works/index/).

## Use with an Existing PostgreSQL Database

The one-click deploy above creates a PostgreSQL database that's used for _both_ Hasura GraphQL Engine's metadata and your application data. If you would like to use Hasura GraphQL Engine with an existing database containing your application data, you can use the *Deploy to Render* button below. You will be asked to specify the database containing your application data on the Hasura console after deploy.

Note that Hasura GraphQL Engine still needs a database to store its own metadata, and one will be created during this deploy.

<deploy-to-render repo="https://github.com/render-examples/hasura-graphql-metadata-db-only">
</deploy-to-render>