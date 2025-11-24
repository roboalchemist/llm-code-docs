# Source: https://www.aptible.com/docs/how-to-guides/database-guides/upgrade-mongodb.md

# Upgrade MongoDB

The goal of this guide is to upgrade a MongoDB [Database](/core-concepts/managed-databases/managing-databases/overview) to a newer release. The process is quick and easy to complete but only works from one release to the next, so in order to upgrade multiple releases, the process must be completed multiple times.

## Preparation

#### Step 0: Install the necessary tools

Install the [Aptible CLI](/reference/aptible-cli/cli-commands/overview) and the [MongoDB shell](https://www.mongodb.com/docs/v4.4/administration/install-community/), `mongo` .

#### Step 1: Configuration

Collect information on the Database you'd like to upgrade and store it in the following environment variables for use later in the guide:

* `DB_HANDLE` - The handle (i.e. name) of the Database.

* `ENVIRONMENT` - The handle of the environment the Database belongs to.

* `VERSION` - The desired MongoDB version. Run `aptible db:versions` to see a full list of options.

Example:

```bash  theme={null}
DB_HANDLE='my-redis'
ENVIRONMENT='test-environment'
VERSION='4.0'
```

#### Step 2: Contact Aptible Support

An Aptible team member must update the Database's metadata to the new version in order to upgrade the Database. When contacting [Aptible Support](/how-to-guides/troubleshooting/aptible-support) please adhere to the following rules to ensure a smooth upgrade process:

* Ensure that you have [Administrator Access](/core-concepts/security-compliance/access-permissions#write-permissions) to the Database's Environment. If you do not, please have someone with access contact support or CC an [Account Owner or Deploy Owner](/core-concepts/security-compliance/access-permissions) for approval.

* Use the same email address that's associated with your Aptible user account to contact support.

* Include the configuration values above. You may run the following command to generate a request with the required information:

```bash  theme={null}
echo "Please upgrade our MongoDB database, ${ENVIRONMENT} - ${DB_HANDLE}, to version ${VERSION}. Thank you."
```

## Execution

#### Step 1: Restart the Database

Once support has updated the Database, restarting it will apply the change. You may do so at your convenience with the [`aptible db:reload`](/reference/aptible-cli/cli-commands/cli-db-reload) CLI command:

```bash  theme={null}
aptible db:reload "$DB_HANDLE" --environment "$ENVIRONMENT"
```

When upgrading a replica set, restart secondary members first, then the primary member.

#### Step 2: Tunnel into the Database

In a separate terminal, create a [Database Tunnel](/core-concepts/managed-databases/connecting-databases/database-tunnels) to the Database using the Aptible CLI.

```bash  theme={null}
aptible db:tunnel "$DB_HANDLE" --environment "$ENVIRONMENT"
```

The tunnel will block the current terminal until it's stopped. Collect the tunnel's full URL, which is printed by [`aptible db:tunnel`](/reference/aptible-cli/cli-commands/cli-db-tunnel), and store it in the `DB_URL` environment variable in the original terminal.

Example:

```bash  theme={null}
DB_URL='postgresql://aptible:pa$word@localhost.aptible.in:5432/db'
```

#### Step 3: Enable Backward-Incompatible Features

Run the [`setFeatureCompatibilityVersion`](https://www.mongodb.com/docs/manual/reference/command/setFeatureCompatibilityVersion/) admin command on the Database:

```bash  theme={null}
echo "db.adminCommand({ setFeatureCompatibilityVersion: '${VERSION}' })" |
  mongo --ssl --authenticationDatabase admin "$DB_URL"
```
