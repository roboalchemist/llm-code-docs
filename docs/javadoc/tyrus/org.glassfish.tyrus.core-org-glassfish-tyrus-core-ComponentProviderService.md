Module org.glassfish.tyrus.core
Package org.glassfish.tyrus.core

# Class ComponentProviderService

java.lang.Object
org.glassfish.tyrus.core.ComponentProviderService

---

public class ComponentProviderService
extends Object
Provides an instance of component. Searches for registered `ComponentProvider`s which are used to provide
 instances.

Author:
Martin Matula, Stepan Kopriva, Pavel Bucek

-

## Constructor Summary

Constructors

Constructor
Description
`ComponentProviderService(ComponentProviderService componentProviderService)`

Copy constructor.

-

## Method Summary

Modifier and Type
Method
Description
`static ComponentProviderService`
`create()`

Create new instance of `ComponentProviderService`.

`static ComponentProviderService`
`createClient()`

Create new instance of `ComponentProviderService`.

`<T> Object`
`getCoderInstance(Class<T> c,
 jakarta.websocket.Session session,
 jakarta.websocket.EndpointConfig endpointConfig,
 ErrorCollector collector)`

Provide an instance of `Encoder` or `Decoder` descendant which is
 coupled to `Session`.

`<T> Object`
`getEndpointInstance(Class<T> endpointClass)`

This method is called by the container each time a new client
 connects to the logical endpoint this configurator configures.

`<T> Object`
`getInstance(Class<T> c,
 jakarta.websocket.Session session,
 ErrorCollector collector)`

Provide an instance of class which is coupled to `Session`.

`Method`
`getInvocableMethod(Method method)`

`void`
`removeSession(jakarta.websocket.Session session)`

Remove `Session` from cache.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

-

## Constructor Details

-

### ComponentProviderService

public ComponentProviderService(ComponentProviderService componentProviderService)
Copy constructor.

Parameters:
`componentProviderService` - original instance.

-

## Method Details

-

### create

public static ComponentProviderService create()
Create new instance of `ComponentProviderService`.

 Searches for registered `ComponentProvider`s and registers them with this service.

 `DefaultComponentProvider` is always added to found providers.

Returns:
initialized `ComponentProviderService`.

-

### createClient

public static ComponentProviderService createClient()
Create new instance of `ComponentProviderService`.

 Contains *only* `DefaultComponentProvider`. Used for creating client instances (CDI/EJB container are
 often confused and using them to retrieve instances leads to unstable results since the injection scope is not
 properly defined for these cases). See https://java.net/jira/browse/WEBSOCKET_SPEC-197 and
 https://java.net/jira/browse/WEBSOCKET_SPEC-196.

Returns:
initialized `ComponentProviderService`.

-

### getInstance

public <T> Object getInstance(Class<T> c,
 jakarta.websocket.Session session,
 ErrorCollector collector)
Provide an instance of class which is coupled to `Session`.

 The first time the method is called the provider creates an instance and caches it.
 Next time the method is called the cached instance is returned.

Type Parameters:
`T` - type of the provided instance.
Parameters:
`c` - `Class` whose instance will be provided.
`session` - session to which the instance belongs (think of this as a scope).
`collector` - error collector.
Returns:
instance

-

### getCoderInstance

public <T> Object getCoderInstance(Class<T> c,
 jakarta.websocket.Session session,
 jakarta.websocket.EndpointConfig endpointConfig,
 ErrorCollector collector)
Provide an instance of `Encoder` or `Decoder` descendant which is
 coupled to `Session`.

 The first time the method is called the provider creates an instance, calls `Encoder.init(jakarta.websocket.EndpointConfig)`
 or `Decoder.init(jakarta.websocket.EndpointConfig)` and caches it.
 Next time the method is called the cached instance is returned.

Type Parameters:
`T` - type of the provided instance.
Parameters:
`c` - `Class` whose instance will be provided.
`session` - session to which the instance belongs (think of this as a scope).
`endpointConfig` - configuration corresponding to current context. Used for
                       `Encoder.init(jakarta.websocket.EndpointConfig)` and
                       `Decoder.init(jakarta.websocket.EndpointConfig)`
`collector` - error collector.
Returns:
instance

-

### getInvocableMethod

public Method getInvocableMethod(Method method)

-

### removeSession

public void removeSession(jakarta.websocket.Session session)
Remove `Session` from cache.

Parameters:
`session` - to be removed.

-

### getEndpointInstance

public <T> Object getEndpointInstance(Class<T> endpointClass)
                               throws InstantiationException
This method is called by the container each time a new client
 connects to the logical endpoint this configurator configures.
 Developers may override this method to control instantiation of
 endpoint instances in order to customize the initialization
 of the endpoint instance, or manage them in some other way.
 If the developer overrides this method, services like
 dependency injection that are otherwise supported, for example, when
 the implementation is part of the Java EE platform
 may not be available.
 The platform default implementation of this method returns a new
 endpoint instance per call, thereby ensuring that there is one
 endpoint instance per client, the default deployment cardinality.

Type Parameters:
`T` - the type of the endpoint.
Parameters:
`endpointClass` - the class of the endpoint.
Returns:
an instance of the endpoint that will handle all
 interactions from a new client.
Throws:
`InstantiationException` - if there was an error producing the
                                endpoint instance.
See Also:

    - `ServerEndpointConfig.Configurator.getEndpointInstance(Class)`
