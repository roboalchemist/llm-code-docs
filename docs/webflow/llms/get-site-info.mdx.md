# Source: https://developers.webflow.com/designer/reference/get-site-info.mdx

***

title: Get site information
slug: designer/reference/get-site-info
description: ''
hidden: false
'og:title': 'Webflow Designer API: Get site information'
'og:description': Get metadata about the current site.
------------------------------------------------------

## `webflow.getSiteInfo()`

Get metadata about the current site.

### Syntax

```typescript
webflow.getSiteInfo(): Promise<{
    siteId: string;
    siteName: string;
    shortName: string;
    isPasswordProtected: boolean;
    isPrivateStaging: boolean;
    workspaceId: string;
    workspaceSlug: string;
    domains: Array<{
        url: string;
        lastPublished: string | null;
        default: boolean;
        stage: "staging" | "production";
    }>;
}>
```

### Returns

A Promise that resolves to a record containing information about the site that's currently open in the Designer. The record has the following properties:

| Property              | Type                                                                                                        | Description                                                                                    |
| --------------------- | ----------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `siteId`              | *string*                                                                                                    | The unique ID of the current Webflow site.                                                     |
| `siteName`            | *string*                                                                                                    | The name of the current Webflow site.                                                          |
| `shortName`           | *string*                                                                                                    | The short name of the current Webflow site.                                                    |
| `isPasswordProtected` | *boolean*                                                                                                   | Whether the current site is password protected.                                                |
| `isPrivateStaging`    | *boolean*                                                                                                   | Whether the current site is private staging.                                                   |
| `domains`             | *Array`<{url: string, lastPublished: string \| null, default: boolean, stage: "staging" \| "production"}>`* | An array of objects containing information about the domains associated with the current site. |
| `workspaceId`         | *string*                                                                                                    | The unique ID of the workspace that the current site belongs to.                               |
| `workspaceSlug`       | *string*                                                                                                    | The unique slug of the workspace that the current site belongs to.                             |

### Example

```typescript
const siteInfo = await webflow.getSiteInfo();

console.log("Site ID:", siteInfo.siteId);
console.log("Site Name:", siteInfo.siteName);
console.log("Short Name:", siteInfo.shortName);
console.log("Is Password Protected:", siteInfo.isPasswordProtected);
console.log("Is Private Staging:", siteInfo.isPrivateStaging);
console.log("Domains:", siteInfo.domains);
console.log("Workspace ID:", siteInfo.workspaceId);
console.log("Workspace Slug:", siteInfo.workspaceSlug);
```

<div>
  <a href="https://webflow.com/oauth/authorize?response_type=code&client_id=19511de1ec410f9228d8dcbc9420e67916dea80d86d18f0c9a533eb475ea0f62">
    Try this example
  </a>
</div>
