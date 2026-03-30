# Source: https://docs.curator.interworks.com/site_content_design/theme/curator_styles.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Curator Styles

> Customize the visual appearance of your Curator portal with built-in styling options and theme configurations.

Curator allows controls related to your site design across all content types, however having a central place to modify
styles that will impact every page your user visits allows you to create a standard and consistent brand.  The live
preview makes this even easier, allowing you to change the configuration of options in the Curator Styles section while
previewing those changes (across device sizes too).  It's best to look through all of the options, and toggle each
selection on or off.  Deleting any content that is input into a text box will revert it back to the default setting.
Feel free to play around and revisit your design as much as you'd like!

## Creating a new Theme

1. Login to the backend of your Curator instance (e.g. `http://curatorexample.com/backend`).
2. Navigate to:
   * **Settings** > **Curator** > **Theme** section from the left-hand menu. Select the Theme you'd like to update.
   * *Pre 2022-11-30:* **Settings** > **Curator** > **Portal Settings** section from the left-hand menu.
3. Click through each tab, expand the sections on the left-hand navigation to see more advanced styling options.
   Changing the the selections will update the live preview on the screen and will show the pending changes.
4. Once you have configured your theme the way you would like, click "Save" to apply your changes to this Theme.

## Applying a Theme to your Site

This feature is only available for Curator instances running 2022-11-30 and above.

1. Login to the backend of your Curator instance (e.g. `http://curatorexample.com/backend`).
2. Navigate to **Settings** > **Curator** > **Portal Settings** section from the left-hand menu.
3. On the "General" tab, use the "Global Theme" dropdown to change the theme applied to your Curator site.  If you would
   like to apply your Theme to a specific group of users, see the
   [Group Override instructions](/site_content_design/theme/group_overrides).
4. Click "Save" to apply your changes.

## Defaults when Using Multiple Themes

Every new theme leverages out-of-the-box defaults for each field if they're left unchanged. These defaults will also be
leveraged if the field is blank, no color is selected, or the "Default" option is selected depending on if it's a text
input, color picker, or dropdown, respectively. You also have the option to have a theme default to the values chosen
in your Global Theme (which is chosen in **Settings** > **Curator** > **Portal Settings**). This is particularly useful
if you have [Group Overrides](/site_content_design/theme/group_overrides) that
need to use themes that look exactly like the Global Theme with just a few minor changes. To enable this you can switch
on **Use Global Theme for Defaults** in any theme that isn't the Global Theme.
