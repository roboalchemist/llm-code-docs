# Source: https://developers.webflow.com/mcp/reference/data/components.mdx

***

title: Components
description: >-
Manage Webflow components, update component content, and configure component
properties
----------

Manage Webflow components, update component content, and configure component properties using the Components tools. Components are reusable design elements that can be instantiated across multiple pages.

***

## List components

List all components in a site. Returns component metadata including IDs, names, and versions.

**Tool:** `components_list`

<Card>
  <ParamField path="site_id" type="string" required={true}>
    Unique identifier for the site
  </ParamField>

  <ParamField path="limit" type="number" required={false}>
    Maximum number of records to return (max: 100)
  </ParamField>

  <ParamField path="offset" type="number" required={false}>
    Offset for pagination
  </ParamField>
</Card>

**Returns**

<EndpointResponseSnippet endpoint="GET /v2/sites/{site_id}/components" />

***

## Get component content

Get the content structure and data for a specific component including text, images, and nested components.

**Tool:** `components_get_content`

<Card>
  <ParamField path="site_id" type="string" required={true}>
    Unique identifier for the site
  </ParamField>

  <ParamField path="component_id" type="string" required={true}>
    Unique identifier for the component
  </ParamField>

  <ParamField path="localeId" type="string" required={false}>
    Unique identifier for a specific locale (for localized sites)
  </ParamField>

  <ParamField path="limit" type="number" required={false}>
    Maximum number of records to return (max: 100)
  </ParamField>

  <ParamField path="offset" type="number" required={false}>
    Offset for pagination
  </ParamField>
</Card>

**Returns**

<EndpointResponseSnippet endpoint="GET /v2/sites/{site_id}/components/{component_id}/dom" />

***

## Update component content

Update content on a component in secondary locales by modifying text nodes and property overrides.

**Tool:** `components_update_content`

<Warning>
  This tool is only for updating content in secondary locales. The `localeId` parameter is required, and requests to update primary locale content will fail.
</Warning>

<Card>
  <ParamField path="site_id" type="string" required={true}>
    Unique identifier for the site
  </ParamField>

  <ParamField path="component_id" type="string" required={true}>
    Unique identifier for the component
  </ParamField>

  <ParamField path="localeId" type="string" required={true}>
    Unique identifier for the target locale
  </ParamField>

  <ParamField path="nodes" type="array" required={true}>
    Array of node updates with text content and property overrides
  </ParamField>
</Card>

**Returns:** Updated component content confirmation

***

## Get component properties

Get component properties including default values and configuration for a specific component.

**Tool:** `components_get_properties`

<Card>
  <ParamField path="site_id" type="string" required={true}>
    Unique identifier for the site
  </ParamField>

  <ParamField path="component_id" type="string" required={true}>
    Unique identifier for the component
  </ParamField>

  <ParamField path="localeId" type="string" required={false}>
    Unique identifier for a specific locale
  </ParamField>

  <ParamField path="limit" type="number" required={false}>
    Maximum number of records to return (max: 100)
  </ParamField>

  <ParamField path="offset" type="number" required={false}>
    Offset for pagination
  </ParamField>
</Card>

**Returns**

<EndpointResponseSnippet endpoint="GET /v2/sites/{site_id}/components/{component_id}/properties" />

***

## Update component properties

Update component properties for localization to customize behavior in different languages.

**Tool:** `components_update_properties`

<Card>
  <ParamField path="site_id" type="string" required={true}>
    Unique identifier for the site
  </ParamField>

  <ParamField path="component_id" type="string" required={true}>
    Unique identifier for the component
  </ParamField>

  <ParamField path="localeId" type="string" required={true}>
    Unique identifier for the target locale
  </ParamField>

  <ParamField path="properties" type="object" required={true}>
    Object with property updates
  </ParamField>
</Card>

**Returns:** Updated component properties confirmation
