# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/util/Animator.md

# [Animator](https://bryntum.com/docs/gantt/api/Core/util/Animator)

Manages one or more [style transitions](https://bryntum.com/docs/gantt/api/#Core/util/Animator#typedef-AnimatorTransition) or other `Animator` instances. Unlike typical config objects, the config object for this class is a mixture of config properties and style names that define [style transitions](https://bryntum.com/docs/gantt/api/#Core/util/Animator#typedef-AnimatorTransition).

For example:

```
 const anim = Animator.run({
     element,
     duration : 500,

     // style transitions:
     opacity : 0
 });

 await anim.done();
```

The static [run](https://bryntum.com/docs/gantt/api/#Core/util/Animator#function-run-static) method is typically used (as above) instead of the `new Animator()` style for brevity (since a manually created `Animator` must also be manually [started](https://bryntum.com/docs/gantt/api/#Core/util/Animator#function-start)).

An `Animator` can be [awaited](https://bryntum.com/docs/gantt/api/#Core/util/Animator#function-done) and will resolve once all of its transitions and/or child animations complete or are aborted (via `destroy()`).

Compound Transitions
--------------------

The following custom transitions can present in the `Animator` config object as if they were normal style transitions:

* [puff](https://bryntum.com/docs/gantt/api/#Core/util/Animator#function-puff-static)

For example:

```
 const anim = Animator.run({
     element,
     marginLeft : -200,
     puff       : true   // true for default scale, a number, or config object
 });
```

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[delay](https://bryntum.com/docs/gantt/api/Core/util/Animator#config-delay)
The optional delay before starting the animation. Numbers less than 10 are assumed to be seconds (instead of milliseconds) unless the `unit` property is specified.

[duration](https://bryntum.com/docs/gantt/api/Core/util/Animator#config-duration)
The duration of the animation. Numbers less than 10 are assumed to be seconds (instead of milliseconds) unless the `unit` property is specified.

[element](https://bryntum.com/docs/gantt/api/Core/util/Animator#config-element)
The element to animate.

[finalize](https://bryntum.com/docs/gantt/api/Core/util/Animator#config-finalize)
A callback function called when the animation completes. This is called after restoring styles to the original values (based on [retain](https://bryntum.com/docs/gantt/api/#Core/util/Animator#config-retain)). When this function is provided, `retain` defaults to `false`. By implementing this function, a CSS class can be applied to the [element](https://bryntum.com/docs/gantt/api/#Core/util/Animator#config-element) to give the proper style, while the inline styles are removed (e.g., a hide animation based on opacity).

For example:

```
 const anim = Animator.run({
     element,
     duration : 500,
     opacity  : 0,

     finalize() {
         element.classList.add('hidden');
     }
 });

 await anim.done();
```

[prefinalize](https://bryntum.com/docs/gantt/api/Core/util/Animator#config-prefinalize)
A callback function called when the animation completes. This is called prior to restoring styles to the original values (based on [retain](https://bryntum.com/docs/gantt/api/#Core/util/Animator#config-retain)).

[retain](https://bryntum.com/docs/gantt/api/Core/util/Animator#config-retain)
Set to `true` to retain the style property values after the animation. This defaults to `true` if a [finalize](https://bryntum.com/docs/gantt/api/#Core/util/Animator#config-finalize) function is not specified, and `false` otherwise. When a `finalize` function is provided, it is typically to apply a CSS class to achieve the desired styling so that inline styles can be removed.

[timing](https://bryntum.com/docs/gantt/api/Core/util/Animator#config-timing)
The [timing function](https://bryntum.com/docs/gantt/api/https://developer.mozilla.org/en-US/docs/Web/CSS/transition-timing-function) for the animation.

[unit](https://bryntum.com/docs/gantt/api/Core/util/Animator#config-unit)
The duration/delay unit (either `'s'` or `'ms'`).

[items](https://bryntum.com/docs/gantt/api/Core/util/Animator#config-items)
When passed at construction time, `items` can be an array of other `Animator` config objects. This can be used to animate multiple elements and wait for this instance to be [done](https://bryntum.com/docs/gantt/api/#Core/util/Animator#function-done).

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isAnimator](https://bryntum.com/docs/gantt/api/Core/util/Animator#property-isAnimator)
Identifies an object as an instance of [Animator](https://bryntum.com/docs/gantt/api/#Core/util/Animator) class, or subclass thereof.

[isAnimator](https://bryntum.com/docs/gantt/api/Core/util/Animator#property-isAnimator-static)
Identifies an object as an instance of [Animator](https://bryntum.com/docs/gantt/api/#Core/util/Animator) class, or subclass thereof.

[completed](https://bryntum.com/docs/gantt/api/Core/util/Animator#property-completed)
This readonly property is set to `true` when the animation completes or `false` if the animation is aborted (by calling the `destroy()` method).

[items](https://bryntum.com/docs/gantt/api/Core/util/Animator#property-items)
An array containing a mixture of `Animator` and/or `AnimatorTransition` objects, depending on what was specified at construction time.

## Functions

Functions are methods available for calling on the class

[run](https://bryntum.com/docs/gantt/api/Core/util/Animator#function-run-static)
A short-hand way to create an `Animator` instance and call its [start](https://bryntum.com/docs/gantt/api/#Core/util/Animator#function-start) method.

```
 const anim = Animator.run({
     element,
     duration : 500,

     // style transitions:
     opacity : 0
 });

 await anim.done();
```

[done](https://bryntum.com/docs/gantt/api/Core/util/Animator#function-done)
Returns a `Promise` that resolves to a `Boolean` when this animation completes. The resolved value is that of this instance's [completed](https://bryntum.com/docs/gantt/api/#Core/util/Animator#property-completed) property.

[start](https://bryntum.com/docs/gantt/api/Core/util/Animator#function-start)
Starts this animation and returns a reference to itself. This method is called automatically by the [run](https://bryntum.com/docs/gantt/api/#Core/util/Animator#function-run-static) method.

[puff](https://bryntum.com/docs/gantt/api/Core/util/Animator#function-puff-static)
A compound animation to achieve `scale: 12` and `opacity: 0`. The `scale` defaults to 8 but can be set in the `anim` config object.

For example

```
 const puff = Animator.puff(element);

 const puff = Animator.puff({
     element,
     scale : 12
 });
```

This compound animation can also be specified in an `Animator` config object along with other style transitions:

```
 const anim = Animator.run({
     element,
     marginLeft : -200,
     puff       : true   // true for default scale, a number, or config object
 });
```

## Typedefs

Typedefs are type definitions for the class

[AnimatorTransition](https://bryntum.com/docs/gantt/api/Core/util/Animator#typedef-AnimatorTransition)
These objects are passed as values in the config object of an `Animator`. The `property` name is the key in the config object.

For example:

```
 const anim = Animator.run({
     element,
     opacity : {
         // AnimatorTransition properties
     }
 });
```

The [anim.items](https://bryntum.com/docs/gantt/api/#Core/util/Animator#config-items) array will contain a single `AnimatorTransition` instance.
