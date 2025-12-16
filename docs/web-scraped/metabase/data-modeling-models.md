# Source: https://www.metabase.com/docs/latest/data-modeling/models

<div>

1.  [Home](/docs/latest/)
2.  [Data Modeling](/docs/latest/data-modeling/start)

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

# Models

Models are a fundamental building block in Metabase. Models curate data from another table or tables from the same database to anticipate the kinds of questions people will ask of the data. You can think of them as derived tables, or a special kind of saved question meant to be used as the starting point for new questions. You can base a model on a SQL or query builder question, which means you can include custom, calculated columns in your model.

Models:

-   Let you update column descriptions and customize metadata to create great starting points for exploration.
-   Show up higher in search results and get highlighted when other users start new questions to promote reuse.
-   Live in collections to keep them separate from messy database schemas.
-   Can [surface individual records in search results](#surface-individual-records-in-search-by-matching-against-this-column).
-   Can be [persisted for faster loading](./model-persistence).

For more on why and how to use models, check out our [Learn article on models](/learn/metabase-basics/getting-started/models).

## How to use models

You can use models to:

-   Create, uh, models, with model here meaning an intuitive description of some concept in your business that you codify as a set of columns. An example model could be a "customer", which is a table that pulls together customer information from multiple tables and adds computed columns, like adding a lifetime value (LTV) column. This model represents the [measures and dimensions](/learn/grow-your-data-skills/data-fundamentals/dimensions-and-measures) that you think are relevant to your understanding of your customers.
-   Let people explore the results of SQL queries with the query builder (provided you [set the column types](#column-type)).
-   Create summary tables that pull in or aggregate data from multiple tables.
-   Clean up tables with unnecessary columns and rows filtered out.

The idea with models is to give other people a good "starting point table" that makes it easier to answer any questions they have about the subject being modeled.

## Create a model

First, search for models that already exist. If you can't find one that meets your needs, you can create a model:

-   [from scratch](#create-a-model-from-scratch), or
-   [from a saved question](#create-a-model-from-a-saved-question).

Models you create are automatically [pinned to the current collection](../exploration-and-organization/collections#pinned-items).

### Create a model from scratch

-   Navigate to the Models tab in the sidebar. You might have to open it using the button in the top left, then scroll down to the section labeled **Data**, and pick **Models**. Then click on the **+** button in the top right.
-   Or open the [command palette](/docs/latest/exploration-and-organization/exploration#command-palette) and type "model." Then click on the **New model** action.

Now choose either the query builder or a native query (if you want to use SQL). The advantage of using the query builder is that Metabase will be able to fill out some of the metadata for you; if you use SQL, you'll have to fill out that metadata manually.

Next, select your data, create your query, and save it.

Models you create are automatically [pinned to the current collection](../exploration-and-organization/collections#pinned-items).

### Create a model from a saved question

1.  [Ask a question](../questions/start) using either the query builder or the SQL editor, or select an existing saved question that you want to convert to a model.
2.  Save the question.
3.  Click on the **...** \> **Turn this into a model**.

![Turn a saved question into a model](./images/turn-into-a-model.png)

## Model details

To view a model's details, visit the model and click on the **info** button in the upper right. Here you'll see several tabs:

-   **Overview**: Includes the description, Creator and Last Editor, and the list of fields included in the model. As well as the model's [Entity ID](../installation-and-operation/serialization#metabase-uses-entity-ids-to-identify-and-reference-metabase-items).
-   **History**: Lists changes to the model, and by whom.
-   **Relationships**: Lists which questions use the model, and which tables the model is linked to.
-   **Actions**: Lists actions created based on the model.
-   **Insights**: Info about the [model's usage](../usage-and-performance-tools/usage-analytics). Only visible to admins on a [Pro or Enterprise plan](/pricing/).

## Add metadata to columns in a model

Metadata is the secret sauce of models. When you write a SQL query, Metabase can display the results, but it can't "know" what kind of data it's returning (like it can with questions built using the query builder). What this means in practice is that people won't be able explore the results with the query builder, because Metabase doesn't understand what the results are. With models, however, you can tell Metabase what kind of data is in each returned column so that Metabase can still do its query magic. Metadata will also make filtering nicer by showing the correct filter widget, and it will help Metabase to pick the right visualization for the results.

If you only set one kind of metadata, set the **Column type** to let Metabase know what kind of data it's working with.

### Display name

What people will see as the column's name.

### Description

A place to write helpful context for the column.

### Database column this maps to

For models based on SQL queries, you can tell Metabase if the column has the same type as an existing database column.

### Column type

You can set the [column type](./semantic-types). The default is "No special type".

If your model is based on a SQL query and you want people to be able to explore the results with the query builder, you'll need to set the [column type](./semantic-types) for each column in your model.

### This column should appear in...

You can specify whether a column should appear in the table view, or just in a detail view (when you click on the entity/primary key for the row).

-   Table and detail views
-   Detail views only

### Display as

-   Text
-   Link (it's a URL people should be able to click on)

### Surface individual records in search by matching against this column

For string fields in records with integer entity keys, Metabase will give you the option make the values in that field show up when people search your Metabase. Essentially, Metabase will index these values and make them available to Metabase's search engine. This option is handy when people often want to jump straight to an individual record in your model.

For example, if you have a model with accounts, you could turn on this option for a column listing the account's name or email so that people can quickly search for specific accounts in the model from anywhere in your Metabase. When people click on a record in the search results, Metabase will jump straight to the model and the object detail for that record.

There are some limitations to this indexing:

-   The indexed field must be a text/string type.
-   The record containing the field must have an integer entity key.
-   To keep your search speedy, Metabase will only index 5000 unique values from that field, so this option isn't the best choice to turn on for tables with a ton of records.

## Edit a model's query

You can edit a model's query by clicking on the down arrow next to the model's name and clicking on **Edit query definition**. When you're doing editing, be sure to save your changes. Unlike questions, which prompt you to save as a new question, any changes here will overwrite the existing model. If you want to create a new model from an existing model, select **Duplicate this model** from the model sidebar (the icon of two overlapping squares).

### Checking for breaking changes

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdib3g9IjAgMCAyNiAyNiIgZmlsbD0ibm9uZSI+CiAgPHBhdGggZD0iTTEyIDEzVjE1IiBzdHJva2Utd2lkdGg9IjIiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgc3Ryb2tlPSIjNTA5RUUzIj48L3BhdGg+CiAgPHBhdGggZD0iTTEyIDEwQzEyLjU1MjMgMTAgMTMgOS41NTIyOCAxMyA5QzEzIDguNDQ3NzIgMTIuNTUyMyA4IDEyIDhDMTEuNDQ3NyA4IDExIDguNDQ3NzIgMTEgOUMxMSA5LjU1MjI4IDExLjQ0NzcgMTAgMTIgMTBaIiBmaWxsPSIjNTA5RUUzIj48L3BhdGg+CiAgPHBhdGggZD0iTTEyIDE5LjI1QzE2LjAwNDEgMTkuMjUgMTkuMjUgMTYuMDA0MSAxOS4yNSAxMkMxOS4yNSA3Ljk5NTk0IDE2LjAwNDEgNC43NSAxMiA0Ljc1QzcuOTk1OTQgNC43NSA0Ljc1IDcuOTk1OTQgNC43NSAxMkM0Ljc1IDE2LjAwNDEgNy45OTU5NCAxOS4yNSAxMiAxOS4yNVoiIHN0cm9rZS13aWR0aD0iMS41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIHN0cm9rZT0iIzUwOUVFMyI+PC9wYXRoPgo8L3N2Zz4=)

Checking for breaking changes is only available on [Pro](/product/pro) and [Enterprise](/product/enterprise) plans (both self-hosted and on Metabase Cloud).

When you save changes to a model, Metabase will try to detect whether your changes would break any other entities that depend on that model. For example, if you remove a column from the model, but other questions based on that model rely on that column, Metabase will warn you that those downstream questions will break.

![Check dependencies](./images/check-dependencies.png)

Currently, Metabase will look for broken column references. If you rename or remove a column, Metabase will likely flag the change as breaking downstream entities. But Metabase can't detect other types of changes like changing the column type or computation logic as breaking changes.

## Model list view

![Viewing a model as a list](./images/model-list.png)

List view helps you explore records one by one instead of sorting through big tables. You can customize the layout to highlight the most important fields.

To view a model as a list:

1.  Visit the model.
2.  Click the three-dot menu.
3.  Select **Edit metadata**.
4.  Navigate to the **Settings** tab.
5.  Under "What should the default view of this data be?", toggle to **List**.

![Model list edit](./images/model-list-edit.png)

### Customize model list view

![Customize list layout](./images/customize-list.png)

You can customize how the data appears by clicking **Customize the List layout**.

Each item in the list has:

-   **An entity icon.** If the record has an image link, it shows the image, which you can hide anytime.
-   **A left column** showing the title or primary identifier.
-   **A right column** for up to 5 additional columns.

You can:

-   **Search for columns** using the "Find a column..." search box.
-   **Drag columns** from the available list into either the left column or right columns areas.
-   **Reorder columns** by dragging them within their respective areas.
-   **Remove columns** by clicking on the X on the column.

You can see a preview on the bottom with sample data from your model.

Click **Done** to save your changes.

## Start a question from a model

See [asking questions](../questions/start).

## [Refer to a model in the SQL query editor](../questions/native-editor/referencing-saved-questions-in-queries)

You can refer to a model in a SQL query just like you can refer to a saved question:

``` highlight
SELECT * FROM }
```

Or as a [common table expression (CTE)](/learn/sql/working-with-sql/sql-cte):

``` highlight
WITH model AS }
SELECT *
FROM model;
```

Simply typing `} ` will allow you to search for models (for example, you could type in `}` to search models, questions, and tables with the word "customer" in the title.

You can also use the data reference sidebar to browse the models available. To open the data reference sidebar, click on the **book** icon.

## Model version history

For [questions](../questions/start), [dashboards](../dashboards/start), and models, Metabase keeps a version history for the previous fifteen versions of that item. You can view changes and revert to previous versions.

See [History](../exploration-and-organization/history).

## Delete a model

You can move outdated or unneeded models to trash, or delete them permanently. Deleting a model will affect questions that use it as a data source.

See [Deleting and restoring items](../exploration-and-organization/delete-and-restore).

## Verifying a model

See [content verification](../exploration-and-organization/content-verification).

## Model persistence

See [Model persistence](./model-persistence)

## Further reading

-   [Models in Metabase](/learn/metabase-basics/getting-started/models)
-   [Troubleshooting models](../troubleshooting-guide/models).

<div>

Read docs for other [versions of Metabase](/docs/all).

</div>

###### Was this helpful?

![](data:image/svg+xml;base64,PHN2ZyBpZCBjbGFzcz0ibWUtMSIgd2lkdGg9IjE4IiBoZWlnaHQ9IjE4IiB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CiAgICA8cGF0aCBkPSJNMTAuNjY2NyA3LjMzMzMzSDE0LjYzNjdDMTQuOTIwNyA3LjMzMzM0IDE1LjIwMDEgNy40MDU5NSAxNS40NDgyIDcuNTQ0MjdDMTUuNjk2MyA3LjY4MjU5IDE1LjkwNDkgNy44ODIwMiAxNi4wNTQzIDguMTIzNjRDMTYuMjAzNiA4LjM2NTI1IDE2LjI4ODggOC42NDEwNCAxNi4zMDE2IDguOTI0OEMxNi4zMTQ0IDkuMjA4NTcgMTYuMjU0NSA5LjQ5MDkgMTYuMTI3NSA5Ljc0NUwxMy4yMTA4IDE1LjU3ODNDMTMuMDcyNCAxNS44NTU0IDEyLjg1OTUgMTYuMDg4NCAxMi41OTYgMTYuMjUxMkMxMi4zMzI1IDE2LjQxNCAxMi4wMjg5IDE2LjUwMDEgMTEuNzE5MiAxNi41SDguMzcxNjdDOC4yMzU4MyAxNi41IDguMSAxNi40ODMzIDcuOTY3NSAxNi40NUw0LjgzMzMzIDE1LjY2NjdNMTAuNjY2NyA3LjMzMzMzVjMuMTY2NjdDMTAuNjY2NyAyLjcyNDY0IDEwLjQ5MTEgMi4zMDA3MiAxMC4xNzg1IDEuOTg4MTZDOS44NjU5NSAxLjY3NTU5IDkuNDQyMDMgMS41IDkgMS41SDguOTIwODNDOC41MDQxNyAxLjUgOC4xNjY2NyAxLjgzNzUgOC4xNjY2NyAyLjI1NDE3QzguMTY2NjcgMi44NDkxNyA3Ljk5MDgzIDMuNDMwODMgNy42NiAzLjkyNTgzTDQuODMzMzMgOC4xNjY2N1YxNS42NjY3TTEwLjY2NjcgNy4zMzMzM0g5TTQuODMzMzMgMTUuNjY2N0gzLjE2NjY3QzIuNzI0NjQgMTUuNjY2NyAyLjMwMDcyIDE1LjQ5MTEgMS45ODgxNiAxNS4xNzg1QzEuNjc1NTkgMTQuODY2IDEuNSAxNC40NDIgMS41IDE0VjlDMS41IDguNTU3OTcgMS42NzU1OSA4LjEzNDA1IDEuOTg4MTYgNy44MjE0OUMyLjMwMDcyIDcuNTA4OTMgMi43MjQ2NCA3LjMzMzMzIDMuMTY2NjcgNy4zMzMzM0g1LjI1IiBzdHJva2U9IiM1MDllZTMiIHN0cm9rZS13aWR0aD0iMS41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjwvcGF0aD4KPC9zdmc+) Yes

![](data:image/svg+xml;base64,PHN2ZyBpZCBjbGFzcz0icm90YXRlLTE4MCBtZS0xIiB3aWR0aD0iMTgiIGhlaWdodD0iMTgiIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxwYXRoIGQ9Ik0xMC42NjY3IDcuMzMzMzNIMTQuNjM2N0MxNC45MjA3IDcuMzMzMzQgMTUuMjAwMSA3LjQwNTk1IDE1LjQ0ODIgNy41NDQyN0MxNS42OTYzIDcuNjgyNTkgMTUuOTA0OSA3Ljg4MjAyIDE2LjA1NDMgOC4xMjM2NEMxNi4yMDM2IDguMzY1MjUgMTYuMjg4OCA4LjY0MTA0IDE2LjMwMTYgOC45MjQ4QzE2LjMxNDQgOS4yMDg1NyAxNi4yNTQ1IDkuNDkwOSAxNi4xMjc1IDkuNzQ1TDEzLjIxMDggMTUuNTc4M0MxMy4wNzI0IDE1Ljg1NTQgMTIuODU5NSAxNi4wODg0IDEyLjU5NiAxNi4yNTEyQzEyLjMzMjUgMTYuNDE0IDEyLjAyODkgMTYuNTAwMSAxMS43MTkyIDE2LjVIOC4zNzE2N0M4LjIzNTgzIDE2LjUgOC4xIDE2LjQ4MzMgNy45Njc1IDE2LjQ1TDQuODMzMzMgMTUuNjY2N00xMC42NjY3IDcuMzMzMzNWMy4xNjY2N0MxMC42NjY3IDIuNzI0NjQgMTAuNDkxMSAyLjMwMDcyIDEwLjE3ODUgMS45ODgxNkM5Ljg2NTk1IDEuNjc1NTkgOS40NDIwMyAxLjUgOSAxLjVIOC45MjA4M0M4LjUwNDE3IDEuNSA4LjE2NjY3IDEuODM3NSA4LjE2NjY3IDIuMjU0MTdDOC4xNjY2NyAyLjg0OTE3IDcuOTkwODMgMy40MzA4MyA3LjY2IDMuOTI1ODNMNC44MzMzMyA4LjE2NjY3VjE1LjY2NjdNMTAuNjY2NyA3LjMzMzMzSDlNNC44MzMzMyAxNS42NjY3SDMuMTY2NjdDMi43MjQ2NCAxNS42NjY3IDIuMzAwNzIgMTUuNDkxMSAxLjk4ODE2IDE1LjE3ODVDMS42NzU1OSAxNC44NjYgMS41IDE0LjQ0MiAxLjUgMTRWOUMxLjUgOC41NTc5NyAxLjY3NTU5IDguMTM0MDUgMS45ODgxNiA3LjgyMTQ5QzIuMzAwNzIgNy41MDg5MyAyLjcyNDY0IDcuMzMzMzMgMy4xNjY2NyA3LjMzMzMzSDUuMjUiIHN0cm9rZT0iIzUwOWVlMyIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI+PC9wYXRoPgo8L3N2Zz4=) No

Send

###### Thanks for your feedback! 

[ Want to improve these docs? [Propose a change.](https://github.com/metabase/metabase/blob/master/docs/data-modeling/models.md) ]