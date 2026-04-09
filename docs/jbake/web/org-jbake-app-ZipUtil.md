Package org.jbake.app

# Class ZipUtil

java.lang.Object
org.jbake.app.ZipUtil

---

public class ZipUtil
extends Object
Provides Zip file related functions

- 

## Constructor Summary

Constructors

Constructor
Description
`ZipUtil()`
 

- 

## Method Summary

Modifier and Type
Method
Description
`static void`
`extract(InputStream is,
 File outputFolder)`

Extracts content of Zip file to specified output path.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Constructor Details

  - 

### ZipUtil

public ZipUtil()

- 

## Method Details

  - 

### extract

public static void extract(InputStream is,
 File outputFolder)
                    throws IOException
Extracts content of Zip file to specified output path.

Parameters:
`is` - `InputStream` InputStream of Zip file
`outputFolder` - folder where Zip file should be extracted to
Throws:
`IOException` - if IOException occurs