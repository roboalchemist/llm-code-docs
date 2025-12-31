# Source: https://planetscale.com/docs/vitess/tutorials/deployments/deploy-to-netlify.md

# Source: https://planetscale.com/docs/vitess/tutorials/deploy-to-netlify.md

# Deploy to Netlify

> This guide will walk you through setting up and deploying your PlanetScale database on Netlify.

<Note>
  This doc is intended for users that are manually storing a connection string in an environment variable in Netlify. If you want to use the Netlify integration, which handles this for you, see the [PlanetScale integration in the Netlify docs](https://docs.netlify.com/integrations/planetscale-integration).
</Note>

## Prerequisites

* A PlanetScale database — If you haven't created a database, refer to our [PlanetScale quickstart guide](/docs/vitess/tutorials/planetscale-quick-start-guide) to get started
* A [Netlify account](https://netlify.com/)
* A project deployed to Netlify — If you're just poking around and don't already have an application to deploy, you can use our [Next.js + PlanetScale sample](/docs/vitess/tutorials/connect-nextjs-app)

## Connecting your PlanetScale database to your Netlify application

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
            <img src="https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/deploy-to-netlify/prisma.png?fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=5223643d334fa7b6d57b3f49abfbaeed" alt="PlanetScale dashboard connect modal priority" data-og-width="3058" width="3058" data-og-height="1644" height="1644" data-path="docs/images/assets/docs/tutorials/deploy-to-netlify/prisma.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/deploy-to-netlify/prisma.png?w=280&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=e6f12bcde37364d056fb4aafb82ff652 280w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/deploy-to-netlify/prisma.png?w=560&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=7340c10cec9455bac5a646ad31accd7d 560w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/deploy-to-netlify/prisma.png?w=840&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=2a2e334d70a193c95d6e8e97d2327d68 840w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/deploy-to-netlify/prisma.png?w=1100&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=f23e9869ad71758206a3066091462b4b 1100w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/deploy-to-netlify/prisma.png?w=1650&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=ca11cdcede078f634ea54985cc979fbe 1650w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/deploy-to-netlify/prisma.png?w=2500&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=3886ae06e04d5a2075cb58a56c363ba1 2500w" />
    </Frame>
  </Step>

  <Step>
    Keep this page open, as you'll need to copy these to Netlify momentarily.
  </Step>

  <Step>
    If you navigate away from the page, and can no longer access the password, create a new password by repeating steps 1-5.
  </Step>
</Steps>

### Copy environment variables to Netlify

<Steps>
  <Step>
    Go to your Netlify dashboard.
  </Step>

  <Step>
    Click on your Netlify project.
  </Step>

  <Step>
    Click "**Site settings**".
  </Step>

  <Step>
    Click "**Build & deploy**," then "**Environment**".
  </Step>

  <Step>
    Click "**Edit variable**".
  </Step>

  <Step>
    Click "**New variable**" and copy each value from your PlanetScale dashboard into a new environment variable in Netlify. Once you're done with one, click "**Add**" and continue to the next, if applicable.
  </Step>
</Steps>

For example, if you're using Prisma, your connection string will look similar to this:

```bash  theme={null}
DATABASE_URL='mysql://xxxxxxxxx:************@xxxxxxxxxx.us-east-3.psdb.cloud/my-database?sslaccept=strict'
```

<Note>
  Your environment variable name will be the same in your application's code. We used `DATABASE_URL` as an example, but this can be given a different name.
</Note>

In Netlify, you'll set it as follows:

* **Key** = `DATABASE_URL`
* **Value** = `mysql://xxxxxxxxx:************@xxxxxxxxxx.us-east-3.psdb.cloud/my-database?sslaccept=strict`

<Info>
  The credentials are blurred for the example, but when you paste them in, use the actual values.
</Info>

<Frame>
    <img src="https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/deploy-to-netlify/environment-variables.png?fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=63adc643664622d94dd39f71b2a3022f" alt="Netlify dashboard - Environment variables" data-og-width="1890" width="1890" data-og-height="1066" height="1066" data-path="docs/images/assets/docs/tutorials/deploy-to-netlify/environment-variables.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/deploy-to-netlify/environment-variables.png?w=280&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=ac023209b24fc8c2a5ee8942f53b4a24 280w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/deploy-to-netlify/environment-variables.png?w=560&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=7f0e43c3f32c2b950843e790cf99985d 560w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/deploy-to-netlify/environment-variables.png?w=840&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=73c82080fe7654b3b3ee66aa3ae765e9 840w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/deploy-to-netlify/environment-variables.png?w=1100&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=c72efaa9df1d71e03e2333626f87e062 1100w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/deploy-to-netlify/environment-variables.png?w=1650&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=c8da466829a7349d59cbc7ebc3d19b2b 1650w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/deploy-to-netlify/environment-variables.png?w=2500&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=6902e1352cac203b2157de3f7afbbecc 2500w" />
</Frame>

After you have saved, you will need to rebuild the site with the new environment variable.

## What's next?

Learn more about how PlanetScale allows you to make [non-blocking schema changes](/docs/vitess/schema-changes) to your database tables without locking or causing downtime for production databases.

## Need help?

Get help from [the PlanetScale Support team](https://support.planetscale.com/), or join our [GitHub discussion board](https://github.com/planetscale/discussion/discussions) to see how others are using PlanetScale.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt