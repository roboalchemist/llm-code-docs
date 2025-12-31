# Source: https://grafbase.com/docs/platform/self-hosting/cli.md

If you haven't installed the Grafbase CLI yet, see the [Installation section](https://grafbase.com/docs/cli/installation.md).

## Interactive use

By default, the CLI will communicate with the API hosted at `https://grafbase.com`. To use the API in your self-hosted instance of the Enterprise Platform, you have to log in using the `--url` flag. Let's see how this works.

First, log out if you are already logged in:

```bash
grafbase logout
```

Then, find the URL of the dashboard (web UI) in your self hosted instance. For example, if you have a local instance created using the [guide](/guides/installing-grafbase-enterprise-platform), it will be `http://localhost:30081`. The command will look like this:

```bash
grafbase login --url http://localhost:30081
```

Log in interactively in the browser tab that the CLI opens, and the CLI is configured. Your credentials and the proper url for your own installation of the API are stored in `$HOME/.grafbase`.

## In scripts and CI

If you are using the CLI in non-interactive contexts, you will need to set the `GRAFBASE_ACCESS_TOKEN` environment variable with a valid access token, and the `GRAFBASE_API_URL` environment variable with the URL the GraphQL endpoint of your hosted instance of the API. For example, if you host the API at `https://grafbase-ep.mydomain.org`, the environment variable should be set to `https://grafbase-ep.mydomain.org/graphql`.