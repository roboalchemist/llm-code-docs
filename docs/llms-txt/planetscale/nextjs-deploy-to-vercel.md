# Source: https://planetscale.com/docs/vitess/tutorials/nextjs-deploy-to-vercel.md

# Deploy to Vercel

> This guide will walk you through setting up and deploying your PlanetScale database on Vercel.

It will cover two options:

<CardGroup>
  <Card title="Manually adding PlanetScale environment variables to your Vercel project" href="#manually-connect-to-vercel" icon="angles-right" />

  <Card title="Connecting your PlanetScale database to your application using the Vercel integration" href="#deploy-with-the-planetscale-vercel-integration" icon="angles-right" />
</CardGroup>

## Prerequisites

* A PlanetScale database — If you haven't created a database, refer to our [PlanetScale quickstart guide](/docs/vitess/tutorials/planetscale-quick-start-guide) to get started
* A [Vercel account](https://vercel.com/)
* A project deployed to Vercel — If you're just poking around and don't already have an application to deploy, you can use our [Next.js + PlanetScale sample](/docs/vitess/tutorials/connect-nextjs-app)

## Manually connect to Vercel

### Get your connection string from PlanetScale

<Steps>
  <Step>
    In your [PlanetScale dashboard](https://app.planetscale.com), click on the database you want to connect to.
  </Step>

  <Step>
    Click "**Connect**".
  </Step>

  <Step>
    Create a new password. Make sure to copy the password, as you'll only be shown it once.
  </Step>

  <Step>
    Select the framework you're using from the "**Select your language or framework**" section. This will give you the exact environment variable names you need for your selected framework. If your framework is not listed, choose "Other".

    <Frame>
            <img src="https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/deploy-to-vercel/prisma.png?fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=fac97227b034edf22a1c3656ed5d2fc7" alt="PlanetScale dashboard connect modal {priority}" data-og-width="3058" width="3058" data-og-height="1644" height="1644" data-path="docs/images/assets/docs/tutorials/deploy-to-vercel/prisma.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/deploy-to-vercel/prisma.png?w=280&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=04521f523c423e9c2b2f5fe91c5f233a 280w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/deploy-to-vercel/prisma.png?w=560&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=3b932dc84efe572119fa65a2fe5c0fb2 560w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/deploy-to-vercel/prisma.png?w=840&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=5d66cb5b2649222a6e7386e5624ceb7c 840w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/deploy-to-vercel/prisma.png?w=1100&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=394acb2d72332a7dc1c97902cf0f38b9 1100w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/deploy-to-vercel/prisma.png?w=1650&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=ba86e785c3f4b65b34194d8a1d968da9 1650w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/deploy-to-vercel/prisma.png?w=2500&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=b02f3870e62d865bd5f263255c9c60d4 2500w" />
    </Frame>
  </Step>

  <Step>
    Keep this page open, as you'll need to copy these to Vercel momentarily.
  </Step>

  <Step>
    If you navigate away from the page, and can no longer access the password, create a new password by repeating steps 1-5.
  </Step>
</Steps>

### Copy environment variables to Vercel

<Steps>
  <Step>
    Go to your Vercel dashboard.
  </Step>

  <Step>
    Click on your Vercel project.
  </Step>

  <Step>
    Click "**Settings**".
  </Step>

  <Step>
    Click "**Environment variables**".
  </Step>

  <Step>
    Copy each value from your PlanetScale dashboard into a new environment variable in Vercel. Once you're done with one, click "**Add**" and continue to the next, if applicable.
  </Step>
</Steps>

For example, if you're using Prisma, your connection string will look similar to this:

```bash  theme={null}
DATABASE_URL='mysql://xxxxxxxxx:************@xxxxxxxxxx.us-east-3.psdb.cloud/my_database?sslaccept=strict'
```

In Vercel, you'll set it as follows:

* **NAME** = `DATABASE_URL`
* **VALUE** = `mysql://xxxxxxxxx:************@xxxxxxxxxx.us-east-3.psdb.cloud/my_database?sslaccept=strict`

<Note>
  The credentials are blurred for the example, but when you paste them in, use the actual values.
</Note>

<Frame>
    <img src="https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/deploy-to-vercel/environment-variables.png?fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=67a6c07441bc0ae4d0f321643211a2a0" alt="Vercel dashboard - Environment variables" data-og-width="1400" width="1400" data-og-height="843" height="843" data-path="docs/images/assets/docs/tutorials/deploy-to-vercel/environment-variables.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/deploy-to-vercel/environment-variables.png?w=280&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=f85c3cd707e970253ebb67939123df2b 280w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/deploy-to-vercel/environment-variables.png?w=560&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=c2e65af344a33fe86250e698b01d26e0 560w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/deploy-to-vercel/environment-variables.png?w=840&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=d883079f64d02f3dd6dbec13cab3025b 840w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/deploy-to-vercel/environment-variables.png?w=1100&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=1b77728c5301f34b406ad1bc9943f82f 1100w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/deploy-to-vercel/environment-variables.png?w=1650&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=4ea56380aba4e8e8c83b10c9996864b6 1650w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/deploy-to-vercel/environment-variables.png?w=2500&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=ae5ba57fa910c64a2c202f317ca8884b 2500w" />
</Frame>

## Deploy with the PlanetScale Vercel integration

If you don't want to copy and paste the environment variables over to Vercel, you can use the [PlanetScale integration from the Vercel marketplace](https://vercel.com/integrations/planetscale). You can choose which database you want to connect to, and we'll automatically pull the necessary environment variables into your Vercel project.

<Steps>
  <Step>
    You must have an existing PlanetScale database to use the integration. You can create a database in the [PlanetScale dashboard](https://app.planetscale.com).
  </Step>

  <Step>
    Click "**Add integration**" on the [Vercel integrations page](https://vercel.com/integrations/planetscale).
  </Step>

  <Step>
    Select the Vercel account you want to connect with.
  </Step>

  <Step>
    On the left, you'll see the Vercel options, and on the right, the PlanetScale options.
  </Step>

  <Step>
    Select the Vercel project you want to connect to, and beneath that, select the framework you're using. If the framework isn't listed, select "**General**". This selection is what determines the names of the environment variables.
  </Step>

  <Step>
    On the right side, choose the [PlanetScale Organization](/docs/security/access-control) that the database is in. The integration will remain tied to this Organization and cannot be changed.
  </Step>

  <Step>
    Beneath that, select the database you want to connect to.
  </Step>

  <Step>
    Click "**Connect database**".
  </Step>

  <Step>
    Back in your Vercel dashboard, confirm the environment variables were added by going to your Vercel project > "**Settings**" > "**Environment variables**"
  </Step>
</Steps>

### Configure your connection

After you set up the initial connection, you also have the option to configure the PlanetScale connection, add more databases to the project, or remove databases from the project.

To access the configuration page:

<Steps>
  <Step>
    In your Vercel project dashboard, click "**Integrations**".
  </Step>

  <Step>
    Click the "**PlanetScale**" integration.
  </Step>

  <Step>
    Click the "**Configure**" button.
  </Step>
</Steps>

<Note>
  If you're modifying an existing connection on a Vercel project, these environment variable values will be regenerated and overwritten.
</Note>

<Note>
  * Environment variables are removed from all projects tied to the integration.
  * Your application will no longer be able to connect to your PlanetScale database.
</Note>

## What's next?

Learn more about how PlanetScale allows you to make [non-blocking schema changes](/docs/vitess/schema-changes) to your database tables without locking or causing downtime for production databases.

## Need help?

Get help from [the PlanetScale Support team](https://support.planetscale.com/), or join our [GitHub discussion board](https://github.com/planetscale/discussion/discussions) to see how others are using PlanetScale.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt