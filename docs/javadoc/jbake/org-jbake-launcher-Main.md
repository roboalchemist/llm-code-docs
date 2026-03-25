Package org.jbake.launcher

# Class Main

java.lang.Object
org.jbake.launcher.Main

---

public class Main
extends Object
Launcher for JBake.

- 

## Constructor Summary

Constructors

Modifier
Constructor
Description
` `
`Main()`

Default constructor.

`protected `
`Main(Baker baker,
 JettyServer jetty,
 BakeWatcher watcher)`

Optional constructor to externalize dependencies.

- 

## Method Summary

Modifier and Type
Method
Description
`JBakeConfigurationFactory`
`getJBakeConfigurationFactory()`
 
`static void`
`main(String[] args)`

Runs the app with the given arguments.

`static void`
`printUsage()`
 
`void`
`run(String[] args)`
 
`protected void`
`run(LaunchOptions res,
 JBakeConfiguration config)`
 
`void`
`setJBakeConfigurationFactory(JBakeConfigurationFactory factory)`
 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Constructor Details

  - 

### Main

public Main()
Default constructor.

  - 

### Main

protected Main(Baker baker,
 JettyServer jetty,
 BakeWatcher watcher)
Optional constructor to externalize dependencies.

Parameters:
`baker` - A `Baker` instance
`jetty` - A `JettyServer` instance
`watcher` - A `BakeWatcher` instance

- 

## Method Details

  - 

### main

public static void main(String[] args)
Runs the app with the given arguments.

Parameters:
`args` - Application arguments

  - 

### run

public void run(String[] args)
         throws JBakeException

Throws:
`JBakeException`

  - 

### run

protected void run(LaunchOptions res,
 JBakeConfiguration config)

  - 

### printUsage

public static void printUsage()

  - 

### getJBakeConfigurationFactory

public JBakeConfigurationFactory getJBakeConfigurationFactory()

  - 

### setJBakeConfigurationFactory

public void setJBakeConfigurationFactory(JBakeConfigurationFactory factory)