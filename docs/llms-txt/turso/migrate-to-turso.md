# Source: https://docs.turso.tech/cloud/migrate-to-turso.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.turso.tech/llms.txt
> Use this file to discover all available pages before exploring further.

# Migrate to Turso

> Learn how to import your existing SQLite database to Turso.

This guide will walk you through the process of migrating your existing SQLite database to Turso Cloud. You can choose between using the Turso CLI, or the Platform API.

<Frame>
    <img src="https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/cloud/import.png?fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=b9672b095d28bc1d3efdc25d337a9a73" alt="Migrate to Turso" data-og-width="2400" width="2400" data-og-height="1350" height="1350" data-path="images/cloud/import.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/cloud/import.png?w=280&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=8702fe3f9759d751a6505f6b46231e9c 280w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/cloud/import.png?w=560&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=3ca3132caf4cd3ac4801ef625d9efe39 560w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/cloud/import.png?w=840&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=dde8a497829d31e67db68821b6f84ca2 840w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/cloud/import.png?w=1100&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=b96b48bea87374fd53ae5d41d72dcff0 1100w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/cloud/import.png?w=1650&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=67de98575c1f5a965da0c01111640e6f 1650w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/cloud/import.png?w=2500&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=db8dad63565c794220b58b68034a1f8e 2500w" />
</Frame>

## Preparing to Migrate

Before importing your SQLite database to Turso, you need to ensure it's compatible with Turso's requirements. Specifically, your SQLite database should be using WAL (Write-Ahead Logging) mode.

<Steps>
  <Step title="Open your SQLite database">
    Use the SQLite command-line tool or any SQLite client to open your database:

    ```bash  theme={null}
    sqlite3 path/to/your/database.db
    ```
  </Step>

  <Step title="Set WAL journal mode">
    Run the following command to switch your database to WAL mode:

    ```sql  theme={null}
    PRAGMA journal_mode='wal';
    ```

    This should return `wal` to confirm the change was successful.
  </Step>

  <Step title="Checkpoint and truncate the WAL file">
    Execute a checkpoint to ensure all changes are written to the main database file and truncate the WAL file:

    ```sql  theme={null}
    PRAGMA wal_checkpoint(truncate);
    ```
  </Step>

  <Step title="Verify the journal mode">
    Confirm that your database is now in WAL mode:

    ```sql  theme={null}
    PRAGMA journal_mode;
    ```

    This should return `wal`.
  </Step>

  <Step title="Close the database">
    Exit the SQLite shell:

    ```sql  theme={null}
    .exit
    ```

    Your database is now ready for migration to Turso.
  </Step>
</Steps>

## Using the CLI

You can create a new database from a local SQLite file using the Turso CLI:

<Steps>
  <Step title="Install the Turso CLI">
    Make sure you have the [Turso CLI installed](/cli/introduction), and you're authenticated.
  </Step>

  <Step title="Import your SQLite Database">
    Import your existing SQLite database file using the `db import` command:

    ```bash  theme={null}
    turso db import ~/path/to/my-database.db
    ```

    <Note>
      Your database will be named after the file (without the .db extension), and
      will import all your tables, data, and schema.
    </Note>
  </Step>

  <Step title="Connect to your database">
    You can now connect to your database using the shell:

    ```bash  theme={null}
    turso db shell <database-name>
    ```
  </Step>
</Steps>

## Using the Platform API

You can also use the Platform API to migrate your existing SQLite database:

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

  <Step title="Create a new Platform API Token">
    Now create a new API Token using the Turso CLI:

    ```bash  theme={null}
    turso auth api-tokens mint quickstart
    ```

    <Info>
      Make sure to save the token somewhere safe. You'll need it to create a database and database token.
    </Info>
  </Step>

  <Step title="Retrieve your account or organization slug">
    The Platform API can be used with your personal account or with an organization. You'll need the obtain the `slug` of your account or organization using using the Turso CLI:

    ```bash  theme={null}
    turso org list
    ```
  </Step>

  <Step title="Create a Database for Import">
    First, create a database that's ready to receive an import:

    ```bash  theme={null}
    curl -X POST "https://api.turso.tech/v1/organizations/{organizationSlug}/databases" \
      -L \
      -H "Authorization: Bearer TOKEN" \
      -H "Content-Type: application/json" \
      -d '{
          "name": "new-database",
          "group": "default",
          "seed": { "type": "database_upload" }
      }'
    ```

    <Note>
      The `seed` parameter with `"type": "database_upload"` indicates that you plan to upload a database file. If you don't proceed to upload a database, this database will count towards your quota, but will not be usable.
    </Note>
  </Step>

  <Step title="Create a Database Token">
    Generate an authentication token for your database:

    ```bash  theme={null}
    curl -X POST "https://api.turso.tech/v1/organizations/{organizationSlug}/databases/{databaseName}/auth/tokens" \
      -L \
      -H "Authorization: Bearer TOKEN"
    ```

    This token will be used to authenticate your upload request, and future requests to the database.
  </Step>

  <Step title="Upload Your SQLite Database">
    Finally, upload your SQLite database file:

    ```bash  theme={null}
    curl -X POST "https://{databaseName}-{organizationSlug}.turso.io/v1/upload" \
      -H "Authorization: Bearer DATABASE_TOKEN" \
      --data-binary @/path/to/your/database.db
    ```

    <Note>
      The `Authorization` header uses the database token you generated in the
      previous step, not your Platform API token.
    </Note>
  </Step>
</Steps>

You're now ready to connect to your new Turso database using any of the Turso client libraries.

<Snippet file="all-sdks.mdx" />
