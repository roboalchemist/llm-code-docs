# Source: https://www.mux.com/docs/guides/monitor-castlabs-prestoplay-web.md

# Monitor castLabs Player (Web)
This guide walks through integration with [castLabs PRESTOplay for Web](https://castlabs.com/prestoplay/web-apps/) to collect video performance metrics with Mux Data.
<Callout type="warning" title="Third-party integration">
  This integration is managed and operated by [castLabs](https://castlabs.com/).
  Feedback should be made by using the [contact form](https://castlabs.com/contact/) or creating a ticket in the [General Helpdesk](https://castlabs.atlassian.net/servicedesk/customer/portal/26).
</Callout>

# Mux Environment Key

Get your `ENV_KEY` from the [Mux environments dashboard](https://dashboard.mux.com/environments).

<Callout type="info" title="Env Key is different than your API token">
  `ENV_KEY` is a client-side key used for Mux Data monitoring. These are not to be confused with API tokens which are created in the admin settings dashboard and meant to access the Mux API from a trusted server.
</Callout>

<Image src="/docs/images/env-key.png" width={2004} height={250} />

# Integration Guide

CastLabs maintains an online version of the official documentation which you can check out [here](https://demo.castlabs.com/#/docs/analytics#mux-data).
