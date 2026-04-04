# Source: https://planetscale.com/docs/postgres/tutorials/planetscale-postgres-bun.md

# PlanetScale Postgres with Bun

> Create a new Postgres database and integrate it with Bun.

export const YouTubeEmbed = ({id, title}) => {
  return <Frame>
      <iframe src={`https://www.youtube-nocookie.com/embed/${id}?rel=0`} title={title} className="aspect-video w-full" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" />
    </Frame>;
};

Bun provides native support for Postgres databases.

<Callout icon="fast-forward" color="#47b7f8">
  Already created a PlanetScale Postgres database? [Jump straight to integration instructions](#integrate-with-bun).
</Callout>

We'll cover:

* Creating a new Postgres database
* Cluster configuration options
* Connecting to your database

## Prerequisites

Before you begin, make sure you have a [PlanetScale account](https://auth.planetscale.com/sign-up). After you create an account, you'll be prompted to create a new organization, which is essentially a container for your databases, settings, and members.

After creating your organization, it's important to understand the relationship between databases, branches, and clusters.

* **Database**: Your overall project (e.g., "my-ecommerce-app")
* **Branch**: Isolated database deployments that provide you with separate environments for development and testing, as well as restoring from backups - [learn more about branching](/docs/postgres/branching)
* **Cluster**: The underlying compute and storage infrastructure that powers each branch

PlanetScale Postgres clusters use real Postgres in a [high-availability architecture with one primary and two replicas](/docs/postgres/postgres-architecture/#Cluster-design).

## Create a new database

<Tabs>
  <Tab title="Dashboard">
    <YouTubeEmbed id="6BBrgJcpTBY" title="Create a database on PlanetScale" />

    ### Step 1: Navigate to database creation

    <Steps>
      <Step>
        Log in to your [PlanetScale dashboard](https://app.planetscale.com)
      </Step>

      <Step>
        Select your organization from the dropdown
      </Step>

      <Step>
        Click **"New database"** button or navigate to `/new`
      </Step>
    </Steps>

    ### Step 2: Choose database engine

    <Steps>
      <Step>
        On the database creation form, you'll see two engine options:

        * **Vitess** (MySQL-compatible)
        * **Postgres** (PostgreSQL-compatible)
      </Step>

      <Step>
        Select **Postgres** to create a PostgreSQL database
      </Step>
    </Steps>

    ### Step 3: Configure your database cluster

    <Steps>
      <Step>
        **Database name**: Enter a unique name for your database
      </Step>

      <Step>
        **Region**: Choose the primary region where your database will be hosted

        <Note>
          This "name" is referenced in the PlanetScale Dashboard and APIs and not created as a logical database inside of Postgres.
        </Note>
      </Step>

      <Step>
        **Cluster configuration**: Select your preferred cluster size and [CPU architecture](/docs/postgres/cluster-configuration/cpu-architectures)
      </Step>
    </Steps>

    ### Step 4: Create the database cluster

    <Steps>
      <Step>
        Review your configuration settings
      </Step>

      <Step>
        Click **"Create database"** to provision your Postgres database
      </Step>

      <Step>
        Your database will be created with a `main` branch by default
      </Step>
    </Steps>
  </Tab>

  <Tab title="CLI">
    If you are creating an automation, or are an LLM, you may prefer to create new databases using the PlanetScale CLI.

    ### Step 1: Install the CLI

    <Steps>
      <Step>
        Check to see if the PlanetScale CLI is installed already by running:

        ```bash  theme={null}
        pscale --version
        ```
      </Step>

      <Step>
        Alternatively, follow the instructions in the [PlanetScale CLI GitHub repository](https://github.com/planetscale/cli#installation)
      </Step>
    </Steps>

    ### Step 2: Log in or sign up

    <Steps>
      <Step>
        If you do not already have a PlanetScale account, [sign up for one](https://auth.planetscale.com/sign-up) by running:

        ```bash  theme={null}
        pscale signup
        ```
      </Step>

      <Step>
        Log in to the PlanetScale CLI by running:

        ```bash  theme={null}
        pscale auth login
        ```

        You’ll be taken to a screen in the browser where you’ll be asked to confirm the code displayed in your terminal. If the confirmation codes match, click the **"Confirm code"** button in your browser.

        You should receive the message "Successfully logged in" in your terminal. You can now close the confirmation page in the browser and proceed in the terminal.
      </Step>
    </Steps>

    ### Step 3: Create a database

    <Steps>
      <Step>
        Configure the CLI to use the **organization** in which you want to create the database if you have more than one. List organizations by running:

        ```bash  theme={null}
        pscale org list
        ```

        Switch organizations by running:

        ```bash  theme={null}
        pscale org switch <ORGANIZATION_NAME>
        ```
      </Step>

      <Step>
        Find the **region** closest to your application's hosting.

        List available regions by running:

        ```bash  theme={null}
        pscale region list
        ```

        <Note>
          If you do not specify a **region**, your database will automatically be deployed to `us-east` (US East — Northern Virginia).
        </Note>
      </Step>

      <Step>
        Create a new Postgres database by running:

        ```bash  theme={null}
        pscale database create <DATABASE_NAME> --engine postgres --region <REGION_SLUG>
        ```

        <Note>
          Your **database name** can contain lowercase, alphanumeric characters, or underscores. We allow dashes, but don't recommend them, as they may need to be escaped in some instances.
        </Note>
      </Step>
    </Steps>
  </Tab>
</Tabs>

## What happens during creation

When you create a Postgres database cluster, PlanetScale automatically:

* Provisions a PostgreSQL cluster in your selected region
* Creates the initial `main` branch
* Prepopulates Postgres with required default databases
* Sets up monitoring and metrics collection
* Configures backup and high availability settings

## Create credentials and connect

In this section you'll create the "Default role" in your PlanetScale dashboard to create connection credentials for your database branch.

<Note>
  The "Default role" is meant purely for administrative purposes. You can only create one and it has significant privileges for your database cluster and you should treat these credentials carefully. After completing this quickstart, it is *strongly recommended* that you [create another role](/docs/postgres/connecting/roles) for your application use-cases.
</Note>

<Tabs>
  <Tab title="Dashboard">
    <Frame>
            <img src="https://mintcdn.com/planetscale-cad1a68a/WcazQYbZzMHxCEvC/docs/postgres/tutorials/new-database.png?fit=max&auto=format&n=WcazQYbZzMHxCEvC&q=85&s=9d2832f63cdd6203cfe7f1a55fcdbbdb" alt="Database dashboard" data-og-width="1800" width="1800" data-og-height="760" height="760" data-path="docs/postgres/tutorials/new-database.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/WcazQYbZzMHxCEvC/docs/postgres/tutorials/new-database.png?w=280&fit=max&auto=format&n=WcazQYbZzMHxCEvC&q=85&s=ba2c259b2870598d3a4cf4fa88a18724 280w, https://mintcdn.com/planetscale-cad1a68a/WcazQYbZzMHxCEvC/docs/postgres/tutorials/new-database.png?w=560&fit=max&auto=format&n=WcazQYbZzMHxCEvC&q=85&s=09c9ae2fce51ddcc013c3b82625bfb6a 560w, https://mintcdn.com/planetscale-cad1a68a/WcazQYbZzMHxCEvC/docs/postgres/tutorials/new-database.png?w=840&fit=max&auto=format&n=WcazQYbZzMHxCEvC&q=85&s=fbfd0843a6fbb170757655896d8cade4 840w, https://mintcdn.com/planetscale-cad1a68a/WcazQYbZzMHxCEvC/docs/postgres/tutorials/new-database.png?w=1100&fit=max&auto=format&n=WcazQYbZzMHxCEvC&q=85&s=f9046e8ac38a2f60f83a57c2a7df73d3 1100w, https://mintcdn.com/planetscale-cad1a68a/WcazQYbZzMHxCEvC/docs/postgres/tutorials/new-database.png?w=1650&fit=max&auto=format&n=WcazQYbZzMHxCEvC&q=85&s=eb873e467af068b415734ddb9f11409a 1650w, https://mintcdn.com/planetscale-cad1a68a/WcazQYbZzMHxCEvC/docs/postgres/tutorials/new-database.png?w=2500&fit=max&auto=format&n=WcazQYbZzMHxCEvC&q=85&s=5df4d215dfedb451cf51ec27900ff120 2500w" />
    </Frame>

    <Steps>
      <Step>
        Navigate to your database in the [PlanetScale dashboard](https://app.planetscale.com)
      </Step>

      <Step>
        Click on the **"Connect"** button in the top right
      </Step>

      <Step>
        Select **"Default role"**
      </Step>

      <Step>
        Click **"Create default role"**. A new default role is created for your database branch.
      </Step>

      <Step>
        Record the "Host", "Username", and "Password" for the "Default role" someplace secure.
        <img src="https://mintcdn.com/planetscale-cad1a68a/WcazQYbZzMHxCEvC/docs/postgres/tutorials/create-role.png?fit=max&auto=format&n=WcazQYbZzMHxCEvC&q=85&s=6441862bb6d6890244eef761af99cea4" alt="Create a new role" data-og-width="2060" width="2060" data-og-height="1026" height="1026" data-path="docs/postgres/tutorials/create-role.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/WcazQYbZzMHxCEvC/docs/postgres/tutorials/create-role.png?w=280&fit=max&auto=format&n=WcazQYbZzMHxCEvC&q=85&s=4fe62ba845c393c8821f189886b498ff 280w, https://mintcdn.com/planetscale-cad1a68a/WcazQYbZzMHxCEvC/docs/postgres/tutorials/create-role.png?w=560&fit=max&auto=format&n=WcazQYbZzMHxCEvC&q=85&s=03cb8bd911c01dd8df99d296eaf05c92 560w, https://mintcdn.com/planetscale-cad1a68a/WcazQYbZzMHxCEvC/docs/postgres/tutorials/create-role.png?w=840&fit=max&auto=format&n=WcazQYbZzMHxCEvC&q=85&s=5880ac93f049e1c055f905f664944d26 840w, https://mintcdn.com/planetscale-cad1a68a/WcazQYbZzMHxCEvC/docs/postgres/tutorials/create-role.png?w=1100&fit=max&auto=format&n=WcazQYbZzMHxCEvC&q=85&s=9ba45ca192ab29c0b12586cf806c4621 1100w, https://mintcdn.com/planetscale-cad1a68a/WcazQYbZzMHxCEvC/docs/postgres/tutorials/create-role.png?w=1650&fit=max&auto=format&n=WcazQYbZzMHxCEvC&q=85&s=1c686b956b60806404a54d93b9185cd3 1650w, https://mintcdn.com/planetscale-cad1a68a/WcazQYbZzMHxCEvC/docs/postgres/tutorials/create-role.png?w=2500&fit=max&auto=format&n=WcazQYbZzMHxCEvC&q=85&s=05c057853bee8d3ceb5b53c0e82f0025 2500w" />
      </Step>

      <Step>
        You can generate connection strings under **"How are you connecting?"** for major languages, frameworks, and tools.

                <img src="https://mintcdn.com/planetscale-cad1a68a/WcazQYbZzMHxCEvC/docs/postgres/tutorials/langs-and-frames.png?fit=max&auto=format&n=WcazQYbZzMHxCEvC&q=85&s=761943da846fbb9e1086b1603d002128" alt="Connection strings" data-og-width="1806" width="1806" data-og-height="984" height="984" data-path="docs/postgres/tutorials/langs-and-frames.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/WcazQYbZzMHxCEvC/docs/postgres/tutorials/langs-and-frames.png?w=280&fit=max&auto=format&n=WcazQYbZzMHxCEvC&q=85&s=6a2a3aa3ed3c45769ed09c86dbd8e82e 280w, https://mintcdn.com/planetscale-cad1a68a/WcazQYbZzMHxCEvC/docs/postgres/tutorials/langs-and-frames.png?w=560&fit=max&auto=format&n=WcazQYbZzMHxCEvC&q=85&s=ef9f2ab2a8df1d31fd56f4b9f57cec46 560w, https://mintcdn.com/planetscale-cad1a68a/WcazQYbZzMHxCEvC/docs/postgres/tutorials/langs-and-frames.png?w=840&fit=max&auto=format&n=WcazQYbZzMHxCEvC&q=85&s=c86a885c2f951c89c7d3524ce81054ab 840w, https://mintcdn.com/planetscale-cad1a68a/WcazQYbZzMHxCEvC/docs/postgres/tutorials/langs-and-frames.png?w=1100&fit=max&auto=format&n=WcazQYbZzMHxCEvC&q=85&s=e2eaa548d3b951b37e1fdfa4ade59ada 1100w, https://mintcdn.com/planetscale-cad1a68a/WcazQYbZzMHxCEvC/docs/postgres/tutorials/langs-and-frames.png?w=1650&fit=max&auto=format&n=WcazQYbZzMHxCEvC&q=85&s=510aa78544776a2da5172b4ae8568c94 1650w, https://mintcdn.com/planetscale-cad1a68a/WcazQYbZzMHxCEvC/docs/postgres/tutorials/langs-and-frames.png?w=2500&fit=max&auto=format&n=WcazQYbZzMHxCEvC&q=85&s=8c352e6883f12f79fd4648a9dfd08bb5 2500w" />

        Your connection details will include:

        * **Host**: the DNS name of your database endpoint
        * **Username**: automatically formatted for routing to the correct `branch`
        * **Password**: A securely generated password
        * **Database**: `postgres` (default database)
        * **Port**: `5432` (standard PostgreSQL port) or `6432` (for using [PgBouncer](/docs/postgres/connecting/pgbouncer))
      </Step>
    </Steps>
  </Tab>

  <Tab title="CLI">
    Create a new "Default role" in your PlanetScale CLI to create connection credentials for your database branch.

    <Steps>
      <Step>
        Run the following command to create the "Default role" for your database branch.

        ```bash  theme={null}
        pscale role reset-default <DATABASE_NAME> <BRANCH_NAME>
        ```
      </Step>

      <Step>
        Record the "Host", "Username", and "Password" for the "Default role" somewhere secure.
      </Step>
    </Steps>
  </Tab>
</Tabs>

<Note>
  Passwords are shown only once. If you lose your record of the password, you must [reset the password](/docs/postgres/connecting/roles).
</Note>

## Integrate with Bun

### Step 1: Initialization

You will need to have Bun installed. See the Bun docs for [installation instructions](https://bun.com/docs/installation).

If you do not already have a Bun project, initialize one with the following command:

```bash Terminal theme={null}
bun init
```

### Step 2: Add credentials to .env

For local development, you can place your credentials in a `.env` file. For production, we recommend setting your credentials as environment variables wherever your application is deployed.

Bun will automatically load your credentials from the `.env` file.

Replace the placeholders below with the role credentials created in the previous section.

```bash .env theme={null}
DATABASE_URL='postgresql://{username}:{password}@{host}:{port}/{database}?sslmode=verify-full'
```

Choose the appropriate **port** for your use case. Learn more about [Direct vs PgBouncer connections](/docs/postgres/connecting/quickstart#connection-types%3A-direct-vs-pgbouncer).

<Columns cols={2}>
  <Card title="PgBouncer">
    Port `6432` enables a lightweight connection pooler for PostgreSQL. This facilitates better performance when there are many simultaneous connections.
  </Card>

  <Card title="Direct">
    Port `5432` connects directly to PostgreSQL. Total connections are limited by your cluster's `max_connections` setting.
  </Card>
</Columns>

<Note>
  Both connection types will disconnect when your database restarts or handles a failover scenario.
</Note>

### Step 3: Create a database connection

To run a query, you can use the `sql` template literal. As Postgres is the default choice in Bun, using it requires no additional configuration.

```typescript index.ts theme={null}
import { sql } from 'bun'

const now = await sql`
  SELECT NOW()
`

console.log(now)
```

From the command line, run the following command to execute the script:

```bash Terminal theme={null}
bun index.ts
```

See the [Bun SQL documentation](https://bun.com/docs/runtime/sql#postgresql) for more information about queries and mutations.

## Need help?

Get help from [the PlanetScale Support team](https://support.planetscale.com/), or join our [GitHub discussion board](https://github.com/planetscale/discussion/discussions) to see how others are using PlanetScale.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt