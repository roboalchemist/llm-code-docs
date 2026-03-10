# Source: https://render.com/docs/faq.md

# Render FAQ

This page lists answers to questions that many folks have as they're getting up and running with Render.

## Languages and technologies

### Which languages does Render support?

Render [natively supports](language-support) *Node.js* / *Bun*, *Python*, *Ruby*, *Go*, *Rust*, and *Elixir*.

You can deploy an app in virtually _any_ language (.NET, Java, PHP, etc.) via a [Docker image](docker).

### Which datastores does Render support?

Render offers managed [Postgres databases](postgresql), along with [Key Value instances](key-value) that are compatible with virtually all Redis clients.

You can also run your own custom database instance (MariaDB, MongoDB, etc.) backed by a [persistent disk](disks).

## Billing

### What can I do on Render for free?

See [Deploy for Free](free).

### What does Render bill for?

Render bills each workspace monthly for the usage listed below. For details on all of these, see the [pricing page](/pricing).

------

###### Billable

Compute costs for paid service instances

###### Description

Prorated by the second. If a service is active for ten seconds in a given month, you are billed only for those ten seconds. You are billed for each of the following:

- Each [paid service instance](/pricing#compute), including Render Postgres and Key Value instances
  - For [scaled](scaling) services, you are billed for each running instance.
- Replica Render Postgres databases created for [high availability](postgresql-high-availability) or [read replicas](postgresql-read-replicas)
- Each paid instance running as part of a [service preview](service-previews) or [preview environment](preview-environments)

---

###### Billable

Build pipeline minutes

###### Description

*Includes a monthly included amount.* Render's [build pipeline](build-pipeline) is responsible for building your project before it's deployed. This includes running each service's [build and pre-deploy commands](/deploys#deploy-steps). Each workspace receives a monthly included amount of pipeline minutes (see the [pricing page](/pricing)), which are consumed while running these commands. Render also offers a [performance pipeline tier](build-pipeline#pipeline-tiers) for teams with builds that require additional memory and/or CPU. Performance pipeline minutes carry an additional charge and do _not_ provide a monthly included amount. You can set a monthly [spend limit](build-pipeline#setting-a-spend-limit) for pipeline minutes. If you reach this limit in a given month, _Render stops running new builds for your services until the next billing period_.

---

###### Billable

Outbound bandwidth

###### Description

> *Render made changes to outbound bandwidth on August 1, 2025.* For details, see [Outbound Bandwidth](outbound-bandwidth).
 *Includes a monthly included amount.* Outbound bandwidth includes all network traffic sent by your services to destinations outside of Render. This data includes web pages, API payloads, and so on. Each workspace receives a monthly included amount of outbound bandwidth shared across all services (see the [pricing page](/pricing)). If you exceed this, Render bills you for a supplementary amount. _Inbound_ bandwidth (traffic _to_ your services) is free. As part of Render's [DDoS protection](ddos-protection), Render does _not_ bill for bandwidth usage incurred from a DDoS attack.

---

###### Billable

Team members

###### Description

[*Professional* workspaces](professional-features) and higher are billed per member per month, depending on plan type. For details, see the [pricing page](/pricing). These workspaces gain access to features like [autoscaling](scaling#autoscaling), [preview environments](preview-environments), and the [Performance build pipeline](build-pipeline#pipeline-tiers).

------

### All of my services run on free instances. Can I still be billed?

*Yes, if you've added a payment method.* If you exceed your monthly included amount of outbound bandwidth or build pipeline minutes, Render bills you for a supplementary amount. You can set a monthly [spend limit](build-pipeline#setting-a-spend-limit) for pipeline minutes.

> If you haven't added a payment method and you would incur charges, Render instead disables your services for the duration of the current billing period.

## Service behavior

### My app runs fine locally. Why does it fail to deploy?

Please see [Troubleshooting Your Deploy](troubleshooting-deploys).

### Why is my free service sometimes slow to respond?

Free web service instances [spin down](free#spinning-down-on-idle) if they receive no incoming traffic for 15 consecutive minutes. These services take up to a minute to spin back up when they next receive a request.

Paid instance types do _not_ spin down.

Learn more about [free instance limitations](free), including for Render Postgres and Key Value.

### Why do files saved to my service's filesystem disappear?

By default, Render services have an *ephemeral filesystem*, which means that any changes you make to local files are *lost* every time a service redeploys or restarts.

For long-term data storage on Render, we recommend one of the following:

- For storage of relational data, create a [Render Postgres database](postgresql).
- For storage of key-value data, create a [Render Key Value instance](key-value).
- For storage of arbitrary files, attach a [persistent disk](disks).
  - You can also use a persistent disk to run a custom database instance instead of Render Postgres, such as [MySQL](/deploy-mysql).

### Can I deploy multiple apps to a single Render service?

*It might be possible, but you shouldn't.* Run each of your applications in a separate service to ensure proper resource isolation for security and performance.

Let's say you want to deploy an architecture consisting of a frontend site, a backend API, and a datastore. We recommend deploying these as follows:

| App           | Service type(s)                                                                           |
| ------------- | ----------------------------------------------------------------------------------------- |
| Frontend site | [Static site](static-sites) or [web service](web-services)                              |
| Backend API   | [Web service](web-services) or [private service](private-services)                      |
| Datastore     | [Render Postgres](postgresql) or a custom database backed by a [persistent disk](disks) |

To help identify which service types are right for your use case, see [this flow chart](service-types#which-service-type-is-right-for-my-app).

## Account administration

### Can I transfer existing services from one workspace to another?

No, it is not currently possible to transfer existing services between workspaces. Instead, you can:

- [Invite team members](team-members) to collaborate on services in your current workspace
- Recreate your services in the workspace you want to move them to

## Render support

### Which types of issues can Render's support team help with?

Please see [When to contact support](troubleshooting-deploys#when-to-contact-support).