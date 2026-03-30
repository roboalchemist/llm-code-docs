# Source: https://docs.curator.interworks.com/site_content_design/pages/pages_overview.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Pages Overview 

> Introduction to creating and managing custom pages within Curator using the page builder for flexible content organization and presentation.

When adding content from your analytics environments, Curator will automatically create default template pages for you.
These can be accessed via the edit page of those individual pieces of content.

However, you may want to create something more tailored for your users to showcase certain content.  In this case, using
Curator's page builder allows a huge amount of flexibility for creating and styling your pages, while still allowing you
to link to content that is both secured to the user viewing the page as well as relevant based on their recent browsing activity.

## Building Pages in Curator

### To create a page in Curator

1. Navigate to the backend of the system (e.g. `http://curatorexample.com/backend`).
2. Navigate to the **Content** > **Pages** section from the left-hand menu.
3. Click "New Page" to create a new page.

### To add content to your page

1. Hover over the element on the page-preview on the right-hand side of the page builder and click the "edit" icon
2. Choose the content you'd like to add to your page

## To style content to your page

1. Click on an item on the page-preview on the right-hand side of the page builder.
2. This will expand a side-panel over the menu on the left-hand side of the page that will give you styling controls
   related to the active content.

## Page Security

Pages will first inherit any [Restrict Access](/site_content_design/menus/restrict_access)
permission that have been set on the individual menu item.  Continuing from there, the permissions will apply according
to the sections below.

Page security for embedded-content was added in the 2024.03-02 release, all prior releases have no security applied
when loading embedded content for pages.  The following section only applies to 2024.03-02 and later.  Proceed to the
**Security for Pages Without Embedded Content** section if you are on an earlier version.

### Security for Pages With Embedded Content

When embedding analytic-content into pages, for example a Dashboard, Curator will check permissions on that embedded
piece of content.  If the user does not have access to the embedded content it will deny them access, routing them to
the
[Access Denied page](/site_content_design/user_notifications_and_email/error_pages).

This applies to both menu items as well as loading the page directly.

#### Disabling Embedded Content Security

To disable the security check in versions released after 2024.03-02:

1. Navigate to the backend of the system (e.g. `http://curatorexample.com/backend`).
2. Click on **Settings** > **Curator** > **Portal Settings** in the left-hand menu.
3. On the **General** tab, scroll down to the **Security** section and expand it.
4. Toggle the switch **Disable Page Element Security Checks** to ON and click the "Save" button.

### Security for Pages Without Embedded Content

Content that is *linked* on a page, for example Tiles, will run through permissions checks while loading the page.
check when rendering the tiles.  So if a page contains a *Tile* that links to a Dashboard that a user does not have
access to the user will simply not see the tile.  However, for pages that have content *embedded* in them, see the
**Security for Pages With Embedded Content** section above.
