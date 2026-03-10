# Interface: RefocusEvent

Dispatched on the engine canvas right before the engine will refocus its text input after a blur. Call `preventDefault()` to prevent the refocusing.

## Extends[#](#extends)

*   `CustomEvent`<`EventTarget` | `null`\>

## Methods[#](#methods)

### preventDefault()[#](#preventdefault)

```
preventDefault(): void;
```

Prevent refocusing the engine input

#### Returns[#](#returns)

`void`

#### Overrides[#](#overrides)

```
CustomEvent.preventDefault
```

* * *

### ~initCustomEvent()~[#](#initcustomevent)

```
initCustomEvent(   type,   bubbles?,   cancelable?,   detail?): void;
```

#### Parameters[#](#parameters)

| Parameter | Type |
| --- | --- |
| `type` | `string` |
| `bubbles?` | `boolean` |
| `cancelable?` | `boolean` |
| `detail?` | `EventTarget` |

#### Returns[#](#returns-1)

`void`

#### Deprecated[#](#deprecated)

[MDN Reference](https://developer.mozilla.org/docs/Web/API/CustomEvent/initCustomEvent)

#### Inherited from[#](#inherited-from)

```
CustomEvent.initCustomEvent
```

* * *

### composedPath()[#](#composedpath)

```
composedPath(): EventTarget[];
```

Returns the invocation target objects of event’s path (objects on which listeners will be invoked), except for any nodes in shadow trees of which the shadow root’s mode is “closed” that are not reachable from event’s currentTarget.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Event/composedPath)

#### Returns[#](#returns-2)

`EventTarget`\[\]

#### Inherited from[#](#inherited-from-1)

```
CustomEvent.composedPath
```

* * *

### ~initEvent()~[#](#initevent)

```
initEvent(   type,   bubbles?,   cancelable?): void;
```

#### Parameters[#](#parameters-1)

| Parameter | Type |
| --- | --- |
| `type` | `string` |
| `bubbles?` | `boolean` |
| `cancelable?` | `boolean` |

#### Returns[#](#returns-3)

`void`

#### Deprecated[#](#deprecated-1)

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Event/initEvent)

#### Inherited from[#](#inherited-from-2)

```
CustomEvent.initEvent
```

* * *

### stopImmediatePropagation()[#](#stopimmediatepropagation)

```
stopImmediatePropagation(): void;
```

Invoking this method prevents event from reaching any registered event listeners after the current one finishes running and, when dispatched in a tree, also prevents event from reaching any other objects.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Event/stopImmediatePropagation)

#### Returns[#](#returns-4)

`void`

#### Inherited from[#](#inherited-from-3)

```
CustomEvent.stopImmediatePropagation
```

* * *

### stopPropagation()[#](#stoppropagation)

```
stopPropagation(): void;
```

When dispatched in a tree, invoking this method prevents event from reaching any objects other than the current object.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Event/stopPropagation)

#### Returns[#](#returns-5)

`void`

#### Inherited from[#](#inherited-from-4)

```
CustomEvent.stopPropagation
```

## Properties[#](#properties)

| Property | Modifier | Type | Description | Overrides | Inherited from |
| --- | --- | --- | --- | --- | --- |
| `type` | `readonly` | `"cesdk-refocus"` | Returns the type of event, e.g. “click”, “hashchange”, or “submit”. [MDN Reference](https://developer.mozilla.org/docs/Web/API/Event/type) | `CustomEvent.type` | \- |
| `detail` | `readonly` | `EventTarget` | Contains the element that has received focus during the blur, or null | `CustomEvent.detail` | \- |
| `bubbles` | `readonly` | `boolean` | Returns true or false depending on how event was initialized. True if event goes through its target’s ancestors in reverse tree order, and false otherwise. [MDN Reference](https://developer.mozilla.org/docs/Web/API/Event/bubbles) | \- | `CustomEvent.bubbles` |
| ~`cancelBubble`~ | `public` | `boolean` | **Deprecated** [MDN Reference](https://developer.mozilla.org/docs/Web/API/Event/cancelBubble) | \- | `CustomEvent.cancelBubble` |
| `cancelable` | `readonly` | `boolean` | Returns true or false depending on how event was initialized. Its return value does not always carry meaning, but true can indicate that part of the operation during which event was dispatched, can be canceled by invoking the preventDefault() method. [MDN Reference](https://developer.mozilla.org/docs/Web/API/Event/cancelable) | \- | `CustomEvent.cancelable` |
| `composed` | `readonly` | `boolean` | Returns true or false depending on how event was initialized. True if event invokes listeners past a ShadowRoot node that is the root of its target, and false otherwise. [MDN Reference](https://developer.mozilla.org/docs/Web/API/Event/composed) | \- | `CustomEvent.composed` |
| `currentTarget` | `readonly` | `EventTarget` | Returns the object whose event listener’s callback is currently being invoked. [MDN Reference](https://developer.mozilla.org/docs/Web/API/Event/currentTarget) | \- | `CustomEvent.currentTarget` |
| `defaultPrevented` | `readonly` | `boolean` | Returns true if preventDefault() was invoked successfully to indicate cancelation, and false otherwise. [MDN Reference](https://developer.mozilla.org/docs/Web/API/Event/defaultPrevented) | \- | `CustomEvent.defaultPrevented` |
| `eventPhase` | `readonly` | `number` | Returns the event’s phase, which is one of NONE, CAPTURING\_PHASE, AT\_TARGET, and BUBBLING\_PHASE. [MDN Reference](https://developer.mozilla.org/docs/Web/API/Event/eventPhase) | \- | `CustomEvent.eventPhase` |
| `isTrusted` | `readonly` | `boolean` | Returns true if event was dispatched by the user agent, and false otherwise. [MDN Reference](https://developer.mozilla.org/docs/Web/API/Event/isTrusted) | \- | `CustomEvent.isTrusted` |
| ~`returnValue`~ | `public` | `boolean` | **Deprecated** [MDN Reference](https://developer.mozilla.org/docs/Web/API/Event/returnValue) | \- | `CustomEvent.returnValue` |
| ~`srcElement`~ | `readonly` | `EventTarget` | **Deprecated** [MDN Reference](https://developer.mozilla.org/docs/Web/API/Event/srcElement) | \- | `CustomEvent.srcElement` |
| `target` | `readonly` | `EventTarget` | Returns the object to which event is dispatched (its target). [MDN Reference](https://developer.mozilla.org/docs/Web/API/Event/target) | \- | `CustomEvent.target` |
| `timeStamp` | `readonly` | `number` | Returns the event’s timestamp as the number of milliseconds measured relative to the time origin. [MDN Reference](https://developer.mozilla.org/docs/Web/API/Event/timeStamp) | \- | `CustomEvent.timeStamp` |
| `NONE` | `readonly` | `0` | \- | \- | `CustomEvent.NONE` |
| `CAPTURING_PHASE` | `readonly` | `1` | \- | \- | `CustomEvent.CAPTURING_PHASE` |
| `AT_TARGET` | `readonly` | `2` | \- | \- | `CustomEvent.AT_TARGET` |
| `BUBBLING_PHASE` | `readonly` | `3` | \- | \- | `CustomEvent.BUBBLING_PHASE` |

---



[Source](https:/img.ly/docs/cesdk/sveltekit/api/engine/interfaces/readonlyreactiveproperty)