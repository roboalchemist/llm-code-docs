# Source: https://render.com/docs/postgresql-read-replicas.md

# Read Replicas for Render Postgres — Offload expensive read operations to separate instances of your database.

*Read replicas* are separate instances of your [Render Postgres database](postgresql) that only allow read access. As you write data to your primary instance, Render asynchronously replicates those changes to your read replicas:

[diagram]

Read replicas can reduce load on your primary instance and make one-off queries safer. They're great for analysis tools that don't need to write data, or for running computationally expensive queries without affecting the performance of your primary instance.

> Read replicas always have the same instance type and storage as their primary database and are billed accordingly.

## Requirements

For your Render Postgres database to support read replicas, it must:

- Have at least 10 GB of storage
- Use the *Basic-1gb* instance type or higher
  - If your database uses a [legacy instance type](postgresql-legacy-instance-types), it must use the *Standard* instance type or higher.

Any database that meets these requirements can have up to five read replicas.

## Setup

Go to your database's *Info* page in the [Render Dashboard](https://dashboard.render.com) and click *Add Read Replica*:

[image: Database Info Page]

A confirmation dialog appears. If you confirm, Render spins up the replica instance and starts copying over data from the primary instance. That's it! Your read replica should become available within a few minutes. If it takes longer, please reach out to our support team in the [Render Dashboard](https://dashboard.render.com?contact-support).

After a read replica becomes available, you can connect to it just like you do your primary instance, using its [internal or external connection URL](postgresql-creating-connecting#connect-to-your-database).

## Performance

Changes to your primary database are synced to its read replicas after a short delay. This means replicas are best suited to use cases that don't require instant access to the most recent data possible.

The length of this delay depends on your primary instance's load. You can monitor this from the primary instance's *Metrics* page, under *Replication Lag*.

## Read replicas vs. high availability

Read replica instances are different from a *standby* instance that's used for [high availability](postgresql-high-availability). Read replicas help decrease load on your primary instance, and they're safer for one-off and expensive queries. In contrast, a standby instance helps reduce downtime in the event of instance failure.