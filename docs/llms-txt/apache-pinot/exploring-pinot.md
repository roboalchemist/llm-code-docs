# Source: https://docs.pinot.apache.org/release-0.4.0/basics/features/exploring-pinot.md

# Source: https://docs.pinot.apache.org/release-0.9.0/basics/components/exploring-pinot.md

# Source: https://docs.pinot.apache.org/release-0.10.0/basics/components/exploring-pinot.md

# Source: https://docs.pinot.apache.org/release-0.11.0/basics/components/exploring-pinot.md

# Source: https://docs.pinot.apache.org/release-0.12.0/basics/components/exploring-pinot.md

# Source: https://docs.pinot.apache.org/release-0.12.1/basics/components/exploring-pinot.md

# Source: https://docs.pinot.apache.org/release-1.0.0/basics/components/exploring-pinot.md

# Source: https://docs.pinot.apache.org/release-1.1.0/basics/components/exploring-pinot.md

# Source: https://docs.pinot.apache.org/release-1.2.0/basics/concepts/components/exploring-pinot.md

# Source: https://docs.pinot.apache.org/release-1.3.0/basics/concepts/components/exploring-pinot.md

# Source: https://docs.pinot.apache.org/release-1.4.0/basics/concepts/components/exploring-pinot.md

# Source: https://docs.pinot.apache.org/basics/concepts/components/exploring-pinot.md

# Pinot Data Explorer

Once you have set up a cluster, you can start exploring the data and the APIs using the Pinot Data Explorer.

Navigate to <http://localhost:9000> in your browser to open the Data Explorer UI.

## Cluster Manager

The first screen that you'll see when you open the Pinot Data Explorer is the Cluster Manager. The Cluster Manager provides a UI to operate and manage your cluster.

![Pinot Cluster Manager](https://459170765-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LtH6nl58DdnZnelPdTc-887967055%2Fuploads%2Ft8mURRDruAI6QxdLMz2J%2FScreenshot%20from%202021-11-25%2010-47-54.png?alt=media\&token=d5653e21-a3bc-404a-b787-1a4f1fd35340)

If you want to view the contents of a server, click on its instance name. You'll then see the following:

![Pinot Server](https://459170765-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LtH6nl58DdnZnelPdTc-887967055%2Fuploads%2Fv18TCnEOqniydObTtGCT%2Fimage.png?alt=media\&token=c19c4c30-9401-44cf-a111-c779e25216f7)

To view the *baseballStats* table, click on its name, which will show the following screen:

![baseballStats Table](https://459170765-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LtH6nl58DdnZnelPdTc-887967055%2Fuploads%2FGwH0aO6ESPKlO3gS5dSE%2Fimage.png?alt=media\&token=d6e8c582-9b96-4e9c-9c8b-e92ab8ba0b8c)

From this screen, we can edit or delete the table, edit or adjust its schema, as well as several other operations.

For example, if we want to add *yearID* to the list of inverted indexes, click on **Edit Table,** add the extra column, and click **Save:**

![Edit Table](https://github.com/pinot-contrib/pinot-docs/blob/latest/.gitbook/assets/edit-baseball-stats-table-config.png)

## Query Console

Let's run some queries on the data in the Pinot cluster. Navigate to [Query Console](http://localhost:9000/#/query) to see the querying interface.

We can see our `baseballStats` table listed on the left (you will see `meetupRSVP` or `airlineStats` if you used the streaming or the hybrid [quick start](https://docs.pinot.apache.org/basics/getting-started/running-pinot-in-docker)). Click on the table name to display all the names along with the data types of the columns of the table.

You can also execute a sample query `select * from baseballStats limit 10` by typing it in the text box and clicking the **Run Query** button.

`Cmd + Enter` can also be used to run the query when focused on the console.

![](https://459170765-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LtH6nl58DdnZnelPdTc%2F-MEkv4Reui1q3pCZv3eG%2F-MEkx7TNGEzYa6TCW6TR%2FPinot_query_console_cropped.png?alt=media\&token=ac2ccb89-1c63-4c50-b7fc-615e42a8590a)

Here are some sample queries you can try:

```sql
select playerName, max(hits) 
from baseballStats 
group by playerName 
order by max(hits) desc
```

```sql
select sum(hits), sum(homeRuns), sum(numberOfGames) 
from baseballStats 
where yearID > 2010
```

```sql
select * 
from baseballStats 
order by league
```

Pinot supports a subset of standard SQL. For more information, see [Pinot Query Language](https://docs.pinot.apache.org/users/user-guide-query/querying-pinot).

## Rest API

The [Pinot Admin UI](http://localhost:9000/help) contains all the APIs that you will need to operate and manage your cluster. It provides a set of APIs for Pinot cluster management including health check, instances management, schema and table management, data segments management.

![](https://459170765-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LtH6nl58DdnZnelPdTc%2F-M1BuoMXn83szIeNCWPT%2F-M1BxN51vPW0p9FFuJCK%2FScreen%20Shot%202020-02-28%20at%2010.00.43%20AM.png?alt=media\&token=283f9390-5d08-4d62-a39f-7746a8cd638c)

Let's check out the tables in this cluster by going to [Table -> List all tables in cluster](http://localhost:9000/help#/Table/listTables), click **Try it out**, and then click **Execute**. We can see the`baseballStats` table listed here. We can also see the exact cURL call made to the controller API.

![List all tables in cluster](https://459170765-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LtH6nl58DdnZnelPdTc-887967055%2Fuploads%2FjZvHBNiaj3QxqUfLGKbx%2Fimage.png?alt=media\&token=91e8c047-83b0-4cbc-ad2c-7faf83ef92e1)

You can look at the configuration of this table by going to [Tables -> Get/Enable/Disable/Drop a table](http://localhost:9000/help#!/Table/alterTableStateOrListTableConfig), click **Try it out**, type `baseballStats` in the table name, and then click **Execute**.

Let's check out the schemas in the cluster by going to [Schema -> List all schemas in the cluster](http://localhost:9000/help#!/Schema/listSchemaNames), click **Try it out**, and then click **Execute**. We can see a schema called `baseballStats` in this list.

![List all schemas in the cluster](https://459170765-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LtH6nl58DdnZnelPdTc-887967055%2Fuploads%2Fs2RDC0IqDvJuMgade8qD%2Fimage.png?alt=media\&token=9164297b-41c4-438e-b507-9d73948f4bca)

Take a look at the schema by going to [Schema -> Get a schema](http://localhost:9000/help#!/Schema/getSchema), click **Try it out**, type `baseballStats` in the schema name, and then click **Execute**.

![baseballStats Schema](https://459170765-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LtH6nl58DdnZnelPdTc-887967055%2Fuploads%2FbKtd5oITNX5mGsM5wMz5%2Fimage.png?alt=media\&token=2bbe9a95-4470-4d2b-837f-05d3568f639b)

Finally, let's check out the data segments in the cluster by going to [Segment -> List all segments](http://localhost:9000/help#!/Segment/getSegments), click **Try it out**, type in `baseballStats` in the table name, and then click **Execute**. There's 1 segment for this table, called `baseballStats_OFFLINE_0`.

To learn how to upload your own data and schema, see [Batch Ingestion](https://docs.pinot.apache.org/manage-data/data-import/batch-ingestion) or [Stream ingestion](https://docs.pinot.apache.org/manage-data/data-import/pinot-stream-ingestion).
