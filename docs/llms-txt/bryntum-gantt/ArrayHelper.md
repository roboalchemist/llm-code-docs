# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/helper/ArrayHelper.md

# [ArrayHelper](https://bryntum.com/docs/gantt/api/Core/helper/ArrayHelper)

Helper with useful functions for handling Arrays

## Functions

Functions are methods available for calling on the class

[from](https://bryntum.com/docs/gantt/api/Core/helper/ArrayHelper#function-from-static)
Similar to [`Array.from()`](https://bryntum.com/docs/gantt/api/https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/from) this method creates an array from an `iterable` object. Where `Array.from()` accepts a mapper function as the second argument, this method accepts a `filter` function as its second argument. If a mapper function is also needed, it can be passed as the third argument. Unlike `Array.from()`, if this method is passed `null`, it will return an empty array.

[remove](https://bryntum.com/docs/gantt/api/Core/helper/ArrayHelper#function-remove-static)
Remove one or more items from an array

[findInsertionIndex](https://bryntum.com/docs/gantt/api/Core/helper/ArrayHelper#function-findInsertionIndex-static)
Calculates the insertion index of a passed object into the passed Array according to the passed comparator function. Note that the passed Array _MUST_ already be ordered.

[findLast](https://bryntum.com/docs/gantt/api/Core/helper/ArrayHelper#function-findLast-static)
Similar to the native `Array.find()` call, but this finds the _last_ element in the array for which the passed function returns a truthy value.

[binarySearch](https://bryntum.com/docs/gantt/api/Core/helper/ArrayHelper#function-binarySearch-static)
This method returns the index that a given item would be inserted into the given (sorted) `array`. Note that the given `item` may or may not be in the array. This method will return the index of where the item _should_ be.

For example:

```
 var array = [ 'A', 'D', 'G', 'K', 'O', 'R', 'X' ];
 var index = ArrayHelper.binarySearch(array, 'E');

 console.log('index: ' + index);
 // logs "index: 2"

 array.splice(index, 0, 'E');

 console.log('array : ' + array.join(''));
 // logs "array: ADEGKORX"
```

[fill](https://bryntum.com/docs/gantt/api/Core/helper/ArrayHelper#function-fill-static)
Similar to Array.prototype.fill(), but constructs a new array with the specified item count and fills it with clones of the supplied item.

[populate](https://bryntum.com/docs/gantt/api/Core/helper/ArrayHelper#function-populate-static)
Populates an array with the return value from `fn`.

[include](https://bryntum.com/docs/gantt/api/Core/helper/ArrayHelper#function-include-static)
Pushes `item` on to the `array` if not already included

[unique](https://bryntum.com/docs/gantt/api/Core/helper/ArrayHelper#function-unique-static)
Returns a new array with the unique items from the supplied array.

[countUnique](https://bryntum.com/docs/gantt/api/Core/helper/ArrayHelper#function-countUnique-static)
Returns an array of unique values and their occurrence count, in { value, count } format

[asArray](https://bryntum.com/docs/gantt/api/Core/helper/ArrayHelper#function-asArray-static)
Returns the passed object wrapped in an array. Special handling of the following cases:

* Passing an array returns it as is
* Passing a `Set` returns it converted to an Array
* Passing `null`/`undefined` returns the passed value

```
const records = ArrayHelper.asArray(record);

// { id : 1 } -> [{ id : 1 }]
// [{ id : 1 }] -> [{ id : 1 }]
```

[identity](https://bryntum.com/docs/gantt/api/Core/helper/ArrayHelper#function-identity-static)
Identity function that returns its input.

[keyBy](https://bryntum.com/docs/gantt/api/Core/helper/ArrayHelper#function-keyBy-static)
Transform an array into a key:value dictionary using the specified key and value getters. Does not group values, so only one result will appear in the output for a given key.

```
const input = [{
    id: '1',
    other: 'one'
},{
    id: '2',
    other: 'two'
}];

keyBy(input, rec => rec.id)

// {
//    '1': { id: '1', other: 'one' },
//    '2': { id: '2', other: 'two' }
// }
```

[aggregate](https://bryntum.com/docs/gantt/api/Core/helper/ArrayHelper#function-aggregate-static)
Combines provided arrays of by aggregating their element values. For example the below code sums up numeric elements of the arrays:

```
ArrayHelper.aggregate(
    [
        [0,   1,  2, 33]
        [10,  1, -1],
        [100, 1, -1]
    ],
    entry => entry || 0, // "|| 0" here to make it work for different array sizes
    (aggregated, entry) => aggregated + entry, // aggregate by summing up
    () => 0 //initial value is zero
);

// returns [111, 3, 0, 33] array
```

[groupBy](https://bryntum.com/docs/gantt/api/Core/helper/ArrayHelper#function-groupBy-static)
Group an array by keys (either the values in a specified property name, or the results of a string-generating function accepting an array entry as input), returning an Object with those keys, whose values are arrays containing the array entries that produced that key.

```
const input = [{
    id: 1,
    color: 'red'
},{
    id: 2,
    color: 'green'
},{
    id: 3,
    color: 'green'
}];

groupBy(input, 'color')

// {
//    'red': [ { id: '1', color: 'red' } ],
//    'green': [ { id: '2', color: 'green' }, { id: '3', color: 'green' } ]
// }

groupBy(input, rec => rec.color?.substr(0, 1))

// {
//    'r': [ { id: '1', color: 'red' } ],
//    'g': [ { id: '2', color: 'green' }, { id: '3', color: 'green' } ]
// }
```

[groupByIndexed](https://bryntum.com/docs/gantt/api/Core/helper/ArrayHelper#function-groupByIndexed-static)

[chunkedInsert](https://bryntum.com/docs/gantt/api/Core/helper/ArrayHelper#function-chunkedInsert-static)
Splice items into an array in chunks, to avoid exceeding the maximum call stack size

[chunkedPush](https://bryntum.com/docs/gantt/api/Core/helper/ArrayHelper#function-chunkedPush-static)
Push items into an array, avoiding exceeding the maximum call stack size.
