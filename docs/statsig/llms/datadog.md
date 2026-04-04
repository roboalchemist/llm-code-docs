# Source: https://docs.statsig.com/integrations/triggers/datadog.md

# Source: https://docs.statsig.com/integrations/datadog.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Datadog

### Overview

There are four key use-cases to the Datadog integration:

1. [Config Changes](#config-changes) - Streaming changes made in Statsig into Datadog, so you can see what feature was turned on that may have caused a CPU usage spike or some other degradation of performance (most widely-used integration).
2. [Event Forwarding](#events) - Statsig will forward event-count totals to DataDog, purely for the purpose of monitoring your Statsig usage volumes.
3. [Datadog RUM integration](#datadog-rum-integration) - This allows you to enrich DataDog RUM data with flag/experiment assignment info, allowing customer to correlate product feature changes with their impact on system/performance metrics.
4. [DataDog triggers](/integrations/triggers/datadog) - When an alarm goes off in DataDog, it kills a Statsig feature gate.

### Connecting to Datadog

1. To create a Datadog API key, navigate to **Organization Settings** > **API Keys**. If you have the permission to create API keys, click **New Key**.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/hdTkQo7iTJfd4sfn/images/integrations/datadog/232632837-d1e81380-78a3-48a2-887d-72b13d541b0a.png?fit=max&auto=format&n=hdTkQo7iTJfd4sfn&q=85&s=7dec8c14e17d7e90f3d57fcde9171631" alt="Datadog API key creation interface" width="2880" height="1634" data-path="images/integrations/datadog/232632837-d1e81380-78a3-48a2-887d-72b13d541b0a.png" />
</Frame>

2. Paste the API key in the text box at the top of the integration dialog, then hit "Confirm".

If the above is out of date, refer to the [Datadog documentation](https://docs.datadoghq.com/account_management/api-app-keys/#add-an-api-key-or-client-token) on how to setup API Keys

### Config Changes

This integration will send Datadog Events of your choice when your
project's settings change. For instance, we will send an Event when
someone edits a Feature Gate.

These events can be found in the Datadog Events Explorer.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/hdTkQo7iTJfd4sfn/images/integrations/datadog/232636042-ee5cf1d0-e9e7-4158-903b-5a447ab14575.png?fit=max&auto=format&n=hdTkQo7iTJfd4sfn&q=85&s=9fb9b4af402c6e0d284dc0754cf1baca" alt="Datadog Events Explorer interface" width="2880" height="1520" data-path="images/integrations/datadog/232636042-ee5cf1d0-e9e7-4158-903b-5a447ab14575.png" />
</Frame>

### Event Totals Forwarding

This integration will forward the <i>number</i> of Statsig SDK Events
reported to Datadog. This is meant for monitoring your project's Statsig
usage. This integration also has the option to allow non-production events
to be forwarded to Datadog.

Statsig events are mapped to Datadog metrics with listed tags as follows:

* statsig::gate\_exposure -> statsig.check\_gate.count

  * environment
  * name
  * value

* statsig::config\_exposure -> statsig.get\_config.count

  * environment

* statsig::experiment\_exposure -> statsig.get\_experiment.count

  * environment
  * group
  * name

* statsig::layer\_exposure -> statsig.get\_layer.count

  * environment
  * name

* statsig::holdout\_exposure -> statsig.get\_holdout.count
  * environment
  * name
  * value

#### Example of check\_gate metric

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/hdTkQo7iTJfd4sfn/images/integrations/datadog/232629870-e1776bd6-c63d-438d-863e-2d7a3a347eab.png?fit=max&auto=format&n=hdTkQo7iTJfd4sfn&q=85&s=a0340aafbca66965bc32433adab7df9f" alt="Datadog check_gate metric visualization" width="1200" height="761" data-path="images/integrations/datadog/232629870-e1776bd6-c63d-438d-863e-2d7a3a347eab.png" />
</Frame>

### Datadog RUM integration

This integration requires a client-side setup as outlined [here in DataDog documentation](https://docs.datadoghq.com/integrations/statsig-rum/).


Built with [Mintlify](https://mintlify.com).