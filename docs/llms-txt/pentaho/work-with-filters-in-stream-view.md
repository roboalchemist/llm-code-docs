# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/data-integration-perspective-in-the-pdi-client/work-with-transformations-cp/run-your-transformation/inspect-your-data/use-filters-to-explore-your-data/filter-examples/work-with-filters-in-stream-view.md

# Work with filters in Stream View

In **Stream View**, to apply a filter to a flat table or other visualization, drag a field from the **Available Fields** panel to the **Filters** panel.

## Use the Select or Exclude filters

In Stream View, you can use the Select filter to search a list of values for a field and then choose the values to apply. Alternately, you can use the Exclude filter to search a list of values for a field and then choose values to omit.

The search method you use to find values can be performed manually from the list of available values or by using the search box to narrow the choices in longer lists. The following illustration shows the features of the Select filter:

![Select Filter Features](https://3411831820-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FAYwCj9fPr1B2pjC11IOQ%2Fuploads%2Fgit-blob-adc6e4aa9ddd64ed293c3623b4bb75449bb1ffd5%2FDET_SelectExcludeFilter_Tour_V2.png?alt=media)

In the table below, use the preceding illustration to reference the features of the Select and Exclude filters.

| Item                                                                                                                                                                                          | Feature      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1                                                                                                                                                                                             | Filter type  | Shows the name of the current filter, for example **Select** or**Exclude**.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| 2                                                                                                                                                                                             | Left pane\*  | <p>Shows the values available for the <strong>Select</strong> or the <strong>Exclude</strong> filter, and includes:</p><ul><li>The <strong>Search</strong> box that you can use to find, according to the entered character pattern, a specific value or values in the Filter field data. Search produces sorted results and is useful when working with large amounts data.</li><li>The number of available values, as indicated. Up to 25 available values are loaded at a time.</li></ul><p>Highlight the values that you want to use for the filtering action and then move them to the right pane.</p> |
| 3                                                                                                                                                                                             | Right pane\* | <p>Shows the values added, which determines the filtering action of the <strong>Select</strong> or the <strong>Exclude</strong> filter, and includes:</p><ul><li>The number of values added, as indicated from a maximum of 50.</li></ul><p>If you have values that you do not want to use for the filtering action, highlight and then move them to the left pane.</p>                                                                                                                                                                                                                                     |
| 4                                                                                                                                                                                             | Move icons   | <p>Use to add or remove values from the right pane, where:</p><ul><li>Single greater than icon (>) adds the highlighted value.</li><li>Single less than icon (<) removes the highlighted value.</li><li>Double greater than icon (>>) adds all the values.</li><li>Double less than symbol (<<) removes all the values.</li></ul>                                                                                                                                                                                                                                                                           |
| \*Single and multi-select actions are supported: Use double-click to move single values; CTRL click to highlight multiple individual values; and, SHIFT click to highlight a range of values. |              |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

#### Select filter example

In this example, you want to identify the names of specific contacts in your dataset using the Select filter.

1. From the Available Fields list, drag the **CONTACTLASTNAME** field to the **Filters panel**.

   ![Select Filter Example](https://3411831820-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FAYwCj9fPr1B2pjC11IOQ%2Fuploads%2Fgit-blob-4d151dcb34e9b152234c5554d74cd2248728715a%2FDET_SelectFilter_Example1_V2.png?alt=media)

   The **Filter menu** automatically displays.
2. Choose the **Select filter** to produce a list of contact names in the left pane and then enter characters and character patterns in the **Search** box to find contact names that contain those characters in the database.

   ![Search Box Entry Example](https://3411831820-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FAYwCj9fPr1B2pjC11IOQ%2Fuploads%2Fgit-blob-24e158cf135b35cb24deec5e3501bc2914a40aa8%2FDET_SelectFilter_Example_2_V2.png?alt=media)

   The left pane displays names that result from your search.
3. Add the names you want to use for filtering by highlighting and moving them to the right pane. Continue searching for names and add them to the right pane. You can add up to 50 names.

   ![Select Filter Value Selections](https://3411831820-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FAYwCj9fPr1B2pjC11IOQ%2Fuploads%2Fgit-blob-015da1fa01a3287c73b0623e166c3605ffbb4940%2FDET_SelectFilter_Example%203_V2.png?alt=media)

   These names are the values that will be used for the Select filter.

   ![Exceeded Selection Indication](https://3411831820-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FAYwCj9fPr1B2pjC11IOQ%2Fuploads%2Fgit-blob-de31e2322b703dd636a5fe8a4fbec9d64ddef4f4%2FDET_SelectFilter_Example_4.png?alt=media)
4. If needed, refine the list of names already chosen. Note that the **Apply** button is enabled when any values are ready to be used as the Select filter.

   ![Value Removal Example](https://3411831820-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FAYwCj9fPr1B2pjC11IOQ%2Fuploads%2Fgit-blob-c3a8fe01c74007deb9e6c4a73a5ec226cde53d88%2FDET_SelectFilter_Example_5_V2.png?alt=media)
5. Click **Apply** to proceed with filtering when your list is complete or the maximum number of values has been added.

   ![Select Filter Limit](https://3411831820-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FAYwCj9fPr1B2pjC11IOQ%2Fuploads%2Fgit-blob-6a8213c75f855ea39df7739038c470d95b133cc6%2FDET_SelectFilter_Example_6_V2.png?alt=media)

   The table updates to only show the selected contact names.
