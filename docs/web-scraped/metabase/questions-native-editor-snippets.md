# Source: https://www.metabase.com/docs/latest/questions/native-editor/snippets

<div>

1.  [Home](/docs/latest/)
2.  [Questions](/docs/latest/questions/start)

</div>

<div>

[ v0.57 ![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzIiIGhlaWdodD0iMzIiIHZpZXdib3g9IjAgMCAzMiAzMiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBjbGFzcz0iY2hldnJvbiI+CjxwYXRoIG9wYWNpdHk9IjAuOSIgZD0iTTMgOC45NjMzOEwxNiAyMS45NjM0TDI5IDguOTYzMzgiIHN0cm9rZT0iIzUwOWVlMyIgc3Ryb2tlLXdpZHRoPSI1IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjwvcGF0aD4KPC9zdmc+) ]

-   [v0.56](/docs/v0.56)
-   [v0.55](/docs/v0.55)
-   [v0.54](/docs/v0.54)
-   [v0.53](/docs/v0.53)
-   [v0.52](/docs/v0.52)
-   [v0.51](/docs/v0.51)
-   [v0.50](/docs/v0.50)
-   [v0.49](/docs/v0.49)
-   [v0.48](/docs/v0.48)
-   [See more](/docs/all)

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld2JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIj48cGF0aCBzdHJva2U9IiM1MDlFRTMiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIxLjUiIGQ9Ik0xNi4yODMgMTIuMjYgMTUuNSAxNWwtLjc4My0yLjc0YTQuMzMzIDQuMzMzIDAgMCAwLTIuOTc1LTIuOTc2TDkgOC41bDIuNzQtLjc4M2E0LjMzMyA0LjMzMyAwIDAgMCAyLjk3Ni0yLjk3NUwxNS41IDJsLjc4MyAyLjc0YTQuMzMzIDQuMzMzIDAgMCAwIDIuOTc1IDIuOTc2TDIyIDguNWwtMi43NC43ODNhNC4zMzQgNC4zMzQgMCAwIDAtMi45NzYgMi45NzVsLS4wMDEuMDAxWk02LjUgMjJsLjU5MS0xLjc3NGEzLjM3NSAzLjM3NSAwIDAgMSAyLjEzNS0yLjEzNUwxMSAxNy41bC0xLjc3NC0uNTkxYTMuMzc1IDMuMzc1IDAgMCAxLTIuMTM1LTIuMTM0TDYuNSAxM2wtLjU5MSAxLjc3NGEzLjM3NSAzLjM3NSAwIDAgMS0yLjEzNCAyLjEzNUwyIDE3LjVsMS43NzUuNTkxYTMuMzc1IDMuMzc1IDAgMCAxIDIuMTM0IDIuMTM0TDYuNSAyMloiPjwvcGF0aD48L3N2Zz4=) What's new](/releases)

</div>

<div>

</div>

# Snippets

![SQL snippet](../images/sql-snippets.png)

**Snippets** are reusable bits of SQL or native queries. Anyone with permissions to the [native editor](./writing-sql) can create and edit snippets, which are then available for all native query authors.

For example, if you frequently write queries that involve multiple tables, you can save the SQL code that joins those tables as a snippet so that you (and others in your organization) can reuse that code in multiple questions.

You can use snippets to define standardized KPIs and filters using SQL, just like you do with [metrics](../../data-modeling/metrics) and [segments](../../data-modeling/segments) in the query builder. For example, you may want to store exactly how you calculate revenue, or what constitutes an active user.

You can also use snippets to define a set of reusable filters for SQL questions.

## Create a snippet

In the [**native editor**](./writing-sql):

1.  Open the native editor by clicking **+ New \> SQL query** or **+ New \> Native query** in the top right corner.

2.  Write some SQL or native code and highlight a section of code that you want to save to reuse later. The section doesn't have to be a whole query. For example, you can highlight:

    ::: 
    ::: highlight
    ``` highlight
    orders AS o
    LEFT JOIN products AS p ON o.product_id = p.id
    WHERE p.category = }
    ```
    :::
    :::

    Within a snippet, you can use:

    -   [SQL parameters](#sql-parameters-in-snippets), like `}`,
    -   references to other snippets, like `}` (Metabase will detect and disallow circular references),
    -   [references to saved questions or models](./referencing-saved-questions-in-queries), like `}`.

3.  Right-click on the highlighted section and select **Save as snippet** to create a snippet.

    ![Save a snippet](../images/save-snippet.png)

4.  Name and describe your snippet. Snippet names must be unique (even names of archived snippets).

5.  Save.

You can also create a new snippet from the Snippet sidebar:

1.  Open the native editor by clicking **+ New \> SQL query** or **+ New \> Native query**in the top right corner.
2.  Open the Snippet sidebar by clicking the **Snippets** button above the editor window
3.  Enter the code that you want to save as a reusable snippet.
4.  Save.

## Use a snippet

You can insert a saved snippet into your query, which will add a `}` reference:

``` highlight
SELECT
  *
FROM
 }
```

To add a snippet to your native code, start typing `}` and Metabase will present autocomplete options for available snippets.

Metabase is sensitive to whitespace in snippet references, so you should type `}`, with no space between ` and `snippet`, and with a space between `:` and snippet's name.

When you execute the query, behind the scenes Metabase replace the snippet reference with the snippet's SQL.

You can also just pick a snippet to insert from the snippet sidebar:

1.  Open the snippet sidebar by clicking on the **Snippets** button above the editor window. ![Open snippet sidebar](../images/snippet-button.png)
2.  Search for the snippet. Note that search results only include snippets that you have permissions to see.
3.  Hover over a snippet and click on the arrow to the left of snippet's name to insert it into your query.

If you use aliases in a snippet, you'll need to refer to those aliases in the larger query. For example, if a snippet aliases `products AS p`, code outside of the snippet will need to use the alias `p` to refer to columns in that table (as in `p.column_name`).

## Preview a query with snippets

Metabase will keep the snippet as a reference and will not show you the full query - with snippet's code substituted - in the SQL editor itself. You can see the full query that Metabase will send to the database by clicking on the **Eye** icon above the editor.

![Query preview](../images/query-preview.png)

## Edit snippets

Editing snippets is a great way to make changes to many questions at once. If, for example, you've saved the SQL code to pull user data from tables X, Y, and Z as the snippet `User Data`, but you need to change how that data is pulled (such as by adding data from another column or table), you can update the SQL code in the snippet, and all questions that use the snippet `User Data` will have the updated code.

![Edit a snippet](../images/edit-snippet.png)

To edit a snippet:

1.  Open the snippet sidebar by clicking on the **Snippet** icon above the editor window.

2.  Search for the snippet. Search results only include snippets you have permission to edit.

3.  Click the **down arrow** to the right of the snippet name, then click **Edit**.

    You can change the code, snippet name, and snippet description.

-   **Editing a snippet's name**. Changing a snippet's name will update the snippet's name in every question that uses that snippet. Renaming a snippet won't break any existing *questions* that reference this snippet, but it will **break other snippets** that reference this snippet.

-   **Editing a snippet's code.** Here's where we have to remind you that with great power comes great responsibility. There is one major caveat when editing snippets, worthy of a callout: if you edit a snippet and include broken code, you will break every question that uses that snippet. Make sure to test your code before saving it to an existing snippet.

## Archive snippets

Archiving snippets can help keep dated or less relevant snippets out of the way.

When you archive a snippet, the snippet no longer populates in the snippet autocomplete dropdown, and the snippet will no longer show up in the list of snippets in the sidebar. Archiving a snippet does **not** affect any existing queries that use the snippet, so you can safely archive a snippet without impacting any questions.

To archive a snippet:

1.  Open the snippet sidebar by clicking on the **Snippet** icon above the editor window.
2.  Search for the snippet.
3.  Click the **down arrow** to the right of the snippet name, then click **Edit**.
4.  Click **Archive**

You can access an archived snippet from the snippet sidebar menu by clicking on the archived button in the bottom left of the sidebar.

Although there is no way to delete a snippet, you can archive and unarchive a snippet at any time.

Two snippets cannot share the same name, as even if a snippet is archived, that snippet might still be active in questions.

## SQL parameters in snippets

You can reference [SQL parameters](sql-parameters) in snippets. For example, you can save a snippet with SQL code like

``` highlight
 
WHERE
  }
AND category = }
GROUP BY }
```

When a snippet with parameters is added to a SQL query, Metabase will show a widget for the snippet's parameter.

![Snippet with a parameter](../images/snippet-with-param.png)

You'll be able to specify the type, connected columns, and default values for the parameters coming from snippets in the query's Variables sidebar.

Settings for snippet parameters are defined by the query, not the snippet, so settings aren't shared between queries that use the same snippet. For example, if you have a snippet like:

``` highlight
WHERE }
```

you could put the snippet in one query and have the snippet parameter map to a `CREATED_AT` column, and put the snippet in another query and have that same snippet parameter map to a different column, like `CANCELED_AT`.

If you have multiple snippets containing parameters with the same name, the question using those snippets will only use one instance of the parameter. For example, if `}` contains parameter `}` and `}` also contains parameter `}`, the question will display only one `}` parameter and use its value in both snippets.

### Sharing parameters across questions

You can also use snippets to share parameters across multiple SQL questions, including questions that build on one another (nested questions). For example, you have a question "Orders by date" that filters orders using `}`. You then create another question, say "Revenue by product," that uses the results from "Orders by date." To keep using the same `}` parameter in both questions, move the SQL that contains the parameter from "Orders by date" into a snippet and update both questions to reference that snippet. Now, both questions surface the same parameter, and a single dashboard date filter can control both cards that use the snippet.

## Snippet permissions

Any user who has native editor permissions to at least one of your connected databases will be able to view the snippets sidebar, and will be able to create, edit, and archive or unarchive any and all snippets --- even snippets intended to be used with databases the user lacks SQL editing access to.

Some plans contain additional functionality for organizing snippets into folders and setting permissions on those folders. See our [docs on Snippet folders and permissions](../../permissions/snippets).

## Why use Snippets?

Snippets are good for:

-   **Standardization**

    How does your organization define a popular product? Is it by number of units sold? Or by reviews with an average rating greater than 4? You can define those qualifications for a popular product and codify them in a Snippet, `}`, and have that code populate in every question that uses that snippet. If down the line this definition needs to change, simply update the snippet's SQL, and the change will propagate to all questions that use that snippet.

    Similar to how [segments](../../data-modeling/segments) (a named filter or set of filters) and [metrics](../../data-modeling/models) (a named computation) can standardize analytics in your organization, snippets offer a way to ensure correctness and consistency of SQL across teams.

-   **Efficiency**

    Do you find yourself copying and pasting SQL code often? Don't want to bother remembering which foreign keys map to which tables? Write that complicated join once, save it as a snippet, and summon the snippet as needed.

-   **Education**

    Snippets can level up folks who are new to SQL (or even experienced analysts) by exposing them to your organization's "canonical SQL," or to more efficient or more complex queries. Reading, copying, and building upon quality code is one of the best ways to develop skills. It can also save your organization time: people can copy a snippet's code, modify it to obtain different results, and save that code as a new snippet for others to use.

## Learn more

-   [Snippets vs Saved Questions vs Views](/learn/metabase-basics/querying-and-dashboards/sql-in-metabase/organizing-sql).
-   If you're having trouble with your SQL query, go to the [SQL troubleshooting guide](../../troubleshooting-guide/sql).

<div>

Read docs for other [versions of Metabase](/docs/all).

</div>

###### Was this helpful?

![](data:image/svg+xml;base64,PHN2ZyBpZCBjbGFzcz0ibWUtMSIgd2lkdGg9IjE4IiBoZWlnaHQ9IjE4IiB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CiAgICA8cGF0aCBkPSJNMTAuNjY2NyA3LjMzMzMzSDE0LjYzNjdDMTQuOTIwNyA3LjMzMzM0IDE1LjIwMDEgNy40MDU5NSAxNS40NDgyIDcuNTQ0MjdDMTUuNjk2MyA3LjY4MjU5IDE1LjkwNDkgNy44ODIwMiAxNi4wNTQzIDguMTIzNjRDMTYuMjAzNiA4LjM2NTI1IDE2LjI4ODggOC42NDEwNCAxNi4zMDE2IDguOTI0OEMxNi4zMTQ0IDkuMjA4NTcgMTYuMjU0NSA5LjQ5MDkgMTYuMTI3NSA5Ljc0NUwxMy4yMTA4IDE1LjU3ODNDMTMuMDcyNCAxNS44NTU0IDEyLjg1OTUgMTYuMDg4NCAxMi41OTYgMTYuMjUxMkMxMi4zMzI1IDE2LjQxNCAxMi4wMjg5IDE2LjUwMDEgMTEuNzE5MiAxNi41SDguMzcxNjdDOC4yMzU4MyAxNi41IDguMSAxNi40ODMzIDcuOTY3NSAxNi40NUw0LjgzMzMzIDE1LjY2NjdNMTAuNjY2NyA3LjMzMzMzVjMuMTY2NjdDMTAuNjY2NyAyLjcyNDY0IDEwLjQ5MTEgMi4zMDA3MiAxMC4xNzg1IDEuOTg4MTZDOS44NjU5NSAxLjY3NTU5IDkuNDQyMDMgMS41IDkgMS41SDguOTIwODNDOC41MDQxNyAxLjUgOC4xNjY2NyAxLjgzNzUgOC4xNjY2NyAyLjI1NDE3QzguMTY2NjcgMi44NDkxNyA3Ljk5MDgzIDMuNDMwODMgNy42NiAzLjkyNTgzTDQuODMzMzMgOC4xNjY2N1YxNS42NjY3TTEwLjY2NjcgNy4zMzMzM0g5TTQuODMzMzMgMTUuNjY2N0gzLjE2NjY3QzIuNzI0NjQgMTUuNjY2NyAyLjMwMDcyIDE1LjQ5MTEgMS45ODgxNiAxNS4xNzg1QzEuNjc1NTkgMTQuODY2IDEuNSAxNC40NDIgMS41IDE0VjlDMS41IDguNTU3OTcgMS42NzU1OSA4LjEzNDA1IDEuOTg4MTYgNy44MjE0OUMyLjMwMDcyIDcuNTA4OTMgMi43MjQ2NCA3LjMzMzMzIDMuMTY2NjcgNy4zMzMzM0g1LjI1IiBzdHJva2U9IiM1MDllZTMiIHN0cm9rZS13aWR0aD0iMS41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjwvcGF0aD4KPC9zdmc+) Yes

![](data:image/svg+xml;base64,PHN2ZyBpZCBjbGFzcz0icm90YXRlLTE4MCBtZS0xIiB3aWR0aD0iMTgiIGhlaWdodD0iMTgiIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxwYXRoIGQ9Ik0xMC42NjY3IDcuMzMzMzNIMTQuNjM2N0MxNC45MjA3IDcuMzMzMzQgMTUuMjAwMSA3LjQwNTk1IDE1LjQ0ODIgNy41NDQyN0MxNS42OTYzIDcuNjgyNTkgMTUuOTA0OSA3Ljg4MjAyIDE2LjA1NDMgOC4xMjM2NEMxNi4yMDM2IDguMzY1MjUgMTYuMjg4OCA4LjY0MTA0IDE2LjMwMTYgOC45MjQ4QzE2LjMxNDQgOS4yMDg1NyAxNi4yNTQ1IDkuNDkwOSAxNi4xMjc1IDkuNzQ1TDEzLjIxMDggMTUuNTc4M0MxMy4wNzI0IDE1Ljg1NTQgMTIuODU5NSAxNi4wODg0IDEyLjU5NiAxNi4yNTEyQzEyLjMzMjUgMTYuNDE0IDEyLjAyODkgMTYuNTAwMSAxMS43MTkyIDE2LjVIOC4zNzE2N0M4LjIzNTgzIDE2LjUgOC4xIDE2LjQ4MzMgNy45Njc1IDE2LjQ1TDQuODMzMzMgMTUuNjY2N00xMC42NjY3IDcuMzMzMzNWMy4xNjY2N0MxMC42NjY3IDIuNzI0NjQgMTAuNDkxMSAyLjMwMDcyIDEwLjE3ODUgMS45ODgxNkM5Ljg2NTk1IDEuNjc1NTkgOS40NDIwMyAxLjUgOSAxLjVIOC45MjA4M0M4LjUwNDE3IDEuNSA4LjE2NjY3IDEuODM3NSA4LjE2NjY3IDIuMjU0MTdDOC4xNjY2NyAyLjg0OTE3IDcuOTkwODMgMy40MzA4MyA3LjY2IDMuOTI1ODNMNC44MzMzMyA4LjE2NjY3VjE1LjY2NjdNMTAuNjY2NyA3LjMzMzMzSDlNNC44MzMzMyAxNS42NjY3SDMuMTY2NjdDMi43MjQ2NCAxNS42NjY3IDIuMzAwNzIgMTUuNDkxMSAxLjk4ODE2IDE1LjE3ODVDMS42NzU1OSAxNC44NjYgMS41IDE0LjQ0MiAxLjUgMTRWOUMxLjUgOC41NTc5NyAxLjY3NTU5IDguMTM0MDUgMS45ODgxNiA3LjgyMTQ5QzIuMzAwNzIgNy41MDg5MyAyLjcyNDY0IDcuMzMzMzMgMy4xNjY2NyA3LjMzMzMzSDUuMjUiIHN0cm9rZT0iIzUwOWVlMyIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI+PC9wYXRoPgo8L3N2Zz4=) No

Send

###### Thanks for your feedback! 

[ Want to improve these docs? [Propose a change.](https://github.com/metabase/metabase/blob/master/docs/questions/native-editor/snippets.md) ]