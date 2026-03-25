Package org.jbake.launcher

# Class CustomFSChangeListener

java.lang.Object
org.jbake.launcher.CustomFSChangeListener

All Implemented Interfaces:
`org.apache.commons.vfs2.FileListener`

---

public class CustomFSChangeListener
extends Object
implements org.apache.commons.vfs2.FileListener

- 

## Constructor Summary

Constructors

Constructor
Description
`CustomFSChangeListener(JBakeConfiguration config)`
 

- 

## Method Summary

Modifier and Type
Method
Description
`void`
`fileChanged(org.apache.commons.vfs2.FileChangeEvent event)`
 
`void`
`fileCreated(org.apache.commons.vfs2.FileChangeEvent event)`
 
`void`
`fileDeleted(org.apache.commons.vfs2.FileChangeEvent event)`
 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Constructor Details

  - 

### CustomFSChangeListener

public CustomFSChangeListener(JBakeConfiguration config)

- 

## Method Details

  - 

### fileCreated

public void fileCreated(org.apache.commons.vfs2.FileChangeEvent event)
                 throws Exception

Specified by:
`fileCreated` in interface `org.apache.commons.vfs2.FileListener`
Throws:
`Exception`

  - 

### fileDeleted

public void fileDeleted(org.apache.commons.vfs2.FileChangeEvent event)
                 throws Exception

Specified by:
`fileDeleted` in interface `org.apache.commons.vfs2.FileListener`
Throws:
`Exception`

  - 

### fileChanged

public void fileChanged(org.apache.commons.vfs2.FileChangeEvent event)
                 throws Exception

Specified by:
`fileChanged` in interface `org.apache.commons.vfs2.FileListener`
Throws:
`Exception`