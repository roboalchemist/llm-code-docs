Package org.jbake.launcher

# Class Init

java.lang.Object
org.jbake.launcher.Init

---

public class Init
extends Object
Initialises sample folder structure with pre-defined template

- 

## Constructor Summary

Constructors

Constructor
Description
`Init(org.apache.commons.configuration2.CompositeConfiguration config)`

Deprecated.
use `Init(JBakeConfiguration)` instead

`Init(JBakeConfiguration config)`
 

- 

## Method Summary

Modifier and Type
Method
Description
`void`
`run(File outputFolder,
 File templateLocationFolder,
 String templateType)`

Performs checks on output folder before extracting template file

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Constructor Details

  - 

### Init

@Deprecated
public Init(org.apache.commons.configuration2.CompositeConfiguration config)
Deprecated.
use `Init(JBakeConfiguration)` instead

Parameters:
`config` - The project configuration

  - 

### Init

public Init(JBakeConfiguration config)

- 

## Method Details

  - 

### run

public void run(File outputFolder,
 File templateLocationFolder,
 String templateType)
         throws Exception
Performs checks on output folder before extracting template file

Parameters:
`outputFolder` - Target directory for extracting template file
`templateLocationFolder` - Source location for template file
`templateType` - Type of the template to be used
Throws:
`Exception` - if required folder structure can't be achieved without content overwriting