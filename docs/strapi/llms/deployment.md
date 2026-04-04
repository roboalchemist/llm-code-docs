# Deployment

Strapi provides many deployment options for your project or application. Your Strapi applications can be deployed on traditional hosting servers or your preferred hosting provider.

The following documentation covers the basics of how to prepare Strapi for deployment on with several common hosting options.

:::strapi Strapi Cloud
You can use [Strapi Cloud](/cloud/intro) to quickly deploy and host your project.
:::

:::tip
If you already created a content structure with the Content-Type Builder and added some data through the Content Manager to your local (development) Strapi instance, you can leverage the [data management system](/cms/features/data-management) to transfer data from a Strapi instance to another one.

Another possible workflow is to first create the content structure locally, push your project to a git-based repository, deploy the changes to production, and only then add content to the production instance.
:::

:::caution
For self-hosted Kubernetes deployments, we recommend using **npm** rather than **pnpm**. `pnpm` aggressive hoisting of dependencies can break native modules, such as `mysql2`— that your application may rely on. `npm` flatter, more predictable `node_modules` layout helps ensure native packages load correctly.
:::

## General guidelines

### Hardware and software requirements

To provide the best possible environment for Strapi the following requirements apply to development (local) and staging and production workflows.

</Tabs>

Run the server with the `production` settings:

</Tabs>

:::caution
We highly recommend using  to manage your process.
:::

If you need a server.js file to be able to run `node server.js` instead of `npm run start` then create a `./server.js` file as follows:

```js title="path: ./server.js"

const strapi = require('@strapi/strapi');
strapi.createStrapi(/* {...} */).start();
```

:::caution

If you are developing a `TypeScript`-based project you must provide the `distDir` option to start the server.
For more information, consult the [TypeScript documentation](/cms/typescript/development#use-the-createstrapi-factory).
:::

:::tip Health check endpoint
Strapi exposes a lightweight health check route at `/_health` for uptime monitors and load balancers. When the server is ready, it responds with an HTTP `204 No Content` status and a `strapi: You are so French!` header value, which you can use to confirm the application is reachable.
:::

### Advanced configurations

If you want to host the administration on another server than the API, [please take a look at this dedicated section](/cms/configurations/admin-panel#deploy-on-different-servers).

## Additional resources

:::prerequisites
* Your Strapi project is [created](/cms/installation) and its code is hosted on GitHub.
* You have read the [general deployment guidelines](/cms/deployment#general-guidelines).
:::

The  of the Strapi website include information on how to integrate Strapi with many resources, including how to deploy Strapi on the following 3rd-party platforms:

<br/>

In addition, community-maintained guides for additional providers are available in the . This includes the following guides:

<br/>

The following external guide(s), not officially maintained by Strapi, might also help deploy Strapi on various environments:

:::strapi Multi-tenancy
If you're looking for multi-tenancy options, the Strapi Blog has a .
:::