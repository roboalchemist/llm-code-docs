# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/helper/util/Gesture.md

# [Gesture](https://bryntum.com/docs/gantt/api/Core/helper/util/Gesture)

Abstract base class for gesture recognizers.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[durationLimit](https://bryntum.com/docs/gantt/api/Core/helper/util/Gesture#config-durationLimit)
The time limit (in milliseconds) for a gesture to be recognized measured from the initial `pointerdown` event.

See the [elapsedTime](https://bryntum.com/docs/gantt/api/#Core/helper/util/Gesture#property-elapsedTime) property.

[element](https://bryntum.com/docs/gantt/api/Core/helper/util/Gesture#config-element)
The target element for gesture recognition.

[handler](https://bryntum.com/docs/gantt/api/Core/helper/util/Gesture#config-handler)
The instance holding all the registered event handlers for the gesture.

[idleLimit](https://bryntum.com/docs/gantt/api/Core/helper/util/Gesture#config-idleLimit)
The time limit (in milliseconds) for a gesture to receive no events.

[recognition](https://bryntum.com/docs/gantt/api/Core/helper/util/Gesture#config-recognition)
The owing recognition context instance.

[state](https://bryntum.com/docs/gantt/api/Core/helper/util/Gesture#config-state)
The `state` is initially `null` but is set to `'active'` if the gesture is `recognized`. The `state` remains `'active'` until a `pointerup` or `pointercancel` event is received, when it will advance to either `'done'` or `'cancel'`, respectively.

[targetEvents](https://bryntum.com/docs/gantt/api/Core/helper/util/Gesture#config-targetEvents)
Additional element event listeners needed by derived classes. These listeners are register when recognition begins are automatically cleaned up when complete.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[state](https://bryntum.com/docs/gantt/api/Core/helper/util/Gesture#property-state)
The `state` is initially `null` but is set to `'active'` if the gesture is `recognized`. The `state` remains `'active'` until a `pointerup` or `pointercancel` event is received, when it will advance to either `'done'` or `'cancel'`, respectively.

[fires](https://bryntum.com/docs/gantt/api/Core/helper/util/Gesture#property-fires-static)
The array of gesture events fired by this class. Derived classes must indicate all of their gesture event names in this static property to allow the [`EventHelper.on`](https://bryntum.com/docs/gantt/api/#Core/helper/EventHelper#function-on-static) method to activate the appropriate derived class when a listener is registered for a gesture.

[gestureName](https://bryntum.com/docs/gantt/api/Core/helper/util/Gesture#property-gestureName-static)
Derived classes should set this static property to indicate the prefix for the three default gesture event names. For example, if `gestureName = 'swipe'`, this is the gesture fired at `pointerup` if the gesture were to be recognized. Further, `'swipeStart'` is fired (prior to `pointerup`) once the gesture has been recognized, and `'swipeCancel'` is fired if the recognized swipe gesture is cancelled. These default gesture events are only fired if they are included in the [fires](https://bryntum.com/docs/gantt/api/#Core/helper/util/Gesture#property-fires-static) array.

[registry](https://bryntum.com/docs/gantt/api/Core/helper/util/Gesture#property-registry)
An object whose keys are the registered gesture event names in their proper case and fully lowercase form. This object is populated via the [fires](https://bryntum.com/docs/gantt/api/#Core/helper/util/Gesture#property-fires-static) property of derived classes.

[touchPoints](https://bryntum.com/docs/gantt/api/Core/helper/util/Gesture#property-touchPoints-static)
Derived classes should set this static property to the number of pointers that define a possible gesture recognition. If there is not a single number of pointers appropriate for a gesture, this property should be ignored.

[elapsedTime](https://bryntum.com/docs/gantt/api/Core/helper/util/Gesture#property-elapsedTime)
Gets the number of milliseconds that have elapsed since the initial `pointerdown` event.

[recognized](https://bryntum.com/docs/gantt/api/Core/helper/util/Gesture#property-recognized)
Get/Set the recognition state for this gesture. The getter indicates whether this gesture has been recognized for the current pointerdown sequence.

This property can be set to `false` during recognition to indicate that this gesture should no longer be considered a candidate. Doing so will remove the gesture from the current recognition process and this gesture instance will `destroy()` itself.

This property is set to `true` when a gesture has been recognized. All other gestures in the set of candidates will be destroyed.

[pointers](https://bryntum.com/docs/gantt/api/Core/helper/util/Gesture#property-pointers)
Gets the current state of pointers.

## Functions

Functions are methods available for calling on the class

[begin](https://bryntum.com/docs/gantt/api/Core/helper/util/Gesture#function-begin-static)
This method is called when processing `pointerdown` to filter down to only the applicable gesture classes. If this method returns `true`, a Gesture instance is created for gesture recognition.

By default, this method returns `true` if the [touchPoints](https://bryntum.com/docs/gantt/api/#Core/helper/util/Gesture#property-touchPoints-static) static property is falsy or is equal to number of pointers that are down.

[is](https://bryntum.com/docs/gantt/api/Core/helper/util/Gesture#function-is-static)
Returns `true` if the given `eventName` is an event fired by a registered gesture (i.e., a Gesture class has declared it in its [fires](https://bryntum.com/docs/gantt/api/#Core/helper/util/Gesture#property-fires-static) property).

[on](https://bryntum.com/docs/gantt/api/Core/helper/util/Gesture#function-on-static)
This is the entry point from the [addElementListener](https://bryntum.com/docs/gantt/api/#Core/helper/EventHelper#function-addElementListener-static) method.

[un](https://bryntum.com/docs/gantt/api/Core/helper/util/Gesture#function-un-static)
This is the entry point from the [removeEventListener](https://bryntum.com/docs/gantt/api/#Core/helper/EventHelper#function-removeEventListener-static) method.

[beforeStart](https://bryntum.com/docs/gantt/api/Core/helper/util/Gesture#function-beforeStart)
This method is called (typically during `pointermove`) when a gesture is [recognized](https://bryntum.com/docs/gantt/api/#Core/helper/util/Gesture#property-recognized) but before its [state](https://bryntum.com/docs/gantt/api/#Core/helper/util/Gesture#property-state) property is set to `'active'`.

By default, this method fires the [`'before'+gestureName`](https://bryntum.com/docs/gantt/api/#Core/helper/util/Gesture#property-gestureName-static) gesture event (if it is present in the [fires](https://bryntum.com/docs/gantt/api/#Core/helper/util/Gesture#property-fires-static) array).

[cancel](https://bryntum.com/docs/gantt/api/Core/helper/util/Gesture#function-cancel)
This method is called at `pointercancel` for the [recognized](https://bryntum.com/docs/gantt/api/#Core/helper/util/Gesture#property-recognized) gesture. If [state](https://bryntum.com/docs/gantt/api/#Core/helper/util/Gesture#property-state) is `'active'`, this method will set it to `'cancel'`, which will call [onCancel](https://bryntum.com/docs/gantt/api/#Core/helper/util/Gesture#function-onCancel).

[end](https://bryntum.com/docs/gantt/api/Core/helper/util/Gesture#function-end)
This method is called at `pointerup` for the [recognized](https://bryntum.com/docs/gantt/api/#Core/helper/util/Gesture#property-recognized) gesture. If [state](https://bryntum.com/docs/gantt/api/#Core/helper/util/Gesture#property-state) is `'active'`, this method will set it to `'done'`, which will call [onEnd](https://bryntum.com/docs/gantt/api/#Core/helper/util/Gesture#function-onEnd).

[getDetails](https://bryntum.com/docs/gantt/api/Core/helper/util/Gesture#function-getDetails)
Returns an object with event properties to include on any fired event (see [trigger](https://bryntum.com/docs/gantt/api/#Core/helper/util/Gesture#function-trigger)).

[move](https://bryntum.com/docs/gantt/api/Core/helper/util/Gesture#function-move)
This method is called on `pointermove` for the [recognized](https://bryntum.com/docs/gantt/api/#Core/helper/util/Gesture#property-recognized) gesture. By default, this method calls [unrecognize](https://bryntum.com/docs/gantt/api/#Core/helper/util/Gesture#function-unrecognize) to determine if the movement invalidated the active gesture recognition.

[onBegin](https://bryntum.com/docs/gantt/api/Core/helper/util/Gesture#function-onBegin)
This method is called when gesture recognition begins (in response to `pointerdown`), prior to any motion of the pointer(s).

[onCancel](https://bryntum.com/docs/gantt/api/Core/helper/util/Gesture#function-onCancel)
This method is called (typically during `pointercancel`) for the [recognized](https://bryntum.com/docs/gantt/api/#Core/helper/util/Gesture#property-recognized) gesture when the [state](https://bryntum.com/docs/gantt/api/#Core/helper/util/Gesture#property-state) property is set to `'cancel'`.

By default, this method fires the [`gestureName+'Cancel'`](https://bryntum.com/docs/gantt/api/#Core/helper/util/Gesture#property-gestureName-static) gesture event (if it is present in the [fires](https://bryntum.com/docs/gantt/api/#Core/helper/util/Gesture#property-fires-static) array).

[onEnd](https://bryntum.com/docs/gantt/api/Core/helper/util/Gesture#function-onEnd)
This method is called (typically during `pointerup`) for the [recognized](https://bryntum.com/docs/gantt/api/#Core/helper/util/Gesture#property-recognized) gesture when the [state](https://bryntum.com/docs/gantt/api/#Core/helper/util/Gesture#property-state) property is set to `'done'`.

By default, this method fires the [gestureName](https://bryntum.com/docs/gantt/api/#Core/helper/util/Gesture#property-gestureName-static) gesture event (if it is present in the [fires](https://bryntum.com/docs/gantt/api/#Core/helper/util/Gesture#property-fires-static) array).

[onStart](https://bryntum.com/docs/gantt/api/Core/helper/util/Gesture#function-onStart)
This method is called (typically during `pointermove`) when a gesture becomes [recognized](https://bryntum.com/docs/gantt/api/#Core/helper/util/Gesture#property-recognized) and the [state](https://bryntum.com/docs/gantt/api/#Core/helper/util/Gesture#property-state) property is set to `'active'`.

By default, this method fires the [`gestureName+'Start'`](https://bryntum.com/docs/gantt/api/#Core/helper/util/Gesture#property-gestureName-static) gesture event (if it is present in the [fires](https://bryntum.com/docs/gantt/api/#Core/helper/util/Gesture#property-fires-static) array).

[recognize](https://bryntum.com/docs/gantt/api/Core/helper/util/Gesture#function-recognize)
Called for all gestures prior to recognition (during `pointermove`) to determine if this gesture is recognized.

If this method returns a boolean value, that value is used to set the [recognized](https://bryntum.com/docs/gantt/api/#Core/helper/util/Gesture#property-recognized) property. This method is also called by the default implementation of [unrecognize](https://bryntum.com/docs/gantt/api/#Core/helper/util/Gesture#function-unrecognize) method (by the [move](https://bryntum.com/docs/gantt/api/#Core/helper/util/Gesture#function-move) method). In this case, if this method returns `false`, [recognized](https://bryntum.com/docs/gantt/api/#Core/helper/util/Gesture#property-recognized) is set to `false`, cancelling the gesture recognition.

By default, this method only checks the [durationLimit](https://bryntum.com/docs/gantt/api/#Core/helper/util/Gesture#config-durationLimit) config.

[trigger](https://bryntum.com/docs/gantt/api/Core/helper/util/Gesture#function-trigger)
Helper method to fire events to the associated listeners. The [fires](https://bryntum.com/docs/gantt/api/#Core/helper/util/Gesture#property-fires-static) array is checked for the `eventName` (case-insensitively), and no event is fired if the `eventName` is not found.

[unrecognize](https://bryntum.com/docs/gantt/api/Core/helper/util/Gesture#function-unrecognize)
This method is called (by [move](https://bryntum.com/docs/gantt/api/#Core/helper/util/Gesture#function-move) for the [recognized](https://bryntum.com/docs/gantt/api/#Core/helper/util/Gesture#property-recognized) gesture) to determine if the gesture is no longer considered valid. If this method returns `true`, the [recognized](https://bryntum.com/docs/gantt/api/#Core/helper/util/Gesture#property-recognized) property is set to `false`, cancelling the gesture recognition.

The default implementation of this method calls [recognize](https://bryntum.com/docs/gantt/api/#Core/helper/util/Gesture#function-recognize) and returns `true` if `recognize` returns `false`.
