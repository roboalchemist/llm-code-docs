# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/util/ClickRepeater.md

# [ClickRepeater](https://bryntum.com/docs/gantt/api/Core/util/ClickRepeater)

A helper class, which, when applied to an [element](https://bryntum.com/docs/gantt/api/#Core/util/ClickRepeater#config-element) means that a mousedown and hold on that element will, after a configured [delay](https://bryntum.com/docs/gantt/api/#Core/util/ClickRepeater#config-delay), begin autorepeating `click` events on that element, starting at a rate of [startRate](https://bryntum.com/docs/gantt/api/#Core/util/ClickRepeater#config-startRate) clicks per second, and over [accelerateDuration](https://bryntum.com/docs/gantt/api/#Core/util/ClickRepeater#config-accelerateDuration) milliseconds, accelerate to firing clicks at [endRate](https://bryntum.com/docs/gantt/api/#Core/util/ClickRepeater#config-endRate) times per second.

An example of this is used by the [NumberField](https://bryntum.com/docs/gantt/api/#Core/widget/NumberField)'s spinner triggers.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[element](https://bryntum.com/docs/gantt/api/Core/util/ClickRepeater#config-element)
The element on which to fire autorepeating `click` events when the mouse is held down.

[delegate](https://bryntum.com/docs/gantt/api/Core/util/ClickRepeater#config-delegate)
A query selector which specifies subtargets of this ClickRepeater's [element](https://bryntum.com/docs/gantt/api/#Core/util/ClickRepeater#config-element) which act as the click auto repeat event targets.

[delay](https://bryntum.com/docs/gantt/api/Core/util/ClickRepeater#config-delay)
How long in milliSeconds to pause before starting the click repeats.

[startRate](https://bryntum.com/docs/gantt/api/Core/util/ClickRepeater#config-startRate)
Clicks per second to start firing after the initial [delay](https://bryntum.com/docs/gantt/api/#Core/util/ClickRepeater#config-delay)

[endRate](https://bryntum.com/docs/gantt/api/Core/util/ClickRepeater#config-endRate)
Clicks per second to fire at top speed, after accelerating over the [accelerateDuration](https://bryntum.com/docs/gantt/api/#Core/util/ClickRepeater#config-accelerateDuration)

[accelerateDuration](https://bryntum.com/docs/gantt/api/Core/util/ClickRepeater#config-accelerateDuration)
How long in milliseconds to accelerate from the [startRate](https://bryntum.com/docs/gantt/api/#Core/util/ClickRepeater#config-startRate) to the [startRate](https://bryntum.com/docs/gantt/api/#Core/util/ClickRepeater#config-startRate).
