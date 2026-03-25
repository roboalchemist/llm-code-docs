# Source: https://docs.snowflake.com/en/developer-guide/snowflake-ml/feature-store/feature-store-ui.md

# Find Feature Store objects

After you create entities and feature views, you can use the Feature Store User Interface in Snowsight to find the objects you need. Use the search bar to search for Feature Store objects, such as the following:

* Feature views
* Feature column names
* Description names
* Entity names

When you search for an object, Snowflake does a universal search across all feature store object names and metadata.
Snowflake searches through all of the metadata to return the best possible result.

For example, you might have a feature view called `rider_features`, that has this comment: “demographic features for all users who are signed up as passengers of ride share services”. If your search query is “passenger features”, the search results will return the `rider_features` view even though the search query didn’t include “rider”.

For more information about the universal search, see [Search Snowflake objects and resources](../../../user-guide/ui-snowsight-universal-search.md).

> **Important:**
>
> For information about the privileges you need to access features within the feature store, see [Snowflake Feature Store access control model](rbac.md).

To access the Feature Store User Interface, do the following:

* Sign in to [Snowsight](../../../user-guide/ui-snowsight-gs.md).
* In the navigation menu, select AI & ML » Features.

The landing page lists all the feature views within the feature store that you’ve selected. It also includes summary information about each feature view, such as the following:

* Number of versions
* Description
* Feature column names
* Entity name

The following image shows the feature views:

At the top of the page, select the Entities tab to see the Feature Views organized by entity.
The view also shows you the join keys used by the entity to get the features.

To see the details of a feature view, do the following:

* Select the feature view.
* Select the version you want to view from the dropdown in the top-right corner.

You can now see the details of the feature view, such as the following:

* Whether it’s a dynamic table or a view
* Feature column details

The following image shows where you can see whether the feature view is a dynamic table or a view:

> **Note:**
>
> You can use the Lineage tab to display the end to end lineage of the source data and the downstream objects from the feature view. Lineage tracking is a public preview feature.

For a dynamic table, to view information about its metrics and refresh history, select the table name.

To delete a feature view or refresh a dynamic table, select the … button.

The following image shows the lineage of a feature view along with the … UI element:
