# Source: https://render.com/docs/platform-maintenance.md

# Render Platform Maintenance — Learn about periodic upgrades to Render's underlying infrastructure.

Render routinely performs infrastructure maintenance to improve platform performance, reliability, and security.

In _most_ cases, maintenance is completely transparent, with no interruption to your services.

## Service-affecting maintenance

> Maintenance _never_ changes a service's configuration details or instance type.

Certain types of maintenance (such as OS upgrades) do require brief downtime, specifically for services that provide persistent storage:

- Render Postgres databases
- Render Key Value instances
- Services with an attached persistent disk

To ensure the integrity of your data, Render spins down these service instances completely before spinning up their replacements. This process usually takes a few minutes. For Render Postgres databases with [high availability](postgresql-high-availability), this is reduced to less than one minute.

*What about other services?*

Services without attached storage ("stateless" services) remain available during maintenance windows, because they support [zero-downtime deploys](/deploys#zero-downtime-deploys). Render can spin up new instances for these services before deprovisioning the old ones, ensuring there's always a routing destination for incoming traffic:

[diagram]

*For services that perform long-running tasks* (such as background workers), make sure these services define logic to handle a graceful shutdown in the event of receiving a `SIGTERM` signal. Render sends this signal when spinning down an instance as part of maintenance (and as part of any zero-downtime deploy).

### Resolving maintenance deploy failures

> *For assistance resolving a maintenance deploy failure:*
>
> - See [Troubleshooting Your Deploy](troubleshooting-deploys) for common issues and solutions.
> - [Reach out to our support team](https://dashboard.render.com/?contact-support) in the Render Dashboard.

As part of service-affecting maintenance, Render deploys your services to new instances before spinning down the old ones. In certain cases, this deploy might fail. This most commonly occurs if your service's most recent deploys were failing _before_ maintenance began, indicating an issue with your service's current build and deploy configuration.

In the event of a deploy failure, Render keeps your old instance running (until a specified deadline) and continues routing traffic to it:

[diagram]

Render immediately notifies you by email if a maintenance deploy fails. This email includes a deadline for resolving the issue, after which Render will bring down the old instance. *If you do not resolve the issue before the deadline, your service will be taken offline.*

### Rescheduling maintenance

> *[*Free services*](free) do not support rescheduling maintenance.*
>
> Render might perform maintenance on a free service at any time, without advance notice.

If any of your paid services will experience downtime as part of a maintenance window, Render always provides advance notice via email _and_ in the [Render Dashboard](https://dashboard.render.com). Service-affecting maintenance windows usually occur no more than once every three months.

Whenever possible, Render provides the ability to reschedule a paid service's maintenance window to a more convenient time (usually within a few days of the original scheduled date). You can reschedule in the [Render Dashboard](https://dashboard.render.com) or via the [Render API](https://api-docs.render.com/reference/update-maintenance).

### Triggering maintenance

Both the Render Dashboard and [API](https://api-docs.render.com/reference/trigger-maintenance) support _immediately_ triggering a service's scheduled maintenance.

The following actions _also_ trigger maintenance immediately, because they already involve replacing a service's current instance with a new one:

- Redeploying a service
- Restarting a Render Postgres database
- Suspending and resuming a Render Postgres database
- Changing the instance type for any service, Render Postgres database, or Render Key Value instance

---

##### Appendix: Glossary definitions

###### Render Postgres

Fully managed PostgreSQL databases that support point-in-time recovery, read replicas, high availability, and more.

Related article: https://render.com/docs/postgresql.md

###### Render Key Value

Fully managed, Redis®-compatible storage ideal for use as a job queue or shared cache.

Related article: https://render.com/docs/key-value.md

###### persistent disk

A high-performance SSD that you can attach to a service to preserve filesystem changes across deploys and restarts.

Disables [zero-downtime deploys](/deploys#zero-downtime-deploys) for the service.

Related article: https://render.com/docs/disks.md

###### background worker

Deploy this *service type* to continuously run code that does not receive incoming requests.

Ideal for processing jobs from a queue.

Related article: https://render.com/docs/background-workers.md

###### instance

A virtual machine that runs your service's code on Render.

You can select from a range of *instance types* with different compute specs.