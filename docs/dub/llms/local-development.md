# Source: https://dub.co/docs/local-development.md

> ## Documentation Index
> Fetch the complete documentation index at: https://dub.co/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Local development

> A guide on how to run Dub's codebase locally.

<Frame>
  <img src="https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/logo-background-gradient.png?fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=f32c52de94aaedcbc56bdf8b8e05d409" alt="Dub Logo on a gradient background" width="1200" height="630" data-og-width="1200" data-og-height="630" data-path="images/logo-background-gradient.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/logo-background-gradient.png?w=280&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=a636f495e47fc235f1e875d09ee78932 280w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/logo-background-gradient.png?w=560&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=c3887a857d4f0c6705d2e82b69a7924c 560w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/logo-background-gradient.png?w=840&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=dd6a66a791086fe615ab4241fa3e14ef 840w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/logo-background-gradient.png?w=1100&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=3df0b2b5a952fb71a9ddbb0cdbbbb103 1100w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/logo-background-gradient.png?w=1650&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=9193de40361c79058631c8c4eb725201 1650w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/logo-background-gradient.png?w=2500&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=a169891e21bae2e50d216901b1062d93 2500w" />
</Frame>

## Introduction

Dub's codebase is set up in a monorepo (via [Turborepo](https://turbo.build/repo)) and is fully [open-source on GitHub](https://github.com/dubinc/dub).

Here's the monorepo structure:

```
apps
├── web
packages
├── cli
├── email
├── embeds
├── prisma
├── stripe-app
├── tailwind-config
├── tinybird
├── tsconfig
├── ui
├── utils
```

The `apps` directory contains the code for:

* `web`: The entirety of Dub's application ([app.dub.co](https://app.dub.co)) + our link redirect infrastructure.

The `packages` directory contains the code for:

* `cli`: A CLI for easily shortening URLs with the Dub API.
* `email`: Dub's email application with function to send emails and templates.
* `embeds`: A package used embed Dub's referral dashboard.
* `prisma`: Prisma Configuration for Dub's web-app.
* `stripe-app`: The Stripe app for dub conversions.
* `tailwind-config`: The Tailwind CSS configuration for Dub's web app.
* `tinybird`: Dub's Tinybird configuration.
* `tsconfig`: The TypeScript configuration for Dub's web app.
* `ui`: Dub's UI component library.
* `utils`: A collection of utility functions and constants used across Dub's codebase.

## How `app.dub.co` works

Dub's web app is built with [Next.js](https://nextjs.org) and [TailwindCSS](https://tailwindcss.com).

It also utilizes code from the `packages` directory, specifically the `@dub/ui` and `@dub/utils` packages.

All of the code for the web app is located in here: [`main`/apps/web/app/app.dub.co](https://github.com/dubinc/dub/tree/main/apps/web/app/app.dub.co). This is using the Next.js [route group pattern](https://nextjs.org/docs/app/building-your-application/routing/route-groups).

There's also the API server, which is located in here: [`main`/apps/web/app/api](https://github.com/dubinc/dub/tree/main/apps/web/app/api)

When you run `pnpm dev` to start the development server, the app will be available at [http://localhost:8888](http://localhost:8888). The reason we use `localhost:8888` and not `app.localhost:8888` is because Google OAuth doesn't allow you to use localhost subdomains.

## How link redirects work on Dub

Link redirects on Dub are powered by [Next.js Middleware](https://nextjs.org/docs/app/building-your-application/routing/middleware).

To handle high traffic, we use Redis to cache every link's metadata when it's first created. This allows us to serve redirects without hitting our MySQL database.

Here's the code that powers link redirects: [`main`/apps/web/lib/middleware/link.ts](https://github.com/dubinc/dub/blob/main/apps/web/lib/middleware/link.ts)

## Running Dub locally

To run Dub locally, you'll need to set up the following:

* A [Tinybird](https://www.tinybird.co/) account
* An [Upstash](https://upstash.com/) account
* A [PlanetScale](https://planetscale.com/)-compatible MySQL database

Watch this video from our friends at Tinybird to learn how to set up Dub locally:

<iframe width="100%" className="aspect-video" src="https://www.youtube.com/embed/9GNYcS9BHhc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />

## Step 1: Local setup

First, you'll need to clone the Dub repo and install the dependencies.

<Steps>
  <Step title="Clone the repo">
    First, clone the [Dub repo](https://d.to/github) into a public GitHub repository.

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

  <Step title="Build internal packages">
    Execute the command below to compile all internal packages:

    ```bash Terminal theme={null}
    pnpm -r --filter "./packages/**" build
    ```
  </Step>

  <Step title="Set up environment variables">
    Copy the `.env.example` file from `./apps/web` to `.env` by executing the following command from `apps/web`:

    ```bash Terminal theme={null}
    cp .env.example .env
    ```

    You'll be updating this `.env` file with your own values as you progress through the setup.
  </Step>
</Steps>

## Step 2: Set up Tinybird Clickhouse database

Next, you'll need to set up the [Tinybird](https://tinybird.co) Clickhouse database. This will be used to store time-series click events data.

<Steps>
  <Step title="Create Tinybird Workspace">
    In your [Tinybird](https://tinybird.co/) account, create a new Workspace. For this guide, we will use the `us-east-1` region.

    Copy your `admin` [Auth Token](https://www.tinybird.co/docs/concepts/auth-tokens.html). Paste this token as the `TINYBIRD_API_KEY` environment variable in your `.env` file.

    <Tip>
      Alternatively, you can set up a [local Tinybird container](https://www.tinybird.co/docs/cli/local-container) for local development.
    </Tip>
  </Step>

  <Step title="Install Tinybird CLI and authenticate">
    In your newly-cloned Dub repo, navigate to the `packages/tinybird` directory.

    If you have `brew`, install `pipx` by running `brew install pipx`. If not, you can check [installation guide](https://pipx.pypa.io/stable/installation/) for other options. After that, install the Tinybird CLI with `pipx install tinybird-cli` (requires Python >= 3.8).

    Run `tb auth --interactive` and paste your `admin` Auth Token.
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

  <Step title="Set up Upstash Redis environment variables">
    Once your database is created, copy the `UPSTASH_REDIS_REST_URL` and `UPSTASH_REDIS_REST_TOKEN` from the **REST API** section into your `.env` file.

    <Frame>    <img src="https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/upstash-redis-tokens.png?fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=18c2630daafe831a527a0986447ec63e" alt="Upstash Redis tokens" data-og-width="704" width="704" data-og-height="285" height="285" data-path="images/upstash-redis-tokens.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/upstash-redis-tokens.png?w=280&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=d7fc2a492b789e9f031a20cadedc7950 280w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/upstash-redis-tokens.png?w=560&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=13abd3ad52519c9e1d9c63c5e4fdf3d8 560w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/upstash-redis-tokens.png?w=840&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=290698786b30e1c7273fcb37e073bf72 840w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/upstash-redis-tokens.png?w=1100&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=47c9499ab1f8f73504a0c923bb65e785 1100w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/upstash-redis-tokens.png?w=1650&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=21a616076690d31f2c9017ea740e6c7c 1650w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/upstash-redis-tokens.png?w=2500&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=665dd5c816a1f2add0f9fa2e74c951ee 2500w" /></Frame>

    Navigate to the [QStash tab](https://console.upstash.com/qstash) and copy the `QSTASH_TOKEN`, `QSTASH_CURRENT_SIGNING_KEY`, and `QSTASH_NEXT_SIGNING_KEY` from the **Request Builder** section into your `.env` file.

    <Frame>    <img src="https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/upstash-qstash-tokens.png?fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=e4d9708c4755d8ccf5d0049261fc4f04" alt="Upstash QStash tokens" data-og-width="692" width="692" data-og-height="264" height="264" data-path="images/upstash-qstash-tokens.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/upstash-qstash-tokens.png?w=280&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=62ce63fea95a613328082fa3b8c44799 280w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/upstash-qstash-tokens.png?w=560&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=776c3859e62443b2899cb8540dd74220 560w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/upstash-qstash-tokens.png?w=840&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=febf1cce0100b465b109abf0512f0a2a 840w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/upstash-qstash-tokens.png?w=1100&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=3f73f9d422ce9151c63fa83161f481c8 1100w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/upstash-qstash-tokens.png?w=1650&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=583a3c2b0032ede7a19a5069e3d735a3 1650w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/upstash-qstash-tokens.png?w=2500&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=b8d81db0d04fe8d157ce08938f80a6ac 2500w" /></Frame>
  </Step>

  <Step title="Optional: Set up Ngrok tunnel">
    If you're planning to run Qstash-powered background jobs locally, you'll need to set up an Ngrok tunnel to expose your local server to the internet.

    Follow [these steps](https://ngrok.com/docs/getting-started/) to setup `ngrok`, and then run the following command to start an Ngrok tunnel at port `8888`:

    ```bash Terminal theme={null}
    ngrok http 8888
    ```

    Copy the `https` URL and paste it as the `NEXT_PUBLIC_NGROK_URL` environment variable in your `.env` file.
  </Step>
</Steps>

## Step 4: Set up PlanetScale MySQL database

Next, you'll need to set up a [PlanetScale](https://planetscale.com/)-compatible MySQL database. This will be used to store user data and link metadata. There are two options:

### Option 1: Local MySQL database with PlanetScale simulator (recommended)

You can use a local MySQL database with a PlanetScale simulator. This is the recommended option for local development since it's 100% free.

Prerequisites:

* [Docker](https://www.docker.com/products/docker-desktop)
* [Docker Compose](https://docs.docker.com/compose/install/)

<Steps>
  <Step title="Spin up the docker-compose stack">
    In the terminal, navigate to the `apps/web` directory and run the following command to start the Docker Compose stack:

    ```bash Terminal theme={null}
    docker compose up
    ```

    This will start two containers: one for the MySQL database and another for the PlanetScale simulator.
  </Step>

  <Step title="Set up database environment variables">
    Ensure the following credentials are added to your `.env` file:

    ```
    DATABASE_URL="mysql://root:@localhost:3306/planetscale"
    PLANETSCALE_DATABASE_URL="http://root:unused@localhost:3900/planetscale"
    ```

    Here, we are using the open-source [PlanetScale simulator](https://github.com/mattrobenolt/ps-http-sim) so the application can continue to use the `@planetscale/database` SDK.

    <Tip>
      While we're using two different values in local development, in production or staging environments, you'll only need the `DATABASE_URL` value.
    </Tip>
  </Step>

  <Step title="Generate Prisma client and create database tables">
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

<Tip>
  The docker-compose setup includes Mailhog, which acts as a mock SMTP server
  and shows received emails in a web UI. You can access the Mailhog web
  interface at [http://localhost:8025](http://localhost:8025). This is useful
  for testing email functionality without sending real emails during local
  development.
</Tip>

### Option 2: PlanetScale hosted database

<Note>
  PlanetScale recently [removed their free
  tier](https://planetscale.com/blog/planetscale-forever), so you'll need to pay
  for this option. A cheaper alternative is to use a [MySQL database on
  Railway](https://railway.app/template/mysql) (\$5/month).
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

## Step 5: Set up Mailhog

To view emails sent from your application during local development, you'll need to set up [Mailhog](https://github.com/mailhog/MailHog).

<Note>
  If you've already run `docker compose up` as part of the database setup, you
  can skip this step. Mailhog is included in the Docker Compose configuration
  and should already be running.
</Note>

<Steps>
  <Step title="Pull Mailhog Docker image">
    Run the following command to pull the Mailhog Docker image:

    ```bash Terminal theme={null}
    docker pull mailhog/mailhog
    ```
  </Step>

  <Step title="Start Mailhog container">
    Start the Mailhog container with the following command:

    ```bash Terminal theme={null}
    docker run -d -p 8025:8025 -p 1025:1025 mailhog/mailhog
    ```

    This will run Mailhog in the background, and the web interface will be available at [http://localhost:8025](http://localhost:8025).
  </Step>
</Steps>

## Step 6: Set NextAuth secret

Generate a secret by visiting [https://generate-secret.vercel.app/32](https://generate-secret.vercel.app/32). Set the value of `NEXTAUTH_SECRET` in `.env` to this value.

## Step 7: Start the development server

Finally, you can start the development server. This will build the packages + start the app servers.

```bash Terminal theme={null}
pnpm dev
```

The web app (`apps/web`) will be available at [localhost:8888](http://localhost:8888). Additionally, you may access Prisma Studio to manage your MySQL database at [localhost:5555](http://localhost:5555).

### Testing your shortlinks locally

Use the following url structure to ensure event tracking is working, and to populate analytics data, replacing `<shortlink-key>` with the shortlink key you've created.

```
http://dub.localhost:8888/<shortlink-key>
```
