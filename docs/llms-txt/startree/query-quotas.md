# Source: https://docs.startree.ai/corecapabilities/query_data/advanced_operations/query-quotas.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Query Quotas in Apache Pinot

Apache Pinot supports three types of query-level quotas that work together in a hierarchical system to control query rates and prevent resource exhaustion.

## **Overview of Quota Types**

The three quota types are enforced in hierarchical order, with the **most restrictive (lowest QPS) quota taking precedence**

## **1. Table-Level Quotas**

Table quotas limit QPS for specific tables and have the highest precedence in the hierarchy. This can be specified in the table config as shown in this example:

```json  theme={null}
{
  "tableName": "pinotTable",
  "tableType": "OFFLINE",
  "quota": {
    "maxQueriesPerSecond": 300
  },
  ...
}
```

## **2. Database-Level Quotas**

Database quotas apply to all tables within a specific database and are checked before table quotas. This is typically set in the cluster config as shown below:

```shellscript  theme={null}
curl -X POST \
  'http://localhost:9000/cluster/configs' \
  -d '{
    "databaseMaxQueriesPerSecond" : "1000"
  }'
```

This can also be set using the database API

```shellscript  theme={null}
# to set database specific quota
curl -X POST 'http://localhost:9000/databases/{databaseName}/quotas?maxQueriesPerSecond=1200'
```

## **3. Application-Level Quotas**

Application quotas limit QPS based on the application identifier passed in query options. This can be set in the cluster config as shown below:

```shellscript  theme={null}
curl -X POST \
  'http://localhost:9000/cluster/configs' \
  -d '{
    "applicationMaxQueriesPerSecond" : "1000"
  }'
```

You could also use the API directly:

```shellscript  theme={null}
# to set application's quota
curl -X POST 'http://localhost:9000/applicationQuotas/{applicationName}?maxQueriesPerSecond=1200'
```

In case of application specific quota, you do need to specify the application name in the query as shown:

```javascript  theme={null}
set applicationName='test';
select * from tables
```

For more details on the syntax, how they're imposed - please refer to the Apache Pinot documentation page that describes this in detail: [Query Quotas](https://docs.pinot.apache.org/users/user-guide-query/query-quotas)

## **Example Scenarios**

| **Table Quota** | **Database Quota** | **Application Quota** | **Effective Limit** | **Reason**                  |
| :-------------- | :----------------- | :-------------------- | :------------------ | :-------------------------- |
| 10 QPS          | 25 QPS             | 50 QPS                | **10 QPS**          | Table quota is lowest       |
| 30 QPS          | 15 QPS             | 50 QPS                | **15 QPS**          | Database quota is lowest    |
| 30 QPS          | 25 QPS             | 5 QPS                 | **5 QPS**           | Application quota is lowest |
| Not set         | 25 QPS             | 50 QPS                | **25 QPS**          | Database quota applies      |

Built with [Mintlify](https://mintlify.com).
