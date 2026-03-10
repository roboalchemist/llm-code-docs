# Source: https://developers.webflow.com/mcp/v1.0.0-beta/reference/data/scripts.mdx

***

title: Scripts
description: >-
Manage custom scripts for Webflow sites including inline JavaScript and
tracking codes.
---------------

The Scripts tool (formerly Custom Code) allows you to register, apply, and manage custom scripts for your Webflow sites. Add inline JavaScript, tracking codes, analytics, or other custom scripts to site headers or footers.

## When to use

Use the Scripts tool to:

* **Add tracking codes**: Implement Google Analytics, Facebook Pixel, or other tracking
* **Custom functionality**: Add JavaScript for custom behaviors or integrations
* **Third-party integrations**: Include scripts from external services

<Warning>
  Currently, only site-level, inline custom code is supported, and only JavaScript scripts can be applied. To apply page-level scripts, use the Custom DOM element and update the tag to `script`.
</Warning>

## Tool details

**Tool name**: `data_scripts_tool`

## Available actions

### List registered scripts

View all scripts registered for a site that are available to be applied.

**Action**: `list_registered_scripts`

**Parameters**:

| Parameter | Type   | Required | Description                    |
| --------- | ------ | -------- | ------------------------------ |
| `site_id` | string | Yes      | Unique identifier for the site |

**Returns**: Array of registered scripts with IDs, names, and metadata

**Example usage**:

```
Show me all registered scripts for site [site_id]
```

### List applied scripts

Retrieve scripts currently applied to a site.

**Action**: `list_applied_scripts`

**Parameters**:

| Parameter | Type   | Required | Description                    |
| --------- | ------ | -------- | ------------------------------ |
| `site_id` | string | Yes      | Unique identifier for the site |

**Returns**: Array of applied scripts with their configuration

**Example usage**:

```
What scripts are currently active on site [site_id]?
```

<Tip>
  Use this to audit which scripts are running on your site before adding new ones.
</Tip>

### Add inline site script

Register and apply a new inline script to a site.

**Action**: `add_inline_site_script`

**Parameters**:

| Parameter     | Type    | Required | Description                                               |
| ------------- | ------- | -------- | --------------------------------------------------------- |
| `site_id`     | string  | Yes      | Unique identifier for the site                            |
| `sourceCode`  | string  | Yes      | JavaScript code (max 2000 characters)                     |
| `version`     | string  | Yes      | Version identifier for the script                         |
| `displayName` | string  | Yes      | Human-readable name for the script                        |
| `location`    | string  | No       | Where to place the script: `header` or `footer` (default) |
| `canCopy`     | boolean | No       | Whether the script can be copied                          |
| `attributes`  | object  | No       | Custom attributes for the script tag                      |

**Example usage**:

```
Add Google Analytics tracking to site [site_id] in the header
```

<Warning>
  Scripts are limited to 2000 characters. For longer scripts, host them externally and use a script tag to include them.
</Warning>

### Delete all site scripts

Remove all custom scripts applied to a site by the MCP server.

**Action**: `delete_all_site_scripts`

**Parameters**:

| Parameter | Type   | Required | Description                    |
| --------- | ------ | -------- | ------------------------------ |
| `site_id` | string | Yes      | Unique identifier for the site |

**Returns**: Confirmation of deletion

**Example usage**:

```
Remove all custom scripts from site [site_id]
```

<Warning>
  This action removes ALL scripts applied through the MCP server. This operation cannot be undone.
</Warning>

## Best practices

<Accordion title="Place scripts appropriately">
  **Header scripts** (`location: "header"`):

  * Critical JavaScript that must load before page content
  * Fonts or CSS dependencies
  * Scripts that modify the DOM before rendering

  **Footer scripts** (`location: "footer"`, default):

  * Analytics and tracking codes
  * Non-critical JavaScript
  * Third-party widgets
  * Social media scripts

  Footer placement is generally preferred for better page load performance.
</Accordion>

<Accordion title="Minify large scripts">
  Minify your JavaScript to reduce character count and fit within the 2000 character limit. For larger scripts:

  * Host externally and include via script tag
  * Split into multiple smaller scripts
  * Load from a CDN
</Accordion>

<Accordion title="Version your scripts">
  Use meaningful version identifiers to track script changes:

  * `v1.0.0` - Initial version
  * `v1.1.0` - Added features
  * `v2.0.0` - Major changes

  This helps with troubleshooting and rollbacks.
</Accordion>

<Accordion title="Test before publishing">
  After adding scripts, test your site thoroughly before publishing:

  * Check browser console for errors
  * Verify tracking codes are firing
  * Test on multiple browsers and devices
  * Ensure scripts don't interfere with site functionality
</Accordion>

<Accordion title="Document script purposes">
  Use descriptive `displayName` values that clearly indicate what each script does:

  * "Google Analytics 4 Tracking"
  * "Facebook Pixel - Purchase Events"
  * "Custom Form Validation"
  * "Hotjar Heatmap Tracking"
</Accordion>

## Limitations

* **Character limit**: Scripts are limited to 2000 characters
* **Inline only**: Can only add inline scripts, not external file references. To add external scripts, use script tags in the Designer.
* **MCP-managed only**: `delete_all_site_scripts` only removes scripts added through the MCP server
* **Publishing required**: Scripts must be published to appear on the live site
* **No execution in MCP**: Scripts are registered but not executed by the MCP server itself

## Security considerations

<Warning>
  **Important security notes:**

  * Only add scripts from trusted sources
  * Never include sensitive data (API keys, passwords) in scripts
  * Validate and sanitize any user input used in scripts
  * Be cautious with third-party scripts that can access site data
  * Regularly audit and update scripts to patch security vulnerabilities
</Warning>

## Related tools

<Cards>
  <Card
    title="Sites"
    icon={
    <>
      <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/48px/Globe.svg" alt="" className="dark-icon" />
      <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/48px/Globe.svg" alt="" className="light-icon" />
    </>
  }
    iconSize={12}
    iconPosition="left"
    href="/mcp/v1.0.0-beta/tools/data/sites"
  >
    Publish sites to make script changes live
  </Card>

  <Card
    title="Pages"
    icon={
    <>
      <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/48px/Page.svg" alt="" className="dark-icon" />
      <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/48px/Page.svg" alt="" className="light-icon" />
    </>
  }
    iconSize={12}
    iconPosition="left"
    href="/mcp/v1.0.0-beta/tools/data/pages"
  >
    Manage page-specific content
  </Card>

  <Card
    title="Elements"
    icon={
    <>
      <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/48px/Elements.svg" alt="" className="dark-icon" />
      <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/48px/Elements.svg" alt="" className="light-icon" />
    </>
  }
    iconSize={12}
    iconPosition="left"
    href="/mcp/v1.0.0-beta/tools/designer/elements"
  >
    Add HTML embed elements for more complex code
  </Card>
</Cards>
