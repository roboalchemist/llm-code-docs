# Source: https://docs.snowflake.com/en/user-guide/cost-attributing.md

# Attributing cost

An organization can apportion the cost of using Snowflake to logical units within the organization (for example, to different
departments, environments, or projects). This chargeback or showback model is useful for accounting purposes and pinpoints
areas of the organization that could benefit from controls and optimizations that can reduce costs.

To attribute costs to different groups like departments or projects, use the following recommended approach:

* Use [object tags](object-tagging/introduction.md) to associate resources and users with departments or projects.
* Use [query tags](../sql-reference/parameters.md) to associate individual queries with departments or projects when the queries are
  made by the same application on behalf of users belonging to multiple departments.

## Types of cost attribution scenarios

The following cost attribution scenarios are the most commonly encountered. In these scenarios, warehouses are used as an
example of a resource that incurs costs.

* **Resources used exclusively by a single cost center or department:** An example of this is using object tags to associate
  warehouses with a department. You can use these object tags to attribute the costs incurred by those warehouses to that
  department entirely.
* **Resources that are shared by users from multiple departments:** An example of this is a warehouse shared by users from
  different departments. In this case, you use object tags to associate each user with a department. The costs of queries are
  attributed to the users. Using the object tags assigned to users, you can break down the costs by department.
* **Applications or workflows shared by users from different departments:** An example of this is an application that issues
  queries on behalf of its users. In this case, each query executed by the application is assigned a query tag that identifies
  the team or cost center of the user on whose behalf the query is being made.

The next sections explain how to set up object tags in your accounts and provide the details for each of these cost attribution
scenarios.

## Setting up object tags for cost attribution

When you set up tags to represent the groupings that you want to use for cost attribution, you should determine if the
groupings apply to a single account or multiple accounts. This determines how you set up your tags.

For example, suppose that you want to attribute costs based on department.

* If the resources used by the department are located in a single account, you create the tags in a database in that account.
* If the resources used by the department span multiple accounts, you create the tags
  in a key account in your organization (for example, in your [organization account](organization-accounts.md)),
  and you make those tags available in other accounts through replication.

The next sections explain how to create the tags, replicate the tags, and apply the tags to resources.

* Creating the tags
* Replicating the tag database
* Tagging the resources and users

> **Note:**
>
> The examples in these sections use the custom role `tag_admin`, which is assumed to have been granted the privileges to
> create and manage tags. Within your organization, you can use more granular
> [privileges for object tagging](object-tagging/work.md) to develop a secure tagging strategy.

### Creating the tags

As part of designing the strategy, decide on the database and schema where you plan to create the tags.

* You can create a dedicated database and schema for the tags.
* If you want to tag resources in different accounts across your organization, you can create the tags in a key account in your
  organization (for example, in your [organization account](organization-accounts.md)).

The following example creates a database named `cost_management` and a schema named `tags` for the tags that you plan to use:

```sqlexample
USE ROLE tag_admin;

CREATE DATABASE cost_management;
CREATE SCHEMA tags;
```

With `cost_management` and `tags` selected as the current database and schema, create a tag named `cost_center` and set
the values allowed for the tag to the names of cost centers:

```sqlexample
CREATE TAG cost_center
  ALLOWED_VALUES 'finance', 'marketing', 'engineering', 'product';
```

### Replicating the tag database

If you have an organization with multiple accounts and you want to make the tags available in these other accounts,
[set up your accounts for replication](account-replication-config.md), and
[create a replication group](../sql-reference/sql/create-replication-group.md) in a main account (for example, in the
[organization account](organization-accounts.md)). Set up this replication group to replicate the database
containing the tags.

For example, to replicate the tags to the accounts named `my_org.my_account` and `my_org.my_account_2`, execute this
statement in your organization account:

```sqlexample
CREATE REPLICATION GROUP cost_management_repl_group
  OBJECT_TYPES = DATABASES
  ALLOWED_DATABASES = cost_management
  ALLOWED_ACCOUNTS = my_org.my_account_1, my_org.my_account_2
  REPLICATION_SCHEDULE = '10 MINUTE';
```

Then, in each account in which you want to make the tags available, create a secondary replication group, and refresh this
group from the primary group:

```sqlexample
CREATE REPLICATION GROUP cost_management_repl_group
  AS REPLICA OF my_org.my_org_account.cost_management_repl_group;

ALTER REPLICATION GROUP cost_management_repl_group REFRESH;
```

### Tagging the resources and users

After creating and replicating the tags, you can use these tags to identify the warehouses and users belonging to each
department. For example, because the sales department uses both `warehouse1` and `warehouse2`, you can set the
`cost_center` tag to `'SALES'` for both warehouses.

> **Tip:**
>
> Ideally, you should have workflows that automate the process of applying these tags when you create resources and users.

```sqlexample
USE ROLE tag_admin;

ALTER WAREHOUSE warehouse1 SET TAG cost_management.tags.cost_center='SALES';
ALTER WAREHOUSE warehouse2 SET TAG cost_management.tags.cost_center='SALES';
ALTER WAREHOUSE warehouse3 SET TAG cost_management.tags.cost_center='FINANCE';

ALTER USER finance_user SET TAG cost_management.tags.cost_center='FINANCE';
ALTER USER sales_user SET TAG cost_management.tags.cost_center='SALES';
```

## Viewing cost by tag in SQL

You can attribute costs within an account or across accounts in an organization:

* **Attributing costs within an account**

  You can attribute costs within an account by querying the following views in the
  [ACCOUNT_USAGE](../sql-reference/account-usage.md) schema:

  * [TAG_REFERENCES view](../sql-reference/account-usage/tag_references.md): Identifies objects (for example, warehouses and users) that have tags.
  * [WAREHOUSE_METERING_HISTORY view](../sql-reference/account-usage/warehouse_metering_history.md): Provides credit usage for warehouses.
  * [QUERY_ATTRIBUTION_HISTORY view](../sql-reference/account-usage/query_attribution_history.md): Provides the compute costs for queries. The cost per query is
    the warehouse credit usage for executing the query.

    For more information on using this view, see About the QUERY_ATTRIBUTION_HISTORY view.
* **Attributing costs across accounts in an organization**

  Within an organization, you can also attribute costs for resources that are used **exclusively by a single department** by
  querying views in the [ORGANIZATION_USAGE](../sql-reference/organization-usage.md) schema from the
  [organization account](organization-accounts.md).

  > **Note:**
  > * In the ORGANIZATION_USAGE schema, the TAG_REFERENCES view is only available in the organization account.
  > * The QUERY_ATTRIBUTION_HISTORY view is only available in the ACCOUNT_USAGE schema for an account. There is no
  >   organization-wide equivalent of the view.

The next sections explain how to attribute costs for some of the
common cost-attribution scenarios:

* Resources not shared by departments
* Resources shared by users from different departments
* Resources used by applications that need to attribute costs to different departments

### Resources not shared by departments

Suppose that you want to attribute costs by department and that each department uses a set of dedicated warehouses.

If you tag warehouses with a `cost_center` tag to identify the department that owns the warehouse, you can join the
ACCOUNT_USAGE [TAG_REFERENCES view](../sql-reference/account-usage/tag_references.md) with the
[WAREHOUSE_METERING_HISTORY view](../sql-reference/account-usage/warehouse_metering_history.md) on the `object_id` and `warehouse_id` columns to get usage
information by warehouse, and you can use the `tag_value` column to identify the departments that own those warehouses.

The following SQL statement performs this join:

```sqlexample
SELECT
    TAG_REFERENCES.tag_name,
    COALESCE(TAG_REFERENCES.tag_value, 'untagged') AS tag_value,
    SUM(WAREHOUSE_METERING_HISTORY.credits_used_compute) AS total_credits
  FROM
    SNOWFLAKE.ACCOUNT_USAGE.WAREHOUSE_METERING_HISTORY
      LEFT JOIN SNOWFLAKE.ACCOUNT_USAGE.TAG_REFERENCES
        ON WAREHOUSE_METERING_HISTORY.warehouse_id = TAG_REFERENCES.object_id
          AND TAG_REFERENCES.domain = 'WAREHOUSE'
  WHERE
    WAREHOUSE_METERING_HISTORY.start_time >= DATE_TRUNC('MONTH', DATEADD(MONTH, -1, CURRENT_DATE))
      AND WAREHOUSE_METERING_HISTORY.start_time < DATE_TRUNC('MONTH',  CURRENT_DATE)
  GROUP BY TAG_REFERENCES.tag_name, COALESCE(TAG_REFERENCES.tag_value, 'untagged')
  ORDER BY total_credits DESC;
```

```output
+-------------+-------------+-----------------+
| TAG_NAME    | TAG_VALUE   |   TOTAL_CREDITS |
|-------------+-------------+-----------------|
| NULL        | untagged    |    20.360277159 |
| COST_CENTER | Sales       |    17.173333333 |
| COST_CENTER | Finance     |      8.14444444 |
+-------------+-------------+-----------------+
```

You can run a similar query to perform the same attribution for all the accounts in your organization using views in the
ORGANIZATION_USAGE schema from the [organization account](organization-accounts.md). The rest of the query
does not change.

```sqlexample
SELECT
    TAG_REFERENCES.tag_name,
    COALESCE(TAG_REFERENCES.tag_value, 'untagged') AS tag_value,
    SUM(WAREHOUSE_METERING_HISTORY.credits_used_compute) AS total_credits
  FROM
    SNOWFLAKE.ORGANIZATION_USAGE.WAREHOUSE_METERING_HISTORY
      LEFT JOIN SNOWFLAKE.ORGANIZATION_USAGE.TAG_REFERENCES
        ON WAREHOUSE_METERING_HISTORY.warehouse_id = TAG_REFERENCES.object_id
          AND TAG_REFERENCES.domain = 'WAREHOUSE'
          AND tag_database = 'COST_MANAGEMENT' AND tag_schema = 'TAGS'
  WHERE
    WAREHOUSE_METERING_HISTORY.start_time >= DATE_TRUNC('MONTH', DATEADD(MONTH, -1, CURRENT_DATE))
      AND WAREHOUSE_METERING_HISTORY.start_time < DATE_TRUNC('MONTH',  CURRENT_DATE)
  GROUP BY TAG_REFERENCES.tag_name, COALESCE(TAG_REFERENCES.tag_value, 'untagged')
  ORDER BY total_credits DESC;
```

### Resources shared by users from different departments

Suppose that users in different departments share the same warehouses and you want to break down the credits used by each
department. You can tag the users with a `cost_center` tag to identify the department that they belong to, and you can join
the [TAG_REFERENCES view](../sql-reference/account-usage/tag_references.md) with the [QUERY_ATTRIBUTION_HISTORY view](../sql-reference/account-usage/query_attribution_history.md).

> **Note:**
>
> You can only get this data for a single account at a time. You cannot execute a query that retrieves this data across
> accounts in an organization.

The next sections provide examples of SQL statements for attributing costs for shared resources.

* Calculating the cost of user queries for the last month
* Calculating the cost of user queries by department without idle time
* Calculating the cost of queries by users without idle time
* Calculating the cost of queries by users without tags

#### Calculating the cost of user queries for the last month

This following SQL statement calculates the costs for the last month.

In this example, idle time is distributed among the users in proportion to their usage.

```sqlexample
WITH
  wh_bill AS (
    SELECT SUM(credits_used_compute) AS compute_credits
      FROM SNOWFLAKE.ACCOUNT_USAGE.WAREHOUSE_METERING_HISTORY
      WHERE start_time >= DATE_TRUNC('MONTH', CURRENT_DATE)
        AND start_time < CURRENT_DATE
  ),
  user_credits AS (
    SELECT user_name, SUM(credits_attributed_compute) AS credits
      FROM SNOWFLAKE.ACCOUNT_USAGE.QUERY_ATTRIBUTION_HISTORY
      WHERE start_time >= DATE_TRUNC('MONTH', CURRENT_DATE)
        AND start_time < CURRENT_DATE
      GROUP BY user_name
  ),
  total_credit AS (
    SELECT SUM(credits) AS sum_all_credits
    FROM user_credits
  )
SELECT
    u.user_name,
    u.credits / t.sum_all_credits * w.compute_credits AS attributed_credits
  FROM user_credits u, total_credit t, wh_bill w
  ORDER BY attributed_credits DESC;
```

```output
+-----------+--------------------+
| USER_NAME | ATTRIBUTED_CREDITS |
|-----------+--------------------+
| FINUSER   | 6.603575468        |
| SALESUSER | 4.321378049        |
| ENGUSER   | 0.6217131392       |
|-----------+--------------------+
```

#### Calculating the cost of user queries by department without idle time

The following example attributes the compute cost to each department through the queries executed by users in that department.
This query depends on the user objects having a tag that identifies their department.

```sqlexample
WITH joined_data AS (
  SELECT
      tr.tag_name,
      tr.tag_value,
      qah.credits_attributed_compute,
      qah.start_time
    FROM SNOWFLAKE.ACCOUNT_USAGE.TAG_REFERENCES tr
      JOIN SNOWFLAKE.ACCOUNT_USAGE.QUERY_ATTRIBUTION_HISTORY qah
        ON tr.domain = 'USER' AND tr.object_name = qah.user_name
)
SELECT
    tag_name,
    tag_value,
    SUM(credits_attributed_compute) AS total_credits
  FROM joined_data
  WHERE start_time >= DATEADD(MONTH, -1, CURRENT_DATE)
    AND start_time < CURRENT_DATE
  GROUP BY tag_name, tag_value
  ORDER BY tag_name, tag_value;
```

```output
+-------------+-------------+-----------------+
| TAG_NAME    | TAG_VALUE   |   TOTAL_CREDITS |
|-------------+-------------+-----------------|
| COST_CENTER | engineering |   0.02493688426 |
| COST_CENTER | finance     |    0.2281084988 |
| COST_CENTER | marketing   |    0.3686840545 |
|-------------+-------------+-----------------|
```

#### Calculating the cost of queries by users without idle time

This following SQL statement calculates the costs per user for the past month (excluding idle time).

```sqlexample
SELECT user_name, SUM(credits_attributed_compute) AS credits
  FROM SNOWFLAKE.ACCOUNT_USAGE.QUERY_ATTRIBUTION_HISTORY
  WHERE
    start_time >= DATEADD(MONTH, -1, CURRENT_DATE)
    AND start_time < CURRENT_DATE
  GROUP BY user_name;
```

```output
+-----------+--------------------+
| USER_NAME | ATTRIBUTED_CREDITS |
|-----------+--------------------|
| JSMITH    |       17.173333333 |
| MJONES    |         8.14444444 |
| SYSTEM    |         5.33985393 |
+-----------+--------------------+
```

#### Calculating the cost of queries by users without tags

The following example calculates the cost of queries by users who are not tagged. You can use this to verify that tags are
being applied consistently to users.

```sqlexample
SELECT qah.user_name, SUM(qah.credits_attributed_compute) as total_credits
  FROM
    SNOWFLAKE.ACCOUNT_USAGE.QUERY_ATTRIBUTION_HISTORY qah
    LEFT JOIN snowflake.account_usage.tag_references tr
    ON qah.user_name = tr.object_name AND tr.DOMAIN = 'USER'
  WHERE
    start_time >= dateadd(month, -1, current_date)
    AND qah.user_name IS NULL OR tr.object_name IS NULL
  GROUP BY qah.user_name
  ORDER BY total_credits DESC;
```

```output
+------------+---------------+
| USER_NAME  | TOTAL_CREDITS |
|------------+---------------|
| RSMITH     |  0.1830555556 |
+------------+---------------+
```

### Resources used by applications that need to attribute costs to different departments

The examples in this section calculate the costs for one or more applications that are powered by Snowflake.

The examples assume that these applications set query tags that identify the application for all queries executed. To set the
query tag for queries in a session, execute the [ALTER SESSION](../sql-reference/sql/alter-session.md) command. For example:

```sqlexample
ALTER SESSION SET QUERY_TAG = 'COST_CENTER=finance';
```

This associates the `COST_CENTER=finance` tag with all subsequent queries executed during the session.

You can then use the query tag to trace back the cost incurred by these queries to the appropriate departments.

The next sections provide examples of using this approach.

* Calculating the cost of queries by department
* Calculating the cost of queries (excluding idle time) by query tag
* Calculating the cost of queries (including idle time) by query tag

#### Calculating the cost of queries by department

The following example calculates the compute credits and the credits used for the
[query acceleration service](query-acceleration-service.md) for the finance department. This depends on the
`COST_CENTER=finance` query tag being applied to the original queries that were executed.

Note that the costs exclude idle time.

```sqlexample
SELECT
    query_tag,
    SUM(credits_attributed_compute) AS compute_credits,
    SUM(credits_used_query_acceleration) AS qas
  FROM SNOWFLAKE.ACCOUNT_USAGE.QUERY_ATTRIBUTION_HISTORY
  WHERE query_tag = 'COST_CENTER=finance'
  GROUP BY query_tag;
```

```output
+---------------------+-----------------+------+
| QUERY_TAG           | COMPUTE_CREDITS | QAS  |
|---------------------+-----------------|------|
| COST_CENTER=finance |      0.00576115 | null |
+---------------------+-----------------+------+
```

#### Calculating the cost of queries (excluding idle time) by query tag

The following example calculates the cost of queries by query tag and includes queries without tags (identified as “untagged”).

```sqlexample
SELECT
    COALESCE(NULLIF(query_tag, ''), 'untagged') AS tag,
    SUM(credits_attributed_compute) AS compute_credits,
    SUM(credits_used_query_acceleration) AS qas
  FROM SNOWFLAKE.ACCOUNT_USAGE.QUERY_ATTRIBUTION_HISTORY
  WHERE start_time >= DATEADD(MONTH, -1, CURRENT_DATE)
  GROUP BY tag
  ORDER BY compute_credits DESC;
```

```output
+-------------------------+-----------------+------+
| TAG                     | COMPUTE_CREDITS | QAS  |
|-------------------------+-----------------+------+
| untagged                | 3.623173449     | null |
| COST_CENTER=engineering | 0.531431948     | null |
|-------------------------+-----------------+------+
```

#### Calculating the cost of queries (including idle time) by query tag

The following example distributes the idle time that is not captured in the per-query cost across departments in proportion
to their usage of the warehouse.

```sqlexample
WITH
  wh_bill AS (
    SELECT SUM(credits_used_compute) AS compute_credits
      FROM SNOWFLAKE.ACCOUNT_USAGE.WAREHOUSE_METERING_HISTORY
      WHERE start_time >= DATE_TRUNC('MONTH', CURRENT_DATE)
      AND start_time < CURRENT_DATE
  ),
  tag_credits AS (
    SELECT
        COALESCE(NULLIF(query_tag, ''), 'untagged') AS tag,
        SUM(credits_attributed_compute) AS credits
      FROM SNOWFLAKE.ACCOUNT_USAGE.QUERY_ATTRIBUTION_HISTORY
      WHERE start_time >= DATEADD(MONTH, -1, CURRENT_DATE)
      GROUP BY tag
  ),
  total_credit AS (
    SELECT SUM(credits) AS sum_all_credits
      FROM tag_credits
  )
SELECT
    tc.tag,
    tc.credits / t.sum_all_credits * w.compute_credits AS attributed_credits
  FROM tag_credits tc, total_credit t, wh_bill w
  ORDER BY attributed_credits DESC;
```

```output
+-------------------------+--------------------+
| TAG                     | ATTRIBUTED_CREDITS |
+-------------------------+--------------------|
| untagged                |        9.020031304 |
| COST_CENTER=finance     |        1.027742521 |
| COST_CENTER=engineering |        1.018755812 |
| COST_CENTER=marketing   |       0.4801370376 |
+-------------------------+--------------------+
```

## Viewing cost by tag in Snowsight

You can attribute costs by reporting on the use of resources that have the `cost_center` tag. You can access this data in
[Snowsight](ui-snowsight-gs.md).

1. Switch to a role that has [access to the ACCOUNT_USAGE schema](../sql-reference/account-usage.md).
2. In the navigation menu, select Admin » Cost management.
3. Select Consumption.
4. From the Tags drop-down, select the `cost_center` tag.
5. To focus on a specific cost center, select a value from the list of the tag’s values.
6. Select Apply.

For more details about filtering in Snowsight, see [Filter by tag](cost-exploring-compute.md).

## About the QUERY_ATTRIBUTION_HISTORY view

You can use the [QUERY_ATTRIBUTION_HISTORY view](../sql-reference/account-usage/query_attribution_history.md) to attribute cost based on queries. The cost per
query is the warehouse credit usage for executing the query. This cost does not include any other credit usage that is incurred
as a result of query execution. For example, the following are not included in the query cost:

* Data transfer costs
* Storage costs
* Cloud services costs
* Costs for serverless features
* Costs for tokens processed by AI services

For queries that are executed concurrently, the cost of the warehouse is attributed to individual queries based on the weighted
average of their resource consumption during a given time interval.

The cost per query does not include warehouse *idle time*. Idle time is a period of time in which no queries are running in the
warehouse and can be measured at the warehouse level.

## Additional examples of queries

The next sections provide additional queries that you can use for cost attribution:

* Grouping similar queries
* Attributing costs of hierarchical queries

### Grouping similar queries

For recurrent or similar queries, use the `query_hash` or `query_parameterized_hash` to group costs
by query.

To find the most expensive recurrent queries for the current month, execute the following statement:

```sqlexample
SELECT query_parameterized_hash,
       COUNT(*) AS query_count,
       SUM(credits_attributed_compute) AS total_credits
  FROM SNOWFLAKE.ACCOUNT_USAGE.QUERY_ATTRIBUTION_HISTORY
  WHERE start_time >= DATE_TRUNC('MONTH', CURRENT_DATE)
  AND start_time < CURRENT_DATE
  GROUP BY query_parameterized_hash
  ORDER BY total_credits DESC
  LIMIT 20;
```

For an additional query based on query ID, see [Examples](../sql-reference/account-usage/query_attribution_history.md).

### Attributing costs of hierarchical queries

For stored procedures that issue multiple hierarchical queries, you can compute the attributed query costs for the
procedure by using the root query ID for the procedure.

1. To find the root query ID for a stored procedure, use the [ACCESS_HISTORY view](../sql-reference/account-usage/access_history.md). For example,
   to find the root query ID for a stored procedure, set the `query_id` and execute the following statements:

   ```sqlexample
   SET query_id = '<query_id>';

   SELECT query_id,
          parent_query_id,
          root_query_id,
          direct_objects_accessed
     FROM SNOWFLAKE.ACCOUNT_USAGE.ACCESS_HISTORY
     WHERE query_id = $query_id;
   ```

   For more information, see [Ancestor queries with stored procedures](access-history.md).
2. To sum the query cost for the entire procedure, replace `<root_query_id>` and execute the following statements:

   ```sqlexample
   SET query_id = '<root_query_id>';

   SELECT SUM(credits_attributed_compute) AS total_attributed_credits
     FROM SNOWFLAKE.ACCOUNT_USAGE.QUERY_ATTRIBUTION_HISTORY
     WHERE (root_query_id = $query_id OR query_id = $query_id);
   ```
