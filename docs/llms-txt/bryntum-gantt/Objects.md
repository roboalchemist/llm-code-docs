# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/helper/util/Objects.md

# [Objects](https://bryntum.com/docs/gantt/api/Core/helper/util/Objects)

Helper for low-level Object manipulation.

While documented on [ObjectHelper](https://bryntum.com/docs/gantt/api/#Core/helper/ObjectHelper), the following static methods are implemented by this class:

* `[assign](https://bryntum.com/docs/gantt/api/#Core/helper/ObjectHelper#function-assign-static)`
* `[assignIf](https://bryntum.com/docs/gantt/api/#Core/helper/ObjectHelper#function-assignIf-static)`
* `[clone](https://bryntum.com/docs/gantt/api/#Core/helper/ObjectHelper#function-clone-static)`
* `[createTruthyKeys](https://bryntum.com/docs/gantt/api/#Core/helper/ObjectHelper#function-createTruthyKeys-static)`
* `[getPath](https://bryntum.com/docs/gantt/api/#Core/helper/ObjectHelper#function-getPath-static)`
* `[getTruthyKeys](https://bryntum.com/docs/gantt/api/#Core/helper/ObjectHelper#function-getTruthyKeys-static)`
* `[getTruthyValues](https://bryntum.com/docs/gantt/api/#Core/helper/ObjectHelper#function-getTruthyValues-static)`
* `[isEmpty](https://bryntum.com/docs/gantt/api/#Core/helper/ObjectHelper#function-isEmpty-static)`
* `[isObject](https://bryntum.com/docs/gantt/api/#Core/helper/ObjectHelper#function-isObject-static)`
* `[merge](https://bryntum.com/docs/gantt/api/#Core/helper/ObjectHelper#function-merge-static)`
* `[setPath](https://bryntum.com/docs/gantt/api/#Core/helper/ObjectHelper#function-setPath-static)`
* `[typeOf](https://bryntum.com/docs/gantt/api/#Core/helper/ObjectHelper#function-typeOf-static)`

## Functions

Functions are methods available for calling on the class

[getPath](https://bryntum.com/docs/gantt/api/Core/helper/util/Objects#function-getPath-static)
Returns value for a given path in the object

[getPathDefault](https://bryntum.com/docs/gantt/api/Core/helper/util/Objects#function-getPathDefault-static)
Returns value for a given path in the object, placing a passed default value in at the leaf property and filling in undefined properties all the way down.

[getPropertyDescriptor](https://bryntum.com/docs/gantt/api/Core/helper/util/Objects#function-getPropertyDescriptor-static)
Finds a property descriptor for the passed object from all inheritance levels.

[hasPath](https://bryntum.com/docs/gantt/api/Core/helper/util/Objects#function-hasPath-static)
Determines if the specified path exists

[isPromise](https://bryntum.com/docs/gantt/api/Core/helper/util/Objects#function-isPromise-static)
Check if passed object is a Promise or contains `then` method. Used to fix problems with detecting promises in code with `instance of Promise` when Promise class is replaced with any other implementation like `ZoneAwarePromise` in Angular. Related to these issues: https://github.com/bryntum/support/issues/791 https://github.com/bryntum/support/issues/2990

[mergeItems](https://bryntum.com/docs/gantt/api/Core/helper/util/Objects#function-mergeItems-static)
Merges two "items" objects. An items object is a simple object whose keys act as identifiers and whose values are "item" objects. An item can be any object type. This method is used to merge such objects while maintaining their property order. Special key syntax is used to allow a source object to insert a key before or after a key in the `dest` object.

For example:

```
 let dest = {
     foo : {},
     bar : {},
     fiz : {}
 }

 console.log(Object.keys(dest));
 > ["foo", "bar", "fiz"]

 dest = mergeItems(dest, {
     'zip > bar' : {}    // insert "zip" before "bar"
     'bar < zap' : {}    // insert "zap" after "bar"
 });

 console.log(Object.keys(dest));
 > ["foo", "zip", "bar", "zap", "fiz"]
```

[setPath](https://bryntum.com/docs/gantt/api/Core/helper/util/Objects#function-setPath-static)
Sets value for a given path in the object

[filterTreeToArray](https://bryntum.com/docs/gantt/api/Core/helper/util/Objects#function-filterTreeToArray-static)
Traverses a tree (or array of trees), collects nodes that match a filter function into a flat array, and recursively visits child nodes of expanded nodes.
