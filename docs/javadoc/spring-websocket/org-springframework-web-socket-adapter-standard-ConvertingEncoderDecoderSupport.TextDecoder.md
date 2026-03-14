# Class ConvertingEncoderDecoderSupport.TextDecoder<T>

java.lang.Object
org.springframework.web.socket.adapter.standard.ConvertingEncoderDecoderSupport<T,String>
org.springframework.web.socket.adapter.standard.ConvertingEncoderDecoderSupport.TextDecoder<T>

Type Parameters:
`T` - the type that this Decoder can convert from

All Implemented Interfaces:
`jakarta.websocket.Decoder, jakarta.websocket.Decoder.Text<T>`

Enclosing class:
`ConvertingEncoderDecoderSupport<T,M>`

---

public abstract static class ConvertingEncoderDecoderSupport.TextDecoder<T>
extends ConvertingEncoderDecoderSupport<T,String>
implements jakarta.websocket.Decoder.Text<T>
A Text `jakarta.websocket.Encoder` that delegates
to Spring's conversion service. See `ConvertingEncoderDecoderSupport` for details.

Since:
4.0
Author:
Phillip Webb

- 

## Nested Class Summary

### Nested classes/interfaces inherited from class ConvertingEncoderDecoderSupport

`ConvertingEncoderDecoderSupport.BinaryDecoder<T>, ConvertingEncoderDecoderSupport.BinaryEncoder<T>, ConvertingEncoderDecoderSupport.TextDecoder<T>, ConvertingEncoderDecoderSupport.TextEncoder<T>`

### Nested classes/interfaces inherited from interface jakarta.websocket.Decoder

`jakarta.websocket.Decoder.Binary<T>, jakarta.websocket.Decoder.BinaryStream<T>, jakarta.websocket.Decoder.Text<T>, jakarta.websocket.Decoder.TextStream<T>`

- 

## Constructor Summary

Constructors

Constructor
Description
`TextDecoder()`
 

- 

## Method Summary

### Methods inherited from class ConvertingEncoderDecoderSupport

`decode, destroy, encode, getApplicationContext, getConversionService, getMessageType, getType, init, willDecode`

### Methods inherited from class Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

### Methods inherited from interface jakarta.websocket.Decoder

`destroy, init`

### Methods inherited from interface jakarta.websocket.Decoder.Text

`decode, willDecode`

- 

## Constructor Details

  - 

### TextDecoder

public TextDecoder()