# Source: https://docs.turso.tech/features/embedded-replicas/with-render.md

# Turso + Render

> Deploy a JavaScript app using [Turso embedded replicas](/features/embedded-replicas) to [Render](https://render.com/).

<img src="https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/platforms/render-banner.png?fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=6e416c1d54d38e041de310997834574e" alt="Render banner" data-og-width="1133" width="1133" data-og-height="595" height="595" data-path="images/platforms/render-banner.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/platforms/render-banner.png?w=280&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=ba8f9b05eec5513e77472bc58aeed6f6 280w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/platforms/render-banner.png?w=560&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=0f641d33347d1f9489f4d54732c63af9 560w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/platforms/render-banner.png?w=840&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=442b19fd3617b08f6d9f1cd70f389e43 840w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/platforms/render-banner.png?w=1100&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=98443de6f20cf710f3b56961a962068f 1100w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/platforms/render-banner.png?w=1650&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=c1a0c7b2acdfbc6e3a5e010578c9d99d 1650w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/platforms/render-banner.png?w=2500&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=64af00e16f300cf2885e5680c668cf9a 2500w" />

## Prerequisites

Before you start, make sure you:

* [Install the Turso CLI](/cli/installation)
* [Sign up or login to Turso](/cli/authentication#signup)
* Have a Render account - [create one](https://dashboard.render.com/)

<Steps>
  <Step title="Retrieve database credentials">
    You will need an existing database to continue. If you don't have one, [create one](/quickstart).

    <Snippet file="retrieve-database-credentials.mdx" />

    <Info>You will want to store these as environment variables.</Info>
  </Step>

  <Step title="Get application code">
    Fork the following embedded replica project from GitHub locally:

    <Card title="My Expenses Tracker - (Elysia + Bun)" icon="github" href="https://github.com/tursodatabase/embedded-replicas-with-js">
      See the full source code
    </Card>

    <Note>
      Or, you can:

      <Card title="Deploy to Render with a single-click" href="https://render.com/deploy?repo=https://github.com/tursodatabase/embedded-replicas-with-js" />
    </Note>
  </Step>

  <Step title="Create a web service">
    Create a new Render **Web Service** by clicking on the "New Web Service" button on the Web Services card inside you Render dashboard.
  </Step>

  <Step title="Connect to Git repository">
    1. Select "build and deploy from a Git repository" and proceed to the next page.

    2. Click on "Connect" for your target project repository
  </Step>

  <Step title="Set project's environment variables">
    On the web service configuration page, under "Advanced" add **a secret file** and fill it in with your database secret credentials:

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/turso/features/embedded-replicas/images/platforms/render-env-vars.png" alt="Render secret credentials" />
  </Step>

  <Step title="Deploy project">
    Scroll to the bottom of the web service configuration page and click on "Create Web Service".
  </Step>
</Steps>
