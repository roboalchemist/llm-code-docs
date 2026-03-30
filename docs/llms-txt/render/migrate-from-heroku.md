# Source: https://render.com/docs/migrate-from-heroku.md

# Migrate from Heroku to Render — Bring your Heroku apps and data to the Render platform.


> *Heroku has transitioned to [maintenance-focused support](https://www.heroku.com/blog/an-update-on-heroku/) as of February 6, 2026.*
>
> The Render team can help you orchestrate your migration to minimize downtime, even for apps with multi-terabyte databases.
>
>
>
> See examples of minimal-downtime migrations by [ReadMe](/customers/readme) and [Reservamos](/customers/reservamos).

Welcome! Let's move your Heroku apps and datastores over to Render. You'll learn:

- How Heroku concepts translate to the Render platform
- How to model a Heroku app as one or more Render services
- How to move your Heroku datastores to Render Postgres and Key Value instances

*If you hit any bumps,* don't hesitate to contact our support team at `support@render.com`. For assistance with migrating complex architectures or very large databases, [get help here.](https://render.com/migrate-from-heroku)

## Why migrate?

Independent of Heroku's [recent announcement,](https://www.heroku.com/blog/an-update-on-heroku/) for years developers have found that running on Render reduces costs and provides more capabilities out of the box, such as private networking, long-lived HTTP/WebSocket connections, and built-in DDoS protection.

## Concept mapping

Before we start, let's translate some helpful terms from Heroku to Render:

---

- On Heroku, you deploy *apps*. They run on *dynos*.
- On Render, you deploy *services*. They run on *instances*.

---

- Your Heroku app's *dyno type* determines compute specs (RAM and CPU).
- Your Render service's *instance type* does the same.

---

- On Heroku, you apply runtime configuration by setting *config vars*.
- On Render, these are *environment variables*.

---

That covers the basics. If you're looking for the Render equivalent of a particular Heroku feature, here's a more extensive mapping:

*Show terminology mapping*

##### Compute

| Heroku | Render |
| --- | --- |
| App | Service |
| Dyno | Instance |
| Dyno type (Eco, Basic, etc.) | Instance type (Free, Starter, etc.) |
| Web dyno | Web service |
| Worker dyno | Background worker |
| Heroku Scheduler / clock process | Cron job |
| Config vars | Environment variables |

##### Deployment

| Heroku | Render |
| --- | --- |
| Release phase (The `release` process in your Procfile) | Pre-deploy command |
| Preboot | [Zero-downtime deploys](/deploys#zero-downtime-deploys) This is the default behavior for Render services. |

##### Observability

| Heroku | Render |
| --- | --- |
| Log drain | [Log stream](log-streams) |

##### Datastores

| Heroku | Render |
| --- | --- |
| Heroku Postgres | Render Postgres |
| Heroku Key-Value Store | Render Key Value |

## 1. Prepare to migrate

Now, let's make sure you have all the accounts and app details you need to migrate successfully.

### Create your Render account

Signing up is fast and free:

### Catalog your Heroku resources

Identify the Heroku apps you want to migrate. Note the following for each:

- All processes defined in the app's Procfile (`web`, `worker`, etc.):
    ```bash:Procfile
    # Example Procfile with two processes
    web: npm run start
    worker: npm run worker
    ```
  - On Render, we'll represent each of these processes as a separate service.
  - The command for each process will serve as the corresponding Render service's start command.
- All defined config vars (i.e., environment variables)
- Any attached Heroku Postgres and Heroku Key-Value Store add-ons

> *You can continue using many Heroku add-ons after moving your app to Render.*
>
> For example, if you're using Heroku's Sendgrid add-on, you can set all of your app's `SENDGRID_*` environment variables on your new Render service.

## 2. Recreate your app on Render

Next, let's spin up Render resources that correspond to your Heroku app's processes and datastores.

### Create datastores

> *Migrating a large database?*
>
> The Render team can help you orchestrate your migration to minimize downtime, even for apps with multi-terabyte databases.
>
>
>
> See examples of minimal-downtime migrations by [ReadMe](/customers/readme) and [Reservamos](/customers/reservamos).

We recommend creating any necessary Render Postgres and Key Value instances _before_ you deploy the apps that use them. This way, your apps can connect to those datastores on their very first deploy.

> *We won't move your existing data from Heroku to Render yet.*
>
> We'll do this as part of the final migration process.

Follow these steps for each Heroku Postgres and Heroku Key-Value Store add-on you want to move:

1. In the [Render Dashboard](https://dashboard.render.com), click *New > Postgres* or *New > Key Value*:

   [image: Creating a new web service in the Render Dashboard]

2. Specify the following:

   - Your datastore's name
   - The *region* where you want to host the datastore
   - Which *instance type* to run on
     - Free instance types are available for Render Postgres and Key Value to help you get started. [See details.](free#free-postgres)
   - Your starting storage (Postgres only)
     - Feel free to start with a small amount of storage (1 GB or 5 GB) for testing. You can increase a database's storage later, but only once every 12 hours.

3. Click the *Create* button.

   Render provisions your new datastore, and it becomes available within a minute or two.

4. After your datastore becomes available, open its *Info* page in the [Render Dashboard](https://dashboard.render.com) and click the *Connect* dropdown in the top right:

   [image: Viewing a database's internal URL]

5. Copy your datastore's *internal URL*. Your Render services will use this URL to connect to the datastore over a private network.

   - External clients (like your local development environment) can instead connect to the datastore via its *external URL*, which is available in the same dropdown.

6. Repeat this set of steps for each Heroku Postgres and Heroku Key-Value Store add-on you want to move.

### Create services based on your Procfile

Most Heroku apps define a file named `Procfile` in their repo's root directory. This file defines startup commands for each of the app's distinct processes.

Here's an example Procfile for a generic Node.js app (the same concepts apply to any language):

```bash:Procfile
# web process
web: npm run start

# non-web process
worker: npm run worker

# release phase command
release: db-migrate -e prod up
```

Let's look at how to replicate this configuration on Render.

#### The `web` and `release` processes

Your Heroku app's `web` process is the only process that receives HTTP traffic from the internet. On Render, this corresponds to a *web service*. Every web service receives an `onrender.com` subdomain, and you can add your own custom domains.

1. In the [Render Dashboard](https://dashboard.render.com), click *New > Web Service*:

   [image: Creating a new web service in the Render Dashboard]

2. Specify the following:

   - Your project repo and branch to deploy (from GitHub, GitLab, or Bitbucket)
   - Your app's *language* (Node.js, Python, etc.)
   - The *region* where you want to host the service
     - Choose the same region as your datastores to enable low-latency private network communication.
   - Which *instance type* to run on
     - Render offers a [free instance type](free) for hobby projects and testing out the platform.

3. Provide the commands that Render will use to build and run your code:

| Command | Value |
| --- | --- |
| *Build Command* | In most cases, provide the same command you use to build your project locally, such as `npm install` for Node.js or `pip install -r requirements.txt` for Python. If necessary for your framework, modify the command to create a production build instead of a development build. |
| *Pre-deploy Command* (optional) | Provide the same command as your Procfile's `release` process, if any. Similar to Heroku's release phase, Render runs the pre-deploy command just before each deploy of your service. Use it to run database migrations and other setup tasks. |
| *Start Command* | Provide the same command as your Procfile's `web` process. Common examples of start commands include `npm run start` for Node.js and `gunicorn your_application.wsgi` for Python. |

   Here are commands for the example Node.js Procfile above:

   [image: Setting deploy-related commands in the Render Dashboard]

4. Set any required environment variables for your web service:

   [image: Setting environment variables in the Render Dashboard]

   - *For datastore connections,* provide the internal datastore URLs you copied earlier.
     - For an app you're moving from Heroku, these environment variables are often named `DATABASE_URL` for Postgres and `REDIS_URL` for Key Value.
   - *For other environment variables,* copy over the values from your Heroku app's config vars.
   - You can make changes to your service's environment variables at any time after your service is created. [See details.](configure-environment-variables)

5. Click *Deploy Web Service*.

You're all set! Render kicks off your service's first deploy. You can view the build logs in the Render Dashboard.

When the deploy completes, your service will be live at its `onrender.com` subdomain. If you encounter any issues, see [Troubleshooting Deploys](troubleshooting-deploys).

#### Non-web processes

If your app defines non-`web` processes in its Procfile, those processes _don't_ receive incoming network traffic. Instead, they usually process jobs from a queue. On Render, these correspond to *background workers*:

[image: Creating a new background worker in the Render Dashboard]

The steps for creating a background worker are similar to those for creating a web service. The key differences are:

- Your background worker probably doesn't need to run a pre-deploy command if your web service already handles database migrations.
- Render does not provide a free instance type for background workers.

Complete the background worker creation process for every non-`web` process in your app's Procfile, specifying the appropriate build and start command for each.

> *Services do not share environment variables by default.*
>
> If your web service and background workers require some of the same environment variables, you can do one of the following:
>
> - Manually set the environment variables for both services
> - Create an [environment group](configure-environment-variables#environment-groups) and apply it to both services

## 3. Swap over to your Render infrastructure

With everything up and running on Render, we're ready to move your data and DNS configuration over from Heroku.

> *This final step (moving your data and DNS configuration) requires downtime for your app, even if brief.*
>
> Schedule your migration for off hours to minimize the impact on your users.
>
> For assistance with a complex migration, [get help here.](https://render.com/migrate-from-heroku)

### Scale up your Render datastores

Before you move over your data, make sure your Render Postgres and Key Value instances have sufficient storage and compute resources to handle your current requirements. You can upgrade as needed in the Render Dashboard.

#### Render Postgres

- You can [increase your storage](postgresql-creating-connecting#increasing-storage-manually) once every 12 hours. You can't decrease it.
- You can [change your instance type](postgresql-creating-connecting#changing-your-instance-type) (upgrade or downgrade) at any time. Your database will be unavailable for a few minutes during the change.

#### Render Key Value

- You can upgrade your instance type at any time. Your Key Value instance will be unavailable for a few minutes during the change.
- You can't downgrade your instance type.

### Enable maintenance mode on Heroku

When you're ready to kick off the migration, put your Heroku app into [maintenance mode](https://devcenter.heroku.com/articles/maintenance-mode) so that it no longer accepts user traffic. This helps ensure that no changes are made to your datastores during the migration.

Using the Heroku CLI, run:

```shell
heroku maintenance:on --app <YOUR HEROKU APP NAME>
```

### Export data from Heroku Postgres

1. Create a backup of your database.

   Using the Heroku CLI, run:

   ```shell
   heroku pg:backups:capture --app <YOUR HEROKU APP NAME>
   ```

2. Download the backup.

   Using the Heroku CLI, run:

   ```shell
   heroku pg:backups:download --app <YOUR HEROKU APP NAME>
   ```

   This downloads a file named `latest.dump` to your local computer.

### Import data into Render Postgres

1. Obtain your Render Postgres database's *External Database URL* from its *Info* page in the Render Dashboard.

2. Import `latest.dump` into your Render Postgres database.

   ```shell
   pg_restore --verbose  --no-acl --no-owner -d <YOUR RENDER DB EXTERNAL CONNECTION STRING> latest.dump
   ```

> *If your database is larger than 20GB or under heavy load, use [*Heroku's instructions*](https://help.heroku.com/7U1BTYHB/how-can-i-take-a-logical-backup-of-large-heroku-postgres-databases) to create a backup of your data.*
>
> After the backup completes, you can use the same `pg_restore` command above to import the data to your Render Postgres database.
>
> Consider using the `--jobs` flag available to both the `pg_dump` and `pg_restore` commands to reduce the time required for backup and restore.

### Update your DNS records

If your Heroku app uses a custom domain, follow the instructions to [update your DNS configuration](custom-domains#1-add-your-domain-in-the-render-dashboard) to point to Render instead of Heroku. Apply each app's custom domain to the corresponding Render web service.

Note that it will take some time for your DNS changes to propagate, and for Render to then provision a TLS certificate for your domain.

## Next steps

Congratulations! You've successfully migrated your Heroku app to Render.

Next, explore more of Render's capabilities. Here are a few to get you started:

- Learn about additional [service types](service-types) you can deploy on Render, such as [cron jobs](cronjobs).
- Control access to your Render [Postgres database](postgresql-creating-connecting#restricting-external-access) and [Key Value instance](key-value#enabling-external-connections).
- Invite team members to join you on Render, and configure their [user roles](team-members).
- Use Render's [Infrastructure as Code](infrastructure-as-code) to define and modify your services.

---

##### Appendix: Glossary definitions

###### instance

A virtual machine that runs your service's code on Render.

You can select from a range of *instance types* with different compute specs.

###### instance type

Specifies the RAM and CPU available to your service's *instances*.

Common instance types for a new web service include:

- *Free*: 512 MB RAM / 0.1 CPU
- *Starter*: 512 MB RAM / 0.5 CPU
- *Standard*: 2 GB RAM / 1 CPU

For the full list, see the [pricing page](/pricing#services).

###### environment variable

Config values you can apply to a service to customize its behavior at build and runtime, such as `NODE_VERSION` or `OPENAI_API_KEY`.

Render sets some environment variables for your service by [default](environment-variables).

Related article: https://render.com/docs/configure-environment-variables.md

###### web service

Deploy this *service type* to host a dynamic application at a public URL.

Ideal for full-stack web apps and API servers.

Related article: https://render.com/docs/web-services.md

###### background worker

Deploy this *service type* to continuously run code that does not receive incoming requests.

Ideal for processing jobs from a queue.

Related article: https://render.com/docs/background-workers.md

###### cron job

Deploy this *service type* to execute a command or script on a predefined schedule.

Ideal for intermittent tasks like sending email digests or generating reports.

Related article: https://render.com/docs/cronjobs.md

###### pre-deploy command

If set for a service, Render runs this command just before each of its deploys.

Ideal for database migrations and other tasks that should always precede service startup.

Related article: https://render.com/docs/deploys.md#pre-deploy-command

###### Render Postgres

Fully managed PostgreSQL databases that support point-in-time recovery, read replicas, high availability, and more.

Related article: https://render.com/docs/postgresql.md

###### Render Key Value

Fully managed, Redis®-compatible storage ideal for use as a job queue or shared cache.

Related article: https://render.com/docs/key-value.md

###### start command

The command that Render runs to start your built service in a newly deployed *instance*.

Common examples include `npm start` for Node.js and `gunicorn your_application.wsgi` for Python.

Related article: https://render.com/docs/deploys.md#start-command

###### region

Each Render service runs in one of the following regions: *Oregon*, *Ohio*, *Virginia*, *Frankfurt*, or *Singapore*.

Services in the same region can communicate over their *private network*.

Related article: https://render.com/docs/regions.md

###### build command

The command that Render runs to build your service from source.

Common examples include `npm install` for Node.js and `pip install -r requirements.txt` for Python.

Related article: https://render.com/docs/deploys.md#build-command