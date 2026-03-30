# Source: https://render.com/docs/deploy-mongodb.md

# Deploy MongoDB

[MongoDB](https://www.mongodb.com/) is a popular, scalable, NoSQL database used by millions of
developers. You can run your own MongoDB instance as a [private service](private-services) on
Render backed by *high performance SSDs* with [automatic daily snapshots](disks#disk-snapshots).

We'll be deploying MongoDB using the latest official [Docker image](https://github.com/docker-library/mongo) and the [Render MongoDB repository](https://github.com/render-examples/mongodb) to install MongoDB with a single click.

> If you're interested in connecting a Render-hosted app with a database on MongoDB Atlas instead of with an instance of MongoDB hosted on Render, refer to the guide:
>
> - [Connecting to MongoDB Atlas](connect-to-mongodb-atlas)

## One-Click Deploy

Click the *Deploy to Render* button below to deploy MongoDB on Render.

<deploy-to-render repo="https://github.com/render-examples/mongodb">
</deploy-to-render>

## Manual Deploy

1. Create a new [*Private Service*](https://dashboard.render.com/select-repo?type=pserv) on Render
   and enter `https://github.com/render-examples/mongodb` in the repository search box. You can also fork [the repository](https://github.com/render-examples/mongodb) on GitHub or click `Use this template`.

2. Set the service's *Language* field to `Docker`.

3. The `master` branch uses the latest stable version of MongoDB. You can pick a different branch if you'd like to use a specific MongoDB version.

4. Under *Advanced*, add a disk with the following values:

   |                |                                                      |
   | -------------- | ---------------------------------------------------- |
   | *Mount Path* | `/data/db`                                           |
   | *Size*       | `10 GB` Feel free to change this to suit your needs. |

You're all set! Save your private service, and your MongoDB instance should be up in a few
minutes. You should be able to connect to it using the `host:port` displayed in the dashboard. It should look like
`mongo-xyz:27017`.

You can use the shell in your dashboard to connect to your database.

```shell
mongo --host mongo-xyz
```

[image: MongoDB Shell on Render]

## Backups

> Relying on a [disk snapshot](disks#disk-snapshots) to restore a database is not recommended. Restoring a disk snapshot will likely result in corrupted or lost database data.

Using a database’s recommended backup tool (for example: [mongodump](https://www.mongodb.com/docs/manual/core/backups/#back-up-with-mongodump)) is the recommended way to backup and restore a database without corrupted or lost data.