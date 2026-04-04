# Source: https://docs.upsun.com/dedicated-environments/dedicated-gen-2/overview.md

# Source: https://docs.upsun.com/dedicated-environments/overview.md

# Source: https://docs.upsun.com/integrations/overview.md

# Source: https://docs.upsun.com/learn/overview.md

# What is Upsun Fixed?

Upsun is a Cloud Application Platform built especially for continuous deployment.
It allows you to host web applications on the cloud while making your development and testing workflows more productive.

If you're new to Upsun, the [Philosophy](https://docs.upsun.com/learn/overview/philosophy.md), [Structure](https://docs.upsun.com/learn/overview/structure.md),
and [Build and Deploy](https://docs.upsun.com/learn/overview/build-deploy.md) pages cover all the basics to start on the right track.

The main requirement of Upsun is that you use Git to manage your application code.
If you have a single-app project, you can configure it from a single `.upsun/config.yaml` file,
usually located at the root of your app folder in your Git repository.
[Multi-app projects](https://docs.upsun.com/create-apps/multi-app.md) can be set up in various ways.

Upsun is built on Debian, supports many different programming [languages](https://docs.upsun.com/languages.md) and environments,
and features recommended optimizations for several [featured frameworks](https://docs.upsun.com/get-started.md).

Finally, you can also get tips for setting up your own [development workflow](https://docs.upsun.com/development.md)
and [administrating](https://docs.upsun.com/administration.md) your Upsun account.

## Git Driven Infrastructure

As a Cloud Application Platform, Upsun automatically manages everything your application needs to run.
That means you can, and should, view your infrastructure needs as part of your application and address them under version control.

### Infrastructure as code

Upsun covers not only all of your hosting needs but also most of your DevOps needs. It is a single tool that covers the application life-cycle from development to production and scaling.

You only need to write your code, including a single or a few YAML files that specify your desired infrastructure, commit it to Git, and push.
You don't need to set up anything manually. The web server is already set up and configured, as is any database, search engine, or cache that you specify.

Every branch you push can be made a fully independent environment—complete with your application code, a copy of your database, a copy of your search index, a copy of your user files, everything.
Its automatically generated URL can be sent to stakeholders or automated CI systems.
It really is "what would my site look like if I merged this to production?" every time.

You can use these concepts to replicate a traditional development/staging/production workflow, or even to give every feature its own effective staging environment before merging to production (empowering you to use git-flow like methodologies even better). You could also have an intermediary integration branch for several other branches.

Upsun respects the structure of branches. It's entirely up to you.

### Full stack management

Managing your full stack on Upsun gives you the following unique features:

1. **Unified Environment:** All of your [services](https://docs.upsun.com/add-services.md) (MySQL, Elasticsearch, MongoDB, etc.) are managed inside the cluster and included in the price, with no external single-points-of-failure. When you [back up an environment](https://docs.upsun.com/environments/backup.md), you get a fully consistent snapshot of your whole application.
2. **Multi-Services & Multi-App:** You can deploy [multiple applications](https://docs.upsun.com/create-apps/multi-app.md) (for example, in a microservice-based architecture), using multiple data backends (MySQL, PostgreSQL, Redis, etc.) written in multiple frameworks (Drupal + NodeJS + Flask, for example) in multiple languages, all in the same cluster.
3. **Full Cluster Cloning Technology:** The full production cluster can be cloned in under a minute—including all of its data—to create on-the-fly, ephemeral [preview environments](https://docs.upsun.com/glossary.md#preview-environment) that are a byte-level copy of production.
4. **Fail-Proof Deployments:** Every time you test a new feature, you also test the deployment process.
5. **Continuous Deployment from the Start:** Everything is build-oriented, with a consistent, repeatable build process, simplifying the process of keeping your application up-to-date and secure.

