# Source: https://docs.curator.interworks.com/site_content_design/user_notifications_and_email/error_pages.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Error Pages 

> Configure custom error pages to provide helpful messaging when users encounter access issues or broken links.

When things go wrong, you want to be sure to send the right messages to your audience.  By default, Curator has error
pages that will let users know when they don't have access, they visit a broken link, or a system is down.
Communicating exactly what you'd like in these situations can be made even easier by sending your users to a custom-made
error page.

**NOTE**: You must [create a page](/site_content_design/pages/pages_overview)
first before setting it to your error page

## Setting up "Not Found" or "Access Denied" Pages

1. Login to the backend of your Curator instance (e.g. `http://curatorexample.com/backend`).

2. Navigate to the **Settings** > **Curator** > **Portal Settings** section from the left-hand menu.

3. Click on the "General" tab and expand the "Error Pages" section.

4. Using the dropdown, select a page from the list of pages you have created on Curator. You can set two pages here:

   * Access Denied (403) - Displays when a user does not have access to a specific link on Curator.
   * Not Found (404) - Displays when a user visits a link that does not exist on Curator, or visits an old deleted/moved link.

5. After making your selection from these dropdowns, save the Settings page.

## Setting up "Tableau Server Down" (503 error) Page

Occasionally your Tableau Server may go down for maintenance reasons, or even unplanned issues.  In this case it's
helpful to tell your users that things will be back shortly, and redirect them to useful resources.
Follow the steps below to ensure your custom page displays when your Tableau Server is unavailable.

1. Login to the backend of your Curator instance (e.g. `http://curatorexample.com/backend`).
2. Navigate to the **Settings** > **Tableau** > **Tableau Server Settings** section from the left-hand menu.
3. From the "General" tab expand the "Errors" section.
4. Using the "Tableau 503 Error Page" dropdown, select a page from the list of pages you have created on Curator.
5. After making your selection from this dropdown, save the Settings page.
