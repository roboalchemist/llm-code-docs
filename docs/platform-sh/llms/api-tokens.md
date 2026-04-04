# Source: https://docs.upsun.com/administration/cli/api-tokens.md

# Authenticate the CLI using an API token

You need to set up an API token to authenticate the Upsun CLI for any of the following tasks:
- Running automated tasks on a CI system
- Running automated tasks directly on app container, for example in a cron job

## Before you begin

You might need the [Upsun CLI](https://docs.upsun.com../cli.md) to perform certain tasks.
For example, you need the CLI to do the following:
- [Check the validity of an API token](#optional-check-the-validity-of-your-api-token).
- [Load the CLI SSH certificate for non-CLI commands](#use-the-cli-ssh-certificate-for-non-cli-commands).

## 1. Create a machine user

To safely run automated tasks, first create machine users.
Each machine user has its own Upsun account associated with a unique email address.
You can grant them restrictive [access permissions](https://docs.upsun.com../users.md) to handle specific automated tasks.
For security purposes, create a machine user for each type of task you want to automate.

To create a machine user, follow these steps:

This sets your machine user as a viewer on your project and a contributor on development environments,
with no access to other environment types.
Note that you can further [adjust user roles](https://docs.upsun.com/administration/users.md#environment-type-roles) depending on your needs and each environment type.

 - In the email invitation, click **Create account**.

 - To create an Upsun account for the machine user, click **Sign up** and follow the instructions.

 - Go to your project and click Settings **Settings**.
 - In the **Project Settings** menu, click **Access**.
 - Click **Add**.
 - Enter your machine user’s email address.
 - For each [environment type](https://docs.upsun.com/administration/users.md#environment-type-roles), assign a role to your machine user and click **Save**.

**Note**: 

Machine users with an email address under your single sign-on (SSO) domain can be excluded from the SSO enforcement rule so they aren’t required to authenticate through your identity provider. See the [SSO documentation](https://docs.upsun.com/administration/security/sso.md#service-users) for more information.

## 2. Create an API token

1. Log in to the Console as your machine user.
2. Open the user menu (your name or profile picture).
3. Click **My profile**.
4. Go to the **API tokens** tab and click **Create API token**.
5. Enter a name for your API token and click **Create API token**.
6. To copy the API token to your clipboard, click ** Copy**.
   Note that after you close the **API tokens** tab, you can't display the API token again.
7. Store the API token somewhere secure on your computer.

### Optional: check the validity of your API token

To check that your API token is valid, run the following command:

```bash
upsun auth:api-token-login
```

When prompted, enter your API token.
You get output similar to this:

```bash
The API token is valid.
You are logged in.
```

For security reasons, rotate your API tokens regularly.
When an API token is compromised, revoke it immediately.

## 3. Authenticate the CLI using your API token

After you create your API token, you can use it to do the following:

-  Allow a CI system to run automated tasks using the Upsun CLI.
-  Run automated tasks on an app container using the Upsun CLI,
   for example in a cron job.

Note that when running CLI commands in these cases,
some operations might take time to complete.
To avoid waiting for an operation to complete before moving on to the next one,
use the `--no-wait` flag.

### Authenticate in a CI system

You can allow your CI system to run automated tasks using the Upsun CLI.
To do so, create an environment variable named `UPSUN_CLI_TOKEN` with your API token as its value.
For more information, see your CI system's official documentation.

To run SSH-based commands that aren't specific to the Upsun CLI,
see how to [load the proper SSH certificate](#use-the-cli-ssh-certificate-for-non-cli-commands).

### Authenticate in an environment

You can run automated tasks on an app container using the Upsun CLI.
To do so, set your API token as a [top-level environment variable](https://docs.upsun.com../../development/variables.md#top-level-environment-variables).

**Note**: 

Once you add the token as an environment variable,
anyone with [SSH access](https://docs.upsun.com/development/ssh.md) can read its value.
Make sure your [machine user has only the necessary permissions](#1-create-a-machine-user).

 - Open the environment where you want to add the variable.
 - Click Settings **Settings**.
 - Click **Variables**.
 - Click **+ Add variable**.
 - In the **Variable name** field, enter ``env:UPSUN_CLI_TOKEN``.
 - In the **Value** field, enter your API token.
 - Make sure the **Available at runtime** and **Sensitive variable** options are selected.
 - Click **Add variable**.

Then add a build hook to your app configuration to install the CLI as part of the build process.

```yaml  {location=".upsun/config.yaml"}
hooks:
  build: |
    set -e
    echo "Installing Upsun CLI"
    curl -fsSL https://raw.githubusercontent.com/platformsh/cli/main/installer.sh | bash

    echo "Testing Upsun CLI"
    upsun
```

You can now call the CLI from within the shell on the app container or in a cron job.

To run SSH-based commands that aren't specific to the Upsun CLI,
see how to [load the proper SSH certificate](#use-the-cli-ssh-certificate-for-non-cli-commands).

You can set up a cron job on a specific type of environment.
For example, to run the `update` source operation on your production environment,
use the following cron job:

```yaml
crons:
  update:
    spec: '0 0 * * *'
    commands:
      start: |
        if [ "$PLATFORM_ENVIRONMENT_TYPE" = production ]; then
          upsun backup:create --yes --no-wait
          upsun source-operation:run update --no-wait --yes
        fi
```

## Use the CLI SSH certificate for non-CLI commands

When you set a `UPSUN_CLI_TOKEN` environment variable,
the CLI authentication isn't complete until your run a CLI command
or load the CLI SSH certificate.

For example, after setting a `UPSUN_CLI_TOKEN` environment variable,
you might need to run `ssh`, `git`, `rsync`, or `scp` commands before you run any CLI commands.

In this case, to ensure all your commands work, load the CLI SSH certificate first.
To do so, run the following command:

```bash
upsun ssh-cert:load --no-interaction
```

