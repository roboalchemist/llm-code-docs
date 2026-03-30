# Class: EventAPI

Subscribe to block lifecycle events in the design engine.

The EventAPI enables real-time monitoring of block changes through event subscriptions. Events are bundled and delivered efficiently at the end of each engine update cycle.

## Constructors[#](#constructors)

### Constructor[#](#constructor)

  

`EventAPI`

## Event Subscriptions[#](#event-subscriptions)

Subscribe to block lifecycle events with filtering and callback management.

### subscribe()[#](#subscribe)

  

Subscribe to block lifecycle events.

Events are bundled and delivered at the end of each engine update cycle for efficient processing.

#### Parameters[#](#parameters)

| Parameter | Type | Description |
| --- | --- | --- |
| `blocks` | `number`\[\] | List of blocks to filter events by. If empty, events for all blocks are sent. |
| `callback` | (`events`) => `void` | Function called with bundled events. |

#### Returns[#](#returns)

A method to unsubscribe from the events.

```
(): void;
```

##### Returns[#](#returns-1)

`void`

---



[Source](https:/img.ly/docs/cesdk/vue/api/engine/classes/editorapi)