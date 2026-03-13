# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/helper/util/DomClassList.md

# [DomClassList](https://bryntum.com/docs/gantt/api/Core/helper/util/DomClassList)

This class encapsulates a list of CSS classes which can be set as the `className` on an `HTMLElement`.

Properties names set on this class equate to _adding_ a class if the property's value is _truthy_, or removing a class if the value is _falsy_.

```
const myClassList = new DomClassList('b-test-button');

myClassList.add('test-class');
myClassList.important = 1;

myHtmlElement.className = myClassList; // Sets it to "b-test-button test-class important"
```

## Properties

Properties are getters/setters or publicly accessible variables on this class

[value](https://bryntum.com/docs/gantt/api/Core/helper/util/DomClassList#property-value)
Get/set string value. Class names separated with space.

[values](https://bryntum.com/docs/gantt/api/Core/helper/util/DomClassList#property-values)
Returns string values as an array.

## Functions

Functions are methods available for calling on the class

[normalize](https://bryntum.com/docs/gantt/api/Core/helper/util/DomClassList#function-normalize-static)
Converts a class name of any understood type to a desired form.

[constructor](https://bryntum.com/docs/gantt/api/Core/helper/util/DomClassList#function-constructor)
Initializes a new DomClassList.

[clear](https://bryntum.com/docs/gantt/api/Core/helper/util/DomClassList#function-clear)
Clears all class names from this DomClassList instance.

[set](https://bryntum.com/docs/gantt/api/Core/helper/util/DomClassList#function-set)
Sets this DomClassList instance to represent the classes passed as either strings or objects.

[clone](https://bryntum.com/docs/gantt/api/Core/helper/util/DomClassList#function-clone)
Returns a clone of this DomClassList with all the same keys set.

[contains](https://bryntum.com/docs/gantt/api/Core/helper/util/DomClassList#function-contains)
Returns a Boolean value, indicating whether this ClassList has the specified CSS class name.

[trim](https://bryntum.com/docs/gantt/api/Core/helper/util/DomClassList#function-trim)
Analogous to string.trim, returns the string value of this `DomClassList` with no trailing space.

[isEqual](https://bryntum.com/docs/gantt/api/Core/helper/util/DomClassList#function-isEqual)
Compares this DomClassList to another DomClassList (or class name string of space separated classes). If the same class names (regardless of order) are present, the two are considered equal.

So `new DomClassList('foo bar bletch').isEqual('bletch bar foo')` would return `true`

[assign](https://bryntum.com/docs/gantt/api/Core/helper/util/DomClassList#function-assign)
Adds/removes class names according to the passed object's properties.

Properties with truthy values are added. Properties with falsy values are removed.

[assignTo](https://bryntum.com/docs/gantt/api/Core/helper/util/DomClassList#function-assignTo)
Adds/removes this objects classes to the passed `classList` or element.

Properties with truthy values are added. Properties with falsy values are removed.

[add](https://bryntum.com/docs/gantt/api/Core/helper/util/DomClassList#function-add)
Add CSS class(es)

```
myClassList.add('bold', 'small');
```

[remove](https://bryntum.com/docs/gantt/api/Core/helper/util/DomClassList#function-remove)
Remove CSS class(es)

```
myClassList.remove('bold', 'small');
```

[toggle](https://bryntum.com/docs/gantt/api/Core/helper/util/DomClassList#function-toggle)
Toggles the passed CSS class name.

If the `force` parameter is passed, `true` means add the class name, `false` means remove it.

```
myClassList.toggle('bold', isImportant);
```

[split](https://bryntum.com/docs/gantt/api/Core/helper/util/DomClassList#function-split)
Analogous to the `String#split` method, but with no delimiter parameter. This method returns an array containing the individual CSS class names set.
