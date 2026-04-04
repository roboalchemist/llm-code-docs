# Source: https://docs.snowflake.com/en/developer-guide/declarative-sharing/consumer/access-app-content.md

# Access content in a Declarative Native App

If you have installed a Snowflake Declarative Native App, or have had a Declarative Native App shared with you by a member of your organization, you can access the data and functionality through Snowsight or [Snowflake CLI](../../snowflake-cli/index.md).

## Access app content from Snowsight

1. [Sign in to Snowsight](https://app.snowflake.com) with your Snowflake account.
2. In the navigation menu, select Catalog » Apps.
3. Select the app you want to access.
4. Browse the app’s content, which includes:

   * **Notebooks**: If the app includes notebooks, you can run them to see visualizations and other content.
   * **Tables and views**: You can query the tables and views that are part of the app.
   > **Note:**
   >
   > Notebooks in Declarative Native Apps are read-only. You can run the cells in a notebook, or run entire notebook, but you can’t modify it.

## Access app notebooks

You can access the app’s notebooks, either through Snowsight or through [Snowflake CLI](../../snowflake-cli/index.md).

### Find and open notebooks available to your role using Snowsight

1. Sign in to [Snowsight](../../../user-guide/ui-snowsight-gs.md).
2. In the navigation menu, select Catalog » Apps.
3. Select the app you want to access. A side panel appears with information about the app and its notebooks.
4. Select **Open**. If notebooks are available to your role, they appear in the drop-down list. If no notebooks are available, the **Open** button opens the worksheet directly.
5. If a list of notebooks appears, select a notebook from the list. The notebook opens, and is listed as a part of the app.
6. You can run individual cells in the notebook, or run the entire notebook by selecting Run » Run all cells.
7. Selecting the notebook name opens a menu with the following items:

   * Other notebooks in the same app that you can navigate to.
   * A link to the listing for this application.
8. The “<” (left chevron) button takes you to the notebook list page. The notebook list page has two tabs:

   * All Notebooks: Lists all notebooks available to your role.
   * Shared with me: Lists notebooks for which you aren’t the owner.

### Find and open notebooks available to your role using SQL commands

1. Sign in to [Snowsight](../../../user-guide/ui-snowsight-gs.md), and select **Write SQL queries**.
2. Use the [SHOW APPLICATIONS](../../../sql-reference/sql/show-applications.md) command to see what apps are installed in your account.

   ```sqlexample
   SHOW APPLICATIONS;
   ```

   Use the application name (for example, `market_data_app`) to access the app’s content.
3. See what notebooks are in the app with the command: [SHOW NOTEBOOKS IN APPLICATION](../../../sql-reference/sql/show-notebooks.md).

   ```sqlexample
   SHOW NOTEBOOKS IN APPLICATION market_data_app;
   ```

   For example, the command might return a notebook called `MARKETING_NB`.

   Optional: Use the [DESC NOTEBOOK](../../../sql-reference/sql/desc-notebook.md) command to see more information about the notebook.

   ```sqlexample
   DESC NOTEBOOK market_data_app.APP$UI.MARKETING_NB;
   ```

4. Run the notebook with the command: [EXECUTE NOTEBOOK](../../../sql-reference/sql/execute-notebook.md).

   ```sqlexample
   EXECUTE NOTEBOOK market_data_app.APP$UI.MARKETING_NB();
   ```

5. In the navigation menu, select Projects » Notebooks.

   The notebook should appear in your list of available notebooks.
6. Open the notebook by selecting it from the list.

   The notebook opens, and is listed as a part of the app.

### Access tables and views in the app

Tables and views are available in the app’s schema. You can access them using SQL commands.

* See what schemas are in the app using [SHOW SCHEMAS IN APPLICATION](../../../sql-reference/sql/show-schemas.md).

  > ```sqlexample
  > SHOW SCHEMAS IN APPLICATION <app_name>;
  > ```
>
* See tables, dynamic tables, views, and semantic views in a schema, application, or account using the [SHOW TABLES](../../../sql-reference/sql/show-tables.md), [SHOW DYNAMIC TABLES](../../../sql-reference/sql/show-dynamic-tables.md), [SHOW VIEWS](../../../sql-reference/sql/show-views.md), and [SHOW SEMANTIC VIEWS](../../../sql-reference/sql/show-semantic-views.md) commands:

  > ```sqlexample
  > -- Using SHOW TABLES
  > SHOW TABLES IN SCHEMA <app_name>.<schema_name>;
  > SHOW TABLES IN APPLICATION <app_name>;
  > SHOW TABLES IN ACCOUNT;
  >
  > -- Using SHOW DYNAMIC TABLES
  > SHOW DYNAMIC TABLES IN SCHEMA <app_name>.<schema_name>;
  > SHOW DYNAMIC TABLES IN APPLICATION <app_name>;
  > SHOW DYNAMIC TABLES IN ACCOUNT;
  >
  > -- Using SHOW VIEWS
  > SHOW VIEWS IN SCHEMA <app_name>.<schema_name>;
  > SHOW VIEWS IN APPLICATION <app_name>;
  > SHOW VIEWS IN ACCOUNT;
  >
  > -- Using SHOW SEMANTIC VIEWS
  > SHOW SEMANTIC VIEWS IN SCHEMA <app_name>.<schema_name>;
  > SHOW SEMANTIC VIEWS IN APPLICATION <app_name>;
  > SHOW SEMANTIC VIEWS IN ACCOUNT;
  > ```
>
* Select items in a view or table, for example:

  > ```sqlexample
  > SELECT * from <app_name>.<schema>.<view>;
  > SELECT * from <app_name>.<schema>.<table>;
  > ```
>
* Create streams on shared tables and views to track changes. See [Introduction to streams](../../../user-guide/streams-intro.md) for syntax examples. Note that creating a stream on a shared table or view requires that the provider has enabled change tracking on the source object. If you encounter an error creating a stream, contact the provider to request that they enable `CHANGE_TRACKING`.

### Considerations

Notebooks in Declarative Native Apps are interactive, but are read-only. They can’t be modified, copied, or cloned.

To view past notebook executions, select Schedule notebook run » View run history.
