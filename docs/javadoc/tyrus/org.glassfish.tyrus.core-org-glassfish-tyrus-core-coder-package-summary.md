Module org.glassfish.tyrus.core

# Package org.glassfish.tyrus.core.coder

---

package org.glassfish.tyrus.core.coder

Encoder and decoder adapters and built-in implementations.

-

Related Packages

Package
Description
org.glassfish.tyrus.core

Core classes.

-

Classes

Class
Description
CoderAdapter

Adapter for `Encoder` and `Decoder` which implements lifecycle
 methods.

CoderWrapper<T>

Wrapper of coders storing the coder coder class (and optionally coder instance), return type of the encode / decode
 method and coder class.

InputStreamDecoder

Built in `Decoder` for `InputStream`.

NoOpByteArrayCoder

`Encoder` and `Decoder` implementation for byte array.

NoOpByteBufferCoder

`Encoder` and `Decoder` implementation for `ByteBuffer`.

NoOpTextCoder

PrimitiveDecoders<T>

Collection of decoders for all primitive types.

PrimitiveDecoders.BooleanDecoder

PrimitiveDecoders.ByteDecoder

PrimitiveDecoders.CharacterDecoder

PrimitiveDecoders.DoubleDecoder

PrimitiveDecoders.FloatDecoder

PrimitiveDecoders.IntegerDecoder

PrimitiveDecoders.LongDecoder

PrimitiveDecoders.ShortDecoder

ReaderDecoder

Built in `Decoder` for `Reader`.

ToStringEncoder

Fall-back encoder - encoders any object to string using `Object.toString()` method.
