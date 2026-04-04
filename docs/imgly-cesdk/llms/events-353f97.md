# Source: https://img.ly/docs/cesdk/android/concepts/events-353f97/

---
title: "Events"
description: "Subscribe to block creation, update, and deletion events to track changes in your CE.SDK scene."
platform: android
url: "https://img.ly/docs/cesdk/android/concepts/events-353f97/"
---

> This is one page of the CE.SDK Android documentation. For a complete overview, see the [Android Documentation Index](https://img.ly/docs/cesdk/android.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/android/llms-full.txt).

**Navigation:** [Concepts](https://img.ly/docs/cesdk/android/concepts-c9ff51/) > [Events](https://img.ly/docs/cesdk/android/concepts/events-353f97/)

---

```kotlin reference-only
val coroutineScope = CoroutineScope(Dispatchers.Main)
val scene = engine.scene.create()
val page = engine.block.create(DesignBlockType.Page)
engine.block.appendChild(parent = scene, child = page)
val block = engine.block.create(DesignBlockType.Graphic)
engine.block.setShape(block, shape = engine.block.createShape(ShapeType.Star))
engine.block.setFill(block, fill = engine.block.createFill(FillType.Color))
engine.block.appendChild(parent = page, child = block)

engine.event.subscribe(listOf(block))
	.onEach { events ->
		events.forEach { event ->
			println("Event: ${event.type} ${event.block}")
			if (engine.block.isValid(event.block)) {
				val type = engine.block.getType(event.block)
				println("Block type: $type")
			}
		}
	}
	.launchIn(coroutineScope)

coroutineScope.launch {
	delay(1000)
	engine.block.setRotation(block, radians = 0.5F * PI.toFloat())
	delay(1000)
	engine.block.destroy(block)
	delay(1000)
}
```

In this example, we will show you how to use the [CreativeEditor SDK](https://img.ly/products/creative-sdk)'s CreativeEngine to subscribe to creation, update, and destruction events of design blocks.

## Subscribing to Events

The event API provides a single function to subscribe to design block events. The types of events are:

- `Created`: The design block was just created.

- `Updated`: A property of the design block was updated.

- `Destroyed`: The design block was destroyed. Note that a destroyed block will have become invalid and trying to use Block API functions on it will result in an exception. You can always use the Block API's `isValid` function to verify whether a block is valid before use.

All events that occur during an engine update are batched, deduplicated, and always delivered at the very end of the engine update. Deduplication means you will receive at most one `Updated` event per block per subscription, even though there could potentially be multiple updates to a block during the engine update. To be clear, this also means the order of the event list provided to your event callback won't reflect the actual order of events within an engine update.

```kotlin
fun subscribe(blocks: List<DesignBlock> = emptyList()): Flow<List<DesignBlockEvent>>
```

Subscribe to block life-cycle events

- `blocks`: a list of blocks to filter events by. If the list is empty, events for every block are sent.

## Full Code

Here's the full code:

```kotlin
val coroutineScope = CoroutineScope(Dispatchers.Main)
val scene = engine.scene.create()
val page = engine.block.create(DesignBlockType.Page)
engine.block.appendChild(parent = scene, child = page)
val block = engine.block.create(DesignBlockType.Graphic)
engine.block.setShape(block, shape = engine.block.createShape(ShapeType.Star))
engine.block.setFill(block, fill = engine.block.createFill(FillType.Color))
engine.block.appendChild(parent = page, child = block)

engine.event.subscribe(listOf(block))
    .onEach { events ->
        events.forEach { event ->
            println("Event: ${event.type} ${event.block}")
            if (engine.block.isValid(event.block)) {
                val type = engine.block.getType(event.block)
                println("Block type: $type")
            }
        }
    }
    .launchIn(coroutineScope)

coroutineScope.launch {
    delay(1000)
    engine.block.setRotation(block, radians = 0.5F * PI.toFloat())
    delay(1000)
    engine.block.destroy(block)
    delay(1000)
}
```



---

## More Resources

- **[Android Documentation Index](https://img.ly/docs/cesdk/android.md)** - Browse all Android documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/android/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/android/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
