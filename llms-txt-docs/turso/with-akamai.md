# Source: https://docs.turso.tech/features/embedded-replicas/with-akamai.md

# Turso + Linode by Akamai

> Deploy a JavaScript/Rust app using [Turso embedded replicas](/features/embedded-replicas) to [Akamai](https://www.linode.com/).

<img src="https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/platforms/akamai-banner.png?fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=66d07bd3d96ab8ddcec273d80a00fdca" alt="Akamai banner" data-og-width="1133" width="1133" data-og-height="595" height="595" data-path="images/platforms/akamai-banner.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/platforms/akamai-banner.png?w=280&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=7e4da37bf6a452264bff0be6725749a8 280w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/platforms/akamai-banner.png?w=560&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=a582bfcffff91ca1d7b40c1565c0870d 560w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/platforms/akamai-banner.png?w=840&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=6e9cb8c3f56ac4d26b7dfbe2902cd12e 840w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/platforms/akamai-banner.png?w=1100&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=0380395041ac579b29e8ca192fcb42f2 1100w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/platforms/akamai-banner.png?w=1650&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=f58c99fc7d4c58b6d14f9852b7d4d49c 1650w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/platforms/akamai-banner.png?w=2500&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=8addc1be9c1c579e1d0cbe4f0334fd2a 2500w" />

## Prerequisites

Before you start, make sure you:

* [Install the Turso CLI](/cli/installation)
* [Sign up or login to Turso](/cli/authentication#signup)
* Have an Akamai account - [create one](https://login.linode.com/signup)

<Steps>
  <Step title="Retrieve database credentials">
    You will need an existing database to continue. If you don't have one, [create one](/quickstart).

    <Snippet file="retrieve-database-credentials.mdx" />

    <Info>You will want to store these as environment variables.</Info>
  </Step>

  <Step>
    Fork one of the following embedded replica projects from GitHub

    <CardGroup cols={2}>
      <Card title="My Expenses Tracker - (Elysia + Bun)" icon="github" href="https://github.com/tursodatabase/embedded-replicas-with-js">
        See the full source code
      </Card>

      <Card title="Web Traffic API - (Rust)" icon="github" href="https://github.com/tursodatabase/embedded-replicas-with-rust">
        See the full source code
      </Card>
    </CardGroup>
  </Step>

  <Step title="Set up a Linode server">
    Configure and create a new linode. Then, [set up SSH authentication](https://www.linode.com/docs/guides/use-public-key-authentication-with-ssh/) to securely access the Linode server from your terminal.

    Prepare the newly created linode server environment by accessing and set it up for Rust/JavaScript development depending on the project you forked earlier. Install and set up [Git](https://git-scm.com/) too.
  </Step>

  <Step title="Transfer project to Linode server">
    SSH into your server, clone the project from GitHub, and follow its README instructions to set it up.
  </Step>

  <Step title="Deploy">
    Build, run the project, and set up load balancing for it.
    [pm2](https://www.npmjs.com/package/pm2) is one of the good candidates out there with built-in load balancing, log monitoring, and bug/exception alerts.

    <Info>
      You can go with your favorite options for where to buy domains, reverse proxy setup, and SSL certificates. [Caddy](https://caddyserver.com/) is another good option here.
    </Info>
  </Step>
</Steps>
