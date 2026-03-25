# Source: https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-search/cortex-search-replication.md

# Replicate a Cortex Search Service

Cortex supports the replication of Cortex Search Services from a source account to one or more target accounts in the same organization. This replication is integrated seamlessly with Snowflake replication and failover groups to provide point-in-time consistency for the objects on the target account. For more information about replication and failover, see [Introduction to replication and failover across multiple accounts](../../account-replication-intro.md).

A search service is automatically replicated if the parent database is in a replication or failover group. An automatically replicated search service follows the same behaviors as other replicated entities.

* A replicated Cortex Search Service is read only. No direct ALTER or DROP commands are allowed on the replicated entity.
* A replicated Cortex Search Service syncs with the primary service according to the replication schedule. Specifically, if the primary replica drops the service, the secondary service is also dropped during replication refresh.
* After replication is completed, there may be up to a 10 minute delay for the serving system to load the replicated service. After the service is loaded, a replicated Cortex Search Service is queryable like a normal service.

  > **Note:**
  >
  > Replicated services in failover groups are suspended in serving and are not queryable. These replicated services are reactivated after the failover group becomes the new primary.
* Replication related costs might incur for data transfer and compute resources during replication. Cortex Search Service serving costs are similar to those in the primary service. There are no additional costs for Cortex Search indexing. For more information, see [Understanding replication cost](../../account-replication-cost.md).

For more information about replication and failover groups, see [CREATE REPLICATION GROUP](../../../sql-reference/sql/create-replication-group.md).

## Create a replicated Cortex Search Service

To create a replicated Cortex Search Service, create a replication group that includes the parent database of the service.

1. Create a replication group in the primary account.

   > ```sqlexample
   > CREATE REPLICATION GROUP myrg
   >     OBJECT_TYPES = DATABASES
   >     ALLOWED_DATABASES = <database1>
   >     ALLOWED_ACCOUNTS = <org-name>.<secondary-account>
   >     REPLICATION_SCHEDULE = '60 MINUTE';
   > ```
>
2. From the secondary account, run the following command to create a replica of the primary account database in the secondary account.

   > ```sqlexample
   > CREATE REPLICATION GROUP myrg
   >     AS REPLICA OF <org-name>.<primary-account>.myrg;
   > ```
>
3. From the secondary account, manually refresh the replica.

   > ```sqlexample
   > ALTER REPLICATION GROUP myrg REFRESH;
   > ```
>
4. Create a Cortex Search Service in the primary database. For more information, see [CREATE CORTEX SEARCH SERVICE](../../../sql-reference/sql/create-cortex-search.md). The search service is automatically replicated according to the replication schedule.

## Create a failover group

Failover groups allow you to back up your data in an additional account without using or paying for the replicated services. With a failover group, you can activate the failover only when needed to resume operations. To create a failover group for the Cortex Search Service, create a failover group that includes the parent database of the service.

1. Create a failover group in the primary account.

   > ```sqlexample
   > CREATE FAILOVER GROUP myrg
   >     OBJECT_TYPES = DATABASES
   >     ALLOWED_DATABASES = <database1>
   >     ALLOWED_ACCOUNTS = <org-name>.<secondary-account>
   >     REPLICATION_SCHEDULE = '60 MINUTE';
   > ```
>
2. From the secondary account, run the following command to create a failover of the primary account database in the secondary account.

   > ```sqlexample
   > CREATE FAILOVER GROUP myrg
   >     AS REPLICA OF <org-name>.<primary-account>.myrg;
   > ```
>
3. From the secondary account, manually refresh the failover group.

   > ```sqlexample
   > ALTER FAILOVER GROUP myrg REFRESH;
   > ```
>
4. Create a Cortex Search Service in the primary database. For more information, see [CREATE CORTEX SEARCH SERVICE](../../../sql-reference/sql/create-cortex-search.md). The search service is automatically replicated according to the replication schedule.
5. At the time of disaster recovery, run the following sql in the secondary account to make it the new primary. The replicated service will be activated and loaded into the serving system to query.

   > ```sqlexample
   > ALTER FAILOVER GROUP myrg PRIMARY;
   > ```
