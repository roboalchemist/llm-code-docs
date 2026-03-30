# Source: https://ebean.io/docs/upgrading

Title: Upgrading Ebean version

URL Source: https://ebean.io/docs/upgrading

Markdown Content:
Summary of changes
------------------

A summary of changes needed in migrating to a later version of Ebean.

Upgrading to 12.x from 11.x
---------------------------

*    #1826 Removed `@PrivateOwned`, migrate to orphanRemoval=true attribute on `@OneToMany`
*    #1824 Stateless updates - Removed update deleteMissingChildren option, instead always use orphanRemoval behaviour change breaking-api 

Upgrading to 11.x from 10.x
---------------------------

*   #1434 Remove deprecated API from EbeanServer - finder methods that take explicit transaction. Migrate to use ebeanServer.extended() 
*   #1417 Breaking API - Remove PersistBatch.INSERT ... migrate to PersistBatch.ALL
*   #1424 Deprecate / Move ... finder methods that take explicit transaction to ExtendedServer API

*   new DbMigration(); -> DbMigration.create();
*   findUnique() -> findOne()

*   CacheMode.QUERY_ONLY -> GET
*   CacheMode.RECACHE -> PUT

*   io.ebean.Platform; -> io.ebean.annotation.Platform;
*   io.ebean.PersistBatch; -> io.ebean.annotation.PersistBatch;
*   io.ebean.TxType; -> io.ebean.annotation.TxType;
*   io.ebean.TxIsolation; -> io.ebean.annotation.TxIsolation;

*   Remove support for PropertyChangeListener from entity beans
*   Remove ServerConfig h2ProductionMode ... means for testing with h2 explicitly set ddlGenerate and ddlRun

Upgrading to 10.x from 9.x
--------------------------

*   #### Change package to io.ebean

*   Remove DbMigrationConfig.generateOnStart() ... migrate to offline generation

Upgrading to 9.x from 8.x
-------------------------

*   Query.includeSoftDeletes() -> setIncludeSoftDeletes()

Upgrading to 8.x from 7.x
-------------------------

*   (#682) Remove deprecated Model.Finder constructors that take Id type ... migrate to ones that don't

Upgrading to 7.x from 6.x
-------------------------

*   (#352) Remove deprecated API - ValuePair getValue1() getValue2() ... use getNewValue() getOldValue()
*   (#344) Remove deprecated annotation @ColumnHstore ... migrate to @DbHstore
*   (#343) Remove deprecated interface BeanFinder<T> ... migrate to BeanFindController
*   (#342) Remove deprecated method - JsonContext createJsonContext() ... migrate to json()
*   (#331) Remove deprecated method - EbeanServer.findVisit() ... migrate to findEach

Changes for: `saveAll()`, `insertAll()`, `updateAll()`, `deleteAll()`

*   (#341) Remove deprecated method - insert(Collection beans); ... migrate to insertAll()
*   (#340) Remove deprecated method - update(Collection beans) ... migrate to updateAll()
*   (#339) Remove deprecated method - save(Collection beans, Transaction transaction) ... migrate to saveAll()
*   (#339) Remove deprecated method - save(Collection beans, Transaction transaction) ... migrate to saveAll()
*   (#338) Remove deprecated method - save(Iterator it, Transaction transaction) ... please change to iterate yourself and save. 
*   (#337) Remove deprecated method - delete(Class beanType, Collection ids) ... migrate to deleteAll()
*   (#336) Remove deprecated method - delete(Iterator it, Transaction transaction) ... migrate to deleteAll()
*   (#335) Remove deprecated method - delete(Collection beans) ... migrate to deleteAll()
*   (#334) Remove deprecated method - delete(Iterator it) ... migrate to deleteAll()
*   (#333) Remove deprecated method - save(Iterator it) ... change to iterate yourself and save()
*   (#332) Remove deprecated method - save(Collection beans) ... migrate to saveAll(beans)

[Edit Page](https://github.com/ebean-orm/website-source/blob/master/docs/upgrading/index.html)
