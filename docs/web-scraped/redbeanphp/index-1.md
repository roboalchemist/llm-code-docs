# Source: https://redbeanphp.com/?p=/welcome

Title:

URL Source: https://redbeanphp.com/?p=/welcome

Markdown Content:
RedBeanPHP :: Welcome
===============

[![Image 1: RedBeanPHP logo, a white bean on a red square.](https://redbeanphp.com/img/redbeanphp_logo.png)](https://redbeanphp.com/)
RedBeanPHP

The Power ORM
=========================

* [](http://github.com/gabordemooij/redbean "(EXTERNAL LINK) Contribute to RedBeanPHP or fork the repository on Github.")
* [Travis](https://www.travis-ci.com/github/gabordemooij/redbean "(EXTERNAL LINK) Read the latest test report on Travis-CI.")
* [API](https://redbeanphp.com/api/namespaces/RedBeanPHP.html "Discover hidden treasures in RedBeanPHP ORM with the API documentation.")
* [Forum](http://groups.google.com/forum/?fromgroups#!forum/redbeanorm "(EXTERNAL LINK) Ask questions or help others at the RedBeanPHP forum.")
* [Sponsor](https://redbeanphp.com/?p=/welcome#sponsor "Sponsor")

* **Introduction**
  * Welcome
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
  * [Changelog](https://redbeanphp.com/changelog "Changelog")
  * [Roadmap](https://redbeanphp.com/roadmap "Roadmap")
  * [Beta](https://redbeanphp.com/beta "Beta")
  * [About](https://redbeanphp.com/about "About")
  * [Plugins](https://redbeanphp.com/plugins "Plugins")
  * [SQN](https://redbeanphp.com/sqn "SQN")
  * [Frameworks](https://redbeanphp.com/frameworks "Frameworks")
  * [Menu](https://redbeanphp.com/menu "Menu")

Welcome
=======

RedBeanPHP is a powerful, **zero config****object relational mapper**.

News
----

2025-05-30: [RedBeanPHP 5.7.5](https://redbeanphp.com/changelog#v575)**New**

2024-03-16: Added PHP 8.3 to Travis-CI test matrix

2023-03-18: [RedBeanPHP 5.7.4](https://redbeanphp.com/changelog#v574)

2022-10-08: [RedBeanPHP 5.7.3](https://redbeanphp.com/changelog#v573)

2022-04-02: [RedBeanPHP 5.7.2](https://redbeanphp.com/changelog#v572)

2021-10-31: [RedBeanPHP 5.7.1](https://redbeanphp.com/changelog#v571)

2021-04-03: [RedBeanPHP 5.7](https://redbeanphp.com/changelog#v57)

2020-10-04: [RedBeanPHP 5.6](https://redbeanphp.com/changelog#v56)

2020-04-30: [RedBeanPHP 5.5](https://redbeanphp.com/changelog#v55)

2019-10-01: [RedBeanPHP 5.4](https://redbeanphp.com/changelog#v54)

2019-04-06: [RedBeanPHP 5.3](https://redbeanphp.com/changelog#v53)

2018-11-05: [RedBeanPHP 5.2](https://redbeanphp.com/changelog#v52)

2017-10-31: [RedBeanPHP 5.0](https://redbeanphp.com/changelog#v50)

DEMO: Quickly import CSV
------------------------

Let's import a CSV of country codes in just about a minute, including the time to download and install RedBeanPHP!

![Image 2: Import a country code CSV-file within 10 seconds, including downloading and installing RedBeanPHP.](https://redbeanphp.com/img/quick_redbean_demo.gif)

 With RedBeanPHP you don't need to design your database schema upfront, you don't need a database administrator, you don't need endless configuration files in yaml, xml or json, you don't need hundreds of untrusted dependencies or a sluggish framework, just one file and go!

Code Example
------------

This is how you do **CRUD** in RedBeanPHP:

```
require 'rb.php';    R::setup();    //for version 5.3 and higher    //optional but recommended    R::useFeatureSet( 'novice/latest' );    $post = R::dispense( 'post' );    $post->text = 'Hello World';    //create or update    $id = R::store( $post );    //retrieve    $post = R::load( 'post', $id );        //delete    R::trash( $post );
```

This **automatically generates** the database, tables and columns... **on-the-fly**. It infers relations based on naming conventions. RedBeanPHP also makes it very easy to work with **trees** in databases:

```
$pages = R::children( $site, $extraSQL );
```

RedBeanPHP uses recursive table expressions to deal with tree structures in your database to _improve performance_ (to use this feature you need a database that supports RCTEs like MySQL 8.0.1+, MariaDB 10.2.2+ or PostgreSQL 9+). Learn more about RedBeanPHP [trees](https://redbeanphp.com/trees).

In RedBeanPHP 5.3 and higher you can use **R::useFeatureSet( 'novice/latest' )** to automatically select the latest features. If you are working on an older code base you can ommit this line. The **latest** keyword means that you want to use the latest features. The **novice** keyword means that some dangerous features like R::nuke() will be turned off. You can also specify a specific RedBeanPHP version like 5.3 (minimum).

Zero Config
-----------

No verbose **XML** files, no annoying **annotations**, no **YAML** or **INI**. **Zero Config**. Just start coding.

Fluid Schema
------------

During development, RedBeanPHP will adapt the database schema to fit your needs, giving you the **NoSQL** experience. When deploying to production servers, you can freeze the schema and benefit from performance gains and referential integrity.

 RedBeanPHP offers the best of both worlds!

Powerful
--------

RedBeanPHP features: **auto-discovery** of models, **fast trees**, **deep copying** and **smart import**.

 Write **less**, do **more**!

Compatible
----------

RedBeanPHP strives to support all **ALL****Free**, **Open Source** databases.

Currently, RedBeanPHP supports: **MySQL**, **MariaDB**, **SQLite**, **PostgreSQL**, **CUBRID** and **Firebird/Interbase*****. RedBeanPHP supports PHP version HHVM, 5.3.0-5.3.2**, 5.3.3, 5.4, 5.5, 5.6, 6.0*, 7.0, 7.1, 7.2, 7.3, 7.4, 8.0, 8.1, 8.2 and 8.3. We take backward compatibility very serious! RedBeanPHP has a track record of **20 years** of PHP **language level compatibility** without a **single breaking change!** You can **trust** RedBeanPHP.

*=partial (according to community)

**=requires patch

***=experimental

Quality Software
----------------

The library has been **created in 2009** and is now considered quite mature. No major bugs have been found since 2013 and only minor features have been added in recent years. The code base is being tested with every change, there are over **20338*** unit tests (**100% code coverage**) for PHP **5.3-latest** and all supported databases. The project is **actively maintained** and we take **backward compatibility** _very_ serious. The code is **well-documented**. RedBeanPHP is trusted by many developers worldwide and has over **2.1** million installs on [packagist](https://packagist.org/packages/gabordemooij/redbean) alone! (since 3.5) and **more than 2k stars** on github, furthermore **thousands of projects** have RedBeanPHP as a dependency. Signify keys and checksums are provided.

*=running the **full** (!) unit test suite

Download
--------

Download the easy-to-use one-in-all package, one single file containing the entire RedBeanPHP library! **No composer**, **no auto-loaders**, **no configuration**, just download and run! Go to the [DOWNLOAD](https://redbeanphp.com/download "Download RedBeanPHP") page and download to latest version of RedBeanPHP!

 Github repository: [RedBeanPHP on Github](http://github.com/gabordemooij/redbean).

 Travis-CI Test Dashboard: [RedBeanPHP on Travis](http://travis-ci.org/gabordemooij/redbean).

 API Documentation: [RedBeanPHP API Documentation](https://redbeanphp.com/api/namespaces/RedBeanPHP.html).

 Community Forum: [RedBeanPHP Community Forum](http://groups.google.com/forum/?fromgroups#!forum/redbeanorm).

Your logo on this website?
--------------------------

Notice something strange? There is no **cookie dialog** on this site! That's because I don't track you in any way. I fully respect your privacy and I want to offer you a high-quality website without annoying ads. So, **no ads**, **no cookies**, **no tracking pixels**, **no MBs of Javascript**, **not even server-side tracking**, nothing! That keeps this website **clean**, **very fast**, **secure** and comfy to use. Hell! I don't even know how many visitors there are on this site! To help me keep this website this way, please consider becoming a sponsor of RedBeanPHP and have your company logo on the website! Contact me for more information.

RedBeanPHP is written by [BDFL](https://en.wikipedia.org/wiki/Benevolent_dictator_for_life) Gabor de Mooij and the RedBeanPHP community.

Other Projects
--------------

Also take a look at some of my other projects:

[Stamp Template Engine for PHP](http://stampte.com/) (a strict logic-less template engine).

[The Straight Framework for PHP](https://gabordemooij.com/straight/) (a no-nonsense framework for PHP).

back to [main menu](https://redbeanphp.com/menu)

Donate to RedBeanPHP using Monero:

 47mmY3AVbRu 7zVVd4bxQnzD

 2jR7PQtBJ cF93jWHQ

 rP7yRED4qr fqu6G9Q8ZNu7

 zqwnB28rz76 w7MaExf

 mALVg69yFd 9sUmz

 (remove spaces and new lines)

 Performance monitor: this page has been generated in 0.028444051742554s. Is the performance lacking? Please drop me an e-mail to notify me!

Partners

[PapelDigital](http://www.papeldigital.eu/index.html "PapelDigital | ideias com sentido")

RedBeanPHP Easy ORM for PHP © 2026 [Gabor de Mooij](http://www.gabordemooij.com/ "My homepage") () and the RedBeanPHP community ([credits](https://redbeanphp.com/credits "Credits")) - [Licensed New BSD/GPLv2](https://redbeanphp.com/license "License details for RedBeanPHP") - [RedBeanPHP Archives](https://redbeanphp.com/archives "Looking for old manuals?")

RedBeanPHP, the power ORM for PHP since 2009.

[Privacy Statement](https://redbeanphp.com/privacy.pdf "Privacy statement (pdf).")
