Package org.jbake.app.configuration

# Class ConfigUtil

java.lang.Object
org.jbake.app.configuration.ConfigUtil

---

public class ConfigUtil
extends Object
Provides Configuration related functions.

- 

## Field Summary

Fields

Modifier and Type
Field
Description
`static final String`
`CONFIG_FILE`
 
`static final String`
`DEFAULT_CONFIG_FILE`
 
`static final String`
`DEFAULT_ENCODING`
 
`static final String`
`LEGACY_CONFIG_FILE`
 
`static final char`
`LIST_DELIMITER`
 

- 

## Constructor Summary

Constructors

Constructor
Description
`ConfigUtil()`
 

- 

## Method Summary

Modifier and Type
Method
Description
`String`
`getEncoding()`
 
`JBakeConfiguration`
`loadConfig(File source)`

Deprecated.
use `loadConfig(File, File)` instead

`JBakeConfiguration`
`loadConfig(File source,
 File propertiesFile)`

Load a configuration.

`ConfigUtil`
`setEncoding(String encoding)`
 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Field Details

  - 

### LIST_DELIMITER

public static final char LIST_DELIMITER

See Also:

    - Constant Field Values

  - 

### DEFAULT_ENCODING

public static final String DEFAULT_ENCODING

See Also:

    - Constant Field Values

  - 

### LEGACY_CONFIG_FILE

public static final String LEGACY_CONFIG_FILE

See Also:

    - Constant Field Values

  - 

### CONFIG_FILE

public static final String CONFIG_FILE

See Also:

    - Constant Field Values

  - 

### DEFAULT_CONFIG_FILE

public static final String DEFAULT_CONFIG_FILE

See Also:

    - Constant Field Values

- 

## Constructor Details

  - 

### ConfigUtil

public ConfigUtil()

- 

## Method Details

  - 

### loadConfig

public JBakeConfiguration loadConfig(File source,
 File propertiesFile)
                              throws JBakeException
Load a configuration.

Parameters:
`source` - the source directory of the project
`propertiesFile` - the properties file for the project
Returns:
the configuration
Throws:
`JBakeException` - if unable to configure

  - 

### loadConfig

@Deprecated
public JBakeConfiguration loadConfig(File source)
                              throws org.apache.commons.configuration2.ex.ConfigurationException
Deprecated.
use `loadConfig(File, File)` instead

Load a configuration.

Parameters:
`source` - the source directory of the project
Returns:
the configuration
Throws:
`org.apache.commons.configuration2.ex.ConfigurationException` - if unable to configure

  - 

### getEncoding

public String getEncoding()

  - 

### setEncoding

public ConfigUtil setEncoding(String encoding)