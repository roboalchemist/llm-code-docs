# Source: https://docs.xano.com/the-function-stack/functions/database-requests/direct-database-query.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Direct Database Query

<Tip>
  The Direct Database Query function is available starting on the **upgraded** (non-Legacy) Launch or Scale plans. If you have any questions, please reach out to support.
</Tip>

To access the Direct Database Query function, add a new function to your function stack, choose Database Operations, and then Direct Database Query.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/kUGpIho8LJSMl5Gv/images/34b0fc67-image.jpeg?fit=max&auto=format&n=kUGpIho8LJSMl5Gv&q=85&s=a77649278d26492b009acc507e616ad1" width="1400" height="638" data-path="images/34b0fc67-image.jpeg" />
</Frame>

From the Direct Database Query panel, you can provide the following:

* **Code** - This is the query you would like to perform
* [**Statement Args**](/the-function-stack/functions/database-requests/direct-database-query#statement-arguments) - If you specify arguments using \*\*? \*\*in your code, you can use this section to sequentially fill in those arguments with other data, such as variables or inputs previously defined in your function stack
* **Response Type** - Return either a single item, or a list of items
* **Output Variable** - The name of the variable that will contain the result of the query

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/RVHCrB1RJjFkWEmQ/images/125ad958-image.jpeg?fit=max&auto=format&n=RVHCrB1RJjFkWEmQ&q=85&s=4d8c03cdb0248fe528716de6e9ea15f2" width="894" height="854" data-path="images/125ad958-image.jpeg" />
</Frame>

### Finding your database identifier

The database identifier can be found by combining the workspace ID and database table ID with 'mvpw'.

For example: If workspace ID = 1 and ID = 3: `mvpw1_3` If workspace ID = 500 and table ID = 3913: `mvpw500_3913`

Using the mvpw selector will return two columns: id and xdo, with xdo containing each record's content. For SELECT statements where you want to return specific columns, use 'x' instead.

You can also use an **x identifier**, such as x1\_3, to return a more readable view of the data. Please note, however, that these views do not always have function parity with working with the mvpw\_ version of your tables (such as when performing inserts).

Using **x\_** is typically best when just performing queries.

<Frame caption="Where to find your table ID and workspace ID">
  <img src="https://mintcdn.com/xano-997cb9ee/_oKnuVg5Nf4VhJM4/images/51435fa3-image.jpeg?fit=max&auto=format&n=_oKnuVg5Nf4VhJM4&q=85&s=16ae715673d6fd08391765dd0509f9d4" width="564" height="640" data-path="images/51435fa3-image.jpeg" />
</Frame>

<Info>
  Direct Database Query allows you to query tables across your Instance. For example, if you are in workspace 2, you can query a table from workspace 1 using the above syntax. Please do so carefully to not misuse sensitive data in a query.
</Info>

### Using Custom Aliases

You can leverage custom view aliases to make direct database queries easier to write, and more readable, based on exactly the data that you need.

Head to your database table, and create a [custom view](/the-database/database-basics/database-views). When creating your custom view, you can provide a **Database View Alias**, which you can use in your Direct Database Query statement.

In the screenshot below, we've created a database view to filter people named David in our people table. When saving the view, we're providing an alias called 'david'.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/NAqNmVIgcJlXegps/images/0954bc17-image.jpeg?fit=max&auto=format&n=NAqNmVIgcJlXegps&q=85&s=1f0693a28149b538e65d71b49ac67884" width="2067" height="599" data-path="images/0954bc17-image.jpeg" />
</Frame>

Once this view is saved, we can utilize it in a Direct Database Query function to retrieve the data from that view. The view is listed when using the Direct Query wizard, or you can type it manually if you are writing a query from scratch as `SELECT * from "view_name";`

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/kUGpIho8LJSMl5Gv/images/3c11a810-image.jpeg?fit=max&auto=format&n=kUGpIho8LJSMl5Gv&q=85&s=7c20be0d95616ecf150c6f0a7e3f3f44" width="1533" height="430" data-path="images/3c11a810-image.jpeg" />
</Frame>

### Test Data

Assuming our data source is named 'test', mvpw599\_2377 would become mvpw599\_test\_2377. You can replace 'test' in this example with the name of your data source.

Direct Database Query does not respond to the selection of your data source in Xano or the data source specified in any external requests. You need to specifically state the test data source in the function. It is not possible at this time to dynamically modify the table selector.

### Statement Arguments

Statement arguments enable dynamic values in your queries. Statement arguments are designed to come from variables, inputs, or environment variables. A `?`\*\* \*\*in the query will identify where a statement argument should be placed; they will be placed in sequential order.

Statement arguments are escaped with single quotes by default. In situations where you want to escape the argument value with double quotes, use `?:alias`. To insert an argument value with no quotes, such as a table name, use `?:raw`.

| Argument Type | Query Syntax | Result    |
| ------------- | ------------ | --------- |
| Default       | `?`          | 'example' |
| Alias         | `?:alias`    | "example" |
| Raw           | `?:raw`      | example   |

#### Example:

In the following query, there are two statement arguments. The input `search` will be placed at the first `?` and the variable `var_1` will be placed at the second `?`.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/dC3SQWgPCF_-1qn6/images/28a9a0fb-image.jpeg?fit=max&auto=format&n=dC3SQWgPCF_-1qn6&q=85&s=91acdc3581d2e99005b9fc049deed8c7" width="594" height="756" data-path="images/28a9a0fb-image.jpeg" />
</Frame>

<Info>
  Arguments can not, at this time, be anything other than single values. Arguments can not also replace functions; they can only serve as query values at this time.
</Info>

<Warning>
  **PREVENTING SQL INJECTION ATTACKS**

  Xano offers some filters to help ensure that any dynamic / user input is not parsed in a way that might harm your database or cause other unintended consequences.

  Make sure to process your inputs **before** they are used in any SQL queries with the appropriate filter.

  These filters are [sql\_alias and sql\_esc](/the-function-stack/filters/text#sql_alias)
</Warning>

### SQL Query Wizard

The SQL Query Wizard generates simple SQL queries. **It is not designed to support complex statements or joins but basic statements** to help get you started.

<Frame caption="Open the Wizard Panel">
  <img src="https://mintcdn.com/xano-997cb9ee/o7zunZFYmjx8RZ8N/images/f6d9455c-image.jpeg?fit=max&auto=format&n=o7zunZFYmjx8RZ8N&q=85&s=e576918b92253ee3384263c8edb09605" width="597" height="865" data-path="images/f6d9455c-image.jpeg" />
</Frame>

#### Step 1: Choose the Database Table to Query

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/kUGpIho8LJSMl5Gv/images/362ea809-image.jpeg?fit=max&auto=format&n=kUGpIho8LJSMl5Gv&q=85&s=0e20e9888f6d9e0371d7e3d1ec824aa9" width="402" height="413" data-path="images/362ea809-image.jpeg" />
</Frame>

#### Step 2: Choose the field

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/p57kHPQ04p_0aEqF/images/b03e61b9-image.jpeg?fit=max&auto=format&n=p57kHPQ04p_0aEqF&q=85&s=f9dcdc3b483d0b7fd9054a12751eb45c" width="397" height="444" data-path="images/b03e61b9-image.jpeg" />
</Frame>

#### Step 3: Choose an operator and value.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/tjSJ_pOzk8E0WRhF/images/c60c8973-image.jpeg?fit=max&auto=format&n=tjSJ_pOzk8E0WRhF&q=85&s=6bebbeeb26c15e7f4137774e6bec7fbf" width="398" height="442" data-path="images/c60c8973-image.jpeg" />
</Frame>

Choose an operator for the query and add a value. Optionally include multiple conditions with AND or OR statements.

#### Step 4: Select the columns to include in the query response.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/RVHCrB1RJjFkWEmQ/images/0bb09b20-image.jpeg?fit=max&auto=format&n=RVHCrB1RJjFkWEmQ&q=85&s=0e603c24fbb0340d7cd09d5e1758ecbc" width="393" height="414" data-path="images/0bb09b20-image.jpeg" />
</Frame>

The Wizard will process the settings and generate a SQL query in the code editor.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/ClU5W_-qt6GI3QWZ/images/4533efd6-image.jpeg?fit=max&auto=format&n=ClU5W_-qt6GI3QWZ&q=85&s=60d1e0c2c1b732f83d00d96d46f0873e" width="594" height="595" data-path="images/4533efd6-image.jpeg" />
</Frame>

The result returns a list from merchant where desc = Pizza.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/o7zunZFYmjx8RZ8N/images/f6b193b1-image.jpeg?fit=max&auto=format&n=o7zunZFYmjx8RZ8N&q=85&s=50eae715edfa6fd9e310904b2f95351c" width="589" height="449" data-path="images/f6b193b1-image.jpeg" />
</Frame>

### What's the difference between Direct Database Query and Direct Database Access?

Direct Database Access is a premium add-on that allows you to connect directly to your Xano PostgreSQL database using an external tool. If you would like to leverage something outside of Xano to manage your database, direct database access is the feature you're looking for.

The Direct Database Query function in Xano is available if you want to simply run SQL queries from inside Xano.

## Using the AI SQL Assistant

<Steps>
  <Step title="When using the Direct Database Query function, click 'SQL Assistant to access the AI SQL assistant.">
    [Direct Database Query](/the-function-stack/functions/database-requests/direct-database-query)

    <Frame>
      <img src="https://mintcdn.com/xano-997cb9ee/_oKnuVg5Nf4VhJM4/images/4eaec823-image.jpeg?fit=max&auto=format&n=_oKnuVg5Nf4VhJM4&q=85&s=16b03c8773fff19df121a0ab3840becd" width="156" height="62" data-path="images/4eaec823-image.jpeg" />
    </Frame>

    The assistant can help you write queries against your Xano database.
  </Step>

  <Step title="Provide the assistant with the query you would like it to build.">
    <Frame>
      <img src="https://mintcdn.com/xano-997cb9ee/SGxJ0muPK3um9hNH/images/757a3322-image.jpeg?fit=max&auto=format&n=SGxJ0muPK3um9hNH&q=85&s=fc9e5035cfea683d9eefa59e55b08c10" width="946" height="204" data-path="images/757a3322-image.jpeg" />
    </Frame>
  </Step>

  <Step title="Once complete, the assistant will present you with the query, along with an explanation of how it works and some records that satisfy the query.">
    <Frame>
      <img src="https://mintcdn.com/xano-997cb9ee/Qia2QBMIuWWrGb-s/images/22cc94f1-image.jpeg?fit=max&auto=format&n=Qia2QBMIuWWrGb-s&q=85&s=787bd1f048c1c2e2df10503b8d8a5889" width="2304" height="1674" data-path="images/22cc94f1-image.jpeg" />
    </Frame>
  </Step>

  <Step title="If the query returns the expected results, click Update SQL. Otherwise, you can ask the assistant to make any desired modifications or fixes.">
    You can also make your own modifications to the query, such as adding ? characters to represent dynamic values.
  </Step>
</Steps>


Built with [Mintlify](https://mintlify.com).