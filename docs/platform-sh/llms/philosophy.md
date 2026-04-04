# Source: https://docs.upsun.com/learn/overview/philosophy.md

# Philosophy

Upsun aims at reducing configuration and making developers more productive.
It abstracts your project infrastructure and manages it for you,
so you never have to configure services like a web server, a MySQL database, or a Redis cache from scratch again.

Upsun is built on one main idea — your server infrastructure is part of your app,
so it should be version controlled along with your app.

Every branch you push to your Git repository can come with bug fixes,
new features, **and** infrastructure changes.
You can then test everything as an independent deployment,
including your application code and all of your services with a copy of their data
(database entries, search index, user files, etc.).

This allows you to preview exactly what your site would look like if you merged your changes to production.

## The basics

On Upsun, a **project** is linked to a Git repository and is composed of one or more **apps**.
An app is a directory in your Git repository with a specific Upsun configuration
and dedicated HTTP endpoints (via the `.upsun/config.yaml` file).

Projects are deployed in **environments**.
An environment is a standalone copy of your live app which can be used for testing,
Q&A, implementing new features, fixing bugs, and so on.

Every project you deploy on Upsun is built as a *virtual cluster* containing a series of containers.
The main branch of your Git repository is always deployed as a production cluster.
Any other branch can be deployed as a staging or development cluster.

There are three types of containers within your cluster,
all usually configured from a single `.upsun/config.yaml` file stored alongside your code:

- The [*router*](https://docs.upsun.com/define-routes.md) is a single Nginx process responsible for mapping incoming requests to an app container,
  and for optionally providing HTTP caching.

- One or more [*apps*](https://docs.upsun.com/create-apps.md) holding the code of your project.

- Some optional [*services*](https://docs.upsun.com/add-services.md) like MySQL/MariaDB, Elasticsearch, Redis, or RabbitMQ.
  They come as optimized pre-built images.

## The workflow

Every time you deploy a branch to Upsun, the code is *built* and then *deployed* on a new cluster.

The [**build** process](https://docs.upsun.com/learn/overview/build-deploy.md#build-steps) looks through the configuration files in your repository
and assembles the necessary containers.

The [**deploy** process](https://docs.upsun.com/learn/overview/build-deploy.md#deploy-steps) makes those containers live, replacing the previous
versions, with no service downtime.

Depending on your needs, you can also [set up a **post-deploy** hook](#add-a-post-deploy-hook) to run after your app is deployed and your application container starts accepting traffic.
Adding a [`post-deploy` hook](https://docs.upsun.com/create-apps/hooks/hooks-comparison.md#post-deploy-hook) can be useful to run updates that don't require exclusive database access.

Note that if you're using Gatsby to pull from a backend container on the same environment,
you need a `post-deploy` hook to successfully build and deploy your app.

### How your app is built

During the [build step](https://docs.upsun.com/learn/overview/build-deploy.md#build-steps),
dependencies specified in `.upsun/config.yaml` are installed on application containers.

You can also customize the build step by providing a [`build` hook](https://docs.upsun.com/create-apps/hooks/hooks-comparison.md#build-hook) composed of one or more shell commands
that help create your production codebase.
That could be compiling TypeScript files, running some scripts,
rearranging files on disk, or whatever else you want.

Note that at this point all you have access to is the filesystem;
there are **no services or other databases available**.
Your live website is unaffected.

Once the build step is completed, the filesystem is frozen and a read-only container image is created.
That filesystem is the final build artifact.

### How your app is deployed

Before starting the [deployment](https://docs.upsun.com/learn/overview/build-deploy.md#deploy-steps) of your app,
Upsun pauses all incoming requests and holds them to avoid downtime.

Then, the current containers are stopped and the new ones are started.
Upsun then opens networking connections between the various containers,
as specified in `.upsun/config.yaml`.
The connection information for each service is available from the [service environment variables](https://docs.upsun.com/development/variables.md#service-environment-variables), or the [`PLATFORM_RELATIONSHIPS` environment variable](https://docs.upsun.com/development/variables/use-variables.md).

Similar to the build step, you can define a [deploy hook](https://docs.upsun.com/create-apps/hooks/hooks-comparison.md#deploy-hook) to prepare your app.
Your app has complete access to all services, but the filesystem where your code lives is now read-only.

Finally, Upsun opens the floodgates and lets incoming requests through your newly deployed app.

### Add a post-deploy hook

You can add a [`post-deploy` hook](https://docs.upsun.com/create-apps/hooks/hooks-comparison.md#post-deploy-hook) to be run after the build and deploy steps.

Similar to the [`deploy` hook](https://docs.upsun.com/create-apps/hooks/hooks-comparison.md#deploy-hook),
the `post-deploy` hook only runs once your application container accepts requests.
So you can use it to run updates such as content imports or cache warmups that can be executed simultaneously with normal traffic.

During a redeploy, the `post-deploy` hook is the only hook that is run.

## Get support

If you're facing an issue with Upsun,
open a [support ticket](https://docs.upsun.com/learn/overview/get-support.md).

## What's next?

To get a feeling of what working with Upsun entails,
see the [Get Started](https://docs.upsun.com/get-started.md) framework guides.

