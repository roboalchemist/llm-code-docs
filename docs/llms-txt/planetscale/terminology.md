# Source: https://planetscale.com/docs/vitess/terminology.md

# PlanetScale terminology

> Here we provide definitions for technologies and concepts you will see throughout our documentation and product. Some of these are common terms in the databases space, while others are Vitess or PlanetScale specific.

## Database technologies

### MySQL

MySQL is the world's most popular relational database.
Many of the worlds largest web applications are powered by MySQL behind the scenes including Slack, X, GitHub, JD.com, and many others.
MySQL is open-source, has existed for 30+ years, and is currently maintained by Oracle.

### Vitess

[Vitess](https://vitess.io) is an open-source project created by engineers at YouTube in the early 2010's.
It was created to solve their MySQL scalability challenges.
Vitess works in tandem with MySQL and provides proxying, orchestration, monitoring, and sharding capabilities.
A Vitess-powered MySQL database can scale to petabytes of data and millions of queries per second.

### PlanetScale

PlanetScale is a complete database platform that emphasizes reliability, scalability, and developer productivity.
Every PlanetScale database is powered by Vitess and MySQL.
PlanetScale makes it easy to spin up, resize, manage, and work with Vitess-powered databases both for small organizations and large enterprises. Additionally, PlanetScale employs the majority of the Vitess core maintainers.

## PlanetScale concepts

### Database

In the PlanetScale app, users can create one or more **Databases**.
Each database is associated with an **Organization**.
A database is an individual Vitess cluster that uses MySQL under the hood.
If you've used vanilla MySQL in the past, you are probably used to being able to have a single MySQL server manage multiple distinct databases (EG: `CREATE DATABASE db1;`, `CREATE DATABASE db2;`...).
You cannot use `CREATE DATABASE` to create multiple logical databases within a single PlanetScale database instance.
However, you can achieve something similar by creating multiple **keyspaces**.

### Keyspace

A **Keyspace** represents a single, logical database.
When you create a new PlanetScale database, it contains a single, default keyspace of the same name as your database.
More keyspaces can be added using the [Clusters](/docs/vitess/cluster-configuration) page.
Each keyspace has its own primary and replicas.
The "keyspace" terminology [comes from Vitess](https://vitess.io/docs/concepts/keyspace/).
[Read more about keyspaces](/docs/vitess/sharding/keyspaces).

### Branch

A typical flow on GitHub is to work on new feature in branches.
When development is complete, the developer can create a pull request which then gets merged into `main`.
PlanetScale allows you to work with your database in a similar fashion via **branches**.
Every database has a default branch, often named `main`.
You can create branches of your database, in which you can make schema changes without affecting your production tables and data.

### Deploy request

When you are ready to bring the changes from a branch into your production database, you can create a **Deploy request** (or **DR** for short).
This is akin to a pull request on GitHub.
Deploy requests can be created, reviewed by peers, and deployed to the main database.
Deploy requests give you the ability to change the schema of your database with 0 downtime.
We also give you the ability to revert deploy requests for a short window of time after being deployed, in case you encounter an issue with your application.

## Vitess concepts

### VTGate

Every PlanetScale database comes with at least 3 **VTGates**.
A VTGate is the layer of Vitess that acts as a proxy between your application servers and the MySQL instances.
VTGates play an important role in allowing your applications to treat the database as a single server, even if your data is actually spread across many keyspaces and shards.
VTGates handle query buffering, distributing your queries across shards, and other important functions for high-availability.

### Shard

Vitess keyspaces can be unsharded or [sharded](/docs/vitess/sharding).
A sharded keyspace is one where the data of tables is spread out across multiple primaries, rather than all going to one.
The way data is sharded is specified via the [Vindex](/docs/vitess/sharding/vindexes).

## Need help?

Get help from [the PlanetScale Support team](https://support.planetscale.com/), or join our [GitHub discussion board](https://github.com/planetscale/discussion/discussions) to see how others are using PlanetScale.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt