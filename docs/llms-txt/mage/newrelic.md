# Source: https://docs.mage.ai/observability/external/newrelic.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.mage.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Monitoring with New Relic

## Enable New Relic

You will need to add `ENABLE_NEW_RELIC` environment variable as `true` in order to use
New Relic in Mage.

## New Relic Configuration File

Following [New Relic Python integration guide](https://docs.newrelic.com/install/python/?python-non-web=non-web-yes),
run command: `newrelic-admin generate-config YOUR_LICENSE_KEY newrelic.ini`
to generate the `newrelic.ini` configuration file and edit your `newrelic.ini` and insert values for the following:
...
license\_key = INSERT\_YOUR\_LICENSE\_KEY
...
app\_name = INSERT\_YOUR\_APP\_NAME
...

An example `example_newrelic.ini` file is attacehd in Mage repo under folder `integrations/newrelic`.

Add path of your newrelic configuration into environment variable `NEW_RELIC_CONFIG_PATH`.

## Using New Relic in Mage

Monitoring with New Relic will be enabled the next time you start the Mage server.

The following logs and errors will be reported to New Relic:

* Trigger runs.
* Mage scheduler.
* `mage run` CLI command.


Built with [Mintlify](https://mintlify.com).