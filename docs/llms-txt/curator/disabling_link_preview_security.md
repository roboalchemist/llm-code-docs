# Source: https://docs.curator.interworks.com/users_groups/user_security/disabling_link_preview_security.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Disabling Link-preview Security 

> Disable link preview security features when needed for specific use cases or legacy browser compatibility.

Curator will automatically check with the source system (e.g. Tableau) when a user logs in to determine their
access to linked content from those systems.  However, you can bypass this initial check and expose links to
all content to your users while still surfacing an
[Access Denied/403 page](/site_content_design/user_notifications_and_email/error_pages)
to prevent them from accessing content.

## Disabling link preview security

In order to disable security-checks on all content a user could see in the menu navigation system, or via a
tile/preview thumbnail:

1. Navigate to the backend of the system (e.g. `http://curatorexample.com/backend`).
2. Navigate to the **Settings** > **Tableau** > **Tableau Server Settings** section from the left-hand menu.
3. Click on the "Advanced" tab at the top of the page.
4. Enable the **Skip checking menu item's Dashboard permissions** and save your settings.
5. If you would like to set up a custom "access denied" page follow the instructions on the [Error Pages document](/site_content_design/user_notifications_and_email/error_pages).
