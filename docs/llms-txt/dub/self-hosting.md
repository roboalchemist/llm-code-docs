# Source: https://dub.co/docs/self-hosting.md

# Self-hosting Dub

> An end-to-end guide on how to self-host Dub – the open-source link attribution platform.

<Frame>
  <img src="https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/logo-background-gradient.png?fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=f32c52de94aaedcbc56bdf8b8e05d409" alt="Dub Logo on a gradient background" width="1200" height="630" data-og-width="1200" data-og-height="630" data-path="images/logo-background-gradient.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/logo-background-gradient.png?w=280&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=a636f495e47fc235f1e875d09ee78932 280w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/logo-background-gradient.png?w=560&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=c3887a857d4f0c6705d2e82b69a7924c 560w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/logo-background-gradient.png?w=840&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=dd6a66a791086fe615ab4241fa3e14ef 840w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/logo-background-gradient.png?w=1100&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=3df0b2b5a952fb71a9ddbb0cdbbbb103 1100w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/logo-background-gradient.png?w=1650&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=9193de40361c79058631c8c4eb725201 1650w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/logo-background-gradient.png?w=2500&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=a169891e21bae2e50d216901b1062d93 2500w" />
</Frame>

You can self-host Dub on your own servers and cloud infrastructure for greater control over your data and design. This guide will walk you through the entire process of setting up Dub on your own servers.

## Prerequisites

Before you begin, make sure you have the following:

* A [GitHub](https://github.com/) account
* A [Tinybird](https://www.tinybird.co/) account
* An [Upstash](https://upstash.com/) account
* A [PlanetScale](https://planetscale.com/) account
* A [Vercel](https://vercel.com/) account
* Either a [Cloudflare](https://www.cloudflare.com/) or [AWS](https://aws.com) account

You'll also need a custom domain that you will be using for your Dub instance, with an optional custom short domain for your links.

In this guide, we'll use `acme.com` as a placeholder for your custom domain, and `ac.me` as a placeholder for your custom short domain.

## Step 1: Local setup

First, you'll need to clone the Dub repo and install the dependencies.

<Steps>
  <Step title="Clone the repo">
    First, clone the [Dub repo](https://d.to/github) into a public GitHub repository. If you are planning to distribute the code or allow users to interact with the code remotely (e.g., as part of a hosted application), make sure to provide source access (including modifications) as required by the [AGPLv3 license](https://d.to/license).

    ```bash Terminal theme={null}
    git clone https://github.com/dubinc/dub.git
    ```
  </Step>

  <Step title="Install dependencies">
    Run the following command to install the dependencies:

    ```bash Terminal theme={null}
    pnpm i
    ```
  </Step>

  <Step title="Remove unnecessary files">
    Delete the `apps/web/vercel.json` file since cron jobs are not required for the self-hosted version:

    ```bash Terminal theme={null}
    rm apps/web/vercel.json
    ```
  </Step>

  <Step title="Set up environment variables">
    Convert the `.env.example` file to `.env`. You can start filling in the first few environment variables:

    ```bash Terminal theme={null}
    # The domain that your app will be hosted on
    NEXT_PUBLIC_APP_DOMAIN=acme.com
    # The short domain that your app will be using (could be the same as the above)
    NEXT_PUBLIC_APP_SHORT_DOMAIN=ac.me
    # The ID of the Vercel team that your app will be deployed to: https://vercel.com/docs/accounts/create-a-team#find-your-team-id
    TEAM_ID_VERCEL=
    # The unique access token for your Vercel account: https://vercel.com/guides/how-do-i-use-a-vercel-api-access-token
    AUTH_BEARER_TOKEN=
    ```

    You will fill in the remaining environment variables in the following steps.
  </Step>
</Steps>

## Step 2: Set up Tinybird Clickhouse database

Next, you'll need to set up the [Tinybird](https://tinybird.co) Clickhouse database. This will be used to store time-series click events data.

<Steps>
  <Step title="Create Tinybird Workspace">
    In your [Tinybird](https://tinybird.co/) account, create a new Workspace.

    Copy your `admin` [Auth Token](https://www.tinybird.co/docs/concepts/auth-tokens.html). Paste this token as the `TINYBIRD_API_KEY` environment variable in your `.env` file.
  </Step>

  <Step title="Install Tinybird CLI and authenticate">
    In your newly-cloned Dub repo, navigate to the `packages/tinybird` directory.

    Install the Tinybird CLI with `pip install tinybird-cli` (requires Python >= 3.8).

    Run `tb login` and paste your `admin` Auth Token.
  </Step>

  <Step title="Publish Tinybird datasource and endpoints">
    Run `tb deploy` to publish the datasource and endpoints in the `packages/tinybird` directory. You should see the following output (truncated for brevity):

    ```bash Terminal theme={null}
    $ tb deploy

    ** Processing ./datasources/click_events.datasource
    ** Processing ./endpoints/clicks.pipe
    ...
    ** Building dependencies
    ** Running 'click_events'
    ** 'click_events' created
    ** Running 'device'
    ** => Test endpoint at https://api.us-east.tinybird.co/v0/pipes/device.json
    ** Token device_endpoint_read_8888 not found, creating one
    ** => Test endpoint with:
    ** $ curl https://api.us-east.tinybird.co/v0/pipes/device.json?token=p.ey...NWeaoTLM
    ** 'device' created
    ...
    ```
  </Step>

  <Step title="Set up Tinybird API base URL">
    You will then need to update your [Tinybird API base URL](https://www.tinybird.co/docs/api-reference/api-reference.html#regions-and-endpoints) to match the region of your database.

    From the previous step, take note of the **Test endpoint** URL. It should look something like this:

    ```bash Terminal theme={null}
    Test endpoint at https://api.us-east.tinybird.co/v0/pipes/device.json
    ```

    Copy the base URL and paste it as the `TINYBIRD_API_URL` environment variable in your `.env` file.

    ```bash Terminal theme={null}
    TINYBIRD_API_URL=https://api.us-east.tinybird.co
    ```
  </Step>
</Steps>

## Step 3: Set up Upstash Redis database

Next, you'll need to set up the [Upstash](https://upstash.com) Redis database. This will be used to cache link metadata and serve link redirects.

<Steps>
  <Step title="Create Upstash database">
    In your [Upstash account](https://console.upstash.com/), create a new database.

    For better performance & read times, we recommend setting up a global database with several read regions.

    <Frame>    <img src="https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/upstash-create-db.png?fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=2ee9689bbeda53180edd455f8c956cd1" alt="Upstash Redis database" data-og-width="1136" width="1136" data-og-height="700" height="700" data-path="images/upstash-create-db.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/upstash-create-db.png?w=280&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=8b8dc7dd83e29c8db00f8355fca0ec61 280w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/upstash-create-db.png?w=560&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=71298ed8724a5d460e442cdf4116431b 560w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/upstash-create-db.png?w=840&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=fd5dc6a440f37a11cc4f4b41aa258f56 840w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/upstash-create-db.png?w=1100&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=6e178b4c8c8bb49a43e222d6fd700da3 1100w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/upstash-create-db.png?w=1650&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=e82e83548ed1c551acbe4cac993b1fd0 1650w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/upstash-create-db.png?w=2500&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=3433cb56300f917e0e383c950c7a48ce 2500w" /></Frame>
  </Step>

  <Step title="Set up Upstash environment variables">
    Once your database is created, copy the `UPSTASH_REDIS_REST_URL` and `UPSTASH_REDIS_REST_TOKEN` from the **REST API** section into your `.env` file.

    <Frame>    <img src="https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/upstash-redis-tokens.png?fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=18c2630daafe831a527a0986447ec63e" alt="Upstash Redis tokens" data-og-width="704" width="704" data-og-height="285" height="285" data-path="images/upstash-redis-tokens.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/upstash-redis-tokens.png?w=280&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=d7fc2a492b789e9f031a20cadedc7950 280w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/upstash-redis-tokens.png?w=560&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=13abd3ad52519c9e1d9c63c5e4fdf3d8 560w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/upstash-redis-tokens.png?w=840&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=290698786b30e1c7273fcb37e073bf72 840w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/upstash-redis-tokens.png?w=1100&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=47c9499ab1f8f73504a0c923bb65e785 1100w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/upstash-redis-tokens.png?w=1650&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=21a616076690d31f2c9017ea740e6c7c 1650w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/upstash-redis-tokens.png?w=2500&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=665dd5c816a1f2add0f9fa2e74c951ee 2500w" /></Frame>

    Navigate to the [QStash tab](https://console.upstash.com/qstash) and copy the `QSTASH_TOKEN`, `QSTASH_CURRENT_SIGNING_KEY`, and `QSTASH_NEXT_SIGNING_KEY` from the **Request Builder** section into your `.env` file.

    <Frame>
            <img src="https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/upstash-qstash-tokens.png?fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=e4d9708c4755d8ccf5d0049261fc4f04" alt="Upstash QStash tokens" data-og-width="692" width="692" data-og-height="264" height="264" data-path="images/upstash-qstash-tokens.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/upstash-qstash-tokens.png?w=280&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=62ce63fea95a613328082fa3b8c44799 280w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/upstash-qstash-tokens.png?w=560&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=776c3859e62443b2899cb8540dd74220 560w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/upstash-qstash-tokens.png?w=840&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=febf1cce0100b465b109abf0512f0a2a 840w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/upstash-qstash-tokens.png?w=1100&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=3f73f9d422ce9151c63fa83161f481c8 1100w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/upstash-qstash-tokens.png?w=1650&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=583a3c2b0032ede7a19a5069e3d735a3 1650w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/upstash-qstash-tokens.png?w=2500&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=b8d81db0d04fe8d157ce08938f80a6ac 2500w" />
    </Frame>
  </Step>
</Steps>

## Step 4: Set up PlanetScale MySQL database

Next, you'll need to set up a [PlanetScale](https://planetscale.com/)-compatible MySQL database. This will be used to store user data and link metadata.

<Note>
  PlanetScale recently [removed their free
  tier](https://planetscale.com/blog/planetscale-forever), so you'll need to pay
  for this option. A cheaper alternative is to use a [MySQL database on
  Railway](https://railway.app/template/mysql) (\$5/month).

  For [local development](local-development), we recommend using a [local MySQL database
  with PlanetScale simulator](local-development#option-1-local-mysql-database-with-planetscale-simulator-recommended) (100% free).
</Note>

<Steps>
  <Step title="Create PlanetScale database">
    In your [PlanetScale account](https://app.planetscale.com/), create a new database.

    Once your database is created, you'll be prompted to select your language or Framework. Select **Prisma**.

    <Frame>
            <img src="https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/planetscale-choose-framework.png?fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=c3fc78f41d81058aef9dcfa4b8b7b85e" alt="PlanetScale choose framework" data-og-width="1342" width="1342" data-og-height="832" height="832" data-path="images/planetscale-choose-framework.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/planetscale-choose-framework.png?w=280&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=bfc938c736d0f5c167b6923c47231dbe 280w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/planetscale-choose-framework.png?w=560&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=80d6b3e51ed81b0d2fc8b7cae4960f88 560w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/planetscale-choose-framework.png?w=840&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=0874c505c7d81ffef35c598a9928326d 840w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/planetscale-choose-framework.png?w=1100&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=f56173ab5bde31e34f4ca2f76164678d 1100w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/planetscale-choose-framework.png?w=1650&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=6ac0f0a26ff7d2b4e3d3cb85cda3955e 1650w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/planetscale-choose-framework.png?w=2500&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=64a709af05dbed2f220b6318aae53711 2500w" />
    </Frame>
  </Step>

  <Step title="Set up PlanetScale environment variables">
    Then, you'll have to create a new password for your database. Once the password is created, scroll down to the **Add credentials to .env** section and copy the `DATABASE_URL` into your `.env` file.

    <Frame>
            <img src="https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/planetscale-add-credentials.png?fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=e942daf967c745ea5050bca9f21d249a" alt="PlanetScale add credentials" data-og-width="1315" width="1315" data-og-height="434" height="434" data-path="images/planetscale-add-credentials.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/planetscale-add-credentials.png?w=280&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=bbab7ca87889d90ecb5da26392da6cde 280w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/planetscale-add-credentials.png?w=560&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=0ab022859606d358ff75cce2b81acadf 560w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/planetscale-add-credentials.png?w=840&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=e65e67b801dd24a7becf4effcf56a2e2 840w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/planetscale-add-credentials.png?w=1100&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=3178fc3db20b2c2d44fcf4b8bcf7e333 1100w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/planetscale-add-credentials.png?w=1650&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=d77e105b4b0e634c59ebd582c73b0723 1650w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/planetscale-add-credentials.png?w=2500&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=8a9584d70e60c5dbced3a344353fe874 2500w" />
    </Frame>
  </Step>

  <Step title="Generate Prisma client and create database tables">
    In your Dub codebase, navigate to `apps/web/prisma/schema.prisma` and replace all the columns in the `DefaultDomains` model to the normalized version of your custom short domain (removing the `.` character).

    For example, if your custom short domain is `ac.me`, your `DefaultDomains` model should look like this:

    ```prisma apps/web/prisma/schema.prisma theme={null}
    model DefaultDomains {
      id          String   @id @default(cuid())
      acme        Boolean  @default(true)
      projectId   String   @unique
      project     Project  @relation(fields: [projectId], references: [id], onDelete: Cascade)
    }
    ```

    In the terminal, navigate to the `apps/web` directory and run the following command to generate the Prisma client:

    ```bash Terminal theme={null}
    pnpm run prisma:generate
    ```

    Then, create the database tables with the following command:

    ```bash Terminal theme={null}
    pnpm run prisma:push
    ```
  </Step>
</Steps>

## Step 5: Set up GitHub OAuth

Next, [create a new GitHub App](https://github.com/settings/applications/new). This will allow you to sign in to Dub with your GitHub account.

Don't forget to set the following Callback URLs:

* `https://app.acme.com/api/auth/callback/github`
* `http://localhost:8888/api/auth/callback/github` for local development.

<Info>
  Optional: Set the "Email addresses" account permission to **read-only** in
  order to access private email addresses on GitHub.
</Info>

Once your GitHub App is created, copy the `Client ID` and `Client Secret` into your `.env` file as the `GITHUB_CLIENT_ID` and `GITHUB_CLIENT_SECRET` environment variables.

## Step 6: Set up Cloudflare R2

Dub stores user-generated assets in either S3 or S3-compatible services like [Cloudflare R2](https://cloudflare.com/r2). These include:

* Project logos
* User avatars
* [Custom Social Media Cards](https://dub.co/help/article/custom-link-previews) images

We recommend using [Cloudflare R2](https://cloudflare.com/r2) for self-hosting Dub, as it's a more cost-effective solution compared to AWS S3. Here's how you can set it up:

<Steps>
  <Step title="Create R2 bucket">
    <Note>You'll need to subscribe to the R2 service if you haven't already.</Note>

    In your [Cloudflare account](https://dash.cloudflare.com/), create a new R2 bucket. We recommend giving your bucket a descriptive name (e.g. `dubassets`) and leaving the remaining settings as is.

    <Frame>    <img src="https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/cloudflare-r2-create-bucket.png?fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=5738442754e0e38dcf857eb93e06c97d" alt="Cloudflare R2 bucket" data-og-width="1736" width="1736" data-og-height="1500" height="1500" data-path="images/cloudflare-r2-create-bucket.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/cloudflare-r2-create-bucket.png?w=280&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=f942ae053c3d0603397e658da6c97a4f 280w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/cloudflare-r2-create-bucket.png?w=560&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=378f709b7db6bbd3f340fea9fdb02fe9 560w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/cloudflare-r2-create-bucket.png?w=840&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=30a0b73039ee2eb69bdebef89e56e7e5 840w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/cloudflare-r2-create-bucket.png?w=1100&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=d21f034c1d95a21745ddb8b8a9109215 1100w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/cloudflare-r2-create-bucket.png?w=1650&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=756775954f026e73530f5b7152ba5ae9 1650w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/cloudflare-r2-create-bucket.png?w=2500&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=ced219ecfc8fcf99dac7680222ca4f19 2500w" /></Frame>

    In your bucket settings, copy the **S3 API** value – you'll need it in Step 3.
  </Step>

  <Step title="Set up access to R2">
    From the R2 main page, click **Manage R2 API Tokens** on the right-hand column.

    <Frame>
            <img src="https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/cloudflare-r2-manage-api-tokens.png?fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=bc4a1b1d65065019f7d80cff8c27a82d" alt="Cloudflare manage API tokens" data-og-width="2368" width="2368" data-og-height="1008" height="1008" data-path="images/cloudflare-r2-manage-api-tokens.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/cloudflare-r2-manage-api-tokens.png?w=280&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=1e207cf199900d21d63866252760c6ae 280w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/cloudflare-r2-manage-api-tokens.png?w=560&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=11a3f9d7d4e049126f969addc210ebec 560w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/cloudflare-r2-manage-api-tokens.png?w=840&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=12bcf69e77d1f6b6f1cccd06a9c3101c 840w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/cloudflare-r2-manage-api-tokens.png?w=1100&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=3d874ca332713007941976b0735e1768 1100w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/cloudflare-r2-manage-api-tokens.png?w=1650&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=00637d5d6d678a14bb4bb908e1f396dc 1650w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/cloudflare-r2-manage-api-tokens.png?w=2500&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=5f455bc1b654c143e0951d5978b94908 2500w" />
    </Frame>

    Then, click **Create API Token**.

    <Frame>
            <img src="https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/cloudflare-r2-create-api-token.png?fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=f8a5315ec1bc72ccf5d2954b9aec543b" alt="Cloudflare R2 API token" data-og-width="2178" width="2178" data-og-height="1490" height="1490" data-path="images/cloudflare-r2-create-api-token.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/cloudflare-r2-create-api-token.png?w=280&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=2f15dceca688e55722e7deb6781b1b89 280w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/cloudflare-r2-create-api-token.png?w=560&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=29f9b94feaba94549170aa00e33a322d 560w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/cloudflare-r2-create-api-token.png?w=840&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=7708f40771128044e5192bd83be66599 840w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/cloudflare-r2-create-api-token.png?w=1100&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=63c954089d1fc20022aa8f88cfdd0b7f 1100w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/cloudflare-r2-create-api-token.png?w=1650&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=1c38d55aebf0415b5fe03d5bcbe48067 1650w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/cloudflare-r2-create-api-token.png?w=2500&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=b5074654de1a23ee898f4125e13e16f9 2500w" />
    </Frame>

    Make sure to name your API token something relevant to the service that will be using the token.

    Give it "Object Read & Write" permissions, and we recommend only applying ito to a single bucket.

    You can leave the remaining settings (TTL, Client IP Address Filtering) as is, and click **Create API Token**.

    After you create you token, copy the `Access Key ID` and `Secret Access Key` values – you'll need them in the next step.
  </Step>

  <Step title="Set up R2 environment variables">
    Once you have your credentials, set them in your `.env` file:

    ```TypeScript .env theme={null}
    STORAGE_ACCESS_KEY_ID= // this is the Access Key ID value from Step 2
    STORAGE_SECRET_ACCESS_KEY= // this is the Secret Access Key value from Step 2
    STORAGE_ENDPOINT= // this is the S3 API value from Step 1
    ```
  </Step>

  <Step title="Set up R2 domain">
    In order for your images to be publically accessible in R2 you need to setup a domain. You can either use your own domain or an R2.dev subdomain.

    To use your own domain, you'll need to create a CNAME record in your DNS settings that points to your R2 bucket.

    In you plan to use an R2.dev subdomain, make sure you "Allow Access".

    Then set the `STORAGE_BASE_URL` in your `.env` file to the domain you chose.

    ```bash  theme={null}
    STORAGE_BASE_URL={URL your assets as available at} # https://static.example.com
    ```

    <Frame>    <img src="https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/cloudflare-r2-public-domain.png?fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=11f9d787953bed9d32da706cb35db8b4" alt="Cloudflare R2 domain" data-og-width="2200" width="2200" data-og-height="1182" height="1182" data-path="images/cloudflare-r2-public-domain.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/cloudflare-r2-public-domain.png?w=280&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=80ab5c8b0bf44b0316e093816d574cd4 280w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/cloudflare-r2-public-domain.png?w=560&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=8952be438553ca89453e33ab3a19a7ca 560w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/cloudflare-r2-public-domain.png?w=840&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=dd5d2716da776cf546017ed2972d047a 840w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/cloudflare-r2-public-domain.png?w=1100&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=f8b222010864b652cafc87767acdb94a 1100w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/cloudflare-r2-public-domain.png?w=1650&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=5797c9fec2048496967f94940109e63f 1650w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/cloudflare-r2-public-domain.png?w=2500&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=f7b4eceb299b3b3dd540e2e61b51eba0 2500w" /></Frame>
  </Step>
</Steps>

## Step 7: Set up Resend (optional)

<Note>
  Note that if you want to use magic link sign-in, this is a required step.
</Note>

Next, you'll need to set up Resend for transactional emails (e.g. magic link emails):

1. Sign up for Resend and [create your API key here](https://resend.com/api-keys).
2. Copy the API key into your `.env` file as the `RESEND_API_KEY` environment variable.
3. You'll then need to set up and verify your domain by [following this guide here](https://resend.com/docs/dashboard/domains/introduction).

## Step 8: Set up Unsplash (optional)

Dub uses Unsplash's API for the [Custom Social Media Cards](https://dub.co/help/article/custom-link-previews) feature. You'll need to set up an Unsplash application to get an access key.

<Frame>
  ![Custom social media
  cards](https://assets.dub.co/changelog/custom-social-cards.png)
</Frame>

Check out Unsplash's [official documentation](https://unsplash.com/documentation#creating-a-developer-account) to learn how you can set up the `UNSPLASH_ACCESS_KEY` env var.

## Step 9: Deploy to Vercel

Once you've set up all of the above services, you can now deploy your app to Vercel.

<Steps>
  <Step title="Deploy code to GitHub">
    If you haven't already, push up your cloned repository to GitHub by running the following commands:

    ```bash Terminal theme={null}
    git add .
    git commit -m "Initial commit"
    git push origin main
    ```
  </Step>

  <Step title="Create a new Vercel project">
    In your [Vercel account](https://vercel.com/), create a new project. Then, select your GitHub repository and click **Import**.

    Make sure that your **Framework Preset** is set to **Next.js** and the **Root Directory** is set to `apps/web`.

    <Frame>
            <img src="https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/vercel-framework-preset.png?fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=66f6fb79a6c101ab92c63c1e0735b9e0" alt="Vercel Framework Preset and Root Directory" data-og-width="923" width="923" data-og-height="626" height="626" data-path="images/vercel-framework-preset.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/vercel-framework-preset.png?w=280&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=7e05bade332fda48432e929a0aa6917d 280w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/vercel-framework-preset.png?w=560&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=66974d3265e41b51384c3b5108064d25 560w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/vercel-framework-preset.png?w=840&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=ae2009c4b785545c130ed5aa4719841c 840w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/vercel-framework-preset.png?w=1100&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=f6b64064132f3c9506c1b8c1160b48f6 1100w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/vercel-framework-preset.png?w=1650&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=46387bc8ac0cde9a671810b03b711325 1650w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/vercel-framework-preset.png?w=2500&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=bb817e7f7dce533cb0ccfe32a1cf9891 2500w" />
    </Frame>

    In the **Environment Variables** section, add all of the environment variables from your `.env` file by copying all of them and pasting it into the first input field. A few notes:

    * Remove the `PROJECT_ID_VERCEL` environment variable for now since we will only get the project ID after deploying the project.
    * Replace the `NEXTAUTH_URL` environment variable with the app domain that you will be using (e.g. `https://app.acme.com`).

    Click on **Deploy** to deploy your project.

    <Tip>
      If you get a `No Output Directory called "public" was found after the build
            completed` error, make sure that your [Vercel deployment
      settings](https://vercel.com/docs/deployments/configure-a-build) to make sure that they match the following:

      <Frame>
                <img src="https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/vercel-deploy-settings.png?fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=25dddd473baa61b71cc17f46250ab026" alt="Vercel Deploy settings" data-og-width="965" width="965" data-og-height="881" height="881" data-path="images/vercel-deploy-settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/vercel-deploy-settings.png?w=280&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=c4496e1a97abe3e1383149d7d61915c6 280w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/vercel-deploy-settings.png?w=560&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=1638b59927ae6fc2a7ae710da08e8ab7 560w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/vercel-deploy-settings.png?w=840&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=8aa3e8e0fdd5847d250ba1daa2f36008 840w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/vercel-deploy-settings.png?w=1100&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=7b5fc987cdee7ce46a86f0ebc0709252 1100w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/vercel-deploy-settings.png?w=1650&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=369ee63ec45956ae06c97e6f81841b60 1650w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/vercel-deploy-settings.png?w=2500&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=65f4645c463019a006112beb10a76400 2500w" />
      </Frame>
    </Tip>
  </Step>

  <Step title="Add required environment variables">
    Once the project deploys, retrieve your [Vercel project ID](https://vercel.com/docs/projects/overview#project-id) and add it as the `PROJECT_ID_VERCEL` environment variable – both in your `.env` file and in your newly created Vercel project's settings (under **Settings > Environment Variables**)

    Add both the `NEXT_PUBLIC_APP_DOMAIN` and `NEXT_PUBLIC_APP_SHORT_DOMAIN` as domains in your Vercel project's settings (under **Settings** > **Domains**). You can follow this guide to learn [how to set up a custom domain on Vercel](https://vercel.com/docs/projects/domains/add-a-domain).
  </Step>

  <Step title="Redeploy your Vercel project">
    Go back to the **Deployments** page and redeploy your project.

    Once the deployment is complete, you should be able to visit your app domain (e.g. `https://app.acme.com`) and see the following login page:

    <Frame>    <img src="https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/whitelabeled-login.png?fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=709be2c8b07d066666910754f1dfc591" alt="Whitelabeled Login" data-og-width="1488" width="1488" data-og-height="956" height="956" data-path="images/whitelabeled-login.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/whitelabeled-login.png?w=280&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=47cf969fc35a9280386a3d49cf4c28a2 280w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/whitelabeled-login.png?w=560&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=59d5e848389e33cc843cdc360fe1cd7c 560w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/whitelabeled-login.png?w=840&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=43a9b476e9032d57c68089ce7bad10fe 840w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/whitelabeled-login.png?w=1100&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=9ea0afb64097a4234cad7c59b4caea2e 1100w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/whitelabeled-login.png?w=1650&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=532c32e04c756c344717ed91810148a9 1650w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/whitelabeled-login.png?w=2500&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=7f3593559e2219d2d8222923f8d27e2d 2500w" /></Frame>
  </Step>
</Steps>

## Caveats

This guide is meant to be a starting point for self-hosting Dub. It currently depends on the following services to work:

* [Tinybird](https://www.tinybird.co/) for the analytics database
* [Upstash](https://upstash.com/) for the Redis database
* [PlanetScale](https://planetscale.com/) for the MySQL database
* [Vercel](https://vercel.com/) for hosting & [Edge Middleware](https://vercel.com/docs/functions/edge-middleware)

In the future, we plan to make it easier to self-host Dub by making these dependencies optional by swapping them out for native databases (e.g. mysql, redis, clickhouse, [GeoLite2](https://github.com/GitSquared/node-geolite2-redist) etc.)

Also, Docker is currently not supported, but we have a few [open](https://github.com/dubinc/dub/issues/25) [issues](https://github.com/dubinc/dub/issues/378) and [PRs](https://github.com/dubinc/dub/pull/391) for it.
