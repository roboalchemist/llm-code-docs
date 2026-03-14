# Class ConvertingEncoderDecoderSupport<T,M>

java.lang.Object
org.springframework.web.socket.adapter.standard.ConvertingEncoderDecoderSupport<T,M>

Type Parameters:
`T` - the type being converted to (for Encoder) or from (for Decoder)
`M` - the WebSocket message type (`String` or `ByteBuffer`)

Direct Known Subclasses:
`ConvertingEncoderDecoderSupport.BinaryDecoder, ConvertingEncoderDecoderSupport.BinaryEncoder, ConvertingEncoderDecoderSupport.TextDecoder, ConvertingEncoderDecoderSupport.TextEncoder`

---

public abstract class ConvertingEncoderDecoderSupport<T,M>
extends Object
Base class that can be used to implement a standard `Encoder`
and/or `Decoder`. It provides encode and decode method
implementations that delegate to a Spring `ConversionService`.

By default, this class looks up a `ConversionService` registered in the
`active ApplicationContext` under
the name `'webSocketConversionService'`. This works fine for both client
and server endpoints, in a Servlet container environment. If not running in a
Servlet container, subclasses will need to override the
`getConversionService()` method to provide an alternative lookup strategy.

Subclasses can extend this class and should also implement one or
both of `Encoder` and `Decoder`.
For convenience `ConvertingEncoderDecoderSupport.BinaryEncoder`,
`ConvertingEncoderDecoderSupport.BinaryDecoder`,
`ConvertingEncoderDecoderSupport.TextEncoder` and
`ConvertingEncoderDecoderSupport.TextDecoder` subclasses are provided.

Since JSR-356 only allows Encoder/Decoder to be registered by type, instances
of this class are therefore managed by the WebSocket runtime, and do not need to
be registered as Spring Beans. They can, however, by injected with Spring-managed
dependencies via `@Autowire`.

Converters to convert between the `type` and `String` or
`ByteBuffer` should be registered.

Since:
4.0
Author:
Phillip Webb
See Also:

- `ConvertingEncoderDecoderSupport.BinaryEncoder`

- `ConvertingEncoderDecoderSupport.BinaryDecoder`

- `ConvertingEncoderDecoderSupport.TextEncoder`

- `ConvertingEncoderDecoderSupport.TextDecoder`

- 

## Nested Class Summary

Nested Classes

Modifier and Type
Class
Description
`static class `
`ConvertingEncoderDecoderSupport.BinaryDecoder<T>`

A binary `jakarta.websocket.Encoder` that delegates
to Spring's conversion service.

`static class `
`ConvertingEncoderDecoderSupport.BinaryEncoder<T>`

A binary `jakarta.websocket.Encoder` that delegates
to Spring's conversion service.

`static class `
`ConvertingEncoderDecoderSupport.TextDecoder<T>`

A Text `jakarta.websocket.Encoder` that delegates
to Spring's conversion service.

`static class `
`ConvertingEncoderDecoderSupport.TextEncoder<T>`

A text `jakarta.websocket.Encoder` that delegates
to Spring's conversion service.

- 

## Constructor Summary

Constructors

Constructor
Description
`ConvertingEncoderDecoderSupport()`
 

- 

## Method Summary

Modifier and Type
Method
Description
`@Nullable T`
`decode(M message)`

Decode the message into an object.

`void`
`destroy()`

Called to destroy the encoder/decoder.

`@Nullable M`
`encode(T object)`

Encode an object to a message.

`protected @Nullable org.springframework.context.ApplicationContext`
`getApplicationContext()`

Returns the active `ApplicationContext`.

`protected org.springframework.core.convert.ConversionService`
`getConversionService()`

Strategy method used to obtain the `ConversionService`.

`protected org.springframework.core.convert.TypeDescriptor`
`getMessageType()`

Returns the websocket message type.

`protected org.springframework.core.convert.TypeDescriptor`
`getType()`

Returns the type being converted.

`void`
`init(jakarta.websocket.EndpointConfig config)`

Called to initialize the encoder/decoder.

`boolean`
`willDecode(M bytes)`

Determine if a given message can be decoded.

### Methods inherited from class Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Constructor Details

  - 

### ConvertingEncoderDecoderSupport

public ConvertingEncoderDecoderSupport()

- 

## Method Details

  - 

### init

public void init(jakarta.websocket.EndpointConfig config)
Called to initialize the encoder/decoder.

See Also:

    - `Encoder.init(EndpointConfig)`

    - `Decoder.init(EndpointConfig)`

  - 

### destroy

public void destroy()
Called to destroy the encoder/decoder.

See Also:

    - `Encoder.destroy()`

    - `Decoder.destroy()`

  - 

### getConversionService

protected org.springframework.core.convert.ConversionService getConversionService()
Strategy method used to obtain the `ConversionService`. By default, this
method expects a bean named `'webSocketConversionService'` in the
`active ApplicationContext`.

Returns:
the `ConversionService` (never null)

  - 

### getApplicationContext

protected @Nullable org.springframework.context.ApplicationContext getApplicationContext()
Returns the active `ApplicationContext`. By default, this method obtains
the context via `ContextLoader.getCurrentWebApplicationContext()`, which
finds the ApplicationContext loaded via `ContextLoader` typically in a
Servlet container environment. When not running in a Servlet container and
not using `ContextLoader`, this method should be overridden.

Returns:
the `ApplicationContext` or `null`

  - 

### getType

protected org.springframework.core.convert.TypeDescriptor getType()
Returns the type being converted. By default, the type is resolved using
the generic arguments of the class.

  - 

### getMessageType

protected org.springframework.core.convert.TypeDescriptor getMessageType()
Returns the websocket message type. By default, the type is resolved using
the generic arguments of the class.

  - 

### encode

public @Nullable M encode(T object)
                   throws jakarta.websocket.EncodeException
Encode an object to a message.

Throws:
`jakarta.websocket.EncodeException`
See Also:

    - `Encoder.Text.encode(Object)`

    - `Encoder.Binary.encode(Object)`

  - 

### willDecode

public boolean willDecode(M bytes)
Determine if a given message can be decoded.

See Also:

    - `decode(Object)`

    - `Decoder.Text.willDecode(String)`

    - `Decoder.Binary.willDecode(ByteBuffer)`

  - 

### decode

public @Nullable T decode(M message)
                   throws jakarta.websocket.DecodeException
Decode the message into an object.

Throws:
`jakarta.websocket.DecodeException`
See Also:

    - `Decoder.Text.decode(String)`

    - `Decoder.Binary.decode(ByteBuffer)`