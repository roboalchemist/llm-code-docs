# Source: https://render.com/docs/deploy-strapi.md

# Deploy Strapi on Render

[Strapi](https://strapi.io) is an open-source headless CMS built with Node.js. It comes with a great admin UI that lets your entire team create and manage content for your websites and apps. Strapi makes your content available via an API and can therefore be used in many different ways.

Depending on how you're using Strapi, your needs will vary when you deploy your project to production. In this guide we'll describe three different methods you can use to deploy Strapi on Render, and help you pick the best one for your project.

You only have to make two choices:

1. The database you will use to store structured content.
2. The storage option you will use for image and video files uploaded through Strapi.

These choices determine the scalability, availability, and cost of your deployment.

In choosing the right [Render plan](/pricing#services) for your Strapi web service, consider Strapi's [recommended requirements](https://strapi.io/documentation/developer-docs/latest/setup-deployment-guides/deployment.html#general-guidelines). Strapi also recommends setting up a proxy server for TLS and using `pm2` to manage your Strapi server process. With Render, neither of these steps is necessary. All Render sites and services come with fully managed and free TLS certificates, and Render services are automatically restarted if they become unresponsive.

## Optimize for cost and simplicity

The simplest deployment method uses a web service with an attached [persistent disk](disks). The disk will store both a SQLite database file and uploaded media files. This approach is straightforward and inexpensive, but using a disk currently prevents [horizontal scaling](scaling) and [zero downtime deploys](/deploys#zero-downtime-deploys). If you're using Strapi as the data source for a static site generator like [Gatsby](/deploy-gatsby) or [Hugo](/deploy-hugo), these limitations shouldn't be an issue for you because your service only needs to be available when you build your site.

Click the button below to see this approach in action. When you're ready to create your own Strapi project, fork our [Strapi with SQLite repository](https://github.com/render-examples/strapi-sqlite) so you can add your own content types, plugins, and configuration options.

<deploy-to-render repo="https://github.com/render-examples/strapi-sqlite">
</deploy-to-render>

## Optimize for scale and uptime

If you're using Strapi as the backend for a website or app that dynamically fetches content, scalability and availability are more important. Our [Strapi with PostgreSQL and Cloudinary repo](https://github.com/render-examples/strapi-postgres-cloudinary) is configured to use a [managed PostgreSQL database](postgresql) for structured data and [Cloudinary](https://cloudinary.com), a public cloud object store, for media file uploads. With this approach you'll get [zero downtime deploys](/deploys#zero-downtime-deploys) and the ability to [horizontally scale](scaling) your Strapi web service. Your uploaded files will be served via Cloudinary's CDN.

There are [Strapi plugins](https://strapi.io/documentation/v3.x/plugins/upload.html#using-a-provider) for a number of object storage providers besides Cloudinary, including [MinIO](https://min.io), which you can self-host on Render. See our [1-click deploy for MinIO](https://github.com/render-examples/minio).

To try this setup, create a Cloudinary account and make note of your cloud name, api key, and api secret. Cloudinary has a free tier that includes 1 GB of storage. Click the button below and fill in your Cloudinary account details when prompted. Fork the repo when you're ready to create your own project.

<deploy-to-render repo="https://github.com/render-examples/strapi-postgres-cloudinary">
</deploy-to-render>

## A hybrid option

If you care about performance but can tolerate a few seconds of downtime when you deploy, you can cut costs compared to a paid Cloudinary instance type with the approach used in our [Strapi with PostgreSQL repo](https://github.com/render-examples/strapi-postgres). Here we're using a [managed PostgreSQL database](postgresql) along with [block storage](disks) for media files. If your Strapi project doesn't need uploaded media, remove the disk to get [zero downtime deploys](/deploys#zero-downtime-deploys) and the ability to add [horizontal scaling](scaling).

<deploy-to-render repo="https://github.com/render-examples/strapi-postgres">
</deploy-to-render>

## Modify an existing Strapi project for Render

If you've been developing a Strapi project locally and are ready to deploy it to Render, follow these steps:

1. Choose the approach that's best for your needs and use the corresponding GitHub repo as a reference. You may find it helpful to look at the repo's commit history.
   - [Strapi with SQLite and uploads on disk](https://github.com/render-examples/strapi-sqlite)
   - [Strapi with PostgreSQL and uploads on Cloudinary](https://github.com/render-examples/strapi-postgres-cloudinary)
   - [Strapi with PostgreSQL and uploads on disk](https://github.com/render-examples/strapi-postgres)
2. Depending on your approach, you may need to install some npm packages. For example:
   - `pg` for PostgreSQL
   - `strapi-provider-upload-cloudinary` for Cloudinary
3. Copy the `render.yaml` file at the root of the Strapi on Render repo you picked in step 1. Consult our [infrastructure as code guide](infrastructure-as-code) to better understand what's happening in this file.
4. Copy `config/env/production` and its contents from the Strapi on Render repo you picked in step 1.
5. Push your changes to GitHub/GitLab/Bitbucket and [create an instance of your Blueprint](infrastructure-as-code#setup) from the [Render Dashboard](https://dashboard.render.com).

## Development &rarr; Staging &rarr; Production

When you deploy one of our Strapi on Render repos, your Strapi server will run in production mode. By design, Strapi's admin UI [doesn't let you edit content types in production](https://strapi.io/documentation/v3.x/getting-started/troubleshooting.html#why-can-t-i-create-or-update-content-types-in-production-staging). Instead, you can set up separate environments for development, staging, and production, and edit your structured content types in development. Here's the flow for creating and deploying your first content type:

1. Fork one of our Strapi on Render repos and clone it on your local machine.
   - [Strapi with SQLite and uploads on disk](https://github.com/render-examples/strapi-sqlite)
   - [Strapi with PostgreSQL and uploads on Cloudinary](https://github.com/render-examples/strapi-postgres-cloudinary)
   - [Strapi with PostgreSQL and uploads on disk](https://github.com/render-examples/strapi-postgres)
2. Start Strapi in development mode by running `yarn install && yarn develop` on your local machine.
3. Use the development admin UI, located by default at http://localhost:1337/admin, to create a new content type. Test by creating and fetching a few examples of this content type. Note that while content types are version controlled, your actual content is stored in a database and does not automatically transfer to other environments like staging and production.
4. Push the changes to your remote GitHub repository.
5. Deploy to a staging environment. Make sure you can create instances of the new content type.
6. Deploy to production. You and your team will now be able to create instances of the new content type via your production admin UI.

If you'd like to set up a staging environment on Render, you can update the `render.yaml` file at the root of your repository and add staging resources that are similar to your production resources. You might want to change the `name` field to something like `strapi-staging` and the `NODE_ENV` environment variable to `staging`. You might also want to use less expensive service and database instance types in staging. Finally, you can use Render's [pull request previews](service-previews) in addition to a permanent staging environment.