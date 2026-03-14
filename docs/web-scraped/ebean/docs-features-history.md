# Source: https://ebean.io/docs/features/history

Title: History | Ebean

URL Source: https://ebean.io/docs/features/history

Markdown Content:
Videos
------

Overview
--------

[SQL2011](https://en.wikipedia.org/wiki/SQL:2011) introduced temporal extensions to SQL including `AS OF SYSTEM TIME` and `VERSIONS BETWEEN SYSTEM TIME`.

Ebean has support for this extension to SQL. The support for this falls into 2 general cases where some databases have SQL2011 support built in (Oracle, DB2, MS SQL Server 2016) or where it is not built in (Postgres, MySql) and Ebean generates history tables/triggers/views to support the feature.

#### Current support in Ebean

*   `Oracle` via Total recall
*   `Postgres` via Triggers/history table
*   `MySql` via Triggers/history table
*   `H2` via Triggers/history table

History tables
--------------

For Postgres, MySql and H2 (and in general databases that don't have SQL2011 support built in) Ebean generates DDL for History tables and associated triggers and views. This is a common "Temporal database design" approach that has been used for some time and not specific to Ebean. For example, this approach is already implemented as a Postgres extension - [arkhipov/temporal_tables](https://github.com/arkhipov/temporal_tables/).

In general the history table approach results in:

*   A "history" table created that has the same (or very similar) structure as the "base table"
*   The "history" table does not have constraints by default (no primary key, foreign key or indexes)
*   2 extra columns added to the base table and history table for "effective start" and "effective end" timestamp range. Postgres has a timestamp range type so that is preferred to 2 separate columns for the Postgres implementation. 
*   A view is used to `union all` combine the "base table" and the "history table" to simplify history queries
*   Triggers are used on update and delete to copy the existing row data from the "base table" to the associated "history table" 
*   Schema changes to the "base table" (add column etc) result in mirrored changes to the "history table" and potentially updates to the associated triggers 

#### See also:

*   [clarkdave blog post - historical-records-with-postgresql](http://clarkdave.net/2015/02/historical-records-with-postgresql-and-temporal-tables-and-sql-2011/)
*   [Postgresql Wiki - SQL2011Temporal](https://wiki.postgresql.org/wiki/SQL2011Temporal)
*   [Postgres extension - arkhipov/temporal_tables](https://github.com/arkhipov/temporal_tables/)

Compared to Change Log
----------------------

#### Transactional

With @History changes are transactional and have the associated guarantees - changes can't be missed or lost.

#### Not bypassed

With @History the database handles all changes. If other frameworks (not Ebean) or stored procedures or raw JDBC is used to update the database all these changes are captured by the database triggers. Although Ebean makes it easier to query and generate the appropriate DDL the capturing of changes is a database function and not strictly tied to Ebean or application code.

#### Easy to query

With @History it is easy to query and view the data "As of" a given timestamp and view the versions and historic changes for a given bean/row. This is also possible with Change log but requires more work (loading the change log into say ElasticSearch and creating appropriate queries to return as of and version type data).

#### DB Overhead

A downside to @History relative to using Change log is that it does introduce extra costs to the database in terms of storage (history tables taking storage space) and in terms of impact to response time as updates and deletes now also copy data into the history tables.

The approach with Oracle Total Recall reduces the impact to response time by processing the copy of data from redo into the history tables in the background and in batch and that probably means it can generally be used more widely (on more base tables) than the traditional trigger based approach.

#### Schema changes

A downside to @History relative to using Change log is that schema changes (like adding a column) can mean more work / complexity as changes need to also be reflected in associated history tables and triggers. The DB migration support in Ebean mitigates this by generating all the appropriate changes to history tables and triggers etc.

Add the `@History` annotation to the entity beans that you want history support on. In the case of Postgres and MySql this means that Ebean will generate DDL (triggers, views etc) to support history on the underlying tables. For Oracle adding @History implies that the table has had flashback archive already assigned to the table.

@HistoryExclude
---------------

Add the `@HistoryExclude` annotation on entity bean properties that should be excluded from history. This is expected to be used on large text or blob columns where there can be a relatively high storage cost associated with keeping the history values and excluding these columns is desired.

ManyToMany intersection
-----------------------

In the case of intersection (bridge) tables for ManyToMany relationships by default the intersection tables also have history. That is, if `@History` is put on an entity bean then by default the intersection tables for `@ManyToMany` properties have history support (associated history tables, views and triggers).

To exclude history from intersection tables `@HistoryExclude` should be put on the `@ManyToMany` property.

As of query
-----------

A Timestamp can be used with `Query.asOf(Timestamp)` and Ebean will generate the query such that the returning object graph represents the state as of the given timestamp. More accurately for tables with history the query returns rows representing the table as of the given timestamp and for other tables included in the query the rows returned represent 'current values'.

// asOf some time in the past like 1 hour ago, 1 week ago, 1 month ago etc
Timestamp asOf = ...;

Customer customer =
    Customer.find.query()
        .asOf(asOf)
        .fetch("billingAddress")
        .where().eq("name", "jim")
        .findOne();

#### Scenario: Customer and Address both have history

In the above query if both Customer Address have history then both the customer data and address data will be returned 'As of' the given timestamp.

#### Scenario: Customer has history but Address does not

In the above query if Customer has history but Address does not then the customer data will be returned 'As of' the given timestamp but the address data will be returned using 'current data'.

#### Scenario: Address lazy loaded

The `AS OF` timestamp is propagated to all secondary queries including lazy loading queries. That is, the `AS OF` timestamp applies to the entire object graph loaded by and not just the "origin query". If Address is lazy loaded and Address has history the address data will also be 'as of' the original timestamp.

Versions between
----------------

`Query.findVersionsBetween()` is used to return a list of versions for a given object over time. The version beans returned contain a "diff" to the prior version as well as the effective start and effective end timestamps.

Timestamp start = ...;
Timestamp end = ...;

List<Version<Customer>> customerVersions =
    Customer.find.query()
      .where()
      .idEq(42)
      .findVersionsBetween(start, end);

for (Version<Customer> customerVersion : customerVersions) {
  Customer bean = customerVersion.getBean();
  Map<String, ValuePair> diff = customerVersion.getDiff();
  Timestamp effectiveStart = customerVersion.getStart();
  Timestamp effectiveEnd = customerVersion.getEnd();
}

Who and When
------------

It is generally expected that the entity beans should contain `@WhoCreated`, `@WhoModified`, `@WhenCreated` and `@WhenModified` properties.

/**
 * Common properties used by many entity beans.
 */
@MappedSuperclass
public class BaseModel {

  @Id
  Long id;

  @Version
  Long version;

  @WhenCreated
  Timestamp whenCreated;

  @WhenModified
  Timestamp whenModified;

  @WhoCreated
  String whoCreated;

  @WhoModified
  String whoModified;
  ...

@History
@Entity
@Table(name="customer")
public class Customer extends BaseModel {

  @Size(max = 100)
  String name;
  ...

Postgres
--------

Postgres has an existing [arkhipov/temporal_tables](https://github.com/arkhipov/temporal_tables/) extension and Postgres/Ebean users could use this extension. By default Ebean does not use this extension but instead generates similar triggers. The difference between using arkhipov/temporal_tables or not comes down to DDL generation. Ultimately it would be good for Ebean to support DDL generation for arkhipov/temporal_tables but that isn't built into Ebean yet.

The other notable aspect of history support in Postgres is that we can make use of the timestamp range type with expected benefits in terms on indexing performance relative to using 2 separate timestamp columns.

MySql
-----

There is a concern with MySql in the case where DDL changes need to be applied to a production database. In the case where Triggers need to change due to a schema change (like add column) MySql has no 'create or replace trigger' and instead a table lock needs to be held to drop and create the trigger. Holding a table lock in a production database might be a problem and restrict schema changes.

Oracle
------

Rob's View: Oracle Total recall has some nice advantages over the explicit trigger/history table approach. The main advantages being:

*   **Performance : low foreground cost** - History table population occurs in the background and results in a much lower overhead/impact on foreground response time
*   **Performance : batch processing** - History table population can be processed in batch reducing the overhead/impact for many small updates
*   **Admin : reduced DDL** - Table alterations (add columns etc) are handled automatically reducing the admin costs of maintaining triggers/views/history tables.
