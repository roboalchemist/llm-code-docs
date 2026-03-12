# Source: https://ebean.io/docs/architecture/compare-hibernate

Title: Ebean versus Hibernate

URL Source: https://ebean.io/docs/architecture/compare-hibernate

Markdown Content:
JPA
---

The issues discussed in this [comparison with JPA](https://ebean.io/architecture/compare-jpa) also apply to Hibernate.

Honoring maxRows in SQL
-----------------------

Ebean ORM will always honor firstRows / maxRows in generated SQL. Once you include a join fetch to a @OneToMany, Hibernate stops implementing maxRows in SQL and instead brings all the rows back to the client (application server) and filters the results there.

This means the database does not get the opportunity to optimise that query using maxRows (via limit offset clause or similar) so the DB query execution plan can be very different by reducing the ability to use indexes and increasing the chance of a full table scan.

Significantly more data is pulled back from the DB to the client in this way.

SQL cartesian product
---------------------

Ebean ORM will never generate a SQL cartesian product. Hibernate generates a SQL cartesian product when you join fetch multiple @OneToMany or @ManyToMany associations.

LazyInitialisationException
---------------------------

Hibernate does not allow lazy loading beyond the end of its' Session scope throwing `LazyInitialisationException`.

#### Ebean allows lazy loading beyond the initial scope

*    The transaction isolation level of read committed is used as per the JPA spec. There is no effective difference when we lazy load with using another JDBC transaction relative to holding open a transaction (as typically required by Hibernate via "Open session in view"). 
*    Ebean's entity beans have a reference back to their load context which enables subsequent lazy loading with the same PersistenceContext. (also enables batch lazy loading) This means the lazy loading still produces a consistent object graph (just as if it was loaded eagerly). 
*    To prevent lazy loading with Ebean, set `query.setDisableLazyLoading(true)`. This is useful when you want to use a partially populated bean and give it to a reflection based tool that converts it to JSON or DTO's etc. 

> With Ebean, lazy loading "just works" without any drama

#### Open session in view

As a byproduct of Ebean supporting lazy loading (beyond transaction scope) Ebean does not require the `"Open session in view"` pattern sometimes seen with Hibernate.

"Open session in view" has the effect of holding a transaction open for a longer time relative to Ebean. This is considered an anti-pattern by many, with the focus now being on ensuring the service layer has loaded everything needed on the entities (and this is code we don't need to write with Ebean).

SQL2011 @History vs Hibernate Envers
------------------------------------

Ebean's @History is a database-centric approach mapping to SQL2011. Hibernate Envers is an application centric approach which means that unlike @History bulk updates and external updates don't get included in auditing with Envers.

Ebean (select/fetch) vs Hibernate JPA fetchgraph hint (EntityGraph)
-------------------------------------------------------------------

Hibernate does not honor the JPA fetchgraph hint at the property/column level which means we can't use that to optimise our SQL queries.

PagedList / findCount
---------------------

JPA nor Hibernate have built in support for PagedList with findCount - That is, having a single query to execute and having that query automatically converted into an appropriate and optimised "find total row count" query.

findEach vs scroll
------------------

JPA does not have a standard approach for large query support but Hibernate has a `scroll` query.

Ebean's findEach() work using a per object graph scope for the persistence context and also automatically adjust the JDBC fetchSize for cursor/scrolling use such that the JDBC driver (Especially MySql and Postgres) don't pull all the results to the client and for MySql runs the findEach() query in a separate transaction (such that we can perform query joins and iterate complex object graphs).

When using Hibernate `scroll` query you need to make sure you:

*   Either regularly `evict()` the beans from the Session or use a StatelessSession.
*   Set the fetchSize on the query
*   If you are using MySql you need to create the Statement with FORWARD_ONLY and READ_ONLY options, use Integer.MIN as the buffer fetchSize and NOT use the same java.sql.Connection if you want to perform other queries while the query scrolls

Set vs List
-----------

Hibernate has different semantics for `Set` and `List` (bag semantics). For Hibernate this tends to promote the use of Set as the preferred collection type.

Ebean does not apply different semantics between `Set` and `List`.

The issue with using `Set` is that it implies the use of `hashCode()/equals()` and the implementation of hashCode()/equals() is not perfect for the case of entity beans that mutate and don't always have an @Id value (e.g. When the @Id value is not populated via generated value and hence not populated until after the save and hence the @Id value can't be used in hashCode/equals implementation).

For Ebean I'd like to promote the use of `List` in preference to `Set` in order to avoid any confusion relating to hashCode()/equals() implementation on mutating entity beans.

Mapping
-------

#### Naming conventions

Ebean's default `UnderscoreNamingConvention` matches Hibernate's `ImprovedNamingStrategy` but not the JPA standard based one (which has mixed case column naming AND underscores). Note that Spring boot automatically configures Hibernate to use the ImprovedNamingStrategy.

#### javax.validation.constraints NotNull & Size

Both Ebean and Hibernate use the `@NotNull` and `@Size` validation annotations for mapping.

#### @ManyToOne

JPA defaults all @ManyToOne to be treated as fetch EAGER. We almost certainly don't want that when using Hibernate (as those Eager fetch types can then not be made lazy via JPQL or via fetchgraph hints so typically with Hibernate we would expect most @ManyToOne to be explicitly lazy via ... @ManyToOne(fetch = FetchType.LAZY).

With Ebean we use our query language to define "What to fetch" and don't need to specify FetchType.LAZY on @ManyToOne.

#### UUID type

Ebean automatically maps UUID to their native types for Postgres and H2 - so UUID just works as we would like.

Hibernate supports mapping UUID to the native type for Postgres via org.hibernate.annotations.Type - @Type(type="pg-uuid"). The downside here is that this does not work with UUID on H2 (mapping to binary instead) and this means that SQL test scripts don't execute against H2 using literal UUID values (so some pain here when testing against H2 here).

#### Entities without an @Id

Ebean allows entities to be mapped without an @Id. These entities are typically based on SQL or DB Views and used for reporting purposes. Ebean allows this and these entity beans bypass the persistence context because they don't have an @Id value.

With Hibernate we would look to use a different approach, perhaps a DTO query.

#### @View - Entities based on views

Ebean has explicit support for entities based on views via @View. This takes into account DDL for creating the view from a DB migration and testing perspective as well as L2 caching based on underlying table dependencies.

#### DDL Foreign Key and Unique constraints

Hibernate currently generates foreign key names like `FK_edi14sijwrl3p2sf41ls3svkm` and unique constraint names like `UK_ajysu81d17lesquo7uqosrtah`.

Ebean has a naming convention for foreign key names and unique constraint names that includes the table and column names. When the names are very restricted (DB2 and Oracle) Ebean uses a "vowel remover" and trim in order to still produce decent foreign key and unique constraint names. The DBA in me thinks those Hibernate constraint names are "absolute pants!".
