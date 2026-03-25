# Source: https://docs.snowflake.com/en/user-guide/account-replication-failover-failback.md

# Failing over account objects

This topic describes the steps necessary to fail over replicated account objects across multiple accounts in different
[regions](intro-regions.md) for disaster recovery.

For information about the purpose of the failover mechanism and when to use it, see [Introduction to business continuity & disaster recovery](replication-intro.md).

## Prerequisites

1. Enable replication in a set of accounts within the same organization, across multiple regions in one cloud service provider
   or across different cloud service providers.
2. Create a primary failover group that defines the kinds of objects to replicate, and specifies the target accounts
   to which to replicate. You can optionally divide the replicated objects across multiple failover groups, for example if
   some databases should be replicated more frequently than others.
3. Create at least one secondary failover group (replica) of each primary failover group in one or more secondary accounts.
4. Refresh (synchronize) each replica with the latest updates to the objects in the failover group. Perform an
   initial refresh, and set up a schedule to regularly bring the latest changes to each secondary account.

For instructions, see [Replicating account objects and databases](account-replication-config.md).

## Promote a target account to serve as the source account

You can promote a target account to serve as the source account (failover) using Snowsight or
[SQL](account-replication-config.md).

For more information about the kinds of objects you can specify in a failover group,
see [Replication groups and failover groups](account-replication-intro.md).

### Promote a target account to serve as the source account using Snowsight

> **Note:**
>
> Only account administrators can edit a replication or failover group using Snowsight (see
> [Limitations of using Snowsight for replication configuration](account-replication-config.md)).
>
> For the most consistent and reliable failover experience, select all the applicable failover groups and
> connections and promote them all at the same time. We refer to this operation as a *bulk failover*.

To promote a target account to serve as the source account using Snowsight, follow these steps:

1. Sign in to [Snowsight](ui-snowsight-gs.md). **Make sure to sign in using the target account**.
2. In the navigation menu, select Admin » Accounts.
3. Select Replication, then select Initiate failover. Doing so brings up a dialog where you make the remaining choices.
4. Select any failover groups to promote. After the failover, the objects specified in those
   failover groups become writable on the newly promoted primary account. Those objects become
   read-only on the account that formerly was the primary and is now a secondary account.
5. Select Next.
6. Select any connections to promote. After the failover, those connections connect to the account
   that you’re promoting to be the new primary account.
7. Select Next.
8. Select Fail over in the confirmation window.
9. If any refresh operations are in progress for the failover groups you selected, you can wait for those refreshes
   to complete, or choose an alternative approach if your failover is urgent and should take priority.

   The default action is to wait for the refreshes to complete. That way, the primary and secondary systems are all
   in a consistent state when the bulk failover runs. Snowflake uses your currently selected warehouse to poll the
   status of the ongoing refreshes. If you don’t have a selected warehouse, you select one now using the
   Select warehouse option.

   Or, you can proceed with the failover immediately by selecting Show advanced options.

   * To fail over only the failover groups that aren’t currently being refreshed, select Exit with current progress.
     In that case, you perform additional refreshes later for the groups that were skipped during the bulk failover.
   * To cancel the refresh operations and continue the failover, select Cancel refreshes and force failover.
     In that case, you might need to clean up any inconsistencies on the secondary system from the interrupted refreshes.

If the failover operation didn’t complete for all failover groups, you can perform another bulk failover. Or you can fail over
the remaining failover groups one at a time, using the procedure in Promote a single failover group to serve as the primary using Snowsight.

### Promote a single failover group to serve as the primary using Snowsight

> **Note:**
>
> Only account administrators can edit a replication or failover group using Snowsight (see
> [Limitations of using Snowsight for replication configuration](account-replication-config.md)).

To promote a single failover group to be the primary using Snowsight, follow these steps:

1. Sign in to [Snowsight](ui-snowsight-gs.md). **Make sure to sign in using the target account**.
2. In the navigation menu, select Admin » Accounts.
3. Select Replication, then select Groups.
4. Locate the failover group that you want to promote, and select the More menu (…) in the last column of the row.
5. Select Fail over, then select Fail over in the confirmation window.

> **Tip:**
>
> You typically use this procedure if you encounter a problem failing over one group, and you need to retry the
> failover only for that group. To promote an entire account to be the primary, select multiple failover groups and connections and
> perform a bulk failover. For more information, see Promote a target account to serve as the source account using Snowsight.

### Promote a target account to serve as the source account using SQL

To promote a target account to serve as the source account using SQL, you sign in to the target account
and execute the [ALTER FAILOVER GROUP … PRIMARY](../sql-reference/sql/alter-failover-group.md) command.

#### Promote a secondary failover group to primary failover group

> **Note:**
>
> The example in this section must be executed by a role with the FAILOVER privilege.

The following example promotes `myaccount2` in the current `myorg` organization to serve as the source account.

1. Sign in to target account `myaccount2`.
2. List failover groups in the account:

   ```sqlexample
   SHOW FAILOVER GROUPS;
   ```

3. Execute the following statement for each secondary failover group you want to promote to serve as the primary failover group:

   ```sqlexample
   ALTER FAILOVER GROUP myfg PRIMARY;
   ```

   > **Note:**
   >
   > During a partial outage in your source region, the replication service might continue to be available and might continue
   > to refresh the secondary failover groups in target regions.
   >
   > To ensure data integrity, Snowflake prevents failover if a refresh operation is in progress. This means you cannot
   > promote a secondary failover group to serve as the primary if it is being refreshed by a replication operation.
   > The ALTER FAILOVER GROUP … PRIMARY command returns an error in this scenario.

#### Resolving failover statement failure due to an in-progress refresh operation

If there is a refresh operation in progress for the secondary failover group you are trying to promote, the failover statement
results in the following error:

```output
Replication group "<GROUP_NAME>" cannot currently be set as primary because it is being
refreshed. Either wait for the refresh to finish or cancel the refresh and try again.
```

To successfully fail over, you must complete the following steps.

1. Select and complete one of the following options:

   > **Important:**
   >
   > Suspending a refresh operation in the SECONDARY_DOWNLOADING_METADATA or SECONDARY_DOWNLOADING_DATA phase
   > might result in an inconsistent state on the target account. For more information, see
   > View the current phase of an in-progress refresh operation.

   1. Suspend future refresh operations for the failover group. If there is an in-progress refresh operation, you must wait for
      it to complete before you can failover:

      ```sqlexample
      ALTER FAILOVER GROUP myfg SUSPEND;
      ```

   2. Suspend future refresh operations *and* cancel a scheduled refresh operation that is currently in progress (if there is one).

      If the in-progress refresh operation was manually triggered, see Cancel an in-progress refresh operation that wasn’t automatically scheduled.

      ```sqlexample
      ALTER FAILOVER GROUP myfg SUSPEND IMMEDIATE;
      ```

      > **Note:**
      >
      > You might experience a slight delay between the time that the statement returns and the time that the cancellation
      > of the refresh operation is finished.
2. Verify no refresh operations are in progress for the failover group `myfg`. The following query
   should return no results:

   ```sqlexample
   SELECT phase_name, start_time, job_uuid
     FROM TABLE(INFORMATION_SCHEMA.REPLICATION_GROUP_REFRESH_HISTORY('myfg'))
     WHERE phase_name <> 'COMPLETED' and phase_name <> 'CANCELED';
   ```

   To see canceled refresh operations for failover group `myfg`, you can execute the following statement:

   ```sqlexample
   SELECT phase_name, start_time, job_uuid
     FROM TABLE(INFORMATION_SCHEMA.REPLICATION_GROUP_REFRESH_HISTORY('myfg'))
     WHERE phase_name = 'CANCELED';
   ```

3. Now you can promote the secondary failover group `myfg` to primary failover group:

   ```sqlexample
   ALTER FAILOVER GROUP myfg PRIMARY;
   ```

#### Resume scheduled replication in target accounts

On failover, scheduled refreshes on all secondary failover groups are suspended.
[ALTER FAILOVER GROUP … RESUME](../sql-reference/sql/alter-failover-group.md) must be executed in each **target account** with a
secondary failover group to resume automatic refreshes.

```sqlexample
ALTER FAILOVER GROUP myfg RESUME;
```

## View the current phase of an in-progress refresh operation

A refresh operation can be safely canceled during most phases of the refresh operation. However, canceling a refresh operation
in the SECONDARY_DOWNLOADING_METADATA or SECONDARY_DOWNLOADING_DATA phase might result in an inconsistent state on the target
account. If the refresh operation has started one of these phases, it proceeds to completion regardless of the availability of
the source account. Allowing the phase to complete before you fail over ensures replicas are in a consistent state.
After the replicas are in a consistent state, you can resume or replay your ingest and transformation pipelines to update the
replicas to the current state.

To view the current phase of an in-progress refresh operation for a failover group, use the Information Schema
[REPLICATION_GROUP_REFRESH_PROGRESS, REPLICATION_GROUP_REFRESH_PROGRESS_BY_JOB, REPLICATION_GROUP_REFRESH_PROGRESS_ALL](../sql-reference/functions/replication_group_refresh_progress.md) table function.

For example, to view the current phase of an in-progress refresh operation for failover group `myfg`, execute
the following statement:

```sqlexample
SELECT phase_name, start_time, end_time
  FROM TABLE(
    INFORMATION_SCHEMA.REPLICATION_GROUP_REFRESH_PROGRESS('myfg')
  );
```

For a list of refresh operations phases, see the [usage notes](../sql-reference/functions/replication_group_refresh_progress.md)
for the function.

## Cancel an in-progress refresh operation that wasn’t automatically scheduled

To cancel an in-progress refresh operation that was not triggered automatically by a replication schedule, you must use the
[SYSTEM$CANCEL_QUERY](../sql-reference/functions/system_cancel_query.md) function:

1. Find the query ID or JOB_UUID for running refresh operations using one of the following options:

   1. Find the query IDs for all running refresh operations:

      ```sqlexample
      SELECT query_id, query_text
        FROM TABLE(INFORMATION_SCHEMA.QUERY_HISTORY())
        WHERE query_type = 'REFRESH REPLICATION GROUP'
        AND execution_status = 'RUNNING'
        ORDER BY start_time;
      ```

      Use the QUERY_TEXT column to identify the QUERY_ID for failover group refresh operations from the list.
   2. Find the JOB_UUID for an in-progress refresh operation for a specific failover group `myfg`:

      ```sqlexample
      SELECT phase_name, start_time, job_uuid
        FROM TABLE(INFORMATION_SCHEMA.REPLICATION_GROUP_REFRESH_HISTORY('myfg'))
        WHERE phase_name <> 'COMPLETED' and phase_name <> 'CANCELED';
      ```

2. Cancel the refresh operation using the SYSTEM$CANCEL_QUERY function and the QUERY_ID or JOB_UUID:

   ```sqlexample
   SELECT SYSTEM$CANCEL_QUERY('<QUERY_ID | JOB_UUID>');
   ```

   Returns the following output:

   ```output
   query [<QUERY_ID>] terminated.
   ```

3. After you cancel the in-progress refresh operation, continue to the
   next steps.

## Reopen active channels for Snowpipe Streaming in newly promoted source account

Tables in a primary database that are populated by [Snowpipe Streaming are replicated](account-replication-considerations.md)
to secondary databases. After failover, reopen active Snowpipe Streaming channels for tables and re-insert any missing data rows
for the channels:

1. Reopen active channels for the table by calling the [openChannel](https://javadoc.io/doc/net.snowflake/snowflake-ingest-sdk/latest/net/snowflake/ingest/streaming/SnowflakeStreamingIngestClient.html) API.
2. Fetch offset tokens:

   1. Call the [getLatestCommittedOffsetToken](https://javadoc.io/doc/net.snowflake/snowflake-ingest-sdk/latest/net/snowflake/ingest/streaming/SnowflakeStreamingIngestChannel.html#getLatestCommittedOffsetToken()) API or
   2. Execute the [SHOW CHANNELS](../sql-reference/sql/show-channels.md) command to retrieve a list of the active channels of the table.
3. Re-insert data rows for the channel from the fetched offset tokens.

> **Note:**
>
> These steps apply only to Snowpipe Streaming with the Snowflake Ingest SDK; it doesn’t apply to Snowpipe Streaming with the Kafka connector. Follow the steps below to restart the Kafka Connector after failover.

### Snowpipe Streaming and the Kafka connector

If you are using the Kafka connector and Snowpipe Streaming, follow these steps after failover:

1. Update the Kafka connector configuration to point to the newly promoted source account.
2. Execute the SHOW CHANNELS command to retrieve the list of active channels and the offset tokens. Each channel belongs to a
   single partition in the Kafka topic.
3. Manually reset offsets in the Kafka Topic for each of those partitions (channels).
4. Restart the Kafka Connector.

For more information, see:

* [Snowflake Connector for Kafka with Snowpipe Streaming classic](snowpipe-streaming/snowpipe-streaming-classic-kafka.md).
* [Replication and Snowpipe Streaming](account-replication-considerations.md).
