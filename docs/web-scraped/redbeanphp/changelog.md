# Source: https://redbeanphp.com/changelog

Title:

URL Source: https://redbeanphp.com/changelog

Markdown Content:
RedBeanPHP :: Changelog
===============

[![Image 1: RedBeanPHP logo, a white bean on a red square.](https://redbeanphp.com/img/redbeanphp_logo.png)](https://redbeanphp.com/)
RedBeanPHP

The Power ORM
=========================

* [](http://github.com/gabordemooij/redbean "(EXTERNAL LINK) Contribute to RedBeanPHP or fork the repository on Github.")
* [Travis](https://www.travis-ci.com/github/gabordemooij/redbean "(EXTERNAL LINK) Read the latest test report on Travis-CI.")
* [API](https://redbeanphp.com/api/namespaces/RedBeanPHP.html "Discover hidden treasures in RedBeanPHP ORM with the API documentation.")
* [Forum](http://groups.google.com/forum/?fromgroups#!forum/redbeanorm "(EXTERNAL LINK) Ask questions or help others at the RedBeanPHP forum.")
* [Sponsor](https://redbeanphp.com/changelog?p=/welcome#sponsor "Sponsor")

* **Introduction**
  * [Welcome](https://redbeanphp.com/welcome "Welcome")
  * [Download](https://redbeanphp.com/download "Download")
  * [Quick Tour](https://redbeanphp.com/quick_tour "Quick Tour")
  * [Requirements](https://redbeanphp.com/requirements "Requirements")
  * [Install](https://redbeanphp.com/install "Install")
  * [Connection](https://redbeanphp.com/connection "Connection")
  * [Tutorial](https://redbeanphp.com/tutorial "Tutorial")
  * [Videos](https://redbeanphp.com/videos "Videos")

* **Basics**
  * [CRUD](https://redbeanphp.com/crud "CRUD")
  * [Finding](https://redbeanphp.com/finding "Finding")
  * [Querying](https://redbeanphp.com/querying "Querying")
  * [Extended SQL](https://redbeanphp.com/extended_sql "Extended SQL")
  * [Data Tools](https://redbeanphp.com/data_tools "Data Tools")
  * [Database](https://redbeanphp.com/database "Database")
  * [Fluid and Frozen](https://redbeanphp.com/fluid_and_frozen "Fluid and Frozen")
  * [Debugging](https://redbeanphp.com/debugging "Debugging")

* **Relations**
  * [One-to-many](https://redbeanphp.com/one_to_many "One-to-many")
  * [Many-to-one](https://redbeanphp.com/many_to_one "Many-to-one")
  * [Aliases](https://redbeanphp.com/aliases "Aliases")
  * [Many-to-many](https://redbeanphp.com/many_to_many "Many-to-many")
  * [Using SQL Snippets](https://redbeanphp.com/using_sql_snippets "Using SQL Snippets")
  * [Counting](https://redbeanphp.com/counting "Counting")
  * [Labels, Enums, Tags](https://redbeanphp.com/labels__enums__tags "Labels, Enums, Tags")

* **Advanced**
  * [Trees](https://redbeanphp.com/trees "Trees")
  * [Link Beans](https://redbeanphp.com/link_beans "Link Beans")
  * [Other relations](https://redbeanphp.com/other_relations "Other relations")
  * [Models](https://redbeanphp.com/models "Models")
  * [Meta data](https://redbeanphp.com/meta_data "Meta data")
  * [Duplicate](https://redbeanphp.com/duplicate "Duplicate")
  * [Import and Export](https://redbeanphp.com/import_and_export "Import and Export")
  * [Non-static](https://redbeanphp.com/non_static "Non-static")
  * [UUIDs](https://redbeanphp.com/uuids "UUIDs")
  * [Templates](https://redbeanphp.com/templates "Templates")
  * [Prefixes](https://redbeanphp.com/prefixes "Prefixes")
  * [Query Builder](https://redbeanphp.com/query_builder "Query Builder")
  * [LOBs](https://redbeanphp.com/lobs "LOBs")
  * [Migrations](https://redbeanphp.com/migrations "Migrations")

* **Project**
  * Changelog
  * [Roadmap](https://redbeanphp.com/roadmap "Roadmap")
  * [Beta](https://redbeanphp.com/beta "Beta")
  * [About](https://redbeanphp.com/about "About")
  * [Plugins](https://redbeanphp.com/plugins "Plugins")
  * [SQN](https://redbeanphp.com/sqn "SQN")
  * [Frameworks](https://redbeanphp.com/frameworks "Frameworks")
  * [Menu](https://redbeanphp.com/menu "Menu")

Changelog
=========

Every six months a new version of RedBeanPHP is released. Here you find the changes in each revision starting from version 4.0. You can download the latest RedBeanPHP from the [Download Page](https://redbeanphp.com/Download "Go to the download page")

RedBeanPHP 5.7.5 (30 May 2025)
------------------------------

* Improved error message for bean types
* Improved performance of GetCol() (thanks [Dima-Stefantsov](https://github.com/gabordemooij/redbean/commit/f1acdd1fa08c7900cfd3a74e292fa8e6841cbeb0))
* Added SimpleModelInterface (thanks [mattimatti](https://github.com/gabordemooij/redbean/commit/599bd825f1b7e0179425a0f6f5af145b817774d2))
* Add [intval](https://github.com/gabordemooij/redbean/commit/7515e018a656d179bc804d9f804fa3b13c73d73d) to R::exec()
* Fix [typehints](https://github.com/gabordemooij/redbean/commit/df5a936f3b46d4eca2cf33aadcab337a55fc314f) in docs
* Fix documentation error (thanks [krisives](https://github.com/gabordemooij/redbean/commit/1bb7b5b93031d1a458a503ee91b595c8f7a8c83d))

RedBeanPHP 5.7.4 (18 March 2023)
--------------------------------

* Improved compatibility with PHP 8.2 (thanks [Rivets](https://github.com/rivets))
* [Fix R::transaction()](https://github.com/gabordemooij/redbean/issues/922) no longer starts transactions in fluid mode (unless allowed) (thanks [Jemt](https://github.com/Jemt))
* Make runQuery() public and optimize it
* [Add support for DateTime(Interface)](https://github.com/gabordemooij/redbean/issues/891) (thanks [Ben Major](https://github.com/benmajor))

RedBeanPHP 5.7.3 (8 October 2022)
---------------------------------

* Added [either()](https://redbeanphp.com/many_to_one#either) method to support ??-like NULL-coalesce
* Compatibility fix: R::loadJoined() on NULL no longer gives an [error](https://github.com/gabordemooij/redbean/issues/900) on PHP 8.1 (thanks [Marios88](https://github.com/marios88))
* Improved [documentation](https://github.com/gabordemooij/redbean/pull/898) (thanks [MangoMarcus](https://github.com/MangoMarcus))
* Fixed [performance issue](https://github.com/gabordemooij/redbean/issues/893) with class_exist (thanks [Gnysek](https://github.com/gnysek))

RedBeanPHP 5.7.2 (2 April 2022)
-------------------------------

* Added [DBPrefix()](https://redbeanphp.com/models#dbprefix) function to select different Model namespaces per database
* Added [$bean->asObject()](https://redbeanphp.com/crud#asobj) to cast value to Object
* Added [$bean->trimport()](https://redbeanphp.com/import_and_export#trimport) to import with trim
* Added support for PHP 8 [TypedModel](https://redbeanphp.com/models#typedmodel) type hinting

RedBeanPHP 5.7.1 (31 October 2021)
----------------------------------

* Added compatibility with PHP 8.1 (thanks Ipsod)
* Fixed a minor bug in setPDO() that failed to set isConnected flag (thanks DengWang)
* Added 4th parameter to BeanCollection to pass a meta mask (thanks MangoMarcus)
* Added initial support for PHPStan/Psalm-annotations (thanks Craig Francis)

RedBeanPHP 5.7 (3 April 2021)
-----------------------------

* Added pstr($x) function to easily generate [$x, PDO::PARAM_STR] for you (Gabor)
* Added pint($x) function to easily generate [$x, PDO::PARAM_INT] for you (Gabor)
* Added R::camelfy() convience function (Gabor)
* Added R::uncamelfy() convience function (Gabor)
* Improved PHP-8 compatibility (Gabor)
* OODBBean::equals now accepts NULL and simply returns FALSE (Gabor)
* Improved some source comments (Gabor)

RedBeanPHP 5.6.2 (29 November 2020)
-----------------------------------

* Minor syntax fix (adding space) for PHP 8.0 compatibility

RedBeanPHP 5.6.1 (21 October 2020)
----------------------------------

* Fixed [issue](https://github.com/gabordemooij/redbean/issues/841) with R::bindFunc and shared lists in some cases (Gabor)

RedBeanPHP 5.6 (04 October 2020)
--------------------------------

* Added [DDL-templates](https://redbeanphp.com/templates) (Gabor)
* Added bean->info() and [R::findFromSQL()](https://redbeanphp.com/querying#find_from_sql) (Gabor)
* Added [getDatabaseServerVersion()](https://redbeanphp.com/database) (Gabor)
* Fix unnecessary widening when storing 1 in a MySQL TINYINT(1) column #839. (Gabor, thanks davidsickmiller)
* Preventing RedBean from trying to call protected or private methods (Lynesth)
* Allowing the use of __call in the model (Lynesth)
* Allow overriding stringifyFetch with setPDO (Gabor)
* Adjust setPDO in RPDO to avoid having pdo instance replaced (Gabor)
* Added support for SQL Select Snippets in CTE-Queries (Gabor)
* Added support for MySQL8 (Gabor)
* New plugin: [RedSeed](https://redbeanphp.com/index.php?p=/plugins#redseed) (Ben Major)
* New plugin: [RDB RedBeanPHP Wrapper](https://redbeanphp.com/index.php?p=/plugins#RDB) (Taeluf)

RedBeanPHP 5.5 (30 April 2020)
------------------------------

* [SQL-Extensions](https://redbeanphp.com/extended_sql) @joined/@own/@shared** (Lynesth)
* [R::countChildren()/R::countParents()](https://redbeanphp.com/trees#counting_in_trees) (Gabor)
* [Finder::onmap()/R::loadJoined()](https://redbeanphp.com/finding#also) (Gabor)
* Execution bit removed from PHP files (Travispaul)
* Plug-ins may now also contain underscores (Lynesth)
* Arrays are now allowed as meta mask (Lynesth)
* Minor performance improvement in convertToBeans (Lynesth)
* Improved checking in LIMIT-1 glue (Lynesth)
* Fix issues in Hybrid mode (Gabor/MadTeddy)
* Make convertToBean compatible with getRow (Gabor/Flip111)
* Fix in OODBBean changelist (AlexanderYIXIAO)
* Fix in testPartialBeansAtSetup (AlexanderYIXIAO)
* Removal of AutoResolve (Gabor/Lynesth/Rayraz)*

** works in every SQL-snippet also in (CTE)-trees

* **possible breaking change** - Due to a bug, the AutoResolve feature never worked in Frozen mode unless you had a table with the same name as the resolved bean type. We tried to fix this but the complexity was going through the roof and Rayraz pointed out this the feature was actually at odds with the whole RedBeanPHP philosophy. So I decided to kill it. Although this is a backward incompatible change we do not expect users to notice due to the fact nobody reported the bug and the whole feature was defect in Frozen mode. Therefore, it looks safe to remove the code. For fluid mode this might pose a breaking change, however fluid systems are not supposed to run on production machines in the first place. In the worst case you have to adjust your development environment in order to update. Because I do not believe this is a real breaking change (the feature did not work at all and nobody reported it) I decided not to update the major version number.

RedBeanPHP 5.4.2 (26 December 2019)
-----------------------------------

* Fix [issue](https://github.com/gabordemooij/redbean/commit/58d366ac135cf14c7b952cda075a7723dfb425a7) with Hybrid Mode not working as documented (Gabor)

RedBeanPHP 5.4.1 (7 December 2019)
----------------------------------

* Fix [issue](https://github.com/gabordemooij/redbean/pull/755) with default values in combination with Partial Beans mode (author Alexander YI)
* Fix minor [issue](https://github.com/gabordemooij/redbean/pull/753) in Unit Test system (author Gabor, thanks for reporting Alexander YI)
* Update test file for PHP 7.4 compatibility (author Gabor)

RedBeanPHP 5.4 (1 October 2019)
-------------------------------

* Debug Logger now correctly handles **typed bindings** (author AbygailG)
* R::store( $beans, [$unfreezeIfNecessary](https://redbeanphp.com/fluid_and_frozen#hybrid)); (author Gabor, inspiration from PR David Sickmiller)
* R::storeAll( $beans, [$unfreezeIfNecessary](https://redbeanphp.com/fluid_and_frozen#hybrid));
* **R::findForUpdate()** (author Gabor)
* **R::traverse(...,function( ,$depth){})** passes depth level (author Lynesth)
* Allow findLike (and the likes) to use **"IS NULL"** conditions (author Lynesth)
* Have trash/trashAll return **number of deleted beans** (author Lynesth)
* Fixed **Facade::removeToolBoxByKey** removing the toolbox (thanks Dmelo)
* **R::getRow()** now adheres to return type array (author Nucc1)
* **R::setAllowFluidTransactions()** (thanks Lynesth and Marios88)
* Peformance improvement of R::diff() (author Lynesth)
* Fix Cache prevent a second FOR-UPDATE SQL query (author Gabor)
* Additional unit tests
* Improvement source code documentation

Changes in version 5.3.1 (1 June 2019)
--------------------------------------

* Improved performance for advanced mapping functions map() and NMMap() (thanks [mario88](https://github.com/marios88))
* Minor fixes in source annotations

Changes in version 5.3 (6 April 2019)
-------------------------------------

* [Explicit parameter type binding](https://redbeanphp.com/finding#explicit_params) (thanks [Lynesth](https://github.com/Lynesth))
* [Added countTaggedAll() and countTagged()](https://redbeanphp.com/labels__enums__tags#countTagged)
* [Added R::useFeatureSet()](https://redbeanphp.com/welcome#featureset)
* [Added nmMap() for complex FindMulti mappings](https://redbeanphp.com/finding#sqn)
* [Released independent SQN library for quick SQL notation in PHP](http://gabordemooij.com/sqn/)
* Added R::noNuke()
* Support for MySQL SSL: useMysqlSSL( $key, $cert, $ca, $id )
* Support for PHP 7.3

Changes in version 5.2 (1 November 2018)
----------------------------------------

* Allow to specify the use of [partial beans in R::setup()](https://redbeanphp.com/database#partialbeansetup) and R::addDatabase() (author: Lynesth)
* Refactoring &__get() (author: Lynesth)
* Small code optimization of getAssoc function (author: Lynesth)
* Fix Prevent R::selectDatabase from changing BeanHelper (author: Lynesth)
* Fix Can't select sqlite if not set (author: Lynesth)
* Fix test issue with MariaDB with JSON (author: Gabor)
* Code refactoring to bail out of parseJoin faster (author: Lynesth)
* Refactoring import() (author: Lynesth)
* Make unit tests more strict, trow an exception for every notice (author: Gabor)
* Allow [OODBBeans as conditions](https://redbeanphp.com/finding#beanconditions) for findLike (author: Lynesth)
* Use **cache for queryRecordCount** (author: Lynesth)
* Use **cache everywhere** possible (author: Lynesth)
* getOwnList and countOwn simple refactoring (author: Lynesth)
* Allow models to provide a [jsonSerialize return](https://redbeanphp.com/models#jsonret) (author: Bert Devriese)
* Update queryRecordWithCursor: add flagNarrowFieldMode, sqlFilters, prevent it from breaking cache state (author: Lynesth)
* Add [R::getCursor()](https://redbeanphp.com/api/classes/RedBeanPHP.Facade.html#method_getCursor) function to query cursors with raw SQL (author: Gabor)
* Automatically trim types in [findMulti()](https://redbeanphp.com/finding#beantrimmulti) (author: Lynesth)
* Update R::hunt(): uses findCollection() instead of find() to prevent memory issues when deleting a lot of beans (author: Lynesth)
* [Update R::hunt()](https://redbeanphp.com/finding#hunt52): returns the number of beans that have been deleted (#675) (author: Lynesth)
* [Update R::hunt()](https://redbeanphp.com/finding#hunt52): The sqlSnippet is now optional, allowing to delete a whole table while still calling FUSE hooks (that's the difference with wipe()) (author: Lynesth)
* Add getToolBoxByKey, addToolBoxWithKey and removeToolBoxByKey (author: Gabor)
* Add basic support for [tree traversal using](https://redbeanphp.com/trees#ctetrees)**common table expressions** (author: Gabor)
* Improve support for CUBRID, **re-add CUBRID driver** to Replica2 packager (author: Gabor)
* Allow SQL = NULL for [findMulti](https://redbeanphp.com/finding#multinull) (authors: Gabor and Lynesth)
* Re-added experimental support for [Firebird/Interbase](https://github.com/gabordemooij/redbean/blob/master/RedBeanPHP/QueryWriter/Firebird.php) Databases
* [**PoolDB**](https://redbeanphp.com/plugins#pooldb) plugin (have beans remember their origin database) (authors: Gabor and Lynesth)

Changes in version 5.1 (2 April 2018)
-------------------------------------

* Added [R::trashBatch($type, $ids)](https://redbeanphp.com/crud#trashBatch "learn more about trashBatch.") to trash a batch of beans in one statement
* Added [R::hunt( $type, $query, $params )](https://redbeanphp.com/finding#hunt "learn more about hunt.") to find and trash beans in one statement
* Added Debugger::setOverrideCLIOutput() to override PHP_SAPI in Debugger
* Improved API documentation box()/unbox()
* Improved API documentation matchUp
* Make QuickExport compatible with PHP versions 5.4 and below
* Add warning in API documentation regarding use of findLast()
* Mark R::findLast() as deprecated
* Fixed compatibility issue with PHP 7.2 (thanks Lynesth)
* Increases execution speed if no conditions are set (thanks Lynesth)
* Added DispenseHelper::setEnforceNamingPolicy() to disable naming policy
* Faster return from __call() if no model (thanks Lynesth)
* Updated README and Composer JSON (thanks Rotzbua)
* Added Composer Model documentation (thanks Ben Major)
* Fix Facade::convertToBean documentation (thanks Diogo Oliveira de Melo)
* Reached 100% test coverage
* Code clean-ups
* Improved other documentation
* Tiny Query Builder now available as plugin for your convenience
* Improved performance of modifySchema() (thanks davidsickmiller)
* Fixed a compatibility issue with ProxySQL in connection mechanism

Changes in version 5.0 (31 October 2017)
----------------------------------------

* Simplified [Exceptions](https://redbeanphp.com/crud#loadexception) for load() functions
* By default R::load() and R::loadForUpdate() will now throw exceptions if a bean cannot be loaded due to a lock timeout
* Support for [JSON columns](https://redbeanphp.com/crud#json) has been extended.
* Update .gitignore (thanks jreklund)
* Update Composer aliasing in readme (thanks benmajor)
* Make filter function in look() [optional](https://github.com/gabordemooij/redbean/commit/3cb153c5d4f49fede3c8828a6710cf4e11633ca4)
* [Added R::loadForUpdate()](https://redbeanphp.com/changelog?p=crud#lock) to load and lock a bean
* Separate versions for MySQL, Postgres and SQLite as well as combined
* Storage of [partial beans](https://redbeanphp.com/changelog?p=/database#partialBeans)
* [R::look(...)](https://redbeanphp.com/changelog?p=data_tools#look) perform query and put result in template
* [R::matchUp(...)](https://redbeanphp.com/changelog?p=data_tools#matchup) match-and-update in one go (easy to create login functionality)
* [R::csv(...)](https://redbeanphp.com/changelog?p=data_tools#csv) create a CSV file from a query
* [R::diff(...)](https://redbeanphp.com/changelog?p=data_tools#diff) returns a diff between a pair of beans
* Added setEnforceUTF8Encoding to fix issue with stringifying binary data
* Added [exists()](https://redbeanphp.com/changelog?p=many_to_one#exists) to bean to check for relation
* Fixed notice in Facade inproper use of reset()
* Added missing validations for findOrDispense and findOneOrDispense
* Support for utf8mb4_unicode_520_ci ([thanks Johan](https://github.com/jreklund))

Changes in version 4.3.4 (March 2017)
-------------------------------------

* Various minor fixes (github issues 530, 531 and 544)

Changes in version 4.3.3 (October 2016)
---------------------------------------

* Automatic unboxing for Simple Models if necessary (instead of exception)
* Added findOrDispense() to facade
* Remove support for PHAR, it makes no sense PHP is not JAVA
* Using var_dump instead of print_r in classic debugger for clarity
* Fixed a minor toString issue in FUSE
* Fixed issue in fancy debugger causing bindings to appear incorrectly
* Fixed issue where multi zero string got converted to INT ([#525](https://github.com/gabordemooij/redbean/issues/525))

Changes in version 4.3.2 (May 2016)
-----------------------------------

* Added [meta-masks](https://redbeanphp.com/changelog?p=meta_data#masks)
* Added R::convertToBean - for single rows
* Added R::hasDatabase
* Added some color to fancyDebug
* Beans now implement the jsonSerializable interface if available
* Support for JSON columns in Postgres (manual only to avoid breaking stuff)
* Improved source comments

Changes in version 4.3.1 (January 2016)
---------------------------------------

* Added more source code documentation to clarify handling of NULL in FUSE
* Fixed a minor issue with backticks in fluid mode
* Added a try-catch to avoid errors with Postgres unremovable views (nuke)

Changes in version 4.3.0 (October 2015)
---------------------------------------

* Add source code highlighting in docs for API
* Compatibility with **PHP 7**
* Compatibility with **HHVM**
* Added **one()** for basic 1-1 support in OODBBean
* Added support for **NUMERIC** fields (fixed precision) in MySQL/Postgres
* Added proper MarkDown markup to source code documentation
* Moved inline facade functions to new Utility Classes.
* Changed DSN trigger_error into RedException
* Bundled handy test shell scripts for unit testing RB
* Clean up source code documentation

Changes in version 4.2.5 (July 2015)
------------------------------------

* [Fixed notice](https://github.com/gabordemooij/redbean/issues/458#issuecomment-125217106 "See Github issue") when selecting invalid database (now throws Exception instead).

Changes in version 4.2.4 (June 2015)
------------------------------------

* Fixed a minor issue with findOne handling redundant LIMIT clauses

Changes in version 4.2.3 (June 2015)
------------------------------------

* Fixed information schema performance issue in fluid mode on large MySQL servers (with lots of databases).
* Very very tiny performance optimization for PHP interpreters: using commas instead of dots (but it's a cute trick) - thanks 'dseguy'

Changes in version 4.2.2 (May 2015)
-----------------------------------

* Added OODB::autoClearHistoryAfterStore()

Changes in version 4.2.1 (May 2015)
-----------------------------------

* Added a function to set the maximum for integer parameter binding (for edge cases).
* Conditional deprecated PGSQL ATTR constant for compatibility with PHP 7
* Some clean-up in inline documentation

Changes in version 4.2.0 (April 2015)
-------------------------------------

* **NEW**[Automatically resolve aliases using foreign key inspection](https://redbeanphp.com/one_to_fixed#autoresolve "Learn about autoresolve")
* **NEW**[Support for cursors (for large datasets)](https://redbeanphp.com/finding#cursors "Learn about cursors")
* **NEW**[R::findOrCreate() to directly create a bean with certain values if it does not exist yet](https://redbeanphp.com/finding#find_create "Learn more about FindOrCreate")
* **NEW**[R::findLike](https://redbeanphp.com/finding#find_like "Learn about the R::findLike() feature") to find beans using an criteria array
* **NEW**[Added $bean->hasListChanged()](https://redbeanphp.com/meta_data#has_list_changed "Learn about hasListChanged")
* **NEW** Re-added CUBRID QueryWriter to main repository again
* **NEW**[Easy logging functions](https://redbeanphp.com/database#logging "Easy Logging")
* **NEW**[Deepfreeze](https://redbeanphp.com/fluid_and_frozen#deepfreeze "Learn about the deepfreeze script")
* **NEW**[Global aliases: R::aliases( ... )](https://redbeanphp.com/one_to_fixed#global_aliases "Learn more about global aliases")
* **NEW**[Query Counter](https://redbeanphp.com/database#query_counter "Learn about the new Query Counter")
* **NEW** You can now configure error handling in models (if model does not exist etc...) see [API](https://redbeanphp.com/api/class-RedBeanPHP.OODBBean.html#_setErrorHandlingFUSE "Specify bean-model error handling.")
* **NEW** You can now use R::fancyDebug() to see parameters embedded in SQL
* **NEW** Improved caching system
* **NEW** New, cleaner QueryWriter architecture
* **NEW** Added GetOne() method in driver (improve ADODB compatibility).
* **NEW** Added findMulti, for complex mappings.

Backward incompatible changes
-----------------------------

* Build commands like 'buildcomamnd.unique' are no longer supported (I always said not to rely on them).

Changes in version 4.1.4 (Februari 2015)
----------------------------------------

* Fixed [slot-issue](https://github.com/gabordemooij/redbean/issues/407) in debugger (mode 2)
* Added extra MySQL type 7 to avoid [utf8mb4-innodb-index](https://github.com/gabordemooij/redbean/issues/411) issues
* Fixed [export issue](https://github.com/gabordemooij/redbean/issues/408) with certain FUSE hooks
* Add feature to [throw exception](https://github.com/gabordemooij/redbean/issues/406) or trigger error if a FUSE method does not exist
* Re-added static $f for backward compatibility with 3.5 SQL Helper
* Fixed some issues with CUBRID compatibility, re-integrated CUBRID support in master

Changes in version 4.1.3 (December 2014)
----------------------------------------

* PostgreSQL money fields now accept more currencies
* Improved caching by allowing multiple cache entries per tag

Changes in version 4.1.2 (November 2014)
----------------------------------------

* Added @joined syntax feature to countOwn as well
* Adjusted clone-syntax to comply with strict PHP code sniffers
* R::$toolboxes R::$toolbox and R::$currentDB are public again for your convenience

Changes in version 4.1 (October 2014)
-------------------------------------

* R::findOne() adds LIMIT 1 to query if no LIMIT clause is found
* R::tagged() and R::taggedAll() now accept SQL for pagination
* Improved performance parent bean saving
* Improved method signature of dup: [R::duplicate](https://redbeanphp.com/duplicate#duplicate "Improved the method signature of R::dup with R::duplicate")
* Custom beans through REDBEAN_OODBBEAN_CLASS constant
* Allow some [JOINS](https://redbeanphp.com/using_sql_snippets#joins "Read more about JOINS in own-lists") in with/withCondition for own-lists.
* Improved support for [UUIDs/GUIDs](https://redbeanphp.com/uuids "Learn about improved support for UUIDs/GUIDs"). This feature has been backported to _4.0.5_ as well.
* [Column functions](https://redbeanphp.com/database#column_functions "Learn more about column functions."): bind a function to a column
* Improve setup time by providing direct PDO setter (use with care!)
* Add a method to [test](https://redbeanphp.com/debugging#test_connection "Use R::testConnection() to test the database connection.") the database connection
* Add new [debug mode](https://redbeanphp.com/debugging#debugger2 "New debug mode with bindings already filled in.") with query parameters filled in
* Add new [debug function](https://redbeanphp.com/debugging#dump "Handy debug function, dump bean or array of beans. Short output.") to inspect beans and arrays of beans
* Treat beans in own-list as shared list: [aggregated list](https://redbeanphp.com/other_relations#aggr "Treat two complimentary own-lists (N-1 relations) as a shared list (N-M): N11N relation.")
* Split OODB in two repositories: frozen and fluid (no API changes)
* Regular maintenance & clean up
* Additional tests

Backward incompatible changes
-----------------------------

RedBeanPHP 4.1 should be fully backward compatible. However, there is one change that may affect some code relying on undefined behaviour. In 4.1 a bean will only be saved if it has been changed through the setter (meta: changed). If a bean is tainted by accessing its lists it will perform all save operations but not fire the actual SQL query if no changes have been made to the bean itself. If for some reason you relied on the redundant SQL query you might want to set the 'changed' meta property manually. You can also implement this system-wide by extending the SimpleModel.

Changes in version 4.0 (April 2014)
-----------------------------------

* PHP native namespaces
* [Exclusive own-list](https://redbeanphp.com/relations#exclusive-one-to-many "Learn more about exclusive one-to-many")
* Tree [Traversal](https://redbeanphp.com/trees "Learn more about traverse") function
* 10% performance improvement for basic CRUD operations
* Performance improvements for bean conversion
* Improved Array Access interface (you can now use arrays instead of beans all the time)
* Improved handling of unique constraints
* Added EID() function to easily insert ENUM bean IDs in queries
* Constraints now also use ON UPDATE CASCADE
* Dispense works more consistently now
* Fixed an issue with type of return ID value in Postgres driver
* Fixed possible cache collision issue
* Performance improvements for fluid mode
* Big clean-up: removed Cooker/Graph (use dispense), Preloader (plugin), BeanCan Server (plugin)
* CUBRID driver still available but as plugin

Version 4 FAQ
-------------

This is a list of questions and answers regarding the 4.0 release.

### Why has the Preloader been removed?

When I wrote the preloader, the original purpose was to prevent for-each loops to fire queries when retrieving the parent of a bean. Later I added the writer cache which could take care of this but was turned off by default. In RedBeanPHP the writer cache is turned on by default solving the original problem. Meanwhile people requested all kinds of new features for the Preloader like support for loading own-lists, shared-lists and even aliases and SQL snippets. It even got its own syntax. I decided to remove the preloader because I believe simple SQL is better suited to query large amounts of records all at once for overviews and reports.

 This functionality is still available as a [plugin](https://redbeanphp.com/plugins#legacy "Plugin").

### Why has graph() been removed from core?

R::graph() was a powerful feature to load and updates beans directly from forms. However the graph() function assumed you were also using FUSE for validation. Otherwise the function could lead to serious architectural and security defects. I fixed this in version 3, but then it became less powerful, so in version 4 I decided to remove it entirely from the core.

 This functionality is still available as a [plugin](https://redbeanphp.com/plugins#legacy "Plugin").

 Also note that the new R::dispense() method works much like the old graph() method.

### Why is R::associate gone?

The R::associate() method (as well as unassociate etc...) is a relic from the past. In the earliest versions of RedBeanPHP I believed you only needed many-to-many relations. Although this was true, performance became a real bottleneck. I had to find a way to apply the on-the-fly philosophy to N-1 relations as well, this resulted in the introduction of own-lists and shared-lists. Since then, I kept the old associate() method for backward compatibility reasons. In version 4 however I decided to finally clean up.

### Why are the BeanCan Servers gone?

They blurred the distinction between plugin and core. Also, the RedBeanPHP Adaptive branch is going more in the direction of a framework which is a better place for BeanCan as well. RedBeanPHP 4 returns to the core of the library: on-the-fly ORM. Another reason is that it turns out it is pretty much impossible to prescribe the interface of a JSON or REST API.

 This functionality is still available as a [plugin](https://redbeanphp.com/plugins#legacy "Plugin")

New in RedBeanPHP 3.5.7
-----------------------

This is a minor maintenance update.

* Fixed issue in QueryWriter cache (3.5.7b)
* Improved stacktrace in SQL exception
* Improved performance of convertToBeans() method
* Allow duplication of trees
* With now also works with joins

back to [main menu](https://redbeanphp.com/menu)

Donate to RedBeanPHP using Monero:

 47mmY3AVbRu 7zVVd4bxQnzD

 2jR7PQtBJ cF93jWHQ

 rP7yRED4qr fqu6G9Q8ZNu7

 zqwnB28rz76 w7MaExf

 mALVg69yFd 9sUmz

 (remove spaces and new lines)

 Performance monitor: this page has been generated in 0.025546789169312s. Is the performance lacking? Please drop me an e-mail to notify me!

Partners

[PapelDigital](http://www.papeldigital.eu/index.html "PapelDigital | ideias com sentido")

RedBeanPHP Easy ORM for PHP © 2026 [Gabor de Mooij](http://www.gabordemooij.com/ "My homepage") () and the RedBeanPHP community ([credits](https://redbeanphp.com/credits "Credits")) - [Licensed New BSD/GPLv2](https://redbeanphp.com/license "License details for RedBeanPHP") - [RedBeanPHP Archives](https://redbeanphp.com/archives "Looking for old manuals?")

RedBeanPHP, the power ORM for PHP since 2009.

[Privacy Statement](https://redbeanphp.com/privacy.pdf "Privacy statement (pdf).")
