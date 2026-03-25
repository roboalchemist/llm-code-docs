# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/util/ElementVisitor.md

# [ElementVisitor](https://bryntum.com/docs/gantt/api/Core/util/ElementVisitor)

A utility class for visiting elements in the DOM tree.

It is recommended to use the static [getVisitor](https://bryntum.com/docs/gantt/api/#Core/util/ElementVisitor#function-getVisitor-static) method to obtain instances of this class because they are cached and reused based on the element and selector.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[element](https://bryntum.com/docs/gantt/api/Core/util/ElementVisitor#config-element)
The element to visit.

[selector](https://bryntum.com/docs/gantt/api/Core/util/ElementVisitor#config-selector)
The selector to use when visiting the element or a function which may accept of reject candidate nodes by returning

* NodeFilter.FILTER\_ACCEPT
* NodeFilter.FILTER\_REJECT
* NodeFilter.FILTER\_SKIP

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isElementVisitor](https://bryntum.com/docs/gantt/api/Core/util/ElementVisitor#property-isElementVisitor)
Identifies an object as an instance of [ElementVisitor](https://bryntum.com/docs/gantt/api/#Core/util/ElementVisitor) class, or subclass thereof.

[isElementVisitor](https://bryntum.com/docs/gantt/api/Core/util/ElementVisitor#property-isElementVisitor-static)
Identifies an object as an instance of [ElementVisitor](https://bryntum.com/docs/gantt/api/#Core/util/ElementVisitor) class, or subclass thereof.

## Functions

Functions are methods available for calling on the class

[getVisitor](https://bryntum.com/docs/gantt/api/Core/util/ElementVisitor#function-getVisitor-static)
Returns an ElementVisitor instance for the given element and selector.

This is the recommended way to get an ElementVisitor instance as it will reuse instances.

[first](https://bryntum.com/docs/gantt/api/Core/util/ElementVisitor#function-first)
Returns the first element in the tree that matches the selector.

[previous](https://bryntum.com/docs/gantt/api/Core/util/ElementVisitor#function-previous)
Returns the previous element in the tree that matches the selector.

[next](https://bryntum.com/docs/gantt/api/Core/util/ElementVisitor#function-next)
Returns the next element in the tree that matches the selector.

[last](https://bryntum.com/docs/gantt/api/Core/util/ElementVisitor#function-last)
Returns the last element in the tree that matches the selector.
