# Source: https://docs.xano.com/the-function-stack/functions/database-requests/external-database-query.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# External Database Query

In Xano, you can connect to the following types of external databases:

* PostgreSQL
* MS SQL
* Oracle
* MySQL
* Snowflake

Add a new function to your function stack that corresponds to the type of database you'd like to connect to. The external connection functions are located under Database Operations.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/_oKnuVg5Nf4VhJM4/images/4e74075f-image.jpeg?fit=max&auto=format&n=_oKnuVg5Nf4VhJM4&q=85&s=1a3c38642312ccbeb0c3012a2ccc5d11" width="1480" height="628" data-path="images/4e74075f-image.jpeg" />
</Frame>

Once you've added your desired connection function, you'll need to define a **connection string**. A connection string is just a URL that contains all of the information we need to connect to your database, such as a hostname or IP address, port, username, and password. We've added an easy to use panel to help you generate a connection string for your database.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/-vy8_DWVOwkWo8Bt/images/88e71409-image.jpeg?fit=max&auto=format&n=-vy8_DWVOwkWo8Bt&q=85&s=8f9f9ddefe11c20abf23fab4ca4b9be2" width="948" height="1132" data-path="images/88e71409-image.jpeg" />
</Frame>

Fill in the required information and click **Save** at the bottom to generate your connection string.

### Dynamic Connection Strings

Connection strings don't have to be static. You can reference **variables** or **inputs** as your connection string, and apply **filters** to dynamically construct them at runtime. This is useful when you need to connect to different databases based on context — for example, routing to a specific tenant's database or switching between environments.

For more information on building a query to run against your database, see our [Direct Database Query documentation](/the-function-stack/functions/database-requests/direct-database-query).


Built with [Mintlify](https://mintlify.com).