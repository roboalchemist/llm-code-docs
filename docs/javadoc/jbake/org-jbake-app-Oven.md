Package org.jbake.app

# Class Oven

java.lang.Object
org.jbake.app.Oven

---

public class Oven
extends Object
All the baking happens in the Oven!

- 

## Constructor Summary

Constructors

Constructor
Description
`Oven(File source,
 File destination,
 boolean isClearCache)`

Deprecated.
Use `Oven(JBakeConfiguration)` instead
 Delegate c'tor to prevent API break for the moment.

`Oven(File source,
 File destination,
 org.apache.commons.configuration2.CompositeConfiguration config,
 boolean isClearCache)`

Deprecated.
Use `Oven(JBakeConfiguration)` instead
 Creates a new instance of the Oven with references to the source and destination folders.

`Oven(JBakeConfiguration config)`

Create an Oven instance by a `JBakeConfiguration`

`Oven(Utensils utensils)`

Create an Oven instance with given `Utensils`

- 

## Method Summary

Modifier and Type
Method
Description
`void`
`bake()`

All the good stuff happens in here...

`void`
`bake(File fileToBake)`

Responsible for incremental baking, typically a single file at a time.

`org.apache.commons.configuration2.CompositeConfiguration`
`getConfig()`

Deprecated.

`List<Throwable>`
`getErrors()`
 
`Utensils`
`getUtensils()`
 
`void`
`setConfig(org.apache.commons.configuration2.CompositeConfiguration config)`

Deprecated.

`void`
`setupPaths()`

Deprecated.
There is no need for this method anymore.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Constructor Details

  - 

### Oven

@Deprecated
public Oven(File source,
 File destination,
 boolean isClearCache)
     throws Exception
Deprecated.
Use `Oven(JBakeConfiguration)` instead
 Delegate c'tor to prevent API break for the moment.

Parameters:
`source` - Project source directory
`destination` - The destination folder
`isClearCache` - Should the cache be cleaned
Throws:
`Exception` - if configuration is not loaded correctly

  - 

### Oven

@Deprecated
public Oven(File source,
 File destination,
 org.apache.commons.configuration2.CompositeConfiguration config,
 boolean isClearCache)
     throws Exception
Deprecated.
Use `Oven(JBakeConfiguration)` instead
 Creates a new instance of the Oven with references to the source and destination folders.

Parameters:
`source` - Project source directory
`destination` - The destination folder
`config` - Project configuration
`isClearCache` - Should the cache be cleaned
Throws:
`Exception` - if configuration is not loaded correctly

  - 

### Oven

public Oven(JBakeConfiguration config)
Create an Oven instance by a `JBakeConfiguration`
 

 It creates default `Utensils` needed to bake sites.

Parameters:
`config` - The project configuration. see `JBakeConfiguration`

  - 

### Oven

public Oven(Utensils utensils)
Create an Oven instance with given `Utensils`

Parameters:
`utensils` - All Utensils necessary to bake

- 

## Method Details

  - 

### getConfig

@Deprecated
public org.apache.commons.configuration2.CompositeConfiguration getConfig()
Deprecated.

  - 

### setConfig

@Deprecated
public void setConfig(org.apache.commons.configuration2.CompositeConfiguration config)
Deprecated.

  - 

### setupPaths

@Deprecated
public void setupPaths()
Deprecated.
There is no need for this method anymore. Validation is now part of the instantiation.
 Can be removed with 3.0.0.

Checks source path contains required sub-folders (i.e. templates) and setups up variables for them.

  - 

### bake

public void bake(File fileToBake)
Responsible for incremental baking, typically a single file at a time.

Parameters:
`fileToBake` - The file to bake

  - 

### bake

public void bake()
All the good stuff happens in here...

  - 

### getErrors

public List<Throwable> getErrors()

  - 

### getUtensils

public Utensils getUtensils()