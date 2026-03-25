# Source: https://www.apollographql.com/docs/ios/tutorial/tutorial-write-your-first-query.md

# 3. Write your first query

The most common GraphQL operation is the **query**, which requests data from your graph in a structure that conforms to your server's schema. If you return to [the Sandbox](https://studio.apollographql.com/sandbox/explorer?endpoint=https%3A%2F%2Fapollo-fullstack-tutorial.herokuapp.com/graphql)  for your server, you can see available queries in the Schema Reference tab you opened earlier.

Scroll down to the `launches` field to get details about it:

Here, you see both the query term itself, the return type, and information about parameters that can be passed to the query.  You can use this information to write a query you'll eventually add to your app.

To start working with this query in the Sandbox Explorer, select the "play" button to the right side of the information:

This brings you back into Sandbox's Explorer tab with the sidebar on the left showing documentation for the query you've selected:

Notice the small button next to the `launches` icon. Click this button to add the query to the middle "operations" panel:

When the query is added, it will look like this:

Let's break down what you're seeing here:

* The type of the operation, `query`, followed by the name of the operation, currently `Query` (we'll make that more specific in a second), is the outermost set of brackets.
* The next set of brackets contains the query's `selection set`.  In GraphQL, the term `selection set` is the list of fields you want to fetch. Since the `arguments` for this query both have default values, they are not automatically added to the query for you.
* An error in the empty space between the brackets, which is where you'll put the list of information you want back from each launch.

The Apollo iOS SDK requires every query to have a name (even though this isn't required by the GraphQL spec). Since you're going to be creating more than one query, it's also a good idea to give this operation a specific name other than `Query`. Change the name of the operation to `LaunchList`:

Next, on the left hand side, you can select what fields you want back in the returned object. Start by clicking the button next to the `cursor` field. It will mark that field as selected, then insert it into your operations:

This is probably the easiest way to add fields to your object, since it knows how everything is spelled and what type everything is.

However, you can also use auto-complete to help you with this. Add a newline below `cursor` in the Operations panel and start typing `ha`. An autocomplete box pops up and shows you options based on what's in the schema:

The Sandbox Explorer is a great tool for building and verifying queries so you don't have to repeatedly rebuild your project in Xcode to try out changes.

As the schema indicates, the `launches` query returns a `LaunchConnection` object. This object includes a list of launches, along with fields related to pagination (`cursor` and `hasMore`). The query you've written so far indicates exactly which fields of this `LaunchConnection` object you want to be returned.

Run this query by pressing the "Submit Operation" button, which should now have the name of your query, `LaunchList`:

You'll quickly see the query returns results as a JSON object on the right-hand side of the page:

This query executes successfully, but it doesn't include any information about the `launches`! That's because we didn't include the necessary field in the query.

Click the button next to the `launches` field at the bottom of the left column. It will add a set of braces for `launches` to the operations section, and then move the documentation to show information for the `Launch` type:

The fields you add in this set of brackets will be fetched for every launch in the list. Click the buttons next to `id` and `site` properties to add those two fields. When you're done, your operation should look like this:

```graphql title=(Sandbox Explorer)
query LaunchList {
  launches {
    cursor
    hasMore
    launches {
      id
      site
    }
  }
}
```

Run the operation again, and you'll now see that in addition to the information you got back before, you're also getting a list of launches with their ID and site information:

## Add the query to Xcode

Now that your query is fetching the right data, it's time to add the query to Xcode.

1. Right-click the `graphql` directory in the project hierarchy and select **New Empty File**.

2) Name the file `LaunchList.graphql` and add it to the `graphql` directory where your `schema.graphqls` file is. Then, verify the file is not included in the build target and remove it if it is.

3. Copy your final operation from Sandbox Explorer by selecting the three-dot menu to the right of your operation name and then selecting **Copy Operation**:

4) Paste the copied operation into the `LaunchList.graphql` file. Your query file should now look like this:

```graphql title=/graphql/LaunchList.graphql
query LaunchList {
  launches {
    cursor
    hasMore
    launches {
      id
      site
    }
  }
}
```

You now have a query ready to use, in the next step you will be generating the graphql code by [Running code generation.](https://www.apollographql.com/docs/ios/tutorial/tutorial-running-code-generation)
