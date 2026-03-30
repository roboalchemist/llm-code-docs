Package org.jbake.app

# Class Asset

java.lang.Object
org.jbake.app.Asset

---

public class Asset
extends Object
Deals with assets (static files such as css, js or image files).

- 

## Constructor Summary

Constructors

Constructor
Description
`Asset(File source,
 File destination,
 org.apache.commons.configuration2.CompositeConfiguration config)`

Deprecated.
Use `Asset(JBakeConfiguration)` instead.

`Asset(JBakeConfiguration config)`

Creates an instance of Asset.

- 

## Method Summary

Modifier and Type
Method
Description
`void`
`copy()`

Copy all files from assets folder to destination folder
 read from configuration

`void`
`copy(File path)`

Copy all files from supplied path.

`void`
`copyAssetsFromContent(File path)`

Responsible for copying any asset files that exist within the content directory.

`void`
`copySingleFile(File asset)`

Copy one asset file at a time.

`List<Throwable>`
`getErrors()`

Accessor method to the collection of errors generated during the bake

`boolean`
`isAssetFile(File path)`

Determine if a given file is an asset file.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Constructor Details

  - 

### Asset

@Deprecated
public Asset(File source,
 File destination,
 org.apache.commons.configuration2.CompositeConfiguration config)
Deprecated.
Use `Asset(JBakeConfiguration)` instead.
 Compatibility constructor.
 Creates an instance of Asset.

Parameters:
`source` - Source file for the asset
`destination` - Destination (target) directory for asset file
`config` - Project configuration

  - 

### Asset

public Asset(JBakeConfiguration config)
Creates an instance of Asset.

Parameters:
`config` - The project configuration. @see{`JBakeConfiguration`}

- 

## Method Details

  - 

### copy

public void copy()
Copy all files from assets folder to destination folder
 read from configuration

  - 

### copy

public void copy(File path)
Copy all files from supplied path.

Parameters:
`path` - The starting path

  - 

### copySingleFile

public void copySingleFile(File asset)
Copy one asset file at a time.

Parameters:
`asset` - The asset file to copy

  - 

### isAssetFile

public boolean isAssetFile(File path)
Determine if a given file is an asset file.

Parameters:
`path` - to the file to validate.
Returns:
true if the path provided points to a file in the asset folder.

  - 

### copyAssetsFromContent

public void copyAssetsFromContent(File path)
Responsible for copying any asset files that exist within the content directory.

Parameters:
`path` - of the content directory

  - 

### getErrors

public List<Throwable> getErrors()
Accessor method to the collection of errors generated during the bake

Returns:
a list of errors.