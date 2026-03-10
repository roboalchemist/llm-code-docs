# Source: https://developers.webflow.com/mcp/reference/data/custom-code.mdx

***

title: Custom Code
description: Manage custom scripts and code for your Webflow site
-----------------------------------------------------------------

Manage custom scripts and code for your Webflow site using the Scripts tools. Register scripts, apply them to sites or pages, and manage script configurations.

<Warning>
  Currently, only site-level custom code is supported, and only JavaScript scripts can be applied. Page-level scripts aren't yet supported.
</Warning>

***

## List registered scripts

List all registered scripts for a site. To apply a script to a site or page, first register it via the Register Script endpoints, then apply it using the relevant Site or Page endpoints.

**Tool:** `site_registered_scripts_list`

<Card>
  <ParamField path="site_id" type="string" required={true}>
    Unique identifier for the site
  </ParamField>
</Card>

**Returns**

<EndpointResponseSnippet endpoint="GET /v2/sites/{site_id}/registered_scripts" />

***

## List applied scripts

Get all scripts applied to a site by the App. To apply a script to a site or page, first register it via the Register Script endpoints, then apply it using the relevant Site or Page endpoints.

**Tool:** `site_applied_scripts_list`

<Card>
  <ParamField path="site_id" type="string" required={true}>
    Unique identifier for the site
  </ParamField>
</Card>

**Returns**

<EndpointResponseSnippet endpoint="GET /v2/sites/{site_id}/custom_code" />

***

## Add inline site script

Register an inline script for a site and apply it to a site. Inline scripts are limited to 2000 characters.

**Tool:** `add_inline_site_script`

<Card>
  <ParamField path="site_id" type="string" required={true}>
    Unique identifier for the site
  </ParamField>

  <ParamField path="request" type="object" required={true}>
    Script registration request

    <Accordion title="+ Show 5 properties">
      <ParamField path="sourceCode" type="string" required={true}>
        JavaScript code (max 2000 characters)
      </ParamField>

      <ParamField path="version" type="string" required={true}>
        Script version identifier
      </ParamField>

      <ParamField path="displayName" type="string" required={true}>
        Name for the script
      </ParamField>

      <ParamField path="canCopy" type="boolean" required={false} default="true">
        Whether the script can be copied
      </ParamField>

      <ParamField path="location" type="enum" required={true}>
        Where to apply the script (`header` or `footer`)
      </ParamField>

      <ParamField path="attributes" type="object" required={false}>
        Optional script attributes
      </ParamField>
    </Accordion>
  </ParamField>
</Card>

**Returns**

<EndpointResponseSnippet endpoint="POST /v2/sites/{site_id}/registered_scripts/inline" example="CustomCodeInlineResponse" />

***

## Delete all site scripts

Delete all custom code scripts from a site.

**Tool:** `delete_all_site_scripts`

<Card>
  <ParamField path="site_id" type="string" required={true}>
    Unique identifier for the site
  </ParamField>
</Card>

**Returns**

<EndpointResponseSnippet endpoint="DELETE /v2/sites/{site_id}/custom_code" />

***

## Example workflow

1. List registered scripts to see what's available
2. List applied scripts to see what's currently active
3. Add inline scripts as needed for site functionality
4. Remove scripts when no longer needed

## Best practices

* Keep inline scripts under 2000 characters
* Use descriptive display names for easier management
* Place critical scripts in the header, non-critical in the footer
* Test scripts in a staging environment before applying to production
