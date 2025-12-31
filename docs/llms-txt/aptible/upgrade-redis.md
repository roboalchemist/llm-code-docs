# Source: https://www.aptible.com/docs/how-to-guides/database-guides/upgrade-redis.md

# Upgrade Redis

This guide covers how to upgrade a Redis [Database](/core-concepts/managed-databases/managing-databases/overview) to a newer release.

<Tip>
  Starting with Redis 6, the Access Control List feature was introduced by Redis. In specific scenarios, this change also changes how a Redis Database can be upgraded. To help describe when each upgrade method applies, we'll use the term `pre-ACL` to describe Redis version 5 and below, and `post-ACL` to describe Redis version 6 and beyond.
</Tip>

<Accordion title="Pre-ACL to Pre-ACL and Post-ACL to Post-ACL Upgrades">
  <Note>
    **Prerequisite:** Install the [Aptible CLI](/reference/aptible-cli/cli-commands/overview)
  </Note>

  <Steps>
    <Step title="Collection Configuration Information">
      Collect information on the Database you'd like to upgrade and store it in the following environment variables for use later in the guide:

      * `DB_HANDLE` - The handle (i.e. name) of the Database.
      * `ENVIRONMENT` - The handle of the environment the Database belongs to.
      * `VERSION` - The desired Redis version. Run `aptible db:versions` to see a full list of options.

      ```bash  theme={null}
        DB_HANDLE='my-redis'
        ENVIRONMENT='test-environment'
        VERSION='5.0-aof'
      ```
    </Step>

    <Step title="Contact the Aptible Support Team">
      An Aptible team member must update the Database's metadata to the new version in order to upgrade the Database. When contacting [Aptible Support](/how-to-guides/troubleshooting/aptible-support) please adhere to the following rules to ensure a smooth upgrade process:

      * Ensure that you have [Administrator Access](/core-concepts/security-compliance/access-permissions#write-permissions) to the Database's Environment. If you do not, please have someone with access contact support or CC an [Account Owner or Deploy Owner](/core-concepts/security-compliance/access-permissions) for approval.
      * Use the same email address that's associated with your Aptible user account to contact support.
      * Include the configuration values above. You may run the following command to generate a request with the required information:

      ```bash  theme={null}
        echo "Please upgrade our Redis database, ${ENVIRONMENT} - ${DB_HANDLE}, to version ${VERSION}. Thank you."
      ```
    </Step>

    <Step title="Restart the Database">
      Once support has updated the Database version, you'll need to restart the database to apply the upgrade. You may do so at your convenience with the [`aptible db:reload`](/reference/aptible-cli/cli-commands/cli-db-reload) CLI command:

      ```bash  theme={null}
        aptible db:reload --environment $ENVIRONMENT $DB_HANDLE
      ```
    </Step>
  </Steps>
</Accordion>

<Accordion title="Pre-ACL to Post-ACL Upgrades">
  <Accordion title="Method 1: Use Replication to Orchestrate a Minimal-Downtime Upgrade">
    <Note>
      **Prerequisite:** Install the [Aptible CLI](/reference/aptible-cli/cli-commands/overview) and [Redis CLI](https://redis.io/docs/install/install-redis/)
    </Note>

    <Steps>
      <Step title="Collect Configuration Information">
        **Step 1: Configuration**

        Collect information on the Database you'd like to upgrade and store it in the following environment variables in a terminal session for use later in the guide:

        * `OLD_HANDLE` - The handle (i.e. name) of the Database.
        * `ENVIRONMENT` - The handle of the Environment the Database belongs to.

        Example:

        ```bash  theme={null}
          SOURCE_HANDLE = 'old-db'
          ENVIRONMENT = 'test-environment'
        ```

        Collect information for the new Database and store it in the following environment variables:

        * `NEW_HANDLE` - The handle (i.e., name) for the Database.
        * `NEW_VERSION` - The desired Redis version. Run `aptible db:versions` to see a full list of options. Note that there are different ["flavors" of Redis](/core-concepts/managed-databases/supported-databases/redis) for each version. Double-check that the new version has the same flavor as the original database's version.
        * `NEW_CONTAINER_SIZE` (Optional) - The size of the new Database's container in MB. You likely want this value to be the same as the original database's container size. See the [Database Scaling](/core-concepts/scaling/database-scaling#ram-scaling) documentation for a full list of supported container sizes.
        * `NEW_DISK_SIZE` (Optional) - The size of the new Database's disk in GB. You likely want this value to be the same as the original database's disk size.

        Example:

        ```bash  theme={null}
          NEW_HANDLE = 'upgrade-test'
          NEW_VERSION = '7.0'
          NEW_CONTAINER_SIZE = 2048
          NEW_DISK_SIZE = 10
        ```
      </Step>

      <Step title="Provision the new Database">
        Create the new Database using `aptible db:create`.

        Example:

        ```bash  theme={null}
          aptible db:create "$NEW_HANDLE" \
          --type "redis" \
          --version "$NEW_VERSION" \
          --container-size $NEW_CONTAINER_SIZE \
          --disk-size $NEW_DISK_SIZE \
          --environment "$ENVIRONMENT"
        ```
      </Step>

      <Step title="Tunnel into the new Database">
        In a separate terminal, create a [Database Tunnel](/core-concepts/managed-databases/connecting-databases/database-tunnels) to the new Database using the `aptible db:tunnel` command.

        Example:

        ```bash  theme={null}
          aptible db:tunnel "$NEW_HANDLE" --environment "$ENVIRONMENT"
        ```

        The tunnel will block the current terminal until it's stopped. Collect the tunnel's full URL, which is printed by [aptible db:tunnel](/reference/aptible-cli/cli-commands/cli-db-tunnel), and store it in the `NEW_URL` environment variable in the original terminal.

        Example:

        ```bash  theme={null}
          NEW_URL ='redis://aptible:pa$word@localhost.aptible.in:6379'
        ```
      </Step>

      <Step title="Retrieve the Old Database's Database Credentials">
        To initialize replication, you'll need the [Database Credentials](/core-concepts/managed-databases/connecting-databases/database-credentials) of the old database. We'll refer to these values as follows:

        * `OLD_HOST`
        * `OLD_PORT`
        * `OLD_PASSWORD`
      </Step>

      <Step title="Connect to the New Database">
        Using the Redis CLI in the original terminal, connect to the new database:

        ```bash  theme={null}
          redis-cli -u $NEW_URL
        ```
      </Step>

      <Step title="Initialize Replication">
        Using the variables from Step 4, run the following commands on the new database to initialize replication.

        ```bash  theme={null}
          REPLICAOF $OLD_HOST $OLD_PORT
          CONFIG SET masterauth $OLD_PASSWORD
        ```
      </Step>

      <Step title="Cutover to the New Database">
        When you're ready to cutover, point your Apps to the new Database and run `REPLICAOF NO ONE` via the Redis CLI to stop replication. Finally, deprovision the old database using the command aptible db:deprovision.
      </Step>
    </Steps>
  </Accordion>

  <Accordion title="Method 2: Dump and Restore to a new Redis Database">
    <Tip>
      We recommend Method 1 above, but you can also dump and restore to upgrade if you'd like. This method introduces extra downtime, as you must take your database offline before conducting the dump to prevent new writes and data loss.
    </Tip>

    <Note>
      **Prerequisite:** Install the [Aptible CLI](/reference/aptible-cli/cli-commands/overview), [Redis CLI](https://redis.io/docs/install/install-redis/), and [rdb tool](https://github.com/sripathikrishnan/redis-rdb-tools)
    </Note>

    <Steps>
      <Step title="Collection Configuration Information">
        Collect information on the Database you'd like to upgrade and store it in the following environment variables in a terminal session for use later in the guide:

        * `OLD_HANDLE` - The handle (i.e. name) of the Database.
        * `ENVIRONMENT` - The handle of the Environment the Database belongs to

        Example:

        ```bash  theme={null}
          SOURCE_HANDLE = 'old-db'
          ENVIRONMENT = 'test-environment'
        ```

        Collect information for the new Database and store it in the following environment variables:

        * `NEW_HANDLE` - The handle (i.e., name) for the Database.
        * `NEW_VERSION` - The desired Redis version. Run `aptible db:versions` to see a full list of options. Note that there are different ["flavors" of Redis](/core-concepts/managed-databases/supported-databases/redis) for each version. Double-check that the new version has the same flavor as the original database's version.
        * `NEW_CONTAINER_SIZE` (Optional) - The size of the new Database's container in MB. You likely want this value to be the same as the original database's container size. See the [Database Scaling](/core-concepts/scaling/database-scaling#ram-scaling) documentation for a full list of supported container sizes.
        * `NEW_DISK_SIZE` (Optional) - The size of the new Database's disk in GB. You likely want this value to be the same as the original database's disk size.

        Example:

        ```bash  theme={null}
          NEW_HANDLE = 'upgrade-test'
          NEW_VERSION = '7.0'
          NEW_CONTAINER_SIZE = 2048
          NEW_DISK_SIZE = 10
        ```
      </Step>

      <Step title="Provision the New Database">
        Create the new Database using `aptible db:create`.

        Example:

        ```bash  theme={null}
          aptible db:create "$NEW_HANDLE" \
          --type "redis" \
          --version "$NEW_VERSION" \
          --container - size $NEW_CONTAINER_SIZE \
          --disk - size $NEW_DISK_SIZE \
          --environment "$ENVIRONMENT"
        ```
      </Step>

      <Step title="Tunnel into the Old Database">
        In a separate terminal, create a [Database Tunnel](/core-concepts/managed-databases/connecting-databases/database-tunnels) to the old Database using the `aptible db:tunnel` command.

        Example:

        ```bash  theme={null}
          aptible db:tunnel "$NEW_HANDLE" --environment "$ENVIRONMENT"
        ```

        The tunnel will block the current terminal until it's stopped. Collect the tunnel's full URL, which is printed by `aptible db:tunnel`, and store it in the `OLD_URL` environment variable in the original terminal.

        Example:

        ```bash  theme={null}
          OLD_URL = 'redis://aptible:pa$word@localhost.aptible.in:6379'
        ```
      </Step>

      <Step title="Dump the Old Database">
        Dump the old database to a file locally using rdb and the Redis CLI.

        Example:

        ```bash  theme={null}
          redis-cli -u $OLD_URL --rdb dump.rdb
        ```
      </Step>

      <Step title="Tunnel into the New Database">
        In a separate terminal, create a [Database Tunnel](/core-concepts/managed-databases/connecting-databases/database-tunnels) to the new Database using the `aptible db:tunnel` command, and save the Connection URL as `NEW_URL`.
      </Step>

      <Step title="Restore the Redis Dump using rdb">
        Using the rdb tool, restore the dump to the new Database.

        ```
          rdb --command protocol dump.rdb | redis - cli - u $NEW_URL--pipe
        ```
      </Step>

      <Step title="Cutover to the New Database">
        Point your Apps and other resources to your new database and deprovision the old database using the command `aptible db:deprovision`.
      </Step>
    </Steps>
  </Accordion>
</Accordion>
