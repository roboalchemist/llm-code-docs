# Source: https://www.aptible.com/docs/core-concepts/integrations/solarwinds.md

# SolarWinds Integration

> Learn about sending Aptible logs to SolarWinds

## Overview

SolarWinds Observability is a cloud-based platform for log management and analytics. With Aptible's integration, you can send logs directly to SolarWinds for analysis and storage.

## Set up

<Info> Prerequisites: A SolarWinds account</Info>

<Steps>
  <Step title="Configure your SolarWinds account for Aptible Log Ingestion">
    Refer to the [SolarWinds documentation](https://documentation.solarwinds.com/en/success_center/observability/content/configure/configure-logs.htm) for setting up your account to receive logs. Aptible sends logs securely via Syslog+TLS, and all we need is the syslog hostname and token from your SolarWinds account.

    Note: Like all Aptible Log Drain providers, SolarWinds also offers Business Associate Agreements (BAAs). To ensure HIPAA compliance, please contact them to execute a BAA.
  </Step>

  <Step title="Configure your Log Drain">
    You can send your Aptible logs directly to SolarWinds with a log drain. A SolarWinds Log Drain can be created in the following ways on Aptible:

    * Within the Aptible Dashboard by:
      * Navigating to an Environment
      * Selecting the **Log Drains** tab
      * Selecting **Create Log Drain**
      * Selecting **SolarWinds**
      * Entering your SolarWinds hostname
      * Entering your SolarWinds token
    * Using the [`aptible log_drain:create:solarwinds`](/reference/aptible-cli/cli-commands/cli-log-drain-create-solarwinds) command
    * Using the [Aptible Terraform Provider](/reference/terraform)
  </Step>
</Steps>
