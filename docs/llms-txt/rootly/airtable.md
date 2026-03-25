# Source: https://docs.rootly.com/integrations/airtable.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Airtable

> Connect Rootly with Airtable to automatically create records when incidents are declared, enabling seamless data integration and tracking.

## Why

**Airtable** Integration allows you to:

* Creating an incident in **Rootly** will create a record in a **Airtable** table of your choice if you choose to.

## Installation

You can setup this integration as a **logged in admin user** in the integrations page:

<Frame>
  <img alt="Document Image" src="https://mintcdn.com/rootly/d2dmochhUzziYtkZ/images/integrations/airtable/images-1.webp?fit=max&auto=format&n=d2dmochhUzziYtkZ&q=85&s=f604bef5dc8ed24221c59b4168dc5ae6" width="899" height="749" data-path="images/integrations/airtable/images-1.webp" />
</Frame>

Create an Oauth Application at [https://airtable.com/create/oauth](https://airtable.com/create/oauth "https://airtable.com/create/oauth")﻿

<Frame>
  <img alt="Document Image" src="https://mintcdn.com/rootly/d2dmochhUzziYtkZ/images/integrations/airtable/images-2.webp?fit=max&auto=format&n=d2dmochhUzziYtkZ&q=85&s=0087c2ef98913772d6d60c7597861546" width="893" height="351" data-path="images/integrations/airtable/images-2.webp" />
</Frame>

With as callback url: `https://rootly.com/auth/airtable/callback`

<Frame>
  <img alt="Document Image" src="https://mintcdn.com/rootly/d2dmochhUzziYtkZ/images/integrations/airtable/images-3.webp?fit=max&auto=format&n=d2dmochhUzziYtkZ&q=85&s=ae439ee52d906743ea239e2619067dcc" width="894" height="411" data-path="images/integrations/airtable/images-3.webp" />
</Frame>

## Permissions

Check the following scopes:

<Frame>
  <img alt="Document Image" src="https://mintcdn.com/rootly/d2dmochhUzziYtkZ/images/integrations/airtable/images-4.webp?fit=max&auto=format&n=d2dmochhUzziYtkZ&q=85&s=26a1186c1398932efe97e5af2aedb335" width="894" height="452" data-path="images/integrations/airtable/images-4.webp" />
</Frame>

## Settings

Copy your `client_id` and `client_secret` into rootly

<Frame>
  <img alt="Document Image" src="https://mintcdn.com/rootly/d2dmochhUzziYtkZ/images/integrations/airtable/images-5.webp?fit=max&auto=format&n=d2dmochhUzziYtkZ&q=85&s=23745bf59a37a145d69c863bbae8273e" width="899" height="780" data-path="images/integrations/airtable/images-5.webp" />
</Frame>

## Fields mapping[](#7z98s)

You can configure column mapping using our custom variables [Incident Variables](/liquid/incident-variables).

```json  theme={null}
{
  "Name": "{{incident.title}}",
  "Notes": "{{incident.summary}}",
  "Started At": "{{incident.started_at | date: '%FT%T%:z' }}",
  "Link": "{{incident.url}}"
}
```

## Uninstall

You can **uninstall** this integration in the integrations panel by clicking **Configure > Delete**


Built with [Mintlify](https://mintlify.com).