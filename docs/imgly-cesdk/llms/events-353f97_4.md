# Source: https://img.ly/docs/cesdk/ios/concepts/events-353f97/

---
title: "Events"
description: "Subscribe to block creation, update, and deletion events to track changes in your CE.SDK scene."
platform: ios
url: "https://img.ly/docs/cesdk/ios/concepts/events-353f97/"
---

> This is one page of the CE.SDK iOS documentation. For a complete overview, see the [iOS Documentation Index](https://img.ly/docs/cesdk/ios.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/ios/llms-full.txt).

**Navigation:** [Concepts](https://img.ly/docs/cesdk/ios/concepts-c9ff51/) > [Events](https://img.ly/docs/cesdk/ios/concepts/events-353f97/)

---

```swift reference-only
let scene = try engine.scene.create()
let page = try engine.block.create(.page)
try engine.block.appendChild(to: scene, child: page)

let block = try engine.block.create(.graphic)
try engine.block.setShape(block, shape: engine.block.createShape(.star))
try engine.block.setFill(block, fill: engine.block.createFill(.color))
try engine.block.appendChild(to: page, child: block)

let task = Task {
  for await events in engine.event.subscribe(to: [block]) {
    for event in events {
      print("Event: \(event.type) \(event.block)")
      if engine.block.isValid(event.block) {
        let type = try engine.block.getType(event.block)
        print("Block type: \(type)")
      }
    }
  }
}

try await Task.sleep(for: .seconds(1))
try engine.block.setRotation(block, radians: 0.5 * .pi)
try await Task.sleep(for: .seconds(1))
try engine.block.destroy(block)
try await Task.sleep(for: .seconds(1))
```

In this example, we will show you how to use the [CreativeEditor SDK](https://img.ly/products/creative-sdk)'s CreativeEngine to subscribe to creation, update, and destruction events of design blocks.

## Subscribing to Events

The event API provides a single function to subscribe to design block events. The types of events are:

- `'Created'`: The design block was just created.

- `'Updated'`: A property of the design block was updated.

- `'Destroyed'`: The design block was destroyed. Note that a destroyed block will have become invalid and trying to use Block API functions on it will result in an exception. You can always use the Block API's `isValid` function to verify whether a block is valid before use.

All events that occur during an engine update are batched, deduplicated, and always delivered at the very end of the engine update. Deduplication means you will receive at most one `'Updated'` event per block per subscription, even though there could potentially be multiple updates to a block during the engine update. To be clear, this also means the order of the event list provided to your event callback won't reflect the actual order of events within an engine update.

```swift
public func subscribe(to blocks: [DesignBlockID]) -> AsyncStream<[BlockEvent]>
```

Subscribe to block life-cycle events.

- `blocks:`: A list of blocks to filter events by. If the list is empty, events for every block are sent.
- Returns: A stream of events. Events are bundled and sent at the end of each engine update.

## Full Code

```swift
let scene = try engine.scene.create()
let page = try engine.block.create(.page)
try engine.block.appendChild(to: scene, child: page)

let block = try engine.block.create(.graphic)
try engine.block.setShape(block, shape: engine.block.createShape(.star))
try engine.block.setFill(block, fill: engine.block.createFill(.color))
try engine.block.appendChild(to: page, child: block)

let task = Task {
  for await events in engine.event.subscribe(to: [block]) {
    for event in events {
      print("Event: \(event.type) \(event.block)")
      if engine.block.isValid(event.block) {
        let type = try engine.block.getType(event.block)
        print("Block type: \(type)")
      }
    }
  }
}

try await Task.sleep(for: .seconds(1))
try engine.block.setRotation(block, radians: 0.5 * .pi)
try await Task.sleep(for: .seconds(1))
try engine.block.destroy(block)
try await Task.sleep(for: .seconds(1))
```



---

## More Resources

- **[iOS Documentation Index](https://img.ly/docs/cesdk/ios.md)** - Browse all iOS documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/ios/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/ios/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
