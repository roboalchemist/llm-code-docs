# Source: https://docs.turso.tech/sdk/ts/guides/qwik.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.turso.tech/llms.txt
> Use this file to discover all available pages before exploring further.

# Qwik + Turso

> Set up Turso in your Qwik project in minutes

<img src="https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/qwik-banner.png?fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=bd50c1555e2915546f901981ac6efba5" alt="Qwik banner" data-og-width="1133" width="1133" data-og-height="595" height="595" data-path="images/guides/qwik-banner.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/qwik-banner.png?w=280&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=1569ff1e72474e2bb1b3a44998bdbb45 280w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/qwik-banner.png?w=560&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=ccc4ef9d6b254e2ed512c3962c77d107 560w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/qwik-banner.png?w=840&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=35c89107df28159b166ba85465d52061 840w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/qwik-banner.png?w=1100&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=647c06e863baef5583cfad139fd6c138 1100w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/qwik-banner.png?w=1650&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=e28f620d00518a4518569ecb212a6f15 1650w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/qwik-banner.png?w=2500&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=ae524559d6b1f2d7a289251da8d78ab7 2500w" />

## Prerequisites

Before you start, make sure you:

* [Install the Turso CLI](/cli/installation)
* [Sign up or login to Turso](/cli/authentication#signup)
* Have a Qwik app — [learn more](https://qwik.builder.io/docs/getting-started/#create-an-app-using-the-cli)

<Steps>
  <Step title="Add Turso Integration">
    <CodeGroup>
      ```bash npm theme={null}
      npm run qwik add turso
      ```

      ```bash pnpm theme={null}
      pnpm qwik add turso
      ```

      ```bash yarn theme={null}
      yarn qwik add turso
      ```
    </CodeGroup>
  </Step>

  <Step title="Configure database credentials">
    Get the database URL:

    ```bash  theme={null}
    turso db show --url <database-name>
    ```

    Get the database authentication token:

    ```bash  theme={null}
    turso db tokens create <database-name>
    ```

    Assign credentials to the environment variables inside `.env.local`.

    ```bash  theme={null}
    PRIVATE_TURSO_DATABASE_URL="..."
    PRIVATE_TURSO_AUTH_TOKEN="..."
    ```
  </Step>

  <Step title="Execute SQL">
    ```ts  theme={null}
    import { tursoClient } from "~/utils/turso";

    export const useFrameworks = routeLoader$(
      async (requestEvent: RequestEventBase) => {
        const db = tursoClient(requestEvent["env"]);
        const { rows } = await db.execute("select * from table_name");

        return {
          items: rows,
        };
      },
    );
    ```
  </Step>
</Steps>

## Examples

<CardGroup cols={2}>
  <Card title="Social Website" icon="github" href="https://github.com/tursodatabase/examples/tree/master/app-find-me-on">
    See the full source code
  </Card>

  <Card title="Shopping Cart" icon="github" href="https://github.com/tursodatabase/examples/tree/master/app-turqw-store">
    See the full source code
  </Card>
</CardGroup>
