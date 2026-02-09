# Source: https://docs.turso.tech/features/embedded-replicas/with-koyeb.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.turso.tech/llms.txt
> Use this file to discover all available pages before exploring further.

# Turso + Koyeb

> Deploy a JavaScript/Rust app using [Turso embedded replicas](/features/embedded-replicas) to [Koyeb](https://www.koyeb.com/).

<img src="https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/platforms/koyeb-banner.png?fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=6f7f0ee22ae417bb3743cd771b4c8a4a" alt="Koyeb banner" data-og-width="1133" width="1133" data-og-height="595" height="595" data-path="images/platforms/koyeb-banner.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/platforms/koyeb-banner.png?w=280&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=3a37d05b05434ec42c03cef40844b2ad 280w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/platforms/koyeb-banner.png?w=560&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=a926c63a243466bfec358e32cbb6b8dc 560w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/platforms/koyeb-banner.png?w=840&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=c32425916c62d0679901af3822b89473 840w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/platforms/koyeb-banner.png?w=1100&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=2f9fe06a552430f6ea5a98eafa9ba733 1100w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/platforms/koyeb-banner.png?w=1650&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=acc4224be02b1b558a835f0713613d50 1650w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/platforms/koyeb-banner.png?w=2500&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=7621a49790d9c814524bada502407df9 2500w" />

## Prerequisites

Before you start, make sure you:

* [Install the Turso CLI](/cli/installation)
* [Sign up or login to Turso](/cli/authentication#signup)
* Have a Koyeb account - [create one](https://app.koyeb.com/)

<Steps>
  <Step title="Retrieve database credentials">
    You will need an existing database to continue. If you don't have one, [create one](/quickstart).

    <Snippet file="retrieve-database-credentials.mdx" />

    <Info>You will want to store these as environment variables.</Info>
  </Step>

  <Step>
    Fork one of the following embedded replica project from GitHub

    <CardGroup cols={2}>
      <Card title="My Expenses Tracker - (Elysia + Bun)" icon="github" href="https://github.com/tursodatabase/embedded-replicas-with-js">
        See the full source code
      </Card>

      <Card title="Web Traffic API - (Rust)" icon="github" href="https://github.com/tursodatabase/embedded-replicas-with-rust">
        See the full source code
      </Card>
    </CardGroup>

    <Note>
      Or, you can:

      <Card title="Deploy to Koyeb with a single-click" href="https://app.koyeb.com/deploy?name=er-with-js&type=git&repository=tursodatabase/embedded-replicas-with-js&branch=main&env[PORT]=8000&env[TURSO_DATABASE_URL]=REPLACE_ME&env[TURSO_AUTH_TOKEN]=REPLACE_ME&env[LOCAL_DB]=file:expenses.db" />
    </Note>
  </Step>

  <Step title="Add a new Koyeb app">
    1. Create a new app in the Koyeb control panel.

    2. Select GitHub as the deployment option.

    3. Import the GitHub project to Koyeb.
  </Step>

  <Step title="Fill in the environment variables on Koyeb's deploy page">
        <img src="https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/platforms/koyeb-env-variables.png?fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=fbe69407ce481b6f89954813101965b4" alt="Koyeb deploy page - environment variables" data-og-width="1298" width="1298" data-og-height="501" height="501" data-path="images/platforms/koyeb-env-variables.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/platforms/koyeb-env-variables.png?w=280&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=6cff6cc0a7847edabe15e14bc6419399 280w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/platforms/koyeb-env-variables.png?w=560&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=7b151860e44183bcbe2cd03d9a40b740 560w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/platforms/koyeb-env-variables.png?w=840&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=d7b37c14230f5247b8b91eb4c39deba1 840w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/platforms/koyeb-env-variables.png?w=1100&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=b2f314dbd701465a55772d5f88feb50e 1100w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/platforms/koyeb-env-variables.png?w=1650&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=d47c9aa00dfcbb0ae7b0a84e5551ccdf 1650w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/platforms/koyeb-env-variables.png?w=2500&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=0fb52561c549f7fba3b316a0db9daf0f 2500w" />
  </Step>

  <Step title="Deploy">
    Click the **Deploy** button at the bottom to deploy your web service.
  </Step>
</Steps>
