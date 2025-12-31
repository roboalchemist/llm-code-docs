# Source: https://www.aptible.com/docs/core-concepts/integrations/sumo-logic.md

# Sumo Logic Integration

> Learn about sending Aptible logs to Sumo Logic

# Overview

[Sumo Logic](https://www.sumologic.com/) is a cloud-based log management and analytics platform. Aptible integrates with Sumo Logic, allowing logs to be sent directly to Sumo Logic for analysis and storage.

Sumo Logic signs BAAs and thus is a reliable log drain option for HIPAA compliance.

# Set up

<Info>  Prerequisites: A [Sumo Logic account](https://service.sumologic.com/ui/) </Info>

You can send your Aptible logs directly to Sumo Logic with a [log drain](/core-concepts/observability/logs/log-drains/overview). A Sumo Logic log drain can be created in the following ways on Aptible:

* Within the Aptible Dashboard by:
  * Navigating to an Environment
  * Selecting the **Log Drains** tab
  * Selecting **Create Log Drain**
  * Selecting **Sumo Logic**
  * Filling the URL by creating a new [Hosted Collector](https://help.sumologic.com/docs/send-data/hosted-collectors/) in Sumologic using an HTTP source
* Using the [`aptible log_drain:create:sumologic`](/reference/aptible-cli/cli-commands/cli-log-drain-create-sumologic) command
