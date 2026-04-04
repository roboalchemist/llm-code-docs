# Source: https://render.com/docs/deploy-mattermost.md

# Deploy Mattermost

[Mattermost](https://mattermost.com) is an open source messaging platform with an easy-to-use and
familiar web interface. It is customizable and can run as a simple standalone web server or as a
complex, clustered, multi-process service connected to separate database, object storage, LDAP
directory, search engine, and mail service, among other things. All of these configurations can be
installed on Render.

In this tutorial, you'll run a Mattermost instance consisting of a Mattermost web service, a
PostgreSQL database, and a [MinIO](https://min.io/) object store backed by a [persistent,
snapshotted disk](disks). Alternatively, if you just want Mattermost up and running, follow the one-click deploy steps.

## One-Click Deploy

Click *Deploy to Render* below and follow the prompts to set up Mattermost on Render.

<deploy-to-render repo="https://github.com/render-examples/mattermost">
</deploy-to-render>

## Manual Deploy

We'll be using
[github.com/render-examples/mattermost](https://github.com/render-examples/mattermost), so start by
forking that repository.

### Create the Database

[Create](https://dashboard.render.com/new/database) a new PostgreSQL database on Render.

You'll need various properties from this database when you're creating the Mattermost service.

### Create the MinIO Service

1. Go [here](https://dashboard.render.com/select-repo?type=pserv) to begin creating a new private
   service.

2. Use the forked Mattermost repository.

3. Add these two environment variables:

   | Key                | Value                                |
   | ------------------ | ------------------------------------ |
   | `MINIO_ACCESS_KEY` | Supply your own value or generate it |
   | `MINIO_SECRET_KEY` | Supply your own value or generate it |

   These values will be needed for the Mattermost service later.

4. Add a disk with `/data` as the mount path.

5. Set the Docker build context directory to `./minio` and the Dockerfile path to `./minio/Dockerfile`.

6. Create the service.

### Create the Mattermost Service

1. Go [here](https://dashboard.render.com/select-repo?type=web) to begin creating a new web service.

2. Use the forked Mattermost repository.

3. Add the following environment variables:

   | Key                                       | Value                                               |
   | ----------------------------------------- | --------------------------------------------------- |
   | `MM_SQLSETTINGS_DRIVERNAME`               | `postgres`                                          |
   | `MM_USERNAME`                             | The username from the database created earlier      |
   | `MM_PASSWORD`                             | The password from the database created earlier      |
   | `MM_DBNAME`                               | The database name from the database created earlier |
   | `DB_HOST`                                 | The hostname from the database created earlier      |
   | `MM_FILESETTINGS_DRIVERNAME`              | `amazons3`                                          |
   | `MM_FILESETTINGS_AMAZONS3BUCKET`          | `mattermost`                                        |
   | `MM_FILESETTINGS_AMAZONS3ACCESSKEYID`     | The `MINIO_ACCESS_KEY` from MinIO created earlier   |
   | `MM_FILESETTINGS_AMAZONS3SECRETACCESSKEY` | The `MINIO_SECRET_KEY` from MinIO created earlier   |
   | `MM_FILESETTINGS_AMAZONS3ENDPOINT`        | The `host:port` from the MinIO created earlier      |
   | `MM_FILESETTINGS_AMAZONS3SSL`             | `false`                                             |

4. Add a disk with `/mattermost/config` as the mount path.

5. Set the Docker build context directory to `./app` and the Dockerfile path to `./app/Dockerfile`.

6. Create the service.

Your Mattermost cluster should be ready to use with regular backups and disk snapshots!