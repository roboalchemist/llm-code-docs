# Source: https://docs.curator.interworks.com/site_content_design/menus/menu_items.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Menu Items

> Configure individual menu items including links, labels, icons, and access permissions for effective site navigation.

***To Create a Navigation menu item:***

1. Navigate to the backend of the system (e.g. `http://curatorexample.com/backend`).
2. Navigate to the *Content* > *Navigation* section from the left-hand menu.
3. Expand/collapse the navigation using the carets to find the menu you would like to edit - or click "New Menu Link" to
   create a new item.
4. From the Create New / Update Link page, you can create/modify your new menu item as you'd like.
5. Once your menu items have been created, visit the Reorder page by navigating to the *Content* > *Reorder Navigation*
   section from the left-hand menu.
6. Click and hold the dots ⠀ to drag/drop your menu items and reorder them as you'd like

***To Bulk Create Tableau Dashboards as Menu Items:***

1. Navigate to *Tableau > Dashboards* on the backend
2. Select the Dashboards you would like to create as menu items
3. Click Create Menu Items button

***To Bulk Create Power BI Dashboards as Menu Items:***

1. Navigate to *Power BI > Dashboards* on the backend
2. Select the Dashboards you would like to create as menu items
3. Click Create Menu Items button

***To Bulk Create Power BI Reports as Menu Items:***

1. Navigate to *Power BI > Reports* on the backend
2. Select the Reports you would like to create as menu items
3. Click Create Menu Items button

***Link Types:***

**Dashboard**
The Dashboard type is used to link to existing dashboards.  See the [Embedded Tableau Server Views](/embedding_using_analytics/tableau_dashboards/adding_a_dashboard)
section for more information.

**Data Manager**
The data manager type is used to link to a front-end enabled data manager page. See the [Data Manager](/embedding_using_analytics/data_manager/data_manager_basics)
section for more information.

**Dropdown Placeholder**
The dropdown placeholder type is used to create a grouping or level in the multilevel navigation. Doesn't contain a link
and only displays text.

**File**
The file type links to a file that has been uploaded to the site. See the [File](/site_content_design/files/files)
section for more information.

**Keyword**
The keyword type is used to create a link to a listing of content tagged with a specified keyword.

**Menu Page**
The menu page type allows you to enter the name of a menu item. The menu link will then take you to a page that displays
all of the dashboards directly under (one menu level) the specified menu item. Similar to a keyword page.

**Project**
The project type is used to mark the spot within the navigation where Dashboards will be synced to from the chosen Project.
These Dashboards will be created and configurable in the Dashboards area of the Backend. Note that the project link will
place all Dashboards as siblings to itself. More info on this can be found [here](https://interworks.com/blog/morr/2017/11/22/automatically-sync-your-dashboards-portals-tableau/).

**Projects**
The projects type will automatically find all the available Workbooks from the specified Site for the logged in user and
places links to view them within Curator in the navigation, organized beneath dropdown placeholders named after the Project
they came from. This will not add Dashboards to the Curator backend as opposed to the project type. Note: if the user has
access to many Workbooks (Site Admin or Server Admin) this will generate many links.

**Page**
The page type is used to link to a static page.  See the [Pages](/site_content_design/pages/pages_overview)
section for more information.

**Tag**
The tag type is used to automatically create links to any Tableau Server workbooks which have been tagged with a specific
name. See the [Tagged Workbooks](/site_content_design/menus/tagged_workbooks)
section for more information.

**Web Edit**
The web edit type is used to create a link to the Tableau Server web editor for a specified Dashboard.

**Workbook**
The workbook link type imports in all of the dashboards from a workbook as menu items. It will also automatically pull in
future dashboards added to the workbook.

**Workbooks**
The workbooks link type imports in all of the dashboards from all workbooks in a project as menu items. It will also automatically
pull in future dashboards added to the project.

**Custom URL**
This link type is used to create a link to a custom URL. Extra options are provided to customize this like opening the link
in a new tab or the same tab.

**External URL**
This link type is used to create a link to an external URL. This is a slimmed-down version of the Custom URL.

*NOTE: If you are adding a link that is external to your Curator instance, ensure that you prepend the proper protocol to
your URL. For example, to add InterWorks.com use `http://www.interworks.com`, or `https://www.interworks.com`.*
