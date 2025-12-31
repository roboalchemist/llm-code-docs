# Source: https://docs.upsun.com/development/local.md

# Source: https://docs.upsun.com/guides/symfony/local.md

# Source: https://docs.upsun.com/guides/django/local.md

# Source: https://docs.upsun.com/development/local.md

# Source: https://docs.upsun.com/guides/symfony/local.md

# Source: https://docs.upsun.com/guides/django/local.md

# Source: https://docs.upsun.com/development/local.md

# Set up your local development environment

To make changes to your app's code and test them without affecting your production environment,
set up a local development environment on your computer.

For the most effective testing, you want your local environment to match your Upsun environments.
The best way to do this is to use a cross-platform tool based on Docker.
This ensures the changes you make locally appear as they would on your Upsun environments.
It also means you don't have to worry about configuring your machine with
the various dependencies, certificates, and connections your app needs to run.

The **recommended tool** for local development with Upsun is **[DDEV](https://docs.upsun.com/development/local/ddev.md)**.
The integration with DDEV is maintained by Upsun to ensure it works smoothly.

If you choose to use DDEV, follow the steps [on its page](https://docs.upsun.com/development/local/ddev.md). Otherwise, follow these steps to run your app on your computer.

## Before you begin

You need to have:

- A Upsun account:
  new users can [register here](https://upsun.com/register/)
- A working project
- [Git](https://git-scm.com/downloads)
- The [Upsun CLI](https://docs.upsun.com../../administration/cli.md)

## 1. Get your code

If you don't have your app code on your computer, download a copy.

1.  Get your project ID by running `upsun projects`.

2.  Get the code by running the following command:

    ```bash
    upsun get <PROJECT_ID> <TARGET_DIRECTORY_NAME>
    ```

    Or pull from your [integrated Git repository](https://docs.upsun.com../../integrations/source.md).

You can now access your code from the project directory on your computer.
The CLI created a `.upsun/config.yaml/local` directory that's excluded from Git.
It contains builds and local metadata about your project.

You can now make changes to your project without pushing to Upsun each time to test them.
Instead, you can locally build your application using the Upsun CLI.

Note that if your app contains services, you need to open an SSH tunnel to connect to them.
For more information, see how to [connect services](https://docs.upsun.com../../add-services#2-define-the-relationship).

## 2. Connect to services

If your app requires services to run, you have two options for developing locally:

- [Tethered local development](https://docs.upsun.com/development/local/tethered.md) involves running your app on a local web server
  but keeping all other services on Upsun and connecting to them over an SSH tunnel.
- [Untethered local development](https://docs.upsun.com/development/local/untethered.md) involves running your entire site locally,
  including all services.

Choose the option that works for you and get your services running.

