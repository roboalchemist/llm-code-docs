# Source: https://www.aptible.com/docs/core-concepts/integrations/mezmo.md

# Mezmo Integration

> Learn about sending Aptible logs to Mezmo

## Overview

Mezmo, formerly known as LogDNA, is a cloud-based platform for log management and analytics. With Aptible's integration, you can send logs directly to Mezmo for analysis and storage.

## Set up

<Info> Prerequisites: A Mezmo account</Info>

<Steps>
  <Step title="Configure your Mezmo account for Aptible Log Ingestion">
    Refer to the [Mezmo documentation for setting up Aptible Log Ingestion on Mezmo.](https://docs.mezmo.com/docs/aptible-logs)

    Note: Like all Aptible Log Drain providers, Mezmo also offers Business Associate Agreements (BAAs). To ensure HIPAA compliance, please contact them to execute a BAA.
  </Step>

  <Step title="Configure your Log Drain">
    You can send your Aptible logs directly to Mezmo with a [log drain](https://www.aptible.com/docs/log-drains). A Mezmo/LogDNA Log Drain can be created in the following ways on Aptible:

    * Within the Aptible Dashboard by:
      * Navigating to an Environment
      * Selecting the **Log Drains** tab
      * Selecting **Create Log Drain**
      * Selecting **Mezmo**
      * Entering your Mezmo URL
    * Using the [`aptible log_drain:create:logdna`](/reference/aptible-cli/cli-commands/cli-log-drain-create-logdna) command
  </Step>
</Steps>
