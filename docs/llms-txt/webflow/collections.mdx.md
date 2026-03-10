# Source: https://developers.webflow.com/mcp/reference/data/cms/collections.mdx

***

title: Collections
description: Create and manage CMS collections in your Webflow site
-------------------------------------------------------------------

Create and manage CMS collections using the Collections tools. Collections define the structure and schema for your content.

***

## List collections

List all CMS collections in a site. Returns collection metadata including IDs, names, and schemas.

**Tool:** `collections_list`

<Card>
  <ParamField path="site_id" type="string" required={true}>
    Unique identifier for the site
  </ParamField>
</Card>

**Returns**

<EndpointResponseSnippet endpoint="GET /v2/sites/{site_id}/collections" />

***

## Get collection details

Get detailed information about a specific CMS collection including its schema and field definitions.

**Tool:** `collections_get`

<Card>
  <ParamField path="collection_id" type="string" required={true}>
    Unique identifier for the collection
  </ParamField>
</Card>

**Returns**

<EndpointResponseSnippet endpoint="GET /v2/collections/{collection_id}" />

***

## Create collection

Create a new CMS collection in a site with specified name and schema.

**Tool:** `collections_create`

<Card>
  <ParamField path="site_id" type="string" required={true}>
    Unique identifier for the site
  </ParamField>

  <ParamField path="request" type="object" required={true}>
    Collection creation request

    <Accordion title="+ Show 3 properties">
      <ParamField path="displayName" type="string" required={true}>
        Collection name
      </ParamField>

      <ParamField path="singularName" type="string" required={true}>
        Singular form of the name
      </ParamField>

      <ParamField path="slug" type="string" required={true}>
        URL slug for the collection
      </ParamField>
    </Accordion>
  </ParamField>
</Card>

<EndpointRequestSnippet endpoint="POST /v2/sites/{site_id}/collections" />
