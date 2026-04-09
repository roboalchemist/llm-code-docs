Package org.jbake.app

# Class DBUtil

java.lang.Object
org.jbake.app.DBUtil

---

public class DBUtil
extends Object

- 

## Constructor Summary

Constructors

Constructor
Description
`DBUtil()`
 

- 

## Method Summary

Modifier and Type
Method
Description
`static void`
`closeDataStore()`
 
`static ContentStore`
`createDataStore(String type,
 String name)`

Deprecated.

`static ContentStore`
`createDataStore(JBakeConfiguration configuration)`
 
`static DocumentModel`
`documentToModel(com.orientechnologies.orient.core.sql.executor.OResult doc)`
 
`static String[]`
`toStringArray(Object entry)`

Converts a DB list into a String array

`static void`
`updateSchema(ContentStore db)`

Deprecated.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Constructor Details

  - 

### DBUtil

public DBUtil()

- 

## Method Details

  - 

### createDataStore

@Deprecated
public static ContentStore createDataStore(String type,
 String name)
Deprecated.

  - 

### updateSchema

@Deprecated
public static void updateSchema(ContentStore db)
Deprecated.

  - 

### createDataStore

public static ContentStore createDataStore(JBakeConfiguration configuration)

  - 

### closeDataStore

public static void closeDataStore()

  - 

### documentToModel

public static DocumentModel documentToModel(com.orientechnologies.orient.core.sql.executor.OResult doc)

  - 

### toStringArray

public static String[] toStringArray(Object entry)
Converts a DB list into a String array

Parameters:
`entry` - Entry input to be converted
Returns:
input entry as String[]