# Source: https://docs.mage.ai/observability/external/sentry.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.mage.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Monitoring with Sentry

## Provide your Sentry credentials

You will need to add the following environment variables in order to use
Sentry in Mage:

* `SENTRY_DSN`: sentry dsn url
* `SENTRY_TRACES_SAMPLE_RATE`: (optional) value between 0 and 1
* `SENTRY_SERVER_NAME`: (optional) Name of the Mage server

## Using Sentry in Mage

Once you set the `SENTRY_DSN` environment variable, the Sentry integration will be
enabled the next time you start the Mage server.

The following errors will be reported to Sentry:

* Exceptions from trigger runs.
* Exceptions from the Mage scheduler.
* Exceptions from runs started by the `mage run` CLI command.


Built with [Mintlify](https://mintlify.com).