# Source: https://docs.turso.tech/features/embedded-replicas/with-fly.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.turso.tech/llms.txt
> Use this file to discover all available pages before exploring further.

# Embedded Replicas on Fly

> Deploy a JavaScript app using [Turso embedded replicas](/features/embedded-replicas) to [Fly.io](https://www.fly.io/).

<img src="https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/platforms/fly-banner.png?fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=f3d7f266e79052e9d176d519a4a277fc" alt="Koyeb banner" data-og-width="1133" width="1133" data-og-height="595" height="595" data-path="images/platforms/fly-banner.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/platforms/fly-banner.png?w=280&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=4f2b9cc3a0a6b192a4d1cb492bb944dc 280w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/platforms/fly-banner.png?w=560&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=437795d31a96fb3c16d0729287a676e5 560w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/platforms/fly-banner.png?w=840&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=15228f989a0e419c8829fc70c5e75700 840w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/platforms/fly-banner.png?w=1100&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=11bbca9fcfeadb59b105fc30eb4996da 1100w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/platforms/fly-banner.png?w=1650&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=0b3ad55854bc704cc5fb3f8d8f00e7c1 1650w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/platforms/fly-banner.png?w=2500&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=d4cd31c518def5ec3454466dbfec6a53 2500w" />

## Prerequisites

Before you start, make sure you:

* [Install the Turso CLI](/cli/installation)
* [Sign up or login to Turso](/cli/authentication#signup)
* [Install the Fly.io CLI](https://fly.io/docs/hands-on/install-flyctl/)

<Steps>
  <Step title="Locate your application">
    You should have an application ready using your Turso database that you want to deploy to Fly.
  </Step>

  <Step title="Launch with Fly">
    Using the Fly CLI, launch it:

    ```bash  theme={null}
    fly launch
    ```

    Your application will automatically deploy to Fly, but we're not ready yet.
  </Step>

  <Step title="Create a shared volume">
    Now create a volume that will be used to store the embedded replica(s):

    ```bash  theme={null}
    fly volumes create libsql_data
    ```
  </Step>

  <Step title="Mount and configure volumes">
    The files `fly.toml` and `Dockerfile` created created when you launched previously.

    Update `fly.toml` this file to mount the new volume:

    ```toml  theme={null}
    [[mounts]]
    source = "libsql_data"
    destination = "/app/data"
    ```

    Then inside `Dockerfile`, make sure you install and update `ca-certificates`:

    ```dockerfile  theme={null}
    RUN apt-get update -qq && \
        apt-get install -y ca-certificates && \
        update-ca-certificates
    ```

    Make sure to also add the following line after any `COPY` commands to copy the certificates:

    ```dockerfile  theme={null}
    COPY --from=build /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/
    ```
  </Step>

  <Step title="Configure the libSQL client">
    You will want to change the `url` to point to a local file, and set the `syncUrl` to be your Turso database URL:

    ```ts  theme={null}
    import { createClient } from "@libsql/client";

    const client = createClient({
      url: "file:/app/data/local.db",
      syncUrl: process.env.TURSO_DATABASE_URL,
      authToken: process.env.TURSO_AUTH_TOKEN,
      syncInterval: 60,
    });
    ```
  </Step>

  <Step title="Deploy your updated app">
    ```bash  theme={null}
    fly deploy
    ```
  </Step>
</Steps>
