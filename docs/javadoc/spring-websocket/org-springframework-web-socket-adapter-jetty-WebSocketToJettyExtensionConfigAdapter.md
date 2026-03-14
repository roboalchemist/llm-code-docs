# Class WebSocketToJettyExtensionConfigAdapter

java.lang.Object
org.eclipse.jetty.websocket.common.JettyExtensionConfig
org.springframework.web.socket.adapter.jetty.WebSocketToJettyExtensionConfigAdapter

All Implemented Interfaces:
`org.eclipse.jetty.websocket.api.ExtensionConfig`

---

public class WebSocketToJettyExtensionConfigAdapter
extends org.eclipse.jetty.websocket.common.JettyExtensionConfig
Adapter class to convert a `WebSocketExtension` to a Jetty
`ExtensionConfig`.

Since:
4.0
Author:
Rossen Stoyanchev

- 

## Nested Class Summary

### Nested classes/interfaces inherited from interface org.eclipse.jetty.websocket.api.ExtensionConfig

`org.eclipse.jetty.websocket.api.ExtensionConfig.Parser`

- 

## Constructor Summary

Constructors

Constructor
Description
`WebSocketToJettyExtensionConfigAdapter(WebSocketExtension extension)`
 

- 

## Method Summary

### Methods inherited from class org.eclipse.jetty.websocket.common.JettyExtensionConfig

`getCoreConfig, getName, getParameter, getParameter, getParameterizedName, getParameterKeys, getParameters, setParameter, setParameter, setParameter, toString`

### Methods inherited from class Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`

- 

## Constructor Details

  - 

### WebSocketToJettyExtensionConfigAdapter

public WebSocketToJettyExtensionConfigAdapter(WebSocketExtension extension)