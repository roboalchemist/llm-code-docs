Package org.jbake.launcher

# Class BakeWatcher

java.lang.Object
org.jbake.launcher.BakeWatcher

---

public class BakeWatcher
extends Object
Delegate responsible for watching the file system for changes.

- 

## Constructor Summary

Constructors

Constructor
Description
`BakeWatcher()`
 

- 

## Method Summary

Modifier and Type
Method
Description
`void`
`start(JBakeConfiguration config)`

Starts watching the file system for changes to trigger a bake.

`void`
`start(LaunchOptions res,
 org.apache.commons.configuration2.CompositeConfiguration config)`

Deprecated.
use `start(JBakeConfiguration)` instead

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Constructor Details

  - 

### BakeWatcher

public BakeWatcher()

- 

## Method Details

  - 

### start

@Deprecated
public void start(LaunchOptions res,
 org.apache.commons.configuration2.CompositeConfiguration config)
Deprecated.
use `start(JBakeConfiguration)` instead

Starts watching the file system for changes to trigger a bake.

Parameters:
`res` - Commandline options
`config` - Configuration settings

  - 

### start

public void start(JBakeConfiguration config)
Starts watching the file system for changes to trigger a bake.

Parameters:
`config` - JBakeConfiguration settings