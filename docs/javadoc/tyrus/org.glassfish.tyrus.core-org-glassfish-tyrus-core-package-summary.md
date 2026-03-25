Module org.glassfish.tyrus.core

# Package org.glassfish.tyrus.core

---

package org.glassfish.tyrus.core

Core classes.

-

Related Packages

Package
Description
org.glassfish.tyrus.core.cluster

Cluster relates classes and interfaces.

org.glassfish.tyrus.core.coder

Encoder and decoder adapters and built-in implementations.

org.glassfish.tyrus.core.collection

org.glassfish.tyrus.core.extension

WebSocket Extension support.

org.glassfish.tyrus.core.frame

WebSocket frame representations.

org.glassfish.tyrus.core.l10n

Common internal localization utility classes.

org.glassfish.tyrus.core.monitoring

Monitoring interfaces.

org.glassfish.tyrus.core.uri

URI matching.

org.glassfish.tyrus.core.virtual

-

Class
Description
AnnotatedEndpoint

`Endpoint` descendant which represents deployed annotated endpoint.

BaseContainer

Base WebSocket container.

BaseContainer.ShutDownCondition

Beta

Marker of a public Tyrus API that is still in "beta" non-final version.

CloseReasons

Enum containing standard CloseReasons defined in RFC 6455, see chapter
 7.4.1 Defined Status Codes.

ComponentProvider

Provides an instance.

ComponentProviderService

Provides an instance of component.

DebugContext

A `Logger` wrapper that gives logging records a common formatting and temporarily stores log
 records and postpones their logging until they can be provided with a session ID.

DebugContext.TracingThreshold

Tracing threshold - used for configuration granularity of information that will be sent in tracing headers.

DebugContext.TracingType

Type of tracing - used for tracing configuration.

DebugContext.Type

Type of the record - used to graphically distinguish these message types in the log.

DefaultComponentProvider

Provides instances using reflection.

ErrorCollector

Used to collect deployment errors to present these to the user together.

ExecutorServiceProvider

Handshake

Class responsible for performing and validating handshake.

HandshakeException

`Exception`, which describes the error, occurred during the handshake phase.

MaskingKeyGenerator

Can be implemented to generate masking keys.

MaxSessions

This annotation may be used to annotate server endpoints as a optional annotation
 to `ServerEndpoint`.

MessageHandlerManager

Manages registered `MessageHandler`s and checks whether the new ones may be registered.

OsgiRegistry

Taken from Jersey 2.

ProtocolException

Represents issue with parsing or producing websocket frame.

ProtocolHandler

Tyrus protocol handler.

ReflectionHelper

Utility methods for Java reflection.

ReflectionHelper.ClassTypePair

A tuple consisting of a class and type of the class.

ReflectionHelper.DeclaringClassInterfacePair

A tuple consisting of a concrete class, declaring class that declares a generic interface type.

ReflectionHelper.TypeClassPair

RequestContext

Implementation of all possible request interfaces.

RequestContext.Builder

`RequestContext` builder.

RequestContext.Builder.IsUserInRoleDelegate

Is user in role delegate.

ServerEndpointConfigWrapper

A public class that holds a wrapped ServerEndpointConfig.

ServiceConfigurationError

Taken from Jersey 2.

ServiceFinder<T>

A simple service-provider lookup mechanism.

ServiceFinder.DefaultServiceIteratorProvider

The default service iterator provider that looks up provider classes in
 META-INF/services files.

ServiceFinder.ServiceIteratorProvider

Supports iteration of provider instances or classes.

StrictUtf8

StrictUtf8.Parser

Surrogate parsing support.

TyrusConfiguration

Inner Tyrus configuration properties holder object.

TyrusConfiguration.Builder

TyrusEndpointWrapper

Wraps the registered application class.

TyrusEndpointWrapper.SessionListener

Session listener.

TyrusEndpointWrapper.SessionListener.OnOpenResult

Result of `TyrusEndpointWrapper.SessionListener.onOpen(TyrusSession)`.

TyrusExtension

WebSocket `Extension` implementation.

TyrusExtension.TyrusParameter

WebSocket `Extension.Parameter` implementation.

TyrusFuture<T>

Tyrus `Future` implementation.

TyrusRemoteEndpoint

Wraps the `RemoteEndpoint` and represents the other side of the websocket connection.

TyrusServerEndpointConfig

Configuration `ServerEndpointConfig` enhanced
 to offer tyrus specific attributes like maxSessions.

TyrusServerEndpointConfig.Builder

The TyrusServerEndpointConfig.Builder is a class used for creating
 `TyrusServerEndpointConfig.Builder` objects for the purposes of
 deploying a server endpoint.

TyrusServerEndpointConfigurator

Tyrus' implementation of `ServerEndpointConfig.Configurator`.

TyrusSession

Implementation of the `Session`.

TyrusUpgradeResponse

HTTP response representation.

TyrusWebSocket

Tyrus representation of web socket connection.

TyrusWebSocketEngine

`WebSocketEngine` implementation, which handles server-side handshake, validation and data processing.

TyrusWebSocketEngine.TyrusWebSocketEngineBuilder

`TyrusWebSocketEngine` builder.

Utf8DecodingException

TODO

Utils

Utility methods shared among Tyrus modules.

Utils.Stringifier<T>

Define to `String` conversion for various types.

Version

TODO

WebSocketException

WebSocketException can be thrown during runtime (after handshake).
