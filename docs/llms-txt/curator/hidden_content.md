# Source: https://docs.curator.interworks.com/site_content_design/content_discovery/hidden_content.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Hidden Content

> Control visibility by hiding dashboards and other content from tiles, explorer, and search results while maintaining direct access and navigation visibility.

## Hidden and Hidden from Search Toggles

You can now control where content appears throughout Curator using the **Hidden** and **Hidden from Search** toggles.
These toggles are available for most content types and allow fine-grained control over how users discover content.

### Availability

| Content Type          | Hidden |  Hidden from Search  |
| --------------------- | :----: | :------------------: |
| File                  |   Yes  |          Yes         |
| Page                  |   Yes  |          Yes         |
| Menu                  |   Yes  | No *(not available)* |
| Power BI Dashboard    |   Yes  |          Yes         |
| Power BI Report       |   Yes  |          Yes         |
| Tableau Dashboard     |   Yes  |          Yes         |
| Tableau Metrics       |   Yes  |          Yes         |
| Sigma Workbooks       |   Yes  |          Yes         |
| ThoughtSpot Liveboard |   Yes  |          Yes         |
| ThoughtSpot Search    |   Yes  |          Yes         |

***

### Behavior

#### Hidden

* Removes the item from **all content displays**, including tiles and Explorer tiles.
* Prevents the content from appearing in featured or related content sections.

#### Hidden from Search

* Excludes the item only from **Curator search results**.
* The content continues to appear in other locations, such as tiles, related content, and Explorer tiles.
* This setting is **not available for Menus**.

***

### Where to Find the Hidden Settings

| Content Type              | Navigation Path                     |
| ------------------------- | ----------------------------------- |
| **File**                  | Content → File → General            |
| **Page**                  | Content → Page → Page Details       |
| **Menu**                  | Content → Navigation → Menu         |
| **Power BI Dashboard**    | Power BI → Dashboards → Discovery   |
| **Power BI Report**       | Power BI → Reports → Discovery      |
| **Tableau Dashboard**     | Tableau → Dashboards → Discovery    |
| **Tableau Metrics**       | Tableau → Metrics → Discovery       |
| **Sigma Workbooks**       | Sigma → Workbooks → Discovery       |
| **ThoughtSpot Liveboard** | ThoughtSpot → Liveboard → Discovery |
| **ThoughtSpot Search**    | ThoughtSpot → Search → Discovery    |

***

### How to Update Visibility Settings

1. Edit the desired content item (for example, a Dashboard, Report, Page, or File).
2. Navigate to the section shown in the table above.
3. Locate the **Hidden** and **Hidden from Search** toggles.
4. Use the toggles:
   * **Hidden** — hides the item from all content listings including menus.
   * **Hidden from Search** — hides the item only from search results.
5. Click **Save** to apply your changes.

***

### Notes

* Hidden items are still accessible through direct URLs for users with the correct permissions.
