Package org.jbake.app

# Class Crawler

java.lang.Object
org.jbake.app.Crawler

---

public class Crawler
extends Object
Crawls a file system looking for content.

- 

## Constructor Summary

Constructors

Constructor
Description
`Crawler(ContentStore db,
 File source,
 org.apache.commons.configuration2.CompositeConfiguration config)`

Deprecated.
Use `Crawler(ContentStore, JBakeConfiguration)` instead.

`Crawler(ContentStore db,
 JBakeConfiguration config)`

Creates new instance of Crawler.

- 

## Method Summary

Modifier and Type
Method
Description
`void`
`crawl()`
 
`void`
`crawlDataFiles()`
 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Constructor Details

  - 

### Crawler

@Deprecated
public Crawler(ContentStore db,
 File source,
 org.apache.commons.configuration2.CompositeConfiguration config)
Deprecated.
Use `Crawler(ContentStore, JBakeConfiguration)` instead.
 

 Creates new instance of Crawler.

Parameters:
`db` - Database instance for content
`source` - Base directory where content directory is located
`config` - Project configuration

  - 

### Crawler

public Crawler(ContentStore db,
 JBakeConfiguration config)
Creates new instance of Crawler.

Parameters:
`db` - Database instance for content
`config` - Project configuration

- 

## Method Details

  - 

### crawl

public void crawl()

  - 

### crawlDataFiles

public void crawlDataFiles()