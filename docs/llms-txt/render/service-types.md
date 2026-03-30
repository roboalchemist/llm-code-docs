# Source: https://render.com/docs/service-types.md

# Render Service Types — Identify the right service type for your use case.

Render supports five different *service types* for hosting your app:

- Web services (most common)
- Static sites
- Private services
- Background workers
- Cron jobs

You can also create *fully managed datastores* to use with your app:

- Render Postgres databases
- Render Key Value instances
  - These instances are compatible with virtually all Redis®<sup>\*</sup> clients.

Choosing a service type is the first step of creating a new service in the [Render Dashboard](https://dashboard.render.com):

[image: Selecting a service type from the New menu]

## Which service type is right for my app?

[diagram]

See below for a summary of each service type, along with links to full documentation.

## Summary of service types

### For running code

------

###### Service Type

[*Web service*](web-services)

###### Description

*The most common service type.* Dynamic web apps with a public `onrender.com` subdomain for receiving traffic over HTTP. If you're building a public web app using Express, FastAPI, Rails, or something similar, use this service type. To get started, you can create a [free instance](free#free-web-services).

---

###### Service Type

[*Static site*](static-sites)

###### Description

Websites that consist entirely of statically served assets (commonly HTML, CSS, and JS). Static sites have a public `onrender.com` subdomain and are served over a global CDN. Use static sites to deploy frontends created with frameworks such as:

- [Vue.js](/deploy-vue-js)
- [Hugo](/deploy-hugo)
- [Svelte](/deploy-svelte)
- [Jekyll](/deploy-jekyll)

---

###### Service Type

[*Private service*](private-services)

###### Description

Dynamic web apps that _don't_ have a public URL. Private services do expose an _internal_ hostname for receiving traffic from your other Render services over their shared [private network](private-network). Private services are great for deploying tools like:

- [Elasticsearch](/deploy-elasticsearch)
- [ClickHouse](/deploy-clickhouse)

---

###### Service Type

[*Background worker*](background-workers)

###### Description

Internal apps that run continuously, often to process jobs that are added to a job queue. Background workers do _not_ expose a URL or internal hostname, but they can send outbound requests to other service types. Use background workers with a framework like:

- [Sidekiq](/deploy-sidekiq-worker)
- [Celery](/deploy-celery)

---

###### Service Type

[*Cron job*](cronjobs)

###### Description

Internal apps that run—and then exit—on a defined schedule. A cron job might run a single bash command, a script with multiple commands, or a compiled executable. Cron jobs do _not_ expose a URL or internal hostname, but they can send outbound requests to other service types.

------

### For storing data

> In addition to the managed datastores below, Render supports attaching a [persistent disk](disks) to most other service types.

| Service Type | Description |
| --- | --- |
| [*Render Postgres*](postgresql) | A powerful, open-source relational database. To get started, you can create a [free instance](free#free-postgres) that expires after 30 days. Render continually backs up all paid Render Postgres instances to provide [point-in-time recovery](postgresql-backups). Larger instances support additional reliability features like [read replicas](postgresql-read-replicas) and [high availability](postgresql-high-availability). |
| [*Render Key Value*](key-value) | An in-memory key-value store that's ideal for use as a job queue or a shared cache. To get started, you can create a [free instance](free#free-key-value). Render Key Value is compatible with virtually all Redis clients. Paid Key Value instances continuously write to disk to persist data across restarts. |

Redis is a registered trademark of Redis Ltd. Any rights therein are reserved to Redis Ltd. Any use by Render Inc is for referential purposes only and does not indicate any sponsorship, endorsement or affiliation between Redis and Render Inc.

---

##### Appendix: Glossary definitions

###### web service

Deploy this *service type* to host a dynamic application at a public URL.

Ideal for full-stack web apps and API servers.

Related article: https://render.com/docs/web-services.md

###### static site

Deploy this *service type* to host a static website (HTML/CSS/JS) over a global CDN at a public URL.

Related article: https://render.com/docs/static-sites.md

###### private service

Deploy this *service type* to host a dynamic application that is not internet-reachable.

Ideal for internal apps that only your other Render services can access.

Related article: https://render.com/docs/private-services.md

###### background worker

Deploy this *service type* to continuously run code that does not receive incoming requests.

Ideal for processing jobs from a queue.

Related article: https://render.com/docs/background-workers.md

###### cron job

Deploy this *service type* to execute a command or script on a predefined schedule.

Ideal for intermittent tasks like sending email digests or generating reports.

Related article: https://render.com/docs/cronjobs.md

###### Render Postgres

Fully managed PostgreSQL databases that support point-in-time recovery, read replicas, high availability, and more.

Related article: https://render.com/docs/postgresql.md

###### Render Key Value

Fully managed, Redis®-compatible storage ideal for use as a job queue or shared cache.

Related article: https://render.com/docs/key-value.md