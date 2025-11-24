# Source: https://www.aptible.com/docs/how-to-guides/app-guides/migrate-nodjs-from-heroku-to-aptible.md

# How to migrate a NodeJS app from Heroku to Aptible

> Guide for migrating a NodeJS app from Heroku to Aptible

## Overview

Migrating applications from one PaaS to another might sound like a daunting task, but thankfully similarities between platforms makes transitioning easier than expected. However, while Heroku and Aptible are both PaaS applications with similar value props, there are some notable differences between them.

Today, developers are often switching to Aptible to access easier turn-key compliance and security at reasonable prices with stellar scalability and reliability.

One of the most common app types that’s transitioned over is a NodeJS app. We’ll guide you through the various considerations you need to make as well as give you a step-by-step guide to transition your NodeJS app to Aptible.

## Set up

Before starting, you should install Aptible’s CLI which will make setting configurations and deploying applications easier. The full guide on installing Aptible’s CLI can be found [here](/reference/aptible-cli/cli-commands/overview). Installing Aptible typically doesn’t take more than a few minutes.

Additionally, you should [set up an Aptible account](https://dashboard.aptible.com/signup) and create an Aptible app to pair with your existing project.

## Example

We’ll be moving over a stock NodeJS application with a Postgres database. However, if you use a different database, you’ll still be able to take advantage of most of this tutorial. We chose Postgres for this example because it is the most common stack pair.

## Things to consider

While Aptible and Heroku have a lot of similarities, there are some differences in how applications are organized and deployed. We’ll summarize those in this section before moving on to a traditional step-by-step guide.

### Aptible mandates Docker

While many Heroku projects already use Docker, Heroku projects can rely on just Git and Heroku’s [Buildpacks](https://elements.heroku.com/buildpacks/heroku/heroku-buildpack-nodejs). Because Heroku originally catered to hobbyists, supporting projects without a Dockerfile was appropriate.

However, Aptible’s focus on production-grade deployments and evergreen reliability mean all of our adopters use containerization. Accordingly, Aptible requires Dockerfiles to build an application, even if the application isn’t using the Docker registry.

If you don’t have a Dockerfile already, you can easily add one.

### Similar Constraints

Like Heroku, Aptible only supports Linux for deployments (with all apps run inside a Docker container). Also like Heroku, Aptible only supports packets via ports 80 and 443, corresponding to TCP / HTTP and TLS / HTTPS.

If you need to use UDP, your application will need to connect to an external service that manages UDP endpoints.

Additionally, like Heroku, Aptible applications are inherently ephemeral and are not expected to have persistent storage. While Aptible’s pristine state feature (which clears the app’s file system on a restart) can be disabled, it is not recommended. Instead, permanent storage should be delegated to an external service like S3 or Cloud Storage.

### Docker Support

Similar to Heroku, Aptible supports both (i) deploying applications via Dockerfile Deploy—where Aptible builds your image—or (ii) pulling a pre-built image from a Docker Registry.

### Aptible doesn’t mandate Procfiles

Unlike Heroku which requires Procfiles, Aptible considers Procfiles as optional. When a Procfile is missing, Aptible will infer command via the Dockerfile’s `CMD` declaration (known as an [Implicit Service](/how-to-guides/app-guides/define-services#implicit-service-cmd)). In short, Aptible requires Dockerfiles while Heroku requires Procfiles.

When switching over from Heroku, you can optionally keep your Procfile. Procfile syntax [is standardized](https://ddollar.github.io/foreman/) and is therefore consistent between Aptible and Heroku. Procfiles can be useful when an application has multiple services. However, you might need to change its location. If you are using the [Dockerfile Deploy](/how-to-guides/app-guides/deploy-from-git) approach, the Procfile should remain in your root director. However, if you are using [Direct Docker Image Deploy](/how-to-guides/app-guides/migrate-dockerfile-to-direct-image-deploy), the Procfile should be moved to `/.aptible/Procfile`.

Alternatively, for `.yaml` fans, you can use Aptible’s optional `.aptible.yml` format. Similar to Procfiles, applications using Dockerfile Deploy should store the `.aptible.yml` file in the root folder, while apps using Direct Docker Image Deploy should store them at `/.aptible/.aptible.yml`.

### Private Registry Authentication

If you are using Docker’s private registries, you’ll need to authorize Aptible to pull images from those private registries.

## Step-by-step guide

### 1. Create a Dockerfile (if you don’t have one already)

For users that don’t have a Dockerfile, you can create a Dockerfile by running

```node  theme={null}
touch Dockerfile
```

Next, we can add some contents, such as stating a node runtime, establishing a work directory, and commands to install packages.

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

Finally, we want to introduce a command for starting an application. We will use Docker’s `CMD` utility to accomplish this. `CMD` accepts an array of individual words. For instance, for **npm start** we could do:

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

### 2. Move over Procfiles (if applicable)

If you wish to still use your Procfile and also want to use Docker’s registry, you need to move your Procfile’s location into inside the `.aptible` folder. We can do this by running:

```js  theme={null}
mkdir .aptible #if it doesn't exist yet
cp Profile /.aptible/Procfile
```

### 3. Set up Aptible’s remote

Assuming you followed Aptible’s instructions to [provision your account](/getting-started/deploy-custom-code) and grant SSH access, you are ready to set Aptible as a remote.

```bash  theme={null}
git remote add aptible <your remote url> 
#your remote should look like ~ git@beta.aptible.com:<env name>/<app name>.git
```

### 4. Migrating databases

If you previously used Heroku PostgreSQL you’ll find comfort in Aptible’s [managed database solution](https://www.aptible.com/product#databases), which supports PostgreSQL, Redis, Elasticsearch, InfluxDB, mySQL, and MongoDB. Similar to Heroku, Aptible supports automated backups, replicas, failover logic, encryption, network isolation, and automated scaling.

Of course, beyond provisioning a new database, you will need to migrate your data from Heroku to Aptible. You may also want to put your database on maintenance mode when doing this to avoid additional data being written to the database during the process. You can accomplish that by running:

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

You can use your current environment, or [create a new environment](/core-concepts/architecture/environments). Then, we will use the Aptible CLI to connect to the database.

```bash  theme={null}
aptible db:tunnel "new_database" --environment "my_environment"
```

This should return the tunnel’s URL, e.g.:

<img src="https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/node-heroku-aptible.png?fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=d9df353b08a7b033e8bdbec48b3be8ce" alt="" data-og-width="2000" width="2000" data-og-height="1125" height="1125" data-path="images/node-heroku-aptible.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/node-heroku-aptible.png?w=280&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=b9e0f8d01302e69d65f977fc03c4ea86 280w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/node-heroku-aptible.png?w=560&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=11e7bf1ec1ae19fb76773680b1eaace6 560w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/node-heroku-aptible.png?w=840&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=e6dfe0ef50f8c6de69ee74bdb2107826 840w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/node-heroku-aptible.png?w=1100&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=598d5988509893ff51b2e1b8cb679b55 1100w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/node-heroku-aptible.png?w=1650&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=ba2aaaf476fad1a11ad5143af224e82f 1650w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/node-heroku-aptible.png?w=2500&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=862080b8de18f0b9777a96af0b59cb0d 2500w" />

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

And that’s it! Moving from Heroku to Aptible is actually a fairly simple process. With some modified configurations, you can switch PaaS platforms in less than a day.
