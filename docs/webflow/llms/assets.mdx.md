# Source: https://developers.webflow.com/mcp/reference/designer/assets.mdx

***

title: Assets
description: Manage assets and folders in the Webflow Designer asset manager
----------------------------------------------------------------------------

Manage assets and folders in the Webflow Designer asset manager using the Assets tools. Organize files, update asset metadata, and retrieve asset information.

<Warning>
  The MCP Companion App must be open in the Webflow Designer for these tools to function.
</Warning>

***

## Asset tool

Perform actions like creating folders, getting assets, and updating asset metadata.

**Tool:** `asset_tool`

<Card>
  <ParamField path="siteId" type="string" required={true}>
    Unique identifier for the site.
  </ParamField>

  <ParamField path="actions" type="array" required={true}>
    An array of asset actions to perform. See action examples below.
  </ParamField>
</Card>

### Actions

### Create folder

Create a new folder in the asset manager.

<Card>
  <ParamField path="name" type="string" required={true}>
    The name of the folder to create.
  </ParamField>

  <ParamField path="parent_folder_id" type="string" required={false}>
    The ID of a parent folder to create the new folder inside. If omitted, the folder is created in the root directory.
  </ParamField>
</Card>

<CodeGroup>
  ```json title="Action Example"
  {
    "actions": [
      {
        "create_folder": {
          "name": "Marketing Images"
        }
      }
    ]
  }
  ```
</CodeGroup>

### Get all assets and folders

Retrieve a list of assets and/or folders.

<Card>
  <ParamField path="query" type="'all' | 'folders' | 'assets'" required={true}>
    Specify what to retrieve.
  </ParamField>

  <ParamField path="filter_assets_by_ids" type="array" required={false}>
    An array of asset IDs to filter by.
  </ParamField>
</Card>

<CodeGroup>
  ```json title="Action Example"
  {
    "actions": [
      {
        "get_all_assets_and_folders": {
          "query": "assets"
        }
      }
    ]
  }
  ```
</CodeGroup>

### Update asset

Update an asset's metadata, such as its name, alt text, or parent folder.

<Card>
  <ParamField path="asset_id" type="string" required={true}>
    The ID of the asset to update.
  </ParamField>

  <ParamField path="name" type="string" required={false}>
    The new name for the asset.
  </ParamField>

  <ParamField path="alt_text" type="string" required={false}>
    The new alt text for the asset.
  </ParamField>

  <ParamField path="parent_folder_id" type="string" required={false}>
    The ID of the folder to move the asset to.
  </ParamField>
</Card>

<CodeGroup>
  ```json title="Action Example"
  {
    "actions": [
      {
        "update_asset": {
          "asset_id": "628f4b034872242526c8f65c",
          "alt_text": "A beautiful landscape"
        }
      }
    ]
  }
  ```
</CodeGroup>

***

## Get image preview

Fetch an image from a URL and return it as a base64-encoded string.

<Card>
  <ParamField path="url" type="string" required={true}>
    The URL of the image to fetch.
  </ParamField>

  <ParamField path="siteId" type="string" required={true}>
    Unique identifier for the site.
  </ParamField>
</Card>

<Note>
  This tool helps analyze uploaded assets in your Webflow project, enabling the LLM to generate ALT text or perform other related tasks. Supported image formats include JPG, PNG, WEBP, and AVIF.
</Note>
