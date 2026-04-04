# Source: https://docs.curator.interworks.com/site_content_design/content_discovery/search.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Search

> Enable and configure search functionality to help users discover and locate content across the Curator portal.

The frontend search functionality helps explore your Curator content or access specific content directly without
navigating through the menus.

## Enabling Search

1. Navigate to the backend of the system (e.g. `http://curatorexample.com/backend`) and log in if prompted.
2. Navigate to *Settings > Curator > Portal Settings > Features > Usability*
3. Switch the toggle *Search* on to enable search

*Note: The search toggle enables the search prompt shown in the menu. If enabled, you can also add a search bar to your
page by using [Page Builder](/site_content_design/pages/pages_overview)*

### Content that is searched

The search considers the following components to generate the search results:

1. Titles
2. Descriptions
3. Keywords
4. From version 2023.02.15 onwards: Text content on pages

*Note:* Search results reflect all permissions set on the BI Platforms or by using [Restrict Access](/site_content_design/menus/restrict_access).
In case you have added dashboards or built content that should not be visible in search results, enable the *Hidden*
toggle. To hide dashboards navigate to the *Misc* tab and then in the *Discovery* section you find the toggle.
To hide other types of content, the toggle is in the details pane.

## Changing Search Result Display

Search results show the following components:

* Thumbnail (default if none was created/ set)
* Title
* Description (if existing)
* Keywords (if existing and matching the search term; max. 2 - more are indicated by an ellipsis)
* If the result content is favorited or not

**From release 2023.02.15 onwards**: The description is only shown for Pages if there is a match in it. Otherwise, Pages
will always show a preview of their content (with or without a match).

We highlight the match from your search term in the title, description, and keywords in bold font.

## Styling Search

Brand your search with the following settings

* Add a custom search icon (Available since 2022.11.30)
* Navigate to *Settings > Curator > Themes > Styles > Logo and Icons* to add your own search icon
* Style the colors of your search results
* Navigate to *Settings > Curator > Themes > Search Options* (in versions until 2022.09.28: *Settings > Curator > Portal
  Settings > Styles > Search Options*) to set the background and text color
* Navigate to *Settings > Curator > Themes > Styles > Miscellaneous > Navigation Highlight Color* (in versions until
  2022.09.28: *Settings > Curator > Portal Settings > Styles > Miscellaneous > Navigation Highlight Color*) to set the
  text color on hover

## Algorithm Details

Our search applies a fuzzy search algorithm, so search results are intentionally loose so as to help users find the
content regardless of minor typos or alternate spellings.

<img src="https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/site_content_design/content_discovery/search_results.png?fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=6ca03a4f356d011ad0b5ac43bc273331" alt="search result example!" data-og-width="1536" width="1536" data-og-height="972" height="972" data-path="assets/images/site_content_design/content_discovery/search_results.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/site_content_design/content_discovery/search_results.png?w=280&fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=e0ec8462282d8cbc594658585bc25d8d 280w, https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/site_content_design/content_discovery/search_results.png?w=560&fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=e6d143c7aa840b18e25163c7f3b7a654 560w, https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/site_content_design/content_discovery/search_results.png?w=840&fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=2703da55708d54fdfba79551da096690 840w, https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/site_content_design/content_discovery/search_results.png?w=1100&fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=e516e0736a662fe4de6cbc804715406c 1100w, https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/site_content_design/content_discovery/search_results.png?w=1650&fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=59f8c439e6fb1618a6c9989f2774fd85 1650w, https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/site_content_design/content_discovery/search_results.png?w=2500&fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=a5b4e946af83d772888942728f371fc5 2500w" />
