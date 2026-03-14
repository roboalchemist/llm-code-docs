# Source: https://redbeanphp.com/trees

Title:

URL Source: https://redbeanphp.com/trees

Markdown Content:
RedBeanPHP :: Trees
===============

[![Image 1: RedBeanPHP logo, a white bean on a red square.](https://redbeanphp.com/img/redbeanphp_logo.png)](https://redbeanphp.com/)
RedBeanPHP

The Power ORM
=========================

* [](http://github.com/gabordemooij/redbean "(EXTERNAL LINK) Contribute to RedBeanPHP or fork the repository on Github.")
* [Travis](https://www.travis-ci.com/github/gabordemooij/redbean "(EXTERNAL LINK) Read the latest test report on Travis-CI.")
* [API](https://redbeanphp.com/api/namespaces/RedBeanPHP.html "Discover hidden treasures in RedBeanPHP ORM with the API documentation.")
* [Forum](http://groups.google.com/forum/?fromgroups#!forum/redbeanorm "(EXTERNAL LINK) Ask questions or help others at the RedBeanPHP forum.")
* [Sponsor](https://redbeanphp.com/trees?p=/welcome#sponsor "Sponsor")

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
  * Trees
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

Trees
=====

RedBeanPHP supports **self-referential** relationships. In RedBeanPHP terminology, these are called trees. Here is an example, let's decorate a christmas tree with some candy canes:

```
$cane = R::dispense('cane',10);    $cane[1]->ownCane = [ $cane[2], $cane[9] ];    $cane[2]->ownCane = [ $cane[3], $cane[4] ];    $cane[4]->ownCane = [( $cane[5],                $cane[7], $cane[8] ];    $cane[5]->ownCane = [ $cane[6] ];    $id = R::store( $cane[1] );    $root = R::load( 'cane', $id );    echo $root->ownCane[2]->ownCane[4]        ->ownCane[5]->ownCane[6]->id;    //outputs: 6
```

Trees are just a special case of lists, you use a list with the same name as the parent type. In the example script above, a **cane** has an **ownCaneList**. Another example: _page->ownPageList_. As you can see in the example above you can navigate the lists using the IDs.

Traversal
---------

Instead of manually looping through each own-list of a bean you can use the traverse() method:

```
$page->traverse( 'ownPage', function( $page ) {        ....    } );
```

This allows you to recursively apply a function to a list. To limit the results when accessing a list you can use the with/withCondition() method:

```
$page->with( ' LIMIT 10 ')->traverse( ... );    $page->withCondition( '  rating > ? ', [ 5 ] )->traverse( ... );
```

You can also use **withCondition** and **alias** together with the traverse function.

 Use the third parameter to specify the maximum depth:

```
$page->traverse( 'ownPage', $func, 3 ); //max 3 levels
```

Use the PHP **use** statement to import variables into the function scope:

```
$task->traverse( 'ownTask', function( $task ) use ( &$todos ) {        $todos[] = $task->name;    } );
```

The traverse() function does not check for _recursion_ in trees.

Traversing upwards
------------------

You can also traverse the other way around, here is a quick example:

```
$page = R::dispense('page');    $page->title = 'chapter';    $page2 = R::dispense('page');    $page2->title = 'article';    $page3 = R::dispense('page');    $page3->title = 'text';    $page->ownPageList[] = $page2;    $page2->ownPageList[] = $page3;    R::store($page);    $p = $page3->fresh();    $p->traverse('page', function($parent) {            echo $parent->title. PHP_EOL;    });
```

Importing Trees
---------------

Do you want to import a hierarchical data structure ? This can be accomplished using the [R::dispense()](https://redbeanphp.com/import_and_export "Import trees with dispense().") feature.

Faster trees (5.2+)
-------------------

If your database supports **common table expressions** (Postgres, MariaDB 10.3+) you can use the CTE-based tree tools as well:

```
$pages = R::dispense(array(        '_type' => 'page',        'title' => 'home',        'ownPageList' => array(array(            '_type' => 'page',            'title' => 'shop',            'ownPageList' => array(array(                '_type' => 'page',                'title' => 'wines',                'ownPageList' => array(array(                    '_type' => 'page',                    'title' => 'whiskies',                ))            ))        ))    ));
```

Given the page hierarchy of the shop above you can use R::parents() and R::children() like this:

```
R::parents( $whiskyPage, ' ORDER BY title ASC ' );    //gives: home,shop,whiskies,wines        R::children( $homePage, ' ORDER BY title ASC ' ) );    //gives:home,shop,whiskies,wines        R::children( $winePage, ' title NOT IN (\'wines\') ORDER BY title ASC ' );    //whiskies        R::parents( $winePage, '  title NOT IN (\'home\') ORDER BY title ASC ' );    //shop,wines
```

Because this approach uses common table expressions the performance is much better.

Caution! This is a new, **experimental** feature available as of RedBeanPHP 5.2. The CTE API has been tested but may still contain bugs. Also the CTE API may be subject to change in future versions.

Counting in Trees (5.5)
-----------------------

To count beans in trees use R::countParents() or R::countChildren.

```
R::countParents( $whiskyPage );    R::countChildren( $winePage, ' title != :title  ', [ ':title' => 'wines' ] );
```

As of 5.6 you can add your own SELECT clause like 'count(distinct vendor)'. By default, countChildren() and countParents() subtract 1 from total number of counted records to exclude the starting bean. If you provide your own select clause (or an SQL snippet), this might not make sense, so it won't happen in that case.

back to [main menu](https://redbeanphp.com/menu)

Donate to RedBeanPHP using Monero:

 47mmY3AVbRu 7zVVd4bxQnzD

 2jR7PQtBJ cF93jWHQ

 rP7yRED4qr fqu6G9Q8ZNu7

 zqwnB28rz76 w7MaExf

 mALVg69yFd 9sUmz

 (remove spaces and new lines)

 Performance monitor: this page has been generated in 0.025415182113647s. Is the performance lacking? Please drop me an e-mail to notify me!

Partners

[PapelDigital](http://www.papeldigital.eu/index.html "PapelDigital | ideias com sentido")

RedBeanPHP Easy ORM for PHP © 2026 [Gabor de Mooij](http://www.gabordemooij.com/ "My homepage") () and the RedBeanPHP community ([credits](https://redbeanphp.com/credits "Credits")) - [Licensed New BSD/GPLv2](https://redbeanphp.com/license "License details for RedBeanPHP") - [RedBeanPHP Archives](https://redbeanphp.com/archives "Looking for old manuals?")

RedBeanPHP, the power ORM for PHP since 2009.

[Privacy Statement](https://redbeanphp.com/privacy.pdf "Privacy statement (pdf).")
