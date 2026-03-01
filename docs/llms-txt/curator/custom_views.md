# Source: https://docs.curator.interworks.com/embedding_using_analytics/tableau_dashboards/custom_views.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Custom Views

> Configure and enable custom views functionality to allow users to save and reload dashboard states with applied filters and parameters.

Curator can allow users to save a Custom View of a Dashboard, which will include any applied filters and parameters, and
then load it again at a later date.

## Enable Custom Views

1. Navigate to the backend of the system (e.g. `http://curatorexample.com/backend`).
2. Log in if prompted.
3. Click on the **Settings** > **Curator** > **Portal Settings** in the left-hand side navigation.
4. Click on the "Features" tab at the top of the main page content.
5. Click to switch on the "Custom Views" setting under the "Toolbar Buttons (Tableau Actions)" section and click the
   "Save" button.

## Enable create/load a Custom View

1. Navigate to the frontend of the system (e.g. `http://curatorexample.com`).
2. Log in if prompted.
3. Navigate to the desired Dashboard by using the navigation menu.
4. Modify the filters, etc. as desired on the Dashboard.
5. Click on the Custom Views icon at the top right portion of the screen. Normally this is displayed on the right side
   of the title bar in the Dashboard.
6. Enter a name for the new Custom View in the text box and click the "Create" button.
7. To load a different Custom View, select an existing view from the drop-down and click on the "Apply" button.

## Sharing Direct Links to Custom Views

Custom Views can be shared via direct URL links, allowing users to access specific Custom Views without manually
selecting them from the dropdown. This functionality works similar to Tableau's native Custom View sharing capabilities.

### How to share a Custom View via direct link

1. **Apply the desired Custom View** using the steps above (steps 1-7).
2. **Copy the current URL** from your browser's address bar. The URL will automatically include the Custom View parameter.
3. **Share the URL** with other users who have access to the Dashboard.

### URL Parameter Format

Custom Views are accessed through the `curator_custom_view` URL parameter (or the legacy `::custom_view` parameter for
backward compatibility). For example:

```txt  theme={null}
http://curatorexample.com/dashboard-name?curator_custom_view=MyCustomViewName
```

When a Custom View is loaded, Curator automatically adds a Custom View ID parameter (`cvi`) to the URL:

```txt  theme={null}
http://curatorexample.com/dashboard-name?curator_custom_view=MyCustomViewName&cvi=abc123def456
```

The `cvi` (Custom View ID) URL parameter contains Tableau's unique identifier (LUID) for the Custom View, which ensures the
correct view is loaded even if multiple Custom Views share the same name. This parameter gets automatically added to the
URL for troubleshooting purposes by Curator. If no Custom View ID is provided via URL load, the first Custom View by
match on name is selected and its ID is added as the cvi parameter.

If a URL contains both the Custom View name and ID parameters, the `cvi` parameter takes precedence to ensure
the exact Custom View is loaded. This means you can safely share URLs that include both parameters without
worrying about ambiguity.

#### Legacy URL Format

For backward compatibility, the legacy `::custom_view` parameter is still supported:

```txt  theme={null}
http://curatorexample.com/dashboard-name?::custom_view=MyCustomViewName
```

However, new Custom View links will use the modern `curator_custom_view` parameter format.

### Sharing Private Custom Views

Private Custom Views are only visible in the dropdown for the user who created them. However, similar to
[sharing a Custom View in Tableau](https://help.tableau.com/current/pro/desktop/en-us/customview.htm#share-a-custom-view)
anyone with access to the Dashboard can see a Custom View using the direct link [outlined above](#how-to-share-a-custom-view-via-direct-link).
