Module org.glassfish.tyrus.core
Package org.glassfish.tyrus.core

# Class TyrusServerEndpointConfig.Builder

java.lang.Object
org.glassfish.tyrus.core.TyrusServerEndpointConfig.Builder

Enclosing interface:
`TyrusServerEndpointConfig`

---

public static final class TyrusServerEndpointConfig.Builder
extends Object
The TyrusServerEndpointConfig.Builder is a class used for creating
 `TyrusServerEndpointConfig.Builder` objects for the purposes of
 deploying a server endpoint.

 Here are some examples:

 Building a plain configuration for an endpoint with just a path.

 `ServerEndpointConfig config = TyrusServerEndpointConfig.Builder.create(ProgrammaticEndpoint.class,
 "/foo").build();`

 Building a configuration with no subprotocols, limited number of sessions (100) and a custom configurator.

```

 ServerEndpointConfig config = TyrusServerEndpointConfig.Builder.create(ProgrammaticEndpoint.class, "/bar")
         .subprotocols(subprotocols)
         .maxSessions(100)
         .configurator(new MyServerConfigurator())
         .build();
 
```

Author:
dannycoward

-

## Method Summary

Modifier and Type
Method
Description
`TyrusServerEndpointConfig`
`build()`

Builds the configuration object using the current attributes
 that have been set on this builder object.

`TyrusServerEndpointConfig.Builder`
`configurator(jakarta.websocket.server.ServerEndpointConfig.Configurator serverEndpointConfigurator)`

Sets the custom configurator to use on the configuration
 object built by this builder.

`static TyrusServerEndpointConfig.Builder`
`create(Class<?> endpointClass,
 String path)`

Creates the builder with the mandatory information of the endpoint class
 (programmatic or annotated), the relative URI or URI-template to use,
 and with no subprotocols, extensions, encoders, decoders or custom
 configurator.

`TyrusServerEndpointConfig.Builder`
`decoders(List<Class<? extends jakarta.websocket.Decoder>> decoders)`

Sets the decoder implementation classes to use in the configuration.

`TyrusServerEndpointConfig.Builder`
`encoders(List<Class<? extends jakarta.websocket.Encoder>> encoders)`

Sets the list of encoder implementation classes for this builder.

`TyrusServerEndpointConfig.Builder`
`extensions(List<jakarta.websocket.Extension> extensions)`

Sets the extensions to use in the configuration.

`TyrusServerEndpointConfig.Builder`
`maxSessions(int maxSessions)`

Sets maximal number of open sessions.

`TyrusServerEndpointConfig.Builder`
`subprotocols(List<String> subprotocols)`

Sets the subprotocols to use in the configuration.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

-

## Method Details

-

### create

public static TyrusServerEndpointConfig.Builder create(Class<?> endpointClass,
 String path)
Creates the builder with the mandatory information of the endpoint class
 (programmatic or annotated), the relative URI or URI-template to use,
 and with no subprotocols, extensions, encoders, decoders or custom
 configurator.

Parameters:
`endpointClass` - the class of the endpoint to configure
`path` - The URI or URI template where the endpoint will be deployed.
                      A trailing "/" will be ignored and the path must begin with /.
Returns:
a new instance of TyrusServerEndpointConfig.Builder .

-

### build

public TyrusServerEndpointConfig build()
Builds the configuration object using the current attributes
 that have been set on this builder object.

Returns:
a new TyrusServerEndpointConfig object.

-

### encoders

public TyrusServerEndpointConfig.Builder encoders(List<Class<? extends jakarta.websocket.Encoder>> encoders)
Sets the list of encoder implementation classes for this builder.

Parameters:
`encoders` - the encoders.
Returns:
this builder instance.

-

### decoders

public TyrusServerEndpointConfig.Builder decoders(List<Class<? extends jakarta.websocket.Decoder>> decoders)
Sets the decoder implementation classes to use in the configuration.

Parameters:
`decoders` - the decoders.
Returns:
this builder instance.

-

### subprotocols

public TyrusServerEndpointConfig.Builder subprotocols(List<String> subprotocols)
Sets the subprotocols to use in the configuration.

Parameters:
`subprotocols` - the subprotocols.
Returns:
this builder instance.

-

### extensions

public TyrusServerEndpointConfig.Builder extensions(List<jakarta.websocket.Extension> extensions)
Sets the extensions to use in the configuration.

Parameters:
`extensions` - the extensions to use.
Returns:
this builder instance.

-

### configurator

public TyrusServerEndpointConfig.Builder configurator(jakarta.websocket.server.ServerEndpointConfig.Configurator serverEndpointConfigurator)
Sets the custom configurator to use on the configuration
 object built by this builder.

Parameters:
`serverEndpointConfigurator` - the configurator.
Returns:
this builder instance

-

### maxSessions

public TyrusServerEndpointConfig.Builder maxSessions(int maxSessions)
Sets maximal number of open sessions.

Parameters:
`maxSessions` - maximal number of open session.
Returns:
this builder instance.
