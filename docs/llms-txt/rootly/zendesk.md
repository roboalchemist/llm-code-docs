# Source: https://docs.rootly.com/integrations/zendesk.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Zendesk

> Create and sync tickets automatically between Rootly incidents and Zendesk, with bidirectional updates and marketplace plugin support.

Leverage our popular Zendesk integration for automatic ticket creation and syncing. In addition to the Rootly Zendesk integration, you can bring Rootly right into Zendesk with our new plugin from the [Zendesk Marketplace](https://www.zendesk.com/marketplace/apps/support/995423/rootly/ "Zendesk Marketplace").

## Integration Capabilities

Our **Zendesk** Integration allows you to:

* Ability to create a Rootly incident directly in Zendesk.
  <Frame>
    <img alt="Document Image" src="https://mintcdn.com/rootly/ljLqQxzWDg3HgLpA/images/integrations/zendesk/images-1.webp?fit=max&auto=format&n=ljLqQxzWDg3HgLpA&q=85&s=5e09b6a02ad41ba96ee635b80399ced4" width="1024" height="768" data-path="images/integrations/zendesk/images-1.webp" />
  </Frame>
* Updating the incident's title, description, and/or status in Rootly will also update the corresponding Zendesk ticket.
* Ability to create a Rootly action item in Zendesk.
* Updating an action item's title, description, and/or status in Rootly will also update the corresponding Zendesk ticket.
* Ability to view, search, and attach recent Rootly incidents in Zendesk.
  <Frame>
    <img alt="Document Image" src="https://mintcdn.com/rootly/ljLqQxzWDg3HgLpA/images/integrations/zendesk/images-2.webp?fit=max&auto=format&n=ljLqQxzWDg3HgLpA&q=85&s=9f5ef3cd8efe499c37d67b2ec3b150d5" width="1024" height="768" data-path="images/integrations/zendesk/images-2.webp" />
  </Frame>
* Ability to view active or related Rootly incidents in Zendesk and attach them to the Zendesk ticket.
  <Frame>
    <img alt="Document Image" src="https://mintcdn.com/rootly/ljLqQxzWDg3HgLpA/images/integrations/zendesk/images-3.webp?fit=max&auto=format&n=ljLqQxzWDg3HgLpA&q=85&s=a859b27074a3bfb2d3b823ed64743939" width="1024" height="768" data-path="images/integrations/zendesk/images-3.webp" />
  </Frame>

Limitations include:

* Changing Zendesk incident ticket attributes will not update incident attributes in Rootly.
* Changing the Zendesk action item ticket status will not update the action item status in Rootly.

## Setting Up

<Note>
  We recommend that you integrate with a **service account** to ensure the integration continues to work if a user leaves your organization.
</Note>

To complete the integration setup, you will need to complete the following steps:﻿

1. Navigate to **Integrations --> Ticketing**
2. Select the **Zendesk** integration.
3. Enter your **Subdomain**.
4. Click '**Connect**'.

<Frame>
  <img alt="Document Image" src="https://mintcdn.com/rootly/ljLqQxzWDg3HgLpA/images/integrations/zendesk/images-4.webp?fit=max&auto=format&n=ljLqQxzWDg3HgLpA&q=85&s=db4acd5753116939cdbcf7c6d3e1c86b" width="895" height="398" data-path="images/integrations/zendesk/images-4.webp" />
</Frame>

## Permissions

Following oauth2 scopes are required

```ruby  theme={null}
users:read
tickets:write
webhooks:write
triggers:write
```

<Frame>
  <img alt="Document Image" src="https://mintcdn.com/rootly/ljLqQxzWDg3HgLpA/images/integrations/zendesk/images-5.webp?fit=max&auto=format&n=ljLqQxzWDg3HgLpA&q=85&s=2ef915a34a772934a8ee71b05882e0b2" width="901" height="543" data-path="images/integrations/zendesk/images-5.webp" />
</Frame>

## Uninstall

You can **uninstall** this integration in the integrations panel by clicking **Configure > Delete**


Built with [Mintlify](https://mintlify.com).