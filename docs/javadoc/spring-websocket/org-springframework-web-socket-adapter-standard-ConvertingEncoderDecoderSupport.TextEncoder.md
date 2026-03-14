# Class ConvertingEncoderDecoderSupport.TextEncoder<T>

java.lang.Object
org.springframework.web.socket.adapter.standard.ConvertingEncoderDecoderSupport<T,String>
org.springframework.web.socket.adapter.standard.ConvertingEncoderDecoderSupport.TextEncoder<T>

Type Parameters:
`T` - the type that this Encoder can convert to

All Implemented Interfaces:
`jakarta.websocket.Encoder, jakarta.websocket.Encoder.Text<T>`

Enclosing class:
`ConvertingEncoderDecoderSupport<T,M>`

---

public abstract static class ConvertingEncoderDecoderSupport.TextEncoder<T>
extends ConvertingEncoderDecoderSupport<T,String>
implements jakarta.websocket.Encoder.Text<T>
A text `jakarta.websocket.Encoder` that delegates
to Spring's conversion service. See `ConvertingEncoderDecoderSupport` for
details.

Since:
4.0
Author:
Phillip Webb

- 

## Nested Class Summary

### Nested classes/interfaces inherited from class ConvertingEncoderDecoderSupport

`ConvertingEncoderDecoderSupport.BinaryDecoder<T>, ConvertingEncoderDecoderSupport.BinaryEncoder<T>, ConvertingEncoderDecoderSupport.TextDecoder<T>, ConvertingEncoderDecoderSupport.TextEncoder<T>`

### Nested classes/interfaces inherited from interface jakarta.websocket.Encoder

`jakarta.websocket.Encoder.Binary<T>, jakarta.websocket.Encoder.BinaryStream<T>, jakarta.websocket.Encoder.Text<T>, jakarta.websocket.Encoder.TextStream<T>`

- 

## Constructor Summary

Constructors

Constructor
Description
`TextEncoder()`
 

- 

## Method Summary

### Methods inherited from class ConvertingEncoderDecoderSupport

`decode, destroy, encode, getApplicationContext, getConversionService, getMessageType, getType, init, willDecode`

### Methods inherited from class Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

### Methods inherited from interface jakarta.websocket.Encoder

`destroy, init`

### Methods inherited from interface jakarta.websocket.Encoder.Text

`encode`

- 

## Constructor Details

  - 

### TextEncoder

public TextEncoder()