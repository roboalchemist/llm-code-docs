Package org.jbake.launcher

# Class Baker

java.lang.Object
org.jbake.launcher.Baker

---

public class Baker
extends Object
Delegate class responsible for launching a Bake.

- 

## Constructor Summary

Constructors

Constructor
Description
`Baker()`
 

- 

## Method Summary

Modifier and Type
Method
Description
`void`
`bake(JBakeConfiguration config)`
 
`void`
`bake(LaunchOptions options,
 org.apache.commons.configuration2.CompositeConfiguration config)`

Deprecated.
use `bake(JBakeConfiguration)` instead

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Constructor Details

  - 

### Baker

public Baker()

- 

## Method Details

  - 

### bake

@Deprecated
public void bake(LaunchOptions options,
 org.apache.commons.configuration2.CompositeConfiguration config)
Deprecated.
use `bake(JBakeConfiguration)` instead

Parameters:
`options` - The given cli options
`config` - The project configuration

  - 

### bake

public void bake(JBakeConfiguration config)