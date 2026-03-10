# Source: https://img.ly/docs/cesdk/android/concepts/buffers-9c565b/

---
title: "Buffers"
description: "Use buffers to store temporary, non-serializable data in CE.SDK via the CreativeEngine API."
platform: android
url: "https://img.ly/docs/cesdk/android/concepts/buffers-9c565b/"
---

> This is one page of the CE.SDK Android documentation. For a complete overview, see the [Android Documentation Index](https://img.ly/docs/cesdk/android.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/android/llms-full.txt).

**Navigation:** [Concepts](https://img.ly/docs/cesdk/android/concepts-c9ff51/) > [Buffers](https://img.ly/docs/cesdk/android/concepts/buffers-9c565b/)

---

```kotlin reference-only
// Create an audio block and append it to the page
val audioBlock = engine.block.create(DesignBlockType.Audio)
engine.block.appendChild(parent = page, child = audioBlock)

// Create a buffer
val audioBuffer = engine.editor.createBuffer()

// Reference the audio buffer resource from the audio block
engine.block.setUri(
    block = audioBlock,
    property = "audio/fileURI",
    value = audioBuffer
)

// Generate 10 seconds of stereo 48 kHz audio data
val sampleCount = 10 * 48000
val byteBuffer = ByteBuffer.allocate(2 * 4 * sampleCount) //2 channels, each 4 bytes
repeat(sampleCount) {
    val sample = sin((440 * it * 2 * PI) / 48000).toFloat()
    byteBuffer.putFloat(sample)
    byteBuffer.putFloat(sample)
}
// Assign the audio data to the buffer
val data = ByteArray(byteBuffer.capacity())
byteBuffer.position(0)
byteBuffer.get(data)
engine.editor.setBufferData(uri = audioBuffer, offset = 0, data = data)

// We can get subranges of the buffer data
val chunk = engine.editor.getBufferData(uri = audioBuffer, offset = 0, length = 4096)

// Get current length of the buffer in bytes
val length = engine.editor.getBufferLength(uri = audioBuffer)

// Reduce the buffer to half its length, leading to 5 seconds worth of audio
engine.editor.setBufferLength(uri = audioBuffer, length = data.size / 2)

// Free data
engine.editor.destroyBuffer(uri = audioBuffer)
```

In this example, we will show you how to use the [CreativeEditor SDK](https://img.ly/products/creative-sdk)'s CreativeEngine to create buffers through the `editor` API. Buffers can hold arbitrary data.

> **Note:** **Limitations**Buffers are intended for temporary data only.* Buffer data is not part of the [scene serialization](https://img.ly/docs/cesdk/android/concepts/scenes-e8596d/)
> * Changes to buffers can't be undone using the [history system](https://img.ly/docs/cesdk/android/concepts/undo-and-history-99479d/)

```kotlin
fun createBuffer(): Uri
```

Create a resizable buffer that can hold arbitrary data.

- Returns a uri to identify the buffer.

```kotlin
fun destroyBuffer(uri: Uri)
```

Destroy a buffer and free its resources.

- `uri`: the uri of the buffer to destroy.

```kotlin
fun setBufferData(
    uri: Uri,
    offset: Int,
    data: ByteBuffer,
)
```

Set the data of a buffer.

- `uri`: the uri of the buffer.

- `offset`: the offset in bytes at which to start writing.

- `data`: the data to write. Note that it has to be a direct `ByteBuffer`, created either via

`ByteBuffer.allocateDirect` or via JNI NewDirectByteBuffer API.

```kotlin
fun getBufferData(
    uri: Uri,
    offset: Int,
    length: Int,
): ByteBuffer
```

Get the data of a buffer.

- `uri`: the uri of the buffer.

- `offset`: the offset in bytes at which to start reading.

- `length`: the number of bytes to read.

- Returns the data read from the buffer or an error.

```kotlin
fun setBufferLength(
    uri: Uri,
    length: Int,
)
```

Set the length of a buffer.

- `uri`: the uri of the buffer.

- `length`: the new length of the buffer in bytes.

```kotlin
fun getBufferLength(uri: Uri): Int
```

Get the length of a buffer.

- `uri`: the uri of the buffer.

- Returns the length of the buffer in bytes.

## Full Code

Here's the full code:

```kotlin
// Create an audio block and append it to the page
val audioBlock = engine.block.create(DesignBlockType.Audio)
engine.block.appendChild(parent = page, child = audioBlock)

// Create a buffer
val audioBuffer = engine.editor.createBuffer()

// Reference the audio buffer resource from the audio block
engine.block.setUri(
    block = audioBlock,
    property = "audio/fileURI",
    value = audioBuffer
)

// Generate 10 seconds of stereo 48 kHz audio data
val sampleCount = 10 * 48000
val byteBuffer = ByteBuffer.allocate(2 * 4 * sampleCount) //2 channels, each 4 bytes
repeat(sampleCount) {
    val sample = sin((440 * it * 2 * PI) / 48000).toFloat()
    byteBuffer.putFloat(sample)
    byteBuffer.putFloat(sample)
}
// Assign the audio data to the buffer
val data = ByteArray(byteBuffer.capacity())
byteBuffer.position(0)
byteBuffer.get(data)
engine.editor.setBufferData(uri = audioBuffer, offset = 0, data = data)

// We can get subranges of the buffer data
val chunk = engine.editor.getBufferData(uri = audioBuffer, offset = 0, length = 4096)

// Get current length of the buffer in bytes
val length = engine.editor.getBufferLength(uri = audioBuffer)

// Reduce the buffer to half its length, leading to 5 seconds worth of audio
engine.editor.setBufferLength(uri = audioBuffer, length = data.size / 2)

// Free data
engine.editor.destroyBuffer(uri = audioBuffer)
```



---

## More Resources

- **[Android Documentation Index](https://img.ly/docs/cesdk/android.md)** - Browse all Android documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/android/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/android/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
