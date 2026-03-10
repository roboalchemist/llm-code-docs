# Source: https://developers.webflow.com/mcp/reference/data/sites.mdx

***

title: Sites
description: 'Manage Webflow sites, retrieve site information, and publish sites to domains'
--------------------------------------------------------------------------------------------

Manage your Webflow sites, retrieve detailed site information, and publish sites to specific domains using the Sites tools.

***

## List sites

List all sites accessible to the authenticated user. Returns basic site information including site ID, name, and last published date.

**Tool:** `sites_list`

<EndpointRequestSnippet endpoint="GET /v2/sites" />

**Returns**

<EndpointResponseSnippet endpoint="GET /v2/sites" />

***

## Get site details

Get detailed information about a specific site including its settings, domains, and publishing status.

**Tool:** `sites_get`

<Card>
  <ParamField path="site_id" type="string" required={true}>
    Unique identifier for the site
  </ParamField>
</Card>

<EndpointRequestSnippet endpoint="GET /v2/sites/{site_id}" />

**Returns**

<EndpointResponseSnippet endpoint="GET /v2/sites/{site_id}" />

***

## Publish site

Publish a site to specified domains. This makes the latest changes live on the specified domains.

**Tool:** `sites_publish`

<Card>
  <ParamField path="site_id" type="string" required={true}>
    Unique identifier for the site
  </ParamField>

  <ParamField path="customDomains" type="array" required={false}>
    Array of custom domain IDs to publish the site to
  </ParamField>

  <ParamField path="publishToWebflowSubdomain" type="boolean" required={false} default="false">
    Whether to publish to the Webflow subdomain
  </ParamField>
</Card>

<EndpointRequestSnippet endpoint="POST /v2/sites/{site_id}/publish" />

**Returns:** Publishing status and confirmation

<EndpointResponseSnippet endpoint="POST /v2/sites/{site_id}/publish" />
