# Source: https://docs.upsun.com/development/local/tethered.md

# Tethered local development

To test changes locally, you can connect your locally running web server
to service containers on an active Upsun environment.
This method requires less configuration than tools such as [DDEV](https://docs.upsun.com/development/local/ddev.md),
but may not perform well enough for everyday use.
Because it replies on a local web server, it's also less consistent across your team.

## Before you begin

You need:

- A local copy of the repository for a  project running on Upsun.

  To get one, run ``upsun
 get <PROJECT_ID>
``.

  Alternatively, you can clone an integrated source repository and set the remote branch.
  To do so, run ``upsun
 project:set-remote <PROJECT_ID>
``.
- The [Upsun CLI](https://docs.upsun.com/administration/cli.md)

## Create the tethered connection

1. Create a new environment based on production.

   ```bash
   upsun branch new-feature <PRODUCTION_ENVIRONMENT_NAME>
   ```

   If you're using a [source integration](https://docs.upsun.com/integrations/source.md),
   open a merge/pull request.

1. To open an SSH tunnel to the new environment's services, run the following command:

   ```bash
   upsun tunnel:open
   ```

   This command returns the addresses for SSH tunnels to all of your services.

1. Export the `PLATFORMSH_RELATIONSHIPS` environment variable with information from the open tunnel:

   ```bash
   export PLATFORM_RELATIONSHIPS="$(upsun tunnel:info --encode)"
   ```

1.  Run your application locally.
    Make sure it's set up to read configuration from Upsun environment variables.

    If you app relies on other Upsun environment configuration, such as routes or secret variables,
    make sure to mock those variables as well.

    Your options for running the app depend on the language and configuration.
    You can use the server for your language, install a copy of Nginx,
    or use a virtual machine or Docker image.

1.  When you've finished your work, close the tunnels to your services by running the following command:

    ```bash
    upsun tunnel:close --all -y
    ```

## Connect to services directly

With open tunnels to all your services, you can also connect to the running services directly.
To get information on all running services, run the following command:

```bash
upsun tunnels
```

You get a response similar to the following:

```bash
+-------+---------------+-------------+-----+--------------+
| Port  | Project       | Environment | App | Relationship |
+-------+---------------+-------------+-----+--------------+
| 30000 | abcdefg123456 | new-feature | app | cache        |
| 30001 | abcdefg123456 | new-feature | app | database     |
+-------+---------------+-------------+-----+--------------+
```

You can use the port information to connect directly to a service.
If you need more detailed information, such as a path or password, run the following command:

```bash
upsun tunnel:info
```

You can use the information returned to connect to the remote database as if it were local.
For example, the following command would connect to a MySQL database running through a tethered connection:

```bash
mysql --host=127.0.0.1 --port=<PORT> --user=<USERNAME> --password=<PASSWORD> --database=<PATH>
```

## Next steps

You can now use your local environment to develop changes for review on Upsun environments.
The following examples show how you can take advantage of that.

### Onboard collaborators

It's essential for every developer on your team to have a local development environment to work on.
Place the local configuration into a script to ensure everyone has this.
You can merge this change into production.

1.  Create a new environment called `local-config`.

1.  To set up a local environment for a new Upsun environment, create an executable script.

    ```bash
    touch init-local.sh && chmod +x init-local.sh
    ```

1. Fill it with something similar to the following example, depending on your app and configuration:

   ```bash  {location="init-local.sh"}
   #!/usr/bin/env bash

   ENVIRONMENT=$1
   PARENT=$2

   # Create the new environment
   upsun branch $ENVIRONMENT $PARENT

   # Open a tunnel to the current environment
   upsun tunnel:open --no-interaction

   # Mock Upsun environment variables
   export PLATFORM_RELATIONSHIPS="$(upsun tunnel:info --encode)"

   # Add any other variables you need

   # If necessary, install dependencies here

   # Add the command to run the server
   ```

1. To commit and push the revisions, run the following command:

   ```bash
   git add . && git commit -m "Add local configuration" && git push upsun local-config
   ```

1.  Merge the change into production.

Once the script is merged into production,
any user can set up their local environment by running the following commands:

```bash
upsun <PROJECT_ID>
cd <PROJECT_NAME>
./init-local.sh <PROJECT_ID> another-new-feature <PRODUCTION_ENVIRONMENT_NAME>
```

