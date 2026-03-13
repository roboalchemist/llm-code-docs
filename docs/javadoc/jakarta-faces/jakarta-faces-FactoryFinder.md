Package jakarta.faces

# Class FactoryFinder

java.lang.Object
jakarta.faces.FactoryFinder

---

public final class FactoryFinder
extends Object

 **FactoryFinder** implements the standard discovery algorithm for all factory objects
 specified in the Jakarta Faces APIs. For a given factory class name, a corresponding implementation class is
 searched for based on the following algorithm. Items are listed in order of decreasing search precedence:

-

 If the Jakarta Faces configuration file bundled into the `WEB-INF` directory of the webapp contains
 a `factory` entry of the given factory class name, that factory is used.

-

 If the Jakarta Faces configuration files named by the `jakarta.faces.CONFIG_FILES`
 `ServletContext` init parameter contain any `factory` entries of the given factory class name,
 those injectionProvider are used, with the last one taking precedence.

-

 If there are any Jakarta Faces configuration files bundled into the `META-INF` directory of any
 jars on the `ServletContext`'s resource paths, the `factory` entries of the given factory class
 name in those files are used, with the last one taking precedence.

-

 If a `META-INF/services/{factory-class-name}` resource is visible to the web application class loader for
 the calling application (typically as a injectionProvider of being present in the manifest of a JAR file), its first
 line is read and assumed to be the name of the factory implementation class to use.

-

 If none of the above steps yield a match, the Jakarta Faces implementation specific class is used.

 If any of the injectionProvider found on any of the steps above happen to have a one-argument constructor, with
 argument the type being the abstract factory class, that constructor is invoked, and the previous match is passed to
 the constructor. For example, say the container vendor provided an implementation of
 `FacesContextFactory`, and identified it in
 `META-INF/services/jakarta.faces.context.FacesContextFactory` in a jar on the webapp ClassLoader. Also say
 this implementation provided by the container vendor had a one argument constructor that took a
 `FacesContextFactory` instance. The `FactoryFinder` system would call that one-argument
 constructor, passing the implementation of `FacesContextFactory` provided by the Jakarta Faces
 implementation.

 If a Factory implementation does not provide a proper one-argument constructor, it must provide a zero-arguments
 constructor in order to be successfully instantiated.

 Once the name of the factory implementation class is located, the web application class loader for the calling
 application is requested to load this class, and a corresponding instance of the class will be created. A side effect
 of this rule is that each web application will receive its own instance of each factory class, whether the Jakarta
 Server Faces implementation is included within the web application or is made visible through the container's
 facilities for shared libraries.

-

## Field Summary

Fields

Modifier and Type
Field
Description
`static final String`
`APPLICATION_FACTORY`

 The property name for the `ApplicationFactory` class name.

`static final String`
`CLIENT_WINDOW_FACTORY`

 The property name for the `ClientWindowFactory` class name.

`static final String`
`EXCEPTION_HANDLER_FACTORY`

 The property name for the `ExceptionHandlerFactory` class name.

`static final String`
`EXTERNAL_CONTEXT_FACTORY`

 The property name for the `ExternalContextFactory` class name.

`static final String`
`FACELET_CACHE_FACTORY`

 The property name for the `FaceletCacheFactory` class name.

`static final String`
`FACES_CONTEXT_FACTORY`

 The property name for the `FacesContextFactory` class name.

`static final String`
`FACES_SERVLET_FACTORY`

 The property name for the `FacesServletFactory` class name.

`static final String`
`FLASH_FACTORY`

 The property name for the `FlashFactory` class name.

`static final String`
`FLOW_HANDLER_FACTORY`

 The property name for the `FlowHandlerFactory` class name.

`static final String`
`LIFECYCLE_FACTORY`

 The property name for the `LifecycleFactory` class name.

`static final String`
`PARTIAL_VIEW_CONTEXT_FACTORY`

 The property name for the `PartialViewContextFactory` class name.

`static final String`
`RENDER_KIT_FACTORY`

 The property name for the `RenderKitFactory` class name.

`static final String`
`SEARCH_EXPRESSION_CONTEXT_FACTORY`

 The property name for the `SearchExpressionContext` class name.

`static final String`
`TAG_HANDLER_DELEGATE_FACTORY`

 The property name for the `TagHandlerDelegate` class name.

`static final String`
`VIEW_DECLARATION_LANGUAGE_FACTORY`

 The property name for the `ViewDeclarationLanguage` class name.

`static final String`
`VISIT_CONTEXT_FACTORY`

 The property name for the `VisitContextFactory` class name.

-

## Method Summary

Modifier and Type
Method
Description
`static Object`
`getFactory(String factoryName)`

 Create (if necessary) and return a per-web-application instance of the
 appropriate implementation class for the specified Jakarta Faces factory class, based on the discovery
 algorithm described in the class description.

`static void`
`releaseFactories()`

 Release any references to factory instances associated with the class
 loader for the calling web application.

`static void`
`setFactory(String factoryName,
 String implName)`

 This method will store the argument `factoryName/implName` mapping in such a way that `getFactory(java.lang.String)`
 will find this mapping when searching for a match.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

-

## Field Details

-

### APPLICATION_FACTORY

public static final String APPLICATION_FACTORY

 The property name for the `ApplicationFactory` class name.

See Also:

    - Constant Field Values

  -

### CLIENT_WINDOW_FACTORY

public static final String CLIENT_WINDOW_FACTORY

 The property name for the `ClientWindowFactory` class name.

Since:
2.2
See Also:

    - Constant Field Values

  -

### EXCEPTION_HANDLER_FACTORY

public static final String EXCEPTION_HANDLER_FACTORY

 The property name for the `ExceptionHandlerFactory` class name.

See Also:

    - Constant Field Values

  -

### EXTERNAL_CONTEXT_FACTORY

public static final String EXTERNAL_CONTEXT_FACTORY

 The property name for the `ExternalContextFactory` class name.

See Also:

    - Constant Field Values

  -

### FACES_CONTEXT_FACTORY

public static final String FACES_CONTEXT_FACTORY

 The property name for the `FacesContextFactory` class name.

See Also:

    - Constant Field Values

  -

### FACES_SERVLET_FACTORY

public static final String FACES_SERVLET_FACTORY

 The property name for the `FacesServletFactory` class name.

See Also:

    - Constant Field Values

  -

### FACELET_CACHE_FACTORY

public static final String FACELET_CACHE_FACTORY

 The property name for the `FaceletCacheFactory` class name.

Since:
2.1
See Also:

    - Constant Field Values

  -

### FLASH_FACTORY

public static final String FLASH_FACTORY

 The property name for the `FlashFactory` class name.

Since:
2.2
See Also:

    - Constant Field Values

  -

### FLOW_HANDLER_FACTORY

public static final String FLOW_HANDLER_FACTORY

 The property name for the `FlowHandlerFactory` class name.

Since:
2.2
See Also:

    - Constant Field Values

  -

### PARTIAL_VIEW_CONTEXT_FACTORY

public static final String PARTIAL_VIEW_CONTEXT_FACTORY

 The property name for the `PartialViewContextFactory` class name.

See Also:

    - Constant Field Values

  -

### VISIT_CONTEXT_FACTORY

public static final String VISIT_CONTEXT_FACTORY

 The property name for the `VisitContextFactory` class name.

See Also:

    - Constant Field Values

  -

### LIFECYCLE_FACTORY

public static final String LIFECYCLE_FACTORY

 The property name for the `LifecycleFactory` class name.

See Also:

    - Constant Field Values

  -

### RENDER_KIT_FACTORY

public static final String RENDER_KIT_FACTORY

 The property name for the `RenderKitFactory` class name.

See Also:

    - Constant Field Values

  -

### VIEW_DECLARATION_LANGUAGE_FACTORY

public static final String VIEW_DECLARATION_LANGUAGE_FACTORY

 The property name for the `ViewDeclarationLanguage` class name.

See Also:

    - Constant Field Values

  -

### TAG_HANDLER_DELEGATE_FACTORY

public static final String TAG_HANDLER_DELEGATE_FACTORY

 The property name for the `TagHandlerDelegate` class name.

See Also:

    - Constant Field Values

  -

### SEARCH_EXPRESSION_CONTEXT_FACTORY

public static final String SEARCH_EXPRESSION_CONTEXT_FACTORY

 The property name for the `SearchExpressionContext` class name.

See Also:

    - Constant Field Values

-

## Method Details

-

### getFactory

public static Object getFactory(String factoryName)
                         throws FacesException

 Create (if necessary) and return a per-web-application instance of the
 appropriate implementation class for the specified Jakarta Faces factory class, based on the discovery
 algorithm described in the class description.

 The standard injectionProvider and wrappers in Jakarta Faces all implement the interface `FacesWrapper`.
 If the returned `Object` is an implementation of one of the standard injectionProvider, it must be legal
 to cast it to an instance of `FacesWrapper` and call `FacesWrapper.getWrapped()` on the instance.

Parameters:
`factoryName` - Fully qualified name of the Jakarta Faces factory for which an implementation instance is
 requested
Returns:
the found factory instance
Throws:
`FacesException` - if the web application class loader cannot be identified
`FacesException` - if an instance of the configured factory implementation class cannot be loaded
`FacesException` - if an instance of the configured factory implementation class cannot be instantiated
`IllegalArgumentException` - if `factoryName` does not identify a standard Jakarta Faces
 factory name
`IllegalStateException` - if there is no configured factory implementation class for the specified factory name
`NullPointerException` - if `factoryname` is null

-

### setFactory

public static void setFactory(String factoryName,
 String implName)

 This method will store the argument `factoryName/implName` mapping in such a way that `getFactory(java.lang.String)`
 will find this mapping when searching for a match.

 This method has no effect if `getFactory()` has already been called looking for a factory for this
 `factoryName`.

 This method can be used by implementations to store a factory mapping while parsing the Faces configuration file

Parameters:
`factoryName` - the name to be used in a subsequent call to `getFactory(java.lang.String)`.
`implName` - the fully qualified class name of the factory corresponding to `factoryName`.
Throws:
`IllegalArgumentException` - if `factoryName` does not identify a standard Jakarta Faces
 factory name
`NullPointerException` - if `factoryname` is null

-

### releaseFactories

public static void releaseFactories()
                             throws FacesException

 Release any references to factory instances associated with the class
 loader for the calling web application. This method must be called during of web
 application shutdown.

Throws:
`FacesException` - if the web application class loader cannot be identified
