# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/mixin/Identifiable.md

# [Identifiable](https://bryntum.com/docs/gantt/api/Core/mixin/Identifiable)

A mixin which provides identifier services such as auto-creation of `id`s and registration and lookup of instances by `id`.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[id](https://bryntum.com/docs/gantt/api/Core/mixin/Identifiable#config-id)
The id of this object. If not specified one will be generated. Also used for lookups through the static `getById` of the class which mixes this in. An example being [Widget](https://bryntum.com/docs/gantt/api/#Core/widget/Widget).

For a [Widget](https://bryntum.com/docs/gantt/api/#Core/widget/Widget), this is assigned as the `id` of the DOM [element](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-element) and must be unique across all elements in the page's `document`.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isIdentifiable](https://bryntum.com/docs/gantt/api/Core/mixin/Identifiable#property-isIdentifiable)
Identifies an object as an instance of [Identifiable](https://bryntum.com/docs/gantt/api/#Core/mixin/Identifiable) class, or subclass thereof.

[isIdentifiable](https://bryntum.com/docs/gantt/api/Core/mixin/Identifiable#property-isIdentifiable-static)
Identifies an object as an instance of [Identifiable](https://bryntum.com/docs/gantt/api/#Core/mixin/Identifiable) class, or subclass thereof.

## Functions

Functions are methods available for calling on the class

[generateAutoId](https://bryntum.com/docs/gantt/api/Core/mixin/Identifiable#function-generateAutoId)
This method generates an id for this instance.

[generateId](https://bryntum.com/docs/gantt/api/Core/mixin/Identifiable#function-generateId-static)
Generate a new id, using an internal counter and a prefix.

[unregisterInstance](https://bryntum.com/docs/gantt/api/Core/mixin/Identifiable#function-unregisterInstance-static)
Unregister Identifiable instance, normally done on destruction
