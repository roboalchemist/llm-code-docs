# Source: https://dagshub.com/docs/quick_start/query_data/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTggMTJoOHYySDh6bTIgOEg2VjRoN3Y1aDV2My4xbDItMlY4bC02LTZINmEyIDIgMCAwIDAtMiAydjE2YTIgMiAwIDAgMCAyIDJoNHptLTItMmg0LjFsLjktLjlWMTZIOHptMTIuMi01Yy4xIDAgLjMuMS40LjJsMS4zIDEuM2MuMi4yLjIuNiAwIC44bC0xIDEtMi4xLTIuMSAxLTFjLjEtLjEuMi0uMi40LS4ybTAgMy45TDE0LjEgMjNIMTJ2LTIuMWw2LjEtNi4xeiIgLz48L3N2Zz4=)](https://dagshub.com/DagsHub-Official/dagshub-docs/src/main/docs/quick_start/query_data.md "Edit this page")

# Query & Filter a Dataset[¶](#query-filter-a-dataset "Permanent link")

Now that we have our [enriched dataset](../add_edit_metadata/), we can start filtering it and creating subsets. Querying and filtering can be used to remove unwanted samples or classes, but also to curate datasets for specific tasks, for example in a case where we\'d want to train on data from a specific location or customer.

After creating our data subsets - we can download or stream the data directly to our training environment using the DagsHub client.

Let\'s see how to query our datasources through the UI and DagsHub client.

## Video Tutorial[¶](#video-tutorial "Permanent link")

# An error occurred. 

Unable to execute JavaScript.

## Step-by-Step Guide[¶](#step-by-step-guide "Permanent link")

### UI Flow[¶](#ui-flow "Permanent link")

1.  In your datasource view, the top of the screen is the query builder. The query builder has a basic and advanced mode. For simple queries, you can simply click the \"+\" icon and add

    <figure data-markdown="span">
    <a href="../assets/query_data/add_simple_condition.jpg" class="glightbox" data-type="image" data-width="auto" data-height="auto" data-desc-position="bottom"><img src="../assets/query_data/add_simple_condition.jpg" alt="Add Simple Condition" /></a>
    <figcaption>Add Simple Condition</figcaption>
    </figure>

2.  Now you\'ll need to choose which metadata field to apply the condition to, which condition to apply, and what value.

    <figure data-markdown="span">
    <a href="../assets/query_data/condition_structure.jpg" class="glightbox" data-type="image" data-width="auto" data-height="auto" data-desc-position="bottom"><img src="../assets/query_data/condition_structure.jpg" alt="Condition Structure" /></a>
    <figcaption>Condition Structure</figcaption>
    </figure>

3.  After applying your condition, click the \"Apply query\" button to run the query and see your data subset.

    <figure data-markdown="span">
    <a href="../assets/query_data/apply_query.jpg" class="glightbox" data-type="image" data-width="auto" data-height="auto" data-desc-position="bottom"><img src="../assets/query_data/apply_query.jpg" alt="Apply Query" /></a>
    <figcaption>Apply Query</figcaption>
    </figure>

    The query will load, and you\'ll see the datapoints that the condition applies to.

4.  To add additional conditions, simply click the \"+\" button again.

5.  Now, you might want to save this query for use in your model training, or for sharing with your team. To do this, simply click \"Save as new dataset\".

    <figure data-markdown="span">
    <a href="../assets/query_data/save_button.jpg" class="glightbox" data-type="image" data-width="auto" data-height="auto" data-desc-position="bottom"><img src="../assets/query_data/save_button.jpg" alt="Save Button" /></a>
    <figcaption>Save Button</figcaption>
    </figure>

6.  Then, add a name for your dataset, and click on save.

    <figure data-markdown="span">
    <a href="../assets/query_data/save_modal.jpg" class="glightbox" data-type="image" data-width="auto" data-height="auto" data-desc-position="bottom"><img src="../assets/query_data/save_modal.jpg" alt="Save Modal" /></a>
    <figcaption>Save Modal</figcaption>
    </figure>

#### Advanced Queries[¶](#advanced-queries "Permanent link")

Sometimes a simple AND query isn\'t enough, and you need to have complex NOT and OR queries. By toggling the advanced query mode, you can create these complex queries easily.

<figure>
<a href="../assets/query_data/advanced_builder.jpg" class="glightbox" data-type="image" data-width="auto" data-height="auto" data-desc-position="bottom"><img src="../assets/query_data/advanced_builder.jpg" alt="Advanced Query Builder Toggle" /></a>
<figcaption>Advanced Query Builder Toggle</figcaption>
</figure>

In the advanced query builder, you can add query conditions, like before, but also add condition groups.

<figure>
<a href="../assets/query_data/advanced_query.jpg" class="glightbox" data-type="image" data-width="auto" data-height="auto" data-desc-position="bottom"><img src="../assets/query_data/advanced_query.jpg" alt="Advanced Query" /></a>
<figcaption>Advanced Query</figcaption>
</figure>

A condition group can be AND or OR, and will define the relationship between the conditions under this group. In the example above, we see a query where one of 2 conditions must be met. Each of these condition is a group of conditions as well, and this can be arbitrarily complex.

### Python Client Flow[¶](#python-client-flow "Permanent link")

In many cases, you\'ll need to run queries from your development environment. DagsHub client offers an easy interface to create and run these queries. Below you\'ll see a simple example, but there are many different query operators - see them all in the [querying doc](../../use_cases/data_engine/query_and_create_subsets/#filtering-operators).

1.  Start by installing the DagsHub client. Simply type in the following:

    ::: highlight
        $ pip3 install dagshub
    :::

2.  Retrieve the datasource you created with the following code:

    ::: highlight
        from dagshub.data_engine import datasources

        ds = datasources.get_datasource(
          repo="<user_name>/<repo_name>", # User name and repository name separated by a "/"
          name="<datasource_name>", # Name of your datasource
        ) 
    :::

3.  Now we can define our query. DagsHub takes a pandas-like approach to querying in the client. To select which field to add the condition to, simply refer to it with square brackets (e.g. `ds["categories"]`). Then, add the operator, and the value.

    ::: highlight
        newQuery = ds["categories"].contains("cats")

        res = newQuery.all() # This will run the query on DagsHub

        print(res.dataframe) # Prints the results as a Pandas dataframe
    :::

    You can of course create more complex queries for example:

    ::: highlight
        newQuery = (ds["categories"].contains("cats") & (ds["cute"] == True)) | 
                   (ds["categories"].contains("dog") & (ds["size"] > 60) & ~(ds["categories"].contains("hot dog")))
    :::

4.  To save your dataset, simply run:

    ::: highlight
        newQuery.save_dataset("Cat Dataset") # The argument is the dataset name
    :::

## Next Steps[¶](#next-steps "Permanent link")

Now that we\'ve queried and filtered our dataset, we might want to [add annotations](../../use_cases/annotation/), before we head over to [train our model](../../use_cases/data_engine/train_model/) and [track our experiments](../../use_cases/track_ml_experiments/).

Was this page helpful?

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIwIDEyYTggOCAwIDAgMC04LTggOCA4IDAgMCAwLTggOCA4IDggMCAwIDAgOCA4IDggOCAwIDAgMCA4LThtMiAwYTEwIDEwIDAgMCAxLTEwIDEwQTEwIDEwIDAgMCAxIDIgMTIgMTAgMTAgMCAwIDEgMTIgMmExMCAxMCAwIDAgMSAxMCAxME0xMCA5LjVjMCAuOC0uNyAxLjUtMS41IDEuNVM3IDEwLjMgNyA5LjUgNy43IDggOC41IDhzMS41LjcgMS41IDEuNW03IDBjMCAuOC0uNyAxLjUtMS41IDEuNVMxNCAxMC4zIDE0IDkuNSAxNC43IDggMTUuNSA4czEuNS43IDEuNSAxLjVtLTUgNy43M2MtMS43NSAwLTMuMjktLjczLTQuMTktMS44MUw5LjIzIDE0Yy40NS43MiAxLjUyIDEuMjMgMi43NyAxLjIzczIuMzItLjUxIDIuNzctMS4yM2wxLjQyIDEuNDJjLS45IDEuMDgtMi40NCAxLjgxLTQuMTkgMS44MSIgLz48L3N2Zz4=)

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIwIDEyYTggOCAwIDAgMC04LTggOCA4IDAgMCAwLTggOCA4IDggMCAwIDAgOCA4IDggOCAwIDAgMCA4LThtMiAwYTEwIDEwIDAgMCAxLTEwIDEwQTEwIDEwIDAgMCAxIDIgMTIgMTAgMTAgMCAwIDEgMTIgMmExMCAxMCAwIDAgMSAxMCAxMG0tNi41LTRjLjggMCAxLjUuNyAxLjUgMS41cy0uNyAxLjUtMS41IDEuNS0xLjUtLjctMS41LTEuNS43LTEuNSAxLjUtMS41TTEwIDkuNWMwIC44LS43IDEuNS0xLjUgMS41UzcgMTAuMyA3IDkuNSA3LjcgOCA4LjUgOHMxLjUuNyAxLjUgMS41bTIgNC41YzEuNzUgMCAzLjI5LjcyIDQuMTkgMS44MWwtMS40MiAxLjQyQzE0LjMyIDE2LjUgMTMuMjUgMTYgMTIgMTZzLTIuMzIuNS0yLjc3IDEuMjNsLTEuNDItMS40MkM4LjcxIDE0LjcyIDEwLjI1IDE0IDEyIDE0IiAvPjwvc3ZnPg==)

Thanks for your feedback!

Thanks for your feedback! Help us improve this page by creating an [issue in our Docs repo](https://dagshub.com/DAGsHub-Official/dagshub-docs/issues).