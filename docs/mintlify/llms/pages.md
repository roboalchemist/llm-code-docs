# Source: https://www.mintlify.com/docs/organize/pages.md

# Source: https://www.mintlify.com/docs/editor/pages.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.mintlify.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Create and edit pages

> Create, edit, and organize documentation pages in the web editor.

## Navigate files

Browse your documentation pages in the **Navigation** tab of the left panel.

* Click navigation elements to expand or collapse them.
* Click pages to open them in the editor.
* Click the search icon or press <kbd>Cmd</kbd> + <kbd>P</kbd> (macOS) or <kbd>Ctrl</kbd> + <kbd>P</kbd> (Windows) to search for files by filename. Search matches exact filenames, so use hyphens between words (for example, `get-agent-job` instead of `get agent job`).

### View unused pages

The **Unused pages** section at the bottom of the **Settings** section of the sidebar shows pages and other files that exist in your repository, but aren't included in your navigation. These are [hidden](/organize/hidden-pages) pages that don't appear on your published site until you add them to navigation.

## Create new pages

1. Click the **+** button in the navigation element where you want to add a page.
2. Click **Add a page**.
3. Enter a filename. The editor adds the `.mdx` extension automatically.

## Add unused pages to navigation

Add pages from the **Unused pages** section to your navigation.

**Drag and drop:**

1. Find the page in the **Unused pages** section.
2. Drag the page to the desired location in your navigation tree.

**In the navigation tree:**

1. Click the plus button, <Icon icon="plus" />, where you want to add the file.
2. Click **Add existing file**.
3. Select the page you want to add.

## Edit content

Switch between visual and Markdown mode with the toggle in the toolbar. The web editor saves your changes when switching modes.

<Frame>
  <img src="https://mintcdn.com/mintlify/DLSr2FhOurD6ae47/images/editor/mode-toggle-light.png?fit=max&auto=format&n=DLSr2FhOurD6ae47&q=85&s=499c9121271dd33043363241461de5c3" alt="Mode toggle in the toolbar." className="block dark:hidden" data-og-width="174" width="174" data-og-height="82" height="82" data-path="images/editor/mode-toggle-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/DLSr2FhOurD6ae47/images/editor/mode-toggle-light.png?w=280&fit=max&auto=format&n=DLSr2FhOurD6ae47&q=85&s=cde92c9d2b09bb939cd0f53d333a98d3 280w, https://mintcdn.com/mintlify/DLSr2FhOurD6ae47/images/editor/mode-toggle-light.png?w=560&fit=max&auto=format&n=DLSr2FhOurD6ae47&q=85&s=2e6cc6f50eab56cda3dfd8a10de95edb 560w, https://mintcdn.com/mintlify/DLSr2FhOurD6ae47/images/editor/mode-toggle-light.png?w=840&fit=max&auto=format&n=DLSr2FhOurD6ae47&q=85&s=d3946323706b3121b448d4ec08a24fd1 840w, https://mintcdn.com/mintlify/DLSr2FhOurD6ae47/images/editor/mode-toggle-light.png?w=1100&fit=max&auto=format&n=DLSr2FhOurD6ae47&q=85&s=76cdfe1c4d2c3618b009549ea31128a3 1100w, https://mintcdn.com/mintlify/DLSr2FhOurD6ae47/images/editor/mode-toggle-light.png?w=1650&fit=max&auto=format&n=DLSr2FhOurD6ae47&q=85&s=4f9d1f1a3e2c44c1f68c7475f878c3e1 1650w, https://mintcdn.com/mintlify/DLSr2FhOurD6ae47/images/editor/mode-toggle-light.png?w=2500&fit=max&auto=format&n=DLSr2FhOurD6ae47&q=85&s=9e6add5fdc7d510597f4e563653218bb 2500w" />

  <img src="https://mintcdn.com/mintlify/SuQEK9bgpZedn8cX/images/editor/mode-toggle-dark.png?fit=max&auto=format&n=SuQEK9bgpZedn8cX&q=85&s=93f0045aa2ba662011376d8f812c8076" alt="Mode toggle in the toolbar." className="hidden dark:block" data-og-width="174" width="174" data-og-height="82" height="82" data-path="images/editor/mode-toggle-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/SuQEK9bgpZedn8cX/images/editor/mode-toggle-dark.png?w=280&fit=max&auto=format&n=SuQEK9bgpZedn8cX&q=85&s=00df6d25393d71b25afee94d5d259913 280w, https://mintcdn.com/mintlify/SuQEK9bgpZedn8cX/images/editor/mode-toggle-dark.png?w=560&fit=max&auto=format&n=SuQEK9bgpZedn8cX&q=85&s=966cb9ab1300b1608a1f8695577301c7 560w, https://mintcdn.com/mintlify/SuQEK9bgpZedn8cX/images/editor/mode-toggle-dark.png?w=840&fit=max&auto=format&n=SuQEK9bgpZedn8cX&q=85&s=efb1a27eb4001147b0348d2947e8dcb1 840w, https://mintcdn.com/mintlify/SuQEK9bgpZedn8cX/images/editor/mode-toggle-dark.png?w=1100&fit=max&auto=format&n=SuQEK9bgpZedn8cX&q=85&s=22104cf4cae821e5d6ae9a07ca9737fd 1100w, https://mintcdn.com/mintlify/SuQEK9bgpZedn8cX/images/editor/mode-toggle-dark.png?w=1650&fit=max&auto=format&n=SuQEK9bgpZedn8cX&q=85&s=2840b2f9ff29006fc072eab374c55312 1650w, https://mintcdn.com/mintlify/SuQEK9bgpZedn8cX/images/editor/mode-toggle-dark.png?w=2500&fit=max&auto=format&n=SuQEK9bgpZedn8cX&q=85&s=c1cd88917407aa8ec94cf76aab260e32 2500w" />
</Frame>

### Visual mode

Edit content with real-time previews that show how the content looks when published.

* **Add text**: Type in the editor to see how the text appears when published.
* **Format text**: Use the toolbar to bold, italicize, or apply other formatting to text.
* **Add components**: Press <kbd>/</kbd> to open the component menu and select components.
* **Add images**: Use the image component from the <kbd>/</kbd> menu.
* **Insert links**: Select text and press <kbd>Cmd</kbd> + <kbd>K</kbd>.

See [Components](/components) for the complete list of available components.

### Markdown mode

Edit the MDX source code.

* **Direct MDX editing**: Write MDX and Markdown syntax for precise control over content.
* **Component properties**: Set component properties and configurations.
* **Frontmatter**: Edit page metadata at the top of the file.

See [Format text](/create/text) and [Format code](/create/code) for more information on MDX syntax.

## Configure pages

Configure page settings to control how pages appear in navigation, search results, and your site layout.

1. Right-click a file.
2. Click **Configure**.

### Customize navigation appearance

Control how the page appears in your site's navigation sidebar.

* **Title**: Set the main heading. Appears in navigation, browser tabs, and search results.
* **Sidebar title**: Display shorter text in navigation when the full title is too long for the sidebar.
* **Icon**: Add a visual marker next to the page to help users identify it quickly.
* **External URL**: Link to an external site instead of a page. Use this to add external resources to your navigation.

### Optimize for search and sharing

Help users find your page and improve how it appears when shared.

* **Description**: Write a brief summary. Appears in search results and SEO meta tags.
* **Keywords**: Add relevant search terms to help users discover this page.
* **OG Image URL**: Set a custom preview image for social media shares and link previews.

### Control page layout

Choose how the page displays to match your content needs.

* **Standard layout** (`default`): Default page with sidebar navigation and table of contents.
* **Full-width layout** (`wide`): Hides table of contents to allow wider layouts for tables, diagrams, or other content.
* **Centered layout** (`center`): Hides sidebar and table of contents for better readability of text-heavy pages like changelogs.
* **Custom width** (`custom`): Minimal layout with only the top navbar for landing pages or other unique layouts.

## Manage pages

### Move pages

Drag and drop pages to reorder them in your navigation or move files between folders in the file tree.

### Duplicate pages

Right-click a page and select **Duplicate**.

### Delete pages

Right-click a page and select **Delete**. Deleting a page removes it from your navigation automatically.

### Hide pages

To remove a page from navigation without deleting the file, right-click the page and click **Hide Page**. The file remains in your repository and you can unhide the page by adding it to your `docs.json` navigation.
