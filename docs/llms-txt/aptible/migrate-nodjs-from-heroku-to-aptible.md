# Source: https://www.aptible.com/docs/how-to-guides/app-guides/migrate-nodjs-from-heroku-to-aptible.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Heroku to Aptible Migration Guide

> A general guide for migrating applications from Heroku to Aptible, illustrated with a Node.js example

# Overview

Migrating your application from Heroku to Aptible is a relatively straightforward process. Because Heroku is also a PaaS, there are many similarities in how applications are built and operated. However, there are a few key differences, primarily in how applications are packaged, deployed, and configured.

This guide focuses on those deployment and configuration differences. It is also worth noting that Aptible differs from Heroku more broadly in its strong focus on security and compliance. [Refer to the Security & Compliance docs for more information on those platform-level capabilities](https://www.aptible.com/docs/core-concepts/security-compliance/overview).

This guide walks you through the general migration process for both your application and database, using a Node.js application with a PostgreSQL database as an example. If you are using a different framework, language, or database, most of the same steps will apply.

<Tip>
  This guide focuses on the technical steps required to migrate from Heroku to Aptible. If you require further assistance or guidance, please [contact Aptible Support](https://app.aptible.com/support).
</Tip>

### FAQs for those migrating

<AccordionGroup>
  <Accordion title="Why migrate from Heroku to Aptible?">
    Aptible is a security, compliance, and reliability-focused platform as a service (PaaS). Migrating to Aptible enables you to instantly adopt a stronger security and compliance posture, with built-in support for frameworks such as HIPAA, HITRUST, and SOC 2, while maintaining the ease of use and developer experience you may already be familiar with from Heroku.

    Teams typically migrate to Aptible when they need more robust security controls, stronger compliance guarantees, or higher reliability, without taking on the operational burden of managing their own infrastructure.
  </Accordion>

  <Accordion title="How does Aptible pricing compare to Heroku (including Heroku Shield)?">
    If you’re coming from Heroku’s standard platform, Aptible’s pricing model will feel familiar: usage-based billing, simple line items, and no long-term lock-ins or steep minimums.

    If you’re migrating from Heroku Shield specifically, Aptible differs in two important ways: Aptible does not require a 12-month contract, and Aptible does not enforce high minimum spend thresholds. This makes it easier to adopt without long-term financial commitments.
  </Accordion>
</AccordionGroup>

# Before you begin

Before starting, you should:

1. **Create an Aptible account and select your plan**

   [Sign up for Aptible here](https://app.aptible.com/signup) - by default, you should receive a 30-day free trial.

   To begin your migration, you will need to select a plan:

   * **Development** is intended for early-stage development and testing, when you do not yet have production security or compliance requirements.
   * **Production** is designed for production workloads and provides access to highly secure and compliant resources, including support for frameworks such as HIPAA.

   If you are migrating an existing production application, or if you require compliance or higher security guarantees, you should select the Production plan and create a dedicated stack before migrating your resources.
2. **Install the Aptible CLI**\
   Install the Aptible CLI on your local machine. The CLI is used to authenticate, manage environments and apps, and deploy your code.\
   [Install the CLI here.](/reference/aptible-cli/overview)
3. **Review your existing Heroku setup**

   Before migrating, make note of the following details from your existing Heroku setup, as you will apply them throughout this guide:

   * Application process types (web, worker, background jobs)
   * Environment variables and secrets
   * Add-ons such as databases, caches, or third-party services
   * Any custom build or runtime configuration
   * Networking or domain configuration

## Key considerations

While Aptible and Heroku are similar in many ways, there are a few important differences in how applications are built, deployed, and run. This section highlights those differences before moving on to the step-by-step migration guide.

### Platform Constraints

Aptible and Heroku share several operational constraints:

* Applications run on Linux inside containers.
* Incoming application traffic is supported over ports 80 (HTTP) and 443 (HTTPS).
* Applications are expected to be stateless and ephemeral.

If your application requires UDP or other non-HTTP protocols, it will need to integrate with an external service that manages those endpoints.

Persistent storage should not be stored on the application filesystem. Instead, use managed databases, object storage (such as S3 or Cloud Storage), or other external persistence services.

### Aptible requires Docker

Aptible requires applications to be built and run as containers, which means every application must include a Dockerfile. If your application is not already containerized, not to worry. Adding a Dockerfile is usually straightforward, and Aptible provides guidance and examples to help you get started.

Aptible supports two deployment workflows:

* Deploy from Git, where you push your code to Aptible and Aptible builds the Docker image for you using your Dockerfile.
* Deploy from a Docker image, where you build the image yourself and have Aptible pull and run it from a registry.

Most teams start by deploying from Git, which provides a Heroku-like experience while still benefiting from containerization. If you need more control over your build process, you can switch to deploying prebuilt images later.

If you do not yet have a Dockerfile, refer to the [Getting Started with Docker guide](https://www.aptible.com/docs/how-to-guides/app-guides/getting-started-with-docker).

### Procfiles are optional

Heroku requires a Procfile to define application processes. Aptible does not.

If no Procfile is present, Aptible will infer the service command from the Dockerfile CMD instruction. This is referred to as an [Implicit Service](https://www.aptible.com/docs/how-to-guides/app-guides/define-services#how-to-define-services).

You can continue using a Procfile if your application has multiple services or process types. Procfile syntax is standardized and compatible between Heroku and Aptible.

Depending on your deployment method, the Procfile location differs:

* Dockerfile Deploy: keep the Procfile in the repository root.
* Direct Docker Image Deploy: move the Procfile to `.aptible/Procfile`.

Alternatively, you can use Aptible’s optional `.aptible.yml` configuration file. Its placement follows the same rules:

* Root directory for Dockerfile Deploy
* `.aptible/.aptible.yml` for Direct Docker Image Deploy

### Private Registry Authentication

If you deploy images from a private Docker registry, you must configure Aptible with credentials that allow it to pull your images. This is done using environment variables or the Aptible CLI before deploying.

# Step-by-step guide

This section walks through a typical Heroku to Aptible migration. We’ll use a Node.js app with PostgreSQL as an example, but the same workflow applies to most applications.

### 1. Add a Dockerfile (if you don’t have one already)

Aptible requires a Dockerfile. If your Heroku app used buildpacks and did not include one, you’ll need to add it before deploying.

**Node.js example Dockerfile**

Create a Dockerfile:

```node  theme={null}
touch Dockerfile
```

Next, add some contents, such as stating a node runtime, establishing a work directory, and commands to install packages.

```node  theme={null}
FROM node:lts

WORKDIR /app

COPY package.json /app
COPY package-lock.json /app

RUN npm ci

COPY . /app
```

We also want to expose the right port. For many Node applications, this is port 3000.

```js  theme={null}
EXPOSE 3000
```

Finally, we want to introduce a command for starting an application. We will use Docker’s `CMD` utility to accomplish this. `CMD` accepts an array of individual words. For instance, for **npm start,** we could do:

```js  theme={null}
CMD [ "npm", "start" ]
```

In total, that creates a Dockerfile that looks like the following.

```js  theme={null}
FROM node:lts

WORKDIR /app

COPY package.json /app
COPY package-lock.json /app

RUN npm ci

COPY . /app

EXPOSE 3000

ARG DATABASE_URL

CMD [ "npm", "start" ]
```

### 2. Migrate over Procfiles (if applicable)

Heroku typically uses a Procfile to define process types (e.g., `web`, `worker`). Aptible supports Procfiles, but they are optional.

* If you do not use a Procfile, Aptible will infer the command from your Dockerfile `CMD`.
* If you do use a Procfile, you can keep using it.

If you are deploying via Git deploy, keep the Procfile in the repository root.

If you are deploying via Direct Docker Image Deploy, move your Procfile to `.aptible/Procfile`:

```js  theme={null}
mkdir .aptible #if it doesn't exist yet
cp Procfile /.aptible/Procfile
```

### 3. Set up Aptible’s remote

If you haven’t already, provision an environment and app in the Aptible UI. Then add the Aptible Git remote.

```bash  theme={null}
git remote add aptible <your remote url> 
#your remote should look like ~ git@beta.aptible.com:<env name>/<app name>.git
```

### 4. Migrate your databases

If your Heroku app uses a database (such as Heroku Postgres), you’ll migrate that data into a new [Aptible-managed database](https://www.aptible.com/docs/core-concepts/managed-databases/overview). Similar to Heroku, Aptible supports automated backups, replicas, failover logic, encryption, network isolation, and automated scaling.

Beyond provisioning a new database, you will need to migrate your data from Heroku to Aptible. You may also want to put your database in maintenance mode when doing this to avoid additional data from being written to it during the process. You can accomplish that by running:

```bash  theme={null}
heroku maintenance:on --app <APP_NAME>
```

Then, create a fresh backup of your data. We’ll use this to move the data to Aptible.

```bash  theme={null}
heroku pg:backups:capture --app <APP_NAME>
```

After, you’ll want to download the backup as a file.

```bash  theme={null}
heroku pg:backups:download --app <APP_NAME>
```

This will download a file named `latest.dump`, which needs to be converted into a SQL file to be imported into Postgres. We can do this by using the `pg_restore` utility. If you do not have the `pg_restore` utility, you can install it [on Mac using Homebrew](https://www.cyberithub.com/how-to-install-pg_dump-and-pg_restore-on-macos-using-7-easy-steps/) or [Postgres.app](https://postgresapp.com/downloads.html), and [one of the many Postgres clients](https://wiki.postgresql.org/wiki/PostgreSQL_Clients) on Linux.

```bash  theme={null}
pg_restore -f - --table=users latest.dump > data.sql
```

Then, we’ll want to move this into Aptible.

We can create a new Database running the desired version. Assuming the environment variables above are set, this command can be copied and pasted as-is to create the Database.

```bash  theme={null}
aptible db:create "new_database" \
  --type postgresql \
  --version "14" \
  --environment "my_environment" \
  --disk-size "100" \
  --container-size "4096"
```

You can use your current environment or [create a new environment](/core-concepts/architecture/environments). Then, we will use the Aptible CLI to connect to the database.

```bash  theme={null}
aptible db:tunnel "new_database" --environment "my_environment"
```

This should return the tunnel’s URL.

Keeping the session open, open a new Terminal tab and store the tunnel’s URL as an environment variable:

```bash  theme={null}
TARGET_URL='postgresql://aptible:passw0rd@localhost.aptible.in:5432/db'
```

Using the environment variable, we can use our terminal’s pSQL client to import our exported data from Heroku (here named as `data.sql`) into the database.

```bash  theme={null}
psql $TARGET_URL -f data.sql > /dev/null
```

You might get some error messages noting that the role `aptible`, `postgres`, and the database `db` already exists. These are okay. You can learn more about potential errors by reading our database import guide [here](/how-to-guides/database-guides/dump-restore-postgresql).

### 5. \[Deploy using Git] Push your code to Aptible

If we aren’t going to use the Docker registry, we can instead directly push to Aptible, which will build an image and deploy it. To do this, first commit our changes and push our code to Aptible.

```bash  theme={null}
git add -A
git commit -m "Re-organization for Aptible" 
git push aptible <branch name> #e.g. main or master
```

### 6. \[Deploying with Docker] Private Registry registration

If you used Docker’s registry for your Heroku deployments, and you were using a private registry, you’ll need to register your credentials with Aptible’s `config` utility.

```bash  theme={null}
aptible config:set APTIBLE_PRIVATE_REGISTRY_USERNAME=YOUR_USERNAME APTIBLE_PRIVATE_REGISTRY_PASSWORD=YOUR_USERNAME
```

### 7. \[Deploying with Docker] Deploy with Docker

While you can get a detailed overview of how to deploy with Docker from our [dedicated guide](/how-to-guides/app-guides/migrate-dockerfile-to-direct-image-deploy), we will summarize the core steps.

Most Docker registries supply long-term credentials, which you only need to provide to Aptible once. We can do that using the following command:

```bash  theme={null}
aptible deploy \
--app "$APP_HANDLE" \
--docker-image "$DOCKER_IMAGE" \
--private-registry-username "$USERNAME" \
--private-registry-password "$PASSWORD"
```

After, we just need to provide the Docker Image URL to deploy to Aptible:

```bash  theme={null}
aptible deploy --app "$APP_HANDLE" \
        --docker-image "$DOCKER_IMAGE"
```

If the image URL is consistent, you can skip the `--docker-image` tag on subsequent deploys.

## Closing Thoughts

For most teams, migrating from Heroku to Aptible is a same-day process. The core steps are adding a Dockerfile, migrating your data, updating configuration, and deploying your app.

Once complete, your application runs on a platform designed for security, compliance, and reliability, while preserving the simplicity and developer experience you expect from a managed PaaS.
