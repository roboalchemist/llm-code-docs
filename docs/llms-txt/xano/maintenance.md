# Source: https://docs.xano.com/the-database/database-performance-and-maintenance/maintenance.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Maintenance

## How do I perform maintenance on my Xano instance?

All paid plans include access to the Maintenance panel, accessible via your instance settings. There are different maintenance operations you can perform to help troubleshoot issues you might be having in Xano, or to manage your database storage.

## Accessing the Maintenance Panel

Head to your instance settings from your instance selection screen and choose Maintenance.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/rOuOq7qlTNyaIMAW/images/54a27e4b-image.jpeg?fit=max&auto=format&n=rOuOq7qlTNyaIMAW&q=85&s=efc6728cc30dfc8bf227ef72c808563a" width="1722" height="836" data-path="images/54a27e4b-image.jpeg" />
</Frame>

From the next panel that appears, you can choose between several maintenance options.

## **Clear Internal Cache**

This maintenance action clears the internal cache within the instance. This does not affect any drafts or redis storage. You should use this option first if you are experiencing any or multiple of the following symptoms:

* Slow loading in Xano or function stacks not loading
* APIs not responding or responding with strange errors such as "invalid app"

## **Database Maintenance**

* [**Analyze**](/the-database/database-performance-and-maintenance/maintenance#analyze)
* [**Vacuum**](/the-database/database-performance-and-maintenance/maintenance#vacuum)

Database maintenance is automatically done daily but Xano does offer ways to manually run PostgreSQL analyze and vacuum commands through the Instance Maintenance panel.

PostgreSQL's VACUUM and ANALYZE functions are essential maintenance tasks for optimizing database performance.

Together, VACUUM and ANALYZE help keep the database running smoothly by managing storage and providing accurate statistics for optimal query planning and execution.

### Analyze

ANALYZE gathers statistics about the data distribution in tables, enabling the query optimizer to generate efficient execution plans. It updates the query planner's knowledge of the data, improving query performance by enabling better index selection and join strategies.

### Vacuum

VACUUM reclaims storage space by removing obsolete or dead data that remains after updates or deletions. It helps prevent performance degradation caused by fragmentation and frees up disk space.

#### Partial VACUUM

This command analyzes and cleans up the database, but it does not necessarily reclaim all available disk space. It marks the space previously occupied by deleted rows as reusable for future inserts and updates. VACUUM also updates statistics used by the query planner to improve query performance.

#### Full VACUUM

<Warning>
  **Full VACUUM requires at least 50% free storage space before continuing. Proceeding with a Full VACUUM without enough free storage can fail or cause instance downtime.**
</Warning>

This command performs a more thorough cleanup compared to partial. It reclaims all available disk space by rewriting the entire table and indexes from scratch. This process can be more resource-intensive and time-consuming, as it involves copying the data to a new file and rebuilding the indexes. Full VACUUM can significantly improve disk space utilization but **may cause downtime** for larger tables.

## Server Maintenance

Your Xano instance is separated into 'pods' that are all responsible for their own functions. Use the guide here to determine what should be restarted and when. You can also use this panel to view the status of your backend. Use the <img src="https://mintcdn.com/xano-997cb9ee/WBQXG-4Ngk82eYAW/images/febfa8f4-image.jpeg?fit=max&auto=format&n=WBQXG-4Ngk82eYAW&q=85&s=07eb8ca30a70397f48ea4494abec20b6" className="inline m-0" width="66" height="28" data-path="images/febfa8f4-image.jpeg" /> button to check the progress of any restarts performed.

<Info>
  If you aren't sure which option to choose, please reach out to support. None of these options are typically destructive in any capacity, but we can provide specific guidance based on the behaviors you are observing.
</Info>

### Backend

This is a full reboot of your Xano instance. A good, quick catch-all for any issues you might be seeing. This option is also appropriate for stopping things like infinite loops.

<Tip>If you received an **Instance Down** email alert, restarting the Backend is the recommended first step to clear any processes stuck in a crash loop. See [Instance Down Alerting](/troubleshooting-and-support/my-instance-is-down#instance-down-alerting) for more details.</Tip>

### Database

If you are experiencing issues with your database, or want to halt an ongoing database transaction, such as an import or bulk operation.

### Frontend

If you are experiencing issues with the Xano UI, you can try restarting it from here.

### Node

This pod is responsible for some backend operations and Lambda functions.

### Realtime

This pod is responsible for our [realtime](/realtime/realtime-in-xano) functionality

### Redis

This pod is responsible for caching both to facilitate Xano functionality, and caching functions inside of your function stacks. Restarting this pod can assist with various issues related to performance and downtime if the cache is full and unable to clear automatically. If you believe you are experiencing issues related to Redis, please reach out to support.

### Task

This pod is responsible for running your background tasks. You can restart this pod if you'd like to halt any ongoing tasks.

<Warning>
  Please note that restarting your tasks will not impact the schedule of those tasks — they will continue to execute as defined. Make sure to disable any tasks either before or after the restart if you want to make sure they do not run again until you are ready.
</Warning>

## Async Function Maintenance

If you are utilizing asynchronous functions and are experiencing issues such as your functions not completing execution, you can clear the asynchronous queue from this panel.

Use the <img src="https://mintcdn.com/xano-997cb9ee/_FyaEhYRFYQZinJ0/images/e115ecde-image.jpeg?fit=max&auto=format&n=_FyaEhYRFYQZinJ0&q=85&s=8864ac981a797756eb85014a134fbf45" className="inline m-0" width="210" height="37" data-path="images/e115ecde-image.jpeg" /> option to clear any queued functions from memory.

## Request History

Use this option to manually clear your request history and free up space in your database.

<Info>
  Request history is typically purged automatically, but you can clear it anytime from here if you find it necessary.

  Make sure to define branch defaults for your request history so you're only logging what you need.
</Info>

From this panel, we have two options: **database storage** and **cache storage**.

### Database Storage for Request History

This is the actual database table that contains all of your request history, and counts against your available database storage in your instance. You can click on this option to delete one portion or all of your request history at any time.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/_oKnuVg5Nf4VhJM4/images/489aca5c-image.jpeg?fit=max&auto=format&n=_oKnuVg5Nf4VhJM4&q=85&s=64fa9a0f5b4dfd3d102e9d13029a273c" width="665" height="869" data-path="images/489aca5c-image.jpeg" />
</Frame>

Use the **Force** option to halt any running processes to ensure the data can be cleared -- please note however that this may result in a little bit of downtime as the server halts running processes.

### Cache Storage for Request History

As requests are logged, they are not immediately saved to the database. For a short period of time, they are held in a cache, and dumped into the database at fast, regular intervals. In some cases, such as during excessive traffic spikes, you may find that clearing the request cache before the items are added to the database can help the recovery process.

Please note that when items are cleared from the cache, they will not be logged in the history database.


Built with [Mintlify](https://mintlify.com).