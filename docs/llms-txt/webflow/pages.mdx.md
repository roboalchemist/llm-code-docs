# Source: https://developers.webflow.com/mcp/reference/data/pages.mdx

***

title: Pages
description: 'Manage static pages, update page settings, and modify page content'
---------------------------------------------------------------------------------

Manage static pages in your Webflow site, update page metadata and settings, and modify page content using the Pages tools.

***

## List pages

List all pages within a site. Returns page metadata including IDs, titles, and slugs.

**Tool:** `pages_list`

<Card>
  <ParamField path="site_id" type="string" required={true}>
    The site’s unique ID, used to list its pages.
  </ParamField>

  <ParamField path="localeId" type="string" required={false}>
    Unique identifier for a specific locale. Applicable when using localization.
  </ParamField>

  <ParamField path="limit" type="number" required={false}>
    Maximum number of records to be returned (max limit: 100)
  </ParamField>

  <ParamField path="offset" type="number" required={false}>
    Offset used for pagination if the results have more than limit records.
  </ParamField>
</Card>

<EndpointRequestSnippet endpoint="GET /v2/sites/{site_id}/pages" />

**Returns**

<EndpointResponseSnippet endpoint="GET /v2/sites/{site_id}/pages" />

***

## Get page metadata

Get metadata for a specific page including SEO settings, Open Graph data, and page status (draft/published).

**Tool:** `pages_get_metadata`

<Card>
  <ParamField path="page_id" type="string" required={true}>
    Unique identifier for the page.
  </ParamField>

  <ParamField path="localeId" type="string" required={false}>
    Unique identifier for a specific locale. Applicable when using localization.
  </ParamField>
</Card>

<EndpointRequestSnippet endpoint="GET /v2/pages/{page_id}" />

**Returns**

<EndpointResponseSnippet endpoint="GET /v2/pages/{page_id}" />

***

## Update page settings

Update page settings including SEO metadata, Open Graph data, slug, and publishing status.

**Tool:** `pages_update_page_settings`

<Card>
  <ParamField path="page_id" type="string" required={true}>
    Unique identifier for the page.
  </ParamField>

  <ParamField path="localeId" type="string" required={false}>
    Unique identifier for a specific locale. Applicable when using localization.
  </ParamField>

  <ParamField path="body" type="object" required={true}>
    Page settings object with fields to update
  </ParamField>
</Card>

<EndpointRequestSnippet endpoint="PUT /v2/pages/{page_id}" />

**Returns:** Updated page metadata

<EndpointResponseSnippet endpoint="PUT /v2/pages/{page_id}" />

***

## Get page content

Get the content structure and data for a specific page including all elements and their properties.

**Tool:** `pages_get_content`

<Card>
  <ParamField path="page_id" type="string" required={true}>
    Unique identifier for the page.
  </ParamField>

  <ParamField path="localeId" type="string" required={false}>
    Unique identifier for a specific locale. Applicable when using localization.
  </ParamField>

  <ParamField path="limit" type="number" required={false}>
    Maximum number of records to be returned (max limit: 100)
  </ParamField>

  <ParamField path="offset" type="number" required={false}>
    Offset used for pagination if the results have more than limit records.
  </ParamField>
</Card>

<EndpointRequestSnippet endpoint="GET /v2/pages/{page_id}/dom" />

**Returns**

<EndpointResponseSnippet endpoint="GET /v2/pages/{page_id}/dom" />

***

## Update static content

Update content on a static page in secondary locales by modifying text nodes and property overrides.

**Tool:** `pages_update_static_content`

<Warning>
  This tool is only for updating content in secondary locales. The `localeId` parameter is required, and requests to update primary locale content will fail.
</Warning>

<Card>
  <ParamField path="page_id" type="string" required={true}>
    Unique identifier for the page.
  </ParamField>

  <ParamField path="localeId" type="string" required={true}>
    Unique identifier for the target locale.
  </ParamField>

  <ParamField path="nodes" type="array" required={true}>
    Array of node updates with text content and property overrides
  </ParamField>
</Card>

<EndpointRequestSnippet endpoint="POST /v2/pages/{page_id}/dom" />

**Returns:** Updated page content confirmation

<EndpointResponseSnippet endpoint="POST /v2/pages/{page_id}/dom" />
