Package org.jbake.app.configuration

# Class JBakeConfigurationFactory

java.lang.Object
org.jbake.app.configuration.JBakeConfigurationFactory

---

public class JBakeConfigurationFactory
extends Object
A `JBakeConfiguration` factory

- 

## Constructor Summary

Constructors

Constructor
Description
`JBakeConfigurationFactory()`
 

- 

## Method Summary

Modifier and Type
Method
Description
`DefaultJBakeConfiguration`
`createDefaultJbakeConfiguration(File sourceFolder,
 File destination,
 boolean isClearCache)`

Creates a `DefaultJBakeConfiguration` using default.properties and jbake.properties

`DefaultJBakeConfiguration`
`createDefaultJbakeConfiguration(File sourceFolder,
 File destination,
 File propertiesFile,
 boolean isClearCache)`

Creates a `DefaultJBakeConfiguration`

`DefaultJBakeConfiguration`
`createDefaultJbakeConfiguration(File sourceFolder,
 File destination,
 org.apache.commons.configuration2.CompositeConfiguration compositeConfiguration)`

Deprecated.
use `createDefaultJbakeConfiguration(File, File, File, boolean)` instead

`DefaultJBakeConfiguration`
`createDefaultJbakeConfiguration(File sourceFolder,
 File destination,
 org.apache.commons.configuration2.CompositeConfiguration compositeConfiguration,
 boolean isClearCache)`

Deprecated.
use `createDefaultJbakeConfiguration(File, File, File, boolean)` instead

`DefaultJBakeConfiguration`
`createDefaultJbakeConfiguration(File sourceFolder,
 org.apache.commons.configuration2.CompositeConfiguration config)`

Deprecated.

`DefaultJBakeConfiguration`
`createJettyJbakeConfiguration(File sourceFolder,
 File destinationFolder,
 boolean isClearCache)`

Deprecated.
use `createJettyJbakeConfiguration(File, File, File, boolean)` instead

`DefaultJBakeConfiguration`
`createJettyJbakeConfiguration(File sourceFolder,
 File destinationFolder,
 File propertiesFile,
 boolean isClearCache)`

Creates a `DefaultJBakeConfiguration` with value site.host replaced
 by http://localhost:[server.port].

`ConfigUtil`
`getConfigUtil()`
 
`void`
`setConfigUtil(ConfigUtil configUtil)`
 
`JBakeConfigurationFactory`
`setEncoding(String charset)`
 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Constructor Details

  - 

### JBakeConfigurationFactory

public JBakeConfigurationFactory()

- 

## Method Details

  - 

### createDefaultJbakeConfiguration

public DefaultJBakeConfiguration createDefaultJbakeConfiguration(File sourceFolder,
 File destination,
 boolean isClearCache)
                                                          throws JBakeException
Creates a `DefaultJBakeConfiguration` using default.properties and jbake.properties

Parameters:
`sourceFolder` - The source folder of the project
`destination` - The destination folder to render and copy files to
`isClearCache` - Whether to clear database cache or not
Returns:
A configuration by given parameters
Throws:
`JBakeException` - if loading the configuration fails

  - 

### createDefaultJbakeConfiguration

public DefaultJBakeConfiguration createDefaultJbakeConfiguration(File sourceFolder,
 File destination,
 File propertiesFile,
 boolean isClearCache)
                                                          throws JBakeException
Creates a `DefaultJBakeConfiguration`

Parameters:
`sourceFolder` - The source folder of the project
`destination` - The destination folder to render and copy files to
`propertiesFile` - The properties file for the project
`isClearCache` - Whether to clear database cache or not
Returns:
A configuration by given parameters
Throws:
`JBakeException` - if loading the configuration fails

  - 

### createDefaultJbakeConfiguration

@Deprecated
public DefaultJBakeConfiguration createDefaultJbakeConfiguration(File sourceFolder,
 File destination,
 org.apache.commons.configuration2.CompositeConfiguration compositeConfiguration,
 boolean isClearCache)
                                                          throws JBakeException
Deprecated.
use `createDefaultJbakeConfiguration(File, File, File, boolean)` instead

Creates a `DefaultJBakeConfiguration`

 This is a compatibility factory method

Parameters:
`sourceFolder` - The source folder of the project
`destination` - The destination folder to render and copy files to
`compositeConfiguration` - A given `CompositeConfiguration`
`isClearCache` - Whether to clear database cache or not
Returns:
A configuration by given parameters
Throws:
`JBakeException`

  - 

### createDefaultJbakeConfiguration

@Deprecated
public DefaultJBakeConfiguration createDefaultJbakeConfiguration(File sourceFolder,
 File destination,
 org.apache.commons.configuration2.CompositeConfiguration compositeConfiguration)
                                                          throws JBakeException
Deprecated.
use `createDefaultJbakeConfiguration(File, File, File, boolean)` instead

Creates a `DefaultJBakeConfiguration`

 This is a compatibility factory method

Parameters:
`sourceFolder` - The source folder of the project
`destination` - The destination folder to render and copy files to
`compositeConfiguration` - A given `CompositeConfiguration`
Returns:
A configuration by given parameters
Throws:
`JBakeException`

  - 

### createDefaultJbakeConfiguration

@Deprecated
public DefaultJBakeConfiguration createDefaultJbakeConfiguration(File sourceFolder,
 org.apache.commons.configuration2.CompositeConfiguration config)
                                                          throws JBakeException
Deprecated.
Creates a `DefaultJBakeConfiguration`

Parameters:
`sourceFolder` - The source folder of the project
`config` - A `CompositeConfiguration`
Returns:
A configuration by given parameters
Throws:
`JBakeException`

  - 

### createJettyJbakeConfiguration

@Deprecated
public DefaultJBakeConfiguration createJettyJbakeConfiguration(File sourceFolder,
 File destinationFolder,
 boolean isClearCache)
                                                        throws JBakeException
Deprecated.
use `createJettyJbakeConfiguration(File, File, File, boolean)` instead

Creates a `DefaultJBakeConfiguration` with value site.host replaced
 by http://localhost:[server.port].
 The server.port is read from the project properties file.

Parameters:
`sourceFolder` - The source folder of the project
`destinationFolder` - The destination folder to render and copy files to
`isClearCache` - Whether to clear database cache or not
Returns:
A configuration by given parameters
Throws:
`JBakeException` - if loading the configuration fails

  - 

### createJettyJbakeConfiguration

public DefaultJBakeConfiguration createJettyJbakeConfiguration(File sourceFolder,
 File destinationFolder,
 File propertiesFile,
 boolean isClearCache)
                                                        throws JBakeException
Creates a `DefaultJBakeConfiguration` with value site.host replaced
 by http://localhost:[server.port].
 The server.port is read from the project properties file.

Parameters:
`sourceFolder` - The source folder of the project
`destinationFolder` - The destination folder to render and copy files to
`propertiesFile` - The properties file for the project
`isClearCache` - Whether to clear database cache or not
Returns:
A configuration by given parameters
Throws:
`JBakeException` - if loading the configuration fails

  - 

### getConfigUtil

public ConfigUtil getConfigUtil()

  - 

### setConfigUtil

public void setConfigUtil(ConfigUtil configUtil)

  - 

### setEncoding

public JBakeConfigurationFactory setEncoding(String charset)