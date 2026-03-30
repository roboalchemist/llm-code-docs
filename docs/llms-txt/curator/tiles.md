# Source: https://docs.curator.interworks.com/site_content_design/pages/tiles.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Tiles

> Create visual tile layouts to organize and link content from multiple source systems with automatic permission handling.

Creating a central location to link all of the content users have access to is a breeze with Curator's tiles feature.
You can bring in content that pulls across different source-systems, from Curator's page system, as well as adding in
your own custom links to send users to other useful websites.

NOTE: All tiles, unless specifically overridden, will respect the permissions of what the user has access to.
If there are any group restrictions on menu items, those will be taken into account.
Second, it will check the source-system permission (e.g. Tableau, Power BI, etc.).
Then finally will look at the individual item's permission (e.g.
[Restrict Access](/site_content_design/menus/restrict_access) on a file).

## Tile Types

You can quickly add tiles into your page in a few clicks.  To give you more insight into what each of these tiles allow
you to display for your users, we've provided a brief description of each section below:

**Dashboards**
Dashboard Tiles allow you to link to analytic content that you have brought into Curator.  This links from any source-system,
be it Tableau, Power BI, or ThoughtSpot - anything that Curator supports natively!  This runs through a permissions check
to make sure the user has access, and can be sorted to your preference.  The default sorting after your preference will
be to place user-favorited dashboards first, then order them by visit, and finally by alphabetical order.

**Pages**
Page Tiles allow you to link to other pages you have created on Curator.  You may want to embed a "contact us" page,
create a feedback form, link to other detail pages, or maybe even use our explorer feature to allow users to browse
through all the content they can see.  Whatever you want to create within Curator, Page Tiles can specifically link to
that content.

**Menus**
Menu Tiles repeat the same-level menu items as the menu you've linked to.  So if you want to display all the top-level
menu items someone has access to, you can add in a link to your highest menu item, and it will display all the links
one level below the link you've selected.  It's an easy way to allow people a more visual exploration while still
maintaining the guardrails of your neatly maintained menu system.

**Keyword Pages**
Keyword Page Tiles pull in content of any sort so long as it has been associated with a specific keyword on Curator.
Linking this content together allows you to logically group things at a topic level that may not make sense to be grouped
in other ways.  It unifies areas that cut across your site in a categorically succinct manner.

**External URL**
External URLs can be created in the Navigation section, and allow you to link to other websites.

**Media**
Media brings in any content that has been uploaded to Curator's Files system.  This allows you to link to specific files
(e.g. PDFs) that are hosted on Curator. Files can have security applied directly to them without needing to be added to
the menu.

**External (RSS) Feeds**
Allows you to bring in external and RSS feeds as tiles, that serve as links to the host page.

**Custom Mix**
For when you want bring in anything and everything someone has access to.  This combines all the tile types listed here
and displays content based on the criteria you've chosen.

**Managed Instances (Enterprise Only)**
If your users have access to multiple Curator sites that you've deployed through Central Dispatch, this tile-type will
allow them to view all the different Curator sites they have access to.

## Tile Style

**Tile Style** can be selected on the Page Styles menu when tiles are selected in the Page Builder. The tile style
selection includes shapes in Square, Small Horizontal, Boxy, Circle, and Hex.

Tile styles in Page Builder is independent of the Global tile styles in Portal Settings. You are able to have different
tile styles for different Pages, but the same Dashboards have to have the same tile style.

## Tile Thumbnails

**Tableau Dashboards** can generate thumbnails automatically and they will be updated regularly if you want them to.
Yet, this might display data that you do not want to show on a thumbnail. To show a generic thumbnail for this Dashboard:

1. Navigate to the backend of the system (e.g. `http://curatorexample.com/backend`).
2. Navigate to the Tableau > Dashboards section from the left-hand menu.
3. Click on the Dashboard you want to change the thumbnail for.
4. Open the Misc tab and expand the Look/ Feel section.
5. Delete the auto-generated thumbnail.
6. Use the Upload button to upload your custom thumbnail.
7. Click Save.

**Pages**' thumbnails default to the global default thumbnail unless you set one on the Page itself:

1. Navigate to the backend of the system (e.g. `http://curatorexample.com/backend`).
2. Navigate to the Content > Pages section from the left-hand menu.
3. Click on the page you want to change the thumbnail for.
4. Scroll down, under the Preview window.
5. Use the Upload button for the Thumbnail Image to upload your custom thumbnail.
6. Click Save.

**Files & Keywords**' thumbnails default to the global default thumbnail unless you set one on the Page itself:

1. Navigate to the backend of the system (e.g. `http://curatorexample.com/backend`).
2. Navigate to the Content > Files or Keywords section from the left-hand menu.
3. Click on the file or keyword you want to change the thumbnail for.
4. Use the Upload button for the Thumbnail Image to upload your custom thumbnail.
5. Click Save.

Most of the **Navigation** items can have an icon associated with them. If there is no additional explicit option to
upload a thumbnail for it, the default thumbnail will be the icon. To set the icon or thumbnail for a navigation item:

1. Navigate to the backend of the system (e.g. `http://curatorexample.com/backend`).
2. Navigate to the Content > Reorder Navigation section from the left-hand menu.
3. Click on the pen icon (edit button) of the navigation item you want to change the icon or thumbnail for.
4. Use the Upload button for the Icon or if existent the Thumbnail Image to upload your custom icon/ thumbnail.
5. Click Save.

If you want to customize the **default thumbnail** to show for any content type that does not have a thumbnail set:

1. Navigate to the backend of the system (e.g. `http://curatorexample.com/backend`).
2. Navigate to the Settings > Curator > Themes section from the left-hand menu.
3. Click on the Pages tab in the middle of the screen.
4. In the new left-hand-side menu, Pages Options, expand the Tile Styles section.
5. Use the Upload button for the Custom Default Thumbnail to upload your default thumbnail.
6. Click Save.

   ***2024.02-02 Default Thumbnail update***

   The default tile was updated in the 2024.02-03 release to a more modern design.  If you wish to re-upload the old file,
   you can right click the file link to save this image: [Old Default Thumbnail](/assets/images/site_content_design/pages/old_default_thumbnail_file.png).
