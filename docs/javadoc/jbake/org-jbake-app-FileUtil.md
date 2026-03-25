Package org.jbake.app

# Class FileUtil

java.lang.Object
org.jbake.app.FileUtil

---

public class FileUtil
extends Object
Provides File related functions

- 

## Field Summary

Fields

Modifier and Type
Field
Description
`static final String`
`URI_SEPARATOR_CHAR`
 

- 

## Constructor Summary

Constructors

Constructor
Description
`FileUtil()`
 

- 

## Method Summary

Modifier and Type
Method
Description
`static String`
`asPath(File file)`

platform independent file.getPath()

`static String`
`asPath(String path)`

platform independent file.getPath()

`static boolean`
`directoryOnlyIfNotIgnored(File file)`

Deprecated.
use `directoryOnlyIfNotIgnored(File, JBakeConfiguration)` instead

`static boolean`
`directoryOnlyIfNotIgnored(File file,
 JBakeConfiguration config)`

Ignores directory (and children) if it contains a file named in the
 configuration as a marker to ignore the directory.

`static String`
`fileExt(File src)`
 
`static String`
`fileExt(String name)`
 
`static FileFilter`
`getDataFileFilter()`

Filters files based on their file extension - only find data files (i.e.

`static FileFilter`
`getFileFilter()`

Deprecated.
use `getFileFilter(JBakeConfiguration)` instead

`static FileFilter`
`getFileFilter(JBakeConfiguration config)`

Filters files based on their file extension.

`static FileFilter`
`getNotContentFileFilter()`

Deprecated.
use `getNotContentFileFilter(JBakeConfiguration)` instead

`static FileFilter`
`getNotContentFileFilter(JBakeConfiguration config)`

Gets the list of files that are not content files based on their extension.

`static String`
`getPathToRoot(JBakeConfiguration config,
 File rootPath,
 File sourceFile)`

Given a file inside content it return
 the relative path to get to the root.

`static File`
`getRunningLocation()`

Works out the folder where JBake is running from.

`static String`
`getUriPathToContentRoot(JBakeConfiguration config,
 File sourceFile)`
 
`static String`
`getUriPathToDestinationRoot(JBakeConfiguration config,
 File sourceFile)`
 
`static boolean`
`isExistingFolder(File f)`
 
`static boolean`
`isFileInDirectory(File file,
 File directory)`

Utility method to determine if a given file is located somewhere in the directory provided.

`static String`
`sha1(File sourceFile)`

Computes the hash of a file or directory.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Field Details

  - 

### URI_SEPARATOR_CHAR

public static final String URI_SEPARATOR_CHAR

See Also:

    - Constant Field Values

- 

## Constructor Details

  - 

### FileUtil

public FileUtil()

- 

## Method Details

  - 

### getFileFilter

public static FileFilter getFileFilter(JBakeConfiguration config)
Filters files based on their file extension.

Parameters:
`config` - the jbake configuration
Returns:
Object for filtering files

  - 

### getFileFilter

@Deprecated
public static FileFilter getFileFilter()
Deprecated.
use `getFileFilter(JBakeConfiguration)` instead

Filters files based on their file extension.

Returns:
Object for filtering files

  - 

### getDataFileFilter

public static FileFilter getDataFileFilter()
Filters files based on their file extension - only find data files (i.e. files with .yaml or .yml extension)

Returns:
Object for filtering files

  - 

### getNotContentFileFilter

public static FileFilter getNotContentFileFilter(JBakeConfiguration config)
Gets the list of files that are not content files based on their extension.

Parameters:
`config` - the jbake configuration
Returns:
FileFilter object

  - 

### getNotContentFileFilter

@Deprecated
public static FileFilter getNotContentFileFilter()
Deprecated.
use `getNotContentFileFilter(JBakeConfiguration)` instead

Gets the list of files that are not content files based on their extension.

Returns:
FileFilter object

  - 

### directoryOnlyIfNotIgnored

public static boolean directoryOnlyIfNotIgnored(File file,
 JBakeConfiguration config)
Ignores directory (and children) if it contains a file named in the
 configuration as a marker to ignore the directory.

Parameters:
`file` - the file to test
`config` - the jbake configuration
Returns:
true if file is directory and not ignored

  - 

### directoryOnlyIfNotIgnored

@Deprecated
public static boolean directoryOnlyIfNotIgnored(File file)
Deprecated.
use `directoryOnlyIfNotIgnored(File, JBakeConfiguration)` instead

Ignores directory (and children) if it contains a file named ".jbakeignore".

Parameters:
`file` - the file to test
Returns:
true if file is directory and not ignored

  - 

### isExistingFolder

public static boolean isExistingFolder(File f)

  - 

### getRunningLocation

public static File getRunningLocation()
                               throws Exception
Works out the folder where JBake is running from.

Returns:
File referencing folder JBake is running from
Throws:
`Exception` - when application is not able to work out where is JBake running from

  - 

### fileExt

public static String fileExt(File src)

  - 

### fileExt

public static String fileExt(String name)

  - 

### sha1

public static String sha1(File sourceFile)
                   throws Exception
Computes the hash of a file or directory.

Parameters:
`sourceFile` - the original file or directory
Returns:
an hex string representing the SHA1 hash of the file or directory.
Throws:
`Exception` - if any IOException of SecurityException occured

  - 

### asPath

public static String asPath(File file)
platform independent file.getPath()

Parameters:
`file` - the file to transform, or `null`
Returns:
The result of file.getPath() with all path Separators beeing a "/", or `null`
 Needed to transform Windows path separators into slashes.

  - 

### asPath

public static String asPath(String path)
platform independent file.getPath()

Parameters:
`path` - the path to transform, or `null`
Returns:
The result will have all platform path separators replaced by "/".

  - 

### getPathToRoot

public static String getPathToRoot(JBakeConfiguration config,
 File rootPath,
 File sourceFile)
Given a file inside content it return
 the relative path to get to the root.
 

 Example: /content and /content/tags/blog will return '../..'

Parameters:
`sourceFile` - the file to calculate relative path for
`rootPath` - the root path
`config` - the jbake configuration
Returns:
the relative path to get to the root

  - 

### getUriPathToDestinationRoot

public static String getUriPathToDestinationRoot(JBakeConfiguration config,
 File sourceFile)

  - 

### getUriPathToContentRoot

public static String getUriPathToContentRoot(JBakeConfiguration config,
 File sourceFile)

  - 

### isFileInDirectory

public static boolean isFileInDirectory(File file,
 File directory)
                                 throws IOException
Utility method to determine if a given file is located somewhere in the directory provided.

Parameters:
`file` - used to check if it is located in the provided directory.
`directory` - to validate whether or not the provided file resides.
Returns:
true if the file is somewhere in the provided directory, false if it is not.
Throws:
`IOException` - if the canonical path for either of the input directories can't be determined.