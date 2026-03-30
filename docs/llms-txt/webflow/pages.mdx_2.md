# Source: https://developers.webflow.com/mcp/v1.0.0-beta/reference/designer/pages.mdx

***

title: Pages
description: 'Create, organize, and navigate pages in the Webflow Designer.'
----------------------------------------------------------------------------

The Designer Pages tools enable you to create new pages, organize them into folders, and navigate between pages while working in the Designer.

<Warning>
  Designer tools require the MCP Bridge App to be open in the Webflow Designer. Ensure it's connected before using these tools.
</Warning>

## When to use

Use Designer Pages tools to:

* **Create new pages**: Add static or dynamic pages to your site
* **Organize pages**: Create folder structures for better organization
* **Navigate Designer**: Switch between pages programmatically
* **Check context**: Verify which page you're currently editing

## Tool details

**Tool name**: `de_page_tool`

## Available actions

### Create page

Establish a new page in your site.

**Action**: `create_page`

**Parameters**:

| Parameter               | Type   | Required | Description            |
| ----------------------- | ------ | -------- | ---------------------- |
| `siteId`                | string | Yes      | Site identifier        |
| `page_name`             | string | Yes      | Page identifier/name   |
| `meta_title`            | string | Yes      | SEO title for the page |
| `meta_description`      | string | No       | SEO meta description   |
| `page_parent_folder_id` | string | No       | Parent folder location |

**Returns**: Created page details

**Example usage**:

```
Create a new "About Us" page with SEO title "About Our Company"
```

<Note>
  After creating a page, the Designer automatically switches to it. This is different from Data API page creation.
</Note>

### Create page folder

Create an organizational folder for pages.

**Action**: `create_page_folder`

**Parameters**:

| Parameter               | Type   | Required | Description               |
| ----------------------- | ------ | -------- | ------------------------- |
| `siteId`                | string | Yes      | Site identifier           |
| `page_folder_name`      | string | Yes      | Folder name               |
| `page_folder_parent_id` | string | No       | Parent folder for nesting |

**Example usage**:

```
Create a "Blog" folder for blog-related pages
```

<Tip>
  Organize pages into folders by section: Marketing, Products, Legal, Blog, etc.
</Tip>

### Get current page

Retrieve details about the active page in the Designer interface.

**Action**: `get_current_page`

**Parameters**:

| Parameter | Type   | Required | Description     |
| --------- | ------ | -------- | --------------- |
| `siteId`  | string | Yes      | Site identifier |

**Returns**: Current page information including ID, name, and path

**Example usage**:

```
What page am I currently editing?
```

## Best practices

<Accordion title="Use descriptive page names">
  Choose clear, URL-friendly page names:

  * ✅ `about-us`, `contact`, `product-details`
  * ❌ `page1`, `new-page`, `untitled`

  Good names improve organization and SEO.
</Accordion>

<Accordion title="Organize with folders early">
  Create folder structure before adding many pages:

  ```
  /Marketing
    - Homepage
    - About Us
    - Contact
  /Products
    - Product Overview
    - Product Catalog
  /Legal
    - Privacy Policy
    - Terms of Service
  ```

  Early organization prevents future cleanup.
</Accordion>

<Accordion title="Set SEO metadata during creation">
  Always provide meta titles and descriptions when creating pages:

  * Title: 50-60 characters
  * Description: 150-160 characters
  * Include target keywords
  * Make them compelling

  Good SEO starts at page creation.
</Accordion>

<Accordion title="Verify context before editing">
  Use `get_current_page` before making changes to ensure you're editing the correct page. This prevents accidental modifications.
</Accordion>

<Accordion title="Combine Data and Designer Page tools">
  For optimal workflow, use both tool types together:

  * **Designer Page tools**: Create pages and navigate between them in real-time
  * **Data API Page tools**: List all pages, update metadata, manage SEO settings, and handle localization

  This combination gives you the best of both worlds: real-time Designer interaction and comprehensive metadata management.
</Accordion>

## Automatic page switching

**Important behavior**: When you create a page using `create_page`, the Designer automatically switches to the newly created page.

This means:

1. You create a page
2. Designer switches to it automatically
3. Any subsequent element/style operations affect the new page
4. Use `switch_page` to navigate to a different page if needed

## Limitations

* **Auto-switch**: Page creation automatically switches Designer view
* **Designer required**: Must have Bridge App open and connected
* **Page structure**: Cannot modify existing page structure, only create new pages
* **No deletion**: Use Data API or Designer UI to delete pages

## Related tools

<Cards>
  <Card
    title="Data API Pages"
    icon={
    <>
      <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/48px/Blog.svg" alt="" className="dark-icon" />
      <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/48px/Blog.svg" alt="" className="light-icon" />
    </>
  }
    iconSize={12}
    iconPosition="left"
    href="/mcp/v1.0.0-beta/tools/data/pages"
  >
    Manage page metadata and content
  </Card>

  <Card
    title="Elements"
    icon={
    <>
      <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/48px/PageBuilding.svg" alt="" className="dark-icon" />
      <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/48px/PageBuilding.svg" alt="" className="light-icon" />
    </>
  }
    iconSize={12}
    iconPosition="left"
    href="/mcp/v1.0.0-beta/tools/designer/elements"
  >
    Build page content
  </Card>

  <Card
    title="Components"
    icon={
    <>
      <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/48px/Components.svg" alt="" className="dark-icon" />
      <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/48px/Components.svg" alt="" className="light-icon" />
    </>
  }
    iconSize={12}
    iconPosition="left"
    href="/mcp/v1.0.0-beta/tools/designer/components"
  >
    Add reusable components to pages
  </Card>
</Cards>
