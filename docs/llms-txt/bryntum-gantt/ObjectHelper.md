# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/helper/ObjectHelper.md

# [ObjectHelper](https://bryntum.com/docs/gantt/api/Core/helper/ObjectHelper)

Helper for Object manipulation.

## Functions

Functions are methods available for calling on the class

[assign](https://bryntum.com/docs/gantt/api/Core/helper/ObjectHelper#function-assign-static)
Copies all enumerable properties from the supplied source objects to `dest`. Unlike `Object.assign`, this copy also includes inherited properties.

[assignIf](https://bryntum.com/docs/gantt/api/Core/helper/ObjectHelper#function-assignIf-static)
Copies all enumerable properties from the supplied source objects to `dest`, only including properties that does not already exist on `dest`. Unlike `Object.assign`, this copy also includes inherited properties.

[clone](https://bryntum.com/docs/gantt/api/Core/helper/ObjectHelper#function-clone-static)
Creates a deep copy of the `value`. Simple objects ([isObject](https://bryntum.com/docs/gantt/api/#Core/helper/ObjectHelper#function-isObject-static), arrays and `Date` objects are cloned. The enumerable properties of simple objects and the elements of arrays are cloned recursively.

[createTruthyKeys](https://bryntum.com/docs/gantt/api/Core/helper/ObjectHelper#function-createTruthyKeys-static)
Converts a list of names (either a space separated string or an array), into an object with those properties assigned truthy values. The converse of [getTruthyKeys](https://bryntum.com/docs/gantt/api/#Core/helper/ObjectHelper#function-getTruthyKeys-static).

[getTruthyKeys](https://bryntum.com/docs/gantt/api/Core/helper/ObjectHelper#function-getTruthyKeys-static)
Gathers the names of properties which have truthy values into an array.

This is useful when gathering CSS class names for complex element production. Instead of appending to an array or string which may already contain the name, and instead of contending with space separation and concatenation and conditional execution, just set the properties of an object:

```
cls = {
    [this.selectedCls] : this.isSelected(thing),
    [this.dirtyCls] : this.isDirty(thing)
};
```

If the `source` parameter is an array, it is returned. If it is a single string, it is wrapped in an array and returned. Otherwise, the value must be an object (or null) it will be processed as described above.

[getTruthyValues](https://bryntum.com/docs/gantt/api/Core/helper/ObjectHelper#function-getTruthyValues-static)
Gathers the values of properties which are truthy into an array.

[isEmpty](https://bryntum.com/docs/gantt/api/Core/helper/ObjectHelper#function-isEmpty-static)
Tests whether a passed object has any enumerable properties.

[isObject](https://bryntum.com/docs/gantt/api/Core/helper/ObjectHelper#function-isObject-static)
Returns `true` if the `value` is a simple `Object`.

[merge](https://bryntum.com/docs/gantt/api/Core/helper/ObjectHelper#function-merge-static)
Copies all enumerable properties from the supplied source objects to `dest`, recursing when the properties of both the source and `dest` are objects.

```
 const o = {
     a : 1,
     b : {
         c : 2
     }
 };
 const o2 = {
     b : {
         d : 3
     }
 }

 console.log(merge(o, o2));

 > { a : 1, b : { c : 2, d : 3 } }
```

[typeOf](https://bryntum.com/docs/gantt/api/Core/helper/ObjectHelper#function-typeOf-static)
Returns the specific type of the given `value`. Unlike the `typeof` operator, this function returns the text from the `Object.prototype.toString` result allowing `Date`, `Array`, `RegExp`, and others to be differentiated.

```
 console.log(typeOf(null));
 > null

 console.log(typeOf({}));
 > object

 console.log(typeOf([]));
 > array

 console.log(typeOf(new Date()));
 > date

 console.log(typeOf(NaN));
 > nan

 console.log(typeOf(/a/));
 > regexp
```

[getPath](https://bryntum.com/docs/gantt/api/Core/helper/ObjectHelper#function-getPath-static)
Returns value for a given path in the object

[setPath](https://bryntum.com/docs/gantt/api/Core/helper/ObjectHelper#function-setPath-static)
Sets value for a given path in the object

[observeObject](https://bryntum.com/docs/gantt/api/Core/helper/ObjectHelper#function-observeObject-static)
Recursively wraps an object and all nested objects in Proxy instances. Invokes a callback whenever any property is mutated (set or deleted) at any depth.

This is useful for observing changes in complex objects, such as configuration objects, where you want to track changes to any property, no matter how deeply nested.

It is advisable to debounce the `onChange` callback to avoid performance issues with frequent updates.

[filter](https://bryntum.com/docs/gantt/api/Core/helper/ObjectHelper#function-filter-static)
Returns an object retaining the enumerable key/value pairs for which the provided function `fn` returns a truthy value.

[forEach](https://bryntum.com/docs/gantt/api/Core/helper/ObjectHelper#function-forEach-static)
Calls a provided function `fn` for each key/value pair of a given `object`.

[transformArrayToNamedObject](https://bryntum.com/docs/gantt/api/Core/helper/ObjectHelper#function-transformArrayToNamedObject-static)
Creates a new object where key is a property in array item (`ref` by default) or index in the array and value is array item.

From:

```
[
    {
         text : 'foo',
         ref : 'fooItem'
    },
    {
         text : 'bar'
    }
]
```

To:

```
{
    fooItem : {
        text : 'foo',
        ref  : 'fooItem'
    },
    1 : {
        text : 'bar'
    }
}
```

[transformNamedObjectToArray](https://bryntum.com/docs/gantt/api/Core/helper/ObjectHelper#function-transformNamedObjectToArray-static)
Creates a new array from object values and saves key in a property (`ref` by default) of each item.

From:

```
{
    fooItem : {
        text : 'foo'
    },
    1 : {
        text : 'bar'
    },
    barItem : false // will be ignored
}
```

To:

```
[
    {
         text : 'foo',
         ref : 'fooItem'
    },
    {
         text : 'bar',
         ref : 1
    }
]
```

[isEqual](https://bryntum.com/docs/gantt/api/Core/helper/ObjectHelper#function-isEqual-static)
Checks if two values are equal. Basically === but special handling of dates.

[isDeeplyEqual](https://bryntum.com/docs/gantt/api/Core/helper/ObjectHelper#function-isDeeplyEqual-static)
Checks if two objects are deeply equal

[isPartial](https://bryntum.com/docs/gantt/api/Core/helper/ObjectHelper#function-isPartial-static)
Checks if value B is partially equal to value A.

[isLessThan](https://bryntum.com/docs/gantt/api/Core/helper/ObjectHelper#function-isLessThan-static)
Checks if value a is smaller than value b.

[isMoreThan](https://bryntum.com/docs/gantt/api/Core/helper/ObjectHelper#function-isMoreThan-static)
Checks if value a is bigger than value b.

[first](https://bryntum.com/docs/gantt/api/Core/helper/ObjectHelper#function-first-static)
If `value` is iterable (`for-of` loopable), this method returns the first element of the iterable sequence. If `value` is async-iterable (i.e., uses a `for await of` loop), this method returns a `Promise` that will resolve to the first element. Otherwise, this method returns the first key/value pair (a 2-element array) using a `for-in` loop.

[fork](https://bryntum.com/docs/gantt/api/Core/helper/ObjectHelper#function-fork-static)
Used by the Base class to make deep copies of defaultConfig blocks

[copyProperties](https://bryntum.com/docs/gantt/api/Core/helper/ObjectHelper#function-copyProperties-static)
Copies the named properties from the `source` parameter into the `dest` parameter.

[copyPropertiesIf](https://bryntum.com/docs/gantt/api/Core/helper/ObjectHelper#function-copyPropertiesIf-static)
Copies the named properties from the `source` parameter into the `dest` parameter unless the property already exists in the `dest`.

[copyPropertiesExcept](https://bryntum.com/docs/gantt/api/Core/helper/ObjectHelper#function-copyPropertiesExcept-static)
Copies all properties from the `source` parameter into the `dest` parameter except those specified in `except`.

[entries](https://bryntum.com/docs/gantt/api/Core/helper/ObjectHelper#function-entries-static)
Returns an array containing the keys and values of all enumerable properties from every prototype level for the object. If `object` is `null`, this method returns an empty array.

[fromEntries](https://bryntum.com/docs/gantt/api/Core/helper/ObjectHelper#function-fromEntries-static)
Populates an `object` with the provided `entries`.

[keys](https://bryntum.com/docs/gantt/api/Core/helper/ObjectHelper#function-keys-static)
Returns an array containing all enumerable property names from every prototype level for the object. If `object` is `null`, this method returns an empty array.

[values](https://bryntum.com/docs/gantt/api/Core/helper/ObjectHelper#function-values-static)
Returns an array containing the values of all enumerable properties from every prototype level for the object. If `object` is `null`, this method returns an empty array.

[pathExists](https://bryntum.com/docs/gantt/api/Core/helper/ObjectHelper#function-pathExists-static)
Checks if a given path exists in an object

[pathifyKeys](https://bryntum.com/docs/gantt/api/Core/helper/ObjectHelper#function-pathifyKeys-static)
Creates a simple single level key-value object from complex deep object.

[deletePath](https://bryntum.com/docs/gantt/api/Core/helper/ObjectHelper#function-deletePath-static)
Removes value for a given path in the object. Doesn't cleanup empty objects.

[hookProperty](https://bryntum.com/docs/gantt/api/Core/helper/ObjectHelper#function-hookProperty-static)
Intercepts access to a `property` of a given `object`.

```
     ObjectHelper.hookProperty(object, 'prop', class {
         get value() {
             return super.value;
         }
         set value(v) {
             super.value = v;
         }
     });
```

The use of `super` allows the hook's getter and setter to invoke the object's existing get/set.

[cleanupProperties](https://bryntum.com/docs/gantt/api/Core/helper/ObjectHelper#function-cleanupProperties-static)
Changes the passed object and removes all null and undefined properties from it

[removeAllProperties](https://bryntum.com/docs/gantt/api/Core/helper/ObjectHelper#function-removeAllProperties-static)
Changes the passed object and removes all properties from it. Used while mutating when need to keep reference to the object but replace its properties.

[assertType](https://bryntum.com/docs/gantt/api/Core/helper/ObjectHelper#function-assertType-static)
Checks that the supplied value is of the specified type.Throws if it is not

[assertObject](https://bryntum.com/docs/gantt/api/Core/helper/ObjectHelper#function-assertObject-static)
Checks that the supplied value is a plain object. Throws if it is not

[assertInstance](https://bryntum.com/docs/gantt/api/Core/helper/ObjectHelper#function-assertInstance-static)
Checks that the supplied value is an instance of a Bryntum class. Throws if it is not

[assertClass](https://bryntum.com/docs/gantt/api/Core/helper/ObjectHelper#function-assertClass-static)
Checks that the supplied value is a Bryntum class. Throws if it is not

[assertFunction](https://bryntum.com/docs/gantt/api/Core/helper/ObjectHelper#function-assertFunction-static)
Checks that the supplied value is a function. Throws if it is not

[assertNumber](https://bryntum.com/docs/gantt/api/Core/helper/ObjectHelper#function-assertNumber-static)
Checks that the supplied value is a number. Throws if it is not

[assertBoolean](https://bryntum.com/docs/gantt/api/Core/helper/ObjectHelper#function-assertBoolean-static)
Checks that the supplied value is a boolean. Throws if it is not

[assertString](https://bryntum.com/docs/gantt/api/Core/helper/ObjectHelper#function-assertString-static)
Checks that the supplied value is a string. Throws if it is not

[assertArray](https://bryntum.com/docs/gantt/api/Core/helper/ObjectHelper#function-assertArray-static)
Checks that the supplied value is an array. Throws if it is not

[toFixed](https://bryntum.com/docs/gantt/api/Core/helper/ObjectHelper#function-toFixed-static)
Number.toFixed(), with polyfill for browsers that needs it

[roundTo](https://bryntum.com/docs/gantt/api/Core/helper/ObjectHelper#function-roundTo-static)
Round the passed number to closest passed step value.

[round](https://bryntum.com/docs/gantt/api/Core/helper/ObjectHelper#function-round-static)
Round the passed number to the passed number of decimals.

[getMapPath](https://bryntum.com/docs/gantt/api/Core/helper/ObjectHelper#function-getMapPath-static)
Returns a non-null entry from a Map for a given key path. This enables a specified defaultValue to be added "just in time" which is returned if the key is not already present.
