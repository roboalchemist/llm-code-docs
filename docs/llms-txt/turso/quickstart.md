# Source: https://docs.turso.tech/tursodb/quickstart.md

# Source: https://docs.turso.tech/sdk/ts/quickstart.md

# Source: https://docs.turso.tech/sdk/swift/quickstart.md

# Source: https://docs.turso.tech/sdk/rust/quickstart.md

# Source: https://docs.turso.tech/sdk/ruby/quickstart.md

# Source: https://docs.turso.tech/sdk/python/quickstart.md

# Source: https://docs.turso.tech/sdk/php/quickstart.md

# Source: https://docs.turso.tech/sdk/kotlin/quickstart.md

# Source: https://docs.turso.tech/sdk/http/quickstart.md

# Source: https://docs.turso.tech/sdk/go/quickstart.md

# Source: https://docs.turso.tech/sdk/flutter/quickstart.md

# Source: https://docs.turso.tech/sdk/c/quickstart.md

# Source: https://docs.turso.tech/sdk/activerecord/quickstart.md

# Source: https://docs.turso.tech/quickstart.md

# Source: https://docs.turso.tech/api-reference/quickstart.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.turso.tech/llms.txt
> Use this file to discover all available pages before exploring further.

# Quickstart

> Get started with Turso API in a few easy steps.

<Steps>
  <Step title="Signup or Login using the Turso CLI">
    Make sure to [install the Turso CLI](/cli/installation) if you haven't
    already.

    <CodeGroup>
      ```bash Signup theme={null}
      turso auth signup
      ```

      ```bash Login theme={null}
      turso auth login
      ```
    </CodeGroup>
  </Step>

  <Step title="Retrieve your account or organization slug">
    The Platform API can be used with your personal account or with an organization. You'll need the obtain the `slug` of your account or organization using using the Turso CLI:

    ```bash  theme={null}
    turso org list
    ```
  </Step>

  <Step title="Create a new Platform API Token">
    Now create a new API Token using the Turso CLI:

    ```bash  theme={null}
    turso auth api-tokens mint quickstart
    ```

    <Info>
      Make sure to save the token somewhere safe. We'll need it next.
    </Info>
  </Step>

  <Step title="Fetch available Locations">
    Before we can create a group or database in a specific region, we'll need to fetch the list of available regions:

    <CodeGroup>
      ```bash cURL theme={null}
      curl -L 'https://api.turso.tech/v1/locations' \
        -H 'Authorization: Bearer TOKEN' \
      ```

      ```ts Node.js theme={null}
      import { createClient } from "@tursodatabase/api";

      const turso = createClient({
        org: "...",
        token: "",
      });

      const locations = await turso.locations.list();
      ```
    </CodeGroup>

    <br />

    <Info>
      The `organizationSlug` is the name of your organization or personal account.
    </Info>
  </Step>

  <Step title="Create a Group">
    All databases belong to a group that can exist in one or more locations.

    Begin by creating a group, giving it a `name` and primary `location`:

    <CodeGroup>
      ```bash cURL theme={null}
      curl -L -X POST 'https://api.turso.tech/v1/organizations/{organizationSlug}/groups' \
        -H 'Authorization: Bearer TOKEN' \
        -H 'Content-Type: application/json' \
        -d '{
            "name": "default",
            "location": "lhr"
        }'
      ```

      ```ts Node.js theme={null}
      import { createClient } from "@tursodatabase/api";

      const turso = createClient({
        org: "...",
        token: "",
      });

      const group = await turso.groups.addLocation("default", "lhr");
      ```
    </CodeGroup>
  </Step>

  <Step title="Create a Database">
    Now create your first database in the group you created above:

    <CodeGroup>
      ```bash cURL theme={null}
      curl -L -X POST 'https://api.turso.tech/v1/organizations/{organizationSlug}/databases' \
        -H 'Authorization: Bearer TOKEN' \
        -H 'Content-Type: application/json' \
        -d '{
            "name": "my-db",
            "group": "default"
        }'
      ```

      ```ts Node.js theme={null}
      import { createClient } from "@tursodatabase/api";

      const turso = createClient({
        org: "...",
        token: "",
      });

      const database = await turso.databases.create("my-db", "ams");
      ```
    </CodeGroup>
  </Step>

  <Step title="Connect to your database">
    You now have a database, distributed across multiple regions that you can connect to using one of the official or experimental SDKs:

    <Snippet file="all-sdks.mdx" />
  </Step>
</Steps>
