# Source: https://img.ly/docs/cesdk/ios/concepts/buffers-9c565b/

---
title: "Buffers"
description: "Use buffers to store temporary, non-serializable data in CE.SDK via the CreativeEngine API."
platform: ios
url: "https://img.ly/docs/cesdk/ios/concepts/buffers-9c565b/"
---

> This is one page of the CE.SDK iOS documentation. For a complete overview, see the [iOS Documentation Index](https://img.ly/docs/cesdk/ios.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/ios/llms-full.txt).

**Navigation:** [Concepts](https://img.ly/docs/cesdk/ios/concepts-c9ff51/) > [Buffers](https://img.ly/docs/cesdk/ios/concepts/buffers-9c565b/)

---

```swift reference-only
// Create an audio block and append it to the page
let audioBlock = try engine.block.create(.audio)
try engine.block.appendChild(to: page, child: audioBlock)

// Create a buffer
let audioBuffer = engine.editor.createBuffer()

// Reference the audio buffer resource from the audio block
try engine.block.setURL(audioBlock, property: "audio/fileURI", value: audioBuffer)

// Generate 10 seconds of stereo 48 kHz audio data
let samples = ContiguousArray<Float>(unsafeUninitializedCapacity: 10 * 2 * 48000) { buffer, initializedCount in
  for i in stride(from: 0, to: buffer.count, by: 2) {
    let sample = sin((440.0 * Float(i) * Float.pi) / 48000.0)
    buffer[i + 0] = sample
    buffer[i + 1] = sample
  }
  initializedCount = buffer.count
}

// Assign the audio data to the buffer
try samples.withUnsafeBufferPointer { buffer in
try engine.editor.setBufferData(url: audioBuffer, offset: 0, data: Data(buffer: buffer))
}

// We can get subranges of the buffer data
let chunk = try engine.editor.getBufferData(url: audioBuffer, offset: 0, length: 4096)

// Get current length of the buffer in bytes
let length = try engine.editor.getBufferLength(url: audioBuffer)

// Reduce the buffer to half its length, leading to 5 seconds worth of audio
try engine.editor.setBufferLength(url: audioBuffer,length: UInt(truncating: length) / 2)

// Free data
try engine.editor.destroyBuffer(url: audioBuffer)
```

In this example, we will show you how to use the [CreativeEditor SDK](https://img.ly/products/creative-sdk)'s CreativeEngine to create buffers through the `editor` API. Buffers can hold arbitrary data.

> **Note:** **Limitations**Buffers are intended for temporary data only.* Buffer data is not part of the [scene serialization](https://img.ly/docs/cesdk/ios/concepts/scenes-e8596d/)
> * Changes to buffers can't be undone using the [history system](https://img.ly/docs/cesdk/ios/concepts/undo-and-history-99479d/)

```swift
public func createBuffer() -> URL
```

Create a resizable buffer that can hold arbitrary data.

- Returns: A URL to identify the buffer.

```swift
public func destroyBuffer(url: URL) throws
```

Destroy a buffer and free its resources.

- `url`: The URL of the buffer to destroy.

```swift
public func setBufferData(url: URL, offset: UInt, data: Data) throws
```

Set the data of a buffer.

- `url`: The URL of the buffer.
- `offset`: The offset in bytes at which to start writing.
- `data`: The data to write.

```swift
public func getBufferData(url: URL, offset: UInt, length: UInt) throws -> Data
```

Get the data of a buffer.

- `url`: The URL of the buffer.
- `offset`: The offset in bytes at which to start reading.
- `length`: The number of bytes to read.
- Returns: The data read from the buffer or an error.

```swift
public func setBufferLength(url: URL, length: UInt) throws
```

Set the length of a buffer.

- `url`: The URL of the buffer.
- `length`: The new length of the buffer in bytes.

```swift
public func getBufferLength(url: URL) throws -> NSNumber
```

Get the length of a buffer.

- `url`: The URL of the buffer.
- Returns: The length of the buffer in bytes.

## Full Code

Here's the full code:

```swift
// Create an audio block and append it to the page
let audioBlock = try engine.block.create(.audio)
try engine.block.appendChild(to: page, child: audioBlock)

// Create a buffer
let audioBuffer = engine.editor.createBuffer()

// Reference the audio buffer resource from the audio block
try engine.block.setURL(audioBlock, property: "audio/fileURI", value: audioBuffer)

// Generate 10 seconds of stereo 48 kHz audio data
let samples = ContiguousArray<Float>(unsafeUninitializedCapacity: 10 * 2 * 48000) { buffer, initializedCount in
  for i in stride(from: 0, to: buffer.count, by: 2) {
    let sample = sin((440.0 * Float(i) * Float.pi) / 48000.0)
    buffer[i + 0] = sample
    buffer[i + 1] = sample
  }
  initializedCount = buffer.count
}

// Assign the audio data to the buffer
try samples.withUnsafeBufferPointer { buffer in
try engine.editor.setBufferData(url: audioBuffer, offset: 0, data: Data(buffer: buffer))
}

// We can get subranges of the buffer data
let chunk = try engine.editor.getBufferData(url: audioBuffer, offset: 0, length: 4096)

// Get current length of the buffer in bytes
let length = try engine.editor.getBufferLength(url: audioBuffer)

// Reduce the buffer to half its length, leading to 5 seconds worth of audio
try engine.editor.setBufferLength(url: audioBuffer,length: UInt(truncating: length) / 2)

// Free data
try engine.editor.destroyBuffer(url: audioBuffer)
```



---

## More Resources

- **[iOS Documentation Index](https://img.ly/docs/cesdk/ios.md)** - Browse all iOS documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/ios/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/ios/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
