# Source: https://planetscale.com/docs/vitess/tutorials/connect-nextjs-app.md

# Connect a Next.js application to PlanetScale

In this tutorial, you'll create a [Next.js](https://nextjs.org/) application that uses [Tailwind CSS](https://tailwindcss.com/) for styling and [Prisma](https://www.prisma.io/) to connect to a [PlanetScale](/) database.

## Prerequisites

* [Node.js](https://nodejs.org/en/download/)
* A [PlanetScale account](https://auth.planetscale.com/sign-up)

## Set up the database

If this is your first time in the dashboard, you'll be prompted to go through a database creation walkthrough where you'll create a new database. Otherwise, click "**New database**" > "**Create new database**".

* **Name** — You can use any name with lowercase, alphanumeric characters, or underscores. We also permit dashes, but don't recommend them, as they may need to be escaped in some instances.
* **Plan type** — Select the [desired plan](/docs/planetscale-plans) for your database.
* **Region** — Choose the [region](/docs/vitess/regions#available-regions) closest to you or your application. It's important to note if you intend to make this branch a production branch, you will not be able to change the region later, so choose the region with this in mind.

Finally, click "**Create database**".

<Note>
  If you have an existing cloud-hosted database, you can also choose the "Import" option to import your database to PlanetScale using our Import tool. If you go this route, we recommend using our [Database Imports documentation](/docs/vitess/imports/database-imports).
</Note>

A [production branch](/docs/vitess/schema-changes/branching), `main`, is automatically created when you create your database. Production branches are highly available, protected database that you can connect your production application to. Once you are satisfied with your initial development, you may enable [safe migrations](/docs/vitess/schema-changes/safe-migrations) to enable zero-downtime migrations and protect the branch from accidental data deletion.

## Set up the starter Next.js app

Now that you have your database, clone the [Next.js starter repository](https://github.com/planetscale/nextjs-starter), or grab your own project.

```sh  theme={null}
git clone https://github.com/planetscale/nextjs-starter
```

Install the dependencies with:

```sh  theme={null}
cd nextjs-starter
npm install
```

Create your `.env` file by renaming the `.env.example` file to `.env`:

```sh  theme={null}
mv .env.example .env
```

## Generate a connection string

Next, you need to generate a database username and password so that you can use it to connect to your application.

In your PlanetScale dashboard, select your database, click "**Connect**", and select "**Prisma**" from the "**Connect with**" dropdown.

As long as you're an organization administrator, this will generate a username and password that has administrator privileges to the database.

Copy the `DATABASE_URL` string from the `.env` tab and paste it into your own `.env` file. The structure will look like this:

```sh  theme={null}
DATABASE_URL='mysql://<USERNAME>:<PASSWORD>@<HOST>/<DATABASE_NAME>?sslaccept=strict'
```

For `DATABASE_NAME`, you can use your PlanetScale database name directly if you have a *single unsharded keyspace*. If you have a sharded keyspace, you'll need to use `@primary`. This will automatically direct incoming queries to the correct keyspace/shard. For more information, see the [Targeting the correct keyspace documentation](/docs/vitess/sharding/targeting-correct-keyspace).

Your PlanetScale database should now be connected to your application.

## Add the schema and data

With the database connected, you're now ready to add a schema, and read/write data.

The sample repo we shared above includes a pre-built schema and some seed data built with Prisma. Push the database schema to your PlanetScale database with:

```sh  theme={null}
npx prisma db push
```

Run the seed script. This will populate your database with `Product` and `Category` data:

```sh  theme={null}
npm run seed
```

## Run the app

Run the app with following command:

```sh  theme={null}
npm run dev
```

Open your browser at [localhost:3000](http://localhost:3000) to see the running application.

## Deploy your app

After you have your application running locally, you may want to deploy it to production. Your database branch (`main` by default) is already a production database branch. You should also enable [safe migrations](/docs/vitess/schema-changes/safe-migrations), which protects your production branch from accidental schema changes. This can be done from the PlanetScale dashboard by clicking the same **"cog"** once the branch has been promoted to production.

In the modal that will appear, toggle the option labeled **"Enable safe migrations"**, then click the **"Enable safe migrations"**. This will close the modal and save the setting.

<Frame>
    <img src="https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/connect-nextjs-app/prod-branch-options-modal.png?fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=188775a86603816ad0f0c900cdf1fe85" alt="Enable safe migrations" data-og-width="1368" width="1368" data-og-height="1134" height="1134" data-path="docs/images/assets/docs/tutorials/connect-nextjs-app/prod-branch-options-modal.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/connect-nextjs-app/prod-branch-options-modal.png?w=280&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=5f5acc74e56d8aedcaa5d5e5b347f948 280w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/connect-nextjs-app/prod-branch-options-modal.png?w=560&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=a217c533e52e021ff824e56d6a7ee91a 560w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/connect-nextjs-app/prod-branch-options-modal.png?w=840&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=f103551ae71cafee6b6c16ae0c5a2211 840w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/connect-nextjs-app/prod-branch-options-modal.png?w=1100&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=9651667ab473245471968d8c4746b038 1100w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/connect-nextjs-app/prod-branch-options-modal.png?w=1650&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=76f01afb085141b8708705321c0c28f3 1650w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/connect-nextjs-app/prod-branch-options-modal.png?w=2500&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=8361c28a1fcb824d955b8e9f70e64891 2500w" />
</Frame>

### Deploy to Vercel

If you'd like to deploy to Vercel, check out our [Deploy to Vercel documentation](/docs/vitess/tutorials/deploy-to-vercel).

### Deploy to Netlify

If you'd like to deploy to Netlify, check out our [Deploy to Netlify documentation](/docs/vitess/tutorials/deploy-to-netlify).

<Note>
  If you are deploying the `nextjs-starter` repo, the `Netlify.toml` file in this repository includes the configuration for you to customize the `PLANETSCALE_PRISMA_DATABASE_URL` property on the initial deploy.
</Note>

## What's next?

To learn more about PlanetScale, take a look at the following resources:

* [PlanetScale workflow](/docs/vitess/best-practices) — Quick overview of the PlanetScale workflow: branching, non-blocking schema changes, deploy requests, and reverting a schema change.
* [PlanetScale branching](/docs/vitess/schema-changes/branching) — Learn how to utilize branching to ship schema changes with no locking or downtime.
* [PlanetScale CLI](/docs/cli) — Power up your workflow with the PlanetScale CLI. Every single action you just performed in this quickstart (and much more) can also be done with the CLI.

## Need help?

Get help from [the PlanetScale Support team](https://support.planetscale.com/), or join our [GitHub discussion board](https://github.com/planetscale/discussion/discussions) to see how others are using PlanetScale.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt