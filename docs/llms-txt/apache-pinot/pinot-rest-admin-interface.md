# Source: https://docs.pinot.apache.org/release-0.4.0/users/api/pinot-rest-admin-interface.md

# Source: https://docs.pinot.apache.org/release-0.9.0/users/api/pinot-rest-admin-interface.md

# Source: https://docs.pinot.apache.org/release-0.10.0/users/api/pinot-rest-admin-interface.md

# Source: https://docs.pinot.apache.org/release-0.11.0/users/api/pinot-rest-admin-interface.md

# Source: https://docs.pinot.apache.org/release-0.12.0/users/api/pinot-rest-admin-interface.md

# Source: https://docs.pinot.apache.org/release-0.12.1/users/api/pinot-rest-admin-interface.md

# Source: https://docs.pinot.apache.org/release-1.0.0/for-users/api/pinot-rest-admin-interface.md

# Source: https://docs.pinot.apache.org/release-1.1.0/for-users/api/pinot-rest-admin-interface.md

# Source: https://docs.pinot.apache.org/release-1.2.0/for-users/api/pinot-rest-admin-interface.md

# Source: https://docs.pinot.apache.org/release-1.3.0/for-users/api/pinot-rest-admin-interface.md

# Source: https://docs.pinot.apache.org/release-1.4.0/for-users/api/pinot-rest-admin-interface.md

# Source: https://docs.pinot.apache.org/users/api/pinot-rest-admin-interface.md

# Controller Admin API

The [Pinot Admin UI](http://localhost:9000/help) contains all the APIs that you will need to operate and manage your cluster. It provides a set of APIs for Pinot cluster management including health check, instances management, schema and table management, data segments management.

Note: The controller API's are primarily for admin tasks. Even though the UI console queries Pinot when running queries from the query console, use the [Broker Query API](https://docs.pinot.apache.org/users/api/querying-pinot-using-standard-sql) for querying Pinot.

![](https://459170765-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LtH6nl58DdnZnelPdTc%2F-M1BuoMXn83szIeNCWPT%2F-M1BxN51vPW0p9FFuJCK%2FScreen%20Shot%202020-02-28%20at%2010.00.43%20AM.png?alt=media\&token=283f9390-5d08-4d62-a39f-7746a8cd638c)

Let's check out the tables in this cluster by going to [Table -> List all tables in cluster](http://localhost:9000/help#!/Table/listTableConfigs) and click on `Try it out!`. We can see the `baseballStats` table listed here. We can also see the exact `curl` call made to the controller API.

![List all tables in cluster](https://459170765-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LtH6nl58DdnZnelPdTc-887967055%2Fuploads%2FjZvHBNiaj3QxqUfLGKbx%2Fimage.png?alt=media\&token=91e8c047-83b0-4cbc-ad2c-7faf83ef92e1)

You can look at the configuration of this table by going to [Tables -> Get/Enable/Disable/Drop a table](http://localhost:9000/help#!/Table/alterTableStateOrListTableConfig), type in `baseballStats` in the table name, and click `Try it out!`

Let's check out the schemas in the cluster by going to [Schema -> List all schemas in the cluster](http://localhost:9000/help#!/Schema/listSchemaNames) and click `Try it out!`. We can see a schema called `baseballStats` in this list.

![List all schemas in the cluster](https://459170765-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LtH6nl58DdnZnelPdTc-887967055%2Fuploads%2Fs2RDC0IqDvJuMgade8qD%2Fimage.png?alt=media\&token=9164297b-41c4-438e-b507-9d73948f4bca)

Take a look at the schema by going to [Schema -> Get a schema](http://localhost:9000/help#!/Schema/getSchema), type `baseballStats` in the schema name, and click `Try it out!`.

```
{
  "schemaName": "baseballStats",
  "dimensionFieldSpecs": [
    {
      "name": "playerID",
      "dataType": "STRING"
    },
    {
      "name": "yearID",
      "dataType": "INT"
    },
    {
      "name": "teamID",
      "dataType": "STRING"
    },
    {
      "name": "league",
      "dataType": "STRING"
    },
    {
      "name": "playerName",
      "dataType": "STRING"
    }
  ],
  "metricFieldSpecs": [
    {
      "name": "playerStint",
      "dataType": "INT"
    },
    {
      "name": "numberOfGames",
      "dataType": "INT"
    },
    {
      "name": "numberOfGamesAsBatter",
      "dataType": "INT"
    },
    {
      "name": "AtBatting",
      "dataType": "INT"
    },
    {
      "name": "runs",
      "dataType": "INT"
    },
    {
      "name": "hits",
      "dataType": "INT"
    },
    {
      "name": "doules",
      "dataType": "INT"
    },
    {
      "name": "tripples",
      "dataType": "INT"
    },
    {
      "name": "homeRuns",
      "dataType": "INT"
    },
    {
      "name": "runsBattedIn",
      "dataType": "INT"
    },
    {
      "name": "stolenBases",
      "dataType": "INT"
    },
    {
      "name": "caughtStealing",
      "dataType": "INT"
    },
    {
      "name": "baseOnBalls",
      "dataType": "INT"
    },
    {
      "name": "strikeouts",
      "dataType": "INT"
    },
    {
      "name": "intentionalWalks",
      "dataType": "INT"
    },
    {
      "name": "hitsByPitch",
      "dataType": "INT"
    },
    {
      "name": "sacrificeHits",
      "dataType": "INT"
    },
    {
      "name": "sacrificeFlies",
      "dataType": "INT"
    },
    {
      "name": "groundedIntoDoublePlays",
      "dataType": "INT"
    },
    {
      "name": "G_old",
      "dataType": "INT"
    }
  ]
}
```

Finally, let's checkout the data segments in the cluster by going to [List all segments](http://localhost:9000/help#!/Segment/getSegments), type in `baseballStats` in the table name, and click `Try it out!`. There's 1 segment for this table, called `baseballStats_OFFLINE_0`.

You might have figured out by now, in order to get data into the Pinot cluster, we need a table, a schema and segments. Let's head over to [Batch upload sample data](https://docs.pinot.apache.org/basics/getting-started/pushing-your-data-to-pinot), to find out more about these components and learn how to create them for your own data.
