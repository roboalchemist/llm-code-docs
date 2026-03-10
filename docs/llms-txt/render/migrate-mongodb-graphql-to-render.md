# Source: https://render.com/docs/migrate-mongodb-graphql-to-render.md

# Migrate MongoDB GraphQL to Render

*MongoDB Atlas GraphQL is deprecated, with service [ending in March 2025](https://www.mongodb.com/docs/atlas/app-services/migrate-hosting-graphql/).* Render provides a flexible, scalable, secure alternative for hosting your GraphQL API, including part or all of a federated GraphQL architecture.

## About Render

Render is a cloud application platform that helps developers flexibly deploy and scale their apps and services. You can host your GraphQL API on Render alongside the entire rest of your stack (frontend and backend). Your GraphQL servers can fetch from all of the same data sources, including MongoDB Atlas.

Render makes it straightforward to auto-deploy code from a Git repo, configure private network communication, autoscale services, and more.

## Before you begin

1. [Sign up for Render.](https://dashboard.render.com/register)
2. Make sure your application source is either hosted in a repostitory on [GitHub](github)/[GitLab](gitlab)/[Bitbucket](bitbucket) or available as a [prebuilt Docker image](/deploying-an-image).

## Migrate to Render

> *Always refer to the official documentation of both MongoDB Atlas and Render for the most up-to-date information.*
>
> Specific steps might vary depending on the details of your project and the technologies used.

To migrate your GraphQL app to Render from MongoDB Atlas App Services, you will deploy a GraphQL server on Render as a [web service](web-services). Here are the steps:

1. *Choose a GraphQL server implementation.*

   You can deploy virtually any GraphQL backend to Render. You might want to integrate an open-source framework like [Apollo Server](https://www.apollographql.com/docs/apollo-server) into an existing backend service or deploy a solution like [Hasura GraphQL Engine](https://hasura.io/docs/2.0/index/) as a standalone service.

   Render provides [native runtime support](language-support) for Node.js, Bun, Python, Ruby, Go, Rust, and Elixir. You can deploy GraphQL services in other languages via Docker.

2. *Deploy your GraphQL server on Render.*

   Next, deploy your GraphQL server as a [web service](web-services) on Render. Each web service on Render automatically gets a public `onrender.com` URL, and you can set up a [custom domain](custom-domains).

   - *If you're integrating a GraphQL framework into an existing web service*, follow our example guides for the web framework most relevant to you, such as [Express](/deploy-node-express-app), [Django](/deploy-django), or [Ruby on Rails](/deploy-rails-8). See the [full list of quickstarts](#quickstarts) for more options.
   - *If you're starting from scratch*, one option is to follow our [Hasura GraphQL Engine quickstart guide](/deploy-hasura-graphql) to create a standalone GraphQL service.

3. *Connect your GraphQL server to your data sources.*

   In many GraphQL API implementations, the data that backs the GraphQL API is stored in a database.

   You can provide your database's URL (also known as a database connection string) to your web service via an [environment variable](configure-environment-variables) set on your web service. Then, you must configure your web service's code to use that environment variable to connect to the database.

   If your data source is MongoDB Atlas:

   - Follow [this guide](connect-to-mongodb-atlas) to learn how to connect your web service to Atlas.
   - See [this quickstart](tutorial-rag-chatbot) for a code example. This example shows a Render web service that uses an environment variable to obtain an Atlas database URL.

4. *Update your client applications.*

   Update any client applications that interact with your GraphQL API endpoints to point to your Render service's URL.

5. *Shut down Atlas App Services endpoints.*

   After you verify that your GraphQL API endpoints are fully migrated and operational on Render, you can delete your MongoDB Atlas App Services app to avoid unnecessary costs. As a reminder, Atlas GraphQL endpoints are scheduled to shut down on March 12, 2025.

## Next steps

Learn about other Render [service types](service-types) you can use as part of your GraphQL implementation.

For example, if you have a federated GraphQL architecture with a self-hosted gateway, you can deploy the gateway as a web service and your individual subgraphs as [private services](private-services) that only receive traffic from the gateway:

[diagram]