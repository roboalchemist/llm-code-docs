# Source: https://docs.curator.interworks.com/site_content_design/user_notifications_and_email/tutorials.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Tutorials 

> Create interactive tutorials and help documentation to guide users through dashboard features and site functionality.

Tutorials can be used to explain how to use a page, embedded visualization, or for any other supporting documentation
related to content on your Curator site.

They can be shown every time a Dashboard is viewed, a fixed number of times the Dashboard is viewed, or only when clicked
on by a user.

***To create a tutorial:***

1. Navigate to the backend of the system (e.g. `http://curatorexample.com/backend`).
2. Log in if prompted.
3. Click on **Content** > **Tutorials** in the left-hand menu. (or in earlier versions **Tableau** > **Tutorials**).
4. Click the "New Tutorial" button.
5. Enter the title, description and content of the tutorial in the appropriate fields. The content field allows for
   fully formatted content, including images, links, etc.
6. Enter the number of times the tutorial should be shown in the "Maximum Views" field.
   * Entering zero in this field means the tutorial will only be shown if the user clicks to see it.
   * Entering -1 in the field means the tutorial will be shown each time the user views the Dashboard until they click
     to not show it again.
7. You can control the size and location of the tutorial on the page by adjusting the pixel value for width, height,
   top position and left position. Leave blank to use the system default.
   * Top position is the number of pixels below the top of the page (0px is at the very top)
   * Left position is the number of pixels from the left of the page (0px is at the very left)
8. A highlighted image can be added by selecting an image from "Highlight Image". Once selected you can control the
   highlighted section by adjusting the pixel value for top position, left position, right position and bottom position.
   * Pixel value determines the size of highlighted area, starting from the top left. For example, if top position is
     10px and bottom position is 100px, the highlighted area will start 10px below the top of the image and end 100px
     below the top.
9. Multiple slides can be created by clicking "Add New Item"
10. Click the "Create" button.

## Setting Tutorials on Individual Content Pages

**Dashboards:**

1. While editing the Dashboard, click on the "Misc" tab.
2. Expand the "Education" section.
3. Select the desired tutorial.
4. Click the "Save" button.

**Pages:**

1. While editing a page, click on the "Misc" tab.
2. Scroll to the "Page Details" section at the bottom of the page.
3. Select the desired tutorial for the **Tutorial** field.
4. Click the "Save" button.

## Setting Tutorials Across Multiple Pages

**Global Tutorials\***(applied across every page of your Curator portal):

1. Navigate to the backend of the system (e.g. `http://curatorexample.com/backend`).
2. Log in if prompted.
3. Click on the **Settings** > **Curator** > **Portal Settings** in the left-hand menu.
4. In the Portal Settings page, click on the "General" tab at the top.
5. Select the desired tutorial in the "Global Tutorial" field under the "Global Settings" section.
6. Click the "Save" button.

\*NOTE: \*\*For versions prior to the **2023.05.31-10** release, "Global tutorials" were not truly global.
To enable a tutorial across all pages for these versions, you will also need to explicitly select a
homepage tutorial (instructions below).

\*NOTE: \*\*For versions prior to the **2023.05.31-10** release to set tutorials across *every single page*
on your Curator site, you will also need to explicitly select a homepage tutorial

**Homepage Tutorials:**

1. Navigate to the backend of the system (e.g. `http://curatorexample.com/backend`).
2. Log in if prompted.
3. Click on the **Settings** > **Curator** > **Portal Settings** in the left-hand menu.
4. In the Portal Settings page, click on the "General" tab at the top.
5. Select the desired tutorial in the "Homepage Tutorial" field under the "Global Settings" section.
6. Click the "Save" button.
