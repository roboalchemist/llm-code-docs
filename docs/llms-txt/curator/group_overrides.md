# Source: https://docs.curator.interworks.com/site_content_design/theme/group_overrides.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Group Overrides

> Apply group-specific theme customizations and styling overrides to provide tailored experiences for different user groups.

When using Curator, you may want to surface different content to different users.  You can achieve this using Curator's
Group Overrides.  Whether you want to show a homepage to a certain subset of users or you want to change the colors and
logos for a specific client, you can use groups (synced from Tableau or your SAML provider) to modify the look and feel
of your Curator site. For additional info, view our
[Group Overrides blog post](https://interworks.com/blog/morr/2018/04/09/portals-tableau-new-feature-spotlight-overriding-settings-tableau-group/).

## To Create a new Group Override

1. Login to the backend of your Curator instance (e.g. `http://curatorexample.com/backend`).
2. Navigate to the **Settings** > **Users** > **Frontend Group Overrides** section from the left-hand menu.
3. Click the 'New Group Override' button at the top.
4. From the Frontend Group list, select the group you would like these settings to apply to.
5. Give the group override a title, if a user has access to multiple groups, this will be the title that is displayed
   that allows them to switch between group overrides\*.
6. Modify the settings you wish to override for this group using the tabbed form fields at the bottom of the page, and
   once you're done, click Save.

## Using the Theme-switcher

If you are logged in to the front-end of Curator and your user is a member of multiple groups, by default you will see
a dropdown in your menu that allows you to view either the "Default" setting\*, or individual Themes.  The experience
when selecting these themes will depend on whether or not "Use Global Theme for Defaults" has been enabled for the theme.

\***Group Override Inheritance - Use Global Theme for Defaults Enabled**
When "Use Global Theme for Defaults" is enabled, and your use is a member of multiple groups, they will see all settings
that have been saved inside of Themes across those groups.

For example, if there are two groups:

* Group 1 - Green menu, default/no bg color
* Group 2 - Default/no bg menu color, black background

"Default" would show you a Green menu and black background, whereas selecting Group 1, you will see a Green menu and the
remainder of settings will show the default settings, and the same goes for Group 2 where you will see a default menu
color but the background of the site will be black.

\***Group Override Inheritance - Use Global Theme for Defaults Disabled**
If you create a  group override with the Global Theme Default disabled, this group override will remain distinct and
separate from the inheritance flow, only allowing you to see this if:

1. You are a member of that group and *only* that group.
2. You are a member of multiple groups, and have chosen that group from the Theme-switcher dropdown on the front-end of Curator.

## Disabling Group Switching

By default, users who have access to multiple group overrides will be allowed to cycle through the group overrides they
belong to.  Group Overrides are inherited by creation-date, with the oldest group-override taking the highest priority.
If you do not want to give users access to changing this to view distinct Themes on a per-group basis you can disable
that dropdown using the steps below:

1. Login to the backend of your Curator instance (e.g. `http://curatorexample.com/backend`).
2. Navigate to the **Settings** > **Curator** > **Portal Settings** section from the left-hand menu.
3. Click on the 'Features' tab and expand the 'Usability' section at the bottom of the page.
4. Toggle **Group Override Selector** to the off position.
5. Save your settings.
