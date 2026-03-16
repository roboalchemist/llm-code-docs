# Source: https://docs.rootly.com/integrations/victor-ops.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# VictorOps (Splunk On-Call)

> Connect Rootly with VictorOps (Splunk On-Call) to import teams, create alerts, and synchronize incident management workflows.

## Why

**VictorOps** Integration allows you to:

* Import **VictorOps** teams into Rootly teams.
* **Create** a Rootly alert when creating an incident in **VictorOps**.
* **Create** a VictorOps incident when creating an incident in Rootly.
* **Resolve** a VictorOps incident right from Rootly.
* Page Directly from Slack ( if Slack Integration enabled ).

**Note:** This integration required an VictorOps account with at least the **Enterprise** plan. [https://portal.victorops.com/dash/rootly-inc#/billing](https://portal.victorops.com/dash/rootly-inc#/billing)

## Installation

You can setup this integration as a **logged in admin user** in the integrations page:

<Frame>
  <img alt="Document Image" src="https://mintcdn.com/rootly/ljLqQxzWDg3HgLpA/images/integrations/victor-ops/images-1.webp?fit=max&auto=format&n=ljLqQxzWDg3HgLpA&q=85&s=918915dea0fa87488a50fa5d0fbeb71d" width="913" height="444" data-path="images/integrations/victor-ops/images-1.webp" />
</Frame>

<Note>
  We recommend you integrating with a **service account** to make sure the integration doesn't break if a user leaves your company.
</Note>

## Configuration

Let's get API keys in VictorOps portal.

<Frame>
  <img alt="Document Image" src="https://mintcdn.com/rootly/ljLqQxzWDg3HgLpA/images/integrations/victor-ops/images-2.webp?fit=max&auto=format&n=ljLqQxzWDg3HgLpA&q=85&s=7a85934fc7834e0cded1a9aef6baaf25" width="915" height="421" data-path="images/integrations/victor-ops/images-2.webp" />
</Frame>

You can also optionally configure webhooks so we ingest VictorOps incidents as Rootly alerts.

<Frame>
  <img alt="Document Image" src="https://mintcdn.com/rootly/ljLqQxzWDg3HgLpA/images/integrations/victor-ops/images-3.webp?fit=max&auto=format&n=ljLqQxzWDg3HgLpA&q=85&s=d3da196b841a9d097707546303a3e8a1" width="914" height="434" data-path="images/integrations/victor-ops/images-3.webp" />
</Frame>

Copy the url above and create a webhook:

<Frame>
  <img alt="Document Image" src="https://mintcdn.com/rootly/ljLqQxzWDg3HgLpA/images/integrations/victor-ops/images-4.webp?fit=max&auto=format&n=ljLqQxzWDg3HgLpA&q=85&s=365fba272d0e0b6b0196c44b9424e0f9" width="908" height="536" data-path="images/integrations/victor-ops/images-4.webp" />
</Frame>

## Paging

You can page VictorOps teams right from Slack using our integration.

<Frame>
  <img alt="Document Image" src="https://mintcdn.com/rootly/ljLqQxzWDg3HgLpA/images/integrations/victor-ops/images-5.webp?fit=max&auto=format&n=ljLqQxzWDg3HgLpA&q=85&s=cbff8a3ec7b32464bc32d3603ddf504d" width="894" height="291" data-path="images/integrations/victor-ops/images-5.webp" />
</Frame>


Built with [Mintlify](https://mintlify.com).