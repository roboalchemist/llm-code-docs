# Source: https://render.com/docs/deploy-redash.md

# Deploy Redash

[Redash](https://redash.io/) is an open-source self-hosted platform for collaborative data querying and visualization. It's quick to set up and it works with many popular data sources including Redshift, Google BigQuery, Google Spreadsheets, PostgreSQL, MySQL, and ElasticSearch.

The main features of Redash include:

- *Browser-based* and *REST API*: Redash runs fully in your browser, with a shareable URL for every view and a well-defined API.
- *Query editor*: You can quickly compose SQL and NoSQL queries with a schema browser and utilize autocomplete. You can also create snippets and reuse them.
- *Visualization* and *dashboards*: Redash allows you to create presentable [visualizations](https://redash.io/help/user-guide/visualizations/visualization-types) with drag and drop. You can group your visuals into dashboards that can automatically update at regular intervals of your choosing.
- *Alerts*: You can define trigger conditions and be alerted instantly when your data changes.

[image: Redash Query Screenshot]

You can host your Redash instance on Render in just a few minutes. Once it's live, you will be able to connect to your data sources, build dashboards to visualize data, and share them with your team.

## One-Click Deploy

Click *Deploy to Render* below to set up Redash on Render.

<deploy-to-render repo="https://github.com/render-examples/redash">
</deploy-to-render>

Execute the statement below in the Render Shell for your Redash service. This will [initialize your database](#initialize-the-database):

```shell
render-redash create_db
```

That’s it! Visit your service available on your `.onrender.com` URL, fill in the basic information about your user account, and start using Redash on Render!

## Manual Deployment

### Create a Database

Create a new [managed PostgreSQL](postgresql) instance on Render. The database should be up in a few minutes; wait for it to go live before moving to the next step.

Note your database *internal database URL*; you will need it later.

### Create a Redis Instance

Create a new Redis instance using [the Redis deployment guide](key-value) and make note of the *hostname* and *port*.

### Create an Environment Group

Create a new *Environment Group* named `redash-shared` and add the following environment variables to it:

| Key                    | Value                                         |
| ---------------------- | --------------------------------------------- |
| `REDASH_COOKIE_SECRET` | Click `Generate` to get a secure random value |
| `REDASH_LOG_LEVEL`     | `INFO`                                        |

### Deploy the Redash Web Service

1. Fork [render-examples/redash](https://github.com/render-examples/redash) on GitHub or click `Use this template`. Make sure to give Render's GitHub app permission to access your new repository

2. Start creating a new *Web Service* on Render using your new repo.

3. Pick a name for your Redash instance and make sure that the *Language* is set to `Docker`.

4. Select _at least_ the *Standard* instance type. The Redash web server may exhaust the memory limit on starter instance types.

5. Add the following environment variables to the web service:

   | Key                   | Value                                                                 |
   | --------------------- | --------------------------------------------------------------------- |
   | `REDASH_DATABASE_URL` | Your internal database URL                                            |
   | `REDIS_HOSTPORT`      | Redis hostname and port, for example: `red-xxxxxxxxxxxxxxxxxxxx:6379` |

6. Under *Advanced*, set the *Docker Command* to `render-redash server`.

7. Click `Create Web Service` to deploy your service.

8. In your web service, under the *Environment* tab, link your shared configuration environment group with this service.

> At this point, your service is likely going to fail while connecting to the database and might report logs about missing tables in the database. This is expected. We will create these tables in the next step.

### Create Redash Background Workers

Redash executes queries and other processing tasks outside its web server, using background services. For this, you have to create two Render *Background Workers*: a _scheduler_ and a _worker_.

#### Scheduler

1. Create a new *Background Worker* on Render and select the same repository you used for the web service. Make sure the *Language* is set to `Docker` and pick a name for your Redash scheduler, e.g. `redash-scheduler`.

2. Add the following environment variables to the background worker:

   | Key                   | Value                                                                 |
   | --------------------- | --------------------------------------------------------------------- |
   | `REDASH_DATABASE_URL` | your internal database URL                                            |
   | `REDIS_HOSTPORT`      | Redis hostname and port, for example: `red-xxxxxxxxxxxxxxxxxxxx:6379` |
   | `QUEUES`              | `celery`                                                              |
   | `WORKERS_COUNT`       | `1`                                                                   |

3. Under *Advanced*, set the *Docker Command* to `render-redash scheduler`.

4. Click *Create Background Worker* to deploy your scheduler.

5. In your scheduler, under *Environment*, link your shared environment group with this service.

#### Worker

1. Now, create another *Background Worker* on Render and select the same repository you used for the web service and the scheduler.

2. Pick a name for your Redash worker, e.g. `redash-worker`, and make sure that the *Language* is set to `Docker`.

3. Add the following environment variables to the background worker:

   | Key                   | Value                                                                 |
   | --------------------- | --------------------------------------------------------------------- |
   | `REDASH_DATABASE_URL` | your internal database URL                                            |
   | `REDIS_HOSTPORT`      | Redis hostname and port, for example: `red-xxxxxxxxxxxxxxxxxxxx:6379` |
   | `QUEUES`              | `queries,scheduled_queries,schemas`                                   |

4. Under *Advanced*, set the *Docker Command* to `render-redash worker`.

5. Click *Create Background Worker* to deploy your worker.

6. In your worker, under *Environment*, link your shared environment group with this service.

### Initialize the Database

To create and prefill the database tables necessary for Redash to operate, you will have to execute a special one-time command. Go to the *Shell* tab of your Redash web service and run the following command:

```shell
render-redash create_db
```

That’s it! After about a minute, the script will finish running, and your Redash installation will be available on your `.onrender.com` URL. Go to `https://your-subdomain.onrender.com`, fill in the basic information about your user account, and start using Redash on Render!

<div style="width: 60%; margin: auto;">

[image: Redash Initial Setup]

</div>

## Optional: Setting up Mailing

To allow Redash to send emails (user invites, password resets, alert triggers, and more), you will need to configure it with the mail server you use. Our one-click deploy has a template for this step that is commented out in its [`render.yaml`](https://github.com/render-examples/redash/blob/master/render.yaml) file.

1. Create a new *Environment Group* named e.g. `redash-mailing` and add the relevant environment variables (not all may be required for your use-case):

   | Key                          | Value                           |
   | ---------------------------- | ------------------------------- |
   | `REDASH_MAIL_SERVER`         | SMTP server address             |
   | `REDASH_MAIL_PORT`           | SMTP server port, default: `25` |
   | `REDASH_MAIL_USE_TLS`        | default: `false`                |
   | `REDASH_MAIL_USE_SSL`        | default: `false`                |
   | `REDASH_MAIL_USERNAME`       | default: `None`                 |
   | `REDASH_MAIL_PASSWORD`       | default: `None`                 |
   | `REDASH_MAIL_DEFAULT_SENDER` | email address to send from      |

1. Link the newly created group to your Redash *web service* and your *background workers*.